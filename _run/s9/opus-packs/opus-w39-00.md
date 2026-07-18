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

## GROUP: content/cases/Moore v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: Moore v. Illinois
type: case
citation: "434 U.S. 220 (1977)"
parallel_cite: "98 S. Ct. 458; 54 L. Ed. 2d 424"
neutral_cite: 1977 U.S. LEXIS 163
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-12-12
docket: No. 76-5344
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
  opinion_url: "https://www.courtlistener.com/opinion/109757/moore-v-illinois/"
  cluster_id: 109757
  opinion_id: null
  identity_checked: true
lake:
  record_id: Moore v. Illinois
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Lineups and the Right to Counsel]]"
    role: Anchor
related:
  - "[[Lineups and the Right to Counsel]]"
  - "[[United States v. Wade]]"
  - "[[Gilbert v. California]]"
  - "[[Kirby v. Illinois]]"
tags:
  - case
  - sixth-amendment
  - right-to-counsel
  - identification
  - critical-stage
  - preliminary-hearing
holding: "The Sixth Amendment right to counsel attaches to a corporeal identification conducted after the initiation of adversary judicial criminal proceedings, so admitting an in-court reference to an uncounseled identification made of the accused at a preliminary hearing — a critical stage — violated his right to counsel under Wade and Gilbert."
aliases:
  - Moore v. Illinois
  - "Moore v. Illinois (1977)"
---

# Moore v. Illinois

