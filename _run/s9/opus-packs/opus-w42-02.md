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

## GROUP: content/cases/Weatherford v. Bursey.md  (`case`, 5 assertions)

### content_page

```
---
title: Weatherford v. Bursey
type: case
citation: "429 U.S. 545 (1977)"
parallel_cite: "97 S. Ct. 837; 51 L. Ed. 2d 30"
neutral_cite: 1977 U.S. LEXIS 40
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-02-22
docket: No. 76-446
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
  opinion_url: "https://www.courtlistener.com/opinion/109590/weatherford-v-bursey/"
  cluster_id: 109590
  opinion_id: null
  identity_checked: true
lake:
  record_id: Weatherford v. Bursey
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: Anchor
related:
  - "[[Sixth Amendment Right to Counsel]]"
  - "[[Hoffa v. United States]]"
  - "[[Massiah v. United States]]"
  - "[[United States v. Henry]]"
  - "[[Kansas v. Ventris]]"
tags:
  - case
  - sixth-amendment
  - right-to-counsel
  - undercover-informant
  - attorney-client
  - section-1983
holding: "The presence of a government undercover agent at defense meetings does not per se violate the Sixth Amendment right to counsel; there is no violation absent tainted evidence, communication of defense strategy to the prosecution (creating a realistic possibility of injury to the defendant or benefit to the State), or purposeful intrusion — none of which occurred where the agent attended at the defense's own invitation, sought no information, and conveyed nothing about the defense to the prosecutors."
aliases:
  - Weatherford v. Bursey
  - "Weatherford v. Bursey (1977)"
---

# Weatherford v. Bursey

*429 U.S. 545 (1977)* (No. 75-1510) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109590 → combined opinion 109590 (White, J.; 429 U.S. 545, argued Dec. 7, 1976, decided Feb. 22, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*558`). S9 promotes. -->

## Background
Weatherford, an undercover South Carolina agent, took part with Bursey in vandalizing a Selective Service office and was arrested alongside him to preserve his cover. At the invitation of Bursey and his lawyer, Weatherford twice attended meetings where the coming trial was discussed, but the trial court found he never sought information and never passed anything about Bursey's defense to his superiors or the prosecutor. On the day of trial Weatherford was unexpectedly called as a prosecution witness and gave damaging eyewitness testimony about the vandalism (not about the defense meetings). After his conviction, Bursey sued under 42 U.S.C. § 1983, claiming the meetings had deprived him of effective assistance of counsel. The District Court found for the agents; the Fourth Circuit reversed, adopting a [[Common Legal Terms#per-se|per se]] rule that any prosecution intrusion into the attorney-client relationship requires a new trial.

## Issue
Whether an undercover agent's attendance at meetings between a defendant and his counsel, standing alone, deprives the defendant of the effective assistance of counsel guaranteed by the Sixth and Fourteenth Amendments.

## Rule
The Court rejected the Fourth Circuit's [[Common Legal Terms#per-se|per se]] rule as sweeping too broadly, because many such encounters cause no conceivable prejudice. A Sixth Amendment violation instead depends on the presence of concrete harm, and here there was none: "There being no tainted evidence in this case, no communication of defense strategy to the prosecution, and no purposeful intrusion by Weatherford, there was no violation of the Sixth Amendment insofar as it is applicable to the States by virtue of the Fourteenth Amendment." — 429 U.S. at 558. ^pin-558

## Application
The key was that Weatherford never communicated the substance of the defense meetings to the prosecution, so his mere presence created no realistic possibility of injury to Bursey or benefit to the State — the situation the Court had left open in *[[Hoffa v. United States|Hoffa]]*. Nor did his trial testimony change the analysis: it concerned only the vandalism and drew nothing from the meetings. The Court likewise rejected a due-process theory built on *[[Brady v. Maryland|Brady]]*, holding that the prosecution had no obligation to disclose in advance that an informant would testify, since there is no general constitutional right to criminal discovery.

