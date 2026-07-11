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

## GROUP: _overhaul2/lake/cases/Gonzalez v. Trevino.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "5e99cfd864858537", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gonzalez v. Trevino"}, "payload": {"all": [{"cite": "602 U.S. 653", "page": "653", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "602"}], "display": "602 U.S. 653", "official": {"cite": "602 U.S. 653", "page": "653", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "602"}, "official_selection_present": true, "record_id": "Gonzalez v. Trevino"}}
{"assertion_id": "00f1ea4aa4b6cd5c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gonzalez v. Trevino"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Gonzalez v. Trevino", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Gooding v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Gooding v. United States"
type: case
citation: "416 U.S. 430 (1974)"
parallel_cite: "94 S. Ct. 1780; 40 L. Ed. 2d 250"
neutral_cite: 1974 U.S. LEXIS 133
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1974
date_decided: 1974-04-29
docket: 72-6902
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1974-04-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gooding v. United States
  varies_by_point: false
  scope_note: "Statutory holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction stands. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109017/gooding-v-united-states/"
  cluster_id: 109017
  opinion_id: 109017
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Related (nighttime execution)"
related: []
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "warrant-execution", "nighttime-search", "narcotics"]
holding: "Under 21 U.S.C. § 879(a), a narcotics search warrant may be executed at night with no special showing of need beyond probable cause that the contraband is likely to be on the premises at that time."
lake:
  record_id: Gooding v. United States
  status: verified
  projected_at: 2026-07-09
---

# Gooding v. United States

*416 U.S. 430 (1974)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
District of Columbia Metropolitan Police, armed with a warrant to search Gooding's apartment for narcotics, executed it at roughly 9:30 p.m. and seized a substantial quantity of contraband. The supporting affidavit stated that the officer was "positive" Gooding was secreting narcotics in the apartment and described continuing drug traffic plus a prior controlled purchase. Gooding moved to suppress, arguing the nighttime seizure violated the governing statutory restrictions on after-dark search-warrant execution.

## Issue
Which statute governs nighttime execution of a federal narcotics search warrant, and what showing it requires — specifically, whether 21 U.S.C. § 879(a) demands a special justification for searching at night beyond probable cause that the contraband is present.

## Rule
The narcotics-specific statute, 21 U.S.C. § 879(a), controls rather than Federal Rule of Criminal Procedure 41 or the D.C. Code daytime-service provisions. Section 879(a) permits service "at any time of the day or night" so long as the issuing authority "is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." — 416 U.S. at 439. ^pin-439

"We therefore conclude that 21 U.S.C. § 879(a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time." — *Id.* at 458. ^pin-458

## Application
The affidavit supporting Gooding's warrant "suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available." That was "sufficient to satisfy 21 U.S.C. § 879(a)," so the 9:30 p.m. execution was lawful and the seized contraband was admissible. — [416 U.S. at 458](https://www.courtlistener.com/opinion/109017/gooding-v-united-states/#:~:text=suggested%20that%20there%20was%20a). ^pin-458b

## Conclusion
The nighttime narcotics search was authorized under § 879(a) on the showing made; the Court of Appeals' judgment upholding the search was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Gooding* is a statutory-construction holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction governs nighttime execution of federal narcotics warrants.

## Appears on
- [[Scope Manner and Related Issues]] — *Related (nighttime execution)*

