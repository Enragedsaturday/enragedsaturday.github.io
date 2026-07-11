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

## GROUP: _overhaul2/lake/cases/Postal Service v. Konan.json  (`lake-record`, 1 assertions)

### content_page

```
---
title: Postal Service v. Konan
type: case
citation: "No. 24-351, slip op. (U.S. 2026)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2026
date_decided: ""
docket: 24-351
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
  opinion_url: "https://www.courtlistener.com/opinion/10799651/postal-service-v-konan/"
  cluster_id: 10799651
  opinion_id: 11266325
  identity_checked: false
lake:
  record_id: Postal Service v. Konan
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - federal-tort-claims-act
  - sovereign-immunity
  - postal-exception
  - statutory-interpretation
  - supreme-court
holding: "The Federal Tort Claims Act's postal exception, which preserves the United States' sovereign immunity for claims 'arising out of the loss, miscarriage, or negligent transmission of letters or postal matter,' bars claims for the intentional nondelivery of mail, because both 'miscarriage' and 'loss' of mail — as ordinarily understood when the FTCA was enacted — can result from the Postal Service's intentional failure to deliver it."
aliases:
  - Postal Service v. Konan
  - United States Postal Service v. Konan
  - "Postal Service v. Konan (2026)"
---

# Postal Service v. Konan

*No. 24-351, slip op. (U.S. 2026)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10799651 → majority opinion 11266325 (No. 24-351, decided Feb. 24, 2026). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (current-Term slip opinion, no reporter cite assigned — S2 A3). S9 promotes. -->

## Background
Lebene Konan owned two rental properties served by the Euless, Texas post office. She alleged that Postal Service employees intentionally withheld her mail and interfered with its delivery, and after administrative complaints failed, she sued the United States under the Federal Tort Claims Act, bringing state-law tort claims. The district court dismissed under the FTCA's "postal exception," 28 U.S.C. § 2680(b), which retains sovereign immunity for claims arising out of the loss, miscarriage, or negligent transmission of letters or postal matter. The Fifth Circuit reversed, holding that intentional nondelivery is not "loss," "miscarriage," or "negligent transmission"; the First and Second Circuits had held otherwise, and the Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]] to resolve the split.

## Issue
Whether the FTCA's postal exception applies to claims arising from the Postal Service's intentional failure to deliver mail.

## Rule
Statutory terms carry the ordinary meaning they had when enacted; when the FTCA was enacted in 1946, a "miscarriage" of mail meant any failure of mail to reach its intended destination — including intentional acts such as mail being stolen or burned — and "loss" meant a deprivation of mail however brought about. The Court held: "The United States retains sovereign immunity for claims arising out of the intentional nondelivery of mail because both 'miscarriage' and 'loss' of mail under the FTCA's postal exception can occur as a result of the Postal Service's intentional failure to deliver the mail." — slip op. at 1. ^pin-slip1

## Application
Konan's theory — that postal employees deliberately withheld her mail — describes conduct squarely within the ordinary 1946 meanings of "miscarriage" and "loss." Nothing in the contemporary dictionaries limited "miscarriage" to negligent failures or to misdelivery at the wrong address; ordinary speakers used the word for mail that never arrived, whatever the cause. Because her claims arise out of the loss and miscarriage of mail, the postal exception preserves the United States' sovereign immunity.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]].** The Court held the postal exception bars the claims.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Konan* resolves a circuit split on the FTCA postal exception, reading "loss" and "miscarriage" broadly enough to cover intentional nondelivery — a sovereign-immunity boundary that channels grievances against the Postal Service away from tort suits, relevant here as a contrast to the remedies available against state and municipal actors under § 1983.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Postal Service v. Konan*, No. 24-351, slip op. (U.S. 2026)](https://www.courtlistener.com/opinion/10799651/postal-service-v-konan/) — pinpoint: slip op. at 1 (postal exception covers intentional nondelivery). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07. Current-Term slip opinion; no U.S. Reports cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5448a4fd7da7c948", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Postal Service v. Konan"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Postal Service v. Konan", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Postal Service v. Konan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Postal Service v. Konan",
  "status": "under_review",
  "identity": {
    "case_name": "Postal Service v. Konan",
    "case_name_short": "Konan",
    "case_name_full": "",
    "input_case_name": "Postal Service v. Konan",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2026,
    "docket": "24-351",
    "cluster_id": 10799651,
    "lead_opinion_id": 11266325,
    "sibling_ids": [],
    "absolute_url": "/opinion/10799651/postal-service-v-konan/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "SCOTUS No. 24-351, decided 2026-02-24 (607 U.S. ___; slip 'subject to formal revision'). No S. Ct. page yet.",
      "legs": [
        {
          "source": "Cornell LII",
          "url": "https://www.law.cornell.edu/supremecourt/text/24-351",
          "cite": "No. 24-351, decided 2026-02-24, subject to revision"
        },
        {
          "source": "Justia",
          "url": "https://supreme.justia.com/cases/federal/us/607/24-351/",
          "cite": "607 U.S. ___ (2026) placeholder"
        }
      ]
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
    "date_created": "2026-07-06T12:13:11Z",
    "date_modified": "2026-07-09T05:52:34Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:13:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "postal-service-v-konan--10799651",
      "to_record_id": "Postal Service v. Konan",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Postal Service v. Konan

```
(Slip Opinion)              OCTOBER TERM, 2025                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

  UNITED STATES POSTAL SERVICE ET AL. v. KONAN

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE FIFTH CIRCUIT

   No. 24–351.      Argued October 8, 2025—Decided February 24, 2026


Respondent Lebene Konan and the local post office in Euless, Texas, had
  an extended dispute concerning mail delivery to two rental properties
  owned by Konan. Konan alleged that, among other things, United
  States Postal Service employees intentionally withheld her mail and
  interfered with its delivery. After administrative complaints proved
  unsuccessful, Konan sued the United States in federal court, bringing
  various state-law tort claims alleging that the United States Postal
  Service intentionally and wrongfully withheld her mail. The District
  Court dismissed Konan’s complaint pursuant to the Federal Tort
  Claims Act’s postal exception, under which the United States retains
  sovereign immunity for all claims “arising out of the loss, miscarriage,
  or negligent transmission of letters or postal matter,” 28
  U. S. C. §2680(b). The District Court concluded that the United States
  enjoys sovereign immunity from Konan’s claims because they all relate
  to personal or financial harms arising from nondelivery of mail. The
  District Court further held that the postal exception is not limited to
  merely negligent failure to properly carry the mail. The Fifth Circuit
  reversed, holding that the terms “loss,” “miscarriage,” and “negligent
  transmission” do not encompass the intentional act of not delivering
  the mail at all. In contrast, the First and Second Circuits have inter-
  preted the postal exception to apply to suits even when they arise from
  harms caused by intentional misconduct. The Court granted certiorari
  to resolve the split.
Held: The United States retains sovereign immunity for claims arising
 out of the intentional nondelivery of mail because both “miscarriage”
 and “loss” of mail under the FTCA’s postal exception can occur as a
2                      POSTAL SERVICE v. KONAN

                                   Syllabus

    result of the Postal Service’s intentional failure to deliver the mail.
    Pp. 5–13.
       (a) The postal exception reflects Congress’s judgment that redress
    for “harms” of “the sort primarily identified with the Postal Service’s
    function of transporting mail throughout the United States” should not
    come from potentially burdensome tort suits. Dolan v. Postal Service,
    546 U. S. 481, 489. Pp. 5–6.
       (b) Both “miscarriage” and “loss” of mail under the postal exception
    can occur as a result of the Postal Service’s intentional failure to de-
    liver the mail. Pp. 6–11.
         (1) The Court interprets statutory terms according to the ordinary
    meanings they had when they were enacted. Wisconsin Central Ltd.
    v. United States, 585 U. S. 274, 277. When Congress enacted the FTCA
    in 1946, the “miscarriage” of mail ordinarily included any failure of
    mail to properly arrive at its intended destination. Dictionaries pub-
    lished around that time confirm that a “miscarriage” of mail happened
    when mail failed to arrive at its destination. The Court declines to
    limit “miscarriage” to negligent failures, as no dictionaries cited im-
    pose this limitation, and ordinary speakers used “miscarriage” to refer
    to problems with mail caused by intentional misconduct, such as when
    mail was stolen or burned. The Court also declines to limit “miscar-
    riage” to when mail goes to the wrong address, as speakers used the
    term when mail failed to reach its intended destination regardless of
    where the mail ended up, including when mail was delayed, came too
    late, or was left in the post office. Pp. 6–8.
         (2) When Congress enacted the FTCA, the “loss” of mail ordinarily
    meant a deprivation of mail, regardless of how the deprivation was
    brought about. Contemporary dictionaries defined “loss” as the act or
    fact of losing or suffering deprivation, and one can suffer a deprivation
    of something when another intentionally keeps that thing for himself.
    Konan alleged that she was entitled to possession of her mail but that
    the Postal Service converted it, meaning she was “deprived of the use
    and possession of the property,” Black’s Law Dictionary 421, so her
    claims arise out of the loss of her mail. The Court disagrees with the
    attempt by Konan to limit “loss” to only inadvertent losses. A loss can
    be the result of another person’s intentional misconduct, and ordinary
    speakers commonly described a “loss” of mail from theft, including
    theft by the carrier. The Court also disagrees with the argument that
    the postal exception applies only when the Postal Service lost the mail,
    because Congress applied the postal exception to all “claim[s] arising
    out of the loss, miscarriage, or negligent transmission” of mail, describ-
    ing kinds of harms, not kinds of actions by the postal workers. This
    interpretation is consistent with the principal provision of the FTCA,
    which includes losses caused by intentional misconduct and does not
                      Cite as: 607 U. S. ___ (2026)                      3

                                 Syllabus

  require that the Government lost anything. The Court rejects Konan’s
  proposal to limit “loss” to only “destruction.” Ordinary speakers re-
  ferred to losses of mail even when the mail was not destroyed, and the
  dictionary definitions Konan pointed to were listed first because they
  were the oldest, not because they were primary. Pp. 8–11.
     (c) The Court rejects Konan’s remaining arguments that her claims
  must not be barred by the postal exception. Pp. 11–13.
        (1) Konan argues that the postal exception’s “negligent transmis-
  sion” category narrows the meaning of “miscarriage” and “loss,” but
  Congress intentionally limited the “negligent” qualifier to “transmis-
  sion” and did not use it to qualify “loss” or “miscarriage.” An adjective
  before the final noun in a list cannot be transplanted to qualify the
  preceding nouns. See Barnhart v. Thomas, 540 U. S. 20, 26. The Court
  does not think that the “negligent” qualifier suggests that Congress
  was trying to enable suits involving intentional misconduct. Instead,
  the inclusion of “negligent” to qualify “transmission” forecloses claims
  involving mail even though nothing went wrong with its transport or
  delivery, keeping the focus of the postal exception on mail-delivery
  problems. Pp. 11–12.
        (2) Konan also argues that the Court’s interpretations of “miscar-
  riage” and “loss” run afoul of the presumption against surplusage, be-
  cause many claims—including Konan’s here—will arise from both a
  “miscarriage” and a “loss” of mail. But Konan’s proposal to solve the
  surplusage—three nonoverlapping definitions of the statutory terms—
  is inconsistent with ordinary meaning, which shows that these terms
  are often used in an overlapping manner. In Dolan, the Court inter-
  preted the terms in the postal exception to substantially overlap, 546
  U. S., at 487, and the canon against surplusage is subordinate to the
  cardinal canon that “a legislature says in a statute what it means and
  means in a statute what it says there,” Connecticut Nat. Bank v. Ger-
  main, 503 U. S. 249, 253–254. Congress likely used broad, overlapping
  terms to better keep complaints about mail delivery out of court.
  Pp. 12–13.
     (d) The Court does not decide whether all of Konan’s claims are
  barred by the postal exception, or which arguments Konan adequately
  preserved. P. 13.
96 F. 4th 799, vacated and remanded.

   THOMAS, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and ALITO, KAVANAUGH, and BARRETT, JJ., joined. SOTOMAYOR, J., filed
a dissenting opinion, in which KAGAN, GORSUCH, and JACKSON, JJ.,
joined.
                        Cite as: 607 U. S. ____ (2026)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     United States Reports. Readers are requested to notify the Reporter of
     Decisions, Supreme Court of the United States, Washington, D. C. 20543,
     pio@supremecourt.gov, of any typographical or other formal errors.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 24–351
                                   _________________


      UNITED STATES POSTAL SERVICE, ET AL.,
         PETITIONERS v. LEBENE KONAN
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                              [February 24, 2026]

   JUSTICE THOMAS delivered the opinion of the Court.
   The United States enjoys sovereign immunity and cannot
be sued without its consent. By means of the Federal Tort
Claims Act, Congress waived that sovereign immunity for
certain tort suits based on the conduct of Government em-
ployees. See 28 U. S. C. §§2674, 1346(b). But, in the provi-
sion at issue in this case, Congress retained sovereign im-
munity for a wide range of claims about mail. Specifically,
the FTCA’s postal exception retains sovereign immunity for
all claims “arising out of the loss, miscarriage, or negligent
transmission of letters or postal matter.” §2680(b). This
case concerns whether this exception applies when postal
workers intentionally fail to deliver the mail. We hold that
it does.
                             I
                             A
   The United States Postal Service is a frequent point of
contact between citizens and the Federal Government. In
2024, the Postal Service’s more than 600,000 employees de-
livered more than 112 billion pieces of mail—over 300 mil-
lion a day—to more than 165 million delivery points. See
2                 POSTAL SERVICE v. KONAN

                       Opinion of the Court

United States Postal Service, Fiscal Year 2024 Annual Re-
port to Congress 3, 29, 32, 34. Unsurprisingly, given this
volume, not all mail arrives properly and on time. The
Postal Service reports receiving approximately 335,000 cus-
tomer complaints per year. See Brief for Petitioners 24.
   Because it is a Government agency, recourse against the
Postal Service in the form of lawsuits for money damages is
limited. As part of “the executive branch of the Government
of the United States,” 39 U. S. C. §201, “the Postal Service
enjoys federal sovereign immunity absent a waiver,” Dolan
v. Postal Service, 546 U. S. 481, 484 (2006). Before 1946,
that sovereign immunity generally prevented those injured
by Government employees from receiving compensation
through lawsuits. See Molzof v. United States, 502 U. S.
301, 304 (1992). That year, Congress enacted a “limited
waiver” of immunity through the FTCA. Id., at 305. Sub-
ject to enumerated exceptions, the FTCA allows a plaintiff
to sue the Government for injuries or loss of property
“caused by the negligent or wrongful act or omission of ” a
federal employee “acting within the scope of his office or em-
ployment.” 28 U. S. C. §1346(b)(1).
   The FTCA’s postal exception retains the Government’s
sovereign immunity for lawsuits about failing to properly
carry or deliver mail. It forecloses “[a]ny claim arising out
of the loss, miscarriage, or negligent transmission of letters
or postal matter.” §2680(b). This Court has interpreted the
postal exception to apply when the plaintiff is harmed “be-
cause mail either fails to arrive at all or arrives late, in dam-
aged condition, or at the wrong address.” Dolan, 546 U. S.,
at 489.
                             B
  This case arises from the dismissal of a complaint, so we
accept the complaint’s allegations as true, although the
Government disputes them. National Rifle Association of
America v. Vullo, 602 U. S. 175, 181 (2024). Respondent
                 Cite as: 607 U. S. ____ (2026)            3

                     Opinion of the Court

Lebene Konan owns two houses a block apart in Euless,
Texas—one on Saratoga Drive and the other on Trenton
Lane. Konan leases rooms to tenants in both houses and
occasionally stays at them herself. The Postal Service de-
livers mail for all the houses in the neighborhood to a cen-
tral structure with a box for each house. The Postal Service
distributes keys to the owners of the houses so that they can
retrieve their mail. As the homeowner, Konan received the
keys to the boxes for both houses. Konan kept the keys and
distributed the mail to her tenants daily, and she also re-
ceived some of her own mail at the Saratoga address.
   Konan’s grievances with her mail service began in May
2020. After Konan noticed that no mail had arrived at her
Saratoga house in several days, she learned that the as-
signed carrier had changed the listed owner from Konan’s
name to a tenant’s name. The same carrier then authorized
a change of the lock to allow the tenant to have his own mail
key without Konan’s consent. Konan confronted the em-
ployees at the local post office about these changes. A su-
pervisor at the local post office explained to Konan that the
Postal Service would stop delivering mail to her Saratoga
address until the Postal Service Inspector General’s office
investigated and determined the proper owner. Konan then
received no mail to the Saratoga address for a couple of
months before service resumed.
   Konan then learned that the same carrier had mail ad-
dressed to her and her tenants returned to senders as “un-
deliverable.” As a result, Konan and her tenants did not
receive important mail. Konan resorted to private carriers.
The disruptions in mail service resulted in the loss of ten-
ants and made it more difficult for Konan to attract new
tenants. The carrier also taped a red notice inside the mail-
box stating that mail addressed to some, but not all, of the
Saratoga residents could be delivered to the box. In 2021,
postal workers also allegedly stopped delivering mail to the
4                   POSTAL SERVICE v. KONAN

                         Opinion of the Court

Trenton house after discovering that Konan owned it as
well.
   In response, Konan signed up for the Postal Service’s “In-
formed Delivery” service, which allows customers to view
scans of incoming mail. When she discovered that mail on
its way to her addresses was not being delivered, she re-
quested that the mail for the Saratoga residence be held at
the post office so that she could retrieve it in person. But
the postal employees did not give her the mail because Ko-
nan failed to provide identification for the addressees. In
addition to these efforts, Konan also filed administrative
complaints, but without success.
                               C
   In January 2022, Konan sued the United States in fed-
eral court. Konan alleged that the Postal Service intention-
ally and wrongfully withheld her mail. As relevant here,
Konan brought claims under state law for nuisance, tor-
tious interference with prospective business relations, con-
version, and intentional infliction of emotional distress.
She sought damages for loss of rental income, the depriva-
tion of her rightful mail, and the distress that the postal
workers caused her.*
   The District Court dismissed Konan’s complaint based on
sovereign immunity. Relying on the postal exception, it
concluded that the United States enjoys sovereign immun-
ity from her claims “because they all relate to ‘personal or
financial harms arising from nondelivery . . . of sensitive
materials or information . . .’ and other mail.” 652 F. Supp.
3d 721, 731 (ND Tex. 2023) (quoting Dolan, 546 U. S., at
——————
  *Konan also brought discrimination claims against the postal workers
under 42 U. S. C. §§1981 and 1985, alleging that they were motivated by
racial animus. The District Court dismissed these claims. 652 F. Supp.
3d 721, 731–732 (ND Tex. 2023). The Court of Appeals affirmed. 96
F. 4th 799, 804–805 (CA5 2024). We denied Konan’s cross-petition for
certiorari regarding those claims, so they are not before us. 604 U. S.
1256 (2025).
                 Cite as: 607 U. S. ____ (2026)            5

                     Opinion of the Court

489). The District Court held that the postal exception is
not limited to merely negligent failure to properly carry the
mail. 652 F. Supp. 3d, at 730–731.
  The Court of Appeals for the Fifth Circuit reversed. It
held that “the terms ‘loss,’ ‘miscarriage,’ and ‘negligent
transmission’ do no not encompass the intentional act of not
delivering the mail at all.” 96 F. 4th 799, 804 (2024). It
reasoned that Konan’s claims did not arise out of the “loss”
of mail “because the mail was not destroyed or misplaced
by unintentional action.” Id., at 802 (emphasis added). It
also reasoned that Konan’s claims did not arise from the
“miscarriage” of mail “because there was no attempt at a
carriage.” Ibid. And it reasoned that Konan’s claims did
not arise from the “negligent transmission” of mail because
“the postal workers’ actions were intentional.” Ibid.
  The Fifth Circuit’s decision conflicts with those of the
First and Second Circuits, which have interpreted the
postal exception to apply to suits even when they arise from
harms caused by intentional misconduct. See Levasseur v.
United States Postal Serv., 543 F. 3d 23, 23–24 (CA1 2008)
(per curiam); Marine Ins. Co. v. United States, 378 F. 2d
812, 813–814 (CA2 1967). We granted certiorari to resolve
the split. 604 U. S. 1256 (2025).
                             II
  The postal exception retains the Federal Government’s
sovereign immunity for “[a]ny claim arising out of the loss,
miscarriage, or negligent transmission of letters or postal
matter.” 28 U. S. C. §2680(b). The postal exception reflects
Congress’s judgment that redress for “harms” of “the sort
primarily identified with the Postal Service’s function of
transporting mail throughout the United States” should not
come from tort suits. Dolan, 546 U. S., at 489. Given the
frequency of postal workers’ interactions with citizens,
those suits would arise so often that they would create a
significant burden for the Government and the courts. And
6                 POSTAL SERVICE v. KONAN

                      Opinion of the Court

their cost to taxpayers would depend on the value and im-
portance of the mail’s contents, over which the Government
typically has no control. See, e.g., Marine Ins. Co., 378
F. 2d, at 813 (theft from mail of six emeralds valued at
$152,190 in 1967 dollars).
  According to Konan and the dissent, the postal exception
does not apply to Konan’s claims because she alleges that
postal workers intentionally refused to deliver her mail.
We disagree. Both “miscarriage” and “loss” of mail under
the postal exception can occur as a result of the Postal Ser-
vice’s intentional failure to deliver the mail.
                                A
    Absent a reason to think otherwise, we interpret statu-
tory terms according to the ordinary meanings they had
when they were enacted. Wisconsin Central Ltd. v. United
States, 585 U. S. 274, 277 (2018). When Congress enacted
the FTCA in 1946, the “miscarriage” of mail ordinarily in-
cluded any failure of mail to properly arrive at its intended
destination. Konan would limit “miscarriage” to uninten-
tional failures or failures where the mail went to the wrong
address. Neither limitation is well founded.
    Dictionaries published around the time Congress enacted
the FTCA confirm that a “miscarriage” of mail happened
when mail failed to arrive properly. Two dictionaries indi-
cate that “miscarriage” of mail meant the “failure of a letter
. . . to reach its destination.” 2 New Century Dictionary of
the English Language 1069 (1927); accord, 6 Oxford Eng-
lish Dictionary 497 (1933 ed.) (“The failure (of a letter, etc.)
to reach its destination”). In a third, “miscarriage” meant
the “[f]ailure (of something sent) to arrive.” Webster’s New
International Dictionary 1568 (2d ed. 1934) (Webster’s Sec-
ond). Definitions of “miscarry” were similarly broad. Ibid.
(“To fail of reaching the destination”); 6 Oxford English Dic-
tionary, at 498 (“To fail to reach its proper destination”).
Something can “fail” to happen as a result of intentional
                  Cite as: 607 U. S. ____ (2026)             7

                      Opinion of the Court

misconduct. See, e.g., 26 U. S. C. §291 (1940 ed.) (imposing
a penalty for “failure to make and file [a tax] return” “unless
it is shown that such failure is due to reasonable cause and
not due to willful neglect”). Because a “miscarriage” in-
cludes any failure of mail to arrive properly, a person expe-
riences a miscarriage of mail when his mail is delivered to
his neighbor, held at the post office, or returned to the
sender—regardless of why it happened. Konan’s claims
about the Postal Service’s willful failure to deliver her mail
therefore result from the miscarriage of her mail.
   We disagree with Konan’s attempt to limit “miscarriage”
to negligent failures of mail to arrive properly. Brief for Re-
spondent 19–20; accord, post, at 9 (SOTOMAYOR, J., dissent-
ing). Neither Konan nor the dissent cites any dictionaries
imposing this limitation. Instead, Konan cites examples of
uses of the term “miscarriage” that suggest that the miscar-
riage in question was unintentional, such as an 1868 tele-
graph-law decision explaining that a telegraph company
should not be liable “for every mistake, miscarriage, or ac-
cidental delay that may occur.” United States Tel. Co. v.
Gildersleve, 29 Md. 232, 246 (1868). We agree that miscar-
riage of mail can be unintentional, but “the fact that the
phrase was commonly used in a particular context does not
show that it is limited to that context.” District of Columbia
v. Heller, 554 U. S. 570, 588 (2008).
   In fact, ordinary speakers used “miscarriage” to refer to
problems with mail caused by intentional misconduct.
When a mail pouch was “stolen,” a newspaper reported that
the letters “[m]iscarried.” Kansas City Star, Oct. 20, 1911,
p. 6A. When a priest failed to receive a summons because
it was “burned by an ecclesiastic,” the headline read “His
Letter Miscarried.” The Carbondale Leader, Jan. 3, 1893,
p. 1. And when litigants’ documents failed to arrive, courts
classified “miscarriage” of mail as an excuse, without any
suggestion as to whether the carrier acted intentionally.
See, e.g., Lake v. Lake, 63 Wyo. 375, 402, 182 P. 2d 824, 835
8                 POSTAL SERVICE v. KONAN

                      Opinion of the Court

(1947) (per curiam); Wagner v. Lucas, 79 Okla. 231, 232–
233, 193 P. 421, 422–423 (1920). We see no reason to sup-
pose that these uses of “miscarriage” were extraordinary.
   Konan separately contends that a “miscarriage” of mail
happens only when the mail goes to the “wrong address,”
not when it is (like her mail) held at the post office or re-
turned to the sender. Brief for Respondent 15. We again
decline to impose a limitation that has no basis in the dic-
tionaries or ordinary usage. Speakers used the term “mis-
carriage” when the mail failed to reach its intended desti-
nation, regardless of where it ended up. One newspaper,
for example, explained that a letter “ ‘[m]iscarried’ ” because
it was “ ‘delayed.’ ” Muskogee Times-Democrat, June 15,
1934, p. 1. Another ran a story in which a correspondent’s
“letter miscarried and came too late.” Jersey City, N. J.,
The Evening Journal, June 10, 1907, p. 10. And a court de-
scribed mail mistakenly left “in the post office” as having
“miscarried.” Heinrich v. First Nat. Bank, 219 N. Y. 1, 4, 6,
113 N. E. 531, 531–532 (1916).
   We decline Konan’s invitations to “artificially narrow or-
dinary meaning.” Bartenwerfer v. Buckley, 598 U. S. 69, 77
(2023). A “miscarriage of mail” includes failure of the mail
to arrive at its intended destination, regardless of the car-
rier’s intent or where the mail goes instead.
                                B
   Konan’s withholding claims also arise out of the “loss” of
