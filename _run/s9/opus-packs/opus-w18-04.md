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

## GROUP: _overhaul2/lake/cases/United States v. Oliveras.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Oliveras
type: case
citation: "96 F.4th 298 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 2d Cir. 2024
court_level: coa
circuit: ca2
year: 2024
date_decided: 2024-03-15
docket: 21-2954
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
  opinion_url: "https://www.courtlistener.com/opinion/9484364/united-states-v-oliveras/"
  cluster_id: 9484364
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Oliveras
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: Key
related:
  - "[[Special Needs and Administrative Searches]]"
  - "[[Griffin v. Wisconsin]]"
  - "[[Samson v. California]]"
  - "[[United States v. Knights]]"
tags:
  - case
  - fourth-amendment
  - special-needs
  - supervised-release
  - suspicionless-search
  - probation
  - second-circuit
holding: "Under the special-needs doctrine, a district court may impose a special condition of supervised release authorizing a probation officer to conduct suspicionless searches of the defendant's person, property, vehicle, or residence, where the record sufficiently supports it under 18 U.S.C. § 3583(d); but because the district court here made no individualized assessment tying the search condition to the statutory factors, the condition was vacated and remanded even though the special-needs authorization itself was sound."
aliases:
  - United States v. Oliveras
  - "United States v. Oliveras (2d Cir. 2024)"
---

# United States v. Oliveras

*96 F.4th 298 (2d Cir. 2024)* (No. 21-2954) · U.S. Court of Appeals for the Second Circuit · **Binding in-circuit — 2d Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 9484364 → lead opinion 9950977 (96 F.4th 298, decided 2024-03-15; panel Lynch, Bianco, Pérez, JJ.); Rule quote string-matched to the CL opinion text 2026-07-07 (slip-style pin per S2 A3 — CL text is slip-paginated). S9 promotes. -->

## Background
Alex Oliveras pleaded guilty in the Western District of New York to possessing cocaine with intent to distribute and to possessing a firearm in furtherance of drug trafficking, and was sentenced principally to sixty-three months' imprisonment followed by a three-year term of supervised release. Among the conditions of that release, the district court imposed a special "Search Condition" subjecting Oliveras to suspicionless searches of his person, property, vehicle, residence, or any other property under his control by a probation officer. His sole contention on appeal was that the suspicionless-search condition violated the Fourth Amendment.

## Issue
Whether the "special needs" doctrine permits a district court to impose a special condition of supervised release authorizing a probation officer to conduct suspicionless searches of a supervisee, and whether the condition imposed here was adequately justified.

## Rule
The "special needs" of a supervision system — beyond ordinary law enforcement — can justify departures from the usual warrant and probable-cause requirements, and a supervisee's diminished expectation of privacy makes suspicionless conditions permissible when the record supports them. The panel held: "We conclude that the 'special needs' doctrine of the Fourth Amendment permits, when sufficiently supported by the record, the imposition of a special condition of supervised release that allows the probation officer to conduct a suspicionless search of the defendant's person, property, vehicle, place of residence, or any other property under his or her control." — 96 F.4th 298, slip op. at 2. ^pin-op2