## Conclusion
The judgment of the Court of Appeals for the Fourth Circuit was **reversed** (reinstating the District Court's judgment for the agents). White, J., delivered the opinion of the Court. Marshall, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Brennan, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Weatherford* anchors the rule that government intrusion into the attorney-client relationship violates the Sixth Amendment only on a showing of prejudice — communication of defense strategy, use of tainted evidence, or purposeful intrusion — not automatically. Teach it within the deliberate-elicitation line of *[[Massiah v. United States]]*, *[[United States v. Henry]]*, and *[[Kansas v. Ventris]]* as the case that declined a [[Common Legal Terms#per-se|per se]] remedy for informant presence at defense meetings.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Anchor*

## Sources
- [*Weatherford v. Bursey*, 429 U.S. 545 (1977)](https://www.courtlistener.com/opinion/109590/weatherford-v-bursey/) — pinpoint: 558 (White, J., for the Court; the CL opinion text carries the reporter star `*558` in the paragraph preceding the quoted holding, which sits before the star `*559`, i.e., on page 558). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "152b6c2e90b77dae", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "429 U.S. 545 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 40", "official_citation_present": true, "parallel_cite": "97 S. Ct. 837; 51 L. Ed. 2d 30", "title": "Weatherford v. Bursey", "year": "1977"}}
{"assertion_id": "a149a6eaf07754c3", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Anchor", "title": "Weatherford v. Bursey"}}
{"assertion_id": "c85842592dedef3b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The presence of a government undercover agent at defense meetings does not per se violate the Sixth Amendment right to counsel; there is no violation absent tainted evidence, communication of defense strategy to the prosecution (creating a realistic possibility of injury to the defendant or benefit to the State), or purposeful intrusion — none of which occurred where the agent attended at the defense's own invitation, sought no information, and conveyed nothing about the defense to the prosecutors.", "title": "Weatherford v. Bursey"}}
{"assertion_id": "c1db755655816c56", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Weatherford v. Bursey"}}
{"assertion_id": "df8019e600cb3867", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Weatherford v. Bursey", "varies_by_point": "false"}}
```

### lake record — Weatherford v. Bursey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Weatherford v. Bursey",
  "status": "under_review",
  "identity": {
    "case_name": "Weatherford v. Bursey",
    "case_name_short": "Weatherford",
    "case_name_full": "WEATHERFORD, AGENT OF THE SOUTH CAROLINA LAW ENFORCEMENT DIVISION, Et Al. v. BURSEY",
    "input_case_name": "Weatherford v. Bursey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-02-22",
    "year": 1977,
    "docket": "No. 76-446",
    "cluster_id": 109590,
    "lead_opinion_id": 9426656,
    "sibling_ids": [],
    "absolute_url": "/opinion/109590/weatherford-v-bursey/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 545",
      "volume": "429",
      "reporter": "U.S.",
      "page": "545",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 837",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "837",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 30",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 40",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 545",
        "volume": "429",
        "reporter": "U.S.",
        "page": "545",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 837",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "837",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 30",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 40",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 545",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 545",
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
    "date_created": "2026-07-06T13:45:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "weatherford-v-bursey--109590",
      "to_record_id": "Weatherford v. Bursey",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Weatherford v. Bursey

```
<opinion type="majority">
<author id="b697-5">Mk. Justice White</author>
<p id="AP3o">delivered the opinion of the Court.</p>
<p id="b697-6">The issue here is whether in the circumstances present in this case the conduct of an undercover agent for a state law enforcement agency deprived respondent Bursey of his right to the effective assistance of counsel guaranteed him by the Sixth and Fourteenth Amendments of the United States Constitution or deprived him of due process of law in violation of the Fourteenth Amendment.</p>
<p id="b697-7">I</p>
<p id="b697-8">This case began when respondent Bursey filed suit under <span class="citation no-link">42 U. S. C. § 1983</span> against petitioners Weatherford and Strom, respectively an undercover agent for and the head of the South Carolina State Law Enforcement Division, asserting that the defendants had deprived him of certain constitutional rights. The case was tried without a jury. The following facts are taken from the District Court’s findings, which were not disturbed by the Court of Appeals.</p>
<p id="b697-9">During the early morning hours of March 20, 1970, Bursey and Weatherford, along with two others, vandalized the offices of the Richland County Selective Service in Columbia, S. C. Police were advised of the incident by Weatherford, who, in order to maintain his undercover status and his capability of working on other current matters in that capacity, was arrested and charged along with Bursey. Weatherford was immediately released on bond and, continuing the masquerade, retained an attorney, Frank Taylor, Sr. Bursey, who was later released on bond, retained his own counsel, C. Rauch Wise.</p>
<p id="b697-10">On two occasions thereafter and prior to trial, Weather-ford met with Bursey and Wise, and the approaching trial <page-number citation-index="1" label="548">*548</page-number>was discussed. With respect to these meetings, the District Court found as follows:</p>
<blockquote id="b698-5">“On neither of these occasions did the defendant Weatherford seek information from the plaintiff or his attorney, and on neither occasion did he initiate or ask for the meeting. He was brought into the meetings by the plaintiff and plaintiff’s attorney in an effort to obtain information, ideas or suggestions as to the plaintiff’s defense. From the beginning Weatherford advised plaintiff and plaintiff’s attorney that Weatherford would obtain a severance of his case from that of the plaintiff. This severance was to be upon the ground that Weatherford might be prejudiced in going to trial with Bursey as a codefendant, because of Bursey’s reputation and participation in other activities which had been covered by the news media. On no occasion did Bursey or his attorney question the granting of a severance, nor did they seem to concern themselves with whether the prosecutor would consent to a severance, although such consent is quite unusual where codefendants are charged with the same crime and proof will be from the same witnesses based upon identical facts. At those meetings between plaintiff, plaintiff’s attorney and defendant Weatherford the plaintiff and his attorney raised the question of a possible informer being used to prove the case, but they never asked Weatherford if he were an informer and he never specifically denied being an informer, since he was never asked or accused.” App. 248-249.</blockquote>
<p id="b698-6">At no time did Weatherford discuss with or pass on to his superiors or to the prosecuting attorney or any of the attorney’s staff “any details or information regarding the plaintiff’s trial plans, strategy, or anything having to do with the criminal action pending against plaintiff.” <span class="citation no-link"><em>Id., </em>at 249</span>. Until the <page-number citation-index="1" label="549">*549</page-number>day of trial the prosecuting attorney did not plan to use Weatherford as a witness. Consequently, until then, Weatherford had not expected to be a witness and had anticipated continuing his undercover work. However, Weatherford had lost some of his effectiveness as an agent in the weeks preceding trial because he had been seen in the company of police officers, and he was called for the prosecution. He testified as to his undercover activities and gave an eyewitness account of the events of March 20, 1970. Bursey took the stand, was convicted, and then disappeared until apprehended some two years later, at which time he was incarcerated and forced to serve his 18-month sentence.</p>
<p id="b699-5">Bursey then began this § 1983 action, alleging that Weatherford had communicated to his superiors and prosecuting officials the defense strategies and plans which he had learned at his meetings with Bursey and Wise, thereby depriving Bursey of the effective assistance of counsel to which he was entitled under the Sixth and Fourteenth Amendments as well as of his right to a fair trial guaranteed him by the Due Process Clause of the Fourteenth Amendment. The District Court found for the defendants in all respects and entered judgment accordingly.</p>
<p id="b699-6">The Court of Appeals for the Fourth Circuit reversed, <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d 483</a></span> (1975), concluding that “on the facts as found by the district court Bursey’s rights to effective assistance of counsel and a fair trial were violated.” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#486" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually..."><em>Id., </em>at 486</a></span>. The Court of Appeals held that “whenever the prosecution knowingly arranges or permits intrusion into the attorney-client relationship the right to counsel is sufficiently endangered to require reversal and a new trial.” <em><span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">Ibid.</a></span> </em>That the intrusion occurred in order to prevent revealing Weather-ford’s identity as an undercover agent was immaterial. The Court of Appeals thought that Weatherford was himself “a member of the prosecution,” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually..."><em>id., </em>at 487</a></span>, and that therefore it was also immaterial that he had not informed other <page-number citation-index="1" label="550">*550</page-number>officials about what was said or done in the two meetings with Bursey and Wise.</p>
<p id="b700-5">In addition, the Court of Appeals concluded that Bursey had been denied due process of law under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), by concealment of Weatherford’s identity until the day of trial and by Weatherford’s statement that he would not be a witness, all of which lulled Bursey into a false sense of security and interfered with his preparations for trial. The judgment of the District Court was reversed, but the remand for further proceedings would have allowed Weatherford and Strom to present a qualified immunity defense under <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975).</p>
<p id="b700-6">We granted the petition for certiorari filed by Weatherford and Strom, who are represented by the State Attorney General. <span class="citation" data-id="9001254"><a href="/opinion/9008466/smith-v-united-states/" aria-description="Citation for case: Smith v. United States">426 U. S. 946</a></span> (1976). We reverse.</p>
<p id="b700-7">II</p>
<p id="b700-8">The exact contours of the Court of Appeals’ <em>per se </em>right-to-counsel rule are difficult to discern; but as the Court of Appeals applied the rule in this case, it would appear that if an undercover agent meets with a criminal defendant who is awaiting trial and with hi.s attorney and if the forthcoming trial is discussed without the agent’s revealing his identity, a violation of the defendant’s constitutional rights has occurred, whatever was the purpose of the agent in attending the meeting, whether or not he reported on the meeting to his superiors, and whether or not any specific prejudice to the defendant’s preparation for or conduct of the trial is demonstrated or otherwise threatened. The Court of Appeals was of the view, <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#486" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 486</a></span>, that this Court “establish [ed] such a per se rule” in <em>Black </em>v. <em>United States, </em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">385 U. S. 26</a></span> (1966), and <em>O’Brien </em>v. <em>United States, </em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">386 U. S. 345</a></span> (1967). The Court of Appeals also relied on <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966).</p>
<p id="b701-4"><page-number citation-index="1" label="551">*551</page-number>We cannot agree that these cases, individually or together, either require or suggest the rule announced by the Court of Appeals and now urged by Bursey. Both <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span> </em>involved surreptitious electronic surveillance by the Government, which was discovered after trial and conviction and which was plainly illegal under the Fourth Amendment.<footnotemark>1</footnotemark> In each case, some, but not all, of the conversations overheard were between the criminal defendant and his counsel during trial preparation. The conviction in each case was set aside and a new trial ordered. The explanatory <em>per curiam </em>in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span>, </em>although referring to the overheard conversations with counsel, did not rule that whenever conversations with counsel are overheard the Sixth Amendment is violated and a new trial must be had. Indeed, neither the Sixth Amendment nor the right to counsel was even mentioned in the short opinion. The Solicitor General conceded that Black was entitled to a “judicial determination” of whether “the monitoring of conversations between [Black] and his attorney had [any] <em>effect </em>upon his conviction or the fairness of his trial,” although the Solicitor General contended that information derived from the overheard conversations was not used in any way by the prosecution. Memorandum for United States in <em>Black </em>v. <em>United States, </em>O. T. 1965, No. 1029, p. 4 (emphasis added). The Court focused on the particular form the “judicial determination” <page-number citation-index="1" label="552">*552</page-number>should take, concluding that on the particular facts of the case a new trial was the more appropriate means of affording Black “an opportunity to protect himself from the <em>use </em>of evidence that might be otherwise inadmissible.” 385 U. S., at 29 (emphasis added). In <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span>, </em>the Court wrote nothing further, merely citing the <em>Black per curiam. </em>Once again the Solicitor General did not oppose further judicial proceedings to determine whether any information from the surveillance had been used at trial, notwithstanding his assertion that the contents of the overheard conversations were never communicated to the prosecuting attorneys. Brief for United States in <em>O’Brien </em>v. <em>United States, </em>O. T. 1966, No. 823, pp. 10-12.</p>
<p id="b702-5">It is difficult to believe that the Court in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span> </em>was evolving a definitive construction of the Sixth Amendment without identifying the Amendment it was interpreting, especially in view of the well-established Fourth Amendment grounds for excluding the fruits of the illegal surveillance.<footnotemark>2</footnotemark> If anything is to be inferred from these two cases with respect to the right to counsel, it is that when conversations with counsel have been overheard, the constitutionality of the conviction depends on whether the overheard conversations have produced, directly or indirectly, any of the evidence offered at trial. This is a far cry from the <em>per se </em>rule announced by the Court of Appeals below, for under that rule trial prejudice to the defendant is deemed irrelevant. Here, the courts below have already conducted the “judicial determination,” lacking in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span>, </em>of the effect of the overheard conversations on the defendant’s conviction, and there is nothing in their findings or in the record to indicate any “use of evidence that might be otherwise inadmissible.”</p>
<p id="b702-6">Neither does the Court’s decision in <em>Hoffa </em>v. <em>United States, supra, </em>support the proposition urged by respondent. There, an informant sat in on conversations that defendant Hoffa had with his lawyers and with others during the <page-number citation-index="1" label="553">*553</page-number>course of Hoffa’s trial on a charge of violating the TaftHartley Act. The jury at that trial hung. Hoffa was then tried for tampering with that jury. The informer testified at the latter trial with respect to conversations he had overheard in Hoffa’s hotel suite during the prior trial, not including, however, the conversations Hoffa had with counsel. The Court sustained Hoffa’s jury-tampering conviction over his claim, among others, that his Sixth Amendment counsel right had been violated.</p>
<p id="b703-5">In doing so, the Court did not hold that the Sixth Amendment right to counsel subsumes a right to be free from intrusion by informers into counsel-client consultations. Nor did it purport to describe the contours of any such right. The Court merely assumed, without deciding, that two cases in the Court of Appeals for the District of Columbia Circuit dealing with the right to counsel, <em>Caldwell </em>v. <em>United States, </em>92 U. S. App. D. C. 355, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">205 F. 2d 879</a></span> (1953), and <em>Coplon </em>v. <em>United States, </em>89 U. S. App. D. C. 103, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749</a></span> (1951), were correctly decided;<footnotemark>3</footnotemark> <em>assumed </em>without deciding, that had Hoffa been convicted at his first trial, the conviction would have been set aside because the informer had overheard Hoffa and his lawyers conversing and had reported to the authorities the substance of at least some of those conversations; and then held that Hoffa’s <em>assumed </em>Sixth Amendment rights had not been violated because the informer’s testimony at the jury-tampering trial did not touch upon the overheard conversations with counsel but dealt only with conversations between Hoffa and third parties when his lawyers were not <page-number citation-index="1" label="554">*554</page-number>present. 385 U. S., at 307-308. Neither <em>Black, O’Brien, Hoffa, </em>nor any other case in this Court to which we have been cited furnishes grounds for the interpretation and application of the Sixth and Fourteenth Amendments appearing in the Court of Appeals’ opinion and judgment.</p>
<p id="b704-5">At the same time, we need not agree with petitioners that whenever a defendant converses with his counsel in the presence of a third party thought to be a confederate and ally, the defendant assumes the risk and cannot complain if the third party turns out to be an informer for the government who has reported on the conversations to the prosecution and who testifies about them at the defendant’s trial. Had Weatherford testified at Bursey’s trial as to the conversation between Bursey and Wise; had any of the State’s evidence originated in these conversations; had those overheard conversations been used in any other way to the substantial detriment of Bursey; or even had the prosecution learned from Weatherford, an undercover agent, the details of the Bursey-Wise conversations about trial preparations, Bursey would have a much .stronger case.<footnotemark>4</footnotemark></p>
<p id="b705-4"><page-number citation-index="1" label="555">*555</page-number>None of these elements is present here, however. Weather-ford’s testimony for the prosecution about the events of March and April 1970 revealed nothing said or done at the meetings between Bursey and Wise that he attended.<footnotemark>5</footnotemark> None of the State’s evidence was obtained as a consequence of Weather-ford’s participation in those meetings. Nevertheless, it <page-number citation-index="1" label="556">*556</page-number>might be argued that Weatherford, a dutiful agent, surely communicated to the prosecutors Bursey’s defense plans and strategy and his attorney’s efforts to prepare for trial, all of which was inherently detrimental to Bursey, unfairly advantaged the prosecution, and threatened to subvert the adversary system of criminal justice.</p>
<p id="b706-5">The argument founders on the District Court’s express finding that Weatherford communicated nothing at all to his superiors or to the prosecution about Bursey’s trial plans or about the upcoming trial. App. 249, 252. The Court of Appeals did not disturb this finding, but sought to surmount it by declaring Weatherford himself to have been a member of the prosecuting team whose knowledge of Bursey’s trial plans was alone enough to violate Bursey’s constitutional right to counsel and to vitiate Bursey’s conviction. <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 487</a></span>. Though imaginative, this reasoning is not a realistic assessment of the relationship of Weatherford to the prosecuting staff or of the potential for detriment to Bursey or benefit to the State that Weather-ford’s uncommunicated knowledge might pose. If the fact was, as found by the District Court, that Weatherford communicated nothing about the two meetings to anyone else, we are quite unconvinced that a constitutional claim under the Sixth and Fourteenth Amendments was made out.</p>
<p id="b706-6">This is consistent with the Court’s approach in the <em>Hoff a </em>case. There, the informant overheard several conversations between Hoffa and his attorneys, but the Court found it necessary to deal with the Sixth Amendment right-to-counsel claim only after noting that the informant had reported to the Government about at least some of the activities of Hoffa’s defense counsel. 385 U. S., at 305-306. As long as the information possessed by Weatherford remained uncommunicated, he posed no substantial threat to Bursey’s Sixth Amendment rights. Nor do we believe that federal or state prosecutors will be so prone to lie or the difficulties of proof <page-number citation-index="1" label="557">*557</page-number>will be so great that we must always assume not only that an informant communicates what he learns from an encounter with the defendant and his counsel but also that what he communicates has the potential for detriment to the defendant or benefit to the prosecutor’s case.</p>
<p id="b707-5">Moreover, this is not a situation where the State’s purpose was to learn what it could about the defendant’s defense plans and the informant was instructed to intrude on the lawyer-client relationship or where the informant has assumed for himself that task and acted accordingly. Weatherford, the District Court found, did not intrude at all; he was invited to the meeting, apparently not for his benefit but for the benefit of Bursey and his lawyer. App. 248. Weatherford went, not to spy, but because he was asked and because the State was interested in retaining his undercover services on other matters and it was therefore necessary to avoid raising the suspicion that he was in fact the informant whose existence Bursey and Wise already suspected.</p>
<p id="b707-6">That the <em>per se </em>rule adopted by the Court of Appeals would operate prophylactically and effectively is very likely true; but it would require the informant to refuse to participate in attorney-client meetings, even though invited, and thus for all practical purposes to unmask himself. Our cases, however, have recognized the unfortunate necessity of undercover work and the value it often is to effective law enforcement. <em>E. g., United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#432" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 432</a></span> (1973); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#208" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 208-209</a></span> (1966). We have also recognized the desirability and legality of continued secrecy even after arrest. <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#59" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53, 59, 62</a></span> (1957). We have no general oversight authority with respect to state police investigations. We may disapprove an investigatory practice only if it violates the Constitution; and judged in this light, the Court of Appeals’ <em>per se </em>rule cuts much too broadly. If, for example, <page-number citation-index="1" label="558">*558</page-number>Weatherford at Bursey’s invitation had attended a meeting between Bursey and Wise but Wise had become suspicious and the conversation was confined to the weather or other harmless subjects, the Court of Appeals’ rule, literally read, would cloud Bursey’s subsequent conviction, although there would have been no constitutional violation. The same would have been true if Wise had merely asked whether Weatherford was an informant, Weatherford had denied it, and the meeting then had ended; likewise if the entire conversation had consisted of Wise’s questions and Weatherford’s answers about Weatherford’s own defense plans. Also, and more cogently for present purposes, unless Weatherford communicated the substance of the Bursey-Wise conversations and thereby created at least a realistic possibility of injury to Bursey or benefit to the State, there can be no Sixth Amendment violation. Yet Under the Court of Appeals’ rule, Bursey’s conviction would have been set aside on appeal.</p>
<p id="b708-5">There being no tainted evidence in this case, no communication of defense strategy to the prosecution, and no purposeful intrusion by Weatherford, there was no violation of the Sixth Amendment insofar as it is applicable to the States by virtue of the Fourteenth Amendment., The proof in this case thus fell short of making out a § 1983 claim, and the judgment of the District Court should have been affirmed in this respect.</p>
<p id="b708-6">It is also apparent that neither Weatherford’s trial testimony nor the fact of his testifying added anything to the Sixth Amendment claim. Weatherford’s testimony for the prosecution related only to events prior to the meetings with Wise and Bursey and referred to nothing that was said at those meetings. There is no indication that any of this testimony was prompted by or was the product of those meetings. Weatherford’s testimony was surely very damaging, but the mere fact that he had met with Bursey and his lawyer prior to trial did not violate Bursey’s right to <page-number citation-index="1" label="559">*559</page-number>counsel any more than the informant’s meetings with Hoffa and Hoffa’s lawyers rendered inadmissible the informant’s testimony having no connection with those conversations.</p>
<p id="b709-5">Ill</p>
<p id="b709-6">Because under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), the prosecution has the “duty under the due process clause to insure that ‘criminal trials are fair’ by disclosing evidence favorable to the defendant upon request,” the Court of Appeals also held that the State was constitutionally forbidden to “conceal the identity of an informant from a defendant during his trial preparation,” to permit the informant to “deny up through the day before his appearance at trial that he will testify against the defendant,” and then to have the informant “testify with devastating effect.” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 487</a></span>. This conduct, the Court of Appeals thought, lulled the defendant into a false sense of security and denied him “the opportunity (1) to consider whether plea bargaining might be the best course, (2) to do a background check on Weatherford for purposes of cross-examination, and (3) to attempt to counter the devastating impact of eyewitness identification.” <em><span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">Ibid.</a></span> </em>The Court of Appeals apparently would have arrived at this conclusion whether or not Weatherford had ever met with Wise.</p>
<p id="b709-7">Again we are in disagreement. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>does not warrant the Court of Appeals’ holding. It does not follow from the prohibition against concealing evidence favorable to the accused that the prosecution must reveal before trial the names of all witnesses who will testify unfavorably. There is no general constitutional right to discovery in a criminal case, and <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>did not create one; as the Court wrote recently, “the Due Process Clause has little to say regarding the amount of discovery which the parties must be afforded . . . .” <em>Wardius </em>v. <em>Oregon, </em><span class="citation" data-id="9425341"><a href="/opinion/108811/wardius-v-oregon/#474" aria-description="Citation for case: Wardius v. Oregon">412 U. S. 470, 474</a></span> (1973). <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>is not implicated here where the only claim is that the State should <page-number citation-index="1" label="560">*560</page-number>have revealed that it would present the eyewitness testimony of a particular agent against the defendant at trial.</p>
<p id="b710-5">In terms of the defendant’s right to a fair trial, the situation is not changed materially by the additional element relied upon by the Court of Appeals, namely, that Weather-ford not only concealed his identity but represented he would not be a witness for the prosecution, an assertion that proved to be inaccurate. There are several answers to the contention that the claim of misrepresentation is of crucial importance. The first is that there was no deliberate misrepresentation in this regard: The trial court found that until the day of trial Weatherford did not expect to be called as a witness; until then he did not know-that he would testify. Second, as we understand the argument, it is that once the undercover agent has successfully caused an arrest, he risks causing an unfair trial if he denies his identity when accused or asked. We would" hesitate so to construe the Due Process Clause. We are not at all convinced that there is a constitutional difference between the situation where the informant is sufficiently trusted that he is never suspected and never asked about the possibility of his testifying but nevertheless surprises the defendant by giving devastating testimony, and the situation we have here, where the defendant is suspicious enough to ask and the informant denies that he will testify but nevertheless does so. Moreover, if the informant must confess his identity when confronted by an arrested defendant, in many cases the agent in order to protect himself will simply disappear pending trial, before the confrontation occurs. In the last analysis, however, the undercover agent who stays in place and continues his deception merely retains the capacity to surprise; and unless the surprise witness or unexpected evidence is, without more, a denial of constitutional rights, Bursey was not denied a fair trial.</p>
<p id="b710-6">The Court of Appeals suggested that Weatherford’s continued duplicity lost Bursey the opportunity to plea bargain. <page-number citation-index="1" label="561">*561</page-number>But there is no constitutional right to plea bargain; the prosecutor need not do so if he prefers to go to trial. It is a novel argument that constitutional rights are infringed by-trying the defendant rather than accepting his plea of guilty. Moreover, Wise could have approached the prosecutor before trial and surely was under no misapprehension about Bursey’s plight during trial. It was also suggested by the Court of Appeals that Bursey was deprived of the opportunity to investigate Weatherford in preparation for possible impeachment on cross-examination. But there was no objection at trial to Weatherford’s testimony, no request for a continuance, and even now no indication of substantial prejudice from this occurrence. As for Bursey’s claimed disability to counter Weatherford’s “devastating” testimony, the disadvantage was no more than exists in any case where the State presents very damaging evidence that was not anticipated. Wise and Bursey must have realized that in going to trial the State was confident of conviction and that if any exculpatory evidence or possible defenses existed it would be extremely wise to have them available. Prudence would have counseled at least as much.</p>
<p id="b711-5">The judgment of the Court of Appeals is</p>
<p id="b711-6">Reversed.<footnotemark>6</footnotemark>.</p>
<footnote label="1">
<p id="b701-5"> In <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), the Court had held that eavesdropping accomplished through use of an electronic listening device similar to the “tubular microphone” used to overhear Black’s and O’Brien’s conversations constituted an unauthorized physical penetration of the petitioners’ premises in violation of the Fourth Amendment. The Solicitor General conceded that both Black and O’Brien should have been allowed to establish that the prosecution’s case was tainted by the interception of conversations between Black and persons other than their attorneys as well as by conversations involving counsel, thus indicating his awareness of the illegality of the Government’s eavesdropping under the Fourth Amendment.</p>
</footnote>
<footnote label="2">
<p id="b702-7"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="3">
<p id="b703-6"> <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>held that interceptions by Government agents of telephone messages between the defendant and her lawyer before and during trial, if proved by the defendant, deprived her of her right to counsel and entitled her to a new trial. <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>held that the defendant’s right to counsel was violated where a Government undercover agent went to work as an assistant for the defense and reported frequently to the prosecution on “many matters connected with the impending trial.” 92 U. S. App. D. C., at 356, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#880" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 880</a></span> (footnote omitted).</p>
</footnote>
<footnote label="4">
<p id="b704-6"><em> In Hoffa, </em>the United States conceded, as it does here as <em>amicus curiae, </em>that the Sixth Amendment would be violated “if the government places an informant in the defense camp during a criminal trial and receives from that informant privileged information pertaining to the defense of the criminal charges . . . because the Sixth Amendment’s assistance-of-counsel guarantee can be meaningfully implemented only if a criminal defendant knows that his communications with his attorney are private and that his lawful preparations for trial are secure against intrusion by the government, his adversary in the criminal proceeding.” Brief for United States in <em>Hoffa </em>v. <em>United States, </em>O. T. 1966, No. 32, p. 71, quoted in Brief for United States as <em>Amicus Curiae </em>in the instant <em>case, </em>p. 24 n. 13.</p>
<p id="b704-7">Respondent argues that <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span> </em>established the same right-to-counsel standard for government interception of attorney-client communications by an undercover agent as for interception by electronic surveillance. Even apart from the fact that the Court was merely assuming the existence of a right-to-counsel violation in that case, see <em>supra, </em>at 553, we find respondent’s argument questionable. One threat to the effective assist<page-number citation-index="1" label="555">*555</page-number>anee of counsel posed by government interception of attorney-client communications lies in the inhibition of free exchanges between defendant and counsel because of the fear of being overheard. However, a fear that some third party may turn out to be a government agent will inhibit attorney-client communication to a lesser degree than the fear that the government is monitoring those communications through electronic eavesdropping, because the former intrusion may be avoided by excluding third parties from defense meetings or refraining from divulging defense strategy when third parties are present at those meetings. Of course, in some circumstances the ability to exclude third parties from defense meetings may not eliminate the chilling effect on attorney-client exchanges, but neither <em>Hoff a </em>nor any other decision of this Court supports respondent’s theory that the chill is the same whether induced by electronic surveillance or by undercover agents. Cf. <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#402" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 402-405</a></span> (1976) (attorney-client privilege protects only those disclosures which might not haye been made absent the privilege, because the purpose of the privilege is to encourage confidential disclosures by a client to an attorney); 8 J. Wigmore, Evidence § 2311, pp. 601-602 (McNaughton rev. ed. 1961) (attorney-client communications in the presence of a third party not the agent of either are generally not protected by the privilege).</p>
</footnote>
<footnote label="5">
<p id="b705-9"> See App. 225-240 (testimony of Weatherford at state trial). On cross-examination by Wise (Bursey’s lawyer), Weatherford acknowledged that at the second meeting with Bursey and Wise, Weatherford told Wise, in response to the latter’s questions, that he had not been asked to testify for the prosecution and that he did not anticipate being present at Bursey’s trial. This testimony, elicited by defense counsel apparently for the purpose of discrediting Weatherford’s testimony on direct examination, obviously does not constitute use by the prosecution of information obtained from Weatherford’s attendance at defense meetings. Whatever the limitations on testimony by informants about statements made at defense meetings attended by them, 'the Sixth Amendment does not prevent the defense from introducing such statements to undercut the effectiveness of the informant’s testimony for the prosecution.</p>
</footnote>
<footnote label="6">
<p id="b711-9"> Because we hold that Bursey’s constitutional rights were not violated by Weatherford’s actions, we reverse the holding of the Court of Appeals that Weatherford’s superior, Strom, was also liable because of his involvement in Weatherford’s undercover activities.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Weeks v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Weeks v. United States"
type: case
citation: "232 U.S. 383 (1914)"
parallel_cite: "34 S. Ct. 341; 58 L. Ed. 652"
neutral_cite: 1914 U.S. LEXIS 1368
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1914
date_decided: 1914-02-24
docket: 461
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1914-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Weeks v. United States
  varies_by_point: false
  scope_note: "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/98094/weeks-v-united-states/"
  cluster_id: 98094
  opinion_id: 98094
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Mapp v. Ohio]]", "[[Wong Sun v. United States]]", "[[United States v. Leon]]"]
aliases: ["Weeks"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "warrantless-search", "origin"]
holding: "Origin of the federal exclusionary rule: evidence obtained in violation of the Fourth Amendment is inadmissible against a defendant in…"
lake:
  record_id: Weeks v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Weeks v. United States

