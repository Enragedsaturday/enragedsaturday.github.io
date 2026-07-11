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

## GROUP: _overhaul2/lake/cases/United States v. Blue.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Blue
type: case
citation: "384 U.S. 251 (1966)"
parallel_cite: "86 S. Ct. 1416; 16 L. Ed. 2d 510; 17 A.F.T.R.2d (RIA) 1032"
neutral_cite: 1966 U.S. LEXIS 2952
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-05-23
docket: No. 531
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
  opinion_url: "https://www.courtlistener.com/opinion/107238/united-states-v-blue/"
  cluster_id: 107238
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Blue
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[The Exclusionary Rule]]"
    role: Anchor
related:
  - "[[The Exclusionary Rule]]"
  - "[[Mapp v. Ohio]]"
  - "[[United States v. Calandra]]"
tags:
  - case
  - fifth-amendment
  - exclusionary-rule
  - self-incrimination
  - indictment
  - remedy
holding: "Dismissal of an indictment is not the remedy for the Government's allegedly unconstitutional acquisition of evidence; even assuming the Government obtained incriminating evidence in violation of the Fifth Amendment privilege against self-incrimination, the defendant is entitled at most to suppress that evidence and its fruits if the Government seeks to use them at trial — the exclusionary remedy does not extend to barring the prosecution altogether."
aliases:
  - United States v. Blue
  - "United States v. Blue (1966)"
---

# United States v. Blue

*384 U.S. 251 (1966)* (No. 531) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 107238 → combined opinion 107238 (Harlan, J.; 384 U.S. 251, argued Apr. 18-19, 1966, decided May 23, 1966). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*255`). On-read identity note: the CL opinion text attributes the opinion to Justice Harlan (not the Chief Justice). S9 promotes. -->

## Background
The Internal Revenue Service told Ben Blue he might be prosecuted for tax evasion, then made jeopardy assessments against him, his wife, and his wholly owned corporation, seized their assets, recorded tax liens, and issued statutory deficiency notices giving Blue 90 days to petition the Tax Court. Blue filed Tax Court petitions contesting the deficiencies. More than a year later the Government indicted him for willfully evading income taxes and filing false corporate returns. Blue moved to dismiss the indictment, arguing that the jeopardy-assessment and Tax Court process had compelled him to incriminate himself; the District Court dismissed the indictment on that ground, and the Government appealed directly to the Supreme Court.

## Issue
Whether an indictment must be dismissed because the Government allegedly compelled the defendant to give incriminating evidence in violation of the Fifth Amendment, or whether the defendant's remedy is limited to suppressing that evidence at trial.

## Rule
Assuming without deciding that a Fifth Amendment violation had occurred, the Court held that dismissal was the wrong remedy — the appropriate response to unconstitutionally obtained evidence is exclusion, not immunity from prosecution: "Even if we assume that the Government did acquire incriminating evidence in violation of the Fifth Amendment, Blue would at most be entitled to suppress the evidence and its fruits if they were sought to be used against him at trial." — 384 U.S. at 255. ^pin-255

## Application
The Court explained that its exclusionary-rule precedents implicitly assume the remedy does not extend to barring the prosecution altogether. Ending the prosecution entirely might add a marginal increment to the interests the exclusionary rule serves, but it would exact an intolerable cost by letting a defendant escape trial rather than merely keeping tainted evidence out of it. Blue's protection, if any, lay in suppression motions and evidentiary objections at trial — not in dismissal of the indictment. Because the District Court had dismissed rather than left those remedies for trial, its judgment could not stand.

## Conclusion
The judgment of the District Court was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]], leaving Blue free to pursue his Fifth Amendment claim through motions to suppress and objections to evidence. Harlan, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Blue* is an exclusionary-rule anchor for the *scope of the remedy*: the sanction for an unconstitutional acquisition of evidence is suppression at trial, not dismissal of the indictment or a bar to prosecution. Teach it with the grand-jury and cost-benefit cases — *[[United States v. Calandra]]* and *[[Mapp v. Ohio]]* — as marking the outer boundary of what the exclusionary rule remedies.

## Appears on
- [[The Exclusionary Rule]] — *Anchor*

## Sources
- [*United States v. Blue*, 384 U.S. 251 (1966)](https://www.courtlistener.com/opinion/107238/united-states-v-blue/) — pinpoint: 255 (Harlan, J., for the Court; in the CL opinion text the quoted holding falls between the reporter stars `*255` and `*256`, i.e., on page 255). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1f23e9bf82725157", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Blue"}, "payload": {"all": [{"cite": "384 U.S. 251", "page": "251", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "384"}, {"cite": "86 S. Ct. 1416", "page": "1416", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "86"}, {"cite": "16 L. Ed. 2d 510", "page": "510", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "16"}, {"cite": "1966 U.S. LEXIS 2952", "page": "2952", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1966"}, {"cite": "17 A.F.T.R.2d (RIA) 1032", "page": "1032", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "17"}], "display": "384 U.S. 251", "official": {"cite": "384 U.S. 251", "page": "251", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "384"}, "official_selection_present": true, "record_id": "United States v. Blue"}}
{"assertion_id": "10b2704c516fecc9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Blue"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Blue", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Blue

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Blue",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Blue",
    "case_name_short": "Blue",
    "case_name_full": "United States v. Blue",
    "input_case_name": "United States v. Blue",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-05-23",
    "year": 1966,
    "docket": "No. 531",
    "cluster_id": 107238,
    "lead_opinion_id": 107238,
    "sibling_ids": [],
    "absolute_url": "/opinion/107238/united-states-v-blue/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 251",
      "volume": "384",
      "reporter": "U.S.",
      "page": "251",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1416",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 510",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 A.F.T.R.2d (RIA) 1032",
        "volume": "17",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1032",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 2952",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2952",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 251",
        "volume": "384",
        "reporter": "U.S.",
        "page": "251",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1416",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 510",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "510",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 2952",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "2952",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 A.F.T.R.2d (RIA) 1032",
        "volume": "17",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "1032",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 251",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 251",
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
    "date_created": "2026-07-06T13:43:06Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:43:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-blue--107238",
      "to_record_id": "United States v. Blue",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Blue

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b350-7">
  Mr. Justice Harlan
 </author>
<p id="AEj">
  delivered the opinion of the Court.
 </p>
<p id="b350-8">
  In 1962 the appellee, Ben Blue, was informed by the Internal Revenue Service that he might be criminally prosecuted for violation of the federal income tax laws. The following year the Service made jeopardy assessments against Blue, his wife, and his wholly owned corporation for tax liability for the years 1958 to 1960 inclusive; the known assets of all three were seized and tax liens recorded. Internal Revenue Code of 1954, §§ 6321-6323, 6331, 6861. Statutory notices were then issued giving Blue 90 days within which to file petitions if he wished to contest the proposed deficiencies in the Tax Court, I. R. C. §6213, and Blue filed petitions setting forth his position and alleging errors in the Commissioner’s determination of deficiencies. More than a year later the Government initiated the present criminal case by a six-count indictment charging Blue with wilfully attempting to evade personal income taxes for the years 1958 through 1960 and with filing false returns for his corporation during the same years. I. R. C. §§ 7201, 7206 (1).
 </p>
<p id="b350-9">
  Blue filed a pretrial motion seeking dismissal of the indictment on several grounds. After a hearing the District Court granted the motion. The court stated orally that because of the jeopardy assessment and Tax Court proceeding Blue “has been compelled and will be compelled to come forward on the same matters as are con
  <span citation-index="1" class="star-pagination" label="253"> 
   *253
   </span>
  cerned in this criminal case, to testify against himself . ...”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The Government filed a notice of appeal and the case was docketed in the Court of Appeals for the Ninth Circuit. Determining that the District Court had sustained a “motion in bar, when the defendant has not been put in jeopardy” so that a direct appeal lay to this Court,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  the Court of Appeals certified the case to us, <span class="citation" data-id="268997"><a href="/opinion/268997/united-states-v-ben-blue/" aria-description="Citation for case: United States v. Ben Blue">350 F. 2d 267</a></span>, and we postponed jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./382/971/">382 U. S. 971</a></span>. We agree that this Court has jurisdiction over the appeal and, on the merits, reverse the decision of the District Court.
 </p>
<p id="b351-5">
  Since Blue had not yet been brought to trial and put in jeopardy when dismissal occurred, see
  <em>
   United States
  </em>
  v. Celestine, <span class="citation" data-id="97114"><a href="/opinion/97114/united-states-v-celestine/#283" aria-description="Citation for case: United States v. Celestine">215 U. S. 278, 283</a></span>, our jurisdiction under the statute is secure if the motion sustained by the District Court was a motion in bar. See,
  <em>
   supra,
  </em>
  n. 2. This in
  <span citation-index="1" class="star-pagination" label="254"> 
   *254
   </span>
  turn depends on “the effect of the ruling sought to be reviewed,”
  <em>
   United States
  </em>
  v.
  <em>
   Hark,
  </em>
  <span class="citation" data-id="9419414"><a href="/opinion/103909/united-states-v-hark/#536" aria-description="Citation for case: United States v. Hark">320 U. S. 531, 536</a></span>, and not on how the pleading is styled or on whether it is ultimately sustained on appeal. Like the Court of Appeals, we take the dismissal in this case as a ruling that absent reversal on review future prosecution of Blue on the pending counts is forever barred. While there are slight ambiguities in language, the District Court’s dismissal was grounded in what it found to be past compulsory self-incrimination and in its apparent belief that this mischief could not be undone save by turning back the clock through ending the prosecution.
 </p>
<p id="b352-6">
  Because the dismissal by its own force would “end the cause and exculpate the defendant,”
  <em>
   United States
  </em>
  v.
  <em>
   Hark,
  </em>
  <span class="citation" data-id="9419414"><a href="/opinion/103909/united-states-v-hark/#536" aria-description="Citation for case: United States v. Hark">320 U. S., at 536</a></span>, rather than merely abate the prosecution on account of some normally curable defect, one requisite of a motion in bar is met. Whether it is a further requisite that the motion introduce “new matter” in the fashion of a plea by way of confession and avoidance need not here be decided. See
  <em>
   United States
  </em>
  v.
  <em>
   Mersky,
  </em>
  <span class="citation" data-id="105997"><a href="/opinion/105997/united-states-v-mersky/#441" aria-description="Citation for case: United States v. Mersky">361 U. S. 431, 441, 453</a></span> (separate opinions disagreeing on this point). For in this instance Blue unquestionably relied on new matter in alleging self-incrimination, so the motion qualifies even under the more stringent definition. Thus under either view of a motion in bar taken in
  <em>
   <span class="citation" data-id="105997"><a href="/opinion/105997/united-states-v-mersky/" aria-description="Citation for case: United States v. Mersky">Mersky</a></span>,
  </em>
  this case qualifies for direct review. Our conclusion on the jurisdictional issue is further supported by two analogous decisions of this Court treating claims of
  <em>
   statutory
  </em>
  immunity as pleas in bar which permitted direct appeal.
  <em>
   United States
  </em>
  v.
  <em>
   Hoffman,
  </em>
  <span class="citation" data-id="9420215"><a href="/opinion/104586/united-states-v-hoffman/" aria-description="Citation for case: United States v. Hoffman">335 U. S. 77</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Monia,
  </em>
  <span class="citation" data-id="9419281"><a href="/opinion/103748/united-states-v-monia/" aria-description="Citation for case: United States v. Monia">317 U. S. 424</a></span>.
 </p>
<p id="b352-7">
  On the merits of the case, we do not believe that the District Court should have dismissed the indictment. The Government has argued that the statements made by Blue in his Tax Court petitions were no more than
  <span citation-index="1" class="star-pagination" label="255"> 
   *255
   </span>
  successive denials of the alleged underpayments and do not constitute incriminating evidence. The Government has also intimated that by merely providing the occasion for the filing of Blue’s petitions in fulfilling its statutory duty to make jeopardy assessments and send deficiency notices, it ought not be regarded as compelling the taxpayer to incriminate himself within the meaning of the Fifth Amendment. There is no need, however, to consider these or other contentions that may point in the same direction.
 </p>
<p id="b353-5">
  Even if we assume that the Government did acquire incriminating evidence in violation of the Fifth Amendment, Blue would at most be entitled to suppress the evidence and its fruits if they were sought to be used against him at trial.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  While the general common-law practice is to admit evidence despite its illegal origins, this Court in a number of areas has recognized or developed exclusionary rules where evidence has been gained in violation of the accused’s rights under the Constitution, federal statutes, or federal rules of procedure.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>;
  <em>
   Rogers
  </em>
  v.
  <em>
   Richmond,
  </em>
  <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>;
  <em>
   Mapp
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>;
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span>;
  <em>
   Mallory
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/" aria-description="Citation for case: Mallory v. United States">354 U. S. 449</a></span>. Our numerous precedents ordering the exclusion of such illegally obtained evidence assume implicitly that the remedy does not extend to barring the prosecution altogether. So drastic a step might advance marginally some of the ends served by exclusionary rules, but it would also increase to an intolerable degree interference with the public interest in having the guilty brought to book.
 </p>
<p id="b354-3">
<span citation-index="1" class="star-pagination" label="256"> 
   *256
   </span>
  We remand this case to the District Court to proceed on the merits, leaving Blue free to pursue his Fifth Amendment claim through motions to suppress and objections to evidence. It is not entirely clear from Blue’s brief and argument whether he seeks to sustain the dismissal below on other grounds that the District Court did not accept. See,
  <em>
   supra,
  </em>
  n. 1. Putting to one side jurisdictional difficulties this course might encounter under the direct-review statute,
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  we believe it is fairer to all to regard no other grounds as presented, thus reserving to Blue the opportunity to articulate them plainly and support them by the record.
 </p>
<p id="b354-4">
<em>
   Reversed and remanded.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b351-6">
   The court stated that it based the dismissal “on that ground alone.” It rejected a claim that the seizure of property and recording of tax liens had prevented Blue from preparing an adequate defense by depleting his resources. It did not expressly consider Blue’s claim that there is an administrative practice of making no assessments in advance of criminal proceedings and that failure to extend the policy to him was a denial of due process.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b351-7">
   <span class="citation no-link">18 U. S. C. §3731</span> (1964 ed.) provides in part:
  </p>
<blockquote id="b351-8">
   “An appeal may be taken by and on behalf of the United States from the district courts direct to the Supreme Court of the United States in all criminal cases in the following instances:
  </blockquote>
<blockquote id="b351-9">
   “From the decision or judgment sustaining a motion in bar, when the defendant has not been put in jeopardy.
  </blockquote>
<blockquote id="b351-10">
   “If an appeal shall be taken pursuant to this section to any court of appeals which, in the opinion of such court, should have been taken directly to the Supreme Court of the United States, such court shall certify the case to the Supreme Court of the United States, which shall thereupon have jurisdiction to hear and determine the case to the same extent as if an appeal had been taken directly to that Court.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b353-6">
   It does not seem to be contended that tainted evidence was presented to the grand jury; but in any event our precedents indicate this would not be a basis for abating the prosecution pending a new indictment, let alone barring it altogether. See
   <em>
    Costello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421237"><a href="/opinion/105355/costello-v-united-states/" aria-description="Citation for case: Costello v. United States">350 U. S. 359</a></span>;
   <em>
    Lawn
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421531"><a href="/opinion/105609/lawn-v-united-states/" aria-description="Citation for case: Lawn v. United States">355 U. S. 339</a></span>; 8 Wigmore, Evidence § 2184a, at 40 (McNaughton rev. 1961).
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b354-5">
   See Stern &amp; Gressman, Supreme Court Practice §2-11, at 31-33 (1962); Friedenthal, Government Appeals in Federal Criminal Cases, <span class="citation no-link">12 Stan. L. Rev. 71</span>, 97-100 (1959).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Braxton.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Braxton"
type: case
citation: "61 F.4th 830 (2023)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2023
date_decided: 2023-03-07
docket: 21-1149
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2023-03-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Braxton
  varies_by_point: false
  scope_note: "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/"
  cluster_id: 9381854
  opinion_id: 9377330
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Recent development (role-based)"
related: ["[[Arizona v. Gant]]", "[[Chimel v. California]]", "[[Riley v. California]]", "[[Nix v. Williams]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "inevitable-discovery"]
holding: "The government CONCEDED the warrantless search of Braxton's backpack was not a valid search incident to arrest, then relied on…"
lake:
  record_id: United States v. Braxton
  status: verified
  projected_at: 2026-07-09
---

# United States v. Braxton

*61 F.4th 830 (10th Cir. 2023)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Braxton on a public sidewalk and, without a warrant, searched a backpack associated with him, finding a firearm. He was charged with firearm and drug offenses and moved to suppress the gun. Under the circuit's recent decision in *United States v. Knapp* — which held that a search of an arrestee's bag is not a valid [[Search Incident to Arrest|search incident to arrest]] where the arrestee cannot reach weapons or evidence in the bag at the time — the government conceded the backpack search was not a lawful [[Search Incident to Arrest|search incident to arrest]] and instead relied on [[Inevitable Discovery and Independent Source|inevitable discovery]].

## Issue
Whether evidence from a backpack search that was not a valid [[Search Incident to Arrest|search incident to arrest]] is nonetheless admissible under the inevitable-discovery exception, on the theory that officers would have lawfully impounded the backpack ([[Community Caretaking|community caretaking]]) and discovered the gun in an inventory search.

## Rule
The search-incident-to-arrest point was conceded: "the government concedes that the warrantless search of the backpack was not justified by the warrant exception for searches incident to arrest." — slip op., at 7. ^pin-op7

To salvage the evidence by [[Inevitable Discovery and Independent Source|inevitable discovery]], the government bore the burden of proving lawful impoundment and inventory would have occurred. The court held it had not: "the inevitable-discovery exception to the exclusionary rule does not apply, and the gun discovered during the illegal search of the backpack must be suppressed." — [*Id.* at 17](https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/#:~:text=the%20inevitable%2Ddiscovery%20exception%20to%20the%20exclusionary%20rule%20does). ^pin-op17

## Application
Because Braxton was under arrest and could not access the backpack at the time of the search, the search was not a valid [[Search Incident to Arrest|search incident to arrest]] — a point the government conceded under *Knapp*. The government then failed to prove by a preponderance that officers would have lawfully impounded the backpack as a matter of [[Community Caretaking|community caretaking]] and inventoried it; the record left the impoundment speculative and suggested any on-scene inventory would itself have been improper. [[Inevitable Discovery and Independent Source|Inevitable discovery]] therefore did not apply, and the gun was suppressed.

## Conclusion
The backpack search was an invalid [[Search Incident to Arrest|search incident to arrest]], and [[Inevitable Discovery and Independent Source|inevitable discovery]] did not cure it; suppression was ordered and the denial below reversed. A bag search is not incident to arrest once the arrestee cannot reach it, and [[Inevitable Discovery and Independent Source|inevitable discovery]] requires proof — not speculation — of a lawful alternative route to the evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Braxton* applies the reaching-distance limit on [[Search Incident to Arrest|searches incident to arrest]] from [[Chimel v. California]] and [[Arizona v. Gant]] (and the circuit's *Knapp* rule for bags), and the inevitable-discovery doctrine of [[Nix v. Williams]]; on digital/container limits compare [[Riley v. California]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Recent development (role-based)*

## Sources
- *United States v. Braxton*, 61 F.4th 830 (10th Cir. 2023) — https://www.courtlistener.com/opinion/9381854/united-states-v-braxton/ — pinpoints: slip op., at 7, 17 (CL carries the slip opinion; cluster 9381854 → opinion 9377330).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7d73c1df78e6e786", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Braxton"}, "payload": {"all": [{"cite": "61 F.4th 830", "page": "830", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}], "display": "61 F.4th 830", "official": {"cite": "61 F.4th 830", "page": "830", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "61"}, "official_selection_present": true, "record_id": "United States v. Braxton"}}
{"assertion_id": "2ddd96ee53713f69", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op17", "record_id": "United States v. Braxton"}, "payload": {"fragment": "#:~:text=the%20inevitable%2Ddiscovery%20exception%20to%20the%20exclusionary%20rule%20does", "page": null, "pin_id": "pin-op17", "pinpoint_status": "star-verified", "quote": "the inevitable-discovery exception to the exclusionary rule does not apply, and the gun discovered during the illegal search of the backpack must be suppressed.", "quote_fidelity": "matched", "record_id": "United States v. Braxton", "star_marker": "3"}}
{"assertion_id": "97acb97817cc8632", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op7", "record_id": "United States v. Braxton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op7", "pinpoint_status": "slip-only", "quote": "--- # United States v. Braxton *61 F.4th 830 (10th Cir. 2023)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Braxton on a public sidewalk and, without a warrant, searched a backpack associated with him, finding a firearm. He was charged with firearm and drug offenses and moved to suppress the gun. Under the circuit's recent decision in *United States v. Knapp* — which held that a search of an arrestee's bag is not a valid search incident to arrest where the arrestee cannot reach weapons or evidence in the bag at the time — the government conceded the backpack search was not a lawful search incident to arrest and instead relied on inevitable discovery. ## Issue Whether evidence from a backpack search that was not a valid search incident to arrest is nonetheless admissible under the inevitable-discovery exception, on the theory that officers would have lawfully impounded the backpack (community caretaking) and discovered the gun in an inventory search. ## Rule The search-incident-to-arrest point was conceded:", "quote_fidelity": "mismatch", "record_id": "United States v. Braxton", "star_marker": null}}
{"assertion_id": "15b624b7c962ba32", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Braxton"}, "payload": {"as_of_content": "2023-03-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Braxton", "scope_note": "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it.", "varies_by_point": false}}
```