*434 U.S. 220 (1977)* (No. 76-5344) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109757 → combined opinion 109757 (Powell, J.; 434 U.S. 220, decided Dec. 12, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*231` precedes the quoted sentence). S9 promotes. -->

## Background
A rape victim identified the petitioner as her assailant at a preliminary hearing. He appeared before the judge without counsel; the victim was told in advance that the man being brought before the bench was the suspect, and she identified him in that one-on-one setting. At trial she testified to that preliminary-hearing identification. The petitioner argued that conducting the identification without counsel, after formal proceedings had begun, violated his Sixth Amendment right to counsel under *[[United States v. Wade]]* and *[[Gilbert v. California]]*.

## Issue
Whether the Sixth Amendment right to counsel applies to a corporeal identification conducted at a preliminary hearing held after the initiation of adversary judicial criminal proceedings.

## Rule
Applying the rule of *[[United States v. Wade|Wade]]*, *[[Gilbert v. California|Gilbert]]*, and *[[Kirby v. Illinois]]* — that the right to counsel attaches to identifications conducted at or after the initiation of adversary judicial proceedings — the Court held: "Here, as in those cases, petitioner's Sixth Amendment rights were violated by a corporeal identification conducted after the initiation of adversary judicial criminal proceedings and in the absence of counsel." — 434 U.S. at 231. ^pin-231

## Application
The preliminary hearing marked the initiation of adversary judicial proceedings: the State had committed to prosecute, and the petitioner faced its prosecutorial forces at a hearing where counsel could have moved to dismiss and to suppress. Under *[[Kirby v. Illinois|Kirby]]*, the *Wade–Gilbert* right had therefore attached, and the Court of Appeals erred in confining that right to post-indictment identifications. Counsel's presence might also have blunted the identification's extreme suggestiveness. The uncounseled corporeal identification thus violated the Sixth Amendment.

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]] (for the state courts to consider [[Inevitable Discovery and Independent Source|independent source]] and harmless error). Powell, J., delivered the opinion of the Court; Blackmun, J., concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Moore* applies the *[[United States v. Wade|Wade]]*–*[[Gilbert v. California|Gilbert]]*–*[[Kirby v. Illinois|Kirby]]* framework to a preliminary-hearing show-up: once adversary judicial proceedings begin, a corporeal identification is a **critical stage** requiring counsel. Teach it for the attachment line — the right runs from the initiation of formal proceedings (by formal charge, preliminary hearing, indictment, information, or arraignment), not from arrest alone.

## Appears on
- [[Lineups and the Right to Counsel]] — *Anchor*

## Sources
- [*Moore v. Illinois*, 434 U.S. 220 (1977)](https://www.courtlistener.com/opinion/109757/moore-v-illinois/) — pinpoint: 231 (Powell, J., for the Court; the CL opinion text carries the reporter star `*231` immediately before the quoted sentence). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "873d1f643ee3d6a7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "434 U.S. 220 (1977)", "court": "U.S. Supreme Court", "neutral_cite": "1977 U.S. LEXIS 163", "official_citation_present": true, "parallel_cite": "98 S. Ct. 458; 54 L. Ed. 2d 424", "title": "Moore v. Illinois", "year": "1977"}}
{"assertion_id": "121186784b801b49", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment right to counsel attaches to a corporeal identification conducted after the initiation of adversary judicial criminal proceedings, so admitting an in-court reference to an uncounseled identification made of the accused at a preliminary hearing — a critical stage — violated his right to counsel under Wade and Gilbert.", "title": "Moore v. Illinois"}}
{"assertion_id": "6e53670b6dd83648", "dimension": "support", "kind": "home_role", "locator": {"home": "Lineups and the Right to Counsel"}, "payload": {"home": "Lineups and the Right to Counsel", "role": "Anchor", "title": "Moore v. Illinois"}}
{"assertion_id": "336b49213c29813d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Moore v. Illinois"}}
{"assertion_id": "91cdbfe101d4671f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Moore v. Illinois", "varies_by_point": "false"}}
```

### lake record — Moore v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Moore v. Illinois",
  "status": "under_review",
  "identity": {
    "case_name": "Moore v. Illinois",
    "case_name_short": "Moore",
    "case_name_full": "Moore v. Illinois",
    "input_case_name": "Moore v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-12-12",
    "year": 1977,
    "docket": "No. 76-5344",
    "cluster_id": 109757,
    "lead_opinion_id": 9427017,
    "sibling_ids": [],
    "absolute_url": "/opinion/109757/moore-v-illinois/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "434 U.S. 220",
      "volume": "434",
      "reporter": "U.S.",
      "page": "220",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 458",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 424",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 163",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "163",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "434 U.S. 220",
        "volume": "434",
        "reporter": "U.S.",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 458",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "458",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 L. Ed. 2d 424",
        "volume": "54",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 163",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "163",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "434 U.S. 220",
    "official_selection": {
      "court_class": "scotus",
      "selected": "434 U.S. 220",
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
    "date_created": "2026-07-06T13:45:24Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "moore-v-illinois--109757",
      "to_record_id": "Moore v. Illinois",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Moore v. Illinois

```
<opinion type="majority">
<author id="b393-10">Mr. Justice Powell</author>
<p id="A-i">delivered the opinion of the Court.</p>
<p id="b393-11">Petitioner was convicted of rape and related offenses. At trial the complaining witness testified on direct examination by the prosecution that she had identified petitioner at a preliminary hearing at which he was not represented by counsel. The State Supreme Court affirmed petitioner's convictions, and the Federal District Court and Court of Appeals denied habeas corpus relief. We granted certiorari because of an apparent conflict between the decisions below and our holdings with respect to the right to counsel at corporeal identifications in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> <em>(1967); </em>and <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972). We reverse.</p>
<p id="b393-12">I</p>
<p id="b393-13">The victim of the offenses in question lived in an apartment on the South Side of Chicago. Shortly after noon on December 14, 1967, she awakened from a nap to find a man standing in the doorway to her bedroom holding a knife. The man entered the bedroom, threw her face down on the bed, and <page-number citation-index="1" label="222">*222</page-number>choked her until she was quiet. After covering his face with a bandana, the intruder partially undressed the victim, forced her to commit oral sodomy, and raped her. Then he left, taking a guitar and a flute from the apartment.</p>
<p id="b394-5">When police arrived, the victim gave them a description of her assailant. Although she did not know who he was and had seen his face for only 10 to 15 seconds during the attack, she thought he was the same man who had made offensive remarks to her in a neighborhood bar the night before. She also gave police a notebook she had found next to her bed after the attack.</p>
<p id="b394-6">In the week that followed, police showed the victim two groups of photographs of men. From the first group of 200 she picked about 30 who resembled her assailant in height, weight, and build. From the second group of about 10, she picked two or three. One of these was of petitioner. Police also found a letter in the notebook that the victim had given them. Investigation revealed that it was written by a woman with whom petitioner had been staying. The letter had been taken from the woman’s home in her absence, and petitioner appeared to be the only other person who had access to the home.</p>
<p id="b394-7">On the evening of December 20, 1967, police arrested petitioner at his apartment and held him overnight pending a preliminary hearing to determine whether he should be bound over to the grand jury and to set bail. The next morning, a policeman accompanied the victim to the Circuit Court of Cook County (First Municipal District) for the hearing. The policeman told her she was going to view a suspect and should identify him if she could. He also had her sign a complaint that named petitioner as her assailant. At the hearing, petitioner’s name was called and he was led before the bench. The judge told petitioner that he was charged with rape and deviate sexual behavior. The judge then called the victim, who had been in the courtroom waiting for the case to be called, to come before the bench. The State’s Attorney stated <page-number citation-index="1" label="223">*223</page-number>that police had found evidence linking petitioner with the offenses charged. He asked the victim whether she saw her assailant in the courtroom, and she pointed at petitioner. The State’s Attorney then requested a continuance of the hearing because more time was needed to check fingerprints. The judge granted the continuance and fixed bail. Petitioner was not represented by counsel at this hearing, and the court'did not offer to appoint counsel.</p>
<p id="b395-5">At a subsequent hearing, petitioner was bound over to the grand jury, which indicted him for rape, deviate sexual behavior, burglary, and robbery. Counsel was appointed, and he moved to suppress the victim’s identification of petitioner because it had been elicited at the preliminary hearing through an unnecessarily suggestive procedure at which petitioner was not represented by counsel.<footnotemark>1</footnotemark> After an evidentiary hearing the trial court denied the motion on the ground that the prosecution had shown an independent basis for the victim’s identification.</p>
<p id="b395-6">At trial, the victim testified on direct examination by the prosecution that she had identified petitioner as her assailant at the preliminary hearing. She also testified that the defendant on trial was the man who had raped her. The prosecution’s other evidence linking petitioner with the crimes was the letter found in the victim’s apartment. Defense counsel stipulated that petitioner had taken the letter from his woman friend’s home, but he presented evidence that petitioner might have lost the notebook containing the letter at the neighborhood bar the night before the attack. The defense theory was that the victim, who also was in the bar that night, could have picked up the notebook by mistake and taken it home. <page-number citation-index="1" label="224">*224</page-number>The defense also called witnesses who testified that petitioner was with them in a college lunchroom in another part of Chicago at the time the attack was committed.</p>
<p id="b396-5">The jury found petitioner guilty on all four counts, thus rejecting his theory and alibi. The trial court sentenced him to 30 to 50 years in prison. The Illinois Supreme Court affirmed. <em>People </em>v. <em>Moore, </em><span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/" aria-description="Citation for case: People v. Moore">51 Ill. 2d 79</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/" aria-description="Citation for case: People v. Moore">281 N. E. 2d 294</a></span> (1972). It rejected petitioner’s argument that the victim’s identification testimony should have been excluded, on the ground that the prosecution had shown an “independent basis” for the identification. <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#86" aria-description="Citation for case: People v. Moore"><em>Id., </em>at 86</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#298" aria-description="Citation for case: People v. Moore">281 N. E. 2d, at 298</a></span>. After this Court denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./409/979/">409 U. S. 979</a></span> (1972), petitioner sought a writ of habeas corpus from the Federal District Court. He contended that admission of the identification testimony at trial violated his Sixth and Fourteenth Amendment rights. Relying on the transcript from the state proceedings, the District Court denied the writ in an unpublished opinion, again on the ground that the prosecution had shown an independent basis for the identification. App. 31-35. The Court of Appeals for the Seventh Circuit affirmed in an unpublished opinion, <em>United States ex rel. Moore </em>v. <em>Illinois, </em><span class="citation" data-id="334955"><a href="/opinion/334955/u-s-ex-rel-moore-v-people-of-state-of-illinois/" aria-description="Citation for case: U. S. Ex Rel. Moore v. People of State of Illinois">534 F. 2d 331</a></span> (1976), and we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./429/1061/">429 U. S. 1061</a></span> (1977).</p>
<p id="b396-6">II</p>
<p id="b396-7"><em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), held that a pretrial corporeal identification conducted after a suspect has been indicted is a critical stage in a criminal prosecution at which the Sixth Amendment entitles the accused to the presence of counsel. The Court emphasized the dangers inherent in a pretrial identification conducted in the absence of counsel. Persons who conduct the identification procedure may suggest, intentionally or unintentionally, that they expect the witness to identify the accused. Such a suggestion, coming Jrom a police officer or prosecutor, can lead a witness to make <page-number citation-index="1" label="225">*225</page-number>a mistaken identification. The witness then will be predisposed to adhere to this identification in subsequent testimony at trial. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#229" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 229, 235-236</a></span>. If an accused’s counsel is present at the pretrial identification, he can serve both his client’s and the prosecution’s interests by objecting to suggestive features of a procedure before they influence a witness’ identification. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#236" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 236, 238</a></span>. In view of the “variables and pitfalls” that exist at an uncounseled pretrial identification, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>id., </em>at 235</a></span>, the <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>Court reasoned:</p>
<blockquote id="b397-5">“[T]he first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused’s fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused, the witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness — ‘that’s the man.’ ” <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 235-236</a></span>.</blockquote>
<p id="b397-6"><em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and its companion case, <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), also considered the admissibility of evidence derived from a corporeal identification conducted in violation of the accused’s right to counsel. In <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>, </em>witnesses to a robbery who had identified the defendant at an uncounseled pretrial lineup testified at trial on direct examination by the prosecution that he was the man who had committed the robbery. The prosecution did not elicit from the witnesses the fact that they had identified the defendant at the pretrial lineup. Nevertheless, because of the likelihood that the witnesses’ in-court identifications were based on their observations of the defendant at the uncounseled lineup rather than at the scene of the crime, the Court held that this testimony should have been excluded unless the prosecution could “establish by clear and convincing evidence that the in-court identifications <page-number citation-index="1" label="226">*226</page-number>were based upon observations of the suspect other than the lineup identification.” 388 U. S., at 240.<footnotemark>2</footnotemark></p>
<p id="b398-5"><em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>differed from <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>in one critical respect. In <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>the prosecution did elicit testimony in its case-in-chief that witnesses had identified the accused at an uncounseled pretrial lineup. The Court recognized that such testimony would “enhance the impact of [a witness’] in-court identification on the jury and seriously aggravate whatever derogation exists of the accused’s right to a fair trial.” 388 U. S., at 273-274. Because “[t]hat testimony [was] the direct result of the illegal lineup 'come at by exploitation of [the primary] illegality [,]’ <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span>,” the prosecution was “not entitled to an opportunity to show that the testimony had an independent source.” <em>Id., </em>at 272-273; see also <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span> </em>at 240 n. 32. The Court announced this exclusionary rule in the belief that such a sanction is necessary “to assure that law enforcement authorities will respect the accused’s constitutional right to the presence of his counsel at the critical lineup.” <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><em>Gilbert, supra, </em>at 273</a></span>. The Court therefore reversed the conviction and remanded to the state court for a determination of whether admission of this evidence was harmless constitutional error under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#274" aria-description="Citation for case: Gilbert v. California">388 U. S., at 274</a></span>.</p>
<p id="b398-6">In <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), the plurality opinion made clear that the right to counsel announced in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>attaches only to corporeal identifications Conducted “at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.” <page-number citation-index="1" label="227">*227</page-number><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. This is so because the initiation of such proceedings “marks the commencement of the 'criminal prosecutions’ to which alone the explicit guarantees of the Sixth Amendment are applicable.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#690" aria-description="Citation for case: Kirby v. Illinois"><em>Id., </em>at 690</a></span>. Thus, in <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>the plurality held that the prosecution’s evidence of a robbery victim’s one-on-one stationhouse identification of an uncoun-seled suspect shortly after the suspect’s arrest was admissible because adversary judicial criminal proceedings had not yet been initiated. In such cases, however, due process protects the accused against the introduction of evidence of, or tainted by, unreliable pretrial identifications obtained through unnecessarily suggestive procedures. <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#690" aria-description="Citation for case: Kirby v. Illinois"><em>Id., </em>at 690-691</a></span>; <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972); <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967); see generally <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977).<footnotemark>3</footnotemark></p>
<p id="b399-5">III</p>
<p id="b399-6">In the instant case, petitioner argues that the preliminary hearing at which the victim identified him marked the initiation of adversary judicial criminal proceedings against him. Hence, under <em>Wade, Gilbert, </em>and <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>, </em>he was entitled to the presence of counsel at that confrontation. Moreover, the <page-number citation-index="1" label="228">*228</page-number>prosecution introduced evidence of this uncounseled corporeal identification at trial in its case-in-chief. Petitioner contends that under <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>, </em>this evidence should have been excluded without regard to whether there was an “independent source” for it.</p>
<p id="b400-5">The Court of Appeals took a different view of the case. It read <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>as holding that evidence of a corporeal identification conducted in the absence of defense counsel must be excluded only if the identification is made after the defendant is <em>indicted. </em>App. 45-46. Such a reading cannot be squared with <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>itself, which held that an accused’s rights under <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>attach to identifications conducted “at or after the initiation of adversary judicial criminal proceedings,” including proceedings instituted “by way of formal charge [or] preliminary hearing.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. The prosecution in this case was commenced under Illinois law when the victim’s complaint was filed in court. See Ill. Rev. Stat., ch. 38, § 111 (1975). The purpose of the preliminary hearing was to determine whether there was probable cause to bind petitioner over to the grand jury and to set bail. §§ 109-1, 109-3. Petitioner had the right to oppose the prosecution at that hearing by moving to dismiss the charges and to suppress the evidence against him. § 109-3 (e). He faced counsel for the State, who elicited the victim’s identification, summarized the State’s other evidence against petitioner, and urged that the State be given more time to marshal its evidence. It is plain that “the government ha[d] committed itself to prosecute,” and that petitioner found “himself faced with the prosecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.” <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois"><em>Kirby, supra, </em>at 689</a></span>. The State candidly concedes that this preliminary hearing. marked the “initiation of adversary judicial criminal proceedings” against petitioner, Brief for Respondent 8, and n. 1; Tr. of Oral Arg. 32, 34, and it hardly could contend otherwise. The Court of Appeals therefore erred in holding <page-number citation-index="1" label="229">*229</page-number>that petitioner’s rights under <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>had not yet attached at the time of the preliminary hearing.</p>
<p id="b401-5">The Court of Appeals also suggested that <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>did not apply here because the “in-court identification could hardly be considered a line-up.” App. 45. The meaning of this statement is not entirely clear. If the court meant that a one-on-one identification procedure, as distinguished from a lineup, is not subject to the counsel requirement, it was mistaken. Although <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>both involved lineups, <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>clearly contemplated that counsel would be required in both situations: “The pretrial confrontation for purpose of identification may take the form of a lineup ... or presentation of the suspect alone to the witness .... It is obvious that risks of suggestion attend either form of confrontation . . . .” 388 U. S., at 229; see also <em>id., </em>at 251 (White, J., dissenting in part and concurring in part); cf. <em>Stovall </em>v. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra;</a></span> Kirby </em>v. <em>Illinois. </em>Indeed, a one-on-one confrontation generally is thought to present greater risks of mistaken identification than a lineup. <em>E. g., </em>P. Wall, EyeWitness Identification in Criminal Cases 27-40 (1965); Williams &amp; Hammelmann, Identification Parades — I, Crim. L. Rev. 479, 480-481 (1963). There is no reason, then, to hold that a one-on-one identification procedure is not subject to the same requirements as a lineup.</p>
<p id="b401-6">If the court believed that petitioner did not have a right to counsel at this identification procedure because it was conducted in the course of a judicial proceeding, we do not agree. The reasons supporting Wade’s holding that a corporeal identification is a critical stage of a criminal prosecution for Sixth Amendment purposes apply with equal force to this identification. It is difficult to imagine a more suggestive manner in which to present a suspect to a witness for their critical first confrontation than was employed in this case. The victim, who had seen her assailant for only 10 to 15 seconds, was asked to make her identification after she was told that she <page-number citation-index="1" label="230">*230</page-number>was going to view a suspect, after she was told his name and heard it called as he was led before the bench, and after she heard the prosecutor recite the evidence believed to implicate petitioner.<footnotemark>4</footnotemark> Had petitioner been represented by counsel, some or all of this suggestiveness could have been avoided.<footnotemark>5</footnotemark></p>
<p id="b403-4"><page-number citation-index="1" label="231">*231</page-number>In sum, we are unpersuaded by the reasons advanced by -the Court of Appeals for distinguishing the identification procedure in this case from those considered in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>. </em>Here, as in those cases, petitioner’s Sixth Amendment rights were violated by a corporeal identification conducted after the initiation of adversary judicial criminal proceedings and in the absence of counsel. The courts below thought that the victim’s testimony at trial that she had identified petitioner at an uncounseled pretrial confrontation was admissible even if petitioner’s rights had been violated, because there was an “independent source” for the victim’s identification at the uncounseled confrontation. <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#86" aria-description="Citation for case: People v. Moore">51 Ill. 2d, at 86</a></span>, <span class="citation" data-id="2157342"><a href="/opinion/2157342/people-v-moore/#298" aria-description="Citation for case: People v. Moore">281 N. E. 2d, at 298</a></span>; App. 35 (District Court), 45-46 (Court of Appeals).<footnotemark>6</footnotemark> But <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>held that the prosecution cannot buttress its case-in-chief by introducing evidence of a pretrial identification made in violation of the accused’s Sixth Amendment rights, even if it can prove that the pretrial identification had an independent source. “That testimony is the direct result of the illegal lineup 'come at by exploitation of [the primary] illegality,’ ” <em>Gilbert, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California">388 U. S., at 272-273</a></span>, and the prosecution is “therefore not entitled to an opportunity to show that the testimony had an independent source.” <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#273" aria-description="Citation for case: Gilbert v. California"><em>Id., </em>at 273</a></span>. Because the prosecution made use of such testimony <page-number citation-index="1" label="232">*232</page-number>in this case, petitioner is entitled to the benefit of the strict rule of <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span>.</em></p>
<p id="b404-5">IV</p>
<p id="b404-6">In view of the violation of petitioner’s Sixth and Fourteenth Amendment right to counsel at the pretrial corporeal identification, and of the prosecution’s exploitation at trial of evidence derived directly from that violation, we reverse the judgment of the Court of Appeals and remand for a determination of whether the failure to exclude that evidence was harmless constitutional error under <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). See <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#274" aria-description="Citation for case: Gilbert v. California"><em>Gilbert, supra, </em>at 274</a></span>. That court also will be free on remand to re-examine the other issues presented by the petition, upon which we do not pass.<footnotemark>7</footnotemark></p>
<p id="b404-7">
<em>Reversed and remanded.</em>
</p>
<judges id="b404-8">Me. Justice Stevens took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b395-7"> Counsel for petitioner explicitly drew the court’s attention to our then recent decision in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967): “If we may look at the Wade case, Your Honor, it has as its holding, Your Honor, the requirement that a defendant have an attorney at an identification procedure . . . .” Trial Transcript 132.</p>
</footnote>
<footnote label="2">
<p id="b398-7"> Among the factors to be considered in making this determination are “the prior opportunity to observe the alleged criminal act, the existence of any discrepancy between any pre-lineup description and the defendant’s actual description, any identification prior to lineup of another person, the identification by picture of the defendant prior to the lineup, failure to identify the defendant on a prior occasion, and the lapse of time between the alleged act and the lineup identification.” 388 U. S., at 241.</p>
</footnote>
<footnote label="3">
<p id="b399-7"> In <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">413 U. S. 300</a></span> (1973), the Court held that the Sixth Amendment does not require that defense counsel be present when a witness views police or prosecution photographic arrays. . A photographic showing, unlike a corporeal identification, is not a “trial-like adversary confrontation” between an accused and agents of the government; hence, “no possibility arises that the accused might be misled by his lack of familiarity with the law or overpowered by his professional adversary.” <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#317" aria-description="Citation for case: United States v. Ash"><em>Id., </em>at 317</a></span>. Moreover, even without attending the prosecution’s photographic showing, defense counsel has an equal chance to prepare for trial by presenting his own photographic displays to witnesses before trial. But “[duplication by defense counsel is a safeguard that normally is not available when a formal confrontation occurs.” <em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/" aria-description="Citation for case: United States v. Ash">Id.,</a></span> </em>at 318 n. 10. An accused nevertheless is entitled to due process protection against the introduction of evidence of, or tainted by, unreliable identifications elicited through unnecessarily suggestive photographic displays. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#320" aria-description="Citation for case: United States v. Ash"><em>Id., </em>at 320</a></span>; <em>Manson </em>v. <em>Brathwaite; Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968).</p>
</footnote>
<footnote label="4">
<p id="b402-5"> Immediately before the State's Attorney asked the victim to identify petitioner, he stated:</p>
<p id="b402-6">“This is an allegation of rape and deviate sexual assault. It’s a home invasion of an apartment in Hyde Park and the victim was raped and forced to commit an oral copulation. Taken from her was a guitar and other instruments. When the defendant was arrested upon an arrest warrant signed by the Judge of the Court, the articles, the guitar and other instruments were found in the apartment, as were the clothes described of the man that attacked her that day.” App. 48-49.</p>
<p id="b402-7">It appears from the record that although a guitar and a flute were found in petitioner’s apartment when he was arrested, they were not the ones taken from the victim’s apartment and they were not introduced into evidence at petitioner’s trial. Transcript of Proceedings at Hearing of Feb. 5, 1968, p. 10; Trial Transcript 4A-45, 400-401. Neither was any clothing.</p>
</footnote>
<footnote label="5">
<p id="b402-8"> For example, counsel could have requested that the hearing be postponed until a lineup could be arranged at which the victim would view petitioner in a less suggestive setting. See, <em>e. g., United States </em>v. <em>Ravich, </em><span class="citation" data-id="288484"><a href="/opinion/288484/united-states-v-ronald-raymond-ravich-and-edward-mcconnell/#1202" aria-description="Citation for case: United States v. Ronald Raymond Ravich and Edward McConnell">421 F. 2d 1196, 1202-1203</a></span> (CA2), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./400/834/">400 U. S. 834</a></span> (1970); <em>Mason </em>v. <em>United States, </em>134 U. S. App. D. C. 280, 283 n. 19, <span class="citation" data-id="286150"><a href="/opinion/286150/william-r-mason-v-united-states/" aria-description="Citation for case: William R. Mason v. United States">414 F. 2d 1176</a></span>, 1179 n. 19 (1969). Short of that, counsel could have asked that the victim be excused from the courtroom while the charges were read and the evidence against petitioner was recited, and that petitioner be seated with other people in the audience when the victim attempted an identification. See <em>Allen </em>v. <em>Rhay, </em><span class="citation" data-id="292225"><a href="/opinion/292225/gordon-m-allen-and-v-b-j-rhay-superintendent-of-the-washington-state/#1165" aria-description="Citation for case: Gordon M. Allen, and v. B. J. Rhay, Superintendent of the...">431 F. 2d 1160, 1165</a></span> (CA9 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/834/">404 U. S. 834</a></span> (1971). Counsel might have sought to cross-examine the victim to test her identification before it hardened. Cf. <em>Haberstroh </em>v. <em>Montanye, </em><span class="citation" data-id="317684"><a href="/opinion/317684/ralph-benno-haberstroh-v-superintendent-montanye-attica-correctional/#485" aria-description="Citation for case: Ralph Benno Haberstroh v. Superintendent Montanye, Attica...">493 F. 2d 483, 485</a></span> (CA2 1974); <em>United States ex rel. Riffert </em>v. <em>Rundle, </em><span class="citation" data-id="305033"><a href="/opinion/305033/united-states-of-america-ex-rel-james-r-riffert-v-alfred-t-rundle/#1351" aria-description="Citation for case: United States of America Ex Rel. James R. Riffert v....">464 F. 2d 1348, 1351</a></span> (CA3 1972), cert. denied <em>sub nom. Riffert </em>v. <em>Johnson, </em><span class="citation" data-id="8989309"><a href="/opinion/8996932/riffert-v-johnson/" aria-description="Citation for case: Riffert v. Johnson">415 U. S. 927</a></span> (1974). Because it is in the prosecution’s interest as well as the accused’s that witnesses’ identifications remain untainted, see <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#238" aria-description="Citation for case: United States v. Wade">388 U. S., at 238</a></span>, we cannot assume that such requests would have been in vain. Such requests ordinarily are addressed to the sound discretion of the court, see <em>United States </em>v. <span class="citation" data-id="288484"><a href="/opinion/288484/united-states-v-ronald-raymond-ravich-and-edward-mcconnell/#1203" aria-description="Citation for case: United States v. Ronald Raymond Ravich and Edward McConnell"><em>Ravich, supra, </em>at 1203</a></span>; we express no <page-number citation-index="1" label="231">*231</page-number>opinion as to whether the preliminary hearing court would have been required to grant any such requests.</p>
</footnote>
<footnote label="6">
<p id="b403-7"> The existence of an “independent source” was thought to be demonstrated by the victim’s selection of a picture of petitioner from the second photographic array. The courts below and the parties here have not been certain as to how many pictures the victim actually selected from that array. Although there is some ambiguity in the record, compare Trial Transcript 110-111, 113-114, 167, 290-292, 294, 307-308, 421, 454, with <em>id., </em>at 155-156, 158, 231-232, we think a fair reading indicates that the victim selected more than one photograph and that she did not make a positive identification of petitioner from them. But resolution of this factual issue is not necessary to our decision in this case.</p>
</footnote>
<footnote label="7">
<p id="b404-11"> In addition to his <em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span> </em>argument, petitioner urges that the victim’s in-court identification was tainted by the prior uncounseled identification, see <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>; </em>that the in-court identification was the unreliable product of an unnecessarily suggestive identification procedure and should have been excluded under the Due Process Clause of the Fourteenth Amendment, see <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977); and that the trial court’s denial of a transcript of the preliminary hearing was prejudicial constitutional error, see <em>Roberts </em>v. <em>LaVallee, </em><span class="citation" data-id="9423508"><a href="/opinion/107527/roberts-v-lavallee/" aria-description="Citation for case: Roberts v. LaVallee">389 U. S. 40</a></span> (1967).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Nardone v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Nardone v. United States"
type: case
citation: "308 U.S. 338 (1939)"
parallel_cite: "60 S. Ct. 266; 84 L. Ed. 307"
neutral_cite: 1939 U.S. LEXIS 1132
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1939
date_decided: 1939-12-11
docket: 240
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1939-12-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Nardone v. United States
  varies_by_point: false
  scope_note: "Foundational good law. Though arising under § 605 of the Communications Act, its 'fruit of the poisonous tree' and attenuation doctrine was carried into Fourth Amendment exclusionary-rule law (Wong Sun, Brown v. Illinois) and remains controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103259/nardone-v-united-states/"
  cluster_id: 103259
  opinion_id: 103259
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Anchor (attenuation; 'fruit of the poisonous tree')"
related: ["[[Silverthorne Lumber Co. v. United States]]", "[[Wong Sun v. United States]]", "[[Brown v. Illinois]]"]
aliases: ["Nardone v. United States (1939)"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "attenuation", "wiretap"]
holding: "Illegally obtained evidence may not be used derivatively: a defendant who proves an unlawful search/wiretap may show that a substantial part of the case against him is a 'fruit of the poisonous tree,' which must be excluded — unless the Government shows an independent origin, or the connection has become so attenuated as to dissipate the taint."
lake:
  record_id: Nardone v. United States
  status: verified
  projected_at: 2026-07-06
---

# Nardone v. United States

*308 U.S. 338 (1939)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Disambiguation:** This is *Nardone v. United States*, 308 U.S. 338 (1939) ("Nardone II" — [[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]] / [[Fruits and Attenuation|attenuation]]). It follows *Nardone v. United States*, 302 U.S. 379 (1937) ("Nardone I"), which held intercepted wiretap evidence inadmissible under § 605 of the Communications Act.

## Background
After *Nardone I* reversed the petitioners' fraud convictions because the prosecution rested on unlawfully intercepted telephone calls, they were retried and reconvicted. At the new trial the judge refused to let the defense examine the prosecution about the *uses* it had made of the wiretap information. The Court of Appeals read § 605 narrowly — barring only the intercepted words themselves, while allowing every derivative use of the unlawful taps.

## Issue
Whether the statutory bar on using unlawfully intercepted communications excludes only the intercepted words, or also bars the Government's derivative use of leads and evidence obtained from the illegal interception.

## Rule
Derivative use is barred. Quoting *Silverthorne*, the Court reaffirmed that illegally obtained evidence "shall not be used at all," and that "the knowledge gained by the Government's own wrong cannot be used by it … simply because it is used derivatively." — 308 U.S. at 340–341. ^pin-340

A defendant may attack derivative evidence as tainted: once he proves the illegality, "the trial judge must give opportunity, however closely confined, to the accused to prove that a substantial portion of the case against him was a *fruit of the poisonous tree*. This leaves ample opportunity to the Government to convince the trial court that its proof had an independent origin." — *Id.* at 341. ^pin-341

But the taint can dissipate: "As a matter of good sense … such connection may have become so attenuated as to dissipate the taint." — *Id.* ^pin-341b

## Application
Reading § 605 to exclude only the exact intercepted words while permitting full derivative use "would largely stultify" *Nardone I* and invite the very practices condemned there. The defendants had plainly established the unlawful wiretapping, so they were entitled to inquire whether parts of the Government's case derived from it; the trial judge's refusal to allow that inquiry was error. The Court placed the initial burden on the accused to prove the illegality and to make a solid (not fishing) taint claim, leaving the Government free to show an [[Inevitable Discovery and Independent Source|independent source]].

## Conclusion
The defendants were entitled to test whether the Government's proof was a fruit of the unlawful wiretap; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Nardone* coined the phrase **"fruit of the poisonous tree"** and recognized the **[[Fruits and Attenuation|attenuation]]** limit, building directly on [[Silverthorne Lumber Co. v. United States]]. Though decided under the wiretap statute, its doctrine became the framework for Fourth Amendment derivative-evidence analysis in [[Wong Sun v. United States]] and the [[Fruits and Attenuation|attenuation]] factors of [[Brown v. Illinois]].

## Appears on
- [[The Exclusionary Rule]] — *Anchor ([[Fruits and Attenuation|attenuation]]; '[[Common Legal Terms#fruit-of-the-poisonous-tree|fruit of the poisonous tree]]')*

## Sources
- *Nardone v. United States*, 308 U.S. 338 (1939) — https://www.courtlistener.com/opinion/103259/nardone-v-united-states/ — pinpoints: 340–341.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ab03926b2074dbd0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "308 U.S. 338 (1939)", "court": "U.S. Supreme Court", "neutral_cite": "1939 U.S. LEXIS 1132", "official_citation_present": true, "parallel_cite": "60 S. Ct. 266; 84 L. Ed. 307", "title": "Nardone v. United States", "year": "1939"}}
{"assertion_id": "0e448d6da8c8697a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Illegally obtained evidence may not be used derivatively: a defendant who proves an unlawful search/wiretap may show that a substantial part of the case against him is a 'fruit of the poisonous tree,' which must be excluded — unless the Government shows an independent origin, or the connection has become so attenuated as to dissipate the taint.", "title": "Nardone v. United States"}}
{"assertion_id": "709b067c66b042da", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Anchor (attenuation; 'fruit of the poisonous tree')", "title": "Nardone v. United States"}}
{"assertion_id": "6898f806f8360665", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Nardone v. United States"}}
{"assertion_id": "d65e68b153bd6615", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1939-12-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Nardone v. United States", "field_i_validity": "good_law", "scope_note": "Foundational good law. Though arising under § 605 of the Communications Act, its 'fruit of the poisonous tree' and attenuation doctrine was carried into Fourth Amendment exclusionary-rule law (Wong Sun, Brown v. Illinois) and remains controlling.", "title": "Nardone v. United States", "varies_by_point": "false"}}
```

### lake record — Nardone v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nardone v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Nardone v. United States",
    "case_name_short": "Nardone",
    "case_name_full": "NARDONE Et Al. v. UNITED STATES",
    "input_case_name": "Nardone v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1939-12-11",
    "year": 1939,
    "docket": "240",
    "cluster_id": 103259,
    "lead_opinion_id": 103259,
    "sibling_ids": [
      103259
    ],
    "absolute_url": "/opinion/103259/nardone-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8192760,
        "score": 20,
        "case_name": "Nardone v. United States"
      },
      {
        "cluster_id": 8192453,
        "score": 20,
        "case_name": "United States v. Nardone"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "308 U.S. 338",
      "volume": "308",
      "reporter": "U.S.",
      "page": "338",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "60 S. Ct. 266",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 307",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1939 U.S. LEXIS 1132",
        "volume": "1939",
        "reporter": "U.S. LEXIS",
        "page": "1132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "308 U.S. 338",
        "volume": "308",
        "reporter": "U.S.",
        "page": "338",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 S. Ct. 266",
        "volume": "60",
        "reporter": "S. Ct.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 L. Ed. 307",
        "volume": "84",
        "reporter": "L. Ed.",
        "page": "307",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1939 U.S. LEXIS 1132",
        "volume": "1939",
        "reporter": "U.S. LEXIS",
        "page": "1132",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "308 U.S. 338",
    "official_selection": {
      "court_class": "scotus",
      "selected": "308 U.S. 338",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-340",
      "page": null,
      "quote": "), which held intercepted wiretap evidence inadmissible under \u00a7 605 of the Communications Act. ## Background After *Nardone I* reversed the petitioners' fraud convictions because the prosecution rested on unlawfully intercepted telephone calls, they were retried and reconvicted. At the new trial the judge refused to let the defense examine the prosecution about the *uses* it had made of the wiretap information. The Court of Appeals read \u00a7 605 narrowly \u2014 barring only the intercepted words themselves, while allowing every derivative use of the unlawful taps. ## Issue Whether the statutory bar on using unlawfully intercepted communications excludes only the intercepted words, or also bars the Government's derivative use of leads and evidence obtained from the illegal interception. ## Rule Derivative use is barred. Quoting *Silverthorne*, the Court reaffirmed that illegally obtained evidence",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-341",
      "page": null,
      "quote": "the trial judge must give opportunity, however closely confined, to the accused to prove that a substantial portion of the case against him was a *fruit of the poisonous tree*. This leaves ample opportunity to the Government to convince the trial court that its proof had an independent origin.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-341b",
      "page": null,
      "quote": "As a matter of good sense \u2026 such connection may have become so attenuated as to dissipate the taint.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1939-12-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Nardone v. United States",
    "varies_by_point": false,
    "scope_note": "Foundational good law. Though arising under \u00a7 605 of the Communications Act, its 'fruit of the poisonous tree' and attenuation doctrine was carried into Fourth Amendment exclusionary-rule law (Wong Sun, Brown v. Illinois) and remains controlling.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gilbert, 06ca3055 (5-30-2007)",
          "cluster_id": 4021002,
          "cite": [
            "2007 Ohio 2717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brunetti",
          "cluster_id": 7901151,
          "cite": [
            "279 Conn. 39",
            "901 A.2d 1",
            "2006 Conn. LEXIS 248"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brunetti",
          "cluster_id": 2258701,
          "cite": [
            "883 A.2d 1167",
            "276 Conn. 40",
            "2005 Conn. LEXIS 456"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane1_negative"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McMann v. Richardson",
          "cluster_id": 108138,
          "cite": [
            "25 L. Ed. 2d 763",
            "90 S. Ct. 1441",
            "397 U.S. 759",
            "1970 U.S. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. United States",
          "cluster_id": 106022,
          "cite": [
            "4 L. Ed. 2d 697",
            "80 S. Ct. 725",
            "362 U.S. 257",
            "1960 U.S. LEXIS 1413",
            "78 A.L.R. 2d 233"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hasting",
          "cluster_id": 110933,
          "cite": [
            "76 L. Ed. 2d 96",
            "103 S. Ct. 1974",
            "461 U.S. 499",
            "1983 U.S. LEXIS 31",
            "51 U.S.L.W. 4572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fahy v. Connecticut",
          "cluster_id": 106699,
          "cite": [
            "11 L. Ed. 2d 171",
            "84 S. Ct. 229",
            "375 U.S. 85",
            "1963 U.S. LEXIS 128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Waterfront Commission of New York Harbor",
          "cluster_id": 106864,
          "cite": [
            "12 L. Ed. 2d 678",
            "84 S. Ct. 1594",
            "378 U.S. 52",
            "1964 U.S. LEXIS 2229",
            "56 L.R.R.M. (BNA) 2544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
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
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walder v. United States",
          "cluster_id": 105188,
          "cite": [
            "98 L. Ed. 2d 503",
            "74 S. Ct. 354",
            "347 U.S. 62",
            "1954 U.S. LEXIS 2453",
            "98 L. Ed. 503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Costello v. United States",
          "cluster_id": 106172,
          "cite": [
            "5 L. Ed. 2d 551",
            "81 S. Ct. 534",
            "365 U.S. 265",
            "1961 U.S. LEXIS 1945",
            "4 Fed. R. Serv. 2d 758"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Giordano",
          "cluster_id": 109020,
          "cite": [
            "40 L. Ed. 2d 341",
            "94 S. Ct. 1820",
            "416 U.S. 505",
            "1974 U.S. LEXIS 36"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harrison v. United States",
          "cluster_id": 107736,
          "cite": [
            "20 L. Ed. 2d 1047",
            "88 S. Ct. 2008",
            "392 U.S. 219",
            "1968 U.S. LEXIS 1349"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawn v. United States",
          "cluster_id": 105609,
          "cite": [
            "2 L. Ed. 2d 321",
            "78 S. Ct. 311",
            "355 U.S. 339",
            "1958 U.S. LEXIS 1859"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Nardone v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103259) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDg4MzgwODAwMDAwJnM9MTM3MDAzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103259%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(103259)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zOTAmcz01Njc4Mzc5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28103259%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103259)",
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
    "complete_query": "cites:(103259)",
    "indexed_citing_opinions": 1313,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103259,
        "count": 1313,
        "count_source": "search"
      }
    ],
    "citation_count": 1927,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/nardone-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MzE5OCZzPTY2MjI3NTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28103259%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103259,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103259,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103259,
        "cited_id": 102883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103259,
        "cited_id": 1494592,
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
    "date_created": "2026-07-05T14:56:52Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:57:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:57:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:01:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:57:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Nardone v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b403-3">
<span citation-index="1" class="star-pagination" label="339"> 
   *339
   </span>
  Mr. Justice Frankfurter
 </author>
<p id="Aov">
  delivered the opinion of the Court.
 </p>
<p id="b403-4">
  We are called upon for the second time to review affirmance by the Circuit Court of Appeals for the Second Circuit of petitioners’ convictions under an indictment for frauds on the revenue. In
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span>, this Court reversed the convictions on the first trial because, they were procured by evidence secured in violation of § 605 of the Communications Act of 1934 (c. 652, <span class="citation no-link">48 Stat. 1064</span>, 1103; <span class="citation no-link">47 U. S. C., § 605</span>). For details of the' facts reference is made to that case. Suffice it here to say that this evidence consisted of intercepted telephone messages, constituting
  <em>
   “a
  </em>
  vital part of the prosecution’s proof.”
 </p>
<p id="b403-5">
  Conviction followed a new trial, and “the main question” on the appeal below is the only question open here— namely, “whether the [trial] judge improperly refused to allow the accused to examine the prosecution as to the uses to which it had put the information” which
  <em>
   Nardone
  </em>
  v.
  <em>
   United <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">States, supra,</a></span>
  </em>
  found to have vitiated the original conviction. Though candidly doubtful of the result it reached, the Circuit Court of Appeals limited the scope of § 605 to the precise circumstances before this Court in the first
  <em>
   <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">Nardone</a></span>
  </em>
  case, and ruled .that “Congress had not also made incompetent testimony which had become accessible by the use of unlawful ‘taps’, for to divulge that information was not to divulge an intercepted telephone talk.” <span class="citation" data-id="1494592"><a href="/opinion/1494592/united-states-v-nardone/" aria-description="Citation for case: United States v. Nardone">106 F. 2d 41</a></span>.
 </p>
<p id="b403-6">
  The issue thus tendered by the Circuit Court of Appeals is the broad one, whether or nof§ 605 merely interdicts the introduction into evidence in a federal trial of intercepted telephone conversations, leaving the prosecution free to make every other use of the proscribed evidence. Plainly, this presents a far-reaching problem in
  <span citation-index="1" class="star-pagination" label="340"> 
   *340
   </span>
  the administration of federal criminal justice, and-we therefore brought the case here for disposition.
 </p>
<p id="b404-6">
  Any claim for the exclusion of evidence logically relevant in criminal prosecutions is heavily handicapped. It must be justified by an over-riding public policy expressed in the Constitution or the law of the land. In a problem such as that before us now, two opposing concerns must be.harmonized: on the one hand, the stern enforcement of the criminal law; on the other, protection of that realm of privacy left free by Constitution and laws but capable of infringement either through zeal or design. In accommodating both thesé concerns, meaning must be given to what Congress has written, even if not in explicit language, so as to effectuate the policy which Congress has formulated.
 </p>
<p id="b404-7">
  We are here dealing with specific prohibition of particular methods in obtaining evidence. The result of the holding below is to reduce the scope of § 605 to exclusion of the exact words heard through forbidden interceptions, allowing these interceptions every derivative use that they may serve. Such a reading of § 605 would largely stultify the policy which compelled our decision in
  <em>
   Nardone
  </em>
  v.
  <em>
   United States, supra.
  </em>
  That decision was not the product of a merely meticulous reading of technical language. It was the translation into practicality of broad considerations of morality and public well-being. This Court found that the logically relevant proof which Congress had outlawed, it outlawed because “inconsistent with ethical standards and destructive of personal liberty.” <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/#383" aria-description="Citation for case: Nardone v. United States">302 U. S. 379, 383</a></span>. To forbid the direct use of methods thus characterized but to pút no curb on their full indirect use would only invite the very methods deemed “inconsistent with ethical standards and destructive of personal liberty.” What was said in a different context in
  <em>
   Silverthorne Lamber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span>, is pertinent here: “The essence of a pro
  <span citation-index="1" class="star-pagination" label="341"> 
   *341
   </span>
  vision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the court, but that it shall not be used at all.” See
  <em>
   Gouled
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#307" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 307</a></span>. A decent respect for the policy of Congress must save us from imputing to it a self-defeating, if not disingenuous purpose.
 </p>
<p id="b405-6">
  Here, as in the
  <em>
   Silverthorne
  </em>
  case, the facts improperly obtained do not “become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any -others, but the knowledge gained by the Government’s own wrong cannot be used by it” simply because it is used derivatively. <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385,392</a></span>.
 </p>
<p id="b405-7">
  In practice this generalized statement may conceal concrete complexities. Sophisticated argument may prove a causal connection between information obtained through illicit wire-tapping and the Government’s proof. As a matter of good sense, however, such connection may have become so attenuated' as to dissipate the taint. A sensible way of dealing with such a situation — fair to the intendment of § 605, but fair also to the purposes of the criminal law — ought to be within the reach of experienced trial judges. The burden is, of course, on the accused in the first instance to prove to the trial court’s satisfaction that wire-tapping was unlawfully employed. Once that is established — as was plainly done here — the trial judge must give opportunity, however closely confined, to the accused to prove that a substantial portion of the ease against him was a fruit of the poisonous tree. ' This leaves ample opportunity to the Government to convince the trial court that its proof had an independent origin.
 </p>
<p id="b405-8">
  Dispatch in the trial of criminal causes is essential in bringing crime to book*. Therefore, timely steps must be taken to secure judicial determination of claims of ille^ gality on the part of agents of the Government in obtain
  <span citation-index="1" class="star-pagination" label="342"> 
   *342
   </span>
  ing testimony. To interrupt the course of the trial for such auxiliary inquiries impedes the momentum of the main proceeding and breaks the continuity of the jury’s attention. Like mischief would result were tenuous claims sufficient to justify the trial court’s indulgence of inquiry into the legitimacy of evidence in the Government’s possession. So to read a Congressional prohibition against the availability of certain evidence would be to subordinate the need for rigorous administration of justice to undue solicitude for potential and, it is to be hoped, abnormal disobedience of the law by the law’s officers. Therefore claims that taint attaches to any portion of the Government’s case must satisfy the trial court with their solidity and not be merely a means of eliciting what is in the Government’s possession before its submission to the jury. And if such a claim is made after the trial is under way, the judge must likewise be satisfied that the accused could not at an earlier stage have had adequate knowledge to make his claim. The civilized conduct of criminal trials cannot be confined within mechanical rules. It necessarily demands the authority of limited direction entrusted to the judge presiding in federal trials, including a well-established range of judicial discretion, subject to appropriate review on appeal, in ruling upon preliminary questions of fact. Such a system as ours must, within the limits here indicated, rely on the learning, good sense, fairness , and courage of federal trial judges.
 </p>
<p id="b406-4">
  We have dealt with this case on the basic issue tendered by the Circuit Court of Appeals and have not indulged in a finicking appraisal of the record, either as to the issue of the time limit of the proposed inquiry into the use to which the Government had put its illicit practices, or as to the existence of independent sources for the Government’s proof. Since the Circuit Court of Appeals did
  <span citation-index="1" class="star-pagination" label="343"> 
   *343
   </span>
  not question its timéliness, we shall not. And the hos? tility of the trial court to the whole scope of the inquiry reflected his own accord with the rule of law by which the Circuit Court of Appeals sustained him, and which we find erroneous.
 </p>
<p id="b407-6">
  The judgment must be reversed and remanded to the District Court for further proceedings in conformity with this opinion.
 </p>
<p id="b407-7">
<em>
   Reversed.
  </em>
</p>
<judges id="b407-8">
  Me. Justice McReynolds is of opinion that the Circuit Court of Appeals reached the proper conclusion upon reasons there adequately stated and its judgment should be affirmed.
 </judges>
<judges id="b407-9">
  Mr. Justice Reed took no part in the consideration or decision of this case.
 </judges>
</opinion>
```

---

## GROUP: content/cases/New Jersey v. T.L.O..md  (`case`, 5 assertions)

### content_page

```
---
title: "New Jersey v. T.L.O."
type: case
citation: "469 U.S. 325 (1985)"
parallel_cite: "105 S. Ct. 733; 83 L. Ed. 2d 720; 53 U.S.L.W. 4083"
neutral_cite: 1985 U.S. LEXIS 41
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1985
date_decided: 1985-01-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: New Jersey v. T.L.O.
  varies_by_point: false
  scope_note: "Anchor for the reasonableness standard governing school searches; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/"
  cluster_id: 111301
  opinion_id: 9429812
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Anchor"
related: ["[[Vernonia School District 47J v. Acton]]", "[[Safford Unified School District v. Redding]]", "[[National Treasury Employees Union v. Von Raab]]", "[[Terry v. Ohio]]"]
aliases: ["New Jersey v. TLO"]
tags: ["case", "fourth-amendment", "school-search", "special-needs", "reasonableness"]
holding: "A school official's search of a student requires only reasonableness under all the circumstances — justified at inception + reasonably…"
lake:
  record_id: New Jersey v. T.L.O.
  status: verified
  projected_at: 2026-07-09
---

# New Jersey v. T.L.O.

*469 U.S. 325 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A teacher found a 14-year-old student, T.L.O., smoking in a school bathroom. An assistant vice principal opened her purse, found cigarettes and rolling papers, and on continued inspection found marijuana, a pipe, plastic bags, money, and a list of students who owed her money. The evidence led to juvenile-delinquency charges.

## Issue
What standard governs a search of a student by a public school official under the Fourth Amendment.

## Rule
The Fourth Amendment applies to public school officials, but a school search requires only reasonableness under all the circumstances — not a warrant or probable cause. "[T]he legality of a search of a student should depend simply on the reasonableness, under all the circumstances, of the search." — 469 U.S. at 341. ^pin-341

"Determining the reasonableness of any search involves a twofold inquiry: first, one must consider 'whether the . . . action was justified at its inception,' . . . second, one must determine whether the search as actually conducted 'was reasonably related in scope to the circumstances which justified the interference in the first place.'" — *Id.* ^pin-341b

A school search is "justified at its inception" when there are reasonable grounds to suspect it will turn up evidence the student has violated the law or school rules, and is permissible in scope when the measures are reasonably related to the search's objectives and not excessively intrusive in light of the student's age and sex and the nature of the infraction. — [*Id.* at 341–42](https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/#:~:text=was-,justified%20at%20its%20inception). ^pin-342

## Application
The report that T.L.O. had been smoking in the bathroom gave reasonable grounds to suspect her purse contained cigarettes, justifying the search at its inception. Discovery of the rolling papers then gave reasonable suspicion that she possessed marijuana, justifying the further inspection that uncovered the drug evidence. The search was reasonable in scope at each step on these facts.

## Conclusion
The search was reasonable; the evidence was admissible, and the New Jersey Supreme Court's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *T.L.O.* established the reasonableness standard for school searches (and the "special needs" rationale articulated in Justice Blackmun's [[Common Legal Terms#concurring-opinion|concurrence]]), later applied to student drug testing ([[Vernonia School District 47J v. Acton]]) and to the scope of an intrusive school search ([[Safford Unified School District v. Redding]]).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *New Jersey v. T.L.O.*, 469 U.S. 325 (1985) — https://www.courtlistener.com/opinion/111301/new-jersey-v-t-l-o/ — pinpoints: 341, 341–42.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a08c815ebe6702ba", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "469 U.S. 325 (1985)", "court": "U.S. Supreme Court", "neutral_cite": "1985 U.S. LEXIS 41", "official_citation_present": true, "parallel_cite": "105 S. Ct. 733; 83 L. Ed. 2d 720; 53 U.S.L.W. 4083", "title": "New Jersey v. T.L.O.", "year": "1985"}}
{"assertion_id": "9dfa59b4619aa135", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A school official's search of a student requires only reasonableness under all the circumstances — justified at inception + reasonably…", "title": "New Jersey v. T.L.O."}}
{"assertion_id": "e609b263f00ff0d3", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Anchor", "title": "New Jersey v. T.L.O."}}
{"assertion_id": "028939ded3338a3c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "New Jersey v. T.L.O."}}
{"assertion_id": "94bd54a0ed99241d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-01-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "New Jersey v. T.L.O.", "field_i_validity": "good_law", "scope_note": "Anchor for the reasonableness standard governing school searches; good law.", "title": "New Jersey v. T.L.O.", "varies_by_point": "false"}}
```

### lake record — New Jersey v. T.L.O.

```json
{
  "schema_version": "s2.v1",
  "record_id": "New Jersey v. T.L.O.",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "New Jersey v. T. L. O.",
    "case_name_short": "TLO",
    "case_name_full": "New Jersey v. T. L. O.",
    "input_case_name": "New Jersey v. T.L.O.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1985-01-15",
    "year": 1985,
    "docket": null,
    "cluster_id": 111301,
    "lead_opinion_id": 9429812,
    "sibling_ids": [
      111301,
      9429812,
      9429813,
      9429814,
      9429815,
      9429816
    ],
    "absolute_url": "/opinion/111301/new-jersey-v-t-l-o/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 325",
      "volume": "469",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 733",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 720",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "720",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4083",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4083",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1985 U.S. LEXIS 41",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "41",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 325",
        "volume": "469",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 733",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "733",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 720",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "720",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1985 U.S. LEXIS 41",
        "volume": "1985",
        "reporter": "U.S. LEXIS",
        "page": "41",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 4083",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "4083",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 325",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-341",
      "page": null,
      "quote": "--- # New Jersey v. T.L.O. *469 U.S. 325 (1985)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A teacher found a 14-year-old student, T.L.O., smoking in a school bathroom. An assistant vice principal opened her purse, found cigarettes and rolling papers, and on continued inspection found marijuana, a pipe, plastic bags, money, and a list of students who owed her money. The evidence led to juvenile-delinquency charges. ## Issue What standard governs a search of a student by a public school official under the Fourth Amendment. ## Rule The Fourth Amendment applies to public school officials, but a school search requires only reasonableness under all the circumstances \u2014 not a warrant or probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-341b",
      "page": null,
      "quote": "Determining the reasonableness of any search involves a twofold inquiry: first, one must consider 'whether the . . . action was justified at its inception,' . . . second, one must determine whether the search as actually conducted 'was reasonably related in scope to the circumstances which justified the interference in the first place.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-342",
      "page": null,
      "quote": "justified at its inception",
      "star_marker": "341",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33899,
      "fragment": "#:~:text=was-,justified%20at%20its%20inception",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "New Jersey v. T.L.O.",
    "varies_by_point": false,
    "scope_note": "Anchor for the reasonableness standard governing school searches; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 10018723,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hilton",
          "cluster_id": 5144554,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fairfax Cnty. Sch. Bd. v. South Carolina",
          "cluster_id": 4624555,
          "cite": [
            "827 S.E.2d 592"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4476634,
          "cite": [
            "96 N.E.3d 719",
            "93 Mass. App. Ct. 6"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Villagran",
          "cluster_id": 4422358,
          "cite": [
            "477 Mass. 711",
            "81 N.E.3d 310"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ulbricht",
          "cluster_id": 7311405,
          "cite": [
            "79 F. Supp. 3d 466",
            "96 Fed. R. Serv. 348",
            "2015 U.S. Dist. LEXIS 2016",
            "2015 WL 105799"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Andre Jerome Lyle Jr.",
          "cluster_id": 2687555,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Clark",
          "cluster_id": 2690293,
          "cite": [
            "2013 Ohio 4731",
            "137 Ohio St. 3d 346",
            "999 N.E.2d 592"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
      },
      {
        "citing_case": {
          "name": "K.W. v. State of Indiana",
          "cluster_id": 851991,
          "cite": [
            "984 N.E.2d 610",
            "2013 WL 653023",
            "2013 Ind. LEXIS 147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane1_negative"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennard v. Dretke, Director, Texas Department of Criminal Justice, Correctional Institutions Division",
          "cluster_id": 136994,
          "cite": [
            "159 L. Ed. 2d 384",
            "124 S. Ct. 2562",
            "542 U.S. 274",
            "2004 U.S. LEXIS 4575",
            "17 Fla. L. Weekly Fed. S 420",
            "72 U.S.L.W. 4540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis Ex Rel. LaShonda D. v. Monroe County Board of Education",
          "cluster_id": 118290,
          "cite": [
            "143 L. Ed. 2d 839",
            "119 S. Ct. 1661",
            "526 U.S. 629",
            "1999 U.S. LEXIS 3452",
            "12 Fla. L. Weekly Fed. S 280",
            "67 U.S.L.W. 4329",
            "1999 Colo. J. C.A.R. 2948",
            "99 Cal. Daily Op. Serv. 3861",
            "99 Daily Journal DAR 4931"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. JL",
          "cluster_id": 118352,
          "cite": [
            "146 L. Ed. 2d 254",
            "120 S. Ct. 1375",
            "529 U.S. 266",
            "2000 U.S. LEXIS 2345",
            "13 Fla. L. Weekly Fed. S 216",
            "68 U.S.L.W. 4236",
            "2000 Cal. Daily Op. Serv. 2409",
            "2000 Colo. J. C.A.R. 1642",
            "2000 Daily Journal DAR 3226"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKoy v. North Carolina",
          "cluster_id": 112388,
          "cite": [
            "108 L. Ed. 2d 369",
            "110 S. Ct. 1227",
            "494 U.S. 433",
            "1990 U.S. LEXIS 1179",
            "58 U.S.L.W. 4311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Waters v. Churchill",
          "cluster_id": 1087950,
          "cite": [
            "128 L. Ed. 2d 686",
            "114 S. Ct. 1878",
            "511 U.S. 661",
            "1994 U.S. LEXIS 4104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hazelwood School District v. Kuhlmeier",
          "cluster_id": 111979,
          "cite": [
            "98 L. Ed. 2d 592",
            "108 S. Ct. 562",
            "484 U.S. 260",
            "1988 U.S. LEXIS 310",
            "56 U.S.L.W. 4079",
            "14 Media L. Rep. (BNA) 2081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
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
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bethel School District No. 403 v. Fraser",
          "cluster_id": 111754,
          "cite": [
            "92 L. Ed. 2d 549",
            "106 S. Ct. 3159",
            "478 U.S. 675",
            "1986 U.S. LEXIS 139",
            "54 U.S.L.W. 5054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Verdugo-Urquidez",
          "cluster_id": 112382,
          "cite": [
            "108 L. Ed. 2d 222",
            "110 S. Ct. 1056",
            "494 U.S. 259",
            "1990 U.S. LEXIS 1175",
            "1990 WL 16772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "New Jersey v. T.L.O.:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzIxMzE1MjAwMDAwJnM9NTk4MDg0MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODgmcz0xNDU3MDcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 0,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111301 OR 9429812 OR 9429813 OR 9429814 OR 9429815 OR 9429816)",
    "indexed_citing_opinions": 1437,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111301,
        "count": 1267,
        "count_source": "search"
      },
      {
        "opinion_id": 9429812,
        "count": 199,
        "count_source": "search"
      },
      {
        "opinion_id": 9429813,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429814,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429815,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429816,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2396,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/new-jersey-v-t-l-o.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NDQ1NyZzPTk1NDYxMjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111301+OR+9429812+OR+9429813+OR+9429814+OR+9429815+OR+9429816%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111301,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 103870,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 111268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 370522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 382282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 386325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 409447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 438820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 440480,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1292717,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1304814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1381369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1391108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1406903,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1463269,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1554742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1567651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1595918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1616294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1677246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1739670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1900299,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1950670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1961736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 1969621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2029772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2122374,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2156966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2183546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2261463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2308367,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111301,
        "cited_id": 2372587,
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
    "date_created": "2026-07-05T15:28:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:31:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:28:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — New Jersey v. T.L.O.

```
<opinion type="majority">
<author id="b469-7">Justice White</author>
<p id="AEJ">delivered the opinion of the Court.</p>
<p id="b469-8">We granted certiorari in this case to examine the appropriateness of the exclusionary rule as a remedy for searches carried out in violation of the Fourth Amendment by public school authorities. Our consideration of the proper application of the Fourth Amendment to the public schools, however, has led us to conclude that the search that gave rise to <page-number citation-index="1" label="328">*328</page-number>the case now before us did not violate the Fourth Amendment. Accordingly, we here address only the questions of the proper standard for assessing the legality of searches conducted by public school officials and the application of that standard to the facts of this case.</p>
<p id="b470-5">I</p>
<p id="b470-6">On March 7, 1980, a teacher at Piscataway High School in Middlesex County, N. J., discovered two girls smoking in a lavatory. One of the two girls was the respondent T. L. 0., who at that time was a 14-year-old high school freshman. Because smoking in the lavatory was a violation of a school rule, the teacher took the two girls to the Principal’s office, where they met with Assistant Vice Principal Theodore Choplick. In response to questioning by Mr. Choplick, T. L. O.’s companion admitted that she had violated the rule. T. L. 0., however, denied that she had been smoking in the lavatory and claimed that she did not smoke at all.</p>
<p id="b470-7">Mr. Choplick asked T. L. O. to come into his private office and demanded to see her purse. Opening the purse, he found a pack of cigarettes, which he removed from the purse and held before T. L. O. as he accused her of having lied to him. As he reached into the purse for the cigarettes, Mr. Choplick also noticed a package of cigarette rolling papers. In his experience, possession of rolling papers by high school students was closely associated with the use of marihuana. Suspecting that a closer examination of the purse might yield further evidence of drug use, Mr. Choplick proceeded to search the purse thoroughly. The search revealed a smáll amount of marihuana, a pipe, a number of empty plastic bags, a substantial quantity of money in one-dollar bills, an index card that appeared to be a list of students who owed T. L. O. money, and two letters that implicated T. L. O. in marihuana dealing.</p>
<p id="b470-8">Mr. Choplick notified T. L. O.’s mother and the police, and turned the evidence of drug dealing over to the police. At <page-number citation-index="1" label="329">*329</page-number>the request of the police, T. L. O.’s mother took her daughter to police headquarters, where T. L. O. confessed that she had been selling marihuana at the high school. On the basis of the confession and the evidence seized by Mr. Choplick, the State brought delinquency charges against T. L. O. in the Juvenile and Domestic Relations Court of Middlesex County.<footnotemark>1</footnotemark> Contending that Mr. Choplick’s search of her purse violated the Fourth Amendment, T. L. O. moved to suppress the evidence found in her purse as well as her confession, which, she argued, was tainted by the allegedly unlawful search. The Juvenile Court denied the motion to suppress. <em>State ex rel. T. L. O., </em>178 N. J. Super. 329, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/" aria-description="Citation for case: State in Interest of TLO">428 A. 2d 1327</a></span> (1980). Although the court concluded that the Fourth Amendment did apply to searches carried out by school officials, it held that</p>
<blockquote id="b471-5">“a school official may properly conduct a search of a student’s person if the official has a reasonable suspicion that a crime has been or is in the process of being committed, or reasonable cause to believe that the search is necessary to maintain school discipline or enforce school policies.” <em>Id., </em>at 341, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/#1333" aria-description="Citation for case: State in Interest of TLO">428 A. 2d, at 1333</a></span> (emphasis in original).</blockquote>
<p id="b471-6">Applying this standard, the court concluded that the search conducted by Mr. Choplick was a reasonable one. The initial decision to open the purse was justified by Mr. Choplick’s well-founded suspicion that T. L. O. had violated the rule forbidding smoking in the lavatory. Once the purse <page-number citation-index="1" label="330">*330</page-number>was open, evidence of marihuana violations was in plain view, and Mr. Choplick was entitled to conduct a thorough search to determine the nature and extent of T. L. O.’s drug-related activities. <em>Id., </em>at 343, <span class="citation" data-id="2261463"><a href="/opinion/2261463/state-in-interest-of-tlo/#1334" aria-description="Citation for case: State in Interest of TLO">428 A. 2d, at 1334</a></span>. Having denied the motion to suppress, the court on March 23, 1981, found T. L. O. to be a delinquent and on January 8, 1982, sentenced her to a year’s probation.</p>
<p id="b472-5">On appeal from the final judgment of the Juvenile Court, a divided Appellate Division affirmed the trial court’s finding that there had been no Fourth Amendment violation, but vacated the adjudication of delinquency and remanded for a determination whether T. L. O. had knowingly and voluntarily waived her Fifth Amendment rights before confessing. <em>State ex rel. T. L. O., </em>185 N. J. Super. 279, <span class="citation" data-id="7318184"><a href="/opinion/7399164/state-ex-rel-t-l-o/" aria-description="Citation for case: State ex rel. T. L. O.">448 A. 2d 493</a></span> (1982). T. L. O. appealed the Fourth Amendment ruling, and the Supreme Court of New Jersey reversed the judgment of the Appellate Division and ordered the suppression of the evidence found in T. L. O.’s purse. <em>State ex rel. T. L. O., </em>94 N. J. 331, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/" aria-description="Citation for case: State v. Engerud">463 A. 2d 934</a></span> (1983).</p>
<p id="b472-6">The New Jersey Supreme Court agreed with the lower courts that the Fourth Amendment applies to searches conducted by school officials. The court also rejected the State of New Jersey’s argument that the exclusionary rule should not be employed to prevent the use in juvenile proceedings of evidence unlawfully seized by school officials. Declining to consider whether applying the rule to the fruits of searches by school officials would have any deterrent value, the court held simply that the precedents of this Court establish that “if an official search violates constitutional rights, the evidence is not admissible in criminal proceedings.” <em>Id., </em>at 341, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#939" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 939</a></span> (footnote omitted).</p>
<p id="b472-7">With respect to the question of the legality of the search before it, the court agreed with the Juvenile Court that a warrantless search by a school official does not violate the Fourth Amendment so long as the official “has reasonable grounds to believe that a student possesses evidence of illegal <page-number citation-index="1" label="331">*331</page-number>activity or activity that would interfere with school discipline and order.” <em>Id., </em>at 346, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#941" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 941-942</a></span>. However, the court, with two justices dissenting, sharply disagreed with the Juvenile Court’s conclusion that the search of the purse was reasonable. According to the majority, the contents of T. L. O.’s purse had no bearing on the accusation against T. L. 0., for possession of cigarettes (as opposed to smoking them in the lavatory) did not violate school rules, and a mere desire for evidence that would impeach T. L. O.’s claim that she did not smoke cigarettes could not justify the search. Moreover, even if a reasonable suspicion that T. L. O. had cigarettes in her purse would justify a search, Mr. Choplick had no such suspicion, as no one had furnished him with any specific information that there were cigarettes in the purse. Finally, leaving aside the question whether Mr. Choplick was justified in opening the purse, the court held that the evidence of drug use that he saw inside did not justify the extensive “rummaging” through T. L. O.’s papers and effects that followed. <em>Id., </em>at 347, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#942" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 942-943</a></span>.</p>
<p id="b473-5">We granted the State of New Jersey’s petition for certio-rari. <span class="citation multiple-matches"><a href="/c/U.%20S./464/991/">464 U. S. 991</a></span> (1983). Although the State had argued in the Supreme Court of New Jersey that the search of T. L. O.’s purse did not violate the Fourth Amendment, the petition for certiorari raised only the question whether the exclusionary rule should operate to bar consideration in juvenile delinquency proceedings of evidence unlawfully seized by a school official without the involvement of law enforcement officers. When this case was first argued last Term, the State conceded for the purpose of argument that the standard devised by the New Jersey Supreme Court for determining the legality of school searches was appropriate and that the court had correctly applied that standard; the State contended only that the remedial purposes of the exclusionary rule were not well served by applying it to searches conducted by public authorities not primarily engaged in law enforcement.</p>
<p id="b474-4"><page-number citation-index="1" label="332">*332</page-number>Although we originally granted certiorari to decide the issue of the appropriate remedy in juvenile court proceedings for unlawful school searches, our doubts regarding the wisdom of deciding that question in isolation from the broader question of what limits, if any, the Fourth Amendment places on the activities of school authorities prompted us to order reargument on that question.<footnotemark>2</footnotemark> Having heard argument on <page-number citation-index="1" label="333">*333</page-number>the legality of the search of T. L. O.’s purse, we are satisfied that the search did not violate the Fourth Amendment.<footnotemark>3</footnotemark></p>
<p id="b475-5">II</p>
<p id="b475-6">In determining whether the search at issue in this case violated the Fourth Amendment, we are faced initially with the question whether that Amendment’s prohibition on unreasonable searches and seizures applies to searches conducted by public school officials. We hold that it does.</p>
<p id="b476-4"><page-number citation-index="1" label="334">*334</page-number>It is now beyond dispute that “the Federal Constitution, by virtue of the Fourteenth Amendment, prohibits unreasonable searches and seizures by state officers.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span> (1960); accord, <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961); <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span> (1949). Equally indisputable is the proposition that the Fourteenth Amendment protects the rights of students against encroachment by public school officials:</p>
<blockquote id="b476-5">“The Fourteenth Amendment, as now applied to the States, protects the citizen against the State itself and all of its creatures — Boards of Education not excepted. These have, of course, important, delicate, and highly discretionary functions, but none that they may not perform within the limits of the Bill of Rights. That they are educating the young for citizenship is reason for scrupulous protection of Constitutional freedoms of the individual, if we are not to strangle the free mind at its source and teach youth to discount important principles of our government as mere platitudes.” <em>West Virginia State Bd. of Ed. </em>v. <em>Barnette, </em><span class="citation" data-id="9419378"><a href="/opinion/103870/west-virginia-state-board-of-education-v-barnette/#637" aria-description="Citation for case: West Virginia State Board of Education v. Barnette">319 U. S. 624, 637</a></span> (1943).</blockquote>
<p id="b476-6">These two propositions — that the Fourth Amendment applies to the States through the Fourteenth Amendment, and that the actions of public school officials are subject to the limits placed on state action by the Fourteenth Amendment — might appear sufficient to answer the suggestion that the Fourth Amendment does not proscribe unreasonable searches by school officials. On reargument, however, the State of New Jersey has argued that the history of the Fourth Amendment indicates that the Amendment was intended to regulate only searches and seizures carried out by law enforcement officers; accordingly, although public school officials are concededly state agents for purposes of the Fourteenth Amendment, the Fourth Amendment creates no rights enforceable against them.<footnotemark>4</footnotemark></p>
<p id="b477-4"><page-number citation-index="1" label="335">*335</page-number>It may well be true that the evil toward which the Fourth Amendment was primarily directed was the resurrection of the pre-Revolutionary practice of using general warrants or “writs of assistance” to authorize searches for contraband by officers of the Crown. See <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-629</a></span> (1886). But this Court has never limited the Amendment’s prohibition on unreasonable searches and seizures to operations conducted by the police. Rather, the Court has long spoken of the Fourth Amendment’s strictures as restraints imposed upon “governmental action” — that is, “upon the activities of sovereign authority.” <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 475</a></span> (1921). Accordingly, we have held the Fourth Amendment applicable to the activities of civil as well as criminal authorities: building inspectors, see <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967), Occupational Safety and Health Act inspectors, see <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978), and even firemen entering privately owned premises to battle a fire, see <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#506" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 506</a></span> (1978), are all subject to the restraints imposed by the Fourth Amendment. As we observed in <em>Camara </em>v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>“[t]he basic purpose of this Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials.” <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. Because the individual’s interest in privacy and personal security “suffers whether the government’s motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards,” <em>Marshall </em>v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><em>Barlow’s, Inc., supra, </em>at 312-313</a></span>, it would be “anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 530</a></span>.</p>
<p id="b478-3"><page-number citation-index="1" label="336">*336</page-number>Notwithstanding the general applicability of the Fourth Amendment to the activities of civil authorities, a few courts have concluded that school officials are exempt from the dictates of the Fourth Amendment by virtue of the special nature of their authority over schoolchildren. See, <em>e. g., R. C. M. </em>v. <em>State, </em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">660 S. W. 2d 552</a></span> (Tex. App. 1983). Teachers and school administrators, it is said, act <em>in loco parentis </em>in their dealings with students: their authority is that of the parent, not the State, and is therefore not subject to the limits of the Fourth Amendment. <em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">Ibid.</a></span></em></p>
<p id="b478-4">Such reasoning is in tension with contemporary reality and the teachings of this Court. We have held school officials subject to the commands of the First Amendment, see <em>Tinker </em>v. <em>Des Moines Independent Community School District, </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503</a></span> (1969), and the Due Process Clause of the Fourteenth Amendment, see <em>Goss </em>v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/" aria-description="Citation for case: Goss v. Lopez">419 U. S. 565</a></span> (1975). If school authorities are state actors for purposes of the constitutional guarantees of freedom of expression and due process, it is difficult to understand why they should be deemed to be exercising parental rather than public authority when conducting searches of their students. More generally, the Court has recognized that “the concept of parental delegation” as a source of school authority is not entirely “consonant with compulsory education laws.” <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#662" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 662</a></span> (1977). Today’s public school officials do not merely exercise authority voluntarily conferred on them by individual parents; rather, they act in furtherance of publicly mandated educational and disciplinary policies. See, <em>e. g., </em>the opinion in <em>State ex rel. T. L. O., </em>94 N. J., at 343, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#934" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 934, 940</a></span>, describing the New Jersey statutes regulating school disciplinary policies and establishing the authority of school officials over their students. In carrying out searches and other disciplinary functions pursuant to such policies, school officials act as representatives of the State, not merely as surrogates for the parents, and they <page-number citation-index="1" label="337">*337</page-number>cannot claim the parents’ immunity from the strictures of the Fourth Amendment.</p>
<p id="b479-5">Ill</p>
<p id="b479-6">To hold that the Fourth Amendment applies to searches conducted by school authorities is only to begin the inquiry into the standards governing such searches. Although the underlying command of the Fourth Amendment is always that searches and seizures be reasonable, what is reasonable depends on the context within which a search takes place. The determination of the standard of reasonableness governing any specific class of searches requires “balancing the need to search against the invasion which the search entails.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 536-537</a></span>. On one side of the balance are arrayed the individual’s legitimate expectations of privacy and personal security; on the other, the government’s need for effective methods to deal with breaches of public order.</p>
<p id="b479-7">We have recognized that even a limited search of the person is a substantial invasion of privacy. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 24-25</a></span> (1967). We have also recognized that searches of closed items of personal luggage are intrusions on protected privacy interests, for “the Fourth Amendment pro-' vides protection to the owner of every container that conceals" its contents from plain view.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#822" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 822-823</a></span> (1982). A search of a child’s person or of' a closed purse or other bag carried on her person,<footnotemark>5</footnotemark> no less <page-number citation-index="1" label="338">*338</page-number>than a similar search carried out on an adult, is undoubtedly a severe violation of subjective expectations of privacy.</p>
<p id="b480-5">. Of course, the Fourth Amendment does not protect subjective expectations of privacy that are unreasonable or otherwise “illegitimate.” See, <em>e. g., Hudson </em>v. <em>Palmer, </em><span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984); <em>Rawlings </em>v. <em>Kentucky, </em><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98</a></span> (1980). To receive the protection of the Fourth Amendment, an expectation of privacy must be one that society is “prepared to recognize as legitimate.” <em>Hudson </em>v. <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#526" aria-description="Citation for case: Hudson v. Palmer"><em>Palmer, supra, </em>at 526</a></span>. The State of New Jersey has argued that because of the pervasive supervision to which children in the schools are necessarily subject, a child has virtually no legitimate expectation of privacy in articles of personal property “unnecessarily” carried into a school. This argument has two factual premises: (1) the fundamental incompatibility of expectations of privacy with the maintenance of a sound educational environment; and (2) the minimal interest of the child in bringing any items of personal property into the school. Both premises are severely flawed.</p>
<p id="b480-6">Although this Court may take notice of the difficulty of maintaining discipline in the public schools today, the situation is not so dire that students in the schools may claim no legitimate expectations of privacy. We have recently recognized that the need to maintain order in a prison is such that prisoners retain no legitimate expectations of privacy in their cells, but it goes almost without saying that “[tjhe prisoner and the schoolchild stand in wholly different circumstances, separated by the harsh facts of criminal conviction and incarceration.” <em>Ingraham </em>v. <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#669" aria-description="Citation for case: Ingraham v. Wright"><em>Wright, supra, </em>at 669</a></span>. We are not <page-number citation-index="1" label="339">*339</page-number>yet ready to hold that the schools and the prisons need be equated for purposes of the Fourth Amendment.</p>
<p id="b481-5">Nor does the State’s suggestion that children have no legitimate need to bring personal property into the schools seem well anchored in reality. Students at a minimum must bring to school not only the supplies needed for their studies, but also keys, money, and the necessaries of personal hygiene and grooming. In addition, students may carry on their persons or in purses or wallets such nondisruptive yet highly personal items as photographs, letters, and diaries. Finally, students may have perfectly legitimate reasons to carry with them articles of property needed in connection with extracurricular or recreational activities. In short, schoolchildren may find it necessary to carry with them a variety of legitimate, noncontraband items, and there is no reason to conclude that they have necessarily waived all rights to privacy in such items merely by bringing them onto school grounds.</p>
<p id="b481-6">Against the child’s interest in privacy must be set the substantial interest of teachers and administrators in maintaining discipline in the classroom and on school grounds. Maintaining order in the classroom has never been easy, but in recent years, school disorder has often taken particularly ugly forms: drug use and violent crime in the schools have become major social problems. See generally 1 NIE, U. S. Dept, of Health, Education and Welfare, Violent Schools— Safe Schools: The Safe School Study Report to the Congress (1978). Even in schools that have been spared the most severe disciplinary problems, the preservation of order and a proper educational environment requires close supervision of schoolchildren, as well as the enforcement of rules against conduct that would be perfectly permissible if undertaken by an adult. “Events calling for discipline are frequent occurrences and sometimes require immediate, effective action.” Goss v. <em>Lopez, </em><span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#580" aria-description="Citation for case: Goss v. Lopez">419 U. S., at 580</a></span>. Accordingly, we have rec<page-number citation-index="1" label="340">*340</page-number>ognized that maintaining security and order in the schools requires a certain degree of flexibility in school disciplinary procedures, and we have respected the value of preserving the informality of the student-teacher relationship. See <span class="citation" data-id="9425909"><a href="/opinion/109136/goss-v-lopez/#582" aria-description="Citation for case: Goss v. Lopez"><em>id., </em>at 582-583</a></span>; <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#680" aria-description="Citation for case: Ingraham v. Wright">430 U. S., at 680-682</a></span>.</p>
<p id="b482-5">How, then, should we strike the balance between the schoolchild’s legitimate expectations of privacy and the school’s equally legitimate need to maintain an environment in which learning can take place? It is evident that the school setting requires some easing of the restrictions to which searches by public authorities are ordinarily subject. The warrant requirement, in particular, is unsuited to the school environment: requiring a teacher to obtain a warrant before searching a child suspected of an infraction of school rules (or of the criminal law) would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools. Just as we have in other cases dispensed with the warrant requirement when “the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search,” <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532-533</a></span>, we hold today that school officials need not obtain a warrant before searching a student who is under their authority.</p>
<p id="b482-6">The school setting also requires some modification of the level of suspicion of illicit activity needed to justify a search. Ordinarily, a search — even one that may permissibly be carried out without a warrant — must be based upon “probable cause” to believe that a violation of the law has occurred. See, <em>e. g., Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#273" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 273</a></span> (1973); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/#62" aria-description="Citation for case: Sibron v. New York">392 U. S. 40, 62-66</a></span> (1968). However, “probable cause” is not an irreducible requirement of a valid search. The fundamental command of the Fourth Amendment is that searches and seizures be reasonable, and although “both the concept of probable cause and the requirement of a warrant bear on the reasonableness of a search, . . . in certain limited circumstances neither is required.” <em>Almeida-Sanchez </em>v. <em>United States, supra, </em>at 277 (Powell, <page-number citation-index="1" label="341">*341</page-number>J., concurring). Thus, we have in a number of cases recognized the legality of searches and seizures based on suspicions that, although “reasonable,” do not rise to the level of probable cause. See, <em>e. g., Terry </em>v. Ohio, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 881</a></span> (1975); <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976); cf. <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 534-539</a></span>. Where a careful balancing of governmental and private interests suggests that the public interest is best served by a Fourth Amendment standard of reasonableness that stops short of probable cause, we have not hesitated to adopt such a standard.</p>
<p id="b483-5">We join the majority of courts that have examined this issue<footnotemark>6</footnotemark> in concluding that the accommodation of the privacy interests of schoolchildren with the substantial need of teachers and administrators for freedom to maintain order in the schools does not require strict adherence to the requirement that searches be based on probable cause to believe that the subject of the search has violated or is violating the law. Rather, the legality of a search of a student should depend simply on the reasonableness, under all the circumstances, of the search. Determining the reasonableness of any search involves a twofold inquiry: first, one must consider “whether the . . . action was justified at its inception,” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20</a></span>; second, one must determine whether the search as actually conducted “was reasonably related in scope to the circumstances which justified the interference in the first place,” <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">ibid.</a></span> </em>Under ordinary circumstances, a search of a student by a teacher or other school official<footnotemark>7</footnotemark> will be <page-number citation-index="1" label="342">*342</page-number>“justified at its inception” when there are reasonable grounds for suspecting that the search will turn up evidence that the student has violated or is violating either the law or the rules of the school.<footnotemark>8</footnotemark> Such a search will be permissible in its scope when the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of the age and sex of the student and the nature of the infraction.<footnotemark>9</footnotemark></p>
<p id="b484-5">This standard will, we trust, neither unduly burden the efforts of school authorities to maintain order in their schools <page-number citation-index="1" label="343">*343</page-number>nor authorize unrestrained intrusions upon the privacy of schoolchildren. By focusing attention on the question of reasonableness, the standard will spare teachers and school administrators the necessity of schooling themselves in the niceties of probable cause and permit them to regulate their conduct according to the dictates of reason and common sense. At the same time, the reasonableness standard should ensure that the interests of students will be invaded no more than is necessary to achieve the legitimate end of preserving order in the schools.</p>
<p id="b485-5">IV</p>
<p id="b485-6">There remains the question of the legality of the search in this case. We recognize that the “reasonable grounds” standard applied by the New Jersey Supreme Court in its consideration of this question is not substantially different from the standard that we have adopted today. Nonetheless, we believe that the New Jersey court’s application of that standard to strike down the search of T. L. O.’s purse reflects a somewhat crabbed notion of reasonableness. Our review of the facts surrounding the search leads us to conclude that the search was in no sense unreasonable for Fourth Amendment purposes.<footnotemark>10</footnotemark></p>
<p id="b485-7">The incident that gave rise to this case actually involved two separate searches, with the first — the search for cigarettes — providing the suspicion that gave rise to the sec<page-number citation-index="1" label="344">*344</page-number>ond — the search for marihuana. Although it is the fruits of the second search that are at issue here, the validity of the search for marihuana must depend on the reasonableness of the initial search for cigarettes, as there would have been no reason to suspect that T. L. O. possessed marihuana had the first search not taken place. Accordingly, it is to the search for cigarettes that we first turn our attention.</p>
<p id="b486-5">The New Jersey Supreme Court pointed to two grounds for its holding that the search for cigarettes was unreasonable. First, the court observed that possession of cigarettes was not in itself illegal or a violation of school rules. Because the contents of T. L. O.’s purse would therefore have “no direct bearing on the infraction” of which she was accused (smoking in a lavatory where smoking was prohibited), there was no reason to search her purse.<footnotemark>11</footnotemark> Second, even assuming that a search of T. L. O.’s purse might under some circumstances be reasonable in light of the accusation made against T. L. 0., the New Jersey court concluded that Mr. Choplick in this particular case had no reasonable grounds to suspect that T. L. O. had cigarettes in her purse. At best, accord<page-number citation-index="1" label="345">*345</page-number>ing to the court, Mr. Chopliek had “a good hunch.” 94 N. J., at 347, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#942" aria-description="Citation for case: State v. Engerud">463 A. 2d, at 942</a></span>.</p>
<p id="b487-5">Both these conclusions are implausible. T. L. O. had been accused of smoking, and had denied the accusation in the strongest possible terms when she stated that she did not smoke at all. Surely it cannot be said that under these circumstances, T. L. O.’s possession of cigarettes would be irrelevant to the charges against her or to her response to those charges. T. L. O.’s possession of cigarettes, once it was discovered, would both corroborate the report that she had been smoking and undermine the credibility of her defense to the charge of smoking. To be sure, the discovery of the cigarettes would not prove that T. L. O. had been smoking in the lavatory; nor would it, strictly speaking, necessarily be inconsistent with her claim that she did not smoke at all. But it is universally recognized that evidence, to be relevant to an inquiry, need not conclusively prove the ultimate fact in issue, but only have “any tendency to make the existence of any fact that is of consequence to the determination of the action more probable or less probable than it would be without the evidence.” Fed. Rule Evid. 401. The relevance of T. L. O.’s possession of cigarettes to the question whether she had been smoking and to the credibility of her denial that she smoked supplied the necessary “nexus” between the item searched for and the infraction under investigation. See <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#306" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 306-307</a></span> (1967). Thus, if Mr. Chopliek in fact had a reasonable suspicion that T. L. O. had cigarettes in her purse, the search was justified despite the fact that the cigarettes, if found, would constitute “mere evidence” of a violation. <em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Ibid.</a></span></em></p>
<p id="b487-6">Of course, the New Jersey Supreme Court also held that Mr. Chopliek had no reasonable suspicion that the purse would contain cigarettes. This conclusion is puzzling. A teacher had reported that T. L. O. was smoking in the lavatory. Certainly this report gave Mr. Chopliek reason to suspect that T. L. O. was carrying cigarettes with her; and <page-number citation-index="1" label="346">*346</page-number>if she did have cigarettes, her purse was the obvious place in which to find them. Mr. Choplick’s suspicion that there were cigarettes in the purse was not an “inchoate and un-particularized suspicion or ‘hunch,’” <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 27</a></span>; rather, it was the sort of “common-sense conclusio[n] about human behavior” upon which “practical people” — including government officials — are entitled to rely. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#418" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 418</a></span> (1981). Of course, even if the teacher’s report were true, T. L. O. <em>might </em>not have had a pack of cigarettes with her; she might have borrowed a cigarette from someone else or have been sharing a cigarette with another student. But the requirement of reasonable suspicion is not a requirement of absolute certainty: “sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment. ...” <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#804" aria-description="Citation for case: Hill v. California">401 U. S. 797, 804</a></span> (1971). Because the hypothesis that T. L. O. was carrying cigarettes in her purse was itself not unreasonable, it is irrelevant that other hypotheses were also consistent with the teacher’s accusation. Accordingly, it cannot be said that Mr. Choplick acted unreasonably when he examined T. L. O.’s purse to see if it contained cigarettes.<footnotemark>12</footnotemark></p>
<p id="b489-4"><page-number citation-index="1" label="347">*347</page-number>Our conclusion that Mr. Choplick’s decision to open T. L. O.’s purse was reasonable brings us to the question of the further search for marihuana once the pack of cigarettes was located. The suspicion upon which the search for marihuana was founded was provided when Mr. Choplick observed a package of rolling papers in the purse as he removed the pack of cigarettes. Although T. L. O. does not dispute the reasonableness of Mr. Choplick’s belief that the rolling papers indicated the presence of marihuana, she does contend that the scope of the search Mr. Choplick conducted exceeded permissible bounds when he seized and read certain letters that implicated T. L. O. in drug dealing. This argument, too, is unpersuasive. The discovery of the rolling papers concededly gave rise to a reasonable suspicion that T. L. O. was carrying marihuana as well as cigarettes in her purse. This suspicion justified further exploration of T. L. O.’s purse, which turned up more evidence of drug-related activities: a pipe, a number of plastic bags of the type commonly used to store marihuana, a small quantity of marihuana, and a fairly substantial amount of money. Under these circumstances, it was not unreasonable to extend the search to a separate zippered compartment of the purse; and when a search of that compartment revealed an index card containing a list of “people who owe me money” as well as two letters, the inference that T. L. O. was involved in marihuana trafficking was substantial enough to justify Mr. Choplick in examining the letters to determine whether they contained any further evidence. In short, we cannot conclude that the search for marihuana was unreasonable in any respect.</p>
<p id="b489-5">Because the search resulting in the discovery of the evidence of marihuana dealing by T. L. O. was reasonable, the New Jersey Supreme Court’s decision to exclude that evi<page-number citation-index="1" label="348">*348</page-number>dence from T. L. O.’s juvenile delinquency proceedings on Fourth Amendment grounds was erroneous. Accordingly, the judgment of the Supreme Court of New Jersey is</p>
<p id="b490-5">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b471-7"> T. L. O. also received a 3-day suspension from school for smoking cigarettes in a nonsmoking area and a 7-day suspension for possession of marihuana. On T. L. O.’s motion, the Superior Court of New Jersey, Chancery Division, set aside the 7-day suspension on the ground that it was based on evidence seized in violation of the Fourth Amendment. <em>(T. L. O.) </em>v. <em>Piscataway Bd. of Ed., </em>No. C.2865-79 (Super. Ct. N. J., Ch. Div., Mar. 31, 1980). The Board of Education apparently did not appeal the decision of the Chancery Division.</p>
</footnote>
<footnote label="2">
<p id="b474-5"> State and federal courts considering these questions have struggled to accommodate the interests protected by the Fourth Amendment and the interest of the States in providing a safe environment conducive to education in the public schools. Some courts have resolved the tension between these interests by giving full force to one or the other side of the balance. Thus, in a number of cases courts have held that school officials conducting in-school searches of students are private parties acting <em>in loco parentis </em>and are therefore not subject to the constraints of the Fourth Amendment. See, <em>e. g., D. R. C. </em>v. <em>State, </em><span class="citation" data-id="5157665"><a href="/opinion/5327621/d-r-c-v-state/" aria-description="Citation for case: D. R. C. v. State">646 P. 2d 252</a></span> (Alaska App. 1982); <em>In re G., </em><span class="citation multiple-matches"><a href="/c/Cal.%20App.%203d/11/1193/">11 Cal. App. 3d 1193</a></span>, <span class="citation multiple-matches"><a href="/c/Cal.%20Rptr./90/361/">90 Cal. Rptr. 361</a></span> (1970); <em>In re Donaldson, </em><span class="citation" data-id="2205714"><a href="/opinion/2205714/mercer-v-donaldson/" aria-description="Citation for case: Mercer v. Donaldson">269 Cal. App. 2d 509</a></span>, <span class="citation" data-id="2205714"><a href="/opinion/2205714/mercer-v-donaldson/" aria-description="Citation for case: Mercer v. Donaldson">75 Cal. Rptr. 220</a></span> (1969); <em>R. C. M. </em>v. <em>State, </em><span class="citation" data-id="5060443"><a href="/opinion/5235277/rcm-v-state/" aria-description="Citation for case: R.C.M. v. State">660 S. W. 2d 552</a></span> (Tex. App. 1983); <em>Mercer </em>v. <em>State, </em><span class="citation" data-id="9653644"><a href="/opinion/1567651/mercer-v-state/" aria-description="Citation for case: Mercer v. State">450 S. W. 2d 715</a></span> (Tex. Civ. App. 1970). At least one court has held, on the other hand, that the Fourth Amendment applies in full to in-school searches by school officials and that a search conducted without probable cause is unreasonable, see <em>State </em>v. <em>Mora, </em><span class="citation" data-id="1739670"><a href="/opinion/1739670/state-v-mora/" aria-description="Citation for case: State v. Mora">307 So. 2d 317</a></span> (La.), vacated, <span class="citation multiple-matches"><a href="/c/U.%20S./423/809/">423 U. S. 809</a></span> (1975), on remand, <span class="citation" data-id="1950670"><a href="/opinion/1950670/state-v-mora/" aria-description="Citation for case: State v. Mora">330 So. 2d 900</a></span> (La. 1976); others have held or suggested that the probable-cause standard is applicable at least where the police are involved in a search, see <em>M. </em>v. <em>Board of Ed. Ball-Chatham Community Unit School Dist. No. 5, </em><span class="citation" data-id="1554742"><a href="/opinion/1554742/m-ex-rel-r-v-board-of-education-ball-chatham-community-unit-school/#292" aria-description="Citation for case: M. Ex Rel. R. v. Board of Education Ball-Chatham...">429 F. Supp. 288, 292</a></span> (SD Ill. 1977); <em>Picha </em>v. <em>Wielgos, </em><span class="citation" data-id="2308367"><a href="/opinion/2308367/picha-v-wielgos/#1219" aria-description="Citation for case: Picha v. Wielgos">410 F. Supp. 1214, 1219-1221</a></span> (ND Ill. 1976); <em>State </em>v. <em>Young, </em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/#498" aria-description="Citation for case: State v. Young">234 Ga. 488, 498</a></span>, <span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/#594" aria-description="Citation for case: State v. Young">216 S. E. 2d 586, 594</a></span> (1975); or where the search is highly intrusive, see <em>M. M. </em>v. <em>Anker, </em><span class="citation multiple-matches"><a href="/c/F.%202d/607/588/">607 F. 2d 588</a></span>, 589 (CA2 1979).</p>
<p id="b474-6">The majority of courts that have addressed the issue of the Fourth Amendment in the schools have, like the Supreme Court of New Jersey in this case, reached a middle position: the Fourth Amendment applies to searches conducted by school authorities, but the special needs of the school environment require assessment of the legality of such searches against a standard less exacting than that of probable cause. These courts have, by and large, upheld warrantless searches by school authorities provided that they are supported by a reasonable suspicion that the search will uncover evidence of an infraction of school disciplinary rules or a violation of the law. See, <em>e. g., Tarter </em>v. <em>Baybuck, </em>No. 83-3174 (CA6, Aug. 31, 1984); <em>Bilbrey </em>v. <em>Brown, </em><span class="citation multiple-matches"><a href="/c/F.%202d/738/1462/">738 F. 2d 1462</a></span> (CA91984); <em>Horton </em>v. <em>Goose Creek </em><page-number citation-index="1" label="333">*333</page-number><em>Independent School Dist., </em><span class="citation multiple-matches"><a href="/c/F.%202d/690/470/">690 F. 2d 470</a></span> (CA5 1982); <em>Bellnier </em>v. <em>Lund, </em><span class="citation" data-id="1463269"><a href="/opinion/1463269/bellnier-v-lund/" aria-description="Citation for case: Bellnier v. Lund">438 F. Supp. 47</a></span> (NDNY 1977); <em>M. </em>v. <em>Board of Ed. Ball-Chatham Community Unit School Dist. No. <span class="citation" data-id="1554742"><a href="/opinion/1554742/m-ex-rel-r-v-board-of-education-ball-chatham-community-unit-school/" aria-description="Citation for case: M. Ex Rel. R. v. Board of Education Ball-Chatham...">5, supra;</a></span> In re W., </em><span class="citation" data-id="2122374"><a href="/opinion/2122374/beckley-v-christopher-w/" aria-description="Citation for case: Beckley v. Christopher W.">29 Cal. App. 3d 777</a></span>, <span class="citation" data-id="2122374"><a href="/opinion/2122374/beckley-v-christopher-w/" aria-description="Citation for case: Beckley v. Christopher W.">105 Cal. Rptr. 775</a></span> (1973); <em>State </em>v. <em>Baccino, </em><span class="citation" data-id="1969621"><a href="/opinion/1969621/state-v-baccino/" aria-description="Citation for case: State v. Baccino">282 A. 2d 869</a></span> (Del. Super. 1971); <em>State </em>v. <em>D. T. W., </em><span class="citation" data-id="7523311"><a href="/opinion/7593883/state-v-dtw/" aria-description="Citation for case: State v. D.T.W.">425 So. 2d 1383</a></span> (Fla. App. 1983); <em>State </em>v. <em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/" aria-description="Citation for case: State v. Young">Young, supra;</a></span> In re J. </em>A., <span class="citation multiple-matches"><a href="/c/Ill.%20App.%203d/85/567/">85 Ill. App. 3d 567</a></span>, <span class="citation multiple-matches"><a href="/c/N.%20E.%202d/406/958/">406 N. E. 2d 958</a></span> (1980); <em>People </em>v. <em>Ward, </em><span class="citation" data-id="2183546"><a href="/opinion/2183546/people-v-ward/" aria-description="Citation for case: People v. Ward">62 Mich. App. 46</a></span>, <span class="citation" data-id="2183546"><a href="/opinion/2183546/people-v-ward/" aria-description="Citation for case: People v. Ward">233 N. W. 2d 180</a></span> (1975); <em>Doe </em>v. <em>State, </em>88 N. M. 347, <span class="citation" data-id="1304814"><a href="/opinion/1304814/doe-v-state/" aria-description="Citation for case: Doe v. State">540 P. 2d 827</a></span> (App. 1975); <em>People </em>v. <em>D., </em>34 N. Y. 2d 483, <span class="citation" data-id="5528818"><a href="/opinion/5680501/people-v-scott-d/" aria-description="Citation for case: People v. Scott D.">315 N. E. 2d 466</a></span> (1974); <em>State </em>v. <em>McKinnon, </em><span class="citation" data-id="9623173"><a href="/opinion/1406903/state-v-mckinnon/" aria-description="Citation for case: State v. McKinnon">88 Wash. 2d 75</a></span>, <span class="citation" data-id="9623173"><a href="/opinion/1406903/state-v-mckinnon/" aria-description="Citation for case: State v. McKinnon">558 P. 2d 781</a></span> (1977); <em>In re L. L., </em><span class="citation" data-id="1900299"><a href="/opinion/1900299/interest-of-l-l-v-circuit-court-of-washington-county/" aria-description="Citation for case: Interest of L. L. v. Circuit Court of Washington County">90 Wis. 2d 585</a></span>, <span class="citation" data-id="1900299"><a href="/opinion/1900299/interest-of-l-l-v-circuit-court-of-washington-county/" aria-description="Citation for case: Interest of L. L. v. Circuit Court of Washington County">280 N. W. 2d 343</a></span> (App. 1979).</p>
<p id="b475-8">Although few have considered the matter, courts have also split over whether the exclusionary rule is an appropriate remedy for Fourth Amendment violations committed by school authorities. The Georgia courts have held that although the Fourth Amendment applies to the schools, the exclusionary rule does not. See, <em>e. g., State </em>v. <em><span class="citation" data-id="9616519"><a href="/opinion/1391108/state-v-young/" aria-description="Citation for case: State v. Young">Young, supra;</a></span> State </em>v. <em>Lamb, </em><span class="citation" data-id="1292717"><a href="/opinion/1292717/state-v-lamb/" aria-description="Citation for case: State v. Lamb">137 Ga. App. 437</a></span>, <span class="citation" data-id="1292717"><a href="/opinion/1292717/state-v-lamb/" aria-description="Citation for case: State v. Lamb">224 S. E. 2d 51</a></span> (1976). Other jurisdictions have applied the rule to exclude the fruits of unlawful school searches from criminal trials and delinquency proceedings. See <em>State </em>v. <em>Mora, supra; People </em>v. <em>D., supra.</em></p>
</footnote>
<footnote label="3">
<p id="b475-9"> In holding that the search of T. L. O.’s purse did not violate the Fourth Amendment, we do not implicitly determine that the exclusionary rule applies to the fruits of unlawful searches conducted by school authorities. . The question whether evidence should be excluded from a criminal proceeding involves two discrete inquiries: whether the evidence was seized in violation of the Fourth Amendment, and whether the exclusionary rule is the appropriate remedy for the violation. Neither question'is logically antecedent to the other, for a negative answer to either question is sufficient to dispose of the case. Thus, our determination that the search at issue in this case did not violate the Fourth Amendment implies no particular resolution of the question of the applicability of the exclusionary rule.</p>
</footnote>
<footnote label="4">
<p id="b476-7"> Cf. <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977) (holding that the Eighth Amendment’s prohibition of cruel and unusual punishment applies only to <page-number citation-index="1" label="335">*335</page-number>punishments imposed after criminal convictions and hence does not apply to the punishment of schoolchildren by public school officials).</p>
</footnote>
<footnote label="5">
<p id="b479-8"> We do not address the question, not presented by this case, whether a schoolchild has a legitimate expectation of privacy in lockers, desks, or other school property provided for the storage of school supplies. Nor do we express any opinion on the standards (if any) governing searches of such areas by school officials or by other public authorities acting at the request of school officials. Compare <em>Zamora </em>v. <em>Pomeroy, </em><span class="citation multiple-matches"><a href="/c/F.%202d/639/662/">639 F. 2d 662</a></span>, 670 (CA10 1981) (“Inasmuch as the school had assumed joint control of the locker it cannot be successfully maintained that the school did not have a right to inspect it”), and <em>People </em>v. <em>Overton, </em>24 N. Y. 2d 522, <span class="citation" data-id="5524876"><a href="/opinion/5677061/people-v-overton/" aria-description="Citation for case: People v. Overton">249 N. E. 2d 366</a></span> (1969) (school administrators have power to consent to search of a <page-number citation-index="1" label="338">*338</page-number>student’s locker), with <em>State </em>v. <em>Engerud, </em>94 N. J. 331, 348, <span class="citation" data-id="7305116"><a href="/opinion/7386217/state-v-engerud/#943" aria-description="Citation for case: State v. Engerud">463 A. 2d 934, 943</a></span> (1983) (“We are satisfied that in the context of this case the student had an expectation of privacy in the contents of his locker. . . . For the four years of high school, the school locker is a home away from home. In it the student stores the kind of personal ‘effects’ protected by the Fourth Amendment”).</p>
</footnote>
<footnote label="6">
<p id="b483-6"> See eases cited in n. 2, <em>supra.</em></p>
</footnote>
<footnote label="7">
<p id="b483-7"> We here consider only searches carried out by school authorities acting alone and on their own authority. This case does not present the question of the appropriate standard for assessing the legality of searches conducted by school officials in conjunction with or at the behest of law enforcement agencies, and we express no opinion on that question. Cf. <em>Picha </em>v. <em>Wielgos, </em><span class="citation" data-id="2308367"><a href="/opinion/2308367/picha-v-wielgos/#1219" aria-description="Citation for case: Picha v. Wielgos">410 F. Supp. 1214, 1219-1221</a></span> (ND Ill. 1976) (holding probable-cause standard applicable to searches involving the police).</p>
</footnote>
<footnote label="8">
<p id="b484-6"> We do not decide whether individualized suspicion is an essential element of the reasonableness standard we adopt for searches by school authorities. In other contexts, however, we have held that although “some quantum of individualized suspicion is usually a prerequisite to a constitutional search or seizure[,]. . . the Fourth Amendment imposes no irreducible requirement of such suspicion.” <em>United States </em>v. <em>Martinez-</em>Fuerte, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 560-561</a></span> (1976). See also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). Exceptions to the requirement of individualized suspicion are generally appropriate only where the privacy interests implicated by a search are minimal and where “other safeguards” are available “to assure that the individual’s reasonable expectation of privacy is not ‘subject to the discretion of the official in the field.’” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979) (citation omitted). Because the search of T. L. O.’s purse was based upon an individualized suspicion that she had violated school rules, see <em>infra, </em>at 343-347, we need not consider the circumstances that might justify school authorities in conducting searches unsupported by individualized suspicion.</p>
</footnote>
<footnote label="9">
<p id="b484-7"> Our reference to the nature of the infraction is not intended as an endorsement of Justice Stevens’ suggestion that some rules regarding student conduct are by nature too “trivial” to justify a search based upon reasonable suspicion. See <em>post, </em>at 377-382. We are unwilling to adopt a standard under which the legality of a search is dependent upon a judge’s evaluation of the relative importance of various school rules. The maintenance of discipline in the schools requires not only that students be restrained from assaulting one another, abusing drugs and alcohol, and committing other crimes, but also that students conform themselves to the standards of conduct prescribed by school authorities. We have “repeatedly emphasized the need for affirming the comprehensive authority of the States and of school officials, consistent with fundamental constitutional safeguards, to prescribe and control conduct in the schools.” <em>Tinker </em>v. <em>Des Moines Independent Community School District, </em><span class="citation" data-id="9423907"><a href="/opinion/107841/tinker-v-des-moines-independent-community-school-district/#507" aria-description="Citation for case: Tinker v. Des Moines Independent Community School District">393 U. S. 503, 507</a></span> <page-number citation-index="1" label="343">*343</page-number>(1969). The promulgation of a rule forbidding specified conduct presumably reflects a judgment on the part of school officials that such conduct is destructive of school order or of a proper educational environment. Absent any suggestion that the rule violates some substantive constitutional guarantee, the courts should, as a general matter, defer to that judgment and refrain from attempting to distinguish between rules that are important to the preservation of order in the schools and rules that are not.</p>
</footnote>
<footnote label="10">
<p id="b485-9"> Of course, New Jersey may insist on a more demanding standard under its own Constitution or statutes. In that case, its courts would not purport to be applying the Fourth Amendment when they invalidate a search.</p>
</footnote>
<footnote label="11">
<p id="b486-6"> Justice Stevens interprets these statements as a holding that enforcement of the school’s smoking regulations was not sufficiently related to the goal of maintaining discipline or order in the school to justify a search under the standard adopted by the New Jersey court. See <em>post, </em>at 382-384. We do not agree that this is an accurate characterization of the New Jersey Supreme Court’s opinion. The New Jersey court did not hold that the school’s smoking rules were unrelated to the goal of maintaining discipline or order, nor did it suggest that a search that would produce evidence bearing directly on an accusation that a student had violated the smoking rules would be impermissible under the court’s reasonable-suspicion standard; rather, the court concluded that any evidence a search of T. L. O.’s purse was likely to produce would not have a sufficiently direct bearing on the infraction to justify a search — a conclusion with which we cannot agree for the reasons set forth <em>infra, </em>at 345. Justice Stevens’ suggestion that the New Jersey Supreme Court’s decision rested on the perceived triviality of the smoking infraction appears to be a reflection of his own views rather than those of the New Jersey court.</p>
</footnote>
<footnote label="12">
<p id="b488-5"> T. L. O. contends that even if it was reasonable for Mr. Choplick to open her purse to look for cigarettes, it was not reasonable for him to reach in and take the cigarettes out of her purse once he found them. Had he not removed the cigarettes from the purse, she asserts, he would not have observed the rolling papers that suggested the presence of marihuana, and the search for marihuana could not have taken place. T. L. O.’s argument is based on the fact that the cigarettes were not “contraband,” as no school rule forbade her to have them. Thus, according to T. L. 0., the cigarettes were not subject to seizure or confiscation by school authorities, and Mr. Choplick was not entitled to take them out of T. L. O.’s purse regardless of whether he was entitled to peer into the purse to see if they were there. Such hairsplitting argumentation has no place in an inquiry addressed to the issue of reasonableness. If Mr. Choplick could permissibly search T. L. O.’s purse for cigarettes, it hardly seems reasonable to suggest that his natural reaction to finding them — picking them up — could <page-number citation-index="1" label="347">*347</page-number>be a constitutional violation. We find that neither in opening the purse nor in reaching into it to remove the cigarettes did Mr. Choplick violate the Fourth Amendment.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/O'Connor v. Ortega.md  (`case`, 5 assertions)

### content_page

```
---
title: "O'Connor v. Ortega"
type: case
citation: "480 U.S. 709 (1987)"
parallel_cite: "107 S. Ct. 1492; 94 L. Ed. 2d 714; 1 I.E.R. Cas. (BNA) 1617; 55 U.S.L.W. 4405; 42 Empl. Prac. Dec. (CCH) 36,891"
neutral_cite: 1987 U.S. LEXIS 1507
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-03-31
docket: 85-530
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "O'Connor v. Ortega"
  varies_by_point: false
  scope_note: "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111851/oconnor-v-ortega/"
  cluster_id: 111851
  opinion_id: 9430897
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Anchor (workplace REP)"
related: ["[[City of Ontario v. Quon]]"]
aliases: []
tags: ["case", "fourth-amendment", "special-needs", "workplace", "public-employee", "reasonable-expectation-of-privacy"]
holding: "Public employees may have a reasonable expectation of privacy in their offices, desks, and files, subject to the operational realities of the workplace; but a public employer's work-related search — whether to retrieve work materials or to investigate work-related misconduct — is judged by reasonableness under all the circumstances, without a warrant or probable cause."
lake:
  record_id: "O'Connor v. Ortega"
  status: under_review
  projected_at: 2026-07-06
---

# O'Connor v. Ortega

*480 U.S. 709 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Dr. Ortega, a physician and administrator at a California state hospital, was placed on administrative leave while officials investigated suspected workplace misconduct (concerning resident-training and the acquisition of a computer). During the investigation, hospital officials entered and searched his office, desk, and file cabinets and seized personal items later used against him in administrative proceedings. Ortega sued under § 1983, claiming the search violated the Fourth Amendment.

## Issue
Whether a public employee has a Fourth Amendment expectation of privacy in his office, desk, and files, and what standard governs a search of those areas by his government employer for work-related purposes.

## Rule
Public employees are not stripped of Fourth Amendment protection at work, though their privacy may be reduced by workplace realities. "Individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer. The operational realities of the workplace, however, may make *some* employees' expectations of privacy unreasonable when an intrusion is by a supervisor rather than a law enforcement official." — 480 U.S. at 717. ^pin-717

Work-related employer searches are judged by reasonableness, not warrant or probable cause: "We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable." — *Id.* at 725–726. ^pin-725

## Application
Because Dr. Ortega did not share his office and kept personal materials in his desk and files, he had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] there. But the warrant and probable-cause requirements would be unworkable for the routine, work-related searches public employers must make, so the intrusion was instead measured by reasonableness — assessed at both inception and scope. The Court did not itself resolve whether this particular search was reasonable; it [[Reading and Citing Cases#on-remand|remanded]] for that fact-bound determination.

## Conclusion
Ortega had a Fourth Amendment privacy interest in his office, but the employer's work-related search is governed by reasonableness rather than warrant/probable cause; the case was [[Reading and Citing Cases#on-remand|remanded]] to apply that standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Scalia, J., concurring in the judgment, provided the controlling fifth vote for the reasonableness standard).
- No negative treatment. *O'Connor* is the anchor for public-employee workplace privacy; its reasonableness framework was reaffirmed and applied to an employer's review of an employee's electronic messages in [[City of Ontario v. Quon]] (2010).

## Appears on
- [[Special Needs and Administrative Searches]] — *Anchor (workplace REP)*

## Sources
- *O'Connor v. Ortega*, 480 U.S. 709 (1987) — https://www.courtlistener.com/opinion/111851/oconnor-v-ortega/ — pinpoints: 717, 725–726.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f0421ce033a8c70", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "480 U.S. 709 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 1507", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1492; 94 L. Ed. 2d 714; 1 I.E.R. Cas. (BNA) 1617; 55 U.S.L.W. 4405; 42 Empl. Prac. Dec. (CCH) 36,891", "title": "O'Connor v. Ortega", "year": "1987"}}
{"assertion_id": "1ef5628494c1f984", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Public employees may have a reasonable expectation of privacy in their offices, desks, and files, subject to the operational realities of the workplace; but a public employer's work-related search — whether to retrieve work materials or to investigate work-related misconduct — is judged by reasonableness under all the circumstances, without a warrant or probable cause.", "title": "O'Connor v. Ortega"}}
{"assertion_id": "6e6872a0dea92d35", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Anchor (workplace REP)", "title": "O'Connor v. Ortega"}}
{"assertion_id": "b7d4c4f1f8439911", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "O'Connor v. Ortega"}}
{"assertion_id": "c28ae27b76fb40af", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-03-31", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "O'Connor v. Ortega", "field_i_validity": "good_law", "scope_note": "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010).", "title": "O'Connor v. Ortega", "varies_by_point": "false"}}
```

### lake record — O'Connor v. Ortega

```json
{
  "schema_version": "s2.v1",
  "record_id": "O'Connor v. Ortega",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "O'CONNOR v. Ortega",
    "case_name_short": "O'Connor",
    "case_name_full": "O\u2019CONNOR Et Al. v. ORTEGA",
    "input_case_name": "O'Connor v. Ortega",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-03-31",
    "year": 1987,
    "docket": "85-530",
    "cluster_id": 111851,
    "lead_opinion_id": 9430897,
    "sibling_ids": [
      111851,
      9430897,
      9430898,
      9430899
    ],
    "absolute_url": "/opinion/111851/oconnor-v-ortega/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 709",
      "volume": "480",
      "reporter": "U.S.",
      "page": "709",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1492",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 714",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 I.E.R. Cas. (BNA) 1617",
        "volume": "1",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1617",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4405",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4405",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "42 Empl. Prac. Dec. (CCH) 36,891",
        "volume": "42",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "36,891",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1507",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1507",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 709",
        "volume": "480",
        "reporter": "U.S.",
        "page": "709",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1492",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 714",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "714",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1507",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1507",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1 I.E.R. Cas. (BNA) 1617",
        "volume": "1",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "1617",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4405",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4405",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "42 Empl. Prac. Dec. (CCH) 36,891",
        "volume": "42",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "36,891",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 709",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 709",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-717",
      "page": null,
      "quote": "--- # O'Connor v. Ortega *480 U.S. 709 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Dr. Ortega, a physician and administrator at a California state hospital, was placed on administrative leave while officials investigated suspected workplace misconduct (concerning resident-training and the acquisition of a computer). During the investigation, hospital officials entered and searched his office, desk, and file cabinets and seized personal items later used against him in administrative proceedings. Ortega sued under \u00a7 1983, claiming the search violated the Fourth Amendment. ## Issue Whether a public employee has a Fourth Amendment expectation of privacy in his office, desk, and files, and what standard governs a search of those areas by his government employer for work-related purposes. ## Rule Public employees are not stripped of Fourth Amendment protection at work, though their privacy may be reduced by workplace realities.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-725",
      "page": null,
      "quote": "We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "O'Connor v. Ortega",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (O'Connor, J.); Scalia concurred in the judgment, supplying a fifth vote for the reasonableness standard, which is controlling. Good law; reaffirmed and applied in City of Ontario v. Quon (2010).",
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
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hitselberger",
          "cluster_id": 2659423,
          "cite": [
            "991 F. Supp. 2d 108",
            "93 Fed. R. Serv. 1076",
            "2014 WL 842465",
            "2014 U.S. Dist. LEXIS 27792"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Southerland v. City of New York",
          "cluster_id": 8441115,
          "cite": [
            "667 F.3d 87",
            "2012 WL 310836",
            "2011 U.S. App. LEXIS 26144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jessica Beechum v. State",
          "cluster_id": 3129045,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 1978636,
          "cite": [
            "2008 VT 53",
            "955 A.2d 1144",
            "184 Vt. 23",
            "2008 Vt. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Brian Ziegler",
          "cluster_id": 796647,
          "cite": [
            "474 F.3d 1184",
            "2007 U.S. App. LEXIS 1953",
            "2007 WL 222167"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane1_negative"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Francis v. Giacomelli",
          "cluster_id": 1030886,
          "cite": [
            "588 F.3d 186",
            "30 I.E.R. Cas. (BNA) 1",
            "2009 U.S. App. LEXIS 26188",
            "107 Fair Empl. Prac. Cas. (BNA) 1605",
            "2009 WL 4348830"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Engquist v. Oregon Department of Agriculture",
          "cluster_id": 145801,
          "cite": [
            "170 L. Ed. 2d 975",
            "128 S. Ct. 2146",
            "553 U.S. 591",
            "2008 U.S. LEXIS 4705",
            "27 I.E.R. Cas. (BNA) 1121",
            "76 U.S.L.W. 4367",
            "21 Fla. L. Weekly Fed. S 302",
            "91 Empl. Prac. Dec. (CCH) 43,213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rutan v. Republican Party of Illinois",
          "cluster_id": 112472,
          "cite": [
            "111 L. Ed. 2d 52",
            "110 S. Ct. 2729",
            "497 U.S. 62",
            "1990 U.S. LEXIS 3298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
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
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Greenwood",
          "cluster_id": 112067,
          "cite": [
            "100 L. Ed. 2d 30",
            "108 S. Ct. 1625",
            "486 U.S. 35",
            "1988 U.S. LEXIS 2279",
            "56 U.S.L.W. 4409"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jessie Walker v. Thomas E. Darby, Hugh L. Robinson, Jr., and Kenneth Day",
          "cluster_id": 546977,
          "cite": [
            "911 F.2d 1573",
            "5 I.E.R. Cas. (BNA) 1342",
            "1990 U.S. App. LEXIS 16510",
            "1990 WL 126642"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dubbs Ex Rel. Dubbs v. Head Start, Inc.",
          "cluster_id": 163684,
          "cite": [
            "336 F.3d 1194",
            "2003 U.S. App. LEXIS 14578",
            "2003 WL 21690533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parviz Karim-Panahi v. Los Angeles Police Department",
          "cluster_id": 501771,
          "cite": [
            "839 F.2d 621",
            "10 Fed. R. Serv. 3d 791",
            "1988 U.S. App. LEXIS 1814",
            "46 Fair Empl. Prac. Cas. (BNA) 287"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ferguson v. City of Charleston",
          "cluster_id": 118414,
          "cite": [
            "149 L. Ed. 2d 205",
            "121 S. Ct. 1281",
            "532 U.S. 67",
            "2001 U.S. LEXIS 2460",
            "2001 Daily Journal DAR 2839",
            "2001 Colo. J. C.A.R. 1427",
            "14 Fla. L. Weekly Fed. S 152",
            "69 U.S.L.W. 4184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tenenbaum v. Williams",
          "cluster_id": 7079141,
          "cite": [
            "193 F.3d 581",
            "1999 WL 822538"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Borough of Duryea v. Guarnieri",
          "cluster_id": 219105,
          "cite": [
            "180 L. Ed. 2d 408",
            "131 S. Ct. 2488",
            "564 U.S. 379",
            "2011 U.S. LEXIS 4564"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brian Sheppard v. Leon Beerman, as an Individual and in His Official Capacity as Justice of the Supreme Court of the State of New York",
          "cluster_id": 664638,
          "cite": [
            "18 F.3d 147",
            "1994 U.S. App. LEXIS 3985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James G. Jackson v. City of Columbus, Gregory Lashutka, Thomas W. Rice, Sr.",
          "cluster_id": 766509,
          "cite": [
            "194 F.3d 737"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "O'Connor v. Ortega:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTAyNjM2ODAwMDAwJnM9Nzg4NjI0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTAmcz01NjA3OTU2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
        "reviewed": 8,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 8,
        "triage_read": 0,
        "triage_snippet_classified": 8
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111851 OR 9430897 OR 9430898 OR 9430899)",
    "indexed_citing_opinions": 694,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111851,
        "count": 635,
        "count_source": "search"
      },
      {
        "opinion_id": 9430897,
        "count": 73,
        "count_source": "search"
      },
      {
        "opinion_id": 9430898,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430899,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1072,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/o-connor-v-ortega.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NjkwMDYmcz01Mjk5Mzc4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111851+OR+9430897+OR+9430898+OR+9430899%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111851,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 106168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 227140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 268915,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 310289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 329742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 346754,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 358050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 359042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 431839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 437463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 453433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 1631759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 2005190,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111851,
        "cited_id": 2263945,
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
    "date_created": "2026-07-05T16:00:58Z",
    "date_modified": "2026-07-06T08:32:27Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:05:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:01:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — O'Connor v. Ortega

```
<opinion type="majority">
<author id="b757-8">Justice O’Connor</author>
<p id="Ad0">announced the judgment of the Court and delivered an opinion in which The Chief Justice, Justice White, and Justice Powell join.</p>
<p id="b757-9">This suit under <span class="citation no-link">42 U. S. C. § 1983</span> presents two issues concerning the Fourth Amendment rights of public employees. First, we must determine whether the respondent, a public <page-number citation-index="1" label="712">*712</page-number>employee, had a reasonable expectation of privacy in his office, desk, and file cabinets at his place of work. Second, we must address the appropriate Fourth Amendment standard for a search conducted by a public employer in areas in which a public employee is found to have a reasonable expectation of privacy.</p>
<p id="b758-5">I</p>
<p id="b758-6">Dr. Magno Ortega, a physician and psychiatrist, held the position of Chief of Professional Education at Napa State Hospital (Hospital) for 17 years, until his dismissal from that position in 1981. As Chief of Professional Education, Dr.. Ortega had primary responsibility for training young physicians in psychiatric residency programs.</p>
<p id="b758-7">In July 1981, Hospital officials, including Dr. Dennis O’Connor, the Executive Director of the Hospital, became concerned about possible improprieties in Dr. Ortega’s management of the residency program. In particular, the Hospital officials were concerned with Dr. Ortega’s acquisition of an Apple II computer for use in the residency program. The officials thought that Dr. Ortega may have misled Dr. O’Con-nor into believing that the computer had been donated, when in fact the computer had been financed by the possibly coerced contributions of residents. Additionally, the Hospital officials were concerned with charges that Dr. Ortega had sexually harassed two female Hospital employees, and had taken inappropriate disciplinary action against a resident.</p>
<p id="b758-8">On July 30, 1981, Dr. O’Connor requested that Dr. Ortega take paid administrative leave during an investigation of these charges. At Dr. Ortega’s request, Dr. O’Connor agreed to allow Dr. Ortega to take two weeks’ vacation instead of administrative leave. Dr. Ortega, however, was requested to stay off Hospital grounds for the duration of the investigation. On August 14, 1981, Dr. O’Connor informed Dr. Ortega that the investigation had not yet been completed, and that he was being placed on paid administrative leave. Dr. Ortega remained on administrative leave until <page-number citation-index="1" label="713">*713</page-number>the Hospital terminated his employment on September 22, 1981.</p>
<p id="b759-5">Dr. O’Connor selected several Hospital personnel to conduct the investigation, including an accountant, a physician, and a Hospital security officer. Richard Friday, the Hospital Administrator, led this “investigative team.” At some point during the investigation, Mr. Friday made the decision to enter Dr. Ortega’s office. The specific reason for the entry into Dr. Ortega’s office is unclear from the record. The petitioners claim that the search was conducted to secure state property. Initially, petitioners contended that such a search was pursuant to a Hospital policy of conducting a routine inventory of state property in the office of a terminated employee. At the time of the search, however, the Hospital had not yet terminated Dr. Ortega’s employment; Dr. Ortega was still on administrative leave. Apparently, there was no policy of inventorying the offices of those on administrative leave. Before the search had been initiated, however, petitioners had become aware that Dr. Ortega had taken the computer to his home. Dr. Ortega contends that the purpose of the search was to secure evidence for use against him in administrative disciplinary proceedings.</p>
<p id="b759-6">The resulting search of Dr. Ortega’s office was quite thorough. The investigators entered the office a number of times and seized several items from Dr. Ortega’s desk and file cabinets, including a Valentine’s Day card, a photograph, and a book of poetry all sent to Dr. Ortega by a former resident physician. These items were later used in a proceeding before a hearing officer of the California State Personnel Board to impeach the credibility of the former resident, who testified on Dr. Ortega’s behalf. The investigators also seized billing documentation of one of Dr. Ortega’s private patients under the California Medicaid program. The investigators did not otherwise separate Dr. Ortega’s property from state property because, as one investigator testified, “[tjrying to sort State from non-State, it was too much to do, so I gave it <page-number citation-index="1" label="714">*714</page-number>up and boxed it up.” App. 62. Thus, no formal inventory of the property in the office was ever made. Instead, all the papers in Dr. Ortega’s office were merely placed in boxes, and put in storage for Dr. Ortega to retrieve.</p>
<p id="b760-5">Dr. Ortega commenced this action against petitioners in Federal District Court under <span class="citation no-link">42 U. S. C. § 1988</span>, alleging that the search of his office violated the Fourth Amendment. On cross-motions for summary judgment, the District Court granted petitioners’ motion for summary judgment. The District Court, relying on <em>Chenkin </em>v. <em>Bellevue Hospital Center, New York City Health &amp; Hospitals Corp., </em><span class="citation" data-id="2263945"><a href="/opinion/2263945/chenkin-v-bellevue-hosp-ctr-nyc-etc/" aria-description="Citation for case: Chenkin v. BELLEVUE HOSP. CTR., NYC, ETC.">479 F. Supp. 207</a></span> (SDNY 1979), concluded that the search was proper because there was a need to secure state property in the office. The Court of Appeals for the Ninth Circuit affirmed in part and reversed in part, <span class="citation multiple-matches"><a href="/c/F.%202d/764/703/">764 F. 2d 703</a></span> (1985), concluding that Dr. Ortega had a reasonable expectation of privacy in his office. While the Hospital had a procedure for office inventories, these inventories were reserved for employees who were departing or were terminated. The Court of Appeals also concluded — albeit without explanation — that the search violated the Fourth Amendment. The Court of Appeals held that the record justified a grant of partial summary judgment for Dr. Ortega on the issue of liability for an unlawful search, and it remanded the case to the District Court for a determination of damages.</p>
<p id="b760-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./474/1018/">474 U. S. 1018</a></span> (1985), and now reverse and remand.</p>
<p id="b760-8">h — I l-H</p>
<p id="b760-7">The strictures of the Fourth Amendment, applied to the States through the Fourteenth Amendment, have been applied to the conduct of governmental officials in various civil activities. <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334-335</a></span> (1985). Thus, we have held in the past that the Fourth Amendment governs the conduct of school officials, see <em>ibid., </em>building inspectors, see <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967), and Occupational Safety and Health <page-number citation-index="1" label="715">*715</page-number>Act inspectors, see <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978). As we observed in <em>T. L. 0., </em>“[b]ecause the individual’s interest in privacy and personal security ‘suffers whether the government’s motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards,’... it would be ‘anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.’” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 335</a></span> (quoting <em>Marshall </em>v. <em>Barlow’s, <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">Inc., supra,</a></span> </em>at 312-313 and <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 530</a></span>). Searches and seizures by government employers or supervisors of the private property of their employees, therefore, are subject to the restraints of the Fourth Amendment.</p>
<p id="b761-5">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . .” Our cases establish that Dr. Ortega’s Fourth Amendment rights are implicated only if the conduct of the Hospital officials at issue in this case infringed “an expectation of privacy that society is prepared to consider reasonable.” <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). We have no talisman that determines in all cases those privacy expectations that society is prepared to accept as reasonable. Instead, “the Court has given weight to such factors as the intention of the Framers of the Fourth Amendment, the uses to which the individual has put a location, and our societal understanding that certain areas deserve the most scrupulous protection from government invasion.” <em>Oliver </em>v. <em>United States, </em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178</a></span> (1984) (citations omitted).</p>
<p id="b761-6">Because the reasonableness of an expectation of privacy, as well as the appropriate standard for a search, is understood to differ according to context, it is essential first to delineate the boundaries of the workplace context. The workplace includes those areas and items that are related to work and are generally within the employer’s control. At a hospital, for <page-number citation-index="1" label="716">*716</page-number>example, the hallways, cafeteria, offices, desks, and file cabinets, among other areas, are all part of the workplace. These areas remain part of the workplace context even if the employee has placed personal items in them, such as a photograph placed in a desk or a letter posted on an employee bulletin board.</p>
<p id="b762-5">Not everything that passes through the confines of the business address can be considered part of the workplace context, however. An employee may bring closed luggage to the office prior to leaving on a trip, or a handbag or briefcase each workday. While whatever expectation of privacy the employee has in the existence and the outward appearance of the luggage is affected by its presence in the workplace, the employee’s expectation of privacy in the <em>contents </em>of the luggage is not affected in the same way. The appropriate standard for a workplace search does not necessarily apply to a piece of closed personal luggage, a handbag, or a briefcase that happens to be within the employer’s business address.</p>
<p id="b762-6">Within the workplace context, this Court has recognized that employees may have a reasonable expectation of privacy against intrusions by police. See <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968). As with the expectation of privacy in one’s home, such an expectation in one’s place of work is “based upon societal expectations that have deep roots in the history of the Amendment.” <em>Oliver </em>v. <em>United States, supra, </em>at 178, n. 8. Thus, in <em>Mancusi </em>v. <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">DeForte, supra,</a></span> </em>the Court held that a union employee who shared an office with other union employees had a privacy interest in the office sufficient to challenge successfully the warrantless search of that office:</p>
<blockquote id="b762-7">“It has long been settled that one has standing to object to a search of his office, as well as of his home. . . . [I]t seems clear that if DeForte had occupied a ‘private’ office in the union headquarters, and union records had been seized from a desk or a filing cabinet in that office, he would have had standing. ... In such a ‘private’ of<page-number citation-index="1" label="717">*717</page-number>fice, DeForte would have been entitled to expect that he would not be disturbed except by personal or business invitees, and that records would not be taken except with his permission or that of his union superiors.” <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 369</a></span>.</blockquote>
<p id="b763-5">Given the societal expectations of privacy in one’s place of work expressed in both <em><span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/" aria-description="Citation for case: Oliver v. United States">Oliver</a></span> </em>and <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span>, </em>we reject the contention made by the Solicitor General and petitioners that public employees can never have a reasonable expectation of privacy in their place of work. Individuals do not lose Fourth Amendment rights merely because they work for the government instead of a private employer. The operational realities of the workplace, however, may make <em>some </em>employees’ expectations of privacy unreasonable when an intrusion is by a supervisor rather than a law enforcement official. Public employees’ expectations of privacy in their offices, desks, and file cabinets, like similar expectations of employees in the private sector, may be reduced by virtue of actual office practices and procedures, or by legitimate regulation. Indeed, in <em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span> </em>itself, the Court suggested that the union employee did not have a reasonable expectation of privacy against his union supervisors. <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 369</a></span>. The employee’s expectation of privacy must be assessed in the context of the employment relation. An office is seldom a private enclave free from entry by supervisors, other employees, and business and personal invitees. Instead, in many cases offices are continually entered by fellow employees and other visitors during the workday for conferences, consultations, and other work-related visits. Simply put, it is the nature of government offices that others — such as fellow employees, supervisors, consensual visitors, and the general public — may have frequent access to an individual’s office. We agree with Justice Scalia that “[cjonstitutional protection against <em>unreasonable </em>searches by the government does not disappear merely because the government has the right to make reasonable. intrusions in its capacity as em<page-number citation-index="1" label="718">*718</page-number>ployer,” <em>post, </em>at 731, but some government offices may be so open to fellow employees or the public that no expectation of privacy is reasonable. Cf. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967) (“What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection”). Given the great variety of work environments in the public sector, the question whether an employee has a reasonable expectation of privacy must be addressed on a case-by-case basis.</p>
<p id="b764-5">The Court of Appeals concluded that Dr. Ortega had a reasonable expectation of privacy in his office, and five Members of this Court agree with that determination. See <em>post, </em>at 731-732 (Scalia, J., concurring in judgment); <em>post, </em>at 732 (Blackmun, J., joined by Brennan, Marshall, and Stevens, JJ., dissenting). Because the record does not reveal the extent to which Hospital officials may have had work-related reasons to enter Dr. Ortega’s office, we think the Court of Appeals should have remanded the matter to the District Court for its further determination. But regardless of any legitimate right of access the Hospital staff may have had to the office as such, we recognize that the undisputed evidence suggests that Dr. Ortega had a reasonable expectation of privacy in his desk and file cabinets. The undisputed evidence discloses that Dr. Ortega did not share his desk or file cabinets with any other employees. Dr. Ortega had occupied the office for 17 years and he kept materials in his office, which included personal correspondence, medical files, correspondence from private patients unconnected to the Hospital, personal financial records, teaching aids and notes, and personal gifts and mementos. App. 14. The files on physicians in residency training were kept outside Dr. Ortega’s office. <em>Id., </em>at 21. Indeed, the only items found by the investigators were apparently personal items because, with the exception of the items seized for use in the administrative hearings, all the papers and effects found in the office were simply placed in boxes and made available to Dr. Ortega. <page-number citation-index="1" label="719">*719</page-number><em>Id., </em>at 58, 62. Finally, we note that there was no evidence that the Hospital had established any reasonable regulation or policy discouraging employees such as Dr. Ortega from storing personal papers and effects in their desks or file cabinets, id., at 44, although the absence of such a policy does not create an expectation of privacy where it would not otherwise exist.</p>
<p id="b765-5">On the basis of this undisputed evidence, we accept the conclusion of the Court of Appeals that Dr. Ortega had a reasonable expectation of privacy at least in his desk and file cabinets. See <em>Gillard </em>v. <em>Schmidt, </em><span class="citation" data-id="358050"><a href="/opinion/358050/francis-d-gillard-v-harold-f-schmidt/#829" aria-description="Citation for case: Francis D. Gillard v. Harold F. Schmidt">579 F. 2d 825, 829</a></span> (CA3 1978); <em>United States </em>v. <em>Speights, </em><span class="citation" data-id="346754"><a href="/opinion/346754/united-states-v-ronald-miller-speights/" aria-description="Citation for case: United States v. Ronald Miller Speights">557 F. 2d 362</a></span> (CA3-4977); <em>United States </em>v. <em>Blok, </em>88 U. S. App. D. C. 326, <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/" aria-description="Citation for case: United States v. Blok">188 F. 2d 1019</a></span> (1951).</p>
<p id="b765-6">Ill</p>
<p id="b765-7">Having determined that Dr. Ortega had a reasonable expectation of privacy in his office, the Court of Appeals simply concluded without discussion that the “search . . . was not a reasonable search under the fourth amendment.” 764 F. 2d, at 707. But as we have stated in <em>T. L. 0., </em>“[t]o hold that the Fourth Amendment applies to searches conducted by [public employers] is only to begin the inquiry into the standards governing such searches. . . . [W]hat is reasonable depends on the context within which a search takes place.” <em>New Jersey </em>v. <em>T. L. 0., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#337" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 337</a></span>. Thus, we must determine the appropriate standard of reasonableness applicable to the search. A determination of the standard of reasonableness applicable to a particular class of searches requires “balancing] the nature and quality of the intrusion on the individual’s Fourth Amendment interests against the importance of the governmental interests alleged to justify the intrusion.” <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 536-537</a></span>. In the case of searches conducted by a public employer, we must balance the invasion of the employees’ legitimate expectations of pri<page-number citation-index="1" label="720">*720</page-number>vacy against the government’s need for supervision, control, and the efficient operation of the workplace.</p>
<p id="b766-5">“[I]t is settled . . . that ‘except in certain carefully defined classes of cases, a search of private property without proper consent is “unreasonable” unless it has been authorized by a valid search warrant.’” <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 370</a></span> (quoting <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 528-529</a></span>). There are some circumstances, however, in which we have recognized that a warrant requirement is unsuitable. In particular, a warrant requirement is not appropriate when “the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search.” <em>Camara </em>v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#533" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>Municipal Court, supra, </em>at 533</a></span>. Or, as Justice Blackmun stated in <em>T. L. 0., </em>“[o]nly in those exceptional circumstances in which special needs, beyond the normal need for law enforcement, make the warrant and probable-cause requirement impracticable.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 351</a></span> (concurring in judgment). In <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978), for example, the Court explored the burdens a warrant requirement would impose on the Occupational Safety and Health Act regulatory scheme, and held that the warrant requirement was appropriate only after concluding that warrants would not “impose serious burdens on the inspection system or the courts, [would not] prevent inspections necessary to enforce the statute, or [would not] make them less effective.” <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#316" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 316</a></span>. In <em>New Jersey </em>v. <em>T. L. O., supra, </em>we concluded that the warrant requirement was not suitable to the school environment, because such a requirement would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools.</p>
<p id="b766-6">There is surprisingly little case law on the appropriate Fourth Amendment standard of reasonableness for a public employer’s work-related search of its employee’s offices, desks, or file cabinets. Generally, however, the lower courts have held that any “work-related” search by an em<page-number citation-index="1" label="721">*721</page-number>ployer satisfies the Fourth Amendment reasonableness requirement. See <em>United States </em>v. <em>Nasser6, </em><span class="citation" data-id="9459389"><a href="/opinion/310289/united-states-v-arthur-nasser-united-states-of-america-v-richard-w/#1123" aria-description="Citation for case: United States v. Arthur Nasser, United States of America...">476 F. 2d 1111, 1123</a></span> (CA7 1973) (“work-related” searches and seizures are reasonable under the Fourth Amendment); <em>United States </em>v. <em>Collins, </em><span class="citation" data-id="268915"><a href="/opinion/268915/united-states-v-madell-collins/#868" aria-description="Citation for case: United States v. Madell Collins">349 F. 2d 863, 868</a></span> (CA2 1965) (upholding search and seizure because conducted pursuant to “the power of the Government as defendant’s employer, to supervise and investigate the performance of his duties as a Customs employee”). Others have suggested the use of a standard other than probable cause. See <em>United States </em>v. <em>Bunkers, </em><span class="citation" data-id="329742"><a href="/opinion/329742/united-states-v-jennieve-rose-bunkers/" aria-description="Citation for case: United States v. Jennieve Rose Bunkers">521 F. 2d 1217</a></span> (CA9 1975) (work-related search of a locker tested under “reasonable cause” standard); <em>United States </em>v. <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/#328" aria-description="Citation for case: United States v. Blok"><em>Blok, supra, </em>at 328</a></span>, <span class="citation" data-id="227140"><a href="/opinion/227140/united-states-v-blok/#1021" aria-description="Citation for case: United States v. Blok">188 F. 2d, at 1021</a></span> (“No doubt a search of [a desk] without her consent would have been reasonable if made by some people in some circumstances. Her official superiors might reasonably have searched the desk for official property needed for official use”). The only cases to imply that a warrant should be required involve searches that are not work related, see <em>Gillard </em>v. <span class="citation" data-id="358050"><a href="/opinion/358050/francis-d-gillard-v-harold-f-schmidt/#829" aria-description="Citation for case: Francis D. Gillard v. Harold F. Schmidt"><em>Schmidt, supra, </em>at 829, n. 1</a></span>, or searches for evidence of criminal misconduct, see <em>United States </em>v. <em>Kahan, </em><span class="citation" data-id="2005190"><a href="/opinion/2005190/united-states-v-kahan/" aria-description="Citation for case: United States v. Kahan">350 F. Supp. 784</a></span> (SDNY 1972).</p>
<p id="b767-5">The legitimate privacy interests of public employees in the private objects they bring to the workplace may be substantial. Against these privacy interests, however, must be balanced the realities of the workplace, which strongly suggest that a warrant requirement would be unworkable. While police, and even administrative enforcement personnel, conduct searches for the primary purpose of obtaining evidence for use in criminal or other enforcement proceedings, employers most frequently need to enter the offices and desks of their employees for legitimate work-related reasons wholly unrelated to illegal conduct. Employers and supervisors are focused primarily on the need to complete the government agency’s work in a prompt and efficient manner. An employer may have need for correspondence, or a file or report available only in an employee’s office while the employee is <page-number citation-index="1" label="722">*722</page-number>away from the office. Or, as is alleged to have been the case here, employers may need to safeguard or identify state property or records in an office in connection with a pending investigation into suspected employee misfeasance.</p>
<p id="b768-5">In our view, requiring an employer to obtain a warrant whenever the employer wished to enter an employee’s office, desk, or file cabinets for a work-related purpose would seriously disrupt the routine conduct of business and would be unduly burdensome. Imposing unwieldy warrant procedures in such cases upon supervisors, who would otherwise have no reason to be familiar with such procedures, is simply unreasonable. In contrast to other circumstances in which we have required warrants, supervisors in offices such as at the Hospital are hardly in the business of investigating the violation of criminal laws. Rather, work-related searches are merely incident to the primary business of the agency. Under these circumstances, the imposition of a warrant requirement would conflict with “the common-sense realization that government offices could not function if every employment decision became a constitutional matter.” <em>Connick </em>v. <em>Myers, </em><span class="citation" data-id="9429164"><a href="/opinion/110917/connick-ex-rel-parish-of-orleans-v-myers/#143" aria-description="Citation for case: Connick Ex Rel. Parish of Orleans v. Myers">461 U. S. 138, 143</a></span> (1983).</p>
<p id="b768-6">Whether probable cause is an inappropriate standard for public employer searches of their employees’ offices presents a more difficult issue. For the most part, we have required that a search be based upon probable cause, but as we noted in <em>New Jersey </em>v. <em>T. L. O., </em>“[t]he fundamental command of the Fourth Amendment is that searches and seizures be reasonable, and although ‘both the concept of probable cause and the requirement of a warrant bear on the reasonableness of a search, ... in certain limited circumstances neither is required.’” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 340</a></span> (quoting <em>Almeida-Sanchez </em>v. <em>United States, </em><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#277" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 277</a></span> (1973) (Powell, J., concurring)). Thus, “[w]here a careful balancing of governmental and private interests suggests that the public interest is best served by a Fourth Amendment standard of reasonableness that stops short of probable cause, we have not hesitated to <page-number citation-index="1" label="723">*723</page-number>adopt such a standard.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#341" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 341</a></span>. We have concluded, for example, that the appropriate standard for administrative searches is not probable cause in its traditional meaning. Instead, an administrative warrant can be obtained if there is a showing that reasonable legislative or administrative standards for conducting an inspection are satisfied. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#320" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 320</a></span>; <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 538</a></span>.</p>
<p id="b769-4">As an initial matter, it is important to recognize the plethora of contexts in which employers will have an occasion to intrude to some extent on an employee’s expectation of privacy. Because the parties in this case have alleged that the search was either a noninvestigatory work-related intrusion or an investigatory search for evidence of suspected work-related employee misfeasance, we undertake to determine the appropriate Fourth Amendment standard of reasonableness <em>only </em>for these two types of employer intrusions and leave for another day inquiry into other circumstances.</p>
<p id="b769-5">The governmental interest justifying work-related intrusions by public employers is the efficient and proper operation of the workplace. Government agencies provide myriad services to the public, and the work of these agencies would suffer if employers were required to have probable cause before they entered an employee’s desk for the purpose of finding a file or piece of office correspondence. Indeed, it is difficult to give the concept of probable cause, rooted as it is in the criminal investigatory context, much meaning when the purpose of a search is to retrieve a file for work-related reasons. Similarly, the concept of probable cause has little meaning for a routine inventory conducted by public employers for the purpose of securing state property. See <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367</a></span> (1987); <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983). To ensure the efficient and proper operation of the agency, therefore, public employers must be given wide latitude to enter employee offices for work-related, noninvestigatory reasons.</p>
<p id="b770-4"><page-number citation-index="1" label="724">*724</page-number>We come to a similar conclusion for searches conducted pursuant to an investigation of work-related employee misconduct. Even when employers conduct an investigation, they have an interest substantially different from “the normal need for law enforcement.” <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 351 (Blackmun, J., concurring in judgment). Public employers have an interest in ensuring that their agencies operate in an effective and efficient manner, and the work of these agencies inevitably suffers from the inefficiency, incompetence, mismanagement, or other work-related misfeasance of its employees. Indeed, in many cases, public employees are entrusted with tremendous responsibility, and the consequences of their misconduct or incompetence to both the agency and the public interest can be severe. In contrast to law enforcement officials, therefore, public employers are not enforcers of the criminal law; instead, public employers have a direct and overriding interest in ensuring that the work of the agency is conducted in a proper and efficient manner. In our view, therefore, a probable cause requirement for searches of the type at issue here would impose intolerable burdens on public employers. The delay in correcting the employee misconduct caused by the need for probable cause rather than reasonable suspicion will be translated into tangible and often irreparable damage to the agency’s work, and ultimately to the public interest. See <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 353</a></span> (“The time required for a teacher to ask the questions or make the observations that are necessary to turn reasonable grounds into probable cause is time during which the teacher, and other students, are diverted from the essential task of education”). Additionally, while law enforcement officials are expected to “schoo[l] themselves in the niceties of probable cause,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O."><em>id., </em>at 343</a></span>, no such expectation is generally applicable to public employers, at least when the search is not used to gather evidence of a criminal offense. It is simply unrealistic to expect supervisors in most government agencies to learn the subtleties of <page-number citation-index="1" label="725">*725</page-number>the probable cause standard. As Justice Blackmun observed in <em>T. L. 0., </em>“[a] teacher has neither the training nor the day-to-day experience in the complexities of probable cause that a law enforcement officer possesses, and is ill-equipped to make a quick judgment about the existence of probable cause.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#353" aria-description="Citation for case: New Jersey v. T. L. O."><em>Id., </em>at 353</a></span>. We believe that this observation is an equally apt description of the public employer and supervisors at the Hospital, and we conclude that a reasonableness standard will permit regulation of the employer’s conduct “according to the dictates of reason and common sense.” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#343" aria-description="Citation for case: New Jersey v. T. L. O."><em>Id., </em>at 343</a></span>.</p>
<p id="b771-5">Balanced against the substantial government interests in the efficient and proper operation of the workplace are the privacy interests of government employees in their place of work which, while not insubstantial, are far less than those found at home or in some other contexts. As with the building inspections in <em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>, </em>the employer intrusions at issue here “involve a relatively limited invasion” of employee privacy. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 537</a></span>. Government offices are provided to employees for the sole purpose of facilitating the work of an agency. The employee may avoid exposing personal belongings at work by simply leaving them at home.</p>
<p id="b771-6">In sum, we conclude that the “special needs, beyond the normal need for law enforcement make the . . . probable-cause requirement impracticable,” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#351" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 351</a></span> (Black-mun, J., concurring in judgment), for legitimate work-related, noninvestigatory intrusions as well as investigations of work-related misconduct. A standard of reasonableness will neither unduly burden the efforts of government employers to ensure the efficient and proper operation of the workplace, nor authorize arbitrary intrusions upon the privacy of public employees. We hold, therefore, that public employer intrusions on the constitutionally protected privacy interests of government employees for noninvestigatory, work-related purposes, as well as for investigations of work-related misconduct, should be judged by the standard of reasonableness <page-number citation-index="1" label="726">*726</page-number>under all the circumstances. Under this reasonableness standard, both the inception and the scope of the intrusion must be reasonable:</p>
<blockquote id="b772-6">“Determining the reasonableness of any search involves a twofold inquiry: first, one must consider ‘whether the . . . action was justified at its inception,’ <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#20" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 20</a></span>; second, one must determine whether ■ the search as actually conducted ‘was reasonably related in scope to the circumstances which justified the interference in the first place,’ <em>ibid.” New Jersey </em>v. <em>T. L. O., supra, </em>at 341.</blockquote>
<p id="b772-7">Ordinarily, a search of an employee’s office by a supervisor will be “justified at its inception” when there are reasonable grounds for suspecting that the search will turn up evidence that the employee is guilty of work-related misconduct, or that the search is necessary for a noninvestigatory work-related purpose such as to retrieve a needed file. Because petitioners had an “individualized suspicion” of misconduct by Dr. Ortega, we need not decide whether individualized suspicion is an essential element of the standard of reasonableness that we adopt today. See <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 342, n. 8. The search will be permissible in its scope when “the measures adopted are reasonably related to the objectives of the search and not excessively intrusive in light of . . . the nature of the [misconduct].” <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 342</a></span>.</p>
<p id="b772-8">&lt;1</p>
<p id="b772-3">In the procedural posture of this case, we do not attempt to determine whether the search of Dr. Ortega’s office and the seizure of his personal belongings satisfy the standard of reasonableness we have articulated in this case. No eviden-tiary hearing was held in this case because the District Court acted on cross-motions for summary judgment, and granted petitioners summary judgment. The Court of Appeals, on the other hand, concluded that the record in this case justi-<page-number citation-index="1" label="727">*727</page-number>fled granting partial summary judgment on liability to Dr. Ortega.</p>
<p id="b773-5">We believe that both the District Court and the Court of Appeals were in error because summary judgment was inappropriate. The parties were in dispute about the actual justification for the search, and the record was inadequate for a determination on motion for summary judgment of the reasonableness of the search and seizure. Petitioners have consistently attempted to justify the search and seizure as required to secure the state property in Dr. Ortega’s office. Mr. Friday testified in a deposition that he had ordered members of the investigative team to “check Dr. Ortega’s office out in order to separate the business files from any personal files in order to ascertain what was in his office.” App. 50. He further testified that the search was initiated because he “wanted to make sure that we had our state property identified, and in order to provide Dr. Ortega with his property and get what we had out of there, in order to make sure our resident’s files were protected, and that sort of stuff.” <em>Id., </em>at 51.</p>
<p id="b773-6">In their motion for summary judgment in the District Court, petitioners alleged that this search to secure property was reasonable as “part of the established hospital policy to inventory property within offices of departing, terminated or separated employees.” Record Doc. No. 24, p. 9. The District Court apparently accepted this characterization of the search because it applied <em>Chenkin </em>v. <em>Bellevue Hospital Center, New York City Health &amp; Hospitals Corp., </em><span class="citation" data-id="2263945"><a href="/opinion/2263945/chenkin-v-bellevue-hosp-ctr-nyc-etc/" aria-description="Citation for case: Chenkin v. BELLEVUE HOSP. CTR., NYC, ETC.">479 F. Supp. 207</a></span> (SDNY 1979), a case involving a Fourth Amendment challenge to an inspection <em>policy. </em>At the time of the search, however, Dr. Ortega had not been terminated, but rather was still on administrative leave, and the record does not reflect whether the Hospital had a policy of inventorying the property of investigated employees. Respondent, moreover, has consistently rejected petitioners’ characterization of the search as motivated by a need to secure state property. <page-number citation-index="1" label="728">*728</page-number>Instead, Dr. Ortega has contended that the intrusion was an investigatory search whose purpose was simply to discover evidence that would be of use in administrative proceedings. He has pointed to the fact that no inventory was ever taken of the property in the office, and that seized evidence was eventually used in the administrative proceedings. Additionally, Dr. O’Connor stated in a deposition that one purpose of the search was “to look for contractural <em>[sic] </em>and other kinds of documents that might have been related to the issues” involved in the investigation. App. 38.</p>
<p id="b774-5">Under these circumstances, the District Court was in error in granting petitioners summary judgment. There was a dispute of fact about the character of the search, and the District Court acted under the erroneous assumption that thq search was conducted pursuant to a Hospital policy. Moreover, no findings were made as to the scope of the search that was undertaken.</p>
<p id="b774-6">The Court of Appeals concluded that Dr. Ortega was entitled to partial summary judgment on liability. It noted that the Hospital had no policy of inventorying the property of employees on administrative leave, but it did not consider whether the search was otherwise reasonable. Under the standard of reasonableness articulated in this case, however, the absence of a Hospital policy did not necessarily make the search unlawful. A search to secure state property is valid as long as petitioners had a reasonable belief that there was government property in Dr. Ortega’s office which needed to be secured, and the scope of the intrusion was itself reasonable in light of this justification. Indeed, petitioners have put forward evidence that they had such a reasonable belief; at the time of the search, petitioners knew that Dr. Ortega had removed the computer from the Hospital. The removal of the computer — together with the allegations of mismanagement of the residency program and sexual harassment— may have made the search reasonable at its inception under the standard we have put forth in this case. As with the <page-number citation-index="1" label="729">*729</page-number>District Court order, therefore, the Court of Appeals conclusion that summary judgment was appropriate cannot stand.</p>
<p id="b775-5">On remand, therefore, the District Court must determine the justification for the search and seizure, and evaluate the reasonableness of both the inception of the search and its scope.<footnotemark>*</footnotemark></p>
<p id="b775-6">Accordingly, the judgment of the Court of Appeals is reversed, and the case is remanded to that court for further proceedings consistent with this opinion.</p>
<p id="b775-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b775-11">We have no occasion in this case to reach the issue of the appropriate standard for the evaluation of the Fourth Amendment reasonableness of the seizure of Dr. Ortega’s personal items. Neither the District Court nor the Court of Appeals addressed this issue, and the <em>amicus curiae </em>brief filed on behalf of respondent did not discuss the legality of the seizure separate from that of the search. We also have no occasion in this case to address whether qualified immunity should protect petitioners from damages liability under § 1983. See <em>Davis </em>v. <em>Scherer, </em><span class="citation" data-id="9429708"><a href="/opinion/111241/davis-v-scherer/" aria-description="Citation for case: Davis v. Scherer">468 U. S. 183</a></span> (1984); <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800</a></span> (1982). The qualified immunity issue was not raised below and was not addressed by either the District Court or the Court of Appeals. Nor do we address the proper Fourth Amendment analysis for drug and alcohol testing of employees. Finally, we do not address the appropriate standard when an employee is being investigated for criminal misconduct or breaches of other nonwork-related statutory or regulatory standards.</p>
</footnote>
</opinion>
```

---