mail and are therefore within the postal exception. 28
U. S. C. §2680(b). When Congress enacted the FTCA, the
“loss” of mail ordinarily meant a deprivation of mail, re-
gardless of how the deprivation was brought about. So, like
“miscarriage,” intentional refusal to deliver mail could
cause the “loss” of mail.
   A “loss” of mail is a deprivation of mail. “Loss is a generic
and relative term; it is not a word of limited, hard and fast
meaning.” Black’s Law Dictionary 1094 (4th ed. 1968). But
                  Cite as: 607 U. S. ____ (2026)            9

                      Opinion of the Court

it is commonly used to refer to any “deprivation” or “that
which is withheld,” id., at 1095, such as when someone suf-
fers the loss of property in a fire or the loss of income from
being laid off. Webster’s defined “loss” as the “[a]ct or fact
of losing (in various senses) or suffering deprivation.” Web-
ster’s Second 1460. Oxford English Dictionary defined it as
“being deprived of, or the failure to keep” something. 6 Ox-
ford English Dictionary, at 452. One can, of course, suffer
a deprivation of something when another intentionally
keeps that thing for himself. Konan alleged that she was
“entitled to possession” of her mail but that the Postal Ser-
vice “converted” it. App. to Pet. for Cert. 58a–59a. Conver-
sion means that Konan was “deprived of the use and pos-
session of the property” in question. Black’s Law Dictionary
421 (12th ed. 2024). Konan’s claims therefore arise out of
the loss of her mail.
   As with “miscarriage,” we disagree with Konan’s attempt
to limit “loss” to only inadvertent losses. See Brief for Re-
spondent 27–28; post, at 6–7 (opinion of SOTOMAYOR, J.). A
loss can be the result of another person’s intentional mis-
conduct. One can, for example, suffer a tax “loss” that re-
sults from “embezzlement.” See, e.g., Burnet v. Huff, 288
U. S. 156, 160 (1933). An army can suffer “loss” of soldiers
as a result of the intentional conduct of the enemy. Funk &
Wagnalls New Standard Dictionary of the English Lan-
guage 1465 (1942 ed.). And, in the mail context, ordinary
speakers commonly described a “loss” of mail from theft, in-
cluding theft by the carrier. Just a year before Congress
enacted the FTCA, the Army explained that “[v]irtually all
loss of mail through theft occurs at terminal transfer points
outside this country.” Pittsfield, Mass., Berkshire Evening
Eagle, Feb. 9, 1945, p. 3 (emphasis added). A few years ear-
lier, a reported “[l]oss of [l]ocal [m]ail” was caused by a
rogue “mail handler, who admitted the theft of considerable
mail during the past few months.” Belvidere News, Dec. 3,
1936, p. 1. Pre-FTCA decisions also described a “loss” of
10               POSTAL SERVICE v. KONAN

                     Opinion of the Court

mail when the carrier stole it. E.g., Boerner v. United
States, 117 F. 2d 387, 387–388 (CA2 1941); Martin v.
United States, 280 F. 513, 514 (CA4 1922).
   We also disagree with Konan’s, and the dissent’s, rejoin-
der that the postal exception applies only when the Postal
Service lost the mail. See post, at 7–8. Congress could have
written the postal exception to apply only when “the Postal
Service lost, miscarried, or negligently transmitted” mail.
But Congress applied the postal exception to all “claim[s]
arising out of the loss, miscarriage, or negligent transmis-
sion” of mail. It described kinds of harms, not kinds of ac-
tions by the postal workers. See Dolan, 546 U. S., at 489;
contra, post, at 4 (opinion of SOTOMAYOR, J.). We decline to
rescue Konan’s claims by inserting the Postal Service as the
sentence’s subject and then converting the three nouns into
three verbs. Cf. Terry v. United States, 593 U. S. 486, 494
(2021) (“[W]e will not convert nouns to adjectives and vice
versa”).
   Our interpretation of “loss” is also consistent with the
principal provision of the FTCA. Under that provision, a
plaintiff must allege a “loss of property . . . caused by the
negligent or wrongful act or omission” of a federal em-
ployee. 28 U. S. C. §1346(b)(1). All agree that this provi-
sion includes losses caused by intentional misconduct and
does not require that the Government “lost” anything. Be-
cause Congress used “loss” in this sense in the FTCA’s prin-
cipal provision, our interpretation adheres to the unrebut-
ted presumption that “the term bears a consistent meaning
throughout” the FTCA. See Azar v. Allina Health Services,
587 U. S. 566, 576 (2019).
   Last, Konan proposes limiting “loss” to only “destruc-
tion.” She contends that the “primary” meaning of “loss” in
1946 was “destruction,” not any other kind of deprivation.
Brief for Respondent 25–26. But, as we have explained, or-
dinary speakers referred to “losses” of mail, even when the
mail was not destroyed. Judge Cardozo wrote that when an
                  Cite as: 607 U. S. ____ (2026)             11

                      Opinion of the Court

envelope fell behind a radiator in the post office, it caused
the “loss” of the checks inside even though they were later
recovered. Heinrich, 219 N. Y., at 4, 113 N. E., at 531. And,
contemporaneous regulations treated “loss” and “destruc-
tion” separately, not, as Konan suggests, synonymously.
See, e.g., Postal Laws and Regulations §159 (1940 ed.) (de-
laying certain procedures until officials have “determined
that such loss, destruction, or damage resulted from no
fault or negligence on the part of ” a postmaster). Konan
asserts that “destruction” was the “primary” meaning of
loss because it was listed as the first definition in dictionar-
ies. Brief for Respondent 25–26. But, “[a]lthough many
people assume that the first sense listed in a dictionary is
the ‘main’ sense, that is often quite untrue.” A. Scalia & B.
Garner, Reading Law: The Interpretation of Legal Texts
418 (2012). The definitions Konan pointed to were listed
first because they were the oldest, not because they were
primary. See 1 Oxford English Dictionary, at xxxi (“[T]hat
sense is placed first which was actually the earliest in the
language . . . ”); 1 New Century Dictionary, at iii (“In gen-
eral, the senses of each word are arranged, as far as possi-
ble, in the order of their derivation and development from
the original source . . . ”); Webster’s New International Dic-
tionary ix (1927) (following “[ t]he principle of historical ar-
rangement followed in the earlier editions”). We do not pre-
sume that Congress intended the oldest usage, but rather
the ordinary one in 1946, and contemporaneous evidence
shows that Konan’s usage was not the primary one.
                            III
  Konan proffers two remaining arguments that her claims
must not be barred by the postal exception. We address
them in turn.
  First, Konan argues that the postal exception’s “negligent
transmission” category narrows the meaning of “miscar-
riage” and “loss.” She argues that the qualifier “negligent”
12               POSTAL SERVICE v. KONAN

                      Opinion of the Court

in the term “negligent transmission” implicitly qualifies the
other two terms. But Congress intentionally limited the
“negligent” qualifier to “transmission” and did not use it to
qualify “loss” or “miscarriage.” Konan’s “argument seems
to assume that pairing a broad statutory term with a nar-
row one shrinks the broad one, but there is no such general
usage.” S. D. Warren Co. v. Maine Bd. of Environmental
Protection, 547 U. S. 370, 379 (2006). Just like “a limiting
clause or phrase . . . should ordinarily be read as modifying
only the noun or phrase that it immediately follows,” an ad-
jective before the final noun in a list cannot be transplanted
to qualify the preceding nouns. Barnhart v. Thomas, 540
U. S. 20, 26 (2003). We also do not think that the “negli-
gent” qualifier suggests that Congress was trying to enable
suits involving intentional misconduct. Contra, post, at 5–
6 (opinion of SOTOMAYOR, J.). If Congress had written the
postal exception to refer to all “transmission” of mail, the
category—unlike “miscarriage” and “loss”—would have en-
compassed claims that involved mail even though nothing
went wrong with its transport or delivery. See Dolan, 546
U. S., at 486 (acknowledging the broad meaning of “trans-
mission” in isolation). The inclusion of “negligent” to qual-
ify “transmission” forecloses that result and thereby keeps
the focus of the postal exception on mail-delivery problems,
but, in doing so, it does not limit the other two categories.
   Second, Konan argues that our interpretations of “mis-
carriage” and “loss” run afoul of the presumption against
surplusage. On our interpretation, she argues, many
claims—including Konan’s here—will arise from both a
“miscarriage” and a “loss” of mail, making one or the other
redundant. To solve the surplusage, Konan proposes three
nonoverlapping definitions: “Loss” covers “damage” to mail;
“miscarriage” covers “what happens” to mail “when it leaves
the USPS’s custody and ends up in the wrong place”; and
“negligent transmission” covers “detention or delays of the
mail while still in the USPS’s possession.” Brief for
                  Cite as: 607 U. S. ____ (2026)                 13

                      Opinion of the Court

Respondent 9. Konan’s proposal is inconsistent with ordi-
nary meaning, which shows that these terms were often
used in an overlapping manner. See, e.g., Heinrich, 219
N. Y., at 4–6, 113 N. E., at 531–532 (describing “[t]he loss
of the checks” that “miscarried in the mails”); Brevard v.
Wimberly, 89 Mo. App. 331, 338–339 (1901) (“miscarriage
of . . . packages” could lead to “the loss of a registered pack-
age”). And, in Dolan, the Court interpreted the terms in the
postal exception to substantially overlap. See 546 U. S., at
487. The canon against surplusage is subordinate to the
“cardinal canon” that “a legislature says in a statute what
it means and means in a statute what it says there.” Con-
necticut Nat. Bank v. Germain, 503 U. S. 249, 253–254
(1992). We think that Congress likely used broad, overlap-
ping terms to better keep complaints about mail delivery
out of court.
                            IV
  We hold that the postal exception covers suits against the
United States for the intentional nondelivery of mail. We
do not decide whether all of Konan’s claims are barred by
the postal exception, or which arguments Konan ade-
quately preserved. We vacate the judgment of the Court of
Appeals and remand the case for further proceedings con-
sistent with this opinion.
                                                   It is so ordered.
                  Cite as: 607 U. S. ____ (2026)             1

                    SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 24–351
                          _________________


      UNITED STATES POSTAL SERVICE, ET AL.,
          PETITIONER v. LEBENE KONAN
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE FIFTH CIRCUIT
                      [February 24, 2026]

  JUSTICE SOTOMAYOR, with whom JUSTICE KAGAN,
JUSTICE GORSUCH, and JUSTICE JACKSON join, dissenting.
  For two years, respondent Lebene Konan and her tenants
did not receive mail addressed to the rental properties that
Konan owned. According to Konan, negligence was not to
blame. Quite the opposite: She alleges that United States
Postal Service employees intentionally withheld delivery
because they did not like “ ‘that a black person own[ed]’ ” the
properties and “ ‘lease[d] rooms . . . to white people.’ ” 652
F. Supp. 3d 721, 725 (ND Tex. 2023).
  Konan brought this action under the Federal Tort Claims
Act (FTCA) against the United States to recover damages
she sustained as a result of this alleged years-long harass-
ment campaign. The United States is generally protected
by sovereign immunity, but Congress, through the FTCA,
has enacted a capacious waiver of that immunity for tort
suits when an individual is harmed by a federal employee
acting within the scope of her employment. That waiver,
however, is subject to several exceptions. Today, the Court
holds that one exception—the postal exception—prevents
individuals from recovering for injuries based on a postal
employee’s intentional misconduct, including when an em-
ployee maliciously withholds their mail. Because this read-
ing of the postal exception transforms, rather than honors,
the exception Congress enacted, I respectfully dissent.
2                POSTAL SERVICE v. KONAN

                    SOTOMAYOR, J., dissenting

                               I
   The FTCA serves a simple purpose: “ ‘to remove the sov-
ereign immunity of the United States from suits in tort.’ ”
Levin v. United States, 568 U. S. 503, 506 (2013). This
“broad waiver” of immunity, Millbrook v. United States, 569
U. S. 50, 52 (2013), allows an individual harmed by a fed-
eral employee “acting within the scope of his office or em-
ployment” to recover for “injury or loss of property, or per-
sonal injury or death caused by the” employee’s “negligent
or wrongful act or omission,” 28 U. S. C. §1346(b)(1); see
United States v. Yellow Cab Co., 340 U. S. 543, 547 (1951)
(describing the waiver as “sweeping”).
   Congress has also enacted several exceptions preserving
the United States’ immunity in some circumstances. See
§2680 (listing 13 such exceptions). The exceptions “are de-
signed to protect certain important governmental functions
and prerogatives from disruption.” Molzof v. United States,
502 U. S. 301, 311 (1992). They thus “mark the ‘boundary
between Congress’ willingness to impose tort liability upon
the United States and its desire to protect certain govern-
mental activities from exposure to suit by private individu-
als.’ ” Ibid.
   At the same time, courts must be careful not to interpret
these exceptions too broadly. “‘[U]nduly generous interpre-
tations,’ ” this Court has warned, “ ‘run the risk of defeating
the central purpose of the statute’”—to “ ‘waiv[e] the Gov-
ernment’s immunity from suit in sweeping language.’ ” Do-
lan v. Postal Service, 546 U. S. 481, 492 (2006) (quoting
Kosak v. United States, 465 U. S. 848, 853, n. 9 (1984); Yel-
low Cab, 340 U. S., at 547). To harmonize these considera-
tions, “ ‘the proper objective of a court attempting to con-
strue one of the’” exceptions “ ‘is to identify those
circumstances which are within the words and reason of the
exception—no less and no more.’ ” Dolan, 546 U. S., at 492
(quoting Kosak, 465 U. S., at 853–854, n. 9 (some internal
quotation marks omitted)).
                  Cite as: 607 U. S. ____ (2026)            3

                   SOTOMAYOR, J., dissenting

   This case calls on the Court to interpret the postal excep-
tion, which covers “[a]ny claim arising out of the loss, mis-
carriage, or negligent transmission of letters or postal mat-
ter.” §2680(b). The wording of this exception is noticeably
narrower than some of its neighbors. For example, all
claims for “damages caused by the fiscal operations of the
Treasury or by the regulation of the monetary system” are
barred. §2680(i). So too are all “claim[s] arising from the
activities of the Tennessee Valley Authority,” the “Panama
Canal Company,” and “a Federal Bank, a Federal interme-
diate credit bank, or a bank for cooperatives,” §§2680(l),
(m), (n).
   By comparison, Congress did not paint with as broad of a
brush in designing the postal exception. Like it had for
these other agencies and activities, Congress could have
granted immunity for all “claims arising from the mail ac-
tivities of the Postal Service.” Instead, Congress identified
certain “misconduct for which the Government was not as-
suming financial responsibility—namely, ‘the loss, miscar-
riage, or negligent transmission of letters or postal mat-
ter.’ ” Kosak, 465 U. S., at 855. By using “specificity” over
“generality,” it follows that Congress intended for this ex-
ception “to be less encompassing” than the coverage pro-
vided by the broader exceptions, and for the Government to
“assum[e] financial responsibility” for certain classes of
“misconduct” related to postal activities. Ibid.
   This Court has already identified some of those classes.
In Kosak, the Court explained that claims arising from car
accidents caused by postal employees delivering mail fall
outside the exception. Ibid. In Dolan, the Court recognized
a second class of claims for slip and falls caused by an em-
ployee negligently placing a package on a porch step. 546
U. S., at 483. Today, I would have affirmed the Fifth Cir-
cuit’s well-reasoned decision that acknowledged a third
class: claims concerning intentional misconduct committed
4                POSTAL SERVICE v. KONAN

                   SOTOMAYOR, J., dissenting

by postal employees, which would necessarily include with-
holding a person’s mail for malicious reasons.
                               II
                               A
   The postal exception’s text shows that Congress did not
intend to immunize intentional misconduct. Recall that the
exception covers the “loss,” “miscarriage,” and “negligent
transmission” of mail. §2680(b). As Kosak observed, the
terms describe three categories of “misconduct” that postal
employees can commit without incurring liability for the
United States. 465 U. S., at 855. The majority, however,
contends that these terms focus on “harms” rather than
Government wrongdoing, citing Dolan. Ante, at 2, 5, 10. To
be sure, Dolan described these terms as “harm[s],” but in
the same breath, it also emphasized that the three terms
protect “only a subset of postal wrongdoing.” 546 U. S., at
490.
   A focus on misconduct is consistent with most other
FTCA exceptions, which generally are triggered by certain
types of Government conduct, rather than the type of harm
the plaintiff experiences. For instance, some exceptions di-
rectly cover different “act[s] or omission[s]” of Government
employees, §§2680(a) (discretionary acts), (e) (administer-
ing §§1–31 of Title 50). Another addresses intentional ac-
tions by employees, capturing, for example, assault, bat-
tery, false imprisonment, and other intentional torts like
them. §2680(h). A different group immunizes the “activi-
ties” of a given Government instrumentality. §§2680(j), (l),
(m), (n). Yet a different subset describes a specific type of
Government action, such as the “assessment or collection of
any tax or customs duty,” §2680(c), the “imposition or es-
tablishment of a quarantine,” §2680(f ), and the “fiscal op-
erations of the Treasury,” §2680(i). The focus of each is on
the Government conduct. The same is necessarily true of
the postal exception.
                      Cite as: 607 U. S. ____ (2026)                     5

                       SOTOMAYOR, J., dissenting

  The key question is thus as follows: What kind of miscon-
duct falls within the “ ‘words and reason’ ” of the postal ex-
ception? Dolan, 546 U. S., at 492 (quoting Kosak, 465 U. S.,
at 854, n. 9). All signs point to Congress leaving intentional
misconduct outside of the exception’s scope.
                              1
   Begin with “negligent transmission.” This term covers
“negligence causing mail to be lost or to arrive late, in dam-
aged condition, or at the wrong address.” Dolan, 546 U. S.,
at 486. It goes without saying that this term therefore does
not immunize intentional misconduct.
   Beyond that basic insight, however, Congress’s express
inclusion of “negligent transmission” provides other im-
portant clues for deciphering statutory meaning about the
scope of the postal exception. As the majority recognizes, if
Congress had included all claims arising out of the “trans-
mission” of mail in the postal exception, the term “would
have encompassed claims that involved mail even though
nothing went wrong with its transport or delivery.” Ante,
at 12. To avoid that outcome, Congress needed to add a
narrowing modifier to focus on when things go wrong.1
   Critically, Congress did not have to choose “negligent” as
that modifier (or the only modifier). Congress could have,
for example, modified “transmission” with both “negligent”
and “wrongful.” Doing so would have avoided the problem
the majority identifies while also clarifying that both clas-
ses of conduct fall within the exception’s scope. Yet Con-
gress elected to immunize negligent conduct alone. Its
choice to do so carries significance. It raises the natural
inference that Congress intended for at least some inten-
tional wrongdoing related to transmitting mail to fall out-
side the scope of the exception.
——————
  1 Congress did not need to add “negligent” before “miscarriage” or “loss”

because the ordinary meaning of those terms, plus statutory context, con-
vey inadvertence on their own. See infra, at 6–12.
6                  POSTAL SERVICE v. KONAN

                     SOTOMAYOR, J., dissenting

   Indeed, before this Court, the Government emphasizes
repeatedly that “negligent transmission” is “significant” be-
cause the term “shows that Congress knew how to exclude
intentional conduct when it wanted to.” Brief for Petition-
ers 3, 17, 35. Yet, according to the Government and the
majority, this was a hollow choice. In their view, Congress
excluded some set of intentional conduct through the “neg-
ligent transmission” modifier only to sweep that conduct
back into the exception through “miscarriage” and “loss.”
The majority adopts the Government’s definition of “mis-
carriage” as capturing situations where “mail fail[s] to ar-
rive properly,” regardless of the actor’s intent. Ante, at 6.
It also adopts the Government’s definition of “loss” as cap-
turing the “deprivation of mail,” regardless, again, of the
depriver’s intent. Ante, at 8. It is difficult to see how a
postal employee could intentionally transmit mail wrong-
fully—such as by refusing to deliver the mail, lighting it on
fire, or shredding it into pieces—without falling within
these definitions of “miscarriage” or “loss.” In this world,
Congress did not even need to bother with the modifier to
transmission that it adopted.
   Congress did not make this odd choice. As explained be-
low, “loss” and “miscarriage,” as used in the postal excep-
tion, do not capture intentional misconduct either.
                                2
   Turn, then, to “loss.” As the Government acknowledged
in its petition for certiorari, “loss” is ordinarily understood
to capture unintentional conduct. Pet. for Cert. 14; see also
Webster’s New International Dictionary 1460 (2d ed. 1934)
(defining “loss” as an “[a]ct or fact of losing . . . esp[ecially],
unintentional parting with something of value”). For good
reason: As the Fifth Circuit observed below, “no one inten-
tionally loses something.” 96 F. 4th 799, 802 (2024). People
lose their keys when they misplace them, not when they
give them to their children. People lose their mail when it
                     Cite as: 607 U. S. ____ (2026)                    7

                       SOTOMAYOR, J., dissenting

gets stuck behind a drawer, not when they intentionally
throw it away. If someone said that they “lost” their car, no
one would think it was stolen, only that the person forgot
where they had parked it. The same is true when the Postal
Service loses someone’s mail. The reason is an error, not
deliberate wrongdoing.
   To reach its contrary result, the majority defines “loss” as
any “deprivation of mail,” which it concludes captures all
situations where the individual does not receive mail, no
matter the cause. Ante, at 8. To do so, however, the major-
ity must shift away from a focus on harms that befall the
mail to harms that befall Konan. The majority says that
the postal exception encompasses three “kinds of harms,
not kinds of actions by the postal workers.” Ante, at 10. The
majority defines the first two terms, “miscarriage” and
“negligent transmission,” to encompass “harms” to the mail.
Yet, under the majority’s interpretation, “loss” is an en-
tirely distinct kind of “harm.” That is because the mail does
not “suffer a deprivation” in the same way that mail fails to
arrive (miscarriage) or mail is damaged due to negligence
(negligent transmission). The only way “loss” could mean a
“deprivation” is if it were a harm experienced by Konan, not
by the mail. No such inconsistency, however, arises if (as
explained above) all three terms are read to refer to the
Government’s misconduct: the Postal Service’s loss, miscar-
riage, or negligent transmission of mail. See supra, at 4–5.
When used in this sense, “loss” plainly and sensibly denotes
unintentional conduct, consistent with its ordinary mean-
ing.2
——————
  2 The Government also contends that “loss” in the postal exception in-

corporates intentional misconduct because it asks “whether the alleged
victims ‘lost’ mail.” Brief for Petitioners 41 (emphasis deleted); Tr. of
Oral Arg. 21 (same). That again requires the same shift in perspective:
asking, on one hand, whether mail was “miscarr[ied]” or “negligently
transmitted” by the Postal Service, and, on the other hand, whether Ko-
nan “los[t]” (and so was deprived of ) her mail.
8                 POSTAL SERVICE v. KONAN

                    SOTOMAYOR, J., dissenting

   The majority also invokes the presumption of consistent
usage. It points to the use of “loss” in the FTCA’s sovereign
immunity waiver as meaning “deprivation,” and argues
that “loss” as used in the postal exception must take on the
same meaning. Ante, at 10. The consistent-usage canon,
however, “ ‘readily yields’ to context,” Utility Air Regulatory
Group v. EPA, 573 U. S. 302, 320 (2014), and here, compar-
ing the context of the FTCA’s waiver to the context of the
postal exception shows that “loss” is being used in two dif-
ferent ways.
   The waiver uses “loss” to describe the form of damages an
individual harmed by a federal employee can seek to re-
cover. It states that plaintiffs can bring claims against the
United States for “loss of property” “caused by the negligent
or wrongful act or omission of any employee of the Govern-
ment” while acting within the scope of their employment.
§1346(b)(1). The plaintiff ’s “loss” could be due to “negligent
or wrongful” conduct, as the waiver states explicitly. Ibid.
In contrast, the postal exception uses “loss” to describe the
form of the employee’s misconduct that is protected from
liability. If an employee lost the mail, the plaintiff suffered
a “loss” under the waiver and the claim arose “out of the
loss” of the mail, meaning the postal exception applies. If
an employee intentionally destroyed the mail, the waiver
would still be implicated because the plaintiff suffered a rel-
evant “loss” for purposes of the waiver. The postal excep-
tion would not apply, however, because the employee de-
stroyed the mail and did not lose it. “Loss” is thus being
clearly used in two different ways and carries two different
meanings.
                                3
  That brings us to “miscarriage.” The majority is correct
that “miscarriage” covers misconduct by the Postal Service
that causes mail to “fai[l] to arrive properly,” ante, at 6, but
                     Cite as: 607 U. S. ____ (2026)                    9

                       SOTOMAYOR, J., dissenting

the majority is wrong to extend this meaning to cover situ-
ations that involve intentional misconduct.
   As the majority recognizes, “miscarriage” commonly co-
vers negligence or inadvertence. Ante, at 7. Indeed, there
are many examples of “miscarriage” being used when mail
“fails to arrive” due to negligence, including as illustrated
by the Government’s own cases. See, e.g., Heinrich v. First
Nat. Bank, 219 N. Y. 1, 113 N. E. 531, 531–532 (1916); Elam
v. St. Louis & S. F. R. Co., 117 Mo. App. 453, 93 S. W. 851
(1906); see n. 3, infra. From here, as the majority sees it,
mail that is intentionally not delivered, even for malicious
reasons, also “failed to arrive properly,” so Congress must
have intended to include intentional misconduct within the
exception by using “miscarriage.” Ante, at 6. The majority,
however, offers no persuasive evidence suggesting that
“miscarriage” is commonly used in this way.
   To start, the majority relies on several dictionary defini-
tions. Ante, at 6–7. None of those definitions addresses an
individual’s mens rea. The phrase “failure to arrive,” more-
over, does not immediately suggest intentional wrongdoing.
“A diplomat might ‘fail to arrive’ at a treaty negotiation if
her flight were cancelled, but no one would describe her as
‘failing to arrive’ if she deliberately skipped the talks to un-
dermine the treaty (‘refused to attend’ would be more accu-
rate).” Brief for Respondent 23.
   Next, the majority turns to real-life examples. Here, the