## Sources
- *Gooding v. United States*, 416 U.S. 430 (1974) — https://www.courtlistener.com/opinion/109017/gooding-v-united-states/ — pinpoints: 439, 458.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "492fbf2b9211538d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gooding v. United States"}, "payload": {"all": [{"cite": "416 U.S. 430", "page": "430", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "416"}, {"cite": "94 S. Ct. 1780", "page": "1780", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "40 L. Ed. 2d 250", "page": "250", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "40"}, {"cite": "1974 U.S. LEXIS 133", "page": "133", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1974"}], "display": "416 U.S. 430", "official": {"cite": "416 U.S. 430", "page": "430", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "416"}, "official_selection_present": true, "record_id": "Gooding v. United States"}}
{"assertion_id": "ca90f61624b04ef6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-458", "record_id": "Gooding v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-458", "pinpoint_status": "slip-only", "quote": "We therefore conclude that 21 U.S.C. § 879(a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time.", "quote_fidelity": "mismatch", "record_id": "Gooding v. United States", "star_marker": null}}
{"assertion_id": "eafd75ab788c9142", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-439", "record_id": "Gooding v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-439", "pinpoint_status": "slip-only", "quote": "Gooding was secreting narcotics in the apartment and described continuing drug traffic plus a prior controlled purchase. Gooding moved to suppress, arguing the nighttime seizure violated the governing statutory restrictions on after-dark search-warrant execution. ## Issue Which statute governs nighttime execution of a federal narcotics search warrant, and what showing it requires — specifically, whether 21 U.S.C. § 879(a) demands a special justification for searching at night beyond probable cause that the contraband is present. ## Rule The narcotics-specific statute, 21 U.S.C. § 879(a), controls rather than Federal Rule of Criminal Procedure 41 or the D.C. Code daytime-service provisions. Section 879(a) permits service", "quote_fidelity": "mismatch", "record_id": "Gooding v. United States", "star_marker": null}}
{"assertion_id": "f3286635ee48b127", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-458b", "record_id": "Gooding v. United States"}, "payload": {"fragment": "#:~:text=suggested%20that%20there%20was%20a", "page": null, "pin_id": "pin-458b", "pinpoint_status": "star-verified", "quote": "suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available.", "quote_fidelity": "matched", "record_id": "Gooding v. United States", "star_marker": "458"}}
{"assertion_id": "996884fe7c94f645", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gooding v. United States"}, "payload": {"as_of_content": "1974-04-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Gooding v. United States", "scope_note": "Statutory holding interpreting 21 U.S.C. § 879(a); the statute remains in force and the construction stands. Good law.", "varies_by_point": false}}
```

### lake record — Gooding v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gooding v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gooding v. United States",
    "case_name_short": "Gooding",
    "case_name_full": "Gooding v. United States",
    "input_case_name": "Gooding v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1974-04-29",
    "year": 1974,
    "docket": "72-6902",
    "cluster_id": 109017,
    "lead_opinion_id": 109017,
    "sibling_ids": [
      109017,
      9425696,
      9425697,
      9425698
    ],
    "absolute_url": "/opinion/109017/gooding-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "416 U.S. 430",
      "volume": "416",
      "reporter": "U.S.",
      "page": "430",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "94 S. Ct. 1780",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1780",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 250",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1974 U.S. LEXIS 133",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "416 U.S. 430",
        "volume": "416",
        "reporter": "U.S.",
        "page": "430",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 S. Ct. 1780",
        "volume": "94",
        "reporter": "S. Ct.",
        "page": "1780",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "40 L. Ed. 2d 250",
        "volume": "40",
        "reporter": "L. Ed. 2d",
        "page": "250",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1974 U.S. LEXIS 133",
        "volume": "1974",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "416 U.S. 430",
    "official_selection": {
      "court_class": "scotus",
      "selected": "416 U.S. 430",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-439",
      "page": null,
      "quote": "Gooding was secreting narcotics in the apartment and described continuing drug traffic plus a prior controlled purchase. Gooding moved to suppress, arguing the nighttime seizure violated the governing statutory restrictions on after-dark search-warrant execution. ## Issue Which statute governs nighttime execution of a federal narcotics search warrant, and what showing it requires \u2014 specifically, whether 21 U.S.C. \u00a7 879(a) demands a special justification for searching at night beyond probable cause that the contraband is present. ## Rule The narcotics-specific statute, 21 U.S.C. \u00a7 879(a), controls rather than Federal Rule of Criminal Procedure 41 or the D.C. Code daytime-service provisions. Section 879(a) permits service",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-458",
      "page": null,
      "quote": "We therefore conclude that 21 U.S.C. \u00a7 879(a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-458b",
      "page": null,
      "quote": "suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available.",
      "star_marker": "458",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 29625,
      "fragment": "#:~:text=suggested%20that%20there%20was%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1974-04-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gooding v. United States",
    "varies_by_point": false,
    "scope_note": "Statutory holding interpreting 21 U.S.C. \u00a7 879(a); the statute remains in force and the construction stands. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Richard J. Rizzi",
          "cluster_id": 792946,
          "cite": [
            "434 F.3d 669",
            "2006 U.S. App. LEXIS 450",
            "2006 WL 39266"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Rome v. United States",
          "cluster_id": 110248,
          "cite": [
            "64 L. Ed. 2d 119",
            "100 S. Ct. 1548",
            "446 U.S. 156",
            "1980 U.S. LEXIS 123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James N. Gramenos v. Jewel Companies, Inc.",
          "cluster_id": 474259,
          "cite": [
            "797 F.2d 432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Alejandrina Torres",
          "cluster_id": 446389,
          "cite": [
            "751 F.2d 875"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antoine Jones v. Steve Kirchner",
          "cluster_id": 4251490,
          "cite": [
            "835 F.3d 74",
            "2016 U.S. App. LEXIS 15759"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Wayne Searp",
          "cluster_id": 360886,
          "cite": [
            "586 F.2d 1117",
            "58 A.L.R. Fed. 743",
            "1978 U.S. App. LEXIS 7945"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. State",
          "cluster_id": 2386467,
          "cite": [
            "782 A.2d 862",
            "366 Md. 121",
            "2001 Md. LEXIS 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Burch, Larry D.",
          "cluster_id": 184680,
          "cite": [
            "156 F.3d 1315",
            "332 U.S. App. D.C. 287",
            "50 Fed. R. Serv. 3d 1",
            "1998 U.S. App. LEXIS 24913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 1995209,
          "cite": [
            "742 N.W.2d 163",
            "2007 Minn. LEXIS 756",
            "2007 WL 4261169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lien",
          "cluster_id": 1719873,
          "cite": [
            "265 N.W.2d 833",
            "1978 Minn. LEXIS 1353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawson",
          "cluster_id": 1512232,
          "cite": [
            "502 F. Supp. 158",
            "1980 U.S. Dist. LEXIS 14227"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Patrick Harm Keene",
          "cluster_id": 548987,
          "cite": [
            "915 F.2d 1164",
            "31 Fed. R. Serv. 64",
            "1990 U.S. App. LEXIS 16882",
            "1990 WL 138148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Richard Tedford",
          "cluster_id": 523577,
          "cite": [
            "875 F.2d 446",
            "1989 U.S. App. LEXIS 7870",
            "1989 WL 56819"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Yanez-Marquez v. Loretta Lynch",
          "cluster_id": 2808824,
          "cite": [
            "789 F.3d 434",
            "2015 U.S. App. LEXIS 10107",
            "2015 WL 3719105"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 1757509,
          "cite": [
            "665 So. 2d 1237",
            "1995 WL 713755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1149871,
          "cite": [
            "617 P.2d 1117",
            "1980 Alas. LEXIS 721"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roth v. State",
          "cluster_id": 898092,
          "cite": [
            "2007 ND 112",
            "735 N.W.2d 882",
            "2007 N.D. LEXIS 125",
            "2007 WL 2120566"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brock",
          "cluster_id": 1188105,
          "cite": [
            "653 P.2d 543",
            "294 Or. 15",
            "1982 Ore. LEXIS 1281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodriguez v. Superior Court",
          "cluster_id": 2180261,
          "cite": [
            "199 Cal. App. 3d 1453",
            "245 Cal. Rptr. 617",
            "1988 Cal. App. LEXIS 309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 1995384,
          "cite": [
            "742 N.W.2d 149",
            "2007 Minn. LEXIS 752",
            "2007 WL 4259511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seth Mason and Carl Peterson v. United States",
          "cluster_id": 426314,
          "cite": [
            "719 F.2d 1485",
            "14 Fed. R. Serv. 817",
            "1983 U.S. App. LEXIS 15900"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Grimshaw",
          "cluster_id": 2219758,
          "cite": [
            "595 N.E.2d 302",
            "413 Mass. 73",
            "1992 Mass. LEXIS 388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Porco",
          "cluster_id": 1461438,
          "cite": [
            "842 F. Supp. 1393",
            "1994 U.S. Dist. LEXIS 869",
            "1994 WL 22574"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rowe",
          "cluster_id": 1379495,
          "cite": [
            "806 P.2d 730",
            "154 Utah Adv. Rep. 12",
            "1991 Utah App. LEXIS 15",
            "1991 WL 17377"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gooding v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 2,
        "triage_snippet_classified": 46
      },
      "lane2_top_cited": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02JnM9MTgxMTkxNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109017+OR+9425696+OR+9425697+OR+9425698%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
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
    "complete_query": "cites:(109017 OR 9425696 OR 9425697 OR 9425698)",
    "indexed_citing_opinions": 65,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109017,
        "count": 61,
        "count_source": "search"
      },
      {
        "opinion_id": 9425696,
        "count": 5,
        "count_source": "search"
      },
      {
        "opinion_id": 9425697,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425698,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 98,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gooding-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjEzMDU1Mjkmcz0yOTY4MjQ3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109017+OR+9425696+OR+9425697+OR+9425698%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109017,
        "cited_id": 101357,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 102494,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 104285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 104671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 106253,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 260559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 270626,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 285611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 310420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 2293098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109017,
        "cited_id": 2307321,
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
    "date_created": "2026-07-05T05:40:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:45:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:40:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gooding v. United States

```
<div>
<center><b><span class="citation" data-id="9425696"><a href="/opinion/109017/gooding-v-united-states/" aria-description="Citation for case: Gooding v. United States">416 U.S. 430</a></span> (1974)</b></center>
<center><h1>GOODING<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 72-6902.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 25, 1974.</center>
<center>Decided April 29, 1974.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><span class="star-pagination">*431</span> <i>Herbert A. Rosenthal,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./414/998/">414 U. S. 998</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Deputy Solicitor General Frey</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Bork, Assistant Attorney General Petersen, Edward R. Korman,</i> and <i>Jerome M. Feit.</i></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Petitioner in this case presents a claim that evidence offered against him at his trial should have been suppressed because it was seized at nighttime in violation of governing statutory provisions. The search which led to the seizure was conducted by officers of the District of Columbia Metropolitan Police Department at approximately 9:30 p. m. within the District of Columbia. <span class="star-pagination">*432</span> Armed with a search warrant, the officers entered petitioner's apartment for the purpose of discovering violations of a federal narcotics statute, and seized a substantial amount of contraband narcotics. The parties urge upon us differing theories concerning which federal or District of Columbia statute bears on the legality of this search, and we must therefore interpret and reconcile several recent congressional enactments dealing with nighttime searches which seem to embody somewhat inconsistent views.<sup>[1]</sup></p>
<p>The Court of Appeals agreed with the District Court's description of this congeries of statutes as a " `bramble-bush of uncertainties and contradictions,' "<sup>[2]</sup> and a mere summary of the statutes attests to the accuracy of that observation:</p>
<p><i>District of Columbia Statutes:</i> The older of the two conceivably relevant District of Columbia statutes, D. C. Code § 33-414 (1973),<sup>[3]</sup> was enacted in 1956 and authorizes <span class="star-pagination">*433</span> search warrants for violations of the District of Columbia narcotics laws. This section does not limit the time during which searches may be made, stating plainly that "[t]he judge or commissioner shall insert a direction in the warrant that it may be served at any time in the day or night." This liberal time provision is in direct contrast to the more restrictive provisions of the second <span class="star-pagination">*434</span> District of Columbia statute to be considered, D. C. Code § 23-521 (f) (5),<sup>[4]</sup> which specifically requires that search warrants be served in the daytime unless certain conditions <span class="star-pagination">*435</span> set forth in § 23-522 (c) (1) are met. These conditions essentially require a showing of special need to search at night, and concededly have not been satisfied in this case.</p>
<p><span class="star-pagination">*436</span> <i>Federal Statutes and Rules:</i> The general provision governing federal search warrants is found in Fed. Rule Crim. Proc. 41.<sup>[5]</sup> At the time the search in this case <span class="star-pagination">*437</span> took place, Rule 41 (c) provided that warrants must be served in the daytime except where "the affidavits are positive that the property is on the person or in the place to be searched."<sup>[6]</sup> In such event the warrant <span class="star-pagination">*438</span> could direct "that it be served at any time." This provision was incorporated in the Rules in 1948 as a replacement for language previously contained in the Espionage Act of 1917.<sup>[7]</sup> A second federal statute relating only to searches for "controlled substances" is found in <span class="citation no-link">21 U. S. C. § 879</span> (a),<sup>[8]</sup> which was enacted in <span class="star-pagination">*439</span> 1970. That section provides that a warrant may be served "at any time of the day or night" so long as the issuing authority "is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." This provision in turn is the successor to a provision in <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.),<sup>[9]</sup> enacted in 1956 to relax the "positivity" test of Rule 41 in cases involving certain narcotic drugs.<sup>[10]</sup> Congress had passed this statute in response to the complaints of law enforcement officers that the positivity requirement gave commercial narcotics dealers a definite advantage over federal agents. Rule 41 is therefore not applicable to searches governed by the more specific narcotic search statutes.<sup>[11]</sup></p>
<p><span class="star-pagination">*440</span> The facts of this case must be understood in the context of these statutes. On February 11, 1971, an Assistant United States Attorney applied to a United States Magistrate sitting in the District of Columbia for a warrant authorizing a search of petitioner's apartment for evidence of illegal narcotics. The application included the brief notation: "Violation: U. S. C.; Title 26. Sections: 4704a." In connection with the application, an officer of the Metropolitan Police Department vice squad appeared before the Magistrate and swore that he had reason to believe petitioner was concealing property held in violation of that same code provision.<sup>[12]</sup><span class="star-pagination">*441</span> The officer supplemented his personal testimony with a written affidavit, outlining the basis for the application in more detail and alleging specifically that "illegal drugs are sold and possessed in violation of the United States Code, Title 26, Section 4704a."<sup>[13]</sup> The affidavit concluded with the language: "I am positive that Lonnie Gooding is secreting narcotics inside his apartment at 1419 Chapin Street NW in violation of the US Code."</p>
<p>The Magistrate then issued a warrant directing the Chief of Police or "any member of MPDC" to search petitioner's apartment.<sup>[14]</sup> The warrant specifically noted <span class="star-pagination">*442</span> that facts had been set forth in an affidavit alleging a violation of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.) and that those facts established probable cause to make the search. The warrant also stated that the search could be made "at any time in the day or night." This phrase was accompanied by a footnote reference to Fed. Rule Crim. Proc. 41 (c), presumably because the police officer had asserted he was "positive" the drugs were in petitioner's apartment. One of the briefs filed in this case suggests that the warrant form was preprinted and contemplated application of Rule 41 standards.<sup>[15]</sup></p>
<p>The search warrant was executed on February 12, 1971, at 9:30 p. m.<sup>[16]</sup> The officers engaged in the search were <span class="star-pagination">*443</span> all members of the District of Columbia Metropolitan Police Department, and the search uncovered a substantial quantity of contraband narcotic materials. They were seized and formed the basis for charging petitioner with violations of <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.)<sup>[17]</sup> and <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.).<sup>[18]</sup> Following his indictment in the United States District Court for the District of Columbia on April 6, 1971, petitioner filed a motion to suppress the evidence discovered in the February 12 search.</p>
<p>Several grounds were asserted in support of the motion, particularly that "[t]he search warrant was executed at night but the application for the warrant did not comply with the D. C. Code provisions for nighttime search <span class="star-pagination">*444</span> warrants . . . ."<sup>[19]</sup> Although no provisions of the D. C. Code were explicitly referred to, petitioner's argument apparently was that Title 23 of the D. C. Code, requiring that a special showing of need be made to justify a search at night, governed this search, and that its requirements had not been met. The District Court found this reasoning persuasive and granted the motion to suppress. Rejecting the Government's argument that the warrant was not issued under Title 23 but rather under <span class="citation no-link">21 U. S. C. § 879</span> (a), the court stated:</p>
<blockquote>"Whatever be the standards generally for issuance of a nighttime search warrant in federal narcotics cases in other parts of the country, however, the Court finds that the existence of <span class="citation no-link">21 U. S. C. § 879</span> (a) does not remove such cases from the explicit requirements for search warrants in the District of Columbia under the newly enacted Title 23, D. C. Code."<sup>[20]</sup></blockquote>
<p>Having decided that District of Columbia law applied, the District Court admitted to some uncertainty about the status of D. C. Code § 33-414, the provision dealing specifically with violations of local drug laws. The court noted with some puzzlement that no mention of this provision was found in the legislative history of Title 23, and that some language in the legislative history suggested that the provision had simply been overlooked.<sup>[21]</sup> Nevertheless, the court determined that</p>
<blockquote>"[p]ending prompt review of this determination <span class="star-pagination">*445</span> or congressional action, and pending interpretation of 33 D. C. Code § 414 (h) in light of the new Title 23 provisions, search warrants which are to be executed in the nighttime should comply in all respects with 23 D. C. Code § 523 (b)."<sup>[22]</sup></blockquote>
<p>Concededly the warrant issued in this case did not comply with the requirements of Title 23.</p>
<p>The Court of Appeals for the District of Columbia Circuit reversed the District Court,<sup>[23]</sup> although none of the three judges who composed the panel completely agreed with any other on the proper rationale. All three agreed, however, that <span class="citation no-link">21 U. S. C. § 879</span> (a), rather than any provision of the District of Columbia Code, was the provision which determined the legality of this search. All three likewise agreed that the affidavit submitted by the District of Columbia police officer satisfied the requirements of that section. Judge Wilkey and Judge Fahy found that no greater showing for a nighttime search was required by § 879 (a) than was required by its predecessor statute governing federal narcotics searches, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), and that the affidavit need establish only probable cause to believe that the property would be on the premises at the time of the search.<sup>[24]</sup> Judge Robinson believed that § 879 (a) <span class="star-pagination">*446</span> did require an additional showing for a nighttime search, but concluded that such a showing had been made in this case.<sup>[25]</sup></p>
<p>Petitioner urges that we reverse the Court of Appeals on either or both of two alternative grounds. First, petitioner repeats his assertion, sustained by the District Court, that Title 23 of the D. C. Code is the statute applicable to the search in this case and that, as the Government has conceded, the requirements of that title have not been satisfied. Second, petitioner argues that, if <span class="citation no-link">21 U. S. C. § 879</span> (a) is considered to be the applicable provision, a special showing for nighttime searches must be made. We agree with the Court of Appeals that <span class="citation no-link">21 U. S. C. § 879</span> (a) is the statute applicable to this case, and that its provisions have been satisfied here.<sup>[26]</sup></p>
<p></p>
<h2>I</h2>
<p>The unique situation of the District of Columbia, for which Congress legislates both specially and as a part <span class="star-pagination">*447</span> of the Nation, gives rise to the principal difficulties in this case. For we deal here not with statutory schemes enacted by independent legislative bodies, but with possibly overlapping schemes enacted by a single body. Despite the potential overlap, however, we think that the operative facts surrounding this search strongly indicate that the standards for issuance of a warrant should be governed by the nationwide federal legislation enacted by Congressthat is, <span class="citation no-link">21 U. S. C. § 879</span> (a)<sup>[27]</sup> rather than by the local D. C. laws. To begin with, an Assistant United States Attorney, who had discretion to proceed either under federal or under local law, filed the application for the search warrant alleging a violation of the United States Code. Application was made to a United States Magistrate, located in the United States District Court building, and neither the application nor the supporting affidavits contained any mention of the local narcotics laws. After the materials were seized, petitioner was indicted for violations of federal law.</p>
<p>Petitioner contends, however, that Title 23 of the D. C. Code should apply to this case because the executing officers, as well as the officer swearing to the affidavit presented to the Magistrate, were not federal officers but officers of the District of Columbia Metropolitan Police Department. He argues that the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) were intended to apply solely to agents of the Bureau of Narcotics and Dangerous Drugs, none of whom were involved here, whereas Title 23 of the D. C. Code was intended to provide comprehensive regulation of District of Columbia police officers investigating both local and federal offenses. Petitioner reinforces his argument by nothing that the former federal statute <span class="star-pagination">*448</span> regulating drug searches specifically provided that "a search warrant may be directed to any officer of the Metropolitan Police of the District of Columbia authorized to enforce or assist in enforcing a violation of any of such provisions,"<sup>[28]</sup> while no such section appears in <span class="citation no-link">21 U. S. C. § 879</span>. Therefore, says petitioner, the District of Columbia police were no longer to be considered federal agents for the purpose of enforcing federal drug laws.</p>
<p>Although petitioner's arguments cannot be dismissed lightly, we find them ultimately unpersuasive. Concededly there are hints in the statutory framework and legislative history of the Controlled Substances Act, <span class="citation no-link">84 Stat. 1242</span>, that indicate the policing function under those provisions would be the primary responsibility of the Bureau of Narcotics and Dangerous Drugs.<sup>[29]</sup> But this focus on the Bureau's role seems entirely natural in view of one of the Act's stated purposes to "collect the diverse drug <span class="star-pagination">*449</span> control and enforcement laws under one piece of legislation to facilitate law enforcement, drug research, educational and related control facilities."<sup>[30]</sup> In providing a comprehensive federal scheme for the control of drug abuse, Congress could be expected to pay special attention to the federal agency set up to enforce the laws. But this attention does not mean that Congress at the same time wished to dispense with the aid of other enforcement personnel who had previously given assistance.</p>
<p>The failure of Congress to include a special provision authorizing District of Columbia police officers to obtain search warrants for investigating federal offenses cannot be taken as a deliberate exclusion in view of the overall statutory framework. The provision included in the previous federal statute may well have seemed unnecessary, both in light of the history of cooperation between the District of Columbia police and federal officers and in view of the provisions of D. C. Code § 4-138 providing that "[a]ny warrant for search or arrest, issued by any magistrate of the District, may be executed in any part of the District by any member of the police force . . . ."<sup>[31]</sup> Thus, both custom and statute already assured the availability of District of Columbia police. Furthermore, the legislative history relating to § 879 (a) stresses the need for stronger enforcement of the federal narcotics laws, a goal hardly advanced by reducing the forces available to execute those laws. In fact, the provision <span class="star-pagination">*450</span> which is now § 879 (b), permitting "no-knock" searches under certain conditions, was one of the most controversial sections of the entire bill, and was defended primarily by the pressing need for added enforcement weapons to combat the increased drug traffic.<sup>[32]</sup></p>
<p>Finally, the interpretation urged by petitioner would leave District of Columbia officers able to execute general federal search warrants under amended Fed. Rule Crim. Proc. 41, but would deny them that authority under the federal drug search statute. Rule 41 now provides that "a federal law enforcement officer"defined in the Rule to include "any category of officers authorized by the Attorney General to request the issuance of a search warrant"may make applications under the Rule. The Attorney General has since listed the Metropolitan Police Department among those agencies <span class="star-pagination">*451</span> which are so authorized.<sup>[33]</sup> If petitioner's contention were accepted, it would seemingly mean that the general search warrant statute applicable to the District of Columbia would govern District of Columbia police officers investigating federal drug cases, but would not govern them when investigating other federal crimes. This result would obtain despite the fact that District of Columbia police officers historically played a prominent role in the enforcement of federal drug laws under <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.).</p>
<p>There is little indication that Title 23 of the D. C. Code was intended to serve the sweeping purpose which petitioner attributes to it.<sup>[34]</sup> The search warrant provisions upon which petitioner relies were part of the Court Reform and Criminal Procedure Act, which substantially reorganized the District of Columbia court system, providing for a new local court of general jurisdiction and relieving the United States District Court for the District of Columbia of much of its local burden.<sup>[35]</sup> Prior to that time all local felonies had been tried in the United States District Court, and the Federal Rules of Criminal Procedure by their terms had applied. The creation of the new Superior Court created the need for a new set of procedural <span class="star-pagination">*452</span> rules, and, though some important changes were made, the new rules quite closely tracked the Federal Rules. It does not seem unreasonable, therefore, to suggest that the general provision relating to search warrants, found in D. C. Code § 23-521 <i>et seq.</i> and then incorporated in similar form into the rules<sup>[36]</sup> promulgated <span class="star-pagination">*453</span> Feb. 1, 1971, for the new Superior Court, was intended to be a counterpart to Fed. Rule Crim. Proc. 41. The Federal Rule, as discussed <i>infra,</i> did not apply to narcotics cases in the federal courts since more specific provisions, first those of <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.) and then those of <span class="citation no-link">21 U. S. C. § 879</span> (a), controlled.<sup>[37]</sup></p>
<p>This conclusion is reinforced by the fact that Federal Rule 41 has been subsequently modified to more closely resemble the District of Columbia statute and rule. The new Federal Rule, though less specific than the local rule, provides that a search warrant must be served in the daytime, "unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime," and abandons the old, cumbersome positivity standard. The concern for individual privacy revealed in the provisions of the District of Columbia search statute may thus be found in the new Federal Rule as well, but Congress, as it had in the earlier version of the Rule, <span class="star-pagination">*454</span> nevertheless showed its clear intention to leave intact other special search warrant provisions, including, of course, the provisions relating to searches for controlled substances.<sup>[38]</sup> In those limited cases Congress has considered the need for privacy to be counterbalanced by the public need for more effective law enforcement. We do not believe that Congress, by enacting a general search warrant provision for the District of Columbia, has struck a different balance in federal drug cases simply because District of Columbia police officers are involved.</p>
<p>We therefore conclude, as did all the judges of the Court of Appeals, that the statute applicable to this case is <span class="citation no-link">21 U. S. C. § 879</span> (a). Our remaining task is to determine whether the requirements of that section have been met.</p>
<p></p>
<h2>II</h2>
<blockquote>"A search warrant relating to offenses involving controlled substances may be served at any time of the day or night if the judge or United States magistrate issuing the warrant is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time." <span class="citation no-link">21 U. S. C. § 879</span> (a).</blockquote>
<p>Only the last seven words of the statute are really in controversy here. Petitioner contends that this language, not found in the predecessor statute, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), was intended to require some special showing of need for searches conducted at night rather than during the day. His contention was adopted, at least in part, by Judge Robinson in the Court of Appeals. The Government, on the other hand, contends that it must show only probable cause to believe that the <span class="star-pagination">*455</span> sought-after property will be on the premises at the time of the search, and that if there is probable cause to believe the property will be on the premises at night, such a showing sufficiently meets the requirement imposed by the last seven words of § 879 (a).</p>
<p>The language of the statute by itself is not crystal clear on this issue. Petitioner insists that the last phrase requires with unmistakable clarity a separate finding of probable cause to justify a nighttime search. Thus, according to petitioner, the issuing magistrate would have to satisfy himself that there was not only probable cause for the search, but also probable cause for believing that the search should be conducted at nighttime rather than during the daytime. While this is <i>a</i> possible meaning, it is by no means the only possible meaning attributable to the words.</p>
<p>Petitioner's interpretation really assumes that the statute reads: "There is probable cause to believe that grounds exist for the warrant and, <i>if served at night,</i> for its service at such time." But the statute does not include the italicized four words; it makes no distinction whatever between day and night, and literally read would apparently require that a special showing be made for a daytime search as well. The idea that a particularized showing must be made for searches in the daytime is completely novel and lacks even a single counterpart in other search statutes enacted by Congress.</p>
<p>Petitioner suggests that since Congress was concerned about the greater intrusion resulting from nighttime searches, it would be logical to apply the language, "probable cause . . . for its service at such time," only to nighttime searches. But even this interpretation, which is by no means a literal reading of the language, is not wholly convincing. The traditional limitation placed on nighttime searches, as evident from the earlier <span class="star-pagination">*456</span> language of Rule 41, is to require, not that there be probable cause for searching at night, but that the affiant be <i>positive</i> that the property is in fact located on the property to be searched. Thus Congress' very choice of the words "probable cause" would indicate that the earlier limitation of "positivity" was not to apply, while offering no other immediately ascertainable standard for what should constitute "probable cause" for executing a search warrant during the night.</p>
<p>This roundabout way of limiting nighttime searches, if that were in fact the statute's intent, would sharply contrast with the manner in which Congress has required special showings for nighttime searches in other statutes. For example, Title 23 of the D. C. Code, discussed <i>supra,</i> specifies that the warrant "be executed <i>during the hours of daylight</i>" (emphasis added) unless certain itemized conditions are met. Federal Rule Crim. Proc. 41, as amended in 1972, states: "The warrant <i>shall be served in the daytime</i> unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime." (Emphasis added.) The fact that Congress, when it has intended to require such special showings for nighttime searches, has done so in language largely free from ambiguity militates against petitioner's assertion that the language of § 879 (a) on its face supports his position.</p>
<p>The legislative history lends no support to petitioner's interpretation, but in fact cuts the other way. Both the House and the Senate Committee Reports on the bill incorporated a summary prepared by the Department of Justice, where much of the bill's drafting had taken place, which stated:</p>
<blockquote>"Section 702 (a) [now § 879 (a)] incorporates 18 U. S. C. [§] 1405 and authorizes service of a search <span class="star-pagination">*457</span> warrant at any time of the day or night if probable cause has been established to the satisfaction of the judge or U. S. magistrate issuing the warrant."<sup>[39]</sup></blockquote>
<p>As previously noted, § 1405 provided that a search warrant could be served at any time of the day or night so long as the issuing officer was "satisfied that there is probable cause to believe that the grounds for the application exist . . . ." Case law had uniformly interpreted the language to mean that probable cause for the warrant itself was all that was necessary for a nighttime search.<sup>[40]</sup> The officers or agents simply had to establish probable cause for believing that the sought-after property would be found in the place to be searched.</p>
<p>There is no suggestion in any of the hearings or debates before Congress that a change from the prior law in this area was intended. The provision itself went unmentioned in the debates and hearings on the bill, a surprising omission if the bill effected the cutback petitioner says it did. Of like import is the fact that in the long and heated discussions over § 702 (b), the so-called "no-knock" provision of the bill, no defender of the bill saw fit to argue that any greater intrusion caused by the no-knock provision would be partially offset by the greater difficulty in obtaining warrants executable at night.<sup>[41]</sup> While congressional silence as to a particular provision of a bill during debates which give extensive consideration to neighboring provisions is not easy to interpret, it would be unusual for such a significant <span class="star-pagination">*458</span> change as that proposed by petitioner to have entirely escaped notice.</p>
<p>Finally, it is important to note that the Department of Justice itself submitted this bill to Congress for enactment, including § 879 (a) in its present form. Since the hearings and debates stress that a major purpose of the bill was to supply more effective enforcement tools to combat the increasing use of narcotic drugs, it seems totally illogical to suggest that the Department of Justice would submit a bill making it substantially more difficult to control the traffic in hard drugs. Petitioner suggests that this surrender was necessary to convince Congress to bring additional drugs within the Controlled Substances Act, but that theory rests entirely on speculation. There is absolutely no indication in the legislative history that any price had to be paid for what was thought to be a much-desired reorganization and expansion of the drug laws, much less the substantial price that petitioner argues had to be paid here.</p>
<p>We therefore conclude that <span class="citation no-link">21 U. S. C. § 879</span> (a) requires no special showing for a nighttime search, other than a showing that the contraband is likely to be on the property or person to be searched at that time.<sup>[42]</sup> We believe that the showing was met in this case. The affidavit submitted by the District of Columbia police officer suggested that there was a continuing traffic of drugs from petitioner's apartment, and a prior purchase through an informer had confirmed that drugs were available. This was sufficient to satisfy <span class="citation no-link">21 U. S. C. § 879</span> (a). The judgment of the Court of Appeals for the District of Columbia Circuit is</p>
<p><i>Affirmed.</i></p>
<p><span class="star-pagination">*459</span> MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BRENNAN and MR. JUSTICE MARSHALL concur, dissenting.</p>
<p>The petitioner is charged with possession of heroin and narcotics paraphernalia in violation of <span class="citation no-link">21 U. S. C. § 174</span> (1964 ed.) and <span class="citation no-link">26 U. S. C. § 4704</span> (a) (1964 ed.). He moved the District Court to suppress certain evidence seized from his home pursuant to a search warrant secured by and directed to the Metropolitan Police Department of the District of Columbia. The District Court granted the suppression motion on the ground that the search was conducted at night in violation of D. C. Code §§ 23-521-523 (1973) which limit search warrant execution to daylight hours absent specific contrary authorization founded upon the judicial officer's determination</p>
<blockquote>"that (A) it cannot be executed during the hours of daylight, (B) the property sought is likely to be removed or destroyed if not seized forthwith, or (C) the property sought is not likely to be found except at certain times or in certain circumstances. . . ." D. C. Code § 23-522 (c) (1).<sup>[1]</sup></blockquote>
<p>Though the warrant here directed a search "at any time in the day or night," none of the grounds set forth in § 23-522 (c) (1) were contained in either the application or the warrant itself. The police obtained the warrant on February 11, 1971, but they failed to execute it during the day of February 12, waiting instead until 9:30 p. m. on that date. Since they delayed execution until well after the daylight hours had ended, <span class="star-pagination">*460</span> the seizure was invalid if governed by D. C. Code §§ 23-521 to 23-523.</p>
<p>The Court holds, however, that the D. C. Code provisions are inapplicable and that the search is governed by <span class="citation no-link">21 U. S. C. § 879</span> (a). That section became effective October 27, 1970, as part of the Controlled Substances Act, <span class="citation no-link">84 Stat. 1242</span>, <span class="citation no-link">21 U. S. C. § 801</span> <i>et seq.;</i> it relates to search warrants issued in connection with offenses involving controlled substances. The D. C. Code provisions, however, became effective February 11, 1971, as part of the District of Columbia Court Reform and Criminal Procedure Act. The latter Act did not distinguish between local and federal prosecutions in its procedural innovations.<sup>[2]</sup> The purpose of the restriction upon nighttime searches was to limit such intrusions to those instances where there is "some justification for it,"<sup>[3]</sup> thus implementing the "policy generally disfavoring nighttime executions, nighttime intrusions, more characteristic of a `police state' lacking in the respect for due process and the right of privacy dictated by the U. S. Constitution and history . . . ."<sup>[4]</sup></p>
<p>Approximately 60% of the search warrants issued in the District of Columbia relate to narcotics violations. Congress was aware of this, and, if it had intended to except federal narcotics search warrants from the protections against unnecessary nighttime "police state" searches, one would expect an expression of such intent. I agree with Judge Gesell that no such intent is indicated. <span class="star-pagination">*461</span> Thus, "[w]hatever be the standards generally for issuance of a nighttime search warrant in federal narcotics cases in other parts of the country . . . the existence of <span class="citation no-link">21 U. S. C. § 879</span> (a) does not remove such cases from the explicit requirements for search warrants in the District of Columbia under the newly enacted Title 23, D. C. Code." <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1007" aria-description="Citation for case: United States v. Gooding">328 F. Supp. 1005, 1007</a></span>. I would reverse the Court of Appeals and sustain the District Court's suppression order.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE DOUGLAS and MR. JUSTICE BRENNAN join, dissenting.</p>
<p>I agree with my Brother DOUGLAS that the provisions of the District of Columbia Code requiring a showing of need for execution of a search warrant at night govern the search involved in this case, and, accordingly, I join in his dissenting opinion. A majority of the Court, however, rejects this argument and goes on to discuss the standards imposed by <span class="citation no-link">21 U. S. C. § 879</span> (a) upon issuance of search warrants for nighttime execution in federal narcotics cases. Obviously, the Court's interpretation of § 879 (a) is of far greater significance, of national rather than purely local concern. I cannot let the Court's construction of § 879 (a) pass without registering my dissent on this issue as well.</p>
<p>The opinion of the Court, it seems to me, analyzes the § 879 (a) issue in a vacuum, without any discussion of some of the important policy considerations which underlie this question of statutory interpretation. Perhaps a partial vacuum would be a more appropriate description, since the Court is obviously fully cognizant of the substantial governmental interest in enforcement of the narcotics laws, an interest which its interpretation of § 879 (a) so well serves. But plainly there are other concerns implicated in our interpretation of this congressional <span class="star-pagination">*462</span> enactment restricting the issuance of search warrantsthe protection of individual privacy which is the very purpose of the statute's search warrant requirement and which of course is given constitutional recognition in the Fourth Amendment. The Court seems totally oblivious to these constitutional considerations. Taking them into account, I find that the only acceptable interpretation of the statute is one which requires some additional justification for authorizing a nighttime search over and above the ordinary showing of probable cause to believe that a crime has been committed and that evidence of the crime will be found upon the search.</p>
<p>Fundamentally at issue in this case is the extent of the protection which we will all enjoy from police intrusion into the privacy of our homes during the middle of the night. The Fourth Amendment was intended to protect our reasonable expectations of privacy from unjustified governmental intrusion. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360-362</a></span> (1967) (Harlan, J., concurring). In my view, there is no expectation of privacy more reasonable and more demanding of constitutional protection than our right to expect that we will be let alone in the privacy of our homes during the night. The idea of the police unnecessarily forcing their way into the home in the middle of the nightfrequently, in narcotics cases, without knocking and announcing their purposerousing the residents out of their beds, and forcing them to stand by in indignity in their night clothes while the police rummage through their belongings does indeed smack of a " `police state' lacking in the respect for . . . the right of privacy dictated by the U. S. Constitution." S. Rep. No. 91-538, p. 12 (1969). The public outrage at the series of mistaken nighttime raids by narcotics agents in Collinsville, Illinois, last <span class="star-pagination">*463</span> April, see N. Y. Times, Apr. 29, 1973, p. 1, col. 5; N. Y. Times, Apr. 30, 1973, p. 30, col. 1, serves to emphasize just how inconsistent with our constitutional guarantees such nighttime searches are.</p>
<p>This Court has consistently recognized that the intrusion upon privacy engendered by a search of a residence at night is of an order of magnitude greater than that produced by an ordinary search. Mr. Justice Harlan observed in holding a nighttime search unconstitutional in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#498" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 498</a></span> (1958): "[I]t is difficult to imagine a more severe invasion of privacy than the nighttime intrusion into a private home." In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#477" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 477</a></span> (1971), the Court again recognized that a midnight entry into a home was an "extremely serious intrusion." And our decision in <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965), was in large part based upon our revulsion at the thought of nighttime searches of the marital bedroom to discover evidence of illegal contraceptive use. See <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#485" aria-description="Citation for case: Griswold v. Connecticut"><i>id.,</i> at 485-486</a></span>.</p>
<p>It is small wonder, then, that Congress has consistently required more stringent justification for nighttime searches than that needed to authorize a search during the day. The first congressional enactment setting out comprehensive search warrant procedures, § 10 of Tit. XI of the Espionage Act of 1917, <span class="citation no-link">40 Stat. 217</span>, 229, <span class="citation no-link">18 U. S. C. § 620</span> (1940 ed.), required that the affiant must be "positive" that the property to be seized was on the premises to justify a nighttime search. When the provisions of the Espionage Act were replaced by the Federal Rules of Criminal Procedure in 1946, this requirement of positivity was carried forward in Rule 41. Despite the stringency of this requirement, it remained with us until very recently, until the 1972 amendments to Rule 41. And although the Rule was then modified to require <span class="star-pagination">*464</span> "reasonable cause" for nighttime execution of a warrant, significantly the amended Rule retained the principle that nighttime searches require an additional showing of justification over and above probable cause. Congress has also manifested its concern for protection of individual privacy against nighttime searches in its legislation for the District of Columbia, as MR. JUSTICE DOUGLAS' opinion amply demonstrates with respect to enactment of the D. C. Court Reform and Criminal Procedure Act in 1970. <i>Ante,</i> at 460.<sup>[1]</sup></p>
<p>The strong policy underlying these congressional enactments is clear. As even the Government in this case concedes, "searches conducted in the middle of the night . . . involve a greater intrusion than ordinary searches and therefore require a greater justification." Brief for United States 14. In my view, this principle may well be a constitutional imperative. It is by now established Fourth Amendment doctrine that increasingly severe standards of probable cause are necessary to justify increasingly intrusive searches. In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), after holding that search warrants were required to authorize administrative inspections, we held that the quantum of probable cause required for issuance of an inspection warrant must be determined in part by the reasonableness of the proposed search. As MR. JUSTICE WHITE stated, "there can be no ready test for determining reasonableness other than by balancing the need to search against the invasion which the search entails." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 536-537</a></span>. The Court in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> thus approved the issuance <span class="star-pagination">*465</span> of area inspection warrants in part because such searches "involve a relatively limited invasion of the urban citizen's privacy." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 537</a></span>. See also <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/" aria-description="Citation for case: Couch v. United States">409 U. S. 322</a></span>, 349 n. 6 (1973) (MARSHALL, J., dissenting). I do not regard this principle as a one-way street, to be used only to water down the requirement of probable cause when necessary to authorize governmental intrusions. In some situationsand the search of a private home during nighttime would seem to be a paradigm this principle requires a showing of additional justification for a search over and above, the ordinary showing of probable cause. Cf. <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 485-486</a></span> (1965).</p>
<p>Of course, this constitutional question is not presented in this case and need not be resolved here. But the long history of congressional authorization of nighttime searches only upon a showing of additional justification, the strong constitutionally based policy which these statutes implement, and the substantial constitutional question posed by the majority's interpretation of § 879 (a) are surely relevant to the question of statutory interpretation with which we are faced. Viewed against this background, I think it is plain that the majority's interpretation of the statute should be rejected.</p>
<p>Section 879 (a) provides that search warrants may be executed at night only if "there is probable cause to believe that grounds exist for the warrant and for its service at such time." It seems to me quite clear that the statute, on its face, imposes two distinct requirements: that there be probable cause for the issuance of the warrant, and that there be cause "for its service at such time." While the Court relies on legislative history which suggests that § 879 (a) merely "incorporates" the provisions of its predecessor, <span class="citation no-link">18 U. S. C. § 1405</span> (1964 ed.), the plain <span class="star-pagination">*466</span> fact is that § 879 (a) does far more than this: it also adds to the language of § 1405 the final clause"and for its service at such time"which is at the heart of the dispute in this case. I can see no plausible interpretation of this final clause other than that it imposes an additional requirement of justification for a search at night over and above a showing of probable cause.</p>
<p>The Court, while conceding this to be a "possible" meaning of the statute's final clause, argues that "it is by no means the only possible meaning attributable to the words." <i>Ante,</i> at 455. Unfortunately, the Court then fails to come forward with any alternative interpretation of these final words of § 879 (a). Instead, the Court simply reads the disputed language out of the statute entirely, and decrees that the statute shall be interpreted as if it were not there. The Court holds that the statute requires only "a showing that the contraband is likely to be on the property or person to be searched at that time" to justify nighttime execution of a search warrant. <i>Ante,</i> at 458. But the showing of probable cause required for issuance of any warrant necessarily includes a showing that the objects to be seized will probably be found on the premises at the time of the search. See <i>Sgro</i> v. <i>United States,</i> <span class="citation" data-id="9418758"><a href="/opinion/101970/sgro-v-united-states/#210" aria-description="Citation for case: Sgro v. United States">287 U. S. 206, 210-211</a></span> (1932); <i>Schoeneman</i> v. <i>United States,</i> 115 U. S. App. D. C. 110, 113, <span class="citation" data-id="260559"><a href="/opinion/260559/harry-carl-schoeneman-v-united-states-of-america-garlan-euel-markham-jr/#176" aria-description="Citation for case: Harry Carl Schoeneman v. United States of America, Garlan...">317 F. 2d 173, 176-177</a></span> (1963); <i>Rosencranz</i> v. <i>United States,</i> <span class="citation" data-id="270626"><a href="/opinion/270626/samuel-rosencranz-v-united-states-of-america-anthony-dipietro-v-united/#315" aria-description="Citation for case: Samuel Rosencranz v. United States of America, Anthony...">356 F. 2d 310, 315-318</a></span> (CA1 1966). This requirement is clearly imposed by the Fourth Amendment itself. It is also clearly mandated by the first part of the statutory language, which merely incorporates the constitutional requirement of probable cause for issuance of the warrant. The majority's interpretation of the statute thus leaves the final clause of § 879 (a)the language in controversy heretotally without meaning. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="9751925"><a href="/opinion/2307321/united-states-v-thomas/#170" aria-description="Citation for case: United States v. Thomas">294 A. 2d 164, 170</a></span> (DC Ct. App.) <span class="star-pagination">*467</span> (Kelly, J., dissenting), cert. denied, <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/" aria-description="Citation for case: Thomas v. United States">409 U. S. 992</a></span> (1972); <i>United States</i> v. <i>Gooding,</i> 155 U. S. App. D. C. 259, 273, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#442" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428, 442</a></span> (1973) (Robinson, J., concurring in result). I cannot subscribe to such an evisceration of the statute.<sup>[2]</sup></p>
<p><span class="star-pagination">*468</span> The Court bases its holding upon the meager recorded legislative history of § 879 (a). But when the language of a statute is as clear and unambiguous as it is here, it is neither helpful nor appropriate to look to its legislative history. <i>Ex parte Collett,</i> <span class="citation" data-id="9420318"><a href="/opinion/104671/ex-parte-collett/#61" aria-description="Citation for case: Ex Parte Collett">337 U. S. 55, 61</a></span> (1949); <i>United States</i> v. <i>Oregon,</i> <span class="citation" data-id="9422227"><a href="/opinion/106253/united-states-v-oregon/#648" aria-description="Citation for case: United States v. Oregon">366 U. S. 643, 648</a></span> (1961). While committee reports in particular are often a helpful guide to the meaning of ambiguous statutory language, even they must be disregarded if inconsistent with the plain language of the statute. <i>Helvering</i> v. <i>City Bank Farmers Trust Co.,</i> <span class="citation" data-id="102494"><a href="/opinion/102494/helvering-v-city-bank-farmers-trust-co/#89" aria-description="Citation for case: Helvering v. City Bank Farmers Trust Co.">296 U. S. 85, 89</a></span> (1935); <i>George Van Camp &amp; Sons Co.</i> v. <i>American Can Co.,</i> <span class="citation" data-id="101357"><a href="/opinion/101357/george-van-camp-sons-co-v-american-can-co/#253" aria-description="Citation for case: George Van Camp &amp; Sons Co. v. American Can Co.">278 U. S. 245, 253-254</a></span> (1929). It is the language of the statute, as enacted by the Congress, that is the law of the land, not the language of a committee report which may or may not represent accurately the views of the hundreds of other legislators who voted for the bill.</p>
<p>In any event, even if resort to examination of the legislative history were appropriate here, I do not find it nearly so conclusive as does the majority of the Court. The Court relies on a single brief statement on § 879 (a) in the committee report stating that the statute merely incorporated the provisions of § 1405, which had been construed not to impose any requirement for a nighttime search warrant over and above probable cause. Yet this statement fails to provide any explanation for the language which Congress added to § 1405, the language <span class="star-pagination">*469</span> in controversy here. As to the meaningor, as the Court would have it, the lack of meaningof this language, the Court relies basically upon the law enforcement goals of the Department of Justice and the silence of Congress. But, as we have frequently warned, "[i]t is at best treacherous to find in congressional silence alone the adoption of a controlling rule of law." <i>Girouard</i> v. <i>United States,</i> <span class="citation" data-id="9419823"><a href="/opinion/104285/girouard-v-united-states/#69" aria-description="Citation for case: Girouard v. United States">328 U. S. 61, 69</a></span> (1946); see H. M. Hart &amp; A. Sacks, The Legal Process:Basic Problems in the Making and Application of Law 1395-1398 (tent. ed. 1958), and cases there cited. The Court in effect presumes from Congress' failure to explain the meaning of the final clause of § 879 (a) its acquiescence in the Justice Department's apparent view that this language in fact serves no purpose.</p>
<p>I would presume the contrary. Congress' consistent protection of nighttime privacy by imposing restrictions upon the availability of warrants for nighttime searches reinforces the unambiguous statutory language. Both lead me to the conclusion that the final clause of § 879 (a) must be viewed as another congressional manifestation of its strong policy against nighttime intrusions into the home. I do not think that this interpretation is at all inconsistent with the narcotics law-enforcement objectives which were the principal focus of this legislation. The requirement that cause be shown for the necessity of a nighttime search is still a substantial easing of the requirement of positivity which was then embodied in Rule 41, and which would otherwise have applied to many of the searches now covered by § 879 (a). I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  The Government contends that even though we were to determine that the applicable statutory provision was violated in this case, the evidence should nonetheless not be suppressed. Since we conclude that the seizure was consistent with the governing statute, we have no occasion to reach this alternative argument.</p>
<p>[2]  See 155 U. S. App. D. C. 259, 261, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#430" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428, 430</a></span> (1973), quoting from <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1008" aria-description="Citation for case: United States v. Gooding">328 F. Supp. 1005, 1008</a></span> (DC 1971).</p>
<p>[3]  "§ 33-414. Search warrantsRequirementsFormContents ReturnPenalty for interfering with service.
</p>
<p>"(a) A search warrant may be issued by any judge of the Superior Court of the District of Columbia or by a United States commissioner for the District of Columbia when any narcotic drugs are manufactured, possessed, controlled, sold, prescribed, administered, dispensed, or compounded, in violation of the provisions of this chapter, and any such narcotic drugs and any other property designed for use in connection with such unlawful manufacturing, possession, controlling, selling, prescribing, administering, dispensing, or compounding, may be seized thereunder, and shall be subject to such disposition as the court may make thereof and such narcotic drugs may be taken on the warrant from any house or other place in which they are concealed.</p>
<p>"(b) A search warrant cannot be issued but upon probable cause supported by affidavit particularly describing the property and the place to be searched.</p>
<p>"(c) The judge or commissioner must, before issuing the warrant, examine on oath the complainant and any witnesses he may produce, and require their affidavits or take their depositions in writing and cause them to be subscribed by the parties making them.</p>
<p>"(d) The affidavits or depositions must set forth the facts tending to establish the grounds of the application or probable cause for believing that they exist.</p>
<p>"(e) If the judge or commissioner is thereupon satisfied of the existence of the grounds of the application or that there is probable cause to believe their existence, he must issue a search warrant, signed by him, to the major and superintendent of police of the District of Columbia or any member of the Metropolitan police department, stating the particular grounds or probable cause for its issue and the names of the persons whose affidavits have been taken in support thereof, and commanding him forthwith to search the place named for the property specified and to bring it before the judge or commissioner.</p>
<p>"(f) A search warrant may in all cases be served by any of the officers mentioned in its direction, but by no other person, except in aid of the officer on his requiring it, he being present and acting in its execution.</p>
<p>"(g) The officer may break open any outer or inner door or window of a house, or any part of a house, or anything therein, to execute the warrant, if, after notice of his authority and purpose, he is refused admittance.</p>
<p>"(h) The judge or commissioner shall insert a direction in the warrant that it may be served at any time in the day or night."</p>
<p>[4]  "§ 23-521. Nature and issuance of search warrants
</p>
<p>"(a) Under circumstances described in this subchapter, a judicial officer may issue a search warrant upon application of a law enforcement officer or prosecutor. A warrant may authorize a search to be conducted anywhere in the District of Columbia and may be executed pursuant to its terms.</p>
<p>"(b) A search warrant may direct a search of any or all of the following:</p>
<p>"(1) one or more designated or described places or premises;</p>
<p>"(2) one or more designated or described vehicles;</p>
<p>"(3) one or more designated or described physical objects; or</p>
<p>"(4) designated persons.</p>
<p>"(c) A search warrant may direct the seizure of designated property or kinds of property, and the seizure may include, to such extent as is reasonable under all the circumstances, taking physical or other impressions, or performing chemical, scientific, or other tests or experiments of, from, or upon designated premises, vehicles, or objects.</p>
<p>"(d) Property is subject to seizure pursuant to a search warrant if there is probable cause to believe that it</p>
<p>"(1) is stolen or embezzled;</p>
<p>"(2) is contraband or otherwise illegally possessed;</p>
<p>"(3) has been used or is possessed for the purpose of being used, or is designed or intended to be used, to commit or conceal the commission of a criminal offense; or</p>
<p>"(4) constitutes evidence of or tends to demonstrate the commission of an offense or the identity of a person participating in the commission of an offense.</p>
<p>"(e) A search warrant may be addressed to a specific law enforcement officer or to any classification of officers of the Metropolitan Police Department of the District of Columbia or other agency authorized to make arrests or execute process in the District of Columbia.</p>
<p>"(f) A search warrant shall contain</p>
<p>"(1) the name of the issuing court, the name and signature of the issuing judicial officer, and the date of issuance;</p>
<p>"(2) if the warrant is addressed to a specific officer, the name of that officer, otherwise, the classifications of officers to whom the warrant is addressed;</p>
<p>"(3) a designation of the premises, vehicles, objects, or persons to be searched, sufficient for certainty of identification;</p>
<p>"(4) a description of the property whose seizure is the object of the warrant;</p>
<p>"(5) a direction that the warrant be executed during the hours of daylight or, where the judicial officer has found cause therefor, including one of the grounds set forth in section 23-522 (c) (1), an authorization for execution at any time of day or night;</p>
<p>"(6) where the judicial officer has found cause therefor, including one of the grounds set forth in subparagraph (A), (B), or (D) of section 23-591 (c) (2), an authorization that the executing officer may break and enter the dwelling house or other building or vehicles to be searched without giving notice of his identity and purpose; and</p>
<p>"(7) a direction that the warrant and an inventory of any property seized pursuant thereto be returned to the court on the next court day after its execution.</p>
<p>"§ 23-522. Applications for search warrants</p>
<p>"(a) Each application for a search warrant shall be made in writing upon oath or affirmation to a judicial officer.</p>
<p>"(b) Each application shall include</p>
<p>"(1) the name and title of the applicant;</p>
<p>"(2) a statement that there is probable cause to believe that property of a kind or character described in section 23-521 (d) is likely to be found in a designated premise, in a designated vehicle or subject, or upon designated persons;</p>
<p>"(3) allegations of fact supporting such statement; and</p>
<p>"(4) a request that the judicial officer issue a search warrant directing a search for and seizure of the property in question.</p>
<p>"The applicant may also submit depositions or affidavits of other persons containing allegations of fact supporting or tending to support those contained in the application.</p>
<p>"(c) The application may also contain</p>
<p>"(1) a request that the search warrant be made executable at any hour of the day or night, upon the ground that there is probable cause to believe that (A) it cannot be executed during the hours of daylight, (B) the property sought is likely to be removed or destroyed if not seized forthwith, or (C) the property sought is not likely to be found except at certain times or in certain circumstances; and</p>
<p>"(2) a request that the search warrant authorize the executing officer to break and enter dwelling houses or other buildings or vehicles to be searched without giving notice of his identity and purpose, upon probable cause to believe that one of the conditions set forth in subparagraph (A), (B), or (D) of section 23-591 (c) (2) is likely to exist at the time and place at which such warrant is to be executed.</p>
<p>"Any request made pursuant to this subsection must be accompanied and supported by allegations of fact supporting such request."</p>
<p>[5]  At the time of the search in this case Rule 41 read, in part, as follows:
</p>
<p>"Search and Seizure</p>
<p>"(a) Authority to Issue Warrant. A search warrant authorized by this rule may be issued by a judge of the United States or of a state, commonwealth or territorial court of record or by a United States commissioner within the district wherein the property sought is located.</p>
<p>"(b) Grounds for Issuance. A warrant may be issued under this rule to search for and seize any property</p>
<p>"(1) Stolen or embezzled in violation of the laws of the United States; or</p>
<p>"(2) Designed or intended for use or which is or has been used as the means of committing a criminal offense; or</p>
<p>"(3) Possessed, controlled, or designed or intended for use or which is or has been used in violation of Title <span class="citation no-link">18, U. S. C., § 957</span>.</p>
<p>"(c) Issuance and contents. A warrant shall issue only on affidavit sworn to before the judge or commissioner and establishing the grounds for issuing the warrant. If the judge or commissioner is satisfied that grounds for the application exist or that there is probable cause to believe that they exist, he shall issue a warrant identifying the property and naming or describing the person or place to be searched. The warrant shall be directed to a civil officer of the United States authorized to enforce or assist in enforcing any law thereof or to a person so authorized by the President of the United States. It shall state the grounds or probable cause for its issuance and the names of the persons whose affidavits have been taken in support thereof. It shall command the officer to search forthwith the person or place named for the property specified. The warrant shall direct that it be served in the daytime, but if the affidavits are positive that the property is on the person or in the place to be searched, the warrant may direct that it be served at any time. It shall designate the district judge or the commissioner to whom it shall be returned.</p>
<p>.....</p>
<p>"(g) Scope and Definition. This rule does not modify any act, inconsistent with it, regulating search, seizure and the issuance and execution of search warrants in circumstances for which special provision is made. The term `property' is used in this rule to include documents, books, papers and any other tangible objects."</p>
<p>[6]  Rule 41 has since been amended to read, in part:
</p>
<p>"(a) Authority to issue warrant. A search warrant authorized by this rule may be issued by a federal magistrate or a judge of a state within the district wherein the property sought is located, upon request of a federal law enforcement officer or an attorney for the government.</p>
<p>"(b) Property which may be seized with a warrant. A warrant may be issued under this rule to search for and seize any (1) property that constitutes evidence of the commission of a criminal offense; or (2) contraband, the fruits of crime, or things otherwise criminally possessed; or (3) property designed or intended for use or which is or has been used as the means of committing a criminal offense.</p>
<p>"(c) Issuance and contents. A warrant shall issue only on an affidavit or affidavits sworn to before the federal magistrate or state judge and establishing the grounds for issuing the warrant. If the federal magistrate or state judge is satisfied that grounds for the application exist or that there is probable cause to believe that they exist, he shall issue a warrant identifying the property and naming or describing the person or place to be searched. The finding of probable cause may be based upon hearsay evidence in whole or in part. Before ruling on a request for a warrant the federal magistrate or state judge may require the affiant to appear personally and may examine under oath the affiant and any witnesses he may produce, provided that such proceeding shall be taken down by a court reporter or recording equipment and made part of the affidavit. The warrant shall be directed to a civil officer of the United States authorized to enforce or assist in enforcing any law thereof or to a person so authorized by the President of the United States. It shall command the officer to search, within a specified period of time not to exceed 10 days, the person or place named for the property specified. The warrant shall be served in the daytime, unless the issuing authority, by appropriate provision in the warrant, and for reasonable cause shown, authorizes its execution at times other than daytime. It shall designate a federal magistrate to whom it shall be returned.</p>
<p>.....</p>
<p>"(h) Scope and definition. This rule does not modify any act, inconsistent with it, regulating search, seizure and the issuance and execution of search warrants in circumstances for which special provision is made. The term `property' is used in this rule to include documents, books, papers and any other tangible objects. The term `daytime' is used in this rule to mean the hours from 6:00 a. m. to 10:00 p. m. according to local time. The phrase `federal law enforcement officer' is used in this rule to mean any government agent, other than an attorney for the government as defined in Rule 54 (c), who is engaged in the enforcement of the criminal laws and is within any category of officers authorized by the Attorney General to request the issuance of a search warrant."</p>
<p>[7]  § 10, <span class="citation no-link">40 Stat. 229</span>.</p>
<p>[8]  "<span class="citation no-link">21 U. S. C. § 879</span>. Search warrants.
</p>
<p>"(a) A search warrant relating to offenses involving controlled substances may be served at any time of the day or night if the judge or United States magistrate issuing the warrant is satisfied that there is probable cause to believe that grounds exist for the warrant and for its service at such time."</p>
<p>[9]  "§ 1405. Issuance of search warrantsprocedure.
</p>
<p>"In any case involving a violation of any provision of part I or part II of subchapter A of chapter 39 of the Internal Revenue Code of 1954 the penalty for which is provided is subsection (a) or (b) of section 7237 of such code, a violation of subsection (c), (h), or (i) of section 2 of the Narcotic Drugs Import and Export Act, as amended (<span class="citation no-link">21 U. S. C., sec. 174</span>), or a violation of the Act of July 11, 1941, as amended (21 U. S. C., sec 184a)</p>
<p>"(1) a search warrant may be served at any time of the day or night if the judge or the United States Commissioner issuing the warrant is satisfied that there is probable cause to believe that the grounds for the application exist, and</p>
<p>"(2) a search warrant may be directed to any officer of the Metropolitan Police of the District of Columbia authorized to enforce or assist in enforcing a violation of any of such provisions."</p>
<p>[10]  See, <i>e. g.,</i> H. R. Rep. No. 2546, 84th Cong., 2d Sess., 16 (1956).</p>
<p>[11]  See, <i>e. g., </i><i>United States</i> v. <i>Stallings,</i> <span class="citation" data-id="9454706"><a href="/opinion/285611/united-states-v-eulice-stallings-william-earl-wilson/" aria-description="Citation for case: United States v. Eulice Stallings, William Earl Wilson">413 F. 2d 200</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/972/">396 U. S. 972</a></span> (1969); <i>United States</i> v. <i>Castle,</i> <span class="citation" data-id="2293098"><a href="/opinion/2293098/united-states-v-castle/" aria-description="Citation for case: United States v. Castle">213 F. Supp. 52</a></span> (DC 1962).
</p>
<p>Our Brother MARSHALL in his dissenting opinion stresses Congress' continuing concern for individual privacy, as demonstrated by the limitations on nighttime searches contained in the Espionage Act, <i>supra,</i> and later, Fed. Rule Crim. Proc 41. The implication seems to be that this concern must be read into the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) to reach the interpretation for which he argues. But this argument totally ignores the fact that Congress, in 1956, enacted a statute governing searches for dangerous drugs which deliberately removed the stricter limitations on night searches found in Rule 41. Our construction of the principal statute considered in this case, <span class="citation no-link">21 U. S. C. § 879</span> (a), therefore, represents no novel departure from previous congressional policy in this area, but is, on the contrary, consistent with the conceded meaning of the statute which governed federal drug searches for almost 15 years.</p>
<p>[12]  The affidavit read in full:
</p>
<p>"BEFORE Lawrence S. Margolis, Wash., D. C. The undersigned being duly sworn deposes and says:</p>
<p>"That he (has reason to believe) that (on the premises known as) 1419 Chapin Street, N. W., as you enter the building last apartment on the right next to the elevator on the first floor Washington in the District of Columbia there is now being concealed certain property, namely heroin, syringes, tourniquets, cookers and paraphernalia used in the preparation of heroin for retail and any other paraphernalia used in the preparation and dispensation of heroin and any other narcotic drugs illegally held, which are in violation of Title 26 U. S. Code Section 4704 (a).</p>
<p>"And that the facts tending to establish the foregoing grounds for issuance of a Search Warrant are as follows: See the facts set forth in the affidavit attached hereto and made a part hereof.</p>
                                   /s/  Marion L. Green
                                        MARION L. GREEN
                                        MPD"