*232 U.S. 383 (1914)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Weeks was arrested at his place of business for using the mails to transport lottery tickets. While he was in custody, police officers and a United States Marshal entered his home without a warrant — twice — and seized letters and private papers, which were turned over to the federal prosecutor. Before trial, Weeks petitioned for the return of his property; the court returned some items but kept the letters, which were admitted over his objection and used to convict him.

## Issue
Whether evidence seized by federal officers from a defendant's home without a warrant, in violation of the Fourth Amendment, may be retained and used against him at his federal criminal trial.

## Rule
Evidence obtained by federal officers in violation of the Fourth Amendment may not be used against the accused in a federal prosecution. If it could be, the Amendment would be a dead letter: "If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures, is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." — 232 U.S. at 393. ^pin-393

A defendant who makes a timely demand for the return of unlawfully seized property is entitled to it, and admitting it is reversible error: "the court should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed." — *Id.* at 398. ^pin-398

## Application
On these facts the letters were taken from Weeks's house by a United States Marshal acting without a warrant — "under color of his office" and in direct violation of the Fourth Amendment. Weeks had made a seasonable application for their return, which the trial court denied. Because the seizure was unconstitutional and the demand timely, the court should have restored the letters; retaining and admitting them at trial was prejudicial error requiring reversal. (The Court noted that the seizure by local police, not acting under federal authority, fell outside the Amendment's reach against the Federal Government.)

