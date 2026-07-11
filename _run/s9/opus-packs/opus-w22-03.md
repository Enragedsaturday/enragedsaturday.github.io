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

## GROUP: _overhaul2/lake/cases/Ziglar v. Abbasi.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Ziglar v. Abbasi
type: case
citation: "582 U.S. 120 (2017)"
parallel_cite: "137 S. Ct. 1843; 198 L. Ed. 2d 290; 26 Fla. L. Weekly Fed. S 655; 85 U.S.L.W. 4360"
neutral_cite: "2017 U.S. LEXIS 3874; 2017 WL 2621317"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-06-19
docket: ""
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
  opinion_url: "https://www.courtlistener.com/opinion/4403804/ziglar-v-abbasi/"
  cluster_id: 4403804
  opinion_id: null
  identity_checked: true
lake:
  record_id: Ziglar v. Abbasi
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Key
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
  - "[[Hernandez v. Mesa]]"
  - "[[Egbert v. Boule]]"
  - "[[Goldey v. Fields]]"
tags:
  - case
  - bivens
  - section-1983
  - special-factors
  - national-security
holding: "A Bivens damages remedy does not extend to claims challenging the post-9/11 detention-policy decisions of high-level executive officials, because those claims arise in a new Bivens context in which special factors — including national-security and separation-of-powers concerns — counsel hesitation against a judicially inferred remedy."
---

# Ziglar v. Abbasi

*582 U.S. 120 (2017)* · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4403804 → opinion 4181057; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
In the weeks after the September 11, 2001 attacks, federal officials detained hundreds of out-of-status Muslim, Arab, and South Asian men as persons "of interest" to the terrorism investigation, holding many in restrictive, punitive confinement. A class of former detainees sued high-level federal officials — including former Attorney General John Ashcroft and former INS Commissioner James Ziglar — as well as a detention-facility warden, seeking damages under *[[Bivens v. Six Unknown Named Agents]]* for unconstitutional detention-policy decisions and abusive confinement conditions.

## Issue
Whether a *[[Bivens v. Six Unknown Named Agents|Bivens]]* damages remedy is available against federal officials for the detention-policy and confinement-conditions claims arising out of the post-9/11 roundup.

## Rule
Expanding *[[Bivens v. Six Unknown Named Agents|Bivens]]* beyond the three contexts the Court has recognized is "a disfavored judicial activity." A court asks first whether a claim presents a "new context" and, if so, whether "special factors" counsel hesitation before inferring a damages remedy. Separation of powers is central: "When a party seeks to assert an implied cause of action under the Constitution itself ... separation-of-powers principles are or should be central to the analysis. The question is 'who should decide' whether to provide for a damages remedy, Congress or the courts?" — 582 U.S. at 135. ^pin-135

The answer will most often be Congress, and a *[[Bivens v. Six Unknown Named Agents|Bivens]]* remedy is unavailable where "special factors counselling hesitation in the absence of affirmative action by Congress" are present.

