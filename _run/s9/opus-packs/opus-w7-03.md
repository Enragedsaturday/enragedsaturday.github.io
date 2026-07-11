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

## GROUP: _overhaul2/lake/cases/Martin v. United States.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Martin v. United States
type: case
citation: "605 U.S. 395 (2025)"
parallel_cite: ""
neutral_cite: ""
court: U.S.
court_level: scotus
circuit: ""
year: 2025
date_decided: 2025-06-12
docket: 24-362
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
  opinion_url: "https://www.courtlistener.com/opinion/10776839/martin-v-united-states/"
  cluster_id: 10776839
  opinion_id: null
  identity_checked: true
lake:
  record_id: Martin v. United States
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
  - ftca
  - federal-officer-liability
  - section-1983
  - wrong-house-raid
holding: "In an FTCA suit arising from a wrong-house raid, the § 2680(h) law-enforcement proviso overrides only that subsection's intentional-tort exception (not the discretionary-function exception), and the Supremacy Clause affords the United States no defense; the Eleventh Circuit's contrary rulings were vacated and remanded."
---

# Martin v. United States

*605 U.S. 395 (2025)* (No. 24-362) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10776839 → opinion 11243426; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
An FBI SWAT team executing a warrant raided the wrong Atlanta house — the home of Curtrina Martin, her partner Hilliard Toi Cliatt, and her seven-year-old son — detonating a flash-bang, breaking down the door, and detaining the occupants before realizing the mistake. The family sued the United States under the Federal Tort Claims Act for the officers' negligent and intentional torts. The Eleventh Circuit affirmed summary judgment for the government on two grounds: it dismissed the negligence claims under the FTCA's discretionary-function exception, and it held the remaining intentional-tort claims defeated by a Supremacy Clause defense that shields officers whose conduct has some nexus with furthering federal policy.

## Issue
Whether the FTCA's § 2680(h) law-enforcement proviso overrides the discretionary-function exception (so that intentional-tort claims automatically proceed), and whether the Supremacy Clause affords the United States a defense in FTCA suits.

## Rule
The § 2680(h) law-enforcement proviso is textually confined: it overrides only the intentional-tort exception within that same subsection, not the discretionary-function exception or the other § 2680 exceptions — so a proviso claim must still clear those other bars. And the Supremacy Clause supplies no separate defense: because the FTCA makes the United States liable under the "law of the place" on the same terms as a private party, "in most cases there is no conflict for the Supremacy Clause to resolve." The Court held that "we find the government's concession commendable and correct: The FTCA does not permit the Eleventh Circuit's Supremacy Clause defense." — 605 U.S. at 409. ^pin-409

