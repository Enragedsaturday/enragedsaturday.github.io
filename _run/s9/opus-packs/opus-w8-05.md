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

## GROUP: _overhaul2/lake/cases/Nance v. Ward.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Nance v. Ward
type: case
citation: "597 U.S. 159 (2022)"
parallel_cite: "142 S. Ct. 2214; 213 L. Ed. 2d 499"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2022
date_decided: ""
docket: 21-439
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
  opinion_url: "https://www.courtlistener.com/opinion/6480697/nance-v-ward/"
  cluster_id: 6480697
  opinion_id: null
  identity_checked: true
lake:
  record_id: Nance v. Ward
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Martin v. United States]]"
tags:
  - case
  - section-1983
  - habeas
  - eighth-amendment
  - method-of-execution
holding: "Section 1983 remains an appropriate procedural vehicle for a prisoner's Eighth Amendment method-of-execution claim even where the alternative method the prisoner proposes is not authorized by the executing State's death-penalty statute, because such relief does not necessarily prevent the State from carrying out the sentence and so falls outside the core of habeas corpus."
---

# Nance v. Ward

*597 U.S. 159 (2022)* (No. 21-439) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6480697 → opinion 6352830; quote string-matched to the CL slip-opinion text 2026-07-07 (CL carries the slip opinion "597 U. S. ____ (2022)"; U.S.-reporter page equality not asserted per S2 A3). S9 promotes. -->

