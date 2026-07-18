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

## GROUP: content/cases/Gonzalez v. Trevino.md  (`case`, 5 assertions)

### content_page

```
---
title: Gonzalez v. Trevino
type: case
citation: "602 U.S. 653 (2024)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2024
date_decided: ""
docket: 22-1025
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
  opinion_url: "https://www.courtlistener.com/opinion/10600071/gonzalez-v-trevino/"
  cluster_id: 10600071
  opinion_id: null
  identity_checked: true
lake:
  record_id: Gonzalez v. Trevino
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Retaliatory Arrest]]"
    role: Key
related:
  - "[[Nieves v. Bartlett]]"
  - "[[Retaliatory Arrest]]"
tags:
  - case
  - first-amendment
  - retaliatory-arrest
  - probable-cause
  - section-1983
holding: "The Nieves exception to the no-probable-cause bar on First Amendment retaliatory-arrest claims is not limited to specific comparator evidence of otherwise-similarly-situated individuals who were not arrested; a plaintiff may satisfy it with any objective evidence, and the Fifth Circuit's contrary demand took an overly cramped view of Nieves."
---

# Gonzalez v. Trevino

*602 U.S. 653 (2024)* (No. 22-1025) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10600071 → opinion 11066659 (per curiam); quotes string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Sylvia Gonzalez, a newly elected city councilmember in Castle Hills, Texas, helped organize a citizen petition to remove the city manager. She was later arrested and charged with tampering with a government record — the petition was found in her binder — in what she alleged was retaliation for her protected political speech. Gonzalez conceded that probable cause supported her arrest but invoked the narrow exception to the no-probable-cause rule recognized in *[[Nieves v. Bartlett]]*. The District Court allowed her claim to proceed, but the Fifth Circuit reversed, holding that a plaintiff can fall within the *[[Nieves v. Bartlett|Nieves]]* exception only by producing "comparative evidence" of otherwise similarly situated individuals who engaged in the same conduct but were not arrested.

## Issue
Whether the *[[Nieves v. Bartlett|Nieves]]* exception permitting a retaliatory-arrest claim to proceed despite probable cause is limited to a specific, narrow form of comparator evidence, or may instead be satisfied by other objective evidence.

## Rule
*[[Nieves v. Bartlett|Nieves]]* held that a retaliatory-arrest plaintiff generally "must plead and prove the absence of probable cause for the arrest," 587 U.S., at 402, but recognized an exception for "circumstances where officers have probable cause to make arrests, but typically exercise their discretion not to do so," 587 U.S., at 406. The only express limit *[[Nieves v. Bartlett|Nieves]]* placed on the evidence a plaintiff may use to show such circumstances is that it be objective. The Fifth Circuit's demand for virtually identical, identifiable comparators therefore read the exception too narrowly: "We agree with Gonzalez that the Fifth Circuit took an overly cramped view of *Nieves*." — 602 U.S. at 658. ^pin-658

## Application
Although the *[[Nieves v. Bartlett|Nieves]]* exception is "slim," the court below went too far in demanding examples of specific, identifiable people who "mishandled a government petition" the way Gonzalez did but were not arrested. Requiring that precise a comparator is not what *[[Nieves v. Bartlett|Nieves]]* commands; objective evidence that Gonzalez's arrest departed from the ordinary exercise of discretion suffices to reach the exception. The Court resolved the case on that first question alone and did not reach Gonzalez's second argument — that the no-probable-cause rule should be confined to split-second arrests rather than deliberative ones.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for the lower courts to assess whether Gonzalez's evidence suffices to satisfy the *[[Nieves v. Bartlett|Nieves]]* exception. The opinion was **[[Common Legal Terms#per-curiam|per curiam]]**; Justices Alito, Kavanaugh, and Jackson (joined by Sotomayor) filed [[Common Legal Terms#concurring-opinion|concurrences]], and Justice Thomas dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Gonzalez* clarifies rather than displaces *[[Nieves v. Bartlett|Nieves]]*: the decision [[Reading and Citing Cases#vacated|vacated]] the Fifth Circuit's judgment and left the sufficiency of Gonzalez's evidence — and the scope of the no-probable-cause rule for deliberative arrests — open [[Reading and Citing Cases#on-remand|on remand]].

## Appears on
- [[Retaliatory Arrest]] — *Key*

## Sources
- [*Gonzalez v. Trevino*, 602 U.S. 653 (2024)](https://www.courtlistener.com/opinion/10600071/gonzalez-v-trevino/) — pinpoint: 658 (per curiam holding); quote string-matched to the CL opinion text 2026-07-07.
- [*Nieves v. Bartlett*, 587 U.S. 391 (2019)](https://www.courtlistener.com/opinion/9231236/nieves-v-bartlett/) — the general rule (at 402) and the exception (at 406) that *Gonzalez* construes.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "779444170dbe0313", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "602 U.S. 653 (2024)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Gonzalez v. Trevino", "year": "2024"}}
{"assertion_id": "6fa5a4ccacb60b1b", "dimension": "support", "kind": "home_role", "locator": {"home": "Retaliatory Arrest"}, "payload": {"home": "Retaliatory Arrest", "role": "Key", "title": "Gonzalez v. Trevino"}}
{"assertion_id": "b937706edba0950a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Nieves exception to the no-probable-cause bar on First Amendment retaliatory-arrest claims is not limited to specific comparator evidence of otherwise-similarly-situated individuals who were not arrested; a plaintiff may satisfy it with any objective evidence, and the Fifth Circuit's contrary demand took an overly cramped view of Nieves.", "title": "Gonzalez v. Trevino"}}
{"assertion_id": "5f58a1fbe16a3599", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Gonzalez v. Trevino", "varies_by_point": "false"}}
{"assertion_id": "dac6cebdea6569b2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gonzalez v. Trevino"}}
```