## Application
The Eleventh Circuit had inverted the statute — treating the proviso as automatically defeating the discretionary-function exception, then offsetting that plaintiff-friendly reading with a novel Supremacy Clause defense found nowhere in § 2674's enumerated defenses. Both moves were wrong. Georgia law (the "law of the place") would let a homeowner sue a private person who mistakenly raided and assaulted him, and no federal statute or constitutional text displaced that liability rule. [[Reading and Citing Cases#on-remand|On remand]] the Eleventh Circuit must decide whether the discretionary-function exception bars any of the claims — without the mistaken premise that the proviso overrides it — and, for surviving claims, apply Georgia's private-analog standard subject only to the § 2674 defenses.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Gorsuch, J., delivered the opinion of a unanimous Court; Sotomayor, J., joined by Jackson, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Martin* is an FTCA decision rather than a *[[Bivens v. Six Unknown Named Agents|Bivens]]* or § 1983 case, but it is central to the remedies available against federal officers for wrong-house raids: it removes two barriers the Eleventh Circuit had erected and returns the wrong-house-raid liability question to the lower courts.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Martin v. United States*, 605 U.S. 395 (2025)](https://www.courtlistener.com/opinion/10776839/martin-v-united-states/) — pinpoint: 409–413 (Supremacy Clause holding, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3ca35bee086c461a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Martin v. United States"}, "payload": {"all": [{"cite": "605 U.S. 395", "page": "395", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "605"}], "display": "605 U.S. 395", "official": {"cite": "605 U.S. 395", "page": "395", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "605"}, "official_selection_present": true, "record_id": "Martin v. United States"}}
{"assertion_id": "2682603d10df1b7e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Martin v. United States"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Martin v. United States", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Martin v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Martin v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Martin v. United States",
    "case_name_short": "Martin",
    "case_name_full": "",
    "input_case_name": "Martin v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2025-06-12",
    "year": 2025,
    "docket": "24-362",
    "cluster_id": 10776839,
    "lead_opinion_id": 11243426,
    "sibling_ids": [],
    "absolute_url": "/opinion/10776839/martin-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 10603452,
        "score": 120,
        "case_name": "Martin v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "605 U.S. 395",
      "volume": "605",
      "reporter": "U.S.",
      "page": "395",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "605 U.S. 395",
        "volume": "605",
        "reporter": "U.S.",
        "page": "395",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "605 U.S. 395",
    "official_selection": {
      "court_class": "scotus",
      "selected": "605 U.S. 395",
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
    "date_created": "2026-07-07T01:37:28Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:37:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "martin-v-united-states--10776839",
      "to_record_id": "Martin v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Martin v. United States

```
                   PRELIMINARY PRINT

              Volume 605 U. S. Part 2
                             Pages 395–421




       OFFICIAL REPORTS
                                     OF


   THE SUPREME COURT
                                June 12, 2025


Page Proof Pending Publication


                    REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D. C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                         OCTOBER TERM, 2024                              395

                                  Syllabus


   MARTIN, individually and as parent and next
    friend of G. W., a minor, et al. v. UNITED
                  STATES et al.
certiorari to the united states court of appeals for
                the eleventh circuit
       No. 24–362. Argued April 29, 2025—Decided June 12, 2025
On October 18, 2017, the FBI raided the wrong house in suburban Atlanta.
  Offcers meant to execute search and arrest warrants at a suspected
  gang hideout at 3741 Landau Lane but instead stormed 3756 Denville
  Trace, a quiet family home occupied by petitioners Hilliard Toi Cliatt,
  his partner Curtrina Martin, and her 7-year-old son. A six-member
  SWAT team breached the front door, detonated a fash-bang grenade,
  and assaulted the innocent occupants before realizing their mistake.
  The cause of the error was Special Agent Guerra's reliance on a personal
  GPS device, combined with the team's failure to notice the street sign
  for “Denville Trace” and the house number visible on the mailbox. Left
  with personal injuries and property damage, petitioners sued the United
Page Proof Pending Publication
  States under the Federal Tort Claims Act (FTCA), 28 U. S. C. § 2671
  et seq., seeking damages resulting from the offcers' alleged negligent
  and intentional actions during the raid. The district court granted
  summary judgment to the government. The Eleventh Circuit affrmed,
  applying a unique approach to FTCA claims.
The FTCA waives the federal government's sovereign immunity from suit
  as to certain torts committed by federal employees acting within the
  scope of their employment. But that waiver is subject to statutory ex-
  ceptions, including two relevant to a law enforcement misconduct case
  like this one. The frst is the intentional-tort exception in § 2680(h),
  which bars claims against the government for 11 enumerated intentional
  torts. The second is the discretionary-function exception in § 2680(a),
  which bars claims against the government that are based on an offcial's
  exercise of discretionary functions. Section 2680(h) also contains a
  “law enforcement proviso” which countermands the intentional-tort ex-
  ception, allowing suits for six specifed torts (including assault, battery,
  false imprisonment, and false arrest) to proceed against the United
  States when the torts are committed by “investigative or law enforce-
  ment offcers.” While most courts hold that the law enforcement pro-
  viso applies only to the intentional-tort exception, the Eleventh Circuit's
  approach is different in two key respects. First, the Eleventh Circuit
  alone holds that the proviso overrides all exceptions in § 2680, including
396                  MARTIN v. UNITED STATES

                                  Syllabus

  the discretionary-function exception, meaning that intentional-tort
  claims covered by the proviso automatically proceed to the merits with-
  out further analysis of other applicable § 2680 exceptions. Second, to
  compensate for this plaintiff-friendly approach, the Eleventh Circuit
  permits the government to assert a restrictive Supremacy Clause de-
  fense at the liability stage, allowing the government to escape liability
  when an offcer's actions have “some nexus with furthering federal pol-
  icy” and reasonably “compl[y] with the full range of federal law.” Den-
  son v. United States, 574 F. 3d 1318, 1348.
     Applying its distinctive approach, the Eleventh Circuit held that the
  law enforcement proviso protected petitioners' intentional-tort claims
  from both the intentional-tort and discretionary-function exceptions.
  The court dismissed petitioners' negligence claims under the
  discretionary-function exception, reasoning that Special Agent Guerra
  enjoyed discretion in preparing for the warrant execution. On the mer-
  its of the remaining intentional-tort claims, the court found the gov-
  ernment had a valid Supremacy Clause defense and granted summary
  judgment for the United States.
Held:
    1. The law enforcement proviso in § 2680(h) overrides only the
Page Proof Pending Publication
 intentional-tort exception in that subsection, not the discretionary-
 function exception or other exceptions throughout § 2680. Pp. 403–408.
      (a) The text and structure of § 2680 demonstrate that the law en-
 forcement proviso applies only to the intentional-tort exception. The
 proviso appears within the same subsection and sentence as the
 intentional-tort exception, refecting the established principle that stat-
 utory provisos generally modify only the provisions in which they ap-
 pear. Section 2680 contains 13 discrete exceptions. Coupled with the
 lead-in clause, each exception forms a separate sentence and operates
 as a structurally distinct provision. The proviso addresses the same
 subject matter as subsection (h)—intentional torts—while other excep-
 tions cover entirely different topics like lost mail, combat injuries, and
 quarantine impositions. Further, the proviso's defnitional sentence ex-
 pressly limits the defnition of “investigative or law enforcement offcer”
 to “this subsection” (i. e., subsection (h)), even though the phrase “law
 enforcement offcer” appears elsewhere in § 2680. Congress's choice to
 embed the proviso within subsection (h) rather than place it at the end
 of the full list of exceptions, as it sometimes does with broadly applicable
 provisos, further confrms the proviso's limited application to subsection
 (h) alone. Pp. 404–407.
      (b) Petitioners' arguments for broader application of the proviso
 are unpersuasive. While the proviso mirrors the language of § 2680's
                      Cite as: 605 U. S. 395 (2025)                      397

                                 Syllabus

 lead-in clause by stating that § 1346(b) “shall apply” rather than “shall
 not apply,” this textual similarity does not demonstrate that the proviso
 applies to all exceptions, which form discrete instructions that may be
 understood completely without reference to other provisions. The ab-
 sence of limiting language in the proviso's frst sentence does not expand
 its scope beyond subsection (h), as Congress accomplished that limita-
 tion through the proviso's placement within the same sentence as the
 intentional-tort exception. Legislative history suggesting Congress in-
 tended to address wrong-house raids broadly cannot displace what the
 law's terms clearly direct, as legislative history is not the law and Mem-
 bers of Congress may have had multiple purposes in mind when crafting
 the proviso. Pp. 407–408.
    2. The Supremacy Clause does not afford the United States a defense
 in FTCA suits. The FTCA is the “supreme” federal law governing
 the United States' tort liability and serves as the exclusive remedy for
 damages claims arising from federal employees' offcial conduct. The
 statute generally makes the government liable under state law on the
 same terms as a private individual would be liable under the law of the
 place where the tortious conduct occurred. Because the FTCA incor-
 porates state law as the liability standard, there is typically no confict
 between federal and state law for the Supremacy Clause to resolve.
Page Proof Pending Publication
 While federal law may sometimes displace state law in FTCA suits
 where a constitutional text or federal statute supplies controlling liabil-
 ity rules, the Eleventh Circuit identifed no such federal statute or con-
 stitutional provision displacing Georgia tort law in this case. The
 court's reliance on In re Neagle, 135 U. S. 1, is misplaced, as that 19th-
 century decision involved a federal offcer's immunity from state crimi-
 nal prosecution for acts necessary and proper in discharging federal
 duties, not the federal government's liability under a statute that ex-
 pressly subjects it to state tort law on the same terms as private parties.
 Section 2674 specifes the defenses available to the government, includ-
 ing judicial or legislative immunity and other defenses to which the
 United States is entitled, but these do not include the Eleventh Circuit's
 novel Supremacy Clause defense. Pp. 409–413.
    3. On remand, the Eleventh Circuit should consider whether subsec-
 tion (a)'s discretionary-function exception bars either the plaintiffs' neg-
 ligent- or intentional-tort claims—undertaking that assessment without
 reference to the mistaken view that the law enforcement proviso applies
 to subsection (a). The court must then ask of any surviving claims
 whether, under Georgia state law, a “private individual under like cir-
 cumstances” would be liable for the acts and omissions the plaintiffs
 allege, subject to the defenses discussed in § 2674—not a Supremacy
 Clause defense.
398                  MARTIN v. UNITED STATES

                          Opinion of the Court

     Remaining questions surrounding whether and under what circum-
  stances the discretionary-function exception may ever foreclose a suit
  like this one lie well beyond the two questions the Court granted certio-
  rari to address, and their resolution would beneft from the Eleventh
  Circuit's careful reexamination of this case in the first instance.
  Pp. 413–415.
Vacated and remanded.

   Gorsuch, J., delivered the opinion for a unanimous Court. Soto-
mayor, J., fled a concurring opinion, in which Jackson, J., joined, post,
p. 415.

  Patrick Jaicomo argued the cause for petitioners. With
him on the briefs were Anya Bidwell and Jared McClain.
  Frederick Liu argued the cause for respondents. With
him on the brief were Acting Solicitor General Harris, Act-
ing Assistant Attorney General Roth, Deputy Solicitor Gen-
eral Kneedler, and Joshua M. Salzman.
  Christopher Mills, by invitation of the Court, 604 U. S.
Page Proof Pending Publication
1115, argued the cause and fled a brief as amicus curiae in
support of the judgment below on Question 1.*

  Justice Gorsuch delivered the opinion of the Court.
  If federal offcers raid the wrong house, causing property
damage and assaulting innocent occupants, may the home-
owners sue the government for damages? The answer is

  *Briefs of amici curiae urging reversal were fled for America's Future
et al. by William J. Olson, Jeremiah L. Morgan, Robert J. Olson, and
Jeffrey C. Tuomala; for the Constitutional Accountability Center by Eliz-
abeth B. Wydra and Brianne J. Gorod; for Members of Congress by Jona-
than C. Bond, Jeff Liu, and Lavi M. Ben Dor; for the National Police
Accountability Project et al. by Charles A. Rothfeld, Paul W. Hughes,
Eugene R. Fidell, and John W. Whitehead; for the New Civil Liberties
Alliance by Casey Norman, Jenin Younes, and Mark Chenoweth; for the
North Central Pennsylvania Trial Lawyers Association by Paul Koster;
for Public Accountability et al. by Athul K. Acharya, Clark M. Neily III,
Cecillia D. Wang, Brett M. Kaufman, Scott Michelman, and Cory Isaac-
son; for Public Citizen by Scott L. Nelson and Allison M. Zieve; and for
Gregory C. Sisk by Geoffrey M. Pipoly and Matthew Stanford.
                  Cite as: 605 U. S. 395 (2025)           399

                     Opinion of the Court

not as obvious as it might be. All agree that the Federal
Tort Claims Act permits some suits for wrong-house raids.
But the scope of the Act's permission is much less clear.
This case poses two questions about the Act's application:
one concerning the FTCA's sovereign-immunity waiver, and
the other touching on the defenses the United States may
assert.
                            I
                               A
   In the predawn hours of October 18, 2017, the Federal Bu-
reau of Investigation raided the wrong house in suburban
Atlanta. Offcers meant to execute search and arrest war-
rants at a suspected gang hideout, 3741 Landau Lane. In-
stead, they stormed a quiet family home, 3756 Denville
Trace, occupied by Hilliard Toi Cliatt, his partner Curtrina
Martin, and her 7-year-old son G. W. App. to Pet. for Cert.
3a–4a.
Page Proof Pending Publication
   A six-member SWAT team, led by FBI Special Agent
Lawrence Guerra, breached the front door and detonated a
fash-bang grenade. Id., at 7a–8a. Fearing a home inva-
sion, Mr. Cliatt and Ms. Martin hid in a bedroom closet. Id.,
at 8a. But the SWAT team soon found the couple's hiding
spot, dragged Mr. Cliatt from the closet, “threw [him] down
on the foor,” handcuffed him, and began “bombarding [him]
with . . . questions.” Id., at 79a. Meanwhile, another off-
cer trained his weapon on Ms. Martin, who was lying on the
foor half-naked, having fallen inside the closet. Id., at 8a,
89a. Only then did another offcer stumble across some mail
with the home's address on it and realize the team had the
wrong house. Id., at 8a.
   The cause of the offcers' mistake? In preparation for the
raid, Agent Guerra visited the correct house to document its
features and identify a staging area for the SWAT team.
Id., at 5a. But, he says, when he used his personal GPS to
navigate to 3741 Landau Lane on the day of the raid, it led
400               MARTIN v. UNITED STATES

                       Opinion of the Court

him to 3756 Denville Trace. 631 F. Supp. 3d 1281, 1287 (ND
Ga. 2022). No one could confrm as much later because
Agent Guerra “threw . . . away” his GPS device “not long
after” the raid. Id., at 1288. And it seems the agents no-
ticed neither the street sign for “Denville Trace” nor the
house number, which was visible on the mailbox at the end
of the driveway. Ibid.; Tr. of Oral Arg. 38. Apparently,
too, Agent Guerra failed to appreciate that a different car
was parked in the driveway, one “not present . . . during [his]
previous visit.” 631 F. Supp. 3d, at 1288.
   Left with personal injuries and property damage—but few
explanations and no compensation—Mr. Cliatt and Ms. Mar-
tin sued the United States. They did so under the Federal
Tort Claims Act, 28 U. S. C. § 2671 et seq., alleging that the
offcers had committed various negligent and intentional
torts, App. 8–14.
                               B

Page       Proof
  After discovery  andPending
                        motions practice, Publication
                                            the district court
rejected each of the plaintiffs' claims and granted summary
judgment to the government. The Eleventh Circuit af-
frmed and, in doing so, relied on an understanding of the
FTCA that no other circuit has adopted. To appreciate
what sets the Eleventh Circuit apart and how its approach
affected its analysis of the plaintiffs' claims, it helps to begin
by outlining how this suit would have proceeded elsewhere.
   The FTCA allows those injured by federal employees to
sue the United States for damages. The statute achieves
that end by waiving, in 28 U. S. C. § 1346(b), the federal gov-
ernment's sovereign immunity for “certain torts committed
by federal employees acting within the scope of their
employment.” Brownback v. King, 592 U. S. 209, 212
(2021) (internal quotation marks omitted). But the statute's
waiver is subject to 13 exceptions that claw back the govern-
ment's immunity in certain circumstances. Set out in § 2680,
most of these 13 exceptions are obviously inapplicable to
suits alleging police misconduct within the United States.
                    Cite as: 605 U. S. 395 (2025)             401

                       Opinion of the Court

But two in particular—the discretionary-function exception
and the intentional-tort exception—sometimes come into
play.
   In a suit like this one, most courts begin by assessing the
intentional-tort exception. Located in subsection (h) of
§ 2680, it prohibits claims alleging any of 11 enumerated
torts. But the exception is itself subject to a “law enforce-
ment proviso.” Millbrook v. United States, 569 U. S. 50, 55
(2013). That proviso countermands the exception with re-
spect to six intentional torts (including assault, battery, false
imprisonment, and false arrest) by “investigative or law en-
forcement offcers.” § 2680(h). So if a plaintiff alleges that
a federal law enforcement offcer committed one or more of
those six torts, the proviso will ensure those claims survive
an encounter with the intentional-tort exception. Id., at
55–56.
   Next, most courts turn to the discretionary-function ex-
Page Proof Pending Publication
ception. Housed in subsection (a) of § 2680, this exception
bars “[a]ny claim” based on the exercise of an offcial's “dis-
cretionary function.” Faced with that instruction, most
courts ask whether the exception precludes any of the plain-
tiff's remaining tort claims. And here, the answer is often
less clear cut. The discretionary-function exception, this
Court has said, forbids suits challenging decisions that “in-
volv[e] an element of judgment or choice” of a “kind that
the . . . exception was designed to shield.” United States v.
Gaubert, 499 U. S. 315, 322–323 (1991) (alteration in original;
internal quotation marks omitted). But several of our lower
court colleagues report that they have “struggl[ed]” to dis-
cern what this direction requires of them. See, e. g., Xi v.
Haugen, 68 F. 4th 824, 842 (CA3 2023) (Bibas, J., concurring).
So, for example, some lower courts have held that the
discretionary-function exception does not shield “careless” or
“unconstitutional” police conduct from judicial scrutiny, but
others have taken a contrary view and read the exception
much more broadly. Id., at 843; Pet. for Cert. 28–34.
402              MARTIN v. UNITED STATES

                      Opinion of the Court

   Finally, if any of the plaintiff 's claims survive the
discretionary-function exception and thus fall within the
FTCA's waiver of sovereign immunity, courts turn to a third
question: Is the government liable to the plaintiff on the mer-
its? When it comes to that question, the FTCA provides that
the government will usually be liable to the plaintiff if a
“private individual under like circumstances,” § 2674, would
be liable under “the law of the place” where the government
employee's wrongful “act or omission occurred,” § 1346(b)(1).
Ordinarily, then, courts will fnd for the plaintiff if he can
demonstrate that federal offcials committed a tort under ap-
plicable state law. See Brownback, 592 U. S., at 218.
   Now compare that approach to the Eleventh Circuit's.
That court begins much as others do, asking whether the
law enforcement proviso permits a plaintiff's intentional-tort
claims to advance past subsection (h)'s intentional-tort ex-
ception. See Nguyen v. United States, 556 F. 3d 1244, 1260
Page Proof Pending Publication
(2009).
   But from there, the Eleventh Circuit proceeds quite differ-
ently. Rather than asking whether the discretionary-
function exception bars either the plaintiff's negligent-tort
claims or his intentional-tort claims, as most courts do, the
Eleventh Circuit applies that exception only to the plaintiff's
negligence claims. The Eleventh Circuit does so because, in
its view, the law enforcement proviso does not just override
the intentional-tort exception, it also overrides all the other
exceptions in § 2680, the discretionary-function exception in-
cluded. Id., at 1257. Under that approach, any intentional-
tort claim covered by the proviso automatically proceeds to
the merits—no matter what any other exception has to say.
   To compensate for its expansive and plaintiff-friendly
reading of the proviso, the Eleventh Circuit then takes a re-
strictive and defendant-friendly view at the FTCA's liability
stage. In other courts, an FTCA plaintiff will usually pre-
vail if he can show a “private individual under like circum-
stances,” § 2674, would be liable under “the law of the place”
                    Cite as: 605 U. S. 395 (2025)             403

                       Opinion of the Court

where the government employee's wrongful “act or omission
occurred,” § 1346(b)(1). But in the Eleventh Circuit, the
government may assert a particular affrmative defense
under the Constitution's Supremacy Clause. See Denson v.
United States, 574 F. 3d 1318, 1347 (2009). And that de-
fense, the Eleventh Circuit holds, defeats a claim whenever a
law enforcement offcer's contested actions bear “some nexus
with furthering federal policy and can reasonably be charac-
terized as complying with the full range of federal law.” Id.,
at 1348; accord, Kordash v. United States, 51 F. 4th 1289,
1293 (CA11 2022).
   Applying its unique approach to this case, the Eleventh
Circuit held that the law enforcement proviso spared the
plaintiffs' intentional-tort claims from both the intentional-
tort and the discretionary-function exceptions. It dismissed
the plaintiffs' negligence claims under the discretionary-
function exception because, in its view, Agent Guerra “en-
joyed discretion in how he prepared for the warrant execu-
Page Proof Pending Publication
tion.” App. to Pet. for Cert. 17a–18a. And on the merits
of the plaintiffs' (remaining) intentional-tort claims, the court
held that the government had a winning Supremacy Clause
defense. As a result, the Eleventh Circuit concluded, the
United States was entitled to summary judgment. Id., at
18a–19a.
   We agreed to take this case to examine the distinctive
features of the Eleventh Circuit's approach—namely (1)
whether the law enforcement proviso overrides not just the
intentional-tort exception but also the discretionary-function
exception, and (2) whether the Supremacy Clause affords the
United States a defense in FTCA suits. Pet. for Cert. 16,
25. 604 U. S. 1103 (2025).
                                II
  Begin with the law enforcement proviso. Does it counter-
mand only § 2680(h)'s intentional-tort exception, as most cir-
cuits have concluded and the government argues? Brief for
Respondents 25; Xi, 68 F. 4th, at 842 (Bibas, J., concurring)
404                MARTIN v. UNITED STATES

                        Opinion of the Court

(collecting cases). Or does the proviso also override the
other exceptions in § 2680, including the discretionary-
function exception in subsection (a), as the Eleventh Circuit
has held and the plaintiffs contend? Nguyen, 556 F. 3d, at
1257; Brief for Petitioners 40.

                                A
   To answer that question, we turn to the relevant statutory
text. Recall that § 1346(b) waives the federal government's
sovereign immunity, subject to a list of 13 exceptions housed
in § 2680. Those exceptions are lettered (a) through (n),
with one letter unused. Rather than setting the law en-
forcement proviso apart as a discrete provision at the end of
that list, Congress folded it into subsection (h)'s intentional-
tort exception. Here's a sense of how the proviso (under-
lined below) appears in context.
         “The provisions of this chapter and section 1346(b) of
Page Proof Pending Publication
      this title shall not apply to—
         “(a) Any claim based upon an act or omission of an
      employee of the Government, exercising due care, in the
      execution of a statute or regulation, whether or not such
      statute or regulation be valid, or based upon the exer-
      cise or performance or the failure to exercise or perform
      a discretionary function or duty on the part of a federal
      agency or an employee of the Government, whether or
      not the discretion involved be abused.
      .              .             .             .              .
         “(h) Any claim arising out of assault, battery, false im-
      prisonment, false arrest, malicious prosecution, abuse of
      process, libel, slander, misrepresentation, deceit, or in-
      terference with contract rights: Provided, That, with re-
      gard to acts or omissions of investigative or law enforce-
      ment offcers of the United States Government, the
      provisions of this chapter and section 1346(b) of this title
      shall apply to any claim arising, on or after the date of
      the enactment of this proviso, out of assault, battery,
                   Cite as: 605 U. S. 395 (2025)            405

                      Opinion of the Court

    false imprisonment, false arrest, abuse of process, or ma-
    licious prosecution. For the purpose of this subsection,
    `investigative or law enforcement offcer' means any of-
    fcer of the United States who is empowered by law to
    execute searches, to seize evidence, or to make arrests
    for violations of Federal law.
.               .              .              .              .
       “(n) Any claim arising from the activities of a Federal
    land bank, a Federal intermediate credit bank, or a bank
    for cooperatives.”
   The proviso's placement supplies an immediate clue about
the scope of its application. It appears in the same subsec-
tion (and the same sentence) as the intentional-tort excep-
tion. Given that arrangement, an ordinary reader would
naturally presume that the proviso modifes only subsection
(h). An everyday example helps illustrate the point. Sup-
pose a wife leaves her husband a shopping list: “Please buy—
Page Proof Pending Publication
Apples. Carrots. Steak: If there is a sale. Bread. Milk.”
The wife, we think, would be understandably frustrated if
her husband returned home with only steak in hand because
he could fnd nothing else discounted. Refecting that intu-
ition about ordinary meaning, our cases recognize that, ab-
sent reason to think otherwise, statutory provisos generally
modify only the provisions in which they sit. See McDon-
ald v. United States, 279 U. S. 12, 20–21 (1929); Alaska v.
United States, 545 U. S. 75, 106 (2005); A. Scalia & B. Garner,
Reading Law 154–155 (2012) (Scalia & Garner).
   Nothing about § 2680(h)'s proviso gives us reason to think
it works differently. To the contrary, one textual clue after
another confrms that it follows the general rule. Start with
the statute's grammatical structure. Section 2680 contains
a lead-in clause (“The provisions of this chapter and section
1346(b) of this title shall not apply to—”) followed by a list
of exceptions. In conjunction with the lead-in clause, each
exception forms a stand-alone sentence ending with a period,
operating as a “distinct,” “structurally discrete” provision.
406               MARTIN v. UNITED STATES

                       Opinion of the Court

Jama v. Immigration and Customs Enforcement, 543 U. S.
335, 344, and n. 4 (2005). And, given that, it is hard to see
how the law enforcement proviso might apply beyond sub-
section (h), modifying exceptions housed in separate subsec-
tions (and separate sentences) elsewhere in § 2680.
   Notice, too, that subsection (h) and its proviso work to-
gether to address the same category of claims: intentional
torts. Subsection (h)'s intentional-tort exception excludes
from the FTCA's sovereign-immunity waiver claims for torts
like “assault, battery, false imprisonment, [and] false arrest.”
The proviso then undoes that assertion of sovereign immu-
nity for some of those same torts when committed by “inves-
tigative or law enforcement offcers.” By contrast, the pro-
viso does not so much as mention the issues addressed by
§ 2680's other exceptions, like claims for lost mail, combat
injuries, or the imposition of quarantines. § 2680(b), (f), ( j).
That the proviso is “confned” to the same “subject-matter”
Page Proof Pending Publication
as subsection (h)'s “principal clause” stands as more evidence
yet that it “refers only to the provision to which it is
attached.” United States v. Morrow, 266 U. S. 531, 535
(1925).
   The proviso's second sentence is telling as well. It defnes
the phrase “investigative or law enforcement offcer.” In
doing so, the sentence tells us that the defnition applies only
to “this subsection” (i. e., subsection (h)), even though the
phrase “law enforcement offcer” also appears in subsection
(c)'s exception for claims arising from tax and customs collec-
tion. § 2680(c), (h). If Congress had wished the proviso to
modify each of the exceptions in § 2680, it might have pro-
vided a section-wide defnition, rather than a limited defni-
tion just for subsection (h).
   If more evidence were needed, comparing this statute with
others would supply it. Often, Congress drafts statutory
lists followed by a proviso in a separate paragraph at the
end. See, e. g., 42 U. S. C. §§ 1383(a)(2)(F)(ii)(II), 6928(f)(2).
Sometimes, that placement can suggest that a proviso relates
                   Cite as: 605 U. S. 395 (2025)             407

                      Opinion of the Court

to all the preceding subparts, not just the nearest one.
Scalia & Garner 156. But here Congress chose a different
course, folding the proviso into a single exception, rather
than appending it to the end of the full list of exceptions.
And that choice, too, suggests this proviso applies to subsec-
tion (h) alone. See Ysleta del Sur Pueblo v. Texas, 596 U. S.
685, 704 (2022).
                              B
   Seeking to defend the Eleventh Circuit's view that the
proviso applies broadly across all of § 2680's exceptions, the
plaintiffs offer a number of thoughtful arguments. But, to
our eyes, none can overcome the textual evidence we have
just laid out.
   First, the plaintiffs ask us to focus on how the proviso mir-
rors § 2680's lead-in clause. Brief for Petitioners 42. The
lead-in clause, they observe, preserves the government's sov-
ereign immunity by instructing that § 1346(b)'s waiver “shall
Page Proof Pending Publication
not apply to” claims covered by the exceptions. § 2680 (em-
phasis added). Meanwhile, the proviso countermands that
direction by instructing that § 1346(b)'s waiver “shall apply”
to certain claims. § 2680(h) (emphasis added). Because the
language of the proviso mirrors the language of the lead-in
clause, the plaintiffs submit, Congress must have meant for
the proviso to have the last word with respect to each of the
FTCA's exceptions. Id., at 42. That conclusion, however,
does not follow from its premise. Yes, the proviso and lead-
in clause contain similar language. And, yes, the proviso
surely countermands the lead-in clause for purposes of sub-
section (h). But none of that means the proviso speaks to
other exceptions that work together with the lead-in lan-
guage to form discrete instructions that “may be understood
completely without reading any further.” Jama, 543 U. S.,
at 344.
   Second, the plaintiffs remind us that the proviso's second,
defnitional sentence applies to “this subsection,” but the
proviso's frst, substantive part contains no such limiting lan-
408               MARTIN v. UNITED STATES

                      Opinion of the Court

guage. Brief for Petitioners 42–43 (quoting § 2680(h)).
And that difference, the plaintiffs say, suggests that the frst,
substantive part applies throughout § 2680. Id., at 42–43.
Again, however, we do not see it. Congress had no need to
include similar limiting language in the frst part of the pro-
viso to confne its application to subsection (h). Congress
accomplished just that by placing the proviso's frst part in
the same sentence as the intentional-tort exception. Mean-
while, in the proviso's second sentence, Congress arguably
needed to confne the defnition of “investigative or law en-
forcement offcer” to “this subsection” to ensure that the
phrase “law enforcement offcer” carries a different meaning
when it appears in subsection (c).
   Third, the plaintiffs resort to legislative history. They
point to a committee report discussing how Congress
enacted the proviso in response to two wrong-house raids
much like their own. Id., at 8–10, 44; see S. Rep. No. 93–
Page Proof Pending Publication
588, p. 3 (1973). And, the plaintiffs argue, unless the proviso
is given broad effect across § 2680, it will not fulfll Con-
gress's purpose of ensuring that wrong-house-raid cases may
proceed. But this argument stumbles, too. Few pieces of
legislation pursue any single “purpos[e] at all costs.” Amer-
ican Express Co. v. Italian Colors Restaurant, 570 U. S. 228,
234 (2013) (internal quotation marks omitted). And Mem-
bers of Congress may well have had more than one purpose
in mind when adding the proviso to the FTCA. Perhaps
some thought amending subsection (h) alone and leaving oth-
ers untouched would strike a suitable balance between im-
munity and liability. Perhaps others concluded there was no
need to apply the proviso more broadly because no other
exception would shield the government from liability for
wrong-house raids. Whatever the reason, no amount of
guesswork about the purposes behind legislation can displace
what the law's terms clearly direct. “[L]egislative history
is not the law.” Epic Systems Corp. v. Lewis, 584 U. S. 497,
523 (2018).
                   Cite as: 605 U. S. 395 (2025)            409

                      Opinion of the Court

                               III
   That takes us to the Eleventh Circuit's second outlier posi-
tion and the second question presented. May the United
States defeat an FTCA suit by invoking the Supremacy
Clause and showing that a federal offcer's acts had “some
nexus with furthering federal policy” and “compl[ied] with
the full range of federal law”? App. to Pet. for Cert. 17a
(internal quotation marks omitted). Because the govern-
ment now concedes that it enjoys no such defense, the Court
appointed Christopher Mills as amicus to represent the
Eleventh Circuit's views. 604 U. S. 1115 (2025). He has
ably discharged his responsibilities. But in the end, we fnd
the government's concession commendable and correct: The
FTCA does not permit the Eleventh Circuit's Supremacy
Clause defense.
   The Supremacy Clause supplies a rule of decision when
federal and state laws confict. It provides that the “Consti-
Page Proof Pending Publication
tution, and the Laws of the United States which shall be
made in Pursuance thereof . . . shall be the supreme Law of
the Land . . . any Thing in the Constitution or Laws of any
state to the Contrary notwithstanding.” Art. VI, cl. 2. So,
for example, when a regulated party cannot comply with
both federal and state directives, the Supremacy Clause tells
us the state law must yield. See, e. g., Virginia Uranium,
Inc. v. Warren, 587 U. S. 761, 767 (2019) (opinion of Gor-
such, J.).
   The FTCA is the “supreme” federal law addressing the
United States' liability for torts committed by its agents. It
supplies the “exclusive remedy” for damages claims arising
out of federal employees' offcial conduct. See Hui v. Cas-
taneda, 599 U. S. 799, 806 (2010). And, as we have seen, the
government will usually be liable if a “private individual
under like circumstances,” § 2674, “would be liable to the
claimant in accordance with the law of the place where the
act or omission occurred,” § 1346(b)(1). Accordingly, a plain-
tiff may generally prevail in an FTCA suit by demonstrating
410               MARTIN v. UNITED STATES

                       Opinion of the Court

that “the State in which the alleged misconduct occurred
would permit a cause of action for that misconduct to go
forward.” Carlson v. Green, 446 U. S. 14, 23 (1980).
   Because the FTCA's liability rule incorporates state law,
in most cases there is no confict for the Supremacy Clause to
resolve. Take this case. Georgia law supplies the relevant
“law of the place” where the offcers' tortious conduct oc-
curred. § 1346(b)(1). And Georgia law would permit a
homeowner to sue a private person for damages if that per-
son intentionally or negligently raided his house and as-
saulted him. See App. 10–13 (citing Hendricks v. Southern
Bell Tel. & Tel. Co., 193 Ga. App. 264, 264–265, 387 S. E. 2d
593, 594–595 (1989), for assault and battery and Lyttle v.
United States, 867 F. Supp. 2d 1256, 1301 (MD Ga. 2012), for
negligence). So when the FTCA, the relevant federal law
in this feld, instructs courts to apply those same state rules
to decide whether the United States is liable to the plaintiffs,
there is no discord between the two.
Page Proof Pending Publication
   To be sure, it is possible (though rare) for federal and state
law to confict in an FTCA suit. So, for example, in Hess
v. United States, this Court held that federal maritime law
supplied the “law of the place” governing an FTCA suit in-
volving an accident on the Columbia River. 361 U. S. 314,
318, and n. 7 (1960). Though the accident “occurred within
the State of Oregon,” it happened “on navigable waters . . .
within the reach of admiralty jurisdiction.” Id., at 318. As
a result, federal maritime law displaced state tort law, just
as it would in “an action between private parties.” Ibid,
n. 7. In much the same way, federal law will control other
FTCA suits where “a litigant [can] point specifcally to a con-
stitutional text or a federal statute” that supplies controlling
liability rules, displacing contrary state law. Virginia Ura-
nium, 587 U. S., at 767 (internal quotation marks omitted);
see, e. g., PLIVA, Inc. v. Mensing, 564 U. S. 604, 618 (2011).
   In this case, however, the Eleventh Circuit did not identify
any federal statute or constitutional provision displacing
Georgia tort law. Instead, the court of appeals pointed to a
                      Cite as: 605 U. S. 395 (2025)                  411

                          Opinion of the Court

line of cases stemming from this Court's decision in In re
Neagle, 135 U. S. 1, 75 (1890). App. to Pet. for Cert. 16a–
17a (citing Denson, 574 F. 3d, at 1336–1337). Those cases,
the Eleventh Circuit has observed, hold that federal offcers
may sometimes defeat state prosecutions against them by
demonstrating that their actions, though criminal under
state law, were “necessary and proper” in the discharge of
their federal responsibilities. Id., at 1346–1347 (discussing
In re Neagle). In the Eleventh Circuit's view, that same
logic works to foreclose FTCA suits like the plaintiffs'. 574
F. 3d, at 1346–1347; Kordash, 51 F. 4th, at 1293–1294.
   To appreciate why that view is mistaken, a little history
helps. In re Neagle involved an affair, a homicide, and a
habeas petition. In 1883, Sarah Althea Hill claimed to be
the wife of U. S. Senator William Sharon and sought a share
of his fortune in acrimonious California divorce proceedings.
Sharon admitted an affair but insisted that Hill had forged
Page Proof Pending Publication
the pair's handwritten marriage contract. Hill hired David
Terry to represent her. A former Chief Justice of the Cali-
fornia Supreme Court, Terry had resigned that post after
killing (another) U. S. Senator in a duel. As the litigation
wore on, lawyer and client married.
   Eventually, the dispute between Hill and Sharon wound
up before U. S. Supreme Court Justice Stephen Field while
he was riding circuit. Terry and Justice Field were no
strangers, having served together on the California Supreme
Court. Even so, Justice Field issued a devastating ruling
against Hill. As he announced his decision, Hill leapt from
her seat, denounced the Justice as “bought,” and had to be
carried from the courtroom. Joining the fracas, Terry
punched a marshal and brandished a bowie knife. Even
after the couple spent time in jail for contempt, they contin-
ued to issue threats against Justice Field.1

  1
   For a full account of the saga, see In re Neagle, 135 U. S., at 42–55;
W. Lewis, The Supreme Court and a Six-Gun: The Extraordinary Story of
In re Neagle, 43 A. B. A. J. 415 (1957) (Lewis).
412              MARTIN v. UNITED STATES

                      Opinion of the Court

  Those events found their way into the U. S. Reports this
way. Aware of the threat Hill and Terry posed, the U. S.
Attorney General ordered Deputy Marshal David Neagle, a
former chief of police in Tombstone, Arizona, to accompany
Justice Field when he next rode circuit in California. Lewis
478; In re Neagle, 135 U. S., at 51–52. That decision proved
prescient, for Terry soon cornered the Justice on a train and
attacked him. Id., at 52–54. Intervening to protect the
Justice, Neagle shot and killed Terry. Ibid. After the
shooting, California authorities arrested Neagle and began
prosecuting him for murder. Neagle countered by fling a
petition for a writ of habeas corpus in federal court seeking
his release. Ibid.
  When Neagle's petition reached this Court, it agreed the
writ should issue, reasoning that the Supremacy Clause
shielded him from state criminal charges. Without some
such protection, the Court concluded, California could frus-
Page Proof Pending Publication
trate federal law by prosecuting a federal marshal “for an
act which he was authorized to do by the law of the United
States,” an act “which it was his duty to do,” and in circum-
stances where he “did no more than what was necessary and
proper.” Id., at 75–76.
  Memorable as In re Neagle may be, we do not see how it
informs the prosaic task of applying the FTCA. The Court's
decision may stand for the proposition that federal law will
sometimes preempt a state criminal law when it conficts
with a federal offcer's duties—and do so even in the absence
of express federal legislation overriding the state law in
question. But In re Neagle does not speak to a situation
where, as here, Congress has entered the feld and expressly
bound the federal government to accept liability under state
tort law on the same terms as a “private individual.” § 2674.
After all, no private individual could deploy In re Neagle to
his advantage. It has only ever worked to shield “[f]ederal
offcers who are discharging their duties.” Ohio v. Thomas,
173 U. S. 276, 283 (1899); see also In re Neagle, 135 U. S., at
                        Cite as: 605 U. S. 395 (2025)                       413

                            Opinion of the Court

62 (“offcers and agents . . . acting . . . within the scope of
their authority”); Davis v. Burke, 179 U. S. 399, 402 (1900)
(“an offcer of the United States [who] has been arrested
under state process for acts done under the authority of the
Federal government”).2
   To be sure, the government may raise other defenses
against tort liability, and some may be uniquely federal in
nature. After setting forth the general rule that the gov-
ernment can be held liable under state tort law on the same
terms as a “private individual,” § 2674 adds that the govern-
ment may “assert any defense based upon judicial or legisla-
tive immunity which otherwise would have been available to
the employee of the United States whose act or omission
gave rise to the claim, as well as any other defenses to which
the United States is entitled.” But none of these defenses
include In re Neagle. That decision did not recognize a “ju-
dicial or legislative immunity.” Nor has it been understood
Page Proof Pending Publication
as a “defens[e] to which the United States is entitled,” but
instead (and again) as a shield “[f]ederal offcers” may assert.
Thomas, 173 U. S., at 283. Had Congress wanted to refash-
ion In re Neagle into a new defense the government itself
can assert under the FTCA, it might have said so. Yet it
did not.
                              IV
  Where does all that leave the case before us? We can say
this much: The plaintiffs' intentional-tort claims survive

  2
    To date at least, this Court has also generally understood In re Neagle
as providing federal offcers a shield against only state criminal prosecu-
tion, not (as here) state tort liability. See, e. g., Thomas, 173 U. S., at 283–
285 (favorably citing In re Waite, a case holding that the defense would
permit “a civil action for damages,” even where it barred “a criminal
prosecution,” because a damages action, unlike a prosecution, would not
bring the “federal and state governments into confict,” 81 F. 359, 363–364
(ND Iowa 1897)); Johnson v. Maryland, 254 U. S. 51, 56 (1920) (suggesting
that the defense would not foreclose “liability under the common law of a
State” for “negligence”).
414               MARTIN v. UNITED STATES

                      Opinion of the Court

their encounter with subsection (h) thanks to the law en-
forcement proviso, as the Eleventh Circuit recognized. But
it remains for that court on remand to consider whether sub-
section (a)'s discretionary-function exception bars either the
plaintiffs' negligent- or intentional-tort claims. As we have
explained, the Eleventh Circuit must undertake that assess-
ment without reference to its mistaken view that the law
enforcement proviso applies to subsection (a). Should some
or all of the plaintiffs' claims survive the discretionary-
function exception, the Eleventh Circuit must then ask
whether, under Georgia state law, a “private individual
under like circumstances” would be liable for the acts and
omissions the plaintiffs allege, subject to the defenses dis-
cussed in § 2674—not a Supremacy Clause defense nowhere
mentioned there.
   Having resolved that much, the plaintiffs ask us to decide
more still. See Brief for Petitioners 19–40. In particular,
Page Proof Pending Publication
they call on us to determine whether and under what circum-
stances the discretionary-function exception bars suits for
wrong-house raids and similar misconduct. Unless we take
up that further question, they worry, the Eleventh Circuit
on remand may take too broad a view of the exception and
dismiss their claims again. After all, the plaintiffs observe,
in the past that court has suggested that the discretionary-
function exception bars any claim “unless a source of federal
law `specifcally prescribes' a course of conduct” and thus de-
prives an offcial of all discretion. Id., at 36 (quoting Shivers
v. United States, 1 F. 4th 924, 931 (CA11 2021)). And that
approach, the plaintiffs insist, is both seriously mistaken and
at odds with how other circuits understand the exception.
Brief for Petitioners 36. Some courts, for instance, have
held that the discretionary-function exception does not pro-
tect conduct “marked by individual carelessness or laziness,”
rather than “policy considerations.” Rich v. United States,
811 F. 3d 140, 147 (CA4 2015). Some courts do not apply the
exception when law enforcement offcers violate the plain-
                   Cite as: 605 U. S. 395 (2025)             415

                    Sotomayor, J., concurring

tiffs' constitutional rights. Xi, 68 F. 4th, at 839 (“govern-
ment offcials never have discretion to violate the Constitu-
tion”). And some have indicated that the exception does not
protect “ministerial” tasks. See id., at 843 (Bibas, J., con-
curring). The plaintiffs ask us to endorse decisions like
these, apply their reasoning to this case, and hold it survives
the discretionary-function exception. Brief for Petitioners
39–40.
   We readily acknowledge that different lower courts have
taken different views of the discretionary-function exception.
We acknowledge, too, that important questions surround
whether and under what circumstances that exception may
ever foreclose a suit like this one. But those questions lie
well beyond the two we granted certiorari to address. And
before addressing them, we would beneft from the Eleventh
Circuit's careful reexamination of this case in the frst in-
stance. It is work enough for the day to answer the ques-
tions we took this case to resolve, clear away the two faulty
Page Proof Pending Publication
assumptions on which that court has relied in the past, and
redirect it to the proper inquiry.
   The judgment of the Eleventh Circuit is vacated, and the
case is remanded for further proceedings consistent with
this opinion.
                                              It is so ordered.

  Justice Sotomayor, with whom Justice Jackson joins,
concurring.
  I join in full the Court's opinion, which holds that the Elev-
enth Circuit's distinctive approach to suits under the Federal
Tort Claims Act (FTCA) is wrong in two respects. See ante,
at 403–404, 413–414. The law enforcement proviso modifes
only the subsection in which it is located: Section 2680(h)'s
intentional-tort exception. Ante, at 403–408. The United
States, moreover, may not defeat an FTCA suit simply by
“showing that a federal offcer's acts had `some nexus with
furthering federal policy' and `compl[ied] with the full range
416              MARTIN v. UNITED STATES

                    Sotomayor, J., concurring

of federal law.' ” Ante, at 409 (alteration in original). With
those two principles clarifed, I also agree that the Eleventh
Circuit must now consider on remand whether the
FTCA's discretionary-function exception bars plaintiffs'
negligent- and intentional-tort claims. Ante, at 414–415. I
write separately to underscore that there is reason to think
the discretionary-function exception may not apply to these
claims.
                               I
   The FTCA shields the United States from liability for
claims “based upon” a federal employee's “exercise or per-
formance” (or failure to exercise or perform) “a discretionary
function or duty,” “whether or not the discretion involved be
abused.” 28 U. S. C. § 2680(a). This Court has set forth a
two-part test that governs the application of § 2680(a), known
as the discretionary-function exception. First, courts must
consider the nature of the offcial's conduct and decide
Page Proof Pending Publication
whether it “ `involv[es] an element of judgment or choice.' ”
United States v. Gaubert, 499 U. S. 315, 322 (1991) (quoting
Berkovitz v. United States, 486 U. S. 531, 536 (1988)). “The
requirement of judgment or choice,” this Court has ex-
plained, “is not satisfed if a `federal statute, regulation, or
policy specifcally prescribes a course of action for an em-
ployee to follow.' ” 499 U. S., at 322. In such circum-
stances, “ `the employee has no rightful option but to adhere
to the directive.' ” Ibid.
   Even where a federal employee retains an element of
choice, however, the exception does not apply refexively.
After all, it is rare for statutes or regulations to prescribe
an offcial's required course of conduct down to the very last
detail, so some degree of choice will almost invariably re-
main. Thus, this Court has required lower courts to deter-
mine, at the second step, whether “th[e] judgment is of the
kind that the discretionary function exception was designed
to shield.” Berkovitz, 486 U. S., at 536. Because “[t]he
basis for the discretionary function exception was Congress'
                   Cite as: 605 U. S. 395 (2025)             417

                    Sotomayor, J., concurring

desire to `prevent judicial “second-guessing” of legislative
and administrative decisions grounded in social, economic,
and political policy through the medium of an action in tort,' ”
this Court has clarifed that the exception protects only those
governmental actions and decisions that are themselves
“based on considerations of public policy.” Id., at 536–537
(quoting United States v. S. A. Empresa De Viacao Aerea
Rio Grandense, 467 U. S. 797, 814 (1984)); see Gaubert, 499
U. S., at 323.
   To that end, this Court has said, it is “obviou[s]” that some
discretionary acts performed by Government agents “are
within the scope of [their] employment but not within the
discretionary function exception.” Id., at 325, n. 7. If a
federal banking regulator “drove an automobile on a mission
connected with his offcial duties and negligently collided
with another car,” for example, the Court has made clear
that “the exception would not apply.” Ibid. That is be-
Page Proof Pending Publication
cause, while “driving requires the constant exercise of dis-
cretion, the offcial's decisions in exercising that discretion
can hardly be said to be grounded in regulatory policy.”
Ibid.
   It has been 34 years since this Court last weighed in on
the discretionary-function exception, see Gaubert, 499 U. S.
315, and despite substantial percolation in the courts of ap-
peals, the “exact boundaries of the exception remain un-
clear,” 14 C. Wright, A. Miller, & H. Hershkoff, Federal Prac-
tice and Procedure § 3658.1 (4th ed. Supp. 2025). The Court
today resolves one of the Circuit splits regarding the excep-
tion's application: whether claims that fall within the FTCA's
law enforcement proviso must necessarily fall outside of the
discretionary-function exception. Yet, as the Court recog-
nizes, ante, at 414–415, several additional points of disagree-
ment remain, including whether allegedly “unconstitutional
conduct necessarily falls outside the exception” because off-
cials lack discretion to violate the Constitution, and “whether
the exception applies when the challenged act was careless
418               MARTIN v. UNITED STATES

                     Sotomayor, J., concurring

rather than a considered exercise of discretion.” Xi v.
Haugen, 68 F. 4th 824, 843 (CA3 2023) (Bibas, J., concurring)
(describing these Circuit splits). Given the enduring ques-
tions about how to apply the discretionary-function excep-
tion, and the divergent approaches taken by the Circuits, it
is long past time for this Court to weigh in on the excep-
tion's scope.
   Even without further intervention by this Court, however,
there is reason to question the Eleventh Circuit's suggestion
in the decision below that the discretionary-function excep-
tion might apply “ `unless a source of federal law “specifcally
prescribes” a [federal employee's] course of conduct.' ” 2024
WL 1716235, *6 (2024) (quoting Shivers v. United States, 1
F. 4th 924, 931 (CA11 2021); emphasis in original). That ap-
proach, which even the Government does not defend before
this Court, would run headlong into this Court's precedents.
Gaubert, after all, applies the discretionary-function excep-
tion only where an offcial's actions both involve an element
Page Proof Pending Publication
of judgment and rely on public policy considerations. See
499 U. S., at 322–323; see also Berkovitz, 486 U. S., at 536–
537. Whether federal law prescribes a particular course of
action resolves only the frst of Gaubert's two questions.
The second question (whether an offcer's decisions were
“ `based on considerations of public policy,' ” 499 U. S., at 323)
remains live. Were it otherwise, a federal offcial's negli-
gent driving decisions would fall beyond the reach of the
discretionary-function exception only if federal law or policy
specifcally prescribed an offcer's permissible maneuvers on
the road. Cf. id., at 325, n. 7.

                                II
  Agent Guerra's preparation to execute search and arrest
warrants at 3741 Landau Lane, and his subsequent decision
to raid Martin and Cliatt's home at 3756 Denville Trace, bear
some resemblance to Gaubert's negligent driving hypotheti-
cal. Like driving, executing a warrant always involves
                   Cite as: 605 U. S. 395 (2025)           419

                   Sotomayor, J., concurring

some measure of discretion. Yet it is hard to see how Guer-
ra's conduct in this case, including his allegedly negligent
choice to use his personal GPS and his failure to check the
street sign or house number on the mailbox before breaking
down Martin's door and terrorizing the home's occupants, in-
volved the kind of policy judgments that the discretionary-
function exception was designed to protect.
   The FTCA's history, too, confrms Congress's intention to
subject the United States to liability for intentional torts
committed by law enforcement offcers like Agent Guerra.
The relevant context is as follows: For several decades after
the FTCA's enactment, Congress retained the United States'
sovereign immunity for myriad intentional torts committed
by federal employees, including assault, battery, and false
arrest. See 28 U. S. C. § 2680(h). That changed, however,
in response to an episode that will sound familiar to readers
of the majority opinion. See ante, at 399–400.
Page Proof Pending Publication
   In April 1973, Herbert and Evelyn Giglotto awoke in their
Collinsville, Illinois, townhouse “to the sound of someone
smashing down their door and bursting into their home.” J.
Boger, M. Gitenstein, & P. Verkuil, The Federal Tort Claims
Act Intentional Torts Amendment: An Interpretative Analy-
sis, 54 N. C. L. Rev. 497, 500 (1976). After 15 state and
federal offcers ransacked the Giglottos' home, tied them up
at gunpoint, and threatened to shoot Mr. Giglotto if he
moved, the offcers realized they “ `ha[d] the wrong people.' ”
Ibid. The offcers eventually moved on to the home of Don-
ald Askew, where they terrorized yet another innocent cou-
ple before confessing they had acted on a “ `bad tip.' ” Id.,
at 501.
   The Collinsville raids garnered national attention, includ-
ing from the United States Senate. See S. Rep. No. 93–588,
pp. 2–3 (1973); see also Brief for Members of Congress as
Amici Curiae 8–12. Noting that “[t]here [was] no effective
legal remedy against the Federal Government for the actual
physical damage, much less the pain, suffering and humilia-
420               MARTIN v. UNITED STATES

                    Sotomayor, J., concurring

tion to which the Collinsville families ha[d] been subjected,”
the Senate Committee on Government Operations proposed
an amendment to the FTCA. See S. Rep. No. 93–588, at 2.
The solution was to add a proviso to the end of the
intentional-tort exception that “deprive[s] the Federal Gov-
ernment of the defense of sovereign immunity” for FTCA
suits arising out of the state-law torts of “assault, battery,
false imprisonment, false arrest, malicious prosecution, or
abuse of process” by federal law enforcement offcers. Id.,
at 3; see § 2680(h). The Committee designed the proviso to
ensure “innocent individuals who are subjected to raids of
the type conducted in Collinsville, Illinois, will have a cause
of action against the individual Federal agents [via suits
under Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971)] and the Federal Government [through the
FTCA].” Id., at 3 (emphasis added).
   Of course, the majority correctly holds that the proviso
Page Proof Pending Publication
does not altogether trump the discretionary-function excep-
tion: Even if an intentional-tort claim “survive[s its] en-
counter with subsection (h) thanks to the law enforcement
proviso,” courts must nevertheless consider whether “sub-
section (a)'s discretionary-function exception bars . . . the
plaintiffs' negligent- or intentional-tort claims.” Ante, at
413–414. Courts, however, should not ignore the existence
of the law enforcement proviso, or the factual context that
inspired its passage, when construing the discretionary-func-
tion exception. Whatever else is true of that exception, any
interpretation should allow for liability in the very cases
Congress amended the FTCA to remedy. See Van Buren v.
United States, 593 U. S. 374, 393 (2021) (“ `When Congress
amends legislation, courts must presume it intends the
change to have real and substantial effect' ”); see also Hun-
gary v. Simon, 604 U. S. 115, 132 (2025) (relying on a statute's
“ `historical backdrop' ” to “ `permit adjudication of claims' ”
that an earlier decision of this Court had avoided).
                  Cite as: 605 U. S. 395 (2025)           421

                   Sotomayor, J., concurring

                        *      *      *
  On remand, the court should approach the discretionary-
function exception with an eye to both steps of the Gaubert
analysis and to the existence and context of the intentional-
tort exception's law enforcement proviso.




Page Proof Pending Publication
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
Page Proof Pending Publication
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

p. 401, line 11: “against” is changed to “by”
p. 419, line 20: “house” is changed to “home”

```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Buie.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Maryland v. Buie"
type: case
citation: "494 U.S. 325 (1990)"
parallel_cite: "110 S. Ct. 1093; 108 L. Ed. 2d 276"
neutral_cite: 1990 U.S. LEXIS 1176
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-03-05
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-03-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Buie
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112384/maryland-v-buie/"
  cluster_id: 112384
  opinion_id: 112384
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[Michigan v. Long]]", "[[Chimel v. California]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "protective-sweep", "officer-safety", "arrest-in-the-home"]
holding: "Protective sweep incident to an in-home arrest: (1) without probable cause or reasonable suspicion, officers may as a precaution look in…"
lake:
  record_id: Maryland v. Buie
  status: verified
  projected_at: 2026-07-09
---

# Maryland v. Buie

*494 U.S. 325 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police with arrest warrants for Buie and an accomplice for an armed robbery entered Buie's house and arrested him as he emerged from the basement. An officer then went down into the basement "in case there was someone else" there and, in plain view, seized a red running suit matching the robber's clothing. Buie sought to suppress the suit as the fruit of an unlawful search.

## Issue
What level of justification the Fourth Amendment requires for a "protective sweep" — a quick search of a house for dangerous persons — conducted incident to an in-home arrest.

## Rule
A two-tier rule. As to spaces right next to the arrest, no suspicion is required: "as an incident to the arrest the officers could, as a precautionary matter and without probable cause or reasonable suspicion, look in closets and other spaces immediately adjoining the place of arrest from which an attack could be immediately launched." — 494 U.S. at 334. ^pin-334

Beyond that, reasonable suspicion is required: "there must be articulable facts which, taken together with the rational inferences from those facts, would warrant a reasonably prudent officer in believing that the area to be swept harbors an individual posing a danger to those on the arrest scene." — *Id.* And the sweep's scope is limited: it "is nevertheless not a full search of the premises, but may extend only to a cursory inspection of those spaces where a person may be found." — [*Id.* at 335](https://www.courtlistener.com/opinion/112384/maryland-v-buie/#:~:text=there%20must%20be%20articulable%20facts). ^pin-335

## Application
The officers had arrest warrants and arrested Buie in his home for an armed robbery committed by two men, one still unaccounted for. Going into the basement to check for the second, dangerous person was the kind of [[Securing the Scene|protective sweep]] at issue; whether the basement entry was justified turned on whether the officers had articulable facts warranting a reasonable belief that the area harbored someone posing a danger. The Court [[Reading and Citing Cases#on-remand|remanded]] for the state courts to apply that reasonable-suspicion standard (the running suit having been seized in plain view during any lawful sweep).

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]: a [[Securing the Scene|protective sweep]] beyond the area immediately adjoining the arrest is permissible only on reasonable, articulable suspicion of danger, and only as a limited, cursory inspection.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Buie* imports the [[Terry v. Ohio]] / [[Michigan v. Long]] reasonable-suspicion balance into the in-home arrest setting and remains the controlling protective-sweep authority; it is distinct from the *[[Chimel v. California|Chimel]]* search-incident rationale of [[Chimel v. California]].

## Appears on
- [[Securing the Scene]] — *Key — Anchor*

## Sources
- *Maryland v. Buie*, 494 U.S. 325 (1990) — https://www.courtlistener.com/opinion/112384/maryland-v-buie/ — pinpoints: 334, 335.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4ca0f4cce5c3f428", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Buie"}, "payload": {"all": [{"cite": "494 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "494"}, {"cite": "110 S. Ct. 1093", "page": "1093", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "108 L. Ed. 2d 276", "page": "276", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "1990 U.S. LEXIS 1176", "page": "1176", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}], "display": "494 U.S. 325", "official": {"cite": "494 U.S. 325", "page": "325", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "494"}, "official_selection_present": true, "record_id": "Maryland v. Buie"}}
{"assertion_id": "0d7c57e3e3ffe3ad", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-334", "record_id": "Maryland v. Buie"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-334", "pinpoint_status": "slip-only", "quote": "— a quick search of a house for dangerous persons — conducted incident to an in-home arrest. ## Rule A two-tier rule. As to spaces right next to the arrest, no suspicion is required:", "quote_fidelity": "mismatch", "record_id": "Maryland v. Buie", "star_marker": null}}
{"assertion_id": "c53e2fb073530133", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-335", "record_id": "Maryland v. Buie"}, "payload": {"fragment": "#:~:text=there%20must%20be%20articulable%20facts", "page": null, "pin_id": "pin-335", "pinpoint_status": "star-verified", "quote": "there must be articulable facts which, taken together with the rational inferences from those facts, would warrant a reasonably prudent officer in believing that the area to be swept harbors an individual posing a danger to those on the arrest scene.", "quote_fidelity": "matched", "record_id": "Maryland v. Buie", "star_marker": "334"}}
{"assertion_id": "8b85e2d37a46ef6d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Buie"}, "payload": {"as_of_content": "1990-03-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Buie", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. Buie

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Buie",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Buie",
    "case_name_short": "Buie",
    "case_name_full": "Maryland v. Buie",
    "input_case_name": "Maryland v. Buie",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-03-05",
    "year": 1990,
    "docket": null,
    "cluster_id": 112384,
    "lead_opinion_id": 112384,
    "sibling_ids": [
      112384,
      9431933,
      9431934,
      9431935,
      9431936
    ],
    "absolute_url": "/opinion/112384/maryland-v-buie/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "494 U.S. 325",
      "volume": "494",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1093",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 276",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "276",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 1176",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1176",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "494 U.S. 325",
        "volume": "494",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1093",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1093",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 276",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "276",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 1176",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1176",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "494 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "494 U.S. 325",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-334",
      "page": null,
      "quote": "\u2014 a quick search of a house for dangerous persons \u2014 conducted incident to an in-home arrest. ## Rule A two-tier rule. As to spaces right next to the arrest, no suspicion is required:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-335",
      "page": null,
      "quote": "there must be articulable facts which, taken together with the rational inferences from those facts, would warrant a reasonably prudent officer in believing that the area to be swept harbors an individual posing a danger to those on the arrest scene.",
      "star_marker": "334",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24852,
      "fragment": "#:~:text=there%20must%20be%20articulable%20facts",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-03-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Buie",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Serrano-Acevedo",
          "cluster_id": 4506969,
          "cite": [
            "892 F.3d 454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Owens",
          "cluster_id": 4425178,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Saywahn",
          "cluster_id": 4400433,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gregory Mahrt v. Jeffrey Beard",
          "cluster_id": 4372117,
          "cite": [
            "849 F.3d 1164",
            "2017 WL 782447",
            "2017 U.S. App. LEXIS 3696"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Johnson v. State of Indiana",
          "cluster_id": 4371565,
          "cite": [
            "70 N.E.3d 890",
            "2017 WL 765897",
            "2017 Ind. App. LEXIS 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Stacey Renee McRae",
          "cluster_id": 3218840,
          "cite": [
            "194 So. 3d 524",
            "2016 Fla. App. LEXIS 9500",
            "2016 WL 3402450"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 3149374,
          "cite": [
            "88 Mass. App. Ct. 579"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Causey v. the State",
          "cluster_id": 3148713,
          "cite": [
            "334 Ga. App. 170",
            "778 S.E.2d 800"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timmie Bradley v. State of Indiana",
          "cluster_id": 2950910,
          "cite": [
            "44 N.E.3d 7",
            "2015 Ind. App. LEXIS 631",
            "2015 WL 5438394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
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
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
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
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richards v. Wisconsin",
          "cluster_id": 118103,
          "cite": [
            "137 L. Ed. 2d 615",
            "117 S. Ct. 1416",
            "520 U.S. 385",
            "1997 U.S. LEXIS 2794"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Joshua M. AARNESS",
          "cluster_id": 10014025,
          "cite": [
            "150 P.3d 1271",
            "2006 WL 2998823"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Archer v. Commonwealth",
          "cluster_id": 1067256,
          "cite": [
            "492 S.E.2d 826",
            "26 Va. App. 1",
            "1997 Va. App. LEXIS 683"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
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
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reasor v. State",
          "cluster_id": 1580731,
          "cite": [
            "12 S.W.3d 813",
            "2000 Tex. Crim. App. LEXIS 25",
            "2000 WL 228439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mattos v. Agarano",
          "cluster_id": 615433,
          "cite": [
            "661 F.3d 433",
            "2011 WL 4908374"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortiz-Sandoval v. Gomez",
          "cluster_id": 7036123,
          "cite": [
            "81 F.3d 891",
            "96 Daily Journal DAR 5369",
            "1996 U.S. App. LEXIS 10489",
            "1996 WL 180227"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Glaser",
          "cluster_id": 2607117,
          "cite": [
            "902 P.2d 729",
            "11 Cal. 4th 354",
            "45 Cal. Rptr. 2d 425",
            "95 Daily Journal DAR 13816",
            "95 Cal. Daily Op. Serv. 8067",
            "1995 Cal. LEXIS 5961"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sharrar v. Felsing",
          "cluster_id": 747743,
          "cite": [
            "128 F.3d 810",
            "1997 U.S. App. LEXIS 29129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martin Gonzalez Munoz",
          "cluster_id": 756462,
          "cite": [
            "150 F.3d 401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The People v. Stanley R. Kims, II",
          "cluster_id": 2744905,
          "cite": [
            "24 N.Y.3d 422",
            "24 N.E.3d 573"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sheppard",
          "cluster_id": 1764910,
          "cite": [
            "271 S.W.3d 281",
            "2008 Tex. Crim. App. LEXIS 1506",
            "2008 WL 5169565"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "El Bey v. Roop",
          "cluster_id": 1189624,
          "cite": [
            "530 F.3d 407",
            "2008 U.S. App. LEXIS 13776",
            "2008 WL 2572935"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jason R. Bervaldi",
          "cluster_id": 770469,
          "cite": [
            "226 F.3d 1256",
            "2000 WL 1299557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maureen Tierney, for Herself and as Mother of Philip T. Newton, Patrick J. Newton v. Joel R. Davidson Thomas E. Williams, State of Vermont",
          "cluster_id": 750084,
          "cite": [
            "133 F.3d 189",
            "1998 U.S. App. LEXIS 111"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Buie:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112384 OR 9431933 OR 9431934 OR 9431935 OR 9431936) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI0MTMxMjAwMDAwJnM9NzMxNzczMiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112384+OR+9431933+OR+9431934+OR+9431935+OR+9431936%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112384 OR 9431933 OR 9431934 OR 9431935 OR 9431936)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQmcz0yMDEzOTQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112384+OR+9431933+OR+9431934+OR+9431935+OR+9431936%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112384 OR 9431933 OR 9431934 OR 9431935 OR 9431936)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 0,
        "triage_snippet_classified": 53
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112384 OR 9431933 OR 9431934 OR 9431935 OR 9431936)",
    "indexed_citing_opinions": 1235,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112384,
        "count": 1045,
        "count_source": "search"
      },
      {
        "opinion_id": 9431933,
        "count": 209,
        "count_source": "search"
      },
      {
        "opinion_id": 9431934,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431935,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431936,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2122,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-buie.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDUwNCZzPTEwMjg3NjY2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112384+OR+9431933+OR+9431934+OR+9431935+OR+9431936%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112384,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 111959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 1540250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112384,
        "cited_id": 1999740,
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
    "date_created": "2026-07-05T11:48:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:48:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:48:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:53:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:48:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Buie

```
<div>
<center><b><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/" aria-description="Citation for case: Maryland v. Buie">494 U.S. 325</a></span> (1990)</b></center>
<center><h1>MARYLAND<br>
v.<br>
BUIE</h1></center>
<center>No. 88-1369.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 4, 1989</center>
<center>Decided February 28, 1990</center>
CERTIORARI TO THE COURT OF APPEALS OF MARYLAND
<p><span class="star-pagination">*326</span> <i>Dennis M. Sweeney,</i> Deputy Attorney General of Maryland, argued the cause for petitioner. With him on the briefs were <i>J. Joseph Curran, Jr.,</i> Attorney General, <i>Gary E. Bair, Mary Ellen Barbera,</i> and <i>Ann N. Bosse,</i> Assistant Attorneys General, and <i>Alexander Williams, Jr.</i></p>
<p><i>Lawrence S. Robbins</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Kathleen A. Felton.</i></p>
<p><span class="star-pagination">*327</span> <i>John L. Kopolow</i> argued the cause for respondent. With him on the brief were <i>Alan H. Murrell, Michael R. Braudes, Nancy S. Forster,</i> and <i>Gary S. Offutt.</i><sup>[*]</sup></p>
<p>JUSTICE WHITE delivered the opinion of the Court.</p>
<p>A "protective sweep" is a quick and limited search of premises, incident to an arrest and conducted to protect the safety of police officers or others. It is narrowly confined to a cursory visual inspection of those places in which a person might be hiding. In this case we must decide what level of justification is required by the Fourth and Fourteenth Amendments before police officers, while effecting the arrest of a suspect in his home pursuant to an arrest warrant, may conduct a warrantless protective sweep of all or part of the premises. The Court of Appeals of Maryland held that a running suit seized in plain view during such a protective sweep should have been suppressed at respondent's armed robbery trial because the officer who conducted the sweep did not have probable cause to believe that a serious and demonstrable potentiality for danger existed. <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#166" aria-description="Citation for case: Buie v. State">314 Md. 151, 166</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#86" aria-description="Citation for case: Buie v. State">550 A. 2d 79, 86</a></span> (1988). We conclude that the Fourth Amendment would permit the protective sweep undertaken here if the searching officer "possesse[d] a reasonable belief based on `specific and articulable facts which, taken together with the rational inferences from those facts, reasonably warrant[ed]' the officer in believing," <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1049" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1049-1050</a></span> (1983) (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968)), that the area swept harbored an individual posing a danger to the officer or others. We accordingly <span class="star-pagination">*328</span> vacate the judgment below and remand for application of this standard.</p>
<p></p>
<h2>I</h2>
<p>On February 3, 1986, two men committed an armed robbery of a Godfather's Pizza restaurant in Prince George's County, Maryland. One of the robbers was wearing a red running suit. That same day, Prince George's County police obtained arrest warrants for respondent Jerome Edward Buie and his suspected accomplice in the robbery, Lloyd Allen. Buie's house was placed under police surveillance.</p>
<p>On February 5, the police executed the arrest warrant for Buie. They first had a police department secretary telephone Buie's house to verify that he was home. The secretary spoke to a female first, then to Buie himself. Six or seven officers proceeded to Buie's house. Once inside, the officers fanned out through the first and second floors. Corporal James Rozar announced that he would "freeze" the basement so that no one could come up and surprise the officers. With his service revolver drawn, Rozar twice shouted into the basement, ordering anyone down there to come out. When a voice asked who was calling, Rozar announced three times: "this is the police, show me your hands." App. 5. Eventually, a pair of hands appeared around the bottom of the stairwell and Buie emerged from the basement. He was arrested, searched, and handcuffed by Rozar. Thereafter, Detective Joseph Frolich entered the basement "in case there was someone else" down there. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#14" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 14</a></span>. He noticed a red running suit lying in plain view on a stack of clothing and seized it.</p>
<p>The trial court denied Buie's motion to suppress the running suit, stating in part: "The man comes out from a basement, the police don't know how many other people are down there. He is charged with a serious offense." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 19</a></span>. The State introduced the running suit into evidence at Buie's trial. A jury convicted Buie of robbery with a deadly weapon and using a handgun in the commission of a felony.</p>
<p><span class="star-pagination">*329</span> The Court of Special Appeals of Maryland affirmed the trial court's denial of the suppression motion. The court stated that Detective Frolich did not go into the basement to search for evidence, but to look for the suspected accomplice or anyone else who might pose a threat to the officers on the scene. <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#571" aria-description="Citation for case: Buie v. State">72 Md. App. 562, 571-572</a></span>, <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#1295" aria-description="Citation for case: Buie v. State">531 A. 2d 1290, 1295</a></span> (1987).</p>
<blockquote>"Traditionally, the sanctity of a person's home  his castle  requires that the police may not invade it without a warrant except under the most exigent of circumstances. But once the police are lawfully within the home, their conduct is measured by a standard of reasonableness. . . . [I]f there is reason to believe that the arrestee had accomplices who are still at large, something less than probable cause  reasonable suspicion  should be sufficient to justify a <i>limited additional intrusion</i> to investigate the <i>possibility</i> of their presence." <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#575" aria-description="Citation for case: Buie v. State"><i>Id.,</i> at 575-576</a></span>, <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#1297" aria-description="Citation for case: Buie v. State">531 A. 2d, at 1297</a></span> (emphasis in original).</blockquote>
<p>The Court of Appeals of Maryland reversed by a 4-to-3 vote. <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/" aria-description="Citation for case: Buie v. State">314 Md. 151</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/" aria-description="Citation for case: Buie v. State">550 A. 2d 79</a></span> (1988). The court acknowledged that "when the intrusion is slight, as in the case of a brief stop and frisk on a public street, and the public interest in prevention of crime is substantial, reasonable articulable suspicion may be enough to pass constitutional muster," <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#159" aria-description="Citation for case: Buie v. State"><i>id.,</i> at 159</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#83" aria-description="Citation for case: Buie v. State">550 A. 2d, at 83</a></span>. The court, however, stated that when the sanctity of the home is involved, the exceptions to the warrant requirement are few, and held: "[T]o justify a protective sweep of a home, the government must show that there is probable cause to believe that ` "a serious and demonstrable potentiality for danger" ' exists." <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#159" aria-description="Citation for case: Buie v. State"><i>Id.,</i> at 159-160</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#83" aria-description="Citation for case: Buie v. State">550 A. 2d, at 83</a></span> (citation omitted). The court went on to find that the State had not satisfied that probable-cause requirement. <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#165" aria-description="Citation for case: Buie v. State"><i>Id.,</i> at 165-166</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#86" aria-description="Citation for case: Buie v. State">550 A. 2d, at 86</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./490/1097/">490 U. S. 1097</a></span> (1989).</p>
<p></p>
<h2>
<span class="star-pagination">*330</span> II</h2>
<p>It is not disputed that until the point of Buie's arrest the police had the right, based on the authority of the arrest warrant, to search anywhere in the house that Buie might have been found, including the basement. "If there is sufficient evidence of a citizen's participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable to require him to open his doors to the officers of the law." <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 602-603</a></span> (1980). There is also no dispute that if Detective Frolich's entry into the basement was lawful, the seizure of the red running suit, which was in plain view and which the officer had probable cause to believe was evidence of a crime, was also lawful under the Fourth Amendment. See <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#326" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 326</a></span> (1987). The issue in this case is what level of justification the Fourth Amendment required before Detective Frolich could legally enter the basement to see if someone else was there.</p>
<p>Petitioner, the State of Maryland, argues that, under a general reasonableness balancing test, police should be permitted to conduct a protective sweep whenever they make an in-home arrest for a violent crime. As an alternative to this suggested bright-line rule, the State contends that protective sweeps fall within the ambit of the doctrine announced in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and that such sweeps may be conducted in conjunction with a valid in-home arrest whenever the police reasonably suspect a risk of danger to the officers or others at the arrest scene. The United States, as <i>amicus curiae</i> supporting the State, also argues for a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>-type standard of reasonable, articulable suspicion of risk to the officer, and contends that that standard is met here. Respondent argues that a protective sweep may not be undertaken without a warrant unless the exigencies of the situation render such warrantless search objectively reasonable. According to Buie, because the State has shown neither exigent circumstances to immediately enter Buie's house <span class="star-pagination">*331</span> nor an unforeseen danger that arose once the officers were in the house, there is no excuse for the failure to obtain a search warrant to search for dangerous persons believed to be on the premises. Buie further contends that, even if the warrant requirement is inapplicable, there is no justification for relaxing the probable-cause standard. If something less than probable cause is sufficient, respondent argues that it is no less than individualized suspicion  specific, articulable facts supporting a reasonable belief that there are persons on the premises who are a threat to the officers. According to Buie, there were no such specific, articulable facts to justify the search of his basement.</p>
<p></p>
<h2>III</h2>
<p>It goes without saying that the Fourth Amendment bars only unreasonable searches and seizures, <i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span> (1989). Our cases show that in determining reasonableness, we have balanced the intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests. <i>United States</i> v. <i>Villamonte-Marquez,</i> <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#588" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 588</a></span> (1983); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979). Under this test, a search of the house or office is generally not reasonable without a warrant issued on probable cause. There are other contexts, however, where the public interest is such that neither a warrant nor probable cause is required. <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn."><i>Skinner, supra,</i> at 619-620</a></span>; <i>Griffin</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9431137"><a href="/opinion/111959/griffin-v-wisconsin/#873" aria-description="Citation for case: Griffin v. Wisconsin">483 U. S. 868, 873</a></span> (1987); <i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#340" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 340-341</a></span> (1985); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. at 20</a></span>.</p>
<p>The <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> case is most instructive for present purposes. There we held that an on-the-street "frisk" for weapons must be tested by the Fourth Amendment's general proscription against unreasonable searches because such a frisk involves "an entire rubric of police conduct  necessarily swift action predicated upon the on-the-spot observations of the officer on the beat  which historically has not been, and as a practical <span class="star-pagination">*332</span> matter could not be, subjected to the warrant procedure." <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ibid.</a></span></i> We stated that there is " `no ready test for determining reasonableness other than by balancing the need to search . . . against the invasion which the search . . . entails.' " <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></i> at 21 (quoting <i>Camara</i> v. <i>Municipal Court of San Francisco,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967). Applying that balancing test, it was held that although a frisk for weapons "constitutes a severe, though brief, intrusion upon cherished personal security," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 24-25</a></span>, such a frisk is reasonable when weighed against the "need for law enforcement officers to protect themselves and other prospective victims of violence in situations where they may lack probable cause for an arrest." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 24</a></span>. We therefore authorized a limited patdown for weapons where a reasonably prudent officer would be warranted in the belief, based on "specific and articulable facts," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 21</a></span>, and not on a mere "inchoate and unparticularized suspicion or `hunch,' " <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 27</a></span>, "that he is dealing with an armed and dangerous individual," <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">ibid.</a></span></i></p>
<p>In <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), the principles of <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> were applied in the context of a roadside encounter: "[T]he search of the passenger compartment of an automobile, limited to those areas in which a weapon may be placed or hidden, is permissible if the police officer possesses a reasonable belief based on `specific and articulable facts which, taken together with the rational inferences from those facts, reasonably warrant' the officer in believing that the suspect is dangerous and the suspect may gain immediate control of weapons." <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></i> at 1049-1050 (quoting <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 21</a></span>). The <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> Court expressly rejected the contention that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> restricted preventative searches to the person of a detained suspect. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1047" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1047</a></span>. In a sense, <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> authorized a "frisk" of an automobile for weapons.</p>
<p>The ingredients to apply the balance struck in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> are present in this case. Possessing an arrest warrant and probable cause to believe Buie was in his home, the officers <span class="star-pagination">*333</span> were entitled to enter and to search anywhere in the house in which Buie might be found. Once he was found, however, the search for him was over, and there was no longer that particular justification for entering any rooms that had not yet been searched.</p>
<p>That Buie had an expectation of privacy in those remaining areas of his house, however, does not mean such rooms were immune from entry. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> we were concerned with the immediate interest of the police officers in taking steps to assure themselves that the persons with whom they were dealing were not armed with, or able to gain immediate control of, a weapon that could unexpectedly and fatally be used against them. In the instant case, there is an analogous interest of the officers in taking steps to assure themselves that the house in which a suspect is being, or has just been, arrested is not harboring other persons who are dangerous and who could unexpectedly launch an attack. The risk of danger in the context of an arrest in the home is as great as, if not greater than, it is in an on-the-street or roadside investigatory encounter. A <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> or <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> frisk occurs before a police-citizen confrontation has escalated to the point of arrest. A protective sweep, in contrast, occurs as an adjunct to the serious step of taking a person into custody for the purpose of prosecuting him for a crime. Moreover, unlike an encounter on the street or along a highway, an in-home arrest puts the officer at the disadvantage of being on his adversary's "turf." An ambush in a confined setting of unknown configuration is more to be feared than it is in open, more familiar surroundings.</p>
<p>We recognized in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> that "[e]ven a limited search of the outer clothing for weapons constitutes a severe, though brief, intrusion upon cherished personal security, and it must surely be an annoying, frightening, and perhaps humiliating experience." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 24-25</a></span>. But we permitted the intrusion, which was no more than necessary to protect the officer from harm. Nor do we here suggest, as the State <span class="star-pagination">*334</span> does, that entering rooms not examined prior to the arrest is a <i>de minimis</i> intrusion that may be disregarded. We are quite sure, however, that the arresting officers are permitted in such circumstances to take reasonable steps to ensure their safety after, and while making, the arrest. That interest is sufficient to outweigh the intrusion such procedures may entail.</p>
<p>We agree with the State, as did the court below, that a warrant was not required.<sup>[1]</sup> We also hold that as an incident to the arrest the officers could, as a precautionary matter and without probable cause or reasonable suspicion, look in closets and other spaces immediately adjoining the place of arrest from which an attack could be immediately launched. Beyond that, however, we hold that there must be articulable facts which, taken together with the rational inferences from those facts, would warrant a reasonably prudent officer in believing that the area to be swept harbors an individual posing a danger to those on the arrest scene. This is no more and no less than was required in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> and as in those cases, we think this balance is the proper one.<sup>[2]</sup></p>
<p><span class="star-pagination">*335</span> We should emphasize that such a protective sweep, aimed at protecting the arresting officers, if justified by the circumstances, is nevertheless not a full search of the premises, but may extend only to a cursory inspection of those spaces where a person may be found.<sup>[3]</sup> The sweep lasts no longer <span class="star-pagination">*336</span> than is necessary to dispel the reasonable suspicion of danger and in any event no longer than it takes to complete the arrest and depart the premises.</p>
<p></p>
<h2>IV</h2>
<p>Affirmance is not required by <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), where it was held that in the absence of a search warrant, the justifiable search incident to an in-home arrest could not extend beyond the arrestee's person and the area from within which the arrestee might have obtained a weapon. First, <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was concerned with a full-blown search of the entire house for evidence of the crime for which the arrest was made, see <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#754" aria-description="Citation for case: Chimel v. California"><i>id.,</i> at 754, 763</a></span>, not the more limited intrusion contemplated by a protective sweep. Second, the justification for the search incident to arrest considered in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> was the threat posed by the arrestee, not the safety threat posed by the house, or more properly by unseen third parties in the house. To reach our conclusion today, therefore, we need not disagree with the Court's statement in <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#766" aria-description="Citation for case: Chimel v. California"><i>Chimel, id.,</i> at 766-767, n. 12</a></span>, that "the invasion of privacy that results from a top-to-bottom search of a man's house [cannot be characterized] as `minor,' " nor hold that "simply because some interference with an individual's privacy and freedom of movement has lawfully taken place, further intrusions should automatically be allowed despite the absence of a warrant that the Fourth Amendment would otherwise require," <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">ibid.</a></span></i> The type of search we authorize today is far removed from the "top-to-bottom" search involved in <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>;</i> moreover, it is decidedly not "automati[c]," but may be conducted only when justified by a reasonable, articulable suspicion that the house is harboring a person posing a danger to those on the arrest scene.</p>
<p></p>
<h2>V</h2>
<p>We conclude that by requiring a protective sweep to be justified by probable cause to believe that a serious and demonstrable potentiality for danger existed, the Court of Appeals <span class="star-pagination">*337</span> of Maryland applied an unnecessarily strict Fourth Amendment standard. The Fourth Amendment permits a properly limited protective sweep in conjunction with an in-home arrest when the searching officer possesses a reasonable belief based on specific and articulable facts that the area to be swept harbors an individual posing a danger to those on the arrest scene. We therefore vacate the judgment below and remand this case to the Court of Appeals of Maryland for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, concurring.</p>
<p>Today the Court holds that reasonable suspicion, rather than probable cause, is necessary to support a protective sweep while an arrest is in progress. I agree with that holding and with the Court's opinion, but I believe it is important to emphasize that the standard applies only to <i>protective</i> sweeps. Officers conducting such a sweep must have a reasonable basis for believing that their search will reduce the danger of harm to themselves or of violent interference with their mission; in short, the search must be protective.</p>
<p>In this case, to justify Officer Frolich's entry into the basement, it is the State's burden to demonstrate that the officers had a reasonable basis for believing not only that someone in the basement might attack them or otherwise try to interfere with the arrest, but also that it would be safer to go down the stairs instead of simply guarding them from above until respondent had been removed from the house. The fact that respondent offered no resistance when he emerged from the basement is somewhat inconsistent with the hypothesis that the danger of an attack by a hidden confederate persisted after the arrest. Moreover, Officer Rozar testified that he was not worried about any possible danger when he arrested Buie. App. 9.<sup>[1]</sup> Officer Frolich, who conducted the search, <span class="star-pagination">*338</span> supplied no explanation for why he might have thought another person was in the basement. He said only that he "had no idea who lived there." <i>Id.,</i> at 15. This admission is made telling by Officer Frolich's participation in the 3-day prearrest surveillance of Buie's home. <i>Id.,</i> at 4. The Maryland Court of Appeals was under the impression that the search took place after "Buie was safely outside the house, handcuffed and unarmed." <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#166" aria-description="Citation for case: Buie v. State">314 Md. 151, 166</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#86" aria-description="Citation for case: Buie v. State">550 A. 2d 79, 86</a></span> (1988). All of this suggests that no reasonable suspicion of danger justified the entry into the basement.</p>
<p>Indeed, were the officers concerned about safety, one would expect them to do what Officer Rozar did before the arrest: guard the basement door to prevent surprise attacks. App. 5. As the Court indicates, Officer Frolich might, at the time of the arrest, reasonably have "look[ed] in" the already open basement door, <i>ante,</i> at 334, to ensure that no accomplice had followed Buie to the stairwell. But Officer Frolich did not merely "look in" the basement; he entered it.<sup>[2]</sup> That strategy is sensible if one wishes to search the basement. It is a surprising choice for an officer, worried about safety, who need not risk entering the stairwell at all.</p>
<p>The State may thus face a formidable task on remand. However, the Maryland courts are better equipped than are we to review the record. See, <i>e. g.,</i> <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#155" aria-description="Citation for case: Buie v. State">314 Md., at 155, n. 2</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#81" aria-description="Citation for case: Buie v. State">550 A. 2d, at 81, n. 2</a></span> (discussing state-law rules restricting review of the record on appeal of suppression decisions); cf. <i>United States</i> v. <i>Hasting,</i> <span class="citation" data-id="9429194"><a href="/opinion/110933/united-states-v-hasting/#516" aria-description="Citation for case: United States v. Hasting">461 U. S. 499, 516-518</a></span> (1983) (STEVENS, J., dissenting) (This Court should avoid undertaking record review functions that can "better be performed by other judges"). Moreover, the Maryland Court of Special <span class="star-pagination">*339</span> Appeals suggested that Officer Frolich's search could survive a "reasonable suspicion" test, <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#576" aria-description="Citation for case: Buie v. State">72 Md. App. 562, 576</a></span>, <span class="citation" data-id="1999740"><a href="/opinion/1999740/buie-v-state/#1297" aria-description="Citation for case: Buie v. State">531 A. 2d 1290, 1297</a></span> (1987), and the Maryland Court of Appeals has not reviewed this conclusion. I therefore agree that a remand is appropriate.</p>
<p>JUSTICE KENNEDY, concurring.</p>
<p>The Court adopts the prudent course of explaining the general rule and permitting the state court to apply it in the first instance. The concurrence by JUSTICE STEVENS, however, makes the gratuitous observation that the State has a formidable task on remand. My view is quite to the contrary. Based on my present understanding of the record, I should think the officers' conduct here was in full accord with standard police safety procedure, and that the officers would have been remiss if they had not taken these precautions. This comment is necessary, lest by acquiescence the impression be left that JUSTICE STEVENS' views can be interpreted as authoritative guidance for application of our ruling to the facts of the case.</p>
<p>JUSTICE BRENNAN, with whom JUSTICE MARSHALL joins, dissenting.</p>
<p>Today the Court for the first time extends <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), into the home, dispensing with the Fourth Amendment's general requirements of a warrant and probable cause and carving a "reasonable suspicion" exception for protective sweeps in private dwellings. In <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry, supra,</a></span></i> the Court held that a police officer may briefly detain a suspect based on a reasonable suspicion of criminal activity and may conduct a limited "frisk" of the suspect for concealed weapons in order to protect herself from personal danger. The Court deemed such a frisk "reasonable" under the Fourth Amendment in light of the special "need for law enforcement officers to protect themselves and other prospective victims of violence" during investigative detentions, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#24" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 24</a></span>, and the <span class="star-pagination">*340</span> "brief, though far from inconsiderable, intrusion upon the sanctity of the person." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#26" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 26</a></span>.</p>
<p><i>Terry</i> and its early progeny "permit[ted] only brief investigative stops and extremely limited searches based on reasonable suspicion." <i>United State</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#714" aria-description="Citation for case: United States v. Place">462 U. S. 696, 714</a></span> (1983) (BRENNAN, J., concurring in result). But this Court more recently has applied the rationale underlying <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> to a wide variety of more intrusive searches and seizures,<sup>[1]</sup> prompting my continued criticism of the " `emerging tendency on the part of the Court to convert the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> decision' " from a narrow exception into one that " `swallow[s] the general rule that [searches] are "reasonable" only if based on probable cause.' " <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#719" aria-description="Citation for case: United States v. Place"><i>Place, supra,</i> at 719</a></span> (BRENNAN, J., concurring in result) (citations omitted).</p>
<p>The Court today holds that <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i>'s "reasonable suspicion" standard "strikes the proper balance between officer safety and citizen privacy" for protective sweeps in private dwellings. <i>Ante,</i> at 335, n. 2. I agree with the majority that officers executing an arrest warrant within a private dwelling have an interest in protecting themselves against potential ambush by third parties, see <i>ante,</i> at 333, but the majority offers no support for its assumption that the danger of ambush during planned home arrests approaches the danger of unavoidable "on-the-beat" confrontations in "the myriad daily situations in which policemen and citizens confront each other on the street." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 12</a></span>.<sup>[2]</sup> In any event, <span class="star-pagination">*341</span> the Court's implicit judgment that a protective sweep constitutes a "minimally intrusive" search akin to that involved in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> markedly undervalues the nature and scope of the privacy interests involved.</p>
<p>While the Fourth Amendment protects a person's privacy interests in a variety of settings, "physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed." <i>United States</i> v. <i>United States District Court, Eastern District of Michigan,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972).<sup>[3]</sup> The Court discounts the nature of the intrusion because it believes that the scope of the intrusion is limited. The Court explains that a protective sweep's scope is "narrowly confined to a cursory visual inspection of those places in which a person might be hiding," <i>ante,</i> at 327, and confined in duration to a period "no longer than is necessary to dispel the reasonable suspicion of danger and in any event no longer than it takes to complete the arrest and depart the premises." <i>Ante,</i> at 335-336.<sup>[4]</sup> But these spatial and temporal <span class="star-pagination">*342</span> restrictions are not particularly limiting. A protective sweep would bring within police purview virtually all personal possessions within the house not hidden from view in a small enclosed space. Police officers searching for potential ambushers might enter every room including basements and attics; open up closets, lockers, chests, wardrobes, and cars; and peer under beds and behind furniture. The officers will view letters, documents, and personal effects that are on tables or desks or are visible inside open drawers; books, records, tapes, and pictures on shelves; and clothing, medicines, toiletries and other paraphernalia not carefully stored in dresser drawers or bathroom cupboards. While perhaps not a "full-blown" or "top-to-bottom" search <i>ante,</i> at 336, a protective sweep is much closer to it than to a "limited patdown for weapons" or a " `frisk' of an automobile." <i>Ante,</i> at 332.<sup>[5]</sup> Because the nature and scope of the intrusion sanctioned here are far greater than those upheld in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span>,</i> the Court's conclusion that "[t]he ingredients to apply the balance struck in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and <i><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Long</a></span></i> are present in this case," <i>ibid.,</i> is unwarranted. The "ingredient" of a minimally intrusive search is absent, and the Court's holding today therefore unpalatably deviates from <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and its progeny.<sup>[6]</sup></p>
<p><span class="star-pagination">*343</span> In light of the special sanctity of a private residence and the highly intrusive nature of a protective sweep, I firmly believe that police officers must have probable cause to fear that their personal safety is threatened by a hidden confederate of an arrestee before they may sweep through the entire home. Given the state-court determination that the officers searching Buie's home lacked probable cause to perceive such a danger and therefore were not lawfully present in the basement, I would affirm the state court's decision to suppress the incriminating evidence. I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  <i>Gregory U. Evans, Daniel B. Hales, Emory A. Plitt, Jr., Judith A. Ronzio, George D. Webster, Jack E. Yelverton, Fred E. Inbau, Wayne W. Schmidt,</i> and <i>James P. Manak</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>Ira Reiner, Harry B. Sondheim,</i> and <i>Eugene D. Tavris</i> field a brief for the Appellate Committee of the California District Attorneys Association as <i>amicus curiae.</i></p>
<p>[1]  Buie suggests that because the police could have sought a warrant to search for dangerous persons in the house, they were constitutionally required to do so. But the arrest warrant gave the police every right to enter the home to search for Buie. Once inside, the potential for danger justified a standard of less than probable cause for conducting a limited protective sweep.</p>
<p>[2]  The State's argument that no level of objective justification should be required because of "the danger that inheres in the in-home arrest for a violent crime," Brief for Petitioner 23, is rebutted by <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), itself. The State argues that "[o]fficers facing the life threatening situation of arresting a violent criminal in the home should not be forced to pause and ponder the legal subtleties associated with a quantum of proof analysis," Brief for Petitioner 23. But despite the danger that inheres in on-the-street encounters and the need for police to act quickly for their own safety, the Court in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> did not adopt a brightline rule authorizing frisks for weapons in all confrontational encounters. Even in high crime areas, where the possibility that any given individual is armed is significant, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> requires reasonable, individualized suspicion before a frisk for weapons can be conducted. That approach is applied to the protective sweep of a house.
</p>
<p>We reject the State's attempts to analogize this case to <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977) <i>(per curiam)</i><i>,</i> and <i>Michigan</i> v. <i>Summers,</i> <span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692</a></span> (1981). The intrusion in <i><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span></i>  requiring the driver of a lawfully stopped vehicle to exit the car  was <i>"de minimis,"</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#111" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S., at 111</a></span>. <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> held that a search warrant for a house carries with it the authority to detain its occupants until the search is completed. The State contends that this case is the "mirror image" of <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> and that the arrest warrant carried with it the authority to search for persons who could interfere with the arrest. In that case, however, the search warrant implied a judicial determination that police had probable cause to believe that someone in the home was committing a crime. Here, the existence of the arrest warrant implies nothing about whether dangerous third parties will be found in the arrestee's house. Moreover, the intrusion in <i><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/" aria-description="Citation for case: Michigan v. Summers">Summers</a></span></i> was less severe and much less susceptible to exploitation than a protective sweep. A more analogous case is <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979), in which we held that, although armed with a warrant to search a bar and bartender, the police could not frisk the bar's patrons absent individualized, reasonable suspicion that the person to be frisked was armed and presently dangerous. Here, too, the reasonable suspicion standard  "one of the relatively simple concepts embodied in the Fourth Amendment," <i>United States</i> v. <i>Sokolow,</i> <span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1</a></span> (1989)  strikes the proper balance between officer safety and citizen privacy.</p>
<p>[3]  Our reliance on the cursory nature of the search is not inconsistent with our statement in <i>Arizona</i> v. <i>Hicks,</i> <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321</a></span> (1987), that "[a] search is a search," <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#325" aria-description="Citation for case: Arizona v. Hicks"><i>id.,</i> at 325</a></span>, or with our refusal in <i><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">Hicks</a></span></i> to sanction a standard less than probable cause on the ground that the search of a stereo was a "cursory inspection," rather than a "full-blown search," <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#328" aria-description="Citation for case: Arizona v. Hicks"><i>id.,</i> at 328</a></span>. When the officer in <i><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/" aria-description="Citation for case: Arizona v. Hicks">Hicks</a></span></i> moved the turntable to look at its serial number, he was searching for evidence plain and simple. There was no interest in officer safety or other exigency at work in that search. A protective sweep is without question a "search," as was the patdown in <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 16</a></span>; they are permissible on less than probable cause only because they are limited to that which is necessary to protect the safety of officers and others.</p>
<p>[1]  Buie's attorney asked, " `You weren't worried about there being any danger or anything like that?' " Officer Rozar answered, " `No.' " App. 9.</p>
<p>[2]  What more the officers might have done to protect themselves against threats from other places is obviously a question not presented on the facts of this case, and so is not one we can answer. Indeed, the peculiarity of Officer Frolich's search is that it appears to have concentrated upon the part of the house least likely to make the departing officers vulnerable to attack.</p>
<p>[1]  The Court has recently relied on <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> to relax the warrant and probable-cause requirements for both searches of places, <i>e. g., </i><i>New York</i> v. <i>Class,</i> <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/" aria-description="Citation for case: New York v. Class">475 U. S. 106</a></span> (1986) (search of car interior); <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983) (same); and seizures of personal effects, <i>e. g., </i><i>New Jersey</i> v. <i>T. L. O.,</i> <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325</a></span> (1985) (search of student's purse); <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983) (seizure of luggage).</p>
<p>[2]  Individual police officers necessarily initiate street encounters without advance planning "for a wide variety of purposes." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#13" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 13</a></span>. But officers choosing to execute an arrest warrant in the suspect's house may minimize any risk of ambush by, for example, a show of force; in this case, at least six armed officers secured the premises. And, of course, officers could select a safer venue for making their arrest.</p>
<p>[3]  Here the officers' arrest warrant for Buie and their probable cause to believe he was present in the house authorized their initial entry. But, as the majority concedes, "[o]nce he was found . . . the search for him was over," and "Buie had an expectation of privacy in those remaining areas of his house." <i>Ante,</i> at 333. The fact that some areas were necessarily exposed to the police during Buie's arrest thus does not diminish his privacy interest in the remaining rooms. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#767" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 767, n. 12</a></span> (1969) ("[W]e can see no reason why, simply because some interference with an individual's privacy and freedom of movement has lawfully taken place, further intrusions should automatically be allowed despite the absence of a warrant that the Fourth Amendment would otherwise require").</p>
<p>[4]  The protective sweep in this case may have exceeded the permissible temporal scope defined by the Court. The Court of Appeals of Maryland expressly noted that "at the time of the warrantless search, Buie was safely outside the house, handcuffed and unarmed." <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#166" aria-description="Citation for case: Buie v. State">314 Md. 151, 166</a></span>, <span class="citation" data-id="9650041"><a href="/opinion/1540250/buie-v-state/#86" aria-description="Citation for case: Buie v. State">550 A. 2d 79, 86</a></span> (1988). On remand, therefore, the state court need not decide whether the "reasonable suspicion" standard is satisfied in this case should it determine that the sweep of the basement took place after the police had sufficient time to "complete the arrest and depart the premises." <i>Ante,</i> at 336.</p>
<p>[5]  Indeed, a protective sweep is sufficiently broad in scope that today's ruling might encourage police officers to execute arrest warrants in suspects' homes so as to take advantage of the opportunity to peruse the premises for incriminating evidence left in "plain view." This incentive runs directly counter to our central tenet that "in[no setting] is the zone of privacy more clearly defined than when bounded by the unambiguous physical dimensions of an individual's home-a zone that finds its roots in clear and specific constitutional terms." <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#589" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 589</a></span> (1980).</p>
<p>[6]  The Court's decision also to expand the "search incident to arrest" exception previously recognized in <i>Chimel</i> v. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">California, supra</a></span></i><i>,</i> allowing police officers without <i>any</i> requisite level of suspicion to look into "closets and other spaces immediately adjoining the place of arrest from which an attack could be immediately launched," <i>ante,</i> at 334, is equally disquieting. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span></i> established that police officers may presume as a matter of law, without need for factual support in a particular case, that arrestees might take advantage of weapons or destroy evidence in the area "within [their] immediate control"; therefore, a protective search of that area is <i>per se</i> reasonable under the Fourth Amendment. <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><i>Chimel, supra,</i> at 763</a></span>. I find much less plausible the Court's implicit assumption today that arrestees are likely to sprinkle hidden allies throughout the rooms in which they might be arrested. Hence there is no comparable justification for permitting arresting officers to presume as a matter of law that they are threatened by ambush from "immediately adjoining" spaces.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Dyson.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Maryland v. Dyson"
type: case
citation: "527 U.S. 465 (1999)"
parallel_cite: "119 S. Ct. 2013; 144 L. Ed. 2d 442"
neutral_cite: 1999 U.S. LEXIS 4200
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-06-21
docket: 98-1062
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Dyson
  varies_by_point: false
  scope_note: "Per curiam. Settled statement of the automobile exception; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2621047/maryland-v-dyson/"
  cluster_id: 2621047
  opinion_id: 9795106
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Pennsylvania v. Labron]]", "[[United States v. Ross]]", "[[California v. Carney]]", "[[Carroll v. United States]]", "[[Michigan v. Thomas]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "no-exigency", "probable-cause", "readily-mobile"]
holding: "The automobile exception has no separate exigency requirement; if a car is readily mobile and probable cause exists to believe it contains contraband, police may search it without a warrant even when there was ample time to obtain one."
lake:
  record_id: Maryland v. Dyson
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Dyson

