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

## GROUP: _overhaul2/lake/cases/Rehberg v. Paulk.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Rehberg v. Paulk
type: case
citation: "566 U.S. 356 (2012)"
parallel_cite: "132 S. Ct. 1497; 182 L. Ed. 2d 593"
neutral_cite: 2012 U.S. LEXIS 2711
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-04-02
docket: No. 10-788
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
  opinion_url: "https://www.courtlistener.com/opinion/626447/rehberg-v-paulk/"
  cluster_id: 626447
  opinion_id: 626447
  identity_checked: true
lake:
  record_id: Rehberg v. Paulk
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Absolute Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Briscoe v. LaHue]]"
  - "[[Imbler v. Pachtman]]"
tags:
  - case
  - section-1983
  - witness-immunity
  - absolute-immunity
  - grand-jury
  - complaining-witness
holding: "A grand jury witness — including a law-enforcement officer who serves as a complaining or investigating witness — has absolute immunity from any § 1983 claim based on his grand jury testimony, and that immunity may not be circumvented by alleging a conspiracy to present false testimony or by using the testimony to support another § 1983 theory."
aliases:
  - Rehberg v. Paulk
  - "Rehberg v. Paulk (2012)"
---

# Rehberg v. Paulk

*566 U.S. 356 (2012)* (No. 10-788) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 626447 → opinion 626447 (Alito, J.; 566 U.S. 356, decided Apr. 2, 2012). Rule quote string-matched to the CL opinion text 2026-07-07 (U.S. Reports star `*369` opens the holding paragraph; `*370` follows within it). S9 promotes. -->

## Background
Charles Rehberg, an accountant, sent anonymous faxes criticizing the management and activities of a Georgia hospital. In response, the local district attorney's chief investigator, James Paulk, allegedly presented false testimony to a grand jury, which returned indictments against Rehberg; the charges were dismissed and re-obtained more than once and ultimately came to nothing. Rehberg sued Paulk under § 1983, alleging that Paulk fabricated the grand jury testimony. Paulk asserted absolute witness immunity, and the Eleventh Circuit agreed.

## Issue
Whether a grand jury witness — including an officer who acts as the complaining or investigating witness — is absolutely immune from a § 1983 claim based on his grand jury testimony.

## Rule
Extending the trial-witness immunity of *[[Briscoe v. LaHue]]* to grand jury proceedings, the Court held: "This means that a grand jury witness has absolute immunity from any § 1983 claim based on the witness' testimony." — 566 U.S. at 369. ^pin-369

## Application
A grand jury witness performs the same function, and would face the same flood of retaliatory suits, as a witness at trial, who is absolutely immune under *[[Briscoe v. LaHue|Briscoe]]*; the same immunity therefore attaches to grand jury testimony. The Court further held that the immunity cannot be evaded by recasting the claim as a conspiracy to present false testimony, or by using the fact of the testimony to prop up some other § 1983 theory about initiating the prosecution — otherwise a plaintiff could defeat the immunity simply by reframing the pleadings to attack the witness's "preparation" instead of the protected testimony itself.

