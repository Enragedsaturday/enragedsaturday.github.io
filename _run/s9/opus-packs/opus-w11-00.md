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

## GROUP: _overhaul2/lake/cases/Scott v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Scott v. United States
type: case
citation: "436 U.S. 128 (1978)"
parallel_cite: "98 S. Ct. 1717; 56 L. Ed. 2d 168"
neutral_cite: 1978 U.S. LEXIS 89
court: U.S.
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-05-15
docket: 76-6767
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
  opinion_url: "https://www.courtlistener.com/opinion/109860/scott-v-united-states/"
  cluster_id: 109860
  opinion_id: null
  identity_checked: true
lake:
  record_id: Scott v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Electronic Surveillance and Title III]]"
    role: Anchor
related:
  - "[[Electronic Surveillance and Title III]]"
  - "[[Katz v. United States]]"
  - "[[Berger v. New York]]"
  - "[[Terry v. Ohio]]"
  - "[[United States v. Donovan]]"
tags:
  - case
  - fourth-amendment
  - electronic-surveillance
  - title-iii
  - wiretap
  - minimization
  - objective-standard
holding: "Whether wiretap agents complied with Title III's minimization requirement (18 U.S.C. § 2518(5)) is determined by an objective assessment of the reasonableness of the actual interceptions in light of the circumstances known to the agents, not by their subjective intent; the agents' knowing failure to make good-faith efforts to minimize does not itself establish a statutory violation where the interceptions were objectively reasonable."
aliases:
  - Scott v. United States
  - "Scott v. United States (1978)"
---

# Scott v. United States