### lake record — United States v. Braxton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Braxton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Braxton",
    "case_name_short": "Braxton",
    "case_name_full": "",
    "input_case_name": "United States v. Braxton",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2023-03-07",
    "year": 2023,
    "docket": "21-1149",
    "cluster_id": 9381854,
    "lead_opinion_id": 9377330,
    "sibling_ids": [
      9377330
    ],
    "absolute_url": "/opinion/9381854/united-states-v-braxton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "61 F.4th 830",
      "volume": "61",
      "reporter": "F.4th",
      "page": "830",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "61 F.4th 830",
        "volume": "61",
        "reporter": "F.4th",
        "page": "830",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "61 F.4th 830",
    "official_selection": {
      "court_class": "coa",
      "selected": "61 F.4th 830",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op7",
      "page": null,
      "quote": "--- # United States v. Braxton *61 F.4th 830 (10th Cir. 2023)* \u00b7 U.S. Court of Appeals, 10th Circuit \u00b7 **Binding in-circuit \u2014 10th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Braxton on a public sidewalk and, without a warrant, searched a backpack associated with him, finding a firearm. He was charged with firearm and drug offenses and moved to suppress the gun. Under the circuit's recent decision in *United States v. Knapp* \u2014 which held that a search of an arrestee's bag is not a valid search incident to arrest where the arrestee cannot reach weapons or evidence in the bag at the time \u2014 the government conceded the backpack search was not a lawful search incident to arrest and instead relied on inevitable discovery. ## Issue Whether evidence from a backpack search that was not a valid search incident to arrest is nonetheless admissible under the inevitable-discovery exception, on the theory that officers would have lawfully impounded the backpack (community caretaking) and discovered the gun in an inventory search. ## Rule The search-incident-to-arrest point was conceded:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op17",
      "page": null,
      "quote": "the inevitable-discovery exception to the exclusionary rule does not apply, and the gun discovered during the illegal search of the backpack must be suppressed.",
      "star_marker": "3",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 30187,
      "fragment": "#:~:text=the%20inevitable%2Ddiscovery%20exception%20to%20the%20exclusionary%20rule%20does",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2023-03-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Braxton",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; backpack search conceded invalid as SITA, and inevitable discovery did not save it.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Brandon Christopher Serini v. The State of Wyoming",
          "cluster_id": 10374407,
          "cite": [
            "566 P.3d 190",
            "2025 WY 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elmore",
          "cluster_id": 9505983,
          "cite": [
            "101 F.4th 1210"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramos",
          "cluster_id": 9452629,
          "cite": [
            "88 F.4th 862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montgomery v. Cruz",
          "cluster_id": 10769646,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campbell",
          "cluster_id": 10681819,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brandon Christopher Serini v. The State of Wyoming",
          "cluster_id": 10375200,
          "cite": [
            "2025 WY 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Braxton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9377330) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(9377330)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9377330)",
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
    "complete_query": "cites:(9377330)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9377330,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 8,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-braxton.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9377330,
        "cited_id": 1245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 161257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 163326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 220780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 332335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 436329,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 600741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 770086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 795888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4373735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4530911,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4674893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 4683374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 8413595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 9430773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9377330,
        "cited_id": 9482577,
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
    "date_created": "2026-07-05T22:45:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:49:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:45:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Braxton

```
Appellate Case: 21-1149     Document: 010110822581       Date Filed: 03/07/2023    Page: 1
                                                                                  FILED
                                                                      United States Court of Appeals
                                       PUBLISH                                Tenth Circuit

                       UNITED STATES COURT OF APPEALS                        March 7, 2023

                                                                         Christopher M. Wolpert
                              FOR THE TENTH CIRCUIT                          Clerk of Court
                          _________________________________

  UNITED STATES OF AMERICA,

        Plaintiff - Appellee,

  v.                                                          No. 21-1149

  TYRELL BRAXTON,

        Defendant - Appellant.
                       _________________________________

                      Appeal from the United States District Court
                              for the District of Colorado
                           (D.C. No. 1:20-CR-00037-RM-1)
                        _________________________________

 Meredith Esser, Assistant Federal Public Defender, Denver, Colorado (Virginia L. Grady,
 Federal Public Defender, with her on the briefs), for Defendant - Appellant.

 Wayne Paugh, Assistant United States Attorney, Denver, Colorado (Cole Finegan, United
 States Attorney, with him on the brief), for Plaintiff - Appellee.
                         _________________________________

 Before HARTZ, SEYMOUR, and MORITZ, Circuit Judges.
                   _________________________________

 MORITZ, Circuit Judge.
                     _________________________________

       Law enforcement searched Tyrell Braxton’s backpack after arresting him and

 found a gun. Facing several criminal charges, Braxton moved to suppress the gun.

 The government conceded that the warrantless search was not a valid search incident

 to arrest. But it invoked the inevitable-discovery doctrine to avoid suppression of the
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023       Page: 2



 illegally obtained evidence, contending that—assuming the illegal search incident to

 arrest had not occurred—law enforcement would have validly impounded the

 backpack as a matter of community caretaking and then searched it pursuant to a

 standardized policy mandating inventory searches of seized property. The district

 court agreed with the government and denied the motion to suppress.

        But the government’s stated community-caretaking interest in safeguarding

 Braxton’s personal property by impounding it is significantly undercut by the

 presence of an individual who arrived on the scene at Braxton’s request and

 repeatedly asked to take possession of the backpack throughout the arrest process.

 The government’s explanation for why the officers could have properly refused this

 individual’s requests is not persuasive. Nor is it dispositive, on these facts, that

 Braxton himself did not ask the officers to turn the backpack over. Thus, the

 government failed to meet its burden to show that law enforcement would have

 validly retained the backpack, and the inevitable-discovery doctrine does not apply to

 excuse application of the exclusionary rule to suppress evidence discovered during

 the illegal search. We accordingly reverse the district court’s order refusing to

 suppress the gun and remand for further proceedings.

                                       Background

        A Denver police officer monitoring a camera installed in a high-crime area

 saw Braxton exchange drugs for cash. Officers arrived on the scene and arrested

 Braxton. As the district court noted, the details of the arrest are not in dispute

 because one officer’s bodycam captured the arrest on video.


                                             2
Appellate Case: 21-1149   Document: 010110822581        Date Filed: 03/07/2023      Page: 3



       The video shows that at the moment he was handcuffed, Braxton was wearing

 a black backpack with a repeating “Emporio Armani” design on it, which the officers

 removed and placed on the sidewalk. One officer then patted Braxton down and

 discovered suspected crack cocaine and $183 in cash in Braxton’s pockets. During

 the patdown, Braxton called out, “Hey, get my girl, my girl. Tan! Tell her to come

 here!” Supp. R. at 1:51–1:56.

       Less than 30 seconds later, a woman—later identified as Braxton’s girlfriend,

 Tanyrah Gay—approached the officers, and Braxton instructed her, “Get the money

 so you can bond me out.” Id. at 2:18–2:23. Gay then asked the officers, “Can I get his

 bag?” Id. at 2:24–2:26. The officers responded in the negative. Gay stood by for a

 little over a minute while one officer continued searching Braxton. Then, as one

 officer walked away with Braxton and another officer picked up the backpack, Gay

 again asked, “I can’t take my backpack?” Id. at 3:38–3:40. The officer immediately

 responded with a curt “nope.” Id. at 3:40–3:41.

       Gay followed as one officer escorted Braxton to a patrol car and another

 carried the backpack. As Braxton was getting into the patrol car, he said, “She needs

 the money, man.” Id. at 4:10–4:12. Gay then said, “I’m in a hotel. Please give me the

 money at least. I’m in a hotel.” Id. at 4:13–4:18. Before Gay could finish, the answer

 again was an immediate “nope.” Id. at 4:16. Gay then asked if the officers would

 write her number down; they told her they would “get to that in a second.” Id. at

 4:38–4:40.




                                           3
Appellate Case: 21-1149    Document: 010110822581         Date Filed: 03/07/2023     Page: 4



       One officer placed the backpack on the hood of the patrol car and searched it.

 As the officer dug through the backpack’s contents, he found a loaded gun with a

 pink handle. Before the officer completed the search of the backpack, Gay asked him

 if she could retrieve her bus pass and identification from the backpack. The officer

 said they could “talk about that in a second.” Id. at 7:15–7:16. About 20 seconds

 later, after the officer placed the gun into an evidence bag and into the front of the

 patrol vehicle, the bodycam footage ends.

       Based on this event, the government charged Braxton with possession of a

 weapon in furtherance of drug trafficking, possession of crack cocaine with intent to

 distribute, and felon in possession of a weapon. Braxton moved to suppress the gun,

 arguing that the warrantless search of his backpack was not justified as a search

 incident to arrest under this court’s recent precedent. See United States v. Knapp, 917

 F.3d 1161 (10th Cir. 2019) (holding that search of arrestee’s purse was not justified

 as search incident to arrest because arrestee could not access weapons or destroy

 evidence within purse at time of arrest).

       The government conceded that the search was not a valid search incident to

 arrest under Knapp. But it argued that the gun should not be suppressed because law

 enforcement would have inevitably discovered it after impounding the backpack and

 conducting an inventory search. That is, the government reasoned, had the officer not

 searched the backpack at the scene, he would have been obligated to take the

 backpack to the station to prevent theft and to protect the community in case the

 backpack contained dangerous items. And once at the station, the government


                                             4
Appellate Case: 21-1149      Document: 010110822581       Date Filed: 03/07/2023    Page: 5



 continued, standard policy required an inventory search that would have revealed the

 gun. The government supported its position with testimony from the officer who

 searched Braxton’s backpack.

          The district court agreed with the government and denied the motion to

 suppress. Braxton eventually entered a conditional guilty plea to possessing a firearm

 in furtherance of a drug-trafficking crime, and the district court sentenced him to 60

 months in prison and three years of supervised release.1

          Braxton now appeals the suppression ruling.

                                          Analysis

          Our review of the overall reasonableness of a search or seizure is de novo,

 though we accept the district court’s factual findings unless clearly erroneous and

 view the evidence in the light most favorable to the district court’s findings. Knapp,

 917 F.3d at 1165; see also United States v. Cook, 599 F.3d 1208, 1213 (10th Cir.

 2010).

          “The Fourth Amendment’s prohibition of ‘unreasonable searches and seizures’

 means that police generally cannot conduct a search or make a seizure absent a

 warrant.” United States v. Kendall, 14 F.4th 1116, 1122 (10th Cir. 2021) (citation

 omitted) (quoting U.S. Const. amend IV). “A warrantless search or seizure is

 reasonable only ‘if it falls within a specific exception to the warrant requirement.’”


          1
         Braxton also pleaded guilty to a separate count of felon in possession of a
 firearm based on events that occurred on a different date. The district court imposed a
 consecutive 12-month sentence for this additional count (and a concurrent three-year
 term of supervised release), bringing Braxton’s prison sentence to 72 months in total.

                                              5
Appellate Case: 21-1149    Document: 010110822581       Date Filed: 03/07/2023    Page: 6



 Id. at 1121–22 (quoting United States v. Venezia, 995 F.3d 1170, 1174 (10th Cir.

 2021)). These exceptions include, among others, searches incident to arrest, searches

 and seizures justified by a noninvestigatory community-caretaking rationale, and

 searches conducted for administrative inventory purposes. See Knapp, 917 F.3d at

 1165 (discussing exception for searches incident to arrest); United States v. Neugin,

 958 F.3d 924, 931 (10th Cir. 2020) (explaining community-caretaking exception);

 Kendall, 14 F.4th at 1124 (describing exception for inventory searches). It is the

 government’s burden to establish that an exception to the warrant requirement

 applies. Neugin, 958 F.3d at 930.

       If law enforcement searches or seizes without a warrant or applicable warrant

 exception and thus “obtains evidence th[r]ough an unconstitutional search, the

 evidence is inadmissible under the exclusionary rule.” Id. at 931. But like the warrant

 requirement, the exclusionary rule is also subject to some exceptions, one of which is

 the inevitable-discovery doctrine. Id. at 932. Under this doctrine, the exclusionary

 rule does not apply if the government can prove by a preponderance that “the

 evidence inevitably would have been discovered by lawful means.” Id. (quoting

 United States v. Souza, 223 F.3d 1197, 1202 (10th Cir. 2000)). The parties agree that

 the inevitable-discovery doctrine requires a counterfactual inquiry into what “would

 have” happened under lawful circumstances.2 Id. At the same time, “‘[i]n


       2
          Because we rule for Braxton on another ground, we need not address his
 argument that law enforcement violated the Fourth Amendment because the officer
 testified that he did search the backpack with an investigatory motive, under the facts
 as they occurred.

                                            6
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023     Page: 7



 determining whether the government has met its burden of proof, we consider

 “demonstrated historical facts,” not “speculative elements.”’” Id. (quoting United

 States v. White, 326 F.3d 1135, 1138 (10th Cir. 2003)).

        Here, the government concedes that the warrantless search of the backpack

 was not justified by the warrant exception for searches incident to arrest. But it

 contends that the inevitable-discovery exception to the exclusionary rule should

 apply because the officers would have eventually conducted a valid warrantless

 search of the backpack via two other exceptions to the warrant requirement:

 community caretaking and inventory. Specifically, the government argues that the

 officers would have impounded the backpack under a community-caretaking

 rationale to protect Braxton’s property rather than leaving it vulnerable to theft on the

 public sidewalk where Braxton was arrested. See, e.g., Venezia, 995 F.3d at 1180

 (“Certainly, an abandoned vehicle on a public highway may be at risk of theft or

 vandalism, and thus may be impounded under the community-caretaking doctrine.”).

 And it further contends that once the backpack was delivered to the police station,

 law-enforcement policy mandated an inventory search to further protect Braxton’s

 property. See, e.g., Kendall, 14 F.4th at 1124 (explaining that inventory “searches

 serve several administrative purposes, including ‘to protect an owner’s property

 while it is in the custody of the police, to insure against claims of lost, stolen, or

 vandalized property, and to guard the police from danger’” (quoting Colorado v.

 Bertine, 479 U.S. 367, 372 (1987))).




                                              7
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023     Page: 8



       The latter point is not in dispute—as the district court concluded, the parties

 do not “quarrel[] with the need or appropriateness of the inventory” search once the

 backpack reached the police station. R. vol. 3, 147. Instead, this case turns on

 whether the officers would have validly impounded Braxton’s backpack in the

 absence of the illegal search incident to arrest. See United States v. Ibarra, 955 F.2d

 1405, 1410 (10th Cir. 1992) (finding no inevitable discovery because although

 inventory search was valid, “no inventory of the contents of defendant’s vehicle

 could have been conducted but for the unlawful impoundment of the vehicle”). On

 impoundment, the district court concluded that the officers were “entitled to take

 physical possession of” the backpack “on a community[-]caretaker . . . basis.” R. vol.

 3, 146. The district court dismissed the relevance of Gay’s presence and her repeated

 requests to take possession of the backpack, emphasizing that Braxton never asked

 the officers to give the backpack to Gay and reasoning that to the officers at the time,

 the relationship between Braxton and Gay was unclear.

       On appeal, Braxton argues that the government did not meet its burden of

 showing that officers would have impounded the backpack as a matter of community

 caretaking. We have had many recent opportunities to examine community-

 caretaking impoundments, albeit in the context of vehicles rather than personal

 property like Braxton’s backpack. See Kendall, 14 F.4th at 1122 (citing three recent

 published cases). Yet the principles from these vehicle-impoundment cases are

 relevant in the context of personal property. See Knapp, 917 F.3d at 1168 (noting that

 principles articulated in vehicle-impoundment caselaw “apply more broadly” and


                                            8
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023      Page: 9



 using such caselaw to review search of defendant’s purse); United States v. Perea,

 986 F.2d 633, 643 (2d Cir. 1993) (noting that for arrests that do not occur at

 individual’s home, “officers may ‘impound the personal effects that are with him [or

 her] at the time to ensure the safety of those effects or to remove nuisances from the

 area’” (quoting Cabbler v. Superintendent, Va. State Penitentiary, 528 F.2d 1142,

 1146 (4th Cir. 1975))). Indeed, the parties also frame their arguments around our

 vehicle-impoundment caselaw, in particular United States v. Sanders, 796 F.3d 1241

 (10th Cir. 2015).

       Sanders held that impoundment of a vehicle from private property must be

 “justified by both [1] a standardized policy and [2] a reasonable, non[]pretextual

 community-caretaking rationale.” Id. at 1248. We begin (and end) our analysis with

 the second prong.3 On that prong, Sanders set out a nonexclusive list of factors

 relevant to determining whether “a reasonable and legitimate, non[]pretextual

 community-caretaking rationale” exists, including:

       (1) whether the vehicle is on public or private property; (2) if on private
       property, whether the property owner has been consulted; (3) whether

       3
          The government contends that Sanders’s first prong does not apply here
 because we are on public—not private—property. See Kendall, 14 F.4th at 1122 (“In
 one of our recent cases, however, we clarified that the first Sanders prong is ‘specific
 to private property impoundments.’” (quoting Venezia, 995 F.3d at 1178)). But
 Braxton asserts in reply that the government waived such argument by not raising it
 below. See United States v. Martinez, 643 F.3d 1292, 1298 (10th Cir. 2011) (“We
 will not consider a suppression argument raised for the first time on appeal absent a
 showing of good cause for why it was not raised before the trial court.”). In any
 event, we need not address these issues here because even if the government did not
 waive its first-prong argument and its argument is correct, it still needs to satisfy the
 second Sanders prong; and the same is true if the government did waive its first-
 prong argument or if such argument is incorrect.

                                             9
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023      Page: 10



        an alternative to impoundment exists (especially another person capable
        of driving the vehicle); (4) whether the vehicle is implicated in a crime;
        and (5) whether the vehicle’s owner and/or driver have consented to the
        impoundment.

  Id. at 1250. These factors help guide the overall question for Fourth Amendment

  purposes: whether, in the counterfactual world of our inevitable-discovery inquiry,

  the seizure of Braxton’s backpack would have been reasonable. See id. (“Protection

  against unreasonable impoundments . . . is part and parcel of the Fourth

  Amendment’s guarantee against unreasonable searches and seizures.”).

        Four of these factors apply in a relatively straightforward manner here. First,

  the arrest took place on public property, so the backpack itself was also on public

  property. See id. Braxton concedes that this fact would weigh in favor of a reasonable

  community-caretaking rationale for impoundment because the officers obviously

  could not have left the backpack on the sidewalk. See Kendall, 14 F.4th at 1123

  (weighing this factor in favor of reasonable community-caretaking rationale for

  impoundment because it was not “a reasonable option for officers to leave the vehicle

  where it was,” parked on public street). Relatedly, the public location renders the

  second Sanders factor—whether the owner of private property has been consulted—

  simply not relevant here. See id. (omitting second factor from discussion where arrest

  took place on public property). On the fourth and fifth other factors, the government

  concedes that the backpack here was not implicated in a crime and that Braxton did

  not consent to the impoundment. See 796 F.3d at 1250.These two factors accordingly

  would weigh against a reasonable community-caretaking rationale for impoundment.



                                            10
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023     Page: 11



  See United States v. Woodard, 5 F.4th 1148, 1158 (10th Cir. 2021) (weighing these

  factors against valid impoundment).

        Largely agreeing on these four factors, the parties center their disagreement on

  the third Sanders factor, the existence of an alternative to impoundment. See 796

  F.3d at 1250. On this point, recall that Gay appeared less than 30 seconds after

  Braxton called out for his “girl,” Gay twice asked to take the backpack, and the

  officers curtly rejected her requests almost before she could finish her requests. R.

  vol. 3, 143. Braxton contends that giving the backpack to Gay would have been an

  alternative to impoundment and argues that this factor weighs heavily against a

  reasonable community-caretaking rationale for impoundment. In response, the

  government argues that giving the backpack to Gay would not have been an

  alternative to impoundment for two reasons: (1) Braxton did not ask the officers to do

  so and (2) nothing in the record suggests that Braxton and Gay had a relationship that

  warranted giving his backpack to her.

        As to the government’s first point, it is true that Braxton did not expressly ask

  the officers to give Gay the backpack. But we have stated that “[t]he proper inquiry

  under the third factor is ‘whether an alternative to impoundment exists’ and is not

  focused on who suggested that alternative.” Venezia, 995 F.3d at 1181 (emphasis

  added) (quoting Sanders, 796 F.3d at 1250). Braxton’s failure to directly ask the

  officers to give the backpack to Gay is therefore not dispositive. It is just one fact

  among many, and we do not find it particularly meaningful in light of Gay’s physical




                                             11
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023    Page: 12



  presence at the scene and repeated requests to take the backpack. Given these facts, a

  satisfactory alternative to impoundment may have existed.

        As to the government’s second point, the record does not support the notion

  that Braxton and Gay’s relationship negated the plausibility of this alternative. Gay

  appeared less than 30 seconds after Braxton called out for his “girl,” and the officer

  who testified at the suppression hearing said that he assumed the person who arrived

  in response to Braxton’s request was, in fact, the person Braxton had asked for—his

  “girl.” R. vol. 3, 143. Other facts support the conclusion that the two had a

  relationship close enough to merit giving her the backpack: Braxton asked Gay to

  bail him out; Braxton asked the officers to give Gay the money they found on him;

  Gay repeatedly asked to take the backpack; Gay at one point referred to the backpack

  as hers, which suggests that Braxton was carrying it for her; Gay remained nearby

  during the entire arrest process; Gay asked the police to write her number down; and

  Gay told the officers her bus pass and identification were in the backpack. These

  facts suggest that, at a minimum, reasonable officers dealing with the backpack in a

  lawful manner would have inquired further about whether they should give the

  backpack to Gay, either by asking Braxton if he wanted Gay to take the backpack or

  by inquiring into their relationship.4


        4
           The government asserts that the district court made a factual finding that Gay
  was essentially “a stranger” to Braxton. R. vol. 3, 149. But as Braxton points out in
  reply, the district court’s comment on this point was less than clear. The district court
  referred to Gay as “a stranger,” but not necessarily a stranger to Braxton; it could
  have been pointing out that Gay was a stranger to the officers. Id. Because of this
  ambiguity and because this case involves undisputed video evidence of the arrest—in

                                             12
Appellate Case: 21-1149     Document: 010110822581        Date Filed: 03/07/2023     Page: 13



        Importantly, the officer who testified at the suppression hearing provided scant

  explanation for why—in the counterfactual scenario in which he was not going to

  search the backpack incident to arrest—he would have refused Gay’s requests and

  would not have inquired further into their relationship or asked Braxton about giving

  her the backpack. At best, when explaining why he did not ask Braxton if Gay could

  take the backpack, the officer said it was “not common practice to be handing out

  personal property of other persons to other people.” Id. at 93. And it is true that the

  government produced a department policy stating that “[a]ny officer coming into

  possession of personal . . . property will bring such property to the [e]vidence and

  [p]roperty [s]ection[] or an authorized remote evidence locker.” R. vol. 1, 28. But the

  existence of and compliance with such a policy does not by itself establish a

  reasonable community-caretaking rationale. See Sanders, 796 F.3d at 1249–50

  (“Protection against unreasonable impoundments, even those conducted pursuant to a

  standardized policy, is part and parcel of the Fourth Amendment’s guarantee against

  unreasonable searches and seizures.” (emphasis added)); Venezia, 995 F.3d at 1182

  (holding impoundment unreasonable despite compliance with policy because policy


  the words of the district court, its factual findings “really do[]n’t matter . . . because
  it’s all on body[]cam,” id. at 142—we decline to interpret the district court’s
  reference to Gay as “a stranger” as a factual finding that she and Braxton were
  strangers to each other, id. at 149. And even if we were to do so, we would hold that
  finding clearly erroneous in light of the strong record evidence—detailed above,
  supra p. 12—that Gay and Braxton were not at all strangers. See United States v.
  Martinez-Jimenez, 464 F.3d 1205, 1209 (10th Cir. 2006) (stating that factual finding
  is clearly erroneous if it is “without factual support in the record or we are left with
  the definite and firm conviction that a mistake has been made” (quoting United States
  v. Cernobyl, 255 F.3d 1215, 1221 (10th Cir. 2001))).

                                             13
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023     Page: 14



  “did not grant the officers authority to do what the Fourth Amendment forbids—to

  impound a vehicle absent a reasonable community-caretaking rationale”). Nor does

  the policy negate the existence of an alternative to impoundment: The policy defines

  personal property as property that “must be held for safekeeping for the owner.”

  R. vol. 1, 27 (emphasis added). And the officer’s testimony does not meaningfully

  explain why, in light of Gay’s requests, he needed to impound the backpack to keep it

  safe for its owner. We thus conclude, on the record before us, that the alternative to

  impoundment of giving the backpack to Gay weighs heavily against finding a

  reasonable community-caretaking rationale. See Woodard, 5 F.4th at 1156 (weighing

  this factor against community-caretaking rationale where officers refused, without

  reason, to let defendant call someone to take his car); Venezia, 995 F.3d at 1179

  (“Where an alternative to impoundment does not threaten public safety or

  convenience, impoundment is less likely to be justified by a community-caretaking

  rationale.”).

         To recap, the only factor that favors a reasonable community-caretaking

  rationale for impoundment is that the arrest took place on public property. The

  remaining factors—an alternative to impoundment, that the backpack was not

  implicated in the crime, and that Braxton did not consent—cut significantly against a

  community-caretaking rationale. On these facts, we conclude the government failed

  to meet its burden of proving that, despite the alternative of giving the backpack to

  Gay, it was inevitable that the officers would have validly impounded the backpack

  under a reasonable community-caretaking rationale. See Venezia, 995 F.3d at 1182


                                             14
Appellate Case: 21-1149    Document: 010110822581        Date Filed: 03/07/2023       Page: 15



  (concluding that existence of alternative rendered impoundment unreasonable); cf.

  Kendall, 14 F.4th at 1123 (concluding that “balance clearly weighs in favor of the

  reasonableness of impoundment, partly because there were no good alternatives”).

        The government emphasizes that officers are not obligated to explore

  alternatives to impoundment, noting that “[t]he reasonableness of any particular

  governmental activity does not necessarily or invariably turn on the existence of

  alternative ‘less intrusive’ means.” Aplee. Br. 24 (emphasis added) (quoting Bertine,

  479 U.S. at 374). But this general proposition does not mean that reasonableness does

  not sometimes, depending on the facts, turn on the existence of alternatives to

  impoundment. Indeed, “we have recognized that impoundment . . . is not reasonable

  when there are clear and promptly available alternatives.” United States v. Trujillo,

  993 F.3d 859, 868 (10th Cir. 2021); see also United States v. Pappas, 735 F.2d 1232,

  1234 (10th Cir. 1984) (finding impoundment unreasonable in part because

  defendant’s girlfriend and other friends were present and could have taken custody);

  cf. Trujillo, 993 F.3d at 870 (concluding that where vehicle posed traffic hazard and

  defendant was alone at 2:30 a.m., officers “were not required to allow [d]efendant to

  call someone to come pick up the [vehicle] and then, assuming he was successful,

  wait around for the new driver to arrive” and citing cases with similar facts and

  reasoning). Moreover, our precedent establishes that officers generally act

  unreasonably when they ignore or shut down obvious alternatives to impoundment.

  See Woodard, 5 F.4th at 1156 (weighing existence of alternative against community-

  caretaking rationale where defendant asked officers if he could call someone to pick


                                            15
Appellate Case: 21-1149     Document: 010110822581         Date Filed: 03/07/2023     Page: 16



  up vehicle and officers refused to let him do so without explanation); Sanders, 796

  F.3d at 1251 (finding impoundment unreasonable in part because “police impounded

  [defendant’s] vehicle without offering her the opportunity to make alternative

  arrangements, even though she stated that she was willing to have someone pick up

  the vehicle on her behalf”); cf. Kendall, 14 F.4th at 1123–25 (finding impoundment

  reasonable in part because of absence of alternatives).5 And the officer here did just

  that, failing to offer any reasonable rationale for not at least inquiring further about

  whether Gay could take the backpack.6

        In sum, because a clear and promptly available alternative existed here, the

  government cannot show that it would have impounded the backpack under a

  reasonable, nonpretextual community-caretaking rationale. Thus, the government




        5
           Braxton additionally highlights a district-court case that held the
  impoundment of personal property was unjustified by a reasonable community-
  caretaking rationale in a factually similar case. See United States v. Knapp, No. 17-
  CR-207, 2019 WL 11502454, at *3 (D. Wyo. June 13, 2019) (concluding
  impoundment was unreasonable in part because friend who was present during
  defendant’s arrest offered to take her purse, but officers talked friend out of it).
         6
           A separate aspect of the officer’s testimony is also troubling: When prompted
  to expound on what he would have done had he availed himself of the alternative to
  impoundment, the officer said that even if he had given Gay the backpack, he would
  have inventoried it before doing so. The government does not argue on appeal that
  this on-the-scene inventory search would have led to the inevitable discovery of the
  gun, and the district court ruled below that any such on-the-scene inventory search
  would have been constitutionally impermissible. But we note that this testimony
  suggests that in a counterfactual world without the illegal search incident to arrest
  and without an illegal impoundment, an illegal search would still have taken place.
  Although by no means determinative, this testimony further supports our conclusion
  that the inevitable-discovery doctrine does not save the government from the
  exclusionary rule in this case.

                                              16
Appellate Case: 21-1149    Document: 010110822581       Date Filed: 03/07/2023    Page: 17



  failed to meet its burden to show that the gun would have been legally and inevitably

  discovered.

                                       Conclusion

        The government failed to prove by a preponderance of the evidence that if the

  law-enforcement officers had not conducted an illegal search incident to arrest, they

  would have nevertheless lawfully impounded the backpack as a matter of community

  caretaking and then discovered the gun during an inventory search. Thus, the

  inevitable-discovery exception to the exclusionary rule does not apply, and the gun

  discovered during the illegal search of the backpack must be suppressed. We

  accordingly reverse the district court’s order denying suppression and remand for

  further proceedings.




                                            17

```

---

## GROUP: _overhaul2/lake/cases/United States v. Brignoni-Ponce.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Brignoni-Ponce"
type: case
citation: "422 U.S. 873 (1975)"
parallel_cite: "95 S. Ct. 2574; 45 L. Ed. 2d 607"
neutral_cite: 1975 U.S. LEXIS 10
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-06-30
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-06-30
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Brignoni-Ponce
  varies_by_point: false
  scope_note: "Holding (roving-patrol stops require reasonable suspicion) is good law; the dictum treating apparent ancestry as a permissible factor has been widely criticized."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109311/united-states-v-brignoni-ponce/"
  cluster_id: 109311
  opinion_id: 109311
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Almeida-Sanchez v. United States]]", "[[Terry v. Ohio]]", "[[Delaware v. Prouse]]", "[[United States v. Cortez]]"]
aliases: ["United States v. Felix Humberto Brignoni-Ponce"]
tags: ["case", "fourth-amendment", "border-search", "reasonable-suspicion"]
holding: "A roving Border Patrol may stop a vehicle near the border to question occupants only on reasonable suspicion, based on specific…"
lake:
  record_id: United States v. Brignoni-Ponce
  status: verified
  projected_at: 2026-07-06
---

# United States v. Brignoni-Ponce

*422 U.S. 873 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A roving Border Patrol unit near the California-Mexico border stopped Brignoni-Ponce's car solely because its three occupants appeared to be of Mexican ancestry, and questioned them about their immigration status; two passengers were illegally present. The stop was not at the border or a fixed checkpoint. The government argued that, near the border, apparent Mexican ancestry alone justified a stop to question occupants.

## Issue
Whether a roving Border Patrol may stop a vehicle near the border and question its occupants about immigration status based only on the occupants' apparent Mexican ancestry, or whether the stop requires reasonable suspicion.

## Rule
A roving-patrol stop requires reasonable suspicion built on articulable facts: "Except at the border and its functional equivalents, officers on roving patrol may stop vehicles only if they are aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country." — 422 U.S. at 884. ^pin-884

Apparent ancestry alone is not enough: "The likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens." — *Id.* at 886–87. ^pin-886

## Application
Because the officers relied on a single factor — the occupants' apparent Mexican ancestry — they lacked the specific, articulable facts needed to warrant a reasonable suspicion that the car carried persons illegally in the country. That sole ground could not justify the roving-patrol stop, so the stop violated the Fourth Amendment and the evidence of the passengers' status had to be suppressed.

## Conclusion
The roving-patrol stop based only on apparent ancestry was unlawful; the suppression was affirmed. Away from the border and its functional equivalents, a roving patrol may stop a vehicle to question occupants only on reasonable suspicion grounded in specific articulable facts.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. The holding remains controlling; the opinion's treatment of apparent ancestry as a relevant factor is widely criticized and, in practice, given little or no weight.
- *Brignoni-Ponce* extends the reasonable-suspicion stop of [[Terry v. Ohio]] to roving border patrols, building on [[Almeida-Sanchez v. United States]] (no suspicionless roving searches) and informing later stop standards in [[United States v. Cortez]] and [[Delaware v. Prouse]].

## Appears on
- [[Border Searches]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Brignoni-Ponce*, 422 U.S. 873 (1975) — https://www.courtlistener.com/opinion/109311/united-states-v-brignoni-ponce/ — pinpoints: 884, 886–87.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0343faf2519beaa8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Brignoni-Ponce"}, "payload": {"all": [{"cite": "422 U.S. 873", "page": "873", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "422"}, {"cite": "95 S. Ct. 2574", "page": "2574", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "95"}, {"cite": "45 L. Ed. 2d 607", "page": "607", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "45"}, {"cite": "1975 U.S. LEXIS 10", "page": "10", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1975"}], "display": "422 U.S. 873", "official": {"cite": "422 U.S. 873", "page": "873", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "422"}, "official_selection_present": true, "record_id": "United States v. Brignoni-Ponce"}}
{"assertion_id": "19915a66373ab4ab", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-884", "record_id": "United States v. Brignoni-Ponce"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-884", "pinpoint_status": "slip-only", "quote": "--- # United States v. Brignoni-Ponce *422 U.S. 873 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A roving Border Patrol unit near the California-Mexico border stopped Brignoni-Ponce's car solely because its three occupants appeared to be of Mexican ancestry, and questioned them about their immigration status; two passengers were illegally present. The stop was not at the border or a fixed checkpoint. The government argued that, near the border, apparent Mexican ancestry alone justified a stop to question occupants. ## Issue Whether a roving Border Patrol may stop a vehicle near the border and question its occupants about immigration status based only on the occupants' apparent Mexican ancestry, or whether the stop requires reasonable suspicion. ## Rule A roving-patrol stop requires reasonable suspicion built on articulable facts:", "quote_fidelity": "mismatch", "record_id": "United States v. Brignoni-Ponce", "star_marker": null}}
{"assertion_id": "d4385013b3e01472", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-886", "record_id": "United States v. Brignoni-Ponce"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-886", "pinpoint_status": "slip-only", "quote": "The likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens.", "quote_fidelity": "mismatch", "record_id": "United States v. Brignoni-Ponce", "star_marker": null}}
{"assertion_id": "8176a4e353fabd99", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Brignoni-Ponce"}, "payload": {"as_of_content": "1975-06-30", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Brignoni-Ponce", "scope_note": "Holding (roving-patrol stops require reasonable suspicion) is good law; the dictum treating apparent ancestry as a permissible factor has been widely criticized.", "varies_by_point": false}}
```

### lake record — United States v. Brignoni-Ponce

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Brignoni-Ponce",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Brignoni-Ponce",
    "case_name_short": "Brignoni-Ponce",
    "case_name_full": "United States v. Brignoni-Ponce",
    "input_case_name": "United States v. Brignoni-Ponce",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-06-30",
    "year": 1975,
    "docket": null,
    "cluster_id": 109311,
    "lead_opinion_id": 109311,
    "sibling_ids": [
      109311,
      9426196,
      9426197,
      9426198
    ],
    "absolute_url": "/opinion/109311/united-states-v-brignoni-ponce/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "422 U.S. 873",
      "volume": "422",
      "reporter": "U.S.",
      "page": "873",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 S. Ct. 2574",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2574",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 607",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "607",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 10",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "10",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "422 U.S. 873",
        "volume": "422",
        "reporter": "U.S.",
        "page": "873",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 S. Ct. 2574",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2574",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 607",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "607",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 10",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "10",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "422 U.S. 873",
    "official_selection": {
      "court_class": "scotus",
      "selected": "422 U.S. 873",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-884",
      "page": null,
      "quote": "--- # United States v. Brignoni-Ponce *422 U.S. 873 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A roving Border Patrol unit near the California-Mexico border stopped Brignoni-Ponce's car solely because its three occupants appeared to be of Mexican ancestry, and questioned them about their immigration status; two passengers were illegally present. The stop was not at the border or a fixed checkpoint. The government argued that, near the border, apparent Mexican ancestry alone justified a stop to question occupants. ## Issue Whether a roving Border Patrol may stop a vehicle near the border and question its occupants about immigration status based only on the occupants' apparent Mexican ancestry, or whether the stop requires reasonable suspicion. ## Rule A roving-patrol stop requires reasonable suspicion built on articulable facts:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-886",
      "page": null,
      "quote": "The likelihood that any given person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-06-30",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Brignoni-Ponce",
    "varies_by_point": false,
    "scope_note": "Holding (roving-patrol stops require reasonable suspicion) is good law; the dictum treating apparent ancestry as a permissible factor has been widely criticized.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Darrell Mark Babcock",
          "cluster_id": 4623035,
          "cite": [
            "924 F.3d 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez",
          "cluster_id": 4574288,
          "cite": [
            "910 F.3d 1309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
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
        "journal_ref": "United States v. Brignoni-Ponce:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109311 OR 9426196 OR 9426197 OR 9426198) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk2OTE1MjAwMDAwJnM9MjY3MzU1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109311+OR+9426196+OR+9426197+OR+9426198%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(109311 OR 9426196 OR 9426197 OR 9426198)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjA3JnM9MTE4MzkxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109311+OR+9426196+OR+9426197+OR+9426198%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109311 OR 9426196 OR 9426197 OR 9426198)",
        "reviewed": 45,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 45,
        "triage_read": 0,
        "triage_snippet_classified": 45
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109311 OR 9426196 OR 9426197 OR 9426198)",
    "indexed_citing_opinions": 2431,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109311,
        "count": 2199,
        "count_source": "search"
      },
      {
        "opinion_id": 9426196,
        "count": 331,
        "count_source": "search"
      },
      {
        "opinion_id": 9426197,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426198,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3737,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-brignoni-ponce.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjAzNDkmcz0xMDYxMjk4MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109311+OR+9426196+OR+9426197+OR+9426198%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109311,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 108612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 109208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 293899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 306426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 310273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 313406,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 318216,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 320445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 320684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 320688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 320689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109311,
        "cited_id": 1802688,
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
    "date_created": "2026-07-05T22:49:27Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:49:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:49:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:52:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:49:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Brignoni-Ponce

```
<div>
<center><b><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U.S. 873</a></span> (1975)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
BRIGNONI-PONCE.</h1></center>
<center>No. 74-114.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 18, 1975.</center>
<center>Decided June 30, 1975.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*874</span> <i>Deputy Solicitor General Frey</i> argued the cause for the United States. On the briefs were <i>Solicitor General Bork, Assistant Attorney General Petersen, Acting Assistant Attorney General Keeney, Mark L. Evans, Peter M. Shannon, Jr.,</i> and <i>Jerome M. Feit.</i></p>
<p><i>John J. Cleary,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./419/1017/">419 U. S. 1017</a></span>, argued the cause for respondent. With him on the brief was <i>Charles M. Sevilla.</i><sup>[*]</sup></p>
<p>MR. JUSTICE POWELL delivered the opinion of the Court.</p>
<p>This case raises questions as to the United States Border Patrol's authority to stop automobiles in areas near the Mexican border. It differs from our decision in <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266</a></span> (1973), in that the Border Patrol does not claim authority to search cars, but only to question the occupants about their citizenship and immigration status.</p>
<p></p>
<h2>I</h2>
<p>As part of its regular traffic-checking operations in southern California, the Border Patrol operates a fixed checkpoint on Interstate Highway 5 south of San Clemente. On the evening of March 11, 1973, the checkpoint was closed because of inclement weather, but two officers were observing northbound traffic from a patrol <span class="star-pagination">*875</span> car parked at the side of the highway. The road was dark, and they were using the patrol car's headlights to illuminate passing cars. They pursued respondent's car and stopped it, saying later that their only reason for doing so was that its three occupants appeared to be of Mexican descent. The officers questioned respondent and his two passengers about their citizenship and learned that the passengers were aliens who had entered the country illegally. All three were then arrested, and respondent was charged with two counts of knowingly transporting illegal immigrants, a violation of § 274 (a) (2) of the Immigration and Nationality Act, <span class="citation no-link">66 Stat. 228</span>, <span class="citation no-link">8 U. S. C. § 1324</span> (a) (2). At trial respondent moved to suppress the testimony of and about the two passengers, claiming that this evidence was the fruit of an illegal seizure. The trial court denied the motion, the aliens testified at trial, and respondent was convicted on both counts.</p>
<p>Respondent's appeal was pending in the Court of Appeals for the Ninth Circuit when we announced our decision in <i>Almeida-Sanchez</i> v. <i>United States, supra</i><i>,</i> holding that the Fourth Amendment prohibits the use of roving patrols to search vehicles, without a warrant or probable cause, at points removed from the border and its functional equivalents. The Court of Appeals, sitting en banc, held that the stop in this case more closely resembled a roving-patrol stop than a stop at a traffic checkpoint, and applied the principles of <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span>.</i><sup>[1]</sup><span class="star-pagination">*876</span> The court held that the Fourth Amendment, as interpreted in <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span>,</i> forbids stopping a vehicle, even for the limited purpose of questioning its occupants, unless the officers have a "founded suspicion" that the occupants are aliens illegally in the country. The court refused to find that Mexican ancestry alone supported such a "founded suspicion" and held that respondent's motion to suppress should have been granted.<sup>[2]</sup> <span class="citation" data-id="320445"><a href="/opinion/320445/united-states-v-felix-humberto-brignoni-ponce/" aria-description="Citation for case: United States v. Felix Humberto Brignoni-Ponce">499 F. 2d 1109</a></span> (1974). We granted certiorari and set the case for oral argument with No. 73-2050, <i>United States</i> v. <i>Ortiz, post,</i> p. 891, and No. 73-6848, <i>Bowen</i> v. <i>United States, post,</i> p. 916. <span class="citation" data-id="8991948"><a href="/opinion/8999445/bowen-v-united-states/" aria-description="Citation for case: Bowen v. United States">419 U. S. 824</a></span> (1974).</p>
<p>The Government does not challenge the Court of Appeals' factual conclusion that the stop of respondent's car was a roving-patrol stop rather than a checkpoint stop. Brief for United States 8. Nor does it challenge the retroactive application of <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez, supra,</a></span></i> Brief for United States 9, or contend that the San Clemente checkpoint is the functional equivalent of the border. The only issue presented for decision is whether a roving patrol may stop a vehicle in an area near the border and question its occupants when the only ground for suspicion is that the occupants appear to be of Mexican ancestry. For the reasons that follow, we affirm the decision of the Court of Appeals.</p>
<p></p>
<h2>II</h2>
<p>The Government claims two sources of statutory authority <span class="star-pagination">*877</span> for stopping cars without warrants in the border areas. Section 287 (a) (1) of the Immigration and Nationality Act, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (1), authorizes any officer or employee of the Immigration and Naturalization Service (INS) without a warrant, "to interrogate any alien or person believed to be an alien as to his right to be or to remain in the United States." There is no geographical limitation on this authority. The Government contends that, at least in the areas adjacent to the Mexican border, a person's apparent Mexican ancestry alone justifies belief that he or she is an alien and satisfies the requirement of this statute. Section 287 (a) (3) of the Act, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3), authorizes agents, without a warrant,</p>
<blockquote>"Within a reasonable distance from any external boundary of the United States, to board and search for aliens any vessel within the territorial waters of the United States and any railway car, aircraft, conveyance, or vehicle . . . ."</blockquote>
<p>Under current regulations, this authority may be exercised anywhere within 100 miles of the border. <span class="citation no-link">8 CFR § 287.1</span> (a) (1975). The Border Patrol interprets the statute as granting authority to stop moving vehicles and question the occupants about their citizenship, even when its officers have no reason to believe that the occupants are aliens or that other aliens may be concealed in the vehicle.<sup>[3]</sup> But "no Act of Congress can authorize a violation of the Constitution." <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#272" aria-description="Citation for case: Almeida-Sanchez v. United States"><i>Almeida-Sanchez, supra,</i> at 272</a></span>. <span class="star-pagination">*878</span> and we must decide whether the Fourth Amendment allows such random vehicle stops in the border areas.</p>
<p></p>
<h2>III</h2>
<p>The Fourth Amendment applies to all seizures of the person, including seizures that involve only a brief detention short of traditional arrest. <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968). "[W]henever a police officer accosts an individual and restrains his freedom to walk away, he has `seized' that person," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 16</a></span>, and the Fourth Amendment requires that the seizure be "reasonable." As with other categories of police action subject to Fourth Amendment constraints, the reasonableness of such seizures depends on a balance between the public interest and the individual's right to personal security free from arbitrary interference by law officers. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20-21</a></span>; <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967).</p>
<p>The Government makes a convincing demonstration that the public interest demands effective measures to prevent the illegal entry of aliens at the Mexican border. Estimates of the number of illegal immigrants in the United States vary widely. A conservative estimate in 1972 produced a figure of about one million, but the INS now suggests there may be as many as 10 or 12 million aliens illegally in the country.<sup>[4]</sup> Whatever the number, these aliens create significant economic and social problems, competing with citizens and legal resident <span class="star-pagination">*879</span> aliens for jobs, and generating extra demand for social services. The aliens themselves are vulnerable to exploitation because they cannot complain of substandard working conditions without risking deportation. See generally Hearings on Illegal Aliens before Subcommittee No. 1 of the House Committee on the Judiciary, 92d Cong., 1st and 2d Sess., ser. 13, pts. 1-5 (1971-1972).</p>
<p>The Government has estimated that 85% of the aliens illegally in the country are from Mexico. <i>United States</i> v. <i>Baca,</i> <span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/#402" aria-description="Citation for case: United States v. Baca">368 F. Supp. 398, 402</a></span> (SD Cal. 1973).<sup>[5]</sup> The Mexican border is almost 2,000 miles long, and even a vastly reinforced Border Patrol would find it impossible to prevent illegal border crossings. Many aliens cross the Mexican border on foot, miles away from patrolled areas, and then purchase transportation from the border area to inland cities, where they find jobs and elude the immigration authorities. Others gain entry on valid temporary border-crossing permits, but then violate the conditions of their entry. Most of these aliens leave the border area in private vehicles, often assisted by professional "alien smugglers." The Border Patrol's traffic-checking operations are designed to prevent this inland movement. They succeed in apprehending some illegal entrants and smugglers, and they deter the movement of others by threatening apprehension and increasing the cost of illegal transportation.</p>
<p>Against this valid public interest we must weigh the interference with individual liberty that results when an officer stops an automobile and questions its occupants. <span class="star-pagination">*880</span> The intrusion is modest. The Government tells us that a stop by a roving patrol "usually consumes no more than a minute." Brief for United States 25. There is no search of the vehicle or its occupants, and the visual inspection is limited to those parts of the vehicle that can be seen by anyone standing alongside.<sup>[6]</sup> According to the Government, "[a]ll that is required of the vehicle's occupants is a response to a brief question or two and possibly the production of a document evidencing a right to be in the United States." <i><span class="citation" data-id="1802688"><a href="/opinion/1802688/united-states-v-baca/" aria-description="Citation for case: United States v. Baca">Ibid.</a></span></i></p>
<p>Because of the limited nature of the intrusion, stops of this sort may be justified on facts that do not amount to the probable cause required for an arrest. In <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> the Court declined expressly to decide whether facts not amounting to probable cause could justify an "investigative `seizure' " short of an arrest, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19</a></span> n. 16, but it approved a limited searcha pat-down for weaponsfor the protection of an officer investigating suspicious behavior of persons he reasonably believed to be armed and dangerous. The Court approved such a search on facts that did not constitute probable cause to believe the suspects guilty of a crime, requiring only that "the police officer . . . be able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant" a belief that his safety or that of others is in danger. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 21</a></span>; see <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 27</a></span>.</p>
<p>We elaborated on <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> in <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), holding that a policeman was justified <span class="star-pagination">*881</span> in approaching the respondent to investigate a tip that he was carrying narcotics and a gun.</p>
<blockquote>"The Fourth Amendment does not require a policeman who lacks the precise level of information necessary for probable cause to arrest to simply shrug his shoulders and allow a crime to occur or a criminal to escape. On the contrary, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> recognizes that it may be the essence of good police work to adopt an intermediate response. . . . A brief stop of a suspicious individual, in order to determine his identity or to maintain the status quo momentarily while obtaining more information, may be most reasonable in light of the facts known to the officer at the time." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#145" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 145-146</a></span>.</blockquote>
<p>These cases together establish that in appropriate circumstances the Fourth Amendment allows a properly limited "search" or "seizure" on facts that do not constitute probable cause to arrest or to search for contraband or evidence of crime. In both <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i>Adams</i> v. <i><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Williams</a></span></i> the investigating officers had reasonable grounds to believe that the suspects were armed and that they might be dangerous. The limited searches and seizures in those cases were a valid method of protecting the public and preventing crime. In this case as well, because of the importance of the governmental interest at stake, the minimal intrusion of a brief stop, and the absence of practical alternatives for policing the border, we hold that when an officer's observations lead him reasonably to suspect that a particular vehicle may contain aliens who are illegally in the country, he may stop the car briefly and investigate the circumstances that provoke suspicion. As in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the stop and inquiry must be "reasonably related in scope to the justification for their initiation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span>. The officer may question the driver and passengers about their citizenship and <span class="star-pagination">*882</span> immigration status, and he may ask them to explain suspicious circumstances, but any further detention or search must be based on consent or probable cause.</p>
<p>We are unwilling to let the Border Patrol dispense entirely with the requirement that officers must have a reasonable suspicion to justify roving-patrol stops.<sup>[7]</sup> In the context of border area stops, the reasonableness requirement of the Fourth Amendment demands something more than the broad and unlimited discretion sought by the Government. Roads near the border carry not only aliens seeking to enter the country illegally, but a large volume of legitimate traffic as well. San Diego, with a metropolitan population of 1.4 million, is located on the border. Texas has two fairly large metropolitan areas directly on the border: El Paso, with a population of 360,000, and the Brownsville-McAllen area, with a combined population of 320,000. We are confident that substantially all of the traffic in these cities is lawful and that relatively few of their residents have any connection with the illegal entry and transportation of aliens. To approve roving-patrol stops of all vehicles in the border area, without any suspicion that a particular vehicle is carrying illegal immigrants, would subject the residents of these and other areas to potentially unlimited interference with their use of the highways, solely at the discretion of Border Patrol officers. The only formal limitation on that discretion appears to be the administrative regulation defining the term "reasonable distance" in § 287 (a) (3) to mean within 100 <span class="star-pagination">*883</span> air miles from the border. <span class="citation no-link">8 CFR § 287.1</span> (a) (1975). Thus, if we approved the Government's position in this case, Border Patrol officers could stop motorists at random for questioning, day or night, anywhere within 100 air miles of the 2,000-mile border, on a city street, a busy highway, or a desert road, without any reason to suspect that they have violated any law.</p>
<p>We are not convinced that the legitimate needs of law enforcement require this degree of interference with lawful traffic. As we discuss in Part IV, <i>infra,</i> the nature of illegal alien traffic and the characteristics of smuggling operations tend to generate articulable grounds for identifying violators. Consequently, a requirement of reasonable suspicion for stops allows the Government adequate means of guarding the public interest and also protects residents of the border areas from indiscriminate official interference. Under the circumstances, and even though the intrusion incident to a stop is modest, we conclude that it is not "reasonable" under the Fourth Amendment to make such stops on a random basis.<sup>[8]</sup></p>
<p>The Government also contends that the public interest in enforcing conditions on legal alien entry justifies stopping persons who may be aliens for questioning about their citizenship and immigration status. Although we <span class="star-pagination">*884</span> may assume for purposes of this case that the broad congressional power over immigration, see <i>Kleindienst</i> v. <i>Mandel,</i> <span class="citation" data-id="9425024"><a href="/opinion/108612/kleindienst-v-mandel/#765" aria-description="Citation for case: Kleindienst v. Mandel">408 U. S. 753, 765-767</a></span> (1972), authorizes Congress to admit aliens on condition that they will submit to reasonable questioning about their right to be and remain in the country, this power cannot diminish the Fourth Amendment rights of citizens who may be mistaken for aliens. For the same reasons that the Fourth Amendment forbids stopping vehicles at random to inquire if they are carrying aliens who are illegally in the country, it also forbids stopping or detaining persons for questioning about their citizenship on less than a reasonable suspicion that they may be aliens.</p>
<p></p>
<h2>IV</h2>
<p>The effect of our decision is to limit exercise of the authority granted by both § 287 (a) (1) and § 287 (a) (3). Except at the border and its functional equivalents, officers on roving patrol may stop vehicles only if they are aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country.<sup>[9]</sup></p>
<p>Any number of factors may be taken into account in deciding whether there is reasonable suspicion to stop a car in the border area. Officers may consider the characteristics of the area in which they encounter a vehicle. Its proximity to the border, the usual patterns <span class="star-pagination">*885</span> of traffic on the particular road, and previous experience with alien traffic are all relevant. See <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#159" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 159-161</a></span> (1925); <i>United States</i> v. <i>Jaime-Barrios,</i> <span class="citation" data-id="318216"><a href="/opinion/318216/united-states-v-carlos-jaime-barrios-united-states-of-america-v-rafael/" aria-description="Citation for case: United States v. Carlos Jaime-Barrios, United States of...">494 F. 2d 455</a></span> (CA9), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./417/972/">417 U. S. 972</a></span> (1974).<sup>[10]</sup> They also may consider information about recent illegal border crossings in the area. The driver's behavior may be relevant, as erratic driving or obvious attempts to evade officers can support a reasonable suspicion. See <i>United States</i> v. <i>Larios-Montes,</i> <span class="citation" data-id="320684"><a href="/opinion/320684/united-states-v-noe-larios-montes/" aria-description="Citation for case: United States v. Noe Larios-Montes">500 F. 2d 941</a></span> (CA9 1974); <i>Duprez</i> v. <i>United States,</i> <span class="citation" data-id="293899"><a href="/opinion/293899/gene-duprez-v-united-states/" aria-description="Citation for case: Gene Duprez v. United States">435 F. 2d 1276</a></span> (CA9 1970). Aspects of the vehicle itself may justify suspicion. For instance, officers say that certain station wagons, with large compartments for fold-down seats or spare tires, are frequently used for transporting concealed aliens. See <i>United States</i> v. <i>Bugarin-Casas,</i> <span class="citation" data-id="313456"><a href="/opinion/313456/united-states-v-salvador-bugarin-casas/" aria-description="Citation for case: United States v. Salvador Bugarin-Casas">484 F. 2d 853</a></span> (CA9 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1136/">414 U. S. 1136</a></span> (1974); <i>United States</i> v. <i>Wright,</i> <span class="citation" data-id="310273"><a href="/opinion/310273/united-states-v-belmer-lewis-wright-jr/" aria-description="Citation for case: United States v. Belmer Lewis Wright, Jr.">476 F. 2d 1027</a></span> (CA5 1973). The vehicle may appear to be heavily loaded, it may have an extraordinary number of passengers, or the officers may observe persons trying to hide. See <i>United States</i> v. <i><span class="citation" data-id="320684"><a href="/opinion/320684/united-states-v-noe-larios-montes/" aria-description="Citation for case: United States v. Noe Larios-Montes">Larios-Montes, supra</a></span></i><i>.</i> The Government also points out that trained officers can recognize the characteristic appearance of persons who live in Mexico, relying on such factors as the mode of dress and haircut. Reply Brief for United States 12-13, in <i>United States</i> v. <i>Ortiz, post,</i> p. 891. In all situations the officer is entitled to assess the facts in light of his experience in detecting illegal entry and smuggling. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>.</p>
<p>In this case the officers relied on a single factor to justify stopping respondent's car: the apparent Mexican ancestry <span class="star-pagination">*886</span> of the occupants.<sup>[11]</sup> We cannot conclude that this furnished reasonable grounds to believe that the three occupants were aliens. At best the officers had only a fleeting glimpse of the persons in the moving car, illuminated by headlights. Even if they saw enough to think that the occupants were of Mexican descent, this factor alone would justify neither a reasonable belief that they were aliens, nor a reasonable belief that the car concealed other aliens who were illegally in the country. Large numbers of native-born and naturalized citizens have the physical characteristics identified with Mexican ancestry, and even in the border area a relatively small proportion of them are aliens.<sup>[12]</sup> The likelihood that any given <span class="star-pagination">*887</span> person of Mexican ancestry is an alien is high enough to make Mexican appearance a relevant factor, but standing alone it does not justify stopping all Mexican-Americans to ask if they are aliens.</p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>[For opinion of THE CHIEF JUSTICE concurring in the judgment, see <i>post,</i> p. 899.]</p>
<p>[For opinion of MR. JUSTICE WHITE concurring in the judgment, see <i>post,</i> p. 914.]</p>
<p>MR. JUSTICE REHNQUIST, concurring.</p>
<p>I join in the opinion of the Court. I think it quite important to point out, however, that that opinion, which is joined by a somewhat different majority than that which comprised the <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> Court, is both by its terms and by its reasoning concerned only with the type of stop involved in this case. I think that just as travelers entering the country may be stopped and searched without probable cause and without founded suspicion, because of "national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in," <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925), a strong case may be made for those charged with the enforcement of laws conditioning the right of vehicular use of a highway to likewise stop motorists using highways in order to determine whether they have met the qualifications prescribed by applicable law for such use. See <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#440" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 440-441</a></span> (1973); <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972). I regard these and similar situations, such <span class="star-pagination">*888</span> as agricultural inspections and highway roadblocks to apprehend known fugitives, as not in any way constitutionally suspect by reason of today's decision.</p>
<p>MR. JUSTICE DOUGLAS, concurring in the judgment.</p>
<p>I join in the affirmance of the judgment. The stopping of respondent's automobile solely because its occupants appeared to be of Mexican ancestry was a patent violation of the Fourth Amendment. I cannot agree, however, with the standard the Court adopts to measure the lawfulness of the officers' action. The Court extends the "suspicion" test of <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to the stop of a moving automobile. I dissented from the adoption of the suspicion test in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> believing it an unjustified weakening of the Fourth Amendment's protection of citizens from arbitrary interference by the police. I remarked then:</p>
<blockquote>"The infringement on personal liberty of any `seizure' of a person can only be `reasonable' under the Fourth Amendment if we require the police to possess `probable cause' before they seize him. Only that line draws a meaningful distinction between an officer's mere inkling and the presence of facts within the officer's personal knowledge which would convince a reasonable man that the person seized has committed, is committing, or is about to commit a particular crime." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#38" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 38</a></span>.</blockquote>
<p>The fears I voiced in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> about the weakening of the Fourth Amendment have regrettably been borne out by subsequent events. Hopes that the suspicion test might be employed only in the pursuit of violent crimea limitation endorsed by some of its proponents<sup>[*]</sup> have now been dashed, as it has been applied <span class="star-pagination">*889</span> in narcotics investigations, in apprehension of "illegal" aliens, and indeed has come to be viewed as a legal construct for the regulation of a general investigatory police power. The suspicion test has been warmly embraced by law enforcement forces and vigorously employed in the cause of crime detection. In criminal cases we see those for whom the initial intrusion led to the discovery of some wrongdoing. But the nature of the test permits the police to interfere as well with a multitude of law-abiding citizens, whose only transgression may be a nonconformist appearance or attitude. As one commentator has remarked:</p>
<blockquote>" `Police power exercised without probable cause <i>is</i> arbitrary. To say that the police may accost citizens at their whim and may detain them upon reasonable suspicion is to say, in reality, that the police may both accost and detain citizens at their whim.' " Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 395 (1974).</blockquote>
<p>The uses to which the suspicion test has been put are illustrated in some of the cases cited in the Court's opinion. In <i>United States</i> v. <i>Wright,</i> <span class="citation" data-id="310273"><a href="/opinion/310273/united-states-v-belmer-lewis-wright-jr/" aria-description="Citation for case: United States v. Belmer Lewis Wright, Jr.">476 F. 2d 1027</a></span> (CA5 1973), for example, immigration officers stopped a station wagon near the border because there was a spare tire in the back seat. The court held that the officers reasonably suspected that the spare wheel well had been freed in order to facilitate the concealment of aliens. In <i>United States</i> v. <i>Bugarin-Cases,</i> <span class="citation" data-id="313456"><a href="/opinion/313456/united-states-v-salvador-bugarin-casas/" aria-description="Citation for case: United States v. Salvador Bugarin-Casas">484 F. 2d 853</a></span> (CA9 1973), the Border Patrol officers encountered a man driving alone in a station wagon which was "riding low"; stopping the car was held reasonable because the officers suspected that aliens might have been hidden beneath the floorboards. The vacationer whose car is weighted down with luggage will find no comfort in these decisions; nor will the many law-abiding citizens <span class="star-pagination">*890</span> who drive older vehicles that ride low because their suspension systems are old or in disrepair. The suspicion test has indeed brought a state of affairs where the police may stop citizens on the highway on the flimsiest of justifications.</p>
<p>The Court does, to be sure, disclaim approval of the particular decisions it cites applying the suspicion test. But by specifying factors to be considered without attempting to explain what combination is necessary to satisfy the test, the Court may actually induce the police to push its language beyond intended limits and to advance as a justification any of the enumerated factors even where its probative significance is negligible.</p>
<p>Ultimately the degree to which the suspicion test actually restrains the police will depend more upon what the Court does henceforth than upon what it says today. If my Brethren mean to give the suspicion test a new bite, I applaud the intention. But in view of the developments since the test was launched in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> I am not optimistic. This is the first decision to invalidate a stop on the basis of the suspicion standard. In fact, since <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> we have granted review of a case applying the test only once, in <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), where the Court found the standard satisfied by the tip from an informant whose credibility was not established and whose information was not shown to be based upon personal knowledge. If in the future the suspicion test is to provide any meaningful restraint of the police, its force must come from vigorous review of its applications, and not alone from the qualifying language of today's opinion. For now, I remain unconvinced that the suspicion test offers significant protection of the "comprehensive right of personal liberty in the face of governmental intrusion," <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#455" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 455</a></span> (1963) (dissenting opinion), that is embodied in the Fourth Amendment.</p>
<h2>NOTES</h2>
<p>[*]  <i>Sanford Jay Rosen</i> filed a brief for the Mexican American Legal Defense and Educational Fund as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  For the Court of Appeals' purposes, the distinction between a roving patrol and a fixed checkpoint was controlling. The court previously had held that the principles of <i>Almeida-Sanchez</i> v. <i>United States</i> applied retrospectively to the activities of roving patrols but not to those of fixed checkpoints. See <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="8894164"><a href="/opinion/8906801/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">500 F. 2d 985</a></span> (CA9 1974), rev'd, <i>ante,</i> p. 531; <i>United States</i> v. <i>Bowen,</i> <span class="citation" data-id="9460842"><a href="/opinion/320688/united-states-v-john-lee-bowen/" aria-description="Citation for case: United States v. John Lee Bowen">500 F. 2d 960</a></span> (CA9 1974), aff'd, <i>post,</i> p. 916.</p>
<p>[2]  There may be room to question whether voluntary testimony of a witness at trial, as opposed to a Government agent's testimony about objects seized or statements overheard, is subject to suppression as the fruit of an illegal search or seizure. See <i>United States</i> v. <i>Guana-Sanchez,</i> <span class="citation" data-id="9459848"><a href="/opinion/313406/united-states-v-pascual-guana-sanchez/" aria-description="Citation for case: United States v. Pascual Guana-Sanchez">484 F. 2d 590</a></span> (CA7 1973), cert, dismissed as improvidently granted, <span class="citation multiple-matches"><a href="/c/U.%20S./420/513/">420 U. S. 513</a></span> (1975). But since the question was not raised in the petition for certiorari, we do not address it.</p>
<p>[3]  We cannot accept respondent's contention that, even though § 287 (a) (3) does not mention probable cause, its legislative history establishes that Congress meant to condition immigration officers' authority to board and search vehicles on probable cause to believe that they contained aliens. The legislative history simply does not support this contention.</p>
<p>[4]  The estimate of one million was produced by the Commissioner of the INS for the Immigration and Nationality Subcommittee of the House Judiciary Committee. Hearings on Illegal Aliens before Subcommittee No. 1 of the House Committee on the Judiciary, 92d Cong., 2d Sess., ser. 13, pt. 5, pp. 1323-1325 (1972). The higher estimate appears in the INS Ann. Rep. iii (1974).</p>
<p>[5]  This estimate tends to be confirmed by the consistently high proportion of Mexican nationals in the number of deportable aliens arrested each year. In 1970, for example, 80% of the deportable aliens arrested were from Mexico. See INS Ann. Rep. 95 (1970). In 1974, the figure was 92%. INS Ann. Rep. 94 (1974).</p>
<p>[6]  In this case the officers did search respondent's car, but because they found no other incriminating evidence the validity of the search is not in issue. <i><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">Almeida-Sanchez</a></span></i> changed the Border Patrol's practice of searching cars on routine stops, and the Government informs us that roving patrols now search vehicles only when they have probable cause to believe they will find illegally present aliens or contraband. Brief for United States 25.</p>
<p>[7]  Because the stop in this case was made without a warrant and the officers made no effort to obtain one, we have no occasion to decide whether a warrant could be issued to stop cars in a designated area on the basis of conditions in the area as a whole and in the absence of reason to suspect that any particular car is carrying aliens. See <i>Almeida-Sanchez,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#275" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S., at 275</a></span> (POWELL, J., concurring); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967).</p>
<p>[8]  Our decision in this case takes into account the special function of the Border Patrol, the importance of the governmental interests in policing the border area, the character of roving-patrol stops, and the availability of alternatives to random stops unsupported by reasonable suspicion. Border Patrol agents have no part in enforcing laws that regulate highway use, and their activities have nothing to do with an inquiry whether motorists and their vehicles are entitled, by virtue of compliance with laws governing highway usage, to be upon the public highways. Our decision thus does not imply that state and local enforcement agencies are without power to conduct such limited stops as are necessary to enforce laws regarding drivers' licenses, vehicle registration, truck weights, and similar matters.</p>
<p>[9]  As noted above, we reserve the question whether Border Patrol officers also may stop persons reasonably believed to be aliens when there is no reason to believe they are illegally in the country. See <i>Cheung Tin Wong</i> v. <i>INS,</i> 152 U. S. App. D. C. 66, <span class="citation" data-id="9458847"><a href="/opinion/306426/cheung-tin-wong-v-united-states-immigration-and-naturalization-service/" aria-description="Citation for case: Cheung Tin Wong v. United States Immigration and...">468 F. 2d 1123</a></span> (1972); <i>Au Yi Lau</i> v. <i>INS,</i> 144 U. S. App. D. C. 147, <span class="citation multiple-matches"><a href="/c/F.%202d/445/217/">445 F. 2d 217</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/864/">404 U. S. 864</a></span> (1971). The facts of this case do not require decision on the point.</p>
<p>[10]  The Courts of Appeals decisions cited throughout this part are merely illustrative. Our citation of them does not imply a view of the merits of particular decisions. Each case must turn on the totality of the particular circumstances.</p>
<p>[11]  The Government also argues that the location of this stop should be considered in deciding whether the officers had adequate reason to stop respondent's car. This appears, however, to be an after-the-fact justification. At trial the officers gave no reason for the stop except the apparent Mexican ancestry of the car's occupants. It is not even clear that the Government presented the broader justification to the Court of Appeals. We therefore decline at this stage of the case to give any weight to the location of the stop.</p>
<p>[12]  The 1970 census and the INS figures for alien registration in 1970 provide the following information about the Mexican-American population in the border States. There were 1,619,064 persons of Mexican origin in Texas, and 200,004 (or 12.4%) of them registered as aliens from Mexico. In New Mexico there were 119,049 persons of Mexican origin, and 10,171 (or 8.5%) registered as aliens. In Arizona there were 239,811 persons of Mexican origin, and 34,075 (or 14.2%) registered as aliens. In California there were 1,857,267 persons of Mexican origin, and 379,951 (or 20.4%) registered as aliens. Bureau of the Census, Subject Report PC (2)-1C: Persons of Spanish Origin 2 (1970); INS Ann Rep. 105 (1970). These figures, of course, do not present the entire picture. The number of registered aliens from Mexico has increased since 1970, INS Ann. Rep. 105 (1974), and we assume that very few illegal immigrants appear in the registration figures. On the other hand, many of the 950,000 other persons of Spanish origin living in these border States, see Bureau of the Census, <i>supra,</i> at 1, may have a physical appearance similar to persons of Mexican origin.</p>
<p>[*]  See LaFave, "Street Encounters" and the Constitution, <span class="citation no-link">67 Mich. L. Rev. 39</span>, 65-66 (1968).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Brinkley.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Brinkley
type: case
citation: "980 F.3d 377 (2020)"
parallel_cite: ""
neutral_cite: ""
court: 4th Cir. 2020
court_level: coa
circuit: ca4
year: 2020
date_decided: 2020-11-13
docket: 18-4455
authority_weight: "Binding in-circuit — 4th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/4805913/united-states-v-kendrick-brinkley/"
  cluster_id: 4805913
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Brinkley
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Arrest in the Home]]"
    role: Key