<p>[13]  The affidavit states specifically:
</p>
<p>"I, the undersigned officer who is assigned to the Third District Vice Squad, Metropolitan Police Department, and working in the City of Washington, D. C. in an undercover capacity where illegal drugs are sold and possessed in violation of the United States Code, Title 26, Section 4704a. Had the occasion to investigate the following offense."</p>
<p>[14]  The warrant read in its entirety:
</p>
<p>"To Chief of Police or any Member of MPDC</p>
<p>"Affidavit having been made before me by Plc. Marrion [<i>sic</i>] L. Green, Jr. Third District Vice Squad that he (has reason to believe) that (on the premises known as) 1419 Chapin Street, N. W., as you enter the building last apartment on the right next to the elevator on the first floor, Washington in the District of Columbia, there is now being concealed certain property, namely heroin, capsules, envelopes, syringes, tourniquets, cookers and paraphernalia used in the preparation of heroin for distribution or use and any other instrumentalities or evidence of illegal possession or dispensation of heroin or of any other narcotic drugs illegally held. See the facts set forth in the affidavit attached hereto and made a part hereof which are in violation of Title 26 Section 4704 (a) of the U. S. Code, and as I am satisfied that there is probable cause to believe that the property so described is being concealed on the (premises) above described and that the foregoing grounds for application for issuance of the search warrant exist.</p>
<p>"<i>You are hereby commanded</i> to search forthwith the (place) named for the property specified, serving this warrant and making the search (at any time in the day or night[*]) and if the property be found there to seize it, leaving a copy of this warrant and a receipt for the property taken, and prepare a written inventory of the property seized and return this warrant and bring the property before me within ten days of this date, as required by law.</p>
  "Dated this day of Feb. 11, 1971
                               /s/   Lawrence S. Margolis
                                     U. S. Commissioner"