## Application
The Second Circuit rejected Oliveras's categorical Fourth Amendment challenge: recognizing the diminished privacy interests of supervisees and the special needs of probation officers in fulfilling their supervisory role, a suspicionless-search condition can be imposed if sufficiently supported by the record under the § 3583(d) factors. But the doctrine's availability did not save this condition. The district court had made no individualized assessment explaining how a suspicionless-search requirement was reasonably related to the applicable statutory factors in Oliveras's particular case. Because that individualized justification was missing, the court held that imposing the condition exceeded the district court's discretion, [[Reading and Citing Cases#vacated|vacated]] the condition, and [[Reading and Citing Cases#on-remand|remanded]] for the required particularized findings.

## Conclusion
The special-needs authorization for suspicionless supervised-release search conditions was **upheld in principle**, but the condition imposed on Oliveras was **[[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]]** for an individualized § 3583(d) assessment. The panel comprised Lynch, Bianco, and Pérez, Circuit Judges.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Oliveras* extends the *[[Griffin v. Wisconsin|Griffin]]*/*[[Samson v. California|Samson]]*/*[[United States v. Knights|Knights]]* line — the **special-needs / diminished-expectation** rationale for supervising probationers and parolees — to hold that a **suspicionless** search condition is permissible on federal **supervised release** when adequately supported. Teach the two moves separately: the doctrine authorizes such a condition, but § 3583(d) still requires a case-specific, individualized justification before it may be imposed.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key*

## Sources
- [*United States v. Oliveras*, 96 F.4th 298 (2d Cir. 2024)](https://www.courtlistener.com/opinion/9484364/united-states-v-oliveras/) — pinpoint: slip op. at 2 (special-needs authorization of a suspicionless supervised-release search condition; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0045bd22a5b21e2c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Oliveras"}, "payload": {"all": [{"cite": "96 F.4th 298", "page": "298", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}], "display": "96 F.4th 298", "official": {"cite": "96 F.4th 298", "page": "298", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "96"}, "official_selection_present": true, "record_id": "United States v. Oliveras"}}
{"assertion_id": "de21483445b1a924", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Oliveras"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Oliveras", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Oliveras

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Oliveras",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Oliveras",
    "case_name_short": "Oliveras",
    "case_name_full": "",
    "input_case_name": "United States v. Oliveras",
    "court": "2d Cir. 2024",
    "court_id": "ca2",
    "court_level": "coa",
    "circuit": "ca2",
    "state": null,
    "date_decided": "2024-03-15",
    "year": 2024,
    "docket": "21-2954",
    "cluster_id": 9484364,
    "lead_opinion_id": 9950977,
    "sibling_ids": [],
    "absolute_url": "/opinion/9484364/united-states-v-oliveras/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "96 F.4th 298",
      "volume": "96",
      "reporter": "F.4th",
      "page": "298",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "96 F.4th 298",
        "volume": "96",
        "reporter": "F.4th",
        "page": "298",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "96 F.4th 298",
    "official_selection": {
      "court_class": "state",
      "selected": "96 F.4th 298",
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
    "date_created": "2026-07-06T05:57:05Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:57:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-oliveras--9484364",
      "to_record_id": "United States v. Oliveras",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Oliveras

```
21-2954
United States v. Oliveras


                      United States Court of Appeals
                                   for the Second Circuit
                            _____________________________________

                                        August Term 2022

                    (Argued: June 30, 2023        Decided: March 15, 2024)

                                           No. 21-2954

                            _____________________________________

                                   UNITED STATES OF AMERICA,

                                             Appellee,

                                             — v. —

                                         ALEX OLIVERAS,

                                       Defendant-Appellant.

                            _____________________________________

Before:                     LYNCH, BIANCO, AND PÉREZ, Circuit Judges.

       Defendant-Appellant Alex Oliveras appeals from a judgment of the United
States District Court for the Western District of New York (Arcara, J.), entered
November 23, 2021, following his guilty plea, sentencing him principally to sixty-
three months’ imprisonment and a three-year supervised release term for
possessing cocaine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and
(b)(1)(C), and possessing a firearm in furtherance of drug trafficking in violation
of 18 U.S.C. § 924(c)(1)(A)(i). Oliveras’s sole contention on appeal is that the
imposition of a special condition of supervised release that subjects him to
suspicionless searches by a probation officer (the “Search Condition”) violates the
Fourth Amendment.

       We conclude that the “special needs” doctrine of the Fourth Amendment
permits, when sufficiently supported by the record, the imposition of a special
condition of supervised release that allows the probation officer to conduct a
suspicionless search of the defendant’s person, property, vehicle, place of
residence, or any other property under his or her control. However, the district
court exceeded its discretion in imposing that special condition here because it
failed to make the individualized assessment required to support the special
condition under 18 U.S.C. § 3583(d), including a sufficient explanation as to how
the condition is reasonably related in this particular case to the applicable statutory
factors under 18 U.S.C. § 3553(a) and involves no greater deprivation of liberty
than is reasonably necessary under those factors.

       Accordingly, we VACATE the Search Condition and REMAND to the
district court for further consideration of whether it is necessary to impose the
Search Condition in this particular case and, if so, for the district court to explain
the individualized basis for imposing the Search Condition.

                                              TIFFANY H. LEE, Assistant United States
                                              Attorney, for Trini E. Ross, United
                                              States Attorney for the Western District
                                              of New York, Buffalo, NY.

                                              TIMOTHY P. MURPHY, Assistant Federal
                                              Public Defender, Federal Public
                                              Defender’s Office, Buffalo, NY.

JOSEPH F. BIANCO, Circuit Judge:

      Defendant-Appellant Alex Oliveras appeals from a judgment of the United

States District Court for the Western District of New York (Arcara, J.), entered



                                          2
November 23, 2021, following his guilty plea, sentencing him principally to sixty-

three months’ imprisonment and a three-year supervised release term for

possessing cocaine with intent to distribute in violation of 21 U.S.C. § 841(a)(1) and

(b)(1)(C), and possessing a firearm in furtherance of drug trafficking in violation

of 18 U.S.C. § 924(c)(1)(A)(i). Oliveras’s sole contention on appeal is that the

imposition of a special condition of supervised release that subjects him to

suspicionless searches by a probation officer (the “Search Condition”) violates the

Fourth Amendment.

      We conclude that the “special needs” doctrine of the Fourth Amendment

permits, when sufficiently supported by the record, the imposition of a special

condition of supervised release that allows the probation officer to conduct a

suspicionless search of the defendant’s person, property, vehicle, place of

residence or any other property under his or her control. However, the district

court exceeded its discretion in imposing that special condition here because it

failed to make the individualized assessment required to support the special

condition under 18 U.S.C. § 3583(d), including a sufficient explanation as to how

the condition is reasonably related in this particular case to the applicable statutory




                                           3
factors under 18 U.S.C. § 3553(a) and involves no greater deprivation of liberty

than is reasonably necessary under those factors.

      Accordingly, we VACATE the Search Condition and REMAND to the

district court for further consideration of whether it is necessary to impose the

Search Condition in this particular case and, if so, for the district court to explain

the individualized basis for imposing the Search Condition.

                                 BACKGROUND

      On November 27, 2018, Oliveras was charged in an indictment in the

Western District of New York with the following: two counts of possession of

cocaine with intent to distribute in violation 21 U.S.C. § 841(a)(1) and (b)(1)(C)

(Counts One and Two); one count of maintaining a drug-involved premises in

violation of 21 U.S.C. § 856(a)(1) (Count Three); one count of possession of a

firearm in furtherance of drug trafficking in violation of 18 U.S.C. § 924(c)(1)(A)(i)

(Count Four); one count of being a felon in possession of a firearm in violation of

18 U.S.C. §§ 922(g)(1) and 924(a)(2) (Count Five); and one count of possession of a

defaced firearm in violation of 18 U.S.C. §§ 922(k) and 924(a)(1)(B) (Count Six).

      On October 22, 2020, Oliveras pled guilty to Count One (possessing cocaine

with intent to distribute) and Count Four (possessing a firearm in furtherance of



                                          4
drug trafficking), pursuant to a plea agreement with the government.           On

November 23, 2021, the district court sentenced Oliveras principally to sixty-three

months’ imprisonment and a three-year supervised release term. In connection

with the supervised release term, the district court imposed the Search Condition

at issue on this appeal, to which Oliveras objected both in writing prior to the

sentencing and at the sentencing proceeding.

      Prior to Oliveras’s sentencing, the United States Probation Office prepared

a Presentence Investigation Report (“PSR”) in which it recommended a search

condition as a special condition of supervised release. The search condition

initially provided for searches “based upon reasonable suspicion.” United States

v. Oliveras, No. 18-cr-00234, Dkt. No. 82 at 23 (Initial PSR). The Probation Office

subsequently, without explanation, revised the proposed condition to remove the

reasonable suspicion requirement. See Oliveras, No. 18-cr-00234, Dkt. No. 101 at

24 (First Revised PSR). More specifically, the Search Condition provided:

      The defendant shall submit to a search of his person, property,
      vehicle, place of residence or any other property under his control,
      and permit confiscation of any evidence or contraband discovered.
      (This condition serves the statutory sentencing purposes of




                                         5
      deterrence, public      protection,       and   rehabilitation.   18   U.S.C.
      § 3553(a)(2)(B)-(D)).

Id.

      Oliveras did not object to the search condition as initially proposed.

However, in his sentencing submission, he objected to the Search Condition as

revised because it omitted reasonable suspicion as a requirement for any search

by the probation officer. See Oliveras, No. 18-cr-00234, Dkt. No. 106 at 2 (Statement

with Respect to Sentencing Factors).

      In response to Oliveras’s objection, the Probation Office submitted another

revised PSR with an addendum that explained the omission of the reasonable

suspicion language from the Search Condition by relying on this Court’s decision

in United States v. Braggs, 5 F.4th 183 (2d Cir. 2021). Specifically, the PSR stated:

      Under the special needs doctrine, a parole officer may search a
      parolee, without violating the Fourth Amendment, so long as the
      search is reasonably related to performance of the officer’s duties.
      The duties of a parole officer include the supervision, rehabilitation,
      and societal reintegration of parolees, as well as assuring that the
      community is not harmed by parolees being at large. Because a search
      undertaken by a parole officer of a parolee to detect parole violations
      is reasonably related to the parole officer's duties, such a search is




                                            6
      permissible under the special needs doctrine and accordingly
      comports with [the] Fourth Amendment.

Oliveras, No. 18-cr-00234, Dkt. No. 109 at 25 (Second Revised PSR) (citing Braggs, 5

F.4th at 184). The Second Revised PSR also relied on this Court’s reasoning in

United States v. Grimes, 225 F.3d 254 (2d Cir. 2000), and stated:

      [W]hile parolees do not surrender their constitutional protection from
      unreasonable searches and seizures, their status as parolees
      diminishes the extent of their Fourth Amendment protection.
      Parolees may be subject to warrantless searches and seizures by a
      parole officer, as long as the officer's conduct is rationally and
      reasonably related to the performance of his or her duties.

Second Revised PSR at 25. The Probation Office noted that both Braggs and Grimes

involved “individuals under a sentence of state parole supervision,” but

concluded that “the same analysis applies to a defendant who is under a sentence

of supervised release, which is the federal counterpart or equivalent of state

parole.” Id. at 25–26.

      At sentencing, the district judge rejected Oliveras’s objection, imposing the

Search Condition as a special condition of his supervised release and declining to

add the reasonable suspicion requirement.          In doing so, the district judge




                                          7
explained that he had a “problem with the reasonable suspicion requirement”

given his view regarding the nature of supervised release:

       [W]hen you're on supervised release, that [is] to allow [you] out of
       prison at an earlier time. And it seems to me that, all of a sudden, you
       have some legal rights that you would not have when you were in
       prison, and that is a search of the cell based on reasonable suspicion.
       They can search a cell any time whenever they feel.

Joint App’x at 100. The district judge stated that he was “open-minded,” but that

he was “not inclined to put the reasonable suspicion [requirement] in [his]

sentences unless somebody can point to [him] a valid reason why in a particular

case it should” be included. Id. He further clarified:

       So I’m going to not require reasonable suspicion in my sentences. I
       don’t want to say all the time. I always want to keep an open mind
       . . . . [I]t’s my intention that [in] the general case, I will provide [that]
       reasonable suspicion is not required, but I’ll keep an open mind, and
       I’ll note in this case here, I’m not going to require reasonable
       suspicion. I can tell you up front.

Id. at 100-01.

       As to the legal basis for the ruling, the district judge, referring to Braggs,

explained that this Court has “clearly indicated” that reasonable suspicion is not

required. Id. at 101. Further, the district judge stated that “even before [Braggs],”

he “was always somewhat surprised in a way that the probation office was




                                            8
requiring this reasonable suspicion requirement” and that he “just never went

along with it.” Id.

      In response, defense counsel attempted to distinguish Braggs, pointing out

that “Braggs involved a defendant who was on New York State Parole . . . . not a

defendant who was on federal supervised release.” Id. Further, defense counsel

noted that “there has not been a Second Circuit or a United States Supreme Court

decision that has expressly decided that there is anything lower than reasonable

suspicion required for the search of a person's home while on federal supervised

release.” Id. The district judge, however, maintained that reasonable suspicion

should not be required for a probation officer to search a defendant on supervised

release, particularly in this case which involved drugs. The district judge stated

his view, based upon past cases, that individuals convicted of drug offenses “often

are involved in drugs when they’re on supervised release.” Id. at 102. In addition,

the district judge noted that, because “[d]rugs are normally a surreptitious type of

thing” and are not “out in the open generally,” a probation officer should be able

to conduct a search without a showing of reasonable suspicion. Id. Accordingly,




                                         9
the district judge adopted the Search Condition as recommended by the Probation

Department, which included no requirement of individualized suspicion.

      This appeal followed.

                                  DISCUSSION

      This Court generally reviews the imposition of supervised release

conditions for abuse of discretion. United States v. Boles, 914 F.3d 95, 111 (2d Cir.

2019). “When a challenge to a condition of supervised release presents an issue of

law, however, we review the imposition of that condition de novo, bearing in mind

that any error of law necessarily constitutes an abuse of discretion.” Id. (quoting

United States v. McLaurin, 731 F.3d 258, 261 (2d Cir. 2013) (internal quotation marks

omitted)). In addition, “[w]here a condition of supervised release implicates a

constitutional right, we conduct a more searching review in light of the

‘heightened constitutional concerns’ presented in such cases.” United States v.

Eaglin, 913 F.3d 88, 95 (2d Cir. 2019) (quoting United States v. Myers, 426 F.3d 117,

126 (2d Cir. 2005)).

      On appeal, Oliveras challenges the district court’s imposition of the Search

Condition. He contends that the Search Condition is unconstitutional because

suspicionless searches by his probation officer would violate his rights under the



                                         10
Fourth Amendment. Oliveras also argues that the condition is unreasonable

because the district court did not make an individualized assessment for imposing

the Search Condition, nor sufficiently state its reasons for doing so.

      For the reasons set forth below, we conclude that a suspicionless search

condition for an individual on supervised release is permissible under the Fourth

Amendment, when supported by the record, because a supervisee has a

diminished expectation of privacy and the effective administration of supervised

release by a probation officer presents a “special need” that “permit[s] a degree of

impingement upon privacy that would not be constitutional if applied to the

public at large.” United States v. Reyes, 283 F.3d 446, 461 (2d Cir. 2002) (internal

quotation marks and citation omitted). However, we also conclude that the

district court exceeded its discretion in imposing the Search Condition here

because it did not make an individualized assessment as to the need for the

imposition of the Special Condition on Oliveras, nor did it sufficiently state its

reasons for imposing the condition.

I.    The Fourth Amendment and Search Conditions

      The Fourth Amendment protects “against unreasonable searches and

seizures.” U.S. Const. amend. IV. In determining whether a search is reasonable,



                                         11
courts must balance “the degree to which [the search] intrudes upon an

individual’s privacy” with “the degree to which it is needed for the promotion of

legitimate governmental interests.” Samson v. California, 547 U.S. 843, 848 (2006)

(internal quotation marks and citation omitted). In doing so, we are required to

“examine the totality of the circumstances.” Id. (alteration adopted) (internal

quotation marks and citation omitted). Under this approach, a search generally is

“not reasonable unless it is accomplished pursuant to a judicial warrant issued

upon probable cause.” Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S. 602, 619 (1989).

However, the “Fourth Amendment protections extend only to ‘unreasonable

government intrusions into . . . legitimate expectations of privacy.’” United States

v. Thomas, 729 F.2d 120, 122 (2d Cir. 1984) (quoting United States v. Chadwick, 433

U.S. 1, 7 (1977)).

       In particular, as relevant here, in Griffin v. Wisconsin, 483 U.S. 868, 873–74

(1987), the Supreme Court recognized that “[a] State’s operation of a probation

system . . . presents ‘special needs’ beyond normal law enforcement that may

justify departures from the usual warrant and probable-cause requirements.” In

assessing whether a special need justifies a search, we have explained that: (1)

“the government must allege a special need, the importance of which derives both



                                         12
from the particular context in which it seeks to implement searches . . . and what

the searches are designed to discover”; (2) “those subject to the search must enjoy

a diminished expectation of privacy, partly occasioned by the special nature of

their situation, and partly derived from the fact that they are notified in advance

of the search policy”; and (3) “the search program at issue must seek a minimum

of intrusiveness coupled with maximum effectiveness so that the searches bear a

close and substantial relationship to the government’s special needs.” United

States v. Lifshitz, 369 F.3d 173, 186 (2d Cir. 2004) (internal quotation marks omitted).

      Although neither the Supreme Court nor this Court has specifically

addressed the constitutionality of a suspicionless search by a probation officer of

a defendant on supervised release, we do not analyze this issue on a blank slate.

Indeed, over the last several decades, both the Supreme Court and this Court have

analyzed the Fourth Amendment standard for searches authorized in connection

with individuals under various forms of post-sentence supervision—such as

probation, parole, or supervised release. Because this case authority is instructive

in analyzing the constitutional issue presented in this appeal, we begin by

summarizing the relevant precedent in each category of supervision.




                                          13
      A.    Probation Supervision

      In United States v. Knights, 534 U.S. 112, 121–22 (2001), the Supreme Court

held that a warrantless search of a probationer’s apartment, supported by

reasonable suspicion and authorized by a probation condition, was reasonable

within the meaning of the Fourth Amendment. In reaching this decision, the

Supreme Court explained:

      Probation, like incarceration, is a form of criminal sanction imposed
      by a court upon an offender after verdict, finding, or plea of guilty.
      Probation is one point . . . on a continuum of possible punishments
      ranging from solitary confinement in a maximum-security facility to
      a few hours of mandatory community service. Inherent in the very
      nature of probation is that probationers do not enjoy the absolute
      liberty to which every citizen is entitled. Just as other punishments
      for criminal convictions curtail an offender’s freedoms, a court
      granting probation may impose reasonable conditions that deprive
      the offender of some freedoms enjoyed by law-abiding citizens.

Id. at 119 (internal quotation marks and citations omitted). The Supreme Court

emphasized that “[i]t was reasonable to conclude that the search condition would

further the two primary goals of probation—rehabilitation and protecting society

from future criminal violations.” Id. The Supreme Court also noted that, “[i]n

assessing the governmental interest side of the balance, it must be remembered

that the very assumption of the institution of probation is that the probationer is

more likely than the ordinary citizen to violate the law.” Id. at 120 (internal


                                        14
quotation marks and citation omitted). Thus, although recognizing “the hope that

[the probationer] will successfully complete probation and be integrated back into

society,” the Supreme Court held “that the balance of these considerations requires

no more than reasonable suspicion to conduct a search of [the] probationer’s

house. Id. at 120–21. The Supreme Court, however, explicitly left open the

question of “whether the probation condition so diminished, or completely

eliminated, [the probationer’s] reasonable expectation of privacy (or constituted

consent) that a search by a law enforcement officer without any individualized

suspicion would have satisfied the reasonableness requirement of the Fourth

Amendment.” Id. at 120 n.6 (emphasis added) (citation omitted).

      B.     Parole Supervision

      In Samson v. California, the Supreme Court answered, in the context of a

parolee, the question left open in Knights and held that suspicionless searches of a

parolee do not violate the Fourth Amendment. 547 U.S. at 857. In that case, a

police officer searched a parolee—pursuant to a California statute that requires

every prisoner eligible for release on state parole to “agree in writing to be subject

to search or seizure by a parole officer or other peace officer at any time of the day

or night, with or without a search warrant and with or without cause”—and found



                                          15
contraband. Id. at 846–47 (citation omitted). The Supreme Court reviewed the

totality of the circumstances pertaining to the petitioner’s status as a parolee,

including his acceptance of the clear and unambiguous search condition, and

concluded that he “did not have an expectation of privacy that society would

recognize as legitimate.” Id. at 852. With respect to his status of a parolee, and the

diminished expectation of privacy resulting therefrom, the Supreme Court

explained:

      As we noted in Knights, parolees are on the continuum of state-
      imposed punishments. On this continuum, parolees have fewer
      expectations of privacy than probationers, because parole is more
      akin to imprisonment than probation is to imprisonment. As this
      Court has pointed out, parole is an established variation on
      imprisonment of convicted criminals. . . . The essence of parole is
      release from prison, before the completion of sentence, on the
      condition that the prisoner abide by certain rules during the balance
      of the sentence. In most cases, the State is willing to extend parole
      only because it is able to condition it upon compliance with certain
      requirements.

Id. at 850 (internal quotation marks and citations omitted). In this context, the

Supreme Court emphasized that “California’s ability to conduct suspicionless

searches of parolees serves its interest in reducing recidivism, in a manner that

aids, rather than hinders, the reintegration of parolees into productive society.” Id.

at 854. Pursuant to that state interest, the Supreme Court “conclude[d] that the



                                         16
Fourth Amendment does not prohibit a police officer from conducting a

suspicionless search of a parolee.” Id. at 857.

      We likewise addressed the scope of suspicionless searches in the context of

parolees in United States v. Braggs, 5 F.4th 183 (2d Cir. 2021). Although noting that

the search at issue was conducted by parole officers rather than by municipal

police officers as in Samson, we concluded that the suspicionless search did not

violate the Fourth Amendment, under the special needs doctrine, when New York

state parole officers were performing a search reasonably related to their duties.

Id. at 187–88. In Braggs, the government appealed from the district court’s decision

suppressing evidence gathered in connection with a parole search of the

defendant’s house. Id. at 184. The government conceded that it lacked reasonable

suspicion, but argued that special needs still permitted the search. Id. On appeal,

this Court agreed and reasoned that “in light of [] special needs” such as “a [s]tate’s

operation of a probation system,” “a search of a parolee is permissible so long as

it is reasonably related to the parole officer’s duties.” Id. at 186–87 (alterations

adopted) (internal quotation marks and citations omitted). “Among these duties

are the supervision, rehabilitation, and societal reintegration of the parolee, as well

as assuring that the community is not harmed by the parolee’s being at large.” Id.



                                          17
at 187 (alterations adopted) (internal quotation marks and citations omitted).

Thus, because the parole officers’ search for a gun in the parolee’s home was

reasonably related to those duties, we held that “the district court erred in holding

that reasonable suspicion was required in this context.” Id. at 188.

      C.     Supervised Release

      Although the Supreme Court has not addressed suspicionless searches in

the context of a defendant on supervised release, this Court has explored that issue

in certain contexts. For example, in United States v. Reyes, 283 F.3d 446, 462 (2d Cir.

2002), we held that a suspicionless visit to the home of a defendant serving a term

of supervised release did not violate the Fourth Amendment. In doing so, we

explained that the diminished Fourth Amendment rights of parolees “appl[y] with

equal force to individuals, like Reyes, subject to federal supervised release—the

reformed successor to federal parole.” Id. at 458. Moreover, we described in detail

the role of the probation officer and emphasized:

      In the same way that a parole officer, of necessity, must have
      investigative powers to gather information about the parolee’s
      activities, environment, and social contacts so as to ensure that the
      conditions of parole are not being violated and to monitor the
      parolee’s progress of reintegration into society, field contacts with a
      convicted person serving a term of federal supervised release are vital
      to ensure that the probation officer is aware of the offender’s conduct
      and condition.


                                          18
Id. at 458 (alterations adopted) (internal quotation marks and citations omitted).

Thus, we held, under the special needs doctrine, that probation officers could

conduct “at any time” a home visit to determine whether the supervisee was

violating the terms of his supervised release, without any individualized

suspicion. Id. at 459–61.

      In United States v. Balon, 384 F.3d 38, 43–44 (2d Cir. 2004), we again discussed

the Fourth Amendment standard for defendants on supervised release in

connection with a challenge to a search condition allowing for remote monitoring

of a defendant’s computer. Balon involved a defendant who was convicted of

transporting child pornography in interstate commerce through the use of a

computer, and, in addition to being sentenced to prison term, was subjected to

conditions of supervised release, including the Probation Department’s remote

monitoring of his use of computers. Id. at 41. In articulating the standard for the

defendant’s Fourth Amendment challenge to that condition of supervised release,

we identified the first part of the inquiry as requiring a determination as to

“whether a convicted person serving a term of federal supervised release[] has a

legitimate expectation of privacy.” Id. at 44 (internal quotation marks, alteration,

and citation omitted). We then reiterated that “[a]n offender on supervised release



                                         19
has a ‘diminished expectation of privacy that is inherent in the very term

“supervised release.”’” Id. (quoting Reyes, 283 F.3d at 460) (emphasis omitted); see

also United States v. Edelman, 726 F.3d 305, 310 (2d Cir. 2013) (noting that

supervisees “who sign waivers manifest an awareness that supervision can

include intrusions into their residence and, thus, have a severely diminished

expectation of privacy” (alteration adopted) (quoting United States v. Newton, 369

F.3d 659, 665 (2d Cir. 2004))). 1



1
    In support of this conclusion, we suggested in Balon that “on the continuum of
supervised release, parole and probation, restrictions imposed by supervised release are
’[t]he most severe.’” 384 F.3d at 44 (quoting Lifshitz, 369 F.3d at 181 n.4). We note that
this suggestion in Balon and Lifshitz may be a misreading of Reyes, which Lifshitz cites for
this proposition. See Lifshitz, 369 F.3d at 181 n.4 (“The most severe [among supervised
release, parole, and probation] is ‘supervised release,’ which is ‘meted out in addition to,
not in lieu of, incarceration’ . . . .” (quoting Reyes, 283 F.3d at 461)). Reyes did state that
the principles supporting the special needs doctrine in the context of probation “apply a
fortiori to federal supervised release, which, in contrast to probation, is meted out in
addition to, not in lieu of, incarceration.” 283 F.3d at 461 (internal quotation marks and
citation omitted). However, while it suggested that the grounds for the special needs
doctrine were even stronger for individuals on supervised release as compared to
probation, we do not read Reyes to suggest that the restrictions imposed by supervised
release are more severe than parole. Indeed, Oliveras asserts that parole is the most
severe on the continuum of forms of post-release supervision because “parole is a
constructive extension of a prison sentence” while “supervised release is imposed in
addition to prison, not as an alternative to it.” Appellant’s Br. at 14. In any event, even if
we accept that construction for purposes of our analysis (notwithstanding the language
in Balon and Lifshitz), we still conclude, as articulated in Reyes, that the governmental
interests supporting suspicionless searches of parolees apply with “equal force” to
supervisees, see 283 F.3d at 458, and, as discussed infra, support the constitutionality of
such searches in the supervised release context.


                                              20
       We further emphasized that “when evaluating conditions of supervised

release under the Fourth Amendment we remain mindful that the alternative

facing defendants on supervised release in the absence of a computer monitoring

probation condition might well be the more extreme deprivation of privacy

wrought by imprisonment.” Balon, 384 F.3d at 44 (alterations adopted) (internal

quotation marks and citation omitted).              Thus, we concluded that “[the

supervisee’s] expectation of privacy is subject to the special needs of supervised

release,” which we then summarized:

       A number of these special needs are set out in Sections 3583(d) and
       3553(a), and provide that conditions reasonably relating to the nature
       and circumstances of the offense and the history and characteristics
       of the defendant must: (i) “afford adequate deterrence to criminal
       conduct”; (ii) “protect the public from further crimes of the
       defendant”; and (iii) “provide the defendant with needed educational
       or vocational training, medical care, or other correctional treatment in
       the most effective manner.” 18 U.S.C. § 3553(a) (cited in 18 U.S.C.
       § 3583(d)). These statutes also require that the conditions “involve[]
       no greater deprivation of liberty than is reasonably necessary” to
       achieve “the[se] purposes.” Id. § 3583(d)(2).

Id. at 44–45. 2



2
   We also note that the policy statement in the Sentencing Guidelines recommends
including certain special conditions of supervised release in cases involving sex offenses,
including a condition that allows a search by a probation officer, without reasonable
suspicion, “in the lawful discharge of the officer’s supervision functions.” U.S.S.G.
§ 5D1.3(d)(7)(C); see also United States v. Parisi, 821 F.3d 343, 348 (2d Cir. 2016) (per
curiam).
                                            21
      We then explained that “[b]ecause of these special needs, the requirements

of effective special conditions define the parameters of a supervised releasee's

Fourth Amendment rights.” Id. at 45. We acknowledged, however, that “the

efficacy of special conditions with respect to computer monitoring, and therefore

the extent to which they must intrude upon a supervised releasee’s privacy in light

of the special needs of supervised release, is fundamentally a question of

technology.” Id. Because the technology at issue is “constantly and rapidly

changing” and “Balon [would] not begin his term of supervised release for three

years,” we concluded that “it [would be] impossible to evaluate at th[at] time

whether one method or another, or a combination of methods, [would] occasion a

greater deprivation of his liberty than necessary in light of the special needs of

supervised release.”   Id. at 46.   We thus dismissed that Fourth Amendment

challenge as unripe for review and directed the district court to reconsider this

issue, at the request of either party, at a time closer to Balon’s release to

supervision. Id.

II.   Suspicionless Search for Defendants on Supervised Release

      Oliveras argues that the Special Condition violates the Fourth Amendment

because it requires him to submit to searches by the probation officer without



                                        22
reasonable suspicion, which infringes on his constitutional right to privacy. We

find this argument, stated so broadly, unpersuasive.

      As we recognized in Reyes, Oliveras has a diminished expectation of privacy

during his period of supervision because he is a “convicted person serving a court-

imposed term of federal supervised release.” 283 F.3d at 457; see also Mont v. United

States, 139 S. Ct. 1826, 1833 (2019) (“Supervised release is a form of

postconfinement monitoring that permits a defendant a kind of conditional liberty

by allowing him to serve part of his sentence outside of prison.” (internal

quotation marks and citation omitted)); United States v. Peguero, 34 F.4th 143, 160-

61 (2d Cir. 2022) (“[P]recedent and logic make clear that a term of supervised

release is imposed as part and parcel of the original sentence—an inextricable part

of the penalty for the initial offense.” (internal quotation marks and citation

omitted)); United States v. Harper, 805 F.3d 818, 822 (7th Cir. 2015) (“[P]rison and

supervised release can be substitutes as well as complements, since, realistically,

supervised release is a form of custody (like parole, which it largely replaced in

the federal system of criminal justice) because it can and often does impose severe

limitations on a defendant’s post-release liberty.” (internal quotation marks and

citation omitted)); see generally United States v. Leon, 663 F.3d 552, 556 (2d Cir. 2011)



                                           23
(“District courts are permitted . . . to hedge against a relatively lenient term of

imprisonment by imposing a longer term of supervised release.” (alterations

adopted) (internal quotation marks and citation omitted)).

      Moreover, Oliveras would be fully aware that he is subject to the Search

Condition during his release, and thus would “[know] that his expectation of

privacy [is] diminished by virtue of his status as a convicted person serving a term

of federal supervised release.” Reyes, 283 F.3d at 460; see also Peguero, 34 F. 4th at

161 (“[E]ven though supervised release fulfills rehabilitative ends, distinct from

those served by incarceration, it is still, like probation or parole, a grant of leniency

based on a defendant’s promise to follow certain conditions.” (internal quotation

marks and citation omitted)).

      Balanced against his diminished expectation of privacy, the government’s

interest in proper and effective supervision of individuals on supervised release is

substantial. The Supreme Court “has repeatedly acknowledged that a State’s

interests in reducing recidivism and thereby promoting reintegration and positive

citizenship among probationers and parolees warrant privacy intrusions that

would not otherwise be tolerated under the Fourth Amendment.” Samson, 547

U.S. at 853. Thus, in Samson, the Supreme Court held that a state’s "ability to



                                           24
conduct suspicionless searches of parolees serves its interest in reducing

recidivism” and that a suspicionless search by a law enforcement officer of a

parolee was not a violation of the Fourth Amendment. Id. at 854, 857. That same

governmental interest in “supervision, rehabilitation, and societal reintegration”

supports a suspicionless search of an individual by his probation officer under the

special needs doctrine during a term of supervised release because such a search

is “reasonably related to the [probation] officer’s duties.” See Braggs, 5 F.4th at

187–88.

      To the extent that Oliveras argues that his status on supervised release

increases his expectation of privacy and/or reduces the government’s interests in

this context when compared to a parolee, such that a suspicionless search cannot

be tolerated by the Fourth Amendment, we are unpersuaded. In rejecting this

argument, we rely on our analysis in Reyes, which thoroughly explained why the

government’s compelling interests in effective supervision during parole are not

diminished simply because an individual is on supervised release.

      To be sure, we recognized that, while both forms of supervision follow

incarceration, supervised release “differs from parole in an important respect:

unlike parole, supervised release does not replace a part of the term of



                                        25
incarceration, but instead is given in addition to any term of imprisonment imposed

by a court.” 3 Reyes, 283 F.3d at 458. Notwithstanding that important distinction,

we concluded that the government’s “special need” to enforce conditions of

supervision imposed on individuals on supervised release is comparable to its

need to enforce such conditions over those on parole and justified a suspicionless

home visit:

       One of the principal purposes of a probation/parole officer’s
       observation and supervision responsibilities is to ensure that a
       convicted person under supervision does not again commit a crime.
       We have long recognized a duty on the part of the parole officer to
       investigate whether a parolee is violating the conditions of his
       parole—one of which, of course, is that the parolee commit no further
       crimes—when the possibility of violation is brought to the officer’s
       attention. Federal probation officers overseeing convicted persons
       serving terms of federal supervised release are similarly charged with
       monitoring supervisees’ adherence to the conditions of their release—
       which, as in the case of parole, includes the requirement that
       supervisees not commit further crimes. Accordingly, because
       probation officers monitoring convicted persons on supervised
       release bear the same supervisory responsibility as when acting as
       parole officers, we conclude that probation officers are required to
       investigate the conduct and condition of a supervisee by, inter alia,
       undertaking “at any time” a home visit to determine whether the
       supervisee is violating the terms of his supervised release, including
       the condition that he not commit any further crimes.

3
  Thus, the district court erred to the extent it suggested that supervised release shortens
a term of imprisonment. See Joint App’x at 100 (“when you’re on supervised release, that
was to allow someone out of prison at an earlier time”). As Reyes explains, supervised
release follows a term of imprisonment, while parole conditionally shortens a term of
imprisonment. See Reyes, 283 F.3d at 458.
                                            26
Id. at 459–60 (internal quotation marks, citations, and footnotes omitted). 4

       In short, recognizing as we did in Reyes the diminished expectation of

privacy of supervisees, and the special needs of probation officers to fulfill their

supervisory roles in that capacity, we hold that the imposition of a special

condition of supervised release that allows for searches without individualized

suspicion does not violate the Fourth Amendment and, thus, can be imposed if

sufficiently supported by the record under the factors set forth in Section 3583(d).

Such a condition gives probation officers the “considerable investigative leeway”

they need to monitor an individual on supervised release, such that they can act

as the “eyes and ears” for the court. Reyes, 283 F.3d at 455, 457 (internal quotation




4
  In contexts other than search conditions, the Supreme Court has expressed a variety of
views on the extent to which supervised release is similar to or different from traditional
parole. See United States v. Haymond, 139 S. Ct. 2369, 2382 (2019) (plurality opinion)
(“[U]nlike parole, supervised release wasn’t introduced to replace a portion of the
defendant’s prison term, only to encourage rehabilitation after the completion of his
prison term. . . . [T]hat structural difference bears constitutional consequences.” (internal
quotation marks omitted)); id. at 2385 (Breyer, J., concurring in judgment) (“[T]he role of
the judge in a supervised-release proceeding is consistent with traditional parole.”); id. at
2388 (Alito, J., dissenting) (Although “parole relieved a prisoner from serving part of the
prison sentence originally imposed, whereas a term of supervised release is added to the
term of imprisonment specified by the sentencing judge[,] . . . this difference is purely
formal and should have no constitutional consequences.”); Mont, 139 S. Ct. at 1833–34
(five-justice majority describing supervised release as both “a form of punishment” and
“a form of postconfinement monitoring that permits a defendant a kind of conditional
liberty by allowing him to serve part of his sentence outside of prison” (internal quotation
marks and citation omitted)).
                                             27
marks and citations omitted).       In other words, the special condition allows

probation officers “to determine whether the supervisee is violating the terms of

his supervised release, including the condition that he not commit any further

crimes.” Id. at 460.

      Our sister circuits who have addressed this issue have reached the same

conclusion under analogous circumstances. For example, in United States v. Betts,

511 F.3d 872, 876 (9th Cir. 2007), the Ninth Circuit upheld a condition of supervised

release that provided that “the defendant shall submit person and property to

search and seizure at any time of the day or night by any law enforcement officer,

with or without a warrant.” 5 In finding no abuse of discretion in imposing that

“very intrusive” condition, the Ninth Circuit relied heavily on the Supreme

Court’s decision in Samson:

      [T]he Supreme Court recently held in Samson v. California, that a
      similarly worded condition imposed by statute on all California
      parolees did not violate the Fourth Amendment, even though the
      condition did not require reasonable suspicion. The Court considered
      the high risk of recidivism for people convicted of crimes, and the
      problem that “[i]mposing a reasonable suspicion requirement . . .
      would give parolees greater opportunity to anticipate searches and
      conceal criminality.” Because the blanket requirement imposed by

5 Because the Special Condition here allowed suspicionless searches only by probation
officers, we do not reach the question of whether law enforcement officers other than the
probation officer(s) conducting the supervision may conduct such searches pursuant to
the special condition.
                                           28
      California on state parolees did not violate the Fourth Amendment, a
      fortiori the individualized requirement imposed in this case on
      supervised release does not. There is no sound reason for
      distinguishing parole from supervised release with respect to this
      condition. The federal system has abolished parole, and uses
      supervised release to supervise felons after they get out of prison.
      People on supervised release have not completed their sentences, they
      are serving them. The Court in Samson itself drew the analogy to
      supervised release. After Samson, there is no room for treating the
      search condition in this case as an abuse of discretion.

Id. (footnotes omitted) (quoting Samson, 547 U.S. at 854–55).

      Similarly, in United States v. Hanrahan, 508 F.3d 962, 971 (10th Cir. 2007), the

Tenth Circuit upheld a special condition of supervised release, for a defendant

convicted of unlawfully possessing a firearm, that required the defendant to

“submit to a search of his person, property, or automobile under his control”

without any level of suspicion. The court noted that “one effective means of

preventing [the defendant] from committing a similar offense in the future is to

require him to submit to suspicionless searches after he has been released from

prison but while he is still under the supervision of the Probation Officer.” Id. The

court further explained that “[s]earches based on some particularized level of

suspicion, by way of contrast, would likely not be as effective at deterring future

crimes of possession since the defendant could easily conceal such wrongdoing.”

Id. It therefore held that the district court acted within its discretion in imposing


                                         29
the suspicionless search condition. Id.; see also United States v. Sulik, 807 F. App’x

489, 493 (6th Cir. 2020) (summary order) (concluding that “the current legal

landscape forecloses any claim that a suspicionless-search condition for

individuals on supervised release ‘plainly’ violates the Fourth Amendment”);

United States v. Oswald, 711 F. App’x 593, 594–95 (11th Cir. 2018) (summary order)

(holding no plain error in imposition of suspicionless search condition of

supervised release); United States v. Erwin, 675 F. App’x 471, 472 (5th Cir. 2017)

(summary order) (same); United States v. Jackson, 866 F.3d 982, 985 (8th Cir. 2017)

(upholding suspicionless search of cell phone of defendant on supervised release

at a residential correctional facility). 6




6
   Other courts, with respect to probation supervision, have likewise found that a
condition allowing for a suspicionless search of a probationer’s residence does not violate
the Fourth Amendment. See, e.g., United States v. Tessier, 814 F.3d 432, 433 (6th Cir. 2016)
(holding that a condition to search probationer’s person, vehicle, property or place of
residence without suspicion did not violate the Fourth Amendment); United States v. King,
736 F.3d 805, 806 (9th Cir. 2013) (holding that suspicionless search of probationer’s
residence is permissible under the Fourth Amendment “when, as here, a violent felon has
accepted a suspicion-less search condition as part of a probation agreement”); Owens v.
Kelley, 681 F.2d 1362, 1368 (11th Cir. 1982) (holding that suspicionless search of
probationer’s residence is permissible under the Fourth Amendment because “[i]t is clear
that a requirement that searches only be conducted when officers have ‘reasonable
suspicion’ or probable cause that a crime has been committed or that a condition of
probation has been violated could completely undermine the [deterrence] purpose of the
search condition”). We have no occasion here to address the constitutionality of
suspicionless searches of probationers.
                                             30
         In sum, we conclude that the special needs doctrine of the Fourth

Amendment permits, when sufficiently supported by the record, the imposition

of a special condition of supervised release by the district court that allows the

probation officer conducting the supervision to search the defendant’s person,

property, vehicle, place of residence, or any other property under his control,

without any level of suspicion.

III.     Procedural Reasonableness of the Search Condition in this Case

         Oliveras alternatively argues that the imposition of the Search Condition

was procedurally unreasonable in this case because the district court did not make

an individualized assessment as to the need to impose the condition, nor

sufficiently state its reasons as to why the imposition of the condition in this case

was reasonably related to the relevant sentence factors under Section 3553(a). We

agree.

         “For a sentence to be procedurally reasonable, a [d]istrict [c]ourt must ‘make

an individualized assessment when determining whether to impose a special

condition of supervised release, and . . . state on the record the reason for imposing

it.’” Eaglin, 913 F.3d at 94 (2d Cir. 2019) (quoting United States v. Betts, 886 F.3d

198, 202 (2d Cir. 2018)). “In the absence of such an explanation, we may uphold



                                           31
the condition imposed only if the district court’s reasoning is ‘self-evident in the

record.’” Betts, 886 F.3d at 202 (quoting Balon, 384 F.3d at 41 n.1).

      In imposing conditions of supervised release, district courts possess broad

discretion. United States v. Myers, 426 F.3d 117, 124 (2d Cir. 2005). The district

court may impose a special condition of supervised release that is “reasonably

related to (A) the nature and circumstances of the offense and the history and

characteristics of the defendant; (B) the need for the sentence imposed to afford

adequate deterrence to criminal conduct; (C) the need to protect the public from

further crimes of the defendant; and (D) the need to provide the defendant with

needed educational or vocational training, medical care, or other correctional

treatment in the most effective manner.” U.S.S.G. § 5D1.3(b); accord 18 U.S.C.

§§ 3583(d)(1), 3553(a); United States v. Johnson, 446 F.3d 272, 277 (2d Cir. 2006).

Notwithstanding the use of the conjunctive in the Guidelines, “a condition may be

imposed if it is reasonably related to any one or more of the specified factors.”

United States v. Amer, 110 F.3d 873, 883 (2d Cir. 1997) (internal quotation marks and

citation omitted).   Moreover, a special condition must involve “no greater

deprivation of liberty than is reasonably necessary for the purposes” of sentencing,

and it must be “consistent with any pertinent policy statements issued by the



                                          32
Sentencing Commission.” 18 U.S.C. § 3583(d)(2), (3); see also U.S.S.G. § 5D1.3(b);

accord Balon, 384 F.3d at 42. Importantly, a district court’s discretion to impose

special conditions is not “untrammelled,” and we will “carefully scrutinize

unusual and severe conditions.” Myers, 426 F.3d at 124 (internal quotation marks

and citations omitted).

      Here, the district court failed to make an individualized assessment to

support the imposition of the suspicionless Search Condition as to Oliveras.

Indeed, the district court made clear that it was not making an individualized

assessment as to the need to impose the condition on Oliveras when it stated that

it was “not inclined to put the reasonable suspicion requirement in [its] sentences

unless somebody can point to . . . a valid reason why in a particular case it should,”

and thus, in “the general case, [the district court] will provide reasonable suspicion

is not required.” Joint App’x at 100. Rather than making an individualized

assessment at the start, the district court espoused the presumptive application of

the Search Condition in drug cases, relying on broad statements about its views

regarding supervision in drug cases generally, untethered to any specific

consideration to the facts and circumstances in this particular case. For example,

the district court justified the Search Condition with its observation that



                                         33
individuals convicted of drug offenses tended to reoffend while on supervised

release. Additionally, the district court reasoned that, because offenders do not

leave drugs out in the open, probation officers should be afforded the ability to

conduct searches without a showing of reasonable suspicion. The district court

also stated that, given the high risk of recidivism in drug cases, requiring

reasonable suspicion would undermine the needs of the probation officer to

supervise those particular offenders on release.

      We recognize that the district court generally expressed some valid reasons

as to why a suspicionless search could be reasonably related to the relevant factors,

under Section 3553(a), in cases involving drug offenses. However, exclusive

reliance on those generalized considerations is inconsistent with the requirement

that the district court make an “individualized assessment” as to each defendant

when determining whether to impose a special condition. Eaglin, 913 F.3d at 94

(internal quotation marks and citation omitted); see also United States v. Arbaugh,

951 F.3d 167, 179 (4th Cir. 2020) (“[T]he district court cannot fulfill its duty by

generally referring to the legal standards in § 3553(a) and § 3583(d), which govern

how the court should exercise its discretion in imposing any special conditions of

release. Instead, the district court had to explain what facts led to its decision to



                                         34
impose the computer-related special conditions[, which permitted random

inspections of defendant’s personal computing devices,] on this defendant.”

(emphasis added)); cf. United States v. Germosen, 139 F.3d 120, 131–32 (2d Cir. 1998)

(upholding search condition permitting searches of defendant’s person and

property “necessary to secure financial information” in a fraud case involving

restitution order, where the district court’s “reasoning behind the condition, as

with her reasoning behind other aspects of [the defendant’s] sentence, was made

clear during the sentencing hearing”); United States v. Winston, 850 F.3d 377, 380–

81 (8th Cir. 2017) (holding district court did not commit plain error in imposing

reasonable suspicion based search condition on a narcotics offender where the

probation officer’s motion and the court’s statement at sentencing explained the

need for the condition); United States v. Monteiro, 270 F.3d 465, 469 (7th Cir. 2001)

(upholding search condition requiring defendant to submit to search “upon

demand” in a fraud case where, “[i]n imposing the special condition . . . , the

district court explained that [the defendant’s] history of fraudulent endeavors

demonstrated the need for ‘exceptional vigilance’ on the part of law enforcement

officials to discourage recidivism”).




                                         35
      The district court’s responsibility to conduct an individualized assessment

is not suspended in drug cases, nor is it permissible to have a presumption that a

suspicionless search condition is warranted in every drug case unless a defendant

can demonstrate otherwise. Indeed, it is not difficult to imagine individualized

cases where, although a defendant was convicted of a drug offense, the nature of

his involvement in that offense, combined with an assessment of the other

applicable statutory factors, would not support a finding that such a highly

intrusive suspicionless search condition is reasonable. Therefore, any decision by

a district court to this or any other special condition must be supported, including

in drug cases, by an individualized assessment and explanation as to why that

condition is “reasonably related” to the sentencing objectives and “involve[s] no

greater deprivation of liberty than is reasonably necessary” for these purposes.

U.S.S.G. § 5D1.3(b); see also Eaglin, 913 F.3d at 100 (emphasizing that “[b]efore

imposing a special condition . . . , a district court must make factual findings

supporting its view that the condition is designed to address a realistic danger and

the deprivation the condition creates is not greater than reasonably necessary to

serve the sentencing factors”).




                                         36
      Moreover, while we agree with the government that a condition of

supervised release permitting suspicionless searches does not per se violate the

Fourth Amendment, and may in appropriate cases be supported by the special

needs of supervision, it does not follow that such a condition may be imposed as

a routine matter. As with other conditions of supervised release that implicate

constitutionally protected interests, such a broad authorization to conduct

unlimited searches must be carefully considered by sentencing courts “and

supported by particularized findings that it does not constitute a greater

deprivation of liberty than reasonably necessary to accomplish the goals of

sentencing.” United States v. Matta, 777 F.3d 116, 123 (2d Cir. 2015) (internal

quotation marks and citations omitted).

      In Reyes, our approval of the condition authorizing suspicionless home visits

rested, in part, on the recognition that “a home visit is far less intrusive than a [full-

scale] probation search,” 283 F.3d at 462 (emphasis omitted), and we have

heretofore approved conditions permitting searches of a supervisee’s home only

upon reasonable suspicion. As we have repeatedly explained in affirming such

search conditions, those conditions do not constitute a greater deprivation than




                                           37
reasonably necessary because they require reasonable suspicion. 7 The requirement

of reasonable suspicion does not set a high bar, and the government cites no

empirical evidence that the ordinary practice of courts within this Circuit of

imposing search conditions based on reasonable suspicion has failed to satisfy the

Probation Department’s “special needs” of supervision in the vast majority of

cases, such that suspicionless search conditions are required. Permitting such

highly intrusive, full-scale searches for no particular reason, without limitation as

to frequency or scope, subjects the supervisee to the prospect of frequent,

unlimited searches without any factual precondition. Such conditions may be

justified, but they require careful consideration as to the need for such broad

discretion to search in each particular case. 8



7
  See United States v. Stiteler, No. 22-2732, 2023 WL 4004573, at *1 (2d Cir. June 15, 2023)
(summary order) (finding that the district court did not abuse its discretion in “finding
that the search condition [did] not depriv[e] [the defendant] of liberty greater than
necessary because it requires . . . reasonable suspicion before the search can be
conducted.” (internal quotation marks and citation omitted)); United States v. Rakhmatov,
No. 21-151, 2022 WL 16984536, at *3 (2d Cir. Nov. 17, 2022) (summary order) (explaining
that the “condition’s limitations on searches to circumstances in which reasonable
suspicion of a supervised release violation exists and to a reasonable time and manner of
search ensure that the condition imposes no greater restraint on liberty than is reasonably
necessary” (alterations adopted) (internal quotation marks and citation omitted)).

8 As we have long acknowledged, “searching for illegal drug use” is a “particularly apt
analogy to monitoring for computer-related sex offenses.” Lifshitz, 369 F.3d at 189. In
light of the constitutional rights implicated by conditions of supervised release


                                            38
       Accordingly, we conclude that the district court committed procedural

error, and therefore exceeded the scope of its discretion, because it did not make

an individualized assessment in deciding whether to impose the Search Condition

or provide adequate reasons for us to decide whether the Search Condition is

reasonable under Section 3583(d), including a sufficient explanation as to how the

condition is reasonably related in this particular case to the applicable statutory

factors under Section 3553(a). 9



permitting monitoring of computer devices or restricting access to the internet, we have
repeatedly emphasized that such conditions must be “narrowly tailored” and “robustly
supported” by a district court. Eaglin, 913 F.3d at 91, 98. Thus, we have not hesitated to
remand monitoring conditions where a less intrusive condition appeared to be a “viable
option” and the record “d[id] not explain why such [an alternative condition] was
insufficient.” Id. at 98; see also United States v. Salazar, No. 22-1385, 2023 WL 4363247, at
*3 (2d Cir. July 6, 2023) (summary order) (vacating monitoring condition authorizing
suspicionless search of defendant’s internet-capable devices, where “narrower options
were available to the district court” and there was “no indication that the district
considered such a [narrower] condition” or “explan[ation] why a more stringent
condition was necessary”).

9
   We recognize that, even in the absence of an explanation, we can uphold the Search
Condition “if the district court’s reasoning is ‘self-evident in the record,’” Betts, 886 F.3d
at 202 (quoting Balon, 384 F.3d at 41 n.1), and the record here does indicate that drugs and
a firearm were seized from a residence in Buffalo attributed to Oliveras. However, that
seizure occurred more than three years prior to his sentence and it is self-evident, based
upon the discussion at sentencing, that the district court’s reasoning did not contain the
requisite individualized assessment of Oliveras at the time of sentencing as it relates to
the Special Condition. Thus, under the circumstances, we conclude that a remand is
necessary for the district court to make that individualized assessment after the parties
have had an opportunity to present any relevant information on this issue that could bear
on the applicable statutory factors.
                                             39
                                 CONCLUSION

      For the reasons set forth above, we VACATE the Search Condition and

REMAND to the district court for further consideration of whether it is necessary

to impose the Search Condition in this particular case and, if so, for the district

court to explain the individualized basis for imposing the Search Condition.




                                        40

```

---

## GROUP: _overhaul2/lake/cases/United States v. Osage.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Osage"
type: case
citation: "235 F.3d 518 (2000)"
parallel_cite: 2000 Colo. J. C.A.R. 6671
neutral_cite: "2000 U.S. App. LEXIS 32020; 2000 WL 1842404"
court: "U.S. Court of Appeals, 10th Circuit"
court_level: coa
circuit: 10th
year: 2000
date_decided: 2000-12-15
docket: ""
authority_weight: "Binding in-circuit — 10th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2000-12-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Osage
  varies_by_point: false
  scope_note: "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/160502/united-states-v-osage/"
  cluster_id: 160502
  opinion_id: 160502
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Limiting"
related: ["[[Florida v. Jimeno]]", "[[Schneckloth v. Bustamonte]]", "[[Georgia v. Randolph]]"]
aliases: ["United States v. David Blake Osage", "United States v. Osage (10th Cir. 2000)"]
tags: ["case", "fourth-amendment", "consent-searches", "scope-of-consent", "containers", "tenth-circuit"]
holding: "General consent to a search does not authorize an officer to destroy a container: before an officer may actually destroy or render completely useless a container otherwise within the scope of a permissive search, the officer must obtain explicit authorization or have some other lawful basis to proceed."
lake:
  record_id: United States v. Osage
  status: verified
  projected_at: 2026-07-09
---

# United States v. Osage

*235 F.3d 518 (10th Cir. 2000)* · U.S. Court of Appeals, 10th Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
On an Amtrak train passing through Albuquerque, Officer Salazar asked David Blake Osage for permission to search his luggage; Osage answered "yeah, I guess," nodded, and gestured toward a black bag. Inside the bag the officer found four 28-ounce cans labeled "tamales in gravy." Noticing that one can's label appeared re-glued and that the can felt and sounded like it held salt rather than tamales in liquid, the officer used a Leatherman tool to cut the can open, discovering methamphetamine inside. Osage was charged with possession with intent to distribute methamphetamine (21 U.S.C. § 841); the district court denied suppression, reasoning that Osage's consent was voluntary and that he never limited its scope or objected as the can was opened. Osage pleaded guilty, reserving his right to appeal the suppression ruling.

## Issue
Whether a suspect's general consent to search his luggage authorized the officer to cut open — and thereby destroy — a sealed can found inside.

## Rule
The scope of a consent search is bounded by the consent given, "measured by objective reasonableness: 'what would the typical reasonable person have understood by the exchange between the officer and the suspect?'" — 235 F.3d at 520 (quoting *Florida v. Jimeno*, 500 U.S. 248, 251 (1991)). ^pin-520

General consent to search an area reaches containers within it that could hold contraband — but it does not reach destroying them: "We acknowledge that the Supreme Court and this court have previously stated that a general consent to search a particular area is reasonably understood to extend to a search of containers within that area that could contain contraband . . . . However, we do not read that authority to permit the destruction of such containers." — *Id.* at 521. ^pin-521

The court therefore held: "before an officer may actually destroy or render completely useless a container which would otherwise be within the scope of a permissive search, the officer must obtain explicit authorization, or have some other, lawful, basis upon which to proceed." — [235 F.3d at 522](https://www.courtlistener.com/opinion/160502/united-states-v-osage/#:~:text=before%20an%20officer%20may%20actually). ^pin-522

## Application
Assuming Osage's consent was valid, opening the sealed can exceeded the scope of that consent because doing so destroyed the can — "rendering it useless and incapable of performing its designated function," which the court found "more like breaking open a locked briefcase than opening the folds of a paper bag." Because the government never claimed independent suspicion or probable cause to detain or open the cans, and obtained no explicit authorization to destroy them, the destruction of the can fell outside the consent and could not be justified on any other ground.

## Conclusion
The search exceeded the scope of consent; the Tenth Circuit reversed the denial of suppression of the methamphetamine and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 10th Cir.**
- *Osage* applies and **cabins** [[Florida v. Jimeno]]'s objective-reasonableness scope-of-consent test: while general consent reaches containers that might hold contraband, it does not authorize an officer to destroy a container without explicit authorization or another lawful basis. It is an illustrative limit on the reach of consent for the [[Consent Searches]] doctrine.

## Appears on
- [[Consent Searches]] — *Limiting*

## Sources
- *United States v. Osage*, 235 F.3d 518 (10th Cir. 2000) — https://www.courtlistener.com/opinion/160502/united-states-v-osage/ — pinpoints: 520, 521, 522.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b4da1d47057fac7b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Osage"}, "payload": {"all": [{"cite": "235 F.3d 518", "page": "518", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "235"}, {"cite": "2000 Colo. J. C.A.R. 6671", "page": "6671", "reporter": "Colo. J. C.A.R.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "2000"}, {"cite": "2000 U.S. App. LEXIS 32020", "page": "32020", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2000"}, {"cite": "2000 WL 1842404", "page": "1842404", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2000"}], "display": "235 F.3d 518", "official": {"cite": "235 F.3d 518", "page": "518", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "235"}, "official_selection_present": true, "record_id": "United States v. Osage"}}
{"assertion_id": "0201c7a8249203ad", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-520", "record_id": "United States v. Osage"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-520", "pinpoint_status": "slip-only", "quote": "Noticing that one can's label appeared re-glued and that the can felt and sounded like it held salt rather than tamales in liquid, the officer used a Leatherman tool to cut the can open, discovering methamphetamine inside. Osage was charged with possession with intent to distribute methamphetamine (21 U.S.C. § 841); the district court denied suppression, reasoning that Osage's consent was voluntary and that he never limited its scope or objected as the can was opened. Osage pleaded guilty, reserving his right to appeal the suppression ruling. ## Issue Whether a suspect's general consent to search his luggage authorized the officer to cut open — and thereby destroy — a sealed can found inside. ## Rule The scope of a consent search is bounded by the consent given,", "quote_fidelity": "mismatch", "record_id": "United States v. Osage", "star_marker": null}}
{"assertion_id": "80e2a74add1eb20d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-521", "record_id": "United States v. Osage"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-521", "pinpoint_status": "slip-only", "quote": "We acknowledge that the Supreme Court and this court have previously stated that a general consent to search a particular area is reasonably understood to extend to a search of containers within that area that could contain contraband . . . . However, we do not read that authority to permit the destruction of such containers.", "quote_fidelity": "mismatch", "record_id": "United States v. Osage", "star_marker": null}}
{"assertion_id": "f556a9aa0ff7dcdb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-522", "record_id": "United States v. Osage"}, "payload": {"fragment": "#:~:text=before%20an%20officer%20may%20actually", "page": null, "pin_id": "pin-522", "pinpoint_status": "slip-only", "quote": "before an officer may actually destroy or render completely useless a container which would otherwise be within the scope of a permissive search, the officer must obtain explicit authorization, or have some other, lawful, basis upon which to proceed.", "quote_fidelity": "matched", "record_id": "United States v. Osage", "star_marker": null}}
{"assertion_id": "89fa078dcd931db7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Osage"}, "payload": {"as_of_content": "2000-12-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Osage", "scope_note": "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container.", "varies_by_point": false}}
```

### lake record — United States v. Osage

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Osage",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Osage",
    "case_name_short": "Osage",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. David Blake OSAGE, Defendant-Appellant",
    "input_case_name": "United States v. Osage",
    "court": "U.S. Court of Appeals, 10th Circuit",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "10th",
    "state": null,
    "date_decided": "2000-12-15",
    "year": 2000,
    "docket": null,
    "cluster_id": 160502,
    "lead_opinion_id": 160502,
    "sibling_ids": [
      160502
    ],
    "absolute_url": "/opinion/160502/united-states-v-osage/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "235 F.3d 518",
      "volume": "235",
      "reporter": "F.3d",
      "page": "518",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2000 Colo. J. C.A.R. 6671",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2000 U.S. App. LEXIS 32020",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "32020",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 1842404",
        "volume": "2000",
        "reporter": "WL",
        "page": "1842404",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "235 F.3d 518",
        "volume": "235",
        "reporter": "F.3d",
        "page": "518",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 Colo. J. C.A.R. 6671",
        "volume": "2000",
        "reporter": "Colo. J. C.A.R.",
        "page": "6671",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 U.S. App. LEXIS 32020",
        "volume": "2000",
        "reporter": "U.S. App. LEXIS",
        "page": "32020",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2000 WL 1842404",
        "volume": "2000",
        "reporter": "WL",
        "page": "1842404",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "235 F.3d 518",
    "official_selection": {
      "court_class": "coa",
      "selected": "235 F.3d 518",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-520",
      "page": null,
      "quote": "Noticing that one can's label appeared re-glued and that the can felt and sounded like it held salt rather than tamales in liquid, the officer used a Leatherman tool to cut the can open, discovering methamphetamine inside. Osage was charged with possession with intent to distribute methamphetamine (21 U.S.C. \u00a7 841); the district court denied suppression, reasoning that Osage's consent was voluntary and that he never limited its scope or objected as the can was opened. Osage pleaded guilty, reserving his right to appeal the suppression ruling. ## Issue Whether a suspect's general consent to search his luggage authorized the officer to cut open \u2014 and thereby destroy \u2014 a sealed can found inside. ## Rule The scope of a consent search is bounded by the consent given,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-521",
      "page": null,
      "quote": "We acknowledge that the Supreme Court and this court have previously stated that a general consent to search a particular area is reasonably understood to extend to a search of containers within that area that could contain contraband . . . . However, we do not read that authority to permit the destruction of such containers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-522",
      "page": null,
      "quote": "before an officer may actually destroy or render completely useless a container which would otherwise be within the scope of a permissive search, the officer must obtain explicit authorization, or have some other, lawful, basis upon which to proceed.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 12507,
      "fragment": "#:~:text=before%20an%20officer%20may%20actually",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2000-12-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Osage",
    "varies_by_point": false,
    "scope_note": "Good law. Applies and cabins Florida v. Jimeno: general consent does not authorize destroying a container.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "No. 01-5098",
          "cluster_id": 782823,
          "cite": [
            "336 F.3d 1194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lyons",
          "cluster_id": 170093,
          "cite": [
            "510 F.3d 1225",
            "2007 U.S. App. LEXIS 29307",
            "2007 WL 4395442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marquez",
          "cluster_id": 163723,
          "cite": [
            "337 F.3d 1203",
            "2003 U.S. App. LEXIS 15374",
            "2003 WL 21758415"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregoire",
          "cluster_id": 166481,
          "cite": [
            "425 F.3d 872",
            "2005 U.S. App. LEXIS 21398",
            "2005 WL 2422788"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan v. Nally",
          "cluster_id": 8209848,
          "cite": [
            "178 Vt. 222",
            "2005 VT 85",
            "882 A.2d 1164",
            "2005 Vt. LEXIS 168"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaniz West v. City of Caldwell",
          "cluster_id": 4642875,
          "cite": [
            "931 F.3d 978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carbajal-Iriarte",
          "cluster_id": 172835,
          "cite": [
            "586 F.3d 795",
            "2009 U.S. App. LEXIS 24129",
            "2009 WL 3585083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pikyavit",
          "cluster_id": 170798,
          "cite": [
            "527 F.3d 1126",
            "2008 U.S. App. LEXIS 11874",
            "2008 WL 2265154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Rosa Elene Becerra",
          "cluster_id": 3171759,
          "cite": [
            "239 Ariz. 90",
            "366 P.3d 567",
            "731 Ariz. Adv. Rep. 9",
            "2016 Ariz. App. LEXIS 9"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 2378130,
          "cite": [
            "501 F. Supp. 2d 1284",
            "2007 U.S. Dist. LEXIS 58308",
            "2007 WL 2258451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendoza",
          "cluster_id": 3189005,
          "cite": [
            "817 F.3d 695",
            "2016 WL 1169102",
            "2016 U.S. App. LEXIS 5597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana-Aguirre",
          "cluster_id": 1451461,
          "cite": [
            "537 F.3d 929",
            "2008 U.S. App. LEXIS 17125",
            "2008 WL 3289403"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Al-Marri",
          "cluster_id": 2425981,
          "cite": [
            "230 F. Supp. 2d 535",
            "2002 U.S. Dist. LEXIS 21765",
            "2002 WL 31519619"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez-Arzate",
          "cluster_id": 4835114,
          "cite": [
            "981 F.3d 832"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Navas",
          "cluster_id": 1452233,
          "cite": [
            "640 F. Supp. 2d 256",
            "2009 U.S. Dist. LEXIS 37464",
            "2009 WL 1138020"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 6243487,
          "cite": [
            "565 S.W.3d 919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pablo Ernesto Villarreal Jr. v. State",
          "cluster_id": 4577200,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Valdivia, R., Aplt.",
          "cluster_id": 4544418,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Santana-Aguirre",
          "cluster_id": 3045182,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Garza",
          "cluster_id": 2528576,
          "cite": [
            "269 F. Supp. 2d 1330",
            "2003 U.S. Dist. LEXIS 11095",
            "2003 WL 21499232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeter",
          "cluster_id": 2427055,
          "cite": [
            "394 F. Supp. 2d 1334",
            "2005 U.S. Dist. LEXIS 6790",
            "2005 WL 941178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Garcia",
          "cluster_id": 2147739,
          "cite": [
            "781 F. Supp. 2d 1167",
            "2011 U.S. Dist. LEXIS 27360",
            "2011 WL 938360"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Osage:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(160502) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca10)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(160502)",
        "reviewed": 24,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 23,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(160502)",
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
    "complete_query": "cites:(160502)",
    "indexed_citing_opinions": 24,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 160502,
        "count": 24,
        "count_source": "search"
      }
    ],
    "citation_count": 34,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-osage.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjA2MDAwNTMmcz0xNjM3MjMmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28160502%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 160502,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 153281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 396620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 463815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 540933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 552827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 563771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 572508,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 672873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 673940,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 676092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 754317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 763263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 769221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 160502,
        "cited_id": 1200095,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T01:55:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T01:58:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:55:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Osage

```
                                                                       F I L E D
                                                                United States Court of Appeals
                                                                        Tenth Circuit
                                       PUBLISH
                                                                       DEC 15 2000
                    UNITED STATES COURT OF APPEALS
                                                                     PATRICK FISHER
                                                                            Clerk
                                 TENTH CIRCUIT



 UNITED STATES OF AMERICA,

               Plaintiff - Appellee,
          v.                                           No. 99-2235
 DAVID BLAKE OSAGE,

               Defendant - Appellant.


           APPEAL FROM THE UNITED STATES DISTRICT COURT
                  FOR THE DISTRICT OF NEW MEXICO
                        (D.C. NO. CR-98-552-BB)


Stuart Southerland, Tulsa, Oklahoma, for Appellant.

David N. Williams, Assistant United States Attorney (John J. Kelly, United States
Attorney, and J. Miles Hanisee, Assistant United States Attorney, on the brief),
Albuquerque, New Mexico, for Appellee.


Before LUCERO and ANDERSON , Circuit Judges, and        MILLS, * District Judge.


ANDERSON , Circuit Judge.




      *
       The Honorable Richard Mills, United States District Judge for the Central
District of Illinois, sitting by designation.
      David Blake Osage appeals his conviction on one count of possession with

intent to distribute one kilogram or more of methamphetamine, in violation of

21 U.S.C. § 841(a)(1), (b)(1)(A). Mr. Osage moved unsuccessfully to suppress

the introduction of the methamphetamine and subsequently pled guilty to the

indictment, reserving his right to appeal the suppression ruling. On appeal, he

challenges the district court’s finding that he consented to the search that resulted

in seizure of the methamphetamine. Because we conclude that the search

exceeded the scope of the consent given, we reverse and remand this case.



                                  BACKGROUND

      On June 4, 1998, Task Force Officer Sam Candelaria of the New Mexico

State Police notified Task Force Officer Jonathan Salazar that Mr. Osage would

be traveling through Albuquerque on an Amtrak train that ran between Los

Angeles and Chicago. Mr. Osage had paid cash for passage in a sleeping car

aboard the train shortly before it left California.

      Officer Salazar boarded the train in Albuquerque with another officer, both

of whom were in plain clothes. Officer Salazar confronted Mr. Osage in a

passageway in the sleeping car, identified himself as a police officer, and asked to

speak to him. The officer asked Mr. Osage about his destination and requested to

see his tickets. Mr. Osage told Officer Salazar that his tickets were in a bag in his


                                          -2-
room. The officer followed Mr. Osage to his room, where Mr. Osage produced

the tickets.

       Officer Salazar then asked Mr. Osage about his luggage, and Mr. Osage

identified two suitcases. One of the suitcases, a black bag, was closed and

locked. The officer asked for permission to search the bags. Mr. Osage

responded, “yeah, I guess.” Appellant’s App. at 311. Officer Salazar asked again

whether it would be okay to search the bags. Mr. Osage did not respond verbally,

but nodded, gestured upward with his palms, and pointed toward the black bag.

       Mr. Osage produced a key and opened the black bag. Inside, Officer

Salazar found plastic grocery bags containing four 28-ounce cans labeled

“tamales in gravy.” The officer picked up one of the cans and noticed that the

label appeared to have been tampered with, perhaps re-glued. When he shook the

can, he noticed that it did not feel and sound like it contained tamales in liquid,

but instead felt like a container of salt would feel when shaken. He then took a

Leatherman tool off his belt, opened the can, and discovered a plastic bag

containing methamphetamine.

       The district court denied Mr. Osage’s motion to suppress on the ground that

his consent to search was freely and voluntarily given, and Mr. Osage never

limited its scope to exclude opening the tamales can. Specifically, the court

stated, “[w]hile the Court was extremely skeptical that the extent of the consent


                                          -3-
extended to physically opening the tamale cans, [Mr. Osage] stood by and

watched without demur while the agent took out a can opener and split the can

lid. If [Mr. Osage] had questioned this procedure, the outcome of this motion

may well have been different.” Order at 2, Appellant’s App. at 91 (citing      United

States v. Kim , 27 F.3d 947 (3d Cir. 1994);     United States v. Torres , 663 F.2d 1019

(10th Cir. 1981), cert. denied , 456 U.S. 973 (1982); United States v. Pena , 920

F.2d 1509, 1515 (10th Cir. 1990)).



                                      DISCUSSION

       When we review the denial of a motion to suppress, we must accept the

district court’s factual findings unless they are clearly erroneous.    United States v.

Wald , 216 F.3d 1222, 1225 (10th Cir. 2000). “The district court’s determination

of reasonableness under the Fourth Amendment, however, is reviewed de novo.”

Id.



       I. Validity of Consent

       Mr. Osage argues that consent solicited by a police officer is involuntary

per se and he argues that the particular consent given in this case was not freely

and voluntarily given. He makes a number of subsidiary arguments. Because we

conclude that the district court erred in denying his motion to suppress based


                                              -4-
upon the scope of the consent, we need not address these other arguments. We

assume that Mr. Osage’s consent was validly given.



       II. Scope of Consent

       Mr. Osage argues that Officer Salazar’s actions in opening the tamale can

exceeded the scope of the search. When law enforcement officers rely upon

consent as the basis for a warrantless search, the scope of the consent determines

the permissible scope of the search.       See Florida v. Jimeno , 500 U.S. 248, 251-52

(1991). The scope of consent is measured by objective reasonableness: “what

would the typical reasonable person have understood by the exchange between the

officer and the suspect?”    Id. at 251.

       “We view the evidence in the light most favorable to the government and

must uphold a district court’s finding that a search is within the boundaries of the

consent unless it is clearly erroneous.”     United States v. Pena , 143 F.3d 1363,

1368 (10th Cir. 1998). While we have stated that a defendant’s “failure to object

to the . . . search of [a particular area] ‘may be considered an indication that the

search was within the scope of the consent,’”      id. (quoting United States v.

Espinosa , 782 F.2d 888, 892 (10th Cir. 1986)), this case presents a more narrow

issue: whether Mr. Osage’s failure to object to a search of a sealed can permitted




                                             -5-
the officer, in the course of conducting his search, to destroy the can or render it

completely useless for its intended function.     1
                                                      We conclude that it does not.

       The Supreme Court in      Jimeno held that “it was objectively reasonable for

the police to conclude that the general consent to search [defendant’s] car

included consent to search containers within that car which might bear drugs.”

Jimeno , 500 U.S. at 251. The Court accordingly upheld the opening and search of

a brown paper bag inside the car. However, the Court also stated, “[i]t is very

likely unreasonable to think that a suspect, by consenting to the search of his

trunk, has agreed to the breaking open of a locked briefcase within the trunk.”        Id.

at 251-52.

       We have not directly addressed the issue of whether a police search which

destroys or renders completely useless the item searched exceeds the scope of any

consent given for the search. However, we have hinted that a search could be “so

invasive or destructive” as to go beyond the scope of the search consented to.        See

United States v. Santurio , 29 F.3d 550, 553 (10th Cir. 1994) (noting that a “search

was not so invasive as to exceed the scope of defendant’s consent to the search”




       The government has never argued that Officer Salazar had articulable
       1

suspicion to briefly detain the cans for further investigation or probable cause to
seek a warrant. Officer Salazar has never claimed he did. At oral argument of
this appeal, the government specifically disavowed any reliance upon that ground.
Thus, this case involves only the validity and scope of Mr. Osage’s consent to the
search of the cans.

                                            -6-
where the officer “did not ‘tear up’ the van or enter the compartment” until a dog

alerted on the compartment). Other courts have reached the same conclusion.

See , e.g. , United States v. Torres , 32 F.3d 225, 231-32 (7th Cir. 1994) (“We agree

that ‘general permission to search does not include permission to inflict

intentional damage to the places or things to be searched.’”) (quoting     United

States v. Martinez , 949 F.2d 1117, 1119 (11th Cir. 1992));     United States v.

Strickland , 902 F.2d 937, 941-42 (11th Cir. 1990) (holding that a general consent

to search a car does not extend to the “intentional infliction of damage to the

vehicle or the property contained within it”);     State v. Garcia , 986 P.2d 491, 495

(N.M. Ct. App. 1999) (holding that “[d]efendant’s consent to permit the officers

to ‘look at’ her vehicle could not reasonably be interpreted to encompass drilling

into the vehicle.”), cert. granted , 990 P.2d 824 (N.M. Aug. 11, 1999).

       The district court relied upon   United States v. Kim , 27 F.3d 947 (3d Cir.

1994), United States v. Torres , 663 F.2d 1019 (10th Cir. 1981) and      United States

v. Pena , 920 F.2d 1509 (10th Cir. 1990), in support of its conclusion that Mr.

Osage’s silence while he watched Officer Salazar open the tamales can indicated

Mr. Osage’s consent to the search of the can. The government places great

reliance upon Kim in this appeal. In Kim , officers aboard an Amtrak train

received consent to search a handbag accompanying the defendant in his train

roomette. One of the officers found inside the bag six cans of “Naturade All-


                                             -7-
Natural Vegetable Protein” which “appeared to be factory-sealed cans with

factory lids which were intact.”     Kim , 27 F.3d at 950. The officer then “opened

one of the cans” and discovered methamphetamine inside.            Id.

       The Third Circuit upheld the search of the can as within the scope of the

permission granted. It relied upon     Jimeno for its conclusion that “when one gives

general permission to search for drugs in a confined area, that permission extends

to any items within that area that a reasonable person would believe to contain

drugs.” Id. at 956. It found no meaningful distinction between the brown paper

bag in Jimeno and the sealed cans in the case before it. Moreover, while

acknowledging that the Court in      Jimeno had stated that a search of a locked

suitcase in a vehicle would not be within the scope of a permissive search of the

vehicle, the Kim court summarily concluded “cans such as those found in the case

sub judice are not similar to locked briefcases.”    Id. at 957.

       We are not persuaded that     Kim requires us to reach the same conclusion in

this case. First, while the   Kim court evidently determined that a sealed can is

more like a brown paper bag than a locked briefcase, it provides no explanation

for that conclusion. Additionally, the court did not consider whether the can was

destroyed or rendered useless after being opened. Indeed, the court may have

assumed that it was not so damaged, because it relied upon and quoted the




                                             -8-
following reasoning from    United States v. Springs , 936 F.2d 1330, 1334-35 (D.C.

Cir. 1991) in support of its holding:

       the evidence supports a view that the opening of the baby powder
       container did not depend upon possession of a key, knowledge of a
       combination, or anything other than merely removing its lid.     Neither
       did the fact of its opening it render it useless, anymore than the
       opening of the folds destroyed the usefulness of the paper bag in
       Jimeno .

(emphasis added). We conclude that the opening of a sealed can, thereby

rendering it useless and incapable of performing its designated function, is more

like breaking open a locked briefcase than opening the folds of a paper bag.

       We acknowledge that the Supreme Court and this court have previously

stated that a general consent to search a particular area is reasonably understood

to extend to a search of containers within that area that could contain contraband,

absent some indication by the suspect that he wishes to terminate or limit the

search. See Jimeno , 500 U.S. at 252 (“[I]f [a suspect’s] consent would reasonably

be understood to extend to a particular container, the Fourth Amendment provides

no grounds for requiring a more explicit authorization.”);      United States v.

Gordon , 173 F.3d 761, 766 (10th Cir.) (“We consistently and repeatedly have held

a defendant’s failure to limit the scope of a general authorization to search, and

failure to object when the search exceeds what he later claims was a more limited

consent, is an indication the search was within the scope of consent.”),     cert.

denied , 120 S. Ct. 205 (1999). However, we do not read that authority to permit

                                            -9-
the destruction of such containers.   2
                                          We therefore hold that, before an officer may

actually destroy or render completely useless a container which would otherwise

be within the scope of a permissive search, the officer must obtain explicit

authorization, or have some other, lawful, basis upon which to proceed.

       For the foregoing reasons, the district court’s decision denying suppression

of the methamphetamine found in the tamales cans is REVERSED and the case is

REMANDED for further proceedings consistent herewith.




       2
        We do not read our prior cases in Torres and Pena, upon which the district
court relied, to compel a different result in this case. In Torres, a defendant gave
police permission to search a car. In conducting the search, the officers “pull[ed]
out an ashtray in the side of the door,” and “removed the air-vent cover in the side
of the door,” where they found contraband. Torres, 663 F.2d at 1021. We held
that search was “within the bounds of the actual consent given.” Id. at 1027.
       Similarly, in Pena, after receiving permission to search a vehicle, the police
officer “got a screwdriver . . . and removed the rear quarter panel vent” of the
vehicle, where he discovered contraband. Pena, 920 F.2d at 1512. The defendant
at no time objected to the search. We held that the search “was conducted within
the general scope of the permission granted.” Id. at 1515. Neither Pena nor
Torres involved the actual destruction of the item searched, as occurred in this
case.
       Other cases in our circuit have permitted some “dismantling” of an item
searched, but none have permitted complete and utter destruction or
incapacitation of an item or container. See, e.g., Pena, 143 F.3d at 1368 (holding
that consent to search motel room included “search into the area above the
bathroom ceiling” in the face of no objection by defendant); United States v.
McRae, 81 F.3d 1528, 1537-38 (10th Cir. 1996) (stating that consent to search car
trunk permitted officer to lift crinkled carpet area in the face of no objection by
defendant); Santurio, 29 F.3d at 552-53 (holding that consent to search interior of
car included removal of screws from strip holding down carpeting).

                                             -10-

```

---

## GROUP: _overhaul2/lake/cases/United States v. Padilla.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Padilla"
type: case
citation: "508 U.S. 77 (1993)"
parallel_cite: "113 S. Ct. 1936; 123 L. Ed. 2d 635"
neutral_cite: 1993 U.S. LEXIS 3126
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1993
date_decided: 1993-05-03
docket: 92-207
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1993-05-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Padilla
  varies_by_point: false
  scope_note: "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112856/united-states-v-padilla/"
  cluster_id: 112856
  opinion_id: 112856
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Alderman v. United States]]", "[[Rakas v. Illinois]]", "[[Rawlings v. Kentucky]]", "[[Soldal v. Cook County]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "conspiracy", "expectation-of-privacy"]
holding: "There is no 'coconspirator exception' to Fourth Amendment standing; a defendant's supervisory role in or joint control over a conspiracy does not by itself confer standing — only a personal privacy or property interest invaded by the search does."
lake:
  record_id: United States v. Padilla
  status: verified
  projected_at: 2026-07-09
---

# United States v. Padilla

*508 U.S. 77 (1993)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Members of a drug-trafficking conspiracy were prosecuted after police stopped and searched a car and found cocaine. The Ninth Circuit had adopted a "coconspirator exception" to standing: a co-conspirator could challenge a search if he had either a supervisory role in the conspiracy or joint control over the place or property searched. Applying that rule, it allowed several respondents to contest the stop and search even without a personal interest in the car.

## Issue
Whether a defendant may challenge a search on the strength of his supervisory role in, or joint control over property used by, a criminal conspiracy — that is, whether a "coconspirator exception" supplements the rule that [[Standing to Challenge a Search|Fourth Amendment standing]] requires a personal privacy or possessory interest.

## Rule
No; standing is personal and the conspiracy adds nothing to it. Quoting *[[Alderman v. United States|Alderman]]*: "suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Co-conspirators and codefendants have been accorded no special standing." — 508 U.S. at 82 (quoting *Alderman v. United States*, 394 U.S. 165, 171–172). ^pin-82

"Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them." — [*Id.* at 82](https://www.courtlistener.com/opinion/112856/united-states-v-padilla/#:~:text=Expectations%20of%20privacy%20and%20property). ^pin-82b

## Application
The respondents' positions in the conspiracy — one serving as the "communication link," others "in charge of transportation" — had "no bearing on their respective Fourth Amendment rights." Whether any of them could suppress the cocaine turned, case by case, on whether that respondent personally held a property interest interfered with by the stop or a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] invaded by the search of the car — not on his conspiratorial role. The Ninth Circuit's exception both contradicted *[[Alderman v. United States|Alderman]]* and was at odds with the personal-rights principle.

## Conclusion
[[Common Legal Terms#per-curiam|Per curiam]]: the "coconspirator exception" was rejected; the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]] for individualized determinations of each respondent's personal Fourth Amendment interest.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Padilla* reaffirms the personal-rights standing rule of [[Alderman v. United States]] and [[Rakas v. Illinois]], rooted in the privacy/property interests of [[Rawlings v. Kentucky]] and [[Soldal v. Cook County]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *United States v. Padilla*, 508 U.S. 77 (1993) — https://www.courtlistener.com/opinion/112856/united-states-v-padilla/ — pinpoint: 82.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "982f6d5d175ff111", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Padilla"}, "payload": {"all": [{"cite": "508 U.S. 77", "page": "77", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "508"}, {"cite": "113 S. Ct. 1936", "page": "1936", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "123 L. Ed. 2d 635", "page": "635", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "123"}, {"cite": "1993 U.S. LEXIS 3126", "page": "3126", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1993"}], "display": "508 U.S. 77", "official": {"cite": "508 U.S. 77", "page": "77", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "508"}, "official_selection_present": true, "record_id": "United States v. Padilla"}}
{"assertion_id": "21b586a0568e2efa", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-82b", "record_id": "United States v. Padilla"}, "payload": {"fragment": "#:~:text=Expectations%20of%20privacy%20and%20property", "page": null, "pin_id": "pin-82b", "pinpoint_status": "star-verified", "quote": "Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them.", "quote_fidelity": "matched", "record_id": "United States v. Padilla", "star_marker": "82"}}
{"assertion_id": "6e443a607256e67e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-82", "record_id": "United States v. Padilla"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-82", "pinpoint_status": "slip-only", "quote": "supplements the rule that Fourth Amendment standing requires a personal privacy or possessory interest. ## Rule No; standing is personal and the conspiracy adds nothing to it. Quoting *Alderman*:", "quote_fidelity": "mismatch", "record_id": "United States v. Padilla", "star_marker": null}}
{"assertion_id": "c45d9059ab0e4f88", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Padilla"}, "payload": {"as_of_content": "1993-05-03", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Padilla", "scope_note": "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law.", "varies_by_point": false}}
```

### lake record — United States v. Padilla

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Padilla",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Padilla",
    "case_name_short": "Padilla",
    "case_name_full": "UNITED STATES v. PADILLA Et Al.",
    "input_case_name": "United States v. Padilla",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1993-05-03",
    "year": 1993,
    "docket": "92-207",
    "cluster_id": 112856,
    "lead_opinion_id": 112856,
    "sibling_ids": [
      112856
    ],
    "absolute_url": "/opinion/112856/united-states-v-padilla/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "508 U.S. 77",
      "volume": "508",
      "reporter": "U.S.",
      "page": "77",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "113 S. Ct. 1936",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 L. Ed. 2d 635",
        "volume": "123",
        "reporter": "L. Ed. 2d",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1993 U.S. LEXIS 3126",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "3126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "508 U.S. 77",
        "volume": "508",
        "reporter": "U.S.",
        "page": "77",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 1936",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "1936",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "123 L. Ed. 2d 635",
        "volume": "123",
        "reporter": "L. Ed. 2d",
        "page": "635",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. LEXIS 3126",
        "volume": "1993",
        "reporter": "U.S. LEXIS",
        "page": "3126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "508 U.S. 77",
    "official_selection": {
      "court_class": "scotus",
      "selected": "508 U.S. 77",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-82",
      "page": null,
      "quote": "supplements the rule that Fourth Amendment standing requires a personal privacy or possessory interest. ## Rule No; standing is personal and the conspiracy adds nothing to it. Quoting *Alderman*:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-82b",
      "page": null,
      "quote": "Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them.",
      "star_marker": "82",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 9952,
      "fragment": "#:~:text=Expectations%20of%20privacy%20and%20property",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1993-05-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Padilla",
    "varies_by_point": false,
    "scope_note": "Rejects the Ninth Circuit's coconspirator exception; standing remains personal. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Padilla",
          "cluster_id": 7042664,
          "cite": [
            "111 F.3d 685",
            "97 Cal. Daily Op. Serv. 2744",
            "97 Daily Journal DAR 4867",
            "1997 U.S. App. LEXIS 7123"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cardona-Sandoval",
          "cluster_id": 194957,
          "cite": [
            "6 F.3d 15",
            "1993 WL 374897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cedeno",
          "cluster_id": 6096982,
          "cite": [
            "193 A.D.2d 540",
            "598 N.Y.S.2d 192",
            "1993 N.Y. App. Div. LEXIS 5275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane1_negative"
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
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 195094,
          "cite": [
            "15 F.3d 1161"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, Plaintiff-Appellee/cross-Appellant v. Rene Gonzalez-Lerma, Defendant-Appellant/cross-Appellee",
          "cluster_id": 661539,
          "cite": [
            "14 F.3d 1479",
            "1994 U.S. App. LEXIS 1539"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "CAMP Legal Defense Fund, Inc. v. City of Atlanta",
          "cluster_id": 77366,
          "cite": [
            "451 F.3d 1257",
            "2006 U.S. App. LEXIS 14407",
            "2006 WL 1623279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sarkisian",
          "cluster_id": 7079538,
          "cite": [
            "197 F.3d 966",
            "1999 WL 1083966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moreno v. Baca",
          "cluster_id": 792690,
          "cite": [
            "431 F.3d 633",
            "2005 WL 3338300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Robert Dale Lowe, Jr.",
          "cluster_id": 4472370,
          "cite": [
            "812 N.W.2d 554",
            "2012 Iowa Sup. LEXIS 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hunter Lee Williams Nicholas Edward George and Geoffrey Hillman Leek",
          "cluster_id": 784663,
          "cite": [
            "354 F.3d 497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald L. Lingenfelter, United States of America v. Gary Marolf, AKA Gary Marlow, United States of America v. Lawrence Morgan",
          "cluster_id": 610679,
          "cite": [
            "997 F.2d 632",
            "93 Daily Journal DAR 8410",
            "93 Cal. Daily Op. Serv. 4978",
            "1993 U.S. App. LEXIS 15893"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Ervin Payne, United States of America v. Christopher Foster",
          "cluster_id": 744110,
          "cite": [
            "119 F.3d 637",
            "1997 U.S. App. LEXIS 17325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vasak Sarkisian, United States of America v. Vitaly Semenov, United States of America v. Ashot Mikayelyan, United States of America v. Sergey Ivanchikov",
          "cluster_id": 766923,
          "cite": [
            "197 F.3d 966",
            "99 Daily Journal DAR 12221",
            "99 Cal. Daily Op. Serv. 9472",
            "1999 U.S. App. LEXIS 31553"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lopez-Lopez",
          "cluster_id": 199833,
          "cite": [
            "282 F.3d 1",
            "2002 U.S. App. LEXIS 2896",
            "2002 WL 229881"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Eric Powell",
          "cluster_id": 4346362,
          "cite": [
            "847 F.3d 760",
            "2017 FED App. 0025p",
            "2017 WL 474343",
            "2017 U.S. App. LEXIS 2093"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 1746991,
          "cite": [
            "648 So. 2d 669",
            "1994 WL 620797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Torres",
          "cluster_id": 198221,
          "cite": [
            "162 F.3d 6",
            "1998 U.S. App. LEXIS 30808",
            "1998 WL 823184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arturo Torres and Ramon R. Vargas-Hernandez, Also Known as Ramon Vargas",
          "cluster_id": 676092,
          "cite": [
            "32 F.3d 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzales",
          "cluster_id": 157368,
          "cite": [
            "164 F.3d 1285",
            "1999 WL 5092"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Ramos, United States of America v. Richard Ramos",
          "cluster_id": 659415,
          "cite": [
            "12 F.3d 1019",
            "1994 WL 2259",
            "1994 U.S. App. LEXIS 973"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gene Hinton (070386)",
          "cluster_id": 1086776,
          "cite": [
            "216 N.J. 211",
            "78 A.3d 553",
            "2013 WL 5745595",
            "2013 N.J. LEXIS 1092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Laura Michelle Morning, United States of America v. Francisco Ignacio Leon-Yanez",
          "cluster_id": 702612,
          "cite": [
            "64 F.3d 531",
            "95 Cal. Daily Op. Serv. 6773",
            "95 Daily Journal DAR 11651",
            "1995 U.S. App. LEXIS 24192",
            "1995 WL 505229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Coleman, United States of America v. Andre Worthy, United States of America v. Orlando Willis",
          "cluster_id": 784218,
          "cite": [
            "349 F.3d 1077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzales",
          "cluster_id": 760543,
          "cite": [
            "164 F.3d 1285",
            "1999 Colo. J. C.A.R. 1285",
            "1999 U.S. App. LEXIS 218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Courtney Noble",
          "cluster_id": 2716405,
          "cite": [
            "762 F.3d 509",
            "2014 WL 3882493",
            "2014 U.S. App. LEXIS 15279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Veronica M. Thompson and Veronica Andalon",
          "cluster_id": 735368,
          "cite": [
            "106 F.3d 794",
            "1997 U.S. App. LEXIS 2281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Padilla:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112856) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 89,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 89,
        "triage_read": 4,
        "triage_snippet_classified": 85
      },
      "lane2_top_cited": {
        "query": "cites:(112856)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMSZzPTE0MzY0MzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112856%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112856)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112856)",
    "indexed_citing_opinions": 120,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112856,
        "count": 120,
        "count_source": "search"
      }
    ],
    "citation_count": 197,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-padilla.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjM4NDY5Mjgmcz0xMDM0NDAzJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112856%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112856,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 110326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 341773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 343457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 387237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 441830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 545151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 571310,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112856,
        "cited_id": 580800,
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
    "date_created": "2026-07-06T01:58:19Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:07:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T01:58:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Padilla

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b126-5">
  Per Curiam.
 </author>
<p id="b126-6">
  The United States Court of Appeals for the Ninth Circuit has adopted what it terms a “coconspirator exception” to the rule regarding who may challenge the constitutionality of a search or seizure. Under its reasoning, a co-conspirator obtains a legitimate expectation of privacy for Fourth Amendment purposes if he has either a supervisory role in the conspiracy or joint control over the place or property involved in the search or seizure. This “exception,” apparently developed in a series of earlier decisions of the Court of Appeals, squarely contradicts the controlling case from this Court. We therefore reject it.
 </p>
<p id="b126-7">
  While patrolling Interstate Highway 10 in Casa Grande, Arizona, Officer Russel Fifer spotted a Cadillac traveling westbound at approximately 65 miles per hour. Fifer followed the Cadillac for several miles because he thought the driver acted suspiciously as he passed the patrol car. Fifer ultimately stopped the Cadillac because it was going too slowly. Luis Arciniega, the driver and sole occupant of the car, gave Fifer his driver’s license and an insurance card demonstrating that respondent Donald Simpson, a United States customs agent, owned the Cadillac. Fifer and Robert Williamson, an officer who appeared on the scene to assist Fifer, believed that Arciniega matched the drug courier profile. Acting on this belief, they requested and received Arci
  <span citation-index="1" class="star-pagination" label="79"> 
   *79
   </span>
  niega’s permission to search the vehicle. The officers found 560 pounds of cocaine in the trunk and immediately arrested Arciniega.
 </p>
<p id="b127-4">
  After agreeing to make a controlled delivery of the cocaine, Arciniega made a telephone call to his contact from a motel in Tempe, Arizona. Respondents Jorge and Maria Padilla drove to the motel in response to the telephone call, but were arrested as they attempted to drive away in the Cadillac. Like Arciniega, Maria Padilla agreed to cooperate with law enforcement officials. She led them to the house in which her husband, respondent Xavier Padilla, was staying. The ensuing investigation linked Donald Simpson and his wife, respondent Maria Sylvia Simpson, to Xavier Padilla.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b127-5">
  Respondents were charged with conspiracy to distribute and possess with intent to distribute cocaine, in violation of <span class="citation no-link">21 U. S. C. §846</span>, and possession of cocaine with intent to distribute, in violation of § 841(a)(1). Xavier Padilla was also charged with engaging in a continuing criminal enterprise, in violation of <span class="citation no-link">21 U. S. C. § 848</span> (1988 ed. and Supp. III). Respondents moved to suppress all evidence discovered in the course of the investigation, claiming that the evidence was the fruit of the unlawful investigatory stop of Arciniega’s vehicle. The United States District Court for the District of Arizona ruled that all respondents were entitled to challenge the stop and search because they were involved in “a joint venture for transportation... that had control of the contraband.” App. to Pet. for Cert. 22a. The District Court reasoned that, as owners, the Simpsons retained a reasonable expectation of privacy in their car, but that the Padillas could
  <span citation-index="1" class="star-pagination" label="80"> 
   *80
   </span>
  contest the stop solely because of their supervisory roles and their “joint control over a very sophisticated operation----”
  <em>
   <span class="citation no-link">Id.,</span>
  </em>
  at 23a. On the merits, the District Court ruled that Officer Fifer lacked reasonable suspicion to stop Areiniega,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and granted respondents’ motion to suppress.
 </p>
<p id="b128-7">
  The Court of Appeals affirmed in part, vacated in part, and remanded. The court began its analysis by stating that in order “[t]o contest the legality of a search and seizure, the defendants must establish that they had a legitimate expectation of privacy’ in the place searched or the property seized.” <span class="citation multiple-matches"><a href="/c/F.%202d/960/854/">960 F. 2d 854</a></span>, 858-859 (CA9 1992) (quoting
  <em>
   Bakas
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143-144</a></span> (1978)). The court then recited its eoeonspirator rule: “[A] coconspirator’s participation in an operation or arrangement that indicates joint control and supervision of the place searched establishes standing.” 960 F. 2d, at 859 (citations omitted).
 </p>
<p id="b128-8">
  Relying on a line of eases from the Ninth Circuit, the court held that “because Xavier Padilla and Donald and Maria Simpson have demonstrated joint control and supervision over the drugs and vehicle and engaged in an active participation in a formalized business arrangement, they have standing to claim a legitimate expectation of privacy in the property searched and the items seized.”
  <em>
   Id.,
  </em>
  at 860-861. Donald Simpson established an expectation of privacy “not simply because [he] owned the car” but also because “he had a coordinating and supervisory role in the operation. He was a critical player in the transportation scheme who was essential in getting the drugs across the border.”
  <em>
   Id.,
  </em>
  at 860. Maria Simpson established a privacy interest because she “provided a communication link” between her husband, Xavier Padilla, and other members of the conspiracy, and “held a supervisory role tying everyone together and overseeing the entire operation.”
  <em>
   Ibid.
  </em>
  Xavier Padilla established an expectation of privacy because he “exhibited sub
  <span citation-index="1" class="star-pagination" label="81"> 
   *81
   </span>
  stantial control and oversight with respect to the purchase [and] the transportation through Arizona.”
  <em>
   Ibid.
  </em>
  The court expressly stated that it did not matter that Padilla was not present during the stop, or that he could not exclude others from searching the Cadillac. Ibid.
 </p>
<p id="b129-5">
  The Court
  <em>
   of
  </em>
  Appeals could not tell from the record whether Jorge and Maria Padilla “shared any responsibility for the enterprise,” or whether they were “mere employees in a family operation.”
  <em>
   Id.,
  </em>
  at 861. As a result, the court remanded to the District Court for further findings on that issue.
 </p>
<p id="b129-6">
  The Ninth Circuit appears to stand alone in embracing the “eoconspirator exception.”
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We granted certiorari to resolve the conflict, <span class="citation multiple-matches"><a href="/c/U.%20S./506/952/">506 U. S. 952</a></span> (1992), and now reverse. It has long been the rule that a defendant can urge the suppression of evidence obtained in violation of the Fourth Amendment only if that defendant demonstrates that
  <em>
   his
  </em>
  Fourth Amendment rights were violated by the challenged search or seizure.
  <em>
   Alderman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#171" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 171-172</a></span> (1969);
  <em>
   Rakas
  </em>
  v.
  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#131" aria-description="Citation for case: Rakas v. Illinois"><em>
   Illinois, supra,
  </em>
  at 131, n. 1, 133-134</a></span>;
  <em>
   Rawlings
  </em>
  v.
  <em>
   Kentucky,
  </em>
  <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/#106" aria-description="Citation for case: Rawlings v. Kentucky">448 U. S. 98, 106</a></span> (1980). We applied this principle to the case of co-conspirators in
  <em>
   <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span>,
  </em>
  in which we said:
 </p>
<blockquote id="b129-7">
  “The established principle is that suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated
  <span citation-index="1" class="star-pagination" label="82"> 
   *82
   </span>
  by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Co-conspirators and codefendants have been accorded no special standing.” 894 U. S., at 171-172.
 </blockquote>
<p id="b130-5">
  In
  <em>
   <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas, supra,</a></span>
  </em>
  a police search of a car yielded a box of rifle shells found in the glove compartment and a sawed-off rifle found under the passenger seat. We held that petitioners, who were passengers in the car and had no ownership interest in the rifle shells or sawed-off rifle, and no legitimate expectation of privacy in the area searched, had suffered no invasion of their Fourth Amendment rights. See also
  <em>
   <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">Rawlings, supra;</a></span> Soldal
  </em>
  v.
  <em>
   Cook County,
  </em>
  <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/#62" aria-description="Citation for case: Soldal v. Cook County">506 U. S. 56, 62-64</a></span> (1992) (decided since the Court of Appeals rendered its decision in the present case).
 </p>
<p id="b130-6">
  The “coconspirator exception” developed by the Ninth Circuit is, therefore, not only contrary to the holding of
  <em>
   Aider-man,
  </em>
  but at odds with the principle discussed above. Expectations of privacy and property interests govern the analysis of Fourth Amendment search and seizure claims. Participants in a criminal conspiracy may have such expectations or interests, but the conspiracy itself neither adds to nor detracts from them. Neither the fact, for example, that Maria Simpson was the “communication link” between her husband and the others, nor the fact that Donald Simpson and Xavier Padilla were in charge of transportation for the conspirators, has any bearing on their respective Fourth Amendment rights.
 </p>
<p id="b130-7">
  We therefore reverse the judgment of the Court of Appeals. The case is remanded so that the court may consider whether each respondent had either a property interest protected by the Fourth Amendment that was interfered with by the stop of the automobile driven by Arciniega, or a reasonable expectation of privacy that was invaded by the search thereof.
  <em>
   <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman, supra;</a></span> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas, supra;</a></span> <span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">Rawlings, supra;</a></span> <span class="citation" data-id="112795"><a href="/opinion/112795/soldal-v-cook-county/" aria-description="Citation for case: Soldal v. Cook County">Soldal, supra.</a></span>
  </em>
</p>
<p id="b130-8">
<em>
   It is so ordered.
  </em>
</p>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b127-6">
   A related investigation led by the Drug Enforcement Agency (DEA) revealed that Warren Strubbe was also involved in the conspiracy. Although Strubbe technically is a respondent in this case, see this Court’s Rule 12.4, the Court of Appeals found that he could not challenge the stop and search of the Cadillac. Strubbe did not file a petition challenging that decision, and we therefore do not address that aspect of the court’s opinion.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b128-9">
   The Government did not challenge this finding on appeal and does not do so here.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b129-8">
   The First, Second, Fifth, Sixth, Eighth, Eleventh, and District of Columbia Circuits have declined to adopt an exception for co-conspirators or codefendants. See
   <em>
    United States
   </em>
   v.
   <em>
    Soule,
   </em>
   <span class="citation" data-id="545151"><a href="/opinion/545151/united-states-v-john-jeffrey-soule/#1036" aria-description="Citation for case: United States v. John Jeffrey Soule">908 F. 2d 1032, 1036-1037</a></span> (CA1 1990);
   <em>
    United States
   </em>
   v.
   <em>
    Galante,
   </em>
   <span class="citation" data-id="9463409"><a href="/opinion/341773/united-states-v-john-frank-galante-and-theodore-n-cameriero/#739" aria-description="Citation for case: United States v. John Frank Galante and Theodore N....">547 F. 2d 733, 739-740</a></span> (CA2 1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./431/969/">431 U. S. 969</a></span> (1977);
   <em>
    United States
   </em>
   v.
   <em>
    Hunter,
   </em>
   <span class="citation" data-id="343457"><a href="/opinion/343457/united-states-v-sheryl-hunter-and-ezell-allen/#1074" aria-description="Citation for case: United States v. Sheryl Hunter and Ezell Allen">550 F. 2d 1066, 1074</a></span> (CA6 1977);
   <em>
    United States
   </em>
   v.
   <em>
    DeLeon,
   </em>
   <span class="citation" data-id="387237"><a href="/opinion/387237/united-states-v-becaficio-saenz-deleon/#337" aria-description="Citation for case: United States v. Becaficio Saenz Deleon">641 F. 2d 330, 337</a></span> (CA5 1981);
   <em>
    United States
   </em>
   v.
   <em>
    Kiser,
   </em>
   <span class="citation" data-id="571310"><a href="/opinion/571310/united-states-v-stanley-carter-kiser/#424" aria-description="Citation for case: United States v. Stanley Carter Kiser">948 F. 2d 418, 424</a></span> (CA8 1991), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./503/983/">503 U. S. 983</a></span> (1992);
   <em>
    United States
   </em>
   v.
   <em>
    Brown,
   </em>
   <span class="citation" data-id="9472640"><a href="/opinion/441830/united-states-v-bruce-christian-brown-and-james-patrick-manikowski/#1507" aria-description="Citation for case: United States v. Bruce Christian Brown and James Patrick...">743 F. 2d 1505, 1507-1508</a></span> (CA11 1984);
   <em>
    United States
   </em>
   v.
   <em>
    Davis,
   </em>
   199 U. S. App. D. C. 95, 108, <span class="citation" data-id="375882"><a href="/opinion/375882/united-states-v-robert-h-davis-united-states-of-america-v-george-d/#690" aria-description="Citation for case: United States v. Robert H. Davis, United States of...">617 F. 2d 677, 690</a></span> (1979).
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Patane.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Patane"
type: case
citation: "542 U.S. 630 (2004)"
parallel_cite: "124 S. Ct. 2620; 159 L. Ed. 2d 667"
neutral_cite: 2004 U.S. LEXIS 4577
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Patane
  varies_by_point: false
  scope_note: "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137003/united-states-v-patane/"
  cluster_id: 137003
  opinion_id: 137003
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oregon v. Elstad]]", "[[Dickerson v. United States]]", "[[Missouri v. Seibert]]", "[[New York v. Quarles]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "self-incrimination", "physical-fruits", "fruit-of-the-poisonous-tree"]
holding: "Physical fruits of an un-warned but voluntary statement are admissible."
lake:
  record_id: United States v. Patane
  status: verified
  projected_at: 2026-07-06
---

# United States v. Patane

*542 U.S. 630 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Patane was arrested in connection with a restraining-order violation. As an officer began to advise him of his *[[Miranda v. Arizona|Miranda]]* rights, Patane interrupted, saying he knew his rights, and the officer stopped. Patane then told the officers he had a Glock pistol in his bedroom. Because Patane was a convicted felon, the pistol supported a felon-in-possession charge. He moved to suppress the gun as the fruit of his unwarned statement. The Tenth Circuit ordered suppression; the Supreme Court reversed.

## Issue
Whether a failure to give *[[Miranda v. Arizona|Miranda]]* warnings requires suppression of the physical fruits — here, a pistol — of a suspect's unwarned but voluntary statements.

## Rule
No. The *[[Miranda v. Arizona|Miranda]]* rule is a prophylactic safeguard for the Self-Incrimination Clause, and that Clause is not violated by admitting the nontestimonial physical fruit of a voluntary statement. The plurality explained: "The Self-Incrimination Clause, however, is not implicated by the admission into evidence of the physical fruit of a voluntary statement. Accordingly, there is no justification for extending the *Miranda* rule to this context." — 542 U.S. at 636. ^pin-636

Because a mere failure to warn is not itself a constitutional violation, "the exclusionary rule articulated in cases such as *Wong Sun* does not apply." — *Id.* at 637. ^pin-637

## Application
Patane's statement about the Glock was voluntary, and the pistol was nontestimonial physical evidence. Admitting that physical fruit did not compel Patane to be a witness against himself, so the Self-Incrimination Clause was not violated and the failure to warn did not require suppressing the gun. The plurality observed that the case for admitting nontestimonial physical fruits (the Glock) was even stronger than the case for admitting the postwarning statements held admissible in *[[Oregon v. Elstad]]* and *[[Michigan v. Tucker]]*.

## Conclusion
The failure to give *[[Miranda v. Arizona|Miranda]]* warnings did not require suppression of the pistol; the Supreme Court reversed the Tenth Circuit and [[Reading and Citing Cases#on-remand|remanded]]. (Plurality opinion; Justices Kennedy and O'Connor concurred in the judgment, agreeing the gun need not be suppressed.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Though a fractured plurality, *Patane*'s result controls: the physical fruits of an unwarned but voluntary statement are admissible. It refines the [[Oregon v. Elstad]] line and the constitutional-rule holding of [[Dickerson v. United States]], distinguishing the deliberate two-step problem addressed the same Term in [[Missouri v. Seibert]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Patane*, 542 U.S. 630 (2004) — https://www.courtlistener.com/opinion/137003/united-states-v-patane/ — pinpoints: 636, 637 (parallel 124 S. Ct. 2620).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4ef1825eb241919f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Patane"}, "payload": {"all": [{"cite": "542 U.S. 630", "page": "630", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "542"}, {"cite": "124 S. Ct. 2620", "page": "2620", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "159 L. Ed. 2d 667", "page": "667", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "159"}, {"cite": "2004 U.S. LEXIS 4577", "page": "4577", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "542 U.S. 630", "official": {"cite": "542 U.S. 630", "page": "630", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "542"}, "official_selection_present": true, "record_id": "United States v. Patane"}}
{"assertion_id": "3cae9a640156104b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-637", "record_id": "United States v. Patane"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-637", "pinpoint_status": "slip-only", "quote": "the exclusionary rule articulated in cases such as *Wong Sun* does not apply.", "quote_fidelity": "mismatch", "record_id": "United States v. Patane", "star_marker": null}}
{"assertion_id": "edd2c7020e4ed11e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-636", "record_id": "United States v. Patane"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-636", "pinpoint_status": "slip-only", "quote": "--- # United States v. Patane *542 U.S. 630 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Patane was arrested in connection with a restraining-order violation. As an officer began to advise him of his *Miranda* rights, Patane interrupted, saying he knew his rights, and the officer stopped. Patane then told the officers he had a Glock pistol in his bedroom. Because Patane was a convicted felon, the pistol supported a felon-in-possession charge. He moved to suppress the gun as the fruit of his unwarned statement. The Tenth Circuit ordered suppression; the Supreme Court reversed. ## Issue Whether a failure to give *Miranda* warnings requires suppression of the physical fruits — here, a pistol — of a suspect's unwarned but voluntary statements. ## Rule No. The *Miranda* rule is a prophylactic safeguard for the Self-Incrimination Clause, and that Clause is not violated by admitting the nontestimonial physical fruit of a voluntary statement. The plurality explained:", "quote_fidelity": "mismatch", "record_id": "United States v. Patane", "star_marker": null}}
{"assertion_id": "211064cd63bbb046", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Patane"}, "payload": {"as_of_content": "2004-06-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Patane", "scope_note": "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment.", "varies_by_point": false}}
```

### lake record — United States v. Patane

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Patane",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Patane",
    "case_name_short": "Patane",
    "case_name_full": "United States v. Patane",
    "input_case_name": "United States v. Patane",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-28",
    "year": 2004,
    "docket": null,
    "cluster_id": 137003,
    "lead_opinion_id": 137003,
    "sibling_ids": [
      137003,
      9434686,
      9434687,
      9434688,
      9434689
    ],
    "absolute_url": "/opinion/137003/united-states-v-patane/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "542 U.S. 630",
      "volume": "542",
      "reporter": "U.S.",
      "page": "630",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2620",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2620",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 667",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4577",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 630",
        "volume": "542",
        "reporter": "U.S.",
        "page": "630",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2620",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2620",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 667",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "667",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4577",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4577",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "542 U.S. 630",
    "official_selection": {
      "court_class": "scotus",
      "selected": "542 U.S. 630",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-636",
      "page": null,
      "quote": "--- # United States v. Patane *542 U.S. 630 (2004)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Patane was arrested in connection with a restraining-order violation. As an officer began to advise him of his *Miranda* rights, Patane interrupted, saying he knew his rights, and the officer stopped. Patane then told the officers he had a Glock pistol in his bedroom. Because Patane was a convicted felon, the pistol supported a felon-in-possession charge. He moved to suppress the gun as the fruit of his unwarned statement. The Tenth Circuit ordered suppression; the Supreme Court reversed. ## Issue Whether a failure to give *Miranda* warnings requires suppression of the physical fruits \u2014 here, a pistol \u2014 of a suspect's unwarned but voluntary statements. ## Rule No. The *Miranda* rule is a prophylactic safeguard for the Self-Incrimination Clause, and that Clause is not violated by admitting the nontestimonial physical fruit of a voluntary statement. The plurality explained:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-637",
      "page": null,
      "quote": "the exclusionary rule articulated in cases such as *Wong Sun* does not apply.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Patane",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; Kennedy and O'Connor, JJ., concurred in the judgment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jones",
          "cluster_id": 4517594,
          "cite": [
            "193 A.3d 957"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cleveland v. Oles (Slip Opinion)",
          "cluster_id": 4410433,
          "cite": [
            "2017 Ohio 5834",
            "92 N.E.3d 810",
            "152 Ohio St. 3d 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "NYIA GORE v. UNITED STATES",
          "cluster_id": 4248978,
          "cite": [
            "145 A.3d 540",
            "2016 D.C. App. LEXIS 313",
            "2016 WL 4411321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Broom a/k/a Patrick Brown v. United States",
          "cluster_id": 2809687,
          "cite": [
            "118 A.3d 207",
            "2015 D.C. App. LEXIS 265",
            "2015 WL 3768885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of J.T.M., a Juvenile",
          "cluster_id": 3076829,
          "cite": [
            "441 S.W.3d 455",
            "2014 WL 949949",
            "2014 Tex. App. LEXIS 2910"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McCallum",
          "cluster_id": 2661991,
          "cite": [
            "885 F. Supp. 2d 105",
            "2012 WL 3289767"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gonzalez",
          "cluster_id": 2319916,
          "cite": [
            "25 A.3d 648",
            "302 Conn. 287",
            "2011 Conn. LEXIS 355",
            "2011 WL 3802478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simon",
          "cluster_id": 2483876,
          "cite": [
            "456 Mass. 280",
            "923 N.E.2d 58",
            "2010 Mass. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Swain v. State",
          "cluster_id": 1490445,
          "cite": [
            "181 S.W.3d 359",
            "2005 Tex. Crim. App. LEXIS 1864",
            "2005 WL 2861584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Davis",
          "cluster_id": 2575950,
          "cite": [
            "115 P.3d 417",
            "31 Cal. Rptr. 3d 96",
            "36 Cal. 4th 510",
            "2005 Cal. Daily Op. Serv. 6393",
            "2005 Daily Journal DAR 8733",
            "2005 Cal. LEXIS 7963"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People in the Interest of B.D",
          "cluster_id": 4611859,
          "cite": [
            "2019 COA 57"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. David Hooper Climer, Jr.",
          "cluster_id": 1043889,
          "cite": [
            "400 S.W.3d 537",
            "2013 WL 1694804",
            "2013 Tenn. LEXIS 354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vega v. Tekoh",
          "cluster_id": 6480695,
          "cite": [
            "597 U.S. 134",
            "213 L. Ed. 2d 479",
            "142 S. Ct. 2095"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Knapp",
          "cluster_id": 1713730,
          "cite": [
            "2005 WI 127",
            "700 N.W.2d 899",
            "285 Wis. 2d 86",
            "2005 Wisc. LEXIS 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Desmond v. Mukasey",
          "cluster_id": 187228,
          "cite": [
            "530 F.3d 944",
            "382 U.S. App. D.C. 31",
            "20 Am. Disabilities Cas. (BNA) 1291",
            "2008 U.S. App. LEXIS 13803",
            "2008 WL 2583022"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chamberlin v. State",
          "cluster_id": 1638526,
          "cite": [
            "989 So. 2d 320",
            "2008 WL 2761889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clay v. State",
          "cluster_id": 2506826,
          "cite": [
            "725 S.E.2d 260",
            "290 Ga. 822",
            "2012 Fulton County D. Rep. 982",
            "2012 Ga. LEXIS 301"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy Stewart",
          "cluster_id": 788327,
          "cite": [
            "388 F.3d 1079",
            "2004 U.S. App. LEXIS 23395",
            "2004 WL 2523358"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. O'NEILL",
          "cluster_id": 1946717,
          "cite": [
            "936 A.2d 438",
            "193 N.J. 148",
            "2007 N.J. LEXIS 1507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santiago",
          "cluster_id": 2306570,
          "cite": [
            "980 A.2d 659",
            "2009 Pa. Super. 169",
            "2009 Pa. Super. LEXIS 3268",
            "2009 WL 2634846"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Carrizales-Toledo",
          "cluster_id": 167815,
          "cite": [
            "454 F.3d 1142",
            "2006 U.S. App. LEXIS 18280",
            "2006 WL 2022911"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Larry D. Peterson and Larry D. Willis",
          "cluster_id": 790977,
          "cite": [
            "414 F.3d 825",
            "2005 U.S. App. LEXIS 14431",
            "2005 WL 1661259"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pettigrew",
          "cluster_id": 167856,
          "cite": [
            "468 F.3d 626",
            "2006 U.S. App. LEXIS 28128",
            "2006 WL 2946893"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Vondehn",
          "cluster_id": 835033,
          "cite": [
            "236 P.3d 691",
            "348 Or. 462",
            "2010 Ore. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mole (Slip Opinion)",
          "cluster_id": 4242422,
          "cite": [
            "2016 Ohio 5124",
            "149 Ohio St. 3d 215",
            "74 N.E.3d 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Vance",
          "cluster_id": 2277859,
          "cite": [
            "188 Cal. App. 4th 1182",
            "116 Cal. Rptr. 3d 98",
            "2010 Cal. App. LEXIS 1691"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welch v. Commonwealth",
          "cluster_id": 1793000,
          "cite": [
            "149 S.W.3d 407",
            "2004 Ky. LEXIS 276",
            "2004 WL 2623964"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2282662,
          "cite": [
            "183 Cal. App. 4th 253",
            "107 Cal. Rptr. 3d 228",
            "2010 Cal. App. LEXIS 429"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Popenhagen",
          "cluster_id": 1917034,
          "cite": [
            "2008 WI 55",
            "749 N.W.2d 611",
            "309 Wis. 2d 601",
            "2008 Wisc. LEXIS 307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Patane:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTkwODUxMjAwMDAwJnM9MTQ3NzQ3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NCZzPTg5NDk4NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 1,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137003 OR 9434686 OR 9434687 OR 9434688 OR 9434689)",
    "indexed_citing_opinions": 344,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137003,
        "count": 276,
        "count_source": "search"
      },
      {
        "opinion_id": 9434686,
        "count": 75,
        "count_source": "search"
      },
      {
        "opinion_id": 9434687,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434688,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434689,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 620,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-patane.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NDI3OCZzPTk0NDMzMzUmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28137003+OR+9434686+OR+9434687+OR+9434688+OR+9434689%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137003,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 107739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 108541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 118242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 162589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 200020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 775633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 776886,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 783781,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 1087666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 2021779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137003,
        "cited_id": 2125014,
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
    "date_created": "2026-07-06T02:07:43Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T02:12:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T02:07:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Patane

```
<div>
<center><b><span class="citation" data-id="9434686"><a href="/opinion/137003/united-states-v-patane/" aria-description="Citation for case: United States v. Patane">542 U.S. 630</a></span> (2004)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
PATANE</h1></center>
<center>No. 02-1183.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 2003.</center>
<center>Decided June 28, 2004.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE TENTH CIRCUIT.
<p><span class="star-pagination">*631</span> <span class="star-pagination">*632</span> <span class="star-pagination">*633</span> THOMAS, J., announced the judgment of the Court and delivered an opinion, in which REHNQUIST, C. J., and SCALIA, J., joined. KENNEDY, J., filed an opinion concurring in the judgment, in which O'CONNOR, J., joined, <i>post,</i> p. 644. SOUTER, J., filed a dissenting opinion, in which STEVENS and GINSBURG, JJ., joined, <i>post,</i> p. 645. BREYER, J., filed a dissenting opinion, <i>post,</i> p. 647.</p>
<p><i>Deputy Solicitor General Dreeben</i> argued the cause for petitioner. With him on the briefs were <i>Solicitor General Olson, Acting Assistant Attorney General Wray, James A. Feldman,</i> and <i>Joseph C. Wyderko.</i></p>
<p><i>Jill M. Wichlens</i> argued the cause for respondent. With her on the brief were <i>Michael G. Katz</i> and <i>Virginia L. Grady.</i><sup>[*]</sup></p>
<p>JUSTICE THOMAS announced the judgment of the Court and delivered an opinion, in which THE CHIEF JUSTICE and JUSTICE SCALIA join.</p>
<p>In this case we must decide whether a failure to give a suspect the warnings prescribed by <i>Miranda</i> v. <i>Arizona,</i> <span class="star-pagination">*634</span> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), requires suppression of the physical fruits of the suspect's unwarned but voluntary statements. The Court has previously addressed this question but has not reached a definitive conclusion. See <i>Massachusetts</i> v. <i>White,</i> <span class="citation" data-id="9011990"><a href="/opinion/9018794/massachusetts-v-white/" aria-description="Citation for case: Massachusetts v. White">439 U. S. 280</a></span> (1978) <i>(per curiam)</i> (dividing evenly on the question); see also <i>Patterson</i> v. <i>United States,</i> <span class="citation" data-id="9431278"><a href="/opinion/112057/patterson-v-united-states/" aria-description="Citation for case: Patterson v. United States">485 U. S. 922</a></span> (1988) (White, J., dissenting from denial of certiorari). Although we believe that the Court's decisions in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), and <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974), are instructive, the Courts of Appeals have split on the question after our decision in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000). See, <i>e. g., </i><i>United States</i> v. <i>Villalba-Alvarado,</i> <span class="citation" data-id="9496439"><a href="/opinion/783781/united-states-v-angel-benito-villalba-alvarado-aka-benito-angel-alvara/" aria-description="Citation for case: United States v. Angel Benito Villalba-Alvarado, A/K/A...">345 F. 3d 1007</a></span> (CA8 2003) (holding admissible the physical fruits of a <i>Miranda</i> violation); <i>United States</i> v. <i>Sterling,</i> <span class="citation" data-id="776886"><a href="/opinion/776886/united-states-v-ricky-g-sterling/" aria-description="Citation for case: United States v. Ricky G. Sterling">283 F. 3d 216</a></span> (CA4 2002) (same); <i>United States</i> v. <i>DeSumma,</i> <span class="citation" data-id="775633"><a href="/opinion/775633/united-states-v-frank-desumma-aka-doc-frank-desumma/" aria-description="Citation for case: United States v. Frank Desumma, A/K/A Doc, Frank Desumma">272 F. 3d 176</a></span> (CA3 2001) (same); <i>United States</i> v. <i>Faulkingham,</i> <span class="citation" data-id="200020"><a href="/opinion/200020/united-states-v-faulkingham/" aria-description="Citation for case: United States v. Faulkingham">295 F. 3d 85</a></span> (CA1 2002) (holding admissible the physical fruits of a negligent <i>Miranda</i> violation). Because the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule protects against violations of the Self-Incrimination Clause, which, in turn, is not implicated by the introduction at trial of physical evidence resulting from voluntary statements, we answer the question presented in the negative.</p>
<p></p>
<h2>I</h2>
<p>In June 2001, respondent, Samuel Francis Patane, was arrested for harassing his ex-girlfriend, Linda O'Donnell. He was released on bond, subject to a temporary restraining order that prohibited him from contacting O'Donnell. Respondent apparently violated the restraining order by attempting to telephone O'Donnell. On June 6, 2001, Officer Tracy Fox of the Colorado Springs Police Department began to investigate the matter. On the same day, a county probation officer informed an agent of the Bureau of Alcohol, Tobacco, and Firearms (ATF), that respondent, a convicted felon, illegally possessed a .40 Glock pistol. The ATF relayed this information to Detective Josh Benner, who worked <span class="star-pagination">*635</span> closely with the ATF. Together, Detective Benner and Officer Fox proceeded to respondent's residence.</p>
<p>After reaching the residence and inquiring into respondent's attempts to contact O'Donnell, Officer Fox arrested respondent for violating the restraining order. Detective Benner attempted to advise respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights but got no further than the right to remain silent. At that point, respondent interrupted, asserting that he knew his rights, and neither officer attempted to complete the warning.<sup>[1]</sup> App. 40.</p>
<p>Detective Benner then asked respondent about the Glock. Respondent was initially reluctant to discuss the matter, stating: "I am not sure I should tell you anything about the Glock because I don't want you to take it away from me." <i>Id.,</i> at 41. Detective Benner persisted, and respondent told him that the pistol was in his bedroom. Respondent then gave Detective Benner permission to retrieve the pistol. Detective Benner found the pistol and seized it.</p>
<p>A grand jury indicted respondent for possession of a firearm by a convicted felon, in violation of <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). The District Court granted respondent's motion to suppress the firearm, reasoning that the officers lacked probable cause to arrest respondent for violating the restraining order. It therefore declined to rule on respondent's alternative argument that the gun should be suppressed as the fruit of an unwarned statement.</p>
<p>The Court of Appeals reversed the District Court's ruling with respect to probable cause but affirmed the suppression order on respondent's alternative theory. The court rejected the Government's argument that this Court's decisions in <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra,</a></span></i> and <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span></i> foreclosed application of the fruit of the poisonous tree doctrine of <i>Wong Sun</i> <span class="star-pagination">*636</span> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), to the present context. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1019" aria-description="Citation for case: United States v. Patane">304 F. 3d 1013, 1019</a></span> (CA10 2002). These holdings were, the Court of Appeals reasoned, based on the view that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> announced a prophylactic rule, a position that it found to be incompatible with this Court's decision in <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson, supra,</i> at 444</a></span> ("<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> announced a constitutional rule that Congress may not supersede legislatively").<sup>[2]</sup> The Court of Appeals thus equated <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i>'s announcement that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a constitutional rule with the proposition that a failure to warn pursuant to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is itself a violation of the Constitution (and, more particularly, of the suspect's Fifth Amendment rights). Based on its understanding of <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> the Court of Appeals rejected the post-<span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson</i></a></span> views of the Third and Fourth Circuits that the fruits doctrine does not apply to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1023" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1023-1027</a></span> (discussing <i>United States</i> v. <i>Sterling,</i> <span class="citation" data-id="776886"><a href="/opinion/776886/united-states-v-ricky-g-sterling/" aria-description="Citation for case: United States v. Ricky G. Sterling">283 F. 3d 216</a></span> (CA4 2002), and <i>United States</i> v. <i>DeSumma,</i> <span class="citation" data-id="775633"><a href="/opinion/775633/united-states-v-frank-desumma-aka-doc-frank-desumma/" aria-description="Citation for case: United States v. Frank Desumma, A/K/A Doc, Frank Desumma">272 F. 3d 176</a></span> (CA3 2001)). It also disagreed with the First Circuit's conclusion that suppression is not generally required in the case of negligent failures to warn, <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1027" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1027-1029</a></span> (discussing <i>United States</i> v. <i>Faulkingham,</i> <span class="citation" data-id="200020"><a href="/opinion/200020/united-states-v-faulkingham/" aria-description="Citation for case: United States v. Faulkingham">295 F. 3d 85</a></span> (CA1 2002)), explaining that "[d]eterrence is necessary not merely to deter intentional wrongdoing, but also to ensure that officers diligently (non-negligently) protect  and properly are trained to protect  the constitutional rights of citizens," <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./538/976/">538 U. S. 976</a></span> (2003).</p>
<p>As we explain below, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule is a prophylactic employed to protect against violations of the Self-Incrimination Clause. The Self-Incrimination Clause, however, is not implicated by the admission into evidence of the physical fruit of a voluntary statement. Accordingly, there is no justification for extending the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule to this context. <span class="star-pagination">*637</span> And just as the Self-Incrimination Clause primarily focuses on the criminal trial, so too does the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule is not a code of police conduct, and police do not violate the Constitution (or even the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule, for that matter) by mere failures to warn. For this reason, the exclusionary rule articulated in cases such as <i>Wong Sun</i> does not apply. Accordingly, we reverse the judgment of the Court of Appeals and remand the case for further proceedings.</p>
<p></p>
<h2>II</h2>
<p>The Self-Incrimination Clause provides: "No person . . . shall be compelled in any criminal case to be a witness against himself." U. S. Const., Amdt. 5. We need not decide here the precise boundaries of the Clause's protection. For present purposes, it suffices to note that the core protection afforded by the Self-Incrimination Clause is a prohibition on compelling a criminal defendant to testify against himself at trial. See, <i>e. g., </i><i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#764" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 764-768</a></span> (2003) (plurality opinion); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#777" aria-description="Citation for case: Chavez v. Martinez"><i>id.,</i> at 777-779</a></span> (SOUTER, J., concurring in judgment); 8 J. Wigmore, Evidence § 2263, p. 378 (J. McNaughton rev. ed. 1961) (explaining that the Clause "was directed at the employment of legal process to <i>extract from the person's own lips</i> an admission of guilt, which would thus take the place of other evidence"); see also <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#49" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 49-56</a></span> (2000) (THOMAS, J., concurring) (explaining that the privilege might extend to bar the compelled production of any incriminating evidence, testimonial or otherwise). The Clause cannot be violated by the introduction of nontestimonial evidence obtained as a result of voluntary statements. See, <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell"><i>e. g., id.,</i> at 34</a></span> (noting that the word "`witness'" in the Self-Incrimination Clause "limits the relevant category of compelled incriminating communications to those that are `testimonial' in character"); <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#35" aria-description="Citation for case: United States v. Hubbell"><i>id.,</i> at 35</a></span> (discussing why compelled blood samples do not violate the Clause; cataloging other examples and citing cases); <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#304" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 304</a></span> ("The Fifth Amendment, of <span class="star-pagination">*638</span> course, is not concerned with nontestimonial evidence"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 306-307</a></span> ("The Fifth Amendment prohibits use by the prosecution in its case in chief only of <i>compelled</i> testimony"); <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#705" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 705</a></span> (1993) (O'CONNOR, J., concurring in part and dissenting in part) (describing "<i>true</i> Fifth Amendment claims [as] the extraction and use of <i>compelled</i> testimony"); <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#665" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 665-672</a></span>, and n. 4 (1984) (O'CONNOR, J., concurring in judgment in part and dissenting in part) (explaining that the physical fruit of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation need not be suppressed for these reasons).</p>
<p>To be sure, the Court has recognized and applied several prophylactic rules designed to protect the core privilege against self-incrimination. See, <i>e. g., </i><span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#770" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 770-772</a></span> (plurality opinion). For example, although the text of the Self-Incrimination Clause at least suggests that "its coverage [is limited to] compelled testimony that is used against the defendant in the trial itself," <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell"><i>Hubbell, supra,</i> at 37</a></span>, potential suspects may, at times, assert the privilege in proceedings in which answers might be used to incriminate them in a subsequent criminal case. See, <i>e. g., </i><i>United States</i> v. <i>Balsys,</i> <span class="citation" data-id="9433709"><a href="/opinion/118242/united-states-v-balsys/#671" aria-description="Citation for case: United States v. Balsys">524 U. S. 666, 671-672</a></span> (1998); <i>Minnesota</i> v. <i>Murphy,</i> <span class="citation" data-id="9429504"><a href="/opinion/111105/minnesota-v-murphy/#426" aria-description="Citation for case: Minnesota v. Murphy">465 U. S. 420, 426</a></span> (1984); cf. <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441</a></span> (1972) (holding that the Government may compel grand jury testimony from witnesses over Fifth Amendment objections if the witnesses receive "use and derivative use immunity"); <i>Uniformed Sanitation Men Assn., Inc.</i> v. <i>Commissioner of Sanitation of City of New York,</i> <span class="citation" data-id="9423788"><a href="/opinion/107739/uniformed-sanitation-men-assn-v-commissioner-of-sanitation-of-new-york/#284" aria-description="Citation for case: Uniformed Sanitation Men Ass&#x27;n v. Commissioner of...">392 U. S. 280, 284</a></span> (1968) (allowing the Government to use economic compulsion to secure statements but only if the Government grants appropriate immunity). We have explained that "[t]he natural concern which underlies [these] decisions is that an inability to protect the right at one stage of a proceeding may make its invocation useless at a later stage." <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#440" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 440-441</a></span>.</p>
<p><span class="star-pagination">*639</span> Similarly, in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court concluded that the possibility of coercion inherent in custodial interrogations unacceptably raises the risk that a suspect's privilege against self-incrimination might be violated. See <i>Dickerson,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#434" aria-description="Citation for case: Dickerson v. United States">530 U. S., at 434-435</a></span>; <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. To protect against this danger, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule creates a presumption of coercion, in the absence of specific warnings, that is generally irrebuttable for purposes of the prosecution's case in chief.</p>
<p>But because these prophylactic rules (including the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule) necessarily sweep beyond the actual protections of the Self-Incrimination Clause, see, <i>e. g., </i><span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#690" aria-description="Citation for case: Withrow v. Williams"><i>Withrow, supra,</i> at 690-691</a></span>; <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span>, any further extension of these rules must be justified by its necessity for the protection of the actual right against compelled self-incrimination, <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#778" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 778</a></span> (SOUTER, J., concurring in judgment) (requiring a "`powerful showing'" before "expand[ing] . . . the privilege against compelled self-incrimination"). Indeed, at times the Court has declined to extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> even where it has perceived a need to protect the privilege against self-incrimination. See, <i>e. g., </i><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#657" aria-description="Citation for case: New York v. Quarles"><i>Quarles, supra,</i> at 657</a></span> (concluding "that the need for answers to questions in a situation posing a threat to the public safety outweighs the need for the prophylactic rule protecting the Fifth Amendment's privilege against self-incrimination").</p>
<p>It is for these reasons that statements taken without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings (though not actually compelled) can be used to impeach a defendant's testimony at trial, see <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 307-308</a></span>; <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), though the fruits of actually compelled testimony cannot, see <i>New Jersey</i> v. <i>Portash,</i> <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#458" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 458-459</a></span> (1979). More generally, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule "does not require that the statements [taken without complying with the rule] and their fruits be discarded as inherently tainted," <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 307</a></span>. Such a blanket suppression rule could not be justified <span class="star-pagination">*640</span> by reference to the "Fifth Amendment goal of assuring trustworthy evidence" or by any deterrence rationale, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 308</a></span>; see <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 446-449</a></span>; <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York"><i>Harris, supra,</i> at 225-226</a></span>, and n. 2, and would therefore fail our close-fit requirement.</p>
<p>Furthermore, the Self-Incrimination Clause contains its own exclusionary rule. It provides that "[n]o person . . . shall be compelled in any criminal case to be a witness against himself." Amdt. 5. Unlike the Fourth Amendment's bar on unreasonable searches, the Self-Incrimination Clause is self-executing. We have repeatedly explained "that those subjected to coercive police interrogations have an <i>automatic</i> protection from the use of their involuntary statements (or evidence derived from their statements) in any subsequent criminal trial." <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#769" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 769</a></span> (plurality opinion) (citing, for example, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#307" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 307-308</a></span>). This explicit textual protection supports a strong presumption against expanding the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule any further. Cf. <i>Graham</i> v. <i>Connor,</i> <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989).</p>
<p>Finally, nothing in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> including its characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as announcing a constitutional rule, 530 U. S., at 444, changes any of these observations. Indeed, in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> the Court specifically noted that the Court's "subsequent cases have reduced the impact of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule on legitimate law enforcement while reaffirming <i>[Miranda]</i>'s core ruling that unwarned statements may not be used as evidence in the prosecution's case in chief." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#443" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 443-444</a></span>. This description of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> especially the emphasis on the use of "unwarned statements . . . in the prosecution's case in chief," makes clear our continued focus on the protections of the Self-Incrimination Clause. The Court's reliance on our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> precedents, including both <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> and <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span>,</i> see, <i>e. g., </i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#438" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson, supra,</i> at 438, 441</a></span>, further demonstrates the continuing validity of those decisions. In short, nothing in <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i> calls into question our continued <span class="star-pagination">*641</span> insistence that the closest possible fit be maintained between the Self-Incrimination Clause and any rule designed to protect it.</p>
<p></p>
<h2>III</h2>
<p>Our cases also make clear the related point that a mere failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not, by itself, violate a suspect's constitutional rights or even the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule. So much was evident in many of our pre-<span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States"><i>Dickerson</i></a></span> cases, and we have adhered to this view since <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>.</i> See <i>Chavez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#772" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 772-773</a></span> (plurality opinion) (holding that a failure to read <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings did not violate the respondent's constitutional rights); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#789" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 789</a></span> (KENNEDY, J., concurring in part and dissenting in part) (agreeing "that failure to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning does not, without more, establish a completed violation when the unwarned interrogation ensues"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#308" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 308</a></span>; <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S., at 654</a></span>; cf. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#777" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 777-779</a></span> (SOUTER, J., concurring in judgment). This, of course, follows from the nature of the right protected by the Self-Incrimination Clause, which the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule, in turn, protects. It is "`a fundamental <i>trial</i> right.'" <i>Withrow,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/" aria-description="Citation for case: Withrow v. Williams">507 U. S., at 691</a></span> (quoting <i>United States</i> v. <i>Verdugo-Urquidez,</i> <span class="citation" data-id="9431925"><a href="/opinion/112382/united-states-v-verdugo-urquidez/#264" aria-description="Citation for case: United States v. Verdugo-Urquidez">494 U. S. 259, 264</a></span> (1990)). See also <i>Chavez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#766" aria-description="Citation for case: Chavez v. Martinez">538 U. S., at 766-768</a></span> (plurality opinion); <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>id.,</i> at 790</a></span> (KENNEDY, J., concurring in part and dissenting in part) ("The identification of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation and its consequences, then, ought to be determined at trial").</p>
<p>It follows that police do not violate a suspect's constitutional rights (or the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule) by negligent or even deliberate failures to provide the suspect with the full panoply of warnings prescribed by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Potential violations occur, if at all, only upon the admission of unwarned statements into evidence at trial. And, at that point, "[t]he exclusion of unwarned statements ... is a complete and sufficient <span class="star-pagination">*642</span> remedy" for any perceived <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 790</a></span>.<sup>[3]</sup></p>
<p>Thus, unlike unreasonable searches under the Fourth Amendment or actual violations of the Due Process Clause or the Self-Incrimination Clause, there is, with respect to mere failures to warn, nothing to deter. There is therefore no reason to apply the "fruit of the poisonous tree" doctrine of <i>Wong Sun,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488</a></span>.<sup>[4]</sup> See also <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#441" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 441</a></span> (1984) (discussing the exclusionary rule in the Sixth Amendment context and noting that it applies to "<i>illegally</i> obtained evidence [and] other incriminating evidence derived from [it]" (emphasis added)). It is not for this Court to impose its preferred police practices on either federal law enforcement officials or their state counterparts.</p>
<p></p>
<h2>IV</h2>
<p>In the present case, the Court of Appeals, relying on <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> wholly adopted the position that the taking of unwarned statements violates a suspect's constitutional rights. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>.<sup>[5]</sup> And, of course, if this were so, a <span class="star-pagination">*643</span> strong deterrence-based argument could be made for suppression of the fruits. See, <i>e. g., </i><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#441" aria-description="Citation for case: Nix v. Williams"><i>Nix, supra,</i> at 441-444</a></span>; <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States"><i>Wong Sun, supra,</i> at 484-486</a></span>; cf. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).</p>
<p>But <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i>'s characterization of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as a constitutional rule does not lessen the need to maintain the closest possible fit between the Self-Incrimination Clause and any judge-made rule designed to protect it. And there is no such fit here. Introduction of the nontestimonial fruit of a voluntary statement, such as respondent's Glock, does not implicate the Self-Incrimination Clause. The admission of such fruit presents no risk that a defendant's coerced statements (however defined) will be used against him at a criminal trial. In any case, "[t]he exclusion of unwarned statements . . . is a complete and sufficient remedy" for any perceived <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez"><i>Chavez, supra,</i> at 790</a></span> (KENNEDY, J., concurring in part and dissenting in part). See also H. Friendly, Benchmarks 280-281 (1967). There is simply no need to extend (and therefore no justification for extending) the prophylactic rule of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to this context.</p>
<p>Similarly, because police cannot violate the Self-Incrimination Clause by taking unwarned though voluntary statements, an exclusionary rule cannot be justified by reference to a deterrence effect on law enforcement, as the Court of Appeals believed, <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1028" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1028-1029</a></span>. Our decision not to apply <i>Wong Sun</i> to mere failures to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings was sound at the time <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span></i> and <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span></i> were decided, and we decline to apply <i>Wong Sun</i> to such failures now.</p>
<p>The Court of Appeals ascribed significance to the fact that, in this case, there might be "little [practical] difference between [respondent's] confessional statement" and the actual physical evidence. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1027" aria-description="Citation for case: United States v. Patane">304 F. 3d, at 1027</a></span>. The distinction, the court said, "appears to make little sense as a matter of policy." <i><span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/" aria-description="Citation for case: United States v. Patane">Ibid.</a></span></i> But, putting policy aside, we have held that "[t]he word `witness' in the constitutional text limits the" <span class="star-pagination">*644</span> scope of the Self-Incrimination Clause to testimonial evidence. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#34" aria-description="Citation for case: United States v. Hubbell">530 U. S., at 34-35</a></span>. The Constitution itself makes the distinction.<sup>[6]</sup> And although it is true that the Court requires the exclusion of the physical fruit of actually coerced statements, it must be remembered that statements taken without sufficient <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are presumed to have been coerced only for certain purposes and then only when necessary to protect the privilege against self-incrimination. See Part II, <i>supra.</i> For the reasons discussed above, we decline to extend that presumption further.<sup>[7]</sup></p>
<p>Accordingly, we reverse the judgment of the Court of Appeals and remand the case for further proceedings.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE KENNEDY, with whom JUSTICE O'CONNOR joins, concurring in the judgment.</p>
<p>In <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), and <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), evidence obtained following an unwarned interrogation was held admissible. This result was based in large part on our recognition that the concerns underlying the <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), rule must be accommodated to other objectives of the criminal justice system. <span class="star-pagination">*645</span> I agree with the plurality that <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000), did not undermine these precedents and, in fact, cited them in support. Here, it is sufficient to note that the Government presents an even stronger case for admitting the evidence obtained as the result of Patane's unwarned statement. Admission of nontestimonial physical fruits (the Glock in this case), even more so than the postwarning statements to the police in <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad</a></span></i> and <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974), does not run the risk of admitting into trial an accused's coerced incriminating statements against himself. In light of the important probative value of reliable physical evidence, it is doubtful that exclusion can be justified by a deterrence rationale sensitive to both law enforcement interests and a suspect's rights during an in-custody interrogation. Unlike the plurality, however, I find it unnecessary to decide whether the detective's failure to give Patane the full <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings should be characterized as a violation of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule itself, or whether there is "[any]thing to deter" so long as the unwarned statements are not later introduced at trial. <i>Ante,</i> at 641-642.</p>
<p>With these observations, I concur in the judgment of the Court.</p>
<p>JUSTICE SOUTER, with whom JUSTICE STEVENS and JUSTICE GINSBURG join, dissenting.</p>
<p>The plurality repeatedly says that the Fifth Amendment does not address the admissibility of nontestimonial evidence, an overstatement that is beside the point. The issue actually presented today is whether courts should apply the fruit of the poisonous tree doctrine lest we create an incentive for the police to omit <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, see <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before custodial interrogation.<sup>[1]</sup><span class="star-pagination">*646</span> In closing their eyes to the consequences of giving an evidentiary advantage to those who ignore <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the plurality adds an important inducement for interrogators to ignore the rule in that case.</p>
<p><i>Miranda</i> rested on insight into the inherently coercive character of custodial interrogation and the inherently difficult exercise of assessing the voluntariness of any confession resulting from it. Unless the police give the prescribed warnings meant to counter the coercive atmosphere, a custodial confession is inadmissible, there being no need for the previous time-consuming and difficult enquiry into voluntariness. That inducement to forestall involuntary statements and troublesome issues of fact can only atrophy if we turn around and recognize an evidentiary benefit when an unwarned statement leads investigators to tangible evidence. There is, of course, a price for excluding evidence, but the Fifth Amendment is worth a price, and in the absence of a very good reason, the logic of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> should be followed: a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation raises a presumption of coercion, <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 306-307</a></span>, and n. 1 (1985), and the Fifth Amendment privilege against compelled self-incrimination extends to the exclusion of derivative evidence, see <i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#37" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 37-38</a></span> (2000) (recognizing "the Fifth Amendment's protection against the prosecutor's use of incriminating information derived directly or indirectly from ... [actually] compelled testimony"); <i>Kastigar</i> v. <i>United States,</i> <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 453</a></span> (1972). That should be the end of this case.</p>
<p>The fact that the books contain some exceptions to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> exclusionary rule carries no weight here. In <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), it was respect for the integrity of the judicial process that justified the admission <span class="star-pagination">*647</span> of unwarned statements as impeachment evidence. But Patane's suppression motion can hardly be described as seeking to "perver[t]" <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> "into a license to use perjury" or otherwise handicap the "traditional truth-testing devices of the adversary process." <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#225" aria-description="Citation for case: Harris v. New York">401 U. S., at 225-226</a></span>. Nor is there any suggestion that the officers' failure to warn Patane was justified or mitigated by a public emergency or other exigent circumstance, as in <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984). And of course the premise of <i>Oregon</i> v. <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra</a></span></i><i>,</i> is not on point; although a failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before one individual statement does not necessarily bar the admission of a subsequent statement given after adequate warnings, <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span>; cf. <i>Missouri</i> v. <i>Seibert, ante,</i> at 614-615 (plurality opinion), that rule obviously does not apply to physical evidence seized once and for all.<sup>[2]</sup></p>
<p>There is no way to read this case except as an unjustifiable invitation to law enforcement officers to flout <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> when there may be physical evidence to be gained. The incentive is an odd one, coming from the Court on the same day it decides <i>Missouri</i> v. <i>Seibert, ante,</i> p. 600. I respectfully dissent.</p>
<p>JUSTICE BREYER, dissenting.</p>
<p>For reasons similar to those set forth in JUSTICE SOUTER's dissent and in my concurring opinion in <i>Missouri</i> v. <i>Seibert, ante,</i> at 617, I would extend to this context the "fruit of the poisonous tree" approach, which I believe the Court has come close to adopting in <i>Seibert.</i> Under that approach, <span class="star-pagination">*648</span> courts would exclude physical evidence derived from unwarned questioning unless the failure to provide <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), warnings was in good faith. See <i>Seibert, ante,</i> at 617-618 (BREYER, J., concurring); cf. <i>ante,</i> at 645-646, n. 1 (SOUTER, J., dissenting). Because the courts below made no explicit finding as to good or bad faith, I would remand for such a determination.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the State of Alabama et al. by <i>William H. Pryor, Jr.,</i> Attorney General of Alabama, <i>Nathan A. Forrester,</i> Solicitor General, <i>Michael B. Billingsley,</i> Deputy Solicitor General, <i>Marc A. Starrett,</i> Assistant Attorney General, and by the Attorneys General for their respective States as follows: <i>M. Jane Brady</i> of Delaware, <i>Charles J. Crist, Jr.,</i> of Florida, <i>Mark J. Bennett</i> of Hawaii, <i>Lisa Madigan</i> of Illinois, <i>Steve Carter</i> of Indiana, <i>Mike McGrath</i> of Montana, <i>Jim Petro</i> of Ohio, <i>D. Michael Fisher</i> of Pennsylvania, <i>Lawrence E. Long</i> of South Dakota, <i>Paul G. Summers</i> of Tennessee, <i>Greg Abbott</i> of Texas, <i>Mark L. Shurtleff</i> of Utah, <i>William H. Sorrell</i> of Vermont, <i>Jerry W. Kilgore</i> of Virginia, <i>Peggy A. Lautenschlager</i> of Wisconsin, and <i>Patrick J. Crank</i> of Wyoming; and for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger.</i>
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed for the Brennan Center for Justice by <i>Stephen J. Schulhofer, Frederick A. O. Schwarz, Jr., Tom Gerety,</i> and <i>E. Joshua Rosenkranz;</i> and for the National Association of Criminal Defense Lawyers et al. by <i>James J. Tomkovicz, David M. Porter,</i> and <i>Steven R. Shapiro.</i></p>
<p>[1]  The Government concedes that respondent's answers to subsequent on-the-scene questioning are inadmissible at trial under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), despite the partial warning and respondent's assertions that he knew his rights.</p>
<p>[2]  The Court of Appeals also distinguished <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), on the ground that the second (and warned) confession at issue there was the product of the defendant's volition. <span class="citation" data-id="162589"><a href="/opinion/162589/united-states-v-patane/#1019" aria-description="Citation for case: United States v. Patane">304 F.3d, at 1019, 1021</a></span>. For the reasons discussed below, we do not find this distinction relevant.</p>
<p>[3]  We acknowledge that there is language in some of the Court's post-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> decisions that might suggest that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule operates as a direct constraint on police. See, <i>e. g., </i><i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 322</a></span> (1994) <i>(per curiam)</i><i>; </i><i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#420" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 420</a></span> (1986) (stating that "<i>Miranda</i> imposed on the police an obligation to follow certain procedures"); cf. <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 485</a></span> (1981). But <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself made clear that its focus was the admissibility of statements, see, <i>e. g.,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#439" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 439, 467</a></span>, a view the Court reaffirmed in <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 443-444</a></span> (2000) (equating the <i>Miranda</i> rule with the proposition that "unwarned statements may not be used <i>as evidence</i> in the prosecution's case in chief" (emphasis added)).</p>
<p>[4]  We reject respondent's invitation to apply the balancing test of <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939). Brief for Respondent 15-33. At issue in <i><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">Nardone</a></span></i> was the violation of a federal wiretap statute, and the Court employed an exclusionary rule to deter those violations. But, once again, there are no violations (statutory or constitutional) to deter here.</p>
<p>[5]  It is worth mentioning that the Court of Appeals did not have the benefit of our decision in <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760</a></span> (2003).</p>
<p>[6]  While Fourth Amendment protections extend to "persons, houses, papers, and effects," the Self-Incrimination Clause prohibits only compelling a defendant to be "a witness against himself," Amdt. 5.</p>
<p>[7]  It is not clear whether the Government could have used legal processes actually to compel respondent to produce the Glock, though there is a reasonable argument that it could have. See, <i>e. g., </i><i>United States</i> v. <i>Hubbell,</i> <span class="citation" data-id="9526953"><a href="/opinion/1087666/united-states-v-hubbell/#42" aria-description="Citation for case: United States v. Hubbell">530 U. S. 27, 42-45</a></span> (2000); <i>Baltimore City Dept. of Social Servs.</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#554" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 554-556</a></span> (1990); <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span> (1976); <i>Warden, Md. Penitentiary</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#302" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 302-303</a></span> (1967); <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U.S. 757, 761</a></span> (1966). But see <i>Commonwealth</i> v. <i>Hughes,</i> <span class="citation" data-id="2021779"><a href="/opinion/2021779/commonwealth-v-hughes/" aria-description="Citation for case: Commonwealth v. Hughes">380 Mass. 583</a></span>, <span class="citation" data-id="2021779"><a href="/opinion/2021779/commonwealth-v-hughes/" aria-description="Citation for case: Commonwealth v. Hughes">404 N. E. 2d 1239</a></span> (1980); <i>Goldsmith</i> v. <i>Superior Court,</i> <span class="citation" data-id="2125014"><a href="/opinion/2125014/goldsmith-v-superior-court/" aria-description="Citation for case: Goldsmith v. Superior Court">152 Cal. App. 3d 76</a></span>, <span class="citation" data-id="2125014"><a href="/opinion/2125014/goldsmith-v-superior-court/" aria-description="Citation for case: Goldsmith v. Superior Court">199 Cal. Rptr. 366</a></span> (1984). In light of this, it would be especially odd to exclude the Glock here.</p>
<p>[1]  In so saying, we are taking the legal issue as it comes to us, even though the facts give off the scent of a made-up case. If there was a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> failure, the most immediate reason was that Patane told the police to stop giving the warnings because he already knew his rights. There could easily be an analogy in this case to the bumbling mistake the police committed in <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). See <i>Missouri</i> v. <i>Seibert, ante,</i> at 614-615 (plurality opinion).</p>
<p>[2]  To the extent that <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974) (admitting the testimony of a witness who was discovered because of an unwarned custodial interrogation), created another exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> it is off the point here. In <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker</a></span>,</i> we explicitly declined to lay down a broad rule about the fruits of unwarned statements. Instead, we "place[d] our holding on a narrower ground," relying principally on the fact that the interrogation occurred before <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was decided and was conducted in good faith according to constitutional standards governing at that time. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 447</a></span>-448 (citing <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964)).</p>

</div>
```

---