related:
  - "[[Arrest in the Home]]"
  - "[[Payton v. New York]]"
  - "[[United States v. Watson]]"
  - "[[United States v. Berkowitz]]"
tags:
  - case
  - fourth-amendment
  - arrest
  - warrantless-arrest
  - payton
  - probable-cause
holding: "To enter a home to execute an arrest warrant, officers must have reason to believe — which in the Fourth Circuit means probable cause — both that the home is the suspect's residence and that the suspect is present; an entry supported only by an arrest warrant and uncorroborated hunches about residence and presence is unlawful, so the evidence obtained must be suppressed."
---

# United States v. Brinkley

*980 F.3d 377 (4th Cir. 2020)* (No. 18-4455) · U.S. Court of Appeals for the Fourth Circuit · **Binding in-circuit — 4th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 4805913 → opinion 4586260 (980 F.3d 377, decided 2020-11-13); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In February 2017, a federal-state task force in Charlotte set out to execute an arrest warrant for Kendrick Brinkley, a convicted felon wanted for unlawfully possessing a firearm. Relying only on the arrest warrant — with neither consent nor a search warrant — officers entered the Stoney Trace apartment, a residence they associated with Kayla Chisholm, with whom Brinkley was involved. They found Brinkley inside and seized evidence. Brinkley moved to suppress, explaining that he had been staying at the apartment as Chisholm's overnight guest and did not reside there. The district court denied the motion, and Brinkley entered conditional guilty pleas on two counts arising from the entry.

