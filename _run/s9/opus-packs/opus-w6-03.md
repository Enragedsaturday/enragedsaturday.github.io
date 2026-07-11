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

## GROUP: _overhaul2/lake/cases/Johnson v. Glick.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Johnson v. Glick
type: case
citation: "481 F.2d 1028 (1973)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir. 1973
court_level: coa
circuit: ca2
year: 1973
date_decided: 1973-06-29
docket: "No. 845, Docket 72-2428"
authority_weight: "Binding in-circuit — 2d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/8903545/johnson-v-glick/"
  cluster_id: 8903545
  opinion_id: null
  identity_checked: true
lake:
  record_id: Johnson v. Glick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Use of Force]]"
    role: Key
related:
  - "[[Use of Force]]"
  - "[[Graham v. Connor]]"
tags:
  - case
  - fourth-amendment
  - use-of-force
  - excessive-force
  - substantive-due-process
  - pretrial-detainee
  - section-1983
holding: "Not every use of force by a custodial officer is a constitutional violation; whether the line is crossed depends on the need for force, the relationship between the need and the amount used, the extent of injury, and whether force was applied in good faith to maintain discipline or maliciously to cause harm — the pre-Graham due-process test for excessive force."
---

# Johnson v. Glick

*481 F.2d 1028 (2d Cir. 1973)* (No. 72-2428) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 8903545 → majority opinion 8890588 (481 F.2d 1028, Friendly, J., decided 1973-06-29); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Australia Johnson, a pretrial detainee at a Manhattan house of detention, alleged that a corrections officer, angered during a disturbance, struck him in the head and threatened him, causing injury. He sued the warden and the officer under § 1983, and the district court dismissed the complaint. On appeal, Judge Friendly confronted the question of what constitutional standard governs a custodial officer's use of force against a detainee.

## Issue
By what standard does a court decide whether a custodial officer's use of force against a detainee is so excessive as to violate the Constitution and support a § 1983 claim.

## Rule
Grounding the claim in substantive due process rather than the Fourth or Eighth Amendments, Judge Friendly announced a multi-factor test that became the template for excessive-force analysis: "In determining whether the constitutional line has been crossed, a court must look to such factors as the need for the application of force, the relationship between the need and the amount of force that was used, the extent of injury inflicted, and whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm." — 481 F.2d at 1033.