## Conclusion
The warrantless federal seizure violated the Fourth Amendment; admitting the seized letters was prejudicial error. The judgment was reversed. *Weeks* established the federal exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of its core holding. *Weeks* originally bound only federal officers; its exclusionary rule was **extended to the States** by [[Mapp v. Ohio]] (1961). The rule was later elaborated and qualified — derivative evidence in [[Wong Sun v. United States]] and the [[The Good-Faith Exception|good-faith exception]] in [[United States v. Leon]] — but *Weeks* remains the foundational authority.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Weeks v. United States*, 232 U.S. 383 (1914) — https://www.courtlistener.com/opinion/98094/weeks-v-united-states/ — pinpoints: 393, 398.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e871d088db9d3bb9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "232 U.S. 383 (1914)", "court": "U.S. Supreme Court", "neutral_cite": "1914 U.S. LEXIS 1368", "official_citation_present": true, "parallel_cite": "34 S. Ct. 341; 58 L. Ed. 652", "title": "Weeks v. United States", "year": "1914"}}
{"assertion_id": "082841937c9432bf", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Origin of the federal exclusionary rule: evidence obtained in violation of the Fourth Amendment is inadmissible against a defendant in…", "title": "Weeks v. United States"}}
{"assertion_id": "15a24ccc64e6a189", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Key — Anchor", "title": "Weeks v. United States"}}
{"assertion_id": "015cb06bcdf5a4d0", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1914-02-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Weeks v. United States", "field_i_validity": "good_law", "scope_note": "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law.", "title": "Weeks v. United States", "varies_by_point": "false"}}
{"assertion_id": "986eb1cf264ff4c1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Weeks v. United States"}}
```

### lake record — Weeks v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Weeks v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Weeks v. United States",
    "case_name_short": "Weeks",
    "case_name_full": "Weeks v. United States",
    "input_case_name": "Weeks v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1914-02-24",
    "year": 1914,
    "docket": "461",
    "cluster_id": 98094,
    "lead_opinion_id": 98094,
    "sibling_ids": [
      98094
    ],
    "absolute_url": "/opinion/98094/weeks-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "232 U.S. 383",
      "volume": "232",
      "reporter": "U.S.",
      "page": "383",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "34 S. Ct. 341",
        "volume": "34",
        "reporter": "S. Ct.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 652",
        "volume": "58",
        "reporter": "L. Ed.",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1914 U.S. LEXIS 1368",
        "volume": "1914",
        "reporter": "U.S. LEXIS",
        "page": "1368",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "232 U.S. 383",
        "volume": "232",
        "reporter": "U.S.",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 S. Ct. 341",
        "volume": "34",
        "reporter": "S. Ct.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 652",
        "volume": "58",
        "reporter": "L. Ed.",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1914 U.S. LEXIS 1368",
        "volume": "1914",
        "reporter": "U.S. LEXIS",
        "page": "1368",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "232 U.S. 383",
    "official_selection": {
      "court_class": "scotus",
      "selected": "232 U.S. 383",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-393",
      "page": null,
      "quote": "--- # Weeks v. United States *232 U.S. 383 (1914)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Weeks was arrested at his place of business for using the mails to transport lottery tickets. While he was in custody, police officers and a United States Marshal entered his home without a warrant \u2014 twice \u2014 and seized letters and private papers, which were turned over to the federal prosecutor. Before trial, Weeks petitioned for the return of his property; the court returned some items but kept the letters, which were admitted over his objection and used to convict him. ## Issue Whether evidence seized by federal officers from a defendant's home without a warrant, in violation of the Fourth Amendment, may be retained and used against him at his federal criminal trial. ## Rule Evidence obtained by federal officers in violation of the Fourth Amendment may not be used against the accused in a federal prosecution. If it could be, the Amendment would be a dead letter:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-398",
      "page": null,
      "quote": "the court should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1914-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Weeks v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jarvis v. Kansas Dept. of Revenue",
          "cluster_id": 4618635,
          "cite": [
            "442 P.3d 1054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dave McNeil v. State",
          "cluster_id": 3094175,
          "cite": [
            "443 S.W.3d 295",
            "2014 WL 3843757",
            "2014 Tex. App. LEXIS 8519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Cal. United States",
          "cluster_id": 2680439,
          "cite": [
            "189 L. Ed. 2d 430",
            "134 S. Ct. 2473",
            "2014 U.S. LEXIS 4497",
            "82 U.S.L.W. 4558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jermaine Lebron v. State of Florida",
          "cluster_id": 2686855,
          "cite": [
            "135 So. 3d 1040",
            "39 Fla. L. Weekly Supp. 62",
            "2014 WL 321817",
            "2014 Fla. LEXIS 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spinelli v. United States",
          "cluster_id": 107831,
          "cite": [
            "21 L. Ed. 2d 637",
            "89 S. Ct. 584",
            "393 U.S. 410",
            "1969 U.S. LEXIS 2701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(98094) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUxNTU1MjAwMDAwJnM9MTA0NTczMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2898094%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(98094)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDE0JnM9MTA4NzY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2898094%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(98094)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 2,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(98094)",
    "indexed_citing_opinions": 2132,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 98094,
        "count": 2132,
        "count_source": "search"
      }
    ],
    "citation_count": 3480,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/weeks-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTgxNDYmcz05NDgxNjY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2898094%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 98094,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 93951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 97412,
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
    "date_created": "2026-07-06T04:11:06Z",
    "date_modified": "2026-07-06T09:17:03Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:13:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Weeks v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b432-5">
  Mr. Justice Day
 </author>
<p id="AXQ">
  delivered the opinion of the court.
 </p>
<p id="b432-6">
  An indictment was returned against the plaintiff in error, defendant below, and herein so designated, in the District Court of the United States for the Western District of Missouri; containing nine counts. The seventh count, upon which a conviction was had, charged, the use of the mails for the purpose of transporting certain coupons or tickets representing chances -or shares in a lottery or gift enterprise, in violation of § 213 of the Criminal Code. Sentence of fine and imprisonment was imposed. This writ of error is to review that judgment.
 </p>
<p id="b432-7">
  The defendant was arrested by a police officer, so far as the record shows, without warrant, at the Union Station in Kansas City, Missouri, where he was employed by an express company. Other police officers had gone to the house of the defendant and being told by a neighbor where the key was kept, found it and entered the house. They searched the defendant’s room and took possession of various papers and articles found there, which were afterwards turned over to the United States Marshal. Later in the same day police officers returned with the Marshal, wfio thought he might find additional evidence, and, being admitted by someone in the house, probably a boarder, in response to- a rap, the Marshal searched the defendant’s room and carried away. certain letters and envelopes found in the drawer of a chiffonier. Neither the marshal nor the police officers had á search warrant.
 </p>
<p id="b433-4">
<span citation-index="1" class="star-pagination" label="387"> 
   *387
   </span>
  The defendant filed in the cause before the time for trial the following petition:
 </p>
<blockquote id="b433-5">
  “Petition to Return Private Papers, Books and Other Property. ■ _
 </blockquote>
<blockquote id="b433-6">
  “Now comes defendant and states that he is a citizen and resident of Kansas City, Missouri, and that he resides, owns and occupies a home at 1834 Penn Street in said City;
 </blockquote>
<blockquote id="b433-7">
  “That on the 21st day of December, 1911, while plaintiff was absent at his daily vocation certain officers of the government whose names are to plaintiff-unknown,' unlawfully and without warrant or authority so to do, broke open the door to plaintiff’s said home and seized all of his books, letters, money, papers, notes, evidences of indebtedness, stock, certificates, insurance policies, deeds, abstracts, and other muniments of title, bonds, candies, clothes and other property in said home, and this in violation of Sections 11 and 23 of the Constitution of Missouri' and of the 4th and 5th Amendments to the Constitution of the United States:
 </blockquote>
<blockquote id="b433-8">
  “That the District Attorney, Marshal and Clerk of the United States Court for the Western District of Missouri took the above described property so seized- into their possession and have failed and refused to return to defendant portion of same, to-wit:
 </blockquote>
<blockquote id="b433-9">
  “One (1) leather grip, value about $7.00; one (1) tin box valued at $3.00; one, (1) Pettis County, Missouri, bond, value $500.00; three (3) Mining stock certificates which defendant is unable to more particularly describe valued at $12&gt;000.00, and certain stock certificates in addition thereto issued by the San Domingo Mining Loan and Investment Company, about $75.00 in currency; one (1) newspaper published about 1790, an heirloom; and certain other property which plaintiff is now unable to describe:
 </blockquote>
<blockquote id="b433-10">
  “That said property is being unlawfully and improperly •
  <span citation-index="1" class="star-pagination" label="388"> 
   *388
   </span>
  held by said District Attorney, Marshal and Clerk in violation of defendant’s rights under the Constitution of the United States and the State of Missouri:
 </blockquote>
<blockquote id="b434-5">
  “ That said District Attorney purposes to use said books, letters, papers, certificates of stock, etc., at the trial of the above entitled cause and that by reason thereof and of the facts above set forth defendant’s rights under the amendments aforesaid to the Constitution of Missouri, and the United States have been and will be violated unless the Court order the return prayed for:
 </blockquote>
<blockquote id="b434-6">
  “Wherefore, defendant prays that said District Attorney, Marshal and Clerk be notified, and that the Court direct and order said District Attorney, Marshal and Clerk to return said property to said defendant.”
 </blockquote>
<p id="b434-7">
  Upon consideration of the petition the court entered in the cause an order directing the return of such property as was not pertinent to the charge against the defendant, but denied the petition as to pertinent matter, reserving the right to pass upon the pertinency at a later time. In obedience to the order the District Attorney returned part of the property taken and retained the remainder, concluding a list of the latter with the statement that, “all of which last above described property is to be used in evidence in the trial of the above entitled cause, and pertains to the alleged sale of lottery tickets of the company above named.”
 </p>
<p id="b434-8">
  After the jury had been sworn and before any evidence had been given, the defendant again urged his petition for the return of his property, which was denied by the court. Upon the introduction of such papers during the' trial, the defendant objected on the ground that the papers had been obtained without a search warrant and by breaking open his home, in violation of the Fourth and Fifth Amendments to the Constitution of the United States, which objection was overruled by the court. Among the papers retained and put in evidence were a number of
  <span citation-index="1" class="star-pagination" label="389"> 
   *389
   </span>
  lottery tickets and statements with reference to the lottery, taken at the first visit of the police to the defendant’s room, and a number of letters written to the defendant in respect to the lottery, taken by the Marshal upon his search of defendant’s room.
 </p>
<p id="b435-5">
  The defendant assigns error, among other things, in the court’s refusal to grant his petition for the return of his property and in permitting the papers to be used at the trial.
 </p>
<p id="b435-6">
  It is thus apparent that the question presented involves the determination of the duty of the court with reference to the motion made by the defendant for the return of certain letters, as well as other papers, taken from his room by the United States Marshal, who, without authority of process, if any such could have been legally issued, visited the room of the defendant for the declared purpose of obtaining additional testimony to support the charge against the accused, and having gained admission to the house took from the drawer of a chiffonier there found certain letters written to the defendant, tending to show his guilt. These letters were placed in the control of the District Attorney and were subsequently produced by him and offered in evidence against the accused at the trial. The defendant contends that such appropriation of his private correspondence was in violation of rights secured to him by the Fourth and Fifth Amendments to the Constitution of the United States. We shall deal with the Fourth Amendment, which provides:
 </p>
<blockquote id="b435-7">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation and particularly' describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b435-8">
  The history of this Amendment is given with particularity in the opinion of Mr. Justice Bradley, speaking for
  <span citation-index="1" class="star-pagination" label="390"> 
   *390
   </span>
  the court in
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>. As was there shown, it took its origin in the determination of the framers of the Amendments to the Federal Constitution to provide for that instrument a Bill of Rights, securing to the American people, among other things, those safeguards which had grown up in England to protect the people from unreasonable searches and seizures, such as were permitted under the general warrants issued under authority of the Government by which there had been invasions of the home and privacy of the citizens and the seizure of their private papers in support of charges, real or imaginary, made against them. Such practices had also received sanction under warrants and seizures under the so-called writs of assistance, issued in the American colonies. See 2 Watson on the Constitution, 1414
  <em>
   et seq.
  </em>
  Resistance to these practices had established the principle which was enacted into the fundamental law in the Fourth Amendment, that a man’s house was his castle and not to be invaded by any general authority to search and seize his goods and papers. Judge Cooley, in his Constitutional Limitations, pp. 425, 426, in treating of this feature of our Constitution, said: “The maxim that ‘every man’s house is his castle,’ is made a part of our constitutional law in the clauses prohibiting unreasonable searches and seizures, and has always been looked upon as of high value to the citizen.” “Accordingly,” says Lieber in his work on Civil Liberty and Self-Government, 62, in speaking of the English law in this respect, “no man’s house can be forcibly opened, or he or his goods be carried away after it has thus been forced, except in cases of felony, and then the sheriff must be furnished with a warrant, and take great care lest he commit a trespass. This principle is jealously insisted upon.” In
  <em>
   Ex parte Jackson,
  </em>
  <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span>, this court recognized the principle of protection as applicable to letters and sealed packages in the mail, and held that consistently
  <span citation-index="1" class="star-pagination" label="391"> 
   *391
   </span>
  with this guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures such matter could only be opened and examined upon warrants issued on oath or affirmation particularly describing the thing to be seized, “as is required when papers are subjected to search in one’s own household.”
 </p>
<p id="b437-5">
  In the
  <em>
   Boyd Case, supra,
  </em>
  after citing Lord Camden’s, judgment in
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington,
  </em>
  19 Howell’s State Trials, 1029, Mr. Justice Bradley said (630):
 </p>
<blockquote id="b437-6">
  “The principles laid down in this opinion affect the very , essence of constitutional liberty and security. They reach farther than the concrete form of the case then before the court, with its adventitious.circumstances; they apply to all invasions on the part of the government and its employés of the sanctity of a man’s home and the privacies of life. It is not the breaking of h'is doors, and the' rummaging of his drawers, that constitutes the essence of the- offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property, where that right has never been forfeited by his conviction of some public offence, — it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden’s judgment.”
 </blockquote>
<p id="b437-7">
  In
  <em>
   Bram
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>, this court in speaking by the present Chief Justice of
  <em>
   Boyd’s Case,
  </em>
  dealing with the Fourth and Fifth Amendments, said (544): ■
 </p>
<blockquote id="b437-8">
  . “It was in that casa demonstrated that both of these Amendments contemplated perpetuating, in their full efficacy, by means of a constitutional provision, principles of humanity and civil liberty, which had been secured in the mother country only after years of-struggle, so as to implant them in our institutions in-'the fullness of their integrity, free from the possibilities of future legislative change.” ■ ;
 </blockquote>
<p id="b437-9">
  The effect of the Fourth Amendment is to put the courts
  <span citation-index="1" class="star-pagination" label="392"> 
   *392
   </span>
  of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law. This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws. The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures and enforced confessions, the latter often obtained after subjecting accused persons to unwarranted practices destructive of rights secured by the Federal Constitution, should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.
 </p>
<p id="b438-5">
  What then is the present case? Before answering that inquiry specifically, it may be, well by a process of exclusion to state what it is not. It is not án assertion of the right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime. This right has been uniformly maintained in many cases. 1 Bishop on Criminal Procedure, §211; Wharton, Crim. Plead, and Practice, 8th ed., § 60;
  <em>
   Dillon
  </em>
  v.
  <em>
   O’Brien and Davis,
  </em>
  16 Cox C. C. 245. Nor is it the case of testimony offered at a trial where the court is asked to stop and consider the illegal means by which proofs, otherwise competent, were obtained — of which we shall have occasion to treat later in this opinion. Nor is it the case of burglar’s tools or other proofs of guilt found upon his arrest within the control of the accused.
 </p>
<p id="b439-4">
<span citation-index="1" class="star-pagination" label="393"> 
   *393
   </span>
  The case in the aspect in which we are dealing with it involves the right of the court in a criminal prosecution to retain for the purposes of evidence the letters and correspondence of the accused, seized in his house in his absence and without his authority, by a United States Marshal holding no warrant for his arrest and none for the search of his premises. The accused, without awaiting his trial,, made timely application to the court for an order for the, return of these letters, as well as other property. This application was denied, the letters retained and put in evidence, after a further application at the beginning of the trial, both applications asserting the rights of the accused under the Fourth and Fifth Amendments to the Constitution. If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures, is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land. The United States Marshal could only have invaded the house of the accused when armed with a warrant issued as required' by the Constitution, upon sworn information and describing with reasonable particularity the thing for which the search was to be made. Instead, he acted without sanction of law, doubtless prompted by the desire to bring further proof to the aid of the Government, and under color of his office undertook to make a seizure of private papers in direct violation of the constitutional prohibition against such action. Under such circumstances, without sworn information and particular description, not even an order of court would
  <span citation-index="1" class="star-pagination" label="394"> 
   *394
   </span>
  have justified such procedure, much less was it within the authority of the United States Marshal to thus invade the house and privacy of the accused. In
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>, this court said that the Fourth Amendment was intended to secure the citizen in person and property against unlawful invasion of the sanctity of his home by officers of the law acting under legislative or judicial sanction. This protection is equally extended to the action of the Government and officers of the law acting under it.
  <em>
   (Boyd Case, supra.)
  </em>
  To sanction such proceedings would be to affirm by judicial decision a manifest neglect if not an open defiance of the prohibitions of the Constitution,- intended for the protection of the people against such unauthorized action.
 </p>
<p id="b440-5">
  The court before which the application was made in this case recognized the illegal character of the seizure and ordered the return of property not in its judgment competent to be offered at the trial, but refused the application of the accused to turn over the letters, which were afterwards put in evidence on behalf of the Government. While there is no opinion in the case, the court in this proceeding doubtless relied upon what is now contended by the Government to be the correct rule of law under such circumstances, that the letters having come into the control of the court,' it would not inquire into the manner in which they were obtained, but if competent would keep them and permit their use in evidence. Such proposition, the Government asserts, is conclusively established by certain decisions of this court, the first' of which is
  <em>
   Adams
  </em>
  v.
  <em>
   New <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">York, supra.</a></span>
  </em>
  In that case the plaintiff in error had been convicted in the. Supreme Court of the State of New York for having in his possession certain gambling paraphernalia used in the game known as policy, in violation of the Penal Code of New York. At the trial certain papers, which had been seized by police • officers executing a search warrant for the discovery and
  <span citation-index="1" class="star-pagination" label="395"> 
   *395
   </span>
  seizure of policy slips and which had been found in addition to the policy slips, were offered in evidence over his objection. The conviction was affirmed by the Court of Appeals of New York (176 N.-Y. 351), and the case was brought here for alleged violation of the Fourth and Fifth Amendments to the Constitution of the United States. Pretermitting the question whether these amendments applied to the action of the States, this court proceeded to examine the alleged violations of the Fourth and Fifth Amendments, and put its decision upon the ground that the papers found in the execution of the search warrant, which warrant had a legal purpose in the attempt to find gambling paraphernalia, were competent evidence against the accused, and their offer in testimony did not violate his constitutional privilege against unlawful search or seizure, for it was held that such incriminatory documents thus discovered were not the subject of an unreasonable search and seizure, and in effect that the same were incidentally seized in the lawful execution of a warrant and not in the wrongful invasion of the home of the citizen and the unwarranted seizure of his papers and property. It was further held, approving in that respect the doctrine laid down in 1 Greenleaf, § 254a, that it was no valid objection to the usq of the papers that they had been thus seized, and that the courts in the course of a trial would not make an issue to determine that question, and many state cases were cited supporting that doctrine.
 </p>
<p id="b441-5">
  The same point had been ruled in
  <em>
   People
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, from‘which decision the case was brought to this court, .where it was held that if the papers seized in ■ addition to the policy slips were competent evidence in the case, as the court held they were, they were admissible in evidence at the trial, the court saying (p. 358): “The underlying principle obviously is that the court, when engaged in trying a criminal causé, will not take notice of
  <span citation-index="1" class="star-pagination" label="396"> 
   *396
   </span>
  the manner in which witnesses have possessed themselves of papers, or other articles of personal property, which are material and properly offered in evidence.” This doctrine thus laid down by the New York Court of Appeals and approved by this court, that a court will not in trying a criminal cause permit a collateral issue to be raised as to the source of competent testimony, has the sanction of so many state cases that it would be impracticable to cite or refer to them in detail. Many of them are collected in the note to
  <em>
   State
  </em>
  v.
  <em>
   Turner,
  </em>
  <span class="citation no-link">136 Am. St. Rep. 129</span>, 135
  <em>
   et seq.
  </em>
  After citing numerous cases the editor says: “The underlying principle of all these decisions obviously is, that the court, when engaged in the trial of a criminal action, will not take notice of the manner in which a witness has possessed himself of papers or other chattels, subjects of evidence, which are material and properly offered in evidence:
  <em>
   People
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation no-link">98 Am. St. Rep. 675</span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>, 63 L. R. A. 406. Such an investigation is not involved necessarily in the litigation in chief, and to pursue it would be to halt in the orderly progress of a cause, and consider incidentally a question which has happened to cross the path of such litigation, and which is wholly independent thereof.”
 </p>
<p id="b442-5">
  It is therefore evident that the
  <em>
   Adams Case
  </em>
  affords no authority for the action of the court in this case, when applied, to in due season for the return of papers seized in violation of the Constitutional Amendment. The decision in that case rests upon incidental seizure made in the execution of a legal warrant and in the application of the doctrine that a collateral issue will not be raised to ascertain the source from which testimony, competent in a criminal case, comes.
 </p>
<p id="b442-6">
  The Government also relies upon
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span>, in which the previous cases of
  <em>
   Boyd
  </em>
  v.
  <em>
   United States, supra, Adams
  </em>
  v.
  <em>
   New. <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">York, supra,</a></span> Interstate Com
  </em>
<span citation-index="1" class="star-pagination" label="397"> 
   *397
   </span>
<em>
   merce Commission
  </em>
  v.
  <em>
   Brimson,
  </em>
  <span class="citation" data-id="93951"><a href="/opinion/93951/interstate-commerce-commission-v-brimson/" aria-description="Citation for case: Interstate Commerce Commission v. Brimson">154 U. S. 447</a></span>, and
  <em>
   Interstate Commerce Commission
  </em>
  v.
  <em>
   Baird,
  </em>
  <span class="citation" data-id="96063"><a href="/opinion/96063/interstate-commerce-commission-v-baird/" aria-description="Citation for case: Interstate Commerce Commission v. Baird">194 U. S. 25</a></span>, are reviewed, and wherein it was held that a
  <em>
   subpoena duces tecum
  </em>
  requiring a corporation to produce all its contracts and correspondence with no less than six other companies, as well as all letters received by the corporation from thirteen other companies located in different parts of the United States, was an unreasonable search and seizure within the Fourth Amendment, and it was there stated that (201 U. S. p. 76) “an order for the production of books and papers may constitute an unreasonable search and seizure within the Fourth Amendment. While a search ordinarily implies a quest by an officer of the law, and a seizure contemplates a forcible dispossession of the owner, still, as was held in the
  <em>
   Boyd Case,
  </em>
  the substance of the offense is the compulsory production of private papers, whether under a search warrant or a
  <em>
   subpoena duces tecum,
  </em>
  against which the person, be he individual or corporation, is entitled to protection.” If such a seizure under the authority of a warrant supposed to be legal, constitutes a violation of the constitutional protection,
  <em>
   a fortiori
  </em>
  does the attempt of an officer of the United States, the United States Marshal, acting under color of his office, without even the sanction of a warrant, constitute an invasion of the rights within the protection afforded by the Fourth Amendment.
 </p>
<p id="b443-5">
  Another case relied upon is
  <em>
   American Tobacco Co.
  </em>
  v.
  <em>
   Werckmeister,
  </em>
  <span class="citation" data-id="96731"><a href="/opinion/96731/american-tobacco-co-v-werckmeister/" aria-description="Citation for case: American Tobacco Co. v. Werckmeister">207 U. S. 284</a></span>, in which it was held that the seizure by the United States Marshal in a copyright case of certain pictures under a writ of replevin did not constitute an unreasonable search and seizure. The other case from this court relied upon is
  <em>
   Holt
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>, in which it was held that testimony tending to show that a certain blouse which was in evidence as ■ incriminating him, had been put upon the prisoner and fitted him, did not violate his constitutional right. We
  <span citation-index="1" class="star-pagination" label="398"> 
   *398
   </span>
  are at a loss to see the application of these cases to the one in hand.
 </p>
<p id="b444-4">
  . The right of the court to deal with papers and documents in the possession of the District Attorney and other officers of the court and subject to its authority was recognized in
  <em>
   Wise
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="97412"><a href="/opinion/97412/wise-v-henkel/" aria-description="Citation for case: Wise v. Henkel">220 U. S. 556</a></span>. That papers wrongfully seized should be turned over to the accused has been frequently recognized in the early as well as later decisions of the courts. 1 Bishop on Criminal Procedure, § 210;
  <em>
   Rex v. Barnett,
  </em>
  3 C. &amp; P. 600;
  <em>
   Rex
  </em>
  v.
  <em>
   Kinsey,
  </em>
  7 C. &amp; P. 447;
  <em>
   United States
  </em>
  v.
  <em>
   Mills,
  </em>
  185 Fed. Rep. 318;
  <em>
   United States
  </em>
  v.
  <em>
   McHie,
  </em>
  194 Fed. Rep. 894, 898.
 </p>
<p id="b444-5">
  We therefore reach the conclusion that the letters in question were taken from the house of the accused by an official of the United States acting under color of his office in direct violation of the constitutional rights of the defendant; that having made a seasonable application for their return, which was heard and passed upon by the court, there was involved in the order refusing the application a denial of the constitutional rights of the accused, and that the court , should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed. As to the papers and property seized by the policemen, it does not appear that they acted under any claim of Federal authority such .as would make the Amendment applicable to such unauthorized seizures. The record shows that what they did by way of arrest and search and seizure was done before the finding of the indictment in the Federal court, under what supposed right or authority does not appear. What remedies the defendant may have against them we need not inquire, as the Fourth Amendment is not directed to individual misconduct of such officials. Its limitations reach the Federal Government and its agencies.
  <em>
   Boyd Case,
  </em>
  116 U. S.,
  <em>
   supra,
  </em>
  and see
  <em>
   Twining
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>.
 </p>
<p id="b445-3">
<span citation-index="1" class="star-pagination" label="399"> 
   *399
   </span>
  It results that the judgment of the court below must be reversed, and the case remanded for further proceedings in accordance with this opinion.
 </p>
<p id="b445-4">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/Whiteley v. Warden.md  (`case`, 5 assertions)

### content_page

```
---
title: "Whiteley v. Warden"
type: case
citation: "401 U.S. 560 (1971)"
parallel_cite: "91 S. Ct. 1031; 28 L. Ed. 2d 306; 58 Ohio Op. 2d 434"
neutral_cite: 1971 U.S. LEXIS 65
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-03-29
docket: 351
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-03-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Whiteley v. Warden
  varies_by_point: false
  scope_note: "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/"
  cluster_id: 108297
  opinion_id: 9424493
  identity_checked: true
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key — Anchor"
related: ["[[United States v. Hensley]]", "[[Herring v. United States]]", "[[Mapp v. Ohio]]"]
aliases: ["Whiteley v. Warden, Wyoming State Penitentiary", "Whiteley"]
tags: ["case", "fourth-amendment", "collective-knowledge", "fellow-officer-rule", "probable-cause", "radio-bulletin"]
holding: "An officer may act on the strength of a police radio bulletin and assume the issuing officer had probable cause. But where the issuing…"
lake:
  record_id: Whiteley v. Warden
  status: verified
  projected_at: 2026-07-06
---

# Whiteley v. Warden

*401 U.S. 560 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a county-building break-in in Wyoming, a county sheriff acting on an informer's tip filed a bare, conclusory complaint and obtained an arrest warrant for Whiteley and Daley, then issued a statewide police radio bulletin describing the men and their car. Laramie police, relying on the bulletin, stopped the car, arrested the two men, and searched the vehicle, recovering tools and other evidence of the burglary. Whiteley sought [[Common Legal Terms#habeas-corpus|habeas]] relief, arguing the arrest lacked probable cause.

## Issue
Whether an arrest made by officers relying on a police bulletin is lawful when the officer who issued the bulletin (and obtained the underlying warrant) did not himself have probable cause.

## Rule
An officer may act on a fellow officer's bulletin or request, but the validity of the arrest still depends on probable cause existing somewhere in the originating chain: "police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest." — 401 U.S. at 568. ^pin-568

When the originating officer lacked probable cause, the arrest is unlawful and its fruits must be suppressed: "petitioner's arrest violated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial." — *Id.* at 568–569. ^pin-569

## Application
On these facts the arresting officers were entitled to rely on the bulletin, but the chain failed at its source. The complaint underlying the warrant stated only the complainant's conclusion and omitted the informer's tip and every operative fact, so it could not support a magistrate's probable-cause finding. The arresting officers, in turn, knew only what the bulletin told them plus the matching car and description — nothing corroborating the tip that these men committed the burglary. Because no one in the chain actually possessed probable cause, the arrest violated the Fourth Amendment, and the evidence seized incident to it should have been excluded.

## Conclusion
The arrest was unconstitutional and the evidence inadmissible; the writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] should issue. Good-faith reliance on a fellow officer's bulletin cannot supply probable cause the originating officer never had.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the collective-knowledge principle, which was applied to investigative stops in [[United States v. Hensley]] (1985). [[Herring v. United States]] (2009) later addressed the separate question of suppression when officers reasonably rely on another agency's erroneous records, declining to suppress where the error was isolated negligence — a good-faith refinement of the *Whiteley/Mapp* exclusionary remedy rather than a change to the probable-cause rule.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key — Anchor*

## Sources
- *Whiteley v. Warden*, 401 U.S. 560 (1971) — https://www.courtlistener.com/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/ — pinpoints: 568, 568–569.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ff609fa2f9a9a04f", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "401 U.S. 560 (1971)", "court": "U.S. Supreme Court", "neutral_cite": "1971 U.S. LEXIS 65", "official_citation_present": true, "parallel_cite": "91 S. Ct. 1031; 28 L. Ed. 2d 306; 58 Ohio Op. 2d 434", "title": "Whiteley v. Warden", "year": "1971"}}
{"assertion_id": "32e3ab8b9e98d9de", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer may act on the strength of a police radio bulletin and assume the issuing officer had probable cause. But where the issuing…", "title": "Whiteley v. Warden"}}
{"assertion_id": "a7b5c421e05cd417", "dimension": "support", "kind": "home_role", "locator": {"home": "Collective Knowledge and the Fellow-Officer Rule"}, "payload": {"home": "Collective Knowledge and the Fellow-Officer Rule", "role": "Key — Anchor", "title": "Whiteley v. Warden"}}
{"assertion_id": "0751f25c25ea5ea5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Whiteley v. Warden"}}
{"assertion_id": "6c24a4b8f2d06723", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1971-03-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Whiteley v. Warden", "field_i_validity": "good_law", "scope_note": "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records.", "title": "Whiteley v. Warden", "varies_by_point": "false"}}
```

### lake record — Whiteley v. Warden

```json
{
  "schema_version": "s2.v1",
  "record_id": "Whiteley v. Warden",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Whiteley v. Warden, Wyoming State Penitentiary",
    "case_name_short": "Whiteley",
    "case_name_full": "Whiteley v. Warden, Wyoming State Penitentiary",
    "input_case_name": "Whiteley v. Warden",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-03-29",
    "year": 1971,
    "docket": "351",
    "cluster_id": 108297,
    "lead_opinion_id": 9424493,
    "sibling_ids": [
      108297,
      9424493,
      9424494
    ],
    "absolute_url": "/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 560",
      "volume": "401",
      "reporter": "U.S.",
      "page": "560",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 1031",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 306",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 Ohio Op. 2d 434",
        "volume": "58",
        "reporter": "Ohio Op. 2d",
        "page": "434",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 65",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 560",
        "volume": "401",
        "reporter": "U.S.",
        "page": "560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 1031",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 306",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 65",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 Ohio Op. 2d 434",
        "volume": "58",
        "reporter": "Ohio Op. 2d",
        "page": "434",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 560",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 560",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-568",
      "page": null,
      "quote": "--- # Whiteley v. Warden *401 U.S. 560 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After a county-building break-in in Wyoming, a county sheriff acting on an informer's tip filed a bare, conclusory complaint and obtained an arrest warrant for Whiteley and Daley, then issued a statewide police radio bulletin describing the men and their car. Laramie police, relying on the bulletin, stopped the car, arrested the two men, and searched the vehicle, recovering tools and other evidence of the burglary. Whiteley sought habeas relief, arguing the arrest lacked probable cause. ## Issue Whether an arrest made by officers relying on a police bulletin is lawful when the officer who issued the bulletin (and obtained the underlying warrant) did not himself have probable cause. ## Rule An officer may act on a fellow officer's bulletin or request, but the validity of the arrest still depends on probable cause existing somewhere in the originating chain:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-569",
      "page": null,
      "quote": "petitioner's arrest violated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-03-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Whiteley v. Warden",
    "varies_by_point": false,
    "scope_note": "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Charlotte Lynn Frazier And Andrea Parks",
          "cluster_id": 4538535,
          "cite": [
            "558 S.W.3d 145"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
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
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry Smith v. The State of Wyoming",
          "cluster_id": 1043203,
          "cite": [
            "2013 WY 122",
            "311 P.3d 132",
            "2013 WL 5507295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Haslam, 08-Mo-4 (2-10-2009)",
          "cluster_id": 3937404,
          "cite": [
            "2009 Ohio 696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Crews",
          "cluster_id": 110230,
          "cite": [
            "63 L. Ed. 2d 537",
            "100 S. Ct. 1244",
            "445 U.S. 463",
            "1980 U.S. LEXIS 1293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Deville v. Marcantel",
          "cluster_id": 65780,
          "cite": [
            "567 F.3d 156",
            "2009 U.S. App. LEXIS 9403",
            "2009 WL 1162586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Andreas",
          "cluster_id": 111013,
          "cite": [
            "77 L. Ed. 2d 1003",
            "103 S. Ct. 3319",
            "463 U.S. 765",
            "1983 U.S. LEXIS 106",
            "51 U.S.L.W. 5157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Maumee v. Weisner",
          "cluster_id": 2689810,
          "cite": [
            "1999 Ohio 68",
            "87 Ohio St. 3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tisler",
          "cluster_id": 2162728,
          "cite": [
            "469 N.E.2d 147",
            "103 Ill. 2d 226",
            "82 Ill. Dec. 613",
            "1984 Ill. LEXIS 331"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walczyk v. Rio",
          "cluster_id": 2704,
          "cite": [
            "496 F.3d 139",
            "2007 WL 2199005"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shadwick v. City of Tampa",
          "cluster_id": 108582,
          "cite": [
            "32 L. Ed. 2d 783",
            "92 S. Ct. 2119",
            "407 U.S. 345",
            "1972 U.S. LEXIS 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harvey",
          "cluster_id": 1343416,
          "cite": [
            "187 S.E.2d 706",
            "281 N.C. 1",
            "1972 N.C. LEXIS 1321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108297 OR 9424493 OR 9424494) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDYxMjUxMjAwMDAwJnM9MTM3NjIyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108297+OR+9424493+OR+9424494%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108297 OR 9424493 OR 9424494)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDgmcz00NjYxNDM2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108297+OR+9424493+OR+9424494%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108297 OR 9424493 OR 9424494)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 1,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108297 OR 9424493 OR 9424494)",
    "indexed_citing_opinions": 1201,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108297,
        "count": 1100,
        "count_source": "search"
      },
      {
        "opinion_id": 9424493,
        "count": 147,
        "count_source": "search"
      },
      {
        "opinion_id": 9424494,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1845,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/whiteley-v-warden.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NDE3NDYmcz01MjYyODE3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108297+OR+9424493+OR+9424494%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108297,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 286552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 1296591,
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
    "date_created": "2026-07-06T04:19:47Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:22:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Whiteley v. Warden

```
<opinion type="majority">
<author id="b645-11">Mr. Justice Harlan</author>
<p id="AOZt">delivered the opinion of the Court.</p>
<p id="b645-12">Petitioner Whiteley, in 1965, was convicted in the District Court for the Second Judicial District of the State of Wyoming on charges of breaking and entering and being an habitual criminal.<footnotemark>1</footnotemark> Both at his arraignment and at trial Whiteley challenged the constitutionality of the use of evidence seized during a search incident to an arrest which he claimed was illegal. The trial court overruled petitioner’s motion to suppress, and on appeal the Supreme Court of Wyoming affirmed. <em>Whiteley </em>v. <em>State, </em><span class="citation" data-id="1296591"><a href="/opinion/1296591/whiteley-v-state/" aria-description="Citation for case: Whiteley v. State">418 P. 2d 164</a></span> (1966). This proceeding commenced with a petition for habeas corpus in the United States District Court for the District of Wyoming, which was denied on November 25, 1968.<footnotemark>2</footnotemark> <em>Whiteley </em>v. <em>Wyoming, </em><span class="citation" data-id="8768821"><a href="/opinion/8784984/whiteley-v-wyoming/" aria-description="Citation for case: Whiteley v. Wyoming">293 F. Supp. 381</a></span>. On appeal, the United States Court of Appeals for <page-number citation-index="1" label="562">*562</page-number>the Tenth Circuit affirmed. <em>Whiteley </em>v. <em>Meacham, </em><span class="citation" data-id="286552"><a href="/opinion/286552/harold-whiteley-v-leonard-meacham-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Harold Whiteley v. Leonard Meacham, Warden, Wyoming State...">416 F. 2d 36</a></span> (1969). We granted certiorari, limiting the writ to the issue of the constitutionality of the arrest and ensuing search and seizure. <span class="citation multiple-matches"><a href="/c/U.%20S./397/1062/">397 U. S. 1062</a></span> (1970).<footnotemark>3</footnotemark> We reverse the judgment of the Tenth Circuit for the reasons stated herein.</p>
<p id="b646-5">I</p>
<p id="b646-6">The circumstances surrounding petitioner’s arrest and the incidental search and seizure, as stated by the Wyoming Supreme Court, <span class="citation" data-id="1296591"><a href="/opinion/1296591/whiteley-v-state/#165" aria-description="Citation for case: Whiteley v. State">418 P. 2d 164, 165-166</a></span>, are as follows:<footnotemark>4</footnotemark></p>
<blockquote id="b646-7">“On November 23, 1964, certain business establishments in Saratoga were broken into, including the Rustic Bar and Shively’s Hardware, the offenses being investigated by the Carbon County Sheriff [Sheriff Ogburn] who, acting on a tip, the next day signed a complaint charging defendant and another with breaking and entering the building identified <page-number citation-index="1" label="563">*563</page-number>as the Rustic Bar. This complaint was made before a justice of the peace at approximately 11:30 a. m. on the 24th, and a warrant issued. After the investigation, the sheriff put out a state item on the radio to pick up two suspects of the breaking and entering, defendant and another. The message went to the network at Casper and was transmitted over the State, received by the Albany County Sheriff’s Office and communicated to the Laramie Police Department, the message giving names and descriptions of the two persons and advising the type of car probably being driven and the amount of money taken, including certain old coins with the dates. Late at night on November 24, a Laramie patrolman, in reliance on the information in the radio item, arrested the defendant and his companion. At the time, the patrolman had no warrant for defendant’s arrest nor search warrant. The officer together with a deputy sheriff, who had come up in the meantime, searched the car and removed a number of items introduced in evidence, including tools and old coins, identified at the trial as taken from Shively’s Hardware. . . .”</blockquote>
<p id="b647-5">Sheriff Ogburn’s complaint, which provided the basis for the arrest warrant issued by the justice of the peace, is as follows:</p>
<blockquote id="b647-6">“I, C. W. Ogburn, do solemnly swear that on or about the 23 day of November, A. D. 1964, in the County of Carbon and State of Wyoming, the said Harold Whiteley and Jack Daley, defendants did then and there unlawfully break and enter a locked and sealed building [describing the location and ownership of the building].” App. 28.</blockquote>
<p id="b647-7">A state item 881, the bulletin which Sheriff Ogburn <page-number citation-index="1" label="564">*564</page-number>put out on the radio and which led to petitioner’s arrest and search by the Laramie patrolman, is as follows:</p>
<blockquote id="b648-5">“P &amp; H for B &amp; E Saratoga, early A. M. 11-24-64. Subj. #1. Jack Daley, WMA, 38, D. O. B. 2-29-[26], 5'10", 175, med. build, med. comp., blonde and blue. Tat. left shoulder: 'Love Me or Leave Me.’ #2. Harold Whitley, WMA, 43, D. O. B. 6-22-21, 5' 11", 180, med. build, fair comp, brown eyes. Tat. on right arm 'Bird.’ Poss. driving 1953 or 1954 Buick, light green bottom, dark top. Wyo. lie. 2-bal. unknown. Taken: $281.71 in small change, numerous old coins ranging from <em>,5‡ </em>pieces to silver dollars, dated from 1853 to 1908. Warrant issues, will extradite. Special attention Denver. . . .” App. 31.<footnotemark>5</footnotemark></blockquote>
<p id="b648-6">II</p>
<p id="b648-7">The decisions of this Court concerning Fourth Amendment probable-cause requirements before a warrant for either arrest or search can issue require that the judicial officer issuing such a warrant be supplied with sufficient information to support an independent judgment that probable cause exists for the warrant.<footnotemark>6</footnotemark> <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969); <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> <em>(1965); Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <em>Rugendorf </em>v. <em>United States, </em><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960); <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). In the instant case — so far as the record stipulated to by the parties <page-number citation-index="1" label="565">*565</page-number>reveals<footnotemark>7</footnotemark> — the sole support for the arrest warrant issued at Sheriff Ogburn’s request was the complaint reproduced above.<footnotemark>8</footnotemark> That complaint consists of nothing more than the complainant’s conclusion that- the individuals named therein perpetrated the offense described in the complaint. The actual basis for Sheriff Ogburn’s conclusion was an informer’s tip, but that fact, as well as every other operative fact, is omitted from the complaint. Under the cases just cited, that document alone could not support the independent judgment of a disinterested magistrate.</p>
<p id="b649-5">The State,<footnotemark>9</footnotemark> however, contends that regardless of the sufficiency of the complaint to support the arrest warrant, the Laramie police officer who actually made the <page-number citation-index="1" label="566">*566</page-number>arrest possessed sufficient factual information to support a finding of probable cause for arrest without a warrant. In support of this proposition, the State argues that a reviewing court should employ less stringent standards for reviewing a police officer’s assessment of probable cause as a prelude to a warrantless arrest than the court would employ in reviewing a magistrate’s assessment as a prelude to issuing an arrest or search warrant.<footnotemark>10</footnotemark> That proposition has been consistently rejected by this Court. <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#105" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 105-109</a></span>; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 110-111</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S., at 270-271</a></span>. And the reason for its rejection is both fundamental and obvious: less stringent standards for reviewing the officer’s discretion in effecting a warrantless arrest and search would discourage resort to the procedures for obtaining a warrant. Thus the standards applicable to the factual basis supporting the officer’s probable-cause assessment at the time of the challenged arrest and search are at least as stringent as the standards applied with respect to the magistrate’s assessment. See <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#304" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 304-305</a></span> (1967).</p>
<p id="b650-5">Applying those standards to the instant case, the information possessed by the Laramie police officer at the time of arrest and search consisted of: (1) the data contained in state bulletin 881, reproduced <em>supra; </em>(2) the knowledge, obtained by personal observation, that two men were driving a car matching the car described in the radio bulletin; (3) the knowledge, possessed by one of the arresting officers, that one of the people in the car was Jack Daley, App. 71; (4) the knowledge, acquired <page-number citation-index="1" label="567">*567</page-number>by personal observation, that the other individual in the car fitted the description of Whiteley contained in state bulletin 881; and (5) the knowledge, acquired by the officer after stopping Whiteley, that he had given a false name.<footnotemark>11</footnotemark></p>
<p id="b651-5">This Court has held that where the initial impetus for an arrest is an informer’s tip, information gathered by the arresting officers can be used to sustain a finding of probable cause for an arrest that could not adequately be supported by the tip alone. <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959). See <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). But the additional information acquired by the arresting officers must in some sense be corroborative of the informer’s tip that the arrestees committed the felony or, as in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>itself, were in the process of committing the felony. See the opinions of the Court and that of Me. Justice White concurring in <em>Spinelli </em>v. <em>United States, supra, </em>and p. 423. In the present case, the very most the additional information tended to establish is that either Sheriff Ogburn, or his informant, or both of them, knew Daley and Whiteley and the kind of car they drove; the record is devoid of any information at any stage of the proceeding from the time of the burglary to the event of the arrest and search that would support either the reliability of the informant or the informant’s conclusion that these men were connected with the crime. <em>Spinelli </em>v. <em>United States, supra; McCray </em>v. <em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">Illinois, supra;</a></span> Aguilar </em>v. <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra.</a></span></em></p>
<p id="b652-4"><page-number citation-index="1" label="568">*568</page-number>The State, however, offers one further argument in support of the legality of the arrest and search: the Laramie police relied on the radio bulletin in making the arrest, and not on Sheriff Ogburn’s unnamed informant. Clearly, it is said, they had probable cause for believing that the passengers in the car were the men described in the bulletin, and, in acting on the bulletin, they reasonably assumed that whoever authorized the bulletin had probable cause to direct Whiteley’s and Daley’s arrest. To prevent arresting officers from acting on the assumption that fellow officers who call upon them to make an arrest have probable cause for believing the arrestees are perpetrators of a crime would, it is argued, unduly hamper law enforcement.</p>
<p id="b652-5">We do not, of course, question that the Laramie police were entitled to act on the strength of the radio bulletin. Certainly police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.</p>
<p id="b652-6">In sum, the complaint on which the warrant issued here clearly could not support a finding of probable cause by the issuing magistrate. The arresting officer was not himself possessed of any factual data tending to corroborate the informer’s tip that Daley and Whiteley committed the crime.<footnotemark>12</footnotemark> Therefore, petitioner’s arrest vio<page-number citation-index="1" label="569">*569</page-number>lated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial. <em>Mapp </em>v. Ohio, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p id="b653-5">Ill</p>
<p id="b653-6">There remains the question as to the proper disposition of this case. The State urges us to remand so that it will have an opportunity to develop a record which might show that the issuing magistrate had factual information additional to that presented in Sheriff Ogburn’s complaint. Brief for Respondent 8-9. Yet the State concedes, as on the record it must, that at every stage in the proceedings below petitioner argued the insufficiency of the warrant as well as the lack of probable cause at the time of the arrest. Brief for Respondent 4. Knowing the basis for petitioner’s constitutional claim, the State chose to try those proceedings on the record it had developed in the state courts. See n. 4, <em>supra. </em>Its sole explanation for this state of affairs is that “the state has felt, based on precedent and logic, that no court would accept the legal reasoning of petitioner.” Brief for Respondent 9. In the circumstances of this case, that justification, as we have shown, is untenable.</p>
<p id="b653-7">Pursuant to our authority under <span class="citation no-link">28 U. S. C. § 2106</span> to make such disposition of the case “as may be just under the circumstances,” we reverse the judgment of the Tenth Circuit and remand with directions that the writ is to issue unless the State makes appropriate arrangements to retry petitioner.<footnotemark>13</footnotemark> Cf. <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#487" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 487-488</a></span>.</p>
<p id="b653-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b645-13"> He was given concurrent sentences on the breaking and entering charges of one to 10 years and, in consequence of the recidivist charge, imprisonment for life.</p>
</footnote>
<footnote label="2">
<p id="b645-14"> Prior to commencing federal habeas corpus proceedings, Whiteley had filed a petition for post-conviction relief pursuant to the Wyoming statutes. No appeal was taken from the denial of that petition.</p>
</footnote>
<footnote label="3">
<p id="b646-8"> In his petition for habeas corpus, Whiteley raised several other issues which had previously been advanced in his state petition for post-conviction relief, but not in his direct appeal to the Supreme Court of Wyoming. On these other issues, both lower federal courts held that failure to appeal the denial of his state post-conviction petition constituted nonexhaustion of state remedies. Petitioner sought to raise the exhaustion issue in his present petition for certiorari, but, as noted in text, we granted the writ limited to the search and seizure issue decided by the lower federal courts.</p>
</footnote>
<footnote label="4">
<p id="b646-9"> At the outset of the federal habeas corpus proceeding now before us, both parties entered into the following stipulation, App. 10:</p>
<blockquote id="b646-10">“IT IS HEREBY STIPULATED by and between the parties through their respective counsel that, pursuant to the agreement of the parties in open court on February 16, 1968, both sides will rely exclusively on the record before the trial court in the original case of the State of Wyoming v. Harold Whiteley . . . and any and all parts of the record on appeal to the State of Wyoming ... in the hearing on the merits of this case before the [U. S. District Court].”</blockquote>
</footnote>
<footnote label="5">
<p id="b648-8"> A second version of state item 881 is identical in all relevant respects except that it omits reference to the arrest warrant. See App. 37.</p>
</footnote>
<footnote label="6">
<p id="b648-9"> In <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), the Court held that the same probable-cause standards were applicable to federal and state warrants under the Fourth and Fourteenth Amendments. In <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the Court held the exclusionary rule was applicable to state prosecutions.</p>
</footnote>
<footnote label="7">
<p id="b649-6"> See n. 4, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b649-7"> The dissent seems to imply that “this record shows” that Sheriff Ogburn received the description of the car contained in the radio bulletin from someone who also informed him that he also saw the car at the scene of the crime. <em>Post, </em>at 570. The record wholly fails to support any such implication. Sheriff Ogburn, who testified on four separate occasions at the trial, see R. 105-112, 187-191, 310-314, 335-337, said nothing of the sort. Only one other witness, Leonard Russell Marion, testified to having given Ogburn any information about the car prior to Whiteley’s arrest; Marion never testified to seeing the car near the scene of the crime. R. 317-322, 329-330. Indeed, it is quite apparent from reading Marion’s testimony that his observations of Whiteley on the day of the robbery took place at his own house. R. 320-321.</p>
<p id="b649-8">More importantly, even the dissent apparently concedes that as far as the record in this case reveals, the only information Sheriff Ogburn communicated to the magistrate issuing the warrant was contained in his written complaint reproduced above. Under the cases of this Court, an otherwise insufficient affidavit cannot be rehabilitated by testimony concerning information possessed by the affiant when he sought the warrant but not disclosed to the issuing magistrate. See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, 109 n. 1. A contrary rule would, of course, render the warrant requirements of the Fourth Amendment meaningless.</p>
</footnote>
<footnote label="9">
<p id="b649-9"> Since this is a federal habeas corpus proceeding, the State is technically not a party.</p>
</footnote>
<footnote label="10">
<p id="b650-6"> “The legal principles relied upon by the state throughout this entire litigated process have been based on the premise that a law enforcement officer may make a warrantless arrest if he has requisite probable cause, which can be something less than the requisite probable cause that must be presented to a judicial officer prior to the issuance of an arrest or search warrant.” Brief for Respondent 6.</p>
</footnote>
<footnote label="11">
<p id="b651-6"> After arresting Whiteley and Daley, the officers searched the car and discovered in the car’s interior the old coins taken in one of the burglaries and described in the radio bulletin. In addition, they found burglar’s tools in the trunk of the car. Of course, the discoveries of an illegal search cannot be used to validate the probable-cause judgment upon which the legality of the search depends.</p>
</footnote>
<footnote label="12">
<p id="b652-7"> The arrest warrant issued at about noon on November 24, 1964. See App. 53. State bulletin 881 was broadcast at 3:03 p. m. that same day. App. 31. It is apparent that Sheriff Ogbum did not himself acquire additional corroborative data possibly supporting a probable-cause arrest after securing the warrant.</p>
</footnote>
<footnote label="13">
<p id="b653-9"> The State makes a halfhearted attempt to argue that the introduction of the illegally seized evidence was harmless error. The <page-number citation-index="1" label="570">*570</page-number>evidence, of course, was damning, to say the least. See n. 10, <em>supra. </em>The only other evidence implicating Whiteley was his accomplice’s testimony. It is clear that the error cannot be said to be harmless under applicable standards. <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967); <em>Harrington </em>v. <em>California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969).</p>
<p id="b654-8">Contrary to the implications in the dissenting opinion, see <em>post, </em>at 571, no witness at trial other than the accomplice placed Whiteley “near the scene of the crime” on the night of the robbery.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Whren v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Whren v. United States"
type: case
citation: "517 U.S. 806 (1996)"
parallel_cite: "116 S. Ct. 1769; 135 L. Ed. 2d 89"
neutral_cite: 1996 U.S. LEXIS 3720
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-05-15
docket: 95-5841
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Whren v. United States
  varies_by_point: false
  scope_note: "Pretext-irrelevance rule reaffirmed throughout; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118036/whren-v-united-states/"
  cluster_id: 118036
  opinion_id: 118036
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
related: ["[[Delaware v. Prouse]]", "[[Pennsylvania v. Mimms]]", "[[Heien v. North Carolina]]"]
aliases: ["Whren"]
tags: ["case", "fourth-amendment", "traffic-stops", "pretext", "probable-cause", "subjective-intent"]
holding: "An officer's subjective motive is irrelevant to the Fourth Amendment validity of a traffic stop; a stop supported by an objective,…"
lake:
  record_id: Whren v. United States
  status: verified
  projected_at: 2026-07-09
---

# Whren v. United States

*517 U.S. 806 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Plainclothes vice officers patrolling a "high drug area" of Washington, D.C. in an unmarked car grew suspicious of a Pathfinder with youthful occupants stopped unusually long at a stop sign, the driver looking into the passenger's lap. When the police made a U-turn, the truck turned right without signaling and sped off at an unreasonable speed. The officers stopped it; approaching the window, Officer Soto saw bags of crack cocaine in Whren's hands. The occupants, charged with drug offenses, argued the traffic stop was a pretext to investigate a drug hunch for which the officers lacked probable cause.

## Issue
Whether a traffic stop supported by probable cause of a traffic violation violates the Fourth Amendment when the officer's actual motivation was to investigate other suspected crime, or whether the test should be whether a reasonable officer would have made the stop for the stated traffic reason.

## Rule
A stop is reasonable when there is probable cause of a traffic violation: "As a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred." — 517 U.S. at 810. ^pin-810

The officer's real motive does not matter: "Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis." — [*Id.* at 813](https://www.courtlistener.com/opinion/118036/whren-v-united-states/#:~:text=Subjective%20intentions%20play%20no%20role). ^pin-813

Claims of racially selective enforcement are governed by the Equal Protection Clause, not the Fourth Amendment.

## Application
On these facts the petitioners conceded that Officer Soto had probable cause to believe several D.C. traffic provisions had been violated — driving without full attention, turning without signaling, and traveling at an unreasonable speed. Because that probable cause existed, the stop was reasonable, and it made no difference that the officers' true interest was possible drug activity or that a reasonable officer arguably would not have made the stop for the traffic violations alone. The crack cocaine the officer then saw in plain view was lawfully observed.

## Conclusion
The traffic stop was constitutional because it was supported by probable cause of a traffic violation; the officers' subjective intent was irrelevant. The convictions were affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Whren* anchors the rule that traffic stops are judged objectively, building on [[Delaware v. Prouse]] and [[Pennsylvania v. Mimms]]; the objective-reasonableness approach extends to an officer's reasonable mistake of law in [[Heien v. North Carolina]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*

## Sources
- *Whren v. United States*, 517 U.S. 806 (1996) — https://www.courtlistener.com/opinion/118036/whren-v-united-states/ — pinpoints: 810, 813.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "66efca83e0f99b3c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "517 U.S. 806 (1996)", "court": "U.S. Supreme Court", "neutral_cite": "1996 U.S. LEXIS 3720", "official_citation_present": true, "parallel_cite": "116 S. Ct. 1769; 135 L. Ed. 2d 89", "title": "Whren v. United States", "year": "1996"}}
{"assertion_id": "ca0eac70e3dae6fb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An officer's subjective motive is irrelevant to the Fourth Amendment validity of a traffic stop; a stop supported by an objective,…", "title": "Whren v. United States"}}
{"assertion_id": "d0538cf598631c04", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Anchor", "title": "Whren v. United States"}}
{"assertion_id": "004a26db2bf02012", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Whren v. United States"}}
{"assertion_id": "3e10a2be6cd0f01d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1996-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Whren v. United States", "field_i_validity": "good_law", "scope_note": "Pretext-irrelevance rule reaffirmed throughout; good law.", "title": "Whren v. United States", "varies_by_point": "false"}}
```

### lake record — Whren v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Whren v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Whren v. United States",
    "case_name_short": "Whren",
    "case_name_full": "WHREN Et Al. v. UNITED STATES",
    "input_case_name": "Whren v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-05-15",
    "year": 1996,
    "docket": "95-5841",
    "cluster_id": 118036,
    "lead_opinion_id": 118036,
    "sibling_ids": [
      118036
    ],
    "absolute_url": "/opinion/118036/whren-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 U.S. 806",
      "volume": "517",
      "reporter": "U.S.",
      "page": "806",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 1769",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 89",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "89",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 3720",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3720",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 U.S. 806",
        "volume": "517",
        "reporter": "U.S.",
        "page": "806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 1769",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 89",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "89",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 3720",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3720",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 U.S. 806",
    "official_selection": {
      "court_class": "scotus",
      "selected": "517 U.S. 806",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-810",
      "page": null,
      "quote": "of Washington, D.C. in an unmarked car grew suspicious of a Pathfinder with youthful occupants stopped unusually long at a stop sign, the driver looking into the passenger's lap. When the police made a U-turn, the truck turned right without signaling and sped off at an unreasonable speed. The officers stopped it; approaching the window, Officer Soto saw bags of crack cocaine in Whren's hands. The occupants, charged with drug offenses, argued the traffic stop was a pretext to investigate a drug hunch for which the officers lacked probable cause. ## Issue Whether a traffic stop supported by probable cause of a traffic violation violates the Fourth Amendment when the officer's actual motivation was to investigate other suspected crime, or whether the test should be whether a reasonable officer would have made the stop for the stated traffic reason. ## Rule A stop is reasonable when there is probable cause of a traffic violation:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-813",
      "page": null,
      "quote": "Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.",
      "star_marker": "813",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15842,
      "fragment": "#:~:text=Subjective%20intentions%20play%20no%20role",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Whren v. United States",
    "varies_by_point": false,
    "scope_note": "Pretext-irrelevance rule reaffirmed throughout; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Robinson-Van Rader",
          "cluster_id": 9398953,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane1_negative"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Bryant",
          "cluster_id": 2959736,
          "cite": [
            "179 L. Ed. 2d 93",
            "131 S. Ct. 1143",
            "562 U.S. 344",
            "2011 U.S. LEXIS 1713"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peso Chavez and Gregory Lee, Individually and on Behalf of All Persons Similarly Situated v. The Illinois State Police, Terrance W. Gainer, Individually and in His Official Capacity as Director of the Illinois State Police, Michael Snyders, Individually and in His Official Capacity as Illinois State Police Operation Valkyrie Coordinator, Edward Kresl, Individually and in His Official Capacity as District Commander of the Illinois State Police, and Larry Thomas, Daniel Gillette, Craig Graham, Robert P. Cessna, Robert Lauterbach, and Dale Fraher, Officers of the Illinois State Police, in Their Individual Capacities",
          "cluster_id": 773427,
          "cite": [
            "251 F.3d 612",
            "49 Fed. R. Serv. 3d 1127",
            "2001 U.S. App. LEXIS 10560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Clark",
          "cluster_id": 6457347,
          "cite": [
            "596 U.S. 36",
            "142 S. Ct. 1332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118036) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjY0ODQxNjAwMDAwJnM9ODI0NjUzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118036%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118036)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NzEmcz00NTAyMzA2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118036%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118036)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkyNzQ4ODAwMDAwJnM9OTQyMjc4MyZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118036%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118036)",
    "indexed_citing_opinions": 3965,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118036,
        "count": 3965,
        "count_source": "search"
      }
    ],
    "citation_count": 7126,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/whren-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MjQ3Njkmcz0xMDYyMTk5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118036%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118036,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 695142,
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
    "date_created": "2026-07-06T04:22:20Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:24:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Whren v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b906-4">
<span citation-index="1" class="star-pagination" label="808"> 
   *808
   </span>
  Justice Scalia
 </author>
<p id="A6N">
  delivered the opinion of the Court.
 </p>
<p id="b906-5">
  In this case we decide whether the temporary detention of a motorist who the police have probable cause to believe has committed a civil traffic violation is inconsistent with the Fourth Amendment’s prohibition against unreasonable seizures unless a reasonable officer would have been motivated to stop the car by a desire to enforce the traffic laws.
 </p>
<p id="b906-6">
  I
 </p>
<p id="b906-7">
  On the evening of June 10, 1993, plainclothes vice-squad officers of the District of Columbia Metropolitan Police Department were patrolling a “high drug area” of the city in an unmarked car. Their suspicions were aroused when they passed a dark Pathfinder truck with temporary license plates and youthful occupants waiting at a stop sign, the driver looking down into the lap of the passenger at his right. The truck remained stopped at the intersection for what seemed an unusually long time — more than 20 seconds. When the police car executed a U-turn in order to head back toward the truck, the Pathfinder turned suddenly to its right, without signaling, and sped off at an “unreasonable” speed. The policemen followed, and in a short while overtook the Pathfinder when it stopped behind other traffic at a red light. They pulled up alongside, and Officer Ephraim Soto stepped out and approached the driver’s door, identifying himself as a police officer and directing the driver, petitioner Brown, to put the vehicle in park. When Soto drew up to the driver’s
  <span citation-index="1" class="star-pagination" label="809"> 
   *809
   </span>
  window, he immediately observed two large plastic bags of what appeared to be crack cocaine in petitioner Whren’s hands. Petitioners were arrested, and quantities of several types of illegal drugs were retrieved from the vehicle.
 </p>
<p id="b907-4">
  Petitioners were charged in a four-count indictment with violating various federal drug laws, including <span class="citation no-link">21 U. S. C. §§ 844</span>(a) and 860(a). At a pretrial suppression hearing, they challenged the legality of the stop and the resulting seizure of the drugs. They argued that the stop had not been justified by probable cause to believe, or even reasonable suspicion, that petitioners were engaged in illegal drug-dealing activity; and that Officer Soto’s asserted ground for approaching the vehicle—to give the driver a warning concerning traffic violations—was pretextual. The District Court denied the suppression motion, concluding that “the facts of the stop were not controverted,” and “[t]here was nothing to really demonstrate that the actions of the officers were contrary to a normal traffic stop.” App. 5.
 </p>
<p id="b907-5">
  Petitioners were convicted of the counts at issue here. The Court of Appeals affirmed the convictions, holding with respect to the suppression issue that, “regardless of whether a police officer subjectively believes that the occupants of an automobile may be engaging in some other illegal behavior, a traffic stop is permissible as long as a reasonable officer in the same circumstances
  <em>
   could have
  </em>
  stopped the car for the suspected traffic violation.” <span class="citation" data-id="695142"><a href="/opinion/695142/united-states-v-michael-a-whren/#374" aria-description="Citation for case: United States v. Michael A. Whren">53 F. 3d 371, 374-375</a></span> (CADC 1995). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./516/1036/">516 U. S. 1036</a></span> (1996).
 </p>
<p id="b907-6">
  II
 </p>
<p id="b907-7">
  The Fourth Amendment guarantees “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” Temporary detention of individuals during the stop of an automobile by the police, even if only for a brief period and for a limited purpose, constitutes a “seizure” of “persons” within the
  <span citation-index="1" class="star-pagination" label="810"> 
   *810
   </span>
  meaning of this provision. See
  <em>
   Delaware
  </em>
  v.
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653</a></span> (1979);
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556</a></span> (1976);
  <em>
   United States
  </em>
  v.
  <em>
   Brignoni-Ponce,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). An automobile stop is thus subject to the constitutional imperative that it not be “unreasonable” under the circumstances. As a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred. See
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 659</a></span>;
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span> (1977)
  <em>
   (per curiam).
  </em>
</p>
<p id="b908-5">
  Petitioners accept that Officer Soto had probable cause to believe that various provisions of the District of Columbia traffic code had been violated. See 18 D. C. Mun. Regs. §§2213.4 (1995) (“An operator shall . . . give full time and attention to the operation of the vehicle”); 2204.3 (“No person shall turn any vehicle ... without giving an appropriate signal”); 2200.3 (“No person shall drive a vehicle ... at a speed greater than is reasonable and prudent under the conditions”). They argue, however, that “in the unique context of civil traffic regulations” probable cause is not enough. Since, they contend, the use of automobiles is so heavily and minutely regulated that total compliance with traffic and safety rules is nearly impossible, a police officer will almost invariably be able to catch any given motorist in a technical violation. This creates the temptation to use traffic stops as a means of investigating other law violations, as to which no probable cause or even articulable suspicion exists. Petitioners, who are both black, further contend that police officers might decide which motorists to stop based on decidedly impermissible factors, such as the race of the car’s occupants. To avoid this danger, they say, the Fourth Amendment test for traffic stops should be, not the normal one (applied by the Court of Appeals) of whether probable cause existed to justify the stop; but rather, whether a police officer, acting reasonably, would have made the stop for the reason given.
 </p>
<p id="b909-4">
<span citation-index="1" class="star-pagination" label="811"> 
   *811
   </span>
  A
 </p>
<p id="b909-5">
  Petitioners contend that the standard they propose is consistent with our past cases’ disapproval of police attempts to use valid bases of action against citizens as pretexts for pursuing other investigatory agendas. We are reminded that in
  <em>
   Florida
  </em>
  v.
  <em>
   Wells,
  </em>
  <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4</a></span> (1990), we stated that “an inventory search
  <a class="footnote" href="#fn[1]" id="fn[1]_ref">
   [1]
  </a>
  must not be a ruse for a general rummaging in order to discover incriminating evidence”; that in
  <em>
   Colorado
  </em>
  v.
  <em>
   Bertine,
  </em>
  <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#372" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 372</a></span> (1987), in approving an inventory search, we apparently thought it significant that there had been “no showing that the police, who were following standardized procedures, acted in bad faith or for the sole purpose of investigation”; and that in
  <em>
   New York
  </em>
  v.
  <em>
   Burger,
  </em>
  <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#716" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 716-717, n. 27</a></span> (1987), we observed, in upholding the constitutionality of a warrantless administrative inspection,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  that the search did not appear to be “a 'pretext’ for obtaining evidence of . . . violation of . . . penal laws.” But only an undiscerning reader would regard these cases as endorsing the principle that ulterior motives can invalidate police conduct that is justifiable on the basis of probable cause to believe that a violation of law has occurred. In each case we were addressing the validity of a search conducted in the
  <em>
   absence
  </em>
  of probable cause. Our quoted statements simply explain that the exemption from the need for probable cause (and warrant), which is accorded to searches made for the purpose of inventory or administrative
  <span citation-index="1" class="star-pagination" label="812"> 
   *812
   </span>
  regulation, is not accorded to searches that are
  <em>
   not
  </em>
  made for those purposes. See
  <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine"><em>
   Bertine, supra,
  </em>
  at 371-372</a></span>;
  <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#702" aria-description="Citation for case: New York v. Burger"><em>
   Burger, supra,
  </em>
  at 702-703</a></span>.
 </p>
<p id="b910-5">
  Petitioners also rely upon
  <em>
   Colorado
  </em>
  v.
  <em>
   Bannister,
  </em>
  <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1</a></span> (1980)
  <em>
   (per curiam),
  </em>
  a case which, like this one, involved a traffic stop as the prelude to a plain-view sighting and arrest on charges wholly unrelated to the basis for the stop. Petitioners point to our statement that “[tjhere was no evidence whatsoever that the officer’s presence to issue a traffic citation was a pretext to confirm any other previous suspicion about the occupants” of the car.
  <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>
   Id.,
  </em>
  at 4, n. 4</a></span>. That dictum
  <em>
   at most
  </em>
  demonstrates that the Court in
  <em>
   <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">Bannister</a></span>
  </em>
  found no need to inquire into the question now under discussion; not that it was certain of the answer. And it may demonstrate even less than that: If by “pretext” the Court meant that the officer really had not seen the car speeding, the statement would mean only that there was no reason to doubt probable cause for the traffic stop.
 </p>
<p id="b910-6">
  It would, moreover, be anomalous, to say the least, to treat a statement in a footnote in the
  <em>
   per curiam Bannister
  </em>
  opinion as indicating a reversal of our prior law. Petitioners’ difficulty is not simply a lack of affirmative support for their position. Not only have we never held, outside the context of inventory search or administrative inspection (discussed above), that an officer’s motive invalidates objectively justifiable behavior under the Fourth Amendment; but we have repeatedly held and asserted the contrary. In
  <em>
   United States
  </em>
  v.
  <em>
   Villamonte-Marquez,
  </em>
  <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#584" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 584, n. 3</a></span> (1983), we held that an otherwise valid warrantless boarding of a vessel by customs officials was not rendered invalid “because the customs officers were accompanied by a Louisiana state policeman, and were following an informant’s tip that a vessel in the ship channel was thought to be carrying marihuana.” We flatly dismissed the idea that an ulterior motive might serve to strip the agents of their legal justification. In
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), we held that
  <span citation-index="1" class="star-pagination" label="813"> 
   *813
   </span>
  a traffic-violation arrest (of the sort here) would not be rendered invalid by the fact that it was “a mere pretext for a narcotics search,”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#221" aria-description="Citation for case: United States v. Robinson"><em>
   id.,
  </em>
  at 221, n. 1</a></span>; and that a lawful post-arrest search of the person would not be rendered invalid by the fact that it was not motivated by the officer-safety concern that justifies such searches, see
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#236" aria-description="Citation for case: United States v. Robinson"><em>
   id.,
  </em>
  at 236</a></span>. See also
  <em>
   Gustafson
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266</a></span> (1973). And in
  <em>
   Scott
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 138</a></span> (1978), in rejecting the contention that wiretap evidence was subject to exclusion because the agents conducting the tap had failed to make any effort to comply with the statutory requirement that unauthorized acquisitions be minimized, we said that “[sjubjective intent alone ... does not make otherwise lawful conduct illegal or unconstitutional.” We described
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>
  </em>
  as having established that “the fact that the officer does not have the state of mind which is hypothecated by the reasons which provide the legal justification for the officer’s action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action.” <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U. S., at 136, 138</a></span>.
 </p>
<p id="b911-5">
  We think these cases foreclose any argument that the constitutional reasonableness of traffic stops depends on the actual motivations of the individual officers involved. We of course agree with petitioners that the Constitution prohibits selective enforcement of the law based on considerations such as race. But the constitutional basis for objecting to intentionally discriminatory application of laws is the Equal Protection Clause, not the Fourth Amendment. Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.
 </p>
<p id="b911-6">
  B
 </p>
<p id="b911-7">
  Recognizing that we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers, petitioners disavow any intention to make the individual officer’s subjective good faith the touchstone of “reasonableness.” They insist that the stand
  <span citation-index="1" class="star-pagination" label="814"> 
   *814
   </span>
  ard they have put forward — whether the officer’s conduct deviated materially from usual police practices, so that a reasonable officer in the same circumstances would not have made the stop for the reasons given — is an “objective” one.
 </p>
<p id="b912-4">
  But although framed in empirical terms, this approach is plainly and indisputably driven by subjective considerations. Its whole purpose is to prevent the police from doing under the guise of enforcing the traffic code what they would like to do for different reasons. Petitioners’ proposed standard may not use the word-“pretext,” but it is designed to combat nothing other than the perceived “danger” of the pretextual stop, albeit only indirectly and over the run of cases. Instead of asking whether the individual officer had the proper state of mind, the petitioners would have us ask, in effect, whether (based on general police practices) it is plausible to believe that the officer had the proper state of mind.
 </p>
<p id="b912-5">
  Why one would frame a test designed to combat pretext in such fashion that the court cannot take into account
  <em>
   actual and admitted pretext
  </em>
  is a curiosity that can only be explained by the fact that our cases have foreclosed the more sensible option. If those cases were based only upon the evidentiary difficulty of establishing subjective intent, petitioners’ attempt to root out subjective vices through objective means might make sense. But they were not based only upon that, or indeed even principally upon that. Their principal basis — which applies equally to attempts to reach subjective intent through ostensibly objective means — is simply that the Fourth Amendment’s concern with “reasonableness” allows certain actions to be taken in certain circumstances,
  <em>
   whatever
  </em>
  the subjective intent. See,
  <em>
   e. g., Robinson, supra,
  </em>
  at 236 (“Since it is the fact of custodial arrest which gives rise to the authority to search, it is of no moment that [the officer] did not indicate any subjective fear of the [arrestee] or that he did not himself suspect that [the arrestee] was armed”) (footnotes omitted);
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida"><em>
   Gustafson, supra,
  </em>
  at 266</a></span> (same). But even if our concern had been only an evidentiary one,
  <span citation-index="1" class="star-pagination" label="815"> 
   *815
   </span>
  petitioners’ proposal would by no means assuage it. Indeed, it seems to us somewhat easier to figure out the intent of an individual officer than to plumb the collective consciousness of law enforcement in order to determine whether a “reasonable officer” would have been moved to act upon the traffic violation. While police manuals and standard procedures may sometimes provide objective assistance, ordinarily one would be reduced to speculating about the hypothetical reaction of a hypothetical constable — an exercise that might be called virtual subjectivity.
 </p>
<p id="b913-5">
  Moreover, police enforcement practices, even if they could be practicably assessed by a judge, vary from place to place and from time to time. We cannot accept that the search and seizure protections of the Fourth Amendment are so variable, cf.
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#265" aria-description="Citation for case: Gustafson v. Florida"><em>
   Gustafson, supra,
  </em>
  at 265</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Caceres,
  </em>
  <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#755" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 755-756</a></span> (1979), and can be made to turn upon such trivialities. The difficulty is illustrated by petitioners’ arguments in this case. Their claim that a reasonable officer would not have made this stop is based largely on District of Columbia police regulations which permit plainclothes officers in unmarked vehicles to enforce traffic laws “only in the case of a violation that is so grave as to pose an
  <em>
   immediate threat
  </em>
  to the safety of others.” Metropolitan Police Department, Washington, D. C., General Order 303.1, pt. 1, Objectives and Policies (A)(2)(4) (Apr. 30, 1992), reprinted as Addendum to Brief for Petitioners. This basis of invalidation would not apply in jurisdictions that had a different practice. And it would not have applied even in the District of Columbia, if Officer Soto had been wearing a uniform or patrolling in a marked police cruiser.
 </p>
<p id="b913-6">
  Petitioners argue that our cases support insistence upon police adherence to standard practices as an objective means of rooting out pretext. They cite no holding to that effect, and dicta in only two cases. In
  <em>
   Abel
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), the petitioner had been arrested by the Immigration and Naturalization Service (INS), on the basis of
  <span citation-index="1" class="star-pagination" label="816"> 
   *816
   </span>
  an administrative warrant that, he claimed, had been issued on pretextual grounds in order to enable the Federal Bureau of Investigation (FBI) to search his room after his arrest. We regarded this as an allegation of “serious misconduct,” but rejected Abel’s claims on the ground that “[a] finding of bad faith is ... not open to us on th[e] record” in light of the findings below, including the finding that “ ‘the proceedings taken by the [INS] differed in no respect from what would have been done in the case of an individual concerning whom [there was no pending FBI investigation],’”
  <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#226" aria-description="Citation for case: Abel v. United States"><em>
   id.,
  </em>
  at 226-227</a></span>. But it is a long leap from the proposition that following regular procedures is some evidence of lack of pretext to the proposition that failure to follow regular procedures
  <em>
   proves
  </em>
  (or is an operational substitute for) pretext.
  <em>
   <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">Abel</a></span>,
  </em>
  moreover, did not involve the assertion that pretext could invalidate a search or seizure for which there was probable cause — and even what it said about pretext in other contexts is plainly inconsistent with the views we later stated in
  <em>
   Robinson, Gustafson, Scott,
  </em>
  and
  <em>
   <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Villamonte-Marquez</a></span>.
  </em>
  In the other case claimed to contain supportive dicta,
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), in approving a search incident to an arrest for driving without a license, we noted that the arrest was “not a departure from established police department practice.”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#221" aria-description="Citation for case: United States v. Robinson"><em>
   Id.,
  </em>
  at 221, n. 1</a></span>. That was followed, however, by the statement that “[w]e leave for another day questions which would arise on facts different from these.”
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Ibid.</a></span>
  </em>
  This is not even a dictum that purports to provide an answer, but merely one that leaves the question open.
 </p>
<p id="AdW">
<em>
   f
  </em>
  — i hH t — 4
 </p>
<p id="AE3">
  In what would appear to be an elaboration on the "reasonable officer” test, petitioners argue that the balancing inherent in any Fourth Amendment inquiry requires us to weigh the governmental and individual interests implicated in a traffic stop such as we have here. That balancing, petitioners claim, does not support investigation of minor traffic in
  <span citation-index="1" class="star-pagination" label="817"> 
   *817
   </span>
  fractions by plainclothes police in unmarked vehicles; such investigation only minimally advances the government’s interest in traffic safety, and may indeed retard it by producing motorist confusion and alarm — a view said to be supported by the Metropolitan Police Department’s own regulations generally prohibiting this practice. And as for the Fourth Amendment interests of the individuals concerned, petitioners point out that our cases acknowledge that even ordinary traffic stops entail “a possibly unsettling show of authority”; that they at best "interfere with freedom of movement, are inconvenient, and consume time” and at worst “may create substantial anxiety,”
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#657" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 657</a></span>. That anxiety is likely to be even more pronounced when the stop is conducted by plainclothes officers in unmarked cars.
 </p>
<p id="b915-5">
  It is of course true that in principle every Fourth Amendment case, since it turns upon a “reasonableness” determination, involves a balancing of all relevant factors. With rare exceptions not applicable here, however, the result of that balancing is not in doubt where the search or seizure is based upon probable cause. That is why petitioners must rely upon cases like
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  to provide examples of actual “balancing” analysis. There, the police action in question was a random traffic stop for the purpose of checking a motorist’s license and vehicle registration, a practice that — like the practices at issue in the inventory search and administrative inspection cases upon which petitioners rely in making their “pretext” claim — involves police intrusion
  <em>
   without the probable cause that is its traditional justification.
  </em>
  Our opinion in
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  expressly distinguished the case from a stop based on precisely what is at issue here: “probable cause to believe that a driver is violating any one of the multitude of applicable traffic and equipment regulations.”
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><em>
   Id.,
  </em>
  at 661</a></span>. It noted approvingly that “[t]he foremost method of enforcing traffic and vehicle safety regulations ... is acting upon observed violations,”
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>
   id.,
  </em>
  at 659</a></span>, which afford the “‘quantum of individualized suspicion’ ” necessary to ensure that police
  <span citation-index="1" class="star-pagination" label="818"> 
   *818
   </span>
  discretion is sufficiently constrained,
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">id.,</a></span>
  </em>
  at 654-655 (quoting
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span>). What is true of
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  is also true of other cases that engaged in detailed “balancing” to decide the constitutionality of automobile stops, such as
  <em>
   <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,
  </em>
  which upheld checkpoint stops, see <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-562</a></span>, and
  <em>
   <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,
  </em>
  which disallowed so-called “roving patrol” stops, see <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 882</a></span>-884: The detailed “balancing” analysis was necessary because they involved seizures without probable cause.
 </p>
<p id="b916-5">
  Where probable cause has existed, the only cases in which we have found it necessary actually to perform the “balancing” analysis involved searches or seizures conducted in an extraordinary manner, unusually harmful to an individual’s privacy or even physical interests — such as, for example, seizure by means of deadly force, see
  <em>
   Tennessee
  </em>
  v.
  <em>
   Garner,
  </em>
  <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), unannounced entry into a home, see
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), entry into a home without a warrant, see
  <em>
   Welsh
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984), or physical penetration of the body, see
  <em>
   Winston
  </em>
  v.
  <em>
   Lee,
  </em>
  <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985). The making of a traffic stop out of uniform does not remotely qualify as such an extreme practice, and so is governed by the usual rule that probable cause to believe the law has been broken “outbalances” private interest in avoiding police contact.
 </p>
<p id="b916-6">
  Petitioners urge as an extraordinary factor in this case that the “multitude of applicable traffic and equipment regulations” is so large and so difficult to obey perfectly that virtually everyone is guilty of violation, permitting the police to single out almost whomever they wish for a stop. But we are aware of no principle that would allow us to decide at what point a code of law becomes so expansive and so commonly violated that infraction itself can no longer be the ordinary measure of the lawfulness of enforcement. And even if we could identify such exorbitant codes, we do not know by what standard (or what right) we would decide, as
  <span citation-index="1" class="star-pagination" label="819"> 
   *819
   </span>
  petitioners would have us do, which particular provisions are sufficiently important to merit enforcement.
 </p>
<p id="b917-5">
  For the run-of-the-mine case, which this surely is, we think there is no realistic alternative to the traditional common-law rule that probable cause justifies a search and seizure.
 </p>
<p id="b917-6">
  * * *
 </p>
<p id="b917-7">
  Here the District Court found that the officers had probable cause to believe that petitioners had violated the traffic code. That rendered the stop reasonable under the Fourth Amendment, the evidence thereby discovered admissible, and the upholding of the convictions by the Court of Appeals for the District of Columbia Circuit correct. The judgment is
 </p>
<p id="b917-8">
<em>
   Affirmed.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn[1]" label="[1]">
<a class="footnote" href="#fn[1]_ref">
   [1]
  </a>
<p id="b909-6">
   1 An inventory search is the search of property lawfully seized and detained, in order to ensure that it is harmless, to secure valuable items (such as might be kept in a towed car), and to protect against false claims of loss or damage. See
   <em>
    South Dakota
   </em>
   v.
   <em>
    Opperman,
   </em>
   <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#369" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 369</a></span> (1976).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b909-7">
   An administrative inspection is the inspection of business premises conducted by authorities responsible for enforcing a pervasive regulatory scheme — for example, unannounced inspection of a mine for compliance with health and safety standards. See
   <em>
    Donovan
   </em>
   v.
   <em>
    Dewey,
   </em>
   <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#599" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 599-605</a></span> (1981).
  </p>
</div></div></opinion>
```

---
