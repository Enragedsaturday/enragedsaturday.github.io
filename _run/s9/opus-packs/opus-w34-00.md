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

## GROUP: content/cases/Postal Service v. Konan.md  (`case`, 5 assertions)

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
{"assertion_id": "4ed9edd355ac8edd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 24-351, slip op. (U.S. 2026)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Postal Service v. Konan", "year": "2026"}}
{"assertion_id": "5a08877a489d8909", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Federal Tort Claims Act's postal exception, which preserves the United States' sovereign immunity for claims 'arising out of the loss, miscarriage, or negligent transmission of letters or postal matter,' bars claims for the intentional nondelivery of mail, because both 'miscarriage' and 'loss' of mail — as ordinarily understood when the FTCA was enacted — can result from the Postal Service's intentional failure to deliver it.", "title": "Postal Service v. Konan"}}
{"assertion_id": "fe54f2f414bfe2e1", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Postal Service v. Konan"}}
{"assertion_id": "9d35d8ce00d3c5ae", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Postal Service v. Konan"}}
{"assertion_id": "fe44b80d86215f81", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Postal Service v. Konan", "varies_by_point": "false"}}
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

## GROUP: content/cases/Rivas-Villegas v. Cortesluna.md  (`case`, 5 assertions)

### content_page

```
---
title: "Rivas-Villegas v. Cortesluna"
type: case
citation: "595 U.S. 1 (2021)"
parallel_cite: "142 S. Ct. 4; 211 L. Ed. 2d 164"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-10-18
docket: 20-1539
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-10-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rivas-Villegas v. Cortesluna
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/5290447/rivas-villegas-v-cortesluna/"
  cluster_id: 5290447
  opinion_id: 5118993
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[City of Tahlequah v. Bond]]", "[[District of Columbia v. Wesby]]", "[[Saucier v. Katz]]", "[[Pearson v. Callahan]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "excessive-force", "clearly-established", "per-curiam"]
holding: "For QI, the plaintiff must identify a case that put the officer on notice that his specific conduct was unlawful, 'in light of the specific context of the case, not as a broad general proposition.'"
lake:
  record_id: Rivas-Villegas v. Cortesluna
  status: verified
  projected_at: 2026-07-06
---

# Rivas-Villegas v. Cortesluna

*595 U.S. 1 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responded to a 911 call from a crying 12-year-old reporting that she, her mother, and her sister had locked themselves in a room because the mother's boyfriend, Cortesluna, was trying to hurt them and had a chainsaw. Officers ordered Cortesluna out and onto the ground and saw a knife in his left pocket. While removing the knife and handcuffing him, Officer Rivas-Villegas briefly placed his knee on the left side of Cortesluna's back for no more than eight seconds. Cortesluna sued under § 1983 for excessive force; the Ninth Circuit denied [[Qualified Immunity|qualified immunity]], relying on its precedent *LaLonde v. County of Riverside*.

## Issue
Whether Rivas-Villegas was entitled to [[Qualified Immunity|qualified immunity]] because he did not violate clearly established law.

## Rule
Clearly established law must be particularized to the case. The "clearly established" inquiry "must be undertaken in light of the specific context of the case, not as a broad general proposition." — 595 U.S. 1 (slip op., at 4) (quoting *Brosseau v. Haugen*). ^pin-op4

"[T]o show a violation of clearly established law, Cortesluna must identify a case that put Rivas-Villegas on notice that his specific conduct was unlawful." — *Id.* (slip op., at 5). ^pin-op5

## Application
Cortesluna identified no Supreme Court case addressing facts like these, and the Ninth Circuit relied solely on *LaLonde*, which is materially distinguishable: *LaLonde* involved a mere noise complaint and an unarmed suspect on whose back an officer "deliberately dug his knee" causing lasting injury, whereas here officers responded to a serious domestic-violence call possibly involving a chainsaw, Cortesluna had a knife in his pocket he had appeared to reach for, and Rivas-Villegas placed his knee on Cortesluna's back for no more than eight seconds beside the knife being retrieved. *LaLonde* therefore did not give fair notice that Rivas-Villegas's conduct was unlawful.

## Conclusion
Because no precedent clearly established that Rivas-Villegas's specific conduct was unlawful, he was entitled to [[Qualified Immunity|qualified immunity]]; the Ninth Circuit was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. Decided the same day as the companion qualified-immunity [[Common Legal Terms#per-curiam|per curiam]] [[City of Tahlequah v. Bond]], reinforcing that "clearly established" law must be defined with specificity.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Rivas-Villegas v. Cortesluna*, 595 U.S. 1 (2021) (per curiam) — https://www.courtlistener.com/opinion/5290447/rivas-villegas-v-cortesluna/ — pinpoints: slip op., at 4, 5 (CL carries the slip opinion; cluster 5290447 → opinion 5118993).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1246c531b4ff074c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "595 U.S. 1 (2021)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "142 S. Ct. 4; 211 L. Ed. 2d 164", "title": "Rivas-Villegas v. Cortesluna", "year": "2021"}}
{"assertion_id": "1e8312b0f4f1e541", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Rivas-Villegas v. Cortesluna"}}
{"assertion_id": "41a6c0c0f2fdcf1c", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "For QI, the plaintiff must identify a case that put the officer on notice that his specific conduct was unlawful, 'in light of the specific context of the case, not as a broad general proposition.'", "title": "Rivas-Villegas v. Cortesluna"}}
{"assertion_id": "702d01458152c328", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-10-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Rivas-Villegas v. Cortesluna", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Rivas-Villegas v. Cortesluna", "varies_by_point": "false"}}
{"assertion_id": "e18da25a72dae72a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rivas-Villegas v. Cortesluna"}}
```

### lake record — Rivas-Villegas v. Cortesluna

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rivas-Villegas v. Cortesluna",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rivas-Villegas v. Cortesluna",
    "case_name_short": "Rivas-Villegas",
    "case_name_full": "",
    "input_case_name": "Rivas-Villegas v. Cortesluna",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-10-18",
    "year": 2021,
    "docket": "20-1539",
    "cluster_id": 5290447,
    "lead_opinion_id": 5118993,
    "sibling_ids": [
      5118993
    ],
    "absolute_url": "/opinion/5290447/rivas-villegas-v-cortesluna/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "595 U.S. 1",
      "volume": "595",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 4",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "211 L. Ed. 2d 164",
        "volume": "211",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "595 U.S. 1",
        "volume": "595",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 4",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "4",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "211 L. Ed. 2d 164",
        "volume": "211",
        "reporter": "L. Ed. 2d",
        "page": "164",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "595 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "595 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op4",
      "page": null,
      "quote": "--- # Rivas-Villegas v. Cortesluna *595 U.S. 1 (2021)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers responded to a 911 call from a crying 12-year-old reporting that she, her mother, and her sister had locked themselves in a room because the mother's boyfriend, Cortesluna, was trying to hurt them and had a chainsaw. Officers ordered Cortesluna out and onto the ground and saw a knife in his left pocket. While removing the knife and handcuffing him, Officer Rivas-Villegas briefly placed his knee on the left side of Cortesluna's back for no more than eight seconds. Cortesluna sued under \u00a7 1983 for excessive force; the Ninth Circuit denied qualified immunity, relying on its precedent *LaLonde v. County of Riverside*. ## Issue Whether Rivas-Villegas was entitled to qualified immunity because he did not violate clearly established law. ## Rule Clearly established law must be particularized to the case. The",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op5",
      "page": null,
      "quote": "[T]o show a violation of clearly established law, Cortesluna must identify a case that put Rivas-Villegas on notice that his specific conduct was unlawful.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2021-10-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rivas-Villegas v. Cortesluna",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Pearlie Gambrel v. Knox Cnty., Ky.",
          "cluster_id": 6347889,
          "cite": [
            "25 F.4th 391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bretton Westmoreland v. Butler Cnty.",
          "cluster_id": 6454550,
          "cite": [
            "29 F.4th 721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melissa Knibbs v. Anthony Momphard, Jr.",
          "cluster_id": 6456228,
          "cite": [
            "30 F.4th 200"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Lawler v. Hardeman Cnty., Tenn.",
          "cluster_id": 9476181,
          "cite": [
            "93 F.4th 919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trellus Richmond v. Mario J. Badia",
          "cluster_id": 7858519,
          "cite": [
            "47 F.4th 1172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheri Trozzi v. Lake County, Ohio",
          "cluster_id": 6455758,
          "cite": [
            "29 F.4th 745"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Shumate v. City of Adrian, Mich.",
          "cluster_id": 7855599,
          "cite": [
            "44 F.4th 427"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William LaPlante v. City of Battle Creek, Mich.",
          "cluster_id": 6458100,
          "cite": [
            "30 F.4th 572"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherelle Thomas v. City of Harrisburg",
          "cluster_id": 9449712,
          "cite": [
            "88 F.4th 275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patricia Polanco v. Ralph Diaz",
          "cluster_id": 9418406,
          "cite": [
            "76 F.4th 918"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. John Yost",
          "cluster_id": 9385401,
          "cite": [
            "63 F.4th 211"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henderson v. Harris County",
          "cluster_id": 8248448,
          "cite": [
            "51 F.4th 125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Azucena Zamorano Aleman v. City of Charlotte",
          "cluster_id": 9421054,
          "cite": [
            "80 F.4th 264"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salazar v. Molina",
          "cluster_id": 6478362,
          "cite": [
            "37 F.4th 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
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
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "George v. Beaver County",
          "cluster_id": 6465265,
          "cite": [
            "32 F.4th 1246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Novak v. City of Parma, Ohio",
          "cluster_id": 6464344,
          "cite": [
            "33 F.4th 296"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crittindon v. LeBlanc",
          "cluster_id": 6476851,
          "cite": [
            "37 F.4th 177"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Jackson v. City of Cleveland",
          "cluster_id": 9389985,
          "cite": [
            "64 F.4th 736"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Timmy Mosier v. Joseph Evans",
          "cluster_id": 9458549,
          "cite": [
            "90 F.4th 541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
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
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniel Andrews v. City of Henderson",
          "cluster_id": 6470929,
          "cite": [
            "35 F.4th 710"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cameron Lewis v. Kevin Caraballo",
          "cluster_id": 9494123,
          "cite": [
            "98 F.4th 521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dejuan Hopson v. Jacob Alexander",
          "cluster_id": 9407196,
          "cite": [
            "71 F.4th 692"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rivas-Villegas v. Cortesluna:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(5118993) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 105,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 105,
        "triage_read": 0,
        "triage_snippet_classified": 105
      },
      "lane2_top_cited": {
        "query": "cites:(5118993)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMSZzPTU3OTM4ODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%285118993%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(5118993)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 0,
        "triage_snippet_classified": 77
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(5118993)",
    "indexed_citing_opinions": 126,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 5118993,
        "count": 126,
        "count_source": "search"
      }
    ],
    "citation_count": 489,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rivas-villegas-v-cortesluna.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTIyNzkmcz0xMDEyNDEwMSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%285118993%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 5118993,
        "cited_id": 4580945,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9429990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9431666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9492827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5118993,
        "cited_id": 9820073,
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
    "date_created": "2026-07-05T17:35:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:38:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:35:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rivas-Villegas v. Cortesluna

```
                  Cite as: 595 U. S. ____ (2021)             1

                           Per Curiam

SUPREME COURT OF THE UNITED STATES
 DANIEL RIVAS-VILLEGAS v. RAMON CORTESLUNA
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
             No. 20–1539. Decided October 18, 2021

    PER CURIAM.
    Petitioner Daniel Rivas-Villegas, a police officer in Union
City, California, responded to a 911 call reporting that a
woman and her two children were barricaded in a room for
fear that respondent Ramon Cortesluna, the woman’s boy-
friend, was going to hurt them. After confirming that the
family had no way of escaping the house, Rivas-Villegas
and the other officers present commanded Cortesluna out-
side and onto the ground. Officers saw a knife in Cor-
tesluna’s left pocket. While Rivas-Villegas and another of-
ficer were in the process of removing the knife and
handcuffing Cortesluna, Rivas-Villegas briefly placed his
knee on the left side of Cortesluna’s back. Cortesluna later
sued under Rev. Stat. §1979, 42 U. S. C. §1983, alleging, as
relevant, that Rivas-Villegas used excessive force. At issue
here is whether Rivas-Villegas is entitled to qualified im-
munity because he did not violate clearly established law.
    The undisputed facts are as follows. A 911 operator re-
ceived a call from a crying 12-year-old girl reporting that
she, her mother, and her 15-year-old sister had shut them-
selves into a room at their home because her mother’s boy-
friend, Cortesluna, was trying to hurt them and had a
chainsaw. The girl told the operator that Cortesluna was
“ ‘always drinking,’ ” had “ ‘anger issues,’ ” was “ ‘really
mad,’ ” and was using the chainsaw to “ ‘break something in
the house.’ ” Cortesluna v. Leon, 979 F. 3d 645, 649 (CA9
2020). A police dispatcher relayed this information along
with a description of Cortesluna in a request for officers to
respond.
2             RIVAS-VILLEGAS v. CORTESLUNA

                         Per Curiam

   Rivas-Villegas heard the broadcast and responded to the
scene along with four other officers. The officers spent sev-
eral minutes observing the home and reported seeing
through a window a man matching Cortesluna’s descrip-
tion. One officer asked whether the girl and her family
could exit the house. Dispatch responded that they “ ‘were
unable to get out’ ” and confirmed that the 911 operator had
“ ‘hear[d] sawing in the background’ ” and thought that Cor-
tesluna might be trying to saw down the door. Cortesluna
v. Leon, 2018 WL 6727824, *2 (ND Cal., Dec. 21, 2018).
   After receiving this information, Rivas-Villegas knocked
on the door and stated loudly, “ ‘police department, come to
the front door, Union City police, come to the front door.’ ”
Ibid. Another officer yelled, “ ‘he’s coming and has a
weapon.’ ” Ibid. A different officer then stated, “ ‘use less-
lethal,’ ” referring to a beanbag shotgun. Ibid. When Rivas-
Villegas ordered Cortesluna to “ ‘drop it,’ ” Cortesluna
dropped the “weapon,” later identified as a metal tool. Ibid.
   Rivas-Villegas then commanded, “ ‘come out, put your
hands up, walk out towards me.’ ” 979 F. 3d, at 650. Cor-
tesluna put his hands up and Rivas-Villegas told him to
“ ‘keep coming.’ ” Ibid. As Cortesluna walked out of the
house and toward the officers, Rivas-Villegas said, “ ‘Stop.
Get on your knees.’ ” Ibid. Plaintiff stopped 10 to 11 feet
from the officers. Another officer then saw a knife sticking
out from the front left pocket of Cortesluna’s pants and
shouted, “ ‘he has a knife in his left pocket, knife in his
pocket,’ ” and directed Cortesluna, “ ‘don’t put your hands
down,’ ” “ ‘hands up.’ ” 2018 WL 6727824, *2. Cortesluna
turned his head toward the instructing officer but then low-
ered his head and his hands in contravention of the officer’s
orders. Another officer twice shot Cortesluna with a bean-
bag round from his shotgun, once in the lower stomach and
once in the left hip.
   After the second shot, Cortesluna raised his hands over
his head. The officers shouted for him to “ ‘get down,’ ”
                  Cite as: 595 U. S. ____ (2021)            3

                           Per Curiam

which he did. Another officer stated, “ ‘left pocket, he’s got
a knife.’ ” Ibid. Rivas-Villegas then straddled Cortesluna.
He placed his right foot on the ground next to Cortesluna’s
right side with his right leg bent at the knee. He placed his
left knee on the left side of Cortesluna’s back, near where
Cortesluna had a knife in his pocket. He raised both of Cor-
tesluna’s arms up behind his back. Rivas-Villegas was in
this position for no more than eight seconds before standing
up while continuing to hold Cortesluna’s arms. At that
point, another officer, who had just removed the knife from
Cortesluna’s pocket and tossed it away, came and hand-
cuffed Cortesluna’s hands behind his back. Rivas-Villegas
lifted Cortesluna up and moved him away from the door.
   Cortesluna brought suit under 42 U. S. C. §1983, claim-
ing, as relevant here, that Rivas-Villegas used excessive
force in violation of the Fourth Amendment. The District
Court granted summary judgment to Rivas-Villegas, but
the Court of Appeals for the Ninth Circuit reversed. 979
F. 3d, at 656.
   The Court of Appeals held that “Rivas-Villegas is not en-
titled to qualified immunity because existing precedent put
him on notice that his conduct constituted excessive force.”
Id., at 654. In reaching this conclusion, the Court of Ap-
peals relied solely on LaLonde v. County of Riverside, 204
F. 3d 947 (CA9 2000). The court acknowledged that “the
officers here responded to a more volatile situation than did
the officers in LaLonde.” 979 F. 3d, at 654. Nevertheless,
it reasoned: “Both LaLonde and this case involve suspects
who were lying face-down on the ground and were not re-
sisting either physically or verbally, on whose back the de-
fendant officer leaned with a knee, causing allegedly signif-
icant injury.” Ibid.
   Judge Collins dissented. As relevant, he argued that “the
facts of LaLonde are materially distinguishable from this
case and are therefore insufficient to have made clear to
every reasonable officer that the force Rivas-Villegas used
4              RIVAS-VILLEGAS v. CORTESLUNA

                          Per Curiam

here was excessive.” Id., at 664 (internal quotation marks
omitted).
   We agree and therefore reverse. Even assuming that con-
trolling Circuit precedent clearly establishes law for pur-
poses of §1983, LaLonde did not give fair notice to Rivas-
Villegas. He is thus entitled to qualified immunity.
   “Qualified immunity attaches when an official’s conduct
does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.” White v. Pauly, 580 U. S. ___, ___ (2017) (per cu-
riam) (slip op., at 6) (internal quotation marks omitted). A
right is clearly established when it is “sufficiently clear that
every reasonable official would have understood that what
he is doing violates that right.” Mullenix v. Luna, 577 U. S.
7, 11 (2015) (per curiam) (internal quotation marks omit-
ted). Although “this Court’s case law does not require a case
directly on point for a right to be clearly established, exist-
ing precedent must have placed the statutory or constitu-
tional question beyond debate.” White, 580 U. S., at ___
(slip op., at 6) (alterations and internal quotation marks
omitted). This inquiry “must be undertaken in light of the
specific context of the case, not as a broad general proposi-
tion.” Brosseau v. Haugen, 543 U. S. 194, 198 (2004) (per
curiam) (internal quotation marks omitted).
   “[S]pecificity is especially important in the Fourth
Amendment context, where . . . it is sometimes difficult for
an officer to determine how the relevant legal doctrine, here
excessive force, will apply to the factual situation the officer
confronts.” Mullenix, 577 U. S., at 12 (alterations and in-
ternal quotation marks omitted). Whether an officer has
used excessive force depends on “the facts and circum-
stances of each particular case, including the severity of the
crime at issue, whether the suspect poses an immediate
threat to the safety of the officers or others, and whether he
is actively resisting arrest or attempting to evade arrest by
flight.” Graham v. Connor, 490 U. S. 386, 396 (1989); see
                  Cite as: 595 U. S. ____ (2021)            5

                           Per Curiam

also Tennessee v. Garner, 471 U. S. 1, 11 (1985) (“Where the
officer has probable cause to believe that the suspect poses
a threat of serious physical harm, either to the officer or to
others, it is not constitutionally unreasonable to prevent es-
cape by using deadly force”). However, Graham’s and Gar-
ner’s standards are cast “at a high level of generality.”
Brosseau, 543 U. S., at 199. “[I]n an obvious case, these
standards can ‘clearly establish’ the answer, even without
a body of relevant case law.” Ibid. But this is not an obvi-
ous case. Thus, to show a violation of clearly established
law, Cortesluna must identify a case that put Rivas-Ville-
gas on notice that his specific conduct was unlawful.
   Cortesluna has not done so. Neither Cortesluna nor the
Court of Appeals identified any Supreme Court case that
addresses facts like the ones at issue here. Instead, the
Court of Appeals relied solely on its precedent in LaLonde.
Even assuming that Circuit precedent can clearly establish
law for purposes of §1983, LaLonde is materially distin-
guishable and thus does not govern the facts of this case.
   In LaLonde, officers were responding to a neighbor’s com-
plaint that LaLonde had been making too much noise in his
apartment. 204 F. 3d, at 950–951. When they knocked on
LaLonde’s door, he “appeared in his underwear and a T-
shirt, holding a sandwich in his hand.” Id., at 951.
LaLonde testified that, after he refused to let the officers
enter his home, they did so anyway and informed him he
would be arrested for obstruction of justice. Ibid. One of-
ficer then knocked the sandwich from LaLonde’s hand and
“grabbed LaLonde by his ponytail and knocked him back-
wards to the ground.” Id., at 952. After a short scuffle, the
officer sprayed LaLonde in the face with pepper spray. At
that point, LaLonde ceased resisting and another officer,
while handcuffing LaLonde, “deliberately dug his knee into
LaLonde’s back with a force that caused him long-term if
not permanent back injury.” Id., at 952, 960, n. 17.
   The situation in LaLonde and the situation at issue here
6             RIVAS-VILLEGAS v. CORTESLUNA

                         Per Curiam

diverge in several respects. In LaLonde, officers were re-
sponding to a mere noise complaint, whereas here they
were responding to a serious alleged incident of domestic
violence possibly involving a chainsaw. In addition,
LaLonde was unarmed. Cortesluna, in contrast, had a
knife protruding from his left pocket for which he had just
previously appeared to reach. Further, in this case, video
evidence shows, and Cortesluna does not dispute, that Ri-
vas-Villegas placed his knee on Cortesluna for no more than
eight seconds and only on the side of his back near the knife
that officers were in the process of retrieving. LaLonde, in
contrast, testified that the officer deliberately dug his knee
into his back when he had no weapon and had made no
threat when approached by police. These facts, considered
together in the context of this particular arrest, materially
distinguish this case from LaLonde.
  “Precedent involving similar facts can help move a case
beyond the otherwise hazy borders between excessive and
acceptable force and thereby provide an officer notice that
a specific use of force is unlawful.” Kisela v. Hughes, 584
U. S. ___, ___ (2018) (per curiam) (slip op., at 5) (internal
quotation marks omitted). On the facts of this case, neither
LaLonde nor any decision of this Court is sufficiently simi-
lar. For that reason, we grant Rivas-Villegas’ petition for
certiorari and reverse the Ninth Circuit’s determination
that Rivas-Villegas is not entitled to qualified immunity.

                                             It is so ordered.

```

---

## GROUP: content/cases/Robinson v. Commonwealth.md  (`case`, 5 assertions)

### content_page

```
---
title: Robinson v. Commonwealth
type: case
citation: "No. 1912-24-1, slip op. (Virginia 2026)"
parallel_cite: ""
neutral_cite: ""
court: Va. Ct. App.
court_level: state
circuit: ""
year: 2026
date_decided: 2026-04-07
docket: 1912-24-1
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/"
  cluster_id: 10838748
  opinion_id: null
  identity_checked: false
lake:
  record_id: Robinson v. Commonwealth
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (ALPR network)"
related:
  - "[[Carpenter v. United States]]"
  - "[[United States v. Knotts]]"
  - "[[United States v. Jones]]"
tags:
  - case
  - fourth-amendment
  - digital-surveillance
  - automatic-license-plate-reader
  - flock
  - carpenter
  - third-party-doctrine
  - virginia-court-of-appeals
holding: "A police query of a network of fixed automatic license plate reader (Flock) cameras that photograph plates and vehicle exteriors on public roads and retain the data for 30 days is not a Fourth Amendment search on this record, because the system captures only a vehicle's public movements and does not create the kind of comprehensive chronicle of a person's life that Carpenter found to invade a reasonable expectation of privacy; the warrantless database query therefore required no warrant."
aliases:
  - Robinson v. Commonwealth
  - "Robinson v. Commonwealth (Va. Ct. App. 2026)"
  - Eddie Eugene Robinson v. Commonwealth
---

# Robinson v. Commonwealth

*No. 1912-24-1, slip op. (Virginia 2026)* · Court of Appeals of Virginia · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10838748 → published opinion 11306090 (Beales, J.; Record No. 1912-24-1, decided Apr. 7, 2026). Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (published Va. Ct. App. slip; no S.E.2d/Va. App. reporter cite assigned yet — S2 A3). S9 promotes. -->

## Background
The City of Norfolk operates 172 fixed Flock Safety cameras at intersections on public roads; they photograph passing vehicles and their plates, recording the plate number, color, make, model, and identifying features, and store the data for 30 days. After a string of predawn commercial burglaries, an investigator matched a stolen lottery ticket to surveillance footage of a white BMW SUV with distinctive black rims. Detective Gross queried the Flock database for that vehicle near the location and time, obtained one image showing the plate, ran the plate through DMV records, and identified Eddie Eugene Robinson. Robinson entered conditional guilty pleas after the circuit court denied his motion to suppress the Flock-derived evidence.

## Issue
Whether a police query of Norfolk's Flock automatic license plate reader system is a Fourth Amendment search requiring a warrant.

## Rule
A search occurs when the government invades a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]], and under *[[Carpenter v. United States]]* some digital dragnets — like long-term cell-site location tracking — do so by creating "a comprehensive chronicle" of a person's movements. But the court held this system different: "We decline to speculate as to when — or if — the Flock cameras could create such 'a comprehensive chronicle' of a person's movements where that person would then have a reasonable expectation of privacy. The search of the Flock database in this case was not an unreasonable search in violation of the Fourth Amendment." — slip op. at 9. ^pin-slip9

## Application
Distinguishing *[[Carpenter v. United States|Carpenter]]* and the Fourth Circuit's aerial-surveillance decision in *Leaders of a Beautiful Struggle*, the court reasoned that the Norfolk Flock system took discrete pictures of a vehicle's plate and exterior as it moved on public thoroughfares — where there is no [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in one's movements or license plate — and could not track a vehicle in real time. On the current record and this configuration, the system did not amass the pervasive, all-encompassing record that made cell-site tracking a search. The Fourth Amendment therefore imposed no warrant requirement on the database query.

## Conclusion
**Affirmed.** On this record the police were not required under the Fourth Amendment to obtain a search warrant to access the Flock system. Judge Beales wrote the published opinion.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Robinson* is a frontier state-court application of *[[Carpenter v. United States|Carpenter]]* to fixed ALPR networks, expressly fact-bound and explicitly declining to say whether a denser or longer-retained system might cross the line. It is persuasive, illustrative authority on the third-party-doctrine/digital-surveillance frontier, not binding federal precedent, and the "comprehensive chronicle" question it reserves remains open.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (ALPR network)*

## Sources
- [*Eddie Eugene Robinson v. Commonwealth of Virginia*, No. 1912-24-1, slip op. (Va. Ct. App. 2026)](https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/) — pinpoint: slip op. at 9 (Flock ALPR query not a Fourth Amendment search on this record). Rule quote string-matched to the CL opinion text 2026-07-07. Published Va. Ct. App. slip; no S.E.2d/Va. App. reporter cite assigned yet (S2 A3 slip precedent).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "300afa3f803dc101", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "No. 1912-24-1, slip op. (Virginia 2026)", "court": "Va. Ct. App.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Robinson v. Commonwealth", "year": "2026"}}
{"assertion_id": "fa400fdbe228c726", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Lower-court development (ALPR network)", "title": "Robinson v. Commonwealth"}}
{"assertion_id": "faf7c5390d8fc920", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A police query of a network of fixed automatic license plate reader (Flock) cameras that photograph plates and vehicle exteriors on public roads and retain the data for 30 days is not a Fourth Amendment search on this record, because the system captures only a vehicle's public movements and does not create the kind of comprehensive chronicle of a person's life that Carpenter found to invade a reasonable expectation of privacy; the warrantless database query therefore required no warrant.", "title": "Robinson v. Commonwealth"}}
{"assertion_id": "456a7657c7878f4c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "Robinson v. Commonwealth"}}
{"assertion_id": "8da96345d903b349", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Robinson v. Commonwealth", "varies_by_point": "false"}}
```

### lake record — Robinson v. Commonwealth

```json
{
  "schema_version": "s2.v1",
  "record_id": "Robinson v. Commonwealth",
  "status": "under_review",
  "identity": {
    "case_name": "Eddie Eugene Robinson v. Commonwealth of Virginia",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "Robinson v. Commonwealth",
    "court": "Va. Ct. App.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Virginia",
    "date_decided": "2026-04-07",
    "year": 2026,
    "docket": "1912-24-1",
    "cluster_id": 10838748,
    "lead_opinion_id": 11306090,
    "sibling_ids": [],
    "absolute_url": "/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/",
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
      "court_class": "state",
      "selected": null,
      "reason": "no_official_class_citation"
    },
    "slip_only": true,
    "slip_only_provenance": {
      "source": "R8-R3-web-cites.jsonl",
      "as_of": "2026-07-07",
      "by": "s6-slip-stamp",
      "note": "W9 RE-STAMP after pre-W5 re-key (prior stamp was on superseded cluster 10793178). Eddie Eugene Robinson v. Commonwealth of Virginia, Va. Ct. App. PUBLISHED slip, Record No. 1912-24-1, decided 2026-04-07 (Flock ALPR digital surveillance). CL cluster 10838748 Published, citations[] empty (live-verified 2026-07-07); no S.E.2d/Va. App. reporter cite assigned yet.",
      "legs": [
        {
          "source": "Court PDF",
          "url": "https://www.vacourts.gov/static/opinions/opncavwp/1912241.pdf",
          "cite": "Record No. 1912-24-1, published 2026-04-07"
        },
        {
          "source": "CourtListener",
          "url": "https://www.courtlistener.com/opinion/10838748/eddie-eugene-robinson-v-commonwealth-of-virginia/",
          "cite": "cluster 10838748 Published, citations[] empty"
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
    "date_created": "2026-07-07T18:26:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:26:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "robinson-v-commonwealth--10838748",
      "to_record_id": "Robinson v. Commonwealth",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Robinson v. Commonwealth

```
                         COURT OF APPEALS OF VIRGINIA

                                      Record No. 1912-24-1


                                EDDIE EUGENE ROBINSON
                                          v.
                              COMMONWEALTH OF VIRGINIA


Present: Judges Beales, Malveaux and Frucci
Argued at Norfolk, Virginia
                                                                      Opinion Issued April 7, 2026


                FROM THE CIRCUIT COURT OF THE CITY OF NORFOLK
                             Jamilah D. LeCruise, Judge1

J. Barry McCracken, Assistant Public Defender, for appellant.

Israel-David J.J. Healy, Assistant Attorney General (Jason S. Miyares,2 Attorney General, on
brief), for appellee.


                                 PUBLISHED OPINION BY
                               JUDGE RANDOLPH A. BEALES

       Eddie Eugene Robinson entered conditional guilty pleas to three felony charges of

statutory burglary in violation of Code § 18.2-91, one felony charge of larceny of lottery tickets

in violation of Code § 58.1-4018.1(A), one charge of grand larceny in violation of Code

§ 18.2-95(ii), and one charge of being a nonviolent felon in possession of a firearm in violation

of Code § 18.2-308.2(A). On appeal, Robinson contends that the circuit court erred in denying

his motion to suppress evidence from automatic license plate reader cameras made by Flock




       1
         Judge David W. Lannetti denied Robinson’s motion to suppress, which is the issue
before the Court in this appeal.
       2
           Jay C. Jones succeeded Jason S. Miyares as Attorney General on January 17, 2026.
Safety (“Flock cameras”), arguing that the evidence was obtained in violation of the Fourth

Amendment.

                                       I. BACKGROUND3

       In 2023, the City of Norfolk installed a system of 172 cameras at intersections on public

roadways throughout Norfolk. They capture still images of cars and their license plates and store

the information—the license plate number, the color, manufacturer, and model of the car, as well

as any identifying characteristics such as roof racks or bumper stickers—on servers for 30 days.

Norfolk Police detectives have access to the database, and they can use it to search for particular

vehicles in particular places. Police can narrow their search of the Flock database by location or

timeframe but generally cannot track a vehicle in real time.

       Over the course of three weeks in November 2023, several commercial storefronts in

Norfolk were broken into and a number of items stolen, all in the early hours of the morning.

The first of these occurred on November 5, 2023, at around 3:50 a.m., when someone broke into

Nu Beauty Supply. The owner reported that money and merchandise had been stolen.

Surveillance footage of the burglary showed that the perpetrator was wearing a hoodie, a head

covering, a medical mask, and duck boots.

       On November 12, 2023, at around 3:00 a.m., someone broke into George’s Seafood. The

owner reported that money and an iPad had been stolen. Surveillance footage of the burglary

showed that the perpetrator was wearing a hoodie, a backpack, a face mask, and duck boots.

       On November 29, 2023, at around 4:00 a.m., someone broke into Quick Serve. The

owner reported that money and lottery tickets had been stolen. Surveillance footage of the

burglary showed a black male wearing a hoodie, a backpack, and duck boots.


       3
         “In reviewing the denial of a motion to suppress, we ‘consider the facts in the light most
favorable to the Commonwealth, the prevailing party at trial.’” Aponte v. Commonwealth, 68
Va. App. 146, 156 (2017) (quoting Hairston v. Commonwealth, 67 Va. App. 552, 560 (2017)).
                                               -2-
       Adam Hankins, an investigator at Virginia Lottery, entered the numbers of the stolen

lottery tickets into a database that alerts investigators if someone attempts to cash them in. At

9:15 a.m. on November 29, 2023, the same day that Quick Serve was broken into, the database

notified Investigator Hankins that someone had attempted to cash in one of the stolen tickets at

Miller’s Store, a gas station in Norfolk. Investigator Hankins accessed the surveillance footage

from Miller’s and, believing the person depicted at Miller’s to match the description of the

person who broke into Quick Serve, shared still photographs from the footage with the Norfolk

Police Department. One of the photographs showed a white BMW SUV with black rims but did

not show the car’s license plate.

       Knowing that there were two Flock cameras near Miller’s, Norfolk Police Detective

Kevin Gross entered the make and model of the vehicle into the Flock system, limiting his search

to the two hours surrounding the burglary. The Flock system returned one image of a white

BMW with black rims, and its license plate.4 Detective Gross then looked up the license plate

number in a Virginia Department of Motor Vehicles database, which revealed Robinson as the

car’s registered owner. The DMV search also yielded a photo of Robinson, whom Detective

Gross determined to be the same person depicted in the footage of the burglary at Quick Serve.

       Detective Gross obtained an arrest warrant for Robinson, and Robinson was arrested on

December 4, 2023. Detective Gross also obtained a search warrant for Robinson’s home, in

which officers found lottery tickets stolen from Quick Serve, checks made out to George’s

Seafood, and beauty products sold by Nu Beauty Supply. Officers also found a firearm in




       4
          Detective Gross could not recall how many white BMW SUVs the Flock system
returned but was able to identify Robinson’s vehicle because of its “distinctive black rims.” He
testified, “Not many pictures that I [had] seen while looking at that data had black rims.”
                                                -3-
Robinson’s home. Robinson was charged with felony burglary, grand larceny, and larceny of

lottery tickets.5

        Robinson moved to suppress, arguing that the warrantless search of the Flock database

violated the Fourth Amendment and that the evidence obtained as a result of the Flock search—

the stolen property and weapon found in his home—should be suppressed. After a hearing, the

circuit court denied Robinson’s motion to suppress.

        Robinson entered conditional guilty pleas to three felony charges of statutory burglary,

one felony charge of larceny of lottery tickets, one charge of grand larceny, and one charge of

being a nonviolent felon in possession of a firearm. Robinson now appeals to this Court.

                                          II. ANALYSIS

        Robinson argues,

                        The trial court erred in denying the Appellant’s motion to
                suppress the warrantless obtaining of location and movement data
                of the Appellant’s vehicle by police from the collection and storage
                of license plate and location information by means of the Flock
                System which constituted a search within the meaning of the
                Fourth Amendment requiring a warrant.

                                      A. Standard of Review

        “The law regarding appellate review of a trial court’s decision on a motion to suppress is

well settled. The appellant bears the burden of establishing that reversible error occurred.”

Williams v. Commonwealth, 71 Va. App. 462, 474 (2020) (quoting Glenn v. Commonwealth, 275

Va. 123, 130 (2008)). “A defendant’s claim that evidence was seized in violation of the Fourth

Amendment presents a mixed question of law and fact.” Jones v. Commonwealth, 277 Va. 171,



        5
         Robinson was indicted for several other commercial burglaries: T&T Seafood Market,
Cajun Seafood, Golden City Chinese Food, Mina Seafood, and Latiendita Costa Del Mar. The
Commonwealth later nolle prossed several of these charges in exchange for Robinson’s
conditional guilty plea. Robinson stipulated to the burglaries of Nu Beauty Supply, George’s
Seafood, and Quick Serve.
                                               -4-
177 (2009) (quoting McCain v. Commonwealth, 275 Va. 546, 551-52 (2008)). “We are bound

by the trial court’s factual findings unless those findings are plainly wrong or unsupported by the

evidence.” Whitaker v. Commonwealth, 279 Va. 268, 273-74 (2010) (quoting Whitehead v.

Commonwealth, 278 Va. 300, 306-07 (2009)). This “Court reviews de novo the overarching

question of whether a search or seizure violated the Fourth Amendment.” Williams, 71 Va. App.

at 475 (citing Glenn, 275 Va. at 130). “Whether a particular governmental intrusion is

reasonable within the meaning of the Fourth Amendment depends upon the particular facts and

circumstances of the case.” Bennett v. Commonwealth, 212 Va. 863, 865 (1972) (citing Cabbler

v. Commonwealth, 212 Va. 520, 522 (1971)).

                        B. The Flock System and the Fourth Amendment

       The Fourth Amendment provides that the “right of the people to be secure in their

persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be

violated.” U.S. CONST. amend. IV. The “basic purpose of this Amendment . . . is to safeguard

the privacy and security of individuals against arbitrary invasions by governmental officials.”

Camara v. Municipal Court of City and County of San Francisco, 387 U.S. 523, 528 (1967).

Therefore, a search without a warrant is “presumptively unreasonable.” Bryant v.

Commonwealth, 72 Va. App. 179, 187-88 (2020) (quoting Glenn, 275 Va. at 130).

       “Since Katz v. United States, the touchstone of [Fourth] Amendment analysis has been

the question whether a person has a ‘constitutionally protected reasonable expectation of

privacy.’” Rideout v. Commonwealth, 62 Va. App. 779, 786 (2014) (alteration in original)

(citation omitted) (quoting Oliver v. United States, 466 U.S. 170, 177 (1984)). In other words, a

search violates the Fourth Amendment if it invades a person’s reasonable expectation of privacy.

       New technology often “does not fit neatly under existing precedents.” Carpenter v.

United States, 585 U.S. 296, 306 (2018). “[A]s technology continues to enhance the

                                               -5-
‘Government’s ability to encroach upon areas normally guarded from inquisitive eyes,’ courts

must assure that individuals maintain the ‘degree of privacy against government that existed

when the Fourth Amendment was adopted.’” United States v. Martin, 753 F. Supp. 3d 454, 462

(E.D. Va. 2024) (quoting Carpenter, 585 U.S. at 305). See also Kyllo v. United States, 533 U.S.

27, 34 (2001).

       In Knotts, police installed a beeper in a container of chloroform that allowed them to

track the container’s location as it was driven on public highways. United States v. Knotts, 460

U.S. 276, 278-79 (1983). The United States Supreme Court held that the warrantless use of the

beeper was constitutional because “[n]othing in the Fourth Amendment prohibited the police

from augmenting the sensory faculties bestowed upon them at birth with such enhancement as

science and technology afforded them in this case.” Id. at 282 (citing United States v. Lee, 274

U.S. 559, 563 (1927)).

       In Carpenter, the United States Supreme Court held that accessing a person’s cell-site

location information (“CSLI”) required a search warrant because CSLI “provides an all-

encompassing record of the holder’s whereabouts.” 585 U.S. at 311. In that case, the CSLI

captured 127 days of Carpenter’s movements, with an average of 101 data points per day. Id. at

302. The United States Supreme Court stated that CSLI “provides an intimate window into a

person’s life, revealing not only his particular movements, but through them his ‘familial,

political, professional, religious, and sexual associations’” because “[a] cell phone faithfully

follows its owner beyond public thoroughfares and into private residences, doctor’s offices,

political headquarters, and other potentially revealing locales.” Id. at 310-11 (quoting United

States v. Jones, 565 U.S. 400, 415 (2012)). “Accordingly, when the Government tracks the

location of a cell phone it achieves near perfect surveillance, as if it had attached an ankle

monitor to the phone’s user.” Id. at 311-12. The Court held that using CSLI to create and

                                                -6-
maintain a comprehensive chronicle of a person’s movements for a period of over 100 days

invaded that person’s reasonable expectation of privacy. Id. at 311, 313. Thus, the Supreme

Court held, accessing the data was a search within the meaning of the Fourth Amendment and

required a search warrant. Id. at 316.

       Finally, in Leaders of a Beautiful Struggle, the United States Court of Appeals for the

Fourth Circuit, sitting en banc, held that an aerial surveillance program that tracked the

movements of people and vehicles in Baltimore violated the Fourth Amendment because its

extensive tracking of city residents revealed “intimate details through habits and patterns.”

Leaders of a Beautiful Struggle v. Baltimore Police Department, 2 F.4th 330, 341 (4th Cir. 2021)

(en banc). The cameras were operated from the air twelve hours a day—only during daylight—

and covered ninety percent of the city. Id. at 334. The data was retained for 45 days. Id. The

court applied Carpenter in holding that a search warrant was required to access the system. Id.

at 341-42.

       These precedents guide our review. As our Supreme Court has instructed, “Whether a

particular governmental intrusion is reasonable within the meaning of the Fourth Amendment

depends upon the particular facts and circumstances of the case.” Bennett, 212 Va. at 865 (citing

Cabbler, 212 Va. at 522). We find that the use of the Flock system in this case is similar to

Knotts, but significantly factually distinguishable from both Carpenter and Leaders of a

Beautiful Struggle.

       As a threshold matter, Robinson had no reasonable expectation of privacy in the physical

characteristics of his vehicle as he drove it down a public street. In the case now before us, as in

Knotts, the use of the Flock cameras did not constitute a search because “the movements of the

vehicle . . . had been ‘voluntarily conveyed to anyone who wanted to look.’” Carpenter, 585

U.S. at 306 (quoting Knotts, 460 U.S. at 281). Indeed, as this Court has recently stated, “A

                                                -7-
person driving his vehicle on a public street with his license plate in plain view has no reasonable

expectation of privacy that his vehicle and license plate will not be seen by other persons,

including law enforcement officers.” Commonwealth v. Church, No. 0737-25-1, slip op. at 4,

2025 Va. App. LEXIS 627, at *5 (Oct. 14, 2025) (citing Knotts, 460 U.S. at 281).

       Moreover, it simply cannot be said that the City of Norfolk’s system of Flock cameras

amounted to “near perfect surveillance.” Carpenter, 585 U.S. at 312. The 172 Flock cameras

situated throughout Norfolk are not as intrusive as the cell towers in Carpenter that monitor the

movement of cell phones both inside and outside of homes and buildings—or the surveillance of

a city from the air in Leaders of a Beautiful Struggle. The images captured by the Flock cameras

are of vehicles, not persons, and the only pieces of information collected—license plates and

physical characteristics of the vehicle—are already publicly viewable to anyone who sees the

vehicle on the street. The search of the Flock system yielded a photo of Robinson’s car as it

passed down a public highway. The cameras did not continuously monitor all of his travels

around the city and did not create an “intimate window” of Robinson’s overall movements and

associations. See, e.g., Schmidt v. City of Norfolk, ___ F. Supp. 3d ___, ___ (E.D. Va. 2026)

(noting that the Flock cameras appear intermittently “across the many miles of Norfolk roadways

such that they are incapable of cataloging the whole of vehicles’ movements”). Unlike in

Carpenter and Leaders of a Beautiful Struggle, the Flock system takes only still images of a

vehicle’s exterior as it passes down public thoroughfares—not of the person. It is not “a detailed

chronicle of a person’s physical presence compiled every day, every moment, over several

years.” Carpenter, 585 U.S. at 315.

       Thus, Detective Gross did not have to obtain a search warrant to access the Flock system

because he was merely requesting information that showed still images of a vehicle in which

Robinson did not have a reasonable expectation of privacy. In addition, the Flock cameras did

                                               -8-
not augment police officers’ sensory faculties to an impermissible degree. The cameras

interspersed along public roads throughout the City of Norfolk are hardly analogous to the 127

days of cell-site location information at issue in Carpenter, and the images are only stored on

servers for 30 days. The scope and scale of the information captured by the Flock cameras are

also not analogous to the aerial surveillance of every movement of virtually every resident of

Baltimore for twelve hours a day that the Fourth Circuit considered in Leaders of a Beautiful

Struggle. For all of these reasons, we therefore hold that the use of the Flock system in this case

did not constitute a search that violated the Fourth Amendment.

       We are also persuaded by recent federal cases that have already addressed the Flock

systems in Richmond and Norfolk. See United States v. Martin, 753 F. Supp. 3d 454 (E.D. Va.

2024) (Richmond); Schmidt, ___ F. Supp. 3d at ___ (Norfolk). While not binding on this Court,

we find these federal district court decisions instructive as they concern the same system of

cameras as in the case now before this Court. In Martin, the United States District Court for the

Eastern District of Virginia held that police officers in Richmond and Chesterfield County did

not violate any reasonable expectation of privacy by using information obtained from the Flock

system in their investigation of the defendant, Martin. 753 F. Supp. 3d at 476. In that case, out

of 2,500 photographs taken of vehicles in a 30-day period, only three were of the defendant’s

vehicle. Id. at 472. In Schmidt, the court held that the City of Norfolk’s system of Flock

cameras—the very same system at issue in the case now before this Court—did not violate the

plaintiffs’ Fourth Amendment rights and awarded summary judgment to the City of Norfolk.6

___ F. Supp. 3d at ___. Both Martin and Schmidt distinguished Carpenter and Leaders of a




       6
       In Schmidt, the plaintiffs brought suit under 42 U.S.C. § 1983 and the Declaratory
Judgment Act.
                                               -9-
Beautiful Struggle, finding that those cases involved much more invasive searches. Martin, 753

F. Supp. 3d at 471-73; Schmidt, ___ F. Supp. 3d at ___.

       The Virginia Supreme Court has stated that an assessment of whether a new technology

runs afoul of the Fourth Amendment is a fact-based inquiry. See Bennett, 212 Va. at 865. See

also Martin, 753 F. Supp. 3d at 476 (“This Court must rule on the facts as they are and may not

speculate about what the future may hold for Flock’s capabilities.”). We must decide each case

on its facts and therefore our decision is based on the current system of Flock cameras in the City

of Norfolk. We decline to speculate as to when—or if—the Flock cameras could create such “a

comprehensive chronicle” of a person’s movements where that person would then have a

reasonable expectation of privacy. Carpenter, 585 U.S. at 300. The search of the Flock database

in this case was not an unreasonable search in violation of the Fourth Amendment.

                                       III. CONCLUSION

       In short, because the Flock system simply took pictures of the license plate of Robinson’s

vehicle and the exterior of his vehicle as he drove it down public thoroughfares in the City of

Norfolk, the police were not required under the Fourth Amendment to obtain a search warrant in

order to access the Flock system. Consequently, for all of the foregoing reasons, we affirm the

judgment of the circuit court.

                                                                                         Affirmed.




                                               - 10 -

```

---

## GROUP: content/cases/State v. Mitcham.md  (`case`, 5 assertions)

### content_page

```
---
title: "State v. Mitcham"
type: case
citation: "559 P.3d 1099 (2024)"
parallel_cite: ""
neutral_cite: ""
court: Arizona Supreme Court
court_level: state
circuit: ""
year: 2024
date_decided: 2024-12-17
docket: CR-23-0238-PR
authority_weight: "Persuasive — state, illustrative"
treatment:
  field_i_validity: good_law
  as_of_content: 2024-12-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: State v. Mitcham
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/10293607/state-of-arizona-v-ian-mitcham/"
  cluster_id: 10293607
  opinion_id: 10760195
  identity_checked: false
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Recent development (role-based)"
related: ["[[Nix v. Williams]]", "[[Murray v. United States]]", "[[Segura v. United States]]", "[[Herring v. United States]]", "[[Utah v. Strieff]]"]
aliases: ["State of Arizona v. Ian Mitcham"]
tags: ["case", "exclusionary-rule", "inevitable-discovery", "independent-source", "dna", "arizona"]
holding: "Arizona Supreme Court applies the independent-source exception: evidence discovered during/because of an unlawful search is admissible…"
lake:
  record_id: State v. Mitcham
  status: under_review
  projected_at: 2026-07-06
---

# State v. Mitcham

*258 Ariz. 435, 559 P.3d 1099 (2024)* · Arizona Supreme Court · **Persuasive — state, illustrative** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a 2015 cold-case murder (victim Allison Feldman), police obtained Mitcham's DNA through an unlawful warrantless search of a second vial of blood drawn after a 2015 DUI arrest; the DNA matched, and Mitcham moved to suppress. Separately, Mitcham had been convicted in 2022 of unrelated felonies (narcotics and aggravated DUI), which by statute required collection of his DNA upon imprisonment.

## Issue
Whether DNA evidence obtained through an unlawful search must be suppressed, or whether an exception to the exclusionary rule permits its use.

## Rule
The Court distinguished and applied the exclusionary-rule exceptions. "The 'independent source' exception permits the admission of evidence discovered during or because of an unlawful search if the evidence was also obtained independently from activities that were tainted by the illegality." — 258 Ariz. 435, ¶ 34 (2024). ^pin-34

The two exceptions differ in that the distinction "rests on whether the evidence was discovered through an independent, untainted source ..., or whether the evidence would have been discovered through an independent, untainted source despite the illegal search ...." — *Id.* ¶ 36. ^pin-36

Applying [[Inevitable Discovery and Independent Source|inevitable discovery]], the Court held the State "would have inevitably obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search of the second vial of blood ...." — *Id.* ¶ 37. ^pin-37

## Application
Mitcham's unrelated 2022 felony convictions and prison sentence triggered Arizona's statutory requirement (A.R.S. § 13-610) that the Department of Corrections collect his DNA for profiling. That lawful, untainted process would inevitably have produced the same DNA profile independent of the illegal 2018 search; the only reason it did not was that police already held a sample from the illegal search. Suppression would put the prosecution in a worse position than if the violation had never occurred, so the inevitable-discovery exception applied.

## Conclusion
The DNA evidence was admissible under the inevitable-discovery exception; suppression was denied.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Persuasive — state, illustrative**.
- Applies the inevitable-discovery exception of [[Nix v. Williams]] and its independent-source roots ([[Murray v. United States]], [[Segura v. United States]]) within the deterrence-focused exclusionary framework of [[Herring v. United States]] and [[Utah v. Strieff]].

## Appears on
- [[The Exclusionary Rule]] — *Recent development (role-based)*

## Sources
- *State v. Mitcham*, 258 Ariz. 435, 559 P.3d 1099 (Ariz. 2024) — https://www.courtlistener.com/opinion/10293607/state-of-arizona-v-ian-mitcham/ (lead opinion id 10760195) — pinpoints: ¶¶ 34, 36, 37.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6d9776dbf1b55cdc", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "559 P.3d 1099 (2024)", "court": "Arizona Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "State v. Mitcham", "year": "2024"}}
{"assertion_id": "a44969083794ad62", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Recent development (role-based)", "title": "State v. Mitcham"}}
{"assertion_id": "f4a9cbdac825c2b4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Arizona Supreme Court applies the independent-source exception: evidence discovered during/because of an unlawful search is admissible…", "title": "State v. Mitcham"}}
{"assertion_id": "6001c8e90b1c39b4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "State v. Mitcham"}}
{"assertion_id": "d19e31ec17d449ac", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2024-12-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "State v. Mitcham", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "State v. Mitcham", "varies_by_point": "false"}}
```

### lake record — State v. Mitcham

```json
{
  "schema_version": "s2.v1",
  "record_id": "State v. Mitcham",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "State of Arizona v. Ian Mitcham",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "State v. Mitcham",
    "court": "Arizona Supreme Court",
    "court_id": "ariz",
    "court_level": "state",
    "circuit": null,
    "state": null,
    "date_decided": "2024-12-17",
    "year": 2024,
    "docket": "CR-23-0238-PR",
    "cluster_id": 10293607,
    "lead_opinion_id": 10760195,
    "sibling_ids": [
      10760195
    ],
    "absolute_url": "/opinion/10293607/state-of-arizona-v-ian-mitcham/",
    "identity_method": "name+docket",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "559 P.3d 1099",
      "volume": "559",
      "reporter": "P.3d",
      "page": "1099",
      "type": 3,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "559 P.3d 1099",
        "volume": "559",
        "reporter": "P.3d",
        "page": "1099",
        "type": 3,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "559 P.3d 1099",
    "official_selection": {
      "court_class": "state",
      "selected": "559 P.3d 1099",
      "reason": "selected_rank_2"
    }
  },
  "pinpoints": [
    {
      "id": "pin-34",
      "page": null,
      "quote": "--- # State v. Mitcham *258 Ariz. 435, 559 P.3d 1099 (2024)* \u00b7 Arizona Supreme Court \u00b7 **Persuasive \u2014 state, illustrative** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a 2015 cold-case murder (victim Allison Feldman), police obtained Mitcham's DNA through an unlawful warrantless search of a second vial of blood drawn after a 2015 DUI arrest; the DNA matched, and Mitcham moved to suppress. Separately, Mitcham had been convicted in 2022 of unrelated felonies (narcotics and aggravated DUI), which by statute required collection of his DNA upon imprisonment. ## Issue Whether DNA evidence obtained through an unlawful search must be suppressed, or whether an exception to the exclusionary rule permits its use. ## Rule The Court distinguished and applied the exclusionary-rule exceptions.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-36",
      "page": null,
      "quote": "rests on whether the evidence was discovered through an independent, untainted source ..., or whether the evidence would have been discovered through an independent, untainted source despite the illegal search ....",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-37",
      "page": null,
      "quote": "would have inevitably obtained Mitcham's DNA profile from an independent, untainted source despite the warrantless search of the second vial of blood ....",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2024-12-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "State v. Mitcham",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(10760195) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ariz OR arizctapp)",
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
        "query": "cites:(10760195)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(10760195)",
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
    "complete_query": "cites:(10760195)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 10760195,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/state-v-mitcham.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 10760195,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 450747,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 700649,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 755893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 867200,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 867501,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 873669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1135969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1179100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1206372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1297298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 1393415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 2582173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 2813060,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3214776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3216391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 3418437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4028107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4171004,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4206137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4287285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4583624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 4650433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 5666093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6104581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6105914,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 6480131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 7263677,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 7268856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9422064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9422515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9423552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9427563,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9427638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9428007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9429647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9429757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9431434,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9431606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9432279,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9433685,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9434934,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9457073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9476246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9514985,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9571325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9628491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9637378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9812443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9822918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 10760195,
        "cited_id": 9888052,
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
    "date_created": "2026-07-05T20:31:00Z",
    "date_modified": "2026-07-06T08:52:25Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:32:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:31:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — State v. Mitcham

```
                               IN THE

    SUPREME COURT OF THE STATE OF ARIZONA

                          STATE OF ARIZONA,
                              Appellant,

                                  v.

                            IAN MITCHAM,
                               Appellee.




                         No. CR-23-0236-PR
                       Filed December 17, 2024


          Appeal from the Superior Court in Maricopa County
              The Honorable Roy C. Whitehead, Judge
                       No. CR2018-118086-001

                   REVERSED AND REMANDED


                   Opinion of the Court of Appeals,
                            Division One
                      256 Ariz. 104 (App. 2023)

                             VACATED



COUNSEL:

Rachel H. Mitchell, Maricopa County Attorney, Nick Klingerman (argued),
Special Deputy County Attorney, Ryan Green, Deputy County Attorney,
Maricopa County Attorney’s Office, Phoenix, Attorneys for State of
Arizona

Gary Kula, Maricopa County Public Defender, Mikel Steinfeld (argued),
Martha Barco Penunuri, Jeffrey A. Kirchler, Richard D. Randall, Deputy
                            STATE V. MITCHAM
                           Opinion of the Court

Public Defenders, Phoenix, Attorneys for Ian Mitcham

David J. Euchner (argued), Pima County Public Defender’s Office, Grant D.
Wille, Ralls, Wille, & Coomer, P.C., Tucson, Attorneys for Amicus Curiae
Arizona Attorneys for Criminal Justice

Kristin K. Mayes, Arizona Attorney General, Alice M. Jones, Deputy
Solicitor General/Section Chief of Criminal Appeals, Michael O’Toole,
Assistant Attorney General, Phoenix, Attorneys for Amicus Curiae Arizona
Attorney General

Jared G. Keenan, Lauren K. Beall, American Civil Liberties Union
Foundation of Arizona; Vera Eidelman, American Civil Liberties Union
Foundation, New York, NY, Attorneys for Amici Curiae American Civil
Liberties Union of Arizona and American Civil Liberties Union



CHIEF JUSTICE TIMMER authored the Opinion of the Court, in which
VICE CHIEF JUSTICE LOPEZ, JUSTICES BOLICK, BEENE, KING,
BRUTINEL (RETIRED), and JUDGE SKLAR joined. *




CHIEF JUSTICE TIMMER, Opinion of the Court:

¶1           After police arrested Ian Mitcham for driving under the
influence of alcohol (“DUI”), he consented to a blood test to determine
alcohol concentration or drug content. Years later, police suspected
Mitcham of committing a murder, and they still had Mitcham’s blood from
the DUI arrest. Without obtaining a warrant, they extracted a DNA profile
from that blood, which linked Mitcham to the murder.




*  Justice Brutinel retired after oral argument in this case but nevertheless
participated in deciding this opinion. Justice Montgomery is recused from
this matter. Pursuant to article 6, section 3 of the Arizona Constitution,
Judge Jeffrey Sklar of the Arizona Court of Appeals, Division Two, was
designated to sit in this matter.

                                     2
                             STATE V. MITCHAM
                            Opinion of the Court

¶2            We decide that the police violated Mitcham’s Fourth
Amendment rights by conducting the warrantless search. Because the
inevitable discovery exception to the exclusionary rule applies, however,
we hold that the trial court erred by suppressing the DNA evidence.

                             BACKGROUND

¶3            In January 2015, Scottsdale Police arrested Mitcham for DUI.
A police officer advised Mitcham that Arizona law required him to submit
to a blood test to determine alcohol concentration or drug content. The
officer explained that if Mitcham refused to consent to testing, the state
would suspend his driver’s license for twelve months.            Mitcham
consented.

¶4             The police drew two vials of blood from Mitcham and used
one vial for their test. They made the second vial available to Mitcham to
allow him to independently test his blood.             Mitcham signed a
“Destruction Notice,” acknowledging that police would destroy the second
vial if he did not ask for it within ninety days. Mitcham never asked for
the second vial, but the police did not destroy it. Mitcham was ultimately
convicted of a misdemeanor DUI.

¶5            Tragically, one month after Mitcham’s DUI arrest, Allison
Feldman was found murdered in her Scottsdale home. The police
collected biological swabs from the scene, developed a male DNA profile,
and uploaded it into the National DNA Index System (“NDIS”) using the
Combined DNA Index System (“CODIS”).                See A.R.S. § 41-2418(A)
(establishing Arizona’s DNA identification system). CODIS is a software
program maintained by the Federal Bureau of Investigation that “link[s]
DNA profiles culled from federal, state, and territorial DNA collection
programs,” United States v. Kriesel, 508 F.3d 941, 944 (9th Cir. 2007), and
searches the NDIS database of DNA profiles taken from convicted
offenders, among others.        See 34 U.S.C. § 12592(a) (authorizing the
establishment of a national DNA index); see also Lockett v. Wray, 271 F. Supp.
3d 205, 209 (D.D.C. 2017) (relating expert descriptions of NDIS and CODIS).
CODIS did not return a match, and Feldman’s murder remained unsolved
for several years.

¶6           In 2017, police initiated a “familial DNA” investigation on the
unknown-male DNA profile by asking the Arizona Department of Public
Safety (“DPS”) to search Arizona’s DNA identification system to determine

                                      3
                            STATE V. MITCHAM
                           Opinion of the Court

whether anyone incarcerated by the state is related to that unknown male.
See § 41-2418(A). Through this investigation, DPS identified Mitcham’s
incarcerated brother as closely related—most likely through a parent-child
or sibling relationship—to the man whose DNA was collected at the
murder scene. The police then discovered that the inmate had two sons
and three brothers, including Mitcham. Only Mitcham and one other
brother lived in the Phoenix area.

¶7           The police focused their investigation on Mitcham. An
investigating officer reviewed Mitcham’s 2015 DUI arrest records and
learned that both vials of blood taken from Mitcham were still in police
possession. Without obtaining a warrant, the police analyzed the blood in
the second vial and created Mitcham’s DNA profile. On April 5, 2018, the
police crime lab determined that Mitcham’s profile matched the
unknown-male DNA profile taken from Feldman’s house.

¶8             Days later, the trial court issued search warrants permitting
officers to search Mitcham’s home and seize certain items; place a GPS
tracking device on his car; and obtain buccal samples from Mitcham for
purposes of DNA profiling.          The affidavits supporting the warrant
applications described the circumstances leading the police to Mitcham and
stated that officers had used the blood sample taken in the 2015 DUI arrest
to match Mitcham’s DNA with the unknown-male DNA profile from the
murder scene.

¶9             On April 10, police collected buccal swabs from Mitcham
pursuant to the search warrant. The police created another DNA profile
from this sample, which again matched the unknown-male DNA profile
taken from the murder scene. On April 18, a grand jury indicted Mitcham
for first degree murder, second degree burglary, and sexual assault.

¶10           On July 7, 2022, Mitcham moved the trial court to suppress
both (1) the DNA evidence gathered from the second vial taken during his
2015 DUI arrest; and (2) the DNA evidence extracted from the buccal swabs
collected pursuant to the 2018 search warrant. After an evidentiary
hearing, the court granted the motion, reasoning that the warrantless search
of the second vial of blood violated the Fourth Amendment, and no
exceptions to exclusion applied. It also suppressed the DNA evidence
gathered from the buccal swabs pursuant to the warrant, reasoning that the
evidence was “the direct result of the improper DNA extraction [in 2018].”
The court subsequently stayed proceedings to permit the State to appeal its
                                     4
                             STATE V. MITCHAM
                            Opinion of the Court

ruling. See A.R.S. § 13-4032(6) (permitting the state to appeal “[a]n order
granting a motion to suppress the use of evidence”).

¶11             The court of appeals unanimously reversed, but the judges
had different reasons for doing so. See State v. Mitcham, 256 Ariz. 104
(App. 2023). The majority concluded that although the police had violated
Mitcham’s Fourth Amendment rights, excluding the DNA evidence was
not warranted because the evidence would inevitably have been
discovered, and it had an independent source. See id. at 115 ¶¶ 46–47, 51.
The concurring judge found no Fourth Amendment violation, explaining
that Mitcham did not have a reasonable expectation of privacy in the second
vial of blood because it was lawfully in police possession. See id. ¶ 53
(Catlett, J., concurring).

¶12           We granted Mitcham’s subsequently filed petition for review
to determine (1) whether the sequencing of Mitcham’s DNA profile from
the second vial of blood taken during the 2015 DUI arrest constituted a
search and violated Mitcham’s rights under the Fourth Amendment; and
(2) if so, whether the DNA evidence should be suppressed. These are
potentially recurring issues of statewide importance and therefore merit
our review. We have jurisdiction under article 6, section 5(3) of the
Arizona Constitution.

                               DISCUSSION

¶13           We review a trial court’s factual findings on a motion to
suppress for an abuse of discretion. State v. Smith, 250 Ariz. 69, 80 ¶ 16
(2020). In doing so, we consider “only the evidence presented at the
suppression hearing and [view such evidence] in the light most favorable
to sustaining the trial court’s ruling.” State v. Thompson, 252 Ariz. 279, 290
¶ 26 (2022) (quoting State v. Primous, 242 Ariz. 221, 223 ¶ 10 (2017)). But
we review de novo the trial court’s legal determination about whether a
search complied with the Fourth Amendment. State v. Jean, 243 Ariz. 331,
334 ¶ 9 (2018).

A. The Police Violated Mitcham’s Fourth Amendment Rights By
Sequencing A DNA Profile From The Second Vial Of Blood Taken
During The 2015 DUI Arrest.

¶14          The Fourth Amendment to the United States Constitution
“safeguard[s] the privacy and security of individuals against arbitrary

                                      5
                             STATE V. MITCHAM
                            Opinion of the Court

invasions by governmental officials.” Carpenter v. United States, 585 U.S.
296, 303 (2018) (quoting Camara v. Municipal Court, 387 U.S. 523, 528 (1967)).
Although Fourth Amendment violations were formerly “tied to
common-law trespass,” United States v. Jones, 565 U.S. 400, 405 (2012), the
Supreme Court has recognized that “the Fourth Amendment protects
people, not places,” Carpenter, 585 U.S. at 304 (quoting Katz v. United States,
389 U.S. 347, 351 (1967)). Thus, when an individual “seeks to preserve
[something] as private,” and that expectation of privacy is “one that society
is prepared to recognize as ‘reasonable,’” Fourth Amendment protections
will apply. Smith v. Maryland, 442 U.S. 735, 740 (1979) (alteration in
original) (quoting Katz, 389 U.S. at 351, 361); see also Florida v. Jimeno, 500
U.S. 248, 250 (1991) (“The touchstone of the Fourth Amendment is
reasonableness.”).

¶15           A search occurs when the government infringes a privacy
interest that society considers to be reasonable. See State v. Mixton, 250
Ariz. 282, 286 ¶ 13 (2021). Such an intrusion “generally . . . requires a
warrant supported by probable cause.”         Carpenter, 585 U.S. at 304.
Warrantless searches are “per se unreasonable under the Fourth
Amendment—subject only to a few specifically established and
well-delineated exceptions.” Katz, 389 U.S. at 357 (footnote omitted).

       1.   A search occurred here.

¶16           The State argues that sequencing Mitcham’s DNA from the
second vial of blood collected during his 2015 DUI arrest was not a “search”
for Fourth Amendment purposes because it already lawfully possessed the
blood. To resolve this argument, we begin with this Court’s opinion in
Mario W. v. Kaipio, 230 Ariz. 122 (2012). There, we considered the
constitutionality of an Arizona law requiring juveniles accused of
committing enumerated offenses to provide law enforcement with a buccal
swab for DNA profiling. Id. at 123–24 ¶ 1. After sequencing, the DNA
profiles were entered into CODIS and Arizona’s DNA identification
database. See id. at 124 ¶ 5. If not ultimately adjudicated delinquent, the
juvenile could petition the court for expungement of the profile from the
databases. Id.

¶17            The Court recognized that the challenged law intruded on a
juvenile’s privacy by authorizing law enforcement to both physically collect
the buccal sample and then process it to extract a DNA profile. Id.
at 126–27 ¶ 18. We therefore addressed each intrusion separately. See id.

                                      6
                             STATE V. MITCHAM
                            Opinion of the Court

at 127 ¶ 20 (noting that a two-tiered analysis was particularly appropriate
because DNA profiling is much more intrusive than collecting buccal cells).

¶18           We first concluded that collecting the buccal sample was
constitutionally permissible. Id. at 128 ¶ 25. We reasoned that the buccal
swab was minimally intrusive, and the state was justified in collecting the
sample for identification purposes before the juvenile was adjudicated
delinquent because it would lose its chance at collection if the juvenile
absconded. See id. at 127–28 ¶¶ 22–25.

¶19            We then reached a different conclusion about the
constitutionality of extracting a DNA profile from the buccal sample before
the juvenile was adjudicated delinquent.           See id. at 129 ¶ 32.    We
recognized that “[t]his second search presents a greater privacy concern
than the buccal swab because it involves the extraction (and subsequent
publication to law enforcement nationwide) of thirteen genetic markers
from the arrestee’s DNA sample that create a DNA profile effectively
unique to that individual.” Id. at 128 ¶ 27. Further, we could not
perceive any governmental interest in processing the sample and creating
the DNA profile before adjudication. Id. at 129 ¶ 28. Thus, we concluded
that the state’s interest in processing the sample before adjudication did not
justify the serious intrusion on a juvenile’s privacy interest in the DNA
profile. Id. ¶ 32. Notably, we remarked that:

       [O]ne accused of a crime, although having diminished
       expectations of privacy in some respects, does not forfeit
       Fourth Amendment protections with respect to other offenses
       not charged absent either probable cause or reasonable
       suspicion. An arrest for vehicular homicide, for example,
       cannot alone justify a warrantless search of an arrestee’s
       financial records to see if he is also an embezzler.

Id. ¶ 31. We therefore disallowed processing the buccal cells to extract a
DNA profile before a delinquency adjudication as an unreasonable search
under the Fourth Amendment. See id. ¶ 32.

¶20           Although Mario W. seemingly resolves that the police in this
case conducted a “search” by extracting Mitcham’s DNA profile from the
second vial of blood taken during his 2015 DUI arrest, the State argues that
the Supreme Court in Maryland v. King, 569 U.S. 435 (2013), overruled Mario
W. The State describes King as concluding that “sequencing a DNA profile
                                      7
                            STATE V. MITCHAM
                           Opinion of the Court

from lawfully obtained evidence is not a second ‘search’ within the
meaning of the Fourth Amendment.” With that characterization, the State
argues that King overruled Mario W. to the extent the latter case concluded
that creating a DNA profile from a buccal swab is a “search” under the
Fourth Amendment. We disagree.

¶21           In King, the Supreme Court held that a Maryland law
authorizing law enforcement officials to “collect DNA samples” from
persons arrested for specific felony offenses—committing or attempting to
commit violent crimes or burglaries—did not violate the Fourth
Amendment. 569 U.S. at 443, 465. The Court found that “using a buccal
swab on the inner tissues of a person’s cheek in order to obtain DNA
samples is a search.” Id. at 446. But it noted that “[t]he expectations of
privacy of an individual taken into police custody ‘necessarily [are] of a
diminished scope.’” Id. at 462 (second alteration in original) (quoting Bell
v. Wolfish, 441 U.S. 520, 557 (1979)). It characterized that search as
minimally intrusive and outweighed by substantial government interests
in identifying arrestees and determining whether they had committed other
crimes. Id. at 461, 463–64. And the DNA analysis did not reveal any
information about the arrestee other than mere identification.           Id.
at 464–65.

¶22           Importantly, the Court never addressed whether creating a
DNA profile from the buccal sample was a separate “search.” Instead, the
Court examined as a set whether collecting and analyzing a DNA sample
taken from felony arrestees violates the Fourth Amendment. See id. at 442.
Because the collection and analysis occurred in short order as part of “a
routine booking procedure” after a suspect’s arrest, the Court had no need
to address whether the analysis itself was a “search.” See id. at 465.

¶23            The conclusion we take from King is that “taking and
analyzing a cheek swab of the arrestee’s DNA is, like fingerprinting and
photographing, a legitimate police booking procedure that is reasonable
under the Fourth Amendment.” Id. at 465–66 (“Upon these considerations
the Court concludes that DNA identification of arrestees is a reasonable
search that can be considered part of a routine booking procedure.”
(emphasis added)). Thus, King overruled Mario W. to the extent the latter
case held that processing buccal swabs before adjudication violated the
juveniles’ Fourth Amendment rights. See Mario W., 230 Ariz. at 129 ¶ 32.
But King did not address whether creating a DNA profile from an arrestee’s
cell sample itself constitutes a separate search. Thus, we do not view King
                                     8
                             STATE V. MITCHAM
                            Opinion of the Court

as overruling Mario W.’s conclusion that processing a sample to extract a
DNA profile is a search. Cf. Birchfield v. N.D. Dep’t of Transp., 579 U.S. 438,
464 (2016) (recognizing that blood can reveal information beyond alcohol
and drug content); Skinner v. Ry. Lab. Execs.’ Ass’n, 489 U.S. 602, 617–18
(1989) (referring to “the collection and subsequent analysis [of urine
samples]” as separate searches under the Fourth Amendment).

¶24            Mario W. remains controlling. We therefore conclude that
extracting Mitcham’s DNA profile in 2018 from the second vial of blood
taken during his 2015 DUI arrest was a “search” under the Fourth
Amendment. See also Skinner, 489 U.S. at 616 (recognizing that the
chemical analysis of a blood sample to obtain physiological data is an
invasion of privacy interests apart from the blood draw itself); State v.
Martinez, 570 S.W.3d 278, 292 (Tex. Crim. App. 2019) (concluding that
subsequent testing of blood drawn for medical purposes constituted “a
Fourth Amendment search separate and apart from the seizure of the blood
by the State”); People v. Thomas, 132 Cal. Rptr. 3d 714, 716 (Cal. Ct. App.
2011) (“When an individual is compelled to provide a biological sample for
analysis, the collection and subsequent analysis of the sample are treated as
separate searches because they intrude on separate privacy interests.”).

       2.   The search was unreasonable.

¶25             Unlike the situation in King, the police here did not extract
Mitcham’s DNA profile pursuant to statutory authority governing routine
booking procedures intended to identify perpetrators. See 569 U.S. at 443;
see also In re Leopoldo L., 209 Ariz. 249, 252 ¶ 14 (App. 2004) (explaining that
“compelled DNA testing of juveniles adjudicated delinquent for
committing sexual offenses is not an unreasonable search” because
statutory procedural safeguards “are more stringent than those required for
issuance of a search warrant based on a probable cause finding”). And the
police did not obtain a warrant to create Mitcham’s DNA profile from the
second vial of blood. Under these circumstances, the warrantless search
was unreasonable under the Fourth Amendment absent an exception. See
Katz, 389 U.S. at 357.

¶26           One such exception occurred here if Mitcham freely and
voluntarily consented to the search. See State v. Valenzuela, 239 Ariz. 299,
301 ¶ 1 (2016); see also Jimeno, 500 U.S. at 250–51 (“[W]e have long approved
consensual searches because it is no doubt reasonable for the police to
conduct a search once they have been permitted to do so.”). The State

                                       9
                             STATE V. MITCHAM
                            Opinion of the Court

bears the burden of proving by a preponderance of the evidence that
Mitcham voluntarily consented to the search and that the search fell within
the scope of that consent. See Valenzuela, 239 Ariz. at 302–03 ¶ 11; State v.
Ontiveros-Loya, 237 Ariz. 472, 479 ¶ 24 (App. 2015); Ariz. R. Crim. P. 16.2(b);
see also Walter v. United States, 447 U.S. 649, 656 (1980) (“When an official
search is properly authorized—whether by consent or by the issuance of a
valid warrant—the scope of the search is limited by the terms of its
authorization.”).

¶27            The State argues that Mitcham consented to the 2018
warrantless search by consenting to the 2015 DUI blood draw, giving the
State lawful possession of the sample and the freedom to later use it to
create a DNA profile. Mitcham acknowledges he consented to the blood
draw in 2015 to allow the State to determine his alcohol concentration or
drug content. But he argues the State exceeded the scope of that consent
by later creating the DNA profile to determine his culpability for Feldman’s
murder, making the warrantless search unreasonable under the Fourth
Amendment.

¶28          Courts measure the scope of a consent to search using an
objective standard: “what would the typical reasonable person have
understood by the exchange between the officer and the suspect?” Jimeno,
500 U.S. at 251. The question before us then is whether a reasonable
person would have understood that consenting to a blood draw to
determine alcohol concentration or drug content would include consent to
create a DNA profile from that sample. See id. We do not think so.

¶29           Here, the search authorization terms were simple and
unambiguous. Mitcham consented to the blood draw after an officer
advised him that Arizona’s implied consent law required him to submit to
the blood draw “for the purpose of determining alcohol concentration or
drug content.” 1 See A.R.S. § 28-1321(A). The officer did not tell Mitcham
that his blood could be used to create a DNA profile, and Mitcham did not
consent to the search of his blood for that purpose. Further, it was not

1  The year after Mitcham’s blood draw, we held that “showing only that
consent was given in response to this admonition fails to prove that an
arrestee’s consent was freely and voluntarily given.” Valenzuela, 239 Ariz.
at 301 ¶ 2. Mitcham does not challenge the voluntariness of his consent to
draw his blood for purposes of determining his alcohol concentration or
drug content.
                                      10
                             STATE V. MITCHAM
                            Opinion of the Court

necessary to create a DNA profile to determine alcohol concentration or
drug content. And Mitcham agreed that his second vial of blood would
be destroyed in ninety days if he did not first retrieve it, further supporting
a reasonable belief that Mitcham’s consent was limited to searching for
evidence pertinent only to the pending DUI charge, not other, future
crimes.

¶30            A typical reasonable person in Mitcham’s circumstances
would not have understood that consenting to the blood draw for the
limited purpose of determining alcohol concentration or drug content also
included consenting to the creation of a DNA profile, especially years later.
See Jimeno, 500 U.S. at 251. The search of the blood to create the DNA
profile therefore exceeded the scope of Mitcham’s consent and cannot serve
as an exception to the warrant requirement. See State v. Billups, 118 Ariz.
124, 126 (1978) (finding that police exceeded the scope of the defendant’s
consent to search his house by searching an unattached shed); United States
v. Dichiarinte, 445 F.2d 126, 128, 130 (7th Cir. 1971) (finding that federal
narcotics agents exceeded the scope of the defendant’s consent to search his
home for narcotics by searching for documents); see also People v. Schmoll, 48
N.E.2d 933, 934 (Ill. 1943) (“An arresting officer has no more right to make
a search beyond the limit prescribed in a consent to search, than he has to
exceed the limit prescribed in a search warrant.”). Other courts have
reached similar conclusions in analogous situations. See People v. Pickard,
222 Cal. Rptr. 3d 686, 687, 689 (Cal. App. Dep’t Super. Ct. 2017) (recognizing
that when a driver consents to a blood test under a state’s implied consent
law, further testing of the sample for other substances or DNA may be
beyond the scope of the consent); State v. Binner, 886 P.2d 1056, 1059 (Or.
Ct. App. 1994) (concluding that the defendant who consented to a blood
draw for purposes of determining alcohol concentration did not consent to
having his blood tested for drugs); State v. Gerace, 437 S.E.2d 862, 863 (Ga.
Ct. App. 1993) (concluding that consent given to test blood for alcohol
concentration did not include consent to extract a DNA profile).

¶31            In sum, the 2018 creation of Mitcham’s DNA profile from the
second vial of blood taken during the 2015 DUI arrest was a search. That
search was unreasonable and violated the Fourth Amendment because it
was not authorized by a warrant, and the search exceeded the scope of
Mitcham’s consent to analyze his blood to determine alcohol concentration
or drug content. In reaching this conclusion, we emphatically reject the
State’s position that it was free to analyze Mitcham’s blood in any way it
pleased simply because the State lawfully possessed the blood vials. See
                                      11
                              STATE V. MITCHAM
                             Opinion of the Court

Walter, 447 U.S. at 654 (“The fact that FBI agents were lawfully in possession
of the boxes of film did not give them authority to search their contents.”);
Gerace, 437 S.E.2d at 863 (“The State’s argument that because the blood
sample was obtained with consent it is free to use it for any purpose, paints
the notion of consent with far too broad a brush.”). Although Mitcham
lost his possessory rights to the second vial of blood, he did not lose all of
his privacy rights in that blood. See Mario W., 230 Ariz. at 128 ¶ 27, 129
¶ 31; see also State v. Granville, 423 S.W.3d 399, 426 (Tex. Crim. App. 2014)
(Keller, P.J., concurring) (recognizing that people can have expectations of
privacy in the informational dimension of property separate and apart from
the expectation of privacy in the physical dimension of that property). The
police violated Mitcham’s Fourth Amendment rights by conducting a
search beyond the scope of his consent.

B. The Exclusionary Rule Does Not Require Suppression Of Mitcham’s
DNA Profile.

       1.   There are exceptions to the exclusionary rule.

¶32             The Fourth Amendment itself does not require courts to
suppress evidence gathered in violation of that amendment. See Davis v.
United States, 564 U.S. 229, 236–38 (2011). Instead, courts invoke the
judicially created “exclusionary rule” to suppress evidence obtained in
violation of the Fourth Amendment. See Utah v. Strieff, 579 U.S. 232, 237
(2016); Wong Sun v. United States, 371 U.S. 471, 484–85 (1963); Valenzuela, 239
Ariz. at 308–09 ¶ 31. The exclusionary rule is a prudential doctrine created
to “compel respect for the constitutional guaranty” by deterring future
violations. See Davis, 564 U.S. at 236 (quoting Elkins v. United States, 364
U.S. 206, 217 (1960)); Valenzuela, 239 Ariz. at 308–09 ¶ 31. The rule applies
to evidence obtained directly from an illegal search and to evidence later
discovered because of the illegal search, which is commonly called the
“fruit of the poisonous tree.” Strieff, 579 U.S. at 237 (quoting Segura v.
United States, 468 U.S. 796, 804 (1984)). The rationale for the exclusionary
rule is that the prosecution should not be placed in a better position because
of the illegal conduct. Nix v. Williams, 467 U.S. 431, 443 (1984).

¶33            Importantly, “[s]uppression of evidence . . . has always been
our last resort, not our first impulse.” Hudson v. Michigan, 547 U.S. 586,
591 (2006); State v. Weakland, 246 Ariz. 67, 73 ¶ 20 (2019). We only apply
the exclusionary rule “where its deterrence benefits outweigh its
‘substantial social costs.’” Hudson, 547 U.S. at 591 (quoting Pa. Bd. of Prob.
& Parole v. Scott, 524 U.S. 357, 363 (1998)); Nix, 467 U.S. at 443 (accepting that
                                        12
                              STATE V. MITCHAM
                             Opinion of the Court

the way to ensure Fourth Amendment protections “is to exclude evidence
seized as a result of such violations notwithstanding the high social cost of
letting persons obviously guilty go unpunished for their crimes”).
Consequently, we have recognized several exceptions to the exclusionary
rule, including the “independent source” and “inevitable discovery”
exceptions. See Strieff, 579 U.S. at 238.

¶34             The “independent source” exception permits the admission
of evidence discovered during or because of an unlawful search if the
evidence was also obtained independently from activities that were tainted
by the illegality. See Murray v. United States, 487 U.S. 533, 537–38 (1988);
State v. Bolt, 142 Ariz. 260, 263 (1984). For instance, in Segura, the Supreme
Court held that although the police illegally entered private premises, the
exclusionary rule did not apply because police seized property at those
premises pursuant to a search warrant that was based on information
unconnected to the illegal entry. 468 U.S. at 814. The independent
source exception, which applies to violations of the Fourth, Fifth, and Sixth
Amendments, rests on the premise that “while the government should not
profit from its illegal activity, neither should it be placed in a worse position
than it would otherwise have occupied” without the illegal conduct. See
Murray, 487 U.S. at 537, 542.

¶35            The “inevitable discovery” exception applies “[i]f the
prosecution can establish by a preponderance of the evidence that the
information ultimately or inevitably would have been discovered by lawful
means,” making the reason for applying the exclusionary rule meaningless.
Nix, 467 U.S. at 444.      Courts extrapolated this exception from the
independent source exception, reasoning that because “tainted evidence
would be admissible if in fact discovered through an independent source,
it should be admissible if it inevitably would have been discovered” from
such a source. Murray, 487 U.S. at 539. Importantly, “[t]he exception
does not turn on whether the evidence would have been discovered had
[officers] acted lawfully in the first place,” but instead “applies if the
evidence would have been lawfully discovered despite the unlawful
behavior and independent of it.” Brown v. McClennen, 239 Ariz. 521,
524–25 ¶ 14 (2016) (emphasis added). For example, in State v. Jones, 185
Ariz. 471, 481 (1996), we held that despite an improper warrantless search
of the arrested defendant’s belongings while stowed in a police car, because
police inevitably would have conducted a proper inventory search of those
belongings upon return to the station, the exclusionary rule did not apply
to suppress evidence of the defendant’s bloody clothing.
                                       13
                            STATE V. MITCHAM
                           Opinion of the Court


¶36           In sum, the distinction between the independent source
exception and the inevitable discovery exception rests on whether the
evidence was discovered through an independent, untainted source
(independent source exception), or whether the evidence would have been
discovered through an independent, untainted source despite the illegal
search (inevitable discovery exception). See State v. Boll, 651 N.W.2d 710,
716–17 ¶¶ 20–26 (S.D. 2002) (similarly distinguishing these exceptions).

      2.   The inevitable discovery exception applies here.

¶37            Turning to this case, we agree with the State that the police
would have inevitably obtained Mitcham’s DNA profile from an
independent, untainted source despite the warrantless search of the second
vial of blood taken after the 2015 DUI arrest. To prove the inevitable
discovery exception, the State cannot speculate but must instead “focus[]
on demonstrated historical facts capable of ready verification or
impeachment.” Nix, 467 U.S. at 444 n.5. The court “view[s] affairs as
they existed at the instant before the unlawful search” and then determines
“what would have happened had the unlawful search never occurred.”
United States v. Kennedy, 61 F.3d 494, 498 (6th Cir. 1995) (quoting United
States v. Eng, 971 F.2d 854, 861 (2d Cir. 1992)).

¶38            Here, the verifiable facts demonstrate inevitable discovery of
Mitcham’s DNA profile. At the time of the illegal search in 2018, Mitcham
was facing charges unrelated to Feldman’s murder. In 2016, the state
charged him with committing a narcotic drug violation, a class four felony.
The next year, the state charged him with two counts of aggravated DUI,
class six felonies. In June 2022, about six months before the suppression
hearing in this case, Mitcham pled guilty to all charges in the narcotics/DUI
cases, and the court sentenced him to a term of imprisonment in the Arizona
Department of Corrections, Rehabilitation and Reentry (“ADCRR”).

¶39           Arizona law requires ADCRR to take a sample of blood or
other bodily substance for purposes of DNA profiling from every person
convicted of a felony and sentenced to prison. See A.R.S. § 13-610(A), (O). 2


2 Section 13-610(A) refers to the “state department of corrections.” That
agency has changed its name to the “Arizona Department of Corrections,
Rehabilitation   and    Reentry.”         See   ADCRR      Home      Page,

                                     14
                             STATE V. MITCHAM
                            Opinion of the Court

Thereafter, ADCRR is required to transmit the sample to DPS, which must
extract a DNA profile and enter the results into Arizona’s DNA
identification system and CODIS. See Mario W., 230 Ariz. at 124 ¶ 5;
§ 13-610(H); § 41-2418(A).     The profile can then be used for “law
enforcement identification purposes” and in any criminal prosecution.
See § 13-610(I)(1)–(2). ADCRR must extract the sample for DNA profiling
within thirty days of sentencing but is prohibited from doing so if DPS “has
previously received and is maintaining a sample sufficient for [DNA]
testing.” See § 13-610(A), (G).

¶40           Pursuant to § 13-610, the State would have inevitably
discovered Mitcham’s DNA profile despite the illegal search of the second
vial of blood taken in 2015. The narcotics/DUI convictions and resulting
sentences were unrelated to and thus untainted by the illegal searches.
Had those searches not occurred, § 13-610(A) would have required ADCRR
to collect samples of Mitcham’s blood or bodily substances, and DPS would
have obtained the same DNA profile that was extracted from the second
vial of blood. As Mitcham acknowledged at oral argument, the only
reason this did not occur was because DPS already had Mitcham’s genetic
sample and DNA profile from the searches conducted in 2018, 3 and was
therefore prohibited from taking new samples.               See § 13-610(G).
Suppressing the DNA evidence in these circumstances would not fulfill the
exclusionary rule’s purpose of preventing the prosecution from being in a
better position due to the illegal search. See Nix, 467 U.S. at 443. Instead,
suppression would put the prosecution in a worse position than it would
have been in without the illegal search. See Murray, 487 U.S. at 537, 542.

¶41           We are not persuaded by Mitcham’s arguments against
application of the inevitable discovery exception. First, he argues that the


https://corrections.az.gov (last visited Dec. 9, 2024). We therefore refer to
the agency using its current name.
3  We could not determine from the record whether the Scottsdale Police
transferred Mitcham’s blood sample to DPS and uploaded the DNA profile
into Arizona’s DNA identification system. But the police were required to
transmit a sample of buccal cells or other bodily substances for DNA testing
to DPS when Mitcham was arrested for Feldman’s murder in 2018. See
§ 13-610(K) (requiring transmittal of a sample for persons arrested for listed
offenses, including first degree murder). Mitcham acknowledges that in
2018 DPS had a sample of his genetic material and his DNA profile.
                                     15
                            STATE V. MITCHAM
                           Opinion of the Court

DNA profile would not have been inevitably discovered from his 2022
felony convictions because DPS never received a blood or bodily substance
sample from which to create a DNA profile. See § 13-610(A). This
argument places form over substance, and we reject it. As explained,
§ 13-610(G) prohibited ADCRR from extracting a new sample because DPS
already had a sample and a DNA profile. The point here is that had the
illegal search not occurred, ADCRR would have provided a sample to DPS,
which would have extracted Mitcham’s DNA profile. And no purpose
would be served by suppressing Mitcham’s DNA profile only to have
ADCRR provide DPS with a new sample so the same profile could again be
extracted.

¶42            Second, Mitcham asserts that the inevitable discovery
exception applies only when “regular police work already in progress” at
the time of the illegal search demonstrates that the evidence would have
been inevitably discovered. Mitcham contends that because “the possible
‘future’ acquisition of [his] DNA from his 2022 convictions is not evidence
that ‘inevitably’ emerged during the homicide investigation,” and the
police “had no way of knowing that [he] would plead guilty over four years
later” to the narcotics/DUI charges, the police investigating at the time of
the illegal searches would not have inevitably discovered his DNA profile.
Applying the inevitable discovery exception in these circumstances, he
argues, would “rel[y] solely on speculation, and such speculation alone
cannot sustain the State’s burden” under Nix. We disagree.

¶43            Relying exclusively on investigative facts and procedures
available to police at the time of the illegal search to assess inevitable
discovery is unnecessarily restrictive. Nix did not confine the examination
of “historical facts capable of ready verification or impeachment” to facts
existing before an illegal search. See Nix, 467 U.S. at 444 n.5. Notably,
“Arizona has adopted the broad view of the inevitable discovery rule,” and
so “the State is not required to demonstrate that police initiated lawful
means to acquire evidence prior to its seizure.” State v. Davolt, 207 Ariz.
191, 204 ¶ 37 (2004). Similarly, we see no reason to require the State to
prove the exception by projecting investigative outcomes using only facts
available to the police before the illegal search. The key inquiry is whether
verifiable facts exist from which the court can find, at the time of the
suppression hearing, that the evidence would have been lawfully
discovered despite the illegal search and independent of it. See Brown, 239
Ariz. at 525 ¶ 14.


                                     16
                             STATE V. MITCHAM
                            Opinion of the Court

¶44            We find the Seventh Circuit’s decision in Sutton v. Pfister, 834
F.3d 816 (7th Cir. 2016), persuasive. There, the State of Illinois unlawfully
collected a sample of defendant Sutton’s blood during his prosecution for a
1991 attempted sexual assault and extracted his DNA profile. Id. at 818.
The state did not introduce DNA evidence at trial, but Sutton was
nevertheless convicted and sentenced to prison. See id. Meanwhile, law
enforcement matched Sutton’s illegally obtained DNA profile to physical
evidence collected from a 1990 sexual assault. See id. The Seventh Circuit
held that the inevitable discovery exception permitted the trial court to
admit the DNA evidence in Sutton’s 1990 sexual assault trial. See id. at 822.
It found that the state would have lawfully obtained Sutton’s blood sample
upon his conviction for the 1991 attempted sexual assault pursuant to an
Illinois law that required blood and saliva samples from convicted sex
offenders. See id. Conspicuously, the decision did not turn on whether
police in the 1991 case had any way of knowing at the time of the illegal
search that Sutton would be convicted without the DNA evidence and then
lawfully required to submit blood and saliva samples.

¶45           The cases cited by Mitcham do not persuade us to view the
inevitable discovery exception more restrictively. In State v. Lamb, 116
Ariz. 134, 138 (1977), this Court agreed with other courts that “evidence
obtained as a result of an unlawful search need not be suppressed where,
in the normal course of the police investigation and absent the illicit
conduct, the evidence would have been discovered anyway.” Although
the events demonstrating inevitable discovery there had occurred at the
time of the illegal search, nothing in Lamb precluded application of the
inevitable discovery exception if new events had occurred after the illegal
search. The key consideration was whether the means of discovery was
untainted by the illegal search. See id.

¶46           The cases Mitcham cites from other jurisdictions admittedly
use language suggesting that the inevitable discovery exception applies
only when investigative facts existing before an illegal search demonstrate
inevitable discovery. See United States v. Lang, 149 F.3d 1044, 1047 (9th Cir.
1998) (stating that application of the exception requires a court “to
determine whether a reasonable probability of discovery existed prior to
the unlawful conduct, based on the information possessed and
investigations being pursued at such time” (quoting United States v. Drosten,
819 F.2d 1067, 1070 (11th Cir. 1987))); Eng, 971 F.2d at 861 (“[T]he alternate
means of obtaining the evidence must at least be in existence and, at least
to some degree, imminent, if yet unrealized.” (alteration in original)
                                      17
                             STATE V. MITCHAM
                            Opinion of the Court

(quoting United States v. Cherry, 759 F.2d 1196, 1205 n.10 (5th Cir. 1985))).
Neither case, however, dealt with identification evidence like the DNA
evidence here, which can be extracted from different sources and at
different times. Rather, they concerned physical evidence that was the
subject of the illegal search. See Lang, 149 F.3d at 1046 (concerning “crack
cocaine found in a cereal box hidden inside the engine compartment” of a
vehicle); Eng, 971 F.2d at 857 (regarding the contents of defendant’s safe).
Thus, it is unsurprising that these courts required the government to show
that an active investigation, independent from and untainted by the illegal
search, would have uncovered the evidence. Regardless, to the extent
these cases categorically preclude assessment of events occurring after the
illegal search to decide whether to apply the inevitable discovery exception,
we disagree for the reasons previously explained. See Part B(2), ¶¶ 38–40,
43–44.

¶47            In sum, the inevitable discovery exception applies here, and
the trial court therefore erred by suppressing Mitcham’s DNA profile. If
the police had not created a DNA profile from the second vial of blood in
2018, DPS would have done so after his 2022 felony convictions. This is
certain, not speculative, so it easily satisfies the preponderance standard
adopted in Nix. See Nix, 467 U.S. at 444 n.5. In light of this conclusion,
we do not address whether other exceptions to the exclusionary rule apply
here. And we do not address Mitcham’s arguments based on the Arizona
Constitution’s Private Affairs Clause, as they were neither raised at the trial
court nor sufficiently developed here. See Ariz. Const. art. 2, § 8.

                              CONCLUSION

¶48           For the foregoing reasons, although we agree with the court
of appeals’ holding, we vacate its opinion to replace its reasoning with our
own. We also reverse the trial court’s suppression order and remand for
further proceedings.




                                      18

```

---
