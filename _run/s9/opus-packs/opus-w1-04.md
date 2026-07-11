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

## GROUP: _overhaul2/lake/cases/Arizona v. Youngblood.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Arizona v. Youngblood
type: case
citation: "488 U.S. 51 (1989)"
parallel_cite: "109 S. Ct. 333; 102 L. Ed. 2d 281"
neutral_cite: 1988 U.S. LEXIS 5404
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-01-23
docket: No. 86-1904
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
  opinion_url: "https://www.courtlistener.com/opinion/112156/arizona-v-youngblood/"
  cluster_id: 112156
  opinion_id: null
  identity_checked: true
lake:
  record_id: Arizona v. Youngblood
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Brady and Giglio]]"
    role: Anchor
related:
  - "[[Brady and Giglio]]"
  - "[[California v. Trombetta]]"
tags:
  - case
  - fourteenth-amendment
  - due-process
  - preservation-of-evidence
  - bad-faith
  - brady
holding: "The government's failure to preserve evidence that is only potentially useful to the defense — as opposed to evidence whose exculpatory value was apparent before it was destroyed — does not deny the defendant due process unless he shows bad faith on the part of the police."
aliases:
  - Arizona v. Youngblood
  - "Arizona v. Youngblood (1988)"
---

# Arizona v. Youngblood

*488 U.S. 51 (1989)* (No. 86-1904) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112156 → combined opinion 112156 (Rehnquist, C.J.; 488 U.S. 51; argued Oct. 11, 1988, decided Nov. 29, 1988). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star *58, confirmed by the dissent's "Ante, at 58"). DATA NOTE: the lake identity carries year 1989 / date 1989-01-23 (CL cluster date_filed), so the projected citation parenthetical reads (1989); the opinion itself was decided Nov. 29, 1988 — flagged for S2. S9 promotes. -->

## Background
A 10-year-old boy was abducted, molested, and repeatedly sodomized; afterward he was examined at a hospital, where a physician collected a rectal swab and preserved the boy's clothing. Investigators did not refrigerate the clothing, and a police criminologist did not perform timely tests on the semen samples. By the time the defense sought to test the samples for blood-group and enzyme markers that might have identified — or excluded — the assailant, the evidence had degraded and could no longer yield useful results. Larry Youngblood was convicted in Pima County, Arizona, of child molestation, sexual assault, and kidnapping. The Arizona Court of Appeals reversed, holding that the State's failure to preserve the testable evidence denied Youngblood due process. The State sought review.

## Issue
Whether the Due Process Clause requires the police to preserve evidentiary material that might have been subjected to tests whose results could have exonerated the defendant — and, if so, whether a failure to do so violates due process absent any showing of bad faith.

## Rule
The Court distinguished evidence whose [[Brady and Giglio|exculpatory]] value is apparent before its destruction — governed by *[[California v. Trombetta|Trombetta]]* — from evidence that is merely "potentially useful," where no more than the possibility of exoneration is at stake. For the latter category the Court fixed the defendant's burden on the police's state of mind rather than on the lost evidence's speculative value: "We therefore hold that unless a criminal defendant can show bad faith on the part of the police, failure to preserve potentially useful evidence does not constitute a denial of due process of law." — 488 U.S. at 58. ^pin-58

## Application
Whatever tests might have been run on the semen samples and clothing, their [[Brady and Giglio|exculpatory]] value was speculative — they might have inculpated Youngblood as easily as cleared him — so the evidence fell in the "potentially useful" category rather than the *[[California v. Trombetta|Trombetta]]* category of apparent [[Brady and Giglio|exculpatory]] value. And the officers' handling of the evidence was, as the Court saw it, at worst negligent; nothing in the record showed the police acted in bad faith or with any awareness that the material could exonerate the accused. Absent that bad faith, the failure to preserve the samples worked no due process violation.

## Conclusion
The judgment of the Arizona Court of Appeals was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Rehnquist, C.J., delivered the opinion of the Court; Stevens, J., concurred in the judgment; Blackmun, J., dissented, joined by Brennan and Marshall, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Youngblood* remains the governing rule for lost or destroyed evidence that is only "potentially useful": the defendant must prove **bad faith**, a demanding standard the Court has adhered to since (see *Illinois v. Fisher* (2004), applying the bad-faith requirement to evidence a defendant had specifically requested). Teach it as the sharp line between the two preservation regimes — *[[California v. Trombetta|Trombetta]]*'s "apparent exculpatory value" duty on one side, and *Youngblood*'s bad-faith gate for merely potentially useful evidence on the other.

## Appears on
- [[Brady and Giglio]] — *Anchor*