<p>"[*] The Federal Rules of Criminal Procedure provide: `The warrant shall direct that it be served in the daytime, but if the affidavits are positive that the property is on the person or in the place to be searched, the warrant may direct that it be served at any time.' (Rule 41C)."</p>
<p>[15]  Reply Brief for Petitioner 8.</p>
<p>[16]  The Government contends in its brief, apparently for the first time in the course of this litigation, that the search was not in fact a nighttime search. The primary basis for this argument is revised Fed. Rule Crim. Proc. 41 which states that "[t]he term `daytime' is used in this rule to mean the hours from 6:00 a. m. to 10:00 p. m. according to local time." See n. 6, <i>supra.</i> In view of our conclusion that the standards for a nighttime as well as a daytime search under <span class="citation no-link">21 U. S. C. § 879</span> (a) were met in this case, we do not need to resolve this issue.</p>
<p>[17]  "§ 4704. Packages.
</p>
<p>"(a) General requirement.</p>
<p>"It shall be unlawful for any person to purchase, sell, dispense, or distribute narcotic drugs except in the original stamped package or from the original stamped package; and the absence of appropriate taxpaid stamps from narcotic drugs shall be prima facie evidence of a violation of this subsection by the person in whose possession the same may be found."</p>
<p>[18]  "§ 174. Same; penalty; evidence.
</p>
<p>"Whoever fraudulently or knowingly imports or brings any narcotic drug into the United States or any territory under its control or jurisdiction, contrary to law, or receives, conceals, buys, sells, or in any manner facilitates the transportation, concealment, or sale of any such narcotic drug after being imported or brought in, knowing the same to have been imported or brought into the United States contrary to law, or conspires to commit any of such acts in violation of the laws of the United States, shall be imprisoned not less than five or more than twenty years and, in addition, may be fined not more than $20,000. For a second or subsequent offense (as determined under section 7237 (c) of the Internal Revenue Code of 1954), the offender shall be imprisoned not less than ten or more than forty years and, in addition, may be fined not more than $20,000."</p>
<p>[19]  Petitioner also contended that the officers entered the apartment without knocking and without having a "no-knock" warrant and that the police had no probable cause to search him. Neither court below passed upon the sufficiency of these contentions, and they are not before us here.</p>
<p>[20]  <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1007" aria-description="Citation for case: United States v. Gooding">328 F. Supp., at 1007</a></span>.</p>
<p>[21]  <i><span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/" aria-description="Citation for case: United States v. Gooding">Id.,</a></span></i> at 1008 n. 1.</p>
<p>[22]  <span class="citation" data-id="8789325"><a href="/opinion/8805087/united-states-v-gooding/#1008" aria-description="Citation for case: United States v. Gooding"><i>Id.,</i> at 1008</a></span>.</p>
<p>[23]  155 U. S. App. D. C. 259, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d 428</a></span> (1973).</p>
<p>[24]  Judge Wilkey stated in his opinion: "We hold that the applicable statute, <span class="citation no-link">21 U. S. C. § 879</span> (a), requires only a showing of probable cause to believe that the narcotics will be found on the premises at any time of the day or night." <span class="citation no-link"><i>Id.,</i> at 266</span>, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#435" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 435</a></span>. Judge Fahy in his opinion stated: "Thus, in the case of narcotics, previously under Section 1405 (1) and later under Section 879 (a), if the judge was satisfied `that there is probable cause to believe' rather than `if the affidavits are positive' that the `property is on the person or in the place to be searched,' the warrant could permit execution at any time." <i>Id.,</i> at 268, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#437" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 437</a></span>.</p>
<p>[25]  Judge Robinson concluded: "The test of reasonable cause for nighttime execution does not demand a demonstration that drugs are positively on the premises at night, or that they could be found on the premises only at night, or that for some reason a search would be impossible in the daytime. It does summon some factual basis for a prudent conclusion that the greater intrusiveness of nighttime execution of the warrant is justified by the exigencies of the situation." <i>Id.,</i> at 274, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#443" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 443</a></span>. Judge Robinson then went on to find that a proper showing had been made in this case. He stated: "Where, as here, it appears that a search is calculated not only to garner evidence of past crime but also to terminate a serious species of ongoing criminality, reasonable cause for a nocturnal intrusion is demonstrated." <i>Id.,</i> at 275, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#444" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 444</a></span>.</p>
<p>[26]  We are therefore not required to reach the Government's argument that, despite the fact that the application for the search warrant alleged a violation of the United States Code, the search could be justified under D. C. Code § 33-414 as a search for violations of local drug laws.</p>
<p>[27]  The provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) prevail over the provisions of Fed. Rule Crim. Proc. 41 when controlled substances are involved. See nn. 10 and 11, <i>supra.</i></p>
<p>[28]  See n. 9, <i>supra.</i></p>
<p>[29]  For example, John Ingersoll, Director of the Bureau of Narcotics and Dangerous Drugs, stated at the Hearings on Drug Abuse Control Amendments1970 before the Subcommittee on Public Health and Welfare of the House Committee on Interstate and Foreign Commerce, 91st Cong., 2d Sess., ser. 91-45, pt. 1, p. 86 (1970), that the no-knock provision, incorporated in § 702 (b) of the proposed bill, see n. 32, <i>infra,</i> would grant authority "restricted to special agents of the Bureau of Narcotics and Dangerous Drugs." In addition, the preceding provision of the bill set forth expanded powers for the agents of the BNDD. However, although these excerpts would argue for petitioner's position here, we believe that the Government's position ultimately proves to be stronger. We believe for the reasons stated in the text that the emphasis on the powers of the BNDD agents was not intended to remove powers from other federal agents who had previously assisted in the enforcement of federal drug laws. See also <span class="citation no-link">18 U. S. C. §§ 3052</span>, 3053, and 3056, setting forth arrest powers for agents of the Federal Bureau of Investigation, United States marshals, and Secret Service agents.</p>
<p>[30]  S. Rep. No. 91-613, p. 3 (1969).</p>
<p>[31]  D. C. Code § 4-138 provides:
</p>
<p>"Any warrant for search or arrest, issued by any magistrate of the District, may be executed in any part of the District by any member of the police force, without any backing or indorsement of the warrant, and according to the terms thereof; and all provisions of law in relation to bail in the District shall apply to this chapter." See <i>Thomas</i> v. <i>United States,</i> <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/#993" aria-description="Citation for case: Thomas v. United States">409 U. S. 992, 993</a></span> (1973) (DOUGLAS, J., dissenting).</p>
<p>[32]  "§ 879. Search warrants.
</p>
<p>.....</p>
<p>"(b) Any officer authorized to execute a search warrant relating to offenses involving controlled substances the penalty for which is imprisonment for more than one year may, without notice of his authority and purpose, break open an outer or inner door or window of a building, or any part of the building, or anything therein, if the judge or United States magistrate issuing the warrant (1) is satisfied that there is probable cause to believe that (A) the property sought may and, if such notice is given, will be easily and quickly destroyed or disposed of, or (B) the giving of such notice will immediately endanger the life or safety of the executing officer or another person, and (2) has included in the warrant a direction that the officer executing it shall not be required to give such notice. Any officer acting under such warrant, shall, as soon as practicable after entering the premises, identify himself and give the reasons and authority for his entrance upon the premises."</p>
<p>See H. R. Rep. No. 91-1444, p. 25 (1970), which stated:</p>
<p>"The purpose of this provision [the no-knock provision], as explained in the hearings, is to provide law enforcement officials with a tool to aid in combatting the illicit traffic in drugs which has proved helpful in all of the 29 States where this authority exists either by statute or common law."</p>
<p>[33]  See Atty. Gen. Order 510-73, <span class="citation no-link">38 Fed. Reg. 7244</span>-7245.</p>
<p>[34]  The effect of Title 23 on other statutes was debated in some detail below. Judge Wilkey in his opinion noted that the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a) were not only enacted after the provisions of Title 23 (although they took effect sooner), but also are more specific in terms of subject matter, <i>i. e.,</i> drug control. 155 U. S. App. D. C., at 262, <span class="citation" data-id="9459426"><a href="/opinion/310420/united-states-v-lonnie-gooding-united-states-of-america-v-leon-f/#431" aria-description="Citation for case: United States v. Lonnie Gooding, United States of America...">477 F. 2d, at 431</a></span>. Thus, as a matter of statutory construction, it is somewhat difficult to see how Title 23 was intended to modify any later, more specific statute. Petitioner no longer suggests that Title 23 must be read into the provisions of <span class="citation no-link">21 U. S. C. § 879</span> (a). He contends either that Title 23 is applicable in its entirety or that § 879 (a) by its own terms requires a special showing for searches at night.</p>
<p>[35]  D. C. Code § 11-901.</p>
<p>[36]  "Rule 41. Search and Seizure.
</p>
<p>"(a) Authority to Issue Warrant. A search warrant authorized by this rule may be issued by a judge of the Superior Court.</p>
<p>"(b) Grounds for Issuance. A warrant may be issued under this rule to search for and seize property. Property is subject to seizure pursuant to a search warrant if there is probable cause to believe that it (1) is stolen or embezzled; or (2) is contraband or otherwise illegally possessed; or (3) has been used or is possessed for the purpose of being used, or is designed or intended to be used, to commit or conceal the commission of an offense; or (4) constitutes evidence of or tends to demonstrate the commission of an offense or the identify of a person participating in the commission of an offense.</p>
<p>"(c) Application for Search Warrants. Each application for a search warrant shall be made in writing upon oath to a judge of the Superior Court. Each application shall include the name and title of the applicant; a statement that there is probable cause to believe that property described in paragraph (b) as subject to seizure is likely to be found in a designated premise, in a designated vehicle or object, or upon designated persons; allegations of fact supporting such statement; and a request that the judge issue a search warrant directing a search for and seizure of the property in question. The applicant may also submit depositions or affidavits of other persons containing allegations of fact supporting or tending to support those contained in the application.</p>
<p>"The application may also contain (1) a request that the search warrant be made executable at any hour of the day or night, upon the ground that (i) there is probable cause to believe that it cannot be executed during the hours of daylight, or (ii) the property sought is likely to be removed or destroyed if not seized forthwith, or (iii) the property sought is not likely to be found except at certain times or in certain circumstances; and (2) a request approved by an appropriate prosecutor that the search warrant authorize the executing officer to break and enter dwelling houses or other buildings or vehicles to be searched without giving notice of his identity and purpose, upon probable cause to believe that one of the conditions listed in subparagraphs (a), (b), or (d) of D. C. Code § 23-591 (c) (2) is likely to exist at the time and place at which such warrant is to be executed whereby the applicant may dispense with such requirement. Any request that a search warrant be executable at any time of the day or night or that a search warrant authorize the executing officer to break and enter without a prior announcement of his identity and purpose must be accompanied and supported by allegations of fact supporting such request." Effective Oct. 25, 1973, paragraph (b) of this rule was amended. Paragraphs (a) and (c) were unchanged.</p>
<p>[37]  We note that the District of Columbia Court of Appeals has indicated that the specific provisions of Title 33 are not qualified by the more general provisions of Title 23 in searches for violations of the local drug laws in the District of Columbia. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="9751925"><a href="/opinion/2307321/united-states-v-thomas/#167" aria-description="Citation for case: United States v. Thomas">294 A. 2d 164, 167-168</a></span>, cert. denied, <span class="citation" data-id="8982903"><a href="/opinion/8990730/thomas-v-united-states/" aria-description="Citation for case: Thomas v. United States">409 U. S. 992</a></span> (1973).</p>
<p>[38]  See Fed. Rule Crim. Proc. 41 (h), <i>supra,</i> n. 6. See also subsection (g) of prior Rule 41, n. 5, <i>supra.</i></p>
<p>[39]  S. Rep. No. 91-613, pp. 30-31 (1969). See also H. R. Rep. No. 91-1444, pt. 1, p. 54 (1970).</p>
<p>[40]  See n. 11, <i>supra.</i></p>
<p>[41]  The debates on this controversial proposal may be found generally in volume 116 of the Congressional Record. See, <i>e. g.,</i> 116 Cong. Rec. 1159-1162, 1164-1177, 33639-33645.</p>
<p>[42]  We note that the Court of Appeals for the Fifth Circuit has recently reached the same conclusion. See <i>United States</i> v. <i>Thomas,</i> <span class="citation" data-id="315831"><a href="/opinion/315831/united-states-v-titus-thomas-aka-tee/" aria-description="Citation for case: United States v. Titus Thomas, AKA Tee">489 F. 2d 664</a></span> (1973).</p>
<p>[1]  D. C. Code § 23-523 (b) directs that all search warrants are to be executed only during daylight hours, absent express authorization pursuant to D. C. Code § 23-521 (f). Section 23-521 (f) (5) allows authorization for nighttime execution where the "judicial officer has found cause therefore, including one of the grounds set forth in section 23-522 (c) (1) . . . ."</p>
<p>[2]  Thus various rules are applicable in the United States District Court for the District of Columbia which are not applicable in district courts elsewhere in the country. See, <i>e. g.,</i> D. C. Code § 23-1322, dealing with detention prior to trial.</p>
<p>[3]  Hearings on Crime in the National Capital before the Senate Committee on the District of Columbia, 91st cong., 1st Sess., pt. 4, p. 1404 (1969).</p>
<p>[4]  S. Rep. No. 91-538, p. 12 (1969).</p>
<p>[1]  Similarly, most of the States' laws provide that search warrants may only be served during the day unless express authorization for a nighttime search is obtained, and such authorization can generally be obtained only by meeting special requirements for a nighttime search. See L. Hall, Y. Kamisar, W. LaFave &amp; J. Israel, Modern Criminal Procedure 259 (3d ed. 1969).</p>
<p>[2]  In an effort to conjure up ambiguity in the statutory language, the Court argues that the statute could have been drawn with more precision, and specifically points out that read literally, the statutory requirement of cause "for its service at such time" would seem to apply to daytime searches as well as those conducted at night. <i>Ante,</i> at 455-456. I readily agree that the statute could have been more artfully drafted, but the fact that it could have been stated in different words hardly justifies disregarding the plain meaning of the statutory language with which we must deal. It ill suits the Court to suggest that this language is ambiguous when the Court is unable to come forward with any plausible alternative construction.
</p>
<p>The Court's suggestion that the statute is ambiguous because it could be literally applied to daytime searches as well as those during the night is wholly insubstantial. As the Court well knows, no one has ever proposed that an additional burden of justification for daytime searches is necessary or appropriate; in sharp contrast, the Congress has consistently acted to protect nighttime privacy through such an additional burden on nighttime searches. The Court's confusion arises only because the words "at such time" in the statute logically refer back to its authorization of service "at any time of the day or night." But this latter phrase has consistently been used in congressional enactments as a shorthand expression for a warrant whose service at night is authorized, see, <i>e. g.,</i> D. C. Code § 33-414 (h), <i>ante,</i> at 433 n. 3; §§ 23-521 (f) (5), 23-522 (c) (1), <i>ante,</i> at 435-436, n. 4; cf. former Fed. Rule Crim. Proc. 41 (c), <i>ante,</i> at 436-437, n. 5, to distinguish such a warrant from any other warrant, which may be served only in the day. Plainly the statute's requirement of cause "for its service at such time" was intended to apply only to nighttime execution of search warrants.</p>
<p>As for the Court's complaint that a requirement of cause for nighttime service of a warrant is not the "traditional limitation" imposed upon nighttime searches, it should suffice to point out that Congress became aware in its consideration of the D. C. Court Reform and Criminal Procedure Act in 1969 that a requirement of cause would provide <i>greater</i> protection for nighttime privacy than the old positivity test, by eliminating unnecessary nighttime searches regardless of how sure police were of their basis for the search. See Hearings on Crime in the National Capital before the Senate Committee on the District of Columbia, 91st Cong., 1st Sess., pt. 4, p. 1404 (1969); Brief for United States 49-50. This change was therefore incorporated into the D. C. Code, see D. C. Code §§ 23-521 to 23-523. It was also adopted in the 1972 amendment to Rule 41. It would hardly be surprising for the Congress to introduce a modification along the same lines into § 879 (a).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Gouled v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Gouled v. United States"
type: case
citation: "255 U.S. 298 (1921)"
parallel_cite: "41 S. Ct. 261; 65 L. Ed. 647"
neutral_cite: 1921 U.S. LEXIS 1826
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1921
date_decided: 1921-02-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1921-02-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gouled v. United States
  varies_by_point: false
  scope_note: "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding — that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable — retains vitality."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/99745/gouled-v-united-states/"
  cluster_id: 99745
  opinion_id: 99745
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Historical (foil)"
related: ["[[Warden v. Hayden]]", "[[Boyd v. United States]]", "[[Weeks v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "mere-evidence-rule", "ruse-entry", "historical"]
holding: "Mere-evidence rule: warrants may seize only contraband, fruits, or instrumentalities, not items of solely evidentiary value (overruled by Warden v. Hayden); entry obtained by stealth or ruse can render a search unreasonable."
lake:
  record_id: Gouled v. United States
  status: verified
  projected_at: 2026-07-06
---

# Gouled v. United States

*255 U.S. 298 (1921)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gouled was suspected of conspiracy to defraud the United States in connection with war contracts. A business acquaintance, acting for federal officers, gained admission to Gouled's office under the pretense of a social/business visit and, in Gouled's absence, took a paper from the office. Later, papers were also seized from the office under search warrants issued on a Department of Justice agent's affidavit. The papers were admitted against Gouled at trial over Fourth and Fifth Amendment objections.

## Issue
(1) Is a search and seizure accomplished by an officer who obtains entry to an office by stealth or social/business pretext, rather than by force, within the Fourth Amendment's prohibition? (2) May a search warrant be used to seize a person's private papers that are of solely evidentiary value?

## Rule
**Entry by stealth or ruse.** A surreptitious taking is no less a Fourth Amendment violation than one by force. The Court held that "whether entrance to the home or office of a person suspected of crime be obtained by a representative of any branch or subdivision of the Government of the United States by stealth, or through social acquaintance, or in the guise of a business call, and whether the owner be present or not when he enters, any search and seizure subsequently and secretly made in his absence, falls within the scope of the prohibition of the Fourth Amendment." — 255 U.S. at 306. ^pin-306

**The mere-evidence rule.** Warrants "may not be used as a means of gaining access to a man's house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but . . . they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it." — *Id.* at 309. ^pin-309

*(This mere-evidence limitation was later overruled by [[Warden v. Hayden]].)*

## Application
On these facts, the federal agent's confederate gained entry to Gouled's office by pretext and, in Gouled's absence, took a document — a clandestine intrusion the Court treated as a Fourth Amendment search and seizure despite the absence of force. As to the warrant-seized papers, the items taken were of purely evidentiary character (an unexecuted contract form, a contract, and an attorney's bill said to be "without pecuniary value" but "evidence more or less injurious"), so under the then-governing rule they could not properly be made the object of a search warrant.