## Issue
Whether, before entering a home to execute an arrest warrant without consent or a search warrant, the officers had the "reason to believe" *[[Payton v. New York]]* requires — both that the apartment was Brinkley's residence and that he was present inside.

## Rule
Under *[[Payton v. New York|Payton]]*, an arrest warrant carries "the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within," a standard courts apply as a two-prong test — reason to believe both that the home is the suspect's residence and that he will be present. Joining the courts that equate that standard with probable cause, the Fourth Circuit held: "We hold that reasonable belief amounts to probable cause, and that the police in this case lacked reason to believe Brinkley resided in the Stoney Trace apartment and would be present when they entered." — slip op. at 25. Where the suspect may be only a guest, *[[Steagald v. United States]]* requires a separate search warrant.

## Application
The officers rested everything on a single, uncorroborated address linking Brinkley to Chisholm's apartment; that did not establish probable cause that he resided there rather than staying as a guest — a distinction that, under *[[Steagald v. United States|Steagald]]*, would have required a search warrant. And even assuming residence, the officers failed the second prong: generic "signs of life" inside and a resident's understandably nervous reactions, without indicators particular to the suspect, do not amount to probable cause that Brinkley himself was present. Because the entry rested solely on the arrest warrant without the required showing on both prongs, it was unlawful.