## Sources
- [*Arizona v. Youngblood*, 488 U.S. 51 (1989)](https://www.courtlistener.com/opinion/112156/arizona-v-youngblood/) — pinpoint: 58 (Rehnquist, C.J., for the Court; the CL opinion text carries the reporter star `*58` and the dissent cross-references the holding as "Ante, at 58"). Argued Oct. 11, 1988; decided Nov. 29, 1988 (the projected "(1989)" parenthetical follows the lake identity year, which mirrors CourtListener's cluster `date_filed`; flagged for S2). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "32c787943618ea0a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arizona v. Youngblood"}, "payload": {"all": [{"cite": "488 U.S. 51", "page": "51", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "488"}, {"cite": "109 S. Ct. 333", "page": "333", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "102 L. Ed. 2d 281", "page": "281", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "102"}, {"cite": "1988 U.S. LEXIS 5404", "page": "5404", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}], "display": "488 U.S. 51", "official": {"cite": "488 U.S. 51", "page": "51", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "488"}, "official_selection_present": true, "record_id": "Arizona v. Youngblood"}}
{"assertion_id": "42afe60d3899271c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arizona v. Youngblood"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Arizona v. Youngblood", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Arizona v. Youngblood

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Youngblood",
  "status": "under_review",
  "identity": {
    "case_name": "Arizona v. Youngblood",
    "case_name_short": "Youngblood",
    "case_name_full": "Arizona v. Youngblood",
    "input_case_name": "Arizona v. Youngblood",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-01-23",
    "year": 1989,
    "docket": "No. 86-1904",
    "cluster_id": 112156,
    "lead_opinion_id": 9431483,
    "sibling_ids": [],
    "absolute_url": "/opinion/112156/arizona-v-youngblood/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "488 U.S. 51",
      "volume": "488",
      "reporter": "U.S.",
      "page": "51",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 333",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 281",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 5404",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "5404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "488 U.S. 51",
        "volume": "488",
        "reporter": "U.S.",
        "page": "51",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 333",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "333",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 L. Ed. 2d 281",
        "volume": "102",
        "reporter": "L. Ed. 2d",
        "page": "281",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 5404",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "5404",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "488 U.S. 51",
    "official_selection": {
      "court_class": "scotus",
      "selected": "488 U.S. 51",
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
    "date_created": "2026-07-06T13:45:44Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "arizona-v-youngblood--112156",
      "to_record_id": "Arizona v. Youngblood",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Arizona v. Youngblood

```
<opinion type="majority">
<author id="b182-6">Chief Justice Rehnquist</author>
<p id="Ar8">delivered the opinion of the Court.</p>
<p id="b182-7">Respondent Larry Youngblood was convicted by a Pima County, Arizona, jury of child molestation, sexual assault, and kidnaping. The Arizona Court of Appeals reversed his conviction on the ground that the State had failed to preserve semen samples from the victim’s body and clothing. <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/" aria-description="Citation for case: State v. Youngblood">153 Ariz. 50</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/" aria-description="Citation for case: State v. Youngblood">734 P. 2d 592</a></span> (1986). We granted certiorari to consider the extent to which the Due Process Clause of the Fourteenth Amendment requires the State to preserve evidentiary material that might be useful to a criminal defendant.</p>
<p id="b182-8">On October 29, 1983, David L., a 10-year-old boy, attended a church service with his mother. After he left the service at about 9:30 p.m., the boy went to a carnival behind the church, where he was abducted by a middle-aged man of medium height and weight. The assailant drove the boy to a secluded area near a ravine and molested him. He then took the boy to an unidentified, sparsely furnished house where he sodomized the boy four times.. Afterwards, the assailant tied the boy up while he went outside to start his car. Once the assailant started the car, albeit with some difficulty, he returned to the house and again sodomized the boy. The assailant then sent the boy to the bathroom to wash up before he returned him to the carnival. He threatened to kill the boy if he told anyone about the attack. The entire ordeal lasted about <em>YA </em>hours.</p>
<p id="b182-9">After the boy made his way home, his mother took him to Kino Hospital. At the hospital, a physician treated the boy for rectal injuries. The physician also used a “sexual assault kit” to collect evidence of the attack. The Tucson Police De<page-number citation-index="1" label="53">*53</page-number>partment provided such kits to all hospitals in Pima County for use in sexual assault cases. Under standard procedure, the victim of a sexual assault was taken to a hospital, where a physician used the kit to collect evidence. The kit included paper to collect saliva samples, a tube for obtaining a blood sample, microscopic slides for making smears, a set of Q-Tip-like swabs, and a medical examination report. Here, the physician used the swab to collect samples from the boy’s rectum and mouth. He then made a microscopic slide of the samples. The doctor also obtained samples of the boy’s saliva, blood, and hair. The physician did not examine the samples at any time. The police placed the kit in a secure refrigerator at the police station. At the hospital, the police also collected the boy’s underwear and T-shirt. This clothing was not refrigerated or frozen.</p>
<p id="b183-5">Nine days after the attack, on November 7, 1983, the police asked the boy to pick out his assailant from a photographic lineup. The boy identified respondent as the assailant. Respondent was not located by the police until four weeks later; he was arrested on December 9, 1983.</p>
<p id="b183-6">On November 8, 1983, Edward Heller, a police criminologist, examined the sexual assault kit. He testified that he followed standard department procedure, which was to examine the slides and determine whether sexual contact had occurred. After he determined that such contact had occurred, the criminologist did not perform any other tests, although he placed the assault kit back in the refrigerator. He testified that tests to identify blood group substances were not routinely conducted during the initial examination of an assault kit and in only about half of all cases in any event. He did not test the clothing at this time.</p>
<p id="b183-7">Respondent was indicted on charges of child molestation, sexual assault, and kidnaping. The State moved to compel respondent to provide blood and saliva samples for comparison with the material gathered through the use of the sexual assault kit, but the trial court denied the motion on the <page-number citation-index="1" label="54">*54</page-number>ground that the State had not obtained a sufficiently large semen sample to make a valid comparison. The prosecutor then asked the State’s criminologist to perform an ABO blood group test on the rectal swab sample in an attempt to ascertain the blood type of the boy’s assailant. This test failed to detect any blood group substances in the sample.</p>
<p id="b184-5">In January 1985, the police criminologist examined the boy’s clothing for the first time. He found one semen stain on the boy’s underwear and another on the rear of his T-shirt. The criminologist tried to obtain blood group substances from both stains using the ABO technique, but was unsuccessful. He also performed a P-30 protein molecule test on the stains, which indicated that only a small quantity of semen was present on the clothing; it was inconclusive as to the assailant’s identity. The Tucson Police Department had just begun using this test, which was then used in slightly more than half of the crime laboratories in the country.</p>
<p id="b184-6">Respondent’s principal defense at trial was that the boy had erred in identifying him as the perpetrator of the crime. In this connection, both a criminologist for the State and an expert witness for respondent testified as to what might have been shown by tests performed on the samples shortly after they were gathered, or by later tests performed on the samples from the boy’s clothing had the clothing been properly refrigerated. The court instructed the jury that if they found the State had destroyed or lost evidence, they might “infer that the true fact is against the State’s interest.” 10 Tr. 90.</p>
<p id="b184-7">The jury found respondent guilty as charged, but the Arizona Court of Appeals reversed the judgment of conviction. It stated that “‘when identity is an issue at trial and the police permit the destruction of evidence that could eliminate the defendant as the perpetrator, such loss is material to the defense and is a denial of due process.’” <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#54" aria-description="Citation for case: State v. Youngblood">153 Ariz., at 54</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#596" aria-description="Citation for case: State v. Youngblood">734 P. 2d, at 596</a></span>, quoting <em>State </em>v. <em>Escalante, </em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#61" aria-description="Citation for case: State v. Escalante">153 Ariz. 55, 61</a></span>, <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#603" aria-description="Citation for case: State v. Escalante">734 P. 2d 597, 603</a></span> (App. 1986). The Court of Ap<page-number citation-index="1" label="55">*55</page-number>peals concluded on the basis of the expert testimony at trial that timely performance of tests with properly preserved semen samples could have produced results that might have completely exonerated respondent. The Court of Appeals reached this conclusion even though it did “not imply any bad faith on the part of the State.” 153 Ariz., at 54, 734 P. 2d, at 596. The Supreme Court of Arizona denied the State’s petition for review, and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./485/903/">485 U. S. 903</a></span> (1988). We now reverse.</p>
<p id="b185-5">Decision of this case requires us to again consider “what might loosely be called the area of constitutionally guaranteed access to evidence.” <em>United States </em>v. <em>Valenzuela-Bernal, </em><span class="citation" data-id="9428945"><a href="/opinion/110797/united-states-v-valenzuela-bernal/#867" aria-description="Citation for case: United States v. Valenzuela-Bernal">458 U. S. 858, 867</a></span> (1982). In <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), we held that “the suppression by the prosecution of evidence favorable to the accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>Id., </em>at 87</a></span>. In <em>United States </em>v. <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">427 U. S. 97</a></span> (1976), we held that the prosecution had a duty to disclose some evidence of this description even though no requests were made for it, but at the same time we rejected the notion that a “prosecutor has a constitutional duty routinely to deliver his entire file to defense counsel.” <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs"><em>Id., </em>at 111</a></span>; see also <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9425027"><a href="/opinion/108613/moore-v-illinois/#795" aria-description="Citation for case: Moore v. Illinois">408 U. S. 786, 795</a></span> (1972) (“We know of no constitutional requirement that the prosecution make a complete and detailed accounting to the defense of all police investigatory work on a case”).</p>
<p id="b185-6">There is no question but that the State complied with <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span> </em>here. The State disclosed relevant police reports to respondent, which contained information about the existence of the swab and the clothing, and the boy’s examination at the hospital. The State provided respondent’s expert with the laboratory reports and notes prepared by the police criminologist, and respondent’s expert had access to the swab and to the clothing.</p>
<p id="b186-4"><page-number citation-index="1" label="56">*56</page-number>If respondent is to prevail on federal constitutional grounds, then, it must be because of some constitutional duty over and above that imposed by cases such as <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>. </em>Our most recent decision in this area of the law, <em>California </em>v. <em>Trombetta, </em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">467 U. S. 479</a></span> (1984), arose out of a drunken driving prosecution in which the State had introduced test results indicating the concentration of alcohol in the blood of two motorists. The defendants sought to suppress the test results on the ground that the State had failed to preserve the breath samples used in the test. We rejected this argument for several reasons: first, “the officers here were acting in ‘good faith and in accord with their normal practice,’” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#488" aria-description="Citation for case: California v. Trombetta"><em>id., </em>at 488</a></span>, quoting <em>Killian </em>v. <em>United States, </em><span class="citation" data-id="9422314"><a href="/opinion/106310/killian-v-united-states/#242" aria-description="Citation for case: Killian v. United States">368 U. S. 231, 242</a></span> (1961); second, in the light of the procedures actually used the chances that preserved samples would have exculpated the defendants were slim, <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#489" aria-description="Citation for case: California v. Trombetta">467 U. S., at 489</a></span>; and, third, even if the samples might have shown inaccuracy in the tests, the defendants had “alternative means of demonstrating their innocence.” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#490" aria-description="Citation for case: California v. Trombetta"><em>Id., </em>at 490</a></span>. In the present case, the likelihood that the preserved materials would have enabled the defendant to exonerate himself appears to be greater than it was in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>, </em>but here, unlike in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>, </em>the State did not attempt to make any use of the materials in its own case in chief. <footnotemark>*</footnotemark></p>
<p id="b187-4"><page-number citation-index="1" label="57">*57</page-number>Our decisions in related areas have stressed the importance for constitutional purposes of good or bad faith on the part of the Government when the claim is based on loss of evidence attributable to the Government. In <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/" aria-description="Citation for case: United States v. Marion">404 U. S. 307</a></span> (1971), we said that “[n]o actual prejudice to the conduct of the defense is alleged or proved, and there is no showing that the Government intentionally delayed to gain some tactical advantage over appellees or to harass them.” <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#325" aria-description="Citation for case: United States v. Marion"><em>Id., </em>at 325</a></span>; see also <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#790" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 790</a></span> (1977). Similarly, in <em>United States </em>v. <em>Valenzuela-Bemal, supra, </em>we considered whether the Government’s deportation of two witnesses who were illegal aliens violated due process. We held that the prompt deportation of the witnesses was justified “upon the Executive’s good-faith determination that they possess no evidence favorable to the defendant in a criminal prosecution.” <em>Id., </em>at 872.</p>
<p id="b187-5">The Due Process Clause of the Fourteenth Amendment, as interpreted in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>makes the good or bad faith of the State irrelevant when the State fails to disclose to the defendant material exculpatory evidence. But we think the Due Process Clause requires a different result when we deal with the failure of the State to preserve evidentiary material of which no more can be said than that it could have been subjected to tests, the results of which might have exonerated the defendant. Part of the reason for the difference in treatment is found in the observation made by the Court in <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#486" aria-description="Citation for case: California v. Trombetta"><em>Trombetta, supra, </em>at 486</a></span>, that “[w]henever potentially excul<page-number citation-index="1" label="58">*58</page-number>patory evidence is permanently lost, courts face the treacherous task of divining the import of materials whose contents are unknown and, very often, disputed.” Part of it stems from our unwillingness to read the “fundamental fairness” requirement of the Due Process Clause, see <em>Lisenba </em>v. <em>California, </em><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 236</a></span> (1941), as imposing on the police an undifferentiated and absolute duty to retain and to preserve all material that might be of conceivable evidentiary significance in a particular prosecution. We think that requiring a defendant to show bad faith on the part of the police both limits the extent of the police’s obligation to preserve evidence to reasonable bounds and confines it to that class of cases where the interests of justice most clearly require it, <em>i. e., </em>those cases in which the police themselves by their conduct indicate that the evidence could form a basis for exonerating the defendant. We therefore hold that unless a criminal defendant can show bad faith on-the part of the police, failure to preserve potentially useful evidence does not constitute a denial of due process of law.</p>
<p id="b188-5">In this case, the police collected the rectal swab and clothing on the night of the crime; respondent was not taken into custody until six weeks later. The failure of the police to refrigerate the clothing and to perform tests on the semen samples can at worst be described as negligent. None of this information was concealed from respondent at trial, and the evidence — such as it was — was made available to respondent’s expert who declined to perform any tests on the samples. The Arizona Court of Appeals noted in its opinion— and we agree — that there was no suggestion of bad faith on the part of the police. It follows, therefore, from what we have said, that there was no violation of the Due Process Clause.</p>
<p id="b188-6">The Arizona Court of Appeals also referred somewhat obliquely to the State’s “inability to quantitatively test” certain semen samples with the newer P-30 test. 153 Ariz., at 54, 734 P. 2d, at 596. If the court meant by this statement <page-number citation-index="1" label="59">*59</page-number>that the Due Process Clause is violated when the police fail to use a particular investigatory tool, we strongly disagree. The situation here is no different than a prosecution for drunken driving that rests on police observation alone; the defendant is free to argue to the finder of fact that a breathalyzer test might have been exculpatory, but the police do not have a constitutional duty to perform any particular tests.</p>
<p id="b189-5">The judgment of the Arizona Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b189-6">
<em>Reversed.</em>
</p>
<footnote label="*">
<p id="b186-5">In this case, the Arizona Court of Appeals relied on its earlier decision in <em>State </em>v. <em>Escalante, </em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">153 Ariz. 55</a></span>, <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">734 P. 2d 597</a></span> (1986), holding that ‘“when identity is an issue at trial and the police permit destruction of evidence that <em>could eliminate </em>a defendant as the perpetrator, such loss is material to the defense and is a denial of due process.’ ” <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#54" aria-description="Citation for case: State v. Youngblood">153 Ariz. 50, 54</a></span>, <span class="citation" data-id="1205788"><a href="/opinion/1205788/state-v-youngblood/#596" aria-description="Citation for case: State v. Youngblood">734 P. 2d 592, 596</a></span> (1986), quoting <span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/#61" aria-description="Citation for case: State v. Escalante"><em>Escalante, supra, </em>at 61</a></span>, 734 P. 2d, at 603 (emphasis added). The reasoning in <em><span class="citation" data-id="1205714"><a href="/opinion/1205714/state-v-escalante/" aria-description="Citation for case: State v. Escalante">Escalante</a></span> </em>and the instant case mark a sharp departure from <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>in two respects. First, <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>speaks of evidence whose exculpatory value is “apparent.” <span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/#489" aria-description="Citation for case: California v. Trombetta">467 U. S., at 489</a></span>. The possibility that the semen samples could have exculpated respondent if preserved or tested is not enough to satisfy the standard of constitutional materiality in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span>. </em>Second, we made clear in <em><span class="citation" data-id="9429651"><a href="/opinion/111206/california-v-trombetta/" aria-description="Citation for case: California v. Trombetta">Trombetta</a></span> </em>that the exculpatory value of the evidence must be apparent <page-number citation-index="1" label="57">*57</page-number><em>“before </em>the evidence was destroyed.” <em>Ibid, </em>(emphasis added). Here, respondent has not shown that the police knew the semen samples would have exculpated him when they failed to perform certain tests or to refrigerate the boy’s clothing; this evidence was simply an avenue of investigation that might have led in any number of directions. The presence or absence of bad faith by the police for purposes of the Due Process Clause must necessarily turn on the police’s knowledge of the exculpatory value of the evidence at the time it was lost or destroyed. Cf. <em>Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span> (1959).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Arkansas v. Sanders.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Arkansas v. Sanders
type: case
citation: "442 U.S. 753 (1979)"
parallel_cite: "99 S. Ct. 2586; 61 L. Ed. 2d 235"
neutral_cite: 1979 U.S. LEXIS 6
court: U.S.
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-20
docket: 77-1497
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
  opinion_url: "https://www.courtlistener.com/opinion/110119/arkansas-v-sanders/"
  cluster_id: 110119
  opinion_id: null
  identity_checked: true
lake:
  record_id: Arkansas v. Sanders
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Automobile Exception]]"
    role: Historical / origin
related:
  - "[[California v. Acevedo]]"
  - "[[United States v. Chadwick]]"
  - "[[United States v. Ross]]"
tags:
  - case
  - fourth-amendment
  - automobile-exception
  - containers
  - luggage
  - warrant-requirement
  - overruled
  - historical
holding: "The Fourth Amendment's warrant requirement applies to personal luggage taken from a lawfully stopped automobile to the same degree it applies to luggage elsewhere, so police may not search a suitcase seized from a car without a warrant absent exigency — a container rule later overruled by California v. Acevedo (1991)."
---

# Arkansas v. Sanders

*442 U.S. 753 (1979)* (No. 77-1497) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — overruled by [[California v. Acevedo]] (1991)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 110119 → 442 U.S. 753, decided 1979-06-20; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Acting on an informant's tip, Little Rock police watched Sanders retrieve a green suitcase from airport baggage claim, hand it to a companion, and drive off in a taxi with the suitcase in the trunk. Officers stopped the taxi, opened the unlocked suitcase without a warrant, and found marihuana. The Arkansas Supreme Court held the warrantless search unlawful and reversed Sanders's conviction; the State sought review, arguing that the automobile exception justified the search because the luggage came from a lawfully stopped car.

## Issue
Whether, absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]], police must obtain a warrant before searching luggage they have seized from a lawfully stopped automobile.

## Rule
Extending *[[United States v. Chadwick|Chadwick]]*, the Court held that the automobile exception does not reach personal luggage merely because it was taken from a car. Once officers have seized a suitcase and reduced it to their exclusive control, the vehicle's mobility no longer supplies an [[Exigent Circumstances and Hot Pursuit|exigency]], and luggage carries the same expectation of privacy wherever it is found: "In sum, we hold that the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applies to such luggage in other locations." — 442 U.S. at 766. ^pin-766

## Application
The Arkansas Supreme Court had found ample probable cause to believe the suitcase held contraband, but no [[Exigent Circumstances and Hot Pursuit|exigency]]: with the police in control of the taxi and its occupants, there was no risk the suitcase would disappear before a warrant could issue. Because the luggage was already secured, the reasons that excuse a warrant for a moving vehicle did not apply, and the officers should have taken the suitcase to the station and obtained a warrant.

## Conclusion
The judgment of the Supreme Court of Arkansas — suppressing the evidence — was **affirmed**. Powell, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled by [[California v. Acevedo]] (1991).** *Sanders* drew a line between the car (searchable on probable cause) and closed containers within it (protected). The Court abandoned that line: *[[United States v. Ross]]* (1982) held that probable cause to search a vehicle extends to containers inside that might hold the object of the search, and *[[California v. Acevedo|Acevedo]]* then unified the rule, expressly overruling *Sanders* so that police with probable cause may search a container found in a car without a warrant.

*Status note (⚪):* this page was authored from a CourtListener-verified identity stub; the overruled treatment above is well-settled but has not yet completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. It is preserved as **history**, never as live law.

## Appears on
- [[Automobile Exception]] — *Historical / origin*

## Sources
- [*Arkansas v. Sanders*, 442 U.S. 753 (1979)](https://www.courtlistener.com/opinion/110119/arkansas-v-sanders/) — pinpoint: 766 (Opinion of the Court; Powell, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Overruled by *California v. Acevedo*, 500 U.S. 565 (1991) (successor page: [[California v. Acevedo]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d87debf53b92c6ed", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arkansas v. Sanders"}, "payload": {"all": [{"cite": "442 U.S. 753", "page": "753", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "442"}, {"cite": "99 S. Ct. 2586", "page": "2586", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "61 L. Ed. 2d 235", "page": "235", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "1979 U.S. LEXIS 6", "page": "6", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "442 U.S. 753", "official": {"cite": "442 U.S. 753", "page": "753", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "442"}, "official_selection_present": true, "record_id": "Arkansas v. Sanders"}}
{"assertion_id": "ebbcafc13114c972", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arkansas v. Sanders"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Arkansas v. Sanders", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Arkansas v. Sanders

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arkansas v. Sanders",
  "status": "under_review",
  "identity": {
    "case_name": "Arkansas v. Sanders",
    "case_name_short": "Sanders",
    "case_name_full": "Arkansas v. Sanders",
    "input_case_name": "Arkansas v. Sanders",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-20",
    "year": 1979,
    "docket": "77-1497",
    "cluster_id": 110119,
    "lead_opinion_id": 9427641,
    "sibling_ids": [],
    "absolute_url": "/opinion/110119/arkansas-v-sanders/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 753",
      "volume": "442",
      "reporter": "U.S.",
      "page": "753",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2586",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 235",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 6",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 753",
        "volume": "442",
        "reporter": "U.S.",
        "page": "753",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2586",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 235",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 6",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 753",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 753",
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
    "date_created": "2026-07-07T01:36:08Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:36:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "arkansas-v-sanders--110119",
      "to_record_id": "Arkansas v. Sanders",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Arkansas v. Sanders

```
<opinion type="majority">
<author id="b800-9">Me. Justice Powell</author>
<p id="A_Ph">delivered the opinion of the Court.</p>
<p id="Adc">This case presents the question whether, in the absence of exigent circumstances, police are required to obtain a warrant before searching luggage taken from an automobile properly stopped and searched for contraband. We took this case by writ of certiorari to the Supreme Court of Arkansas to resolve some apparent misunderstanding as to the application of our decision in <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), to warrantless searches of luggage seized from automobiles.<footnotemark>1</footnotemark></p>
<p id="b801-4"><page-number citation-index="1" label="755">*755</page-number>I</p>
<p id="b801-5">On April 23, 1976, Officer David Isom of the Little Rock, Ark., Police Department received word from an informant that at 4:35 that afternoon respondent would arrive aboard an American Airlines flight at gate No. 1 of the Municipal Airport of Little Rock. According to the informant, respondent would be carrying a green suitcase containing marihuana. Both Isom and the informant knew respondent well, as in January 1976 the informant had given the Little Rock Police Department information that had led to respondent’s arrest and conviction for possession of marihuana. Acting on the tip, Officer Isom and two other police officers placed the airport under surveillance. As the informant had predicted, respondent duly arrived at gate No. 1. The police watched as respondent deposited some hand luggage in a waiting taxicab, returned to the baggage claim area, and met a man whom police subsequently identified as David Rambo. While Rambo waited, respondent retrieved from the airline baggage service a green suitcase matching that described by the informant. Respondent gave this suitcase to his companion and went outside, where he entered the taxi into which he had put his luggage. Rambo waited a short while in the airport and then joined respondent in the taxi, after placing the green suitcase in the trunk of the vehicle.</p>
<p id="b801-6">When respondent’s taxi drove away carrying respondent, Rambo, and the suitcase, Officer Isom and one of his fellow officers gave pursuit and, with the help of a patrol car, stopped the vehicle several blocks from the airport. At the request of the police, the taxi driver opened the trunk of his vehicle, where the officers found the green suitcase. Without asking the permission of either respondent or Rambo, the police opened the unlocked suitcase and discovered what proved to be 9.3 pounds of marihuana packaged in 10 plastic bags.</p>
<p id="b801-7">On October 14, 1976, respondent and Rambo were charged with possession of marihuana with intent to deliver in viola<page-number citation-index="1" label="756">*756</page-number>tion of Ark. Stat. Ann. § 82-2617 (1976).<footnotemark>2</footnotemark> Before trial, respondent moved to suppress the evidence obtained from the suitcase, contending that the search violated his rights under the Fourth and Fourteenth Amendments. The trial court held a hearing on January 31, 1977, and denied the suppression motion without explanation. After respondent’s conviction by a jury on February 3, 1977, he was sentenced to 10 years in prison and was fined $15,000.</p>
<p id="b802-5">On appeal the Supreme Court of Arkansas reversed respondent’s conviction, ruling that the trial court should have suppressed the marihuana because it was obtained through an unlawful search of the suitcase. <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/" aria-description="Citation for case: Sanders v. State">262 Ark. 595</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/" aria-description="Citation for case: Sanders v. State">559 S. W. 2d 704</a></span> (1977). Relying upon <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra,</a></span> </em>and <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), the court concluded that a warrantless search generally must be supported by “probable cause coupled with exigent circumstances.” 262 Ark., at 599, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 706</a></span>. In the present case, the court found there was ample probable cause for the police officers’ belief that contraband was contained in the suitcase they searched. The court found to be wholly lacking, however, any exigent circumstance justifying the officers’ failure to secure a warrant for the search of the luggage. With the police in control of the automobile and its occupants, there was no danger that the suitcase and its contents would be rendered unavailable to due legal process. The court concluded, therefore, that there was “nothing in this set of circumstances that would lend credence to an assertion of impracticality in obtaining a search warrant.” <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#600" aria-description="Citation for case: Sanders v. State"><em>Id., </em>at 600</a></span>, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#706" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 706</a></span>.<footnotemark>3</footnotemark></p>
<p id="b803-4"><page-number citation-index="1" label="757">*757</page-number>II</p>
<p id="b803-5">Although the general principles applicable to claims of Fourth Amendment violations are well settled, litigation over requests for suppression of highly relevant evidence continues to occupy much of the attention of courts at all levels of the state and federal judiciary. Courts and law enforcement officials often find it difficult to discern the proper application of these principles to individual cases, because the circumstances giving rise to suppression requests can vary almost infinitely. Moreover, an apparently small difference in the factual situation frequently is viewed as a controlling difference in determining Fourth Amendment rights. The present case presents an example. Only two Terms ago, we held that a locked footlocker could not lawfully be searched without a warrant, even though it had been loaded into the trunk of an automobile parked at a curb. <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977). In earlier cases, on the other hand, the Court sustained the constitutionality of warrantless searches of automobiles and their contents under what has become known as the “automobile exception” to the warrant requirement. See, e. <em>g., Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> <em>(1970); Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). We thus are presented with the task of determining whether the warrantless search of respondent's suitcase falls on the <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>or the <em>Chambers/Carroll </em>side of the Fourth Amendment line. Although in a sense this is a line-drawing process, it must be guided by established principles.</p>
<p id="b803-6">We commence with a summary of these principles. The Fourth Amendment protects the privacy and security of per<page-number citation-index="1" label="758">*758</page-number>sons in two important ways. First, it guarantees ''[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” In addition, this Court has interpreted the Amendment to include the requirement that normally searches of private property be performed pursuant to a search warrant issued in compliance with the Warrant Clause.<footnotemark>4</footnotemark> See, <em>e. g., Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 390</a></span> (1978); <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 9</a></span>; <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967); <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span> (1925). In the ordinary case, therefore, a search of private property must be both reasonable and pursuant to a properly issued search warrant. The mere reasonableness of a search, assessed in the light of the surrounding circumstances, is not a substitute for the judicial warrant required under the Fourth Amendment. See <em>United States </em>v. <em>United States District <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">Court, supra.</a></span> </em>As the Court said in <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra,</a></span> </em>at 481:</p>
<blockquote id="b804-5">“The warrant requirement has been a valued part of our constitutional law for decades, and it has determined the result in scores and scores of cases in courts all over this country. It is not an inconvenience to be somehow 'weighed’ against the claims of police efficiency. It is, or should be, an important working part of our machinery of government, operating as a matter of course to check the 'well-intentioned but mistakenly overzealous executive officers’ who are a part of any system of law enforcement.”</blockquote>
<p id="b805-4"><page-number citation-index="1" label="759">*759</page-number>The prominent place the warrant requirement is given in our decisions reflects the “basic constitutional doctrine that individual freedoms will best be preserved through a separation of powers and division of functions among the different branches and levels of Government.” <em>United States </em>v. <em>United States District Court, supra, </em>at 317. By requiring that conclusions concerning probable cause and the scope of a search “be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime,” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948), we minimize the risk of unreasonable assertions of executive authority. See <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948).<footnotemark>5</footnotemark></p>
<p id="b805-5">Nonetheless, there are some exceptions to the warrant requirement. These have been established where it was concluded that the public interest required some flexibility in the application of the general rule that a valid warrant is a prerequisite for a search. See <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 555</a></span> (1976). Thus, a few “jealously and carefully drawn” <footnotemark>6</footnotemark> exceptions provide for those cases where the societal costs of obtaining a warrant, such as danger to law officers or the risk of loss or destruction of evidence, outweigh the reasons for prior recourse to a neutral magistrate. See <em>United States </em>v. <em>United States District Court, supra, </em>at 318. But because each exception to the warrant requirement invariably impinges to some extent on the protective purpose of <page-number citation-index="1" label="760">*760</page-number>the Fourth Amendment, the few situations in which a search may be conducted in the absence of a warrant have been carefully delineated and “the burden is on those seeking the exemption to show the need for it.” <em>United States </em>v. <em>Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951). See <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#762" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 762</a></span> (1969); <em>Katz </em>v. <em>United States, supra, </em>at 357. Moreover, we have limited the reach of each exception to that which is necessary to accommodate the identified needs of society. See <em>Mincey </em>v. <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona"><em>Arizona, supra, </em>at 393</a></span>; <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#15" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 15</a></span>; <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#455" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 455</a></span>.</p>
<p id="b806-5">One of the circumstances in which the Constitution does not require a search warrant is when the police stop an automobile on the street or highway because they have probable cause to believe it contains contraband or evidence of a crime. See <em>United States </em>v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte"><em>Martinez-Fuerte, supra, </em>at 561-562</a></span>; <em>United States </em>v. <em>Ortiz, </em><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#896" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 896</a></span> (1975); <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S. 67, 68</a></span> (1975). As the Court said in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>:</p>
<blockquote id="b806-6">“[T]he guaranty of freedom from unreasonable searches and seizures by the Fourth Amendment has been construed, practically since the beginning of the Government, as recognizing a necessary difference between a search of a store, dwelling house or other structure in respect of which a proper official warrant readily may be obtained, and a search of a ship, motor boat, wagon or automobile, for contraband goods, where it is not practicable to secure a warrant . ...”<footnotemark>7</footnotemark></blockquote>
<p id="b807-4"><page-number citation-index="1" label="761">*761</page-number>There are essentially two reasons for the distinction between automobiles and other private property. First, as the Court repeatedly has recognized, the inherent mobility of automobiles often makes it impracticable to obtain a warrant. See, <em>e. g., United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 12</a></span>; <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#49" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 49-50</a></span>; <em>Carroll </em>v. <em>United States, supra. </em>In addition, the configuration, use, and regulation of automobiles often may dilute the reasonable expectation of privacy that exists with respect to differently situated property. See <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#155" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 155</a></span> (1978) (Powell, J., concurring); <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra;</a></span> South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 368</a></span> (1978); <em>Cardwell </em>v. <em>Lewis, </em><span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441-442</a></span> (1973); <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (Powell, J., concurring).</p>
<p id="b807-5">Ill</p>
<p id="b807-6">In the present case, the State argues that the warrantless search of respondent’s suitcase was proper under <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and its progeny.<footnotemark>8</footnotemark> The police acted properly — indeed commendably — in apprehending respondent and his luggage. They had ample probable cause to believe that respondent’s green suitcase contained marihuana. A previously reliable informant had provided a detailed account of respondent’s expected arrival at the Little Rock Airport, which account proved to be accurate in every detail, including the color of the suitcase in which respondent would be carrying the marihuana. Having probable cause to believe that contraband was being driven away in the taxi, the police were justified in stopping the vehicle, searching it on the spot, and seizing the suitcase they suspected contained contraband. See <em>Chambers </em>v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney"><em>Maroney, supra, </em>at 52</a></span>. At oral argument, respondent conceded that the <page-number citation-index="1" label="762">*762</page-number>stopping of the taxi and the seizure of the suitcase were constitutionally unobjectionable. See Tr. of Oral Arg. 30, 44-46.</p>
<p id="b808-5">The only question, therefore, is whether the police, rather than immediately searching the suitcase without a warrant, should have taken it, along with respondent, to the police station and there obtained a warrant for the search. A lawful search of luggage generally may be performed only pursuant to a warrant. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>we declined an invitation to extend the <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>exception to all searches of luggage, noting that neither of the two policies supporting warrantless searches of automobiles applies to luggage. Here, as in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>the officers had seized the luggage and had it exclusively within their control at the time of the search. Consequently, “there was not the slightest danger that [the luggage] or its contents could have been removed before a valid search warrant could be obtained.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>. And, as we observed in that case, luggage is a common repository for one’s personal effects, and therefore is inevitably associated with the expectation of privacy. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Ibid.</a></span></em></p>
<p id="b808-6">The State argues, nevertheless, that the warrantless search of respondent’s suitcase was proper, not because the property searched was luggage, but rather because it was taken from an automobile lawfully stopped and searched on the street. In effect, the State would have us extend <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>to allow war-rantless searches of everything found within an automobile, as well as of the vehicle itself. As noted above, the Supreme Court of Arkansas found our decision in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>virtually controlling in this case.<footnotemark>9</footnotemark> The State contends, however, that <page-number citation-index="1" label="763">*763</page-number><em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span> </em>does not control because in that case the vehicle had remained parked at the curb where the footlocker had been placed in its trunk and that therefore no argument was made that the “automobile exception” was applicable. This Court has not had occasion previously to rule on the constitutionality of a warrantless search of luggage taken from an automobile lawfully stopped. Rather, the decisions to date have involved searches of some integral part of the automobile. See, <em>e. g., South Dakota </em>v. <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#366" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 366</a></span> (glove compartment); <em>Texas </em>v. <em>White, </em><span class="citation" data-id="9426226"><a href="/opinion/109332/texas-v-white/#68" aria-description="Citation for case: Texas v. White">423 U. S., at 68</a></span> (passenger compartment); <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#437" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 437</a></span> (trunk); <em>Chambers </em>v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#44" aria-description="Citation for case: Chambers v. Maroney"><em>Maroney, supra, </em>at 44</a></span> (concealed compartment under the dashboard); <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#136" aria-description="Citation for case: Carroll v. United States">267 U. S., at 136</a></span> (behind the upholstering of the seats).</p>
<p id="b809-5">We conclude that the State has failed to carry its burden of demonstrating the need for warrantless searches of luggage properly taken from automobiles. A closed suitcase in the trunk of an automobile may be as mobile as the vehicle in which it rides. But as we noted in <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>the exigency of mobility must be assessed at the point immediately before the search — after the police have seized the object to be searched and have it securely within their control.<footnotemark>10</footnotemark> See <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>. Once police have seized a suitcase, as they did here, the extent of its mobility is in no way affected by the place from which it was taken.<footnotemark>11</footnotemark> Accordingly, as a general rule there is <page-number citation-index="1" label="764">*764</page-number>no greater need for warrantless searches of luggage taken from automobiles than of luggage taken from other places.<footnotemark>12</footnotemark></p>
<p id="b810-5">Similarly, a suitcase taken from an automobile stopped on the highway is not necessarily attended by any lesser expectation of privacy than is associated with luggage taken from other locations. One is not less inclined to place private, personal possessions in a suitcase merely because the suitcase is to be carried in an automobile rather than transported by other means or temporarily checked or stored. Indeed, the very purpose of a suitcase is to serve as a repository for personal items when one wishes to transport them.<footnotemark>13</footnotemark> Accord<page-number citation-index="1" label="765">*765</page-number>ingly, the reasons for not requiring a warrant for the search of an automobile do not apply to searches of personal luggage taken by police from automobiles. We therefore find no justification for the extension of <em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span> </em>and its progeny to the warrantless search of one’s personal luggage merely because it was located in an automobile lawfully stopped by the police.<footnotemark>14</footnotemark></p>
<p id="b812-4"><page-number citation-index="1" label="766">*766</page-number>In sum, we hold that the warrant requirement of the Fourth Amendment applies to personal luggage taken from an automobile to the same degree it applies to such luggage in other locations. Thus, insofar as the police are entitled to search such luggage without a warrant, their actions must be justified under some exception to the warrant requirement other than that applicable to automobiles stopped on the highway. Where — as in the present case — the police, without endangering themselves or risking loss of the evidence, lawfully have detained one suspected of criminal activity and secured his suitcase, they should delay the search thereof until after judicial approval has been obtained. In this way, constitutional rights of suspects to prior judicial review of searches will be fully protected.</p>
<p id="b812-5">The judgment of the Arkansas Supreme Court is</p>
<p id="b812-6">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b800-11"> Compare <em>United States </em>v. <em>Finnegan, </em><span class="citation" data-id="351991"><a href="/opinion/351991/united-states-v-gary-charles-finnegan/#641" aria-description="Citation for case: United States v. Gary Charles Finnegan">568 F. 2d 637, 641-642</a></span> (CA9 1977), with <em>United States </em>v. <em>Stevie, </em><span class="citation" data-id="9465095"><a href="/opinion/359034/united-states-v-robert-charles-stevie-united-states-of-america-v-raymond/#1178" aria-description="Citation for case: United States v. Robert Charles Stevie, United States of...">582 F. 2d 1175, 1178-1179</a></span> (CA8 1978) (en banc).</p>
</footnote>
<footnote label="2">
<p id="b802-6"> In addition <em>to the </em>marihuana found in the suitcase, <em>police officers </em>found one ounce of heroin hidden in their patrol car after transporting Rambo to police headquarters. Accordingly, Rambo also was charged with possession of heroin with intent to deliver. Immediately before trial on both counts, the court severed the heroin-possession count for later trial.</p>
</footnote>
<footnote label="3">
<p id="b802-7"> “With the suitcase safely immobilized, it was unreasonable to under<page-number citation-index="1" label="757">*757</page-number>take the additional and greater intrusion of a search without a warrant.” 262 Ark., at 601, <span class="citation" data-id="1666834"><a href="/opinion/1666834/sanders-v-state/#707" aria-description="Citation for case: Sanders v. State">559 S. W. 2d, at 707</a></span>. The court also rejected the State's contention that luggage is entitled to a lesser protection against warrantless searches than are other private areas, such as homes. It noted that suitcases, unlike automobiles, customarily are the repositories for personal effects.</p>
</footnote>
<footnote label="4">
<p id="b804-6"> The Warrant Clause of <em>the </em>Fourth Amendment provides that “no Warrants shall issue but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched and the persons or things to be seized.” The Fourth Amendment has been made fully applicable to the States by the Fourteenth Amendment. See <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949). In this opinion we refer to the Fourth Amendment as it so applies to the State of Arkansas.</p>
</footnote>
<footnote label="5">
<p id="b805-6"> The need for a carefully drawn, limited warrant for searches of private premises was the product in large part of the colonists’ resentment of the writs of assistance to which they were subjected by the English. See <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#8" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 8</a></span> (1977); J. Landynski, Search and Seizure and the Supreme Court 19 (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937). Mr. Justice Frankfurter went so far as to suggest that abuses of the writs of assistance were “so deeply felt by the Colonies as to be one of the potent causes of the Revolution.” <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#69" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 69</a></span> (1950) (dissenting opinion).</p>
</footnote>
<footnote label="6">
<p id="b805-7"> <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499</a></span> (1958).</p>
</footnote>
<footnote label="7">
<p id="b806-7"> The willingness of courts to excuse the absence of a warrant where spontaneous searches are required of a vehicle on the road has led to what is called the “automobile exception” to the warrant requirement, although the exception does not invariably apply whenever automobiles are searched. See, <em>e. g., Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#461" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 461-462</a></span> (1971) (“The word 'automobile' is not a talisman in whose presence the Fourth Amendment fades away and disappears”). See generally Moylan, The Automobile Exception: What it is and What it is not — A Rationale in Search of a Clearer Label, <span class="citation no-link">27 Mercer L. Rev. 987</span> (1976).</p>
</footnote>
<footnote label="8">
<p id="b807-7"> Respondent concedes that the suitcase was his property, see Brief for Respondent 3, and so there is no question of his standing to challenge the search. See <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#387" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 387-388</a></span> (1968). Cf. <em>Rakas </em>v. <em>Illinois, </em><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#148" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 148-149</a></span> (1978).</p>
</footnote>
<footnote label="9">
<p id="b808-7"> The facts of the two cases are similar in several critical respects. In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>a locked, 200-pound footlocker was searched without a warrant after the police, acting with probable cause, had taken it from the trunk of a parked automobile. In the present case, respondent’s comparatively small, unlocked suitcase also had been placed in the trunk of an automobile and was searched without a warrant by police acting upon probable cause. We do not view the difference in the sizes of the footlocker and suitcase as material here; nor did respondent’s failure to lock his suitcase alter its <page-number citation-index="1" label="763">*763</page-number>fundamental character as a repository for personal, private effects. Cf. Note, A Reconsideration of the <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>Expectation of Privacy Test, <span class="citation no-link">76 Mich. L. Rev. 154</span>, 170 (1977).</p>
</footnote>
<footnote label="10">
<p id="b809-7"> The difficulties in seizing and securing automobiles have led the Court to make special allowances for their search. See n. 14, <em>infra.</em></p>
</footnote>
<footnote label="11">
<p id="b809-8"> There may be cases in which the special exigencies of the situation would justify the warrantless search of a suitcase. Cf. <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973) (police had reason to suspect automobile trunk contained a weapon). Generally, however, such exigencies will depend upon the probable contents of the luggage and the suspect’s access to those contents — not upon whether the luggage is taken from an automobile. In <page-number citation-index="1" label="764">*764</page-number>the present case the State has conceded that there were no special exigencies. See Tr. of Oral Arg. 16.</p>
<p id="b810-7">Nor do we consider the constitutionality of searches of luggage incident to the arrest of its possessor. See, e. <em>g., United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973). The State has not argued that respondent's suitcase was searched incident to his arrest, and it appears'that the bag was not within his “immediate control” at the time of the search.</p>
</footnote>
<footnote label="12">
<p id="b810-8"> We have recognized that personal property brought into the country may be searched at the border under circumstances that would not otherwise justify a warrantless search. See <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-617</a></span> (1977). Arkansas does not assert, however, that the search of respondent’s luggage was a border search. Moreover, it may be that the public safety requires luggage to be searched without a warrant in some circumstances — such as when luggage is about to be placed onto an airplane. This presents questions under the Fourth Amendment wholly absent from the present case.</p>
<p id="b810-9">It is beyond question that the police easily could have obtained a warrant to search respondent’s bag if they had taken the suitcase to a magistrate. They had probable cause to believe not only that respondent was carrying marihuana, but also that the contraband was contained in the suitcase that they seized. The State argues that under the circumstances of this case inconvenience to all concerned would have been the only result of deferring search of the suitcase until a warrant was obtained. Those in respondent’s position who find such inconvenience unacceptable may avoid it simply by consenting to the search.</p>
</footnote>
<footnote label="13">
<p id="b810-10"> Not all containers and packages found by police during the course of a search will deserve the full protection of the Fourth Amendment. Thus, some containers (for example a kit of burglar tools or a gun case) by their <page-number citation-index="1" label="765">*765</page-number>very nature cannot support any reasonable expectation of privacy because their contents can be inferred from their outward appearance. Similarly, in some cases the contents of a package will be open to “plain view,” thereby obviating the need for a warrant. See <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968) <em>(per curiam). </em>There will be difficulties in determining which parcels taken from an automobile require a warrant for their search and which do not. Our decision in this case means only that a warrant generally is required before personal luggage can be searched and that the extent to which the Fourth Amendment applies to containers and other parcels depends not at all upon whether they are seized from an automobile.</p>
</footnote>
<footnote label="14">
<p id="b811-6"> We are not persuaded by the State’s argument that, under <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), if the police were entitled to seize the suitcase, then they were entitled to search it. In <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>the Court upheld the warrantless search of an automobile stopped on the highway by police who believed that its occupants had robbed a gasoline station a short time before. The Court recognized that “[a]rguably, because of the preference for a magistrate’s judgment, only the immobilization of the car should be permitted until a search warrant is obtained <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><em>Id., </em>at 51</a></span>. Nonetheless, the Court ruled that a warrantless search was permissible, concluding that there was no constitutional difference between the intrusion of seizing and holding the automobile until a warrant could be obtained, on the one hand, and searching the vehicle without a warrant, on the other.</p>
<p id="b811-8">We view, however, the seizure of a suitcase as quite different from the seizure of an automobile. In <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>if the Court had required seizure and holding of the vehicle, it would have imposed a constitutional requirement upon police departments of all sizes around the country to have available the people and equipment necessary to transport impounded automobiles to some central location until warrants could be secured. Moreover, once seized automobiles were taken from the highway the police would be responsible for providing some appropriate location where they could be kept, with due regard to the safety of the vehicles and their contents, until a magistrate ruled on the application for a warrant. Such <page-number citation-index="1" label="766">*766</page-number>a constitutional requirement therefore would have imposed severe, even impossible, burdens on many police departments. See Note, Warrant-less Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 841-842 (1974). No comparable burdens are likely to exist with respect to the seizure of personal luggage.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Arkansas v. Sullivan.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Arkansas v. Sullivan"
type: case
citation: "532 U.S. 769 (2001)"
parallel_cite: "121 S. Ct. 1876; 149 L. Ed. 2d 994"
neutral_cite: 2001 U.S. LEXIS 4118
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-05-29
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arkansas v. Sullivan
  varies_by_point: false
  scope_note: "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2620699/arkansas-v-sullivan/"
  cluster_id: 2620699
  opinion_id: 9795082
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Progeny"
related: ["[[Whren v. United States]]", "[[Atwater v. City of Lago Vista]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "pretext", "arrest", "per-curiam"]
holding: "An arrest supported by probable cause is reasonable under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren's rule from stops to arrests."
lake:
  record_id: Arkansas v. Sullivan
  status: verified
  projected_at: 2026-07-06
---

# Arkansas v. Sullivan

*532 U.S. 769 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Taylor stopped Kenneth Sullivan for speeding and arrested him for traffic offenses, including a fine-only speeding violation. A search of the vehicle turned up drug-related evidence. Sullivan moved to suppress, arguing that his arrest was "merely a 'pretext and sham to search' him" and therefore violated the Fourth Amendment. The trial court suppressed the evidence and the Arkansas Supreme Court affirmed on rehearing, holding that an arrest — even one supported by probable cause — violates the Fourth Amendment if the officer's true motivation was to conduct a search, and that Arkansas could in any event read the Constitution to provide such protection. The State sought [[Reading and Citing Cases#certiorari-cert|certiorari]], and the Court decided the case [[Common Legal Terms#per-curiam|per curiam]].

## Issue
Whether an arrest supported by probable cause violates the Fourth Amendment because the arresting officer had a pretextual or improper subjective motivation, and whether a state may interpret the Federal Constitution to forbid such pretextual arrests.

## Rule
No to both. The officer's subjective motive is irrelevant to an objectively justified, probable-cause arrest: the Court "held unanimously that '[s]ubjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.'" — 532 U.S. at 772 (quoting *Whren v. United States*). ^pin-772

The Arkansas court's contrary view — that a probable-cause arrest can nevertheless be invalid because of improper motive — "cannot be squared with our decision in *Whren*, in which we noted our 'unwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers.'" — *Id.* ^pin-772b

A state also may not use the *federal* Constitution to impose greater restrictions than this Court requires: while a State is free "as a matter of its own law to impose greater restrictions on police activity," it "may not impose such greater restrictions as a matter of *federal constitutional law* when this Court specifically refrains from imposing them." — *Id.* at 772 (quoting *Oregon v. Hass*). ^pin-772c

## Application
The Arkansas Supreme Court never questioned Officer Taylor's authority to arrest Sullivan for a fine-only traffic violation, and the arrest was supported by probable cause. It suppressed the drug evidence solely on the theory that Taylor's real motivation was to search — exactly the subjective-motive inquiry *[[Whren v. United States|Whren]]* forecloses. Because *[[Whren v. United States|Whren]]*'s rule applies to a probable-cause arrest no less than to a stop, the pretext theory could not invalidate the arrest; and the state court's alternative basis (reading the Federal Constitution more broadly) was foreclosed by *Oregon v. Hass*.

## Conclusion
A probable-cause arrest is reasonable regardless of the officer's pretextual or subjective motive, and a state may not hold otherwise as a matter of federal constitutional law. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Sullivan* extends [[Whren v. United States]] from traffic stops to arrests and pairs with [[Atwater v. City of Lago Vista]] (decided the same day, recognizing authority to arrest for a fine-only offense). The objective-reasonableness, motive-irrelevant principle is reaffirmed in [[Devenpeck v. Alford]].

## Appears on
- [[Traffic Stops]] — *Progeny*

## Sources
- *Arkansas v. Sullivan*, 532 U.S. 769 (2001) (per curiam) — https://www.courtlistener.com/opinion/2620699/arkansas-v-sullivan/ — pinpoint: 772.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d25ee901edd65210", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Arkansas v. Sullivan"}, "payload": {"all": [{"cite": "532 U.S. 769", "page": "769", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "532"}, {"cite": "121 S. Ct. 1876", "page": "1876", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "149 L. Ed. 2d 994", "page": "994", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "149"}, {"cite": "2001 U.S. LEXIS 4118", "page": "4118", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2001"}], "display": "532 U.S. 769", "official": {"cite": "532 U.S. 769", "page": "769", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "532"}, "official_selection_present": true, "record_id": "Arkansas v. Sullivan"}}
{"assertion_id": "2ff559b1f1a6f136", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-772", "record_id": "Arkansas v. Sullivan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-772", "pinpoint_status": "slip-only", "quote": "and therefore violated the Fourth Amendment. The trial court suppressed the evidence and the Arkansas Supreme Court affirmed on rehearing, holding that an arrest — even one supported by probable cause — violates the Fourth Amendment if the officer's true motivation was to conduct a search, and that Arkansas could in any event read the Constitution to provide such protection. The State sought certiorari, and the Court decided the case per curiam. ## Issue Whether an arrest supported by probable cause violates the Fourth Amendment because the arresting officer had a pretextual or improper subjective motivation, and whether a state may interpret the Federal Constitution to forbid such pretextual arrests. ## Rule No to both. The officer's subjective motive is irrelevant to an objectively justified, probable-cause arrest: the Court", "quote_fidelity": "mismatch", "record_id": "Arkansas v. Sullivan", "star_marker": null}}
{"assertion_id": "ac5ec3e0a05e438d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-772c", "record_id": "Arkansas v. Sullivan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-772c", "pinpoint_status": "slip-only", "quote": "as a matter of its own law to impose greater restrictions on police activity,", "quote_fidelity": "mismatch", "record_id": "Arkansas v. Sullivan", "star_marker": null}}
{"assertion_id": "b416a33ee31d23d6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-772b", "record_id": "Arkansas v. Sullivan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-772b", "pinpoint_status": "slip-only", "quote": "cannot be squared with our decision in *Whren*, in which we noted our 'unwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers.'", "quote_fidelity": "mismatch", "record_id": "Arkansas v. Sullivan", "star_marker": null}}
{"assertion_id": "3441b4160c545f6d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Arkansas v. Sullivan"}, "payload": {"as_of_content": "2001-05-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Arkansas v. Sullivan", "scope_note": "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive.", "varies_by_point": false}}
```

### lake record — Arkansas v. Sullivan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arkansas v. Sullivan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arkansas v. Sullivan",
    "case_name_short": "Sullivan",
    "case_name_full": "Arkansas v. Sullivan",
    "input_case_name": "Arkansas v. Sullivan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-05-29",
    "year": 2001,
    "docket": null,
    "cluster_id": 2620699,
    "lead_opinion_id": 9795082,
    "sibling_ids": [
      2620699,
      9795082,
      9795083
    ],
    "absolute_url": "/opinion/2620699/arkansas-v-sullivan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "532 U.S. 769",
      "volume": "532",
      "reporter": "U.S.",
      "page": "769",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 1876",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1876",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 994",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 4118",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 769",
        "volume": "532",
        "reporter": "U.S.",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1876",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1876",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 994",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 4118",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "532 U.S. 769",
    "official_selection": {
      "court_class": "scotus",
      "selected": "532 U.S. 769",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-772",
      "page": null,
      "quote": "and therefore violated the Fourth Amendment. The trial court suppressed the evidence and the Arkansas Supreme Court affirmed on rehearing, holding that an arrest \u2014 even one supported by probable cause \u2014 violates the Fourth Amendment if the officer's true motivation was to conduct a search, and that Arkansas could in any event read the Constitution to provide such protection. The State sought certiorari, and the Court decided the case per curiam. ## Issue Whether an arrest supported by probable cause violates the Fourth Amendment because the arresting officer had a pretextual or improper subjective motivation, and whether a state may interpret the Federal Constitution to forbid such pretextual arrests. ## Rule No to both. The officer's subjective motive is irrelevant to an objectively justified, probable-cause arrest: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-772b",
      "page": null,
      "quote": "cannot be squared with our decision in *Whren*, in which we noted our 'unwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-772c",
      "page": null,
      "quote": "as a matter of its own law to impose greater restrictions on police activity,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arkansas v. Sullivan",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive.",
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
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
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
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vennus v. State",
          "cluster_id": 1496491,
          "cite": [
            "282 S.W.3d 70",
            "2009 Tex. Crim. App. LEXIS 977",
            "2009 WL 1066947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mount v. State",
          "cluster_id": 1505113,
          "cite": [
            "217 S.W.3d 716",
            "2007 Tex. App. LEXIS 1135",
            "2007 WL 484784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bookhardt, Ronnie",
          "cluster_id": 185564,
          "cite": [
            "277 F.3d 558",
            "349 U.S. App. D.C. 317",
            "2002 U.S. App. LEXIS 1224",
            "2002 WL 104531"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Devenpeck v. Alford",
          "cluster_id": 137733,
          "cite": [
            "160 L. Ed. 2d 537",
            "125 S. Ct. 588",
            "543 U.S. 146",
            "2004 U.S. LEXIS 8272"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zellner v. Summerlin",
          "cluster_id": 2707,
          "cite": [
            "494 F.3d 344",
            "2007 U.S. App. LEXIS 17272",
            "2007 WL 2067932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Darruthy v. City of Miami",
          "cluster_id": 76372,
          "cite": [
            "351 F.3d 1080",
            "2003 U.S. App. LEXIS 24048",
            "2003 WL 22799497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 1060443,
          "cite": [
            "55 S.W.3d 515",
            "2001 Tenn. LEXIS 658",
            "2001 WL 1035172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex parte Argent",
          "cluster_id": 5284517,
          "cite": [
            "393 S.W.3d 781",
            "2013 WL 1136518",
            "2013 Tex. Crim. App. LEXIS 532"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond Anthony Miller v. Terry J. Harget",
          "cluster_id": 77447,
          "cite": [
            "458 F.3d 1251",
            "2006 U.S. App. LEXIS 19887",
            "2006 WL 2190555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKay",
          "cluster_id": 2600831,
          "cite": [
            "41 P.3d 59",
            "117 Cal. Rptr. 2d 236",
            "27 Cal. 4th 601",
            "2002 Cal. Daily Op. Serv. 2036",
            "2002 Daily Journal DAR 2485",
            "2002 Cal. LEXIS 624"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'BOYLE v. State",
          "cluster_id": 2629952,
          "cite": [
            "2005 WY 83",
            "117 P.3d 401",
            "2005 Wyo. LEXIS 97",
            "2005 WL 1771001"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Com.",
          "cluster_id": 1058715,
          "cite": [
            "639 S.E.2d 217",
            "273 Va. 26",
            "2007 Va. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sykes",
          "cluster_id": 1278169,
          "cite": [
            "2005 WI 48",
            "279 Wis. 2d 742",
            "695 N.W.2d 277",
            "2005 Wisc. LEXIS 155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America v. Curtis Dennis Callarman",
          "cluster_id": 775859,
          "cite": [
            "273 F.3d 1284",
            "2001 U.S. App. LEXIS 26204",
            "2001 WL 1561112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chris Hartman v. Jeremy Thompson",
          "cluster_id": 4642062,
          "cite": [
            "931 F.3d 471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 1812472,
          "cite": [
            "2007 WI 32",
            "729 N.W.2d 182",
            "299 Wis. 2d 675",
            "2007 Wisc. LEXIS 33"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damato v. State",
          "cluster_id": 2571711,
          "cite": [
            "2003 WY 13",
            "64 P.3d 700",
            "2003 WL 186628"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J & J Construction Co. v. Bricklayers & Allied Craftsmen, Local 1",
          "cluster_id": 848785,
          "cite": [
            "664 N.W.2d 728",
            "468 Mich. 722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mikal Mahdi v. Bryan Stirling",
          "cluster_id": 5308013,
          "cite": [
            "20 F.4th 846"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Franklin",
          "cluster_id": 1225871,
          "cite": [
            "547 F.3d 726",
            "2008 U.S. App. LEXIS 22305",
            "2008 WL 4694937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. Appleby v. Recht",
          "cluster_id": 1309488,
          "cite": [
            "583 S.E.2d 800",
            "213 W. Va. 503"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 2335692,
          "cite": [
            "67 S.W.3d 582",
            "347 Ark. 788",
            "2002 Ark. LEXIS 128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2620699 OR 9795082 OR 9795083) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 119,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 119,
        "triage_read": 6,
        "triage_snippet_classified": 113
      },
      "lane2_top_cited": {
        "query": "cites:(2620699 OR 9795082 OR 9795083)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMSZzPTIyNTUzODcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282620699+OR+9795082+OR+9795083%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2620699 OR 9795082 OR 9795083)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2620699 OR 9795082 OR 9795083)",
    "indexed_citing_opinions": 156,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2620699,
        "count": 139,
        "count_source": "search"
      },
      {
        "opinion_id": 9795082,
        "count": 21,
        "count_source": "search"
      },
      {
        "opinion_id": 9795083,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 234,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arkansas-v-sullivan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2Njc4OSZzPTEwMDQ0Mjg1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282620699+OR+9795082+OR+9795083%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2620699,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 1448404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 1960847,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T18:46:09Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:55:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arkansas v. Sullivan

```
<opinion type="majority">
<author id="b869-10">Per Curiam.</author>
<p id="b869-11">In November 1998, Officer Joe Taylor of the Conway, Arkansas, Police Department stopped respondent Sullivan for speeding and for having an improperly tinted windshield. Taylor approached Sullivan’s vehicle, explained the reason for the stop, and requested Sullivan’s license, regis<page-number citation-index="1" label="770">*770</page-number>tration, and insurance documentation. Upon seeing Sullivan’s license, Taylor realized that he was aware of “ ‘intelligence on [Sullivan] regarding narcotics.’ ” <span class="citation no-link">840 Ark. 318</span>-A, 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S.W. 3d 551, 552</a></span> (2000). When Sullivan opened his ear door in an (unsuccessful) attempt to locate his registration and insurance papers, Taylor noticed a rusted roofing hatchet on the ear’s floorboard. Taylor then arrested Sullivan for speeding, driving without his registration and insurance documentation, carrying a weapon (the roofing hatchet), and improper window tinting.</p>
<p id="b870-5">After another officer arrived and placed Sullivan in his squad car, Officer Taylor conducted an inventory search of Sullivan’s vehicle pursuant to the Conway Police Department’s Vehicle Inventory Policy. Under the vehicle’s armrest, Taylor discovered a bag containing a substance that appeared to him to be methamphetamine as well as numerous items of suspected drug paraphernalia. As a result of the detention and search, Sullivan was charged with various state-law drug offenses, unlawful possession of a weapon, and speeding.</p>
<p id="b870-6">Sullivan moved to suppress the evidence seized from his vehicle on the basis that his arrest was merely a “pretext and sham to search” him and, therefore, violated the Fourth and Fourteenth Amendments to the United States Constitution. Pet. for Cert. 3. The trial court granted the suppression motion and, on the State’s interlocutory appeal, the Arkansas Supreme Court affirmed. <span class="citation multiple-matches"><a href="/c/Ark./340/315/">340 Ark. 315</a></span>, <span class="citation multiple-matches"><a href="/c/S.W.%203d/11/526/">11 S.W. 3d 526</a></span> (2000). The State petitioned for rehearing, contending that the court had erred by taking into account Officer Taylor’s subjective motivation, in disregard of this Court’s opinion in <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span> (1996). Over the dissent of three justices, the court rejected the State’s argument that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>makes “the ulterior motives of police officers . . . irrelevant so long as there is probable cause for the traffic stop” and denied the State’s rehearing petition. 340 Ark., at 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>.</p>
<p id="b871-4"><page-number citation-index="1" label="771">*771</page-number>The Arkansas Supreme Court declined to follow <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>on the ground that “much of it is <em>dicta.” </em>340 Ark., at 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>. The court reiterated the trial judge’s conclusion that “the arrest was pretextual and made for the purpose of searching Sullivan’s vehicle for evidence of a crime,” and observed that “we do not believe that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>disallows” suppression on such a basis. <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Id.,</a></span> </em>at 318-C, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>. Finally, the court asserted that, even if it were to conclude that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>precludes inquiry into an arresting officer’s subjective motivation, “there is nothing that prevents this court from interpreting the U. S. Constitution more broadly than the United States Supreme Court, which has the effect of providing more rights.” 340 Ark., at 318-C, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>.</p>
<p id="b871-5">Because the Arkansas Supreme Court’s decision on rehearing is flatly contrary to this Court’s controlling precedent, we grant the State’s petition for a writ of certiorari and reverse.<footnotemark>*</footnotemark> As an initial matter, we note that the Arkansas Supreme Court never questioned Officer Taylor’s authority to arrest Sullivan for a fine-only traffic violation (speeding), and rightly so. See <em>Atwater </em>v. <em>Lago Vista, ante, </em>p. 318. Rather, the court affirmed the trial judge’s suppression of the drug-related evidence on the theory that Officer Taylor’s arrest of Sullivan, although supported by probable cause, nonetheless violated the Fourth Amendment because Taylor had an improper subjective motivation for making the stop. The Arkansas Supreme Court’s holding to that effect cannot be squared with our decision in <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>, </em>in which we noted our “vmwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers,” <page-number citation-index="1" label="772">*772</page-number>and held unanimously that “[sjubjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U.S., at 813</a></span>. That <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>involved a traffic stop, rather than a custodial arrest, is of no particular moment; indeed, <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>itself relied on <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U.S. 218</a></span> (1973), for the proposition that “a traffic-violation arrest . . . [will] not be rendered invalid by the fact that it was ‘a mere pretext for a narcotics search.’ ” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U. S., at 812-813</a></span>.</p>
<p id="b872-5">The Arkansas Supreme Court’s alternative holding, that it may interpret the United States Constitution to provide greater protection than this Court’s own federal constitutional precedents provide, is foreclosed by <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U.S. 714</a></span> (1975). There, we observed that the Oregon Supreme Court’s statement that it could “‘interpret the Fourth Amendment more restrietively than interpreted by the United States Supreme Court’” was “not the law and surely must be an inadvertent error.” <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass"><em>Id., </em>at 719, n. 4</a></span>. We reiterated in <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>that while “a State is free <em>as a matter of its own law </em>to impose greater restrictions on police activity than those this Court holds to be necessary upon federal constitutional standards,” it “may not impose such greater restrictions as a matter of <em>federal constitutional law </em>when this Court specifically refrains from imposing them.” <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass"><em>Id., </em>at 719</a></span>.</p>
<p id="b872-6">The judgment of the Arkansas Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b872-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b871-6"> Sullivan’s motion for leave to proceed <em>informa pauperis </em>is granted. We have jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span> notwithstanding the absence of final judgment in the underlying prosecution. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#651" aria-description="Citation for case: New York v. Quarles">467 U.S. 649, 651, n. 1</a></span> (1984) (“[S]hould the State convict respondent at trial, its claim that certain evidence was wrongfully suppressed will be moot. Should respondent be acquitted at trial, the State will be precluded from pressing its federal claim again on appeal”).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Ashcraft v. Tennessee.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Ashcraft v. Tennessee"
type: case
citation: "322 U.S. 143 (1944)"
parallel_cite: "64 S. Ct. 921; 88 L. Ed. 1192"
neutral_cite: 1944 U.S. LEXIS 782
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1944
date_decided: 1944-05-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1944-05-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ashcraft v. Tennessee
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/"
  cluster_id: 103981
  opinion_id: 103981
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "interrogation"]
holding: "Thirty-six hours of continuous, relay interrogation without sleep is \"inherently coercive,\" rendering the resulting confession…"
lake:
  record_id: Ashcraft v. Tennessee
  status: verified
  projected_at: 2026-07-09