## Background
Michael Nance, a Georgia death-row inmate, sued under 42 U.S.C. § 1983 to enjoin the State from executing him by lethal injection — the sole method Georgia law authorizes — alleging that his compromised veins would make that method create a substantial risk of severe pain in violation of the Eighth Amendment. As the required readily-available alternative, Nance proposed death by firing squad, a method authorized by four other States but not by Georgia. The Eleventh Circuit did not reach the merits: it recharacterized his § 1983 complaint as a second-or-successive [[Common Legal Terms#habeas-corpus|habeas]] petition, reasoning that because Georgia law (treated as "fixed") authorized only lethal injection, enjoining that method would necessarily invalidate his death sentence.

## Issue
Whether a prisoner may bring an Eighth Amendment method-of-execution claim under § 1983 — rather than in [[Common Legal Terms#habeas-corpus|habeas]] — when the alternative method he identifies is not authorized by the executing State's death-penalty statute.

## Rule
A prisoner may generally sue under § 1983 unless his claim falls within that statute's implicit exception for actions lying at the core of [[Common Legal Terms#habeas-corpus|habeas corpus]] — that is, where the relief sought would "necessarily imply the invalidity of his conviction or sentence." Because a method-of-execution claim requires the prisoner to identify an available alternative, granting relief does not necessarily prevent the State from carrying out the sentence; it merely requires the State to switch methods. That the proposed alternative would require Georgia to amend its statute does not change the vehicle: "one of the 'main aims' of § 1983 is to 'override'—and thus compel change of—state laws when necessary to vindicate federal constitutional rights." The Court framed and answered the question directly: "The question presented is whether § 1983 is still a proper vehicle. We hold that it is." — 597 U.S. 159 (slip op., at 1). ^pin-op

## Application
Nance's requested relief left his execution in Georgia's control: if the State wished to carry out the sentence, it could enact legislation authorizing the firing squad, a method a court had found fairly easy to employ. Any incidental delay from a statutory change was irrelevant to the vehicle question, which turns on whether the relief would *necessarily* invalidate the sentence. Reading state-by-state statutory variation into the § 1983-versus-[[Common Legal Terms#habeas-corpus|habeas]] line would make the federal vehicle turn on "the vagaries of state law" and would turn the Court's promise in *Bucklew* — that a prisoner may propose an out-of-state alternative — "into a sham."

## Conclusion
The judgment of the Eleventh Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Kagan, J., delivered the opinion of the Court, joined by Roberts, C.J., and Breyer, Sotomayor, and Kavanaugh, JJ.; Barrett, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Thomas, Alito, and Gorsuch, JJ.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Nance* is a vehicle-selection decision at the § 1983/[[Common Legal Terms#habeas-corpus|habeas]] boundary rather than a liability-standard case: it confirms that § 1983 reaches claims whose remedy would compel a change in state law, so long as the relief does not necessarily bar the sentence's enforcement.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Nance v. Ward*, 597 U.S. 159 (2022)](https://www.courtlistener.com/opinion/6480697/nance-v-ward/) — pinpoint: slip op., at 1 (Opinion of the Court, holding; Kagan, J.). CL carries the slip opinion ("597 U. S. ____ (2022)"; cluster 6480697 → opinion 6352830); slip-only per S2 A3 — quote string-matched to the CL opinion text 2026-07-07, U.S.-reporter page equality not asserted.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "19cccca39375ba9e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Nance v. Ward"}, "payload": {"all": [{"cite": "597 U.S. 159", "page": "159", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "597"}, {"cite": "142 S. Ct. 2214", "page": "2214", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "142"}, {"cite": "213 L. Ed. 2d 499", "page": "499", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "213"}], "display": "597 U.S. 159", "official": {"cite": "597 U.S. 159", "page": "159", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "597"}, "official_selection_present": true, "record_id": "Nance v. Ward"}}
{"assertion_id": "a53e806e4504b093", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Nance v. Ward"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Nance v. Ward", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Nance v. Ward

```json
{
  "schema_version": "s2.v1",
  "record_id": "Nance v. Ward",
  "status": "under_review",
  "identity": {
    "case_name": "Nance v. Ward",
    "case_name_short": "Nance",
    "case_name_full": "",
    "input_case_name": "Nance v. Ward",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2022,
    "docket": "21-439",
    "cluster_id": 6480697,
    "lead_opinion_id": 6352830,
    "sibling_ids": [],
    "absolute_url": "/opinion/6480697/nance-v-ward/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "597 U.S. 159",
      "volume": "597",
      "reporter": "U.S.",
      "page": "159",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 2214",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 499",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "597 U.S. 159",
        "volume": "597",
        "reporter": "U.S.",
        "page": "159",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 2214",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "2214",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "213 L. Ed. 2d 499",
        "volume": "213",
        "reporter": "L. Ed. 2d",
        "page": "499",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "597 U.S. 159",
    "official_selection": {
      "court_class": "scotus",
      "selected": "597 U.S. 159",
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
    "date_created": "2026-07-06T12:11:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:11:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "nance-v-ward--6480697",
      "to_record_id": "Nance v. Ward",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Nance v. Ward

```
(Slip Opinion)              OCTOBER TERM, 2021                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

       NANCE v. WARD, COMMISSIONER, GEORGIA
         DEPARTMENT OF CORRECTIONS, ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

       No. 21–439.      Argued April 25, 2022—Decided June 23, 2022
A prisoner who challenges a State’s proposed method of execution under
  the Eighth Amendment must identify a readily available alternative
  method that would significantly reduce the risk of severe pain. If the
  prisoner proposes a method already authorized under state law, the
  Court has held that his claim can go forward under 42 U. S. C. §1983,
  rather than in habeas. See Nelson v. Campbell, 541 U. S. 637, 644–
  647. But the prisoner is not confined to proposing a method already
  authorized under state law; he may ask for a method used in other
  States. See Bucklew v. Precythe, 587 U. S. ___, ___. The question pre-
  sented is whether a prisoner who does so may still proceed under
  §1983.
     Petitioner Michael Nance brought suit under §1983 to enjoin Geor-
  gia from using lethal injection to carry out his execution. Lethal injec-
  tion is the only method of execution that Georgia law now authorizes.
  Nance alleges that applying that method to him would create a sub-
  stantial risk of severe pain. As an alternative to lethal injection,
  Nance proposes death by firing squad—a method currently approved
  by four other States. The District Court dismissed Nance’s §1983 suit
  as untimely. The Eleventh Circuit rejected it for a different reason:
  that Nance should have advanced his method-of-execution claim by
  way of a habeas petition rather than a §1983 suit. A habeas petition,
  that court stated, is appropriate when a prisoner seeks to invalidate
  his death sentence. And the Eleventh Circuit thought that was what
  Nance was doing. It asserted that Georgia law—which again, only au-
  thorizes execution by lethal injection—had to be taken as “fixed.” 981
  F. 3d 1201, 1211. Under that “fixed” law, the court said, enjoining
  Georgia from executing Nance by lethal injection would mean that he
2                            NANCE v. WARD

                                 Syllabus

    could not be executed at all. The court therefore “reconstrued” Nance’s
    §1983 complaint as a habeas petition. Id., at 1203. Having done so,
    the court then dismissed Nance’s petition as “second or successive,”
    because he had previously sought federal habeas relief. 28 U. S. C.
    §2244(b).
Held: Section 1983 remains an appropriate vehicle for a prisoner’s
 method-of-execution claim where, as here, the prisoner proposes an al-
 ternative method not authorized by the State’s death-penalty statute.
    Both §1983 and the federal habeas statute enable a prisoner to com-
 plain of “unconstitutional treatment at the hands of state officials.”
 Heck v. Humphrey, 512 U. S. 477, 480. A prisoner may generally sue
 under §1983, unless his claim falls into that statute’s “implicit excep-
 tion” for actions that lie “within the core of habeas corpus.” Wilkinson
 v. Dotson, 544 U. S. 74, 79. When a prisoner seeks relief that would
 “necessarily imply the invalidity of his conviction or sentence,” he
 comes within the core and must proceed in habeas. Heck, 512 U. S., at
 487.
    The Court has twice held that prisoners could bring method-of-
 execution claims under §1983. See Nelson, 541 U. S., at 644–647; Hill
 v. McDonough, 547 U. S. 573, 580–583. Although these cases predated
 the Court’s requirement that prisoners identify alternative methods of
 execution, each prisoner had still said enough to leave the Court con-
 vinced that alternatives to the challenged procedures were available.
 See Nelson, 541 U. S., at 646; Hill, 547 U. S., at 580–581. Because
 alternatives were available, the prisoners’ challenges would not “nec-
 essarily prevent [the State] from carrying out [their] execution[s].”
 Nelson, 541 U. S., at 647 (emphasis in original); see Hill, 547 U. S., at
 583. That made §1983 a proper vehicle.
    In Nelson and Hill, the Court observed that using a different method
 required only a change in an agency’s uncodified protocol. Here, Geor-
 gia would have to change its statute to carry out Nance’s execution by
 firing squad. Except for that fact, this case would even more clearly
 than Nelson and Hill be fit for §1983. Since those cases, the Court has
 required a prisoner bringing a method-of-execution claim to propose
 an alternative way of carrying out his death sentence. Thus, an order
 granting the prisoner relief does not, as required for habeas, “neces-
 sarily prevent” the State from implementing the execution. Nelson,
 541 U. S., at 647 (emphasis in original). Rather, the order gives the
 State a pathway forward.
    That remains true even where, as here, the proposed alternative is
 one unauthorized by present state law. Nance’s requested relief still
 places his execution in Georgia’s control. If Georgia wants to carry out
 the death sentence, it can enact legislation approving what a court has
 found to be a fairly easy-to-employ method of execution. Although that
                     Cite as: 597 U. S. ____ (2022)                     3

                                Syllabus

  may take more time and effort than changing an agency protocol, Hill
  explained that the “incidental delay” involved in changing a procedure
  is irrelevant to the vehicle question—which focuses on whether the re-
  quested relief would “necessarily” invalidate the death sentence. 547
  U. S., at 583. And anyway, Georgia has given no reason to think that
  passing new legislation would be a substantial impediment.
     The Court of Appeals could reach the contrary conclusion only by
  wrongly treating Georgia’s statute as immutable. In its view, granting
  Nance relief would necessarily imply the invalidity of his death sen-
  tence because Georgia law must be taken as “fixed.” 981 F. 3d, at 1211.
  But one of the “main aims” of §1983 is to “override”—and thus compel
  change of—state laws when necessary to vindicate federal constitu-
  tional rights. Monroe v. Pape, 365 U. S. 167, 173. Indeed, courts not
  uncommonly entertain prisoner suits under §1983 that may, if success-
  ful, require changing state law.
     Under the contrary approach, the federal vehicle for bringing a fed-
  eral method-of-execution claim would depend on the vagaries of state
  law. Consider how Nance’s claim would fare in different States. In
  Georgia (and any other State with lethal injection as the sole author-
  ized method), he would have to bring his claim in a habeas petition.
  But in States authorizing other methods when a court holds injection
  unlawful, he could file a §1983 suit. It would be strange to read state-
  by-state discrepancies into the Court’s understanding of how §1983
  and the habeas statute apply to federal constitutional claims. That is
  especially so because the use of the vehicles can lead to different out-
  comes: An inmate in one State could end up getting his requested re-
  lief, while an inmate in another might have his case thrown out.
     The approach of the Court of Appeals raises one last problem: It
  threatens to undo the commitment this Court made in Bucklew. The
  Court there told prisoners they could identify an alternative method
  not “presently authorized” by the executing State’s law. 587 U. S., at
  ___. But under the approach of the Court of Appeals, a prisoner who
  presents an out-of-state alternative is relegated to habeas—and once
  there, he will almost inevitably collide with the second-or-successive
  bar. That result, precluding claims like Nance’s, would turn Bucklew
  into a sham.
     Finally, recognizing that §1983 is a good vehicle for a claim like
  Nance’s does not countenance “last-minute” claims to forestall an exe-
  cution. Id., at ___. Courts must consider delay in deciding whether to
  grant a stay of execution, and outside the stay context, courts have
  tools to streamline §1983 actions and protect a sentence’s timely en-
  forcement. Pp. 5–13.
981 F. 3d 1201, reversed and remanded.

  KAGAN, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and BREYER, SOTOMAYOR, and KAVANAUGH, JJ., joined. BARRETT, J., filed
a dissenting opinion, in which THOMAS, ALITO, and GORSUCH, JJ., joined.
                        Cite as: 597 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 21–439
                                    _________________


   MICHAEL NANCE, PETITIONER v. TIMOTHY C.
    WARD, COMMISSIONER, GEORGIA DEPART-
        MENT OF CORRECTIONS, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                                  [June 23, 2022]

  JUSTICE KAGAN delivered the opinion of the Court.
   In several recent decisions, this Court has set out rules
for challenging a State’s proposed method of execution un-
der the Eighth Amendment. To prevail on such a claim, a
prisoner must identify a readily available alternative
method of execution that would significantly reduce the risk
of severe pain. In doing so, the prisoner is not confined to
proposing a method authorized by the executing State’s
law; he may instead ask for a method used in other States.
See Bucklew v. Precythe, 587 U. S. ___, ___ (2019) (slip op.,
at 19).
   This case concerns the procedural vehicle appropriate for
a prisoner’s method-of-execution claim. We have held that
such a claim can go forward under 42 U. S. C. §1983, rather
than in habeas, when the alternative method proposed is
already authorized under state law. See Nelson v. Camp-
bell, 541 U. S. 637, 644–647 (2004). Here, the prisoner has
identified an alternative method that is not so authorized.
The question presented is whether §1983 is still a proper
vehicle. We hold that it is.
2                          NANCE v. WARD

                          Opinion of the Court

                             I
                             A
  States choosing to impose capital punishment have over
time sought out “more humane way[s] to carry out death
sentences.” Glossip v. Gross, 576 U. S. 863, 868 (2015). In
the 27 States with the death penalty, lethal injection is by
far the most common method of execution. See ibid. Fif-
teen States, including Georgia, authorize only the use of le-
thal injection.1 Nine States authorize lethal injection plus
one or more other specified methods; of those (to use an ex-
ample relevant here), four approve the firing squad.2 And
three States provide that if their authorized methods (in-
cluding lethal injection) are found unconstitutional, then
they may carry out a death sentence by any constitutional
means.3
  A death row inmate may attempt to show that a State’s
planned method of execution, either on its face or as applied
to him, violates the Eighth Amendment’s prohibition on

——————
  1 Ariz. Rev. Stat. Ann. §13–757(A) (2020); Ga. Code Ann. §17–10–38(a)

(2020); Idaho Code Ann. §19–2716 (2017); Ind. Code §35–38–6–1(a)
(2021); Kan. Stat. Ann. §22–4001(a) (2007); La. Rev. Stat. Ann.
§15:569(B) (West 2022); Mont. Code Ann. §46–19–103(3) (2021); Neb.
Rev. Stat. §83–964 (2020 Cum. Supp.); Nev. Rev. Stat. §176.355(1)
(2017); N. C. Gen. Stat. Ann. §15–188 (2021); Ohio Rev. Code Ann.
§2949.22(A) (Lexis 2021); Ore. Rev. Stat. §137.473(1) (2021); 61 Pa. Cons.
Stat. §4304(a) (2015 Special Edition); S. D. Codified Laws §23A–27A–32
(2016); Tex. Code Crim. Proc. Ann., Art. §43.14(a) (Vernon 2018).
  2 Mississippi, Oklahoma, South Carolina, and Utah authorize the fir-

ing squad among other methods of execution. H. B. 1479, 2022 Leg., Reg.
Sess. (Miss.); Okla. Stat., Tit. 22, §1014 (2020 Supp.); S. C. Code Ann.
§24–3–530 (2021 Cum. Supp.); Utah Code §77–18–113 (2021). The rest
of the States in this bucket most commonly authorize electrocution or
lethal gas. See Ark. Code Ann. §§5–4–617(a), (l) (Supp. 2021); Cal. Penal
Code Ann. §3604(a) (West Supp. 2022); Ky. Rev. Stat. Ann.
§§431.220(1)(a), 431.223 (Lexis 2021); Mo. Rev. Stat. §546.720(1) (2016);
Wyo. Stat. Ann. §7–13–904 (2021).
  3 Ala. Code §15–18–82.1(c) (2018); Fla. Stat. §922.105(3) (2018); Tenn.

Code Ann. §40–23–114(d) (2018).
                  Cite as: 597 U. S. ____ (2022)            3

                      Opinion of the Court

“cruel and unusual” punishment. To succeed on that claim,
the Court held in Glossip, he must satisfy two require-
ments. First, he must establish that the State’s method of
execution presents a “substantial risk of serious harm”—
severe pain over and above death itself. Id., at 877. Second,
and more relevant here, he “must identify an alternative
[method] that is feasible, readily implemented, and in fact
significantly reduce[s]” the risk of harm involved. Ibid. (in-
ternal quotation marks omitted). Only through a “compar-
ative exercise,” we have explained, can a judge “decide
whether the State has cruelly ‘superadded’ pain to the pun-
ishment of death.” Bucklew, 587 U. S., at ___ (slip op., at
15).
   In identifying an alternative method, the Court in Buck-
lew held, an inmate is “not limited to choosing among those
presently authorized by a particular State’s law.” Id., at ___
(slip op., at 19). The prisoner may, for example, “point to a
well-established protocol in another State as a potentially
viable option.” Ibid. The Eighth Amendment, Bucklew ex-
plained, “is the supreme law of the land, and the compara-
tive assessment it requires can’t be controlled by the State’s
choice of which methods to authorize.” Id., at ___ (slip op.,
at 20); see Arthur v. Dunn, 580 U. S. ___, ___ (2017) (slip
op., at 10) (SOTOMAYOR, J., dissenting from denial of certi-
orari). In addition, Bucklew stated, allowing an inmate to
propose a method not authorized by the State keeps his
“burden” within reasonable bounds. 587 U. S., at ___ (slip
op., at 19). Because the inmate can look beyond the State’s
current law, we saw “little likelihood” that he would “be un-
able to identify an available alternative.” Id., at ___ (slip
op., at 20); see id., at ___ (slip op., at 2) (KAVANAUGH, J.,
concurring).
                            B
  While trying to flee a bank robbery, petitioner Michael
4                        NANCE v. WARD

                        Opinion of the Court

Nance shot and killed a bystander. A Georgia jury con-
victed Nance of murder, and the trial court sentenced him
to death. Nance challenged his conviction and sentence—
first on direct appeal, next in state collateral proceedings,
and finally in federal habeas—but without success.
   Nance later brought suit under §1983 to enjoin Georgia
from using lethal injection to carry out his death sentence.
As stated above, lethal injection is the only method of exe-
cution Georgia law now authorizes. See supra, at 2.4 In his
complaint, Nance alleges that applying that method to him
would create a substantial risk of severe pain. See App. to
Pet. for Cert. 86a. According to Nance, his veins are “se-
verely compromised and unsuitable for sustained intrave-
nous access.” Ibid. They are, Nance says, likely to “blow”
during the execution, “leading to the leakage of the lethal
injection drug into the surrounding tissue” and thereby
causing “intense pain and burning.” Ibid. On top of that,
Nance asserts, his longtime use of a prescription drug for
back pain creates a risk that the sedative used in the State’s
lethal injection protocol will fail to “render him unconscious
and insensate.” Ibid. Nance proposes, as a “readily availa-
ble alternative” method of execution, “death by firing
squad.” Ibid. As noted earlier, four other States have ap-
proved that method. See supra, at 2, and n. 2. Use of a
firing squad, Nance says, will lead to “swift and virtually
painless” death. App. to Pet. for Cert. 102a. And imple-
menting that method, he says, would be simple: Georgia
has enough qualified personnel and could borrow specific
protocols from another State. Ibid.
   After the District Court dismissed Nance’s suit as un-
timely, the Court of Appeals for the Eleventh Circuit re-
jected it for a different reason—that Nance had used the

——————
   4 See Ga. Code Ann. §17–10–38(a) (“All persons who have been con-

victed of a capital offense and have had imposed upon them a sentence
of death shall suffer such punishment by lethal injection”).
                 Cite as: 597 U. S. ____ (2022)            5

                     Opinion of the Court

wrong procedural vehicle. In the panel majority’s view,
Nance should have brought his method-of-execution claim
by way of a habeas petition rather than a §1983 suit. A
habeas petition, the court stated, is appropriate when a
prisoner seeks to “invalidate” a death sentence. 981 F. 3d
1201, 1209 (2020). And the court thought that was what
Nance was doing: The injunction he requested, preventing
the use of lethal injection, “necessarily impl[ies] the inva-
lidity of his death sentence.” Id., at 1203. That was so, the
court reasoned, because Georgia law “must [be taken] as
fixed”—and under that “fixed” law, if Nance could not be
executed by lethal injection, then he could not be executed
at all. Id., at 1211. The court therefore “reconstrued”
Nance’s complaint as a habeas petition. Id., at 1203. And
having done so, the court dismissed the petition as “second
or successive” because Nance had already sought federal
habeas relief. 28 U. S. C. §2244(b); see supra, at 4. Judge
Martin dissented, arguing that Nance could proceed under
§1983. In her view, Nance was not challenging his death
sentence; all he wanted was an order telling “the State to
execute him by a different method.” 981 F. 3d, at 1215. The
Eleventh Circuit denied Nance’s petition for rehearing en
banc over the dissent of three judges. See 994 F. 3d 1335
(2021).
   We granted certiorari, 595 U. S. ___ (2022), and now re-
verse.
                              II
  This Court has often considered, when evaluating state
prisoners’ constitutional claims, the dividing line between
§1983 and the federal habeas statute. Each law enables a
prisoner to complain of “unconstitutional treatment at the
hands of state officials.” Heck v. Humphrey, 512 U. S. 477,
480 (1994). But there the resemblance stops. The habeas
statute contains procedural requirements (like the second-
6                     NANCE v. WARD

                     Opinion of the Court

or-successive rule) nowhere found in §1983; the former stat-
ute may therefore require dismissal of a claim when the lat-
ter statute would not. See id., at 480–481. Still more per-
tinent here, the scope of the two laws also differs. Section
1983 broadly authorizes suit against state officials for the
“deprivation of any rights” secured by the Constitution.
Read literally, that language would apply to all of a pris-
oner’s constitutional claims, thus swamping the habeas
statute’s coverage of claims that the prisoner is “in custody
in violation of the Constitution.” 28 U. S. C. §2254(a); see
Wilkinson v. Dotson, 544 U. S. 74, 78–79 (2005). So we have
not read §1983 literally in the prisoner context. To the con-
trary, we have insisted that §1983 contains an “implicit ex-
ception” for actions that lie “within the core of habeas cor-
pus.” Id., at 79.
   In defining that core, this Court has focused on whether
a claim challenges the validity of a conviction or sentence.
See Preiser v. Rodriguez, 411 U. S. 475, 489 (1973). The
simplest cases arise when an inmate, alleging a flaw in his
conviction or sentence, seeks “immediate or speedier re-
lease” from prison. Heck, 512 U. S., at 481. The analogue
in the capital punishment context, also clear-cut, is when
an inmate seeks to overturn his death sentence, thus pre-
venting the State from executing him. Slightly less obvious,
this Court has held that an inmate must proceed in habeas
when the relief he seeks would “necessarily imply the inva-
lidity of his conviction or sentence.” Id., at 487 (barring
§1983 suits for money damages when prevailing would im-
ply a conviction was wrongful). In doing so, though, we
have underscored that the implication must be “neces-
sar[y].” Wilkinson, 544 U. S., at 81 (emphasis in original);
see Nelson, 541 U. S., at 647. On the opposite end of the
spectrum, the Court has held that a prison-conditions claim
may be brought as a §1983 suit. See Preiser, 411 U. S., at
498–499. Such a suit—for example, challenging the ade-
quacy of a prison’s medical care—does not go to the validity
                     Cite as: 597 U. S. ____ (2022)                     7

                          Opinion of the Court

of a conviction or sentence, and thus falls outside habeas’s
core.
   In Nelson v. Campbell and Hill v. McDonough, this Court
held two method-of-execution claims to fall on the §1983
side of the divide. See Nelson, 541 U. S., at 644–647; Hill,
547 U. S. 573, 580–583 (2006). Both cases involved chal-
lenges to a State’s lethal injection protocol—the first to the
use of a “cut-down” procedure to access the prisoner’s veins,
the second to a particular three-drug sequence. The cases
predated our requirement that prisoners identify alterna-
tive methods, but each prisoner had said enough to leave
the Court convinced that alternatives to the challenged pro-
cedures were available. See Nelson, 541 U. S., at 646; Hill,
547 U. S., at 580–581. And that made the difference in both
cases. A claim should go to habeas, the Court held, only if
granting the prisoner relief “would necessarily prevent [the
State] from carrying out its execution.” Nelson, 541 U. S.,
at 647 (emphasis in original); see Hill, 547 U. S., at 583.5
In neither case would it have done so. Each prisoner had
asked only for a change in implementing the death penalty,
and an order granting that relief would not prevent the
State from executing him. So the claims could proceed un-
der §1983.
   Both Nelson and Hill, though, reserved the question at
issue here: whether the result should be different when a
State’s death-penalty statute does not authorize the alter-
native method of execution. See Nelson, 541 U. S., at 645;
Hill, 547 U. S., at 580. In each case, the Court observed
that using a different method required no change in the
State’s statute, but only a change in an agency’s uncodified
——————
  5 In both cases, the Court made clear that its formulation (again, would

granting relief necessarily prevent the execution) merely adapted to the
capital punishment context the question the Court had formerly asked
in choosing between §1983 and habeas: Would granting relief necessarily
imply the invalidity of a conviction or sentence? See Nelson, 541 U. S.,
at 646; Hill, 547 U. S., at 583; supra, at 6.
8                      NANCE v. WARD

                      Opinion of the Court

protocols. Here, all parties agree that Georgia would have
to change its statute to carry out Nance’s execution by
means of a firing squad. They dispute whether that fact
switches Nance’s claim to the habeas track.
   Except for the Georgia statute, this case would even more
clearly than Nelson and Hill be fit for §1983. Since those
two cases, we have compelled a prisoner bringing a method-
of-execution claim to propose an alternative way for the
State to carry out his death sentence. He must, we have
said, present a “proposal” that is “sufficiently detailed” to
show that an alternative method is both “feasible” and
“readily implemented.” Bucklew, 587 U. S., at ___ (slip op.,
at 21); see supra, at 3. In other words, he must make the
case that the State really can put him to death, though in a
different way than it plans. The substance of the claim, now
more than ever, thus points toward §1983. The prisoner is
not challenging the death sentence itself; he is taking the
validity of that sentence as a given. And he is providing the
State with a veritable blueprint for carrying the death sen-
tence out. If the inmate obtains his requested relief, it is
because he has persuaded a court that the State could read-
ily use his proposal to execute him. The court’s order there-
fore does not, as required for habeas, “necessarily prevent”
the State from carrying out its execution. Nelson, 541 U. S.,
at 647 (emphasis in original). Rather, the order gives the
State a pathway forward.
   That remains true, we hold today, even if the alternative
route necessitates a change in state law. Nance’s requested
relief still places his execution in Georgia’s control. Assum-
ing it wants to carry out the death sentence, the State can
enact legislation approving what a court has found to be a
fairly easy-to-employ method of execution. To be sure,
amending a statute may require some more time and effort
than changing an agency protocol, of the sort involved in
Nelson and Hill. But in Hill, we explained that the “inci-
dental delay” involved in changing a procedure—which
                     Cite as: 597 U. S. ____ (2022)                    9

                          Opinion of the Court

even when uncodified may take some real work6—is not rel-
evant to the vehicle question. 547 U. S., at 583. Instead,
that inquiry (as described earlier) focuses on whether the
requested relief would “necessarily” invalidate, or foreclose
the State from implementing, the death sentence. Ibid.; see
supra, at 6. And anyway, Georgia has given us no reason
to think that the amendment process would be a substan-
tial impediment. The State has legislated changes to its
execution method several times before. See Dept. of Cor-
rections, Office of Planning and Analysis, A History of the
Death Penalty in Georgia: Executions by Year 1924–2014
(Jan. 2015) (describing how Georgia moved from hanging to
electrocution to lethal injection). Other States have regu-
larly done the same, often in an effort to make executions
more humane. See S. Banner, The Death Penalty: An
American History 296–297 (2002); see supra, at 2. That
Nance’s claim would require such action does not turn it
from one contesting a method of execution into one disput-
ing the underlying death sentence.
   The Court of Appeals could reach the contrary conclusion
only by wrongly treating Georgia’s statute as immutable.
Recall the court’s reasoning: Granting Nance relief would
“necessarily imply[] the invalidity” of his death sentence be-
cause Georgia law (presumably both statutes and regula-
tions) “must [be taken] as fixed.” 981 F. 3d, at 1210–1211;
see supra, at 5; post, at 3–4 (BARRETT, J., dissenting) (agree-
ing that we must “take state law as we find it”). But why
must it be so taken—when as a matter of fact Georgia could
change its law and execute Nance? And when Nance ac-
cepts the validity of the State’s taking that course? The
Court of Appeals posited that “it is not [a federal court’s]
place to entertain complaints under section 1983” that
——————
  6 In a recent case, Texas described to this Court the complexity of

changing uncodified execution protocols, given the number of state actors
who need to reach agreement. See Respondents’ Rule 32.3 Material in
Ramirez v. Collier, O. T. 2021, No. 21–5592, p. 14a.
10                    NANCE v. WARD

                     Opinion of the Court

would compel a State to change its capital punishment law.
981 F. 3d, at 1211; see post, at 3. Except that sometimes it
is. One of the “main aims” of §1983 is to “override”—and
thus compel change of—state laws when necessary to vin-
dicate federal constitutional rights. Monroe v. Pape, 365
U. S. 167, 173 (1961); see Zinermon v. Burch, 494 U. S. 113,
124 (1990). Or said otherwise, the ordinary and expected
outcome of many a meritorious §1983 suit is to declare un-
enforceable (whether on its face or as applied) a state stat-
ute as currently written. See, e.g., Cedar Point Nursery v.
Hassid, 594 U. S. ___ (2021). And in turn, the unsurprising
effect of such a judgment may be to send state legislators
back to the drawing board. See, e.g., Kolender v. Lawson,
461 U. S. 352, 358 (1983). A prisoner, no less than any
other §1983 litigant, can bring a suit of that ilk—can seek
relief that would preclude a State from achieving some re-
sult unless and until it amends a statute.
   And indeed, courts not uncommonly entertain prisoner
suits under §1983 that may, if successful, require changing
state law. As noted earlier, the classic prisoner §1983 suit
is one challenging prison conditions—say, overcrowding or
inadequate medical care. See supra, at 6–7. Those suits
can be brought under §1983 because—just like this one—
they attack not the validity of a conviction or sentence, but
only a way of implementing the sentence. (They concern, in
other words, how the prescribed incarceration is being car-
ried out.) And the suits do not get diverted into habeas if,
as sometimes is true, a judgment for the inmate would re-
quire a new statutory appropriation for the prison—to hire
more doctors, for example. See, e.g., Stafford v. Carter, No.
1:17–cv–00289 (SD Ind.), ECF Docs. 268, 282. Similarly, no
one would think an action of that kind should go to habeas
if the prison policy challenged (say, each facility’s maximum
population) were specified in a statute or regulation. Or
consider another kind of prisoner §1983 suit this Court has
recently considered—one by a death row inmate seeking to
                  Cite as: 597 U. S. ____ (2022)            11

                      Opinion of the Court

compel the State to open the execution chamber to his spir-
itual advisor. See Dunn v. Ray, 586 U. S. ___ (2019); Mur-
phy v. Collier, 587 U. S. ___ (2019); Gutierrez v. Saenz, 592
U. S. ___ (2021); Ramirez v. Collier, 595 U. S. ___ (2022).
Here too, the claim belongs in §1983 because—just like this
one—it challenges not the validity of a death sentence, but
only the State’s mode of carrying it out. And again, we can-
not think it would matter if a State codified its no-spiritual-
advisor protocol in a regulation. The State, assuming it lost
the suit, would then have to modify its law to go forward
with the execution. But the nature of the suit would still be
the same. The complaint would still ask to adjust only a
matter of implementation, so it still could be filed under
§1983.
   Under the contrary approach, the federal vehicle for
bringing a federal claim—and with that, the viability of the
claim—would depend on the vagaries of state law. Consider
how Nance’s own method-of-execution claim would fare in
different States. In Georgia (and any other State with le-
thal injection as the sole authorized method), he would have
to bring his claim in a habeas petition. But in some other
States primarily using lethal injection, he could file a §1983
suit—because their statutes include back-up plans for when
a court holds injection unconstitutional. See supra, at 2.
Oklahoma’s statute, for example, provides in that event for
several alternative methods, including a firing squad. See
Okla. Stat., Tit. 22, §§1014(B)–(D). And Alabama’s statute,
in addition to listing alternatives, provides for execution “by
any constitutional method.” Ala. Code §15–18–82.1(c).
Similar issues of non-uniformity could arise when inmates
challenge, as in Nelson and Hill, specific ways of carrying
out a lethal injection. See supra, at 7. That is because some
States have codified injection protocols in their statutes or
regulations, while others (like Georgia) have not. Compare,
e.g., Ark. Code Ann. §§5–4–617(c)–(f ) with, e.g., Ga. Code
Ann. §17–10–38(a). It would be strange to read such state-
12                    NANCE v. WARD

                     Opinion of the Court

by-state discrepancies into our understanding of how §1983
and the habeas statute apply to federal constitutional
claims. And that is especially so because the use of those
vehicles can lead to different outcomes: An inmate in one
State could end up getting his requested relief, while a sim-
ilarly situated inmate in another would have his suit
thrown out. We cannot agree with the dissent that such a
disparity would be “unremarkable.” Post, at 3. Its ac-
ceptance would mean that the Eighth Amendment is en-
forceable in federal court in one State, but not in another.
Again, this case tells the tale: Having reconstrued Nance’s
complaint as a habeas petition, the court below dismissed it
as second or successive—a bar existing in habeas alone. See
supra, at 5–6.
   That part of the circuit court’s opinion raises one last
problem, because it threatens to undo the commitment this
Court made in Bucklew. See post, at 4 (acknowledging the
point, though finding it irrelevant). Recall that the Court
there told inmates they could identify an alternative
method of execution not “presently authorized” by the exe-
cuting State’s law. 587 U. S., at ___ (slip op., at 19); see
supra, at 3. That option would ensure state law does not
“control[ ]” the Eighth Amendment inquiry; and it would
keep manageable the inmate’s “burden” to identify an alter-
native. 587 U. S., at ___–___ (slip op., at 19–20). Under the
circuit court’s approach, however, that option is no option
at all. Once an inmate presents an out-of-state alternative,
he is relegated to habeas. And once he is in habeas, he will
(according to the circuit court) almost inevitably collide
with the second-or-successive bar (because a method-of-ex-
ecution claim typically postdates a first habeas petition by
many years). We do not here decide whether that view of
the second-or-successive bar is correct. But the two aspects
of the circuit court’s ruling, when taken together, turn
Bucklew into a sham. On the Eleventh Circuit’s view, Geor-
                 Cite as: 597 U. S. ____ (2022)           13

                     Opinion of the Court

gia law effectively prevents an inmate like Nance from put-
ting forward an out-of-state alternative. And Georgia law
thereby precludes the kind of method-of-execution claim
this Court told prisoners they could bring.
  One last point from Bucklew—this one about “dilatory”
tactics—bears repeating here. Id., at ___ (slip op., at 30).
In recognizing that §1983 is a good vehicle for a claim like
Nance’s, we do not for a moment countenance “last-minute”
claims relied on to forestall an execution. Ibid. “Courts
should police carefully against attempts to use [method-of-
execution] challenges as tools to interpose unjustified de-
lay.” Ibid. In deciding whether to grant a stay of execution,
courts must consider whether such a challenge “could have
been brought earlier” or otherwise reflects a prisoner’s “at-
tempt at manipulation.” Ibid. (internal quotation marks
omitted). And outside the stay context, courts have a vari-
ety of tools—including the “substantive [and] procedural
limitations” that the Prison Litigation Reform Act im-
poses—to streamline §1983 actions and protect “the timely
enforcement of a sentence.” Nelson, 541 U. S., at 650 (list-
ing PLRA limitations); Bucklew, 587 U. S., at ___ (slip op.,
at 29). Finally, all §1983 suits must be brought within a
State’s statute of limitations for personal-injury actions.
See Wallace v. Kato, 549 U. S. 384, 387 (2007). Here, the
District Court held Nance’s suit untimely under that limi-
tations period. See No. 20–cv–00107 (ND Ga., Mar. 13,
2020), ECF Doc. 26, p. 12; supra, at 4. The Eleventh Circuit
did not review that holding because it instead reconstrued
the action as a habeas petition. Now that we have held that
reconstruction unjustified, the court on remand can address
the timeliness question, as well as any others that remain.
                        *     *    *
   For the reasons stated, we reverse the judgment of the
Court of Appeals for the Eleventh Circuit and remand the
case for further proceedings consistent with this opinion.
14    NANCE v. WARD

     Opinion of the Court


                            It is so ordered.
                   Cite as: 597 U. S. ____ (2022)              1

                      BARRETT, J., dissenting

SUPREME COURT OF THE UNITED STATES
                           _________________

                            No. 21–439
                           _________________


    MICHAEL NANCE, PETITIONER v. TIMOTHY C.
     WARD, COMMISSIONER, GEORGIA DEPART-
         MENT OF CORRECTIONS, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
          APPEALS FOR THE ELEVENTH CIRCUIT
                          [June 23, 2022]

  JUSTICE BARRETT, with whom JUSTICE THOMAS, JUSTICE
ALITO, and JUSTICE GORSUCH join, dissenting.
  An inmate must bring a method-of-execution challenge in
a federal habeas application, rather than under 42 U. S. C.
§1983, if “a grant of relief to the inmate would necessarily
bar the execution.” Hill v. McDonough, 547 U. S. 573, 583
(2006). Under this criterion, Michael Nance must proceed
in habeas because a judgment in his favor would “neces-
sarily bar” the State from executing him. Ibid. Nance
asked the District Court to “enjoin the Defendants from pro-
ceeding with [his] execution . . . by a lethal injection,” claim-
ing that the use of such method would violate the Eighth
Amendment as applied to him. App. to Pet. for Cert. 103a–
104a. But lethal injection is the only method of execution
authorized under Georgia law. See Ga. Code Ann. §17–10–
38(a) (2020). Thus, if Nance is successful, the defendants
in this case—the commissioner of the Georgia Department
of Corrections and the warden—will be powerless to carry
out his sentence. That makes habeas the right vehicle for
Nance’s Eighth Amendment challenge.
  The Court sees things differently. True, Nance is arguing
that the Eighth Amendment renders his sentence invalid
under current Georgia law. But the Court points out that
2                      NANCE v. WARD

                     BARRETT, J., dissenting

the law could change: The legislature could authorize exe-
cution by firing squad, the alternative method that Nance
has proposed. In fact, the Court says that Nance’s proposal
offers Georgia a “veritable blueprint for carrying the death
sentence out.” Ante, at 8. So an order in Nance’s favor
would not “necessarily bar” the State from ever executing
Nance, in the Court’s view. Instead, the order would “giv[e]
the State a pathway forward” if the legislature chooses to
pursue the amendment process. Ibid.
   The Court is looking too far down the road. In my view,
the consequence of the relief that a prisoner seeks depends
on state law as it currently exists. And under existing state
law, there is no question that Nance’s challenge necessarily
implies the invalidity of his lethal injection sentence: He
seeks to prevent the State from executing him in the only
way it lawfully can.
   In this respect, Nance’s method-of-execution challenge
differs from those brought in Nelson v. Campbell, 541 U. S.
637 (2004), and Hill, 547 U. S. 573. In Nelson, the inmate
challenged the use of a “cut-down” procedure to access his
veins. 541 U. S., at 640–642. We held that the suit sounded
in §1983 because it would not “necessarily prevent Alabama
from carrying out its execution.” Id., at 647. We reasoned
that, though venous access was an indispensable prerequi-
site to lethal injection, “a particular means of gaining such
access” was not. Id., at 645. Notably, “[n]o Alabama statute
require[d] use of the cut-down,” and the State did not put
forward any “duly-promulgated regulations to the con-
trary.” Id., at 646. So even a successful challenge on these
grounds “would have allowed the State to proceed with the
execution as scheduled.” Ibid.
   The same was true in Hill, which involved an inmate’s
challenge to Florida’s three-drug protocol. 547 U. S., at 578.
We held that the inmate could proceed under §1983 because
his “action if successful would not necessarily prevent the
State from executing him by lethal injection.” Id., at 580.
                  Cite as: 597 U. S. ____ (2022)            3

                     BARRETT, J., dissenting

We emphasized that the complaint did “not challenge the
lethal injection sentence as a general matter” but instead
only “the anticipated protocol.” Ibid. As in Nelson, we
stressed that Florida law did “not require the department
of corrections to use the challenged procedure.” 547 U. S.,
at 580. The State was “free to use an alternative lethal in-
jection procedure,” and so we explained that “[u]nder these
circumstances a grant of injunctive relief could not be seen
as barring the execution of Hill’s sentence.” Id., at 580–581.
   Here, by contrast, the warden and the commissioner are
not free to use an alternative to lethal injection—so if Nance
succeeds, they cannot carry out his sentence. And though
the Court contends otherwise, that consequence “switches
Nance’s claim to the habeas track.” Ante, at 8. An inmate
can use §1983 actions to challenge many, if not most, as-
pects of prison administration. But when a challenge would
prevent a State from enforcing a conviction or sentence, the
more rigorous, federalism-protective requirements of ha-
beas apply. The Court finds a way around those require-
ments with a theory at odds with the very federalism inter-
ests they are designed to protect: that an injunction barring
the State from enforcing a sentence according to state law
does not really bar the State from enforcing the sentence
because the State can pass a new law.
   Unlike the Court, I would take state law as we find it in
determining whether a suit sounds in habeas or §1983. The
Court worries that this approach would make the appropri-
ate federal vehicle “depend on the vagaries of state law.”
Ante, at 11. Some States, like Georgia, provide for a single
method of execution by statute; other States, like Alabama,
allow for more flexibility. See ibid. So if state law deter-
mined the vehicle, an inmate in Georgia would have to chal-
lenge the lethal injection method in habeas, while an in-
mate in Alabama could use §1983. But that does not
illustrate “the vagaries of state law”; it is an unremarkable
consequence of federalism. States make different choices in
4                      NANCE v. WARD

                     BARRETT, J., dissenting

exercising their power to define punishment, and the law
has long recognized a sovereign’s interest in mandating a
particular form of capital punishment. Cf. 4 W. Blackstone,
Commentaries on the Laws of England 397 (1769) (a sheriff
would be “guilty of felony” if he “alter[ed] the manner of the
execution”). Habeas is appropriate in Georgia because un-
der Georgia law, to enjoin execution by lethal injection is to
enjoin enforcement of the sentence itself. See Ga. Code
Ann. §17–10–38(a) (“All persons who have been convicted
of a capital offense and have had imposed upon them a sen-
tence of death shall suffer such punishment by lethal injec-
tion”). In Alabama, enjoining execution by lethal injection
does not have the same effect. See Ala. Code §15–18–82.1(c)
(2018) (permitting execution “by any constitutional method
of execution” if the other methods provided for by statute
are held unconstitutional). The two sovereigns have made
different choices about how to define punishment, and fed-
eral law is designed to respect the choice of each.
   I understand the impulse to find a way out of habeas and
into §1983. In States like Georgia, a claim under Bucklew
v. Precythe, 587 U. S. ___ (2019), alleging an alternative
method of execution not presently authorized by state law
would be difficult to assert in a federal habeas application
because it would “almost inevitably collide with the second-
or-successive bar.” Ante, at 12. But we acknowledged that
very possibility in Bucklew. 587 U. S., at ___ (slip op., at
19). And more importantly, the unavailability of federal ha-
beas relief does not justify recourse to §1983. Cf. Wilkinson
v. Dotson, 544 U. S. 74, 87–88 (2005) (Scalia, J., concurring)
(“[A] prisoner who wishes to challenge the length of his con-
finement, but who cannot obtain federal habeas relief be-
cause of the statute of limitations or the restrictions on suc-
cessive petitions, cannot use the unavailability of federal
habeas relief in his individual case as grounds for proceed-
ing under §1983” (citations omitted)). The habeas statutes
funnel such challenges to the state courts—which are, after
                 Cite as: 597 U. S. ____ (2022)           5

                    BARRETT, J., dissenting

all, “the principal forum” for them. Harrington v. Richter,
562 U. S. 86, 103 (2011).
  For these reasons, I respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/Napue v. Illinois.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Napue v. Illinois"
type: case
citation: "360 U.S. 264 (1959)"
parallel_cite: "79 S. Ct. 1173; 3 L. Ed. 2d 1217"
neutral_cite: 1959 U.S. LEXIS 811
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Napue v. Illinois
  varies_by_point: false
  scope_note: "Foundational false-testimony due-process rule; carried into the Giglio line; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105912/napue-v-illinois/"
  cluster_id: 105912
  opinion_id: 105912
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "due-process", "false-testimony", "brady-giglio", "credibility"]
holding: "The State may not knowingly use false testimony to obtain a conviction, and that duty applies even when the false testimony goes only to…"
lake:
  record_id: Napue v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Napue v. Illinois

*360 U.S. 264 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At Napue's murder trial, the State's key witness — an accomplice already convicted of the same murder — falsely testified that he had received no promise of consideration in exchange for his testimony, when in fact the prosecutor had promised to help him. The prosecutor knew the testimony was false and did nothing to correct it.

## Issue
Whether the knowing use of false testimony violates due process even when the falsehood goes only to the witness's credibility rather than directly to the defendant's guilt.

## Rule
Yes. "[I]t is established that a conviction obtained through use of false evidence, known to be such by representatives of the State, must fall under the Fourteenth Amendment." — 360 U.S. at 269. ^pin-269

That principle "does not cease to apply merely because the false testimony goes only to the credibility of the witness," because the jury's estimate of a witness's truthfulness may be determinative of guilt or innocence. — *Id.* ^pin-269b

The duty applies as well when the State, though it did not solicit the false testimony, allows it to go uncorrected when it appears.

## Application
The accomplice's false denial of any deal went only to his credibility, but because the jury's assessment of his truthfulness could be determinative and the prosecutor knowingly allowed the false testimony to stand uncorrected, the conviction could not stand on these facts. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]: the prosecution's knowing use of the uncorrected false testimony violated due process.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Napue* is foundational to the prosecutorial-duty line later developed in [[Giglio v. United States]] and synthesized with [[Brady v. Maryland]]'s disclosure rule.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Napue v. Illinois*, 360 U.S. 264 (1959) — https://www.courtlistener.com/opinion/105912/napue-v-illinois/ — pinpoint: 269.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ea80528374bd548a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Napue v. Illinois"}, "payload": {"all": [{"cite": "360 U.S. 264", "page": "264", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "360"}, {"cite": "79 S. Ct. 1173", "page": "1173", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "79"}, {"cite": "3 L. Ed. 2d 1217", "page": "1217", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "3"}, {"cite": "1959 U.S. LEXIS 811", "page": "811", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1959"}], "display": "360 U.S. 264", "official": {"cite": "360 U.S. 264", "page": "264", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "360"}, "official_selection_present": true, "record_id": "Napue v. Illinois"}}
{"assertion_id": "8c4076543f5084b5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-269", "record_id": "Napue v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-269", "pinpoint_status": "slip-only", "quote": "--- # Napue v. Illinois *360 U.S. 264 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At Napue's murder trial, the State's key witness — an accomplice already convicted of the same murder — falsely testified that he had received no promise of consideration in exchange for his testimony, when in fact the prosecutor had promised to help him. The prosecutor knew the testimony was false and did nothing to correct it. ## Issue Whether the knowing use of false testimony violates due process even when the falsehood goes only to the witness's credibility rather than directly to the defendant's guilt. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Napue v. Illinois", "star_marker": null}}
{"assertion_id": "bcd8ca9624beb0fd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-269b", "record_id": "Napue v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-269b", "pinpoint_status": "slip-only", "quote": "does not cease to apply merely because the false testimony goes only to the credibility of the witness,", "quote_fidelity": "mismatch", "record_id": "Napue v. Illinois", "star_marker": null}}
{"assertion_id": "4b1371c869267138", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Napue v. Illinois"}, "payload": {"as_of_content": "1959-06-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Napue v. Illinois", "scope_note": "Foundational false-testimony due-process rule; carried into the Giglio line; good law.", "varies_by_point": false}}
```

### lake record — Napue v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Napue v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Napue v. Illinois",
    "case_name_short": "Napue",
    "case_name_full": "Napue v. Illinois",
    "input_case_name": "Napue v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-06-15",
    "year": 1959,
    "docket": null,
    "cluster_id": 105912,
    "lead_opinion_id": 105912,
    "sibling_ids": [
      105912
    ],
    "absolute_url": "/opinion/105912/napue-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "360 U.S. 264",
      "volume": "360",
      "reporter": "U.S.",
      "page": "264",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 1173",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1173",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1217",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 811",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "811",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "360 U.S. 264",
        "volume": "360",
        "reporter": "U.S.",
        "page": "264",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 1173",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1173",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1217",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 811",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "811",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "360 U.S. 264",
    "official_selection": {
      "court_class": "scotus",
      "selected": "360 U.S. 264",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-269",
      "page": null,
      "quote": "--- # Napue v. Illinois *360 U.S. 264 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At Napue's murder trial, the State's key witness \u2014 an accomplice already convicted of the same murder \u2014 falsely testified that he had received no promise of consideration in exchange for his testimony, when in fact the prosecutor had promised to help him. The prosecutor knew the testimony was false and did nothing to correct it. ## Issue Whether the knowing use of false testimony violates due process even when the falsehood goes only to the witness's credibility rather than directly to the defendant's guilt. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-269b",
      "page": null,
      "quote": "does not cease to apply merely because the false testimony goes only to the credibility of the witness,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Napue v. Illinois",
    "varies_by_point": false,
    "scope_note": "Foundational false-testimony due-process rule; carried into the Giglio line; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State Ex Rel. Darrell J. Robinson v. Darrel Vannoy, Warden, Louisiana State Penitentiary, Angola, Louisiana",
          "cluster_id": 10292764,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schmitt v. State",
          "cluster_id": 10680344,
          "cite": [
            "901 S.E.2d 102",
            "318 Ga. 835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sosa",
          "cluster_id": 9447945,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of a Grand Jury Investigation",
          "cluster_id": 4783492,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brady v. Maryland",
          "cluster_id": 106598,
          "cite": [
            "10 L. Ed. 2d 215",
            "83 S. Ct. 1194",
            "373 U.S. 83",
            "1963 U.S. LEXIS 1615"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Giglio v. United States",
          "cluster_id": 108471,
          "cite": [
            "31 L. Ed. 2d 104",
            "92 S. Ct. 763",
            "405 U.S. 150",
            "1972 U.S. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santobello v. New York",
          "cluster_id": 108416,
          "cite": [
            "30 L. Ed. 2d 427",
            "92 S. Ct. 495",
            "404 U.S. 257",
            "1971 U.S. LEXIS 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donnelly v. DeChristoforo",
          "cluster_id": 109024,
          "cite": [
            "40 L. Ed. 2d 431",
            "94 S. Ct. 1868",
            "416 U.S. 637",
            "1974 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marion",
          "cluster_id": 108420,
          "cite": [
            "30 L. Ed. 2d 468",
            "92 S. Ct. 455",
            "404 U.S. 307",
            "1971 U.S. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Ritchie",
          "cluster_id": 111822,
          "cite": [
            "94 L. Ed. 2d 40",
            "107 S. Ct. 989",
            "480 U.S. 39",
            "1987 U.S. LEXIS 558",
            "55 U.S.L.W. 4180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hinkson",
          "cluster_id": 1191667,
          "cite": [
            "585 F.3d 1247",
            "2009 U.S. App. LEXIS 24358",
            "2009 WL 3645003"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boyde v. California",
          "cluster_id": 112386,
          "cite": [
            "108 L. Ed. 2d 316",
            "110 S. Ct. 1190",
            "494 U.S. 370",
            "1990 U.S. LEXIS 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estes v. Texas",
          "cluster_id": 107083,
          "cite": [
            "14 L. Ed. 2d 543",
            "85 S. Ct. 1628",
            "381 U.S. 532",
            "1965 U.S. LEXIS 2339",
            "1 Media L. Rep. (BNA) 1187",
            "6 Rad. Reg. 2d (P & F) 2104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burgett v. Texas",
          "cluster_id": 107540,
          "cite": [
            "19 L. Ed. 2d 319",
            "88 S. Ct. 258",
            "389 U.S. 109",
            "1967 U.S. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 108613,
          "cite": [
            "33 L. Ed. 2d 706",
            "92 S. Ct. 2562",
            "408 U.S. 786",
            "1972 U.S. LEXIS 23"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105912) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg2MjE3NjAwMDAwJnM9NDc0Mjg1MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105912%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(105912)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MjQmcz04Njc0NzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105912%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105912)",
        "reviewed": 121,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 121,
        "triage_read": 3,
        "triage_snippet_classified": 118
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(105912)",
    "indexed_citing_opinions": 2479,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105912,
        "count": 2479,
        "count_source": "search"
      }
    ],
    "citation_count": 4249,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/napue-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzczOTkmcz0xMDU1MzA3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28105912%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105912,
        "cited_id": 85160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 97658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 97816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 100264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 101991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 102101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 229184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 236467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 238555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 246192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 1550123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 2107640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 2354547,
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
    "date_created": "2026-07-05T14:54:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:56:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Napue v. Illinois

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b307-3">
<span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
  Mr. Chief Justice Warren
 </author>
<p id="Ago">
  delivered the opinion of the Court.
 </p>
<p id="b307-4">
  At the murder trial- of petitioner the principal state witness, then serving a 199-year sentence for the same murder, testified in response to a question by the Assistant State’s Attorney that he had received no promise of consideration in return for his testimony. The Assistant State’s Attorney had in fact promised him consideration, but did nothing to correct the witness’ false testimony. The jury was apprised, however, that' a public defender had promised “to do what he could” for the witness. The question presented is whether on these facts the failure of the prosecutor to correct the testimony of the witness which he knew to be false denied petitioner due process of law in violation of the Fourteenth Amendment to the Constitution, of the United States.
 </p>
<p id="b307-5">
  The record in this Court contains testimony from which the following facts could have been found. The murder in question occurred early in the morning of August 21, 1938, in a Chicago, Illinois, cocktail lounge., Petitioner Henry Napue, the witness George Hamer, one Poe and one Townsend entered the dimly lighted lounge and announced their intention to rob those present. An off-duty policeman, present in the lounge, drew his service revolver and began firing at the four men. In the melee that followed Townsend was killed, the officer wás fatally wounded, and the witness Hamer was seriously wounded. Napue and Poe carried Hamer to the car where a fifth man, one Webb, was waiting. In due course Hamer was apprehended, tried for the murder of the policeman, convicted on his plea of guilty and sentenced to 199 years. Subsequently, Poe was apprehended, tried, convicted, sentenced to death and executed. Hamer was not-used as a witness.
 </p>
<p id="b307-6">
  Thereafter, petitioner Napue was apprehended. He was put ón trial with 'Hamer being the principal witness
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  for the State. Hamer’s testimony was. extremely important because the passage of time and the dim light in the cocktail lounge made eyewitness identification very difficult and uncertain, and because some pertinent witnesses had left the state. On the basis of the evidence presented, which consisted largely of Hamer’s testimony, the jury returned a. guilty verdict and petitioner was sentenced to 199 years.
 </p>
<p id="b308-4">
  Finally, the driver of the car, Webb, was apprehended. Hamer also testified against him. He was convicted of murder and sentenced-to 199 years.
 </p>
<p id="b308-5">
  Following the conviction of Webb, the lawyer who, as former Assistant State’s_Attorney, had prosecuted the Hamer, Poe and Napue cases filed a petition in the nature of a writ of error
  <em>
   coram nobis
  </em>
  on “behalf of Hamer. In the petition he alleged that as prosecuting attorney he had promised Hamer that if he would testify against Napue, “a recommendation for a reduction of his [Hamer’s] sentence would be made and, if possible, effectuated.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  attorney prayed that the court would effect “consummation of the compact entered into between the duly authorized representatives of the State of Illinois and George Hamer.”
 </p>
<p id="b309-4">
  This
  <em>
   coram nobis
  </em>
  proceeding came to the attention of Napue, who thereafter filed a post-conviction petition,- in which he alleged that Hamer had falsely testified that he had been promised no consideration for his testimony,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and that the Assistant State’s Attorney handling the case had known this to be false. A hearing was ultimately held at which the former Assistant State’s Attorney testified that he had only'promised to help Hamer if Hamer’s story “about being a reluctant participant” in the robbery was borne out, and not merely if Hamer would testify at petitioner’s trial. He testified that in his
  <em>
   coram nobis
  </em>
  petition on Hamer’s behalf he “probably .used some language that [he] should not. have used” in his “zeal to do something for Hamer” to whom he “felt a, moral obligation.” The lower court denied petitioner relief on the basis of the attorney’s testimony.
 </p>
<p id="b309-5">
  On appeal, the Illinois Supreme Court affirmed on di£-' ferent‘grounds over two dissents. <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">13 Ill. 2d 566</a></span>, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">150 N. E. 2d 613</a></span>. It fcjiind,' contrary to the trial éourt, that the attorney had promised Hamer consideration if he would testify at petitioner’s trial, a finding which the State does not contest here. It further found that the Assistant State’s Attorney knew that Hamer had lied in denying that
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  he had been promised consideration. It held, however, that petitioner was entitled to no relief since the jury had already been apprised that someone whom Hamer had tentatively identified as being a public defender “was going to do what he could” in aid of Hamer, and “was trying to get something did” for him.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We granted cer
  <span citation-index="1" class="star-pagination" label="269"> 
   *269
   </span>
  tiorari to considér the question posed in the first paragraph of this opinion. <span class="citation multiple-matches"><a href="/c/U.%20S./358/919/">358 U. S. 919</a></span>.
 </p>
<p id="AEf">
<em>
   First,
  </em>
  it is established that a conviction obtained through use of false evidence, known to be such by representatives of the State, must fall under the Fourteenth Amendment,
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>;
  <em>
   Pyle
  </em>
  v. Kansas, <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span>;
  <em>
   Curran
  </em>
  v.
  <em>
   Delaware,
  </em>
  <span class="citation" data-id="246192"><a href="/opinion/246192/francis-j-curran-francis-j-maguire-and-ira-f-jones-jr-v-state-of/" aria-description="Citation for case: Francis J. Curran, Francis J. Maguire and Ira F. Jones,...">259 F. 2d 707</a></span>. See
  <em>
   New York ex rel. Whitman
  </em>
  v.
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="103813"><a href="/opinion/103813/new-york-ex-rel-whitman-v-wilson/" aria-description="Citation for case: New York Ex Rel. Whitman v. Wilson">318 U. S. 688</a></span>, and
  <em>
   White
  </em>
  v.
  <em>
   Ragen,
  </em>
  <span class="citation" data-id="104125"><a href="/opinion/104125/white-v-ragen/" aria-description="Citation for case: White v. Ragen">324 U. S. 760</a></span>. Compare
  <em>
   Jones
  </em>
  v.
  <em>
   Commonwealth,
  </em>
  <span class="citation" data-id="1550123"><a href="/opinion/1550123/jones-v-commonwealth-of-kentucky/#338" aria-description="Citation for case: Jones v. Commonwealth of Kentucky">97 F. 2d 335, 338</a></span>, with
  <em>
   In re Sawyer’s Petition,
  </em>
  <span class="citation" data-id="238555"><a href="/opinion/238555/petition-for-writ-of-habeas-corpus-for-walter-j-sawyer-walter-j-sawyer/#809" aria-description="Citation for case: Petition for Writ of Habeas Corpus for Walter J. Sawyer....">229 F. 2d 805, 809</a></span>. Cf.
  <em>
   Mesarosh
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421334"><a href="/opinion/105421/mesarosh-v-united-states/" aria-description="Citation for case: Mesarosh v. United States">352 U. S. 1</a></span>. The same result obtains when the State, although not soliciting false evidence, allows it to go unconnected when it appears.
  <em>
   Alcorta
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>;
  <em>
   United States ex rel. Thompson
  </em>
  v.
  <em>
   Dye,
  </em>
  <span class="citation" data-id="9444580"><a href="/opinion/236467/united-states-of-america-ex-rel-cleveland-thompson-v-charles-l-dye/" aria-description="Citation for case: United States of America Ex Rel. Cleveland Thompson v....">221 F. 2d 763</a></span>;
  <em>
   United States ex rel. Almeida
  </em>
  v.
  <em>
   Baldi,
  </em>
  <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d 815</a></span>;
  <em>
   United States ex rel. Montgomery
  </em>
  v.
  <em>
   Ragen,
  </em>
  <span class="citation" data-id="2354547"><a href="/opinion/2354547/united-states-ex-rel-montgomery-v-ragen/" aria-description="Citation for case: United States Ex Rel. Montgomery v. Ragen">86 F. Supp. 382</a></span>. See generally annotation, <span class="citation no-link">2 L. Ed. 2d 1575</span>.
 </p>
<p id="b311-5">
  The principle that a State may not knowingly úse false evidence, including false testimony, to obtain a tainted conviction, implicit in any concept of ordered liberty, does not cease to apply merely because the false testimony goes only to the credibility of the witness. The jury’s estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence; and it is upon such subtle factors as the possible interest of the witness' in testifying falsely that a defendant’s life or liberty may depend. As stated by the New York Court of Appeals in a case very similar to this one,
  <em>
   People
  </em>
  v.
  <em>
   Savvides,
  </em>
  1 N. Y. 2d 554, 557; <span class="citation" data-id="5515949"><a href="/opinion/5668946/people-v-savvides/#854" aria-description="Citation for case: People v. Savvides">136 N. E. 2d 853, 854-855</a></span>; 154 N. Y. S. 2d 885, 887:
 </p>
<blockquote id="b311-6">
  “It is of no consequence that the falsehood bore upon the witness’ credibility rather than directly upon defendant’s guilt. A lie is a lie, no matter
  <span citation-index="1" class="star-pagination" label="270"> 
   *270
   </span>
  what its subject, and, if it is in any way relevant to the case, the district, attorney has the responsibility and duty to correct what he knows to be false and elicit the truth. . . . That the district attorney’s silence was not the result of guile or a desire to prejudice matters little, for its impact was the same, preventing, as it did, a trial that could in any real sense be termed fair.”
 </blockquote>
<p id="b312-4">
<em>
   Second,
  </em>
  we do not believe that the fact that the jury was apprised of other grounds for believing that the witness Hamer may have had an interest in testifying against petitioner turned what was otherwise a tainted trial into a fair one. &gt; As Mr. Justice Schaefer, joined by Chief Justice Davis, rightly put it in his dissenting opinion below, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/#571" aria-description="Citation for case: Napue v. THE PEOPLE">13 Ill. 2d 566, 571</a></span>, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">150 N. E. 2d 613</a></span>, 616:
 </p>
<blockquote id="b312-5">
  “What is overlooked here is that Hamer clearly testified that no one had offered to help him except an unidentified lawyer from the public defender’s office.”
 </blockquote>
<p id="b312-6">
  Had the jury been apprised, of the true facts, however, it might well have concluded that Hamer had fabricated testimony in order to curry the favor of the very representative of the State who was prosecuting the case in which Hamer was testifying, for Hamer might-have believed that such a representative was in a position to. implement (as he ultimately attempted to do) any promise of consideration. That the Assistant State’s Attorney himself thought it important to establish before the jury that no official source had promised Hamer consideration is made clear by his redirect examination, which was the last testimony of Hamer’s heard by the jury:
 </p>
<blockquote id="b312-7">
  “Q. Mr. Hamer, has Judge Prystalski [the trial judge] promised you any reduction of sentence?
 </blockquote>
<blockquote id="b313-5">
<span citation-index="1" class="star-pagination" label="271"> 
   *271
   </span>
  “A. No,, sir.
 </blockquote>
<blockquote id="b313-6">
  “Q. Have I promised you that I would recommend any reduction of sentence^to anybody?
 </blockquote>
<blockquote id="b313-7">
  “A. You did hot. [That answer was false and known to be so by the prosecutor.]
 </blockquote>
<blockquote id="b313-8">
  . “Q. Has any Judge of the criminal court promised that they [sic] would reduce your sentence?
 </blockquote>
<blockquote id="b313-9">
  “A. No, sir.
 </blockquote>
<blockquote id="b313-10">
  “Q. Has any representative of the Parole Board been to see you and promised you a reduction of sentence?
 </blockquote>
<blockquote id="b313-11">
  ' “A. No, sir.-
 </blockquote>
<blockquote id="b313-12">
  “Q. Has any representative of the Governor of the State of Illinois promised you a reduction of sentence?
 </blockquote>
<blockquote id="b313-13">
  “A. No, sir.”
 </blockquote>
<p id="b313-14">
  We are therefore unable to agree with the Illinois Supreme Court that “there was no constitutional infirmity by virtue of the false statement.”
 </p>
<p id="b313-15">
<em>
   Third,
  </em>
  the State argues that we are not free to reach a factual conclusion different from that reached by the Illinois Supreme Court, and that we are bound by its determination that the false testimony could not in any reasonable likelihood have affected the judgment of the jury. The State relies on
  <em>
   Hysler
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="9419213"><a href="/opinion/103621/hysler-v-florida/" aria-description="Citation for case: Hysler v. Florida">315 U. S. 411</a></span>. But in that case the Court held only that a state standard of specificity and substantiality in making allegations of federal constitutional deprivations .would be respected, and this Court made its own “independent examination” of the allegations there, to determine if they had in fact met the Florida standard. The duty of this Court to make its own independent examination of the record when federal constitutional deprivations are alleged is clear, resting, as it does, on our solemn responsibility for main-' taining the Constitution inviolate.
  <em>
   Martin
  </em>
  v.
  <em>
   Hunter’s Lessee,
  </em>
  <span class="citation" data-id="85160"><a href="/opinion/85160/martin-v-hunters-lessee/" aria-description="Citation for case: Martin v. Hunter&#x27;s Lessee">1 Wheat. 304</a></span>;
  <em>
   Cooper
  </em>
  v.
  <em>
   Aaron,
  </em>
  <span class="citation" data-id="9421708"><a href="/opinion/105766/cooper-v-aaron/" aria-description="Citation for case: Cooper v. Aaron">358 U. S. 1</a></span>.
  <span citation-index="1" class="star-pagination" label="272"> 
   *272
   </span>
  This principle was well stated in
  <em>
   Niemotko
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9420519"><a href="/opinion/104842/niemotko-v-maryland/" aria-description="Citation for case: Niemotko v. Maryland">340 U. S. 268</a></span>, 271:
 </p>
<blockquote id="b314-4">
  “In cases in which there is a claim of denial of rights under the Federal Constitution, this Court is not bound by the conclusions of lower courts, but will reexamine the evidentiary basis on which those conclusions are founded.”
 </blockquote>
<p id="b314-5">
  It is now so well settled that the Court was able to speak in
  <em>
   Kern-Limerick, Inc.,
  </em>
  v.
  <em>
   Scurlock,
  </em>
  <span class="citation" data-id="9421036"><a href="/opinion/105193/kern-limerick-inc-v-scurlock/#121" aria-description="Citation for case: Kern-Limerick, Inc. v. Scurlock">347 U. S. 110, 121</a></span>, of the “long course of judicial construction which establishes as a principle that the duty rests on this Court to decide for itself facts or constructions upon which federal constitutional issues rest.”
  <a class="footnote" href="#fn4" id="fn4_ref">
<em>
    4
   </em>
</a>
<em>
</em>
  As previously indicated, our own evaluation of the record here compels us to hold that the false testimony used by the State in securing the conviction of petitioner may have had an effect on the outcome of the trial. Accordingly, the judgment below must be
 </p>
<p id="b314-6">
<em>
   Reversed.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b308-6">
   In relevant part, his petition read as follows:
  </p>
<blockquote id="b308-7">
   “After Hamer was sentenced your petitioner [the Assistant State’s Attorney] well knowing that identification of Poe, Napue and Webb if and when apprehended would be of an unsatisfactory character and not the kind of evidence upon which a jury could be asked to inflict a proper, severe penalty, and being unable to determine in advance whether Poe, Napue and Webb would make confessions of their participation in the' crime, represented to Hamer that if he would be willing to cooperate with law enforcing officials upon the trial of [sic] trials of Poe, Napue and Webb when they were apprehended, that a recommendation for a reduction of his sentence would be made-and, if possible, effectuated.
  </blockquote>
<blockquote id="b308-8">
   “Before testifying oh behalf of the State and against Napue, Hamer expressed to your petitioner a reluctance to cooperate any further Unless he were given definite assurance that a recommendation for reduction of his sentence would be made. Your petitioner, feeling that the interests of justice required Hamer’s testimony, again assured Hamer that every possible effort would be made to conform to the promise previously made to him.”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b309-6">
   The alleged false testimony of Hamer first occurred on his cross-examination :
  </p>
<blockquote id="b309-7">
   “Q. Did anybody give you a reward or promise you a reward for testifying?
  </blockquote>
<blockquote id="b309-8">
   ‘.‘A. There ain’t nobody promised me anything.”
  </blockquote>
<blockquote id="b309-9">
   On redirect examination the Assistant State’s Attorney again elicited' the same false answer.
  </blockquote>
<blockquote id="b309-10">
   “Q. [by the-Assistant State's Attorney] Have I promised you that I would recommend any reduction of sentence to anybody?
  </blockquote>
<blockquote id="b309-11">
   “A. You did not.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b310-5">
   The following is Hamer’s testimony on one subject:
  </p>
<blockquote id="b310-6">
   “Q. [on cross-examination] And didn’t you tell him [one of Napue’s •attorneys] that you wouldn’t testify in this ease unless you got some consideration for it ?
  </blockquote>
<blockquote id="b310-7">
   “A. ... Yes, I did; I told him that.
  </blockquote>
<blockquote id="b310-8">
   “Q. What are you sentenced for?
  </blockquote>
<blockquote id="b310-9">
   “A. One Hundred and Ninety-Nine Years. ‘
  </blockquote>
<blockquote id="b310-10">
   “Q. You hope to have that reduced, don’t you?
  </blockquote>
<blockquote id="b310-11">
   “A. Well, if anybody would help me or do anything for me, why certainly I would.
  </blockquote>
<blockquote id="b310-12">
   “Q. Weren’t you expecting that when you came here today?
  </blockquote>
<blockquote id="b310-13">
   “A. There haven’t no one told pie anything, no more than the lawyer. The lawyer come in and talked to me a while ago and said he was going to do what he could.
   <em>
    f &gt;
   </em>
</blockquote>
<blockquote id="b310-14">
   “Q. Which lawyer was that?
  </blockquote>
<blockquote id="b310-15">
<em>
    “A.
   </em>
   I don’t know; it was a Public Defender.' I don’t see him in here.
   <em>
    ¡,
   </em>
</blockquote>
<blockquote id="b310-16">
   “Q. You mean he was from the Public Defender s office?
  </blockquote>
<blockquote id="b310-17">
   “A. I imagine that is where he was from, I don’t know.-
  </blockquote>
<blockquote id="b310-18">
   “Q. And he was the one who told you that?
  </blockquote>
<blockquote id="b310-19">
   “A. Yes, he told me he was trying to get something did for me.
  </blockquote>
<blockquote id="b310-20">
   “Q. . . . And he told you he was going to do something for you ?
  </blockquote>
<blockquote id="b310-21">
   “A. He said he was going to try to.
  </blockquote>
<blockquote id="b310-22">
   “Q.'And you told them [police officers] you would [testify at the trial of Napue] but you expected some consideration for it?
  </blockquote>
<blockquote id="b310-23">
   “A. I asked them was there any chance of me getting any. The man told me he didn’t know, that he couldn’t promise me anything.
  </blockquote>
<blockquote id="b310-24">
   “Q. Then you spoke to a lawyer today who said he would try to get yoúr time cut?
  </blockquote>
<blockquote id="b310-25">
<em>
    “A.
   </em>
   That was this Public Defender. I don’t even know his name. . . .”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b314-7">
   See,
   <em>
    e. g., Payne
   </em>
   v.
   <em>
    Arkansas,
   </em>
   <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#562" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 562</a></span>;
   <em>
    Leyra
   </em>
   v.
   <em>
    Denno,
   </em>
   <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span>;
   <em>
    Avery
   </em>
   v.
   <em>
    Georgia,
   </em>
   <span class="citation" data-id="9420951"><a href="/opinion/105128/avery-v-georgia/#561" aria-description="Citation for case: Avery v. Georgia">345 U. S. 559, 561</a></span>;
   <em>
    Feiner
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9420523"><a href="/opinion/104844/feiner-v-new-york/#322" aria-description="Citation for case: Feiner v. New York">340 U. S. 315, 322, 323, note 4</a></span> (dissenting opinion);
   <em>
    Cassell
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="9420469"><a href="/opinion/104785/cassell-v-texas/#283" aria-description="Citation for case: Cassell v. Texas">339 U. S. 282, 283</a></span>;
   <em>
    Holey
   </em>
   v.
   <em>
    Ohio,
   </em>
   <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599</a></span>;
   <em>
    Malinski
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span>;
   <em>
    Ashcraft
   </em>
   v.
   <em>
    Tennessee,
   </em>
   <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#149" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 149</a></span>;
   <em>
    Ward
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#550" aria-description="Citation for case: Ward v. Texas">316 U. S. 547, 550</a></span>;
   <em>
    Smith
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="103391"><a href="/opinion/103391/smith-v-texas/#130" aria-description="Citation for case: Smith v. Texas">311 U. S. 128, 130</a></span>;
   <em>
    South Carolina
   </em>
   v.
   <em>
    Bailey,
   </em>
   <span class="citation" data-id="102101"><a href="/opinion/102101/south-carolina-v-bailey/#420" aria-description="Citation for case: South Carolina v. Bailey">289 U. S. 412, 420</a></span>. See also,
   <em>
    e. g., Roth
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/#497" aria-description="Citation for case: Roth v. United States">354 U. S. 476, 497</a></span> (dissenting opinion);
   <em>
    Stroble
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span>;
   <em>
    Sterling
   </em>
   v.
   <em>
    Constantin,
   </em>
   <span class="citation" data-id="101991"><a href="/opinion/101991/sterling-v-constantin/#398" aria-description="Citation for case: Sterling v. Constantin">287 U. S. 378, 398</a></span>;
   <em>
    Southern Pacific Co.
   </em>
   v.
   <em>
    Schuyler,
   </em>
   <span class="citation" data-id="97816"><a href="/opinion/97816/southern-pacific-co-v-schuyler/#611" aria-description="Citation for case: Southern Pacific Co. v. Schuyler">227 U. S. 601, 611</a></span>;
   <em>
    Creswill
   </em>
   v.
   <em>
    Grand Lodge Knights of Pythias,
   </em>
   <span class="citation" data-id="9418222"><a href="/opinion/97658/creswill-v-grand-lodge-knights-of-pythias-of-georgia/#261" aria-description="Citation for case: Creswill v. Grand Lodge Knights of Pythias of Georgia">225 U. S. 246, 261</a></span>.
  </p>
<p id="b314-8">
   Mr. Justice Holmes, writing for the Court, recognized the principle over 35 years ago in
   <em>
    Davis
   </em>
   v.
   <em>
    Wechsler,
   </em>
   <span class="citation" data-id="100264"><a href="/opinion/100264/davis-v-wechsler/" aria-description="Citation for case: Davis v. Wechsler">263 U. S. 22</a></span>, 24:
  </p>
<blockquote id="b314-9">
   “If the Constitution and laws of the United States are to be enforced, this Court cannot accept as final the decision of a state -tribunal as (to what are the facts alleged to give rise to the right or to bar the assertion of it even upon local grounds.”
  </blockquote>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Nardone v. United States.json  (`lake-record`, 5 assertions)

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
{"assertion_id": "4a142d4956d844f2", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Nardone v. United States"}, "payload": {"all": [{"cite": "308 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "308"}, {"cite": "60 S. Ct. 266", "page": "266", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "84 L. Ed. 307", "page": "307", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "1939 U.S. LEXIS 1132", "page": "1132", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1939"}], "display": "308 U.S. 338", "official": {"cite": "308 U.S. 338", "page": "338", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "308"}, "official_selection_present": true, "record_id": "Nardone v. United States"}}
{"assertion_id": "b229c2afb313728f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-341b", "record_id": "Nardone v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-341b", "pinpoint_status": "slip-only", "quote": "As a matter of good sense … such connection may have become so attenuated as to dissipate the taint.", "quote_fidelity": "mismatch", "record_id": "Nardone v. United States", "star_marker": null}}
{"assertion_id": "cb2925735cf35d8f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-340", "record_id": "Nardone v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-340", "pinpoint_status": "slip-only", "quote": "), which held intercepted wiretap evidence inadmissible under § 605 of the Communications Act. ## Background After *Nardone I* reversed the petitioners' fraud convictions because the prosecution rested on unlawfully intercepted telephone calls, they were retried and reconvicted. At the new trial the judge refused to let the defense examine the prosecution about the *uses* it had made of the wiretap information. The Court of Appeals read § 605 narrowly — barring only the intercepted words themselves, while allowing every derivative use of the unlawful taps. ## Issue Whether the statutory bar on using unlawfully intercepted communications excludes only the intercepted words, or also bars the Government's derivative use of leads and evidence obtained from the illegal interception. ## Rule Derivative use is barred. Quoting *Silverthorne*, the Court reaffirmed that illegally obtained evidence", "quote_fidelity": "mismatch", "record_id": "Nardone v. United States", "star_marker": null}}
{"assertion_id": "f125e4086cc4bb3c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-341", "record_id": "Nardone v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-341", "pinpoint_status": "slip-only", "quote": "the trial judge must give opportunity, however closely confined, to the accused to prove that a substantial portion of the case against him was a *fruit of the poisonous tree*. This leaves ample opportunity to the Government to convince the trial court that its proof had an independent origin.", "quote_fidelity": "mismatch", "record_id": "Nardone v. United States", "star_marker": null}}
{"assertion_id": "01db28ac718c7003", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Nardone v. United States"}, "payload": {"as_of_content": "1939-12-11", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Nardone v. United States", "scope_note": "Foundational good law. Though arising under § 605 of the Communications Act, its 'fruit of the poisonous tree' and attenuation doctrine was carried into Fourth Amendment exclusionary-rule law (Wong Sun, Brown v. Illinois) and remains controlling.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/National Treasury Employees Union v. Von Raab.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "National Treasury Employees Union v. Von Raab"
type: case
citation: "489 U.S. 656 (1989)"
parallel_cite: "109 S. Ct. 1384; 103 L. Ed. 2d 685; 1989 CCH OSHD 28,589; 4 I.E.R. Cas. (BNA) 246; 57 U.S.L.W. 4338; 49 Empl. Prac. Dec. (CCH) 38,792"
neutral_cite: 1989 U.S. LEXIS 6033
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-03-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: National Treasury Employees Union v. Von Raab
  varies_by_point: false
  scope_note: "Special-needs suspicionless-testing precedent; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/"
  cluster_id: 112220
  opinion_id: 9431609
  identity_checked: true
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Skinner v. Railway Labor Executives' Association]]", "[[New Jersey v. T.L.O.]]", "[[Vernonia School District 47J v. Acton]]", "[[Chandler v. Miller]]"]
aliases: ["Von Raab", "NTEU v. Von Raab"]
tags: ["case", "fourth-amendment", "special-needs", "drug-testing", "administrative-search"]
holding: "Suspicionless drug testing of Customs employees seeking drug-interdiction or firearm-carrying positions is reasonable under the…"
lake:
  record_id: National Treasury Employees Union v. Von Raab
  status: verified
  projected_at: 2026-07-09
---

# National Treasury Employees Union v. Von Raab

*489 U.S. 656 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The U.S. Customs Service adopted a drug-screening program requiring urinalysis for employees seeking transfer or promotion to positions involving drug interdiction, the carrying of firearms, or the handling of classified material. The employees' union challenged the suspicionless testing under the Fourth Amendment.

## Issue
Whether suspicionless drug testing of Customs employees who seek such positions is a reasonable search under the Fourth Amendment.

## Rule
Where a search serves a special governmental need beyond ordinary law enforcement, reasonableness is determined by balancing, and a warrant or individualized suspicion may be unnecessary: "where a Fourth Amendment intrusion serves special governmental needs, beyond the normal need for law enforcement, it is necessary to balance the individual's privacy expectations against the Government's interests to determine whether it is impractical to require a warrant or some level of individualized suspicion in the particular context." — 489 U.S. at 665–66. ^pin-665

Employees in such sensitive roles have a reduced privacy interest: "Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test." — [*Id.* at 672](https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/#:~:text=Customs%20employees%20who%20are%20directly). ^pin-672

## Application
The Customs program was not designed to serve ordinary law enforcement, and its results could not be used in a criminal prosecution without the employee's consent. Balancing the Government's compelling interest in the integrity of the borders and in keeping firearms out of the hands of drug users against the diminished privacy of employees who seek those specific positions, the testing of applicants for drug-interdiction and firearm-carrying positions was reasonable. The Court [[Reading and Citing Cases#on-remand|remanded]] as to the classified-materials category for clarification of which positions it actually covered.

## Conclusion
Suspicionless testing of applicants for drug-interdiction and firearms positions was upheld as reasonable; the case was [[Reading and Citing Cases#on-remand|remanded]] for further consideration of the classified-materials category.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Decided with [[Skinner v. Railway Labor Executives' Association]], *Von Raab* is a leading special-needs precedent later applied in the school-testing context ([[Vernonia School District 47J v. Acton]]) and distinguished where the asserted need was not substantial ([[Chandler v. Miller]]).

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Progeny / Refinement*

## Sources
- *National Treasury Employees Union v. Von Raab*, 489 U.S. 656 (1989) — https://www.courtlistener.com/opinion/112220/national-treasury-employees-union-v-von-raab/ — pinpoints: 665–66, 672.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "781263432fb6b96c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "National Treasury Employees Union v. Von Raab"}, "payload": {"all": [{"cite": "489 U.S. 656", "page": "656", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "489"}, {"cite": "109 S. Ct. 1384", "page": "1384", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "103 L. Ed. 2d 685", "page": "685", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "1989 U.S. LEXIS 6033", "page": "6033", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "1989 CCH OSHD 28,589", "page": "28,589", "reporter": "CCH OSHD", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "1989"}, {"cite": "4 I.E.R. Cas. (BNA) 246", "page": "246", "reporter": "I.E.R. Cas. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "4"}, {"cite": "57 U.S.L.W. 4338", "page": "4338", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}, {"cite": "49 Empl. Prac. Dec. (CCH) 38,792", "page": "38,792", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "489 U.S. 656", "official": {"cite": "489 U.S. 656", "page": "656", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "489"}, "official_selection_present": true, "record_id": "National Treasury Employees Union v. Von Raab"}}
{"assertion_id": "1b0319239161fd98", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-672", "record_id": "National Treasury Employees Union v. Von Raab"}, "payload": {"fragment": "#:~:text=Customs%20employees%20who%20are%20directly", "page": null, "pin_id": "pin-672", "pinpoint_status": "star-verified", "quote": "Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test.", "quote_fidelity": "matched", "record_id": "National Treasury Employees Union v. Von Raab", "star_marker": "672"}}
{"assertion_id": "48cda930cd2882cf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-665", "record_id": "National Treasury Employees Union v. Von Raab"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-665", "pinpoint_status": "slip-only", "quote": "--- # National Treasury Employees Union v. Von Raab *489 U.S. 656 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The U.S. Customs Service adopted a drug-screening program requiring urinalysis for employees seeking transfer or promotion to positions involving drug interdiction, the carrying of firearms, or the handling of classified material. The employees' union challenged the suspicionless testing under the Fourth Amendment. ## Issue Whether suspicionless drug testing of Customs employees who seek such positions is a reasonable search under the Fourth Amendment. ## Rule Where a search serves a special governmental need beyond ordinary law enforcement, reasonableness is determined by balancing, and a warrant or individualized suspicion may be unnecessary:", "quote_fidelity": "mismatch", "record_id": "National Treasury Employees Union v. Von Raab", "star_marker": null}}
{"assertion_id": "d2226cb199552309", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "National Treasury Employees Union v. Von Raab"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "National Treasury Employees Union v. Von Raab", "scope_note": "Special-needs suspicionless-testing precedent; good law.", "varies_by_point": false}}
```

### lake record — National Treasury Employees Union v. Von Raab

```json
{
  "schema_version": "s2.v1",
  "record_id": "National Treasury Employees Union v. Von Raab",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "National Treasury Employees Union v. Von Raab",
    "case_name_short": "Von Raab",
    "case_name_full": "NATIONAL TREASURY EMPLOYEES UNION Et Al. v. VON RAAB, COMMISSIONER, UNITED STATES CUSTOMS SERVICE",
    "input_case_name": "National Treasury Employees Union v. Von Raab",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": null,
    "cluster_id": 112220,
    "lead_opinion_id": 9431609,
    "sibling_ids": [
      112220,
      9431609,
      9431610,
      9431611
    ],
    "absolute_url": "/opinion/112220/national-treasury-employees-union-v-von-raab/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 656",
      "volume": "489",
      "reporter": "U.S.",
      "page": "656",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1384",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 685",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,589",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,589",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 246",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "246",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4338",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4338",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,792",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,792",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 6033",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "6033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 656",
        "volume": "489",
        "reporter": "U.S.",
        "page": "656",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1384",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1384",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 685",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "685",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 6033",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "6033",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 CCH OSHD 28,589",
        "volume": "1989",
        "reporter": "CCH OSHD",
        "page": "28,589",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 I.E.R. Cas. (BNA) 246",
        "volume": "4",
        "reporter": "I.E.R. Cas. (BNA)",
        "page": "246",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4338",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4338",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 Empl. Prac. Dec. (CCH) 38,792",
        "volume": "49",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "38,792",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 656",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 656",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-665",
      "page": null,
      "quote": "--- # National Treasury Employees Union v. Von Raab *489 U.S. 656 (1989)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The U.S. Customs Service adopted a drug-screening program requiring urinalysis for employees seeking transfer or promotion to positions involving drug interdiction, the carrying of firearms, or the handling of classified material. The employees' union challenged the suspicionless testing under the Fourth Amendment. ## Issue Whether suspicionless drug testing of Customs employees who seek such positions is a reasonable search under the Fourth Amendment. ## Rule Where a search serves a special governmental need beyond ordinary law enforcement, reasonableness is determined by balancing, and a warrant or individualized suspicion may be unnecessary:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-672",
      "page": null,
      "quote": "Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test.",
      "star_marker": "672",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 31893,
      "fragment": "#:~:text=Customs%20employees%20who%20are%20directly",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "National Treasury Employees Union v. Von Raab",
    "varies_by_point": false,
    "scope_note": "Special-needs suspicionless-testing precedent; good law.",
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4381539,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Landgraf v. USI Film Products",
          "cluster_id": 117841,
          "cite": [
            "128 L. Ed. 2d 229",
            "114 S. Ct. 1483",
            "511 U.S. 244",
            "1994 U.S. LEXIS 3292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmelin v. Michigan",
          "cluster_id": 112646,
          "cite": [
            "115 L. Ed. 2d 836",
            "111 S. Ct. 2680",
            "501 U.S. 957",
            "1991 U.S. LEXIS 3816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yates v. People",
          "cluster_id": 4675566,
          "cite": [
            "2019 CO 90"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Employment Div., Dept. of Human Resources of Ore. v. Smith",
          "cluster_id": 112404,
          "cite": [
            "108 L. Ed. 2d 876",
            "110 S. Ct. 1595",
            "494 U.S. 872",
            "1990 U.S. LEXIS 2021",
            "58 U.S.L.W. 4433",
            "53 Empl. Prac. Dec. (CCH) 39,826",
            "52 Fair Empl. Prac. Cas. (BNA) 855"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Allegheny v. American Civil Liberties Union",
          "cluster_id": 112331,
          "cite": [
            "106 L. Ed. 2d 472",
            "109 S. Ct. 3086",
            "492 U.S. 573",
            "1989 U.S. LEXIS 3468",
            "57 U.S.L.W. 5045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaiser Aluminum & Chemical Corp. v. Bonjorno",
          "cluster_id": 112403,
          "cite": [
            "108 L. Ed. 2d 842",
            "110 S. Ct. 1570",
            "494 U.S. 827",
            "1990 U.S. LEXIS 2024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samson v. California",
          "cluster_id": 145640,
          "cite": [
            "165 L. Ed. 2d 250",
            "126 S. Ct. 2193",
            "547 U.S. 843",
            "2006 U.S. LEXIS 4885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chandler v. Miller",
          "cluster_id": 118100,
          "cite": [
            "137 L. Ed. 2d 513",
            "117 S. Ct. 1295",
            "520 U.S. 305",
            "1997 U.S. LEXIS 2505"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
          "cluster_id": 121171,
          "cite": [
            "153 L. Ed. 2d 735",
            "122 S. Ct. 2559",
            "536 U.S. 822",
            "2002 U.S. LEXIS 4882",
            "2002 Cal. Daily Op. Serv. 5761",
            "2002 Daily Journal DAR 7275",
            "70 U.S.L.W. 4737",
            "15 Fla. L. Weekly Fed. S 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stein v. Davidson Hotel Co.",
          "cluster_id": 1060994,
          "cite": [
            "945 S.W.2d 714",
            "12 I.E.R. Cas. (BNA) 1636",
            "1997 Tenn. LEXIS 283",
            "1997 WL 257138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Reyes",
          "cluster_id": 1444172,
          "cite": [
            "968 P.2d 445",
            "80 Cal. Rptr. 2d 734",
            "19 Cal. 4th 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bull v. City and County of San Francisco",
          "cluster_id": 1313115,
          "cite": [
            "595 F.3d 964",
            "2010 WL 431790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bevill v. State",
          "cluster_id": 1149417,
          "cite": [
            "556 So. 2d 699",
            "1990 WL 7305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
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
        "journal_ref": "National Treasury Employees Union v. Von Raab:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDczNjA2NDAwMDAwJnM9Mjk5NjgwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTMmcz0yNjg3NTU4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
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
    "complete_query": "cites:(112220 OR 9431609 OR 9431610 OR 9431611)",
    "indexed_citing_opinions": 760,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112220,
        "count": 703,
        "count_source": "search"
      },
      {
        "opinion_id": 9431609,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9431610,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431611,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1190,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/national-treasury-employees-union-v-von-raab.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc1NTUxODkmcz01MzExNzM2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112220+OR+9431609+OR+9431610+OR+9431611%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112220,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 107814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 110917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 111990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 312772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 312834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 319945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 328554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 486563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 504461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112220,
        "cited_id": 1631759,
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
    "date_created": "2026-07-05T15:04:49Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:09:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:05:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — National Treasury Employees Union v. Von Raab

```
<opinion type="majority">
<author id="b731-10">Justice Kennedy</author>
<p id="AURm">delivered the opinion of the Court.</p>
<p id="b731-11">We granted certiorari to decide whether it violates the Fourth Amendment for the United States Customs Service to require a urinalysis test from employees who seek transfer or promotion to certain positions.</p>
<p id="AEk">I</p>
<p id="b731-3">A</p>
<p id="b731-4">The United States Customs Service, a bureau of the Department of the Treasury, is the federal agency responsible for processing persons, carriers, cargo, and mail into the United States, collecting revenue from imports, and enforcing customs and related laws. See United States Customs Service, Customs U. S. A., Fiscal Year 1985, p. 4. An important responsibility of the Service is the interdiction and <page-number citation-index="1" label="660">*660</page-number>seizure of contraband, including illegal drugs. <em>Ibid. </em>In 1987 alone, Customs agents seized drugs with a retail value of nearly $9 billion. See United States Customs Service, Customs U. S. A., Fiscal Year 1987, p. 40. In the routine discharge of their duties, many Customs employees have direct contact with those who traffic in drugs for profit. Drug import operations, often directed by sophisticated criminal syndicates, <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#561" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 561-562</a></span> (1980) (Powell, J., concurring), may be effected by violence or its threat. As a necessary response, many Customs operatives carry and use firearms in connection with their official duties. App. 109.</p>
<p id="b732-5">In December 1985, respondent, the Commissioner of Customs, established a Drug Screening Task Force to explore the possibility of implementing a drug-screening program within the Service. <em>Id., </em>at 11. After extensive research and consultation with experts in the field, the task force concluded that “drug screening through urinalysis is technologically reliable, valid and accurate.” <em>Ibid. </em>Citing this conclusion, the Commissioner announced his intention to require drug tests of employees who applied for, or occupied, certain positions within the Service. <em>Id., </em>at 10-11. The Commissioner stated his belief that “Customs is largely drug-free,” but noted also that “unfortunately no segment of society is immune from the threat of illegal drug use.” <em>Id., </em>at 10. Drug interdiction has become the agency’s primary enforcement mission, and the Commissioner stressed that “there is no room in the Customs Service for those who break the laws prohibiting the possession and use of illegal drugs.” <em>Ibid.</em></p>
<p id="b732-6">In May 1986, the Commissioner announced implementation of the drug-testing program. Drug tests were made a condition of placement or employment for positions that meet one or more of three criteria. The first is direct involvement in drug interdiction or enforcement of related laws, an activity the Commissioner deemed fraught with obvious dangers to the mission of the agency and the lives of Customs <page-number citation-index="1" label="661">*661</page-number>agents. <em>Id., </em>at 17, 113. The second criterion is a requirement that the incumbent carry firearms, as the Commissioner concluded that “[pjublic safety demands that employees who carry deadly arms and are prepared to make instant life or death decisions be drug free.” <em>Id., </em>at 113. The third criterion is a requirement for the incumbent to handle “classified” material, which the Commissioner determined might fall into the hands of smugglers if accessible to employees who, by reason of their own illegal drug use, are susceptible to bribery or blackmail. <em>Id., </em>at 114.</p>
<p id="b733-5">After an employee qualifies for a position covered by the Customs testing program, the Service advises him by letter that his final selection is contingent upon successful completion of drug screening. An independent contractor contacts the employee to fix the time and place for collecting the sample. On reporting for the test, the employee must produce photographic identification and remove any outer garments, such as a coat or a jacket, and personal belongings. The employee may produce the sample behind a partition, or in the privacy of a bathroom stall if he so chooses. To ensure against adulteration of the specimen, or substitution of a sample from another person, a monitor of the same sex as the employee remains close at hand to listen for the normal sounds of urination. Dye is added to the toilet water to prevent the employee from using the water to adulterate the sample.</p>
<p id="b733-6">Upon receiving the specimen, the monitor inspects it to ensure its proper temperature and color, places a tamper-proof custody seal over the container, and affixes an identification label indicating the date and the individual’s specimen number. The employee signs a chain-of-custody form, which is initialed by the monitor, and the urine sample is placed in a plastic bag, sealed, and submitted to a laboratory.<footnotemark>1</footnotemark></p>
<p id="b734-4"><page-number citation-index="1" label="662">*662</page-number>The laboratory tests the sample for the presence of marijuana, cocaine, opiates, amphetamines, and phencyclidine. Two tests are used. An initial screening test uses the enzyme-multiplied-immunoassay technique (EMIT). Any specimen that is identified as positive on this initial test must then be confirmed using gas chromatography/mass spectrometry (GC/MS). Confirmed positive results are reported to a “Medical Review Officer,” “[a] licensed physician. . . who has knowledge of substance abuse disorders and has appropriate medical training to interpret and evaluate an individual’s positive test result together with his or her medical history and any other relevant biomedical information.” HHS Reg. § 1.2, <page-number citation-index="1" label="663">*663</page-number><span class="citation no-link">53 Fed. Reg. 11980</span> (1988); HHS Reg. §2.4(g), 53 Fed. Reg., at 11983. 'After verifying the positive result, the Medical Review Officer transmits it to the agency.</p>
<p id="b735-5">Customs employees.who test positive for drugs and who can offer no satisfactory explanation are subject to dismissal from the Service. Test results may not, however, be turned over to any other agency, including criminal prosecutors, without the employee’s written consent.</p>
<p id="b735-6">B</p>
<p id="b735-7">Petitioners, a union of federal employees and a union official, commenced this suit in the United States District Court for the Eastern District of Louisiana on behalf of current Customs Service employees who seek covered positions. Petitioners alleged that the Custom Service drug-testing program violated, <em>inter alia, </em>the Fourth Amendment. The District Court agreed. <span class="citation" data-id="1631759"><a href="/opinion/1631759/national-treasury-employees-union-v-von-raab/" aria-description="Citation for case: National Treasury Employees Union v. Von Raab">649 F. Supp. 380</a></span> (1986). The court acknowledged “the legitimate governmental interest in a drug-free work place and work force,” but concluded that “the drug testing plan constitutes an overly intrusive policy of searches and seizures without probable cause or reasonable suspicion, in violation of legitimate expectations of privacy.” <span class="citation" data-id="1631759"><a href="/opinion/1631759/national-treasury-employees-union-v-von-raab/#387" aria-description="Citation for case: National Treasury Employees Union v. Von Raab"><em>Id., </em>at 387</a></span>. The court enjoined the drug-testing program, and ordered the Customs Service not to require drug tests of any applicants for covered positions.</p>
<p id="b735-8">A divided panel of the United States Court of Appeals for the Fifth Circuit vacated the injunction. <span class="citation multiple-matches"><a href="/c/F.%202d/816/170/">816 F. 2d 170</a></span> (1987). The court agreed with petitioners that the drug-screening program, by requiring an employee to produce a urine sample for chemical testing, effects a search within the meaning of the Fourth Amendment. The court held further that the searches required by the Commissioner’s directive are reasonable under the Fourth Amendment. It first noted that “[t]he Service has attempted to minimize the intrusiveness of the search” by not requiring visual observation of the act of urination and by affording notice to the employee that <page-number citation-index="1" label="664">*664</page-number>he will be tested. <em>Id., </em>at 177. The court also considered it significant that the program limits discretion in determining which employees are to be tested, <em>ibid., </em>and noted that the tests are an aspect of the employment relationship, <em>id., </em>at 178.</p>
<p id="b736-5">The court further found that the Government has a strong interest in detecting drug use among employees who meet the criteria of the Customs program. It reasoned that drug use by covered employees casts substantial doubt on their ability to discharge their duties honestly and vigorously, undermining public confidence in the integrity of the Service and concomitantly impairing the Service’s efforts to enforce the drug laws. <em>Ibid. </em>Illicit drug users, the court found, are susceptible to bribery and blackmail, may be tempted to divert for their own use portions of any drug shipments they interdict, and may, if required to carry firearms, “endanger the safety of their fellow agents, as well as their own, when their performance is impaired by drug use.” <em>Ibid. </em>“Considering the nature and responsibilities of the jobs for which applicants are being considered at Customs and the limited scope of the search,” the court stated, “the exaction of consent as a condition of assignment to the new job is not unreasonable.” <em>Id., </em>at 179.</p>
<p id="b736-6">The dissenting judge concluded that the Customs program is not an effective method for achieving the Service’s goals. He argued principally that an employee “given a five day notification of a test date need only abstain from drug use to prevent being identified as a user.” <em>Id., </em>at 184. He noted also that persons already employed in sensitive positions are not subject to the test. <em>Ibid. </em>Because he did not believe the Customs program can achieve its purposes, the dissenting judge found it unreasonable under the Fourth Amendment.</p>
<p id="b736-7">We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./485/903/">485 U. S. 903</a></span> (1988). We now affirm so much of the judgment of the Court of Appeals as upheld the testing of employees directly involved in drug interdiction or required to carry firearms. We vacate the <page-number citation-index="1" label="665">*665</page-number>judgment to the extent it upheld the testing of applicants for positions requiring the incumbent to handle classified materials, and remand for further proceedings. II</p>
<p id="b737-7">hH</p>
<p id="b737-3">In <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., ante, </em>at 616-618, decided today, we held that federal regulations requiring employees of private railroads to produce urine samples for chemical testing implicate the Fourth Amendment, as those tests invade reasonable expectations of privacy. Our earlier cases have settled that the Fourth Amendment protects individuals from unreasonable searches conducted by the Government, even when the Government acts as an employer, <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709, 717</a></span> (1987) (plurality opinion); see <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#731" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 731</a></span> (Scalia, J., concurring in judgment), and, in view of our holding in <em>Railway Labor Executives </em>that urine tests are searches, it follows that the Customs Service’s drug-testing program must meet the reasonableness requirement of the Fourth Amendment.</p>
<p id="b737-4">While we have often emphasized, and reiterate today, that a search must be supported, as a general matter, by a warrant issued upon probable cause, see, <em>e. g., Griffin </em>v. <em>Wisconsin, </em><span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987); <em>United States </em>v. <em>Karo, </em><span class="citation" data-id="9429751"><a href="/opinion/111257/united-states-v-karo/#717" aria-description="Citation for case: United States v. Karo">468 U. S. 705, 717</a></span> (1984), our decision in <em>Railway Labor Executives </em>reaffirms the longstanding principle that neither a <em>warrant nor probable cause, nor, indeed, any measure of </em>individualized suspicion, is an indispensable component of reasonableness in every circumstance. <em>Ante, </em>at 618-624. See also <em>New Jersey </em>v. <em>T. L. O., </em><span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#342" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 342, n. 8</a></span> (1985); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-661</a></span> (1976). As we note in <em>Railway Labor Executives, </em>our cases establish that where a Fourth Amendment intrusion serves special governmental needs, beyond the normal need for law enforcement, it is necessary to balance the individual’s privacy expectations against the Government’s interests to determine whether it is impractical to require a warrant or <page-number citation-index="1" label="666">*666</page-number>some level of individualized suspicion in the particular context. <em>Ante, </em>at 619-620.</p>
<p id="b738-5">It is clear that the Customs Service’s drug-testing program is not designed to serve the ordinary needs of law enforcement. Test results may not be used in a criminal prosecution of the employee without the employee’s consent. The purposes of the program are to deter drug use among those eligible for promotion to sensitive positions within the Service and to prevent the promotion of drug users to those positions. These substantial interests, no less than the Government’s concern for safe rail transportation at issue in <em>Railway Labor Executives, </em>present a special need that may justify departure from the ordinary warrant and probable-cause requirements.</p>
<p id="b738-6">A</p>
<p id="b738-7">Petitioners do not contend that a warrant is required by the balance of privacy and governmental interests in this context, nor could any such contention withstand scrutiny. We have recognized before that requiring the Government to procure a warrant for every work-related intrusion “would conflict with ‘the common-sense realization that government offices could not function if every employment decision became a constitutional matter.’” <em>O’Connor </em>v. <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#722" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>Ortega, supra, </em>at 722</a></span>, quoting <em>Connick </em>v. <em>Myers, </em><span class="citation" data-id="9429164"><a href="/opinion/110917/connick-ex-rel-parish-of-orleans-v-myers/#143" aria-description="Citation for case: Connick Ex Rel. Parish of Orleans v. Myers">461 U. S. 138, 143</a></span> (1983). See also <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 732</a></span> (Scalia, J., concurring in judgment); <em>New Jersey </em>v. <em>T. L. O., supra, </em>at 340 (noting that “[t]he warrant requirement ... is unsuited to the school environment: requiring a teacher to obtain a warrant before searching a child suspected of an infraction of school rules (or of the criminal law) would unduly interfere with the maintenance of the swift and informal disciplinary procedures needed in the schools”). Even if Customs Service employees are more likely to be familiar with the procedures required to obtain a warrant than most other Government workers, requiring a warrant in this context would serve only to divert valuable agency resources from the Service’s primary mis<page-number citation-index="1" label="667">*667</page-number>sion. The Customs Service has been entrusted with pressing responsibilities, and its mission would be compromised if it were required to seek search warrants in connection with routine, yet sensitive, employment decisions.</p>
<p id="b739-5">Furthermore, a warrant would provide little or nothing in the way of additional protection of personal privacy. A warrant serves primarily to advise the citizen that an intrusion is authorized by law and limited in its permissible scope and to interpose a neutral magistrate between the citizen and the law enforcement officer “engaged in the often competitive enterprise of ferreting out crime.” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). But in the present context, “the circumstances justifying toxicological testing and the permissible limits of such intrusions are defined narrowly and specifically . . . , and doubtless are well known to covered employees.” <em>Ante, </em>at 622. Under the Customs program, every employee who seeks a transfer to a covered position knows that he must take a drug test, and is likewise aware of the procedures the Service must follow in administering the test. A covered employee is simply not subject “to the discretion of the official in the field.” <em>Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 532</a></span> (1967). The process becomes automatic when the employee elects to apply for, and thereafter pursue, a covered position. Because the Service does not make a discretionary determination to search based on a judgment that certain conditions are present, there are simply “no special facts for a neutral magistrate to evaluate.” <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#383" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 383</a></span> (1976) (Powell, J., concurring).</p>
<p id="b739-6">B</p>
<p id="b739-7">Even where it is reasonable to dispense with the warrant requirement in the particular circumstances, a search ordinarily must be based on probable cause. <em>Ante, </em>at 624. Our cases teach, however, that the probable-cause standard “ ‘is peculiarly related to criminal investigations.’” <em>Colorado </em>v. <em>Bertine, </em><span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 371</a></span> (1987), quoting <em>South Dakota </em>v. <page-number citation-index="1" label="668">*668</page-number><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 370, n. 5</a></span>. In particular, the traditional probable-cause standard may be unhelpful in analyzing the reasonableness of routine administrative functions, <em>Colorado </em>v. <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine"><em>Bertine, supra, </em>at 371</a></span>; see also <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#723" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 723</a></span>, especially where the Government seeks to <em>prevent </em>the development of hazardous conditions or to detect violations that rarely generate articulable grounds for searching any particular place or person. Cf. <em>Camara </em>v. <em>Municipal Court of San Francisco, supra, </em>at 535-536 (noting that building code inspections, unlike searches conducted pursuant to a criminal investigation, are designed “to prevent even the unintentional development of conditions which are hazardous to public health and safety”); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 557</a></span> (noting that requiring particularized suspicion before routine stops on major highways near the Mexican border “would be impractical because the flow of traffic tends to be too heavy to allow the particularized study of a given car that would enable it to be identified as a possible carrier of illegal aliens”). Our precedents have settled that, in certain limited circumstances, the Government’s need to discover such latent or hidden conditions, or to prevent their development, is sufficiently compelling to justify the intrusion on privacy entailed by conducting such searches without any measure of individualized suspicion. <em>E. g., ante, </em>at 624. We think the Government’s need to conduct the suspicionless searches required by the Customs program outweighs the privacy interests of employees engaged directly in drug interdiction, and of those who otherwise are required to carry firearms.</p>
<p id="b740-5">The Customs Service is our Nation’s first line of defense against one of the greatest problems affecting the health and welfare of our population. We have adverted before to “the veritable national crisis in law enforcement caused by smuggling of illicit narcotics.” <em>United States </em>v. <em>Montoya de Hernandez, </em><span class="citation" data-id="9430181"><a href="/opinion/111509/united-states-v-montoya-de-hernandez/#538" aria-description="Citation for case: United States v. Montoya De Hernandez">473 U. S. 531, 538</a></span> (1985). See also <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#513" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 513</a></span> (Blackmun, J., dissenting). Our <page-number citation-index="1" label="669">*669</page-number>cases also reflect the traffickers’ seemingly inexhaustible repertoire of deceptive practices and elaborate schemes for importing narcotics, <em>e. g., United States </em>v. <em>Montoya de Hernandez, supra, </em>at 538-539; <em>United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#608" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 608-609</a></span> (1977). The record in this case confirms that, through the adroit selection of source locations, smuggling routes, and increasingly elaborate methods of concealment, drug traffickers have managed to bring into this country increasingly large quantities of illegal drugs. App. 111. The record also indicates, and it is well known, that drug smugglers do not hesitate to use violence to protect their lucrative trade and avoid apprehension. <em>Id., </em>at 109.</p>
<p id="b741-5">Many of the Service’s employees are often exposed to this criminal element and to the controlled substances it seeks to smuggle into the country. <em>Ibid. </em>Cf. <em>United States </em>v. <em>Montoya de Hernandez, supra, </em>at 543. The physical safety of these employees may be threatened, and many may be tempted not only by bribes from the traffickers with whom they deal, but also by their own access to vast sources of valuable contraband seized and controlled by the Service. The Commissioner indicated below that “Customs [officers have been shot, stabbed, run over, dragged by automobiles, and assaulted with blunt objects while performing their duties.” App. at 109-110. At least nine officers have died in the line of duty since 1974. He also noted that Customs officers have been the targets of bribery by drug smugglers on numerous occasions, and several have been removed from the Service for accepting bribes and for other integrity violations. <em>Id., </em>at 114. See also United States Customs Service, Customs U. S. A., Fiscal Year 1987, p. 31 (reporting internal investigations that resulted in the arrest of 24 employees and 54 civilians); United States Customs Service, Customs U. S. A., Fiscal Year 1986, p. 32 (reporting that 334 criminal and serious integrity investigations were conducted during the fiscal year, resulting in the arrest of 37 employees and 17 civilians); United States Customs Service, Customs <page-number citation-index="1" label="670">*670</page-number>U. S. A., Fiscal Year 1985, p. 32 (reporting that 284 criminal and serious integrity investigations were conducted during the 1985 fiscal year, resulting in the arrest of 15 employees and 51 civilians).</p>
<p id="b742-4">It is readily apparent that the Government has a compelling interest in ensuring that front-line interdiction personnel are physically fit, and have unimpeachable integrity and judgment. Indeed, the Government’s interest here is at least as important as its interest in searching travelers entering the country. We have long held that travelers seeking to enter the country may be stopped and required to submit to a routine search without probable cause, or even founded suspicion, “because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in.” <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925). See also <em>United States </em>v. <em>Montoya de Hernandez, supra, </em>at <em>538; United States </em>v. <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#617" aria-description="Citation for case: United States v. Ramsey"><em>Ramsey, supra, </em>at 617-619</a></span>. This national interest in self-protection could be irreparably damaged if those charged with safeguarding it were, because of their own drug use, unsympathetic to their mission of interdicting narcotics. A drug user’s indifference to the Service’s basic mission or, even worse, his active complicity with the malefactors, can facilitate importation of sizable drug shipments or block apprehension of dangerous criminals. The public interest demands effective measures to bar drug users from positions directly involving the interdiction of illegal drugs.</p>
<p id="b742-5">The public interest likewise demands effective measures to prevent the promotion of drug users to positions that require the incumbent to carry a firearm, even if the incumbent is not engaged directly in the interdiction of drugs. Customs employees who may use deadly force plainly “discharge duties fraught with such risks of injury to others that even a momentary lapse of attention can have disastrous consequences.” <em>Ante, </em>at 628. We agree with the Government <page-number citation-index="1" label="671">*671</page-number>that the public should not bear the risk that employees who may suffer from impaired perception and judgment will be promoted to positions where they may need to employ deadly force. Indeed, ensuring against the creation of this dangerous risk will itself further Fourth Amendment values, as the use of deadly force may violate the Fourth Amendment in certain circumstances. See <em>Tennessee </em>v. <em>Garner, </em><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 7-12</a></span> (1985).</p>
<p id="b743-5">Against these valid public interests we must weigh the interference with individual liberty that results from requiring these classes of employees to undergo a urine test. The interference with individual privacy that results from the collection of a urine sample for subsequent chemical analysis could be substantial in some circumstances. <em>Ante, </em>at 626. We have recognized, however, that the “operational realities of the workplace” may render entirely reasonable certain work-related intrusions by supervisors and co-workers that might be viewed as unreasonable in other contexts. See <em>O’Connor </em>v. <em>Ortega, </em><span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#717" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S., at 717</a></span>; <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#732" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 732</a></span> (Scalia, J., concurring in judgment). While these operational realities will rarely affect an employee’s expectations of privacy with respect to searches of his person, or of personal effects that the employee may bring to the workplace, <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/#716" aria-description="Citation for case: O&#x27;CONNOR v. Ortega"><em>id., </em>at 716, 725</a></span>, it is plain that certain forms of public employment may diminish privacy expectations even with respect to such personal searches. Employees of the United States Mint, for example, should expect to be subject to certain routine personal searches when they leave the workplace every day. Similarly, those who join our military or intelligence services may not only be required to give what in other contexts might be viewed as extraordinary assurances of trustworthiness and probity, but also may expect intrusive inquiries into their physical fitness for those special positions. Cf. <em>Snepp </em>v. <em>United States, </em><span class="citation" data-id="9427761"><a href="/opinion/110183/snepp-v-united-states/#509" aria-description="Citation for case: Snepp v. United States">444 U. S. 507, 509, n. 3</a></span> (1980); <em>Parker </em>v. <em>Levy, </em><span class="citation" data-id="9425778"><a href="/opinion/109077/parker-v-levy/#758" aria-description="Citation for case: Parker v. Levy">417 U. S. 733, 758</a></span> (1974); <em>Committee for GI Rights </em>v. <page-number citation-index="1" label="672">*672</page-number><em>Callaway, </em>171 U. S. App. D. C. 73, 84, <span class="citation" data-id="328554"><a href="/opinion/328554/the-committee-for-gi-rights-v-honorable-howard-h-callaway-secretary-of/#477" aria-description="Citation for case: The Committee for Gi Rights v. Honorable Howard H....">518 F. 2d 466, 477</a></span> (1975).</p>
<p id="b744-5">We think Customs employees who are directly involved in the interdiction of illegal drugs or who are required to carry firearms in the line of duty likewise have a diminished expectation of privacy in respect to the intrusions occasioned by a urine test. Unlike most private citizens or government employees in general, employees involved in drug interdiction reasonably should expect effective inquiry into their fitness and probity. Much the same is true of employees who are required to carry firearms. Because successful performance of their duties depends uniquely on their judgment and dexterity, these employees cannot reasonably expect to keep from the Service personal information that bears directly on their fitness. Cf. <em>In re Caruso </em>v. <em>Ward, </em>72 N. Y. 2d 433, 441, <span class="citation" data-id="5538531"><a href="/opinion/5689297/caruso-v-ward/#854" aria-description="Citation for case: Caruso v. Ward">530 N. E. 2d 850, 854-855</a></span> (1988). While reasonable tests designed to elicit this information doubtless infringe some privacy expectations, we do not believe these expectations outweigh the Government’s compelling interests in safety and in the integrity of our borders.<footnotemark>2</footnotemark></p>
<p id="b745-4"><page-number citation-index="1" label="673">*673</page-number>Without disparaging the importance of the governmental interests that support the suspicionless searches of these employees, petitioners nevertheless contend that the Service’s drug-testing program is unreasonable in two particulars. First, petitioners argue that the program is unjustified because it is not based on a belief that testing will reveal any drug use by covered employees. In pressing this argument, petitioners point out that the Service’s testing scheme was not implemented in response to any perceived drug problem among Customs employees, and that the program actually has not led to the discovery of a significant number of drug users. Brief for Petitioners 37, 44; Tr. of Oral Arg. 11-12, 20-21. Counsel for petitioners informed us at oral argument that no more than 5 employees out of 3,600 have tested positive for drugs. <em>Id., </em>at 11. Second, petitioners contend that the Service’s scheme is not a “sufficiently productive mechanism to justify [its] intrusion upon Fourth Amendment interests,” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#658" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 658-659</a></span> (1979), because illegal drug users can avoid detection with ease by temporary abstinence or by surreptitious adulteration of their urine specimens. Brief for Petitioners 46-47. These contentions are unpersuasive.</p>
<p id="b746-4"><page-number citation-index="1" label="674">*674</page-number>Petitioners’ first contention evinces an unduly narrow view of the context in which the Service’s testing program was implemented. Petitioners do not dispute, nor can there be doubt, that drug abuse is one of the most serious problems confronting our society today. There is little reason to believe that American workplaces are immune from this pervasive social problem, as is amply illustrated by our decision in <em>Railway Labor Executives. </em>See also <em>Masino </em>v. <em>United States, </em><span class="citation" data-id="1418046"><a href="/opinion/1418046/state-v-frank/#1050" aria-description="Citation for case: State v. Frank">589 P. 2d 1048, 1050</a></span> (Ct. Cl. 1978) (describing marijuana use by two Customs inspectors). Detecting drug impairment on the part of employees can be a difficult task, especially where, as here, it is not feasible to subject employees and their work product to the kind of day-to-day scrutiny that is the norm in more traditional office environments. Indeed, the almost unique mission of the Service gives the Government a compelling interest in ensuring that many of these covered employees do not use drugs even off duty, for such use creates risks of bribery and blackmail against which the Government is entitled to guard. In light of the extraordinary safety and national security hazards that would attend the promotion of drug users to positions that require the carrying of firearms or the interdiction of controlled substances, the Service’s policy of deterring drug users from seeking such promotions cannot be deemed unreasonable.</p>
<p id="b746-5">The mere circumstance that all but a few of the employees tested are entirely innocent of wrongdoing does not impugn the program’s validity. The same is likely to be true of householders who are required to submit to suspicionless housing code inspections, see <em>Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and of motorists who are stopped at the checkpoints we approved in <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976). The Service’s program is designed to prevent the promotion of drug users to sensitive positions as much as it is designed to detect those employees who use drugs. Where, as here, the possible harm against which the Government seeks to guard is <page-number citation-index="1" label="675">*675</page-number>substantial, the need to prevent its occurrence furnishes an ample justification for reasonable searches calculated to advance the Government’s goal.<footnotemark>3</footnotemark></p>
<p id="b748-4"><page-number citation-index="1" label="676">*676</page-number>We think petitioners’ second argument — that the Service’s testing program is ineffective because employees may attempt to deceive the test by a brief abstention before the test date, or by adulterating their urine specimens — overstates the case. As the Court of Appeals noted, addicts may be unable to abstain even for a limited period of time, or may be unaware of the “fade-away effect” of certain drugs. 816 F. 2d, at 180. More importantly, the avoidance techniques suggested by petitioners are fraught with uncertainty and risks for those employees who venture to attempt them. A particular employee’s pattern of elimination for a given drug cannot be predicted with perfect accuracy, and, in any event, this information is not likely to be known or available to the employee. Petitioners’ own expert indicated below that the time it takes for particular drugs to become undetectable in urine can vary widely depending on the individual, and may extend for as long as 22 days. App. 66. See also <em>ante, </em>at 631 (noting Court of Appeals’ reliance on certain academic literature that indicates that the testing of urine can discover drug use “ ‘for. . . weeks after the ingestion of the drug’ ”). Thus, contrary to petitioners’ suggestion, no employee reasonably can expect to deceive the test by the simple expedient of abstaining after the test date is assigned. Nor can he expect attempts at adulteration to succeed, in view of the precautions taken by the sample collector to ensure the integrity of the sample. In all the circumstances, we are persuaded that the program bears a close and substantial relation to the Service’s goal of deterring drug users from seeking promotion to sensitive positions.<footnotemark>4</footnotemark></p>
<p id="b749-4"><page-number citation-index="1" label="677">*677</page-number>In sum, we believe the Government has demonstrated that its compelling interests in safeguarding our borders and the public safety outweigh the privacy expectations of employees who seek to be promoted to positions that directly involve the interdiction of illegal drugs or that require the incumbent to carry a firearm. We hold that the testing of these employees is reasonable under the Fourth Amendment.</p>
<p id="b749-5">C</p>
<p id="b749-6">We are unable, on the present record, to assess the reasonableness of the Government’s testing program insofar as it covers employees who are required “to handle classified material.” App. 17. We readily agree that the Government has a compelling interest in protecting truly sensitive information from those who, “under compulsion of circumstances or for other reasons, . . . might compromise [such] information.” <em>Department of Navy </em>v. <em>Egan, </em><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/#528" aria-description="Citation for case: Department of the Navy v. Egan">484 U. S. 518, 528</a></span> (1988). See also <em>United States </em>v. <em>Robel, </em><span class="citation" data-id="9423541"><a href="/opinion/107554/united-states-v-robel/#267" aria-description="Citation for case: United States v. Robel">389 U. S. 258, 267</a></span> (1967) (“We have recognized that, while the Constitution protects against invasions of individual rights, it does not withdraw from the Government the power to safeguard its vital interests. . . . The Government can deny access to its secrets to those who would use such information to harm the Nation”). We also agree that employees who seek promotions to positions where they would handle sensitive information can be required to submit to a urine test under the Service’s screening program, especially if the positions covered under this category require background investigations, medical examinations, or other intrusions that may be expected to diminish their expectations of privacy in respect of a urinalysis test. Cf. <em>Department of Navy </em>v. <span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/#528" aria-description="Citation for case: Department of the Navy v. Egan"><em>Egan, supra, </em>at 528</a></span> (noting that the Executive Branch generally subjects those desir<page-number citation-index="1" label="678">*678</page-number>ing a security clearance to “a background investigation that varies according to the degree of adverse effect the applicant could have on the national security”).</p>
<p id="b750-5">It is not clear, however, whether the category defined by the Service’s testing directive encompasses only those Customs employees likely to gain access to sensitive information. Employees who are tested under the Service’s scheme include those holding such diverse positions as “Accountant,” “Accounting Technician,” “Animal Caretaker,” “Attorney (All),” “Baggage Clerk,” “Co-op Student (All),” “Electric Equipment Repairer,” “Mail Clerk/Assistant,” and “Messenger.” App. 42-43. We assume these positions were selected for coverage under the Service’s testing program by reason of the incumbent’s access to “classified” information, as it is not clear that they would fall under either of the two categories we have already considered. Yet it is not evident that those occupying these positions are likely to gain access to sensitive information, and this apparent discrepancy raises in our minds the question whether the Service has defined this category of employees more broadly than is necessary to meet the purposes of the Commissioner’s directive.</p>
<p id="b750-6">We cannot resolve this ambiguity on the basis of the record before us, and we think it is appropriate to remand the case to the Court of Appeals for such proceedings as may be necessary to clarify the scope of this category of employees subject to testing. Upon remand the Court of Appeals should examine the criteria used by the Service in determining what materials are classified and in deciding whom to test under this rubric. In assessing the reasonableness of requiring tests of these employees, the court should also consider pertinent information bearing upon the employees’ privacy expectations, as well as the supervision to which these employees are already subject.</p>
<p id="b750-7">Ill</p>
<p id="b750-8">Where the Government requires its employees to produce urine samples to be analyzed for evidence of illegal drug <page-number citation-index="1" label="679">*679</page-number>use, the collection and subsequent chemical analysis of such samples are searches that must meet the reasonableness requirement of the Fourth Amendment. Because the testing program adopted by the Customs Service is not designed to serve the ordinary' needs of law enforcement, we have balanced the public interest in the Service’s testing program against the privacy concerns implicated by the tests, without reference to our usual presumption in favor of the procedures specified in the Warrant Clause, to assess whether the tests required by Customs are reasonable.</p>
<p id="b751-5">We hold that the suspicionless testing of employees who apply for promotion to positions directly involving the interdiction of illegal drugs, or to positions that require the incumbent to carry a firearm, is reasonable. The Government’s compelling interests in preventing the promotion of drug users to positions where they might endanger the integrity of our Nation’s borders or the life of the citizenry outweigh the privacy interests of those who seek promotion to these positions, who enjoy a diminished expectation of privacy by virtue of the special, and obvious, physical and ethical demands of those positions. We do not decide whether testing those who apply for promotion to positions where they would handle “classified” information is reasonable because we find the record inadequate for this purpose.</p>
<p id="b751-6">The judgment of the Court of Appeals for the Fifth Circuit is affirmed in part and vacated in part, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b751-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b733-7"> After this case was decided by .the Court of Appeals, <span class="citation multiple-matches"><a href="/c/F.%202d/816/170/">816 F. 2d 170</a></span> (CA5 1987), the United States Department of Health and Human Services, in accordance with recently enacted legislation, <span class="citation no-link">Pub. L. 100-71, § 503</span>, <span class="citation no-link">101 <page-number citation-index="1" label="662">*662</page-number>Stat. 468</span>-471, promulgated regulations (hereinafter HHS Regulations or HHS Reg.) governing certain federal employee drug-testing programs. <span class="citation no-link">53 Fed. Reg. 11979</span> (1988). To the extent the HHS Regulations add to, or depart from, the procedures adopted as part of a federal drug-screening program covered by <span class="citation no-link">Pub. L. 100-71, </span>the HHS Regulations control. <span class="citation no-link">Pub. L. 100-71, § 503</span>(b)(2)(B), <span class="citation no-link">101 Stat. 470</span>. Both parties agree that the Customs Service’s drug-testing program must conform to the HHS Regulations. See Brief for Petitioners 6, n. 8; Brief for Respondent 4-5, and n. 4. We therefore consider the HHS Regulations to the extent they supplement or displace the Commissioner’s original directive. See <em>California Bankers Assn. </em>v. <em>Shultz, </em><span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#53" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 53</a></span> (1974); <em>Thorpe </em>v. <em>Housing Authority of Durham, </em><span class="citation" data-id="9423867"><a href="/opinion/107814/thorpe-v-housing-authority-of-durham/#281" aria-description="Citation for case: Thorpe v. Housing Authority of Durham">393 U. S. 268, 281-282</a></span> (1969).</p>
<p id="b734-6">One respect in which the original Customs directive differs from the now-prevailing regime concerns the extent to which the employee may be required to disclose personal medical information. Under the Service’s original plan, each tested employee was asked to disclose, at the time the urine sample was collected, any medications taken within the last 30 days, and to explain any circumstances under which he may have been in legitimate contact with illegal substances within the last 30 days. Failure to provide this information at this time could result in the agency not considering the effect of medications or other licit contacts with drugs on a positive test result. Under the HHS Regulations, an employee need not provide information concerning medications when he produces the sample for testing. He may instead present such information only, after he is notified that his specimen tested positive for illicit drugs, at which time the Medical Review Officer reviews all records made available by the employee to determine whether the positive indication could have been caused by lawful use of drugs. See HHS Reg. § 2.7, <span class="citation no-link">53 Fed. Reg. 11985</span>-11986 (1988).</p>
</footnote>
<footnote label="2">
<p id="b744-6"> The procedures prescribed by the Customs Service for the collection and analysis of the requisite samples do not carry the grave potential for “arbitrary and oppressive interference with the privacy and personal security of individuals,” <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span>, (1976), that the Fourth Amendment was designed to prevent. Indeed, these procedures significantly minimize the program’s intrusion on privacy interests. Only employees who have been tentatively accepted for promotion or transfer to one of the three categories of covered positions are tested, and applicants know at the outset that a drug test is a requirement of those positions. Employees are also notified in advance of the scheduled sample collection, thus reducing to a minimum any “unsettling show of authority,” <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#657" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 657</a></span> (1979), that may be associated with unexpected intrusions on privacy. Cf. <em>United States </em>v. <em>Martinez-FueHe, supra, </em>at 559 (noting that the intrusion on privacy occasioned by routine highway checkpoints is minimized by the fact that motorists “are not taken by surprise as they know, or may obtain knowledge of, the location of the checkpoints and will not be stopped elsewhere”); <em>Wyman </em>v. <em>James, </em><span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#320" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 320-321</a></span> (1971) (providing a welfare re-<page-number citation-index="1" label="673">*673</page-number>eipient with advance notice that she would be visited by a welfare caseworker minimized the intrusion on privacy occasioned by the visit). There is no direct observation of the act of urination, as the employee may provide a specimen in the privacy of a stall.</p>
<p id="b745-6">Further, urine samples may be examined only for the specified drugs. The use of samples to test for any other substances is prohibited. See HHS Reg. § 2.1(c), <span class="citation no-link">53 Fed. Reg. 11980</span> (1988). And, as the Court of Appeals noted, the combination of EMIT and GC/MS tests required by the Service is highly accurate, assuming proper storage, handling, and measurement techniques. 816 F. 2d, at 181. Finally, an employee need not disclose personal medical information to the Government unless his test result is positive, and even then any such information is reported to a licensed physician. Taken together, these procedures significantly minimize the intrusiveness of the Service’s drug-screening program.</p>
</footnote>
<footnote label="3">
<p id="b747-5"> The point is well illustrated also by the Federal Government’s practice of requiring the search of all passengers seeking to board commercial airliners, as well as the search of their carry-on luggage, without any basis for suspecting any particular passenger of an untoward motive. Applying our precedents dealing with administrative searches, see, <em>e. g., Camara </em>v. <em>Municipal Court of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), the lower courts that have considered the question have consistently concluded that such searches are reasonable under the Fourth Amendment. As Judge Friendly explained in a leading case upholding such searches:</p>
<p id="b747-6">“When the risk is the jeopardy to hundreds of human lives and millions of dollars of property inherent in the pirating or blowing up of a large airplane, that danger <em>alone </em>meets the test of reasonableness, so long as the search is conducted in good faith for the purpose of preventing hijacking or like damage and with reasonable scope and the passenger has been given advance notice of his liability to such a search so that he can avoid it by choosing not to travel by air.” <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="9460705"><a href="/opinion/319945/united-states-v-cynthia-edwards/#500" aria-description="Citation for case: United States v. Cynthia Edwards">498 F. 2d 496, 500</a></span> (CA2 1974) (emphasis in original).</p>
<p id="b747-7">See also <em>United States </em>v. <em>Skipwith, </em><span class="citation" data-id="9459727"><a href="/opinion/312834/united-states-v-lee-skipwith-iii/#1275" aria-description="Citation for case: United States v. Lee Skipwith, III">482 F. 2d 1272, 1275-1276</a></span> (CA5 1973); <em>United States </em>v. <em>Davis, </em><span class="citation" data-id="312772"><a href="/opinion/312772/united-states-v-charles-davis-aka-marcus-anderson/#907" aria-description="Citation for case: United States v. Charles Davis AKA Marcus Anderson">482 F. 2d 893, 907-912</a></span> (CA9 1973). It is true, as counsel for petitioners pointed out at oral argument, that these air piracy precautions were adopted in response to an observable national and international hijacking crisis. Tr. of Oral Arg. 13. Yet we would not suppose that, if the validity of these searches be conceded, the Government would be precluded from conducting them absent a demonstration of danger as to any particular airport or airline. It is sufficient that the Government have a compelling interest in preventing an otherwise pervasive societal problem from spreading to the particular context.</p>
<p id="b747-9">Nor would we think, in view of the obvious deterrent purpose of these searches, that the validity of the Government’s airport screening program necessarily turns on whether significant numbers of putative air pirates are actually discovered by the searches conducted under the program. In the 15 years the program has been in effect, more than 9.5 <em>billion </em>persons have been screened, and over 10 <em>billion </em>pieces of luggage have been inspected. See Federal Aviation Administration, Semiannual Report to Congress on the Effectiveness of The Civil Aviation Program (Nov. 1988) (Exhibit 6). By far the overwhelming majority of those persons who have been searched, like Customs employees who have been tested under the Service’s drug-screening scheme, have proved entirely innocent — only <page-number citation-index="1" label="676">*676</page-number>42,000 firearms have been detected during the same period. <em><span class="citation" data-id="312772"><a href="/opinion/312772/united-states-v-charles-davis-aka-marcus-anderson/" aria-description="Citation for case: United States v. Charles Davis AKA Marcus Anderson">Ibid.</a></span> </em>When the Government’s interest lies in deterring highly hazardous conduct, a low incidence of such conduct, far from impugning the validity of the scheme for implementing this interest, is more logically viewed as a hallmark of success. See <em>Bell </em>v. <em>Wolfish, </em><span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 559</a></span> (1979).</p>
</footnote>
<footnote label="4">
<p id="b748-6"> Indeed, petitioners’ objection is based on those features of the Service's program — the provision of advance notice and the failure of the sample collector to observe directly the act of urination — that contribute sig-<page-number citation-index="1" label="677">*677</page-number>nifieantly to diminish the program’s intrusion on privacy. See <em>supra, </em>at 672-673, n. 2. Thus, under petitioners’ view, “the testing program would be more likely to be constitutional if it were more pervasive and more invasive of privacy.” 816 F. 2d, at 180.</p>
</footnote>
</opinion>
```

---
