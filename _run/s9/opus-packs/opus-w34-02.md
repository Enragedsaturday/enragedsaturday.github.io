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

## GROUP: content/cases/Thompson v. Clark.md  (`case`, 5 assertions)

### content_page

```
---
title: Thompson v. Clark
type: case
citation: "596 U.S. 36 (2022)"
parallel_cite: 142 S. Ct. 1332
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2022
date_decided: ""
docket: 20-659
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
  opinion_url: "https://www.courtlistener.com/opinion/6457347/thompson-v-clark/"
  cluster_id: 6457347
  opinion_id: 6329458
  identity_checked: true
lake:
  record_id: Thompson v. Clark
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Key
related:
  - "[[Chiaverini v. City of Napoleon]]"
  - "[[Heck v. Humphrey]]"
  - "[[Malicious Prosecution under the Fourth Amendment]]"
tags:
  - case
  - fourth-amendment
  - malicious-prosecution
  - section-1983
  - favorable-termination
holding: "To show a favorable termination for a Fourth Amendment § 1983 malicious-prosecution claim, a plaintiff need only show that the criminal prosecution ended without a conviction — not that it ended with some affirmative indication of innocence."
---

# Thompson v. Clark

*596 U.S. 36 (2022)* (No. 20-659) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6457347 → opinion 6329458; quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 596 U.S. ___; pin cited slip-style per S2 A3). S9 promotes. -->

## Background
Larry Thompson's sister-in-law, who lived with his family in Brooklyn, called authorities to report suspected child abuse of his newborn daughter; the marks were later shown to be a normal diaper rash. When EMTs and police arrived, Thompson refused to let them enter without a warrant. Officers entered anyway, and Thompson was arrested and charged with obstructing governmental administration and resisting arrest. He was held two days; the charges were later dismissed on the prosecution's motion, without any explanation. Thompson sued the officers under 42 U.S.C. § 1983, advancing a Fourth Amendment malicious-prosecution claim. Under Second Circuit precedent (*Lanning*), a plaintiff had to show that the prosecution ended not merely without a conviction but with some affirmative indication of innocence — a showing Thompson could not make — so the courts below dismissed the claim.

## Issue
What a plaintiff must show to establish the "favorable termination" element of a Fourth Amendment malicious-prosecution claim under § 1983: is it enough that the prosecution ended without a conviction, or must it also have ended with an affirmative indication of innocence?

## Rule
A Fourth Amendment claim under § 1983 for malicious prosecution borrows the elements of the most analogous common-law tort — malicious prosecution — as it stood in 1871, requiring the plaintiff to show a favorable termination of the underlying criminal case. Because the American tort-law consensus of 1871 treated the favorable-termination element as satisfied whenever the prosecution ended without a conviction, the Court held: "To demonstrate a favorable termination of a criminal prosecution for purposes of the Fourth Amendment claim under §1983 for malicious prosecution, a plaintiff need only show that his prosecution ended without a conviction." — 596 U.S. 36 (slip op., at 2). ^pin-2

## Application
Thompson's charges were dismissed before trial without any explanation, which is enough to satisfy the favorable-termination requirement as the Court defined it. Requiring an affirmative indication of innocence, the Court reasoned, would be inconsistent with the 1871 tort consensus, would be hard to apply to the many prosecutions that end in unexplained dismissals, and would leave plaintiffs unable to sue simply because a busy prosecutor gave no reasons. Because Thompson's prosecution ended without a conviction, he satisfied that element and his claim could proceed.

## Conclusion
The judgment of the Second Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Kavanaugh, J., delivered the opinion of the Court; Alito, J., joined by Thomas, Gorsuch, and Barrett, JJ., dissented, disputing that the Fourth Amendment houses a malicious-prosecution claim at all.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Thompson* supplies the favorable-termination rule for Fourth Amendment malicious-prosecution claims; the Court applied and built on it in *[[Chiaverini v. City of Napoleon]]* (2024), which held that such claims are assessed charge by charge.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Key*

## Sources
- [*Thompson v. Clark*, 596 U.S. 36 (2022)](https://www.courtlistener.com/opinion/6457347/thompson-v-clark/) — pinpoint: slip op., at 2 (Opinion of the Court, holding); quote string-matched to the CL slip-opinion text 2026-07-07.
- [*Chiaverini v. City of Napoleon*, 602 U.S. 556 (2024)](https://www.courtlistener.com/opinion/10600074/chiaverini-v-city-of-napoleon/) — applying *Thompson*'s framework charge by charge.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3bac3aa30a54e7aa", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "596 U.S. 36 (2022)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "142 S. Ct. 1332", "title": "Thompson v. Clark", "year": "2022"}}
{"assertion_id": "7706cacb835d4bf5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "To show a favorable termination for a Fourth Amendment § 1983 malicious-prosecution claim, a plaintiff need only show that the criminal prosecution ended without a conviction — not that it ended with some affirmative indication of innocence.", "title": "Thompson v. Clark"}}
{"assertion_id": "f4a47bdb9f111e58", "dimension": "support", "kind": "home_role", "locator": {"home": "Malicious Prosecution under the Fourth Amendment"}, "payload": {"home": "Malicious Prosecution under the Fourth Amendment", "role": "Key", "title": "Thompson v. Clark"}}
{"assertion_id": "61b37d797ef6cde9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Thompson v. Clark"}}
{"assertion_id": "86520e80cf970912", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Thompson v. Clark", "varies_by_point": "false"}}
```

