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

## GROUP: _overhaul2/lake/cases/Gutierrez v. Saenz.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "5b3185b500bd8ad8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gutierrez v. Saenz"}, "payload": {"all": [{"cite": "606 U.S. 305", "page": "305", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "606"}], "display": "606 U.S. 305", "official": {"cite": "606 U.S. 305", "page": "305", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "606"}, "official_selection_present": true, "record_id": "Gutierrez v. Saenz"}}
{"assertion_id": "02da7e4a1ddb08f1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gutierrez v. Saenz"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Gutierrez v. Saenz", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Hafer v. Melo.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Hafer v. Melo
type: case
citation: "502 U.S. 21 (1991)"
parallel_cite: "112 S. Ct. 358; 116 L. Ed. 2d 301; 57 Empl. Prac. Dec. (CCH) 41,059"
neutral_cite: 1991 U.S. LEXIS 6502
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-11-05
docket: No. 90-681
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
  opinion_url: "https://www.courtlistener.com/opinion/112657/hafer-v-melo/"
  cluster_id: 112657
  opinion_id: null
  identity_checked: true
lake:
  record_id: Hafer v. Melo
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - personal-capacity
  - eleventh-amendment
  - state-officials
  - qualified-immunity
holding: "State officials sued in their individual (personal) capacities for actions taken in their official capacity are 'persons' within the meaning of § 1983; the Eleventh Amendment does not bar such personal-capacity suits, and the official character of the challenged acts does not by itself confer absolute immunity."
aliases:
  - Hafer v. Melo
  - "Hafer v. Melo (1991)"
---

# Hafer v. Melo

*502 U.S. 21 (1991)* (No. 90-681) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112657 → combined opinion 112657 (O'Connor, J.; 502 U.S. 21, decided Nov. 5, 1991). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*31`). S9 promotes. -->

## Background
Barbara Hafer, shortly after becoming Pennsylvania's Auditor General, discharged a number of employees in her office. The discharged employees sued her under 42 U.S.C. § 1983 for damages, alleging the firings were unlawful. Hafer sought dismissal, arguing that because she was acting in her official capacity, she was not a "person" subject to § 1983 and was shielded by the Eleventh Amendment. The Third Circuit allowed the personal-capacity claims to proceed, and the Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]] to resolve how *[[Will v. Michigan Department of State Police]]* applies to a personal-capacity suit.

## Issue
Whether a state official sued in her personal capacity for acts taken in her official capacity is a "person" amenable to suit under § 1983, or is instead protected by the Eleventh Amendment and the rule of *[[Will v. Michigan Department of State Police|Will]]*.

## Rule
The Court distinguished official-capacity suits (which are really suits against the State) from personal-capacity suits (which seek to impose individual liability on the officer) and held: "We hold that state officials, sued in their individual capacities, are 'persons' within the meaning of § 1983. The Eleventh Amendment does not bar such suits, nor are state officers absolutely immune from personal liability under § 1983 solely by virtue of the 'official' nature of their acts." — 502 U.S. at 31. ^pin-31

## Application
*[[Will v. Michigan Department of State Police|Will]]* held that a State — and a state official sued in his official capacity for damages — is not a "person" under § 1983, because the suit is in substance against the sovereign. A personal-capacity action is different in kind: it seeks money from the official individually for conduct taken [[Section 1983 Liability and Qualified Immunity|under color of law]], so the Eleventh Amendment's bar on suits against the State does not apply. That officials may find personal liability burdensome is a concern for the separate doctrine of **[[Qualified Immunity|qualified immunity]]**, not a reason to read them out of § 1983 altogether.

## Conclusion
The judgment was **affirmed**. O'Connor, J., delivered the opinion of the Court; Thomas, J., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Hafer* draws the pivotal **capacity** line that governs § 1983 suits against state officials: **personal-capacity** damages claims are allowed (subject to [[Qualified Immunity|qualified immunity]]), while **official-capacity** damages claims are barred by *[[Will v. Michigan Department of State Police|Will]]* and the Eleventh Amendment as suits against the State. Teach it as the practical key to pleading a § 1983 damages case against a state officer.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Hafer v. Melo*, 502 U.S. 21 (1991)](https://www.courtlistener.com/opinion/112657/hafer-v-melo/) — pinpoint: 31 (O'Connor, J., for the Court; the CL opinion text carries the reporter star `*31` immediately before the holding paragraph). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "616b14e029366811", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hafer v. Melo"}, "payload": {"all": [{"cite": "502 U.S. 21", "page": "21", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "502"}, {"cite": "112 S. Ct. 358", "page": "358", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "112"}, {"cite": "116 L. Ed. 2d 301", "page": "301", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "1991 U.S. LEXIS 6502", "page": "6502", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}, {"cite": "57 Empl. Prac. Dec. (CCH) 41,059", "page": "41,059", "reporter": "Empl. Prac. Dec. (CCH)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}], "display": "502 U.S. 21", "official": {"cite": "502 U.S. 21", "page": "21", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "502"}, "official_selection_present": true, "record_id": "Hafer v. Melo"}}
{"assertion_id": "9ba08273ba7d3fdc", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hafer v. Melo"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Hafer v. Melo", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Hafer v. Melo

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hafer v. Melo",
  "status": "under_review",
  "identity": {
    "case_name": "Hafer v. Melo",
    "case_name_short": "Hafer",
    "case_name_full": "HAFER v. MELO Et Al.",
    "input_case_name": "Hafer v. Melo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-11-05",
    "year": 1991,
    "docket": "No. 90-681",
    "cluster_id": 112657,
    "lead_opinion_id": 112657,
    "sibling_ids": [],
    "absolute_url": "/opinion/112657/hafer-v-melo/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "502 U.S. 21",
      "volume": "502",
      "reporter": "U.S.",
      "page": "21",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "112 S. Ct. 358",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "358",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 L. Ed. 2d 301",
        "volume": "116",
        "reporter": "L. Ed. 2d",
        "page": "301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 Empl. Prac. Dec. (CCH) 41,059",
        "volume": "57",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "41,059",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 6502",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "6502",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "502 U.S. 21",
        "volume": "502",
        "reporter": "U.S.",
        "page": "21",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 S. Ct. 358",
        "volume": "112",
        "reporter": "S. Ct.",
        "page": "358",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 L. Ed. 2d 301",
        "volume": "116",
        "reporter": "L. Ed. 2d",
        "page": "301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 6502",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "6502",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 Empl. Prac. Dec. (CCH) 41,059",
        "volume": "57",
        "reporter": "Empl. Prac. Dec. (CCH)",
        "page": "41,059",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "502 U.S. 21",
    "official_selection": {
      "court_class": "scotus",
      "selected": "502 U.S. 21",
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
    "date_created": "2026-07-06T13:18:47Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:18:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:18:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:18:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "hafer-v-melo--112657",
      "to_record_id": "Hafer v. Melo",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Hafer v. Melo

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b182-10">
  Justice O’Connor
 </author>
<p id="Aqm">
  delivered the opinion of the Court.
 </p>
<p id="b182-11">
  In
  <em>
   Will
  </em>
  v.
  <em>
   Michigan Dept. of State Police,
  </em>
  <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">491 U. S. 58</a></span> (1989), we held that state officials “acting in their official capacities” are outside the class of “persons” subject to liability
  <span citation-index="1" class="star-pagination" label="23"> 
   *23
   </span>
  under Rev. Stat. § 1979, <span class="citation no-link">42 U. S. C. § 1983</span>. <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/#71" aria-description="Citation for case: Will v. Michigan Department of State Police">491 U. S., at 71</a></span>. Petitioner takes this language to mean that § 1983 does not authorize suits against state officers for damages arising from official acts. We reject this reading of
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  and hold that state officials sued in their individual capacities are “persons” for purposes of § 1983.
 </p>
<p id="b183-8">
  I
 </p>
<p id="b183-3">
  In 1988, petitioner Barbara Hafer sought election to the post of auditor general of Pennsylvania. Respondents allege that during the campaign United States Attorney James West gave Hafer a list of 21 employees in the auditor general’s office who secured their jobs through payments to a former employee of the office. App. 10. They further allege that Hafer publicly promised to fire all employees on the list if elected.
  <em>
   Ibid.
  </em>
</p>
<p id="b183-4">
  Hafer won the election. Shortly after becoming auditor general, she dismissed 18 employees, including named respondent James Melo, Jr., on the basis that they “bought” their jobs. Melo and seven other terminated employees sued Hafer and West in Federal District Court. They asserted state and federal claims, including a claim under § 1983, and sought monetary damages. Carl Gurley and the remaining respondents in this case also lost their jobs with the auditor general soon after Hafer took office. These respondents allege that Hafer discharged them because of their Democratic political affiliation and support for her opponent in the 1988 election.
  <em>
   Id.,
  </em>
  at 28, 35, 40. They too filed suit against Hafer, seeking monetary damages and reinstatement under § 1983.
 </p>
<p id="b183-5">
  After consolidating the Melo and Gurley actions, the District Court dismissed all claims. In relevant part, the court held that the § 1983 claims against Hafer were barred because, under
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>,
  </em>
  she could not be held liable for employment decisions made in her official capacity as auditor general.
 </p>
<p id="b184-4">
<span citation-index="1" class="star-pagination" label="24"> 
   *24
   </span>
  The Court of Appeals for the Third Circuit reversed this portion of the District Court’s decision. <span class="citation multiple-matches"><a href="/c/F.%202d/912/628/">912 F. 2d 628</a></span> (1990). As to claims for reinstatement brought against Hafer in her official capacity, the court rested on our statement in
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  that state officials sued for injunctive relief in their official capacities are “persons” subject to liability under § 1983. See
  <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/#71" aria-description="Citation for case: Will v. Michigan Department of State Police"><em>
   Will, supra,
  </em>
  at 71, n. 10</a></span>. Turning to respondents’ monetary claims, the court found that six members of the Gurley group had expressly sought damages from Hafer in her personal capacity. The remaining plaintiffs “although not as explicit, signified a similar intent.” 912 F. 2d, at 636.
  <a class="footnote" href="#fn*" id="fn*_ref">
   *
  </a>
  The court found this critical. While Hafer’s power to hire and fire derived from her position as auditor general, it said, a suit for damages based on the exercise of this authority could be brought against Hafer in her personal capacity. Because Hafer acted under color of state law, respondents could maintain a § 1983 individual-capacity suit against her.
 </p>
<p id="b184-5">
  We granted certiorari, 498 U. S..1H8 (1991), to address the question whether state officers may be held personally liable for damages under § 1983 based upon actions taken in their official capacities.
 </p>
<p id="AX">
<span citation-index="1" class="star-pagination" label="25"> 
   *25
   </span>
  II
 </p>
<p id="b185-4">
  In
  <em>
   Kentucky
  </em>
  v.
  <em>
   Graham,
  </em>
  <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/" aria-description="Citation for case: Kentucky v. Graham">473 U. S. 159</a></span> (1985), the Court sought to eliminate lingering confusion about the distinction between personal- and official-capacity suits. We emphasized that official-capacity suits “‘generally represent only another way of pleading an action against an entity of which an officer is an agent.’ ”
  <em>
   <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/" aria-description="Citation for case: Kentucky v. Graham">Id.,</a></span>
  </em>
  at 165 (quoting
  <em>
   Monell
  </em>
  v.
  <em>
   New York City Dept. of Social Services,
  </em>
  <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 690, n. 55</a></span> (1978)). Suits against state officials in their official capacity therefore should be treated as suits against the State. <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#166" aria-description="Citation for case: Kentucky v. Graham">473 U. S., at 166</a></span>. Indeed, when officials sued in this capacity in federal court die or leave office, their successors automatically assume their roles in the litigation. See Fed. Rule Civ. Proc. 25(d)(1); Fed. Rule App. Proc. 43(c)(1); this Court’s Rule 35.3. Because the real party in interest in an official-capacity suit is the governmental entity and not the named official, “the entity’s ‘policy or custom’ must have played a part in the violation of federal law.”
  <em>
   <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/" aria-description="Citation for case: Kentucky v. Graham">Graham, supra,</a></span>
  </em>
  at 166 (quoting
  <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs."><em>
   Monell, supra,
  </em>
  at 694</a></span>). For the same reason, the only immunities available to the defendant in an official-capacity action are those that the governmental entity possesses. <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#167" aria-description="Citation for case: Kentucky v. Graham">473 U. S., at 167</a></span>.
 </p>
<p id="b185-5">
  Personal-capacity suits, on the other hand, seek to impose individual liability upon a government officer for actions taken under color of state law. Thus, “[o]n the merits, to establish
  <em>
   personal
  </em>
  liability in a § 1983 action, it is enough to show that the official, acting under color of state law, caused the deprivation of a federal right.”
  <em>
   Id.,
  </em>
  at 166. While the plaintiff in a personal-capacity suit need not establish a connection to governmental “policy or custom,” officials sued in their personal capacities, unlike those sued in their official capacities, may assert personal immunity defenses such as objectively reasonable reliance on existing law.
  <em>
   Id.,
  </em>
  at 166-167.
 </p>
<p id="b185-6">
  Our decision in
  <em>
   Will
  </em>
  v.
  <em>
   Michigan Dept. of State Police,
  </em>
  <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">491 U. S. 58</a></span> (1989), turned in part on these differences between
  <span citation-index="1" class="star-pagination" label="26"> 
   *26
   </span>
  personal- and official-capacity actions. The principal issue in
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  was whether States are “persons” subject to suit under § 1983. Section 1983 provides, in relevant part:
 </p>
<blockquote id="b186-5">
  “Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured . . . .”
 </blockquote>
<p id="b186-6">
  The Court held that interpreting the words “[ejvery person” to exclude the States accorded with the most natural reading of the law, with its legislative history, and with the rule that Congress must clearly state its intention to alter “ ‘the federal balance’” when it seeks to do so.
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will, supra,</a></span>
  </em>
  at 65 (quoting
  <em>
   United States
  </em>
  v.
  <em>
   Bass,
  </em>
  <span class="citation" data-id="9424710"><a href="/opinion/108421/united-states-v-bass/#349" aria-description="Citation for case: United States v. Bass">404 U. S. 336, 349</a></span> (1971)).
 </p>
<p id="b186-7">
  The Court then addressed the related question whether state officials, sued for monetary relief in their official capacities, are persons under § 1983. We held that they are not. Although “state officials literally are persons,” an official-capacity suit against a state officer “is not a suit against the official but rather is a suit against the official’s office. As such it is no different from a suit against the State itself.” <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/#71" aria-description="Citation for case: Will v. Michigan Department of State Police">491 U. S., at 71</a></span> (citation omitted).
 </p>
<p id="b186-8">
  Summarizing our holding, we said: “[NJeither a State nor its officials acting in their official capacities are ‘persons’ under § 1983.”
  <em>
   Ibid.
  </em>
  Hafer relies on this recapitulation for the proposition that she may not be held personally liable under § 1983 for discharging respondents because she “act[ed]” in her official capacity as auditor general of Pennsylvania. Of course, the claims considered in
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  were official-capacity claims; the phrase “acting in their official capacities” is best understood as a reference to the capacity in which the state officer is sued, not the capacity in which the officer inflicts the alleged injury. To the extent that
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
<span citation-index="1" class="star-pagination" label="27"> 
   *27
   </span>
  allows the construction Hafer suggests, however, we now eliminate that ambiguity.
 </p>
<p id="b187-5">
  A
 </p>
<p id="b187-6">
<em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  itself makes clear that the distinction between official-capacity suits and personal-capacity suits is more than “a mere pleading device.”
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Ibid.</a></span>
  </em>
  State officers sued for damages in their official capacity are not “persons” for purposes of the suit because they assume the identity of the government that employs them.
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Ibid.</a></span>
  </em>
  By contrast, officers sued in their personal capacity come to court as individuals. A government official in the role of personal-capacity defendant thus fits comfortably within the statutory term “person.” Cf.
  <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/#71" aria-description="Citation for case: Will v. Michigan Department of State Police"><em>
   id.,
  </em>
  at 71, n. 10</a></span> (“[A] state official in his or her official capacity, when sued for injunctive relief, would be a person under § 1983 because ‘official-capacity actions for prospective relief are not treated as actions against the State’ ”) (quoting
  <em>
   Graham,
  </em>
  <span class="citation" data-id="111500"><a href="/opinion/111500/kentucky-v-graham/#167" aria-description="Citation for case: Kentucky v. Graham">473 U. S., at 167, n. 14</a></span>).
 </p>
<p id="b187-7">
  Hafer seeks to overcome the distinction between official- and personal-capacity suits by arguing that §1983 liability turns not on the capacity in which state officials are sued, but on the capacity in which they acted when injuring the plaintiff. Under
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>,
  </em>
  she asserts, state officials may not be held liable in their personal capacity for actions they take in their official capacity. Although one Court of Appeals has endorsed this view, see
  <em>
   Cowan
  </em>
  v.
  <em>
   University of Louisville School of Medicine,
  </em>
  <span class="citation" data-id="9480203"><a href="/opinion/539862/jonathan-cowan-phd-v-university-of-louisville-school-of-medicine-leah/#942" aria-description="Citation for case: Jonathan Cowan, ph.d. v. University of Louisville School...">900 F. 2d 936, 942-943</a></span> (CA6 1990), we find it both unpersuasive as an interpretation of § 1983 and foreclosed by our prior decisions.
 </p>
<p id="b187-8">
  Through § 1983, Congress sought “to give a remedy to parties deprived of constitutional rights, privileges and immunities by an official’s abuse of his position.”
  <em>
   Monroe
  </em>
  v.
  <em>
   Pape,
  </em>
  <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#172" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167, 172</a></span> (1961). Accordingly, it authorized suits to redress deprivations of civil rights by persons acting “under color of any [state] statute, ordinance, regulation, custom, or usage.” <span class="citation no-link">42 U. S. C. § 1983</span>. The requirement of action under color of state law means that Hafer may be liable for
  <span citation-index="1" class="star-pagination" label="28"> 
   *28
   </span>
  discharging respondents precisely because of her authority as auditor general. We cannot accept the novel proposition that this same official authority insulates Hafer from suit.
 </p>
<p id="b188-5">
  In an effort to limit the scope of her argument, Hafer distinguishes between two categories of acts taken under color of state law: those outside the official’s authority or not essential to the operation of state government, and those both within the official’s authority and necessary to the performance of governmental functions. Only the former group, she asserts, can subject state officials to personal liability under § 1983; the latter group (including the employment decisions at issue in this case) should be considered acts of the State that cannot give rise to a personal-capacity action.
 </p>
<p id="b188-6">
  The distinction Hafer urges finds no support in the broad language of § 1983. To the contrary, it ignores our holding that Congress enacted § 1983 “ ‘to enforce provisions of the Fourteenth Amendment against those who carry a badge of authority of a State and represent it in some capacity, whether they act in accordance with their authority or misuse it.’ ”
  <em>
   Scheuer
  </em>
  v.
  <em>
   Rhodes,
  </em>
  <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#243" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 243</a></span> (1974) (quoting
  <em>
   Monroe
  </em>
  v.
  <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#171" aria-description="Citation for case: Monroe v. Pape"><em>
   Pape, supra,
  </em>
  at 171-172</a></span>). Because of that intent, we have held that in § 1983 actions the statutory requirement of action “under color of” state law is just as broad as the Fourteenth Amendment’s “state action” requirement.
  <em>
   Lugar
  </em>
  v.
  <em>
   Edmondson Oil Co.,
  </em>
  <span class="citation" data-id="9428872"><a href="/opinion/110766/lugar-v-edmondson-oil-co/#929" aria-description="Citation for case: Lugar v. Edmondson Oil Co.">457 U. S. 922, 929</a></span> (1982).
 </p>
<p id="b188-7">
  Furthermore, Hafer’s distinction cannot be reconciled with our decisions regarding immunity of government officers otherwise personally liable for acts done in the course of their official duties. Her theory would absolutely immunize state officials from personal liability for acts within their authority and necessary to fulfilling governmental responsibilities. Yet our cases do not extend absolute immunity to all officers who engage in necessary official acts. Rather, immunity from suit under § 1983 is “predicated upon a considered inquiry into the immunity historically accorded the relevant
  <span citation-index="1" class="star-pagination" label="29"> 
   *29
   </span>
  official at common law and the interests behind it,”
  <em>
   Imbler
  </em>
  v.
  <em>
   Pachtman,
  </em>
  <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 421</a></span> (1976), and officials seeking absolute immunity must show that such immunity is justified for the governmental function at issue,
  <em>
   Burns
  </em>
  v. Reed, <span class="citation" data-id="9432302"><a href="/opinion/112606/burns-v-reed/#486" aria-description="Citation for case: Burns v. Reed">500 U. S. 478, 486-487</a></span> (1991).
 </p>
<p id="b189-5">
  This Court has refused to extend absolute immunity beyond a very limited class of officials, including the President of the United States, legislators carrying out their legislative functions, and judges carrying out their judicial functions, “whose special functions or constitutional status requires complete protection from suit.”
  <em>
   Harlow
  </em>
  v.
  <em>
   Fitzgerald,
  </em>
  <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#807" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 807</a></span> (1982). State executive officials are not entitled to absolute immunity for their official actions.
  <em>
   Scheuer
  </em>
  v.
  <em>
   <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Rhodes, supra.</a></span>
  </em>
  In several instances, moreover, we have concluded that no more than a qualified immunity attaches to administrative employment decisions, even if the same official has absolute immunity when performing other functions. See
  <em>
   Forrester
  </em>
  v.
  <em>
   White,
  </em>
  <span class="citation" data-id="111977"><a href="/opinion/111977/forrester-v-white/" aria-description="Citation for case: Forrester v. White">484 U. S. 219</a></span> (1988) (dismissal of court employee by state judge);
  <em>
   Harlow
  </em>
  v.
  <em>
   <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">Fitzgerald, supra</a></span>
  </em>
  (discharge of Air Force employee, allegedly orchestrated by senior White House aides) (action under
  <em>
   Bivens
  </em>
  v.
  <em>
   Six Unknown Fed. Narcotics Agents,
  </em>
  <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971));
  <em>
   Davis
  </em>
  v.
  <em>
   Passman,
  </em>
  <span class="citation" data-id="9427603"><a href="/opinion/110097/davis-v-passman/" aria-description="Citation for case: Davis v. Passman">442 U. S. 228</a></span> (1979) (dismissal of congressional aide)
  <em>
   (Bivens
  </em>
  action). That Hafer may assert personal immunity within the framework of these cases in no way supports her argument here.
 </p>
<p id="b189-6">
  B
 </p>
<p id="b189-7">
  Hafer further asks us to read
  <em>
   Will’s
  </em>
  language concerning suits against state officials as establishing the limits of liability under the Eleventh Amendment. She asserts that imposing personal liability on officeholders may infringe on state sovereignty by rendering government less effective; thus, she argues, the Eleventh Amendment forbids personal-capacity suits against state officials in federal court.
 </p>
<p id="b190-4">
<span citation-index="1" class="star-pagination" label="30"> 
   *30
   </span>
  Most certainly,
  <em>
   Will’s
  </em>
  holding does not rest directly on the Eleventh Amendment. Whereas the Eleventh Amendment bars suits in federal court “by private parties seeking to impose a liability which must be paid from public funds in the state treasury,”
  <em>
   Edelman
  </em>
  v.
  <em>
   Jordan,
  </em>
  <span class="citation" data-id="9425645"><a href="/opinion/108990/edelman-v-jordan/#663" aria-description="Citation for case: Edelman v. Jordan">415 U. S. 651, 663</a></span> (1974),
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  arose from a suit in
  <em>
   state
  </em>
  court. We considered the Eleventh Amendment in
  <em>
   <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/" aria-description="Citation for case: Will v. Michigan Department of State Police">Will</a></span>
  </em>
  only because the fact that Congress did not intend to override state immunity when it enacted § 1983 was relevant to statutory construction: “Given that a principal purpose behind the enactment of § 1983 was to provide a federal forum for civil rights claims,” Congress’ failure to authorize suits against States in federal courts suggested that it also did not intend to authorize such claims in state courts. <span class="citation" data-id="9431737"><a href="/opinion/112293/will-v-michigan-department-of-state-police/#66" aria-description="Citation for case: Will v. Michigan Department of State Police">491 U. S., at 66</a></span>.
 </p>
<p id="b190-5">
  To the extent that Hafer argues from the Eleventh Amendment itself, she makes a claim that failed in
  <em>
   Scheuer
  </em>
  v.
  <em>
   <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Rhodes, supra.</a></span>
  </em>
  In
  <em>
   <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span>,
  </em>
  personal representatives of the estates of three students who died at Kent State University in May 1970 sought damages from the Governor of Ohio and other state officials. The District Court dismissed their complaints on the theory that the suits, although brought against state officials in their personal capacities, were in substance actions against the State of Ohio and therefore barred by the Eleventh Amendment.
 </p>
<p id="b190-6">
  We rejected this view. “[S]ince
  <em>
   Ex parte Young,
  </em>
  <span class="citation" data-id="9418117"><a href="/opinion/96819/ex-parte-young/" aria-description="Citation for case: Ex Parte Young">209 U. S. 123</a></span> (1908),” we said, “it has been settled that the Eleventh Amendment provides no shield for a state official confronted by a claim that he had deprived another of a federal right under the color of state law.”
  <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#237" aria-description="Citation for case: Scheuer v. Rhodes"><em>
   Scheuer, supra,
  </em>
  at 237</a></span>. While the doctrine of
  <em>
   Ex parte Young
  </em>
  does not apply where a plaintiff seeks damages from the public treasury, damages awards against individual defendants in federal courts “are a permissible remedy in some circumstances notwithstanding the fact that they hold public office.” <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#238" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 238</a></span>. That is, the Eleventh Amendment does not erect a barrier
  <span citation-index="1" class="star-pagination" label="31"> 
   *31
   </span>
  against suits to impose “individual and personal liability” on state officials under § 1983.
  <em>
   Ibid.
  </em>
</p>
<p id="b191-5">
  To be sure, imposing personal liability on state officers may hamper their performance of public duties. But such concerns are properly addressed within the framework of our personal immunity jurisprudence. See
  <em>
   Forrester
  </em>
  v.
  <span class="citation" data-id="111977"><a href="/opinion/111977/forrester-v-white/#223" aria-description="Citation for case: Forrester v. White"><em>
   White, supra,
  </em>
  at 223</a></span>. Insofar as respondents seek damages against Hafer personally, the Eleventh Amendment does not restrict their ability to sue in federal court.
 </p>
<p id="b191-6">
  We hold that state officials, sued in their individual capacities, are “persons” within the meaning of § 1983. The Eleventh Amendment does not bar such suits, nor are state officers absolutely immune from personal liability under § 1983 solely by virtue of the “official” nature of their acts.
 </p>
<p id="b191-7">
  The judgment of the Court of Appeals is
 </p>
<p id="b191-8">
<em>
   Affirmed.
  </em>
</p>
<p id="b191-9">
  Justice Thomas took no part in the consideration or decision of this case.
 </p>

<div class="footnotes"><div class="footnote" id="fn*" label="*">
<a class="footnote" href="#fn*_ref">
   *
  </a>
<p id="b184-6">
   The Third Circuit looked to the proceedings below to determine whether certain respondents brought their claims for damages against Hafer in her official capacity or her personal capacity. 912 F. 2d, at 635-636. Several other Courts of Appeals adhere to this practice. See
   <em>
    Conner
   </em>
   v.
   <em>
    Reinhard,
   </em>
   <span class="citation" data-id="9477676"><a href="/opinion/506245/barbara-conner-v-rudy-g-reinhard/#394" aria-description="Citation for case: Barbara Conner v. Rudy G. Reinhard">847 F. 2d 384, 394, n. 8</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./488/856/">488 U. S. 856</a></span> (1988);
   <em>
    Houston
   </em>
   v.
   <em>
    Reich,
   </em>
   <span class="citation" data-id="560586"><a href="/opinion/560586/ricky-houston-v-allen-reich-harold-dean-mcham-the-excise-board-of-choctaw/#885" aria-description="Citation for case: Ricky Houston v. Allen Reich, Harold Dean McHam the...">932 F. 2d 883, 885</a></span> (CA10 1991);
   <em>
    Lundgren
   </em>
   v.
   <em>
    McDaniel,
   </em>
   <span class="citation" data-id="485039"><a href="/opinion/485039/lundgren-v-mcdaniel/#603" aria-description="Citation for case: Lundgren v. Mcdaniel">814 F. 2d 600, 603-604</a></span> (CA11 1987). Still others impose a more rigid pleading requirement. See
   <em>
    Wells
   </em>
   v.
   <em>
    Brown,
   </em>
   <span class="citation" data-id="8976025"><a href="/opinion/8984067/wells-v-brown/#592" aria-description="Citation for case: Wells v. Brown">891 F. 2d 591, 592</a></span> (CA6 1989) (§ 1983 plaintiff must specifically plead that suit for damages is brought against state official in individual capacity);
   <em>
    Nix
   </em>
   v.
   <em>
    Norman,
   </em>
   <span class="citation" data-id="526119"><a href="/opinion/526119/laura-nix-v-bobby-norman-arkansas-commission-on-law-enforcement-standards/#431" aria-description="Citation for case: Laura Nix v. Bobby Norman, Arkansas Commission on Law...">879 F. 2d 429, 431</a></span> (CA8 1989) (same). Because this issue is not properly before us, we simply reiterate the Third Circuit’s view that “[i]t is obviously preferable for the plaintiff to be specific in the first instance to avoid any ambiguity.” 912 F. 2d, at 636, n. 7. See this Court’s Rule 14.1(a) (“Only the questions set forth in the petition, or fairly included therein, will be considered by the Court”).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Hampton v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hampton v. United States"
type: case
citation: "425 U.S. 484 (1976)"
parallel_cite: "96 S. Ct. 1646; 48 L. Ed. 2d 113"
neutral_cite: 1976 U.S. LEXIS 49
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-04-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-04-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hampton v. United States
  varies_by_point: false
  scope_note: "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109437/hampton-v-united-states/"
  cluster_id: 109437
  opinion_id: 9426380
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[United States v. Russell]]", "[[Sorrells v. United States]]", "[[Sherman v. United States]]"]
aliases: ["Hampton v. US"]
tags: ["case", "entrapment", "due-process", "predisposition", "outrageous-government-conduct"]
holding: "Neither the entrapment defense nor the Due Process Clause bars conviction of a PREDISPOSED defendant even where a government agent…"
lake:
  record_id: Hampton v. United States
  status: verified
  projected_at: 2026-07-06
---

# Hampton v. United States

*425 U.S. 484 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Hampton was convicted of selling heroin to undercover federal agents. He claimed that a government informant had supplied him the very heroin he then sold, and argued that the Government's furnishing the contraband barred his conviction. The jury was instructed that predisposition defeated entrapment, and Hampton's predisposition to commit the offense was established.

## Issue
Whether the Government's supplying the contraband that a predisposed defendant then sells bars his conviction — either under the entrapment defense or under the Due Process Clause.

## Rule
No. A predisposed defendant cannot claim entrapment, and — in the plurality's view — due process does not bar his conviction even where a government agent supplied the contraband. "The remedy of the criminal defendant with respect to the acts of Government agents, which, far from being resisted, are encouraged by him, lies solely in the defense of entrapment." — 425 U.S. at 490. ^pin-490

"If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under the applicable provisions of state or federal law." — *Id.* ^pin-490a

## Application
Hampton's predisposition to sell heroin was established, so the entrapment defense was unavailable to him. And although the informant allegedly supplied the drug, the police, the informant, and Hampton acted in concert, and that conduct deprived him of no constitutional right — so neither entrapment nor due process freed him. (Justices Powell and Blackmun concurred in the judgment but declined to hold that government supply of contraband can never violate due process.)

## Conclusion
The conviction was affirmed; the defendant's predisposition foreclosed the entrapment defense, and the Government's role in supplying the contraband did not bar the conviction.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hampton* is a plurality decision; its judgment forecloses entrapment for a predisposed defendant, while the broader due-process holding (no bar even when the Government supplies contraband) commanded only three votes, with Powell and Blackmun reserving the possibility of an outrageous-government-conduct due-process defense in a future case.

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Hampton v. United States*, 425 U.S. 484 (1976) — https://www.courtlistener.com/opinion/109437/hampton-v-united-states/ — pinpoint: 490.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4a02aa420259d056", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hampton v. United States"}, "payload": {"all": [{"cite": "425 U.S. 484", "page": "484", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "425"}, {"cite": "96 S. Ct. 1646", "page": "1646", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "48 L. Ed. 2d 113", "page": "113", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "48"}, {"cite": "1976 U.S. LEXIS 49", "page": "49", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "425 U.S. 484", "official": {"cite": "425 U.S. 484", "page": "484", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "425"}, "official_selection_present": true, "record_id": "Hampton v. United States"}}
{"assertion_id": "3440d13e556535c9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-490", "record_id": "Hampton v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-490", "pinpoint_status": "slip-only", "quote": "--- # Hampton v. United States *425 U.S. 484 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Hampton was convicted of selling heroin to undercover federal agents. He claimed that a government informant had supplied him the very heroin he then sold, and argued that the Government's furnishing the contraband barred his conviction. The jury was instructed that predisposition defeated entrapment, and Hampton's predisposition to commit the offense was established. ## Issue Whether the Government's supplying the contraband that a predisposed defendant then sells bars his conviction — either under the entrapment defense or under the Due Process Clause. ## Rule No. A predisposed defendant cannot claim entrapment, and — in the plurality's view — due process does not bar his conviction even where a government agent supplied the contraband.", "quote_fidelity": "mismatch", "record_id": "Hampton v. United States", "star_marker": null}}
{"assertion_id": "4ad67e73da0a7df0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-490a", "record_id": "Hampton v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-490a", "pinpoint_status": "slip-only", "quote": "If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under the applicable provisions of state or federal law.", "quote_fidelity": "mismatch", "record_id": "Hampton v. United States", "star_marker": null}}
{"assertion_id": "9ab1d216f3ee74aa", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hampton v. United States"}, "payload": {"as_of_content": "1976-04-27", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hampton v. United States", "scope_note": "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds.", "varies_by_point": false}}
```

### lake record — Hampton v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hampton v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hampton v. United States",
    "case_name_short": "Hampton",
    "case_name_full": "HAMPTON, AKA BYERS v. UNITED STATES",
    "input_case_name": "Hampton v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-04-27",
    "year": 1976,
    "docket": null,
    "cluster_id": 109437,
    "lead_opinion_id": 9426380,
    "sibling_ids": [
      109437,
      9426380,
      9426381,
      9426382
    ],
    "absolute_url": "/opinion/109437/hampton-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9010580,
        "score": 20,
        "case_name": "Hampton v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "425 U.S. 484",
      "volume": "425",
      "reporter": "U.S.",
      "page": "484",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 1646",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 113",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 49",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "425 U.S. 484",
        "volume": "425",
        "reporter": "U.S.",
        "page": "484",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 1646",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "1646",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "48 L. Ed. 2d 113",
        "volume": "48",
        "reporter": "L. Ed. 2d",
        "page": "113",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 49",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "49",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "425 U.S. 484",
    "official_selection": {
      "court_class": "scotus",
      "selected": "425 U.S. 484",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-490",
      "page": null,
      "quote": "--- # Hampton v. United States *425 U.S. 484 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Hampton was convicted of selling heroin to undercover federal agents. He claimed that a government informant had supplied him the very heroin he then sold, and argued that the Government's furnishing the contraband barred his conviction. The jury was instructed that predisposition defeated entrapment, and Hampton's predisposition to commit the offense was established. ## Issue Whether the Government's supplying the contraband that a predisposed defendant then sells bars his conviction \u2014 either under the entrapment defense or under the Due Process Clause. ## Rule No. A predisposed defendant cannot claim entrapment, and \u2014 in the plurality's view \u2014 due process does not bar his conviction even where a government agent supplied the contraband.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-490a",
      "page": null,
      "quote": "If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under the applicable provisions of state or federal law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-04-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hampton v. United States",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Rehnquist, J.); Powell & Blackmun concurred in the judgment on narrower grounds.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Washington",
          "cluster_id": 7315755,
          "cite": [
            "131 F. Supp. 3d 1007",
            "2015 U.S. Dist. LEXIS 124545",
            "2015 WL 5522286"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rich",
          "cluster_id": 7311690,
          "cite": [
            "83 F. Supp. 3d 424",
            "2015 U.S. Dist. LEXIS 12347",
            "2015 WL 452190"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Uribe",
          "cluster_id": 5810602,
          "cite": [
            "199 Cal. App. 4th 836",
            "132 Cal. Rptr. 3d 102",
            "2011 Cal. App. LEXIS 1253"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert A. Burke",
          "cluster_id": 792103,
          "cite": [
            "425 F.3d 400",
            "68 Fed. R. Serv. 437",
            "2005 U.S. App. LEXIS 21013",
            "2005 WL 2373934"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cunningham",
          "cluster_id": 3952337,
          "cite": [
            "808 N.E.2d 488",
            "156 Ohio App. 3d 714",
            "2004 Ohio 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sanchez",
          "cluster_id": 72803,
          "cite": [
            "138 F.3d 1410",
            "1998 U.S. App. LEXIS 7487",
            "1998 WL 176673"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Greer",
          "cluster_id": 9050105,
          "cite": [
            "178 F.R.D. 418",
            "1998 U.S. Dist. LEXIS 3360",
            "1998 WL 128483"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Sandoval",
          "cluster_id": 603895,
          "cite": [
            "990 F.2d 481",
            "93 Daily Journal DAR 4205",
            "93 Cal. Daily Op. Serv. 2475",
            "1993 U.S. App. LEXIS 6759",
            "1993 WL 94342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellant/cross-Appellee v. Jack Pardue, Michel Pardue, Appellee/cross-Appellant",
          "cluster_id": 597867,
          "cite": [
            "983 F.2d 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barrera-Moreno",
          "cluster_id": 9003836,
          "cite": [
            "951 F.2d 1089",
            "1991 WL 263160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Douglas Floyd Osborne, Jr.",
          "cluster_id": 562325,
          "cite": [
            "935 F.2d 32"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nicholas R. Marino, United States of America v. Peter R. Chabot",
          "cluster_id": 563220,
          "cite": [
            "936 F.2d 23",
            "1991 U.S. App. LEXIS 12662",
            "1991 WL 104191"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Gonzales, A/K/A Jose Menas, United States of America v. Ruiz, Wilson",
          "cluster_id": 556660,
          "cite": [
            "927 F.2d 139",
            "1991 U.S. App. LEXIS 3577",
            "1991 WL 28353"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brent Eugene Smith, United States of America v. Roberto Osegueya Martinez, United States of America v. Richard Leroy Popp, Jr.",
          "cluster_id": 555136,
          "cite": [
            "924 F.2d 889",
            "91 Cal. Daily Op. Serv. 682",
            "91 Daily Journal DAR 1029",
            "1991 U.S. App. LEXIS 915"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane1_negative"
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
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 109895,
          "cite": [
            "57 L. Ed. 2d 65",
            "98 S. Ct. 2187",
            "437 U.S. 82",
            "1978 U.S. LEXIS 109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathews v. United States",
          "cluster_id": 112012,
          "cite": [
            "99 L. Ed. 2d 54",
            "108 S. Ct. 883",
            "485 U.S. 58",
            "1988 U.S. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
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
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Voigt",
          "cluster_id": 722380,
          "cite": [
            "89 F.3d 1050",
            "78 A.F.T.R.2d (RIA) 5577",
            "1996 U.S. App. LEXIS 16287",
            "1996 WL 380609"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Christopher Twigg, Iii, United States of America v. Henry Alfred Neville",
          "cluster_id": 361264,
          "cite": [
            "588 F.2d 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John M. Murphy",
          "cluster_id": 456168,
          "cite": [
            "768 F.2d 1518"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sonya Evette Singleton",
          "cluster_id": 754623,
          "cite": [
            "144 F.3d 1343",
            "1998 U.S. App. LEXIS 15451",
            "1998 WL 350507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Bagnariol, United States of America v. Gordon L. Walgren, United States of America v. Patrick Gallagher",
          "cluster_id": 397437,
          "cite": [
            "665 F.2d 877",
            "1981 U.S. App. LEXIS 15028"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Zavaras",
          "cluster_id": 158747,
          "cite": [
            "195 F.3d 573",
            "1999 Colo. J. C.A.R. 6110",
            "1999 U.S. App. LEXIS 26874",
            "1999 WL 973608"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stokes v. Gann",
          "cluster_id": 51572,
          "cite": [
            "498 F.3d 483",
            "2007 U.S. App. LEXIS 20735",
            "2007 WL 2430109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Rey",
          "cluster_id": 483372,
          "cite": [
            "811 F.2d 1453",
            "1987 U.S. App. LEXIS 3116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rafael Santana and Francis Fuentes",
          "cluster_id": 654192,
          "cite": [
            "6 F.3d 1",
            "1993 U.S. App. LEXIS 23810",
            "1993 WL 345746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gendron",
          "cluster_id": 195225,
          "cite": [
            "18 F.3d 955",
            "1994 WL 50975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hilario Mendoza-Salgado, United States of America v. Ramon Edwardo Garcia",
          "cluster_id": 583725,
          "cite": [
            "964 F.2d 993",
            "35 Fed. R. Serv. 1029",
            "1992 U.S. App. LEXIS 10413",
            "1992 WL 101352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kojo Sababu, Jaime Delgado, and Dora Garcia",
          "cluster_id": 533826,
          "cite": [
            "891 F.2d 1308",
            "1989 U.S. App. LEXIS 19420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. F. Thomas Little, United States of America v. Peter Chernik, United States of America v. Harold Grutchfield",
          "cluster_id": 447563,
          "cite": [
            "753 F.2d 1420"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul C. Porter, United States v. Walter G. Baker, United States v. Frederick L. Hearn, United States v. Larry Reservitz",
          "cluster_id": 453326,
          "cite": [
            "764 F.2d 1",
            "1985 U.S. App. LEXIS 20706"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Humberto Barbosa",
          "cluster_id": 775561,
          "cite": [
            "271 F.3d 438",
            "2001 U.S. App. LEXIS 24350",
            "2001 WL 1382027"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Angela Nolan-Cooper",
          "cluster_id": 757749,
          "cite": [
            "155 F.3d 221",
            "1998 U.S. App. LEXIS 21403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Roy Moreno Ramirez, United States of America v. Robert H. Reynolds",
          "cluster_id": 420788,
          "cite": [
            "710 F.2d 535",
            "13 Fed. R. Serv. 1310",
            "1983 U.S. App. LEXIS 25876"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Darrel Paterson Simpson, Robert MacRiner Anderson, and James Roy Freeman",
          "cluster_id": 484907,
          "cite": [
            "813 F.2d 1462",
            "1987 U.S. App. LEXIS 4561"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lilly Schmidt",
          "cluster_id": 733396,
          "cite": [
            "105 F.3d 82",
            "1997 U.S. App. LEXIS 705",
            "1997 WL 31579"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hampton v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MzY2ODE2MDAwMDAmcz0xOTU1NDYyJnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 18,
        "triage_snippet_classified": 182
      },
      "lane2_top_cited": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgmcz0zODA0ODAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
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
    "complete_query": "cites:(109437 OR 9426380 OR 9426381 OR 9426382)",
    "indexed_citing_opinions": 628,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109437,
        "count": 585,
        "count_source": "search"
      },
      {
        "opinion_id": 9426380,
        "count": 57,
        "count_source": "search"
      },
      {
        "opinion_id": 9426381,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426382,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 911,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hampton-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQyMjc5OTcmcz0yNzE1MDU1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109437+OR+9426380+OR+9426381+OR+9426382%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109437,
        "cited_id": 101251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 105681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 108906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 298766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 306412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 314188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 316284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 318238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 319175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 325618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 1270730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109437,
        "cited_id": 2136075,
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
    "date_created": "2026-07-05T06:03:22Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:11:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:03:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hampton v. United States

```
<opinion type="majority">
<author id="b555-6">Mr. Justice Kehnquist</author>
<p id="A0d">announced the judgment of the Court in an opinion in which The Chief Justice and Mr. Justice White join.</p>
<p id="b555-7">This case presents the question of whether a defendant may be convicted for the sale of contraband which he procured from a Government informant or agent. The Court of Appeals for the Eighth Circuit held he could be, and we agree.</p>
<p id="b555-8">I</p>
<p id="b555-9">Petitioner was convicted of two counts of distributing heroin in violation of <span class="citation no-link">21 U. S. C. §841</span> (a)(1) in the United States District Court for the Eastern District of Missouri and sentenced to concurrent terms of five years’ imprisonment (suspended).<footnotemark>1</footnotemark> The case arose from two sales of heroin by petitioner to agents of the Federal Drug Enforcement Administration (DEA) in St. Louis on February 25 and 26, 1974. The sales were arranged by one Hutton, who was a pool-playing acquaintance of petitioner at the Pud bar in St. Louis and also a DEA informant.</p>
<p id="b555-10">According to the Government’s witnesses, in late February 1974, Hutton and petitioner were shooting pool <page-number citation-index="1" label="486">*486</page-number>at the Pud when petitioner, after observing “track” (needle) marks on Hutton's arms told Hutton that he needed money and knew where he could get some heroin. Hutton responded that he could find a buyer and petitioner suggested that he “get in touch with those people.” Hutton then called DEA Agent Terry Sawyer and arranged a sale for 10 p. m. on February 25.<footnotemark>2</footnotemark></p>
<p id="b556-4">At the appointed time, Hutton and petitioner went to a prearranged meetingplace and were met by Agent Sawyer and DEA Agent McDowell, posing as narcotics dealers. Petitioner produced a tinfoil packet from his cap and turned it over to the agents who tested it, pronounced it “okay,” and negotiated a price of $145 which was paid to petitioner. Before they parted, petitioner told Sawyer that he could obtain larger quantities of heroin and gave Sawyer a phone number where he could be reached.</p>
<p id="b556-5">The next day Sawyer called petitioner and arranged for another “buy” that afternoon. Petitioner got Hutton to go along and they met the agents again near where they had been the previous night.</p>
<p id="b556-6">They all entered the agents’ car, and petitioner again produced a tinfoil packet from his cap. The agents again field-tested it and pronounced it satisfactory. Petitioner then asked for $500 which Agent Sawyer said he would get from the trunk. Sawyer got out and opened the trunk which was a signal to other agents to move in and arrest petitioner, which they did.</p>
<p id="b556-7">Petitioner’s version of events was quite different. According to him, in response to his statement that he was short of cash, Hutton said that he had a <page-number citation-index="1" label="487">*487</page-number>friend who was a pharmacist who could produce a nonnarcotic counterfeit drug which would give the same reaction as heroin. Hutton proposed selling this drug to gullible acquaintances who would be led to believe they were buying heroin. Petitioner testified that they successfully duped one buyer with this fake drug and that the sales which led to the arrest were solicited by petitioner<footnotemark>3</footnotemark> in an effort to profit further from this ploy.</p>
<p id="b557-5">Petitioner contended that he neither intended to sell, nor knew that he was dealing in heroin and that all of the drugs he sold were supplied by Hutton. His account was at least partially disbelieved by the jury which was instructed that in order to convict petitioner they had to find that the Government proved “that the defendant knowingly did an act which the law forbids, purposely intending to violate the law.” Thus the guilty verdict necessarily implies that the jury rejected petitioner's claim that he did not know the substance was heroin, and petitioner himself admitted both soliciting and carrying out sales. The only relevance of his version of the facts, then, lies in his having requested an instruction embodying that version.<footnotemark>4</footnotemark> He did not request a standard entrapment instruction but he did request the following:</p>
<blockquote id="b557-6">“The defendant asserts that he was the victim of entrapment as to the crimes charged in the indictment.</blockquote>
<blockquote id="b558-4"><page-number citation-index="1" label="488">*488</page-number>“If you find that the defendant’s sales of narcotics were sales of narcotics supplied to him by an informer in the employ of or acting on behalf of the government, then you must acquit the defendant because the law as a matter of policy forbids his conviction in such a case.</blockquote>
<blockquote id="b558-5">“Furthermore, under this particular defense, you need not consider the predisposition of the defendant to commit the offense charged, because if the governmental involvement through its informer reached the point that I have just defined in your own minds, then the predisposition of the defendant would not matter.” Brief for Petitioner 9.</blockquote>
<p id="b558-6">The trial court refused the instruction and petitioner was found guilty. He appealed to the United States Court of Appeals for the Eighth Circuit, claiming that if the jury had believed that the drug was supplied by Hutton he should have been acquitted. The Court of Appeals rejected this argument and affirmed the conviction, relying on our opinion in <em>United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">411 U. S. 423</a></span> (1973). <span class="citation" data-id="9461293"><a href="/opinion/323851/united-states-v-charles-hampton-also-known-as-michael-byers/" aria-description="Citation for case: United States v. Charles Hampton, Also Known as Michael...">507 F. 2d 832</a></span> (1974).</p>
<p id="b558-7">II</p>
<p id="b558-8">In <em>Russell </em>we held that the statutory defense of entrapment was not available where it was conceded that a Government agent supplied a necessary ingredient in the manufacture of an illicit drug. We reaffirmed the principle of <em>Sorrells </em>v. <em>United States, </em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span> (1932), and <em>Sherman </em>v. <em>United States, </em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U. S. 369</a></span> (1958), that the entrapment defense “focus[es] on the intent or predisposition of the defendant to commit the crime,” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#429" aria-description="Citation for case: United States v. Russell"><em>Russell, supra, at </em>429</a></span>, rather than upon the conduct of the Government’s agents. We ruled out the possibility that the defense of entrapment could ever be <page-number citation-index="1" label="489">*489</page-number>based upon governmental misconduct in a case, such as this one, where the predisposition of the defendant to commit the crime was established.</p>
<p id="b559-5">In holding that “[i]t is only when the Government’s deception actually implants the criminal design in the mind of the defendant that the defense of entrapment comes into play,” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#436" aria-description="Citation for case: United States v. Russell">411 U. S., at 436</a></span>, we, of course, rejected the contrary view of the dissents in that case and the concurrences in <em><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span> </em>and <em><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">Sherman</a></span>. </em>In view of these holdings, petitioner correctly recognizes that his case does not qualify as one involving “entrapment” at all. He instead relies on the language in <em>Russell </em>that “we may some day be presented with a situation in which the conduct of law enforcement agents is so outrageous that due process principles would absolutely bar the government from invoking judicial processes to obtain a conviction, cf. <em>Rochin </em>v. California, <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952) . . . .” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#431" aria-description="Citation for case: United States v. Russell">411 U. S., at 431-432</a></span>.</p>
<p id="b559-6">In urging that this case involves a violation of his due process rights, petitioner misapprehends the meaning of the quoted language in <em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/" aria-description="Citation for case: United States v. Russell">Russell, supra.</a></span> </em>Admittedly petitioner’s case is different from Russell’s but the difference is one of degree, not of kind. In <em>Russell </em>the ingredient supplied by the Government agent was a legal drug which the defendants demonstrably could have obtained from other sources besides the Government. Here the drug which the Government informant allegedly supplied to petitioner both was illegal and constituted the <em>corpus delicti </em>for the sale of which the petitioner was convicted. The Government obviously played a more significant role in enabling petitioner to sell contraband in this case than it did in <em>Russell.</em></p>
<p id="b559-7">But in each case the Government agents were acting in concert with the defendant, and in each case either the jury found or the defendant conceded that he was <page-number citation-index="1" label="490">*490</page-number>predisposed to commit the crime for which he was convicted. The remedy of the criminal defendant with respect to the acts of Government agents, which, far from being resisted, are encouraged by him, lies solely in the defense of entrapment. But, as noted, petitioner's conceded predisposition rendered this defense unavailable to him.</p>
<p id="b560-5">To sustain petitioner’s contention here wo Id run directly contrary to our statement in <em>Russell </em>that the defense of entrapment is not intended “to give the federal judiciary a ‘chancellor’s foot’ veto over law enforcement practices of which it did not approve. The execution of the federal laws under our Constitution is confided primarily to the Executive Branch of the Government, subject to applicable constitutional and statutory limitations and to judicially fashioned rules to enforce those limitations.” <span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S., at 435</a></span>.</p>
<p id="b560-6">The limitations of the Due Process Clause of the Fifth Amendment come into play only when the Government activity in question violates some protected right of the <em>defendant. </em>Here, as we have noted, the police, the Government informant, and the defendant acted in concert with one another. If the result of the governmental activity is to “implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission . . . ,” <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States"><em>Sorrells, supra, </em>at 442</a></span>, the defendant is protected by the defense of entrapment. If the police engage in illegal activity in concert with a defendant beyond the scope of their duties the remedy lies, not in freeing the equally culpable defendant, but in prosecuting the police under' the applicable provisions of state or federal law. See <em>O’Shea </em>v. <em>Littleton, </em><span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#503" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U. S. 488, 503</a></span> (1974); <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#428" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 428-429</a></span> (1976). But the police conduct here no more deprived defendant of any right <page-number citation-index="1" label="491">*491</page-number>secured to him by the United States Constitution than did the police conduct in <em>Bussell </em>deprive Russell of any rights.</p>
<p id="b561-5">
<em>Affirmed.</em>
</p>
<p id="b561-6">Mr. Justice Stevens took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b555-11"> Petitioner was placed on five years’ probation which, was to run concurrently with the remainder of a 28- to 30-year. state armed robbery sentence from which petitioner had escaped.</p>
</footnote>
<footnote label="2">
<p id="b556-8"> The testimony of Hutton is confused as to the dates. At one point he indicated that the initial conversation and the sale both occurred on February 25. At another point he testified that they occurred on two separate days.</p>
</footnote>
<footnote label="3">
<p id="b557-7"> On appeal, petitioner’s counsel, who was also his counsel at trial, conceded that petitioner was predisposed to commit this offense. <span class="citation" data-id="9461293"><a href="/opinion/323851/united-states-v-charles-hampton-also-known-as-michael-byers/" aria-description="Citation for case: United States v. Charles Hampton, Also Known as Michael...">507 F. 2d 832</a></span>, 836 n. 5 (CA8 1974).</p>
</footnote>
<footnote label="4">
<p id="b557-8"> The Court of Appeals treated the proffered instruction on its merits, rather than inquiring as to whether its refusal, in light of the other instructions given and of the jury’s verdict, may have been harmless error. We therefore do likewise.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Hanlon v. Berger.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Hanlon v. Berger"
type: case
citation: "526 U.S. 808 (1999)"
parallel_cite: "119 S. Ct. 1706; 143 L. Ed. 2d 978"
neutral_cite: 1999 U.S. LEXIS 3634
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-05-24
docket: 97-1927
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Hanlon v. Berger
  varies_by_point: false
  scope_note: "Per curiam companion to Wilson v. Layne; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1087699/hanlon-v-berger/"
  cluster_id: 1087699
  opinion_id: 1087699
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Layne]]", "[[Bivens v. Six Unknown Named Agents]]", "[[Harlow v. Fitzgerald]]"]
aliases: []
tags: ["case", "section-1983", "bivens", "qualified-immunity", "media-ride-along", "per-curiam"]
holding: "A media ride-along during the execution of a search warrant violated the Fourth Amendment under Wilson v. Layne, but the officers were entitled to qualified immunity."
lake:
  record_id: Hanlon v. Berger
  status: verified
  projected_at: 2026-07-06