## Conclusion
The judgment was **affirmed**. Alito, J., delivered the opinion of a unanimous Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Rehberg* extends *[[Briscoe v. LaHue]]*'s trial-witness immunity to the grand jury and forecloses pleading around it. Teach the boundary the Court preserved (drawing on the *[[Malley v. Briggs|Malley]]*/*Kalina* "complaining witness" line): the immunity protects a witness's *testimony*, not the distinct, non-testimonial act of a "complaining witness" who, for example, swears out a defective arrest-warrant affidavit — conduct that draws only [[Qualified Immunity|qualified immunity]]. Pair it with *[[Imbler v. Pachtman|Imbler]]* and *[[Buckley v. Fitzsimmons|Buckley]]* on the advocacy/investigation line.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Rehberg v. Paulk*, 566 U.S. 356 (2012)](https://www.courtlistener.com/opinion/626447/rehberg-v-paulk/) — pinpoint: 369 (Alito, J., for the Court; the CL opinion text carries the reporter star `*369` at the start of the holding paragraph, with `*370` appearing later in the same paragraph). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "165291b395a62819", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Rehberg v. Paulk"}, "payload": {"all": [{"cite": "132 S. Ct. 1497", "page": "1497", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "182 L. Ed. 2d 593", "page": "593", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "182"}, {"cite": "566 U.S. 356", "page": "356", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "566"}, {"cite": "2012 U.S. LEXIS 2711", "page": "2711", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}], "display": "566 U.S. 356", "official": {"cite": "566 U.S. 356", "page": "356", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "566"}, "official_selection_present": true, "record_id": "Rehberg v. Paulk"}}
{"assertion_id": "05e536daa151a345", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Rehberg v. Paulk"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Rehberg v. Paulk", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Rehberg v. Paulk

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rehberg v. Paulk",
  "status": "under_review",
  "identity": {
    "case_name": "Rehberg v. Paulk",
    "case_name_short": "Rehberg",
    "case_name_full": "Rehberg v. Paulk",
    "input_case_name": "Rehberg v. Paulk",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-04-02",
    "year": 2012,
    "docket": "No. 10-788",
    "cluster_id": 626447,
    "lead_opinion_id": 626447,
    "sibling_ids": [],
    "absolute_url": "/opinion/626447/rehberg-v-paulk/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "566 U.S. 356",
      "volume": "566",
      "reporter": "U.S.",
      "page": "356",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1497",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 593",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 2711",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2711",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1497",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1497",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 593",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "566 U.S. 356",
        "volume": "566",
        "reporter": "U.S.",
        "page": "356",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 2711",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "2711",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "566 U.S. 356",
    "official_selection": {
      "court_class": "scotus",
      "selected": "566 U.S. 356",
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
    "date_created": "2026-07-06T13:47:34Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:47:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "rehberg-v-paulk--626447",
      "to_record_id": "Rehberg v. Paulk",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Rehberg v. Paulk

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                           REHBERG v. PAULK

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                THE ELEVENTH CIRCUIT

     No. 10–788.      Argued November 1, 2011—Decided April 2, 2012
Respondent, the chief investigator for a district attorney’s office, testi-
  fied at grand jury proceedings that resulted in petitioner’s indict-
  ment. After the indictments were dismissed, petitioner brought an
  action under 42 U. S. C. §1983, alleging that respondent had con-
  spired to present and did present false testimony to the grand jury.
  The Federal District Court denied respondent’s motion to dismiss on
  immunity grounds, but the Eleventh Circuit reversed, holding that
  respondent had absolute immunity from a §1983 claim based on his
  grand jury testimony.
Held: A witness in a grand jury proceeding is entitled to the same abso-
 lute immunity from suit under §1983 as a witness who testifies at
 trial. Pp. 3–18.
    (a) Section 1983, which derives from §1 of the Civil Rights Act of
 1871, was not meant to effect a radical departure from ordinary tort
 law and the common-law immunities applicable in tort suits. See,
 e.g., Burns v. Reed, 500 U. S. 478, 484. This interpretation of §1983
 has been reaffirmed by the Court time and again. Thus, the Court
 looks to the common law for guidance in determining the scope of the
 immunities available in actions brought under §1983. See Kalina v.
 Fletcher, 522 U. S. 118, 123. Taking a “functional approach,” see,
 e.g., Forrester v. White, 484 U. S. 219, 224, the Court identifies those
 governmental functions that were historically viewed as so important
 and vulnerable to interference by means of litigation that some form
 of absolute immunity from civil liability was needed to ensure that
 they are “ ‘performed with independence and without fear of conse-
 quences,’ ” Pierson v. Ray, 386 U. S. 547, 554.
    The Court’s functional approach is tied to the common law’s identi-
 fication of functions meriting the protection of absolute immunity,
2                           REHBERG v. PAULK

                                   Syllabus

    but the Court’s precedents have not mechanically duplicated the pre-
    cise scope of the absolute immunity the common law provided to pro-
    tect those functions. For example, it was common in 1871 for cases to
    be prosecuted by private parties, who did not enjoy absolute immuni-
    ty from suit. But as the prosecutorial function was increasingly as-
    sumed by public officials, common-law courts held that public prose-
    cutors, unlike their private predecessors, were absolutely immune
    from the types of tort claims that an aggrieved or vengeful criminal
    defendant was most likely to assert. This adaptation of prosecutorial
    immunity accommodated the special needs of public, as opposed to
    private, prosecutors. Thus, when the issue of prosecutorial immunity
    under §1983 reached this Court in Imbler v. Pachtman, 424 U. S.
    409, the Court did not simply apply the scope of immunity recognized
    by common-law courts as of 1871 but instead relied substantially on
    post-1871 cases extending broad immunity to public prosecutors sued
    for common-law torts. Neither has the Court suggested that §1983 is
    simply a federalized amalgamation of pre-existing common-law
    claims. The new federal claim created by §1983 differs in important
    ways from pre-existing common-law torts. Accordingly, both the
    scope of the new tort and the scope of the absolute immunity availa-
    ble in §1983 actions differ in some respects from the common law.
    Pp. 3―9.
       (b) A trial witness sued under §1983 enjoys absolute immunity
    from any claim based on his testimony. Briscoe v. LaHue, 460 U. S.
    352. Without absolute immunity, the truth-seeking process would be
    impaired as witnesses might be reluctant to testify, and even a wit-
    ness who took the stand “might be inclined to shade his testimony in
    favor of the potential plaintiff ” for “fear of subsequent liability.” Id.,
    at 333. These factors apply with equal force to grand jury witnesses.
    In both contexts, a witness’ fear of retaliatory litigation may deprive
    the tribunal of critical evidence. And in neither context is the deter-
    rent of potential civil liability needed to prevent false testimony be-
    cause other sanctions, chiefly prosecution for perjury, provide a suffi-
    cient deterrent.
       For the reasons identified in Briscoe, supra, at 342–344, there is no
    reason to distinguish law enforcement witnesses from lay witnesses
    in §1983 actions. And the rule that a grand jury witness has absolute
    immunity from any §1983 claim based on the witness’ testimony may
    not be circumvented by claiming that a grand jury witness conspired
    to present false testimony, or by using evidence of the witness’ testi-
    mony to support any other §1983 claim concerning the initiation or
    maintenance of a prosecution. Were it otherwise, a criminal defend-
    ant turned civil plaintiff could reframe a claim to attack the prepara-
    tory activity—such as a preliminary discussion in which the witness
                     Cite as: 566 U. S. ____ (2012)                      3

                                Syllabus

  relates the substance of his intended testimony—rather than the ab-
  solutely immune actions themselves. Pp. 9−12.
     (c) Petitioner’s main argument is that under Malley v. Briggs, 475
  U. S. 335, 340−341, and Kalina v. Fletcher, 522 U. S. 118, 131, grand
  jury witnesses who are “complaining witnesses” are not entitled to
  absolute immunity. But at the time §1983’s predecessor was enacted,
  a “complaining witness” was a party who procured an arrest and ini-
  tiated a criminal prosecution. A “complaining witness” might testify,
  either before a grand jury or at trial, but testifying was not a neces-
  sary characteristic of a “complaining witness.” Thus, testifying,
  whether before a grand jury or at trial, was not the distinctive func-
  tion performed by a “complaining witness.” A “complaining witness”
  cannot be held liable for perjurious trial testimony, see Briscoe, 460
  U. S., at 326, and there is no more reason why a “complaining wit-
  ness” should be subject to liability for testimony before a grand jury.
     Once the distinctive function performed by a “complaining witness”
  is understood, it is apparent that a law enforcement officer who testi-
  fies before a grand jury is not comparable to a “complaining witness”
  because it is not the officer who makes the critical decision to press
  criminal charges, but the prosecutor. It would be anomalous to per-
  mit a police officer testifying before a grand jury to be sued for mali-
  ciously procuring an unjust prosecution when it is the prosecutor,
  who is shielded by absolute immunity, who is actually responsible for
  the decision to initiate a prosecution. Petitioner also contends that
  the deterrent effect of civil liability is more needed in grand jury pro-
  ceedings because trial witnesses face cross-examination. But the
  force of that argument is more than offset by the problem that allow-
  ing such civil actions would create—subversion of grand jury secrecy,
  which is essential to the proper functioning of the grand jury system.
  See United States v. Sells Engineering, Inc., 463 U. S. 418, 424. And
  finally, contrary to petitioner’s suggestion, recognizing absolute im-
  munity for grand jury witnesses does not create an insupportable dis-
  tinction between States that use grand juries and States that permit
  felony prosecutions to be brought by complaint or information. Most
  States that do not require an indictment for felonies provide a prelim-
  inary hearing at which witnesses testify, and the lower courts have
  held that preliminary hearing witnesses are protected by the same
  immunity accorded grand jury witnesses. Pp. 12−18.
611 F. 3d 828, affirmed.

  ALITO, J., delivered the opinion for a unanimous Court.
                        Cite as: 566 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–788
                                   _________________


   CHARLES A. REHBERG, PETITIONER v. JAMES
                  P. PAULK
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

          APPEALS FOR THE ELEVENTH CIRCUIT

                                 [April 2, 2012]


  JUSTICE ALITO delivered the opinion of the Court.
  This case requires us to decide whether a “complaining
witness” in a grand jury proceeding is entitled to the
same immunity in an action under 42 U. S. C. §1983 as a
witness who testifies at trial. We see no sound reason
to draw a distinction for this purpose between grand jury
and trial witnesses.
                              I
   Petitioner Charles Rehberg, a certified public account-
ant, sent anonymous faxes to several recipients, including
the management of a hospital in Albany, Georgia, criticiz-
ing the hospital’s management and activities. In response,
the local district attorney’s office, with the assistance of
its chief investigator, respondent James Paulk, launched a
criminal investigation of petitioner, allegedly as a favor to
the hospital’s leadership.
   Respondent testified before a grand jury, and petitioner
was then indicted for aggravated assault, burglary, and
six counts of making harassing telephone calls. The in-
dictment charged that petitioner had assaulted a hospital
physician, Dr. James Hotz, after unlawfully entering the
2                   REHBERG v. PAULK

                     Opinion of the Court

doctor’s home. Petitioner challenged the sufficiency of the
indictment, and it was dismissed.
   A few months later, respondent returned to the grand
jury, and petitioner was indicted again, this time for as-
saulting Dr. Hotz on August 22, 2004, and for making
harassing phone calls. On this occasion, both the doctor
and respondent testified. Petitioner challenged the suf-
ficiency of this second indictment, claiming that he was
“nowhere near Dr. Hotz” on the date in question and that
“[t]here was no evidence whatsoever that [he] committed
an assault on anybody.” 611 F. 3d 828, 836 (CA11 2010).
Again, the indictment was dismissed.
   While the second indictment was still pending, respond-
ent appeared before a grand jury for a third time, and yet
another indictment was returned. Petitioner was charged
with assault and making harassing phone calls. This final
indictment was ultimately dismissed as well.
   Petitioner then brought this action against respondent
under Rev. Stat. §1979, 42 U. S. C. §1983. Petitioner
alleged that respondent conspired to present and did
present false testimony to the grand jury. Respondent
moved to dismiss, arguing, among other things, that he
was entitled to absolute immunity for his grand jury
testimony. The United States District Court for the Mid-
dle District of Georgia denied respondent’s motion to
dismiss, but the Court of Appeals reversed, holding, in
accordance with Circuit precedent, that respondent was
absolutely immune from a §1983 claim based on his grand
jury testimony.
   The Court of Appeals noted petitioner’s allegation that
respondent was the sole “complaining witness” before the
grand jury, but the Court of Appeals declined to recognize
a “complaining witness” exception to its precedent on
grand jury witness immunity. See 611 F. 3d, at 839–840.
“[A]llowing civil suits for false grand jury testimony,” the
court reasoned, “would . . . emasculate the confidential
                 Cite as: 566 U. S. ____ (2012)            3

                     Opinion of the Court

nature of grand jury testimony, and eviscerate the tradi-
tional absolute immunity for witness testimony in judi-
cial proceedings.” Id., at 840. The court went on to hold
that respondent was entitled to absolute immunity, not only
with respect to claims based directly on his grand jury
testimony, but also with respect to the claim that he con-
spired to present such testimony. Id., at 841. To allow
liability to be predicated on the alleged conspiracy, the
court concluded, “ ‘would be to permit through the back
door what is prohibited through the front.’ ” Ibid. (quoting
Jones v. Cannon, 174 F. 3d 1271, 1289 (CA11 1999)).
   We granted certiorari to resolve a Circuit conflict re-
garding the immunity of a “complaining witness” in a
grand jury proceeding, 562 U. S. ___ (2011), and we now
affirm.
                              II
  Section 1983, which derives from §1 of the Civil Rights
Act of 1871, 17 Stat. 13, creates a private right of action
to vindicate violations of “rights, privileges, or immunities
secured by the Constitution and laws” of the United
States. Under the terms of the statute, “ ‘[e]very person’
who acts under color of state law to deprive another of a
constitutional right [is] answerable to that person in a suit
for damages.” Imbler v. Pachtman, 424 U. S. 409, 417
(1976) (citing 42 U. S. C. §1983).
                            A
  Despite the broad terms of §1983, this Court has long
recognized that the statute was not meant to effect a
radical departure from ordinary tort law and the common-
law immunities applicable in tort suits. See, e.g., Burns v.
Reed, 500 U. S. 478, 484 (1991). More than 60 years ago,
in Tenney v. Brandhove, 341 U. S. 367 (1951), the Court
held that §1983 did not abrogate the long-established
absolute immunity enjoyed by legislators for actions taken
4                    REHBERG v. PAULK

                     Opinion of the Court

within the legitimate sphere of legislative authority.
Immunities “well grounded in history and reason,” the
Court wrote, were not somehow eliminated “by covert
inclusion in the general language” of §1983. Id., at 376.
   This interpretation has been reaffirmed by the Court
time and again and is now an entrenched feature of our
§1983 jurisprudence. See, e.g., Pierson v. Ray, 386 U. S.
547, 554–555 (1967) (“The legislative record gives no clear
indication that Congress meant to abolish wholesale all
common-law immunities. Accordingly, this Court held . . .
that the immunity of legislators for acts within the legisla-
tive role was not abolished. The immunity of judges for
acts within the judicial role is equally well established,
and we presume that Congress would have specifically so
provided had it wished to abolish the doctrine”); Imbler,
supra, at 418 (statute must “be read in harmony with
general principles of tort immunities and defenses rather
than in derogation of them”); Procunier v. Navarette, 434
U. S. 555, 561 (1978) (“Although the Court has recognized
that in enacting §1983 Congress must have intended to
expose state officials to damages liability in some circum-
stances, the section has been consistently construed as not
intending wholesale revocation of the common-law im-
munity afforded government officials”); Briscoe v. LaHue,
460 U. S. 325, 330 (1983) (“ ‘It is by now well settled that
the tort liability created by §1983 cannot be understood in
a historical vacuum. . . . One important assumption under-
lying the Court’s decisions in this area is that members of
the 42d Congress were familiar with common-law princi-
ples, including defenses previously recognized in ordinary
tort litigation, and that they likely intended these com-
mon-law principles to obtain, absent specific provisions to
the contrary’ ” (quoting Newport v. Fact Concerts, Inc., 453
U. S. 247, 258 (1981)); Pulliam v. Allen, 466 U. S. 522, 529
(1984) (“The starting point in our own analysis is the
common law. Our cases have proceeded on the assump-
                 Cite as: 566 U. S. ____ (2012)            5

                     Opinion of the Court

tion that common-law principles of . . . immunity were
incorporated into our judicial system and that they should
not be abrogated absent clear legislative intent to do so”).
                             B
   Recognizing that “Congress intended [§1983] to be
construed in the light of common-law principles,” the
Court has looked to the common law for guidance in de-
termining the scope of the immunities available in a §1983
action. Kalina v. Fletcher, 522 U. S. 118, 123 (1997). We
do not simply make our own judgment about the need for
immunity. We have made it clear that it is not our role “to
make a freewheeling policy choice,” Malley v. Briggs, 475
U. S. 335, 342 (1986), and that we do not have a license to
create immunities based solely on our view of sound pol-
icy, see Tower v. Glover, 467 U. S. 914, 922–923 (1984).
Instead, we conduct “a considered inquiry into the immun-
ity historically accorded the relevant official at common
law and the interests behind it.” Imbler, supra, at 421.
   We take what has been termed a “functional approach.”
See Forrester v. White, 484 U. S. 219, 224 (1988); Burns,
supra, at 486. We consult the common law to identify
those governmental functions that were historically
viewed as so important and vulnerable to interference by
means of litigation that some form of absolute immunity
from civil liability was needed to ensure that they are
performed “ ‘with independence and without fear of conse-
quences.’ ” Pierson, supra, at 554 (quoting Bradley v.
Fisher, 13 Wall. 335, 350, n. ‡ (1872)). Taking this ap-
proach, we have identified the following functions that are
absolutely immune from liability for damages under
§1983: actions taken by legislators within the legitimate
scope of legislative authority, see Tenney, supra; actions
taken by judges within the legitimate scope of judicial
authority, see Pierson, supra; actions taken by prosecutors
in their role as advocates, see Imbler, 424 U. S., at 430–
6                     REHBERG v. PAULK

                      Opinion of the Court

431; and the giving of testimony by witnesses at trial, see
Briscoe, supra. By contrast, the Court has found no abso-
lute immunity for the acts of the chief executive officer of
a State, the senior and subordinate officers of a State’s
National Guard, the president of a state university, see
Scheuer v. Rhodes, 416 U. S. 232, 247–248 (1974); school
board members, see Wood v. Strickland, 420 U. S. 308,
318 (1975); the superintendent of a state hospital, see
O’Connor v. Donaldson, 422 U. S. 563, 577 (1975); police
officers, see Pierson, supra, at 555; prison officials and
officers, Procunier, supra, at 561; and private co-
conspirators of a judge, see Dennis v. Sparks, 449 U. S. 24,
27 (1980).
                              C
    While the Court’s functional approach is tied to the
common law’s identification of the functions that merit the
protection of absolute immunity, the Court’s precedents
have not mechanically duplicated the precise scope of the
absolute immunity that the common law provided to pro-
tect those functions. See, e.g., Burns, 500 U. S., at 493
(“ ‘[T]he precise contours of official immunity’ need not
mirror the immunity at common law” (quoting Anderson v.
Creighton, 483 U. S. 635, 645 (1987))).
    This approach is illustrated by the Court’s analysis of
the absolute immunity enjoyed today by public prosecu-
tors. When §1983’s predecessor was enacted in 1871, it
was common for criminal cases to be prosecuted by private
parties. See, e.g., Stewart v. Sonneborn, 98 U. S. 187, 198
(1879) (Bradley, J., dissenting) (“[E]very man in the com-
munity, if he has probable cause for prosecuting another,
has a perfect right, by law, to institute such prosecution,
subject only, in the case of private prosecutions, to the
penalty of paying the costs if he fails in his suit”). And
private prosecutors, like private plaintiffs in civil suits, did
not enjoy absolute immunity from suit. See Malley, 475
                  Cite as: 566 U. S. ____ (2012)            7

                      Opinion of the Court

U. S., at 340–341, and n. 3 (citing cases). Instead, “the
generally accepted rule” was that a private complainant
who procured an arrest or prosecution could be held liable
in an action for malicious prosecution if the complainant
acted with malice and without probable cause. See id., at
340–341; see also Briscoe, 460 U. S., at 351 (Marshall, J.,
dissenting) (“Both English and American courts routinely
permitted plaintiffs to bring actions alleging that the de-
fendant had made a false and malicious accusation of a
felony to a magistrate or other judicial officer”); Wheeler v.
Nesbitt, 24 How. 544, 550 (1861) (“Undoubtedly, every
person who puts the criminal law in force maliciously,
and without any reasonable or probable cause, commits a
wrongful act; and if the accused is thereby prejudiced,
either in his person or property, the injury and loss so
sustained constitute the proper foundation of an action to
recover compensation”); Dinsman v. Wilkes, 12 How. 390,
402 (1852) (no immunity “where a party had maliciously,
and without probable cause, procured the plaintiff to be
indicted or arrested for an offence of which he was not
guilty”).
   In the decades after the adoption of the 1871 Civil
Rights Act, however, the prosecutorial function was in-
creasingly assumed by public officials, and common-law
courts held that public prosecutors, unlike their private
predecessors, were absolutely immune from the types of
tort claims that an aggrieved or vengeful criminal defend-
ant was most likely to assert, namely, claims for malicious
prosecution or defamation. See Imbler, supra, at 441–442
(White, J., concurring in judgment); Kalina, supra, at 124,
n. 11 (noting that cases “decided after 1871 . . . granted a
broader immunity to public prosecutors than had been
available in malicious prosecution actions against private
persons who brought prosecutions at early common law”);
see also Burns, supra, at 505 (SCALIA, J., concurring in
judgment in part and dissenting in part) (noting that the
8                    REHBERG v. PAULK

                     Opinion of the Court

“common-law tradition of prosecutorial immunity . . .
developed much later than 1871”).
   This adaptation of prosecutorial immunity accommo-
dated the special needs of public, as opposed to private,
prosecutors. Because the daily function of a public prosecu-
tor is to bring criminal charges, tort claims against public
prosecutors “could be expected with some frequency, for a
defendant often will transform his resentment at being
prosecuted into the ascription of improper and malicious
actions to the State’s advocate.” Imbler, 424 U. S., at 425.
Such “harassment by unfounded litigation would cause a
deflection of the prosecutor’s energies from his public
duties,” and would result in a severe interference with the
administration of an important public office. Id., at 423.
Constant vulnerability to vexatious litigation would give
rise to the “possibility that [the prosecutor] would shade
his decisions instead of exercising the independence of
judgment required by his public trust.” Ibid.
   Thus, when the issue of prosecutorial immunity un-
der §1983 reached this Court in Imbler, the Court did
not simply apply the scope of immunity recognized by
common-law courts as of 1871 but instead placed substan-
tial reliance on post-1871 cases extending broad immunity
to public prosecutors sued for common-law torts.
   While the Court has looked to the common law in de-
termining the scope of the absolute immunity available
under §1983, the Court has not suggested that §1983
is simply a federalized amalgamation of pre-existing
common-law claims, an all-in-one federal claim encompass-
ing the torts of assault, trespass, false arrest, defamation,
malicious prosecution, and more. The new federal claim
created by §1983 differs in important ways from those pre-
existing torts. It is broader in that it reaches constitu-
tional and statutory violations that do not correspond to
any previously known tort. See Kalina, 522 U. S., at 123.
But it is narrower in that it applies only to tortfeasors who
                  Cite as: 566 U. S. ____ (2012)            9

                      Opinion of the Court

act under color of state law. See Briscoe, supra, at 329.
Section 1983 “ha[s] no precise counterpart in state law. . . .
[I]t is the purest coincidence when state statutes or the
common law provide for equivalent remedies; any analo-
gies to those causes of action are bound to be imperfect.”
Wilson v. Garcia, 471 U. S. 261, 272 (1985) (internal quo-
tation marks and citation omitted). Thus, both the scope
of the new tort and the scope of the absolute immunity
available in §1983 actions differ in some respects from the
common law.
                              III

                               A

    At common law, trial witnesses enjoyed a limited form
of absolute immunity for statements made in the course
of a judicial proceeding: They had complete immunity
against slander and libel claims, even if it was alleged that
the statements in question were maliciously false. Kalina,
supra, at 133 (SCALIA, J., concurring) (citing F. Hilliard,
Law of Torts 319 (1866)); see Briscoe, supra, at 351 (Mar-
shall, J., dissenting); Burns, 500 U. S., at 501 (opinion of
SCALIA, J.).
    In Briscoe, however, this Court held that the immunity
of a trial witness sued under §1983 is broader: In such a
case, a trial witness has absolute immunity with respect to
any claim based on the witness’ testimony. When a wit-
ness is sued because of his testimony, the Court wrote,
“ ‘the claims of the individual must yield to the dictates of
public policy.’ ” 460 U. S., at 332–333 (quoting Calkins v.
Sumner, 13 Wis. 193, 197 (1860)). Without absolute im-
munity for witnesses, the Court concluded, the truth-
seeking process at trial would be impaired. Witnesses
“might be reluctant to come forward to testify,” and even if
a witness took the stand, the witness “might be inclined to
shade his testimony in favor of the potential plaintiff ” for
“fear of subsequent liability.” 460 U. S., at 333.
10                   REHBERG v. PAULK

                      Opinion of the Court

  The factors that justify absolute immunity for trial
witnesses apply with equal force to grand jury witnesses.
In both contexts, a witness’ fear of retaliatory litigation
may deprive the tribunal of critical evidence. And in
neither context is the deterrent of potential civil liability
needed to prevent perjurious testimony. In Briscoe, the
Court concluded that the possibility of civil liability was
not needed to deter false testimony at trial because other
sanctions—chiefly prosecution for perjury—provided a
sufficient deterrent. Id., at 342. Since perjury before a
grand jury, like perjury at trial, is a serious criminal
offense, see, e.g., 18 U. S. C. §1623(a), there is no reason to
think that this deterrent is any less effective in preventing
false grand jury testimony.
                             B
  Neither is there any reason to distinguish law enforce-
ment witnesses from lay witnesses. In Briscoe, it was
argued that absolute immunity was not needed for police-
officer witnesses, but the Court refused to draw that dis-
tinction. The Court wrote:
     “When a police officer appears as a witness, he may
     reasonably be viewed as acting like any other witness
     sworn to tell the truth—in which event he can make a
     strong claim to witness immunity; alternatively, he
     may be regarded as an official performing a critical
     role in the judicial process, in which event he may
     seek the benefit afforded to other governmental par-
     ticipants in the same proceeding. Nothing in the lan-
     guage of the statute suggests that such a witness be-
     longs in a narrow, special category lacking protection
     against damages suits.” 460 U. S., at 335–336 (foot-
     note omitted).
See also id., at 342 (“A police officer on the witness stand
performs the same functions as any other witness”).
                 Cite as: 566 U. S. ____ (2012)           11

                     Opinion of the Court

  The Briscoe Court rebuffed two arguments for distin-
guishing between law enforcement witnesses and lay
witnesses for immunity purposes: first, that absolute im-
munity is not needed for law enforcement witnesses be-
cause they are less likely to be intimidated by the threat
of suit and, second, that such witnesses should not be
shielded by absolute immunity because false testimony by
a police officer is likely to be more damaging than false
testimony by a lay witness. See ibid. The Court observed
that there are other factors not applicable to lay witnesses
that weigh in favor of extending absolute immunity to
police officer witnesses.
  First, police officers testify with some frequency. Id., at
343. “Police officers testify in scores of cases every year,”
the Court noted, “and defendants often will transform
resentment at being convicted into allegations of perjury
by the State’s official witnesses.” Ibid. If police officer
witnesses were routinely forced to defend against claims
based on their testimony, their “ ‘energy and attention
would be diverted from the pressing duty of enforcing the
criminal law.’ ” Id., at 343–344 (quoting Imbler, 424 U. S.,
at 425).
  Second, a police officer witness’ potential liability, if
conditioned on the exoneration of the accused, could influ-
ence decisions on appeal and collateral relief. 460 U. S., at
344. Needless to say, such decisions should not be influ-
enced by the likelihood of a subsequent civil rights action.
But the possibility that a decision favorable to the accused
might subject a police officer witness to liability would
create the “ ‘risk of injecting extraneous concerns’ ” into
appellate review and postconviction proceedings. Ibid.
(quoting Imbler, supra, at 428, n. 27). In addition, law
enforcement witnesses face the possibility of sanctions not
applicable to lay witnesses, namely, loss of their jobs and
other employment-related sanctions.
  For these reasons, we conclude that grand jury wit-
12                      REHBERG v. PAULK

                         Opinion of the Court

nesses should enjoy the same immunity as witnesses at
trial. This means that a grand jury witness has absolute
immunity from any §1983 claim based on the witness’
testimony. In addition, as the Court of Appeals held, this
rule may not be circumvented by claiming that a grand jury
witness conspired to present false testimony or by using
evidence of the witness’ testimony to support any other
§1983 claim concerning the initiation or maintenance of
a prosecution. Were it otherwise, “a criminal defendant
turned civil plaintiff could simply reframe a claim to at-
tack the preparation instead of the absolutely immune
actions themselves.” Buckley v. Fitzsimmons, 509 U. S.
259, 283 (1993) (KENNEDY, J., concurring in part and
dissenting in part); see also Dykes v. Hosemann, 776 F. 2d
942, 946 (CA11 1985) (per curiam) (“[J]udges, on mere
allegations of conspiracy or prior agreement, could be
hauled into court and made to defend their judicial acts,
the precise result judicial immunity was designed to
avoid”). In the vast majority of cases involving a claim
against a grand jury witness, the witness and the prose-
cutor conducting the investigation engage in preparatory
activity, such as a preliminary discussion in which the
witness relates the substance of his intended testimony.
We decline to endorse a rule of absolute immunity that is
so easily frustrated.1
                            IV
                             A
     Petitioner’s main argument is that our cases, chiefly

——————
   1 Of course, we do not suggest that absolute immunity extends to all

activity that a witness conducts outside of the grand jury room. For
example, we have accorded only qualified immunity to law enforcement
officials who falsify affidavits, see Kalina v. Fletcher, 522 U. S. 118,
129–131 (1997); Malley v. Briggs, 475 U. S. 335, 340–345 (1986), and
fabricate evidence concerning an unsolved crime, see Buckley, 509
U. S., at 272–276.
                 Cite as: 566 U. S. ____ (2012)          13

                     Opinion of the Court

Malley and Kalina, already establish that a “complaining
witness” is not shielded by absolute immunity. See Brief
for Petitioner 17–22. In those cases, law enforcement
officials who submitted affidavits in support of applica-
tions for arrest warrants were denied absolute immunity
because they “performed the function of a complaining
witness.” Kalina, 522 U. S., at 131; see Malley, 475 U. S.,
at 340–341. Relying on these cases, petitioner contends
that certain grand jury witnesses—namely, those who
qualify as “complaining witnesses”—are not entitled to
absolute immunity. Petitioner’s argument is based on a
fundamental misunderstanding of the distinctive function
played by a “complaining witness” during the period when
§1983’s predecessor was enacted.
   At that time, the term “complaining witness” was used
to refer to a party who procured an arrest and initiated a
criminal prosecution, see Kalina, 522 U. S., at 135
(SCALIA, J., concurring). A “complaining witness” might
not actually ever testify, and thus the term “ ‘witness’ in
‘complaining witness’ is misleading.” Ibid. See also Mal-
ley, supra, at 340 (complaining witness “procure[s] the
issuance of an arrest warrant by submitting a complaint”);
Wyatt v. Cole, 504 U. S. 158, 164–165 (1992) (complaining
witness “set[s] the wheels of government in motion by
instigating a legal action”).
   It is true that a mid-19th century complaining witness
might testify, either before a grand jury or at trial. But
testifying was not a necessary characteristic of a “com-
plaining witness.” See M. Newell, Malicious Prosecution
368 (1892). Nor have we been presented with evidence
that witnesses who did no more than testify before a grand
jury were regarded as complaining witnesses and were
successfully sued for malicious prosecution. See Tr. of
Oral Arg. 14–15, 24–25.
   In sum, testifying, whether before a grand jury or at
trial, was not the distinctive function performed by a
14                      REHBERG v. PAULK

                         Opinion of the Court

complaining witness. It is clear—and petitioner does not
contend otherwise—that a complaining witness cannot
be held liable for perjurious trial testimony. Briscoe, 460
U. S., at 326. And there is no more reason why a com-
plaining witness should be subject to liability for testi-
mony before a grand jury.
   Once the distinctive function performed by a “complain-
ing witness” is understood, it is apparent that a law en-
forcement officer who testifies before a grand jury is not at
all comparable to a “complaining witness.” By testifying
before a grand jury, a law enforcement officer does not
perform the function of applying for an arrest warrant; nor
does such an officer make the critical decision to initiate a
prosecution. It is of course true that a detective or case
agent who has performed or supervised most of the inves-
tigative work in a case may serve as an important witness
in the grand jury proceeding and may very much want the
grand jury to return an indictment. But such a witness,
unlike a complaining witness at common law, does not
make the decision to press criminal charges.
   Instead, it is almost always a prosecutor who is respon-
sible for the decision to present a case to a grand jury, and
in many jurisdictions, even if an indictment is handed up,
a prosecution cannot proceed unless the prosecutor signs
the indictment.2 It would thus be anomalous to permit a
police officer who testifies before a grand jury to be sued
——————
  2 The  federal courts have concluded uniformly that Rule 7(c) of the
Federal Rules of Criminal Procedure, providing that an indictment
“must be signed by an attorney for the government,” precludes federal
grand juries from issuing an indictment without the prosecutor’s
signature, signifying his or her approval. See 4 W. LaFave, J. Israel,
N. King, & O. Kerr, Criminal Procedure §15.1(d) (3d ed. 2007) (herein-
after LaFave). However, in some jurisdictions, the grand jury may
return an indictment and initiate a prosecution without the prosecu-
tor’s signature, but such cases are rare. See 1 S. Beale, W. Bryson, J.
Felman, & M. Elston, Grand Jury Law and Practice, p. 4–76, and n. 2
(2d ed. 2001).
                     Cite as: 566 U. S. ____ (2012)                   15

                          Opinion of the Court

for maliciously procuring an unjust prosecution when it is
the prosecutor, who is shielded by absolute immunity, who
is actually responsible for the decision to prosecute. See
Albright v. Oliver, 510 U. S. 266, 279, n. 5 (1994)
(GINSBURG, J., concurring) (the prosecutor is the “principal
player in carrying out a prosecution”); see ibid. (“[T]he
star player is exonerated, but the supporting actor is
not”).3
   Precisely because no grand jury witness has the power
to initiate a prosecution, petitioner is unable to provide a
workable standard for determining whether a particular
grand jury witness is a “complaining witness.” Here,
respondent was the only witness to testify in two of the
three grand jury sessions that resulted in indictments.
But where multiple witnesses testify before a grand jury,
identifying the “complaining witness” would often be
difficult. Petitioner suggests that a “complaining witness”

——————
  3 Petitioner says there is no reason to distinguish between a person
who goes to the police to swear out a criminal complaint and a person
who testifies to facts before a grand jury for the same purpose and with
the same effect. Brief for Petitioner 2, 23. But this is like saying that
a bicycle and an F-16 are the same thing. Even if the functions are
similar as a general matter, the entities are quite different. Grand
juries, by tradition, statute, and sometimes constitutional mandate,
have a status and entitlement to information that absolute immunity
furthers. See, e.g., Imbler v. Pachtman, 424 U. S. 409, 423, n. 20 (1976)
(“It is the functional comparability of their judgments to those of
the judge that has resulted in both grand jurors and prosecutors be-
ing referred to as ‘quasi-judicial’ officers, and their immunities being
termed ‘quasi-judicial’ as well”); see also United States v. Sells Engi-
neering, Inc., 463 U. S. 418, 423 (1983) (“The grand jury has always
occupied a high place as an instrument of justice in our system of
criminal law—so much so that it is enshrined in the Constitution”).
Our holding today supports the functioning of the grand jury system.
The importance of the grand jury cannot be underestimated: In the
federal system and many States, see LaFave §15.1(d), a felony cannot
be charged without the consent of community representatives, a vital
protection from unwarranted prosecutions.
16                  REHBERG v. PAULK

                     Opinion of the Court

is “someone who sets the prosecution in motion.” Tr. of
Oral Arg. 8; see Reply Brief for Petitioner 15. And peti-
tioner maintains that the same distinction made at com-
mon law between complaining witnesses and other wit-
nesses applies in §1983 actions. See id., at 14–16. But,
as we have explained, a complaining witness played a dis-
tinctive role, and therefore even when a “complaining
witness” testified, there was a clear basis for distinguish-
ing between the “complaining witness” and other wit-
nesses. Because no modern grand jury witness plays a
comparable role, petitioner’s proposed test would be of
little use. Consider a case in which the case agent or lead
detective testifies before the grand jury and provides a
wealth of background information and then a cooperating
witness appears and furnishes critical incriminating
testimony. Or suppose that two witnesses each provide
essential testimony regarding different counts of an in-
dictment or different elements of an offense. In these
cases, which witnesses would be “complaining witnesses”
and thus vulnerable to suit based on their testimony?
                              B
   Petitioner contends that the deterrent effect of civil
liability is more needed in the grand jury context because
trial witnesses are exposed to cross-examination, which is
designed to expose perjury. See Brief for Petitioner 21,
25–26. This argument overlooks the fact that a critical
grand jury witness is likely to testify again at trial and
may be cross-examined at that time. But in any event, the
force of petitioner’s argument is more than offset by a
special problem that would be created by allowing civil
actions against grand jury witnesses—subversion of grand
jury secrecy.
   “ ‘We consistently have recognized that the proper func-
tioning of our grand jury system depends upon the secrecy
of grand jury proceedings.’ ” United States v. Sells Engi-
                 Cite as: 566 U. S. ____ (2012)          17

                     Opinion of the Court

neering, Inc., 463 U. S. 418, 424 (1983) (quoting Douglas
Oil Co. v. Petrol Stops Northwest, 441 U. S. 211, 218–219
(1979)). “ ‘[I]f preindictment proceedings were made public,
many prospective witnesses would be hesitant to come
forward voluntarily, knowing that those against whom
they testify would be aware of that testimony. Moreover,
witnesses who appeared before the grand jury would be
less likely to testify fully and frankly, as they would be
open to retribution.’ ” 463 U. S., at 424.
  Allowing §1983 actions against grand jury witnesses
would compromise this vital secrecy. If the testimony of
witnesses before a grand jury could provide the basis for,
or could be used as evidence supporting, a §1983 claim,
the identities of grand jury witnesses could be discovered
by filing a §1983 action and moving for the disclosure of
the transcript of grand jury proceedings. Especially in
cases involving violent criminal organizations or other
subjects who might retaliate against adverse grand jury
witnesses, the threat of such disclosure might seriously
undermine the grand jury process.
                              C
  Finally, contrary to petitioner’s suggestion, recognizing
absolute immunity for grand jury witnesses does not
create an insupportable distinction between States that
use grand juries and those that do not. Petitioner argues
that it would make no sense to distinguish for purposes
of §1983 immunity between prosecutions initiated by the
return of a grand jury indictment and those initiated by
the filing of a complaint or information, and he notes that
26 States permit felony prosecutions to be brought by
information. Brief for Petitioner 23–24. But petitioner
draws the wrong analogy. In States that permit felony
prosecutions to be initiated by information, the closest
analog to a grand jury witness is a witness at a prelimi-
nary hearing. Most of the States that do not require an
18                  REHBERG v. PAULK

                     Opinion of the Court

indictment for felonies provide a preliminary hearing at
which witnesses testify. See LaFave §14.2(d), at 304, and
n. 47, 307, and n. 60. The lower courts have held that
witnesses at a preliminary hearing are protected by the
same immunity accorded grand jury witnesses, see, e.g.,
Brice v. Nkaru, 220 F. 3d 233, 239, n. 6 (CA4 2000); Curtis
v. Bembenek, 48 F. 3d 281, 284–285 (CA7 1995) (citing
cases), and petitioner does not argue otherwise, see Tr. of
Oral Arg. 51.
                       *    *    *
  For these reasons, we hold that a grand jury witness is
entitled to the same immunity as a trial witness. Accord-
ingly, the judgment of the Court of Appeals for the Elev-
enth Circuit is
                                                Affirmed.

```

---

## GROUP: _overhaul2/lake/cases/Rhode Island v. Innis.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Rhode Island v. Innis"
type: case
citation: "446 U.S. 291 (1980)"
parallel_cite: "100 S. Ct. 1682; 64 L. Ed. 2d 297"
neutral_cite: 1980 U.S. LEXIS 94
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-05-12
docket: 78-1076
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-05-12
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rhode Island v. Innis
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110254/rhode-island-v-innis/"
  cluster_id: 110254
  opinion_id: 9427901
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Anchor"
related: ["[[Miranda v. Arizona]]", "[[Brewer v. Williams]]", "[[Edwards v. Arizona]]", "[[Berkemer v. McCarty]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "interrogation", "functional-equivalent"]
holding: "'Interrogation' under Miranda is not limited to express questioning. It also includes the 'functional equivalent' of express…"
lake:
  record_id: Rhode Island v. Innis
  status: verified
  projected_at: 2026-07-09
---

# Rhode Island v. Innis

*446 U.S. 291 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Innis was arrested for a shotgun murder, given *[[Miranda v. Arizona|Miranda]]* warnings, and invoked his right to counsel. While transporting him, two officers conversed between themselves, expressing concern that the missing shotgun might be found by children from a nearby school for the handicapped. Innis interrupted and directed the officers to the gun. He sought to suppress the gun and his statements, arguing the conversation was interrogation conducted after he invoked counsel.

## Issue
Whether the officers' conversation constituted "interrogation" under *[[Miranda v. Arizona|Miranda]]*, such that it was barred after Innis invoked his right to counsel.

## Rule
"Interrogation" includes its functional equivalent. "We conclude that the *Miranda* safeguards come into play whenever a person in custody is subjected to either express questioning or its functional equivalent. That is to say, the term 'interrogation' under *Miranda* refers not only to express questioning, but also to any words or actions on the part of the police (other than those normally attendant to arrest and custody) that the police should know are reasonably likely to elicit an incriminating response from the suspect." — 446 U.S. at 300–301. ^pin-301

"The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police." — [*Id.* at 301](https://www.courtlistener.com/opinion/110254/rhode-island-v-innis/#:~:text=The%20latter%20portion%20of%20this). ^pin-301a

## Application
The officers' brief exchange was addressed to each other, not to Innis, and consisted of a few offhand remarks. Nothing showed the officers should have known their conversation was reasonably likely to elicit an incriminating response: there was no indication Innis was peculiarly susceptible to an appeal about the handicapped children, and the remarks were not designed to elicit a response. Because the exchange was not the functional equivalent of express questioning, Innis was not "interrogated," and suppression was not required.

## Conclusion
The officers' conversation was not interrogation under *[[Miranda v. Arizona|Miranda]]*; the Rhode Island Supreme Court's suppression order was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Innis* supplies the controlling definition of "interrogation" (express questioning or its functional equivalent) for *[[Miranda v. Arizona|Miranda]]* purposes.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Anchor*

## Sources
- *Rhode Island v. Innis*, 446 U.S. 291 (1980) — https://www.courtlistener.com/opinion/110254/rhode-island-v-innis/ — pinpoints: 300–301.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fa4045836e3ada3d", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Rhode Island v. Innis"}, "payload": {"all": [{"cite": "446 U.S. 291", "page": "291", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "446"}, {"cite": "100 S. Ct. 1682", "page": "1682", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "64 L. Ed. 2d 297", "page": "297", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "64"}, {"cite": "1980 U.S. LEXIS 94", "page": "94", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "446 U.S. 291", "official": {"cite": "446 U.S. 291", "page": "291", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "446"}, "official_selection_present": true, "record_id": "Rhode Island v. Innis"}}
{"assertion_id": "326f6e73900f2395", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-301a", "record_id": "Rhode Island v. Innis"}, "payload": {"fragment": "#:~:text=The%20latter%20portion%20of%20this", "page": null, "pin_id": "pin-301a", "pinpoint_status": "star-verified", "quote": "The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police.", "quote_fidelity": "matched", "record_id": "Rhode Island v. Innis", "star_marker": "301"}}
{"assertion_id": "740a47d6766bfccf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-301", "record_id": "Rhode Island v. Innis"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-301", "pinpoint_status": "slip-only", "quote": "under *Miranda*, such that it was barred after Innis invoked his right to counsel. ## Rule", "quote_fidelity": "mismatch", "record_id": "Rhode Island v. Innis", "star_marker": null}}
{"assertion_id": "712725790b739cd9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Rhode Island v. Innis"}, "payload": {"as_of_content": "1980-05-12", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Rhode Island v. Innis", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Rhode Island v. Innis

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rhode Island v. Innis",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rhode Island v. Innis",
    "case_name_short": "Innis",
    "case_name_full": "Rhode Island v. Innis",
    "input_case_name": "Rhode Island v. Innis",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-05-12",
    "year": 1980,
    "docket": "78-1076",
    "cluster_id": 110254,
    "lead_opinion_id": 9427901,
    "sibling_ids": [
      110254,
      9427901,
      9427902,
      9427903,
      9427904,
      9427905
    ],
    "absolute_url": "/opinion/110254/rhode-island-v-innis/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "446 U.S. 291",
      "volume": "446",
      "reporter": "U.S.",
      "page": "291",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1682",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 297",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 94",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "94",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "446 U.S. 291",
        "volume": "446",
        "reporter": "U.S.",
        "page": "291",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1682",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 L. Ed. 2d 297",
        "volume": "64",
        "reporter": "L. Ed. 2d",
        "page": "297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 94",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "94",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "446 U.S. 291",
    "official_selection": {
      "court_class": "scotus",
      "selected": "446 U.S. 291",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-301",
      "page": null,
      "quote": "under *Miranda*, such that it was barred after Innis invoked his right to counsel. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-301a",
      "page": null,
      "quote": "The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police.",
      "star_marker": "301",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17473,
      "fragment": "#:~:text=The%20latter%20portion%20of%20this",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-05-12",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rhode Island v. Innis",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Phillip W. Lowery",
          "cluster_id": 10005376,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Roberson",
          "cluster_id": 9481866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
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
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tappia Green",
          "cluster_id": 9409950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yaeger",
          "cluster_id": 10134256,
          "cite": [
            "311 Or. App. 626",
            "492 P.3d 668"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shevyakov",
          "cluster_id": 10134233,
          "cite": [
            "311 Or. App. 82",
            "489 P.3d 580"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Crawford v. Washington",
          "cluster_id": 134724,
          "cite": [
            "158 L. Ed. 2d 177",
            "124 S. Ct. 1354",
            "541 U.S. 36",
            "2004 U.S. LEXIS 1838"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
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
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
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
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Enoch",
          "cluster_id": 2139907,
          "cite": [
            "522 N.E.2d 1124",
            "122 Ill. 2d 176",
            "119 Ill. Dec. 265",
            "1988 Ill. LEXIS 41"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
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
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Beheler",
          "cluster_id": 111023,
          "cite": [
            "77 L. Ed. 2d 1275",
            "103 S. Ct. 3517",
            "463 U.S. 1121",
            "1983 U.S. LEXIS 114",
            "51 U.S.L.W. 3934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dickerson v. United States",
          "cluster_id": 118380,
          "cite": [
            "147 L. Ed. 2d 405",
            "120 S. Ct. 2326",
            "530 U.S. 428",
            "2000 U.S. LEXIS 4305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
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
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1407600,
          "cite": [
            "616 P.2d 628",
            "94 Wash. 2d 216",
            "1980 Wash. LEXIS 1360"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Neville",
          "cluster_id": 110832,
          "cite": [
            "74 L. Ed. 2d 748",
            "103 S. Ct. 916",
            "459 U.S. 553",
            "1983 U.S. LEXIS 129",
            "51 U.S.L.W. 4148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rhode Island v. Innis:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110254 OR 9427901 OR 9427902 OR 9427903 OR 9427904 OR 9427905) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg2OTA4ODAwMDAwJnM9NDc0NTUzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110254+OR+9427901+OR+9427902+OR+9427903+OR+9427904+OR+9427905%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(110254 OR 9427901 OR 9427902 OR 9427903 OR 9427904 OR 9427905)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MTkmcz0xMTE4NzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110254+OR+9427901+OR+9427902+OR+9427903+OR+9427904+OR+9427905%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110254 OR 9427901 OR 9427902 OR 9427903 OR 9427904 OR 9427905)",
        "reviewed": 110,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 110,
        "triage_read": 3,
        "triage_snippet_classified": 107
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110254 OR 9427901 OR 9427902 OR 9427903 OR 9427904 OR 9427905)",
    "indexed_citing_opinions": 3579,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110254,
        "count": 3110,
        "count_source": "search"
      },
      {
        "opinion_id": 9427901,
        "count": 526,
        "count_source": "search"
      },
      {
        "opinion_id": 9427902,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427903,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427904,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427905,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5575,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rhode-island-v-innis.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MjQ3Njkmcz0xMDYyMTgyOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110254+OR+9427901+OR+9427902+OR+9427903+OR+9427904+OR+9427905%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110254,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110254,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110254,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110254,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110254,
        "cited_id": 110207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110254,
        "cited_id": 2318620,
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
    "date_created": "2026-07-05T17:26:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:29:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:26:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rhode Island v. Innis

```
<opinion type="majority">
<author id="b351-5">Mr. Justice Stewart</author>
<p id="AyL">delivered the opinion of the Court.</p>
<p id="b351-6">In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span>, the Court held that, once a defendant in custody asks to speak with a lawyer, all interrogation must cease until a lawyer is present. The issue in this case is whether the respondent was “interrogated” in violation of the standards promulgated in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion.</p>
<p id="b351-7">I</p>
<p id="b351-8">On the night of January 12, 1975, John Mulvaney, a Providence, R. I., taxicab driver, disappeared after being dispatched to pick up a customer. His body was discovered four days later buried in a shallow grave in Coventry, R. I. He had died from a shotgun blast aimed at the back of his head.</p>
<p id="b351-9">On January 17, 1975, shortly after midnight, the Providence police received a telephone call from Gerald Aubin, also a taxicab driver, who reported that he had just been robbed by a man wielding a sawed-off shotgun. Aubin further reported that he had dropped off his assailant near Rhode Island College in a section of Providence known as Mount Pleasant. While at the Providence police station waiting to give a statement, Aubin noticed a picture of his assailant on a bulletin board. Aubin so informed one of the police officers present. The officer prepared a photo array, and again Aubin identified a picture of the same person. That person was the respondent. Shortly thereafter, the Providence police began a search of the Mount Pleasant area.</p>
<p id="b351-10">At approximately 4:30 a. m. on the same date, Patrolman Lovell, while cruising the streets of Mount Pleasant in a pa<page-number citation-index="1" label="294">*294</page-number>trol car, spotted the respondent standing in the street facing him. When Patrolman Lovell stopped his car, the respondent walked towards it. Patrolman Lovell then arrested the respondent, who was unarmed, and advised him of his so-called <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. While the two men waited in the patrol car for other police officers to arrive, Patrolman Lovell did not converse with the respondent other than to respond to the latter’s request for a cigarette.</p>
<p id="b352-5">Within minutes, Sergeant Sears arrived at the scene of the arrest, and he also gave the respondent the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Immediately thereafter, Captain Leyden and other police officers arrived. Captain Leyden advised the respondent of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The respondent stated that he understood those rights and wanted to speak with a lawyer. Captain Leyden then directed that the respondent be placed in a “caged wagon,” a four-door police car with a wire screen mesh between the front and rear seats, and be driven to the central police station. Three officers, Patrolmen Gleckman, Williams, and McKenna, were assigned to accompany the respondent to the central station. They placed the respondent in the vehicle and shut the doors. Captain Leyden then instructed the officers not to question the respondent or intimidate or coerce him in any way. The three officers then entered the vehicle, and it departed.</p>
<p id="b352-6">While en route to the central station, Patrolman Gleckman initiated a conversation with Patrolman McKenna concerning the missing shotgun.<footnotemark>1</footnotemark> As Patrolman Gleckman later testified:</p>
<blockquote id="b352-7">“A. At this point, I was talking back and forth with Patrolman McKenna stating that I frequent this area while on patrol and [that because a school for handicapped children is located nearby,] there’s a lot of handicapped children running around in this area, and God <page-number citation-index="1" label="295">*295</page-number>forbid one of them might find a weapon with shells and they might hurt themselves.” App. 43^44.</blockquote>
<p id="b353-5">Patrolman McKenna apparently shared his fellow officer’s concern:</p>
<blockquote id="b353-6">“A. I more or less concurred with him [Gleckman] that it was a safety factor and that we should, you know, continue to search for the weapon and try to find it.” <em>Id., </em>at 53.</blockquote>
<p id="b353-7">While Patrolman Williams said nothing, he overheard the conversation between the two officers:</p>
<blockquote id="b353-8">“A. He [Gleckman] said it would be too bad if the little — I believe he said a girl — would pick up the gun, maybe kill herself.” <em>Id., </em>at 59.</blockquote>
<p id="b353-9">The respondent then interrupted the conversation, stating that the officers should turn the car around so he could show them where the gun was located. At this point, Patrolman McKenna radioed back to Captain Leyden that they were returning to the scene of the arrest, and that the respondent would inform them of the location of the gun. At the time the respondent indicated that the officers should turn back, they had traveled no more than a mile, a trip encompassing only a few minutes.</p>
<p id="b353-10">The police vehicle then returned to the scene of the arrest where a search for the shotgun was in progress. There, Captain Leyden again advised the respondent of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. The respondent replied that he understood those rights but that he “wanted to get the gun out of the way bepause of the kids in the area in the school.” The respondent then led the police to a nearby field, where he pointed out the shotgun under some rocks by hhe side of the road.</p>
<p id="b353-11">On March 20, 1975, a grand jury returned an indictment charging the respondent with the kidnaping, robbery, and murder of John Mulvaney. Before trial, the respondent moved to suppress the shotgun and the statements he had <page-number citation-index="1" label="296">*296</page-number>made to the police regarding it. After an evidentiary hearing at which the respondent elected not to testify, the trial judge found that the respondent had been “repeatedly and completely advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights.” He further found that it was “entirely understandable that [the officers in the police vehicle] would voice their concern [for the safety of the handicapped children] to each other.” The judge then concluded that the respondent’s decision to inform the police of the location of the shotgun was “a waiver, clearly, and on the basis of the evidence that I have heard, and [sic] intelligent waiver, of his [Miranda] right to remain silent.” Thus, without passing on whether the police officers had in fact “interrogated” the respondent, the trial court sustained the admissibility of the shotgun and'testimony related to its discovery. That evidence was later introduced at the respondent’s trial, and the jury returned a verdict of guilty on all counts.</p>
<p id="b354-5">On appeal, the Rhode Island Supreme Court, in a 3-2 decision, set aside the respondent’s conviction. 120 R. I. -, <span class="citation" data-id="9700924"><a href="/opinion/1956720/state-v-innis/" aria-description="Citation for case: State v. Innis">391 A. 2d 1158</a></span>. Relying at least in part on this Court’s decision in <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span>, the court concluded that the respondent had invoked his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel and that, contrary to <em>Miranda’s </em>mandate that, in the absence of counsel, all custodial interrogation then cease, the police officers in the vehicle had “interrogated” the respondent without a valid waiver of his right to counsel. It was the view of the state appellate court that, even though the police officers may have been genuinely concerned about the public safety and even though the respondent had not been addressed personally by the police officers, the respondent nonetheless had been subjected to “subtle coercion” that was the equivalent of “interrogation” within the meaning of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>opinion. Moreover, contrary to the holding of the trial court, the appellate court concluded that the evidence was insufficient to support a finding of waiver. Having <page-number citation-index="1" label="297">*297</page-number>concluded that both the shotgun and testimony relating to its discovery were obtained in violation of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>standards and therefore should not have been admitted into evidence, the Rhode Island Supreme Court held that the respondent was entitled to a new trial.</p>
<p id="b355-5">We granted certiorari to address for the first time the meaning of “interrogation” under <em>Miranda </em>v. <em>Arizona. </em><span class="citation multiple-matches"><a href="/c/U.%20S./440/934/">440 U. S. 934</a></span>.</p>
<p id="b355-6">II</p>
<p id="b355-7">In its <em>Miranda </em>opinion, the Court concluded that in the context of “custodial interrogation” certain procedural safeguards are necessary to protect a defendant’s Fifth and Fourteenth Amendment privilege against compulsory self-incrimination. More specifically, the Court held that “the prosecution may not use statements, whether exculpatory or inculpatory, stemming from custodial interrogation of the defendant unless it demonstrates the use of procedural safeguards effective to secure the privilege against self-incrimination.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444</a></span>. Those safeguards included the now familiar <em>Miranda </em>warnings — namely, that the defendant be informed “that he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires” — or their equivalent. <em>Id., </em>at 479.</p>
<p id="b355-8">The Court in the <em>Miranda </em>opinion also outlined in some detail the consequences that would result if a defendant sought to invoke those procedural safeguards. With regard to the right to the presence of counsel, the Court noted:</p>
<blockquote id="b355-9">“Once warnings have been given, the subsequent procedure is clear. ... If the individual states that he wants an attorney, the interrogation must cease until an attorney is present. At that time, the individual must have an opportunity to confer with the attorney and to <page-number citation-index="1" label="298">*298</page-number>have him present during any subsequent questioning. If the individual cannot obtain an attorney and he indicates that he wants one before speaking to police, they must respect his decision to remain silent.” <em>Id., </em>at 473-474.</blockquote>
<p id="b356-5">In the present case, the parties are in agreement that the respondent was fully informed of his <em>Miranda </em>rights and that he invoked his <em>Miranda </em>right to counsel when he told Captain Leyden that he wished to consult with a lawyer. It is also uncontested that the respondent was “in custody” while being transported to the police station.</p>
<p id="b356-6">The issue, therefore, is whether the respondent was “interrogated” by the police officers in violation of the respondent’s undisputed right under <em>Miranda </em>to remain silent until he had consulted with a lawyer.<footnotemark>2</footnotemark> In resolving this issue, we first define the term “interrogation” under <em>Miranda </em>before turning to a consideration of the facts of this case.</p>
<p id="b356-7">A</p>
<p id="b356-8">The starting point for defining “interrogation” in this context is, of course, the Court’s <em>Miranda </em>opinion. There the Court observed that “[b]y custodial interrogation, we mean <em>questioning </em>initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way.” <em>Id., </em>at 444 (emphasis added). This passage and other references throughout the opinion to “questioning” might suggest that the <em>Miranda </em>rules were to apply only to those police interrogation practices that involve express questioning of a defendant while in custody.</p>
<p id="b357-4"><page-number citation-index="1" label="299">*299</page-number>We' do not, however, construe the <em>Miranda </em>opinion so narrowly. The concern of the Court in <em>Miranda </em>was that the “interrogation environment” created by the interplay of interrogation and custody would “subjugate the individual to the will of his examiner” and thereby undermine the privilege against compulsory self-incrimination. <em>Id., </em>at 457-458. The police practices that evoked this concern included several that did not involve express questioning. For example, one of the practices discussed in <em>Miranda </em>was the use of lineups in which a coached witness would pick the defendant as the perpetrator. This was designed to establish that the defendant was in fact guilty as a predicate for further interrogation. <em>Id., </em>at 453. A variation on this theme discussed in <em>Miranda </em>was the so-called “reverse line-up” in which a defendant would be identified by coached witnesses as the perpetrator of a fictitious crime, with the object of inducing him to confess to the actual crime of which he was suspected in order to escape the false prosecution. <em>Ibid. </em>The Court in <em>Miranda </em>also included in its survey of interrogation practices the use of psychological ploys, such as to “posi[t]” "the guilt of the subject,” to “minimize the moral seriousness of the offense,” and “to cast blame on the victim or on society.” <em>Id., </em>at 450. It is clear that these techniques of persuasion, no less than express questioning, were thought, in a custodial setting, to amount to interrogation.<footnotemark>3</footnotemark></p>
<p id="b357-5">This is not to say, however, that all statements obtained by the police after a person has been taken into custody are to be considered the product of interrogation. As the Court in <em>Miranda </em>noted:</p>
<blockquote id="b357-6">“Confessions remain a proper element in law enforcement. Any statement given freely and voluntarily with<page-number citation-index="1" label="300">*300</page-number>out any compelling influences is, of course, admissible in evidence. <em>The fundamental import of the privilege while an individual is in custody is not whether he is allowed to talk to the police without the benefit of warnings and counsel, but whether he can be interrogated. . . . </em>Volunteered statements of any kind are not barred by the Fifth Amendment and their admissibility is not affected by our holding today.” <em>Id., </em>at 478 (emphasis added).</blockquote>
<p id="b358-5">It is clear therefore that the special procedural safeguards outlined in <em>Miranda </em>are required not where a suspect is simply taken into custody, but rather where a suspect in custody is subjected to interrogation. “Interrogation,” as conceptualized in the <em>Miranda </em>opinion, must reflect a measure of compulsion above and beyond that inherent in custody itself.<footnotemark>4</footnotemark></p>
<p id="b358-6">We conclude that the <em>Miranda </em>safeguards come into play whenever a person in custody is subjected to either express <page-number citation-index="1" label="301">*301</page-number>questioning or its functional equivalent. That is to say, the term “interrogation” under <em>Miranda </em>refers not only to express questioning, but also to any words or actions on the part of the police (other than those normally attendant to arrest and custody) that the police should know are reasonably likely to elicit an incriminating response <footnotemark>5</footnotemark> from the suspect.<footnotemark>6</footnotemark> The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police. This focus reflects the fact that the <em>Miranda </em>safeguards were designed to vest a suspect in custody with an added measure of protection against coercive police practices, without regard to objective proof of the underlying intent of the police. A practice that the police should know is reasonably likely to evoke an incriminating response from a suspect thus amounts to interrogation.<footnotemark>7</footnotemark> But, since the police surely <page-number citation-index="1" label="302">*302</page-number>cannot be held accountable for the unforeseeable results of their words or actions, the definition of interrogation can extend only to words or actions on the part of police officers that they <em>should have known </em>were reasonably likely to elicit an incriminating response.<footnotemark>8</footnotemark></p>
<p id="b360-5">B</p>
<p id="b360-6">Turning to the facts of the present case, we conclude that the respondent was not “interrogated” within the meaning of <em>Miranda. </em>It is undisputed that the first prong of the definition of “interrogation” was not satisfied, for the conversation between Patrolmen Gleckman and McKenna included no express questioning of the respondent. Rather, that conversation was, at least in form, nothing more than a dialogue between the two officers to which no response from the respondent was invited.</p>
<p id="b360-7">Moreover, it cannot be fairly concluded that the respondent was subjected to the “functional equivalent” of questioning. It cannot be said, in short, that Patrolmen Gleckman and McKenna should have known that their conversation was reasonably likely to elicit an incriminating response from the respondent. There is nothing in the record to suggest that the officers were aware that the respondent was peculiarly susceptible to an appeal to his conscience concerning the safety of handicapped children. Nor is there anything in the <page-number citation-index="1" label="303">*303</page-number>record to suggest that the police knew that the respondent was unusually disoriented or upset at the time of his arrest.<footnotemark>9</footnotemark></p>
<p id="b361-4">The case thus boils down to whether, in the context of a brief conversation, the officers should have known that the respondent would suddenly be moved to make a self-incriminating response. Given the fact that the entire conversation appears to have consisted of no more than a few offhand remarks, we cannot say that the officers should have known that it was reasonably likely that Innis would so respond. This is not a case where the police carried on a lengthy harangue in the presence of the suspect. Nor does the record support the respondent’s contention that, under the circumstances, the officers’ comments were particularly “evocative.” It is our view, therefore, that the respondent was not subjected by the police to words or actions that the police should have known were reasonably likely to elicit an incriminating response from him.</p>
<p id="b361-5">The Rhode Island Supreme Court erred, in short, in equating “subtle compulsion” with interrogation. That the officers’ comments struck a responsive chord is readily apparent. Thus, it may be said, as the Rhode Island Supreme Court did say, that the respondent was subjected to “subtle compulsion.” But that is not the end of the inquiry. It must also be established that a suspect’s incriminating response was the product of words or actions on the part of the police that they should have known were reasonably likely to elicit an incriminating response.<footnotemark>10</footnotemark> This was not established in the present case.</p>
<p id="b362-3"><page-number citation-index="1" label="304">*304</page-number>For the reasons stated, the judgment of the Supreme Court of Rhode Island is vacated, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b362-4">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b352-8"> Although there was conflicting testimony about the exact seating arrangements, it is clear that everyone in the vehicle heard the conversation.</p>
</footnote>
<footnote label="2">
<p id="b356-9"> Since we conclude that the respondent was not “interrogated” for <em>Miranda </em>purposes, we do not reach the question whether the respondent waived his right under <em>Miranda </em>to be free from interrogation until counsel was present.</p>
</footnote>
<footnote label="3">
<p id="b357-7"> To limit the ambit of <em>Miranda </em>to express questioning would “place a premium on the ingenuity of the police to devise methods of indirect interrogation, rather than to implement the plain mandate of <em>Miranda." Commonwealth </em>v. <em>Hamilton, </em><span class="citation" data-id="2318620"><a href="/opinion/2318620/commonwealth-v-hamilton/#297" aria-description="Citation for case: Commonwealth v. Hamilton">445 Pa. 292, 297</a></span>, <span class="citation" data-id="2318620"><a href="/opinion/2318620/commonwealth-v-hamilton/#175" aria-description="Citation for case: Commonwealth v. Hamilton">285 A. 2d 172, 175</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b358-7"> There is language in the opinion of the Rhode Island Supreme Court in this case suggesting that the definition of “interrogation” under <em>Miranda </em>is informed by this Court’s decision in <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span>. 120 R. I. —,-, <span class="citation" data-id="9700924"><a href="/opinion/1956720/state-v-innis/#1161" aria-description="Citation for case: State v. Innis">391 A. 2d 1158, 1161-1162</a></span>. This suggestion is erroneous. Our decision in <em>Brewer </em>rested solely on the Sixth and Fourteenth Amendment right to counsel. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#397" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 397-399</a></span>. That right, as we held in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 206</a></span>, prohibits law enforcement officers from “deliberately elicit [ing]” incriminating information from a defendant in the absence of counsel after a formal charge against the defendant has been filed. Custody in such a case is not controlling; indeed, the petitioner in <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>was not in custody. By contrast, the right to counsel at issue in the present case is based not on the Sixth and Fourteenth Amendments, but rather on the Fifth and Fourteenth Amendments as interpreted in the <em>Miranda </em>opinion. The definitions of “interrogation” under the Fifth and Sixth Amendments, if indeed the term “interrogation” is even apt in the Sixth Amendment context, are not necessarily interchangeable, since the policies underlying the two constitutional protections are quite distinct. See Kamisar, <em>Brewer v. Williams, Massiah, </em>and <em>Miranda: </em>What is “Interrogation”? When Does it Matter?, 67 Geo. L. J. 1, 41-55 (1978).</p>
</footnote>
<footnote label="5">
<p id="b359-5"> By “incriminating response” we refer to any response — whether incul-patory or exculpatory — that the <em>prosecution </em>may seek to introduce at trial. As the Court observed in <em>Miranda:</em></p>
<blockquote id="b359-6">“No distinction can be drawn between statements which are direct confessions and statements which amount to ‘admissions’ of part or all of an offense. The privilege against self-incrimination protects the individual from being compelled to incriminate himself in any manner; it does not distinguish degrees of incrimination. Similarly, for precisely the same reason, no distinction may be drawn between inculpatory statements and statements alleged to be merely ‘exculpatory.’ If a statement made were in fact truly exculpatory it would, of course, never be used by the prosecution. In fact, statements merely intended to be exculpatory by the defendant are often used to impeach his testimony at trial or to demonstrate untruths in the statement given under interrogation and thus to prove guilt by implication. These statements are incriminating in any meaningful sense of the word and may not be used without the full warnings and effective waiver required for any other statement.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476-477</a></span>.</blockquote>
</footnote>
<footnote label="6">
<p id="b359-7"> One of the dissenting opinions seems totally to misapprehend this definition in suggesting that it “will almost certainly exclude every statement [of the police] that is not punctuated with a question mark.” Post, at 312.</p>
</footnote>
<footnote label="7">
<p id="b359-8"> This is not to say that the intent of the police is irrelevant, for it <page-number citation-index="1" label="302">*302</page-number>may well have a bearing on whether the police should have known that their words or actions were reasonably likely to evoke an incriminating response. In particular, where a police practice is designed to elicit an incriminating response from the accused, it is unlikely that the practice will not also be one which the police should have known was reasonably likely to have that effect.</p>
</footnote>
<footnote label="8">
<p id="b360-14"> Any knowledge the police may have had concerning the unusual susceptibility of a defendant to a particular form of persuasion might be an important factor in determining whether the police should have known that their words or actions were reasonably likely to elicit an incriminating response from the suspect.</p>
</footnote>
<footnote label="9">
<p id="b361-6"> The record in no way suggests that the officers’ remarks were <em>designed </em>to elicit a response. See n. 7, <em>supra. </em>It is significant that the trial judge, after hearing the officers’ testimony, concluded that it was “entirely understandable that [the officers] would voice their concern [for the safety of the handicapped children] to each other.”</p>
</footnote>
<footnote label="10">
<p id="b361-7"> By way of example, if the police had done no more than to drive past the site of the concealed weapon while taking the most direct route to the police station, and if the respondent, upon noticing for the first time <page-number citation-index="1" label="304">*304</page-number>the proximity of the school for handicapped children, had blurted out that he would show the officers where the gun was located, it could not seriously be argued that this “subtle compulsion” would have constituted “interrogation” within the meaning of the <em>Miranda </em>opinion.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Richards v. Wisconsin.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Richards v. Wisconsin"
type: case
citation: "520 U.S. 385 (1997)"
parallel_cite: "117 S. Ct. 1416; 137 L. Ed. 2d 615"
neutral_cite: 1997 U.S. LEXIS 2794
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1997
date_decided: 1997-04-28
docket: 96-5955
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1997-04-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Richards v. Wisconsin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118103/richards-v-wisconsin/"
  cluster_id: 118103
  opinion_id: 118103
  identity_checked: true
homes:
  - page: "[[Knock-and-Announce]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wilson v. Arkansas]]", "[[Hudson v. Michigan]]", "[[Maryland v. Buie]]"]
aliases: []
tags: ["case", "fourth-amendment", "knock-and-announce", "no-knock", "reasonable-suspicion", "warrant-execution"]
holding: "There is **no blanket exception** to knock-and-announce for entire categories of crime (e.g., felony drug cases); the no-knock decision…"
lake:
  record_id: Richards v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# Richards v. Wisconsin

*520 U.S. 385 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers had a warrant to search Richards's motel room for drugs (the magistrate had deleted no-knock authorization). An officer posing as a maintenance man knocked; Richards opened the door, saw a uniformed officer, and quickly closed it. The officers then forced entry without further announcement and found drugs and cash. The Wisconsin Supreme Court upheld the entry under a blanket rule that police need never knock and announce when executing a warrant in a felony drug investigation.

## Issue
Whether the Fourth Amendment permits a blanket exception to the [[Knock-and-Announce|knock-and-announce]] requirement for an entire category of crime — all felony drug investigations.

## Rule
No blanket exception. "[T]he fact that felony drug investigations may frequently present circumstances warranting a no-knock entry cannot remove from the neutral scrutiny of a reviewing court the reasonableness of the police decision not to knock and announce in a particular case." — 520 U.S. at 394. ^pin-394

"In order to justify a 'no-knock' entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence." — 520 U.S. at 394. ^pin-394a

## Application
Rejecting Wisconsin's blanket rule, the Court nonetheless held the no-knock entry into Richards's room was reasonable on these facts: once Richards opened the door, recognized the police, and slammed it, the officers had reasonable suspicion that he would destroy the easily disposable drugs if they paused to announce. The magistrate's deletion of no-knock authority did not control, because reasonableness is judged as of the moment of entry.

## Conclusion
There is no blanket [[Knock-and-Announce|knock-and-announce]] exception for drug cases; case-specific reasonable suspicion is required, and it was present here, so the entry was upheld and the judgment affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Richards* refines the [[Knock-and-Announce|knock-and-announce]] rule of [[Wilson v. Arkansas]]; suppression for a [[Knock-and-Announce|knock-and-announce]] violation was later denied in [[Hudson v. Michigan]].

## Appears on
- [[Knock-and-Announce]] — *Key — Progeny / Refinement*

## Sources
- *Richards v. Wisconsin*, 520 U.S. 385 (1997) — https://www.courtlistener.com/opinion/118103/richards-v-wisconsin/ — pinpoint: 394.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5c5346620199b4c0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Richards v. Wisconsin"}, "payload": {"all": [{"cite": "520 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "520"}, {"cite": "117 S. Ct. 1416", "page": "1416", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "117"}, {"cite": "137 L. Ed. 2d 615", "page": "615", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "1997 U.S. LEXIS 2794", "page": "2794", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1997"}], "display": "520 U.S. 385", "official": {"cite": "520 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "520"}, "official_selection_present": true, "record_id": "Richards v. Wisconsin"}}
{"assertion_id": "2f1dc0ec1c4a2898", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-394a", "record_id": "Richards v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-394a", "pinpoint_status": "slip-only", "quote": "In order to justify a 'no-knock' entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence.", "quote_fidelity": "mismatch", "record_id": "Richards v. Wisconsin", "star_marker": null}}
{"assertion_id": "97214cb6986a5c63", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-394", "record_id": "Richards v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-394", "pinpoint_status": "slip-only", "quote": "--- # Richards v. Wisconsin *520 U.S. 385 (1997)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search Richards's motel room for drugs (the magistrate had deleted no-knock authorization). An officer posing as a maintenance man knocked; Richards opened the door, saw a uniformed officer, and quickly closed it. The officers then forced entry without further announcement and found drugs and cash. The Wisconsin Supreme Court upheld the entry under a blanket rule that police need never knock and announce when executing a warrant in a felony drug investigation. ## Issue Whether the Fourth Amendment permits a blanket exception to the knock-and-announce requirement for an entire category of crime — all felony drug investigations. ## Rule No blanket exception.", "quote_fidelity": "mismatch", "record_id": "Richards v. Wisconsin", "star_marker": null}}
{"assertion_id": "cb4350cfed4ed172", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Richards v. Wisconsin"}, "payload": {"as_of_content": "1997-04-28", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Richards v. Wisconsin", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Richards v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Richards v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Richards v. Wisconsin",
    "case_name_short": "Richards",
    "case_name_full": "Richards v. Wisconsin",
    "input_case_name": "Richards v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1997-04-28",
    "year": 1997,
    "docket": "96-5955",
    "cluster_id": 118103,
    "lead_opinion_id": 118103,
    "sibling_ids": [
      118103
    ],
    "absolute_url": "/opinion/118103/richards-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9163841,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9163840,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9162684,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9162683,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      },
      {
        "cluster_id": 9284920,
        "score": 20,
        "case_name": "Richards v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "520 U.S. 385",
      "volume": "520",
      "reporter": "U.S.",
      "page": "385",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "117 S. Ct. 1416",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 615",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1997 U.S. LEXIS 2794",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "520 U.S. 385",
        "volume": "520",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "117 S. Ct. 1416",
        "volume": "117",
        "reporter": "S. Ct.",
        "page": "1416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 L. Ed. 2d 615",
        "volume": "137",
        "reporter": "L. Ed. 2d",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1997 U.S. LEXIS 2794",
        "volume": "1997",
        "reporter": "U.S. LEXIS",
        "page": "2794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "520 U.S. 385",
    "official_selection": {
      "court_class": "scotus",
      "selected": "520 U.S. 385",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-394",
      "page": null,
      "quote": "--- # Richards v. Wisconsin *520 U.S. 385 (1997)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers had a warrant to search Richards's motel room for drugs (the magistrate had deleted no-knock authorization). An officer posing as a maintenance man knocked; Richards opened the door, saw a uniformed officer, and quickly closed it. The officers then forced entry without further announcement and found drugs and cash. The Wisconsin Supreme Court upheld the entry under a blanket rule that police need never knock and announce when executing a warrant in a felony drug investigation. ## Issue Whether the Fourth Amendment permits a blanket exception to the knock-and-announce requirement for an entire category of crime \u2014 all felony drug investigations. ## Rule No blanket exception.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-394a",
      "page": null,
      "quote": "In order to justify a 'no-knock' entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1997-04-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Richards v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
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
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Sunny Burton v. State",
          "cluster_id": 3092638,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Foster",
          "cluster_id": 835141,
          "cite": [
            "217 P.3d 168",
            "347 Or. 1",
            "2009 Ore. LEXIS 223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
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
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dennis Russell Callaghan",
          "cluster_id": 2933574,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Southerland, Vince",
          "cluster_id": 186774,
          "cite": [
            "373 U.S. App. D.C. 305",
            "466 F.3d 1083",
            "2006 U.S. App. LEXIS 26978",
            "2006 WL 3069122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Singleton",
          "cluster_id": 793669,
          "cite": [
            "441 F.3d 290",
            "2006 U.S. App. LEXIS 7201",
            "2006 WL 724800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
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
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1790339,
          "cite": [
            "177 S.W.3d 8"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Henning",
          "cluster_id": 1060855,
          "cite": [
            "975 S.W.2d 290",
            "1998 Tenn. LEXIS 370",
            "1998 WL 324318"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramirez",
          "cluster_id": 118180,
          "cite": [
            "140 L. Ed. 2d 191",
            "118 S. Ct. 992",
            "523 U.S. 65",
            "1998 U.S. LEXIS 1600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Banks",
          "cluster_id": 131146,
          "cite": [
            "157 L. Ed. 2d 343",
            "124 S. Ct. 521",
            "540 U.S. 31",
            "2003 U.S. LEXIS 8966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James H. Spikes (96-3899) Marilyn Smith (96-3660)",
          "cluster_id": 758684,
          "cite": [
            "158 F.3d 913",
            "49 Fed. R. Serv. 1564",
            "1998 U.S. App. LEXIS 21399",
            "1998 WL 551966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terebesi v. Torreso",
          "cluster_id": 8441937,
          "cite": [
            "764 F.3d 217",
            "2014 U.S. App. LEXIS 16133",
            "2014 WL 4099309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cheryl D. Lyons v. City of Xenia, Christine Keith, Officer Matthew Foubert, Officer",
          "cluster_id": 791266,
          "cite": [
            "417 F.3d 565",
            "2005 U.S. App. LEXIS 16034",
            "2005 WL 1846994"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Eason",
          "cluster_id": 1863783,
          "cite": [
            "2001 WI 98",
            "629 N.W.2d 625",
            "245 Wis. 2d 206",
            "2001 Wisc. LEXIS 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Fields Christopher Crawley",
          "cluster_id": 740479,
          "cite": [
            "113 F.3d 313",
            "1997 U.S. App. LEXIS 10728"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Zhahir",
          "cluster_id": 2196510,
          "cite": [
            "751 A.2d 1153",
            "561 Pa. 545",
            "2000 Pa. LEXIS 1245"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Trent v. Steven Wade",
          "cluster_id": 2774855,
          "cite": [
            "776 F.3d 368",
            "2015 WL 394096"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bravo v. City of Santa Maria",
          "cluster_id": 618647,
          "cite": [
            "665 F.3d 1076",
            "101 A.L.R. 6th 615",
            "2011 U.S. App. LEXIS 24383",
            "2011 WL 6117918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Quinn v. Jesus Guerrero",
          "cluster_id": 4407590,
          "cite": [
            "863 F.3d 353",
            "2017 WL 2951586",
            "2017 U.S. App. LEXIS 12290"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie Jacobs and Linda Siller v. City of Chicago , a Municipal Corporation the Estate of Sergeant Michael Garner Officers Quintero, Buckner, McLean Keith, and Garrido and Metropolitan Enforcement Group Officers Huff, Martin, Sowinski, and McIntyre",
          "cluster_id": 769087,
          "cite": [
            "215 F.3d 758",
            "46 Fed. R. Serv. 3d 832",
            "2000 U.S. App. LEXIS 12013"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Larry J. Leaf, Individually and as Personal Representative of the Estate of John P. Leaf, Deceased, Martha A. Leaf, John P. Leaf v. Ronald Shelnutt",
          "cluster_id": 789551,
          "cite": [
            "400 F.3d 1070",
            "2005 U.S. App. LEXIS 4513",
            "2005 WL 628217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelly Donald Gould",
          "cluster_id": 785789,
          "cite": [
            "364 F.3d 578",
            "2004 U.S. App. LEXIS 5505",
            "2004 WL 576173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 2181223,
          "cite": [
            "846 A.2d 569",
            "179 N.J. 377",
            "2004 N.J. LEXIS 437"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 1614689,
          "cite": [
            "2000 WI 3",
            "604 N.W.2d 517",
            "231 Wis. 2d 723",
            "2000 Wisc. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adcock v. Commonwealth",
          "cluster_id": 2433405,
          "cite": [
            "967 S.W.2d 6",
            "1998 Ky. LEXIS 59",
            "1998 WL 178596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nordstrom",
          "cluster_id": 2587271,
          "cite": [
            "25 P.3d 717",
            "200 Ariz. 229",
            "350 Ariz. Adv. Rep. 16",
            "2001 Ariz. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Richards v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118103) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTA4MzM5MjAwMDAwJnM9MTU0NzY1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118103%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118103)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NSZzPTIwMzYwMzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28118103%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118103)",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 0,
        "triage_snippet_classified": 12
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118103)",
    "indexed_citing_opinions": 584,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118103,
        "count": 584,
        "count_source": "search"
      }
    ],
    "citation_count": 959,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/richards-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY3NDA1MDgmcz00NzQ3Mzk3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28118103%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118103,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 112873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1124319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1504743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1632862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 1677415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118103,
        "cited_id": 2032318,
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
    "date_created": "2026-07-05T17:29:24Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:33:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:30:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Richards v. Wisconsin

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b479-5">
  Justice Stevens
 </author>
<p id="AAd">
  delivered the opinion of the Court.
 </p>
<p id="b479-6">
  In
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), we held that the Fourth Amendment incorporates the common-law requirement that police officers entering a dwelling must knock on the door and announce their identity and purpose before attempting forcible entry. At the same time, we recognized that the “flexible requirement of reasonableness should not be read to mandate a rigid rule of announcement that ignores countervailing law enforcement interests,”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#934" aria-description="Citation for case: Wilson v. Arkansas"><em>
   id.,
  </em>
  at 934</a></span>, and left “to the lower courts the task of determining the circumstances under which an unannounced entry is reasonable under the Fourth Amendment,”
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#936" aria-description="Citation for case: Wilson v. Arkansas"><em>
   id.,
  </em>
  at 936</a></span>.
 </p>
<p id="b479-7">
  In this case, the Wisconsin Supreme Court concluded that police officers are
  <em>
   never
  </em>
  required to knock and announce their presence when executing a search warrant in a felony
  <span citation-index="1" class="star-pagination" label="388"> 
   *388
   </span>
  drug investigation. In so doing, it reaffirmed a
  <em>
   pre-Wilson
  </em>
  holding and concluded that
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  did not preclude this
  <em>
   per se
  </em>
  rule. We disagree with the court’s conclusion that the Fourth Amendment permits a blanket exception to the knock-and-announce requirement for this entire category of criminal activity. But because the evidence presented to support the officers’ actions in this case establishes that the decision not to knock and announce was a reasonable one under the circumstances, we affirm the judgment of the Wisconsin court.
 </p>
<p id="b480-5">
  I
 </p>
<p id="b480-6">
  On December 31, 1991, police officers in Madison, Wisconsin, obtained a warrant to search Steiney Richards’ motel room for drugs and related paraphernalia. The search warrant was the culmination of an investigation that had uncovered substantial evidence that Richards was one of several individuals dealing drugs out of hotel rooms in Madison. The police requested a warrant that would have given advance authorization for a “no-knock” entry into the motel room, but the Magistrate explicitly deleted those portions of the warrant. App. 7, 9.
 </p>
<p id="b480-7">
  The officers arrived at the motel room at 3:40 a.m. Officer Pharo, dressed as a maintenance man, led the team. With him were several plainclothes officers and at least one man in uniform. Officer Pharo knocked on Richards’ door and, responding to the query from inside the room, stated that he was a maintenance man. With the chain still on the door, Richards cracked it open. Although there is some dispute as to what occurred next, Richards acknowledges that when he opened the door he saw the man in uniform standing behind Officer Pharo. Brief for Petitioner 6. He quickly slammed the door closed and, after waiting two or three seconds, the officers began kicking and ramming the door to gain entry to the locked room. At trial, the officers testified that they identified themselves as police while they were kicking the door in. App. 40. When they finally did break
  <span citation-index="1" class="star-pagination" label="389"> 
   *389
   </span>
  into the room, the officers caught Richards trying to escape through the window. They also found cash and cocaine hidden in plastic bags above the bathroom ceiling tiles.
 </p>
<p id="b481-5">
  Richards sought to have the evidence from his motel room suppressed on the ground that the officers had failed to knock and announce their presence prior to forcing entry into the room. The trial court denied the motion, concluding that the officers could gather from Richards’ strange behavior when they first sought entry that he knew they were police officers and that he might try to destroy evidence or to escape.
  <em>
   Id.,
  </em>
  at 54. The judge emphasized that the easily disposable nature of the drugs the police were searching for further justified their decision to identify themselves as they crossed the threshold instead of announcing their presence before seeking entry.
  <em>
   Id.,
  </em>
  at 55. Richards appealed the decision to the Wisconsin Supreme Court and that court affirmed. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/" aria-description="Citation for case: State v. Richards">201 Wis. 2d 845</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/" aria-description="Citation for case: State v. Richards">549 N. W. 2d 218</a></span> (1996).
 </p>
<p id="b481-6">
  The Wisconsin Supreme Court did not delve into the events underlying Richards’ arrest in any detail, but accepted the following facts: “[0]n December 31, 1991, police executed a search warrant for the motel room of the defendant seeking evidence of the felonious crime of Possession with Intent to Deliver a Controlled Substance in violation of <span class="citation no-link">Wis. Stat. § 161.41</span>(lm) (1991-92). They did not knock and announce prior to their entry. Drugs were seized.”
  <span class="citation no-link"><em>
   Id.,
  </em>
  at 849</span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#220" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 220</a></span>.
 </p>
<p id="b481-7">
  Assuming these facts, the court proceeded to consider whether our decision in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  required the court to abandon its decision in
  <em>
   State
  </em>
  v.
  <em>
   Stevens,
  </em>
  <span class="citation" data-id="9668150"><a href="/opinion/1677415/state-v-stevens/" aria-description="Citation for case: State v. Stevens">181 Wis. 2d 410</a></span>, <span class="citation" data-id="9668150"><a href="/opinion/1677415/state-v-stevens/" aria-description="Citation for case: State v. Stevens">511 N. W. 2d 591</a></span> (1994), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./515/1102/">515 U. S. 1102</a></span> (1995), which held that “when the police have a search warrant, supported by probable cause, to search a residence for evidence of delivery of drugs or evidence of possession with intent to deliver drugs, they necessarily have reasonable cause to believe exigent circumstances exist” to justify a no-knock entry. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#852" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 852</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#221" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 221</a></span>. The court concluded
  <span citation-index="1" class="star-pagination" label="390"> 
   *390
   </span>
  that nothing in
  <em>
   Wilson’s
  </em>
  acknowledgment that the knock- and-announce rule was an element of the Fourth Amendment “reasonableness” requirement would prohibit application of a
  <em>
   per se
  </em>
  exception to that rule in a category of cases. <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#854" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 854-855</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#220" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 220</a></span>.
 </p>
<p id="b482-5">
  In reaching this conclusion, the Wisconsin court found it reasonable — after considering criminal conduct surveys, newspaper articles, and other judicial opinions — to assume that all felony drug crimes will involve “an extremely high risk of serious if not deadly injury to the police as well as the potential for the disposal of drugs by the occupants prior to entry by the police.”
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#847" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 847-848</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#219" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 219</a></span>. Notwithstanding its acknowledgment that in “some cases, police officers will undoubtedly decide that their safety, the safety of others, and the effective execution of the warrant dictate that they knock and announce,”
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#863" aria-description="Citation for case: State v. Richards"><em>
   id.,
  </em>
  at 863</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#225" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 225</a></span>, the court concluded that exigent circumstances justifying a no-knock entry are always present in felony drug cases. Further, the court reasoned that the violation of privacy that occurs when officers who have a search warrant forcibly enter a residence without first announcing their presence is minimal, given that the residents would ultimately be without authority to refuse the police entry. The principal intrusion on individual privacy interests in such a situation, the court concluded, comes from the issuance of the search warrant, not the manner in which it is executed.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#864" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 864-865</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#226" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 226</a></span>. Accordingly, the court determined that police in Wisconsin do not need specific information about dangerousness, or the possible destruction of drugs in a particular case, in order to dispense with the knock-and-announce requirement in felony drug cases.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b483-7">
<span citation-index="1" class="star-pagination" label="391"> 
   *391
   </span>
  Justice Abrahamson concurred in the judgment because, in her view, the facts found by the trial judge justified a no-knock entry.
  <em>
   Id,.,
  </em>
  at 866-868, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#227" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 227</a></span>. Specifically, she noted that Richards’ actions in slamming the door when he saw the uniformed man standing behind Officer Pharo indicated that he already knew that the people knocking on his door were police officers. Under these circumstances, any further announcement of their presence would have been a useless gesture.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#868" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 868-869, n. 3</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#228" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 228, n. 3</a></span>. While agreeing with the outcome, Justice Abrahamson took issue with her colleagues’ affirmation of the blanket exception to the knock-and-announce requirement in drug felony cases. She observed that the constitutional reasonableness of a search has generally been a matter left to the court, rather than to the officers who conducted the search, and she objected to the creation of a blanket rule that insulated searches in a particular category of crime from the neutral oversight of a reviewing judge.
  <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#868" aria-description="Citation for case: State v. Richards"><em>
   Id.,
  </em>
  at 868-875</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#228" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 228-230</a></span>.
 </p>
<p id="AxNk">
  II
 </p>
<p id="Ahtv">
  We recognized in
  <em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
  </em>
  that the knock-and-announce requirement could give way “under circumstances presenting a threat of physical violence,” or “where police officers have reason to believe that evidence would likely be destroyed if advance notice were given.” <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#936" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 936</a></span>. It is indisputable that felony drug investigations may frequently involve both of these circumstances.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The question we must
  <span citation-index="1" class="star-pagination" label="392"> 
   *392
   </span>
  resolve is whether this fact justifies dispensing with case-by-case evaluation of the manner in which a search was executed.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b484-5">
  The Wisconsin court explained its blanket exception as necessitated by the special circumstances of today’s drug culture, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#863" aria-description="Citation for case: State v. Richards">201 Wis. 2d, at 863-866</a></span>, <span class="citation" data-id="9524169"><a href="/opinion/2032318/state-v-richards/#226" aria-description="Citation for case: State v. Richards">549 N. W. 2d, at 226-227</a></span>, and the State asserted at oral argument that the blanket exception was reasonable in “felony drug cases because of the convergence in a violent and dangerous form of commerce of weapons and the destruction of drugs.” Tr. of Oral Arg. 26. But creating exceptions to the knock-and-announce rule based on the “culture” surrounding a general category of criminal behavior presents at least two serious concerns.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b485-4">
<span citation-index="1" class="star-pagination" label="393"> 
   *393
   </span>
  First, the exception contains considerable overgeneralization. For example, while drug investigation frequently does pose special risks to officer safety and the preservation of evidence, not every drug investigation will pose these risks to a substantial degree. For example, a search could be conducted at a time when the only individuals present in a residence have no connection with the drug activity and thus will be unlikely to threaten officers or destroy evidence. Or the police could know that the drugs being searched for were of a type or in a location that made them impossible to destroy quickly. In those situations, the asserted governmental interests in preserving evidence and maintaining safety may not outweigh the individual privacy interests intruded upon by a no-knock entry.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Wisconsin’s blanket rule imper-missibly insulates these cases from judicial review.
 </p>
<p id="b485-5">
  A second difficulty with permitting a criminal-category exception to the knock-and-announce requirement is that the
  <span citation-index="1" class="star-pagination" label="394"> 
   *394
   </span>
  reasons for creating an exception in one category can, relatively easily, be applied to others. Armed bank robbers, for example, are, by definition, likely to have weapons, and the fruits of their crime may be destroyed without too much difficulty. If a
  <em>
   per se
  </em>
  exception were allowed for each category of criminal investigation that included a considerable — albeit hypothetical — risk of danger to officers or destruction of evidence, the knock-and-announce element of the Fourth Amendment’s reasonableness requirement would be meaningless.
 </p>
<p id="b486-4">
  Thus, the fact that felony drug investigations may frequently present circumstances warranting a no-knock entry cannot remove from the neutral scrutiny of a reviewing court the reasonableness of the police decision not to knock and announce in a particular case. Instead, in each case, it is the duty of a court confronted with the question to determine whether the facts and circumstances of the particular entry justified dispensing with the knock-and-announce requirement.
 </p>
<p id="b486-5">
  In order to justify a “no-knock” entry, the police must have a reasonable suspicion that knocking and announcing their presence, under the particular circumstances, would be dangerous or futile, or that it would inhibit the effective investigation of the crime by, for example, allowing the destruction of evidence. This standard — as opposed to a probable-cause requirement — strikes the appropriate balance between the legitimate law enforcement concerns at issue in the execution of search warrants and the individual privacy interests affected by no-knock entries. Cf.
  <em>
   Maryland
  </em>
  v.
  <em>
   Buie,
  </em>
  <span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#337" aria-description="Citation for case: Maryland v. Buie">494 U. S. 325, 337</a></span> (1990) (allowing a protective sweep of a house during an arrest where the officers have “a reasonable belief based on specific and articulable facts that the area to be swept harbors an individual posing a danger to those on the arrest scene”);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#30" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 30</a></span> (1968) (requiring a reasonable and articulable suspicion of danger to justify a patdown search). This showing is not high, but the police
  <span citation-index="1" class="star-pagination" label="395"> 
   *395
   </span>
  should be required to make it whenever the reasonableness of a no-knock entry is challenged.
 </p>
<p id="b487-5">
  III
 </p>
<p id="b487-6">
  Although we reject the Wisconsin court’s blanket exception to the knock-and-announce requirement, we conclude that the officers’ no-knock entry into Richards’ motel room did not violate the Fourth Amendment. We agree with the trial court, and with Justice Abrahamson, that the circumstances in this case show that the officers had a reasonable suspicion that Richards might destroy evidence if given further opportunity to do so.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b487-7">
  The judge who heard testimony at Richards’ suppression hearing concluded that it was reasonable for the officers executing the warrant to believe that Richards knew, after opening the door to his motel room the first time, that the men seeking entry to his room were the police. App. 54. Once the officers reasonably believed that Richards knew who they were, the court concluded, it was reasonable for them to force entry immediately given the disposable nature of the drugs.
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#55" aria-description="Citation for case: Terry v. Ohio"><em>
   Id.,
  </em>
  at 55</a></span>.
 </p>
<p id="b487-8">
  In arguing that the officers’ entry was unreasonable, Richards places great emphasis on the fact that the Magistrate who signed the search warrant for his motel room deleted the portions of the proposed warrant that would have given the officers permission to execute a no-knock entry. But this fact does not alter the reasonableness of the officers’ decision, which must be evaluated as of the time they entered the motel room. At the time the officers obtained the warrant, they did not have evidence sufficient, in the judgment of the Magistrate, to justify a no-knock warrant. Of course,
  <span citation-index="1" class="star-pagination" label="396"> 
   *396
   </span>
  the Magistrate could not have anticipated in every particular the circumstances that would confront the officers when they arrived at Richards’ motel room.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  These actual circumstances — petitioner’s apparent recognition of the officers combined with the easily disposable nature of the drugs— justified the officers’ ultimate decision to enter without first announcing their presence and authority.
 </p>
<p id="b488-5">
  Accordingly, although we reject the blanket exception to the knock-and-announce requirement for felony drug investigations, the judgment of the Wisconsin Supreme Court is affirmed.
 </p>
<p id="b488-6">
<em>
   It is so ordered.
  </em>
</p>







<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b482-6">
   Several other state courts — in eases that predate our decision in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   — have adopted similar rules, concluding that simple probable cause to search a home for narcotics always allows the police to forgo the knock- and-announce requirement. See, e.
   <em>
    g., People
   </em>
   v.
   <em>
    Lujan,
   </em>
   <span class="citation" data-id="1185551"><a href="/opinion/1185551/people-v-lujan/#1241" aria-description="Citation for case: People v. Lujan">484 P. 2d 1238, 1241</a></span> (Colo. 1971) (en banc);
   <em>
    Henson
   </em>
   v.
   <em>
    State,
   </em>
   <span class="citation no-link">236 Md. 519</span>, 523-524, 204 A.
   <span citation-index="1" class="star-pagination" label="391"> 
    *391
    </span>
   2d 516, 519-520 (1964);
   <em>
    State
   </em>
   v.
   <em>
    Loucks,
   </em>
   <span class="citation" data-id="1632862"><a href="/opinion/1632862/state-v-loucks/#777" aria-description="Citation for case: State v. Loucks">209 N. W. 2d 772, 777-778</a></span> (N. D. 1973). Cf.
   <em>
    People
   </em>
   v.
   <em>
    De Lago,
   </em>
   16 N. Y. 2d 289, 292, <span class="citation" data-id="5522059"><a href="/opinion/5674482/people-v-de-lago/#661" aria-description="Citation for case: People v. De Lago">213 N. E. 2d 659, 661</a></span> (1965) (similar rule for searches related to gambling operations), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./383/963/">383 U. S. 963</a></span> (1966).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b483-5">
   This Court has encountered before the links between drugs and violence, see,
   <em>
    e. g., Michigan
   </em>
   v.
   <em>
    Summers,
   </em>
   <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#702" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 702</a></span> (1981), and the likelihood that drug dealers will attempt to dispose of drugs before police seize them, see,
   <em>
    e. g., Ker
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#28" aria-description="Citation for case: Ker v. California">374 U. S. 23, 28, n. 3</a></span> (1963).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b484-6">
   Although our decision in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   did not address this issue directly, it is instructive that in that case — which involved a felony drug investigation — we remanded to the state court for further factual development to determine whether the no-knock entry was reasonable under the circumstances of the case. Two
   <em>
    amicus
   </em>
   briefs in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>
   </em>
   suggested that we adopt just the sort of
   <em>
    per se
   </em>
   rule the Wisconsin court propounded here. Brief for Americans for Effective Law Enforcement, Inc., et al. as
   <em>
    Amici Curiae
   </em>
   10-11, Brief for Wayne County, Michigan, as
   <em>
    Amicus Curiae
   </em>
   39-46, in
   <em>
    Wilson
   </em>
   v.
   <em>
    Arkansas, O.
   </em>
   T. 1994, No. 5707. Although the respondent did not argue for a categorical rule, the petitioner, in her reply brief, did address the arguments put forward by the
   <em>
    dmicus
   </em>
   briefs, Reply Brief for Petitioner in
   <em>
    Wilson
   </em>
   v.
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span>,
   </em>
   O. T. 1994, No. 5707, p. 11, and
   <em>
    amici
   </em>
   supporting the petitioner also presented arguments against a categorical rule. Brief for American Civil Liberties Union et al. as
   <em>
    Amici Curiae
   </em>
   in
   <em>
    Wilson
   </em>
   v.
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span>,
   </em>
   O. T. 1994, No. 5707, p. 29, n. 44. Thus, while the prospect of a categorical rule was one to which we were alerted in
   <em>
    <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,
   </em>
   we did not choose to adopt such a rule at that time.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b484-9">
   It is always somewhat dangerous to ground exceptions to constitutional protections in the social norms of a given historical moment. The purpose of the Fourth Amendment’s requirement of reasonableness “is to preserve that degree of respect for the privacy of persons and the inviolability of their property that existed when the provision was adopted — even if a later, less virtuous age should become accustomed to considering all sorts of intrusion ‘reasonable.’”
   <em>
    Minnesota
   </em>
   v.
   <em>
    Dickerson,
   </em>
   <span class="citation" data-id="9432823"><a href="/opinion/112873/minnesota-v-dickerson/#380" aria-description="Citation for case: Minnesota v. Dickerson">508 U. S. 366, 380</a></span> (1993) (Scalia, J,, concurring).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b485-6">
   The State asserts that the intrusion on individual interests effectuated by a no-knock entry is minimal because the execution of the warrant itself constitutes the primary intrusion on individual privacy and that the individual privacy interest cannot outweigh the generalized governmental interest in effective and safe law enforcement. Brief for Respondent 21-24. See also Brief for United States as
   <em>
    Amicus Curiae
   </em>
   16 (“occupants’ privacy interest is necessarily limited to the brief interval between the officers’ announcement and their entry”). While it is true that a no-knoek entry is less intrusive than, for example, a warrantless search, the individual interests implicated by an unannounced, forcible entry should not be unduly minimized. As we observed in
   <em>
    Wilson
   </em>
   v.
   <em>
    Arkansas,
   </em>
   <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#930" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 930-932</a></span> (1995), the common law recognized that individuals should be provided the opportunity to comply with the law and to avoid the destruction of property occasioned by a forcible entry. These interests are not inconsequential.
  </p>
<p id="b485-7">
   Additionally, when police enter a residence without announcing their presence, the residents are not given any opportunity to prepare themselves for such an entry. The State pointed out at oral argument that, in Wisconsin, most search warrants are executed during the late night and early morning hours. Tr. of Oral Arg. 24. The brief interlude between announcement and entry with a warrant may be the opportunity that an individual has to pull on clothes or get out of bed.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b487-9">
   We note that the attorneys general of 26 States, the Commonwealth of Puerto Rico, and the Territory of Guam filed an
   <em>
    amicus
   </em>
   brief taking the position that the officers’ decision was reasonable under the specific facts of this ease, but rejecting Wisconsin’s
   <em>
    per se
   </em>
   rule. See Brief for Ohio et al. as
   <em>
    Amici Curiae.
   </em>
</p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b488-7">
   A number of States give magistrate judges the authority to issue “no-knoek” warrants if the officers demonstrate ahead of time a reasonable suspicion that entry without prior announcement will be appropriate in a particular context. See,
   <em>
    e. g.,
   </em>
   725 Ill. Comp. Stat., eh. 725, § 5/108-8 (1992); <span class="citation no-link">Neb. Rev. Stat. §29-411</span> (1995); Okla. Stat., Tit. 22, §1228 (Supp. 1997); S. D. Codified Laws §23A-35-9 (1988); <span class="citation no-link">Utah Code Ann. § 77-23-210</span> (1995). But see
   <em>
    State
   </em>
   v.
   <em>
    Arce,
   </em>
   <span class="citation" data-id="9529581"><a href="/opinion/1118987/state-v-arce/" aria-description="Citation for case: State v. Arce">83 Ore. App. 185</a></span>, <span class="citation" data-id="9529581"><a href="/opinion/1118987/state-v-arce/" aria-description="Citation for case: State v. Arce">730 P. 2d 1260</a></span> (1986) (magistrate has no authority to abrogate knock-and-announce requirement);
   <em>
    State
   </em>
   v.
   <em>
    Bamber,
   </em>
   <span class="citation" data-id="1124319"><a href="/opinion/1124319/state-v-bamber/" aria-description="Citation for case: State v. Bamber">630 So. 2d 1048</a></span> (Fla. 1994) (same).
  </p>
<p id="b488-8">
   The practice of allowing magistrates to issue no-knock warrants seems entirely reasonable when sufficient cause to do so can be demonstrated ahead of time. But, as the facts of this case demonstrate, a magistrate’s decision not to authorize a no-knoek entry should not be interpreted to remove the officers’ authority to exercise independent judgment concerning the wisdom of a no-knock entry at the time the warrant is being executed.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/Riley v. California.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Riley v. California"
type: case
citation: "134 S. Ct. 2473 (2014)"
parallel_cite: "189 L. Ed. 2d 430; 82 U.S.L.W. 4558"
neutral_cite: 2014 U.S. LEXIS 4497
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2014
date_decided: 2014-06-25
docket: 13-132
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2014-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Riley v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2680439/riley-v-cal-united-states/"
  cluster_id: 2680439
  opinion_id: 2680439
  identity_checked: true
homes:
  - page: "[[SIA Cell Phones]]"
    role: "Key — Anchor"
  - page: "[[Plain View Doctrine]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Robinson]]", "[[Chimel v. California]]", "[[Arizona v. Gant]]", "[[Carpenter v. United States]]", "[[People v. Hughes]]"]
aliases: ["Riley v. California (2014)", "United States v. Wurie"]
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "cell-phone", "digital-search", "warrant-requirement"]
holding: "The Robinson bright-line search-incident rule does NOT extend to the digital contents of a cell phone seized incident to arrest.…"
lake:
  record_id: Riley v. California
  status: under_review
  projected_at: 2026-07-09
---

# Riley v. California

*573 U.S. 373 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In two consolidated cases, police searched the digital contents of arrestees' cell phones without a warrant, as [[Search Incident to Arrest|searches incident to arrest]]. After arresting Riley on weapons charges, an officer searched his smart phone and found photos, videos, and contacts linking him to a gang shooting. In the companion *Wurie* case, officers searched a flip phone's call log.

## Issue
Whether police may, without a warrant, search the digital contents of a cell phone seized from an individual incident to arrest.

## Rule
A warrant is generally required. "Our answer to the question of what police must do before searching a cell phone seized incident to an arrest is accordingly simple — get a warrant." — *Riley v. California*, 573 U.S. at 403. ^pin-403

The categorical search-incident-to-arrest authority of *[[United States v. Robinson]]* does not extend to the vast store of digital data on a modern cell phone: the officer-safety and evidence-preservation rationales of *[[Chimel v. California|Chimel]]* do not justify searching data, and cell phones implicate privacy interests far greater than any physical item.

## Application
The data on Riley's smart phone and on Wurie's flip phone was searched without a warrant as a [[Search Incident to Arrest|search incident to arrest]]. Because digital data cannot harm an arresting officer, and any risk of remote wiping or encryption can be addressed by other means (such as turning the phone off or removing its battery), the *[[Chimel v. California|Chimel]]* justifications were absent; and the immense quantity and sensitivity of the information on a phone made the intrusion incomparable to inspecting physical items. The warrantless searches of the phones' contents therefore could not be justified as [[Search Incident to Arrest|searches incident to arrest]].

## Conclusion
Officers must generally obtain a warrant before searching a cell phone seized incident to arrest; the Court reversed in *Riley* and affirmed the suppression in *Wurie*.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Riley* cabins the [[Common Legal Terms#bright-line-rule|bright-line rule]] of [[United States v. Robinson]] for digital data and anchors the digital-privacy reasoning later extended in [[Carpenter v. United States]].

## Appears on
- [[SIA Cell Phones]] — *Key — Anchor*
- [[Plain View Doctrine]] — *Related (cross-doctrine)*

## Sources
- *Riley v. California*, 573 U.S. 373 (2014) — https://www.courtlistener.com/opinion/2680439/riley-v-cal-united-states/ — pinpoint: 403 (CL carries an unpaginated case-text import; pinpoint per the U.S. Reports).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ff3188c21ac1d10a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Riley v. California"}, "payload": {"all": [{"cite": "134 S. Ct. 2473", "page": "2473", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "134"}, {"cite": "189 L. Ed. 2d 430", "page": "430", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "189"}, {"cite": "2014 U.S. LEXIS 4497", "page": "4497", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2014"}, {"cite": "82 U.S.L.W. 4558", "page": "4558", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "82"}], "display": "134 S. Ct. 2473", "official": {"cite": "134 S. Ct. 2473", "page": "2473", "reporter": "S. Ct.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "134"}, "official_selection_present": true, "record_id": "Riley v. California"}}
{"assertion_id": "594a6336b674db17", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-403", "record_id": "Riley v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-403", "pinpoint_status": "slip-only", "quote": "--- # Riley v. California *573 U.S. 373 (2014)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In two consolidated cases, police searched the digital contents of arrestees' cell phones without a warrant, as searches incident to arrest. After arresting Riley on weapons charges, an officer searched his smart phone and found photos, videos, and contacts linking him to a gang shooting. In the companion *Wurie* case, officers searched a flip phone's call log. ## Issue Whether police may, without a warrant, search the digital contents of a cell phone seized from an individual incident to arrest. ## Rule A warrant is generally required.", "quote_fidelity": "mismatch", "record_id": "Riley v. California", "star_marker": null}}
{"assertion_id": "1965e891303ceba7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Riley v. California"}, "payload": {"as_of_content": "2014-06-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Riley v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Riley v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Riley v. California",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Riley v. California",
    "case_name_short": "Riley",
    "case_name_full": "David Leon RILEY v. CALIFORNIA.",
    "input_case_name": "Riley v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2014-06-25",
    "year": 2014,
    "docket": "13-132",
    "cluster_id": 2680439,
    "lead_opinion_id": 2680439,
    "sibling_ids": [
      2680439
    ],
    "absolute_url": "/opinion/2680439/riley-v-cal-united-states/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8414700,
        "score": 20,
        "case_name": "Riley v. California"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "134 S. Ct. 2473",
      "volume": "134",
      "reporter": "S. Ct.",
      "page": "2473",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "189 L. Ed. 2d 430",
        "volume": "189",
        "reporter": "L. Ed. 2d",
        "page": "430",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4558",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2014 U.S. LEXIS 4497",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "4497",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "134 S. Ct. 2473",
        "volume": "134",
        "reporter": "S. Ct.",
        "page": "2473",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "189 L. Ed. 2d 430",
        "volume": "189",
        "reporter": "L. Ed. 2d",
        "page": "430",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2014 U.S. LEXIS 4497",
        "volume": "2014",
        "reporter": "U.S. LEXIS",
        "page": "4497",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "82 U.S.L.W. 4558",
        "volume": "82",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "134 S. Ct. 2473",
    "official_selection": {
      "court_class": "scotus",
      "selected": "134 S. Ct. 2473",
      "reason": "selected_rank_2"
    }
  },
  "pinpoints": [
    {
      "id": "pin-403",
      "page": null,
      "quote": "--- # Riley v. California *573 U.S. 373 (2014)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In two consolidated cases, police searched the digital contents of arrestees' cell phones without a warrant, as searches incident to arrest. After arresting Riley on weapons charges, an officer searched his smart phone and found photos, videos, and contacts linking him to a gang shooting. In the companion *Wurie* case, officers searched a flip phone's call log. ## Issue Whether police may, without a warrant, search the digital contents of a cell phone seized from an individual incident to arrest. ## Rule A warrant is generally required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2014-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Riley v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(8386852) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(8386852)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(8386852)",
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
    "complete_query": "cites:(8386852)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 8386852,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/riley-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T17:33:55Z",
    "date_modified": "2026-07-09T05:52:51Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law",
      "panel cluster re-key -> cluster 2680439 (evidence: batch-11 catch #5; phase-a cache verification (merits cluster 2680439 vs SG-order 8416508))"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:35:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:35:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:35:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:35:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Riley v. California

```
(Slip Opinion)              OCTOBER TERM, 2013                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                         RILEY v. CALIFORNIA

    CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA,

        FOURTH APPELLATE DISTRICT, DIVISION ONE


      No. 13–132.      Argued April 29, 2014—Decided June 25, 2014*
In No. 13–132, petitioner Riley was stopped for a traffic violation,
  which eventually led to his arrest on weapons charges. An officer
  searching Riley incident to the arrest seized a cell phone from Riley’s
  pants pocket. The officer accessed information on the phone and no-
  ticed the repeated use of a term associated with a street gang. At the
  police station two hours later, a detective specializing in gangs fur-
  ther examined the phone’s digital contents. Based in part on photo-
  graphs and videos that the detective found, the State charged Riley
  in connection with a shooting that had occurred a few weeks earlier
  and sought an enhanced sentence based on Riley’s gang membership.
  Riley moved to suppress all evidence that the police had obtained
  from his cell phone. The trial court denied the motion, and Riley was
  convicted. The California Court of Appeal affirmed.
     In No. 13–212, respondent Wurie was arrested after police ob-
  served him participate in an apparent drug sale. At the police sta-
  tion, the officers seized a cell phone from Wurie’s person and noticed
  that the phone was receiving multiple calls from a source identified
  as “my house” on its external screen. The officers opened the phone,
  accessed its call log, determined the number associated with the “my
  house” label, and traced that number to what they suspected was
  Wurie’s apartment. They secured a search warrant and found drugs,
  a firearm and ammunition, and cash in the ensuing search. Wurie
  was then charged with drug and firearm offenses. He moved to sup-
  press the evidence obtained from the search of the apartment. The
  District Court denied the motion, and Wurie was convicted. The
——————
  * Together with No. 13–212, United States v. Wurie, on certiorari to
the United States Court of Appeals for the First Circuit.
2                        RILEY v. CALIFORNIA

                                 Syllabus

    First Circuit reversed the denial of the motion to suppress and vacat-
    ed the relevant convictions.
Held: The police generally may not, without a warrant, search digital
 information on a cell phone seized from an individual who has been
 arrested. Pp. 5–28.
    (a) A warrantless search is reasonable only if it falls within a spe-
 cific exception to the Fourth Amendment’s warrant requirement. See
 Kentucky v. King, 563 U. S. ___, ___. The well-established exception
 at issue here applies when a warrantless search is conducted incident
 to a lawful arrest.
    Three related precedents govern the extent to which officers may
 search property found on or near an arrestee. Chimel v. California,
 395 U. S. 752, requires that a search incident to arrest be limited to
 the area within the arrestee’s immediate control, where it is justified
 by the interests in officer safety and in preventing evidence destruc-
 tion. In United States v. Robinson, 414 U. S. 218, the Court applied
 the Chimel analysis to a search of a cigarette pack found on the ar-
 restee’s person. It held that the risks identified in Chimel are pre-
 sent in all custodial arrests, 414 U. S., at 235, even when there is no
 specific concern about the loss of evidence or the threat to officers in a
 particular case, id., at 236. The trilogy concludes with Arizona v.
 Gant, 556 U. S. 332, which permits searches of a car where the ar-
 restee is unsecured and within reaching distance of the passenger
 compartment, or where it is reasonable to believe that evidence of the
 crime of arrest might be found in the vehicle, id., at 343. Pp. 5–8.
    (b) The Court declines to extend Robinson’s categorical rule to
 searches of data stored on cell phones. Absent more precise guidance
 from the founding era, the Court generally determines whether to ex-
 empt a given type of search from the warrant requirement “by as-
 sessing, on the one hand, the degree to which it intrudes upon an in-
 dividual’s privacy and, on the other, the degree to which it is needed
 for the promotion of legitimate governmental interests.” Wyoming v.
 Houghton, 526 U. S. 295, 300. That balance of interests supported
 the search incident to arrest exception in Robinson. But a search of
 digital information on a cell phone does not further the government
 interests identified in Chimel, and implicates substantially greater
 individual privacy interests than a brief physical search. Pp. 8–22.
      (1) The digital data stored on cell phones does not present either
 Chimel risk. Pp. 10–15.
         (i) Digital data stored on a cell phone cannot itself be used as a
 weapon to harm an arresting officer or to effectuate the arrestee’s es-
 cape. Officers may examine the phone’s physical aspects to ensure
 that it will not be used as a weapon, but the data on the phone can
 endanger no one. To the extent that a search of cell phone data
                   Cite as: 573 U. S. ____ (2014)                    3

                              Syllabus

might warn officers of an impending danger, e.g., that the arrestee’s
confederates are headed to the scene, such a concern is better ad-
dressed through consideration of case-specific exceptions to the war-
rant requirement, such as exigent circumstances. See, e.g., Warden,
Md. Penitentiary v. Hayden, 387 U. S. 294, 298–299. Pp. 10–12.
       (ii) The United States and California raise concerns about the
destruction of evidence, arguing that, even if the cell phone is physi-
cally secure, information on the cell phone remains vulnerable to re-
mote wiping and data encryption. As an initial matter, those broad
concerns are distinct from Chimel’s focus on a defendant who re-
sponds to arrest by trying to conceal or destroy evidence within his
reach. The briefing also gives little indication that either problem is
prevalent or that the opportunity to perform a search incident to ar-
rest would be an effective solution. And, at least as to remote wiping,
law enforcement currently has some technologies of its own for com-
batting the loss of evidence. Finally, law enforcement’s remaining
concerns in a particular case might be addressed by responding in a
targeted manner to urgent threats of remote wiping, see Missouri v.
McNeely, 569 U. S. ___, ___, or by taking action to disable a phone’s
locking mechanism in order to secure the scene, see Illinois v. McAr-
thur, 531 U. S. 326, 331–333. Pp. 12–15.
     (2) A conclusion that inspecting the contents of an arrestee’s
pockets works no substantial additional intrusion on privacy beyond
the arrest itself may make sense as applied to physical items, but
more substantial privacy interests are at stake when digital data is
involved. Pp. 15–22.
       (i) Cell phones differ in both a quantitative and a qualitative
sense from other objects that might be carried on an arrestee’s per-
son. Notably, modern cell phones have an immense storage capacity.
Before cell phones, a search of a person was limited by physical reali-
ties and generally constituted only a narrow intrusion on privacy.
But cell phones can store millions of pages of text, thousands of pic-
tures, or hundreds of videos. This has several interrelated privacy
consequences. First, a cell phone collects in one place many distinct
types of information that reveal much more in combination than any
isolated record. Second, the phone’s capacity allows even just one
type of information to convey far more than previously possible.
Third, data on the phone can date back for years. In addition, an el-
ement of pervasiveness characterizes cell phones but not physical
records. A decade ago officers might have occasionally stumbled
across a highly personal item such as a diary, but today many of the
more than 90% of American adults who own cell phones keep on their
person a digital record of nearly every aspect of their lives. Pp. 17–
21.
4                         RILEY v. CALIFORNIA

                                  Syllabus

            (ii) The scope of the privacy interests at stake is further com-
    plicated by the fact that the data viewed on many modern cell phones
    may in fact be stored on a remote server. Thus, a search may extend
    well beyond papers and effects in the physical proximity of an ar-
    restee, a concern that the United States recognizes but cannot defini-
    tively foreclose. Pp. 21–22.
       (c) Fallback options offered by the United States and California are
    flawed and contravene this Court’s general preference to provide
    clear guidance to law enforcement through categorical rules. See
    Michigan v. Summers, 452 U. S. 692, 705, n. 19. One possible rule is
    to import the Gant standard from the vehicle context and allow a
    warrantless search of an arrestee’s cell phone whenever it is reason-
    able to believe that the phone contains evidence of the crime of ar-
    rest. That proposal is not appropriate in this context, and would
    prove no practical limit at all when it comes to cell phone searches.
    Another possible rule is to restrict the scope of a cell phone search to
    information relevant to the crime, the arrestee’s identity, or officer
    safety. That proposal would again impose few meaningful con-
    straints on officers. Finally, California suggests an analogue rule,
    under which officers could search cell phone data if they could have
    obtained the same information from a pre-digital counterpart. That
    proposal would allow law enforcement to search a broad range of
    items contained on a phone even though people would be unlikely to
    carry such a variety of information in physical form, and would
    launch courts on a difficult line-drawing expedition to determine
    which digital files are comparable to physical records. Pp. 22–25.
       (d) It is true that this decision will have some impact on the ability
    of law enforcement to combat crime. But the Court’s holding is not
    that the information on a cell phone is immune from search; it is that
    a warrant is generally required before a search. The warrant re-
    quirement is an important component of the Court’s Fourth Amend-
    ment jurisprudence, and warrants may be obtained with increasing
    efficiency. In addition, although the search incident to arrest excep-
    tion does not apply to cell phones, the continued availability of the ex-
    igent circumstances exception may give law enforcement a justifica-
    tion for a warrantless search in particular cases. Pp. 25–27.
No. 13–132, reversed and remanded; No. 13–212, 728 F. 3d 1, affirmed.

   ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, THOMAS, GINSBURG, BREYER, SOTOMAYOR, and KAGAN, JJ.,
joined. ALITO, J., filed an opinion concurring in part and concurring in
the judgment.
                        Cite as: 573 U. S. ____ (2014)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                           Nos. 13–132 and 13–212
                                   _________________


              DAVID LEON RILEY, PETITIONER
13–132                     v.
                      CALIFORNIA
ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF CALI-
  FORNIA, FOURTH APPELLATE DISTRICT, DIVISION ONE


                UNITED STATES, PETITIONER
13–212                     v.
                      BRIMA WURIE
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

             APPEALS FOR THE FIRST CIRCUIT

                                 [June 25, 2014]


  CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
  These two cases raise a common question: whether the
police may, without a warrant, search digital information
on a cell phone seized from an individual who has been
arrested.
                                I

                                A

   In the first case, petitioner David Riley was stopped by a
police officer for driving with expired registration tags. In
the course of the stop, the officer also learned that Riley’s
license had been suspended. The officer impounded Ri-
ley’s car, pursuant to department policy, and another
2                   RILEY v. CALIFORNIA

                     Opinion of the Court

officer conducted an inventory search of the car. Riley was
arrested for possession of concealed and loaded firearms
when that search turned up two handguns under the car’s
hood. See Cal. Penal Code Ann. §§12025(a)(1), 12031(a)(1)
(West 2009).
   An officer searched Riley incident to the arrest and
found items associated with the “Bloods” street gang. He
also seized a cell phone from Riley’s pants pocket. Accord-
ing to Riley’s uncontradicted assertion, the phone was a
“smart phone,” a cell phone with a broad range of other
functions based on advanced computing capability, large
storage capacity, and Internet connectivity. The officer
accessed information on the phone and noticed that some
words (presumably in text messages or a contacts list)
were preceded by the letters “CK”—a label that, he be-
lieved, stood for “Crip Killers,” a slang term for members
of the Bloods gang.
   At the police station about two hours after the arrest, a
detective specializing in gangs further examined the con-
tents of the phone. The detective testified that he “went
through” Riley’s phone “looking for evidence, because . . .
gang members will often video themselves with guns or
take pictures of themselves with the guns.” App. in No.
13–132, p. 20. Although there was “a lot of stuff ” on the
phone, particular files that “caught [the detective’s] eye”
included videos of young men sparring while someone
yelled encouragement using the moniker “Blood.” Id., at
11–13. The police also found photographs of Riley stand-
ing in front of a car they suspected had been involved in a
shooting a few weeks earlier.
   Riley was ultimately charged, in connection with that
earlier shooting, with firing at an occupied vehicle, assault
with a semiautomatic firearm, and attempted murder.
The State alleged that Riley had committed those crimes
for the benefit of a criminal street gang, an aggravating
factor that carries an enhanced sentence. Compare Cal.
                 Cite as: 573 U. S. ____ (2014)           3

                     Opinion of the Court

Penal Code Ann. §246 (2008) with §186.22(b)(4)(B) (2014).
Prior to trial, Riley moved to suppress all evidence that
the police had obtained from his cell phone. He contended
that the searches of his phone violated the Fourth
Amendment, because they had been performed without a
warrant and were not otherwise justified by exigent cir-
cumstances. The trial court rejected that argument. App.
in No. 13–132, at 24, 26. At Riley’s trial, police officers
testified about the photographs and videos found on the
phone, and some of the photographs were admitted into
evidence. Riley was convicted on all three counts and
received an enhanced sentence of 15 years to life in prison.
  The California Court of Appeal affirmed. No. D059840
(Cal. App., Feb. 8, 2013), App. to Pet. for Cert. in No. 13–
132, pp. 1a–23a. The court relied on the California Su-
preme Court’s decision in People v. Diaz, 51 Cal. 4th 84,
244 P. 3d 501 (2011), which held that the Fourth Amend-
ment permits a warrantless search of cell phone data
incident to an arrest, so long as the cell phone was imme-
diately associated with the arrestee’s person. See id., at
93, 244 P. 3d, at 505–506.
  The California Supreme Court denied Riley’s petition for
review, App. to Pet. for Cert. in No. 13–132, at 24a, and we
granted certiorari, 571 U. S. ___ (2014).
                             B
  In the second case, a police officer performing routine
surveillance observed respondent Brima Wurie make an
apparent drug sale from a car. Officers subsequently
arrested Wurie and took him to the police station. At the
station, the officers seized two cell phones from Wurie’s
person. The one at issue here was a “flip phone,” a kind of
phone that is flipped open for use and that generally has a
smaller range of features than a smart phone. Five to ten
minutes after arriving at the station, the officers noticed
that the phone was repeatedly receiving calls from a
4                  RILEY v. CALIFORNIA

                     Opinion of the Court

source identified as “my house” on the phone’s external
screen. A few minutes later, they opened the phone and
saw a photograph of a woman and a baby set as the
phone’s wallpaper. They pressed one button on the phone
to access its call log, then another button to determine the
phone number associated with the “my house” label. They
next used an online phone directory to trace that phone
number to an apartment building.
   When the officers went to the building, they saw Wurie’s
name on a mailbox and observed through a window a
woman who resembled the woman in the photograph on
Wurie’s phone. They secured the apartment while obtain-
ing a search warrant and, upon later executing the war-
rant, found and seized 215 grams of crack cocaine, mari-
juana, drug paraphernalia, a firearm and ammunition, and
cash.
   Wurie was charged with distributing crack cocaine,
possessing crack cocaine with intent to distribute, and
being a felon in possession of a firearm and ammunition.
See 18 U. S. C. §922(g); 21 U. S. C. §841(a). He moved to
suppress the evidence obtained from the search of the
apartment, arguing that it was the fruit of an unconstitu-
tional search of his cell phone. The District Court denied
the motion. 612 F. Supp. 2d 104 (Mass. 2009). Wurie was
convicted on all three counts and sentenced to 262 months
in prison.
   A divided panel of the First Circuit reversed the denial
of Wurie’s motion to suppress and vacated Wurie’s convic-
tions for possession with intent to distribute and posses-
sion of a firearm as a felon. 728 F. 3d 1 (2013). The court
held that cell phones are distinct from other physical
possessions that may be searched incident to arrest with-
out a warrant, because of the amount of personal data cell
phones contain and the negligible threat they pose to law
enforcement interests. See id., at 8–11.
   We granted certiorari. 571 U. S. ___ (2014).
                  Cite as: 573 U. S. ____ (2014)            5

                      Opinion of the Court

                        II
  The Fourth Amendment provides:
      “The right of the people to be secure in their per-
    sons, houses, papers, and effects, against unreasona-
    ble searches and seizures, shall not be violated, and
    no Warrants shall issue, but upon probable cause,
    supported by Oath or affirmation, and particularly
    describing the place to be searched, and the persons or
    things to be seized.”
   As the text makes clear, “the ultimate touchstone of the
Fourth Amendment is ‘reasonableness.’ ” Brigham City v.
Stuart, 547 U. S. 398, 403 (2006). Our cases have deter-
mined that “[w]here a search is undertaken by law en-
forcement officials to discover evidence of criminal wrong-
doing, . . . reasonableness generally requires the obtaining
of a judicial warrant.” Vernonia School Dist. 47J v. Acton,
515 U. S. 646, 653 (1995). Such a warrant ensures that
the inferences to support a search are “drawn by a neutral
and detached magistrate instead of being judged by the
officer engaged in the often competitive enterprise of
ferreting out crime.” Johnson v. United States, 333 U. S.
10, 14 (1948). In the absence of a warrant, a search is
reasonable only if it falls within a specific exception to the
warrant requirement. See Kentucky v. King, 563 U. S.
___, ___ (2011) (slip op., at 5–6).
   The two cases before us concern the reasonableness of a
warrantless search incident to a lawful arrest. In 1914,
this Court first acknowledged in dictum “the right on the
part of the Government, always recognized under English
and American law, to search the person of the accused
when legally arrested to discover and seize the fruits or
evidences of crime.” Weeks v. United States, 232 U. S. 383,
392. Since that time, it has been well accepted that such a
search constitutes an exception to the warrant require-
ment. Indeed, the label “exception” is something of a
6                   RILEY v. CALIFORNIA

                     Opinion of the Court

misnomer in this context, as warrantless searches incident
to arrest occur with far greater frequency than searches
conducted pursuant to a warrant. See 3 W. LaFave,
Search and Seizure §5.2(b), p. 132, and n. 15 (5th ed.
2012).
  Although the existence of the exception for such searches
has been recognized for a century, its scope has been de-
bated for nearly as long. See Arizona v. Gant, 556 U. S.
332, 350 (2009) (noting the exception’s “checkered his-
tory”). That debate has focused on the extent to which
officers may search property found on or near the arrestee.
Three related precedents set forth the rules governing
such searches:
  The first, Chimel v. California, 395 U. S. 752 (1969), laid
the groundwork for most of the existing search incident to
arrest doctrine. Police officers in that case arrested
Chimel inside his home and proceeded to search his entire
three-bedroom house, including the attic and garage. In
particular rooms, they also looked through the contents of
drawers. Id., at 753–754.
   The Court crafted the following rule for assessing the
reasonableness of a search incident to arrest:
    “When an arrest is made, it is reasonable for the ar-
    resting officer to search the person arrested in order
    to remove any weapons that the latter might seek to
    use in order to resist arrest or effect his escape. Oth-
    erwise, the officer’s safety might well be endangered,
    and the arrest itself frustrated. In addition, it is en-
    tirely reasonable for the arresting officer to search for
    and seize any evidence on the arrestee’s person in or-
    der to prevent its concealment or destruction. . . .
    There is ample justification, therefore, for a search of
    the arrestee’s person and the area ‘within his immedi-
    ate control’—construing that phrase to mean the area
    from within which he might gain possession of a
                 Cite as: 573 U. S. ____ (2014)            7

                     Opinion of the Court

    weapon or destructible evidence.” Id., at 762–763.
The extensive warrantless search of Chimel’s home did not
fit within this exception, because it was not needed to
protect officer safety or to preserve evidence. Id., at 763,
768.
   Four years later, in United States v. Robinson, 414 U. S.
218 (1973), the Court applied the Chimel analysis in the
context of a search of the arrestee’s person. A police of-
ficer had arrested Robinson for driving with a revoked
license. The officer conducted a patdown search and felt
an object that he could not identify in Robinson’s coat
pocket. He removed the object, which turned out to be a
crumpled cigarette package, and opened it. Inside were 14
capsules of heroin. Id., at 220, 223.
   The Court of Appeals concluded that the search was
unreasonable because Robinson was unlikely to have
evidence of the crime of arrest on his person, and because
it believed that extracting the cigarette package and open-
ing it could not be justified as part of a protective search
for weapons. This Court reversed, rejecting the notion
that “case-by-case adjudication” was required to determine
“whether or not there was present one of the reasons
supporting the authority for a search of the person inci-
dent to a lawful arrest.” Id., at 235. As the Court ex-
plained, “[t]he authority to search the person incident to a
lawful custodial arrest, while based upon the need to
disarm and to discover evidence, does not depend on what
a court may later decide was the probability in a particu-
lar arrest situation that weapons or evidence would in fact
be found upon the person of the suspect.” Ibid. Instead, a
“custodial arrest of a suspect based on probable cause is a
reasonable intrusion under the Fourth Amendment; that
intrusion being lawful, a search incident to the arrest
requires no additional justification.” Ibid.
   The Court thus concluded that the search of Robinson
8                    RILEY v. CALIFORNIA

                      Opinion of the Court

was reasonable even though there was no concern about
the loss of evidence, and the arresting officer had no spe-
cific concern that Robinson might be armed. Id., at 236.
In doing so, the Court did not draw a line between a
search of Robinson’s person and a further examination of
the cigarette pack found during that search. It merely
noted that, “[h]aving in the course of a lawful search come
upon the crumpled package of cigarettes, [the officer] was
entitled to inspect it.” Ibid. A few years later, the Court
clarified that this exception was limited to “personal prop-
erty . . . immediately associated with the person of the
arrestee.” United States v. Chadwick, 433 U. S. 1, 15
(1977) (200-pound, locked footlocker could not be searched
incident to arrest), abrogated on other grounds by Califor-
nia v. Acevedo, 500 U. S. 565 (1991).
   The search incident to arrest trilogy concludes with
Gant, which analyzed searches of an arrestee’s vehicle.
Gant, like Robinson, recognized that the Chimel concerns
for officer safety and evidence preservation underlie the
search incident to arrest exception. See 556 U. S., at 338.
As a result, the Court concluded that Chimel could author-
ize police to search a vehicle “only when the arrestee is
unsecured and within reaching distance of the passenger
compartment at the time of the search.” 556 U. S., at 343.
Gant added, however, an independent exception for a
warrantless search of a vehicle’s passenger compartment
“when it is ‘reasonable to believe evidence relevant to the
crime of arrest might be found in the vehicle.’ ” Ibid.
(quoting Thornton v. United States, 541 U. S. 615, 632
(2004) (SCALIA, J., concurring in judgment)). That excep-
tion stems not from Chimel, the Court explained, but from
“circumstances unique to the vehicle context.” 556 U. S.,
at 343.
                              III
    These cases require us to decide how the search incident
                 Cite as: 573 U. S. ____ (2014)            9

                     Opinion of the Court

to arrest doctrine applies to modern cell phones, which are
now such a pervasive and insistent part of daily life that
the proverbial visitor from Mars might conclude they were
an important feature of human anatomy. A smart phone
of the sort taken from Riley was unheard of ten years ago;
a significant majority of American adults now own such
phones. See A. Smith, Pew Research Center, Smartphone
Ownership—2013 Update (June 5, 2013). Even less so-
phisticated phones like Wurie’s, which have already faded
in popularity since Wurie was arrested in 2007, have been
around for less than 15 years. Both phones are based on
technology nearly inconceivable just a few decades ago,
when Chimel and Robinson were decided.
   Absent more precise guidance from the founding era, we
generally determine whether to exempt a given type of
search from the warrant requirement “by assessing, on the
one hand, the degree to which it intrudes upon an individ-
ual’s privacy and, on the other, the degree to which it is
needed for the promotion of legitimate governmental
interests.” Wyoming v. Houghton, 526 U. S. 295, 300
(1999). Such a balancing of interests supported the search
incident to arrest exception in Robinson, and a mechanical
application of Robinson might well support the warrant-
less searches at issue here.
   But while Robinson’s categorical rule strikes the appro-
priate balance in the context of physical objects, neither of
its rationales has much force with respect to digital con-
tent on cell phones. On the government interest side,
Robinson concluded that the two risks identified in
Chimel—harm to officers and destruction of evidence—are
present in all custodial arrests. There are no comparable
risks when the search is of digital data. In addition, Rob-
inson regarded any privacy interests retained by an indi-
vidual after arrest as significantly diminished by the fact
of the arrest itself. Cell phones, however, place vast quan-
tities of personal information literally in the hands of
10                  RILEY v. CALIFORNIA

                     Opinion of the Court

individuals. A search of the information on a cell phone
bears little resemblance to the type of brief physical search
considered in Robinson.
  We therefore decline to extend Robinson to searches of
data on cell phones, and hold instead that officers must
generally secure a warrant before conducting such a
search.
                               A
   We first consider each Chimel concern in turn. In doing
so, we do not overlook Robinson’s admonition that searches
of a person incident to arrest, “while based upon the
need to disarm and to discover evidence,” are reasonable
regardless of “the probability in a particular arrest situa-
tion that weapons or evidence would in fact be found.” 414
U. S., at 235. Rather than requiring the “case-by-case
adjudication” that Robinson rejected, ibid., we ask instead
whether application of the search incident to arrest doc-
trine to this particular category of effects would “untether
the rule from the justifications underlying the Chimel
exception,” Gant, supra, at 343. See also Knowles v. Iowa,
525 U. S. 113, 119 (1998) (declining to extend Robinson to
the issuance of citations, “a situation where the concern
for officer safety is not present to the same extent and the
concern for destruction or loss of evidence is not present at
all”).
                              1
   Digital data stored on a cell phone cannot itself be used
as a weapon to harm an arresting officer or to effectuate
the arrestee’s escape. Law enforcement officers remain
free to examine the physical aspects of a phone to ensure
that it will not be used as a weapon—say, to determine
whether there is a razor blade hidden between the phone
and its case. Once an officer has secured a phone and
eliminated any potential physical threats, however, data
                  Cite as: 573 U. S. ____ (2014)           11

                      Opinion of the Court

on the phone can endanger no one.
   Perhaps the same might have been said of the cigarette
pack seized from Robinson’s pocket. Once an officer
gained control of the pack, it was unlikely that Robinson
could have accessed the pack’s contents. But unknown
physical objects may always pose risks, no matter how
slight, during the tense atmosphere of a custodial arrest.
The officer in Robinson testified that he could not identify
the objects in the cigarette pack but knew they were not
cigarettes. See 414 U. S., at 223, 236, n. 7. Given that, a
further search was a reasonable protective measure. No
such unknowns exist with respect to digital data. As the
First Circuit explained, the officers who searched Wurie’s
cell phone “knew exactly what they would find therein:
data. They also knew that the data could not harm them.”
728 F. 3d, at 10.
   The United States and California both suggest that a
search of cell phone data might help ensure officer safety
in more indirect ways, for example by alerting officers that
confederates of the arrestee are headed to the scene.
There is undoubtedly a strong government interest in
warning officers about such possibilities, but neither the
United States nor California offers evidence to suggest
that their concerns are based on actual experience. The
proposed consideration would also represent a broadening
of Chimel’s concern that an arrestee himself might grab a
weapon and use it against an officer “to resist arrest or
effect his escape.” 395 U. S., at 763. And any such threats
from outside the arrest scene do not “lurk[ ] in all custodial
arrests.” Chadwick, 433 U. S., at 14–15. Accordingly, the
interest in protecting officer safety does not justify dis-
pensing with the warrant requirement across the board.
To the extent dangers to arresting officers may be impli-
cated in a particular way in a particular case, they are
better addressed through consideration of case-specific
exceptions to the warrant requirement, such as the one for
12                 RILEY v. CALIFORNIA

                     Opinion of the Court

exigent circumstances. See, e.g., Warden, Md. Peniten-
tiary v. Hayden, 387 U. S. 294, 298–299 (1967) (“The
Fourth Amendment does not require police officers to
delay in the course of an investigation if to do so would
gravely endanger their lives or the lives of others.”).
                              2
   The United States and California focus primarily on the
second Chimel rationale: preventing the destruction of
evidence.
   Both Riley and Wurie concede that officers could have
seized and secured their cell phones to prevent destruction
of evidence while seeking a warrant. See Brief for Peti-
tioner in No. 13–132, p. 20; Brief for Respondent in No.
13–212, p. 41. That is a sensible concession. See Illinois
v. McArthur, 531 U. S. 326, 331–333 (2001); Chadwick,
supra, at 13, and n. 8. And once law enforcement officers
have secured a cell phone, there is no longer any risk that
the arrestee himself will be able to delete incriminating
data from the phone.
   The United States and California argue that infor-
mation on a cell phone may nevertheless be vulnerable to
two types of evidence destruction unique to digital data—
remote wiping and data encryption. Remote wiping occurs
when a phone, connected to a wireless network, receives a
signal that erases stored data. This can happen when a
third party sends a remote signal or when a phone is
preprogrammed to delete data upon entering or leaving
certain geographic areas (so-called “geofencing”). See
Dept. of Commerce, National Institute of Standards and
Technology, R. Ayers, S. Brothers, & W. Jansen, Guide-
lines on Mobile Device Forensics (Draft) 29, 31 (SP 800–
101 Rev. 1, Sept. 2013) (hereinafter Ayers). Encryption is
a security feature that some modern cell phones use in
addition to password protection. When such phones lock,
data becomes protected by sophisticated encryption that
                 Cite as: 573 U. S. ____ (2014)           13

                     Opinion of the Court

renders a phone all but “unbreakable” unless police know
the password. Brief for United States as Amicus Curiae in
No. 13–132, p. 11.
   As an initial matter, these broader concerns about the
loss of evidence are distinct from Chimel’s focus on a
defendant who responds to arrest by trying to conceal or
destroy evidence within his reach. See 395 U. S., at 763–
764. With respect to remote wiping, the Government’s
primary concern turns on the actions of third parties who
are not present at the scene of arrest. And data encryp-
tion is even further afield. There, the Government focuses
on the ordinary operation of a phone’s security features,
apart from any active attempt by a defendant or his asso-
ciates to conceal or destroy evidence upon arrest.
   We have also been given little reason to believe that
either problem is prevalent. The briefing reveals only a
couple of anecdotal examples of remote wiping triggered
by an arrest. See Brief for Association of State Criminal
Investigative Agencies et al. as Amici Curiae in No. 13–
132, pp. 9–10; see also Tr. of Oral Arg. in No. 13–132,
p. 48. Similarly, the opportunities for officers to search a
password-protected phone before data becomes encrypted
are quite limited. Law enforcement officers are very
unlikely to come upon such a phone in an unlocked state
because most phones lock at the touch of a button or, as a
default, after some very short period of inactivity. See,
e.g., iPhone User Guide for iOS 7.1 Software 10 (2014)
(default lock after about one minute). This may explain
why the encryption argument was not made until the
merits stage in this Court, and has never been considered
by the Courts of Appeals.
   Moreover, in situations in which an arrest might trigger
a remote-wipe attempt or an officer discovers an unlocked
phone, it is not clear that the ability to conduct a warrant-
less search would make much of a difference. The need to
effect the arrest, secure the scene, and tend to other press-
14                 RILEY v. CALIFORNIA

                     Opinion of the Court

ing matters means that law enforcement officers may well
not be able to turn their attention to a cell phone right
away. See Tr. of Oral Arg. in No. 13–132, at 50; see also
Brief for United States as Amicus Curiae in No. 13–132, at
19. Cell phone data would be vulnerable to remote wiping
from the time an individual anticipates arrest to the time
any eventual search of the phone is completed, which
might be at the station house hours later. Likewise, an
officer who seizes a phone in an unlocked state might not
be able to begin his search in the short time remaining
before the phone locks and data becomes encrypted.
   In any event, as to remote wiping, law enforcement is
not without specific means to address the threat. Remote
wiping can be fully prevented by disconnecting a phone
from the network. There are at least two simple ways to
do this: First, law enforcement officers can turn the phone
off or remove its battery. Second, if they are concerned
about encryption or other potential problems, they can
leave a phone powered on and place it in an enclosure that
isolates the phone from radio waves. See Ayers 30–31.
Such devices are commonly called “Faraday bags,” after
the English scientist Michael Faraday. They are essen-
tially sandwich bags made of aluminum foil: cheap, light-
weight, and easy to use. See Brief for Criminal Law Pro-
fessors as Amici Curiae 9. They may not be a complete
answer to the problem, see Ayers 32, but at least for now
they provide a reasonable response. In fact, a number of
law enforcement agencies around the country already
encourage the use of Faraday bags. See, e.g., Dept. of
Justice, National Institute of Justice, Electronic Crime
Scene Investigation: A Guide for First Responders 14, 32
(2d ed. Apr. 2008); Brief for Criminal Law Professors as
Amici Curiae 4–6.
   To the extent that law enforcement still has specific
concerns about the potential loss of evidence in a particu-
lar case, there remain more targeted ways to address
                  Cite as: 573 U. S. ____ (2014)           15

                      Opinion of the Court

those concerns. If “the police are truly confronted with a
‘now or never’ situation,”—for example, circumstances
suggesting that a defendant’s phone will be the target of
an imminent remote-wipe attempt—they may be able to
rely on exigent circumstances to search the phone imme-
diately. Missouri v. McNeely, 569 U. S. ___, ___ (2013)
(slip op., at 10) (quoting Roaden v. Kentucky, 413 U. S.
496, 505 (1973); some internal quotation marks omitted).
Or, if officers happen to seize a phone in an unlocked
state, they may be able to disable a phone’s automatic-lock
feature in order to prevent the phone from locking and
encrypting data. See App. to Reply Brief in No. 13–132, p.
3a (diagramming the few necessary steps). Such a preven-
tive measure could be analyzed under the principles set
forth in our decision in McArthur, 531 U. S. 326, which
approved officers’ reasonable steps to secure a scene to
preserve evidence while they awaited a warrant. See id.,
at 331–333.
                              B
   The search incident to arrest exception rests not only on
the heightened government interests at stake in a volatile
arrest situation, but also on an arrestee’s reduced privacy
interests upon being taken into police custody. Robinson
focused primarily on the first of those rationales. But it
also quoted with approval then-Judge Cardozo’s account of
the historical basis for the search incident to arrest excep-
tion: “Search of the person becomes lawful when grounds
for arrest and accusation have been discovered, and the
law is in the act of subjecting the body of the accused to its
physical dominion.” 414 U. S., at 232 (quoting People v.
Chiagles, 237 N. Y. 193, 197, 142 N. E. 583, 584 (1923));
see also 414 U. S., at 237 (Powell, J., concurring) (“an
individual lawfully subjected to a custodial arrest retains
no significant Fourth Amendment interest in the privacy
of his person”). Put simply, a patdown of Robinson’s cloth-
16                  RILEY v. CALIFORNIA

                     Opinion of the Court

ing and an inspection of the cigarette pack found in his
pocket constituted only minor additional intrusions com-
pared to the substantial government authority exercised
in taking Robinson into custody. See Chadwick, 433 U. S.,
at 16, n. 10 (searches of a person are justified in part by
“reduced expectations of privacy caused by the arrest”).
   The fact that an arrestee has diminished privacy inter-
ests does not mean that the Fourth Amendment falls out
of the picture entirely. Not every search “is acceptable
solely because a person is in custody.” Maryland v. King,
569 U. S. ___, ___ (2013) (slip op., at 26). To the contrary,
when “privacy-related concerns are weighty enough” a
“search may require a warrant, notwithstanding the di-
minished expectations of privacy of the arrestee.” Ibid.
One such example, of course, is Chimel. Chimel refused to
“characteriz[e] the invasion of privacy that results from a
top-to-bottom search of a man’s house as ‘minor.’ ” 395
U. S., at 766–767, n. 12. Because a search of the arrestee’s
entire house was a substantial invasion beyond the arrest
itself, the Court concluded that a warrant was required.
   Robinson is the only decision from this Court applying
Chimel to a search of the contents of an item found on an
arrestee’s person. In an earlier case, this Court had ap-
proved a search of a zipper bag carried by an arrestee, but
the Court analyzed only the validity of the arrest itself.
See Draper v. United States, 358 U. S. 307, 310–311
(1959). Lower courts applying Robinson and Chimel,
however, have approved searches of a variety of personal
items carried by an arrestee. See, e.g., United States v.
Carrion, 809 F. 2d 1120, 1123, 1128 (CA5 1987) (billfold
and address book); United States v. Watson, 669 F. 2d
1374, 1383–1384 (CA11 1982) (wallet); United States v.
Lee, 501 F. 2d 890, 892 (CADC 1974) (purse).
   The United States asserts that a search of all data
stored on a cell phone is “materially indistinguishable”
from searches of these sorts of physical items. Brief for
                 Cite as: 573 U. S. ____ (2014)          17

                     Opinion of the Court

United States in No. 13–212, p. 26. That is like saying a
ride on horseback is materially indistinguishable from a
flight to the moon. Both are ways of getting from point A
to point B, but little else justifies lumping them together.
Modern cell phones, as a category, implicate privacy con-
cerns far beyond those implicated by the search of a ciga-
rette pack, a wallet, or a purse. A conclusion that inspect-
ing the contents of an arrestee’s pockets works no
substantial additional intrusion on privacy beyond the
arrest itself may make sense as applied to physical items,
but any extension of that reasoning to digital data has to
rest on its own bottom.
                               1
   Cell phones differ in both a quantitative and a qualita-
tive sense from other objects that might be kept on an
arrestee’s person. The term “cell phone” is itself mislead-
ing shorthand; many of these devices are in fact minicom-
puters that also happen to have the capacity to be used as
a telephone. They could just as easily be called cameras,
video players, rolodexes, calendars, tape recorders, librar-
ies, diaries, albums, televisions, maps, or newspapers.
   One of the most notable distinguishing features of mod-
ern cell phones is their immense storage capacity. Before
cell phones, a search of a person was limited by physical
realities and tended as a general matter to constitute only
a narrow intrusion on privacy. See Kerr, Foreword: Ac-
counting for Technological Change, 36 Harv. J. L. & Pub.
Pol’y 403, 404–405 (2013). Most people cannot lug around
every piece of mail they have received for the past several
months, every picture they have taken, or every book or
article they have read—nor would they have any reason to
attempt to do so. And if they did, they would have to drag
behind them a trunk of the sort held to require a search
warrant in Chadwick, supra, rather than a container the
size of the cigarette package in Robinson.
18                    RILEY v. CALIFORNIA

                        Opinion of the Court

   But the possible intrusion on privacy is not physically
limited in the same way when it comes to cell phones. The
current top-selling smart phone has a standard capacity of
16 gigabytes (and is available with up to 64 gigabytes).
Sixteen gigabytes translates to millions of pages of text,
thousands of pictures, or hundreds of videos. See Kerr,
supra, at 404; Brief for Center for Democracy & Technol-
ogy et al. as Amici Curiae 7–8. Cell phones couple that
capacity with the ability to store many different types of
information: Even the most basic phones that sell for less
than $20 might hold photographs, picture messages, text
messages, Internet browsing history, a calendar, a thousand-
entry phone book, and so on. See id., at 30; United States
v. Flores-Lopez, 670 F. 3d 803, 806 (CA7 2012). We expect
that the gulf between physical practicability and digital
capacity will only continue to widen in the future.
   The storage capacity of cell phones has several interre-
lated consequences for privacy. First, a cell phone collects
in one place many distinct types of information—an ad-
dress, a note, a prescription, a bank statement, a video—
that reveal much more in combination than any isolated
record. Second, a cell phone’s capacity allows even just
one type of information to convey far more than previously
possible. The sum of an individual’s private life can be
reconstructed through a thousand photographs labeled
with dates, locations, and descriptions; the same cannot be
said of a photograph or two of loved ones tucked into a
wallet. Third, the data on a phone can date back to the
purchase of the phone, or even earlier. A person might
carry in his pocket a slip of paper reminding him to call
Mr. Jones; he would not carry a record of all his communi-
cations with Mr. Jones for the past several months, as
would routinely be kept on a phone.1
——————
  1 Because the United States and California agree that these cases

involve searches incident to arrest, these cases do not implicate the
                   Cite as: 573 U. S. ____ (2014)                19

                        Opinion of the Court

   Finally, there is an element of pervasiveness that char-
acterizes cell phones but not physical records. Prior to the
digital age, people did not typically carry a cache of sensi-
tive personal information with them as they went about
their day. Now it is the person who is not carrying a cell
phone, with all that it contains, who is the exception.
According to one poll, nearly three-quarters of smart
phone users report being within five feet of their phones
most of the time, with 12% admitting that they even use
their phones in the shower. See Harris Interactive, 2013
Mobile Consumer Habits Study (June 2013). A decade ago
police officers searching an arrestee might have occasion-
ally stumbled across a highly personal item such as a
diary. See, e.g., United States v. Frankenberry, 387 F. 2d
337 (CA2 1967) (per curiam). But those discoveries were
likely to be few and far between. Today, by contrast, it is
no exaggeration to say that many of the more than 90% of
American adults who own a cell phone keep on their per-
son a digital record of nearly every aspect of their lives—
from the mundane to the intimate. See Ontario v. Quon,
560 U. S. 746, 760 (2010). Allowing the police to scrutinize
such records on a routine basis is quite different from
allowing them to search a personal item or two in the
occasional case.
   Although the data stored on a cell phone is distin-
guished from physical records by quantity alone, certain
types of data are also qualitatively different. An Internet
search and browsing history, for example, can be found on
an Internet-enabled phone and could reveal an individu-
al’s private interests or concerns—perhaps a search for
certain symptoms of disease, coupled with frequent visits
to WebMD. Data on a cell phone can also reveal where a
person has been. Historic location information is a stand-
—————— 

question whether the collection or inspection of aggregated digital

information amounts to a search under other circumstances.

20                 RILEY v. CALIFORNIA

                     Opinion of the Court

ard feature on many smart phones and can reconstruct
someone’s specific movements down to the minute, not
only around town but also within a particular building.
See United States v. Jones, 565 U. S. ___, ___ (2012)
(SOTOMAYOR, J., concurring) (slip op., at 3) (“GPS monitor-
ing generates a precise, comprehensive record of a person’s
public movements that reflects a wealth of detail about
her familial, political, professional, religious, and sexual
associations.”).
  Mobile application software on a cell phone, or “apps,”
offer a range of tools for managing detailed information
about all aspects of a person’s life. There are apps for
Democratic Party news and Republican Party news; apps
for alcohol, drug, and gambling addictions; apps for shar-
ing prayer requests; apps for tracking pregnancy symp-
toms; apps for planning your budget; apps for every con-
ceivable hobby or pastime; apps for improving your
romantic life. There are popular apps for buying or selling
just about anything, and the records of such transactions
may be accessible on the phone indefinitely. There are
over a million apps available in each of the two major app
stores; the phrase “there’s an app for that” is now part of
the popular lexicon. The average smart phone user has
installed 33 apps, which together can form a revealing
montage of the user’s life. See Brief for Electronic Privacy
Information Center as Amicus Curiae in No. 13–132, p. 9.
  In 1926, Learned Hand observed (in an opinion later
quoted in Chimel) that it is “a totally different thing to
search a man’s pockets and use against him what they
contain, from ransacking his house for everything which
may incriminate him.” United States v. Kirschenblatt, 16
F. 2d 202, 203 (CA2). If his pockets contain a cell phone,
however, that is no longer true. Indeed, a cell phone
search would typically expose to the government far more
than the most exhaustive search of a house: A phone not
only contains in digital form many sensitive records previ-
                 Cite as: 573 U. S. ____ (2014)          21

                     Opinion of the Court

ously found in the home; it also contains a broad array of
private information never found in a home in any form—
unless the phone is.
                              2
   To further complicate the scope of the privacy interests
at stake, the data a user views on many modern cell
phones may not in fact be stored on the device itself.
Treating a cell phone as a container whose contents may
be searched incident to an arrest is a bit strained as an
initial matter. See New York v. Belton, 453 U. S. 454, 460,
n. 4 (1981) (describing a “container” as “any object capable
of holding another object”). But the analogy crumbles
entirely when a cell phone is used to access data located
elsewhere, at the tap of a screen. That is what cell
phones, with increasing frequency, are designed to do by
taking advantage of “cloud computing.” Cloud computing
is the capacity of Internet-connected devices to display
data stored on remote servers rather than on the device
itself. Cell phone users often may not know whether
particular information is stored on the device or in the
cloud, and it generally makes little difference. See Brief
for Electronic Privacy Information Center in No. 13–132,
at 12–14, 20. Moreover, the same type of data may be
stored locally on the device for one user and in the cloud
for another.
   The United States concedes that the search incident to
arrest exception may not be stretched to cover a search of
files accessed remotely—that is, a search of files stored in
the cloud. See Brief for United States in No. 13–212, at
43–44. Such a search would be like finding a key in a
suspect’s pocket and arguing that it allowed law enforce-
ment to unlock and search a house. But officers searching
a phone’s data would not typically know whether the
information they are viewing was stored locally at the
time of the arrest or has been pulled from the cloud.
22                  RILEY v. CALIFORNIA

                     Opinion of the Court

  Although the Government recognizes the problem, its
proposed solutions are unclear. It suggests that officers
could disconnect a phone from the network before search-
ing the device—the very solution whose feasibility it con-
tested with respect to the threat of remote wiping. Com-
pare Tr. of Oral Arg. in No. 13–132, at 50–51, with Tr. of
Oral Arg. in No. 13–212, pp. 13–14. Alternatively, the
Government proposes that law enforcement agencies
“develop protocols to address” concerns raised by cloud
computing. Reply Brief in No. 13–212, pp. 14–15. Proba-
bly a good idea, but the Founders did not fight a revolution
to gain the right to government agency protocols. The
possibility that a search might extend well beyond papers
and effects in the physical proximity of an arrestee is yet
another reason that the privacy interests here dwarf those
in Robinson.
                              C
  Apart from their arguments for a direct extension of
Robinson, the United States and California offer various
fallback options for permitting warrantless cell phone
searches under certain circumstances. Each of the pro-
posals is flawed and contravenes our general preference to
provide clear guidance to law enforcement through cate-
gorical rules. “[I]f police are to have workable rules, the
balancing of the competing interests . . . ‘must in large
part be done on a categorical basis—not in an ad hoc, case-
by-case fashion by individual police officers.’ ” Michigan v.
Summers, 452 U. S. 692, 705, n. 19 (1981) (quoting Duna-
way v. New York, 442 U. S. 200, 219–220 (1979) (White, J.,
concurring)).
  The United States first proposes that the Gant standard
be imported from the vehicle context, allowing a warrant-
less search of an arrestee’s cell phone whenever it is rea-
sonable to believe that the phone contains evidence of the
crime of arrest. But Gant relied on “circumstances unique
                 Cite as: 573 U. S. ____ (2014)           23

                     Opinion of the Court

to the vehicle context” to endorse a search solely for the
purpose of gathering evidence. 556 U. S., at 343. JUSTICE
SCALIA’s Thornton opinion, on which Gant was based,
explained that those unique circumstances are “a reduced
expectation of privacy” and “heightened law enforcement
needs” when it comes to motor vehicles. 541 U. S., at 631;
see also Wyoming v. Houghton, 526 U. S., at 303–304. For
reasons that we have explained, cell phone searches bear
neither of those characteristics.
  At any rate, a Gant standard would prove no practical
limit at all when it comes to cell phone searches. In the
vehicle context, Gant generally protects against searches
for evidence of past crimes. See 3 W. LaFave, Search and
Seizure §7.1(d), at 709, and n. 191. In the cell phone
context, however, it is reasonable to expect that incrimi-
nating information will be found on a phone regardless of
when the crime occurred. Similarly, in the vehicle context
Gant restricts broad searches resulting from minor crimes
such as traffic violations. See id., §7.1(d), at 713, and n.
204. That would not necessarily be true for cell phones. It
would be a particularly inexperienced or unimaginative
law enforcement officer who could not come up with sev-
eral reasons to suppose evidence of just about any crime
could be found on a cell phone. Even an individual pulled
over for something as basic as speeding might well have
locational data dispositive of guilt on his phone. An indi-
vidual pulled over for reckless driving might have evi-
dence on the phone that shows whether he was texting
while driving. The sources of potential pertinent infor-
mation are virtually unlimited, so applying the Gant
standard to cell phones would in effect give “police officers
unbridled discretion to rummage at will among a person’s
private effects.” 556 U. S., at 345.
  The United States also proposes a rule that would re-
strict the scope of a cell phone search to those areas of the
phone where an officer reasonably believes that infor-
24                  RILEY v. CALIFORNIA

                     Opinion of the Court

mation relevant to the crime, the arrestee’s identity, or
officer safety will be discovered. See Brief for United
States in No. 13–212, at 51–53. This approach would
again impose few meaningful constraints on officers. The
proposed categories would sweep in a great deal of infor-
mation, and officers would not always be able to discern in
advance what information would be found where.
  We also reject the United States’ final suggestion that
officers should always be able to search a phone’s call log,
as they did in Wurie’s case. The Government relies on
Smith v. Maryland, 442 U. S. 735 (1979), which held that
no warrant was required to use a pen register at telephone
company premises to identify numbers dialed by a particu-
lar caller. The Court in that case, however, concluded that
the use of a pen register was not a “search” at all under
the Fourth Amendment. See id., at 745–746. There is no
dispute here that the officers engaged in a search of
Wurie’s cell phone. Moreover, call logs typically contain
more than just phone numbers; they include any identify-
ing information that an individual might add, such as the
label “my house” in Wurie’s case.
  Finally, at oral argument California suggested a differ-
ent limiting principle, under which officers could search
cell phone data if they could have obtained the same in-
formation from a pre-digital counterpart. See Tr. of Oral
Arg. in No. 13–132, at 38–43; see also Flores-Lopez, 670
F. 3d, at 807 (“If police are entitled to open a pocket diary
to copy the owner’s address, they should be entitled to
turn on a cell phone to learn its number.”). But the fact
that a search in the pre-digital era could have turned up a
photograph or two in a wallet does not justify a search of
thousands of photos in a digital gallery. The fact that
someone could have tucked a paper bank statement in a
pocket does not justify a search of every bank statement
from the last five years. And to make matters worse, such
an analogue test would allow law enforcement to search a
                 Cite as: 573 U. S. ____ (2014)           25

                     Opinion of the Court

range of items contained on a phone, even though people
would be unlikely to carry such a variety of information in
physical form. In Riley’s case, for example, it is implausi-
ble that he would have strolled around with video tapes,
photo albums, and an address book all crammed into his
pockets. But because each of those items has a pre-digital
analogue, police under California’s proposal would be able
to search a phone for all of those items—a significant
diminution of privacy.
  In addition, an analogue test would launch courts on a
difficult line-drawing expedition to determine which digi-
tal files are comparable to physical records. Is an e-mail
equivalent to a letter? Is a voicemail equivalent to a
phone message slip? It is not clear how officers could
make these kinds of decisions before conducting a search,
or how courts would apply the proposed rule after the fact.
An analogue test would “keep defendants and judges
guessing for years to come.” Sykes v. United States, 564
U. S. 1, ___ (2011) (SCALIA, J., dissenting) (slip op., at 7)
(discussing the Court’s analogue test under the Armed
Career Criminal Act).
                            IV
  We cannot deny that our decision today will have an
impact on the ability of law enforcement to combat crime.
Cell phones have become important tools in facilitating
coordination and communication among members of crim-
inal enterprises, and can provide valuable incriminating
information about dangerous criminals. Privacy comes at
a cost.
  Our holding, of course, is not that the information on a
cell phone is immune from search; it is instead that a
warrant is generally required before such a search, even
when a cell phone is seized incident to arrest. Our cases
have historically recognized that the warrant requirement
is “an important working part of our machinery of gov-
26                  RILEY v. CALIFORNIA

                     Opinion of the Court

ernment,” not merely “an inconvenience to be somehow
‘weighed’ against the claims of police efficiency.” Coolidge
v. New Hampshire, 403 U. S. 443, 481 (1971). Recent
technological advances similar to those discussed here
have, in addition, made the process of obtaining a warrant
itself more efficient. See McNeely, 569 U. S., at ___ (slip
op., at 11–12); id., at ___ (ROBERTS, C. J., concurring in
part and dissenting in part) (slip op., at 8) (describing
jurisdiction where “police officers can e-mail warrant
requests to judges’ iPads [and] judges have signed such
warrants and e-mailed them back to officers in less than
15 minutes”).
   Moreover, even though the search incident to arrest
exception does not apply to cell phones, other case-specific
exceptions may still justify a warrantless search of a
particular phone. “One well-recognized exception applies
when ‘ “the exigencies of the situation” make the needs of
law enforcement so compelling that [a] warrantless search
is objectively reasonable under the Fourth Amendment.’ ”
Kentucky v. King, 563 U. S., at ___ (slip op., at 6) (quoting
Mincey v. Arizona, 437 U. S. 385, 394 (1978)). Such exi-
gencies could include the need to prevent the imminent
destruction of evidence in individual cases, to pursue a
fleeing suspect, and to assist persons who are seriously
injured or are threatened with imminent injury. 563
U. S., at ___. In Chadwick, for example, the Court held
that the exception for searches incident to arrest did not
justify a search of the trunk at issue, but noted that “if
officers have reason to believe that luggage contains some
immediately dangerous instrumentality, such as explo-
sives, it would be foolhardy to transport it to the station
house without opening the luggage.” 433 U. S., at 15, n. 9.
   In light of the availability of the exigent circumstances
exception, there is no reason to believe that law enforce-
ment officers will not be able to address some of the more
extreme hypotheticals that have been suggested: a suspect
                     Cite as: 573 U. S. ____ (2014)                  27

                         Opinion of the Court

texting an accomplice who, it is feared, is preparing to
detonate a bomb, or a child abductor who may have infor-
mation about the child’s location on his cell phone. The
defendants here recognize—indeed, they stress—that such
fact-specific threats may justify a warrantless search of
cell phone data. See Reply Brief in No. 13–132, at 8–9;
Brief for Respondent in No. 13–212, at 30, 41. The critical
point is that, unlike the search incident to arrest excep-
tion, the exigent circumstances exception requires a court
to examine whether an emergency justified a warrantless
search in each particular case. See McNeely, supra, at ___
(slip op., at 6).2
                        *    *    *
   Our cases have recognized that the Fourth Amendment
was the founding generation’s response to the reviled
“general warrants” and “writs of assistance” of the colonial
era, which allowed British officers to rummage through
homes in an unrestrained search for evidence of criminal
activity. Opposition to such searches was in fact one of the
driving forces behind the Revolution itself. In 1761, the
patriot James Otis delivered a speech in Boston denounc-
ing the use of writs of assistance. A young John Adams
was there, and he would later write that “[e]very man of a
crowded audience appeared to me to go away, as I did,
ready to take arms against writs of assistance.” 10 Works
of John Adams 247–248 (C. Adams ed. 1856). According to
Adams, Otis’s speech was “the first scene of the first act of

——————
  2 In Wurie’s case, for example, the dissenting First Circuit judge ar-
gued that exigent circumstances could have justified a search of Wurie’s
phone. See 728 F. 3d 1, 17 (2013) (opinion of Howard, J.) (discussing
the repeated unanswered calls from “my house,” the suspected location
of a drug stash). But the majority concluded that the Government had
not made an exigent circumstances argument. See id., at 1. The
Government acknowledges the same in this Court. See Brief for United
States in No. 13–212, p. 28, n. 8.
28                 RILEY v. CALIFORNIA

                     Opinion of the Court

opposition to the arbitrary claims of Great Britain. Then
and there the child Independence was born.” Id., at 248
(quoted in Boyd v. United States, 116 U. S. 616, 625
(1886)).
   Modern cell phones are not just another technological
convenience. With all they contain and all they may
reveal, they hold for many Americans “the privacies of
life,” Boyd, supra, at 630. The fact that technology now
allows an individual to carry such information in his hand
does not make the information any less worthy of the
protection for which the Founders fought. Our answer to
the question of what police must do before searching a cell
phone seized incident to an arrest is accordingly simple—
get a warrant.
   We reverse the judgment of the California Court of
Appeal in No. 13–132 and remand the case for further
proceedings not inconsistent with this opinion. We affirm
the judgment of the First Circuit in No. 13–212.

                                            It is so ordered.
                 Cite as: 573 U. S. ____ (2014)            1

                      Opinion of ALITO, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                   Nos. 13–132 and 13–212
                         _________________


          DAVID LEON RILEY, PETITIONER
13–132                 v.
                  CALIFORNIA
ON WRIT OF CERTIORARI TO THE COURT OF APPEAL OF CALI-
  FORNIA, FOURTH APPELLATE DISTRICT, DIVISION ONE


            UNITED STATES, PETITIONER
13–212                 v.
                  BRIMA WURIE
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF 

             APPEALS FOR THE FIRST CIRCUIT

                        [June 25, 2014] 


  JUSTICE ALITO, concurring in part and concurring in the
judgment.
  I agree with the Court that law enforcement officers, in
conducting a lawful search incident to arrest, must gener-
ally obtain a warrant before searching information stored
or accessible on a cell phone. I write separately to address
two points.
                              I

                              A

  First, I am not convinced at this time that the ancient
rule on searches incident to arrest is based exclusively (or
even primarily) on the need to protect the safety of arrest-
ing officers and the need to prevent the destruction of
evidence. Cf. ante, at 9. This rule antedates the adoption
of the Fourth Amendment by at least a century. See T.
Clancy, The Fourth Amendment: Its History and Interpre-
tation 340 (2008); T. Taylor, Two Studies in Constitutional
2                   RILEY v. CALIFORNIA

                      Opinion of ALITO, J.

Interpretation 28 (1969); Amar, Fourth Amendment First
Principles, 107 Harv. L. Rev. 757, 764 (1994). In Weeks v.
United States, 232 U. S. 383, 392 (1914), we held that the
Fourth Amendment did not disturb this rule. See also
Taylor, supra, at 45; Stuntz, The Substantive Origins of
Criminal Procedure, 105 Yale L. J. 393, 401 (1995) (“The
power to search incident to arrest—a search of the arrested
suspect’s person . . .—was well established in the mid-
eighteenth century, and nothing in . . . the Fourth
Amendment changed that”). And neither in Weeks nor in
any of the authorities discussing the old common-law rule
have I found any suggestion that it was based exclusively
or primarily on the need to protect arresting officers or to
prevent the destruction of evidence.
  On the contrary, when pre-Weeks authorities discussed
the basis for the rule, what was mentioned was the need to
obtain probative evidence. For example, an 1839 case
stated that “it is clear, and beyond doubt, that . . . consta-
bles . . . are entitled, upon a lawful arrest by them of one
charged with treason or felony, to take and detain prop-
erty found in his possession which will form material evi-
dence in his prosecution for that crime.” See Dillon v.
O’Brien, 16 Cox Crim. Cas. 245, 249–251 (1887) (citing
Regina, v. Frost, 9 Car. & P. 129, 173 Eng. Rep. 771)). The
court noted that the origins of that rule “deriv[e] from the
interest which the State has in a person guilty (or reason-
ably believed to be guilty) of a crime being brought to
justice, and in a prosecution, once commenced, being
determined in due course of law.” 16 Cox Crim. Cas., at
249–250. See also Holker v. Hennessey, 141 Mo. 527, 537–
540, 42 S. W. 1090, 1093 (1897).
  Two 19th-century treatises that this Court has previ-
ously cited in connection with the origin of the search-
incident-to-arrest rule, see Weeks, supra, at 392, suggest
the same rationale. See F. Wharton, Criminal Pleading
and Practice §60, p. 45 (8th ed. 1880) (“Those arresting a
                      Cite as: 573 U. S. ____ (2014)                       3

                            Opinion of ALITO, J.

defendant are bound to take from his person any articles
which may be of use as proof in the trial of the offense
with which the defendant is charged”); J. Bishop, Criminal
Procedure §§210–212, p. 127 (2d ed. 1872) (if an arresting
officer finds “about the prisoner’s person, or otherwise in
his possession, either goods or moneys which there is
reason to believe are connected with the supposed crime as
its fruits, or as the instruments with which it was commit-
ted, or as directly furnishing evidence relating to the
transaction, he may take the same, and hold them to be
disposed of as the court may direct”).
   What ultimately convinces me that the rule is not closely
linked to the need for officer safety and evidence preser-
vation is that these rationales fail to explain the rule’s
well-recognized scope. It has long been accepted that
written items found on the person of an arrestee may be
examined and used at trial.* But once these items are
——————
   * Cf. Hill v. California, 401 U. S. 797, 799–802, and n. 1 (1971) (diary);
Marron v. United States, 275 U. S. 192, 193, 198–199 (1927) (ledger
and bills); Gouled v. United States, 255 U. S. 298, 309 (1921), overruled
on other grounds, Warden, Md. Penitentiary v. Hayden, 387 U. S. 294,
300–301 (1967) (papers); see United States v. Rodriguez, 995 F. 2d 776,
778 (CA7 1993) (address book); United States v. Armendariz–Mata, 949
F. 2d 151, 153 (CA5 1991) (notebook); United States v. Molinaro, 877
F. 2d 1341 (CA7 1989) (wallet); United States v. Richardson, 764 F. 2d
1514, 1527 (CA11 1985) (wallet and papers); United States v. Watson,
669 F. 2d 1374, 1383–1384 (CA11 1982) (documents found in a wallet);
United States v. Castro, 596 F. 2d 674, 677 (CA5 1979), cert. denied,
444 U. S. 963 (1979) (paper found in a pocket); United States v. Jeffers,
520 F. 2d 1256, 1267–1268 (CA7 1975) (three notebooks and meeting
minutes); Bozel v. Hudspeth, 126 F. 2d 585, 587 (CA10 1942) (papers,
circulars, advertising matter, “memoranda containing various names
and addresses”); United States v. Park Avenue Pharmacy, 56 F. 2d 753,
755 (CA2 1932) (“numerous prescriptions blanks” and a check book).
See also 3 W. LaFave, Search and Seizure §5.2(c), p. 144 (5th ed. 2012)
(“Lower courts, in applying Robinson, have deemed evidentiary searches
of an arrested person to be virtually unlimited”); W. Cuddihy, Fourth
Amendment: Origins and Original Meaning 847–848 (1990) (in the pre-
Constitution colonial era, “[a]nyone arrested could expect that not only
4                     RILEY v. CALIFORNIA

                        Opinion of ALITO, J.

taken away from an arrestee (something that obviously
must be done before the items are read), there is no risk
that the arrestee will destroy them. Nor is there any risk
that leaving these items unread will endanger the arrest-
ing officers.
  The idea that officer safety and the preservation of
evidence are the sole reasons for allowing a warrantless
search incident to arrest appears to derive from the
Court’s reasoning in Chimel v. California, 395 U. S. 752
(1969), a case that involved the lawfulness of a search of
the scene of an arrest, not the person of an arrestee. As I
have explained, Chimel’s reasoning is questionable, see
Arizona v. Gant, 556 U. S. 332, 361–363 (2009) (ALITO, J.,
dissenting), and I think it is a mistake to allow that rea-
soning to affect cases like these that concern the search of
the person of arrestees.
                            B
  Despite my view on the point discussed above, I agree
that we should not mechanically apply the rule used in the
predigital era to the search of a cell phone. Many cell
phones now in use are capable of storing and accessing a
quantity of information, some highly personal, that no
person would ever have had on his person in hard-copy
form. This calls for a new balancing of law enforcement
and privacy interests.
  The Court strikes this balance in favor of privacy inter-
ests with respect to all cell phones and all information
found in them, and this approach leads to anomalies. For
example, the Court’s broad holding favors information in
digital form over information in hard-copy form. Suppose
that two suspects are arrested. Suspect number one has
in his pocket a monthly bill for his land-line phone, and

—————— 

his surface clothing but his body, luggage, and saddlebags would be

searched”). 

                 Cite as: 573 U. S. ____ (2014)           5

                      Opinion of ALITO, J.

the bill lists an incriminating call to a long-distance num-
ber. He also has in his a wallet a few snapshots, and one
of these is incriminating. Suspect number two has in his
pocket a cell phone, the call log of which shows a call to
the same incriminating number. In addition, a number of
photos are stored in the memory of the cell phone, and one
of these is incriminating. Under established law, the
police may seize and examine the phone bill and the snap-
shots in the wallet without obtaining a warrant, but under
the Court’s holding today, the information stored in the
cell phone is out.
  While the Court’s approach leads to anomalies, I do not
see a workable alternative. Law enforcement officers need
clear rules regarding searches incident to arrest, and it
would take many cases and many years for the courts to
develop more nuanced rules. And during that time, the
nature of the electronic devices that ordinary Americans
carry on their persons would continue to change.
                             II
  This brings me to my second point. While I agree with
the holding of the Court, I would reconsider the question
presented here if either Congress or state legislatures,
after assessing the legitimate needs of law enforcement
and the privacy interests of cell phone owners, enact legis-
lation that draws reasonable distinctions based on catego-
ries of information or perhaps other variables.
  The regulation of electronic surveillance provides an
instructive example. After this Court held that electronic
surveillance constitutes a search even when no property
interest is invaded, see Katz v. United States, 389 U. S.
347, 353–359 (1967), Congress responded by enacting Title
III of the Omnibus Crime Control and Safe Streets Act of
1968, 82 Stat. 211. See also 18 U. S. C. §2510 et seq.
Since that time, electronic surveillance has been governed
primarily, not by decisions of this Court, but by the stat-
6                  RILEY v. CALIFORNIA

                     Opinion of ALITO, J.

ute, which authorizes but imposes detailed restrictions on
electronic surveillance. See ibid.
  Modern cell phones are of great value for both lawful
and unlawful purposes. They can be used in committing
many serious crimes, and they present new and difficult
law enforcement problems. See Brief for United States in
No. 13–212, pp. 2–3. At the same time, because of the role
that these devices have come to play in contemporary life,
searching their contents implicates very sensitive privacy
interests that this Court is poorly positioned to under-
stand and evaluate. Many forms of modern technology are
making it easier and easier for both government and
private entities to amass a wealth of information about
the lives of ordinary Americans, and at the same time,
many ordinary Americans are choosing to make public
much information that was seldom revealed to outsiders
just a few decades ago.
  In light of these developments, it would be very unfor-
tunate if privacy protection in the 21st century were left
primarily to the federal courts using the blunt instrument
of the Fourth Amendment. Legislatures, elected by the
people, are in a better position than we are to assess and
respond to the changes that have already occurred and
those that almost certainly will take place in the future.

```

---
