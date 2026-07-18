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

## GROUP: content/cases/Grady v. North Carolina.md  (`case`, 5 assertions)

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
{"assertion_id": "f1aada8762b5558d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "575 U.S. 306 (2015)", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 2124", "official_citation_present": true, "parallel_cite": "135 S. Ct. 1368; 191 L. Ed. 2d 459; 83 U.S.L.W. 4226; 25 Fla. L. Weekly Fed. S 181", "title": "Grady v. North Carolina", "year": "2015"}}
{"assertion_id": "730dc9d9248c50e7", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Anchor", "title": "Grady v. North Carolina"}}
{"assertion_id": "ec57ab9574b0f228", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A State conducts a Fourth Amendment search when it attaches a satellite-based monitoring device to a person's body, without consent, to track his movements; the civil character of the monitoring program does not remove the conduct from the Fourth Amendment, leaving only the reasonableness of the search for decision on remand.", "title": "Grady v. North Carolina"}}
{"assertion_id": "409c00cf12be3519", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Grady v. North Carolina"}}
{"assertion_id": "cd58fcb15674111a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Grady v. North Carolina", "varies_by_point": "false"}}
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

## GROUP: content/cases/Graham v. Connor.md  (`case`, 5 assertions)

### content_page

```
---
title: "Graham v. Connor"
type: case
citation: "490 U.S. 386 (1989)"
parallel_cite: "109 S. Ct. 1865; 104 L. Ed. 2d 443; 57 U.S.L.W. 4513"
neutral_cite: 1989 U.S. LEXIS 2467
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-05-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Graham v. Connor
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112257/graham-v-connor/"
  cluster_id: 112257
  opinion_id: 112257
  identity_checked: true
homes:
  - page: "[[Use of Force]]"
    role: "Key — Anchor"
related: ["[[Tennessee v. Garner]]", "[[Scott v. Harris]]", "[[Saucier v. Katz]]"]
aliases: []
tags: ["case", "fourth-amendment", "excessive-force", "section-1983", "objective-reasonableness", "seizure"]
holding: "Excessive-force § 1983 claims arising from an arrest, stop, or other seizure are analyzed under the Fourth Amendment's 'objective…"
lake:
  record_id: Graham v. Connor
  status: verified
  projected_at: 2026-07-09
---

# Graham v. Connor

*490 U.S. 386 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Graham, a diabetic, asked a friend to drive him to a store for orange juice to counter an insulin reaction. Seeing Graham hurry in and out, Officer Connor made an investigative stop. During the encounter officers handcuffed Graham, disregarded explanations about his diabetic condition, and used force that caused injuries. Graham sued under § 1983 for excessive force. The lower courts analyzed the claim under a substantive-due-process "good faith / malicious and sadistic" test drawn from *[[Johnson v. Glick]]*.

## Issue
What constitutional standard governs a § 1983 claim that law enforcement officers used excessive force in the course of an arrest, investigatory stop, or other seizure.

## Rule
Such claims are governed by the Fourth Amendment's objective-reasonableness standard, not substantive due process. "[A]ll claims that law enforcement officers have used excessive force — deadly or not — in the course of an arrest, investigatory stop, or other 'seizure' of a free citizen should be analyzed under the Fourth Amendment and its 'reasonableness' standard, rather than under a 'substantive due process' approach." — 490 U.S. at 395. ^pin-395

Reasonableness is judged objectively and from the officer's on-scene vantage: "The 'reasonableness' of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight." — *Id.* at 396. ^pin-396

The inquiry weighs the facts of each case, "including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight." — [*Id.*](https://www.courtlistener.com/opinion/112257/graham-v-connor/#:~:text=including%20the%20severity%20of%20the) ^pin-396a

## Application
Graham's claim arose from an investigatory stop and the force used during it — a Fourth Amendment "seizure" — so it had to be assessed under the objective-reasonableness standard rather than the *[[Johnson v. Glick]]* due-process test the Court of Appeals applied. Because the lower courts used a standard turning on the officers' subjective good or bad faith, the case was [[Reading and Citing Cases#on-remand|remanded]] for analysis under the proper Fourth Amendment framework.

## Conclusion
Excessive-force claims arising from a seizure are governed by Fourth Amendment objective reasonableness; the judgment applying a substantive-due-process test was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Graham*'s objective-reasonableness standard and three-factor balancing govern excessive-force claims and frame the merits question in qualified-immunity analysis; it builds on [[Tennessee v. Garner]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Graham v. Connor*, 490 U.S. 386 (1989) — https://www.courtlistener.com/opinion/112257/graham-v-connor/ — pinpoints: 395, 396.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4de19d357ca500d7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "490 U.S. 386 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 2467", "official_citation_present": true, "parallel_cite": "109 S. Ct. 1865; 104 L. Ed. 2d 443; 57 U.S.L.W. 4513", "title": "Graham v. Connor", "year": "1989"}}
{"assertion_id": "5a3c1b9b1e9dfc18", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Excessive-force § 1983 claims arising from an arrest, stop, or other seizure are analyzed under the Fourth Amendment's 'objective…", "title": "Graham v. Connor"}}
{"assertion_id": "6f933ad0970f9019", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Key — Anchor", "title": "Graham v. Connor"}}
{"assertion_id": "b12ce029f4d1e8b4", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-05-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Graham v. Connor", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Graham v. Connor", "varies_by_point": "false"}}
{"assertion_id": "c5ff6e5db2bfd407", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Graham v. Connor"}}
```

### lake record — Graham v. Connor

```json
{
  "schema_version": "s2.v1",
  "record_id": "Graham v. Connor",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Graham v. Connor",
    "case_name_short": "Graham",
    "case_name_full": "GRAHAM v. CONNOR Et Al.",
    "input_case_name": "Graham v. Connor",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-05-15",
    "year": 1989,
    "docket": null,
    "cluster_id": 112257,
    "lead_opinion_id": 112257,
    "sibling_ids": [
      112257,
      9431666,
      9431667
    ],
    "absolute_url": "/opinion/112257/graham-v-connor/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9083940,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083939,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083419,
        "score": 20,
        "case_name": "Graham v. Connor"
      },
      {
        "cluster_id": 9083418,
        "score": 20,
        "case_name": "Graham v. Connor"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "490 U.S. 386",
      "volume": "490",
      "reporter": "U.S.",
      "page": "386",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1865",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 443",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4513",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4513",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 2467",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2467",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "490 U.S. 386",
        "volume": "490",
        "reporter": "U.S.",
        "page": "386",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1865",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1865",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 L. Ed. 2d 443",
        "volume": "104",
        "reporter": "L. Ed. 2d",
        "page": "443",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 2467",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "2467",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4513",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4513",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "490 U.S. 386",
    "official_selection": {
      "court_class": "scotus",
      "selected": "490 U.S. 386",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-395",
      "page": null,
      "quote": "test drawn from *Johnson v. Glick*. ## Issue What constitutional standard governs a \u00a7 1983 claim that law enforcement officers used excessive force in the course of an arrest, investigatory stop, or other seizure. ## Rule Such claims are governed by the Fourth Amendment's objective-reasonableness standard, not substantive due process.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-396",
      "page": null,
      "quote": "The 'reasonableness' of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-396a",
      "page": null,
      "quote": "including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight.",
      "star_marker": "396",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19548,
      "fragment": "#:~:text=including%20the%20severity%20of%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Graham v. Connor",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
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
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Seiter",
          "cluster_id": 112626,
          "cite": [
            "115 L. Ed. 2d 271",
            "111 S. Ct. 2321",
            "501 U.S. 294",
            "1991 U.S. LEXIS 3490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tolan v. Cotton",
          "cluster_id": 2672535,
          "cite": [
            "188 L. Ed. 2d 895",
            "134 S. Ct. 1861",
            "2014 U.S. LEXIS 3112",
            "82 U.S.L.W. 4358",
            "572 U.S. 650",
            "88 Fed. R. Serv. 3d 765",
            "24 Fla. L. Weekly Fed. S 731",
            "2014 WL 1757856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kingsley v. Hendrickson",
          "cluster_id": 2811847,
          "cite": [
            "576 U.S. 389",
            "135 S. Ct. 2466",
            "192 L. Ed. 2d 416",
            "2015 U.S. LEXIS 4073",
            "25 Fla. L. Weekly Fed. S 401",
            "83 U.S.L.W. 4515"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koon v. United States",
          "cluster_id": 118044,
          "cite": [
            "135 L. Ed. 2d 392",
            "116 S. Ct. 2035",
            "518 U.S. 81",
            "1996 U.S. LEXIS 3877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City of Los Angeles",
          "cluster_id": 7092482,
          "cite": [
            "250 F.3d 668",
            "2001 WL 468408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brosseau v. Haugen",
          "cluster_id": 137736,
          "cite": [
            "160 L. Ed. 2d 583",
            "125 S. Ct. 596",
            "543 U.S. 194",
            "2004 U.S. LEXIS 8275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
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
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thaddeus-X and Earnest Bell, Jr. v. Blatter",
          "cluster_id": 763587,
          "cite": [
            "175 F.3d 378",
            "1999 U.S. App. LEXIS 3497",
            "1999 WL 114379"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Pauly",
          "cluster_id": 4374579,
          "cite": [
            "580 U.S. 73",
            "196 L. Ed. 2d 463",
            "2017 U.S. LEXIS 5",
            "137 S. Ct. 548",
            "26 Fla. L. Weekly Fed. S 409",
            "85 U.S.L.W. 4027",
            "2017 WL 69170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. City Of Los Angeles",
          "cluster_id": 773312,
          "cite": [
            "250 F.3d 668",
            "2001 Cal. Daily Op. Serv. 3507",
            "2001 Daily Journal DAR 4351",
            "56 Fed. R. Serv. 698",
            "2001 U.S. App. LEXIS 8150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Christopher J. Weiland v. Palm Beach County Sheriff's Office",
          "cluster_id": 2815299,
          "cite": [
            "792 F.3d 1313",
            "92 Fed. R. Serv. 3d 378",
            "2015 U.S. App. LEXIS 11750",
            "2015 WL 4098270"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathon Castro v. County of Los Angeles",
          "cluster_id": 4247081,
          "cite": [
            "833 F.3d 1060",
            "2016 U.S. App. LEXIS 14950",
            "2016 WL 4268955"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lanier",
          "cluster_id": 118098,
          "cite": [
            "137 L. Ed. 2d 432",
            "117 S. Ct. 1219",
            "520 U.S. 259",
            "1997 U.S. LEXIS 2079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Allen King v. Eric Taylor",
          "cluster_id": 808337,
          "cite": [
            "694 F.3d 650",
            "2012 WL 3968371",
            "2012 U.S. App. LEXIS 19109"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy v. Freshwater",
          "cluster_id": 177179,
          "cite": [
            "623 F.3d 90",
            "2010 U.S. App. LEXIS 21238",
            "2010 WL 4008747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
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
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Graham v. Connor:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112257 OR 9431666 OR 9431667) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzA2ODMyMDAwMDAwJnM9OTQ3MTU4NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(112257 OR 9431666 OR 9431667)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDI4JnM9MjgwMTQzNSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112257 OR 9431666 OR 9431667)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzI4MzQ1NjAwMDAwJnM9MTAxMzE3NjMmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112257 OR 9431666 OR 9431667)",
    "indexed_citing_opinions": 5378,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112257,
        "count": 4465,
        "count_source": "search"
      },
      {
        "opinion_id": 9431666,
        "count": 1007,
        "count_source": "search"
      },
      {
        "opinion_id": 9431667,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 16638,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/graham-v-connor.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjY2MDU5MSZzPTg3MTI4MzImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28112257+OR+9431666+OR+9431667%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112257,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110075,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 312370,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 459830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 493625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 498147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112257,
        "cited_id": 1558828,
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
    "date_created": "2026-07-05T05:51:56Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:55:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:52:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Graham v. Connor

```
<div>
<center><b><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U.S. 386</a></span> (1989)</b></center>
<center><h1>GRAHAM<br>
v.<br>
CONNOR ET AL.</h1></center>
<center>No. 87-6571.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 21, 1989</center>
<center>Decided May 15, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FOURTH CIRCUIT
<p><span class="star-pagination">*388</span> <i>H. Gerald Beaver</i> argued the cause for petitioner. On the briefs was <i>Richard B. Glazier.</i></p>
<p><i>Mark I. Levy</i> argued the cause for respondents. On the brief was <i>Frank B. Aycock III.</i><sup>[*]</sup></p>
<p><i>Lacy H. Thornburg,</i> Attorney General of North Carolina, <i>Isaac T. Avery III,</i> Special Deputy Attorney General, and <i>Linda Anne Morris,</i> Assistant Attorney General, filed a brief for the State of North Carolina as <i>amicus curiae</i> urging affirmance.</p>
<p>CHIEF JUSTICE REHNQUIST delivered the opinion of the Court.</p>
<p>This case requires us to decide what constitutional standard governs a free citizen's claim that law enforcement officials used excessive force in the course of making an arrest, investigatory stop, or other "seizure" of his person. We hold that such claims are properly analyzed under the Fourth Amendment's "objective reasonableness" standard, rather than under a substantive due process standard.</p>
<p>In this action under <span class="citation no-link">42 U. S. C. § 1983</span>, petitioner Dethorne Graham seeks to recover damages for injuries allegedly sustained when law enforcement officers used physical force against him during the course of an investigatory stop. Because the case comes to us from a decision of the Court of Appeals affirming the entry of a directed verdict for respondents, we take the evidence hereafter noted in the light most favorable to petitioner. On November 12, 1984, Graham, a diabetic, felt the onset of an insulin reaction. He asked a friend, William Berry, to drive him to a nearby convenience store so he could purchase some orange juice to counteract the reaction. Berry agreed, but when Graham entered the store, he saw a number of people ahead of him in the checkout <span class="star-pagination">*389</span> line. Concerned about the delay, he hurried out of the store and asked Berry to drive him to a friend's house instead.</p>
<p>Respondent Connor, an officer of the Charlotte, North Carolina, Police Department, saw Graham hastily enter and leave the store. The officer became suspicious that something was amiss and followed Berry's car. About one-half mile from the store, he made an investigative stop. Although Berry told Connor that Graham was simply suffering from a "sugar reaction," the officer ordered Berry and Graham to wait while he found out what, if anything, had happened at the convenience store. When Officer Connor returned to his patrol car to call for backup assistance, Graham got out of the car, ran around it twice, and finally sat down on the curb, where he passed out briefly.</p>
<p>In the ensuing confusion, a number of other Charlotte police officers arrived on the scene in response to Officer Connor's request for backup. One of the officers rolled Graham over on the sidewalk and cuffed his hands tightly behind his back, ignoring Berry's pleas to get him some sugar. Another officer said: "I've seen a lot of people with sugar diabetes that never acted like this. Ain't nothing wrong with the M. F. but drunk. Lock the S. B. up." App. 42. Several officers then lifted Graham up from behind, carried him over to Berry's car, and placed him face down on its hood. Regaining consciousness, Graham asked the officers to check in his wallet for a diabetic decal that he carried. In response, one of the officers told him to "shut up" and shoved his face down against the hood of the car. Four officers grabbed Graham and threw him headfirst into the police car. A friend of Graham's brought some orange juice to the car, but the officers refused to let him have it. Finally, Officer Connor received a report that Graham had done nothing wrong at the convenience store, and the officers drove him home and released him.</p>
<p><span class="star-pagination">*390</span> At some point during his encounter with the police, Graham sustained a broken foot, cuts on his wrists, a bruised forehead, and an injured shoulder; he also claims to have developed a loud ringing in his right ear that continues to this day. He commenced this action under <span class="citation no-link">42 U. S. C. § 1983</span> against the individual officers involved in the incident, all of whom are respondents here,<sup>[1]</sup> alleging that they had used excessive force in making the investigatory stop, in violation of "rights secured to him under the Fourteenth Amendment to the United States Constitution and <span class="citation no-link">42 U. S. C. § 1983</span>." Complaint ¶ 10, App. 5.<sup>[2]</sup> The case was tried before a jury. At the close of petitioner's evidence, respondents moved for a directed verdict. In ruling on that motion, the District Court considered the following four factors, which it identified as "[t]he factors to be considered in determining when the excessive use of force gives rise to a cause of action under § 1983": (1) the need for the application of force; (2) the relationship between that need and the amount of force that was used; (3) the extent of the injury inflicted; and (4) "[w]hether the force was applied in a good faith effort to maintain and restore discipline or maliciously and sadistically for the very purpose of causing harm." <span class="citation" data-id="1558828"><a href="/opinion/1558828/graham-v-city-of-charlotte/#248" aria-description="Citation for case: Graham v. City of Charlotte">644 F. Supp. 246, 248</a></span> (WDNC 1986). Finding that the amount of force used by the officers was "appropriate under the circumstances," that "[t]here was no discernable injury inflicted," and that the force used "was not applied maliciously or sadistically for the very purpose of causing harm," but in "a good faith effort to maintain or restore order in the face of a potentially explosive <span class="star-pagination">*391</span> situation." <span class="citation" data-id="1558828"><a href="/opinion/1558828/graham-v-city-of-charlotte/#248" aria-description="Citation for case: Graham v. City of Charlotte"><i>id.,</i> at 248-249</a></span>, the District Court granted respondents' motion for a directed verdict.</p>
<p>A divided panel of the Court of Appeals for the Fourth Circuit affirmed. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d 945</a></span> (1987). The majority ruled first that the District Court had applied the correct legal standard in assessing petitioner's excessive force claim. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 948-949</a></span>. Without attempting to identify the specific constitutional provision under which that claim arose,<sup>[3]</sup> the majority endorsed the four-factor test applied by the District Court as generally applicable to all claims of "constitutionally excessive force" brought against governmental officials. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 948</a></span>. The majority rejected petitioner's argument, based on Circuit precedent,<sup>[4]</sup> that it was error to require him to prove that the allegedly excessive force used against him was applied "maliciously and sadistically for the very purpose of causing harm."<sup>[5]</sup><i><span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">Ibid.</a></span></i> Finally, the majority held that a reasonable jury applying the four-part test it had just endorsed <span class="star-pagination">*392</span> to petitioner's evidence "could not find that the force applied was constitutionally excessive." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#949" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>Id.,</i> at 949-950</a></span>. The dissenting judge argued that this Court's decisions in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), required that excessive force claims arising out of investigatory stops be analyzed under the Fourth Amendment's "objective reasonableness" standard. <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#950" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 950-952</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./488/816/">488 U. S. 816</a></span> (1988), and now reverse.</p>
<p>Fifteen years ago, in <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">481 F. 2d 1028</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1033/">414 U. S. 1033</a></span> (1973), the Court of Appeals for the Second Circuit addressed a § 1983 damages claim filed by a pretrial detainee who claimed that a guard had assaulted him without justification. In evaluating the detainee's claim, Judge Friendly applied neither the Fourth Amendment nor the Eighth, the two most textually obvious sources of constitutional protection against physically abusive governmental conduct.<sup>[6]</sup> Instead, he looked to "substantive due process," holding that "quite apart from any `specific' of the Bill of Rights, application of undue force by <span class="star-pagination">*393</span> law enforcement officers deprives a suspect of liberty without due process of law." <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. As support for this proposition, he relied upon our decision in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span> (1952), which used the Due Process Clause to void a state criminal conviction based on evidence obtained by pumping the defendant's stomach. <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032-1033</a></span>. If a police officer's use of force which "shocks the conscience" could justify setting aside a criminal conviction, Judge Friendly reasoned, a correctional officer's use of similarly excessive force must give rise to a due process violation actionable under § 1983. <i>Ibid.</i> Judge Friendly went on to set forth four factors to guide courts in determining "whether the constitutional line has been crossed" by a particular use of force  the same four factors relied upon by the courts below in this case. <i>Id.,</i> at 1033.</p>
<p>In the years following <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i><i>,</i> the vast majority of lower federal courts have applied its four-part "substantive due process" test indiscriminately to all excessive force claims lodged against law enforcement and prison officials under § 1983, without considering whether the particular application of force might implicate a more specific constitutional right governed by a different standard.<sup>[7]</sup> Indeed, many courts have seemed to assume, as did the courts below in this case, that there is a generic "right" to be free from excessive force, grounded not in any particular constitutional provision but rather in "basic principles of § 1983 jurisprudence."<sup>[8]</sup></p>
<p>We reject this notion that all excessive force claims brought under § 1983 are governed by a single generic standard. As we have said many times, § 1983 "is not itself a <span class="star-pagination">*394</span> source of substantive rights," but merely provides "a method for vindicating federal rights elsewhere conferred." <i>Baker</i> v. <i>McCollan,</i> <span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#144" aria-description="Citation for case: Baker v. McCollan">443 U. S. 137, 144, n. 3</a></span> (1979). In addressing an excessive force claim brought under § 1983, analysis begins by identifying the specific constitutional right allegedly infringed by the challenged application of force. See <i>id.,</i> at 140 ("The first inquiry in any § 1983 suit" is "to isolate the precise constitutional violation with which [the defendant] is charged").<sup>[9]</sup> In most instances, that will be either the Fourth Amendment's prohibition against unreasonable seizures of the person, or the Eighth Amendment's ban on cruel and unusual punishments, which are the two primary sources of constitutional protection against physically abusive governmental conduct. The validity of the claim must then be judged by reference to the specific constitutional standard which governs that right, rather than to some generalized "excessive force" standard. See <i>Tennessee</i> v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 7-22</a></span> (claim of excessive force to effect arrest analyzed under a Fourth Amendment standard); <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#318" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312, 318-326</a></span> (1986) (claim of excessive force to subdue convicted prisoner analyzed under an Eighth Amendment standard).</p>
<p>Where, as here, the excessive force claim arises in the context of an arrest or investigatory stop of a free citizen, it is most properly characterized as one invoking the protections of the Fourth Amendment, which guarantees citizens the right "to be secure in their persons . . . against unreasonable. . . seizures" of the person. This much is clear from our decision in <i>Tennessee</i> v. <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner, supra</a></span></i><i>.</i> In <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> we addressed a claim that the use of deadly force to apprehend a fleeing suspect who did not appear to be armed or otherwise dangerous violated the suspect's constitutional rights, notwithstanding the existence of probable cause to arrest. <span class="star-pagination">*395</span> Though the complaint alleged violations of both the Fourth Amendment and the Due Process Clause, see <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#5" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 5</a></span>, we analyzed the constitutionality of the challenged application of force solely by reference to the Fourth Amendment's prohibition against unreasonable seizures of the person, holding that the "reasonableness" of a particular seizure depends not only on <i>when</i> it is made, but also on <i>how</i> it is carried out. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 7-8</a></span>. Today we make explicit what was implicit in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i>'s analysis, and hold that <i>all</i> claims that law enforcement officers have used excessive force  deadly or not  in the course of an arrest, investigatory stop, or other "seizure" of a free citizen should be analyzed under the Fourth Amendment and its "reasonableness" standard, rather than under a "substantive due process" approach. Because the Fourth Amendment provides an explicit textual source of constitutional protection against this sort of physically intrusive governmental conduct, that Amendment, not the more generalized notion of "substantive due process," must be the guide for analyzing these claims.<sup>[10]</sup></p>
<p><span class="star-pagination">*396</span> Determining whether the force used to effect a particular seizure is "reasonable" under the Fourth Amendment requires a careful balancing of " `the nature and quality of the intrusion on the individual's Fourth Amendment interests' " against the countervailing governmental interests at stake. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 8</a></span>, quoting <i>United States</i> v. <i>Place,</i> <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983). Our Fourth Amendment jurisprudence has long recognized that the right to make an arrest or investigatory stop necessarily carries with it the right to use some degree of physical coercion or threat thereof to effect it. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22-27</a></span>. Because "[t]he test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application," <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#559" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 559</a></span> (1979), however, its proper application requires careful attention to the facts and circumstances of each particular case, including the severity of the crime at issue, whether the suspect poses an immediate threat to the safety of the officers or others, and whether he is actively resisting arrest or attempting to evade arrest by flight. See <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 8-9</a></span> (the question is "whether the totality of the circumstances justifie[s] a particular sort of . . . seizure").</p>
<p>The "reasonableness" of a particular use of force must be judged from the perspective of a reasonable officer on the scene, rather than with the 20/20 vision of hindsight. See <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 20-22</a></span>. The Fourth Amendment is not violated by an arrest based on probable cause, even though the wrong person is arrested, <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/" aria-description="Citation for case: Hill v. California">401 U. S. 797</a></span> (1971), nor by the mistaken execution of a valid search warrant on the wrong premises, <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79</a></span> (1987). With respect to a claim of excessive force, the same standard of reasonableness at the moment applies: "Not every push or shove, even if it may later seem unnecessary in the peace of a judge's chambers," <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1033</a></span>, violates the Fourth Amendment. The calculus of reasonableness must embody <span class="star-pagination">*397</span> allowance for the fact that police officers are often forced to make split-second judgments  in circumstances that are tense, uncertain, and rapidly evolving  about the amount of force that is necessary in a particular situation.</p>
<p>As in other Fourth Amendment contexts, however, the "reasonableness" inquiry in an excessive force case is an objective one: the question is whether the officers' actions are "objectively reasonable" in light of the facts and circumstances confronting them, without regard to their underlying intent or motivation. See <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#137" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 137-139</a></span> (1978); see also <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 21</a></span> (in analyzing the reasonableness of a particular search or seizure, "it is imperative that the facts be judged against an objective standard"). An officer's evil intentions will not make a Fourth Amendment violation out of an objectively reasonable use of force; nor will an officer's good intentions make an objectively unreasonable use of force constitutional. See <i>Scott</i> v. <i>United States, supra,</i> at 138, citing <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973).</p>
<p>Because petitioner's excessive force claim is one arising under the Fourth Amendment, the Court of Appeals erred in analyzing it under the four-part <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test. That test, which requires consideration of whether the individual officers acted in "good faith" or "maliciously and sadistically for the very purpose of causing harm," is incompatible with a proper Fourth Amendment analysis. We do not agree with the Court of Appeals' suggestion, see <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948</a></span>, that the "malicious and sadistic" inquiry is merely another way of describing conduct that is objectively unreasonable under the circumstances. Whatever the empirical correlations between "malicious and sadistic" behavior and objective unreasonableness may be, the fact remains that the "malicious and sadistic" factor puts in issue the subjective motivations of the individual officers, which our prior cases make clear has no bearing on whether a particular seizure is "unreasonable" under the Fourth Amendment. Nor do we agree with the <span class="star-pagination">*398</span> Court of Appeals' conclusion, see <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B...."><i>id.,</i> at 948, n. 3</a></span>, that because the subjective motivations of the individual officers are of central importance in deciding whether force used against a convicted prisoner violates the Eighth Amendment, see <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320-321</a></span>,<sup>[11]</sup> it cannot be reversible error to inquire into them in deciding whether force used against a suspect or arrestee violates the Fourth Amendment. Differing standards under the Fourth and Eighth Amendments are hardly surprising: the terms "cruel" and "punishments" clearly suggest some inquiry into subjective state of mind, whereas the term "unreasonable" does not. Moreover, the less protective Eighth Amendment standard applies "only after the State has complied with the constitutional guarantees traditionally associated with criminal prosecutions." <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#671" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 671</a></span>, <span class="star-pagination">*399</span> n. 40 (1977). The Fourth Amendment inquiry is one of "objective reasonableness" under the circumstances, and subjective concepts like "malice" and "sadism" have no proper place in that inquiry.<sup>[12]</sup></p>
<p>Because the Court of Appeals reviewed the District Court's ruling on the motion for directed verdict under an erroneous view of the governing substantive law, its judgment must be vacated and the case remanded to that court for reconsideration of that issue under the proper Fourth Amendment standard.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BLACKMUN, with whom JUSTICE BRENNAN and JUSTICE MARSHALL join, concurring in part and concurring in the judgment.</p>
<p>I join the Court's opinion insofar as it rules that the Fourth Amendment is the primary tool for analyzing claims of excessive force in the prearrest context, and I concur in the judgment remanding the case to the Court of Appeals for reconsideration of the evidence under a reasonableness standard. In light of respondents' concession, however, that the pleadings in this case properly may be construed as raising a Fourth Amendment claim, see Brief for Respondents 3, I see no reason for the Court to find it necessary further to reach out to decide that prearrest excessive force claims are to be analyzed under the Fourth Amendment <i>rather than</i> under a <span class="star-pagination">*400</span> substantive due process standard. I also see no basis for the Court's suggestion, <i>ante,</i> at 395, that our decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), implicitly so held. Nowhere in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span></i> is a substantive due process standard for evaluating the use of excessive force in a particular case discussed; there is no suggestion that such a standard was offered as an alternative and rejected.</p>
<p>In this case, petitioner apparently decided that it was in his best interest to disavow the continued applicability of substantive due process analysis as an alternative basis for recovery in prearrest excessive force cases. See Brief for Petitioner 20. His choice was certainly wise as a matter of litigation strategy in his own case, but does not (indeed, cannot be expected to) serve other potential plaintiffs equally well. It is for that reason that the Court would have done better to leave that question for another day. I expect that the use of force that is not demonstrably unreasonable under the Fourth Amendment only rarely will raise substantive due process concerns. But until I am faced with a case in which that question is squarely raised, and its merits are subjected to adversary presentation, I do not join in foreclosing the use of substantive due process analysis in prearrest cases.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed for the United States by <i>Solicitor General Fried, Assistant Attorney General Reynolds, Deputy Assistant Attorney General Clegg, David L. Shapiro, Brian J. Martin,</i> and <i>David K. Flynn;</i> and for the American Civil Liberties Union et al. by <i>Steven R. Shapiro.</i></p>
<p>[1]  Also named as a defendant was the city of Charlotte, which employed the individual respondents. The District Court granted a directed verdict for the city, and petitioner did not challenge that ruling before the Court of Appeals. Accordingly, the city is not a party to the proceedings before this Court.</p>
<p>[2]  Petitioner also asserted pendent state-law claims of assault, false imprisonment, and intentional infliction of emotional distress. Those claims have been dismissed from the case and are not before this Court.</p>
<p>[3]  The majority did note that because Graham was not an incarcerated prisoner, "his complaint of excessive force did not, therefore, arise under the eighth amendment." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>. However, it made no further effort to identify the constitutional basis for his claim.</p>
<p>[4]  Petitioner's argument was based primarily on <i>Kidd</i> v. <i>O'Neil,</i> <span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">774 F. 2d 1252</a></span> (CA4 1985), which read this Court's decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), as mandating application of a Fourth Amendment "objective reasonableness" standard to claims of excessive force during arrest. See <span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/#1254" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">774 F. 2d, at 1254-1257</a></span>. The reasoning of <i><span class="citation" data-id="459830"><a href="/opinion/459830/dennis-ray-kidd-v-robert-oneil-mike-lomonaco-fairfax-county-police-dept/" aria-description="Citation for case: Dennis Ray Kidd v. Robert O&#x27;Neil Mike Lomonaco Fairfax...">Kidd</a></span></i> was subsequently rejected by the en banc Fourth Circuit in <i>Justice</i> v. <i>Dennis,</i> <span class="citation" data-id="9476991"><a href="/opinion/498147/gary-w-justice-v-john-w-dennis-individually-and-in-his-official/#383" aria-description="Citation for case: Gary W. Justice v. John W. Dennis, Individually and in...">834 F. 2d 380, 383</a></span> (1987), cert. pending, No. 87-1422.</p>
<p>[5]  The majority noted that in <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">475 U. S. 312</a></span> (1986), we held that the question whether physical force used against convicted prisoners in the course of quelling a prison riot violates the Eighth Amendment "ultimately turns on `whether force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm.' " <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>, quoting <i>Whitley</i> v. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>Albers, supra,</i> at 320-321</a></span>. Though the Court of Appeals acknowledged that petitioner was not a convicted prisoner, it thought it "unreasonable . . . to suggest that a conceptual factor could be central to one type of excessive force claim but reversible error when merely considered by the court in another context." <span class="citation" data-id="9476639"><a href="/opinion/493625/dethorn-graham-v-city-of-charlotte-ms-connor-rb-townes-t-rice-hilda/#948" aria-description="Citation for case: Dethorn Graham v. City of Charlotte M.S. Connor R.B....">827 F. 2d, at 948, n. 3</a></span>.</p>
<p>[6]  Judge Friendly did not apply the Eighth Amendment's Cruel and Unusual Punishments Clause to the detainee's claim for two reasons. First, he thought that the Eighth Amendment's protections did not attach until after conviction and sentence. <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. This view was confirmed by <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#671" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 671, n. 40</a></span> (1977) ("Eighth Amendment scrutiny is appropriate only after the State has complied with the constitutional guarantees traditionally associated with criminal prosecutions"). Second, he expressed doubt whether a "spontaneous attack" by a prison guard, done without the authorization of prison officials, fell within the traditional Eighth Amendment definition of "punishments." <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1032" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1032</a></span>. Although Judge Friendly gave no reason for not analyzing the detainee's claim under the Fourth Amendment's prohibition against "unreasonable . . . seizures" of the person, his refusal to do so was apparently based on a belief that the protections of the Fourth Amendment did not extend to pretrial detainees. See <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick"><i>id.,</i> at 1033</a></span> (noting that "most of the courts faced with challenges to the conditions of <i>pretrial</i> detention have primarily based their analysis directly on the due process clause"). See n. 10, <i>infra.</i></p>
<p>[7]  See Freyermuth, Rethinking Excessive Force, 1987 Duke L. J. 692, 694-696, and nn. 16-23 (1987) (collecting cases).</p>
<p>[8]  See <i>Justice</i> v. <i>Dennis, supra,</i> at 382 ("There are . . . certain basic principles in section 1983 jurisprudence as it relates to claims of excessive force that are beyond question [,] [w]hether the factual circumstances involve an arrestee, a pretrial detainee or a prisoner").</p>
<p>[9]  The same analysis applies to excessive force claims brought against federal law enforcement and correctional officials under <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971).</p>
<p>[10]  A "seizure" triggering the Fourth Amendment's protections occurs only when government actors have, "by means of physical force or show of authority, . . . in some way restrained the liberty of a citizen," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19, n. 16</a></span> (1968); see <i>Brower</i> v. <i>County of Inyo,</i> <span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#596" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U. S. 593, 596</a></span> (1989).
</p>
<p>Our cases have not resolved the question whether the Fourth Amendment continues to provide individuals with protection against the deliberate use of excessive physical force beyond the point at which arrest ends and pretrial detention begins, and we do not attempt to answer that question today. It is clear, however, that the Due Process Clause protects a pretrial detainee from the use of excessive force that amounts to punishment. See <i>Bell</i> v. <i>Wolfish,</i> <span class="citation" data-id="9427563"><a href="/opinion/110075/bell-v-wolfish/#535" aria-description="Citation for case: Bell v. Wolfish">441 U. S. 520, 535-539</a></span> (1979). After conviction, the Eighth Amendment "serves as the primary source of substantive protection . . . in cases . . . where the deliberate use of force is challenged as excessive and unjustified." <i>Whitley</i> v. <i>Albers,</i> <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#327" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 327</a></span>. Any protection that "substantive due process" affords convicted prisoners against excessive force is, we have held, at best redundant of that provided by the Eighth Amendment. <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Ibid.</a></span></i></p>
<p>[11]  In <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span>,</i> we addressed a § 1983 claim brought by a convicted prisoner, who claimed that prison officials had violated his Eighth Amendment rights by shooting him in the knee during a prison riot. We began our Eighth Amendment analysis by reiterating the long-established maxim that an Eighth Amendment violation requires proof of the " ` "unnecessary and wanton infliction of pain." ' " <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#319" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 319</a></span>, quoting <i>Ingraham</i> v. <i>Wright,</i> <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#670" aria-description="Citation for case: Ingraham v. Wright">430 U. S., at 670</a></span>, in turn quoting <i>Estelle</i> v. <i>Gamble,</i> <span class="citation" data-id="9426610"><a href="/opinion/109561/estelle-v-gamble/#103" aria-description="Citation for case: Estelle v. Gamble">429 U. S. 97, 103</a></span> (1976). We went on to say that when prison officials use physical force against an inmate "to restore order in the face of a prison disturbance, . . . the question whether the measure taken inflicted unnecessary and wanton pain . . . <i>ultimately turns</i> on `whether the force was applied in a good faith effort to maintain or restore discipline or maliciously and sadistically for the very purpose of causing harm.' " <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 320-321</a></span> (emphasis added), quoting <i>Johnson</i> v. <i>Glick,</i> <span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/#1033" aria-description="Citation for case: Johnson v. Glick">481 F. 2d, at 1033</a></span>. We also suggested that the other prongs of the <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test might be useful in analyzing excessive force claims brought under the Eighth Amendment. <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#321" aria-description="Citation for case: Whitley v. Albers">475 U. S., at 321</a></span>. But we made clear that this was so <i>not</i> because Judge Friendly's four-part test is some talismanic formula generally applicable to all excessive force claims, but because its four factors help to focus the central inquiry in the Eighth Amendment context, which is whether the particular use of force amounts to the "unnecessary and wanton infliction of pain." See <span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/#320" aria-description="Citation for case: Whitley v. Albers"><i>id.,</i> at 320-321</a></span>. Our endorsement of the <i>Johnson</i> v. <i><span class="citation" data-id="8890588"><a href="/opinion/8903545/johnson-v-glick/" aria-description="Citation for case: Johnson v. Glick">Glick</a></span></i> test in <i><span class="citation" data-id="9430377"><a href="/opinion/111610/whitley-v-albers/" aria-description="Citation for case: Whitley v. Albers">Whitley</a></span></i> thus had no implications beyond the Eighth Amendment context.</p>
<p>[12]  Of course, in assessing the credibility of an officer's account of the circumstances that prompted the use of force, a factfinder may consider, along with other factors, evidence that the officer may have harbored ill-will toward the citizen. See <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#139" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 139, n. 13</a></span> (1978). Similarly, the officer's <i>objective</i> "good faith"  that is, whether he could reasonably have believed that the force used did not violate the Fourth Amendment  may be relevant to the availability of the qualified immunity defense to monetary liability under § 1983. See <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635</a></span> (1987). Since no claim of qualified immunity has been raised in this case, however, we express no view on its proper application in excessive force cases that arise under the Fourth Amendment.</p>

</div>
```

---

## GROUP: content/cases/Hafer v. Melo.md  (`case`, 5 assertions)

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
{"assertion_id": "337ad8ef1f1c81b9", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "502 U.S. 21 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 6502", "official_citation_present": true, "parallel_cite": "112 S. Ct. 358; 116 L. Ed. 2d 301; 57 Empl. Prac. Dec. (CCH) 41,059", "title": "Hafer v. Melo", "year": "1991"}}
{"assertion_id": "6f4121f67685ab5e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "State officials sued in their individual (personal) capacities for actions taken in their official capacity are 'persons' within the meaning of § 1983; the Eleventh Amendment does not bar such personal-capacity suits, and the official character of the challenged acts does not by itself confer absolute immunity.", "title": "Hafer v. Melo"}}
{"assertion_id": "fbaf44fe96eafe82", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Anchor", "title": "Hafer v. Melo"}}
{"assertion_id": "81adcd57361eefe1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Hafer v. Melo"}}
{"assertion_id": "d58c1918bafd0674", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Hafer v. Melo", "varies_by_point": "false"}}
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

## GROUP: content/cases/Harlow v. Fitzgerald.md  (`case`, 5 assertions)

### content_page

```
---
title: "Harlow v. Fitzgerald"
type: case
citation: "457 U.S. 800 (1982)"
parallel_cite: "102 S. Ct. 2727; 73 L. Ed. 2d 396"
neutral_cite: 1982 U.S. LEXIS 139
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1982
date_decided: 1982-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1982-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Harlow v. Fitzgerald
  varies_by_point: false
  scope_note: "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110763/harlow-v-fitzgerald/"
  cluster_id: 110763
  opinion_id: 9428863
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Anchor"
related: ["[[Saucier v. Katz]]", "[[Pearson v. Callahan]]", "[[City of Tahlequah v. Bond]]"]
aliases: []
tags: ["case", "qualified-immunity", "section-1983", "clearly-established-law", "objective-test"]
holding: "Reformulated qualified immunity as a purely OBJECTIVE test: officials performing discretionary functions are shielded from civil damages…"
lake:
  record_id: Harlow v. Fitzgerald
  status: verified
  projected_at: 2026-07-06
---

# Harlow v. Fitzgerald

*457 U.S. 800 (1982)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A. Ernest Fitzgerald, a former Air Force management analyst, sued senior aides to President Nixon, claiming he had been unlawfully discharged in retaliation for his whistleblowing testimony to Congress. The aides asserted [[Qualified Immunity|qualified immunity]]. (The suit was a *[[Bivens v. Six Unknown Named Agents|Bivens]]* action against federal officials, but the immunity standard the Court announced governs § 1983 suits against state officials as well.) The Court used the case to re-examine the standard for [[Qualified Immunity|qualified immunity]].

## Issue
What standard governs the [[Qualified Immunity|qualified immunity]] of government officials performing discretionary functions when they are sued for civil damages.

## Rule
[[Qualified Immunity|Qualified immunity]] is governed by a purely objective standard keyed to clearly established law. "[G]overnment officials performing discretionary functions generally are shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known." — 457 U.S. at 818. ^pin-818

The Court abandoned the older inquiry's subjective "good faith / malice" prong because it too often defeated summary judgment and exposed officials to the burdens of trial and discovery; immunity now turns on the objective legal reasonableness of the conduct measured against clearly established law.

## Application
Because the governing inquiry is objective, resolving the aides' immunity did not require probing their subjective intent; instead the question was whether their alleged conduct violated clearly established rights of which a reasonable official would have known. The Court therefore [[Reading and Citing Cases#vacated|vacated]] the denial of summary judgment and [[Reading and Citing Cases#on-remand|remanded]] for the lower court to apply the new objective standard.

## Conclusion
[[Qualified Immunity|Qualified immunity]] is determined by an objective "clearly established law" test, not by an official's subjective good faith; the judgment was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]] for application of that standard.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Harlow*'s objective standard remains the foundation of qualified-immunity doctrine; later cases refine the "clearly established" inquiry (e.g., the level of generality and case-specificity stressed in [[City of Tahlequah v. Bond]]) without disturbing *Harlow*'s objective test.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Anchor*

## Sources
- *Harlow v. Fitzgerald*, 457 U.S. 800 (1982) — https://www.courtlistener.com/opinion/110763/harlow-v-fitzgerald/ — pinpoint: 818.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "09934ff653b52dc0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "457 U.S. 800 (1982)", "court": "U.S. Supreme Court", "neutral_cite": "1982 U.S. LEXIS 139", "official_citation_present": true, "parallel_cite": "102 S. Ct. 2727; 73 L. Ed. 2d 396", "title": "Harlow v. Fitzgerald", "year": "1982"}}
{"assertion_id": "a8d89fb83efd805d", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Anchor", "title": "Harlow v. Fitzgerald"}}
{"assertion_id": "dff595ef247367cb", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reformulated qualified immunity as a purely OBJECTIVE test: officials performing discretionary functions are shielded from civil damages…", "title": "Harlow v. Fitzgerald"}}
{"assertion_id": "78d4c79912093d24", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Harlow v. Fitzgerald"}}
{"assertion_id": "a97a5c74d0f8afdc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1982-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Harlow v. Fitzgerald", "field_i_validity": "good_law", "scope_note": "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry.", "title": "Harlow v. Fitzgerald", "varies_by_point": "false"}}
```

### lake record — Harlow v. Fitzgerald

```json
{
  "schema_version": "s2.v1",
  "record_id": "Harlow v. Fitzgerald",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Harlow v. Fitzgerald",
    "case_name_short": "Harlow",
    "case_name_full": "HARLOW Et Al. v. FITZGERALD",
    "input_case_name": "Harlow v. Fitzgerald",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1982-06-24",
    "year": 1982,
    "docket": null,
    "cluster_id": 110763,
    "lead_opinion_id": 9428863,
    "sibling_ids": [
      110763,
      9428863,
      9428864,
      9428865
    ],
    "absolute_url": "/opinion/110763/harlow-v-fitzgerald/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "457 U.S. 800",
      "volume": "457",
      "reporter": "U.S.",
      "page": "800",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "102 S. Ct. 2727",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 396",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "396",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1982 U.S. LEXIS 139",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "139",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "457 U.S. 800",
        "volume": "457",
        "reporter": "U.S.",
        "page": "800",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "102 S. Ct. 2727",
        "volume": "102",
        "reporter": "S. Ct.",
        "page": "2727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "73 L. Ed. 2d 396",
        "volume": "73",
        "reporter": "L. Ed. 2d",
        "page": "396",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1982 U.S. LEXIS 139",
        "volume": "1982",
        "reporter": "U.S. LEXIS",
        "page": "139",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "457 U.S. 800",
    "official_selection": {
      "court_class": "scotus",
      "selected": "457 U.S. 800",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-818",
      "page": null,
      "quote": "--- # Harlow v. Fitzgerald *457 U.S. 800 (1982)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A. Ernest Fitzgerald, a former Air Force management analyst, sued senior aides to President Nixon, claiming he had been unlawfully discharged in retaliation for his whistleblowing testimony to Congress. The aides asserted qualified immunity. (The suit was a *Bivens* action against federal officials, but the immunity standard the Court announced governs \u00a7 1983 suits against state officials as well.) The Court used the case to re-examine the standard for qualified immunity. ## Issue What standard governs the qualified immunity of government officials performing discretionary functions when they are sued for civil damages. ## Rule Qualified immunity is governed by a purely objective standard keyed to clearly established law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1982-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Harlow v. Fitzgerald",
    "varies_by_point": false,
    "scope_note": "Objective standard refined (not displaced) by later cases governing the clearly-established inquiry.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Ashcroft v. Iqbal",
          "cluster_id": 145875,
          "cite": [
            "173 L. Ed. 2d 868",
            "129 S. Ct. 1937",
            "556 U.S. 662",
            "2009 U.S. LEXIS 3472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": [
            "76 L. Ed. 2d 527",
            "103 S. Ct. 2317",
            "462 U.S. 213",
            "1983 U.S. LEXIS 54",
            "51 U.S.L.W. 4709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. Graham",
          "cluster_id": 111500,
          "cite": [
            "87 L. Ed. 2d 114",
            "105 S. Ct. 3099",
            "473 U.S. 159",
            "1985 U.S. LEXIS 86",
            "53 U.S.L.W. 4966"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
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
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennhurst State School and Hospital v. Halderman",
          "cluster_id": 111094,
          "cite": [
            "79 L. Ed. 2d 67",
            "104 S. Ct. 900",
            "465 U.S. 89",
            "1984 U.S. LEXIS 4",
            "52 U.S.L.W. 4155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hudson v. McMillian",
          "cluster_id": 112693,
          "cite": [
            "117 L. Ed. 2d 156",
            "112 S. Ct. 995",
            "503 U.S. 1",
            "1992 U.S. LEXIS 1372"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hope v. Pelzer",
          "cluster_id": 121169,
          "cite": [
            "153 L. Ed. 2d 666",
            "122 S. Ct. 2508",
            "536 U.S. 730",
            "2002 U.S. LEXIS 4884"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Lacey v. Joseph Arpaio",
          "cluster_id": 807646,
          "cite": [
            "693 F.3d 896"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mireles v. Waco",
          "cluster_id": 112655,
          "cite": [
            "116 L. Ed. 2d 9",
            "112 S. Ct. 286",
            "502 U.S. 9",
            "1991 U.S. LEXIS 6225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hafer v. Melo",
          "cluster_id": 112657,
          "cite": [
            "116 L. Ed. 2d 301",
            "112 S. Ct. 358",
            "502 U.S. 21",
            "1991 U.S. LEXIS 6502",
            "57 Empl. Prac. Dec. (CCH) 41,059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Oklahoma v. Tuttle",
          "cluster_id": 111441,
          "cite": [
            "85 L. Ed. 2d 791",
            "105 S. Ct. 2427",
            "471 U.S. 808",
            "1985 U.S. LEXIS 26"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Seminole Tribe of Florida v. Florida",
          "cluster_id": 118011,
          "cite": [
            "134 L. Ed. 2d 252",
            "116 S. Ct. 1114",
            "517 U.S. 44",
            "1996 U.S. LEXIS 2165",
            "96 Cal. Daily Op. Serv. 2125",
            "96 Daily Journal DAR 3499",
            "64 U.S.L.W. 4167",
            "9 Fla. L. Weekly Fed. S 484",
            "34 Collier Bankr. Cas. 2d 1199",
            "42 ERC (BNA) 1289",
            "67 Empl. Prac. Dec. (CCH) 43,952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robbins Ex Rel. Robbins v. Oklahoma Ex Rel. Department of Human Services",
          "cluster_id": 170460,
          "cite": [
            "519 F.3d 1242",
            "70 Fed. R. Serv. 3d 175",
            "2008 U.S. App. LEXIS 5915",
            "2008 WL 747132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mullenix v. Luna",
          "cluster_id": 3153112,
          "cite": [
            "577 U.S. 7",
            "136 S. Ct. 305",
            "193 L. Ed. 2d 255",
            "2015 U.S. LEXIS 7160",
            "84 U.S.L.W. 4003",
            "25 Fla. L. Weekly Fed. S 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hunter v. Bryant",
          "cluster_id": 112671,
          "cite": [
            "116 L. Ed. 2d 589",
            "112 S. Ct. 534",
            "502 U.S. 224",
            "1991 U.S. LEXIS 7262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moss v. U.S. Secret Service",
          "cluster_id": 1450162,
          "cite": [
            "572 F.3d 962",
            "2009 U.S. App. LEXIS 15694",
            "2009 WL 2052985"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Walker v. Schult",
          "cluster_id": 868764,
          "cite": [
            "717 F.3d 119",
            "2013 U.S. App. LEXIS 10397",
            "2013 WL 2249159"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cuoco v. Moritsugu",
          "cluster_id": 7080999,
          "cite": [
            "222 F.3d 99",
            "2000 WL 1041227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ziglar v. Abbasi",
          "cluster_id": 4403804,
          "cite": [
            "582 U.S. 120",
            "2017 U.S. LEXIS 3874",
            "137 S. Ct. 1843",
            "198 L. Ed. 2d 290",
            "26 Fla. L. Weekly Fed. S 655",
            "85 U.S.L.W. 4360",
            "2017 WL 2621317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Jones",
          "cluster_id": 117950,
          "cite": [
            "132 L. Ed. 2d 238",
            "115 S. Ct. 2151",
            "515 U.S. 304",
            "1995 U.S. LEXIS 3907"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Harlow v. Fitzgerald:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjg2Nzg3MjAwMDAwJnM9OTQwNjk2OCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      },
      "lane2_top_cited": {
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTk4JnM9NzkwMzA0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzA4OTA1NjAwMDAwJnM9OTQ4NTYzNSZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 0,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 0,
        "triage_snippet_classified": 200
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110763 OR 9428863 OR 9428864 OR 9428865)",
    "indexed_citing_opinions": 11839,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110763,
        "count": 10331,
        "count_source": "search"
      },
      {
        "opinion_id": 9428863,
        "count": 1355,
        "count_source": "search"
      },
      {
        "opinion_id": 9428864,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428865,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 22957,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/harlow-v-fitzgerald.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk3NDY4Mjgmcz03MTAzMjEwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110763+OR+9428863+OR+9428864+OR+9428865%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110763,
        "cited_id": 90311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 94400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 104906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 106334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 108802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110059,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110131,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110132,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110273,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 110701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 350998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 356040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 366924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 370395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 382202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 389983,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 1507366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110763,
        "cited_id": 2390269,
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
    "date_created": "2026-07-05T06:15:17Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T06:21:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T06:15:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Harlow v. Fitzgerald

```
<opinion type="majority">
<author id="b846-6">Justice Powell</author>
<p id="Ache">delivered the opinion of the Court.</p>
<p id="b846-7">The issue in this case is the scope of the immunity available to the senior aides and advisers of the President of the United States in a suit for damages based upon their official acts.</p>
<p id="b846-8">I</p>
<p id="b846-9">In this suit for civil damages petitioners Bryce Harlow and Alexander Butterfield are alleged to have participated in a conspiracy to violate the constitutional and statutory rights of the respondent A. Ernest Fitzgerald. Respondent avers that petitioners entered the conspiracy in their capacities as senior White House aides to former President Richard M. Nixon. As the alleged conspiracy is the same as that involved in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, the facts need not be repeated in detail.</p>
<p id="b846-10">Respondent claims that Harlow joined the conspiracy in his role as the Presidential aide principally responsible for congressional relations.<footnotemark>1</footnotemark> At the conclusion of discovery the <page-number citation-index="1" label="803">*803</page-number>supporting evidence remained inferential. As evidence of Harlow’s conspiratorial activity respondent relies heavily on a series of conversations in which Harlow discussed Fitzgerald’s dismissal with Air Force Secretary Robert Seamans.<footnotemark>2</footnotemark> The other evidence most supportive of Fitzgerald’s claims consists of a recorded conversation in which the President later voiced a tentative recollection that Harlow was “all for canning” Fitzgerald.<footnotemark>3</footnotemark></p>
<p id="b847-5">Disputing Fitzgerald’s contentions, Harlow argues that exhaustive discovery has adduced no direct evidence of his in<page-number citation-index="1" label="804">*804</page-number>volvement in any wrongful activity.<footnotemark>4</footnotemark> He avers that Secretary Seamans advised him that considerations of efficiency required Fitzgerald’s removal by a reduction in force, despite anticipated adverse congressional reaction. Harlow asserts he had no reason to believe that a conspiracy existed. He contends that he took all his actions in good faith.<footnotemark>5</footnotemark></p>
<p id="b848-5">Petitioner Butterfield also is alleged to have entered the conspiracy not later than May 1969. Employed as Deputy Assistant to the President and Deputy Chief of Staff to H. R. Haldeman,<footnotemark>6</footnotemark> Butterfield circulated a White House memorandum in that month in which he claimed to have learned that Fitzgerald planned to “blow the whistle” on some “shoddy purchasing practices” by exposing these practices to public view.<footnotemark>7</footnotemark> Fitzgerald characterizes this memorandum as evi<page-number citation-index="1" label="805">*805</page-number>dence that Butterfield had commenced efforts to secure Fitzgerald’s retaliatory dismissal. As evidence that Butterfield participated in the conspiracy to conceal his unlawful discharge and prevent his reemployment, Fitzgerald cites communications between Butterfield and Haldeman in December 1969 and January 1970. After the President had promised at a press conference to inquire into Fitzgerald’s dismissal, Haldeman solicited Butterfield’s recommendations. In a subsequent memorandum emphasizing the importance of “loyalty,” Butterfield counseled against offering Fitzgerald another job in the administration at that time.<footnotemark>8</footnotemark></p>
<p id="b849-5">For his part, Butterfield denies that he was involved in any decision concerning Fitzgerald’s employment status until Haldeman sought his advice in December 1969 — more than a month after Fitzgerald’s termination had been scheduled and announced publicly by the Air Force. Butterfield states that he never communicated his views about Fitzgerald to any official of the Defense Department. He argues generally that nearly eight years of discovery have failed to turn up any evidence that he caused injury to Fitzgerald.<footnotemark>9</footnotemark></p>
<p id="b849-6">Together with their codefendant Richard Nixon, petitioners Harlow and Butterfield moved for summary judgment on February 12, 1980. In denying the motion the District Court upheld the legal sufficiency of Fitzgerald’s <em>Bivens (Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971)) claim under the First Amendment and his “inferred” statutory causes of action under <span class="citation no-link">5 U. S. C. §7211</span> (1976 ed., Supp. IV) and <span class="citation no-link">18 U. S. C. §1505</span>.<footnotemark>10</footnotemark> The court <page-number citation-index="1" label="806">*806</page-number>found that genuine issues of disputed fact remained for resolution at trial. It also ruled that petitioners were not entitled to absolute immunity. App. to Pet. for Cert. la-3a.</p>
<p id="b850-8">Independently of former President Nixon, petitioners invoked the collateral order doctrine and appealed the denial of their immunity defense to the Court of Appeals for. the District of Columbia Circuit. The Court of Appeals dismissed the appeal without opinion. <em><span class="citation no-link">Id.,</span> </em>at lla-12a. Never having determined the immunity available to the senior aides and advisers of the President of the United States, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./452/959/">452 U. S. 959</a></span> (1981).<footnotemark>11</footnotemark></p>
<p id="b850-9">H-1</p>
<p id="b850-3">As we reiterated today in <em>Nixon </em>v. Fitzgerald, <em>ante, </em>p. 731, our decisions consistently have held that government officials are entitled to some form of immunity from suits for damages. As recognized at common law, public officers require this protection to shield them from undue interference with their duties and' from potentially disabling threats of liability.</p>
<p id="b851-4"><page-number citation-index="1" label="807">*807</page-number>Our decisions have recognized immunity defenses of two kinds. For officials whose special functions or constitutional status requires complete protection from suit, we have recognized the defense of “absolute immunity.” The absolute immunity of legislators, in their legislative functions, see, <em>e. g., Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975), and of judges, in their judicial functions, see, <em>e. g., Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349</a></span> (1978), now is well settled. Our decisions also have extended absolute immunity to certain officials of the Executive Branch. These include prosecutors and similar officials, see <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou">438 U. S. 478, 508-512</a></span> (1978), executive officers engaged in adjudicative functions, <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#513" aria-description="Citation for case: Butz v. Economou"><em>id., </em>at 513-517</a></span>, and the President of the United States, see <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731.</p>
<p id="b851-5">For executive officials in general, however, our cases make plain that qualified immunity represents the norm. In <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), we acknowledged that high officials require greater protection than those with less complex discretionary responsibilities. Nonetheless, we held that a governor and his aides could receive the requisite protection from qualified or good-faith immunity. <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#247" aria-description="Citation for case: Scheuer v. Rhodes"><em>Id., </em>at 247-248</a></span>. In <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou, supra,</a></span> </em>we extended the approach of <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>to high federal officials of the Executive Branch. Discussing in detail the considerations that also had underlain our decision in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span>, </em>we explained that the recognition of a qualified immunity defense for high executives reflected an attempt to balance competing values: not only the importance of a damages remedy to protect the rights of citizens, <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#504" aria-description="Citation for case: Butz v. Economou">438 U. S., at 504-505</a></span>, but also “the need to protect officials who are required to exercise their discretion and the related public interest in encouraging the vigorous exercise of official authority.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Id., </em>at 506</a></span>. Without discounting the adverse consequences of denying high officials an absolute immunity from private lawsuits alleging constitutional violations — consequences found sufficient in <em>Spalding </em>v. <em>Vilas, </em><span class="citation" data-id="94400"><a href="/opinion/94400/spalding-v-vilas/" aria-description="Citation for case: Spalding v. Vilas">161 U. S. 483</a></span> (1896), and <em>Barr </em>v. <em>Matteo, </em><span class="citation" data-id="9764526"><a href="/opinion/2390269/barr-v-matteo/" aria-description="Citation for case: Barr v. Matteo">360 U. S. 564</a></span> <page-number citation-index="1" label="808">*808</page-number>(1959), to warrant extension to such officials of absolute immunity from suits at common law — we emphasized our expectation that insubstantial suits need not proceed to trial:</p>
<blockquote id="b852-7">“Insubstantial lawsuits can be quickly terminated by federal courts alert to the possibilities of artful pleading. Unless the complaint states a compensable claim for relief... , it should not survive a motion to dismiss. Moreover, the Court recognized in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>that damages suits concerning constitutional violations need not proceed to trial, but can be terminated on a properly supported motion for summary judgment based on the defense of immunity. ... In responding to such a motion, plaintiffs may not play dog in the manger; and firm application of the Federal Rules of Civil Procedure will ensure that federal officials are not harassed by frivolous lawsuits.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507-508</a></span> (citations omitted).</blockquote>
<p id="b852-8"><em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>continued to acknowledge that the special functions of some officials might require absolute immunity. But the Court held that “federal officials who seek absolute exemption from personal liability for unconstitutional conduct must bear the burden of showing that public policy requires an exemption of that scope.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Id., </em>at 506</a></span>. This we reaffirmed today in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 747.</p>
<p id="b852-10">HH HH f-H</p>
<p id="b852-3">A</p>
<p id="b852-4">Petitioners argue that they are entitled to a blanket protection of absolute immunity as an incident of their offices as Presidential aides. In deciding this claim we do not write on an empty page. In <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou, supra,</a></span> </em>the Secretary of Agriculture — a Cabinet official directly accountable to the President — asserted a defense of absolute official immunity from suit for civil damages. We rejected his claim. In so doing we did not question the power or the importance of the Secretary’s office. Nor did we doubt the importance to the <page-number citation-index="1" label="809">*809</page-number>President of loyal and efficient subordinates in executing his duties of office. Yet we found these factors, alone, to be insufficient to justify absolute immunity. “[T]he greater power of [high] officials,” we reasoned, “affords a greater potential for a regime of lawless conduct.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. Damages actions against high officials were therefore “an important means of vindicating constitutional guarantees.” <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Ibid.</a></span> </em>Moreover, we concluded that it would be “untenable to draw a distinction for purposes of immunity law between suits brought against state officials under [42 U. S. C.] § 1983 and suits brought directly under the Constitution against federal officials.” <em>Id., </em>at 504.</p>
<p id="b853-5">Having decided in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>that Members of the Cabinet ordinarily enjoy only qualified immunity from suit, we conclude today that it would be equally untenable to hold absolute immunity an incident of the office of every Presidential subordinate based in the White House. Members of the Cabinet are direct subordinates of the President, frequently with greater responsibilities, both to the President and to the Nation, than White House staff. The considerations that supported our decision in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>apply with equal force to this case. It is no disparagement of the offices held by petitioners to hold that Presidential aides, like Members of the Cabinet, generally are entitled only to a qualified immunity.</p>
<p id="b853-6">B</p>
<p id="b853-7">In disputing the controlling authority of <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>petitioners rely on the principles developed in <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">408 U. S. 606</a></span> (1972).<footnotemark>12</footnotemark> In <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>we endorsed the view that “it is literally impossible... for Members of Congress to per<page-number citation-index="1" label="810">*810</page-number>form their legislative tasks without the help of aide's and assistants” and that “the day-to-day work of such aides is so critical to the Members’ performance that they must be treated as the latter’s alter egos . . . <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#616" aria-description="Citation for case: Gravel v. United States"><em>Id., </em>at 616-617</a></span>. Having done so, we held the Speech and Debate Clause derivatively applicable to the “legislative acts” of a Senator’s aide that would have been privileged if performed by the Senator himself. <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#621" aria-description="Citation for case: Gravel v. United States"><em>Id., </em>at 621-622</a></span>.</p>
<p id="b854-5">Petitioners contend that the rationale of <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>mandates a similar “derivative” immunity for the chief aides of the President of the United States. Emphasizing that the President must delegate a large measure of authority to execute the duties of his office, they argue that recognition of derivative absolute immunity is made essential by all the considerations that support absolute immunity for the President himself.</p>
<p id="b854-6">Petitioners’ argument is not without force. Ultimately, however, it sweeps too far. If the President’s aides are derivatively immune because they are essential to the functioning of the Presidency, so should the Members of the Cabinet — Presidential subordinates some of whose essential roles are acknowledged by the Constitution itself<footnotemark>13</footnotemark> — be absolutely immune. Yet we implicitly rejected such derivative immunity in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>.</em><footnotemark><em>14</em></footnotemark><em> </em>Moreover, in general our cases have followed a “functional” approach to immunity law. We have reeog-<page-number citation-index="1" label="811">*811</page-number>nized that the judicial, prosecutorial, and legislative functions require absolute immunity. But this protection has extended no further than its justification would warrant. In Gravel, for example, we emphasized that Senators and their aides were absolutely immune only when performing “acts legislative in nature,” and not when taking other acts even “in their official capacity.” <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#625" aria-description="Citation for case: Gravel v. United States">408 U. S., at 625</a></span>. See <em>Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/#125" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S. 111, 125-133</a></span> (1979). Our cases involving judges<footnotemark>15</footnotemark> and prosecutors<footnotemark>16</footnotemark> have followed a similar line. The undifferentiated extension of absolute “derivative” immunity to the President’s aides therefore could not be reconciled with the “functional” approach that has characterized the immunity decisions of this Court, indeed including <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>itself.<footnotemark>17</footnotemark></p>
<p id="b855-5">C</p>
<p id="b855-6">Petitioners also assert an entitlement to immunity based on the “special functions” of White House aides. This form <page-number citation-index="1" label="812">*812</page-number>of argument accords with the analytical approach of our cases. For aides entrusted with discretionary authority in such sensitive areas as national security or foreign policy, absolute immunity might well be justified to protect the unhesitating performance of functions vital to the national interest.<footnotemark>18</footnotemark> But a “special functions” rationale does not warrant a blanket recognition of absolute immunity for all Presidential aides in the performance of all their, duties. This conclusion too follows from our decision in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>which establishes that an executive official’s claim to absolute immunity must be justified by reference to the public interest in the special functions of his office, not the mere fact of high station.<footnotemark>19</footnotemark></p>
<p id="b856-5"><em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>also identifies the location of the burden of proof. The burden of justifying absolute immunity rests on the official asserting the claim. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. We have not of course had occasion to identify how a Presidential aide might carry this burden. But the general requisites are familiar in our cases. In order to establish entitlement to absolute im<page-number citation-index="1" label="813">*813</page-number>munity a Presidential aide first must show that the responsibilities of his office embraced a function so sensitive as to require a total shield from liability.<footnotemark>20</footnotemark> He then must demonstrate that he was discharging the protected function when performing the act for which liability is asserted.<footnotemark>21</footnotemark></p>
<p id="b857-10">Applying these standards to the claims advanced by petitioners Harlow and Butterfield, we cannot conclude on the record before us that either has shown that “public policy requires [for any of the functions of his office] an exemption of [absolute] scope.” <em>Butz, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou">438 U. S., at 506</a></span>. Nor, assuming that petitioners did have functions for which absolute immunity would be warranted, could we now conclude that the acts charged in this lawsuit — if taken at all — would lie within the protected area. We do not, however, foreclose the possibility that petitioners, on remand, could satisfy the standards properly applicable to their claims.</p>
<p id="b857-11">
<em>&lt;</em>
</p>
<p id="b857-3">Even if they cannot establish that their official functions require absolute immunity, petitioners assert that public policy at least mandates an application of the qualified immunity standard that would permit the defeat of insubstantial claims without resort to trial. We agree.</p>
<p id="b857-4">A</p>
<p id="b857-5">The resolution of immunity questions inherently requires a balance between the evils inevitable in any available alterna<page-number citation-index="1" label="814">*814</page-number>tive. In situations of abuse of office, an action for damages may offer the only realistic avenue for vindication of constitutional guarantees. <em>Butz </em>v. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#506" aria-description="Citation for case: Butz v. Economou"><em>Economou, supra, </em>at 506</a></span>; see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#410" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S., at 410</a></span> (“For people in Bivens’ shoes, it is damages or nothing”). It is this recognition that has required the denial of absolute immunity to most public officers. At the same time, however, it cannot be disputed seriously that claims frequently run against the innocent as well as the guilty — at a cost not only to the defendant officials, but to society as a whole.<footnotemark>22</footnotemark> These social costs include the expenses of litigation, the diversion of official energy from pressing public issues, and the deterrence of able citizens from acceptance of public office. Finally, there is the danger that fear of being sued will “dampen the ardor of all but the most resolute, or the most irresponsible [public officials], in the unflinching discharge of their duties.” <em>Gregoire </em>v. <em>Biddle, </em><span class="citation" data-id="1507366"><a href="/opinion/1507366/gregoire-v-biddle/#581" aria-description="Citation for case: Gregoire v. Biddle">177 F. 2d 579, 581</a></span> (CA2 1949), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./339/949/">339 U. S. 949</a></span> (1950).</p>
<p id="b858-5">In identifying qualified immunity as the best attainable accommodation of competing values, in <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou"><em>Butz, supra, </em>at 507-508</a></span>, as in <em>Scheuer, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#245" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S., at 245-248</a></span>, we relied on the assumption that this standard would permit “[ijnsubstan-tial lawsuits [to] be quickly terminated.” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507-508</a></span>; see <em>Hanrahan </em>v. <em>Hampton, </em><span class="citation" data-id="9427946"><a href="/opinion/110275/hanrahan-v-hampton/#765" aria-description="Citation for case: Hanrahan v. Hampton">446 U. S. 754, 765</a></span> (1980) (Powell, J., concurring in part and dissenting in part).<footnotemark>23</footnotemark> Yet petitioners advance persuasive arguments that the dismissal of insubstantial lawsuits without trial — a factor presupposed in the balance of competing interests struck by <page-number citation-index="1" label="815">*815</page-number>our prior cases — requires an adjustment of the “good faith” standard established by our decisions.</p>
<p id="b859-5">B</p>
<p id="b859-6">Qualified or “good faith” immunity is an affirmative defense that must be pleaded by a defendant official. <em>Gomez </em>v. <em>Toledo, </em><span class="citation multiple-matches"><a href="/c/U.%20S./446/685/">446 U. S. 685</a></span> (1980).<footnotemark>24</footnotemark> Decisions of this Court have established that the “good faith” defense has both an “objective” and a “subjective” aspect. The objective element involves a presumptive knowledge of and respect for “basic, unquestioned constitutional, rights.” <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 322</a></span> (1975). The subjective component refers to “permissible intentions.” <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Ibid.</a></span> </em>Characteristically the Court has defined these elements by identifying the circumstances in which qualified immunity would <em>not </em>be available. Referring both to the objective and subjective elements, we have held that qualified immunity would be defeated if an official <em>“knew or reasonably should have known </em>that the action he took within his sphere of official responsibility would violate the constitutional rights of the [plaintiff], or if he took the action <em>with the malicious intention </em>to cause a deprivation of constitutional rights or other injury . . . .” <em>Ibid, </em>(emphasis added).<footnotemark>25</footnotemark></p>
<p id="b859-7">The subjective element of the good-faith defense frequently has proved incompatible with our admonition in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em><page-number citation-index="1" label="816">*816</page-number>that insubstantial claims should not proceed to trial. Rule 56 of the Federal Rules of Civil Procedure provides that disputed questions of fact ordinarily may not be decided on motions for summary judgment.<footnotemark>26</footnotemark> And an official’s subjective good faith has been considered to be a question of fact that some courts have regarded as inherently requiring resolution by a jury.<footnotemark>27</footnotemark></p>
<p id="b860-5">In the context of <em>Buts’ </em>attempted balancing of competing values, it now is clear that substantial costs attend the litigation of the subjective good faith of government officials. Not only are there the general costs of subjecting officials to the risks of trial — distraction of officials from their governmental duties, inhibition of discretionary action, and deterrence of able people from public service. There are special costs to “subjective” inquiries of this kind. Immunity generally is available only to officials performing discretionary functions. In contrast with the thought processes accompanying “ministerial” tasks, the judgments surrounding discretionary action almost inevitably are influenced by the decisionmaker’s experiences, values, and emotions. These variables explain in part why questions of subjective intent so rarely can be decided by summary judgment. Yet they also frame a back<page-number citation-index="1" label="817">*817</page-number>ground in which there often is no clear end to the relevant evidence. Judicial inquiry into subjective motivation therefore may entail broad-ranging discovery and the deposing of numerous persons, including an official’s professional colleagues.<footnotemark>28</footnotemark> Inquiries of this kind can be peculiarly disruptive of effective government.<footnotemark>29</footnotemark></p>
<p id="b861-5">Consistently with the balance at which we aimed in <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>we conclude today that bare allegations of malice should not suffice to subject government officials either to the costs of <page-number citation-index="1" label="818">*818</page-number>trial or to the burdens of broad-reaching discovery. We therefore hold that government officials performing discretionary functions, generally are shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known. See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 565</a></span> (1978); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>.<footnotemark>30</footnotemark></p>
<p id="b862-5">Reliance on the objective reasonableness of an official’s conduct, as measured by reference to clearly established law,<footnotemark>31</footnotemark> should avoid excessive disruption of government and permit the resolution of many insubstantial claims on summary judgment. On summary judgment, the judge appropriately may determine, not only the currently applicable law, but whether that law was clearly established at the time an action occurred.<footnotemark>32</footnotemark> If the law at that time was not clearly established, an official could not reasonably be expected to anticipate subsequent legal developments, nor could he fairly be said to “know” that the law forbade conduct not previously identified as unlawful. Until this threshold immunity question is resolved, discovery should not be allowed. If the law was clearly established, the immunity defense ordinarily <page-number citation-index="1" label="819">*819</page-number>should fail, since a reasonably competent public official should know the law governing his conduct. Nevertheless, if the official pleading the defense claims extraordinary circumstances and can prove that he neither knew nor should have known of the relevant legal standard, the defense should be sustained. But again, the defense would turn primarily on objective factors.</p>
<p id="b863-5">By defining the limits of qualified immunity essentially in objective terms, we provide no license to lawless conduct. The public interest in deterrence of unlawful conduct and in compensation of victims remains protected by a test that focuses on the objective legal reasonableness of an official’s acts. Where an official could be expected to know that certain conduct would violate statutory or constitutional rights, he should be made to hesitate; and a person who suffers injury caused by such conduct may have a cause of action.<footnotemark>33</footnotemark> But where an official’s duties legitimately require action in which clearly established rights are not implicated, the public interest may be better served by action taken “with independence and without fear of consequences.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#554" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 554</a></span> (1967).<footnotemark>34</footnotemark></p>
<p id="b863-6">C</p>
<p id="b863-7">In this case petitioners have asked us to hold that the respondent’s pretrial showings were insufficient to survive their motion for summary judgment.<footnotemark>35</footnotemark> We think it appropri<page-number citation-index="1" label="820">*820</page-number>ate, however, to remand the ease to the District Court for its reconsideration of this issue in light of this opinion.<footnotemark>36</footnotemark> The trial court is more familiar with the record so far developed and also is better situated to make any such further findings as may be necessary.</p>
<p id="b864-5">V</p>
<p id="b864-6">The judgment of the Court of Appeals is vacated, and the case is remanded for further action consistent with this opinion.</p>
<p id="b864-7">
<em>So ordered.</em>
</p>
<footnote label="1">
<p id="b846-13"> Harlow held this position from the beginning of the Nixon administration on January 20, 1969, through November 4, 1969. On the latter date he was designated as Counselor to the President, a position accorded Cabinet status. He served in that capacity until December 9, 1970, when he returned to private life. Harlow later resumed the duties of Counselor for <page-number citation-index="1" label="803">*803</page-number>the period from July 1,1973, through April 14,1974. Respondent appears to allege that Harlow continued in a conspiracy against him throughout the various changes of official assignment.</p>
</footnote>
<footnote label="2">
<p id="b847-7"> The record reveals that Secretary Seamans called Harlow in May 1969 to inquire about likely congressional reaction to a draft reorganization plan that would cause Fitzgerald’s dismissal. According to Seamans’ testimony, “[w]e [the Air Force] didn’t ask [Harlow] to pass judgment on the action itself. We just asked him what the impact would be in the relationship with the Congress.” App. 153a, 164a-165a (deposition of Robert Sea-mans). Through an aide Harlow responded that “this was a very sensitive item on the Hill and that it would be [his] recommendation that [the Air Force] not proceed to make such a change at that time.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 152a. But the Air Force persisted. Seamans spoke to Harlow on at least one subsequent occasion diming the spring of 1969. The record also establishes that Secretary Seamans called Harlow on November 4,1969, shortly after the public announcement of Fitzgerald’s impending dismissal, and again in December 1969. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 186a.</p>
</footnote>
<footnote label="3">
<p id="b847-8"> See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 284a (transcript of a recorded conversation between Richard Nixon and Ronald Ziegler, February 26,1973). In a conversation with the President on January 31, 1973, John Ehrliehman also recalled that Harlow had discussed the Fitzgerald case with the President. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 218a-221a (transcript of recorded conversation between Richard Nixon and John Ehrliehman, January 31,1973). In the same conversation the President himself asserted that he had spoken to Harlow about the Fitzgerald matter, see <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 218a, but the parties continue to dispute whether Mr. Nixon — at the most relevant moments in the discussion — was confusing Fitzgerald’s case with that of another dismissed employee. The President explicitly stated at one point that he previously had been confused. See <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">id.,</a></span> </em>at 220a.</p>
</footnote>
<footnote label="4">
<p id="b848-6"> See Defendants Memorandum of Points and Authorities in Support of Their Motion for Summary Judgment in Civ. No. 74-178 (DC), p. 7 (Feb. 12, 1980).</p>
</footnote>
<footnote label="5">
<p id="b848-7"> In support of his version of events Harlow relies particularly on the deposition testimony of Air Force Secretary Seamans, who stated that he regarded abolition of Fitzgerald’s position as necessary “to improve the efficiency” of the Financial Management Office of the Air Force and that he never received any White House instruction regarding the Fitzgerald case. App. 159a-160a. Harlow also disputes the probative value of Richard Nixon’s recorded remark that Harlow had supported Fitzgerald’s firing. Harlow emphasizes the tentativeness of the President’s statement. To the President’s query whether Harlow was “all for canning [Fitzgerald], wasn’t he?”, White House Press Secretary Ronald Ziegler in fact gave a negative reply: “No, I think Bryce may have been the other way.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 284a. The President did not respond to Ziegler’s comment.</p>
</footnote>
<footnote label="6">
<p id="b848-8"> The record establishes that Butterfield worked from an office immediately adjacent to the oval office. He had almost daily contact with the President until March 1973, when he left the White House to become Administrator of the Federal Aviation Administration.</p>
</footnote>
<footnote label="7">
<p id="b848-9"><em> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 274a. Butterfield reported that this information had been referred to the Federal Bureau of Investigation. In the memorandum Butterfield reported that he had received the information “by word of several mouths, but allegedly from a senior AFL-CIO official originally .... Evidently, Fitzgerald attended a recent meeting of the National Democratic Coalition and, while there, revealed his intentions to a labor representative who, fortunately for us, was unsympathetic.” <em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Ibid.</a></span></em></p>
</footnote>
<footnote label="8">
<p id="b849-7"><em> <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/" aria-description="Citation for case: Pierson v. Ray">Id.,</a></span> </em>at 99a-100a, 180a-181a. This memorandum, quoted in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 735-736, was not sent to the Defense Department.</p>
</footnote>
<footnote label="9">
<p id="b849-9"> See Memorandum in Support of Summary Judgment, <em>supra, </em>at 26. The history of Fitzgerald’s litigation is recounted in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731. Butterfield was named as a defendant in the initial civil action filed by Fitzgerald in 1974. Harlow was named for the first time in respondent’s second amended complaint of July 5, 1978.</p>
</footnote>
<footnote label="10">
<p id="b849-10"> The first of these statutes, <span class="citation no-link">5 U. S. C. § 7211</span> (1976 ed., Supp. IV), provides generally that “[t]he right of employees . . . to . . . furnish informa<page-number citation-index="1" label="806">*806</page-number>tion to either House of Congress, or to a committee or Member thereof, may not be interfered with or denied.” The second, <span class="citation no-link">18 U. S. C. § 1505</span>, is a criminal statute making it a crime to obstruct congressional testimony. Neither expressly creates a private right to sue for damages. Petitioners argue that the District Court erred in finding that a private cause of action could be inferred under either statute, and that “special factors” present in the context of the federal employer-employee relationship preclude the recognition of respondent’s <em>Bivens </em>action under the First Amendment. The legal sufficiency of respondent’s asserted causes of action is not, however, a question that we view as properly presented for our decision in the present posture of this case. See n. 36,. <em>infra.</em></p>
</footnote>
<footnote label="11">
<p id="b850-5"> As in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, our jurisdiction has been challenged on the basis that the District Court’s order denying petitioners’ claim of absolute immunity was not an appealable final order and that the Court of Appeals’ dismissal of petitioners’ appeal establishes that this case was never “in” the Court of Appeals within the meaning of <span class="citation no-link">28 U. S. C. § 1254</span>. As the discussion in <em>Nixon </em>establishes our jurisdiction in this case as well, we need not consider those challenges in this opinion.</p>
</footnote>
<footnote label="12">
<p id="b853-8"> Petitioners also claim support from other cases that have followed <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span> </em>in holding that congressional employees are derivatively entitled to the legislative immunity provided to United States Senators and Representatives under the Speech and Debate Clause. See <em>Eastland </em>v. <em>United States Servicemen’s Fund, </em><span class="citation" data-id="9426086"><a href="/opinion/109257/eastland-v-united-states-servicemens-fund/" aria-description="Citation for case: Eastland v. United States Servicemen&#x27;s Fund">421 U. S. 491</a></span> (1975); <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973).</p>
</footnote>
<footnote label="13">
<p id="b854-7"> See U. S. Const., Art. II, §2 (“The President . . . may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices . . .”).</p>
</footnote>
<footnote label="14">
<p id="b854-8"> The Chief Justice, <em>post, </em>at 828, argues that senior Presidential aides work “more intimately with the President on a daily basis than does a Cabinet officer,” and that <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span> </em>therefore is not controlling. In recent years, however, such men as Henry Kissinger and James Schlesinger have served in both Presidential advisory and Cabinet positions. Kissinger held both posts simultaneously. In our viéw it is impossible to generalize about the role of “offices” in an individual President’s administration without reference to the functions that particular officeholders are assigned by the President. <em>Butz </em>v. <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Economou</a></span> </em>cannot be distinguished on this basis.</p>
</footnote>
<footnote label="15">
<p id="b855-7"> See, <em>e. g., Supreme Court of Virginia </em>v. <em>Consumers Union of United States, </em><span class="citation" data-id="110273"><a href="/opinion/110273/supreme-court-of-virginia-v-consumers-union-of-the-united-states-inc/#731" aria-description="Citation for case: Supreme Court of Virginia v. Consumers Union of the...">446 U. S. 719, 731-737</a></span> (1980); <em>Stump </em>v. <em>Sparkman, </em><span class="citation" data-id="9427113"><a href="/opinion/109820/stump-v-sparkman/#362" aria-description="Citation for case: Stump v. Sparkman">435 U. S. 349, 362</a></span> (1978).</p>
</footnote>
<footnote label="16">
<p id="b855-8"> In <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 430-431</a></span> (1976), this Court reserved the question whether absolute immunity would extend to “those aspects of the prosecutor’s responsibility that cast him in the role of an administrator or investigative officer.” Since that time the Courts of Appeals generally have ruled that prosecutors do not enjoy absolute immunity for acts taken in those capacities. See, <em>e. g., Mancini </em>v. <em>Lester, </em><span class="citation" data-id="382202"><a href="/opinion/382202/dominick-mancini-v-sherwin-lester-and-david-lucas/#992" aria-description="Citation for case: Dominick Mancini v. Sherwin Lester and David Lucas">630 F. 2d 990, 992</a></span> (CA3 1980); <em>Forsyth </em>v. <em>Kleindienst, </em><span class="citation" data-id="8909855"><a href="/opinion/8921097/forsyth-v-kleindienst/#1213" aria-description="Citation for case: Forsyth v. Kleindienst">599 F. 2d 1203, 1213-1214</a></span> (CA3 1979). This Court at least implicitly has drawn the same distinction in extending absolute immunity to executive officials when they are engaged in quasi-prosecutorial functions. See <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#515" aria-description="Citation for case: Butz v. Economou">438 U. S., at 515-517</a></span>.</p>
</footnote>
<footnote label="17">
<p id="b855-9"> Our decision today in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, in no way abrogates this general rule. As we explained in that opinion, the recognition of absolute immunity for all of a President’s acts in office derives in principal part from factors unique to his constitutional responsibilities and station. Suits against other officials — including Presidential aides — generally do not invoke separation-of-powers considerations to the same extent as suits against the President himself.</p>
</footnote>
<footnote label="18">
<p id="b856-6"> Cf. <em>United States </em>v. <em>Nixon, </em><span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/#710" aria-description="Citation for case: United States v. Nixon">418 U. S. 683, 710-711</a></span> (1974) (“[C]ourts have traditionally shown the utmost deference to Presidential responsibilities” for foreign policy and military affairs, and claims of privilege in this area would receive a higher degree of deference than invocations of “a President’s generalized interest in confidentiality”); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#364" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 364</a></span> (1967) (White, J., concurring) (“We should not require the warrant procedure and the magistrate’s judgment if the President of the United States <em>or his chief legal officer, the Attorney General, </em>has considered the requirements of national security and authorized electronic surveillance as reasonable”) (emphasis added).</p>
</footnote>
<footnote label="19">
<p id="b856-7"> <em>Gravel </em>v. <em>United States, </em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">408 U. S. 606</a></span> (1972), points to a similar conclusion. We fairly may assume that some aides are assigned to act as Presidential “alter egos,” <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#616" aria-description="Citation for case: Gravel v. United States"><em>id., </em>at 616-617</a></span>, in the exercise of functions for which absolute immunity is “essential for the conduct of the public business,” <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou"><em>Butz, supra, </em>at 507</a></span>. Cf. <span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/#620" aria-description="Citation for case: Gravel v. United States"><em>Gravel, supra, </em>at 620</a></span> (derivative immunity extends only to acts within the “central role” of the Speech and Debate Clause in permitting free legislative speech and debate). By analogy to <em><span class="citation" data-id="9425016"><a href="/opinion/108610/gravel-v-united-states/" aria-description="Citation for case: Gravel v. United States">Gravel</a></span>, </em>a derivative claim to Presidential immunity would be strongest in such “central” Presidential domains as foreign policy and national security, in which the President could not discharge his singularly vital mandate without delegating functions nearly as sensitive as his own.</p>
</footnote>
<footnote label="20">
<p id="b857-6"> Here as elsewhere the relevant judicial inquiries would encompass considerations of public policy, the importance of which should be confirmed either by reference to the common law or, more likely, our constitutional heritage and structure. See <em>Nixon </em>v. <em>Fitzgerald, ante, </em>at 747-748.</p>
</footnote>
<footnote label="21">
<p id="b857-7"> The need for such an inquiry is implicit in <em>Butz </em>v. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou"><em>Economou, supra, </em>at 508-517</a></span>; see <em>Imbler </em>v. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#430" aria-description="Citation for case: Imbler v. Pachtman"><em>Pachtman, supra, </em>at 430-431</a></span>. Cases involving immunity under the Speech and Debate Clause have inquired explicitly into whether particular acts and activities qualified for the protection of the Clause. See, <em>e. g., Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S. 111</a></span> (1979); <em>Doe </em>v. <em>McMillan, </em><span class="citation" data-id="9425326"><a href="/opinion/108802/doe-v-mcmillan/" aria-description="Citation for case: Doe v. McMillan">412 U. S. 306</a></span> (1973); <em>Gravel </em>v. <em>United States, supra.</em></p>
</footnote>
<footnote label="22">
<p id="b858-6"> See generally Schuck, Suing Our Servants: The Court, Congress, and the Liability of Public Officials for Damages, 1980 S. Ct. Rev. 281,-324-327.</p>
</footnote>
<footnote label="23">
<p id="b858-7"> The importance of this consideration hardly needs emphasis. This Court has noted the risk imposed upon political officials who must defend their actions and motives before a jury. See <em>Lake Country Estates, Inc. </em>v. <em>Tahoe Regional Planning Agency, </em><span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/#405" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S. 391, 405</a></span> (1979); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#377" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 377-378</a></span> (1951). As the Court observed in <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Tenney</a></span>: </em>“In times of political passion, dishonest or vindictive motives are readily attributed . . . and as readily believed.” <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#378" aria-description="Citation for case: Tenney v. Brandhove"><em>Id., </em>at 378</a></span>.</p>
</footnote>
<footnote label="24">
<p id="b859-8"><em> </em>Although <em>Gomez </em>presented the question in the context of an action under <span class="citation no-link">42 U. S. C. § 1983</span>, the Court’s analysis indicates that “immunity” must also be pleaded as a defense in actions under the Constitution and laws of the United States. See 446 U. S., at 640. <em>Gomez </em>did not decide which party bore the burden of proof on the issue of good faith. Id., at 642 (Rehnquist, J., concurring).</p>
</footnote>
<footnote label="25">
<p id="b859-9"> In <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span> </em>the Court explicitly limited its holding to the circumstances in which a school board member, ’In the specific context of school discipline,” <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>, would be stripped of claimed immunity in an action under § 1983. Subsequent cases, however, have quoted the <em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">Wood</a></span> </em>formulation as a general statement of the qualified immunity standard. See, <em>e. g., Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555, 562-563, 566</a></span> (1978), quoted in <em>Baker </em>v. <em>McCollan, </em><span class="citation" data-id="9427663"><a href="/opinion/110132/baker-v-mccollan/#139" aria-description="Citation for case: Baker v. McCollan">443 U. S. 137, 139</a></span> (1979).</p>
</footnote>
<footnote label="26">
<p id="b860-6"> Rule 56(c) states that summary judgment “shall be rendered forthwith if the pleadings, depositions, answers to interrogatories, and admissions on file, together with the affidavits, if any, show that there is no genuine issue as to any material fact and that the moving party is entitled to a judgment as a matter of law.” In determining whether summary judgment is proper, a court ordinarily must look at the record in the light most favorable to the party opposing the motion, drawing all inferences most favorable to that party. <em>E. g., Poller </em>v. <em>Columbia Broadcasting System, Inc., 368 </em>U. S. 464, 473 (1962).</p>
</footnote>
<footnote label="27">
<p id="b860-7"><em> E. g., Landrum </em>v. <em>Moats, </em><span class="citation" data-id="356040"><a href="/opinion/356040/leslie-landrum-special-administratrix-of-the-estate-of-roy-lee-landrum/#1329" aria-description="Citation for case: Leslie Landrum, Special Administratrix of the Estate of...">576 F. 2d 1320, 1329</a></span> (CA8 1978); <em>Duchesne </em>v. <em>Sugarman, </em><span class="citation" data-id="350998"><a href="/opinion/350998/josephina-duchesne-as-administratrix-of-the-estate-of-pauline-perez-v-jule/#832" aria-description="Citation for case: Josephina Duchesne as Administratrix of the Estate of...">566 F. 2d 817, 832-833</a></span> (CA2 1977); cf. <em>Hutchinson </em>v. <em>Proxmire, </em><span class="citation" data-id="9427661"><a href="/opinion/110131/hutchinson-v-proxmire/#120" aria-description="Citation for case: Hutchinson v. Proxmire">443 U. S., at 120, n. 9</a></span> (questioning whether the existence of “actual malice,” as an issue of fact, may properly be decided on summary judgment in a suit alleging libel of a public figure).</p>
</footnote>
<footnote label="28">
<p id="b861-6"> In suits against a President’s closest aides, discovery of this kind frequently could implicate separation-of-powers concerns. As the Court recognized in <em>United States </em>v. <em>Nixon, </em><span class="citation" data-id="109101"><a href="/opinion/109101/united-states-v-nixon/" aria-description="Citation for case: United States v. Nixon">418 U. S., at 708</a></span>:</p>
<blockquote id="b861-7">“A President and those who assist him must be free to explore alternatives in the process of shaping policies and making decisions and to do so in a way many would be unwilling to express except privately. These are the considerations justifying a presumptive privilege for Presidential communications. The privilege is fundamental to the operation of Government and inextricably rooted in the separation of powers under the Constitution.”</blockquote>
</footnote>
<footnote label="29">
<p id="b861-8"> As Judge Gesell observed in his concurring opinion in <em>Halperin </em>v. <em>Kissinger, </em>196 U. S. App. D. C. 285, 307, <span class="citation" data-id="9842937"><a href="/opinion/370395/morton-halperin-v-henry-kissinger-morton-halperin-v-henry-kissinger/#1214" aria-description="Citation for case: Morton Halperin v. Henry Kissinger Morton Halperin v....">606 F. 2d 1192, 1214</a></span> (1979), aff’d in pertinent part by an equally divided Court, <span class="citation multiple-matches"><a href="/c/U.%20S./452/713/">452 U. S. 713</a></span> (1981):</p>
<blockquote id="b861-9">“We should not close our eyes to the fact that with increasing frequency in this jurisdiction and throughout the country plaintiffs are filing suits seeking damage awards against high government officials in their personal capacities based on alleged constitutional torts. Each such suit almost invariably results in these officials and their colleagues being subjected to extensive discovery into traditionally protected areas, such as their deliberations preparatory to the formulation of government policy and their intimate thought processes and communications at the presidential and cabinet levels. Such discover <em>[sic] </em>is wide-ranging, time-consuming, and not without considerable cost to the officials involved. It is not difficult for ingenious plaintiff’s counsel to create a material issue of fact on some element of the immunity defense where subtle questions of constitutional law and a decisionmaker’s mental processes are involved. A sentence from a casual document or a difference in recollection with regard to a particular policy conversation held long ago would usually, under the normal summary judgment standards, be sufficient [to force a trial]. . . . The effect of this development upon the willingness of individuals to serve their country is obvious.”</blockquote>
</footnote>
<footnote label="30">
<p id="b862-6"> This case involves no issue concerning the elements of the immunity available to state officials sued for constitutional violations under <span class="citation no-link">42 U. S. C. § 1983</span>. We have found previously, however, that it would be “untenable to draw a distinction for purposes of immunity law between suits brought against state officials under § 1983 and suits brought directly under the Constitution against federal officials.” <em>Butz </em>v. <em>Economou, </em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#504" aria-description="Citation for case: Butz v. Economou">438 U. S., at 504</a></span>.</p>
<p id="b862-7">Our decision in no way diminishes the absolute immunity currently available to officials whose ftmctions have been held to require a protection of this scope.</p>
</footnote>
<footnote label="31">
<p id="b862-8"> This case involves no claim that Congress has expressed its intent to impose “no fault” tort liability on high federal officials for violations of particular statutes or the Constitution.</p>
</footnote>
<footnote label="32">
<p id="b862-9"> As in <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette">434 U. S., at 565</a></span>, we need not define here the circumstances under which “the state of the law” should be “evaluated by reference to the opinions of this Court, of the Courts of Appeals, or of the local District Court.”</p>
</footnote>
<footnote label="33">
<p id="b863-8"> Cf. <em>Procunier </em>v. <span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#565" aria-description="Citation for case: Procunier v. Navarette"><em>Navarette, supra, </em>at 565</a></span>, quoting <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span> ("Because they could not reasonably have been expected to be aware of a constitutional right that had not yet been declared, petitioners did not act with such disregard for the established law that their conduct ‘cannot reasonably be characterized as being in good faith”’).</p>
</footnote>
<footnote label="34">
<p id="b863-9"> We emphasize that our decision applies only to suits for civil <em>damages </em>arising from actions within the scope of an official’s duties and in “objective” good faith. We express no view as to the conditions in which injunc-tive or declaratory relief might be available.</p>
</footnote>
<footnote label="35">
<p id="b863-10"> In <em><span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">Butz</a></span>, </em>we admonished that “insubstantial” suits against high public officials should not be allowed to proceed to trial. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#507" aria-description="Citation for case: Butz v. Economou">438 U. S., at 507</a></span>. See Schuck, <em>supra </em>n. 22, at 324-327. We reiterate this admonition. Insub<page-number citation-index="1" label="820">*820</page-number>stantial lawsuits undermine the effectiveness of government as contemplated by our constitutional structure, and “firm application of the Federal Rules of Civil Procedure” is fully warranted in such cases. <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/#508" aria-description="Citation for case: Butz v. Economou">438 U. S., at 508</a></span>.</p>
</footnote>
<footnote label="36">
<p id="b864-11"> Petitioners also have urged us, prior to the remand, to rule on the legal sufficiency of respondent’s “implied” causes of action under <span class="citation no-link">5 U. S. C. §7211</span> (1976 ed., Supp. IV) and <span class="citation no-link">18 U. S. C. § 1505</span> and his <em>Bivens </em>claim under the First Amendment. We do not view petitioners’ argument on the statutory question as insubstantial. <em>Cf. Merrill Lynch, Pierce, Fenner &amp; Smith, Inc. </em>v. <em>Curran, </em><span class="citation" data-id="9428751"><a href="/opinion/110701/merrill-lynch-pierce-fenner-smith-inc-v-curran/#377" aria-description="Citation for case: Merrill Lynch, Pierce, Fenner &amp; Smith, Inc. v. Curran">456 U. S. 353, 377-378</a></span> (1982) (controlling question in implication of statutory causes of action is whether Congress affirmatively intended to create a damages remedy); <em>Middlesex County Sewerage Auth. </em>v. <em>National Sea Clammers Assn., </em><span class="citation" data-id="9428452"><a href="/opinion/110546/middlesex-county-sewerage-authority-v-national-sea-clammers-assn/" aria-description="Citation for case: Middlesex County Sewerage Authority v. National Sea...">453 U. S. 1</a></span> (1981) (same); <em>Texas Industries, Inc. </em>v. <em>Radcliff Materials, Inc., 451 U. S. 630, </em>638-639 (1981) (same). Nor is the <em>Bivens </em>question. Cf. <em>Bush v. Lucas, </em><span class="citation" data-id="389983"><a href="/opinion/389983/william-c-bush-v-william-r-lucas/#576" aria-description="Citation for case: William C. Bush v. William R. Lucas">647 F. 2d 573, 576</a></span> (CA5 1981) (holding that the “unique relationship between the Federal Government and its civil service employees is a special consideration which counsels hesitation in inferring a <em>Bivens </em>remedy”). As in <em>Nixon </em>v. <em>Fitzgerald, ante, </em>p. 731, however, we took jurisdiction of the case only to resolve the immunity question under the collateral order doctrine. We therefore think it appropriate to leave these questions for fuller consideration by the District Court and, if necessary, by the Court of Appeals.</p>
</footnote>
</opinion>
```

---