### lake record — Thompson v. Clark

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thompson v. Clark",
  "status": "under_review",
  "identity": {
    "case_name": "Thompson v. Clark",
    "case_name_short": "Thompson",
    "case_name_full": "",
    "input_case_name": "Thompson v. Clark",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2022,
    "docket": "20-659",
    "cluster_id": 6457347,
    "lead_opinion_id": 6329458,
    "sibling_ids": [],
    "absolute_url": "/opinion/6457347/thompson-v-clark/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "596 U.S. 36",
      "volume": "596",
      "reporter": "U.S.",
      "page": "36",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 1332",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "596 U.S. 36",
        "volume": "596",
        "reporter": "U.S.",
        "page": "36",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 1332",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "596 U.S. 36",
    "official_selection": {
      "court_class": "scotus",
      "selected": "596 U.S. 36",
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
    "date_created": "2026-07-06T12:11:00Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:11:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "thompson-v-clark--6457347",
      "to_record_id": "Thompson v. Clark",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Thompson v. Clark

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

                     THOMPSON v. CLARK ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE SECOND CIRCUIT

      No. 20–659.     Argued October 12, 2021—Decided April 4, 2022
In January 2014, petitioner Larry Thompson was living with his fiancée
  (now wife) and their newborn baby in an apartment in Brooklyn, New
  York. Thompson’s sister-in-law, who apparently suffered from a men-
  tal illness, called 911 to report that Thompson was sexually abusing
  the baby. When Emergency Medical Technicians arrived, Thompson
  denied that anyone had called 911. When the EMTs returned with
  four police officers, Thompson told them that they could not enter with-
  out a warrant. The police nonetheless entered and handcuffed Thomp-
  son. EMTs took the baby to the hospital where medical professionals
  examined her and found no signs of abuse. Meanwhile, Thompson was
  arrested and charged with obstructing governmental administration
  and resisting arrest. He was detained for two days before being re-
  leased. The charges against Thompson were dismissed before trial
  without any explanation by the prosecutor or judge. After the dismis-
  sal, Thompson filed suit under 42 U. S. C. §1983, alleging several con-
  stitutional violations, including a Fourth Amendment claim for mali-
  cious prosecution. To maintain that Fourth Amendment claim under
  §1983, a plaintiff such as Thompson must demonstrate, among other
  things, that he obtained a favorable termination of the underlying
  criminal prosecution. To meet that requirement, Second Circuit prec-
  edent required Thompson to show that his criminal prosecution ended
  not merely without a conviction, but also with some affirmative indi-
  cation of his innocence. See Lanning v. Glens Falls, 908 F. 3d 19, 22.
  The District Court, bound by Lanning, held that Thompson’s criminal
  case had not ended in a way that affirmatively indicated his innocence
  because Thompson could not offer any substantial evidence to explain
  why his case was dismissed. The Second Circuit affirmed the dismis-
  sal of Thompson’s claim. This Court granted certiorari to resolve a
2                        THOMPSON v. CLARK

                                 Syllabus

    split among the Courts of Appeals over how to apply the favorable ter-
    mination requirement of the Fourth Amendment claim under §1983
    for malicious prosecution.
Held: To demonstrate a favorable termination of a criminal prosecution
 for purposes of the Fourth Amendment claim under §1983 for mali-
 cious prosecution, a plaintiff need not show that the criminal prosecu-
 tion ended with some affirmative indication of innocence. A plaintiff
 need only show that his prosecution ended without a conviction.
 Thompson has satisfied that requirement here. Pp. 4–12.
    (a) To determine the elements of a constitutional claim under §1983,
 this Court’s practice is to first look to the elements of the most analo-
 gous tort as of 1871 when §1983 was enacted, so long as doing so is
 consistent with “the values and purposes of the constitutional right at
 issue.” Manuel v. Joliet, 580 U. S. 357, 370. Here, as most of the
 Courts of Appeals to consider the question have determined, the most
 analogous tort to this Fourth Amendment claim is malicious prosecu-
 tion. Pp. 4–7.
    (b) In accord with the elements of the malicious prosecution tort, a
 Fourth Amendment claim under §1983 for malicious prosecution re-
 quires the plaintiff to show a favorable termination of the underlying
 criminal case against him. The parties to this case, as well as the lower
 courts, disagree about what a favorable termination entails, i.e., is it
 sufficient to show that Thompson’s prosecution ended without a con-
 viction or must he also show that his prosecution ended with some af-
 firmative indication of innocence? To resolve that disagreement, the
 Court looks to American malicious prosecution tort law as of 1871. At
 that time, most American courts agreed that the favorable termination
 element of a malicious prosecution claim was satisfied so long as the
 prosecution ended without a conviction. A plaintiff could maintain a
 malicious prosecution claim when, for example, the prosecutor aban-
 doned the criminal case or the court dismissed the case without provid-
 ing a reason.
    The American tort-law consensus as of 1871 did not require a plain-
 tiff in a malicious prosecution suit to show that his prosecution ended
 with an affirmative indication of innocence, and this Court similarly
 construes Thompson’s Fourth Amendment claim under §1983 for ma-
 licious prosecution. Doing so is consistent with “the values and pur-
 poses” of the Fourth Amendment. Manuel, 580 U. S., at 370. Ques-
 tions concerning whether a criminal defendant was wrongly charged,
 or whether an individual may seek redress for a wrongful prosecution,
 cannot reasonably depend on whether the prosecutor or court hap-
 pened to explain why charges were dismissed. And requiring a plain-
 tiff to show that his prosecution ended with an affirmative indication
 of innocence is not necessary to protect officers from unwarranted civil
                     Cite as: 596 U. S. ____ (2022)                      3

                                Syllabus

  suits, as officers are still protected by the requirement that the plain-
  tiff show the absence of probable cause and by qualified immunity.
  Pp. 7–11.
794 Fed. Appx. 140, reversed and remanded.

   KAVANAUGH, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and BREYER, SOTOMAYOR, KAGAN, and BARRETT, JJ., joined. ALITO,
J., filed a dissenting opinion, in which THOMAS and GORSUCH, JJ., joined.
                        Cite as: 596 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–659
                                    _________________


            LARRY THOMPSON, PETITIONER v.
                 PAGIEL CLARK, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                                   [April 4, 2022]

   JUSTICE KAVANAUGH delivered the opinion of the Court.
   Larry Thompson was charged and detained in state crim-
inal proceedings, but the charges were dismissed before
trial without any explanation by the prosecutor or judge.
After the dismissal, Thompson alleged that the police offic-
ers who initiated the criminal proceedings had “maliciously
prosecuted” him without probable cause. App. 33–34.
Thompson sued and sought money damages from those of-
ficers in federal court. As relevant here, he advanced a
Fourth Amendment claim under 42 U. S. C. §1983 for ma-
licious prosecution.
   To maintain that Fourth Amendment claim under §1983,
a plaintiff such as Thompson must demonstrate, among
other things, that he obtained a favorable termination of the
underlying criminal prosecution. Cf. Heck v. Humphrey,
512 U. S. 477, 484, and n. 4 (1994). This case requires us to
flesh out what a favorable termination entails. Does it suf-
fice for a plaintiff to show that his criminal prosecution
ended without a conviction? Or must the plaintiff also
demonstrate that the prosecution ended with some affirm-
ative indication of his innocence, such as an acquittal or a
2                   THOMPSON v. CLARK

                     Opinion of the Court

dismissal accompanied by a statement from the judge that
the evidence was insufficient?
   We conclude as follows: To demonstrate a favorable ter-
mination of a criminal prosecution for purposes of the
Fourth Amendment claim under §1983 for malicious prose-
cution, a plaintiff need only show that his prosecution
ended without a conviction. Thompson satisfied that re-
quirement in this case. We therefore reverse the judgment
of the U. S. Court of Appeals for the Second Circuit and re-
mand for further proceedings consistent with this opinion.
                              I
  Larry Thompson lived with his fiancée (now wife) and
their newborn baby girl in an apartment in Brooklyn, New
York. In January 2014, Thompson’s sister-in-law was also
staying there. The sister-in-law apparently suffered from a
mental illness. One day that January, the sister-in-law
called 911 and claimed that Thompson was sexually abus-
ing his one-week-old baby daughter. Two Emergency Med-
ical Technicians promptly responded. When the EMTs ar-
rived at the family’s apartment, Thompson asked the EMTs
why they were there and denied that anyone had called 911.
The EMTs left and informed the police of the situation.
  The EMTs and four police officers then returned to the
apartment. When they arrived, Thompson told them that
they could not come in without a warrant. The police offic-
ers nonetheless entered and, after a brief scuffle, hand-
cuffed Thompson. The EMTs followed the officers into the
apartment and examined the baby. After finding red marks
on the baby’s body, the EMTs took the baby to the hospital
for evaluation. The marks turned out to be a case of diaper
rash. The medical professionals found no signs of abuse.
  Meanwhile, the police officers arrested Thompson for re-
sisting their entry into the apartment. Thompson was
taken to a local hospital and then to jail. While Thompson
was in custody, one of the police officers prepared and filed
                 Cite as: 596 U. S. ____ (2022)           3

                     Opinion of the Court

a criminal complaint charging Thompson with obstructing
governmental administration and resisting arrest. Thomp-
son remained in custody for two days. A judge then re-
leased him on his own recognizance.
  Before trial, the prosecution moved to dismiss the
charges, and the trial judge in turn dismissed the case. The
prosecutor did not explain why she sought to dismiss the
charges, nor did the trial judge explain why he dismissed
the case.
  After the criminal prosecution ended, Thompson brought
suit for damages under 42 U. S. C. §1983 against the police
officers who had arrested and charged him. Thompson al-
leged several constitutional violations, including a Fourth
Amendment claim for “malicious prosecution.” App. 33.
Thompson asserted that the officers “maliciously prose-
cuted” him and “subjected him to an unlawful, illegal and
excessive detention” in violation of his Fourth Amendment
rights. Id., at 34.
   To prevail on that claim under Second Circuit precedent,
Thompson had to show that his criminal prosecution ended
not merely without a conviction, but also with some affirm-
ative indication of his innocence. See Lanning v. Glens
Falls, 908 F. 3d 19, 22 (2018). Thompson could not put forth
any substantial evidence that would explain why the pros-
ecutor had moved to dismiss the charges or why the trial
court had dismissed the charges. Therefore, the District
Court ruled that Thompson’s criminal case had not ended
in a way that affirmatively indicated his innocence. The
District Court granted judgment to the defendant officers
on that Fourth Amendment claim. Notably, the District
Court also opined that the relevant Second Circuit prece-
dent “can and should be changed” to say that a favorable
termination occurs so long as the prosecution ends without
a conviction. 364 F. Supp. 3d 178, 181, 196–197 (EDNY
2019). On appeal, however, the U. S. Court of Appeals for
the Second Circuit adhered to its precedent in Lanning and
4                    THOMPSON v. CLARK

                      Opinion of the Court

affirmed the dismissal of Thompson’s Fourth Amendment
claim. 794 Fed. Appx. 140 (2020).
   The Courts of Appeals have split over how to apply the
favorable termination requirement of the Fourth Amend-
ment claim under §1983 for malicious prosecution. In ad-
dition to the Second Circuit, some other Courts of Appeals
have held that a favorable termination requires some af-
firmative indication of innocence. See, e.g., Kossler v.
Crisanti, 564 F. 3d 181, 187 (CA3 2009) (en banc); Cordova
v. Albuquerque, 816 F. 3d 645, 649 (CA10 2016). By con-
trast, the Eleventh Circuit has held that a favorable termi-
nation occurs so long as the criminal prosecution ends with-
out a conviction. See Laskar v. Hurd, 972 F. 3d 1278, 1282
(2020). This Court granted certiorari to resolve the split.
592 U. S. ___ (2021).
                               II
                               A
   In 1871, Congress passed and President Grant signed the
Civil Rights Act of 1871. Section 1 of that Act, now codified
at 42 U. S. C. §1983, created a species of federal tort liabil-
ity for individuals to sue state and local officers for depriva-
tions of constitutional rights.
   In this case, Thompson sued several police officers under
§1983, alleging that he was “maliciously prosecuted” with-
out probable cause and that he was seized as a result. App.
33–34. He brought a Fourth Amendment claim under
§1983 for malicious prosecution, sometimes referred to as a
claim for unreasonable seizure pursuant to legal process.
This Court’s precedents recognize such a claim. See Manuel
v. Joliet, 580 U. S. 357, 363–364, 367–368 (2017); Albright
v. Oliver, 510 U. S. 266, 271 (1994) (plurality opinion); see
also id., at 290–291 (Souter, J., concurring in judgment).
And following this Court’s precedents, the District Courts
and Courts of Appeals have decided numerous cases involv-
ing Fourth Amendment claims under §1983 for malicious
                      Cite as: 596 U. S. ____ (2022)                     5

                          Opinion of the Court

prosecution. See, e.g., Pitt v. District of Columbia, 491 F. 3d
494, 510–511 (CADC 2007) (“[N]early every other Circuit
has held that malicious prosecution is actionable under the
Fourth Amendment to the extent that the defendant’s ac-
tions cause the plaintiff to be ‘seized’ without probable
cause”); Kossler, 564 F. 3d, at 186–187; Sykes v. Anderson,
625 F. 3d 294, 308–309 (CA6 2010); Durham v. Horner, 690
F. 3d 183, 188 (CA4 2012); Myers v. Koopman, 738 F. 3d
1190, 1194 (CA10 2013); Winfrey v. Rogers, 901 F. 3d 483,
491–493 (CA5 2018); Lanning, 908 F. 3d, at 28; Jordan v.
Waldoboro, 943 F. 3d 532, 545 (CA1 2019); Williams v.
Aguirre, 965 F. 3d 1147, 1157 (CA11 2020).1
   The narrow dispute in this case concerns one element of
the Fourth Amendment claim under §1983 for malicious
prosecution. To determine the elements of a constitutional
claim under §1983, this Court’s practice is to first look to
the elements of the most analogous tort as of 1871 when
§1983 was enacted, so long as doing so is consistent with
“the values and purposes of the constitutional right at is-
sue.” Manuel, 580 U. S., at 370; see also Nieves v. Bartlett,
587 U. S. ___, ___ (2019) (slip op., at 12); Heck, 512 U. S., at
483.2
   Here, as most of the Courts of Appeals to consider the

——————
   1 Thompson also brought a Fourth Amendment claim for unreasonable

seizure (labeled a false arrest claim), based on his initial arrest before
charges were filed against him. But the jury ruled against him on the
merits of that claim. That claim is not before us, and we therefore do not
consider it.
   2 Because this claim is housed in the Fourth Amendment, the plaintiff

also has to prove that the malicious prosecution resulted in a seizure of
the plaintiff. See Manuel v. Joliet, 580 U. S. 357, 365–366 (2017). It has
been argued that the Due Process Clause could be an appropriate ana-
lytical home for a malicious prosecution claim under §1983. See Albright
v. Oliver, 510 U. S. 266, 281, 286 (1994) (Kennedy, J., concurring in judg-
ment). If so, the plaintiff presumably would not have to prove that he
was seized as a result of the malicious prosecution. But we have no oc-
casion to consider such an argument here.
6                      THOMPSON v. CLARK

                        Opinion of the Court

question have determined, the most analogous tort to this
Fourth Amendment claim is malicious prosecution. See
Kossler, 564 F. 3d, at 186; Sykes, 625 F. 3d, at 308–309;
Durham, 690 F. 3d, at 188; Myers, 738 F. 3d, at 1194; Lan-
ning, 908 F. 3d, at 28; Jordan, 943 F. 3d, at 545. That is
because the gravamen of the Fourth Amendment claim for
malicious prosecution, as this Court has recognized it, is the
wrongful initiation of charges without probable cause. And
the wrongful initiation of charges without probable cause is
likewise the gravamen of the tort of malicious prosecution.
   In American courts as of 1871, the malicious prosecution
tort generally allowed recovery against an individual who
had initiated or caused the initiation of criminal proceed-
ings despite having “no good reason to believe” that crimi-
nal charges were “justified by the facts and the law.” T.
Cooley, Law of Torts 180 (1880) (Cooley); see also 1 F. Hil-
liard, The Law of Torts or Private Wrongs 412–414 (1866)
(Hilliard). The malicious prosecution tort protected against
“injury to the person, as connected with false imprison-
ment” and against “a wrong to character or reputation.” Id.,
at 412 (emphasis deleted).
   American courts described the elements of the malicious
prosecution tort as follows: (i) the suit or proceeding was
“instituted without any probable cause”; (ii) the “motive in
instituting” the suit “was malicious,” which was often de-
fined in this context as without probable cause and for a
purpose other than bringing the defendant to justice; and
(iii) the prosecution “terminated in the acquittal or dis-
charge of the accused.” Cooley 181.3
   That third requirement—a favorable termination of the
underlying criminal prosecution—is the focus of the parties’
dispute in this case.

——————
  3 We need not decide whether a plaintiff bringing a Fourth Amend-

ment claim under §1983 for malicious prosecution must establish malice
(or some other mens rea) in addition to the absence of probable cause.
                  Cite as: 596 U. S. ____ (2022)            7

                      Opinion of the Court

                                B
   In accord with the elements of the malicious prosecution
tort, a Fourth Amendment claim under §1983 for malicious
prosecution requires the plaintiff to show a favorable termi-
nation of the underlying criminal case against him. The
favorable termination requirement serves multiple pur-
poses: (i) it avoids parallel litigation in civil and criminal
proceedings over the issues of probable cause and guilt;
(ii) it precludes inconsistent civil and criminal judgments
where a claimant could succeed in the tort action after hav-
ing been convicted in the criminal case; and (iii) it prevents
civil suits from being improperly used as collateral attacks
on criminal proceedings. Cf. Heck, 512 U. S., at 484–485;
see also McDonough v. Smith, 588 U. S. ___, ___ (2019) (slip
op., at 7).
   The parties to this case disagree about what a favorable
termination entails. In particular, does it suffice for a
plaintiff to show that his prosecution ended without a con-
viction? Or must the plaintiff also show that his prosecu-
tion ended with some affirmative indication of innocence,
such as an acquittal or a dismissal accompanied by a state-
ment from the judge that the evidence was insufficient?
   To resolve that disagreement, we must look to American
malicious prosecution tort law as of 1871. See Nieves, 587
U. S., at ___ (slip op., at 12). In most American courts that
had considered the question as of 1871, the favorable ter-
mination element of a malicious prosecution claim was sat-
isfied so long as the prosecution ended without a conviction.
As one influential New York decision explained, when the
individual was “convicted in the suit or proceeding com-
plained of,” he could not maintain an action for malicious
prosecution. Clark v. Cleveland, 6 Hill 344, 346, n. a (1844).
But when the individual was not convicted, the “question
is, whether the prosecution instituted by the defendant can
be said to have been terminated, disposed of, or, as the
books usually say, at an end.” Id., at 346. The “technical
8                   THOMPSON v. CLARK

                      Opinion of the Court

prerequisite is only that the particular prosecution be dis-
posed of in such a manner” that it “cannot be revived.” Id.,
at 347; Bacon v. Waters, 84 Mass. 400, 401–402 (1861); M.
Newell, Law of Malicious Prosecution 327–328 (1892)
(Newell).
   On that point, American courts as of 1871 were largely in
agreement. To take one example, the Supreme Court of In-
diana ruled that a dismissal satisfied the favorable termi-
nation requirement because it marked “an end to further
proceedings against the defendant” on the charges. Chap-
man v. Woods, 6 Blackf. 504, 505–506 (1843). Similarly, the
Supreme Court of Tennessee concluded that a suit was
proper when “the prosecution was at an end.” Pharis v.
Lambert, 33 Tenn. 228, 232 (1853).
   For that reason, a plaintiff could maintain a malicious
prosecution claim when, for example, the prosecutor aban-
doned the criminal case or the court dismissed the case
without providing a reason. See, e.g., Fay v. O’Neill, 36
N. Y. 11, 13 (1867); Murray v. Lackey, 6 N. C. 368, 368–369
(1818); Driggs v. Burton, 44 Vt. 124, 143–144 (1871); Brown
v. Randall, 36 Conn. 56, 61–63 (1869); Chapman, 6 Blackf.,
at 505–506; Sayles v. Briggs, 45 Mass. 421, 425–426 (1842);
Yocum v. Polly, 40 Ky. 358, 359 (1841); Burhans v. Sanford,
19 Wend. 417, 418 (N. Y. 1838); Cotton v. Wilson, Minor 203
(Ala. 1824).
   Several courts explicitly added, moreover, that a favora-
ble termination did not require an acquittal or a dismissal
accompanied by some affirmative indication of innocence.
In the words of one court, it “is not to be understood, that
an action, for a malicious prosecution, will not lie, unless
the party has been acquitted by a jury on trial.” Thomas v.
DeGraffenreid, 11 S. C. L. 143, 144–145 (1819). “On the
contrary, a person may have his action after a bill rejected
by the grand jury, or even where no bill has been preferred,
if there is a final end of the prosecution, and the party dis-
charged.” Id., at 145; see also Chapman, 6 Blackf., at 505–
                  Cite as: 596 U. S. ____ (2022)            9

                      Opinion of the Court

506.
   The treatises of that era agreed that a favorable termina-
tion occurred so long as the prosecution ended without con-
viction. Cooley’s tort-law treatise stated, for example, that
“the reasonable rule seems to be, that the technical prereq-
uisite is only that the particular prosecution be disposed of
in such a manner that this cannot be revived, and the pros-
ecutor, if he proceeds further, will be put to a new one.”
Cooley 186; see also Newell 343 (expressing approval of the
rule); Hilliard 453, and n. 5 (recognizing the rule).
   The parties to this case have identified only one court
that required something more, such as an acquittal or a dis-
missal accompanied by some affirmative indication of inno-
cence. In 1863, the Rhode Island Supreme Court concluded,
“with reluctance,” that “ ‘the termination must be such as to
furnish prima facie evidence that the action was without
foundation.’ ” Rounds v. Humes, 7 R. I. 535, 537 (1863). But
Rhode Island stood as an outlier on that question. The
other American courts to consider the issue did not require
some affirmative indication of innocence in order for a ma-
licious prosecution tort claim to proceed. The courts simply
required that the prosecution ended in the defendant’s fa-
vor. As Chief Judge Pryor explained in his comprehensive
opinion for the Eleventh Circuit in Laskar v. Hurd, 972
F. 3d, at 1287: “The clear majority of American courts did
not limit favorable terminations to those that suggested the
accused’s innocence.”
   Against that body of precedent and historical practice, re-
spondent Clark contends that American courts as of 1871
had not settled on any particular favorable termination
rule. But the cases and treatises that respondent latches
onto addressed a separate issue—not whether the prosecu-
tion had terminated in the defendant’s favor, but whether
the prosecution had terminated at all. In particular, courts
divided over whether a prosecutor’s dismissal without dis-
charge by a judge in fact terminated a prosecution. Some
10                  THOMPSON v. CLARK

                     Opinion of the Court

courts concluded that a prosecution ended when the prose-
cutor dismissed the case, even if the court had not yet taken
action. See, e.g., Woodman v. Prescott, 66 N. H. 375, 376–
377 (1890); see also 1 F. Hilliard, The Law of Torts or Pri-
vate Wrongs 475 (1874); Newell 327–328; Cooley 186.
Other courts said that a prosecution did not end until a
judge discharged, or formally released, the defendant from
the case. See, e.g., DeGraffenreid, 11 S. C. L., at 145; Pau-
kett v. Livermore, 5 Iowa 277, 282 (1857).
   But those cases did not purport to alter the basic favora-
ble termination principle—namely, that a malicious prose-
cution claim could proceed when the prosecution termi-
nated without a conviction.
   Respondent also seizes on a comment in the American
Law Institute’s 1976 Second Restatement of Torts (as have
most of the Courts of Appeals that have sided with respond-
ent’s position on this issue). See Jordan, 943 F. 3d, at 545–
546; Lanning, 908 F. 3d, at 26; Salley v. Myers, 971 F. 3d
308, 312–313 (CA4 2020); Jones v. Clark Cty., 959 F. 3d
748, 763–765 (CA6 2020); Cordova, 816 F. 3d, at 651. The
comment in the Second Restatement opined that, for pur-
poses of a malicious prosecution claim, a criminal case ter-
minates “in favor of the accused” when the prosecution ends
in a way “as to indicate the innocence of the accused.” Re-
statement (Second) of Torts §660, and Comment a (1976).
   But respondent’s reliance on the 1976 Restatement is
flawed because the Restatement did not purport to describe
the consensus of American law as of 1871, at least on that
question. The status of American law as of 1871 is the rel-
evant inquiry for our purposes. See Manuel, 580 U. S., at
370; Nieves, 587 U. S., at ___ (slip op., at 12); Laskar, 972
F. 3d, at 1286. And in the overwhelming majority of Amer-
ican jurisdictions that had considered the issue as of 1871,
a plaintiff alleging malicious prosecution did not need to
show that his prosecution had ended with some affirmative
indication of innocence.
                 Cite as: 596 U. S. ____ (2022)           11

                     Opinion of the Court

   Because the American tort-law consensus as of 1871 did
not require a plaintiff in a malicious prosecution suit to
show that his prosecution ended with an affirmative indi-
cation of innocence, we similarly construe the Fourth
Amendment claim under §1983 for malicious prosecution.
Doing so is consistent, moreover, with “the values and pur-
poses” of the Fourth Amendment. Manuel, 580 U. S., at
370. The question of whether a criminal defendant was
wrongly charged does not logically depend on whether the
prosecutor or court explained why the prosecution was dis-
missed. And the individual’s ability to seek redress for a
wrongful prosecution cannot reasonably turn on the fortu-
ity of whether the prosecutor or court happened to explain
why the charges were dismissed. In addition, requiring the
plaintiff to show that his prosecution ended with an affirm-
ative indication of innocence would paradoxically foreclose
a §1983 claim when the government’s case was weaker and
dismissed without explanation before trial, but allow a
claim when the government’s evidence was substantial
enough to proceed to trial. That would make little sense.
Finally, requiring a plaintiff to show that his prosecution
ended with an affirmative indication of innocence is not nec-
essary to protect officers from unwarranted civil suits—
among other things, officers are still protected by the re-
quirement that the plaintiff show the absence of probable
cause and by qualified immunity.
                         *    *    *
   In sum, we hold that a Fourth Amendment claim under
§1983 for malicious prosecution does not require the plain-
tiff to show that the criminal prosecution ended with some
affirmative indication of innocence. A plaintiff need only
show that the criminal prosecution ended without a convic-
tion. Thompson has satisfied that requirement here. We
express no view, however, on additional questions that may
be relevant on remand, including whether Thompson was
12                  THOMPSON v. CLARK

                     Opinion of the Court

ever seized as a result of the alleged malicious prosecution,
whether he was charged without probable cause, and
whether respondent is entitled to qualified immunity. On
remand, the Second Circuit or the District Court as appro-
priate may consider those and other pertinent questions.
We reverse the judgment of the U. S. Court of Appeals for
the Second Circuit and remand for further proceedings con-
sistent with this opinion.

                                             It is so ordered.
                 Cite as: 596 U. S. ____ (2022)            1

                      LITO, J., concurring
                     ALITO      dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 20–659
                         _________________


          LARRY THOMPSON, PETITIONER v.
               PAGIEL CLARK, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                        [April 4, 2022]

   JUSTICE ALITO, with whom JUSTICE THOMAS and
JUSTICE GORSUCH join, dissenting.
   Homer described the mythical chimera as a “grim mon-
ster” made of “all lion in front, all snake behind, all goat
between.” The Iliad p. 201 (R. Fagles trans. 1990). Today,
the Court creates a chimera of a constitutional tort by
stitching together elements taken from two very different
claims: a Fourth Amendment unreasonable seizure claim
and a common-law malicious-prosecution claim.
   The Court justifies this creation on the ground that mali-
cious prosecution is the common-law tort that is most anal-
ogous to an unreasonable seizure claim. And because a
common-law malicious-prosecution claim demanded proof
of a favorable termination, the Court holds that its new cre-
ation includes that element. But this Court has never held
that the Fourth Amendment houses a malicious-prosecu-
tion claim, and the Court defends its analogy with just two
sentences of independent analysis and a reference to a body
of lower court cases.
   I cannot agree with that approach. The Court’s independ-
ent analysis of this important question is far too cursory,
and its reliance on lower court cases is particularly ill-ad-
vised here because that body of case law appears to have
been heavily influenced by a mistaken reading of the plu-
rality opinion in Albright v. Oliver, 510 U. S. 266 (1994).
2                    THOMPSON v. CLARK

                      ALITO, J., dissenting

   What the Court has done is to recognize a novel hybrid
claim of uncertain scope that has no basis in the Constitu-
tion and is almost certain to lead to confusion.
                            I
  The Court asserts that malicious prosecution is the com-
mon-law tort that is most analogous to petitioner’s Fourth
Amendment claim, ante, at 5, but in fact the Fourth Amend-
ment and malicious prosecution have almost nothing in
common.
                                A
   The Fourth Amendment prohibits “unreasonable
searches and seizures.” And a Fourth Amendment claim
based on an unreasonable seizure has two indispensable
elements: (i) there must have been a “seizure,” i.e., an arrest
or some other use of “ ‘physical force’ or a ‘show of authority’
that ‘in some way restrain[s] the liberty’ of [a] person,”
Torres v. Madrid, 592 U. S. ___, ___ (2021) (slip op., at 3),
and (ii) the seizure must have been “unreasonable,” which
means, in the case of a full-blown arrest, that the officers
making the arrest must have lacked probable cause. Dis-
trict of Columbia v. Wesby, 583 U. S. ___, ___ (2018) (slip
op., at 7).
   Malicious prosecution, on the other hand, requires proof
that “(i) the suit or proceeding was ‘instituted without any
probable cause;’ (ii) the ‘motive in instituting’ the suit ‘was
malicious . . . ; and (iii) the prosecution ‘terminated in the
acquittal or discharge of the accused.’ ” Ante, at 6 (quoting
T. Cooley, Law of Torts 180 (1880) (Cooley)); see also Ma-
nuel v. Joliet, 580 U. S. 357, 378 (2017) (ALITO, J., dissent-
ing).
   A comparison of the elements of the malicious-prosecution
tort with the elements of a Fourth Amendment unreasona-
ble-seizure claim shows that there is no overlap. That is, a
plaintiff suing for unreasonable seizure need not prove any
                  Cite as: 596 U. S. ____ (2022)              3

                       ALITO, J., dissenting

of the elements of common-law malicious prosecution, and
a plaintiff suing for common-law malicious prosecution
need not prove any of the elements required to establish an
unreasonable seizure.
   Start with the elements of an unreasonable-seizure
claim. Such a claim does not require proof that there was a
“prosecution”—i.e., a criminal proceeding that is initiated
by the filing of charges in the form of a criminal complaint,
information, or indictment—while a malicious-prosecution
claim obviously requires a prosecution. See, e.g., 1 F. Hilli-
ard, The Law of Torts or Private Wrongs §2, pp. 413–414
(1866) (Hilliard) (“The general principle is laid down, that
an action lies for maliciously causing one to be indicted,
whereby he is damnified, either in person, reputation, or
property” (emphasis added)); Cooley 180 (“[I]t is a duty
which every man owes to every other not to institute pro-
ceedings maliciously, which he has no good reason to believe
are justified by the facts and the law” (emphasis added));
M. Newell, Law of Malicious Prosecution, False Imprison-
ment, and Abuse of Process §1, p. 3 (1892) (Newell) (same);
see also W. Prosser, Law of Torts 860 (1941) (“The interest
in freedom from unjustifiable litigation is protected by an
action for malicious prosecution” (boldface deleted and em-
phasis added)). A person who is arrested without probable
cause may have a viable unreasonable-seizure claim even if
he or she is released before any charges are filed.
   An unreasonable-seizure claim also does not require
“malice.” The Court has “almost uniformly rejected invita-
tions to probe subjective intent” in Fourth Amendment
cases. Ashcroft v. al-Kidd, 563 U. S. 731, 737 (2011). If a
law enforcement officer makes an arrest without probable
cause, the arrest is unreasonable and therefore unconstitu-
tional even if the officer harbors no ill will for the arrestee.
Likewise, if an officer makes an arrest with probable cause,
there is no Fourth Amendment violation regardless of the
“actual motivations of the individual officers involved.”
4                   THOMPSON v. CLARK

                      ALITO, J., dissenting

Whren v. United States, 517 U. S. 806, 813 (1996); see also
Cordova v. Albuquerque, 816 F. 3d 645, 664 (CA10 2016)
(Gorsuch, J., concurring in judgment).
   Finally, the validity of an unreasonable-seizure claim is
not dependent on the outcome of any prosecution that hap-
pens to follow a seizure. A person who is arrested without
probable cause but then convicted based on evidence discov-
ered after the arrest is not barred from recovering simply
because he or she cannot show a favorable termination to
the proceeding. See Wallace v. Kato, 549 U. S. 384, 389–
392 (2007); cf. Heck v. Humphrey, 512 U. S. 477, 487, n. 7
(1994) (a person may bring “a suit for damages attributable
to an allegedly unreasonable search” even if he or she was
convicted). Thus, an unreasonable-seizure claim may be
shown without proving any of the elements of a common-
law malicious-prosecution claim.
   Turning now to the elements of malicious prosecution, we
see that all of those may be established without proving ei-
ther of the two elements that the constitutional text and our
precedents require in order to establish an unreasonable
seizure.
   First, the tort of malicious prosecution does not require a
seizure within the meaning of the Fourth Amendment.
There are cases in which defendants charged with non-
violent crimes agree to appear for arraignment and are then
released pending trial on their own recognizance. These de-
fendants are prosecuted, and they may bring a common-law
suit for malicious prosecution if the other elements of that
tort can be shown, but they are not seized. See, e.g., 1 Hil-
liard §1, at 412 (noting that malicious prosecution may in-
volve “injury to the person, as connected with false impris-
onment,” but is “primarily . . . a wrong to character or
reputation”); 3 D. Dobbs, The Law of Torts §586, p. 388
(2011) (the “prosecution does not necessarily involve any
detention of the plaintiff at all”). The term seizure would
have to be given a novel and extravagant interpretation in
                 Cite as: 596 U. S. ____ (2022)            5

                     ALITO, J., dissenting

order to reach a “defendant awaiting trial on his own recog-
nizance” or one who simply receives a “summons to appear
at trial.” Cordova, 816 F. 3d, at 663 (opinion of Gorsuch,
J.).
  Second, since a malicious-prosecution claim does not re-
quire a seizure, it obviously does not require proof that the
person bringing suit was seized without probable cause.
The claim does demand proof that the person bringing suit
was prosecuted without probable cause, but probable cause
at the time of arrest is a different question from probable
cause at the time at which a prosecution is initiated.
  In light of the differences between these two claims, it is
apparent that a Fourth Amendment unreasonable-seizure
claim is not analogous to a claim for malicious prosecution.
Much more analogous are the common-law torts of false ar-
rest and false imprisonment, which protect against “[e]very
confinement of the person,” including one effected by “forci-
bly detaining [someone] in the public streets.” Wallace, 549
U. S., at 388–389 (internal quotation marks omitted); see
also Dobbs, Law of Torts §41 (describing elements of false
imprisonment and false arrest); Restatement (Second) of
Torts §35 (1964) (same).
                            B
  The Court does not make a serious effort to justify its
analogy between unreasonable seizure and malicious pros-
ecution. Instead, the Court largely relies on the fact that
“most of the Courts of Appeals to consider the question”
have drawn that analogy, ante, at 6, but the Court ignores
contrary lower court authority. See, e.g., Manuel v. Joliet,
903 F. 3d 667, 670 (CA7 2018); Jones v. Clark County, 959
F. 3d 748, 776–777 (CA6 2020) (Murphy, J., concurring in
part); Pagan-Gonzalez v. Moreno, 919 F. 3d 582, 608–617
(CA1 2019) (Barron, J., concurring). But in any event, we
should not decide this important question without inde-
pendent analysis, and the Court’s own cursory analysis is
6                    THOMPSON v. CLARK

                      ALITO, J., dissenting

erroneous.
   The Court claims that the “gravamen” of petitioner’s
Fourth Amendment claim is the same as that of a mali-
cious-prosecution claim: the “wrongful initiation of charges
without probable cause.” Ante, at 6. But what the Court
describes is not a Fourth Amendment violation at all. As
explained, that Amendment protects against “unreasonable
searches and seizures”—not the unreasonable “initiation of
charges.” In fact, “the specific provisions of the Bill of
Rights neither impose a standard for the initiation of a
prosecution” nor “require a pretrial hearing to weigh evi-
dence according to a given standard.” Albright, 510 U. S.,
at 282 (Kennedy, J., concurring in judgment); see also 4 W.
LaFave, J. Israel, N. King, & O. Kerr, Criminal Procedure
§14.2(a), pp. 329, 331 (4th ed. 2015) (noting that the Con-
stitution does not require “screening” of the decision to pros-
ecute “by some neutral body” to ensure “some minimal evi-
dence supporting the charge,” and “the sole constitutional
protection” is “what the Fourth Amendment requires to jus-
tify physical restraints”).
   The Court also says that the initiation of charges must be
“wrongful,” but it is not clear what that means. If that term
simply refers to the lack of probable cause, then the Court
has failed to capture the “gravamen” of malicious prosecu-
tion because that tort requires not just that the defendant
initiated charges “without probable cause” but also—as the
name of the tort suggests—that this was done with “mal-
ice.” See 1 Hilliard §4, at 416 (“want of probable cause” is
not enough “without malice”); 1 Newell §6, at 7 (“The plain-
tiff must show that the defendant acted from malicious mo-
tives in prosecuting him”). Cf. ante, at 6, n. 5 (claiming to
reserve the question whether the claim requires malice).
   If, on the other hand, the Court uses the term “wrongful”
to require “malice,” then the claim it has endorsed is even
more incompatible with the Fourth Amendment, which al-
                 Cite as: 596 U. S. ____ (2022)            7

                     ALITO, J., dissenting

most always imposes a purely objective standard. See su-
pra, at 4.
                            II
   The Court’s recognition of a Fourth Amendment mali-
cious-prosecution claim has no basis in our precedents.
                              A
   The Court relies on certain lower court decisions that ac-
cepted the strange concept of a Fourth Amendment mali-
cious-prosecution claim, but that line of cases developed in
large part because of a misunderstanding of the tersely
worded plurality opinion in Albright, 510 U. S. 266. See
Hernandez-Cuevas v. Taylor, 723 F. 3d 91, 99 (CA1 2013)
(noting that “dicta” in Albright led many jurisdictions to
“recogniz[e] a Fourth Amendment malicious prosecution
claim”). Instead of simply accepting that misreading, we
should explain what Albright actually decided and what the
plurality said.
   In that case, Kevin Albright was arrested and bound over
for trial without probable cause. The prosecution was dis-
missed before trial, and Albright then sued under 42
U. S. C. §1983. The District Court dismissed his suit; the
Court of Appeals affirmed the dismissal; and when the case
was argued in this Court, the only claim that Albright
pressed was that his prosecution without probable cause vi-
olated substantive due process. 510 U. S., at 268 (plurality
opinion). He did not advance either a Fourth Amendment
claim or a malicious-prosecution claim.
   This Court affirmed the dismissal of Albright’s substan-
tive due process claim, and while no opinion gained major-
ity approval, both the four Justices who joined the plurality
opinion and the three justices who concurred in the judg-
ment agreed that substantive due process does not include
the right to be free from prosecution without probable
8                    THOMPSON v. CLARK

                      ALITO, J., dissenting

cause. Id., at 268, 275 (plurality opinion); id., at 282 (opin-
ion of Kennedy, J.); id., at 286 (Souter, J., concurring in
judgment). That is all that Albright actually decided.
   The terse plurality opinion did make comments about the
Fourth Amendment and malicious prosecution, and those
comments have led to confusion in the lower courts. But a
careful reading of the plurality opinion shows that it in no
way suggested that the Fourth Amendment protects
against malicious prosecution.
   When the plurality commented on the Fourth Amend-
ment, it was addressing Albright’s prosecution-without-
probable-cause claim, not malicious prosecution. And in
connection with the prosecution-without-probable-cause
claim, the plurality made the following two points. First,
the plurality noted that “[w]here a particular Amendment
‘provides an explicit textual source of constitutional protec-
tion’ against a particular sort of government behavior, ‘that
Amendment, not the more generalized notion of “substan-
tive due process,” must be the guide for analyzing [the]
claims.’ ” Id., at 273. Second, the plurality observed that
the Fourth Amendment is the constitutional provision that
deals with “pretrial deprivations of liberty.” Id., at 274.
   What this discussion suggested was that if any provision
of the Constitution provided a home for Albright’s prosecu-
tion-without-probable-cause claim, the Fourth Amendment
was a better bet than the Fourteenth Amendment’s Due
Process Clause. But the plurality did not conclude or even
suggest that a prosecution-without-probable-cause claim
could be brought under the Fourth Amendment. See id., at
274–275 (expressly declining to express a view on the ques-
tion). Indeed, the plurality expressly reiterated that “the
accused is not ‘entitled to judicial oversight or review of the
decision to prosecute,’ ” suggesting instead that the harm to
Albright—if any—was that he was “not merely charged”
but also “submitted himself to arrest.” Id., at 274 (quoting
Gerstein v. Pugh, 420 U. S. 103, 114 (1975)).
                      Cite as: 596 U. S. ____ (2022)                     9

                          ALITO, J., dissenting

   As for malicious prosecution, the plurality did not even
hint that such a claim could be brought under the Fourth
Amendment. The plurality’s only two references to mali-
cious prosecution appeared in the portion of the opinion
that set out what had occurred in the lower courts. Foot-
note 3 recounted that Albright’s complaint contained a com-
mon-law malicious-prosecution claim but that this claim
had been dismissed without prejudice and that this issue
was not before the Court. 510 U. S., at 269, n. 3. Footnote
4 then observed that there was an “ ‘embarrassing diversity
of judicial opinion’ ” in the lower courts as to whether a ma-
licious-prosecution claim was actionable under §1983, and
the footnote added that substantive due process did not
“furnish the constitutional peg on which to hang such a
‘tort.’ ” Id., at 270–271, n. 4. But the plurality opinion did
not suggest that the Fourth Amendment could provide such
a “peg,” and neither did any other Justice who concurred in
the judgment.*
                             B
  Manuel v. Joliet, 580 U. S. 357, also provides no support
for a Fourth Amendment malicious-prosecution claim.
There, petitioner Elijah Manuel brought suit under the
Fourth Amendment, alleging that he was arrested without


——————
   *Justice Scalia’s concurring opinion made no mention of malicious
prosecution. Justice Ginsburg mentioned malicious prosecution only
when describing Albright’s claims, see 510 U. S., at 277, n. 1, and to note
that it was “anomalous” that Albright sought to hold a police officer (ra-
ther than a prosecutor) liable under a malicious-prosecution theory, id.,
at 279, n. 5. Justice Kennedy, joined by JUSTICE THOMAS, filed an opinion
concurring in the judgment and argued that “if a State did not provide a
tort remedy for malicious prosecution, there would be force to the argu-
ment that the malicious initiation of a baseless criminal prosecution in-
fringes an interest protected by the Due Process Clause.” Id., at 286.
But he did not suggest that a malicious-prosecution claim could be
brought under the Fourth Amendment.
10                  THOMPSON v. CLARK

                      ALITO, J., dissenting

probable cause and then held for seven weeks without prob-
able cause after a judge ordered him detained. Id., at 359–
360. The Court reasoned that the Fourth Amendment pro-
hibits “government officials from detaining a person in the
absence of probable cause.” Id., at 367. A violation of that
prohibition, the Court continued, may occur both “before
the formal onset of a criminal proceeding” and “when legal
process itself goes wrong—when, for example, a judge’s
probable-cause determination is predicated solely on a po-
lice officer’s false statements.” Ibid. Accordingly, the Court
concluded that the plaintiff in that case could state a Fourth
Amendment claim because the “judge’s order holding [him]
for trial” was not supported by probable cause. Id., at 368.
   Although the majority asserts that Manuel authorized
Fourth Amendment malicious-prosecution claims, see ante,
at 4, Manuel did no such thing. That decision expressly de-
clined to determine “whether (and, if so, how) [petitioner’s
Fourth Amendment claim] should resemble the malicious
prosecution tort.” Id., at 372, n. 10. Indeed, the majority’s
analysis here is incompatible with the analysis in Manuel,
where the gravamen of the wrong was that petitioner was
“detain[ed] . . . in the absence of probable cause.” Id., at
367. Manuel thus provides no support for the Court’s sug-
gestion that the Fourth Amendment prohibits the “initia-
tion of charges without probable cause.” Ante, at 6.
                               III
  Instead of clarifying the law regarding §1983 malicious-
prosecution claims, today’s decision, I fear, will sow more
confusion. The Court endorses a Fourth Amendment claim
for malicious prosecution that appears to have the following
elements: (1) the defendant “initiat[ed]” charges against the
plaintiff in a way that was “wrongful” and “without proba-
ble cause,” (2) the “malicious prosecution resulted in a sei-
zure of the plaintiff,” and (3) the prosecution must not have
ended in conviction. Ante, at 5–6, and n. 2. This tort has
                  Cite as: 596 U. S. ____ (2022)           11

                      ALITO, J., dissenting

no precedent in Fourth Amendment law. It is markedly dif-
ferent from the common-law tort of malicious prosecution,
and its dimensions are uncertain.
  First, it is not clear why this tort requires both a seizure
and a prosecution. As noted, the two do not always go to-
gether, and if the aim is to permit the victims of malicious
prosecution to sue under §1983, it is not clear why detention
should be required. While pretrial detention certainly in-
creases the harm inflicted by a malicious prosecution, such
a prosecution can be very damaging even if the victim is
never detained. See, e.g., M. Bigelow, The Law of Torts 204
(1875) (a plaintiff may show damage to “his person by im-
prisonment, his reputation by the scandal, or . . . his prop-
erty by the expense”). The majority’s only answer to the
question why the claim requires a seizure is that it is
“housed in the Fourth Amendment,” ante, at 5, n. 2, but
that response begs the antecedent question whether the
Fourth Amendment houses a malicious-prosecution suit at
all.
  Second, where the person bringing suit under §1983 is
arrested and then prosecuted, it is not clear whether both
the arrest and the prosecution must have been done with-
out probable cause and without a legitimate law enforce-
ment purpose. An arrest made without probable cause may
be followed by a prosecution based on new evidence that
clearly establishes probable cause. And by the same token,
the evidence that establishes probable cause at the time of
arrest may be thoroughly discredited at some point well be-
fore the termination of a prosecution.
  Third and most important, it is not clear what the Court
means when it says that the “gravamen” of the claim is
“wrongful initiation of charges without probable cause.”
Ante, at 6. Since the Court refers repeatedly to “malicious
prosecution,” one might think that this requires a guilty
mental state, but in a footnote, the Court raises the possi-
bility that the constitutional tort it recognizes may require
12                   THOMPSON v. CLARK

                       ALITO, J., dissenting

nothing more than the absence of probable cause. See ibid.,
n. 3.
   If that turns out to be so, it is hard to see even the slight-
est connection between the Court’s new tort and common-
law malicious prosecution. Malice is the hallmark of a
malicious-prosecution claim. Even if a prosecution is
brought and maintained without probable cause, a
malicious-prosecution claim cannot succeed without proof
of malice. See supra, at 6. And if the Court’s new tort has
nothing to do with malicious prosecution, what possible rea-
son can there be for borrowing that tort’s favorable-termi-
nation element?
                              IV
   Instead of creating a new hybrid claim, we should simply
hold that a malicious-prosecution claim may not be brought
under the Fourth Amendment. Such a holding would not
leave a person in petitioner’s situation without legal protec-
tion. Petitioner brought Fourth Amendment claims against
respondents for false arrest, excessive force, and unlawful
entry, but after trial a jury ruled against him on all those
claims. See App. 142–146. Petitioner could have also
sought relief under state law. See, e.g., Cordova, 816 F. 3d,
at 662 (opinion of Gorsuch, J.). New York law appears to
recognize a malicious-prosecution tort with an element very
much like the favorable-termination element that the Court
adopts today, see Lanning v. Glens Falls, 908 F. 3d 19, 24–
25 (CA2 2018), but petitioner chose not to bring such a
claim. See Tr. of Oral Arg. 40–41.
   For these reasons, I would affirm the judgment below,
and I therefore respectfully dissent.

```

---

## GROUP: content/cases/Torres v. Madrid.md  (`case`, 5 assertions)

### content_page

```
---
title: "Torres v. Madrid"
type: case
citation: "592 U.S. 306 (2021)"
parallel_cite: "141 S. Ct. 989; 209 L. Ed. 2d 190"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-03-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Torres v. Madrid
  varies_by_point: false
  scope_note: "Recent SCOTUS holding; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4867542/torres-v-madrid/"
  cluster_id: 4867542
  opinion_id: 4671321
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny / Refinement"
related: ["[[California v. Hodari D.]]", "[[Tennessee v. Garner]]", "[[Graham v. Connor]]", "[[Brendlin v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure"]
holding: "Physical force applied with intent to restrain is a seizure at the moment of application, even if the person does not submit and is not subdued."
lake:
  record_id: Torres v. Madrid
  status: verified
  projected_at: 2026-07-06
---

# Torres v. Madrid

*592 U.S. 306 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New Mexico State Police officers approached Torres in an apartment-complex parking lot to execute an arrest warrant for someone else. Torres, who was experiencing methamphetamine withdrawal, got into her car; the officers, believing she was reaching for a weapon, fired thirteen shots, striking her twice in the back. She nonetheless drove away, eluding capture that day, and later sued under § 1983, claiming the shooting was an unreasonable seizure.

## Issue
Whether the application of physical force to a person with intent to restrain is a Fourth Amendment seizure when the force does not succeed in subduing the person and she temporarily eludes capture.

## Rule
Yes. Adopting the common-law rule that the slightest application of force to effect an arrest is an arrest, the Court held: "The application of physical force to the body of a person with intent to restrain is a seizure, even if the force does not succeed in subduing the person." — slip op., at 1. ^pin-op1

A seizure by force is complete at the moment force is applied with intent to restrain; submission is not required. The Court cautioned that such a seizure is only the first step in the analysis — only unreasonable seizures violate the Fourth Amendment.

## Application
Because the officers shot Torres with the intent to restrain her, the bullets that struck her effected a seizure at the moment of impact — notwithstanding that she managed to drive away and was not subdued or apprehended until the next day. The shooting was therefore a seizure of her person, and the lower court erred in holding that her escape defeated any seizure; whether that seizure was reasonable remained for remand.

## Conclusion
The shooting was a seizure even though Torres temporarily eluded capture; the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]. Physical force applied with intent to restrain seizes the person at the instant of application.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Torres* distinguishes [[California v. Hodari D.]], where an unsubmitting suspect chased but not touched was not seized; the force/intent rule traces to the deadly-force seizure framework of [[Tennessee v. Garner]], with reasonableness governed by [[Graham v. Connor]].

## Appears on
- [[Seizure of the Person]] — *Key — Progeny / Refinement*

## Sources
- *Torres v. Madrid*, 592 U.S. 306 (2021) — https://www.courtlistener.com/opinion/4867542/torres-v-madrid/ — pinpoint: slip op., at 1 (CL carries the slip opinion; cluster 4867542 → opinion 4671321).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59f1c8ba5230b5f7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "592 U.S. 306 (2021)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "141 S. Ct. 989; 209 L. Ed. 2d 190", "title": "Torres v. Madrid", "year": "2021"}}
{"assertion_id": "27961618e9d90f7e", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key — Progeny / Refinement", "title": "Torres v. Madrid"}}
{"assertion_id": "5dcc5254e565ebdd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Physical force applied with intent to restrain is a seizure at the moment of application, even if the person does not submit and is not subdued.", "title": "Torres v. Madrid"}}
{"assertion_id": "5d073f27b766feed", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Torres v. Madrid"}}
{"assertion_id": "89873e8d85e09c58", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-03-25", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Torres v. Madrid", "field_i_validity": "good_law", "scope_note": "Recent SCOTUS holding; good law.", "title": "Torres v. Madrid", "varies_by_point": "false"}}
```

### lake record — Torres v. Madrid

```json
{
  "schema_version": "s2.v1",
  "record_id": "Torres v. Madrid",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Torres v. Madrid",
    "case_name_short": "Torres",
    "case_name_full": "",
    "input_case_name": "Torres v. Madrid",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-03-25",
    "year": 2021,
    "docket": null,
    "cluster_id": 4867542,
    "lead_opinion_id": 4671321,
    "sibling_ids": [
      4671321
    ],
    "absolute_url": "/opinion/4867542/torres-v-madrid/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "592 U.S. 306",
      "volume": "592",
      "reporter": "U.S.",
      "page": "306",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 989",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 190",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "592 U.S. 306",
        "volume": "592",
        "reporter": "U.S.",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 989",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "989",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "209 L. Ed. 2d 190",
        "volume": "209",
        "reporter": "L. Ed. 2d",
        "page": "190",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "592 U.S. 306",
    "official_selection": {
      "court_class": "scotus",
      "selected": "592 U.S. 306",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # Torres v. Madrid *592 U.S. 306 (2021)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Mexico State Police officers approached Torres in an apartment-complex parking lot to execute an arrest warrant for someone else. Torres, who was experiencing methamphetamine withdrawal, got into her car; the officers, believing she was reaching for a weapon, fired thirteen shots, striking her twice in the back. She nonetheless drove away, eluding capture that day, and later sued under \u00a7 1983, claiming the shooting was an unreasonable seizure. ## Issue Whether the application of physical force to a person with intent to restrain is a Fourth Amendment seizure when the force does not succeed in subduing the person and she temporarily eludes capture. ## Rule Yes. Adopting the common-law rule that the slightest application of force to effect an arrest is an arrest, the Court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Torres v. Madrid",
    "varies_by_point": false,
    "scope_note": "Recent SCOTUS holding; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Smith, Jr. v. Melvin Finkley",
          "cluster_id": 4970388,
          "cite": [
            "10 F.4th 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zailey Hess v. Jamie Garcia",
          "cluster_id": 9415232,
          "cite": [
            "72 F.4th 753"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gloria Taylor v. City of Milford",
          "cluster_id": 4982498,
          "cite": [
            "10 F.4th 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Devin Jefferson v. George Lias",
          "cluster_id": 5307076,
          "cite": [
            "21 F.4th 74"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kamel Chaney-Snell v. Andrew Young",
          "cluster_id": 9493618,
          "cite": [
            "98 F.4th 699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Campbell v. Cheatham County Sheriff's Dep't",
          "cluster_id": 7860703,
          "cite": [
            "47 F.4th 468"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany J. Buckley v. Hennepin County",
          "cluster_id": 4957820,
          "cite": [
            "9 F.4th 757"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 9376547,
          "cite": [
            "60 F.4th 596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry Jones, Jr.",
          "cluster_id": 5428746,
          "cite": [
            "22 F.4th 667"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keith Smith v. City of Chicago",
          "cluster_id": 4895377,
          "cite": [
            "3 F.4th 332"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rosa Cuevas v. City of Tulare",
          "cluster_id": 9999054,
          "cite": [
            "107 F.4th 894"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "April Sabbe v. Washington Cnty Bd of Comm'rs",
          "cluster_id": 9433444,
          "cite": [
            "84 F.4th 807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston Seidner v. Jonathan De Vries",
          "cluster_id": 6620483,
          "cite": [
            "39 F.4th 591"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Nieters v. Brandon Holtan",
          "cluster_id": 9431950,
          "cite": [
            "83 F.4th 1099"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vardeman v. City of Houston",
          "cluster_id": 9354006,
          "cite": [
            "55 F.4th 1045"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Huff v. Reeves",
          "cluster_id": 4881659,
          "cite": [
            "996 F.3d 1082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vanessa Dundon v. Kyle Kirchmeier",
          "cluster_id": 9437055,
          "cite": [
            "85 F.4th 1250"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 9328456,
          "cite": [
            "218 N.E.3d 790",
            "171 Ohio St. 3d 412",
            "2022 Ohio 4365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dwayne Furlow v. Jon Belmar",
          "cluster_id": 8436813,
          "cite": [
            "52 F.4th 393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wright",
          "cluster_id": 9368876,
          "cite": [
            "57 F.4th 524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derrick Sanderlin v. Jason Dwyer",
          "cluster_id": 10104398,
          "cite": [
            "116 F.4th 905"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Cloud",
          "cluster_id": 4872727,
          "cite": [
            "994 F.3d 233"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stephen Hopkins v. Anthony Nichols",
          "cluster_id": 6478429,
          "cite": [
            "37 F.4th 1110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Torres v. Madrid:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4671321) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 73,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 73,
        "triage_read": 1,
        "triage_snippet_classified": 72
      },
      "lane2_top_cited": {
        "query": "cites:(4671321)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01JnM9MTAwMDY2NDUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284671321%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4671321)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 0,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4671321)",
    "indexed_citing_opinions": 104,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4671321,
        "count": 104,
        "count_source": "search"
      }
    ],
    "citation_count": 380,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/torres-v-madrid.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NTcxNTQmcz05NDkzNjE4JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284671321%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4671321,
        "cited_id": 85330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 85464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 88142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 88824,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 102310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 112919,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 152652,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4671321,
        "cited_id": 3819289,
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
    "date_created": "2026-07-05T21:47:23Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:52:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:48:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Torres v. Madrid

```
(Slip Opinion)              OCTOBER TERM, 2020                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                      TORRES v. MADRID ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE TENTH CIRCUIT

    No. 19–292.      Argued October 14, 2020—Decided March 25, 2021
Respondents Janice Madrid and Richard Williamson, officers with the
  New Mexico State Police, arrived at an Albuquerque apartment com-
  plex to execute an arrest warrant and approached petitioner Roxanne
  Torres, then standing near a Toyota FJ Cruiser. The officers at-
  tempted to speak with her as she got into the driver’s seat. Believing
  the officers to be carjackers, Torres hit the gas to escape. The officers
  fired their service pistols 13 times to stop Torres, striking her twice.
  Torres managed to escape and drove to a hospital 75 miles away, only
  to be airlifted back to a hospital in Albuquerque, where the police ar-
  rested her the next day. Torres later sought damages from the officers
  under 42 U. S. C. §1983. She claimed that the officers used excessive
  force against her and that the shooting constituted an unreasonable
  seizure under the Fourth Amendment. Affirming the District Court’s
  grant of summary judgment to the officers, the Tenth Circuit held that
  “a suspect’s continued flight after being shot by police negates a Fourth
  Amendment excessive-force claim.” 769 Fed. Appx. 654, 657.
Held: The application of physical force to the body of a person with intent
 to restrain is a seizure even if the person does not submit and is not
 subdued. Pp. 3–18.
    (a) The Fourth Amendment protects “[t]he right of the people to be
 secure in their persons, houses, papers, and effects, against unreason-
 able searches and seizures.” This Court’s precedents have interpreted
 the term “seizure” by consulting the common law of arrest, the “quin-
 tessential” seizure of the person. Payton v. New York, 445 U. S. 573,
 585; California v. Hodari D., 499 U. S. 621, 624. In Hodari D., this
 Court explained that the common law considered the application of
 physical force to the body of a person with the intent to restrain to be
 an arrest—not an attempted arrest—even if the person does not yield.
2                           TORRES v. MADRID

                                   Syllabus

    Id., at 624–625. A review of the pertinent English and American deci-
    sions confirms that the slightest touching was a constructive detention
    that would complete the arrest. See, e.g., Genner v. Sparks, 6 Mod.
    173, 87 Eng. Rep. 928.
       The analysis does not change because the officers used force from a
    distance to restrain Torres. The required “corporal seising or touching
    the defendant’s body,” 3 W. Blackstone, Commentaries on the Laws of
    England 288 (1768), can be as readily accomplished by a bullet as by
    the end of a finger. The focus of the Fourth Amendment is “the privacy
    and security of individuals,” not the particular form of governmental
    intrusion. Camara v. Municipal Court of City and County of San Fran-
    cisco, 387 U. S. 523, 528.
       The application of force, standing alone, does not satisfy the rule
    recognized in this decision. A seizure requires the use of force with
    intent to restrain, as opposed to force applied by accident or for some
    other purpose. County of Sacramento v. Lewis, 523 U. S. 833, 844. The
    appropriate inquiry is whether the challenged conduct objectively
    manifests an intent to restrain. Michigan v. Chesternut, 486 U. S. 567,
    574. This test does not depend on either the subjective motivation of
    the officer or the subjective perception of the suspect. Finally, a sei-
    zure by force lasts only as long as the application of force unless the
    suspect submits. Hodari D., 499 U. S., at 625. Pp. 3–11.
       (b) In place of the rule that the application of force completes an
    arrest, the officers would assess all seizures under one test: intentional
    acquisition of control. This alternative approach finds support in nei-
    ther the history of the Fourth Amendment nor this Court’s precedents.
    Pp. 11–16.
          (1) The officers attempt to recast the common law doctrine recog-
    nized in Hodari D. as a rule applicable only to civil arrests. But the
    common law did not define the arrest of a debtor any differently from
    the arrest of a felon. Treatises and courts discussing criminal arrests
    articulated a rule indistinguishable from the one applied to civil ar-
    rests at common law. Pp. 11–14.
          (2) The officers’ contrary test would limit seizures of a person to
    “an intentional acquisition of physical control.” Brower v. County of
    Inyo, 489 U. S. 593, 596. While that test properly describes seizures
    by control, seizures by force enjoy a separate common law pedigree
    that gives rise to a separate rule. A seizure by acquisition of control
    involves either voluntary submission to a show of authority or the ter-
    mination of freedom of movement. But as common law courts recog-
    nized, any such requirement of control would be difficult to apply to
    seizures by force. The officers’ test will often yield uncertainty about
    whether an officer succeeded in gaining control over a suspect. For
    centuries, the rule recognized in this opinion has avoided such line-
                     Cite as: 592 U. S. ____ (2021)                      3

                                Syllabus

  drawing problems. Pp. 14–16.
     (c) The officers seized Torres by shooting her with the intent to re-
  strain her movement. This Court does not address the reasonableness
  of the seizure, the damages caused by the seizure, or the officers’ enti-
  tlement to qualified immunity. Pp. 17–18.
769 Fed. Appx. 654, vacated and remanded.

  ROBERTS, C. J., delivered the opinion of the Court, in which BREYER,
SOTOMAYOR, KAGAN, and KAVANAUGH, JJ., joined. GORSUCH, J., filed a
dissenting opinion, in which THOMAS and ALITO, JJ., joined. BARRETT, J.,
took no part in the consideration or decision of the case.
                        Cite as: 592 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 19–292
                                    _________________


             ROXANNE TORRES, PETITIONER v.
                 JANICE MADRID, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                                 [March 25, 2021]

  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  The Fourth Amendment prohibits unreasonable “sei-
zures” to safeguard “[t]he right of the people to be secure in
their persons.” Under our cases, an officer seizes a person
when he uses force to apprehend her. The question in this
case is whether a seizure occurs when an officer shoots
someone who temporarily eludes capture after the shooting.
The answer is yes: The application of physical force to the
body of a person with intent to restrain is a seizure, even if
the force does not succeed in subduing the person.
                             I
  At dawn on July 15, 2014, four New Mexico State Police
officers arrived at an apartment complex in Albuquerque to
execute an arrest warrant for a woman accused of white col-
lar crimes, but also “suspected of having been involved in
drug trafficking, murder, and other violent crimes.” App.
to Pet. for Cert. 11a. What happened next is hotly con-
tested. We recount the facts in the light most favorable to
petitioner Roxanne Torres because the court below granted
summary judgment to Officers Janice Madrid and Richard
2                    TORRES v. MADRID

                      Opinion of the Court

Williamson, the two respondents here. Tolan v. Cotton, 572
U. S. 650, 655–656 (2014) (per curiam).
   The officers observed Torres standing with another per-
son near a Toyota FJ Cruiser in the parking lot of the com-
plex. Officer Williamson concluded that neither Torres nor
her companion was the target of the warrant. As the offic-
ers approached the vehicle, the companion departed, and
Torres—at the time experiencing methamphetamine with-
drawal—got into the driver’s seat. The officers attempted
to speak with her, but she did not notice their presence until
one of them tried to open the door of her car.
   Although the officers wore tactical vests marked with po-
lice identification, Torres saw only that they had guns. She
thought the officers were carjackers trying to steal her car,
and she hit the gas to escape them. Neither Officer Madrid
nor Officer Williamson, according to Torres, stood in the
path of the vehicle, but both fired their service pistols to
stop her. All told, the two officers fired 13 shots at Torres,
striking her twice in the back and temporarily paralyzing
her left arm.
   Steering with her right arm, Torres accelerated through
the fusillade of bullets, exited the apartment complex, drove
a short distance, and stopped in a parking lot. After asking
a bystander to report an attempted carjacking, Torres stole
a Kia Soul that happened to be idling nearby and drove 75
miles to Grants, New Mexico. The good news for Torres was
that the hospital in Grants was able to airlift her to another
hospital where she could receive appropriate care. The bad
news was that the hospital was back in Albuquerque, where
the police arrested her the next day. She pleaded no contest
to aggravated fleeing from a law enforcement officer, as-
sault on a peace officer, and unlawfully taking a motor
vehicle.
   Torres later sought damages from Officers Madrid and
Williamson under 42 U. S. C. §1983, which provides a cause
                  Cite as: 592 U. S. ____ (2021)              3

                      Opinion of the Court

of action for the deprivation of constitutional rights by per-
sons acting under color of state law. She claimed that the
officers applied excessive force, making the shooting an un-
reasonable seizure under the Fourth Amendment. The Dis-
trict Court granted summary judgment to the officers, and
the Court of Appeals for the Tenth Circuit affirmed on the
ground that “a suspect’s continued flight after being shot by
police negates a Fourth Amendment excessive-force claim.”
769 Fed. Appx. 654, 657 (2019). The court relied on Circuit
precedent providing that “no seizure can occur unless there
is physical touch or a show of authority,” and that “such
physical touch (or force) must terminate the suspect’s move-
ment” or otherwise give rise to physical control over the sus-
pect. Brooks v. Gaenzle, 614 F. 3d 1213, 1223 (2010).
   We granted certiorari. 589 U. S. ___ (2019).
                               II
   The Fourth Amendment protects “[t]he right of the people
to be secure in their persons, houses, papers, and effects,
against unreasonable searches and seizures.” This case
concerns the “seizure” of a “person,” which can take the
form of “physical force” or a “show of authority” that “in
some way restrain[s] the liberty” of the person. Terry v.
Ohio, 392 U. S. 1, 19, n. 16 (1968). The question before us
is whether the application of physical force is a seizure if
the force, despite hitting its target, fails to stop the person.
   We largely covered this ground in California v. Hodari
D., 499 U. S. 621 (1991). There we interpreted the term
“seizure” by consulting the common law of arrest, the “quin-
tessential ‘seizure of the person’ under our Fourth Amend-
ment jurisprudence.” Id., at 624. As Justice Scalia ex-
plained for himself and six other Members of the Court, the
common law treated “the mere grasping or application of
physical force with lawful authority” as an arrest, “whether
or not it succeeded in subduing the arrestee.” Ibid.; see id.,
at 625 (“merely touching” sufficient to constitute an arrest).
4                     TORRES v. MADRID

                      Opinion of the Court

Put another way, an officer’s application of physical force to
the body of a person “ ‘for the purpose of arresting him’ ” was
itself an arrest—not an attempted arrest—even if the per-
son did not yield. Id., at 624 (quoting Whithead v. Keyes, 85
Mass. 495, 501 (1862)).
   The common law distinguished the application of force
from a show of authority, such as an order for a suspect to
halt. The latter does not become an arrest unless and until
the arrestee complies with the demand. As the Court ex-
plained in Hodari D., “[a]n arrest requires either physical
force . . . or, where that is absent, submission to the asser-
tion of authority.” 499 U. S., at 626 (emphasis in original).
   Hodari D. articulates two pertinent principles. First,
common law arrests are Fourth Amendment seizures. And
second, the common law considered the application of force
to the body of a person with intent to restrain to be an ar-
rest, no matter whether the arrestee escaped. We need not
decide whether Hodari D., which principally concerned a
show of authority, controls the outcome of this case as a
matter of stare decisis, because we independently reach the
same conclusions.
   At the adoption of the Fourth Amendment, a “seizure”
was the “act of taking by warrant” or “of laying hold on sud-
denly”—for example, when an “officer seizes a thief.” 2 N.
Webster, An American Dictionary of the English Language
67 (1828) (Webster) (emphasis deleted). A seizure did not
necessarily result in actual control or detention. It is true
that, when speaking of property, “[f]rom the time of the
founding to the present, the word ‘seizure’ has meant a ‘tak-
ing possession.’ ” Hodari D., 499 U. S., at 624 (quoting 2
Webster 67). But the Framers selected a term—seizure—
broad enough to apply to all the concerns of the Fourth
Amendment: “persons,” as well as “houses, papers, and ef-
fects.” As applied to a person, “[t]he word ‘seizure’ readily
bears the meaning of a laying on of hands or application of
                   Cite as: 592 U. S. ____ (2021)              5

                       Opinion of the Court

physical force to restrain movement, even when it is ulti-
mately unsuccessful.” 499 U. S., at 626. Then, as now, an
ordinary user of the English language could remark: “She
seized the purse-snatcher, but he broke out of her grasp.”
Ibid.
   The “seizure” of a “person” plainly refers to an arrest.
That linkage existed at the founding. Samuel Johnson, for
example, defined an “arrest” as “[a]ny . . . seizure of the per-
son.” 1 A Dictionary of the English Language 108 (4th ed.
1773). And that linkage persists today. As we have repeat-
edly recognized, “the arrest of a person is quintessentially
a seizure.” Payton v. New York, 445 U. S. 573, 585 (1980)
(internal quotation marks omitted); see Hodari D., 499
U. S., at 624.
   Because arrests are seizures of a person, Hodari D.
properly looked to the common law of arrest for “historical
understandings ‘of what was deemed an unreasonable
search and seizure when the Fourth Amendment was
adopted.’ ” Carpenter v. United States, 585 U. S. ___, ___
(2018) (slip op., at 6) (quoting Carroll v. United States, 267
U. S. 132, 149 (1925); alteration omitted). Sometimes the
historical record will not yield a well-settled legal rule. See,
e.g., Atwater v. Lago Vista, 532 U. S. 318, 327–328 (2001);
Payton, 445 U. S., at 593–596. We do not face that problem
here. The cases and commentary speak with virtual una-
nimity on the question before us today.
   The common law rule identified in Hodari D.—that the
application of force gives rise to an arrest, even if the officer
does not secure control over the arrestee—achieved recog-
nition to such an extent that English lawyers could confi-
dently (and accurately) proclaim that “[a]ll the authorities,
from the earliest time to the present, establish that a cor-
poral touch is sufficient to constitute an arrest, even though
the defendant do not submit.” Nicholl v. Darley, 2 Y. & J.
399, 400, 148 Eng. Rep. 974 (Exch. 1828) (citing Hodges v.
Marks, Cro. Jac. 485, 79 Eng. Rep. 414 (K. B. 1615)). The
6                     TORRES v. MADRID

                      Opinion of the Court

slightest application of force could satisfy this rule. In Gen-
ner v. Sparks, 6 Mod. 173, 87 Eng. Rep. 928 (Q. B. 1704),
the defendant did not submit to the authority of an arrest
warrant, but the court explained that the bailiff would have
made an arrest if he “had but touched the defendant even
with the end of his finger.” Ibid., 87 Eng. Rep., at 929. So
too, if a “bailiff caught one by the hand (whom he had a
warrant to arrest) as he held it out of a window,” that alone
would accomplish an arrest. Anonymus, 1 Vent. 306, 86
Eng. Rep. 197 (K. B. 1677). The touching of the person—
frequently called a laying of hands—was enough. See Dun-
scomb v. Smith, Cro. Car. 164, 79 Eng. Rep. 743 (K. B.
1629). Only later did English law grow to recognize arrest
without touching through a submission to a show of author-
ity. See Horner v. Battyn, Bull. N. P. 62 (K. B. 1738), re-
printed in W. Loyd, Cases on Civil Procedure 798 (1916).
Even so, the traditional rule persisted that all an arrest re-
quired was “corporal seising or touching the defendant’s
body.” 3 W. Blackstone, Commentaries on the Laws of Eng-
land 288 (1768) (Blackstone).
   Early American courts adopted this mere-touch rule from
England, just as they embraced other common law princi-
ples of search and seizure. See Wilson v. Arkansas, 514
U. S. 927, 933 (1995). Justice Baldwin, instructing a jury
in his capacity as Circuit Justice, defined an arrest to in-
clude “touching or putting hands upon [the arrestee] in the
execution of process.” United States v. Benner, 24 F. Cas.
1084, 1086–1087 (No. 14,568) (CC ED Pa. 1830). State
courts agreed that “any touching, however slight, is
enough,” Butler v. Washburn, 25 N. H. 251, 258 (1852), pro-
vided the officer made his intent to arrest clear, see Jones
v. Jones, 35 N. C. 448, 448–449 (1852). Courts continued to
hold that an arrest required only the application of force—
not control or custody—through the framing of the Four-
teenth Amendment, which incorporated the protections of
the Fourth Amendment against the States. See Whithead,
                  Cite as: 592 U. S. ____ (2021)            7

                      Opinion of the Court

85 Mass., at 501; Searls v. Viets, 2 Thomp. & C. 224, 226
(N. Y. Sup. Ct. 1873); State v. Dennis, 16 Del. 433, 436–437,
43 A. 261, 262 (1895); see also H. Voorhees, The Law of Ar-
rest in Civil and Criminal Actions §74, p. 44 (1904).
   Stated simply, the cases “abundantly shew that the
slightest touch [was] an arrest in point of law.” Nicholl, 2
Y. & J., at 404, 148 Eng. Rep., at 976. Indeed, it was not
even required that the officer have, at the time of such an
arrest, “the power of keeping the party so arrested under
restraint.” Sandon v. Jervis, El. Bl. & El. 935, 940, 120 Eng.
Rep. 758, 760 (Q. B. 1858). The consequences would be
“pernicious,” an English judge worried, if the question of
control “were perpetually to be submitted to a jury.” Ibid.;
cf. 3 Blackstone 120 (describing how “[t]he least touching of
another’s person” could satisfy the common law definition
of force to commit battery, “for the law cannot draw the line
between different degrees of violence”).
   This case, of course, does not involve “laying hands,”
Sheriff v. Godfrey, 7 Mod. 288, 289, 87 Eng. Rep. 1247 (K. B.
1739), but instead a shooting. Neither the parties nor the
United States as amicus curiae suggests that the officers’
use of bullets to restrain Torres alters the analysis in any
way. And we are aware of no common law authority ad-
dressing an arrest under such circumstances, or indeed any
case involving an application of force from a distance.
   The closest decision seems to be Countess of Rutland’s
Case, 6 Co. Rep. 52b, 77 Eng. Rep. 332 (Star Chamber
1605). In that case, serjeants-at-mace tracked down Isabel
Holcroft, Countess of Rutland, to execute a writ for a judg-
ment of debt. They “shewed her their mace, and touching
her body with it, said to her, we arrest you, madam.” Id.,
at 54a, 77 Eng. Rep., at 336. We think the case is best un-
derstood as an example of an arrest made by touching with
an object, for the serjeants-at-mace announced the arrest at
the time they touched the countess with the mace. See, e.g.,
8                        TORRES v. MADRID

                          Opinion of the Court

Hodges, Cro. Jac., at 485, 79 Eng. Rep., at 414 (similar an-
nouncement upon laying of hands). Maybe the arrest could
be viewed as a submission to a show of authority, because a
mace served not only as a weapon but also as an insignia of
office. See Kelly, The Great Mace, and Other Corporation
Insignia of the Borough of Leicester, 3 Transactions of the
Royal Hist. Soc. 295, 296–301 (1874). But that view is dif-
ficult to reconcile with the fact that English courts did not
recognize arrest by submission to a show of authority until
the following century. See supra, at 6.*
   However one reads Countess of Rutland, we see no basis
for drawing an artificial line between grasping with a hand
and other means of applying physical force to effect an ar-
rest. The dissent (though not the officers) argues that the
common law limited arrests by force to the literal place-
ment of hands on the suspect, because no court published
an opinion discussing a suspect who continued to flee after
being hit with a bullet or some other weapon. See post, at
18–20 (opinion of GORSUCH, J.). This objection calls to mind
the unavailing defense of the person who “persistently de-
nied that he had laid hands upon a priest, for he had only
cudgelled and kicked him.” 2 S. Pufendorf, De Jure Natu-
rae et Gentium 795 (C. Oldfather & W. Oldfather transl.
1934). The required “corporal seising or touching the de-
fendant’s body” can be as readily accomplished by a bullet
as by the end of a finger. 3 Blackstone 288.
   We will not carve out this greater intrusion on personal
security from the mere-touch rule just because founding-

——————
   *The arrest was not Isabel’s first brush with the law or money trou-
bles. A decade earlier, Elizabeth Charlton sued to recover for the estate
of her husband, the fourth Earl of Rutland, an assortment of jewels al-
legedly taken by Isabel, the widow of the third Earl of Rutland. Eliza-
beth bested Isabel in the clash of the countesses, and Isabel was found
liable for 940 pounds, worth about $400,000 today. Elizabeth Countess
of Rutland v. Isabel Countess of Rutland, Cro. Eliz. 377, 78 Eng. Rep. 624
(C. P. 1595).
                  Cite as: 592 U. S. ____ (2021)            9

                      Opinion of the Court

era courts did not confront apprehension by firearm. While
firearms have existed for a millennium and were certainly
familiar at the founding, we have observed that law en-
forcement did not carry handguns until the latter half of the
19th century, at which point “it bec[a]me possible to use
deadly force from a distance as a means of apprehension.”
Tennessee v. Garner, 471 U. S. 1, 14–15 (1985). So it should
come as no surprise that neither we nor the dissent has lo-
cated a common law case in which an officer used a gun to
apprehend a suspect. Cf. post, at 20 (discussing Dickenson
v. Watson, Jones, T. 205, 84 Eng. Rep. 1218, 1218–1219
(K. B. 1682), in which a tax collector accidentally dis-
charged hailshot into a passerby’s eye). But the focus of the
Fourth Amendment is “the privacy and security of individ-
uals,” not the particular manner of “arbitrary invasion[ ] by
governmental officials.” Camara v. Municipal Court of City
and County of San Francisco, 387 U. S. 523, 528 (1967). As
noted, our precedent protects “that degree of privacy
against government that existed when the Fourth Amend-
ment was adopted,” Kyllo v. United States, 533 U. S. 27, 34
(2001)—a protection that extends to “[s]ubtler and more
far-reaching means of invading privacy” adopted only later,
Olmstead v. United States, 277 U. S. 438, 473 (1928)
(Brandeis, J., dissenting). There is nothing subtle about a
bullet, but the Fourth Amendment preserves personal se-
curity with respect to methods of apprehension old and new.
   We stress, however, that the application of the common
law rule does not transform every physical contact between
a government employee and a member of the public into a
Fourth Amendment seizure. A seizure requires the use of
force with intent to restrain. Accidental force will not qual-
ify. See County of Sacramento v. Lewis, 523 U. S. 833, 844
(1998). Nor will force intentionally applied for some other
purpose satisfy this rule. In this opinion, we consider only
force used to apprehend. We do not accept the dissent’s in-
vitation to opine on matters not presented here—pepper
10                   TORRES v. MADRID

                      Opinion of the Court

spray, flash-bang grenades, lasers, and more. Post, at 23.
   Moreover, the appropriate inquiry is whether the chal-
lenged conduct objectively manifests an intent to restrain,
for we rarely probe the subjective motivations of police of-
ficers in the Fourth Amendment context. See Nieves v.
Bartlett, 587 U. S. ___, ___ (2019) (slip op., at 10). Only an
objective test “allows the police to determine in advance
whether the conduct contemplated will implicate the
Fourth Amendment.” Michigan v. Chesternut, 486 U. S.
567, 574 (1988). While a mere touch can be enough for a
seizure, the amount of force remains pertinent in assessing
the objective intent to restrain. A tap on the shoulder to get
one’s attention will rarely exhibit such an intent. See INS
v. Delgado, 466 U. S. 210, 220 (1984); Jones, 35 N. C., at
448–449.
   Nor does the seizure depend on the subjective perceptions
of the seized person. Here, for example, Torres claims to
have perceived the officers’ actions as an attempted carjack-
ing. But the conduct of the officers—ordering Torres to stop
and then shooting to restrain her movement—satisfies the
objective test for a seizure, regardless whether Torres com-
prehended the governmental character of their actions.
   The rule we announce today is narrow. In addition to the
requirement of intent to restrain, a seizure by force—absent
submission—lasts only as long as the application of force.
That is to say that the Fourth Amendment does not recog-
nize any “continuing arrest during the period of fugitivity.”
Hodari D., 499 U. S., at 625. The fleeting nature of some
seizures by force undoubtedly may inform what damages a
civil plaintiff may recover, and what evidence a criminal de-
fendant may exclude from trial. See, e.g., Utah v. Strieff,
579 U. S. ___, ___ (2016) (slip op., at 4). But brief seizures
are seizures all the same.
   Applying these principles to the facts viewed in the light
most favorable to Torres, the officers’ shooting applied
                  Cite as: 592 U. S. ____ (2021)            11

                      Opinion of the Court

physical force to her body and objectively manifested an in-
tent to restrain her from driving away. We therefore con-
clude that the officers seized Torres for the instant that the
bullets struck her.
                               III
   In place of the rule that the application of force completes
an arrest even if the arrestee eludes custody, the officers
would introduce a single test for all types of seizures: inten-
tional acquisition of control. This alternative rule is incon-
sistent with the history of the Fourth Amendment and our
cases.
                              A
   The officers and their amici stress that common law rules
are not automatically “elevated to constitutional proscrip-
tions,” Hodari D., 499 U. S., at 626, n. 2, especially if they
are “distorted almost beyond recognition when literally ap-
plied,” Garner, 471 U. S., at 15. In their view, the common
law doctrine recognized in Hodari D. is just “a narrow legal
rule intended to govern liability in civil cases involving
debtors.” Brief for National Association of Counties et al.
as Amici Curiae 12. The dissent presses the same argu-
ment. See post, at 14–17.
   But the common law did not define the arrest of a debtor
any differently from the arrest of a felon. Whether the ar-
rest was authorized by a criminal indictment or a civil writ,
“there must be a corporal seizing, or touching the defend-
ant’s person; or, what is tantamount, a power of taking im-
mediate possession of the body, and the party’s submission
thereto, and a declaration of the officer that he makes an
arrest.” 1 J. Backus, A Digest of Laws Relating to the Of-
fices and Duties of Sheriff, Coroner and Constable 115–116
(1812). Treatises on the law governing criminal arrests
cited Genner v. Sparks, 6 Mod. 173, 87 Eng. Rep. 928—the
preeminent mere-touch case involving a debtor—for the
12                    TORRES v. MADRID

                      Opinion of the Court

proposition that, “[i]n making the arrest, the constable or
party making it should actually seize or touch the offender’s
body, or otherwise restrain his liberty.” 1 R. Burn, The Jus-
tice of the Peace 275 (28th ed. 1837). When English courts
confronted arrests for criminal offenses, they too relied on
precedents concerning arrests for civil offenses. See
Bridgett v. Coyney, 1 Man. & Ryl. 1, 5–6 (K. B. 1827); Ar-
rowsmith v. Le Mesurier, 2 Bos. & Pul. 211, 211–212, 127
Eng. Rep. 605, 606 (C. P. 1806). American courts likewise
articulated a materially identical definition in criminal
cases—that “[t]he arrest itself is the laying hands on the
defendant,” State v. Townsend, 5 Del. 487, 488 (Ct. Gen.
Sess. 1854), or that an arrest is “the taking, seizing, or de-
taining of the person of another, either by touching him or
putting hands on him,” McAdams v. State, 30 Okla. Crim.
207, 210, 235 P. 241, 242 (1925).
   This uniform definition also explains why an arrest by
mere touch carried legal consequences in both the criminal
and civil contexts. The point of an arrest was of course to
take custody of a person to secure his appearance at a pro-
ceeding. But some arrests did not culminate in actual con-
trol of the individual, let alone a trip to the gaol or compter.
See Nicholl, 2 Y. & J., at 403–404, 148 Eng. Rep., at 975–
976. When an officer let an arrestee get away, the officer
risked becoming a defendant himself in an action for “es-
cape.” See Perkins, The Law of Arrest, 25 Iowa L. Rev. 201,
204 (1940). The laying of hands constituted a taking cus-
tody and would expose the officer to liability for the escape
of felons and debtors alike. See 1 M. Hale, Pleas of the
Crown 590–591, 597, 603 (1736); 2 id., at 93 (no liability for
escape “if the felon were not once in the hands of an officer”);
see also Perkins, 25 Iowa L. Rev., at 206.
   The tort of false imprisonment, which the dissent rightly
acknowledges as the “ ‘closest analogy’ to an arrest without
probable cause,” post, at 12 (quoting Wallace v. Kato, 549
U. S. 384, 388–389 (2007)), reinforces the conclusion that
                  Cite as: 592 U. S. ____ (2021)            13

                      Opinion of the Court

the common law considered touching to be a seizure. Stated
generally, false imprisonment required “confinement,” such
as “taking a person into custody under an asserted legal au-
thority.” Restatement of Torts §§35, 41 (1934); see 3 Black-
stone 127. But that element of confinement demanded no
more than that the defendant “had for one moment taken
possession of the plaintiff ’s person”—including, “for exam-
ple, if he had tapped her on the shoulder, and said, ‘You are
my prisoner.’ ” Simpson v. Hill, 1 Esp. 431, 431–432, 170
Eng. Rep. 409 (N. P. 1795); see Restatement of Torts §41,
Comment h (noting that “the touching alone of the person
against whom [legal authority] was asserted would be suf-
ficient to constitute” confinement by arrest when the au-
thority was valid). While the dissent emphasizes that “the
court [in Simpson] proceeded to reject the plaintiff ’s claim
for false imprisonment,” post, at 13, that was only because
“the constable never touched the plaintiff, or took her into
custody.” 1 Esp., at 431, 170 Eng. Rep., at 409.
   To be sure, the mere-touch rule was particularly well doc-
umented in cases involving the execution of civil process.
An officer pursuing a debtor could not forcibly enter the
debtor’s home unless the debtor had escaped arrest, such as
by fleeing after being touched. See Semayne’s Case, 5 Co.
Rep. 91a, 91b, 77 Eng. Rep. 194, 196 (K. B. 1604); see also
Miller v. United States, 357 U. S. 301, 307 (1958). Officers
seeking to execute criminal process, on the other hand, pos-
sessed greater pre-arrest authority to enter a felon’s home.
See Payton, 445 U. S., at 598. But the fact that the common
law rules of arrest generated more litigation in the civil con-
text proves only that creditors had ready recourse to the
courts to pursue escape actions for unsatisfactory arrests.
There is no reason to suspect that English jurists silently
adopted a special definition of arrest only for debt collec-
tion—indeed, they told us just the opposite. See supra, at
12. Nothing specific to debt collection elevated escape from
arrest into a justification for entry of the home. Whenever
14                    TORRES v. MADRID

                      Opinion of the Court

a person was “lawfully arrested for any Cause and after-
wards escape[d], and shelter[ed] himself in a House,” the
officer could break open the doors of the house. 2 W. Haw-
kins, Pleas of the Crown 87 (1721) (emphasis added).
   In any event, the officers and the dissent misapprehend
the history of the Fourth Amendment by minimizing the
role of practices in civil cases. “[A]rrests in civil suits were
still common in America” at the founding. Long v. Ansell,
293 U. S. 76, 83 (1934). And questions regarding the legal-
ity of an arrest “typically arose in civil damages actions for
trespass or false arrest.” Payton, 445 U. S., at 592. Accord-
ingly, this Court has not hesitated to rely on such decisions
when interpreting the Fourth Amendment. See, e.g.,
United States v. Jones, 565 U. S. 400, 404–405 (2012); Boyd
v. United States, 116 U. S. 616, 626 (1886). We see no rea-
son to break with our settled approach in this case.
                               B
   The officers and the dissent derive from our cases a dif-
ferent touchstone for the seizure of a person: “an intentional
acquisition of physical control.” Brower v. County of Inyo,
489 U. S. 593, 596 (1989). Under their alternative rule, the
use of force becomes a seizure “only when there is a govern-
mental termination of freedom of movement through means
intentionally applied.” Id., at 597 (emphasis deleted); see
Brief for Respondents 12–15; post, at 6–7.
   This approach improperly erases the distinction between
seizures by control and seizures by force. In all fairness, we
too have not always been attentive to this distinction when
a case did not implicate the issue. See, e.g., Brendlin v. Cal-
ifornia, 551 U. S. 249, 254 (2007). But each type of seizure
enjoys a separate common law pedigree that gives rise to a
separate rule. See Hodari D., 499 U. S., at 624–625; A. Cor-
nelius, The Law of Search and Seizure §47, pp. 163–164 (2d
ed. 1930) (contrasting actual control with “constructive de-
tention” by touching).
                   Cite as: 592 U. S. ____ (2021)             15

                       Opinion of the Court

    Unlike a seizure by force, a seizure by acquisition of con-
trol involves either voluntary submission to a show of au-
thority or the termination of freedom of movement. A prime
example of the latter comes from Brower, where the police
seized a driver when he crashed into their roadblock. 489
U. S., at 598–599; see also, e.g., Scott v. Harris, 550 U. S.
372, 385 (2007) (ramming car off road); Williams v. Jones,
Cas. t. Hard. 299, 301, 95 Eng. Rep. 193, 194 (K. B. 1736)
(locking person in room). Under the common law rules of
arrest, actual control is a necessary element for this type of
seizure. See Wilgus, Arrest Without a Warrant, 22 Mich.
L. Rev. 541, 553 (1924). Such a seizure requires that “a per-
son be stopped by the very instrumentality set in motion or
put in place in order to achieve that result.” Brower, 489
U. S., at 599. But that requirement of control or submission
never extended to seizures by force. See, e.g., Sandon, El.
Bl. & El., at 940–941, 120 Eng. Rep., at 760.
    As common law courts recognized, any such requirement
of control would be difficult to apply in cases involving the
application of force. See supra, at 7. At the most basic level,
it will often be unclear when an officer succeeds in gaining
control over a struggling suspect. Courts will puzzle over
whether an officer exercises control when he grabs a sus-
pect, when he tackles him, or only when he slaps on the
cuffs. Neither the officers nor the dissent explains how long
the control must be maintained—only for a moment, into
the squad car, or all the way to the station house. To cite
another example, counsel for the officers speculated that
the shooting would have been a seizure if Torres stopped
“maybe 50 feet” or “half a block” from the scene of the shoot-
ing to allow the officers to promptly acquire control. Tr. of
Oral Arg. 45. None of this squares with our recognition that
“ ‘[a] seizure is a single act, and not a continuous fact.’ ” Ho-
dari D., 499 U. S., at 625 (quoting Thompson v. Whitman,
18 Wall. 457, 471 (1874)). For centuries, the common law
16                   TORRES v. MADRID

                      Opinion of the Court

rule has avoided such line-drawing problems by clearly fix-
ing the moment of the seizure.
                               IV
   The dissent sees things differently. It insists that the
term “seizure” has always entailed a taking of possession,
whether the officer is seizing a person, a ship, or a promis-
sory note. See post, at 6–7. But the facts of the cases and
the language of the opinions confirm that the concept of pos-
session included the “constructive detention” of persons
“never actually brought within the physical control of the
party making an arrest.” Wilgus, 22 Mich. L. Rev., at 556
(emphasis deleted); see, e.g., Nicholl, 2 Y. & J., at 404, 148
Eng. Rep., at 976 (explaining that the “slightest touch” can
constitute “custody”); Anonymus, 1 Vent., at 306, 86 Eng.
Rep., at 197 (describing a touch as a “taking” of a person).
Even the dissent acknowledges that a touch can establish a
form of constructive possession. See post, at 20.
   The dissent says that “common law courts never contem-
plated” that the touching itself could effect a seizure. Post,
at 18. But one need only look at the many decisions adopt-
ing that definition of arrest. See supra, at 5–8, 12–13. The
dissent can offer no case expressing doubt about the rule
that the touching constitutes an arrest, much less refusing
to apply that rule in any context—felon or debtor. And we
have, as noted, definitively stated that “the arrest of a per-
son is quintessentially a seizure.” Payton, 445 U. S., at 585
(internal quotation marks omitted). The dissent’s attempt
to ignore arrests it appraises as “unfortunate” or “peculiar,”
post, at 15, 16, pays insufficient regard to the complete his-
tory underlying the Fourth Amendment.
   The dissent argues that we advance a “schizophrenic
reading of the word ‘seizure.’ ” Post, at 7. But our cases
demonstrate the unremarkable proposition that the nature
of a seizure can depend on the nature of the object being
seized. It is not surprising that the concept of constructive
                  Cite as: 592 U. S. ____ (2021)             17

                      Opinion of the Court

detention or the mere-touch rule developed in the context
of seizures of a person—capable of fleeing and with an in-
terest in doing so—rather than seizures of “houses, papers,
and effects.”
   The dissent also criticizes us for “posit[ing] penumbras”
of “privacy” and “personal security” in our analysis of the
Fourth Amendment. Post, at 24. But the text of the Fourth
Amendment expressly guarantees the “right of the people
to be secure in their persons,” and our earliest precedents
recognized privacy as the “essence” of the Amendment—not
some penumbral emanation. Boyd, 116 U. S., at 630. We
have relied on that understanding in construing the mean-
ing of the Amendment. See, e.g., Riley v. California, 573
U. S. 373, 403 (2014).
   The dissent speculates that the real reason for today’s de-
cision is an “impulse” to provide relief to Torres, post, at 23,
or maybe a desire “to make life easier for ourselves,” post,
at 22. It may even be, says the dissent, that the Court “at
least hopes to be seen as trying” to achieve particular goals.
Post, at 25. There is no call for such surmise. At the end of
the day we simply agree with the analysis of the common
law of arrest and its relation to the Fourth Amendment set
forth thirty years ago by Justice Scalia, joined by six of his
colleagues, rather than the competing view urged by the
dissent today.
                         *    *     *
  We hold that the application of physical force to the body
of a person with intent to restrain is a seizure even if the
person does not submit and is not subdued. Of course, a
seizure is just the first step in the analysis. The Fourth
Amendment does not forbid all or even most seizures—only
unreasonable ones. All we decide today is that the officers
seized Torres by shooting her with intent to restrain her
movement. We leave open on remand any questions re-
garding the reasonableness of the seizure, the damages
18                    TORRES v. MADRID

                      Opinion of the Court

caused by the seizure, and the officers’ entitlement to qual-
ified immunity.
   The judgment of the Court of Appeals is vacated, and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.

   JUSTICE BARRETT took no part in the consideration or de-
cision of this case.
                  Cite as: 592 U. S. ____ (2021)            1

                     GORSUCH, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 19–292
                          _________________


          ROXANNE TORRES, PETITIONER v.
              JANICE MADRID, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE TENTH CIRCUIT
                        [March 25, 2021]

   JUSTICE GORSUCH, with whom JUSTICE THOMAS and
JUSTICE ALITO join, dissenting.
   The majority holds that a criminal suspect can be simul-
taneously seized and roaming at large. On the majority’s
account, a Fourth Amendment “seizure” takes place when-
ever an officer “merely touches” a suspect. It’s a seizure
even if the suspect refuses to stop, evades capture, and rides
off into the sunset never to be seen again. That view is as
mistaken as it is novel.
   Until today, a Fourth Amendment “seizure” has required
taking possession of someone or something. To reach its
contrary judgment, the majority must conflate a seizure
with its attempt and confuse an arrest with a battery. In
the process, too, the majority must disregard the Constitu-
tion’s original and ordinary meaning, dispense with our
conventional interpretive rules, and bypass the main cur-
rents of the common law. Unable to rely on any of these
traditional sources of authority, the majority is left to lean
on (really, repurpose) an abusive and long-abandoned Eng-
lish debt-collection practice. But there is a reason why, in
two centuries filled with litigation over the Fourth Amend-
ment’s meaning, this Court has never before adopted the
majority’s definition of a “seizure.” Neither the Constitu-
tion nor common sense can sustain it.
2                    TORRES v. MADRID

                    GORSUCH, J., dissenting

                              I
                              A
   This case began when two Albuquerque police officers ap-
proached Roxanne Torres on foot. The officers thought
Ms. Torres was the subject of an arrest warrant and sus-
pected of involvement in murder and drug trafficking. As
it turned out, they had the wrong person; Ms. Torres was
the subject of a different arrest warrant. As she saw the
officers walk toward her, Ms. Torres responded by getting
into her car and hitting the gas. At the time, Ms. Torres
admits, she was “tripping out bad” on methamphetamine.
Fearing the oncoming car was about to hit them, the officers
fired their duty weapons, and two bullets struck Ms. Torres
while others hit her car.
   None of that stopped Ms. Torres. She continued driv-
ing—over a curb, across some landscaping, and into a
street, eventually colliding with another vehicle. Abandon-
ing her car, she promptly stole a different one parked
nearby. Ms. Torres then drove over 75 miles to another city.
When she eventually sought medical treatment, doctors de-
cided she needed to be airlifted back to Albuquerque for
more intensive care. Only at that point, a day after her en-
counter with the officers, was Ms. Torres finally identified
and arrested. Ultimately, she pleaded no contest to assault
on a police officer, aggravated fleeing from an officer, and
the unlawful taking of a motor vehicle.
   More than two years later, Ms. Torres sued the officers
for damages in federal court under 42 U. S. C. §1983. She
alleged that they had violated the Fourth Amendment by
unreasonably “seizing” her. After discovery, the officers
moved for summary judgment. The district court granted
the motion, and the court of appeals affirmed. Individuals
like Ms. Torres are free to sue officers under New Mexico
state law for assault or battery. They may also sue officers
under the Fourteenth Amendment for conduct that “shocks
the conscience.” But under longstanding circuit precedent,
                   Cite as: 592 U. S. ____ (2021)              3

                      GORSUCH, J., dissenting

the courts explained, a Fourth Amendment “seizure” occurs
only when the government obtains “physical control” over a
person or object. Because Ms. Torres “managed to elude the
police for at least a full day after being shot,” the courts rea-
soned, the officers’ bullets had not “seized” her; any seizure
took place only when she was finally arrested back in Albu-
querque the following day. Torres v. Madrid, 769 Fed.
Appx. 654, 657 (CA10 2019).
                               B
   Now before us, Ms. Torres argues that this Court’s deci-
sion in California v. Hodari D., 499 U. S. 621 (1991), “com-
pel[s] reversal.” Brief for Petitioner 25. As she reads it,
Hodari D. held that a Fourth Amendment seizure takes
place whenever an officer shoots or even “mere[ly]
touch[es]” an individual with the intent to restrain. Brief
for Petitioner 15.
   Whatever one thinks of Ms. Torres’s argument, one thing
is certain: Hodari D. has generated considerable confusion.
There, officers chased a suspect on foot. 499 U. S., at 623.
Later, the suspect argued that he was “seized” for purposes
of the Fourth Amendment the moment the chase began.
See id., at 625. Though he fled, the suspect argued, a “rea-
sonable person” would not have felt at liberty given the of-
ficers’ “show of authority,” so a Fourth Amendment seizure
had occurred. Id., at 627–628.
   The Court rejected this argument. In doing so, it ex-
plained that, “[f]rom the time of the founding to the present,
the word ‘seizure’ has meant a ‘taking possession.’ ” Id., at
624. Because the defendant did not submit to the officers’
show of authority, the Court reasoned, the officers’ conduct
amounted at most to an attempted seizure. See id., at 626,
and n. 2. And “neither usage nor common-law tradition
makes an attempted seizure a seizure.” Ibid.
   At the same time, and as Ms. Torres emphasizes, the
4                     TORRES v. MADRID

                     GORSUCH, J., dissenting

Court didn’t end its discussion there. It proceeded to imag-
ine a different and hypothetical case, one in which the offic-
ers not only chased the suspect but also “appl[ied] physical
force” to him. In these circumstances, the Court suggested,
“merely touching” a suspect, even when officers fail to gain
possession, might qualify as a seizure. Id., at 624–625.
   Unsurprisingly, these dueling passages in Hodari D. led
to a circuit split. For the first time, some lower courts began
holding that a “mere touch” constitutes a Fourth Amend-
ment “seizure.” Others, however, continued to adhere to
the view, taken “[f]rom the time of the founding to the pre-
sent,” that the word “seizure” means “taking possession.”
Id., at 624 (internal quotation marks omitted). We took this
case to sort out the confusion.
                               II
   As an initial matter, Ms. Torres is mistaken that Hodari
D.’s discussion of “mere touch” seizures compels a ruling in
her favor. Under the doctrine of stare decisis, we normally
afford prior holdings of this Court considerable respect.
But, in the course of issuing their holdings, judges some-
times include a “witty opening paragraph, the background
information on how the law developed,” or “digressions
speculating on how similar hypothetical cases might be re-
solved.” B. Garner et al., The Law of Judicial Precedent 44
(2016). Such asides are dicta. The label is hardly an epi-
thet: “Dicta may afford litigants the benefit of a fuller un-
derstanding of the court’s decisional path or related areas
of concern.” Id., at 65. Dicta can also “be a source of advice
to successors.” Ibid. But whatever utility it may have, dicta
cannot bind future courts.
   This ancient rule serves important purposes. A passage
unnecessary to the outcome may not be fully considered.
Parties with little at stake in a hypothetical question may
afford it little or no adversarial testing. And, of course, fed-
eral courts possess no authority to issue rulings beyond the
                  Cite as: 592 U. S. ____ (2021)              5

                     GORSUCH, J., dissenting

cases and controversies before them. If the respect we af-
ford past holdings under the doctrine of stare decisis may
be justified in part as an act of judicial humility, respecting
that doctrine’s limits must be too. Fewer things could be
less humble than insisting our every passing surmise con-
stitutes a rule forever binding a Nation of over 300 million
people. No judge can see around every corner, predict the
future, or fairly resolve matters not at issue. See, e.g., Co-
hens v. Virginia, 6 Wheat. 264, 399–400 (1821); Central Va.
Community College v. Katz, 546 U. S. 356, 363 (2006).
   On any account, the passage in Hodari D. Ms. Torres
seeks to invoke was dicta. The only question presented in
that case was whether officers seize a defendant by a show
of authority without touching him. The Court answered
that question in the negative. The separate question
whether a “mere touch” also qualifies as a seizure was not
presented by facts of the case. No party briefed the issue.
And the opinion offered the matter only shallow considera-
tion, resting on just three sources: A state court opinion
from the 1860s, a “comment” in the 1934 Restatement of
Torts, and a 1930s legal treatise. See 499 U. S., at 624–625.
   Already some lower courts, including those below, have
recognized that Hodari D.’s aside does not constitute a
binding holding. See Brooks v. Gaenzle, 614 F. 3d 1213,
1220–1221 (CA10 2010); Henson v. United States, 55 A. 3d
859, 864–865 (D. C. 2012). Today’s majority seems to ac-
cept the point too. It acknowledges that Hodari D. “princi-
pally concerned a show of authority.” Ante, at 4. And it
says it intends to rule for Ms. Torres “independently” of Ho-
dari D. Ante, at 4.
                                III
  Seeking to carry that burden, the majority picks up where
Hodari D.’s dicta left off. It contends that an officer “seizes”
a person by merely touching him with an “intent to re-
strain.” Ante, at 9. We are told that a touch is a seizure
6                           TORRES v. MADRID

                          GORSUCH, J., dissenting

even if the suspect never stops or slows down; it’s a seizure
even if he evades capture. In all the years before Hodari
D.’s dicta, this conclusion would have sounded more than a
little improbable to most lawyers and judges—as it should
still today. A mere touch may be a battery. It may even be
part of an attempted seizure. But the Fourth Amendment’s
text, its history, and our precedent all confirm that “seizing”
something doesn’t mean touching it; it means taking pos-
session.
                              A
    Start with the text. The Fourth Amendment guarantees
that “[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated.” As at least part of Ho-
dari D. recognized, “[f ]rom the time of the founding to the
present,” the key term here—“seizure”—has always meant
“ ‘taking possession.’ ” 499 U. S., at 624.
    Countless contemporary dictionaries define a “seizure” or
the act of “seizing” in terms of possession.1 This Court’s
early cases reflect the same understanding. Just sixteen
——————
   1 N. Bailey, Universal Etymological English Dictionary (22 ed. 1770)

(To seize is “to take into Custody or Possession by Force, or wrongfully;
to distrain, to attack, to lay hold of, or catch”; a seizure is a “seizing, tak-
ing into Custody”); T. Dyche & W. Pardon, A New General English Dic-
tionary (14th ed. 1771) (To seize is “to lay or take hold of violently or at
unawares, wrongfully, or by force”; a seizing or seizure is “a taking pos-
session of any thing by violent, force, &c”); 2 S. Johnson, A Dictionary of
the English Language (6th ed. 1785) (To seize is “1. To take hold of; to
gripe; to grasp.” “2. To take possession of by force.” “3. To take possession
of; to lay hold on; to invade suddenly.” “4. To take forcible possession of
by law.” “5. To make possessed; to put in possession of.” A seizure is “1.
The act of seizing.” “2. The thing seized.” “3. The act of taking forcible
possession.” “4. Gripe; possession.” “5. Catch”); 2 J. Ash, The New and
Complete Dictionary of the English Language (2d ed. 1795) (To seize is
“[t]o grasp, to lay hold on, to fasten on, to take possession of, to take pos-
session by law”; a seizure is “[t]he act of seizing, a gripe, a catch; the act
of taking possession by force of law; the thing seized, the thing pos-
sessed”).
                  Cite as: 592 U. S. ____ (2021)             7

                     GORSUCH, J., dissenting

years after the Fourth Amendment’s adoption, Congress
passed a statute regulating the “seizure” of ships. See The
Josefa Segunda, 10 Wheat. 312, 322 (1825). This Court in-
terpreted the term to require “an open, visible possession
claimed,” so that those previously possessing the ship “un-
derstand that they are dispossessed, and that they are no
longer at liberty to exercise any dominion on board of the
ship.” Id., at 325. Nor did the Court’s view change over
time. In Pelham v. Rose, 9 Wall. 103, 106 (1870), the Court
likewise explained that “[t]o effect [a] seizure” of something,
one needed “to take” the thing “into his actual custody and
control.” Id., at 107.
   Today’s majority disputes none of this. It accepts that a
seizure of the inanimate objects mentioned in the Fourth
Amendment (houses, papers, and effects) requires posses-
sion. Ante, at 4. And when it comes to persons, the majority
agrees (as Hodari D. held) that a seizure in response to a
“show of authority” takes place if and when the suspect sub-
mits to an officer’s possession. Ante, at 15. The majority
insists that a different rule should apply only in cases
where an officer “touches” the suspect. Here—and here
alone—possession is not required. So, under the majority’s
logic, we are quite literally asked to believe the officers in
this case “seized” Ms. Torres’s person, but not her car, when
they shot both and both continued speeding down the
highway.
   The majority’s need to resort to such a schizophrenic
reading of the word “seizure” should be a signal that some-
thing has gone seriously wrong. The Fourth Amendment’s
Search and Seizure Clause uses the word “seizures” once in
connection with four objects (persons, houses, papers, and
effects). The text thus suggests parity, not disparity, in
meaning. It is close to canon that when a provision uses the
same word multiple times, courts must give it the same
meaning each time. Ratzlaf v. United States, 510 U. S. 135,
143 (1994). And it is canonical that courts cannot give a
8                    TORRES v. MADRID

                    GORSUCH, J., dissenting

single word different meanings depending on the happen-
stance of “which object it is modifying.” Reno v. Bossier Par-
ish School Bd., 528 U. S. 320, 329 (2000) (“[W]e refuse to
adopt a construction that would attribute different mean-
ings to the same phrase in the same sentence, depending on
which object it is modifying”). To “[a]scrib[e] various mean-
ings” to a single word, we have observed, is to “render mean-
ing so malleable” that written laws risk “becom[ing] suscep-
tible to individuated interpretation.” Ratzlaf, 510 U. S., at
143 (internal quotation marks omitted). The majority’s con-
clusion that a single use of the word “seizures” bears two
different meanings at the same time—indeed, in this very
case—is truly novel. And when it comes to construing the
Constitution, that kind of innovation is no virtue.
   If more textual evidence were needed, the Fourth Amend-
ment’s neighboring Warrant Clause would seem to provide
it. That Clause states that warrants must describe “the
persons or things to be seized.” Once more, the Amendment
uses the same verb—“seized”—for both persons and objects.
Once more, it suggests parity, not some hidden divergence
between people and their possessions. Nor does anyone dis-
pute that a warrant for the “seizure” of a person means a
warrant authorizing officers to take that person into their
possession.
   Against all these adverse textual clues, the majority of-
fers little in reply. It admits that its interpretation defies
this Court’s teachings in Ratzlaf and Reno by ascribing dif-
ferent meanings to the word “seizure” depending on “the ob-
ject being seized.” Ante, at 16. It says only that we should
overlook the problem because “our cases” in the Fourth
Amendment context compel this remarkable construction.
Ibid. But it is unclear what cases the majority might have
in mind for it cites none.
   Instead, the majority proceeds to reason that the word
“seizure” must carry a different meaning for persons and
objects because persons alone are “capable of fleeing” and
                      Cite as: 592 U. S. ____ (2021)                      9

                         GORSUCH, J., dissenting

have “an interest in doing so.” Ibid. But that reasoning
faces trouble even from Hodari D., which explained that “[a]
ship still fleeing, even though under attack, would not be
considered to have been seized as a war prize.” 499 U. S.,
at 624. Of course, as the majority observes, persons alone
can possess “an interest” in fleeing. But, as Hodari D.’s ex-
ample shows, they can have as much (or more) interest in
fleeing to prevent the seizure of their possessions as they do
their persons. Even today, a suspect driving a car loaded
with illegal drugs may be more interested in fleeing to avoid
the loss of her valuable cargo than to prevent her own de-
tention. Yet the majority offers no reasoned explanation
why the meaning of the word “seizure” changes when offic-
ers hit the suspect and when they hit her drugs and car as
all three speed away.
   Unable to muster any precedent or sound reason for its
reading, the majority finishes its textual analysis with a se-
lective snippet from Webster’s Dictionary and a hypothet-
ical about a purse snatching. The majority notes that Web-
ster equated a seizure with “ ‘the act of taking by warrant’ ”
or “ ‘laying hold on suddenly.’ ” Ante, at 4. But Webster used
the warrant definition to describe “the seizure of contra-
band goods”—a seizure the majority agrees requires posses-
sion. Meanwhile, the phrase “laying hold on” a person con-
notes physical possession, as a look at the dictionary’s
entire definition demonstrates. A “seizure,” Webster con-
tinued, is the “act of taking possession by force,” the “act of
taking by warrant,” “possession,” and “a catching.”2 Read
——————
  2 2 N. Webster, An American Dictionary of the English Language 67

(1828) (To seize is “1. To fall or rush upon suddenly and lay hold on; or
to gripe or grasp suddenly.” “2. To take possession by force, with or with-
out right.” “3. To invade suddenly; to take hold of; to come upon suddenly;
as, a fever seizes a patient.” “4. To take possession by virtue of a warrant
or legal authority.” To be seized is to be “[s]uddenly caught or grasped;
taken by force; invaded suddenly; taken possession of; fastened with a
cord; having possession.” A seizure is “1. The act of seizing; the act of
laying hold on suddenly; as the seizure of a thief. 2. The act of taking
10                        TORRES v. MADRID

                         GORSUCH, J., dissenting

in full, Webster thus lends no support to the majority’s
view.
   The purse hypothetical, borrowed from Hodari D.’s dicta,
turns out to be even less illuminating. It supposes that “an
ordinary user of the English language could remark: ‘She
seized the purse-snatcher, but he broke out of her grasp.’ ”
Ante, at 5 (quoting Hodari D., 499 U. S., at 626). But what
does that prove? The hypothetical contemplates a woman
who takes possession of the purse-snatcher, establishing a
“grasp” for him to “break out of.” One doesn’t “break out of ”
a mere touch.
   Really, the majority’s answer to the Constitution’s text is
to ignore it. The majority stands mute before the consensus
among founding-era dictionaries, this Court’s early cases
interpreting the word “seizure,” and the Warrant Clause.
It admits its interpretation spurns the canonical interpre-
tive principle that a single word in a legal text does not
change its meaning depending on what object it modifies.
All we’re offered is a curated snippet and an unhelpful hy-
pothetical. Ultimately, it’s hard not to wonder whether the
majority says so little about the Constitution’s terms be-
cause so little can be said that might support its ruling.
                             B
  Rather than focus on text, the majority turns quickly to
history. At common law, it insists, a “linkage” existed be-
tween the “seizure” of a person and the concept of an “ar-
rest.” Ante, at 5. Thus, the majority contends, we must
examine how the common law defined that term. But fol-
lowing the majority down this path only leads to another
dead end. Unsurprisingly, an “arrest” at common law ordi-
narily required possession too.
——————
possession by force; as the seizure of lands or goods; the seizure of a town
by an enemy; the seizure of a throne by an usurper. 3. The act of taking
by warrant; as the seizure of contraband goods. 4. The thing taken or
seized.” “5. Gripe; grasp; possession.” “6. Catch; a catching”).
                      Cite as: 592 U. S. ____ (2021)                       11

                          GORSUCH, J., dissenting

                              1
  Consider what some of our usual common law guides say
on the subject. Blackstone defined “an arrest” in the crim-
inal context as “the apprehending or restraining of one’s
person, in order to be forthcoming to answer an alleged or
suspected crime.” 4 Commentaries on the Laws of England
286 (1769). Hale and Hawkins both equated an “arrest”
with “apprehending,” “taking,” and “detain[ing]” a person.
See 1 M. Hale, Pleas of the Crown 89, 93–94 (5th ed. 1716);
2 W. Hawkins, Pleas of the Crown 74–75, 77, 80–81, 86 (3d
ed. 1739). And Hawkins stated that an arrest required the
officer to “actually have” the suspect “in his Custody.” Id.,
at 129. Any number of historical dictionaries attest to a
similar understanding—defining an “arrest” as a “stop,” a
“taking of a person,” and the act “by which a man becomes
a prisoner.”3
  Common law causes of action point to the same common-
sense conclusion. During the founding era, an individual
who was unlawfully arrested could seek redress through
the tort of false imprisonment. See 3 W. Blackstone, Com-
mentaries on the Laws of England 127 (1768); see also Pay-
ton v. New York, 445 U. S. 573, 592 (1980); Wallace v. Kato,

——————
   3 See, e.g., Bailey, Universal Etymological English Dictionary (To ar-

rest is “to stop or stay”; an arrest (in the legal sense) is “a Legal taking
of a Person, and restraining him from Liberty”); Dyche & Pardon, A New
General English Dictionary (An arrest is “the stopping or detaining a
person, by a legal process”); 1 Johnson, A Dictionary of the English Lan-
guage (“1. In law. A stop or stay; as, a man apprehended for debt, is said
to be arrested.” “An arrest is a certain restraint of a man’s person, de-
priving him of his own will, and binding it to become obedient to the will
of the law, and may be called the beginning of imprisonment.” “2. Any
caption, seizure of the person.” “3. A stop” (emphasis deleted)); 1 Ash,
The New and Complete Dictionary of the English Language (To arrest is
“[t]o seize a man for debt, to apprehend by virtue of a writ from any court
of justice, to stop, to hinder”; an arrest is “[t]he act of seizing on a man’s
person for debt, the execution of a writ from any court of justice by which
a man becomes a prisoner, a stop, a hindrance”).
12                    TORRES v. MADRID

                     GORSUCH, J., dissenting

549 U. S. 384, 388–389 (2007) (describing “false arrest and
false imprisonment” as the “closest analogy” to an arrest
without probable cause). That cause of action aimed to rem-
edy “the violation of the right of personal liberty,” 3 Black-
stone, supra, at 127, which was “the power of loco-motion,
of changing situation, or removing one’s person to whatso-
ever place one’s own inclination may direct,” 1 W. Black-
stone, Commentaries on the Laws of England 130 (1765).
Thus, false imprisonment—the violation of the right to
move where one desired—required proof of “[t]he detention
of the person” and “[t]he unlawfulness of such detention.” 3
Blackstone, supra, at 127. That detention could occur “in a
gaol, house, stocks, or in the street,” but it occurred only if
a person was “under the custody of another.” 1 E. East,
Pleas of the Crown 428 (1806) (emphasis added).
   Much the same held true in another related field. At com-
mon law, an officer could be held criminally liable for allow-
ing an individual to escape after being arrested. And to
prove the existence of an arrest in an “Indictment for an
Escape,” a prosecutor had to “expressly shew” that “the
Party was actually in the Defendant’s Custody for a Crime,
Action, or Commitment for it.” 2 Hawkins, supra, at 132
(emphasis added). In other words, to demonstrate an ar-
rest, a prosecutor had to prove the suspect had been “a Pris-
oner in [the officer’s] Custody.” 1 Hale, supra, at 112 (em-
phasis added). Here, too, an arrest required possession.
   Once more, the majority’s primary answer to all this
countervailing evidence is to ignore it. And once more, the
majority’s own sources do more to hurt than help its cause.
Lifting a line from Simpson v. Hill, 1 Esp. 431, 170 Eng.
Rep. 409 (N. P. 1795), the majority suggests that the tort of
false imprisonment at common law required no more than
a “tapping on the shoulder.” Ante, at 13 (citing 1 Esp., at
431–432, 170 Eng. Rep., at 409). But Simpson could not
have stated the possession requirement more plainly:
“[W]ithout any taking possession of the person,” there “is
                  Cite as: 592 U. S. ____ (2021)             13

                     GORSUCH, J., dissenting

not, by law, a false imprisonment.” Id., at 432, 170 Eng.
Rep., at 409 (emphasis added). And the court proceeded to
reject the plaintiff ’s claim for false imprisonment because
the “constable did never take her into custody.” Ibid. (em-
phasis added). The majority offers no case finding the ele-
ments of false imprisonment satisfied by the mere touch of
a fleeing person.
   What remains of the majority’s response follows the same
course. The majority asserts that claims for escape only re-
quired proof that the officer touched a suspect. Ante, at 12.
But to prove its point, the majority quotes a sentence from
Hale stating that no liability for escape exists “ ‘if the felon
were not once in the hands of an officer.’ ” Ibid. (quoting 2
Pleas of the Crown 93 (1736)). And as Hale proceeded to
make plain, a felon “in the hands of an officer” was another
way of saying the officer had “apprehended” or “taken” the
felon into his “custody.” See id., at 89, 93–94 (5th ed. 1716).
   Ultimately, the majority seeks to invoke Samuel John-
son’s dictionary and Payton, 445 U. S., at 585, to confirm
only the anodyne point that some sort of “linkage” existed
at common law between the concepts of “arrests” and “sei-
zures.” Ante, at 5. Yet, even here it turns out there is more
to the story. The majority neglects to mention that Johnson
proceeded to define an “arrest” as a “caption” of the person,
“a stop or stay,” a “restraint of a man’s person, depriving
him of his own will,” and “the beginning of imprisonment.”
1 S. Johnson, A Dictionary of the English Language (6th ed.
1785). “To arrest,” Johnson said, was “[t]o seize,” “to detain
by power,” “[t]o withhold; to hinder,” and “[t]o stop motion.”
Ibid. Meanwhile, the sentence fragment the majority
quotes from Payton turns out to have originated in Justice
Powell’s concurrence in United States v. Watson, 423 U. S.
411, 428 (1976). And looking to that sentence in full, it is
plain Justice Powell, too, understood an arrest not as a
touching, but as “the taking hold of one’s person.” Ibid.
14                   TORRES v. MADRID

                    GORSUCH, J., dissenting

Thus, even the majority’s best sources only wind up point-
ing us back to the traditional possession rule.
                                2
   Unable to identify anything helpful in the main current
of the common law, the majority is forced to retreat to an
obscure eddy. Starting from Hodari D.’s three references to
“mere touch” arrests, the majority traces these authorities
back to their English origins. The tale that unfolds is a cu-
rious one.
   Before bankruptcy reforms in the 19th century, creditors
seeking to induce repayment of their loans could employ
bailiffs to civilly arrest delinquent debtors and haul them
off to debtors prison. See Cohen, The History of Imprison-
ment for Debt and Its Relation to the Development of Dis-
charge in Bankruptcy, 3 J. Legal Hist. 153, 154–155 (1982).
But the common law also offered debtors some tools to avoid
or delay that fate. Relevant here, the common law treated
the home as a “castle of defence and asylum” so no bailiff
could break into a debtor’s home to effect a civil arrest. 3
Blackstone, supra, at 288; see also Treiman, Escaping the
Creditor in the Middle Ages, 43 L. Q. Rev. 230, 233 (1927).
Over time, the practice of “keeping house” became an in-
creasingly popular way for debtors to evade the bailiff. Id.,
at 234. Naturally, too, creditors railed against this “notori-
ous” practice. See ibid. And eventually Parliament re-
sponded to their clamor. The English bankruptcy statutes
of 1542 and 1570 imposed serious penalties on debtors who
“kept house” to avoid imprisonment. Cohen, supra, at 157.
   It was seemingly against this backdrop that the strange
cases Hodari D.’s dicta briefly alluded to and the majority
has now dug up began to appear. Under their terms, a bail-
iff who could manage to touch a person hiding in his home,
often through an open window or door, was deemed to have
effected a civil “arrest.” See Genner v. Sparks, 6 Mod. 173,
87 Eng. Rep. 928 (K. B. 1704). And because this mere touch
                  Cite as: 592 U. S. ____ (2021)            15

                     GORSUCH, J., dissenting

was deemed an “arrest,” the bailiff was then permitted by
law to proceed to “br[eak] the house . . . to seize upon” the
person and render him to prison. Ibid., 87 Eng. Rep., at
929. Of course it was farcical to call a tap through an open
window an “arrest.” But it proved a useful farce, at least
for creditors.
  One of the majority’s lead cases, Sandon v. Jervis, El. Bl.
& El. 935, 120 Eng. Rep. 758 (K. B. 1858), illustrates the
absurdity of it all. There, a bailiff tried and failed “on sev-
eral occasions” to arrest a debtor. Id., at 936, 120 Eng. Rep.,
at 758. Eventually, the bailiff spotted an open window on
“an upper story,” so he ordered an assistant to fetch a lad-
der. Ibid. But the debtor and his daughter noticed the ploy
and “ran to the window,” slamming it closed. Ibid. Unfor-
tunately, in the excitement a window pane broke. Seeing
the opportunity, the bailiff ’s assistant, while perched atop
the ladder, thrust his hand through the opening and man-
aged to touch the debtor. Id., at 936–937, 120 Eng. Rep., at
758. According to the court, this “arrest” was sufficient to
justify the bailiff ’s later forcible entry into the home. Id.,
at 946–948, 120 Eng. Rep., at 762–763.
  By everyone’s account, however, the farce extended only
so far. Yes, the mere-touch arrest was a feature of civil
bankruptcy practice for an unfortunate period. But the ma-
jority has not identified a single founding-era case extend-
ing the mere-touch arrest rule to the criminal context. The
majority points to two nineteenth-century treatises, but
both reference only a case about a debt-collection arrest.
See ante, at 11–12 (citing 1 J. Backus, A Digest of Laws Re-
lating to the Offices and Duties of Sheriff, Coroner and Con-
stable 115–116, n. (c) (1812) (citing Genner v. Sparks, 6
Mod. 173, 87 Eng. Rep. 928 (K. B. 1704)), and 1 R. Burn,
The Justice of the Peace 275 (28th ed. 1837) (citing the
same)). The majority nods to dicta from an 1854 Delaware
state trial court, but that came long after the founding and
the majority does not explain how it sheds light on the
16                    TORRES v. MADRID

                     GORSUCH, J., dissenting

Fourth Amendment’s original meaning. See ante, at 12 (cit-
ing State v. Townsend, 5 Del. 487, 488)). And every remain-
ing early American case the majority cites for its “mere
touch” rule—from the founding through the Civil War—in-
volved only civil debt-collection arrests. See ante, at 4 (cit-
ing Whithead v. Keyes, 85 Mass. 495 (1862)); ante, at 6 (cit-
ing United States v. Benner, 24 F. Cas. 1084 (No. 14,568)
(CC ED Pa. 1830)); ante, at 6 (citing Butler v. Washburn, 25
N. H. 251 (1852) (tax collection)). The same goes for the
majority’s primary English authorities. See ante, at 7 (cit-
ing Nicholl v. Darley, 2 Y. & J. 399, 400, 148 Eng. Rep. 974
(Exch. 1828); Sandon, El. Bl. & El., at 940, 120 Eng. Rep.,
at 760)).
  So what relevance do these obscure and long-abandoned
civil debt-collection practices have for today’s case concern-
ing a criminal arrest and brought under the Fourth Amend-
ment? The answer seems to be not much, for at least three
reasons.
  In the first place, the Amendment speaks of “seizures,”
not “arrests.” To the extent the common law of arrests in-
forms the Amendment’s meaning, we have already seen
that an arrest normally meant taking possession of an ar-
restee. Maybe in one peculiar area, and for less than admi-
rable reasons, the common law deviated from this under-
standing. But this Court usually presumes that those who
wrote the Constitution used words in their ordinary sense,
not in some idiosyncratic way. See District of Columbia v.
Heller, 554 U. S. 570, 576 (2008). And today’s majority sup-
plies no evidence that anyone during the founding era un-
derstood the Fourth Amendment to adopt the specialized
definition of “arrest” from civil debt-collection practice.
  Second, even if we were to hypothesize that people did
understand the Fourth Amendment to incorporate this
quirky rule, what would that tell us? Here, the officers tried
to arrest Ms. Torres in a parking lot on behalf of the State
for serious crimes, not break into her home on behalf of the
                      Cite as: 592 U. S. ____ (2021)                     17

                         GORSUCH, J., dissenting

local credit union for missing a payment. So even if we were
willing to suppose that the founding generation understood
the Constitution to incorporate the majority’s civil debt-
collection arrest rule, nothing before us suggests they con-
templated, let alone endorsed, injecting it into the criminal
law and overriding settled doctrine equating arrests with
possession.
   Finally, even in the civil debt-collection context, the ma-
jority cannot point to even a single case suggesting that hit-
ting a suspect with an object—an arrow, a bullet, a cudgel,
anything—as she flees amounted to an arrest. Instead, the
majority’s cases hold only that the “laying of hands” on an
arrestee constituted an arrest. Ante, at 7. Thus, even if the
Fourth Amendment did transpose the “mere touch” rule
from the context of civil arrests into the criminal arena, it
still would not reach this case.
   How does the majority respond? Again, it does little more
than disregard the difficulties. The majority says there is
“no reason to suspect” the common law defined criminal ar-
rests of felons “any differently” than civil arrests of debtors.
Ante, at 13, 11. But the majority skips over all the evidence
canvassed above showing that a criminal arrest required
possession, not a mere touch. See Part III–B–1, supra. It
sails past its failure to identify any case holding that a mere
touch qualified as a criminal arrest. It ignores the fact
Blackstone defined criminal and civil arrests differently.4
And it claims to find support in Hawkins’s statement that
an officer could break into a house to capture an arrestee
——————
  4 The majority cites only Blackstone’s definition of a civil arrest, which

required a “corporal seising or touching the defendant’s body.” Ante, at
6 (quoting 3 W. Blackstone, Commentaries on the Laws of England 288
(1768)). But flipping from Blackstone’s third volume (discussing “private
wrongs”) to his fourth volume (discussing “public wrongs”) reveals—as
we have already seen but the majority fails to acknowledge—that Black-
stone equated a criminal arrest with “apprehending or restraining . . .
one’s person, in order to be forthcoming to answer an alleged or suspected
crime.” See supra, at 11.
18                   TORRES v. MADRID

                    GORSUCH, J., dissenting

who escaped after being “ ‘lawfully arrested for any Cause.’ ”
Ante, at 13–14 (quoting 2 Pleas of the Crown 87 (1721)).
Yet, the question before us isn’t what an officer might do
after making an arrest; it’s what constitutes an arrest in the
first place.
   Rather than confront shortcomings like these, the major-
ity asks us to glide past them. It suggests that importing
the mere-touch rule into the criminal context is permissible
because “no common law case” had occasion to reject that
idea expressly. See ante, at 16. But this gets things back-
wards. Today, for the first time, the majority seeks to
equate seizures and criminal arrests with mere touches, at-
tempted seizures, and batteries. It is for the majority to
show the Fourth Amendment commands this result. No
amount of rhetorical maneuvering can obscure how flat it
has fallen: Even its own authorities do more to undermine
than support its thesis. If common law courts never con-
templated the majority’s odd definition of a criminal ar-
rest—and this Court didn’t either for more than two centu-
ries—that can only be further proof of its implausibility.
   The majority asks us to glide past another problem too.
It acknowledges that its debt-collection cases required a
“laying on of hands” to complete an arrest. But it says we
should overlook that rule as an accident of antiquity.
“Touchings” by “firearm,” we are told, were unknown to
“founding-era courts,” and no “officer used a gun to appre-
hend a suspect” before 1850. Ante, at 9. Never mind the
shot heard round the world in 1775 and the adoption of the
Second Amendment. Never mind that as early as 1592,
when a bailiff “feared resistance” and thus “brought with
him” a gun “to arrest” someone, a common law court
deemed it lawful because “[t]he sheriff or any of his minis-
ters may for the better execution of justice carry with them
offensive or defensive weapons.” Seint John’s Case, 5 Co.
Rep. 71b, 77 Eng. Rep. 162, 162–163 (K. B. 1592). Never
mind that even tax collectors were carrying guns by the
                 Cite as: 592 U. S. ____ (2021)           19

                    GORSUCH, J., dissenting

1680s. E.g., Dickenson v. Watson, Jones, T. 205, 205–206,
84 Eng. Rep. 1218, 1218–1219 (K. B. 1682). And never
mind, too, that the majority’s problem isn’t limited to guns.
It fails to cite any case in which a touching by any weapon
was deemed sufficient to effect an arrest. Seemingly, the
majority would have us believe that bailiffs wielding any-
thing but their fists were beyond the framers’ imagination.
   Faced with all these problems, the majority tacks. It
scrambles to locate a case—any case—suggesting that com-
mon law courts considered “touchings” by weapon enough
to effect an arrest in the debt-collection context. Ulti-
mately, the majority asks us to dwell at length on the Coun-
tess of Rutland’s case. In at least that lone instance, the
majority promises, we will find bailiffs who arrested a
debtor by touching her with an object (a mace) rather than
a laying on of hands. See ante, at 7–8 (citing Countess of
Rutland’s Case, 6 Co. Rep. 52b, 54a, 77 Eng. Rep. 332 (Star
Chamber 1605)). But it turns out the dispute concerned
whether a countess could be civilly arrested at all, not when
or how the arrest was completed. The court had no reason
to (and did not) decide whether the bailiffs accomplished
their arrest when they “shewed her their mace,” “touch[ed]”
her with the mace, or “compelled the coachman to carry”
her to jail. Id., at 54a, 77 Eng. Rep., at 336. And no one
questions that these things together—a show of authority
followed by compelled detention—have always been enough
to complete an arrest. Not even minor royalty can rescue
the majority.
   So the majority tacks again. Now it asks us to dispense
with the common law’s “laying on of hands” requirement as
an “artificial” rule. Ante, at 8. Distinguishing between
“touchings” by hand and by weapon, it says, “calls to mind
the unavailing defense of the person who ‘persistently de-
nied that he had laid hands upon a priest, for he had only
cudgelled and kicked him.’ ” Ibid. But the quip exposes the
majority’s bind. To get where it wishes to go, the majority
20                        TORRES v. MADRID

                         GORSUCH, J., dissenting

not only must rework the rules found in the cases on which
it relies, it must also abandon their rationale. The debt-
collection cases treated the “laying on of hands” as a sign of
possession.5 Maybe the possession was more “constructive”
or even fictional than “actual.” See ante, at 16. But the idea
was that someone who stood next to a debtor and laid hands
on him could theoretically exercise a degree of control over
his person. Common law courts never said the same of bail-
iffs who fired arrows at debtors, shot them with firearms,
or cudgeled them as they ran away. Such conduct might
have amounted to a battery, but it was never deemed suffi-
cient to constitute an arrest. Doubtless that’s why when a
tax collector shot a man in the eye with a (supposedly una-
vailable) firearm in 1682, the man sued the officer for “as-
sault, battery, and wounding”—not false imprisonment.
See Dickenson, Jones, T., at 205, 84 Eng. Rep., at 1218–
1219.
   The majority implores us to study the common law his-
tory of arrests. But almost immediately, the majority real-
izes it cannot find what it seeks in the history of criminal
arrests. So it is forced to disinter a long-abandoned mere-
touch rule from civil bankruptcy practice. Then it must im-
port that rule into the criminal law. And because even that
isn’t enough to do the work it wishes done, the majority
must jettison both the laying on of hands requirement and
the rationale that sustained it. All of which leaves us con-

——————
  5 That is why the mere-touch cases often discussed the “corporal pos-

session of the debtor.” E.g., Sandon v. Jervis, El. Bl. & El. 935, 941–942,
120 Eng. Rep. 758 (K. B. 1858) (Hill, J.). A “corporal” touch was a legal
term of art and was frequently used in the context of determining the
possession of goods. E.g., Jordan v. James, 5 Ohio 88, 98 (1831) (stating
that an owner “may deliver any chattel he sells, symbolically and con-
structively, as well as by corporal touch”); see also 2 W. Blackstone, Com-
mentaries on the Laws 448–449, n. 16 (J. Chitty ed. 1826); Friedman,
Formative Elements in the Law of Sales: The Eighteenth Century, 44
Minn. L. Rev. 411, 445 (1960).
                  Cite as: 592 U. S. ____ (2021)           21

                     GORSUCH, J., dissenting

fusing seizures with their attempts and arrests with batter-
ies.
  The common law offers a vast legal library. Like any
other, it must be used thoughtfully. We have no business
wandering about and randomly grabbing volumes off the
shelf, plucking out passages we like, scratching out bits we
don’t, all before pasting our own new pastiche into the U. S.
Reports. That does not respect legal history; it rewrites it.
                                C
   If text and history pose challenges for the majority, so do
this Court’s precedents. The majority admits (as it must)
that the seizure of an object occurs only through taking pos-
session. Ante, at 4. The majority also admits (as it must)
that the seizure of a person through a “show of authority”
occurs only if the suspect submits to an officer’s possession.
Ante, at 15. But the majority fails to acknowledge that this
Court has also said the same principle governs the seizure
of persons effected through the use of force.
   In Terry v. Ohio, 392 U. S. 1 (1968), the Court explained
that “[o]nly when the officer, by means of physical force or
show of authority, has in some way restrained the liberty of
a citizen may we conclude that a ‘seizure’ has occurred.” Id.,
at 19, n. 16 (emphasis added). The restraint of liberty Terry
referred to was “interference” with a person’s “freedom of
movement.” United States v. Jacobsen, 466 U. S. 109, 113,
n. 5 (1984). As the Court put it in Brower v. County of Inyo,
489 U. S. 593 (1989), a decision issued just two years before
Hodari D.: “It is clear, in other words, that a Fourth Amend-
ment seizure” occurs “only when there is a governmental
termination of freedom of movement through means inten-
tionally applied.” 489 U. S., at 597 (emphasis deleted).
   Rather than follow these teachings, the majority dispar-
ages them. After highlighting (multiple times) that Justice
Scalia authored Hodari D.’s dicta, the majority turns about
22                    TORRES v. MADRID

                     GORSUCH, J., dissenting

and faults his opinion for the Court in Brower for “improp-
erly eras[ing] the distinction between seizures by control
and seizures by force.” Ante, at 14. The majority continues
on to blame other of our decisions, too, for “hav[ing] not al-
ways been attentive” to this supposedly fundamental dis-
tinction. Ibid. But this Court has not been “[in]attentive”
to a fundamental Fourth Amendment distinction for over
two centuries, let alone sought to “erase” it. In truth, the
majority’s “distinction” is a product of its own invention.
This Court has always recognized that how seizures take
place can differ. Some may take place after a show of au-
thority, others by the application of force, still others after
a polite request. But to be a “seizure,” the same result has
always been required: An officer must acquire possession.
                                IV
   If text, history, and precedent cannot explain today’s re-
sult, what can? The majority seems to offer a clue when it
promises its new rule will help us “avoi[d] . . . line-drawing
problems.” Ante, at 15–16 (internal quotation marks omit-
ted). Any different standard, the majority worries, would
be “difficult to apply.” Ante, at 15.
   But if efficiency in judicial administration is the explana-
tion, it is a troubling one. Surely our role as interpreters of
the Constitution isn’t to make life easier for ourselves. Cf.
Calabresi & Lawson, The Rule of Law as a Law of Law, 90
Notre Dame L. Rev. 483, 488 (2014). Nor, for that matter,
has the majority even tried to show that the traditional pos-
session rule—in use “[f]rom the time of the founding,” Ho-
dari D., 499 U. S., at 624—has proven unreasonably diffi-
cult to administer.        Everyone agrees, too, that the
possession rule will continue to govern when it comes to the
seizures of objects and persons through a show of authority.
So, rather than simplify things, the majority’s new rule for
“mere touch” seizures promises only to add another layer of
complexity to the law.
                  Cite as: 592 U. S. ____ (2021)           23

                     GORSUCH, J., dissenting

   Even within its field of operation, the majority’s rule
seems destined to underdeliver on its predicted efficiencies.
The majority tells us that its new test requires an “objective
intent to restrain.” Ante, at 10. But what qualifies is far
from clear. The majority assures us that a “tap on the
shoulder to get one’s attention will rarely exhibit such an
intent.” Ibid. Suppose, though, the circumstances “objec-
tively” indicate that the tap was “intended” to secure a per-
son’s attention for a minute, a quarter hour, or longer.
Would that be enough?
   Then there’s the question what kind of “touching” will
suffice. Imagine that, with an objective intent to detain a
suspect, officers deploy pepper spray that enters a suspect’s
lungs as he sprints away. Does the application of the pep-
per spray count? Suppose that, intending to capture a flee-
ing suspect, officers detonate flash-bang grenades that are
so loud they damage the suspect’s eardrum, even though he
manages to run off. Or imagine an officer shines a laser
into a suspect’s eyes to get him to stop, but the suspect is
able to drive away with now-damaged retinas. Are these
“touchings”? What about an officer’s bullet that shatters
the driver’s windshield, a piece of which cuts her as she
speeds away? Maybe the officer didn’t touch the suspect,
but he set in motion a series of events that yielded a touch-
ing. Does that count? While assuring us that its new rule
will prove easy to administer, the majority refuses to con-
front its certain complications. Lower courts and law en-
forcement won’t have that luxury.
   If efficiency cannot explain today’s decision, what’s left?
Maybe it is an impulse that individuals like Ms. Torres
should be able to sue for damages. Sometimes police shoot-
ings are justified, but other times they cry out for a remedy.
The majority seems to give voice to this sentiment when it
disparages the traditional possession rule as “artificial” and
promotes its alternative as more sensitive to “personal se-
curity” and “new” policing realities. Ante, at 8–9. It takes
24                    TORRES v. MADRID

                     GORSUCH, J., dissenting

pains to explain, too, that its new rule will provide greater
protection for personal “privacy” interests, which we’re told
make up the “essence” of the Fourth Amendment. Ante, at
16 (internal quotation marks omitted).
   But tasked only with applying the Constitution’s terms,
we have no authority to posit penumbras of “privacy” and
“personal security” and devise whatever rules we think
might best serve the Amendment’s “essence.” The Fourth
Amendment allows this Court to protect against specific
governmental actions—unreasonable searches and seizures
of persons, houses, papers, and effects—and that is the
limit of our license. Besides, it’s hard to see why we should
stretch to invent a new remedy here. Ms. Torres had ready-
made claims for assault and battery under New Mexico law
to test the officers’ actions. See N. M. Stat. Ann §41–4–12
(2020). The only reason this case comes before us under
§1983 and the Fourth Amendment rather than before a
New Mexico court under state tort law seems to be that Ms.
Torres (or her lawyers) missed the State’s two-year statu-
tory filing deadline. See Tr. of Oral Arg. 16–17; Brief for
Respondents 20, n. 4. That may be a misfortune for her,
but it is hardly a reason to upend a 230 year-old under-
standing of our Constitution.
   Nor, if we are honest, does today’s decision promise much
help to anyone else. Like Ms. Torres, many seeking to sue
officers will be able to bring state tort claims. Even for
those whose only recourse is a federal lawsuit, the major-
ity’s new rule seems likely to accomplish little. This Court
has already said that a remedy lies under §1983 and the
Fourteenth Amendment for police conduct that “shocks the
conscience.” County of Sacramento v. Lewis, 523 U. S. 833,
840, 845–847 (1998). At the same time, qualified immunity
poses a daunting hurdle for those seeking to recover for less
egregious police behavior. In our own case, Ms. Torres has
yet to clear that bar and still faces it on remand. So, at the
end of it all, the majority’s new rule will help only those who
                   Cite as: 592 U. S. ____ (2021)             25

                      GORSUCH, J., dissenting

(1) lack a state-law remedy, (2) evade custody, (3) after
some physical contact by the police, (4) where the contact
was sufficient to show an objective intent to restrain, (5)
and where the police acted “unreasonably” in light of clearly
established law, (6) but the police conduct was not “con-
science shocking.” With qualification heaped on qualifica-
tion, that can describe only a vanishingly small number of
cases.
   Even if its holding offers little practical assistance to an-
yone, perhaps the majority at least hopes to be seen as try-
ing to vindicate “personal security” and the “essence” of
“privacy” when it derides the traditional possession rule as
“artificial.” But an attractive narrative cannot obscure the
hard truth. Not only does the majority’s “mere touch” rule
allow a new cause of action in exceedingly few cases (non-
conscience-shocking-but-still-unreasonable batteries in-
tended to result in possession that don’t achieve it). It sup-
plies no path to relief for otherwise identical near-misses
(assaults). A fleeing suspect briefly touched by pursuing
officers may have a claim. But a suspect who evades a hail
of bullets unscathed, or one who endures a series of flash-
bang grenades untouched, is out of luck. That distinction
is no less “artificial” than the one the law has recognized for
centuries. And the majority’s new rule promises such
scarce relief that it can hardly claim more sensitivity to
“personal security” than the rule the Constitution has long
enshrined.
   In the face of these concerns, the majority replies by deny-
ing their relevance. It says there is “no call” to “surmise”
that its decision rests on anything beyond an “analysis of
the common law of arrest.” Ante, at 17. But there is no
surmise about it. The majority itself tells us that its deci-
sion is also justified by the need to “avoi[d] . . . line-drawing
problems,” protect “personal security,” and advance the
“privacy” interests that form the “essence” of the Fourth
Amendment. Having invoked these sundry considerations,
26                    TORRES v. MADRID

                     GORSUCH, J., dissenting

it’s hard to see how the majority might disown them.
                                *
  To rule as it does, the majority must endow the term “sei-
zure” with two different meanings at the same time. It
must disregard the dominant rule of the common law. It
must disparage this Court’s existing case law for erasing
distinctions that never existed. It cannot even guarantee
that its new rule will offer great efficiencies or meaningfully
vindicate the penumbral promises it supposes. Instead, we
are asked to skip from one snippet to another, finally land-
ing on a long-abandoned debt-collection practice that must
be reengineered to do the work the majority wishes done.
Our final destination confuses a battery for a seizure and
an attempted seizure with its completion. All this is miles
from where the standard principles of interpretation lead
and just as far from the Constitution’s original meaning.
And for what? A new rule that may seem tempting at first
blush, but that offers those like Ms. Torres little more than
false hope in the end.
  Respectfully, I dissent.

```

---

## GROUP: content/cases/United States v. Amos.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Amos
type: case
citation: "88 F.4th 446 (2023)"
parallel_cite: ""
neutral_cite: ""
court: 3d Cir.
court_level: coa
circuit: ca3
year: 2023
date_decided: 2023-12-14
docket: 20-3298
authority_weight: "Binding in-circuit — 3d Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9452158/united-states-v-shiheem-amos/"
  cluster_id: 9452158
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Amos
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Seizure of the Person]]"
    role: Key
related:
  - "[[Seizure of the Person]]"
  - "[[California v. Hodari D.]]"
  - "[[Brendlin v. California]]"
  - "[[United States v. Mendenhall]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - show-of-authority
  - terry-stop
holding: "A show of authority does not effect a Fourth Amendment seizure unless the suspect actually submits to it; a suspect already in motion who raises his hands only partway and pauses momentarily before fleeing has not submitted, so no seizure occurs until he is physically restrained — meaning a handgun that falls at that point is not the fruit of any earlier, unsupported seizure."
---

# United States v. Amos

*88 F.4th 446 (3d Cir. 2023)* (No. 20-3298) · U.S. Court of Appeals for the Third Circuit · **Binding in-circuit — 3d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9452158 → opinion 9909983 (88 F.4th 446, decided 2023-12-14); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
At about 2:00 a.m., two uniformed Philadelphia officers responded to a radio call about a person screaming and a man assaulting a woman near Eddie's Café. Finding no one there, they saw Shiheem Amos walking alone in an alleyway, "stomping [his] feet" and "throwing his arms around." The officers drove the wrong way down a one-way street with their lights on to cut him off and parked in the mouth of the alley, in Amos's path. Officer Lemos commanded Amos to stop and put his hands up; Amos raised his hands to a "halfway point," stopped for "[m]aybe a second," and then ran. Officer Mastroianni caught and handcuffed him about three car lengths away, and a handgun fell from Amos's pocket. Charged as a felon in possession, Amos moved to suppress the gun, arguing he had been seized pre-flight without reasonable suspicion. The district court found no pre-flight seizure and denied the motion.

## Issue
Whether Amos was "seized" before he fled — which requires both a show of authority and actual submission to it — so that the handgun recovered after his flight was the fruit of a seizure unsupported by reasonable suspicion.

## Rule
A seizure by show of authority is not complete without submission. The Third Circuit held the officers did show authority: "When a uniformed officer approaches an individual in the middle of the night in a marked police car and commands that person to stop and raise his or her hands, that is a show of authority." — slip op. at 10. But a show of authority alone does not seize a person; quoting *[[Brendlin v. California]]*, the court reaffirmed that "there is no seizure without actual submission; otherwise, there is at most an attempted seizure, so far as the Fourth Amendment is concerned."

## Application
Amos raised his hands only partway and paused for "maybe a second" before fleeing — the conduct of a suspect "already in motion" who refuses to stop, not the submission of the stationary, "frozen" suspect in *United States v. Lowe* who was seized precisely because he remained still. Momentary compliance is not submission. Because Amos never submitted, no seizure occurred until Officer Mastroianni physically overpowered him after the flight; the pre-flight encounter therefore required no reasonable suspicion, and the handgun that fell during the arrest was not the fruit of an unlawful seizure.

## Conclusion
The denial of the motion to suppress was **affirmed**; the court [[Reading and Citing Cases#on-remand|remanded]] for resentencing because Amos's prior Pennsylvania aggravated-assault conviction did not qualify as a "crime of violence." Nygaard, J., wrote for the court (Bibas, Nygaard, Fuentes, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Amos* illustrates the submission requirement of *[[California v. Hodari D.|Hodari D.]]* and *[[Brendlin v. California|Brendlin]]*: a moving suspect who only momentarily pauses before running has not submitted to a show of authority, so the Fourth Amendment clock does not start until physical restraint — the point at which reasonable suspicion is measured.

## Appears on
- [[Seizure of the Person]] — *Key*

## Sources
- [*United States v. Amos*, 88 F.4th 446 (3d Cir. 2023)](https://www.courtlistener.com/opinion/9452158/united-states-v-shiheem-amos/) — pinpoint: slip op. at 10 (show-of-authority holding); the CL opinion text carries the slip-opinion page numbers rather than 88 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "45620b02ff4ef661", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "88 F.4th 446 (2023)", "court": "3d Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Amos", "year": "2023"}}
{"assertion_id": "463ed64ebe81f5c8", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key", "title": "United States v. Amos"}}
{"assertion_id": "d2c5dec2b532b2a5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A show of authority does not effect a Fourth Amendment seizure unless the suspect actually submits to it; a suspect already in motion who raises his hands only partway and pauses momentarily before fleeing has not submitted, so no seizure occurs until he is physically restrained — meaning a handgun that falls at that point is not the fruit of any earlier, unsupported seizure.", "title": "United States v. Amos"}}
{"assertion_id": "bc9a743a919998fe", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Amos", "varies_by_point": "false"}}
{"assertion_id": "cddf4cb3c7a65fe1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 3d Cir.", "title": "United States v. Amos"}}
```

### lake record — United States v. Amos

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Amos",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Shiheem Amos",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Amos",
    "court": "3d Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca3",
    "state": null,
    "date_decided": "2023-12-14",
    "year": 2023,
    "docket": "20-3298",
    "cluster_id": 9452158,
    "lead_opinion_id": 9909983,
    "sibling_ids": [],
    "absolute_url": "/opinion/9452158/united-states-v-shiheem-amos/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "88 F.4th 446",
      "volume": "88",
      "reporter": "F.4th",
      "page": "446",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "88 F.4th 446",
        "volume": "88",
        "reporter": "F.4th",
        "page": "446",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "88 F.4th 446",
    "official_selection": {
      "court_class": "coa",
      "selected": "88 F.4th 446",
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
    "date_created": "2026-07-07T01:38:56Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-amos--9452158",
      "to_record_id": "United States v. Amos",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Amos

```
                                 PRECEDENTIAL


  UNITED STATES COURT OF APPEALS
       FOR THE THIRD CIRCUIT

                 __________

                 No. 20-3298
                 __________

      UNITED STATES OF AMERICA

                      v.

              SHIHEEM AMOS,
                         Appellant
                __________

On Appeal from the United States District Court
   for the Eastern District of Pennsylvania

(District Court Criminal No. 2-18-cr-00571-001)
  District Judge: Honorable Gerald J. Pappert

           Argued: January 23, 2023

BEFORE: BIBAS, NYGAARD, and FUENTES,
            Circuit Judges


          (Filed: December 14, 2023)
Anthony J. Carissimi
Timothy M. Stengel
Robert A. Zauzmer [Argued]
Office of United States Attorney
615 Chestnut Street
Suite 1250
Philadelphia, PA 19106
       Counsel for Appellee

Abigail E. Horn [Argued]
Federal Community Defender Office
for the Eastern District of Pennsylvania
601 Walnut Street
The Curtis Center, Suite 540 West
Philadelphia, PA 19106
        Counsel for Appellant
                          __________

                 OPINION OF THE COURT
                       __________

NYGAARD, Circuit Judge.
       Shiheem Amos appeals the District Court’s denial of his
motion to suppress and his criminal sentence. He first argues
that the court erred when it denied his motion to suppress a
firearm because he was seized without reasonable suspicion.
Second, he argues that the court erred when it included a
United States Sentencing Guidelines’ crime of violence en-
hancement for a previous state court conviction and sentenced
him to 62 months’ imprisonment. We will affirm the denial of
the motion to suppress, but because Amos’s prior conviction is
not a crime of violence, we will remand for resentencing.




                              2
            I.    Background
       On September 26, 2018, police officers Hugo Lemos
and Nicholas Mastroianni were working the overnight shift as
patrol officers in southwest Philadelphia. At about 2:00 a.m.,
they received a radio call for a person screaming at the inter-
section of 65th Street and Dicks Avenue outside Eddie’s Café
and a man assaulting a woman on the highway. The officers
were nearby and arrived at Eddie’s Café within two minutes.
No one was outside Eddie’s Café.
        The officers continued driving past the café on 65th
Street and Officer Lemos saw one pedestrian, later discovered
to be Shiheem Amos, walking alone in an alleyway across the
street. Amos was walking toward 64th Street and was “stomp-
ing [his] feet, and kind of throwing his arms around,” accord-
ing to Officer Lemos. App’x 85. The officers drove around the
block to cut Amos off, driving the wrong way down a one-way
street with the overhead lights on. The officers parked midway
in the entrance to the alleyway and Amos continued to walk
toward them. Officer Lemos got out of the vehicle and told
Amos to stop and put his hands up. 1 Officer Lemos testified
that Amos placed his hands at a “halfway point” and stopped

1
  There is some discrepancy about where Officer Lemos was
when he asked Amos to stop. At the preliminary hearing, he
testified that he was out of the car. At the suppression hearing,
he testified that he was still in the car and yelled out the win-
dow. He testified that the earlier testimony was probably accu-
rate. The District Court explained that any discrepancy did not
impact its assessment of Officer Lemos’s credibility or alter its
legal analysis.




                               3
for “[m]aybe a second.” App’x 89, 91. Amos then ran diago-
nally and reached about three car lengths away from the offic-
ers. Officer Mastroianni quickly caught up with Amos and
handcuffed him. At that time, a handgun fell from Amos’s
pocket, a firearm he was not permitted to carry due to his pre-
vious conviction of a felony punishable by a term of imprison-
ment exceeding one year.
        Amos was charged with one count of possession of a
firearm by a felon under 18 U.S.C. § 922(g). He filed a motion
to suppress the gun and argued that he was seized pre-flight
without reasonable suspicion. After an evidentiary hearing, the
District Court denied the motion, finding no pre-flight seizure
occurred. Amos then pleaded guilty pursuant to a plea agree-
ment. 2
       At sentencing, the parties disputed the applicability of a
sentencing enhancement under Sentencing Guidelines
§ 2K2.1(a)(4)(A) which applies to defendants previously con-
victed of a felony “crime of violence.” The Government argued
that Amos’s 2008 Pennsylvania state conviction for aggravated

2
  Amos’s plea agreement waived appellate and collateral chal-
lenges with only a few exceptions, including that he could chal-
lenge the denial of his motion to suppress and he could raise
ineffective assistance of counsel. As such, Amos originally
couched his crime of violence argument in ineffective assis-
tance of counsel. However, the Government agreed to waive
the appellate waiver so we can exercise ordinary review of the
guideline challenge. Amos confirms this, explaining that the
ineffective assistance claim is no longer necessary, and the
Court can review the issue squarely.




                               4
assault, a second-degree felony, qualified as a predicate crime
of violence.
       The state court records did not identify the specific
second-degree subsection of the aggravated assault statute, 18
Pa. Cons. Stat. § 2702(a)(3)–(7), under which Amos was con-
victed. Accordingly, the Government had to prove that all five
subsections qualified as a crime of violence. The District Court
found that the Government met its burden and applied the en-
hancement. This resulted in a base offense level of twenty,
from which the court deducted two levels for acceptance of re-
sponsibility, making it eighteen. Combined with Amos’s crim-
inal history category of six, he was subject to an advisory
Guidelines’ range of 57 to 71 months’ imprisonment. Without
the enhancement, Amos’s range would have been 30 to 37
months’ imprisonment. The court imposed a sentence of 62
months’ imprisonment followed by three years of supervised
release. Amos timely appealed. 3
           II.   Motion to Suppress
       We review the District Court’s denial of a motion to
suppress for clear error as to the underlying factual findings
and exercise plenary review over questions of law. United
States v. Coward, 296 F.3d 176, 179 (3d Cir. 2002).




3
 The District Court had jurisdiction under 18 U.S.C. § 3231
and we have jurisdiction pursuant to 28 U.S.C. § 1291 and 18
U.S.C. § 3742.




                               5
                  A. The Fourth Amendment Suppression
                     Analysis
        The Fourth Amendment prohibits “unreasonable
searches and seizures….” U.S. Const. amend. IV. Unless an
exception applies, a seizure “must be effectuated with a war-
rant based on probable cause” in order to be reasonable under
the Fourth Amendment. United States v. Robertson, 305 F.3d
164, 167 (3d Cir. 2002). One such exception to the warrant re-
quirement was established in Terry v. Ohio, 392 U.S. 1 (1968).
When a police officer has a “reasonable, articulable suspicion
that criminal activity is afoot,” he may conduct a brief, inves-
tigatory stop without a warrant, i.e., a “Terry stop.” Illinois v.
Wardlow, 528 U.S. 119, 123 (2000). “[R]easonable suspicion
is a less demanding standard than probable cause and requires
a showing considerably less than preponderance of the evi-
dence.” Id. However, an officer must “articulate more than an
‘inchoate and unparticularized suspicion or “hunch”’ of crimi-
nal activity” to establish reasonable suspicion. Id. at 124 (quot-
ing Terry, 392 U.S. at 27). If a Terry stop is conducted without
reasonable suspicion of criminal activity, any evidence ob-
tained must be suppressed as “fruit of the poisonous tree.”
Wong Sun v. United States, 371 U.S. 471, 487–88 (1963) (in-
ternal quotation marks omitted).
       Reasonable suspicion is evaluated at the moment of a
seizure, so the first step in a suppression analysis is to deter-
mine when the seizure occurred. United States v. Smith, 575
F.3d 308, 312 (3d Cir. 2009). When determining whether a sei-
zure occurred, we must consider “all the circumstances sur-
rounding the encounter.” Id. (quoting Florida v. Bostick, 501
U.S. 429, 439 (1991)). If a seizure occurred pre-flight, then the




                                6
flight “plays no role in the reasonable suspicion analysis.”
United States v. Brown, 448 F.3d 239, 245 (3d Cir. 2006).
        A seizure can occur in two ways: 1) “a laying on of
hands or application of physical force to restrain movement,
even when it is ultimately unsuccessful,” or 2) “submission to
a ‘show of authority.’” Id. (quoting California v. Hodari D.,
499 U.S. 621, 626 (1991)). There is no dispute that the police
officers did not touch Amos before he tried to flee, so a seizure
could only have occurred pre-flight if Amos 1) submitted 2) to
a show of authority. The absence of either element is fatal to
his appeal.
                  B. The Police Officers Showed Authority
                     Because No Reasonable Person in
                     Amos’s Position Would Have Felt Free to
                     Leave
        We first address whether the police officers showed au-
thority when they encountered Amos in the alleyway. The Dis-
trict Court found no show of authority by the officers because
they did not communicate to Amos that he was not free to
leave. The court relied on the facts that the officers did not ac-
tivate the police car’s lights or sirens, brandish their weapons,
block Amos’s path, come into contact with Amos, or make any
threats or intimidating movements.
        An objective test determines whether there has been a
show of authority; we must ask whether a reasonable person
would have believed he was not free to leave based on the of-
ficer’s words and actions. Hodari D, 499 U.S. at 628. Factors
such as “the threatening presence of several officers, the dis-
play of a weapon by an officer, some physical touching of the




                                7
person of the citizen, or the use of language or tone of voice
indicating that compliance with the officer’s request might be
compelled” may indicate a show of authority occurred. United
States v. Mendenhall, 446 U.S. 544, 554 (1980) (plurality opin-
ion).
       The Government hardly protests that the officers did not
show authority. See Appellee Br. 12 (“In this matter, whether
or not there was a show of authority in the officer’s command
to stop, there is no question that Amos did not comply before
running on foot.”); see also id. at 15 (“Assuming Officer
Lemos’ single request that the defendant stop and raise hands
was a show of authority, the defendant never submitted to it.”).
In a footnote, the Government notes that the District Court did
not find a show of authority and says, “that conclusion alone
resolves this case.” Id. at 16 n.3.
       Amos argues that the police officers’ show of authority
was strong. He asserts that late at night, he was pursued by two
uniformed officers in a marked patrol car. The officers
emerged the wrong way out of a one-way street and parked in
the mouth of the alleyway from where Amos was emerging.
He argues that based on our caselaw, the officers showed au-
thority because no reasonable person would have felt free to
leave.
       We agree with Amos that the officers displayed a show
of authority. Under the circumstances of the encounter between
Amos and the officers, a reasonable person would have be-
lieved he was not free to leave. While the District Court is right
that the officers did not brandish their weapons or make any
threats, the record shows that at 2:00 a.m. a marked police car




                                8
parked against the flow of traffic midway in the entrance to the
alleyway from where Amos was walking. The car was parked
in Amos’s direct forward path and inside were two uniformed
officers. One officer immediately got out and approached
Amos, commanding him to stop and show his hands.
        Additionally, the record indicates the officers arrived in
a hurried manner as they drove the wrong way against traffic
with their lights on initially to get in Amos’s path. Similar facts
were presented in United States v. Lowe, 791 F.3d 424 (3d Cir.
2015). In Lowe, multiple marked police cars, which used their
lights and sirens en route to their destination, arrived at a resi-
dence in the middle of the night. Id. at 428. Multiple uniformed
officers approached the defendant and commanded that he
show his hands. Id. at 431–32. Based on the record, we found
that “the officers’ approach constituted a show of authority, as
a reasonable person in Lowe’s position would not have felt free
to decline the interaction or leave.” Id. at 432.
       We think that under the circumstances presented to
Amos, a reasonable individual would have understood that the
officers were exercising control and showing authority. No rea-
sonable person who is commanded to stop and show their
hands in the middle of the night by uniformed officers with a
marked police car would feel free to ignore the command and
walk away. We have previously found a “clear show of author-
ity” when an officer informed two robbery suspects that the
“victim was being brought over to identify them as possible
suspects and, if they were not identified, they would be free to
go—necessarily implying that they were not free to leave.”
Brown, 448 F.3d at 245. We went on to say that the officer’s
demand that the suspects submit to a pat-down “would have




                                9
conveyed … to a reasonable person” that “he was being or-
dered to restrict his movement.” Id. (quoting Hodari D., 499
U.S. at 628). And we have assumed a show of authority when
officers instruct a defendant to place his hands on their vehicle.
See Smith, 575 F.3d at 314. Today, we confirm that assump-
tion. When a uniformed officer approaches an individual in the
middle of the night in a marked police car and commands that
person to stop and raise his or her hands, that is a show of au-
thority.
                  C. Amos Did Not Submit to the Officer’s
                     Show of Authority
       We next consider submission to authority. Although
Amos is correct that the officers displayed a show of authority,
he must have also submitted to that display in order to have
been seized. “A police officer may make a seizure by a show
of authority and without the use of physical force, but there is
no seizure without actual submission; otherwise, there is at
most an attempted seizure, so far as the Fourth Amendment is
concerned.” Brendlin v. California, 551 U.S. 249, 254 (2007).
       When Officer Lemos told Amos to stop and put his
hands up, Amos placed his hands at a “halfway point” and
stopped for “[m]aybe a second” before he ran. App’x 89, 91.
The District Court found that Amos did not submit to the of-
ficers when he fled before his hands were all the way up.
       When determining whether an individual has submitted
to a show of authority, we consider both the nature of the show
of authority and the individual’s conduct at that moment. See
Lowe, 791 F.3d at 430. “Thus, while ‘a fleeing man is not
seized until he is physically overpowered, … one sitting in a




                               10
chair may submit to authority by not getting up to run away.’”
Id. at 431 (quoting Brendlin, 551 U.S. at 262).
        Amos focuses on three cases to argue that he submitted
to the officers’ authority, but his reliance on those cases is mis-
placed. Amos asserts that in Lowe, the defendant “submitted
even though he took several steps backward into a fence, and
even though he failed to comply with the officers’ commands
to show his hands.” Appellant Br. 19. But we explained that
Lowe stayed put where he was when the officers converged
and was described by officers as “frozen” and “shocked.”
Lowe, 791 F.3d at 433. We explicitly held that “when a station-
ary suspect reacts to a show of authority by not fleeing, making
no threatening movement or gesture, and remaining stationary,
he has submitted under the Fourth Amendment and a seizure
has been effectuated.” Id. at 434 (emphasis added). Amos was
not a stationary suspect and did not remain stationary. In fact,
we distinguished such a circumstance in Lowe when we
pointed out that “[o]ther courts have found no submission
when a suspect already in motion refuses to stop when ap-
proached by an officer.” Id. at 433 (collecting cases).
       Amos also relies on Brown, which bears closer resem-
blance to the situation at hand but just misses the mark. As de-
scribed above, the officer in Brown demanded that robbery sus-
pects submit to a pat-down. 448 F.3d at 245. We explained that
one suspect “clearly submitted” when he “turned to face the
police car and placed his hands on the vehicle in response to
[the officer’s] demand.” Id. at 246. Amos points out that we
said that “conclusion is not meaningfully contradicted by [the
officer’s] testimony that Brown had begun to move his hands
to the vehicle, but did not complete the action.” Id. True




                                11
enough, but we also explained that “Brown demonstrated more
than ‘momentary compliance’” with the officer’s demands and
distinguished a situation where a defendant did not. Id. (distin-
guishing United States v. Valentine, 232 F.3d 350, 359 (3d Cir.
2000)).
        For its seizure analysis, we found Brown similar to
United States v. Coggins, 986 F.2d 651 (3d Cir. 1993), which
Amos also relies on. Coggins, who was sitting down, attempted
to terminate an encounter with a Drug Enforcement Admin-
istration agent at an airport. Id. at 652. When he stood up and
said he had to use the bathroom, the agent told him to wait. Id.
Coggins then sat back down. Id. We explained that Coggins
submitted to the agent’s authority by sitting down. Id. at 654.
He made a clear request to leave, the agent ordered him to stay,
and Coggins complied with the order by sitting down. Id. Such
a clear affirmative submission is missing from Amos’s encoun-
ter with the officers.
        Instead, Amos’s actions were like those in Valentine
and Smith, where we found no submission and thus no seizure.
In Valentine, police officers approached a man who matched
the description of a tip for a gunman and told him to place his
hands on their police car. 232 F.3d at 352–53. The man re-
sponded, “Who, me?” and then ran toward the officers before
being grabbed and wrestled to the ground. Id. at 353. Although
we found that, under the totality of the circumstances, the of-
ficers had reasonable suspicion to stop and frisk Valentine, we
went on to address whether a seizure occurred prior to his at-
tempt to flee. Id. at 357–59. Valentine argued that when the
officer ordered him to place his hands on the car, he momen-
tarily complied with the order when he stopped and gave his




                               12
name, which in turn triggered a seizure. Id. at 359. But we ex-
plained that Valentine’s momentary “compliance” was not a
submission to authority. Id. “Even if Valentine paused for a
few moments and gave his name, he did not submit in any re-
alistic sense to the officers’ show of authority, and therefore
there was no seizure until [the officer] grabbed him.” Id.
        In Smith, officers were patrolling during the night when
they encountered Smith on the street and asked him to talk. 575
F.3d at 311. He briefly complied, walking toward the officers’
car and answering questions about his identification and desti-
nation. Id. He then provided nonresponsive answers to contin-
ued questioning, so one of the officers asked him to place his
hands on the hood of the car. Id. Smith took two steps toward
the vehicle, at which point the officers opened their car doors
and Smith ran. Id. We relied on Valentine for the finding that
“momentary compliance was not enough to trigger a seizure”
and found that Smith’s two steps towards the officers’ vehicle
did not indicate submission to the show of authority. Id. at 315–
16. “[S]ubmission to authority under Hodari D., ‘requires at
minimum, that a suspect manifest compliance with police or-
ders.’” Id. at 316 (quoting United States v. Waterman, 569 F.3d
144, 146 n.3 (3d Cir. 2009)). Smith’s two steps and non-
responsive answers did not represent manifest compliance. Id.
We distinguished Brown by explaining that the defendant there
submitted to the officer’s orders to stay put prior to turning to
face the car, and thus his submission was manifested at that
point. Id. at 315.
       Amos’s situation is most analogous to Smith. Id. at 311.
Like the officer in Smith who directed the suspect to put his
hands on the vehicle, the officer here told Amos to stop and put




                               13
his hands up. Just as Smith did not comply by taking two steps
forward before running, Amos’s brief hesitation and raising of
his hands halfway before running was not “manifest compli-
ance.” Id. at 316. Similarly, even though Valentine paused for
a few moments and gave his name, he did not submit in a real-
istic sense to the officers’ show of authority. Valentine, 232
F.3d at 359. The same can be said for Amos.
       We conclude that as in Valentine and Smith, Amos’s ac-
tions were not a submission to authority. In the cases where we
found such a submission, the compliance was more definite
than Amos’s display. Amos’s one- or two-second pause and
halfway hand raise is clearly different than affirmatively sitting
down after being told to or complying with an officer’s order
for more than a moment. Instead, it was more akin to the “ex-
traordinarily brief” compliance we have recognized as insuffi-
cient submission to authority. See United States v. Hester, 910
F.3d 78, 86 (3d Cir. 2018) (referring to Valentine and Smith).
        Accordingly, because submission “would seem to re-
quire something more than a momentary pause,” Amos’s brief
pause and halfway hand raise was not a submission to the of-
ficers’ show of authority. Waterman, 569 F.3d at 146. As
Amos did not submit to the show of authority, no seizure oc-
curred at that time. Thus, reasonable suspicion is not evaluated
at that point. See Smith, 575 F.3d at 312.
       When Amos ran and attempted to flee, the officers
caught him and put him into handcuffs—a classic seizure. See
Hodari D., 499 U.S. at 624. Amos concedes that if he was not
seized until after he fled, then there was reasonable suspicion




                               14
at that point to seize him based on his headlong flight. 4 See
Wardlow, 528 U.S. at 124; Appellant Br. 6.
       In sum, Amos’s one- or two-second pause and halfway
hand raise did not manifest submission to the officer’s show of
authority. Because Amos did not submit to the show of author-
ity and was not seized until the officers put him in handcuffs
based on reasonable suspicion, the District Court did not err in
denying his motion to suppress.
           III.   Crime of Violence Sentencing Enhancement
       We next consider Amos’s challenge to his sentence. He
has challenged only one aspect of his sentencing: the crime of
violence enhancement. Whether an offense qualifies as a crime
of violence is a question of law subject to plenary review. See
United States v. Wilson, 880 F.3d 80, 83 (3d Cir. 2018).
                  A. The Elements of Force Clause
        The “crime of violence” enhancement to the firearm
guideline applies where “the defendant committed any part of
the instant offense subsequent to sustaining one felony convic-
tion of either a crime of violence or a controlled substance of-
fense.” U.S.S.G. § 2K2.1(a)(4)(A). A crime of violence is any
federal or state offense, punishable by imprisonment for more
than a year, that “(1) has as an element the use, attempted use,
or threatened use of physical force against the person of

4
 Because Amos was not seized until he was grabbed and hand-
cuffed by the officers, we need not decide whether the officers
had reasonable suspicion at an earlier time based on the anon-
ymous tip.




                              15
another, or (2) is murder, voluntary manslaughter, kidnapping,
aggravated assault, a forcible sex offense, robbery, arson, ex-
tortion, or the use or unlawful possession of a firearm described
in 26 U.S.C. § 5845(a) or explosive material as defined in 18
U.S.C. § 841(c).” U.S.S.G. § 4B1.2(a). There is no assertion
by the parties that subsection two applies to Amos, so our in-
quiry is confined to subsection one, the so-called elements of
force clause. “Physical force” in the elements of force clause
“means violent force—that is, force capable of causing physi-
cal pain or injury to another person.” Johnson v. United States,
559 U.S. 133, 138–40 (2010). 5
                  B. The Modified Categorical Approach
       When determining whether a conviction is a crime of
violence, we must use the categorical approach. This requires
us to “compare the elements of the statute under which the de-
fendant was convicted to the [G]uidelines’ definition of crime
of violence.” United States v. Wilson, 880 F.3d 80, 83 (3d Cir.
2018) (citing United States v. Chapman, 866 F.3d 129, 133 (3d
Cir. 2017)). When conducting the categorical approach analy-
sis under the elements of force clause, we ask whether “the use,
attempted use, or threatened use of physical force against an-
other person is categorically an element of the offense of

5
  Johnson addressed whether an offense constituted a “violent
felony” under the Armed Career Criminal Act, 18 U.S.C.
§ 924(e). Because the definition of crime of violence bears
“substantial similarity” to the definition of violent felony in the
ACCA, we apply authority interpreting one definition to the
other. See United States v. Marrero, 743 F.3d 389, 394 n.2 (3d
Cir. 2014) (citation omitted).




                                16
conviction.” United States v. Ramos, 892 F.3d 599, 606 (3d
Cir. 2018). As stated above, physical force “means vio-
lent force—that is, force capable of causing physical pain or
injury to another person.” Johnson, 559 U.S. at 140. “Accord-
ingly, a crime is a violent one under the elements clause so long
as it has an element that can be satisfied only through the use,
threatened use, or attempted use of force against another per-
son that is capable of causing that person physical pain or in-
jury.” Ramos, 892 F.3d at 611. That is true regardless of
whether an offender could be convicted under the statute for
applying force directly or indirectly. Chapman, 866 F.3d at
132–33.
        Thus, if the state statute Amos was convicted under has
an element of violent force capable of causing physical pain or
injury, “then the statute proscribes a predicate crime of vio-
lence within the meaning of the Guidelines.” Ramos, 892 F.3d
at 606. But if the statute does not have such an element, it
“sweeps more broadly” and the state conviction is not a predi-
cate offense for the crime of violence sentencing enhancement.
See United States v. Brown, 765 F.3d 185, 189 (3d Cir. 2014)
(citation omitted).
         A court “may ‘look only to the statutory definitions’—
i.e., the elements—of a defendant’s prior offenses, and not ‘to
the particular facts underlying those convictions.’” Id. (quoting
Descamps v. United States, 570 U.S. 254, 261 (2013) (empha-
sis in original)). This approach requires that a court both “ig-
nore the actual manner in which the defendant committed the
prior offense” and “presume that the defendant did so by en-
gaging in no more than ‘the minimum conduct criminalized by




                               17
the state statute.’” Ramos, 892 F.3d at 606 (quoting Moncrieffe
v. Holder, 569 U.S. 184, 191 (2013)).
       However, when a defendant was convicted under a “di-
visible” statute that defines multiple crimes, we apply the
“modified categorical approach.” United States v. Abdullah,
905 F.3d 739, 744 (3d Cir. 2018) (citation omitted). This ap-
proach allows us to look beyond the statute of conviction and
identify the specific statutory provision under which the de-
fendant was previously convicted. Id. We may look to so-
called Shepard documents, including the charging document,
written plea agreement, and plea colloquy transcript. Id.; see
Shepard v. United States, 544 U.S. 13, 16 (2005). If a specific
provision is identified, the categorical approach is applied to
that one provision. Abdullah, 905 F.3d at 744. If the records
are unclear, the Government must “show that all of the stat-
ute’s offenses [meet] the federal definition” of crime of vio-
lence. Pereida v. Wilkinson, 141 S. Ct. 754, 766 (2021) (em-
phasis in original).
                 C. The Pennsylvania Second-Degree Aggra-
                    vated Assault Statute
        The state court records show that Amos was charged
with and entered a guilty plea to aggravated assault as a felony
in the second-degree generally. In 2008, when Amos commit-
ted the crime, the Pennsylvania aggravated assault statute in-
cluded seven subsections enumerating an aggravated assault.
Subsections one and two are felonies in the first-degree,
whereas subsections three through seven are felonies in the
second-degree. See 18 Pa. Cons. Stat. § 2702(b).
       A person is guilty of aggravated assault if he:




                              18
(3) attempts to cause or intentionally or know-
ingly causes bodily injury to any of the officers,
agents, employees or other persons enumerated
in subsection (c), in the performance of duty;
(4) attempts to cause or intentionally or know-
ingly causes bodily injury to another with a
deadly weapon;
(5) attempts to cause or intentionally or know-
ingly causes bodily injury to a teaching staff
member, school board member or other em-
ployee, including a student employee, of any el-
ementary or secondary publicly-funded educa-
tional institution, any elementary or secondary
private school licensed by the Department of Ed-
ucation or any elementary or secondary paro-
chial school while acting in the scope of his or
her employment or because of his or her employ-
ment relationship to the school;
(6) attempts by physical menace to put any of the
officers, agents, employees or other persons enu-
merated in subsection (c), while in the perfor-
mance of duty, in fear of imminent serious bodily
injury; or
(7) uses tear or noxious gas as defined in section
2708(b) (relating to use of tear or noxious gas in
labor disputes) or uses an electric or electronic
incapacitation device against any officer, em-
ployee or other person enumerated in subsection
(c) while acting in the scope of his employment.




                       19
Id. § 2702(a)(3)–(7).
        At sentencing, the Government argued that Amos’s
2008 Pennsylvania state aggravated assault conviction quali-
fied as a predicate crime of violence. Under Ramos, the modi-
fied categorial approach applies because the Pennsylvania ag-
gravated assault statute is divisible. See 892 F.3d at 607–10.
Accordingly, the Government provided the District Court with
the state court Certified Records of Conviction. The Govern-
ment conceded that the Shepard documents do not indicate
what subsection of Section 2702(a) Amos was convicted un-
der, except to say it was a felony in the second-degree as listed
on the written guilty plea colloquy. The Government argued
the crime of violence enhancement applied because each of the
possible five subsections is a crime of violence. Amos’s trial
counsel confined his argument in opposition to subsection six.
See App’x 240 (“Your Honor, my argument is limited to § 6.”).
The court agreed with the Government and applied the sentenc-
ing enhancement, which resulted in a sentence of 62 months’
imprisonment followed by three years of supervised release.
                  D. 18 Pa. Con. Stat. § 2702(a)(3) Is Not a
                     Crime of Violence 6
       As previously stated, the Government must show that
all subsections of Pennsylvania’s aggravated assault statute



6
  Because Amos succeeds under subsection three, we need not
address whether the other subsections of aggravated assault in
the second-degree are crimes of violence. Likewise, we need
not address whether the Government waived its right to argue




                               20
meet the federal definition of crime of violence. See Pereida,
141 S. Ct. at 766. If the Government is unable to do so on even
one subsection, then Amos prevails in his argument that his
conviction under the statute is not a crime of violence, and he
is thus not subject to the sentencing enhancement.
        We start and end our analysis by applying our recent
decision in United States v. Jenkins, 68 F.4th 148 (3d Cir.
2023). In Jenkins, we addressed whether 18 Pa. Cons. Stat.
§ 2702(a)(3)—one of the exact subsections at issue here—is a
violent felony under the ACCA. We relied on the Pennsylvania
Supreme Court’s decision United States v. Harris, 289 A.3d
1060 (Pa. 2023), to find “that Section 2702(a)(3) can at least
be violated by a failure to act, so it is not a violent felony.”
Jenkins, 68 F.4th at 152. Like the subsection addressed in Har-
ris, the statutory language in Section 2702(a)(3) makes no
mention of force and there is no reference “to the manner by
which an injury must be inflicted.” Id. at 153 (quoting Harris,
289 A.3d at 1070).
       That affirmative holding controls here because of the
“substantial similarity” between the definitions of violent fel-
ony in the ACCA and crime of violence in the Guidelines. See
Marrero, 743 F.3d at 394 n.2 (citation omitted). The Shepard
documents do not rule out that Amos was convicted under sub-
section three of the Pennsylvania aggravated assault statute,
and under Jenkins, subsection three is not a crime a violence.
Accordingly, Amos must be resentenced.


that Amos was not convicted under subsection seven and
whether a closed record on remand is necessary.




                              21
          IV.    Conclusion
        For the foregoing reasons, we will affirm the District
Court’s order denying Amos’s motion to suppress. Addition-
ally, because Section 2702(a)(3) is not a crime of violence, we
vacate Amos’s sentence and remand for resentencing con-
sistent with this opinion.




                              22

```

---

## GROUP: content/cases/United States v. August.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. August"
type: case
citation: "136 F.4th 595 (2025)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Court of Appeals, 5th Circuit"
court_level: coa
circuit: 5th
year: 2025
date_decided: 2025-05-08
docket: 24-30457
authority_weight: "Binding in-circuit — 5th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2025-05-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. August
  varies_by_point: false
  scope_note: "Recent published 5th Circuit decision; good law in-circuit."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10574922/united-states-v-august/"
  cluster_id: 10574922
  opinion_id: 11041510
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Recent development (role-based)"
related: ["[[Maryland v. Buie]]", "[[United States v. Conner]]"]
aliases: []
tags: ["case", "fourth-amendment", "protective-sweep", "securing-the-scene"]
holding: "(Binding in-circuit — 5th Cir.; Persuasive (outside circuit)) Articulates a four-part protective-sweep test and extends *Buie*'s officer-safety rationale to curtilage and to a non-arrest, investigatory entry."
lake:
  record_id: United States v. August
  status: verified
  projected_at: 2026-07-06
---

# United States v. August

*136 F.4th 595 (5th Cir. 2025)* · U.S. Court of Appeals, 5th Circuit · **Binding in-circuit — 5th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A neighbor told officers she had just seen August — a felon — firing a handgun in his fenced backyard, that he did so frequently, and that stray bullets had struck her home. Officers ordered August to the fence, patted him down (no weapon), and entered the backyard to conduct a [[Securing the Scene|protective sweep]], finding spent shell casings. Unable to locate the firearm and doubting August's claim that the house was empty, they swept the home (finding a magazine) and searched his car (finding methamphetamine in plain view), then obtained and executed a search warrant.

## Issue
Whether the protective-sweep doctrine justified the warrantless sweeps of August's [[Curtilage|curtilage]] (backyard) and home during a non-arrest, investigatory encounter.

## Rule
The court applied the circuit's four-part protective-sweep test, extending it by its terms to [[Curtilage|curtilage]]: "A protective sweep is lawful if: (1) the government agents have a legitimate law enforcement purpose for being in the house [or curtilage]; (2) the sweep is supported by a reasonable, articulable suspicion that the area to be swept harbors an individual posing a danger to those on the scene; (3) the sweep is no more than a cursory inspection of those spaces where a person may be found; and (4) the sweep lasts no longer than is necessary to dispel the reasonable suspicion of danger and lasts no longer than the police are justified in remaining on the premises." — slip op., at 5 (quoting *United States v. Mendez*, 431 F.3d 420, 428 (5th Cir. 2005)). ^pin-op5

## Application
On these facts the officers had a legitimate law-enforcement purpose in the backyard and home (investigating reported illegal gunfire by a felon while awaiting a warrant), and a reasonable, articulable suspicion of danger: a reported, recently fired but unlocated firearm, a cluttered yard offering hiding spots, and August's shifting, untrustworthy statements made it reasonable to fear another person or accessible weapon. The sweeps were brief and cursory inspections of spaces where a person could hide. Because each element was satisfied — including in the [[Curtilage|curtilage]] — the warrantless protective sweeps were reasonable, and the shell casings and other evidence were not suppressed.

## Conclusion
The protective sweeps of August's backyard and home were lawful and the evidence was admissible; the district court's denial of suppression was affirmed. In the Fifth Circuit, the protective-sweep doctrine's four-part test extends to [[Curtilage|curtilage]] and to non-arrest, investigatory entries supported by articulable suspicion of danger.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 5th Cir.**
- *August* extends the officer-safety protective-sweep rationale of [[Maryland v. Buie]] beyond the arrest context to [[Curtilage|curtilage]] and investigatory entries, applying the circuit's *Mendez* four-part test.

## Appears on
- [[Securing the Scene]] — *Recent development (role-based)*

## Sources
- *United States v. August*, 136 F.4th 595 (5th Cir. 2025) — https://www.courtlistener.com/opinion/10574922/united-states-v-august/ — pinpoint: slip op., at 5 (CL carries the slip opinion; cluster 10574922 → opinion 11041510).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4d691f92f9ec0c36", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "136 F.4th 595 (2025)", "court": "U.S. Court of Appeals, 5th Circuit", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. August", "year": "2025"}}
{"assertion_id": "023d2596aa28e109", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Recent development (role-based)", "title": "United States v. August"}}
{"assertion_id": "ca3ed85b2ba019c5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "(Binding in-circuit — 5th Cir.; Persuasive (outside circuit)) Articulates a four-part protective-sweep test and extends *Buie*'s officer-safety rationale to curtilage and to a non-arrest, investigatory entry.", "title": "United States v. August"}}
{"assertion_id": "8547d170ae6af91c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2025-05-08", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. August", "field_i_validity": "good_law", "scope_note": "Recent published 5th Circuit decision; good law in-circuit.", "title": "United States v. August", "varies_by_point": "false"}}
{"assertion_id": "ee85ddcc66849d2c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 5th Cir.", "title": "United States v. August"}}
```

### lake record — United States v. August

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. August",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. August",
    "case_name_short": "August",
    "case_name_full": "",
    "input_case_name": "United States v. August",
    "court": "U.S. Court of Appeals, 5th Circuit",
    "court_id": "ca5",
    "court_level": "coa",
    "circuit": "5th",
    "state": null,
    "date_decided": "2025-05-08",
    "year": 2025,
    "docket": "24-30457",
    "cluster_id": 10574922,
    "lead_opinion_id": 11041510,
    "sibling_ids": [
      11041510
    ],
    "absolute_url": "/opinion/10574922/united-states-v-august/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "136 F.4th 595",
      "volume": "136",
      "reporter": "F.4th",
      "page": "595",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "136 F.4th 595",
        "volume": "136",
        "reporter": "F.4th",
        "page": "595",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "136 F.4th 595",
    "official_selection": {
      "court_class": "coa",
      "selected": "136 F.4th 595",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op5",
      "page": null,
      "quote": "--- # United States v. August *136 F.4th 595 (5th Cir. 2025)* \u00b7 U.S. Court of Appeals, 5th Circuit \u00b7 **Binding in-circuit \u2014 5th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A neighbor told officers she had just seen August \u2014 a felon \u2014 firing a handgun in his fenced backyard, that he did so frequently, and that stray bullets had struck her home. Officers ordered August to the fence, patted him down (no weapon), and entered the backyard to conduct a protective sweep, finding spent shell casings. Unable to locate the firearm and doubting August's claim that the house was empty, they swept the home (finding a magazine) and searched his car (finding methamphetamine in plain view), then obtained and executed a search warrant. ## Issue Whether the protective-sweep doctrine justified the warrantless sweeps of August's curtilage (backyard) and home during a non-arrest, investigatory encounter. ## Rule The court applied the circuit's four-part protective-sweep test, extending it by its terms to curtilage:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2025-05-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. August",
    "varies_by_point": false,
    "scope_note": "Recent published 5th Circuit decision; good law in-circuit.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(11041510) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca5)",
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
        "query": "cites:(11041510)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(11041510)",
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
    "complete_query": "cites:(11041510)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 11041510,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-august.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 11041510,
        "cited_id": 9280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 39963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 49000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 65023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 69228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 71470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 178767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 527826,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 596417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 775796,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 785402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 4159168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 4177578,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9414811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9429766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9431933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9436658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 11041510,
        "cited_id": 9802250,
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
    "date_created": "2026-07-05T22:24:27Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T22:25:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T22:24:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. August

```
Case: 24-30457       Document: 68-1      Page: 1     Date Filed: 05/08/2025




        United States Court of Appeals
             for the Fifth Circuit                                  United States Court of Appeals
                                                                             Fifth Circuit
                             ____________                                  FILED
                                                                        May 8, 2025
                              No. 24-30457
                                                                      Lyle W. Cayce
                             ____________
                                                                           Clerk
United States of America,

                                                          Plaintiff—Appellee,

                                    versus

Kirk August,

                                        Defendant—Appellant.
               ______________________________

               Appeal from the United States District Court
                  for the Western District of Louisiana
                         USDC No. 2:23-CR-23-1
               ______________________________

Before King, Jones, and Oldham, Circuit Judges.
Edith H. Jones, Circuit Judge:
       Kirk August pled guilty to one count of possession of a firearm by a
convicted felon in violation of 18 U.S.C. § 922(g)(1). He reserved the right
to argue in this appeal that the district court should have granted his motion
to suppress evidence. Finding no error, we AFFIRM.
                       I. Factual Background
       On May 14, 2022, the Lake Charles Police Department received a call
about gunshots on the 700 block of N. Lyons Street, a residential street in
Lake Charles, Louisiana.     Officers Baccigalopi, Bernat, and Rainwater
 Case: 24-30457          Document: 68-1          Page: 2      Date Filed: 05/08/2025




                                       No. 24-30457


responded. Baccigalopi arrived on scene and spoke with the caller, who
pointed him to the blue home where August resided.
        Baccigalopi, Bernat, and Rainwater descended on the home at
virtually the same time. Baccigalopi and Bernat approached August’s home
through the next-door neighbor’s property, and they encountered August
standing in his backyard behind a chain-link fence. The backyard was
cluttered with junk, which officers believed gave August ample cover to hide
a weapon. A top-down convertible was parked in his driveway with the
driver-side door left ajar and music playing from the radio. Mattresses were
stacked against the main door to the home, preventing it from being used as
an entrance.
        Baccigalopi spoke with August while still standing on the neighbor’s
side of the fence. He asked August whether he had heard gunshots or had
any “weapons or anything” on the property. August responded “no” to
both of Baccigalopi’s questions. Meanwhile, Rainwater had gotten held up
in a conversation with the next-door neighbor, who explained to Rainwater
that she had “just now” seen August firing a handgun in his backyard.1 The
neighbor also stated that August discharged firearms in his backyard
frequently, and that stray bullets had previously struck her home. Rainwater
promptly informed his colleagues that August might have a firearm.2



        _____________________
        1
          Rainwater had assisted in executing a search warrant at August’s home a year
earlier when police located a .22 revolver in the home.
        2
          This information was enough to give the officers reasonable suspicion that a crime
had been committed. La. Rev. Stat. 14:94 prohibits the discharge of a firearm in a
residential neighborhood. See United States v. LeJeune, 2021 WL 3926154, at *2
(W.D. La. 2021). And the officers were all aware soon after arriving at the scene that
August was a felon barred from possessing a firearm.




                                             2
Case: 24-30457        Document: 68-1       Page: 3   Date Filed: 05/08/2025




                                 No. 24-30457


       Baccigalopi—still on the neighbor’s side of the fence—then ordered
August to walk backward with his hands on his head toward the fence.
August was patted down, and no weapon was found on his person. He
remained near the fence this entire time. Rainwater and Bernat entered the
backyard and began conducting a protective sweep. Bernat testified that they
entered the backyard “mostly” for safety reasons: “There was a lot of junk
behind the house . . . So if he did have a firearm within close proximity, I’d
rather be on that side.” During the protective sweep, Bernat discovered shell
casings on the ground and a large sign riddled with bullet holes. He returned
to where August was standing and handcuffed him. August continued to
contend that there was no gun on the property.
       The government maintains that officers next decided to seek a warrant
authorizing them to search the property. The officers knew they would have
to remain at the scene while they waited for the warrant application’s
approval. Given that none of them had been able to locate the alleged
firearm—and having little reason to trust August’s claim that the house was
empty—police decided to conduct a protective sweep of the home. But the
only accessible door was locked. August told police that his sister had the
only set of keys, which contradicted his previous statement that he had been
taking a bath before police arrived.
       Baccigalopi walked over to the vehicle parked in the driveway and
removed August’s keys from the ignition. While doing so, Baccigalopi
noticed a baggie of methamphetamine in plain view near the center console.
August was secured in the back of Baccigalopi’s police vehicle. Officers then
used the keys that were retrieved from the car to enter a side door of the
house and conduct a protective sweep. The sweep lasted approximately
three minutes, during which the officers located a magazine clip for a firearm.
Baccigalopi and Bernat returned to the convertible. Bernat found a gray




                                       3
Case: 24-30457        Document: 68-1        Page: 4    Date Filed: 05/08/2025




                                  No. 24-30457


plastic bag containing ammunition inside the side pocket of the open driver’s
door. Bernat stated that the ammunition itself was not in plain view.
       Satisfied that they were not in imminent danger by remaining on the
scene, police formally requested a search warrant for August’s entire
property. They remained on the scene until after they received and executed
the warrant. Their search of August’s property ultimately yielded a .22
caliber rifle, .410 shotgun, and ammunition.
                    II. Procedural Background
       August was charged with violating 18 U.S.C. § 922(g)(1) for
knowingly possessing a firearm in and affecting commerce while knowing he
had been convicted of a crime punishable by imprisonment for a term
exceeding one year. The district court denied a motion by August to dismiss
the indictment. August moved to suppress nearly all of the relevant evidence:
(1) shell casings found in the backyard; (2) the magazine clip found in the
home; (3) ammunition found in the car; and (4) firearms found in the home.
A magistrate judge issued a report and recommendation that suggested the
district court should deny the motion to suppress, reasoning that protective
sweeps of the backyard and home were justified by exigent circumstances,
and that any constitutional defect pertaining to the car search was excused
under the independent source doctrine. The district court adopted the
report and recommendation in full. August pled guilty but reserved the right
to argue that the district court should have granted his motion to suppress.
The district court sentenced August to 63 months in prison and three years
of supervised release.
                         III. Standard of Review
       When considering a district court’s denial of a motion to suppress,
this court reviews the district court’s factual findings for clear error and legal
conclusions de novo. United States v. Pack, 612 F.3d 341, 347 (5th Cir. 2010).




                                        4
Case: 24-30457       Document: 68-1       Page: 5    Date Filed: 05/08/2025




                                 No. 24-30457


A few words on the Fourth Amendment doctrines that the district court
relied on, and then on how the standard of review applies to those doctrines.
                       A. Protective Sweep Doctrine
       Under the protective sweep doctrine, police may conduct, without a
warrant, “a quick and limited search of premises for the safety of the agents
and others present at the scene.” United States v. Mendez, 431 F.3d 420, 428
(5th Cir. 2005) (citation omitted). A protective sweep is lawful if:
       (1) the government agents have a legitimate law enforcement
       purpose for being in the house [or curtilage]; (2) the sweep is
       supported by a reasonable, articulable suspicion that the area
       to be swept harbors an individual posing a danger to those on
       the scene; (3) the sweep is no more than a cursory inspection
       of those spaces where a person may be found; and (4) the sweep
       lasts no longer than is necessary to dispel the reasonable
       suspicion of danger and lasts no longer than the police are
       justified in remaining on the premises.
Id. (internal quotation marks and citation omitted). See also United States v.
Mendoza–Burciaga, 981 F.2d 192, 196 (5th Cir. 1992) (explaining that exigent
circumstances provide officers a legitimate law enforcement purpose to
conduct a warrantless entry when “officers reasonably fear for their safety,
where firearms are present, or where there is risk of a criminal suspect's
escaping or fear of destruction of evidence”) (citations omitted).
       In evaluating the legality of a protective sweep conducted because of
exigent circumstances, courts consider how “the scene of the search . . .
would appear to reasonable and prudent men standing in the shoes of the
officers.” United States v. Menchaca-Castruita, 587 F.3d 283, 290 (5th Cir.
2009) (internal quotation marks and citation omitted). Where “reasonable
minds could differ on [] whether the sweep was warranted,” courts “do not




                                      5
Case: 24-30457       Document: 68-1        Page: 6    Date Filed: 05/08/2025




                                 No. 24-30457


second-guess the judgment of experienced law enforcement officers
concerning the risks in a particular situation.” United States v. Silva, 865
F.3d 238, 242 (5th Cir. 2017) (citation omitted).
       In the context of appellate review, protective sweep cases present
mixed questions of law and fact, with the ultimate issue of whether there was
reasonable suspicion of danger being subject to de novo review. United States
v. Scroggins, 599 F.3d 433, 441 (5th Cir. 2010). This court, however, “view[s]
the evidence [going toward reasonable suspicion] in the light most favorable
to the party prevailing below, which in this case is the Government,” and
gives “due weight to inferences drawn from those facts by . . . local law
enforcement officers.”      United States v. Henry, 853 F.3d 754, 756
(5th Cir. 2017) (internal quotation marks and citations omitted).
                     B. Independent Source Doctrine
       Under the independent source doctrine, “‘information which is
received through an illegal source is considered to be cleanly obtained when
it arrives through an independent source.’” United States v. Hearn, 563 F.3d
95, 102 (5th Cir. 2009) (quoting Murray v. United States, 484 U.S. 533, 538–
39, 108 S. Ct. 2529, 2534 (1988)). This court conducts a two-step analysis to
determine whether the independent source doctrine cures an issue when
police subsequently obtain a warrant, asking whether (1) “the warrant
affidavit, when purged of tainted information gained through the initial
illegal entry, contain[ed] sufficient remaining facts to constitute probable
cause”; and (2) “the illegal search affect[ed] or motivate[d] the officers’
decision to procure the search warrant.” Id. (citation omitted).
       In the context of appellate review, this court reviews de novo a district
court’s determination that a search warrant affidavit establishes probable
cause after the warrant has been purged of potentially “tainted” information,
and it reviews for clear error a district court’s findings regarding whether an




                                       6
Case: 24-30457         Document: 68-1       Page: 7   Date Filed: 05/08/2025




                                No. 24-30457


unlawful prior search or entry motivated officers’ decision to obtain a
warrant. See United States v. Hassan, 83 F.3d 693, 697 (5th Cir. 1996)
(citations omitted).
                              IV. Analysis
       August contends that law enforcement erred at every step of their
operation: (1) the protective sweep of his backyard; (2) the protective sweep
of his home; (3) searches of his car; and therefore (4) the execution of a
search warrant in his home. His claims pertaining to each of these searches
are considered in turn.
                   A. Protective Sweep of the Backyard
       August argues that the protective sweep doctrine did not justify the
search of his backyard because police hopped the gate and did not stay nearby
to prevent him from grabbing a weapon but continued to search beyond his
immediate vicinity. August does not cite an apposite case to support his
argument that the protective sweep of his backyard was unlawful. His
argument fails.
       August was not arrested until after law enforcement officers had
located shell casings and concluded their protective sweep of his yard. He
acknowledged in his objection to the report and recommendation that his
lawn was “surrounded by hurricane fencing and filled with spillover objects
from the home’s interior.” Without a protective sweep of the entire
backyard, it remained possible that someone else might be present, or that
August’s questioning might end without an arrest, at which point he could
have accessed a firearm hidden in the yard.
       Police had reasons to distrust August’s insistence that there was no
firearm on the property: their knowledge of his felon status, and his direct
contradictions during their limited encounter. And the presence of a gray




                                        7
Case: 24-30457        Document: 68-1       Page: 8     Date Filed: 05/08/2025




                                  No. 24-30457


convertible in the driveway—top down, driver door left ajar, keys still in the
ignition, and music playing from the radio—was potentially suggestive of a
recent visitor’s arrival or a third party’s presence, especially because August
claimed he had just been taking a bath before officers arrived. The chaos,
contradictions, and incredible story that August attempted to sell the
officers, when considered together and in the light most favorable to the
government, made it completely reasonable for police to fear that someone—
or something—else hiding in August’s backyard posed a serious threat to
their safety.
       August has failed to show that the protective sweep of his backyard
was unlawful. The district court did not err in its refusal to suppress the spent
shell casings.
                     B. Protective Sweep of the Home
       August argues that the protective sweep doctrine did not justify a
search of his home because “officers had been safely outside the home for
almost seven minutes” when they decided to enter, “officers had already
isolated August,” and “there was nothing to suggest that destruction of
evidence was likely or that anyone even remained in the home.” His
argument relies primarily on United States v. Manchaca-Castruita, 587 F.3d
283 (5th Cir. 2009), where this court held that exigent circumstances could
not justify police sweeping a home suspected of storing illegal marijuana
because there was no evidence that any person remained inside the home,
officers stood safely outside with bystanders even further removed from the
home, and a search warrant could readily have been obtained. Id. at 294–95.
       This case is different. Unlike Manchaca-Castruita, (1) the suspected
contraband—firearms—could be used to jeopardize the safety of law
enforcement; (2) the suspect had not left the home, denied any personal
knowledge of a firearm, and contradicted himself to police, and a car




                                       8
Case: 24-30457        Document: 68-1       Page: 9     Date Filed: 05/08/2025




                                  No. 24-30457


appeared to have recently arrived, which introduced the possibility that
another person on the property possessed a firearm; (3) there were no
witnesses who had been inside of August’s home to confirm whether
accomplices were inside; (4) the door to August’s home was closed,
suggesting there was no last-minute escape; (5) nobody at the property
received a warning that law enforcement was being contacted, likely
frustrating plans for a last-minute escape; (6) the spent shell casings in the
backyard confirmed that a firearm had probably been discharged at some
point on the property; and (7) the incident occurred on the weekend,
potentially making it more difficult for officers to communicate with a
magistrate and to obtain a search warrant. See id. at 285–88, 294.
       Case law tends to reflect that exigent circumstances are unlikely to
exist if there is “no articulable reason to believe that someone else might be
inside [the] residence.” Id. at 295. See also United States v. Carter, 360 F.3d
1235, 1241 (10th Cir. 2004) (granting motion to suppress) (“[T]he
government points to no reason to believe that other people were in the
garage, or even the house.”) (emphasis added). The outcome is typically
different, though, if law enforcement had at least a reasonable belief that
another dangerous person might be hiding in the residence that they decided
to sweep. See United States v. Watson, 273 F.3d 599, 603 (5th Cir. 2001) (“A
protective sweep of a suspect’s house may be made . . . if the arresting officers
‘have reasonable grounds to believe that there are other persons present
inside who might present a security risk.’”) (quoting United States v. Merritt,
882 F.2d 916, 921 (5th Cir. 1989) (internal citation omitted)); United States
v. Maldonado, 472 F.3d 388, 394 (5th Cir. 2006) (determining that a
protective sweep was justified based in part on the fact that agents were
exposed in an open area surrounding a trailer with “no certain knowledge”
whether others might be in the trailer) (subsequent history omitted).




                                       9
Case: 24-30457        Document: 68-1         Page: 10    Date Filed: 05/08/2025




                                   No. 24-30457


       It cannot be said that police had no articulable reason to fear that
someone remained in August’s home. After sweeping his backyard, the
officers knew that (1) at least two neighbors heard gunshots, and the next-
door neighbor reported seeing someone on the property firing a weapon;
(2) spent shell casings littered the backyard; (3) August had little to no
credibility; (4) a car that looked as if it had just arrived was parked in the
driveway; and (5) most entry points to the house were barricaded. See, e.g.,
United States v. Cousins, 841 F. App’x 885, 899 (7th Cir. 2021) (noting that
an occupant’s “nervous” and “evasive” demeanor when questioned by
officers supported a protective sweep of a home, especially when police are
already aware of a firearm’s presence on the property).             It makes no
difference that officers chose to investigate these concerns only after
arresting August. See Maryland v. Buie, 494 U.S. 325, 333 (1990) (“[T]here
is an analogous interest . . . in [officers] taking steps to assure themselves that
the house in which a suspect . . . has just been[] arrested is not harboring other
persons who are dangerous and who could unexpectedly launch an attack.”).
Any remaining doubt as to the reasonableness of the officers’ concerns is
dispelled by the deferential review that police are entitled to in this context.
See Silva, 865 F.3d at 242 (protective sweep standard) (where “reasonable
minds could differ on . . . whether the sweep was warranted,” a court will not
“second-guess the judgment of experienced law enforcement officers”);
Henry, 853 F.3d at 756 (appellate review standard) (this court views the
evidence going toward reasonable suspicion “in the light most favorable to
the party prevailing below,” and gives “due weight to inferences drawn from
those facts by . . . local law enforcement officers”).




                                        10
Case: 24-30457         Document: 68-1         Page: 11    Date Filed: 05/08/2025




                                    No. 24-30457


         August has failed to show that the protective sweep of his home was
unlawful. The district court did not err in its refusal to suppress the magazine
clip.3
                             C. Searches of the Car
         August argues that law enforcement twice violated the Fourth
Amendment in connection with their searches of the car parked in his
driveway. Officer Baccigalopi walked over to the car and retrieved the keys
from the ignition after August claimed that his sister had the only key to the
house. He noticed a baggie of illicit drugs when he reached for the keys.
Police returned after sweeping the backyard and the home. They conducted
a more thorough search of the car, recovering methamphetamine and
ammunition.      The magistrate judge held that the independent source
doctrine excused any constitutional defect in these searches of the car
without analyzing whether the searches were in fact constitutional. We
similarly limit our discussion to applicability of the independent source
doctrine due to insufficient briefing as to whether (1) the protective sweep
doctrine could justify the police entering the car, (2) the driver’s side door’s
being left open removed any expectation of privacy, or (3) either the
protective sweep doctrine or plain view doctrine authorized law enforcement
to acquire the keys.
         August argues that the independent source doctrine cannot cure
defects in the car searches because (1) there would be no probable cause
supporting the warrant without the magazine clip (which was obtained using
the house keys that were retrieved during the first car search) and
ammunition (which was recovered during the second car search), and (2) the

         _____________________
         3
          The magazine clip was alternatively admissible under the independent source
doctrine as discussed below.




                                         11
Case: 24-30457           Document: 68-1           Page: 12      Date Filed: 05/08/2025




                                       No. 24-30457


magazine clip and ammunition compelled the officers to pursue a search
warrant.4 His argument proves unpersuasive.
        First, aside from mentioning the magazine clip and ammunition, the
search warrant affidavit noted that law enforcement officers responded to a
report of multiple shots fired in the area; another witness advised police
officers that she observed the resident of 710 N. Lyons outside with a firearm;
officers observed multiple spent shell casings on the property of the
residence; officers located Kirk August at the residence; and officers
confirmed that August stays at the residence.
        “Probable cause does not require proof beyond a reasonable doubt.”
United States v. Perez, 484 F.3d 735, 740 (5th Cir. 2007). “[A] magistrate
need only have a substantial basis for concluding that a search would uncover
evidence of wrongdoing.” Id. Scrubbed of the allegedly tainted magazine
clip and ammunition, and considering the issue de novo, the warrant affidavit
still contained sufficient remaining facts to provide the magistrate a
substantial basis for concluding that a search would uncover evidence of
wrongdoing.        The magistrate could reasonably infer from eyewitness
testimony and shell casings on the property that August had discharged a
firearm in violation of Louisiana law.5

        _____________________
        4
          August also argues that the search warrant would not have been granted without
police locating the shell casings in his backyard. However, police clearly did not violate the
Constitution in conducting the protective sweep that produced the shell casings.
        5
          Cf. United States v. Coleman, 540 F. Supp. 3d 596, 611 (S.D. Miss. 2021) (holding
that search warrant was not supported by probable cause) (“The affidavit includes the
informant’s statement that Coleman discharged a firearm on the property against an
intruder ‘several weeks ago.’ But the affiant does not state how the informant obtained this
information, whether by personal observations or from an eyewitness.”); United States v.
Wooldridge, 2016 WL 11473559, at *6 (E.D. Tex. Apr. 22, 2016) (same) (“Here, the search
warrant affidavit describes in detail the particular place to be searched and is appropriately
limited in scope[.] However, the affidavit fails to provide the state judge with facts from




                                             12
Case: 24-30457         Document: 68-1          Page: 13     Date Filed: 05/08/2025




                                    No. 24-30457


       Second, August contends “it was not until after the officers searched
the home and car, finding a magazine and ammunition, that the officers
requested a search warrant.” But the district court’s determination that the
“tainted” magazine clip and ammunition evidence did not influence the
officers is a finding of fact that must stand unless clearly erroneous. And
there is ample evidence in the record to support it. For example, officers
arrested August immediately after they located spent shell casings in the
backyard. At that point, probable cause existed to obtain a proper search
warrant. Police retrieved house keys to access the home and reported that
they swept the home to secure the area while they waited for a search
warrant. This narrative accords with the warrant affidavit, which noted that
officers “cleared the residence . . . for safety and to check for any injured
parties.”     August has not identified any substantial evidence that
undermines this narrative.         The district court did not clearly err by
determining that officers decided to seek a search warrant after they
discovered the spent shell casings but before they discovered the magazine
clip or ammunition.
       To summarize why the district court did not err in applying the
independent source doctrine: The magazine clip and ammunition were not
necessary to establish probable cause and did not motivate the officers to
obtain a search warrant. The magistrate issued a search warrant that
authorized police to search all property located at 710 N. Lyons Street,
including the “interior of the residence, vehicles located on the property,
and curtilage of the property.” This encompassed the areas where the
magazine clip and ammunition were located. The independent source
doctrine permits the magazine clip and ammunition to be introduced as
       _____________________
which he could infer that the firearm was contraband, that it had been used in a crime,
and/or that it was linked to any wrongdoing.” (citation omitted)).




                                          13
Case: 24-30457       Document: 68-1         Page: 14   Date Filed: 05/08/2025




                                  No. 24-30457


evidence in these circumstances regardless whether the initial car searches
were lawful.
                      D. Execution of Search Warrant
       The district court correctly allowed the firearms to be admitted into
evidence because the firearms were recovered through the execution of a
valid search warrant that was obtained without regard to bad acts by law
enforcement. The district court could have alternatively admitted the
“smoking gun” in this case under the good-faith exception to the
exclusionary rule. Under that exception, “if the evidence was obtained by
law enforcement officers who relied on the warrant in objectively reasonable
good-faith, then the evidence obtained during the search is admissible.”
United States v. Allen, 625 F.3d 830, 835 (5th Cir. 2010) (citation omitted).
“This is true even if the evidence in the affidavit . . . was not sufficient to
establish probable cause.” Id.
       August offers scant evidence of bad faith, primarily relying on
exchanges captured by officer body-cam footage that indicate several officers
had a negative opinion of August due to previous interactions with him. But
this evidence fails to move the needle because the good-faith inquiry is
strictly objective. See United States v. Massi, 761 F.3d 512, 530 (5th Cir. 2014)
(“In determining whether the good faith exception applies, ‘we do not
attempt an “expedition into the minds of police officers” to determine their
subjective beliefs regarding the validity of the warrant.’” (citations
omitted)).
       August does not even attempt to allege that it was objectively
unreasonable to rely on the warrant. Nor could he. This is not a case in
which “the magistrate . . . was misled by information in an affidavit that the
affiant knew was false or would have known was false except for his reckless
disregard of the truth.” United States v. Leon, 468 U.S. 897, 923, 104 S. Ct.




                                       14
Case: 24-30457        Document: 68-1         Page: 15   Date Filed: 05/08/2025




                                  No. 24-30457


3405, 3421 (1984) (citation omitted). It is not a case in which the issuing
magistrate “wholly abandoned his judicial role,” or the warrant was based on
an affidavit “so lacking in indicia of probable cause as to render official belief
in its existence entirely unreasonable.” Id. (internal quotation marks and
citations omitted). And it is not a case in which the warrant is “so facially
deficient . . . that the executing officers [could not] reasonably presume it to
be valid.” Id. The good-faith exception therefore supports admitting the
firearms into evidence even if there were a defect in the warrant.
                              V. Conclusion
       For the foregoing reasons, the judgment of the district court is
AFFIRMED.




                                        15

```

---