## Application
Not every push or shove, even one that later seems unnecessary in the calm of a courtroom, offends the Constitution; managing detainees may justify some intentional force. But a blow inflicted maliciously, without penological need, does. Reading the [[Common Legal Terms#pro-se|pro se]] complaint generously, the court held it stated a claim against the officer who allegedly struck Johnson, while affirming dismissal against the warden, who could not be liable under § 1983 on a [[Common Legal Terms#respondeat-superior|respondeat superior]] theory absent personal involvement.

## Conclusion
Dismissal was **reversed** as to the officer and **affirmed** as to the warden; the case was [[Reading and Citing Cases#on-remand|remanded]]. Friendly, J., wrote for the panel.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Johnson v. Glick*'s four-factor test was the dominant excessive-force standard for a generation, but *[[Graham v. Connor]]* (1989) held that force claims arising during an arrest, investigatory stop, or other seizure are governed by the Fourth Amendment's objective-reasonableness standard — not *Glick*'s substantive-due-process test — and criticized importing *Glick*'s "malicious and sadistic" element into that context. *Glick*'s approach continued to inform the analysis for pretrial detainees until the standard there was itself recalibrated by *[[Kingsley v. Hendrickson]]* (2015).

## Appears on
- [[Use of Force]] — *Key*

## Sources
- [*Johnson v. Glick*, 481 F.2d 1028 (2d Cir. 1973)](https://www.courtlistener.com/opinion/8903545/johnson-v-glick/) — pinpoint: 1033 (majority; Friendly, J.); Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "900459dee5ad9524", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Johnson v. Glick"}, "payload": {"all": [{"cite": "481 F.2d 1028", "page": "1028", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "481"}], "display": "481 F.2d 1028", "official": {"cite": "481 F.2d 1028", "page": "1028", "reporter": "F.2d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "481"}, "official_selection_present": true, "record_id": "Johnson v. Glick"}}
{"assertion_id": "e157700f76d450e4", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Johnson v. Glick"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Johnson v. Glick", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Johnson v. Glick

```json
{
  "schema_version": "s2.v1",
  "record_id": "Johnson v. Glick",
  "status": "under_review",
  "identity": {
    "case_name": "Johnson v. Glick",
    "case_name_short": "Glick",
    "case_name_full": "Australia JOHNSON v. A. GLICK, Warden of Manhattan House of Detention for Men, 125 White Street, New York, N. Y. Employee-Officer John, 1765 Badge Number, Manhattan House of Detention for Men, 125 White Street, New York, N. Y.",
    "input_case_name": "Johnson v. Glick",
    "court": "2d Cir. 1973",
    "court_id": "ca2",
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "1973-06-29",
    "year": 1973,
    "docket": "No. 845, Docket 72-2428",
    "cluster_id": 8903545,
    "lead_opinion_id": 8890588,
    "sibling_ids": [],
    "absolute_url": "/opinion/8903545/johnson-v-glick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "481 F.2d 1028",
      "volume": "481",
      "reporter": "F.2d",
      "page": "1028",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "481 F.2d 1028",
        "volume": "481",
        "reporter": "F.2d",
        "page": "1028",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "481 F.2d 1028",
    "official_selection": {
      "court_class": "state",
      "selected": "481 F.2d 1028",
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
    "date_created": "2026-07-06T05:46:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:46:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "johnson-v-glick--8903545",
      "to_record_id": "Johnson v. Glick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Johnson v. Glick

```
<opinion type="majority">
<author id="b1091-21">FRIENDLY, Circuit Judge:</author>
<p id="b1091-22">This appeal concerns an order of the District Court for the Southern District of New York dismissing a complaint under the Civil Rights Act, <span class="citation no-link">42 U.S.C. § 1983</span>, <span class="citation no-link">28 U.S.C. § 1343</span>(3), for failure to state a claim on which relief can be granted. The complaint was brought against the Warden of the Manhattan House of Detention for Men and a correction officer, described in the complaint only as Officer John, Badge No. 1765, but now identified as John Fuller; by plaintiff Australia Johnson, who had been held in the House of Detention prior to and during his trial in the state courts on felony charges. It alleged that, while plaintiff was being checked back into the House of Detention, Officer Fuller reprimanded Johnson and other men for a claimed failure to follow instructions; that when Johnson endeavored to explain that they were doing only what another officer had told them to do, Officer Fuller rushed into the holding cell, grabbed him by the collar and struck him twice on the head with something enclosed in the officer’s fist; that during this incident the officer <page-number citation-index="1" label="1030">*1030</page-number>threatened him, saying “I’ll kill you, old man, I’ll break you in half”; that Fuller than harassed Johnson by detaining him in the holding cell for two hours before returning him to his cell; that when Johnson requested medical attention, Fuller, who was called upon by another officer to escort Johnson to the jail doctor, instead held him for another two hours in another cell before permitting him to see the doctor; and that despite the “pain pills” given him by the doctor, Johnson has since “been having terrible pains in his head.”</p>
<p id="b1092-4">Recognizing that there were numerous decisions in other circuits that would seem to uphold the validity of the'complaint as against the officer, as well as one to the contrary, Judge Knapp nevertheless dismissed the complaint, saying “So far as I am aware no decision in this circuit requires such a conclusion, and it is one at which I would arrive only under constraint.” Although we realize that upholding this complaint may well lead to considerable further expansion of actions by state prisoners under <span class="citation no-link">42 U.S.C. § 1983</span>, so long as they may bring their civil rights complaints directly to federal courts without first presenting them to state courts,<footnotemark>1</footnotemark> we think the ruling was in error so far as the officer was concerned.</p>
<p id="b1092-5">The longest line of authority for the proposition that a complaint alleging an unprovoked attack on a prisoner by a state prison guard is within <span class="citation no-link">42 U.S.C. § 1983</span> comes from the Ninth Circuit. The first case in the line is Brown v. Brown, <span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">368 F.2d 992</a></span> (9 Cir. 1966), where, however, the complaint alleged other deprivations of civil rights.<footnotemark>2</footnotemark> This was followed by Dodd v. Spokane County, <span class="citation" data-id="279782"><a href="/opinion/279782/dodd-v-spokane-county/#333" aria-description="Citation for case: Dodd v. Spokane County">393 F.2d 330, 333-334</a></span> (9 Cir. 1968),</p>
<p id="b1092-8">although the complaint there alleged not brutality <em>simpliciter </em>but the administration of violence in an effort to cause Dodd to testify falsely in another’s criminal trial. Next came Wiltsie v. California Department of Corrections, <span class="citation" data-id="8880072"><a href="/opinion/8893681/wiltsie-v-california-department-of-corrections/" aria-description="Citation for case: Wiltsie v. California Department of Corrections">406 F.2d 515</a></span> (9 Cir. 1968). Although this was a case of beating pure and simple, the court, over Judge Chambers' dissent held it to be “indistinguishable from Brown v. Brown,” <em>supra. </em>To the same effect is Allison v. California Adult Authority, <span class="citation" data-id="287696"><a href="/opinion/287696/charles-allison-v-california-adult-authority/" aria-description="Citation for case: Charles Allison v. California Adult Authority">419 F.2d 822</a></span> (9 Cir. 1969), where the court followed <em><span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">Brown</a></span> </em>despite its recognition “that frivolous Civil Rights suits by prison inmates have become a matter of concern to district courts” and its belief that “Allison’s allegations of physical abuse stretch one’s credulity.”</p>
<p id="b1092-9">Several other circuits have reached the same result. Bethea v. Crouse, <span class="citation" data-id="9454967"><a href="/opinion/286950/oscar-bethea-v-sherman-h-crouse-warden-kansas-state-penitentiary-james/" aria-description="Citation for case: Oscar Bethea v. Sherman H. Crouse, Warden, Kansas State...">417 F.2d 504</a></span> (10 Cir. 1969); Collum v. Butler, <span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">421 F.2d 1257</a></span> (7 Cir. 1970); Tolbert v. Bragan, <span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">451 F.2d 1020</a></span> (5th Cir. 1971) ; Howell v. Cataldi, <span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/" aria-description="Citation for case: Henry Howell v. Cataldi">464 F.2d 272</a></span> (3 Cir. 1972). Still others, though they apparently^have not yet been faced with precisely the issue posed by this complaint, have sustained civil rights actions involving closely related situations. Jenkins v. Averett, <span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">424 F.2d 1228</a></span> (4 Cir. 1970) (police brutality following arrest) ; Carter v. Carlson, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">144 U.S.App.D.C. 388</a></span>, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">447 F.2d 358</a></span> (1971) (same), rev’d on other grounds sub nom. District of Columbia <em>v. </em>Carter, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">409 U.S. 418</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">93 S.Ct. 602</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter"><em>34 </em>L.Ed.2d 613</a></span> (1973); Fitzke v. Shappell, <span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">468 F.2d 1072</a></span> (6 Cir. 1972) (failure to provide medical care for prisoner). Only one circuit is clearly to the contrary, Cole v. Smith, <span class="citation" data-id="267690"><a href="/opinion/267690/robert-l-cole-v-lavern-smith-bernard-danner-and-allen-vogel/" aria-description="Citation for case: Robert L. Cole v. Lavern Smith, Bernard Danner and Allen...">344 F.2d 721</a></span> (8 Cir. 1965).</p>
<p id="b1092-12">Aside from the weight of all this authority, we are not so certain as was the <page-number citation-index="1" label="1031">*1031</page-number>district judge that the slate in this circuit is completely clean. In Martinez v. Mancusi, <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d 921</a></span> (2 Cir. 1970), we upheld a civil rights complaint against prison officials which was read to allege “a deliberate indifference to, and defiance of, the express instructions of the operating surgeons and the hospital attendants,” <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>; it seems hard to draw a satisfactory legal distinction between such conduct and the deliberate infliction of physical suffering in a non-medical setting. In Inmates of the Attica Correctional Facility v. Rockefeller, <span class="citation" data-id="9457668"><a href="/opinion/300646/inmates-of-the-attica-correctional-facility-v-nelson-rockefeller/#22" aria-description="Citation for case: Inmates of the Attica Correctional Facility v. Nelson...">453 F.2d 12, 22-24</a></span> (2 Cir. 1971), we granted preliminary injunctive relief where there had been a record of “beatings, physical abuse, torture, running of gauntlets, and similar cruelty.” While some emphasis was placed on the continuing and systematic acts of the correctional officers, this was said more in justification of issuance of an injunction than as a predicate for actionability. And, subsequent to Judge Knapp’s decision, we have stated in dictum:</p>
<blockquote id="b1093-5">We assume that brutal police conduct violates a right guaranteed by the due process clause of the Fourteenth Amendment.</blockquote>
<p id="b1093-6">Rosenberg v. Martin, <span class="citation" data-id="310933"><a href="/opinion/310933/jerome-rosenberg-v-raymond-v-martin/#526" aria-description="Citation for case: Jerome Rosenberg v. Raymond v. Martin">478 F.2d 520, 526</a></span> (2 Cir. 1973).</p>
<p id="b1093-7">The great weight of authority in favor of the assumption thus stated in <em><span class="citation" data-id="310933"><a href="/opinion/310933/jerome-rosenberg-v-raymond-v-martin/" aria-description="Citation for case: Jerome Rosenberg v. Raymond v. Martin">Rosenberg</a></span> </em>has not been accompanied by an equivalent amount of analysis. Many of 'the opinions, including our own in <em><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Martinez</a></span> </em>and <em>Inmates, </em>rely on a passing reference to the “cruel and unusual punishment” clause of the Eighth Amendment. The most extensive judicial treatment of the subject,' Judge Aldisert’s opinion in Howell v. <span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/" aria-description="Citation for case: Henry Howell v. Cataldi">Cataldi, <em>supra, </em></a></span><span class="citation" data-id="9458497"><a href="/opinion/304768/henry-howell-v-cataldi/#280" aria-description="Citation for case: Henry Howell v. Cataldi">464 F.2d at 280-282</a></span>, likewise relies on that clause.</p>
<p id="b1093-8">A case like this, however, does not lie comfortably within the Eighth Amendment. The text:</p>
<p id="b1093-11">Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted suggests action taken, usually by a court, in carrying out a legislative authorization or command. The language, as is well known, is practically a verbatim copy of the tenth clause of the English Bill of Rights, 1 Wm. &amp; Mary, 2d sess., eh. 2 (1688), which, in turn, embodied a corresponding section of the Declaration of Rights that was a cornerstone of the settlement of the Glorious Revolution. Although George Mason, who drafted the similar clause in the Virginia Declaration of Rights, which was the more immediate progenitor of the Eighth Amendment, may have been mistaken in thinking that the provision was aimed merely at torturous rather than at excessive punishments,<footnotemark>3</footnotemark> there can be no disagreement that what sparked the English provision was the conduct of judges under James II. ^The background of our own Bill of Rights/ however,^ makes clear that the Eighth Amendment was intended to apply not only to the acts of judges but as a restraint on legislative action as wellH See In re Kemmler, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#446" aria-description="Citation for case: In Re Kemmler">136 U.S. 436, 446-447</a></span>, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">10 S.Ct. 930</a></span>, <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">34 L.Ed. 519</a></span> (1890); Weems v. United States, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/#371" aria-description="Citation for case: Weems v. United States">217 U.S. 349, 371-373, 378-379</a></span>, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">30 S.Ct. 544</a></span>, <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">54 L.Ed. 793</a></span> (1910); Furman v. Georgia, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/#266" aria-description="Citation for case: Furman v. Georgia">408 U.S. 238, 266-269</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">92 S.Ct. 2726</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">33 L.Ed.2d 346</a></span> (1972) (concurring opinion of Mr. Justice Brennan).<footnotemark>4</footnotemark> Undeed, every decision of the Supreme Court striking down a punishment under the Eighth Amendment has concerned a legislative act. Weems v. United <span class="citation" data-id="9418181"><a href="/opinion/97242/weems-v-united-states/" aria-description="Citation for case: Weems v. United States">States, <em>supra; </em></a></span>Trop v. Dulles, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">356 U.S. 86</a></span>, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">78 S.Ct. 590</a></span>, <span class="citation" data-id="9421564"><a href="/opinion/105659/trop-v-dulles/" aria-description="Citation for case: Trop v. Dulles">2 L.Ed.2d 630</a></span> (1958) (plurality opinion of Chief Justice Warren); Robinson v. California, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">370 U.S. 660</a></span>, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">82 S.Ct. 1417</a></span>, <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/" aria-description="Citation for case: Robinson v. California">8 L.Ed.2d 758</a></span> (1962); Furman v. <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">Georgia, <em>supra.</em></a></span></p>
<p id="AAB"><page-number citation-index="1" label="1032">*1032</page-number>We do not suggest, however, that the cruel and unusual punishment clause must necessarily be read as limited to acts of legislatures in authorizing sentences or of judges imposing them. It can fairly be deemed to be applicable to the manner in which an otherwise constitutional sentence, as the death penalty was then thought to be, is carried out by an executioner, see Louisiana ex rel. Francis v. Resweber, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">329 U.S. 459</a></span>, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">67 S.Ct. 374</a></span>, <span class="citation" data-id="9419910"><a href="/opinion/104355/louisiana-ex-rel-francis-v-resweber/" aria-description="Citation for case: Louisiana Ex Rel. Francis v. Resweber">91 L.Ed. 422</a></span> (1947), or to cover conditions of confinement which may make intolerable an otherwise constitutional term of imprisonment, see Holt v. Sarver, <span class="citation" data-id="9456861"><a href="/opinion/296489/lawrence-j-holt-v-robert-sarver-commissioner-of-corrections/" aria-description="Citation for case: Lawrence J. Holt v. Robert Sarver, Commissioner of...">442 F.2d 304</a></span> (8 Cir. 1971). On a parity of reasoning, we find no difficulty in considering the cruel and unusual punishment clause to be applicable to such systems of prison discipline as solitary confinement, see Wright v. McMann, <span class="citation" data-id="9453201"><a href="/opinion/278308/lawrence-william-wright-v-daniel-mcmann-as-warden-of-clinton-state-prison/" aria-description="Citation for case: Lawrence William Wright v. Daniel McMann as Warden of...">387 F.2d 519</a></span> (2 Cir. 1967) (reversing dismissal of complaint), <span class="citation multiple-matches"><a href="/c/F.2d/460/126/">460 F.2d 126</a></span> (2 Cir.) (upholding award of damages), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./409/885/">409 U.S. 885</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/115/">93 S.Ct. 115</a></span>, <span class="citation no-link">34 L.Ed.2d 141</span> (1972); Sostre v. McGinnis, <span class="citation" data-id="8885370"><a href="/opinion/8898661/sostre-v-mcginnis/#190" aria-description="Citation for case: Sostre v. McGinnis">442 F.2d 178, 190-194</a></span> (2 Cir. 1971), cert. denied, <span class="citation" data-id="108452"><a href="/opinion/108452/robins-v-united-states/" aria-description="Citation for case: Robins v. United States">404 U.S. 1049</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./92/719/">92 S.Ct. 719</a></span>, <span class="citation no-link">30 L.Ed.2d 740</span> (1972); Novak v. Beto, <span class="citation" data-id="8886941"><a href="/opinion/8900130/novak-v-beto/" aria-description="Citation for case: Novak v. Beto">453 F.2d 661</a></span> (5 Cir. 1971), cert. denied, <span class="citation" data-id="9425123"><a href="/opinion/108686/sellars-et-al-v-beto-corrections-director/" aria-description="Citation for case: Sellars Et Al. v. Beto, Corrections Director">409 U.S. 968</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/279/">93 S.Ct. 279</a></span>, <span class="citation" data-id="9425123"><a href="/opinion/108686/sellars-et-al-v-beto-corrections-director/" aria-description="Citation for case: Sellars Et Al. v. Beto, Corrections Director">34 L.Ed.2d 233</a></span> (1972), or corporal punishment, see Jackson v. Bishop, <span class="citation" data-id="8879837"><a href="/opinion/8893462/jackson-v-bishop/" aria-description="Citation for case: Jackson v. Bishop">404 F.2d 571</a></span> (8 Cir. 1968). The thread common to all these cases is that “punishment” has been deliberately administered for a penal or disciplinary purpose, with the apparent authorization of high prison officials charged by the state with responsibility for care, control, and discipline of prisoners. In contrast, although a spontaneous attack by a guard is “cruel” and, we hope, “unusual,” it does not fit any ordinary concept of “punishment.”</p>
<p id="b1094-6">This is particularly clear in a case like the present where the plaintiff had not yet been found liable to “punishment” of any sort. We have considerable doubt that the cruel and unusual punishment clause is properly applicable at all until after conviction and sentence. See Anderson v. Nosser, 456 F.2d 2d 835 (5 Cir.) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./409/848/">409 U.S. 848</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./93/53/">93 S.Ct. 53</a></span>, <span class="citation" data-id="8981837"><a href="/opinion/8989681/berger-v-columbia-broadcasting-system-inc/" aria-description="Citation for case: Berger v. Columbia Broadcasting System, Inc.">34 L.Ed.2d 89</a></span> (1972) modifying <span class="citation" data-id="9456521"><a href="/opinion/294828/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">438 F.2d 183</a></span> (5 Cir. 1971); Hamilton v. Love, <span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/#1191" aria-description="Citation for case: Hamilton v. Love">328 F.Supp. 1182, 1191</a></span> (E.D.Ark.1971); but see Rhem v. McGrath, <span class="citation" data-id="1460390"><a href="/opinion/1460390/rhem-v-mcgrath/#690" aria-description="Citation for case: Rhem v. McGrath">326 F.Supp. 681, 690</a></span> (S.D.N.Y. 1971). Yet it would be absurd to hold that a pre-trial detainee has less constitutional protection against acts of prison guards than one who has been convicted.</p>
<p id="b1094-7">The solution lies in the proposition that, both before and after sentence, constitutional protection against police brutality is not limited to conduct violating the specific command of the Eighth Amendment or, as in Monroe v. Pape, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U.S. 167</a></span>, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">81 S.Ct. 473</a></span>, <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">5 L.Ed.2d 492</a></span> (1961), of the Fourth. Rochin v. California, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U.S. 165</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">96 L.Ed. 183</a></span> (1952), must stand for the proposition that, quite apart from any “specific” of the Bill of Rights, application of undue force by law enforcement officers deprives a suspect of liberty without due process of law. If Rochin suffered such a violation of his constitutional rights by the police as to be entitled to invalidation of a conviction obtained as a consequence, he also was the victim of a violation sufficient to sustain an action under the Civil Rights Act.<footnotemark>5</footnotemark> The same principle <page-number citation-index="1" label="1033">*1033</page-number>should extend to acts of brutality by correctional officers, although the notion of what constitutes brutality may not necessarily be the same. This, apparently, was the view taken by the Seventh Circuit in Collum v. <span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">Butler, <em>supra, </em></a></span><span class="citation" data-id="288499"><a href="/opinion/288499/curtis-collum-cross-appellee-v-frank-a-butler-james-hand-and-james/#1259" aria-description="Citation for case: Curtis Collum, Cross-Appellee v. Frank A. Butler, James...">421 F.2d at 1259-1260</a></span>, by the Fifth in Tolbert v. <span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">Bragan, <em>supra, </em></a></span><span class="citation" data-id="300228"><a href="/opinion/300228/george-tolbert-jr-v-warden-bragan/" aria-description="Citation for case: George Tolbert, Jr. v. Warden Bragan">451 F.2d 1020</a></span>, and by the Ninth in Wiltsie v. California Department of Corrections, <em>supra, </em><span class="citation" data-id="8880072"><a href="/opinion/8893681/wiltsie-v-california-department-of-corrections/#517" aria-description="Citation for case: Wiltsie v. California Department of Corrections">406 F.2d at 517</a></span>. See also Jenkins v. <span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">Averett, <em>supra, </em></a></span><span class="citation" data-id="9455514"><a href="/opinion/289671/robert-leon-jenkins-a-minor-by-his-mother-and-next-friend-roberta-b/#1232" aria-description="Citation for case: Robert Leon Jenkins, a Minor, by His Mother and Next...">424 F.2d at 1232</a></span>, Fitzke v. <span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">Shappell, <em>supra, </em></a></span><span class="citation" data-id="306421"><a href="/opinion/306421/robert-fitzke-and-joy-fitzke-v-barry-shappell-deputy-sheriff-and-elwin/#1076" aria-description="Citation for case: Robert Fitzke and Joy Fitzke v. Barry Shappell, Deputy...">468 F.2d at 1076</a></span>. And most of the courts faced with challenges to the conditions of <em>pre-trial </em>detention have primarily based their analysis directly on the due process clause. See Anderson v. Nosser, <em>supra, </em><span class="citation" data-id="302032"><a href="/opinion/302032/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">456 F.2d 835</a></span>; Hamilton v. <span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/" aria-description="Citation for case: Hamilton v. Love">Love, <em>supra, </em></a></span><span class="citation" data-id="1428202"><a href="/opinion/1428202/hamilton-v-love/" aria-description="Citation for case: Hamilton v. Love">328 F.Supp. 1182</a></span>; Jones v. Wittenberg, <span class="citation" data-id="1572711"><a href="/opinion/1572711/jones-v-wittenberg/" aria-description="Citation for case: Jones v. Wittenberg">323 F.Supp. 93</a></span> (N.D.Ohio 1971), aff’d, <span class="citation" data-id="302035"><a href="/opinion/302035/charles-jones-v-william-metzger-homer-roberts/" aria-description="Citation for case: Charles Jones v. William Metzger, Homer Roberts">456 F.2d 854</a></span> (6 Cir. 1972); Brenneman v. Madigan, <span class="citation" data-id="1691314"><a href="/opinion/1691314/brenneman-v-madigan/" aria-description="Citation for case: Brenneman v. Madigan">343 F.Supp. 128</a></span> (N.D.Cal. 1972).</p>
<p id="b1095-5">While the <em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Rochin</a></span> </em>test, “conduct that shocks the conscience,” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U. S. at 172</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>, is not one that can be applied by a computer,<footnotemark>6</footnotemark> it at least points the way. Certainly the constitutional protection is nowhere nearly so extensive as that afforded by the common law tort action for battery, which makes actionable any intentional and unpermitted contact with the plaintiff’s person or anything attached to it and practically identified with it, see Prosser, Torts § 9 (4th ed. 1971); still less is it as extensive as that afforded by the common law tort action for assault, redressing “Any act of such a nature as to excite an apprehension of battery,” <em>id. </em>§ 10, at <em>38.</em><footnotemark><em>7</em></footnotemark><em> </em>Although “the least touching of another in anger is a battery,” Cole v. Turner, 6 Mod. 149, 87 Eng.Rep. 907, 90 Eng.Rep. 958 (K.B. 1704) (Holt, C. J.), it is not a violation of a constitutional right actionable under <span class="citation no-link">42 U.S.C. § 1983</span>. The management by a few guards of large numbers of prisoners, not usually the most gentle or tractable of men and women, may require and justify the occasional use of a degree of intentional force. Not every push or shove, even if it may later seem unnecessary in the peace of a judge’s chambers, violates a prisoner’s constitutional rights. In determining whether the constitutional line has been crossed, a court must look to such factors as the need for the application of force, the relationship between the need and the amount of force that was used, the extent of injury inflicted, and whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm. Taking this view, and reading the complaint with the generosity required in <em>pro se </em>civil rights actions, Haines v. Kerner, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/#520" aria-description="Citation for case: Haines v. Kerner">404 U.S. 519, 520-521</a></span>, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">92 S.Ct. 594</a></span>, <span class="citation" data-id="108432"><a href="/opinion/108432/haines-v-kerner/" aria-description="Citation for case: Haines v. Kerner">30 L.Ed.2d 652</a></span> (1972), we think it stated a claim against Officer Fuller.</p>
<p id="b1095-11">On the other hand, even on a charitable reading, we see no basis for <page-number citation-index="1" label="1034">*1034</page-number>sustaining the complaint against the warden. The rule in this circuit is that when monetary damages are sought under § 1983, the general doctrine of <em>respondeat superior </em>does not suffice and a showing of some personal responsibility of the defendant is required. Thus in Martinez v. <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Mancusi, <em>supra, </em></a></span><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>, we conditioned a conclusion of liability of the warden on a finding that he was personally “responsible for what the guards did.” Again, in Wright v. Mc-Mann, <em>supra, </em>460 F.2d at 134-135, in upholding a damage award as against Warden McMann, we stressed that “there is every reason to believe that he was aware of segregation cell conditions,” and that “responsibility for permitting such conditions to exist was ultimately, in any event, squarely his.” See also Harty v. Rockefeller, <span class="citation" data-id="2182189"><a href="/opinion/2182189/harty-v-rockefeller/" aria-description="Citation for case: Harty v. Rockefeller">338 F. Supp. 367</a></span> (S.D.N.Y.1972); (Gurfein, J.). Adams v. Pate, <span class="citation" data-id="297684"><a href="/opinion/297684/vernon-c-adams-v-frank-j-pate-warden-luther-w-miller-v-illinois/" aria-description="Citation for case: Vernon C. Adams v. Frank J. Pate, Warden, Luther W....">445 F.2d 105</a></span>, 107 &amp; n. 2 (7 Cir. 1971), and a dictum in Dunham v. Crosby, <span class="citation" data-id="293866"><a href="/opinion/293866/kenneth-t-dunham-v-philip-b-crosby-jr/#1180" aria-description="Citation for case: Kenneth T. Dunham v. Philip B. Crosby, Jr.">435 F.2d 1177, 1180</a></span> (1 Cir. 1970), are in accord. We reaffirm our position here, though we are aware that Anderson v. Nosser, <span class="citation" data-id="9456521"><a href="/opinion/294828/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">438 F.2d 183</a></span>, 199-200 &amp; n. 13 (5 Cir. 1971), modified, <span class="citation" data-id="302032"><a href="/opinion/302032/katie-ruth-anderson-v-j-j-nosser-james-bradley-v-j-j-nosser/" aria-description="Citation for case: Katie Ruth Anderson v. J. J. Nosser, James Bradley v. J....">456 F.2d 835</a></span> (5 Cir. 1972) (en banc), left the question open; that Hesselgesser v. Reilly, <span class="citation" data-id="295850"><a href="/opinion/295850/donald-d-hesselgesser-v-william-j-reilly-sheriff-of-spokane-county/" aria-description="Citation for case: Donald D. Hesselgesser v. William J. Reilly, Sheriff of...">440 F.2d 901</a></span> (9 Cir. 1971), held that § 1983 liability might be predicated on a specific state statute making a sheriff liable for the acts of his deputies; and that Carter v. Carlson, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">144 U.S.App.D.C. 388</a></span>, <span class="citation" data-id="9457236"><a href="/opinion/298619/melvin-carter-v-john-r-carlson/" aria-description="Citation for case: Melvin Carter v. John R. Carlson">447 F.2d 358</a></span>, 370 &amp; n. 39, rev’d on other grounds, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">409 U.S. 418</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">93 S.Ct. 602</a></span>, <span class="citation" data-id="108654"><a href="/opinion/108654/district-of-columbia-v-carter/" aria-description="Citation for case: District of Columbia v. Carter">34 L.Ed.2d 613</a></span> (1973), went all the way, holding <em>respondeat superior </em>to be fully applicable to actions under § 1983.</p>
<p id="b1096-6">Here the complaint alleged only that Warden Glick was in charge of all the correctional officers employed at the House of Detention. It did not allege that the warden had authorized the officer’s conduct, see Martinez v. <span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">Mancusi, <em>supra, </em></a></span><span class="citation" data-id="297139"><a href="/opinion/297139/louis-martinez-v-vincent-r-mancusi-warden-attica-prison-dr-williams/#924" aria-description="Citation for case: Louis Martinez v. Vincent R. Mancusi, Warden, Attica...">443 F.2d at 924</a></span>, or even that there had been a history of previous episodes requiring the warden to take therapeutic action, <em>cf. </em>Wright v. <span class="citation" data-id="9453201"><a href="/opinion/278308/lawrence-william-wright-v-daniel-mcmann-as-warden-of-clinton-state-prison/" aria-description="Citation for case: Lawrence William Wright v. Daniel McMann as Warden of...">McMann, <em>supra, </em></a></span>460 F.2d at 134-135; it alleged a single spontaneous incident, unforeseen and unforeseeable by higher authority. While appellant’s counsel urged that we permit him to develop further facts that might implicate the warden, the better course is to affirm the dismissal of the complaint against the warden without prejudice to an application for leave to amend if a factual basis for this should appear. We request that counsel assigned by the judge to take this appeal shall continue to act for Johnson in the district court.</p>
<p id="b1096-8">Reversed with respect to Officer Fuller; affirmed with respect to Warden Glick. No costs.</p>
<footnote label="1">
<p id="b1092-6">. Apart from controlling Supreme Court authority, see Preiser v. Rodriguez, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#477" aria-description="Citation for case: Preiser v. Rodriguez">411 U.S. 475, 477, 498-499</a></span>, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">93 S.Ct. 1827</a></span>, <span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">36 L.Ed.2d 439</a></span> (1973), this would be a most inappropriate ease in which to require exhaustion of state judicial remedies. As a result of Johnson’s conviction of manslaughter, and the consequent suspension of his civil rights, N.Y_. Civil Rights Law, McKinney’s Consol.Laws, c. 6, § 79, he is presently unable to bring an action in the state courts.</p>
</footnote>
<footnote label="2">
<p id="b1092-14">. Also, it may be that all the beatings alleged there were for the purpose of extracting a confession from Brown, see <span class="citation" data-id="273780"><a href="/opinion/273780/homer-ray-brown-v-edmund-g-brown-governor-state-of-california/" aria-description="Citation for case: Homer Ray Brown v. Edmund G. Brown, Governor, State of...">368 F.2d at 993</a></span>-994 n. 2, in which case Fifth Amendment protections would be implicated.</p>
</footnote>
<footnote label="3">
<p id="b1093-9">. See Granucci, “Nor Cruel and Unusual Punishments Inflicted”: The Originnl Meaning, 57 Calif.L.Rev. 839 (1969).</p>
</footnote>
<footnote label="4">
<p id="b1093-12">. The history of the cruel and unusual punishment clause is lucidly recounted in Mr. Justice Marshall’s concurring opinion in Furman v. <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">Georgia, <em>supra, </em></a></span><span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/#316" aria-description="Citation for case: Furman v. Georgia">408 U.S. at 316-322</a></span>, <span class="citation" data-id="9424993"><a href="/opinion/108605/furman-v-georgia/" aria-description="Citation for case: Furman v. Georgia">92 S.Ct. 2726</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b1094-4">. We note also that in Williams v. United States, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">341 U.S. 97</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">71 S.Ct. 576</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/" aria-description="Citation for case: Williams v. United States">95 L.Ed. 774</a></span> (1951), the Supreme Court had little difficulty in upholding a conviction of a law enforcement officer under <span class="citation no-link">18 U.S.C. § 242</span>, the criminal counterpart of <span class="citation no-link">42 U.S.C. § 1983</span>, finding due process to be violated “where police take matters in their own hands, seize victims, [and] beat and pound them until they confess.” <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#101" aria-description="Citation for case: Williams v. United States">341 U.S. at 101</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#579" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 579</a></span>. The indictment charged that the victim had been deprived of</p>
<blockquote id="b1094-9">the right and privilege not to be deprived of liberty without due process of law, the right and privilege to be secure in his person while in the custody of the State of Florida, the right and privilege not to be subjected to punishment without due process of <page-number citation-index="1" label="1033">*1033</page-number>law, the right to be immune, while in the custody of persons acting under color of the laws of the State of Florida, from illegal assault and battery by any person exercising the authority of said State</blockquote>
<p id="b1095-7">as well as the right to be tried in accordance with due process of law, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#103" aria-description="Citation for case: Williams v. United States">341 U.S. at 103</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#580" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 580</a></span>, and the trial judge charged the jury that it could find Williams guilty if he beat the victim “for the purpose of imposing illegal summary punishment upon him” as well as if the beating was “for the purpose of forcing him to make a confession”. <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#104" aria-description="Citation for case: Williams v. United States">341 U.S. at 104</a></span>, <span class="citation" data-id="9420566"><a href="/opinion/104890/williams-v-united-states/#580" aria-description="Citation for case: Williams v. United States">71 S.Ct. at 580</a></span>. See also United States v. Price, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/#793" aria-description="Citation for case: United States v. Price">383 U.S. 787, 793</a></span>, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/" aria-description="Citation for case: United States v. Price">86 S.Ct. 1152</a></span>, <span class="citation" data-id="107202"><a href="/opinion/107202/united-states-v-price/" aria-description="Citation for case: United States v. Price">16 L.Ed.2d 267</a></span> (1966).</p>
</footnote>
<footnote label="6">
<p id="b1095-12">. The standard gains added content from other language in the opinion. The acts must do more than “offend some fastidious squeamishness or private sentimentalism about combatting crime too energetically”; they must be such as “to offend even hardened sensibilities,” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#172" aria-description="Citation for case: Rochin v. California">342 U.S. at 172</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#209" aria-description="Citation for case: Rochin v. California">72 S.Ct. at 209</a></span>, or constitute force that is “brutal” and “offensive to human dignity.” <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California">342 U.S. at 174</a></span>, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">72 S.Ct. 205</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b1095-13">. Even at common law “mere words, however violent, are held not to amount to an assault,” <em><span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">Id.</a></span> </em>§ 10, at 39.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Johnson v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Johnson v. United States"
type: case
citation: "333 U.S. 10 (1948)"
parallel_cite: "68 S. Ct. 367; 92 L. Ed. 2d 436; 92 L. Ed. 436"
neutral_cite: 1948 U.S. LEXIS 2583
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1948
date_decided: 1948-02-02
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1948-02-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Johnson v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/104504/johnson-v-united-states/"
  cluster_id: 104504
  opinion_id: 104504
  identity_checked: true
homes:
  - page: "[[The Neutral and Detached Magistrate]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[Coolidge v. New Hampshire]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "neutral-magistrate", "probable-cause"]
holding: "Probable-cause inferences must be drawn by a neutral and detached magistrate, not by the officer engaged in ferreting out crime."
lake:
  record_id: Johnson v. United States
  status: verified
  projected_at: 2026-07-06
---

# Johnson v. United States

*333 U.S. 10 (1948)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers, acting on an informant's tip, detected the distinctive odor of burning opium coming from a hotel room. Without a warrant, they knocked, entered when the occupant opened the door, arrested Johnson, and searched the room, finding opium and smoking apparatus. Johnson challenged the warrantless search.

## Issue
Whether officers who have probable cause may conduct a warrantless search of a home or hotel room, or whether the probable-cause determination must instead be made by a neutral magistrate issuing a warrant.

## Rule
The probable-cause inference must be drawn by a neutral magistrate, not the investigating officer. "The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." — 333 U.S. at 13–14. ^pin-13

"Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." — *Id.* at 14. ^pin-14

## Application
The opium odor may well have furnished probable cause, but the officers — not a magistrate — made that judgment and searched the room without a warrant. No exceptional circumstances excused the failure to obtain a warrant: there was no consent, no search incident to a valid arrest (the arrest itself depended on the entry), and no risk of evidence destruction shown. Because the officers, rather than a neutral magistrate, drew the probable-cause inference, the warrantless search was unreasonable.

## Conclusion
The warrantless search was invalid; the conviction resting on the seized evidence was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Johnson*'s neutral-and-detached-magistrate principle remains a cornerstone of the warrant requirement and is invoked across the modern Fourth Amendment cases, including [[Katz v. United States]] and [[Coolidge v. New Hampshire]].

## Appears on
- [[The Neutral and Detached Magistrate]] — *Key — Anchor*

## Sources
- *Johnson v. United States*, 333 U.S. 10 (1948) — https://www.courtlistener.com/opinion/104504/johnson-v-united-states/ — pinpoints: 13, 14.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0e54b48b86982a9a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Johnson v. United States"}, "payload": {"all": [{"cite": "333 U.S. 10", "page": "10", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "333"}, {"cite": "68 S. Ct. 367", "page": "367", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "68"}, {"cite": "92 L. Ed. 2d 436", "page": "436", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "1948 U.S. LEXIS 2583", "page": "2583", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1948"}, {"cite": "92 L. Ed. 436", "page": "436", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}], "display": "333 U.S. 10", "official": {"cite": "333 U.S. 10", "page": "10", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "333"}, "official_selection_present": true, "record_id": "Johnson v. United States"}}
{"assertion_id": "927d4ccc56e2effe", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-13", "record_id": "Johnson v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-13", "pinpoint_status": "slip-only", "quote": "--- # Johnson v. United States *333 U.S. 10 (1948)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers, acting on an informant's tip, detected the distinctive odor of burning opium coming from a hotel room. Without a warrant, they knocked, entered when the occupant opened the door, arrested Johnson, and searched the room, finding opium and smoking apparatus. Johnson challenged the warrantless search. ## Issue Whether officers who have probable cause may conduct a warrantless search of a home or hotel room, or whether the probable-cause determination must instead be made by a neutral magistrate issuing a warrant. ## Rule The probable-cause inference must be drawn by a neutral magistrate, not the investigating officer.", "quote_fidelity": "mismatch", "record_id": "Johnson v. United States", "star_marker": null}}
{"assertion_id": "d7d8c3a4066f9d7b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-14", "record_id": "Johnson v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-14", "pinpoint_status": "slip-only", "quote": "Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers.", "quote_fidelity": "mismatch", "record_id": "Johnson v. United States", "star_marker": null}}
{"assertion_id": "0c6280240a37cee0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Johnson v. United States"}, "payload": {"as_of_content": "1948-02-02", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Johnson v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Johnson v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Johnson v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Johnson v. United States",
    "case_name_short": "",
    "case_name_full": "Johnson v. United States",
    "input_case_name": "Johnson v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1948-02-02",
    "year": 1948,
    "docket": null,
    "cluster_id": 104504,
    "lead_opinion_id": 104504,
    "sibling_ids": [
      104504
    ],
    "absolute_url": "/opinion/104504/johnson-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8202565,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 8202381,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 104507,
        "score": 20,
        "case_name": "Johnson v. United States"
      },
      {
        "cluster_id": 8202305,
        "score": 20,
        "case_name": "Johnson v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "333 U.S. 10",
      "volume": "333",
      "reporter": "U.S.",
      "page": "10",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "68 S. Ct. 367",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 436",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 436",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1948 U.S. LEXIS 2583",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2583",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "333 U.S. 10",
        "volume": "333",
        "reporter": "U.S.",
        "page": "10",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 367",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 436",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1948 U.S. LEXIS 2583",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "2583",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 436",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "436",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "333 U.S. 10",
    "official_selection": {
      "court_class": "scotus",
      "selected": "333 U.S. 10",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-13",
      "page": null,
      "quote": "--- # Johnson v. United States *333 U.S. 10 (1948)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers, acting on an informant's tip, detected the distinctive odor of burning opium coming from a hotel room. Without a warrant, they knocked, entered when the occupant opened the door, arrested Johnson, and searched the room, finding opium and smoking apparatus. Johnson challenged the warrantless search. ## Issue Whether officers who have probable cause may conduct a warrantless search of a home or hotel room, or whether the probable-cause determination must instead be made by a neutral magistrate issuing a warrant. ## Rule The probable-cause inference must be drawn by a neutral magistrate, not the investigating officer.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-14",
      "page": null,
      "quote": "Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1948-02-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Johnson v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sorenson",
          "cluster_id": 4806437,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yee",
          "cluster_id": 3062319,
          "cite": [
            "177 So. 3d 72",
            "2015 Fla. App. LEXIS 15198",
            "2015 WL 5965213"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pyon v. State",
          "cluster_id": 2791489,
          "cite": [
            "222 Md. App. 412",
            "112 A.3d 1130",
            "2015 Md. App. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2792904,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grice",
          "cluster_id": 2772730,
          "cite": [
            "367 N.C. 753",
            "767 S.E.2d 312",
            "2015 N.C. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983813,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane1_negative"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brinegar v. United States",
          "cluster_id": 104716,
          "cite": [
            "93 L. Ed. 2d 1879",
            "69 S. Ct. 1302",
            "338 U.S. 160",
            "1949 U.S. LEXIS 2084"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
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
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Johnson v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(104504) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk0NDk2MDAwMDAwJnM9MjcwODgyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28104504%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(104504)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzk2JnM9MTExMzAxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28104504%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(104504)",
        "reviewed": 39,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 39,
        "triage_read": 0,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(104504)",
    "indexed_citing_opinions": 2463,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 104504,
        "count": 2463,
        "count_source": "search"
      }
    ],
    "citation_count": 3856,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/johnson-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MTA0Mzkmcz0xMDY4ODU2NyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28104504%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 104504,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 104490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 3994178,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 3998924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 104504,
        "cited_id": 4001986,
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
    "date_created": "2026-07-05T08:55:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T08:59:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:56:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Johnson v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b89-11">
  Mr. Justice Jackson
 </author>
<p id="AnP">
  delivered the opinion of the Court.
 </p>
<p id="b89-12">
  Petitioner was convicted on four counts charging violation of federal narcotic laws.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The only question which brings the case here is whether it was lawful, without a warrant of any kind, to arrest petitioner and to search her living quarters.
 </p>
<p id="b90-5">
<span citation-index="1" class="star-pagination" label="12"> 
   *12
   </span>
  Taking the Government’s version of disputed events, decision would rest on these facts:
 </p>
<p id="b90-6">
  At about 7:30 p. m. Detective Lieutenant Belland, an officer of the Seattle police force narcotic detail, received information from a confidential informer, who was also a known narcotic user, that unknown persons were smoking opium in the Europe Hotel. The informer was taken back to the hotel to interview the manager, but he returned at once saying he could smell burning opium in the hallway. Belland communicated with federal narcotic agents and between 8:30 and 9 o’clock went back to the hotel with four such agents. All were experienced in narcotic work and recognized at once a strong odor of burning opium which to them was distinctive and unmistakable. The odor led to Room 1. The officers did not know who was occupying that room. They knocked and a voice inside asked who was there. “Lieutenant Bel-land,” was the reply. There was a slight delay, some “shuffling or noise” in the room and then the defendant opened the door. The officer said, “I want to talk to you a little bit.” She then, as he describes it, “stepped back acquiescently and admitted us.” He said, “I want to talk to you about this opium smell in the room here.” She denied that there was such a smell. Then he said, “I want you to consider yourself under arrest because we are going to search the room.” The search turned up incriminating opium and smoking apparatus, the latter being warm, apparently from recent use. This evidence the District Court refused to suppress before trial and admitted over defendant’s objection at the trial. Conviction resulted and the Circuit Court of Appeals affirmed.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
</p>
<p id="b90-7">
  The defendant challenged the search of her home as a violation of the rights secured to her, in common with others, by the Fourth Amendment to the Constitution.
  <span citation-index="1" class="star-pagination" label="13"> 
   *13
   </span>
  The Government defends the search as legally justifiable, more particularly as incident to what it urges was a lawful arrest of the person.
 </p>
<p id="b91-5">
  I.
 </p>
<p id="b91-6">
  The Fourth Amendment to the Constitution of the United States provides:
 </p>
<blockquote id="b91-7">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b91-8">
  Entry to defendant’s living quarters, which was the beginning of the search, was demanded under color of office. It was granted in submission to authority rather than as an understanding and intentional waiver of a constitutional right. Cf.
  <em>
   Amos
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>.
 </p>
<p id="b91-9">
  At the time entry was demanded the officers were possessed of evidence which a magistrate might have found to be probable cause for issuing a search warrant. We cannot sustain defendant’s contention, erroneously made, on the strength of
  <em>
   Taylor
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">286 U. S. 1</a></span>, that odors cannot be evidence sufficient to constitute probable grounds for any search. That decision held only that odors alone do not authorize a search without warrant. If the presence of odors is testified to before a magistrate and he finds the affiant qualified to know the odor, and it is one sufficiently distinctive to identify a forbidden substance, this Court has never held such a basis insufficient to justify issuance of a search warrant. Indeed it might very well be found to be evidence of most persuasive character.
 </p>
<p id="b91-10">
  The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law en
  <span citation-index="1" class="star-pagination" label="14"> 
   *14
   </span>
  forcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Any assumption that evidence sufficient to support a magistrate’s disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people’s homes secure only in the discretion of police officers.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Crime, even in the privacy of one’s own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.
 </p>
<p id="b92-4">
  There are exceptional circumstances in which, on balancing the need for effective law enforcement against the
  <span citation-index="1" class="star-pagination" label="15"> 
   *15
   </span>
  right of privacy, it may be contended that a magistrate’s warrant for search may be dispensed with. But this is not such a case. No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the constitutional requirement. No suspect was fleeing or likely to take flight. The search was of permanent premises, not of a movable vehicle. No evidence or contraband was threatened with removal or destruction, except perhaps the fumes which we suppose in time would disappear. But they were not capable at any time of being reduced to possession for presentation to court. The evidence of their existence before the search was adequate and the testimony of the officers to that effect would not perish from the delay of getting a warrant.
 </p>
<p id="b93-5">
  If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, it is difficult to think of a case in which it should be required.
 </p>
<p id="b93-6">
  II.
 </p>
<p id="b93-7">
  The Government contends, however, that this search without warrant must be held valid because incident to an arrest. This alleged ground of validity requires examination of the facts to determine whether the arrest itself was lawful. Since it was without warrant, it could be valid only if for a crime committed in the presence of the arresting officer or for a felony of which he had reasonable cause to believe defendant guilty.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b94-5">
<span citation-index="1" class="star-pagination" label="16"> 
   *16
   </span>
  The Government, in effect, concedes that the arresting officer did not have probable cause to arrest petitioner until he had entered her room and found her to be the sole occupant.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  It points out specifically, referring to the time just before entry, “For at that time the agents did not know whether there was one or several persons in the room. It was reasonable to believe that the room might have been an opium smoking den.” And it says, “. . . that when the agents were admitted into the room and found only petitioner present they had a reasonable basis for believing that she had been smoking opium and thus illicitly possessed the narcotic.” Thus the Government quite properly stakes the right to arrest, not on the informer’s tip and the smell the officers recognized before entry, but on the knowledge that she was alone in the room, gained only after, and wholly by reason of, their entry of her home. It was therefore their observations inside of her quarters, after they had obtained admission under color of their police authority, on which they made the arrest.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
</p>
<p id="b94-6">
  Thus the Government is obliged to justify the arrest by the search and at the same time to justify the search by
  <span citation-index="1" class="star-pagination" label="17"> 
   *17
   </span>
  the arrest. This will not do. An officer gaining access to private living quarters under color of his office and of the law which he personifies must then have some valid basis in law for the intrusion. Any other rule would undermine “the right of the people to be secure in their persons, houses, papers, and effects,”
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  and would obliterate one of the most fundamental distinctions between our form of government, where officers are under the law, and the police-state where they are the law.
 </p>
<p id="b95-5">
<em>
   Reversed.
  </em>
</p>
<judges id="b95-6">
  The Chief Justice, Mr. Justice Black, Mr. Justice Reed and Mr. Justice Burton dissent.
 </judges>








<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b89-13">
   Two counts charged violation of § 2553 (a) of the Internal Revenue Code (<span class="citation no-link">26 U. S. C. § 2553</span> (a)) and two counts charged violation of the Narcotic Drugs Import and Export Act as amended (<span class="citation no-link">21 U. S. C. §174</span>).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b90-8">
   <span class="citation" data-id="6896359"><a href="/opinion/6997439/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">162 F. 2d 562</a></span>.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b92-5">
   In
   <em>
    United States
   </em>
   v.
   <em>
    Lefkowitz,
   </em>
   <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>, this Court said:
  </p>
<blockquote id="b92-6">
   . . the informed and deliberate determinations of magistrates empowered to issue warrants as to what searches and seizures are permissible under the Constitution are to be preferred over the hurried action of officers and others who may happen to make arrests. Security against unlawful searches is more likely to be attained by resort to search warrants than by reliance upon the caution and sagacity of petty officers while acting under the excitement that attends the capture of persons accused of crime. . . .”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b92-7">
   “Belief, however well founded, that an article sought is concealed in a dwelling house furnishes no justification for a search of that place without a warrant. And such searches are held unlawful notwithstanding facts unquestionably showing probable cause.”
   <em>
    Agnello
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b93-8">
   This is the Washington law.
   <em>
    State
   </em>
   v.
   <em>
    Symes,
   </em>
   <span class="citation" data-id="4724347"><a href="/opinion/4917761/state-v-symes/" aria-description="Citation for case: State v. Symes">20 Wash. 484</a></span>, <span class="citation" data-id="4724347"><a href="/opinion/4917761/state-v-symes/" aria-description="Citation for case: State v. Symes">55 P. 626</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Lindsey,
   </em>
   <span class="citation" data-id="4001986"><a href="/opinion/4225695/state-v-lindsey/" aria-description="Citation for case: State v. Lindsey">192 Wash. 356</a></span>, <span class="citation" data-id="4001986"><a href="/opinion/4225695/state-v-lindsey/" aria-description="Citation for case: State v. Lindsey">73 P. 2d 738</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Krantz,
   </em>
   <span class="citation" data-id="3998924"><a href="/opinion/4223178/state-v-krantz/" aria-description="Citation for case: State v. Krantz">24 Wash. 2d 350</a></span>, <span class="citation" data-id="3998924"><a href="/opinion/4223178/state-v-krantz/" aria-description="Citation for case: State v. Krantz">164 P. 2d 453</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Robbins,
   </em>
   <span class="citation" data-id="3994178"><a href="/opinion/4219303/state-v-robbins/" aria-description="Citation for case: State v. Robbins">25 Wash. 2d 110</a></span>, <span class="citation" data-id="3994178"><a href="/opinion/4219303/state-v-robbins/" aria-description="Citation for case: State v. Robbins">169 P. 2d 246</a></span>. State law determines the validity of arrests without warrant.
   <em>
    United States
   </em>
   v.
   <em>
    Di Re,
   </em>
   <span class="citation" data-id="104490"><a href="/opinion/104490/united-states-v-di-re/" aria-description="Citation for case: United States v. Di Re">332 U. S. 581</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b94-7">
   The Government brief states that the question presented is “Whether there was probable cause for the arrest of petitioner for possessing opium prepared for smoking and the search of her room in a hotel incident thereto for the contraband opium, where experienced narcotic agents unmistakably detected and traced the pungent, identifiable odor of burning opium emanating from her room and knew, before they arrested her, that she was the only person in. the room.”
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b94-8">
   The Government also suggests that “In a sense, the arrest was made in ‘hot pursuit.’ . . .” However, we find no element of “hot pursuit” in the arrest of one who was not in flight, was completely surrounded by agents before she knew of their presence, who claims without denial that she was in bed at the time, and who made no attempt to escape. Nor would these facts seem to meet the requirements of the Washington “Uniform Law on Fresh Pursuit.” Session Laws 1943, ch. 261.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b95-7">
   In
   <em>
    Gouled
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#304" aria-description="Citation for case: Gouled v. United States">255 U. S. 303, 304</a></span>, this Court said: “It would not be possible to add to the emphasis with which the framers of our Constitution and this court (in
   <em>
    Boyd
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, in
   <em>
    Weeks
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and in
   <em>
    Silver-thorne Lumber Co.
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>) have declared the importance to political liberty and to the welfare of our country of the due observance of the rights guaranteed under the Constitution by these two [Fourth and Fifth] Amendments. The effect of the decisions cited is: .that such rights are declared to be indispensable to the ‘full enjoyment of personal security, personal liberty and private property’; that they are to be regarded as of the very essence of constitutional liberty; and that the guaranty of them is as important and as imperative as are the guaranties of the other fundamental rights of the individual citizen, — the right, to trial by jury, to the writ of
   <em>
    habeas corpus
   </em>
   and to due process of law. It has been repeatedly decided that these Amendments should receive a liberal construction, so as to prevent stealthy encroachment upon or ‘gradual depreciation’ of the rights secured by them, by imperceptible practice of courts or by well-intentioned but mistakenly over-zealous executive officers.”
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Jones v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Jones v. United States"
type: case
citation: "362 U.S. 257 (1960)"
parallel_cite: "80 S. Ct. 725; 4 L. Ed. 2d 697; 78 A.L.R. 2d 233"
neutral_cite: 1960 U.S. LEXIS 1413
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-03-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1960-03-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Jones v. United States
  varies_by_point: false
  scope_note: "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106022/jones-v-united-states/"
  cluster_id: 106022
  opinion_id: 106022
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Historical / origin"
related: ["[[Rakas v. Illinois]]", "[[United States v. Salvucci]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "suppression", "historical"]
holding: "Established \"automatic standing\" for those charged with possessory offenses and the broader rule that anyone \"legitimately on the…"
lake:
  record_id: Jones v. United States
  status: verified
  projected_at: 2026-07-09
---

# Jones v. United States

*362 U.S. 257 (1960)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled by [[Rakas v. Illinois]] and [[United States v. Salvucci]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal narcotics agents executed a search warrant at an apartment belonging to Jones's friend Evans, where Jones was present with Evans's permission. The agents found narcotics and paraphernalia, and Jones was charged with federal possessory narcotics offenses. He moved to suppress, but the lower courts denied him standing because he asserted no ownership or possessory interest in the apartment or the seized items.

## Issue
Whether a defendant charged with a possessory offense, or a person who is legitimately on the premises searched, has standing to move to suppress evidence obtained in an allegedly unlawful search.

## Rule
Yes, on two independent grounds. First, automatic standing for those charged with possession: "In cases where the indictment itself charges possession, the defendant in a very real sense is revealed as a 'person aggrieved by an unlawful search and seizure' upon a motion to suppress evidence prior to trial." — 362 U.S. at 264. ^pin-264

Second, broader possessory-interest standing: "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him." — [*Id.* at 267](https://www.courtlistener.com/opinion/106022/jones-v-united-states/#:~:text=anyone%20legitimately%20on%20premises%20where). ^pin-267

## Application
Jones was charged with a possessory narcotics offense and was, by his own testimony, present in Evans's apartment with Evans's consent at the time of the search. Under either ground — the automatic standing flowing from the possessory charge, or his legitimate presence on the premises — Jones was a "person aggrieved" entitled to litigate the search, so he was entitled to have his motion to suppress adjudicated on the merits (the Court then sustained the warrant as adequately supported by corroborated hearsay).

## Conclusion
Jones had standing to contest the search; the lower courts erred in denying it. (On the merits the warrant was upheld and the conviction affirmed.) Both standing grounds announced here have since been overruled.

## Treatment & subsequent history
- **Status:** overruled *(as of 2026-06-30)* — **Historical** (tier 6).
- The "automatic standing" rule was **overruled by [[United States v. Salvucci]]** (1980) after *[[Simmons v. United States]]* removed the self-incrimination dilemma it was designed to cure.
- The "legitimately on premises" standing test was **disavowed by [[Rakas v. Illinois]]** (1978), which held that Fourth Amendment rights are personal and that standing turns on whether the defendant's **own** legitimate expectation of privacy was violated — not on mere lawful presence.

## Appears on
- [[Standing to Challenge a Search]] — *Historical / origin*

## Sources
- *Jones v. United States*, 362 U.S. 257 (1960) — https://www.courtlistener.com/opinion/106022/jones-v-united-states/ — pinpoints: 264, 267.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1ae9995d3fa05ccd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Jones v. United States"}, "payload": {"all": [{"cite": "362 U.S. 257", "page": "257", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "362"}, {"cite": "80 S. Ct. 725", "page": "725", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "4 L. Ed. 2d 697", "page": "697", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "4"}, {"cite": "1960 U.S. LEXIS 1413", "page": "1413", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1960"}, {"cite": "78 A.L.R. 2d 233", "page": "233", "reporter": "A.L.R. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "78"}], "display": "362 U.S. 257", "official": {"cite": "362 U.S. 257", "page": "257", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "362"}, "official_selection_present": true, "record_id": "Jones v. United States"}}
{"assertion_id": "1687c708552524c7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-264", "record_id": "Jones v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-264", "pinpoint_status": "slip-only", "quote": "--- # Jones v. United States *362 U.S. 257 (1960)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* — overruled by [[Rakas v. Illinois]] and [[United States v. Salvucci]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal narcotics agents executed a search warrant at an apartment belonging to Jones's friend Evans, where Jones was present with Evans's permission. The agents found narcotics and paraphernalia, and Jones was charged with federal possessory narcotics offenses. He moved to suppress, but the lower courts denied him standing because he asserted no ownership or possessory interest in the apartment or the seized items. ## Issue Whether a defendant charged with a possessory offense, or a person who is legitimately on the premises searched, has standing to move to suppress evidence obtained in an allegedly unlawful search. ## Rule Yes, on two independent grounds. First, automatic standing for those charged with possession:", "quote_fidelity": "mismatch", "record_id": "Jones v. United States", "star_marker": null}}
{"assertion_id": "98d065211961c525", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-267", "record_id": "Jones v. United States"}, "payload": {"fragment": "#:~:text=anyone%20legitimately%20on%20premises%20where", "page": null, "pin_id": "pin-267", "pinpoint_status": "star-verified", "quote": "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him.", "quote_fidelity": "matched", "record_id": "Jones v. United States", "star_marker": "267"}}
{"assertion_id": "2b60daf32b09a23f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Jones v. United States"}, "payload": {"as_of_content": "1960-03-28", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Jones v. United States", "scope_note": "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded.", "varies_by_point": false}}
```

### lake record — Jones v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Jones v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Jones v. United States",
    "case_name_short": "Jones",
    "case_name_full": "Jones v. United States",
    "input_case_name": "Jones v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-03-28",
    "year": 1960,
    "docket": null,
    "cluster_id": 106022,
    "lead_opinion_id": 106022,
    "sibling_ids": [
      106022
    ],
    "absolute_url": "/opinion/106022/jones-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8948768,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8948588,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8947339,
        "score": 20,
        "case_name": "Jones v. United States"
      },
      {
        "cluster_id": 8947221,
        "score": 20,
        "case_name": "Jones v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "362 U.S. 257",
      "volume": "362",
      "reporter": "U.S.",
      "page": "257",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 725",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "725",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 697",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "697",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 A.L.R. 2d 233",
        "volume": "78",
        "reporter": "A.L.R. 2d",
        "page": "233",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1413",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1413",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "362 U.S. 257",
        "volume": "362",
        "reporter": "U.S.",
        "page": "257",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 725",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "725",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 697",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "697",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1413",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1413",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 A.L.R. 2d 233",
        "volume": "78",
        "reporter": "A.L.R. 2d",
        "page": "233",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "362 U.S. 257",
    "official_selection": {
      "court_class": "scotus",
      "selected": "362 U.S. 257",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-264",
      "page": null,
      "quote": "--- # Jones v. United States *362 U.S. 257 (1960)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* \u2014 overruled by [[Rakas v. Illinois]] and [[United States v. Salvucci]] <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal narcotics agents executed a search warrant at an apartment belonging to Jones's friend Evans, where Jones was present with Evans's permission. The agents found narcotics and paraphernalia, and Jones was charged with federal possessory narcotics offenses. He moved to suppress, but the lower courts denied him standing because he asserted no ownership or possessory interest in the apartment or the seized items. ## Issue Whether a defendant charged with a possessory offense, or a person who is legitimately on the premises searched, has standing to move to suppress evidence obtained in an allegedly unlawful search. ## Rule Yes, on two independent grounds. First, automatic standing for those charged with possession:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-267",
      "page": null,
      "quote": "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him.",
      "star_marker": "267",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 23289,
      "fragment": "#:~:text=anyone%20legitimately%20on%20premises%20where",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1960-03-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Jones v. United States",
    "varies_by_point": false,
    "scope_note": "The 'automatic standing' rule was overruled by United States v. Salvucci (1980); the broad 'legitimately on premises' standing test was disavowed by Rakas v. Illinois (1978), which refocused standing on whether the defendant's own reasonable expectation of privacy was invaded.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Rakas v. Illinois",
          "cluster_id": 109953,
          "cite": "439 U.S. 128",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": "448 U.S. 83",
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:overruled"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. DeJesus",
          "cluster_id": 4860242,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
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
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Glover",
          "cluster_id": 4433034,
          "cite": [
            "872 F.3d 625",
            "2017 WL 4507530",
            "2017 U.S. App. LEXIS 19741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Glover",
          "cluster_id": 3190718,
          "cite": [
            "174 F. Supp. 3d 431",
            "2016 U.S. Dist. LEXIS 43260",
            "2016 WL 1273171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane1_negative"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Alford",
          "cluster_id": 108215,
          "cite": [
            "27 L. Ed. 2d 162",
            "91 S. Ct. 160",
            "400 U.S. 25",
            "1970 U.S. LEXIS 3",
            "56 Ohio Op. 2d 85"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguilar v. Texas",
          "cluster_id": 106865,
          "cite": [
            "12 L. Ed. 2d 723",
            "84 S. Ct. 1509",
            "378 U.S. 108",
            "1964 U.S. LEXIS 994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valley Forge Christian College v. Americans United for Separation of Church and State, Inc.",
          "cluster_id": 110599,
          "cite": [
            "70 L. Ed. 2d 700",
            "102 S. Ct. 752",
            "454 U.S. 464",
            "1982 U.S. LEXIS 22",
            "50 U.S.L.W. 4103"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bumper v. North Carolina",
          "cluster_id": 107716,
          "cite": [
            "20 L. Ed. 2d 797",
            "88 S. Ct. 1788",
            "391 U.S. 543",
            "1968 U.S. LEXIS 1470",
            "46 Ohio Op. 2d 382"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Jones v. United States:lane2_top_cited"
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
        "journal_ref": "Jones v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106022) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzI0MzM5MjAwMDAwJnM9NjE5MzM0JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106022%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106022)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMyJnM9MTA4NzYwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106022%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106022)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106022)",
    "indexed_citing_opinions": 3331,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106022,
        "count": 3331,
        "count_source": "search"
      }
    ],
    "citation_count": 4796,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/jones-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2NTk5MDMmcz05NDczODA1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106022%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106022,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 96569,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 101148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 105837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 226671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 230030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 231127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 233225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 235396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 243012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 246901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1471426,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1473427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1477422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1480436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1504217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1507600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1507641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106022,
        "cited_id": 1550051,
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
    "date_created": "2026-07-05T08:59:23Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T08:59:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Jones v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b316-7">
  Mr. Justice Frankfurter
 </author>
<p id="AJs">
  delivered the opinion of the Court.
 </p>
<p id="b316-8">
  This is a prosecution for violation of federal narcotics laws. In the first count of a two-count indictment petitioner was charged with having “purchased, sold, dispensed and distributed” narcotics in violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a), that is, not in or from the “original stamped package.” In the second count petitioner was charged under <span class="citation no-link">21 U. S. C. § 174</span> with having “facilitated the concealment and sale of” the same narcotics, knowing them to have been imported illegally into the United States. Petitioner was found guilty on both counts and sentenced to seven years’ imprisonment. The Court of Appeals, one judge dissenting, affirmed the conviction. 104 U. S. App. D. C. 345, <span class="citation" data-id="9446541"><a href="/opinion/246901/cecil-jones-v-united-states/" aria-description="Citation for case: Cecil Jones v. United States">262 F. 2d 234</a></span>. Since the case presented important questions in the administration of criminal justice, more particularly a defendant’s standing to challenge the legality of a search in the circumstances of this case, as well as the legality of the particular search should standing be established, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./359/988/">359 U. S. 988</a></span>.
 </p>
<p id="b316-9">
  Both statutory provisions under which petitioner was prosecuted permit conviction upon proof of the defendant’s possession of narcotics, and in the case of <span class="citation no-link">26 U. S. C. § 4704</span> (a) of the absence of the appropriate stamps. Possession was the basis of the Government’s case against petitioner. The evidence against him may be briefly summarized. He was arrested in an apartment in the District of Columbia by federal narcotics officers, who
  <span citation-index="1" class="star-pagination" label="259"> 
   *259
   </span>
  were executing a warrant to search for narcotics. Those officers found narcotics, without appropriate stamps, and narcotics paraphernalia in a bird’s nest in an awning just outside a window in the apartment. Another officer, stationed outside the building, had a short time before seen petitioner put his hand on the awning. Upon the discovery of the narcotics and the paraphernalia petitioner had admitted to the officers that some of these were his and that he was living in the apartment.
 </p>
<p id="b317-5">
  Prior to trial petitioner duly moved to suppress the evidence obtained through the execution of the search warrant on the ground that the warrant had been issued without a showing of probable cause. The Government challenged petitioner’s standing to make this motion because petitioner alleged neither ownership of the seized articles nor an interest in the apartment greater than that of an “invitee or guest.” The District Court agreed to take evidence on the issue of petitioner’s standing. Only petitioner gave evidence. On direct examination he testified that the apartment belonged to a friend, Evans, who had given him the use of it, and a key, with which petitioner had admitted himself on the day of the arrest. On cross-examination petitioner testified that he had a suit and shirt at the apartment, that his home was elsewhere, that he paid nothing for the use of the apartment, that Evans had let him use it “as a friend,” that he had slept there “maybe a night,” and that at the time of the search Evans had been away in Philadelphia for about five days.
 </p>
<p id="b317-6">
  Solely on the basis of petitioner’s lack of standing to make it, the district judge denied petitioner’s motion to suppress. When the case came on for trial before a different judge, the motion to suppress was renewed and was denied on the basis of the prior ruling. An unsuccessful objection was made when the seized items were offered in evidence at the trial.
 </p>
<p id="b318-3">
<span citation-index="1" class="star-pagination" label="260"> 
   *260
   </span>
  In affirming petitioner’s conviction the Court of Appeals agreed with the District Court that petitioner lacked standing, but proceeded to rule that even if it were to find that petitioner had standing, it would hold the evidence to have been- lawfully received. A challenge to the search which petitioner had not made in the District Court, namely, that the method of executing the warrant had been illegal, was considered by the Court of Appeals and rejected, while the contention petitioner had made below, that there had been insufficient cause to issue the warrant, was rejected without discussion.
 </p>
<p id="b318-4">
  The issue of petitioner’s standing is to be decided with reference to Rule 41 (e) of the Federal Rules of Criminal Procedure. This is a statutory direction governing the suppression of evidence acquired in violation of the conditions validating a search. It is desirable to set forth the Rule.
 </p>
<blockquote id="b318-5">
  “A person aggrieved by an unlawful search and seizure may move the district court for the district in which the property was seized for the return of the property and to suppress for use as evidence anything so obtained on the ground that (1) the property was illegally seized without warrant, or (2) the warrant is insufficient on its face, or (3) the property seized is not that described in the warrant, or (4) there was not probable cause for believing the existence of the grounds on which the warrant was issued, or (5) the warrant was illegally executed. The judge shall receive evidence on any issue of fact necessary to the decision of the motion. If the motion is granted the property shall be restored unless otherwise subject to lawful detention and it shall not be admissible in evidence at any hearing or trial. The motion to suppress evidence may also be made in the district where the trial is to be had. The motion shall be made before trial or hearing unless opportunity
  <span citation-index="1" class="star-pagination" label="261"> 
   *261
   </span>
  therefor did not exist or the defendant was not aware of the grounds for the motion, but the court in its discretion may entertain the motion at the trial or hearing.”
 </blockquote>
<p id="b319-5">
  In order to qualify as a “person aggrieved by an unlawful search and seizure” one must have been a victim of a search or seizure, one against whom the search was directed, as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else. Rule 41 (e) applies the general principle that a party will not be heard to claim a constitutional protection, unless he “belongs to the class for whose sake the constitutional protection is given.”
  <em>
   Hatch
  </em>
  v.
  <em>
   Reardon,
  </em>
  <span class="citation" data-id="96569"><a href="/opinion/96569/new-york-ex-rel-hatch-v-reardon/#160" aria-description="Citation for case: New York Ex Rel. Hatch v. Reardon">204 U. S. 152, 160</a></span>. The restrictions upon searches and seizures were obviously designed for protection against official invasion of privacy and the security of property. They are not exclusionary provisions against the admission of kinds of evidence deemed inherently unreliable or prejudicial. The exclusion in federal trials of evidence otherwise competent but gathered by federal officials in violation of the Fourth Amendment is a means for making effective the protection of privacy.
 </p>
<p id="b319-6">
  Ordinarily, then, it is entirely proper to require of one who seeks to challenge the legality of a search as the basis for suppressing relevant evidence that he allege, and if the allegation be disputed that he establish, that he himself was the victim of an invasion of privacy. But prosecutions like this one have presented a special problem. To establish “standing,” Courts of Appeals have generally required that the movant claim either to have owned or possessed the seized property or to have had a substantial possessory interest in the premises searched. Since narcotics charges like those in the present indictment may be established through proof solely of possession of narcotics, a defendant seeking to comply with what has
  <span citation-index="1" class="star-pagination" label="262"> 
   *262
   </span>
  been the conventional standing requirement has been forced to allege facts the proof of which would tend, if indeed not be sufficient, to convict him. At the least, such a defendant has been placed in the criminally tendentious position of explaining his possession of the premises. He has been faced, not only with the chance that the allegations made on the motion to suppress may be used against him at the trial, although that they may is by no means an inevitable holding, but also with the encouragement that he perjure himself if he seeks to establish “standing” while maintaining a defense to the charge of possession.
 </p>
<p id="b320-4">
  The dilemma that has thus been created for defendants in cases like this has been pointedly put by Judge Learned Hand:
 </p>
<blockquote id="b320-5">
  “Men may wince at admitting that they were the owners, or in possession, of contraband property; may wish at once to secure the remedies of a possessor, and avoid the perils of the part; but equivocation will not serve. If they come as victims, they must take on that role, with enough detail to cast them without question. The petitioners at bar shrank from that predicament; but they were obliged to choose one horn of the dilemma.”
  <em>
   Connolly
  </em>
  v.
  <em>
   Medalie,
  </em>
  <span class="citation" data-id="1504217"><a href="/opinion/1504217/connolly-v-medalie/#630" aria-description="Citation for case: Connolly v. Medalie">58 F. 2d 629, 630</a></span>.
 </blockquote>
<p id="b320-6">
  Following this holding, several Courts of Appeals have pinioned a defendant within this dilemma. See, e.
  <em>
   g., Scoggins
  </em>
  v.
  <em>
   United States,
  </em>
  92 U. S. App. D. C. 29-30, <span class="citation" data-id="231127"><a href="/opinion/231127/scoggins-v-united-states/#212" aria-description="Citation for case: Scoggins v. United States">202 F. 2d 211, 212</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Eversole,
  </em>
  <span class="citation" data-id="233225"><a href="/opinion/233225/united-states-v-eversole/#768" aria-description="Citation for case: United States v. Eversole">209 F. 2d 766, 768</a></span>;
  <em>
   Accardo
  </em>
  v.
  <em>
   United States,
  </em>
  101 U. S. App. D. C. 162, 163-164, <span class="citation" data-id="243012"><a href="/opinion/243012/anthony-m-accardo-v-united-states/#569" aria-description="Citation for case: Anthony M. Accardo v. United States">247 F. 2d 568, 569-570</a></span>;
  <em>
   Grainger
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="1473427"><a href="/opinion/1473427/grainger-v-united-states/" aria-description="Citation for case: Grainger v. United States">158 F. 2d 236</a></span>. A District Court has held otherwise.
  <em>
   United States
  </em>
  v.
  <em>
   Dean,
  </em>
  <span class="citation" data-id="6846493"><a href="/opinion/6949464/united-states-v-dean/#906" aria-description="Citation for case: United States v. Dean">50 F. 2d 905, 906</a></span> (D. C. Mass.). The Government urges us to follow the body of Court of Appeals’ decisions and to rule that the lower
  <span citation-index="1" class="star-pagination" label="263"> 
   *263
   </span>
  courts, including the courts below, have been right in barring a defendant in a case like this from challenging a search because of his failure, when making his motion to suppress, to allege either that he owned or possessed the property seized or that he had a possessory interest in the premises searched greater than the interest of an “invitee or guest.”
 </p>
<p id="b321-5">
  Judge Hand’s dilemma is not inescapable. It presupposes requirements of “standing” which we do not find compelling. Two separate lines of thought effectively sustain defendant’s standing in this case. (1) The same element in this prosecution which has caused a dilemma,
  <em>
   i. e.,
  </em>
  that possession both convicts and confers standing, eliminates any necessity for a preliminary showing of an interest in the premises searched or the property seized, which ordinarily is required when standing is challenged. (2) Even were this not a prosecution turning on illicit possession, the legally requisite interest in the premises was here satisfied, for it need not be as extensive a property interest as was required by the courts below.
 </p>
<p id="b321-6">
  As to the first ground, we are persuaded by this consideration : to hold to the contrary, that is, to hold that petitioner’s failure to acknowledge interest in the narcotics or the premises prevented his attack upon the search, would be to permit the Government to have the advantage of contradictory positions as a basis for conviction. Petitioner’s conviction flows from his possession of the narcotics at the time of the search. Yet the fruits of that search, upon which the conviction depends, were admitted into evidence on the ground that petitioner did not have possession of the narcotics at that time. The prosecution here thus subjected the defendant to the penalties meted out to one in lawless possession while refusing him the remedies designed for one in that situation. It is not consonant. with the amenities, to put it mildly, of the administration of criminal justice to sanction
  <span citation-index="1" class="star-pagination" label="264"> 
   *264
   </span>
  such squarely contradictory assertions of power by the Government. The possession on the basis of which petitioner is to be and was convicted suffices to give him standing under any fair and rational conception of the requirements of Rule 41 (e).
 </p>
<p id="b322-5">
  The Government’s argument to the contrary essentially invokes
  <em>
   elegantia juris.
  </em>
  In the interest of normal procedural orderliness, a motion to suppress, under Rule 41 (e),.must be made prior to trial, if the defendant then has knowledge of the grounds on which to base the motion. The Government argues that the defendant therefore must establish his standing to suppress the evidence at that time through affirmative allegations and may not wait to rest standing upon the Government’s case at the trial. This provision of Rule 41 (e), requiring the motion to suppress to be made before trial, is a crystallization of decisions of this Court requiring that procedure, and is designed to eliminate from the trial disputes over police conduct not immediately relevant to the question of guilt. See
  <em>
   Nardone
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341-342</a></span>;
  <em>
   Segurola
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101148"><a href="/opinion/101148/segurola-v-united-states/" aria-description="Citation for case: Segurola v. United States">275 U. S. 106</a></span>, 111—112;
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#34" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 34</a></span>;
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>. As codified, the rule is not a rigid one, for under Rule 41 (e)' “the court in its discretion may entertain the motion [to suppress] at the trial or hearing.” This qualification proves that we are dealing with carrying out an important social policy and not a narrow, finicky procedural requirement. This underlying policy likewise precludes application of the Rule so as to compel the injustice of an internally inconsistent conviction. In cases where the indictment itself charges possession, the defendant in a very real sense is revealed as a “person aggrieved by an unlawful search and seizure” upon a motion to suppress evidence prior to trial. Rule 41 (e) should not be applied to allow the Government to deprive the defendant of standing to bring a motion
  <span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
  to suppress by framing the indictment in general terms, while prosecuting for possession.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b323-5">
  As a second ground sustaining “standing” here we hold that petitioner’s testimony on the motion to suppress made out a sufficient interest in the premises to establish him as a “person aggrieved” by their search. That testimony established that at the time of the search petitioner was present in the apartment with the permission of Evans, whose apartment it was. The Government asserts that such an interest is insufficient to give standing. The Government does not contend that only ownership of the premises may confer standing. It would draw distinctions among various classes of possessors, deeming some, such as “guests” and “invitees” with only the “use” of the premises, to have too “tenuous” an interest although concededly having “some measure of control” through their “temporary presence,” while conceding that others, who in a “realistic sense, have dominion of the apartment” or who are “domiciled” there, have standing. Petitioner, it is insisted, by his own testimony falls in the former class.
 </p>
<p id="b323-6">
  While this Court has never passed upon the interest in the searched premises necessary to maintain a motion to suppress, the Government’s argument closely follows the prevailing view in the lower courts. They have denied standing to “guests” and “invitees” (e.
  <em>
   g., Gaskins
  </em>
  v.
  <em>
   United States,
  </em>
  95 U. S. App. D. C. 34, 35, <span class="citation" data-id="235396"><a href="/opinion/235396/ola-mary-gaskins-v-united-states/#48" aria-description="Citation for case: Ola Mary Gaskins v. United States">218 F. 2d 47, 48</a></span>;
  <em>
   Gibson
  </em>
  v.
  <em>
   United States,
  </em>
  80 U. S. App. D. C. 81, 84, <span class="citation" data-id="1507641"><a href="/opinion/1507641/gibson-v-united-states/#384" aria-description="Citation for case: Gibson v. United States">149 F. 2d 381, 384</a></span>;
  <em>
   In re Nassetta,
  </em>
  <span class="citation" data-id="1477422"><a href="/opinion/1477422/in-re-nassetta/" aria-description="Citation for case: In Re Nassetta">125 F. 2d 924</a></span>;
  <em>
   Jones
  </em>
  v.
  <em>
   United States,
  </em>
  104 U. S. App. D. C. 345, <span class="citation" data-id="9446541"><a href="/opinion/246901/cecil-jones-v-united-states/" aria-description="Citation for case: Cecil Jones v. United States">262 F. 2d 234</a></span>),
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  and employees, who though in “control” or “occupancy” lacked “possession”
  <em>
   (e. g., Connolly
  </em>
  v.
  <em>
   Medalie,
  </em>
  <span class="citation" data-id="1504217"><a href="/opinion/1504217/connolly-v-medalie/#630" aria-description="Citation for case: Connolly v. Medalie">58 F. 2d 629, 630</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Conoscente,
  </em>
  <span class="citation" data-id="1480436"><a href="/opinion/1480436/united-states-v-conoscente/" aria-description="Citation for case: United States v. Conoscente">63 F. 2d 811</a></span>). The necessary quantum of interest has been distinguished as being, variously, “ownership in or right to possession of the premises”
  <em>
   (e. g., Jeffers
  </em>
  v.
  <em>
   United States,
  </em>
  88 U. S. App. D. C. 58, 61, <span class="citation" data-id="9442748"><a href="/opinion/226671/jeffers-v-united-states/#501" aria-description="Citation for case: Jeffers v. United States">187 F. 2d 498, 501</a></span>, affirmed,
  <em>
   Jeffers
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>), the interest of a “lessee or licensee”
  <em>
   (United States
  </em>
  v.
  <em>
   De Bousi,
  </em>
  <span class="citation" data-id="1550051"><a href="/opinion/1550051/united-states-v-de-bousi/" aria-description="Citation for case: United States v. De Bousi">32 F. 2d 902</a></span>), or of one with “dominion”
  <em>
   (McMillan
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="1471426"><a href="/opinion/1471426/mcmillan-v-united-states/#60" aria-description="Citation for case: McMillan v. United States">26 F. 2d 58, 60</a></span>;
  <em>
   Steeber
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="230030"><a href="/opinion/230030/steeber-v-united-states/#617" aria-description="Citation for case: Steeber v. United States">198 F. 2d 615, 617</a></span>). We do not lightly depart from this course of decisions by the lower courts. We are persuaded, however, that it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical. Even in the area from which they derive, due consideration has led to the discarding of these distinctions in the homeland of the common law. See Occupiers’ Liability Act, 1957, 5 and 6 Eliz. 2, c. 31, carrying out Law Reform Committee, Third Report, Cmd. 9305. Distinctions such as those between “lessee,” “licensee,” “invitee” and “guest,” often only of gossamer strength, ought not to be determinative in fashioning procedures ultimately referable to constitutional safeguards.
 </p>
<p id="b324-6">
  We rejected such distinctions as inappropriate to the law of maritime torts in
  <em>
   Kermarec
  </em>
  v.
  <em>
   Compagnie Generate,
  </em>
  <span class="citation" data-id="105837"><a href="/opinion/105837/kermarec-v-compagnie-generale-transatlantique/#630" aria-description="Citation for case: Kermarec v. Compagnie Generale Transatlantique">358 U. S. 625, 630-632</a></span>. We found there to be a duty of ordinary care to one rightfully on the ship, regardless of whether he was a “licensee” rather than an “invitee.” “For the admiralty law at this late date to import such conceptual distinctions would be foreign to its traditions
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  of simplicity and practicality.” <span class="citation" data-id="105837"><a href="/opinion/105837/kermarec-v-compagnie-generale-transatlantique/#631" aria-description="Citation for case: Kermarec v. Compagnie Generale Transatlantique">358 U. S., at 631</a></span>.
  <em>
   A forti-ori
  </em>
  we ought not to bow to them in the fair administration of the criminal law. To do so would not comport with our justly proud claim of the procedural protections accorded to those charged with crime. No just interest of the Government in the effective and rigorous enforcement of the criminal law will be hampered by recognizing that anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him. This would of course not avail those who, by virtue of their wrongful presence, cannot invoke the privacy of the premises searched. As petitioner’s testimony established Evans’ consent to his presence in the apartment, he was entitled to have the merits of his motion to suppress adjudicated.
 </p>
<p id="b325-5">
  We come to consider the grounds upon which the search is alleged to have been illegal. The attack which was made in the District Court was one of lack of probable cause for issuing the search warrant. The question raised is whether sufficient evidence to establish probable cause to search was put before the Commissioner by the officer, Didone, who applied for the warrant. The sole evidence upon which the warrant was issued was an affidavit signed by Didone. Both parties urge us to decide the question here, without remanding it to the District Court which, because it found lack of standing, did not pass on it. We think it appropriate to decide the question.
 </p>
<p id="b325-6">
  The affidavit is set out in the margin.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Didone was a member of the Narcotic Squad in the District of Columbia.
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  His affidavit claimed no direct knowledge of the presence of narcotics in the apartment. He swore that on the day before making the affidavit he had been given information, by one unnamed, that petitioner and another “were involved in the illicit narcotic traffic” and “kept a ready supply of heroin on hand” in the apartment. He swore that his informant claimed to have purchased narcotics at the apartment from petitioner and another “on many occasions,” the last of which had been the day before the warrant was applied for. Didone swore that his informant “has given information to the undersigned on previous occasion and which was correct,” that “[t]his same
  <span citation-index="1" class="star-pagination" label="269"> 
   *269
   </span>
  information” regarding petitioner had been given the narcotic squad by “other sources of information” and that the petitioner and the other implicated by the informant had admitted being users of narcotics. On this basis Didone founded his oath that he believed “that there is now illicit narcotic drugs being secreated [sic] in the above apartment by Cecil Jones.”
 </p>
<p id="b327-5">
  This affidavit was, it is claimed, insufficient to establish probable cause because it did not set forth the affiant’s personal observations regarding the presence of narcotics in the apartment, but rested wholly on hearsay. We held in
  <em>
   Nathanson
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>, that an affidavit does not establish probable cause which merely states the affiant’s belief that there is cause to search, without stating facts upon which that belief is based.
  <em>
   A fortiori
  </em>
  this is true of an affidavit which states only the belief of one not the affiant. That is not, however, this case. The question here is whether an affidavit which sets out personal observations relating to the existence of cause to search is to be deemed insufficient by virtue of the fact that it sets out not the affiant’s observations but those of another. An affidavit is not to be deemed insufficient on that score, so long as a substantial basis for crediting the hearsay is presented.
 </p>
<p id="b327-6">
  In testing the sufficiency of probable cause for an officer’s action even without a warrant, we have held that he may rely upon information received through an informant, rather than upon his direct observations, so long as the informant’s statement is reasonably corroborated by other matters within the officer’s knowledge.
  <em>
   Draper
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. We there upheld an arrest without a warrant solely upon an informant’s statement that the defendant was peddling narcotics, as corroborated by the fact that the informant’s description of the defendant’s appearance, and of where he would be on a given morning (matters in themselves totally
  <span citation-index="1" class="star-pagination" label="270"> 
   *270
   </span>
  innocuous) agreed with the officer’s observations. We rejected the contention that an officer may act without a warrant only when his basis for acting would be competent evidence upon a trial to prove defendant’s guilt. Quoting from
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#172" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 172</a></span>, we said that such a contention “goes much too far in-confusing and disregarding the difference between what is required to prove guilt in a criminal case and what is required to show probable cause for arrest or search. . . . There is a large difference between the two things to be proved [guilt and probable cause] . . . and therefore a like difference in the
  <em>
   quanta
  </em>
  and modes of proof required to establish them.” 358 U. S., at 311-312. The dictum to the contrary in
  <em>
   Grau
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/#128" aria-description="Citation for case: Grau v. United States">287 U. S. 124, 128</a></span>, was expressly rejected in
  <em>
   Draper.
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#312" aria-description="Citation for case: Draper v. United States">358 U. S., at 312, n. 4</a></span>. See also Judge Learned Hand in.
  <em>
   United States
  </em>
  v.
  <em>
   Heitner,
  </em>
  <span class="citation" data-id="1507600"><a href="/opinion/1507600/united-states-v-heitner/#106" aria-description="Citation for case: United States v. Heitner">149 F. 2d 105, 106</a></span>.
 </p>
<p id="b328-6">
  What we have ruled in the case of an officer who acts without a warrant governs our decision here. If an officer may act upon probable cause without a warrant when the only incriminating evidence in his possession is hearsay, it would be incongruous to hold that such evidence presented in an affidavit is insufficient basis for a warrant. If evidence of a more judicially competent or persuasive character than would have justified an officer in acting on his own without a warrant must be presented when a warrant is sought, warrants could seldom legitimatize police conduct, and resort to them would ultimately be discouraged. Due regard for the safeguards governing arrests and searches counsels the contrary. In a doubtful case, when the officer does not have clearly convincing evidence of the immediate need to search, it is most important that resort be had to a warrant, so that the evidence in the possession of the police may be weighed by an independent judicial officer, whose decision, not that
  <span citation-index="1" class="star-pagination" label="271"> 
   *271
   </span>
  of the police, may govern whether liberty or privacy is to be invaded.
 </p>
<p id="b329-5">
  We conclude therefore that hearsay may be the basis for a warrant. We cannot say that there was so little basis for accepting the hearsay here that the Commissioner acted improperly. The Commissioner need not have been convinced of the presence of narcotics in the apartment. He might have found the affidavit insufficient and withheld his warrant. But there was substantial basis for him to conclude that narcotics were probably present in the apartment, and that is sufficient. It is not suggested that the Commissioner doubted Didone’s word. Thus we may assume that Didone had the day before been told, by one who claimed to have bought narcotics there, that petitioner was selling narcotics in the apartment. Had that been all, it might not have been enough; but Didone swore to a basis for accepting the informant’s story. The informant had previously given accurate information. His story was corroborated by other sources of information. And petitioner was known by the police to be a user of narcotics. Corroboration through other sources of information reduced the chances of a reckless or prevaricating tale; that petitioner was a known user of narcotics made the charge against him much less subject to scepticism than would be such a charge against one without such a history.
 </p>
<p id="b329-6">
  Petitioner argues that the warrant was defective because Didone’s informants were not produced, because his affidavit did not even state their names, and Didone did not undertake and swear to the results of his own independent investigation of the claims made by his informants. If the objections raised were that Didone had misrepresented to the Commissioner his basis for seeking a warrant, these matters might be relevant. Such a charge is not made. All we are here asked to decide is
  <span citation-index="1" class="star-pagination" label="272"> 
   *272
   </span>
  whether the Commissioner acted properly, not whether Didone did. We have decided that, as hearsay alone does not render an affidavit insufficient, the Commissioner need not have required the informants or their affidavits to be produced, or that Didone have personally made inquiries about the apartment, so long as there was a substantial basis for crediting the hearsay.
 </p>
<p id="b330-5">
  In the Court of Appeals petitioner presented an additional attack upon the legality of the search, namely, that the warrant was not executed in conformity with <span class="citation no-link">18 U. S. C. § 3109</span>.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Since petitioner did not, with ample opportunity to do so, make this claim in the District Court, we should not ordinarily consider it here had the Court of Appeals refused for that reason to entertain it. The Court of Appeals, however, fully considered the claim and rejected it; nor does the Government contend that it is not properly before us. In these circumstances we hold that the question of the legality of the execution of the search warrant under <span class="citation no-link">18 U. S. C. § 3109</span> is open for our decision.
 </p>
<p id="b330-6">
  Unlike the claim of lack of probable cause, this contention is not one which can satisfactorily be resolved upon the record before us. As
  <em>
   Miller
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span>, demonstrated, a claim under <span class="citation no-link">18 U. S. C. § 3109</span> depends upon the particular circumstances surrounding the execution of the warrant. The trial revealed a direct conflict in testimony on this matter. We cannot yield to the Government’s suggestion that we ignore that conflict and consider the question on the version of the warrant's execution given at the trial most favorable to the prosecution. We therefore vacate the
  <span citation-index="1" class="star-pagination" label="273"> 
   *273
   </span>
  decision of the Court of Appeals and remand the case to the District Court to consider petitioner’s contention under <span class="citation no-link">18 U. S. C. § 3109</span>, in light of our decision that petitioner had standing to make it.
 </p>
<p id="b331-5">
<em>
   Vacated and remanded.
  </em>
</p>
<author id="b331-6">
  Mr. Justice Douglas.
 </author>
<p id="b331-7">
  I join the part of the opinion which holds that petitioner had “standing” to challenge the legality of the search. But I dissent from the ruling that there was “probable cause” for issuance of the warrant. The view that there was “probable cause” finds some support in
  <em>
   Draper
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. But my dissent in
  <em>
   <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span>
  </em>
  gives, I think, the true dimensions of the problem. This is an age where faceless informers have been reintroduced into our society in alarming ways. Sometimes their anonymity is defended on the ground that revelation of their names would ruin counter-espionage or cripple an underground network of agents. Yet I think in these Fourth Amendment cases the duty of the magistrate is nondelegable. It is not sufficient that the police think there is cause for an invasion of the privacy of the home. The judicial officer must also be convinced; and to him the police must go except for emergency situations. The magistrate should know the evidence on which the police propose to act. Unless that is the requirement, unless the magistrate makes his independent judgment on all the known facts, then he tends to become merely the tool of police interests. Though the police are honest and their aims worthy, history shows they are not appropriate guardians of the privacy which the Fourth Amendment protects.
 </p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b323-7">
   Ordinarily the Government should choose between opposing a motion to suppress made before trial and basing the case upon possession, but if necessary the District Court’s discretion to hear the motion to suppress during trial may be invoked. The Government must, in any case, not permit a conviction to be obtained on the basis of possession, without the merits of a duly made motion to suppress having been considered.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b325-7">
   “Affidavit in Support of a U. S. Commissioners Search Warrant for Premises 1436 Meridian Place, N. W., Washington, D. C., apartment 36, including window spaces of said apartment. Occupied by Cecil Jones and Earline Richardson.
  </p>
<p id="b325-8">
   “In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline
   <span citation-index="1" class="star-pagination" label="268"> 
    *268
    </span>
   Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [sic] in the above mentioned places. The last time being August 20, 1967.
  </p>
<p id="b326-7">
   “Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.
  </p>
<p id="b326-8">
   “This same information, regarding the illicit narcotic traffic, conducted by Cecil Jones and Earline Richardson, has been given to the undersigned and to other officers of the narcotic squad by other sources of information.
  </p>
<p id="b326-9">
   “Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [sic] in the above apartment by Cecil Jones and Earline Richardson.
  </p>
<p id="b326-10">
   “Det. Thomas Didone, Jr., Narcotic Squad, MPDC.
  </p>
<p id="b326-11">
   “Subscribed and sworn to before me this 21 day of August, 1957.
  </p>
<p id="b326-12">
   “James F. Splain, TJ. S. Commissioner, D. C.”
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b330-7">
   “The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance or when necessary to liberate himself or a person aiding him in the execution of the warrant.”
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Kalkines v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Kalkines v. United States"
type: case
citation: ""
parallel_cite: "200 Ct. Cl. 570; 473 F.2d 1391; 1973 U.S. Ct. Cl. LEXIS 11"
neutral_cite: ""
court: U.S. Court of Claims
court_level: other
circuit: ""
year: 1973
date_decided: 1973-02-16
docket: ""
authority_weight: Historical
treatment:
  field_i_validity: good_law
  as_of_content: 1973-02-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Kalkines v. United States
  varies_by_point: false
  scope_note: "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/8615714/kalkines-v-united-states/"
  cluster_id: 8615714
  opinion_id: 8594616
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Progeny / Refinement"
related: ["[[Garrity v. New Jersey]]", "[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "kalkines-warning", "federal-employee"]
holding: "A federal employee may be discharged for refusing to answer narrowly job-related questions only if first adequately advised both that refusal subjects him to discharge and that his answers (and their fruits) cannot be used against him in a criminal case — the 'Kalkines warning.'"
lake:
  record_id: Kalkines v. United States
  status: verified
  projected_at: 2026-07-06
---

# Kalkines v. United States

*473 F.2d 1391 (Ct. Cl. 1973)* · U.S. Court of Claims · **Binding in-circuit — Fed. Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
George Kalkines, an import specialist with the Bureau of Customs, was investigated for allegedly accepting a bribe, with a criminal grand-jury investigation proceeding concurrently with the agency's administrative inquiry. At four interviews he declined to answer certain questions about his finances and the performance of his duties. The agency discharged him for failing to answer work-related questions in violation of Customs and Treasury manuals, and the Civil Service Commission affirmed. Kalkines sued, contending he had never been adequately assured that his answers could not be used against him in the pending criminal matter.

## Issue
Whether a federal employee may be discharged for refusing to answer questions about the performance of his duties when he was not adequately advised that he must answer or face discharge, and that his answers and their fruits could not be used against him in a criminal prosecution.

## Rule
A public employee cannot be fired merely for invoking the privilege: "It is now settled that the individual cannot be discharged simply because he invokes his Fifth Amendment privilege against self-incrimination in refusing to respond." — 473 F.2d at 1393 (200 Ct. Cl. at 574). ^pin-1393a

But he can be compelled to answer under a sufficient warning: "[A] governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case." — *Id.* ^pin-1393

## Application
Throughout the interviews Kalkines faced a concurrent criminal bribery investigation, so the protection against criminal use of his answers was critical. On none of the four occasions was he adequately advised both that refusal would subject him to discharge and that his answers (and their fruits) could not be used against him criminally — the agent's most explicit statement omitted the "fruits" protection and never properly brought home that he would have immunity. Because the required warning was not given, Kalkines's refusals did not violate the duty-to-answer regulations, and his discharge on that ground was invalid.

## Conclusion
Kalkines's removal could not stand, because he was discharged for refusing to answer without first receiving the constitutionally adequate assurance of immunity. The decision establishes the federal "Kalkines warning" implementing *[[Garrity v. New Jersey|Garrity]]* and *[[Gardner v. Broderick|Gardner]]* for federal employees.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — Fed. Cir.**
- *Kalkines* is good law; the "Kalkines warning" it articulates is the standard federal-employer advisement when compelling job-related answers. It implements [[Garrity v. New Jersey]] and [[Gardner v. Broderick]] (and parallels [[Lefkowitz v. Turley]]). As a U.S. Court of Claims decision, its precedent binds in the Federal Circuit.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Progeny / Refinement*

## Sources
- *Kalkines v. United States*, 473 F.2d 1391 (Ct. Cl. 1973) (200 Ct. Cl. 570) — https://www.courtlistener.com/opinion/8615714/kalkines-v-united-states/ — pinpoints: 473 F.2d 1393 (200 Ct. Cl. 574). (CourtListener copy carries Ct. Cl. star-pagination.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd17f13bc906aac4", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Kalkines v. United States"}, "payload": {"all": [{"cite": "200 Ct. Cl. 570", "page": "570", "reporter": "Ct. Cl.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "200"}, {"cite": "473 F.2d 1391", "page": "1391", "reporter": "F.2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "473"}, {"cite": "1973 U.S. Ct. Cl. LEXIS 11", "page": "11", "reporter": "U.S. Ct. Cl. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "1973"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Kalkines v. United States"}}
{"assertion_id": "478cd6921306a489", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1393", "record_id": "Kalkines v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1393", "pinpoint_status": "slip-only", "quote": "[A] governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case.", "quote_fidelity": "mismatch", "record_id": "Kalkines v. United States", "star_marker": null}}
{"assertion_id": "4fa6f06e50394bd7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1393a", "record_id": "Kalkines v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1393a", "pinpoint_status": "slip-only", "quote": "--- # Kalkines v. United States *473 F.2d 1391 (Ct. Cl. 1973)* · U.S. Court of Claims · **Binding in-circuit — Fed. Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background George Kalkines, an import specialist with the Bureau of Customs, was investigated for allegedly accepting a bribe, with a criminal grand-jury investigation proceeding concurrently with the agency's administrative inquiry. At four interviews he declined to answer certain questions about his finances and the performance of his duties. The agency discharged him for failing to answer work-related questions in violation of Customs and Treasury manuals, and the Civil Service Commission affirmed. Kalkines sued, contending he had never been adequately assured that his answers could not be used against him in the pending criminal matter. ## Issue Whether a federal employee may be discharged for refusing to answer questions about the performance of his duties when he was not adequately advised that he must answer or face discharge, and that his answers and their fruits could not be used against him in a criminal prosecution. ## Rule A public employee cannot be fired merely for invoking the privilege:", "quote_fidelity": "mismatch", "record_id": "Kalkines v. United States", "star_marker": null}}
{"assertion_id": "5326af6f217a7926", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Kalkines v. United States"}, "payload": {"as_of_content": "1973-02-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Kalkines v. United States", "scope_note": "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States).", "varies_by_point": false}}
```

### lake record — Kalkines v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Kalkines v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Kalkines v. United States",
    "case_name_short": "Kalkines",
    "case_name_full": "GEORGE KALKINES v. United States",
    "input_case_name": "Kalkines v. United States",
    "court": "U.S. Court of Claims",
    "court_id": "cc",
    "court_level": "other",
    "circuit": null,
    "state": null,
    "date_decided": "1973-02-16",
    "year": 1973,
    "docket": null,
    "cluster_id": 8615714,
    "lead_opinion_id": 8594616,
    "sibling_ids": [
      8594616
    ],
    "absolute_url": "/opinion/8615714/kalkines-v-united-states/",
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
        "cite": "200 Ct. Cl. 570",
        "volume": "200",
        "reporter": "Ct. Cl.",
        "page": "570",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "473 F.2d 1391",
        "volume": "473",
        "reporter": "F.2d",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. Ct. Cl. LEXIS 11",
        "volume": "1973",
        "reporter": "U.S. Ct. Cl. LEXIS",
        "page": "11",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "200 Ct. Cl. 570",
        "volume": "200",
        "reporter": "Ct. Cl.",
        "page": "570",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "473 F.2d 1391",
        "volume": "473",
        "reporter": "F.2d",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. Ct. Cl. LEXIS 11",
        "volume": "1973",
        "reporter": "U.S. Ct. Cl. LEXIS",
        "page": "11",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:Ct. Cl."
    }
  },
  "pinpoints": [
    {
      "id": "pin-1393a",
      "page": null,
      "quote": "--- # Kalkines v. United States *473 F.2d 1391 (Ct. Cl. 1973)* \u00b7 U.S. Court of Claims \u00b7 **Binding in-circuit \u2014 Fed. Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background George Kalkines, an import specialist with the Bureau of Customs, was investigated for allegedly accepting a bribe, with a criminal grand-jury investigation proceeding concurrently with the agency's administrative inquiry. At four interviews he declined to answer certain questions about his finances and the performance of his duties. The agency discharged him for failing to answer work-related questions in violation of Customs and Treasury manuals, and the Civil Service Commission affirmed. Kalkines sued, contending he had never been adequately assured that his answers could not be used against him in the pending criminal matter. ## Issue Whether a federal employee may be discharged for refusing to answer questions about the performance of his duties when he was not adequately advised that he must answer or face discharge, and that his answers and their fruits could not be used against him in a criminal prosecution. ## Rule A public employee cannot be fired merely for invoking the privilege:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1393",
      "page": null,
      "quote": "[A] governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-02-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Kalkines v. United States",
    "varies_by_point": false,
    "scope_note": "Good law; the 'Kalkines warning' remains the governing standard for compelling federal employees to answer job-related questions. A U.S. Court of Claims decision; its precedent was adopted as binding by the Federal Circuit (South Corp. v. United States).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "John P. Mack v. United States of America, Federal Bureau of Investigation, Defendants",
          "cluster_id": 484948,
          "cite": [
            "814 F.2d 120",
            "1987 U.S. App. LEXIS 4041",
            "43 Empl. Prac. Dec. (CCH) 37,032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
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
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meyer Kama v. Alejandro Mayorkas",
          "cluster_id": 10006780,
          "cite": [
            "107 F.4th 1054"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sergio Luna v. Department of Homeland Security",
          "cluster_id": 9459217,
          "cite": [
            "2024 MSPB 2"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michelle Shows v. Department of the Treasury",
          "cluster_id": 10743161,
          "cite": [
            "2025 MSPB 5"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Use of Polygraph Examinations in Investigating Disclosure of Information About Pending Criminal Investigations",
          "cluster_id": 4342987,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Kalkines v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(8594616) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus)",
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
        "query": "cites:(8594616)",
        "reviewed": 6,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(8594616)",
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
    "complete_query": "cites:(8594616)",
    "indexed_citing_opinions": 6,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 8594616,
        "count": 6,
        "count_source": "search"
      }
    ],
    "citation_count": 59,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/kalkines-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 6,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T09:03:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Ct. Cl.",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T09:04:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T09:03:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Kalkines v. United States

```
<opinion type="majority">
<author id="b604-7">Davis, <em>Judge,</em></author>
<p id="Aq--">delivered the opinion of the court:</p>
<p id="b604-8">Plaintiff George Kalkines worked for the Bureau of Customs of the Treasury Department from November 1960 until his suspension in June 1968, rising from an initial rating of GS-7 to the position of import specialist, GS-1'3. His suspension and subsequent discharge came about because of his alleged failure, in violation of the Customs Manual, the Customs Personnel Manual, and the Treasury Personnel Manual,<footnotemark>1</footnotemark> to answer questions put to him by the Bureau of Customs relating to the performance of his duties. According to management, this failure occurred at four separate interviews, three in New York and one in Washington, each listed as an individual specification of the charge. The agency sustained his removal on this charge, upholding each of the four specifications.<footnotemark>2</footnotemark> The Civil Service Commission affirmed. The validity of this determination is brought before us by the parties’ cross-motions for summary judgment, both of <page-number citation-index="1" label="573">*573</page-number>which invoke the administrative record on which we rest for onr decision.<footnotemark>3</footnotemark></p>
<p id="b605-6">In November 1967 the Burean of Customs began an investigation sparked by information saying that plaintiff had accepted a $200 payment from an importer’s representative in return for favorable treatment on valuation of a customs entry. The inquiry initially disclosed that plaintiff had had lunch with the representative on November 16th and had made a $400 deposit in his personal bank account on November 17th. He was then visited or summoned by customs agents (acting as investigatory arms of the Bureau) on several occasions, at four of which (November 28,1967, May 2, 1968, May 8, 1968, all in New York, and June 5, 1968, in Washington) he did not answer, or indicated that he would not answer, certain questions relating to the $400 deposit, his finances, and some aspects of the performance of his customs duties. At other interviews he did answer the queries then put to him. Plaintiff’s defense is that his failure to reply at the four specified times was excusable and justifiable in each instance, and therefore not contrary to the directives cited in footnote 1, <em>supra.</em></p>
<p id="b605-7">The most important fact bearing on the propriety of Mr. Kalkines’ conduct at the interviews is that, for all or most of the time, a criminal investigation was being carried on concurrently with the civil inquiry connected with possible disciplinary proceedings against him. The United States Attorney’s Office had been informed about the possible bribery before the customs agents’ first interview with plaintiff, and it became active in investigating the matter in December 1967; witnesses were subpoenaed to, and did, testify before the grand jury. This criminal inquest continued until well into the spring of 1968, and perhaps even longer. Plaintiff was never indicted, the United States Attorney ultimately declining prosecution, but Mr. Kalkines saw the Damoclean sword poised overhead during the entire period with which we are concerned.</p>
<p id="b606-4"><page-number citation-index="1" label="574">*574</page-number>In recent years the courts have given more precise content to the obligations of a public employee to answer his employer’s work-related questions where, as here, there is a substantial risk that the employee may be subject to prosecution for actions connected with the subject of management’s inquiry. It is now settled that the individual cannot be discharged simply because he invokes his Fifth Amendment privilege against self-incrimination in refusing to respond. <em>Gardner </em>v. Broderick, <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">392 U.S. 273</a></span> (1968); <em>Uniformed Sanitation Men Ass'n </em>v. <em>Commissioner of </em>Sanitation, <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U.S. 280</a></span> (1968). Conversely, a later prosecution cannot constitutionally use statements (or their fruits) coerced from the employee — in an earlier disciplinary investigation or proceeding — by a threat of removal from office if he fails to answer the question. <em>Garrity </em>v. <em>New </em>Jersey, <span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span> (1967). But a governmental employer is not wholly barred from insisting that relevant information be given it; the public servant can be removed for not replying if he is adequately informed both that he is subject to discharge for not answering and that his replies (and their fruits) cannot be employed against him in a criminal case. <em>See Gardner </em>v. <span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Broderick, <em>supra, </em></a></span>392 U.S. at 278; <em>Uniformed Sanitation Men Ass’n </em>v. <em>Commissioner of Sanitation, supra, </em>392 U.S. at 283, 284, 285 [hereafter cited as <em>Uniformed Sanitation Men </em>I] ; <em>Uniformed Sanitation Men Ass'n </em>v. <em>Commissioner of Sanitation, </em><span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d 619</a></span> (C.A. 2, 1970), <em>cert. denied, </em><span class="citation multiple-matches"><a href="/c/U.S./406/961/">406 U.S. 961</a></span> (1972) [hereafter cited as <em>Uniformed Sanitation Men </em>II].</p>
<p id="b606-5">This requirement for a sufficient warning to the employee, before questioning, was foreshadowed by the Supreme Court in <em>Uniformed Sanitation Men I, </em>and has been set forth more exactly by the Second Circuit in <em>Uniformed Sanitation Men II. </em>The highest court said that public employees “subject themselves to dismissal if they refuse to account for their performance of their public trust, after proper proceedings, which do not involve an attempt to coerce them to relinquish their constitutional rights.” 392 U.S. at 285. “Proper proceedings” of that type means, according to Chief Judge Friendly in <em>Uniformed Sanitation Men II, </em>inquiries, such <page-number citation-index="1" label="575">*575</page-number>as were held in that case,<footnotemark>4</footnotemark> “in which the employee is asked only pertinent questions about the performance of his duties <em>and is duly advised of his options and the consequences of his </em>choice.” <span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#627" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 627</a></span> (emphasis added). The same opinion said: “To require a public body to continue to keep an officer or employee who refuses to answer pertinent questions concerning his official conduct, <em>although assured of protection against use of his answers or their fruits in any criminal </em>prosecution, would push the constitutional protection beyond its language, its history or any conceivable purpose of the framers of the Bill of Rights.” <span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#626" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 626</a></span> (emphasis added). We think that the general directives of the various Treasury and Customs manuals (footnote 1, <em>supra) </em>should be read with this specific gloss supplied by the <em>Uniformed Sanitation Men </em>opinions.</p>
<p id="b607-6">The only issue we need address is whether plaintiff was “duly advised of his options and the consequences of his choice” and was adequately “assured of protection against use of his answers or their fruits in any criminal prosecution.” For the reasons which follow, we hold that this requirement was not fulfilled on any of the four occasions at which he is charged with failing to respond, that as a consequence he did not transgress the duty-to-reply regulations, and therefore that he was invalidly discharged for not answering the questions put to him.</p>
<p id="b607-7">At the interview of November 28, 1967, it is clear that no advice or warnings as to his constitutional rights was given to Mr. Kalkines, though he was told of the requirement of <page-number citation-index="1" label="576">*576</page-number>the Customs Manual that he answer. -Despite the fact that the matter had already been presented to the United States Attorney (as the customs agents knew), plaintiff was not told that his answers (or information stemming from them) could not be used against him in a criminal proceeding. So as far as the investigators were concerned, he was left sharply impaled on the dilemma of either answering and thereby subjecting himself to the possibility of self-incrimination, or of avoiding giving such help to the prosecution at the cost of his livelihood. The record shows conclusively that at this interview Mr. Kalkines was keenly aware of, and troubled by, the possible criminal implications, and that his failure to respond stemmed, at least in very substantial part, from this anxiety. <em>See also </em>note 6 <em>infra.</em></p>
<p id="b608-5">The next specification is that plaintiff refused to answer pertinent questions on May 2, 1968.<footnotemark>5</footnotemark> By this time, he had retained an attorney, but counsel was not present. Mr. Kalkines declined to answer unless he had the opportunity of consulting with his lawyer. After an exchange on this subject, the customs agent did not attempt to question him further, but called the attorney on the telephone and arranged for a joint meeting on May 8th. The Regional Office of the Civil Service Commission “concluded that there was at the least an implied acquiescence to the [plaintiff’s] request for the presence of his attorney as of May 2, 1968, and, in the circumstances, the [plaintiff’s] failure to answer questions on that date may not be recognized to have established a substantive basis to support” the specification as to May 2d which, accordingly, the Regional Office held not to be sustained. Without overturning the Regional Office’s factual finding on this point, the Board of Appeals and Review ruled that plaintiff was nevertheless guilty of failing to respond on May 2d. The basis for this holding appears <page-number citation-index="1" label="577">*577</page-number>to be that an employee’s obligation to answer is so absolute that it cannot even be waived by the interrogating agent’s agreement to wait until the lawyer is present. This, we hold, was plain error. If, as in this instance, the interrogator acquiesces in a request that questioning be deferred, the employee cannot be held to have violated his duty to account. The directives of the manuals cannot reasonably be interpreted in so absolute, rigid, and insensitive a fashion.<footnotemark>6</footnotemark></p>
<p id="b609-6">In addition, there is no indication whatever that plaintiff was told on May 2d that any answers could <em>not </em>be used against him criminally. Ait the last meeting on December 15th <em>(see </em>note 5 supra), the agent had specifically informed Mr. Kalkines that his answers <em>could </em>be used against him in a criminal proceeding, and in the absence of an explicit disavowal that advice could be expected to retain its force. Plaintiff justifiably remained under the impression that his replies could lead to his conviction of a criminal offense.</p>
<p id="b609-7">The third day on which plaintiff is accused of not answering was May 8,1968. At that time he appeared with counsel. There is a dispute in the testimony as to whether the attorney improperly interfered with the questioning by preventing, in effect, the putting of particular questions. In any event, no specific questions were asked or answered, and the agent <page-number citation-index="1" label="578">*578</page-number>ultimately directed counsel to withdraw from the room while a statement was taken from Mr. Kalkines. Thereupon both the attorney and plaintiff left the room. Plaintiff was told that he had to answer and that he had no right to have his counsel present but declined to stay or respond. Again, the significant element is that it is indisputable that neither the employee nor the lawyer was ever advised on May 8th that the responses to the questions, and their products, could not be used against plaintiff in a criminal trial or proceeding. In whatever way one interprets the controverted evidence as to the course of that meeting, this much is clear — no such caution was given, expressly or impliedly, by the agents.</p>
<p id="b610-5">On these facts, the only outcome, for the first three of the four specifications (November 28,1967; May 2,1968; May 8, 1968), must be that plaintiff cannot be held to have violated his obligation to answer. At those times a criminal investigation was either in the immediate offing or was actively being carried on. At the least, there is no question but that plaintiff thought so, and had no good reason to think otherwise. He obviously obtained a lawyer primarily because he was disturbed at the possibility of a criminal accusation; that danger was uppermost in his mind. It was reasonable for him to fear that any answer he gave to the customs agents might help to bring prosecution nearer; indeed, it was sensible to think that the civil and the criminal investigations were coordinated, so that the former would help the latter. He was never told that under the law his responses to the customs agents could not be used or would not be used as bricks to build him a prison cell. On the contrary, the one time the subject was mentioned by the agents (on December 15th, <em>see </em>note 5 supra), they said that his replies <em>could </em>be used against him. Under the standard of the <em>Uniformed Sanitation Mm </em>decisions, these three proceedings cannot be called “proper.” Plaintiff was not “duly advised of his options and the consequences of his choice.” Quite the opposite, he was left to squirm with a choice he should not have been put to — the possibility of going to jail or of losing his job. <em>Cf. Stevens </em>v. <em>Marks, </em><span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/" aria-description="Citation for case: Stevens v. Marks">383 U.S. 234</a></span> (1966).</p>
<p id="b610-6">The Government suggests that Mr. Kalkines, or at least <page-number citation-index="1" label="579">*579</page-number>his lawyer, should have known that his answers (and their fruits) could not be used to his disadvantage, and therefore that the explicit caution mandated by <em>Uniformed Sanitation Men II </em>might be omitted. With respect to the plaintiff, a frightened layman, this is certainly an unacceptable position; he could not be expected to know what lawyers and judges were even then arguing about. The case is hardly better for insisting that the attorney should have known, and should have been responsible for alerting his client. <em>Garriiy </em>v. <em>New </em><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">Jersey, <em>supra, </em></a></span><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span>, was not decided until January 16, 1967, and its reach was uncertain for some years. <em><span class="citation" data-id="107738"><a href="/opinion/107738/gardner-v-broderick/" aria-description="Citation for case: Gardner v. Broderick">Gardner</a></span> </em>and <em>Uniformed Sanitation Men I </em>did not come down until June 10, 1968 — after the last failure-to-respond charged against this plaintiff. <em>Uniformed Sanitation Men II </em>was not decided until April 3, 1970 (the Supreme Court did not decline review until May 30,1972). Many knowledgeable people believed that a specific immunity statute was necessary before anybody in the Federal Government could assure criminal immunity to individuals, including employees, being questioned in noncriminal proceedings. Perhaps, we may add, the law on the point is not yet wholly firm. At any rate, even the legendary Mr. Tutt, fictional legal genius of a generation or two ago, would have been hard put to know with any certainty, in the fall of 1967 and the spring of 1968, that this employee would be protected against prosecutorial use of his statements made to the customs agents.</p>
<p id="b611-6">This brings us to the last interview on June 5, 1968. Plaintiff was peremptorily ordered to come to Washington for this meeting with less than a day’s notice; he came without his lawyer who was engaged at the time on other urgent legal business and could not leave the New York area. The record contains a transcript of a portion of the interview. An agent opened by informing Mr. Kalkines that he was required to answer questions, and inquired whether he would “answer such questions as they pertain to your employee-employer relationship to the Bureau of Customs and the duties you perform on behalf of the Customs Service.” Plaintiff then said that he had “been advised by the customs agents that they are investigating me on an alleged criminal <page-number citation-index="1" label="580">*580</page-number>action. I was further advised by them to engage counsel.” He denied that he 'had refused to answer proper questions and went on to say that his attorney had advised him that “since this is a criminal action” the counsel should be present; “all I [plaintiff] ask is that if there is a criminal action pending against me that I have a right to have my counsel present.”</p>
<p id="b612-5">The agent replied “that the following interview is administrative in nature, that it is not criminal, that there is no criminal action pending against you and that the purpose of this interview is entirely on an employer-employee basis and that furthermore any answers given to questions put to you in the interview cannot and will not be used against you in any criminal action”; that if the interview were in connection with a criminal action the attorney would most certainly be permitted to be present and to advise; and “this is an administrative interview and do you understand that this interview is administrative and accordingly your attorney will not be permitted to be present during the interview.” The agent concluded these observations by asking plaintiff whether he would answer questions in counsel’s absence.</p>
<p id="b612-6">The defendant urges that this was proper and sufficient advice to Mr. Kalkines that he had immunity against use of his responses. But even the agent’s most explicit statement was incomplete since it did not refer to the fruits of the answers (in addition to the answers themselves). Moreover, and very significantly, the remainder of the colloquy shows that plaintiff was still very concerned about a criminal prosecution and that the agent never properly brought home that he would have immunity with respect to his answers. This portion of the interview is set forth in the footnote.<footnotemark>7</footnotemark></p>
<p id="b613-5"><page-number citation-index="1" label="581">*581</page-number>The essential aspects are four: First, in describing a “conduct” investigation the agent clearly indicated that a criminal investigation or trial was still possible; he contented himself with reiterating that his own concern was “administrative” and he was not pursuing a violation of criminal law, without denying that a criminal proceeding could possibly eventuate. Second, the agent never really responded to plaintiff’s query as to whether the criminal investigation had been dropped, and did not tell him that the U.S. Attorney had refused to go forward with prosecution.<footnotemark>8</footnotemark> Third, the agent failed to repeat or even refer to the earlier statement about non-use for criminal purposes of plaintiff’s answers in this “administrative” inquiry. Fourth, the plaintiff was obviously, and quite reasonably, left uncertain as to the connection between the questioning he was then being asked to undergo and a potential criminal action. This last element seems to us reinforced by some confused remarks of plaintiff’s later on in the exchange — after the agent had commenced to ask specific questions — which seem to express great doubt about the separation between the civil and criminal sides of the investigation.<footnotemark>9</footnotemark> Moreover, at the agency hearing, both the interrogating agent and the plaintiff made it clear in their testimony that <page-number citation-index="1" label="582">*582</page-number>plaintiff was fearful on June <em>5th that the </em>criminal aspect was still inextricably linked to the so-called “conduct investigation.”</p>
<p id="b614-5">The sum of this June 5th. episode is that, by failing to make and maintain a clear and unequivocal declaration of plaintiff’s “use” immunity, the customs agents gave the employee very good reason to be apprehensive that he could be walking into the criminal trap if he responded to potentially incriminating questions, and that in that dangerous situation he very much needed his lawyer’s help. The record compels this conclusion. Perhaps the agents were not more positive in their statements because there still remained at that time the possibility of prosecution.<footnotemark>10</footnotemark> Whatever the basis for their failure to clear up plaintiff’s reasonable doubts, we are convinced the record shows that he was not “duly advised of his options and •the consequences of his choice.”<footnotemark>11</footnotemark> His failure to respond was excused on this occasion, as on the earlier dates cited in the other specifications. The agency and the Civil Service Commission erred in disregarding this justification, and in holding that the duty to respond was absolute and was violated.</p>
<p id="b614-6">The result is that, for this reason,<footnotemark>12</footnotemark> plaintiff’s discharge in 1968 was invalid, and he is now entitled to recover his lost pay, less offsets. His motion for summary judgment is granted and the defendant’s is denied. The amount of recovery will be determined under Rule 131 (c) ,<footnotemark>13</footnotemark></p>
<footnote label="1">
<p id="b604-9"> The Customs Manual provided (§ 27.39(j)) : “Customs employees shall disclose any information in their possession pertaining to customs matters when requested to do so by a customs agent, and shall answer any proper questions put to them by customs agents.”</p>
<p id="b604-10">The Customs Personnel Manual stated (ch. 73,5, § 3, ¶ 3f) : “Every customs employee is required to disclose any information he has concerning customs matters when requested to do so by a customs agent. Every customs employee is required to answer any proper questions posed by a customs agent. Every customs employee, when requested to do so by a customs agent, shall furnish to such agent, or authorize him in writing to obtain, information of the employee’s financial affairs which bears a reasonable relationship to customs matters.”</p>
<p id="b604-11">The Treasury Personnel Manual declared (ch. 735, § 0.735-48) : “When directed to do so by competent Treasury authority, employees must testify or respond to questions (under oath when required) concerning matters of official interest. See further 31 CFR <em>1.10."</em></p>
</footnote>
<footnote label="2">
<p id="b604-12"> The original notice contained three other charges which were not sustained by the agency and are not before us.</p>
</footnote>
<footnote label="3">
<p id="b605-8"> There was a full-scale hearing within the Treasury Department (the “agency hearing”), which the record sets forth in question-and-answer form, as well as some additional testimony taken by the Civil Service Commission’s Regional Office, of which we have a narrative summary.</p>
</footnote>
<footnote label="4">
<p id="b607-8"> Those employees were advised as follows at the time management put the questions to them (<span class="citation" data-id="290212"><a href="/opinion/290212/uniformed-sanitation-men-association-inc-v-commissioner-of-sanitation-of/#621" aria-description="Citation for case: Uniformed Sanitation Men Association, Inc. v....">426 F. 2d at 621</a></span>) :</p>
<blockquote id="b607-9">“I want to advise you, Mr. -, that you have all the rights and privileges guaranteed by the Laws of the State of New Xork and the Constitution of this State and of the united States, including the right to be represented by counsel at this inquiry, the right to remain silent, although you may be subject to disciplinary action by the Department of Sanitation for the failure to answer material and relevant questions relating to the performance of your duties as an employee of the City of New Xork.</blockquote>
<blockquote id="b607-11">“I further advise you that the answers you may give to the questions propounded to you at this proceeding, or any information or evidence which is gained by reason of your answers, may not be used against you in a criminal proceeding except that you may be subject to criminal prosecution for any false answer that you may give under any applicable law, including Section 1121 of the New Xork City Charter.”</blockquote>
</footnote>
<footnote label="5">
<p id="b608-6"> Between November 28, 1967, and May 2, 1968, he had been called for an interview on December 15th. On this occasion he was informed, according to the Civil Service Commission’s Regional Office, "of his constitutional rights to remain silent and to have the presence of an attorney for consultation during the questioning, <em>and that anything he said could, he used against him in court proceedings" </em>(emphasis added). He answered the questions posed, and his conduct at that interview is not charged against him in the present proceedings.</p>
</footnote>
<footnote label="6">
<p id="b609-8"> We are also very dubious about a related bolding of tbe Board of Appeals and Review with respect to tbe first interview on November 28tb, <em>supra. </em>Tbe Regional Office accepted plaintiff’s testimony that on that day be was first confronted with a serious allegation of misconduct on bis part (with criminal implications) and as a consequence became nervous and flustered, being unable to continue the interview and just “closed down.” He did return the next day and answered detailed and extensive questions, including inquiries as to tbe $400 deposit on November 17th. On tbe basis of these facts, tbe Region found that plaintiff’s “first refusal to reply on November 2S, 1967 was effectively set aside as basis for the adverse action” and that tbe specification involving November 28th “is not sustained as substantive cause in support of that action.”</p>
<p id="b609-9">Again, without reversing the Regional Office’s finding of fact — paraphrased by the Board as: “the Region was persuaded that Mr. Kalkines’ refusal to cooperate at the first interview could be attributed to shock and mental stress” — .the Board of Appeals and Review reinstated that specification on the ground, apparently, that the duty to respond is so absolute that failure cannot be excused even by “shock and mental stress”, and even though the questions were answered the next day. This harsh position is very questionable. We have the greatest doubt that a federal employee can be validly discharged if it is determined, first, that his failure to answer queries on one day is due to such a disabling mental or emotional condition and, second, that he did respond to the questions shortly ther»after.</p>
</footnote>
<footnote label="7">
<p id="b612-7"> “A. To go over what you just said, are you stating that there Is no criminal Investigation relative to this matter, has this been dropped?</p>
<p id="b612-8">“Q. This Interview and the purpose of this interview Is purely administrative and is not a criminal action or related to a criminal action as it pertains to you.</p>
<p id="b612-9">“A. I don’t understand, you are not answering my question, is there an Investigation relative to me, a criminal investigation <em>1</em></p>
<p id="b612-10">“Q. No, there is a conduct investigation pending against you.</p>
<p id="b612-11">“A. For the record, may I state this is the first time that I have ever been told this. X have been advised for the last 6 months that I am under investigation for a criminal action and further I don’t know the difference between a conduct and a criminal action.</p>
<p id="b612-12">“Q. It is possible that if you have acted improper in the conduct of your business that your conduct may have involved conduct which is in violation <page-number citation-index="1" label="581">*581</page-number>of some criminal law. I restate that this interview is administrative and is not pursuing the violation of criminal law if one existed and in view of its administrative nature, your attorney will not be present. Please answer will you or will you not answer the questions I am about to put to you?</p>
<p id="Ayhs">“A. I can’t see the separation in which you call an administrative interview and the allegations that have unjustly been made against me. In my position, as I have stated, I will answer any and all questions regarding my customs duties gladly, cheerfully, openly, but I would lite to be afforded the opportunity of having my counsel .present.”</p>
</footnote>
<footnote label="8">
<p id="b613-11"> This is clear enough from the transcript of the interview. It is confirmed, moreover, by Mr. Kalkines’ explicit testimony at the agency hearing that at no time during that meeting did the agents tell him that criminal proceedings were not pending against him or that all criminal charges had been dropped. The agents did not testify to the contrary.</p>
</footnote>
<footnote label="9">
<p id="b613-13"> When the agent began to ash about the questioned customs transaction, the plaintiff repeated that he had never refused, and did not then refuse, to answer about his customs duties, that he wished counsel, and that he had previously answered that question. He went on: “The records cannot substantiate that to sit here and to state that there is disassoeiation between the allegation made against me and that this is merely the ordinary practice of Customs, I don’t think is correct. This is directly associated with an allegation against me and there is no disassoeiation, cannot be considered an administrative action, and again let me reiterate I have and will continue to answer every question relative to my customs duty, all I ask is that I have a right to have my counsel * *</p>
</footnote>
<footnote label="10">
<p id="b614-7"> There is a question whether the idea of a criminal proceeding had been entirely dropped by June 5th. The defendant says it had been but admits that formal notification to that effect was not given by the united States Attorney’s Office until some months later. In any event, the customs agent who interrogated plaintiff on June 5th conceded at the agency hearing that, if Mr. Kalkines had then made what appeared to the agents to be incriminating responses or had revealed circumstances which were obviously of a criminal nature, a report would probably have been made to the U.S. Attorney. The agent’s superior, who was present at the interrogation, testified at the agency hearing to similar effect.</p>
</footnote>
<footnote label="11">
<p id="b614-8"> An example of proper advice is that given in <em>Uniformed Sanitation Ken II, see </em>note 4 <em>supra.</em></p>
</footnote>
<footnote label="12">
<p id="b614-9"> We do not reach or consider any of plaintiff’s other contentions, including the argument that in any event he was entitled to the assistance of a lawyer at the May 8th and June 5th interviews even if properly advised as to his options.</p>
</footnote>
<footnote label="13">
<p id="b614-10"> Plaintiff is granted 30 days to file, if he desires, an amendment to his petition requesting restoration under <span class="citation no-link">Public Law 92-415, 86</span> Stat. 652 (August 29, 1972) to his position in the Bureau of Customs. <em>See </em>General Order No. 3 of 1972 (Dee. 12,1972), paras. 3(a), 4(b).</p>
</footnote>
</opinion>
```

---