---

# Hanlon v. Berger

*526 U.S. 808 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Paul and Erma Berger lived on a 75,000-acre ranch near Jordan, Montana. In 1993 a magistrate issued a warrant to search the ranch and outbuildings (excluding the residence) for evidence of unlawful taking of wildlife. When U.S. Fish and Wildlife Service agents executed the warrant, a CNN photo-and-reporting crew accompanied them, observing and recording the search. The Bergers sued the agents and an assistant U.S. attorney for damages under [[Bivens v. Six Unknown Named Agents]], alleging a Fourth Amendment violation.

## Issue
Whether the media's accompaniment during execution of the warrant stated a Fourth Amendment violation, and whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
The case is governed by its same-day companion, [[Wilson v. Layne]]. The Court treated the allegations as stating a Fourth Amendment violation under *[[Wilson v. Layne|Wilson]]* — "respondents alleged a Fourth Amendment violation under our decision today in *Wilson v. Layne.*" — 526 U.S. at 810. ^pin-810

But the officers were entitled to [[Qualified Immunity|qualified immunity]]: "Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in *Wilson* makes clear that this right was not clearly established in 1992." — *Id.* ^pin-810b

## Application
*[[Wilson v. Layne|Wilson]]* held that letting the media into a home during a warrant's execution violates the Fourth Amendment, and that the right was not clearly established before that 1999 decision. Because the 1993 ranch search here predated *[[Wilson v. Layne|Wilson]]* and no intervening decision had made the law any clearer, the agents could not have known their conduct was unlawful and were entitled to [[Qualified Immunity|qualified immunity]], just as in *[[Wilson v. Layne|Wilson]]*.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). The media ride-along stated a Fourth Amendment violation under *[[Wilson v. Layne]]*, but the officers received [[Qualified Immunity|qualified immunity]] because the right was not clearly established at the time of the search.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- A [[Common Legal Terms#per-curiam|per curiam]] companion decided the same day as [[Wilson v. Layne]], applying that decision's Fourth Amendment holding and qualified-immunity analysis to a media ride-along onto a ranch under a *[[Bivens v. Six Unknown Named Agents|Bivens]]* claim. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Hanlon v. Berger*, 526 U.S. 808 (1999) (per curiam) — https://www.courtlistener.com/opinion/1087699/hanlon-v-berger/ — pinpoint: 810.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3738cb1e95f5a4f6", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Hanlon v. Berger"}, "payload": {"all": [{"cite": "526 U.S. 808", "page": "808", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "526"}, {"cite": "119 S. Ct. 1706", "page": "1706", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "143 L. Ed. 2d 978", "page": "978", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "143"}, {"cite": "1999 U.S. LEXIS 3634", "page": "3634", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "526 U.S. 808", "official": {"cite": "526 U.S. 808", "page": "808", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "526"}, "official_selection_present": true, "record_id": "Hanlon v. Berger"}}
{"assertion_id": "7953f6e6c34cd729", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-810", "record_id": "Hanlon v. Berger"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-810", "pinpoint_status": "slip-only", "quote": "--- # Hanlon v. Berger *526 U.S. 808 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Paul and Erma Berger lived on a 75,000-acre ranch near Jordan, Montana. In 1993 a magistrate issued a warrant to search the ranch and outbuildings (excluding the residence) for evidence of unlawful taking of wildlife. When U.S. Fish and Wildlife Service agents executed the warrant, a CNN photo-and-reporting crew accompanied them, observing and recording the search. The Bergers sued the agents and an assistant U.S. attorney for damages under [[Bivens v. Six Unknown Named Agents]], alleging a Fourth Amendment violation. ## Issue Whether the media's accompaniment during execution of the warrant stated a Fourth Amendment violation, and whether the officers were entitled to qualified immunity. ## Rule The case is governed by its same-day companion, [[Wilson v. Layne]]. The Court treated the allegations as stating a Fourth Amendment violation under *Wilson* —", "quote_fidelity": "mismatch", "record_id": "Hanlon v. Berger", "star_marker": null}}
{"assertion_id": "a2795e0b7f6bb696", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-810b", "record_id": "Hanlon v. Berger"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-810b", "pinpoint_status": "slip-only", "quote": "Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in *Wilson* makes clear that this right was not clearly established in 1992.", "quote_fidelity": "mismatch", "record_id": "Hanlon v. Berger", "star_marker": null}}
{"assertion_id": "41aca81b96bd966b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Hanlon v. Berger"}, "payload": {"as_of_content": "1999-05-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Hanlon v. Berger", "scope_note": "Per curiam companion to Wilson v. Layne; good law.", "varies_by_point": false}}
```

### lake record — Hanlon v. Berger

```json
{
  "schema_version": "s2.v1",
  "record_id": "Hanlon v. Berger",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Hanlon v. Berger",
    "case_name_short": "Hanlon",
    "case_name_full": "HANLON Et Al. v. BERGER Et Ux.",
    "input_case_name": "Hanlon v. Berger",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-05-24",
    "year": 1999,
    "docket": "97-1927",
    "cluster_id": 1087699,
    "lead_opinion_id": 1087699,
    "sibling_ids": [
      1087699,
      9526990,
      9526991
    ],
    "absolute_url": "/opinion/1087699/hanlon-v-berger/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9183869,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9183868,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9182880,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      },
      {
        "cluster_id": 9182879,
        "score": 20,
        "case_name": "Hanlon v. Berger"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 808",
      "volume": "526",
      "reporter": "U.S.",
      "page": "808",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1706",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 978",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "978",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 3634",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3634",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 808",
        "volume": "526",
        "reporter": "U.S.",
        "page": "808",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1706",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1706",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 978",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "978",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 3634",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3634",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 808",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 808",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-810",
      "page": null,
      "quote": "--- # Hanlon v. Berger *526 U.S. 808 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Paul and Erma Berger lived on a 75,000-acre ranch near Jordan, Montana. In 1993 a magistrate issued a warrant to search the ranch and outbuildings (excluding the residence) for evidence of unlawful taking of wildlife. When U.S. Fish and Wildlife Service agents executed the warrant, a CNN photo-and-reporting crew accompanied them, observing and recording the search. The Bergers sued the agents and an assistant U.S. attorney for damages under [[Bivens v. Six Unknown Named Agents]], alleging a Fourth Amendment violation. ## Issue Whether the media's accompaniment during execution of the warrant stated a Fourth Amendment violation, and whether the officers were entitled to qualified immunity. ## Rule The case is governed by its same-day companion, [[Wilson v. Layne]]. The Court treated the allegations as stating a Fourth Amendment violation under *Wilson* \u2014",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-810b",
      "page": null,
      "quote": "Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in *Wilson* makes clear that this right was not clearly established in 1992.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Hanlon v. Berger",
    "varies_by_point": false,
    "scope_note": "Per curiam companion to Wilson v. Layne; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Detroy v. City & County of Honolulu",
          "cluster_id": 8653044,
          "cite": [
            "271 F. App'x 554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America, Inc. v. NBC Universal, Inc.",
          "cluster_id": 2682361,
          "cite": [
            "757 F.3d 1125",
            "2014 WL 3307834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Suiters",
          "cluster_id": 169685,
          "cite": [
            "499 F.3d 1228",
            "35 Media L. Rep. (BNA) 2409",
            "2007 U.S. App. LEXIS 20686",
            "2007 WL 2421765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villegas v. Gilroy Garlic Festival Ass'n",
          "cluster_id": 1441350,
          "cite": [
            "541 F.3d 950",
            "2008 U.S. App. LEXIS 18801",
            "2008 WL 4058566"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re DoubleClick Inc. Privacy Litigation",
          "cluster_id": 2429654,
          "cite": [
            "154 F. Supp. 2d 497",
            "2001 WL 303744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brunette v. Humane Society Of Ventura County",
          "cluster_id": 778168,
          "cite": [
            "294 F.3d 1205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8438109,
          "cite": [
            "359 F.3d 1066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny, George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny",
          "cluster_id": 785281,
          "cite": [
            "359 F.3d 1066",
            "2003 U.S. App. LEXIS 26896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 778595,
          "cite": [
            "298 F.3d 1022",
            "2002 Cal. Daily Op. Serv. 6645",
            "2002 Daily Journal DAR 8361",
            "2002 U.S. App. LEXIS 14911",
            "2002 WL 1677990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Artis v. United States",
          "cluster_id": 2159070,
          "cite": [
            "802 A.2d 959",
            "2002 D.C. App. LEXIS 380",
            "2002 WL 1575751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny, George Theofel Howard Teig David Kelley Integrated Capital Associates, Inc., a Delaware Corporation Nancy Rilett Ryan Tam Claudia English Teresa Patterson Tanya Young Roberto Marsella Regina Ovenden Emil Pesiri Eric Sullivan Douglas H. Wolf Richard Buckingham v. Alwyn Farey-Jones Iryna A. Kwasny",
          "cluster_id": 783378,
          "cite": [
            "341 F.3d 978",
            "2003 Daily Journal DAR 9849",
            "2003 Cal. Daily Op. Serv. 7848",
            "2003 U.S. App. LEXIS 17963"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Theofel v. Farey-Jones",
          "cluster_id": 8437727,
          "cite": [
            "341 F.3d 978",
            "2003 WL 22020268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Conradt Ex Rel. Conradt v. NBC Universal, Inc.",
          "cluster_id": 2009416,
          "cite": [
            "536 F. Supp. 2d 380",
            "36 Media L. Rep. (BNA) 1490",
            "2008 U.S. Dist. LEXIS 14112",
            "2008 WL 501361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 7103940,
          "cite": [
            "283 F.3d 985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joseph R. Ramirez Julia L. Ramirez Joshua Ramirez Regina Ramirez v. Butte-Silver Bow County John McPherson Sheriff of Butte-Silver Bow County Joe Lee, Undersheriff of Butte-Silver Bow County John Does 1-50, in Their Individual And/or Official Capacities, and Jeff Groh, Special Agent With the Bureau of Alcohol, Tobacco, and Firearms, Joseph R. Ramirez Julia L. Ramirez Joshua Ramirez Regina Ramirez v. Butte Silver Bow County John McPherson Sheriff of Butte-Silver Bow County Joe Lee, Undersheriff of Butte-Silver Bow County Jeff Groh, Special Agent With the Bureau of Alcohol, Tobacco, and Firearms John Does 1-50, in Their Individual And/or Official Capacities",
          "cluster_id": 776951,
          "cite": [
            "283 F.3d 985",
            "2002 Daily Journal DAR 2872",
            "2002 Cal. Daily Op. Serv. 2343",
            "2002 U.S. App. LEXIS 3893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brunette v. Humane Society",
          "cluster_id": 7105844,
          "cite": [
            "294 F.3d 1205",
            "2002 WL 1396511"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramirez v. Butte-Silver Bow County",
          "cluster_id": 7106653,
          "cite": [
            "298 F.3d 1022"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America v. NBC Universal, Inc.",
          "cluster_id": 3062233,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villegas v. City of Gilroy",
          "cluster_id": 3052856,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frederick v. BIOGRAPHY CHANNEL",
          "cluster_id": 2350172,
          "cite": [
            "683 F. Supp. 2d 798",
            "38 Media L. Rep. (BNA) 1362",
            "2010 U.S. Dist. LEXIS 9743",
            "2010 WL 431502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Hanlon v. Berger:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1087699 OR 9526990 OR 9526991) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 2,
        "triage_snippet_classified": 20
      },
      "lane2_top_cited": {
        "query": "cites:(1087699 OR 9526990 OR 9526991)",
        "reviewed": 23,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 20,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(1087699 OR 9526990 OR 9526991)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(1087699 OR 9526990 OR 9526991)",
    "indexed_citing_opinions": 23,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1087699,
        "count": 22,
        "count_source": "search"
      },
      {
        "opinion_id": 9526990,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9526991,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 34,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/hanlon-v-berger.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjAyMjYxNzcmcz03NzY5NTEmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%281087699+OR+9526990+OR+9526991%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1087699,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1087699,
        "cited_id": 748210,
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
    "date_created": "2026-07-05T06:11:33Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:15:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:12:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Hanlon v. Berger

```
<div>
<center><b><span class="citation" data-id="9526990"><a href="/opinion/1087699/hanlon-v-berger/" aria-description="Citation for case: Hanlon v. Berger">526 U.S. 808</a></span> (1999)</b></center>
<center><h1>HANLON et al.<br>
v.<br>
BERGER et ux.</h1></center>
<center>No. 97-1927.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 24, 1999.</center>
<center>Decided May 24, 1999.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><i>Richard A. Cordray</i> argued the cause for petitioners. With him on the briefs was <i>James A. Anzelmo.</i> </p>
<p><i>Henry H. Rossbacher</i> argued the cause for respondents. With him on the brief for respondents Berger et al. were <i>Nanci E. Nishimura</i> and <i>Jay F. Lansing. P. Cameron DeVore, Jessica L. Goldman,</i> and <i>David C. Kohler</i> filed briefs for respondents Cable News Network, Inc., et al.<sup>[*]</sup></p>
<p><span class="star-pagination">*809</span> Per Curiam.</p>
<p>Respondents Paul and Erma Berger sued petitioners special agents of the United States Fish and Wildlife Service and an assistant United States attorneyfor damages under <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). They alleged that the conduct of petitioners had violated their rights under the Fourth Amendment to the United States Constitution. <span class="citation" data-id="748210"><a href="/opinion/748210/paul-w-berger-and-erma-r-berger-v-rodney-c-hanlon-joel-scrafford/" aria-description="Citation for case: Paul W. Berger and Erma R. Berger v. Rodney C. Hanlon...">129 F. 3d 505</a></span> (CA9 1997). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./525/981/">525 U. S. 981</a></span> (1998).</p>
<p>Respondents live on a 75,000-acre ranch near Jordan, Montana. In 1993, a Magistrate Judge issued a warrant authorizing the search of "The Paul W. Berger ranch with appurtenant structures, excluding the residence" for evidence of "the taking of wildlife in violation of Federal laws." App. 17. About a week later, a multiple-vehicle caravan consisting of Government agents and a crew of photographers and reporters from Cable News Network, Inc. (CNN), proceeded to a point near the ranch. The agents executed the warrant and explained: "Over the course of the day, the officers searched the ranch and its outbuildings pursuant to the authority conferred by the search warrant. The CNN media crew . . . accompanied and observed the officers, and the media crew recorded the officers' conduct in executing the warrant." Brief for Petitioners 5.</p>
<p>Review of the complaint's much more detailed allegations to the same effect satisfies us that respondents alleged a Fourth Amendment violation under our decision today in <span class="star-pagination">*810</span> <i>Wilson</i> v. <i>Layne, ante,</i> p. 603. There we hold that police violate the Fourth Amendment rights of homeowners when they allow members of the media to accompany them during the execution of a warrant in their home. We also hold there that because the law on this question before today's decision was not clearly established, the police in that case were entitled to the defense of qualified immunity. <i>Ante,</i>  at 605-606.</p>
<p>Petitioners maintain that even though they may have violated the Fourth Amendment rights of respondents, they are entitled to the defense of qualified immunity. We agree. Our holding in <i>Wilson</i> makes clear that this right was not clearly established in 1992. The parties have not called our attention to any decisions which would have made the state of the law any clearer a year laterat the time of the search in this case. We therefore vacate the judgment of the Court of Appeals for the Ninth Circuit and remand the case for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Stevens, concurring in part and dissenting in part.</p>
<p>As I explain in my dissent in <i>Wilson</i> v. <i>Layne, ante,</i> p. 618, I am convinced that the constitutional rule recognized in that case had been clearly established long before 1992. I therefore respectfully dissent from the Court's disposition of this case on qualified immunity grounds.</p>
<h2>NOTES</h2>
<p>[*]   A brief of <i>amici curiae</i> urging reversal was filed for ABC, Inc., et al. by <i>Lee Levine, James E. Grossberg, Jay Ward Brown, Henry S. Hoberman, Richard M. Schmidt, Jr., Susanna M. Lowy, Harold W. Fuson, Jr., Barbara Wartelle Wall, Ralph E. Goldberg, Karlene W. Goller, Jerry S.</i>  <i>Birenz, Slade R. Metcalf, Jack N. Goodman, David S. J. Brown, René P. Milam, George Freeman,</i> and <i>Jane E. Kirtley.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the National Association of Criminal Defense Lawyers by <i>Joshua L. Dratel;</i> and for the National Association of Securities and Commercial Law Attorneys by <i>Kevin P. Roddy.</i> </p>
<p><i>M. Reed Hopper</i> and <i>Robin L. Rivett</i> filed a brief for the Pacific Legal Foundation as <i>amicus curiae.</i> </p>

</div>
```

---