*527 U.S. 465 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A sheriff's deputy received a tip from a reliable confidential informant that the respondent, a known drug dealer, had gone to New York to buy cocaine and would return that day in a specifically identified rented red Toyota. The deputy corroborated the rental and the license plate. When the respondent returned in the car, deputies stopped and searched it without a warrant and found 23 grams of crack cocaine in a duffel bag in the trunk. The Maryland Court of Special Appeals reversed the conviction, holding that the automobile exception requires, in addition to probable cause, a separate finding of [[Exigent Circumstances and Hot Pursuit|exigency]] — and that here, with "abundant probable cause" but ample time to get a warrant, the warrantless search was invalid.

## Issue
Whether the automobile exception requires a separate finding of [[Exigent Circumstances and Hot Pursuit|exigency]] in addition to probable cause to believe the vehicle contains contraband.

## Rule
No. "[U]nder our established precedent, the 'automobile exception' has no separate exigency requirement." — 527 U.S. at 466. ^pin-466

Quoting *[[Pennsylvania v. Labron]]*: "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment . . . permits police to search the vehicle without more." — *Id.* at 467 (quoting 518 U.S. at 940). ^pin-467

## Application
The state court itself found "abundant probable cause" that the car contained contraband. That finding alone satisfied the automobile exception, exactly as the trial court had concluded. Requiring a separate showing of [[Exigent Circumstances and Hot Pursuit|exigency]] — and faulting the police for not getting a warrant when there was time — was "squarely contrary" to *[[United States v. Ross|Ross]]* and *[[Pennsylvania v. Labron|Labron]]*. The warrantless search of the readily mobile car was therefore valid.