## Conclusion
**Reversed, [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]]**: the denial of suppression was reversed and Brinkley's convictions on the two challenged counts [[Reading and Citing Cases#vacated|vacated]]. Motz, J., wrote for the court (Gregory, C.J., joined); Richardson, J., dissented, arguing that *[[Payton v. New York|Payton]]*'s "reason to believe" should not be equated with probable cause.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Brinkley* places the Fourth Circuit among the courts holding that *[[Payton v. New York|Payton]]*'s "reason to believe" means probable cause — deepening an acknowledged circuit split — and reinforces that when officers are uncertain whether their suspect is a resident or merely a guest, *[[Steagald v. United States|Steagald]]* demands a separate search warrant to protect the home's actual occupants.

## Appears on
- [[Arrest in the Home]] — *Key*

## Sources
- [*United States v. Brinkley*, 980 F.3d 377 (4th Cir. 2020)](https://www.courtlistener.com/opinion/4805913/united-states-v-kendrick-brinkley/) — pinpoint: slip op. at 25 (reason-to-believe / probable-cause holding); the CL opinion text carries the slip-opinion page numbers rather than 980 F.3d star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2ec05700316bd91f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Brinkley"}, "payload": {"all": [{"cite": "980 F.3d 377", "page": "377", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "980"}], "display": "980 F.3d 377", "official": {"cite": "980 F.3d 377", "page": "377", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "980"}, "official_selection_present": true, "record_id": "United States v. Brinkley"}}
{"assertion_id": "319b158b8f203875", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Brinkley"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Brinkley", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Brinkley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Brinkley",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Kendrick Brinkley",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Brinkley",
    "court": "4th Cir. 2020",
    "court_id": "ca4",
    "court_level": "coa",
    "circuit": "ca4",
    "state": null,
    "date_decided": "2020-11-13",
    "year": 2020,
    "docket": "18-4455",
    "cluster_id": 4805913,
    "lead_opinion_id": 4586260,
    "sibling_ids": [],
    "absolute_url": "/opinion/4805913/united-states-v-kendrick-brinkley/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "980 F.3d 377",
      "volume": "980",
      "reporter": "F.3d",
      "page": "377",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "980 F.3d 377",
        "volume": "980",
        "reporter": "F.3d",
        "page": "377",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "980 F.3d 377",
    "official_selection": {
      "court_class": "state",
      "selected": "980 F.3d 377",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:50:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-brinkley--4805913",
      "to_record_id": "United States v. Brinkley",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Brinkley

```
                                      PUBLISHED

                       UNITED STATES COURT OF APPEALS
                           FOR THE FOURTH CIRCUIT


                                       No. 18-4455


UNITED STATES OF AMERICA,

                     Plaintiff - Appellee,

              v.

KENDRICK BRINKLEY,

                     Defendant - Appellant.


Appeal from the United States District Court for the Western District of North Carolina, at
Charlotte. Robert J. Conrad, Jr., District Judge. (3:16-cr-00324-RJC-DSC-1)


Argued: January 31, 2020                                    Decided: November 13, 2020


Before GREGORY, Chief Judge, and MOTZ and RICHARDSON, Circuit Judges.


Reversed, vacated, and remanded by published opinion. Judge Motz wrote the opinion, in
which Chief Judge Gregory joined. Judge Richardson wrote a dissenting opinion.


ARGUED: John Parke Davis, FEDERAL DEFENDERS OF WESTERN NORTH
CAROLINA, INC., Charlotte, North Carolina, for Appellant. Amy Elizabeth Ray,
OFFICE OF THE UNITED STATES ATTORNEY, Asheville, North Carolina, for
Appellee. ON BRIEF: Anthony Martinez, Federal Public Defender, OFFICE OF THE
FEDERAL PUBLIC DEFENDER, Charlotte, North Carolina, for Appellant. R. Andrew
Murray, United States Attorney, OFFICE OF THE UNITED STATES ATTORNEY,
Charlotte, North Carolina, for Appellee.
DIANA GRIBBON MOTZ, Circuit Judge:

       To execute an arrest warrant for Kendrick Brinkley, police officers entered a private

home. They had neither consent to do so nor a search warrant. Brinkley appeals the district

court’s denial of his motion to suppress evidence obtained in the home, arguing that the

officers lacked the necessary reason to believe both that he (1) resided in the home and (2)

would be present when they entered. We agree and so must reverse.



                                             I.

       In February 2017, a federal-state task force in Charlotte, North Carolina, sought to

execute outstanding arrest warrants. J.A. 113. Brinkley, then subject to an arrest warrant

for unlawfully possessing a firearm as a convicted felon, was among the targets. J.A. 111.

                                            A.

       Bureau of Alcohol, Tobacco, and Firearms (ATF) Special Agent Jason Murphy

oversaw the operation. J.A. 110–11. An ATF analyst first provided Agent Murphy with

at least two possible addresses. J.A. 125. Because a water bill for one of these addresses

was in Brinkley’s name, Agent Murphy initially believed that address was Brinkley’s most

likely residence. J.A. 125–26. One of the other addresses that the analyst provided was an

apartment on Stoney Trace Drive in Mint Hill, North Carolina, J.A. 64, 125–26; no utility

bill in Brinkley’s name was associated with this address, J.A. 125.

       Charlotte-Mecklenburg Police Department Detective Robert Stark, a member of

Agent Murphy’s task force, also tried to locate Brinkley. J.A. 63–64, 110–11, 125. On

February 2, Detective Stark searched for Brinkley on CJLEADS, a North Carolina

                                             2
statewide law enforcement database. 1 J.A. 64. Detective Stark found multiple addresses

in the database linked to Brinkley. J.A. 64–66, 154. Two CJLEADS entries — one for a

traffic citation, added January 2, J.A. 155–56, and another from the state department of

corrections, added “at some point in January” — were associated with the Stoney Trace

apartment, J.A. 64–65, 68.

       But other CJLEADS entries that Detective Stark found placed Brinkley at numerous

other addresses. J.A. 74, 87. One entry, added five days before the January 2 traffic

citation, provided an address on Planters View Drive. J.A. 88, 154. Another entry, added

a month before that, gave an address on Stone Post Road in Charlotte. J.A. 88, 154. Older

entries, including at least five more from the same year, and others dating further back,

listed the Planters View Drive address and still other addresses. J.A. 74, 154. Detective

Stark did not look into the Planters View Drive address or any of these other addresses.

Rather, “based on the length of time that those addresses had been associated with”

Brinkley, Detective Stark believed that they “were probably family addresses” where

Brinkley did not reside. J.A. 89. But the detective intended to check these other addresses

if Brinkley was not found at the Stoney Trace apartment. J.A. 89.

       Detective Stark then found Brinkley’s public Facebook page. J.A. 72–73. Posts

and photos there led him to believe that Brinkley was dating one Brittany Chisholm. J.A.

73. Detective Stark searched for Chisholm on CJLEADS and found that she was also



       1
         Detective Stark also searched for Brinkley on KBCOPS, an internal police
department reporting system, but there is no indication in the record that he found anything
there. J.A. 64.
                                             3
associated with the Stoney Trace apartment. J.A. 73–74. Based on this information,

Detective Stark concluded that Brinkley lived there with Chisholm. J.A. 75.

       Detective Stark reported his conclusion to Agent Murphy, who came to agree that

Brinkley probably resided in the Stoney Trace apartment. J.A. 111–12, 126. Neither

officer was certain that they had uncovered Brinkley’s address. J.A. 112, 126. Rather, in

Agent Murphy’s experience, it was “common for someone like Mr. Brinkley . . . to have

more than one place where they will stay the night.” J.A. 126.

       The next day, Agent Murphy, Detective Stark, and three other police officers went

to the Stoney Trace apartment to conduct what both Agent Murphy and Detective Stark

characterized as a “knock-and-talk” to “start [their] search for Mr. Brinkley.” J.A. 75–76,

113, 126–27. The officers intended to “interview the occupants to find out if [he] was

indeed there,” and to arrest him if he was. J.A. 75, 113. Agent Murphy acknowledged that

he “had no idea if [Brinkley] was going to be there that morning,” but thought the Stoney

Trace apartment was the “most likely address” to “find Mr. Brinkley or evidence of his

whereabouts.” J.A. 134.

                                            B.

       The five officers arrived at the Stoney Trace apartment around 8:30 AM on Friday,

February 3, all wearing clothing identifying themselves as police officers. J.A. 75–77, 91.

In Agent Murphy’s words, they intended “to basically secure the area and sit up on the

house and wait to see if Mr. Brinkley left.” J.A. 134. Detective Stark knocked on the front

door, and the officers heard movement inside for about a minute. J.A. 77. A woman asked

who was there, and Detective Stark answered that it was the police. J.A. 77. The officers

                                            4
heard movement for another minute until Chisholm, wearing pajamas, slowly opened the

door. J.A. 77, 114.

       Detective Stark informed Chisholm that the officers were looking for Brinkley and

asked to enter the apartment. J.A. 96. Chisholm denied that Brinkley was there. J.A. 78,

96, 115, 128. According to Detective Stark, Chisholm grew “very nervous”; her “body

tensed” and her “breathing quickened,” and she looked back over her shoulder into the

apartment. J.A. 78. The officers saw another woman they did not recognize, but later

identified as Jermica Prigon, wearing pajamas and folding clothes in the living room. J.A.

79, 97, 116. The officers heard movement coming from a room in the back of the

apartment, and both Chisholm and Prigon repeatedly looked back toward that area. J.A.

78–80, 115–16.

       Detective Stark again asked if Brinkley was present and if the officers could enter

to look for him. J.A. 79, 115. He explained that the police “had information that [Brinkley]

was staying at this residence” and “asked for [Chisholm’s] permission . . . to come through

and just do a walk through to make sure that he was indeed not at the residence.” J.A. 115.

Chisholm, still seeming nervous, answered that she did not want the police officers to enter

her apartment and asked if they had a search warrant authorizing them to do so. J.A. 79,

115.

       Detective Stark estimated the entire exchange with Chisholm lasted “a little more

than a minute”; Agent Murphy thought it lasted more than three. J.A. 96–97, 129. Both

testified that based on Chisholm’s demeanor and behavior, Prigon’s presence, the

movement they heard in the back of the apartment, and the morning hour (8:30 AM), they

                                             5
believed Brinkley was inside. J.A. 81, 117, 133. Agent Murphy testified that the sounds

and the women’s reactions led him to believe “100 percent that Mr. Brinkley was hiding

in the apartment.” J.A. 134.

       At this point, the officers decided not to follow the original plan to secure the area

and wait to see if Brinkley left the home. J.A. 134. Instead, Agent Murphy told Chisholm

that he believed she was hiding Brinkley and that the officers were going to enter the

apartment to serve an arrest warrant on him. J.A. 81, 117. Then the five uniformed and

armed officers entered the apartment. J.A. 99. Detective Stark recalled that he probably

entered with his gun drawn; Agent Murphy believed that he did not draw his weapon at

this time. J.A. 81, 117. The officers found Brinkley in a bedroom. J.A. 82, 99, 118. They

arrested and handcuffed him. J.A. 82, 99, 118.

       The officers conducted a protective sweep to check for others hiding in the

apartment. J.A. 82, 99, 119. They did not find anyone else but did see digital scales, a

plastic baggie containing cocaine base, and a bullet. J.A. 83, 105, 119–20, 131. Chisholm

then gave but subsequently revoked verbal consent to search the apartment, so the officers

obtained a search warrant, pursuant to which they seized three firearms and magazines.

J.A. 83–86, 108–09, 120–23, 159.

                                             C.

       A grand jury indicted Brinkley on two felon-in-possession charges under 18 U.S.C.

§ 922(g)(1), one charge of possession with intent to distribute cocaine base under 21 U.S.C.

§ 841(a)(1), and one charge of firearm possession in furtherance of a drug offense under

18 U.S.C. § 924(c)(1)(A). J.A. 8–10. Brinkley moved to suppress the evidence police

                                             6
obtained after entering the Stoney Trace apartment. J.A. 12–15. He denied that he resided

in the apartment and explained that he was staying there as Chisholm’s overnight guest. 2

J.A. 13, 20. Brinkley argued that when the officers entered the apartment, they lacked

reason to believe that he (1) resided in the apartment or (2) would be present there at that

time. J.A. 19–23. The district court denied the motion. J.A. 144.

       Brinkley entered an unconditional guilty plea to one felon-in-possession charge, the

predicate for the arrest warrant. He entered a conditional guilty plea to two other charges

arising from the search of the home, reserving the right to appeal the suppression ruling.

J.A. 220. The district court sentenced Brinkley to 84 months’ imprisonment and three

years’ supervised release on each count, to run concurrently. J.A. 206, 208. Brinkley

timely appealed.

       We review the district court’s legal conclusions — including determinations of

reasonable suspicion and probable cause — de novo, Ornelas v. United States, 517 U.S.

690, 699 (1996), and its factual findings for clear error, construing the facts in the

Government’s favor, United States v. Alston, 941 F.3d 132, 136–37 (4th Cir. 2019).



                                            II.

                                            A.

       The Fourth Amendment protects “[t]he right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures.” U.S.


       2
        Whether as a resident or as an overnight guest, Brinkley has standing to assert a
Fourth Amendment violation. See Minnesota v. Olson, 495 U.S. 91, 98–100 (1990).
                                             7
Const., amend. IV. In most cases, a search or seizure is unreasonable unless authorized by

a warrant. See, e.g., City of Los Angeles v. Patel, 576 U.S. 409, 419 (2015); Katz v. United

States, 389 U.S. 347, 357 (1967). The warrant requirement “ensures that the inferences to

support a search are ‘drawn by a neutral and detached magistrate instead of being judged

by the officer engaged in the often competitive enterprise of ferreting out crime,’” Riley v.

California, 573 U.S. 373, 382 (2014) (quoting Johnson v. United States, 333 U.S. 10, 14

(1948)), and so safeguards “the individual’s interests in protecting his own liberty and the

privacy of his home,” Steagald v. United States, 451 U.S. 204, 212 (1981).

       The warrant requirement carries special force when police seek to enter a private

home, which is “afforded the most stringent Fourth Amendment protection.” United States

v. Martinez-Fuerte, 428 U.S. 543, 561 (1976). “With few exceptions, the question whether

a warrantless search of a home is reasonable and hence constitutional must be answered

no.” Kyllo v. United States, 533 U.S. 27, 31 (2001). But a valid search warrant of course

authorizes police to enter a home.

       In some circumstances, an arrest warrant can also allow officers to enter a home in

order to apprehend a suspect. But the Supreme Court has held that when police officers

seek to enter a home pursuant to an arrest warrant, the Fourth Amendment imposes specific

and different requirements for entry based on whether the home is the suspect’s own

residence or someone else’s.

       When police armed with an arrest warrant seek to enter a suspect’s own home,

Payton v. New York, 445 U.S. 573 (1980), controls. There the Court concluded that “for

Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly

                                             8
carries with it the limited authority to enter a dwelling in which the suspect lives when

there is reason to believe the suspect is within.” Id. at 603. The Payton Court reasoned

that an arrest warrant “will suffice to interpose the magistrate’s determination of probable

cause between the zealous officer and the citizen,” so it is not constitutionally necessary

for officers to seek additional judicial authorization before entering a suspect’s own home

to arrest him. Id. at 602–03.

       But one year later, in Steagald v. United States, 451 U.S. 204, the Court decided

that an arrest warrant alone did not authorize police to enter a third party’s home. The

Court explained that in this situation, unlike in Payton, “two distinct interests” protected

by the Fourth Amendment are at stake: not only “[the suspect’s] interest in being free from

an unreasonable seizure,” but also “[the third party’s] interest in being free from an

unreasonable search.” Id. at 216. While an arrest warrant may adequately protect the

former interest, it does “absolutely nothing to protect [the third party’s] privacy interest in

being free from an unreasonable invasion and search of [her] home.”               Id. at 213.

Consequently, the Steagald Court held that, absent exigent circumstances or consent, the

Fourth Amendment requires police to obtain a search warrant before trying to apprehend

the subject of an arrest warrant in a third party’s home. Id. at 216.

       Because the officers in this case assertedly believed that Brinkley resided in the

Stoney Trace apartment — and entered it pursuant solely to the authority of the arrest

warrant — Payton’s framework applies. We next consider what, exactly, Payton requires.




                                              9
                                             B.

       The courts of appeals have unanimously interpreted Payton’s standard — “reason

to believe the suspect is within,” 445 U.S. at 603 — to require a two-prong test: the officers

must have reason to believe both (1) “that the location is the defendant’s residence” and

(2) “that he [will] be home” when they enter. United States v. Hill, 649 F.3d 258, 262 (4th

Cir. 2011). But the quantum of proof necessary to satisfy Payton has divided the circuits,

with some construing “reason to believe” to demand less than probable cause and others

equating the two standards. See United States v. Vasquez-Algarin, 821 F.3d 467, 474–77

(3d Cir. 2016) (collecting cases).

       In Hill, 649 F.3d 258, we declined to join either camp, reasoning that the police

there had not satisfied even the lower standard. Id. at 263. In this case, however, we cannot

reach a conclusion as to Payton’s first prong — which was not at issue in Hill — without

first determining the quantum of proof that reasonable belief requires, and so we must

answer that question today.

       The courts that interpret reasonable belief to demand less than probable cause have

done so with scant explanation. See Vasquez-Algarin, 821 F.3d at 474. They simply rest

on the logic “that the Supreme Court in Payton used a phrase other than ‘probable cause’

because it meant something other than ‘probable cause.’” United States v. Thomas, 429

F.3d 282, 286 (D.C. Cir. 2005). At first blush, that certainly seems reasonable. But the

courts that have endorsed the view that reasonable belief amounts to probable cause rely

on two more compelling rationales.



                                             10
       The first is that the Supreme Court itself has often used language apparently

equating “reason to believe” with probable cause. See Vasquez-Algarin, 821 F.3d at 475–

78; United States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009); United States v. Hardin,

539 F.3d 404, 416 n.6 (6th Cir. 2008). Years before Payton, for instance, the Court

concluded that “police had probable cause to search [a] car” when observations gave them

“reason to believe that the car was used in the commission of [a] crime.” Cardwell v.

Lewis, 417 U.S. 583, 592 (1974). Similarly, the Court has instructed “that ‘the substance

of all the definitions of probable cause is a reasonable ground for belief of guilt.’”

Maryland v. Pringle, 540 U.S. 366, 371 (2003) (alteration omitted) (quoting Brinegar v.

United States, 338 U.S. 160, 175 (1949)). And strikingly, in Maryland v. Buie, 494 U.S.

325 (1990), the Court used the language of probable cause to find Payton’s reasonable

belief standard satisfied, holding that officers with “an arrest warrant and probable cause

to believe [the suspect] was in his home . . . were entitled to enter and to search” for him

within. Id. at 332–33.

       The second is that, as the Third Circuit reasoned in Vasquez-Algarin, 821 F.3d at

477–80, interpreting Payton’s reasonable belief to amount to probable cause is most

consistent with the special protections that the Constitution affords to the home. The home

has long enjoyed “pride of place in our constitutional jurisprudence.” Id. at 478; see, e.g.,

Florida v. Jardines, 569 U.S. 1, 6 (2013); Silverman v. United States, 365 U.S. 505, 511

(1961). Indeed, Payton itself reiterated that “the physical entry of the home is the chief

evil against which the wording of the Fourth Amendment is directed.” 445 U.S. at 585

(internal quotation marks omitted).

                                             11
       Steagald sheds particular light on how Payton must be interpreted to respect the

home’s privileged status under the Fourth Amendment. As noted above, when officers

armed with an arrest warrant seek to apprehend the suspect in a third party’s home,

Steagald, not Payton, controls, and requires police to obtain a search warrant founded on

probable cause in order to enter the home. But Payton controls when officers believe that

the suspect resides in a certain home, even if they are mistaken. See Vasquez-Algarin, 821

F.3d at 472. Under these circumstances, the home’s actual residents are no longer entitled

to the judicial authorization founded on probable cause that Steagald guarantees; Payton’s

“reason to believe” standard is all that protects their weighty Fourth Amendment privacy

interests. Thus, when police seek to enter a home and are uncertain whether the suspect

resides there, interpreting reasonable belief to require less than probable cause “would

effect an end-run around . . . Steagald and render all private homes . . . susceptible to

search by dint of mere suspicion or uncorroborated information and without the benefit of

any judicial determination.” Id. at 480.

       It seems to us that interpreting reasonable belief to require probable cause hews

most closely to Supreme Court precedent and most faithfully implements the special

protections that the Fourth Amendment affords the home. For these reasons, we join those

courts “that have held that reasonable belief in the Payton context ‘embodies the same

standard of reasonableness inherent in probable cause.’” Id. (quoting United States v.

Gorman, 314 F.3d 1105, 1111 (9th Cir. 2002)).




                                           12
                                             C.

       Applying these requirements here means that before entering the Stoney Trace

apartment without a search warrant, the police needed to have probable cause to believe

that Brinkley resided there and would be present when they entered. See Hill, 649 F.3d at

262. We consider the totality of the circumstances in assessing probable cause. Florida v.

Harris, 568 U.S. 237, 244 (2013). The “quantity and quality” of information known to

officers bear on whether they have probable cause, with less reliable information requiring

more corroboration. See Alabama v. White, 496 U.S. 325, 330 (1990). With these

principles in mind, we turn to Payton’s first prong.



                                            III.

       The police could satisfy Payton’s first prong only if the information known to them

at the time they entered the Stoney Trace apartment provided them with probable cause

that Brinkley resided there — that is, if the information sufficed for a person of reasonable

prudence to believe that Brinkley resided there. See Ornelas, 517 U.S. at 696. In

investigating Brinkley’s residence, Agent Murphy relied exclusively on Detective Stark.

Detective Stark’s conclusion that Brinkley resided in the Stoney Trace apartment rested on

two entries on CJLEADS and Brinkley’s public Facebook.               This information was

somewhat sparse, in that police officers typically rely on considerably more evidence to

establish reasonable belief as to a suspect’s residence. See Vasquez-Algarin, 821 F.3d at

482; Hardin, 539 F.3d at 421–22; see also, e.g., United States v. Hamilton, 819 F.3d 503,

507 (1st Cir. 2016) (police found the defendant’s address in an arrest warrant, postal

                                             13
records, a “public database, booking reports, a National Insurance Crime Bureau accident

report, and credit bureau reports”); United States v. Route, 104 F.3d 59, 61 n.1 (5th Cir.

1997) (police found the defendant’s address in his credit card applications, his car

registration, and an electric and water bill in his name and verified that the defendant

received mail there). Probable cause, however, looks to the totality of the circumstances

and does not require any particular source or kind of information.             Accordingly,

information gleaned from online sources like CJLEADS and Facebook could be enough to

establish probable cause of a suspect’s residence in some situations.

       But here, the information Detective Stark gathered from CJLEADS did not point to

just one address but rather indicated that Brinkley might well be transient. Although the

two most recent entries that the detective found linked Brinkley to the Stoney Trace

apartment, many others — including the two immediately preceding entries, one added just

five days earlier 3 — linked Brinkley to other addresses. J.A. 154. The utility bill in

Brinkley’s name that the ATF analyst initially uncovered was associated with not the

Stoney Trace apartment but a different address. J.A. 125–26. This consistent pattern of


       3
         The dissent calls into question the accuracy of the date associated with this entry,
December 28, 2016. See Dissenting Op. at 39 n.11. But as Detective Stark explained,
“[t]he dates [on CJLEADS] before February 2nd probably would not have changed . . . if
it’s anything more than a month [before February 2nd] it’s probably there and present with
what it was” when Detective Stark first searched for Brinkley on CJLEADS. J.A. 88
(confirming that the entry for Planters View Drive is dated December 28, 2016). Thus, we
do not, as the dissent suggests, look upon the CJLEADS entries “with less-than-expert
eyes” and draw our own conclusions. Dissenting Op. at 38. Rather, we rely on Detective
Stark’s expert knowledge of the database’s inner workings. See id. at 39–40 (observing
that officers like Detective Stark “often review and navigate [CJLEADS] to determine the
date” of “addresses [that] are entered and updated”).

                                             14
inconsistent addresses suggests that Brinkley may have tended to stay temporarily in

various places rather than residing at any one address. In fact, Agent Murphy himself

acknowledged that it was “common for someone like Mr. Brinkley . . . to have more than

one place where they will stay the night from time to time.” 4 J.A. 126.

       But the officers investigated only one place. “[P]olice may rely on the totality of

facts available to them in establishing probable cause,” but they cannot “disregard facts

tending to dissipate probable cause.” Bigford v. Taylor, 834 F.2d 1213, 1218 (5th Cir.

1988); accord Hernandez v. United States, 939 F.3d 191, 201 (2d Cir. 2019). The utility

bill in Brinkley’s name initially led Agent Murphy to believe that Brinkley resided at the

address associated with it, J.A. 125–26 — and with good reason, as utility bills typically

constitute strong evidence of a defendant’s residence. See United States v. Graham, 553

F.3d 6, 13 (1st Cir. 2009). But the officers did not look into this address. Nor did they

look into any of the numerous other addresses Detective Stark found on CJLEADS, even

those listed multiple times. J.A. 154. Had the officers ruled out any of these alternatives,

it could have bolstered their theory that Brinkley resided in the Stoney Trace apartment.

See id. (officers ruled out prior residence); cf. United States v. Young, 835 F.3d 13, 21 (1st

Cir. 2016) (no reasonable belief as to residence even where officers eliminated three other




       4
        Similarly, Detective Stark testified that, based on the CJLEADS entries and other
available information, he believed that Brinkley might be found at multiple addresses. J.A.
89 (explaining that while he “believed that [Brinkley] was staying at Stone Trace Drive,”
he also “believed it might be possible to find him at those other addresses” listed on
CJLEADS). Accordingly, the suggestion that Brinkley might be transient originated not
with us but with both experienced officers.
                                             15
possibilities). But because they did not examine any other possibilities, everything hinged

solely on their investigation into that one address.

       Pursuant to Payton and Steagald, the officers needed to establish reason to believe

not just that Brinkley was staying in the Stoney Trace apartment but that he resided there.

If Brinkley was merely staying as a guest in someone else’s home, Steagald would require

the officers to obtain a search warrant before they could enter it. Detective Stark’s

discovery that Brinkley was involved with Chisholm, and that Chisholm was associated

with the Stoney Trace apartment, certainly provided additional evidence that Brinkley

might well have stayed at Chisholm’s home, but it did not speak to whether he did so as a

resident or as Chisholm’s overnight guest. See United States v. Werra, 638 F.3d 326, 338

(1st Cir. 2011). Further investigation was necessary to establish probable cause that

Brinkley resided there. 5

       Police often conduct such further investigation by going to the suspected residence,

where they can obtain “recent, eyewitness evidence connecting the suspect to the residence,

and often even [observe] conduct by the suspect that demonstrates a tie to the residence” —


       5
         The dissent, which repeatedly refers to Chisholm as Brinkley’s “fiancée,”
Dissenting Op. at 35, 44, contends that Detective Stark “believed” that Chisholm and
Brinkley were “living together before marriage” on Stoney Trace Drive, id. at 41. This
contention finds scant support in the record. Detective Stark did refer to a single
photograph on Brinkley’s Facebook page in which Brinkley “appeared to be engaged” to
Chisholm, but in the next sentence of his testimony, the detective explained that he
“believed they were in a dating relationship.” J.A. 73. (emphasis added). All other
testimony by the officers, and even submissions by the Government, either describe
Chisholm and Brinkley as “boyfriend and girlfriend,” J.A. 111, 158, or “dating,” J.A. 26,
75, 89, 133, 142. Nothing in the record supports the dissent’s claim that the officers
“believed” that Brinkley and Chisholm were “living together before marriage.” Dissenting
Op. at 41.
                                             16
“common feature[s]” of cases finding that police satisfied Payton’s first prong. Hardin,

539 F.3d at 421. Officers gather this kind of evidence, for example, by conducting

surveillance at the suspected residence. See Hamilton, 819 F.3d at 505 (“police installed a

pole camera on [the street outside the residence] for surveillance purposes”); United States

v. Barrera, 464 F.3d 496, 498–99 (5th Cir. 2006) (officers found three vehicles associated

with the suspect at the residence). They also talk to people at or near the residence to gather

information from them. See Graham, 553 F.3d at 13 (police corroborated an address from

an incident report by, inter alia, showing a picture of the suspect to a person outside the

residence); Hardin, 539 F.3d at 407 (officers asked property manager who leased the

apartment in question); United States v. Lovelock, 170 F.3d 339, 344–45 (2d Cir. 1999)

(police confirmed address listed on suspect’s arrest warrant with two tenants in building).

In short, going to the residence in question opens several possible avenues for the police to

gather information about whether the suspect in fact resides there.

       The officers in this case explained that they went to the Stoney Trace apartment with

precisely this investigatory intent in mind. Detective Stark testified that they planned to

conduct a “knock-and-talk” at the door of the apartment. J.A. 76. Agent Murphy

confirmed that their intent in doing so “was to interview the occupants to find out if Mr.

Brinkley was indeed there.” J.A. 113. He further explained that when the officers began

speaking with Chisholm at the doorstep, he still intended “to basically secure the area and

sit up on the house and wait to see if Mr. Brinkley left.” J.A. 134. And when the officers

doubted Chisholm’s assertion that Brinkley was not inside, Detective Stark “asked for her



                                              17
permission . . . to come through and just do a walk through to make sure that he was indeed

not at the residence.” J.A. 115.

       That the officers went to the apartment to obtain more information to establish that

Brinkley resided there underscores that at the time of their arrival, they had a “limited basis

to believe” that he did. Vasquez-Algarin, 821 F.3d at 481. On the doorstep of the

apartment, the police officers did talk to an occupant, but they gathered no evidence as to

whether this was Brinkley’s residence. 6 The police officers did not even ask Chisholm if

Brinkley resided there, but only if he was present — a critical difference under Steagald.

The unexpected arrival of five armed officers apparently led Chisholm to grow nervous as

they pressed her to allow them to enter. And the officers heard someone, or something,

moving inside. But these facts did not establish that Brinkley resided in the home. At the

time they entered the Stoney Trace apartment, all the officers had was the same “limited

basis to believe” that Brinkley resided there that they had when they knocked on the door.

       Of course, “the police need not possess . . . rock-solid indicators of residence in

order to form a ‘reasonable belief’ that a suspect resides at a given place.” Graham, 553

F.3d at 13. But we have seen no case finding Payton’s first prong satisfied on evidence as

thin as the evidence here. The information known to the officers suggested that Brinkley

may have stayed temporarily in several places. The officers, however, investigated only



       6
        If anything, the information they learned raised more questions about whether
Brinkley resided there than it answered. For the officers found not just Chisholm but also
Prigon, a woman completely foreign to them, folding laundry in pajamas, as a resident
would.

                                              18
one. Though the officers developed a well-founded suspicion that Brinkley might have

stayed in the Stoney Trace apartment at times, they failed to establish probable cause that

he resided there. And because the officers entered the apartment pursuant solely to the

authority of the arrest warrant, under Payton and its progeny, their entry was unlawful. 7



                                            IV.

       Even if the available information were enough to give police reason to believe that

Brinkley resided in the Stoney Trace apartment and so satisfy Payton’s first prong, the

evidence here falls far short of satisfying Payton’s second; that is, the officers failed to

establish probable cause that Brinkley would be present in the home when they entered.

       In determining reasonable belief as to a suspect’s presence, courts assess the signs

of presence known to officers before they enter a home. See Graham, 553 F.3d at 14.

Though we now know that the officers’ belief that Brinkley would be present proved to be


       7
         Our determination that the officers failed to establish probable cause in no way
denigrates their years of experience. Nor does it suggest that we have not given “due
weight” to the “reasonable inferences” they drew “in light of [their] experience.” Terry v.
Ohio, 392 U.S. 1, 27 (1968); accord Ornelas, 517 U.S. at 699. But experience does not
establish probable cause. See 2 Wayne R. LaFave, Search & Seizure § 3.2(c) (6th ed. 2020)
(observing that “experience, without more, is not a fact to be added to the quantum of
evidence to determine if probable cause exists, but rather a lens through which courts view
the quantum of evidence”) (quotation marks and emphasis omitted). Experienced officers
like Agent Murphy and Detective Stark may not render the probable cause requirement a
“toothless tiger” through reliance on “cop-on-the-beat intuition[s].” United States v.
Rutkowski, 877 F.2d 139, 142 (1st Cir. 1989). Rather, their actions — like those of all law
enforcement officers — must be “judged against an objective standard” with a familiar
lodestar: whether the available information sufficed for a “man of reasonable caution” to
believe that the search was warranted. Terry, 392 U.S. at 22. Contrary to the dissent’s
intimations, Dissenting Op. at 42, even experienced officers may sometimes fail to meet
this standard.
                                            19
correct, the Fourth Amendment demands that we “prevent hindsight from coloring the

evaluation of the reasonableness of a search or seizure.” Martinez-Fuerte, 428 U.S. at 565.

       The Government points to six factors assertedly supporting the officers’ belief that

Brinkley would be present in the Stoney Trace apartment: (1) the officers’ purportedly

reasonable belief that he resided there; (2) the morning hour (8:30 AM); (3) Chisholm’s

delay in opening the door; (4) Chisholm’s nervousness; (5) the sounds of movement in the

apartment; and (6) Chisholm and Prigon’s looks toward the back of the apartment.

Response Br. at 26–28.

       A substantiated belief as to a suspect’s residence is especially important. See Werra,

638 F.3d at 340 (“The fact that an individual is known to live at a particular location is one

sound reason to expect him or her to be there.”). But an ill-founded belief about a suspect’s

residence does not, and cannot, shore up a belief about his presence there. In Hill, for

instance, we noted that police went to the defendant’s suspected residence “to gain

information” and “had documented another primary residence” for the defendant, and we

discounted the probative value of other indicia of the defendant’s presence accordingly.

649 F.3d at 264. Here, too, the officers went to the Stoney Trace apartment to gather more

information. J.A. 89, 113. Moreover, while in Hill the police knew of only one other

possible primary residence, in this case the officers had documented multiple other possible

primary residences for Brinkley. Unlike in Hill, where the defendant’s girlfriend told

police that the defendant resided in the home that the officers entered, id. at 261 — and the

defendant himself had previously told an officer that he had recently moved to the city



                                             20
where the home was located, id. — police here had no firsthand information about where

Brinkley resided.

       The officers’ uncertainty as to Brinkley’s residence undermines the evidentiary

strength of any possible signs of his presence. See Werra, 638 F.3d at 339 (discounting

the probative value of time-of-day evidence for this reason). When police know a suspect

lives somewhere, generic indicia of presence may suggest that he is there, but when police

are uncertain about where he lives, the same signs suggest only that someone is there —

not necessarily the suspect. In this case, counting the officers’ investigation into whether

Brinkley resided in the Stoney Trace apartment as evidence that he would be found inside

would condone “bootstrapping,” allowing police to establish reasonable belief of presence

by poking around a suspected residence until they find “mere signs of life inside.”

Vasquez-Algarin, 821 F.3d at 482. With the officers’ uncertainty about where Brinkley

resided in mind, we look to the other factors to determine whether they established probable

cause that he would be present.

       The hour and Chisholm’s delay in opening the door offer meager support for the

officers’ belief under these circumstances.      It may be reasonable to assume that an

unemployed person would be home at 8:30 AM. See United States v. Magluta, 44 F.3d

1530, 1536 (11th Cir. 1995); United States v. Lauter, 57 F.3d 212, 215 (2d Cir. 1995). But

here the officers did not know whether Brinkley was employed; Agent Murphy

acknowledged that Brinkley might not have been home at 8:30 AM because “[h]e may

have gone to work.” J.A. 134. Cf. Werra, 638 F.3d at 340 (not reasonable to assume

suspect would be home at 10:00 AM without information about her employment status).

                                            21
And as to the purported delay, Detective Stark testified that Chisholm answered the door

no more than two minutes after the officers knocked. J.A. 77. Two minutes is not an

unusual amount of time for a woman, in her pajamas, to respond to an unanticipated knock,

at 8:30 AM. We do not evaluate the totality of the circumstances by running through a list

of factors and ticking off each individually. See Harris, 568 U.S. at 244. But viewing both

of these factors in tandem with the others, we cannot see how they support probable cause

to believe that Brinkley was present in the apartment.

       We are left with the noises in the apartment and Chisholm and Prigon’s reactions to

them and to the police officers. Unlike the “unresponsive noises” in Hill, “which could

have been voices or a television,” 649 F.3d at 264, the sounds of active movement here at

least indicated that some living being was present. But as in Hill, these sounds were not

particularized to the suspect; “at best, the police had reason to believe that someone was

present.” Id. (emphasis added). The same goes for Chisholm and Prigon looking toward

the source of the noises. Their looks toward the back of the apartment were typical

reactions to any source of noises. The noises could have been made by anyone, including

a child (and police knew that children might be present in the apartment, J.A. 90, 127) or a

grandparent, or even a pet. Prigon’s unanticipated presence accentuates the point: the

officers observed one entirely unexpected person in the apartment before they entered, and

they had no reason to think that the noises came from Brinkley rather than some other

unknown person.

       The only evidence that someone was present that was even arguably particularized

to Brinkley was Chisholm’s nervousness. But “[i]t is common for most people to exhibit

                                            22
signs of nervousness when confronted by a law enforcement officer whether or not the

person is currently engaged in criminal activity.” United States v. Massenburg, 654 F.3d

480, 490 (4th Cir. 2011) (alteration omitted) (quoting United States v. Salzano, 158 F.3d

1107, 1113 (10th Cir. 1998)). Here Chisholm was confronted by five armed officers

crowding the door to her apartment. The Government nonetheless insists that Chisholm’s

nervousness was a response to the officers’ questions about Brinkley. But police here did

not merely ask if Brinkley was inside or where he might be. From their very first question,

the officers conveyed their intent to enter the apartment. J.A. 96, 128. Throughout the

conversation, they consistently pressed Chisholm to permit them to enter the apartment.

J.A. 79, 115. Chisholm could have been nervous at the prospect of exposing any number

of people — for example, an elderly parent or a young child — to five armed policemen.

       Chisholm might also have feared for herself. Recent events have underscored how

quickly police encounters with Black Americans may escalate, at times fatally. See Estate

of Jones v. City of Martinsburg, 961 F.3d 661, 673 (4th Cir. 2020). 8 “[W]e recognize that

our police officers are often asked to make split-second decisions,” id., and we respect the


       8
         Two months after this case was argued, police in Louisville, Kentucky, barged into
the home of Breonna Taylor, a 26-year-old emergency medical technician. The officers
entered Taylor’s home pursuant to a search warrant, which they obtained to investigate a
suspected drug dealer who was purportedly associated with the residence. See Tessa
Duvall & Darcy Costello, Louisville Police Pursued “No-Knock” Search Warrant in Fatal
Shooting of ER Tech in Her Home, Louisville Courier J. (June 9, 2020), https://
www.courier-journal.com/story/news/2020/05/12/breonna-taylor-louisville-emt-not-main-
target-drug-investigation/3115928001/ [https://perma.cc/3UGF-XQHA]. The officers
found neither the suspect nor any drugs in the home, but they shot Taylor eight times,
killing her. And this tragedy is hardly an anomaly. See, e.g., Kimberlé Crenshaw, “You
Promised You Wouldn’t Kill Me,” N.Y. Times (Oct. 28, 2019), https://www.nytimes.com/
2019/10/28/opinion/police-black-women-racism.html [https://perma.cc/6QRN-KUHL].
                                            23
challenges that law enforcement officers face in the service of our communities. But we

cannot ignore this context when making sense of how someone reacted to five armed

officers at her door. That would make anyone nervous — including Chisholm, whether

Brinkley was inside the apartment or not. And we cannot conclude that Chisholm’s

understandable response gave rise to probable cause that Brinkley was present within.

       To the contrary, Chisholm’s reluctance to allow the officers to enter her home

without a warrant to do so goes to the “very core” of the Fourth Amendment: “the right of

a man to retreat into his own home and there be free from unreasonable governmental

intrusion.” Silverman, 365 U.S. at 511. That right would not mean much if all officers

needed to enter a private home was a hunch about a suspect’s presence and a resident’s

understandably nervous reaction to the officers’ questioning. Cf. Jardines, 569 U.S. at 6

(“This right would be of little practical value if the State’s agents could stand in a home’s

porch or side garden and trawl for evidence with impunity . . . .”).

       Like Hill, 649 F.3d at 260, this case is ultimately about the “centuries-old principle

of respect for the privacy of the home.” Wilson v. Layne, 526 U.S. 603, 610 (1999). In

recognition of this constitutionally enshrined principle, “law enforcement officers often

rely on independent investigation and observations of the premises to determine whether a

suspect is actually inside before entering.” El Bey v. Roop, 530 F.3d 407, 417 (6th Cir.

2008). But police here conducted no independent investigation or observation of the

Stoney Trace apartment to determine whether Brinkley was within. They stacked a hunch

about Chisholm’s nervousness atop a hunch about Brinkley’s residence.



                                             24
       When police have limited reason to believe a suspect resides in a home, generic

signs of life inside and understandably nervous reactions from residents, without more, do

not amount to probable cause that the suspect is present within. This conclusion follows

from Hill, which for the sake of argument applied the less demanding interpretation of

reasonable belief and found even that not met. 649 F.3d at 263. If police could not satisfy

that lower standard with generic signs of life coming from a suspect’s known residence,

they surely cannot establish probable cause that a suspect is present based on generic signs

of life coming from a potential but uncorroborated residence. All of the facts the officers

in this case relied on, viewed together, did not give rise to reason to believe that Brinkley

would be present in the Stoney Trace apartment when they entered. To hold otherwise

would gut “the most stringent Fourth Amendment protection” that “private dwellings [are]

ordinarily afforded.” Martinez-Fuerte, 428 U.S. at 561.

                                             V.

       We hold that reasonable belief amounts to probable cause, and that the police in this

case lacked reason to believe Brinkley resided in the Stoney Trace apartment and would

be present when they entered. The Fourth Amendment requires a more rigorous showing

of cause before officers may lawfully enter a private home under these circumstances.

        Accordingly, we reverse the district court’s denial of Brinkley’s suppression

motion and vacate Brinkley’s convictions on the two counts at issue. We also vacate

Brinkley’s sentence, see United States v. Pratt, 915 F.3d 266, 275 (4th Cir. 2019), and we

remand the case for further proceedings consistent with this opinion.

                                              REVERSED, VACATED, AND REMANDED

                                             25
RICHARDSON, Circuit Judge, dissenting:

       If equipped with an arrest warrant “founded on probable cause,” officers have “the

limited authority to enter a dwelling in which the suspect lives when there is reason to

believe the suspect is within.” Payton v. New York, 445 U.S. 573, 603 (1980) (emphasis

added). Though the Supreme Court used the phrase “reason to believe,” my colleagues in

the majority hold that officers must have “probable cause to believe that [the suspect]

resided [at the dwelling] and would be present when they entered.” Majority Op. 13

(emphasis added). This divergence from what the Supreme Court said is not without some

support. But I would follow the words used in Payton until I am told otherwise.

       And yet, the majority did not need to wade into this morass. Whatever the standard,

the officers here had enough to enter an apartment to arrest Kendrick Brinkley. Those

experienced officers made reasonable inferences that deserve our respect. Rather than

respecting those inferences and the district court who agreed with them, the majority

invents its own inferences with little support from a database with which judges have

precious little experience. I respectfully dissent.

I.     Background

       Experienced law enforcement, state and federal, 1 sought to arrest Brinkley on an

outstanding arrest warrant. To find him, they turned to a North Carolina law-enforcement

database, Criminal Justice Law Enforcement Automated Data Services (CJLEADS).



       1
         Detective Robert Stark had served as a police officer for twelve years. J.A. 63.
Special Agent Jason Murphy had worked for the ATF for nine years and had served in
other law-enforcement positions for more than seven years before that. J.A. 110.
                                              26
Using that information, along with court records and Facebook, the officers identified

Brinkley’s most probable residence as being an apartment on Stoney Trace Drive.

       The two most recent records in CJLEADS linked Brinkley to the Stoney Trace

address. The first record, from just a month earlier, involved a “ticket citation issued [to

Brinkley] for driving while [his] license [was] revoked.” J.A. 65. Cross-referencing the

North Carolina Courts’ system confirmed that Brinkley had provided the Stoney Trace

address during the traffic stop. A second record, this one from the Department of

Corrections, linked Brinkley to the Stoney Trace address. From this record, the officer

concluded that Brinkley gave the Stoney Trace address to his probation officer “as Mr.

Brinkley was on probation at the time.” J.A. 65. And Brinkley’s own counsel agreed this

second address was the “probation office[’s] indication that that was his residence.” J.A.

137. So it was no surprise that the district court found that Stoney Trace was the “place

that [Brinkley] gave as a residence.” J.A. 145; see also J.A. 144 (concluding that the

database provided “indicators of Mr. Brinkley giving that as an address, recent in time”)

       The Stoney Trace address that Brinkley provided was corroborated by information

from Facebook. Brinkley’s Facebook page showed that Brinkley was engaged to or dating

Brittany Chisholm. CJLEADS identified Chisholm’s address as the same Stoney Trace

address, which the officers felt helped confirm that Brinkley resided there. The district

court agreed.

       Considering this information together, the lead officers (Detective Stark and Special

Agent Murphy) concluded that Brinkley “was residing at the Stoney Trace address.” J.A.

74–75. While other addresses “had been provided over a number of years . . . [t]hey

                                            27
appeared [to Detective Stark] to be family-associated addresses.” J.A. 74. As one officer

explained, the law-enforcement database had no other addresses “within the [prior] year

that [they] felt w[ere] credible as a place [Brinkley] was living.” J.A. 112–113, 126.

       Having concluded that Brinkley likely resided on Stoney Trace, the officers went

“to interview the occupants to find out if Mr. Brinkley was indeed there.” J.A. 113. After

arriving around 8:30am, they knocked on the front door wearing clothing identifying

themselves as law enforcement. After hearing movement inside for “just about a minute,”

they knocked “a few more times and announced ‘police’” because “nobody was coming to

the door.” J.A. 77, 114. Eventually, a female voice asked who was there, and the officers

responded that it was the police. After another “minute’s worth of movement,” a pajama-

clad Chisholm “opened [the front door] slowly” to about “[a] full body length wide” so

that Detective Stark “could see all the way inside the apartment.” J.A. 77.

       When asked if Brinkley was inside, Chisholm “became very nervous. Her body

tensed. Her breathing quickened. She looked back into the apartment and said, ‘He’s not

here.’” J.A. 78. She “looked back over her shoulder . . . multiple times.” J.A. 78. When

told that the officers were there to serve an arrest warrant for Brinkley, “Chisholm become

more and more . . . nervous . . . constantly looking behind her, stammering, [ ] never really

giv[ing] full answers.” J.A. 115.

       While talking to Chisholm, the officers could hear movement coming from the

bedroom area. J.A. 79, 115–16. A second woman, later identified as Jermica Prigon,

crossed from the kitchen to the living room in her pajamas and appeared to be “messing

with [ ] folding clothes or something.” J.A. 79, 116. When another noise came from the

                                             28
bedroom area, the officers saw Prigon “snap[] her head back towards that area to look.”

J.A. 116. And each time the officers told Chisholm that they believed Brinkley was inside,

she “would kind of do . . . a subconscious . . . look back over her shoulder towards the back

of the apartment.” J.A. 117.

       Based on the noise from the bedroom area, Chisholm’s movement and demeanor,

Prigon’s actions, and the time of day, the officers “believed . . . 100 percent that Mr.

Brinkley was hiding in the apartment.” J.A. 134; see also J.A. 81, 117.

       The officers then entered the apartment and, unsurprisingly, found Brinkley in the

bedroom’s hallway. A protective sweep revealed digital scales, a plastic baggie with

suspected crack cocaine, and ammunition in a clear box. After obtaining a search warrant,

the officers also found three guns.

       After Brinkley was indicted, he sought to suppress the seized evidence. The district

court held a hearing and found that the officers reasonably believed that Brinkley lived at

the Stoney Trace address and that he was there when they entered. The district court based

its conclusion on: (1) Detective Stark’s CJLEADS and Facebook research, (2) Chisholm’s

“nervousness” which “[c]ould be explained by the fact that law enforcement was at the

door” but “also [was] highly likely to be connected to . . . [the fact that] they were looking

for Mr. Brinkley,” (3) Chisholm’s demeanor and constant looking back, (4) Prigon’s

looking back toward the bedroom, (5) the noise inside the apartment and the “two women

looking back at the direction of the noise,” (6) Detective Stark recognizing Chisholm as

Brinkley’s girlfriend, tying “Chisholm to that address, and [tying] the defendant” to it, and



                                             29
(7) that the officers were there “early in the morning on a week day when a resident would

likely be at home.” J.A. 144–47.

II.    Legal Framework

       As the majority points out, “a private home . . . is ‘afforded the most stringent Fourth

Amendment protection.’” Majority Op. 8 (quoting United States v. Martinez-Fuerte, 428

U.S. 543, 561 (1976)). That said, officers seeking to execute an arrest warrant may “enter

a dwelling in which [a] suspect lives when there is reason to believe the suspect is within.”

Payton, 445 U.S. at 603 (emphasis added). Courts have disagreed on what the Supreme

Court meant when it said “reason to believe.” Is “reason to believe” the same as “probable

cause,” as the majority suggests? Or does “reason to believe” merely require a “reasonable

belief,” which may be less than probable cause to believe? 2

       One might read inconsistency into the Supreme Court’s use of the terms “reason to

believe” or “reasonable belief.” As the majority points out, there is some language in

Supreme Court opinions that could be read to equate “reason to believe” with “probable

cause.” See Majority Op. 11 (citing Maryland v. Pringle, 540 U.S. 366, 371 (2003);


       2
         Some circuits have equated “reason to believe” and “probable cause.” See United
States v. Vasquez-Algarin, 821 F.3d 467, 480 (3d Cir. 2016); United States v. Gorman, 314
F.3d 1105, 1111 (9th Cir. 2002). Others have suggested the same in dicta. See United
States v. Jackson, 576 F.3d 465, 469 (7th Cir. 2009); United States v. Hardin, 539 F.3d
404, 416 n.6 (6th Cir. 2008). On the other hand, some circuits have found that the “reason
to believe” standard is less stringent than the “probable cause” standard. See United States
v. Thomas, 429 F.3d 282, 286 (D.C. Cir. 2005); Valdez v. McPheters, 172 F.3d 1220, 1225
n.5 (10th Cir. 1999); United States v. Lauter, 57 F.3d 212, 215 (2d Cir. 1995); United States
v. Werra, 638 F.3d 326, 337 (1st Cir. 2011). And still others have side-stepped the
problem. See United States v. Barrera, 464 F.3d 496, 501 n.5 (5th Cir. 2006); United States
v. Risse, 83 F.3d 212, 216 (8th Cir. 1996); United States v. Magluta, 44 F.3d 1530, 1535
(11th Cir. 1995).
                                              30
Cardwell v. Lewis, 417 U.S. 583, 592 (1974)). But other times, the Supreme Court more

plainly equates “reason to believe” with “reasonable suspicion.” See Terry v. Ohio, 392

U.S. 1, 27 (1968) (An officer may conduct a reasonable search “where he has reason to

believe that he is dealing with an armed and dangerous individual, regardless of whether

he has probable cause to arrest.”). Compare Maryland v. Buie, 494 U.S. 325, 337 (1990)

(A protective sweep is permitted when a “reasonable belief” exists that an area harbors a

dangerous individual (emphasis added)), with id. at 335–36 (“The sweep lasts no longer

than is necessary to dispel the reasonable suspicion of danger.” (emphasis added)).

      As an inferior court judge, I must follow the Supreme Court’s guidance. And

although we are left with few tools to reconcile the Supreme Court’s cases in this area,

what we have leads me to conclude that “reason to believe” means a “reasonable belief,”

which is equivalent to “reasonable suspicion.” First, Payton itself sets the standard as

“reason to believe the suspect is within.” Payton, 445 U.S. at 603. The Supreme Court

chose not to use the phrase “probable cause,” a phrase it knows how to use. Instead, the

Court used “reason to believe,” the same phrase it used in Terry, the seminal case on

reasonable suspicion. Terry, 392 U.S. at 27. 3 Second, in Buie, a case that the majority

relies on, the Supreme Court differentiates “reasonable belief” from “probable cause” by



      3
         If “reason to believe,” as Terry uses it, meant “probable cause,” then “reasonable
suspicion” would mean “probable cause.” And yet the Supreme Court has been clear that
Terry’s standard is “obviously less than is necessary for probable cause.” See Kansas v.
Glover, 140 S. Ct. 1183, 1187 (2020) (quoting Prado Navarette v. California, 572 U.S.
393, 397 (2014)).


                                            31
admonishing the Maryland court for requiring the higher probable cause standard and

demanding that it instead use the “reasonable belief” standard. See Buie, 494 U.S. at 336–

37. 4 I think it a more faithful reading of Payton to adhere to the words the Court used,

rather than words they did not. 5

III.   A “Reason to Believe” Existed

       But the dispute over what the Supreme Court meant when they used “reason to

believe,” at least here, should be academic. However one understands a “reason to

believe,” the officers had it here. Drawing on their experience, the officers drew inferences

from the information they had to conclude that Brinkley resided on Stoney Trace. And




       4
         The majority instead relies on Buie’s descriptive phrase that the officers possessed
“an arrest warrant and probable cause to believe Buie was in his home.” 494 U.S. at 332–
33 (emphasis added); see Majority Op. 11. This single sentence reflects only that the
Supreme Court believed that there was in fact “probable cause to believe Buie was in his
home.” See Buie v. State, 550 A.2d 79, 80 (Md. 1988) (explaining that the police were
surveilling Buie’s house and had placed a phone call to confirm he was there before
entering under an arrest warrant). The Supreme Court did not make a broader statement
that Payton required probable cause, particularly since Buie did not address the authority
of officers to enter a home pursuant to an arrest warrant.
       5
         I understand the majority to be concerned that reading Payton to permit warrantless
entries into homes with less knowledge than probable cause might “render all private
homes . . . susceptible to search by dint of mere suspicion or uncorroborated information
and without the benefit of any judicial determination.” Majority Op. 12 (quoting Vasquez-
Algarin, 821 F.3d at 480). But the majority creates a straw man, as “mere suspicion or
uncorroborated information” is far from how this Court has defined “reasonable belief.”
Instead, as the majority fails to recognize, “[a]n objectively reasonable belief,” although a
quantum of proof less than probable cause, still “must be based on specific articulable facts
and reasonable inferences that could have been drawn therefrom.” United States v. Yengel,
711 F.3d 392, 397 (4th Cir. 2012). This is worlds away from a “dint of mere suspicion”
that the majority has characterized the “reason to believe” standard as requiring. Majority
Op. 12 (quoting Vazquez-Algarin, 821 F.3d at 480).
                                             32
once at the residence, the circumstances provided a reason to believe that Brinkley was

home.

        Even using the majority’s probable-cause standard, the officers had “probable cause

to believe that Brinkley” (1) “resided [at the Stoney Trace address],” and (2) “would be

present when they entered.” Majority Op. 13. The majority disagrees. But in conducting

their analysis, the majority fails to give due weight to the inferences made by experienced

officers based on information in a law-enforcement database, a source that we as appellate

judges lack significant experience in interpreting.

        Probable cause is not weighed “in terms of library analysis by scholars, but as

understood by those versed in the field of law enforcement.” United States v. Dickey-Bey,

393 F.3d 449, 453 (4th Cir. 2004) (emphasis added) (quoting Illinois v. Gates, 462 U.S.

213, 232 (1983)). This last part is important. In determining whether probable cause exists,

this Court must use a “pragmatic, common sense approach, [ ] defer[ring] to the expertise

and experience of law enforcement officers at the scene.” Id. (citing Ornelas v. United

States, 517 U.S. 690, 699 (1996)). And we are to give “due weight to inferences drawn

from [the] facts by resident judges,” who, like local officers, “view[] the facts of a particular

case in light of the distinctive features and events of the community.” Ornelas, 517 U.S.

at 699. “The most precise instrument that the judiciary possesses for ensuring the proper

balance between the interests that under-gird the Fourth Amendment is the on-the-ground

assessment of district courts.” United States v. Bumpers, 705 F.3d 168, 173 (4th Cir. 2013).

Local officers and local judges are in a better position, based on their experience in their

own communities, to make logical inferences from facts on the ground. Ornelas, 517 U.S.

                                               33
at 699. And when a resident judge agrees with the officers, we should be particularly

cautious about rejecting the agreed-upon inferences. 6

       The majority errs by rejecting law enforcement’s inferences and replacing them with

its own inferences drawn from a sliver of information. And, in doing so, the majority fails

to “construe the evidence in the light most favorable to the Government, the prevailing

party below,” as we must do. United States v. Seidman, 156 F.3d 542, 547 (4th Cir. 1998).

       A.     The officers had probable cause to believe Brinkley resided at the Stoney
              Trace address

       The information known and the inferences made by these experienced officers

provided probable cause that Brinkley resided at the Stoney Trace address. See J.A. 89,

134. And the information developed when officers visited that address only confirmed that

reasonable belief.

       Detective Stark testified that the two most recent CJLEADS results pointed to the

Stoney Trace address as Brinkley’s residence. That address had been provided once to an

officer and once to the Department of Corrections. And it was new. This led Detective



       6
         This does not mean that we defer to local law enforcement’s subjective belief that
probable cause exists. United States v. Gray, 137 F.3d 765, 769 (4th Cir. 1998). That
subjective belief is owed no deference. But the underlying inferences they make from the
facts are entitled to deference. And again, this is not controlling weight: after all, “while
officers have the advantage of experience, they do not necessarily have the advantage of
neutrality.” United States v. Johnson, 599 F.3d 339, 343 (4th Cir. 2010). But, “that is
where the district courts come in.” Id. And local district courts’ neutral inferences are to
be given not controlling, but “due weight,” at least as to their “finding[s] that [an] officer
was credible and the inference[s made were] reasonable.” Ornelas, 517 U.S. at 700. This
proposition is “an acknowledgement that satellite imagery often cannot replicate
community insights and on-the-ground intelligence.” Johnson, 599 F.3d at 344.

                                             34
Stark to believe that this address was not a “family-associated address[],” but his current

residence. J.A. 74. And this inference was supported by Brinkley’s fiancée’s link to that

address.

       Detective Stark made several inferences based on his experience in concluding that

the Stoney Trace address was Brinkley’s residence. First, Brinkley gave those supervising

his probation the Stoney Trace address as his residence. J.A. 65, 137. 7 Second, Brinkley

gave the Stoney Trace address as his residence to an officer during a traffic stop. J.A. 65.

Third, older addresses in the database were likely “family-associated addresses,” not

Brinkley’s current residence. J.A. 74. Fourth, it is common for someone to live with their

significant other. And finally, given that the two most recent CJLEADS results listed the

same Stoney Trace address where Chisholm lived, Detective Stark concluded that Brinkley

lived with her. J.A. 74–75. Hearing the testimony, the district court found these inferences

and the resulting conclusion persuasive. J.A. 144–47.

       In place of law enforcement’s inferences and analysis, the majority looks at a single-

page printout from the CJLEADS database and hypothesizes that Brinkley “might well be

transient.” Majority Op. 14. The majority then suggests that perhaps “Brinkley may have

tended to stay temporarily in various places rather than residing at any one address.”



       7
        It is true Detective Stark did not try to find the probation officer to confirm his
conclusion, but that “does not mean that [his conclusions] were unreasonable.” Wadkins
v. Arnold, 214 F.3d 535, 543 (4th Cir. 2000). Given probation caseloads, it is far from
apparent that contacting a probation officer is even a realistic investigative technique.
Indeed, Brinkley’s PSR shows that when a U.S. Probation Officer tried to contact
Brinkley’s state probation officer, the state probation officer did not respond. J.A. 246.

                                             35
Majority Op. 15. 8 Perhaps the majority’s own inferences are reasonable ones. But even

so, an alternative inference from the information does nothing to eliminate probable cause.

See District of Columbia v. Wesby, 138 S. Ct. 577, 592 (2018) (explaining that “innocent

explanations—even uncontradicted ones—do not have any automatic, probable-cause-

vitiating effect”). 9

        And yet, the majority’s own inferences rest on meager information. The single-

page printout from the CJLEADS database on which their alternative hypothesis is based

is below.




        8
           The majority suggests that their transience conclusion originated with the officers.
Majority Op. 15 n.4. But Special Agent Murphy did not say that he thought, based on the
CJLEADS data, that it was a reasonable inference that Brinkley lacked a residence.
Instead, he only agreed that “someone like Mr. Brinkley” may stay in various places “from
time to time.” J.A. 126. But even acknowledging that possibility, he rejected the likelihood
of it here. See id. (“[A]nything’s possible . . . [b]ut I felt that all the facts that we had at
that point were pointing to the most likely place he was at was this address at Stoney
Trace.”). And Detective Stark did not say that Brinkley may have resided at multiple
addresses. He only agreed that “it might be possible to find [Brinkley] at those other
addresses if he was not located at Stoney Trace Drive.” J.A. 89 (emphasis added). And he
too rejected the majority’s premise. See id. (In response to the question: “[D]id you deem
. . . that it was possible that Mr. Brinkley was staying at one of those other addresses,”
Detective Stark responded: “No. I believed that [Brinkley] was staying at Stoney Trace
Drive.”). Ultimately, the testimony that the majority points to amounts to no more than a
similar suggestion that it might be possible to find me at my house, but also at my office,
my parent’s house, a vacation home, or my brother’s house, or that I stay at those locations
from time to time. Cf. J.A. 89 (The other addresses on Brinkley’s CJLEADS page were
probably “family addresses.”). That would do little to suggest that I am nomadic and lack
any residence.
        9
         The majority’s theory is also a new one, raised only on appeal. Before the district
court, Brinkley’s counsel admitted the government “certainly had some basis to believe
Mr. Brinkley was residing at 4709 Stoney Trace” and never mentioned transience or a
particular alternative residential address during his argument. J.A. 141.
                                              36
37
       To be clear, this page is not what the officers relied on in February 2017 but is a

later-printed example of what the database’s first page might have looked like at the time.

Compared to what the officers saw before arresting Brinkley, this single page includes

“more addresses,” “changed” addresses, and “changed” dates. J.A. 66–67 (noting Exhibit

1 was made “later” to illustrate the officer testimony and explaining that it included “more

addresses” with “different dates besides the addresses,” and that the addresses may have

changed since February 2, 2017). We are not sure what addresses were added or changed,

or what dates were changed. See J.A. 66–67, 88. So even if we were looking at this with

expert eyes, we would be unable to see what the officers saw. The majority, however,

comes at the illustrative printout with less-than-expert eyes and suggests that a reasonable

inference from the database was that Brinkley might have been transient.

       But even if a sample page could support a new theory, this page only presents us

with skeletal information. We have only limited information about the various entries, no

information about the types of connections they indicate, no information about who else

was linked to the various addresses, nor a plethora of other information that was available

to the officers but is not included in the record. Cf. J.A. 155 (Exhibit 2 showing an

illustrative CJLEADS page that displays when an entry on Exhibit 1 is “clicked on,” see

J.A. 69).

       For example, the majority identifies a Planters View address as having been

“entered” on December 28, 2016, five days before the traffic stop where Brinkley had




                                            38
identified his address as Stoney Trace. 10 The majority says that the addition of another

address “just five days earlier” should undermine the conclusion that Brinkley resided on

Stoney Trace. Majority Op. 14. But we know little about the entry listing Planters View,

as the record does not include the click-through page for that entry. All we as judges know

is that the entry with the Planters View address was updated by someone on December 28,

2016. It seems plausible that Brinkley gave that address to another government actor much

earlier than December 28, 2016. 11 Again, officers have experience using this database as

part of their job responsibilities. They often review and navigate it to determine the date



       10
         Given the import that the majority places on this entry, it should be surprising that
neither the government nor defense counsel found it probative enough to specifically
mention during their arguments and that the district court did not find it worth discussing
when making its ruling.
       11
          Even the limited information in the record should make the majority question its
own hypothesis. The December 28 entry seems—at least to me based on the CJLEADS
printout—to be linked to an earlier criminal charge from 2015: “15CRS228668.” And
Brinkley was indeed arrested under that criminal case number for breaking and entering in
August 2015. See J.A. 246 (listing convictions). A reasonable officer could well conclude
that an address associated with a 2015 offense was an older address than the one that
Brinkley recently provided during a traffic stop and to his probation officer. Cf. J.A. 74
(explaining that the other addresses in the database dated to 2008 or 2009)
       But even if one doubted the connection above, the majority errs in relying on its
hypothesis that the Planters View address was “added [to the system] just five days” before
Brinkley’s traffic offense. Majority Op. 14 (emphasis added). We only know that the
offense occurred on January 2, 2017 because the government provided an illustrative click-
through page showing as much. J.A. 155 (government’s Exhibit 2). The CJLEADS entry
that we have reflects an “update” to that entry on March 1, 2017. J.A. 154–55. So we
know that the date on the illustrative exhibit does not reflect the date of the traffic stop
when Brinkley gave that address as his residence. And yet the majority assumes that the
entry date provides useful timing information about the Planters View address.
       I say all of this not to indicate that I know how to read the illustrative CJLEADS
page any better than the majority. It merely highlights that we, as judges, lack enough
information to say that the officers’ conclusions were unreasonable.
                                             39
and frequency with which addresses are entered and updated. So even if we could explore

the system and learn more about each entry, our review of their inferences should be

deferential. But, given that we cannot, we lack any legitimate basis for finding their

inferences in this case to be unreasonable and for substituting our own inferences and

conclusions. Cf. Glover, 140 S. Ct. at 1188 (crediting the officer’s “commonsense

inference” that the defendant was likely the driver of the truck when a database search

showed that the defendant was the truck’s registered owner).

       The majority also explains that the database included another entry—though we

cannot tell what address or the entry’s date—that was linked to a utility bill. Cf. J.A. 74

(noting that other addresses on CJLEADS dated to 2008 or 2009). The majority suggests

that the utility-bill address is just as likely Brinkley’s address because a utility bill

“constitute[s] strong evidence of a defendant’s residence.” Majority Op. 15 (citing United

States v. Graham, 553 F.3d 6, 13 (1st Cir. 2009)). The majority then says that the officers

should have done more to rule out that utility-bill-associated address, even though the

majority knows next to nothing about that address. Id. 12 Regardless, the majority does not



       12
           It seems difficult on this record to conclude that this utility bill was the “most
reasonably reliable information” as to where Brinkley lived. Appellant Reply 4. The utility
bill is not in the record and there is no discussion about when it was sent. For all we know,
it could have been from years before the February 3, 2017 arrest. Further, as Detective
Stark explained, many of these older addresses were likely “family-associated addresses.”
J.A. 74. Perhaps a member of the family put Brinkley’s name on the water bill, or another
family member bears a similar name. See J.A. 125–26 (noting a water bill that came back
either in “Mr. Brinkley’s name, or at least to a Kendrick Brinkley at another address”). All
of this is to say, just because the CJLEADS search turned up a utility bill with a different
address does not render unreasonable the officers’ conclusion that Brinkley lived on Stoney
Trace.
                                             40
give due weight to the fact that the officers considered that address and found that it was

likely a “family-associated address[]” or was at least not “credible as a place where

[Brinkley] was living.” J.A. 74, 113. It might be true that utility-bill-associated addresses

are particularly strong indicators of where someone lives in some jurisdictions or at a given

time. Or perhaps not. Again, I have not examined an actual CJLEADS profile and had to

conclude whether an older utility-bill-associated address is better evidence of where

someone lives than an address recently provided twice. But we know the experienced

officers considered the utility bill and found it was more likely a family-associated address.

See Ornelas, 517 U.S. at 700.

       The majority also decides that Brinkley’s apparent engagement to Chisholm

“certainly provided additional evidence that Brinkley might well have stayed at Chisholm’s

home, but it did not speak to whether he did so as a resident or as Chisholm’s overnight

guest.” Majority Op. 16. It may well be, in some communities, that living together before

marriage is unusual.     But these officers, based on their own experience, believed

differently. And we must “apply the probable cause standard to the facts in their totality.”

United States v. Thomas, 913 F.2d 1111, 1115 (4th Cir. 1990) (emphasis added). So even

if you might infer that a couple would not live together before marriage, these officers had

more information: Brinkley had recently provided that same address during a traffic stop

and to his probation officer. So I find it hard to conclude that the officers unreasonably

considered his relationship status alongside that information to conclude that Brinkley was

living with Chisholm on Stoney Trace.



                                             41
       The majority repeatedly presses that the officers could have investigated more.

Majority Op. 15–17. And it is true that they could have done more. That is almost always

true. But we do not require officers to “exhaust every potential avenue for investigation.”

Smith v. Munday, 848 F.3d 248, 261 (4th Cir. 2017) (quoting Wadkins v. Arnold, 214 F.3d

535, 543 (4th Cir. 2000) (If officers “could have been more thorough, or even [if] . . . [their]

actions may have been mistaken, [that] does not mean that they were unreasonable.”)).

       In sum, the majority failed to give the appropriate weight to the officer’s inferences,

which were entitled to substantial weight given the limited information in the record and

our lack of expertise with this law-enforcement database. And while the officers could

have done more, they did not have to. In total, the information here established probable

cause to believe Brinkley resided at the Stoney Trace address.

       B.     The officers had probable cause to believe that Brinkley would be at the
              Stoney Trace address when they entered to execute the arrest warrant

       The majority’s second-prong analysis is plagued by their faulty first-prong analysis.

In analyzing the second prong, the majority explains that any belief about Brinkley’s

presence was undermined by “uncertainty about where Brinkley resided.” Majority Op.

21; id. at 20 (“[A]n ill-founded belief about a suspect’s residence does not, and cannot,

shore up a belief about his presence.”). The majority is right that the reasonableness of the

belief of an arrestee’s residence affects the reasonableness of the belief in the arrestee’s

presence. See Vasquez-Algarin, 821 F.3d at 481 (A reasonable belief in an arrestee’s

residence “alone carries significant weight in establishing probable cause to believe the

arrestee is present.”). But this means that the majority’s improper inferences about


                                              42
Brinkley’s residence become the engine behind their conclusion that the officers lacked

probable cause to believe Brinkley was present.

       The majority acknowledges that the sounds coming from the apartment “at least

indicated that some living being was present.” Majority Op. 22. But the majority then

concludes that the police had “no reason to think that the noises came from Brinkley rather

than some unknown person.” Id. If the officers really had no reason to believe Brinkley

resided there, then the majority’s conclusion would hold. But if they did have reason to

believe Brinkley lived there, they would have some “reason to think that the noises [inside

the apartment] came from Brinkley.” Id. 13

       The noises from inside the apartment, Chisholm’s increasing nervousness, and

Chisholm and Prigon’s responses to the noises suggested that someone else was inside the

apartment. And when combined with the reasonable belief that Brinkley resided on Stoney

Trace, officers had probable cause to believe that “someone else” was Brinkley.



       13
          The majority likens this case to United States v. Hill, 649 F.3d 258 (4th Cir. 2011).
But as the district court found, this case is materially different. In Hill, the officers admitted
that they did not believe Hill would be present at the residence when they did the search.
Id. at 263–64 (One officer believed that Hill would not be home because Hill had fled
before and that there was an 80 percent chance Hill would not be present when they went
to the residence. Another characterized the trip as one “in regards to a fugitive
investigation.”). And another resident informed the police that Hill was not there and
attributed the noise inside the apartment to her sister. Id. at 264. In Hill, the primary issue,
and why no “reason to believe” Hill was present was found, was that the police relied
“solely . . . on an unidentified noise coming from within the home.” Id. at 265. That was
not the case here. The officers were sure that Brinkley was present before they entered.
See J.A. 81, 134. And the majority cannot seriously contend that an unidentified noise was
the only evidence the officers had that Brinkley was there after the majority themselves list
five other pieces of evidence that would suggest Brinkley was in the apartment. Majority
Op. 20. Hill simply does not dictate this result.
                                               43
                        *                     *                    *

       Experienced officers used a law-enforcement database and supporting information

to concluded that Brinkley resided at the Stoney Trace address. Rejecting their inferences

and conclusions, the majority looks at the limited information we have in the record and

adopts an alternative theory of the evidence. They posit that Brinkley may have been

transient and without a residence—a theory not even argued below. They then suggest that

Brinkley providing law enforcement and probation with the same address that his fiancée

used could only signify that Brinkley was possibly an overnight guest. The majority then

uses their new theory of Brinkley’s residence to decide the officers lacked probable cause

to believe Brinkley was present at the apartment that morning.

       I disagree. But what really matters is that we, as a court far removed from the reality

on the ground, are commanded to give due deference to law enforcement’s inferences that

the local district court agrees with. Giving due weight to those inferences, these officers

had probable cause to believe that Brinkley lived with Chisholm on Stoney Trace. And,

based on that belief and information developed after they arrived, they had probable cause

to believe that Brinkley was present. I respectfully dissent.




                                             44

```

---