## Application
The detention-policy claims sought to impose personal liability on executive officials for high-level national-security policy adopted in a national emergency — a new *[[Bivens v. Six Unknown Named Agents|Bivens]]* context far removed from the search-and-arrest, employment, and prisoner-medical settings previously recognized. The national-security dimension, the risk of exposing sensitive executive deliberations, and the availability of other checks were special factors counseling hesitation, so the Court declined to extend *[[Bivens v. Six Unknown Named Agents|Bivens]]* to those claims. It [[Reading and Citing Cases#on-remand|remanded]] the narrower prisoner-abuse claim against the warden for a proper special-factors analysis and separately addressed [[Qualified Immunity|qualified immunity]] on the detainees' conspiracy claim.

## Conclusion
The judgment of the Second Circuit was **reversed in part and [[Reading and Citing Cases#vacated|vacated]] in part**, and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Kennedy, J., delivered the opinion of the Court, joined by Roberts, C.J., and Thomas and Alito, JJ. (Thomas, J., concurring in part and in the judgment); Breyer, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Ginsburg, J. Sotomayor, Kagan, and Gorsuch, JJ., took no part in the consideration or decision of the case.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Ziglar* is the leading modern statement of the *[[Bivens v. Six Unknown Named Agents|Bivens]]*-contraction doctrine — the new-context and special-factors framework — and anchors the trilogy that narrows federal-officer damages liability alongside *[[Hernandez v. Mesa]]* (2020) and *[[Egbert v. Boule]]* (2022).

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key*

## Sources
- [*Ziglar v. Abbasi*, 582 U.S. 120 (2017)](https://www.courtlistener.com/opinion/4403804/ziglar-v-abbasi/) — pinpoint: 135 (Opinion of the Court, separation-of-powers/who-should-decide holding; Kennedy, J.). The CL opinion carries S. Ct. star pagination (137 S. Ct. 1843); the quoted passage sits immediately before the *1858 marker (137 S. Ct. 1857–58 = 582 U.S. 135). Quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0db253e9ecec133c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Ziglar v. Abbasi"}, "payload": {"all": [{"cite": "582 U.S. 120", "page": "120", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "582"}, {"cite": "2017 U.S. LEXIS 3874", "page": "3874", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}, {"cite": "137 S. Ct. 1843", "page": "1843", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "198 L. Ed. 2d 290", "page": "290", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "198"}, {"cite": "26 Fla. L. Weekly Fed. S 655", "page": "655", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "85 U.S.L.W. 4360", "page": "4360", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}, {"cite": "2017 WL 2621317", "page": "2621317", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}], "display": "582 U.S. 120", "official": {"cite": "582 U.S. 120", "page": "120", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "582"}, "official_selection_present": true, "record_id": "Ziglar v. Abbasi"}}
{"assertion_id": "226a93cfc71184b0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Ziglar v. Abbasi"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Ziglar v. Abbasi", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Ziglar v. Abbasi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ziglar v. Abbasi",
  "status": "under_review",
  "identity": {
    "case_name": "Ziglar v. Abbasi",
    "case_name_short": "Ziglar",
    "case_name_full": "James W. ZIGLAR, Petitioner v. Ahmer Iqbal ABBASI, Et Al. John D. Ashcroft, Former Attorney General, Et Al., Petitioners v. Ahmer Iqbal Abbasi, Et Al. Dennis Hasty, Et Al., Petitioners v. Ahmer Iqbal Abbasi, Et Al.",
    "input_case_name": "Ziglar v. Abbasi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-06-19",
    "year": 2017,
    "docket": null,
    "cluster_id": 4403804,
    "lead_opinion_id": 4181057,
    "sibling_ids": [],
    "absolute_url": "/opinion/4403804/ziglar-v-abbasi/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "582 U.S. 120",
      "volume": "582",
      "reporter": "U.S.",
      "page": "120",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "137 S. Ct. 1843",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 290",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "290",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 655",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "655",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4360",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4360",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 3874",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3874",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2621317",
        "volume": "2017",
        "reporter": "WL",
        "page": "2621317",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "582 U.S. 120",
        "volume": "582",
        "reporter": "U.S.",
        "page": "120",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 3874",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "3874",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 1843",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "1843",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "198 L. Ed. 2d 290",
        "volume": "198",
        "reporter": "L. Ed. 2d",
        "page": "290",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 655",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "655",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4360",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4360",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 2621317",
        "volume": "2017",
        "reporter": "WL",
        "page": "2621317",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "582 U.S. 120",
    "official_selection": {
      "court_class": "scotus",
      "selected": "582 U.S. 120",
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
    "date_created": "2026-07-06T06:02:09Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T06:02:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:02:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T06:02:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T06:02:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "ziglar-v-abbasi--4403804",
      "to_record_id": "Ziglar v. Abbasi",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Ziglar v. Abbasi (truncated)

```
(Slip Opinion)              OCTOBER TERM, 2016                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                        ZIGLAR v. ABBASI ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                 THE SECOND CIRCUIT

   No. 15–1358. Argued January 18, 2017—Decided June 19, 2017*
In the immediate aftermath of the September 11 terrorist attacks, the
  Federal Government ordered hundreds of illegal aliens to be taken
  into custody and held pending a determination whether a particular
  detainee had connections to terrorism. Respondents, six men of Arab
  or South Asian descent, were detained for periods of three to six
  months in a federal facility in Brooklyn. After their release, they
  were removed from the United States. They then filed this putative
  class action against petitioners, two groups of federal officials. The
  first group consisted of former Attorney General John Ashcroft, for-
  mer Federal Bureau of Investigation Director Robert Mueller, and
  former Immigration and Naturalization Service Commissioner James
  Ziglar (Executive Officials). The second group consisted of the facili-
  ty’s warden and assistant warden Dennis Hasty and James Sherman
  (Wardens). Respondents sought damages for constitutional viola-
  tions under the implied cause of action theory adopted in Bivens v.
  Six Unknown Fed. Narcotics Agents, 403 U. S. 388, alleging that peti-
  tioners detained them in harsh pretrial conditions for a punitive pur-
  pose, in violation of the Fifth Amendment; that petitioners did so be-
  cause of their actual or apparent race, religion, or national origin, in
  violation of the Fifth Amendment; that the Wardens subjected them
  to punitive strip searches, in violation of the Fourth and Fifth
  Amendments; and that the Wardens knowingly allowed the guards to
  abuse them, in violation of the Fifth Amendment. Respondents also
  brought a claim under 42 U. S. C. §1985(3), which forbids certain
——————
   *Together with No. 15–1359, Ashcroft, Former Attorney General,
et al. v. Abbasi et al., and No. 15–1363, Hasty et al. v. Abbasi et al., also
on certiorari to the same court.
2                         ZIGLAR v. ABBASI

                                Syllabus

 conspiracies to violate equal protection rights. The District Court
 dismissed the claims against the Executive Officials but allowed the
 claims against the Wardens to go forward. The Second Circuit af-
 firmed in most respects as to the Wardens but reversed as to the Ex-
 ecutive Officials, reinstating respondents’ claims.
Held: The judgment is reversed in part and vacated and remanded in
 part.
789 F. 3d 218, reversed in part and vacated and remanded in part.
     JUSTICE KENNEDY delivered the opinion of the Court, except as to
  Part IV–B, concluding:
     1. The limited reach of the Bivens action informs the decision
  whether an implied damages remedy should be recognized here.
  Pp. 6–14.
        (a) In 42 U. S. C. §1983, Congress provided a specific damages
  remedy for plaintiffs whose constitutional rights were violated by
  state officials, but Congress provided no corresponding remedy for
  constitutional violations by agents of the Federal Government. In
  1971, and against this background, this Court recognized in Bivens
  an implied damages action to compensate persons injured by federal
  officers who violated the Fourth Amendment’s prohibition against
  unreasonable searches and seizures. In the following decade, the
  Court allowed Bivens-type remedies twice more, in a Fifth Amend-
  ment gender-discrimination case, Davis v. Passman, 442 U. S. 228,
  and in an Eighth Amendment Cruel and Unusual Punishments
  Clause case, Carlson v. Green, 446 U. S. 14. These are the only cases
  in which the Court has approved of an implied damages remedy un-
  der the Constitution itself. Pp. 6–7.
        (b) Bivens, Davis, and Carlson were decided at a time when the
  prevailing law assumed that a proper judicial function was to “pro-
  vide such remedies as are necessary to make effective” a statute’s
  purpose. J. I. Case Co. v. Borak, 377 U. S. 426, 433. The Court has
  since adopted a far more cautious course, clarifying that, when decid-
  ing whether to recognize an implied cause of action, the “determina-
  tive” question is one of statutory intent. Alexander v. Sandoval, 532
  U. S. 275, 286. If a statute does not evince Congress’ intent “to create
  the private right of action asserted,” Touche Ross & Co. v. Redington,
  442 U. S. 560, 568, no such action will be created through judicial
  mandate. Similar caution must be exercised with respect to damages
  actions implied to enforce the Constitution itself. Bivens is well-
  settled law in its own context, but expanding the Bivens remedy is
  now considered a “disfavored” judicial activity. Ashcroft v. Iqbal, 556
  U. S. 662, 675.
     When a party seeks to assert an implied cause of action under the
  Constitution, separation-of-powers principles should be central to the
                   Cite as: 582 U. S. ____ (2017)                      3

                              Syllabus

analysis. The question is whether Congress or the courts should de-
cide to authorize a damages suit. Bush v. Lucas, 462 U. S. 367, 380.
Most often it will be Congress, for Bivens will not be extended to a
new context if there are “ ‘special factors counselling hesitation in the
absence of affirmative action by Congress.’ ” Carlson, supra, at 18. If
there are sound reasons to think Congress might doubt the efficacy or
necessity of a damages remedy as part of the system for enforcing the
law and correcting a wrong, courts must refrain from creating that
kind of remedy. An alternative remedial structure may also limit the
Judiciary’s power to infer a new Bivens cause of action. Pp. 8–14.
  2. Considering the relevant special factors here, a Bivens-type rem-
edy should not be extended to the claims challenging the confinement
conditions imposed on respondents pursuant to the formal policy
adopted by the Executive Officials in the wake of the September 11
attacks. These “detention policy claims” include the allegations that
petitioners violated respondents’ due process and equal protection
rights by holding them in restrictive conditions of confinement, and
the allegations that the Wardens violated the Fourth and Fifth
Amendments by subjecting respondents to frequent strip searches.
The detention policy claims do not include the guard-abuse claim
against Warden Hasty. Pp. 14–23.
     (a) The proper test for determining whether a claim arises in a
new Bivens context is as follows. If the case is different in a mean-
ingful way from previous Bivens cases decided by this Court, then the
context is new. Meaningful differences may include, e.g., the rank of
the officers involved; the constitutional right at issue; the extent of
judicial guidance for the official conduct; the risk of disruptive intru-
sion by the Judiciary into the functioning of other branches; or the
presence of potential special factors not considered in previous Bivens
cases. Respondents’ detention policy claims bear little resemblance
to the three Bivens claims the Court has approved in previous cases.
The Second Circuit thus should have held that this was a new Bivens
context and then performed a special factors analysis before allowing
this damages suit to proceed. Pp. 15–17.
     (b) The special factors here indicate that Congress, not the
courts, should decide whether a damages action should be allowed.
  With regard to the Executive Officials, a Bivens action is not “a
proper vehicle for altering an entity’s policy,” Correctional Services
Corp. v. Malesko, 534 U. S. 61, 74, and is not designed to hold officers
responsible for acts of their subordinates, see Iqbal, supra, at 676.
Even an action confined to the Executive Officers’ own discrete con-
duct would call into question the formulation and implementation of
a high-level executive policy, and the burdens of that litigation could
prevent officials from properly discharging their duties, see Cheney v.
4                           ZIGLAR v. ABBASI

                                  Syllabus

    United States Dist. Court for D. C., 542 U. S. 367, 382. The litigation
    process might also implicate the discussion and deliberations that led
    to the formation of the particular policy, requiring courts to interfere
    with sensitive Executive Branch functions. See Clinton v. Jones, 520
    U. S. 681, 701.
       Other special factors counsel against extending Bivens to cover the
    detention policy claims against any of the petitioners. Because those
    claims challenge major elements of the Government’s response to the
    September 11 attacks, they necessarily require an inquiry into na-
    tional-security issues. National-security policy, however, is the pre-
    rogative of Congress and the President, and courts are “reluctant to
    intrude upon” that authority absent congressional authorization.
    Department of Navy v. Egan, 484 U. S. 518, 530. Thus, Congress’
    failure to provide a damages remedy might be more than mere over-
    sight, and its silence might be more than “inadvertent.” Schweiker v.
    Chilicky, 487 U. S. 412, 423. That silence is also relevant and telling
    here, where Congress has had nearly 16 years to extend “the kind of
    remedies [sought by] respondents,” id., at 426, but has not done so.
    Respondents also may have had available “ ‘other alternative forms of
    judicial relief,’ ” Minneci v. Pollard, 565 U. S. 118, 124, including in-
    junctions and habeas petitions.
       The proper balance in situations like this, between deterring con-
    stitutional violations and freeing high officials to make the lawful de-
    cisions necessary to protect the Nation in times of great peril, is one
    for the Congress to undertake, not the Judiciary. The Second Circuit
    thus erred in allowing respondents’ detention policy claims to proceed
    under Bivens. Pp. 17–23.
       3. The Second Circuit also erred in allowing the prisoner abuse
    claim against Warden Hasty to go forward without conducting the
    required special factors analysis. Respondents’ prisoner abuse alle-
    gations against Warden Hasty state a plausible ground to find a con-
    stitutional violation should a Bivens remedy be implied. But the first
    question is whether the claim arises in a new Bivens context. This
    claim has significant parallels to Carlson, which extended Bivens to
    cover a failure to provide medical care to a prisoner, but this claim
    nevertheless seeks to extend Carlson to a new context. The constitu-
    tional right is different here: Carlson was predicated on the Eighth
    Amendment while this claim was predicated on the Fifth. The judi-
    cial guidance available to this warden with respect to his supervisory
    duties was less developed. There might have been alternative reme-
    dies available. And Congress did not provide a standalone damages
    remedy against federal jailers when it enacted the Prison Litigation
    Reform Act some 15 years after Carlson. Given this Court’s ex-
    pressed caution about extending the Bivens remedy, this context
                     Cite as: 582 U. S. ____ (2017)                      5

                                Syllabus

  must be regarded as a new one. Pp. 23–26.
     4. Petitioners are entitled to qualified immunity with respect to re-
  spondents’ claims under 42 U. S. C. §1985(3). Pp. 26–32.
        (a) Assuming that respondents’ allegations are true and well
  pleaded, the question is whether a reasonable officer in petitioners’
  position would have known the alleged conduct was an unlawful con-
  spiracy. The qualified-immunity inquiry turns on the “objective legal
  reasonableness” of the official’s acts, Harlow v. Fitzgerald, 457 U. S.
  800, 819, “assessed in light of the legal rules that were ‘clearly estab-
  lished’ at the time [the action] was taken,” Anderson v. Creighton,
  483 U. S. 635, 639. If it would have been clear to a reasonable officer
  that the alleged conduct “was unlawful in the situation he confront-
  ed,” Saucier v. Katz, 533 U. S. 194, 202, the defendant officer is not
  entitled to qualified immunity. But if a reasonable officer might not
  have known that the conduct was unlawful, then the officer is enti-
  tled to qualified immunity. Pp. 27–29.
        (b) Here, reasonable officials in petitioners’ positions would not
  have known with sufficient certainty that §1985(3) prohibited their
  joint consultations and the resulting policies. There are two reasons.
  First, the conspiracy is alleged to have been among officers in the
  same Department of the Federal Government. And there is no clear-
  ly established law on the issue whether agents of the same executive
  department are distinct enough to “conspire” with one another within
  the meaning of 42 U. S. C. §1985(3). Second, open discussion among
  federal officers should be encouraged to help those officials reach con-
  sensus on department policies, so there is a reasonable argument
  that §1985(3) liability should not extend to cases like this one. As
  these considerations indicate, the question whether federal officials
  can be said to “conspire” in these kinds of situations is sufficiently
  open that the officials in this suit would not have known that
  §1985(3) applied to their discussions and actions. It follows that rea-
  sonable officers in petitioners’ positions would not have known with
  any certainty that the alleged agreements were forbidden by that
  statute. Pp. 29–32.

   KENNEDY, J., delivered the opinion of the Court with respect to Parts
I, II, III, IV–A, and V, in which ROBERTS, C. J., and THOMAS and ALITO,
JJ., joined, and an opinion with respect to Part IV–B, in which ROB-
ERTS, C. J., and ALITO, J., joined. THOMAS, J., filed an opinion concur-
ring in part and concurring in the judgment. BREYER, J., filed a dis-
senting opinion, in which GINSBURG, J., joined. SOTOMAYOR, KAGAN,
and GORSUCH, JJ., took no part in the consideration or decision of the
cases.
                       Cite as: 582 U. S. ____ (2017)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                  Nos. 15–1358, 15–1359 and 15–1363
                                  _________________


              JAMES W. ZIGLAR, PETITIONER
15–1358                    v.
               AHMER IQBAL ABBASI, ET AL.

     JOHN D. ASHCROFT, FORMER ATTORNEY
         GENERAL, ET AL., PETITIONERS
15–1359               v.
          AHMER IQBAL ABBASI, ET AL.

          DENNIS HASTY, ET AL., PETITIONERS
15–1363                  v.
             AHMER IQBAL ABBASI, ET AL.
ON WRITS OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                                [June 19, 2017]

  JUSTICE KENNEDY delivered the opinion of the Court,
except as to Part IV–B.
  After the September 11 terrorist attacks in this country,
and in response to the deaths, destruction, and dangers
they caused, the United States Government ordered hun-
dreds of illegal aliens to be taken into custody and held.
Pending a determination whether a particular detainee
had connections to terrorism, the custody, under harsh
conditions to be described, continued. In many instances
custody lasted for days and weeks, then stretching into
months. Later, some of the aliens who had been detained
2                    ZIGLAR v. ABBASI

                     Opinion of the Court

filed suit, leading to the cases now before the Court.
   The complaint named as defendants three high execu-
tive officers in the Department of Justice and two of the
wardens at the facility where the detainees had been held.
Most of the claims, alleging various constitutional viola-
tions, sought damages under the implied cause of action
theory adopted by this Court in Bivens v. Six Unknown
Fed. Narcotics Agents, 403 U. S. 388 (1971). Another
claim in the complaint was based upon the statutory cause
of action authorized and created by Congress under Rev.
Stat. §1980, 42 U. S. C. §1985(3). This statutory cause of
action allows damages to persons injured by conspiracies
to deprive them of the equal protection of the laws.
   The suit was commenced in the United States District
Court for the Eastern District of New York. After this
Court’s decision in Ashcroft v. Iqbal, 556 U. S. 662 (2009),
a fourth amended complaint was filed; and that is the
complaint to be considered here. Motions to dismiss the
fourth amended complaint were denied as to some defend-
ants and granted as to others. These rulings were the
subject of interlocutory appeals to the United States Court
of Appeals for the Second Circuit. Over a dissenting opin-
ion by Judge Raggi with respect to the decision of the
three-judge panel—and a second unsigned dissent from
the court’s declining to rehear the suit en banc, joined by
Judge Raggi and five other judges—the Court of Appeals
ruled that the complaint was sufficient for the action to
proceed against the named officials who are now before us.
See Turkmen v. Hasty, 789 F. 3d 218 (2015) (panel deci-
sion); Turkmen v. Hasty, 808 F. 3d 197 (2015) (en banc
decision).
   The Court granted certiorari to consider these rulings.
580 U. S. ___ (2016). The officials who must defend the
suit on the merits, under the ruling of the Court of Ap-
peals, are the petitioners here. The former detainees who
seek relief under the fourth amended complaint are the
                 Cite as: 582 U. S. ____ (2017)           3

                     Opinion of the Court

respondents. The various claims and theories advanced
for recovery, and the grounds asserted for their dismissal
as insufficient as a matter of law, will be addressed in
turn.
                              I
  Given the present procedural posture of the suit, the
Court accepts as true the facts alleged in the complaint.
See Iqbal, 556 U. S., at 678.
                              A
   In the weeks following the September 11, 2001, terrorist
attacks—the worst in American history—the Federal
Bureau of Investigation (FBI) received more than 96,000
tips from members of the public. See id., at 667. Some
tips were based on well-grounded suspicion of terrorist
activity, but many others may have been based on fear of
Arabs and Muslims. FBI agents “questioned more than
1,000 people with suspected links to the [September 11]
attacks in particular or to terrorism in general.” Ibid.
   While investigating the tips—including the less sub-
stantiated ones—the FBI encountered many aliens who
were present in this country without legal authorization.
As a result, more than 700 individuals were arrested and
detained on immigration charges. Ibid. If the FBI desig-
nated an alien as not being “of interest” to the investiga-
tion, then he or she was processed according to normal
procedures. In other words the alien was treated just as
if, for example, he or she had been arrested at the border
after an illegal entry. If, however, the FBI designated an
alien as “of interest” to the investigation, or if it had
doubts about the proper designation in a particular case,
the alien was detained subject to a “hold-until-cleared
policy.” The aliens were held without bail.
   Respondents were among some 84 aliens who were
subject to the hold-until-cleared policy and detained at the
4                     ZIGLAR v. ABBASI

                      Opinion of the Court

Metropolitan Detention Center (MDC) in Brooklyn, New
York. They were held in the Administrative Maximum
Special Housing Unit (or Unit) of the MDC. The com-
plaint includes these allegations: Conditions in the Unit
were harsh. Pursuant to official Bureau of Prisons policy,
detainees were held in “ ‘tiny cells for over 23 hours a
day.’ ” 789 F. 3d, at 228. Lights in the cells were left on 24
hours. Detainees had little opportunity for exercise or
recreation. They were forbidden to keep anything in their
cells, even basic hygiene products such as soap or a tooth-
brush. When removed from the cells for any reason, they
were shackled and escorted by four guards. They were
denied access to most forms of communication with the
outside world. And they were strip searched often—any
time they were moved, as well as at random in their cells.
  Some of the harsh conditions in the Unit were not im-
posed pursuant to official policy. According to the com-
plaint, prison guards engaged in a pattern of “physical and
verbal abuse.” Ibid. Guards allegedly slammed detainees
into walls; twisted their arms, wrists, and fingers; broke
their bones; referred to them as terrorists; threatened
them with violence; subjected them to humiliating sexual
comments; and insulted their religion.
                             B
   Respondents are six men of Arab or South Asian de-
scent. Five are Muslims. Each was illegally in this coun-
try, arrested during the course of the September 11 inves-
tigation, and detained in the Administrative Maximum
Special Housing Unit for periods ranging from three to
eight months. After being released respondents were
removed from the United States.
   Respondents then sued on their own behalf, and on
behalf of a putative class, seeking compensatory and
punitive damages, attorney’s fees, and costs. Respond-
ents, it seems fair to conclude from the arguments pre-
                 Cite as: 582 U. S. ____ (2017)           5

                     Opinion of the Court

sented, acknowledge that in the ordinary course aliens
who are present in the United States without legal author-
ization can be detained for some period of time. But here
the challenge is to the conditions of their confinement and
the reasons or motives for imposing those conditions. The
gravamen of their claims was that the Government had no
reason to suspect them of any connection to terrorism, and
thus had no legitimate reason to hold them for so long in
these harsh conditions.
   As relevant here, respondents sued two groups of federal
officials in their official capacities. The first group con-
sisted of former Attorney General John Ashcroft, former
FBI Director Robert Mueller, and former Immigration and
Naturalization Service Commissioner James Ziglar. This
opinion refers to these three petitioners as the “Executive
Officials.” The other petitioners named in the complaint
were the MDC’s warden, Dennis Hasty, and associate
warden, James Sherman. This opinion refers to these two
petitioners as the “Wardens.”
   Seeking to invoke the Court’s decision in Bivens, re-
spondents brought four claims under the Constitution
itself. First, respondents alleged that petitioners detained
them in harsh pretrial conditions for a punitive purpose,
in violation of the substantive due process component of
the Fifth Amendment. Second, respondents alleged that
petitioners detained them in harsh conditions because of
their actual or apparent race, religion, or national origin,
in violation of the equal protection component of the Fifth
Amendment. Third, respondents alleged that the War-
dens subjected them to punitive strip searches unrelated
to any legitimate penological interest, in violation of the
Fourth Amendment and the substantive due process
component of the Fifth Amendment. Fourth, respondents
alleged that the Wardens knowingly allowed the guards to
abuse respondents, in violation of the substantive due
process component of the Fifth Amendment.
6                     ZIGLAR v. ABBASI

                     Opinion of the Court

   Respondents also brought a claim under 42 U. S. C.
§1985(3), which forbids certain conspiracies to violate
equal protection rights. Respondents alleged that peti-
tioners conspired with one another to hold respondents in
harsh conditions because of their actual or apparent race,
religion, or national origin.
                             C
   The District Court dismissed the claims against the
Executive Officials but allowed the claims against the
Wardens to go forward. The Court of Appeals affirmed in
most respects as to the Wardens, though it held that the
prisoner abuse claim against Sherman (the associate
warden) should have been dismissed. 789 F. 3d, at 264–
265. As to the Executive Officials, however, the Court of
Appeals reversed, reinstating respondents’ claims. Ibid.
As noted above, Judge Raggi dissented. She would have
held that only the prisoner abuse claim against Hasty
should go forward. Id., at 295, n. 41, 302 (opinion concur-
ring in part in judgment and dissenting in part). The
Court of Appeals declined to rehear the suit en banc, 808
F. 3d, at 197; and, again as noted above, Judge Raggi
joined a second dissent along with five other judges, id., at
198. This Court granted certiorari. 580 U. S. ___ (2016).
                             II
  The first question to be discussed is whether petitioners
can be sued for damages under Bivens and the ensuing
cases in this Court defining the reach and the limits of
that precedent.
                             A
   In 1871, Congress passed a statute that was later codi-
fied at Rev. Stat. §1979, 42 U. S. C. §1983. It entitles an
injured person to money damages if a state official violates
his or her constitutional rights. Congress did not create
an analogous statute for federal officials. Indeed, in the
                 Cite as: 582 U. S. ____ (2017)            7

                     Opinion of the Court

100 years leading up to Bivens, Congress did not pro-
vide a specific damages remedy for plaintiffs whose con-
stitutional rights were violated by agents of the Federal
Government.
  In 1971, and against this background, this Court decided
Bivens. The Court held that, even absent statutory
authorization, it would enforce a damages remedy to
compensate persons injured by federal officers who vio-
lated the prohibition against unreasonable search and sei-
zures. See 403 U. S., at 397. The Court acknowledged
that the Fourth Amendment does not provide for money
damages “in so many words.” Id., at 396. The Court
noted, however, that Congress had not foreclosed a dam-
ages remedy in “explicit” terms and that no “special fac-
tors” suggested that the Judiciary should “hesitat[e]” in
the face of congressional silence. Id., at 396–397. The
Court, accordingly, held that it could authorize a remedy
under general principles of federal jurisdiction. See id., at
392 (citing Bell v. Hood, 327 U. S. 678, 684 (1946)).
  In the decade that followed, the Court recognized what
has come to be called an implied cause of action in two
cases involving other constitutional violations. In Davis v.
Passman, 442 U. S. 228 (1979), an administrative assis-
tant sued a Congressman for firing her because she was a
woman. The Court held that the Fifth Amendment Due
Process Clause gave her a damages remedy for gender
discrimination. Id., at 248–249. And in Carlson v. Green,
446 U. S. 14 (1980), a prisoner’s estate sued federal jailers
for failing to treat the prisoner’s asthma. The Court held
that the Eighth Amendment Cruel and Unusual Punish-
ments Clause gave him a damages remedy for failure to
provide adequate medical treatment. See id., at 19. These
three cases—Bivens, Davis, and Carlson—represent the
only instances in which the Court has approved of an
implied damages remedy under the Constitution itself.
8                     ZIGLAR v. ABBASI

                      Opinion of the Court

                                B
   To understand Bivens and the two other cases implying
a damages remedy under the Constitution, it is necessary
to understand the prevailing law when they were decided.
In the mid-20th century, the Court followed a different
approach to recognizing implied causes of action than it
follows now. During this “ancien regime,” Alexander v.
Sandoval, 532 U. S. 275, 287 (2001), the Court assumed it
to be a proper judicial function to “provide such remedies
as are necessary to make effective” a statute’s purpose,
J. I. Case Co. v. Borak, 377 U. S. 426, 433 (1964). Thus, as
a routine matter with respect to statutes, the Court would
imply causes of action not explicit in the statutory text
itself. See, e.g., id., at 430–432; Allen v. State Bd. of Elec-
tions, 393 U. S. 544, 557 (1969); Sullivan v. Little Hunting
Park, Inc., 396 U. S. 229, 239 (1969) (“The existence of a
statutory right implies the existence of all necessary and
appropriate remedies”).
   These statutory decisions were in place when Bivens
recognized an implied cause of action to remedy a consti-
tutional violation. Against that background, the Bivens
decision held that courts must “adjust their remedies so as
to grant the necessary relief ” when “federally protected
rights have been invaded.” 403 U. S., at 392 (quoting Bell,
supra, at 678); see also 403 U. S., at 402 (Harlan, J., con-
curring) (discussing cases recognizing implied causes of
action under federal statutes). In light of this interpretive
framework, there was a possibility that “the Court would
keep expanding Bivens until it became the substantial
equivalent of 42 U. S. C. §1983.” Kent, Are Damages
Different?: Bivens and National Security, 87 S. Cal.
L. Rev. 1123, 1139–1140 (2014).
                           C
  Later, the arguments for recognizing implied causes of
action for damages began to lose their force. In cases
                 Cite as: 582 U. S. ____ (2017)            9

                     Opinion of the Court

decided after Bivens, and after the statutory implied
cause-of-action cases that Bivens itself relied upon, the
Court adopted a far more cautious course before finding
implied causes of action. In two principal cases under
other statutes, it declined to find an implied cause of
action. See Piper v. Chris-Craft Industries, Inc., 430 U. S.
1, 42, 45–46 (1977); Cort v. Ash, 422 U. S. 66, 68–69
(1975). Later, in Cannon v. University of Chicago, 441
U. S. 677 (1979), the Court did allow an implied cause of
action; but it cautioned that, where Congress “intends
private litigants to have a cause of action,” the “far better
course” is for Congress to confer that remedy in explicit
terms. Id., at 717.
   Following this expressed caution, the Court clarified in
a series of cases that, when deciding whether to recognize
an implied cause of action, the “determinative” question is
one of statutory intent. Sandoval, 532 U. S., at 286. If the
statute itself does not “displa[y] an intent” to create “a
private remedy,” then “a cause of action does not exist and
courts may not create one, no matter how desirable that
might be as a policy matter, or how compatible with the
statute.” Id., at 286–287; see also Transamerica Mortgage
Advisors, Inc. v. Lewis, 444 U. S. 11, 15–16, 23–24 (1979);
Karahalios v. Federal Employees, 489 U. S. 527, 536–537
(1989). The Court held that the judicial task was instead
“limited solely to determining whether Congress intended
to create the private right of action asserted.” Touche
Ross & Co. v. Redington, 442 U. S. 560, 568 (1979). If the
statute does not itself so provide, a private cause of action
will not be created through judicial mandate.            See
Transamerica, supra, at 24.
   The decision to recognize an implied cause of action
under a statute involves somewhat different considera-
tions than when the question is whether to recognize an
implied cause of action to enforce a provision of the Con-
stitution itself. When Congress enacts a statute, there are
10                    ZIGLAR v. ABBASI

                     Opinion of the Court

specific procedures and times for considering its terms and
the proper means for its enforcement. It is logical, then, to
assume that Congress will be explicit if it intends to create
a private cause of action. With respect to the Constitu-
tion, however, there is no single, specific congressional
action to consider and interpret.
   Even so, it is a significant step under separation-of-
powers principles for a court to determine that it has the
authority, under the judicial power, to create and enforce a
cause of action for damages against federal officials in
order to remedy a constitutional violation. When deter-
mining whether traditional equitable powers suffice to
give necessary constitutional protection—or whether, in
addition, a damages remedy is necessary—there are a
number of economic and governmental concerns to con-
sider. Claims against federal officials often create sub-
stantial costs, in the form of defense and indemnification.
Congress, then, has a substantial responsibility to deter-
mine whether, and the extent to which, monetary and
other liabilities should be imposed upon individual officers
and employees of the Federal Government. In addition,
the time and administrative costs attendant upon intru-
sions resulting from the discovery and trial process are
significant factors to be considered. In an analogous con-
text, Congress, it is fair to assume, weighed those concerns
in deciding not to substitute the Government as defendant
in suits seeking damages for constitutional violations. See
28 U. S. C. §2679(b)(2)(A) (providing that certain provi-
sions of the Federal Tort Claims Act do not apply to any
claim against a federal employee “which is brought for a
violation of the Constitution”).
   For these and other reasons, the Court’s expressed
caution as to implied causes of actions under congressional
statutes led to similar caution with respect to actions in
the Bivens context, where the action is implied to enforce
the Constitution itself. Indeed, in light of the changes to
                 Cite as: 582 U. S. ____ (2017)           11

                     Opinion of the Court

the Court’s general approach to recognizing implied dam-
ages remedies, it is possible that the analysis in the
Court’s three Bivens cases might have been different if
they were decided today. To be sure, no congressional
enactment has disapproved of these decisions. And it
must be understood that this opinion is not intended to
cast doubt on the continued force, or even the necessity, of
Bivens in the search-and-seizure context in which it arose.
Bivens does vindicate the Constitution by allowing some
redress for injuries, and it provides instruction and guid-
ance to federal law enforcement officers going forward.
The settled law of Bivens in this common and recurrent
sphere of law enforcement, and the undoubted reliance
upon it as a fixed principle in the law, are powerful rea-
sons to retain it in that sphere.
  Given the notable change in the Court’s approach to
recognizing implied causes of action, however, the Court
has made clear that expanding the Bivens remedy is now a
“disfavored” judicial activity. Iqbal, 556 U. S., at 675.
This is in accord with the Court’s observation that it has
“consistently refused to extend Bivens to any new context
or new category of defendants.” Correctional Services
Corp. v. Malesko, 534 U. S. 61, 68 (2001). Indeed, the
Court has refused to do so for the past 30 years.
  For example, the Court declined to create an implied
damages remedy in the following cases: a First Amend-
ment suit against a federal employer, Bush v. Lucas, 462
U. S. 367, 390 (1983); a race-discrimination suit against
military officers, Chappell v. Wallace, 462 U. S. 296, 297,
304–305 (1983); a substantive due process suit against
military officers, United States v. Stanley, 483 U. S. 669,
671–672, 683–684 (1987); a procedural due process suit
against Social Security officials, Schweiker v. Chilicky, 487
U. S. 412, 414 (1988); a procedural due process suit
against a federal agency for wrongful termination, FDIC v.
Meyer, 510 U. S. 471, 473–474 (1994); an Eighth Amend-
12                    ZIGLAR v. ABBASI

                     Opinion of the Court

ment suit against a private prison operator, Malesko,
supra, at 63; a due process suit against officials from the
Bureau of Land Management, Wilkie v. Robbins, 551 U. S.
537, 547–548, 562 (2007); and an Eighth Amendment suit
against prison guards at a private prison, Minneci v.
Pollard, 565 U. S. 118, 120 (2012).
    When a party seeks to assert an implied cause of action
under the Constitution itself, just as when a party seeks to
assert an implied cause of action under a federal statute,
separation-of-powers principles are or should be central to
the analysis. The question is “who should decide” whether
to provide for a damages remedy, Congress or the courts?
Bush, 462 U. S., at 380.
    The answer most often will be Congress. When an issue
“ ‘involves a host of considerations that must be weighed
and appraised,’ ” it should be committed to “ ‘those who
write the laws’ ” rather than “ ‘those who interpret them.’ ”
Ibid. (quoting United States v. Gilman, 347 U. S. 507,
512–513 (1954)). In most instances, the Court’s prece-
dents now instruct, the Legislature is in the better posi-
tion to consider if “ ‘the public interest would be served’ ”
by imposing a “‘new substantive legal liability.’” Schweiker,
supra, at 426–427 (quoting Bush, supra, at 390). As a
result, the Court has urged “caution” before “extending
Bivens remedies into any new context.” Malesko, supra, at
74. The Court’s precedents now make clear that a Bivens
remedy will not be available if there are “ ‘special factors
counselling hesitation in the absence of affirmative action
by Congress.’ ” Carlson, 446 U. S., at 18 (quoting Bivens,
403 U. S., at 396).
    This Court has not defined the phrase “special factors
counselling hesitation.” The necessary inference, though,
is that the inquiry must concentrate on whether the Judi-
ciary is well suited, absent congressional action or instruc-
tion, to consider and weigh the costs and benefits of allow-
ing a damages action to proceed. Thus, to be a “special
                 Cite as: 582 U. S. ____ (2017)         13

                     Opinion of the Court

factor counselling hesitation,” a factor must cause a
court to hesitate before answering that question in the
affirmative.
   It is not necessarily a judicial function to establish
whole categories of cases in which federal officers must
defend against personal liability claims in the complex
sphere of litigation, with all of its burdens on some and
benefits to others. It is true that, if equitable remedies
prove insufficient, a damages remedy might be necessary
to redress past harm and deter future violations. Yet the
decision to recognize a damages remedy requires an as-
sessment of its impact on governmental operations sys-
temwide. Those matters include the burdens on Govern-
ment employees who are sued personally, as well as the
projected costs and consequences to the Government itself
when the tort and monetary liability mechanisms of the
legal system are used to bring about the proper formula-
tion and implementation of public policies. These and
other considerations may make it less probable that Con-
gress would want the Judiciary to entertain a damages
suit in a given case.
   Sometimes there will be doubt because the case arises in
a context in which Congress has designed its regulatory
authority in a guarded way, making it less likely that
Congress would want the Judiciary to interfere. See
Chappell, supra, at 302 (military); Stanley, supra, at 679
(same); Meyer, supra, at 486 (public purse); Wilkie, supra,
at 561–562 (federal land). And sometimes there will be
doubt because some other feature of a case—difficult to
predict in advance—causes a court to pause before acting
without express congressional authorization. In sum, if
there are sound reasons to think Congress might doubt
the efficacy or necessity of a damages remedy as part of
the system for enforcing the law and correcting a wrong,
the courts must refrain from creating the remedy in order
to respect the role of Congress in determining the nature
14                   ZIGLAR v. ABBASI

                     Opinion of the Court

and extent of federal-court jurisdiction under Article III.
  In a related way, if there is an alternative remedial
structure present in a certain case, that alone may limit
the power of the Judiciary to infer a new Bivens cause of
action. For if Congress has created “any alternative,
existing process for protecting the [injured party’s] inter-
est” that itself may “amoun[t] to a convincing reason for
the Judicial Branch to refrain from providing a new and
freestanding remedy in damages.” Wilkie, supra, at 550;
see also Bush, supra, at 385–388 (recognizing that civil-
service regulations provided alternative means for relief);
Malesko, 534 U. S., at 73–74 (recognizing that state tort
law provided alternative means for relief); Minneci, supra,
at 127–130 (same).
                             III
   It is appropriate now to turn first to the Bivens claims
challenging the conditions of confinement imposed on
respondents pursuant to the formal policy adopted by the
Executive Officials in the wake of the September 11 at-
tacks. The Court will refer to these claims as the “deten-
tion policy claims.” The detention policy claims allege that
petitioners violated respondents’ due process and equal
protection rights by holding them in restrictive conditions
of confinement; the claims further allege that the Wardens
violated the Fourth and Fifth Amendments by subjecting
respondents to frequent strip searches. The term “deten-
tion policy claims” does not include respondents’ claim
alleging that Warden Hasty allowed guards to abuse the
detainees. That claim will be considered separately, and
further, below. At this point, the question is whether,
having considered the relevant special factors in the whole
context of the detention policy claims, the Court should
extend a Bivens-type remedy to those claims.
                 Cite as: 582 U. S. ____ (2017)           15

                     Opinion of the Court 


                               A

  Before allowing respondents’ detention policy claims to
proceed under Bivens, the Court of Appeals did not per-
form any special factors analysis at all. 789 F. 3d, at 237.
The reason, it said, was that the special factors analysis is
necessary only if a plaintiff asks for a Bivens remedy in a
new context. 789 F. 3d, at 234. And in the Court of Ap-
peals’ view, the context here was not new. Id., at 235.
  To determine whether the Bivens context was novel, the
Court of Appeals employed a two-part test. First, it asked
whether the asserted constitutional right was at issue in a
previous Bivens case. 789 F. 3d, at 234. Second, it asked
whether the mechanism of injury was the same mecha-
nism of injury in a previous Bivens case. 789 F. 3d, at 234.
Under the Court of Appeals’ approach, if the answer to
both questions is “yes,” then the context is not new and no
special factors analysis is required. Ibid.
  That approach is inconsistent with the analysis in
Malesko. Before the Court decided that case, it had ap-
proved a Bivens action under the Eighth Amendment
against federal prison officials for failure to provide medi-
cal treatment. See Carlson, 446 U. S., at 16, n. 1, 18–19.
In Malesko, the plaintiff sought relief against a private
prison operator in almost parallel circumstances. 534
U. S., at 64. In both cases, the right at issue was the
same: the Eighth Amendment right to be free from cruel
and unusual punishment. And in both cases, the mecha-
nism of injury was the same: failure to provide adequate
medical treatment. Thus, if the approach followed by the
Court of Appeals is the correct one, this Court should have
held that the cases arose in the same context, obviating
any need for a special factors inquiry.
  That, however, was not the controlling analytic frame-
work in Malesko. Even though the right and the mecha-
nism of injury were the same as they were in Carlson, the
Court held that the contexts were different. 534 U. S., at
16                    ZIGLAR v. ABBASI

                      Opinion of the Court

70, and n. 4. The Court explained that special factors
counseled hesitation and that the Bivens remedy was
therefore unavailable. 534 U. S., at 74.
  For similar reasons, the holding of the Court of Appeals
in the instant suit is inconsistent with this Court’s ana-
lytic framework in Chappell. In Davis, decided before the
Court’s cautionary instructions with respect to Bivens
suits, see supra, at 11–12, the Court had held that an
employment-discrimination claim against a Congressman
could proceed as a Bivens-type action. Davis, 442 U. S., at
230–231. In Chappell, however, the cautionary rules were
applicable; and, as a result, a similar discrimination suit
against military officers was not allowed to proceed. It is
the Chappell framework that now controls; and, under it,
the Court of Appeals erred by holding that this suit did
not present a new Bivens context.
  The proper test for determining whether a case presents
a new Bivens context is as follows. If the case is different
in a meaningful way from previous Bivens cases decided
by this Court, then the context is new. Without endeavor-
ing to create an exhaustive list of differences that are
meaningful enough to make a given context a new one,
some examples might prove instructive. A case might
differ in a meaningful way because of the rank of the
officers involved; the constitutional right at issue; the
generality or specificity of the official action; the extent of
judicial guidance as to how an officer should respond to
the problem or emergency to be confronted; the statutory
or other legal mandate under which the officer was operat-
ing; the risk of disruptive intrusion by the Judiciary into
the functioning of other branches; or the presence of po-
tential special factors that previous Bivens cases did not
consider.
  In the present suit, respondents’ detention policy claims
challenge the confinement conditions imposed on illegal
aliens pursuant to a high-level executive policy created in
                  Cite as: 582 U. S. ____ (2017)           17

                      Opinion of the Court

the wake of a major terrorist attack on American soil.
Those claims bear little resemblance to the three Bivens
claims the Court has approved in the past: a claim against
FBI agents for handcuffing a man in his own home with-
out a warrant; a claim against a Congressman for firing
his female secretary; and a claim against prison officials
for failure to treat an inmate’s asthma. See Bivens, 403
U. S. 388; Davis, 442 U. S. 228; Chappell, 462 U. S. 296.
The Court of Appeals therefore should have held that this
was a new Bivens context. Had it done so, it would have
recognized that a special factors analysis was required
before allowing this damages suit to proceed.
                               B
   After considering the special factors necessarily impli-
cated by the detention policy claims, the Court now holds
that those factors show that whether a damages action
should be allowed is a decision for the Congress to make,
not the courts.
   With respect to the claims against the Executive Offi-
cials, it must be noted that a Bivens action is not “a proper
vehicle for altering an entity’s policy.” Malesko, supra, at
74. Furthermore, a Bivens claim is brought against the
individual official for his or her own acts, not the acts of
others. “The purpose of Bivens is to deter the officer.”
Meyer, 510 U. S., at 485. Bivens is not designed to hold
officers responsible for acts of their subordinates. See
Iqbal, 556 U. S., at 676 (“Government officials may not be
held liable for the unconstitutional conduct of their subor-
dinates under a theory of respondeat superior ”).
   Even if the action is confined to the conduct of a particu-
lar Executive Officer in a discrete instance, these claims
would call into question the formulation and implementa-
tion of a general policy. This, in turn, would necessarily
require inquiry and discovery into the whole course of the
discussions and deliberations that led to the policies and
18                   ZIGLAR v. ABBASI

                     Opinion of the Court

governmental acts being challenged. These consequences
counsel against allowing a Bivens action against the Exec-
utive Officials, for the burden and demand of litigation
might well prevent them—or, to be more precise, future
officials like them—from devoting the time and effort
required for the proper discharge of their duties. See
Cheney v. United States Dist. Court for D. C., 542 U. S.
367, 382 (2004) (noting “the paramount necessity of pro-
tecting the Executive Branch from vexatious litigation
that might distract it from the energetic performance of its
constitutional duties”).
  A closely related problem, as just noted, is that the
discovery and litigation process would either border upon
or directly implicate the discussion and deliberations that
led to the formation of the policy in question. See Federal
Open Market Comm. v. Merrill, 443 U. S. 340, 360 (1979)
(noting that disclosure of Executive Branch documents
“could inhibit the free flow of advice, including analysis,
reports, and expression of opinion within an agency”).
Allowing a damages suit in this context, or in a like con-
text in other circumstances, would require courts to inter-
fere in an intrusive way with sensitive functions of the
Executive Branch. See Clinton v. Jones, 520 U. S. 681,
701 (1997) (recognizing that “ ‘[e]ven when a branch does
not arrogate power to itself . . . the separation-of-powers
doctrine requires that a branch not impair another in the
performance of its constitutional duties’ ” (quoting Loving
v. United States, 517 U. S. 748, 757 (1996))). These con-
siderations also counsel against allowing a damages claim
to proceed against the Executive Officials. See Cheney,
supra, at 385 (noting that “special considerations control”
when a case implicates “the Executive Branch’s interests
in maintaining the autonomy of its office and safeguarding
the confidentiality of its communications”).
  In addition to this special factor, which applies to the
claims against the Executive Officials, there are three
                 Cite as: 582 U. S. ____ (2017)           19

                     Opinion of the Court

other special factors that apply as well to the detention
policy claims against all of the petitioners. First, respond-
ents’ detention policy claims challenge more than standard
“law enforcement operations.” United States v. Verdugo-
Urquidez, 494 U. S. 259, 273 (1990). They challenge as
well major elements of the Government’s whole response
to the September 11 attacks, thus of necessity requiring
an inquiry into sensitive issues of national security. Were
this inquiry to be allowed in a private suit for damages,
the Bivens action would assume dimensions far greater
than those present in Bivens itself, or in either of its two
follow-on cases, or indeed in any putative Bivens case yet
to come before the Court.
   National-security policy is the prerogative of the Con-
gress and President. See U. S. Const., Art. I, §8; Art. II,
§1, §2. Judicial inquiry into the national-security realm
raises “concerns for the separation of powers in trenching
on matters committed to the other branches.” Christopher
v. Harbury, 536 U. S. 403, 417 (2002). These concerns are
even more pronounced when the judicial inquiry comes in
the context of a claim seeking money damages rather than
a claim seeking injunctive or other equitable relief. The
risk of personal damages liability is more likely to cause
an official to second-guess difficult but necessary decisions
concerning national-security policy.
   For these and other reasons, courts have shown defer-
ence to what the Executive Branch “has determined . . . is
‘essential to national security.’ ” Winter v. Natural Re-
sources Defense Council, Inc., 555 U. S. 7, 24, 26 (2008).
Indeed, “courts traditionally have been reluctant to in-
trude upon the authority of the Executive in military and
national security affairs” unless “Congress specifically has
provided otherwise.” Department of Navy v. Egan, 484
U. S. 518, 530 (1988). Congress has not provided other-
wise here.
   There are limitations, of course, on the power of the
20                     ZIGLAR v. ABBASI

                       Opinion of the Court

Executive under Article II of the Constitution and in the
powers authorized by congressional enactments, even with
respect to matters of national security. See, e.g., Hamdi v.
Rumsfeld, 542 U. S. 507, 527, 532–537 (2004) (plurality
opinion) (“Whatever power the United States Constitution
envisions for the Executive . . . in times of conflict, it most
assuredly envisions a role for all three branches when
individual liberties are at stake”); Boumediene v. Bush,
553 U. S. 723, 798 (2008) (“Liberty and security can be
reconciled; and in our system they are reconciled within
the framework of the law”). And national-security con-
cerns must not become a talisman used to ward off incon-
venient claims—a “label” used to “cover a multitude of
sins.” Mitchell v. Forsyth, 472 U. S. 511, 523 (1985). This
“ ‘danger of abuse’ ” is even more heightened given “ ‘the
difficulty of defining’ ” the “ ‘security interest’ ” in domestic
cases. Ibid. (quoting United States v. United States Dist.
Court for Eastern Dist. of Mich., 407 U. S. 297, 313–314
(1972)).
   Even so, the question is only whether “congressionally
uninvited intrusion” is “inappropriate” action for the
Judiciary to take. Stanley, 483 U. S., at 683. The factors
discussed above all suggest that Congress’ failure to pro-
vide a damages remedy might be more than mere over-
sight, and that congressional silence might be more than
“inadvertent.” Schweiker, 487 U. S., at 423. This possibil-
ity counsels hesitation “in the absence of affirmative ac-
tion by Congress.” Bivens, 403 U. S., at 396.
   Furthermore, in any inquiry respecting the likely or
probable intent of Congress, the silence of Congress is
relevant; and here that silence is telling. In the almost 16
years since September 11, the Federal Government’s
responses to that terrorist attack have been well docu-
mented. Congressional interest has been “frequent and
intense,” Schweiker, supra, at 425, and some of that inter-
est has been directed to the conditions of confinement at
                  Cite as: 582 U. S. ____ (2017)            21

                      Opinion of the Court

issue here. Indeed, at Congress’ behest, the Department
of Justice’s Office of the Inspector General compiled a 300-
page report documenting the conditions in the MDC in
great detail. See 789 F. 3d, at 279 (opinion of Raggi, J.)
(noting that the USA PATRIOT Act required “the De-
partment’s Inspector General to review and report semi-
annually to Congress on any identified abuses of civil
rights and civil liberties in fighting terrorism”). Neverthe-
less, “[a]t no point did Congress choose to extend to any
person the kind of remedies that respondents seek in this
lawsuit.” Schweiker, 487 U. S., at 426.
   This silence is notable because it is likely that high-level
policies will attract the attention of Congress. Thus, when
Congress fails to provide a damages remedy in circum-
stances like these, it is much more difficult to believe that
“congressional inaction” was “inadvertent.” Id., at 423.
   It is of central importance, too, that this is not a case
like Bivens or Davis in which “it is damages or nothing.”
Bivens, supra, at 410 (Harlan, J., concurring in judgment);
Davis, 442 U. S., at 245. Unlike the plaintiffs in those
cases, respondents do not challenge individual instances of
discrimination or law enforcement overreach, which due to
their very nature are difficult to address except by way of
damages actions after the fact. Respondents instead
challenge large-scale policy decisions concerning the con-
ditions of confinement imposed on hundreds of prisoners.
To address those kinds of decisions, detainees may seek
injunctive relief. And in addition to that, we have left
open the question whether they might be able to challenge
their confinement conditions via a petition for a writ of
habeas corpus. See Bell v. Wolfish, 441 U. S. 520, 526, n. 6
(1979) (“[W]e leave to another day the question of the
propriety of using a writ of habeas corpus to obtain review
of the conditions of confinement”); Preiser v. Rodriguez,
411 U. S. 475, 499 (1973) (“When a prisoner is put under
additional and unconstitutional restraints during his
22                    ZIGLAR v. ABBASI

                     Opinion of the Court

lawful custody, it is arguable that habeas corpus will lie to
remove the restraints making custody illegal”).
   Indeed, the habeas remedy, if necessity required its use,
would have provided a faster and more direct route to
relief than a suit for money damages. A successful habeas
petition would have required officials to place respondents
in less-restrictive conditions immediately; yet this dam-
ages suit remains unresolved some 15 years later. (As in
Bell and Preiser, the Court need not determine the scope
or availability of the habeas corpus remedy, a question
that is not before the Court and has not been briefed or
argued.) In sum, respondents had available to them “ ‘other
alternative forms of judicial relief.’ ” Minneci, 565 U. S.,
at 124. And when alternative methods of relief are avail-
able, a Bivens remedy usually is not. See Bush, 462 U. S.,
at 386–388; Schweiker, supra, at 425–426; Malesko, 534
U. S., at 73–74; Minneci, supra, at 125–126.
   There is a persisting concern, of course, that absent a
Bivens remedy there will be insufficient deterrence to
prevent officers from violating the Constitution. In cir-
cumstances like those presented here, however, the stakes
on both sides of the argument are far higher than in past
cases the Court has considered. If Bivens liability were to
be imposed, high officers who face personal liability for
damages might refrain from taking urgent and lawful
action in a time of crisis. And, as already noted, the costs
and difficulties of later litigation might intrude upon and
interfere with the proper exercise of their office.
   On the other side of the balance, the very fact that some
executive actions have the sweeping potential to affect the
liberty of so many is a reason to consider proper means to
impose restraint and to provide some redress from injury.
There is therefore a balance to be struck, in situations like
this one, between deterring constitutional violations and
freeing high officials to make the lawful decisions neces-
sary to protect the Nation in times of great peril. Cf.
                  Cite as: 582 U. S. ____ (2017)            23

                      Opinion of the Court

Stanley, supra, at 681 (noting that the special-factors
analysis in that case turned on “how much occasional,
unintended impairment of military discipline one is will-
ing to tolerate”). The proper balance is one for the Con-
gress, not the Judiciary, to undertake. For all of these
reasons, the Court of Appeals erred by allowing respond-
ents’ detention policy claims to proceed under Bivens.
                               IV 

                                A

   One of respondents’ claims under Bivens requires a
different analysis: the prisoner abuse claim against the
MDC’s warden, Dennis Hasty. The allegation is that
Warden Hasty violated the Fifth Amendment by allowing
prison guards to abuse respondents.
   The warden argues, as an initial matter, that the com-
plaint does not “ ‘state a claim to relief that is plausible on
its face.’ ” Iqbal, 556 U. S., at 678 (quoting Bell Atlantic
Corp. v. Twombly, 550 U. S. 544, 570 (2007)). Applying its
precedents, the Court of Appeals held that the substantive
standard for the sufficiency of the claim is whether the
warden showed “deliberate indifference” to prisoner abuse.
789 F. 3d, at 249–250. The parties appear to agree on this
standard, and, for purposes of this case, the Court as-
sumes it to be correct.
   The complaint alleges that guards routinely abused
respondents; that the warden encouraged the abuse by
referring to respondents as “terrorists”; that he prevented
respondents from using normal grievance procedures; that
he stayed away from the Unit to avoid seeing the abuse;
that he was made aware of the abuse via “inmate com-
plaints, staff complaints, hunger strikes, and suicide
attempts”; that he ignored other “direct evidence of [the]
abuse, including logs and other official [records]”; that he
took no action “to rectify or address the situation”; and
that the abuse resulted in the injuries described above, see
24                     ZIGLAR v. ABBASI

                      Opinion of the Court

supra, at 4. These allegations—assumed here to be true,
subject to proof at a later stage—plausibly show the war-
den’s deliberate indifference to the abuse. Consistent with
the opinion of every judge in this case to have considered
the question, including the dissenters in the Court of
Appeals, the Court concludes that the prisoner abuse
allegations against Warden Hasty state a plausible ground
to find a constitutional violation if a Bivens remedy is to be
implied.
   Warden Hasty argues, however, that Bivens ought not
to be extended to this instance of alleged prisoner abuse.
As noted above, the first question a court must ask in a
case like this one is whether the claim arises in a new
Bivens context, i.e., whether “the case is different in a
meaningful way from previous Bivens cases decided by
this Court.” Supra, at 16.
   It is true that this case has significant parallels to one of
the Court’s previous Bivens cases, Carlson v. Green, 446
U. S. 14. There, the Court did allow a Bivens claim for
prisoner mistreatment—specifically, for failure to provide
medical care. And the allegations of injury here are just
as compelling as those at issue in Carlson. This is espe-
cially true given that the complaint alleges serious viola-
tions of Bureau of Prisons policy. See 28 CFR §552.20
(2016) (providing that prison staff may use force “only as a
last alternative after all other reasonable efforts to resolve
a situation have failed” and that staff may “use only that
amount of force necessary to [ensure prison safety and
security]”); §552.22(j) (“All incidents involving the use of
force . . . must be carefully documented”); §542.11 (requir-
ing the warden to investigate certain complaints of inmate
abuse).
   Yet even a modest extension is still an extension. And
this case does seek to extend Carlson to a new context. As
noted above, a case can present a new context for Bivens
purposes if it implicates a different constitutional right; if
                 Cite as: 582 U. S. ____ (2017)           25

                     Opinion of the Court

judicial precedents provide a less meaningful guide for
official conduct; or if there are potential special factors
that were not considered in previous Bivens cases. See
supra, at 13.
   The constitutional right is different here, since Carlson
was predicated on the Eighth Amendment and this claim
is predicated on the Fifth. See 446 U. S., at 16. And the
judicial guidance available to this warden, with respect to
his supervisory duties, was less developed. The Court has
long made clear the standard for claims alleging failure to
provide medical treatment to a prisoner—“deliberate
indifference to serious medical needs.” Estelle v. Gamble,
429 U. S. 97, 104 (1976). The standard for a claim alleging
that a warden allowed guards to abuse pre-trial detainees
is less clear under the Court’s precedents.
   This case also has certain features that were not consid-
ered in the Court’s previous Bivens cases and that might
discourage a court from authorizing a Bivens remedy. As
noted above, the existence of alternative remedies usually
precludes a court from authorizing a Bivens action. Su-
pra, at 14. And there might have been alternative reme-
dies available here, for example, a writ of habeas corpus,
Wolfish, 441 U. S., at 526, n. 6; an injunction requiring the
warden to bring his prison into compliance with the regu-
lations discussed above; or some other form of equitable
relief.
   Furthermore, legislative action suggesting that Con-
gress does not want a damages remedy is itself a factor
counseling hesitation. See supra, at 14. Some 15 years
after Carlson was decided, Congress passed the Prison
Litigation Reform Act of 1995, which made comprehensive
changes to the way prisoner abuse claims must be brought
in federal court. See 42 U. S. C. §1997e. So it seems clear
that Congress had specific occasion to consider the matter
of prisoner abuse and to consider the proper way to rem-
edy those wrongs. This Court has said in dicta that the
26                    ZIGLAR v. ABBASI

                     Opinion of the Court

Act’s exhaustion provisions would apply to Bivens suits.
See Porter v. Nussle, 534 U. S. 516, 524 (2002). But the
Act itself does not provide for a standalone damages rem-
edy against federal jailers. It could be argued that this
suggests Congress chose not to extend the Carlson dam-
ages remedy to cases involving other types of prisoner
mistreatment.
   The differences between this claim and the one in Carl-
son are perhaps small, at least in practical terms. Given
this Court’s expressed caution about extending the Bivens
remedy, however, the new-context inquiry is easily satis-
fied. Some differences, of course, will be so trivial that
they will not suffice to create a new Bivens context. But
here the differences identified above are at the very least
meaningful ones. Thus, before allowing this claim to
proceed under Bivens, the Court of Appeals should have
performed a special factors analysis. It should have ana-
lyzed whether there were alternative remedies available
or other “sound reasons to think Congress might doubt the
efficacy or necessity of a damages remedy” in a suit like
this one. Supra, at 15.
                              B
   Although the Court could perform that analysis in the
first instance, the briefs have concentrated almost all of
their efforts elsewhere. Given the absence of a compre-
hensive presentation by the parties, and the fact that the
Court of Appeals did not conduct the analysis, the Court
declines to perform the special factors analysis itself. The
better course is to vacate the judgment below, allowing the
Court of Appeals or the District Court to do so on remand.
                              V
   One issue remains to be addressed: the claim that
petitioners are subject to liability for civil conspiracy
under 42 U. S. C. §1985(3). Unlike the prisoner abuse
claim just discussed, this claim implicates the activities of
                  Cite as: 582 U. S. ____ (2017)           27

                      Opinion of the Court

all the petitioners—the Executive Officials as well as the
Wardens—in creating the conditions of confinement at
issue here.
   The civil-conspiracy prohibition contained in §1985(3)
was enacted as a significant part of the civil rights legisla-
tion passed in the aftermath of the Civil War. See Car-
penters v. Scott, 463 U. S. 825, 834–837 (1983) (detailing
the legislative history of §1985(3)); Griffin v. Breckenridge,
403 U. S. 88, 99–101 (1971) (same); Great American Fed.
Sav. & Loan Assn. v. Novotny, 442 U. S. 366, 379 (1979)
(Powell, J., concurring) (describing §1985(3) as a “Civil
War Era remedial statute”). The statute imposes liability
on two or more persons who “conspire . . . for the purpose
of depriving . . . any person or class of persons of the equal
protection of the laws.” §1985(3). In the instant suit,
respondents allege that petitioners violated the statute by
“agreeing to implement a policy” under which respondents
would be detained in harsh conditions “because of their
race, religion, ethnicity, and national origin.” Assuming
these allegations to be true and well pleaded, the question
is whether petitioners are entitled to qualified immunity.
                             A
  The qualified immunity rule seeks a proper balance
between two competing interests. On one hand, damages
suits “may offer the only realistic avenue for vindication of
constitutional guarantees.” Harlow v. Fitzgerald, 457
U. S. 800, 814 (1982). “On the other hand, permitting
damages suits against government officials can entail
substantial social costs, including the risk that fear of
personal monetary liability and harassing litigation will
unduly inhibit officials in the discharge of their duties.”
Anderson v. Creighton, 483 U. S. 635, 638 (1987). As one
means to accommodate these two objectives, the Court has
held that Government officials are entitled to qualified
immunity with respect to “discretionary functions” per-
28                    ZIGLAR v. ABBASI

                     Opinion of the Court

formed in their official capacities. Ibid. The doctrine of
qualified immunity gives officials “breathing room to make
reasonable but mistaken judgments about open legal
questions.” Ashcroft v. al-Kidd, 563 U. S. 731, 743 (2011).
   The Court’s cases provide additional instruction to
define and implement that immunity. Whether qualified
immunity can be invoked turns on the “objective legal
reasonableness” of the official’s acts. Harlow, supra, at
819. And reasonableness of official action, in turn, must
be “assessed in light of the legal rules that were clearly
established at the time [the action] was taken.” Anderson,
supra, at 639 (internal quotation marks omitted); see also
Mitchell, 472 U. S., at 528. This requirement—that an
official loses qualified immunity only for violating clearly
established law—protects officials accused of violating
“extremely abstract rights.” Anderson, supra, at 639.
   The Fourth Amendment provides an example of how
qualified immunity functions with respect to abstract
rights. By its plain terms, the Amendment forbids unrea-
sonable searches and seizures, yet it may be difficult for
an officer to know whether a search or seizure will be
deemed reasonable given the precise situation encoun-
tered. See Saucier v. Katz, 533 U. S. 194, 205 (2001) (“It is
sometimes difficult for an officer to determine how the
relevant legal doctrine, here excessive force, will apply to
the factual situation the officer confronts”). For this rea-
son, “[t]he dispositive question is ‘whether the violative
nature of particular conduct is clearly established.’ ”
Mullenix v. Luna, 577 U. S. ___, ___ (2015) ( per curiam)
(slip op., at 5) (quoting Ashcroft, supra, at 742).
    It is not necessary, of course, that “the very action in
question has previously been held unlawful.” Anderson,
supra, at 640. That is, an officer might lose qualified
immunity even if there is no reported case “directly on
point.” Ashcroft, supra, at 741. But “in the light of pre-
existing law,” the unlawfulness of the officer’s conduct
                  Cite as: 582 U. S. ____ (2017)            29

                      Opinion of the Court

“must be apparent.” Anderson, supra, at 640. To subject
officers to any broader liability would be to “disrupt the
balance that our cases strike between the interests in
vindication of citizens’ constitutional rights and in public
officials’ effective performance of their duties.” Davis v.
Scherer, 468 U. S. 183, 195 (1984). For then, both as a
practical and legal matter, it would be difficult for officials
“reasonably [to] anticipate when their conduct may give
rise to liability for damages.” Ibid.
   In light of these concerns, the Court has held that quali-
fied immunity protects “all but the plainly incompetent or
those who knowingly violate the law.” Malley v. Briggs,
475 U. S. 335, 341 (1986). To determine whether a given
officer falls into either of those two categories, a court
must ask whether it would have been clear to a reasonable
officer that the alleged conduct “was unlawful in the situa-
tion he confronted.” Saucier, supra, at 202. If so, then the
defendant officer must have been either incompetent or
else a knowing violator of the law, and thus not entitled to
qualified immunity. If not, however—i.e., if a reasonable
officer might not have known for certain that the conduct
was unlawful—then the officer is immune from liability.
                               B
   Under these principles, it must be concluded that rea-
sonable officials in petitioners’ positions would not have
known, and could not have predicted, that §1985(3) pro-
hibited their joint consultations and the resulting policies
that caused the injuries alleged.
   At least two aspects of the complaint indicate that peti-
tioners’ potential liability for this statutory offense would
not have been known or anticipated by reasonable officials
in their position. First, the conspiracy recited in the com-
plaint is alleged to have been between or among officers in
the same branch of the Government (the Executive
Branch) and in the same Department (the Department of
30                    ZIGLAR v. ABBASI

                      Opinion of the Court

Justice). Second, the discussions were the preface to, and
the outline of, a general and far-reaching policy.
  As to the fact that these officers were in the same De-
partment, an analogous principle discussed in the context
of antitrust law is instructive. The Court’s precedent
indicates that there is no unlawful conspiracy when offic-
ers within a single corporate entity consult among them-
selves and then adopt a policy for the entity. See Copper-
weld Corp v. Independence Tube Corp., 467 U. S. 752,
769–771 (1984). Under this principle—sometimes called the
intracorporate-conspiracy doctrine—an agreement be-
tween or among agents of the same legal entity, when the
agents act in their official capacities, is not an unlawful
conspiracy. Ibid. The rule is derived from the nature of
the conspiracy prohibition.        Conspiracy requires an
agreement—and in particular an agreement to do an
unlawful act—between or among two or more separate
persons. When two agents of the same legal entity make
an agreement in the course of their official duties, how-
ever, as a practical and legal matter their acts are attributed
to their principal. And it then follows that there has not
been an agreement between two or more separate people.
See id., at 771 (analogizing to “a multiple team of horses
drawing a vehicle under the control of a single driver”).
    To be sure, this Court has not given its approval to this
doctrine in the specific context of §1985(3). See Great
American, 442 U. S., at 372, n. 11. There is a division in
the courts of appeals, moreover, respecting the validity or
correctness of the intracorporate-conspiracy doctrine with
reference to §1985 conspiracies. See Hull v. Shuck, 501
U. S. 1261, 1261–1262 (1991) (White, J., dissenting from
denial of certiorari) (discussing the Circuit split); Bowie v.
Maddox, 642 F. 3d 1122, 1130–1131 (CADC 2011) (detail-
ing a longstanding split about whether the intracorporate-
conspiracy doctrine applies to civil rights conspiracies).
Nothing in this opinion should be interpreted as either
                 Cite as: 582 U. S. ____ (2017)           31

                     Opinion of the Court

approving or disapproving the intracorporate-conspiracy
doctrine’s application in the context of an alleged §1985(3)
violation. The Court might determine, in some later case,
that different considerations apply to a conspiracy respect-
ing equal protection guarantees, as distinct from a con-
spiracy in the antitrust context. Yet the fact that the
courts are divided as to whether or not a §1985(3) conspir-
acy can arise from official discussions between or among
agents of the same entity demonstrates that the law on
the point is not well established. When the courts are
divided on an issue so central to the cause of action al-
leged, a reasonable official lacks the notice required before
imposing liability. See Wilson v. Layne, 526 U. S. 603, 618
(1999) (noting that it would be “unfair” to subject officers
to damages liability when even “judges . . . disagree”);
Reichle v. Howards, 566 U. S. 658, 669–670 (2012) (same).
  In addition to the concern that agents of the same legal
entity are not distinct enough to conspire with one another,
there are other sound reasons to conclude that conver-
sations and agreements between and among federal offi-
cials in the same Department should not be the subject of
a private cause of action for damages under §1985(3). To
state a claim under §1985(3), a plaintiff must first show
that the defendants conspired—that is, reached an agree-
ment—with one another. See Carpenters, 463 U. S., at
828 (stating that the elements of a §1985(3) claim include
“a conspiracy”). Thus, a §1985(3) claim against federal
officials by necessity implicates the substance of their
official discussions.
  As indicated above with respect to other claims in this
suit, open discussion among federal officers is to be en-
couraged, so that they can reach consensus on the policies
a department of the Federal Government should pursue.
See supra, at 17–18. Close and frequent consultations to
facilitate the adoption and implementation of policies are
essential to the orderly conduct of governmental affairs.
32                    ZIGLAR v. ABBASI

                     Opinion of the Court

Were those discussions, and the resulting policies, to be
the basis for private suits seeking damages against the
officials as individuals, the result would be to chill the
interchange and discourse that is necessary for the adop-
tion and implementation of governmental policies. See
Cheney, 542 U. S., at 383 (discussing the need for confi-
dential communications among Executive Branch offi-
cials); Merrill, 443 U. S., at 360 (same).
   These considerations suggest that officials employed by
the same governmental department do not conspire when
they speak to one another and work together in their
official capacities. Whether that contention should prevail
need not be decided here. It suffices to say that the ques-
tion is sufficiently open so that the officials in this suit
could not be certain that §1985(3) was applicable to their
discussions and actions. Thus, the law respondents seek
to invoke cannot be clearly established. It follows that
reasonable officers in petitioners’ positions would not have
known with any certainty that the alleged agreements
were forbidden by law. See Saucier, 533 U. S., at 202.
Petitioners are entitled to qualified immunity with respect
to the claims under 42 U. S. C. §1985(3).
                         *     *   *
  If the facts alleged in the complaint are true, then what
happened to respondents in the days following September
11 was tragic. Nothing in this opinion should be read to
condone the treatment to which they contend they were
subjected. The question before the Court, however, is not
whether petitioners’ alleged conduct was proper, nor
whether it gave decent respect to respondents’ dignity and
well-being, nor whether it was in keeping with the idea of
the rule of law that must inspire us even in times of crisis.
  Instead, the question with respect to the Bivens claims
is whether to allow an action for money damages in the
absence of congressional authorization. For the reasons
                 Cite as: 582 U. S. ____ (2017)           33

                     Opinion of the Court

given above, the Court answers that question in the nega-
tive as to the detention policy claims. As to the prisoner
abuse claim, because the briefs have not concentrated on
that issue, the Court remands to allow the Court of Ap-
peals to consider the claim in light of the Bivens analysis
set forth above.
   The question with respect to the §1985(3) claim is
whether a reasonable officer in petitioners’ position would
have known the alleged conduct was an unlawful conspir-
acy. For the reasons given above, the Court answers that
question, too, in the negative.
   The judgment of the Court of Appeals is reversed as to
all of the claims except the prisoner abuse claim against
Warden Hasty. The judgment of the Court of Appeals
with respect to that claim is vacated, and that case is
remanded for further proceedings.
                                            It is so ordered.

  JUSTICE SOTOMAYOR, JUSTICE KAGAN, and JUSTICE
GORSUCH took no part in the consideration or decision of
these cases.
                 Cite as: 582 U. S. ____ (2017)           1

                     Opinion of THOMAS, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

              Nos. 15–1358, 15–1359 and 15–1363
                         _________________


            JAMES W. ZIGLAR, PETITIONER
15–1358                  v.
             AHMER IQBAL ABBASI, ET AL.

     JOHN D. ASHCROFT, FORMER ATTORNEY
         GENERAL, ET AL., PETITIONERS
15–1359               v.
          AHMER IQBAL ABBASI, ET AL.

          DENNIS HASTY, ET AL., PETITIONERS
15–1363                  v.
             AHMER IQBAL ABBASI, ET AL.
ON WRITS OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                        [June 19, 2017]

  JUSTICE THOMAS, concurring in part and concurring in
the judgment.
  I join the Court’s opinion except for Part IV–B. I write
separately to express my view on the Court’s decision to
remand some of respondents’ claims under Bivens v. Six
Unknown Fed. Narcotics Agents, 403 U. S. 388 (1971), and
my concerns about our qualified immunity precedents.
                             I
  With respect to respondents’ Bivens claims, I join the
opinion of the Court to the extent it reverses the Second
Circuit’s ruling. The Court correctly applies our prece-
dents to hold that Bivens does not supply a cause of action
against petitioners for most of the alleged Fourth and
2                     ZIGLAR v. ABBASI

                     Opinion of THOMAS, J.

Fifth Amendment violations. It also correctly recognizes
that respondents’ claims against petitioner Dennis Hasty
seek to extend Bivens to a new context. See ante, at 24.
   I concur in the judgment of the Court vacating the Court
of Appeals’ judgment with regard to claims against Hasty.
Ante, at 29. I have previously noted that “ ‘Bivens is a relic
of the heady days in which this Court assumed common-
law powers to create causes of action.’ ” Wilkie v. Robbins,
551 U. S. 537, 568 (2007) (concurring opinion) (quoting
Correctional Services Corp. v. Malesko, 534 U. S. 61, 75
(2001) (Scalia, J., concurring)). I have thus declined to
“extend Bivens even [where] its reasoning logically ap-
plied,” thereby limiting “Bivens and its progeny . . . to the
precise circumstances that they involved.” Ibid. (internal
quotation marks omitted). This would, in most cases,
mean a reversal of the judgment of the Court of Appeals is
in order. However, in order for there to be a controlling
judgment in this suit, I concur in the judgment vacating
and remanding the claims against petitioner Hasty as that
disposition is closest to my preferred approach.
                             II
  As for respondents’ claims under 42 U. S. C. §1985(3),
I join Part V of the Court’s opinion, which holds that
respondents are entitled to qualified immunity. The
Court correctly applies our precedents, which no party has
asked us to reconsider. I write separately, however, to
note my growing concern with our qualified immunity
jurisprudence.
  The Civil Rights Act of 1871, of which §1985(3) and the
more frequently litigated §1983 were originally a part,
established causes of action for plaintiffs to seek money
damages from Government officers who violated federal
law. See §§1, 2, 17 Stat. 13. Although the Act made no
mention of defenses or immunities, “we have read it in
harmony with general principles of tort immunities and
                  Cite as: 582 U. S. ____ (2017)            3

                      Opinion of THOMAS, J.

defenses rather than in derogation of them.” Malley v.
Briggs, 475 U. S. 335, 339 (1986) (internal quotation
marks omitted). We have done so because “[c]ertain im-
munities were so well established in 1871 . . . that ‘we
presume that Congress would have specifically so provided
had it wished to abolish’ them.” Buckley v. Fitzsimmons,
509 U. S. 259, 268 (1993); accord, Briscoe v. LaHue, 460
U. S. 325, 330 (1983). Immunity is thus available under
the statute if it was “historically accorded the relevant
official” in an analogous situation “at common law,” Imbler
v. Pachtman, 424 U. S. 409, 421 (1976), unless the statute
provides some reason to think that Congress did not pre-
serve the defense, see Tower v. Glover, 467 U. S. 914, 920
(1984).
   In some contexts, we have conducted the common-law
inquiry that the statute requires. See Wyatt v. Cole, 504
U. S. 158, 170 (1992) (KENNEDY, J., concurring). For
example, we have concluded that legislators and judges
are absolutely immune from liability under §1983 for their
official acts because that immunity was well established at
common law in 1871. See Tenney v. Brandhove, 341 U. S.
367, 372–376 (1951) (legislators); Pierson v. Ray, 386 U. S.
547, 553–555 (1967) (judges). We have similarly looked to
the common law in holding that a prosecutor is immune
from suits relating to the “judicial phase of the criminal
process,” Imbler, supra, at 430; Burns v. Reed, 500 U. S.
478, 489–492 (1991); but see Kalina v. Fletcher, 522 U. S.
118, 131–134 (1997) (Scalia, J., joined by THOMAS, J.,
concurring) (arguing that the Court in Imbler misunder-
stood 1871 common-law rules), although not from suits
relating to the prosecutor’s advice to police officers, Burns,
supra, at 493.
   In developing immunity doctrine for other executive
officers, we also started off by applying common-law rules.
In Pierson, we held that police officers are not absolutely
immune from a §1983 claim arising from an arrest made
4                     ZIGLAR v. ABBASI

                      Opinion of THOMAS, J.

pursuant to an unconstitutional statute because the com-
mon law never granted arresting officers that sort of
immunity. 386 U. S., at 555. Rather, we concluded that
police officers could assert “the defense of good faith and
probable cause” against the claim for an unconstitutional
arrest because that defense was available against the
analogous torts of “false arrest and imprisonment” at
common law. Id., at 557.
    In further elaborating the doctrine of qualified immun-
ity for executive officials, however, we have diverged from
the historical inquiry mandated by the statute. See Wyatt,
supra, at 170 (KENNEDY, J., concurring); accord, Crawford-
El v. Britton, 523 U. S. 574, 611 (1998) (Scalia, J.,
joined by THOMAS, J., dissenting). In the decisions follow-
ing Pierson, we have “completely reformulated qualified
immunity along principles not at all embodied in the
common law.” Anderson v. Creighton, 483 U. S. 635, 645
(1987) (discussing Harlow v. Fitzgerald, 457 U. S. 800
(1982)). Instead of asking whether the common law in
1871 would have accorded immunity to an officer for a tort
analogous to the plaintiff ’s claim under §1983, we instead
grant immunity to any officer whose conduct “does not
violate clearly established statutory or constitutional
rights of which a reasonable person would have known.”
Mullenix v. Luna, 577 U. S. ___, ___–___ (2015) ( per cu-
riam) (slip op., at 4–5) (internal quotation marks omitted);
Taylor v. Barkes, 575 U. S. ___, ___ (2015) (slip op., at 4) (a
Government official is liable under the 1871 Act only if
“ ‘existing precedent . . . placed the statutory or constitu-
tional question beyond debate’ ” (quoting Ashcroft v. al-
Kidd, 563 U. S. 731, 741 (2011))). We apply this “clearly
established” standard “across the board” and without
regard to “the precise nature of the various officials’ duties
or the precise character of the particular rights alleged to
                     Cite as: 582 U. S. ____ (2017)                    5

                         Opinion of THOMAS, J.

have been violated.” Anderson, supra, at 641–643 (internal
quotation marks omitted).* We have not attempted to
locate that standard in the common law as it existed in
1871, however, and some evidence supports the conclusion
that common-law immunity as it existed in 1871 looked
quite different from our current doctrine. See generally
Baude, Is Qualified Immunity Unlawful? 106 Cal. L. Rev.
(forthcoming 2018) (manuscript, at 7–17), online at
https://papers.ssrn.com/abstract=2896508 (as last visited
June 15, 2017).
    Because our analysis is no longer grounded in the
common-law backdrop against which Congress enacted the
1871 Act, we are no longer engaged in “interpret[ing] the
intent of Congress in enacting” the Act. Malley, supra, at
342; see Burns, supra, at 493. Our qualified immunity
precedents instead represent precisely the sort of “free-
wheeling policy choice[s]” that we have previously dis-
claimed the power to make. Rehberg v. Paulk, 566 U. S.
356, 363 (2012) (internal quotation marks omitted); see
also Tower, supra, at 922–923 (“We do not have a license
to establish immunities from” suits brought under the Act
“in the interests of what we judge to be sound public pol-
icy”). We have acknowledged, in fact, that the “clearly
established” standard is designed to “protec[t] the balance
between vindication of constitutional rights and govern-
ment officials’ effective performance of their duties.”
Reichle v. Howards, 566 U. S. 658, 664 (2012) (internal
quotation marks omitted); Harlow, supra, at 807 (explain-
ing that “the recognition of a qualified immunity defense
. . . reflected an attempt to balance competing values”).
——————
  * Although we first formulated the “clearly established” standard in
Bivens cases like Harlow and Anderson, we have imported that stand-
ard directly into our 1871 Act cases. See, e.g., Pearson v. Callahan, 555
U. S. 223, 243–244 (2009) (applying the clearly established standard to
a §1983 claim).
6                    ZIGLAR v. ABBASI

                    Opinion of THOMAS, J.

The Constitution assigns this kind of balancing to Con-
gress, not the Courts.
   In today’s decision, we continue down the path our
precedents have marked. We ask “whether it would have
been clear to a reasonable officer that the alleged conduct
was unlawful in the situation he confronted,” ante, at 29
(internal quotation marks omitted), rather than whether
officers in petitioners’ positions would have been accorded
immunity at common law in 1871 from claims analogous
to respondents’. Even if we ultimately reach a conclusion
consistent with the common-law rules prevailing in 1871,
it is mere fortuity. Until we shift the focus of our inquiry
to whether immunity existed at common law, we will
continue to substitute our own policy preferences for the
mandates of Congress. In an appropriate case, we should
reconsider our qualified immunity jurisprudence.
                 Cite as: 582 U. S. ____ (2017)          1

                    BREYER, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

              Nos. 15–1358, 15–1359 and 15–1363
                         _________________


            JAMES W. ZIGLAR, PETITIONER
15–1358                  v.
             AHMER IQBAL ABBASI, ET AL.

     JOHN D. ASHCROFT, FORMER ATTORNEY
         GENERAL, ET AL., PETITIONERS
15–1359               v.
          AHMER IQBAL ABBASI, ET AL.

          DENNIS HASTY, ET AL., PETITIONERS
15–1363                  v.
             AHMER IQBAL ABBASI, ET AL.
ON WRITS OF CERTIORARI TO THE UNITED STATES COURT OF
           APPEALS FOR THE SECOND CIRCUIT
                        [June 19, 2017]

  JUSTICE BREYER, with whom JUSTICE GINSBURG joins,
dissenting.
  In Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971), this Court held that the Fourth Amend-
ment provides a damages remedy for those whom federal
officials have injured as a result of an unconstitutional
search or seizure. In Davis v. Passman, 442 U. S. 228
(1979), the Court held that the Fifth Amendment provides
a damages remedy to an individual dismissed by her
employer (a Member of Congress) on the basis of her sex in
violation of the equal protection component of that
Amendment’s Due Process Clause. And in Carlson v.
Green, 446 U. S. 14 (1980), the Court held that the Eighth
Amendment provides a damages remedy to a prisoner who
2                      ZIGLAR v. ABBASI

                      BREYER, J., dissenting

died as a result of prison official’s deliberate indifference
to his medical needs, in violation of the Amendment’s
prohibition against cruel and unusual punishment.
    It is by now well established that federal law provides
damages actions at least in similar contexts, where claims
of constitutional violation arise. Congress has ratified
Bivens actions, plaintiffs frequently bring them, courts
accept them, and scholars defend their importance. See J.
Pfander, Constitutional Torts and the War on Terror
(2017) (canvassing the history of Bivens and cataloguing
cases). Moreover, the courts, in order to avoid deterring
federal officials from properly performing their work, have
developed safeguards for defendants, including the re-
quirement that plaintiffs plead “plausible” claims, Ashcroft
v. Iqbal, 556 U. S. 662, 679 (2009), as well as the defense
of “qualified immunity,” which frees federal officials from
both threat of liability and involvement in the lawsuit,
unless the plaintiffs establish that officials have violated
“ ‘clearly established . . . constitutional rights,’ ” id., at 672
(quoting Harlow v. Fitzgerald, 457 U. S. 800, 818 (1982)).
“[This] Court has been reluctant to extend Bivens liability
‘to any new context or new category of defendants.’ ” Iqbal,
supra, at 675 (quoting Correctional Services Corp. v.
Malesko, 534 U. S. 61, 68 (2001)). But the Court has made
clear that it would not narrow Bivens’ existing scope. See
FDIC v. Meyer, 510 U. S. 471, 485 (1994) (guarding
against “the evisceration of the Bivens remedy” so that its
“deterrent effects . . . would [not] be lost”).
    The plaintiffs before us today seek damages for uncon-
stitutional conditions of confinement. They alleged that
federal officials slammed them against walls, shackled
them, exposed them to nonstop lighting, lack of hygiene,
and the like, all based upon invidious discrimination and
without penological justification. See ante, at 4–5. In my
view, these claims are well-pleaded, state violations of
clearly established law, and fall within the scope of
                  Cite as: 582 U. S. ____ (2017)             3

                     BREYER, J., dissenting

longstanding Bivens law. For those reasons, I would
affirm the judgment of the Court of Appeals. I shall dis-
cuss at some length what I believe is the most important
point of disagreement. The Court, in my view, is wrong to
hold that permitting a constitutional tort action here
would “extend” Bivens, applying it in a new context. To
the contrary, I fear that the Court’s holding would signifi-
cantly shrink the existing Bivens contexts, diminishing
the compensatory remedy constitutional tort law now
offers to harmed individuals.
  I shall explain why I believe this suit falls well within
the scope of traditional constitutional tort law and why I
cannot agree with the Court’s arguments to the contrary.
I recognize, and write separately about, the strongest of
the Court’s arguments, namely, the fact that plaintiffs’
claims concern detention that took place soon after a
serious attack on the United States and some of them
concern actions of high-level Government officials. While
these facts may affect the substantive constitutional
questions (e.g., were any of the conditions “legitimate”?) or
the scope of the qualified-immunity defense, they do not
extinguish the Bivens action itself. If I may paraphrase
Justice Harlan, concurring in Bivens: In wartime as well
as in peacetime, “it is important, in a civilized society, that
the judicial branch of the Nation’s government stand
ready to afford a remedy” “for the most flagrant and pat-
ently unjustified,” unconstitutional “abuses of official
power.” 403 U. S., at 410–411 (opinion concurring in
judgment); cf. Boumediene v. Bush, 553 U. S. 723, 798
(2008).
                            I
  The majority opinion well summarizes the particular
claims that the plaintiffs make in this suit. All concern
the conditions of their confinement, which began soon
after the September 11, 2001, attacks and “lasted for days
4                     ZIGLAR v. ABBASI

                     BREYER, J., dissenting

and weeks, then stretching into months.” Ante, at 1. At
some point, the plaintiffs allege, all the defendants knew
that they had nothing to do with the September 11 attacks
but continued to detain them anyway in harsh conditions.
Official Government policy, both before and after the
defendants became aware of the plaintiffs’ innocence, led
to the plaintiffs being held in “tiny cells for over 23 hours a
day” with lights continuously left on, “shackled” when
moved, often “strip searched,” and “denied access to most
forms of communication with the outside world.” Ante, at
4 (internal quotation marks omitted). The defendants
detained the plaintiffs in these conditions on the basis of
their race or religion and without justification.
  Moreover, the prison wardens were aware of, but delib-
erately indifferent to, certain unofficial activities of prison
guards involving a pattern of “physical and verbal abuse,”
such as “slam[ming] detainees into walls; twist[ing] their
arms, wrists, and fingers; [breaking] their bones;” and
subjecting them to verbal taunts. Ibid. (internal quotation
marks omitted).
  The plaintiffs’ complaint alleges that all the defend-
ants—high-level Department of Justice officials and prison
wardens alike—were directly responsible for the official
confinement policy, which, in some or all of the aspects
mentioned, violated the due process and equal protection
components of the Fifth Amendment. The complaint adds
that, insofar as the prison wardens were deliberately
indifferent to the unofficial conduct of the guards, they
violated the Fourth and the Fifth Amendments.
  I would hold that the complaint properly alleges consti-
tutional torts, i.e., Bivens actions for damages.
                           A
  The Court’s holdings in Bivens, Carlson, and Davis rest
upon four basic legal considerations. First, the Bivens
Court referred to longstanding Supreme Court precedent
                  Cite as: 582 U. S. ____ (2017)             5

                     BREYER, J., dissenting

stating or suggesting that the Constitution provides fed-
eral courts with considerable legal authority to use tradi-
tional remedies to right constitutional wrongs. That
precedent begins with Marbury v. Madison, 1 Cranch 137
(1803), which effectively placed upon those who would
deny the existence of an effective legal remedy the burden
of showing why their case was special. Chief Justice John
Marshall wrote for the Court that
    “[t]he very essence of civil liberty [lies] in the right of
    every individual to claim the protection of the laws,
    whenever he receives an injury.” Id., at 163.
The Chief Justice referred to Blackstone’s Commentaries
stating that there
    “ ‘is a general and indisputable rule, that where there
    is a legal right, there is also a legal remedy . . . [and
    that] it is a settled and invariable principle in the
    laws of England, that every right, when withheld,
    must have a remedy, and every injury its proper re-
    dress.’ ” 1 Cranch, at 163.
The Chief Justice then wrote:
      “The government of the United States has been em-
    phatically termed a government of laws, and not of
    men. It will [not] deserve this high appellation, if the
    laws furnish no remedy for the violation of a vested
    legal right.” Ibid.
He concluded for the Court that there must be something
“peculiar” (i.e., special) about a case that warrants “ex-
clu[ding] the injured party from legal redress . . . [and
placing it within] that class of cases which come under the
description of damnum absque injuria—a loss without an
injury.” Id., at 163–164; but cf. id., at 164 (placing “politi-
cal” questions in the latter, special category).
  Much later, in Bell v. Hood, 327 U. S. 678, 684 (1946),
6                       ZIGLAR v. ABBASI

                     BREYER, J., dissenting

the Court wrote that,
    “where federally protected rights have been invaded,
    it has been the rule from the beginning that courts
    will be alert to adjust their remedies so as to grant the
    necessary relief.”
See also Bivens, 403 U. S., at 392 (citing opinions of Jus-
tices Cardozo and Holmes to similar effect).
   The Bivens Court reiterated these principles and con-
firmed that the appropriate remedial “adjust[ment]” in the
case before it was an award of money damages, the “reme-
dial mechanism normally available in the federal courts.”
Id., at 392, 397. Justice Harlan agreed, adding that, since
Congress’ “general” statutory “grant of jurisdiction” au-
thorized courts to grant equitable relief in cases arising
under federal jurisdiction, courts likewise had the author-
ity to award damages—the “traditional remedy at law”—in
order to “vindicate the interests of the individual” protected
by the Bill of Rights. Id., at 405–407 (opinion concur-
ring in judgment).
   Second, our cases have recognized that Congress’ silence
on the subject indicates a willingness to leave this matter
to the courts. In Bivens, the Court noted, as an argument
favoring its conclusion, the absence of an “explicit congres-
sional declaration that persons injured by a federal of-
ficer’s violation of the Fourth Amendment may not recover
money damages from the agents.” Id., at 397. Similarly,
in Davis v. Passman, the Court stressed that there was
“no evidence . . . that Congress meant . . . to foreclose” a
damages remedy. 442 U. S., at 247. In Carlson, the Court
went further, observing that not only was there no sign
“that Congress meant to pre-empt a Bivens remedy,” but
there was also “clear” evidence that Congress intended to
preserve it. 446 U. S., at 19–20.
   Third, our Bivens cases acknowledge that a constitu-
tional tort may not lie when “special factors counse[l]
                  Cite as: 582 U. S. ____ (2017)            7

                     BREYER, J., dissenting

hesitation” and when Congress has provided an adequate
alternative remedy. 446 U. S., at 18–19. The relevant
special factors in those cases included whether the court
was faced “with a question of ‘federal fiscal policy,’ ”
Bivens, supra, at 396, or a risk of “deluging federal courts
with claims,” Davis, supra, at 248 (internal quotation
marks omitted). Carlson acknowledged an additional
factor—that damages suits “might inhibit [federal offi-
cials’] efforts to perform their official duties”—but con-
cluded that “the qualified immunity accorded [federal
officials] under [existing law] provides adequate protec-
tion.” 446 U. S., at 19.
   Fourth, as the Court recognized later in Carlson, a
Bivens remedy was needed to cure what would, without it,
amount to a constitutional anomaly. Long before this
Court incorporated many of the Bill of Rights’ guarantees
against the States, see Amar, The Bill of Rights and the
Fourteenth Amendment, 101 Yale L. J. 1193 (1992), fed-
eral civil rights statutes afforded a damages remedy to
any person whom a state official deprived of a federal
constitutional right, see 42 U. S. C. §1983; Monroe v. Pape,
365 U. S. 167, 171–187 (1961) (describing this history).
But federal statutory law did not provide a damages rem-
edy to a person whom a federal official had deprived of
that same right, even though the Bill of Rights was at the
time of the founding primarily aimed at constraining the
Federal Government. Thus, a person harmed by an un-
constitutional search or seizure might sue a city mayor, a
state legislator, or even a Governor. But that person could
not sue a federal agent, a national legislator, or a Justice
Department official for an identical offense. “[Our] ‘consti-
tutional design,’ ” the Court wrote, “would be stood on its
head if federal officials did not face at least the same
liability as state officials guilty of the same constitutional
transgression.” Carlson, supra, at 22 (quoting Butz v.
Economou, 438 U. S. 478, 504 (1978)).
8                     ZIGLAR v. ABBASI

                     BREYER, J., dissenting

   The Bivens Court also recognized that the Court had
previously inferred damages remedies caused by violations
of certain federal statutes that themselves did not explic-
itly authorize damages remedies. 403 U. S., at 395–396. At
the same time, Bivens, Davis, and Carlson treat the
courts’ power to derive a damages remedy from a constitu-
tional provision not as included within a power to find a
statute-based damages remedy but as flowing from those
statutory cases a fortiori.
   As the majority opinion points out, this Court in more
recent years has indicated that “expanding the Bivens
remedy is now a ‘disfavored’ judicial activity.” Ante, at 11
(quoting Iqbal, 556 U. S., at 675; emphasis added). Thus,
it has held that the remedy is not available in the context
of suits against military officers, see Chappell v. Wallace,
462 U. S. 296, 298–300 (1983); United States v. Stanley,
483 U. S. 669, 683–684 (1987); in the context of suits
against privately operated prisons and their employees,
see Minneci v. Pollard, 565 U. S. 118, 120 (2012); Malesko,
534 U. S., at 70–73; in the context of suits seeking to
vindicate procedural, rather than substantive, constitu-
tional protections, see Schweiker v. Chilicky, 487 U. S.
412, 423 (1988); and in the context of suits seeking to
vindicate two quite different forms of important substan-
tive protection, one involving free speech, see Bush v.
Lucas, 462 U. S. 367, 368 (1983), and the other involving
protection of land rights, see Wilkie v. Robbins, 551 U. S.
537, 551 (2007). Each of these cases involved a context
that differed from that of Bivens, Davis, and Carlson with
respect to the kind of defendant, the basic nature of the
right, or the kind of harm suffered. That is to say, as we
have explicitly stated, these cases were “fundamentally
different from anything recognized in Bivens or subse-
quent cases.” Malesko, supra, at 70 (emphasis added). In
each of them, the plaintiffs were asking the Court to “ ‘au-
thoriz[e] a new kind of federal litigation.’ ” Wilkie, supra,
                 Cite as: 582 U. S. ____ (2017)            9

                    BREYER, J., dissenting

at 550 (emphasis added).
   Thus the Court, as the majority opinion says, repeatedly
wrote that it was not “expanding” the scope of the Bivens
remedy. Ante, at 11. But the Court nowhere suggested
that it would narrow Bivens’ existing scope. In fact, to
diminish any ambiguity about its holdings, the Court set
out a framework for determining whether a claim of con-
stitutional violation calls for a Bivens remedy. See Wilkie,
supra, at 549–550. At Step One, the court must determine
whether the case before it arises in a “new context,” that
is, whether it involves a “new category of defendants,”
Malesko, supra, at 68, or (presumably) a significantly
different kind of constitutional harm, such as a purely
procedural harm, a harm to speech, or a harm caused to
physical property. If the context is new, then the court
proceeds to Step Two and asks “whether any alternative,
existing process for protecting the interest amounts to a
convincing reason for the Judicial Branch to refrain from
providing a new and freestanding remedy in damages.”
Wilkie, 551 U. S., at 550. If there is none, then the court
proceeds to Step Three and asks whether there are “ ‘any
special factors counselling hesitation before authorizing a
new kind of federal litigation.’ ” Ibid.
   Precedent makes this framework applicable here. I
would apply it. And, doing so, I cannot get past Step One.
This suit, it seems to me, arises in a context similar to
those in which this Court has previously permitted Bivens
actions.
                            B
                            1
  The context here is not “new,” Wilkie, supra, at 550, or
“fundamentally different” than our previous Bivens cases,
Malesko, supra, at 70. First, the plaintiffs are civilians,
not members of the military. They are not citizens, but
the Constitution protects noncitizens against serious
10                    ZIGLAR v. ABBASI

                     BREYER, J., dissenting

mistreatment, as it protects citizens. See United States v.
Verdugo-Urquidez, 494 U. S. 259, 271 (1990) (“[A]liens
receive constitutional protections when they have come
within the territory of the United States and developed
substantial connections with this country”). Some or all of
the plaintiffs here may have been illegally present in the
United States. But that fact cannot justify physical mis-
treatment. Nor does anyone claim that that fact deprives
them of a Bivens right available to other persons, citizens
and noncitizens alike.
   Second, the defendants are Government officials. They
are not members of the military or private persons. Two
are prison wardens. Three others are high-ranking De-
partment of Justice officials. Prison wardens have been
defendants in Bivens actions, as have other high-level
Government officials. One of the defendants in Carlson
was the Director of the Bureau of Prisons; the defendant
in Davis was a Member of Congress. We have also held
that the Attorney General of the United States is not
entitled to absolute immunity in a damages suit arising
out of his actions related to national security. See Mitchell
v. Forsyth, 472 U. S. 511, 520 (1985).
   Third, from a Bivens perspective, the injuries that the
plaintiffs claim they suffered are familiar ones. They
focus upon the conditions of confinement. The plaintiffs
say that they were unnecessarily shackled, confined in
small unhygienic cells, subjected to continuous lighting
(presumably preventing sleep), unnecessarily and fre-
quently strip searched, slammed against walls, injured
physically, and subject to verbal abuse. They allege that
they suffered these harms because of their race or religion,
the defendants having either turned a blind eye to what
was happening or themselves introduced policies that they
knew would lead to these harms even though the defend-
ants knew the plaintiffs had no connections to terrorism.
   These claimed harms are similar to, or even worse than,
                  Cite as: 582 U. S. ____ (2017)             11

                      BREYER, J., dissenting

the harms the plaintiffs suffered in Bivens (unreasonable
search and seizure in violation of the Fourth Amendment),
Davis (unlawful discrimination in violation of the Fifth
Amendment), and Carlson (deliberate indifference to
medical need in violation of the Eighth Amend-
ment). Indeed, we have said that, “[i]f a federal prisoner
in a [Bureau of Prisons] facility alleges a constitutional
deprivation, he may bring a Bivens claim against the
offending individual officer, subject to the defense of quali-
fied immunity.” Malesko, 534 U. S., at 72; see also Farmer
v. Brennan, 511 U. S. 825, 832 (1994) (Bivens case about
prisoner abuse). The claims in this suit would seem to fill
the Bivens’ bill. See Sell v. United States, 539 U. S. 166,
193 (2003) (Scalia, J., dissenting) (“[A] [Bivens] action . . .
is available to federal pretrial detainees challenging the
conditions of their confinement”).
   It is true that the plaintiffs bring their “deliberate indif-
ference” claim against Warden Hasty under the Fifth
Amendment’s Due Process Clause, not the Eighth
Amendment’s Cruel and Unusual Punishment Clause, as
in Carlson. But that is because the latter applies to con-
victed criminals while the former applies to pretrial and
immigration detainees. Where the harm is the same,
where this Court has held that both the Fifth and Eighth
Amendments give rise to Bivens’ remedies, and where the
only difference in constitutional scope consists of a circum-
stance (the absence of a conviction) that makes the viola-
tion here worse, it cannot be maintained that the differ-
ence between the use of the two Amendments is
“fundamental.” See City of Revere v. Massachusetts Gen.
Hospital, 463 U. S. 239, 244 (1983) (“due process rights” of
an unconvicted person “are at least as great as the Eighth
Amendment protections available to a convicted pris-
oner”); Kingsley v. Hendrickson, 576 U. S. ___, ___–___ (2015)
(slip op., at 10–11) (“pretrial detainees (unlike convicted
prisoners) cannot be punished at all”); Zadvydas v. Davis,
12                    ZIGLAR v. ABBASI

                     BREYER, J., dissenting

533 U. S. 678, 721 (2001) (KENNEDY, J., dissenting) (de-
tention “incident to removal . . . cannot be justified as
punishment nor can the confinement or its conditions be
designed in order to punish”). See also Bistrian v. Levi,
696 F. 3d 352, 372 (CA3 2012) (permitting Bivens action
brought by detainee in administrative segregation);
Thomas v. Ashcroft, 470 F. 3d 491, 493, 496–497 (CA2
2006) (detainee alleging failure to provide adequate medi-
cal care); Magluta v. Samples, 375 F. 3d 1269, 1271, 1275–
1276 (CA11 2004) (detainee in solitary confinement); Papa
v. United States, 281 F. 3d 1004, 1010–1011 (CA9 2002)
(due process claims arising from death of immigration
detainee); Loe v. Armistead, 582 F. 2d 1291, 1293–1296
(CA4 1978) (detainee’s claim of deliberate indifference to
medical need). If an arrestee can bring a claim of exces-
sive force (Bivens itself), and a convicted prisoner can
bring a claim for denying medical care (Carlson), someone
who has neither been charged nor convicted with a crime
should also be able to challenge abuse that causes him to
need medical care.
   Nor has Congress suggested that it wants to withdraw a
damages remedy in circumstances like these. By its ex-
press terms, the Prison Litigation Reform Act of 1995
(PLRA) does not apply to immigration detainees. See 42
U. S. C. §1997e(h) (“[T]he term ‘prisoner’ means any per-
son incarcerated or detained in any facility who is accused
of, convicted of, sentenced for, or adjudicated delinquent
for, violations of criminal law . . . ”); see also Agyeman v.
INS, 296 F. 3d 871, 886 (CA9 2002) (“[W]e hold that an
alien detained by the INS pending deportation is not a
‘prisoner’ within the meaning of the PLRA”); LaFontant v.
INS, 135 F. 3d 158, 165 (CADC 1998) (same); Ojo v. INS,
106 F. 3d 680, 683 (CA5 1997) (same). And, in fact, there
is strong evidence that Congress assumed that Bivens
remedies would be available to prisoners when it enacted
the PLRA—e.g., Congress continued to permit prisoners to
                 Cite as: 582 U. S. ____ (2017)          13

                    BREYER, J., dissenting

recover for physical injuries, the typical kinds of Bivens
injuries. See 28 U. S. C. §1346(b)(2); Pfander, Constitu-
tional Torts, at 105–106.
   If there were any lingering doubt that the claim against
Warden Hasty arises in a familiar Bivens context, the
Court has made clear that conditions-of-confinement
claims and medical-care claims are subject to the same
substantive standard. See Hudson v. McMillian, 503 U. S.
1, 8 (1992) (“[Wilson v. Seiter, 501 U. S. 294, 303 (1991)]
extended the deliberate indifference standard applied to
Eighth Amendment claims involving medical care to
claims about conditions of confinement”). Indeed, the
Court made this very point in a Bivens case alleging that
prison wardens were deliberately indifferent to an in-
mate’s safety. See Farmer, supra, at 830, 834.
   I recognize that the Court finds a significant difference
in the fact that the confinement here arose soon after a
national-security emergency, namely, the September 11
attacks. The short answer to this argument, in respect to
at least some of the claimed harms, is that some plaintiffs
continued to suffer those harms up to eight months after
the September 11 attacks took place and after the defend-
ants knew the plaintiffs had no connection to terrorism.
See App. to Pet. for Cert. in No. 15–1359, p. 280a. But
because I believe the Court’s argument here is its strong-
est, I will consider it at greater length below. See Part
III–C, infra.
   Because the context here is not new, I would allow the
plaintiffs’ constitutional claims to proceed. The plaintiffs
have adequately alleged that the defendants were person-
ally involved in imposing the conditions of confinement
and did so with knowledge that the plaintiffs bore no ties
to terrorism, thus satisfying Iqbal’s pleading standard.
See 556 U. S., at 679 (claims must be “plausible”); see also
id., at 699–700 (BREYER, J., dissenting). And because it is
clearly established that it is unconstitutional to subject
14                    ZIGLAR v. ABBASI

                     BREYER, J., dissenting

detainees to punitive conditions of confinement and to
target them based solely on their race, religion, or national
origin, the defendants are not entitled to qualified immun-
ity on the constitutional claims. See Bell v. Wolfish, 441
U. S. 520, 535–539, and n. 20 (1979); Davis, 442 U. S., at
236 (“It is equally clear . . . that the Fifth Amendment
confers on petitioner a constitutional right to be free from
illegal discrimination”). (Similarly, I would affirm the
judgment of the Court of Appeals with respect to the
plaintiffs’ statutory claim, namely, that the defendants
conspired to deprive the plaintiffs of equal protection of
the laws in violation of 42 U. S. C. §1985(3). See Turkmen
v. Hasty, 789 F. 3d 218, 262–264 (CA2 2015). I agree with
the Court of Appeals that the defendants are not entitled
to qualified immunity on this claim. See ibid.)
                             2
   Even were I wrong and were the context here “funda-
mentally different,” Malesko, 534 U. S., at 70, the plain-
tiffs’ claims would nonetheless survive Step Two and Step
Three of the Court’s framework for determining whether
Bivens applies, see supra, at 9. Step Two consists of ask-
ing whether “any alternative, existing process for protect-
ing the interest amounts to a convincing reason for the
Judicial Branch to refrain from providing a new and free-
standing remedy in damages.” Wilkie, 551 U. S., at 550. I
can find no such “alternative, existing process” here.
   The Court does not claim that the PLRA provides plain-
tiffs with a remedy. Ante, at 25–26. Rather, it says that
the plaintiffs may have “had available to them” relief in
the form of a prospective injunction or an application for a
writ of habeas corpus. Ante, at 22. Neither a prospective
injun

[...TRUNCATED 20279 of 140279 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Zurcher v. Stanford Daily.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Zurcher v. Stanford Daily"
type: case
citation: "436 U.S. 547 (1978)"
parallel_cite: "98 S. Ct. 1970; 56 L. Ed. 2d 525"
neutral_cite: 1978 U.S. LEXIS 98
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1978
date_decided: 1978-10-02
docket: 76-1484
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1978-05-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Zurcher v. Stanford Daily
  varies_by_point: false
  scope_note: "Fourth Amendment holding remains good law. Congress responded with the Privacy Protection Act of 1980 (42 U.S.C. § 2000aa), which statutorily restricts searches of press/documentary work product — a statutory overlay, not a constitutional limitation of Zurcher."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109876/zurcher-v-stanford-daily/"
  cluster_id: 109876
  opinion_id: 109876
  identity_checked: true
homes:
  - page: "[[Scope Manner and Related Issues]]"
    role: "Progeny (third-party premises)"
related: ["[[Stanford v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant", "search-warrant", "third-party-premises", "first-amendment", "press"]
holding: "A warrant may authorize the search of premises held by a third party not suspected of crime — including a newspaper — whenever there is probable cause to believe evidence is located there; the First Amendment requires only that the warrant requirements be applied with scrupulous exactitude, not a subpoena-first rule."
lake:
  record_id: Zurcher v. Stanford Daily
  status: verified
  projected_at: 2026-07-06
---

# Zurcher v. Stanford Daily

*436 U.S. 547 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a clash between police and demonstrators at Stanford University Hospital, police obtained a warrant to search the offices of the *Stanford Daily*, a student newspaper, for photographs that might identify assailants. The newspaper itself was not suspected of any crime. The *Daily* sued, claiming the search of a non-suspect third party — and of a newspaper in particular — violated the Fourth and First Amendments and that police should have been required to proceed by subpoena.

## Issue
Whether the Fourth Amendment bars a warranted search of premises occupied by a third party not suspected of crime, and whether the First Amendment requires that searches of a newspaper proceed only by subpoena rather than search warrant.

## Rule
A warrant may issue to search a non-suspect third party's premises on probable cause that evidence is there. "The critical element in a reasonable search is not that the owner of the property is suspected of crime but that there is reasonable cause to believe that the specific 'things' to be searched for and seized are located on the property to which entry is sought." — 436 U.S. at 556. ^pin-556

The First Amendment does not impose a subpoena-first rule, but heightens the care required of the magistrate. "Where the materials sought to be seized may be protected by the First Amendment, the requirements of the Fourth Amendment must be applied with 'scrupulous exactitude.'" — *Id.* at 564 (quoting *Stanford v. Texas*). ^pin-564

## Application
Properly issued warrants protect third parties by requiring probable cause that the items sought are presently on the described premises, so no special rule was needed to shield non-suspect owners. As to the newspaper, the First Amendment did not justify the District Court's near-per-se bar on warrants; the answer was for magistrates to apply the warrant requirements with scrupulous exactitude where protected materials are at stake, leaving "as little as possible to the discretion or whim of the officer in the field." The warrant to search the *Daily* was therefore constitutionally permissible.

## Conclusion
The warranted search of the newspaper's offices did not violate the Fourth or First Amendment; the judgment for the *Daily* was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Statutory overlay (field-relevant):** Congress responded to *Zurcher* with the Privacy Protection Act of 1980 (42 U.S.C. § 2000aa), which generally bars searches for a journalist's or author's documentary "work product" and instead requires a subpoena, subject to exceptions (e.g., the possessor is a suspect, or imminent risk to life). The PPA constrains the field practice for press searches by statute; it does not disturb *Zurcher*'s Fourth Amendment holding, which remains good law.

## Appears on
- [[Scope Manner and Related Issues]] — *Progeny (third-party premises)*

## Sources
- *Zurcher v. Stanford Daily*, 436 U.S. 547 (1978) — https://www.courtlistener.com/opinion/109876/zurcher-v-stanford-daily/ — pinpoints: 556, 564.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c16a6b3d7b61201a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Zurcher v. Stanford Daily"}, "payload": {"all": [{"cite": "436 U.S. 547", "page": "547", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "436"}, {"cite": "98 S. Ct. 1970", "page": "1970", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "98"}, {"cite": "56 L. Ed. 2d 525", "page": "525", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}, {"cite": "1978 U.S. LEXIS 98", "page": "98", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1978"}], "display": "436 U.S. 547", "official": {"cite": "436 U.S. 547", "page": "547", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "436"}, "official_selection_present": true, "record_id": "Zurcher v. Stanford Daily"}}
{"assertion_id": "14f4ed8dff480038", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-564", "record_id": "Zurcher v. Stanford Daily"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-564", "pinpoint_status": "slip-only", "quote": "Where the materials sought to be seized may be protected by the First Amendment, the requirements of the Fourth Amendment must be applied with 'scrupulous exactitude.'", "quote_fidelity": "mismatch", "record_id": "Zurcher v. Stanford Daily", "star_marker": null}}
{"assertion_id": "ac9dc0c540da22d4", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-556", "record_id": "Zurcher v. Stanford Daily"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-556", "pinpoint_status": "slip-only", "quote": "--- # Zurcher v. Stanford Daily *436 U.S. 547 (1978)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After a clash between police and demonstrators at Stanford University Hospital, police obtained a warrant to search the offices of the *Stanford Daily*, a student newspaper, for photographs that might identify assailants. The newspaper itself was not suspected of any crime. The *Daily* sued, claiming the search of a non-suspect third party — and of a newspaper in particular — violated the Fourth and First Amendments and that police should have been required to proceed by subpoena. ## Issue Whether the Fourth Amendment bars a warranted search of premises occupied by a third party not suspected of crime, and whether the First Amendment requires that searches of a newspaper proceed only by subpoena rather than search warrant. ## Rule A warrant may issue to search a non-suspect third party's premises on probable cause that evidence is there.", "quote_fidelity": "mismatch", "record_id": "Zurcher v. Stanford Daily", "star_marker": null}}
{"assertion_id": "c56c88b8cf0d744e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Zurcher v. Stanford Daily"}, "payload": {"as_of_content": "1978-05-31", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Zurcher v. Stanford Daily", "scope_note": "Fourth Amendment holding remains good law. Congress responded with the Privacy Protection Act of 1980 (42 U.S.C. § 2000aa), which statutorily restricts searches of press/documentary work product — a statutory overlay, not a constitutional limitation of Zurcher.", "varies_by_point": false}}
```

### lake record — Zurcher v. Stanford Daily

```json
{
  "schema_version": "s2.v1",
  "record_id": "Zurcher v. Stanford Daily",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Zurcher v. Stanford Daily",
    "case_name_short": "Zurcher",
    "case_name_full": "ZURCHER, CHIEF OF POLICE OF PALO ALTO, Et Al. v. STANFORD DAILY Et Al.",
    "input_case_name": "Zurcher v. Stanford Daily",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1978-10-02",
    "year": 1978,
    "docket": "76-1484",
    "cluster_id": 109876,
    "lead_opinion_id": 109876,
    "sibling_ids": [
      109876,
      9427224,
      9427225,
      9427226,
      9427227
    ],
    "absolute_url": "/opinion/109876/zurcher-v-stanford-daily/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "436 U.S. 547",
      "volume": "436",
      "reporter": "U.S.",
      "page": "547",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "98 S. Ct. 1970",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1970",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 525",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1978 U.S. LEXIS 98",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "98",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "436 U.S. 547",
        "volume": "436",
        "reporter": "U.S.",
        "page": "547",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "98 S. Ct. 1970",
        "volume": "98",
        "reporter": "S. Ct.",
        "page": "1970",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 L. Ed. 2d 525",
        "volume": "56",
        "reporter": "L. Ed. 2d",
        "page": "525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1978 U.S. LEXIS 98",
        "volume": "1978",
        "reporter": "U.S. LEXIS",
        "page": "98",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "436 U.S. 547",
    "official_selection": {
      "court_class": "scotus",
      "selected": "436 U.S. 547",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-556",
      "page": null,
      "quote": "--- # Zurcher v. Stanford Daily *436 U.S. 547 (1978)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After a clash between police and demonstrators at Stanford University Hospital, police obtained a warrant to search the offices of the *Stanford Daily*, a student newspaper, for photographs that might identify assailants. The newspaper itself was not suspected of any crime. The *Daily* sued, claiming the search of a non-suspect third party \u2014 and of a newspaper in particular \u2014 violated the Fourth and First Amendments and that police should have been required to proceed by subpoena. ## Issue Whether the Fourth Amendment bars a warranted search of premises occupied by a third party not suspected of crime, and whether the First Amendment requires that searches of a newspaper proceed only by subpoena rather than search warrant. ## Rule A warrant may issue to search a non-suspect third party's premises on probable cause that evidence is there.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-564",
      "page": null,
      "quote": "Where the materials sought to be seized may be protected by the First Amendment, the requirements of the Fourth Amendment must be applied with 'scrupulous exactitude.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1978-05-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Zurcher v. Stanford Daily",
    "varies_by_point": false,
    "scope_note": "Fourth Amendment holding remains good law. Congress responded with the Privacy Protection Act of 1980 (42 U.S.C. \u00a7 2000aa), which statutorily restricts searches of press/documentary work product \u2014 a statutory overlay, not a constitutional limitation of Zurcher.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Ghim",
          "cluster_id": 4312059,
          "cite": [
            "360 Or. 425",
            "381 P.3d 789",
            "2016 Ore. LEXIS 680"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rose",
          "cluster_id": 2981732,
          "cite": [
            "714 F.3d 362",
            "2013 WL 1664697",
            "2013 U.S. App. LEXIS 7764"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Al-Kidd v. Ashcroft",
          "cluster_id": 1204118,
          "cite": [
            "580 F.3d 949",
            "2009 U.S. App. LEXIS 20000",
            "2009 WL 2836448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Eric Curtin",
          "cluster_id": 798060,
          "cite": [
            "489 F.3d 935",
            "73 Fed. R. Serv. 646",
            "2007 U.S. App. LEXIS 12110",
            "2007 WL 1500295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 145121,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hensley v. Eckerhart",
          "cluster_id": 110929,
          "cite": [
            "76 L. Ed. 2d 40",
            "103 S. Ct. 1933",
            "461 U.S. 424",
            "1983 U.S. LEXIS 160",
            "51 U.S.L.W. 4552",
            "32 Empl. Prac. Dec. (CCH) 33,618",
            "31 Fair Empl. Prac. Cas. (BNA) 1169"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
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
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
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
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blum v. Stenson",
          "cluster_id": 111123,
          "cite": [
            "79 L. Ed. 2d 891",
            "104 S. Ct. 1541",
            "465 U.S. 886",
            "1984 U.S. LEXIS 47",
            "52 U.S.L.W. 4377",
            "33 Empl. Prac. Dec. (CCH) 34,226",
            "34 Fair Empl. Prac. Cas. (BNA) 417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunaway v. New York",
          "cluster_id": 110096,
          "cite": [
            "60 L. Ed. 2d 824",
            "99 S. Ct. 2248",
            "442 U.S. 200",
            "1979 U.S. LEXIS 126"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Summers",
          "cluster_id": 110534,
          "cite": [
            "69 L. Ed. 2d 340",
            "101 S. Ct. 2587",
            "452 U.S. 692",
            "1981 U.S. LEXIS 118",
            "49 U.S.L.W. 4776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornburgh v. Abbott",
          "cluster_id": 112258,
          "cite": [
            "104 L. Ed. 2d 459",
            "109 S. Ct. 1874",
            "490 U.S. 401",
            "1989 U.S. LEXIS 2437",
            "57 U.S.L.W. 4517"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blanchard v. Bergeron",
          "cluster_id": 112196,
          "cite": [
            "103 L. Ed. 2d 67",
            "109 S. Ct. 939",
            "489 U.S. 87",
            "1989 U.S. LEXIS 595",
            "57 U.S.L.W. 4191",
            "49 Fair Empl. Prac. Cas. (BNA) 1",
            "49 Empl. Prac. Dec. (CCH) 38,722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
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
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
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
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Delaware Valley Citizens' Council for Clean Air",
          "cluster_id": 111955,
          "cite": [
            "97 L. Ed. 2d 585",
            "107 S. Ct. 3078",
            "483 U.S. 711",
            "1987 U.S. LEXIS 2979",
            "17 Envtl. L. Rep. (Envtl. Law Inst.) 20929",
            "55 U.S.L.W. 5113",
            "26 ERC (BNA) 1091",
            "45 Fair Empl. Prac. Cas. (BNA) 1750"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
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
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dalia v. United States",
          "cluster_id": 110061,
          "cite": [
            "60 L. Ed. 2d 177",
            "99 S. Ct. 1682",
            "441 U.S. 238",
            "1979 U.S. LEXIS 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1728885,
          "cite": [
            "868 S.W.2d 561",
            "1993 Tenn. LEXIS 410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. City of Stockton",
          "cluster_id": 1310475,
          "cite": [
            "588 F.3d 1218",
            "2009 U.S. App. LEXIS 26799",
            "2009 WL 4641736"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marvin Jones, on His Own Behalf and on Behalf of Those Similarly Situated v. Fred R. Diamond",
          "cluster_id": 385707,
          "cite": [
            "636 F.2d 1364",
            "1981 U.S. App. LEXIS 20595"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aaron Tobey v. Terri Jones",
          "cluster_id": 816055,
          "cite": [
            "706 F.3d 379"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Clifford",
          "cluster_id": 111057,
          "cite": [
            "78 L. Ed. 2d 477",
            "104 S. Ct. 641",
            "464 U.S. 287",
            "1984 U.S. LEXIS 14",
            "52 U.S.L.W. 4056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Eugene Allen",
          "cluster_id": 768626,
          "cite": [
            "211 F.3d 970",
            "2000 U.S. App. LEXIS 8795",
            "2000 WL 547599"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Serrano v. Unruh",
          "cluster_id": 1165326,
          "cite": [
            "652 P.2d 985",
            "32 Cal. 3d 621",
            "186 Cal. Rptr. 754",
            "1982 Cal. LEXIS 238"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Caraher",
          "cluster_id": 1188275,
          "cite": [
            "653 P.2d 942",
            "293 Or. 741",
            "1982 Ore. LEXIS 1190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "General William C. Westmoreland, Ambassador Richard Helms v. Cbs, Inc.",
          "cluster_id": 457539,
          "cite": [
            "770 F.2d 1168",
            "248 U.S. App. D.C. 255",
            "2 Fed. R. Serv. 3d 1451",
            "1985 U.S. App. LEXIS 21281"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Nucorp Energy, Inc., an Ohio Corporation, and Its Affiliates, Debtors. Luce, Forward, Hamilton & Scripps",
          "cluster_id": 453423,
          "cite": [
            "764 F.2d 655",
            "12 Collier Bankr. Cas. 2d 1463",
            "1985 U.S. App. LEXIS 20043",
            "13 Bankr. Ct. Dec. (CRR) 435",
            "54 U.S.L.W. 2013"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Parcel of Rumson, NJ, Land",
          "cluster_id": 112823,
          "cite": [
            "122 L. Ed. 2d 469",
            "113 S. Ct. 1126",
            "507 U.S. 111",
            "1993 U.S. LEXIS 1782",
            "61 U.S.L.W. 4189",
            "7 Fla. L. Weekly Fed. S 24",
            "93 Cal. Daily Op. Serv. 1249"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hector Martin Ramos",
          "cluster_id": 554939,
          "cite": [
            "923 F.2d 1346",
            "91 Daily Journal DAR 800",
            "91 Cal. Daily Op. Serv. 513",
            "1991 U.S. App. LEXIS 547",
            "1991 WL 2877"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Zurcher v. Stanford Daily:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109876 OR 9427224 OR 9427225 OR 9427226 OR 9427227) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04NzUxNDU2MDAwMDAmcz03NDY3NzMmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109876+OR+9427224+OR+9427225+OR+9427226+OR+9427227%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109876 OR 9427224 OR 9427225 OR 9427226 OR 9427227)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkmcz0zNjAxODgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109876+OR+9427224+OR+9427225+OR+9427226+OR+9427227%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109876 OR 9427224 OR 9427225 OR 9427226 OR 9427227)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109876 OR 9427224 OR 9427225 OR 9427226 OR 9427227)",
    "indexed_citing_opinions": 586,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109876,
        "count": 521,
        "count_source": "search"
      },
      {
        "opinion_id": 9427224,
        "count": 79,
        "count_source": "search"
      },
      {
        "opinion_id": 9427225,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427226,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427227,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 910,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/zurcher-v-stanford-daily.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxMzc4NzImcz05Mzc1MDIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28109876+OR+9427224+OR+9427225+OR+9427226+OR+9427227%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109876,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 101764,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 102601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 105972,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108853,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 108966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 109023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 109079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 109130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 299535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 336136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 343344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 1396227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 1964303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109876,
        "cited_id": 2344500,
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
    "date_created": "2026-07-06T04:59:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:59:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:59:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T05:02:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:59:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Zurcher v. Stanford Daily

```
<div>
<center><b><span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U.S. 547</a></span> (1978)</b></center>
<center><h1>ZURCHER, CHIEF OF POLICE OF PALO ALTO, ET AL.<br>
v.<br>
STANFORD DAILY ET AL.</h1></center>
<center>No. 76-1484.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued January 17, 1978.</center>
<center>Decided May 31, 1978.<sup>[*]</sup></center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*548</span> <i>Robert K. Booth, Jr.,</i> argued the cause for petitioners in No. 76-1484. With him on the briefs were <i>Marilyn Norek Taketa, Melville A. Toff,</i> and <i>Stephen L. Newton.</i></p>
<p><i>W. Eric Collins,</i> Deputy Attorney General of California, argued the cause for petitioners in No. 76-1600. With him on the briefs were <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>Edward P. O'Brien,</i> Assistant Attorney General, <i>Patrick G. Golden</i> and <i>Eugene W. Kaster,</i> Deputy Attorneys General, <i>Selby Brown, Jr.,</i> and <i>Richard K. Abdalah.</i></p>
<p><i>Jerome B. Falk, Jr.,</i> argued the cause for respondents in both cases. With him on the briefs was <i>Anthony G. Amsterdam.</i><sup>[]</sup></p>
<p><span class="star-pagination">*549</span> MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The terms of the Fourth Amendment, applicable to the States by virtue of the Fourteenth Amendment, are familiar:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>As heretofore understood, the Amendment has not been a barrier to warrants to search property on which there is <span class="star-pagination">*550</span> probable cause to believe that fruits, instrumentalities, or evidence of crime is located, whether or not the owner or possessor of the premises to be searched is himself reasonably suspected of complicity in the crime being investigated. We are now asked to reconstrue the Fourth Amendment and to hold for the first time that when the place to be searched is occupied by a person not then a suspect, a warrant to search for criminal objects and evidence reasonably believed to be located there should not issue except in the most unusual circumstances, and that except in such circumstances, a subpoena <i>duces tecum</i> must be relied upon to recover the objects or evidence sought.</p>
<p></p>
<h2>I</h2>
<p>Late in the day on Friday, April 9, 1971, officers of the Palo Alto Police Department and of the Santa Clara County Sheriff's Department responded to a call from the director of the Stanford University Hospital requesting the removal of a large group of demonstrators who had seized the hospital's administrative offices and occupied them since the previous afternoon. After several futile efforts to persuade the demonstrators to leave peacefully, more drastic measures were employed. The demonstrators had barricaded the doors at both ends of a hall adjacent to the administrative offices. The police chose to force their way in at the west end of the corridor. As they did so, a group of demonstrators emerged through the doors at the east end and, armed with sticks and clubs, attacked the group of nine police officers stationed there. One officer was knocked to the floor and struck repeatedly on the head; another suffered a broken shoulder. All nine were injured.<sup>[1]</sup> There were no police photographers at the east doors, and most bystanders and reporters were on the west side. The officers themselves were able to identify only two of their <span class="star-pagination">*551</span> assailants, but one of them did see at least one person photographing the assault at the east doors.</p>
<p>On Sunday, April 11, a special edition of the Stanford Daily (Daily), a student newspaper published at Stanford University, carried articles and photographs devoted to the hospital protest and the violent clash between demonstrators and police. The photographs carried the byline of a Daily staff member and indicated that he had been at the east end of the hospital hallway where he could have photographed the assault on the nine officers. The next day, the Santa Clara County District Attorney's Office secured a warrant from the Municipal Court for an immediate search of the Daily's offices for negatives, film, and pictures showing the events and occurrences at the hospital on the evening of April 9. The warrant issued on a finding of "just, probable and reasonable cause for believing that: Negatives and photographs and films, evidence material and relevant to the identity of the perpetrators of felonies, to wit, Battery on a Peace Officer, and Assault with Deadly Weapon, will be located [on the premises of the Daily]." App. 31-32. The warrant affidavit contained no allegation or indication that members of the Daily staff were in any way involved in unlawful acts at the hospital.</p>
<p>The search pursuant to the warrant was conducted later that day by four police officers and took place in the presence of some members of the Daily staff. The Daily's photographic laboratories, filing cabinets, desks, and wastepaper baskets were searched. Locked drawers and rooms were not opened. The officers apparently had opportunity to read notes and correspondence during the search; but, contrary to claims of the staff, the officers denied that they had exceeded the limits of the warrant.<sup>[2]</sup> They had not been advised by the staff that the areas they were searching contained confidential materials. The search revealed only the photographs that had already <span class="star-pagination">*552</span> been published on April 11, and no materials were removed from the Daily's office.</p>
<p>A month later the Daily and various members of its staff, respondents here, brought a civil action in the United States District Court for the Northern District of California seeking declaratory and injunctive relief under <span class="citation no-link">42 U. S. C. § 1983</span> against the police officers who conducted the search, the chief of police, the district attorney and one of his deputies, and the judge who had issued the warrant. The complaint alleged that the search of the Daily's office had deprived respondents under color of state law of rights secured to them by the First, Fourth, and Fourteenth Amendments of the United States Constitution.</p>
<p>The District Court denied the request for an injunction but, on respondents' motion for summary judgment, granted declaratory relief. <span class="citation" data-id="2344500"><a href="/opinion/2344500/stanford-daily-v-zurcher/" aria-description="Citation for case: Stanford Daily v. Zurcher">353 F. Supp. 124</a></span> (1972). The court did not question the existence of probable cause to believe that a crime had been committed and to believe that relevant evidence would be found on the Daily's premises. It held, however, that the Fourth and Fourteenth Amendments forbade the issuance of a warrant to search for materials in possession of one not suspected of crime unless there is probable cause to believe, based on facts presented in a sworn affidavit, that a subpoena <i>duces tecum</i> would be impracticable. Moreover, the failure to honor a subpoena would not alone justify a warrant; it must also appear that the possessor of the objects sought would disregard a court order not to remove or destroy them. The District Court further held that where the innocent object of the search is a newspaper, First Amendment interests are also involved and that such a search is constitutionally permissible "only in the rare circumstance where there is a <i>clear showing</i> that (1) important materials will be destroyed or removed from the jurisdiction; <i>and</i> (2) a restraining order would be futile." <span class="citation" data-id="2344500"><a href="/opinion/2344500/stanford-daily-v-zurcher/#135" aria-description="Citation for case: Stanford Daily v. Zurcher"><i>Id.,</i> at 135</a></span>. Since these preconditions to a valid warrant had not been satisfied here, <span class="star-pagination">*553</span> the search of the Daily's offices was declared to have been illegal. The Court of Appeals affirmed <i>per curiam,</i> adopting the opinion of the District Court. <span class="citation" data-id="343344"><a href="/opinion/343344/the-stanford-daily-v-james-zurcher-individually-and-as-chief-of-police-of/" aria-description="Citation for case: The Stanford Daily v. James Zurcher, Individually and as...">550 F. 2d 464</a></span> (CA9 1977).<sup>[3]</sup> We issued the writs of certiorari requested by petitioners. <span class="citation multiple-matches"><a href="/c/U.%20S./434/816/">434 U. S. 816</a></span> (1977).<sup>[4]</sup> We reverse.</p>
<p></p>
<h2>II</h2>
<p>The issue here is how the Fourth Amendment is to be construed and applied to the "third party" search, the recurring situation where state authorities have probable cause to believe that fruits, instrumentalities, or other evidence of crime is located on identified property but do not then have probable cause to believe that the owner or possessor of the property is himself implicated in the crime that has occurred or is occurring. Because under the District Court's rule impracticability can be shown only by furnishing facts demonstrating that the third party will not only disobey the subpoena but also ignore a restraining order not to move or destroy the property, it is apparent that only in unusual situations could the State satisfy such a severe burden and that for all practical purposes the effect of the rule is that fruits, instrumentalities, and evidence of crime may be recovered from third parties only by subpoena, not by search warrant. At least, we assume that the District Court did not intend its rule to be toothless and anticipated that only subpoenas would be available in many cases where without the rule a search warrant would issue.</p>
<p><span class="star-pagination">*554</span> It is an understatement to say that there is no direct authority in this or any other federal court for the District Court's sweeping revision of the Fourth Amendment.<sup>[5]</sup> Under existing law, valid warrants may be issued to search <i>any</i> property, whether or not occupied by a third party, at which there is probable cause to believe that fruits, instrumentalities, or evidence of a crime will be found. Nothing on the face of the Amendment suggests that a third-party search warrant should not normally issue. The Warrant Clause speaks of search warrants issued on "probable cause" and "particularly describing the place to be searched, and the persons or things to be seized." In situations where the State does not seek to seize "persons" but only those "things" which there is probable cause to believe are located on the place to be searched, there is no apparent basis in the language of the Amendment for also imposing the requirements for a valid arrestprobable cause to believe that the third party is implicated in the crime.</p>
<p>As the Fourth Amendment has been construed and applied by this Court, "when the State's reason to believe incriminating evidence will be found becomes sufficiently great, the invasion of privacy becomes justified and a warrant to search and seize will issue." <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#400" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 400</a></span> (1976). In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535</a></span> (1967), we indicated that in applying the "probable cause" standard "by which a particular decision to search is <span class="star-pagination">*555</span> tested against the constitutional mandate of reasonableness," it is necessary "to focus upon the governmental interest which allegedly justifies official intrusion" and that in criminal investigations a warrant to search for recoverable items is reasonable "only when there is `probable cause' to believe that they will be uncovered in a particular dwelling." Search warrants are not directed at persons; they authorize the search of "place[s]" and the seizure of "things," and as a constitutional matter they need not even name the person from whom the things will be seized. <i>United States</i> v. <i>Kahn,</i> <span class="citation" data-id="9425604"><a href="/opinion/108966/united-states-v-kahn/" aria-description="Citation for case: United States v. Kahn">415 U. S. 143</a></span>, 155 n. 15 (1974).</p>
<p>Because the State's interest in enforcing the criminal law and recovering evidence is the same whether the third party is culpable or not, the premise of the District Court's holding appears to be that state entitlement to a search warrant depends on the culpability of the owner or possessor of the place to be searched and on the State's right to arrest him. The cases are to the contrary. Prior to <i>Camara</i> v. <i>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra</a></span></i><i>,</i> and <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), the central purpose of the Fourth Amendment was seen to be the protection of the individual against official searches for evidence to convict him of a crime. Entries upon property for civil purposes, where the occupant was suspected of no criminal conduct whatsoever, involved a more peripheral concern and the less intense "right to be secure from intrusion into personal privacy." <i>Frank</i> v. <i>Maryland,</i> <span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#365" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 365</a></span> (1959); <i>Camara</i> v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Municipal Court, supra,</i> at 530</a></span>. Such searches could proceed without warrant, as long as the State's interest was sufficiently substantial. Under this view, the Fourth Amendment was <i>more</i> protective where the place to be searched was occupied by one suspected of crime and the search was for evidence to use against him. <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> and <i>See,</i> disagreeing with <i><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Frank</a></span></i> to this extent, held that a warrant <i>is</i> required where entry is sought for <i>civil</i> purposes, as well as when criminal law enforcement is involved. Neither <span class="star-pagination">*556</span> case, however, suggested that to secure a search warrant the owner or occupant of the place to be inspected or searched must be suspected of criminal involvement. Indeed, both cases held that a less stringent standard of probable cause is acceptable where the entry is not to secure evidence of crime against the possessor.</p>
<p>We have suggested nothing to the contrary since <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> and <i>See.</i> Indeed, <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), and <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), dispensed with the warrant requirement in cases involving limited types of inspections and searches.</p>
<p>The critical element in a reasonable search is not that the owner of the property is suspected of crime but that there is reasonable cause to believe that the specific "things" to be searched for and seized are located on the property to which entry is sought.<sup>[6]</sup> In <i>Carroll</i> v. <i>United States,</i> 267 U. S. 132 <span class="star-pagination">*557</span> (1925), it was claimed that the seizure of liquor was unconstitutional because the occupant of a car stopped with probable cause to believe that it was carrying illegal liquor was not subject to arrest. The Court, however, said:</p>
<blockquote>"If their theory were sound, their conclusion would be. The validity of the seizure then would turn wholly on the validity of the arrest without a seizure. But the theory is unsound. The right to search and the validity of the seizure are not dependent on the right to arrest. They are dependent on the reasonable cause the seizing officer has for belief that the contents of the automobile offend against the law." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 158-159</a></span>.</blockquote>
<p>The Court's ultimate conclusion was that "the officers here had justification for the search and seizure," that is, a reasonable "belief that intoxicating liquor was being transported in the automobile which they stopped and searched." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 162</a></span>. See also <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/#700" aria-description="Citation for case: Husty v. United States">282 U. S. 694, 700-701</a></span> (1931).</p>
<p><span class="star-pagination">*558</span> Federal Rule Crim. Proc. 41, which reflects "[t]he Fourth Amendment's policy against unreasonable searches and seizures," <i>United States v. Ventresca,</i> <span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span>, 105 n. 1 (1965), authorizes warrants to search for contraband, fruits or instrumentalities of crime, or "any . . . property that constitutes evidence of the commission of a criminal offense . . . ." Upon proper showing, the warrant is to issue "identifying the property and naming or describing the person or place to be searched." Probable cause for the warrant must be presented, but there is nothing in the Rule indicating that the officers must be entitled to arrest the owner of the "place" to be searched before a search warrant may issue and the "property" may be searched for and seized. The Rule deals with warrants to search, and is unrelated to arrests. Nor is there anything in the Fourth Amendment indicating that absent probable cause to arrest a third party, resort must be had to a subpoena.<sup>[7]</sup></p>
<p>The Court of Appeals for the Sixth Circuit expressed the correct view of Rule 41 and of the Fourth Amendment when, contrary to the decisions of the Court of Appeals and the District Court in the present litigation, it ruled that "[o]nce it is established that probable cause exists to believe a federal crime has been committed a warrant may issue for the search of any property which the magistrate has probable cause to believe may be the place of concealment of evidence of the crime." <i>United States</i> v. <i>Manufacturers Nat. Bank of Detroit,</i> <span class="citation" data-id="336136"><a href="/opinion/336136/united-states-v-manufacturers-national-bank-of-detroit-livernois-lyndon/#703" aria-description="Citation for case: United States v. Manufacturers National Bank of Detroit,...">536 F. 2d 699, 703</a></span> (1976), cert. denied <i>sub nom. </i><i>Wingate</i> v. <i>United States,</i> <span class="citation" data-id="9003942"><a href="/opinion/9011032/wingate-v-united-states/" aria-description="Citation for case: Wingate v. United States">429 U. S. 1039</a></span> (1977). Accord, <i>State</i> v. <i>Tunnel Citgo Services,</i> 149 N. J. Super. 427, 433, <span class="citation" data-id="1964303"><a href="/opinion/1964303/state-v-tunnel-citgo-services/#35" aria-description="Citation for case: State v. Tunnel Citgo Services">374 A. 2d 32, 35</a></span> (1977).</p>
<p>The net of the matter is that "[s]earches and seizures, in a <span class="star-pagination">*559</span> technical sense, are independent of, rather than ancillary to, arrest and arraignment." ALI, A Model Code of Pre-Arraignment Procedure, Commentary 491 (Proposed Off. Draft 1975). The Model Code provides that the warrant application "shall describe with particularity the individuals or places to be searched and the individuals or things to be seized, and shall be supported by one or more affidavits particularly setting forth the facts and circumstances tending to show that such individuals or things are or will be in the places, or the things are or will be in possession of the individuals, to be searched." § SS 220.1 (3). There is no suggestion that the occupant of the place to be searched must himself be implicated in misconduct.</p>
<p>Against this background, it is untenable to conclude that property may not be searched unless its occupant is reasonably suspected of crime and is subject to arrest. And if those considered free of criminal involvement may nevertheless be searched or inspected under civil statutes, it is difficult to understand why the Fourth Amendment would prevent entry onto their property to recover evidence of a crime not committed by them but by others. As we understand the structure and language of the Fourth Amendment and our cases expounding it, valid warrants to search property may be issued when it is satisfactorily demonstrated to the magistrate that fruits, instrumentalities, or evidence of crime is located on the premises. The Fourth Amendment has itself struck the balance between privacy and public need, and there is no occasion or justification for a court to revise the Amendment and strike a new balance by denying the search warrant in the circumstances present here and by insisting that the investigation proceed by subpoena <i>duces tecum,</i> whether on the theory that the latter is a less intrusive alternative or otherwise.</p>
<p>This is not to question that "reasonableness" is the overriding test of compliance with the Fourth Amendment or to assert that searches, however or whenever executed, may never <span class="star-pagination">*560</span> be unreasonable if supported by a warrant issued on probable cause and properly identifying the place to be searched and the property to be seized. We do hold, however, that the courts may not, in the name of Fourth Amendment reasonableness, prohibit the States from issuing warrants to search for evidence simply because the owner or possessor of the place to be searched is not then reasonably suspected of criminal involvement.</p>
<p></p>
<h2>III</h2>
<p>In any event, the reasons presented by the District Court and adopted by the Court of Appeals for arriving at its remarkable conclusion do not withstand analysis. First, as we have said, it is apparent that whether the third-party occupant is suspect or not, the State's interest in enforcing the criminal law and recovering the evidence remains the same; and it is the seeming innocence of the property owner that the District Court relied on to foreclose the warrant to search. But, as respondents themselves now concede, if the third party knows that contraband or other illegal materials are on his property, he is sufficiently culpable to justify the issuance of a search warrant. Similarly, if his ethical stance is the determining factor, it seems to us that whether or not he knows that the soughtafter articles are secreted on his property and whether or not he knows that the articles are in fact the fruits, instrumentalities, or evidence of crime, he will be so informed when the search warrant is served, and it is doubtful that he should then be permitted to object to the search, to withhold, if it is there, the evidence of crime reasonably believed to be possessed by him or secreted on his property, and to forbid the search and insist that the officers serve him with a subpoena <i>duces tecum.</i></p>
<p>Second, we are unpersuaded that the District Court's new rule denying search warrants against third parties and insisting on subpoenas would substantially further privacy interests without seriously undermining law enforcement efforts. Because of the fundamental public interest in implementing <span class="star-pagination">*561</span> the criminal law, the search warrant, a heretofore effective and constitutionally acceptable enforcement tool, should not be suppressed on the basis of surmise and without solid evidence supporting the change. As the District Court understands it, denying third-party search warrants would not have substantial adverse effects on criminal investigations because the nonsuspect third party, once served with a subpoena, will preserve the evidence and ultimately lawfully respond. The difficulty with this assumption is that search warrants are often employed early in an investigation, perhaps before the identity of any likely criminal and certainly before all the perpetrators are or could be known. The seemingly blameless third party in possession of the fruits or evidence may not be innocent at all; and if he is, he may nevertheless be so related to or so sympathetic with the culpable that he cannot be relied upon to retain and preserve the articles that may implicate his friends, or at least not to notify those who would be damaged by the evidence that the authorities are aware of its location. In any event, it is likely that the real culprits will have access to the property, and the delay involved in employing the subpoena <i>duces tecum,</i> offering as it does the opportunity to litigate its validity, could easily result in the disappearance of the evidence, whatever the good faith of the third party.</p>
<p>Forbidding the warrant and insisting on the subpoena instead when the custodian of the object of the search is not then suspected of crime, involves hazards to criminal investigation much more serious than the District Court believed; and the record is barren of anything but the District Court's assumptions to support its conclusions.<sup>[8]</sup> At the very least, the <span class="star-pagination">*562</span> burden of justifying a major revision of the Fourth Amendment has not been carried.</p>
<p>We are also not convinced that the net gain to privacy interests by the District Court's new rule would be worth the candle.<sup>[9]</sup> In the normal course of events, search warrants are <span class="star-pagination">*563</span> more difficult to obtain than subpoenas, since the latter do not involve the judiciary and do not require proof of probable cause. Where, in the real world, subpoenas would suffice, it can be expected that they will be employed by the rational prosecutor. On the other hand, when choice is available under local law and the prosecutor chooses to use the search warrant, it is unlikely that he has needlessly selected the more difficult course. His choice is more likely to be based on the solid belief, arrived at through experience but difficult, if not impossible, to sustain in a specific case, that the warranted search is necessary to secure and to avoid the destruction of evidence.<sup>[10]</sup></p>
<p></p>
<h2>IV</h2>
<p>The District Court held, and respondents assert here, that whatever may be true of third-party searches generally, where the third party is a newspaper, there are additional factors derived from the First Amendment that justify a nearly <i>per se</i> rule forbidding the search warrant and permitting only the subpoena <i>duces tecum.</i> The general submission is that searches of newspaper offices for evidence of crime reasonably believed to be on the premises will seriously threaten the ability of the press to gather, analyze, and disseminate news. This is said to be true for several reasons: First, searches will be physically disruptive to such an extent that timely publication will be impeded. Second, confidential sources of information <span class="star-pagination">*564</span> will dry up, and the press will also lose opportunities to cover various events because of fears of the participants that press files will be readily available to the authorities. Third, reporters will be deterred from recording and preserving their recollections for future use if such information is subject to seizure. Fourth, the processing of news and its dissemination will be chilled by the prospects that searches will disclose internal editorial deliberations. Fifth, the press will resort to self-censorship to conceal its possession of information of potential interest to the police.</p>
<p>It is true that the struggle from which the Fourth Amendment emerged "is largely a history of conflict between the Crown and the press," <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#482" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 482</a></span> (1965), and that in issuing warrants and determining the reasonableness of a search, state and federal magistrates should be aware that "unrestricted power of search and seizure could also be an instrument for stifling liberty of expression." <i>Marcus</i> v. <i>Search Warrant,</i> <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#729" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 729</a></span> (1961). Where the materials sought to be seized may be protected by the First Amendment, the requirements of the Fourth Amendment must be applied with "scrupulous exactitude." <i>Stanford</i> v. <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><i>Texas, supra,</i> at 485</a></span>. "A seizure reasonable as to one type of material in one setting may be unreasonable in a different setting or with respect to another kind of material." <i>Roaden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#501" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496, 501</a></span> (1973). Hence, in <i>Stanford</i> v. <i><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas</a></span></i><i>,</i> the Court invalidated a warrant authorizing the search of a private home for all books, records, and other materials relating to the Communist Party, on the ground that whether or not the warrant would have been sufficient in other contexts, it authorized the searchers to rummage among and make judgments about books and papers and was the functional equivalent of a general warrant, one of the principal targets of the Fourth Amendment. Where presumptively protected materials are sought to be seized, the warrant requirement should be administered to leave as little as possible to the discretion or whim of the officer in the field.</p>
<p><span class="star-pagination">*565</span> Similarly, where seizure is sought of allegedly obscene materials, the judgment of the arresting officer alone is insufficient to justify issuance of a search warrant or a seizure without a warrant incident to arrest. The procedure for determining probable cause must afford an opportunity for the judicial officer to "focus searchingly on the question of obscenity." <i>Marcus</i> v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><i>Search Warrant, supra,</i> at 732</a></span>; <i>A Quantity of Books</i> v. <i>Kansas,</i> <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/#210" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205, 210</a></span> (1964); <i>Lee Art Theatre, Inc.</i> v. <i>Virginia,</i> <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S. 636, 637</a></span> (1968); <i>Roaden</i> v. <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/#502" aria-description="Citation for case: Roaden v. Kentucky"><i>Kentucky, supra,</i> at 502</a></span>; <i>Heller</i> v. <i>New York,</i> <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/#489" aria-description="Citation for case: Heller v. New York">413 U. S. 483, 489</a></span> (1973).</p>
<p>Neither the Fourth Amendment nor the cases requiring consideration of First Amendment values in issuing search warrants, however, call for imposing the regime ordered by the District Court. Aware of the long struggle between Crown and press and desiring to curb unjustified official intrusions, the Framers took the enormously important step of subjecting searches to the test of reasonableness and to the general rule requiring search warrants issued by neutral magistrates. They nevertheless did not forbid warrants where the press was involved, did not require special showings that subpoenas would be impractical, and did not insist that the owner of the place to be searched, if connected with the press, must be shown to be implicated in the offense being investigated. Further, the prior cases do no more than insist that the courts apply the warrant requirements with particular exactitude when First Amendment interests would be endangered by the search. As we see it, no more than this is required where the warrant requested is for the seizure of criminal evidence reasonably believed to be on the premises occupied by a newspaper. Properly administered, the preconditions for a warrantprobable cause, specificity with respect to the place to be searched and the things to be seized, and overall reasonableness should afford sufficient protection against the harms that are assertedly threatened by warrants for searching newspaper offices.</p>
<p><span class="star-pagination">*566</span> There is no reason to believe, for example, that magistrates cannot guard against searches of the type, scope, and intrusiveness that would actually interfere with the timely publication of a newspaper. Nor, if the requirements of specificity and reasonableness are properly applied, policed, and observed, will there be any occasion or opportunity for officers to rummage at large in newspaper files or to intrude into or to deter normal editorial and publication decisions. The warrant issued in this case authorized nothing of this sort. Nor are we convinced, any more than we were in <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665</a></span> (1972), that confidential sources will disappear and that the press will suppress news because of fears of warranted searches. Whatever incremental effect there may be in this regard if search warrants, as well as subpoenas, are permissible in proper circumstances, it does not make a constitutional difference in our judgment.</p>
<p>The fact is that respondents and <i>amici</i> have pointed to only a very few instances in the entire United States since 1971 involving the issuance of warrants for searching newspaper premises. This reality hardly suggests abuse; and if abuse occurs, there will be time enough to deal with it. Furthermore, the press is not only an important, critical, and valuable asset to society, but it is not easily intimidatednor should it be.</p>
<p>Respondents also insist that the press should be afforded opportunity to litigate the State's entitlement to the material it seeks before it is turned over or seized and that whereas the search warrant procedure is defective in this respect, resort to the subpoena would solve the problem. The Court has held that a restraining order imposing a prior restraint upon free expression is invalid for want of notice and opportunity for a hearing, <i>Carroll</i> v. <i>Princess Anne,</i> <span class="citation" data-id="9423852"><a href="/opinion/107801/carroll-v-president-commissioners-of-princess-anne/" aria-description="Citation for case: Carroll v. President &amp; Commissioners of Princess Anne">393 U. S. 175</a></span> (1968), and that seizures not merely for use as evidence but entirely removing arguably protected materials from circulation may be effected only after an adversary hearing and a judicial <span class="star-pagination">*567</span> finding of obscenity. <i>A Quantity of Books</i> v. <i><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">Kansas, supra</a></span></i><i>.</i> But presumptively protected materials are not necessarily immune from seizure under warrant for use at a criminal trial. Not every such seizure, and not even most, will impose a prior restraint. <i>Heller</i> v. <i>New <span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">York, supra</a></span></i><i>.</i> And surely a warrant to search newspaper premises for criminal evidence such as the one issued here for news photographs taken in a public place carries no realistic threat of prior restraint or of any direct restraint whatsoever on the publication of the Daily or on its communication of ideas. The hazards of such warrants can be avoided by a neutral magistrate carrying out his responsibilities under the Fourth Amendment, for he has ample tools at his disposal to confine warrants to search within reasonable limits.</p>
<p>We note finally that if the evidence sought by warrant is sufficiently connected with the crime to satisfy the probable-cause requirement, it will very likely be sufficiently relevant to justify a subpoena and to withstand a motion to quash. Further, Fifth Amendment and state shield-law objections that might be asserted in opposition to compliance with a subpoena are largely irrelevant to determining the legality of a search warrant under the Fourth Amendment. Of course, the Fourth Amendment does not prevent or advise against legislative or executive efforts to establish nonconstitutional protections against possible abuses of the search warrant procedure, but we decline to reinterpret the Amendment to impose a general constitutional barrier against warrants to search newspaper premises, to require resort to subpoenas as a general rule, or to demand prior notice and hearing in connection with the issuance of search warrants.</p>
<p></p>
<h2>V</h2>
<p>We accordingly reject the reasons given by the District Court and adopted by the Court of Appeals for holding the search for photographs at the Stanford Daily to have been <span class="star-pagination">*568</span> unreasonable within the meaning of the Fourth Amendment and in violation of the First Amendment. Nor has anything else presented here persuaded us that the Amendments forbade this search. It follows that the judgment of the Court of Appeals is reversed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BRENNAN took no part in the consideration or decision of these cases.</p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>I join the opinion of the Court, and I write simply to emphasize what I take to be the fundamental error of MR. JUSTICE STEWART'S dissenting opinion. As I understand that opinion, it would read into the Fourth Amendment, as a new and <i>per se</i> exception, the rule that any search of an entity protected by the Press Clause of the First Amendment is unreasonable so long as a subpoena could be used as a substitute procedure. Even aside from the difficulties involved in deciding on a case-by-case basis whether a subpoena can serve as an adequate substitute,<sup>[1]</sup> I agree with the Court that there is no constitutional basis for such a reading.</p>
<p><span class="star-pagination">*569</span> If the Framers had believed that the press was entitled to a special procedure, not available to others, when government authorities required evidence in its possession, one would have expected the terms of the Fourth Amendment to reflect that belief. As the opinion of the Court points out, the struggle from which the Fourth Amendment emerged was that between Crown and press. <i>Ante,</i> at 564. The Framers were painfully aware of that history, and their response to it was the Fourth Amendment. <i>Ante,</i> at 565. Hence, there is every reason to believe that the usual procedures contemplated by the Fourth Amendment do indeed apply to the press, as to every other person.</p>
<p>This is not to say that a warrant which would be sufficient to support the search of an apartment or an automobile necessarily would be reasonable in supporting the search of a <span class="star-pagination">*570</span> newspaper office. As the Court's opinion makes clear, <i>ante,</i> at 564-565, the magistrate must judge the reasonableness of every warrant in light of the circumstances of the particular case, carefully considering the description of the evidence sought, the situation of the premises, and the position and interests of the owner or occupant. While there is no justification for the establishment of a separate Fourth Amendment procedure for the press, a magistrate asked to issue a warrant for the search of press offices can and should take cognizance of the independent values protected by the First Amendment such as those highlighted by MR. JUSTICE STEWARTwhen he weighs such factors. If the reasonableness and particularity requirements are thus applied, the dangers are likely to be minimal.<sup>[2]</sup><i><span class="citation" data-id="9425413"><a href="/opinion/108853/heller-v-new-york/" aria-description="Citation for case: Heller v. New York">Ibid.</a></span></i></p>
<p>In any event, considerations such as these are the province of the Fourth Amendment. There is no authority either in history or in the Constitution itself for exempting certain classes of persons or entities from its reach.<sup>[3]</sup></p>
<p>MR. JUSTICE STEWART, with whom MR. JUSTICE MARSHALL joins, dissenting.</p>
<p>Believing that the search by the police of the offices of the <span class="star-pagination">*571</span> Stanford Daily infringed the First and Fourteenth Amendments' guarantee of a free press, I respectfully dissent.<sup>[1]</sup></p>
<p></p>
<h2>I</h2>
<p>It seems to me self-evident that police searches of newspaper offices burden the freedom of the press. The most immediate and obvious First Amendment injury caused by such a visitation by the police is physical disruption of the operation of the newspaper. Policemen occupying a newsroom and searching it thoroughly for what may be an extended period of time<sup>[2]</sup> will inevitably interrupt its normal operations, and thus impair or even temporarily prevent the processes of newsgathering, writing, editing, and publishing. By contrast, a subpoena would afford the newspaper itself an opportunity to locate whatever material might be requested and produce it.</p>
<p>But there is another and more serious burden on a free press imposed by an unannounced police search of a newspaper office: the possibility of disclosure of information received from confidential sources, or of the identity of the sources themselves. Protection of those sources is necessary to ensure that <span class="star-pagination">*572</span> the press can fulfill its constitutionally designated function of informing the public,<sup>[3]</sup> because important information can often be obtained only by an assurance that the source will not be revealed. <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#725" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665, 725-736</a></span> (dissenting opinion).<sup>[4]</sup> And the Court has recognized that "`without some protection for seeking out the news, freedom of the press could be eviscerated.'" <i>Pell</i> v. <i>Procunier,</i> <span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#833" aria-description="Citation for case: Pell v. Procunier">417 U. S. 817, 833</a></span>.</p>
<p>Today the Court does not question the existence of this constitutional protection, but says only that it is not "convinced. . . that confidential sources will disappear and that the press will suppress news because of fears of warranted searches." <i>Ante,</i> at 566. This facile conclusion seems to me to ignore common experience. It requires no blind leap of faith to understand that a person who gives information to a journalist only on condition that his identity will not be revealed will be less likely to give that information if he knows that, despite the journalist's assurance, his identity may in fact be disclosed. And it cannot be denied that confidential information may be exposed to the eyes of police officers who execute a search warrant by rummaging through the files, cabinets, desks, and wastebaskets of a newsroom.<sup>[5]</sup> Since the indisputable effect of such searches will thus be to prevent a newsman from being able to promise confidentiality to his potential sources, it seems obvious to me that a journalist's <span class="star-pagination">*573</span> access to information, and thus the public's, will thereby be impaired.<sup>[6]</sup></p>
<p>A search warrant allows police officers to ransack the files of a newspaper, reading each and every document until they have found the one named in the warrant,<sup>[7]</sup> while a subpoena would permit the newspaper itself to produce only the specific documents requested. A search, unlike a subpoena, will therefore lead to the needless exposure of confidential information completely unrelated to the purpose of the investigation. The knowledge that police officers can make an unannounced raid on a newsroom is thus bound to have a deterrent effect on the availability of confidential news sources. The end result, wholly inimical to the First Amendment, will be a diminishing flow of potentially important information to the public.</p>
<p>One need not rely on mere intuition to reach this conclusion. The record in this case includes affidavits not only from members of the staff of the Stanford Daily but also from many professional journalists and editors, attesting to precisely such personal experience.<sup>[8]</sup> Despite the Court's rejection of this <span class="star-pagination">*574</span> uncontroverted evidence, I believe it clearly establishes that unannounced police searches of newspaper offices will significantly burden the constitutionally protected function of the press to gather news and report it to the public.</p>
<p></p>
<h2>II</h2>
<p>In <i>Branzburg</i> v. <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Hayes, supra</a></span></i><i>,</i> the more limited disclosure of a journalist's sources caused by compelling him to testify was held to be justified by the necessity of "pursuing and prosecuting those crimes reported to the press by informants and . . . thus deterring the commission of such crimes in the future." <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#695" aria-description="Citation for case: Branzburg v. Hayes">408 U. S., at 695</a></span>. The Court found that these important societal interests would be frustrated if a reporter were able to claim an absolute privilege for his confidential sources. In the present case, however, the respondents do not claim that any of the evidence sought was privileged from disclosure; they claim only that a subpoena would have served equally well to produce that evidence. Thus, we are not concerned with the principle, central to <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Branzburg</a></span>,</i> that "`the public . . . has a right to every man's evidence,'" <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#688" aria-description="Citation for case: Branzburg v. Hayes"><i>id.,</i> at 688</a></span>, but only with whether any significant societal interest would be impaired if the police were generally required to obtain evidence from the press by means of a subpoena rather than a search.</p>
<p>It is well to recall the actual circumstances of this litigation. The application for a warrant showed only that there was reason to believe that photographic evidence of assaults on the police would be found in the offices of the Stanford Daily. There was no emergency need to protect life or property by an <span class="star-pagination">*575</span> immediate search. The evidence sought was not contraband, but material obtained by the Daily in the normal exercise of its journalistic function. Neither the Daily nor any member of its staff was suspected of criminal activity. And there was no showing that the Daily would not respond to a subpoena commanding production of the photographs, or that for any other reason a subpoena could not be obtained. Surely, then, a subpoena <i>duces tecum</i> would have been just as effective as a police raid in obtaining the production of the material sought by the Santa Clara County District Attorney.</p>
<p>The District Court and the Court of Appeals clearly recognized that <i>if</i> the affidavits submitted with a search warrant application should demonstrate probable cause to believe that a subpoena would be impractical, the magistrate must have the authority to issue a warrant. In such a case, by definition, a subpoena would not be adequate to protect the relevant societal interest. But they held, and I agree, that a warrant should issue only after the magistrate has performed the careful "balanc[ing] of these vital constitutional and societal interests." <i>Branzburg</i> v. <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#710" aria-description="Citation for case: Branzburg v. Hayes"><i>Hayes, supra,</i> at 710</a></span> (PowELL, J., concurring).<sup>[9]</sup></p>
<p>The decisions of this Court establish that a prior adversary judicial hearing is generally required to assess in advance any threatened invasion of First Amendment liberty.<sup>[10]</sup> A search by police officers affords no timely opportunity for such a <span class="star-pagination">*576</span> hearing, since a search warrant is ordinarily issued <i>ex parte</i> upon the affidavit of a policeman or prosecutor. There is no opportunity to challenge the necessity for the search until after it has occurred and the constitutional protection of the newspaper has been irretrievably invaded.</p>
<p>On the other hand, a subpoena would allow a newspaper, through a motion to quash, an opportunity for an adversary hearing with respect to the production of any material which a prosecutor might think is in its possession. This very principle was emphasized in the <i><span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/" aria-description="Citation for case: Branzburg v. Hayes">Branzburg</a></span></i> case:</p>
<blockquote>"[I]f the newsman is called upon to give information bearing only a remote and tenuous relationship to the subject of the investigation, or if he has some other reason to believe that his testimony implicates confidential source relationships without a legitimate need of law enforcement, he will have access to the court on a motion to quash and an appropriate protective order may be entered." <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#710" aria-description="Citation for case: Branzburg v. Hayes">408 U. S., at 710</a></span> (POWELL, J., concurring).</blockquote>
<p>See also <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#707" aria-description="Citation for case: Branzburg v. Hayes"><i>id.,</i> at 707-708</a></span> (opinion of Court). If, in the present litigation, the Stanford Daily had been served with a subpoena, it would have had an opportunity to demonstrate to the court what the police ultimately found to be truethat the evidence sought did not exist. The legitimate needs of government thus would have been served without infringing the freedom of the press.</p>
<p></p>
<h2>III</h2>
<p>Perhaps as a matter of abstract policy a newspaper office should receive no more protection from unannounced police searches than, say, the office of a doctor or the office of a bank. But we are here to uphold a Constitution. And our Constitution does not explicitly protect the practice of medicine or the business of banking from all abridgment by government. It does explicitly protect the freedom of the press.</p>
<p><span class="star-pagination">*577</span> For these reasons I would affirm the judgment of the Court of Appeals.</p>
<p>MR. JUSTICE STEVENS, dissenting.</p>
<p>The novel problem presented by this case is an outgrowth of the profound change in Fourth Amendment law that occurred in 1967, when <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>, was decided. The question is what kind of "probable cause" must be established in order to obtain a warrant to conduct an unannounced search for documentary evidence in the private files of a person not suspected of involvement in any criminal activity. The Court holds that a reasonable belief that the files contain relevant evidence is a sufficient justification. This holding rests on a misconstruction of history and of the Fourth Amendment's purposely broad language.</p>
<p>The Amendment contains two Clauses, one protecting "persons, houses, papers, and effects, against unreasonable searches and seizures," the other regulating the issuance of warrants: "no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." When these words were written, the procedures of the Warrant Clause were not the primary protection against oppressive searches. It is unlikely that the authors expected private papers ever to be among the "things" that could be seized with a warrant, for only a few years earlier, in 1765, Lord Camden had delivered his famous opinion denying that any magistrate had power to authorize the seizure of private papers.<sup>[1]</sup> Because all such <span class="star-pagination">*578</span> seizures were considered unreasonable, the Warrant Clause was not framed to protect against them.</p>
<p>Nonetheless, the authors of the Clause used words that were adequate for situations not expressly contemplated at the time. As Mr. Justice Black noted, the Amendment does not "attempt to describe with precision what was meant by its words `probable cause'"; the words of the Amendment are deliberately "imprecise and flexible."<sup>[2]</sup> And MR. JUSTICE STEWART, when confronted with the problem of applying the probable-cause standard in an unprecedented situation, observed that "[t]he standard of reasonableness embodied in the Fourth Amendment demands that the showing of justification match the degree of intrusion."<sup>[3]</sup> Today, for the first time, the Court has an opportunity to consider the kind of showing that is necessary to justify the vastly expanded "degree of intrusion" upon privacy that is authorized by the opinion in <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden, supra</a></span></i><i>.</i></p>
<p>In the pre-<span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden"><i>Hayden</i></a></span> era warrants were used to search for contraband,<sup>[4]</sup> weapons, and plunder, but not for "mere evidence." <span class="star-pagination">*579</span> <sup>[5]</sup> The practical effect of the rule prohibiting the issuance of warrants to search for mere evidence was to narrowly limit not only the category of objects, but also the category of persons and the character of the privacy interests that might be affected by an unannounced police search.</p>
<p>Just as the witnesses who participate in an investigation or a trial far outnumber the defendants, the persons who possess evidence that may help to identify an offender, or explain an aspect of a criminal transaction, far outnumber those who have custody of weapons or plunder. Countless law-abiding citizens doctors, lawyers, merchants, customers, bystanders may have documents in their possession that relate to an ongoing criminal investigation. The consequences of subjecting this large category of persons to unannounced police searches are extremely serious. The <i>ex parte</i> warrant procedure enables the prosecutor to obtain access to privileged documents that could not be examined if advance notice gave the custodian an opportunity to object.<sup>[6]</sup> The search for the documents described in a warrant may involve the inspection <span class="star-pagination">*580</span> of files containing other private matter.<sup>[7]</sup> The dramatic character of a; sudden search may cause an entirely unjustified injury to the reputation of the persons searched.<sup>[8]</sup></p>
<p><span class="star-pagination">*581</span> Of greatest importance, however, is the question whether the offensive intrusion on the privacy of the ordinary citizen is justified by the law enforcement interest it is intended to vindicate. Possession of contraband or the proceeds or tools of crime gives rise to two inferences: that the custodian is involved in the criminal activity, and that, if given notice of an intended search, he will conceal or destroy what is being sought. The probability of criminal culpability justifies the invasion of his privacy; the need to accomplish the law enforcement purpose of the search justifies acting without advance notice and by force, if necessary. By satisfying the probable-cause standard appropriate for weapons or plunder, the police effectively demonstrate that no less intrusive method of investigation will succeed.</p>
<p>Mere possession of documentary evidence, however, is much less likely to demonstrate that the custodian is guilty of any wrongdoing or that he will not honor a subpoena or informal request to produce it. In the pre-<span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden"><i>Hayden</i></a></span> era, evidence of that kind was routinely obtained by procedures that presumed that the custodian would respect his obligation to obey subpoenas and to cooperate in the investigation of crime. These procedures had a constitutional dimension. For the innocent citizen's interest in the privacy of his papers and possessions is an aspect of liberty protected by the Due Process Clause of the Fourteenth Amendment. Notice and an opportunity to object to the deprivation of the citizen's liberty are, therefore, the constitutionally mandated general rule.<sup>[9]</sup> An <span class="star-pagination">*582</span> exception to that rule can only be justified by strict compliance with the Fourth Amendment. That Amendment flatly prohibits the issuance of any warrant unless justified by probable cause.</p>
<p>A showing of probable cause that was adequate to justify the issuance of a warrant to search for stolen goods in the 18th century does not automatically satisfy the new dimensions of the Fourth Amendment in the post-<span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden"><i>Hayden</i></a></span> era.<sup>[10]</sup> In <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> itself, the Court recognized that the meaning of probable cause should be reconsidered in the light of the new authority it conferred on the police.<sup>[11]</sup> The only conceivable justification for an unannounced search of an innocent citizen is the fear that, if notice were given, he would conceal or destroy the object of the search. Probable cause to believe that the <span class="star-pagination">*583</span> custodian is a criminal, or that he holds a criminal's weapons, spoils, or the like, justifies that fear,<sup>[12]</sup> and therefore such a showing complies with the Clause. But if nothing said under oath in the warrant application demonstrates the need for an unannounced search by force, the probable-cause requirement is not satisfied. In the absence of some other showing of reasonableness,<sup>[13]</sup> the ensuing search violates the Fourth Amendment.</p>
<p>In this case, the warrant application set forth no facts suggesting that respondents were involved in any wrongdoing or would destroy the desired evidence if given notice of what the police desired. I would therefore hold that the warrant did not comply with the Warrant Clause and that the search was unreasonable within the meaning of the first Clause of the Fourth Amendment.</p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 76-1600, <i>Bergna, District Attorney of Santa Clara County, et al.</i> v. <i>Stanford Daily et al.,</i> also on certiorari to the same court.</p>
<p>[]  A brief of <i>amici curiae</i> urging reversal was filed for their respective States by <i>William J. Baxley,</i> Attorney General of Alabama; <i>Avrum M.</i> <i>Gross,</i> Attorney General of Alaska; <i>Evelle J. Younger,</i> Attorney General of California, and <i>W. Eric Collins</i> and <i>Dane R. Gillette,</i> Deputy Attorneys General; <i>Arthur K. Bolton,</i> Attorney General of Georgia; <i>Wayne L. Kidwell,</i> Attorney General of Idaho; <i>William J. Scott,</i> Attorney General of Illinois; <i>Theodore L. Sendak,</i> Attorney General of Indiana; <i>Francis B. Burch,</i> Attorney General of Maryland; <i>Francis X. Bellotti,</i> Attorney General of Massachusetts; <i>A. F. Summer,</i> Attorney General of Mississippi; <i>Paul L. Douglas,</i> Attorney General of Nebraska; <i>David H. Souter,</i> Attorney General of New Hampshire; <i>Toney Anaya,</i> Attorney General of New Mexico; <i>James A. Redden,</i> Attorney General of Oregon; <i>Robert P. Kane,</i> Attorney General of Pennsylvania; <i>Robert B. Hansen,</i> Attorney General of Utah; and <i>Anthony F. Troy,</i> Attorney General of Virginia. A brief of <i>amici curiae</i> urging reversal was filed by <i>Frank Carrington, Wayne W. Schmidt, Glen R. Murphy, James P. Costello, Robert Smith,</i> and <i>Richard F. Mayer</i> for Americans for Effective Law Enforcement, Inc., et al.
</p>
<p>Briefs of <i>amici curiae</i> urging affirmance were filed by <i>Dominic P. Gentile, John E. Ackerman,</i> and <i>Joseph Beeler</i> for the National Association of Criminal Defense Lawyers, Inc.; and by <i>Lloyd N. Cutler, Dennis M. Flannery, William T. Lake, A. Stephen Hut, Jr., Arthur B. Hanson, James R. Cregan, Erwin G. Krasnow, Richard M. Schmidt, Jr., J. Laurent Scharff, Christopher B. Fager, David S. Barr,</i> and <i>Mortimer Becker</i> for the Reporters Committee for Freedom of the Press et al.</p>
<p>Briefs of <i>amici curiae</i> were filed by <i>Solicitor General McCree, Assistant Attorney General Civiletti, Deputy Solicitor General Frey, Harriet S. Shapiro,</i> and <i>Elliot Schulder</i> for the United States; and by <i>Edwin L. Miller, Jr., Richard D. Huffman,</i> and <i>Peter C. Lehman</i> for the National District Attorneys Assn. et al.</p>
<p>[1]  There was extensive damage to the administrative offices resulting from the occupation and the removal of the demonstrators.</p>
<p>[2]  The District Court did not find it necessary to resolve this dispute.</p>
<p>[3]  The Court of Appeals also approved the award of attorney's fees to respondents pursuant to the Civil Rights Attorney's Fees Awards Act of 1976, <span class="citation no-link">42 U. S. C. § 1988</span> (1976 ed.). We do not consider the propriety of this award in light of our disposition on the merits reversing the judgment upon which the award was predicated.</p>
<p>[4]  Petitioners in No. 76-1484 are the chief of police and the officers under his command who conducted the search. Petitioners in No. 76-1600 are the district attorney and a deputy district attorney who participated in the obtaining of the search warrant. The action against the judge who issued the warrant was subsequently dismissed upon the motion of respondents.</p>
<p>[5]  Respondents rely on four state cases to support the holding that a warrant may not issue unless it is shown that a subpoena is impracticable: <i>Owens</i> v. <i>Way,</i> <span class="citation" data-id="5579679"><a href="/opinion/5729336/owens-v-way/" aria-description="Citation for case: Owens v. Way">141 Ga. 796</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20E./82/132/">82 S. E. 132</a></span> (1914); <i>Newberry v. Carpenter,</i> <span class="citation" data-id="7938056"><a href="/opinion/7985025/newberry-v-carpenter/" aria-description="Citation for case: Newberry v. Carpenter">107 Mich. 567</a></span>, <span class="citation" data-id="9283149"><a href="/opinion/9288277/newberry-v-circuit-judge/" aria-description="Citation for case: Newberry v. Circuit Judge">65 N. W. 530</a></span> (1895); <i>People</i> v. <i>Carver,</i> <span class="citation" data-id="6158352"><a href="/opinion/6290228/people-v-carver/" aria-description="Citation for case: People v. Carver">172 Misc. 820</a></span>, 16 N. Y. S. 2d 268 (County Ct. 1939); and <i>Commodity Mfg. Co.</i> v. <i>Moore,</i> 198 N. Y. S. 45 (Sup. Ct. 1923). None of these cases, however, stands for the proposition arrived at by the District Court and urged by respondents. The District Court also drew upon <i>Bacon</i> v. <i>United States,</i> <span class="citation" data-id="299535"><a href="/opinion/299535/in-the-matter-of-the-petition-of-leslie-bacon-for-writ-of-habeas-corpus-v/" aria-description="Citation for case: In the Matter of the Petition of Leslie Bacon for Writ of...">449 F. 2d 933</a></span> (CA9 1971), but that case dealt with arrest of a material witness and is unpersuasive with respect to the search for criminal evidence.</p>
<p>[6]  The same view has been expressed by those who have given close attention to the Fourth Amendment. "It does not follow, however, that probable cause for arrest would justify the issuance of a search warrant, or, on the other hand, that probable cause for a search warrant would necessarily justify an arrest. Each requires probabilities as to somewhat different facts and circumstancesa point which is seldom made explicit in the appellate cases. . . .
</p>
<p>"This means, for one thing, that while probable cause for arrest requires information justifying a reasonable belief that a crime has been committed and that a particular person committed it, a search warrant may be issued on a complaint which does not identify any particular person as the likely offender. Because the complaint for a search warrant is not `filed as the basis of a criminal prosecution,' it need not identify the person in charge of the premises or name the person in possession or any other person as the offender." LaFave, Search and Seizure: "The Course of True Law ... Has Not . . . Run Smooth," U. Ill. Law Forum 255, 260-261 (1966) (footnotes omitted).</p>
<p>"Furthermore, a warrant may issue to search the premises of anyone, without any showing that the occupant is guilty of any offense whatever." T. Taylor, Two Studies in Constitutional Interpretation 48-49 (1969). "Search warrants may be issued only by a neutral and detached judicial officer, upon a showing of probable causethat is, reasonable grounds to believethat criminally related objects are in the place which the warrant authorizes to be searched, at the time when the search is authorized to be conducted." Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 358 (1974) (footnotes omitted).</p>
<p>"Two conclusions necessary to the issuance of the warrant must be supported by substantial evidence: that the items sought are in fact seizable by virtue of being connected with criminal activity, and that the items will be found in the place to be searched. By comparison, the right of arrest arises only when a crime is committed or attempted in the presence of the arresting officer or when the officer has `reasonable grounds to believe'sometimes stated `probable cause to believe'that a felony has been committed by the person to be arrested. Although it would appear that the conclusions which justify either arrest or the issuance of a search warrant must be supported by evidence of the same degree of probity, it is clear that the conclusions themselves are not identical.</p>
<p>"In the case of arrest, the conclusion concerns the guilt of the arrestee, whereas in the case of search warrants, the conclusions go to the connection of the items sought with crime and to their present location." Comment, <span class="citation no-link">28 U. Chi. L. Rev. 664</span>, 687 (1961) (footnotes omitted).</p>
<p>[7]  Petitioners assert that third-party searches have long been authorized under Cal. Penal Code Ann. § 1524 (West 1970), which provides that fruits, instrumentalities, and evidence of crime "may be taken on the warrant from any place, or from any person in whose possession [they] may be." The District Court did not advert to this provision.</p>
<p>[8]  It is also far from clear, even apart from the dangers of destruction and removal, whether the use of the subpoena <i>duces tecum</i> under circumstances where there is probable cause to believe that a crime has been committed and that the materials sought constitute evidence of its commission will result in the production of evidence with sufficient regularity to satisfy the public interest in law enforcement. Unlike the individual whose privacy is invaded by a search, the recipient of a subpoena may assert the Fifth Amendment privilege against self-incrimination in response to a summons to produce evidence or give testimony. See <i>Maness v. Meyers,</i> <span class="citation" data-id="9425898"><a href="/opinion/109130/maness-v-meyers/" aria-description="Citation for case: Maness v. Meyers">419 U. S. 449</a></span> (1975). This privilege is not restricted to suspects. We have construed it broadly as covering any individual who might be incriminated by the evidence in connection with which the privilege is asserted. <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span> (1951). The burden of overcoming an assertion of the Fifth Amendment privilege, even if prompted by a desire not to cooperate rather than any real fear of self-incrimination, is one which prosecutors would rarely be able to meet in the early stages of an investigation despite the fact they did not regard the witness as a suspect. Even time spent litigating such matters could seriously impede criminal investigations.</p>
<p>[9]  We reject totally the reasoning of the District Court that additional protections are required to assure that the Fourth Amendment rights of third parties are not violated because of the unavailability of the exclusionary rule as a deterrent to improper searches of premises in the control of nonsuspects. <span class="citation" data-id="2344500"><a href="/opinion/2344500/stanford-daily-v-zurcher/#131" aria-description="Citation for case: Stanford Daily v. Zurcher">353 F. Supp. 124, 131-132</a></span> (1972). In <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/" aria-description="Citation for case: Alderman v. United States">394 U. S. 165</a></span> (1969), we expressly ruled that suppression of the fruits of a Fourth Amendment violation may be urged only by those whose rights were infringed by the search itself and not by those aggrieved solely by the introduction of incriminating evidence. The predicate for this holding was that the additional deterrent effect of permitting defendants whose Fourth Amendment rights had not been violated to challenge infringements of the privacy interests of others did not "justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth." <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#175" aria-description="Citation for case: Alderman v. United States"><i>Id.,</i> at 175</a></span>. For similar reasons, we conclude that the interest in deterring illegal third-party searches does not justify a rule such as that adopted by the District Court. It is probably seldom that police during the investigatory stage when most searches occur will be so convinced that no potential defendant will have standing to exclude evidence on Fourth Amendment grounds that they will feel free to ignore constitutional restraints. In any event, it would be placing the cart before the horse to prohibit searches otherwise conforming to the Fourth Amendment because of a perception that the deterrence provided by the existing rules of standing is insufficient to discourage illegal searches. Cf. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#309" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 309</a></span> (1967). Finally, the District Court overlooked the fact that the California Supreme Court has ruled as a matter of state law that the legality of a search and seizure may be challenged by anyone against whom evidence thus obtained is used. <i>Kaplan</i> v. <i>Superior Court,</i> <span class="citation" data-id="9618981"><a href="/opinion/1396227/kaplan-v-superior-court/" aria-description="Citation for case: Kaplan v. Superior Court">6 Cal. 3d 150</a></span>, <span class="citation" data-id="9618981"><a href="/opinion/1396227/kaplan-v-superior-court/" aria-description="Citation for case: Kaplan v. Superior Court">491 P. 2d 1</a></span> (1971).</p>
<p>[10]  Petitioners assert that the District Court ignored the realities of California law and practice that are said to preclude or make very difficult the use of subpoenas as investigatory techniques. If true, the choice of procedures may not always be open to the diligent prosecutor in the State of California.</p>
<p>[1]  For example, respondents had announced a policy of destroying any photographs that might aid prosecution of protesters. App. 118, 152-153. While this policy probably reflected the deep feelings of the Vietnam era, and one may assume that under normal circumstances few, if any, press entities would adopt a policy so hostile to law enforcement, respondents' policy at least illustrates the possibility of such hostility. Use of a subpoena, as proposed by the dissent, would be of no utility in face of a policy of destroying evidence. And unless the policy were publicly announced, it probably would be difficult to show the impracticality of a subpoena as opposed to a search warrant.
</p>
<p>At oral argument, counsel for respondents stated that the announced policy of the Stanford Daily conceivably could have extended to the destruction of evidence of <i>any</i> crime:</p>
<p>"QUESTION: Let us assume you had a picture of the commission of a crime. For example, in banks they take pictures regularly of, not only of robbery but of murder committed in a bank and there have been pictures taken of the actual pulling of the trigger or the pointing of the gun and pulling of the trigger. There is a very famous one related to the assassination of President Kennedy.</p>
<p>"What would the policy of the <i>Stanford Daily</i> be with respect to that? Would it feel free to destroy it at any time before a subpoena had been served?</p>
<p>"MR. FALK: Theliterally read, the policy of the <i>Daily</i> requires me to give an affirmative answer. I find it hard to believe that in an example such as that, that the policy would have been carried out. It was not addressed to a picture of that kind or in that context.</p>
<p>"QUESTION: Well, I am sure you were right. I was just getting to the scope of your theory.</p>
<p>"MR. FALK: Our</p>
<p>"QUESTION: What is the difference between the pictures Justice Powell just described and the pictures they were thought to have?</p>
<p>"MR. FALK: Well, it simply is a distinction that</p>
<p>"QUESTION: Attacking police officers instead of the President. That is the only difference." Tr. of Oral Arg. 39-40.</p>
<p>While the existence of this policy was not before the magistrate at the time of the warrant's issuance, <span class="citation" data-id="2344500"><a href="/opinion/2344500/stanford-daily-v-zurcher/" aria-description="Citation for case: Stanford Daily v. Zurcher">353 F. Supp. 124</a></span>, 135 n. 16 (ND Cal. 1972), it illustrates the possible dangers of creating separate standards for the press alone.</p>
<p>[2]  Similarly, the magnitude of a proposed searoh directed at <i>any</i> third party and the nature and significance of the material sought are factors properly considered as bearing on the reasonableness and particularity requirements. Moreover, there is no reason why police officers executing a warrant should not seek the cooperation of the subject party, in order to prevent needless disruption.</p>
<p>[3]  The concurring opinion in <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#709" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665, 709-710</a></span> (1972) (POWELL, J.), does not support the view that the Fourth Amendment contains an implied exception for the press, through the operation of the First Amendment. That opinion noted only that in considering a motion to quash a subpoena directed to a newsman, the court should balance the competing values of a free press and the societal interest in detecting and prosecuting crime. The concurrence expressed no doubt as to the applicability of the subpoena procedure to members of the press. Rather than advocating the creation of a special procedural exception for the press, it approved recognition of First Amendment concerns within the applicable procedure. The concurring opinion may, however, properly be read as supporting the view expressed in the text above, and in the Court's opinion, that under the warrant requirement of the Fourth Amendment, the magistrate should consider the values of a free press as well as the societal interest in enforcing the criminal laws.</p>
<p>[1]  I agree with the Court that the <i>Fourth</i> Amendment does not forbid the issuance of search warrants "simply because the owner or possessor of the place to be searched is not then reasonably suspected of criminal involvement." <i>Ante,</i> at 560. Thus, contrary to the understanding expressed in the concurring opinion, I do not "read" anything "into the Fourth Amendment." <i>Ante,</i> at 568. Instead, I would simply enforce the provisions of the <i>First</i> Amendment.</p>
<p>[2]  One search of a radio station in Los Angeles lasted over eight hours. Note, Search and Seizure of the Media: A Statutory, Fourth Amendment and First Amendment Analysis, <span class="citation no-link">28 Stan. L. Rev. 957</span>, 957-959 (1976).</p>
<p>[3]  See <i>Mills</i> v. <i>Alabama,</i> <span class="citation" data-id="9423221"><a href="/opinion/107235/mills-v-alabama/#219" aria-description="Citation for case: Mills v. Alabama">384 U. S. 214, 219</a></span>; <i>New York Times Co.</i> v. <i>Sullivan,</i> <span class="citation" data-id="9422744"><a href="/opinion/106761/new-york-times-co-v-sullivan/#269" aria-description="Citation for case: New York Times Co. v. Sullivan">376 U. S. 254, 269</a></span>; <i>Grosjean</i> v. <i>American Press Co.,</i> <span class="citation" data-id="102601"><a href="/opinion/102601/grosjean-v-american-press-co/#250" aria-description="Citation for case: Grosjean v. American Press Co.">297 U. S. 233, 250</a></span>.</p>
<p>[4]  Recognizing the importance of this confidential relationship, at least 26 States have enacted so-called "shield laws" protecting reporters. Note, The Newsman's Privilege After <i>Branzburg:</i> The Case for a Federal Shield Law, <span class="citation no-link">24 UCLA L. Rev. 160</span>, 167 n. 41 (1976).</p>
<p>[5]  In this case, the policemen executing the search warrant were concededly in a position to read confidential material unrelated to the object of their search; whether they in fact did so is disputed.</p>
<p>[6]  This prospect of losing access to confidential sources may cause reporters to engage in "self-censorship," in order to avoid publicizing the fact that they may have confidential information. See <i>New York Times Co.</i> v. <span class="citation" data-id="9422744"><a href="/opinion/106761/new-york-times-co-v-sullivan/#279" aria-description="Citation for case: New York Times Co. v. Sullivan"><i>Sullivan, supra,</i> at 279</a></span>; <i>Smith</i> v. <i>California,</i> <span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#154" aria-description="Citation for case: Smith v. California">361 U. S. 147, 154</a></span>. Or journalists may destroy notes and photographs rather than save them for reference and use in future stories. Either of these indirect effects of police searches would further lessen the flow of news to the public.</p>
<p>[7]  The Court says that "if the requirements of specificity and reasonableness are properly applied, policed, and observed" there will be no opportunity for the police to "rummage at large in newspaper files." <i>Ante,</i> at 566. But in order to find a particular document, no matter how specifically it is identified in the warrant, the police will have to search every place where it might beincluding, presumably, every file in the officeand to examine each document they find to see if it is the correct one. I thus fail to see how the Fourth Amendment would provide an effective limit to these searches.</p>
<p>[8]  According to these uncontradicted affidavits, when it becomes known that a newsman cannot guarantee confidentiality, potential sources of information often become unavailable. Moreover, efforts are sometimes made, occasionally by force, to prevent reporters and photographers from covering newsworthy events, because of fear that the police will seize the newsman's notes or photographs as evidence. The affidavits of the members of the staff of the Stanford Daily give examples of how this very search produced such an impact on the Daily's own journalistic functions.</p>
<p>[9]  The petitioners have argued here that in fact there was reason to believe that the Daily would not honor a subpoena. Regardless of the probative value of this information, it is irrelevant, since it was not before the magistrate when he issued the warrant. <i>Whiteley</i> v. <i>Warden,</i> <span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span>, 565 n. 8; <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>, 413 n. 3; <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, 109 n. 1; see <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span>.</p>
<p>[10]  <i>E. g., </i><i>United States</i> v. <i>Thirty-seven Photographs,</i> <span class="citation" data-id="9424558"><a href="/opinion/108332/united-states-v-thirty-seven-37-photographs/" aria-description="Citation for case: United States v. Thirty-Seven (37) Photographs">402 U. S. 363</a></span>; <i>Carroll</i> v. <i>Princess Anne,</i> <span class="citation" data-id="9423852"><a href="/opinion/107801/carroll-v-president-commissioners-of-princess-anne/" aria-description="Citation for case: Carroll v. President &amp; Commissioners of Princess Anne">393 U. S. 175</a></span>; <i>Freedman</i> v. <i>Maryland,</i> <span class="citation" data-id="9422964"><a href="/opinion/106987/freedman-v-maryland/" aria-description="Citation for case: Freedman v. Maryland">380 U. S. 51</a></span>. Cf. <i>Roaden</i> v. <i>Kentucky,</i> <span class="citation" data-id="9425416"><a href="/opinion/108854/roaden-v-kentucky/" aria-description="Citation for case: Roaden v. Kentucky">413 U. S. 496</a></span>; <i>A Quantity of Books</i> v. <i>Kansas,</i> <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span>; <i>Marcus</i> v. <i>Search Warrant,</i> <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>.</p>
<p>[1]  "Papers are the owner's goods and chattels: they are his dearest property; and are so far from enduring a seizure, that they will hardly bear an inspection; and though the eye cannot by the laws of England be guilty of a trespass, yet where private papers are removed and carried away, the secret nature of those goods will be an aggravation of the trespass, and demand more considerable damages in that respect. Where is the written law that gives any magistrate such a power? I can safely answer, there is none; and therefore it is too much for us without such authority to pronounce a practice legal, which would be subversive of all the comforts of society." <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 1066 (1765).</p>
<p>[2]  "Obviously, those who wrote this Fourth Amendment knew from experience that searches and seizures were too valuable to law enforcement to prohibit them entirely, but also knew at the same time that while searches or seizures must not be stopped, they should be slowed down, and warrants should be issued only after studied caution. This accounts for use of the imprecise and flexible term, `unreasonable,' the key word permeating this whole Amendment. Also it is noticeable that this Amendment contains no appropriate language, as does the Fifth, to forbid the use and introduction of search and seizure evidence even though secured `unreasonably.' Nor does this Fourth Amendment attempt to describe with precision what was meant by its words, `probable cause'; nor by whom the `Oath or affirmation' should be taken; nor what it need contain." <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#75" aria-description="Citation for case: Berger v. New York">388 U. S. 41, 75</a></span> (Black, J., dissenting).</p>
<p>[3]  <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/#69" aria-description="Citation for case: Berger v. New York"><i>Id.,</i> at 69</a></span> (STEWART, J., concurring in result).</p>
<p>[4]  It was stated in 1967 that about 95% of the search warrants obtained by the office of the District Attorney for New York County were for the purpose of seizing narcotics and arresting the possessors. See T. Taylor, Two Studies in Constitutional Interpretation 48, and n. 85 (1969).</p>
<p>[5]  Until 1967, when <i>Warden</i> v. <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> was decided, our cases interpreting the Fourth Amendment had drawn a "`distinction between merely evidentiary materials, on the one hand, which may not be seized either under the authority of a search warrant or during the course of a search incident to arrest, and on the other hand, those objects which may validly be seized including the instrumentalities and means by which a crime is committed, the fruits of crime such as stolen property, weapons by which escape of the person arrested might be effected, and property the possession of which is a crime.'" See <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#295" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 295-296</a></span>, quoting from <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 154</a></span>.</p>
<p>[6]  The suggestion that, instead of setting standards, we should rely on the good judgment of the magistrate to prevent abuse represents an abdication of the responsibilities this Court previously accepted in carefully supervising the performance of the magistrate's warrant-issuing function. See <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 111</a></span>.</p>
<p>[7]  "There are three considerations which support the conclusion that private papers are central to the concerns of the fourth amendment and which suggest that, in accord with the amendment's privacy rationale, private papers should occupy a type of preferred position. The first consideration is the very personal, private nature of such papers. This rationale has been cogently articulated on a number of occasions. Private papers have been said to be `little more than an extension of [the owner's] person,' their seizure `a particularly abrasive infringement of privacy,' and their protection `impelled by the moral and symbolic need to recognize and defend the private aspect of personality.' In this sense, every governmental procurement of private papers, regardless of how it is accomplished, is uniquely intrusive. In addition to the nature of the papers themselves, a second reason for according them strict protection concerns the nature of the search for private papers. The fundamental evil at which the fourth amendment was directed was the sweeping, exploratory search conducted pursuant to a general warrant. A search involving private papers, it has been noted, invariably partakes of a similar generality, for `even a search for a specific, identified paper may involve the same rude intrusion [of an exploratory search] if the quest for it leads to an examination of all of a man's private papers.' Thus, both their contents and the inherently intrusive nature of a search for them militates toward the position that private papers are deserving of the fullest possible fourth amendment protection. Finally, not only is a search involving private papers highly intrusive in fourth amendment terms, but the nature of the papers themselves may implicate the policies of other constitutional protections. In addition to the `intimate' relation with fifth amendment values, the obtaining of private papers by the government touches upon the first amendment and the generalized right of privacy." McKenna, The Constitutional Protection of Private Papers: The Role of a Hierarchical Fourth Amendment, 53 Ind. L. J. 55, 68-69 (1977-1978) (footnotes omitted).</p>
<p>[8]  "Whether the search be for rubbish or narcotics, both innocent and guilty will suffer the loss of the proprietary right of privacy. The search for evidence of crime, however, threatens the innocent with an injury not recognized in the cases. That is the damage to reputation resulting from an overt manifestation of official suspicion of crime. Connected with loss of reputation, standing, or credit may be humiliation and other mental suffering. The interests here at stake are the same which are recognized in the common law actions for defamation and malicious prosecution. Indeed, the loss of reputation and the humiliation resulting from the search of one's home for evidence of a heinous crime may greatly exceed the injury caused by an ill-grounded prosecution for a minor offense." Comment, Search and Seizure in the Supreme Court: Shadows on the Fourth Amendment, <span class="citation no-link">28 U. Chi. L. Rev. 664</span>, 701 (1961) (footnotes omitted).</p>
<p>[9]  Only with great reluctance has this Court approved the seizure even of refrigerators or washing machines without notice and a prior adversary hearing; in doing so, the Court has relied on the distinction between loss of property, which can often be easily compensated, and loss of less tangible but more precious rights: "`[w]here only property rights are involved, mere postponement of the judicial enquiry is not a denial of due process.'" <i>Mitchell</i> v. <i>W. T. Grant Co.,</i> <span class="citation" data-id="9425706"><a href="/opinion/109023/mitchell-v-w-t-grant-co/#611" aria-description="Citation for case: Mitchell v. W. T. Grant Co.">416 U. S. 600, 611</a></span>, quoting from <i>Phillips</i> v. <i>Commissioner,</i> <span class="citation" data-id="101764"><a href="/opinion/101764/phillips-v-commissioner/#596" aria-description="Citation for case: Phillips v. Commissioner">283 U. S. 589, 596-597</a></span>. See also <i>Michigan</i> v. <i>Tyler, ante,</i> at 514 (opinion of STEVENS, J.).</p>
<p>[10]  Even before <i><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">Hayden</a></span></i> had repudiated the mere-evidence rule, scholars had recognized that such a change in the scope of the prosecutor's search authority would require a fresh examination of the probable-cause requirement. It was noted that the personal character of some evidentiary documents would "justify stringent limitation, if not total prohibition, of their seizure by exercise of official authority." Taylor, <i>supra,</i> n. 4, at 66.
</p>
<p>It is ironic that the Court today should adopt a rigid interpretation of the Warrant Clause to uphold this search when the Court was prepared only a few years ago to rely on the flexibility of the Clause to create an entirely new warrant in order to preserve the government's power to conduct unannounced inspections of citizens' homes and businesses. See <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535</a></span>, and 538.</p>
<p>[11]  "There must, of course, be a nexusautomatically provided in the case of fruits, instrumentalities or contrabandbetween the item to be seized and criminal behavior. Thus in the case of `mere evidence,' probable cause must be examined in terms of cause to believe that the evidence sought will aid in a particular apprehension or conviction. In so doing, consideration of police purposes will be required." 387 U. S., at 307.</p>
<p>[12]  "The danger is all too obvious that a criminal will destroy or hide evidence or fruits of his crime if given any prior notice." <i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#93" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 93-94, n. 30</a></span>.</p>
<p>[13]  Cf. <i>Marshall</i> v. <i>Barlow's, Inc., ante,</i> at 336-339, and nn. 9-11 (STEVENS, J., dissenting).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/addington-v-texas--110067.json  (`lake-record`, 2 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cf064c0d9f831678", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "addington-v-texas--110067"}, "payload": {"all": [{"cite": "441 U.S. 418", "page": "418", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "441"}, {"cite": "99 S. Ct. 1804", "page": "1804", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "60 L. Ed. 2d 323", "page": "323", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "60"}, {"cite": "1979 U.S. LEXIS 93", "page": "93", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": null, "official": null, "official_selection_present": false, "record_id": "addington-v-texas--110067"}}
{"assertion_id": "a1d7c7830aec6354", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "addington-v-texas--110067"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "addington-v-texas--110067", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — addington-v-texas--110067

```json
{
  "schema_version": "s2.v1",
  "record_id": "addington-v-texas--110067",
  "stub": true,
  "status": "verified_identity",
  "identity": {
    "case_name": "Addington v. Texas",
    "case_name_short": "Addington",
    "case_name_full": "Addington v. Texas",
    "input_case_name": "Addington v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-04-30",
    "year": 1979,
    "docket": null,
    "cluster_id": 110067,
    "lead_opinion_id": 110067,
    "sibling_ids": [],
    "absolute_url": "/opinion/110067/addington-v-texas/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "441 U.S. 418",
        "volume": "441",
        "reporter": "U.S.",
        "page": "418",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1804",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 323",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "323",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 93",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "93",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 418",
        "volume": "441",
        "reporter": "U.S.",
        "page": "418",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1804",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1804",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 323",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "323",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 93",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "93",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "other",
      "selected": null,
      "reason": "unlisted_reporter:U.S."
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
    "date_created": "2026-07-06T13:52:56Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:53:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:53:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:53:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — addington-v-texas--110067

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b477-11">
  Me. Chief Justice Burgee
 </author>
<p id="AYL">
  delivered the opinion of the Court.
 </p>
<p id="b477-12">
  The question in this case is what standard of proof is required by the Fourteenth Amendment to the Constitution in a civil proceeding brought under state law to commit an
  <span citation-index="1" class="star-pagination" label="420"> 
   *420
   </span>
  individual involuntarily for an indefinite period to a state mental hospital.
 </p>
<p id="b478-5">
  I
 </p>
<p id="b478-6">
  On seven occasions between 1969 and 1975, appellant was committed temporarily, Tex. Rev. Civ. Stat. Ann., Arts. 5547-31 to 5547-39 (Vernon 1958 and Supp. 1978-1979), to various Texas state mental hospitals and was committed for indefinite periods, Arts. 5547-40 to 5547-57, to Austin State Hospital on three different occasions. On December 18, 1975, when appellant was arrested on a misdemeanor charge of “assault by threat” against his mother, the county and state mental health authorities therefore were well aware of his history of mental and emotional difficulties.
 </p>
<p id="b478-7">
  Appellant’s mother filed a petition for his indefinite commitment in accordance with Texas law. The county psychiatric examiner interviewed appellant while in custody and after the interview issued a Certificate of Medical Examination for Mental Illness. In the certificate, the examiner stated his opinion that appellant was “mentally ill and require [d] hospitalization in a mental hospital.” Art. 5547-42 (Vernon 1958).
 </p>
<p id="b478-8">
  Appellant retained counsel and a trial was held before a jury to determine in accord with the statute:
 </p>
<blockquote id="b478-9">
  “(1) whether the proposed patient is mentally ill, and if so
 </blockquote>
<blockquote id="b478-10">
  “(2) whether he requires hospitalization in a mental hospital for his own welfare and protection or the protection of others, and if so
 </blockquote>
<blockquote id="b478-11">
  “(3) whether he is mentally incompetent.” Art. 5547-51 (Vernon 1958).
 </blockquote>
<p id="b478-12">
  The trial on these issues extended over six days.
 </p>
<p id="b478-13">
  The State offered evidence that appellant suffered from serious delusions, that he often had threatened to injure both of his parents and others, that he had been involved in several
  <span citation-index="1" class="star-pagination" label="421"> 
   *421
   </span>
  assaultive episodes while hospitalized and that he had caused substantial property damage both at his own apartment and at his parents’ home. From these undisputed facts, two psychiatrists, who qualified as experts, expressed opinions that appellant suffered from psychotic schizophrenia and that he had paranoid tendencies. They also expressed medical opinions that appellant was probably dangerous both to himself and to others. They explained that appellant required hospitalization in a closed area to treat his condition because in the past he had refused to attend outpatient treatment programs and had escaped several times from mental hospitals.
 </p>
<p id="b479-5">
  Appellant did not contest the factual assertions made by the State’s witnesses; indeed, he conceded that he suffered from a mental illness. What appellant attempted to show was that there was no substantial basis for concluding that he was probably dangerous to himself or others.
 </p>
<p id="b479-6">
  The trial judge submitted the case to the jury with the instructions in the form of two questions:
 </p>
<blockquote id="b479-7">
  “1. Based on clear, unequivocal and convincing evidence, is Frank O’Neal Addington mentally ill?
 </blockquote>
<blockquote id="b479-8">
<em>
   “2.
  </em>
  Based on clear, unequivocal and convincing evidence, does Frank O’Neal Addington require hospitalization in a mental hospital for his own welfare and protection or the protection of others?”
 </blockquote>
<p id="b479-9">
  Appellant objected to these instructions on several grounds, including the trial court’s refusal to employ the “beyond a reasonable doubt” standard of proof.
 </p>
<p id="b479-10">
  The jury found that appellant was mentally ill and that he required hospitalization for his own or others’ welfare. The trial court then entered an order committing appellant as a patient to Austin State Hospital for an indefinite period.
 </p>
<p id="b479-11">
  Appellant appealed that order to the Texas Court of Civil Appeals, arguing, among other things, that the standards for commitment violated his substantive due process rights and that any standard of proof for commitment less than that
  <span citation-index="1" class="star-pagination" label="422"> 
   *422
   </span>
  required for criminal convictions,
  <em>
   i. e.,
  </em>
  beyond a reasonable doubt, violated his procedural due process rights. The Court of Civil Appeals agreed with appellant on the standard-of-proof issue and reversed the judgment of the trial court. Because of its treatment of the standard of proof, that court did not consider any of the other issues raised in the appeal.
 </p>
<p id="b480-5">
  On appeal, the Texas Supreme Court reversed the Court of Civil Appeals’ decision. <span class="citation" data-id="1737608"><a href="/opinion/1737608/state-v-addington/" aria-description="Citation for case: State v. Addington">557 S. W. 2d 511</a></span>. In so holding the Supreme Court relied primarily upon its previous decision in
  <em>
   State
  </em>
  v.
  <em>
   Turner,
  </em>
  <span class="citation" data-id="1794082"><a href="/opinion/1794082/state-v-turner/" aria-description="Citation for case: State v. Turner">556 S. W. 2d 563</a></span> (1977), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./435/929/">435 U. S. 929</a></span> (1978).
 </p>
<p id="b480-6">
  In
  <em>
   <span class="citation" data-id="1794082"><a href="/opinion/1794082/state-v-turner/" aria-description="Citation for case: State v. Turner">Turner</a></span>,
  </em>
  the Texas Supreme Court held that a “preponderance of the evidence” standard of proof in a civil commitment proceeding satisfied due process. The court declined to adopt the criminal law standard of “beyond a reasonable doubt” primarily because it questioned whether the State could prove by that exacting standard that a particular person would or would not be dangerous in the future. It also distinguished a civil commitment from a criminal conviction by noting that under Texas law the mentally ill patient has the right to treatment, periodic review of his condition, and immediate release when no longer deemed to be a danger to himself or others. Finally, the
  <em>
   <span class="citation" data-id="1794082"><a href="/opinion/1794082/state-v-turner/" aria-description="Citation for case: State v. Turner">Turner</a></span>
  </em>
  court rejected the “clear and convincing” evidence standard because under Texas rules of procedure juries could be instructed only under a beyond-a-reasonable-doubt or a preponderance standard of proof.
 </p>
<p id="b480-7">
  Reaffirming
  <em>
   <span class="citation" data-id="1794082"><a href="/opinion/1794082/state-v-turner/" aria-description="Citation for case: State v. Turner">Turner</a></span>,
  </em>
  the Texas Supreme Court in this case concluded that the trial court’s instruction to the jury, although not in conformity with the legal requirements, had benefited appellant, and hence the error was harmless. Accordingly, the court reinstated the judgment of the trial court.
 </p>
<p id="b480-8">
  We noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./435/967/">435 U. S. 967</a></span>. After oral argument it became clear that no challenge to the constitutionality of any Texas statute was presented. Under <span class="citation no-link">28 U. S. C. § 1257</span> (2) no appeal is authorized; accordingly, con
  <span citation-index="1" class="star-pagination" label="423"> 
   *423
   </span>
  struing the papers filed as a petition for a writ of certiorari, we now grant the petition.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
</p>
<p id="b481-5">
  II
 </p>
<p id="b481-6">
  The function of a standard of proof, as that concept is embodied in the Due Process Clause and in the realm of factfinding, is to “instruct the factfinder concerning the degree of confidence our society thinks he should have in the correctness of factual conclusions for a particular type of adjudication.”
  <em>
   In re Winship,
  </em>
  <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#370" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358, 370</a></span> (1970) (Harlan, J., concurring). The standard serves to allocate the risk of error between the litigants and to indicate the relative importance attached to the ultimate decision.
 </p>
<p id="b481-7">
  Generally speaking, the evolution of this area of the law has produced across a continuum three standards or levels of proof for different types of cases. At one end of the spectrum is the typical civil case involving a monetary dispute between private parties. Since society has a minimal concern with the outcome of such private suits, plaintiff’s burden of proof is a mere preponderance of the evidence. The litigants thus share the risk of error in roughly equal fashion.
 </p>
<p id="b481-8">
  In a criminal case, on the other hand, the interests of the defendant are of such magnitude that historically and without any explicit constitutional requirement they have been protected by standards of proof designed to exclude as nearly as possible the likelihood of an erroneous judgment.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  In the
  <span citation-index="1" class="star-pagination" label="424"> 
   *424
   </span>
  administration of criminal justice, our society imposes almost the entire risk of error upon itself. This is accomplished by requiring under the Due Process Clause that the state prove the guilt of an accused beyond a reasonable doubt.
  <em>
   In re Winship, supra.
  </em>
</p>
<p id="b482-5">
  The intermediate standard, which usually employs some combination of the words "clear,” "cogent,” “unequivocal” and “convincing,” is less commonly used, but nonetheless “is no stranger to the civil law.”
  <em>
   Woodby
  </em>
  v.
  <em>
   INS,
  </em>
  <span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/#285" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">385 U. S. 276, 285</a></span> (1966). See also C. McCormick, Evidence § 320 (1954); 9 J. Wigmore, Evidence § 2498 (3d ed. 1940). One typical use of the standard is in civil cases involving allegations of fraud or some other quasi-criminal wrongdoing by the defendant. The interests at stake in those cases are deemed to be more substantial than mere loss of money and some jurisdictions accordingly reduce the risk to the defendant of having his reputation tarnished erroneously by increasing the plaintiff’s burden of proof. Similarly, this Court has used the “clear, unequivocal and convincing” standard of proof to protect particularly important individual interests in various civil cases. See,
  <em>
   e. g.; Woodby
  </em>
  v.
  <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#285" aria-description="Citation for case: In Re WINSHIP"><em>
   INS, supra,
  </em>
  at 285</a></span> (deportation);
  <em>
   Chaunt
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422072"><a href="/opinion/106128/chaunt-v-united-states/#353" aria-description="Citation for case: Chaunt v. United States">364 U. S. 350, 353</a></span> (1960) (denaturalization) ;
  <em>
   Schneiderman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9419390"><a href="/opinion/103877/schneiderman-v-united-states/#125" aria-description="Citation for case: Schneiderman v. United States">320 U. S. 118, 125, 159</a></span> (1943) (denaturalization).
 </p>
<p id="b482-6">
  Candor suggests that, to a degree, efforts to analyze what lay jurors understand concerning the differences among these three tests or the nuances of a judge’s instructions on the law may well be largely an academic exercise; there are no directly relevant empirical studies.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Indeed, the ultimate truth as to how the standards of proof affect decisionmaking may well be
  <span citation-index="1" class="star-pagination" label="425"> 
   *425
   </span>
  unknowable, given that factfinding is a process shared by countless thousands of individuals throughout the country. We probably can assume no more than that the difference between a preponderance of the evidence and proof beyond a reasonable doubt probably is better understood than either of them in relation to the intermediate standard of clear and convincing evidence. Nonetheless, even if the particular standard-of-proof catchwords do not always make a great difference in a particular case, adopting a “standard of proof is more than an empty semantic exercise.”
  <em>
   Tippett
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="8884420"><a href="/opinion/8897758/tippett-v-maryland/#1166" aria-description="Citation for case: Tippett v. Maryland">436 F. 2d 1153, 1166</a></span> (CA4 1971) (Sobeloff, J., concurring in part and dissenting in part), cert, dismissed
  <em>
   sub nom. Murel
  </em>
  v.
  <em>
   Baltimore City Criminal Court,
  </em>
  <span class="citation" data-id="9424955"><a href="/opinion/108583/murel-v-baltimore-city-criminal-court/" aria-description="Citation for case: Murel v. Baltimore City Criminal Court">407 U. S. 355</a></span> (1972). In cases involving individual rights, whether criminal or civil, “[t]he standard of proof [at a minimum] reflects the value society places on individual liberty.” <span class="citation" data-id="8884420"><a href="/opinion/8897758/tippett-v-maryland/#1166" aria-description="Citation for case: Tippett v. Maryland">436 F. 2d, at 1166</a></span>.
 </p>
<p id="b483-5">
  Ill
 </p>
<p id="b483-6">
  In considering what standard should govern in a civil commitment proceeding, we must assess both the extent of the individual’s interest in not being involuntarily confined indefinitely and the state’s interest in committing the emotionally disturbed under a particular standard of proof. Moreover, we must be mindful that the function of legal process is to minimize the risk of erroneous decisions. See
  <em>
   Mathews
  </em>
  v.
  <em>
   Eldridge,
  </em>
  <span class="citation" data-id="9426279"><a href="/opinion/109382/mathews-v-eldridge/#335" aria-description="Citation for case: Mathews v. Eldridge">424 U. S. 319, 335</a></span> (1976);
  <em>
   Speiser
  </em>
  v.
  <em>
   Randall,
  </em>
  <span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525-526</a></span> (1958).
 </p>
<p id="b483-7">
  A
 </p>
<p id="b483-8">
  This Court repeatedly has recognized that civil commitment for any purpose constitutes a significant deprivation of liberty that requires due process protection. See,
  <em>
   e. g., Jackson
  </em>
  v.
  <em>
   Indiana,
  </em>
  <span class="citation" data-id="108556"><a href="/opinion/108556/jackson-v-indiana/" aria-description="Citation for case: Jackson v. Indiana">406 U. S. 715</a></span> (1972);
  <em>
   Humphrey
  </em>
  v.
  <em>
   Cady,
  </em>
  <span class="citation" data-id="108491"><a href="/opinion/108491/humphrey-v-cady/" aria-description="Citation for case: Humphrey v. Cady">405 U. S. 504</a></span> (1972);
  <em>
   In re Gault,
  </em>
  <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">387 U. S. 1</a></span> (1967);
  <em>
   Specht
  </em>
  v.
  <em>
   Patterson,
  </em>
  <span class="citation" data-id="107413"><a href="/opinion/107413/specht-v-patterson/" aria-description="Citation for case: Specht v. Patterson">386 U. S. 605</a></span> (1967). Moreover, it is indisputable that involuntary commitment to a mental hospital after a finding
  <span citation-index="1" class="star-pagination" label="426"> 
   *426
   </span>
  of probable dangerousness to self or others can engender adverse social consequences to the individual. Whether we label this phenomena “stigma” or choose to call it something else is less important than that we recognize that it can occur and that it can have a very significant impact on the individual.
 </p>
<p id="b484-5">
  The state has a legitimate interest under its
  <em>
   parens patriae
  </em>
  powers in providing care to its citizens who are unable because of emotional disorders to care for themselves; the state also has authority under its police power to protect the community from the dangerous tendencies of some who are mentally ill. Under the Texas Mental Health Code, however, the State has no interest in confining individuals involuntarily if they are not mentally ill or if they do not pose some danger to themselves or others. Since the preponderance standard creates the risk of increasing the number of individuals erroneously committed, it is at least unclear to what extent, if any, the state’s interests are furthered by using a preponderance standard in such commitment proceedings.
 </p>
<p id="b484-6">
  The expanding concern of society with problems of mental disorders is reflected in the fact that in recent years many states have enacted statutes designed to protect the rights of the mentally ill. However, only one state by statute permits involuntary commitment by a mere preponderance of the evidence, <span class="citation no-link">Miss. Code Ann. § 41-21-75</span> (1978 Supp.), and Texas is the only state where a court has concluded that the preponderance-of-the-evidence standard satisfies due process. We attribute this not to any lack of concern in those states, but rather to a belief that the varying standards tend to produce comparable results. As we noted earlier, however, standards of proof are important for their symbolic meaning as well as for their practical effect.
 </p>
<p id="b484-7">
  At one time or another every person exhibits some abnormal behavior which might be perceived by some as symptomatic of a mental or emotional disorder, but which is in fact within
  <span citation-index="1" class="star-pagination" label="427"> 
   *427
   </span>
  a range of conduct that is generally acceptable. Obviously, such behavior is no basis for compelled treatment and surely none for confinement. However, there is the possible risk that a factfinder might decide to commit an individual based solely on a few isolated instances of unusual conduct. Loss of liberty calls for a showing that the individual suffers from something more serious than is demonstrated by idiosyncratic behavior. Increasing the burden of proof is one way to impress the factfinder with the importance of the decision and thereby perhaps to reduce the chances that inappropriate commitments will be ordered.
 </p>
<p id="b485-4">
  The individual should not be asked to share equally with society the risk of error when the possible injury to the individual is significantly greater than any possible harm to the state. We conclude that the individual’s interest in the outcome of a civil commitment proceeding is of such weight and gravity that due process requires the state to justify confinement by proof more substantial than a mere preponderance of the evidence.
 </p>
<p id="b485-5">
  B
 </p>
<p id="b485-6">
  Appellant urges the Court to hold that due process requires use of the criminal law’s standard of proof — “beyond a reasonable doubt.” He argues that the rationale of the
  <em>
   <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span>
  </em>
  holding that the criminal law standard of proof was required in a delinquency proceeding applies with equal force to a civil commitment proceeding.
 </p>
<p id="b485-7">
  In
  <em>
   <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span>,
  </em>
  against the background of a gradual assimilation of juvenile proceedings into traditional criminal prosecutions, we declined to allow the state’s “civil labels and good intentions” to “obviate the need for criminal due process safeguards in juvenile courts.” <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#365" aria-description="Citation for case: In Re WINSHIP">397 U. S., at 365-366</a></span>. The Court saw no controlling difference in loss of liberty and stigma between a conviction for an adult and a delinquency adjudication for a juvenile.
  <em>
   <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span>
  </em>
  recognized that the basic issue— whether the individual in fact committed a criminal act — was
  <span citation-index="1" class="star-pagination" label="428"> 
   *428
   </span>
  the same in both proceedings. There being no meaningful distinctions between the two proceedings, we required the state to prove the juvenile’s act and intent beyond a reasonable doubt.
 </p>
<p id="b486-5">
  There are significant reasons why different standards of proof are called for in civil commitment proceedings as opposed to criminal prosecutions. In a civil commitment state power is not exercised in a punitive sense.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Unlike the delinquency proceeding in
  <em>
   <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">Winship</a></span>,
  </em>
  a civil commitment proceeding can in no sense be equated to a criminal prosecution. Cf.
  <em>
   Woodby
  </em>
  v.
  <em>
   INS,
  </em>
  <span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/#284" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">385 U. S., at 284-285</a></span>.
 </p>
<p id="b486-6">
  In addition, the “beyond a reasonable doubt” standard historically has been reserved for criminal cases. This unique standard of proof, not prescribed or defined in the Constitution, is regarded as a critical part of the “moral force of the criminal law,”
  <em>
   In re Winship,
  </em>
  <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP">397 U. S., at 364</a></span>, and we should hesitate to apply it too broadly or casually in noncriminal cases. Cf.
  <em>
   <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">ibid.</a></span>
  </em>
</p>
<p id="b486-7">
  The heavy standard applied in criminal cases manifests our concern that the risk of error to the individual must be minimized even at the risk that some who are guilty might go free.
  <em>
   Patterson
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9426883"><a href="/opinion/109698/patterson-v-new-york/#208" aria-description="Citation for case: Patterson v. New York">432 U. S. 197, 208</a></span> (1977). The full force of that idea does not apply to a civil commitment. It may be true that an erroneous commitment is sometimes as undesirable as an erroneous conviction, 5 J. Wigmore, Evidence § 1400 (Chadboum rev. 1974). However, even though an erroneous confinement should be avoided in the first instance, the layers of professional review and observation of the patient’s condition, and the concern of family and
  <span citation-index="1" class="star-pagination" label="429"> 
   *429
   </span>
  friends generally will provide continuous opportunities for an erroneous commitment to be corrected. Moreover, it is not true that the release of a genuinely mentally ill person is no worse for the individual than the failure to convict the guilty. One who is suffering from a debilitating mental illness and in need of treatment is neither wholly at liberty nor free of stigma. See Chodoff, The Case for Involuntary Hospitalization of the Mentally Ill, 133 Am. J. Psychiatry 496, 498 (1976); Schwartz, Myers, &amp; Astrachan, Psychiatric Labeling and the Rehabilitation of the Mental Patient, 31 Arch. Gen. Psychiatry 329, 334 (1974). It cannot be said, therefore, that it is much better for a mentally ill person to “go free” than for a mentally normal person to be committed.
 </p>
<p id="b487-5">
  Finally, the initial inquiry in a civil commitment proceeding is very different from the central issue in either a delinquency proceeding or a criminal prosecution. In the latter cases the basic issue is a straightforward factual question — did the accused commit the act alleged? There may be factual issues to resolve in a commitment proceeding, but the factual aspects represent only the beginning of the inquiry. Whether the individual is mentally ill and dangerous to either himself or others and is in need of confined therapy turns on the
  <em>
   meaning
  </em>
  of the facts which must be interpreted by expert psychiatrists and psychologists. Given the lack of certainty and the fallibility of psychiatric diagnosis, there is a serious question as to whether a state could ever prove beyond a reasonable doubt that an individual is both mentally ill and likely to be dangerous. See
  <em>
   O’Connor
  </em>
  v.
  <em>
   Donaldson,
  </em>
  <span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/#584" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563, 584</a></span> (1975) (concurring
  <em>
   opinion); Blocker
  </em>
  v.
  <em>
   United States,
  </em>
  110 U. S. App. D. C. 41, 48-49, <span class="citation" data-id="9447847"><a href="/opinion/253629/comer-blocker-v-united-states/#860" aria-description="Citation for case: Comer Blocker v. United States">288 F. 2d 853, 860-861</a></span> (1961) (opinion concurring in result). See also
  <em>
   Tippett
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="8884420"><a href="/opinion/8897758/tippett-v-maryland/#1165" aria-description="Citation for case: Tippett v. Maryland">436 F. 2d, at 1165</a></span> (Sobeloff, J., concurring in part and dissenting in part); Note, Civil Commitment of the Mentally Ill: Theories and Procedures, <span class="citation no-link">79 Harv. L. Rev. 1288</span>, 1291 (1966); Note, Due Process and the Development of “Criminal” Safeguards
  <span citation-index="1" class="star-pagination" label="430"> 
   *430
   </span>
  in Civil Commitment Adjudications, 42 Ford. L. Rev. 611, 624 (1974).
 </p>
<p id="b488-4">
  The subtleties and nuances of psychiatric diagnosis render certainties virtually beyond reach in most situations. The reasonable-doubt standard of criminal law functions in its realm because there the standard is addressed to specific, knowable facts. Psychiatric diagnosis, in contrast, is to a large extent based on medical “impressions” drawn from subjective analysis and filtered through the experience of the diagnostician. This process often makes it very difficult for the expert physician to offer definite conclusions about any particular patient. Within the medical discipline, the traditional standard for “factfinding” is a “reasonable medical certainty.” If a trained psychiatrist has difficulty with the categorical “beyond a reasonable doubt” standard, the untrained lay juror — or indeed even a trained judge — who is required to rely upon expert opinion could be forced by the criminal law standard of proof to reject commitment for many patients desperately in need of institutionalized psychiatric care. See
  <em>
   <span class="citation no-link">ibid.</span>
  </em>
  Such “freedom” for a mentally ill person would be purchased at a high price.
 </p>
<p id="b488-5">
  That practical considerations may limit a constitutionally based burden of proof is demonstrated by the reasonable-doubt standard, which is a compromise between what is possible to prove and what protects the rights of the individual. If the state was required to guarantee error-free convictions, it would be required to prove guilt beyond all doubt. However, “[d]ue process does not require that every conceivable step be taken, at whatever cost, to eliminate the possibility of convicting an innocent person.”
  <em>
   Patterson
  </em>
  v.
  <span class="citation" data-id="9426883"><a href="/opinion/109698/patterson-v-new-york/#208" aria-description="Citation for case: Patterson v. New York"><em>
   New York, supra,
  </em>
  at 208</a></span>. Nor should the state be required to employ a standard of proof that may completely undercut its efforts to further the legitimate interests of both the state and the patient that are served by civil commitments.
 </p>
<p id="b488-6">
  That some states have chosen — either legislatively or judi
  <span citation-index="1" class="star-pagination" label="431"> 
   *431
   </span>
  cially — to adopt the criminal law standard
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  gives no assurance that the more stringent standard of proof is needed or is even adaptable to the needs of all states. The essence of federalism is that states must be free to develop a variety of solutions to problems and not be forced into a common, uniform mold. As the substantive standards for civil commitment may vary from state to state, procedures must be allowed to vary so long as they meet the constitutional minimum. See Monahan &amp; Wexler, A Definite Maybe: Proof and Probability in Civil Commitment, 2 Law
  <em>
   &amp;
  </em>
  Human Behavior 37, 41-42 (1978); Share, The Standard of Proof in Involuntary Civil Commitment Proceedings, 1977 Detroit College L. Rev. 209, 210. We conclude that it is unnecessary to require states to apply the strict, criminal standard.
 </p>
<p id="b489-5">
  C
 </p>
<p id="b489-6">
  Having concluded that the preponderance standard falls short of meeting the demands of due process and that the reasonable-doubt standard is not required, we turn to a middle level of burden of proof that strikes a fair balance between the rights of the individual and the legitimate concerns of the state. We note that 20 states, most by statute, employ the standard of “clear and convincing” evidence;
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  3 states use
  <span citation-index="1" class="star-pagination" label="432"> 
   *432
   </span>
  “clear,
  <em>
   cogent,
  </em>
  and convincing” evidence;
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  and 2 states require “clear,
  <em>
   unequivocal
  </em>
  and convincing” evidence.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
</p>
<p id="b490-5">
  In
  <em>
   Woodby
  </em>
  v.
  <em>
   INS,
  </em>
  <span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">385 U. S. 276</a></span> (1966), dealing with deportation, and
  <em>
   Schneiderman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9419390"><a href="/opinion/103877/schneiderman-v-united-states/#125" aria-description="Citation for case: Schneiderman v. United States">320 U. S., at 125, 159</a></span>, dealing with denaturalization, the Court held that “clear, unequivocal, and convincing” evidence was the appropriate standard of proof. The term “unequivocal,” taken by itself, means proof that admits of no doubt,
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  a burden approximating, if not exceeding, that used in criminal cases. The issues in
  <em>
   <span class="citation" data-id="9419390"><a href="/opinion/103877/schneiderman-v-united-states/" aria-description="Citation for case: Schneiderman v. United States">Schneiderman</a></span>
  </em>
  and
  <em>
   <span class="citation" data-id="9423303"><a href="/opinion/107317/woodby-v-immigration-naturalization-service/" aria-description="Citation for case: Woodby v. Immigration &amp; Naturalization Service">Woodby</a></span>
  </em>
  were basically factual and therefore susceptible of objective proof and the consequences to the individual were unusually drastic — loss of citizenship and expulsion from the United States.
 </p>
<p id="b490-6">
  We have concluded that the reasonable-doubt standard is inappropriate in civil commitment proceedings because, given the uncertainties of psychiatric diagnosis, it may impose a burden the state cannot meet and thereby erect an unreasonable barrier to needed medical treatment. Similarly, we conclude that use of the term “unequivocal” is not constitutionally required, although the states are free to use that standard. To meet due process demands, the standard has to
  <span citation-index="1" class="star-pagination" label="433"> 
   *433
   </span>
  inform the factfinder that the proof must be greater than the preponderance-of-the-evidence standard applicable to other categories of civil cases.
 </p>
<p id="b491-5">
  We noted earlier that the trial court employed the standard of “clear, unequivocal and convincing” evidence in appellant’s commitment hearing before a jury. That instruction was constitutionally adequate. However, determination of the precise burden equal to or greater than the “clear and convincing” standard which we hold is required to meet due process guarantees is a matter of state law which we leave to the Texas Supreme Court.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  Accordingly, we remand the case for further proceedings not inconsistent with this opinion.
 </p>
<p id="b491-6">
<em>
   Vacated and remanded.
  </em>
</p>
<judges id="b491-7">
  Mr. Justice Powell took no part in the consideration or decision of this case.
 </judges>










<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b481-9">
   See
   <em>
    Kulko
   </em>
   v.
   <em>
    California Superior Court,
   </em>
   <span class="citation" data-id="9427178"><a href="/opinion/109858/kulko-v-superior-court-of-cal-city-and-county-of-san-francisco/" aria-description="Citation for case: Kulko v. Superior Court of Cal., City and County of San...">436 U. S. 84</a></span> (1978);
   <em>
    Hanson
   </em>
   v.
   <em>
    Denckla,
   </em>
   <span class="citation" data-id="9421664"><a href="/opinion/105728/hanson-v-denckla/" aria-description="Citation for case: Hanson v. Denckla">357 U. S. 235</a></span> (1958);
   <em>
    May
   </em>
   v.
   <em>
    Anderson,
   </em>
   <span class="citation" data-id="9420945"><a href="/opinion/105126/may-v-anderson/" aria-description="Citation for case: May v. Anderson">345 U. S. 528</a></span> (1953). As in those cases, we continue to refer to the parties as appellant and appellee. See
   <em>
    Kulko
   </em>
   v.
   <em>
    California Superior Court, supra,
   </em>
   at 90 n. 4.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b481-10">
   Compare Morano, A Reexamination of the Development of the Reasonable Doubt Rule, 55 B. U. L. Rev. 507 (1975) (reasonable doubt represented a less strict standard than previous common-law rules), with May, Some Rules of Evidence, 10 Am. L. Rev. 642 (1875) (reasonable doubt constituted a stricter rule than previous ones). See generally Underwood, The Thumb on the Scales of Justice: Burdens of Persuasion in Criminal Cases, 86 Yale L. J. 1299 (1977).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b482-7">
   There have been some efforts to evaluate the effect of varying standards of proof on jury factfinding, see,
   <em>
    e. g.,
   </em>
   L. S. E. Jury Project, Juries and the Rules of Evidence, <span class="citation no-link">1973 Crim. L. Rev. 208</span>, but we have found no study comparing all three standards of proof to determine how juries, real or mock, apply them.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b486-8">
   The State of Texas confines only for the purpose of providing care designed to treat the individual. As the Texas Supreme Court said in
   <em>
    State
   </em>
   v.
   <em>
    Turner,
   </em>
   <span class="citation" data-id="1794082"><a href="/opinion/1794082/state-v-turner/#566" aria-description="Citation for case: State v. Turner">556 S. W. 2d 563, 566</a></span> (1977):
  </p>
<blockquote id="b486-9">
   “The involuntary mental patient is entitled to treatment, to periodic and recurrent review of his mental condition, and to release at such time as he no longer presents a danger to himself or others.”
  </blockquote>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b489-7">
   <span class="citation no-link">Haw. Rev. Stat. § 334-60</span> (b) (4) (I) (Supp. 1978); <span class="citation no-link">Idaho Code § 66-329</span> (i) (Supp. 1978); <span class="citation no-link">Kan. Stat. Ann. §59-2917</span> (1976); Mont. Rev. Codes Ann. § 38-1305 (7) (Supp. 1977); Okla. Stat., Tit. 43A, § 54.1 (C) (Supp. 1978); Ore. Rev. Stat. §426.130 (1977); Utah Code Ann. §64r-7-36 (6) (1953); <span class="citation no-link">Wis. Stat. § 51.20</span> (14) (e) (Supp. 1978-1979);
   <em>
    Superintendent of Worcester State Hospital
   </em>
   v.
   <em>
    Hagberg,
   </em>
   <span class="citation" data-id="2052218"><a href="/opinion/2052218/superintendent-of-worcester-state-hospital-v-hagberg/" aria-description="Citation for case: Superintendent of Worcester State Hospital v. Hagberg">374 Mass. 271</a></span>, <span class="citation" data-id="2052218"><a href="/opinion/2052218/superintendent-of-worcester-state-hospital-v-hagberg/" aria-description="Citation for case: Superintendent of Worcester State Hospital v. Hagberg">372 N. E. 2d 242</a></span> (1978);
   <em>
    Proctor
   </em>
   v.
   <em>
    Butler,
   </em>
   117 N. H. 927, <span class="citation" data-id="9652192"><a href="/opinion/1560516/proctor-v-butler/" aria-description="Citation for case: Proctor v. Butler">380 A. 2d 673</a></span> (1977);
   <em>
    In re Hodges,
   </em>
   <span class="citation" data-id="1436331"><a href="/opinion/1436331/in-re-hodges/" aria-description="Citation for case: In Re Hodges">325 A. 2d 605</a></span> (D. C. 1974);
   <em>
    Lausche
   </em>
   v.
   <em>
    Commissioner of Public Welfare,
   </em>
   <span class="citation" data-id="2069358"><a href="/opinion/2069358/lausche-v-commissioner-of-public-welfare/" aria-description="Citation for case: Lausche v. Commissioner of Public Welfare">302 Minn. 65</a></span>, <span class="citation" data-id="2069358"><a href="/opinion/2069358/lausche-v-commissioner-of-public-welfare/" aria-description="Citation for case: Lausche v. Commissioner of Public Welfare">225 N. W. 2d 366</a></span> (1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/993/">420 U. S. 993</a></span> (1975). See also
   <em>
    In re J. W.,
   </em>
   44 N. J. Super. 216, <span class="citation multiple-matches"><a href="/c/A.%202d/130/64/">130 A. 2d 64</a></span> (App. Div.), cert. denied, 24 N. J. 465, <span class="citation multiple-matches"><a href="/c/A.%202d/132/558/">132 A. 2d 558</a></span> (1957);
   <em>
    Denton
   </em>
   v.
   <em>
    Commonwealth,
   </em>
   <span class="citation" data-id="1738737"><a href="/opinion/1738737/denton-v-commonwealth/" aria-description="Citation for case: Denton v. Commonwealth">383 S. W. 2d 681</a></span> (Ky. App. 1964) (dicta).
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b489-8">
   <span class="citation no-link">Ariz. Rev. Stat. Ann. § 36-540</span> (1974); <span class="citation no-link">Colo. Rev. Stat. § 27-10-111</span> (1) (Supp. 1976); <span class="citation no-link">Conn. Gen. Stat. § 17-178</span> (c) (1979); Del. Code Ann., Tit. 16, §5010 (2) (Supp. 1978); Ga. Code §88-501 (u) (1978); Ill. Rev.
   <span citation-index="1" class="star-pagination" label="432"> 
    *432
    </span>
   Stat., ch. 911/2, §3-808 (Supp. 1977); <span class="citation no-link">Iowa Code §229.12</span> (1979); La. Rev. Stat. Ann. §28:55E (West Supp. 1979); Me. Rev. Stat. Ann., Tit. 34, § 2334 (5) (A) (1) (1978); Mich. Stat. Ann. §14.800 (465) (1976); <span class="citation no-link">Neb. Rev. Stat. §83-1035</span> (1976); N. M. Stat. Ann. §43-1-11C (1978); N. D. Cent. Code § 25-03.1-19 (1978); <span class="citation no-link">Ohio Rev. Code Ann. § 5122.15</span> (B) (Supp. 1978); Pa. Stat. Ann., Tit. 50, § 7304 (f) (Purdon Supp. 1978-1979); S. C. Code § 44-17-580 (Supp. 1978); S. D. Comp. Laws Ann. § 27A-9-18 (1977); Vt. Stat. Ann., Tit. 18, §7616 (b) (Supp. 1978); Md. Dept, of Health &amp; Mental Hygiene Reg. 10.21.03G (1973);
   <em>
    In re Beverly,
   </em>
   <span class="citation" data-id="1125652"><a href="/opinion/1125652/in-re-beverly/" aria-description="Citation for case: In Re Beverly">342 So. 2d 481</a></span> (Fla. 1977).
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b490-13">
   N. C. Gen. Stat. § 122-58.7 (i) (Supp. 1977); <span class="citation no-link">Wash. Rev. Code § 71.05.310</span> (1976);
   <em>
    State ex rel. Hawks
   </em>
   v.
   <em>
    Lasaro,
   </em>
   <span class="citation" data-id="1271721"><a href="/opinion/1271721/state-ex-rel-hawks-v-lazaro/" aria-description="Citation for case: State Ex Rel. Hawks v. Lazaro">157 W. Va. 417</a></span>, <span class="citation" data-id="1271721"><a href="/opinion/1271721/state-ex-rel-hawks-v-lazaro/" aria-description="Citation for case: State Ex Rel. Hawks v. Lazaro">202 S. E. 2d 109</a></span> (1974).
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b490-14">
   <span class="citation no-link">Ala. Code § 22-52-10</span> (a) (Supp. 1978); <span class="citation no-link">Tenn. Code Ann. § 33-604</span> (d) (Supp. 1978).
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b490-15">
   See Webster's Third New International Dictionary 2494 (1961).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b491-8">
   We noted earlier the court’s holding on harmless error. See
   <em>
    supra,
   </em>
   at 422.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/alasaad-v-mayorkas--u782a2d04.json  (`lake-record`, 1 assertions)

### content_page

```
[content page unresolved]
```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0578197e1e25e27d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "alasaad-v-mayorkas--u782a2d04"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "alasaad-v-mayorkas--u782a2d04", "scope_note": null, "varies_by_point": false}}
```

### lake record — alasaad-v-mayorkas--u782a2d04

```json
{
  "schema_version": "s2.v1",
  "record_id": "alasaad-v-mayorkas--u782a2d04",
  "stub": true,
  "status": "not_found",
  "identity": {
    "case_name": null,
    "case_name_short": null,
    "case_name_full": null,
    "input_case_name": "Alasaad v. Mayorkas",
    "court": "1st Cir. 2021",
    "court_id": null,
    "court_level": null,
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": null,
    "docket": null,
    "cluster_id": null,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": null,
    "identity_method": "not_found",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": null,
    "alternates": [],
    "reason_code": "frontier_no_candidate_cluster"
  },
  "citations": {
    "official": null,
    "parallel": [],
    "vendor_neutral": [],
    "all": [],
    "display": null,
    "official_selection": {
      "court_class": null,
      "selected": null,
      "reason": null
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
    "scope_note": null,
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
    "date_created": "2026-07-06T05:02:22Z",
    "date_modified": "2026-07-06T05:02:26Z",
    "warnings": [
      "frontier not_found requires web/second-source cross-check before fabrication inference"
    ],
    "field_provenance": {
      "identity": {
        "src": "pending",
        "at": "2026-07-06T05:02:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "pending",
        "at": "2026-07-06T05:02:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "pending",
        "at": "2026-07-06T05:02:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "pending",
        "at": "2026-07-06T05:02:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

---