## Conclusion
Reversed (per curiam). Probable cause that a readily mobile vehicle contains contraband is enough; the automobile exception carries no independent [[Exigent Circumstances and Hot Pursuit|exigency]] requirement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Dyson* states flatly the principle developed across [[Carroll v. United States]], [[United States v. Ross]], [[Michigan v. Thomas]], and [[Pennsylvania v. Labron]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Dyson*, 527 U.S. 465 (1999) — https://www.courtlistener.com/opinion/2621047/maryland-v-dyson/ — pinpoints: 466, 467.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e002e96285162310", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Dyson"}, "payload": {"all": [{"cite": "527 U.S. 465", "page": "465", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "527"}, {"cite": "119 S. Ct. 2013", "page": "2013", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "119"}, {"cite": "144 L. Ed. 2d 442", "page": "442", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "144"}, {"cite": "1999 U.S. LEXIS 4200", "page": "4200", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1999"}], "display": "527 U.S. 465", "official": {"cite": "527 U.S. 465", "page": "465", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "527"}, "official_selection_present": true, "record_id": "Maryland v. Dyson"}}
{"assertion_id": "58860ccce7e4a691", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-467", "record_id": "Maryland v. Dyson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-467", "pinpoint_status": "slip-only", "quote": "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment . . . permits police to search the vehicle without more.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Dyson", "star_marker": null}}
{"assertion_id": "74de8ac9e461f3cf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-466", "record_id": "Maryland v. Dyson"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-466", "pinpoint_status": "slip-only", "quote": "but ample time to get a warrant, the warrantless search was invalid. ## Issue Whether the automobile exception requires a separate finding of exigency in addition to probable cause to believe the vehicle contains contraband. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Dyson", "star_marker": null}}
{"assertion_id": "26ef089364be15a8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Dyson"}, "payload": {"as_of_content": "1999-06-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Dyson", "scope_note": "Per curiam. Settled statement of the automobile exception; no negative treatment.", "varies_by_point": false}}
```

### lake record — Maryland v. Dyson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Dyson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Dyson",
    "case_name_short": "Dyson",
    "case_name_full": "Maryland v. Dyson",
    "input_case_name": "Maryland v. Dyson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-06-21",
    "year": 1999,
    "docket": "98-1062",
    "cluster_id": 2621047,
    "lead_opinion_id": 9795106,
    "sibling_ids": [
      2621047,
      9795106,
      9795107
    ],
    "absolute_url": "/opinion/2621047/maryland-v-dyson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "527 U.S. 465",
      "volume": "527",
      "reporter": "U.S.",
      "page": "465",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 2013",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "2013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 442",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 4200",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "527 U.S. 465",
        "volume": "527",
        "reporter": "U.S.",
        "page": "465",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 2013",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "2013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 442",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 4200",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4200",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "527 U.S. 465",
    "official_selection": {
      "court_class": "scotus",
      "selected": "527 U.S. 465",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-466",
      "page": null,
      "quote": "but ample time to get a warrant, the warrantless search was invalid. ## Issue Whether the automobile exception requires a separate finding of exigency in addition to probable cause to believe the vehicle contains contraband. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-467",
      "page": null,
      "quote": "If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment . . . permits police to search the vehicle without more.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Dyson",
    "varies_by_point": false,
    "scope_note": "Per curiam. Settled statement of the automobile exception; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Knight",
          "cluster_id": 4499332,
          "cite": [
            "419 P.3d 637",
            "55 Kan. App. 2d 642"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Limon v. State",
          "cluster_id": 1466284,
          "cite": [
            "314 S.W.3d 694",
            "2010 Tex. App. LEXIS 4565",
            "2010 WL 2430428"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hubert v. State",
          "cluster_id": 1464366,
          "cite": [
            "312 S.W.3d 554",
            "2010 Tex. Crim. App. LEXIS 636",
            "2010 WL 2077166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 2347917,
          "cite": [
            "256 S.W.3d 264",
            "2008 Tex. Crim. App. LEXIS 754",
            "2008 WL 2437667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 2187417,
          "cite": [
            "305 S.W.3d 530",
            "2009 Tex. Crim. App. LEXIS 1440",
            "2009 WL 3365661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tyronski Johnson",
          "cluster_id": 790485,
          "cite": [
            "410 F.3d 137",
            "2005 U.S. App. LEXIS 10600",
            "2005 WL 1345622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Kazmierczak",
          "cluster_id": 1965440,
          "cite": [
            "605 N.W.2d 667",
            "461 Mich. 411",
            "2000 WL 146099"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keehn v. State",
          "cluster_id": 2341745,
          "cite": [
            "279 S.W.3d 330",
            "2009 Tex. Crim. App. LEXIS 425",
            "2009 WL 774854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randy Graham",
          "cluster_id": 775981,
          "cite": [
            "275 F.3d 490",
            "2001 U.S. App. LEXIS 26685",
            "2001 WL 1636805"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Turner",
          "cluster_id": 4326929,
          "cite": [
            "2016 Ohio 7983"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cooke",
          "cluster_id": 2196499,
          "cite": [
            "751 A.2d 92",
            "163 N.J. 657",
            "2000 N.J. LEXIS 529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dixon v. State",
          "cluster_id": 1400372,
          "cite": [
            "206 S.W.3d 613",
            "2006 Tex. Crim. App. LEXIS 1006",
            "2006 WL 1408451"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Randall Cope and Terry Wayne Cope",
          "cluster_id": 780062,
          "cite": [
            "312 F.3d 757"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gauster",
          "cluster_id": 1873770,
          "cite": [
            "752 N.W.2d 496",
            "2008 Minn. LEXIS 322",
            "2008 WL 2678037"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 852726,
          "cite": [
            "839 N.E.2d 1146",
            "2005 Ind. LEXIS 1135",
            "2005 WL 3484607"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Mosley",
          "cluster_id": 794964,
          "cite": [
            "454 F.3d 249",
            "2006 U.S. App. LEXIS 18322",
            "2006 WL 2035249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elison",
          "cluster_id": 885285,
          "cite": [
            "2000 MT 288",
            "14 P.3d 456",
            "302 Mont. 228",
            "2000 Mont. LEXIS 291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baldwin v. Reagan",
          "cluster_id": 853850,
          "cite": [
            "715 N.E.2d 332",
            "1999 Ind. LEXIS 413",
            "1999 WL 452155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Katrina Lyons",
          "cluster_id": 805149,
          "cite": [
            "687 F.3d 754",
            "2012 WL 3023528",
            "2012 U.S. App. LEXIS 15300"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Dyson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2621047 OR 9795106 OR 9795107) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMxOTc3NjAwMDAwJnM9MjkyNzUxMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282621047+OR+9795106+OR+9795107%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(2621047 OR 9795106 OR 9795107)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MSZzPTIxNjI2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282621047+OR+9795106+OR+9795107%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2621047 OR 9795106 OR 9795107)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2621047 OR 9795106 OR 9795107)",
    "indexed_citing_opinions": 416,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2621047,
        "count": 352,
        "count_source": "search"
      },
      {
        "opinion_id": 9795106,
        "count": 72,
        "count_source": "search"
      },
      {
        "opinion_id": 9795107,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 696,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-dyson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwODM4ODImcz05MzU3MDM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282621047+OR+9795106+OR+9795107%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2621047,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2621047,
        "cited_id": 1929659,
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
    "date_created": "2026-07-05T11:53:09Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:56:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:53:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Dyson

```
<opinion type="majority">
<author id="b499-10">Per Curiam.</author>
<p id="b499-11">In this case, the Maryland Court of Special Appeals held that the Fourth Amendment requires police to obtain a search warrant before searching a vehicle which they have probable cause to believe contains illegal drugs. Because this holding rests upon an incorrect interpretation of the automobile exception to the Fourth Amendment’s warrant requirement, we grant the petition for certiorari and reverse.</p>
<p id="b499-12">At 11 a.m. on the morning of July 2, 1996, a St. Mary’s County (Maryland) Sheriff’s Deputy received a tip from a reliable confidential informant that respondent had gone to New York to buy drugs, and would be returning to Maryland in a rented red Toyota, license number DDY 787, later that day with a large quantity of cocaine. The deputy investí-<page-number citation-index="1" label="466">*466</page-number>gated the tip and found that the license number given to him by the informant belonged to a red Toyota Corolla that had been rented to respondent, who was a known drug dealer in St. Mary’s County. When respondent returned to St. Mary’s County in the rented car at 1 a.m. on July 3, the deputies stopped and searched the vehicle, finding 23 grams of crack cocaine in a duffel bag in the trunk. Respondent was arrested, tried, and convicted of conspiracy to possess cocaine with intent to distribute. He appealed, arguing that the trial court had erroneously denied his motion to suppress the cocaine on the alternative grounds that the police lacked probable cause, or that even if there was probable cause, the warrantless search violated the Fourth Amendment because there was sufficient time after the informant’s tip to obtain a warrant.</p>
<p id="b500-5">The Maryland Court of Special Appeals reversed, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/" aria-description="Citation for case: Dyson v. State">122 Md. App. 413</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/" aria-description="Citation for case: Dyson v. State">712 A. 2d 573</a></span> (1998), holding that in order for the automobile exception to the warrant requirement to apply, there must not only be probable cause to believe that evidence of a crime is contained in the automobile, but also a separate finding of exigency precluding the police from obtaining a warrant. <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#424" aria-description="Citation for case: Dyson v. State"><em>Id., </em>at 424</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#578" aria-description="Citation for case: Dyson v. State">712 A. 2d, at 578</a></span>. Applying this rule to the facts of the case, the Court of Special Appeals concluded that although there was “abundant probable cause,” the search violated the Fourth Amendment because there was no exigency that prevented or even made it significantly difficult for the police to obtain a search warrant. <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#426" aria-description="Citation for case: Dyson v. State"><em>Id., </em>at 426</a></span>, <span class="citation" data-id="1929659"><a href="/opinion/1929659/dyson-v-state/#579" aria-description="Citation for case: Dyson v. State">712 A. 2d, at 579</a></span>. The Maryland Court of Appeals denied certiorari. <span class="citation no-link">351 Md. 287</span>, <span class="citation no-link">718 A. 2d 235</span> (1998). We grant certiorari and now reverse.</p>
<p id="b500-6">The Fourth Amendment generally requires police to secure a warrant before conducting a search. <em>California </em>v. <em>Carney, </em><span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#390" aria-description="Citation for case: California v. Carney">471 U. S. 386, 390-391</a></span> (1985). As we recognized nearly 75 years ago in <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153</a></span> (1925), there is an exception to this requirement for searches of vehicles. And under our established precedent, the “automobile exception” has no separate exigency re<page-number citation-index="1" label="467">*467</page-number>quirement. We made this clear in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#809" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 809</a></span> (1982), when we said that in cases where there was probable cause to search a vehicle “a search is not unreasonable if based on facts that would justify the issuance of a warrant, <em>even though a warrant has not been actually obtained.” </em>(Emphasis added.) In a case with virtually identical facts to this one (even down to the bag of cocaine in the trunk of the car), <em>Pennsylvania </em>v. <em>Labron, </em><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">518 U. S. 938</a></span> (1996) <em>(per curiam), </em>we repeated that the automobile exception does not have a separate exigency requirement: “If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment... permits police to search the vehicle without more.” <span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/#940" aria-description="Citation for case: Pennsylvania v. Labron"><em>Id., </em>at 940</a></span>.</p>
<p id="b501-5">In this case, the Court of Special Appeals found that there was “abundant probable cause” that the car contained contraband. This finding alone satisfies the automobile exception to the Fourth Amendment’s warrant requirement, a conclusion correctly reached by the trial court when it denied respondent’s motion to suppress. The holding of the Court of Special Appeals that the “automobile exception” requires a separate finding of exigency in addition to a finding of probable cause is squarely contrary to our holdings in <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>and <em><span class="citation" data-id="9433386"><a href="/opinion/118063/pennsylvania-v-labron/" aria-description="Citation for case: Pennsylvania v. Labron">Labron</a></span>. </em>We therefore grant the petition for writ of certiorari and reverse the judgment of the Court of Special Appeals.<footnotemark>*</footnotemark></p>
<p id="b501-6">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b501-7">Justice Breyer in dissent suggests that we should not summarily reverse a judgment in a criminal case, even though he agrees with this opinion as a matter of law. But to adopt that position would simply leave it in the hands of a respondent — who had obtained a lower court judgment manifestly wrong as a matter of federal constitutional law — to avoid summary reversal by the simple expedient of refusing to file a response. While we have on occasion appointed an attorney to file a brief as <em>amicus curiae </em>in a case where we have <em>granted </em>certiorari, in order to be sure that the argued case is fully briefed, we have never done so in cases which we have summarily reversed. The reason for this is that a summary reversal does not decide any new or unanswered question of law, but simply corrects a lower court’s demonstrably erroneous application of federal law.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Maryland v. Garrison.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Maryland v. Garrison"
type: case
citation: "480 U.S. 79 (1987)"
parallel_cite: "107 S. Ct. 1013; 94 L. Ed. 2d 72; 55 U.S.L.W. 4190"
neutral_cite: 1987 U.S. LEXIS 559
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Maryland v. Garrison
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111823/maryland-v-garrison/"
  cluster_id: 111823
  opinion_id: 9430836
  identity_checked: true
homes:
  - page: "[[Particularity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Hill v. California]]", "[[Groh v. Ramirez]]", "[[Andresen v. Maryland]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "particularity", "reasonable-mistake", "overbroad-warrant"]
holding: "A warrant's validity is judged on the information reasonably available to officers when they sought it; a reasonable, good-faith mistake…"
lake:
  record_id: Maryland v. Garrison
  status: verified
  projected_at: 2026-07-06
---

# Maryland v. Garrison

*480 U.S. 79 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers obtained a warrant to search "the third floor apartment" of a building they reasonably believed contained a single unit on that floor. In fact the third floor held two apartments. Before they realized their mistake, the officers entered Garrison's apartment (not the target's) and found contraband. They stopped once they recognized the third floor was divided.

## Issue
Whether a warrant valid on its face is invalidated by a latent factual mistake about the premises, and whether the officers' good-faith execution of the warrant before discovering the error violated the Fourth Amendment.

## Rule
Warrant validity is judged on the information reasonably available when it issued: "The validity of the warrant must be assessed on the basis of the information that the officers disclosed, or had a duty to discover and to disclose, to the issuing Magistrate." — 480 U.S. at 85. ^pin-85

And execution is judged for objective reasonableness in light of the facts then known: "the validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable." — *Id.* at 88. ^pin-88

## Application
When the officers applied for the warrant, the information available to them — and reasonably discoverable — indicated a single third-floor apartment, so the warrant was valid when issued despite the later-revealed ambiguity. As the officers executed it, the objective facts (a single doorbell, mailbox, and the like) gave them no reason to know the floor was divided; their failure to appreciate the overbreadth was objectively understandable and reasonable, and they limited the search once they recognized the error. The entry into Garrison's apartment was therefore constitutional.

## Conclusion
Affirmed: a warrant valid when issued is not retroactively invalidated by a latent factual mistake, and a search executed on an objectively reasonable, honest mistake about the premises does not violate the Fourth Amendment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Garrison* applies the reasonable-mistake logic of [[Hill v. California]] to warrant execution and remains good law on warrant [[Particularity|particularity]] and objectively reasonable execution; compare the facial-[[Particularity|particularity]] failure in [[Groh v. Ramirez]].

## Appears on
- [[Particularity]] — *Key — Progeny / Refinement*

## Sources
- *Maryland v. Garrison*, 480 U.S. 79 (1987) — https://www.courtlistener.com/opinion/111823/maryland-v-garrison/ — pinpoints: 85, 88.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7f2c7c09670a78fe", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Maryland v. Garrison"}, "payload": {"all": [{"cite": "480 U.S. 79", "page": "79", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "480"}, {"cite": "107 S. Ct. 1013", "page": "1013", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "107"}, {"cite": "94 L. Ed. 2d 72", "page": "72", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "94"}, {"cite": "1987 U.S. LEXIS 559", "page": "559", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1987"}, {"cite": "55 U.S.L.W. 4190", "page": "4190", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "55"}], "display": "480 U.S. 79", "official": {"cite": "480 U.S. 79", "page": "79", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "480"}, "official_selection_present": true, "record_id": "Maryland v. Garrison"}}
{"assertion_id": "8112497b9fd6270c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-88", "record_id": "Maryland v. Garrison"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-88", "pinpoint_status": "slip-only", "quote": "the validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable.", "quote_fidelity": "mismatch", "record_id": "Maryland v. Garrison", "star_marker": null}}
{"assertion_id": "9bb94a110a81cdf0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-85", "record_id": "Maryland v. Garrison"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-85", "pinpoint_status": "slip-only", "quote": "of a building they reasonably believed contained a single unit on that floor. In fact the third floor held two apartments. Before they realized their mistake, the officers entered Garrison's apartment (not the target's) and found contraband. They stopped once they recognized the third floor was divided. ## Issue Whether a warrant valid on its face is invalidated by a latent factual mistake about the premises, and whether the officers' good-faith execution of the warrant before discovering the error violated the Fourth Amendment. ## Rule Warrant validity is judged on the information reasonably available when it issued:", "quote_fidelity": "mismatch", "record_id": "Maryland v. Garrison", "star_marker": null}}
{"assertion_id": "fc9cbf389d51b0eb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Maryland v. Garrison"}, "payload": {"as_of_content": "1987-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Maryland v. Garrison", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Maryland v. Garrison

```json
{
  "schema_version": "s2.v1",
  "record_id": "Maryland v. Garrison",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Maryland v. Garrison",
    "case_name_short": "Garrison",
    "case_name_full": "Maryland v. Garrison",
    "input_case_name": "Maryland v. Garrison",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-02-24",
    "year": 1987,
    "docket": null,
    "cluster_id": 111823,
    "lead_opinion_id": 9430836,
    "sibling_ids": [
      111823,
      9430836,
      9430837
    ],
    "absolute_url": "/opinion/111823/maryland-v-garrison/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 79",
      "volume": "480",
      "reporter": "U.S.",
      "page": "79",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1013",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 72",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4190",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 559",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "559",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 79",
        "volume": "480",
        "reporter": "U.S.",
        "page": "79",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1013",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1013",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 72",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 559",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "559",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4190",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4190",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 79",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 79",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-85",
      "page": null,
      "quote": "of a building they reasonably believed contained a single unit on that floor. In fact the third floor held two apartments. Before they realized their mistake, the officers entered Garrison's apartment (not the target's) and found contraband. They stopped once they recognized the third floor was divided. ## Issue Whether a warrant valid on its face is invalidated by a latent factual mistake about the premises, and whether the officers' good-faith execution of the warrant before discovering the error violated the Fourth Amendment. ## Rule Warrant validity is judged on the information reasonably available when it issued:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-88",
      "page": null,
      "quote": "the validity of the search of respondent's apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers' failure to realize the overbreadth of the warrant was objectively understandable and reasonable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Maryland v. Garrison",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Janvier",
          "cluster_id": 9494606,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hector Feliciano(074395)",
          "cluster_id": 3183943,
          "cite": [
            "224 N.J. 351",
            "132 A.3d 1245",
            "2016 N.J. LEXIS 229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948505,
          "cite": [
            "403 S.W.3d 867",
            "2013 Tex. Crim. App. LEXIS 531",
            "2013 WL 1136522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hamilton",
          "cluster_id": 893142,
          "cite": [
            "2012 NMCA 115",
            "3 N.M. 61"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane1_negative"
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
        "journal_ref": "Maryland v. Garrison:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
          "cluster_id": 112218,
          "cite": [
            "103 L. Ed. 2d 628",
            "109 S. Ct. 1378",
            "489 U.S. 593",
            "1989 U.S. LEXIS 1569",
            "57 U.S.L.W. 4321"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
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
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2428168,
          "cite": [
            "827 S.W.2d 937",
            "1992 Tex. Crim. App. LEXIS 83",
            "1992 WL 61756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bryan Santini v. Joseph Fuentes",
          "cluster_id": 2823503,
          "cite": [
            "795 F.3d 410",
            "2015 U.S. App. LEXIS 13552",
            "2015 WL 4620235"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockett v. State",
          "cluster_id": 1148135,
          "cite": [
            "517 So. 2d 1317",
            "1987 WL 778"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Curley v. Klem",
          "cluster_id": 1362944,
          "cite": [
            "499 F.3d 199",
            "2007 U.S. App. LEXIS 20213",
            "2007 WL 2404803"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. City of Madera",
          "cluster_id": 223714,
          "cite": [
            "648 F.3d 1119",
            "2011 U.S. App. LEXIS 17459",
            "2011 WL 3659355"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bradley",
          "cluster_id": 220050,
          "cite": [
            "644 F.3d 1213"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaime Soto, Also Known as Leonel Guerra",
          "cluster_id": 602824,
          "cite": [
            "988 F.2d 1548",
            "1993 U.S. App. LEXIS 5415",
            "1993 WL 77475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cynthia Archer v. John Chisholm",
          "cluster_id": 4422481,
          "cite": [
            "870 F.3d 603",
            "2017 WL 3709149",
            "2017 U.S. App. LEXIS 16493"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martin",
          "cluster_id": 1651199,
          "cite": [
            "721 N.W.2d 815",
            "271 Mich. App. 280"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard J. Leary, and F.L. Kleinberg & Co.",
          "cluster_id": 505922,
          "cite": [
            "846 F.2d 592",
            "1988 U.S. App. LEXIS 5755",
            "1988 WL 39811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Enrique Espinosa",
          "cluster_id": 493363,
          "cite": [
            "827 F.2d 604",
            "23 Fed. R. Serv. 963",
            "1987 U.S. App. LEXIS 12164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Riccardi",
          "cluster_id": 165743,
          "cite": [
            "405 F.3d 852",
            "2005 U.S. App. LEXIS 6631",
            "2005 WL 896430"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Maryland v. Garrison:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111823 OR 9430836 OR 9430837) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MTM0NDAwMDAwJnM9MjAxMDQ2MCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111823+OR+9430836+OR+9430837%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 6,
        "triage_snippet_classified": 194
      },
      "lane2_top_cited": {
        "query": "cites:(111823 OR 9430836 OR 9430837)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDImcz01MTgwODgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111823+OR+9430836+OR+9430837%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111823 OR 9430836 OR 9430837)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 1,
        "triage_snippet_classified": 41
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111823 OR 9430836 OR 9430837)",
    "indexed_citing_opinions": 655,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111823,
        "count": 551,
        "count_source": "search"
      },
      {
        "opinion_id": 9430836,
        "count": 120,
        "count_source": "search"
      },
      {
        "opinion_id": 9430837,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1108,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/maryland-v-garrison.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MDQwOTUmcz0xMDAxMTYzNSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111823+OR+9430836+OR+9430837%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111823,
        "cited_id": 100621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 290856,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 328845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 340572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 1513305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111823,
        "cited_id": 2379484,
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
    "date_created": "2026-07-05T11:56:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:59:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:56:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Maryland v. Garrison

```
<opinion type="majority">
<author id="b126-7">Justice Stevens</author>
<p id="Ahc">delivered the opinion of the Court.</p>
<p id="b126-8">Baltimore police officers obtained and executed a warrant to search the person of Lawrence McWebb and “the premises known as 2036 Park Avenue third floor apartment.”<footnotemark>1</footnotemark> When the police applied for the warrant and when they conducted the search pursuant to the warrant, they reasonably believed that there was only one apartment on the premises described in the warrant. In fact, the third floor was divided into two apartments, one occupied by McWebb and one by respondent Garrison. Before the officers executing the warrant became aware that they were in a separate apartment occupied by respondent, they had discovered the contraband that provided the basis for respondent’s conviction for violating Maryland’s Controlled Substances Act. The question presented is whether the seizure of that contraband was prohibited by the Fourth Amendment.</p>
<p id="b126-9">The trial court denied respondent’s motion to suppress the evidence seized from his apartment, App. 46, and the Mary<page-number citation-index="1" label="81">*81</page-number>land Court of Special Appeals affirmed. <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/" aria-description="Citation for case: Garrison v. State">58 Md. App. 417</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/" aria-description="Citation for case: Garrison v. State">473 A. 2d 514</a></span> (1984). The Court of Appeals of Maryland reversed and remanded with instructions to remand the case for a new trial. <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/" aria-description="Citation for case: Garrison v. State">303 Md. 385</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/" aria-description="Citation for case: Garrison v. State">494 A. 2d 193</a></span> (1985).</p>
<p id="b127-5">There is no question that the warrant was valid and was supported by probable cause. <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#392" aria-description="Citation for case: Garrison v. State"><em>Id., </em>at 392</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 196</a></span>. The trial court found, and the two appellate courts did not dispute, that after making a reasonable investigation, including a verification of information obtained from a reliable informant, an exterior examination of the three-story building at 2036 Park Avenue, and an inquiry of the utility company, the officer who obtained the warrant reasonably concluded that there was only one apartment on the third floor and that it was occupied by McWebb. App. 41; <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#433" aria-description="Citation for case: Garrison v. State">58 Md. App., at 433</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#522" aria-description="Citation for case: Garrison v. State">473 A. 2d, at 522</a></span>; <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#387" aria-description="Citation for case: Garrison v. State">303 Md., at 387-390</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#194" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 194-195</a></span>. When six Baltimore police officers executed the warrant, they fortuitously encountered McWebb in front of the building and used his key to gain admittance to the first-floor hallway and to the locked door at the top of the stairs to the third floor. As they entered the vestibule on the third floor, they encountered respondent, who was standing in the hallway area. The police could see into the interior of both Mc-Webb’s apartment to the left and respondent’s to the right, for the doors to both were open. Only after respondent’s apartment had been entered and heroin, cash, and drug paraphernalia had been found did any of the officers realize that the third floor contained two apartments. App. 41-46. As soon as they became aware of that fact, the search was discontinued. <em>Id., </em>at 32, 39. All of the officers reasonably believed that they were searching McWebb’s apartment.<footnotemark>2</footnotemark> No further search of respondent’s apartment was made.</p>
<p id="b128-4"><page-number citation-index="1" label="82">*82</page-number>The matter on which there is a difference of opinion concerns the proper interpretation of the warrant. A literal reading of its plain language, as well as the language used in the application for the warrant, indicates that it was intended to authorize a search of the entire third floor.<footnotemark>3</footnotemark> This is the construction adopted by the intermediate appellate court, see <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#419" aria-description="Citation for case: Garrison v. State">58 Md. App., at 419</a></span>, <span class="citation" data-id="2379484"><a href="/opinion/2379484/garrison-v-state/#515" aria-description="Citation for case: Garrison v. State">473 A. 2d, at 515</a></span>, and it also appears to be the construction adopted by the trial judge. See App. 41. One sentence in the trial judge’s oral opinion, however, lends support to the construction adopted by the Court of Appeals, namely, that the warrant authorized a search of McWebb’s apartment only.<footnotemark>4</footnotemark> Under that interpretation, the Court of <page-number citation-index="1" label="83">*83</page-number>Appeals concluded that the warrant did not authorize the search of respondent’s apartment and the police had no justification for making a warrantless entry into his premises.<footnotemark>5</footnotemark></p>
<p id="b129-4">The opinion of the Maryland Court of Appeals relies on Article 26 of the Maryland Declaration of Rights<footnotemark>6</footnotemark> and Maryland cases as well as the Fourth Amendment to the Federal Constitution and federal cases. Rather than containing any “plain statement” that the decision rests upon adequate and independent state grounds, see <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1042" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1042</a></span> (1983), the opinion indicates that the Maryland constitutional provision is construed <em>in pari materia </em>with the</p>
<p id="b130-7"><page-number citation-index="1" label="84">*84</page-number>Fourth Amendment.<footnotemark>7</footnotemark> We therefore have jurisdiction. Because the result that the Court of Appeals reached did not appear to be required by the Fourth Amendment, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./475/1009/">475 U. S. 1009</a></span> (1986). We reverse.</p>
<p id="b130-8">In our view, the case presents two separate constitutional issues, one concerning the validity of the warrant and the other concerning the reasonableness of the manner in which it was executed. See <em>Dalia </em>v. <em>United States, </em><span class="citation" data-id="9427537"><a href="/opinion/110061/dalia-v-united-states/#258" aria-description="Citation for case: Dalia v. United States">441 U. S. 238, 258</a></span> (1979). We shall discuss the questions separately.</p>
<p id="b130-9">I-H</p>
<p id="b130-3">The Warrant Clause of the Fourth Amendment categorically prohibits the issuance of any warrant except one “particularly describing the place to be searched and the persons or things to be seized.” The manifest purpose of this particularity requirement was to prevent general searches. By limiting the authorization to search to the specific areas and things for which there is probable cause to search, the requirement ensures that the search will be carefully tailored to its justifications, and will not take on the character of the wide-ranging exploratory searches the Framers intended to prohibit.<footnotemark>8</footnotemark> Thus, the scope of a lawful search is “defined by the object of the search and the places in which there is probable cause to believe that it may be found. Just as probable cause to believe that a stolen lawnmower may be found in a garage will not support a warrant to search an upstairs bedroom, probable cause to believe that undocumented aliens are being transported in a van will not justify a warrantless <page-number citation-index="1" label="85">*85</page-number>search of a suitcase.” <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824</a></span> (1982).</p>
<p id="b131-5">In this case there is no claim that the “persons or things to be seized” were inadequately described or that there was no probable cause to believe that those things might be found in “the place to be searched” as it was described in the warrant. With the benefit of hindsight, however, we now know that the description of that place was broader than appropriate because it was based on the mistaken belief that there was only one apartment on the third floor of the building at 2036 Park Avenue. The question is whether that factual mistake invalidated a warrant that undoubtedly would have been valid if it had reflected a completely accurate understanding of the building’s floor plan.</p>
<p id="b131-6">Plainly, if the officers had known, or even if they should have known, that there were two separate dwelling units on the third floor of 2036 Park Avenue, they would have been obligated to exclude respondent’s apartment from the scope of the requested warrant. But we must judge the constitutionality of their conduct in light of the information available to them at the time they acted. Those items of evidence that emerge after the warrant is issued have no bearing on whether or not a warrant was validly issued.<footnotemark>9</footnotemark> Just as the discovery of contraband cannot validate a warrant invalid when issued, so is it equally clear that the discovery of facts demonstrating that a valid warrant was unnecessarily broad does not retroactively invalidate the warrant. The validity of the warrant must be assessed on the basis of the information that the officers disclosed, or had a duty to discover and to disclose, to the issuing Magistrate.<footnotemark>10</footnotemark> On the basis of that <page-number citation-index="1" label="86">*86</page-number>information, we agree with the conclusion of all three Maryland courts that the warrant, insofar as it authorized a search that turned out to be ambiguous in scope, was valid when it issued.</p>
<p id="b132-5">II</p>
<p id="b132-6">The question whether the execution of the warrant violated respondent’s constitutional right to be secure in his home is somewhat less clear. We have no difficulty concluding that the officers’ entry into the third-floor common area was legal; they carried a warrant for those premises, and they were accompanied by McWebb, who provided the key that they used to open the door giving access to the third-floor common area. If the officers had known, or should have known, that the third floor contained two apartments before they entered the living quarters on the third floor, and thus had been aware of the error in the warrant, they would have been obligated to limit their search to McWebb’s apart<page-number citation-index="1" label="87">*87</page-number>ment. Moreover, as the officers recognized, they were required to discontinue the search of respondent’s apartment as soon as they discovered that there were two separate units on the third floor and therefore were put on notice of the risk that they might be in a unit erroneously included within the terms of the warrant. The officers’ conduct and the limits of the search were based on the information available as the search proceeded. While the purposes justifying a police search strictly limit the permissible extent of the search, the Court has also recognized the need to allow some latitude for honest mistakes that are made by officers in the dangerous and difficult process of making arrests and executing search warrants.<footnotemark>11</footnotemark></p>
<p id="b133-5">In <em>Hill </em>v. <em>California, </em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), we considered the validity of the arrest of a man named Miller based on the mistaken belief that he was Hill. The police had probable cause to arrest Hill and they in good faith believed that Miller was Hill when they found him in Hill’s apartment. As we explained:</p>
<blockquote id="b133-6">“The upshot was that the officers in good faith believed Miller was Hill and arrested him. They Were quite wrong as it turned out, and subjective good-faith belief would not in itself justify either the arrest or the subsequent search. But sufficient probability, not certainty, is the touchstone of reasonableness under the Fourth Amendment and on the record before us the officers’ mistake was understandable and the arrest a reasonable response to the situation facing them at the time.” <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#803" aria-description="Citation for case: Hill v. California"><em>Id., </em>at 803-804</a></span>.</blockquote>
<p id="b133-7">While <em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">Hill</a></span> </em>involved an arrest without a warrant, its underlying rationale that an officer’s reasonable misidentification <page-number citation-index="1" label="88">*88</page-number>of a person does not invalidate a valid arrest is equally applicable to an officer’s reasonable failure to appreciate that a valid warrant describes too broadly the premises to be searched. Under the reasoning in <em><span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">Hill</a></span>, </em>the validity of the search of respondent’s apartment pursuant to a warrant authorizing the search of the entire third floor depends on whether the officers’ failure to realize the overbreadth of the warrant was objectively understandable and reasonable. Here it unquestionably was. The objective facts available to the officers at the time suggested no distinction between McWebb’s apartment and the third-floor premises.<footnotemark>12</footnotemark></p>
<p id="b134-5">For that reason, the officers properly responded to the command contained in a valid warrant even if the warrant is interpreted as authorizing a search limited to McWebb’s apartment rather than the entire third floor. Prior to the officers’ discovery of the factual mistake, they perceived McWebb’s apartment and the third-floor premises as one and the same; therefore their execution of the warrant reasonably included the entire third floor.<footnotemark>13</footnotemark> Under either interpretation of the warrant, the officers’ conduct was consistent with a reasonable effort to ascertain and identify the place intended to be searched within the meaning of the Fourth Amend<page-number citation-index="1" label="89">*89</page-number>ment.<footnotemark>14</footnotemark> Cf. <em>Steele </em>v. <em>United States, </em><span class="citation" data-id="100621"><a href="/opinion/100621/steele-v-united-states-no-1/#503" aria-description="Citation for case: Steele v. United States No. 1">267 U. S. 498, 503</a></span> (1925).</p>
<p id="b135-4">The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b135-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b126-11"><em> </em>App. 9, 41. The warrant was issued and executed on May 21, 1982. It authorized the Baltimore police to search the person of McWebb and “the premises known as 2036 Park Avenue third floor apartment” for “Marihuana, related paraphernalia, minies, books, papers, and photographs pertaining to the illegal distribution of Marihuana . . . .” <em>Id., </em>at 9.</p>
</footnote>
<footnote label="2">
<p id="b127-6"> While the search was in progress, an officer in respondent’s apartment answered the telephone. The caller asked for “Red Cross”; that was the name by which McWebb was known to the confidential informant. <em>Id., </em>at 6. Neither respondent nor McWebb indicated to the police during the search that there were two apartments. <em>Id., </em>at 38, 39-40.</p>
</footnote>
<footnote label="3">
<p id="b128-5"> The warrant states:</p>
<blockquote id="b128-6">“Affidavit having been made before me by Detective Albert Marcus, Baltimore Police Department, Narcotic Unit, that he has reason to believe that on the person of Lawrence Meril McWebb . . . [and] that on the premises known as 2036 Park Avenue third floor apartment, described as a three story brick dwelling with the numerals 2-0-3-6 affixed to the front of same in the City of Baltimore, there is now being concealed certain property ....</blockquote>
<blockquote id="b128-7">“You are therefor commanded, with the necessary and proper assistants, to search forthwith the person/premises hereinabove described for the property specified, executing this warrant and making the search . . . .” <em>Id., </em>at 9.</blockquote>
</footnote>
<footnote label="4">
<p id="b128-8"> Immediately before ruling on the suppression motions made by McWebb and Garrison, the court observed that a search of two or more apartments in the same building must be supported by probable cause for searching each apartment. The court added, “[t]here is an exception to this general rule where the multiple unit character of the premises is not externally apparent and is not known to the officer applying for or executing the warrant.” <em>Id., </em>at 45. The trial court then ruled, “It is clear that the warrant specified the premises to be searched as the third floor apartment of the Defendant McWebb . . . .” <em>Id., at </em>46. This statement only makes sense as a rejection of Garrison’s claim that “the warrant was a general warrant as it did not specify which apartment was to be searched on the third floor,” <em>id., </em>at 40, and as a recognition that the search was not invalid for lack of specificity in the warrant as to the premises to be searched. We interpret the trial court’s statement as a ruling that the search of a subunit of the building — which he referred to as “the third floor <page-number citation-index="1" label="83">*83</page-number>apartment of the Defendant McWebb” — was authorized by the warrant. The court then found on the precise facts of this ease that the search of Garrison’s apartment was valid because “the officers did not know that there was more than one apartment on the third floor and nothing alerted them of such a fact until after the search had been made and the items were [seized].” <em>Id., </em>at 46. The contrary construction adopted by the Court of Appeals fails to take into account the plain language of the warrant, which authorized a search of the person of McWebb and of the premises of 2036 Park Avenue, third floor. <em>Id., </em>at 9.</p>
</footnote>
<footnote label="5">
<p id="b129-9"> As the Court of Appeals explained:</p>
<blockquote id="b129-10">“It is undisputed that the police were authorized to search only one apartment, MeWebb’s; the warrant did not authorize the search of Garrison’s apartment. There is no question as to the validity of the search warrant itself. No argument was made in this Court that any of the exceptions to the warrant requirement applied here. It is clear, therefore, that the police had no authority to cross the threshold of Garrison’s apartment and seize evidence.</blockquote>
<blockquote id="b129-11">“Police had a warrant to search MeWebb’s apartment. They had no warrant to search Garrison’s. They had no justification for entering his premises, regardless of appearances.” <span class="citation no-link">303 Md. 386</span>, 392r394, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, 193, 196-197</a></span> (1985).</blockquote>
</footnote>
<footnote label="6">
<p id="b129-12"> Article 26 of the Maryland Declaration of Rights provides:</p>
<blockquote id="b129-13">“That all warrants, without oath or affirmation, to search suspected places, or to seize any person or property, are grevious [grievous] and oppressive; and all general warrants to search suspected places, or to apprehend suspected persons, without naming or describing the place, or the person in special, are illegal, and ought not to be granted.”</blockquote>
</footnote>
<footnote label="7">
<p id="b130-4"> <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#391" aria-description="Citation for case: Garrison v. State">303 Md., at 391</a></span>, <span class="citation" data-id="2381242"><a href="/opinion/2381242/garrison-v-state/#196" aria-description="Citation for case: Garrison v. State">494 A. 2d, at 196</a></span>. This statement indicates that the “state court decision fairly appears to rest primarily on federal law, or to be interwoven with the federal law . . . .” <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S., at 1040</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b130-5"> See <em>Andresen </em>v. <em>Maryland, </em><span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#480" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 480</a></span> (1976); <em>Stanley </em>v. <em>Georgia, </em><span class="citation" data-id="9423992"><a href="/opinion/107898/stanley-v-georgia/#569" aria-description="Citation for case: Stanley v. Georgia">394 U. S. 557, 569-572</a></span> (1969) (Stewart, J., concurring in result); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482, 485</a></span> (1965); <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931); <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#195" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 195-196</a></span> (1927).</p>
</footnote>
<footnote label="9">
<p id="b131-7"> Cf. <em>United States </em>v. <em>Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#115" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 115</a></span> (1984) (warrantless test of white powder; “[t]he reasonableness of an official invasion of the citizen’s privacy must be appraised on the basis of the facts as they existed at the time that invasion occurred”).</p>
</footnote>
<footnote label="10">
<p id="b131-8">Arguments can certainly be made that the police in this case should have been able to ascertain that there was more than one apartment on the <page-number citation-index="1" label="86">*86</page-number>third floor of this building. It contained seven separate dwelling units and it was surely possible that two of them might be on the third floor. But the record also establishes that Officer Marcus made specific inquiries to determine the identity of the occupants of the third-floor premises. The officer went to 2036 Park Avenue and found that it matched the description given by the informant: a three-story brick dwelling with the numerals 2-0-3-6 affixed to the front of the premises. App. 7. The officer “made a cheek with the Baltimore Gas and Electric Company and discovered that the premises of 2036 Park Ave. third floor was in the name of Lawrence McWebb.” <em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Ibid.</a></span> </em>Officer Marcus testified at the suppression hearing that he inquired of the Baltimore Gas and Electric Company in whose name the third floor apartment was listed: “I asked if there is a front or rear or middle room. They told me, one third floor was only listed to Lawrence McWebb.” <em>Id., </em>at 36-38. The officer also discovered from a check with the Baltimore Police Department that the police records of Lawrence McWebb matched the address and physical description given by the informant. <em>Id., </em>at 7. The Maryland courts that are presumptively familiar with local conditions were unanimous in concluding that the officer reasonably believed McWebb was the only tenant on that floor. Because the evidence supports their conclusion, we accept that conclusion for the purpose of our decision.</p>
</footnote>
<footnote label="11">
<p id="b133-8"> “Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949).</p>
</footnote>
<footnote label="12">
<p id="b134-6"> Nothing McWebb did or said after he was detained outside 2036 Park Avenue would have suggested to the police that there were two apartments on the third floor. McWebb provided the key that opened the doors on the first floor and on the third floor. The police could reasonably have believed that McWebb was admitting them to an undivided apartment on the third floor. When the officers entered the foyer on the third floor, neither McWebb nor Garrison informed them that they lived in separate apartments. App. 39-40, 42.</p>
</footnote>
<footnote label="13">
<p id="b134-7"> We expressly distinguish the facts of this case from a situation in which the police know there are two apartments on a certain floor of a building, and have probable cause to believe that drugs are being sold out of that floor, but do not know in which of the two apartments the illegal transactions are taking place. A search pursuant to a warrant authorizing a search of the entire floor under those circumstances would present quite different issues from the ones before us in this case.</p>
</footnote>
<footnote label="14">
<p id="b135-8"> Respondent argued that the execution of the warrant violated the Fourth Amendment at the moment when the officers “walked in through that threshold of that house . . . .” Tr. ofOralArg. 35. At another point respondent argued that the search was illegal at the point when the police went through Garrison’s apartment without probable cause for his apartment. <em>Id., </em>at 43. For the purpose of addressing respondent’s argument, the exact point at which he asserts the search became illegal is not essential. Whether the illegal threshold is viewed as the beginning of the entire premises or as the beginning of those premises that, upon closer examination, turn out to be excluded from the intended scope of the warrant, we cannot accept respondent’s argument. It would brand as illegal the execution of any warrant in which, due to a mistake in fact, the premises intended to be searched vary from their description in the warrant. Yet in this case, in which the mistake in fact does not invalidate the warrant precisely because the police do not know of the mistake in fact when they apply for, receive, and prepare to execute the warrant, the police cannot reasonably know prior to their search that the warrant rests on a mistake in fact. It is only after the police begin to execute the warrant and set foot upon the described premises that they will discover the factual mistake and must reasonably limit their search accordingly.</p>
<p id="b135-9">Respondent proposes that the police conduct a preliminary survey of the premises whenever they search a building in which there are multiple dwelling units, in order to determine the extent of the premises to be searched. Id., at 42. We find no persuasive reason to impose such a burden over and above the bedrock requirement that, with the exceptions we have traced in our cases, the police may conduct searches only pursuant to a reasonably detailed warrant.</p>
</footnote>
</opinion>
```

---