---

# Ashcraft v. Tennessee

*322 U.S. 143 (1944)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Ashcraft was suspected of arranging his wife's murder. Police held him in custody and questioned him for thirty-six hours straight — incommunicado, without sleep or rest, by relays of experienced investigators and lawyers under electric lights. He denied involvement throughout but allegedly confessed at the end. The confession was the principal evidence at his murder trial, and he was convicted.

## Issue
Whether a confession obtained after thirty-six hours of continuous, incommunicado interrogation by relays of officers, without rest or sleep, can be deemed voluntary — or whether such interrogation is inherently coercive so that the resulting confession violates Fourteenth Amendment due process.

## Rule
Such prolonged, relentless interrogation is inherently coercive and yields an involuntary confession: "We think a situation such as that here shown by uncontradicted evidence is so inherently coercive that its very existence is irreconcilable with the possession of mental freedom by a lone suspect against whom its full coercive force is brought to bear." — 322 U.S. at 154. ^pin-154

"The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession." — [*Id.* at 155](https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/#:~:text=The%20Constitution%20of%20the%20United). ^pin-155

## Application
Ashcraft was interrogated for thirty-six hours without rest or sleep, held incommunicado, by relays of officers and lawyers — a situation the Court found inherently coercive and irreconcilable with the mental freedom of a lone suspect. On these facts the resulting confession could not be treated as voluntary, and its use to convict him violated due process.

## Conclusion
The confession was the product of inherently coercive interrogation and could not support the conviction; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ashcraft* is a foundational due-process voluntariness decision establishing that prolonged, relentless custodial interrogation can be inherently coercive. The voluntariness inquiry later settled into a totality-of-the-circumstances test that requires coercive police activity (see [[Colorado v. Connelly]]), and custodial interrogation acquired separate procedural safeguards under *[[Miranda v. Arizona|Miranda]]*.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *Ashcraft v. Tennessee*, 322 U.S. 143 (1944) — https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/ — pinpoints: 154, 155.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f87471a4fa454f3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ashcraft v. Tennessee"}, "payload": {"all": [{"cite": "322 U.S. 143", "page": "143", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "322"}, {"cite": "64 S. Ct. 921", "page": "921", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "64"}, {"cite": "88 L. Ed. 1192", "page": "1192", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "1944 U.S. LEXIS 782", "page": "782", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1944"}], "display": "322 U.S. 143", "official": {"cite": "322 U.S. 143", "page": "143", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "322"}, "official_selection_present": true, "record_id": "Ashcraft v. Tennessee"}}
{"assertion_id": "1394a4920eef9766", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-155", "record_id": "Ashcraft v. Tennessee"}, "payload": {"fragment": "#:~:text=The%20Constitution%20of%20the%20United", "page": null, "pin_id": "pin-155", "pinpoint_status": "star-verified", "quote": "The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession.", "quote_fidelity": "matched", "record_id": "Ashcraft v. Tennessee", "star_marker": "155"}}
{"assertion_id": "2c2ec2cf7c0c98c6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-154", "record_id": "Ashcraft v. Tennessee"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-154", "pinpoint_status": "slip-only", "quote": "--- # Ashcraft v. Tennessee *322 U.S. 143 (1944)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Ashcraft was suspected of arranging his wife's murder. Police held him in custody and questioned him for thirty-six hours straight — incommunicado, without sleep or rest, by relays of experienced investigators and lawyers under electric lights. He denied involvement throughout but allegedly confessed at the end. The confession was the principal evidence at his murder trial, and he was convicted. ## Issue Whether a confession obtained after thirty-six hours of continuous, incommunicado interrogation by relays of officers, without rest or sleep, can be deemed voluntary — or whether such interrogation is inherently coercive so that the resulting confession violates Fourteenth Amendment due process. ## Rule Such prolonged, relentless interrogation is inherently coercive and yields an involuntary confession:", "quote_fidelity": "mismatch", "record_id": "Ashcraft v. Tennessee", "star_marker": null}}
{"assertion_id": "e26eea949cd5ea6c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ashcraft v. Tennessee"}, "payload": {"as_of_content": "1944-05-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Ashcraft v. Tennessee", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Ashcraft v. Tennessee

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ashcraft v. Tennessee",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ashcraft v. Tennessee",
    "case_name_short": "Ashcraft",
    "case_name_full": "ASHCRAFT Et Al. v. TENNESSEE",
    "input_case_name": "Ashcraft v. Tennessee",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1944-05-01",
    "year": 1944,
    "docket": null,
    "cluster_id": 103981,
    "lead_opinion_id": 103981,
    "sibling_ids": [
      103981,
      9419494,
      9419495
    ],
    "absolute_url": "/opinion/103981/ashcraft-v-tennessee/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "322 U.S. 143",
      "volume": "322",
      "reporter": "U.S.",
      "page": "143",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "64 S. Ct. 921",
        "volume": "64",
        "reporter": "S. Ct.",
        "page": "921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 1192",
        "volume": "88",
        "reporter": "L. Ed.",
        "page": "1192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1944 U.S. LEXIS 782",
        "volume": "1944",
        "reporter": "U.S. LEXIS",
        "page": "782",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "322 U.S. 143",
        "volume": "322",
        "reporter": "U.S.",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 S. Ct. 921",
        "volume": "64",
        "reporter": "S. Ct.",
        "page": "921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 1192",
        "volume": "88",
        "reporter": "L. Ed.",
        "page": "1192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1944 U.S. LEXIS 782",
        "volume": "1944",
        "reporter": "U.S. LEXIS",
        "page": "782",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "322 U.S. 143",
    "official_selection": {
      "court_class": "scotus",
      "selected": "322 U.S. 143",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-154",
      "page": null,
      "quote": "--- # Ashcraft v. Tennessee *322 U.S. 143 (1944)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Ashcraft was suspected of arranging his wife's murder. Police held him in custody and questioned him for thirty-six hours straight \u2014 incommunicado, without sleep or rest, by relays of experienced investigators and lawyers under electric lights. He denied involvement throughout but allegedly confessed at the end. The confession was the principal evidence at his murder trial, and he was convicted. ## Issue Whether a confession obtained after thirty-six hours of continuous, incommunicado interrogation by relays of officers, without rest or sleep, can be deemed voluntary \u2014 or whether such interrogation is inherently coercive so that the resulting confession violates Fourteenth Amendment due process. ## Rule Such prolonged, relentless interrogation is inherently coercive and yields an involuntary confession:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-155",
      "page": null,
      "quote": "The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession.",
      "star_marker": "155",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15902,
      "fragment": "#:~:text=The%20Constitution%20of%20the%20United",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1944-05-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ashcraft v. Tennessee",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Charley B. Haswood",
          "cluster_id": 784327,
          "cite": [
            "350 F.3d 1024",
            "2003 Cal. Daily Op. Serv. 10282",
            "62 Fed. R. Serv. 1478",
            "2003 U.S. App. LEXIS 24181",
            "2003 WL 22833048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 156277,
          "cite": [
            "142 F.3d 1243",
            "1998 Colo. J. C.A.R. 2038",
            "1998 U.S. App. LEXIS 8245",
            "1998 WL 207912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cahill",
          "cluster_id": 1244769,
          "cite": [
            "853 P.2d 1037",
            "5 Cal. 4th 478",
            "20 Cal. Rptr. 2d 582",
            "93 Daily Journal DAR 8304",
            "93 Cal. Daily Op. Serv. 4902",
            "1993 Cal. LEXIS 3087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte McCary",
          "cluster_id": 1793877,
          "cite": [
            "528 So. 2d 1133",
            "1988 WL 10157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Lane Jurek v. W. J. Estelle, Jr., Director, Texas Department of Corrections, Respondent",
          "cluster_id": 379222,
          "cite": [
            "623 F.2d 929",
            "1980 U.S. App. LEXIS 14967"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Schmidt",
          "cluster_id": 354373,
          "cite": [
            "573 F.2d 1057"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 5682513,
          "cite": [
            "42 N.Y.2d 35",
            "364 N.E.2d 1318",
            "396 N.Y.S.2d 625",
            "1977 N.Y. LEXIS 2096"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Lee Thomas v. State of North Carolina and Mr. Bill Mahoney, Superintendent",
          "cluster_id": 298888,
          "cite": [
            "447 F.2d 1320",
            "1971 U.S. App. LEXIS 8130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Napue v. Illinois",
          "cluster_id": 105912,
          "cite": [
            "3 L. Ed. 2d 1217",
            "79 S. Ct. 1173",
            "360 U.S. 264",
            "1959 U.S. LEXIS 811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. New York",
          "cluster_id": 112601,
          "cite": [
            "114 L. Ed. 2d 395",
            "111 S. Ct. 1859",
            "500 U.S. 352",
            "1991 U.S. LEXIS 2913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michel v. Louisiana",
          "cluster_id": 105333,
          "cite": [
            "100 L. Ed. 2d 83",
            "76 S. Ct. 158",
            "350 U.S. 91",
            "1955 U.S. LEXIS 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shelley v. Kraemer",
          "cluster_id": 104545,
          "cite": [
            "92 L. Ed. 2d 1161",
            "68 S. Ct. 836",
            "334 U.S. 1",
            "1948 U.S. LEXIS 2764",
            "3 A.L.R. 2d 441",
            "92 L. Ed. 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrity v. New Jersey",
          "cluster_id": 107336,
          "cite": [
            "17 L. Ed. 2d 562",
            "87 S. Ct. 616",
            "385 U.S. 493",
            "1967 U.S. LEXIS 2882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haynes v. Washington",
          "cluster_id": 106625,
          "cite": [
            "10 L. Ed. 2d 513",
            "83 S. Ct. 1336",
            "373 U.S. 503",
            "1963 U.S. LEXIS 1439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacobellis v. Ohio",
          "cluster_id": 106877,
          "cite": [
            "12 L. Ed. 2d 793",
            "84 S. Ct. 1676",
            "378 U.S. 184",
            "1964 U.S. LEXIS 822",
            "28 Ohio Op. 2d 101"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blackburn v. Alabama",
          "cluster_id": 105977,
          "cite": [
            "4 L. Ed. 2d 242",
            "80 S. Ct. 274",
            "361 U.S. 199",
            "1960 U.S. LEXIS 1766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spano v. New York",
          "cluster_id": 105917,
          "cite": [
            "3 L. Ed. 2d 1265",
            "79 S. Ct. 1202",
            "360 U.S. 315",
            "1959 U.S. LEXIS 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. Ohio",
          "cluster_id": 104491,
          "cite": [
            "92 L. Ed. 2d 224",
            "68 S. Ct. 302",
            "332 U.S. 596",
            "1948 U.S. LEXIS 2643"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. North Carolina",
          "cluster_id": 107261,
          "cite": [
            "16 L. Ed. 2d 895",
            "86 S. Ct. 1761",
            "384 U.S. 737",
            "1966 U.S. LEXIS 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103981 OR 9419494 OR 9419495) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NjkxNTIwMDAwMCZzPTIzNzQwODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103981+OR+9419494+OR+9419495%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(103981 OR 9419494 OR 9419495)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDcmcz0xMDQ0NTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103981+OR+9419494+OR+9419495%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103981 OR 9419494 OR 9419495)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103981 OR 9419494 OR 9419495)",
    "indexed_citing_opinions": 436,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103981,
        "count": 407,
        "count_source": "search"
      },
      {
        "opinion_id": 9419494,
        "count": 42,
        "count_source": "search"
      },
      {
        "opinion_id": 9419495,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 693,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ashcraft-v-tennessee.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU4MTUzNTgmcz02MjQxNzczJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103981+OR+9419494+OR+9419495%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103981,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 101593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 102408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 1322156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 1545293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 3891773,
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
    "date_created": "2026-07-04T18:55:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ashcraft v. Tennessee

```
<div>
<center><b><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U.S. 143</a></span> (1944)</b></center>
<center><h1>ASHCRAFT ET AL.<br>
v.<br>
TENNESSEE.</h1></center>
<center>No. 391.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 28, 1944.</center>
<center>Decided May 1, 1944.</center>
CERTIORARI TO THE SUPREME COURT OF TENNESSEE.
<p><span class="star-pagination">*144</span> <i>Messrs. James F. Bickers</i> and <i>Grover N. McCormick</i> for petitioners.</p>
<p><i>Mr. Nat Tipton,</i> with whom <i>Mr. Roy H. Beeler,</i> Attorney General of Tennessee, was on the brief, for respondent.</p>
<p>MR. JUSTICE BLACK delivered the opinion of the Court.</p>
<p>About three o'clock on the morning of Thursday, June 5, 1941, Mrs. Zelma Ida Ashcraft got in her automobile at her home in Memphis, Tennessee, and set out on a trip to visit her mother's home in Kentucky. Late in the afternoon of the same day, her car was observed a few miles out of Memphis, standing on the wrong side of a road which she would likely have taken on her journey. Just off the road, in a slough, her lifeless body was found. On her head were cut places inflicted by blows sufficient to have caused her death. Petitioner Ware, age 20, a Negro, was indicted in a state court and found guilty of her murder. Petitioner Ashcraft, age 45, a white man, husband of the deceased, charged with having hired Ware to commit the murder, was tried jointly with Ware and convicted as an accessory before the fact. Both were sentenced to ninety-nine years in the state penitentiary. <span class="star-pagination">*145</span> The Supreme Court of Tennessee affirmed the convictions.</p>
<p>In applying to us for certiorari, Ware and Ashcraft urged that alleged confessions were used at their trial which had been extorted from them by state law enforcement officers in violation of the Fourteenth Amendment, and that "solely and alone" on the basis of these confessions they had been convicted. Their contentions raised a federal question which the record showed to be substantial and we brought both cases here for review. Upon oral argument before this Court Tennessee's legal representatives conceded that the convictions could not be sustained without the confessions but defended their use upon the ground that they were not compelled but were "freely and voluntarily made."</p>
<p>The record discloses that neither the trial court nor the Tennessee Supreme Court actually held as a matter of fact that petitioners' confessions were "freely and voluntarily made." The trial court heard evidence on the issue out of the jury's hearing, but did not itself determine from that evidence that the confessions were voluntary. Instead it overruled Ashcraft's objection to the use of his alleged confession with the statement that, "This Court is not able to hold, as a matter of law, that reasonable minds might not differ on the question of whether or not that alleged confession was voluntarily obtained." And it likewise overruled Ware's objection to use of his alleged confession, stating that "the reasonable minds of twelve men might . . . differ as to . . . whether Ware's confession was voluntary, and . . . therefore, that is a question of fact for the jury to pass on."<sup>[1]</sup> Nor did the <span class="star-pagination">*146</span> State Supreme Court review the evidence pertaining to the confessions and affirmatively hold them voluntary. In sustaining the petitioners' convictions, one Justice dissenting, it went no further than to point out that, "The trial judge . . . held . . . he could not say that the confessions were not voluntarily made and, therefore, permitted them to go to the jury," and to declare that it, likewise, was "unable to say that the confessions were not freely and voluntarily made."<sup>[2]</sup></p>
<p>If, therefore, the question of the voluntariness of the two confessions was actually decided at all it was by the jury. And the jury was charged generally on the subject of the two confessions as follows:</p>
<p>"I further charge you that if verbal or written statements made by the defendants freely and voluntarily and without fear of punishment or hope of reward, have been proven to you in this case, you may take them into consideration with all of the other facts and circumstances in the case. . . . In statements made at the time of the arrest, you may take into consideration the condition of the minds of the prisoners owing to their arrest and <span class="star-pagination">*147</span> whether they were influenced by motives of hope or fear, to make the statements. Such a statement is competent evidence against the defendant who makes it and is not competent evidence against the other defendant . . . You cannot consider it for any purpose against the other defendant."</p>
<p>Concerning Ashcraft's alleged confession this general charge constituted the sole instruction to the jury.<sup>[3]</sup> But with regard to Ware's alleged confession the jury further was instructed:</p>
<p>"It is his [Ware's] further theory that he was induced by the fear of violence at the hands of a mob and by fear of the officers of the law to confess his guilt of the crime charged against him, but that such confession was false and that he had nothing whatsoever to do with, and no knowledge of the alleged crime. If you believe the theory of the defendant, Ware, . . . it is your duty to acquit him."</p>
<p>Having submitted the two alleged confessions to the jury in this manner, the trial court instructed the jury that: "What the proof may show you, if anything, that the defendants have said against themselves, the law presumes to be true, but anything the defendants have said in their own behalf, you are not obliged to believe. . . ."</p>
<p>This treatment of the confessions by the two state courts, the manner of the confessions' submission to the jury, and the emphasis upon the great weight to be given confessions make all the more important the kind of "independent examination" of petitioners' claims which, in <span class="star-pagination">*148</span> any event, we are bound to make. <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#237" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 237-238</a></span>. Our duty to make that examination could not have been "foreclosed by the finding of a court, or the verdict of a jury, or both." <i><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">Id.</a></span></i> We proceed therefore to consider the evidence relating to the circumstances out of which the alleged confessions came.</p>
<p><i>First, as to Ashcraft.</i> Ashcraft was born on an Arkansas farm. At the age of eleven he left the farm and became a farm hand working for others. Years later he gravitated into construction work, finally becoming a skilled dragline and steam-shovel operator. Uncontradicted evidence in the record was that he had acquired for himself "an excellent reputation." In 1929 he married the deceased Zelma Ida Ashcraft. Childless, they accumulated, apparently through Ashcraft's earnings, a very modest amount of jointly held property including bank accounts and an equity in the home in which they lived. The Supreme Court of Tennessee found "nothing to show but what the home life of Ashcraft and the deceased was pleasant and happy." Several of Mrs. Ashcraft's friends who were guests at the Ashcraft home on the night before her tragic death testified that both husband and wife appeared to be in a happy frame of mind.</p>
<p>The officers first talked to Ashcraft about 6 P.M. on the day of his wife's murder as he was returning home from work. Informed by them of the tragedy, he was taken to an undertaking establishment to identify her body which previously had been identified only by a driver's license. From there he was taken to the county jail where he conferred with the officers until about 2 A.M. No clues of ultimate value came from this conference, though it did result in the officers' holding and interrogating the Ashcrafts' maid and several of her friends. During the following week the officers made extensive investigations in Ashcraft's neighborhood and <span class="star-pagination">*149</span> elsewhere and further conferred with Ashcraft himself on several occasions, but none of these activities produced tangible evidence pointing to the identity of the murderer.</p>
<p>Then, early in the evening of Saturday, June 14, the officers came to Ashcraft's home and "took him into custody." In the words of the Tennessee Supreme Court,</p>
<p>"They took him to an office or room on the northwest corner of the fifth floor of the Shelby County jail. This office is equipped with all sorts of crime and detective devices such as a fingerprint outfit, cameras, high-powered lights, and such other devices as might be found in a homicide investigating office. . .. It appears that the officers placed Ashcraft at a table in this room on the fifth floor of the county jail with a light over his head and began to quiz him. They questioned him in relays until the following Monday morning, June 16, 1941, around ninethirty or ten o'clock. It appears that Ashcraft from Saturday evening at seven o'clock until Monday morning at approximately nine-thirty never left this homicide room on the fifth floor."<sup>[4]</sup></p>
<p>Testimony of the officers shows that the reason they questioned Ashcraft "in relays" was that they became so tired they were compelled to rest. But from 7:00 Saturday evening until 9:30 Monday morning Ashcraft had no rest. One officer did say that he gave the suspect a single five minutes' respite, but except for this five minutes the procedure consisted of one continuous stream of questions.</p>
<p>As to what happened in the fifth-floor jail room during this thirty-six hour secret examination the testimony <span class="star-pagination">*150</span> follows the usual pattern and is in hopeless conflict.<sup>[5]</sup> Ashcraft swears that the first thing said to him when he was taken into custody was, "Why in hell did you kill your wife?"; that during the course of the examination he was threatened and abused in various ways; and that as the hours passed his eyes became blinded by a powerful electric light, his body became weary, and the strain on his nerves became unbearable.<sup>[6]</sup> The officers, on the other hand, swear that throughout the questioning they were kind and considerate. They say that they did not accuse Ashcraft of the murder until four hours after he was brought to the jail building, though they freely admit that from that time on their barrage of questions was constantly directed at him on the assumption that he was <span class="star-pagination">*151</span> the murderer. Together with other persons whom they brought in on Monday morning to witness the culmination of the thirty-six hour ordeal the officers declare that at that time Ashcraft was "cool," "calm," "collected," "normal"; that his vision was unimpaired and his eyes not bloodshot; and that he showed no outward signs of being tired or sleepy.</p>
<p>As to whether Ashcraft actually confessed, there is a similar conflict of testimony. Ashcraft maintains that although the officers incessantly attempted by various tactics of intimidation to entrap him into a confession, not once did he admit knowledge concerning or participation in the crime. And he specifically denies the officers' statements that he accused Ware of the crime, insisting that in response to their questions he merely gave them the name of Ware as one of several men who occasionally had ridden with him to work. The officers' version of what happened, however, is that about 11 P.M. on Sunday night, after twenty-eight hours' constant questioning, Ashcraft made a statement that Ware had overpowered him at his home and abducted the deceased, and was probably the killer. About midnight the officers found Ware and took him into custody, and, according to their testimony, Ware made a self-incriminating statement as of early Monday morning, and at 5:40 A.M. signed by mark a written confession in which appeared the statement that Ashcraft had hired him to commit the murder. This alleged confession of Ware was read to Ashcraft about six o'clock Monday morning, whereupon Ashcraft is said substantially to have admitted its truth in a detailed statement taken down by a reporter. About 9:30 Monday morning a transcript of Ashcraft's purported statement was read to him. The State's position is that he affirmed its truth but refused to sign the transcript, saying that he first wanted to consult his lawyer. As to <span class="star-pagination">*152</span> this latter 9:30 episode the officers' testimony is reinforced by testimony of the several persons whom they brought in to witness the end of the examination.</p>
<p>In reaching our conclusion as to the validity of Ashcraft's confession we do not resolve any of the disputed questions of fact relating to the details of what transpired within the confession chamber of the jail or whether Ashcraft actually did confess.<sup>[7]</sup> Such disputes, we may say, are an inescapable consequence of secret inquisitorial practices. And always evidence concerning the inner details of secret inquisitions<sup>[8]</sup> is weighted against an accused, <span class="star-pagination">*153</span> particularly where, as here, he is charged with a brutal crime, or where, as in many other cases, his supposed offense bears relation to an unpopular economic, political, or religious cause.</p>
<p>Our conclusion is that if Ashcraft made a confession it was not voluntary but compelled. We reach this conclusion from facts which are not in dispute at all. Ashcraft, a citizen of excellent reputation, was taken into custody by police officers. Ten days' examination of the Ashcrafts' maid, and of several others, in jail where they were held, had revealed nothing whatever against Ashcraft. Inquiries among his neighbors and business associates likewise had failed to unearth one single tangible clue pointing to his guilt. For thirty-six hours after Ashcraft's seizure during which period he was held incommunicado, without sleep or rest, relays of officers, experienced investigators, and highly trained lawyers questioned him without respite. From the beginning of the questioning at 7 o'clock on Saturday evening until 6 o'clock on Monday morning Ashcraft denied that he had anything to do with the murder of his wife. And at a hearing <span class="star-pagination">*154</span> before a magistrate about 8:30 Monday morning Ashcraft pleaded not guilty to the charge of murder which the officers had sought to make him confess during the previous thirty-six hours.</p>
<p>We think a situation such as that here shown by uncontradicted evidence is so inherently coercive that its very existence is irreconcilable with the possession of mental freedom by a lone suspect against whom its full coercive force is brought to bear.<sup>[9]</sup> It is inconceivable that any court of justice in the land, conducted as our courts are, open to the public, would permit prosecutors serving in relays to keep a defendant witness under continuous cross-examination for thirty-six hours without rest or sleep in an effort to extract a "voluntary" confession. Nor can we, consistently with Constitutional due process of law, hold voluntary a confession where prosecutors do the same thing away from the restraining influences of a public trial in an open court room.<sup>[10]</sup></p>
<p><span class="star-pagination">*155</span> The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession.<sup>[11]</sup> There have been, and are now, certain foreign nations with governments dedicated to an opposite policy: governments which convict individuals with testimony obtained by police organizations possessed of an unrestrained power to seize persons suspected of crimes against the state, hold them in secret custody, and wring from them confessions by physical or mental torture. So long as the Constitution remains the basic law of our Republic, America will not have that kind of government.</p>
<p><i>Second, as to Ware.</i> Ashcraft and Ware were jointly tried, and were convicted on the theory that Ashcraft hired Ware to perform the murder. Ware's conviction was sustained by the Tennessee Supreme Court on the assumption that Ashcraft's confession was properly admitted and his conviction valid. Whether it would have been sustained had the court reached the conclusion we have reached as to Ashcraft we cannot know. Doubt as to what the state court would have done under the changed <span class="star-pagination">*156</span> circumstances brought about by our reversal of its decision as to Ashcraft is emphasized by the position of the State's representatives in this Court. They have asked that if we reverse Ashcraft's conviction we also reverse Ware's.</p>
<p>In disposing of cases before us it is our responsibility to make such disposition as justice may require. "And in determining what justice does require, the Court is bound to consider any change, either in fact or in law, which has supervened since the judgment was entered." <i>Patterson</i> v. <i>Alabama,</i> <span class="citation" data-id="102408"><a href="/opinion/102408/patterson-v-alabama/#607" aria-description="Citation for case: Patterson v. Alabama">294 U.S. 600, 607</a></span>; <i>State Tax Commission</i> v. <i>Van Cott,</i> <span class="citation" data-id="103175"><a href="/opinion/103175/state-tax-commission-v-van-cott/#515" aria-description="Citation for case: State Tax Commission v. Van Cott">306 U.S. 511, 515-516</a></span>. Application of this guiding principle to the case at hand requires that we send Ware's case back to the Tennessee Supreme Court. Should that Court in passing on Ware's conviction in the light of our ruling as to Ashcraft adopt the State Attorney General's view and reverse the conviction there then would be no occasion for our passing on the federal question here raised by Ware. Under these circumstances we vacate the judgment of the Tennessee Supreme Court affirming Ware's conviction, and remand his case to that Court for further proceedings.</p>
<p>The judgment affirming Ashcraft's conviction is reversed and the cause is remanded to the Supreme Court of Tennessee for proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE JACKSON, dissenting:</p>
<p>A sovereign State is now before us, summoned on the charge that it has obtained convictions by methods so unfair that a federal court must set aside what the state courts have done. Heretofore the State has had the benefit of a presumption of regularity and legality. A confession made by one in custody heretofore has been <span class="star-pagination">*157</span> admissible in evidence unless it was proved and found that it was obtained by pressures so strong that it was <i>in fact</i> involuntarily made, that the individual will of the particular confessor had been overcome by torture, mob violence, fraud, trickery, threats, or promises. Even where there was excess and abuse of power on the part of officers, the State still was entitled to use the confession if upon examination of the whole evidence it was found to negative the view that the accused had "so lost his freedom of action that the statements made were not his but were the result of the deprivation of his free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 241</a></span>.</p>
<p>In determining these issues of fact, respect for the sovereign character of the several States always has constrained this Court to give great weight to findings of fact of state courts. While we have sometimes gone back of state court determinations to make sure whether the guaranties of the Fourteenth Amendment have or have not been violated, in close cases the decisions of state courts have often been sufficient to tip the scales in favor of affirmance. <i>Lisenba</i> v. <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#238" aria-description="Citation for case: Lisenba v. California"><i>California, supra,</i> 238, 239</a></span>; <i>Buchalter</i> v. <i>New York,</i> <span class="citation" data-id="103850"><a href="/opinion/103850/buchalter-v-new-york/#431" aria-description="Citation for case: Buchalter v. New York">319 U.S. 427, 431</a></span>; cf. <i>Milk Wagon Drivers Union</i> v. <i>Meadowmoor Dairies,</i> <span class="citation" data-id="9419143"><a href="/opinion/103459/milk-wagon-drivers-union-local-753-v-meadowmoor-dairies-inc/#294" aria-description="Citation for case: Milk Wagon Drivers Union, Local 753 v. Meadowmoor...">312 U.S. 287, 294</a></span>.</p>
<p>As we read the present decision the Court in effect declines to apply these well-established principles. Instead, it: (1) substitutes for determination on conflicting evidence the question whether this confession was actually produced by coercion, a presumption that it was, on a new doctrine that examination in custody of this duration is "inherently coercive"; (2) it makes that presumption irrebuttable  i.e., a rule of law  because, while it goes back of the state decisions to find certain facts, it refuses to resolve conflicts in evidence to determine whether other of <span class="star-pagination">*158</span> the State's proof is sufficient to overcome such presumption; and, in so doing, (3) it sets aside the findings by the courts of Tennessee that on all the facts this confession did not result from coercion, either giving those findings no weight or regarding them as immaterial.</p>
<p>We must bear in mind that this case does not come here from a lower federal court over whose conduct we may assert a general supervisory power. If it did, we should be at liberty to apply rules as to the admissibility of confessions, based on our own conception of permissible procedure, and in which we may embody restrictions even greater than those imposed upon the States by the Fourteenth Amendment. See <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U.S. 532</a></span>; <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1</a></span>; <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#341" aria-description="Citation for case: McNabb v. United States">318 U.S. 332, 341</a></span>; <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9419486"><a href="/opinion/103974/united-states-v-mitchell/" aria-description="Citation for case: United States v. Mitchell">322 U.S. 65</a></span>. But we have no such supervisory power over state courts. We may not lay down rules of evidence for them nor revise their decisions merely because we feel more confidence in our own wisdom and rectitude. We have no power to discipline the police or law-enforcement officers of the State of Tennessee nor to reverse its convictions in retribution for conduct which we may personally disapprove.</p>
<p>The burden of protecting society from most crimes against persons and property falls upon the State. Different States have different crime problems and some freedom to vary procedures according to their own ideas. Here, a State was forced by an unwitnessed and baffling murder to vindicate its law and protect its society. To nullify its conviction in this particular case upon a consideration of all the facts would be a delicate exercise of federal judicial power. But to go beyond this, as the Court does today, and divine in the due process clause of the Fourteenth Amendment an exclusion of confessions on an irrebuttable presumption that custody and examination are "inherently coercive" if of some unspecified duration within <span class="star-pagination">*159</span> thirty-six hours, requires us to make more than a passing expression of our doubts and disagreements.</p>
<p></p>
<h2>I.</h2>
<p>The claim of a suspect to immunity from questioning creates one of the most vexing problems in criminal law  that branch of the law which does the courts and the legal profession least credit. The consequences upon society of limiting examination of persons out of court cannot fairly be appraised without recognition of the advantage criminals already enjoy in immunity from compulsory examination in court. Of this latter Mr. Justice Cardozo, for an all but unanimous Court, said: "This too might be lost, and justice still be done. Indeed, today as in the past there are students of our penal system who look upon the immunity as a mischief rather than a benefit, and who would limit its scope, or destroy it altogether. No doubt there would remain the need to give protection against torture, physical or mental." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U.S. 319, 325-26</a></span>.</p>
<p>This Court never yet has held that the Constitution denies a State the right to use a confession just because the confessor was questioned in custody where it did not also find other circumstances that deprived him of a "free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 241</a></span>. The Constitution requires that a conviction rest on a fair trial. Forced confessions are ruled out of a fair trial. They are ruled out because they have been wrung from a prisoner by measures which are offensive to concepts of fundamental fairness. Different courts have used different terms to express the test by which to judge the inadmissibility of a confession, such as "forced," "coerced," "involuntary," "extorted," "loss of freedom of will." But always where we have professed to speak with the voice of the due process clause, the test, in whatever words stated, has been <span class="star-pagination">*160</span> applied to the particular confessor at the time of confession.</p>
<p>It is for this reason that American courts hold almost universally and very properly that a confession obtained during or shortly after the confessor has been subjected to brutality, torture, beating, starvation, or physical pain of any kind is <i>prima facie</i> "involuntary." The effect of threats alone may depend more on individual susceptibility to fear. But men are so constituted that many will risk the postponed consequences of yielding to a demand for a confession in order to be rid of present or imminent physical suffering. Actual or threatened violence have no place in eliciting truth and it is fair to assume that no officer of the law will resort to cruelty if truth is what he is seeking. We need not be too exacting about proof of the effects of such violence on the individual involved, for their effect on the human personality is invariably and seriously demoralizing.</p>
<p>When, however, we consider a confession obtained by questioning, even if persistent and prolonged, we are in a different field. Interrogation <i>per se</i> is not, while violence <i>per se</i> is, an outlaw. Questioning is an indispensable instrumentality of justice. It may be abused, of course, as cross-examination in court may be abused, but the principles by which we may adjudge when it passes constitutional limits are quite different from those that condemn police brutality, and are far more difficult to apply. And they call for a more responsible and cautious exercise of our office. For we may err on the side of hostility to violence without doing injury to legitimate prosecution of crime; we cannot read an undiscriminating hostility to mere interrogation into the Constitution without unduly fettering the States in protecting society from the criminal.</p>
<p>It probably is the normal instinct to deny and conceal any shameful or guilty act. Even a "voluntary confession" <span class="star-pagination">*161</span> is not likely to be the product of the same motives with which one may volunteer information that does not incriminate or concern him. The term "voluntary" confession does not mean voluntary in the sense of a confession to a priest merely to rid one's soul of a sense of guilt. "Voluntary confessions" in criminal law are the product of calculations of a different order, and usually proceed from a belief that further denial is useless and perhaps prejudicial. To speak of any confessions of crime made after arrest as being "voluntary" or "uncoerced" is somewhat inaccurate, although traditional.</p>
<p>A confession is wholly and incontestably voluntary only if a guilty person gives himself up to the law and becomes his own accuser. The Court bases its decision on the premise that custody and examination of a prisoner for thirty-six hours is "inherently coercive." Of course it is. And so is custody and examination for one hour. Arrest itself is inherently coercive, and so is detention. When not justified, infliction of such indignities upon the person is actionable as a tort. Of course such acts put pressure upon the prisoner to answer questions to answer them truthfully, and to confess if guilty.</p>
<p>But does the Constitution prohibit use of all confessions made after arrest because questioning, while one is deprived of freedom, is "inherently coercive"? The Court does not quite say so, but it is moving far and fast in that direction. The step it now takes is to hold this confession inadmissible because of the time taken in getting it.</p>
<p>The duration and intensity of an examination or inquisition always have been regarded as one of the relevant and important considerations in estimating its effect on the will of the individual involved. Thirty-six hours is a long stretch of questioning. That the inquiry was prolonged and persistent is a factor that in any calculation <span class="star-pagination">*162</span> of its effect on Ashcraft would count heavily against the confession. But some men would withstand for days pressures that would destroy the will of another in hours. Always heretofore the ultimate question has been whether the confessor was in possession of his own will and self-control at the time of confession. For its bearing on this question the Court always has considered the confessor's strength or weakness, whether he was educated or illiterate, intelligent or moronic, well or ill, Negro or white.</p>
<p>But the Court refuses in this case to be guided by this test. It rejects the finding of the Tennessee courts and says it must make an "independent examination" of the circumstances. Then it says that it will not "resolve any of the disputed questions of fact" relating to the circumstances of the confession. Instead of finding as a fact that Ashcraft's freedom of will was impaired, it substitutes the doctrine that the situation was "inherently coercive." It thus reaches on a <i>part</i> of the evidence in the case a conclusion which I shall demonstrate it could not properly reach on <i>all</i> the evidence. And it refuses to resolve the conflicts in the other evidence to determine whether it rebuts the presumption thus reached that the confession is a coerced one.</p>
<p>If the constitutional admissibility of a confession is no longer to be measured by the mental state of the individual confessor but by a general doctrine dependent on the clock, it should be capable of statement in definite terms. If thirty-six hours is more than is permissible, what about 24? or 12? or 6? or 1? All are "inherently coercive." Of course questions of law like this often turn on matters of degree. But are not the States entitled to know, if this Court is able to state, what the considerations are which make any particular degree decisive? How else may state courts apply our tests?</p>
<p><span class="star-pagination">*163</span> The importance of defining these new constitutional standards of admissibility of confessions is emphasized by the decision to return the companion case of Ware to the Supreme Court of Tennessee for reconsideration "in the light of our ruling as to Ashcraft." Except for Ware's own testimony, all of the evidence is that when he confronted Ashcraft in custody Ware confessed immediately, voluntarily, and almost spontaneously. But he had been arrested, taken from bed into custody, and detained and questioned. Does the doctrine of inherent coerciveness condemn the Ware confession? Should the Tennessee court decide whether Ware, obviously a much weaker character than Ashcraft, was <i>actually</i> coerced into confessing? It already has decided that question and this Court does not hold the fact determined wrongly. Ware's case is properly in this Court. Why should not this Court decide Ware's case on the merits and thus test and expound its novel ruling as applied to a different set of circumstances?</p>
<p>No one can regard the rule of exclusion dependent on the state of the individual's will as an easy one to apply. It leads to controversy, speculation, and variations in application. To eliminate these evils by eliminating all confessions made after interrogation while in custody is a drastic alternative, but it is the logical consequence of today's ruling, as its application to the facts of Ashcraft's case will show.</p>
<p></p>
<h2>II.</h2>
<p>Apart from Ashcraft's uncorroborated testimony, which the Tennessee courts refused to believe, there is much evidence in this record from persons whom they did believe and were justified in believing. This evidence shows that despite the "inherent coerciveness" of the circumstances of his examination, the confession when made was deliberate, <span class="star-pagination">*164</span> free, and voluntary in the sense in which that term is used in criminal law. This Court could not, in our opinion, hold this confession an involuntary one except by substituting its presumption in place of analysis of the evidence and refusing to weigh the evidence even in rebuttal of its presumption.</p>
<p>As in most such cases, we start with some admitted facts. In the early morning Mrs. Ashcraft left her home in an automobile to visit relatives. She was found murdered. She had not been robbed nor ravished, although an effort had been made to give the crime an appearance of robbery. The officers knew of no other motive for the killing and naturally turned to her husband for information.</p>
<p>On the afternoon of the crime, Thursday, June 5, 1941, they took Ashcraft to the morgue to identify the body, and to the county jail, where he was kept and interviewed until 2:00 a.m. He makes no complaint of his treatment at this time. In this and several later interviews he made a number of statements with reference to the condition of the car, and as to Mrs. Ashcraft's having taken a certain drug, and as to money which she was accustomed to carry on her person, which further investigation indicated to be untrue. Still Ashcraft was not arrested. He professed to be willing to assist in identifying the killer. At last, on Saturday evening, June 14, an officer brought Ashcraft to the jail for further questioning. He was taken to a room on the fifth floor and questioned intermittently by several officers over a period of about thirty-six hours.</p>
<p>There are two versions as to what happened during this period of questioning. According to the version of the officers, which was accepted by the court which saw the witnesses, what happened? On Saturday evening Ashcraft was taken to the jail, where he was questioned by Mr. Becker and Mr. Battle. Becker is in the Intelligence <span class="star-pagination">*165</span> Service of the United States Army at the present time and before that was in charge of the Homicide Bureau of the Sheriff's office of Shelby County, Tennessee. Battle has for eight years been an Assistant Attorney General of the County. They began questioning Ashcraft about 7:00 p.m. They recounted various statements of his which had proved untrue. About 11:00 o'clock Ashcraft said he realized the circumstances all pointed to him and that he could not explain the circumstances. They then accused him of the murder, but he denied it. About 3:00 a.m. Becker and Battle retired and left Ashcraft in charge of Ezzell, a special investigator connected with the Attorney General's office. He questioned Ashcraft and discussed the crime with him until about 7:00 on Sunday morning. Becker and Battle then returned and interviewed him intermittently until about noon, when Ezzell returned and remained until about 5:00. Becker then returned, and about 11:00 o'clock Sunday night Ashcraft expressed a desire to talk with Ezzell. Ezzell was sent for and Ashcraft told him he wanted to tell him the truth. He said, "Mr. Ezzell, a Negro killed my wife." Ezzell asked the Negro's name, and Ashcraft said, "Tom Ware." Up to this time Ware had not been suspected, nor had his name been mentioned. Ashcraft explained that he did not tell the officers before because "I was scared; the Negro said he would burn my house down if I told the law."</p>
<p>Thereupon Becker, Battle, Ezzell, and Mr. Jayroe, connected with the Sheriff's office, took Ashcraft in a car and found Ware. When questioned at the jail, Ware turned to Ashcraft and said in substance that he had told Ashcraft when this thing happened that he did not intend to take the entire blame. The officers thereupon turned their attention to Ware. He promptly admitted the killing and said Ashcraft hired him to do it. Waldauer, the court reporter, was called to take down this confession, and <span class="star-pagination">*166</span> completed his transcript at about 5:40 a.m. He read it to Ware and told him he did not have to sign it unless he so chose. Ware made his mark upon it and swore to it before Waldauer as a Notary Public. A copy was given to Ashcraft, and he then admitted that he had hired Ware to kill his wife. He was given breakfast and then in response to questions made a statement which was taken down by the court reporter, Waldauer. It was transcribed, but Ashcraft declined to sign it, saying that he wanted his lawyer to see it before he signed it. No effort was made to compel him to sign the confession. However, two business men of Memphis, Mr. Castle, vice president of a bank, and Mr. Pidgeon, president of the Coca-Cola Bottling Company, were called in. Both testified that Ashcraft in their presence asserted that the transcript was correct but that he declined to sign it. The officers also called Dr. McQuiston to the jail to make a physical examination of both Ashcraft and Ware. He had practiced medicine in Memphis for twenty-eight years and both Mr. and Mrs. Ashcraft had been his patients for something like five years. In the presence of this friendly doctor Ashcraft might have complained of his treatment and avowed his innocence. The doctor testified, however, that Ashcraft said he had been treated all right, that he made no complaint about his eyes, and that they were not bloodshot. The doctor made a physical examination, and says Ashcraft appeared normal. He further testified as to Ashcraft, "Well, sir, he said he had not been able to get along with his wife for some time; that her health had been bad; that he had offered her a property settlement, and that she might go her way and he his way; and he also stated that he offered this colored man, Ware, a sum of money to make away with his wife."<sup>[1]</sup> The doctor says <span class="star-pagination">*167</span> that that statement was entirely voluntary. No matter what pressure had been put on Ashcraft before, the courts below could reasonably believe that he made this statement voluntarily to a man of whom he had no fear and who knew his family relations.</p>
<p>Ashcraft's story of torture could only be accepted by disbelieving such credible and unimpeached contradiction. Ashcraft testified that he was refused food, and was not allowed to go to the lavatory, and was denied even a drink of water. Other testimony is that on Saturday night he was brought a sandwich and coffee about midnight; that he drank the coffee but refused the sandwich; that on Sunday morning he was given a breakfast and was fed again about noon a plate lunch consisting of meat and vegetables and coffee. Both Waldauer, the Reporter, and Dr. McQuiston testified that they saw breakfast served to Ashcraft the next morning before the statement taken down by Waldauer. Ashcraft claims he was threatened and that a cigarette was slapped out of his mouth. This is all denied.</p>
<p>This Court rejects the testimony of the officers and disinterested witnesses in this case that the confession was voluntary not because it lacked probative value in itself nor because the witnesses were self-contradictory or were impeached. On the contrary, it is impugned only on grounds such as that such disputes "are an inescapable consequence of secret inquisitorial practices." We infer from this that since a prisoner's unsupported word often conflicts with that of the officers, the officer's testimony for constitutional purposes is always <i>prima facie</i> false. We know that police standards often leave much to be desired, but we are not ready to believe that the democratic process <span class="star-pagination">*168</span> brings to office men generally less believable than the average of those accused of crime.</p>
<p>Reference also is made to the fact that when petitioner was questioned investigation had failed "to unearth one single tangible clue pointing to his guilt." We cannot see the relevance of such circumstances on the question of the voluntary or involuntary character of his statements to the officers. Is the suggestion that if they had probable clews to his guilt, their questioning of him would have been better justified?</p>
<p>This questioning is characterized as a "secret inquisition," invoking all of the horrendous historical associations of those words. Certainly the inquiry was participated in by a good many persons, and we do not see how it could have been much less "secret" unless the press should have been called in. Of course, any questioning may be characterized as an "inquisition," but the use of such characterizations is no substitute for the detached and judicial consideration that the court below gave to the case.</p>
<p>We conclude that even going behind the state court decisions into the facts, no independent judgment on the whole evidence that Ashcraft's confession was in fact coerced is possible. And against this background of facts the extreme character of the Court's ruling becomes apparent.</p>
<p>I am not sure whether the Court denies the State all right to arrest and question the husband of the slain woman. No investigation worthy of the name could fail to examine him. Of all persons, he was most likely to know whether she had enemies or rivals. Would not the State have a constitutional right, whether he was accused or not, to arrest and detain him as a material witness? If it has the right to detain one as a witness, presumably it has the right to examine him.</p>
<p><span class="star-pagination">*169</span> Could the State not confront Ashcraft with his false statements and ask his explanation? He did not throw himself at any time on his rights, refuse to answer, and demand counsel, even according to his own testimony. The strategy of the officers evidently was to keep him talking, to give him plenty of rope and see if he would not hang himself. He does not claim to have made objection to this. Instead he relied on his wits. The time came when it dawned on him that his own story brought him under suspicion, and that he could not meet it. Must the officers stop at this point because he was coming to appreciate the uselessness of deception?</p>
<p>Then he became desperate and accused the Negro. Certainly from this point the State was justified in holding and questioning him as a witness, for he claimed to know the killer. That accusation backfired and only turned up a witness against him. He had run out of expedients and inventions; he knew he had lost the battle of wits. After all, honesty seemed to be the best, even if the last, policy. He confessed in detail.</p>
<p>At what point in all this investigation does the Court hold that the Constitution commands these officers to send Ashcraft on his way and give up the murder as insoluble? If the State is denied the right to apply any pressure to him which is "inherently coercive" it could hardly deprive him of his freedom at all. I, too, dislike to think of any man, under the disadvantages and indignities of detention being questioned about his personal life for thirty-six hours or for one hour. In fact, there is much in our whole system of penology that seems archaic and vindictive and badly managed. Every person in the community, no matter how inconvenient or embarrassing, no matter what retaliation it exposes him to, may be called upon to take the witness stand and tell all he knows about a crime  except the person who knows most about it. <span class="star-pagination">*170</span> Efforts of prosecutors to compensate for this handicap by violent or brutal treatment or threats we condemn as passionately and sincerely as other members of the Court. But we are not ready to say that the pressure to disclose crime, involved in decent detention and lengthy examination, although we admit them to be "inherently coercive," are denied to a State by the Constitution, where they are not proved to have passed the individual's ability to resist and to admit, deny, or refuse to answer.</p>
<p></p>
<h2>III.</h2>
<p>The Court either gives no weight to the findings of the Tennessee courts or it regards their inquiry as to the effect on the individuals involved as immaterial. We think it was a material inquiry and that respect is due to their conclusion.</p>
<p>The Supreme Court of Tennessee, writing in this case, stated the law of that State by which it reviewed and affirmed the action of the trial court. It said, "When confessions are offered as evidence, their competency becomes a preliminary question to be determined by the court. This imposes upon the presiding judge the duty of deciding <i>the fact</i> whether the party making the confession was influenced by hope or fear. This rule is so well established, that if the judge allow the jury to determine the preliminary fact, it is error, for which the judgment will be reversed.</p>
<p>"In the instant case the trial judge heard the witnesses as to their confessions out of the presence of the jury, and he held that under the facts he could not say that the confessions were not voluntarily made and, therefore, permitted them to go to the jury." (Emphasis supplied.)</p>
<p>The rule of law thus laid down complied with the law as this Court had settled it at the time of trial.</p>
<p>The Tennessee Supreme Court made a painstaking examination of the evidence in the light of the claim that <span class="star-pagination">*171</span> the confessions were coerced. It concluded that it was "unable to say that the confessions were not freely and voluntarily made. Both of the plaintiffs in error have had a fair trial and we decline to disturb the conviction."</p>
<p>That court, it is clear, renders no mere lip service to the guaranties of the Constitution. In other cases it has set aside convictions because confessions used at trials were found to have been coerced.<sup>[2]</sup> There is not the least indication that the court was passionate or biased or that the result does not represent the honest judgment of a high-minded court, sensitive to these problems.</p>
<p>A trial judge out of hearing of the jury saw and heard Ashcraft and saw and heard those whom Ashcraft accused of coercing him. In determining a matter of this kind no one can deny the great advantage of a court which may see and hear a man who claims that his will succumbed and those who, it is claimed, were so overbearing. The real issue is strength of character, and a few minutes' observation of the parties in the courtroom is more informing than reams of cold record. There is not the slightest indication that the trial judge was prejudiced or indifferent to the prisoner's rights. Ashcraft's counsel moved to exclude his confession "for the reason that the statements contained therein were not freely and voluntarily made, nor were they free from duress and restraint, but were secured by compulsion. . . ." The court said, ". . . the sole proposition, as the Court sees it from this testimony, is that he was confined and questioned for a period of approximately thirty-six hours. I think counsel concedes that is practically the main ground upon which he rests his motion. There was no physical violence offered to the defendant Ashcraft, and none claimed." He overruled the motion and received the confession. This <span class="star-pagination">*172</span> Court, not one of whose members ever saw Ashcraft or any one of the State's witnesses, overturns the decision by the trial judge.</p>
<p>Moreover, a jury held Ashcraft's statements incredible. After the trial judge, out of their presence, heard the evidence and decided the confession was admissible, the jury heard the evidence to decide whether the confession should be believed. Ashcraft again testified and so did all of the witnesses for the State. Conduct of the hearing both by the judge and the prosecutors was above criticism. The Court observes: "If, therefore, the question of the voluntariness of the two confessions was actually decided at all it was by the jury." Is it suggested that a State consistently with the Constitution may not leave this question to the sole determination of a jury? I had supposed that the constitutional duty of a State when such questions of fact arise is to furnish due process of law for deciding them. Does not jury trial meet this test? Here Tennessee, and I think very commendably, provided the double safeguards of a preliminary trial by the judge and a final determination by the jury.</p>
<p>The Court's opinion makes a critical reference to the charge of the trial judge. However, diligent counsel took no exception to the part of the charge quoted, made no request for further instruction on the subject, and assigned no error to the charge. Even if we think the charge inadequate, does the inadequacy of a charge constitute want of due process? And if so, do we review questions as to the charge although counsel for the petitioner made no objection during the trial when the judge could have corrected the error, but after the trial was over assigned it as one of twelve reasons for demanding a new trial?</p>
<p>No conclusion that this confession was actually coerced can be reached on this record except by reliance upon the utterly uncorroborated statements of defendant Ashcraft. <span class="star-pagination">*173</span> His testimony does not carry even ordinary guaranties of truthfulness, and the courts and jury were not bound to accept it. Perjury is a light offense compared to murder and they may well have believed that Ashcraft was ready to resort to a lesser crime to avoid conviction of a greater one. Furthermore, the very grounds on which this Court now upsets his conviction Ashcraft repudiated at the trial. He asserts that he was abused, but he does not testify as this Court holds that it had the effect of forcing an involuntary confession from him. On the contrary, he flatly insists that it had no such effect and that he never did confess at all.</p>
<p>Against Ashcraft's word the state courts and jury accepted the testimony of several apparently disinterested witnesses of high standing in their communities, in addition to that of the accused officers. One of the witnesses to Ashcraft's admission of guilt was his own family physician, two were disinterested businessmen of substance and standing, another was an experienced court reporter who had long held this position of considerable trust. Another was a member of the bar. Certainly, the state courts were not committing an offense against the Constitution of the United States in refusing to believe that this whole group of apparently reputable citizens entered into a conspiracy to swear a murder onto an innocent man, against whom not one of them is shown to have had a grievance or a grudge.</p>
<p>This is not the case of an ignorant and unrepresented defendant who has been the victim of prejudice. Ashcraft was a white man of good reputation, good position, and substantial property. For a week after this crime was discovered he was not detained, although his stories to the officers did not hang together, but was at large, free to consult his friends and counsel. There was no indecent haste, but on the contrary evident deliberation, in suspecting <span class="star-pagination">*174</span> and accusing him. He was not sentenced to death, but for a term that probably means life. He was defended by resourceful and diligent counsel.</p>
<p>The use of the due process clause to disable the States in protection of society from crime is quite as dangerous and delicate a use of federal judicial power as to use it to disable them from social or economic experimentation. The warning words of Mr. Justice Holmes in his dissenting opinion in <i>Baldwin</i> v. <i>Missouri,</i> <span class="citation" data-id="101593"><a href="/opinion/101593/baldwin-v-missouri/#595" aria-description="Citation for case: Baldwin v. Missouri">281 U.S. 586, 595</a></span>, seem to us appropriate for rereading now.</p>
<p>MR. JUSTICE ROBERTS and MR. JUSTICE FRANKFURTER join in this opinion.</p>
<h2>NOTES</h2>
<p>[1]  The legal test applied by the trial court to determine the admissibility of the two confessions was stated thus:
</p>
<p>"The Court has come to the conclusion . . . that the law in Tennessee with reference to confession is simply this: it is largely a question of fact as to whether or not a confession is voluntary, and is made without hope of reward or fear of punishment. It only becomes a question of law for the Court to decide when, from the facts surrounding the taking of the alleged confessions or statements, the Court, as a matter of law, can hold that the State has failed to carry its burden, which it has of showing that the confessions were free and voluntary, and that reasonable minds could not differ, and could come to but one conclusion that the confessions were involuntary and forced."</p>
<p>[2]  Notwithstanding the apparent fact that neither the trial court nor the appellate court affirmatively held the confessions voluntary, the Tennessee Supreme Court, in its opinion, restated the rule it had announced in previous cases, that, "When confessions are offered as evidence, their competency becomes a preliminary question, to be determined by the court. . . . [If] the judge allow the jury to determine the preliminary fact, it is error, for which the judgment will be reversed." See <i>Self</i> v. <i>State,</i> <span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/#253" aria-description="Citation for case: Self v. State">65 Tenn. 244, 253</a></span>.</p>
<p>[3]  On motion for new trial, Ashcraft's counsel urged error in that, "The court . . . in delivering his charge to the jury . . . in no place or at any time . . . presented the theory of the defendant Ashcraft to the jury. He wholly and completely in his charge ignored the contention and theory of the defendant Ashcraft that the alleged confession or admissions made by him . . . were not freely and voluntarily made. . . ."</p>
<p>[4]  From the testimony it appears that Ashcraft was taken from the jail about 11 o'clock Sunday night for a period of approximately an hour to help the officers hunt the place where Ware lived. On his return Ashcraft was, for a short time, kept in a jail room different from that in which he was kept the rest of the time.</p>
<p>[5]  "As the report avers, `The third degree is a secret and illegal practice.' Hence the difficulty of discovering the facts as to the extent and manner it is practiced." IV Reports of National Committee on Law Observance and Enforcement (Wickersham Commission), U.S. Government Printing Office, 1931, Lawlessness in Law Enforcement, p. 3. Station houses and jails are most frequently employed for third degree practices, "upstairs rooms or back rooms being sometimes picked out for their greater privacy." <i><span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/" aria-description="Citation for case: Self v. State">Id.,</a></span></i> The Third Degree, p. 170. Cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#238" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227, 238</a></span>.</p>
<p>[6]  "`Work' is the term used to signify any form of what is commonly called the third degree, and may consist in nothing more than a severe cross-examination. Perhaps in most cases it is no more than that, but the prisoner knows that he is wholly at the mercy of his inquisitor and that the severe cross-examination may at any moment shift to a severe beating. . . . Powerful lights turned full on the prisoner's face, or switched on and off have been found effective. . . . The most commonly used method is persistent questioning, continuing hour after hour, sometimes by relays of officers. It has been known since 1500 at least that deprivation of sleep is the most effective torture and certain to produce any confession desired." Report of Committee on Lawless Enforcement of Law made to the Section of Criminal Law and Criminology of the American Bar Association (1930) 1 American Journal of Police Science 575, 579-580, also quoted in IV Wickersham Report, <i>supra,</i> p. 47.</p>
<p>[7]  The use in evidence of a defendant's coerced confession cannot be justified on the ground that the defendant has denied he ever gave the confession. <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/#531" aria-description="Citation for case: White v. Texas">310 U.S. 530, 531-532</a></span>.</p>
<p>[8]  State and federal courts, textbook writers, legal commentators, and governmental commissions consistently have applied the name of "inquisition" to prolonged examination of suspects conducted as was the examination of Ashcraft. See, e.g., cases cited in IV Wickersham Report, <i>supra,</i> and also pp. 44, 47, 48, and passim; Pound (Cuthbert W.), Inquisitorial Confessions, 1 Cornell L.Q. 77; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#237" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227, 237</a></span>; <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#544" aria-description="Citation for case: Bram v. United States">168 U.S. 532, 544</a></span>; <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#596" aria-description="Citation for case: Brown v. Walker">161 U.S. 591, 596</a></span>; <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#573" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 573</a></span>; cf. <i>Cooper</i> v. <i>State,</i> <span class="citation" data-id="6513449"><a href="/opinion/6636874/cooper-v-state/#611" aria-description="Citation for case: Cooper v. State">86 Ala. 610, 611</a></span>, <span class="citation no-link">6 So. 110</span>. In a case where no physical violence was inflicted or threatened, the Supreme Court of Virginia expressly approved the statement of the trial judge that the manner and methods used in obtaining the confession read "like a chapter from the history of the inquisition of the Middle Ages." <i>Enoch</i> v. <i>Commonwealth,</i> <span class="citation" data-id="9579748"><a href="/opinion/1322156/enoch-v-commonwealth/#423" aria-description="Citation for case: Enoch v. Commonwealth">141 Va. 411, 423</a></span>, <span class="citation" data-id="9579748"><a href="/opinion/1322156/enoch-v-commonwealth/#225" aria-description="Citation for case: Enoch v. Commonwealth">126 S.E. 222, 225</a></span>; and see <i>Cross</i> v. <i>State,</i> <span class="citation" data-id="8301941"><a href="/opinion/8333908/cross-v-state/#514" aria-description="Citation for case: Cross v. State">142 Tenn. 510, 514</a></span>, <span class="citation no-link">221 S.W. 489</span>. The analogy, of course, was in the fact that old inquisition practices included questioning suspects in secret places, away from friends and counsel, with notaries waiting to take down "confessions," and with arrangements to have the suspect later affirm the truth of his confession in the presence of witnesses who took no part in the inquisition. See Encyclopedia Britannica, Fourteenth Ed., "Inquisition"; Prescott, Ferdinand and Isabella, Sixth Ed., Part First, Chap. VII, The Inquisition; VIII Wigmore on Evidence, Third Ed., p. 307. "In the more serious offenses the party suspected is arrested, he is placed on his inquisition before the chief of police, and a statement is obtained. . . . Where the office of the district attorney is in political harmony with the police system, the district attorney is generally invited to be present as an inquisitor." 2 Wharton on Criminal Evidence, Eleventh Ed., pp. 1021-1022; and see Notes 5 and 6, <i>supra.</i>
</p>
<p>An admirable summary of the generally expressed judicial attitude toward these practices is set forth in the Report of The Committee on Lawless Enforcement of Law, 1 Amer. Journ. of Police Science, <i>supra,</i> p. 587: "Holding incommunicado is objectionable because arbitrary  at the mere will and unregulated pleasure of a police officer. . . . The use of the third degree is obnoxious because it is secret; because the prisoner is wholly unrepresented; because there is present no neutral, impartial authority to determine questions between the police and the prisoner; because there is no limit to the range of the inquisition, nor to the pressure that may be put upon the prisoner."</p>
<p>[9]  <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#556" aria-description="Citation for case: Bram v. United States">168 U.S. 532, 556, 562-563</a></span>; see also <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1, 14-15</a></span>; <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U.S. 465, 475</a></span>; <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#573" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 573-574</a></span>; 3 Elliot's Debates, pp. 445-449, 452; cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>. The question in the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> case was whether Bram had been compelled or coerced by a police officer to make a self-incriminatory statement, contrary to the Fifth Amendment; and the question here is whether Ashcraft similarly was coerced to make such a statement, contrary to the Fourteenth Amendment. <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 236-238</a></span>. Taken together, the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> and <i><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">Lisenba</a></span></i> cases hold that a coerced or compelled confession cannot be used to convict a defendant in any state or federal court. And the decision in the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> case makes it clear that the admitted circumstances under which Ashcraft is alleged to have confessed preclude a holding that he acted voluntarily.</p>
<p>[10]  Compare the following allegation contained in Ashcraft's motion for new trial, "The Sheriff's deputies . . . set themselves up as a quasi judicial tribunal and tried . . . and convicted him there and in so doing rendered a trial . . . before the trial court . .. and the jury of peers . . . a mere formality," with <i>Lisenba</i> v. <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#237" aria-description="Citation for case: Lisenba v. California"><i>California, supra,</i> p. 237</a></span>. "The requirement of a public trial is for the benefit of the accused; that the public may see he is fairly dealt with and not unjustly condemned, and that the presence of interested spectators may keep his triers keenly alive to a sense of their responsibility and to the importance of their functions . . ." Cooley's Constitutional Limitations, Sixth Ed. (1890) p. 379; see also <i>Keddington</i> v. <i>State,</i> <span class="citation" data-id="6474469"><a href="/opinion/6599127/keddington-v-state/#459" aria-description="Citation for case: Keddington v. State">19 Ariz. 457, 459</a></span>, <span class="citation" data-id="6474469"><a href="/opinion/6599127/keddington-v-state/" aria-description="Citation for case: Keddington v. State">172 P. 273</a></span>. "The aid of counsel in preparation would be farcical if the case could be foreclosed by a preliminary inquisition which would squeeze out conviction or prejudice by means unconstitutional if used at the trial." <i>Wood</i> v. <i>United States,</i> <span class="citation" data-id="1545293"><a href="/opinion/1545293/wood-v-united-states/#271" aria-description="Citation for case: Wood v. United States">128 F.2d 265, 271</a></span>. See also <i>Chambers</i> v. <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#237" aria-description="Citation for case: Chambers v. Florida"><i>Florida, supra,</i> p. 237</a></span>, Note 10.</p>
<p>[11]  <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>; <i>Canty</i> v. <i>Alabama,</i> <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U.S. 629</a></span>; <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U.S. 530</a></span>; <i>Lomax</i> v. <i>Texas,</i> <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U.S. 544</a></span>; <i>Vernon</i> v. <i>Alabama,</i> <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U.S. 547</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 236-238</a></span>; <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#555" aria-description="Citation for case: Ward v. Texas">316 U.S. 547, 555</a></span>; and see <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U.S. 532</a></span>.</p>
<p>[1]  The officers had been baffled as to any motive for Ashcraft to murder his wife (who was his third, two former ones having been separated from him by divorce). He disclosed in his confession to them that her sickness had resulted in a degree of irritability which had made them incompatible and resulted in his sexual frustration.</p>
<p>[2]  <i>Deathridge</i> v. <i>State,</i> <span class="citation" data-id="7663198"><a href="/opinion/7727512/deathridge-v-state/" aria-description="Citation for case: Deathridge v. State">33 Tenn. 75</a></span>; <i>Strady</i> v. <i>State,</i> <span class="citation multiple-matches"><a href="/c/Tenn./45/300/">45 Tenn. 300</a></span>; <i>Self</i> v. <i>State,</i> <span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/" aria-description="Citation for case: Self v. State">65 Tenn. 244</a></span>; <i>Cross</i> v. <i>State,</i> <span class="citation" data-id="8301941"><a href="/opinion/8333908/cross-v-state/" aria-description="Citation for case: Cross v. State">142 Tenn. 510</a></span>, <span class="citation no-link">221 S.W. 489</span>; <i>Rounds</i> v. <i>State,</i> <span class="citation" data-id="3891773"><a href="/opinion/4129358/rounds-v-state/" aria-description="Citation for case: Rounds v. State">171 Tenn. 511</a></span>, <span class="citation" data-id="3891773"><a href="/opinion/4129358/rounds-v-state/" aria-description="Citation for case: Rounds v. State">106 S.W.2d 212</a></span>.</p>

</div>
```

---