*436 U.S. 128 (1978)* (No. 76-6767) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109860 → combined opinion 109860 (Rehnquist, J.; 436 U.S. 128, argued Mar. 1, 1978, decided May 15, 1978). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*137`). S9 promotes. -->

## Background
Acting under a Title III wiretap order that required them to minimize the interception of non-pertinent calls, government agents investigating a Washington, D.C., narcotics conspiracy intercepted virtually every conversation on a target telephone for roughly a month, even though only about 40% of the calls proved narcotics-related. The agents conceded they made no efforts that resulted in the non-interception of any call. The District Court twice ordered suppression, reasoning that the agents' "admitted knowing and purposeful failure" to comply with the minimization order was unreasonable regardless of the calls' content. The Court of Appeals for the D.C. Circuit twice reversed, holding that the reasonableness of the *actual interceptions*, judged objectively, controls — not the agents' subjective intent — and ultimately found suppression unwarranted.

## Issue
Whether a violation of Title III's minimization requirement is established by the agents' failure to make good-faith efforts to minimize, or instead by an objective assessment of whether the interceptions they actually made were reasonable under the circumstances.

## Rule
The Court distinguished what establishes a violation from what motives may bear on the suppression remedy, and held that the existence of a statutory or constitutional violation turns on objective reasonableness, not subjective intent. It adopted that approach for minimization: "We think the Government's position, which also served as the basis for decision in the Court of Appeals, embodies the proper approach for evaluating compliance with the minimization requirement. Although we have not examined this exact question at great length in any of our prior opinions, almost without exception in evaluating alleged violations of the Fourth Amendment the Court has first undertaken an objective assessment of an officer's actions in light of the facts and circumstances then known to him." — 436 U.S. at 137. ^pin-137

## Application
Because the Fourth Amendment proscribes only "unreasonable" searches and seizures, and because the Court had long judged an officer's conduct against an objective standard (as in *[[Terry v. Ohio|Terry]]* and *[[United States v. Robinson]]*), the agents' bad faith could not by itself invalidate interceptions that were objectively reasonable. Reasonableness here depended on such things as the scope of the probable-cause showing, the character of the suspected conspiracy (a wide-ranging narcotics network in which many callers might be implicated), and the difficulty of knowing in advance which calls would be pertinent. Judged that way, the agents had not acted unreasonably in the interceptions they made, so no § 2518(5) violation was shown.

## Conclusion
The judgment of the Court of Appeals for the D.C. Circuit was **affirmed**. Rehnquist, J., delivered the opinion of the Court. Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Scott* is the anchor for how Title III's minimization requirement is enforced: courts test the objective reasonableness of the interceptions actually made, not the monitoring agents' state of mind. It is one instance of the broader move to an objective standard for Fourth Amendment reasonableness. Teach it alongside the statute's origins in *[[Berger v. New York]]* and *[[Katz v. United States]]* and the companion Title III decisions *[[United States v. Donovan]]* and *[[United States v. Giordano]]*.

## Appears on
- [[Electronic Surveillance and Title III]] — *Anchor*

## Sources
- [*Scott v. United States*, 436 U.S. 128 (1978)](https://www.courtlistener.com/opinion/109860/scott-v-united-states/) — pinpoint: 137 (Rehnquist, J., for the Court; the CL opinion text carries the reporter star `*137` immediately before the quoted holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "783b9c18ed11fa9d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Scott v. United States"}, "payload": {"all": [{"cite": "436 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "436"}, {"cite": "98 S. Ct. 1717", "page": "1717", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "56 L. Ed. 2d 168", "page": "168", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}, {"cite": "1978 U.S. LEXIS 89", "page": "89", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "436 U.S. 128", "official": {"cite": "436 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "436"}, "official_selection_present": true, "record_id": "Scott v. United States"}}
{"assertion_id": "16f97cb74cd280a6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Scott v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Scott v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Scott v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Scott v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Scott v. United States",
    "case_name_short": "Scott",
    "case_name_full": "SCOTT Et Al. v. UNITED STATES",
    "input_case_name": "Scott v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-05-15",
    "year": 1978,
    "docket": "76-6767",
    "cluster_id": 109860,
    "lead_opinion_id": 9427183,
    "sibling_ids": [],
    "absolute_url": "/opinion/109860/scott-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 128",
      "volume": "436",
      "reporter": "U.S.",
      "page": "128",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 1717",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1717",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 168",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "168",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 89",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 128",
        "volume": "436",
        "reporter": "U.S.",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 1717",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1717",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 168",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "168",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 89",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "89",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 128",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 128",
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
    "date_created": "2026-07-07T13:24:56Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "scott-v-united-states--109860",
      "to_record_id": "Scott v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Scott v. United States

```
<opinion type="majority">
<author id="b182-7">Me. Justice Rehnquist</author>
<p id="AmT">delivered the opinion of the Court.</p>
<p id="b182-8">In 1968, Congress enacted Title III of the Omnibus Crime Control and Safe Streets Act of 1968, which deals with wiretapping and other forms of electronic surveillance. <span class="citation no-link">18 U. S. C. §§ 2510-2520</span> (1976 ed.). In this Act Congress, after this Court’s decisions in <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967), and <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), set out to provide law enforcement officials with some of the tools thought necessary to combat crime without unnecessarily infringing upon the right of individual privacy. See generally S. Rep. No. 1097, 90th Cong., 2d Sess. (1968). We have had occasion in the past, the most recent being just last Term, to consider exactly how the statute effectuates this balance.<footnotemark>1</footnotemark> This case requires us to construe the statutory requirement that wiretapping or electronic surveillance “be conducted in such a way as to minimize the interception of communications not otherwise subject to interception under this chapter . . . .” 18 U. S.C. §2518(5) (1976 ed.).</p>
<p id="b182-9">Pursuant to judicial authorization which required such minimization, Government agents intercepted all the phone conversations over a particular phone for a period of one <page-number citation-index="1" label="131">*131</page-number>month. The District Court for the District of Columbia suppressed all intercepted conversations and evidence derived therefrom in essence because the “admitted knowing and purposeful failure by the monitoring agents to comply with the minimization order was unreasonable . . . even if every intercepted call were narcotic-related.” App. 39. The Court of Appeals for the District of Columbia Circuit reversed, concluding that an assessment of the reasonableness of the efforts at minimization first requires an evaluation of the reasonableness of the actual interceptions in light of the purpose of the wiretap and the totality of the circumstances before any inquiry is made into the subjective intent of the agents conducting the surveillance. 170 U. S. App. D. C. 158, <span class="citation" data-id="327713"><a href="/opinion/327713/united-states-v-frank-ricardo-scott-aka-reds-united-states-of/" aria-description="Citation for case: United States v. Frank Ricardo Scott, A/K/A &quot;Reds,&quot;...">516 F. 2d 751</a></span> (1975). We granted certiorari to consider this important question, <span class="citation multiple-matches"><a href="/c/U.%20S./434/888/">434 U. S. 888</a></span> (1977), and, finding ourselves in basic agreement with the Court of Appeals, affirm.</p>
<p id="b183-4">I</p>
<p id="b183-5">In January 1970, Government officials applied, pursuant to Title III, for authorization to wiretap a telephone registered to Geneva Jenkins.<footnotemark>2</footnotemark> The supporting affidavits alleged that there was probable cause to believe nine individuals, all named, were participating in a conspiracy to import and distribute narcotics in the Washington, D. C., area and that Geneva Jenkins’ telephone had been used in furtherance of the conspiracy, particularly by petitioner Thurmon, who was then living with Jenkins. The District Court granted the application on January 24, 1970, authorizing agents to “[ijntercept the wire communications of Alphonso H. Lee, Bernis Lee Thurmon, and other persons as may make use of the facilities hereinbefore described.” App. 80. The order also required the agents to conduct the wiretap in “such a way as to ,mini<page-number citation-index="1" label="132">*132</page-number>mize the interception of communications that are [not] otherwise subject to interception” under the Act<footnotemark>3</footnotemark> and to report to the court every five days “the progress of the interception and the nature of the communication intercepted.” <em>Ibid. </em>Interception began that same day and continued, pursuant to a judicially authorized extension, until February 24, 1970, with the agents making the periodic reports to the judge as required. Upon cessation of the interceptions, search and arrest warrants were executed which led to the arrest of 22 persons and the indictment of 14.</p>
<p id="b184-5">Before trial the defendants, including petitioners Scott and Thurmon, moved to suppress all the intercepted conversations on a variety of grounds. After comprehensive discovery and an extensive series of hearings, the District Court held that the agents had failed to comply with the minimization requirement contained in the wiretap order and ordered suppression of the intercepted conversations and all derivative evidence. The court relied in large part on the fact that virtually all the conversations were intercepted while only 40% of them were shown to be narcotics related. This, the court reasoned, “strongly indicate[d] the indiscriminate use of wire surveillance that was proscribed by Katz[<footnotemark>4</footnotemark>] and <em>Berger.” </em><footnotemark>5</footnotemark> <span class="citation" data-id="1401222"><a href="/opinion/1401222/united-states-v-scott/#247" aria-description="Citation for case: United States v. Scott">331 F. Supp. 233, 247</a></span> (DC 1971).</p>
<p id="b184-6">The Court of Appeals for the District of Columbia Circuit reversed and remanded, stating that the District Court should not have based its determination upon a general comparison of the number of narcotics-related calls with the total number of calls intercepted, but rather should have engaged in a particularized assessment of. the reasonableness of the agents’ attempts to minimize in light of the purpose of the wiretap and the information available to the agents at the time of <page-number citation-index="1" label="133">*133</page-number>interception. 164 U. S. App. D. C. 125, 129, <span class="citation" data-id="322190"><a href="/opinion/322190/united-states-v-frank-r-scott-united-states-of-america-v-bernis-l/#198" aria-description="Citation for case: United States v. Frank R. Scott United States of America...">504 F. 2d 194, 198</a></span> (1974).<footnotemark>6</footnotemark></p>
<p id="b185-5">Upon remand, the District Court again ordered suppression, this time relying largely on the fact that the agents were aware of the minimization requirement, “but made no attempt to comply therewith.” App. 37, 38.<footnotemark>7</footnotemark> “The admitted knowing <page-number citation-index="1" label="134">*134</page-number>and purposeful failure by the monitoring agents to comply with the minimization order was unreasonable . . . even if every intercepted call were narcotic-related.” <em>Id., </em>at 39.</p>
<p id="b186-5">The Court of Appeals again reversed, holding that the District Court had yet to apply the correct standard. 170 U. S. App. D. C. 158, <span class="citation" data-id="327713"><a href="/opinion/327713/united-states-v-frank-ricardo-scott-aka-reds-united-states-of/" aria-description="Citation for case: United States v. Frank Ricardo Scott, A/K/A &quot;Reds,&quot;...">516 F. 2d 751</a></span> (1975). The court recognized that the “presence or absence of a good faith attempt to minimize on the part of the agents is undoubtedly one factor to be considered in assessing whether the minimization requirement has been satisfied,” but went on to hold that “the decision on the suppression motion must ultimately be based on the reasonableness of the actual interceptions and not on whether the agents subjectively intended to minimize their interceptions.” <em>Id., </em>at 163, <span class="citation" data-id="327713"><a href="/opinion/327713/united-states-v-frank-ricardo-scott-aka-reds-united-states-of/#756" aria-description="Citation for case: United States v. Frank Ricardo Scott, A/K/A &quot;Reds,&quot;...">516 F. 2d, at 756</a></span>. Then, because of the extended period of time which had elapsed since the commission of the offense in question, that court itself examined the intercepted conversations and held that suppression was not appropriate in this case because the court could not conclude that “some conversation was intercepted which clearly would not have been intercepted had reasonable attempts at minimization been made.” <em>Id., </em>at 164, <span class="citation" data-id="327713"><a href="/opinion/327713/united-states-v-frank-ricardo-scott-aka-reds-united-states-of/#757" aria-description="Citation for case: United States v. Frank Ricardo Scott, A/K/A &quot;Reds,&quot;...">516 F. 2d, at 757</a></span>.<footnotemark>8</footnotemark></p>
<p id="b186-6">On the remand from the Court of Appeals, following a non jury trial on stipulated evidence which consisted primarily of petitioners’ intercepted conversations, Scott was found guilty of selling and purchasing narcotics not in the original stamped package, see <span class="citation no-link">26 U. S. C. §4704</span> (a) (1964 ed.), and Thurmon of conspiracy to sell narcotics, see <span class="citation no-link">26 U. S. C. §§ 7237</span> (b) and 4705 (a) (1964 ed.).<footnotemark>9</footnotemark> The Court of Appeals affirmed <page-number citation-index="1" label="135">*135</page-number>the convictions, 179 U. S. App. D. C. 281, <span class="citation" data-id="344017"><a href="/opinion/344017/patterson-v-d-c-board-of-parole/" aria-description="Citation for case: Patterson v. D. C. Board of Parole">551 F. 2d 467</a></span> (1977), and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./434/888/">434 U. S. 888</a></span> (1977).</p>
<p id="b187-5">II</p>
<p id="b187-6">Petitioners’ principal contention is that the failure to make good-faith efforts to comply with the minimization requirement is itself a violation of § 2518 (5). They urge that it is only after an assessment is made of the agents’ good-faith efforts, and presumably a determination that the agents did make such efforts, that one turns to the question of whether those efforts were reasonable under the circumstances. See Reply Brief for Petitioner <em>4r-5. </em>Thus, argue petitioners, Agent Cooper’s testimony, which is basically a concession that the Government made no efforts which resulted in the non-interception of any call, is dispositive of the matter. The so-called “call analysis,” which was introduced by the Government to suggest the reasonableness of intercepting most of the calls, cannot lead to a contrary conclusion because, having been prepared after the fact by a Government attorney and using terminology and categories which were not indicative of the agents’ thinking at the time of the interceptions, it does not reflect the perceptions and mental state of the agents who actually conducted the wiretap.</p>
<p id="b187-7">The Government responds that petitioners’ argument fails to properly distinguish between what is necessary to establish a statutory or constitutional violation and what is necessary to support a suppression remedy once a violation has been established.<footnotemark>10</footnotemark> In view of the deterrent purposes of the exclu<page-number citation-index="1" label="136">*136</page-number>sionary rule, consideration of official motives may play some part in determining whether application of the exclusionary rule is appropriate <em>after </em>a statutory or constitutional violation has been established. But the existence <em>vel non </em>of such a violation turns on an objective assessment of the officer’s actions in light of the facts and circumstances confronting him at the time. Subjective intent alone, the Government contends, does not make otherwise lawful conduct illegal or unconstitutional.<footnotemark>11</footnotemark></p>
<p id="b189-4"><page-number citation-index="1" label="137">*137</page-number>We think the Government’s position, which also served as the basis for decision in the Court of Appeals, embodies the proper approach for evaluating compliance with the minimization requirement. Although we have not examined this exact question at great length in any of our prior opinions, almost without exception in evaluating alleged violations of the Fourth Amendment the Court has first undertaken an objective assessment of an officer’s actions in light of the facts and circumstances then known to him. The language of the Amendment itself proscribes only “unreasonable” searches and seizures. In <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21-22</a></span> (1968), the Court emphasized the objective aspect of the term “reasonable.”</p>
<blockquote id="b189-5">“And in justifying the particular intrusion the police officer must be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant that intrusion. The scheme of the Fourth Amendment becomes meaningful only when it is assured that at some point the conduct of those charged with enforcing the laws can be subjected to the more detached, neutral scrutiny of a judge who must evaluate the reasonableness of a particular search or seizure in light of the particular circumstances. And in making that assessment it is imperative that the facts be judged against an objective standard; would the facts available to the officer at the moment of the seizure or the search 'warrant a man of reasonable caution in the belief’ that the action taken was appropriate?” (Footnotes omitted.)</blockquote>
<p id="b189-6">See also <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#96" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 96-97</a></span> (1964); <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#102" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 102-103</a></span> (1959).</p>
<p id="b190-4"><page-number citation-index="1" label="138">*138</page-number>We have since held that the fact that the officer does not have the state of mind which is hypothecated by the reasons which provide the legal justification for the officer’s action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action. In <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), a suspect was searched incident to a lawful arrest. He challenged the search on the ground that the motivation for the search did not coincide with the legal justification for the search-incident-to-arrest exception. We rejected this argument: “Since it is the fact of custodial arrest which gives rise to the authority to search, it is of no moment that [the officer] did not indicate any subjective fear of the respondent or that he did not himself suspect that respondent was armed.” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#236" aria-description="Citation for case: United States v. Robinson"><em>Id., </em>at 236</a></span>. The Courts of Appeals which have considered the matter have likewise generally followed these principles, first examining the challenged searches under a standard of objective reasonableness without regard to the underlying intent or motivation of the officers involved.<footnotemark>12</footnotemark></p>
<p id="b190-5">Petitioners do not appear, however, to rest their argument entirely on Fourth Amendment principles. Rather, they argue in effect that regardless of the search-and-seizure analysis conducted under the Fourth Amendment, the statute regulating wiretaps requires the agents to make good-faith efforts at <page-number citation-index="1" label="139">*139</page-number>minimization, and the failure to make such efforts is itself a violation of the statute which requires suppression.</p>
<p id="b191-5">This argument fails for more than one reason. In the first place, in the very section in which it directs minimization Congress, by its use of the word “conducted,” made it clear that the focus was to be on the agents’ actions not their motives. Any lingering doubt is dispelled by the legislative history which, as we have recognized before in another context, declares that § 2515 was not intended “generally to press the scope of the suppression role beyond present search and seizure law.” S. Rep. No. 1097, 90th Cong., 2d Sess., 96 (1968). See <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 175-176</a></span> (1969).<footnotemark>13</footnotemark></p>
<p id="b191-6">III</p>
<p id="b191-7">We turn now to the Court of Appeals’ analysis of the reasonableness of the agents’ conduct in intercepting all of the calls in this particular wiretap. Because of the necessarily ad hoc nature of any determination of reasonableness, there can be no inflexible rule of law which will decide every case. <page-number citation-index="1" label="140">*140</page-number>The statute does not forbid the interception of all nonrelevant conversations, but rather instructs the agents to conduct the surveillance in such a manner as to “minimize” the interception of such conversations. Whether the agents have in fact conducted the wiretap in such a manner will depend on the facts and circumstances of each case.</p>
<p id="b192-5">We agree with the Court of Appeals that blind reliance on the percentage of nonpertinent calls intercepted is not a sure guide to the correct answer. Such percentages may provide assistance, but there are surely cases, such as the one at bar, where the percentage of nonpertinent calls is relatively high and yet their interception was still reasonable. The reasons for this may be many. Many of the nonpertinent calls may have been very short. Others may have been one-time only calls. Still other calls may have been ambiguous in nature or apparently involved guarded or coded language. In all these circumstances agents can hardly be expected to know that the calls are not pertinent prior to their termination.</p>
<p id="b192-6">In determining whether the agents properly minimized, it is also important to consider the circumstances of the wiretap. For example, when the investigation is focusing on what is thought to be a widespread conspiracy more extensive surveillance may be justified in an attempt to determine the precise scope of the enterprise. And it is possible that many more of the conversations will be permissibly interceptable because they will involve one or more of the co-conspirators. The type of use to which the telephone is normally put may also have some bearing on the extent of minimization required. For example, if the agents are permitted to tap a public telephone because one individual is thought to be placing bets over the phone, substantial doubts as to minimization may arise if the agents listen to every call which goes out over that phone regardless of who places the call. On the other hand, if the phone is located in the residence of a person who is thought to be the head of a major drug ring, a contrary conclusion may be indicated.</p>
<p id="b193-4"><page-number citation-index="1" label="141">*141</page-number>Other factors may also play a significant part in a particular case. For example, it may be important to determine at exactly what point during the authorized period the interception was made. During the early stages of surveillance the agents may be forced to intercept all calls to establish categories of nonpertinent calls which will not be intercepted thereafter. Interception of those same types of calls might be unreasonable later on, however, once the nonpertinent categories have been established and it is clear that this particular conversation is of that type. Other situations may arise where patterns of nonpertinent calls do not appear. In these circumstances it may not be unreasonable to intercept almost every short conversation because the determination of relevancy cannot be made before the call is completed.</p>
<p id="b193-5">After consideration of the minimization claim in this case in the light of these observations, we find nothing to persuade us that the Court of Appeals was wrong in its rejection of that claim.<footnotemark>14</footnotemark> Forty percent of the calls were clearly narcotics related and the propriety of their interception is, of course, not in dispute. Many of the remaining calls were very short, such as wrong-number calls, calls to persons who were not available to come to the phone, and calls to the telephone company to <page-number citation-index="1" label="142">*142</page-number>hear the recorded weather message which lasts less than 90 seconds. In a case such as this, involving a wide-ranging conspiracy with a large number of participants, even a seasoned listener would have been hard pressed to determine with any precision the relevancy of many of the calls before they were completed.<footnotemark>15</footnotemark> A large number were ambiguous in nature, making characterization virtually impossible until the completion of these calls. And some of the nonpertinent conversations were one-time conversations. Since these calls did not give the agents an opportunity to develop a category of innocent calls which should not have been intercepted, their interception cannot be viewed as a violation of the minimization requirement.</p>
<p id="b194-5">We are thus left with the seven calls between Jenkins and her mother. The first four calls were intercepted over a three-day period at the very beginning of the surveillance. They were of relatively short length and at least two of them indicated that the mother may have known of the conspiracy. The next two calls, which occurred about a week later, both contained statements from the mother to the effect that she had something to tell Jenkins regarding the “business” but did not want to do so over the phone. The final call was substantially longer and likewise contained a statement which could have been interpreted as having some bearing on the conspiracy, <em>i. e., </em>that one “Reds,” a suspect in the conspiracy, <page-number citation-index="1" label="143">*143</page-number>had called to ask for a telephone number. Although none of these conversations turned out to be material to the investigation at hand, we cannot say that the Court of Appeals was incorrect in concluding that the agents did not act unreasonably at the time they made these interceptions. Its judgment is accordingly</p>
<p id="b195-5">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b182-11"> See <em>United States </em>v. <em>Donovan, </em><span class="citation" data-id="9426645"><a href="/opinion/109584/united-states-v-donovan/" aria-description="Citation for case: United States v. Donovan">429 U. S. 413</a></span> (1977), which involved that part of the Act which requires the Government to identify the person, if known, whose conversations are to be intercepted.</p>
</footnote>
<footnote label="2">
<p id="b183-6"> The application and subsequent court order identified the subscriber as Geneva Thornton, but that was apparently an alias. <span class="citation" data-id="1401222"><a href="/opinion/1401222/united-states-v-scott/#236" aria-description="Citation for case: United States v. Scott">331 F. Supp. 233, 236</a></span> (DC 1971).</p>
</footnote>
<footnote label="3">
<p id="b184-7"> The word “not” was inadvertently omitted, but the agents apparently understood the intent of the order. <em><span class="citation" data-id="1401222"><a href="/opinion/1401222/united-states-v-scott/" aria-description="Citation for case: United States v. Scott">Id.,</a></span> </em>at 245 n. 1.</p>
</footnote>
<footnote label="4">
<p id="b184-8"><em> Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967).</p>
</footnote>
<footnote label="5">
<p id="b184-9"> <em>Berger </em>v. <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York"><em>New York, 388 </em>U. S. 41</a></span> (1967).</p>
</footnote>
<footnote label="6">
<p id="b185-6"> The District Court also made a number of other related rulings which were affirmed on appeal. It upheld Title III against a claim that the statute contravened the Fourth Amendment restriction against unreasonable searches and seizures; determined that the application and affidavits were sufficient on their face to establish probable cause; and held that the order complied with the requirements of the statute. Petitioners have not sought review of any of these holdings. The Court of Appeals; also held that Scott could introduce evidence based on conversations in which he did not participate to demonstrate that the intercepted conversations to which he was a party were not seized “in conformity with the order of authorization.” <span class="citation no-link">18 U. S. C. §2518</span> (10) (a) (iii) (1976 ed.). See 164 U. S. App. D. C., at 127-128, <span class="citation" data-id="322190"><a href="/opinion/322190/united-states-v-frank-r-scott-united-states-of-america-v-bernis-l/#196" aria-description="Citation for case: United States v. Frank R. Scott United States of America...">504 F. 2d, at 196-197</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b185-12"> This conclusion was based on the fact that virtually all calls were intercepted and on the testimony of Special Agent Glennon Cooper, the agent in charge of the investigation, who testified that the only steps taken which actually resulted in the nonreception of a conversation were those taken when the agents discovered the wiretap had inadvertently been connected to an improper line. The court laid particular stress on the following exchange:</p>
<blockquote id="b185-13">“BY THE COURT:</blockquote>
<blockquote id="b185-14">“Q. The question I wish to ask you is this, whether at any time during the course of the wiretap — of the intercept, what if any steps were taken by you or any agent under you to minimize the listening?</blockquote>
<blockquote id="b185-15">“A. Well, as I believe I mentioned before, I would have to say that the only effective steps taken by us to curtail the reception of conversations was in that instance where the line was connected to — misconnected from the correct line and connected to an improper line. We discontinued at that time.</blockquote>
<blockquote id="b185-16">“Q. Do I understand from you then that the only time that you considered minimization was when you found that you had been connected with a wrong number?</blockquote>
<blockquote id="b185-17">“A. That is correct, Your Honor.” App. 179.</blockquote>
</footnote>
<footnote label="8">
<p id="b186-7"> The Court of Appeals, with four judges dissenting, denied rehearing and rehearing en banc, 173 U. S. App. D. C. 118, <span class="citation" data-id="330164"><a href="/opinion/330164/united-states-v-frank-ricardo-scott-aka-reds-united-states-of-america/" aria-description="Citation for case: United States v. Frank Ricardo Scott, A/K/A &quot;Reds&quot; United...">522 F. 2d 1333</a></span> (1975), and we denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./425/917/">425 U. S. 917</a></span> (1976). Mr. Justice Brennan, Mr. Justice Marshall, and Mr. Justice Powell dissented from the denial of certiorari.</p>
</footnote>
<footnote label="9">
<p id="b186-8"> The specific statutes under which petitioners were convicted were repealed in connection with the enactment of the Comprehensive Drug Abuse Prevention and Control Act of 1970, <span class="citation no-link">84 Stat. 1292</span>.</p>
</footnote>
<footnote label="10">
<p id="b187-8"> The Government also argues that even if the agents in this ease violated the minimization requirement by intercepting some conversations which could not have reasonably been intercepted, § 2518 (10) requires suppression of only those conversations which were illegally intercepted, not suppression of all the intercepted conversations. See, e. <em>g., United States </em>v. <em>Cox, </em><span class="citation" data-id="8888268"><a href="/opinion/8901364/united-states-v-cox/#1301" aria-description="Citation for case: United States v. Cox">462 F. 2d 1293, 1301-1302</a></span> (CA8 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./417/918/">417 U. S. 918</a></span> (1974); <em>United States </em>v. <em>Sisca, </em><span class="citation" data-id="1602011"><a href="/opinion/1602011/united-states-v-sisca/#746" aria-description="Citation for case: United States v. Sisca">361 F. Supp. 735, 746-747</a></span> <page-number citation-index="1" label="136">*136</page-number>(SDNY 1973), aff’d, <span class="citation" data-id="321972"><a href="/opinion/321972/united-states-v-alphonse-sisca/" aria-description="Citation for case: United States v. Alphonse Sisca">503 F. 2d 1337</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1008/">419 U. S. 1008</a></span> (1974); <em>United States </em>v. <em>Mainello, </em><span class="citation" data-id="1891738"><a href="/opinion/1891738/united-states-v-mainello/#874" aria-description="Citation for case: United States v. Mainello">345 F. Supp. 863, 874-877</a></span> (EDNY 1972); <em>United States </em>v. <em>LaGorga, </em><span class="citation" data-id="1795377"><a href="/opinion/1795377/united-states-v-lagorga/" aria-description="Citation for case: United States v. LaGorga">336 F. Supp. 190</a></span> (WD Pa. 1971). It also renews its argument that petitioner Scott does not have standing to raise a minimization challenge based upon the interception of conversations to which he was not a party. To permit such a challenge would allow Scott to secure the suppression of evidence against him by showing that the rights of other parties were violated. This, argues the Government, would contravene well-settled principles of Fourth Amendment law, cf. <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#230" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 230</a></span> (1973); <em>Alderman </em>v. <em>United States, </em><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#197" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 197</a></span> (1969); <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968), which clearly apply to Title III cases, see S. Rep. No. 1097, 90th Cong., 2d Sess., 91, 106 (1968); <em>Alderman </em>v. <em>United States, supra, </em>at 175-176.</p>
<p id="b188-5">Given our disposition of this case we find it unnecessary to reach the Government’s contention regarding the sco'pe of the suppression remedy in the event of a violation of the minimization requirement. We also decline to address the Government’s argument with respect to standing. The Government concedes that petitioner Thurmon was a party to some nonnarcotics-related calls and thus has standing to make the arguments advanced herein. Thus, even if we were to decide that Scott has no standing we would be compelled to undertake the decision of these issues. If, on the other hand, we were to decide that Scott does have standing, we would simply repeat exactly the same analysis made with respect to Thurmon’s claim and find against Scott as well. In this circumstance we need not decide the questions of Scott’s standing. See <em>California Bankers </em>Assn. v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#44" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 44-45</a></span> (1974); <em>Doe </em>v. <em>Bolton, </em><span class="citation" data-id="9425160"><a href="/opinion/108714/doe-v-bolton/#189" aria-description="Citation for case: Doe v. Bolton">410 U. S. 179, 189</a></span> (1973).</p>
</footnote>
<footnote label="11">
<p id="b188-6"> The Government also adds that even if subjective intent were the standard, the record does not support the District Court’s conclusion that <page-number citation-index="1" label="137">*137</page-number>the agents subjectively intended to violate the statute or the Constitution. It contends that the failure to stop intercepting calls, the interception of which was entirely reasonable, does not support a finding that the agents would have intercepted calls that should not have been intercepted had they been confronted with that situation. We express no view on this matter.</p>
</footnote>
<footnote label="12">
<p id="b190-6"> See, <em>e. g., United States </em>v. <em>Bugarin-Casas, </em><span class="citation" data-id="313456"><a href="/opinion/313456/united-states-v-salvador-bugarin-casas/" aria-description="Citation for case: United States v. Salvador Bugarin-Casas">484 F. 2d 853</a></span>, 854 n. 1 (CA9 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1136/">414 U. S. 1136</a></span> (1974) (“The fact that the agents were intending at the time they stopped the car to search it in any event . . . does not render the search, supported by independent probable cause, invalid”); <em>Dodd </em>v. <em>Beto, </em><span class="citation multiple-matches"><a href="/c/F.%202d/435/868/">435 F. 2d 868</a></span>, 870 (CA5 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/845/">404 U. S. 845</a></span> (1971); <em>Klingler </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/F.%202d/409/299/">409 F. 2d 299</a></span>, 304 (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/859/">396 U. S. 859</a></span> (1969); <em>Green </em>v. <em>United States, </em><span class="citation" data-id="8878037"><a href="/opinion/8891764/green-v-united-states/#956" aria-description="Citation for case: Green v. United States">386 F. 2d 953, 956</a></span> (CA10 1967); <em>Sirimarco </em>v. <em>United States, </em><span class="citation" data-id="9449132"><a href="/opinion/260186/anthony-sirimarco-v-united-states/#702" aria-description="Citation for case: Anthony Sirimarco v. United States">315 F. 2d 699, 702</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./374/807/">374 U. S. 807</a></span> (1963). As is our usual custom, we do not, in citing these or other cases, intend to approve any particular language or holding in them.</p>
</footnote>
<footnote label="13">
<p id="b191-8"> This is not to say, of course, that the question of motive plays absolutely no part in the suppression inquiry. On occasion, the motive with which the officer conducts an illegal search may have some relevance in determining the propriety of applying the exclusionary rule. For example, in <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#458" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 458</a></span> (1976), we ruled that evidence unconstitutionally seized by state police could be introduced in federal civil tax proceedings because “the imposition of the exclusionary rule ... is unlikely to provide significant, much less substantial, additional deterrence. It falls outside the offending officer’s zone of primary interest.” See also <em>United States </em>v. <em>Ceccolini, </em><span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#276" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 276-277</a></span> (1978). This focus on intent, however, becomes relevant only after it has been determined that the Constitution was in fact violated. We also have little doubt that as a practical matter the judge’s assessment of the motives of the officers may occasionally influence his judgment regarding the credibility of the officers’ claims with respect to what information was or was not available to them at the time of the incident in question. But the assessment and use of motive in this limited manner is irrelevant to our analysis of the questions at issue in this case.</p>
</footnote>
<footnote label="14">
<p id="b193-6"> Petitioners argue that the “district court found that the call analysis contained errors of characterization and factual inaccuracies and did not represent information known to the agents at the time of interception.” Brief for Petitioners 25-26. We do not think petitioners have fairly characterized the District Court’s findings, however. The District Court found: “The 'call analysis’ conflicts with the reports and characterizations of the intercepted calls as made and determined by the monitoring agents whose conduct is controlling in this case.” App. 38. This does not suggest that the call analysis was factually erroneous, but rather that the categories used by the attorney who prepared the analysis were not necessarily of the same sort employed by the monitoring agents. This finding would thus have relevance if the critical inquiry focused on the subjective intent of the agents, but it certainly cannot be read as a finding that the general analysis of the calls set forth in the call analysis contains "factual inaccuracies.”</p>
</footnote>
<footnote label="15">
<p id="b194-6"> Petitioners intimate that the scope of the investigation was narrower than originally anticipated because the intercepts revealed only local purchases within the Washington area. That certainly has no bearing on what the officers had reasonable cause to believe at the time they made the interceptions, however. And while it is true that the conspiracy turned out to involve mainly local distribution, rather than major interstate and international importation, it is not at all clear that the information garnered through the wiretap reduced the agents’ estimates of the number of people involved or the extent of the drug traffic. In short, there is little doubt on the record that, as the agents originally thought, the conspiracy can fairly be characterized as extensive.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Screws v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Screws v. United States"
type: case
citation: "325 U.S. 91 (1945)"
parallel_cite: "65 S. Ct. 1031; 89 L. Ed. 1495; 162 A.L.R. 1330"
neutral_cite: 1945 U.S. LEXIS 2096
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1945
date_decided: 1945-05-07
docket: 42
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1945-05-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Screws v. United States
  varies_by_point: false
  scope_note: "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of § 242 remains the controlling reading."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104135/screws-v-united-states/"
  cluster_id: 104135
  opinion_id: 104135
  identity_checked: true
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: "Related (cross-doctrine)"
related: ["[[Monroe v. Pape]]"]
aliases: []
tags: ["case", "civil-rights", "color-of-law", "section-242", "willfulness"]
holding: "Construing 18 U.S.C. § 242 'willfully' — the criminal civil-rights statute requires a specific-intent (willful) deprivation of constitutional rights under color of law."
lake:
  record_id: Screws v. United States
  status: verified
  projected_at: 2026-07-06
---

# Screws v. United States

*325 U.S. 91 (1945)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Georgia sheriff M. Claude Screws and two other officers arrested Robert Hall, a young Black man, and beat him to death with their fists and a blackjack. They were convicted under the criminal civil-rights statute (now 18 U.S.C. § 242) of willfully depriving Hall, [[Section 1983 Liability and Qualified Immunity|under color of law]], of rights secured by the Constitution. They argued the statute was unconstitutionally vague.

## Issue
Whether § 242's prohibition on willfully depriving a person of constitutional rights [[Section 1983 Liability and Qualified Immunity|under color of law]] is void for vagueness, and what mental state "willfully" requires.

## Rule
The statute is saved from vagueness by reading "willfully" to require specific intent. "We do say that a requirement of a specific intent to deprive a person of a federal right made definite by decision or other rule of law saves the Act from any charge of unconstitutionality on the grounds of vagueness." — 325 U.S. at 103. ^pin-103

The Court also reaffirmed that action "under color of" state law includes the misuse of authority an officer possesses only because he is clothed with his official position.

## Application
Because the trial court had not instructed the jury that the defendants must have acted with the specific intent to deprive Hall of a federal constitutional right, the convictions could not stand under the proper construction of "willfully," and the Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for a new trial under that standard.

## Conclusion
Section 242 is not void for vagueness when read to require a willful—specific-intent—deprivation; the convictions were reversed for the faulty jury instruction and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Douglas, J., announced the judgment).
- The specific-intent construction of § 242 remains the controlling reading, and *Screws*'s "under color of law" analysis informs civil liability under § 1983 ([[Monroe v. Pape]]).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Related (cross-doctrine)*

## Sources
- *Screws v. United States*, 325 U.S. 91 (1945) — https://www.courtlistener.com/opinion/104135/screws-v-united-states/ — pinpoint: 103.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7fbde5eaf27f52da", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Screws v. United States"}, "payload": {"all": [{"cite": "325 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "325"}, {"cite": "65 S. Ct. 1031", "page": "1031", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "89 L. Ed. 1495", "page": "1495", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "1945 U.S. LEXIS 2096", "page": "2096", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1945"}, {"cite": "162 A.L.R. 1330", "page": "1330", "reporter": "A.L.R.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "162"}], "display": "325 U.S. 91", "official": {"cite": "325 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "325"}, "official_selection_present": true, "record_id": "Screws v. United States"}}
{"assertion_id": "0a444ab7ab695da9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-103", "record_id": "Screws v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-103", "pinpoint_status": "slip-only", "quote": "requires. ## Rule The statute is saved from vagueness by reading", "quote_fidelity": "mismatch", "record_id": "Screws v. United States", "star_marker": null}}
{"assertion_id": "68ef81d6e3551bfa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Screws v. United States"}, "payload": {"as_of_content": "1945-05-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Screws v. United States", "scope_note": "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of § 242 remains the controlling reading.", "varies_by_point": false}}
```

### lake record — Screws v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Screws v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Screws v. United States",
    "case_name_short": "Screws",
    "case_name_full": "SCREWS Et Al. v. UNITED STATES",
    "input_case_name": "Screws v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1945-05-07",
    "year": 1945,
    "docket": "42",
    "cluster_id": 104135,
    "lead_opinion_id": 104135,
    "sibling_ids": [
      104135,
      9419636,
      9419637,
      9419638,
      9419639
    ],
    "absolute_url": "/opinion/104135/screws-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "325 U.S. 91",
      "volume": "325",
      "reporter": "U.S.",
      "page": "91",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "65 S. Ct. 1031",
        "volume": "65",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 1495",
        "volume": "89",
        "reporter": "L. Ed.",
        "page": "1495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "162 A.L.R. 1330",
        "volume": "162",
        "reporter": "A.L.R.",
        "page": "1330",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1945 U.S. LEXIS 2096",
        "volume": "1945",
        "reporter": "U.S. LEXIS",
        "page": "2096",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "325 U.S. 91",
        "volume": "325",
        "reporter": "U.S.",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 S. Ct. 1031",
        "volume": "65",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 L. Ed. 1495",
        "volume": "89",
        "reporter": "L. Ed.",
        "page": "1495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1945 U.S. LEXIS 2096",
        "volume": "1945",
        "reporter": "U.S. LEXIS",
        "page": "2096",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "162 A.L.R. 1330",
        "volume": "162",
        "reporter": "A.L.R.",
        "page": "1330",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "325 U.S. 91",
    "official_selection": {
      "court_class": "scotus",
      "selected": "325 U.S. 91",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-103",
      "page": null,
      "quote": "requires. ## Rule The statute is saved from vagueness by reading",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1945-05-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Screws v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality (Douglas, J., announcing the judgment); the specific-intent construction of \u00a7 242 remains the controlling reading.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Kelly",
          "cluster_id": 2780739,
          "cite": [
            "470 Mass. 682",
            "25 N.E.3d 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dustin Myers v. Murry Bowman",
          "cluster_id": 857864,
          "cite": [
            "713 F.3d 1319",
            "2013 WL 1442055",
            "2013 U.S. App. LEXIS 7216",
            "24 Fla. L. Weekly Fed. C 194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Winot",
          "cluster_id": 1545853,
          "cite": [
            "988 A.2d 188",
            "294 Conn. 753",
            "2010 Conn. LEXIS 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Franco Andre Goyzueta v. State",
          "cluster_id": 2853303,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellee-Cross-Appellant v. Eva C. Temple, Appellant-Cross-Appellee",
          "cluster_id": 794242,
          "cite": [
            "447 F.3d 130",
            "97 A.F.T.R.2d (RIA) 2265",
            "2006 U.S. App. LEXIS 10885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monell v. New York City Dept. of Social Servs.",
          "cluster_id": 109881,
          "cite": [
            "56 L. Ed. 2d 611",
            "98 S. Ct. 2018",
            "436 U.S. 658",
            "1978 U.S. LEXIS 100",
            "16 Empl. Prac. Dec. (CCH) 8345",
            "17 Fair Empl. Prac. Cas. (BNA) 873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adickes v. S. H. Kress & Co.",
          "cluster_id": 108153,
          "cite": [
            "26 L. Ed. 2d 142",
            "90 S. Ct. 1598",
            "398 U.S. 144",
            "1970 U.S. LEXIS 31"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolff v. McDonnell",
          "cluster_id": 109097,
          "cite": [
            "41 L. Ed. 2d 935",
            "94 S. Ct. 2963",
            "418 U.S. 539",
            "1974 U.S. LEXIS 91",
            "71 Ohio Op. 2d 336"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
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
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parratt v. Taylor",
          "cluster_id": 110478,
          "cite": [
            "68 L. Ed. 2d 420",
            "101 S. Ct. 1908",
            "451 U.S. 527",
            "1981 U.S. LEXIS 99",
            "49 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Polk County v. Dodson",
          "cluster_id": 110589,
          "cite": [
            "70 L. Ed. 2d 509",
            "102 S. Ct. 445",
            "454 U.S. 312",
            "1981 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul v. Davis",
          "cluster_id": 109402,
          "cite": [
            "47 L. Ed. 2d 405",
            "96 S. Ct. 1155",
            "424 U.S. 693",
            "1976 U.S. LEXIS 112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koon v. United States",
          "cluster_id": 118044,
          "cite": [
            "135 L. Ed. 2d 392",
            "116 S. Ct. 2035",
            "518 U.S. 81",
            "1996 U.S. LEXIS 3877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffman Estates v. Flipside, Hoffman Estates, Inc.",
          "cluster_id": 110661,
          "cite": [
            "71 L. Ed. 2d 362",
            "102 S. Ct. 1186",
            "455 U.S. 489",
            "1982 U.S. LEXIS 78",
            "50 U.S.L.W. 4267"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Shea v. Littleton",
          "cluster_id": 108906,
          "cite": [
            "38 L. Ed. 2d 674",
            "94 S. Ct. 669",
            "414 U.S. 488",
            "1974 U.S. LEXIS 41"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Breckenridge",
          "cluster_id": 108362,
          "cite": [
            "29 L. Ed. 2d 338",
            "91 S. Ct. 1790",
            "403 U.S. 88",
            "1971 U.S. LEXIS 3774",
            "3 Empl. Prac. Dec. (CCH) 8284",
            "9 Fair Empl. Prac. Cas. (BNA) 1196"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morissette v. United States",
          "cluster_id": 104952,
          "cite": [
            "96 L. Ed. 2d 288",
            "72 S. Ct. 240",
            "342 U.S. 246",
            "1952 U.S. LEXIS 2714",
            "96 L. Ed. 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez",
          "cluster_id": 117927,
          "cite": [
            "131 L. Ed. 2d 626",
            "115 S. Ct. 1624",
            "514 U.S. 549",
            "1995 U.S. LEXIS 3039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Golding",
          "cluster_id": 7893833,
          "cite": [
            "213 Conn. 233",
            "567 A.2d 823",
            "1989 Conn. LEXIS 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hamdi v. Rumsfeld",
          "cluster_id": 137001,
          "cite": [
            "159 L. Ed. 2d 578",
            "124 S. Ct. 2633",
            "542 U.S. 507",
            "2004 U.S. LEXIS 4761"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Papachristou v. City of Jacksonville",
          "cluster_id": 108472,
          "cite": [
            "31 L. Ed. 2d 110",
            "92 S. Ct. 839",
            "405 U.S. 156",
            "1972 U.S. LEXIS 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parker v. Levy",
          "cluster_id": 109077,
          "cite": [
            "41 L. Ed. 2d 439",
            "94 S. Ct. 2547",
            "417 U.S. 733",
            "1974 U.S. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harriss",
          "cluster_id": 105232,
          "cite": [
            "98 L. Ed. 2d 989",
            "74 S. Ct. 808",
            "347 U.S. 612",
            "1954 U.S. LEXIS 2657",
            "98 L. Ed. 989"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner Broadcasting System, Inc. v. Federal Communications Commission",
          "cluster_id": 117869,
          "cite": [
            "129 L. Ed. 2d 497",
            "114 S. Ct. 2445",
            "512 U.S. 622",
            "1994 U.S. LEXIS 4831"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Sparks",
          "cluster_id": 110353,
          "cite": [
            "66 L. Ed. 2d 185",
            "101 S. Ct. 183",
            "449 U.S. 24",
            "1980 U.S. LEXIS 9",
            "49 U.S.L.W. 4001"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. Houston Welfare Rights Organization",
          "cluster_id": 110076,
          "cite": [
            "60 L. Ed. 2d 508",
            "99 S. Ct. 1905",
            "441 U.S. 600",
            "1979 U.S. LEXIS 101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Goguen",
          "cluster_id": 108988,
          "cite": [
            "39 L. Ed. 2d 605",
            "94 S. Ct. 1242",
            "415 U.S. 566",
            "1974 U.S. LEXIS 113"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Screws v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDk4MDU3NjAwMDAwJnM9MzY0NzYmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NzImcz0xMDk5NjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104135 OR 9419636 OR 9419637 OR 9419638 OR 9419639)",
    "indexed_citing_opinions": 1336,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104135,
        "count": 1235,
        "count_source": "search"
      },
      {
        "opinion_id": 9419636,
        "count": 142,
        "count_source": "search"
      },
      {
        "opinion_id": 9419637,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9419638,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9419639,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2025,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/screws-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMDIwNDMmcz05Mzg4MjcwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28104135+OR+9419636+OR+9419637+OR+9419638+OR+9419639%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104135,
        "cited_id": 85535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 90897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 91704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 92834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 93322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 95097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 95317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96819,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 96905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 97928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98220,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98518,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 98682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 99947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101106,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101955,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 101991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102166,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102804,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 102970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103632,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103753,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 103998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1087658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1087739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1410732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1410842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1447641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1480783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1500930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1511950,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1564666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1567036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1620902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1739405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 1755008,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 2394729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104135,
        "cited_id": 2620779,
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
    "date_created": "2026-07-05T18:47:38Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:57:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:47:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Screws v. United States (truncated)

```
<div>
<center><b><span class="citation" data-id="9419636"><a href="/opinion/104135/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">325 U.S. 91</a></span> (1945)</b></center>
<center><h1>SCREWS ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 42.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 20, 1944.</center>
<center>Decided May 7, 1945.</center>
CERTIORARI TO THE CIRCUIT COURT OF APPEALS FOR THE FIFTH CIRCUIT.
<p><span class="star-pagination">*92</span> <i>Mr. James F. Kemp,</i> with whom <i>Messrs. Clint W. Hager</i> and <i>Robert B. Short</i> were on the brief, for petitioners.</p>
<p><i>Solicitor General Fahy,</i> with whom <i>Assistant Attorney General Tom C. Clark, Messrs. Robert S. Erdahl</i> and <i>Irving S. Shapiro</i> were on the brief, for the United States.</p>
<p><i>Messrs. William H. Hastie, Thurgood Marshall</i> and <i>Leon A. Ransom</i> filed a brief on behalf of the National Association for the Advancement of Colored People, as <i>amicus curiae,</i> urging affirmance.</p>
<p>MR. JUSTICE DOUGLAS announced the judgment of the Court and delivered the following opinion, in which the CHIEF JUSTICE, MR. JUSTICE BLACK and MR. JUSTICE REED concur.</p>
<p>This case involves a shocking and revolting episode in law enforcement. Petitioner Screws was sheriff of Baker County, Georgia. He enlisted the assistance of petitioner Jones, a policeman, and petitioner Kelley, a special deputy, in arresting Robert Hall, a citizen of the United States and of Georgia. The arrest was made late at night at Hall's home on a warrant charging Hall with theft of a tire. Hall, a young negro about thirty years of age, was handcuffed and taken by car to the court house. As Hall alighted from the car at the court-house square, the three petitioners began beating him with their fists and with a solid-bar blackjack about eight inches long and weighing two pounds. They claimed Hall had reached for a gun and had used insulting language as he alighted from the <span class="star-pagination">*93</span> car. But after Hall, still handcuffed, had been knocked to the ground they continued to beat him from fifteen to thirty minutes until he was unconscious. Hall was then dragged feet first through the court-house yard into the jail and thrown upon the floor dying. An ambulance was called and Hall was removed to a hospital where he died within the hour and without regaining consciousness. There was evidence that Screws held a grudge against Hall and had threatened to "get" him.</p>
<p>An indictment was returned against petitioners  one count charging a violation of § 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 52</span> and another charging a conspiracy to violate § 20 contrary to § 37 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 88</span>. Sec. 20 provides:</p>
<p>"Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects, or causes to be subjected, any inhabitant of any State, Territory, or District to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States, or to different punishments, pains, or penalties, on account of such inhabitant being an alien, or by reason of his color, or race, than are prescribed for the punishment of citizens, shall be fined not more than $1,000, or imprisoned not more than one year, or both." The indictment charged that petitioners, acting under color of the laws of Georgia, "willfully" caused Hall to be deprived of "rights, privileges, or immunities secured or protected" to him by the Fourteenth Amendment  the right not to be deprived of life without due process of law; the right to be tried, upon the charge on which he was arrested, by due process of law and if found guilty to be punished in accordance with the laws of Georgia; that is to say that petitioners "unlawfully and wrongfully did assault, strike and beat the said Robert Hall about the head with human fists and a blackjack causing injuries" to Hall "which were the proximate and immediate cause <span class="star-pagination">*94</span> of his death." A like charge was made in the conspiracy count.</p>
<p>The case was tried to a jury.<sup>[1]</sup> The court charged the jury that due process of law gave one charged with a crime the right to be tried by a jury and sentenced by a court. On the question of intent it charged that</p>
<p>". . . if these defendants, without its being necessary to make the arrest effectual or necessary to their own personal protection, beat this man, assaulted him or killed him while he was under arrest, then they would be acting illegally under color of law, as stated by this statute, and would be depriving the prisoner of certain constitutional rights guaranteed to him by the Constitution of the United States and consented to by the State of Georgia."</p>
<p>The jury returned a verdict of guilty and a fine and imprisonment on each count was imposed. The Circuit Court of Appeals affirmed the judgment of conviction, one judge dissenting. <span class="citation" data-id="9653538"><a href="/opinion/1567036/screws-v-united-states/" aria-description="Citation for case: Screws v. United States">140 F.2d 662</a></span>. The case is here on a petition for a writ of certiorari which we granted because of the importance in the administration of the criminal laws of the questions presented.</p>
<p></p>
<h2>I</h2>
<p>We are met at the outset with the claim that § 20 is unconstitutional, insofar as it makes criminal acts in violation of the due process clause of the Fourteenth Amendment. The argument runs as follows: It is true that this Act as construed in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#328" aria-description="Citation for case: United States v. Classic">313 U.S. 299, 328</a></span>, was upheld in its application to certain ballot box frauds committed by state officials. But in that case the constitutional rights protected were the rights to vote <span class="star-pagination">*95</span> specifically guaranteed by Art. I, § 2 and § 4 of the Constitution. Here there is no ascertainable standard of guilt. There have been conflicting views in the Court as to the proper construction of the due process clause. The majority have quite consistently construed it in broad general terms. Thus it was stated in <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#101" aria-description="Citation for case: Twining v. New Jersey">211 U.S. 78, 101</a></span>, that due process requires that "no change in ancient procedure can be made which disregards those fundamental principles, to be ascertained from time to time by judicial action, which have relation to process of law and protect the citizen in his private right, and guard him against the arbitrary action of government." In <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U.S. 97, 105</a></span>, it was said that due process prevents state action which "offends some principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental." The same standard was expressed in <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U.S. 319, 325</a></span>, in terms of a "scheme of ordered liberty." And the same idea was recently phrased as follows: "The phrase formulates a concept less rigid and more fluid than those envisaged in other specific and particular provisions of the Bill of Rights. Its application is less a matter of rule. Asserted denial is to be tested by an appraisal of the totality of facts in a given case. That which may, in one setting, constitute a denial of fundamental fairness, shocking to the universal sense of justice, may, in other circumstances, and in the light of other considerations, fall short of such denial." <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#462" aria-description="Citation for case: Betts v. Brady">316 U.S. 455, 462</a></span>.</p>
<p>It is said that the Act must be read as if it contained those broad and fluid definitions of due process and that if it is so read it provides no ascertainable standard of guilt. It is pointed out that in <i>United States</i> v. <i>Cohen Grocery Co.,</i> <span class="citation" data-id="9418445"><a href="/opinion/99713/united-states-v-l-cohen-grocery-co/#89" aria-description="Citation for case: United States v. L. Cohen Grocery Co.">255 U.S. 81, 89</a></span>, an Act of Congress was struck down, the enforcement of which would have been "the exact equivalent of an effort to carry out a statute <span class="star-pagination">*96</span> which in terms merely penalized and punished all acts detrimental to the public interest when unjust and unreasonable in the estimation of the court and jury." In that case the act declared criminal was the making of "any unjust or unreasonable rate or charge in handling or dealing in or with any necessaries." 255 U.S. p. 86. The Act contained no definition of an "unjust or unreasonable rate" nor did it refer to any source where the measure of "unjust or unreasonable" could be ascertained. In the instant case the decisions of the courts are, to be sure, a source of reference for ascertaining the specific content of the concept of due process. But even so the Act would incorporate by reference a large body of changing and uncertain law. That law is not always reducible to specific rules, is expressible only in general terms, and turns many times on the facts of a particular case. Accordingly, it is argued that such a body of legal principles lacks the basic specificity necessary for criminal statutes under our system of government. Congress did not define what it desired to punish but referred the citizen to a comprehensive law library in order to ascertain what acts were prohibited. To enforce such a statute would be like sanctioning the practice of Caligula who "published the law, but it was written in a very small hand, and posted up in a corner, so that no one could make a copy of it." Suetonius, Lives of the Twelve Caesars, p. 278.</p>
<p>The serious character of that challenge to the constitutionality of the Act is emphasized if the customary standard of guilt for statutory crimes is taken. As we shall see, specific intent is at times required. Holmes, The Common Law, pp. 66 <i>et seq.</i> But the general rule was stated in <i>Ellis</i> v. <i>United States,</i> <span class="citation" data-id="9418092"><a href="/opinion/96682/ellis-v-united-states/#257" aria-description="Citation for case: Ellis v. United States">206 U.S. 246, 257</a></span>, as follows: "If a man intentionally adopts certain conduct in certain circumstances known to him, and that conduct is forbidden by the law under those circumstances, he intentionally breaks the law in the only sense in which the law ever considers intent." And see <i>Horning</i> v. <i>District of</i> <span class="star-pagination">*97</span> <i>Columbia,</i> <span class="citation" data-id="9418436"><a href="/opinion/99651/horning-v-district-of-columbia/#137" aria-description="Citation for case: Horning v. District of Columbia">254 U.S. 135, 137</a></span>; <i>Nash</i> v. <i>United States,</i> <span class="citation" data-id="97928"><a href="/opinion/97928/nash-v-united-states/#377" aria-description="Citation for case: Nash v. United States">229 U.S. 373, 377</a></span>. Under that test a local law enforcement officer violates § 20 and commits a federal offense for which he can be sent to the penitentiary if he does an act which some court later holds deprives a person of due process of law. And he is a criminal though his motive was pure and though his purpose was unrelated to the disregard of any constitutional guarantee. The treacherous ground on which state officials  police, prosecutors, legislators, and judges  would walk is indicated by the character and closeness of decisions of this Court interpreting the due process clause of the Fourteenth Amendment. A confession obtained by too long questioning (<i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U.S. 143</a></span>); the enforcement of an ordinance requiring a license for the distribution of religious literature (<i>Murdock</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9419338"><a href="/opinion/103831/murdock-v-pennsylvania/" aria-description="Citation for case: Murdock v. Pennsylvania">319 U.S. 105</a></span>); the denial of the assistance of counsel in certain types of cases (Cf. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U.S. 45</a></span> with <i>Betts</i> v. <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Brady, supra</a></span></i>); the enforcement of certain types of anti-picketing statutes (<i>Thornhill</i> v. <i>Alabama,</i> <span class="citation" data-id="103347"><a href="/opinion/103347/thornhill-v-alabama/" aria-description="Citation for case: Thornhill v. Alabama">310 U.S. 88</a></span>); the enforcement of state price control laws (<i>Olsen</i> v. <i>Nebraska,</i> <span class="citation" data-id="103522"><a href="/opinion/103522/olsen-v-nebraska-ex-rel-western-reference-bond-assn-inc/" aria-description="Citation for case: Olsen v. Nebraska Ex Rel. Western Reference &amp; Bond Assn.,...">313 U.S. 236</a></span>); the requirement that public school children salute the flag (<i>Board of Education</i> v. <i>Barnette,</i> <span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U.S. 624</a></span>)  these are illustrative of the kind of state action<sup>[2]</sup> which might or might not be caught in the broad reaches of § 20 dependent on the prevailing view of the Court as constituted when the case arose. Those who enforced local law today might not know for many months (and meanwhile could not find out) whether what they did deprived some one of due process of law. The enforcement of a criminal statute so construed would indeed cast <span class="star-pagination">*98</span> law enforcement agencies loose at their own risk on a vast uncharted sea.</p>
<p>If such a construction is not necessary, it should be avoided. This Court has consistently favored that interpretation of legislation which supports its constitutionality. <i>Ashwander</i> v. <i>Tennessee Valley Authority,</i> <span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#348" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U.S. 288, 348</a></span>; <i>Labor Board</i> v. <i>Jones &amp; Laughlin Steel Corp.,</i> <span class="citation" data-id="102804"><a href="/opinion/102804/national-labor-relations-board-v-jones-laughlin-steel-corp/#30" aria-description="Citation for case: National Labor Relations Board v. Jones &amp; Laughlin Steel...">301 U.S. 1, 30</a></span>; <i>Anniston Mfg. Co.</i> v. <i>Davis,</i> <span class="citation" data-id="9418917"><a href="/opinion/102826/anniston-manufacturing-co-v-davis/#351" aria-description="Citation for case: Anniston Manufacturing Co. v. Davis">301 U.S. 337, 351-352</a></span>. That reason is impelling here so that if at all possible § 20 may be allowed to serve its great purpose  the protection of the individual in his civil liberties.</p>
<p>Sec. 20 was enacted to enforce the Fourteenth Amendment.<sup>[3]</sup> It derives<sup>[4]</sup> from § 2 of the Civil Rights Act of April 9, 1866. <span class="citation no-link">14 Stat. 27</span>.<sup>[5]</sup> Senator Trumbull, chairman of the Senate Judiciary Committee which reported the bill, stated that its purpose was "to protect all persons in the United States in their civil rights, and furnish the means of their vindication." Cong. Globe, 39th Cong., 1st Sess., p. 211. In origin it was an antidiscrimination measure (as its language indicated), framed to protect Negroes in their newly won rights. See Flack, The Adoption of the Fourteenth Amendment (1908), p. 21. It was <span class="star-pagination">*99</span> amended by § 17 of the Act of May 31, 1870, <span class="citation no-link">16 Stat. 144</span>,<sup>[6]</sup> and made applicable to "any inhabitant of any State or Territory."<sup>[7]</sup> The prohibition against the "deprivation of any rights, privileges, or immunities, secured or protected by the Constitution and laws of the United States" was introduced by the revisers in 1874. R.S. § 5510. Those words were taken over from § 1 of the Act of April 20, 1871, <span class="citation no-link">17 Stat. 13</span> (the so-called Ku-Klux Act) which provided civil suits for redress of such wrongs.<sup>[8]</sup> See Cong. Rec., <span class="star-pagination">*100</span> 43d Cong., 1st Sess., p. 828. The 1874 revision was applicable to any person who under color of law, etc., "subjects, or causes to be subjected" any inhabitant to the deprivation of any rights, etc. The requirement for a "willful" violation was introduced by the draftsmen of the Criminal Code of 1909. Act of March 4, 1909, <span class="citation no-link">35 Stat. 1092</span>. And we are told "willfully" was added to § 20 in order to make the section "less severe." 43 Cong. Rec., 60th Cong., 2d Sess., p. 3599.</p>
<p>We hesitate to say that when Congress sought to enforce the Fourteenth Amendment<sup>[9]</sup> in this fashion it did a vain thing. We hesitate to conclude that for 80 years this effort of Congress, renewed several times, to protect the important rights of the individual guaranteed by the Fourteenth Amendment has been an idle gesture. Yet if the Act falls by reason of vagueness so far as due process of law is concerned, there would seem to be a similar lack of specificity when the privileges and immunities clause (<i>Madden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9419076"><a href="/opinion/103290/madden-v-kentucky-ex-rel-commissioner/" aria-description="Citation for case: Madden v. Kentucky Ex Rel. Commissioner">309 U.S. 83</a></span>) and the equal protection clause (<i>Smith</i> v. <i>Texas,</i> <span class="citation" data-id="103391"><a href="/opinion/103391/smith-v-texas/" aria-description="Citation for case: Smith v. Texas">311 U.S. 128</a></span>; <i>Hill</i> v. <i>Texas,</i> <span class="citation" data-id="103690"><a href="/opinion/103690/hill-v-texas/" aria-description="Citation for case: Hill v. Texas">316 U.S. 400</a></span>) of the Fourteenth Amendment are involved. Only if no construction can save the Act from this claim of unconstitutionality are we willing to reach that result. We do not reach it, for we are of the view that if § 20 is confined more narrowly than the lower courts confined it, it can be preserved as one of the sanctions to the great rights which the Fourteenth Amendment was designed to secure.</p>
<p></p>
<h2>
<span class="star-pagination">*101</span> II</h2>
<p>We recently pointed out that "willful" is a word "of many meanings, its construction often being influenced by its context." <i>Spies</i> v. <i>United States,</i> <span class="citation" data-id="103753"><a href="/opinion/103753/spies-v-united-states/#497" aria-description="Citation for case: Spies v. United States">317 U.S. 492, 497</a></span>. At times, as the Court held in <i>United States</i> v. <i>Murdock,</i> <span class="citation" data-id="102166"><a href="/opinion/102166/united-states-v-murdock/#394" aria-description="Citation for case: United States v. Murdock">290 U.S. 389, 394</a></span>, the word denotes an act which is intentional rather than accidental. And see <i>United States</i> v. <i>Illinois Central R. Co.,</i> <span class="citation" data-id="102970"><a href="/opinion/102970/united-states-v-illinois-central-railroad/" aria-description="Citation for case: United States v. Illinois Central Railroad">303 U.S. 239</a></span>. But "when used in a criminal statute it generally means an act done with a bad purpose." <i>Id.,</i> p. 394. And see <i>Felton</i> v. <i>United States,</i> <span class="citation" data-id="1087739"><a href="/opinion/1087739/felton-v-united-states/" aria-description="Citation for case: Felton v. United States">96 U.S. 699</a></span>; <i>Potter</i> v. <i>United States,</i> <span class="citation" data-id="94052"><a href="/opinion/94052/potter-v-united-states/" aria-description="Citation for case: Potter v. United States">155 U.S. 438</a></span>; <i>Spurr</i> v. <i>United States,</i> <span class="citation" data-id="95097"><a href="/opinion/95097/spurr-v-united-states/" aria-description="Citation for case: Spurr v. United States">174 U.S. 728</a></span>; <i>Hargrove</i> v. <i>United States,</i> <span class="citation" data-id="1564666"><a href="/opinion/1564666/hargrove-v-united-states/" aria-description="Citation for case: Hargrove v. United States">67 F.2d 820</a></span>. In that event something more is required than the doing of the act proscribed by the statute. Cf. <i>United States</i> v. <i>Balint,</i> <span class="citation" data-id="99947"><a href="/opinion/99947/united-states-v-balint/" aria-description="Citation for case: United States v. Balint">258 U.S. 250</a></span>. An evil motive to accomplish that which the statute condemns becomes a constituent element of the crime. <i>Spurr</i> v. <i>United States, supra,</i> p. 734; <i>United States</i> v. <i>Murdock, supra,</i> p. 395. And that issue must be submitted to the jury under appropriate instructions. <i>United States</i> v. <i>Ragen,</i> <span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/#524" aria-description="Citation for case: United States v. Ragen">314 U.S. 513, 524</a></span>.</p>
<p>An analysis of the cases in which "willfully" has been held to connote more than an act which is voluntary or intentional would not prove helpful as each turns on its own peculiar facts. Those cases, however, make clear that if we construe "willfully" in § 20 as connoting a purpose to deprive a person of a specific constitutional right, we would introduce no innovation. The Court, indeed, has recognized that the requirement of a specific intent to do a prohibited act may avoid those consequences to the accused which may otherwise render a vague or indefinite statute invalid. The constitutional vice in such a statute is the essential injustice to the accused of placing him on trial for an offense, the nature of which the statute does not define and hence of which it gives no warning. <span class="star-pagination">*102</span> See <i>United States</i> v. <i>Cohen Grocery Co., supra</i><i>.</i> But where the punishment imposed is only for an act knowingly done with the purpose of doing that which the statute prohibits, the accused cannot be said to suffer from lack of warning or knowledge that the act which he does is a violation of law. The requirement that the act must be willful or purposeful may not render certain, for all purposes, a statutory definition of the crime which is in some respects uncertain. But it does relieve the statute of the objection that it punishes without warning an offense of which the accused was unaware. That was pointed out by Mr. Justice Brandeis speaking for the Court in <i>Omaechevarria</i> v. <i>Idaho,</i> <span class="citation" data-id="99130"><a href="/opinion/99130/omaechevarria-v-idaho/" aria-description="Citation for case: Omaechevarria v. Idaho">246 U.S. 343</a></span>. An Idaho statute made it a misdemeanor to graze sheep "upon any range usually occupied by any cattle grower." The argument was that the statute was void for indefiniteness because it failed to provide for the ascertainment of boundaries of a "range" or for determining what length of time was necessary to make a prior occupation a "usual" one. The Court ruled that "any danger to sheepmen which might otherwise arise from indefiniteness, is removed by § 6314 of Revised Codes, which provides that: `In every crime or public offense there must exist a union, or joint operation, of act and intent, or criminal negligence.'" <i>Id.,</i> p. 348. A similar ruling was made in <i>Hygrade Provision Co.</i> v. <i>Sherman,</i> <span class="citation" data-id="1620902"><a href="/opinion/1620902/hygrade-provision-co-v-sherman/" aria-description="Citation for case: Hygrade Provision Co. v. Sherman">266 U.S. 497</a></span>. The charge was that a criminal statute which regulated the sale of "kosher" meat or products "sanctioned by the orthodox Hebrew religious requirements" was unconstitutional for want of any ascertainable standard of guilt. The Court speaking through Mr. Justice Sutherland stated, ". . . since the statutes require a specific intent to defraud in order to encounter their prohibitions, the hazard of prosecution which appellants fear loses whatever substantial foundation it might have in the absence of such a requirement." 266 U.S. pp. 502-503. In <i>United States</i> v. <i><span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/" aria-description="Citation for case: United States v. Ragen">Ragen, supra</a></span></i><i>,</i> we took <span class="star-pagination">*103</span> that course in a prosecution for willful evasion of a federal income tax where it was alleged that the defendant had deducted more than "reasonable" allowances for salaries. By construing the statute to require proof of bad faith we avoided the serious question which the rule of <i>United States</i> v. <i>Cohen Grocery Co., supra</i><i>,</i> might have presented. We think a like course is appropriate here.</p>
<p>Moreover, the history of § 20 affords some support for that narrower construction. As we have seen, the word "willfully" was not added to the Act until 1909. Prior to that time it may be that Congress intended that he who deprived a person of any right protected by the Constitution should be liable without more. That was the pattern of criminal legislation which has been sustained without any charge or proof of <i>scienter. </i><i>Shevlin-Carpenter Co.</i> v. <i>Minnesota,</i> <span class="citation" data-id="97275"><a href="/opinion/97275/shevlin-carpenter-co-v-minnesota/" aria-description="Citation for case: Shevlin-Carpenter Co. v. Minnesota">218 U.S. 57</a></span>; <i>United States</i> v. <i><span class="citation" data-id="99947"><a href="/opinion/99947/united-states-v-balint/" aria-description="Citation for case: United States v. Balint">Balint, supra</a></span></i><i>.</i> And the present Act in its original form would have been susceptible of the same interpretation apart from the equal protection clause of the Fourteenth Amendment, where "purposeful discriminatory" action must be shown. <i>Snowden</i> v. <i>Hughes,</i> <span class="citation" data-id="9419429"><a href="/opinion/103921/snowden-v-hughes/#8" aria-description="Citation for case: Snowden v. Hughes">321 U.S. 1, 8-9</a></span>. But as we have seen, the word "willfully" was added to make the section "less severe." We think the inference is permissible that its severity was to be lessened by making it applicable only where the requisite bad purpose was present, thus requiring specific intent not only where discrimination is claimed but in other situations as well. We repeat that the presence of a bad purpose or evil intent alone may not be sufficient. We do say that a requirement of a specific intent to deprive a person of a federal right made definite by decision or other rule of law saves the Act from any charge of unconstitutionality on the grounds of vagueness.</p>
<p>Once the section is given that construction, we think that the claim that the section lacks an ascertainable standard of guilt must fail. The constitutional requirement that a criminal statute be definite serves a high function. <span class="star-pagination">*104</span> It gives a person acting with reference to the statute fair warning that his conduct is within its prohibition. This requirement is met when a statute prohibits only "willful" acts in the sense we have explained. One who does act with such specific intent is aware that what he does is precisely that which the statute forbids. He is under no necessity of guessing whether the statute applies to him (see <i>Connally</i> v. <i>General Construction Co.,</i> <span class="citation" data-id="100759"><a href="/opinion/100759/connally-v-general-construction-co/" aria-description="Citation for case: Connally v. General Construction Co.">269 U.S. 385</a></span>) for he either knows or acts in reckless disregard of its prohibition of the deprivation of a defined constitutional or other federal right. See <i>Gorin</i> v. <i>United States,</i> <span class="citation" data-id="103434"><a href="/opinion/103434/gorin-v-united-states/#27" aria-description="Citation for case: Gorin v. United States">312 U.S. 19, 27-28</a></span>. Nor is such an act beyond the understanding and comprehension of juries summoned to pass on them. The Act would then not become a trap for law enforcement agencies acting in good faith. "A mind intent upon willful evasion is inconsistent with surprised innocence." <i>United States</i> v. <span class="citation" data-id="103582"><a href="/opinion/103582/united-states-v-ragen/#524" aria-description="Citation for case: United States v. Ragen"><i>Ragen, supra,</i> p. 524</a></span>.</p>
<p>It is said, however, that this construction of the Act will not save it from the infirmity of vagueness since neither a law enforcement official nor a trial judge can know with sufficient definiteness the range of rights that are constitutional. But that criticism is wide of the mark. For the specific intent required by the Act is an intent to deprive a person of a right which has been made specific either by the express terms of the Constitution or laws of the United States or by decisions interpreting them. Take the case of a local officer who persists in enforcing a type of ordinance which the Court has held invalid as violative of the guarantees of free speech or freedom of worship. Or a local official continues to select juries in a manner which flies in the teeth of decisions of the Court. If those acts are done willfully, how can the officer possibly claim that he had no fair warning that his acts were prohibited by the statute? He violates the statute not merely because he has a bad purpose but because he acts in defiance of announced rules of law. He who defies a <span class="star-pagination">*105</span> decision interpreting the Constitution knows precisely what he is doing. If sane, he hardly may be heard to say that he knew not what he did. Of course, willful conduct cannot make definite that which is undefined. But willful violators of constitutional requirements, which have been defined, certainly are in no position to say that they had no adequate advance notice that they would be visited with punishment. When they act willfully in the sense in which we use the word, they act in open defiance or in reckless disregard of a constitutional requirement which has been made specific and definite. When they are convicted for so acting, they are not punished for violating an unknowable something.</p>
<p>The Act so construed has a narrower range in all its applications than if it were interpreted in the manner urged by the government. But the only other alternative, if we are to avoid grave constitutional questions, is to construe it as applicable only to those acts which are clearly marked by the specific provisions of the Constitution as deprivations of constitutional rights, privileges, or immunities, and which are knowingly done within the rule of <i>Ellis</i> v. <i>United States, supra</i><i>.</i> But as we have said, that course would mean that all protection for violations of due process of law would drop out of the Act. We take the course which makes it possible to preserve the entire Act and save all parts of it from constitutional challenge. If Congress desires to give the Act wider scope, it may find ways of doing so. Moreover, here as in <i>Apex Hosiery Co.</i> v. <i>Leader,</i> <span class="citation" data-id="9419107"><a href="/opinion/103367/apex-hosiery-co-v-leader/" aria-description="Citation for case: Apex Hosiery Co. v. Leader">310 U.S. 469</a></span>, we are dealing with a situation where the interpretation of the Act which we adopt does not preclude any state from punishing any act made criminal by its own laws. Indeed, the narrow construction which we have adopted more nearly preserves the traditional balance between the States and the national government in law enforcement than that which is urged upon us.</p>
<p><span class="star-pagination">*106</span> <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> met the test we suggest. In that case we were dealing merely with the validity of an indictment, not with instructions to the jury. The indictment was sufficient since it charged a willful failure and refusal of the defendant election officials to count the votes cast, by their alteration of the ballots and by their false certification of the number of votes cast for the respective candidates. 313 U.S. pp. 308-309. The right so to vote is guaranteed by Art. I, § 2 and § 4 of the Constitution. Such a charge is adequate since he who alters ballots or without legal justification destroys them would be acting willfully in the sense in which § 20 uses the term. The fact that the defendants may not have been thinking in constitutional terms is not material where their aim was not to enforce local law but to deprive a citizen of a right and that right was protected by the Constitution. When they so act they at least act in reckless disregard of constitutional prohibitions or guarantees. Likewise, it is plain that basic to the concept of due process of law in a criminal case is a trial  a trial in a court of law, not a "trial by ordeal." <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278, 285</a></span>. It could hardly be doubted that they who "under color of any law, statute, ordinance, regulation, or custom" act with that evil motive violate § 20. Those who decide to take the law into their own hands and act as prosecutor, jury, judge, and executioner plainly act to deprive a prisoner of the trial which due process of law guarantees him. And such a purpose need not be expressed; it may at times be reasonably inferred from all the circumstances attendant on the act. See <i>Tot</i> v. <i>United States,</i> <span class="citation" data-id="103855"><a href="/opinion/103855/tot-v-united-states/" aria-description="Citation for case: Tot v. United States">319 U.S. 463</a></span>.</p>
<p>The difficulty here is that this question of intent was not submitted to the jury with the proper instructions. The court charged that petitioners acted illegally if they applied more force than was necessary to make the arrest effectual or to protect themselves from the prisoner's alleged <span class="star-pagination">*107</span> assault. But in view of our construction of the word "willfully" the jury should have been further instructed that it was not sufficient that petitioners had a generally bad purpose. To convict it was necessary for them to find that petitioners had the purpose to deprive the prisoner of a constitutional right, e. g. the right to be tried by a court rather than by ordeal. And in determining whether that requisite bad purpose was present the jury would be entitled to consider all the attendant circumstances  the malice of petitioners, the weapons used in the assault, its character and duration, the provocation, if any, and the like.</p>
<p>It is true that no exception was taken to the trial court's charge. Normally we would under those circumstances not take note of the error. See <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="9419306"><a href="/opinion/103779/johnson-v-united-states/#200" aria-description="Citation for case: Johnson v. United States">318 U.S. 189, 200</a></span>. But there are exceptions to that rule. <i>United States</i> v. <i>Atkinson,</i> <span class="citation" data-id="102591"><a href="/opinion/102591/united-states-v-atkinson/#160" aria-description="Citation for case: United States v. Atkinson">297 U.S. 157, 160</a></span>; <i>Clyatt</i> v. <i>United States,</i> <span class="citation" data-id="9417982"><a href="/opinion/96244/clyatt-v-united-states/#221" aria-description="Citation for case: Clyatt v. United States">197 U.S. 207, 221-222</a></span>. And where the error is so fundamental as not to submit to the jury the essential ingredients of the only offense on which the conviction could rest, we think it is necessary to take note of it on our own motion. Even those guilty of the most heinous offenses are entitled to a fair trial. Whatever the degree of guilt, those charged with a federal crime are entitled to be tried by the standards of guilt which Congress has prescribed.</p>
<p></p>
<h2>III</h2>
<p>It is said, however, that petitioners did not act "under color of any law" within the meaning of § 20 of the Criminal Code. We disagree. We are of the view that petitioners acted under "color" of law in making the arrest of Robert Hall and in assaulting him. They were officers of the law who made the arrest. By their own admissions they assaulted Hall in order to protect themselves and to keep their prisoner from escaping. It was their duty <span class="star-pagination">*108</span> under Georgia law to make the arrest effective. Hence, their conduct comes within the statute.</p>
<p>Some of the arguments which have been advanced in support of the contrary conclusion suggest that the question under § 20 is whether Congress has made it a federal offense for a state officer to violate the law of his State. But there is no warrant for treating the question in state law terms. The problem is not whether state law has been violated but whether an inhabitant of a State has been deprived of a federal right by one who acts under "color of any law." He who acts under "color" of law may be a federal officer or a state officer. He may act under "color" of federal law or of state law. The statute does not come into play merely because the federal law or the state law under which the officer purports to act is violated. It is applicable when and only when someone is deprived of a federal right by that action. The fact that it is also a violation of state law does not make it any the less a federal offense punishable as such. Nor does its punishment by federal authority encroach on state authority or relieve the state from its responsibility for punishing state offenses.<sup>[10]</sup></p>
<p>We agree that when this statute is applied to the action of state officials, it should be construed so as to respect the proper balance between the States and the federal government in law enforcement. Violation of local law does not necessarily mean that federal rights have been invaded. The fact that a prisoner is assaulted, injured, or even murdered by state officials does not necessarily mean that he is deprived of any right protected or secured by the <span class="star-pagination">*109</span> Constitution or laws of the United States. Cf. <i>Logan</i> v. <i>United States,</i> <span class="citation" data-id="93322"><a href="/opinion/93322/logan-v-united-states/" aria-description="Citation for case: Logan v. United States">144 U.S. 263</a></span>, dealing with assaults by federal officials. The Fourteenth Amendment did not alter the basic relations between the States and the national government. <i>United States</i> v. <i>Harris,</i> <span class="citation" data-id="90728"><a href="/opinion/90728/united-states-v-harris/" aria-description="Citation for case: United States v. Harris">106 U.S. 629</a></span>; <i>In re Kemmler,</i> <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#448" aria-description="Citation for case: In Re Kemmler">136 U.S. 436, 448</a></span>. Our national government is one of delegated powers alone. Under our federal system the administration of criminal justice rests with the States except as Congress, acting within the scope of those delegated powers, has created offenses against the United States. <i>Jerome</i> v. <i>United States,</i> <span class="citation" data-id="103771"><a href="/opinion/103771/jerome-v-united-states/#105" aria-description="Citation for case: Jerome v. United States">318 U.S. 101, 105</a></span>. As stated in <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#553" aria-description="Citation for case: United States v. Cruikshank">92 U.S. 542, 553-554</a></span>, "It is no more the duty or within the power of the United States to punish for a conspiracy to falsely imprison or murder within a State, than it would be to punish for false imprisonment or murder itself." And see <i>United States</i> v. <i>Fox,</i> <span class="citation" data-id="89649"><a href="/opinion/89649/united-states-v-fox/#672" aria-description="Citation for case: United States v. Fox">95 U.S. 670, 672</a></span>. It is only state action of a "particular character" that is prohibited by the Fourteenth Amendment and against which the Amendment authorizes Congress to afford relief. <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/#11" aria-description="Citation for case: Civil Rights Cases">109 U.S. 3, 11, 13</a></span>. Thus Congress in § 20 of the Criminal Code did not undertake to make all torts of state officials federal crimes. It brought within § 20 only specified acts done "under color" of law and then only those acts which deprived a person of some right secured by the Constitution or laws of the United States.</p>
<p>This section was before us in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic">313 U.S. 299, 326</a></span>, where we said: "Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken `under color of' state law." In that case state election officials were charged with failure to count the votes as cast, alteration of the ballots, and false certification of the number of votes cast for the respective candidates. 313 U.S. pp. 308-309. We stated that those acts of the defendants "were committed in the course of <span class="star-pagination">*110</span> their performance of duties under the Louisiana statute requiring them to count the ballots, to record the result of the count, and to certify the result of the election." <i>Id.,</i> pp. 325-326. In the present case, as we have said, the defendants were officers of the law who had made an arrest and who by their own admissions made the assault in order to protect themselves and to keep the prisoner from escaping, i.e., to make the arrest effective. That was a duty they had under Georgia law. <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> is, therefore, indistinguishable from this case so far as "under color of" state law is concerned. In each officers of the State were performing official duties; in each the power which they were authorized to exercise was misused. We cannot draw a distinction between them unless we are to say that § 20 is not applicable to police officers. But the broad sweep of its language leaves no room for such an exception.</p>
<p>It is said that we should abandon the holding of the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case. It is suggested that the present problem was not clearly in focus in that case and that its holding was ill-advised. A reading of the opinion makes plain that the question was squarely involved and squarely met. It followed the rule announced in <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339, 346</a></span>, that a state judge who in violation of state law discriminated against negroes in the selection of juries violated the Act of March 1, 1875, <span class="citation no-link">18 Stat. 336</span>. It is true that that statute did not contain the words under "color" of law. But the Court in deciding what was state action within the meaning of the Fourteenth Amendment held that it was immaterial that the state officer exceeded the limits of his authority. ". . . as he acts in the name and for the State, and is clothed with the State's power, his act is that of the State. This must be so, or the constitutional prohibition has no meaning. Then the State has clothed one of its agents with power to annul or to evade it." <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#347" aria-description="Citation for case: Ex Parte Virginia">100 U.S. at p. 347</a></span>. And see <i>Virginia</i> v. <i>Rives,</i> <span class="star-pagination">*111</span> <span class="citation" data-id="90040"><a href="/opinion/90040/virginia-v-rives/#321" aria-description="Citation for case: Virginia v. Rives">100 U.S. 313, 321</a></span>. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case recognized, without dissent, that the contrary view would defeat the great purpose which § 20 was designed to serve. Reference is made to statements<sup>[11]</sup> of Senator Trumbull in his discussion of § 2 of the Civil Rights Act of 1866, <span class="citation no-link">14 Stat. 27</span>, and to statements of Senator Sherman concerning the 1870 Act<sup>[12]</sup> as supporting the conclusion that "under color of any law" was designed to include only action taken by officials pursuant to state law. But those statements in their context are inconclusive on the precise problem involved in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case and in the present case. We are not dealing here with a case where an officer not authorized to act nevertheless takes action. Here the state officers were authorized to make an arrest and to take such steps as were necessary to make the arrest effective. They acted without authority only in the sense that they used excessive force in making the arrest effective. It is clear that under "color" of law means under "pretense" of law. Thus acts of officers in the ambit of their personal pursuits are plainly excluded. Acts of officers who undertake to perform their official duties are included whether they hew to the line of their authority or overstep it. If, as suggested, the statute was designed to embrace only action which the State in fact authorized, the words "under color of any law" were hardly apt words to express the idea.</p>
<p>Nor are the decisions under § 33 of the Judicial Code, <span class="citation no-link">28 U.S.C. § 76</span>, in point. That section gives the right of removal to a federal court of any criminal prosecution begun in a state court against a revenue officer of the United States "on account of any act done under color of his office or of any such (revenue) law." The cases under it recognize that it is an "exceptional" procedure which wrests from state courts the power to try offenses against <span class="star-pagination">*112</span> their own laws. <i>Maryland</i> v. <i>Soper</i> (<i>No. 1</i>), <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/#29" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9, 29, 35</a></span>; <i>Colorado</i> v. <i>Symes,</i> <span class="citation" data-id="101949"><a href="/opinion/101949/colorado-v-symes/#518" aria-description="Citation for case: Colorado v. Symes">286 U.S. 510, 518</a></span>. Thus the requirements of the showing necessary for removal are strict. See <i>Maryland</i> v. <i>Soper</i> (<i>No. 2</i>), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/#42" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36, 42</a></span>, saying that acts "necessary to make the enforcement effective" are done under "color" of law. Hence those cases do not supply an authoritative guide to the problems under § 20 which seeks to afford protection against officers who possess authority to act and who exercise their powers in such a way as to deprive a person of rights secured to him by the Constitution or laws of the United States. It is one thing to deprive state courts of their authority to enforce their own laws. It is quite another to emasculate an Act of Congress designed to secure individuals their constitutional rights by finely spun distinctions concerning the precise scope of the authority of officers of the law. Cf. <i>Yick Wo</i> v. <i>Hopkins,</i> <span class="citation" data-id="91704"><a href="/opinion/91704/yick-wo-v-hopkins/" aria-description="Citation for case: Yick Wo v. Hopkins">118 U.S. 356</a></span>.</p>
<p>But beyond that is the problem of <i>stare decisis.</i> The construction given § 20 in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case formulated a rule of law which has become the basis of federal enforcement in this important field. The rule adopted in that case was formulated after mature consideration. It should be good for more than one day only. We do not have here a situation comparable to <i>Mahnich</i> v. <i>Southern S.S. Co.,</i> <span class="citation" data-id="103927"><a href="/opinion/103927/mahnich-v-southern-steamship-co/" aria-description="Citation for case: Mahnich v. Southern Steamship Co.">321 U.S. 96</a></span>, where we overruled a decision demonstrated to be a sport in the law and inconsistent with what preceded and what followed. The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not the product of hasty action or inadvertence. It was not out of line with the cases which preceded. It was designed to fashion the governing rule of law in this important field. We are not dealing with constitutional interpretations which throughout the history of the Court have wisely remained flexible and subject to frequent re-examination. The meaning which the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case gave to the phrase "under color of any law" involved only a construction of the statute. Hence if it states a rule undesirable <span class="star-pagination">*113</span> in its consequences, Congress can change it. We add only to the instability and uncertainty of the law if we revise the meaning of § 20 to meet the exigencies of each case coming before us.</p>
<p>Since there must be a new trial, the judgment below is</p>
<p><i>Reversed.</i></p>
<p id="rutconcur">MR. JUSTICE RUTLEDGE, concurring in the result.</p>
<p>For the compelling reason stated at the end of this opinion I concur in reversing the judgment and remanding the cause for further proceedings. But for that reason, my views would require that my vote be cast to affirm the judgment, for the reasons stated by MR. JUSTICE MURPHY and others I feel forced, in the peculiar situation, to state.</p>
<p>The case comes here established in fact as a gross abuse of authority by state officers. Entrusted with the state's power and using it, without a warrant or with one of only doubtful legality<sup>[1]</sup> they invaded a citizen's home, arrested him for alleged theft of a tire, forcibly took him in handcuffs to the courthouse yard, and there beat him to death. Previously they had threatened to kill him, fortified themselves at a near-by bar, and resisted the bartender's importunities not to carry out the arrest. Upon this and other evidence which overwhelmingly supports (<span class="citation" data-id="9653538"><a href="/opinion/1567036/screws-v-united-states/#665" aria-description="Citation for case: Screws v. United States">140 F.2d at 665</a></span>) the verdict, together with instructions adequately <span class="star-pagination">*114</span> covering an officer's right to use force, the jury found the petitioners guilty.</p>
<p></p>
<h2>I</h2>
<p>The verdict has shaped their position here. Their contention hardly disputes the facts on which it rests.<sup>[2]</sup> They do not come therefore as faithful state officers, innocent of crime. Justification has been foreclosed. Accordingly, their argument now admits the offense, but insists it was against the state alone, not the nation. So they have made their case in this Court.<sup>[3]</sup></p>
<p>In effect, the position urges it is murder they have done,<sup>[4]</sup> not deprivation of constitutional right. Strange as the argument is the reason. It comes to this, that abuse of state power creates immunity to federal power. Because what they did violated the state's laws, the nation cannot reach their conduct.<sup>[5]</sup> It may deprive the citizen of his liberty and his life. But whatever state officers may do in abuse of their official capacity can give this Government and its courts no concern. This, though the prime object of the Fourteenth Amendment and § 20 was to secure these fundamental rights against wrongful denial by exercise of the power of the states.</p>
<p>The defense is not pretty. Nor is it valid. By a long course of decision from <i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/" aria-description="Citation for case: Ex Parte Virginia">100 U.S. 339</a></span>, to <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>, it has been rejected.<sup>[6]</sup><span class="star-pagination">*115</span> The ground should not need ploughing again. It was cleared long ago and thoroughly. It has been kept clear, until the ancient doubt, laid in the beginning, was resurrected in the last stage of this case. The evidence has nullified any pretense that petitioners acted as individuals, about their personal though nefarious business. They used the power of official place in all that was done. The verdict has foreclosed semblance of any claim that only private matters, not touching official functions, were involved. Yet neither was the state's power, they say.</p>
<p>There is no third category. The Amendment and the legislation were not aimed at rightful state action. Abuse of state power was the target. Limits were put to state authority, and states were forbidden to pass them, by whatever agency.<sup>[7]</sup> It is too late now, if there were better reason than exists for doing so, to question that in these matters abuse binds the state and is its act, when done by <span class="star-pagination">*116</span> one to whom it has given power to make the abuse effective to achieve the forbidden ends. Vague ideas of dual federalism,<sup>[8]</sup> of ultra vires doctrine imported from private agency,<sup>[9]</sup> and of want of finality in official action,<sup>[10]</sup> do not nullify what four years of civil strife secured and eighty years have verified. For it was abuse of basic civil and political rights, by states and their officials, that the Amendment and the enforcing legislation were adopted to uproot.</p>
<p>The danger was not merely legislative or judicial. Nor was it threatened only from the state's highest officials. It was abuse by whatever agency the state might invest with its power capable of inflicting the deprivation. In all its flux, time makes some things axiomatic. One has been that state officials who violate their oaths of office and flout <span class="star-pagination">*117</span> the fundamental law are answerable to it when their misconduct brings upon them the penalty it authorizes and Congress has provided.</p>
<p>There could be no clearer violation of the Amendment or the statute. No act could be more final or complete, to denude the victim of rights secured by the Amendment's very terms. Those rights so destroyed cannot be restored. Nor could the part played by the state's power in causing their destruction be lessened, though other organs were now to repudiate what was done. The state's law might thus be vindicated. If so, the vindication could only sustain, it could not detract from the federal power. Nor could it restore what the federal power shielded. Neither acquittal nor conviction, though affirmed by the state's highest court, could resurrect what the wrongful use of state power has annihilated. There was in this case abuse of state power, which for the Amendment's great purposes was state action, final in the last degree, depriving the victim of his liberty and his life without due process of law.</p>
<p>If the issues made by the parties themselves were allowed to govern, there would be no need to say more. At various stages petitioners have sought to show that they used no more force than was necessary, that there was no state action, and that the evidence was not sufficient to sustain the verdict and the judgment. These issues, in various formulations,<sup>[11]</sup> have comprehended their case. All have been resolved against them without error. This should end the matter.</p>
<p></p>
<h2>
<span class="star-pagination">*118</span> II</h2>
<p>But other and most important issues have been injected and made decisive to reverse the judgment. Petitioners have not denied that they acted "willfully" within the meaning of § 20 or that they intended to do the acts which took their victim's liberty and life. In the trial court they claimed justification. But they were unable to prove it. The verdict, on overwhelming evidence, has concluded against them their denial of bad purpose and reckless disregard of rights. This is necessarily implied in the finding that excessive force was used. No complaint was made of the charge in any of these respects and no request for additional charges concerning them was offered. Nor, in the application for certiorari or the briefs, have they raised questions of the requisite criminal intent or of unconstitutional vagueness in the statute's definition of the crime. However, these issues have been brought forward, so far as the record discloses, first by the dissenting opinion in the Court of Appeals, then by inquiry at the argument and in the disposition here.</p>
<p>The story would be too long, to trace in more than outline the history of § 20 and companion provisions, in particular § 19,<sup>[12]</sup> with which it must be considered on any suggestion of fatal ambiguity. But this history cannot be ignored, unless we would risk throwing overboard what the nation's greatest internal conflict created and eight <span class="star-pagination">*119</span> decades have confirmed, in protection of individual rights against impairment by the states.</p>
<p>Sections 19 and 20 are twin sections in all respects that concern any question of vagueness in defining the crimes. There are important differences. Section 19 strikes at conspiracies, § 20 at substantive offenses. The former protects "citizens," the latter "inhabitants." There are, however, no differences in the basic rights guarded. Each protects in a different way the rights and privileges secured to individuals by the Constitution. If one falls for vagueness in pointing to these, the other also must fall for the same reason. If one stands, so must both. It is not one statute therefore which we sustain or nullify. It is two.</p>
<p>The sections have stood for nearly eighty years. Nor has this been without attack for ambiguity. Together the two sections have repelled it. In 1915, one of this Court's greatest judges, speaking for it, summarily disposed of the suggestion that § 19 is invalid: "It is not open to question that this statute is constitutional. . . [It] dealt with Federal rights and with all Federal rights, and protected them in the lump . . ." <i>United States</i> v. <i>Mosley,</i> <span class="citation" data-id="9418291"><a href="/opinion/98518/united-states-v-mosley/#386" aria-description="Citation for case: United States v. Mosley">238 U.S. 383, 386, 387</a></span>. And in <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>, the Court with equal vigor reaffirmed the validity of both sections, against dissenting assault for fatal <span class="star-pagination">*120</span> ambiguity in relation to the constitutional rights then in question. These more recent pronouncements but reaffirmed earlier and repeated ones. The history should not require retelling. But old and established freedoms vanish when history is forgotten.</p>
<p>Section 20 originated in the Civil Rights Act of 1866 (<span class="citation no-link">14 Stat. 27</span>), § 19 in the Enforcement Act of 1870 (<span class="citation no-link">16 Stat. 141</span>, § 6). Their great original purpose was to strike at discrimination, particularly against Negroes, the one securing civil, the other political rights. But they were not drawn so narrowly. From the beginning § 19 protected all "citizens," § 20 "inhabitants."</p>
<p>At first § 20 secured only rights enumerated in the Civil Rights Act. The first ten years brought it, through broadening changes, to substantially its present form. Only the word "willfully" has been added since then, a change of no materiality, for the statute implied it beforehand.<sup>[13]</sup> <span class="citation no-link">35 Stat. 1092</span>. The most important change of the first decade replaced the specific enumeration of the Civil Rights Act with the present broad language covering "the deprivation of any rights, privileges, or immunities, secured or protected by the Constitution and laws of the United States." R.S. § 5510. This inclusive designation brought § 20 into conformity with § 19's original coverage of "any right or privilege secured to him by the Constitution or laws of the United States." Since then, under these generic designations, the two have been literally identical in the scope of the rights they secure. The slight difference in wording cannot be one of substance.<sup>[14]</sup></p>
<p><span class="star-pagination">*121</span> Throughout a long and varied course of application the sections have remained unimpaired on the score of vagueness in the crimes they denounce. From 1874 to today they have repelled all attacks proposed to invalidate them. None has succeeded. If time and uniform decision can give stability to statutes, these have acquired it.</p>
<p>Section 20 has not been much used, in direct application, until recently. There were however a number of early decisions.<sup>[15]</sup> Of late the section has been applied more frequently, in considerable variety of situation, against varied and vigorous attack.<sup>[16]</sup> In <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#321" aria-description="Citation for case: United States v. Classic">313 U.S. at 321</a></span>, as has been stated, this Court gave it clear-cut sanction. The opinion expressly repudiated any idea that the section, or § 19, is vitiated by ambiguity. Moreover, this was done in terms which leave no room to say that the decision was not focused upon that question.<sup>[17]</sup> True, application to Fourteenth Amendment <span class="star-pagination">*122</span> rights was reserved because the question was raised for the first time in the Government's brief filed here. 313 U.S. at 329. But the statute was sustained in application to a vast range of rights secured by the Constitution, apart from the reserved segment, as the opinion's language and the single reservation itself attest. The ruling, thus broad, could not have been inadvertent. For it was repeated concerning both sections, broadly, forcefully, and upon citation of long-established authority. And this was done in response to a vigorous dissent which made the most of the point of vagueness.<sup>[18]</sup> The point was flatly, and deliberately, rejected. The Court could not have been blinded by other issues to the import of this one.</p>
<p>The <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> decision thus cannot be put aside in this case. Nor can it be demonstrated that the rights secured by the Fourteenth Amendment are more numerous or more dubious than the aggregate encompassed by other <span class="star-pagination">*123</span> constitutional provisions. Certainly "the equal protection of the laws," guaranteed by the Amendment, is not more vague and indefinite than many rights protected by other commands.<sup>[19]</sup> The same thing is true of "the privileges or immunities of citizens of the United States." The Fifth Amendment contains a due process clause as broad in its terms restricting national power as the Fourteenth is of state power.<sup>[20]</sup> If § 20 (with § 19) is valid in general coverage of other constitutional rights, it cannot be void in the less sweeping application to Fourteenth Amendment rights. If it is valid to assure the rights "plainly and directly" secured by other provisions, it is equally valid to protect those "plainly and directly" secured by the Fourteenth Amendment, including the expressly guaranteed rights not to be deprived of life, liberty or property without due process of law. If in fact there could be any difference among the various rights protected, in view of the history it would be that the section applies more clearly to Fourteenth Amendment rights than to others. Its phrases "are all phrases of large generalities. But they are not generalities of unillumined vagueness; they are generalities circumscribed by history and appropriate to the largeness of the problems of government with which they were concerned." <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U.S. 401</a></span>, concurring opinion, p. 413.</p>
<p>Historically, the section's function and purpose have been to secure rights given by the Amendment. From the Amendment's adoption until 1874, it was Fourteenth Amendment legislation. Surely when in that year the section was expanded to include other rights these were <span class="star-pagination">*124</span> not dropped out. By giving the citizen additional security in the exercise of his voting and other political rights, which was the section's effect, unless the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case falls, Congress did not take from him the protection it previously afforded (wholly apart from the prohibition of different penalties)<sup>[21]</sup> against deprivation of such rights on account of race, color or previous condition of servitude, or repeal the prior safeguard of civil rights.</p>
<p>To strike from the statute the rights secured by the Fourteenth Amendment, but at the same time to leave within its coverage the vast area bounded by other constitutional provisions, would contradict both reason and history. No logic but one which nullifies the historic foundations of the Amendment and the section could support such an emasculation. There should be no judicial hack work cutting out some of the great rights the Amendment secures but leaving in others. There can be none excising all protected by the Amendment, but leaving <span class="star-pagination">*125</span> every other given by the Constitution intact under the statute's aegis.</p>
<p>All that has been said of § 20 applies with equal force to § 19. It had an earlier more litigious history, firmly establishing its validity.<sup>[22]</sup> It also has received recent application,<sup>[23]</sup><span class="star-pagination">*126</span> without question for ambiguity except in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case, which nevertheless gave it equal sanction with its substantive counterpart.</p>
<p>Separately, and often together in application, §§ 19 and 20 have been woven into our fundamental and statutory law. They have place among our more permanent legal achievements. They have safeguarded many rights and privileges apart from political ones. Among those buttressed, either by direct application or through the general conspiracy statute, § 37 (<span class="citation no-link">18 U.S.C. § 88</span>),<sup>[24]</sup> are the rights to a fair trial, including freedom from sham trials; to be free from arrest and detention by methods constitutionally forbidden and from extortion of property by such methods; from extortion of confessions; from mob action incited or shared by state officers; from failure to furnish police protection on proper occasion and demand; from interference with the free exercise of religion, freedom of the press, freedom of speech and assembly;<sup>[25]</sup> and <span class="star-pagination">*127</span> the necessary import of the decisions is that the right to be free from deprivation of life itself, without due process of law, that is, through abuse of state power by state officials, is as fully protected as other rights so secured.</p>
<p>So much experience cannot be swept aside, or its teaching annulled, without overthrowing a great, and a firmly established, constitutional tradition. Nor has the feared welter of uncertainty arisen. Defendants have attacked the sections, or their application, often and strenuously. Seldom has complaint been made that they are too vague and uncertain. Objections have centered principally about "state action," including "color of law" and failure by inaction to discharge official duty, cf. <i>Catlette</i> v. <i>United States,</i> <span class="citation" data-id="1480783"><a href="/opinion/1480783/catlette-v-united-states/" aria-description="Citation for case: Catlette v. United States">132 F.2d 902</a></span>, and about the strength of federal power to reach particular abuses.<sup>[26]</sup> More rarely they have touched other matters, such as the limiting effect of official privilege<sup>[27]</sup> and, in occasional instances, <i>mens rea.</i><sup>[28]</sup><span class="star-pagination">*128</span> In all this wealth of attack accused officials have little used the shield of ambiguity. The omission, like the Court's rejection in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case, cannot have been inadvertent. There are valid reasons for it, apart from the old teaching that the matter has been foreclosed.</p>
<p>One is that the generality of the section's terms simply has not worked out to be a hazard of unconstitutional, or even serious, proportions. It has not proved a source of practical difficulty. In no other way can be explained the paucity of the objection's appearance in the wealth of others made. If experience is the life of the law, as has been said, this has been true preeminently in the application of §§ 19 and 20.</p>
<p>Moreover, statutory specificity has two purposes, to give due notice that an act has been made criminal before it is done and to inform one accused of the nature of the offense charged, so that he may adequately prepare and make his defense. More than this certainly the Constitution does not require. Cf. Amend. VI. All difficulty on the latter score vanishes, under § 20, with the indictment's particularization of the rights infringed and the acts infringing them. If it is not sufficient in either respect, in these as in other cases the motion to quash or one for a bill of particulars is at the defendant's disposal. The decided cases demonstrate that accused persons have had little or no difficulty to ascertain the rights they have been charged with transgressing or the acts of transgression.<sup>[29]</sup> So it was with the defendants in this case. They were not puzzled to know for what they were indicted, as their proof and their defense upon the law conclusively show. They simply misconceived that the victim had no federal rights and that what they had done was not a crime within the federal power to penalize.<sup>[30]</sup> That kind of error relieves no one from penalty.</p>
<p><span class="star-pagination">*129</span> In the other aspect of specificity, two answers, apart from experience, suffice. One is that § 20, and § 19, are no more general and vague, Fourteenth Amendment rights included, than other criminal statutes commonly enforced against this objection. The Sherman Act is the most obvious illustration.<sup>[31]</sup></p>
<p>Furthermore, the argument of vagueness, to warn men of their conduct, ignores the nature of the criminal act itself and the notice necessarily given from this. Section 20 strikes only at abuse of official functions by state officers. It does not reach out for crimes done by men in general. Not murder per se, but murder by state officers in the course of official conduct and done with the aid of state power, is outlawed. These facts, inherent in the crime, give all the warning constitutionally required. For one, so situated, who goes so far in misconduct can have no excuse of innocence or ignorance.</p>
<p>Generally state officials know something of the individual's basic legal rights. If they do not, they should, for they assume that duty when they assume their office. Ignorance of the law is no excuse for men in general. It is less an excuse for men whose special duty is to apply it, and therefore to know and observe it. If their knowledge is not comprehensive, state officials know or should know when they pass the limits of their authority, so far at any rate that their action exceeds honest error of judgment and amounts to abuse of their office and its function. When they enter such a domain in dealing with the citizen's rights, they should do so at their peril, whether that <span class="star-pagination">*130</span> be created by state or federal law. For their sworn oath and their first duty are to uphold the Constitution, then only the law of the state which too is bound by the charter. Since the statute, as I think, condemns only something more than error of judgment, made in honest effort at once to apply and to follow the law, cf. <i>United States</i> v. <i>Murdock,</i> <span class="citation" data-id="102166"><a href="/opinion/102166/united-states-v-murdock/" aria-description="Citation for case: United States v. Murdock">290 U.S. 389</a></span>, officials who violate it must act in intentional or reckless disregard of individual rights and cannot be ignorant that they do great wrong.<sup>[32]</sup> This being true, they must be taken to act at peril of incurring the penalty placed upon such conduct by the federal law, as they do of that the state imposes.</p>
<p>What has been said supplies all the case requires to be decided on the question of criminal intent. If the criminal act is limited, as I think it must be and the statute intends, to infraction of constitutional rights, including rights secured by the Fourteenth Amendment, by conduct which amounts to abuse of one's official place or reckless disregard of duty, no undue hazard or burden can be placed on state officials honestly seeking to perform the rightful functions of their office. Others are not entitled to greater protection.</p>
<p>But, it is said, a penumbra of rights may be involved, which none can know until decision has been made and infraction may occur before it is had. It seems doubtful this could be true in any case involving the abuse of official function which the statute requires and, if it could, that one guilty of such an abuse should have immunity for that reason. Furthermore, the doubtful character of the <span class="star-pagination">*131</span> right infringed could give reason at the most to invalidate the particular charge, not for outlawing the statute or narrowly restricting its application in advance of compelling occasion.</p>
<p>For there is a body of well-established, clear-cut fundamental rights, including many secured by the Fourteenth Amendment, to all of which the sections may and do apply, without specific enumeration and without creating hazards of uncertainty for conduct or defense. Others will enter that category. So far, at the least when they have done so, the sections should stand without question of their validity. Beyond this, the character of the act proscribed and the intent it necessarily implies would seem to afford would-be violators all of notice the law requires, that they act at peril of the penalty it places on their misconduct.</p>
<p>We have in this case no instance of mere error in judgment, made in good faith. It would be time enough to reverse and remand a conviction, obtained without instructions along these lines, if such a case should arise. Actually the substance of such instruction was given in the wholly adequate charge concerning the officer's right to use force, though not to excess. When, as here, a state official abuses his place consciously or grossly in abnegation of its rightful obligation, and thereby tramples underfoot the established constitutional rights of men or citizens, his conviction should stand when he has had the fair trial and full defense the petitioners have been given in this case.</p>
<p></p>
<h2>III</h2>
<p>Two implicit but highly important considerations must be noticed more definitely. One is the fear grounded in concern for possible maladjustment of federal-state relations if this and like convictions are sustained. Enough has been said to show that the fear is not well grounded. The same fear was expressed, by some in exaggerated and <span class="star-pagination">*132</span> highly emotional terms, when § 2 of the Civil Rights Act, the antecedent of § 20, was under debate in Congress.<sup>[33]</sup> The history of the legislation's enforcement gives it no support. The fear was not realized in later experience. Eighty years should be enough to remove any remaining vestige. The volume of prosecutions and convictions has been small, in view of the importance of the subject matter and the length of time the statutes have been in force. There are reasons for this, apart from self-restraint of federal prosecuting officials.</p>
<p>One lies in the character of the criminal act and the intent which must be proved. A strong case must be made to show abuse of official function, and therefore to secure indictment or conviction. Trial must be "by an impartial jury of the State and the district wherein the crime shall have been committed." Const., Amend. VI; cf. Art. III, § 2. For all practical purposes this means within the state of which the accused is an officer. Citizens of the state have not been, and will not be, ready to indict or convict their local officers on groundless charges or in doubtful cases. The sections can be applied effectively only when twelve of them concur in a verdict which accords with the prosecuting official's belief that the accused has violated another's fundamental rights. A federal official therefore faces both a delicate and a difficult task when he undertakes to charge and try a state officer under the terms of §§ 19 and 20. The restraint which has been shown is as much enforced by these limitations as it has been voluntary.</p>
<p><span class="star-pagination">*133</span> These are the reasons why prosecution has not been frequent, has been brought only in cases of gross abuse, and therefore has produced no grave or substantial problem of interference by federal authority in state affairs. But if the problem in this phase of the case were more serious than it has been or is likely to be, the result legally could not be to give state officials immunity from the obligations and liabilities the Amendment and its supporting legislation have imposed. For the verdict of the struggle which brought about adoption of the Amendment was to the contrary.</p>
<p>Lying beneath all the surface arguments is a deeper implication, which comprehends them. It goes to federal power. It is that Congress could not in so many words denounce as a federal crime the intentional and wrongful taking of an individual's life or liberty by a state official acting in abuse of his official function and applying to the deed all the power of his office. This is the ultimate purport of the notions that state action is not involved and that the crime is against the state alone, not the nation. It is reflected also in the idea that the statute can protect the victim in his many procedural rights encompassed in the right to a fair trial before condemnation, but cannot protect him in the right which comprehends all others, the right to life itself.</p>
<p>Suffice it to say that if these ideas did not pass from the American scene once and for all, as I think they did, upon adoption of the Amendment without more, they have long since done so. Violation of state law there may be. But from this no immunity to federal authority can arise where any part of the Constitution has made it supreme. To the Constitution state officials and the states themselves owe first obligation. The federal power lacks no strength to reach their malfeasance in office when it infringes constitutional rights. If that is a great power, it is one generated by the Constitution and the Amendments, <span class="star-pagination">*134</span> to which the states have assented and their officials owe prime allegiance.<sup>[34]</sup></p>
<p>The right not to be deprived of life or liberty by a state officer who takes it by abuse of his office and its power is such a right. To secure these rights is not beyond federal power. This §§ 19 and 20 have done, in a manner history long since has validated.</p>
<p>Accordingly, I would affirm the judgment.</p>
<p>My convictions are as I have stated them. Were it possible for me to adhere to them in my vote, and for the Court at the same time to dispose of the cause, I would act accordingly. The Court, however, is divided in opinion. If each member accords his vote to his belief, the case cannot have disposition. Stalemate should not prevail for any reason, however compelling, in a criminal cause or, if avoidable, in any other. My views concerning appropriate disposition are more nearly in accord with those stated by MR. JUSTICE DOUGLAS, in which three other members of the Court concur, than they are with the views of my dissenting brethren who favor outright reversal. Accordingly, in order that disposition may be made of this case, my vote has been cast to reverse the decision of the Court of Appeals and remand the cause to the District Court for further proceedings in accordance with the disposition required by the opinion of MR. JUSTICE DOUGLAS.</p>
<p>MR. JUSTICE MURPHY, dissenting.</p>
<p>I dissent. Robert Hall, a Negro citizen, has been deprived not only of the right to be tried by a court rather than by ordeal. He has been deprived of the right to life itself. That right belonged to him not because he was a Negro or a member of any particular race or creed. That right was his because he was an American citizen, because <span class="star-pagination">*135</span> he was a human being. As such, he was entitled to all the respect and fair treatment that befits the dignity of man, a dignity that is recognized and guaranteed by the Constitution. Yet not even the semblance of due process has been accorded him. He has been cruelly and unjustifiably beaten to death by local police officers acting under color of authority derived from the state. It is difficult to believe that such an obvious and necessary right is indefinitely guaranteed by the Constitution or is foreign to the knowledge of local police officers so as to cast any reasonable doubt on the conviction under § 20 of the Criminal Code of the perpetrators of this "shocking and revolting episode in law enforcement."</p>
<p>The Constitution and § 20 must be read together inasmuch as § 20 refers in part to certain provisions of the Constitution. Section 20 punishes anyone, acting under color of any law, who willfully deprives any person of any right, privilege or immunity secured or protected by the Constitution or laws of the United States. The pertinent part of the Constitution in this instance is § 1 of the Fourteenth Amendment, which firmly and unmistakably provides that no state shall deprive any person of life without due process of law. Translated in light of this specific provision of the Fourteenth Amendment, § 20 thus punishes anyone, acting under color of state law, who willfully deprives any person of life without due process of law. Such is the clear statutory provision upon which this conviction must stand or fall.</p>
<p>A grave constitutional issue, however, is said to lurk in the alleged indefiniteness of the crime outlawed by § 20. The rights, privileges and immunities secured or protected by the Constitution or laws of the United States are claimed to be so uncertain and flexible, dependent upon changeable legal concepts, as to leave a state official confused and ignorant as to what actions of his might run afoul of the law. The statute, it is concluded, must be set aside for vagueness.</p>
<p><span class="star-pagination">*136</span> It is axiomatic, of course, that a criminal statute must give a clear and unmistakable warning as to the acts which will subject one to criminal punishment. And courts are without power to supply that which Congress has left vague. But this salutary principle does not mean that if a statute is vague as to certain criminal acts but definite as to others the entire statute must fall. Nor does it mean that in the first case involving the statute to come before us we must delineate all the prohibited acts that are obscure and all those that are explicit.</p>
<p>Thus it is idle to speculate on other situations that might involve § 20 which are not now before us. We are unconcerned here with state officials who have coerced a confession from a prisoner, denied counsel to a defendant or made a faulty tax assessment. Whatever doubt may exist in those or in other situations as to whether the state officials could reasonably anticipate and recognize the relevant constitutional rights is immaterial in this case. Our attention here is directed solely to three state officials who, in the course of their official duties, have unjustifiably beaten and crushed the body of a human being, thereby depriving him of trial by jury and of life itself. The only pertinent inquiry is whether § 20, by its reference to the Fourteenth Amendment guarantee that no state shall deprive any person of life without due process of law, gives fair warning to state officials that they are criminally liable for violating this right to life.</p>
<p>Common sense gives an affirmative answer to that problem. The reference in § 20 to rights protected by the Constitution is manifest and simple. At the same time, the right not to be deprived of life without due process of law is distinctly and lucidly protected by the Fourteenth Amendment. There is nothing vague or indefinite in these references to this most basic of all human rights. Knowledge of a comprehensive law library is unnecessary for officers of the law to know that the right to murder <span class="star-pagination">*137</span> individuals in the course of their duties is unrecognized in this nation. No appreciable amount of intelligence or conjecture on the part of the lowliest state official is needed for him to realize that fact; nor should it surprise him to find out that the Constitution protects persons from his reckless disregard of human life and that statutes punish him therefor. To subject a state official to punishment under § 20 for such acts is not to penalize him without fair and definite warning. Rather it is to uphold elementary standards of decency and to make American principles of law and our constitutional guarantees mean something more than pious rhetoric.</p>
<p>Under these circumstances it is unnecessary to send this case back for a further trial on the assumption that the jury was not charged on the matter of the willfulness of the state officials, an issue that was not raised below or before us. The evidence is more than convincing that the officials willfully, or at least with wanton disregard of the consequences, deprived Robert Hall of his life without due process of law. A new trial could hardly make that fact more evident; the failure to charge the jury on willfulness was at most an inconsequential error. Moreover, the presence or absence of willfulness fails to decide the constitutional issue raised before us. Section 20 is very definite and certain in its reference to the right to life as spelled out in the Fourteenth Amendment quite apart from the state of mind of the state officials. A finding of willfulness can add nothing to the clarity of that reference.</p>
<p>It is an illusion to say that the real issue in this case is the alleged failure of § 20 fully to warn the state officials that their actions were illegal. The Constitution, § 20 and their own consciences told them that. They knew that they lacked any mandate or authority to take human life unnecessarily or without due process of law in the course of their duties. They knew that their excessive and abusive <span class="star-pagination">*138</span> use of authority would only subvert the ends of justice. The significant question, rather, is whether law enforcement officers and those entrusted with authority shall be allowed to violate with impunity the clear constitutional rights of the inarticulate and the friendless. Too often unpopular minorities, such as Negroes, are unable to find effective refuge from the cruelties of bigoted and ruthless authority. States are undoubtedly capable of punishing their officers who commit such outrages. But where, as here, the states are unwilling for some reason to prosecute such crimes the federal government must step in unless constitutional guarantees are to become atrophied.</p>
<p>This necessary intervention, however, will be futile if courts disregard reality and misuse the principle that criminal statutes must be clear and definite. Here state officers have violated with reckless abandon a plain constitutional right of an American citizen. The two courts below have found and the record demonstrates that the trial was fair and the evidence of guilt clear. And § 20 unmistakably outlaws such actions by state officers. We should therefore affirm the judgment.</p>
<p id="frankdissent">MR. JUSTICE ROBERTS, MR. JUSTICE FRANKFURTER and MR. JUSTICE JACKSON, dissenting.</p>
<p>Three law enforcement officers of Georgia, a county sheriff, a special deputy and a city policeman, arrested a young Negro charged with a local crime, that of stealing a tire. While he was in their custody and handcuffed, they so severely beat the lad that he died. This brutal misconduct rendered these lawless law officers guilty of manslaughter, if not of murder, under Georgia law. Instead of leaving this misdeed to vindication by Georgia law, the United States deflected Georgia's responsibility by instituting a federal prosecution. But this was a criminal homicide only under Georgia law. The United States could not prosecute the petitioners for taking life. Instead <span class="star-pagination">*139</span> a prosecution was brought, and the conviction now under review was obtained, under § 20 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 52</span>. Section 20, originating in § 2 of the Civil Rights Act of April 9, 1866, <span class="citation no-link">14 Stat. 27</span>, was put on the statute books on May 31, 1870, but for all practical purposes it has remained a dead letter all these years. This section provides that "Whoever, under color of any law, statute, ordinance, regulation, or custom, willfully subjects . . . any inhabitant of any State . .. to the deprivation of any rights, privileges, or immunities secured or protected by the Constitution and laws of the United States . . . shall be fined not more than one thousand dollars, or imprisoned not more than one year, or both." Under § 37 of the Criminal Code, <span class="citation no-link">18 U.S.C. § 88</span>, a conspiracy to commit any federal offense is punishable by imprisonment for two years. The theory of this prosecution is that one charged with crime is entitled to due process of law and that that includes the right to an orderly trial of which the petitioners deprived the Negro.</p>
<p>Of course the petitioners are punishable. The only issue is whether Georgia alone has the power and duty to punish, or whether this patently local crime can be made the basis of a federal prosecution. The practical question is whether the States should be relieved from responsibility to bring their law officers to book for homicide, by allowing prosecutions in the federal courts for a relatively minor offense carrying a short sentence. The legal question is whether, for the purpose of accomplishing this relaxation of State responsibility, hitherto settled principles for the protection of civil liberties shall be bent and tortured.</p>
<p></p>
<h2>I</h2>
<p>By the Thirteenth Amendment slavery was abolished. In order to secure equality of treatment for the emancipated, the Fourteenth Amendment was adopted at the <span class="star-pagination">*140</span> same time. To be sure, the latter Amendment has not been confined to instances of discrimination because of race or color. Undoubtedly, however, the necessary protection of the new freedmen was the most powerful impulse behind the Fourteenth Amendment. The vital part of that Amendment, § 1, reads as follows:</p>
<p>"All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside. No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws."</p>
<p>By itself, this Amendment is merely an instrument for striking down action by the States in defiance of it. It does not create rights and obligations actively enforceable by federal law. However, like all rights secured by the Constitution of the United States, those created by the Fourteenth Amendment could be enforced by appropriate federal legislation. The general power of Congress to pass measures effectuating the Constitution is given by Art. I, § 8, cl. 18  the Necessary-and-Proper Clause. In order to indicate the importance of enforcing the guarantees of Amendment XIV, its fifth section specifically provides: "The Congress shall have power to enforce, by appropriate legislation, the provisions of this article."</p>
<p>Accordingly, Congress passed various measures for its enforcement. It is familiar history that much of this legislation was born of that vengeful spirit which to no small degree envenomed the Reconstruction era. Legislative respect for constitutional limitations was not at its height and Congress passed laws clearly unconstitutional. See <i>Civil Rights Cases,</i> <span class="citation" data-id="90897"><a href="/opinion/90897/civil-rights-cases/" aria-description="Citation for case: Civil Rights Cases">109 U.S. 3</a></span>. One of the laws of this period was the Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>. In its <span class="star-pagination">*141</span> present form, as § 20, it is now here for the first time on full consideration as to its meaning and its constitutionality, unembarrassed by preoccupation both on the part of counsel and Court with the more compelling issue of the power of Congress to control State procedure for the election of federal officers. If § 20 were read as other legislation is read, by giving it the meaning which its language in its proper setting naturally and spontaneously yields, it is difficult to believe that there would be real doubt about the proper construction. The unstrained significance of the words chosen by Congress, the disclosed purpose for which they were chosen and to which they were limited, the always relevant implications of our federal system especially in the distribution of power and responsibility for the enforcement of the criminal law as between the States and the National Government, all converge to make plain what conduct Congress outlawed by the Act of 1870 and what impliedly it did not.</p>
<p>The Fourteenth Amendment prohibited a State from so acting as to deprive persons of new federal rights defined by it. Section 5 of the Amendment specifically authorized enabling legislation to enforce that prohibition. Since a State can act only through its officers, Congress provided for the prosecution of any officer who deprives others of their guaranteed rights and denied such an officer the right to defend by claiming the authority of the State for his action. In short, Congress said that no State can empower an officer to commit acts which the Constitution forbade the State from authorizing, whether such unauthorized command be given for the State by its legislative or judicial voice, or by a custom contradicting the written law. See <i>Nashville, C. &amp; St. L.R. Co.</i> v. <i>Browning,</i> <span class="citation" data-id="103360"><a href="/opinion/103360/nashville-chattanooga-st-louis-railway-v-browning/#369" aria-description="Citation for case: Nashville, Chattanooga &amp; St. Louis Railway v. Browning">310 U.S. 362, 369</a></span>. The present prosecution is not based on an officer's claim that that for which the United States seeks his punishment was commanded or authorized by the law of his State. On the contrary, <span class="star-pagination">*142</span> the present prosecution is based on the theory that Congress made it a federal offense for a State officer to violate the explicit law of his State. We are asked to construe legislation which was intended to effectuate prohibitions against States for defiance of the Constitution, to be equally applicable where a State duly obeys the Constitution, but an officer flouts State law and is unquestionably subject to punishment by the State for his disobedience.</p>
<p>So to read § 20 disregards not merely the normal function of language to express ideas appropriately. It fails not merely to leave to the States the province of local crime enforcement, that the proper balance of political forces in our federalism requires. It does both, heedless of the Congressional purpose, clearly evinced even during the feverish Reconstruction days, to leave undisturbed the power and the duty of the States to enforce their criminal law by restricting federal authority to the punishment only of those persons who violate federal rights under claim of State authority and not by exerting federal authority against offenders of State authority. Such a distortion of federal power devised against recalcitrant State authority never entered the minds of the proponents of the legislation.</p>
<p>Indeed, we have the weightiest evidence to indicate that they rejected that which now, after seventy-five years, the Government urges. Section 20 of the Criminal Code derived from § 2 of the Civil Rights Act of 1866, <span class="citation no-link">14 Stat. 27</span>. During the debate on that section, Senator Trumbull, the Chairman of the Senate Judiciary Committee, answered fears concerning the loose inclusiveness of the phrase "color of law." In particular, opponents of the Act were troubled lest it would make criminals of State judges and officials for carrying out their legal duties. Senator Trumbull agreed that they would be guilty if they consciously helped to enforce discriminatory State <span class="star-pagination">*143</span> legislation. Federal law, replied Senator Trumbull, was directed against those, and only against those, who were not punishable by State law precisely because they acted in obedience to unconstitutional State law and by State law justified their action. Said Senator Trumbull, "If an offense is committed against a colored person simply because he is colored, in a State where the law affords him the same protection as if he were white, this act neither has nor was intended to have anything to do with his case, because he has adequate remedies in the State courts; but if he is discriminated against under color of State laws because he is colored, then it becomes necessary to interfere for his protection." Cong. Globe, 39th Cong., 1st Sess., p. 1758. And this language applies equally to § 17 of the Act of May 31, 1870, <span class="citation no-link">16 Stat. 140</span>, 144 (now § 20 of the Criminal Code), which reenacted the Civil Rights Act.</p>
<p>That this legislation was confined to attempted deprivations of federal rights by State law and was not extended to breaches of State law by its officials, is likewise confirmed by observations of Senator Sherman, another leading Reconstruction statesman. When asked about the applicability of the 1870 Act to a Negro's right to vote when State law provided for that right, Senator Sherman replied, "That is not the case with which we are dealing. I intend to propose an amendment to present a question of that kind. This bill only proposes to deal with offenses committed by officers or persons under color of existing State law, under color of existing State constitutions. No man could be convicted under this bill reported by the Judiciary Committee unless the denial of the right to vote was done under color or pretense of State regulation. The whole bill shows that. My honorable friend from California has not read this bill with his usual care if he does not see that that runs through the whole of the provisions of the first and second sections of the bill, which <span class="star-pagination">*144</span> simply punish officers as well as persons for discrimination under color of State laws or constitutions; and so it provides all the way through." Cong. Globe, 41st Cong., 2d Sess., p. 3663. The debates in Congress are barren of any indication that the supporters of the legislation now before us had the remotest notion of authorizing the National Government to prosecute State officers for conduct which their State had made a State offense where the settled custom of the State did not run counter to formulated law.</p>
<p>Were it otherwise it would indeed be surprising. It was natural to give the shelter of the Constitution to those basic human rights for the vindication of which the successful conduct of the Civil War was the end of a long process. And the extension of federal authority so as to guard against evasion by any State of these newly created federal rights was an obvious corollary. But to attribute to Congress the making overnight of a revolutionary change in the balance of the political relations between the National Government and the States without reason, is a very different thing. And to have provided for the National Government to take over the administration of criminal justice from the States to the extent of making every lawless act of the policeman on the beat or in the station house, whether by way of third degree or the illegal ransacking for evidence in a man's house (see <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>; <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>), a federal offense, would have constituted a revolutionary break with the past overnight. The desire for such a dislocation in our federal system plainly was not contemplated by the Lyman Trumbulls and the John Shermans, and not even by the Thaddeus Stevenses.</p>
<p>Regard for maintaining the delicate balance "between the judicial tribunals of the Union and of the States" in <span class="star-pagination">*145</span> the enforcement of the criminal law has informed this Court, as it has influenced Congress, "in recognition of the fact that the public good requires that those relations be not disturbed by unnecessary conflict between courts equally bound to guard and protect rights secured by the Constitution." <i>Ex parte Royall,</i> <span class="citation" data-id="91598"><a href="/opinion/91598/ex-parte-royall/#251" aria-description="Citation for case: Ex Parte Royall">117 U.S. 241, 251</a></span>. Observance of this basic principle under our system of Government has led this Court to abstain, even under more tempting circumstances than those now here, from needless extension of federal criminal authority into matters that normally are of State concern and for which the States had best be charged with responsibility.</p>
<p>We have reference to § 33 of the Judicial Code, as amended, <span class="citation no-link">28 U.S.C. § 76</span>. That provision gives the right of removal to a federal court of any criminal prosecution begun in a State court against a revenue officer of the United States "on account of any act done under color of his office or of any such [revenue] law." Where a State prosecution for manslaughter is resisted by the claim that what was done was justifiably done by a United States officer one would suppose that this Court would be alert to construe very broadly "under color of his office or of any such law" in order to avoid the hazards of trial, whether through conscious or unconscious discrimination or hostility, of a United States officer accused of homicide and to assure him a trial in a presumably more impartial federal court. But this Court long ago indicated that misuse of federal authority does not come within the statute's protection. <i>Tennessee</i> v. <i>Davis,</i> <span class="citation" data-id="90038"><a href="/opinion/90038/tennessee-v-davis/#261" aria-description="Citation for case: Tennessee v. Davis">100 U.S. 257, 261-262</a></span>. More recently, this Court in a series of cases unanimously insisted that a petition for removal must show with particularity that the offense for which the State is prosecuting resulted from a discharge of federal duty. "It must appear that the prosecution of him, for whatever offense, has arisen out of the acts done by him under color of federal authority and in enforcement of federal law, and <span class="star-pagination">*146</span> he must by direct averment exclude the possibility that it was based on acts or conduct of his not justified by his federal duty. . . . The defense he is to make is that of his immunity from punishment by the State, because what he did was justified by his duty under the federal law, and because he did nothing else on which the prosecution could be based." <i>Maryland</i> v. <i>Soper</i> (No. 1), <span class="citation" data-id="100776"><a href="/opinion/100776/maryland-v-soper-judge/#33" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 9, 33</a></span>. And see <i>Maryland</i> v. <i>Soper</i> (No. 2), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36</a></span>; <i>Maryland</i> v. <i>Soper</i> (No. 3), <span class="citation" data-id="1410842"><a href="/opinion/1410842/maryland-v-soper-no-3/" aria-description="Citation for case: Maryland v. Soper (No. 3)">270 U.S. 44</a></span>; <i>Colorado</i> v. <i>Symes,</i> <span class="citation" data-id="101949"><a href="/opinion/101949/colorado-v-symes/" aria-description="Citation for case: Colorado v. Symes">286 U.S. 510</a></span>. To the suggestion that such a limited construction of the removal statute enacted for the protection of the United States officers would restrict its effectiveness, the answer was that if Congress chose to afford even greater protection and to withdraw from the States the right and duty to enforce their criminal law in their own courts, it should express its desire more specifically. <i>Maryland</i> v. <i>Soper</i> (No. 2), <span class="citation" data-id="1410732"><a href="/opinion/1410732/maryland-v-soper-judge/#42" aria-description="Citation for case: Maryland v. Soper, Judge">270 U.S. 36, 42, 44</a></span>. That answer should be binding in the situation now before us.</p>
<p>The reasons which led this Court to give such a retricted scope to the removal statute are even more compelling as to § 20. The matter concerns policies inherent in our federal system and the undesirable consequences of federal prosecution for crimes which are obviously and predominantly State crimes no matter how much sophisticated argumentation may give them the appearance of federal crimes. Congress has not expressed a contrary purpose, either by the language of its legislation or by anything appearing in the environment out of which its language came. The practice of government for seventy-five years likewise speaks against it. Nor is there a body of judicial opinion which bids us find in the unbridled excess of a State officer, constituting a crime under his State law, action taken "under color of law" which federal law forbids.</p>
<p>Only two reported cases considered § 20 before <i>United States</i> v. <i>Classic,</i> <span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">313 U.S. 299</a></span>. In <i>United States</i> v. <i>Buntin,</i> <span class="star-pagination">*147</span> <span class="citation" data-id="8122539"><a href="/opinion/8160884/united-states-v-buntin/" aria-description="Citation for case: United States v. Buntin">10 F. 730</a></span>, a teacher, in reliance on a State statute, refused admittance to a colored child, while in <i>United States</i> v. <i>Stone,</i> <span class="citation" data-id="8779667"><a href="/opinion/8795605/united-states-v-stone/" aria-description="Citation for case: United States v. Stone">188 F. 836</a></span>, election supervisors who acted under a Maryland election law were held to act "under color of law." In neither case was there a patent violation of State law but rather an attempt at justification under State law. <i>United States</i> v. <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic, supra</a></span></i><i>,</i> is the only decision that looks the other way. In that case primary election officials were held to have acted "under color of law" even though the acts complained of as a federal offense were likewise condemned by Louisiana law. The truth of the matter is that the focus of attention in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case was not our present problem, but was the relation of primaries to the protection of the electoral process under the United States Constitution. The views in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case thus reached ought not to stand in the way of a decision on the merits of a question which has now for the first time been fully explored and its implications for the workings of our federal system have been adequately revealed.</p>
<p>It was assumed quite needlessly in the <i><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/" aria-description="Citation for case: United States v. Classic">Classic</a></span></i> case that the scope of § 20 was coextensive with the Fourteenth Amendment. Because the weight of the case was elsewhere, we did not pursue the difference between the power granted to Congress by that Amendment to bar "any State" from depriving persons of the newly created constitutional rights and the limited extent to which Congress exercised that power, in what is now § 20, by making it an offense for one acting "under color of any law" to deprive another of such constitutional rights. It may well be that Congress could, within the bounds of the Fourteenth Amendment, treat action taken by a State official even though in defiance of State law and not condoned by ultimate State authority as the action of "a State." It has never been satisfactorily explained how a State can be said to deprive a person of liberty or property without <span class="star-pagination">*148</span> due process of law when the foundation of the claim is that a minor official has disobeyed the authentic command of his State. See <i>Raymond</i> v. <i>Chicago Traction Co.,</i> <span class="citation" data-id="96704"><a href="/opinion/96704/raymondv-v-chicago-union-traction-co/#40" aria-description="Citation for case: Raymondv v. Chicago Union Traction Co.">207 U.S. 20, 40, 41</a></span>. Although action taken under such circumstances has been deemed to be deprivation by a "State" of rights guaranteed by the Fourteenth Amendment for purposes of federal jurisdiction, the doctrine has had a fluctuating and dubious history. Compare <i>Barney</i> v. <i>City of New York,</i> <span class="citation" data-id="96036"><a href="/opinion/96036/barney-v-city-of-new-york/" aria-description="Citation for case: Barney v. City of New York">193 U.S. 430</a></span>, with <i>Raymond</i> v. <i>Chicago Traction Co., supra</i><i>; </i><i>Memphis</i> v. <i>Cumberland Telephone Co.,</i> <span class="citation" data-id="9418191"><a href="/opinion/97326/city-of-memphis-v-cumberland-telephone-telegraph-co/" aria-description="Citation for case: City of Memphis v. Cumberland Telephone &amp; Telegraph Co.">218 U.S. 624</a></span>, with <i>Home Tel. &amp; Tel. Co.</i> v. <i>Los Angeles,</i> <span class="citation" data-id="97779"><a href="/opinion/97779/home-telephone-telegraph-co-v-city-of-los-angeles/" aria-description="Citation for case: Home Telephone &amp; Telegraph Co. v. City of Los Angeles">227 U.S. 278</a></span>. <i>Barney</i> v. <i>City of New York, supra</i><i>,</i> which ruled otherwise, although questioned, has never been overruled. See, for instance, <i>Iowa-Des Moines Bank</i> v. <i>Bennett,</i> <span class="citation" data-id="101816"><a href="/opinion/101816/iowa-des-moines-national-bank-v-bennett/#246" aria-description="Citation for case: Iowa-Des Moines National Bank v. Bennett">284 U.S. 239, 246-247</a></span>, and <i>Snowden</i> v. <i>Hughes,</i> <span class="citation" data-id="9419429"><a href="/opinion/103921/snowden-v-hughes/#13" aria-description="Citation for case: Snowden v. Hughes">321 U.S. 1, 13</a></span>.<sup>[1]</sup></p>
<p>But assuming unreservedly that conduct such as that now before us, perpetrated by State officers in flagrant defiance of State law, may be attributed to the State under the Fourteenth Amendment, this does not make it action under "color of any law." Section 20 is much narrower than the power of Congress. Even though Congress might have swept within the federal criminal law any action that could be deemed within the vast reach of the Fourteenth Amendment, Congress did not do so. The presuppositions of our federal system, the pronouncements of the statesmen who shaped this legislation, and the normal meaning of language powerfully counsel against attributing to Congress intrusion into the sphere of criminal law traditionally <span class="star-pagination">*149</span> and naturally reserved for the States alone. When due account is taken of the considerations that have heretofore controlled the political and legal relations between the States and the National Government, there is not the slightest warrant in the reason of things for torturing language plainly designed for nullifying a claim of acting under a State law that conflicts with the Constitution so as to apply to situations where State law is in conformity with the Constitution and local misconduct is in undisputed violation of that State law. In the absence of clear direction by Congress we should leave to the States the enforcement of their criminal law, and not relieve States of the responsibility for vindicating wrongdoing that is essentially local or weaken the habits of local law enforcement by tempting reliance on federal authority for an occasional unpleasan

[...TRUNCATED 68811 of 188811 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/See v. City of Seattle.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "See v. City of Seattle"
type: case
citation: "387 U.S. 541 (1967)"
parallel_cite: "87 S. Ct. 1737; 18 L. Ed. 2d 943"
neutral_cite: 1967 U.S. LEXIS 1255
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-06-05
docket: 180
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: See v. City of Seattle
  varies_by_point: false
  scope_note: "Good law; the commercial-premises companion to Camara. Later cases recognized the pervasively-regulated-industry exception (Barlow's, Donovan v. Dewey, Biswell, Burger) but did not disturb See's general warrant rule."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107474/see-v-city-of-seattle/"
  cluster_id: 107474
  opinion_id: 107474
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Anchor (commercial inspections)"
  - page: "[[Curtilage]]"
    role: "Related (cross-doctrine)"
related: ["[[Camara v. Municipal Court]]", "[[Marshall v. Barlow's Inc.]]"]
aliases: []
tags: ["case", "fourth-amendment", "administrative-search", "inspections", "commercial-premises", "warrant"]
holding: "An administrative inspection of the nonpublic portions of commercial premises generally requires a warrant; a businessman, like a homeowner, may refuse a warrantless regulatory entry and cannot be punished for that refusal."
lake:
  record_id: See v. City of Seattle
  status: verified
  projected_at: 2026-07-09
---

# See v. City of Seattle

*387 U.S. 541 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Seattle fire inspector sought to enter See's locked commercial warehouse as part of a routine, area-wide fire-code inspection. See refused to permit the entry because the inspector had no warrant, and he was convicted of violating a city ordinance making it unlawful to refuse a lawful inspection. Decided the same day as *[[Camara v. Municipal Court]]* (residences), *See* extended the question to commercial premises.

## Issue
Whether the Fourth Amendment permits a municipality to punish a businessman for refusing to consent to a warrantless administrative inspection of the nonpublic portions of his commercial premises.

## Rule
No. Commercial premises receive Fourth Amendment protection against warrantless regulatory entry. "The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property." — 387 U.S. at 543. ^pin-543

"We therefore conclude that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure." — [*Id.* at 545](https://www.courtlistener.com/opinion/107474/see-v-city-of-seattle/#:~:text=We%20therefore%20conclude%20that%20administrative). ^pin-545

## Application
See's warehouse was private commercial property not open to the public, and the inspector had no warrant. Because the Fourth Amendment guards a businessman's commercial premises much as it guards a home, See had a constitutional right to insist on a warrant and could not be criminally punished for refusing the warrantless inspection. The Court left intact reasonable inspections in many regulatory settings and accepted licensing schemes, deciding only that a warrant procedure governs a contested nonpublic entry.

## Conclusion
See could not be convicted for refusing the warrantless inspection; his conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *See* is the commercial-premises companion to [[Camara v. Municipal Court]]. Later decisions carved a **pervasively-regulated-industry exception** that dispenses with the warrant for certain heavily regulated businesses (e.g., [[Marshall v. Barlow's Inc.]], *[[Donovan v. Dewey]]*, *[[United States v. Biswell]]*, *[[New York v. Burger]]*), but *See*'s default warrant rule for ordinary commercial inspections remains good law.

## Appears on
- [[Special Needs and Administrative Searches]] — *Anchor (commercial inspections)*

## Sources
- *See v. City of Seattle*, 387 U.S. 541 (1967) — https://www.courtlistener.com/opinion/107474/see-v-city-of-seattle/ — pinpoints: 543, 545.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b329f9186827d323", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "See v. City of Seattle"}, "payload": {"all": [{"cite": "387 U.S. 541", "page": "541", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "387"}, {"cite": "87 S. Ct. 1737", "page": "1737", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 943", "page": "943", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 1255", "page": "1255", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "387 U.S. 541", "official": {"cite": "387 U.S. 541", "page": "541", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "387"}, "official_selection_present": true, "record_id": "See v. City of Seattle"}}
{"assertion_id": "3d44a0db7ebdabb4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-543", "record_id": "See v. City of Seattle"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-543", "pinpoint_status": "slip-only", "quote": "--- # See v. City of Seattle *387 U.S. 541 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Seattle fire inspector sought to enter See's locked commercial warehouse as part of a routine, area-wide fire-code inspection. See refused to permit the entry because the inspector had no warrant, and he was convicted of violating a city ordinance making it unlawful to refuse a lawful inspection. Decided the same day as *Camara v. Municipal Court* (residences), *See* extended the question to commercial premises. ## Issue Whether the Fourth Amendment permits a municipality to punish a businessman for refusing to consent to a warrantless administrative inspection of the nonpublic portions of his commercial premises. ## Rule No. Commercial premises receive Fourth Amendment protection against warrantless regulatory entry.", "quote_fidelity": "mismatch", "record_id": "See v. City of Seattle", "star_marker": null}}
{"assertion_id": "9f15c1a7b3399d9a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-545", "record_id": "See v. City of Seattle"}, "payload": {"fragment": "#:~:text=We%20therefore%20conclude%20that%20administrative", "page": null, "pin_id": "pin-545", "pinpoint_status": "star-verified", "quote": "We therefore conclude that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure.", "quote_fidelity": "matched", "record_id": "See v. City of Seattle", "star_marker": "545"}}
{"assertion_id": "b5d282a79d04379a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "See v. City of Seattle"}, "payload": {"as_of_content": "1967-06-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "See v. City of Seattle", "scope_note": "Good law; the commercial-premises companion to Camara. Later cases recognized the pervasively-regulated-industry exception (Barlow's, Donovan v. Dewey, Biswell, Burger) but did not disturb See's general warrant rule.", "varies_by_point": false}}
```

### lake record — See v. City of Seattle

```json
{
  "schema_version": "s2.v1",
  "record_id": "See v. City of Seattle",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "See v. City of Seattle",
    "case_name_short": "See",
    "case_name_full": "See v. City of Seattle",
    "input_case_name": "See v. City of Seattle",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-06-05",
    "year": 1967,
    "docket": "180",
    "cluster_id": 107474,
    "lead_opinion_id": 107474,
    "sibling_ids": [
      107474,
      9423449,
      9423450
    ],
    "absolute_url": "/opinion/107474/see-v-city-of-seattle/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "387 U.S. 541",
      "volume": "387",
      "reporter": "U.S.",
      "page": "541",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1737",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 943",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "943",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 1255",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1255",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "387 U.S. 541",
        "volume": "387",
        "reporter": "U.S.",
        "page": "541",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1737",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1737",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 943",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "943",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 1255",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "1255",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "387 U.S. 541",
    "official_selection": {
      "court_class": "scotus",
      "selected": "387 U.S. 541",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-543",
      "page": null,
      "quote": "--- # See v. City of Seattle *387 U.S. 541 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Seattle fire inspector sought to enter See's locked commercial warehouse as part of a routine, area-wide fire-code inspection. See refused to permit the entry because the inspector had no warrant, and he was convicted of violating a city ordinance making it unlawful to refuse a lawful inspection. Decided the same day as *Camara v. Municipal Court* (residences), *See* extended the question to commercial premises. ## Issue Whether the Fourth Amendment permits a municipality to punish a businessman for refusing to consent to a warrantless administrative inspection of the nonpublic portions of his commercial premises. ## Rule No. Commercial premises receive Fourth Amendment protection against warrantless regulatory entry.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-545",
      "page": null,
      "quote": "We therefore conclude that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure.",
      "star_marker": "545",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9499,
      "fragment": "#:~:text=We%20therefore%20conclude%20that%20administrative",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "See v. City of Seattle",
    "varies_by_point": false,
    "scope_note": "Good law; the commercial-premises companion to Camara. Later cases recognized the pervasively-regulated-industry exception (Barlow's, Donovan v. Dewey, Biswell, Burger) but did not disturb See's general warrant rule.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3262306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perry G. Blocker",
          "cluster_id": 733272,
          "cite": [
            "104 F.3d 720",
            "1997 U.S. App. LEXIS 712",
            "1997 WL 14762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Argent Chemical Laboratories, Inc.",
          "cluster_id": 7038653,
          "cite": [
            "93 F.3d 572",
            "96 Cal. Daily Op. Serv. 6117",
            "96 Daily Journal DAR 10005",
            "1996 U.S. App. LEXIS 20462",
            "1996 WL 465363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Paxton",
          "cluster_id": 4020585,
          "cite": [
            "615 N.E.2d 1086",
            "83 Ohio App. 3d 818",
            "1992 Ohio App. LEXIS 5867"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Higbie v. State",
          "cluster_id": 2412833,
          "cite": [
            "780 S.W.2d 228",
            "1989 Tex. Crim. App. LEXIS 182",
            "1989 WL 118822"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane1_negative"
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
        "journal_ref": "See v. City of Seattle:lane1_negative"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tyler",
          "cluster_id": 109874,
          "cite": [
            "56 L. Ed. 2d 486",
            "98 S. Ct. 1942",
            "436 U.S. 499",
            "1978 U.S. LEXIS 97"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dunn",
          "cluster_id": 111833,
          "cite": [
            "94 L. Ed. 2d 326",
            "107 S. Ct. 1134",
            "480 U.S. 294",
            "1987 U.S. LEXIS 1057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Almeida-Sanchez v. United States",
          "cluster_id": 108845,
          "cite": [
            "37 L. Ed. 2d 596",
            "93 S. Ct. 2535",
            "413 U.S. 266",
            "1973 U.S. LEXIS 44"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berger v. New York",
          "cluster_id": 107483,
          "cite": [
            "18 L. Ed. 2d 1040",
            "87 S. Ct. 1873",
            "388 U.S. 41",
            "1967 U.S. LEXIS 2964"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
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
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Biswell",
          "cluster_id": 108533,
          "cite": [
            "32 L. Ed. 2d 87",
            "92 S. Ct. 1593",
            "406 U.S. 311",
            "1972 U.S. LEXIS 60"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mancusi v. DeForte",
          "cluster_id": 107745,
          "cite": [
            "20 L. Ed. 2d 1154",
            "88 S. Ct. 2120",
            "392 U.S. 364",
            "1968 U.S. LEXIS 3075",
            "68 L.R.R.M. (BNA) 2449"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colonnade Catering Corp. v. United States",
          "cluster_id": 108077,
          "cite": [
            "25 L. Ed. 2d 60",
            "90 S. Ct. 774",
            "397 U.S. 72",
            "1970 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donovan v. Dewey",
          "cluster_id": 110530,
          "cite": [
            "69 L. Ed. 2d 262",
            "101 S. Ct. 2534",
            "452 U.S. 594",
            "1980 U.S. LEXIS 58"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avery v. Midland County",
          "cluster_id": 107647,
          "cite": [
            "20 L. Ed. 2d 45",
            "88 S. Ct. 1114",
            "390 U.S. 474",
            "1968 U.S. LEXIS 2061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "G. M. Leasing Corp. v. United States",
          "cluster_id": 109579,
          "cite": [
            "50 L. Ed. 2d 530",
            "97 S. Ct. 619",
            "429 U.S. 338",
            "1977 U.S. LEXIS 33",
            "39 A.F.T.R.2d (RIA) 475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California Bankers Assn. v. Shultz",
          "cluster_id": 109005,
          "cite": [
            "39 L. Ed. 2d 812",
            "94 S. Ct. 1494",
            "416 U.S. 21",
            "1974 U.S. LEXIS 34",
            "33 A.F.T.R.2d (RIA) 1041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyman v. James",
          "cluster_id": 108223,
          "cite": [
            "27 L. Ed. 2d 408",
            "91 S. Ct. 381",
            "400 U.S. 309",
            "1971 U.S. LEXIS 106"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Clifford",
          "cluster_id": 111057,
          "cite": [
            "78 L. Ed. 2d 477",
            "104 S. Ct. 641",
            "464 U.S. 287",
            "1984 U.S. LEXIS 14",
            "52 U.S.L.W. 4056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dow Chemical Co. v. United States Ex Rel. Administrator",
          "cluster_id": 111667,
          "cite": [
            "90 L. Ed. 2d 226",
            "106 S. Ct. 1819",
            "476 U.S. 227",
            "1986 U.S. LEXIS 155",
            "16 Envtl. L. Rep. (Envtl. Law Inst.) 20679",
            "54 U.S.L.W. 4464",
            "24 ERC (BNA) 1385"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "See v. City of Seattle:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107474 OR 9423449 OR 9423450) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NTU4OTc2MDAwMDAmcz0xNDY0ODkzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107474+OR+9423449+OR+9423450%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(107474 OR 9423449 OR 9423450)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMmcz0yNTQ2NDg1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107474+OR+9423449+OR+9423450%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107474 OR 9423449 OR 9423450)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 0,
        "triage_snippet_classified": 14
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107474 OR 9423449 OR 9423450)",
    "indexed_citing_opinions": 789,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107474,
        "count": 715,
        "count_source": "search"
      },
      {
        "opinion_id": 9423449,
        "count": 98,
        "count_source": "search"
      },
      {
        "opinion_id": 9423450,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1228,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/see-v-city-of-seattle.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY0ODE1MjImcz00NjY3MTQ3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107474+OR+9423449+OR+9423450%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107474,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 100375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 104239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 104758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 104766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 105052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 105244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 1329358,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 1421045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 2008391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107474,
        "cited_id": 2435050,
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
    "date_created": "2026-07-05T18:57:20Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:57:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:57:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:12:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:57:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — See v. City of Seattle

```
<div>
<center><b><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U.S. 541</a></span> (1967)</b></center>
<center><h1>SEE<br>
v.<br>
CITY OF SEATTLE.</h1></center>
<center>No. 180.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 15, 1967.</center>
<center>Decided June 5, 1967.</center>
APPEAL FROM THE SUPREME COURT OF WASHINGTON.
<p><i>Norman Dorsen</i> argued the cause for appellant. With him on the briefs were <i>Melvin L. Wulf</i> and <i>Marvin M. Karpatkin.</i></p>
<p><i>A. L. Newbould</i> argued the cause for appellee. With him on the brief was <i>Charles S. Rhyne.</i></p>
<p>MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>Appellant seeks reversal of his conviction for refusing to permit a representative of the City of Seattle Fire Department to enter and inspect appellant's locked commercial warehouse without a warrant and without probable cause to believe that a violation of any municipal ordinance existed therein. The inspection was conducted as part of a routine, periodic city-wide canvass to obtain compliance with Seattle's Fire Code. City of Seattle Ordinance No. 87870, c. 8.01. After he refused the inspector access, appellant was arrested and charged with violating § 8.01.050 of the Code:</p>
<blockquote>"INSPECTION OF BUILDING AND PREMISES. It shall be the duty of the Fire Chief to inspect and he may enter all buildings and premises, except the interiors of dwellings, as often as may be necessary for the purpose of ascertaining and causing to be corrected any conditions liable to cause fire, or any violations of the provisions of this Title, and of any other ordinance concerning fire hazards."</blockquote>
<p><span class="star-pagination">*542</span> Appellant was convicted and given a suspended fine of $100<sup>[1]</sup> despite his claim that § 8.01.050, if interpreted to authorize this warrantless inspection of his warehouse, would violate his rights under the Fourth and Fourteenth Amendments. We noted probable jurisdiction and set this case for argument with <i>Camara</i> v. <i>Municipal Court, ante,</i> p. 523. <span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">385 U. S. 808</a></span>. We find the principles enunciated in the <i><span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">Camara</a></span></i> opinion applicable here and therefore we reverse.</p>
<p>In <i><span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">Camara</a></span>,</i> we held that the Fourth Amendment bars prosecution of a person who has refused to permit a warrantless code-enforcement inspection of his personal residence. The only question which this case presents is whether <i><span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">Camara</a></span></i> applies to similar inspections of commercial structures which are not used as private residences. The Supreme Court of Washington, in affirming appellant's conviction, suggested that this Court "has applied different standards of reasonableness to searches of dwellings than to places of business," citing <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>. The Washington court held, and appellee here argues, that § 8.01.050, which excludes "the interiors of dwellings,"<sup>[2]</sup> establishes a <span class="star-pagination">*543</span> reasonable scheme for the warrantless inspection of commercial premises pursuant to the Seattle Fire Code.</p>
<p>In <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>; and <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, this Court refused to uphold otherwise unreasonable criminal investigative searches merely because commercial rather than residential premises were the object of the police intrusions. Likewise, we see no justification for so relaxing Fourth Amendment safeguards where the official inspection is intended to aid enforcement of laws prescribing minimum physical standards for commercial premises. As we explained in <i><span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">Camara</a></span>,</i> a search of private houses is presumptively unreasonable if conducted without a warrant. The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property. The businessman, too, has that right placed in jeopardy if the decision to enter and inspect for violation of regulatory laws can be made and enforced by the inspector in the field without official authority evidenced by a warrant.</p>
<p>As governmental regulation of business enterprise has mushroomed in recent years, the need for effective investigative techniques to achieve the aims of such regulation has been the subject of substantial comment and legislation.<sup>[3]</sup> Official entry upon commercial property <span class="star-pagination">*544</span> is a technique commonly adopted by administrative agencies at all levels of government to enforce a variety of regulatory laws; thus, entry may permit inspection of the structure in which a business is housed, as in this case, or inspection of business products, or a perusal of financial books and records. This Court has not had occasion to consider the Fourth Amendment's relation to this broad range of investigations.<sup>[4]</sup> However, we have dealt with the Fourth Amendment issues raised by another common investigative technique, the administrative subpoena of corporate books and records. We find strong support in these subpoena cases for our conclusion that warrants are a necessary and a tolerable limitation on the right to enter upon and inspect commercial premises.</p>
<p>It is now settled that, when an administrative agency subpoenas corporate books or records, the Fourth Amendment requires that the subpoena be sufficiently limited in scope, relevant in purpose, and specific in directive so that compliance will not be unreasonably burdensome.<sup>[5]</sup> The agency has the right to conduct all reasonable inspections of such documents which are contemplated by statute, but it must delimit the confines of a search by designating the needed documents in a formal subpoena. In addition, while the demand to inspect may be issued by the agency, in the form of an administrative subpoena, it may not be made and enforced <span class="star-pagination">*545</span> by the inspector in the field, and the subpoenaed party may obtain judicial review of the reasonableness of the demand prior to suffering penalties for refusing to comply.</p>
<p>It is these rather minimal limitations on administrative action which we think are constitutionally required in the case of investigative entry upon commercial establishments. The agency's particular demand for access will of course be measured, in terms of probable cause to issue a warrant, against a flexible standard of reasonableness that takes into account the public need for effective enforcement of the particular regulation involved. But the decision to enter and inspect will not be the product of the unreviewed discretion of the enforcement officer in the field.<sup>[6]</sup> Given the analogous investigative functions performed by the administrative subpoena and the demand for entry, we find untenable the proposition that the subpoena, which has been termed a "constructive" search, <i>Oklahoma Press Pub. Co.</i> v. <i>Walling,</i> <span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/#202" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186, 202</a></span>, is subject to Fourth Amendment limitations which do not apply to actual searches and inspections of commercial premises.</p>
<p>We therefore conclude that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure.<sup>[7]</sup> We do not in any way <span class="star-pagination">*546</span> imply that business premises may not reasonably be inspected in many more situations than private homes, nor do we question such accepted regulatory techniques as licensing programs which require inspections prior to operating a business or marketing a product. Any constitutional challenge to such programs can only be resolved, as many have been in the past, on a case-by-case basis under the general Fourth Amendment standard of reasonableness. We hold only that the basic component of a reasonable search under the Fourth Amendmentthat it not be enforced without a suitable warrant procedureis applicable in this context, as in others, to business as well as to residential premises. Therefore, appellant may not be prosecuted for exercising his constitutional right to insist that the fire inspector obtain a warrant authorizing entry upon appellant's locked warehouse.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE CLARK, with whom MR. JUSTICE HARLAN and MR. JUSTICE STEWART join, dissenting.<sup>[*]</sup></p>
<p>Eight years ago my Brother Frankfurter wisely wrote in <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360</a></span> (1959):</p>
<blockquote>"Time and experience have forcefully taught that the power to inspect dwelling places, either as a matter of systematic area-by-area search or, as here, to treat a specific problem, is of indispensable importance to the maintenance of community health; a power that would be greatly hobbled by the blanket requirement of the safeguards necessary for a search of evidence of criminal acts. The need for preventive <span class="star-pagination">*547</span> action is great, and city after city has seen this need and granted the power of inspection to its health officials; and these inspections are apparently welcomed by all but an insignificant few." At 372.</blockquote>
<p>Today the Court renders this municipal experience, which dates back to Colonial days, for naught by overruling <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span></i> and by striking down hundreds of city ordinances throughout the country and jeopardizing thereby the health, welfare, and safety of literally millions of people.</p>
<p>But this is not all. It prostitutes the command of the Fourth Amendment that "no Warrants shall issue, but upon probable cause" and sets up in the health and safety codes area inspection a newfangled "warrant" system that is entirely foreign to Fourth Amendment standards. It is regrettable that the Court wipes out such a long and widely accepted practice and creates in its place such enormous confusion in all of our towns and metropolitan cities in one fell swoop. I dissent.</p>
<p></p>
<h2>I.</h2>
<p>I shall not treat in any detail the constitutional issue involved. For me it was settled in <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland, supra</a></span></i><i>.</i> I would adhere to that decision and the reasoning therein of my late Brother Frankfurter. Time has not shown any need for change. Indeed the opposite is true, as I shall show later. As I read it, the Fourth Amendment guarantee of individual privacy is, by its language, specifically qualified. It prohibits only those searches that are "unreasonable." The majority seem to recognize this for they set up a new test for the long-recognized and enforced Fourth Amendment's "probable-cause" requirement for the issuance of warrants. They would permit the issuance of paper warrants, in area inspection programs, with probable cause based on area inspection standards as set out in municipal codes, and <span class="star-pagination">*548</span> with warrants issued by the rubber stamp of a willing magistrate.<sup>[1]</sup> In my view, this degrades the Fourth Amendment.</p>
<p></p>
<h2>II.</h2>
<p>Moreover, history supports the <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> disposition. Over 150 years of city <i>in rem</i> inspections for health and safety purposes have continuously been enforced. In only one case during all that period have the courts denied municipalities this right. See <i>District of Columbia</i> v. <i>Little,</i> 85 U. S. App. D. C. 242, <span class="citation" data-id="9442232"><a href="/opinion/223783/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">178 F. 2d 13</a></span> (1949), aff'd on other grounds, <span class="citation" data-id="104766"><a href="/opinion/104766/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">339 U. S. 1</a></span> (1950). In addition to the two cases in this Court (<i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank, supra,</a></span></i> and <i>Eaton</i> v. <i>Price,</i> <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263</a></span> (1960)), which have upheld the municipal action, not a single state high court has held against the validity of such ordinances. Indeed, since our <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> decision five of the States' highest courts have found that reasonable inspections are constitutionally permissible and in fact imperative, for the protection of health, safety, and welfare of the millions who inhabit our cities and towns.<sup>[2]</sup></p>
<p>I submit that under the carefully circumscribed requirements of health and safety codes, as well as the facts and circumstances of these particular inspections, <span class="star-pagination">*549</span> there is nothing unreasonable about the ones undertaken here. These inspections meet the Fourth Amendment's test of reasonableness and are entirely consistent with the Amendment's commands and our cases.</p>
<p>There is nothing here that suggests that the inspection was unauthorized, unreasonable, for any improper purpose, or designed as a basis for a criminal prosecution; nor is there any indication of any discriminatory, arbitrary, or capricious action affecting the appellant in either case. Indeed, Camara was admittedly violating the Code by living in quarters prohibited thereby; and See was operating a locked warehousea business establishment subject to inspection.</p>
<p>The majority say, however, that under the present system the occupant has no way of knowing the necessity for the inspection, the limits of the inspector's power, or whether the inspector is himself authorized to perform the search. Each of the ordinances here is supported by findings as to the necessity for inspections of this type and San Francisco specifically bans the conduct in which appellant Camara is admittedly engaged. Furthermore, all of these doubts raised by the Court could be resolved very quickly. Indeed, the inspectors all have identification cards which they show the occupant and the latter could easily resolve the remaining questions by a call to the inspector's superior or, upon demand, receive a written answer thereto. The record here shows these challenges could have been easily interposed. The inspectors called on several occasions, but still no such questions were raised.<sup>[3]</sup> These cases, from the outset, were based on the Fourth Amendment, not on any of the circumstances surrounding the attempted inspection. To say, therefore, <span class="star-pagination">*550</span> that the inspection is left to the discretion of the officer in the field is to reach a conclusion not authorized by this record or the ordinances involved here. The Court says the question is not whether the "inspections may be made, but whether they may be made without a warrant." With due respect, inspections of this type have been made for over a century and a half without warrants and it is a little late to impose a death sentence on such procedures now. In most instances the officer could not secure a warrantsuch as in See's casethereby insulating large and important segments of our cities from inspection for health and safety conditions. It is this situationwhich is even recognized by the Courtthat should give us pause.</p>
<p></p>
<h2>III.</h2>
<p>The great need for health and safety inspection is emphasized by the experience of San Francisco, a metropolitan area known for its cleanliness and safety ever since it suffered earthquake and fire back in 1906. For the fiscal year ending June 30, 1965, over 16,000 dwelling structures were inspected, of which over 5,600 required some type of compliance action in order to meet code requirements. And in 1965-1966 over 62,000 apartments, hotels, and dwellings were inspected with similar results. During the same period the Public Works Department conducted over 52,000 building inspections, over 43,000 electrical ones and over 33,000 plumbing inspections. During the entire year 1965-1966 inspectors were refused entry on less than 10 occasions where the ordinance required the householder to so permit.</p>
<p>In Seattle, the site of No. 180, <i>See</i> v. <i>City of Seattle,</i> fire inspections of commercial and industrial buildings totaled over 85,000 in 1965. In Jacksonville, Florida, over 21,000 fire inspections were carried on in the same year, while in excess of 135,000 health inspections were <span class="star-pagination">*551</span> conducted. In Portland, Oregon, out of 27,000 health and safety inspections over 4,500 violations of regulations were uncovered and the fire marshal in Portland found over 17,000 violations of the fire code in 1965 alone. In Boston over 56,000 code violations were uncovered in 1966 while in Baltimore a somewhat similar situation was reported.</p>
<p>In the larger metropolitan areas such as Los Angeles, over 300,000 inspections (health and fire) revealed over 28,000 hazardous violations. In Chicago during the period November 1965 to December 1966, over 18,000 buildings were found to be rodent infested out of some 46,000 inspections. And in Cleveland the division of housing found over 42,000 violations of its code in 1965; its health inspectors found over 33,000 violations in commercial establishments alone and over 27,000 dwelling code infractions were reported in the same period. And in New York City the problem is even more acute. A grand jury in Brooklyn conducted a housing survey of 15 square blocks in three different areas and found over 12,000 hazardous violations of code restrictions in those areas alone. Prior to this test there were only 567 violations reported in the three areas. The pressing need for inspection is shown by the fact that some 12,000 additional violations were actually present at that very time.</p>
<p>An even more disastrous effect will be suffered in plumbing violations. These are not only more frequent but also the more dangerous to the community. Defective plumbing causes back siphonage of sewage and other household wastes. Chicago's disastrous amoebic dysentery epidemic is an example. Over 100 deaths resulted. Fire code violations also often cause many conflagrations. Indeed, if the fire inspection attempted in <i>District of Columbia</i> v. <i>Little,</i> <span class="citation" data-id="104766"><a href="/opinion/104766/district-of-columbia-v-little/" aria-description="Citation for case: District of Columbia v. Little">339 U. S. 1</a></span> (1950), <span class="star-pagination">*552</span> had been permitted a two-year-old child's death resulting from a fire that gutted the home involved there on August 6, 1949, might well have been prevented.</p>
<p>Inspections also play a vital role in urban redevelopment and slum clearance. Statistics indicate that slums constitute 20% of the residential area of the average American city, still they produce 35% of the fires, 45% of the major crimes, and 50% of the disease. Today's decision will play havoc with the many programs now designed to aid in the improvement of these areas. We should remember the admonition of MR. JUSTICE DOUGLAS in <i>Berman</i> v. <i>Parker,</i> <span class="citation" data-id="105244"><a href="/opinion/105244/berman-v-parker/#32" aria-description="Citation for case: Berman v. Parker">348 U. S. 26, 32</a></span> (1954):</p>
<blockquote>"Miserable and disreputable housing conditions may do more than spread disease and crime and immorality. They may also suffocate the spirit by reducing the people who live there to the status of cattle. They may indeed make living an almost insufferable burden."</blockquote>
<p></p>
<h2>IV.</h2>
<p>The majority propose two answers to this admittedly pressing problem of need for constant inspection of premises for fire, health, and safety infractions of municipal codes. First, they say that there will be few refusals of entry to inspect. Unlike the attitude of householders as to codes requiring entry for inspection, we have few empirical statistics on attitudes where consent must be obtained. It is true that in the required entry-to-inspect situations most occupants welcome the periodic visits of municipal inspectors. In my view this will not be true when consent is necessary. The City of Portland, Oregon, has a voluntary home inspection program. The 1966 record shows that out of 16,171 calls where the occupant was at home, entry was refused in 2,540 casesapproximately one out of six. This is a large percentage and would place an intolerable burden on the inspection service <span class="star-pagination">*553</span> when required to secure warrants. What is more important is that out of the houses inspected 4,515 hazardous conditions were found! Hence, on the same percentage, there would be approximately 840 hazardous situations in the 2,540 in which inspection was refused in Portland.</p>
<p>Human nature being what it is, we must face up to the fact that thousands of inspections are going to be denied. The economics of the situation alone will force this result. Homeowners generally try to minimize maintenance costs and some landlords make needed repairs only when required to do so. Immediate prospects for costly repairs to correct possible defects are going to keep many a door closed to the inspector. It was said by way of dissent in <i>Frank</i> v. <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#384" aria-description="Citation for case: Frank v. Maryland"><i>Maryland, supra,</i> at 384</a></span>, that "[o]ne rebel a year" is not too great a price to pay for the right to privacy. But when voluntary inspection is relied upon this "one rebel" is going to become a general rebellion. That there will be a significant increase in refusals is certain and, as time goes on, that trend may well become a frightening reality. It is submitted that voluntary compliance cannot be depended upon.</p>
<p>The Court then addresses itself to the propriety of warrantless area inspections.<sup>[4]</sup> The basis of "probable cause" for area inspection warrants, the Court says, begins with the Fourth Amendment's reasonableness requirement; in determining whether an inspection is reasonable "the need for the inspection must be weighed in terms of these reasonable goals of code enforcement." It adds that there are "a number of persuasive factors" <span class="star-pagination">*554</span> supporting "the reasonableness of area code-enforcement inspections." It is interesting to note that the factors the Court relies upon are the identical ones my Brother Frankfurter gave for excusing warrants in <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland, supra</a></span></i><i>.</i> They are: long acceptance historically; the great public interest in health and safety; and the impersonal nature of the inspectionsnot for evidence of crimebut for the public welfare. Upon this reasoning, the Court concludes that probable cause exists "if reasonable legislative or administrative standards for conducting an area inspection are satisfied with respect to a particular dwelling." These standards will vary, it says, according to the code program and the condition of the area with reference thereto rather than the condition of a particular dwelling. The majority seem to hold that warrants may be obtained after a refusal of initial entry; I can find no such constitutional distinction or command. These boxcar warrants will be identical as to every dwelling in the area, save the street number itself. I daresay they will be printed up in pads of a thousand or morewith space for the street number to be insertedand issued by magistrates in broadcast fashion as a matter of course.</p>
<p>I ask: Why go through such an exercise, such a pretense? As the same essentials are being followed under the present procedures, I ask: Why the ceremony, the delay, the expense, the abuse of the search warrant? In my view this will not only destroy its integrity but will degrade the magistrate issuing them and soon bring disrepute not only upon the practice but upon the judicial process. It will be very costly to the city in paperwork incident to the issuance of the paper warrants, in loss of time of inspectors and waste of the time of magistrates and will result in more annoyance to the public. It will also be more burdensome to the occupant of the premises to be inspected. Under a search warrant the inspector <span class="star-pagination">*555</span> can enter any time he chooses. Under the existing procedures he can enter only at reasonable times and invariably the convenience of the occupant is considered. I submit that the identical grounds for action elaborated today give more supportboth legal and practicalto the present practice as approved in <i>Frank</i> v. <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland, supra</a></span></i><i>,</i> than they do to this legalistic facade that the Court creates. In the Court's anxiety to limit its own holding as to mass searches it hopes to divert attention from the fact that it destroys the health and safety codes as they apply to individual inspections of specific problems as contrasted to area ones. While the latter are important, the individual inspection is often more so; that was true in <i>District of Columbia</i> v. <i>Little</i> and it may well be in both <i><span class="citation" data-id="8956642"><a href="/opinion/8965309/camara-v-municipal-court-of-the-city-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of the City &amp; County of San...">Camara</a></span></i> and <i>See.</i> Frankly, I cannot understand how the Court can authorize warrants in wholesale fashion in the case of an area inspection, but hold the hand of the inspector when a specific dwelling is hazardous to the health and safety of its neighbors.</p>
<h2>NOTES</h2>
<p>[1]  Conviction and sentence were pursuant to § 8.01.140 of the Fire Code:
</p>
<p>"PENALTY. Anyone violating or failing to comply with any provision of this Title or lawful order of the Fire Chief pursuant hereto shall upon conviction thereof be punishable by a fine not to exceed Three Hundred Dollars ($300.00), or imprisonment in the City Jail for a period not to exceed ninety (90) days, or by both such fine and imprisonment, and each day of violation shall constitute a separate offense."</p>
<p>[2]  "Dwelling" is defined in the Code as "a building occupied exclusively for residential purposes and having not more than two (2) dwelling units." Such dwellings are subject to the substantive provisions of the Code, but the Fire Chief's right to enter such premises is limited to times "when he has reasonable cause to believe a violation of the provisions of this Title exists therein." § 8.01.040. This provision also lacks a warrant procedure.</p>
<p>[3]  See Antitrust Civil Process Act of 1962, <span class="citation no-link">76 Stat. 548</span>, <span class="citation no-link">15 U. S. C. §§ 1311-1314</span>; H. R. Rep. No. 708, 83d Cong., 1st Sess. (1953) (reporting the "factory inspection" amendments to the Federal Food, Drug, and Cosmetic Act, <span class="citation no-link">67 Stat. 476</span>, <span class="citation no-link">21 U. S. C. § 374</span>); Davis, The Administrative Power of Investigation, 56 Yale L. J. 1111; Handler, The Constitutionality of Investigations by the Federal Trade Commission, I &amp; II, 28 Col. L. Rev. 708, 905; Schwartz, Crucial Areas in Administrative Law, <span class="citation no-link">34 Geo. Wash. L. Rev. 401</span>, 425-430; Note, Constitutional Aspects of Federal Tax Investigations, 57 Col. L. Rev. 676.</p>
<p>[4]  In <i>United States</i> v. <i>Cardiff,</i> <span class="citation" data-id="105052"><a href="/opinion/105052/united-states-v-cardiff/" aria-description="Citation for case: United States v. Cardiff">344 U. S. 174</a></span>, this Court held that the Federal Food, Drug, and Cosmetic Act did not compel that consent be given to warrantless inspections of establishments covered by the Act. (As a result, the statute was subsequently amended, see n. 3, <i>supra.</i>) See also <i>Federal Trade Comm'n</i> v. <i>American Tobacco Co.,</i> <span class="citation" data-id="100375"><a href="/opinion/100375/federal-trade-commission-v-american-tobacco-co/" aria-description="Citation for case: Federal Trade Commission v. American Tobacco Co.">264 U. S. 298</a></span>.</p>
<p>[5]  See <i>United States</i> v. <i>Morton Salt Co.,</i> <span class="citation" data-id="104758"><a href="/opinion/104758/united-states-v-morton-salt-co/" aria-description="Citation for case: United States v. Morton Salt Co.">338 U. S. 632</a></span>; <i>Oklahoma Press Pub. Co.</i> v. <i>Walling,</i> <span class="citation" data-id="9419755"><a href="/opinion/104239/oklahoma-press-publishing-co-v-walling/" aria-description="Citation for case: Oklahoma Press Publishing Co. v. Walling">327 U. S. 186</a></span>; <i>United States</i> v. <i>Bausch &amp; Lomb Optical Co.,</i> <span class="citation" data-id="103966"><a href="/opinion/103966/united-states-v-bausch-lomb-optical-co/" aria-description="Citation for case: United States v. Bausch &amp; Lomb Optical Co.">321 U. S. 707</a></span>; <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span>. See generally 1 Davis, Administrative Law §§ 3.05-3.06 (1958).</p>
<p>[6]  We do not decide whether warrants to inspect business premises may be issued only after access is refused; since surprise may often be a crucial aspect of routine inspections of business establishments, the reasonableness of warrants issued in advance of inspection will necessarily vary with the nature of the regulation involved and may differ from standards applicable to private homes.</p>
<p>[7]  <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>, relied upon by the Supreme Court of Washington, held only that government officials could demand access to business premises and, upon obtaining consent to search, could seize gasoline ration coupons issued by the Government and illegally possessed by the petitioner. <i><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">Davis</a></span></i> thus involved the reasonableness of a particular search of business premises but did not involve a search warrant issue.</p>
<p>[*]  [This opinion applies also to No. 92, <i>Camara</i> v. <i>Municipal Court of the City and County of San Francisco, ante,</i> p. 523.]</p>
<p>[1]  Under the probable-cause standard laid down by the Court, it appears to me that the issuance of warrants could more appropriately be the function of the agency involved than that of the magistrate. This would also relieve magistrates of an intolerable burden. It is therefore unfortunate that the Court fails to pass on the validity of the use of administrative warrants.</p>
<p>[2]  <i>DePass</i> v. <i>City of Spartanburg,</i> 234 S. C. 198, <span class="citation" data-id="1329358"><a href="/opinion/1329358/depass-v-city-of-spartanburg/" aria-description="Citation for case: DePass v. CITY OF SPARTANBURG">107 S. E. 2d 350</a></span> (1959); <i>City of St. Louis</i> v. <i>Evans,</i> <span class="citation" data-id="2435050"><a href="/opinion/2435050/city-of-st-louis-v-evans/" aria-description="Citation for case: City of St. Louis v. Evans">337 S. W. 2d 948</a></span> (Mo. 1960); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="2190984"><a href="/opinion/2190984/camara-v-municipal-court/" aria-description="Citation for case: Camara v. Municipal Court">237 Cal. App. 2d 128</a></span>, <span class="citation" data-id="2190984"><a href="/opinion/2190984/camara-v-municipal-court/" aria-description="Citation for case: Camara v. Municipal Court">46 Cal. Rptr. 585</a></span> (1965), pet. for hearing in Cal. Sup. Ct. den. (Civ. No. 22128) Nov. 19, 1965; <i>Commonwealth</i> v. <i>Hadley,</i> <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">351 Mass. 439</a></span>, <span class="citation" data-id="2008391"><a href="/opinion/2008391/commonwealth-v-hadley/" aria-description="Citation for case: Commonwealth v. Hadley">222 N. E. 2d 681</a></span>, appeal docketed, Jan. 5, 1967, No. 1179, Misc., O. T. 1966; <i>City of Seattle</i> v. <i>See,</i> <span class="citation" data-id="1421045"><a href="/opinion/1421045/city-of-seattle-v-see/" aria-description="Citation for case: City of Seattle v. See">67 Wash. 2d 475</a></span>, <span class="citation" data-id="1421045"><a href="/opinion/1421045/city-of-seattle-v-see/" aria-description="Citation for case: City of Seattle v. See">408 P. 2d 262</a></span> (1965).</p>
<p>[3]  Indeed, appellant Camara was summoned to the office of the district attorneybut failed to appearwhere he certainly could have raised these questions.</p>
<p>[4]  It is interesting to note that in each of the cases here the authorities were making periodic area inspections when the refusals to allow entry occurred. Under the holding of the Court today, "probable cause" would therefore be present in each case and a "paper warrant" would issue as a matter of course. This but emphasizes the absurdity of the holding.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Segura v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Segura v. United States"
type: case
citation: "468 U.S. 796 (1984)"
parallel_cite: "104 S. Ct. 3380; 82 L. Ed. 2d 599; 52 U.S.L.W. 5128"
neutral_cite: 1984 U.S. LEXIS 150
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-07-05
docket: 82-5298
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-07-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Segura v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111259/segura-v-united-states/"
  cluster_id: 111259
  opinion_id: 9429757
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Key — Anchor"
related: ["[[Murray v. United States]]", "[[Nix v. Williams]]", "[[Illinois v. McArthur]]", "[[Wong Sun v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "independent-source", "exclusionary-rule", "securing-premises"]
holding: "Evidence seized under a valid warrant is admissible even after an earlier illegal entry, where the warrant was supported wholly by…"
lake:
  record_id: Segura v. United States
  status: verified
  projected_at: 2026-07-06
---

# Segura v. United States

*468 U.S. 796 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DEA agents, suspecting Segura and Colon of cocaine trafficking, arrested Segura in his apartment building, entered the apartment without a warrant, and secured it from within for roughly 19 hours until a search warrant arrived. The warrant rested entirely on information the agents knew before the entry. Evidence found during the later warranted search was challenged as fruit of the illegal entry.

## Issue
Whether evidence discovered during a later search under a valid warrant—issued on information wholly independent of an earlier illegal entry—must be suppressed as fruit of that entry.

## Rule
Evidence obtained under a genuinely independent warrant is not tainted by a prior illegal entry. "Whether the initial entry was illegal or not is irrelevant to the admissibility of the challenged evidence because there was an independent source for the warrant under which that evidence was seized." — 468 U.S. at 814. ^pin-814

Resting on that independent-source ground, the Court did not decide whether securing the premises was itself reasonable.

## Application
None of the information supporting the warrant derived from the entry; it came from sources wholly unconnected with the entry and known to the agents well before it. The warranted search the following day was therefore a genuinely [[Inevitable Discovery and Independent Source|independent source]], and the drugs, cash, and records seized under the warrant were admissible despite the assumed-illegal initial entry and 19-hour occupation.

## Conclusion
The evidence seized under the independent warrant was admissible and should not have been suppressed; the judgment below was reversed in relevant part.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The independent-source doctrine was elaborated four years later in [[Murray v. United States]]; *Segura* sits alongside [[Nix v. Williams]] ([[Inevitable Discovery and Independent Source|inevitable discovery]]) and [[Illinois v. McArthur]] (securing premises pending a warrant), and applies the "fruit"/taint framework of [[Wong Sun v. United States]].

## Appears on
- [[Securing the Scene]] — *Key — Anchor*

## Sources
- *Segura v. United States*, 468 U.S. 796 (1984) — https://www.courtlistener.com/opinion/111259/segura-v-united-states/ — pinpoint: 814.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "483226c241012da0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Segura v. United States"}, "payload": {"all": [{"cite": "468 U.S. 796", "page": "796", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "468"}, {"cite": "104 S. Ct. 3380", "page": "3380", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "82 L. Ed. 2d 599", "page": "599", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "82"}, {"cite": "1984 U.S. LEXIS 150", "page": "150", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 5128", "page": "5128", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "468 U.S. 796", "official": {"cite": "468 U.S. 796", "page": "796", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "468"}, "official_selection_present": true, "record_id": "Segura v. United States"}}
{"assertion_id": "f9a49fbf35a7c462", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-814", "record_id": "Segura v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-814", "pinpoint_status": "slip-only", "quote": "--- # Segura v. United States *468 U.S. 796 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DEA agents, suspecting Segura and Colon of cocaine trafficking, arrested Segura in his apartment building, entered the apartment without a warrant, and secured it from within for roughly 19 hours until a search warrant arrived. The warrant rested entirely on information the agents knew before the entry. Evidence found during the later warranted search was challenged as fruit of the illegal entry. ## Issue Whether evidence discovered during a later search under a valid warrant—issued on information wholly independent of an earlier illegal entry—must be suppressed as fruit of that entry. ## Rule Evidence obtained under a genuinely independent warrant is not tainted by a prior illegal entry.", "quote_fidelity": "mismatch", "record_id": "Segura v. United States", "star_marker": null}}
{"assertion_id": "12f5042f676e2c14", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Segura v. United States"}, "payload": {"as_of_content": "1984-07-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Segura v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Segura v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Segura v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Segura v. United States",
    "case_name_short": "Segura",
    "case_name_full": "SEGURA Et Al. v. UNITED STATES",
    "input_case_name": "Segura v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-07-05",
    "year": 1984,
    "docket": "82-5298",
    "cluster_id": 111259,
    "lead_opinion_id": 9429757,
    "sibling_ids": [
      111259,
      9429757,
      9429758
    ],
    "absolute_url": "/opinion/111259/segura-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "468 U.S. 796",
      "volume": "468",
      "reporter": "U.S.",
      "page": "796",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 3380",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3380",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 599",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5128",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5128",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 150",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "150",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "468 U.S. 796",
        "volume": "468",
        "reporter": "U.S.",
        "page": "796",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 3380",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "3380",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 L. Ed. 2d 599",
        "volume": "82",
        "reporter": "L. Ed. 2d",
        "page": "599",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 150",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "150",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 5128",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "5128",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "468 U.S. 796",
    "official_selection": {
      "court_class": "scotus",
      "selected": "468 U.S. 796",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-814",
      "page": null,
      "quote": "--- # Segura v. United States *468 U.S. 796 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DEA agents, suspecting Segura and Colon of cocaine trafficking, arrested Segura in his apartment building, entered the apartment without a warrant, and secured it from within for roughly 19 hours until a search warrant arrived. The warrant rested entirely on information the agents knew before the entry. Evidence found during the later warranted search was challenged as fruit of the illegal entry. ## Issue Whether evidence discovered during a later search under a valid warrant\u2014issued on information wholly independent of an earlier illegal entry\u2014must be suppressed as fruit of that entry. ## Rule Evidence obtained under a genuinely independent warrant is not tainted by a prior illegal entry.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-07-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Segura v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 10018712,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Strudwick",
          "cluster_id": 5293509,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789821,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
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
        "journal_ref": "Segura v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
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
        "journal_ref": "Segura v. United States:lane1_negative"
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
        "journal_ref": "Segura v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane1_negative"
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
        "journal_ref": "Segura v. United States:lane1_negative"
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
        "journal_ref": "Segura v. United States:lane2_top_cited"
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
        "journal_ref": "Segura v. United States:lane2_top_cited"
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
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Garrison",
          "cluster_id": 111823,
          "cite": [
            "94 L. Ed. 2d 72",
            "107 S. Ct. 1013",
            "480 U.S. 79",
            "1987 U.S. LEXIS 559",
            "55 U.S.L.W. 4190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Arkansas",
          "cluster_id": 117936,
          "cite": [
            "131 L. Ed. 2d 976",
            "115 S. Ct. 1914",
            "514 U.S. 927",
            "1995 U.S. LEXIS 3464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania Bd. of Probation and Parole v. Scott",
          "cluster_id": 118235,
          "cite": [
            "141 L. Ed. 2d 344",
            "118 S. Ct. 2014",
            "524 U.S. 357",
            "1998 U.S. LEXIS 4037"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scroggins",
          "cluster_id": 71470,
          "cite": [
            "599 F.3d 433",
            "2010 U.S. App. LEXIS 4551",
            "2010 WL 724688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Geisler",
          "cluster_id": 7894925,
          "cite": [
            "222 Conn. 672",
            "610 A.2d 1225",
            "61 U.S.L.W. 2093",
            "1992 Conn. LEXIS 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
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
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McQuarters v. State",
          "cluster_id": 1772991,
          "cite": [
            "58 S.W.3d 250",
            "2001 Tex. App. LEXIS 6457",
            "2001 WL 1098006"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
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
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Henry Morgan",
          "cluster_id": 441786,
          "cite": [
            "743 F.2d 1158",
            "1984 U.S. App. LEXIS 18632"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olivarez v. State",
          "cluster_id": 1560637,
          "cite": [
            "171 S.W.3d 283",
            "2005 WL 1385355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re United States",
          "cluster_id": 441742,
          "cite": [
            "743 F.2d 827",
            "1984 U.S. App. LEXIS 18020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Woodard, A., Aplt.",
          "cluster_id": 3159995,
          "cite": [
            "129 A.3d 480",
            "634 Pa. 162",
            "2015 Pa. LEXIS 2786",
            "2015 WL 7767271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2087727,
          "cite": [
            "745 A.2d 856",
            "1999 Del. LEXIS 445",
            "1999 WL 1259008"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 1216654,
          "cite": [
            "358 S.E.2d 1",
            "320 N.C. 179",
            "1987 N.C. LEXIS 2180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dortch",
          "cluster_id": 7079686,
          "cite": [
            "199 F.3d 193",
            "1999 WL 1251873"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Terzado-Madruga",
          "cluster_id": 537704,
          "cite": [
            "897 F.2d 1099",
            "1990 WL 27249"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gulbrandson",
          "cluster_id": 1127545,
          "cite": [
            "906 P.2d 579",
            "184 Ariz. 46",
            "202 Ariz. Adv. Rep. 46",
            "1995 Ariz. LEXIS 105"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. Nevada",
          "cluster_id": 117833,
          "cite": [
            "128 L. Ed. 2d 1",
            "114 S. Ct. 1280",
            "511 U.S. 79",
            "1994 U.S. LEXIS 2655"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "110OAG40",
          "cluster_id": 10638768,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane3_recency"
      },
      {
        "citing_case": {
          "name": "Maryland Attorney General Opinion 110OAG40",
          "cluster_id": 10848272,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Segura v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111259 OR 9429757 OR 9429758) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDEwMjIwODAwMDAwJnM9MjczMTIyMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111259+OR+9429757+OR+9429758%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(111259 OR 9429757 OR 9429758)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMmcz03OTc1NTMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111259+OR+9429757+OR+9429758%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111259 OR 9429757 OR 9429758)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 2,
        "triage_snippet_classified": 47
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111259 OR 9429757 OR 9429758)",
    "indexed_citing_opinions": 1022,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111259,
        "count": 854,
        "count_source": "search"
      },
      {
        "opinion_id": 9429757,
        "count": 188,
        "count_source": "search"
      },
      {
        "opinion_id": 9429758,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1571,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/segura-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDIwMjQmcz0xMDI4NjMwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111259+OR+9429757+OR+9429758%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111259,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 106172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 108995,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 321384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 377806,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 383555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 384447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 386073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 396523,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 402452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 414500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111259,
        "cited_id": 418054,
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
    "date_created": "2026-07-05T19:12:03Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:17:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:12:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Segura v. United States

```
<opinion type="majority">
<author id="pAhi">Chief Justice Burger</author>
<p id="pATFq">delivered the opinion of the Court. <footnotemark>†</footnotemark></p>
<p id="b839-11">We granted certiorari to decide whether, because of an earlier illegal entry, the Fourth Amendment requires suppression of evidence seized later from a private residence <page-number citation-index="1" label="798">*798</page-number>pursuant to a valid search warrant which was issued on information obtained by the police before the entry into the residence.</p>
<p id="b840-5">I</p>
<p id="b840-6">Resolution of this issue requires us to consider two separate questions: first, whether the entry and internal securing of the premises constituted an impermissible seizure of all the contents of the apartment, seen and unseen; second, whether the evidence first discovered during the search of the apartment pursuant to a valid warrant issued the day after the entry should have been suppressed as “fruit” of the illegal entry. Our disposition of both questions is carefully limited.</p>
<p id="b840-7">The Court of Appeals affirmed the District Court’s holding that there were no exigent circumstances to justify the war-rantless entry into petitioners’ apartment. That issue is not before us, and we have no reason to question the courts’ holding that that <em>search </em>was illegal. The ensuing interference with petitioners’ possessory interests in their apartment, however, is another matter. On this first question, we conclude that, assuming that there was a <em>seizure </em>of all the contents of the petitioners’ apartment when agents secured the premises from within, that seizure did not violate the Fourth Amendment. Specifically, we hold that where officers, having probable cause, enter premises, and with probable cause, arrest the occupants who have legitimate pos-sessory interests in its contents and take them into custody and, for no more than the period here involved, secure the premises from within to preserve the status quo while others, in good faith, are in the process of obtaining a warrant, they do not violate the Fourth Amendment’s proscription against unreasonable seizures.<footnotemark>1</footnotemark></p>
<p id="b841-4"><page-number citation-index="1" label="799">*799</page-number>The illegality of the initial entry, as we will show, has no bearing on the second question. The resolution of this second question requires that we determine whether the initial entry tainted the discovery of the evidence now challenged. On this issue, we hold that the evidence discovered during the subsequent search of the apartment the following day pursuant to the valid search warrant issued wholly on information known to the officers before the entry into the apartment need not have been suppressed as “fruit” of the illegal entry because the warrant and the information on which it was based were unrelated to the entry and therefore constituted an independent source for the evidence under <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).</p>
<p id="b841-5">II</p>
<p id="b841-6">In January 1981, the New York Drug Enforcement Task Force received information indicating that petitioners Andres Segura and Luz Marina Colon probably were trafficking in cocaine from their New York apartment. Acting on this information, Task Force agents maintained continuing surveillance over petitioners until their arrest on February 12, 1981. On February 9, agents observed a meeting between Segura and Enrique Rivudalla-Vidal, during which, as it later developed, the two discussed the possible sale of cocaine by Segura to Rivudalla-Vidal. Three days later, February 12, Segura telephoned Rivudalla-Vidal and agreed to provide him with cocaine. The two agreed that the delivery would be made at 5 p. m. that day at a designated fast-food restaurant in Queens, N. Y. Rivudalla-Vidal and one Esther Parra, arrived at the restaurant at 5 p. m., as agreed. While Segura and Rivudalla-Vidal visited inside the restaurant, agents observed Colon deliver a bulky package to Parra, who had remained in Rivudalla-Vidal’s car in the restaurant parking lot. A short time after the delivery of the package, Rivudalla-Vidal and Parra left the restaurant and <page-number citation-index="1" label="800">*800</page-number>proceeded to their apartment. Task Force agents followed. The agents stopped the couple as they were about to enter Rivudalla-Vidal’s apartment. Parra was found to possess cocaine; both Rivudalla-Vidal and Parra were immediately arrested.</p>
<p id="b842-5">After Rivudalla-Vidal and Parra were advised of their constitutional rights, Rivudalla-Vidal agreed to cooperate with the agents. He admitted that he had purchased the cocaine from Segura and he confirmed that Colon had made the delivery at the fast-food restaurant earlier that day, as the agents had observed. Rivudalla-Vidal informed the agents that Segura was to call him at approximately 10 o’clock that evening to learn if Rivudalla-Vidal had sold the cocaine, in which case Segura was to deliver additional cocaine.</p>
<p id="b842-6">Between 6:30 and 7 p. m., the same day, Task Force agents sought and received authorization from an Assistant United States Attorney to arrest Segura and Colon. The agents were advised by the Assistant United States Attorney that because of the lateness of the hour, a search warrant for petitioners’ apartment probably could not be obtained until the following day, but that the agents should proceed to secure the premises to prevent the destruction of evidence.</p>
<p id="b842-7">At about 7:80 p. m., the agents arrived at petitioners’ apartment and established external surveillance. At 11:15 p. m., Segura, alone, entered the lobby of the apartment building where he was immediately arrested by agents. He first claimed he did not reside in the building. The agents took him to his third floor apartment, and when they knocked on the apartment door, a woman later identified as Colon appeared; the agents then entered with Segura, without requesting or receiving permission. There were three persons in the living room of the apartment in addition to Colon. Those present were informed by the agents that Segura was under arrest and that a search warrant for the apartment was being obtained.</p>
<p id="b842-8">Following this brief exchange in the living room, the agents conducted a limited security check of the apartment to <page-number citation-index="1" label="801">*801</page-number>ensure that no one else was there who might pose a threat to their safety or destroy evidence. In the process, the agents observed, in a bedroom in plain view, a triple-beam scale, jars of lactose, and numerous small cellophane bags, all accouterments of drug trafficking. None of these items was disturbed by the agents. After this limited security check, Colon was arrested. In the search incident to her arrest, agents found in her purse a loaded revolver and more than $2,000 in cash. Colon, Segura, and the other occupants of the apartment were taken to Drug Enforcement Administration headquarters.</p>
<p id="b843-5">Two Task Force agents remained in petitioners’ apartment awaiting the warrant. Because of what is characterized as “administrative delay” the warrant application was not presented to the Magistrate until 5 p. m. the next day. The warrant was issued and the search was performed at approximately 6 p. m., some 19 hours after the agents’ initial entry into the apartment. In the search pursuant to the warrant, agents discovered almost three pounds of cocaine, 18 rounds of .38-caliber ammunition fitting the revolver agents had found in Colon’s possession at the time of her arrest, more than $50,000 cash, and records of narcotics transactions. Agents seized these items, together with those observed during the security check the previous night.</p>
<p id="b843-6">Before trial in the United States District Court in the Eastern District of New York, petitioners moved to suppress all of the evidence seized from the apartment — the items discovered in plain view during the initial security check and those not in plain view first discovered during the subsequent warrant search.<footnotemark>2</footnotemark> After a full evidentiary hearing, the <page-number citation-index="1" label="802">*802</page-number>District Court granted petitioners’ motion. The court ruled that there were no exigent circumstances justifying the initial entry into the apartment. Accordingly, it held that the entry, the arrest of Colon and search incident to her arrest, and the effective seizure of the drug paraphernalia in plain view were illegal. The District Court ordered this evidence suppressed as “fruits” of illegal searches.</p>
<p id="b844-5">The District Court held that the warrant later issued was supported by information sufficient to establish probable cause; however, it read <em>United States </em>v. <em>Griffin, </em><span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">502 F. 2d 959</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1050/">419 U. S. 1050</a></span> (1974), as requiring suppression of the evidence seized under the valid warrant.<footnotemark>3</footnotemark> The District Court reasoned that this evidence would not necessarily have been discovered because, absent the illegal entry and “occupation” of the apartment, Colon might have arranged to have the drugs removed or destroyed, in which event they would not have been in the apartment when the warrant search was made. Under this analysis, the District Court held that even the drugs seized under the valid warrant were “fruit of the poisonous tree.”</p>
<p id="b844-6">On an appeal limited to the admissibility of the incriminating evidence, the Court of Appeals affirmed in part and reversed in part. <span class="citation" data-id="396523"><a href="/opinion/396523/united-states-v-andres-segura-and-luz-marina-colon/" aria-description="Citation for case: United States v. Andres Segura and Luz Marina Colon">663 F. 2d 411</a></span> (1981). It affirmed the District Court holding that the initial warrantless entry was not justified by exigent circumstances and that the evidence discovered in plain view during the initial entry must be suppressed.<footnotemark>4</footnotemark> The Court of Appeals rejected the argument <page-number citation-index="1" label="803">*803</page-number>advanced by the United States that the evidence in plain view should not be excluded because it was not actually “seized” until after the search warrant was secured.</p>
<p id="b845-5">Relying upon its holding in <em>United States </em>v. Agapito, <span class="citation" data-id="377806"><a href="/opinion/377806/united-states-v-calixto-agapito-martha-calderon-and-horacio-rueda/" aria-description="Citation for case: United States v. Calixto Agapito, Martha Calderon and...">620 F. 2d 324</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/834/">449 U. S. 834</a></span> (1980),<footnotemark>5</footnotemark> the Court of Appeals reversed the District Court’s holding requiring suppression of the evidence seized under the valid warrant executed on the day following the initial entry. The Court of Appeals described as “prudentially unsound” the District Court’s decision to suppress that evidence simply because it could have been destroyed had the agents not entered.</p>
<p id="b845-6">Petitioners were convicted of conspiring to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. § 846</span>, and of distributing and possessing with intent to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. § 841</span>(a)(1). On the subsequent review of these convictions, the Second Circuit affirmed, <span class="citation multiple-matches"><a href="/c/F.%202d/697/300/">697 F. 2d 300</a></span> (1982), rejecting claims by petitioners that the search warrant was procured through material misrepresentations and that the evidence at trial was insufficient as a matter of law to support <page-number citation-index="1" label="804">*804</page-number>their convictions. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./459/1200/">459 U. S. 1200</a></span> (1983), and we affirm.</p>
<p id="b846-5">Ill</p>
<p id="b846-6">At the outset, it is important to focus on the narrow and precise question now before us. As we have noted, the Court of Appeals agreed with the District Court that the initial warrantless entry and the limited security search were not justified by exigent circumstances and were therefore illegal. No review of that aspect of the case was sought by the Government and no issue concerning items observed during the initial entry is before the Court. The only issue here is whether drugs and the other items not observed during the initial entry and first discovered by the agents the day after the entry, under an admittedly valid search warrant, should have been suppressed.</p>
<p id="b846-7">The suppression or exclusionary rule is a judicially prescribed remedial measure and as “with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). Under this Court’s holdings, the exclusionary rule reaches not only primary evidence obtained as a direct result of an illegal search or seizure, <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), but also evidence later discovered and found to be derivative of an illegality or “fruit of the poisonous tree.” <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939). It “extends as well to the indirect as the direct products” of unconstitutional conduct. <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 484</a></span> (1963).</p>
<p id="b846-8">Evidence obtained as a direct result of an unconstitutional search or seizure is plainly subject to exclusion. The question to be resolved when it is claimed that evidence subsequently obtained is “tainted” or is “fruit” of a prior illegality is whether the challenged evidence was</p>
<blockquote id="b846-9">“ ‘come at by exploitation of [the initial] illegality or instead by means <em>sufficiently distinguishable </em>to be purged <page-number citation-index="1" label="805">*805</page-number>of the primary taint.’” <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States"><em>Id., </em>at 488</a></span> (citation omitted; emphasis added).</blockquote>
<p id="ApN">It has been well established for more than 60 years that evidence is not to be excluded if the connection between the illegal police conduct and the discovery and seizure of the evidence is “so attenuated as to dissipate the taint,” <em>Nardone </em>v. <em>United States, supra, </em>at 341. It is not to be excluded, for example, if police had an “independent source” for discovery of the evidence:</p>
<blockquote id="AVP">“The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all. Of course this does not mean that the facts thus obtained become sacred and inaccessible. <em>If knowledge of them is gained from an independent source they may be proved like any </em>others.” <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S., at 392</a></span> (emphasis added).</blockquote>
<p id="A47t">In short, it is clear from our prior holdings that “the exclusionary rule has no application [where] the Government learned of the evidence ‘from an independent source.’” <em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span> </em>at 487 (quoting <em>Silverthorne Lumber Co., supra, </em>at 392); see also <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/" aria-description="Citation for case: United States v. Crews">445 U. S. 463</a></span> (1980); <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#242" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 242</a></span> (1967); <em>Costello </em>v. <em>United States, </em><span class="citation" data-id="9422121"><a href="/opinion/106172/costello-v-united-states/#278" aria-description="Citation for case: Costello v. United States">365 U. S. 265, 278-280</a></span> (1961).</p>
<p id="Aqqj"><em>&gt; </em>I — I</p>
<p id="A2W">Petitioners argue that all of the contents of the apartment, seen and not seen, including the evidence now in question, were “seized” when the agents entered and remained on the premises while the lawful occupants were away from the apartment in police custody. The essence of this argument is that because the contents were then under the control of the agents and no one would have been permitted to remove the incriminating evidence from the premises or destroy it, a <page-number citation-index="1" label="806">*806</page-number>“seizure” took place. Plainly, this argument is advanced to avoid the <em>Silverthorne </em>“independent source” exception. If all the contents of the apartment were “seized” at the time of the illegal entry and securing, presumably the evidence now challenged would be suppressible as primary evidence obtained as a direct result of that entry.</p>
<p id="b848-5">We need not decide whether, when the agents entered the apartment and secured the premises, they effected a seizure of the cocaine, the cash, the ammunition, and the narcotics records within the meaning of the Fourth Amendment. By its terms, the Fourth Amendment forbids only “unreasonable” searches and seizures. Assuming, arguendo, that the agents seized the entire apartment and its contents, as petitioners suggest, the seizure was not unreasonable under the totality of the circumstances.</p>
<p id="b848-6">Different interests are implicated by a seizure than by a search. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span>, and n. 5, 122-126 (1984); <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 747-748</a></span> (Stevens, J., concurring in judgment); <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 13-14, n. 8</a></span> (1977); <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51-52</a></span> (1970). A seizure affects only the person’s possessory interests; a search affects a person’s privacy interests. <em>United States </em>v. <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen"><em>Jacobsen, supra, </em>at 113</a></span>, and n. 5; <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 13-14, n. 8</a></span>; see generally <em>Texas </em>v. <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown"><em>Brown, supra, </em>at 747-751</a></span> (Stevens, J., concurring in judgment). Recognizing the generally less intrusive nature of a seizure, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 13-14, n. 8</a></span>; <em>Chambers </em>v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><em>Maroney, supra, </em>at 51</a></span>, the Court has frequently approved warrantless seizures of property, on the basis of probable cause, for the time necessary to secure a warrant, where a warrantless search was either held to be or likely would have been held impermissible. <em>Chambers </em>v. <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra;</a></span> United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra;</a></span> Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979).<footnotemark>6</footnotemark></p>
<p id="b849-4"><page-number citation-index="1" label="807">*807</page-number>We focused on the issue notably in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>, </em>holding that it was reasonable to seize and impound an automobile, on the basis of probable cause, for “whatever period is necessary to obtain a warrant for the search.” <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S., at 51</a></span> (footnote omitted). We acknowledged in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>that following the car until a warrant could be obtained was an alternative to impoundment, albeit an impractical one. But we allowed the seizure nonetheless because otherwise the occupants of the car could have removed the “instruments or fruits of crime” before the search. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><em>Id., </em>at 51, n. 9</a></span>. The Court allowed the warrantless seizure to protect the evidence from destruction even though there was no immediate fear that the evidence was in the process of being destroyed or otherwise lost. The <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>Court declared:</p>
<blockquote id="b849-5">“For constitutional purposes, we see no difference between on the one hand seizing and holding the car before presenting the probable cause issue to a magistrate and on the other hand carrying out an immediate search without a warrant. <em>Given probable cause to search, </em><page-number citation-index="1" label="808">*808</page-number><em>either course is reasonable under the Fourth Amendment.” Id., </em>at 52 (emphasis added)</blockquote>
<p id="b850-5">In <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>, </em>we held that the warrantless <em>search </em>of the footloeker after it had been seized and was in a secure area of the Federal Building violated the Fourth Amendment’s proscription against unreasonable searches, but neither the respondents nor the Court questioned the validity of the initial warrantless <em>seizure </em>of the footloeker on the basis of probable cause. The seizure of Chadwick’s footloeker clearly interfered with his use and possession of the footloeker — his possessory interest — but we held that this did not “diminish [his] legitimate expectation that the footlocker’s <em>contents </em>would remain private.” <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13-14, n. 8</a></span> (emphasis added). And again, in <em>Arkansas </em>v. <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders, supra,</a></span> </em>we held that absent exigent circumstances a warrant was required to search luggage seized from an automobile which was already in the possession and control of police at the time of the search. However, we expressly noted that the police acted not only “properly,” but “commendably” in seizing the suitcase without a warrant on the basis of probable cause to believe that it contained drugs. <span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/#761" aria-description="Citation for case: Arkansas v. Sanders">442 U. S., at 761</a></span>. The taxi into which the suitcase had been placed was about to drive away. However, just as there was no immediate threat of loss or destruction of evidence in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>— since officers could have followed the car until a warrant issued — so too in <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span> </em>officers could have followed the taxicab. Indeed, there arguably was even less fear of immediate loss of the evidence in <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span> </em>because the suitcase at issue had been placed in the vehicle’s trunk, thus rendering immediate access unlikely before police could act.</p>
<p id="b850-6">Underlying these decisions is a belief that society’s interest in the discovery and protection of incriminating evidence from removal or destruction can supersede, at least for a limited period, a person’s possessory interest in property, provided that there is probable cause to believe that that property is associated with criminal activity. See <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983).</p>
<p id="b851-4"><page-number citation-index="1" label="809">*809</page-number>The Court has not had occasion to consider whether, when officers have probable cause to believe that evidence of criminal activity is on the premises, the temporary securing of a dwelling to prevent the removal or destruction of evidence violates the Fourth Amendment. However, in two cases we have suggested that securing of premises under these circumstances does not violate the Fourth Amendment, at least when undertaken to preserve the status quo while a search warrant is being sought. In <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we noted with approval that, to preserve evidence, a police guard had been stationed at the entrance to an apartment in which a homicide had been committed, even though “[t]here was no indication that evidence would be lost, destroyed, or removed during the time required to obtain a search warrant.” <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona"><em>Id., </em>at 394</a></span>. Similarly, in <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980), although officers secured, from within, the home of a person for whom they had an arrest warrant, and detained all occupants while other officers were obtaining a search warrant, the Court did not question the admissibility of evidence discovered pursuant to the warrant later issued.<footnotemark>7</footnotemark></p>
<p id="b852-4"><page-number citation-index="1" label="810">*810</page-number>We see no reason, as <em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span> </em>and <em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">Rawlings</a></span> </em>would suggest, why the same principle applied in <em>Chambers, Chadwick, </em>and <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders</a></span>, </em>should not apply where a dwelling is involved. The sanctity of the home is not to be disputed. But the home is sacred in Fourth Amendment terms not primarily because of the occupants' <em>possessory </em>interests in the premises, but because of their <em>privacy </em>interests in the activities that take place within. “[T]he Fourth Amendment protects people, not places.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967); see also <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#615" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 615</a></span> (1980) (White, J., dissenting).</p>
<p id="b852-5">As we have noted, however, a seizure affects only pos-sessory interests, not privacy interests. Therefore, the heightened protection we accord privacy interests is simply not implicated where a <em>seizure </em>of premises, not a search, is at issue. We hold, therefore, that securing a dwelling, on the basis of probable cause, to prevent the destruction or removal of evidence while a search warrant is being sought is not itself an unreasonable seizure of either the dwelling or its contents. We reaffirm at the same time, however, that, absent exigent circumstances, a warrantless search — such as that invalidated in <em>Vale </em>v. <em>Louisiana, </em><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#33" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 33-34</a></span> (1970) — is illegal.</p>
<p id="b852-6">Here, the agents had abundant probable cause in advance of their entry to believe that there was a criminal drug operation being carried on in petitioners' apartment; indeed petitioners do not dispute the probable-cause determination. The agents had maintained surveillance over petitioners for weeks, and had observed petitioners leave the apartment to <page-number citation-index="1" label="811">*811</page-number>make sales of cocaine. Wholly apart from observations made during that extended surveillance, Rivudalla-Vidal had told agents after his arrest on February 13, that petitioners had supplied him with cocaine earlier that day, that he had not purchased all of the cocaine offered by Segura, and that Segura probably had more cocaine in the apartment. On the basis of this information, a Magistrate duly issued a search warrant, the validity of which was upheld by both the District Court and the Court of Appeals, and which is not before us now.</p>
<p id="b853-5">In this case, the agents entered and secured the apartment from within. Arguably, the wiser course would have been to depart immediately and secure the premises from the outside by a “stakeout” once the security check revealed that no one other than those taken into custody were in the apartment. But the method actually employed does not require a different result under the Fourth Amendment, insofar as the <em>seizure </em>is concerned. As the Court of Appeals held, absent exigent' circumstances, the entry may have constituted an illegal <em>search, </em>or interference with petitioners’ privacy interests, requiring suppression of all evidence observed during the entry. Securing of the premises from within, however, was no more an interference with the petitioners’ possessory interests in the contents of the apartment than a perimeter “stakeout.” In other words, the initial entry — legal or not— does not affect the reasonableness of the seizure. Under either method — entry and securing from within or a perimeter stakeout — agents control the apartment pending arrival of the warrant; both an internal securing and a perimeter stakeout interfere to the same extent with the possessory interests of the owners.</p>
<p id="b853-6">Petitioners argue that we heighten the possibility of illegal entries by a holding that the illegal entry and securing of the premises from the inside do not themselves render the <em>seizure </em>any more unreasonable than had the agents staked out the apartment from the outside. We disagree. In the <page-number citation-index="1" label="812">*812</page-number>first place, an entry in the absence of exigent circumstances is illegal. We are unwilling to believe that officers will routinely and purposely violate the law as a matter of course. Second, as a practical matter, officers who have probable cause and who are in the process of obtaining a warrant have no reason to enter the premises before the warrant issues, absent exigent circumstances which, of course, would justify the entry. <em>United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span> (1976); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948). Third, officers who enter illegally will recognize that whatever evidence they discover as a direct result of the entry may be suppressed, as it was by the Court of Appeals in this case. Finally, if officers enter without exigent circumstances to justify the entry, they expose themselves to potential civil liability under <span class="citation no-link">42 U. S. C. § 1983</span>. <em>Bivens </em>v. <em>Six Unknown Federal Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).</p>
<p id="b854-5">Of course, a seizure reasonable at its inception because based upon probable cause may become unreasonable as a result of its duration or for other reasons. Cf. <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983). Here, because of the delay in securing the warrant, the occupation of the apartment continued throughout the night and into the next day. Such delay in securing a warrant in a large metropolitan center unfortunately is not uncommon; this is not, in itself, evidence of bad faith. And there is no suggestion that the officers, in bad faith, purposely delayed obtaining the warrant. The asserted explanation is that the officers focused first on the task of processing those whom they had arrested before turning to the task of securing the warrant. It is not unreasonable for officers to believe that the former should take priority, given, as was the case here, that the proprietors of the apartment were in the custody of the officers throughout the period in question.</p>
<p id="b854-6">There is no evidence that the agents in any way exploited their presence in the apartment; they simply awaited issuance of the warrant. Moreover, more than half of the 19-<page-number citation-index="1" label="813">*813</page-number>hour delay was between 10 p. m. and 10 a. m. the following day, when it is reasonable to assume that judicial officers are not as readily available for consideration of warrant requests. Finally, and most important, we observed in <em>United States </em>v. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#705" aria-description="Citation for case: United States v. Place"><em>Place, supra, </em>at 705</a></span>, that</p>
<blockquote id="b855-5">“[t]he intrusion on possessory interests occasioned by a seizure . . . can vary both in its nature and extent. The seizure may be made after the owner has relinquished control of the property to a third party or . . . from the immediate custody and control of the owner.”</blockquote>
<p id="b855-6">Here, of course, Segura and Colon, whose possessory interests were interfered with by the occupation, were under arrest and in the custody of the police throughout the entire period the agents occupied the apartment. The actual interference with their possessory interests in the apartment and its contents was, thus, virtually nonexistent. Cf. <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970). We are not prepared to say under these limited circumstances that the seizure was unreasonable under the Fourth Amendment.<footnotemark>8</footnotemark></p>
<p id="b855-7">V</p>
<p id="b855-8">Petitioners also argue that even if the evidence was not subject to suppression as primary evidence “seized” by virtue of the initial illegal entry and occupation of the premises, it should have been excluded as “fruit” derived from that illegal entry. Whether the initial entry was illegal or not is irrelevant to the admissibility of the challenged evidence because <page-number citation-index="1" label="814">*814</page-number>there was an independent source for the warrant under which that evidence was seized. Exclusion of evidence as derivative or “fruit of the poisonous tree” is not warranted here because of that independent source.</p>
<p id="b856-5">None of the information on which the warrant was secured was derived from or related in any way to the initial entry into petitioners’ apartment; the information came from sources wholly unconnected with the entry and was known to the agents well before the initial entry. No information obtained during the initial entry or occupation of the apartment was needed or used by the agents to secure the warrant. It is therefore beyond dispute that the information possessed by the agents before they entered the apartment constituted an independent source for the discovery and seizure of the evidence now challenged. This evidence was discovered the day following the entry, during the search conducted under a valid warrant; it was the product of that search, wholly unrelated to the prior entry. The valid warrant search was a “means sufficiently distinguishable” to purge the evidence of any “taint” arising from the entry. <em>Wong Sun, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488</a></span>.<footnotemark>9</footnotemark> Had police never entered the apartment, but instead conducted a perimeter stakeout to prevent anyone from entering the apartment and destroying evidence, the contraband now challenged would have been discovered and seized precisely as it was here. The legality of the initial entry is, thus, wholly irrelevant under <em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span> </em>and <page-number citation-index="1" label="815">*815</page-number><em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).<footnotemark>10</footnotemark></p>
<p id="b857-5">Our conclusion that the challenged evidence was admissible is fully supported by our prior cases going back more than a half century. The Court has never held that evidence is “fruit of the poisonous tree” simply because “it would not have come to light but for the illegal actions of the police.” See <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><em>Wong Sun, supra, </em>at 487-488</a></span>; <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#599" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 599</a></span> (1975). That would squarely conflict with <em>Silverthome </em>and our other cases allowing admission of evidence, notwithstanding a prior illegality, when the link between the illegality and that evidence was sufficiently attenuated to dissipate the taint. By the same token, our cases make clear that evidence will not be excluded as “fruit” unless the illegality is at least the “but for” cause of the discovery of the evidence. Suppression is not justified unless “the challenged evidence is in some sense the product of illegal governmental activity.” <em>United States </em>v. <em>Crews, </em><span class="citation" data-id="9427838"><a href="/opinion/110230/united-states-v-crews/#471" aria-description="Citation for case: United States v. Crews">445 U. S., at 471</a></span>. The illegal entry into petitioners’ apartment did not contribute in any way to discovery of the evidence seized under the warrant; it is clear, therefore, that not even the threshold “but for” requirement was met in this case.</p>
<p id="b857-6">The dissent contends that the initial entry and securing of the premises are the “but for” causes of the discovery of the evidence in that, had the agents not entered the apartment, but instead secured the premises from the outside, Colon or her friends if alerted, could have removed or destroyed the evidence before the warrant issued. While the dissent embraces this “reasoning,” petitioners do not press this ar<page-number citation-index="1" label="816">*816</page-number>gument. The Court of Appeals rejected this argument as “prudentially unsound” and because it rested on “wholly speculative assumptions.” Among other things, the Court of Appeals suggested that, had the agents waited to enter the apartment until the warrant issued, they might not have decided to take Segura to the apartment and thereby alert Colon. Or, once alerted by Segura’s failure to appear, Colon might have attempted to remove the evidence, rather than destroy it, in which event the agents could have intercepted her and the evidence.</p>
<p id="b858-6">We agree fully with the Court of Appeals that the District Court’s suggestion that Colon and her cohorts would have removed or destroyed the evidence was pure speculation. Even more important, however, we decline to extend the exclusionary rule, which already exacts an enormous price from society and our system of justice, to further “protect” criminal activity, as the dissent would have us do.</p>
<p id="b858-7">It may be that, if the agents had not entered the apartment, petitioners might have arranged for the removal or destruction of the evidence, and that in this sense the agents’ actions could be considered the “but for” cause for discovery of the evidence. But at this juncture, we are reminded of Justice Frankfurter’s warning that “[s]ophisticated argument may prove a causal connection between information obtained through [illegal conduct] and the Government’s proof,” and his admonition that the courts should consider whether “[a]s a matter of good sense . . . such connection may have become so attenuated, as to dissipate the taint.” <em>Nardone, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S., at 341</a></span>. The essence of the dissent is that there is some “constitutional right” to destroy evidence. This concept defies both logic and common sense.</p>
<p id="b858-9">rH i&gt;</p>
<p id="Amm">We agree with the Court of Appeals that the cocaine, cash records, and ammunition were properly admitted into evidence. Accordingly, the judgment is affirmed.</p>
<p id="b858-10">
<em>It is so ordered.</em>
</p>
<footnote label="†">
<p id="b839-13">Justice White, Justice Powell, and Justice Rehnquist join all but Part IV of this opinion.</p>
</footnote>
<footnote label="1">
<p id="b840-8"> See Griswold, Criminal Procedure, 1969 — Is It a Means or an End?, <span class="citation no-link">29 Md. L. Rev. 307</span>, 317 (1969); see generally 2 W. LaFave, Search and Seizure §6.5 (1978).</p>
</footnote>
<footnote label="2">
<p id="b843-7"> Rivudalla-Vidal and Parra were indicted with petitioners and were charged with one count of possession with intent to distribute one-half kilogram of cocaine on one occasion and one kilogram on another occasion. Both pleaded guilty to the charges. They moved in the District Court to suppress the one-half kilogram of cocaine found on Parra’s person at the time of their arrests on the ground that the Task Force agents had stopped them in violation of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). The court denied <page-number citation-index="1" label="802">*802</page-number>the motion. Rivudalla-Vidal and Parra absconded prior to sentencing by the District Court.</p>
</footnote>
<footnote label="3">
<p id="b844-9"> In <em><span class="citation" data-id="321384"><a href="/opinion/321384/united-states-v-thomas-griffin-and-catherine-tucker/" aria-description="Citation for case: United States v. Thomas Griffin and Catherine Tucker">Griffin</a></span>, </em>absent exigent circumstances, police officers forcibly entered an apartment and discovered in plain view narcotics and related paraphernalia. The entry took place while other officers sought a search warrant. The Court of Appeals for the Sixth Circuit affirmed the District Court’s grant of the defendant’s suppression motion.</p>
</footnote>
<footnote label="4">
<p id="b844-10"> Both the District Court and the Court of Appeals held that the initial entry into the apartment was not justified by exigent circumstances, and thus that the items discovered in plain view during the limited security <page-number citation-index="1" label="803">*803</page-number>check had to be suppressed to effect the purposes of the Fourth Amendment. The United States, although it does not concede the correctness of this holding, does not contest it in this Court. Because the Government has decided not to press its argument that exigent circumstances existed, we need not and do not address this aspect of the Court of Appeals decision. We are concerned only with whether the Court of Appeals properly determined that the Fourth Amendment did not require suppression of the evidence seized during execution of the valid warrant.</p>
</footnote>
<footnote label="5">
<p id="b845-12"> In <em><span class="citation" data-id="377806"><a href="/opinion/377806/united-states-v-calixto-agapito-martha-calderon-and-horacio-rueda/" aria-description="Citation for case: United States v. Calixto Agapito, Martha Calderon and...">Agapito</a></span>, </em>DEA agents, following a 2-day surveillance of the defendant’s hotel room, arrested the suspected occupants of the room in the lobby of the hotel. After the arrests, the agents entered the hotel room and remained within, with the exception of periodic departures, for almost 24 hours until a search warrant issued. During their stay in the room, the agents seized but did not open a suitcase found in the room. In the search pursuant to the warrant, the agents found cocaine in the suitcase. Although the Second Circuit held that the initial entry was illegal, it held that the cocaine need not be suppressed because it was discovered in the search under the valid warrant.</p>
</footnote>
<footnote label="6">
<p id="b848-7"> In two instances, the Court has allowed temporary seizures and limited detentions of property based upon less than probable cause. In <em>United States </em>v. <em>Van Leeuwen, </em><span class="citation" data-id="108099"><a href="/opinion/108099/united-states-v-van-leeuwen/" aria-description="Citation for case: United States v. Van Leeuwen">397 U. S. 249</a></span> (1970), the Court refused to <page-number citation-index="1" label="807">*807</page-number>invalidate the seizure and detention — on the basis of only reasonable suspicion — of two packages delivered to a United States Post Office for mailing. One of the packages was detained on mere suspicion for only <em>1% </em>hours; by the end of that period enough information had been obtained to establish probable cause that the packages contained stolen coins. But the other package was detained for 29 hours before a search warrant was finally served. Both seizures were held reasonable. In fact, the Court suggested that both seizures and detentions for these “limited times” were “prudent” under the circumstances.</p>
<p id="b849-7">Only last Term, in <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), we considered the validity of a brief seizure and detention of a traveler’s luggage, on the basis of a reasonable suspicion that the luggage contained contraband; the purpose of the seizure and brief detention was to investigate further the causes for the suspicion. Although we held that the 90-minute detention of the luggage in the airport was, under the circumstances, unreasonable, we held that the rationale of <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), applies to permit an officer, on the basis of reasonable suspicion that a traveler is carrying luggage containing contraband, to seize and detain the luggage briefly to “investigate the circumstances that aroused his suspicion.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S., at 706</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b851-5"> A distinguished constitutional scholar raised the question whether a seizure of premises might not be appropriate to preserve the status quo and protect valuable evidence while police officers in good faith seek a warrant.</p>
<blockquote id="b851-6">“Here there is a very real practical problem. Does the police officer have any power to maintain the status quo while he, or a colleague of his, is taking the time necessary to draw up a sufficient affidavit to support an application for a search warrant, and then finding a magistrate, submitting the application to him, obtaining the search warrant if it is issued, and then bringing it to the place where the arrest was made. It seems inevitable that a minimum of several hours will be required for this process, at the very best. <em>Unless there is some kind, of a power to prevent removal of material from the premises, or destruction of material during this time, the search warrant mil almost inevitably be fruitless." </em>Griswold, 29 Md. L. Rev., at 317 (emphasis added).</blockquote>
<p id="b851-7">Justice Black posed essentially the same question in his dissent in <em>Vale </em>v. <em>Louisiana, </em><span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#36" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 36</a></span> (1970). After pointing out that Vale’s arrest just outside his residence was “plainly visible to anyone within the house, <page-number citation-index="1" label="810">*810</page-number>and the police had every reason to believe that someone in the house was likely to destroy the contraband if the search were postponed,” he noted:</p>
<blockquote id="b852-8">“This case raises most graphically the question how does a policeman protect evidence necessary to the State if he must leave the premises to get a warrant, allowing the evidence he seeks to be destroyed. The Court’s answer to that question makes unnecessarily difficult the conviction of those who prey upon society.” <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#41" aria-description="Citation for case: Vale v. Louisiana"><em>Id., </em>at 41</a></span>.</blockquote>
</footnote>
<footnote label="8">
<p id="b855-9"> Our decision in <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), is not inconsistent with this conclusion. There, we found unreasonable a 90-minute detention of a traveler’s luggage. But the detention was based only on a suspicion that the luggage contained contraband, not on probable cause. After probable cause was established, authorities held the unopened luggage for almost three days before a warrant was obtained. It was not suggested that this delay presented an independent basis for suppression of the evidence eventually discovered.</p>
</footnote>
<footnote label="9">
<p id="b856-6"><em> </em>Our holding in this respect is consistent wjth the vast majority of Federal Courts of Appeals which have held that evidence obtained pursuant to a valid warrant search need not be excluded because of a prior illegal entry. See, <em>e. g., United States </em>v. <em>Perez, </em><span class="citation" data-id="414500"><a href="/opinion/414500/united-states-v-ignacio-perez-united-states-of-america-v-luis-quintero/" aria-description="Citation for case: United States v. Ignacio Perez, United States of America...">700 F. 2d 1232</a></span> (CA8 1983); <em>United States </em>v. <em>Kinney, </em><span class="citation" data-id="9467461"><a href="/opinion/386073/united-states-v-timothy-kinney/" aria-description="Citation for case: United States v. Timothy Kinney">638 F. 2d 941</a></span> (CA6), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./452/918/">452 U. S. 918</a></span> (1981); <em>United States </em>v. <em>Fitzharris, </em><span class="citation" data-id="383555"><a href="/opinion/383555/united-states-v-cyril-b-fitzharris-archie-edwin-whatley-and-arturo/" aria-description="Citation for case: United States v. Cyril B. Fitzharris, Archie Edwin...">633 F. 2d 416</a></span> (CA51980), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./451/988/">451 U. S. 988</a></span> (1981); <em>United States </em>v. <em>Agapito, </em><span class="citation" data-id="377806"><a href="/opinion/377806/united-states-v-calixto-agapito-martha-calderon-and-horacio-rueda/" aria-description="Citation for case: United States v. Calixto Agapito, Martha Calderon and...">620 F. 2d 324</a></span> (CA2 1980); <em>United States </em>v. <em>Bosby, </em><span class="citation" data-id="402452"><a href="/opinion/402452/united-states-v-calvin-lamar-bosby-alan-maurice-ticey-and-charles-f/" aria-description="Citation for case: United States v. Calvin Lamar Bosby, Alan Maurice Ticey,...">675 F. 2d 1174</a></span> (CA11 1982) (dictum). The only Federal Court of Appeals to hold otherwise is the Ninth Circuit. See <em>United States </em>v. <em>Lomas, </em><span class="citation" data-id="9470594"><a href="/opinion/418054/united-states-v-robert-kenneth-lomas-united-states-of-america-v-peter/" aria-description="Citation for case: United States v. Robert Kenneth Lomas, United States of...">706 F. 2d 886</a></span> (1983); <em>United States </em>v. <em>Allard, </em><span class="citation" data-id="384447"><a href="/opinion/384447/united-states-v-wayne-allard/" aria-description="Citation for case: United States v. Wayne Allard">634 F. 2d 1182</a></span> (1980).</p>
</footnote>
<footnote label="10">
<p id="b857-7"> It is important to note that the dissent stresses the legal status of the agents’ initial entry and occupation of the apartment; however, this case involves only evidence seized in the search made subsequently under a valid warrant. Implicit in the dissent is that the agents’ presence in the apartment denied petitioners some legal “right” to arrange to have the incriminating evidence concealed or destroyed.</p>
</footnote>
</opinion>
```

---