### lake record — Gonzalez v. Trevino

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gonzalez v. Trevino",
  "status": "under_review",
  "identity": {
    "case_name": "Gonzalez v. Trevino",
    "case_name_short": "Gonzalez",
    "case_name_full": "",
    "input_case_name": "Gonzalez v. Trevino",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "22-1025",
    "cluster_id": 10600071,
    "lead_opinion_id": 11066659,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600071/gonzalez-v-trevino/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "602 U.S. 653",
      "volume": "602",
      "reporter": "U.S.",
      "page": "653",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "602 U.S. 653",
        "volume": "602",
        "reporter": "U.S.",
        "page": "653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "602 U.S. 653",
    "official_selection": {
      "court_class": "scotus",
      "selected": "602 U.S. 653",
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
    "date_created": "2026-07-06T12:12:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:12:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:12:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:12:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "gonzalez-v-trevino--10600071",
      "to_record_id": "Gonzalez v. Trevino",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Gonzalez v. Trevino

```
                   PRELIMINARY PRINT

             Volume 602 U. S. Part 1
                             Pages 653–679




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                               June 20, 2024


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                         OCTOBER TERM, 2023                               653

                                  Syllabus


                GONZALEZ v. TREVINO et al.

certiorari to the united states court of appeals for
                  the fth circuit
      No. 22–1025. Argued March 20, 2024—Decided June 20, 2024
In Nieves v. Bartlett, the Court held that a plaintiff bringing a retaliatory-
  arrest claim “must plead and prove the absence of probable cause for
  the arrest.” 587 U. S. 391, 402. Nieves recognized an exception to that
  rule, namely, that the existence of probable cause does not defeat a plain-
  tiff's claim if he produces “objective evidence that he was arrested when
  otherwise similarly situated individuals not engaged in the same sort
  of protected speech had not been.” Id., at 407. The Court granted
  certiorari to consider whether the Fifth Circuit properly applied these
  principles to petitioner Sylvia Gonzalez's retaliatory-arrest claim.
     Gonzalez claims that her arrest for violating a Texas anti-tampering
  statute was in retaliation for gathering signatures on a petition seeking
  the removal of the city manager of Castle Hills, Texas. To bolster her
  claim, Gonzalez alleges that the past decade's misdemeanor and felony
Page Proof Pending Publication
  data for Bexar County (where Castle Hills is located) shows that the
  Texas anti-tampering statute has never been used in the county to crim-
  inally charge someone for the sort of conduct Gonzalez had engaged in.
  The District Court denied the defendants' motion to dismiss, but the
  Fifth Circuit reversed, concluding that because Gonzalez could not pro-
  vide “comparative evidence” of “otherwise similarly situated individuals
  who engaged in the same criminal conduct but were not arrested,” Gon-
  zalez could not qualify for the Nieves exception, 42 F. 4th 487, 493.
Held: In requiring petitioner Gonzalez to provide specifc comparator evi-
 dence to support her retaliatory-arrest claim, the Fifth Circuit took
 an overly cramped view of Nieves. The Court recognized the Nieves
 exception to account for “circumstances where offcers have probable
 cause to make arrests, but typically exercise their discretion not to do
 so.” 587 U. S., at 406. The only express limit the Court placed on the
 sort of evidence a plaintiff may present to show their arrest occurred
 under such circumstances is that it must be objective. Id., at 407.
 Gonzalez provided a permissible type of evidence because the fact that
 no one has ever been arrested for engaging in a certain kind of conduct
 makes it more likely that an offcer has declined to arrest someone for
 engaging in such conduct in the past. Gonzalez's survey is objective
 evidence tending to show that she “was arrested when otherwise simi-
654                    GONZALEZ v. TREVINO

                                Syllabus

  larly situated individuals not engaged in the same sort of protected
  speech had not been.” Ibid.
42 F. 4th 487, vacated and remanded.

  Anya Bidwell argued the cause for petitioner. With her
on the briefs were Patr ick Jaicomo, Will Aronin, and
Marie Miller.
  Nicole Frazer Reaves argued the cause for the United
States as amicus curiae supporting neither party. With her
on the brief were Solicitor General Prelogar, Assistant At-
torney General Clarke, Deputy Solicitor General Feigin,
Tovah R. Calderón, and Jessica Merry Samuels.
  Lisa S. Blatt argued the cause for respondents. With her
on the brief were Sarah M. Harris, Aaron Z. Roper, Scott
M. Tschirhart, and Lowell F. Denton.*

   *Briefs of amici curiae urging reversal were fled for the American
Civil Liberties Union et al. by Vera Eidelman, Esha Bhandari, David D.
Cole, Cecillia D. Wang, Barbara E. Bergman, J. T. Morris, Darpana
Page Proof Pending Publication
Sheth, Clark M. Neily III, and Anastasia P. Boden; for the Constitutional
Accountability Center et al. by Elizabeth B. Wydra, Brianne J. Gorod,
Brian R. Frazelle, Mary B. McCord, Kelsi Brown Corkran, and Shelby
Calambokidis; for the Institute for Free Speech by Easha Anand, Pamela
S. Karlan, Jeffrey L. Fisher, and Alan Gura; for the Law Enforcement
Action Partnership by David Debold; for the National Police Accountabil-
ity Project by Charles A. Rothfeld, Eugene R. Fidell, Paul W. Hughes,
and Michael B. Kimberly; for the Reporters Committee for Freedom of
the Press by Bruce D. Brown; for the Roderick & Solange MacArthur
Justice Center by Devi M. Rao; for the Thomas More Society by Thomas
Brejcha, B. Tyler Brooks, and Joan M. Mannix; and for Fane Lozman by
Anton Metlitsky and Kerri L. Barsh.
   Briefs of amici curiae urging affrmance were fled for the State of
Alaska et al. by Treg Taylor, Attorney General of Alaska, and Kimberly
D. Rodgers, Assistant Attorney General, and by the Attorneys General for
their respective States as follows: Ashley Moody of Florida, Lynn Fitch
of Mississippi, Austin Knudsen of Montana, Michael T. Hilgers of Ne-
braska, Drew H. Wrigley of North Dakota, Dave Yost of Ohio, Alan Wil-
son of South Carolina, Marty Jackley of South Dakota, and Sean D. Reyes
of Utah; for the State of Texas by Ken Paxton, Attorney General of Texas,
Aaron L. Nielson, Solicitor General, Brent Webster, First Assistant Attor-
ney General, Lanora C. Pettit, Principal Deputy Solicitor General, and
                     Cite as: 602 U. S. 653 (2024)                 655

                             Per Curiam

  Per Curiam.
   In Nieves v. Bartlett, 587 U. S. 391, 402 (2019), this Court
held that, as a general rule, a plaintiff bringing a retaliatory-
arrest claim “must plead and prove the absence of probable
cause for the arrest.” At the same time, we recognized a
narrow exception to that rule. The existence of probable
cause does not defeat a plaintiff's claim if he produces “objec-
tive evidence that he was arrested when otherwise similarly
situated individuals not engaged in the same sort of pro-
tected speech had not been.” Id., at 407. We granted cer-
tiorari in this case to consider whether the Fifth Circuit
properly applied these principles. It did not. We therefore
vacate that court's judgment and remand for proceedings
consistent with this opinion.

                                  I
  In 2019, Sylvia Gonzalez ran for a seat on the city council
Page       Proof
of Castle Hills, a smallPending
                        town in southernPublication
                                          Texas. While she
was on the campaign trail, Gonzalez heard multiple com-
plaints about the city manager, Ryan Rapelye. As city man-
ager, Rapelye was responsible for, among other things, en-
forcing the city's laws and managing its budget.
   Gonzalez was elected in May 2019. Her frst act in offce
was to help gather signatures for a petition seeking Ra-
pelye's removal. Eventually, over 300 residents signed the
petition. The petition was introduced at the next city coun-
cil meeting, where discussions grew heated after various res-
idents rose to Rapelye's defense and spoke against Gonzalez.
The discussion over the petition continued the next day.

Kathryn M. Cherry, Assistant Solicitor General; for the Local Govern-
ment Legal Center et al. by C. Harker Rhodes IV; for the National Sher-
iffs' Association by Gregory C. Champagne and Maurice E. Bostick; and
for the Texas Association of Counties et al. by Cameron T. Norris and
Mike Thompson, Jr.
   Michel Paradis fled a brief for Law Professors as amici curiae.
656                     GONZALEZ v. TREVINO

                                 Per Curiam

   At the end of the second day, Gonzalez was packing up her
belongings when the mayor, Edward Trevino, II, asked her
for the petition. Gonzalez indicated that the petition was in
Trevino's possession, which he denied. He then asked Gon-
zalez to check her binder, where she found the petition.
Gonzalez claims that she “did not intentionally put the peti-
tion in her binder,” and that she was “surprise[d]” to fnd it
there. Complaint and Jury Demand in No. 5:20–cv–01151
(WD Tex., Sept. 29, 2020), ECF Doc. 1, p. 11.
   Trevino brought this incident to the city police's attention,
and an investigation into these events soon began. Within
a month, a private attorney tasked with leading the investi-
gation concluded that Gonzalez had likely violated a Texas
anti-tampering statute that, among other things, prohibits a
person from intentionally “remov[ing] . . . a governmental
record.” Tex. Penal Code Ann. §§ 37.10(a)(3), (c)(1) (West
Cum. Supp. 2023).1
   On the private attorney's request, a local Magistrate
Page Proof Pending Publication
granted a warrant for Gonzalez's arrest. When she heard
the news, Gonzalez turned herself in and spent an evening in
jail. The district attorney ultimately dismissed the charges.
Gonzalez claims that this episode has convinced her to step
away from political life.
   Gonzalez brought suit under 42 U. S. C. § 1983 in Federal
District Court against Trevino, along with the police chief
and the private attorney in their individual capacities.2 Her
complaint alleged that she was arrested in retaliation for
her role in organizing the petition for Rapelye's removal and
that the defendants therefore violated her First Amend-
ment rights.

   1
     The statute also prohibits a person from intentionally “destroy[ing],”
“conceal[ing],” or “otherwise impair[ing] the verity, legibility, or availabil-
ity” of a governmental record.
   2
     She also pressed a claim in this action against Castle Hills. That claim
is not before us.
                   Cite as: 602 U. S. 653 (2024)           657

                           Per Curiam

   To bolster her claim, Gonzalez alleged that she had re-
viewed the past decade's misdemeanor and felony data for
Bexar County (where Castle Hills is located) and that her
review had found that the Texas anti-tampering statute had
never been used in the county “to criminally charge someone
for trying to steal a nonbinding or expressive document.”
ECF Doc. 1, at 17. Gonzalez's search turned up 215 felony
indictments, and she characterized the typical indictment as
involving “accusations of either using or making fake govern-
ment identifcation documents.” Ibid. Other felony indict-
ments included ones for fake checks, hiding murder evidence,
or cheating on government exams. Every misdemeanor
case, according to Gonzalez, involved “fake social security
numbers, driver's licenses, [or] green cards.” Ibid. Gonza-
lez pointed to this research as evidence that the defendants
had engaged in a political vendetta by bringing a “sham
charge” against her. Id., at 27.
Page Proof Pending Publication
   The defendants moved to dismiss the complaint. They ar-
gued that the presence of probable cause defeated Gonzalez's
retaliatory-arrest claims against the individual defendants.
The District Court denied the defendants' motion. Al-
though Gonzalez conceded that probable cause supported her
arrest, the court allowed her claim to advance after fnding
that it fell within an exception to the no-probable-cause rule
that we recognized in Nieves. Gonzalez v. Castle Hills,
2021 WL 4046758, *5, n. 7 (WD Tex., Mar. 12, 2021).
   The Fifth Circuit reversed that decision on appeal. The
court thought that a plaintiff's claim could fall within the
Nieves exception only if the plaintiff proffered “comparative
evidence” of “otherwise similarly situated individuals who
engaged in the same criminal conduct but were not ar-
rested.” 42 F. 4th 487, 493 (2022) (internal quotation marks
omitted). Gonzalez's claim failed because she did not pro-
vide such evidence.
   We granted certiorari. 601 U. S. ––– (2023).
658                GONZALEZ v. TREVINO

                          Per Curiam

                             II
   Gonzalez seeks reversal on two grounds. First, she asks
us to reject the Fifth Circuit's rule that plaintiffs must use
specifc comparator evidence to demonstrate that they fall
within the Nieves exception. Second, Gonzalez contends
that the Nieves no-probable-cause rule applies only to claims
predicated on split-second arrests, rather than deliberative
ones.
   We agree with Gonzalez that the Fifth Circuit took an
overly cramped view of Nieves. That court thought Gonza-
lez had to provide very specifc comparator evidence—that
is, examples of identifable people who “mishandled a govern-
ment petition” in the same way Gonzalez did but were not
arrested. 42 F. 4th, at 492. Although the Nieves exception
is slim, the demand for virtually identical and identifable
comparators goes too far.
   We recognized the Nieves exception to account for “cir-
Page Proof Pending Publication
cumstances where offcers have probable cause to make ar-
rests, but typically exercise their discretion not to do so.”
587 U. S., at 406. To fall within the exception, a plaintiff
must produce evidence to prove that his arrest occurred in
such circumstances. The only express limit we placed on
the sort of evidence a plaintiff may present for that purpose
is that it must be objective in order to avoid “the signifcant
problems that would arise from reviewing police conduct
under a purely subjective standard.” Id., at 407.
   Here, Gonzalez provided that sort of evidence. She was
charged with intentionally “remov[ing] . . . a governmental
record.” Tex. Penal Code Ann. § 37.10(a)(3). Gonzalez's
survey is a permissible type of evidence because the fact that
no one has ever been arrested for engaging in a certain kind
of conduct—especially when the criminal prohibition is long-
standing and the conduct at issue is not novel—makes it
more likely that an offcer has declined to arrest someone for
engaging in such conduct in the past.
                   Cite as: 602 U. S. 653 (2024)            659

                      Alito, J., concurring

  Because we agree with Gonzalez's frst argument, we do
not need to reach her second. We vacate the judgment
below and remand the case for the lower courts to assess
whether Gonzalez's evidence suffces to satisfy the Nieves
exception.
                                          It is so ordered.
  Justice Alito, concurring.
  The per curiam opinion correctly decides that the Fifth
Circuit took an unduly narrow view of the exception we rec-
ognized in Nieves v. Bartlett, 587 U. S. 391 (2019). I write
separately to provide further guidance on the scope of that
decision.
                              I
   Because the District Court dismissed Sylvia Gonzalez's
complaint for failure to state a claim, the per curiam opinion
properly takes its facts solely from the complaint. But I
Page Proof Pending Publication
provide a fuller account of the events leading up to her arrest
because they may typify the messy quarrels that courts will
have to sift through if we accept Gonzalez's reading of our
case law.
   Upon her election to the city council, Gonzalez launched
a campaign to oust Ryan Rapelye from his position as city
manager. As part of her efforts, Gonzalez paid personal vis-
its to Castle Hills residents, requesting their signatures and
support. According to some accounts, her efforts were ag-
gressive. Chalene Martinez averred that Gonzalez solicited
her signature “ `under false pretenses' ”—specifcally by mis-
leading her about the nature of the petitions and by lying
about Rapelye's performance in offce. Record in No. 5:20–
cv–01151 (WD Tex., Sept. 29, 2020), ECF Doc. 1, p. 9; App.
45, 52. Another resident, Jesus Quilantan, reported that
Gonzalez had asked to see his parents. When she learned
that they were not home, Gonzalez cajoled him into signing
the petition on their behalf. Id., at 57. Her efforts paid off.
660                    GONZALEZ v. TREVINO

                          Alito, J., concurring

In a town of roughly 4,000 inhabitants, she helped garner
over 300 signatures for her petition seeking Rapelye's
removal.
  At the next city council meeting, just over two weeks after
Gonzalez's election, one resident submitted a stack of docu-
ments representing the petition to remove Rapelye. As the
presiding offcer of the meeting, Mayor Edward Trevino as-
sumed control of the petition. And as the Court's opinion
notes, the meeting grew contentious. Multiple residents
spoke out in support of Rapelye. Martinez, for instance,
accused Gonzalez of misleading residents into signing the
petition based on false representations about Rapelye and
the campaign for his removal. These allegations disturbed
Trevino. The next morning, he arrived before the meeting
resumed to see if the petition contained any anomalies.
When he was fnished, he fastened the documents together
with a large black binder clip and placed the stack on top of
his other papers on the dais.
Page Proof Pending Publication
  What happened next was captured by surveillance videos.1
Shortly before the meeting began, Trevino was engaged in
conversation with two constituents. While he turned away
from his papers, Gonzalez approached the dais and took the
petition from his pile. After quickly fipping through its
pages, Gonzalez placed the petition inside her binder.
  During the meeting, Trevino could not fnd the petition
among his papers. He also noticed that Gonzalez's binder
contained a familiar stack of documents held together with a
black binder clip. But Trevino chalked this up to a coinci-
dence, and he assumed that the city secretary had already
collected the petition.
  Trevino dropped this assumption when the city secretary
asked him for the petition after the meeting. At this point,
Trevino suspected that Gonzalez had taken the petition. He
  1
   These videos are publicly available, and they can be viewed at https://
www.youtube.com/watch?v=VGXht6ARK_4 and https://www.youtube
.com/watch?v=GGLIrFiso1c.
                   Cite as: 602 U. S. 653 (2024)             661

                      Alito, J., concurring

relayed those suspicions to Captain Esteban Zuniga, a police
offcer who was present at the meeting. Zuniga walked over
to Gonzalez and asked her if she had taken the petition.
After Gonzalez denied his accusation, Trevino suggested she
check her binder.
   This, too, was captured on tape. At Trevino's prompting,
Gonzalez slowly fipped through her binder. Before she
reached the binder-clipped stack, however, she stopped and
once again denied possessing the petition. Trevino and
Zuniga simultaneously pointed to the visible black binder
clip. Forced to produce the petition, Gonzalez told Zuniga
that she thought it was an extra copy.
   Trevino fled a criminal complaint against Gonzalez, alleg-
ing that she had stolen the petition. See ante, at 656. On
account of Gonzalez's political post, the police chief tasked
Alex Wright—a peace offcer and special detective—with
leading the investigation. As a special detective, Wright is
Page Proof Pending Publication
assigned cases “which might otherwise be considered sensi-
tive . . . or delicate, either due to the nature of the crime or
. . . the parties involved.” App. 43.
   Wright conducted a thorough investigation. He inter-
viewed Trevino, Zuniga, and Martinez, each of whom gave
him their version of these events. Zuniga said that he found
it “odd” that Gonzalez claimed that she thought the petition
in her binder was an “extr[a],” given that she had strenu-
ously denied having the petition in her possession. Id., at
48. After meeting with Martinez, Wright suspected that
Gonzalez took the petition to avoid further scrutiny. Wright
contacted Gonzalez several times to hear her side of the
story, but she refused to speak with him.
   The surveillance videos, moreover, confrmed Trevino and
Zuniga's account of Gonzalez's evasiveness. From this evi-
dence, Wright concluded that Gonzalez had likely violated
Texas's anti-tampering statute, which makes it a crime for
someone to “remov[e]” a government document intentionally,
Tex. Penal Code Ann. § 37.10(a)(3) (West Cum. Supp. 2023),
662                GONZALEZ v. TREVINO

                      Alito, J., concurring

and he sought an arrest warrant from the local Magistrate.
Wright's warrant affdavit included details from his inter-
views with the witnesses and his review of the surveillance
videos. The Magistrate agreed that probable cause sup-
ported Gonzalez's arrest, and he granted Wright's request.
   The Court's opinion completes the story. After the war-
rant was issued, Gonzalez spent an evening in jail. A month
later, the district attorney dropped all charges against her.
But Gonzalez's suit against Trevino, Wright, and the police
chief is still ongoing fve years later. And Gonzalez has
never disputed—at any point of the litigation—that probable
cause supported her arrest.

                               II
   Gonzalez attacks the Fifth Circuit's judgment on two
fronts. First, she contends that the Fifth Circuit took an
unduly restrictive view of the Nieves exception. Second,
she asks us to cabin the no-probable-cause requirement to
Page Proof Pending Publication
on-the-spot arrests. The Court briskly dispatches this case
on the frst question, but I think lower courts and litigants
deserve additional guidance. I therefore divide my analysis
into three parts. First, I provide the relevant legal back-
ground for retaliatory-arrest and retaliatory-prosecution
claims. Second, I elaborate on the scope of the Nieves ex-
ception. Third, I explain why Nieves is not limited to split-
second arrests.
                             A
  “[T]he law is settled that as a general matter the First
Amendment prohibits government offcials from subjecting
an individual to retaliatory actions, including criminal prose-
cutions, for speaking out.” Hartman v. Moore, 547 U. S.
250, 256 (2006). We ordinarily analyze First Amendment re-
taliation claims under the two-step framework set out in Mt.
Healthy City Bd. of Ed. v. Doyle, 429 U. S. 274, 287 (1977).
At the frst step, the plaintiff must demonstrate that he en-
gaged in protected speech and that his speech was a “ `sub-
                    Cite as: 602 U. S. 653 (2024)             663

                       Alito, J., concurring

stantial' ” or “ `motivating' ” factor in the defendant's decision
to take action against him. Ibid. Once the plaintiff makes
this showing, the burden shifts to the defendant at the sec-
ond step to show that he would have taken the same adverse
action even in the absence of the protected speech. Ibid.
To carry these burdens, parties operating within the Mt.
Healthy framework may present a wide range of evidence—
both objective and subjective. See, e.g., id., at 282–283 (dis-
cussing the plaintiff's behavioral history in the years leading
up to the litigation); Texas v. Lesage, 528 U. S. 18, 19 (1999)
(per curiam) (the defendants produced an affdavit to explain
that the plaintiff's application to graduate school was re-
jected because of his poor personal statement).
   Our cases have admitted, however, that this framework
fts uneasily with First Amendment retaliatory-arrest and
retaliatory-prosecution claims for at least three reasons.
First, it is all too easy for a plaintiff to subject a law-
Page Proof Pending Publication
enforcement offcer to the crucible of litigation based on alle-
gations about an offcer's state of mind that are easy to make
and diffcult to disprove. For example, a driver with an
anti-police bumper sticker on his car could claim that any
traffc stop was due to his protected speech. Any person
who carries a sign while trespassing, blocking traffc, or dis-
turbing the peace could similarly allege that an arrest for
these offenses was motivated by the sign's message. We are
loath to undertake such inquiries into subjective intent in
the law-enforcement context. Cf. Ashcroft v. al-Kidd, 563
U. S. 731, 737 (2011); see also Kentucky v. King, 563 U. S. 452,
464 (2011); Whren v. United States, 517 U. S. 806, 812 (1996).
   Second, protected speech is often a “wholly legitimate con-
sideration” for offcers when deciding whether to fle charges
or to make an arrest. Reichle v. Howards, 566 U. S. 658,
668 (2012). An “offcer may decide to arrest [a] suspect be-
cause his speech provides evidence of a crime or suggests a
potential threat.” Ibid. The facts of Nieves itself illustrate
this point. In that case, the police offcers decided to arrest
664                 GONZALEZ v. TREVINO

                      Alito, J., concurring

the plaintiff for disorderly conduct and resisting arrest be-
cause “they perceived [the plaintiff] to be a threat” based in
part on the combative tone and content of his speech. 587
U. S., at 401. And no one suggested that an individual's
speech is off-limits in this respect. Ibid. (explaining that
“the content and manner of a suspect's speech” may provide
important information for law enforcement).
   Third, the machinery of criminal justice of ten works
 through multiple government offcers. An offcer who makes
an arrest may do so based on his own judgment, orders from
a superior, or as in this case, a warrant issued by a magis-
trate. Thus, it is often challenging to draw a straight line
between the plaintiff's protected speech and the defendant
from whom he seeks recovery. In such circumstances, it
may be diffcult to discern whether the offcer acted improp-
erly. Cf. Messerschmidt v. Millender, 565 U. S. 535, 546
(2012) (noting that “the fact that a neutral magistrate has
Page Proof Pending Publication
issued a warrant is the clearest indication that the [arresting]
offcers acted in an objectively reasonable manner”); Bilida
v. McCleod, 211 F. 3d 166, 174–175 (CA1 2000) (Boudin, J.)
(“Plausible instructions from a superior or fellow offcer sup-
port qualifed immunity where, viewed objectively in light of
the surrounding circumstances, they could lead a reasonable
offcer to conclude that the necessary legal justifcation for
his actions exists”).
   For these reasons, we have required plaintiffs pressing
such claims to prove the absence of probable cause as a
threshold requirement before they can advance their claims
under the Mt. Healthy framework. We defended this re-
quirement on the assumption that the “existence of probable
cause will be at issue in practically all” retaliatory-arrest or
retaliatory-prosecution cases given its obvious evidentiary
value. Nieves, 587 U. S., at 400 (internal quotation marks
omitted). Thus, we reasoned that this requirement, which
imposes “little or no added cost” on the parties or the court,
was a small price to pay for a plaintiff seeking to discard
                     Cite as: 602 U. S. 653 (2024)                665

                         Alito, J., concurring

the presumption of good faith we afford to law-enforcement
offcials. Ibid. (internal quotation marks omitted).
   In Nieves, however, we recognized a narrow exception to
the no-probable-cause rule. While a showing of probable
cause generally defeats a retaliatory-arrest claim, we ob-
served that this requirement should be relaxed “where off-
cers have probable cause to make arrests, but typically exer-
cise their discretion not to do so.” Id., at 406. Concerned
that some police offcers might exploit the arrest power as a
means of suppressing disfavored speech, we explained that
the no-probable-cause requirement may be set aside “when
a plaintiff presents objective evidence that he was arrested
when otherwise similarly situated individuals not engaged in
the same sort of protected speech had not been.” Id., at
407; cf. United States v. Armstrong, 517 U. S. 456, 470 (1996).
   In recognizing this exception, we emphasized that it is
merely a “narrow qualifcation” to the general rule. Nieves,
587 U. S., at 406. And to illustrate the thinness of this ex-
Page Proof Pending Publication
ception, Nieves offered the example of a vocal critic of the
police who is arrested for jaywalking. Id., at 407. The un-
yielding enforcement of a no-probable-cause requirement in
this context would be insuffciently protective of the plain-
tiff's First Amendment rights because the defendant's ani-
mus is a much likelier explanation for such an arrest than the
mere existence of probable cause. We chose this example
because jaywalking represents the type of relatively benign
offense that is “endemic but rarely results in arrest.” Ibid.
                                  B
   Because Gonzalez concedes that her arrest was supported
by probable cause, her claim can proceed only if she falls
within Nieves's exception.2 Under this exception, a plain-
tiff's inability to prove the absence of probable cause is ex-
cused only if the plaintiff presents “objective evidence that
  2
   For this reason, I assume for the sake of argument that her alleged
conduct constituted a violation of Texas's anti-tampering statute.
666                GONZALEZ v. TREVINO

                     Alito, J., concurring

he was arrested when otherwise similarly situated individu-
als not engaged in the same sort of protected speech had not
been.” Ibid.
   The Court is correct to note that a plaintiff must provide
objective evidence to fall within the Nieves exception. We
enforce this requirement to avoid “the signifcant problems
that would arise from reviewing police conduct under a
purely subjective standard.” Ibid.; see also Horton v. Cali-
fornia, 496 U. S. 128, 138 (1990) (“[E]venhanded law enforce-
ment is best achieved by the application of objective stand-
ards of conduct, rather than standards that depend upon the
subjective state of mind of the offcer”). For that reason,
evidence regarding an offcer's state of mind—e. g., evidence
of bad blood between the offcer and the plaintiff or allega-
tions that the offcer harbored animus—does not qualify.
   The defendants argue that permitting anything other than
the kind of strict comparator evidence demanded by the
Page Proof Pending Publication
Fif th Circuit will defeat the whole purpose of the no-
probable-cause rule. Our decisions refect our sensitivity to
these concerns, see Lozman v. Riviera Beach, 585 U. S. 87,
98 (2018), but a proper application of the Nieves exception
will not produce this result for at least two reasons.
   First, courts must remember that the exception is just
that—an exception, and a narrow one at that. Judges
should not confate the question whether certain evidence
can be considered under the Nieves exception with the en-
tirely distinct question whether the evidence suffces to sat-
isfy this threshold inquiry. We have long recognized “[t]he
deep-rooted nature of law-enforcement discretion,” Castle
Rock v. Gonzales, 545 U. S. 748, 761 (2005), and a plaintiff
therefore must surmount a very high bar when the offcial
can point to the existence of probable cause underpinning an
arrest. The example in Nieves of a police offcer arresting
a vocal critic for jaywalking serves as a helpful benchmark
for courts and litigants. A plaintiff may satisfy the Nieves
exception only by providing comparably powerful evidence.
                   Cite as: 602 U. S. 653 (2024)            667

                      Alito, J., concurring

   Second, evidence that tends to show only that the plain-
tiff's constitutionally protected speech was a “substantial or
motivating factor” behind the adverse action should not be
considered unless and until the plaintiff can provide other
evidence to satisfy the Nieves exception. Lozman, 585
U. S., at 97. This requirement fows from the recognition
that the Nieves exception serves only as a gateway to the
Mt. Healthy framework. The Ni eves exception asks
whether the plaintiff engaged in the type of conduct that is
unlikely to result in arrest or prosecution. By contrast, the
Mt. Healthy inquiry is keyed toward whether the defendant's
adverse decision was infuenced by the plaintiff's constitu-
tionally protected speech.
   To see how these principles operate in practice, consider
the following hypothetical. Suppose a plaintiff charged with
a particular crime brings three pieces of evidence. First, he
proffers an affdavit from an offcer testifying that no one has
Page Proof Pending Publication
been prosecuted in the jurisdiction for engaging in similar
conduct. Second, he produces a statistical study corroborat-
ing the affdavit. And third, the plaintiff testifes that a po-
lice offcer has been surveilling his house for several weeks.
The frst two pieces of evidence count toward the Nieves
exception, but the third piece of evidence does not. Instead,
the third piece of evidence can be considered only after his
claim advances to the Mt. Healthy framework. Any other
approach would render the Mt. Healthy framework redun-
dant in most, if not all, cases.
   In Nieves, three Justices dissented at least in part and
would have permitted plaintiffs in cases with probable cause
to proceed to trial if they were able to survive summary
judgment under Mt. Healthy. They argued their positions
forcefully and well, but it is not faithful to our precedent to
use the “narrow” Nieves exception as a crowbar for over-
turning the core of that decision's holding, supported by six
Justices—namely, that the existence of probable cause either
always or nearly always precludes a suit like this one.
668                GONZALEZ v. TREVINO

                     Alito, J., concurring

   I now turn to the facts of Gonzalez's case. Here, her evi-
dence is of the type that plaintiffs can use in making out
their case under the Nieves exception. I agree with the
Court that a plaintiff does not need to identify another per-
son who was not arrested under the same law for engaging
in a carbon-copy course of conduct. Our jaywalking exam-
ple in Nieves plainly proves this point. We did not suggest
that a vocal critic of the police charged with jaywalking had
to produce evidence that police offcers knowingly refused to
arrest other specifc jaywalkers. And we certainly did not
suggest that this jaywalker had to fnd others who com-
mitted the offense under the same conditions as those in his
case—for example, on a street with the same amount of traf-
fc traveling at the same speed within a certain distance from
a crosswalk at the same time of day.
   On remand, the Fifth Circuit must determine whether
Gonzalez's survey is enough for her claim to advance to the
Page Proof Pending Publication
Mt. Healthy framework. The Nieves exception is most
easily satisfed by strong affrmative evidence that the de-
fendant let other individuals off the hook for comparable be-
havior. But when a plaintiff's claim hinges on negative evi-
dence, like what Gonzalez offers here, context is key for
determining the strength of his case. When a plaintiff's al-
leged criminal conduct is egregious or novel, for instance,
the lack of similar arrests might warrant little weight.
Courts must also ensure that they are assessing the plain-
tiff's conduct at the appropriate level of generality because
every arrest, if defned too specifcally, can be described as
the first of its kind. If a plaintiff could evade the no-
probable-cause requirement simply by submitting evidence
that no one who engaged in an exact duplicate of his behavior
had been arrested, courts will be “fooded with dubious re-
taliatory arrest suits,” Lozman, 585 U. S., at 98, and the
Nieves's exception would drain the no-probable-cause re-
quirement of all force.
                      Cite as: 602 U. S. 653 (2024)                 669

                         Alito, J., concurring

                                   C
   We also granted certiorari on whether the Nieves no-
probable-cause rule applies beyond split-second arrests.
The parties vigorously contested this question in briefng
and at oral argument, yet the Court today reserves judg-
ment on this issue. I disagree with this course. In my
view, Nieves already answered this question in the affrma-
tive after faithfully applying our precedents.
   Nothing about Nieves's rationale depends on whether the
offcer made a split-second arrest of the plaintiff.3 That de-
cision expressly borrowed the no-probable-cause rule and its
underlying justifcations from Hartman, the seminal case
governing retaliatory-prosecution claims. Nieves self-
consciously emulated Hartman because both types of retali-
ation claims share the same critical characteristics.
   Three features stand out. For one thing, courts ad-
judicating either claim face the “ultimate problem” of
Page Proof Pending Publication
determining “whether the adverse government action was
caused by the offcer's malice or the plaintiff's potentially
criminal conduct.” Nieves, 587 U. S., at 402; see also Hart-
man, 547 U. S., at 265. The causal challenge is similarly
complex in both contexts because “protected speech is often
a `wholly legitimate consideration' ” for offcers deciding
whether to launch a prosecution or to make an arrest.
Nieves, 587 U. S., at 401. For another, with or without the
no-probable-cause rule, the presence or absence of probable
cause plays a similarly vital role in both retaliatory-arrest
and retaliatory-prosecution cases. That is because “ `evi-
dence of the presence or absence of probable cause . . . will
be available in virtually every' ” retaliatory-prosecution or
retaliatory-arrest case and because such evidence speaks vol-

  3
   Indeed, the plaintiff in Nieves implied that the offcer held a grudge
against him before he even had an opportunity to take the plaintiff into
custody. See 587 U. S., at 396–397.
670                    GONZALEZ v. TREVINO

                          Alito, J., concurring

umes about the objective reasonableness of a defendant's ac-
tion. Ibid.; see also Hartman, 547 U. S., at 265. Lastly, by
focusing the inquiry on objective indicia of reasonableness,
a no-probable-cause rule refects our general reluctance
to probe the subjective intent of law-enforcement offcers.
Nieves, 587 U. S., at 403; see also Hartman, 547 U. S., at
263–265.
   This analysis—none of which turns on whether an arrest
was made in a split-second context—is plainly incompatible
with Gonzalez's theory. And it would be bizarre to think
Nieves silently limited itself to split-second decisions when
the reasoning it imported came from the retaliatory-
prosecution context, which by defnition involves only delib-
erative government acts.4
   Gonzalez argues that we should limit Nieves to split-
second cases because, in her view, a retaliatory-arrest claim
is analogous to the common-law tort of abuse of process,
which lacks a no-probable-cause requirement. Tr. of Oral
Page Proof Pending Publication
Arg. 5–6. She urges us to rely on the abuse-of-process anal-
ogy to draw a line between split-second arrests with no proc-
ess and arrests pursuant to process that can be likened to
the common-law tort. Ibid.
   Gonzalez's appeal to the common law is wrong twice over.
To start, she is wrong to suggest that the abuse-of-process
tort was somehow not before us when we decided Nieves.
Our prior decision in Hartman gave full consideration to
whether abuse of process was the appropriate analog for a
retaliatory-prosecution claim. See 547 U. S., at 258 (noting
  4
    It is certainly true that we made a feeting reference to split-second
arrests in Nieves. Specifcally, we mentioned that offcers often must
make quick, diffcult assessments of a potential arrestee's conduct and
speech to determine whether the subject poses a threat. 587 U. S., at 401.
But we offered that observation as an additional justifcation for the no-
probable-cause rule rather than as a limit on the rule's applicability. The
“ultimate problem” remains the diffculty of fguring out whether the ar-
rest was motivated by “the offcer's malice or the plaintiff's potentially
criminal conduct.” Id., at 402 (emphasis added).
                    Cite as: 602 U. S. 653 (2024)             671

                       Alito, J., concurring

that “we could debate whether the closer common-law analog
to retaliatory prosecution is malicious prosecution (with its
no-probable-cause element) or abuse of process (without it)”).
By holding that such a claim requires a plaintiff to prove
there was no probable cause for the charge, Hartman neces-
sarily rejected the force of any analogy to abuse of process.
In Nieves, the core dispute was whether we should ex-
tend the same no-probable-cause requirement to retaliatory-
arrest claims. Once we decided to do so, we copied Hart-
man's reasoning. It is therefore quite clear that the Nieves
Court was aware of the abuse-of-process tort, as well as the
argument that this tort should govern our decision. And if
we needed any reminding, the United States argued in Nieves
that “[a] retaliatory-arrest claim is not analogous to the tort of
abuse of process.” Brief for United States as Amicus Cu-
riae in Nieves v. Bartlett, O. T. 2018, No. 17–1174, p. 10, n. 2.
   Gonzalez's common-law argument suffers from another
Page Proof Pending Publication
defect. It is well settled that common-law principles are
meant to serve as helpful guides rather than prefabricated
components of a 42 U. S. C. § 1983 claim. Manuel v. Joliet,
580 U. S. 357, 370 (2017); see also Rehberg v. Paulk, 566 U. S.
356, 366 (2012) (“[T]he Court has not suggested that § 1983
is simply a federalized amalgamation of pre-existing
common-law claims”). At the end of the day, none of our
decisions in this area has unthinkingly outsourced our analy-
sis to the common law of torts. In Hartman, for instance,
we expressly declined the parties' “invitation to rely on
common-law parallels,” and never took a position on whether
malicious prosecution or abuse of process was the better ana-
log to retaliatory prosecution. 547 U. S., at 258. And in
Nieves, we looked to the common law only to “confr[m]”
what we had already concluded: that the same no-probable-
cause requirement we established in Hartman should also
apply to retaliatory-arrest claims. 587 U. S., at 405.
Common-law torts can assist our analysis, but they do not
dictate every dimension of a § 1983 claim.
672                   GONZALEZ v. TREVINO

                         Alito, J., concurring

   And that is for good reason. Many § 1983 claims “can be
favorably analogized to more than one of the ancient
common-law forms of action.” Wilson v. Garcia, 471 U. S.
261, 272–273 (1985). Because any analogy to a common-law
cause of action is thus “bound to be imperfect,” id., at 272,
we necessarily deal in generalities when we look to the com-
mon law to defne § 1983 claims.5 The specifc facts of a
given case might align more or less well with the chosen
common-law analog, but until today no one has suggested
that our jurisprudence requires courts to toggle between dif-
ferent tort analogies within the same class of § 1983 claims.
Consider the parties' arguments in Hartman. The defend-
ants urged us to analogize retaliatory-prosecution claims to
the malicious-prosecution tort, while the plaintiff suggested
that abuse of process might be the more apt analog. Brief
for Petitioners 25–30 and Brief for Respondent 41–42 in
Hartman v. Moore, O. T. 2005, No. 04–1495. But neither
party asked us to adopt the malicious-prosecution analogy
Page Proof Pending Publication
for some § 1983 retaliatory-prosecution claims while relying
on the abuse-of-process analogy for others.
   Gonzalez, by contrast, invites us to slice and dice every
complaint alleging a retaliatory-arrest claim based on a quick
skim of the facts at the motion-to-dismiss stage. Under her
view, the elements of a plaintiff's meritorious § 1983 claim
may evolve throughout the lawsuit as more facts are dis-
covered and verifed. I see little value in endorsing this
awkward and predictably ineffcient innovation.
   Gonzalez's proposed limit on Nieves would also be unwork-
able in practice because it raises thorny line-drawing ques-
tions about the meaning of a “split-second” decision to arrest.
Consider an offcer who surveils a political dissident for many
months with the plan of arresting him the moment he broke

  5
    First Amendment retaliation claims offer a particularly good example
of this point. Justice Thomas's dissent in this case shows, at a mini-
mum, that there are strong reasons to suspect that the abuse-of-process
tort is an inferior analog compared to the torts of false imprisonment,
malicious arrest, and malicious prosecution. See post, at 676–679.
                   Cite as: 602 U. S. 653 (2024)            673

                   Kavanaugh, J., concurring

the law. Would that arrest be considered a split-second de-
cision under Gonzalez's view? Or suppose that an arresting
offcer takes several minutes to confer with another offcer on
the scene. Would the no-probable-cause requirement apply?
What if an offcer takes time to ensure that everyone at a
crime scene is safe before completing an arrest? These hy-
potheticals illustrate the vast practical diffculties with Gon-
zalez's theory, and there is no principled basis for drawing
such fnely grained lines in any event.
   A “split-second” rule would also create a perverse incen-
tive for police offcers to make quick arrest decisions rather
than proceeding in a deliberative manner. Gonzalez's test
punishes the city offcials for seeking a warrant from a neu-
tral magistrate before arresting her. Under her approach,
the defendants would have been better off if they had ar-
rested her immediately. I see no good reason to switch out
Nieves for a novel doctrinal dichotomy that generates such
Page Proof Pending Publication
counterintuitive results.
   In sum, Nieves applies to all retaliatory-arrest claims
brought under § 1983. And that decision means what it
says. “[P]robable cause should generally defeat a retalia-
tory arrest claim,” and a plaintiff bringing such a claim
“must plead and prove the absence of probable cause for the
arrest” unless he can ft within its narrow exception. 587
U. S., at 402, 406. Nothing in the Court's decision today
should be understood as casting doubt on this holding.

                               III
  With these observations, I join the Court's opinion.

  Justice Kavanaugh, concurring.
   Sylvia Gonzalez was arrested for intentionally stealing a
government record. See Tex. Penal Code Ann. § 37.10(a)(3)
(West Cum. Supp. 2023). Gonzalez sued city offcials under
42 U. S. C. § 1983, alleging that she was arrested in retalia-
tion for First Amendment-protected activity.
674                GONZALEZ v. TREVINO

                   Kavanaugh, J., concurring

   But Gonzalez conceded that city offcials had probable
cause to arrest her for intentionally removing the govern-
ment record. (A video shows Gonzalez putting the govern-
ment record into her binder at a city council meeting. See
ante, at 659–662 (Alito, J., concurring).) An arrestee ordi-
narily cannot sue a public offcial under § 1983 for retaliatory
arrest if the offcial had probable cause to make the arrest.
See Nieves v. Bartlett, 587 U. S. 391, 404 (2019). To somehow
maintain her § 1983 suit, Gonzalez invoked what is known
as the Nieves exception. That exception applies when an
individual is arrested for minor criminal conduct where off-
cers “typically exercise their discretion not” to arrest. Id.,
at 406. The prime example is jaywalking. Id., at 407.
   To come within the Nieves exception, Gonzalez was re-
quired to present “objective evidence” that she was arrested
when “similarly situated individuals” who engaged in the
same conduct would not have been arrested. Ibid. Of
Page Proof Pending Publication
course, Gonzalez could not plausibly claim that people in
Texas who steal things (or more precisely here, who steal
government records) do not get arrested. Instead, she says
that she took the government record accidentally, not inten-
tionally, and that people who accidentally remove govern-
ment documents are not arrested.
   Properly understood, that is not a Nieves-exception claim
at all. The Nieves exception is a conduct-based comparison.
Only if the conduct does not usually trigger an arrest under
any statute can you have a Nieves-exception claim—like jay-
walking. Gonzalez's argument turns not on her conduct
(taking government records) but rather on her mens rea.
She essentially argues that an objectively reasonable offcer
would have known that Gonzalez accidentally rather than in-
tentionally took the government record.
   When Gonzalez conceded that the offcials had probable
cause to arrest her, however, she necessarily conceded that
the offcers had probable cause to conclude that she “in-
tentionally” removed the document. Tex. Penal Code Ann.
                   Cite as: 602 U. S. 653 (2024)            675

                     Jackson, J., concurring

§ 37.10(a)(3). That may have been an unwise concession.
But it should have foreclosed Gonzalez's attempt to contest
her mens rea for purposes of her § 1983 retaliatory arrest
claim. And even if Gonzalez had not made the concession,
the question here would be whether an objectively reason-
able offcer would have known that Gonzalez accidentally
(rather than intentionally) took the document. In short, this
is (at most) a case about probable cause as to mens rea, not
about conduct-based comparisons. This case has nothing to
do with the Nieves exception.
   At this point, the Court's grant of certiorari looks ill-
advised given that the question presented about the Nieves
exception bears no relation to the issue on which Gonzalez's
suit actually turns. In any event, we are where we are. I
concur in the per curiam because the per curiam does not
seem to say anything that is harmful to the law, even though
the per curiam (in my view) does not really have anything
to do with Gonzalez's case.
Page Proof Pending Publication
  Justice Jackson, with whom Justice Sotomayor joins,
concurring.
  Today, the Court rightly recognizes that petitioner Sylvia
Gonzalez's survey—showing that, in the last decade, no one
charged with the crime for which she was arrested had en-
gaged in conduct similar to hers—is objective evidence ad-
missible to prove that she “was arrested when otherwise
similarly situated individuals not engaged in the same sort
of protected speech had not been.” Nieves v. Bartlett, 587
U. S. 391, 407 (2019); see ante, at 658.
  That recognition, however, should not be taken to suggest
that plaintiffs cannot use other types of objective evidence
to make this showing. The Nieves exception is satisfed in
“circumstances where offcers have probable cause to make
arrests, but typically exercise their discretion not to do so.”
587 U. S., at 406. “The only express limit we placed on the
sort of evidence a plaintiff may present for that purpose is
676                     GONZALEZ v. TREVINO

                          Thomas, J., dissenting

that it must be objective.” Ante, at 658. As the United
States explains, such objective evidence could “include off-
cers' employment of an unusual, irregular, or unnecessarily
onerous arrest procedure,” as well as “[t]he timing of and
events leading up to a plaintiff's arrest.” Brief for United
States as Amicus Curiae 20.* Similarly, “if offcers falsely
document the arrest or include other indicia of retaliatory
motive in arrest-related documents, that too might suggest
meaningfully differential treatment.” Id., at 21.
   Here, in addition to her survey, Gonzalez presented this
other kind of evidence as well. Before the District Court,
Gonzalez pointed to, among other things, details about the
anomalous procedures used for her arrest and statements in
the arresting offcer's warrant affdavit suggesting a retalia-
tory motive. See Brief for Petitioner 43–44. Those catego-
ries of evidence, too, can support the conclusion that Gon-
zalez “was arrested when otherwise similarly situated
individuals not engaged in the same sort of protected speech
Page Proof Pending Publication
had not been.” Nieves, 587 U. S., at 407. On remand, the
lower courts may consider the full scope of objective evi-
dence that Gonzalez has offered to establish differential
treatment. See ante, at 658.
   With this understanding, I join the Court's per curiam
opinion.
  Justice Thomas, dissenting.
  I continue to believe that “plaintiffs bringing a First
Amendment retaliatory-arrest claim under § 1983 should
have to plead and prove a lack of probable cause.” Lozman
   *Justice Alito suggests that evidence of this sort—such as the fact
that “a police offcer has been surveilling [a plaintiff's] house for several
weeks”—would not “count toward the Nieves exception.” Ante, at 667
(concurring opinion). He does not explain, however, why such evidence
would not be objective, or why such evidence would not be relevant to
proving that a plaintiff “was arrested when otherwise similarly situated
individuals not engaged in the same sort of protected speech had not
been.” Nieves, 587 U. S., at 407.
                       Cite as: 602 U. S. 653 (2024)                    677

                          Thomas, J., dissenting

v. Riviera Beach, 585 U. S. 87, 107 (2018) (Thomas, J., dis-
senting).* Under the Court's precedents, 42 U. S. C. § 1983
is “construed in light of common-law principles that were
well settled at the time of its enactment.” Kalina v. Flet-
cher, 522 U. S. 118, 123 (1997). “Because no common-law
tort for retaliatory arrest in violation of the freedom of
speech existed when § 1983 was enacted, we look to the
common-law torts that provide the closest analogy to this
claim.” Nieves v. Bartlett, 587 U. S. 391, 409 (2019)
(Thomas, J., concurring in part and concurring in judgment)
(internal quotation marks and alteration omitted). As I
have previously explained, the common-law torts most analo-
gous to retaliatory-arrest claims are false imprisonment, ma-
licious arrest, and malicious prosecution—all of which re-
quired a plaintiff to prove “the absence of probable cause.”
Id., at 409–410. Gonzalez concedes that there was probable
cause for her arrest. Brief for Petitioner 30. Her
retaliatory-arrest claim therefore cannot proceed.
Page Proof Pending Publication
   Resisting that conclusion, Gonzalez contends that there is
still another common-law analogue for a retaliatory-arrest
claim: abuse of process. Although the exact contours of that
tort are unclear, abuse of process generally addressed the
“extortionate perversion of lawfully initiated process to ille-
gitimate ends.” Heck v. Humphrey, 512 U. S. 477, 486, n. 5
(1994). Critically for Gonzalez's argument, an abuse-of-
process claim did not require a plaintiff to establish the ab-
sence of probable cause. See C. Addison, Wrongs and Their
Remedies 601–602 (3d ed. 1870) (Addison); 1 T. Cooley, Law
of Torts 356 (3d ed. 1906) (Cooley).

   *I also remain “skeptical that 42 U. S. C. § 1983 recognizes a claim for
retaliatory arrests under the First Amendment.” Lozman, 585 U. S., at
104, n. 2 (Thomas, J., dissenting). “Because no party questions whether
§ 1983 claims for retaliatory arrests under the First Amendment are ac-
tionable, I assume that § 1983 permits such claims.” Nieves v. Bartlett,
587 U. S. 391, 409, n. (2019) (Thomas, J., concurring in part and concurring
in judgment).
678                 GONZALEZ v. TREVINO

                      Thomas, J., dissenting

   I am not persuaded that an abuse-of-process claim is analo-
gous to Gonzalez's retaliatory-arrest claim. Gonzalez's cen-
tral argument is that her arrest was invalid because the de-
fendants had an improper motive. As she sees it, even
though the defendants had probable cause to arrest her, they
did so only in retaliation for her constitutionally protected
speech. See App. to Pet. for Cert. 126a, 129a. Abuse of
process, however, appeared to be less concerned with why
process was initiated and more with whether process was
ultimately used as “intended by the law.” Mayer v. Walter,
64 Pa. 283, 285–286 (1870); see Addison 602 (abuse-of-process
tort applies where process has been “prostituted to an illegal
purpose”). An abuse of process occurred when an ordinary
process was distorted “for a purpose not justifed by the
law,” and the tort required “ `an act in the use of the process
not proper in the regular prosecution of the proceeding.' ”
Cooley 354–356. For example, a plaintiff could assert an
Page Proof Pending Publication
abuse-of-process claim if an offcer arrested and detained him
in an oppressive manner as a means of extortion. See id.,
at 354–355 (providing as an example “causing an arrest . . .
and keeping [the plaintiff] imprisoned until, by stress
thereof, he is compelled to surrender property to which the
other is not entitled”). Or, a plaintiff could bring an abuse-
of-process claim if an offcer deprived him of food while he
was detained. Wood v. Graves, 144 Mass. 365, 366, 11 N. E.
567, 576 (1887) (describing where a person “arrested . . . is
treated with cruelty, is deprived of proper food, or is other-
wise treated with oppression and undue hardship”). Either
way, the essential question appears to have been how the
process was used—not whether the process was initiated
with an improper motive. See Glidewell v. Murray-Lacy &
Co., 124 Va. 563, 569, 98 S. E. 665, 667 (1919) (explaining that
the “distinctive nature of an action for abuse of process . . .
lies for the improper use of a regularly issued process, not
for maliciously causing process to issue”); Cooley 356 (“ `Reg-
ular and legitimate use of process, though with a bad inten-
                   Cite as: 602 U. S. 653 (2024)           679

                     Thomas, J., dissenting

tion, is not a malicious abuse of process' ”). Because Gonza-
lez's retaliatory-arrest claim focuses on the motives behind
her arrest and not the process itself, the abuse-of-process
tort is a poor ft.
   The Court takes an even more dubious route in its at-
tempt to salvage Gonzalez's case. In Nieves v. Bartlett, the
Court correctly recognized that probable cause precludes a
retaliatory-arrest claim. 587 U. S., at 406. But, it intro-
duced one purportedly “narrow qualifcation.” Ibid.; see
Lund v. Rockford, 956 F. 3d 938, 944 (CA7 2020) (considering
whether a plaintiff's “case squeeze[d] through the crack of an
opening that Nieves left ajar”). The Nieves Court con-
cluded that a plaintiff need not show a lack of probable cause
if he “presents objective evidence that he was arrested when
otherwise similarly situated individuals not engaged in the
same sort of protected speech had not been.” 587 U. S.,
at 407.
   Today, the Court expands that qualifcation. Nieves's ex-
Page Proof Pending Publication
ception can now apply if a plaintiff presents evidence of any
objective fact that “makes it more likely that an offcer has
declined to arrest someone for engaging in such conduct
in the past.” Ante, at 658 (emphasis deleted). Accordingly,
even though Gonzalez's proffered evidence does not point to
a single “similarly situated individua[l],” the Court none-
theless concludes she may satisfy the Nieves exception.
Nieves, 587 U. S., at 407.
   There is “no basis in either the common law or our First
Amendment precedents” for the exception created in Nieves
and expanded upon today. Id., at 409 (opinion of Thomas,
J.). And, the Court should not craft § 1983 rules “as a mat-
ter of policy.” Id., at 411. I would adhere to the only rule
grounded in history: Probable cause defeats a retaliatory-
arrest claim. I respectfully dissent.
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

None

```

---

## GROUP: content/cases/Graham v. Barnette.md  (`case`, 5 assertions)

### content_page

```
---
title: "Graham v. Barnette"
type: case
citation: "5 F.4th 872 (2021)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 8th Circuit"
court_level: coa
circuit: 8th
year: 2021
date_decided: 2021-07-16
docket: 19-2512
authority_weight: "Binding in-circuit — 8th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2021-07-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Graham v. Barnette
  varies_by_point: false
  scope_note: "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/"
  cluster_id: 4900401
  opinion_id: 4704180
  identity_checked: true
homes:
  - page: "[[Community Caretaking]]"
    role: "Key — Progeny / Limit"
related: ["[[Caniglia v. Strom]]", "[[United States v. Garner]]", "[[United States v. Rideau]]", "[[Cady v. Dombrowski]]"]
aliases: ["Teresa Graham v. Shannon Barnette", "Graham v. Barnette (8th Cir. 2021)"]
tags: ["case", "fourth-amendment", "community-caretaking", "mental-health-seizure", "probable-cause", "qualified-immunity", "eighth-circuit", "persons-in-public"]
holding: "After Caniglia v. Strom, using the 'community caretaking' label for warrantless psychiatric seizures is a category error; a seizure of a person for an emergency mental-health evaluation is reasonable under the Fourth Amendment only on probable cause that the person is mentally ill and dangerous to herself or others (though the officers received qualified immunity because that standard was not clearly established in the circuit)."
lake:
  record_id: Graham v. Barnette
  status: verified
  projected_at: 2026-07-09
---

# Graham v. Barnette

*5 F.4th 872 (8th Cir. 2021)* · U.S. Court of Appeals, 8th Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a series of escalating 911 calls on May 25, 2017 — including an anonymous caller claiming to be Teresa Graham's cousin who requested a "welfare check" and referenced a possible mental-health history — Sergeant Barnette ordered Minneapolis officers to take Graham into custody for an emergency mental-health evaluation under Minnesota's civil-commitment statute. The officers entered Graham's home, seized her, and transported her to a hospital, all without a warrant. Graham sued the officers and the City under 42 U.S.C. § 1983. The district court granted the officers summary judgment; the Eighth Circuit affirmed in 2020 (970 F.3d 1075), and the Supreme Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for reconsideration in light of [[Caniglia v. Strom]].

## Issue
[[Reading and Citing Cases#on-remand|On remand]] after *[[Caniglia v. Strom|Caniglia]]*, whether the "community caretaking" framing supports a warrantless seizure of a person for a mental-health evaluation, and what Fourth Amendment standard governs such a seizure.

## Rule
After *[[Caniglia v. Strom|Caniglia]]*, the "community caretaking" label does not fit a psychiatric seizure. "Now that *Caniglia* has made clear that 'there is no overarching "[[Community Caretaking|community caretaking]]" doctrine,' . . . our use of that label seems to be a category error." — *Graham v. Barnette*, 5 F.4th 872 (8th Cir. 2021) (slip op., at 10). ^pin-op10

The governing standard is probable cause of dangerousness: "we again conclude that probable cause of dangerousness is the standard that must be met for a warrantless mental-health seizure to be reasonable under the Fourth Amendment." — *Id.* (slip op., at [10](https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/#:~:text=we%20again%20conclude%20that%20probable)). ^pin-op10a

The court noted that "[a]t least nine of our sister circuits have held that the Fourth Amendment requires probable cause that a person is mentally ill and dangerous to herself or others for a seizure for an emergency mental-health evaluation to be reasonable." — *Id.* (slip op., at 10-11). ^pin-op10b

## Application
On these facts, the court reaffirmed (prong one) that the officers needed probable cause that Graham was mentally ill and dangerous to herself or others to seize her for a mental-health evaluation, and it rejected the "community caretaking" label as the analytic frame. *[[Caniglia v. Strom|Caniglia]]* did not disturb that reasoning, because the Supreme Court there "refrain[ed]" from addressing the standards for "emergency seizures for psychiatric treatment, observation, or stabilization." But because Eighth Circuit case law had previously been ambiguous — some precedents suggesting a lower "reasonable belief" standard — the probable-cause-of-dangerousness rule was not clearly established at the time of Graham's seizure, so the officers were entitled to [[Qualified Immunity|qualified immunity]] on that claim.

## Conclusion
The Eighth Circuit again affirmed summary judgment for the officers on qualified-immunity grounds, while holding that probable cause of dangerousness — not a "community caretaking" rationale — is the standard a warrantless mental-health seizure must satisfy under the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 8th Cir.**
- *Graham* is the Eighth Circuit's post-*[[Caniglia v. Strom|Caniglia]]* **limit** on the caretaking framing: it treats the "community caretaking" label for psychiatric seizures as a category error and routes such seizures through **probable cause of dangerousness**. It builds on [[Caniglia v. Strom]] (no freestanding community-caretaking entry into the home) and stands alongside the persons-in-public caretaking-detention line of [[United States v. Garner]] (10th Cir.) and [[United States v. Rideau]] (5th Cir.), which address brief caretaking detentions rather than full psychiatric seizures.

## Appears on
- [[Community Caretaking]] — *Key — Progeny / Limit*

## Sources
- *Graham v. Barnette*, 5 F.4th 872 (8th Cir. 2021) — https://www.courtlistener.com/opinion/4900401/teresa-graham-v-shannon-barnette/ — pinpoints given as slip-opinion pages (slip op., at 10-11); CourtListener carries the slip opinion (cluster 4900401 → opinion 4704180).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b1c6d1acc66b0bd6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "5 F.4th 872 (2021)", "court": "U.S. Court of Appeals, 8th Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Graham v. Barnette", "year": "2021"}}
{"assertion_id": "81b3b9e9b5de2ed6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "After Caniglia v. Strom, using the 'community caretaking' label for warrantless psychiatric seizures is a category error; a seizure of a person for an emergency mental-health evaluation is reasonable under the Fourth Amendment only on probable cause that the person is mentally ill and dangerous to herself or others (though the officers received qualified immunity because that standard was not clearly established in the circuit).", "title": "Graham v. Barnette"}}
{"assertion_id": "e5ddd0f7896d9549", "dimension": "support", "kind": "home_role", "locator": {"home": "Community Caretaking"}, "payload": {"home": "Community Caretaking", "role": "Key — Progeny / Limit", "title": "Graham v. Barnette"}}
{"assertion_id": "7357610d8c7a0e29", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-07-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Graham v. Barnette", "field_i_validity": "good_law", "scope_note": "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs.", "title": "Graham v. Barnette", "varies_by_point": "false"}}
{"assertion_id": "77e3bbe6d201c160", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "Graham v. Barnette"}}
```

### lake record — Graham v. Barnette

```json
{
  "schema_version": "s2.v1",
  "record_id": "Graham v. Barnette",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Teresa Graham v. Shannon Barnette",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Graham v. Barnette",
    "court": "U.S. Court of Appeals, 8th Circuit",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "8th",
    "state": null,
    "date_decided": "2021-07-16",
    "year": 2021,
    "docket": "19-2512",
    "cluster_id": 4900401,
    "lead_opinion_id": 4704180,
    "sibling_ids": [
      4704180
    ],
    "absolute_url": "/opinion/4900401/teresa-graham-v-shannon-barnette/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "5 F.4th 872",
      "volume": "5",
      "reporter": "F.4th",
      "page": "872",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "5 F.4th 872",
        "volume": "5",
        "reporter": "F.4th",
        "page": "872",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "5 F.4th 872",
    "official_selection": {
      "court_class": "coa",
      "selected": "5 F.4th 872",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op10",
      "page": null,
      "quote": "framing supports a warrantless seizure of a person for a mental-health evaluation, and what Fourth Amendment standard governs such a seizure. ## Rule After *Caniglia*, the",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op10a",
      "page": null,
      "quote": "we again conclude that probable cause of dangerousness is the standard that must be met for a warrantless mental-health seizure to be reasonable under the Fourth Amendment.",
      "star_marker": "1",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 21278,
      "fragment": "#:~:text=we%20again%20conclude%20that%20probable",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-op10b",
      "page": null,
      "quote": "[a]t least nine of our sister circuits have held that the Fourth Amendment requires probable cause that a person is mentally ill and dangerous to herself or others for a seizure for an emergency mental-health evaluation to be reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-07-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Graham v. Barnette",
    "varies_by_point": false,
    "scope_note": "Good law; decided on remand from the Supreme Court in light of Caniglia v. Strom. Holds that post-Caniglia the 'community caretaking' label for psychiatric seizures is a category error and that probable cause of dangerousness governs.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Marcus Mitchell v. Kyle Kirchmeier",
          "cluster_id": 6450805,
          "cite": [
            "28 F.4th 888"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher De Rossitte v. Correct Care Solutions, Inc.",
          "cluster_id": 5668863,
          "cite": [
            "22 F.4th 796"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Courtney Saunders v. Kyle Thies",
          "cluster_id": 6619908,
          "cite": [
            "38 F.4th 701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eric Poemoceah v. Morton County",
          "cluster_id": 10124806,
          "cite": [
            "117 F. 4th 1049"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelly Martin v. Jordan Turner",
          "cluster_id": 9415009,
          "cite": [
            "73 F.4th 1007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devin Ledbetter v. B. Helmers",
          "cluster_id": 10372074,
          "cite": [
            "133 F.4th 788"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cory Sessler v. City of Davenport, Iowa",
          "cluster_id": 9506531,
          "cite": [
            "102 F.4th 876"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monica Perkins v. City of Des Moines",
          "cluster_id": 10804290,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyrone Cameron v. City of Des Moines",
          "cluster_id": 10800891,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Teulilo",
          "cluster_id": 10798023,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tara McNeally v. HomeTown Bank",
          "cluster_id": 10706938,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jennifer Harmon v. Second Judicial Circuit of the State of Missouri",
          "cluster_id": 10312599,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dywan Conley",
          "cluster_id": 9404331,
          "cite": [
            "69 F.4th 519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Barnette:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4704180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca8)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      },
      "lane2_top_cited": {
        "query": "cites:(4704180)",
        "reviewed": 13,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 13,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(4704180)",
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
    "complete_query": "cites:(4704180)",
    "indexed_citing_opinions": 13,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4704180,
        "count": 13,
        "count_source": "search"
      }
    ],
    "citation_count": 50,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/graham-v-barnette.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 13,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4704180,
        "cited_id": 89833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 169087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 178217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 197278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 218764,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 288616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 301743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 403636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 580786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 601532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 617079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 620238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 622303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 712235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 738277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 743603,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 786941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 787644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 793704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 794431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 795126,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 797197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 797743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 798058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 799248,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1027858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1274696,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1348291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1378661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1808076,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 1836506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2668794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2670795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2677985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2718042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2801435,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2804087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 2973307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 3194110,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4148210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4155743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4238107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4307201,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4307919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4386310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4525061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4543039,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4556124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4669130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 4687473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 7261027,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 8413948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 8415460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9226038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9420390,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9423752,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9427853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9430599,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9431119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9431589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9434540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9494088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9497489,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9500600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9569092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9799674,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9805636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9811318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9821360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9842136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9873109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4704180,
        "cited_id": 9878125,
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
    "date_created": "2026-07-05T05:49:51Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:51:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:50:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Graham v. Barnette

```
               United States Court of Appeals
                          For the Eighth Circuit
                      ___________________________

                              No. 19-2512
                      ___________________________

                              Teresa M. Graham

                                   Plaintiff - Appellant

                                      v.

Sgt. Shannon L. Barnette; Officer Amanda Sanchez; Officer Mohamed Noor; City
                                 of Minneapolis

                                 Defendants - Appellees
                               ____________

                             State of Minnesota

                                    Amicus Curiae
                               ____________

                   Appeal from United States District Court
                        for the District of Minnesota
                               ____________

                           Submitted: July 12, 2021
                             Filed: July 16, 2021
                                ____________

Before GRUENDER, WOLLMAN, and KOBES, Circuit Judges.
                       ____________

GRUENDER, Circuit Judge.
       Teresa Graham sued Sergeant Shannon Barnette, Officer Mohamed Noor, and
Officer Amanda Sanchez (“the officers”), as well as the City of Minneapolis (“the
City”), under 42 U.S.C. § 1983 and Minnesota state law after the officers entered
her home, seized her, and transported her to a hospital for a mental-health evaluation,
all without a warrant. The district court 1 granted the officers and the City summary
judgment. Graham appealed. We affirmed. Graham v. Barnette, 970 F.3d 1075,
1082 (8th Cir. 2020). The Supreme Court subsequently vacated our judgment and
remanded the case for reconsideration in light of Caniglia v. Strom, 593 U.S. ---, 141
S. Ct. 1596 (2021). Graham v. Barnette, 593 U.S. ---, 2021 WL 2301963, at *1
(U.S. June 7, 2021). We have done so and once again affirm. Our prior opinion in
this case is hereby vacated, and this opinion is substituted for it.

                                          I.

      “We recount the facts of this case in the light most favorable to [Graham], the
non-moving party.” Meehan v. Thompson, 763 F.3d 936, 938 (8th Cir. 2014). In so
doing, we rely on the factual findings of the district court, see Saylor v. Nebraska,
812 F.3d 637, 642 (8th Cir. 2016), as well as audio and video recordings of the
relevant events, see Meehan, 763 F.3d at 938.

       At approximately 10:00 a.m. on May 25, 2017, Graham called 911 and
reported that a man was smoking marijuana on a retaining wall behind her home. A
City police officer arrived at Graham’s address later that morning, saw no one, and
left without following up with Graham. Several hours later, Graham called the
police again and left a voicemail for the precinct’s commander, complaining that
officers did not respond to her emergency call and referencing an email she sent
earlier in the day regarding the police department’s failure to respond to a different
report she had filed. Around 6:00 p.m., a police officer returned Graham’s call and



      1
      The Honorable Joan N. Ericksen, United States District Judge for the District
of Minnesota.

                                         -2-
informed her that officers had investigated her complaint regarding the unidentified
man in her backyard.

      Things then took an unusual turn. At 6:11 p.m., an anonymous informant
claiming to be Graham’s cousin called 911 and reported that Graham had called him
at work to threaten him and his family. He told the 911 operator that “this is not an
emergency” and that he “did not think [Graham] was going to do anything.” Even
so, he requested a “welfare check” because he believed Graham had a history of
mental-health issues. The operator summarized the call for the responding officers
in a comment to the incident report that read, “CLRS COUSIN WHO JUST
CALLED HIM AT WORK AND THREATENED HIM AND HIS FAMILY.” The
operator also noted that the individual requested a welfare check on Graham and that
Graham’s mental-health diagnosis was unknown.

       Two hours later, Officers Noor and Sanchez arrived at Graham’s home.
Officer Sanchez recorded the encounter using a body camera. When Graham
answered the door, she demanded to know who requested the welfare check, claimed
she was being slandered, retrieved her phone to videotape the officers, accused the
police of harassing her because of her earlier complaints, and then demanded that
the officers leave. The officers apologized for disturbing Graham, left her home,
and noted in their incident report that they were unable to “check on her welfare”
because of her insistence that they leave but concluded she “appeared to be AOK.”

      But the interaction between Graham and the police did not end there. At 9:05
p.m., a 911 operator reported that Graham had called three more times since the
welfare check. Graham first called at 8:20 p.m. to complain about what she viewed
as the officers harassing her in retaliation for her previous calls. The operator
described Graham as agitated as well as aggressive and suggested that Graham was
not making sense. Approximately fifteen minutes later, Sergeant Barnette returned
Graham’s call, and the two spoke briefly about Graham’s concerns. At 8:40 p.m.,
Graham called 911 again, asking to be connected to the Edina police department.
Twenty minutes later, she called once more and made the same request.


                                         -3-
       At this time, Sergeant Barnette ordered Officers Noor and Sanchez to take
Graham into custody for an emergency mental-health evaluation as authorized by
Minnesota’s Civil Commitment and Treatment Act (“MCCTA”), Minn. Stat.
§ 253B.05, subd. 2(a) (2017), which permits an officer to seize a person for an
emergency mental-health evaluation “if the officer has reason to believe . . . that the
person is mentally ill . . . and in danger of injuring self or others if not immediately
detained.” In ordering the seizure, Sergeant Barnette relied on the officers’
interactions with Graham throughout the day, the anonymous report that Graham
had threatened her cousin, and Sergeant Barnette’s own previous interactions with
Graham through which Sergeant Barnette claimed to be aware of “some mental
health history” and a history of restraining orders.

      The officers arrived for a second time at Graham’s home at 9:40 p.m. By this
time, one of Graham’s family members—a state police officer—had warned the
Edina police department that Graham may fight with police, and Sergeant Barnette
decided to join Officers Noor and Sanchez at Graham’s home. The officers wore
body cameras that recorded the encounter.

       When the officers arrived, Graham opened the interior front door but left her
storm door locked and shut. Graham appeared angry, told the officers that she did
not call them for help, demanded that they leave her property, and slammed the front
door. Sergeant Barnette then removed the screen from the storm door to allow entry
should Graham reopen the interior door. With the interior door closed, Graham told
the officers she was fine. She then called 911 to complain that the officers would
not leave. After an extended discussion with the officers through the door, Graham
reopened the door, at which point the officers entered her home through the then-
screenless storm door and held Graham by each arm. During the encounter in her
home, Graham did not resist or threaten the officers, but she did criticize them and
threaten to sue them, alleging they were kidnapping her because of her complaints.

      After several minutes, the officers placed Graham in an ambulance, noting in
the relevant paperwork that they took Graham into custody because she


                                          -4-
“continuously called 911 and per dispatchers was verbally agitated and not making
sense.” Graham was then transported to Southdale Fairview Hospital, where she
was evaluated and subsequently discharged after an examination demonstrated that,
while she exhibited “some paranoid behavior” and was “royally pissed,” she was
“somewhat rational” and, according to the examining physician, not “hold-able.”

      Graham brought suit, asserting (as relevant here) claims under 42 U.S.C.
§ 1983 on the basis that the officers violated her Fourth Amendment rights by
conducting an unreasonable search and seizure and that they violated her First
Amendment rights by arresting her in retaliation for protected speech. 2 She also
brought § 1983 claims against the City under Monell v. Department of Social
Services, 436 U.S. 658, 690 (1978), alleging that the City’s policy regarding seizures
for emergency mental-health evaluations caused the officers’ unconstitutional
conduct and that the City’s failure to train the officers resulted in their
unconstitutional conduct. Finally, Graham brought Minnesota state-law claims
against the officers for false imprisonment, battery, assault, and negligence.

       The district court entered summary judgment in favor of the officers, granting
them qualified immunity on Graham’s Fourth Amendment claims, finding that
Graham had not established a triable issue of fact regarding her retaliatory-arrest
claim, and granting the officers statutory and official immunity on Graham’s state-
law claims. The district court also entered summary judgment in favor of the City,
determining that the City’s policy concerning seizures for emergency mental-health
evaluations was not facially unconstitutional and that Graham did not plead facts
sufficient to support a claim for failure to train.

     Graham appealed. We previously affirmed the district court’s judgment. See
Graham, 970 F.3d at 1082. Graham then petitioned for a writ of certiorari, arguing

      2
       Graham also raised claims of excessive force, property damage, and
conspiracy before the district court, but she did not raise them on appeal and has thus
abandoned them. See Griffith v. City of Des Moines, 387 F.3d 733, 739 (8th Cir.
2004).

                                         -5-
(as relevant here) that the doctrine we relied on to find that the officers’ warrantless
entry was reasonable under the Fourth Amendment—the so-called community-
caretaking or community-caretaker exception—did not apply to the home. 3 While
Graham’s petition was pending, the Supreme Court decided Caniglia, where it
explained that this “exception” is not actually a “standalone doctrine that justifies
warrantless searches and seizures in the home.” 141 S. Ct. at 1598. Subsequently,
it granted Graham’s certiorari petition, vacated our prior judgment in Graham’s
appeal, and remanded the matter to us for further consideration in light of Caniglia.
Graham, 2021 WL 2301963, at *1. We have reconsidered this appeal in light of
Caniglia, and we once again affirm the district court’s judgment.

                                          II.

       We first consider the district court’s grant of summary judgment to the officers
and the City on Graham’s § 1983 claims. “We review the district court’s grant of
summary judgment and qualified immunity rulings de novo.” Samuelson v. City of
New Ulm, 455 F.3d 871, 875 (8th Cir. 2006). Summary judgment is proper if, when
viewing the facts in the light most favorable to the nonmoving party, see Mullenix
v. Luna, 577 U.S. ---, 136 S. Ct. 305, 307 (2015) (per curiam), “the movant shows
that there is no genuine dispute as to any material fact and the movant is entitled to
judgment as a matter of law,” Fed. R. Civ. P. 56(a). A genuine dispute exists “if the
evidence is such that a reasonable jury could return a verdict for the nonmoving
party.” Anderson v. Liberty Lobby, Inc., 477 U.S. 242, 248 (1986).




      3
       As she did before us, Graham also argued in her certiorari petition that the
doctrine of qualified immunity should be modified or “overruled.” This argument
remains foreclosed by Supreme Court and Eighth Circuit precedent. See, e.g., White
v. Pauly, 580 U.S. ---, 137 S. Ct. 548, 551 (2017) (per curiam); Lane v. Nading, 927
F.3d 1018, 1022 (8th Cir. 2019).

                                          -6-
                                        A.

       Graham first argues that the officers violated her clearly established Fourth
Amendment right to be free from an unreasonable search by entering her home. Pre-
Caniglia, the officers responded that their warrantless entry into her home was
reasonable under the community-caretaking exception but that, even if it was not,
they were entitled to qualified immunity as to this claim because it was not clearly
established that their actions were unreasonable in the circumstances.

       A law-enforcement officer is entitled to qualified immunity unless “(1) the
facts, viewed in the light most favorable to the plaintiff, demonstrate the deprivation
of a constitutional or statutory right; and (2) the right was clearly established at the
time of the deprivation.” Walton v. Dawson, 752 F.3d 1109, 1116 (8th Cir. 2014).
Due to the “dearth of community caretaking cases,” the district court bypassed the
first prong of the analysis, see Reichle v. Howards, 566 U.S. 658, 664 (2012),
concluding instead that the law was not clearly established that the officers violated
Graham’s Fourth Amendment rights by entering her home without a warrant
pursuant to the community-caretaking exception. Previously, we opted to affirm
under the first prong, see, e.g., Greenman v. Jessen, 787 F.3d 882, 887 & n.10 (8th
Cir. 2015), concluding that the officers’ warrantless entry was sufficiently justified
and thus reasonable under the community-caretaking exception, Graham, 970 F.3d
at 1084-86. But Caniglia rendered our prior rationale untenable insofar as it
explained that “community caretaking” was not a “standalone doctrine” that could
justify warrantless entry into the home. See 141 S. Ct. at 1598. Accordingly, we
now affirm the district court’s grant of summary judgment under the second prong
of the qualified-immunity analysis.

       For purposes of the second prong, we look to “the legal rules that were clearly
established at the time” the action at issue was taken. Davis v. Hall, 375 F.3d 703,
711 (8th Cir. 2004) (internal quotation marks omitted); see also Anderson v.
Creighton, 483 U.S. 635, 640 (1987) (noting that this analysis turns on whether the
unlawfulness of the official’s actions was apparent “in the light of pre-existing law”).


                                          -7-
In other words, this inquiry “does not take into account later . . . changes in the law.”
Jackson v. Humphrey, 776 F.3d 1232, 1242 (11th Cir. 2015).

       On May 25, 2017, it was well established in this circuit that the community-
caretaking exception was a standalone doctrine that alone could justify warrantless
entry into a home. See, e.g., United States v. Smith, 820 F.3d 356, 360 (8th Cir.
2016); Burke v. Sullivan, 677 F.3d 367, 372 (8th Cir. 2012); United States v.
Quezada, 448 F.3d 1005, 1007 (8th Cir. 2006). And, in the circumstances present
here, the officers’ warrantless entry did not violate Graham’s Fourth Amendment
rights under our then-extant community-caretaking jurisprudence. As we previously
explained:

      Affording the officers “substantial latitude in interpreting and drawing
      inferences from factual circumstances,” United States v. Washington,
      109 F.3d 459, 465 (8th Cir. 1997), we . . . conclude that the warrantless
      entry into Graham’s home was justified by a reasonable belief that
      Graham was experiencing a mental health emergency and might harm
      herself or others if not detained, see Quezada, 448 F.3d at 1007. The
      officers could reasonably believe that Graham had recently made some
      sort of threat to her cousin; she had called 911 five times that day and
      three times within two hours; and the operator had noted that she was
      “not making sense” and that each time she was argumentative,
      uncooperative, and agitated; Sergeant Barnette knew Graham had a
      history of restraining orders; and a second member of Graham’s family
      warned the police department that she may fight the officers. When the
      officers arrived at her home the second time, Graham was agitated and
      refused to talk with them. She initially stated that she had not called
      the police—even though Sergeant Barnette identified herself and
      explained that she and Graham had spoken shortly before. When the
      officers tried to enter, Graham slammed the door and called 911 again
      even as the officers attempted to explain, as one officer put it, “we are
      911.”

      “When viewed collectively, these facts could lead a reasonable police
      officer to conclude there was either a threat of violence or an emergency
      requiring attention.” Burke[, 677 F.3d at 372]. . . .



                                          -8-
      Finally, once inside the home, the officers did not expand the scope of
      their search beyond that which was justified by the emergency. “The
      justification for the officers’ entry ar[ose] from their obligation to help
      those in danger and ensure the safety of the public,” and the officers
      “carefully tailored” “the scope of the encounter” so as to “satisfy th[at]
      purpose.” Smith, 820 F.3d at 361-62. Upon entry, they immediately
      located Graham, secured her person so she could not harm herself or
      anyone else, and limited their entry to this purpose rather than, say,
      searching throughout the rest of her home or rummaging through her
      belongings. See id. (explaining that the scope of the entry and search
      in the emergency-aid context must be limited to determining whether
      an emergency exists).

      The officers thus acted reasonably when entering Graham’s home.

Graham, 970 F.3d at 1085-86.

       We need not and do not unpack today Caniglia’s full ramifications for our
community-caretaking jurisprudence. Cf. Caniglia, 141 S. Ct. at 1603 (Kavanaugh,
J., concurring) (noting that the “Fourth Amendment issue” presented by warrantless
home entries done for noninvestigatory, “community caretaking” purposes is “more
labeling than substance”). Rather, we decide only that the officers’ warrantless entry
was reasonable under “the legal rules that were clearly established” in this circuit on
May 25, 2017. See Davis, 375 F.3d at 711 (internal quotation marks omitted). While
Caniglia made clear that “community caretaking” was not its own Fourth
Amendment exception that alone could justify warrantless entry into the home,
“Caniglia did not address” what “rights were clearly established” under “pre-
existing circuit law.” Luer v. Cnty. of St. Louis, --- F.4th ---, 2021 WL 2285499, at
*1 (8th Cir. June 3, 2021). Accordingly, we affirm the district court’s grant of
summary judgment on the basis of qualified immunity to the officers with respect to
Graham’s Fourth Amendment warrantless-entry claim.




                                         -9-
                                          B.

        Graham next contends that the officers violated her Fourth Amendment right
to be free from unreasonable seizures when they seized her for a mental-health
evaluation without probable cause to believe that she was a danger to herself or
others. She also argues that probable cause was the clearly established standard at
the time, meaning the officers are not entitled to qualified immunity as to this claim.
Alternatively, she argues that even if this circuit’s standard for evaluating mental-
health seizures is a lower, “reasonable belief” standard, the officers still lacked such
justification to seize her for a mental-health evaluation under clearly established law
and thus should not be granted qualified immunity even under this lower standard.

       Although the district court agreed with Graham that the officers needed
probable cause of dangerousness to seize her for a mental-health evaluation and
lacked such probable cause, it found that the probable-cause standard was not clearly
established. Accordingly, the district court granted the officers qualified immunity
as to this claim. On appeal, the officers (joined by the State of Minnesota as amicus
curiae) contended that, under circuit precedent, the officers needed only reasonable
belief of dangerousness to seize her, and the officers argued that they had such
reasonable belief here. The officers also argued that they were entitled to qualified
immunity as to this claim because their seizure of Graham did not violate clearly
established law.

      Previously, we agreed with the district court that, although our case law had
engendered some confusion about the proper standard, “only probable cause that a
person poses an emergent danger . . . to herself or others” could justify a warrantless
mental-health seizure. Graham, 970 F.3d at 1088-89. But, given the ambiguity in
our case law about this issue, we held that, even if the officers lacked the requisite
probable cause, they could still be entitled to qualified immunity because the
probable-cause standard was not clearly established. Id. at 1090. And we ultimately
concluded that the officers were entitled to qualified immunity because their actions



                                         -10-
did not violate clearly established law under the lower reasonable-belief standard
that some of our precedents had suggested applied here. Id. at 1090-91.

       In our prior discussion of this issue, we used the “community caretaking” label
to discuss the standard under which warrantless mental-health seizures are
permissible under the Fourth Amendment. Id. at 1088. Now that Caniglia has made
clear that “there is no overarching ‘community caretaking’ doctrine,” 141 S. Ct. at
1600 (Alito, J., concurring), our use of that label seems to be a category error. That
said, the Court in Caniglia “refrain[ed]” from addressing generally the standards
governing “emergency seizures for psychiatric treatment, observation, or
stabilization.” Id. at 1601 (Alito, J., concurring). Thus, Caniglia did not affect the
substance of our reasoning or holdings on the issues Graham raises regarding her
warrantless seizure. Accordingly, we once again conclude that (1) probable cause
of dangerousness is the requisite standard; (2) assuming the officers lacked probable
cause here, they may still be entitled to qualified immunity given the ambiguity in
our case law about the requisite standard; and (3) the officers are entitled to qualified
immunity because their actions did not violate clearly established law under the
lower reasonable-belief standard some of our precedents suggested was the requisite
standard.

                                           1.

      First, we again conclude that probable cause of dangerousness is the standard
that must be met for a warrantless mental-health seizure to be reasonable under the
Fourth Amendment.

       At least nine of our sister circuits have held that the Fourth Amendment
requires probable cause that a person is mentally ill and dangerous to herself or
others for a seizure for an emergency mental-health evaluation to be reasonable. See,
e.g., Myers v. Patterson, 819 F.3d 625, 632 (2d Cir. 2016); Cantrell v. City of
Murphy, 666 F.3d 911, 923 (5th Cir. 2012); Roberts v. Spielman, 643 F.3d 899, 905
(11th Cir. 2011); Cloaninger ex rel. Estate of Cloaninger v. McDevitt, 555 F.3d 324,


                                          -11-
334 (4th Cir. 2009); Meyer v. Bd. of Cnty. Comm’rs of Harper Cnty., 482 F.3d 1232,
1239 (10th Cir. 2007); Ahern v. O’Donnell, 109 F.3d 809, 817 (1st Cir. 1997);
Monday v. Oullette, 118 F.3d 1099, 1102 (6th Cir. 1997); Sherman v. Four Cnty.
Counseling Ctr., 987 F.2d 397, 401-02 (7th Cir. 1993); Maag v. Wessler, 960 F.2d
773, 775-76 (9th Cir. 1991) (per curiam); see also Cole v. Town of Morristown, 627
F. App’x 102, 106-07 (3d Cir. 2015) (upholding as reasonable a mental-health
seizure because “the police . . . had probable cause to believe” the plaintiff “was
dangerous”); In re Barnard, 455 F.2d 1370, 1373-74 (D.C. Cir. 1971) (finding that
a plaintiff was seized within the meaning of the Fourth Amendment when taken into
custody for an involuntary mental-health evaluation and explaining that such
seizures are unconstitutional “unless supported by probable cause”). These courts
have uniformly determined that “a seizure of a person for an emergency mental
health evaluation raises concerns that are closely analogous to those implicated by a
criminal arrest, and both are equally intrusive.” See Pino v. Higgs, 75 F.3d 1461,
1468 (10th Cir. 1996).

       Some of these circuits have thought we were first movers in this area, pointing
to Harris v. Pirch, 677 F.2d 681 (8th Cir. 1982), while holding that the right to be
free from seizures for an emergency mental-health evaluation without probable
cause of dangerousness was clearly established. See, e.g., Maag, 960 F.2d at 776.
But neither Pirch nor our later cases are so clear. In Pirch, we determined that an
officer was entitled to qualified immunity after effectuating a mental-health seizure,
and in so doing we commented that “when a court evaluates police conduct relating
to an arrest its guideline is good faith and probable cause.” 677 F.2d at 686 (brackets
omitted). But, because we were evaluating whether an officer complied with a
Missouri statute that used the phrase “reasonable cause,” id. at 684, we held that the
officer was immune from suit because he acted in “good faith and had reasonable
cause” to believe the plaintiff overdosed without explaining whether reasonable
cause was as rigorous a standard as probable cause, id. at 689. Compare Navarette
v. California, 572 U.S. 393, 404 (2014) (using “reasonable cause” and “reasonable
suspicion” interchangeably to justify an investigative stop), with Stacey v. Emery,
97 U.S. 642, 646 (1878) (“If there was a probable cause of seizure, there was a


                                         -12-
reasonable cause. If there was a reasonable cause of seizure, there was a probable
cause.”).

       Since Pirch, we have never held that reasonable belief is sufficient, nor have
we held that probable cause is required, to justify a mental-health seizure. We have
instead suggested that reasonable belief is sufficient to justify some noninvestigatory
seizures while intimating that probable cause is required in other instances.4
Compare Winters v. Adams, 254 F.3d 758, 764, 766 (8th Cir. 2001) (upholding a
brief detention of an intoxicated individual under the community-caretaking
exception and analogizing the officers’ decision to “investigate” and “briefly detain”
to investigative stops), Samuelson, 455 F.3d at 874 (finding “objectively reasonable”
the officers’ decision to transport the plaintiff to a hospital for evaluation due to his
“incoherent” statements after he was mistakenly arrested and in police custody for
breaking into his own garage), and Burke, 677 F.3d at 372-73 (stating that a “brief
detention” based on reasonable belief that it was necessary to secure the safety of an
individual “was lawful”), with Meehan, 763 F.3d at 943 (articulating a
reasonableness balancing test under the community-caretaking exception but
framing the ultimate question as one concerning whether the facts at issue gave the
officer acting “in his capacity as community caretaker” “probable cause to arrest”
the individual), and United States v. Harris, 747 F.3d 1013, 1017, 1019 (8th Cir.
2014) (same).



      4
       Amicus Minnesota argues that we rejected the probable-cause standard for
emergency mental-health seizures in Collins v. Bellinghausen, 153 F.3d 591, 596
(8th Cir. 1998), but this is not so. Instead, when evaluating the plaintiff’s Fourth
Amendment claim, we held that officers acted reasonably when they entered a home
to seize a vulnerable adult that the officers “reasonably believe[d]” needed
immediate aid. Id. And, in the context of evaluating the plaintiff’s claim that the
defendants violated her Fourteenth Amendment right to due process, we stated that
the “probable cause” requirement necessary to justify the initiation of involuntary
commitment proceedings under Iowa law was “irrelevant” to our analysis of what
the Due Process Clause demands—an issue itself distinct from what the Fourth
Amendment requires. See id.

                                          -13-
       We think the through line of these cases is straightforward. As in the criminal
context of an investigative stop, when officers act in a noninvestigatory capacity,
they may briefly detain an individual to ensure her safety and that of the officers or
the public when the officer reasonably believes that an emergency exists requiring
the officer’s attention. But, as with other police functions, all seizures—whether
brief detentions or arrests—done for noninvestigatory purposes are governed by the
Fourth Amendment’s reasonableness balancing test. As a result, the greater the
intrusion on a citizen, the greater the justification required for that intrusion to be
reasonable. Thus, if the detention evolves into an arrest, it must be justified by
probable cause. This balancing test, ever attuned to the nature and quality of the
intrusion, comports with the Supreme Court’s instruction that reasonableness is the
touchstone of the Fourth Amendment. See Smith, 820 F.3d at 360-62 (articulating a
similar rule in the context of community-caretaking searches).

        Our decision in Harris illustrates this point. There, we stated that a “seizure
of a person by a police officer acting in the officer’s noninvestigatory capacity is
reasonable if the governmental interest in the police officer’s exercise of [the
officer’s] community caretaking function, based on specific articulable facts,
outweighs the individual’s interest in being free from arbitrary government
interference.” 747 F.3d at 1017 (internal quotation marks omitted). But we also
explained that even when an officer is operating in a noninvestigatory capacity,
“[t]he scope of [an] encounter must be carefully tailored to satisfy the purpose of the
initial detention, and the police must allow the person to proceed once the officer
has completed the officer’s inquiry, unless, of course, the officer obtains further
reason to justify the stop.” Id. We continued to analyze the initial encounter and
brief detention under the standard of reasonable belief, which we analogized to the
standard required for a Terry stop, but we concluded that the later arrest of the
individual was reasonable because, in the course of the encounter, the officers
developed probable cause. Id. at 1019; see also Terry v. Ohio, 392 U.S. 1, 13 (1969)
(“Encounters are initiated by the police for a wide variety of purposes, some of which
are wholly unrelated to a desire to prosecute for crime.”).



                                         -14-
       Accordingly, we now make explicit that which has long been implicit in our
case law and align our circuit with the unanimous consensus in all other circuits. We
conclude that only probable cause that a person poses an emergent danger—that is,
one calling for prompt action—to herself or others can tip the scales of the Fourth
Amendment’s reasonableness balancing test in favor of the government when it
arrests an individual for a mental-health evaluation because only probable cause
constitutes a sufficient “governmental interest” to outweigh a person’s “interest in
freedom.”5 See Harris, 747 F.3d at 1017; Dunaway v. New York, 442 U.S. 200, 208
(1979) (“The long-prevailing standards of probable cause embod[y] the best
compromise that has been found for accommodating the often opposing interests in
safeguarding citizens from rash and unreasonable interferences with privacy and in
seeking to give fair leeway for enforcing the law in the community’s protection.”
(internal quotation marks and brackets omitted)). Officers have probable cause to
arrest a person for a mental-health evaluation when “the facts and circumstances
within . . . the officers’ knowledge and of which they had reasonably trustworthy
information are sufficient . . . to warrant a man of reasonable caution” to believe that
the person poses an emergent danger to himself or others. Cf. Baribeau v. City of
Minneapolis, 596 F.3d 465, 474 (8th Cir. 2010) (quoting Brinegar v. United States,
338 U.S. 160, 175 (1949)); Cantrell, 666 F.3d at 923 (articulating a similar
standard); Cloaninger, 555 F.3d at 334 (same).

       Our confidence that the Fourth Amendment demands probable cause of
dangerousness to effectuate a mental-health arrest in this case is reinforced by the
location of this arrest: Graham’s home. As the Supreme Court has emphasized, “the
right of a man to retreat into his own home and there be free from unreasonable
government intrusion stands at the very core of the Fourth Amendment.” Groh v.
Ramirez, 540 U.S. 551, 559 (2004) (internal quotation marks and brackets omitted).

      5
       Of course, we do not mean arrest in the traditional criminal sense. Instead,
we agree with our sister circuits that taking a person into custody for an emergency
mental-health evaluation “raises concerns that are closely analogous to those
implicated by a criminal arrest, and both are equally intrusive.” See Pino, 75 F.3d
at 1468.

                                         -15-
For this reason, the Court has “drawn a firm line at the entrance to the house,” and
absent a warrant or probable cause and exigent circumstances, police may not seize
a person in her home. Payton v. New York, 445 U.S. 573, 590 (1980).

                                           2.

       Second, we again conclude that the probable-cause standard was not clearly
established in our jurisprudence, meaning the officers may still be entitled to
qualified immunity even if they seized Graham without probable cause of
dangerousness.

       “To be clearly established, a legal principle must have a sufficiently clear
foundation in then-existing precedent.” See District of Columbia v. Wesby, 583 U.S.
---, 138 S. Ct. 577, 589 (2018). This generally requires a plaintiff to “point to
existing circuit precedent that involves sufficiently ‘similar facts’ to ‘squarely
govern’” the officers’ conduct in the specific circumstances at issue, see Boudoin v.
Harsson, 962 F.3d 1034, 1040 (8th Cir. 2020) (brackets omitted), or, in the absence
of binding precedent, to present “a robust consensus of cases of persuasive
authority” constituting settled law, see De La Rosa v. White, 852 F.3d 740, 745 (8th
Cir. 2017). The plaintiff has the burden to prove that a right was clearly established
at the time of the alleged violation. Wilson v. Lamp, 901 F.3d 981, 986 (8th Cir.
2018).

       Here, Graham cannot point to existing Eighth Circuit precedent that clearly
establishes the probable-cause standard because of the ambiguity in our case law
highlighted above. Indeed, in her briefing, Graham conceded as much, arguing that
Pirch clearly established the standard of probable cause but noting that our case law
“does create confusion.” And during oral argument, Graham’s counsel specifically
asked this court to “make clear” that probable cause is required in this circuit because
“there hasn’t been a case that has directly stated what the requirement is for a mental
health hold.” A right is not clearly established by “controlling authority” merely



                                         -16-
because it may be “suggested by then-existing precedent.” See Wesby, 138 S. Ct. at
589-90.

       Neither is this an instance in which every reasonable officer would have
known that his conduct was unlawful due to a robust consensus of authority from
other circuits. Though, at the time the officers seized Graham, several other circuits
had determined that probable cause was the constitutional standard required to
justify a mental-health arrest, our case law was not merely silent on the issue;
instead, we had created ambiguity concerning the answer, suggesting that reasonable
belief might be sufficient to satisfy the demands of the Fourth Amendment. See
Lane v. Franks, 573 U.S. 228, 243-46 (2014) (concluding that an official was entitled
to qualified immunity because, although decisions from other circuits took one side
of an intracircuit debate, the intracircuit panel decisions conflicted). “No matter how
carefully a reasonable officer read” our precedent “beforehand, that officer could not
know that” the conduct at issue would violate our circuit’s “test.” See City & Cnty.
of San Francisco v. Sheehan, 575 U.S. 600, 616 (2015). This determination is
enough to resolve this issue as the officers are entitled to qualified immunity unless
the right is established “beyond debate.” See Ashcroft v. al-Kidd, 563 U.S. 731, 741
(2011).

                                          3.

      Third, we again conclude that the officers are entitled to qualified immunity
because their actions did not violate clearly established law under the more lenient
reasonable-belief standard that some of our precedents had suggested was the
requisite standard governing warrantless mental-health seizures.

       Graham contends that even if the probable-cause standard was not clearly
established, no reasonable officer could have believed that it was lawful to seize her
because the facts known to the officers after they entered her home did not support
even the lower standard of reasonable belief that she presented an emergent danger
to herself or others. We disagree. We do not think that only a “plainly incompetent”


                                         -17-
officer could conclude he had arguable reasonable belief. See Mullenix, 136 S. Ct.
at 308; Waters v. Madson, 921 F.3d 725, 736 (8th Cir. 2019) (explaining that even
if officers lack reasonable suspicion for an investigative stop, they are entitled to
qualified immunity if they had arguable reasonable suspicion).

       Reasonable belief “is a less exacting standard than probable cause,” Quezada,
448 F.3d at 1007, and, to be reasonable, an officer’s belief must be supported by
specific, articulable facts, see United States v. Sanders, 956 F.3d 534, 539 (8th Cir.
2020). Here, the officers believed that Graham had threatened a family member,
and a second family member warned she might fight the officers; Graham called 911
repeatedly over the previous two hours, and the operator reported that her calls were
nonsensical; Graham denied calling the police when the officers arrived; and
Graham appeared confused as to why the officers were at her home. Although
Graham maintained that she was not a threat to herself or others, the officers were
not required to believe her, particularly considering her agitated state and the prior
reports of threats.

       Thus, at the very least, the facts known to the officers at the time were
sufficient to support arguable reasonable belief that Graham was experiencing a
mental-health crisis and presented an emergent danger to herself or others. Cf.
Ryburn v. Huff, 565 U.S. 469, 476-77 (2012) (“[I]t is a matter of common sense that
a combination of events each of which is mundane when viewed in isolation may
paint an alarming picture.”). Graham has offered no precedent that squarely governs
these facts such that, when considering the officers’ “observations as a whole,”
Waters, 921 F.3d at 736, every reasonable officer would have known that he lacked
a reasonable belief that Graham was an emergent danger to herself or others, see
Wesby, 138 S. Ct. at 590 (explaining that, for the law to be clearly established, a
reasonable officer must be able to interpret precedent “to establish the particular rule
the plaintiff seeks to apply” and to determine that such “legal principle clearly
prohibit[s] the officer’s conduct in the particular circumstances before him”).




                                         -18-
                                     *      *      *

       The “principle at the heart” of the clearly established requirement is that “state
actors are liable only for transgressing bright lines, not for making bad guesses in
gray areas.” L.G. ex rel. M.G. v. Columbia Pub. Schs., 990 F.3d 1145, 1148 (8th
Cir. 2021). For the foregoing reasons, we conclude that, in warrantlessly seizing
Graham for a mental-health evaluation, the officers may have made a bad guess in a
gray area, but they did not transgress any “bright lines” so as to lose the protection
of qualified immunity. Accordingly, we affirm the district court’s grant of qualified
immunity to the officers regarding Graham’s warrantless-seizure claim.

                                           C.

       Graham next claims that the district court erred in granting summary judgment
to the officers on Graham’s claim of retaliatory arrest because, according to Graham,
she presented sufficient evidence of retaliatory intent to create a triable issue of fact.
We disagree.

       “[T]he law is settled that as a general matter the First Amendment prohibits
government officials from subjecting an individual to retaliatory actions . . . for
speaking out.” Hoyland v. McMenomy, 869 F.3d 644, 655 (8th Cir. 2017). To
establish a First Amendment retaliatory-arrest claim, a plaintiff must show that
(1) she engaged in protected activity, (2) a government official took an adverse
action against her that would chill a person of ordinary firmness from continuing in
the activity, (3) the adverse action was caused by the exercise of the protected
activity, and (4) the government official lacked probable cause or arguable probable
cause. Peterson v. Kopp, 754 F.3d 594, 602 (8th Cir. 2014).

       To survive summary judgment, a plaintiff must show that a reasonable jury
could find that a retaliatory motive of the government official was a “but-for cause”
of the adverse action, “meaning that the adverse action against the plaintiff would
not have been taken absent the retaliatory motive.” Nieves v. Bartlett, 587 U.S. ---,


                                          -19-
139 S. Ct. 1715, 1722 (2019) (“It is not enough to show that an official acted with a
retaliatory motive and that the plaintiff was injured—the motive must cause the
injury.”). “The causal connection is generally a jury question, but it can provide a
basis for summary judgment when the question is so free from doubt as to justify
taking it from the jury.” Revels v. Vincenz, 382 F.3d 870, 876 (8th Cir. 2004)
(internal quotation marks omitted).

       For instance, in Baribeau, we denied officers qualified immunity on a claim
of unreasonable seizure when they arrested and detained protestors without arguable
probable cause to believe the protestors either engaged in disorderly conduct or
displayed a simulated bomb. 596 F.3d at 481. Even so, we granted the officers
summary judgment on the plaintiffs’ retaliatory-arrest claim because no “reasonable
jury could find that retaliatory animus was a . . . ‘but-for’ cause” of the arrests where
the evidence demonstrated that the officers made the arrest after observing a young
girl become frightened by the plaintiffs’ appearance, and because the evidence
demonstrated that the decision to arrest the plaintiffs was “based on an actual but
overly exaggerated belief that the plaintiffs violated the WMD statute.” Id.

       Given the information available to the officers in this case, we likewise
determine that no reasonable jury could conclude that retaliatory animus was a but-
for cause of Graham’s arrest. As in Baribeau, there is no evidence that the officers’
actions were based on anything other than perhaps “an actual but overly exaggerated
belief” that Graham was experiencing a mental-health emergency and presented a
threat either to herself or to others. And though the temporal proximity of Graham’s
protected activity and her subsequent arrest is relevant, it is not enough on its own
to create a triable issue of fact regarding cause where no other record evidence
supports finding a retaliatory motive and there is evidence that the officers acted in
good faith. See Wilson v. Northcutt, 441 F.3d 586, 592 (8th Cir. 2006) (“Temporal
proximity is relevant but not dispositive.”); see also Williams v. City of Carl
Junction, 480 F.3d 871, 877-78 (8th Cir. 2007) (holding that the plaintiff had not
demonstrated retaliatory animus sufficient to support a retaliatory-prosecution claim
under the First Amendment where he “presented no evidence”—other than the


                                          -20-
traffic ticket itself—“that the officer who issued [the] citation harbored any
retaliatory animus against him”).

     Thus, the district court properly granted the officers summary judgment on
Graham’s retaliatory-arrest claim.

                                          D.

       Graham next contends that the City’s policy concerning seizures for an
emergency mental-health evaluation caused the officers to violate her Fourth
Amendment rights because the policy was facially unconstitutional. In the
alternative, Graham argues that the City should be liable because it was
deliberatively indifferent to her constitutional rights and failed to train the officers
properly. We conclude that the district court did not err in granting the City
summary judgment.

       “A municipality may be liable under § 1983 where ‘action pursuant to official
municipal policy of some nature caused a constitutional tort.’” Hollingsworth v. City
of St. Ann, 800 F.3d 985, 991-92 (8th Cir. 2015) (quoting Monell, 436 U.S. at 691).
When a city’s policy is facially unconstitutional, we have recognized that “resolving
[the] issues of fault and causation is straightforward.” Szabla v. City of Brooklyn
Park, 486 F.3d 385, 389-90 (8th Cir. 2007) (en banc). In that instance, “[t]o establish
a constitutional violation, no evidence is needed other than a statement of the
municipal policy and its exercise.” Id.

       The relevant portion of the MCCTA provides that an officer may seize a
person for an emergency mental-health evaluation and transport that person to “a
licensed physician or treatment facility if the officer has reason to believe . . . that
the person is mentally ill . . . and in danger of injuring self or others if not
immediately detained.” Minn. Stat. § 253B.05, subd. 2(a) (emphasis added). In
compliance with the statute, the City’s policy allows an officer to take a person with
mental illness into custody “if there is a reason to believe the person poses a threat


                                         -21-
to himself or others.” The policy further directs that “[t]he threat does not have to
be imminent.”

       The district court initially denied the City summary judgment, determining
that the phrase “reason to believe” was inconsistent with the Fourth Amendment’s
probable-cause requirement for a mental-health seizure. After the City filed a
motion for reconsideration, the district court determined that it had “made a manifest
error of law” by failing to construe the phrase “reason to believe” to require probable
cause.

       We agree that the policy is not facially unconstitutional. First, “reason to
believe” is commonly used to mean probable cause. For instance, in United States
v. Quintana, we analyzed the meaning of the phrase “reason to believe” in a federal
immigration statute relating to arrests of undocumented aliens and concluded that
the phrase means “constitutionally required probable cause.” 623 F.3d 1237, 1239
(8th Cir. 2010); see also United States v. Stead, 422 F.2d 183, 184 n.1 (8th Cir. 1970)
(per curiam) (“Probable cause exists since a prudent man would have had reason to
believe that this defendant had committed a felony.”). Other circuits have come to
similar conclusions when interpreting statutes governing mental-health seizures. In
Cantrell, for example, the Fifth Circuit interpreted the Texas Health and Safety
Code’s use of “reason to believe” to require probable cause. 666 F.3d at 923.

       Second, the policy’s language stating that the threat presented “does not have
to be imminent” does not make the policy facially unconstitutional. To be sure, a
mental-health seizure must be justified by probable cause that the person subject to
the arrest presents an emergent threat of harm to herself or others, but government
officials need not wait to intervene until an individual is a split second away from
harming herself or others. See Meyers v. Comm’r of Soc. Sec. Admin., 801 F. App’x
90, 95 (4th Cir. 2020) (per curiam) (“‘Imminent’ means ‘threatening to occur
immediately; dangerously impending’ or ‘[a]bout to take place.’” (quoting Black’s
Law Dictionary (11th ed. 2019)); United States v. Hardeman, 449 F. App’x 408, 410
(5th Cir. 2011) (per curiam) (defining imminent as “impending; on the point of


                                         -22-
happening”). The Fourth Amendment does not demand that police wait until a
suicidal citizen has raised a gun to her temple before officers may intervene. See
Caniglia, 141 S. Ct. at 1604 (Kavanaugh, J., concurring) (explaining that “the
Court’s exigency precedents” do not require that the harm be “mere moments
away”). Instead, it requires only that a prudent person would have reason to believe
that the individual subject to the seizure presents a threat to herself or others such
that an order of a court or other authority cannot be obtained in time to prevent the
anticipated harm or injury. See Michigan v. Tyler, 436 U.S. 499, 509 (1978)
(explaining that police may rely on the exigent-circumstances or emergency-aid
exceptions when “there is compelling need for official action and no time to secure
a warrant”); Caniglia, 141 S. Ct. at 1602 (Alito, J., concurring) (noting that
circumstances are “exigent” when “there is not enough time to get a warrant”). As
a result, the policy is not facially unconstitutional because it does “not affirmatively
sanction” an unconstitutional action. See Szabla, 486 F.3d at 392.

       Where an official policy is lawful on its face, a plaintiff nevertheless may
establish liability by showing that a municipality caused the constitutional violation
by providing “inadequate training” for its employees. Parrish v. Ball, 594 F.3d 993,
997 (8th Cir. 2010). To establish such liability, a plaintiff must show that (1) the
municipality’s “training practices [were] inadequate,” (2) the municipality was
“deliberately indifferent” to the plaintiff’s rights when adopting the training
practices such that the “failure to train reflects a deliberate or conscious choice,” and
(3) the plaintiff’s injury was “actually caused” by the “alleged deficiency” in the
training practices. Id.

        Graham has not met this standard for two reasons. First, she advances no
evidence concerning other mental-health seizures, so she has not shown a history of
the City’s officers committing unreasonable seizures such that the need for
additional training was plain. See Bd. of Cnty. Comm’rs of Bryan Cnty. v. Brown,
520 U.S. 397, 407-08 (1997). The Supreme Court has held that a “pattern of similar
constitutional violations” is “ordinarily necessary” to establish municipal
liability, Connick v. Thompson, 563 U.S. 51, 62 (2011), unless “the need for more


                                          -23-
or different training is so obvious and the inadequacy [is] so likely to result in the
violation of constitutional rights” that the municipality can be said to have been
“deliberatively indifferent to the need,” City of Canton v. Harris, 489 U.S. 378, 390
(1989). Here, there is no evidence of past violations, and what happened to Graham
is not “so obviously” the consequence of a systemic lack of training, as opposed to
the decisions of individual officers, that the need for different or additional training
was plain. See Dick v. Watonwan Cnty., 738 F.2d 939, 942 (8th Cir. 1984) (noting
that an “isolated incident” is “not enough to establish a policy or custom”).

       Second, “the lack of clarity in the law” concerning the appropriate standard of
cause needed to justify a mental-health hold “precludes a finding that the
municipality had an unconstitutional policy at all, because its policymakers cannot
properly be said to have exhibited a policy of deliberate indifference to
constitutional rights that were not clearly established.” Szabla, 486 F.3d at 394; see
also Hollingsworth, 800 F.3d at 992 (“While a single constitutional violation arising
out of a lack of safeguards or training may be sufficient to establish deliberate
indifference where the need for such safeguards or training is obvious, a
municipality cannot exhibit fault rising to the level of deliberate indifference to a
constitutional right when that right has not yet been clearly established.” (internal
quotation marks omitted)). In other words, because the right at issue was not clearly
established, Graham cannot meet the “demand that deliberate indifference in fact be
deliberate.” Arrington-Bey v. City of Bedford Heights, 858 F.3d 988, 995 (6th Cir.
2017) (discussing and adopting the Eighth Circuit’s approach).

       Accordingly, the district court correctly entered summary judgment in favor
of the City on Graham’s Monell claims.

                                          III.

       We next consider the district court’s grant of summary judgment to the
officers on Graham’s state-law claims. Graham contends that the district court
improperly granted summary judgment to the officers on her claims of false


                                         -24-
imprisonment, battery, assault, and negligence because it erroneously concluded that
they were entitled to statutory and official immunity under Minnesota law. We
review de novo the application of state statutory and official immunity. See Boudoin,
962 F.3d at 1044; Johnson v. City of Minneapolis, 901 F.3d 963, 972 (8th Cir. 2018).
We conclude that the district court did not err.

      The MCCTA includes a statute-specific immunity section that provides:

      All persons acting in good faith, upon either actual knowledge or
      information thought by them to be reliable, who act pursuant to any
      provision of this chapter or who procedurally or physically assist in the
      commitment of any individual, pursuant to this chapter, are not subject
      to any civil or criminal liability under this chapter.

Minn. Stat. § 253B.23, subd. 4. Thus, all persons who in good faith participate in
the civil-commitment process, including by seizing someone for an emergency
mental-health evaluation, are immune from any civil or criminal liability, regardless
of whether the detained person is actually committed. Losen v. Allina Health Sys.,
767 N.W.2d 703, 709 (Minn. Ct. App. 2009) (holding that the MCCTA
“encompasses the good-faith decision whether to place an emergency hold on a
proposed patient, even if the result of that decision is that no hold is placed”). The
grant of immunity provides complete immunity from suit. Dokman v. Cnty. of
Hennepin, 637 N.W.2d 286, 297 (Minn. Ct. App. 2001).

       Just as Graham has not demonstrated a triable issue of fact as to whether the
officers had the requisite retaliatory animus to support her First Amendment
retaliatory-arrest claim, she has not shown a triable issue of fact regarding the good-
faith belief of the officers when they seized her for a mental-health evaluation. See
supra Section II.C. She simply advances no evidence that the officers acted in bad
faith. They are thus entitled to statutory immunity.

     For similar reasons, the officers also are entitled to official immunity. Under
Minnesota law, a public official is entitled to official immunity when his conduct


                                         -25-
requires the exercise of discretion or judgment and there is no evidence that he acted
maliciously or in bad faith. Johnson v. Morris, 453 N.W.2d 31, 41 (Minn. 1990);
Elwood v. Rice Cnty., 423 N.W.2d 671, 679 (Minn. 1988). “In determining whether
an official has committed a malicious wrong, we consider whether the official has
intentionally committed an act that he or she had reason to believe is prohibited.”
Hassan v. City of Minneapolis, 489 F.3d 914, 920 (8th Cir. 2007). Here, the officers
could not have acted in a manner that they believed to be unlawful when seizing
Graham because, as discussed above, the law was not clearly established. See id.

                                         IV.

     For the foregoing reasons, we affirm the district court’s grant of summary
judgment.
                          __________________________




                                        -26-

```

---

## GROUP: content/cases/Gutierrez v. Saenz.md  (`case`, 5 assertions)

### content_page

```
---
title: Gutierrez v. Saenz
type: case
citation: "606 U.S. 305 (2025)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2025
date_decided: ""
docket: 23-7809
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
  opinion_url: "https://www.courtlistener.com/opinion/10776824/gutierrez-v-saenz/"
  cluster_id: 10776824
  opinion_id: null
  identity_checked: true
lake:
  record_id: Gutierrez v. Saenz
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Standing to Challenge a Search]]"
tags:
  - case
  - section-1983
  - standing
  - due-process
  - postconviction-dna
  - redressability
  - supreme-court
holding: "A death-sentenced prisoner has Article III standing to bring a § 1983 procedural-due-process challenge to a State's postconviction DNA-testing scheme where a favorable judgment would redress his injury by removing the state prosecutor's asserted reason for denying DNA testing, even though the testing itself would not necessarily lead to his release."
aliases:
  - Gutierrez v. Saenz
  - "Gutierrez v. Saenz (2025)"
---

# Gutierrez v. Saenz

*606 U.S. 305 (2025)* (No. 23-7809) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776824 → opinion 11243411 (Sotomayor, J.; 606 U.S. 305, decided June 26, 2025). MCP read_document is blind to this opinion (html_with_citations empty); Rule quote sourced from the opinion 11243411 plain_text (U.S. Reports preliminary print, Vol. 606) via the REST method in CONSOLIDATED-REPAIR-REPORT.md §task-5, string-matched 2026-07-07. S9 promotes. -->

## Background
Ruben Gutierrez was sentenced to death in Texas for a 1998 murder. He has long maintained that he was not the killer and sought DNA testing of crime-scene evidence, but Texas's postconviction DNA-testing statute (Chapter 64) permits testing only to establish that a movant would not have been convicted — not merely that he would not have been eligible for the death penalty. When state courts denied testing, Gutierrez sued the local district attorney under 42 U.S.C. § 1983, claiming Texas's scheme denied him procedural due process. The lower courts held he lacked Article III standing because a declaratory judgment would not necessarily result in testing or his release.

## Issue
Whether Gutierrez has Article III standing to bring a § 1983 due-process challenge to Texas's postconviction DNA-testing procedures.

## Rule
Standing requires an injury that is redressable by a favorable decision, but redressability does not demand that relief guarantee an ultimate favorable outcome; a declaratory judgment satisfies it when it would remove the specific legal barrier the defendant relies on — here, eliminating the prosecutor's reliance on the challenged state law as the reason to deny testing. The Court held: "Gutierrez has standing to bring his §1983 claim challenging Texas's postconviction DNA testing procedures under the Due Process Clause." — 606 U.S. at 314. ^pin-314

## Application
Gutierrez's injury was the denial of access to DNA testing under an assertedly unconstitutional procedure. A declaration that Texas's scheme violates due process would redress that injury by knocking out the prosecutor's stated legal justification for refusing to test — even if the State might later invoke some other ground, and even though testing might not ultimately exonerate him. The Court analogized to *Reed v. Goertz*, where a nearly identical § 1983 challenge to the same Texas statute cleared the standing bar.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]]** (93 F.4th 267). Justice Sotomayor wrote for the Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Gutierrez* extends *Reed v. Goertz* and reinforces that a § 1983 procedural-due-process plaintiff challenging a postconviction evidence scheme need only show that a favorable declaration would clear away the challenged barrier — a redressability point of general importance to standing under the civil-rights statute.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Gutierrez v. Saenz*, 606 U.S. 305 (2025)](https://www.courtlistener.com/opinion/10776824/gutierrez-v-saenz/) — pinpoint: 606 U.S. at 314 (standing / redressability holding; syllabus "Pp. 314–321"). Rule quote sourced from opinion 11243411 `plain_text` (U.S. Reports preliminary print) — MCP `read_document` reads `html_with_citations`, which is empty for this opinion — string-matched 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a5d3947d0abd04ae", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "606 U.S. 305 (2025)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Gutierrez v. Saenz", "year": "2025"}}
{"assertion_id": "0f9925fdaad016bb", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Gutierrez v. Saenz"}}
{"assertion_id": "b8a02a44f6869fe1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A death-sentenced prisoner has Article III standing to bring a § 1983 procedural-due-process challenge to a State's postconviction DNA-testing scheme where a favorable judgment would redress his injury by removing the state prosecutor's asserted reason for denying DNA testing, even though the testing itself would not necessarily lead to his release.", "title": "Gutierrez v. Saenz"}}
{"assertion_id": "6bcb81a4627ddf22", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Gutierrez v. Saenz", "varies_by_point": "false"}}
{"assertion_id": "97affb882ea858f2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Gutierrez v. Saenz"}}
```

### lake record — Gutierrez v. Saenz

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gutierrez v. Saenz",
  "status": "under_review",
  "identity": {
    "case_name": "Gutierrez v. Saenz",
    "case_name_short": "Gutierrez",
    "case_name_full": "",
    "input_case_name": "Gutierrez v. Saenz",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2025,
    "docket": "23-7809",
    "cluster_id": 10776824,
    "lead_opinion_id": 11243411,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776824/gutierrez-v-saenz/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "606 U.S. 305",
      "volume": "606",
      "reporter": "U.S.",
      "page": "305",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "606 U.S. 305",
        "volume": "606",
        "reporter": "U.S.",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "606 U.S. 305",
    "official_selection": {
      "court_class": "scotus",
      "selected": "606 U.S. 305",
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
    "date_created": "2026-07-06T12:12:51Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "gutierrez-v-saenz--10776824",
      "to_record_id": "Gutierrez v. Saenz",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Gutierrez v. Saenz

```
                   PRELIMINARY PRINT

              Volume 606 U. S. Part 1
                             Pages 305–356




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 26, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                        OCTOBER TERM, 2024                             305

                                 Syllabus


                GUTIERREZ v. SAENZ et al.

certiorari to the united states court of appeals for
                  the fth circuit
    No. 23–7809. Argued February 24, 2025—Decided June 26, 2025
In 1998, Texas charged Ruben Gutierrez with capital murder for his
  involvement in the killing of Escolastica Harrison. The State's theory
  at trial was that Gutierrez wielded one of the two screwdrivers used to
  stab Harrison to death in her mobile home. The jury convicted Gutier-
  rez of capital murder. At the sentencing phase of Gutierrez's trial, the
  jury was required to answer whether Texas proved beyond a reasonable
  doubt that Gutierrez “actually caused” Harrison's death or, if not, that
  he “intended to kill [her]” or “anticipated that a human life would be
  taken.” Tex. Code Crim. Proc. Ann., Art. 37.071(2)(b)(2). The jury an-
  swered yes, and Gutierrez was sentenced to death.
     For nearly 15 years, Gutierrez has sought DNA testing of evidence
  he claims would prove he was not in Harrison's home the night of the
  murder. Texas's Article 64 allows DNA testing where a “convicted per-
Page Proof Pending Publication
  son establishes by a preponderance of the evidence” that he “would not
  have been convicted if exculpatory results had been obtained through
  DNA testing,” among other criteria. Art. 64.03(a)(2). Invoking Arti-
  cle 64, Gutierrez twice moved in state court for DNA testing of untested
  crime scene evidence. The trial court denied his frst request in 2010,
  and the Texas Court of Criminal Appeals (TCCA) affrmed. The court
  reasoned that even if Gutierrez's DNA was not found on the tested
  items, that would not establish his innocence of capital murder because
  he would still be a party to the robbery that resulted in Harrison's
  death. The court concluded that Gutierrez could not use Article 64 to
  show he was wrongly sentenced to death unless he could also establish
  his innocence of the underlying crime. In 2019, Gutierrez again sought
  DNA testing, but Texas courts denied his motion. On appeal, the
  TCCA reiterated that DNA testing was not available to show only death
  penalty ineligibility.
     Gutierrez then fled suit in federal court under 42 U. S. C. § 1983
  against Luis Saenz, the district attorney who has custody of the untes-
  ted evidence. Gutierrez argued that Texas's DNA testing procedures
  violated his liberty interests in utilizing state postconviction proce-
  dures. The District Court agreed and granted declaratory relief, fnd-
  ing it fundamentally unfair that Texas gives prisoners the right to chal-
  lenge their death sentence through habeas petitions but prevents them
306                     GUTIERREZ v. SAENZ

                                 Syllabus

  from obtaining DNA testing to support those petitions unless they can
  establish innocence of the underlying crime. The Fifth Circuit vacated
  the District Court's judgment and held that Gutierrez lacked standing to
  bring his § 1983 suit, fnding that his claimed injury was not redressable
  because a declaratory judgment would be unlikely to cause the prosecu-
  tor to “reverse course and allow testing.” 93 F. 4th 267, 272.
Held: Gutierrez has standing to bring his § 1983 claim challenging Texas's
 postconviction DNA testing procedures under the Due Process Clause.
 Pp. 314–321.
    (a) Individuals convicted of crimes in state court “have a liberty in-
 terest in demonstrating [their] innocence with new evidence under state
 law.” District Attorney's Offce for Third Judicial Dist. v. Osborne,
 557 U. S. 52, 68. For that reason, a state-created right to postconviction
 procedures can sometimes create rights to other procedures essential to
 realizing the state-created right. In Skinner v. Switzer, 562 U. S. 521,
 the Court held that a Texas prisoner could fle a due process claim under
 § 1983 against a prosecutor where the prisoner alleged that the prosecu-
 tor's refusal to turn over evidence deprived him of his liberty interests
 in utilizing state procedures to obtain reversal of his conviction or to
 obtain a pardon or reduction of his sentence. The Court reasoned that,
Page Proof Pending Publication
 while the prisoner could not challenge in federal court the state court
 decisions denying his Article 64 motions, he could allege in a federal
 § 1983 action that Article 64 unconstitutionally prevented him from ob-
 taining such testing.
    The question of a state prisoner's standing to bring a due process
 claim against the custodian of his evidence was frst addressed in Reed
 v. Goertz, 598 U. S. 230, where the Court confronted another challenge
 to Texas's postconviction DNA testing law. Reed alleged, among other
 things, that Article 64's chain-of-custody requirement was unconstitu-
 tional and effectively prevented many individuals from obtaining DNA
 testing. The Court held that Reed had standing to pursue declaratory
 relief. First, Reed adequately alleged an injury: denial of access to the
 requested evidence. Second, the state prosecutor caused Reed's injury
 by denying access to the evidence. Finally, if a federal court concluded
 that Texas's postconviction DNA testing procedures violate due process,
 the state prosecutor's justifcation for denying DNA testing would be
 eliminated, thereby removing the barrier between Reed and the re-
 quested testing. The same is true here. Like Reed, Gutierrez alleges
 that the local prosecutor's denial of his DNA testing request deprived
 him of his liberty interests in utilizing state procedures to obtain an
 acquittal or sentence reduction. As in Reed, the declaratory judgment
 Gutierrez seeks would redress that injury by changing the legal status
                      Cite as: 606 U. S. 305 (2025)                      307

                                 Syllabus

 of the parties and eliminating the state prosecutor's allegedly unlawful
 justifcation for denying DNA testing. Pp. 314–316.
    (b) The Fifth Circuit recognized the clear parallels between this case
 and Reed but distinguished the cases, reasoning that the local prosecu-
 tor in this case was unlikely to allow testing even if a federal court
 declared that Texas may not deny DNA testing that would affect only
 the punishment stage. Respondents, too, argue that Gutierrez lacks
 standing because the District Court's reason for declaring part of Arti-
 cle 64 unconstitutional was only one of several independent state-law
 grounds supporting the prosecutor's decision to deny access to the evi-
 dence. But this attempt to distinguish Reed fails twice over.
    First, to the extent the Fifth Circuit based its assessment of redress-
 ability on the declaratory judgment the District Court later issued,
 rather than Gutierrez's complaint, it turned the Article III standing in-
 quiry on its head. Gutierrez's standing does not depend on the relief
 the District Court ultimately granted on the merits. The proper focus
 of the standing inquiry is the complaint, and Gutierrez's complaint chal-
 lenges not just Article 64's limitation to actual innocence claims, but also
 the other barriers Article 64 erects between Gutierrez and DNA testing.
 Second, and more fundamentally, the Fifth Circuit erred in transforming

Page Proof Pending Publication
 the redressability inquiry into a guess about whether a favorable court
 decision will ultimately result in the prosecutor turning over the DNA
 evidence. In Reed, the Court reasoned that, if a federal court concludes
 that Texas's postconviction DNA testing procedures violate due process,
 that court order would redress the injury by eliminating the state prose-
 cutor's reliance on Article 64 as a reason for denying DNA testing. The
 same is true here. A declaratory judgment in Gutierrez's favor would
 redress his injury by removing the allegedly unconstitutional barrier
 Article 64 erected between Gutierrez and the requested testing. The
 Court in Reed was unmoved by the prosecutor's assertion that a declara-
 tory judgment would not change his ultimate decision to turn over the
 evidence. The reason is simple: That a prosecutor might eventually
 fnd another reason to deny a prisoner's DNA testing request does not
 eliminate the prisoner's standing to argue that the cited reasons vio-
 lated his rights under the Due Process Clause. Pp. 316–320.
    (c) Respondents also assert that this case is now moot because the
 state prosecutor refused Gutierrez's DNA testing request even after the
 District Court issued the declaratory judgment. That claim fails, too.
 A procedural due process claim like Gutierrez's is not mooted by the
 defendant's mid-appeal promise that, regardless of the lawsuit's out-
 come, the ultimate result will remain the same. Holding otherwise
 would allow defendants to manufacture mootness by ensuring that, no
 matter what procedures a court requires them to employ, the same sub-
308                     GUTIERREZ v. SAENZ

                          Opinion of the Court

  stantive outcome will follow. Article III requires no such result.
  Pp. 320–321.
93 F. 4th 267, reversed and remanded.

  Sotomayor, J., delivered the opinion of the Court, in which Roberts,
C. J., and Kagan, Kavanaugh, and Jackson, JJ., joined, and in which
Barrett, J., joined as to all but Part II–B–2. Barrett, J., fled an opin-
ion concurring in part and concurring in the judgment, post, p. 321.
Thomas, J., fled a dissenting opinion, post, p. 322. Alito, J., fled a dis-
senting opinion, in which Thomas and Gorsuch, JJ., joined, post, p. 338.

  Anne Elizabeth Fisher argued the cause for petitioner.
With her on the briefs were Lisa Evans Lewis, Joseph W.
Luby, and Joanne M. Heisey.
  William F. Cole, Deputy Solicitor General of Texas, ar-
gued the cause for respondents. With him on the brief were
Ken Paxton, Attorney General, Aaron L. Nielson, Solicitor
General, Brent Webster, First Assistant Attorney General,
Cameron Fraser, Assistant Solicitor General, and Eric Abels
Page Proof Pending Publication
and Jefferson D. Clendenin, Assistant Attorneys General.*

  Justice Sotomayor delivered the opinion of the Court.
  For nearly 15 years, petitioner Ruben Gutierrez has
sought DNA testing of evidence that, he says, will help him
prove he was never at the scene of the murder he was con-
victed of committing. When the local prosecutor refused to
test the evidence in his custody, Gutierrez fled suit under
Rev. Stat. § 1979, 42 U. S. C. § 1983, arguing that Texas's pro-

   *Elizabeth B. Wydra and Brianne J. Gorod fled a brief for the Constitu-
tional Accountability Center as amicus curiae urging reversal.
   A brief of amici curiae urging affrmance was fled for the State of
Arkansas et al. by Tim Griffn, Attorney General of Arkansas, and Dylan
L. Jacobs, Interim Solicitor General, and by the Attorneys General for
their respective States as follows: Steve Marshall of Alabama, Treg Taylor
of Alaska, Theodore E. Rokita of Indiana, Brenna Bird of Iowa, Russell
Coleman of Kentucky, Liz Murrill of Louisiana, Lynn Fitch of Mississippi,
Michael T. Hilgers of Nebraska, Dave Yost of Ohio, Gentner Drummond
of Oklahoma, Alan Wilson of South Carolina, Jonathan Skrmetti of Ten-
nessee, and Derek Brown of Utah.
                   Cite as: 606 U. S. 305 (202)            309

                      Opinion of the Court

cedures for obtaining DNA testing violated his rights under
the Due Process Clause. The District Court agreed and
granted a declaratory judgment to that effect.
  The Fifth Circuit, however, held that Gutierrez lacked
standing to bring his § 1983 suit, reasoning that, even if a
federal court declared Texas's procedures unconstitutional,
the local prosecutor would be unlikely to turn over the physi-
cal evidence for DNA testing. That holding contravenes
Reed v. Goertz, 598 U. S. 230 (2023), where this Court decided
on analogous facts that another Texas prisoner had standing
to sue the local prosecutor who denied him access to DNA
testing. Id., at 234. Put simply, Reed held that a federal
court order declaring “that Texas's post-conviction DNA
testing procedures violate due process” would redress the
prisoner's claimed injury by “eliminat[ing]” the state prose-
cutor's reliance on Article 64 as a reason for denying DNA
testing. Ibid.; see Tex. Code Crim. Proc. Ann., Art. 64.01
Page Proof Pending Publication
(Vernon 2018). The same is true here and the Court there-
fore reverses.
                                I
                               A
  In 1998, Texas charged Ruben Gutierrez with capital mur-
der for the killing of Escolastica Harrison at her mobile home
in Brownsville, Texas. The State's theory at trial was that
Harrison had been stabbed to death with two different
screwdrivers. To support its view that Gutierrez wielded
one of the two screwdrivers in question, the State introduced
a statement Gutierrez gave to the police, in which he ac-
knowledged that he and two accomplices had planned to rob
Harrison on the day she was killed and that he had been in
Harrison's home while one of his accomplices stabbed her.
The jury convicted Gutierrez of capital murder.
  Texas law provides that a criminal defendant can be guilty
of capital murder even where he was merely a party to a
crime (such as robbery) that resulted in a person's death.
310                   GUTIERREZ v. SAENZ

                        Opinion of the Court

Tex. Penal Code Ann. §§ 7.01, 7.02, 19.02, 19.03 (West 2021
and Cum. Supp. 2024). A death sentence, however, may be
imposed only if “the defendant actually caused the death of
the deceased[,] . . . intended to kill the deceased or . . . antici-
pated that a human life would be taken.” Tex. Code Crim.
Proc. Ann., Art. 37.071(2)(b)(2) (Vernon 2006); see also John-
son v. State, 853 S. W. 2d 527, 535 (Tex. Crim. App. 1992) (en
banc) (“The Texas capital murder scheme does not allow an
individual to be put to death for merely being a party to a
murder”). To that end, the jury was required at the sen-
tencing phase of Gutierrez's trial to answer whether Texas
proved beyond a reasonable doubt that Gutierrez “actually
caused” Harrison's death or, if not, that he “intended to kill
[her]” or “anticipated that a human life would be taken.”
Art. 37.071(2)(b)(2). The jury answered yes, and Gutierrez
was sentenced to death.
   Gutierrez has long maintained that the police coerced him
Page Proof Pending Publication
into confessing that he was in Harrison's home on the night
of the murder. He insists that, as he twice told the police
before the statement in which he purportedly confessed, he
never entered the mobile home that night. Although Gutier-
rez never disputed that he and two accomplices planned to
rob Harrison, he contends that he thought his accomplices
would merely rob Harrison's empty mobile home and that
no one would be harmed during the robbery. He accordingly
asserts that he should never have been sentenced to death, and
intends to seek vacatur of his death sentence in a state habeas
petition. See Art. 11.071(5)(a)(3) (Vernon Cum. Supp. 2024).
   Since 2010, Gutierrez has sought DNA testing of crime-
scene evidence, including Harrison's nail scrapings, a loose
hair, and various blood samples, to help him prove it was his
accomplices, not Gutierrez, in Harrison's home on the night
of her murder. He maintains that Texas's Article 64 entitles
him to such DNA testing. Art. 64.01(a)(1). That law pro-
vides for DNA testing where a “convicted person establishes
by a preponderance of the evidence” that he “would not have
                   Cite as: 606 U. S. 305 (202)             311

                      Opinion of the Court

been convicted if exculpatory results had been obtained
through DNA testing” and that the request was “not made
to unreasonably delay the execution of sentence or adminis-
tration of justice.” Art. 64.03(a)(2). To grant a motion for
DNA testing under Article 64, the state court must also fnd,
among other things, that the evidence “is in a condition mak-
ing DNA testing possible” and that “identity was or is an
issue in the case.” Art. 64.03(a)(1).
   Invoking Article 64, Gutierrez twice moved in state court
for an order requiring the local district attorney to turn over
the untested crime scene evidence for DNA testing. The
trial court denied his frst request in 2010, and the Texas
Court of Criminal Appeals (TCCA) affrmed. Ex parte Gu-
tierrez, 337 S. W. 3d 883, 886 (2011). The TCCA reasoned
that, even if Gutierrez's DNA was not present on the tested
items, that would not establish his innocence of Texas capital
murder. Id., at 899, 901. After all, even if he was not in
Page Proof Pending Publication
the home, Gutierrez could still be a party to the robbery that
eventually resulted in Harrison's death. Id., at 901. And,
as the TCCA saw it, Gutierrez could not invoke Article 64 to
establish that he had been wrongly sentenced to death unless
he could also establish his innocence of the underlying crime.
Ibid. Finally, the court added: “[E]ven if [Article] 64 did
apply to evidence that might affect the punishment stage as
well as conviction,” Gutierrez “still would not be entitled to
testing” because “the record facts” show that “he played a
major role in the underlying robbery and that his acts
showed a reckless indifference to human life.” Ibid.
   Gutierrez tried again in 2019, this time bolstered by new
counsel and new evidence that, according to Gutierrez, would
implicate Harrison's nephew, Avel Cuellar, as one of the two
people who stabbed Harrison to death. In the interim, Fer-
min Cuellar (Avel Cuellar's nephew), had signed a sworn
statement averring that his uncle Avel approached him in
the summer of 1998 about stealing “ `a lot' ” of money from
Harrison. App. 701a. Fermin also averred that, after the
312                  GUTIERREZ v. SAENZ

                       Opinion of the Court

murder, Avel boasted to Fermin that he had money buried in
the trailer park. Again, the Texas courts denied Gutierrez's
motion. On appeal, the TCCA reiterated that DNA testing
was not available to show ineligibility for the death penalty
and that, “ `even if [it were],' ” Gutierrez “ `still would not be
entitled to testing.' ” Gutierrez v. State, 2020 WL 918669,
*7–*9 (Feb. 26, 2020) (per curiam).

                                B
  Gutierrez next fled this federal action for declaratory and
injunctive relief under 42 U. S. C. § 1983. He sued respond-
ent Luis Saenz, the district attorney who has custody of the
evidence Gutierrez would like tested and whose offce prose-
cuted Gutierrez. Gutierrez's complaint alleges that, “[b]y
refusing to release the biological evidence for testing, and
thereby preventing [Gutierrez] from gaining access to excul-
patory evidence that could have led to his acquittal [or] dem-
Page Proof Pending Publication
onstrated that he is not death eligible,” the district attorney
“deprived” him “of his liberty interests in utilizing state
[postconviction] procedures . . . in violation of his right to
due process of law.” App. 457a–458a.
  Gutierrez's complaint pinpoints at least three features of
Article 64 that prevented him from gaining access to the rel-
evant evidence to which, he says, the Due Process Clause
entitles him. First, Gutierrez says, the Texas courts inter-
pret Article 64 to impose a virtually insurmountable barrier
to obtaining DNA testing, deeming a prisoner ineligible as
long as the record contains any evidence, no matter how
minor, that he committed the crime. Id., at 449a, 451a.
Second, and relatedly, he asserts that it was unfair for the
TCCA not to consider new evidence he had proffered since
his trial: A fair procedure, he contends, would require consid-
ering the effect exculpatory DNA evidence would have on a
jury that also heard “new evidence casting doubt on [Gutier-
rez's] statement” to the police. Id., at 452a, n. 8. Third,
Gutierrez asserts that, as interpreted by the TCCA, Article
                     Cite as: 606 U. S. 305 (202)              313

                        Opinion of the Court

64 violates the Due Process Clause by forbidding DNA test-
ing when its sole purpose is to establish that a defendant is
ineligible for the death penalty. Id., at 456a.
   The District Court agreed with Gutierrez in part. 565 F.
Supp. 3d 892 (SD Tex. 2021). It is fundamentally unfair, the
court declared, that Texas gives prisoners the right to fle a
habeas petition challenging their death sentence, but pre-
cludes them from obtaining DNA testing to support that ha-
beas petition unless they can establish innocence of the un-
derlying crime. Id., at 911. That limitation renders the
habeas right “illusory” because few people can make a clear
showing that they were wrongly sentenced to death without
DNA evidence. Id., at 910–911. “Due process,” the court
explained, “does not countenance procedural sleight of hand
whereby a state extends a right with one hand and then
takes it away with another.” Id., at 911.
   On appeal, a divided panel of the Fifth Circuit vacated the
Page Proof Pending Publication
District Court's declaratory judgment, reasoning that Gutie-
rrez's claimed injury was not redressable because the declar-
atory judgment would be unlikely to cause the prosecutor to
“reverse course and allow testing.” 93 F. 4th 267, 272
(2024). The court recognized that, just two years ago, this
Court rejected a nearly identical argument in Reed, 598 U. S.
230. See 93 F. 4th, at 273–274, and n. 3. Yet the Fifth Cir-
cuit purported to distinguish Reed because, in Gutierrez's
case, the TCCA “effectively anticipated an unfavorable fed-
eral court ruling” when it held that, even if Article 64 ap-
plied to claims affecting death eligibility, the facts in the trial
record would still not entitle Gutierrez to DNA testing. 93
F. 4th, at 275. Judge Higginson dissented, noting that he
saw no “meaningful distinction” between this case and Reed.
93 F. 4th, at 275.
   While Gutierrez's request for rehearing was pending in the
Fifth Circuit, Texas scheduled his execution. This Court
stayed his execution and granted certiorari to consider Gu-
tierrez's standing to bring his § 1983 claim. 603 U. S. 949
314                       GUTIERREZ v. SAENZ

                            Opinion of the Court

(2024). Because Reed plainly establishes that he does, the
Court now reverses.
                           II
                                      A
   Individuals convicted of crimes in state court “have a lib-
erty interest in demonstrating [their] innocence with new ev-
idence under state law.” District Attorney's Offce for
Third Judicial Dist. v. Osborne, 557 U. S. 52, 68 (2009). For
that reason, a state-created right to postconviction proce-
dures can, “ `in some circumstances, beget yet other rights to
procedures essential to the realization of the parent right.' ”
Ibid.1 To that end, this Court held in Skinner v. Switzer,
562 U. S. 521 (2011), that a Texas prisoner could fle a due
process claim under § 1983 against a prosecutor who refused
“ `to release . . . biological evidence for testing.' ” Id., at
530. In that case, Skinner had alleged that the prosecutor's

Page Proof Pending Publication
refusal to turn over evidence deprived him of “ `his liberty
interests in utilizing state procedures to obtain reversal of
his conviction and/or to obtain a pardon or reduction of his
sentence.' ” Ibid. This Court reasoned that, while Skinner
could not challenge in federal court the TCCA decisions de-
nying his Article 64 motions, he could allege in a § 1983 ac-
tion that Article 64 unconstitutionally prevented him from
obtaining such testing. Id., at 532.
   Skinner did not explicitly address a state prisoner's stand-
ing to bring a due process claim against the custodian of his

  1
    One of the dissents contends that this Court “ha[d] no business inter-
vening in this case in the frst place” because “Gutierrez's suit rests on the
premise that the Fourteenth Amendment's Due Process Clause gives him
a `liberty interest' in Texas's voluntarily created procedures.” Post, at
322 (opinion of Thomas, J.). Even if the merits of Gutierrez's due process
claim were relevant to the standing question at issue here (they are not),
Osborne squarely forecloses Justice Thomas's view of that claim. See
557 U. S., at 68; see also, e. g., Wolff v. McDonnell, 418 U. S. 539, 558 (1974)
(“[L]iberty,” like property, is protected by the Constitution, “even when
the liberty itself is a statutory creation of the State”).
                    Cite as: 606 U. S. 305 (202)             315

                       Opinion of the Court

evidence. That question was frst raised in Reed, where this
Court confronted another claim that Texas's postconviction
DNA testing law failed to guarantee procedural due process.
598 U. S., at 233. Rodney Reed alleged, among other things,
that Article 64's “stringent chain-of-custody requirement
was unconstitutional and in effect foreclosed DNA testing
for individuals convicted before `rules governing the State's
handling and storage of evidence were put in place.' ” Ibid.
Before this Court, the local prosecutor argued that Reed
lacked Article III standing. Specifcally, the prosecutor as-
serted that a favorable court decision would not redress
Reed's injury. That was because, in the prosecutor's view, a
federal court's “declaration that the statutory provision [he]
attack[s] is unconstitutional” would not “ `likely' ” cause the
district attorney to turn over the physical evidence in his
possession. Brief for Respondents 38–39; Reed, 598 U. S.
230; California v. Texas, 593 U. S. 659, 673 (2021).
Page Proof Pending Publication
   This Court disagreed and held that Reed had established
standing to pursue the declaratory judgment action. First,
the Court explained, “Reed suffciently alleged an injury in
fact: denial of access to the requested evidence.” 598 U. S.,
at 234. Second, “[t]he state prosecutor, who is the named
defendant, denied access to the evidence and thereby caused
Reed's injury.” Ibid. Finally, the Court reasoned, “if a
federal court concludes that Texas's post-conviction DNA
testing procedures violate due process, that court order
would eliminate the state prosecutor's justifcation for deny-
ing DNA testing” and thereby remove the barrier between
Reed and the requested DNA testing. Ibid.
   The same is true of Gutierrez's suit. Like Reed and Skin-
ner, Gutierrez alleges that the local prosecutor's denial of his
request for DNA testing deprived him of “his liberty inter-
ests in utilizing state procedures to obtain an acquittal and/
or reduction of his sentence, in violation of his right to due
process of law.” App. 458a. As in Reed, moreover, the de-
claratory judgment Gutierrez seeks would redress that in-
316                 GUTIERREZ v. SAENZ

                      Opinion of the Court

jury by “ `order[ing] a change in [the] legal status' ” of the
parties and “eliminat[ing]” the state prosecutor's allegedly
unlawful “justifcation for denying DNA testing.” 598 U. S.,
at 234. That is suffcient to resolve this case.

                               B
                               1
   The Fifth Circuit recognized the clear parallels between
this case and Reed. See 93 F. 4th, at 272, 274, n. 3. Never-
theless, the court thought that, unlike in Reed, the local
prosecutor here was unlikely to allow testing even if a fed-
eral court “declare[d] Texas may not deny DNA testing that
would affect only the punishment stage.” 93 F. 4th, at 272.
Because the TCCA already concluded Gutierrez would not
be entitled to DNA testing even if Article 64 did apply to
evidence affecting only the punishment stage, the Fifth Cir-
cuit reasoned that the district attorney would “quite likely”
Page Proof Pending Publication
rely on that holding to deny testing again. Id., at 274. Re-
spondents, joined by the principal dissent, similarly urge
that Gutierrez lacks standing because the District Court's
reason for declaring part of Article 64 unconstitutional “was
only one of several independent state-law grounds support-
ing District Attorney Saenz's decision to deny access to the
requested evidence.” Brief for Respondents 24; see also
post, at 348–349 (opinion of Alito, J.).
   This attempt to distinguish Reed is wrong twice over.
First, both respondents and the Fifth Circuit gloss over the
substance of Gutierrez's complaint, which is the proper focus
of the standing inquiry here. See Davis v. Federal Election
Comm'n, 554 U. S. 724, 734 (2008). Gutierrez's complaint
takes issue not just with Article 64's limitation to actual in-
nocence claims, but with the barrier Article 64 erects be-
tween Gutierrez and DNA testing. At bottom, Gutierrez as-
serts that, to the extent Texas law precludes him from
obtaining the requested evidence, it violates his rights under
the Due Process Clause. App. 457a–458a. That is why his
                        Cite as: 606 U. S. 305 (202)                     317

                           Opinion of the Court

complaint alleges, among other things, that Article 64 poses
a “virtually impossible [standard] for anyone convicted under
the law of parties to obtain DNA testing,” id., at 453a, and
why he takes issue with the TCCA's refusal to consider
“newly proffered evidence” in assessing claims like his own,
id., at 452a, n. 8.2 To the extent the Fifth Circuit based its
assessment of redressability on the declaratory judgment the
District Court later issued, rather than Gutierrez's com-
plaint, it turned the Article III standing inquiry on its head.
Gutierrez's “standing to bring this suit,” 93 F. 4th, at 271,
does not depend on the relief the District Court granted on
the merits.
   The principal dissent does not dispute that Gutierrez chal-
lenged, in his complaint, each of the roadblocks Article 64
placed between himself and DNA testing. Post, at 350
(opinion of Alito, J.). Instead, the dissent repeats the Fifth
Circuit's error, urging that Gutierrez can now obtain only
Page Proof Pending Publication
“reinstatement of the District Court's declaratory judg-
ment.” Post, at 347. But rather than assert that the scope
of the declaratory judgment retroactively deprived the Dis-
trict Court of jurisdiction over Gutierrez's complaint, as the
Fifth Circuit erroneously held, the principal dissent suggests
instead that “affrmance of the District Court's declaratory

  2
    The principal dissent highlights the TCCA's rule “ that only evi-
dence in the trial record may be considered in determining whether post-
conviction DNA testing is allowed.” Post, at 354 (opinion of Alito, J.).
That construction of Texas law is, of course, what Gutierrez has challenged
under the Due Process Clause. See supra, at 312. In Gutierrez's view,
that new evidence, together with the DNA testing, will help him establish
that he did not in fact “anticipat[e] that a human life would be taken,” Tex.
Code Crim. Proc. Ann., Art. 37.071(2)(b)(2), and that his death sentence
must therefore be vacated. Contra, post, at 354 (Alito, J., dissenting)
(insisting that “a favorable decision on Gutierrez's constitutional argument
would not bolster his challenge to his sentence”). That the principal dis-
sent is skeptical about the merits of Gutierrez's due process challenge is
not pertinent because the Court only granted certiorari to consider Gutier-
rez's Article III standing to bring his suit. See ibid.
318                      GUTIERREZ v. SAENZ

                            Opinion of the Court

judgment” would not help Gutierrez moving forward. Post,
at 350. That argument, however, does nothing to support
the Fifth Circuit's holding, which the principal dissent de-
fends, that Gutierrez lacked “standing to bring this suit.”
93 F. 4th, at 271.3
                              2
  Second, and more fundamentally, the Fifth Circuit erred
in transforming the redressability inquiry into a guess as to
whether a favorable court decision will in fact ultimately
cause the prosecutor to turn over the evidence. Id., at 274.
In Reed, just like in this case, the Texas courts had proffered
multiple reasons for denying Reed's Article 64 motion, in-
cluding that “Reed did not demonstrate that he would have
been acquitted if the DNA results were exculpatory,” 598
U. S., at 233, and that Reed “failed to establish that his re-
quest [was] not made to unreasonably delay the execution of
his sentence,” Reed v. State, 541 S. W. 3d 759, 778 (Tex. Crim.
Page Proof Pending Publication
App. 2017). The principal dissent claims that, for Reed,
“striking down the chain-of-custody rule” would have “criti-
cally undermined the TCCA's holding” as to “[t]wenty-one
additional items,” which “could have been considered” if the
declaratory judgment issued in his favor. Post, at 352. Yet

   3
     As the principal dissent sees it, the Fifth Circuit held only that Gutier-
rez lacked standing to press one of his arguments in favor of Article 64's
unconstitutionality: that “ `the state violates due process by . . . preventing
testing if resulting evidence would be relevant only to the sentence.' ”
Post, at 348, n. 7 (quoting 93 F. 4th, at 271). Even if that particular argu-
ment about Article 64's unlawfulness could be disentangled from the rest
of Gutierrez's due process claim, see supra, at 312–313, 316, however, the
dissent never embraces the Fifth Circuit's view that Gutierrez lacked
“standing to bring this suit” in the District Court, 93 F. 4th, at 271. In-
stead, it suggests that Gutierrez lacked standing to seek “affrmance of
th[at] claim” from the Fifth Circuit. Post, at 348, n. 7. It was the district
attorney, not Gutierrez, who sought relief from the Fifth Circuit, and there
is no reason to think the Courts of Appeals must dismiss a case for lack
of standing simply because the nonappealing party did not cross-appeal
the scope of the District Court's judgment.
                   Cite as: 606 U. S. 305 (202)             319

                      Opinion of the Court

even absent the chain-of-custody rule, Reed still faced the
TCCA's assessment that his DNA testing request was “un-
timely,” 541 S. W. 3d, at 778, and the trial court's determina-
tion that “exculpatory results from DNA testing of all the
evidence he requested to be tested” would not establish his
innocence, id., at 773. This Court nevertheless reasoned in
Reed that, “if a federal court concludes that Texas's post-
conviction DNA testing procedures violate due process,”
that court order would redress his injury by “eliminat[ing]”
the state prosecutor's reliance on Article 64 as a reason for
denying DNA testing. 598 U. S., at 234. The particular de-
claratory judgment Reed requested was thus no more likely
to yield a change in the district attorney's conduct than the
one Gutierrez sought here. Contra, post, at 347, 351–354
(opinion of Alito, J.).
   What was true in Reed thus applies here, too. There is
little doubt that Saenz considers Article 64 in his assessment
Page Proof Pending Publication
of whether to provide requested DNA evidence. Indeed,
Saenz confrmed at oral argument that he would likely “turn
over the evidence” if he thought Article 64 entitled Gutierrez
to DNA testing. Tr. of Oral Arg. 71. A declaratory judg-
ment in Gutierrez's favor would accordingly redress his in-
jury by removing the allegedly unconstitutional barrier Arti-
cle 64 erected between Gutierrez and the requested testing.
   To be sure, Saenz nevertheless states that any declaratory
judgment will not affect his ultimate willingness to turn over
the evidence. He and the principal dissent urge that the
Court need not even “speculate” about what he might do
because, “[a]fter securing a declaratory judgment from the
district court,” Gutierrez again sought DNA testing and
“Saenz refused.” Brief for Respondents 27; see post, at 350
(opinion of Alito, J.). This, again, is a familiar refrain. The
prosecutor in Reed, too, maintained that a declaratory judg-
ment would not “ `bring about' ” “ `any change in [his] con-
duct.' ” Brief for Respondents 38–39; Reed, 598 U. S., at 249
(Thomas, J., dissenting). This Court was unmoved by that
320                 GUTIERREZ v. SAENZ

                      Opinion of the Court

assertion. See id., at 234. The reason is simple: That a
prosecutor might eventually fnd another reason, grounded
in Article 64 or elsewhere, to deny a prisoner's request for
DNA testing does not vitiate his standing to argue that the
cited reasons violated his rights under the Due Process
Clause. See, e. g., Federal Election Comm'n v. Akins, 524
U. S. 11, 25 (1998) (“[T]hose adversely affected by a discre-
tionary agency decision generally have standing to complain
that the agency based its decision upon an improper legal
ground . . . even though the agency . . . might later, in the
exercise of its lawful discretion, reach the same result for a
different reason”); Lujan v. Defenders of Wildlife, 504 U. S.
555, 572, n. 7 (1992) (“[U]nder our case law, one living adja-
cent to the site for proposed construction of a federally li-
censed dam has standing to challenge the licensing agency's
failure to prepare an environmental impact statement, even
though he cannot establish with any certainty that the state-

Page Proof Pending Publication
ment will cause the license to be withheld or altered . . . ”).

                               C
   Finally, Saenz asserts in the alternative that this case is
now moot because Saenz refused Gutierrez's request for
DNA testing even after the District Court issued the declar-
atory judgment. Brief for Respondents 42–44. That claim
fails, too. As Saenz himself recognizes, “a case `becomes
moot only when it is impossible for a court to grant any effec-
tual relief whatever to the prevailing party.' ” Chafn v.
Chafn, 568 U. S. 165, 172 (2013) (quoting Knox v. Service
Employees, 567 U. S. 298, 307 (2012)). It is not enough that
“the practical impact of any decision is not assured.” 568
U. S., at 175.
   In any event, a procedural due process claim like the one
Gutierrez presses is not mooted by the defendant's mid-
appeal promise that, no matter the result of a lawsuit, the
ultimate outcome will not change. Holding otherwise would
                   Cite as: 606 U. S. 305 (2025)             321

                     Opinion of Barrett, J.

allow all manner of defendants to manufacture mootness by
ensuring that, no matter what procedures a court requires
the defendant to employ, the same substantive outcome will
result. In that world, the person “living adjacent to the site
for proposed construction of a federally licensed dam” would
lose her claim “to challenge the licensing agency's failure to
prepare an environmental impact statement” as long as the
agency promised that the statement would not cause the li-
cense to be withheld or altered. Lujan, 504 U. S., at 572,
n. 7. Article III mandates no such result.

                         *      *      *
  In the end, Reed is indistinguishable. Gutierrez has
standing to challenge Texas's DNA testing procedures under
the Due Process Clause. The judgment of the U. S. Court
of Appeals for the Fifth Circuit is therefore reversed, and
the case is remanded for further proceedings consistent with
Page Proof Pending Publication
this opinion.
                                            It is so ordered.

  Justice Barrett, concurring in part and concurring in
the judgment.
  When the Fifth Circuit attempted to distinguish this case
from Reed v. Goertz, 598 U. S. 230 (2023), it failed to consider
the breadth of the relief that Gutierrez requested in his com-
plaint. See ante, at 316. I would reverse on that basis
alone. The Court goes further, borrowing from our some-
what relaxed redressability inquiry in administrative-law
procedural injury cases. See ante, at 318–320 (citing Fed-
eral Election Comm'n v. Akins, 524 U. S. 11, 25 (1998);
Lujan v. Defenders of Wildlife, 504 U. S. 555, 572, n. 7
(1992)). By invoking Akins and Lujan in the unique context
of requests for DNA evidence from Texas prosecutors, the
Court muddies the waters of standing doctrine. I respect-
fully join all but Part II–B–2 of the Court's opinion.
322                      GUTIERREZ v. SAENZ

                          Thomas, J., dissenting

   Justice Thomas, dissenting.
   I join Justice Alito's principal dissent because I agree
that Ruben Gutierrez lacks standing to bring a federal suit
alleging that Texas's post-conviction DNA testing proce-
dures violate due process.1 I write separately to emphasize
that this Court has no business intervening in this case in
the frst place. The Constitution does not require any State
to establish procedures for state prisoners to challenge the
validity of their convictions after trial. Yet, Gutierrez's suit
rests on the premise that the Fourteenth Amendment's Due
Process Clause gives him a “liberty interest” in Texas's
voluntarily created procedures. That premise cannot be
squared with any principled reading of the Due Process
Clause. I therefore disagree with our decision to grant cer-
tiorari and revive Gutierrez's challenge. Our intervention
serves no purpose other than to exacerbate the already egre-
gious delays endemic to capital litigation.
Page Proof Pending
              I    Publication
                                     A
  The Texas Constitution provides capital defendants the
right to a trial by jury. Art. 1, § 10. It further provides
that, after a defendant is convicted and sentenced, he may
   1
     I agree that the Court “fagrantly distorts the standard” that this
Court articulated in Reed v. Goertz, 598 U. S. 230 (2023), by deeming irrele-
vant the independent grounds that the Texas courts have given for deny-
ing DNA testing to Gutierrez. Post, at 346–348 (Alito, J., dissenting).
I also continue to believe that Reed made “chaos” of our standing doctrine.
598 U. S., at 255 (Thomas, J., dissenting). Even if the Texas courts had
not articulated alternative grounds for denying Gutierrez testing, “an ab-
stract declaration” that Texas's limits on DNA testing are unconstitutional
cannot redress any injury because it does not compel any “change in con-
duct” on the part of the district attorney. Id., at 249. Gutierrez's real
dispute is with the Texas courts for denying his motions for testing, but
the Rooker-Feldman doctrine prohibits parties from attacking state-court
judgments in federal district court. See Reed, 598 U. S., at 244–252
(Thomas, J., dissenting); Rooker v. Fidelity Trust Co., 263 U. S. 413 (1923);
District of Columbia Court of Appeals v. Feldman, 460 U. S. 462 (1983).
                   Cite as: 606 U. S. 305 (2025)           323

                     Thomas, J., dissenting

fle a direct appeal to the Texas Court of Criminal Appeals
(TCCA), the State's highest court for criminal cases. Art.
5, § 5(b). Texas law also allows prisoners sentenced to death
to challenge their conviction and sentence collaterally by fl-
ing a petition for habeas corpus in their court of conviction.
Tex. Code Crim. Proc. Ann., Art. 11.071 (Vernon Cum. Supp.
2024). Even if the prisoner's trial was error free, he may
obtain habeas relief under state law if he produces newly
discovered evidence establishing that he is actually innocent
of the offense. Ex parte Mayhugh, 512 S. W. 3d 285, 295
(Tex. Crim. App. 2016).
   Chapter 64 of the Texas Code of Criminal Procedure fur-
ther allows convicted defendants to seek testing of DNA evi-
dence that was in the possession of the State during trial.
Arts. 64.01(a)(2)(a–1), (b) (Vernon 2018). Upon the defend-
ant's motion, the convicting court may order testing if cer-
tain conditions are met, including that the evidence still

Page Proof Pending Publication
exists in a testable condition, that the defendant can show
that he likely would not have been convicted had he obtained
exculpatory results from DNA testing, and that the defend-
ant can show that he is not bringing the motion unreasonably
to delay his execution. Art. 64.03(a). Defendants who ob-
tain DNA testing may use the results to support their state
habeas petitions. Thacker v. State, 177 S. W. 3d 926, 927
(Tex. Crim. App. 2005) (per curiam).

                                B
   A Texas jury convicted Gutierrez and sentenced him to
death for the 1998 robbery and murder of Escolastica Har-
rison. Having thrice failed to obtain DNA testing under
Chapter 64 in state court, he now claims that several of
Chapter 64's restrictions on obtaining DNA testing violate
the Due Process Clause of the Fourteenth Amendment. See
ante, at 311–313.
   To make sense of Gutierrez's claim, we must frst under-
stand what rights the Due Process Clause protects. The
Clause provides that no State shall “deprive any person of
324                  GUTIERREZ v. SAENZ

                      Thomas, J., dissenting

life, liberty, or property, without due process of law.” Amdt.
14, § 1. In other words, the State cannot decide to take
away an individual's life, liberty, or property unless it ad-
heres to certain procedures. But, the Due Process Clause
does not protect all rights—only life, liberty, and property.
Thus, the frst step in any due process analysis is to deter-
mine whether the right that the individual asserts falls
within one of these three categories. See Board of Regents
of State Colleges v. Roth, 408 U. S. 564, 570–571 (1972). If
it does not, the “requirements” of due process do not
“apply.” Ibid.
   By seeking to execute Gutierrez and to imprison him until
his execution, Texas undoubtedly seeks to deprive Gutierrez
of his life and liberty. Yet, Gutierrez rightly does not base
his due process claim on either of these deprivations, because
he has received far more than the process required to justify
them. Under our precedents, Texas must conduct a trial
Page Proof Pending Publication
before it can imprison or execute a person as punishment for
a crime. See Herrera v. Collins, 506 U. S. 390, 398–399
(1993). But, the “State is not required by the Federal Con-
stitution to provide . . . a right to appellate review.” Griffn
v. Illinois, 351 U. S. 12, 18 (1956) (plurality opinion); accord,
id., at 21 (Frankfurter, J., concurring in judgment); McKane
v. Durston, 153 U. S. 684, 687 (1894). Nor need it provide
“[p]ostconviction relief,” which “is even further removed
from the criminal trial.” Pennsylvania v. Finley, 481 U. S.
551, 556–557 (1987). Texas thus gave Gutierrez at his 1999
trial all the process necessary to imprison and execute him.
The ensuing quarter century of direct and collateral review
has been additional process above the constitutional foor.
   Gutierrez instead asserts that he has a distinct “ `liberty
interest' ” in Texas's “state-created right to postconviction”
relief. Ante, at 314. In Gutierrez's view, part of the “lib-
erty” that Texas prisoners enjoy under the Fourteenth
Amendment is a right to obtain release pursuant to Texas's
habeas statute, which the State takes away every time its
                       Cite as: 606 U. S. 305 (2025)                   325

                          Thomas, J., dissenting

courts deny habeas relief. Thus, Gutierrez contends, if
Texas law does not afford prisoners suffcient procedural
rights to bolster their habeas petitions—such as, in his case,
access to DNA testing—the State has deprived them of lib-
erty without the due process of law.2
   Gutierrez bases his asserted interest on this Court's deci-
sion in District Attorney's Offce for Third Judicial Dist. v.
Osborne, 557 U. S. 52 (2009). There, the Court concluded
that a prisoner has a “postconviction liberty interest” under
the Due Process Clause if state law grants him “an entitle-
ment . . . to prove his innocence even after a fair trial has
proved otherwise.” Id., at 67–68.

                                    II
  The Fourteenth Amendment does not protect Gutierrez's
asserted “liberty interest.” As originally understood, “lib-
erty” in the Fourteenth Amendment likely referred only to
Page Proof Pending Publication
freedom from physical restraint. It did not include entitle-

   2
     Gutierrez also claims that executive clemency is a “liberty interest”
that he cannot be denied without access to DNA testing. But, “noncapital
defendants do not have a liberty interest in traditional state executive
clemency.” District Attorney's Offce for Third Judicial Dist. v. Osborne,
557 U. S. 52, 67 (2009); see Connecticut Bd. of Pardons v. Dumschat, 452
U. S. 458, 464 (1981). In Ohio Adult Parole Authority v. Woodard, 523
U. S. 272 (1998), Chief Justice Rehnquist concluded for a plurality of the
Court that the same is true of capital defendants, because trial and sen-
tencing extinguish the defendant's “interest in not being executed in ac-
cord with his sentence.” Id., at 281. When applying for clemency, the
“defendant in effect accepts the fnality of the death sentence for purposes
of adjudication, and appeals for clemency as a matter of grace.” Id., at
282. Justice O'Connor, in contrast, left open the possibility that “some
minimal procedural safeguards apply to clemency proceedings,” such that
a due process violation “might” occur if “a state offcial fipped a coin to
determine whether to grant clemency.” Id., at 289 (opinion concurring in
part and concurring in judgment). But, even if Justice O'Connor's view
is correct, Gutierrez plainly cannot rely on it to establish a due process
violation. DNA testing is not necessary to make the Texas clemency
process less arbitrary than a coin fip.
326                GUTIERREZ v. SAENZ

                    Thomas, J., dissenting

ments to government-created benefts. This Court's con-
trary precedent stems from a conscious, policy-based rejec-
tion of the Due Process Clause's original meaning.

                             A
   The original meaning of “liberty” in the Fourteenth
Amendment was likely far narrower than our precedents
currently hold. The term originally appears to have re-
ferred only to freedom from physical restraint. But, in the
Lochner era, the Court began to hold that “liberty” includes
fundamental rights generally. See Lochner v. New York,
198 U. S. 45 (1905). This Court has since adhered to that
broader meaning.
   As with any legal text, we must construe the Fourteenth
Amendment according to the ordinary meaning of its terms
at the time of its enactment. Gibbons v. Ogden, 9 Wheat. 1,
188–189 (1824); T. Cooley, Constitutional Limitations 55
Page Proof Pending Publication
(1868). We may not defer to “demonstrably erroneous”
precedents that are inconsistent with the Amendment's orig-
inal meaning. Gamble v. United States, 587 U. S. 678, 717–
718 (2019) (Thomas, J., concurring).
   When the Fourteenth Amendment was adopted in 1868,
its Due Process Clause was understood to embody an “old
. . . principle” dating back to Magna Carta, the great 13th-
century charter of English liberties. Munn v. Illinois, 94
U. S. 113, 123–124 (1877). Magna Carta provided that a
“free man” may not be “prosecute[d],” “imprisoned,” or “de-
stroyed” except “by the law of the land.” Magna Carta, ch.
39 (1215), in A. Howard, Magna Carta: Text and Commen-
tary 43 (1964). A century later, a statute interpreting this
“law of the land” provision stated that “no Man” shall be
“imprisoned” or “put to Death, without being brought in An-
swer by due Process of the Law.” 28 Edw. III, c. 3 (1354);
see also 1 E. Coke, The Second Part of the Institutes of
the Laws of England 50 (1642) (interpreting “by the Law of
the Land” to be equivalent to “by due Process of the Com-
mon law”).
                   Cite as: 606 U. S. 305 (2025)            327

                     Thomas, J., dissenting

   Blackstone referred to Magna Carta's “law of the land”
provision as protecting the three “absolute rights of every
Englishman”: the “right of personal security,” including
“life”; “the right of personal liberty”; and “the right of
private property.” 1 W. Blackstone, Commentaries on
the Laws of England 123, 125 (1765) (Blackstone). This for-
mulation “heavily” infuenced the founding generation of
America. Obergefell v. Hodges, 576 U. S. 644, 724 (2015)
(Thomas, J., dissenting). Many early state constitutions
contained provisions “that replicated Magna Carta's lan-
guage, but were modifed to refer specifcally to `life, liberty,
or property.' ” Ibid., and n. 3 (collecting examples). And,
the Fifth Amendment similarly prohibited the Federal Gov-
ernment from depriving any person “of life, liberty, or prop-
erty, without due process of law.”
   “Liberty” in the Fifth Amendment likely refers only to
freedom from physical restraint. Blackstone defned “the
Page Proof Pending Publication
right of personal liberty” as “the power of loco-motion, of
changing situation, or removing one's person to whatsoever
place one's own inclination may direct; without imprisonment
or restraint, unless by due course of law.” 1 Blackstone 130.
Following Blackstone, “[s]tate decisions interpreting [state
due process] provisions between the founding and the ratif-
cation of the Fourteenth Amendment almost uniformly con-
strued the word `liberty' to refer only to freedom from physi-
cal restraint.” Obergefell, 576 U. S., at 724–725 (Thomas, J.,
dissenting) (citing C. Warren, The New “Liberty” Under the
Fourteenth Amendment, 39 Harv. L. Rev. 431, 441–445 (1926)
(Warren)). In light of this history, “it is hard to see how
the `liberty' protected by the [Fifth Amendment] could be
interpreted to include anything broader.” 576 U. S., at 725
(Thomas, J., dissenting).
   “If the Fifth Amendment uses `liberty' in this narrow
sense, then the Fourteenth Amendment likely does as well.”
Ibid. When the language of a provision “is obviously trans-
planted from another legal source, it brings the old soil with
it.” Taggart v. Lorenzen, 587 U. S. 554, 560 (2019) (internal
328                     GUTIERREZ v. SAENZ

                         Thomas, J., dissenting

quotation marks omitted). Applying that well-established
principle, this Court has long recognized the Fourteenth
Amendment's due process protections as having “the same
sense” as the Fifth Amendment's. Hurtado v. California,
110 U. S. 516, 534–535 (1884); accord, Slaughter-House Cases,
16 Wall. 36, 80–81 (1873); Hibben v. Smith, 191 U. S. 310, 325
(1903); Malinski v. New York, 324 U. S. 401, 415 (1945) (opin-
ion of Frankfurter, J.).3
  It was not until the Lochner era that this Court adopted
a broader understanding of “liberty.” During that period,
stretching from 1897 to 1937, this Court relied on the “legal
fction” of “substantive” due process to invalidate disfavored
social and economic legislation by States. McDonald v. Chi-
cago, 561 U. S. 742, 811 (2010) (Thomas, J., concurring in part
and concurring in judgment). Under that fction, the Due
Process Clauses forbade all government infringement on
“certain `fundamental' liberty interests . . . , no matter what
Page Proof Pending Publication
process is provided.” Reno v. Flores, 507 U. S. 292, 302
(1993). To make the fction work, the Court reinterpreted
the Clauses' guarantee of “ `process' ” to encompass “sub-
stance,” a notion that “strains credulity for even the most
casual user of words.” McDonald, 561 U. S., at 811 (opinion
of Thomas, J.).

  3
    Some decisions of this Court, while recognizing the general principle
that the Fifth and Fourteenth Amendments' Due Process Clauses should
be read together, have left open the possibility “that questions may arise
in which different constructions and applications of [the Clauses] may be
proper.” French v. Barber Asphalt Paving Co., 181 U. S. 324, 328 (1901).
Even assuming that caveat is correct, however, reading “liberty” in the
Fourteenth Amendment to mean fundamental rights generally, see infra
this page and 329, would appear to render the Fourteenth Amendment so
broad that it would destroy the general rule that the Fifth and Fourteenth
Amendments should be read coextensively. And, even if “liberty” in the
Fourteenth Amendment were entirely decoupled from its meaning in the
Fifth Amendment, I am aware of nothing showing that the term was un-
derstood to encompass government entitlements before the 1970s. See
infra, at 331–334.
                   Cite as: 606 U. S. 305 (2025)             329

                      Thomas, J., dissenting

   The Court's embrace of substantive due process also re-
quired it to jettison the concept of “liberty” as only freedom
from restraint, so that it could encompass other rights that
the Court deemed “fundamental.” In Allgeyer v. Louisi-
ana, 165 U. S. 578 (1897), this Court's frst substantive due
process decision under the Fourteenth Amendment, the
Court for the frst time broadened the defnition of “liberty”
to include the freedom of contract. Id., at 589; see Warren
445–449 (tracing the interpretation of “liberty” from the
Fourteenth Amendment's ratifcation to Allgeyer). By the
height of the Lochner era, the Court had stretched the term
to cover “those privileges long recognized at common law as
essential to the orderly pursuit of happiness by free men.”
Meyer v. Nebraska, 262 U. S. 390, 399 (1923). These privi-
leges included “the right of the individual to contract, to en-
gage in any of the common occupations of life, to acquire
useful knowledge, to marry, establish a home and bring up

Page Proof Pending Publication
children,” and “to worship God according to the dictates of
his own conscience.” Ibid.
   This Court eventually repudiated Lochner's muscular ver-
sion of substantive due process—at least for economic rights.
See Ferguson v. Skrupa, 372 U. S. 726, 730 (1963); West Coast
Hotel Co. v. Parrish, 300 U. S. 379 (1937). But, the Court
continues to treat Meyer's defnition of “liberty” as authori-
tative. E. g., Roth, 408 U. S., at 572.

                                B
  Gutierrez's claim of a state-created “liberty interest” in ob-
taining post-conviction relief is inconsistent with the original
understanding of “liberty.” From the founding through the
Lochner era, “liberty” was understood to be a natural, pre-
political right. Such an understanding is fundamentally in-
compatible with a “right” bestowed by the government.
  Blackstone squarely framed life, liberty, and property as
natural rights that existed before government. In an ac-
count “heavily infuenced” by the political theories of John
330                 GUTIERREZ v. SAENZ

                      Thomas, J., dissenting

Locke, Obergefell, 576 U. S., at 726–727, n. 4 (Thomas, J.,
dissenting), Blackstone explained that, in the state of nature,
every man has the “power of acting as [he] thinks ft, without
any restraint or control.” 1 Blackstone 121. When man
“enters into society, [he] gives up a part of his natural lib-
erty” to enjoy the rest of it in security. Ibid. Thus, the
liberty that each man enjoys as “a member of society, is no
other than natural liberty so far restrained by human laws
. . . as is necessary and expedient for the general advantage
of the publick.” Ibid. This includes “the absolute rights”
of life, liberty, and property, which exist in the “state of na-
ture, and which every man is intitled to enjoy whether out
of society or in it.” Id., at 119 (emphasis deleted). In other
words, according to Blackstone, life, liberty, and property are
rights that predate government and that were not surren-
dered when government was established; they are not enti-
tlements that the government can bestow by positive law.
Page Proof Pending Publication
   Founding-era Americans shared this understanding of lib-
erty. The Lockean “idea of civil liberty as natural liberty
constrained by human law” “permeated the 18th-century po-
litical scene in America.” Obergefell, 576 U. S., at 726–728
(Thomas, J., dissenting). For instance, the Virginia Decla-
ration of Rights of 1776—“the frst of the colonial bills of
rights,” Klopfer v. North Carolina, 386 U. S. 213, 225
(1967)—proclaimed that “all men . . . by nature” possess the
“inherent rights” of “life,” “liberty,” and “property,” which
they retain “when they enter into a state of society.” § I, in
1 Milestone Documents in American History 154 (P. Finkel-
man ed. 2008) (Finkelman). Similarly, the Declaration of In-
dependence asserts that the “unalienable Rights” of “Life,
Liberty, and the pursuit of Happiness” come from the “Cre-
ator,” and that, “to secure these rights, Governments are
instituted among Men.” ¶2.
   The understanding of liberty as a natural right persisted
until well after the enactment of the Fourteenth Amend-
ment. Even as this Court expanded the notion of “liberty”
                   Cite as: 606 U. S. 305 (2025)            331

                     Thomas, J., dissenting

in the Lochner era, it remained faithful to the idea of liberty
as “individual freedom from governmental action, not as a
right to a particular governmental entitlement.” Oberge-
fell, 576 U. S., at 726 (Thomas, J., dissenting). None of the
liberties enumerated in Meyer, for instance, could be charac-
terized as state-created benefts. See 262 U. S., at 399. To
the contrary, when interpreting the Due Process Clauses, the
Court distinguished between rights inherent to the individ-
ual and privileges established by the government. The
Court recognized, for example, that a prisoner's statutory
entitlement to early release on parole was a “privilege” that
“comes as an act of grace to one convicted of a crime,” not
a right protected by the Due Process Clauses. Escoe v.
Zerbst, 295 U. S. 490, 492–493 (1935).
   In short, entitlements established by the government can-
not be “liberty” under the Due Process Clause of the Four-
teenth Amendment. Gutierrez thus has no “liberty inter-

Page Proof Pending Publication
est” in Texas's state-created right to post-conviction relief.

                                C
   Gutierrez rests the legitimacy of his due process claim on
Osborne, which concluded that a prisoner has a “ `liberty in-
terest' ” when state law gives him “an entitlement . . . to
prove his innocence even after a fair trial has proved other-
wise.” 557 U. S., at 67. But, Osborne did not base this con-
clusion on the original meaning of “liberty” in the Four-
teenth Amendment. It instead relied on a line of cases
ultimately tracing back to Goldberg v. Kelly, 397 U. S. 254
(1970), where this Court relied on policy considerations to
redefne “property” to include government entitlements.
   Scholars generally agree that the term “property” in the
Due Process Clauses originally referred only to those inter-
ests traditionally recognized as property at common law.
See, e. g., 1 K. Hickman & R. Pierce, Administrative Law
§ 7.4, pp. 903–904 (7th ed. 2024); G. Lawson, Federal Adminis-
trative Law 350 (1998); L. Tribe, American Constitutional
332                 GUTIERREZ v. SAENZ

                     Thomas, J., dissenting

Law § 10–8, pp. 680–681 (2d ed. 1988). Property at common
law did not include entitlements to government benefts.
See 2 Blackstone 16–19, 384–399; J. Kent, Commentaries on
American Law 324–330, 613–614 (W. Browne ed. 1894)
(Kent). And, consistent with their general view of civil lib-
erties, Americans at the founding and in the early Republic
viewed property—like liberty—as a natural, pre-political
right. See, e. g., Virginia Declaration of Rights, § I, in
Finkelman 154; Calder v. Bull, 3 Dall. 386, 388–389 (1798)
(opinion of Chase, J.); H. Baldwin, A General View of the
Origin and Nature of the Constitution and Government of
the United States 136 (1837); Kent 203.
   The understanding of property as a natural right per-
sisted through the ratifcation of the Fourteenth Amend-
ment. After the Civil War, this Court held that a statute-of-
limitations defense was not “property” within the meaning
of the Constitution because it “is the creation of conventional
Page Proof Pending Publication
law,” not a “natural right.” Campbell v. Holt, 115 U. S. 620,
629 (1885). And, state-court decisions in the years leading
up to and immediately following the Amendment's ratifca-
tion continued to recognize property as a natural right.
See, e. g., People v. Quant, 12 How. Pr. 83, 89 (NY Sup. Ct.
1855); Sherman v. Buick, 32 Cal. 241, 249 (1867); Munn v.
People, 69 Ill. 80, 96 (1873), aff'd, 94 U. S. 113 (1877).
   Consistent with this view, “it has traditionally been held”
that the Due Process Clauses do not apply where it is “possi-
ble to characterize [the asserted] private interest . . . as a
mere privilege subject to the [government's] plenary power.”
Cafeteria & Restaurant Workers v. McElroy, 367 U. S. 886,
895 (1961). Thus, from the antebellum period to the 1960s,
this Court consistently recognized that government employ-
ment, veterans' benefts, admission to the country as an
alien, and other government-created entitlements are not
property or otherwise cognizable interests under the Due
Process Clauses. See, e. g., United States ex rel. Knauff v.
Shaughnessy, 338 U. S. 537, 542 (1950); Oceanic Steam Nav.
                    Cite as: 606 U. S. 305 (2025)             333

                      Thomas, J., dissenting

Co. v. Stranahan, 214 U. S. 320, 340–343 (1909); Buttfeld v.
Stranahan, 192 U. S. 470, 497 (1904); Taylor v. Beckham, 178
U. S. 548, 576 (1900); Crenshaw v. United States, 134 U. S.
99, 104 (1890); United States v. Teller, 107 U. S. 64, 68 (1883);
Butler v. Pennsylvania, 10 How. 402, 416 (1851); Kendall v.
United States ex rel. Stokes, 12 Pet. 524, 592–593 (1838).
   In the 1960s, Professor Charles Reich of the Yale Law
School published two articles proposing a radical reinterpre-
tation of the concept of property. See Individual Rights and
Social Welfare: The Emerging Legal Issues, 74 Yale L. J.
1245 (1965) (Individual Rights); The New Property, 73 Yale
L. J. 733 (1964) (The New Property). Taking direct aim at
the Framers' understanding, Reich argued that “[p]roperty
is not a natural right but a deliberate construction by soci-
ety” that could be redefned to meet contemporary social
needs. Id., at 771. In his view, the rise of “the welfare
state” and the dependence it fostered meant that “each man
Page Proof Pending Publication
cannot be wholly the master of his own destiny.” Id., at 786.
Thus, he concluded, to protect the now-dependent citizenry
from arbitrary government power, the legal system must
“mak[e government] benefts into rights” akin to traditional
property rights. Ibid. In other words, “[w]e must create a
new property.” Id., at 787.
   This Court embraced Reich's vision in 1970, holding that
“welfare benefits” are property under the Fourteenth
Amendment's Due Process Clause because they “are a mat-
ter of statutory entitlement for persons qualifed to receive
them.” Goldberg, 397 U. S., at 261–262. The Court dis-
missed any distinction between “a `privilege' and . . . a
`right,' ” and did not attempt to ground its conclusion in the
text or history of the Due Process Clause. Id., at 262 (some
internal quotation marks omitted). The Court instead gave
a sociological justifcation, “simply highlight[ing] the social
importance of `entitlements,' which had come to make up
`[m]uch of the existing wealth in this country,' and which only
the poor had been theretofore unable to effectively enforce.”
334                  GUTIERREZ v. SAENZ

                       Thomas, J., dissenting

Williams v. Reed, 604 U. S. 168, 182, n. (2025) (Thomas, J.,
dissenting); see Goldberg, 397 U. S., at 262, and n. 8 (citing
Individual Rights 1255; The New Property).
   Soon after Goldberg's radical redefnition of “property” to
include government-created entitlements, this Court rede-
fned “liberty” along similar lines. The Court held that, in
at least some circumstances, the denial of parole triggered
the Due Process Clause because “a person's liberty is equally
protected, even when the liberty itself is a statutory creation
of the State.” Wolff v. McDonnell, 418 U. S. 539, 558 (1974);
accord, Meachum v. Fano, 427 U. S. 215, 226 (1976). To jus-
tify this shift, the Court relied on “the accepted due process
analysis as to property.” Wolff, 418 U. S., at 557–558; ac-
cord, Meachum, 427 U. S., at 226 (citing Goldberg, 397 U. S.
254); see also Evitts v. Lucey, 469 U. S. 387, 400–401 (1985)
(citing Goldberg, 397 U. S., at 262).
   As with property, the Court's redefnition of “liberty” was
Page Proof Pending Publication
a conscious break with the past. The Court rejected the
inquiry of “whether [a] parolee's liberty is a `right' or a `privi-
lege' ” as “hardly useful any longer.” Morrissey v. Brewer,
408 U. S. 471, 482 (1972) (emphasis added). It expressly re-
pudiated its earlier case law holding that probation, as “an
`act of grace,' ” triggers no due process protections. See
Gagnon v. Scarpelli, 411 U. S. 778, 782, n. 4 (1973) (quoting
Escoe, 295 U. S., at 492). And, seemingly to obfuscate the
awkwardness of referring to a government-created entitle-
ment as “liberty,” the Court began to speak instead of “lib-
erty interests.” Kenosha v. Bruno, 412 U. S. 507, 515 (1973)
(internal quotation marks omitted). Although it is now
standard terminology in due process litigation, the phrase
did not appear in the United States Reports before Goldberg.
   Osborne relied on this line of cases to recognize a “liberty
interest” in post-conviction procedures. Invoking the lan-
guage of Goldberg, the Court asserted that a prisoner has a
“liberty interest” in a State's post-conviction procedures if
those procedures confer “an entitlement . . . to prove his
                         Cite as: 606 U. S. 305 (2025)                       335

                            Thomas, J., dissenting

innocence” after trial. 557 U. S., at 67 (emphasis added).
And, to establish that an entitlement of this kind can give
rise to a viable due process claim, the Court cited Connecti-
cut Bd. of Pardons v. Dumschat, 452 U. S. 458, 463 (1981),
and Wolff, 418 U. S., at 556–558, both of which relied on this
Court's post-Goldberg redefnition of “property.” 4 See 557
U. S., at 68.
   Osborne thus cannot support Gutierrez's asserted “liberty
interest.” We may, consistent with the judicial power, defer
to earlier decisions that “apply traditional tools of construc-
tion and arrive at different,” but reasonable, “interpretations
of legal texts.” Gamble, 587 U. S., at 721 (Thomas, J., con-
curring). But, Osborne rests on nothing more than Gold-
berg's abandonment of the Due Process Clause's original
meaning.
                               III
   We should correct the error we made in Osborne, which
Page Proof Pending Publication
seriously undermines States' interests in fnality and in pro-
viding relief to compelling claims of actual innocence. At
the very least, we should cease fnding novel ways to revive
due process challenges to post-conviction DNA testing pro-
cedures, as the Court does today.
   In enacting Chapter 64, Texas has voluntarily chosen to
prioritize claims of actual innocence at a signifcant cost to
its interest in fnality. Thanks in no small part to decisions
of this Court, capital cases today are routinely plagued by
decades-long delays between sentencing and execution, with
much of the litigation concerning convoluted procedural is-
sues having little or nothing to do with the guilt or innocence
of the defendant. See Baze v. Rees, 553 U. S. 35, 69–70
  4
    Wolff invoked “the accepted due process analysis as to property” to
hold that a “statutory right to good time” credits constituted a liberty
interest. 418 U. S., at 557–558. Dumschat relied on Wolff and Meachum
v. Fano, 427 U. S. 215, 226 (1976), to establish that a “ `state-created right' ”
can be a cognizable liberty interest. 452 U. S., at 463. Meachum cited
Goldberg for that point. 427 U. S., at 226.
336                  GUTIERREZ v. SAENZ

                      Thomas, J., dissenting

(2008) (Alito, J., concurring); id., at 92 (Scalia, J., concurring
in judgment). This delay undermines the “important inter-
est” that both “the State and the victims of crime have . . .
in the timely enforcement of a sentence.” Hill v. McDon-
ough, 547 U. S. 573, 584 (2006). In spite of these interests,
Texas has willingly decided to make freestanding actual-
innocence claims cognizable on post-conviction review and to
create a process for obtaining DNA testing to support such
claims. In this respect, Texas is more generous to capital
defendants than the Federal Government, which offers
no statutory mechanism for raising a freestanding actual-
innocence claim. See Herrera, 506 U. S., at 400.
   By recognizing a “liberty interest” in Texas's post-
conviction procedures, however, this Court has converted
those procedures from a means of vindicating compelling
claims of actual innocence into a tool for obstruction. In ad-
dition to trial, direct appeal, and multiple rounds of collateral
Page Proof Pending Publication
review in state and federal court, Texas must now prevail
in yet another arena—§ 1983 litigation challenging its DNA
testing procedures—before it can carry out its lawfully im-
posed sentences. See Rev. Stat. § 1979, 42 U. S. C. § 1983.
And, given the novelty of this litigation, such suits give rise
to a host of diffcult threshold justiciability questions that
must be resolved before a federal court can reach the merits
of the due process challenge, much less before a state court
can resolve the prisoner's claim of actual innocence.
   We need look no further than this case. Twenty-six years
after the brutal murder of Escolastica Harrison, this Court
stayed Gutierrez's impending execution. 603 U. S. 937
(2024). Why? Not because Gutierrez had made a compel-
ling allegation of innocence. Rather, the Court stayed the
execution to decide whether Gutierrez has standing to raise a
due process challenge to Texas's post-conviction procedures.
There is every reason to think that the ultimate claim of
actual innocence on which Gutierrez's case rests is baseless.
The key premise that Gutierrez hopes that DNA testing will
                       Cite as: 606 U. S. 305 (2025)                   337

                          Thomas, J., dissenting

establish—that he was not inside Harrison's home when she
was stabbed to death with a pair of screwdrivers—is contra-
dicted by his own confession, to say nothing of the unani-
mous statements of his accomplices. See post, at 339–340
(Alito, J., dissenting). The TCCA has held three times that
Gutierrez would likely still have been convicted of capital
murder as an accomplice even if he could prove that he had
not personally been inside Harrison's home. See post, at
343–344. And, in Gutierrez's most recent motion for DNA
testing, the trial court explicitly found that Gutierrez had
made the motion “for the purpose of unreasonably delaying
the execution of [his] sentence.” App. 655a. In short,
Texas could reasonably determine that the need for fnality
outweighed the upsides of giving Gutierrez additional proc-
ess. Yet, because this Court has found a “liberty interest”
where none exists, that judgment must be thwarted until
this additional multiyear front of litigation reaches its conclu-

Page Proof Pending Publication
sion. If this is what States can expect when they create
new post-conviction avenues for raising actual-innocence
claims, they may well conclude that doing so is not worth
the cost.5
                         *     *      *
  Gutierrez's suit rests on a non-existent “liberty interest.”
The Due Process Clause protects an individual's natural lib-
erty from government interference. It does not guarantee
entitlements to government benefts, like Texas's voluntarily
adopted post-conviction procedures. By intervening to re-
vive this suit, the Court facilitates precisely the “unjustifed

   5
     Our two earlier cases addressing due process challenges to Texas's
DNA testing procedures followed a similar pattern. In both cases, the
Court intervened long after sentencing to address threshold procedural
issues in the petitioners' federal due process suits. See Reed, 598 U. S.,
at 232–233 (addressing the timeliness of petitioner's due process suit 25
years after sentencing); Skinner v. Switzer, 562 U. S. 521, 525 (2011) (ad-
dressing the availability of § 1983 as a cause of action 16 years after
sentencing).
338                 GUTIERREZ v. SAENZ

                      Alito, J., dissenting

delay” that it is supposed to prevent in capital cases. Buck-
lew v. Precythe, 587 U. S. 119, 150 (2019). That is a misuse
of our discretionary certiorari jurisdiction. I respectfully
dissent.

  Justice Alito, with whom Justice Thomas and Justice
Gorsuch join, dissenting.
   The Court and I agree on one thing: we should decide this
case based on the test adopted in Reed v. Goertz, 598 U. S.
230, 234 (2023). After that, however, the majority veers
sharply off course. First, it blatantly alters the Reed test.
See ante, at 309, 315, 317. Second, it then has the audacity
to criticize the Fifth Circuit for applying the real Reed test.
See ante, at 316. Third, it ignores critical differences be-
tween the situation in Reed and the situation here. See ante,
at 316–318. Fourth, it paints a misleading picture of underly-
ing facts and Gutierrez's decades-long litigation campaign.

Page Proof Pending Publication
See ante, at 309–314. Fifth, it fails to recognize the limited
scope of the declaratory judgment at issue. See ante, at 316.
And sixth, it ignores lawful and binding Texas law regarding
the facts that may be considered when a prisoner seeks DNA
testing. See ante, at 317.
                                I
                               A
                               1
   Because the majority paints a misleading picture of the
facts and prior proceedings in this case, I begin by setting
the record straight. In 1999, Gutierrez was convicted and
sentenced to death for the brutal murder of Escolastica Har-
rison, an 85-year-old woman who lived in a mobile home park
in Brownsville, Texas, with her nephew Avel Cuellar. See
Ex parte Gutierrez, 337 S. W. 3d 883, 886 (Tex. Crim. App.
2011). As a result of his friendship with Cuellar, Gutierrez
became acquainted with Harrison and occasionally ran er-
rands for her. Ibid. Cuellar, Gutierrez, and other friends
                     Cite as: 606 U. S. 305 (2025)                 339

                         Alito, J., dissenting

gathered to drink behind Harrison's home—and Cuellar,
while inebriated, revealed that Harrison kept her entire life
savings (more than $600,000) in her home because she
distrusted banks. See Gutierrez v. Stephens, 2013 WL
12092544, *1 (SD Tex., Oct. 3, 2013); Ex parte Gutierrez, 337
S. W. 3d, at 886.
   When Gutierrez heard this, he hatched a plan to break
into the mobile home and steal the money. Id., at 886. He
recruited two accomplices—Rene Garcia and Pedro Gracia—
and on September 5, 1998, the three men went to Harrison's
trailer home to execute the plan. Ibid. By the time they
left the scene, Harrison had been beaten and stabbed 13
times in her face and neck with two different instruments.
See id., at 887, and n. 2. When Cuellar came home that
night, he reported discovering his elderly aunt's dead body
face-down in a pool of blood. Id., at 886.
   Several witnesses told detectives that they had seen Gu-
Page Proof Pending Publication
tierrez at the mobile home park on the day of the murder.
Ibid.; see Gutierrez v. Stephens, No. 1:09–cv–00022 (SD Tex.,
July 30, 2012), ECF Doc. 23–96, pp. 22–23. Detectives vis-
ited Gutierrez's home but were told he was not there.
Ex parte Gutierrez, 337 S. W. 3d, at 886. The next day,
Gutierrez voluntarily appeared at the police station and
made the frst of three conficting statements. Ibid. He
told detectives that on the day of the murder, he was driving
with a friend far away from the mobile home park. Ibid.;
see 93 F. 4th 267, 269 (CA5 2024). This alibi fell through,
however, when the friend told a conficting story. Ex parte
Gutierrez, 337 S. W. 3d, at 886. In addition, Garcia and
Gracia confessed to involvement in the crime, named Gutier-
rez as an accomplice, and said he was inside the mobile home
when Harrison was killed.1 Id., at 891; ECF Doc. 2–2, at 2.
Based on these statements and other evidence, Gutierrez

  1
   These statements were not admitted at trial. See Ex parte Gutierrez,
337 S. W. 3d, at 891.
340                     GUTIERREZ v. SAENZ

                           Alito, J., dissenting

was arrested. Ex parte Gutierrez, 337 S. W. 3d, at 887;
ECF Doc. 2–2, at 2.
   At the police station, Gutierrez agreed to give a second
statement. Id., at 2. Abandoning his earlier story, he ad-
mitted that he had planned to “ `rip off' ” Harrison, but he
claimed that he had not wanted to murder her. Ex parte
Gutierrez, 337 S. W. 3d, at 887. He told the police he had
been waiting at a park when Garcia and Gracia carried out
the scheme. Ibid. When they later met, he asserted, Gar-
cia was holding a screwdriver covered in blood and said he
had killed Harrison. Ibid.
   The following day, Gutierrez gave his third conficting
statement. Ibid. In a signed confession, he said that Gar-
cia was supposed to lure Harrison out of her home so that
Gutierrez could enter through the back of the trailer and
steal the money, but when Harrison saw Gutierrez enter her
home, Garcia knocked her out and began to stab her with

Page Proof Pending Publication
a screwdriver. Ibid. Gutierrez admitted that both he and
Garcia were armed with screwdrivers during the robbery.
Gutierrez, 2013 WL 12092544, *2. Gutierrez said that he
took the money while Garcia was stabbing Harrison and that
Gracia drove everyone away from the scene. Ibid. The
State of Texas then charged Gutierrez with capital murder
committed in the course of a robbery. Ibid.
                                    2
  Gutierrez moved to suppress his signed confession, ar-
guing that it was coerced and that the police continued to
question him after he had invoked his right to counsel and
his right to remain silent. See id., at *20. After conduct-
ing a hearing at which Gutierrez and two police offcers testi-
fed, the judge denied the motion and issued detailed fndings
of fact.2 Ibid.; see also ECF Doc. 23–66, at 47–125.
  2
   After the hearing, the judge initially denied the suppression motion
orally, but after Gutierrez appealed, the case was remanded, at the State's
request, for the issuance of written findings. Guti er rez, 2013 WL
                      Cite as: 606 U. S. 305 (2025)                 341

                          Alito, J., dissenting

  Gutierrez appealed, but the TCCA affrmed. See Gutier-
rez, 2013 WL 12092544, *21.

                                   3
   At trial, the State's theory was that Gutierrez was guilty
of murder either as a principal or a party to the crime. Ex
parte Gutierrez, 337 S. W. 3d, at 888. The State relied on
Texas's “law of parties,” under which “[a] person is crimi-
nally responsible as a party to an offense if the offense is
committed . . . by the conduct of another for which he is
criminally responsible.” Tex. Penal Code Ann. § 7.01(a)
(West 2021). Because Gutierrez had admitted to participat-
ing in the robbery, the State argued that he could be found
guilty of murder even if he was not the one who delivered
the fatal blows. See ECF Doc. 23–102, at 69–70.
   Gutierrez's defense offered a version of events that dif-
fered from all three of Gutierrez's prior stories. The new
Page Proof Pending Publication
account was that Cuellar had fatally stabbed Harrison. Gu-
tierrez, 2013 WL 12092544, *3. The defense “intimated that
the police had manufactured Gutierrez's statements” and
criticized the police for conducting a shoddy investigation.
Ibid. The jury found Gutierrez guilty.
   At the penalty phase of the trial, the State presented evi-
dence that Gutierrez had a long history of crime and vio-
lence, including burglaries, assault on a police offcer, and
threats to kill an assistant district attorney and a prison
guard. Ibid. The jury found (1) that Gutierrez posed a
“continuing threat to society,” (2) that he had “intended to
kill the deceased or . . . anticipated that a human life would
be taken,” and (3) that any mitigating circumstance were in-
suffcient to warrant a sentence of life imprisonment without
parole. ECF Doc. 23–108, at 45–48; ECF Doc. 23–109, at 4–

 12092544, *20–*21. Gutierrez then took a second appeal, and the Texas
Court of Criminal Appeals (TCCA) affrmed. Gutierrez v. Stephens,
No. 1:09–cv–00022 (Jan. 26, 2009), ECF Doc. 2–2, pp. 2–4; see Gutierrez,
2013 WL 12092544, *21.
342                 GUTIERREZ v. SAENZ

                      Alito, J., dissenting

5; see Tex. Code Crim. Proc. Ann., Art. 37.071, §§ 2(b), (e)(1)
(Vernon 2006). Based on these fndings, the judge imposed
a sentence of death.
   Gutierrez appealed and argued, among many other things,
that his confession should have been suppressed, but the
TCCA affrmed his conviction and sentence. See Ex parte
Gutierrez, 337 S. W. 3d, at 888; ECF Doc. 19, at 58–60.

                               B
   The end of direct appellate review was just the start of a
new litigation saga spanning 23 years (and counting). After
the conclusion of direct appellate review in 2002, Gutierrez
fled multiple petitions for state and federal post-conviction
relief, none of which has been successful. See 93 F. 4th, at
269–270. And Gutierrez has told us that he intends to fle
yet another petition for state post-conviction relief. See
Brief for Petitioner 40–41.
Page Proof Pending Publication
   Among the many claims that Gutierrez has advanced in
post-trial litigation, the claim involved here—that he is enti-
tled to DNA testing of items found at the murder scene—has
a prominent place. At trial, however, his counsel declined
to request DNA testing. Ex parte Gutierrez, 337 S. W. 3d,
at 897. As recounted by the TCCA, “the record affrma-
tively shows that DNA testing was available to appellant
before trial,” but “defense counsel apparently did not have
testing performed on those same items because of sound
trial strategy.” Ibid. (emphasis added). Instead of risking
what testing might reveal, counsel “used the fact that the
Brownsville Police Department failed to test the evidence
containing biological DNA evidence to argue the lack of in-
vestigation and the existence of reasonable doubt during the
trial.” Id., at 896. The lack of testing fgured prominently
in his cross-examination of prosecution witnesses and was
repeatedly raised during summation. Id., at 896–897, and
n. 45.
                      Cite as: 606 U. S. 305 (2025)                   343

                          Alito, J., dissenting

   The decision to forgo DNA testing at trial did not pay off,
so after his conviction, Gutierrez changed course and de-
manded testing in post-conviction proceedings. Chapter 64
of the Texas Code of Criminal Procedure governs such re-
quests, and Gutierrez fled his frst Chapter 643 motion in
2010. See 93 F. 4th, at 269. He sought testing of: (1) a
blood sample taken from Harrison; (2) a blood-stained shirt
belonging to Cuellar; (3) nail scrapings from Harrison; (4)
blood samples collected from Cuellar's bathroom, from a rain-
coat located in or just outside Cuellar's bedroom, and from
the sofa in the front room of the home; and (5) a loose hair
recovered from Harrison's fnger. Ex parte Gutierrez, 337
S. W. 3d, at 888. According to Gutierrez, the testing would
show that he had not entered Harrison's house and would
“support his position that he neither murdered Mrs. Har-
rison nor anticipated her murder.” Ibid.
   The trial court denied this motion, and the TCCA affrmed.
Page Proof Pending Publication
Id., at 888–889, 901–902. The TCCA explained that Chapter
64 authorizes post-conviction DNA testing only when the re-
sults would affect the applicant's conviction, not his sentence.
Id., at 899–901. And in any event, it explained, favorable
DNA results would not undermine the jury's guilty verdict
because they would not “make it less probable” that Gutier-
rez planned and participated in the crime. Id., at 901. Nor,
it added, would such results affect Gutierrez's eligibility for
the death penalty because “the record facts satisfy the En-
mund/Tison culpability requirements that he played a major
role in the underlying robbery and that his acts showed a
reckless indifference to human life.” Ibid.4

  3
    The majority refers to this provision as “Article 64,” but because the
lower courts consistently refer to the provision as “Chapter 64” and the
associated motions for DNA testing as “Chapter 64 motions,” I use that
terminology here.
  4
    See Enmund v. Florida, 458 U. S. 782, 797 (1982); Tison v. Arizona,
481 U. S. 137, 157–158 (1987).
344                 GUTIERREZ v. SAENZ

                      Alito, J., dissenting

  Gutierrez fled additional Chapter 64 motions for DNA
testing in June 2019 and July 2021, but the trial court denied
those motions, and each time the TCCA affrmed on the same
grounds. Gutierrez v. State, 2020 WL 918669, *6–*9 (Feb.
26, 2020) (per curiam); App. 477a–479a.

                               C
   This brings us to the latest chapter—Gutierrez's current
suit. In September 2019, Gutierrez sued Cameron County
District Attorney Luis Saenz and other Texas offcials in fed-
eral court under Rev. Stat. § 1979, 42 U. S. C. § 1983. See
Complaint in Gutierrez v. Saenz, No. 1:19–cv–00185 (SD
Tex., Sept. 26, 2019), ECF Doc. 1. Gutierrez asserted sev-
eral facial and as-applied constitutional challenges to Chap-
ter 64, including a Fourteenth Amendment due process
claim, a First Amendment access-to-courts claim, and an
Eighth Amendment cruel-and-unusual-punishment claim.
Page Proof Pending Publication
See ibid.
   The District Court rejected almost all of Gutierrez's
claims, but the court held that Chapter 64 is unconstitutional
insofar as it allows a defendant to seek post-conviction DNA
testing to challenge his conviction but not his sentence. 565
F. Supp. 3d 892, 910–911 (SD Tex. 2021). The District Court
entered a partial declaratory judgment for Gutierrez on that
ground but did not issue the injunction Gutierrez had sought.
Ibid.; see 2020 WL 12771965, *6 (SD Tex., June 2, 2020) (de-
nying Gutierrez's request for a “preliminary and permanent
injunction” requiring Saenz to turn over the requested evi-
dence (internal quotation marks omitted)). The State ap-
pealed, but Gutierrez did not cross-appeal, so the only issue
before the Fifth Circuit was whether Gutierrez was entitled
to a declaratory judgment on the one constitutional claim
accepted by the District Court.
   The Fifth Circuit did not reach the merits of that claim
because it held that Gutierrez lacked standing. Our test for
Article III standing, set out in Lujan v. Defenders of Wild-
                   Cite as: 606 U. S. 305 (2025)             345

                       Alito, J., dissenting

life, 504 U. S. 555, 560 (1992), has three prongs, and the Fifth
Circuit found that Gutierrez failed the third prong—that is,
the court found that Gutierrez could not show that his
claimed injury (lack of DNA testing) was “ `likely' ” to be
redressed by the relief that could at that point be awarded.
See 93 F. 4th, at 275; Lujan, 504 U. S., at 561 (“[I]t must be
likely, as opposed to merely speculative, that the injury will
be redressed by a favorable decision” (internal quotation
marks omitted)).
   In Reed v. Goertz, this Court recently applied this test
under related circumstances. As I will explain, there are
critical differences between that case and the case at hand,
but there are similarities that seem to have led the majority
astray. In Reed, a prisoner sentenced to death (Rodney
Reed) brought a § 1983 action against a district attorney and
sought a declaratory judgment that a particular provision
of Chapter 64 (its chain-of-custody provision, Tex. Code

Page Proof Pending Publication
Crim. Proc. Ann., Art. 64.03(a)(1)(A)(ii) (Vernon 2018)) vio-
lates the Constitution. This Court held that this declara-
tory judgment would redress the prisoner's deprivation of
DNA testing because it would “ `substantially' ” alter the
likelihood of the district attorney's ordering DNA testing.
Reed, 598 U. S., at 234.
   There were multiple issues in Reed, and the Court's discus-
sion of redressability was terse. In its entirety, it was as
follows:
      “[I]f a federal court concludes that Texas's post-
    conviction DNA testing procedures violate due process,
    that court order would eliminate the state prosecutor's
    justifcation for denying DNA testing. It is `substan-
    tially likely' that the state prosecutor would abide by
    such a court order. In other words, in `terms of our
    “standing” precedent, the courts would have ordered a
    change in a legal status,' and `the practical consequence of
    that change would amount to a signifcant increase in the
    likelihood' that the state prosecutor would grant access
346                     GUTIERREZ v. SAENZ

                          Alito, J., dissenting

      to the requested evidence and that Reed therefore
      `would obtain relief that directly redresses the injury
      suffered.' ” Ibid. (emphasis added; citation omitted).5
   The Court held that the prisoner satisfed this test. In
other words, the Court was persuaded that if he got the de-
claratory judgment he wanted, it was “substantially likely”
that the district attorney would order testing.
   The Fifth Circuit faithfully applied this test in its decision
below, taking into account the particular facts of Gutierrez's
case. It noted that the TCCA has repeatedly held that Gu-
tierrez would still be responsible for the murder under the
law of parties and would still be death-penalty eligible even
if DNA testing provided the results he wanted. 93 F. 4th,
at 272–273, 275. And it thus held that a decision in Gutier-
rez's favor on his constitutional claim would not make it sub-
stantially likely that the district attorney would release the

Page Proof Pending Publication
items for testing.6 Id., at 275.
   Today's decision, in contrast, fagrantly distorts the stand-
ard that Reed articulated. Indeed, the majority edits Reed's
critical language in a way that would draw rebuke if done
by an attorney in a brief fled in this Court. Reed's full dis-
cussion of redressability was quoted above. It consists of
three sentences. The majority's analysis is based entirely
on the frst sentence, which states: “ `[I]f a federal court con-
cludes that Texas's post-conviction DNA testing procedures

  5
    Reed advanced the theory that the Court adopted. His brief said that
“the question here is whether declaratory relief is likely to stop Goertz
from relying on the CCA's unconstitutional interpretation of Article 64 to
continue denying DNA testing. The answer is yes.” Reply Brief in
Reed v. Goertz, O. T. 2022, No. 21–442, p. 6.
  6
    The Fifth Circuit's assessment of the likely effect of the declaratory
judgment that Gutierrez sought was borne out when the TCCA affrmed
the denial of Gutierrez's third motion for DNA testing in June 2024—after
he had obtained the favorable declaratory judgment in the District Court.
See App. 467a–468a.
                   Cite as: 606 U. S. 305 (2025)             347

                       Alito, J., dissenting

violate due process,' that court order would redress [a pris-
oner's] injury by `eliminat[ing]' the state prosecutor's reli-
ance on Article 64 as a reason for denying DNA testing.”
See ante, at 319 (quoting Reed, 598 U. S., at 234). The sec-
ond and third sentences explain why the conclusion drawn in
the frst sentence was true in Reed's case: because the partic-
ular declaratory judgment that Reed sought (striking down
Chapter 64's chain-of-custody requirement) would “substan-
tially” increase the likelihood that the district attorney
would turn over the requested items for DNA testing. Id.,
at 234. But the majority pretends those sentences do not
exist.
   This distortion is bad enough, but to make matters worse,
the majority then criticizes the Fifth Circuit for “transform-
ing the redressability inquiry into a guess as to whether a
favorable court decision will in fact ultimately cause the
prosecutor to turn over the evidence.” Ante, at 318 (citing
Page Proof Pending Publication
93 F. 4th, at 274). In the majority's view, this Court appar-
ently should not consider whether the District Court's judg-
ment is likely to result in Gutierrez obtaining relief, but
whether the District Court's judgment removes just one of
the numerous “barrier[s] . . . between Gutierrez and the re-
quested testing.” Ante, at 319. The majority's new test
makes a hash of redressability. It appears that, under this
new test, the likelihood of redress is simply not relevant.
That most certainly is not what Reed held.
   Under the real Reed test, a plaintiff like Gutierrez must
show that a favorable decision on his constitutional claim is
“ `substantially likely' ” to prompt the district attorney to
allow DNA testing. 598 U. S., at 234. And in this case, un-
like in Reed, it is clear that the only relief that Gutierrez is
in a position to seek—reinstatement of the District Court's
declaratory judgment—is most unlikely to cause respondent
Saenz to order DNA testing. That is the conclusion that the
Fifth Circuit reached after carefully considering the relevant
348                     GUTIERREZ v. SAENZ

                           Alito, J., dissenting

facts, and that court was right. The following part of this
opinion will explain why.7
                             II
                                    A
   The Texas courts have provided three reasons why Gutier-
rez is not entitled to the testing he seeks. Any one of these,
if sound, would justify the denial of testing.
   First, both the trial court and the TCCA have held that
Gutierrez is not entitled to post-conviction DNA testing be-
cause such testing is unavailable under Chapter 64 to show
ineligibility for the death penalty, and Gutierrez could not
show by a preponderance of the evidence that he would not
have been convicted if he obtained favorable DNA test re-
sults. See Ex parte Gutierrez, 337 S. W. 3d, at 899–901;

  7
    According to the majority, the Fifth Circuit held that “Gutierrez lacked

Page Proof Pending Publication
`standing to bring this suit,' ” and it therefore concluded that Gutierrez
lacked standing to assert any of the claims he originally brought. See
ante, at 318. But just a few paragraphs after the part of the opinion in
which the language quoted by the majority appears, the opinion makes it
clear that its standing analysis focused on the one claim that was before
it. See 93 F. 4th 267, 271 (2024). That claim, the opinion noted, was that
“the state violates due process by permitting testing only if the evidence
could establish the prisoner would not have been convicted, thereby pre-
venting testing if resulting evidence would be relevant only to the sen-
tence.” Ibid. It then set out respondents' standing argument: “The de-
fendants allege that Gutierrez has no standing to make that claim.” Ibid.
(emphasis added). Thus, the Fifth Circuit's opinion is best understood as
holding only that affrmance of the claim that respondents appealed—that
Chapter 64 violates due process by barring defendants from seeking post-
conviction DNA testing to establish innocence of the death penalty—
would not redress Gutierrez's injury. And in any event, the redressability
inquiry had to be limited in that way because Gutierrez did not cross-
appeal the District Court's rejection of his other claims.
   Attempting to evade the cross-appeal rule, the majority characterizes
this case as one in which an appellee merely wishes to defend a judgment
whose “scope” did not reach the entirety of his claim. Ante, at 318, n. 3.
But the District Court did not simply fail to award Gutierrez complete
relief on the one claim on which he prevailed. Rather, it entered judg-
ment against him on different claims.
                    Cite as: 606 U. S. 305 (2025)             349

                        Alito, J., dissenting

Gutierrez, 2020 WL 918669, *5–*8. Second, both the trial
court and the TCCA have concluded that even favorable
DNA test results would not help Gutierrez because he would
still be responsible for the murder and would still satisfy
the Enmund/Tison Eighth Amendment requirements. See
Ex parte Gutierrez, 337 S. W. 3d, at 901; Gutierrez, 2020
WL 918669, *8. Third, the trial court found that Gutierrez's
application for DNA testing was made for the purpose of
delay. See id., at *5. This fnding of fact was not addressed
by the TCCA. See id., at *9.
   Contrary to the majority's suggestion, a favorable declara-
tory judgment respecting the frst of these reasons (Chapter
64 does not allow post-conviction DNA testing to prove ineli-
gibility for the death penalty) would not remove “the . . .
barrier Article 64 erected between Gutierrez and the re-
quested testing”; it would remove a barrier. Ante, at 319
(emphasis added). The District Court's declaratory judg-
Page Proof Pending Publication
ment regarding the constitutionality of Chapter 64's limited
grounds for post-conviction DNA testing, even if upheld by
the Fifth Circuit and this Court, would affect only that rea-
son and not the other two. And even if the TCCA did not
accept the trial court's fnding that Gutierrez fled his Chap-
ter 64 motion for the purpose of delay, the TCCA would al-
most certainly adhere to its prior decisions holding that fa-
vorable DNA results would not show that Gutierrez was
innocent of the crime or ineligible for the death penalty. As
a result, the only relief Gutierrez can possibly get in this case
would not result in court-ordered testing unless the TCCA
reverses course in an utterly unforeseeable way.
   Gutierrez argues, however, that even if the declaratory
judgment would not lead the Texas courts to grant DNA
testing, respondent Saenz would still have discretion to turn
over the items and might do so. See Brief for Petitioner 37–
38. But Gutierrez does not spell out why Saenz might do
that. His argument is based on rank speculation, and that
is not enough to support redressability. See Lujan, 504
U. S., at 561.
350                 GUTIERREZ v. SAENZ

                       Alito, J., dissenting

   Furthermore, nothing in the record suggests that there is
any likelihood that Saenz would do what Gutierrez wants.
The declaratory judgment would not require Saenz to order
testing. And he would know that the testing would be
pointless because even if the items were tested and revealed
what Gutierrez hopes for, the Texas courts would not disturb
his conviction or sentence.
   Not only is there no reason to think that Saenz—for some
unknown reason—might nevertheless order DNA testing,
but his conduct to date strongly suggests the opposite.
Even after the District Court issued its declaratory judg-
ment, he refused to order testing. And Gutierrez cannot ex-
plain why Saenz has steadfastly declined to allow testing
ever since. If he had any inclination to allow testing, he
could have done that at any point during this litigation—for
example, when Gutierrez fled his petition, when this Court
granted review, at any point during the briefng process, be-
Page Proof Pending Publication
fore or after argument, or yesterday. Not only has he not
done so, he has steadfastly maintained that he will not do so.
His position is that this case should be dismissed!
   Unable to explain why affrmance of the District Court's
declaratory judgment might change Saenz's mind, the major-
ity contends that a favorable decision on other constitutional
claims asserted in Gutierrez's complaint might do the trick.
And it criticizes the Fifth Circuit for “bas[ing] its assessment
of redressability on the declaratory judgment the District
Court later issued, rather than Gutierrez's complaint. ”
Ante, at 317.
   This reasoning is fundamentally wrong and, if allowed to
stand, will corrupt our Article III case law. Our standing
requirements “persist throughout all stages of litigation.”
Hollingsworth v. Perry, 570 U. S. 693, 705 (2013). “That
means that standing `must be met by persons seeking appel-
late review, just as it must be met by persons appearing in
courts of frst instance.' ” Ibid. (quoting Arizonans for Of-
fcial English v. Arizona, 520 U. S. 43, 64 (1997)). The con-
                   Cite as: 606 U. S. 305 (2025)           351

                       Alito, J., dissenting

stitutional claims on which the majority relies were rejected
by the District Court, and Gutierrez did not appeal that part
of the judgment. As a result, the best relief that Gutierrez
could now obtain in this case is an affrmance of the District
Court's declaratory judgment—and for the reasons already
discussed, that relief would not make DNA testing substan-
tially likely.
   For all these the reasons, Gutierrez cannot satisfy Reed's
real test for redressability.
                              B
   The majority treats this case as indistinguishable from
Reed, but that is not correct. An examination of the situa-
tion in that case provides a clear explanation for the Reed
Court's conclusion that its test for redressability was met.
And once that is understood, it is clear that the present case
is different.

Page    Proof      Pending          Publication
                              1
 Rodney Reed was convicted and sentenced to death for the
murder of Stacey Lee Stites, whose body was found partially
clothed and abandoned near a back country road. Reed v.
State, 541 S. W. 3d 759, 762 (Tex. Crim. App. 2017). Based
on an examination of her body, the police concluded that she
had been sexually assaulted and strangled with a belt found
at the scene. Ibid. DNA found on semen in Stites's body
matched Reed's genetic profle, and Reed was subsequently
arrested and charged with her murder. See id., at 763. At
trial, Reed argued (among other things) that he and Stites
were in a romantic relationship, that they had engaged in
consensual intercourse, and that the real culprit was Stites's
fance, Jimmy Fennell. Ex parte Reed, 271 S. W. 3d 698, 710
(Tex. Crim. App. 2008). The jury was not persuaded, and
Reed was convicted of capital murder and sentenced to
death. Id., at 712.
   Reed fled a Chapter 64 motion seeking DNA testing of
the belt and more than 35 other items that were found either
352                        GUTIERREZ v. SAENZ

                             Alito, J., dissenting

on Stites's body, at the scene of the crime, or in or near the
truck she shared with Fennell. Reed, 541 S. W. 3d, at 764–
765. Applying Chapter 64, the TCCA ruled out consider-
ation of evidence that fell into either of two categories. See
id., at 773. First, the TCCA refused to consider 21 items on
the ground that they did not satisfy Chapter 64's chain-of-
custody requirement.8 Id., at 769–770. Among these were
the strap and buckle from the belt with which Stites had
apparently been strangled. Id., at 769. Second, the TCCA
excluded other items on the ground that they were not rea-
sonably likely to contain biological material suitable for test-
ing. Id., at 772. Eight items remained for the TCCA to
consider, and fve of them were found in or near the truck,
not at the crime scene. Id., at 774–775. The court then
found that favorable results with respect to these eight items
would not have shown by a preponderance of the evidence
that Reed was not guilty. Id., at 773–777.

Page Proof Pending
              2    Publication
   Once the role that the chain-of-custody rule played in the
TCCA's analysis is understood, the support for this Court's
redressability fnding in Reed is easy to understand. The
declaratory judgment that Reed sought—striking down the
chain-of-custody rule—would have critically undermined the
TCCA's holding with respect to the potential impact of DNA
testing. Twenty-one additional items, including the belt,
could have been considered. If Fennell's DNA, but not
Reed's, had been detected on the belt and perhaps other
items found at the scene, that would have provided signif-
cant support for Reed's theory that Fennell was the mur-
derer. As a result, the declaratory judgment might well
have led to a state-court decision ordering DNA testing, and
that possibility would have given the district attorney a rea-
son to turn over the items even before such a state-court

  8
      See Tex. Code Crim. Proc. Ann., Art. 64.03(a)(1)(A)(ii).
                   Cite as: 606 U. S. 305 (2025)            353

                       Alito, J., dissenting

decision was handed down. The result would have been “a
signifcant increase in the likelihood that the state prosecu-
tor would grant access to the requested evidence.” Reed,
598 U. S., at 234 (emphasis added; internal quotation marks
omitted).
  In response, the majority argues that even if the chain of
custody rule were held to be unconstitutional, the district
attorney could have denied Reed's request for another rea-
son. Ante, at 318–319. That is true but beside the point.
Under this Court's decision in Reed, all that was required to
show redressability was “a signifcant increase in the likeli-
hood” that the district attorney would allow testing.

                                C
   Gutierrez's case presents a far different situation. Here,
the TCCA has held that, even if DNA testing failed to detect
Gutierrez's DNA and detected the presence of Cuellar's
Page Proof Pending Publication
DNA, Gutierrez could not establish that he was not guilty of
murder or that he is ineligible for a death sentence. The
TCCA noted that, since Cuellar lived with Harrison in the
same trailer home and was the person who found her dead
body, detecting his DNA on many items in the house would
not necessarily be incriminating. See Gutierrez, 2020 WL
918669, *7–*8. And more important, even if Cuellar's DNA
was detected on the most important items, such as the mate-
rial found under Harrison's fngernails, that would be of little
value to Gutierrez. It would suggest that Cuellar was one
of the individuals who stabbed Harrison—but that would not
affect Gutierrez's culpability or his sentence. Whether the
fatal blows were administered by Garcia, Gracia, Cuellar, or
some combination of these men, Gutierrez would still be
guilty of murder under the law of parties because he partici-
pated in the scheme. See Tex. Penal Code Ann. § 7.01(a).
And because he had reason to know that the execution of his
scheme could well result in the loss of life, he would still be
eligible for the death penalty. See Enmund v. Florida, 458
354                     GUTIERREZ v. SAENZ

                           Alito, J., dissenting

U. S. 782, 797 (1982); Tison v. Arizona, 481 U. S. 137, 157–
158 (1987). Thus, a favorable decision on Gutierrez's consti-
tutional argument would not bolster his challenge to his
sentence.
   Gutierrez responds that favorable DNA results might
change the TCCA's thinking because that court's holding on
the effect of DNA evidence did not take into account newly
discovered evidence that he wants to introduce. See Brief
for Petitioner 38–42. The majority suggests that, in assess-
ing whether Gutierrez's injury of not receiving DNA testing
is redressable, the Fifth Circuit should have considered Gu-
tierrez's assertion in his complaint that favorable DNA re-
sults along with the new evidence could render him ineligi-
ble for the death penalty. See ante, at 317. But the TCCA
has held that only evidence in the trial record may be consid-
ered in determining whether post-conviction DNA testing is
allowed. See Holberg v. State, 425 S. W. 3d 282, 285 (Tex.

Page Proof Pending Publication
Crim. App. 2014) (“[T]his Court will not consider post-trial
evidence when deciding whether or not the appellant has car-
ried her burden to establish by a preponderance of the evi-
dence that she would not have been convicted had exculpa-
tory results been obtained through DNA testing.”).9 We
have no basis for disregarding that limitation here. We are,
of course, bound by the TCCA's interpretation of Texas law,
and no question regarding the constitutionality of this fea-
ture of Texas law is now before us.10
  9
     A similar limitation applies in federal habeas proceedings. See Cullen
v. Pinholster, 563 U. S. 170, 181 (2011) (holding that habeas review of a
state-court conviction pursuant to 28 U. S. C. § 2254(d)(1) “is limited to
the record that was before the state court that adjudicated the claim on
the merits”).
   10
      This is so for three reasons. First, if Gutierrez wanted to challenge
those parts of the District Court's judgment, he needed to fle a cross-
appeal, but he did not do so. See, e. g., Northwest Airlines, Inc. v. County
of Kent, 510 U. S. 355, 364 (1994) (collecting cases). Second, the constitu-
tionality of this provision is not within the question on which we granted
                       Cite as: 606 U. S. 305 (2025)                    355

                           Alito, J., dissenting

   Not only does the majority's redressability analysis take
into account evidence that this binding state-law rule ex-
cludes, but the majority seems to think it is relevant that
“Gutierrez has long maintained that the police coerced him
into confessing that he was in Harrison's home on the night
of the murder.” Ante, at 310.
   The majority does not see ft to mention that the state
courts have defnitively rejected Gutierrez's argument that
the confession was coerced, that Texas law would almost cer-
tainly bar him from raising the same claim again in a post-
conviction proceeding,11 and that the federal habeas statute
would likewise bar consideration of the claim.12

                              *      *      *
  This decision's only practical effect will be to aid and abet
Gutierrez's efforts to run out the clock on the execution of

Page         Proof
certiorari. And
parties.
                third, the Pending           Publication
                           question was not briefed or argued by the

   11
      See Tex. Code Crim. Proc. Ann., Art. 11.071, §§ 5(a)(1)–(a)(3) (Vernon
Cum. Supp. 2024) (providing that a defendant can only fle a second habeas
petition challenging his death sentence if “the current claims and issues
have not been and could not have been presented previously,” no rational
juror would have found the defendant guilty but for a constitutional viola-
tion, or no rational juror would have answered one or more of the special
issues in the State's favor but for a constitutional violation); Ex parte
Blue, 230 S. W. 3d 151, 161 (Tex. Crim. App. 2007) (noting that a state
habeas applicant can only succeed on his claim under Art. 11.071, § 5(a)(3),
in the “rare” case when “constitutional error . . . so permeated the State's
evidence relevant to one of the special issues upon which it carries the
burden of proof that, absent the error, it is practically inconceivable that
any rational juror would actually answer the special issues in a way that
mandates the death penalty” (emphasis added)).
   12
      Because a claim regarding the admissibility of Gutierrez's confession
would constitute an attack on his conviction, it cannot be raised in a suit
under § 1983. See Heck v. Humphrey, 512 U. S. 477, 486–487 (1994). And
any attempt to raise the issue in a federal habeas petition would almost
certainly fail. See 28 U. S. C. §§ 2244(b)(2), 2254(d).
356                GUTIERREZ v. SAENZ

                      Alito, J., dissenting

his sentence. And if the decision is taken seriously as a
precedent on Article III standing, it will do serious damage.
I therefore dissent.




Page Proof Pending Publication
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

None

```

---

## GROUP: content/cases/Hernandez v. Mesa.md  (`case`, 5 assertions)

### content_page

```
---
title: Hernandez v. Mesa
type: case
citation: "589 U.S. 93 (2020)"
parallel_cite: "140 S. Ct. 735; 206 L. Ed. 2d 29"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2020
date_decided: ""
docket: 17-1678
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
  opinion_url: "https://www.courtlistener.com/opinion/9231296/hernandez-v-mesa/"
  cluster_id: 9231296
  opinion_id: null
  identity_checked: true
lake:
  record_id: Hernandez v. Mesa
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
tags:
  - case
  - bivens
  - cross-border-shooting
  - national-security
  - federal-officer-liability
  - section-1983
holding: "Bivens does not extend to a damages claim arising from a cross-border shooting: such a claim arises in a markedly new context with foreign-relations and national-security implications, and Congress's reluctance to create remedies for tortious conduct abroad counsels against implying a cause of action."
---

# Hernandez v. Mesa

*589 U.S. 93 (2020)* (No. 17-1678) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9231296 → opinion 9226104; quote string-matched to the CL opinion text 2026-07-07 (CL text carries S. Ct. star-pagination, 140 S. Ct. 735). S9 promotes. -->

## Background
Sergio Adrián Hernández Güereca, a fifteen-year-old Mexican national, was playing in the concrete culvert that separates El Paso, Texas, from Ciudad Juárez, Mexico. U.S. Border Patrol Agent Jesus Mesa, standing on the U.S. side, fired across the border and killed Hernández, who was on the Mexican side. Hernández's parents sued Mesa for damages under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging violations of the Fourth and Fifth Amendments. The [[Reading and Citing Cases#en-banc|en banc]] Fifth Circuit refused to recognize a *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedy, and the Supreme Court granted review.

## Issue
Whether *[[Bivens v. Six Unknown Named Agents|Bivens]]* should be extended to provide a damages remedy against a federal officer for a cross-border shooting.

## Rule
Recognizing an implied *[[Bivens v. Six Unknown Named Agents|Bivens]]* cause of action is disfavored, and separation-of-powers principles require caution before extending it to any "new context" — one that differs meaningfully from the three settings in which the Court has recognized a *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedy. A cross-border shooting is such a new context, and it carries foreign-relations and national-security implications that a court is ill-suited to weigh. The Court accordingly held: "Because of the distinctive characteristics of cross-border shooting claims, we refuse to extend *Bivens* into this new field." — 589 U.S. at 99. ^pin-99

## Application
A cross-border shooting is "by definition an international incident" affecting the interests of two nations, and such incidents are addressed through diplomatic channels (here, the U.S.–Mexico Border Violence Prevention Council and bilateral Human Rights Dialogue) that a judicially created damages remedy could disrupt. Congress, moreover, has been "notably hesitant" to create causes of action for tortious conduct abroad — declining, for instance, to make the Federal Tort Claims Act reach injuries in foreign countries. Because these special factors counsel hesitation, and no equally strong reason favors a judicial remedy, the Court refused to imply a *[[Bivens v. Six Unknown Named Agents|Bivens]]* action; it declined to decide the antecedent Fourth Amendment question.

## Conclusion
The judgment of the Fifth Circuit was **affirmed**. Alito, J., delivered the opinion of the Court; Thomas, J., joined by Gorsuch, J., concurred (urging reconsideration of *[[Bivens v. Six Unknown Named Agents|Bivens]]* itself); Ginsburg, J., joined by Breyer, Sotomayor, and Kagan, JJ., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Hernández v. Mesa* is part of the Court's line — with *[[Ziglar v. Abbasi]]* (2017) and *[[Egbert v. Boule]]* (2022) — sharply confining *[[Bivens v. Six Unknown Named Agents|Bivens]]* and refusing to extend implied damages remedies against federal officers into new, sensitive contexts.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Hernández v. Mesa*, 589 U.S. 93 (2020)](https://www.courtlistener.com/opinion/9231296/hernandez-v-mesa/) — pinpoint: 99 (holding, Opinion of the Court); CL text carries S. Ct. star-pagination (140 S. Ct. 735), the holding sitting just before the confirmed *741 page-label; quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "426aa499f0d1d8cb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "589 U.S. 93 (2020)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "140 S. Ct. 735; 206 L. Ed. 2d 29", "title": "Hernandez v. Mesa", "year": "2020"}}
{"assertion_id": "11a254bb93556641", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Hernandez v. Mesa"}}
{"assertion_id": "ce9be9eea563a56b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Bivens does not extend to a damages claim arising from a cross-border shooting: such a claim arises in a markedly new context with foreign-relations and national-security implications, and Congress's reluctance to create remedies for tortious conduct abroad counsels against implying a cause of action.", "title": "Hernandez v. Mesa"}}
{"assertion_id": "5238300079646ba9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Hernandez v. Mesa", "varies_by_point": "false"}}
{"assertion_id": "ea2983fa0777da6f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hernandez v. Mesa"}}
```

### lake record — Hernandez v. Mesa

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hernandez v. Mesa",
  "status": "under_review",
  "identity": {
    "case_name": "Hernandez v. Mesa",
    "case_name_short": "Hernandez",
    "case_name_full": "Jesus C. HERNANDEZ v. Jesus MESA, Jr.",
    "input_case_name": "Hernandez v. Mesa",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2020,
    "docket": "17-1678",
    "cluster_id": 9231296,
    "lead_opinion_id": 9226104,
    "sibling_ids": [],
    "absolute_url": "/opinion/9231296/hernandez-v-mesa/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "589 U.S. 93",
      "volume": "589",
      "reporter": "U.S.",
      "page": "93",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "140 S. Ct. 735",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 29",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "29",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "589 U.S. 93",
        "volume": "589",
        "reporter": "U.S.",
        "page": "93",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "140 S. Ct. 735",
        "volume": "140",
        "reporter": "S. Ct.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "206 L. Ed. 2d 29",
        "volume": "206",
        "reporter": "L. Ed. 2d",
        "page": "29",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "589 U.S. 93",
    "official_selection": {
      "court_class": "scotus",
      "selected": "589 U.S. 93",
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
    "date_created": "2026-07-06T12:09:39Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:09:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "hernandez-v-mesa--9231296",
      "to_record_id": "Hernandez v. Mesa",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Hernandez v. Mesa (truncated)

```
<opinion type="majority">
<author id="p-7">Justice ALITO delivered the opinion of the Court.</author>
<p id="p-8"><a class="page-label" data-citation-index="1" data-label="739" href="#p739" id="p739">*739</a>We are asked in this case to extend <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="0" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="1" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="2" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation> (1971), and create a damages remedy for a cross-border shooting. As we have made clear in many prior cases, however, the Constitution's separation of powers requires us to exercise caution before extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to a new "context," and a claim based on a cross-border shooting arises in a context that is markedly new. Unlike any previously recognized <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim, a cross-border shooting claim has foreign relations and national security implications. In addition, Congress has been notably hesitant to create claims based on allegedly tortious conduct abroad. Because of the distinctive characteristics of cross-border shooting claims, we refuse to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> into this new field.</p>
<p id="p-9">I</p>
<p id="p-10">The facts of this tragic case are set forth in our earlier opinion in this matter, <a class="page-label" data-citation-index="1" data-label="740" href="#p740" id="p740">*740</a><em>Hernández v.</em> <em>Mesa</em> , 582 U.S. ----, <extracted-citation case-ids="12605122" index="3" url="https://cite.case.law/s-ct/137/2003/"><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">137 S.Ct. 2003</a></span></extracted-citation>, <extracted-citation case-ids="12605122" index="4" url="https://cite.case.law/s-ct/137/2003/"><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">198 L.Ed.2d 625</a></span></extracted-citation> (2017) (<em>per curiam</em> ). Sergio Adrián Hernández Güereca, a 15-year-old Mexican national, was with a group of friends in a concrete culvert that separates El Paso, Texas, from Ciudad Juarez, Mexico. The border runs through the center of the culvert, which was designed to hold the waters of the Rio Grande River but is now largely dry. Border Patrol Agent Jesus Mesa, Jr., detained one of Hernández's friends who had run onto the United States' side of the culvert. After Hernández, who was also on the United States' side, ran back across the culvert onto Mexican soil, Agent Mesa fired two shots at Hernández; one struck and killed him on the other side of the border.</p>
<p id="p-11">Petitioners and Agent Mesa disagree about what Hernández and his friends were doing at the time of shooting. According to petitioners, they were simply playing a game, running across the culvert, touching the fence on the U.S. side, and then running back across the border. According to Agent Mesa, Hernández and his friends were involved in an illegal border crossing attempt, and they pelted him with rocks.<footnotemark>1</footnotemark></p>
<p id="p-12">The shooting quickly became an international incident, with the United States and Mexico disagreeing about how the matter should be handled. On the United States' side, the Department of Justice conducted an investigation. When it finished, the Department, while expressing regret over Hernández's death, concluded that Agent Mesa had not violated Customs and Border Patrol policy or training, and it declined to bring charges or take other action against him. Mexico was not and is not satisfied with the U.S. investigation. It requested that Agent Mesa be extradited to face criminal charges in a Mexican court, a request that the United States has denied.</p>
<p id="p-13">Petitioners, Hernández's parents, were also dissatisfied</p>
<p id="p-14">and therefore brought suit for damages in the United States District Court for the Western District of Texas. Among other claims, they sought recovery of damages under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , alleging that Mesa violated Hernández's Fourth and Fifth Amendment rights. The District Court granted Mesa's motion to dismiss, and the Court of Appeals for the Fifth Circuit sitting en banc has twice affirmed this dismissal.</p>
<p id="p-15">On the first occasion, the court held that Hernández was not entitled to Fourth Amendment protection because he was "a Mexican citizen who had no 'significant voluntary connection' to the United States" and "was on Mexican soil at the time he was shot." <em>Hernandez v. United States</em> , <extracted-citation case-ids="4182853" index="5" url="https://cite.case.law/f3d/785/117/#p119"><span class="citation" data-id="9807043"><a href="/opinion/2796556/jesus-hernandez-v-unknown-named-agents-et/" aria-description="Citation for case: Jesus Hernandez v. Unknown Named Agents, et">785 F.3d 117</a></span></extracted-citation>, 119 (C.A.5 2015) (<em>per curiam</em> ). It further concluded that Mesa was entitled to qualified immunity on petitioners' Fifth Amendment claim. <em><extracted-citation case-ids="4182853" index="6" url="https://cite.case.law/f3d/785/117/#p119"><span class="citation" data-id="9807043"><a href="/opinion/2796556/jesus-hernandez-v-unknown-named-agents-et/" aria-description="Citation for case: Jesus Hernandez v. Unknown Named Agents, et">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="4182853" index="6" url="https://cite.case.law/f3d/785/117/#p119"> at 120</extracted-citation>.</p>
<p id="p-16">After granting review, we vacated the Fifth Circuit's decision and remanded the case, instructing the court "to consider how the reasoning and analysis" of <em>Ziglar v.</em> <em>Abbasi</em> , 582 U.S. ----, <extracted-citation case-ids="12604999" index="7" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">137 S.Ct. 1843</a></span></extracted-citation>, <extracted-citation case-ids="12604999" index="8" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">198 L.Ed.2d 290</a></span></extracted-citation> (2017), our most recent explication of <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , "[might] bear on this case." <em><span class="citation" data-id="9876889"><a href="/opinion/4403795/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">Hernández</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 2006. We found it "appropriate for the Court of Appeals, rather than this Court, to address the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> question in the first instance." <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Ibid.</a></span></em> And with the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> issue unresolved, we thought it "imprudent" to resolve the "sensitive"</p>
<p id="p-17"><a class="page-label" data-citation-index="1" data-label="741" href="#p741" id="p741">*741</a>question whether the Fourth Amendment applies to a cross-border shooting. <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Ibid.</a></span></em> In addition, while rejecting the ground on which the Court of Appeals had held that Agent Mesa was entitled to qualified immunity, we declined to decide whether he was entitled to qualified immunity on a different ground or whether petitioners' claim was cognizable under the Fifth Amendment. <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.,</a></span></em> at ---- - ----, 137 S.Ct., at 2006-2008</p>
<p id="p-18">On remand, the en banc Fifth Circuit evaluated petitioners' case in light of <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> and refused to recognize a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim for a cross-border shooting. <extracted-citation case-ids="12516361" index="9" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d 811</a></span></extracted-citation> (C.A.5 2018). The court reasoned that such an incident presents a " 'new context' " and that multiple factors-including the incident's relationship to foreign affairs and national security, the extraterritorial aspect of the case, and Congress's "repeated refusals" to create a damages remedy for injuries incurred on foreign soil-counseled against an extension of <em>Bivens</em> . <extracted-citation case-ids="12516361" index="10" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d at 816</a></span>-823</extracted-citation>.</p>
<p id="p-19">We granted certiorari, 587 U.S. ----, <extracted-citation case-ids="12621056,12621057,12621058,12621059,12621060" index="11" url="https://cite.case.law/s-ct/139/2636/"><span class="citation multiple-matches"><a href="/c/S.Ct./139/2636/">139 S.Ct. 2636</a></span></extracted-citation>, <extracted-citation case-ids="12621056,12621186,12621058,12621061,12621063,12621227,12621228" index="12" url="https://cite.case.law/l-ed-2d/204/282/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/204/282/">204 L.Ed.2d 282</a></span></extracted-citation> (2019), and now affirm.</p>
<p id="p-20">II</p>
<p id="p-21">In <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="13" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="14" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="15" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation>, the Court broke new ground by holding that a person claiming to be the victim of an unlawful arrest and search could bring a Fourth Amendment claim for damages against the responsible agents even though no federal statute authorized such a claim. The Court subsequently extended <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to cover two additional constitutional claims: in <em>Davis v. Passman</em> , <extracted-citation case-ids="1532130" index="16" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. 228</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="17" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="18" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">60 L.Ed.2d 846</a></span></extracted-citation> (1979), a former congressional staffer's Fifth Amendment claim of dismissal based on sex, and in <em>Carlson v. Green</em> , <extracted-citation case-ids="6180250" index="19" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. 14</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="20" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="21" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">64 L.Ed.2d 15</a></span></extracted-citation> (1980), a federal prisoner's Eighth Amendment claim for failure to provide adequate medical treatment. After those decisions, however, the Court changed course.</p>
<p id="p-22"><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> , and <em><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">Carlson</a></span></em> were the products of an era when the Court routinely inferred "causes of action" that were "not explicit" in the text of the provision that was allegedly violated. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1855. As <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> recounted:</p>
<blockquote id="p-23">"During this '<em>ancien regime</em> ,' ... the Court assumed it to be a proper judicial function to 'provide such remedies as are necessary to make effective' a statute's purpose .... Thus, as a routine matter with respect to statutes, the Court would imply causes of action not explicit in the statutory text itself." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Ibid.</a></span></em> (quoting <em>Alexander v. Sandoval</em> , <extracted-citation case-ids="9301210" index="22" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">532 U.S. 275</a></span></extracted-citation>, 287, <extracted-citation case-ids="9301210" index="23" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation>, <extracted-citation case-ids="9301210" index="24" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">149 L.Ed.2d 517</a></span></extracted-citation> (2001) ; <em>J. I. Case Co. v. Borak</em> , <extracted-citation case-ids="6170359" index="25" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. 426</a></span></extracted-citation>, 433, <extracted-citation case-ids="6170359" index="26" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="27" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">12 L.Ed.2d 423</a></span></extracted-citation> (1964) ).</blockquote>
<p id="p-24"><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> extended this practice to claims based on the Constitution itself. 582 U.S., at ----, 137 S.Ct., at 1855 ; <em>Bivens</em> , <extracted-citation case-ids="12027206" index="28" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 402</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="29" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (Harlan, J., concurring in judgment) (Court can infer availability of damages when, "in its view, damages are necessary to effectuate" the "policy underpinning the substantive provisio[n]").</p>
<p id="p-25">In later years, we came to appreciate more fully the tension between this practice and the Constitution's separation of legislative and judicial power. The Constitution grants legislative power to Congress; this Court and the lower federal courts, by contrast, have only "judicial Power." Art. III, § 1. But when a court recognizes an implied claim for damages on the ground that doing so furthers the "purpose" of the law, the court risks arrogating legislative power. No law " 'pursues <a class="page-label" data-citation-index="1" data-label="742" href="#p742" id="p742">*742</a>its purposes at all costs.' " <em>American Express Co. v. Italian Colors Restaurant</em> , <extracted-citation case-ids="12698468" index="30" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">570 U.S. 228</a></span></extracted-citation>, 234, <extracted-citation case-ids="12698468" index="31" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">133 S.Ct. 2304</a></span></extracted-citation>, <extracted-citation case-ids="12698468" index="32" url="https://cite.case.law/us/570/228/#p234"><span class="citation" data-id="9515841"><a href="/opinion/903973/american-express-co-v-italian-colors-restaurant/" aria-description="Citation for case: American Express Co. v. Italian Colors Restaurant">186 L.Ed.2d 417</a></span></extracted-citation> (2013) (quoting <em>Rodriguez v. United States</em> , <extracted-citation case-ids="1131066" index="33" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">480 U.S. 522</a></span></extracted-citation>, 525-526, <extracted-citation case-ids="1131066" index="34" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">107 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="1131066" index="35" url="https://cite.case.law/us/480/522/#p525"><span class="citation" data-id="111840"><a href="/opinion/111840/rodriguez-v-united-states/" aria-description="Citation for case: Rodriguez v. United States">94 L.Ed.2d 533</a></span></extracted-citation> (1987) (<em>per curiam</em> )). Instead, lawmaking involves balancing interests and often demands compromise. See <em>Board of Governors, FRS v. Dimension Financial Corp.</em> , <extracted-citation case-ids="6205521" index="36" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">474 U.S. 361</a></span></extracted-citation>, 373-374, <extracted-citation case-ids="6205521" index="37" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">106 S.Ct. 681</a></span></extracted-citation>, <extracted-citation case-ids="6205521" index="38" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">88 L.Ed.2d 691</a></span></extracted-citation> (1986). Thus, a lawmaking body that enacts a provision that creates a right or prohibits specified conduct may not wish to pursue the provision's purpose to the extent of authorizing private suits for damages. For this reason, finding that a damages remedy is implied by a provision that makes no reference to that remedy may upset the careful balance of interests struck by the lawmakers. See <em><extracted-citation case-ids="6205521" index="39" url="https://cite.case.law/us/474/361/#p373"><span class="citation" data-id="111557"><a href="/opinion/111557/board-of-governors-of-the-federal-reserve-system-v-dimension-financial/" aria-description="Citation for case: Board of Governors of the Federal Reserve System v....">ibid.</a></span></extracted-citation></em></p>
<p id="p-26">This problem does not exist when a common-law court, which exercises a degree of lawmaking authority, fleshes out the remedies available for a common-law tort. Analogizing <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> to the work of a common-law court, petitioners and some of their <em>amici</em> make much of the fact that common-law claims against federal officers for intentional torts were once available. See, <em>e.g.</em> , Brief for Petitioners 10-20. But <em>Erie R. Co. v. Tompkins</em> , <extracted-citation case-ids="10687" index="40" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">304 U.S. 64</a></span></extracted-citation>, 78, <extracted-citation case-ids="10687" index="41" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">58 S.Ct. 817</a></span></extracted-citation>, <extracted-citation case-ids="10687" index="42" url="https://cite.case.law/us/304/64/#p78"><span class="citation" data-id="9418969"><a href="/opinion/103012/erie-railroad-v-tompkins/" aria-description="Citation for case: Erie Railroad v. Tompkins">82 L.Ed. 1188</a></span></extracted-citation> (1938), held that "[t]here is no federal general common law," and therefore federal courts today cannot fashion new claims in the way that they could before 1938. See <em>Alexander</em> , <extracted-citation case-ids="9301210" index="43" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">532 U.S. at 287</a></span></extracted-citation>, <extracted-citation case-ids="9301210" index="44" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation> (" 'Raising up causes of action where a statute has not created them may be a proper function for common-law courts, but not for federal tribunals' ").</p>
<p id="p-27">With the demise of federal general common law, a federal court's authority to recognize a damages remedy must rest at bottom on a statute enacted by Congress, see <em><extracted-citation case-ids="9301210" index="45" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">id.,</a></span></extracted-citation></em><extracted-citation case-ids="9301210" index="45" url="https://cite.case.law/us/532/275/#p287"> at 286</extracted-citation>, <extracted-citation case-ids="9301210" index="46" url="https://cite.case.law/us/532/275/#p287"><span class="citation" data-id="9795078"><a href="/opinion/2620697/alexander-v-sandoval/" aria-description="Citation for case: Alexander v. Sandoval">121 S.Ct. 1511</a></span></extracted-citation> ("private rights of action to enforce federal law must be created by Congress"), and no statute expressly creates a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy. Justice Harlan's <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> concurrence argued that this power is inherent in the grant of federal question jurisdiction, see <extracted-citation case-ids="12027206" index="47" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 396</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="48" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (majority opinion); <em><extracted-citation case-ids="12027206" index="49" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">id.</a></span></extracted-citation></em> , at 405, <extracted-citation case-ids="12027206" index="50" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (opinion of Harlan, J.), but our later cases have demanded a clearer manifestation of congressional intent, see <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ---- - ----, 137 S.Ct., at 1856-1858.</p>
<p id="p-28">In both statutory and constitutional cases, our watchword is caution. For example, in <em>Jesner v.</em> <em>Arab Bank, PLC</em> , 584 U.S. ----, ---- - ----, <extracted-citation case-ids="12611257" index="51" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct. 1386</a></span></extracted-citation>, 1391-1403, <extracted-citation case-ids="12611257" index="52" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">200 L.Ed.2d 612</a></span></extracted-citation> (2018) we expressed doubt about our authority to recognize any causes of action not expressly created by Congress. See also <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span>,</em> 582 U.S.<em>,</em> at ----, 137 S.Ct., at 1856 ("If the statute does not itself so provide, a private cause of action will not be created through judicial mandate"). And we declined to recognize a claim against a foreign corporation under the Alien Tort Statute. <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="53" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1408</a></span></extracted-citation>.</p>
<p id="p-29">In constitutional cases, we have been at least equally reluctant to create new causes of action. We have recognized that Congress is best positioned to evaluate "whether, and the extent to which, monetary and other liabilities should be imposed upon individual officers and employees of the Federal Government" based on constitutional torts. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1856. We have stated that expansion of <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> is "a 'disfavored' judicial activity," 582 U.S., at ----, 137 S.Ct., at 1857 (quoting <em>Ashcroft v. Iqbal</em> , <extracted-citation case-ids="3653744" index="54" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">556 U.S. 662</a></span></extracted-citation>, 675, <extracted-citation case-ids="3653744" index="55" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">129 S.Ct. 1937</a></span></extracted-citation>, <extracted-citation case-ids="3653744" index="56" url="https://cite.case.law/us/556/662/#p675"><span class="citation" data-id="9435339"><a href="/opinion/145875/ashcroft-v-iqbal/" aria-description="Citation for case: Ashcroft v. Iqbal">173 L.Ed.2d 868</a></span></extracted-citation> (2009) ), and have gone so far as to observe that if "the Court's three <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> cases [had] been ... decided today," it is doubtful that we would have <a class="page-label" data-citation-index="1" data-label="743" href="#p743" id="p743">*743</a>reached the same result, 582 U.S., at ----, 137 S.Ct., at 1856. And for almost 40 years, we have consistently rebuffed requests to add to the claims allowed under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> . See 582 U.S., at ----, 137 S.Ct., at 1863-1864 ; <em>Minneci v. Pollard</em> , <extracted-citation case-ids="12445441,12185990" index="57" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">565 U.S. 118</a></span></extracted-citation>, <extracted-citation case-ids="12445441,12185990" index="58" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">132 S.Ct. 617</a></span></extracted-citation>, <extracted-citation case-ids="12445441,12185990" index="59" url="https://cite.case.law/us/565/118/"><span class="citation" data-id="7268271"><a href="/opinion/7350292/minneci-v-pollard/" aria-description="Citation for case: Minneci v. Pollard">181 L.Ed.2d 606</a></span></extracted-citation> (2012) ; <em>Wilkie v. Robbins</em> , <extracted-citation case-ids="3573210" index="60" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">551 U.S. 537</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="61" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">127 S.Ct. 2588</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="62" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">168 L.Ed.2d 389</a></span></extracted-citation> (2007) ; <em>Correctional Services Corp. v. Malesko</em> , <extracted-citation case-ids="9107996" index="63" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. 61</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="64" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="65" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">151 L.Ed.2d 456</a></span></extracted-citation> (2001) ; <em>FDIC v. Meyer</em> , <extracted-citation case-ids="230419" index="66" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">510 U.S. 471</a></span></extracted-citation>, <extracted-citation case-ids="230419" index="67" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">114 S.Ct. 996</a></span></extracted-citation>, <extracted-citation case-ids="230419" index="68" url="https://cite.case.law/us/510/471/"><span class="citation" data-id="112931"><a href="/opinion/112931/federal-deposit-insurance-v-meyer/" aria-description="Citation for case: Federal Deposit Insurance v. Meyer">127 L.Ed.2d 308</a></span></extracted-citation> (1994) ; <em>Schweiker v. Chilicky</em> , <extracted-citation case-ids="1775175" index="69" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">487 U.S. 412</a></span></extracted-citation>, <extracted-citation case-ids="1775175" index="70" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">108 S.Ct. 2460</a></span></extracted-citation>, <extracted-citation case-ids="1775175" index="71" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">101 L.Ed.2d 370</a></span></extracted-citation> (1988) ; <em>United States v. Stanley</em> , <extracted-citation case-ids="28195" index="72" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. 669</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="73" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="74" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">97 L.Ed.2d 550</a></span></extracted-citation> (1987) ; <em>Chappell v. Wallace</em> , <extracted-citation case-ids="6187620" index="75" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">462 U.S. 296</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="76" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">103 S.Ct. 2362</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="77" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">76 L.Ed.2d 586</a></span></extracted-citation> (1983) ; <em>Bush v. Lucas</em> , <extracted-citation case-ids="6188608" index="78" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">462 U.S. 367</a></span></extracted-citation>, <extracted-citation case-ids="6188608" index="79" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">103 S.Ct. 2404</a></span></extracted-citation>, <extracted-citation case-ids="6188608" index="80" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">76 L.Ed.2d 648</a></span></extracted-citation> (1983).</p>
<p id="p-30">When asked to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , we engage in a two-step inquiry. We first inquire whether the request involves a claim that arises in a "new context" or involves a "new category of defendants." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="81" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 68</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="82" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. And our understanding of a "new context" is broad. We regard a context as "new" if it is "different in a meaningful way from previous <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> cases decided by this Court." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1859.</p>
<p id="p-31">When we find that a claim arises in a new context, we proceed to the second step and ask whether there are any " ' "special factors [that] counse[l] hesitation" ' " about granting the extension. <em>Id.</em> , at ----, 137 S.Ct., at 1857 (quoting <em>Carlson</em> , <extracted-citation case-ids="6180250" index="83" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. at 18</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="84" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, in turn quoting <em>Bivens</em> , <extracted-citation case-ids="12027206" index="85" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 396</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="86" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> ). If there are-that is, if we have reason to pause before applying <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> in a new context or to a new class of defendants-we reject the request.</p>
<p id="p-32">We have not attempted to "create an exhaustive list" of factors that may provide a reason not to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , but we have explained that "central to [this] analysis" are "separation-of-powers principles." <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857. We thus consider the risk of interfering with the authority of the other branches, and we ask whether "there are sound reasons to think Congress might doubt the efficacy or necessity of a damages remedy," <em>id.,</em> at ----, 137 S.Ct., at 1858, and "whether the Judiciary is well suited, absent congressional action or instruction, to consider and weigh the costs and benefits of allowing a damages action to proceed," <em>id.,</em> at ----, 137 S.Ct., at 1858</p>
<p id="p-33">III</p>
<p id="p-34">A</p>
<p id="p-35">The <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claims in this case assuredly arise in a new context. Petitioners contend that their Fourth and Fifth Amendment claims do not involve a new context because <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> and <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> involved claims under those same two amendments, but that argument rests on a basic misunderstanding of what our cases mean by a new context. A claim may arise in a new context even if it is based on the same constitutional provision as a claim in a case in which a damages remedy was previously recognized. Compare <em>Carlson</em> , <extracted-citation case-ids="6180250" index="87" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. at 16</a></span>-18</extracted-citation>, <extracted-citation case-ids="6180250" index="88" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation> (allowing <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy for an Eighth Amendment claim for failure to provide adequate medical treatment), with <em>Malesko</em> , <extracted-citation case-ids="9107996" index="89" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 71</a></span>-74</extracted-citation>, <extracted-citation case-ids="9107996" index="90" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation> (declining to create a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy in similar circumstances because the suit was against a private prison operator, not federal officials). And once we look beyond the constitutional provisions invoked in <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> , and the present case, it is glaringly obvious that petitioners' claims involve a new context, <em>i.e.</em> , one that is meaningfully different.</p>
<p id="p-36"><a class="page-label" data-citation-index="1" data-label="744" href="#p744" id="p744">*744</a><em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> concerned an allegedly unconstitutional arrest and search carried out in New York City, <extracted-citation case-ids="12027206" index="91" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 389</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="92" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> ; <em><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">Davis</a></span></em> concerned alleged sex discrimination on Capitol Hill, <extracted-citation case-ids="1532130" index="93" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. at 230</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="94" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>. There is a world of difference between those claims and petitioners' cross-border shooting claims, where "the risk of disruptive intrusion by the Judiciary into the functioning of other branches" is significant. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1860 ; see Parts III-B and III-C, <em>infra</em> .</p>
<p id="p-37">Because petitioners assert claims that arise in a new context, we must proceed to the next step and ask whether there are factors that counsel hesitation. As we will explain, there are multiple, related factors that raise warning flags.</p>
<p id="p-38">B</p>
<p id="p-39">The first is the potential effect on foreign relations. "The political branches, not the Judiciary, have the responsibility and institutional capacity to weigh foreign-policy concerns." <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="95" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation>. Indeed, we have said that "matters relating 'to the conduct of foreign relations ... are so exclusively entrusted to the political branches of government as to be largely immune from judicial inquiry or interference.' " <em>Haig v. Agee</em> , <extracted-citation case-ids="11722549" index="96" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">453 U.S. 280</a></span></extracted-citation>, 292, <extracted-citation case-ids="11722549" index="97" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">101 S.Ct. 2766</a></span></extracted-citation>, <extracted-citation case-ids="11722549" index="98" url="https://cite.case.law/us/453/280/#p292"><span class="citation" data-id="9428473"><a href="/opinion/110554/haig-v-agee/" aria-description="Citation for case: Haig v. Agee">69 L.Ed.2d 640</a></span></extracted-citation> (1981) (quoting <em>Harisiades v. Shaughnessy</em> , <extracted-citation case-ids="641171" index="99" url="https://cite.case.law/us/342/580/#p589"><span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/" aria-description="Citation for case: Harisiades v. Shaughnessy">342 U.S. 580</a></span></extracted-citation>, 589, <extracted-citation case-ids="641171" index="100" url="https://cite.case.law/us/342/580/#p589"><span class="citation" data-id="9420696"><a href="/opinion/104980/harisiades-v-shaughnessy/" aria-description="Citation for case: Harisiades v. Shaughnessy">72 S.Ct. 512</a></span></extracted-citation>, <extracted-citation index="101" url="https://cite.case.law/citations/?q=96%20L.%20Ed.%20586"><span class="citation no-link">96 L.Ed. 586</span></extracted-citation> (1952) ). "Thus, unless Congress specifically has provided otherwise, courts traditionally have been reluctant to intrude upon the authority of the Executive in [these matters]." <em>Department of Navy v. Egan</em> , <extracted-citation case-ids="601280" index="102" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">484 U.S. 518</a></span></extracted-citation>, 530, <extracted-citation case-ids="601280" index="103" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">108 S.Ct. 818</a></span></extracted-citation>, <extracted-citation case-ids="601280" index="104" url="https://cite.case.law/us/484/518/#p530"><span class="citation" data-id="9431176"><a href="/opinion/111990/department-of-the-navy-v-egan/" aria-description="Citation for case: Department of the Navy v. Egan">98 L.Ed.2d 918</a></span></extracted-citation> (1988). We must therefore be especially wary before allowing a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> remedy that impinges on this arena.</p>
<p id="p-40">A cross-border shooting is by definition an international incident; it involves an event that occurs simultaneously in two countries and affects both countries' interests. Such an incident may lead to a disagreement between those countries, as happened in this case.</p>
<p id="p-41">The United States, through the Executive Branch, which has " 'the lead role in foreign policy,' " <em>Medellín v. Texas</em> , <extracted-citation case-ids="3675774" index="105" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">552 U.S. 491</a></span></extracted-citation>, 524, <extracted-citation case-ids="3675774" index="106" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">128 S.Ct. 1346</a></span></extracted-citation>, <extracted-citation case-ids="3675774" index="107" url="https://cite.case.law/us/552/491/#p524"><span class="citation" data-id="9435251"><a href="/opinion/145822/medellin-v-texas/" aria-description="Citation for case: Medellin v. Texas">170 L.Ed.2d 190</a></span></extracted-citation> (2008) (alteration omitted), has taken the position that this incident should be handled in a particular way-namely, that Agent Mesa should not face charges in the United States nor be extradited to stand trial in Mexico. As noted, the Executive decided not to take action against Agent Mesa because it found that he "did not act inconsistently with [Border Patrol] policy or training regarding use of force." DOJ Press Release. We presume that Border Patrol policy and training incorporate both the Executive's understanding of the Fourth Amendment's prohibition of unreasonable seizures and the Executive's assessment of circumstances at the border. Thus, the Executive judged Agent Mesa's conduct by what it regards as reasonable conduct by an agent under the circumstances that Mesa faced at the time of the shooting, and based on the application of those standards, it declined to prosecute. The Executive does not want a Mexican criminal court to judge Agent Mesa's conduct by whatever standards would be applicable under Mexican law; nor does it want a jury in a <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> action to apply its own understanding of what constituted reasonable conduct by a Border Patrol agent under the circumstances of this case. Such a jury determination, the Executive claims, would risk the " ' "embarrassment of our government abroad" through "multifarious pronouncements by various departments on one question." ' " Brief for United States as <em>Amicus Curiae</em> 18 (quoting <em>Sanchez-Espinoza v. Reagan</em> , <extracted-citation case-ids="332853,3600966" index="108" url="https://cite.case.law/f2d/770/202/"><span class="citation" data-id="9473867"><a href="/opinion/457042/javier-sanchez-espinoza-v-ronald-wilson-reagan-president-of-the-united/" aria-description="Citation for case: Javier Sanchez-Espinoza v. Ronald Wilson Reagan,...">770 F.2d 202</a></span></extracted-citation>, 209 (C.A.D.C. 1985) (Scalia, J.)).</p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="745" href="#p745" id="p745">*745</a>The Government of Mexico has taken a different view of what should be done. It has requested that Agent Mesa be extradited for criminal prosecution in a Mexican court under Mexican law, and it has supported petitioners' <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> suit. In a brief filed in this Court, Mexico suggests that shootings by Border Patrol agents are a persistent problem and argues that the United States has an obligation under international law, specifically Article 6(1) of the International Covenant on Civil and Political Rights, Dec. 19, 1966, S. Treaty Doc. No. 95-20, 999 U. N. T. S. 174, to provide a remedy for the shooting in this case. Brief for Government of United Mexican States as <em>Amicus Curiae</em> 2, 20-22. Mexico states that it "has a responsibility to look after the well-being of its nationals" and that "it is a priority to Mexico to see that the United States provides adequate means to hold the agents accountable and to compensate the victims." <em><extracted-citation case-ids="332853,3600966" index="109" url="https://cite.case.law/f2d/770/202/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 3.</p>
<p id="p-43">Both the United States and Mexico have legitimate and important interests that may be affected by the way in which this matter is handled. The United States has an interest in ensuring that agents assigned the difficult and important task of policing the border are held to standards and judged by procedures that satisfy United States law and do not undermine the agents' effectiveness and morale. Mexico has an interest in exercising sovereignty over its territory and in protecting and obtaining justice for its nationals. It is not our task to arbitrate between them.</p>
<p id="p-44">In the absence of judicial intervention, the United States and Mexico would attempt to reconcile their interests through diplomacy-and that has occurred. The broad issue of violence along the border, the occurrence of crossborder shootings, and this particular matter have been addressed through diplomatic channels. In 2014, Mexico and the United States established a joint Border Violence Prevention Council, and the two countries have addressed cross-border shootings through the United States-Mexico bilateral Human Rights Dialogue.<footnotemark>2</footnotemark> Following the Justice Department investigation in the present case, the United States reaffirmed its commitment to "work with the Mexican government within existing mechanisms and agreements to prevent future incidents." DOJ Press Release.</p>
<p id="p-45">For these reasons, petitioners' assertion that their claims have "nothing to do with the substance or conduct of U.S. foreign ... policy," Brief for Petitioners 29, is plainly wrong.<footnotemark>3</footnotemark></p>
<p id="p-46">C</p>
<p id="p-47">Petitioners are similarly incorrect in deprecating the Fifth Circuit's conclusion <a class="page-label" data-citation-index="1" data-label="746" href="#p746" id="p746">*746</a>that the issue here implicates an element of national security.</p>
<p id="p-48">One of the ways in which the Executive protects this country is by attempting to control the movement of people and goods across the border, and that is a daunting task. The United States' border with Mexico extends for 1,900 miles, and every day thousands of persons and a large volume of goods enter this country at ports of entry on the southern border.<footnotemark>4</footnotemark> The lawful passage of people and goods in both directions across the border is beneficial to both countries.</p>
<p id="p-49">Unfortunately, there is also a large volume of illegal</p>
<p id="p-50">cross-border traffic. During the last fiscal year, approximately 850,000 persons were apprehended attempting to enter the United States illegally from Mexico,<footnotemark>5</footnotemark> and large quantities of drugs were smuggled across the border.<footnotemark>6</footnotemark> In addition, powerful criminal organizations operating on both sides of the border present a serious law enforcement problem for both countries.<footnotemark>7</footnotemark></p>
<p id="p-51">On the United States' side, the responsibility for attempting to prevent the illegal entry of dangerous persons and goods rests primarily with the U.S. Customs and Border Protection Agency, and one of its main responsibilities is to "detect, respond to, and interdict terrorists, drug smugglers and traffickers, human smugglers and traffickers, and other persons who may undermine the security of the United States." <extracted-citation index="110" url="https://cite.case.law/citations/?q=6%20U.S.C.%20%C2%A7%20211"><span class="citation no-link">6 U.S.C. § 211</span></extracted-citation>(c)(5). While Border Patrol agents often work miles from the border, some, like Agent Mesa, are stationed right at the border and have the responsibility of attempting to prevent illegal entry. For these reasons, the conduct of agents positioned at the border has a clear and strong connection to national security, as the Fifth Circuit understood. <extracted-citation case-ids="12516361" index="111" url="https://cite.case.law/f3d/885/811/"><span class="citation" data-id="8410662"><a href="/opinion/8439846/hernandez-v-mesa/" aria-description="Citation for case: Hernandez v. Mesa">885 F.3d at 819</a></span></extracted-citation>.</p>
<p id="p-52">Petitioners protest that " 'shooting people who are just walking down a street in Mexico' " does not involve national security, Brief for Petitioners 28, but that misses the point. The question is not whether national security requires such conduct-of course, it does not-but whether the Judiciary should alter the framework established by the political branches for addressing cases in which it is alleged that lethal force was unlawfully employed by an agent at the border. Cf. <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1861 (explaining that "[n]ational-security policy is the prerogative of the Congress and President").</p>
<p id="p-53">We have declined to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> where doing so would interfere with the <a class="page-label" data-citation-index="1" data-label="747" href="#p747" id="p747">*747</a>system of military discipline created by statute and regulation, see <em>Chappell</em> , <extracted-citation case-ids="6187620" index="112" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">462 U.S. 296</a></span></extracted-citation>, <extracted-citation case-ids="6187620" index="113" url="https://cite.case.law/us/462/296/"><span class="citation" data-id="110960"><a href="/opinion/110960/chappell-v-wallace/" aria-description="Citation for case: Chappell v. Wallace">103 S.Ct. 2362</a></span></extracted-citation> ; <em>Stanley</em> , <extracted-citation case-ids="28195" index="114" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. 669</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="115" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation>, and a similar consideration is applicable here. Since regulating the conduct of agents at the border unquestionably has national security implications, the risk of undermining border security provides reason to hesitate before extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> into this field. See <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1861 ("Judicial inquiry into the national-security realm raises 'concerns for the separation of powers' " (quoting <em>Christopher v. Harbury</em> , <extracted-citation case-ids="1254643" index="116" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">536 U.S. 403</a></span></extracted-citation>, 417, <extracted-citation case-ids="1254643" index="117" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">122 S.Ct. 2179</a></span></extracted-citation>, <extracted-citation case-ids="1254643" index="118" url="https://cite.case.law/us/536/403/#p417"><span class="citation" data-id="9434290"><a href="/opinion/121160/christopher-v-harbury/" aria-description="Citation for case: Christopher v. Harbury">153 L.Ed.2d 413</a></span></extracted-citation> (2002) )).</p>
<p id="p-54">D</p>
<p id="p-55">Our reluctance to take that step is reinforced by our survey of what Congress has done in statutes addressing related matters. We frequently "loo[k] to analogous statutes for guidance on the appropriate boundaries of judge-made causes of action." <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="119" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/#1403" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation> (opinion of Kennedy, J.). When foreign relations are implicated, it "is even more important ... 'to look for legislative guidance before exercising innovative authority over substantive law.' " <em><extracted-citation case-ids="12611257" index="120" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12611257" index="121" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1403</a></span></extracted-citation> (quoting <em>Sosa v. Alvarez-Machain</em> , <extracted-citation case-ids="5862480" index="122" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">542 U.S. 692</a></span></extracted-citation>, 726, <extracted-citation case-ids="5862480" index="123" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">124 S.Ct. 2739</a></span></extracted-citation>, <extracted-citation case-ids="5862480" index="124" url="https://cite.case.law/us/542/692/#p726"><span class="citation" data-id="9434694"><a href="/opinion/137006/sosa-v-alvarez-machain/" aria-description="Citation for case: Sosa v. Alvarez-Machain">159 L.Ed.2d 718</a></span></extracted-citation> (2004) ). Accordingly, it is "telling," <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1862, that Congress has repeatedly declined to authorize the award of damages for injury inflicted outside our borders.</p>
<p id="p-56">A leading example is <extracted-citation index="125" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>, which permits the recovery of damages for constitutional violations by officers acting under color of <em>state</em> law. We have described <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> as a "more limited" "federal analog" to § 1983. <em>Hartman v. Moore</em> , <extracted-citation case-ids="3275855" index="126" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 254, n. 2, <extracted-citation case-ids="3275855" index="127" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="128" url="https://cite.case.law/us/547/250/#p254"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006). It is therefore instructive that Congress chose to make § 1983 available only to "citizen[s] of the United States or other person[s] within the jurisdiction thereof." It would be "anomalous to impute ... a judicially implied cause of action beyond the bounds [Congress has] delineated for [a] comparable express caus[e] of action." <em>Blue Chip Stamps v. Manor Drug Stores</em> , <extracted-citation case-ids="541651" index="129" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">421 U.S. 723</a></span></extracted-citation>, 736, <extracted-citation case-ids="541651" index="130" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">95 S.Ct. 1917</a></span></extracted-citation>, <extracted-citation case-ids="541651" index="131" url="https://cite.case.law/us/421/723/#p736"><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">44 L.Ed.2d 539</a></span></extracted-citation> (1975). Thus, the limited scope of § 1983 weighs against recognition of the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> claim at issue here.</p>
<p id="p-57">Section 1983's express limitation to the claims brought by citizens and persons subject to United States jurisdiction is especially significant, but even if this explicit limitation were lacking, we would presume that § 1983 did not apply abroad. See <em>RJR Nabisco, Inc. v. European Community</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597929" index="132" url="https://cite.case.law/s-ct/136/2090/#p2100"><span class="citation" data-id="8137991"><a href="/opinion/8176209/rjr-nabisco-inc-v-european-cmty/" aria-description="Citation for case: RJR Nabisco, Inc. v. European Cmty.">136 S.Ct. 2090</a></span></extracted-citation>, 2100, <extracted-citation case-ids="12597929" index="133" url="https://cite.case.law/s-ct/136/2090/#p2100"><span class="citation" data-id="3214778"><a href="/opinion/3214884/rjr-nabisco-inc-v-european-community/" aria-description="Citation for case: RJR Nabisco, Inc. v. European Community">195 L.Ed.2d 476</a></span></extracted-citation> (2016) ("Absent clearly expressed congressional intent to the contrary, federal laws will be construed to have only domestic application"). We presume that statutes do not apply extraterritorially to "ensure that the Judiciary does not erroneously adopt an interpretation of U.S. law that carries foreign policy consequences not clearly intended by the political branches." <em>Kiobel v. Royal Dutch Petroleum Co.</em> , <extracted-citation case-ids="12697039" index="134" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">569 U.S. 108</a></span></extracted-citation>, 116, <extracted-citation case-ids="12697039" index="135" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">133 S.Ct. 1659</a></span></extracted-citation>, <extracted-citation case-ids="12697039" index="136" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">185 L.Ed.2d 671</a></span></extracted-citation> (2013) ; see also <em>EEOC v. Arabian American Oil Co.</em> , <extracted-citation case-ids="11318695" index="137" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">499 U.S. 244</a></span></extracted-citation>, 248, <extracted-citation case-ids="11318695" index="138" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">111 S.Ct. 1227</a></span></extracted-citation>, <extracted-citation case-ids="11318695" index="139" url="https://cite.case.law/us/499/244/#p248"><span class="citation" data-id="9432237"><a href="/opinion/112565/equal-employment-opportunity-commission-v-arabian-american-oil-co/" aria-description="Citation for case: Equal Employment Opportunity Commission v. Arabian...">113 L.Ed.2d 274</a></span></extracted-citation> (1991).</p>
<p id="p-58">If this danger provides a reason for caution when Congress has enacted a statute but has not provided expressly whether it applies abroad, we have even greater reason for hesitation in deciding whether to extend a judge-made cause of action beyond our borders. "[T]he danger of unwarranted judicial interference in the conduct of foreign policy is magnified" where "the question is not what Congress has <a class="page-label" data-citation-index="1" data-label="748" href="#p748" id="p748">*748</a>done but instead what courts may do." <em>Kiobel</em> , <extracted-citation case-ids="12697039" index="140" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">569 U.S. at 116</a></span></extracted-citation>, <extracted-citation case-ids="12697039" index="141" url="https://cite.case.law/us/569/108/#p116"><span class="citation" data-id="9506050"><a href="/opinion/858289/kiobel-v-royal-dutch-petroleum-co/" aria-description="Citation for case: Kiobel v. Royal Dutch Petroleum Co.">133 S.Ct. 1659</a></span></extracted-citation>. Where Congress has not spoken at all, the likelihood of impinging on its foreign affairs authority is especially acute.</p>
<p id="p-59">Congress's treatment of ordinary tort claims against federal officers is also revealing. As petitioners and their <em>amici</em> stress, the traditional way in which civil litigation addressed abusive conduct by federal officers was by subjecting them to liability for common-law torts. See Brief for Petitioners 10-17. For many years, such claims could be raised in state or federal court,<footnotemark>8</footnotemark> and this Court occasionally considered tort suits against federal officers for extraterritorial injuries. See, <em>e.g.</em> , <em>Mitchell v. Harmony</em> , <extracted-citation case-ids="3361041" index="142" url="https://cite.case.law/us/54/115/"><span class="citation" data-id="9416513"><a href="/opinion/86727/mitchell-v-harmony/" aria-description="Citation for case: Mitchell v. Harmony">13 How. 115</a></span></extracted-citation>, <extracted-citation case-ids="3361041" index="143" url="https://cite.case.law/us/54/115/"><span class="citation" data-id="9416513"><a href="/opinion/86727/mitchell-v-harmony/" aria-description="Citation for case: Mitchell v. Harmony">14 L.Ed. 75</a></span></extracted-citation> (1852) (affirming award in trespass suit brought by U.S. citizen against U.S. Army officer who seized personal property in Mexico during the Mexican-American war). After <em>Erie</em> , federal common-law claims were out, but we recognized the continuing viability of state-law tort suits against federal officials as recently as <em>Westfall v. Erwin</em> , <extracted-citation case-ids="602224" index="144" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">484 U.S. 292</a></span></extracted-citation>, <extracted-citation case-ids="602224" index="145" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">108 S.Ct. 580</a></span></extracted-citation>, <extracted-citation case-ids="602224" index="146" url="https://cite.case.law/us/484/292/"><span class="citation" data-id="111980"><a href="/opinion/111980/westfall-v-erwin/" aria-description="Citation for case: Westfall v. Erwin">98 L.Ed.2d 619</a></span></extracted-citation> (1988).</p>
<p id="p-60">In response to that decision, Congress passed the so-called Westfall Act, formally the Federal Employees Liability Reform and Tort Compensation Act of 1988, <extracted-citation index="147" url="https://cite.case.law/citations/?q=28%20U.S.C.%20%C2%A7%202679"><span class="citation no-link">28 U.S.C. § 2679</span></extracted-citation>. That Act makes the Federal Tort Claims Act (FTCA) "the exclusive remedy for most claims against Government employees arising out of their official conduct." <em>Hui v. Castaneda</em> , <extracted-citation case-ids="3582219,12448446" index="148" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">559 U.S. 799</a></span></extracted-citation>, 806, <extracted-citation case-ids="3582219,12448446" index="149" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">130 S.Ct. 1845</a></span></extracted-citation>, <extracted-citation case-ids="3582219,12448446" index="150" url="https://cite.case.law/us/559/799/"><span class="citation" data-id="145448"><a href="/opinion/145448/hui-v-castaneda/" aria-description="Citation for case: Hui v. Castaneda">176 L.Ed.2d 703</a></span></extracted-citation> (2010).<footnotemark>9</footnotemark> Thus, a person injured by a federal employee may seek recovery directly from the United States under the FTCA, but the FTCA bars "[a]ny claim arising in a foreign country." § 2680(k).<footnotemark>10</footnotemark> The upshot is that claims that would otherwise permit the recovery of damages are barred if the injury occurred abroad.</p>
<p id="p-61">Yet another example is provided by the Torture Victim Protection Act of 1991, note following <extracted-citation index="151" url="https://cite.case.law/citations/?q=28%20U.S.C.%20%C2%A7%201350"><span class="citation no-link">28 U.S.C. § 1350</span></extracted-citation>, which created a cause of action that may be brought by an alien in a U.S. court under the Alien Tort Statute, § 1350. Under the Torture Victim Protection Act, a damages action may be brought by or on behalf of a victim of torture or an extrajudicial killing carried out by a person who acted under the authority of a foreign <a class="page-label" data-citation-index="1" data-label="749" href="#p749" id="p749">*749</a>state. Consequently, this provision, which is often employed to seek redress for acts committed abroad,<footnotemark>11</footnotemark> cannot be used to sue a United States officer. See <em>Meshal v. Higgenbotham</em> , <extracted-citation case-ids="4357472,12309896" index="152" url="https://cite.case.law/f3d/804/417/"><span class="citation" data-id="9864161"><a href="/opinion/3148973/amir-meshal-v-chris-higgenbotham/" aria-description="Citation for case: Amir Meshal v. Chris Higgenbotham">804 F.3d 417</a></span></extracted-citation>, 430 (C.A.D.C. 2015) (KAVANAUGH, J., concurring).</p>
<p id="p-62">These statutes form a pattern that is important for present purposes. When Congress has enacted statutes creating a damages remedy for persons injured by United States Government officers, it has taken care to preclude claims for injuries that occurred abroad.</p>
<p id="p-63">Instead, when Congress has provided compensation for injuries suffered by aliens outside the United States, it has done so by empowering Executive Branch officials to make payments under circumstances found to be appropriate. Thus, the Foreign Claims Act, <extracted-citation index="153" url="https://cite.case.law/citations/?q=10%20U.S.C.%20%C2%A7%202734"><span class="citation no-link">10 U.S.C. § 2734</span></extracted-citation>, first enacted during World War II, ch. 645, <extracted-citation index="154" url="https://cite.case.law/citations/?q=55%20Stat.%20880"><span class="citation no-link">55 Stat. 880</span></extracted-citation>, allows the Secretary of Defense to appoint claims commissions to settle and pay claims for personal injury and property damage resulting from the noncombat activities of the Armed Forces outside this country. § 2734(a). Similarly, § 2734a allows the Secretary of Defense and the Secretary of Homeland Security to make payments pursuant to "an international agreement which provides for the settlement or adjudication and cost sharing of claims against the United States" that arise out of "acts or omissions" of the Armed Forces. § 2734a(a); see also <extracted-citation index="155" url="https://cite.case.law/citations/?q=22%20U.S.C.%20%C2%A7%202669"><span class="citation no-link">22 U.S.C. § 2669</span></extracted-citation>(b) (State Department may settle and pay certain claims for death, injury, or property loss or damage "for the purpose of promoting and maintaining friendly relations with foreign countries"); § 2669-1 (Secretary of State has authority to pay tort claims arising in foreign countries in connection with State Department operations); <extracted-citation index="156" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%20904"><span class="citation no-link">21 U.S.C. § 904</span></extracted-citation> (Attorney General has authority to pay tort claims arising in connection with the operations of the Drug Enforcement Administration abroad).</p>
<p id="p-64">This pattern of congressional action-refraining from authorizing damages actions for injury inflicted abroad by Government officers, while providing alternative avenues for compensation in some situations-gives us further reason to hesitate about extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> in this case.</p>
<p id="p-65">E</p>
<p id="p-66">In sum, this case features multiple factors that counsel hesitation about extending <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> <em>,</em> but they can all be condensed to one concern-respect for the separation of powers. See <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857-1858. "Foreign policy and national security decisions are 'delicate, complex, and involve large elements of prophecy' for which 'the Judiciary has neither aptitude, facilities[,] nor responsibility.' " <em><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/" aria-description="Citation for case: Jesner v. Arab Bank, PLC">Jesner</a></span></em> , 584 U.S., at ----, <extracted-citation case-ids="12611257" index="157" url="https://cite.case.law/s-ct/138/1386/#p1391"><span class="citation" data-id="4271160"><a href="/opinion/4493907/jesner-v-arab-bank-plc/#1414" aria-description="Citation for case: Jesner v. Arab Bank, PLC">138 S.Ct., at 1414</a></span></extracted-citation> (GORSUCH, J., concurring part and concurring in judgment) (quoting <em>Chicago &amp; Southern Air Lines, Inc. v. Waterman S. S. Corp.</em> , <extracted-citation case-ids="6157296" index="158" url="https://cite.case.law/us/333/103/#p111"><span class="citation" data-id="9420099"><a href="/opinion/104510/chicago-southern-air-lines-inc-v-waterman-steamship-corp/" aria-description="Citation for case: Chicago &amp; Southern Air Lines, Inc. v. Waterman Steamship...">333 U.S. 103</a></span></extracted-citation>, 111, <extracted-citation case-ids="6157296" index="159" url="https://cite.case.law/us/333/103/#p111"><span class="citation" data-id="9420099"><a href="/opinion/104510/chicago-southern-air-lines-inc-v-waterman-steamship-corp/" aria-description="Citation for case: Chicago &amp; Southern Air Lines, Inc. v. Waterman Steamship...">68 S.Ct. 431</a></span></extracted-citation>, <extracted-citation index="160" url="https://cite.case.law/citations/?q=92%20L.%20Ed.%20568"><span class="citation no-link">92 L.Ed. 568</span></extracted-citation> (1948) ). To avoid upsetting the delicate web of international relations, we typically presume that even congressionally crafted causes of action do not apply outside our borders. These concerns are only heightened when judges are asked to fashion constitutional remedies. Congress, which has authority in the field of foreign affairs, has chosen not to create liability in similar statutes, leaving the resolution of extraterritorial <a class="page-label" data-citation-index="1" data-label="750" href="#p750" id="p750">*750</a>claims brought by foreign nationals to executive officials and the diplomatic process.</p>
<p id="p-67">Congress's decision not to provide a judicial remedy does not compel us to step into its shoes. "The absence of statutory relief for a constitutional violation ... does not by any means necessarily imply that courts should award money damages against the officers responsible for the violation." <em>Schweiker</em> , <extracted-citation case-ids="1775175" index="161" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">487 U.S. at 421</a></span>-422</extracted-citation>, <extracted-citation case-ids="1775175" index="162" url="https://cite.case.law/us/487/412/"><span class="citation" data-id="9431421"><a href="/opinion/112132/schweiker-v-chilicky/" aria-description="Citation for case: Schweiker v. Chilicky">108 S.Ct. 2460</a></span></extracted-citation> ; see also <em>Stanley</em> , <extracted-citation case-ids="28195" index="163" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">483 U.S. at 683</a></span></extracted-citation>, <extracted-citation case-ids="28195" index="164" url="https://cite.case.law/us/483/669/"><span class="citation" data-id="9431121"><a href="/opinion/111954/united-states-v-stanley/" aria-description="Citation for case: United States v. Stanley">107 S.Ct. 3054</a></span></extracted-citation> ("[I]t is irrelevant to a 'special factors' analysis whether the laws currently on the books afford [plaintiff] an 'adequate' federal remedy for his injuries").<footnotemark>12</footnotemark></p>
<p id="p-68">When evaluating whether to extend <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span>,</em> the most important question "is 'who should decide' whether to provide for a damages remedy, Congress or the courts?" <em><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">Abbasi</a></span></em> , 582 U.S., at ----, 137 S.Ct., at 1857 (quoting <em>Bush</em> , <span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/#380" aria-description="Citation for case: Bush v. Lucas">462 U.S. at 380</a></span>, <extracted-citation case-ids="6188608" index="165" url="https://cite.case.law/us/462/367/"><span class="citation" data-id="9429240"><a href="/opinion/110965/bush-v-lucas/" aria-description="Citation for case: Bush v. Lucas">103 S.Ct. 2404</a></span></extracted-citation> ). The correct "answer most often will be Congress." 582 U.S., at ----, 137 S.Ct., at 1857<em>.</em> That is undoubtedly the answer here.</p>
<p id="p-69">* * *</p>
<p id="p-70">The judgment of the United States Court of Appeals for the Fifth Circuit is affirmed.</p>
<p id="p-71">It is so ordered.</p>
<p id="p-72">Justice THOMAS, with whom Justice GORSUCH joins, concurring.</p>
<p id="p-73">The Court correctly applies our precedents to conclude that the implied cause of action created in <em>Bivens v. Six Unknown Fed. Narcotics Agents</em> , <extracted-citation case-ids="12027206" index="166" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="167" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="168" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L.Ed.2d 619</a></span></extracted-citation> (1971), should not be extended to cross-border shootings. I therefore join its opinion.</p>
<p id="p-74">I write separately because, in my view, the time has come to consider discarding the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine altogether. The foundation for <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> -the practice of creating implied causes of action in the statutory context-has already been abandoned. And the Court has consistently refused to extend the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine for nearly 40 years, even going so far as to suggest that <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> and its progeny were wrongly decided. <em>Stare decisis</em> provides no "veneer of respectability to our continued application of [these] demonstrably incorrect precedents." <em>Gamble</em> <em>v.</em> <em>United States</em> , 587 U.S. ----, ----, <extracted-citation case-ids="12620232" index="169" url="https://cite.case.law/s-ct/139/1960/#p1981"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">139 S.Ct. 1960</a></span></extracted-citation>, 1981, <extracted-citation index="170" url="https://cite.case.law/citations/?q=204%20L.%20Ed.%202d%20322"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">204 L.Ed.2d 322</a></span></extracted-citation> (2019) (THOMAS, J., concurring). To ensure that we are not "perpetuat[ing] a usurpation of the legislative power," <em><extracted-citation index="171" url="https://cite.case.law/citations/?q=204%20L.%20Ed.%202d%20322"><span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/" aria-description="Citation for case: Gamble v. United States">id.</a></span></extracted-citation></em> , at ----, <span class="citation" data-id="9888741"><a href="/opinion/4630267/gamble-v-united-states/#1984" aria-description="Citation for case: Gamble v. United States">139 S.Ct., at 1984</a></span>, we should reevaluate our continued recognition of even a limited form of the <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> doctrine.</p>
<p id="p-75">" ' <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> is a relic of the heady days in which this Court assumed common-law powers to create causes of action.' " <em>Wilkie v. Robbins</em> , <extracted-citation case-ids="3573210" index="172" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">551 U.S. 537</a></span></extracted-citation>, 568, <extracted-citation case-ids="3573210" index="173" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">127 S.Ct. 2588</a></span></extracted-citation>, <extracted-citation case-ids="3573210" index="174" url="https://cite.case.law/us/551/537/"><span class="citation" data-id="9435015"><a href="/opinion/145705/wilkie-v-robbins/" aria-description="Citation for case: Wilkie v. Robbins">168 L.Ed.2d 389</a></span></extracted-citation> (2007) (THOMAS, J., concurring) (quoting <em>Correctional Services Corp. v. Malesko</em> , <extracted-citation case-ids="9107996" index="175" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. 61</a></span></extracted-citation>, 75, <extracted-citation case-ids="9107996" index="176" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="177" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">151 L.Ed.2d 456</a></span></extracted-citation> (2001) (Scalia, J., concurring)). In the decade preceding <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> , the Court believed that it had a duty "to be alert to provide such remedies as are necessary to make effective" Congress' purposes in enacting a statute. <em>J. I. Case Co. v. Borak</em> , <extracted-citation case-ids="6170359" index="178" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. 426</a></span></extracted-citation>, 433, <extracted-citation case-ids="6170359" index="179" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="180" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">12 L.Ed.2d 423</a></span></extracted-citation> (1964). Accordingly, the Court freely created implied private causes of action for damages under federal statutes. See, <em>e.g.,</em> <a class="page-label" data-citation-index="1" data-label="751" href="#p751" id="p751">*751</a><em>Sullivan v. Little Hunting Park, Inc.</em> , <extracted-citation case-ids="11331541" index="181" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">396 U.S. 229</a></span></extracted-citation>, 239, <extracted-citation case-ids="11331541" index="182" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">90 S.Ct. 400</a></span></extracted-citation>, <extracted-citation case-ids="11331541" index="183" url="https://cite.case.law/us/396/229/#p239"><span class="citation" data-id="9424129"><a href="/opinion/108017/sullivan-v-little-hunting-park-inc/" aria-description="Citation for case: Sullivan v. Little Hunting Park, Inc.">24 L.Ed.2d 386</a></span></extracted-citation> (1969) ; <em>Allen v. State Bd. of Elections</em> , <extracted-citation case-ids="11320219" index="184" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">393 U.S. 544</a></span></extracted-citation>, 557, <extracted-citation case-ids="11320219" index="185" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">89 S.Ct. 817</a></span></extracted-citation>, <extracted-citation case-ids="11320219" index="186" url="https://cite.case.law/us/393/544/#p557"><span class="citation" data-id="9423914"><a href="/opinion/107846/allen-v-state-board-of-elections/" aria-description="Citation for case: Allen v. State Board of Elections">22 L.Ed.2d 1</a></span></extracted-citation> (1969).</p>
<p id="p-76">This misguided approach to implied causes of action in the statutory context formed the backdrop of the Court's decision in <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> . There, the Court held that federal officers who conducted a warrantless search and arrest in violation of the Fourth Amendment could be sued for damages. <em>Bivens</em> , <extracted-citation case-ids="12027206" index="187" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. at 397</a></span></extracted-citation>, <extracted-citation case-ids="12027206" index="188" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>. The Court acknowledged that Congress had not provided a statutory cause of action for damages against federal officers and that "the Fourth Amendment does not in so many words provide for its enforcement by an award of money damages." <em><extracted-citation case-ids="12027206" index="189" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 396-397, <extracted-citation case-ids="12027206" index="190" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation>. But it concluded, consistent with the then-prevailing understanding of implied causes of action in the statutory context, that federal courts could infer such a "remedial mechanism." <em><extracted-citation case-ids="12027206" index="191" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Id.</a></span></extracted-citation></em> , at 397, <extracted-citation case-ids="12027206" index="192" url="https://cite.case.law/us/403/388/"><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S.Ct. 1999</a></span></extracted-citation> (citing <em>Borak</em> , <extracted-citation case-ids="6170359" index="193" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">377 U.S. at 433</a></span></extracted-citation>, <extracted-citation case-ids="6170359" index="194" url="https://cite.case.law/us/377/426/#p433"><span class="citation" data-id="106845"><a href="/opinion/106845/j-i-case-co-v-borak/" aria-description="Citation for case: J. I. Case Co. v. Borak">84 S.Ct. 1555</a></span></extracted-citation> ).</p>
<p id="p-77">This holding "broke new ground." <em>Ante</em> , at 741. From the ratification of the Bill of Rights until 1971, the Court did not create "implied private action[s] for damages against federal officers alleged to have violated a citizen's constitutional rights." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="195" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 66</a></span></extracted-citation>, <extracted-citation case-ids="9107996" index="196" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. Suits to recover such damages were generally brought under state tort law. See <em>Wheeldin v. Wheeler</em> , <extracted-citation case-ids="11719775" index="197" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">373 U.S. 647</a></span></extracted-citation>, 652, <extracted-citation case-ids="11719775" index="198" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">83 S.Ct. 1441</a></span></extracted-citation>, <extracted-citation case-ids="11719775" index="199" url="https://cite.case.law/us/373/647/#p652"><span class="citation" data-id="9422624"><a href="/opinion/106628/wheeldin-v-wheeler/" aria-description="Citation for case: Wheeldin v. Wheeler">10 L.Ed.2d 605</a></span></extracted-citation> (1963). <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> thus opened the door to a new avenue for recovering damages from federal officers. In the wake of that decision, the Court recognized an implied cause of action for damages against a Member of Congress accused of sex discrimination in violation of the Fifth Amendment's Due Process Clause, <em>Davis v. Passman</em> , <extracted-citation case-ids="1532130" index="200" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U.S. 228</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="201" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">99 S.Ct. 2264</a></span></extracted-citation>, <extracted-citation case-ids="1532130" index="202" url="https://cite.case.law/us/442/228/"><span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">60 L.Ed.2d 846</a></span></extracted-citation> (1979), and against prison officials accused of denying medical care in violation of the Eighth Amendment's Cruel and Unusual Punishments Clause, <em>Carlson v. Green</em> , <extracted-citation case-ids="6180250" index="203" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">446 U.S. 14</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="204" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">100 S.Ct. 1468</a></span></extracted-citation>, <extracted-citation case-ids="6180250" index="205" url="https://cite.case.law/us/446/14/"><span class="citation" data-id="9427872"><a href="/opinion/110245/carlson-v-green/" aria-description="Citation for case: Carlson v. Green">64 L.Ed.2d 15</a></span></extracted-citation> (1980). Given this Court's trend of creating implied causes of action, "there was a possibility that the Court would keep expanding <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span></em> until it became the substantial equivalent of <extracted-citation index="206" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation>." <em>Ziglar</em> <em>v.</em> <em>Abbasi</em> , 582 U.S. ----, ----, <extracted-citation case-ids="12604999" index="207" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">137 S.Ct. 1843</a></span></extracted-citation>, 1855, <extracted-citation case-ids="12604999" index="208" url="https://cite.case.law/s-ct/137/1843/"><span class="citation" data-id="4181057"><a href="/opinion/4403804/ziglar-v-abbasi/" aria-description="Citation for case: Ziglar v. Abbasi">198 L.Ed.2d 290</a></span></extracted-citation> (2017) (internal quotation marks omitted).</p>
<p id="p-78">The Court, however, eventually corrected course. In the statutory context, the Court "retreated from [its] previous willingness to imply a cause of action where Congress has not provided one." <em>Malesko</em> , <extracted-citation case-ids="9107996" index="209" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/#67" aria-description="Citation for case: Correctional Services Corp. v. Malesko">534 U.S. at 67</a></span>, n. 3</extracted-citation>, <extracted-citation case-ids="9107996" index="210" url="https://cite.case.law/us/534/61/"><span class="citation" data-id="9434165"><a href="/opinion/118466/correctional-services-corp-v-malesko/" aria-description="Citation for case: Correctional Services Corp. v. Malesko">122 S.Ct. 515</a></span></extracted-citation>. After a series of decisions limiting courts' discretion to create statut

[...TRUNCATED 90943 of 210943 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