majority does not rely on any cases cited by the Govern-
ment. That is not a surprise, as the Government failed to
identify a single example of “miscarriage” being used to de-
scribe mail “failing to arrive properly” due to intentional
misconduct.3 The majority thus searches elsewhere, citing
——————
   3 See Reply Brief 8–10 (citing Bowen v. Wilson, 15 F. 2d 733, 734 (DC

1926) (“miscarriage” when delivery was attempted but returned because
the recipient could not be found); Heinrich v. First Nat. Bank, 219 N. Y.
1, 113 N. E. 531, 531–532 (1916) (mail was “miscarried” when it was mis-
placed behind a radiator due to “the negligence of employees of the post-
10                   POSTAL SERVICE v. KONAN

                       SOTOMAYOR, J., dissenting

examples of its own: two cherry-picked newspaper refer-
ences almost 20 years apart, and at least 30 years before
the enactment of the FTCA, that used “miscarried,” not
“miscarriage.” Ante, at 7–8. If “miscarriage” were in fact
ordinarily used to describe intentional misconduct, one
might expect that actual examples of the usage would be
easier to come by.
   The majority also cites cases in which the reason behind
a “miscarriage” was not identified, but those cases do not
support its position. Ante, at 7–8. How a word is used when
the cause is unknown hardly informs whether an ordinary
speaker would use the same word when the cause is known.
Those cases, moreover, simply reflect the general presump-
tion that issues with mail are typically not a result of inten-
tional misconduct by postal workers. For example, in Lake
v. Lake, 63 Wyo. 375, 182 P. 2d 824 (1947) (per curiam), the
court explained that when a motion arrived in court “a day
too late” due to a “miscarriage of the mails,” with no further
cause explained, that “ ‘mere accident’ ” should not be held
against the party. Id., at 402, 182 P. 2d, at 835. Similarly,
in Wagner v. Lucas, 79 Okla. 231, 193 P. 421 (1920), the
court described “miscarriage of the mails” as a situation
that “human prudence, foresight, and sagacity . . . could not
——————
office”); Southern Express Co. v. Hill, 81 Ark. 1, 98 S. W. 371, 372–373
(1906) (“miscarriage” due to the sender mistakenly writing the wrong
address); Elam v. St. Louis & S. F. R. Co., 117 Mo. App. 453, 93 S. W.
851 (1906) (“miscarriage” due to the “negligence” of the postal carrier);
Western Home Ins. Co. v. Richardson, 40 Neb. 1, 58 N. W. 597, 598 (1894)
(cause unknown); Fosters v. McKibben, 14 Pa. 168, 170 (1850) (describing
a letter that “miscarrie[s] for want of publication”); People ex rel.
Holdsworth v. Superior Ct., 18 Wend. 675, 678 (N. Y. Sup. Ct. 1837)
(cause unknown)). See also Missouri, K. & T. R. Co. v. Ellis, 53 Okla.
264, 156 P. 226, 228 (1916) (although the cause of the mail arriving late
was unknown, the court referred to the “miscarriage of the mail” as an
“accident”); Kellogg v. Smith, 171 Okla. 355, 42 P. 2d 493, 495 (1935) (per
curiam) (similar); Hogan v. Bailey, 27 Okla. 15, 110 P. 890, 891 (1910)
(similar); Chichester v. Cande, 3 Cow. 39, 48 (N. Y. Sup. Ct. 1824) (simi-
lar).
                  Cite as: 607 U. S. ____ (2026)           11

                   SOTOMAYOR, J., dissenting

prevent,” like a “mistake in the wording of a telegram.” Id.,
at 232–233, 193 P., at 423. Accordingly, the use of the term
“miscarriage” in these cases does not prove that the term
covers intentional misconduct; in context, had the courts
suspected that the late delivery, for instance, was a result
of such misconduct, they likely would have used a different
word.
   The contemporaneous Postal Laws and Regulations from
before the FTCA was enacted—the “backdrop” against
which “Congress enacted the postal exception,” Brief for Pe-
titioners 35—further undermine the majority’s interpreta-
tion. For example, those regulations directed the Division
of Stamps to make adjustments in “cases of loss, miscar-
riage, or detention of stamped supplies in transit.” Post Of-
fice Dept., Postal Law & Regs. §13.6 (1940 ed.). This sug-
gests that when the stamped supplies were intentionally
held back and not delivered (i.e., failed to arrive), “deten-
tion” was used instead of “miscarriage,” even though, on the
majority’s reading, “miscarriage” would have sufficed. The
regulations also directed postal employees to “hold” pack-
ages dropped off for “forwarding” if they contained “destruc-
tive mail matter,” to “notify the sender” of the “detention of
the package,” and to let them know it cannot be “trans-
ported by mail.” §728. This is another use of “detention” in
the context where, under the majority’s view, “miscarriage”
would have been appropriate because the mail “failed to ar-
rive” at its destination. Yet, in each, the cause of the non-
delivery was known, it was not inadvertence, and a differ-
ent term was used.
   At most, the majority shows that certain dictionary defi-
nitions of “miscarriage” could conceivably capture inten-
tionally withholding mail, or tearing up a letter into pieces,
or lighting a package on fire—in all those situations, the
mail “failed to arrive properly.” Ante, at 6. “That a defini-
tion is broad enough to encompass one sense of a word,”
however, “does not establish that the word is ordinarily
12               POSTAL SERVICE v. KONAN

                   SOTOMAYOR, J., dissenting

understood in that sense.” Taniguchi v. Kan Pacific Sai-
pan, Ltd., 566 U. S. 560, 568 (2012). Here, neither the ma-
jority nor the Government has offered any meaningful evi-
dence supporting the view that “miscarriage” was
commonly used in situations when the mail failed to arrive
properly due to intentional wrongdoing, and that, by includ-
ing “miscarriage” within the postal exception, Congress in-
tended to capture such wrongdoing.
   If there were any doubt, the words surrounding “miscar-
riage” resolve it. As the Court in Dolan explained, when
construed in context, “[a] word in a statute may or may not
extend to the outer limits of its definitional possibilities.”
546 U. S., at 486. For example, “ ‘[a] word is known by the
company it keeps,’ ” and “ ‘[w]ords grouped in a list should
be given related meaning.’ ” Id., at 486–487. Without this
rule, courts risk “ ‘ascribing to one word a meaning so broad
that it is inconsistent with its accompanying words, thus
giving unintended breadth to the Acts of Congress.’ ” Yates
v. United States, 574 U. S. 528, 543 (2015) (plurality opin-
ion).
   Here, reading “miscarriage” to capture intentional mis-
conduct does precisely that. As noted above, the word “loss”
typically connotes negligence, see supra, at 6–7, and the
majority’s reading makes Congress’s specific inclusion of
the “negligent” modifier for “transmission” entirely ineffec-
tive at serving its purpose—excluding intentional miscon-
duct. See supra, at 5–6. There also does not appear to be
any good reason why Congress would have wanted one term
(“miscarriage,” alone) to cover intentional misconduct and
not the other two terms. Indeed, under the majority’s broad
definition of “miscarriage,” the words “loss” and “negligent
transmission” become no more than “misleading surplus-
age.” Yates, 574 U. S., at 546.
                       Cite as: 607 U. S. ____ (2026)                        13

                         SOTOMAYOR, J., dissenting

                              B
    For all these reasons, a faithful interpretation of the
postal exception leads to the conclusion that intentional
misconduct is excluded from its reach. Congress used “over-
lapping” terms in the exception, ante, at 13, but Congress
intended for that overlap to keep claims alleging negli-
gence, not intentional wrongdoing, out of court. This read-
ing gives meaning to Congress’s choice to put “negligent”
before “transmission” and to use the words “miscarriage”
and “loss” in their common understanding, and it respects
the “specificity” Congress used in the postal exception as
compared to the broadly worded exceptions Congress used
for other agencies. Kosak, 465 U. S., at 855.
    Undeterred by this evidence, the majority gives the
Postal Service the blanket exception Congress withheld. In
its view, the exception immunizes the agency for all inten-
tional and nonintentional actions in the delivery of mail
(apart from auto accidents and slip and falls, as Dolan and
Kosak require). Relying on “loss, miscarriage, and negli-
gent transmission” is an odd way to cover this waterfront.
If Congress had intended this outcome, why not follow the
same approach that it used for other broad exceptions in the
FTCA? See supra, at 3. The answer is that Congress in-
tended no such thing. By expanding the “words and reason”
of the postal exception beyond their “specifi[c]” scope,
Kosak, 565 U. S., at 855, the majority undermines the
“ ‘sweeping’ ” waiver of immunity Congress adopted, Dolan,
546 U. S., at 492.
    Contrary to the majority’s suggestion otherwise, adher-
ing to the text Congress enacted would not flood the Gov-
ernment or courts with frivolous lawsuits.4 That is because
——————
  4 The majority points to the 335,000 complaints filed with the Postal

Service each year to suggest that those claims arise out of mail failing to
“arriv[e] properly and on time.” Ante, at 2. This is misleading. As Konan
explains, those complaints include “everything from ‘[r]ude or unprofes-
sional . . . employee behavior’ to ‘[c]omplaints about . . . vehicle parking.’ ”
14                   POSTAL SERVICE v. KONAN

                       SOTOMAYOR, J., dissenting

the FTCA has additional safeguards that bar many claims
premised on intentional misconduct. Liability for the
United States will arise only in the rare situation in which
the employee’s intentional conduct is tortious, falls within
the scope of her employment, and falls outside of the due-
care and discretionary-function exceptions. See 28 U. S. C.
§2680(a). For example, the majority cites one case of an
insurance company suing after a federal employee stole an
expensive package it had insured, see ante, at 6, but most
States likely do not consider intentional torts like theft to
fall within an individual’s scope of employment, see Re-
statement (Second) of Agency §228 (1957) (torts fall outside
the scope of employment when they are “too little actuated
by a purpose to serve” the employer); Brief for Respondent
43, n. 21 (collecting cases where theft fell outside the scope
of employment). The United States, accordingly, would not
incur liability in those circumstances or others involving
claims of similar misconduct.
   In addition, there are ordinary litigation tools to prevent
any threat of abuses, from Rule 11 of the Federal Rules of
Civil Procedure to the plausibility standards in Bell Atlan-
tic Corp. v. Twombly, 550 U. S. 544 (2007), and Ashcroft v.
Iqbal, 556 U. S. 662 (2009). These tools suffice in many
other circumstances where the threats of disruption posed
by large volumes of litigation are also high. Other excep-
tions, like the intentional-tort exception, §2680(h), and the
due-care exception, §2680(a), turn on Government officials’
mens rea, and courts are well equipped to assess the plau-
sibility of any given case based on the facts before them.

——————
Brief for Respondent 43. Submitting a “ ‘customer complaint,’ ” moreo-
ver, requires “typing a few sentences into an online form,” whereas “[f]il-
ing an FTCA claim requires first exhausting administrative remedies
and then filing suit in court.” Ibid. The raw number of complaints there-
fore does not provide an accurate gauge of the consequences for recogniz-
ing that intentional misconduct does not fall within the postal exception.
                  Cite as: 607 U. S. ____ (2026)            15

                    SOTOMAYOR, J., dissenting

   Finally, even if ruling for Konan today would mean more
suits against the Government for mail-related intentional
torts tomorrow, that would not provide this Court with au-
thority to change the text Congress enacted. Ultimately,
this regime is the consequence of Congress’s choice to have
the exception turn on certain types of misconduct, rather
than providing the Postal Service with a blanket exception.
It is not the role of the Judiciary to supplant the choice Con-
gress made because it would have chosen differently.
                         *    *    *
   Today, the majority concludes that the postal exception
captures, and therefore protects, the intentional nondeliv-
ery of mail, even when that nondelivery was driven by ma-
licious reasons. Because this interpretation expands the
scope of the exception beyond what it can reasonably sup-
port, and undermines the FTCA’s sweeping waiver in the
process, I respectfully dissent.

```

---

## GROUP: _overhaul2/lake/cases/Preston v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Preston v. United States"
type: case
citation: "376 U.S. 364 (1964)"
parallel_cite: "84 S. Ct. 881; 11 L. Ed. 2d 777"
neutral_cite: 1964 U.S. LEXIS 1578
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-03-23
docket: 163
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-03-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Preston v. United States
  varies_by_point: false
  scope_note: "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing — not overruling — Preston, so it no longer implies every station-house car search is unreasonable."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106771/preston-v-united-states/"
  cluster_id: 106771
  opinion_id: 106771
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Historical"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Chambers v. Maroney]]", "[[Chimel v. California]]", "[[Agnello v. United States]]", "[[United States v. Chadwick]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search", "warrant-requirement"]
holding: "A warrantless search of a vehicle is not a valid search incident to arrest once the arrestee is in custody and the car has been removed; a search remote in time or place from the arrest cannot be justified as incident to it."
lake:
  record_id: Preston v. United States
  status: verified
  projected_at: 2026-07-09
---

# Preston v. United States

*376 U.S. 364 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police received a 3 a.m. complaint about three suspicious men who had been sitting in a parked car for hours in a business district. Officers questioned the men, found their answers evasive, learned all three were unemployed with 25 cents among them, and arrested them for vagrancy. The men were searched for weapons and taken to the station; the car, unsearched at the scene, was driven to the station and then towed to a garage. After the men were booked, officers searched the car at the garage, finding loaded revolvers in the glove compartment and — after forcing into the trunk — robbery paraphernalia (a stocking mask, rope, a fake license plate). The items were used to convict petitioner of conspiracy to rob a bank.

## Issue
May a warrantless search of a car at a garage — conducted after the arrestees were in custody at the station and the car had been towed — be justified as a search incident to the arrest?

## Rule
No. A [[Search Incident to Arrest|search incident to arrest]] must be contemporaneous, and "[o]nce an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." — 376 U.S. at 367. ^pin-367

The officer-safety and evidence-preservation "justifications are absent where a search is remote in time or place from the arrest." — [*Id.*](https://www.courtlistener.com/opinion/106771/preston-v-united-states/#:~:text=justifications%20are%20absent%20where%20a) ^pin-367b

On these facts, "the search was too remote in time or place to have been made as incidental to the arrest . . . , [so] the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained . . . inadmissible." — *Id.* at 368. ^pin-368

## Application
The car was not searched until the men had been arrested, booked, and taken into custody at the station, and the car had been towed to a garage. At that point none of the arrestees could have reached a weapon in the car or destroyed evidence, and there was no danger the car would be moved out of the locality. The search was therefore too remote in time and place from the arrest to qualify as incident to it, and no warrant had been obtained.

## Conclusion
The warrantless garage search of the car was unreasonable and its fruits inadmissible. The judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Preston* remains a controlling statement of the temporal/spatial limit on [[Search Incident to Arrest|searches incident to arrest]], regularly cited (e.g., in [[United States v. Chadwick]]). It was decided solely on search-incident grounds; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) **distinguished** *Preston* and now independently permits a warrantless delayed vehicle search on probable cause — so *Preston* does not bar every station-house car search, but its search-incident holding is intact and not overruled.

## Appears on
- [[SIA Persons]] — *Historical*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Preston v. United States*, 376 U.S. 364 (1964) — https://www.courtlistener.com/opinion/106771/preston-v-united-states/ — pinpoints: 367, 368.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d102ae478c242f60", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Preston v. United States"}, "payload": {"all": [{"cite": "376 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "376"}, {"cite": "84 S. Ct. 881", "page": "881", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "11 L. Ed. 2d 777", "page": "777", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "11"}, {"cite": "1964 U.S. LEXIS 1578", "page": "1578", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "376 U.S. 364", "official": {"cite": "376 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "376"}, "official_selection_present": true, "record_id": "Preston v. United States"}}
{"assertion_id": "8b5467cb9f8bdc03", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-368", "record_id": "Preston v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-368", "pinpoint_status": "slip-only", "quote": "the search was too remote in time or place to have been made as incidental to the arrest . . . , [so] the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained . . . inadmissible.", "quote_fidelity": "mismatch", "record_id": "Preston v. United States", "star_marker": null}}
{"assertion_id": "8dce0920b2eabcca", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-367b", "record_id": "Preston v. United States"}, "payload": {"fragment": "#:~:text=justifications%20are%20absent%20where%20a", "page": null, "pin_id": "pin-367b", "pinpoint_status": "star-verified", "quote": "justifications are absent where a search is remote in time or place from the arrest.", "quote_fidelity": "matched", "record_id": "Preston v. United States", "star_marker": "367"}}
{"assertion_id": "e5f664f222c7c86b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-367", "record_id": "Preston v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-367", "pinpoint_status": "slip-only", "quote": "--- # Preston v. United States *376 U.S. 364 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received a 3 a.m. complaint about three suspicious men who had been sitting in a parked car for hours in a business district. Officers questioned the men, found their answers evasive, learned all three were unemployed with 25 cents among them, and arrested them for vagrancy. The men were searched for weapons and taken to the station; the car, unsearched at the scene, was driven to the station and then towed to a garage. After the men were booked, officers searched the car at the garage, finding loaded revolvers in the glove compartment and — after forcing into the trunk — robbery paraphernalia (a stocking mask, rope, a fake license plate). The items were used to convict petitioner of conspiracy to rob a bank. ## Issue May a warrantless search of a car at a garage — conducted after the arrestees were in custody at the station and the car had been towed — be justified as a search incident to the arrest? ## Rule No. A search incident to arrest must be contemporaneous, and", "quote_fidelity": "mismatch", "record_id": "Preston v. United States", "star_marker": null}}
{"assertion_id": "c99ed8fdcd0128e0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Preston v. United States"}, "payload": {"as_of_content": "1964-03-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Preston v. United States", "scope_note": "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing — not overruling — Preston, so it no longer implies every station-house car search is unreasonable.", "varies_by_point": false}}
```