## Conclusion
The clandestine taking and the use of the evidentiary papers violated Gouled's Fourth and Fifth Amendment rights. The mere-evidence rule the case announced was abandoned in [[Warden v. Hayden]] (1967); Gouled survives today chiefly for its holding that a search obtained by stealth or pretext is not thereby removed from the Fourth Amendment.

## Treatment & subsequent history
- **Status:** overruled (in part) *(as of 2026-06-30)* — **Historical**.
- **Mere-evidence rule overruled/abandoned by** [[Warden v. Hayden]] (1967): the Fourth Amendment draws no distinction between "mere evidence" and contraband/fruits/instrumentalities, so evidentiary items may be seized on probable cause. This changes field application — officers may seize evidentiary materials, not only contraband, fruits, and instrumentalities.
- **Surviving principle:** the holding that entry obtained by stealth, ruse, or social pretext can render the ensuing search unreasonable remains good law and is cited in the consent/undercover line (cf. *[[Lewis v. United States (1966)|Lewis v. United States]]* (1966), distinguishing a legitimate undercover business visit).

## Appears on
- [[Trespass]] — *Historical (foil)*

## Sources
- *Gouled v. United States*, 255 U.S. 298 (1921) — https://www.courtlistener.com/opinion/99745/gouled-v-united-states/ — pinpoints: 306, 309.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "837daabd230545e6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gouled v. United States"}, "payload": {"all": [{"cite": "255 U.S. 298", "page": "298", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "255"}, {"cite": "41 S. Ct. 261", "page": "261", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "41"}, {"cite": "65 L. Ed. 647", "page": "647", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1921 U.S. LEXIS 1826", "page": "1826", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1921"}], "display": "255 U.S. 298", "official": {"cite": "255 U.S. 298", "page": "298", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "255"}, "official_selection_present": true, "record_id": "Gouled v. United States"}}
{"assertion_id": "73a08eb46a15b767", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-309", "record_id": "Gouled v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-309", "pinpoint_status": "slip-only", "quote": "may not be used as a means of gaining access to a man's house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but . . . they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it.", "quote_fidelity": "mismatch", "record_id": "Gouled v. United States", "star_marker": null}}
{"assertion_id": "e004d7cc524a811d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-306", "record_id": "Gouled v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-306", "pinpoint_status": "slip-only", "quote": "--- # Gouled v. United States *255 U.S. 298 (1921)* · U.S. Supreme Court · **Historical** · Treatment: **overruled** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouled was suspected of conspiracy to defraud the United States in connection with war contracts. A business acquaintance, acting for federal officers, gained admission to Gouled's office under the pretense of a social/business visit and, in Gouled's absence, took a paper from the office. Later, papers were also seized from the office under search warrants issued on a Department of Justice agent's affidavit. The papers were admitted against Gouled at trial over Fourth and Fifth Amendment objections. ## Issue (1) Is a search and seizure accomplished by an officer who obtains entry to an office by stealth or social/business pretext, rather than by force, within the Fourth Amendment's prohibition? (2) May a search warrant be used to seize a person's private papers that are of solely evidentiary value? ## Rule **Entry by stealth or ruse.** A surreptitious taking is no less a Fourth Amendment violation than one by force. The Court held that", "quote_fidelity": "mismatch", "record_id": "Gouled v. United States", "star_marker": null}}
{"assertion_id": "e493537c43edc2f8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gouled v. United States"}, "payload": {"as_of_content": "1921-02-28", "as_of_treatment": "2026-06-30", "field_i_validity": "superseded", "record_id": "Gouled v. United States", "scope_note": "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding — that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable — retains vitality.", "varies_by_point": false}}
```

### lake record — Gouled v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gouled v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gouled v. United States",
    "case_name_short": "Gouled",
    "case_name_full": "Gouled v. United States",
    "input_case_name": "Gouled v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1921-02-28",
    "year": 1921,
    "docket": null,
    "cluster_id": 99745,
    "lead_opinion_id": 99745,
    "sibling_ids": [
      99745
    ],
    "absolute_url": "/opinion/99745/gouled-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "255 U.S. 298",
      "volume": "255",
      "reporter": "U.S.",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "41 S. Ct. 261",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 647",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "647",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1921 U.S. LEXIS 1826",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1826",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "255 U.S. 298",
        "volume": "255",
        "reporter": "U.S.",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "41 S. Ct. 261",
        "volume": "41",
        "reporter": "S. Ct.",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 647",
        "volume": "65",
        "reporter": "L. Ed.",
        "page": "647",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1921 U.S. LEXIS 1826",
        "volume": "1921",
        "reporter": "U.S. LEXIS",
        "page": "1826",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "255 U.S. 298",
    "official_selection": {
      "court_class": "scotus",
      "selected": "255 U.S. 298",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-306",
      "page": null,
      "quote": "--- # Gouled v. United States *255 U.S. 298 (1921)* \u00b7 U.S. Supreme Court \u00b7 **Historical** \u00b7 Treatment: **overruled** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouled was suspected of conspiracy to defraud the United States in connection with war contracts. A business acquaintance, acting for federal officers, gained admission to Gouled's office under the pretense of a social/business visit and, in Gouled's absence, took a paper from the office. Later, papers were also seized from the office under search warrants issued on a Department of Justice agent's affidavit. The papers were admitted against Gouled at trial over Fourth and Fifth Amendment objections. ## Issue (1) Is a search and seizure accomplished by an officer who obtains entry to an office by stealth or social/business pretext, rather than by force, within the Fourth Amendment's prohibition? (2) May a search warrant be used to seize a person's private papers that are of solely evidentiary value? ## Rule **Entry by stealth or ruse.** A surreptitious taking is no less a Fourth Amendment violation than one by force. The Court held that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-309",
      "page": null,
      "quote": "may not be used as a means of gaining access to a man's house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but . . . they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1921-02-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gouled v. United States",
    "varies_by_point": false,
    "scope_note": "The mere-evidence rule was overruled/abandoned by Warden v. Hayden (1967), which held the Fourth Amendment does not bar the seizure of items of solely evidentiary value. The separate Gouled holding \u2014 that entry obtained by stealth, ruse, or social pretext can render a subsequent search unreasonable \u2014 retains vitality.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Warden v. Hayden",
          "cluster_id": 107465,
          "cite": "387 U.S. 294",
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
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 1882057,
          "cite": [
            "60 S.W.3d 106",
            "2001 Tex. Crim. App. LEXIS 104",
            "2001 WL 1415274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. State",
          "cluster_id": 2104545,
          "cite": [
            "13 S.W.3d 492",
            "2000 WL 246424"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Henry Jerome Hicks",
          "cluster_id": 593876,
          "cite": [
            "978 F.2d 722",
            "298 U.S. App. D.C. 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Andrew Eschweiler",
          "cluster_id": 442818,
          "cite": [
            "745 F.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Berry",
          "cluster_id": 8928076,
          "cite": [
            "722 F.2d 443"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 1753238,
          "cite": [
            "657 S.W.2d 797",
            "1983 Tex. Crim. App. LEXIS 1136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rubio",
          "cluster_id": 8929383,
          "cite": [
            "727 F.2d 786",
            "13 Fed. R. Serv. 365"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Scherer, Jr.",
          "cluster_id": 400981,
          "cite": [
            "673 F.2d 176"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nelson Bunker Hunt and W. Herbert Hunt",
          "cluster_id": 322924,
          "cite": [
            "505 F.2d 931",
            "1974 U.S. App. LEXIS 5521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane1_negative"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Olmstead v. United States",
          "cluster_id": 101320,
          "cite": [
            "277 U.S. 438",
            "48 S. Ct. 564",
            "72 L. Ed. 944",
            "1928 U.S. LEXIS 694",
            "66 A.L.R. 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
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
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nardone v. United States",
          "cluster_id": 103259,
          "cite": [
            "308 U.S. 338",
            "60 S. Ct. 266",
            "84 L. Ed. 307",
            "1939 U.S. LEXIS 1132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffman v. United States",
          "cluster_id": 104912,
          "cite": [
            "95 L. Ed. 2d 1118",
            "71 S. Ct. 814",
            "341 U.S. 479",
            "1951 U.S. LEXIS 1802",
            "95 L. Ed. 1118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Agnello v. United States",
          "cluster_id": 100711,
          "cite": [
            "269 U.S. 20",
            "46 S. Ct. 4",
            "70 L. Ed. 145",
            "1925 U.S. LEXIS 2",
            "51 A.L.R. 409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abel v. United States",
          "cluster_id": 106021,
          "cite": [
            "4 L. Ed. 2d 668",
            "80 S. Ct. 683",
            "362 U.S. 217",
            "1960 U.S. LEXIS 1412"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 104422,
          "cite": [
            "67 S. Ct. 1098",
            "331 U.S. 145",
            "91 L. Ed. 1399",
            "1947 U.S. LEXIS 2936"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNally v. United States",
          "cluster_id": 111945,
          "cite": [
            "97 L. Ed. 2d 292",
            "107 S. Ct. 2875",
            "483 U.S. 350",
            "1987 U.S. LEXIS 2878",
            "55 U.S.L.W. 5011"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gouled v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(99745) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OTk2MTYwMDAwMCZzPTE0MzcyMjgmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2899745%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(99745)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NTEmcz0xMTA4ODImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%2899745%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(99745)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(99745)",
    "indexed_citing_opinions": 766,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 99745,
        "count": 766,
        "count_source": "search"
      }
    ],
    "citation_count": 1256,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gouled-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjI3MjUxNTcmcz0yMTEyMDY5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2899745%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 99745,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 99745,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 99745,
        "cited_id": 99506,
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
    "date_created": "2026-07-05T05:45:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: overruled -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:46:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gouled v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b340-9">
  Mr. Justice Clarke
 </author>
<p id="AbB">
  delivered the opinion of the court.
 </p>
<p id="b340-10">
  In a joint indictment the plaintiff in error, Gouled, one Vaughan, an officer of the United States Army, and a third, an attorney at law, were charged, in the first count, with being parties to a conspiracy to defraud the United States, in violation of § 37 of the Federal Criminal Code, and, in the second count, with having used the mails to
  <span citation-index="1" class="star-pagination" label="303"> 
   *303
   </span>
  promote a scheme to defraud the United States, in violation of § 215 of that Code. Vaughan pleaded guilty, the attorney was acquitted, and Gouled, whom we shall refer to as the defendant, was convicted, and thereupon prosecuted error from the Circuit Court of Appeals, which certifies to this court six questions which we are to consider.
 </p>
<p id="Asfi">
  Of these questions, the first two relate to the admission in evidence of a paper surreptitiously, taken from the office of the defendant by one acting under direction of officers of the Intelligence Department of the Army of the United States, and the remaining four relate to papers taken from defendant’s office, under two search warrants, issued pursuant to the Act of June 15, 1917, c. 30, <span class="citation no-link">40 Stat. 217</span>, 228. It was objected on the trial, and is here insisted, that it was error to admit these papers in evidence because possession of them was obtained by violating the rights secured to the defendant by the Fourth and Fifth Amendments to the Constitution of the United States.
 </p>
<p id="b341-6">
  The Fourth Amendment reads:
 </p>
<blockquote id="b341-7">
  • “The right of the people to be secure in their persons, houses, papers -and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b341-8">
  The part of the Fifth Amendment here involved reads:
 </p>
<blockquote id="Am3g">
  “No person . . . shall be compelled in any criminal case to be a witness against, himself.”
 </blockquote>
<p id="b341-10">
  It would not be possible to add to thé emphasis with which the framers of our Constitution' and this court (in
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, in
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, and in
  <em>
   Silverthorne Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>) have declared the importance to political liberty and to the welfare of our country of the due observance of the. rights guaranteed under the Consti
  <span citation-index="1" class="star-pagination" label="304"> 
   *304
   </span>
  tution by "these two Amendments. The effect of the decisions cited is: that such rights are declared to be indispensable to the “full enjoyment of personal security, personal liberty and private property”; that they are to be regarded as of the very essence of constitutional liberty; and that the guaranty of them is as important and as imperative as are the guaranties of the other fundamental rights of the individual citizen, — the right, to trial by jury, to the writ of
  <em>
   habeas corpus
  </em>
  and to due process of law. It has been repeatedly decided that these Amendments should receive a liberal construction, so as to prevent stealthy encroachment upon or “gradual depreciation” of the rights secured by them, by imperceptible practice of courts or by well-intentioned but mistakenly over-zealous executive officers.
 </p>
<p id="b342-5">
  In the spirit of these decisions we must deal with the questions before us.
 </p>
<p id="b342-6">
  The facts derived from the certificate, • essential to be considered, in answering the first two questions, are: that in January, 1918, it was suspected that the defendant, Gouled, and Vaughan were conspiring to defraud the Government through contracts with it for clothing and equipment; that one Cohen, a private in the Army, attached to the Intelligence Department, and a business acquaintance of defendant Gouled, under direction of his superior officers, pretending to make a friendly call upon the defendant, gained admission to his office and, in his absence, without warrant of any character, seized and carried away sevéral documents; that one of these papers, described as “of evidential value only” and belonging to Gouled, was subsequently delivered to the United States District Attorney, and was by him introduced in evidence over the objection of the defendant that possession of it was obtained by a violation of the Fourth or Fifth Amendment to the Constitution; and that the defendant did not know that Cohen had earned away any of his papers until
  <span citation-index="1" class="star-pagination" label="305"> 
   *305
   </span>
  he appeared on the witness stand and detailed the facts with respect thereto as we have stated them, when, necessarily, objection was first made to the admission of the paper in evidence.
 </p>
<p id="b343-5">
  • Out of these facts arise the first two questions, both relating to the paper thus seized. The first of these, is:
 </p>
<blockquote id="b343-6">
  “Is the secret taking or abstraction, without force, by a. representative of any branch or subdivision of the Government of the United States, of a paper writing of evidential value only belonging to one suspected of crime and from the house or office of such person, — a violation of the 4th amendment?”
 </blockquote>
<p id="b343-7">
  The.ground on which the trial court overruled the objection to this paper is not stated, but from the certificate and the argument we must infer that it was admitted either because it appeared that the possession of it was obtained without the use of force or illegal coercion, or because the objection to it came too late.
 </p>
<p id="b343-8">
  The objection was not too late, for, coming as it did promptly upon the first notice the defendant had that the Government was in possession of the paper, the rule of practice relied upon, that such an objection will not be entertained unless made before trial, was obviously inapplicable.
 </p>
<p id="b343-9">
  The prohibition of the Fourth Amendment is against all unreasonable seárches and seizures and if for a Government officer to obtain entrance to a man’s house or office by force or by an illegal threat or show of force, amounting to coercion, and then to search for and seize his private papers would be an unreasonable and. therefore a prohibited search and seizure, as it certainly would be, it is impossible to successfully contend that a like search and seizure would be a reasonable one if only admission were obtained by stealth instead of by force or coercion. The security and privacy of the home or office ancLof the papers of the owner would be as much invaded and the search and
  <span citation-index="1" class="star-pagination" label="306"> 
   *306
   </span>
  seizure would be as much against his will in the one case as in the other, and it must therefore be regarded as equally in violation of his constitutional rights.
 </p>
<p id="b344-4">
  Without discussing them, we cannot doubt that such decisions as there are in conflict with this conclusion are unsound, and that, whether entrance to the home or office of a person suspected of crime be obtained by a representative of any branch or subdivision of the Government of the United States by stealth, or through social acquaintance, or in the guise of a business call, and whether the owner be present or not when he enters, any search and seizure subsequently and secretly made in his absence, falls within the scope of the prohibition of the Fourth Amendment.,, and therefore the answer to the first question must be in the affirmative.
 </p>
<p id="b344-5">
  The second question reads:
 </p>
<blockquote id="b344-6">
  “Is the admission of such paper in evidence against the same person when indicted for crime a violation of the bth amendment? ”
 </blockquote>
<p id="b344-7">
  Upon authority of the
  <em>
   Boyd Case, supra,
  </em>
  this second question must also be answered in the affirmative. In practice the result is the same to one accused of crime, whether he be obliged to supply evidence against himself or whether such evidence be obtained by an illegal search of his premises and seizure of his private papers. In either case he is the unwilling source of the evidence, and the Fifth Amendment forbids that he shall be compelled to be a witness against himself in a criminal case.
 </p>
<p id="b344-8">
  The remaining four questions relate' to three other papers which were admitted in evidence on the trial over the same constitutional objections as were interposed to the admission of the first paper. One was an unexecuted form of contract between the defendant and one Lavinsky, another was a written contract, signed by the defendant and one Steinthal, and the third was a bill for
  <span citation-index="1" class="star-pagination" label="307"> 
   *307
   </span>
  disbursements and professional services rendered by the attorney at law to the defendant Gouled.
 </p>
<p id="b345-5">
  Of these' papers, the first was seized in defendant’s office under a search warrant, dated June 17, and the other two under a like warrant dated July 22, 1918,-each of which was issued by a United States Commissioner on the affidavit of an agent of the Department of Justice. It is certified that it was averred in the first affidavit that there were in Gouled’s office “certain property, to wit: certain contracts of the said Felix Gouled with S. Lavihsky [which] were used as a means of committing a felony, to wit: ... as means for the bribery of a certain office? of the United States.” It is also certified that the second, affidavit declared that Gouled had at his office “certain letters, papers, documents and writings which ... relate to, concern and have been used in the commission of a felony, to wit: -a conspiracy to defraud the United States.” Neither the affidavits nor the warrants are given in full in the certificate, but no exception was taken to the sufficiency of either.
 </p>
<p id="b345-6">
  - After the seizure of the papers, a joint indictment was returned; as stated, against Gouled, Vaughan and the attorney, and before trial a motion,was made by Gouled, for a return of the papers seized under the search warrants, which was denied, and when the motion was renewed at the trial, but before any evidence was introduced, it was again , denied. The denial of this motion is not assigned as error.
 </p>
<p id="b345-7">
  The contract of the defendant with Steinthal, which-was seized under the warrant, was not offered in evidence ~but a duplicate original, .obtained from Steinthal, was admitted over the objection that the possession of the seized original must have suggested the existence and the obtaining of the counterpart, and that therefore the use of it in evidence would violate the rights of the defendant under the Fourth or Fifth Amendment.
  <em>
   Silverthorne
  </em>
<span citation-index="1" class="star-pagination" label="308"> 
   *308
   </span>
<em>
   Lumber Co.
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>. The unsigned form of contract and the attorney’s bill were offered and also admitted over the same constitutional objection. There is no statement in the certificate of the contents of these papers, but it is said of them only, that they belonged to Gouled, that they were without pecuniary value and that they- constituted evidence “more or less .injurious to” the defendant.
 </p>
<p id="b346-4">
  It is apparent from this statement that to answer the remaining four 'questions involves a consideration of the applicable law of search warrants.
 </p>
<p id="b346-5">
  The wording of the Fourth Amendment implies that search warrants were in familiar use when the Constitution was adopted and, plainly, that when issued “upon probable cause, supported by óáth or affirmation,' and particularly describing'the place to be searched, and the "persons or things to be seized,” searches, and seizures made under them, are to be regarded as not-unreasonable, and therefore not prohibited by the Amendment. Searches and seizures are as constitutional under the Amendment when made under valid search warrants as they áre unconstitutional,' because unreasonable,--when máde without them, — the .permission of the. Amendment has the same constitutional 'warrant as the prohibition has, ánd the definition of the former restrains the scope of the latter. All of this is abundantly recognized in the opinions of the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  and
  <em>
   Weeks Cases, supra,
  </em>
  in which it is pointed out that at the time the Constitution was adopted stolen of forfeited property, or property liable to duties and concealed to avoid payment of them, excisable articles and books required by law to be kept with respect to them,' counterfeit coin, burglars’ tools and weapons, impleráents 'of gambling “and many other things of like character,” might be seárched for in home of office and if found might be seized, under search warrants, lawfully applied for, issued and executed.
 </p>
<p id="A8p">
<span citation-index="1" class="star-pagination" label="309"> 
   *309
   </span>
  Although search warrants have thus been used in many cases ever since the adoption of the Constitution, and although their use has been extended from time to .time to meet new cases within the old rules, nevertheless it is clear that, at common law and as the result of the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  and Weeks
  <em>
   Cases, supra,
  </em>
  they may not be used as a means of gaming access to a man’s' house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding, but that they may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it, or when a Valid exercise of the police power renders possession of the property by- the accused unlawful and provides that it may be taken.
  <em>
   Boyd Case,
  </em>
  pp. 623, 624.
 </p>
<p id="AxH">
  There is no special sanctity in papers, as distinguished from other forms of property, to render them immune from search and seizure, if only they fall within the scope of the principles of the cases in which other property may be seized, and if they be adequately described in the affidavit and warrant. Stolen or forged papers have been so seized,
  <em>
   Langdon
  </em>
  v.
  <em>
   People,
  </em>
  133 Illinois, 382, and lottery tickets, under a statute prohibiting their possession with intent to sell them,
  <em>
   Commonwealth
  </em>
  v.
  <em>
   Dana,
  </em>
  2 Mete. 329, and we cannot doubt that contracts may be so used as instruments or agencies for perpetrating frauds upon the Government as to give the public an interest in them which would justify the search for and seizure of them, under a properly issued search warrant, for the purpose of preventing further frauds.
 </p>
<p id="b347-6">
  With these principles of law in mind, we come to the remaining questions.
 </p>
<p id="A0uq1">
  The third question.reads: “Are papers of no pecuniary value ,but possessing evidential value against persons presently suspected and subsequently indicted under
  <span citation-index="1" class="star-pagination" label="310"> 
   *310
   </span>
  Sections 37 and 215 of the United States Criminal Code, when' taken under search warrants issued pursuant to the Act of June 15, 1917, from the house or office of the person so suspected, — seized and taken in violation of the 4th Amendment? ”
 </p>
<p id="AXY">
  That the papers involved are of no pecuniary value is of no significance. Many papers, having no pecuniary value to others, are of the greatest possible value to the owners and are property of a most important character
  <em>
   (Boyd Case, supra,
  </em>
  pp. 627, 628), and since those here involved possessed “evidential value ” against the defendant, we must assume that they were relevant to the issue..
 </p>
<p id="b348-6">
  Restraining the questions to the papers described, and first as to the unexecuted form of contract with Lavinsky, a stranger to the indictment. While the contents of this paper are not given, it is impossible to see how the Government could have such an interest in such a paper that under the principles of law stated it would have the right to take it into its possession to prevent injury to the public from its use. The Government could desire its possession only to use it as evidence against the defendant and to search for and seize it for such purpose was unlawful.
 </p>
<p id="b348-7">
  Likewise the public could be interested in the bill of the attorney for legal services only to the extent that it might be used as evidence and the seizure of this also was unlawful. '
 </p>
<p id="b348-8">
  As to the contract with Steinthal, also a stranger to the indictment. It is not difficult, as we have said, to imagine, how an executed written contract might be an important agency or instrumentality in the bribing of a public servant and in perpetrating frauds upon the Government so that it would have a legitimate and important interest in seizing such a paper in order to prevent further frauds, but the facts necessary to give this contract such a character do not appear in the certificate. On the con
  <span citation-index="1" class="star-pagination" label="311"> 
   *311
   </span>
  trary, -this third question recites that the papers are all of no pecuniary, but are of evidential, value, and in the sixth question it is recited that they are “of evidential value only,” so that it is impossible to say; on the record before us, that the Government had any interest in it other than as evidence against the accused, and therefore as to all three papers the answer to the question must be in the affirmative.
 </p>
<p id="b349-5">
  The fourth question reads: “If such papers so taken are admitted in evidence against the person from whose house or office they were taken, such person being then on trial for the crime of which he was accused in the affidavit for warrant, — is such admission in evidence a violation of the 5th amendment? ”
 </p>
<p id="b349-6">
  The same papers being involved, the answer to this question must be in the affirmative for, they having been seized in an unconstitutional search, to permit them to be used in evidence would be, in effect, as ruled in the
  <em>
   <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>
  </em>
  Case, to compel the. defendant to become a witness against himself.
 </p>
<p id="b349-7">
  The fifth question reads: “If in the affidavit for search warrant under Act of June 15, 1917, the party whose premises are to be searched be charged with one crime and property be taken under the warrant issued thereon, —can such property so seized be introduced in evidence against said party when on trial for a different offence? ”
 </p>
<p id="b349-8">
  It has never been required that a criminal prosecution should be pending against a person in order to justify search for and seizure of his property under a proper warrant, if a case of crime having been committed and of probable cause is made out sufficient to satisfy the law and the officer having authority to issue it, and we see no reason why property seized under a valid search warrant, when thus lawfully obtained by the Government, may not be used in the prosecution of a suspected person for a crime other than that which may have been described
  <span citation-index="1" class="star-pagination" label="312"> 
   *312
   </span>
  in the affidavit as having been committed by him. The question assumes that the property seized was obtained on a search warrant, sufficient in form to satisfy the law, and if the papers to which the question refers had been of a character to be thus obtained, lawfully, it would have been competent to use then! to prove any crime against the accused as to which they constituted relevant evidence.
 </p>
<p id="b350-5">
  The sixth question reads: “If papers of evidential value only be seized under a search warrant and t^e party from whose house or office they are taken be indicted;— if he then move before trial for the return of said papers and said motion is denied — is the court at trial bound in law to inquire as to. the origin of or method of procuring said papers when they are offered in. evidence against the party so indicted? ”
 </p>
<p id="b350-6">
  The papers being of “evidential value only” and having been unlawfully seized, this question really is, whether, it having been decided on a motion before trial that they should not be returned to the defendant, the trial court, when objection was made to their use on the trial, was' bound to again inquire as to the unconstitutional origin of thé possession of them. It is'plain that the trial court acted upon the rule, widely adopted, that courts in criminal trials will not pause to. determine how the possession of evidence tendered has been obtained. While tliis is a rule; of great practical importance, yet, after all, it is only a rule of procedure, and therefore it is not to be applied as a hard and fast formula to every case, regardless of its.special circumstances. We think rather that it is a rule to be used to secure the ends of justice under the circumstances presented by each case, and -where, in the progress of a trial, it becomes propable that there has been an unconstitutional seizure of papers, it is the. duty of the trial court to entertain an objection to their admission or a motion for their exclusion and to consider
  <span citation-index="1" class="star-pagination" label="313"> 
   *313
   </span>
  and decide the question as then presented; even where a motion to return the papers may have been denied before trial. A rule, of practice must not be allowed for any technical reason to prevail over a constitutional right.
 </p>
<p id="b351-5">
  In the case we are considering the certificate shows that a motion to return the papers, seized under the search warrants, was made before the trial, and was denied, and that, on the trial of the case before another judge, this ruling was treated as conclusive, although, as we have seen, in the progress of the trial it must have become. apparent that the papers had been unconstitutionally seized. The constitutional objection having been renewed,.,. under the circumstances, the court should have inquired as to the origin of the possession of the papers when they were offered in evidence against the defendant.
 </p>
<p id="b351-6">
<em>
   Each question is answered, Yes.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Grady v. North Carolina.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Grady v. North Carolina
type: case
citation: "575 U.S. 306 (2015)"
parallel_cite: "135 S. Ct. 1368; 191 L. Ed. 2d 459; 83 U.S.L.W. 4226; 25 Fla. L. Weekly Fed. S 181"
neutral_cite: 2015 U.S. LEXIS 2124
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-03-30
docket: No. 14-593
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
  opinion_url: "https://www.courtlistener.com/opinion/2789928/grady-v-north-carolina/"
  cluster_id: 2789928
  opinion_id: null
  identity_checked: true
lake:
  record_id: Grady v. North Carolina
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Trespass]]"
    role: Anchor
related:
  - "[[Trespass]]"
  - "[[United States v. Jones]]"
  - "[[Florida v. Jardines]]"
tags:
  - case
  - fourth-amendment
  - search
  - trespass
  - physical-intrusion
  - gps-monitoring
  - sex-offender
holding: "A State conducts a Fourth Amendment search when it attaches a satellite-based monitoring device to a person's body, without consent, to track his movements; the civil character of the monitoring program does not remove the conduct from the Fourth Amendment, leaving only the reasonableness of the search for decision on remand."
aliases:
  - Grady v. North Carolina
  - "Grady v. North Carolina (2015)"
---

# Grady v. North Carolina

*575 U.S. 306 (2015)* (No. 14-593) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 2789928 → opinion 2789928 (per curiam; 575 U.S. 306, decided Mar. 30, 2015). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 135 S. Ct. 1368), so the pin is to 135 S. Ct. at 1370 (the holding precedes the page-label `*1371`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Torrey Grady, a recidivist sex offender in North Carolina, was ordered under a state program to enroll in satellite-based monitoring: he would wear an ankle device that tracks his location continuously, in Grady's case for the rest of his life. Grady objected that subjecting him to this monitoring was an unreasonable search under the Fourth Amendment. The North Carolina courts rejected the argument, reasoning that the monitoring program was civil and that attaching and operating the device was not a Fourth Amendment search at all.

## Issue
Whether a State conducts a Fourth Amendment search when it attaches a tracking device to a person's body, without consent, in order to monitor his movements.

## Rule
Building directly on the Court's physical-intrusion cases, the [[Common Legal Terms#per-curiam|per curiam]] opinion held: "it follows that a State also conducts a search when it attaches a device to a person's body, without consent, for the purpose of tracking that individual's movements." — 135 S. Ct. at 1370. ^pin-1370

## Application
*[[United States v. Jones]]* and *[[Florida v. Jardines]]* establish that the government conducts a Fourth Amendment search when it physically intrudes on a constitutionally protected area to obtain information. Attaching a monitor to a person's body to track his movements is exactly such a physical intrusion — indeed a more direct one than the vehicle-mounted GPS in *[[United States v. Jones|Jones]]*. The civil label on North Carolina's program did not change the analysis, because Fourth Amendment coverage does not turn on whether the government's aim is civil or criminal. The Court held a search occurs and [[Reading and Citing Cases#on-remand|remanded]], expressly leaving open whether *this* search — lifetime satellite monitoring of a recidivist offender — is *reasonable*.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]] (per curiam) for a determination of the search's reasonableness.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Grady* applies the *[[United States v. Jones|Jones]]*/*[[Florida v. Jardines|Jardines]]* physical-intrusion (trespass) test to the human body: strapping a GPS monitor on a person is a search. It resolves only the threshold question; whether continuous or lifetime monitoring is a *reasonable* search — under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] and any special-needs justification — was left for the courts below. Teach it as the trespass theory reaching wearable tracking devices.

## Appears on
- [[Trespass]] — *Anchor*

## Sources
- [*Grady v. North Carolina*, 575 U.S. 306 (2015)](https://www.courtlistener.com/opinion/2789928/grady-v-north-carolina/) — pinpoint: 135 S. Ct. 1368, 1370 (per curiam; the CL opinion text is paginated to the parallel S. Ct. reporter, with the holding sentence appearing immediately before the page-label `*1371` — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1f5a0da0ebf52a69", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Grady v. North Carolina"}, "payload": {"all": [{"cite": "575 U.S. 306", "page": "306", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "575"}, {"cite": "135 S. Ct. 1368", "page": "1368", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "191 L. Ed. 2d 459", "page": "459", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "191"}, {"cite": "2015 U.S. LEXIS 2124", "page": "2124", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2015"}, {"cite": "83 U.S.L.W. 4226", "page": "4226", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "83"}, {"cite": "25 Fla. L. Weekly Fed. S 181", "page": "181", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "25"}], "display": "575 U.S. 306", "official": {"cite": "575 U.S. 306", "page": "306", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "575"}, "official_selection_present": true, "record_id": "Grady v. North Carolina"}}
{"assertion_id": "79cd5a71f2509a6c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Grady v. North Carolina"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Grady v. North Carolina", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Grady v. North Carolina

```json
{
  "schema_version": "s2.v1",
  "record_id": "Grady v. North Carolina",
  "status": "under_review",
  "identity": {
    "case_name": "Grady v. North Carolina",
    "case_name_short": "Grady",
    "case_name_full": "Torrey Dale GRADY v. NORTH CAROLINA.",
    "input_case_name": "Grady v. North Carolina",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-03-30",
    "year": 2015,
    "docket": "No. 14-593",
    "cluster_id": 2789928,
    "lead_opinion_id": 2789928,
    "sibling_ids": [],
    "absolute_url": "/opinion/2789928/grady-v-north-carolina/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "575 U.S. 306",
      "volume": "575",
      "reporter": "U.S.",
      "page": "306",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "135 S. Ct. 1368",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 459",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "459",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4226",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4226",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 181",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 2124",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "2124",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "575 U.S. 306",
        "volume": "575",
        "reporter": "U.S.",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1368",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1368",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 459",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "459",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 2124",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "2124",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4226",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4226",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 181",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "181",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "575 U.S. 306",
    "official_selection": {
      "court_class": "scotus",
      "selected": "575 U.S. 306",
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
    "date_created": "2026-07-06T13:11:25Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:11:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:11:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "grady-v-north-carolina--2789928",
      "to_record_id": "Grady v. North Carolina",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Grady v. North Carolina

```
                 Cite as: 575 U. S. ____ (2015)            1

                            Per Curiam

SUPREME COURT OF THE UNITED STATES
     TORREY DALE GRADY v. NORTH CAROLINA
       ON PETITION FOR WRIT OF CERTIORARI TO THE

           SUPREME COURT OF NORTH CAROLINA

              No. 14–593.   Decided March 30, 2015


  PER CURIAM.
  Petitioner Torrey Dale Grady was convicted in North
Carolina trial courts of a second degree sexual offense in
1997 and of taking indecent liberties with a child in 2006.
After serving his sentence for the latter crime, Grady was
ordered to appear in New Hanover County Superior Court
for a hearing to determine whether he should be subjected
to satellite-based monitoring (SBM) as a recidivist sex
offender. See N. C. Gen. Stat. Ann. §§14–208.40(a)(1), 14–
208.40B (2013). Grady did not dispute that his prior
convictions rendered him a recidivist under the relevant
North Carolina statutes. He argued, however, that the
monitoring program—under which he would be forced to
wear tracking devices at all times—would violate his
Fourth Amendment right to be free from unreasonable
searches and seizures. Unpersuaded, the trial court or-
dered Grady to enroll in the program and be monitored for
the rest of his life. Record in No. COA13-958 (N. C. App.),
pp. 3–4, 18–22.
  Grady renewed his Fourth Amendment challenge on
appeal, relying on this Court’s decision in United States v.
Jones, 565 U. S. ___ (2012). In that case, this Court held
that police officers had engaged in a “search” within the
meaning of the Fourth Amendment when they installed
and monitored a Global Positioning System (GPS) track-
ing device on a suspect’s car. The North Carolina Court of
Appeals rejected Grady’s argument, concluding that it was
foreclosed by one of its earlier decisions. App. to Pet. for
Cert. 5a–7a. In that decision, coincidentally named State
2                    GRADY v. NORTH CAROLINA

                               Per Curiam

v. Jones, the court had said:
     “Defendant essentially argues that if affixing a GPS to
     an individual’s vehicle constitutes a search of the in-
     dividual, then the arguably more intrusive act of affix-
     ing an ankle bracelet to an individual must constitute
     a search of the individual as well. We disagree. The
     context presented in the instant case—which involves
     a civil SBM proceeding—is readily distinguishable
     from that presented in [United States v.] Jones, where
     the Court considered the propriety of a search in the
     context of a motion to suppress evidence. We con-
     clude, therefore, that the specific holding in [United
     States v.] Jones does not control in the case sub ju-
     dice.” ___ N. C. App. ___, ___, 750 S. E. 2d 883, 886
     (2013).
   The court in Grady’s case held itself bound by this rea-
soning and accordingly rejected his Fourth Amendment
challenge. App. to Pet. for Cert. 6a–7a. The North Caro-
lina Supreme Court in turn summarily dismissed Grady’s
appeal and denied his petition for discretionary review.
367 N. C. 523, 762 S. E. 2d 460 (2014). Grady now asks us
to reverse these decisions.*
   The only explanation provided below for the rejection of
Grady’s challenge is the quoted passage from State v.
Jones. And the only theory we discern in that passage is
that the State’s system of nonconsensual satellite-based
monitoring does not entail a search within the meaning of
the Fourth Amendment. That theory is inconsistent with
——————
   * Grady aims his petition at the decisions of both North Carolina
appellate courts. See Pet. for Cert. 1. Because we treat the North
Carolina Supreme Court’s dismissal of an appeal for lack of a substan-
tial constitutional question as a decision on the merits, it is that court’s
judgment, rather than the judgment of the Court of Appeals, that is
subject to our review under 28 U. S. C. §1257(a). See R. J. Reynolds
Tobacco Co. v. Durham County, 479 U. S. 130, 138–139 (1986).
                 Cite as: 575 U. S. ____ (2015)            3

                          Per Curiam

this Court’s precedents.
   In United States v. Jones, we held that “the Govern-
ment’s installation of a GPS device on a target’s vehicle,
and its use of that device to monitor the vehicle’s move-
ments, constitutes a ‘search.’ ” 565 U. S., at ___ (slip op.,
at 3) (footnote omitted). We stressed the importance of the
fact that the Government had “physically occupied private
property for the purpose of obtaining information.” Id., at
___ (slip op., at 4). Under such circumstances, it was not
necessary to inquire about the target’s expectation of
privacy in his vehicle’s movements in order to determine if
a Fourth Amendment search had occurred. “Where, as
here, the Government obtains information by physically
intruding on a constitutionally protected area, such a
search has undoubtedly occurred.” Id., at ___, n. 3 (slip
op., at 6, n. 3).
   We reaffirmed this principle in Florida v. Jardines, 569
U. S. ___, ___–___ (2013) (slip op., at 3–4), where we held
that having a drug-sniffing dog nose around a suspect’s
front porch was a search, because police had “gathered . . .
information by physically entering and occupying the
[curtilage of the house] to engage in conduct not explicitly
or implicitly permitted by the homeowner.” See also id., at
___ (slip op., at 9) (a search occurs “when the government
gains evidence by physically intruding on constitutionally
protected areas”). In light of these decisions, it follows
that a State also conducts a search when it attaches a
device to a person’s body, without consent, for the purpose
of tracking that individual’s movements.
   In concluding otherwise, the North Carolina Court of
Appeals apparently placed decisive weight on the fact that
the State’s monitoring program is civil in nature. See
Jones, ___ N. C. App., at ___, 750 S. E. 2d, at 886 (“the
instant case . . . involves a civil SBM proceeding”). “It is
well settled,” however, “that the Fourth Amendment’s
protection extends beyond the sphere of criminal investi-
4                GRADY v. NORTH CAROLINA

                         Per Curiam

gations,” Ontario v. Quon, 560 U. S. 746, 755 (2010), and
the government’s purpose in collecting information does
not control whether the method of collection constitutes a
search. A building inspector who enters a home simply to
ensure compliance with civil safety regulations has un-
doubtedly conducted a search under the Fourth Amend-
ment. See Camara v. Municipal Court of City and County
of San Francisco, 387 U. S. 523, 534 (1967) (housing in-
spections are “administrative searches” that must comply
with the Fourth Amendment).
   In its brief in opposition to certiorari, the State faults
Grady for failing to introduce “evidence about the State’s
implementation of the SBM program or what information,
if any, it currently obtains through the monitoring pro-
cess.” Brief in Opposition 11. Without evidence that it is
acting to obtain information, the State argues, “there is no
basis upon which this Court can determine whether North
Carolina conducts a ‘search’ of an offender enrolled in its
SBM program.” Ibid. (citing Jones, 565 U. S., at ___, n. 5
(slip op., at 7, n. 5) (noting that a government intrusion is
not a search unless “done to obtain information”)). In
other words, the State argues that we cannot be sure its
program for satellite-based monitoring of sex offenders
collects any information. If the very name of the program
does not suffice to rebut this contention, the text of the
statute surely does:
    “The satellite-based monitoring program shall use a
    system that provides all of the following:
      “(1) Time-correlated and continuous tracking of the
    geographic location of the subject . . . .
      “(2) Reporting of subject’s violations of prescriptive
    and proscriptive schedule or location requirements.”
    N. C. Gen. Stat. Ann. §14–208.40(c).
The State’s program is plainly designed to obtain infor-
mation. And since it does so by physically intruding on a
                 Cite as: 575 U. S. ____ (2015)            5

                          Per Curiam

subject’s body, it effects a Fourth Amendment search.
   That conclusion, however, does not decide the ultimate
question of the program’s constitutionality. The Fourth
Amendment prohibits only unreasonable searches. The
reasonableness of a search depends on the totality of the
circumstances, including the nature and purpose of the
search and the extent to which the search intrudes upon
reasonable privacy expectations. See, e.g., Samson v.
California, 547 U. S. 843 (2006) (suspicionless search of
parolee was reasonable); Vernonia School Dist. 47J v.
Acton, 515 U. S. 646 (1995) (random drug testing of stu-
dent athletes was reasonable). The North Carolina courts
did not examine whether the State’s monitoring program
is reasonable—when properly viewed as a search—and we
will not do so in the first instance.
   The petition for certiorari is granted, the judgment of
the Supreme Court of North Carolina is vacated, and the
case is remanded for further proceedings not inconsistent
with this opinion.
                                            It is so ordered.

```

---