### lake record — Preston v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Preston v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Preston v. United States",
    "case_name_short": "Preston",
    "case_name_full": "Preston v. United States",
    "input_case_name": "Preston v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-03-23",
    "year": 1964,
    "docket": "163",
    "cluster_id": 106771,
    "lead_opinion_id": 106771,
    "sibling_ids": [
      106771
    ],
    "absolute_url": "/opinion/106771/preston-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "376 U.S. 364",
      "volume": "376",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 881",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 777",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "777",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1578",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "376 U.S. 364",
        "volume": "376",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 881",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "881",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "11 L. Ed. 2d 777",
        "volume": "11",
        "reporter": "L. Ed. 2d",
        "page": "777",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1578",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "376 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "376 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-367",
      "page": null,
      "quote": "--- # Preston v. United States *376 U.S. 364 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received a 3 a.m. complaint about three suspicious men who had been sitting in a parked car for hours in a business district. Officers questioned the men, found their answers evasive, learned all three were unemployed with 25 cents among them, and arrested them for vagrancy. The men were searched for weapons and taken to the station; the car, unsearched at the scene, was driven to the station and then towed to a garage. After the men were booked, officers searched the car at the garage, finding loaded revolvers in the glove compartment and \u2014 after forcing into the trunk \u2014 robbery paraphernalia (a stocking mask, rope, a fake license plate). The items were used to convict petitioner of conspiracy to rob a bank. ## Issue May a warrantless search of a car at a garage \u2014 conducted after the arrestees were in custody at the station and the car had been towed \u2014 be justified as a search incident to the arrest? ## Rule No. A search incident to arrest must be contemporaneous, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-367b",
      "page": null,
      "quote": "justifications are absent where a search is remote in time or place from the arrest.",
      "star_marker": "367",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 8643,
      "fragment": "#:~:text=justifications%20are%20absent%20where%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-368",
      "page": null,
      "quote": "the search was too remote in time or place to have been made as incidental to the arrest . . . , [so] the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained . . . inadmissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-03-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Preston v. United States",
    "varies_by_point": false,
    "scope_note": "The search-incident-to-arrest remoteness holding remains controlling. Preston is a SITA case; the later automobile-exception line ([[Chambers v. Maroney]], [[Michigan v. Thomas]]) independently permits warrantless delayed vehicle searches on probable cause, distinguishing \u2014 not overruling \u2014 Preston, so it no longer implies every station-house car search is unreasonable.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Dennis",
          "cluster_id": 4679939,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Lee Douds v. State",
          "cluster_id": 2983810,
          "cite": [
            "434 S.W.3d 842",
            "2014 WL 2619863",
            "2014 Tex. App. LEXIS 6152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hughes v. State",
          "cluster_id": 2284872,
          "cite": [
            "334 S.W.3d 379",
            "2011 WL 561497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sawyer",
          "cluster_id": 167203,
          "cite": [
            "441 F.3d 890",
            "2006 U.S. App. LEXIS 6838",
            "2006 WL 689451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion No.",
          "cluster_id": 3256671,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Garner",
          "cluster_id": 8742797,
          "cite": [
            "945 F. Supp. 990",
            "1996 U.S. Dist. LEXIS 16709",
            "1996 WL 655571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mark A. McKinnell",
          "cluster_id": 531282,
          "cite": [
            "888 F.2d 669",
            "28 Fed. R. Serv. 1309",
            "1989 U.S. App. LEXIS 16209",
            "1989 WL 127016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Belton",
          "cluster_id": 5685394,
          "cite": [
            "55 N.Y.2d 49",
            "432 N.E.2d 745",
            "447 N.Y.S.2d 873",
            "1982 N.Y. LEXIS 3067"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Riegler",
          "cluster_id": 2135147,
          "cite": [
            "127 Cal. App. 3d 317",
            "179 Cal. Rptr. 530",
            "1981 Cal. App. LEXIS 2530"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gill v. State",
          "cluster_id": 1770662,
          "cite": [
            "625 S.W.2d 307",
            "1981 Tex. Crim. App. LEXIS 1283"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jozsef Tibor Wiga, United States of America v. Jozsef Tibor Wiga",
          "cluster_id": 396356,
          "cite": [
            "662 F.2d 1325",
            "1981 U.S. App. LEXIS 15460"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rafaela Monclavo-Cruz",
          "cluster_id": 396352,
          "cite": [
            "662 F.2d 1285"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Taylor v. State",
          "cluster_id": 1596133,
          "cite": [
            "399 So. 2d 881"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane1_negative"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Winston Bryant McConney",
          "cluster_id": 431931,
          "cite": [
            "728 F.2d 1195",
            "1984 U.S. App. LEXIS 25576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. United States",
          "cluster_id": 107625,
          "cite": [
            "19 L. Ed. 2d 1067",
            "88 S. Ct. 992",
            "390 U.S. 234",
            "1968 U.S. LEXIS 2283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cooper v. California",
          "cluster_id": 107360,
          "cite": [
            "17 L. Ed. 2d 730",
            "87 S. Ct. 788",
            "386 U.S. 58",
            "1967 U.S. LEXIS 2199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
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
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cardwell v. Lewis",
          "cluster_id": 109069,
          "cite": [
            "41 L. Ed. 2d 325",
            "94 S. Ct. 2464",
            "417 U.S. 583",
            "1974 U.S. LEXIS 75",
            "69 Ohio Op. 2d 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Edwards",
          "cluster_id": 108995,
          "cite": [
            "39 L. Ed. 2d 771",
            "94 S. Ct. 1234",
            "415 U.S. 800",
            "1974 U.S. LEXIS 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Knowles v. Iowa",
          "cluster_id": 118250,
          "cite": [
            "142 L. Ed. 2d 492",
            "119 S. Ct. 484",
            "525 U.S. 113",
            "1998 U.S. LEXIS 8068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Preston v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106771) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTIwODAwMDAwMDAmcz0xNTk2MTMzJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106771%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(106771)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzAmcz0xMzg4MDYxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106771%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106771)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106771)",
    "indexed_citing_opinions": 1251,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106771,
        "count": 1251,
        "count_source": "search"
      }
    ],
    "citation_count": 1906,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/preston-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5NTI0OSZzPTQ1MjQ4MjImdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28106771%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106771,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106771,
        "cited_id": 106107,
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
    "date_created": "2026-07-05T17:15:33Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:19:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:15:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Preston v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b426-12">
  Mr. Justice Black
 </author>
<p id="A69">
  delivered the opinion of the Court.
 </p>
<p id="b426-13">
  Petitioner and three others were convicted in the United States District Court for the Eastern District of Kentucky on a charge of conspiracy to rob a federally insured bank in violation of <span class="citation no-link">18 U. S. C. § 2113</span>, the conviction having been based largely on evidence obtained by the search of a motorcar. The Court of Appeals for the Sixth Circuit affirmed, rejecting the contentions, timely made in the trial and appellate courts, that
  <span citation-index="1" class="star-pagination" label="365"> 
   *365
   </span>
  both the original arrest, on a charge of vagrancy, and the subsequent search and seizure had violated the Fourth Amendment. <span class="citation" data-id="9448645"><a href="/opinion/257690/united-states-v-john-richard-sykes-john-brenton-preston-and-kenneth-ray/" aria-description="Citation for case: United States v. John Richard Sykes, John Brenton...">305 F. 2d 172</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./373/931/">373 U. S. 931</a></span>. In the view we take of the case, we heed not decide whether the arrest was valid, since we hold that the search and seizure was not-.
 </p>
<p id="b427-5">
  The police of Newport, Kentucky, received a telephone complaint at 3 o’clock one morning that “three suspicious men acting suspiciously”- had been seated in a motorcar parked in a business district since 10 o’clock the evening before. Four policemen straightaway went to the place where the car was parked and found petitioner and two companions. The officers asked the three men why they were parked there, but the men gave answers which the officers testified were unsatisfactory and evasive. All three men admitted that they were unemployed; all of them together had only 25 cents. One of the men said that he had bought the car the day before (which later turned out to be true), but he could not produce any title. They said that their reason for being there was to meet a truck driver who would pass through Newport that night, but they could not identify the company he worked for, could not say what his truck looked like, and did not know what time he would arrive. The officers arrested the three men for vagrancy, searched them for weapons, and took them to police headquarters. The car, which had not been searched at the time of the arrest, was driven by an officer to the station, from which it was towed to a garage. Soon after the men had been booked at the station, some of the police officers went to the garage to search the car and found two loaded revolvers in the glove compartment. They were unable to open the trunk and returned to the station, where a detective told one of the officers to go back and try to get into the trunk. The officer did so, was able to enter the trunk through the back seat of the car, and in
  <span citation-index="1" class="star-pagination" label="366"> 
   *366
   </span>
  the trunk found caps, women’s stockings (one with mouth and eye holes), rope, pillow slips, an illegally manufactured license plate equipped to be snapped over another plate, and other items. After the search, one of petitioner’s companions confessed that he and two others— he did not name petitioner — intended to rob a bank in Berry, Kentucky, a town about 51 miles from Newport. At this, the police called the Federal Bureau of Investigation into the case and turned over to the Bureau the articles found in the car. It was the use of these articles, over timely objections, which raised the Fourth Amendment question we here consider.
 </p>
<p id="b428-5">
  The Amendment provides:
 </p>
<blockquote id="b428-6">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b428-7">
  The question whether evidence obtained by state officers and used against a defendant in a federal trial was obtained by unreasonable search and seizure is to be judged as if the search and seizure had been made by federal officers.
  <em>
   Elkins
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960). Our cases make it clear that searches of motorcars must meet the test of reasonableness under the Fourth Amendment before evidence obtained as a result of such searches is admissible.
  <em>
   E. g., Carroll
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925);
  <em>
   Brinegar
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949). Common sense dictates, of course, that questions involving searches of motorcars or other things readily moved cannot be treated as identical to questions arising out of searches of fixed structures like houses. For this reason, what may be an unreasonable search of
  <span citation-index="1" class="star-pagination" label="367"> 
   *367
   </span>
  a house may be reasonable in the case of a motorcar. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. But even in the case of motorcars, the test still is, was the search unreasonable. Therefore we must inquire whether the facts of this case are such as to fall within any of the exceptions to the constitutional rule that a search warrant must be had before a search may be made.
 </p>
<p id="b429-5">
  It is argued that the search and seizure was justified as incidental to a lawful arrest. Unquestionably, when a person is lawfully arrested, the police have the right, without a search warrant, to make a contemporaneous search of the person of the accused for weapons or for the fruits of or implements used to commit the crime.
  <em>
   Weeks
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914);
  <em>
   Agnello
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1925). This right to search and seize without a search warrant extends to things under the accused’s immediate control,
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>, and, to an extent depending on the circumstances of the case, to the place where he is arrested,
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30</a></span>;
  <em>
   Marron
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#199" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 199</a></span> (1927);
  <em>
   United States
  </em>
  v.
  <em>
   Rabinowitz,
  </em>
  <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 61-62</a></span> (1950). The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime — things which might easily happen where the weapon or evidence is on the accused’s person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest.
  <em>
   Agnello
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#31" aria-description="Citation for case: Agnello v. United States">269 U. S., at 31</a></span>. Here, we may assume, as the Government urges, that, either because the arrests were valid or because the police had
  <span citation-index="1" class="star-pagination" label="368"> 
   *368
   </span>
  probable cause to think the car stolen, the police had the right to search the car when they first came on the scene. But this does not decide the question of the reasonableness of a search at a later time and at another place. See
  <em>
   Stoner
  </em>
  v.
  <em>
   California, post,
  </em>
  p. 483. The search of the car was not undertaken until petitioner and his companions had been arrested and taken in custody to the police station and the car had been towed to the garage. At this point there was no danger that any of the men arrested could have used any weapons in the car or could have destroyed any evidence of a crime — assuming that there are articles which can be the “fruits” or “implements” of the crime of vagrancy. Cf.
  <em>
   United States
  </em>
  v.
  <em>
   Jeffers,
  </em>
  <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51-52</a></span> (1951). Nor, since the men were under arrest at the police station and the car was in police custody at a garage, was there any danger that the car would be moved out of the locality or jurisdiction. See
  <em>
   Carroll
  </em>
  v.
  <em>
   United States, supra,
  </em>
  <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153</a></span>. We think that the search was too remote in time or place to have been made as incidental to the arrest and conclude, therefore, that the search of the car without a warrant failed to meet the test of reasonableness under the Fourth Amendment, rendering the evidence obtained as a result of the search inadmissible.
 </p>
<p id="b430-5">
<em>
   Reversed and remanded.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Rakas v. Illinois.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Rakas v. Illinois"
type: case
citation: "439 U.S. 128 (1978)"
parallel_cite: "99 S. Ct. 421; 58 L. Ed. 2d 387"
neutral_cite: 1978 U.S. LEXIS 2452
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-12-05
docket: 77-5781
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-12-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rakas v. Illinois
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109953/rakas-v-illinois/"
  cluster_id: 109953
  opinion_id: 109953
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Anchor"
  - page: "[[The Exclusionary Rule]]"
    role: "Related (cross-doctrine)"
related: ["[[Katz v. United States]]", "[[Rawlings v. Kentucky]]", "[[Minnesota v. Carter]]", "[[Byrd v. United States]]", "[[Brendlin v. California]]", "[[Jones v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "passenger", "vehicle-search"]
holding: "Fourth Amendment rights are personal; a defendant must show his own legitimate expectation of privacy was infringed and cannot…"
lake:
  record_id: Rakas v. Illinois
  status: verified
  projected_at: 2026-07-10
---

# Rakas v. Illinois

*439 U.S. 128 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police stopped a car suspected of being the getaway vehicle in a robbery. Rakas and the other petitioners were passengers; they asserted neither ownership of the car nor of the items seized. A search turned up a box of rifle shells in the locked glove compartment and a sawed-off rifle under the front passenger seat. The passengers moved to suppress.

## Issue
Whether passengers who assert no property or possessory interest in the automobile or in the seized items, and who claim no legitimate expectation of privacy in the areas searched, may challenge the search.

## Rule
No. Fourth Amendment rights are personal: "Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously asserted." — 439 U.S. at 133–134 (quoting *Alderman v. United States*). ^pin-133

The standing question is subsumed into the substantive inquiry: "capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place." — [439 U.S. at 143](https://www.courtlistener.com/opinion/109953/rakas-v-illinois/#:~:text=capacity%20to%20claim%20the%20protection). ^pin-143

## Application
Rakas and his co-passengers asserted neither ownership of the car nor of the rifle and shells, and they showed no legitimate expectation of privacy in the glove compartment or the area under the seat — places in which a mere passenger would not normally have such an expectation. Because the Fourth Amendment right is personal and they had no privacy interest in the areas searched, they could not contest the search, and suppression was properly denied.

## Conclusion
The passengers lacked standing — i.e., any legitimate expectation of privacy in the places searched — to challenge the search; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Rakas* merged "standing" into the substantive expectation-of-privacy inquiry; it was applied to owned-but-bailed property in [[Rawlings v. Kentucky]] and to rental cars in [[Byrd v. United States]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Anchor*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Rakas v. Illinois*, 439 U.S. 128 (1978) — https://www.courtlistener.com/opinion/109953/rakas-v-illinois/ — pinpoints: 133–134, 143.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9c5899f369444489", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Rakas v. Illinois"}, "payload": {"all": [{"cite": "439 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "439"}, {"cite": "99 S. Ct. 421", "page": "421", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "58 L. Ed. 2d 387", "page": "387", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "58"}, {"cite": "1978 U.S. LEXIS 2452", "page": "2452", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "439 U.S. 128", "official": {"cite": "439 U.S. 128", "page": "128", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "439"}, "official_selection_present": true, "record_id": "Rakas v. Illinois"}}
{"assertion_id": "78f2c5777f8d736f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-143", "record_id": "Rakas v. Illinois"}, "payload": {"fragment": "#:~:text=capacity%20to%20claim%20the%20protection", "page": null, "pin_id": "pin-143", "pinpoint_status": "star-verified", "quote": "capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place.", "quote_fidelity": "matched", "record_id": "Rakas v. Illinois", "star_marker": "143"}}
{"assertion_id": "85d2ef19be365dd3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-133", "record_id": "Rakas v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-133", "pinpoint_status": "slip-only", "quote": "--- # Rakas v. Illinois *439 U.S. 128 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police stopped a car suspected of being the getaway vehicle in a robbery. Rakas and the other petitioners were passengers; they asserted neither ownership of the car nor of the items seized. A search turned up a box of rifle shells in the locked glove compartment and a sawed-off rifle under the front passenger seat. The passengers moved to suppress. ## Issue Whether passengers who assert no property or possessory interest in the automobile or in the seized items, and who claim no legitimate expectation of privacy in the areas searched, may challenge the search. ## Rule No. Fourth Amendment rights are personal:", "quote_fidelity": "mismatch", "record_id": "Rakas v. Illinois", "star_marker": null}}
{"assertion_id": "b166bb37cfc42452", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Rakas v. Illinois"}, "payload": {"as_of_content": "1978-12-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Rakas v. Illinois", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Rakas v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rakas v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rakas v. Illinois",
    "case_name_short": "Rakas",
    "case_name_full": "RAKAS Et Al. v. ILLINOIS",
    "input_case_name": "Rakas v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-12-05",
    "year": 1978,
    "docket": "77-5781",
    "cluster_id": 109953,
    "lead_opinion_id": 109953,
    "sibling_ids": [
      109953,
      9427384,
      9427385,
      9427386
    ],
    "absolute_url": "/opinion/109953/rakas-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9019150,
        "score": 20,
        "case_name": "Satterfield v. United States"
      },
      {
        "cluster_id": 9019149,
        "score": 20,
        "case_name": "Riggs v. Flamm"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "439 U.S. 128",
      "volume": "439",
      "reporter": "U.S.",
      "page": "128",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 421",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "421",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 2d 387",
        "volume": "58",
        "reporter": "L. Ed. 2d",
        "page": "387",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 2452",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "2452",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "439 U.S. 128",
        "volume": "439",
        "reporter": "U.S.",
        "page": "128",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 421",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "421",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 2d 387",
        "volume": "58",
        "reporter": "L. Ed. 2d",
        "page": "387",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 2452",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "2452",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "439 U.S. 128",
    "official_selection": {
      "court_class": "scotus",
      "selected": "439 U.S. 128",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-133",
      "page": null,
      "quote": "--- # Rakas v. Illinois *439 U.S. 128 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police stopped a car suspected of being the getaway vehicle in a robbery. Rakas and the other petitioners were passengers; they asserted neither ownership of the car nor of the items seized. A search turned up a box of rifle shells in the locked glove compartment and a sawed-off rifle under the front passenger seat. The passengers moved to suppress. ## Issue Whether passengers who assert no property or possessory interest in the automobile or in the seized items, and who claim no legitimate expectation of privacy in the areas searched, may challenge the search. ## Rule No. Fourth Amendment rights are personal:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-143",
      "page": null,
      "quote": "capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place.",
      "star_marker": "143",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 36336,
      "fragment": "#:~:text=capacity%20to%20claim%20the%20protection",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-12-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rakas v. Illinois",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Ganeous",
          "cluster_id": 10266125,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Aiken",
          "cluster_id": 8619549,
          "cite": [
            "877 F.3d 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane1_negative"
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
        "journal_ref": "Rakas v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brock v. Dunning",
          "cluster_id": 2722122,
          "cite": [
            "288 Neb. 909"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ortiz",
          "cluster_id": 8477550,
          "cite": [
            "507 F. App'x 339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
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
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
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
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bryant, Smith and Wheeler",
          "cluster_id": 2720490,
          "cite": [
            "60 Cal. 4th 335",
            "178 Cal. Rptr. 3d 185",
            "334 P.3d 573",
            "2014 Cal. LEXIS 6110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lance W.",
          "cluster_id": 1421847,
          "cite": [
            "694 P.2d 744",
            "37 Cal. 3d 873",
            "210 Cal. Rptr. 631",
            "1985 Cal. LEXIS 241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walter v. State",
          "cluster_id": 1755500,
          "cite": [
            "28 S.W.3d 538",
            "2000 Tex. Crim. App. LEXIS 84",
            "2000 WL 1348504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Linette Perez, United States of America v. Juancho Alcantera, United States of America v. Edmundo Batoon",
          "cluster_id": 776532,
          "cite": [
            "280 F.3d 318",
            "2002 WL 171241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ayala",
          "cluster_id": 2551468,
          "cite": [
            "1 P.3d 3",
            "96 Cal. Rptr. 2d 682",
            "23 Cal. 4th 225",
            "2000 Cal. Daily Op. Serv. 4490",
            "2000 Daily Journal DAR 6037",
            "2000 Cal. LEXIS 4545"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2629957,
          "cite": [
            "117 P.3d 476",
            "32 Cal. Rptr. 3d 759",
            "36 Cal. 4th 1114",
            "2005 Cal. Daily Op. Serv. 7196",
            "2005 Daily Journal DAR 9801",
            "2005 Cal. LEXIS 8908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Tibbetts",
          "cluster_id": 6889013,
          "cite": [
            "92 Ohio St. 3d 146",
            "749 N.E.2d 226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. State",
          "cluster_id": 2106367,
          "cite": [
            "311 S.W.3d 452",
            "2010 Tex. Crim. App. LEXIS 685",
            "2010 WL 715253"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Granados v. State",
          "cluster_id": 1588783,
          "cite": [
            "85 S.W.3d 217",
            "2002 Tex. Crim. App. LEXIS 99",
            "2002 WL 922901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emerson v. State",
          "cluster_id": 2392754,
          "cite": [
            "880 S.W.2d 759",
            "1994 Tex. Crim. App. LEXIS 48",
            "1994 WL 122847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Calloway v. State",
          "cluster_id": 2364085,
          "cite": [
            "743 S.W.2d 645",
            "1988 Tex. Crim. App. LEXIS 35",
            "1988 WL 4310"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hardy",
          "cluster_id": 1494781,
          "cite": [
            "963 S.W.2d 516",
            "1997 WL 716775"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bower v. State",
          "cluster_id": 1625069,
          "cite": [
            "769 S.W.2d 887",
            "1989 Tex. Crim. App. LEXIS 6",
            "1989 WL 4325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
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
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 8923386,
          "cite": [
            "636 F.2d 1028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rakas v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109953 OR 9427384 OR 9427385 OR 9427386) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzQ1NDIwODAwMDAwJnM9MjcwNTg3MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109953+OR+9427384+OR+9427385+OR+9427386%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109953 OR 9427384 OR 9427385 OR 9427386)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDYmcz0zOTcxMzkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109953+OR+9427384+OR+9427385+OR+9427386%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109953 OR 9427384 OR 9427385 OR 9427386)",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 1,
        "triage_snippet_classified": 71
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109953 OR 9427384 OR 9427385 OR 9427386)",
    "indexed_citing_opinions": 1418,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109953,
        "count": 700,
        "count_source": "search"
      },
      {
        "opinion_id": 9427384,
        "count": 772,
        "count_source": "search"
      },
      {
        "opinion_id": 9427385,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427386,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6107,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rakas-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjIxODI3NjUmcz03OTAwMzMmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28109953+OR+9427384+OR+9427385+OR+9427386%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109953,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 101118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 104016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 105152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106425,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109046,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 109816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 259018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 264659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 268148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 274387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 277129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 281517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 299112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 299539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 301437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 312637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 329973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 339194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 347694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 356972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 1190053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 1424578,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 1427556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 1872066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 1978947,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 2136957,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 2244074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109953,
        "cited_id": 2443377,
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
    "date_created": "2026-07-05T17:19:40Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:20:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:20:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:23:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:20:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rakas v. Illinois (truncated)

```
<div>
<center><b><span class="citation no-link">439 U.S. 128</span> (1978)</b></center>
<center><h1>RAKAS ET AL.<br>
v.<br>
ILLINOIS.</h1></center>
<center>No. 77-5781.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 3, 1978.</center>
<center>Decided December 5, 1978.</center>
CERTIORARI TO THE APPELLATE COURT OF ILLINOIS, THIRD DIVISION.
<p><span class="star-pagination">*129</span> <i>G. Joseph Weller</i> argued the cause for petitioners. With him on the briefs were <i>Robert Agostinelli</i> and <i>Mark W. Burkhalter.</i></p>
<p><i>Donald B. Mackay,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With him on the brief were <i>William J. Scott,</i> Attorney General, and <i>Melbourne A. Noel, Jr.,</i> and <i>Michael B. Weinstein,</i> Assistant Attorneys General.<sup>[*]</sup></p>
<p>MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Petitioners were convicted of armed robbery in the Circuit Court of Kankakee County, Ill., and their convictions were affirmed on appeal. At their trial, the prosecution offered into evidence a sawed-off rifle and rifle shells that had been seized by police during a search of an automobile in which petitioners had been passengers. Neither petitioner is the owner of the automobile and neither has ever asserted that he owned the rifle or shells seized. The Illinois Appellate Court held that petitioners lacked standing to object to the allegedly <span class="star-pagination">*130</span> unlawful search and seizure and denied their motion to suppress the evidence. We granted certiorari in light of the obvious importance of the issues raised to the administration of criminal justice, <span class="citation multiple-matches"><a href="/c/U.%20S./435/922/">435 U. S. 922</a></span> (1978), and now affirm.</p>
<p></p>
<h2>I</h2>
<p>Because we are not here concerned with the issue of probable cause, a brief description of the events leading to the search of the automobile will suffice. A police officer on a routine patrol received a radio call notifying him of a robbery of a clothing store in Bourbonnais, Ill., and describing the getaway car. Shortly thereafter, the officer spotted an automobile which he thought might be the getaway car. After following the car for some time and after the arrival of assistance, he and several other officers stopped the vehicle. The occupants of the automobile, petitioners and two female companions, were ordered out of the car and, after the occupants had left the car, two officers searched the interior of the vehicle. They discovered a box of rifle shells in the glove compartment, which had been locked, and a sawed-off rifle under the front passenger seat. App. 10-11. After discovering the rifle and the shells, the officers took petitioners to the station and placed them under arrest.</p>
<p>Before trial petitioners moved to suppress the rifle and shells seized from the car on the ground that the search violated the Fourth and Fourteenth Amendments. They conceded that they did not own the automobile and were simply passengers; the owner of the car had been the driver of the vehicle at the time of the search. Nor did they assert that they owned the rifle or the shells seized.<sup>[1]</sup> The prosecutor <span class="star-pagination">*131</span> challenged petitioners' standing to object to the lawfulness of the search of the car because neither the car, the shells nor the rifle belonged to them. The trial court agreed that petitioners lacked standing and denied the motion to suppress the evidence. App. 23-24. In view of this holding, the court did not determine whether there was probable cause for the search and seizure. On appeal after petitioners' conviction, the Appellate Court of Illinois, Third Judicial District, affirmed the trial court's denial of petitioners' motion to suppress because it held that "without a proprietary or other similar interest in an automobile, a mere passenger therein lacks standing to challenge the legality of the search of the vehicle." <span class="star-pagination">*132</span> <span class="citation" data-id="2244074"><a href="/opinion/2244074/people-v-rakas/#571" aria-description="Citation for case: People v. Rakas">46 Ill. App. 3d 569, 571</a></span>, <span class="citation" data-id="2244074"><a href="/opinion/2244074/people-v-rakas/#1253" aria-description="Citation for case: People v. Rakas">360 N. E. 2d 1252, 1253</a></span> (1977). The court stated:</p>
<blockquote>"We believe that defendants failed to establish any prejudice to their own constitutional rights because they were not persons aggrieved by the unlawful search and seizure. . . . They wrongly seek to establish prejudice only through the use of evidence gathered as a consequence of a search and seizure directed at someone else and fail to prove an invasion of their own privacy. <i>Alderman</i> v. <i>United States</i> (1969), <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> . . . ." <i>Id.,</i> at 571-572, <span class="citation" data-id="2244074"><a href="/opinion/2244074/people-v-rakas/#1254" aria-description="Citation for case: People v. Rakas">360 N. E. 2d, at 1254</a></span>.</blockquote>
<p>The Illinois Supreme Court denied petitioners leave to appeal.</p>
<p></p>
<h2>II</h2>
<p>Petitioners first urge us to relax or broaden the rule of standing enunciated in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), so that any criminal defendant at whom a search was "directed" would have standing to contest the legality of that search and object to the admission at trial of evidence obtained as a result of the search. Alternatively, petitioners argue that they have standing to object to the search under <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> because they were "legitimately on [the] premises" at the time of the search.</p>
<p>The concept of standing discussed in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> focuses on whether the person seeking to challenge the legality of a search as a basis for suppressing evidence was himself the "victim" of the search or seizure. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 261</a></span>.<sup>[2]</sup> Adoption of <span class="star-pagination">*133</span> the so-called "target" theory advanced by petitioners would in effect permit a defendant to assert that a violation of the Fourth Amendment rights of a third party entitled him to have evidence suppressed at his trial. If we reject petitioners' request for a broadened rule of standing such as this, and reaffirm the holding of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and other cases that Fourth Amendment rights are personal rights that may not be asserted vicariously, we will have occasion to re-examine the "standing" terminology emphasized in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i>. For we are not at all sure that the determination of a motion to suppress is materially aided by labeling the inquiry identified in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> as one of standing, rather than simply recognizing it as one involving the substantive question of whether or not the proponent of the motion to suppress has had his own Fourth Amendment rights infringed by the search and seizure which he seeks to challenge. We shall therefore consider in turn petitioners' target theory, the necessity for continued adherence to the notion of standing discussed in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> as a concept that is theoretically distinct from the merits of a defendant's Fourth Amendment claim, and, finally, the proper disposition of petitioners' ultimate claim in this case.</p>
<p></p>
<h2>A</h2>
<p>We decline to extend the rule of standing in Fourth Amendment cases in the manner suggested by petitioners. As we stated in <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174</a></span> (1969), "Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously <span class="star-pagination">*134</span> asserted." See <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#230" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 230</a></span> (1973); <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389</a></span> (1968); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#492" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 492</a></span> (1963); cf. <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span> (1961); <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#304" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 304</a></span> (1921). A person who is aggrieved by an illegal search and seizure only through the introduction of damaging evidence secured by a search of a third person's premises or property has not had any of his Fourth Amendment rights infringed. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States"><i>Alderman, supra,</i> at 174</a></span>. And since the exclusionary rule is an attempt to effectuate the guarantees of the Fourth Amendment, <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974), it is proper to permit only defendants whose Fourth Amendment rights have been violated to benefit from the rule's protections.<sup>[3]</sup> See <i>Simmons</i> v. <i>United States, supra,</i> at 389. There is no reason to think that a party whose rights have been infringed will not, if evidence is used against him, have ample motivation to move to suppress it. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States"><i>Alderman, supra,</i> at 174</a></span>. Even if such a person is not a defendant in the action, he may be able to recover damages for the violation of his Fourth Amendment rights, see <i>Monroe</i> v. <i>Pape,</i> <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), or seek redress under state law for invasion of privacy or trespass.</p>
<p>In support of their target theory, petitioners rely on the following quotation from <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>:</i></p>
<blockquote>"In order to qualify as a `person aggrieved by an unlawful search and seizure' one must have been a victim of a search or seizure, <i>one against whom the search was</i> <span class="star-pagination">*135</span> <i>directed,</i> as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span> (emphasis added).</blockquote>
<p>They also rely on <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span>, 548 n. 11 (1968), and <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951).</p>
<p>The above-quoted statement from <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> suggests that the italicized language was meant merely as a parenthetical equivalent of the previous phrase "a victim of a search or seizure." To the extent that the language might be read more broadly, it is dictum which was impliedly repudiated in <i>Alderman</i> v. <i>United States, supra</i><i>,</i> and which we now expressly reject. In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the Court set forth two alternative holdings: It established a rule of "automatic" standing to contest an allegedly illegal search where the same possession needed to establish standing is an essential element of the offense charged;<sup>[4]</sup> and second, it stated that "anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#264" aria-description="Citation for case: Jones v. United States">362 U. S., at 264, 267</a></span>. See <i>Combs</i> v. <i>United States,</i> <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">408 U. S. 224</a></span>, 227 n. 4 (1972); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span>, 368 n. 5 (1968); <i>Simmons</i> v. <i>United States, supra,</i> at 390. Had the Court intended to adopt the target theory now put forth by petitioners, neither of the above two holdings would have been necessary since Jones was the "target" of the police search in that case.<sup>[5]</sup> Nor does <i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>,</i> or <span class="star-pagination">*136</span> <i>Bumper</i> v. <i>North <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Carolina, supra</a></span></i><i>,</i> support the target theory. Standing in <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers</a></span></i> was based on Jeffers' possessory interest in both the premises searched and the property seized. <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#49" aria-description="Citation for case: United States v. Jeffers">342 U. S., at 49-50, 54</a></span>; see <i>Mancusi</i> v. <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#367" aria-description="Citation for case: Mancusi v. DeForte"><i>DeForte, supra,</i> at 367-368</a></span>; <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#301" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 301</a></span> (1966); <i>Lanza</i> v. <i>New York,</i> <span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143</a></span>, and n. 10 (1962). Similarly, in <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>,</i> the defendant had a substantial possessory interest in both the house searched and the rifle seized. <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S., at 548</a></span> n. 11.</p>
<p><i>In </i><i>Alderman</i> v. <i>United States</i><i>,</i> Mr. Justice Fortas, in a concurring and dissenting opinion, argued that the Court should "include within the category of those who may object to the introduction of illegal evidence `one against whom the search was directed.' " <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#206" aria-description="Citation for case: Alderman v. United States">394 U. S., at 206-209</a></span>. The Court did not directly comment on Mr. Justice Fortas' suggestion, but it left no doubt that it rejected this theory by holding that persons who were not parties to unlawfully overheard conversations or who did not own the premises on which such conversations took place did not have standing to contest the legality of the surveillance, regardless of whether or not they were the "targets" of the surveillance. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#176" aria-description="Citation for case: Alderman v. United States"><i>Id.,</i> at 176</a></span>. Mr. Justice Harlan, concurring and dissenting, did squarely address Mr. Justice Fortas' arguments and declined to accept them. <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#188" aria-description="Citation for case: Alderman v. United States"><i>Id.,</i> at 188-189, n. 1</a></span>. He identified administrative problems posed by the target theory:</p>
<blockquote>"[T]he [target] rule would entail very substantial administrative difficulties. In the majority of cases, I would imagine that the police plant a bug with the expectation that it may well produce leads to a large number of crimes. A lengthy hearing would, then, appear to be necessary in order to determine whether the police knew of an accused's criminal activity at the time the bug was <span class="star-pagination">*137</span> planted and whether the police decision to plant a bug was motivated by an effort to obtain information against the accused or some other individual. I do not believe that this administrative burden is justified in any substantial degree by the hypothesized marginal increase in Fourth Amendment protection." <i><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Ibid.</a></span></i>
</blockquote>
<p>When we are urged to grant standing to a criminal defendant to assert a violation, not of his own constitutional rights but of someone else's, we cannot but give weight to practical difficulties such as those foreseen by Mr. Justice Harlan in the quoted language.</p>
<p>Conferring standing to raise vicarious Fourth Amendment claims would necessarily mean a more widespread invocation of the exclusionary rule during criminal trials. The Court's opinion in <i><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span></i> counseled against such an extension of the exclusionary rule:</p>
<blockquote>"The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But we are not convinced that the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth." <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States"><i>Id.,</i> at 174-175</a></span>.</blockquote>
<p>Each time the exclusionary rule is applied it exacts a substantial social cost for the vindication of Fourth Amendment rights. Relevant and reliable evidence is kept from the trier of fact and the search for truth at trial is deflected. See <i>United States</i> v. <i>Ceccolini,</i> <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 275</a></span> (1978); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#489" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 489-490</a></span> (1976); <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348-352</a></span>. Since our cases generally <span class="star-pagination">*138</span> have held that one whose Fourth Amendment rights are violated may successfully suppress evidence obtained in the course of an illegal search and seizure, misgivings as to the benefit of enlarging the class of persons who may invoke that rule are properly considered when deciding whether to expand standing to assert Fourth Amendment violations.<sup>[6]</sup></p>
<p></p>
<h2>B</h2>
<p>Had we accepted petitioners' request to allow persons other than those whose own Fourth Amendment rights were violated by a challenged search and seizure to suppress evidence obtained in the course of such police activity, it would be appropriate to retain <i>Jones'</i> use of standing in Fourth Amendment analysis. Under petitioners' target theory, a court could determine that a defendant had standing to invoke the exclusionary rule without having to inquire into the substantive question of whether the challenged search or seizure violated the Fourth Amendment rights of that particular defendant. However, having rejected petitioners' target theory and reaffirmed the principle that the "rights assured by the Fourth Amendment are personal rights, [which] . . . may be enforced by exclusion of evidence only at the instance of one whose own protection was infringed by the search and seizure," <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S., at 389</a></span>, the question necessarily arises whether it serves any useful analytical purpose to consider this principle a matter of standing, distinct from the merits of a defendant's Fourth <span class="star-pagination">*139</span> Amendment claim. We can think of no decided cases of this Court that would have come out differently had we concluded, as we do now, that the type of standing requirement discussed in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and reaffirmed today is more properly subsumed under substantive Fourth Amendment doctrine. Rigorous application of the principle that the rights secured by this Amendment are personal, in place of a notion of "standing," will produce no additional situations in which evidence must be excluded. The inquiry under either approach is the same.<sup>[7]</sup> But we think the better analysis forthrightly focuses on the extent of a particular defendant's rights under the Fourth Amendment, rather than on any theoretically separate, but invariably intertwined concept of standing. The Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> also may have been aware that there was a certain artificiality in analyzing this question in terms of standing because in at least three separate places in its opinion the Court placed that term within quotation marks. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261, 263, 265</a></span>.</p>
<p>It should be emphasized that nothing we say here casts the least doubt on cases which recognize that, as a general proposition, the issue of standing involves two inquiries: first, whether the proponent of a particular legal right has alleged "injury in fact," and, second, whether the proponent is asserting his own legal rights and interests rather than basing his claim for relief upon the rights of third parties. See, <i>e. g., </i><i>Singleton</i> v. <i>Wulff,</i> <span class="citation" data-id="9426552"><a href="/opinion/109530/singleton-v-wulff/#112" aria-description="Citation for case: Singleton v. Wulff">428 U. S. 106, 112</a></span> (1976); <i>Warth</i> v. <i>Seldin,</i> <span class="star-pagination">*140</span> <span class="citation" data-id="9426170"><a href="/opinion/109301/warth-v-seldin/#499" aria-description="Citation for case: Warth v. Seldin">422 U. S. 490, 499</a></span> (1975); <i>Data Processing Service</i> v. <i>Camp,</i> <span class="citation" data-id="108088"><a href="/opinion/108088/association-of-data-processing-service-organizations-inc-v-camp/#152" aria-description="Citation for case: Association of Data Processing Service Organizations,...">397 U. S. 150, 152-153</a></span> (1970). But this Court's long history of insistence that Fourth Amendment rights are personal in nature has already answered many of these traditional standing inquiries, and we think that definition of those rights is more properly placed within the purview of substantive Fourth Amendment law than within that of standing. Cf. <span class="citation" data-id="108088"><a href="/opinion/108088/association-of-data-processing-service-organizations-inc-v-camp/#153" aria-description="Citation for case: Association of Data Processing Service Organizations,..."><i>id.,</i> at 153</a></span>, and n. 1; <i>Barrows</i> v. <i>Jackson,</i> <span class="citation" data-id="9420983"><a href="/opinion/105152/barrows-v-jackson/" aria-description="Citation for case: Barrows v. Jackson">346 U. S. 249</a></span>, 256 n. 4 (1953); <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/#69" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43, 69-70</a></span> (1906).<sup>[8]</sup></p>
<p>Analyzed in these terms, the question is whether the challenged search and seizure violated the Fourth Amendment rights of a criminal defendant who seeks to exclude the evidence obtained during it. That inquiry in turn requires a determination of whether the disputed search and seizure has infringed an interest of the defendant which the Fourth Amendment was designed to protect. We are under no illusion that by dispensing with the rubric of standing used in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> we have rendered any simpler the determination of whether the proponent of a motion to suppress is entitled to contest the legality of a search and seizure. But by frankly recognizing that this aspect of the analysis belongs more properly under the heading of substantive Fourth Amendment doctrine than under the heading of standing, we think the decision of this issue will rest on sounder logical footing.</p>
<p></p>
<h2>C</h2>
<p>Here petitioners, who were passengers occupying a car which they neither owned nor leased, seek to analogize their position to that of the defendant in <i>Jones</i> v. <i>United States</i><i>.</i> <span class="star-pagination">*141</span> In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> petitioner was present at the time of the search of an apartment which was owned by a friend. The friend had given Jones permission to use the apartment and a key to it, with which Jones had admitted himself on the day of the search. He had a suit and shirt at the apartment and had slept there "maybe a night," but his home was elsewhere. At the time of the search, Jones was the only occupant of the apartment because the lessee was away for a period of several days. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S., at 259</a></span>. Under these circumstances, this Court stated that while one wrongfully on the premises could not move to suppress evidence obtained as a result of searching them,<sup>[9]</sup> "anyone legitimately on premises where a search occurs may challenge its legality." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 267</a></span>. Petitioners argue that their occupancy of the automobile in question was comparable to that of Jones in the apartment and that they therefore have standing to contest the legality of the searchor as we have rephrased the inquiry, that they, like Jones, had their Fourth Amendment rights violated by the search.</p>
<p>We do not question the conclusion in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that the defendant in that case suffered a violation of his personal Fourth Amendment rights if the search in question was unlawful. <span class="star-pagination">*142</span> Nonetheless, we believe that the phrase "legitimately on premises" coined in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> creates too broad a gauge for measurement of Fourth Amendment rights.<sup>[10]</sup> For example, applied literally, this statement would permit a casual visitor who has never seen, or been permitted to visit, the basement of another's house to object to a search of the basement if the visitor happened to be in the kitchen of the house at the time of the search. Likewise, a casual visitor who walks into a house one minute before a search of the house commences and leaves one minute after the search ends would be able to contest the legality of the search. The first visitor would have absolutely no interest or legitimate expectation of privacy in the basement, the second would have none in the house, and it advances no purpose served by the Fourth Amendment to permit either of them to object to the lawfulness of the search.<sup>[11]</sup></p>
<p>We think that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> on its facts merely stands for the unremarkable proposition that a person can have a legally sufficient interest in a place other than his own home so that the Fourth Amendment protects him from unreasonable governmental intrusion into that place. See <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States">362 U. S., at 263</a></span>, <span class="star-pagination">*143</span> 265. In defining the scope of that interest, we adhere to the view expressed in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and echoed in later cases that arcane distinctions developed in property and tort law between guests, licensees, invitees, and the like, ought not to control. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 266</a></span>; see <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961). But the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> statement that a person need only be "legitimately on premises" in order to challenge the validity of the search of a dwelling place cannot be taken in its full sweep beyond the facts of that case.</p>
<p><i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), provides guidance in defining the scope of the interest protected by the Fourth Amendment. In the course of repudiating the doctrine derived from <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span> (1928), and <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span> (1942), that if police officers had not been guilty of a common-law trespass they were not prohibited by the Fourth Amendment from eavesdropping, the Court in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> held that capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>; see <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7</a></span> (1977); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S. 745, 752</a></span> (1971). Viewed in this manner, the holding in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> can best be explained by the fact that Jones had a legitimate expectation of privacy in the premises he was using and therefore could claim the protection of the Fourth Amendment with respect to a governmental invasion of those premises, even though his "interest" in those premises might not have been a recognized property interest at common law.<sup>[12]</sup> See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>.</p>
<p><span class="star-pagination">*144</span> Our Brother WHITE in dissent expresses the view that by rejecting the phrase "legitimately on [the] premises" as the appropriate measure of Fourth Amendment rights, we are abandoning a thoroughly workable, "bright line" test in favor of a less certain analysis of whether the facts of a particular case give rise to a legitimate expectation of privacy. <i>Post,</i> <span class="star-pagination">*145</span> at 168. If "legitimately on premises" were the successful litmus test of Fourth Amendment rights that he assumes it is, his approach would have at least the merit of easy application, whatever it lacked in fidelity to the history and purposes of the Fourth Amendment. But a reading of lower court cases that have applied the phrase "legitimately on premises," and of the dissent itself, reveals that this expression is not a shorthand summary for a bright-line rule which somehow encapsulates the "core" of the Fourth Amendment's protections.<sup>[13]</sup></p>
<p><span class="star-pagination">*146</span> The dissent itself shows that the facile consistency it is striving for is illusory. The dissenters concede that "there comes a point when use of an area is shared with so many that one simply cannot reasonably expect seclusion." <i>Post,</i> at 164. But surely the "point" referred to is not one demarcating a line which is black on one side and white on another; it is inevitably a point which separates one shade of gray from another. We are likewise told by the dissent that a person "legitimately on <i>private</i> premises . . . , though his privacy is <i>not absolute,</i> is entitled to expect that he is sharing it only with those persons [allowed there] and that governmental officials will intrude only with <i>consent</i> or by complying with the Fourth Amendment." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i> (emphasis added). This single sentence describing the contours of the supposedly easily applied rule virtually abounds with unanswered questions: What are "private" premises? Indeed, what are the "premises?" It may be easy to describe the "premises" when one is confronted with a 1-room apartment, but what of the case of a 10-room house, or of a house with an attached garage that is searched? Also, if one's privacy is not absolute, how is it bounded? If he risks governmental intrusion "with consent," who may give that consent?</p>
<p>Again, we are told by the dissent that the Fourth Amendment assures that "<i>some</i> expectations of privacy are justified and will be protected from official intrusion." <i>Post,</i> at 166 (emphasis added). But we are not told which of many possible expectations of privacy are embraced within this sentence. And our dissenting Brethren concede that "perhaps the Constitution provides some degree less protection for the <span class="star-pagination">*147</span> personal freedom from unreasonable governmental intrusion when one does not have a possessory interest in the invaded private place." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i> But how much "less" protection is available when one does not have such a possessory interest?</p>
<p>Our disagreement with the dissent is not that it leaves these questions unanswered, or that the questions are necessarily irrelevant in the context of the analysis contained in this opinion. Our disagreement is rather with the dissent's bland and self-refuting assumption that there will not be fine lines to be drawn in Fourth Amendment cases as in other areas of the law, and that its rubric, rather than a meaningful exegesis of Fourth Amendment doctrine, is more desirable or more easily resolves Fourth Amendment cases.<sup>[14]</sup> In abandoning "legitimately on premises" for the doctrine that we announce today, we are not forsaking a time-tested and workable rule, which has produced consistent results when applied, solely for the sake of fidelity to the values underlying the Fourth Amendment. Rather, we are rejecting blind adherence to a phrase which at most has superficial clarity and which conceals underneath that thin veneer all of the problems of line drawing which must be faced in any conscientious effort to apply the Fourth Amendment. Where the factual premises for a rule are so generally prevalent that little would be lost and much would be gained by abandoning case-by-case analysis, we have not hesitated to do so. See <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 235</a></span> (1973). But the phrase "legitimately <span class="star-pagination">*148</span> on premises" has not been shown to be an easily applicable measure of Fourth Amendment rights so much as it has proved to be simply a label placed by the courts on results which have not been subjected to careful analysis. We would not wish to be understood as saying that legitimate presence on the premises is irrelevant to one's expectation of privacy, but it cannot be deemed controlling.</p>
<p></p>
<h2>D</h2>
<p>Judged by the foregoing analysis, petitioners' claims must fail. They asserted neither a property nor a possessory interest in the automobile, nor an interest in the property seized. And as we have previously indicated, the fact that they were "legitimately on [the] premises" in the sense that they were in the car with the permission of its owner is not determinative of whether they had a legitimate expectation of privacy in the particular areas of the automobile searched. It is unnecessary for us to decide here whether the same expectations of privacy are warranted in a car as would be justified in a dwelling place in analogous circumstances. We have on numerous occasions pointed out that cars are not to be treated identically with houses or apartments for Fourth Amendment purposes. See <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 12</a></span>; <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 561</a></span> (1976); <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion).<sup>[15]</sup> But here petitioners' claim is one which would fail even in an analogous situation in a dwelling place, since they made no showing that they had any legitimate expectation of privacy in the glove compartment or area under the seat of the car in which they were merely passengers. Like the trunk of an automobile, these are areas in which a <span class="star-pagination">*149</span> passenger <i>qua</i> passenger simply would not normally have a legitimate expectation of privacy. <i>Supra,</i> at 142.</p>
<p><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960) and <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), involved significantly different factual circumstances. Jones not only had permission to use the apartment of his friend, but had a key to the apartment with which he admitted himself on the day of the search and kept possessions in the apartment. Except with respect to his friend, Jones had complete dominion and control over the apartment and could exclude others from it. Likewise in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> the defendant occupied the telephone booth, shut the door behind him to exclude all others and paid the toll, which "entitled [him] to assume that the words he utter[ed] into the mouthpiece [would] not be broadcast to the world." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 352</a></span>.<sup>[16]</sup> Katz and Jones could legitimately expect privacy in the areas which were the subject of the search and seizure each sought to contest. No such showing was made by these petitioners with respect to those portions of the automobile which were searched and from which incriminating evidence was seized.<sup>[17]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*150</span> III</h2>
<p>The Illinois courts were therefore correct in concluding that it was unnecessary to decide whether the search of the car might have violated the rights secured to someone else by the Fourth and Fourteenth Amendments to the United States Constitution. Since it did not violate any rights of these petitioners, their judgment of conviction is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE POWELL, with whom THE CHIEF JUSTICE joins, concurring.</p>
<p>I concur in the opinion of the Court, and add these thoughts. I do not believe my dissenting Brethren correctly characterize the rationale of the Court's opinion when they assert that it ties "the application of the Fourth Amendment. . . to property law concepts." <i>Post,</i> at 156-157. On the contrary, I read the Court's opinion as focusing on whether there was a <i>legitimate</i> expectation of privacy protected by the Fourth Amendment.</p>
<p>The petitioners do not challenge the constitutionality of the police action in stopping the automobile in which they <span class="star-pagination">*151</span> were riding; nor do they complain of being made to get out of the vehicle. Rather, petitioners assert that their constitutionally protected interest in privacy was violated when the police, after stopping the automobile and making them get out, searched the vehicle's interior, where they discovered a sawed-off rifle under the front seat and rifle shells in the locked glove compartment. The question before the Court, therefore, is a narrow one: Did the search of their friend's automobile after they had left it violate any Fourth Amendment right of the petitioners?</p>
<p>The dissenting opinion urges the Court to answer this question by considering only the talisman of legitimate presence on the premises. To be sure, one of the two alternative reasons given by the Court for its ruling in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), was that the defendant had been legitimately on the premises searched. Since <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> however, the view that mere legitimate presence is enough to create a Fourth Amendment right has been questioned. See <i>ante,</i> at 147 n. 14. There also has been a signal absence of uniformity in the application of this theory. See <i>ante,</i> at 145-146 n. 13.</p>
<p>This Court's decisions since <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> have emphasized a sounder standard for determining the scope of a person's Fourth Amendment rights: Only legitimate expectations of privacy are protected by the Constitution. In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the Court rejected the notion that the Fourth Amendment protects places or property, ruling that the scope of the Amendment must be determined by the scope of privacy that a free people legitimately may expect. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 353</a></span>. As Mr. Justice Harlan pointed out in his concurrence, however, it is not enough that an individual desired or anticipated that he would be free from governmental intrusion. Rather, for an expectation to deserve the protection of the Fourth Amendment, it must "be one that society is prepared to recognize as `reasonable.' " See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span>.</p>
<p><span class="star-pagination">*152</span> The ultimate question, therefore, is whether one's claim to privacy from government intrusion is reasonable in light of all the surrounding circumstances. As the dissenting opinion states, this standard "will not provide law enforcement officials with a bright line between the protected and the unprotected." See <i>post,</i> at 168. Whatever the application of this standard may lack in ready administration, it is more faithful to the purposes of the Fourth Amendment than a test focusing solely or primarily on whether the defendant was legitimately present during the search.<sup>[1]</sup></p>
<p>In considering the reasonableness of asserted privacy expectations, the Court has recognized that no single factor invariably will be determinative. Thus, the Court has examined whether a person invoking the protection of the Fourth Amendment took normal precautions to maintain his privacy that is, precautions customarily taken by those seeking privacy. See, <i>e. g., </i><i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 11</a></span> (1977) ("By placing personal effects inside a doublelocked <span class="star-pagination">*153</span> footlocker, respondents manifested an expectation that the contents would remain free from public examination"); <i>Katz</i> v. <i>United States, supra,</i> at 352 ("One who occupies [a telephone booth], shuts the door behind him, and pays the toll that permits him to place a call is surely entitled to assume that the words he utters into the mouthpiece will not be broadcast to the world"). Similarly, the Court has looked to the way a person has used a location, to determine whether the Fourth Amendment should protect his expectations of privacy. In <i>Jones</i> v. <i>United States, supra</i><i>,</i> for example, the Court found that the defendant had a Fourth Amendment privacy interest in an apartment in which he had slept and in which he kept his clothing. The Court on occasion also has looked to history to discern whether certain types of government intrusion were perceived to be objectionable by the Framers of the Fourth Amendment. See <i>United States</i> v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 7-9</a></span>. And, as the Court states today, property rights reflect society's explicit recognition of a person's authority to act as he wishes in certain areas, and therefore should be considered in determining whether an individual's expectations of privacy are reasonable. See <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969).</p>
<p>The Court correctly points out that petitioners cannot invoke decisions such as <i><span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">Alderman</a></span></i> in support of their Fourth Amendment claim, as they had no property interest in the automobile in which they were riding. But this determination is only part of the inquiry required under <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> The petitioners' Fourth Amendment rights were not abridged here because none of the factors relied upon by this Court on prior occasions supports petitioners' claim that their alleged expectation of privacy from government intrusion was <i>reasonable.</i></p>
<p>We are concerned here with an automobile search. Nothing is better established in Fourth Amendment jurisprudence than the distinction between one's expectation of privacy in <span class="star-pagination">*154</span> an automobile and one's expectation when in other locations.<sup>[2]</sup> We have repeatedly recognized that this expectation in "an automobile . . . [is] significantly different from the traditional expectation of privacy and freedom in one's residence." <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#561" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 561</a></span> (1976). In <i>United States</i> v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick"><i>Chadwick, supra,</i> at 12</a></span>, the distinction was stated more broadly:</p>
<blockquote>"[T]his Court has recognized significant differences between motor vehicles and other property which permit warrantless searches of automobiles in circumstances in which warrantless searches would not be reasonable in other contexts. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <i>Preston</i> v. <i>United States,</i> [<span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>,] 366-367 [(1964)]; <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970). See also <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 367</a></span> (1976)."<sup>[3]</sup></blockquote>
<p>In <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick</a></span>,</i> the Court recognized a reasonable expectation of privacy with respect to one's locked footlocker, and rejected the Government's argument that luggage always should be equated with motor vehicles for Fourth Amendment purposes. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U. S., at 13</a></span>.</p>
<p>A distinction also properly may be made in some circumstances between the Fourth Amendment rights of passengers and the rights of an individual who has exclusive control of an automobile or of its locked compartments. In <i>South Dakota</i> v. <i>Opperman,</i> <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), for example, we <span class="star-pagination">*155</span> considered "the citizen's interest in the privacy of the contents of his automobile" where its doors were locked and windows rolled up. See <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#379" aria-description="Citation for case: South Dakota v. Opperman"><i>id.,</i> at 379</a></span> (POWELL J., concurring). Here there were three passengers and a driver in the automobile searched. None of the passengers is said to have had control of the vehicle or the keys. It is unrealisticas the shared experience of us all bears witnessto suggest that these passengers had any reasonable expectation that the car in which they had been riding would not be searched after they were lawfully stopped and made to get out. The minimal privacy that existed simply is not comparable to that, for example, of an individual in his place of abode, see <i>Jones</i> v. <i>United States, supra</i><i>;</i> of one who secludes himself in a telephone booth, <i>Katz</i> v. <i>United States, supra</i><i>;</i> or of the traveler who secures his belongings in a locked suitcase or footlocker. See <i>United States</i> v. <i><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra.</a></span></i><sup></sup>[4]</p>
<p>This is not an area of the law in which any "bright line" rule would safeguard both Fourth Amendment rights and the <span class="star-pagination">*156</span> public interest in a fair and effective criminal justice system. The range of variables in the fact situations of search and seizure is almost infinite. Rather than seek facile solutions, it is best to apply principles broadly faithful to Fourth Amendment purposes. I believe the Court has identified these principles.<sup>[5]</sup></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE BRENNAN, MR. JUSTICE MARSHALL, and MR. JUSTICE STEVENS join, dissenting.</p>
<p>The Court today holds that the Fourth Amendment protects property, not people, and specifically that a legitimate occupant of an automobile may not invoke the exclusionary rule and challenge a search of that vehicle unless he happens to own or have a possessory interest in it.<sup>[1]</sup> Though professing to acknowledge that the primary purpose of the Fourth Amendment's prohibition of unreasonable searches is the protection of privacynot propertythe Court nonetheless effectively ties the application of the Fourth Amendment and <span class="star-pagination">*157</span> the exclusionary rule in this situation to property law concepts. Insofar as passengers are concerned, the Court's opinion today declares an "open season" on automobiles. However unlawful stopping and searching a car may be, absent a possessory or ownership interest, no "mere" passenger may object, regardless of his relationship to the owner. Because the majority's conclusion has no support in the Court's controlling decisions, in the logic of the Fourth Amendment, or in common sense, I must respectfully dissent. If the Court is troubled by the practical impact of the exclusionary rule, it should face the issue of that rule's continued validity squarely instead of distorting other doctrines in an attempt to reach what are perceived as the correct results in specific cases. Cf. <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#536" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 536</a></span> (1976) (WHITE, J., dissenting).</p>
<p></p>
<h2>I</h2>
<p>Two intersecting doctrines long established in this Court's opinions control here. The first is the recognition of some cognizable level of privacy in the interior of an automobile. Though the reasonableness of the expectation of privacy in a vehicle may be somewhat weaker than that in a home, see <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#12" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 12-13</a></span> (1977), "[a] search, even of an automobile, is a substantial invasion of privacy. To protect that privacy from official arbitrariness, the Court always has regarded probable cause as the minimum requirement for a lawful search." <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#896" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 896</a></span> (1975) (footnote omitted). So far, the Court has not strayed from this application of the Fourth Amendment.<sup>[2]</sup></p>
<p>The second tenet is that when a person is legitimately present in a private place, his right to privacy is protected from unreasonable governmental interference even if he does <span class="star-pagination">*158</span> not own the premises. Just a few years ago, THE CHIEF JUSTICE, for a unanimous Court, wrote that the "[p]resence of the defendant at the search and seizure was held, in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> to be a sufficient source of standing in itself." <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">411 U. S. 223</a></span>, 227 n. 2 (1973); accord, <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#229" aria-description="Citation for case: Brown v. United States"><i>id.,</i> at 229</a></span> (one basis for Fourth Amendment protection is presence "on the premises at the time of the contested search and seizure"); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960) (individual legitimately present in friend's apartment may object to search of apartment). <i><span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">Brown</a></span></i> was not the first time we had recognized that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> established the rights of one legitimately in a private area against unreasonable governmental intrusion. <i>E. g., </i><i>Combs</i> v. <i>United States,</i> <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/#227" aria-description="Citation for case: Combs v. United States">408 U. S. 224, 227</a></span>, and n. 4 (1972); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 368</a></span>, and n. 5 (1968); <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#390" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 390</a></span> (1968). The Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> itself was unanimous in this regard, and its holding is not the less binding because it was an alternative one. See <i>Combs</i> v. <i>United States, supra,</i> at 227 n. 4.</p>
<p>These two fundamental aspects of Fourth Amendment law demand that petitioners be permitted to challenge the search and seizure of the automobile in this case. It is of no significance that a car is different for Fourth Amendment purposes from a house, for if there is some protection for the privacy of an automobile then the only relevant analogy is between a person legitimately in someone else's vehicle and a person legitimately in someone else's home. If both strands of the Fourth Amendment doctrine adumbrated above are valid, the Court must reach a different result. Instead, it chooses to eviscerate the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> principle, an action in which I am unwilling to participate.</p>
<p></p>
<h2>II</h2>
<p>Though we had reserved the very issue over 50 years ago, see <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925), and never expressly dealt with it again until today, many of our opinions have assumed that a mere passenger in an automobile <span class="star-pagination">*159</span> is entitled to protection against unreasonable searches occurring in his presence. In decisions upholding the validity of automobile searches, we have gone directly to the merits even though some of the petitioners did not own or possess the vehicles in question. <i>E. g., </i><i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973) (sole petitioner was not owner; in fact, owner was not in the automobile at all); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970) (sole petitioner was not owner); <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931). In <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span> (1968), the Court, with seven Members agreeing, upset the admission of evidence against three petitioners though only one owned the vehicle. See <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co."><i>id.,</i> at 221-222</a></span>. Similarly, in <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964), the Court unanimously overturned a search though the single petitioner was not the owner of the automobile. The Court's silence on this issue in light of its actions can only mean that, until now, we, like most lower courts,<sup>[3]</sup> had assumed that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> foreclosed the answer now supplied by the majority. That assumption was perfectly understandable, since all private premises would seem to be the same for the purposes of the analysis set out in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i></p>
<p></p>
<h2>III</h2>
<p>The logic of Fourth Amendment jurisprudence compels the result reached by the above decisions. Our starting point is "[t]he established principle . . . that suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated by the search itself . . . ." <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#171" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 171-172</a></span> (1969).<sup>[4]</sup> Though the Amendment protects one's liberty <span class="star-pagination">*160</span> and property interests against unreasonable seizures of self<sup>[5]</sup> and effects,<sup>[6]</sup> "the primary object of the Fourth Amendment [is] . . . the protection of privacy." <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#589" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 589</a></span> (1974) (plurality opinion).<sup>[7]</sup> And privacy is the <span class="star-pagination">*161</span> interest asserted here,<sup>[8]</sup> so the first step is to ascertain whether the premises searched "fall within a protected zone of privacy." <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#440" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 440</a></span> (1976). My Brethren in the majority assertedly do not deny that automobiles warrant at least some protection from official interference with privacy. Thus, the next step is to decide who is entitled, vis-à-vis the State, to enjoy that privacy. The answer to that question must be found by determining "whether petitioner had an interest in connection with the searched premises that gave rise to `a reasonable expectation [on his part] of freedom from governmental intrusion' upon those premises." <i>Combs</i> v. <i>United States,</i> <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/#227" aria-description="Citation for case: Combs v. United States">408 U. S., at 227</a></span>, quoting <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 368</a></span> (bracketed material in original).</p>
<p>Not only does <i><span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">Combs</a></span></i> supply the relevant inquiry, it also directs us to the proper answer. We recognized there that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> had held that one of those protected interests is created by legitimate presence on the searched premises, even absent any possessory interest. <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">408 U. S., at 227</a></span> n. 4. This makes unquestionable sense. We have concluded on numerous occasions that the entitlement to an expectation of privacy does not hinge on ownership:</p>
<blockquote>"What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection. . . . But what he seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351-352</a></span> (1967).</blockquote>
<p>In <i>Alderman</i> v. <i>United States, supra,</i> at 196, Mr. Justice Harlan, concurring in part and dissenting in part, noted that "our own past decisions . . . have decisively rejected the notion <span class="star-pagination">*162</span> that the accused must necessarily have a possessory interest in the premises before he may assert a Fourth Amendment claim." That rejection should not have been surprising in light of our conclusion as early as 1960 that "it is unnecessary and ill-advised to import into the law surrounding the constitutional right to be free from unreasonable searches and seizures subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>.<sup>[9]</sup> The proposition today overruled was stated most directly in <i>Mancusi</i> v. <i><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">DeForte, supra,</a></span></i> at 368: "[T]he protection of the Amendment depends not upon a property right in the invaded place but upon whether the area was one in which there was a reasonable expectation of freedom from governmental intrusion."</p>
<p>Prior to <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the lower federal courts had based Fourth Amendment rights upon possession or ownership of the items seized or the premises searched.<sup>[10]</sup> But <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> was foreshadowed by Mr. Justice Jackson's remark in 1948 that "even a guest may expect the shelter of the rooftree he is under against criminal intrusion." <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#461" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 461</a></span> (1948) (Jackson, J., joined by Frankfurter, J., concurring). Indeed, the decision today is contrary to Mr. Justice Brandeis' dissent in <i>Olmstead</i> v. <i>United States,</i> 277 <span class="star-pagination">*163</span> U. S. 438, 478 (1928), expressing a view of the Fourth Amendment thought to have been vindicated by <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i> The majority in <i>Olmstead</i> found the Fourth Amendment inapplicable absent a trespass on property rights. <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#466" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 466</a></span>. That is exactly what the Court holds in this case; but Mr. Justice Brandeis asserted 50 years ago that more than mere property rights are involved, and the Court's opinion in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> re-emphasized that " `[t]he premise that property interests control the right of the Government to search and seize has been discredited.' " <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U. S., at 353</a></span>, quoting <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 304</a></span> (1967). That logic led us inescapably to the conclusion that "[n]o less than an individual in a business office, in a friend's apartment, or in a taxicab, a person in a telephone booth may rely upon the protection of the Fourth Amendment." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S., at 352</a></span> (footnotes omitted). And if all of those situations are protected, surely a person riding in an automobile next to his friend the owner, or a child or wife with the father or spouse, must have some protection as well.</p>
<p>The same result is reached by tracing other lines of our Fourth Amendment decisions. If a nonowner may consent to a search merely because he is a joint user or occupant of a "premises," <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span> (1969),<sup>[11]</sup> then that same nonowner must have a protected privacy interest. The scope of the authority sufficient to grant a valid consent can hardly be broader than the contours of protected privacy.<sup>[12]</sup><span class="star-pagination">*164</span> And why should the owner of a vehicle be entitled to challenge the seizure from it of evidence even if he is absent at the time of the search, see <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), while a nonowner enjoying in person, and with the owner's permission, the privacy of an automobile is not so entitled?</p>
<p>In sum, one consistent theme in our decisions under the Fourth Amendment has been, until now, that "the Amendment does not shield only those who have title to the searched premises." <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#367" aria-description="Citation for case: Mancusi v. DeForte">392 U. S., at 367</a></span>. Though there comes a point when use of an area is shared with so many that one simply cannot reasonably expect seclusion, see <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#377" aria-description="Citation for case: Mancusi v. DeForte"><i>id.,</i> at 377</a></span> (WHITE, J., dissenting); <i>Air Pollution Variance Bd.</i> v. <i>Western Alfalfa Corp.,</i> <span class="citation" data-id="109032"><a href="/opinion/109032/air-pollution-variance-bd-of-colo-v-western-alfalfa-corp/#865" aria-description="Citation for case: Air Pollution Variance Bd. of Colo. v. Western Alfalfa Corp.">416 U. S. 861, 865</a></span> (1974), short of that limit a person legitimately on private premises knows the others allowed there and, though his privacy is not absolute, is entitled to expect that he is sharing it only with those persons and that governmental officials will intrude only with consent or by complying with the Fourth Amendment. See <i>Mancusi</i> v. <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#369" aria-description="Citation for case: Mancusi v. DeForte"><i>DeForte, supra,</i> at 369-370</a></span>.<sup>[13]</sup></p>
<p>It is true that the Court asserts that it is not limiting the Fourth Amendment bar against unreasonable searches to the protection of property rights, but in reality it is doing exactly that.<sup>[14]</sup> Petitioners were in a private place with the permission <span class="star-pagination">*165</span> of the owner, but the Court states that that is not sufficient to establish entitlement to a legitimate expectation of privacy. <i>Ante,</i> at 148. But if that is not sufficient, what would be? We are not told, and it is hard to imagine anything short of a property interest that would satisfy the majority. Insofar as the Court's rationale is concerned, no passenger in an automobile, without an ownership or possessory interest and regardless of his relationship to the owner, may claim Fourth Amendment protection against illegal stops and searches of the automobile in which he is rightfully present. The Court approves the result in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> but it fails to give any explanation why the facts in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> differ, in a fashion material to the Fourth Amendment, from the facts here.<sup>[15]</sup> More importantly, how is the Court able to avoid answering the question why presence in a private place with the owner's permission is insufficient? If it is "tautological to fall back on the notion that those expectations of privacy which are legitimate depend primarily on cases deciding exclusionary-rule issues in criminal cases," <i>ante,</i> at 144 n. 12, then it surely must be tautological to decide that issue simply by unadorned fiat.</p>
<p><span class="star-pagination">*166</span> As a control on governmental power, the Fourth Amendment assures that some expectations of privacy are justified and will be protected from official intrusion. That should be true in this instance, for if protected zones of privacy can only be purchased or obtained by possession of property, then much of our daily lives will be unshielded from unreasonable governmental prying, and the reach of the Fourth Amendment will have been narrowed to protect chiefly those with possessory interests in real or personal property. I had thought that <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> firmly established that the Fourth Amendment was intended as more than simply a trespass law applicable to the government. Katz had no possessory interest in the public telephone booth, at least no more than petitioners had in their friend's car; Katz was simply legitimately present. And the decision in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> was based not on property rights, but on the theory that it was essential to securing "conditions favorable to the pursuit of happiness"<sup>[16]</sup> that the expectation of privacy in question be recognized.<sup>[17]</sup></p>
<p>At most, one could say that perhaps the Constitution provides some degree less protection for the personal freedom from unreasonable governmental intrusion when one does not have a possessory interest in the invaded private place. But that would only change the extent of the protection; it would not free police to do the unreasonable, as does the decision today. And since the accused should be entitled to litigate the application of the Fourth Amendment where his privacy interest is merely arguable,<sup>[18]</sup> the failure to allow such litigation here is the more incomprehensible.</p>
<p></p>
<h2>
<span class="star-pagination">*167</span> IV</h2>
<p>The Court's holding is contrary not only to our past decisions and the logic of the Fourth Amendment but also to the everyday expectations of privacy that we all share. Because of that, it is unworkable in all the various situations that arise in real life. If the owner of the car had not only invited petitioners to join her but had said to them, "I give you a temporary possessory interest in my vehicle so that you will share the right to privacy that the Supreme Court says that I own," then apparently the majority would reverse. But people seldom say such things, though they may mean their invitation to encompass them if only they had thought of the problem.<sup>[19]</sup> If the nonowner were the spouse or child of the owner,<sup>[20]</sup> would the Court recognize a sufficient interest? If so, would distant relatives somehow have more of an expectation of privacy than close friends? What if the nonowner were driving with the owner's permission? Would nonowning drivers have more of an expectation of privacy than mere passengers? What about a passenger in a taxicab? <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> expressly recognized protection for such passengers. Why should Fourth Amendment rights be present when one pays a cabdriver for a ride but be absent when one is given a ride by a friend?</p>
<p>The distinctions the Court would draw are based on relationships between private parties, but the Fourth Amendment is concerned with the relationship of one of those parties to <span class="star-pagination">*168</span> the government. Divorced as it is from the purpose of the Fourth Amendment, the Court's essentially property-based rationale can satisfactorily answer none of the questions posed above. That is reason enough to reject it. The <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> rule is relatively easily applied by police and courts; the rule announced today will not provide law enforcement officials with a bright line between the protected and the unprotected.<sup>[21]</sup> Only rarely will police know whether one private party has or has not been granted a sufficient possessory or other interest by another private party. Surely in this case the officers had no such knowledge. The Court's rule will ensnare defendants and police in needless litigation over factors that should not be determinative of Fourth Amendment rights.<sup>[22]</sup></p>
<p>More importantly, the ruling today undercuts the force of the exclusionary rule in the one area in which its use is most certainly justifiedthe deterrence of bad-faith violations of the Fourth Amendment. See <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#536" aria-description="Citation for case: Stone v. Powell">428 U. S., at 536-542</a></span> (WHITE, J., dissenting). This decision invites police to engage in patently unreasonable searches every time an automobile contains more than one occupant. Should something be found, only the owner of the vehicle, or of the item, will have standing to seek suppression, and the evidence will <span class="star-pagination">*169</span> presumably be usable against the other occupants.<sup>[23]</sup> The danger of such bad faith is especially high in cases such as this one where the officers are only after the passengers and can usually infer accurately that the driver is the owner. The suppression remedy for those owners in whose vehicles something is found and who are charged with crime is small consolation for all those owners <i>and</i> occupants whose privacy will be needlessly invaded by officers following mistaken hunches not rising to the level of probable cause but operated on in the knowledge that someone in a crowded car will probably be unprotected if contraband or incriminating evidence happens to be found. After this decision, police will have little to lose by unreasonably searching vehicles occupied by more than one person.</p>
<p>Of course, most police officers will decline the Court's invitation and will continue to do their jobs as best they can in accord with the Fourth Amendment. But the very purpose of the Bill of Rights was to answer the justified fear that governmental agents cannot be left totally to their own devices, and the Bill of Rights is enforceable in the courts because human experience teaches that not all such officials will otherwise adhere to the stated precepts. Some policemen simply do act in bad faith, even if for understandable ends, and some deterrent is needed. In the rush to limit the applicability of the exclusionary rule somewhere, anywhere, the Court ignores precedent, logic, and common sense to exclude the rule's operation from situations in which, paradoxically, it is justified and needed.</p>
<h2>NOTES</h2>
<p>[*]  <i>Fred Inbau, Frank Carrington, Wayne W. Schmidt, Robert Smith,</i> and <i>James P. Costello</i> filed a brief for Effective Law Enforcement, Inc., as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Petitioners claim that they were never asked whether they owned the rifle or shells seized during the search and, citing <i>Combs</i> v. <i>United States,</i> <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">408 U. S. 224</a></span> (1972), argue that if the Court determines that a property interest in the items seized is an adequate ground for standing to object to their seizure, the Court should remand the case for further proceedings on the question whether petitioners owned the seized rifle or shells. Reply Brief for Petitioners 4 n. 2. Petitioners do not now assert that they own the rifle or the shells.
</p>
<p>We reject petitioners' suggestion. The proponent of a motion to suppress has the burden of establishing that his own Fourth Amendment rights were violated by the challenged search or seizure. See <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389-390</a></span> (1968); <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960). The prosecutor argued that petitioners lacked standing to challenge the search because they did not own the rifle, the shells or the automobile. Petitioners did not contest the factual predicates of the prosecutor's argument and instead, simply stated that they were not required to prove ownership to object to the search. App. 23. The prosecutor's argument gave petitioners notice that they were to be put to their proof on any issue as to which they had the burden, and because of their failure to assert ownership, we must assume, for purposes of our review, that petitioners do not own the rifle or the shells. <i>Combs</i> v. <i>United States, supra</i><i>,</i> was quite different. In <i><span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/" aria-description="Citation for case: Combs v. United States">Combs</a></span>,</i> the Government had not challenged Combs' standing at the suppression hearing and the issue of standing was not raised until the appellate level, where the Government conceded that its warrant was not based on probable cause. Because the record was "virtually barren of the facts necessary to determine" Combs' right to contest the search and seizure, the Court remanded the case for further proceedings. <span class="citation" data-id="108602"><a href="/opinion/108602/combs-v-united-states/#227" aria-description="Citation for case: Combs v. United States">408 U. S., at 227</a></span>. The Government had requested the Court to remand for further proceedings on this issue. Brief for United States in <i>Combs</i> v. <i>United States</i><i>,</i> O. T. 1971, No. 71-517, pp. 40-41.</p>
<p>[2]  Although <i>Jones</i> v. <i>United States</i> was based upon an interpretation of Fed. Rule Crim. Proc. 41 (e), the Court stated in <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span>, 173 n. 6 (1969), that Rule 41 (e) conforms to the general standard and is no broader than the constitutional rule. See <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348-349, n. 6</a></span> (1974).
</p>
<p>There is an aspect of traditional standing doctrine that was not considered in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and which we do not question. It is the proposition that a party seeking relief must allege such a personal stake or interest in the outcome of the controversy as to assure the concrete adverseness which Art. III requires. See, <i>e. g., </i><i>O'Shea</i> v. <i>Littleton,</i> <span class="citation" data-id="9425502"><a href="/opinion/108906/oshea-v-littleton/#493" aria-description="Citation for case: O&#x27;Shea v. Littleton">414 U. S. 488, 493</a></span> (1974); <i>Flast</i> v. <i>Cohen,</i> <span class="citation" data-id="9423763"><a href="/opinion/107731/flast-v-cohen/#99" aria-description="Citation for case: Flast v. Cohen">392 U. S. 83, 99</a></span> (1968); <i>Baker</i> v. <i>Carr,</i> <span class="citation" data-id="9422369"><a href="/opinion/106366/baker-v-carr/#204" aria-description="Citation for case: Baker v. Carr">369 U. S. 186, 204</a></span> (1962). Thus, a person whose Fourth Amendment rights were violated by a search or seizure, but who is not a defendant in a criminal action in which the illegally seized evidence is sought to be introduced, would not have standing to invoke the exclusionary rule to prevent use of that evidence in that action. See <i><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra,</a></span></i> at 352 n. 8.</p>
<p>[3]  The necessity for a showing of a violation of personal rights is not obviated by recognizing the deterrent purpose of the exclusionary rule, <i>Alderman</i> v. <i>United States, supra,</i> at 174. Despite the deterrent aim of the exclusionary rule, we never have held that unlawfully seized evidence is inadmissible in all proceedings or against all persons. See, <i>e. g., </i><i>United States</i> v. <i>Ceccolini,</i> <span class="citation" data-id="9427104"><a href="/opinion/109816/united-states-v-ceccolini/#275" aria-description="Citation for case: United States v. Ceccolini">435 U. S. 268, 275</a></span> (1978); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976); <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>. "[T]he application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served." <i><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Ibid.</a></span></i></p>
<p>[4]  We have not yet had occasion to decide whether the automatic-standing rule of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> survives our decision in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968). See <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#228" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 228-229</a></span> (1973). Such a rule is, of course, one which may allow a defendant to assert the Fourth Amendment rights of another.</p>
<p>[5]  The search of the apartment in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> was pursuant to a search warrant naming Jones and another woman as occupants of the apartment. The affidavit submitted in support of the search warrant alleged that Jones and the woman were involved in illicit narcotics traffic and kept a supply of heroin and narcotics paraphernalia in the apartment. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267-269</a></span>, and n. 2; App. in <i>Jones</i> v. <i>United States</i><i>,</i> O. T. 1959, No. 69, p. 1.</p>
<p>[6]  For these same prudential reasons, the Court in <i>Alderman</i> v. <i>United States</i> rejected the argument that <i>any</i> defendant should be enabled to apprise the court of unconstitutional searches and seizures and to exclude all such unlawfully seized evidence from trial, regardless of whether his Fourth Amendment rights were violated by the search <i>or</i> whether he was the "target" of the search. This expansive reading of the Fourth Amendment also was advanced by the petitioner in <i>Jones</i> v. <i>United States</i> and implicitly rejected by the Court. Brief for Petitioner in <i>Jones</i> v. <i>United States</i><i>,</i> O. T. 1959, No. 69, pp. 21-25.</p>
<p>[7]  So, for example, in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352</a></span> (1967), the Court focused on substantive Fourth Amendment law, concluded that a person in a telephone booth "may rely upon the protection of the Fourth Amendment," and then proceeded to determine whether the search was "unreasonable." In <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968), on the other hand, the Court concentrated on the issue of standing, decided that the defendant possessed it, and with barely any mention of the threshold substantive question of whether the search violated DeForte's own Fourth Amendment rights, went on to decide whether the search was "unreasonable." In both cases, however, the first inquiry was much the same.</p>
<p>[8]  This approach is consonant with that which the Court already has taken with respect to the Fifth Amendment privilege against selfincrimination, which also is a purely personal right. See, <i>e. g., </i><i>Bellis</i> v. <i>United States,</i> <span class="citation" data-id="9425735"><a href="/opinion/109046/bellis-v-united-states/#89" aria-description="Citation for case: Bellis v. United States">417 U. S. 85, 89-90</a></span> (1974); <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#327" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 327-328</a></span> (1973); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/#698" aria-description="Citation for case: United States v. White">322 U. S. 694, 698-699</a></span> (1944).</p>
<p>[9]  The Court in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> was quite careful to note that "wrongful" presence at the scene of a search would not enable a defendant to object to the legality of the search. <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>. The Court stated: "No just interest of the Government in the effective and rigorous enforcement of the criminal law will be hampered by recognizing that anyone legitimately on premises where a search occurs may challenge its legality by way of a motion to suppress, when its fruits are proposed to be used against him. <i>This would of course not avail those who, by virtue of their wrongful presence, cannot invoke the privacy of the premises searched.</i>" <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i> (emphasis added). Despite this clear statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> several lower courts inexplicably have held that a person present in a stolen automobile at the time of a search may object to the lawfulness of the search of the automobile. See, <i>e. g., </i><i>Cotton</i> v. <i>United States,</i> <span class="citation" data-id="274387"><a href="/opinion/274387/gary-leland-cotton-v-united-states/" aria-description="Citation for case: Gary Leland Cotton v. United States">371 F. 2d 385</a></span> (CA9 1967); <i>Simpson</i> v. <i>United States,</i> <span class="citation" data-id="9450769"><a href="/opinion/268148/george-frank-simpson-v-united-states/" aria-description="Citation for case: George Frank Simpson v. United States">346 F. 2d 291</a></span> (CA10 1965).</p>
<p>[10]  The Court in <i>Mancusi</i> v. <i><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">DeForte, supra</a></span></i><i>,</i> also must have been unsatisfied with the "legitimately on premises" statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i> DeForte was legitimately in his office at the time of the search and if the <i><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">Mancusi</a></span></i> Court had literally applied the statement from <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> DeForte's standing to object to the search should have been obvious. Instead, to determine whether DeForte possessed standing to object to the search, the Court inquired into whether DeForte's office was an area "in which there was a reasonable expectation of freedom from governmental intrusion." 392 U. S., at 368; see <i>id.,</i> at 376 (Black, J., dissenting).
</p>
<p>Unfortunately, with few exceptions, lower courts have literally applied this language from <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and have held that anyone legitimately on premises at the time of the search may contest its legality. See, <i>e. g., </i><i>Garza-Fuentes</i> v. <i>United States,</i> <span class="citation" data-id="281517"><a href="/opinion/281517/armando-garza-fuentes-and-tomas-elizalde-guereca-v-united-states/" aria-description="Citation for case: Armando Garza-Fuentes and Tomas Elizalde-Guereca v....">400 F. 2d 219</a></span> (CA5 1968); <i>State</i> v. <i>Bresolin,</i> <span class="citation" data-id="1190053"><a href="/opinion/1190053/state-v-bresolin/" aria-description="Citation for case: State v. Bresolin">13 Wash. App. 386</a></span>, <span class="citation" data-id="1190053"><a href="/opinion/1190053/state-v-bresolin/" aria-description="Citation for case: State v. Bresolin">534 P. 2d 1394</a></span> (1975).</p>
<p>[11]  This is not to say that such visitors could not contest the lawfulness of the seizure of evidence or the search if their own property were seized during the search.</p>
<p>[12]  Obviously, however, a "legitimate" expectation of privacy by definition means more than a subjective expectation of not being discovered. A burglar plying his trade in a summer cabin during the off season may have a thoroughly justified subjective expectation of privacy, but it is not one which the law recognizes as "legitimate." His presence, in the words of <i>Jones,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>, is "wrongful"; his expectation is not "one that society is prepared to recognize as `reasonable.' " <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span> (Harlan, J., concurring). And it would, of course, be merely tautological to fall back on the notion that those expectations of privacy which are legitimate depend primarily on cases deciding exclusionary-rule issues in criminal cases. Legitimation of expectations of privacy by law must have a source outside of the Fourth Amendment, either by reference to concepts of real or personal property law or to understandings that are recognized and permitted by society. One of the main rights attaching to property is the right to exclude others, see W. Blackstone, Commentaries, Book 2, ch. 1, and one who owns or lawfully possesses or controls property will in all likelihood have a legitimate expectation of privacy by virtue of this right to exclude. Expectations of privacy protected by the Fourth Amendment, of course, need not be based on a common-law interest in real or personal property, or on the invasion of such an interest. These ideas were rejected both in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones, supra,</a></span></i> and <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz, supra</a></span></i><i>.</i> But by focusing on legitimate expectations of privacy in Fourth Amendment jurisprudence, the Court has not altogether abandoned use of property concepts in determining the presence or absence of the privacy interests protected by that Amendment. No better demonstration of this proposition exists than the decision in <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969), where the Court held that an individual's property interest in his own home was so great as to allow him to object to electronic surveillance of conversations emanating from his home, even though he himself was not a party to the conversations. On the other hand, even a property interest in premises may not be sufficient to establish a legitimate expectation of privacy with respect to particular items located on the premises or activity conducted thereon. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Katz, supra,</i> at 351</a></span>; <i>Lewis</i> v. <i>United States,</i> <span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#210" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 210</a></span> (1966); <i>United States</i> v. <i>Lee,</i> <span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span> (1927); <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States">265 U. S. 57, 58-59</a></span> (1924).</p>
<p>[13]  An examination of lower court decisions shows that use of this purported "bright line" test has led to widely varying results. For example, compare <i>United States</i> v. <i>Westerbann-Martinez,</i> <span class="citation" data-id="1424578"><a href="/opinion/1424578/united-states-v-westerbann-martinez/" aria-description="Citation for case: United States v. Westerbann-Martinez">435 F. Supp. 690</a></span> (EDNY 1977) (defendant has standing to object to search of co-defendant's <i>person</i> at airport because defendant was lawfully present at time of search), with <i>Sumrall</i> v. <i>United States,</i> <span class="citation" data-id="277129"><a href="/opinion/277129/donald-wayne-sumrall-joe-jerrell-crocker-and-raymond-claud-nabors-v/" aria-description="Citation for case: Donald Wayne Sumrall, Joe Jerrell Crocker and Raymond...">382 F. 2d 651</a></span> (CA10 1967), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/1055/">389 U. S. 1055</a></span> (1968) (defendant did not have standing to object to search of codefendant's purse even though defendant present at time of search). Compare <i>Holloway</i> v. <i>Wolff,</i> <span class="citation" data-id="312637"><a href="/opinion/312637/william-r-holloway-v-charles-l-wolff-jr-warden-nebraska-penal-and/" aria-description="Citation for case: William R. Holloway v. Charles L. Wolff, Jr., Warden,...">482 F. 2d 110</a></span> (CA8 1973) (defendant has standing to object to search of bedroom in house of third person because lawfully in house at time of search even though no showing that defendant had ever been given permission to use, or had ever been in, bedroom), with <i>Northern</i> v. <i>United States,</i> <span class="citation" data-id="301437"><a href="/opinion/301437/clifford-northern-v-united-states/" aria-description="Citation for case: Clifford Northern v. United States">455 F. 2d 427</a></span> (CA9 1972) (defendant lacked standing to object to search of apartment-mate's bedroom even though present in apartment at time of search since no showing that defendant had permission to enter or use roommate's bedroom), and <i>United States</i> v. <i>Miller,</i> 145 U. S. App. D. C. 312, <span class="citation" data-id="9457446"><a href="/opinion/299539/united-states-v-dennis-o-miller/" aria-description="Citation for case: United States v. Dennis O. Miller">449 F. 2d 974</a></span> (1971) (defendant lawfully present in third person's office has standing to object to police entry into office since lawfully present but lacks standing to object to search of drawer of third person's desk since no showing that he had permission to open or use drawer). Compare <i>United States</i> v. <i>Tussell,</i> <span class="citation" data-id="1427556"><a href="/opinion/1427556/united-states-v-tussell/" aria-description="Citation for case: United States v. Tussell">441 F. Supp. 1092</a></span> (MD Pa. 1977) (lessee does not have standing because not present at time of search), with <i>United States</i> v. <i>Potter,</i> <span class="citation" data-id="1978947"><a href="/opinion/1978947/united-states-v-potter/" aria-description="Citation for case: United States v. Potter">419 F. Supp. 1151</a></span> (ND Ill. 1976) (lessee has standing even though not present when premises searched). Compare <i>United States</i> v. <i>Fernandez,</i> <span class="citation" data-id="2136957"><a href="/opinion/2136957/united-states-v-fernandez/" aria-description="Citation for case: United States v. Fernandez">430 F. Supp. 794</a></span> (ND Cal. 1976) (defendant with authorized access to apartment has standing even though not present at time of search), with <i>United States</i> v. <i><span class="citation" data-id="1978947"><a href="/opinion/1978947/united-states-v-potter/" aria-description="Citation for case: United States v. Potter">Potter, supra</a></span></i> (defendants with authorized access to premises lack standing because not present at the time of the search). Compare <i>United States</i> v. <i>Delguyd,</i> <span class="citation" data-id="9463115"><a href="/opinion/339194/united-states-v-anthony-f-delguyd-and-santo-maimone/" aria-description="Citation for case: United States v. Anthony F. Delguyd and Santo Maimone">542 F. 2d 346</a></span> (CA6 1976) (defendant stopped by police in parking lot of apartment house which he intended to visit lacks standing to object to subsequent search of apartment since not present in apartment at time of search), with <i>United States</i> v. <i>Fay,</i> <span class="citation" data-id="1872066"><a href="/opinion/1872066/united-states-ex-rel-eastman-v-fay/" aria-description="Citation for case: United States Ex Rel. Eastman v. Fay">225 F. Supp. 677</a></span> (SDNY 1963), rev'd on other grounds, <span class="citation multiple-matches"><a href="/c/F.%202d/333/28/">333 F. 2d 28</a></span> (CA2 1964) (defendant-invitee stopped in hallway of apartment building has standing to object to search of apartment he intended to visit).</p>
<p>[14]  Commentators have expressed similar dissatisfaction with reliance on "legitimate presence" to resolve Fourth Amendment questions. Trager &amp; Lobenfeld, The Law of Standing Under the Fourth Amendment, 41 Brooklyn L. Rev. 421, 448 (1975); White &amp; Greenspan, Standing to Object to Search and Seizure, <span class="citation no-link">118 U. Pa. L. Rev. 333</span>, 344-345 (1970). And, as we earlier noted, <i>supra,</i> at 142 n. 10, the Court in <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968), also implicitly recognized that the phrase "legitimately on premises" simply does not answer the question whether the search violated a defendant's "reasonable expectation of freedom from governmental intrusion." See <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte"><i>id.,</i> at 368</a></span>.</p>
<p>[15]  As we noted in <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,</i> "[o]ne's expectation of privacy in an automobile and of freedom in its operation are significantly different from the traditional expectation of privacy and freedom in one's residence." 428 U. S., at 561.</p>
<p>[16]  The dissent states that <i>Katz</i> v. <i>United States</i> expressly recognized protection for passengers of taxicabs and asks why that protection should not also extend to these petitioners. <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> relied on <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span> (1960), as support for that proposition. The question of Rios' right to contest the search was not presented to or addressed by the Court and the property seized appears to have belonged to Rios. See <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951). Additionally, the facts of that case are quite different from those of the present case. Rios had hired the cab and occupied the rear passenger section. When police stopped the cab, he placed a package he had been holding on the floor of the rear section. The police saw the package and seized it after defendant was removed from the cab.</p>
<p>[17]  For reasons which they do not explain, our dissenting Brethren repeatedly criticize our "holding" that unless one has a common-law property interest in the premises searched, one cannot object to the search. We have rendered no such "holding," however. To the contrary, we have taken pains to reaffirm the statements in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> that "arcane distinctions developed in property . . . law . . . ought not to control." <i>Supra,</i> at 143, and n. 12. In a si

[...TRUNCATED 21086 of 141086 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Rawlings v. Kentucky.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Rawlings v. Kentucky"
type: case
citation: "448 U.S. 98 (1980)"
parallel_cite: "100 S. Ct. 2556; 65 L. Ed. 2d 633"
neutral_cite: 1980 U.S. LEXIS 142
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-06-25
docket: 79-5146
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rawlings v. Kentucky
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110326/rawlings-v-kentucky/"
  cluster_id: 110326
  opinion_id: 110326
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Katz v. United States]]", "[[United States v. Salvucci]]", "[[Byrd v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "ownership", "consent"]
holding: "Owning the items seized is not enough to challenge a search; a defendant must have a legitimate expectation of privacy in the PLACE…"
lake:
  record_id: Rawlings v. Kentucky
  status: verified
  projected_at: 2026-07-06
---

# Rawlings v. Kentucky

*448 U.S. 98 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
While police detained the occupants of a house and waited for a search warrant, Rawlings dumped a quantity of drugs into the purse of a companion, Vanessa Cox, whom he had known only a few days. When the warrant arrived and an officer searched Cox's purse, the drugs were found; Rawlings immediately admitted they were his. He moved to suppress, claiming his ownership of the drugs gave him a privacy interest in the purse.

## Issue
Whether a defendant who owns the items seized, but lacks a legitimate expectation of privacy in the place searched, may challenge the search — and whether ownership of the items alone suffices.

## Rule
Ownership of the seized items does not, by itself, confer a legitimate expectation of privacy in the place searched. After [[Rakas v. Illinois]], "the two inquiries merge into one: whether governmental officials violated any legitimate expectation of privacy held by petitioner." — 448 U.S. at 106. ^pin-106

Although the defendant's ownership of the property "is undoubtedly one fact to be considered," *[[Rakas v. Illinois|Rakas]]* "emphatically rejected the notion that 'arcane' concepts of property law ought to control the ability to claim the protections of the Fourth Amendment." — 448 U.S. at 105. ^pin-105

## Application
Rawlings had known Cox only a few days, had never before sought or obtained access to her purse, had no right to exclude others from it (another acquaintance had free access), and admitted he held no expectation that the purse would remain free from governmental intrusion; the precipitous "bailment" of the drugs showed no effort to maintain privacy. He therefore had no legitimate expectation of privacy in Cox's purse, and his ownership of the drugs did not supply one. He could not challenge the search.

## Conclusion
Owning the seized drugs did not give Rawlings a privacy interest in Cox's purse; he could not contest the search, and the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Rawlings* applies [[Rakas v. Illinois]]: privacy in the *[[United States v. Place|place]]* searched, not ownership of the items, governs the ability to challenge a search.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Rawlings v. Kentucky*, 448 U.S. 98 (1980) — https://www.courtlistener.com/opinion/110326/rawlings-v-kentucky/ — pinpoints: 105, 106.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "231a1e8aedd4dacb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Rawlings v. Kentucky"}, "payload": {"all": [{"cite": "448 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "448"}, {"cite": "100 S. Ct. 2556", "page": "2556", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "65 L. Ed. 2d 633", "page": "633", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "65"}, {"cite": "1980 U.S. LEXIS 142", "page": "142", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "448 U.S. 98", "official": {"cite": "448 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "448"}, "official_selection_present": true, "record_id": "Rawlings v. Kentucky"}}
{"assertion_id": "1203c0948594333a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-105", "record_id": "Rawlings v. Kentucky"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-105", "pinpoint_status": "slip-only", "quote": "is undoubtedly one fact to be considered,", "quote_fidelity": "mismatch", "record_id": "Rawlings v. Kentucky", "star_marker": null}}
{"assertion_id": "7482a82172e7fadd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-106", "record_id": "Rawlings v. Kentucky"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-106", "pinpoint_status": "slip-only", "quote": "--- # Rawlings v. Kentucky *448 U.S. 98 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police detained the occupants of a house and waited for a search warrant, Rawlings dumped a quantity of drugs into the purse of a companion, Vanessa Cox, whom he had known only a few days. When the warrant arrived and an officer searched Cox's purse, the drugs were found; Rawlings immediately admitted they were his. He moved to suppress, claiming his ownership of the drugs gave him a privacy interest in the purse. ## Issue Whether a defendant who owns the items seized, but lacks a legitimate expectation of privacy in the place searched, may challenge the search — and whether ownership of the items alone suffices. ## Rule Ownership of the seized items does not, by itself, confer a legitimate expectation of privacy in the place searched. After [[Rakas v. Illinois]],", "quote_fidelity": "mismatch", "record_id": "Rawlings v. Kentucky", "star_marker": null}}
{"assertion_id": "d4a68ab35a577d2b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Rawlings v. Kentucky"}, "payload": {"as_of_content": "1980-06-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Rawlings v. Kentucky", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Rawlings v. Kentucky

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rawlings v. Kentucky",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rawlings v. Kentucky",
    "case_name_short": "Rawlings",
    "case_name_full": "Rawlings v. Kentucky",
    "input_case_name": "Rawlings v. Kentucky",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-06-25",
    "year": 1980,
    "docket": "79-5146",
    "cluster_id": 110326,
    "lead_opinion_id": 110326,
    "sibling_ids": [
      110326,
      9428038,
      9428039,
      9428040,
      9428041
    ],
    "absolute_url": "/opinion/110326/rawlings-v-kentucky/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "448 U.S. 98",
      "volume": "448",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 2556",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 633",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 142",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "142",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "448 U.S. 98",
        "volume": "448",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 2556",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "2556",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "65 L. Ed. 2d 633",
        "volume": "65",
        "reporter": "L. Ed. 2d",
        "page": "633",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 142",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "142",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "448 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "448 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-106",
      "page": null,
      "quote": "--- # Rawlings v. Kentucky *448 U.S. 98 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background While police detained the occupants of a house and waited for a search warrant, Rawlings dumped a quantity of drugs into the purse of a companion, Vanessa Cox, whom he had known only a few days. When the warrant arrived and an officer searched Cox's purse, the drugs were found; Rawlings immediately admitted they were his. He moved to suppress, claiming his ownership of the drugs gave him a privacy interest in the purse. ## Issue Whether a defendant who owns the items seized, but lacks a legitimate expectation of privacy in the place searched, may challenge the search \u2014 and whether ownership of the items alone suffices. ## Rule Ownership of the seized items does not, by itself, confer a legitimate expectation of privacy in the place searched. After [[Rakas v. Illinois]],",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-105",
      "page": null,
      "quote": "is undoubtedly one fact to be considered,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rawlings v. Kentucky",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532256,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532251,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William A. Nash, Jr. and David Lewis",
          "cluster_id": 2736697,
          "cite": [
            "100 A.3d 157",
            "2014 D.C. App. LEXIS 393"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 2713876,
          "cite": [
            "2014 SD 50",
            "851 N.W.2d 719",
            "2014 S.D. LEXIS 65",
            "2014 WL 3558758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 2487584,
          "cite": [
            "79 So. 3d 1013",
            "2012 La. LEXIS 268",
            "2012 WL 415483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Joshua Daniel Fleming",
          "cluster_id": 4472496,
          "cite": [
            "790 N.W.2d 560",
            "2010 Iowa Sup. LEXIS 110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane1_negative"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kimmelman v. Morrison",
          "cluster_id": 111724,
          "cite": [
            "91 L. Ed. 2d 305",
            "106 S. Ct. 2574",
            "477 U.S. 365",
            "1986 U.S. LEXIS 63",
            "54 U.S.L.W. 4789"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powers v. Ohio",
          "cluster_id": 112570,
          "cite": [
            "113 L. Ed. 2d 411",
            "111 S. Ct. 1364",
            "499 U.S. 400",
            "1991 U.S. LEXIS 1857",
            "59 U.S.L.W. 4268",
            "91 Daily Journal DAR 3732",
            "91 Cal. Daily Op. Serv. 2259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111301,
          "cite": [
            "83 L. Ed. 2d 720",
            "105 S. Ct. 733",
            "469 U.S. 325",
            "1985 U.S. LEXIS 41",
            "53 U.S.L.W. 4083"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Matthews",
          "cluster_id": 2362733,
          "cite": [
            "805 S.W.2d 776",
            "1990 Tenn. Crim. App. LEXIS 597"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oliver v. United States",
          "cluster_id": 111146,
          "cite": [
            "80 L. Ed. 2d 214",
            "104 S. Ct. 1735",
            "466 U.S. 170",
            "1984 U.S. LEXIS 55",
            "52 U.S.L.W. 4425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ballard",
          "cluster_id": 1533349,
          "cite": [
            "987 S.W.2d 889",
            "1999 Tex. Crim. App. LEXIS 14",
            "1999 WL 89535"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
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
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lance W.",
          "cluster_id": 1421847,
          "cite": [
            "694 P.2d 744",
            "37 Cal. 3d 873",
            "210 Cal. Rptr. 631",
            "1985 Cal. LEXIS 241"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Oody",
          "cluster_id": 1740610,
          "cite": [
            "823 S.W.2d 554",
            "1991 Tenn. Crim. App. LEXIS 405"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2629957,
          "cite": [
            "117 P.3d 476",
            "32 Cal. Rptr. 3d 759",
            "36 Cal. 4th 1114",
            "2005 Cal. Daily Op. Serv. 7196",
            "2005 Daily Journal DAR 9801",
            "2005 Cal. LEXIS 8908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parks v. Commonwealth",
          "cluster_id": 1315235,
          "cite": [
            "270 S.E.2d 755",
            "221 Va. 492",
            "1980 Va. LEXIS 269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez-Portoreal",
          "cluster_id": 2033638,
          "cite": [
            "666 N.E.2d 207",
            "88 N.Y.2d 99",
            "643 N.Y.S.2d 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rawlings v. Kentucky:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgwMzYxNjAwMDAwJnM9MjYzMDkyNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNDImcz00NzU4NDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 0,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110326 OR 9428038 OR 9428039 OR 9428040 OR 9428041)",
    "indexed_citing_opinions": 1565,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110326,
        "count": 1385,
        "count_source": "search"
      },
      {
        "opinion_id": 9428038,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9428039,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428040,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428041,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2426,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rawlings-v-kentucky.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MTQ1MzQmcz0xMDAyMDg3NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110326+OR+9428038+OR+9428039+OR+9428040+OR+9428041%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110326,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 110161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 270326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 304598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110326,
        "cited_id": 2463407,
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
    "date_created": "2026-07-05T17:23:01Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:26:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:23:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rawlings v. Kentucky

```
<div>
<center><b><span class="citation" data-id="9428038"><a href="/opinion/110326/rawlings-v-kentucky/" aria-description="Citation for case: Rawlings v. Kentucky">448 U.S. 98</a></span> (1980)</b></center>
<center><h1>RAWLINGS<br>
v.<br>
KENTUCKY.</h1></center>
<center>No. 79-5146.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 26, 1980.</center>
<center>Decided June 25, 1980.</center>
CERTIORARI TO THE SUPREME COURT OF KENTUCKY.
<p><span class="star-pagination">*99</span> <i>J. Vincent Aprile II</i> argued the cause and filed briefs for petitioner.</p>
<p><i>Victor Fox,</i> Assistant Attorney General of Kentucky, argued the cause for respondent. With him on the brief were <i>Steven L. Beshear,</i> Attorney General, and <i>Gerald Henry</i> and <i>Patrick B. Kimberlin III,</i> Assistant Attorneys General.</p>
<p><span class="star-pagination">*100</span> MR. JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>Petitioner David Rawlings was convicted by the Commonwealth of Kentucky on charges of trafficking in, and possession of, various controlled substances. Throughout the proceedings below, Rawlings challenged the admissibility of certain evidence and statements on the ground that they were the fruits of an illegal detention and illegal searches. The trial court, the Kentucky Court of Appeals, and the Supreme Court of Kentucky all rejected Rawlings' challenges. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./444/989/">444 U. S. 989</a></span>, and now affirm.</p>
<p></p>
<h2>I</h2>
<p>In the middle of the afternoon on October 18, 1976, six police officers armed with a warrant for the arrest of one Lawrence Marquess on charges of drug distribution arrived at Marquess' house in Bowling Green, Ky. In the house at the time the police arrived were one of Marquess' housemates, Dennis Saddler, and four visitors, Keith Northern, Linda Braden, Vanessa Cox, and petitioner David Rawlings. While searching unsuccessfully in the house for Marquess, several police officers smelled marihuana smoke and saw marihuana seeds on the mantel in one of the bedrooms. After conferring briefly, Officers Eddie Railey and John Bruce left to obtain a search warrant. While Railey and Bruce were gone, the other four officers detained the occupants of the house in the living room, allowing them to leave only if they consented to a body search. Northern and Braden did consent to such a search and were permitted to depart. Saddler, Cox, and petitioner remained seated in the living room.</p>
<p>Approximately 45 minutes later, Railey and Bruce returned with a warrant authorizing them to search the house. Railey read the warrant to Saddler, Cox, and petitioner, and also read <i>"Miranda"</i> warnings from a card he carried in his pocket. At that time, Cox was seated on a couch with petitioner seated to her left. In the space between them was Cox's handbag.</p>
<p>After Railey finished his recitation, he approached petitioner <span class="star-pagination">*101</span> and told him to stand. Officer Don Bivens simultaneously approached Cox and ordered her to empty the contents of her purse onto a coffee table in front of the couch. Among those contents were a jar containing 1,800 tablets of LSD and a number of smaller vials containing benzphetamine, methamphetamine, methyprylan, and pentobarbital, all of which are controlled substances under Kentucky law.</p>
<p>Upon pouring these objects out onto the coffee table, Cox turned to petitioner and told him "to take what was his." App. 62. Petitioner, who was standing in response to Officer Railey's command, immediately claimed ownership of the controlled substances. At that time, Railey searched petitioner's person and found $4,500 in cash in petitioner's shirt pocket and a knife in a sheath at petitioner's side. Railey then placed petitioner under formal arrest.</p>
<p>Petitioner was indicted for possession with intent to sell the various controlled substances recovered from Cox's purse. At the suppression hearing, he testified that he had flown into Bowling Green about a week before his arrest to look for a job and perhaps to attend the local university. He brought with him at that time the drugs later found in Cox's purse. Initially, petitioner stayed in the house where the arrest took place as the guest of Michael Swank, who shared the house with Marquess and Saddler. While at a party at that house, he met Cox and spent at least two nights of the next week on a couch at Cox's house.</p>
<p>On the morning of petitioner's arrest, Cox had dropped him off at Swank's house where he waited for her to return from class. At that time, he was carrying the drugs in a green bank bag. When Cox returned to the house to meet him, petitioner dumped the contents of the bank bag into Cox's purse. Although there is dispute over the discussion that took place, petitioner testified that he "asked her if she would carry this for me, and she said, `yes'. . . ." App. 42.<sup>[1]</sup> Petitioner <span class="star-pagination">*102</span> then left the room to use the bathroom and, by the time he returned, discovered that the police had arrived to arrest Marquess.</p>
<p>The trial court denied petitioner's motion to suppress the drugs and the money and to exclude the statements made by petitioner when the police discovered the drugs. According to the trial court, the warrant obtained by the police authorized them to search Cox's purse. Moreover, even if the search of the purse was illegal, the trial court believed that petitioner lacked "standing" to contest that search. Finally, the trial court believed that the search that revealed the money and the knife was permissible "under the exigencies of the situation." <i>Id.,</i> at 21. After a bench trial, petitioner was found guilty of possession with intent to sell LSD and of possession of benzphetamine, methamphetamine, methyprylan, and pentobarbital.</p>
<p><span class="star-pagination">*103</span> The Kentucky Court of Appeals affirmed. Disagreeing with the trial court, the appellate court held that petitioner did have "standing" to dispute the legality of the search of Cox's purse but that the detention of the five persons present in the house and the subsequent searches were legitimate because the police had probable cause to arrest all five people in the house when they smelled the marihuana smoke and saw the marihuana seeds.</p>
<p>The Supreme Court of Kentucky in turn affirmed, but again on a somewhat different rationale. See <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d 348</a></span> (1979). According to the Supreme Court, petitioner had no "standing" because he had no "legitimate or reasonable expectation of freedom from governmental intrusion" into Cox's purse. <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth"><i>Id.,</i> at 350</a></span>, citing <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). Moreover, according to the Supreme Court, the search uncovering the money in petitioner's pocket, which search followed petitioner's admission that he owned the drugs in Cox's purse, was justifiable as incident to a lawful arrest based on probable cause.</p>
<p></p>
<h2>II</h2>
<p>In this Court, petitioner challenges three aspects of the judgment below. First, he claims that he did have a reasonable expectation of privacy in Cox's purse so as to allow him to challenge the legality of the search of that purse.<sup>[2]</sup> Second, petitioner argues that his admission of ownership was the fruit of an illegal detention that began when the police refused to let the occupants of the house leave unless they consented to a search. Third, petitioner contends that the search uncovering the money and the knife was itself illegal.</p>
<p></p>
<h2>
<span class="star-pagination">*104</span> A</h2>
<p>In holding that petitioner could not challenge the legality of the search of Cox's purse, the Supreme Court of Kentucky looked primarily to our then recent decision in <i>Rakas</i> v. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Illinois, supra</a></span></i><i>,</i> where we abandoned a separate inquiry into a defendant's "standing" to contest an allegedly illegal search in favor of an inquiry that focused directly on the substance of the defendant's claim that he or she possessed a "legitimate expectation of privacy" in the area searched. See <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). In the present case, the Supreme Court of Kentucky looked to the "totality of the circumstances," including petitioner's own admission at the suppression hearing that he did not believe that Cox's purse would be free from governmental intrusion,<sup>[3]</sup> and held that petitioner "[had] not made a sufficient showing that his legitimate or reasonable expectations of privacy were violated" by the search of the purse. <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d, at 350</a></span>.</p>
<p>We believe that the record in this case supports that conclusion. Petitioner, of course, bears the burden of proving not only that the search of Cox's purse was illegal, but also that he had a legitimate expectation of privacy in that purse. See <span class="star-pagination">*105</span> <i>Rakas</i> v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#131" aria-description="Citation for case: Rakas v. Illinois"><i>Illinois, supra,</i> at 131, n. 1</a></span>; <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389-390</a></span> (1968). At the time petitioner dumped thousands of dollars worth of illegal drugs into Cox's purse, he had known her for only a few days. According to Cox's uncontested testimony, petitioner had never sought or received access to her purse prior to that sudden bailment. Contrast <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#259" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 259</a></span> (1960). Nor did petitioner have any right to exclude other persons from access to Cox's purse. See <i>Rakas</i> v. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois"><i>Illinois, supra,</i> at 149</a></span>. In fact, Cox testified that Bob Stallons, a longtime acquaintance and frequent companion of Cox's, had free access to her purse and on the very morning of the arrest had rummaged through its contents in search of a hairbrush. Moreover, even assuming that petitioner's version of the bailment is correct and that Cox did consent to the transfer of possession,<sup>[4]</sup> the precipitous nature of the transaction hardly supports a reasonable inference that petitioner took normal precautions to maintain his privacy. Contrast <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#11" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 11</a></span> (1977); <i>Katz</i> v. <i>United States, supra,</i> at 352. In addition to all the foregoing facts, the record also contains a frank admission by petitioner that he had no subjective expectation that Cox's purse would remain free from governmental intrusion, an admission credited by both the trial court and the Supreme Court of Kentucky. See n. 3, <i>supra,</i> and accompanying text.</p>
<p>Petitioner contends nevertheless that, because he claimed ownership of the drugs in Cox's purse, he should be entitled to challenge the search regardless of his expectation of privacy. We disagree. While petitioner's ownership of the drugs is undoubtedly one fact to be considered in this case, <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> emphatically rejected the notion that "arcane" concepts of property law ought to control the ability to claim the protections of the Fourth Amendment. See <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 149-150, n. 17</a></span>. See also <i>United States</i> v. <i>Salvucci, ante,</i> at 91-92. <span class="star-pagination">*106</span> Had petitioner placed his drugs in plain view, he would still have owned them, but he could not claim any legitimate expectation of privacy. Prior to <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> petitioner might have been given "standing" in such a case to challenge a "search" that netted those drugs but probably would have lost his claim on the merits. After <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> the two inquiries merge into one: whether governmental officials violated any legitimate expectation of privacy held by petitioner.</p>
<p>In sum, we find no reason to overturn the lower court's conclusion that petitioner had no legitimate expectation of privacy in Cox's purse at the time of the search.</p>
<p></p>
<h2>B</h2>
<p>We turn, then, to petitioner's contention that the occupants of the house were illegally detained by the police and that his admission to ownership of the drugs was a fruit of that illegal detention. Somewhat surprisingly, none of the courts below confronted this issue squarely, even though it would seem to be presented under any analysis of this case except that adopted by the Kentucky Court of Appeals, which concluded that the police officers were entitled to arrest the five occupants of the house as soon as they smelled marihuana smoke and saw the marihuana seeds.</p>
<p>We can assume both that this issue was properly presented in the Kentucky courts and that the police violated the Fourth and Fourteenth Amendments by detaining petitioner and his companions in the house while they obtained a search warrant for the premises. Even given such a constitutional violation, however, exclusion of petitioner's admissions would not be necessary unless his statements were the result of his illegal detention. As we noted in <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 603</a></span> (1975), where we rejected a "but for" approach to the admissibility of such statements, "persons arrested illegally frequently may decide to confess, as an act of free will unaffected by the initial illegality." In <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> we also set forth <span class="star-pagination">*107</span> the standard for determining whether such statements were tainted by antecedent illegality:</p>
<blockquote>"The question whether a confession is the product of a free will . . . must be answered on the facts of each case. No single fact is dispositive. . . . The <i>Miranda</i> warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered. The temporal proximity of the arrest and the confession, the presence of intervening circumstances, and, particularly, the purpose and flagrancy of the official misconduct are all relevant. The voluntariness of the statement is a threshold requirement. And the burden of showing admissibility rests, of course, on the prosecution." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 603-604</a></span> (footnotes and citations omitted).</blockquote>
<p>See also <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#218" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 218</a></span> (1979). As already noted, the lower courts did not undertake the inquiry suggested by <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span>.</i> Nevertheless, as in <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> itself, we believe that "the trial resulted in a record of amply sufficient detail and depth from which the determination may be made." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>.</p>
<p>First, we observe that petitioner received <i>Miranda</i> warnings only moments before he made his incriminating statements, a consideration <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> treated as important, although not dispositive, in determining whether the statements at issue were obtained by exploitation of an illegal detention.</p>
<p>Second, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> calls our attention to the "temporal proximity of the arrest and the confession. . . ." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#603" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 603</a></span>. In this case, petitioner and his companions were detained for a period of approximately 45 minutes. Although under the strictest of custodial conditions such a short lapse of time might not suffice to purge the initial taint, we believe it necessary to examine the precise conditions under which the occupants of this house were detained. By all accounts, the three people who chose not to consent to a body search in order to leave sat <span class="star-pagination">*108</span> quietly in the living room or, at least initially, moved freely about the first floor of the house. Upon being informed that he would be detained until Officers Railey and Bruce returned with a search warrant, Dennis Saddler "just went on in and got a cup of coffee and sat down and started waiting" for the officers to return. Tr. 109. When asked by petitioner's counsel whether there was "any show of force or violence by you or Dave or anybody else," Saddler explained:</p>
<blockquote>"A Oh, no. One person tried to sick my four and a half month old dog on one of the officers. (laughing)</blockquote>
<blockquote>"Q48 You're saying that in a joking manner?</blockquote>
<blockquote>"A Yeah. He just wagged his tail.</blockquote>
<blockquote>"Q49 And other than that, that's the most violent thing you proposed toward these police officers; is that correct?</blockquote>
<blockquote>"A Yes sir. I wouldthey were more or less courteous to us and were trying to bewe offered them coffee or a drink of water or whatever they wanted." <i>Id.,</i> at 113.</blockquote>
<p>According to Saddler, petitioner's first reaction when the officers told him that he would be detained pending issuance of a search warrant was to "[get] up and put an album on. . . ." <i>Id.,</i> at 110. As even the dissenting judge in the Court of Appeals noted: "[A]ll witnesses for both sides of this litigation agreed to the congenial atmosphere existing during the forty-five minute interval. . . ." App. 73 (Lester, J., dissenting). We think that these circumstances outweigh the relatively short period of time that elapsed between the initiation of the detention and petitioner's admissions.</p>
<p>Third, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> suggests that we inquire whether any circumstances intervened between the initial detention and the challenged statements. Here, where petitioner's admissions were apparently spontaneous reactions to the discovery of his drugs in Cox's purse, we have little doubt that this factor weighs heavily in favor of a finding that petitioner acted "of free will unaffected by the initial illegality." 422 U. S., at <span class="star-pagination">*109</span> 603. Nor need we speculate as to petitioner's motivations in admitting ownership of the drugs, since he explained them later to Lawrence Marquess and Dennis Saddler. Under examination by petitioner's counsel, Marquess testified as follows:</p>
<blockquote>"Q1 Mr. Marquess, when you were talking to David Rawlings in the jail, and he told you that the things were dumped out on the table and that he admitted they were his, did he tell you why he did that?</blockquote>
<blockquote>"A Well, he said Vanessa [Cox] was freaking out, you know, or something.</blockquote>
<blockquote>"Q2 Did he tell you that he did that to protect her or words to that effect?</blockquote>
<blockquote>"A Well, now, I mean he said he was going to take what was his, I mean, he wasn't going to try to pin that on her." Tr. 130.</blockquote>
<p>Saddler offered additional insight into petitioner's motivations:</p>
<blockquote>"Q114 Did Dave Rawlings make any statements to you in jail about any of these substances?</blockquote>
<blockquote>"A Yes sir.</blockquote>
<blockquote>"Q115 And would you tell the Court what statements he made?</blockquote>
<blockquote>"A well, his main concern was whether or not Vanessa Cox was going to say anything, and he just kept talking and harping on that, and I don't know how many times he mentioned it, you know, `I hope she doesn't break,' or hope she doesn't talk. And I saw her walking on the sidewalk through the windows and got a little upset about that because we all thought she turned State's evidence." <i>Id.,</i> at 103.</blockquote>
<p>Fourth, <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> mandates consideration of "the purpose and flagrancy of the official misconduct. . . ." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 604</a></span>. The officers who detained petitioner and his companions uniformly testified that they took those measures to avoid the <span class="star-pagination">*110</span> asportation or destruction of the marihuana they thought was present in the house and that they believed that a warrant authorizing them to search the house would also authorize them to search the five occupants of the house. While the legality of temporarily detaining a person at the scene of suspected drug activity to secure a search warrant may be an open question,<sup>[5]</sup> and while the officer's belief about the scope of the warrant they obtained may well have been erroneous under our recent decision in <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), the conduct of the police here does not rise to the level of conscious or flagrant misconduct requiring prophylactic exclusion of petitioner's statements. Contrast <i>Brown</i> v. <i>Illinois, supra,</i> at 605.</p>
<p>Finally, while <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Brown</a></span></i> requires that the voluntariness of the statement be established as a threshold requirement, petitioner has not argued here or in any other court that his admission to ownership of the drugs was anything other than voluntary. Thus, examining the totality of circumstances present in this case, we believe that the Commonwealth of Kentucky has carried its burden of showing that petitioner's statements were acts of free will unaffected by any illegality in the initial detention.</p>
<p></p>
<h2>C</h2>
<p>Petitioner also contends that the search of his person that uncovered the money and the knife was illegal. Like the <span class="star-pagination">*111</span> Supreme Court of Kentucky, we have no difficulty upholding this search as incident to petitioner's formal arrest. Once petitioner admitted ownership of the sizable quantity of drugs found in Cox's purse, the police clearly had probable cause to place petitioner under arrest. Where the formal arrest followed quickly on the heels of the challenged search of petitioner's person, we do not believe it particularly important that the search preceded the arrest rather than vice versa. See <i>Bailey</i> v. <i>United States,</i> 128 U. S. App. D. C. 354, 357, <span class="citation multiple-matches"><a href="/c/F.%202d/389/305/">389 F. 2d 305</a></span>, 308 (1967); <i>United States</i> v. <i>Brown,</i> 150 U. S. App. D. C. 113, 114, <span class="citation" data-id="304598"><a href="/opinion/304598/united-states-v-reginald-t-brown/#950" aria-description="Citation for case: United States v. Reginald T. Brown">463 F. 2d 949, 950</a></span> (1972). See also <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291</a></span> (1973); <i>United States</i> v. <i>Gorman,</i> <span class="citation" data-id="270326"><a href="/opinion/270326/united-states-v-robert-william-gorman-and-edward-terrence-roche/#160" aria-description="Citation for case: United States v. Robert William Gorman and Edward...">355 F. 2d 151, 160</a></span> (CA2 1965) (dictum), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/1024/">384 U. S. 1024</a></span> (1966).<sup>[6]</sup></p>
<p></p>
<h2>III</h2>
<p>Having found no error in the lower courts' refusal to suppress the evidence challenged by petitioner, we believe that the judgment of the Supreme Court of Kentucky should be, and the same hereby is,</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion, but I write separately to explain my somewhat different approach to the issues addressed in Part II-A thereof.</p>
<p>In my view, <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978), recognized two analytically distinct but "invariably intertwined" issues of substantive Fourth Amendment jurisprudence. <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#139" aria-description="Citation for case: Rakas v. Illinois"><i>Id.,</i> at 139</a></span>. The first is "whether [a] disputed search or seizure has infringed an interest of the defendant which the Fourth Amendment was designed to protect," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#140" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 140</a></span>; the second <span class="star-pagination">*112</span> is whether "the challenged search or seizure violated [that] Fourth Amendment righ[t]," <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">ibid.</a></span></i> The first of these questions is answered by determining whether the defendant has a "legitimate expectation of privacy" that has been invaded by a governmental search or seizure. The second is answered by determining whether applicable cause and warrant requirements have been properly observed.</p>
<p>I agree with the Court that these two inquiries "merge into one," <i>ante,</i> at 106, in the sense that both are to be addressed under the principles of Fourth Amendment analysis developed in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), and its progeny. But I do not read today's decision, or <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span>,</i> as holding that it is improper for lower courts to treat these inquiries as distinct components of a Fourth Amendment claim. Indeed, I am convinced that it would invite confusion to hold otherwise. It remains possible for a defendant to prove that his legitimate interest of privacy was invaded, and yet fail to prove that the police acted illegally in doing so. And it is equally possible for a defendant to prove that the police acted illegally, and yet fail to prove that his own privacy interest was affected.</p>
<p>Nor do I read this Court's decisions to hold that property interests cannot be, in some circumstances at least, weighty factors in establishing the existence of Fourth Amendment rights. Not every concept of ownership or possession is "arcane." Not every interest in property exists only in the desiccated atmosphere of ancient maxims and dusty books. Earlier this Term the Court recognized that "the right to exclude" is an essential element of modern property rights. <i>Kaiser Aetna</i> v. <i>United States,</i> <span class="citation" data-id="9427728"><a href="/opinion/110161/kaiser-aetna-v-united-states/#179" aria-description="Citation for case: Kaiser Aetna v. United States">444 U. S. 164, 179-180</a></span> (1979). In my view, that "right to exclude" often may be a principal determinant in the establishment of a legitimate Fourth Amendment interest. Accordingly, I would confine analysis to the facts of this case. On those facts, however, I agree that petitioner's possessory interest in the vials of controlled <span class="star-pagination">*113</span> substances is not sufficient to create a privacy interest in Vanessa Cox's purse, and that such an interest was not otherwise conferred by any agreement between petitioner and Cox.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, concurring in part.</p>
<p>Although I join Parts I and II-A of the Court's opinion, I do not join Parts II-B, II-C, and III because I believe that the fruits inquiry undertaken in Part II-B should not be done in the first instance in this Court. As the Court recognizes, the Supreme Court of Kentucky did not address the question whether petitioner's admission to ownership of the drugs was the fruit of an illegal detention, even though the question was presented there. The state-court majority did state that in concluding that the search of petitioner's person was incident to a valid arrest it "disregard[ed] as irrelevant the detention during the period in which the officers were procuring a search warrant." The court also observed that "[t]his search was not explored in detail at the suppression hearing" and that "the sequence of the search of the purse and Rawlings' admission of ownership of the drugs is not clearly established in the record." The court then concluded that "[c]learly, after Rawlings admitted ownership of the drugs, the officers were entitled to arrest and search the person, or search and then arrest." <span class="citation" data-id="9778383"><a href="/opinion/2463407/rawlings-v-commonwealth/#350" aria-description="Citation for case: Rawlings v. Commonwealth">581 S. W. 2d 348, 350</a></span> (1979).</p>
<p>In proceeding in this manner, the Supreme Court of Kentucky plainly failed properly to dispose of a federal question, as the Court implicitly recognizes. Because the fruits question was never addressed below and was barely mentioned in the briefs before this Court, I would vacate the judgment below and remand to permit the state court to address the question under the correct legal standard. This Court should not attempt to decide a factual issue on a record that the <span class="star-pagination">*114</span> state court itself apparently thought inadequate for that purpose.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>The vials of pills found in Vanessa Cox's purse and petitioner's admission that they belonged to him established his guilt conclusively. The State concedes, as it must, that the search of the purse was unreasonable and in violation of the Fourth Amendment, see <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), and the Court assumes that the detention which led to the search, the seizure, and the admissions also violated the Fourth Amendment, <i>ante,</i> at 106. Nevertheless, the Court upholds the conviction. I dissent.</p>
<p></p>
<h2>I</h2>
<p>The Court holds first that petitioner may not object to the introduction of the pills into evidence because the unconstitutional actions of the police officers did not violate his personal Fourth Amendment rights. To reach this result, the Court holds that the Constitution protects an individual against unreasonable searches and seizures only if he has "a `legitimate expectation of privacy' in the area searched." <i>Ante,</i> at 104. This holding cavalierly rejects the fundamental principle, unquestioned until today, that an interest in either the place searched or the property seized is sufficient to invoke the Constitution's protections against unreasonable searches and seizures.</p>
<p>The Court's examination of previous Fourth Amendment cases begins and endsas it must if it is to reach its desired conclusionwith <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span> (1978). Contrary to the Court's assertion, however, <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> did not establish that the Fourth Amendment protects individuals against unreasonable searches and seizures only if they have a privacy interest in the place searched. The question before the Court in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> was whether the defendants could establish <span class="star-pagination">*115</span> their right to Fourth Amendment protection simply by showing that they were "legitimately on [the] premises" searched, see <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 267</a></span> (1960). Overruling that portion of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> the Court held that when a Fourth Amendment objection is based on an interest in the place searched, the defendant must show an actual invasion of his personal privacy interest. The petitioners in <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Rakas</a></span></i> did not claim that they had standing either under the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> automatic standing rule for persons charged with possessory offenses, which the Court overrules today, see <i>United States</i> v. <i>Salvucci, ante,</i> p. 83, or because their possessory interest in the items seized gave them "actual standing." No Fourth Amendment claim based on an interest in the property seized was before the Court, and, consequently, the Court did not and could not have decided whether such a claim could be maintained. In fact, the Court expressly disavowed any intention to foreclose such a claim ("This is not to say that such [casual] visitors could not contest the lawfulness of the seizure of evidence or the search if their own property were seized during the search," <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#142" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 142, n. 11</a></span>), and suggested its continuing validity ("[P]etitioners' claims must fail. They asserted neither a property nor a possessory interest in the automobile, <i>nor an interest in the property seized,</i>" <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#148" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 148</a></span> (emphasis supplied)).</p>
<p>The decision today, then, is not supported by the only case directly cited in its favor.<sup>[*]</sup> Further, the Court has ignored <span class="star-pagination">*116</span> a long tradition embodying the opposite view. <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span> (1951), for example, involved a seizure of contraband alleged to belong to the defendant from a hotel room occupied by his two aunts. The Court rejected the Government's argument that because the search of the room did not invade Jeffers' privacy he lacked standing to suppress the evidence. It held that standing to object to the seizure could not be separated from standing to object to the search, for "[t]he search and seizure are . . . incapable of being untied." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Id.,</i> at 52</a></span>. The Court then concluded that Jeffers "unquestionably had standing . . . unless the contraband nature of the narcotics seized precluded his assertion, for purposes of the exclusionary rule, of <i>a property interest therein." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Ibid.</a></span></i> (emphasis supplied).</p>
<p>Similarly, <i>Jones</i> v. <i>United States, supra</i><i>,</i> is quite plainly premised on the understanding that an interest in the seized property is sufficient to establish that the defendant "himself was the victim of an invasion of privacy." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>. The Court observed that the "conventional standing requirement," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#262" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 262</a></span>, required the defendant to "claim either to have <i>owned or possessed the seized property</i> or to have had a substantial possessory interest in the premises searched," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 261</a></span> (emphasis supplied). The Court relaxed that rule for defendants charged with possessory offenses because "[t]he same element . . . which has caused a dilemma, <i>i. e.,</i> that <i>possession both convicts and confers standing,</i> eliminates any necessity for a preliminary showing of an interest in the premises searched <i>or the property seized,</i> which ordinarily is <span class="star-pagination">*117</span> required when standing is challenged." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 263</a></span> (emphasis supplied). Instead, "[t]he possession on the basis of which petitioner is to be and was convicted suffices to give him standing," <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#264" aria-description="Citation for case: Jones v. United States"><i>id.,</i> at 264</a></span>.</p>
<p><i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968), proceeded upon a like understanding. The Court there reiterated that prior to <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> "a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor <i>of the seized property</i> or that he had a possessory interest in the searched premises." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S., at 389-390</a></span> (emphasis supplied). <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> had changed that rule only with respect to defendants charged with possessory offenses, so the defendant Garrett, who was charged with armed robbery, had to establish standing. Because he was not "legitimately on [the] premises" at the time of the search, see <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Jones, supra,</i> at 267</a></span>, "[t]he only, or at least the most natural, way in which he could found standing to object to the admission of the suitcase was to testify that he was its owner." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#391" aria-description="Citation for case: Simmons v. United States">390 U. S., at 391</a></span> (footnote omitted). See also <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#228" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 228</a></span> (1973); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#367" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 367</a></span> (1968).</p>
<p>The Court's decision today is not wrong, however, simply because it is contrary to our previous cases. It is wrong because it is contrary to the Fourth Amendment, which guarantees that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." The Court's reading of the Amendment is far too narrow. The Court misreads the guarantee of security <i>"in</i> their persons, houses, papers, and effects, <i>against</i> unreasonable searches and seizures" to afford protection only against unreasonable searches and seizures <i>of</i> persons and places.</p>
<p>The Fourth Amendment, it seems to me, provides in plain language that if one's security in one's "effects" is disturbed by an unreasonable search and seizure, one has been the victim of a constitutional violation; and so it has always been <span class="star-pagination">*118</span> understood. Therefore the Court's insistence that in order to challenge the legality of the search one must also assert a protected interest in the premises is misplaced. The interest in the item seized is quite enough to establish that the defendant's personal Fourth Amendment rights have been invaded by the government's conduct.</p>
<p>The idea that a person cannot object to a search unless he can show an interest in the premises, even though he is the owner of the seized property, was squarely rejected almost 30 years ago in <i>United States</i> v. <i><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">Jeffers, supra</a></span></i><i>.</i> There the Court stated:</p>
<blockquote>"The Government argues . . . that the search did not invade respondent's privacy and that he, therefore, lacked the necessary standing to suppress the evidence seized. The significant act, it says, is the seizure of the goods of the respondent without a warrant. We do not believe the events are so easily isolable. Rather they are bound together by one sole purposeto locate and seize the narcotics of respondent. The search and seizure are, therefore, incapable of being untied. To hold that this search and seizure were lawful as to the respondent would permit a quibbling distinction to overturn a principle which was designed to protect a fundamental right." <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#52" aria-description="Citation for case: United States v. Jeffers"><i>Id.,</i> at 52</a></span>.</blockquote>
<p>When the government seizes a person's property, it interferes with his constitutionally protected right to be secure in his effects. That interference gives him the right to challenge the reasonableness of the government's conduct, including the seizure. If the defendant's property was seized as the result of an unreasonable search, the seizure cannot be other than unreasonable.</p>
<p>In holding that the Fourth Amendment protects only those with a privacy interest in the place searched, and not those with an ownership or possessory interest in the things seized, the Court has turned the development of the law of search <span class="star-pagination">*119</span> and seizure on its head. The history of the Fourth Amendment shows that it was designed to protect property interests as well as privacy interests; in fact, until <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> the question whether a person's Fourth Amendment rights had been violated turned on whether he had a property interest in the place searched or the items seized. <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> and <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), expanded our view of the protections afforded by the Fourth Amendment by recognizing that privacy interests are protected even if they do not arise from property rights. But that recognition was never intended to exclude interests that had historically been sheltered by the Fourth Amendment from its protection. Neither <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> nor <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> purported to provide an exclusive definition of the interests protected by the Fourth Amendment. Indeed, as <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> recognized: "That Amendment protects individual privacy against certain kinds of governmental intrusion, but its protections go further, and often have nothing to do with privacy at all." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S., at 350</a></span>. Those decisions freed Fourth Amendment jurisprudence from the constraints of "subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical." <i>Jones,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>. Rejection of those finely drawn distinctions as irrelevant to the concerns of the Fourth Amendment did not render property rights wholly outside its protection, however. Not every concept involving property rights, we should remember, is "arcane." Cf. <i>ante,</i> at 105.</p>
<p>In fact, the Court rather inconsistently denies that property rights may, by themselves, entitle one to the protection of the Fourth Amendment, but simultaneously suggests that a person may claim such protection only if his expectation of privacy in the premises searched is so strong that he may exclude all others from that place. See <i>ante,</i> at 105-106; <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#149" aria-description="Citation for case: Rakas v. Illinois">439 U. S., at 149</a></span>. Such a harsh threshold requirement <span class="star-pagination">*120</span> was not imposed even in the heyday of a property rights oriented Fourth Amendment.</p>
<p></p>
<h2>II</h2>
<p>Petitioner also contends that his admission of ownership of the drugs should have been suppressed as the fruit of an unlawful detention. The state courts did not pass on that claim, and no factual record was developed which would shed light on the proper disposition of the claim. In such circumstances, it would be appropriate for us to defer to the state court and permit it to make the initial determination. Nevertheless, the majority proceeds to dispose of petitioner's claim by concluding that, even if the detention was illegal, "petitioner's statements were acts of free will unaffected by any illegality in the initial detention." <i>Ante,</i> at 110. I disagree.</p>
<p>Petitioner's admissions, far from being "spontaneous," <i>ante,</i> at 108, were made in response to Vanessa Cox's demand that petitioner "take what was his." In turn, it is plain that her statement was the direct product of the illegal search of her purse. And that search was made possible only because the police refused to let anyone in the house depart unless they "consented" to a body search; that detention the Court has assumed was illegal. Under these circumstances petitioner's admissions were obviously the fruit of the illegal detention and should have been suppressed.</p>
<p></p>
<h2>III</h2>
<p>In the words of Mr. Justice Frankfurter: "A decision [of a Fourth Amendment claim] may turn on whether one gives that Amendment a place second to none in the Bill of Rights, or considers it on the whole a kind of nuisance, a serious impediment in the war against crime." <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#157" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 157</a></span> (1947) (dissenting opinion). Today a majority of the Court has substantially cut back the protection afforded by the Fourth Amendment and the ability of the <span class="star-pagination">*121</span> people to claim that protection, apparently out of concern lest the government's ability to obtain criminal convictions be impeded. A slow and steady erosion of the ability of victims of unconstitutional searches and seizures to obtain a remedy for the invasion of their rights saps the constitutional guarantee of its life just as surely as would a substantive limitation. Because we are called on to decide whether evidence should be excluded only when a search has been "successful," it is easy to forget that the standards we announce determine what government conduct is reasonable in searches and seizures directed at persons who turn out to be innocent as well as those who are guilty. I continue to believe that ungrudging application of the Fourth Amendment is indispensable to preserving the liberties of a democratic society. Accordingly, I dissent.</p>
<h2>NOTES</h2>
<p>[1]  At petitioner's trial, Vanessa Cox described the transfer of possession quite differently. She testified that, as she and petitioner were getting ready to leave the house, petitioner asked "would you please carry this for me" and simultaneously dumped the drugs into her purse. According to Cox, she looked into her purse, saw the drugs, and said "would you please take this, I do not want this in my purse." Petitioner allegedly replied "okay, just a minute, I will," and then went out of the room. At that point the police entered the house. Tr. 12-14. David Saddler, who was in the next room at the time of the transfer, corroborated Cox's version of the events, testifying that he heard Cox say "I do not want this in my purse" and that he heard petitioner reply "don't worry" or something to that effect. <i>Id.,</i> at 100.
</p>
<p>Although none of the lower courts specifically found that Cox did not consent to the bailment, the trial court clearly was skeptical about petitioner's version of events:</p>
<p>"The Court finds it unbelievable that just of his own volition, David Rawlings put the contraband in the purse of Mrs. Cox just a minute before the officers knocked on the door. He had been carrying these things around Bowling Green in a bank deposit sack for days, either on his person or in his pocket, and it is unworthy of belief that just immediately before the officers knocked on the door that he put them in the purse of Vanessa Cox. It is far more plausible to believe that he saw the officers pull up out front and then elected to `push them off' on Vanessa Cox, believing that search was probable, possible, and emminent [<i>sic</i>]." App. 21.</p>
<p>[2]  Petitioner also claims that he is entitled to "automatic standing" to contest the legality of the search that uncovered the drugs. See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). Our decision today in <i>United States</i> v. <i>Salvucci, ante,</i> p. 83, disposes of this contention adversely to him.</p>
<p>[3]  Under questioning by his own counsel, petitioner testified as follows:
</p>
<p>"Q72 Did you feel that Vannessa [<i>sic</i>] Cox's purse would be free from the intrusion of the officers as you sat there? When you put the pills in her purse, did you feel that they would be free from governmental intrusion?</p>
<p>"A No sir." App. 48.</p>
<p>The trial court also credited this statement, noting immediately:</p>
<p>"You know what, I believe this boy tells the truth. You all wanted to bring him in here before the Court, and he said, `no, I want a jury.' He said `no, I don't understand that.' And I don't blame him for not understanding that. That's the first time I've ever seen such a thing brought on before this Court, and I've been here for quite a few years as an attorney, of course.</p>
<p>"Now, no question but what the boy fully understood what was meant by that. None at all in the Court's mind. If you want to go ahead, you can do so." <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Ibid.</a></span></i></p>
<p>[4]  But see n. 1, <i>supra.</i></p>
<p>[5]  "The reasonableness of seizures that are less intrusive than a traditional arrest, see <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 209-210</a></span> (1979); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968), depends `on a balance between the public interest and the individual's right to personal security free from arbitrary interference by law officers.' <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span> (1977); <i>United States</i> v. <i>Brignoni-Ponce,</i> [<span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975)]. Consideration of the constitutionality of such seizures involves a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." <i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#50" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 50-51</a></span> (1979).</p>
<p>[6]  The fruits of the search of petitioner's person were, of course, not necessary to support probable cause to arrest petitioner.</p>
<p>[*]  The Court invites the reader to "contrast" <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), which it expressly overrules, and to "see" <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 389-390</a></span> (1968). <i>Ante,</i> at 105, 104. The passage cited in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> contains the following language: "At one time, a defendant who wished to assert a Fourth Amendment objection was required to show that he was the owner or possessor <i>of the seized property</i> or that he had a possessory interest in the searched premises." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S., at 389-390</a></span> (emphasis supplied). The Court in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> then observed that <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> had "relaxed" those standing requirements by holding that in a case charging a possessory offense "the Government is precluded from denying that the defendant has the requisite possessory interest to challenge the admission of the evidence. . . ." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#390" aria-description="Citation for case: Simmons v. United States">390 U. S., at 390</a></span>. The Court also "contrasts" two other cases in connection with its subsidiary point that a "bailment" that is "precipitous" may not be enough to show that a person "took normal precautions to maintain his privacy." <i>Ante,</i> at 105. The Court also cites <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), as the source of the phrase "legitimate expectation of privacy." But <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> did not purport to restrict the interest protected by the Fourth Amendment, see <i>infra,</i> at 119-120.</p>

</div>
```

---
