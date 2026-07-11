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

## GROUP: content/cases/Egbert v. Boule.md  (`case`, 5 assertions)

### content_page

```
---
title: Egbert v. Boule
type: case
citation: "596 U.S. 482 (2022)"
parallel_cite: 142 S. Ct. 1793
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2022
date_decided: 2022-06-08
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
  opinion_url: "https://www.courtlistener.com/opinion/6475794/egbert-v-boule/"
  cluster_id: 6475794
  opinion_id: null
  identity_checked: true
lake:
  record_id: Egbert v. Boule
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Bivens v. Six Unknown Named Agents]]"
  - "[[Ziglar v. Abbasi]]"
  - "[[Hernandez v. Mesa]]"
tags:
  - case
  - fourth-amendment
  - bivens
  - section-1983
  - qualified-immunity
  - damages-remedy
  - supreme-court
holding: "The two-step Bivens inquiry — whether a claim arises in a new context and, if so, whether special factors counsel hesitation — often reduces to the single question whether Congress is better positioned than the courts to create a damages remedy; applying that framework, the Court declined to extend Bivens to Boule's Fourth Amendment excessive-force claim against a Border Patrol agent or his First Amendment retaliation claim."
aliases:
  - Egbert v. Boule
  - "Egbert v. Boule (2022)"
---

# Egbert v. Boule

*596 U.S. 482 (2022)* (No. 21-147) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6475794 → majority opinion 6347905 (Thomas, J.; 596 U.S. 482, decided June 8, 2022). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; slip-style pin (the CL text carries the U.S. slip-opinion pagination, not the 596 U.S. star pages) — S9 verifies the body pincite. -->

## Background
Robert Boule ran the Smuggler's Inn, a bed-and-breakfast abutting the Canada–U.S. border in Blaine, Washington. Border Patrol Agent Erik Egbert, suspecting a guest had just crossed the border, entered the inn's driveway; on Boule's account, Egbert refused a request to leave, threw Boule against a vehicle and then to the ground, checked the guest's papers, and left. After Boule complained, Egbert allegedly retaliated by reporting Boule's "SMUGLER" license plate and prompting an IRS audit. Boule sued Egbert directly under the Constitution, invoking *[[Bivens v. Six Unknown Named Agents|Bivens]]*, for Fourth Amendment excessive force and First Amendment retaliation. The Ninth Circuit recognized both damages actions.

## Issue
Whether *[[Bivens v. Six Unknown Named Agents|Bivens]]* supplies an implied damages remedy for a Fourth Amendment excessive-force claim against a Border Patrol agent and for a First Amendment retaliation claim.

## Rule
Recognizing a *[[Bivens v. Six Unknown Named Agents|Bivens]]* action is "a disfavored judicial activity," and if there is any rational reason to defer to Congress no remedy may be implied. The analysis proceeds in two steps — whether the case presents "a new *Bivens* context" and, if so, whether "special factors" show the Judiciary is "less equipped than Congress" to weigh a damages action's costs and benefits — but the Court held that this inquiry "often resolves to a single question: whether there is any reason to think that Congress might be better equipped to create a damages remedy." — slip op. at 2. ^pin-slip2

## Application
Both claims flunked the reformulated test. The Fourth Amendment claim arose in a new context — border security — where Congress and the Executive have independent interests and where an alternative remedial structure (the Border Patrol's grievance process) already existed; that Congress might be better suited to weigh the consequences of a damages remedy was reason enough to withhold one. The First Amendment retaliation claim failed for the further reason that the Court has never extended *[[Bivens v. Six Unknown Named Agents|Bivens]]* to First Amendment claims.

## Conclusion
**Reversed.** The Court held that *[[Bivens v. Six Unknown Named Agents|Bivens]]* does not extend to create causes of action for either the Fourth Amendment excessive-force claim or the First Amendment retaliation claim. Justice Thomas wrote for the Court; Justice Gorsuch concurred in the judgment; Justice Sotomayor concurred in part and dissented in part.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Egbert* is the modern capstone of the Court's retrenchment of *[[Bivens v. Six Unknown Named Agents|Bivens]]*, collapsing the *[[Ziglar v. Abbasi|Ziglar]]* two-step into a single congressional-deference question and, with *[[Hernandez v. Mesa]]*, leaving the implied constitutional-tort remedy nearly a dead letter outside its original three contexts — a counterpoint to the statutory § 1983 remedy against state officers.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Egbert v. Boule*, 596 U.S. 482 (2022)](https://www.courtlistener.com/opinion/6475794/egbert-v-boule/) — pinpoint: slip op. at 2 (the two-step-to-one-question Bivens rule). Rule quote string-matched to the CL slip-opinion syllabus 2026-07-07; parallel cite 142 S. Ct. 1793.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "99d783d90fd1e7b4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "596 U.S. 482 (2022)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "142 S. Ct. 1793", "title": "Egbert v. Boule", "year": "2022"}}
{"assertion_id": "71f46544bf6f3309", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "Egbert v. Boule"}}
{"assertion_id": "acde4b16368d5a40", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The two-step Bivens inquiry — whether a claim arises in a new context and, if so, whether special factors counsel hesitation — often reduces to the single question whether Congress is better positioned than the courts to create a damages remedy; applying that framework, the Court declined to extend Bivens to Boule's Fourth Amendment excessive-force claim against a Border Patrol agent or his First Amendment retaliation claim.", "title": "Egbert v. Boule"}}
{"assertion_id": "38bce43e494503f7", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Egbert v. Boule", "varies_by_point": "false"}}
{"assertion_id": "d6420ff2178979da", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Egbert v. Boule"}}
```

### lake record — Egbert v. Boule

```json
{
  "schema_version": "s2.v1",
  "record_id": "Egbert v. Boule",
  "status": "under_review",
  "identity": {
    "case_name": "Egbert v. Boule",
    "case_name_short": "Egbert",
    "case_name_full": "",
    "input_case_name": "Egbert v. Boule",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2022-06-08",
    "year": 2022,
    "docket": null,
    "cluster_id": 6475794,
    "lead_opinion_id": 6347905,
    "sibling_ids": [],
    "absolute_url": "/opinion/6475794/egbert-v-boule/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "596 U.S. 482",
      "volume": "596",
      "reporter": "U.S.",
      "page": "482",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "142 S. Ct. 1793",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1793",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "596 U.S. 482",
        "volume": "596",
        "reporter": "U.S.",
        "page": "482",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "142 S. Ct. 1793",
        "volume": "142",
        "reporter": "S. Ct.",
        "page": "1793",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "596 U.S. 482",
    "official_selection": {
      "court_class": "scotus",
      "selected": "596 U.S. 482",
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
    "date_created": "2026-07-06T05:45:13Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:45:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:45:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:45:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "egbert-v-boule--6475794",
      "to_record_id": "Egbert v. Boule",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Egbert v. Boule

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

                            EGBERT v. BOULE

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

       No. 21–147.      Argued March 2, 2022—Decided June 8, 2022
Respondent Robert Boule owns a bed-and-breakfast—the Smuggler’s
  Inn—in Blaine, Washington. The inn abuts the international border
  between Canada and the United States. Boule at times helped federal
  agents identify and apprehend persons engaged in unlawful cross-bor-
  der activity on or near his property. But Boule also would provide
  transportation and lodging to illegal border crossers. Often, Boule
  would agree to help illegal border crossers enter or exit the United
  States, only to later call federal agents to report the unlawful activity.
    In 2014, Boule informed petitioner Erik Egbert, a U. S. Border Pa-
  trol agent, that a Turkish national, arriving in Seattle by way of New
  York, had scheduled transportation to Smuggler’s Inn. When Agent
  Egbert observed one of Boule’s vehicles returning to the inn, he sus-
  pected that the Turkish national was a passenger and followed the ve-
  hicle to the inn. On Boule’s account, Boule asked Egbert to leave, but
  Egbert refused, became violent, and threw Boule first against the ve-
  hicle and then to the ground. Egbert then checked the immigration
  paperwork for Boule’s guest and left after finding everything in order.
  The Turkish guest unlawfully entered Canada later that evening.
    Boule filed a grievance with Agent Egbert’s supervisors and an ad-
  ministrative claim with Border Patrol pursuant to the Federal Tort
  Claims Act (FTCA). Egbert allegedly retaliated against Boule by re-
  porting Boule’s “SMUGLER” license plate to the Washington Depart-
  ment of Licensing for referencing illegal activity, and by contacting the
  Internal Revenue Service and prompting an audit of Boule’s tax re-
  turns. Boule’s FTCA claim was ultimately denied, and Border Patrol
  took no action against Egbert for his use of force or alleged acts of re-
  taliation. Boule then sued Egbert in Federal District Court, alleging
  a Fourth Amendment violation for excessive use of force and a First
2                          EGBERT v. BOULE

                                 Syllabus

    Amendment violation for unlawful retaliation. Invoking Bivens v. Six
    Unknown Fed. Narcotics Agents, 403 U. S. 388, Boule asked the Dis-
    trict Court to recognize a damages action for each alleged constitu-
    tional violation. The District Court declined to extend Bivens as re-
    quested, but the Court of Appeals reversed.
Held: Bivens does not extend to create causes of action for Boule’s Fourth
 Amendment excessive-force claim and First Amendment retaliation
 claim. Pp. 5–17.
    (a) In Bivens, the Court held that it had authority to create a dam-
 ages action against federal agents for violating the plaintiff’s Fourth
 Amendment rights. Over the next decade, the Court also fashioned
 new causes of action under the Fifth Amendment, see Davis v. Pass-
 man, 442 U. S. 228, and the Eighth Amendment, see Carlson v. Green,
 446 U. S. 14. Since then, however, the Court has come “to appreciate
 more fully the tension between” judicially created causes of action and
 “the Constitution’s separation of legislative and judicial power,” Her-
 nández v. Mesa, 589 U. S. ___, ___, and has declined 11 times to imply
 a similar cause of action for other alleged constitutional violations, see,
 e.g., Chappell v. Wallace, 462 U. S. 296; Bush v. Lucas, 462 U. S. 367.
 Rather than dispense with Bivens, the Court now emphasizes that rec-
 ognizing a Bivens cause of action is “a disfavored judicial activity.”
 Ziglar v. Abbasi, 582 U. S. ___, ___.
    The analysis of a proposed Bivens claim proceeds in two steps: A
 court asks first whether the case presents “a new Bivens context”—i.e.,
 is it “meaningfully different from the three cases in which the Court
 has implied a damages action,” Ziglar, 582 U. S., at ___, and, second,
 even if so, do “special factors” indicate that the Judiciary is at least
 arguably less equipped than Congress to “weigh the costs and benefits
 of allowing a damages action to proceed.” Id., at ___. This two-step
 inquiry often resolves to a single question: whether there is any reason
 to think that Congress might be better equipped to create a damages
 remedy. Further, under the Court’s precedents, a court may not fash-
 ion a Bivens remedy if Congress already has provided, or has author-
 ized the Executive to provide, “an alternative remedial structure.”
 Ziglar, 582 U. S., at ___. Pp. 5–8.
    (b) The Court of Appeals conceded that Boule’s Fourth Amendment
 claim presented a new Bivens context, but its conclusion that there
 was no reason to hesitate before recognizing a cause of action against
 Agent Egbert was incorrect for two independent reasons. Pp. 9–13.
       (1) First, the “risk of undermining border security provides reason
 to hesitate before extending Bivens into this field.” Hernández, 589
 U. S., at ___. In Hernández, the Court declined to create a damages
 remedy for an excessive-force claim against a Border Patrol agent be-
 cause “regulating the conduct of agents at the border unquestionably
                    Cite as: 596 U. S. ____ (2022)                      3

                               Syllabus

has national security implications.” Id., at ___. That reasoning applies
with full force here. The Court of Appeals disagreed because it viewed
Boule’s Fourth Amendment claim as akin to a “conventional” exces-
sive-force claim, as in Bivens, and less like the cross-border shooting
in Hernández. But that does not bear on the relevant point: Permitting
suit against a Border Patrol agent presents national security concerns
that foreclose Bivens relief. Further, the Court of Appeals’ analysis
betrays the pitfalls of applying the special-factors analysis at too gran-
ular a level. A court should not inquire whether Bivens relief is appro-
priate in light of the balance of circumstances in the “particular case.”
United States v. Stanley, 483 U. S. 669, 683. Rather, it should ask
“[m]ore broadly” whether there is any reason to think that “judicial
intrusion” into a given field might be “harmful” or “inappropriate,” id.,
at 681. The proper inquiry here is whether a court is competent to
authorize a damages action not just against Agent Egbert, but against
Border Patrol agents generally. The answer is no. Pp. 9–12.
      (2) Second, Congress has provided alternative remedies for ag-
grieved parties in Boule’s position that independently foreclose a
Bivens action here. By regulation, Border Patrol must investigate
“[a]lleged violations” and accept grievances from “[a]ny persons.” 8
CFR §§287.10(a)–(b). Boule claims that this regulatory grievance pro-
cedure was inadequate, but this Court has never held that a Bivens
alternative must afford rights such as judicial review of an adverse
determination. Bivens “is concerned solely with deterring the uncon-
stitutional acts of individual officers.” Correctional Services Corp. v.
Malesko, 534 U. S. 61, 71. And, regardless, the question whether a
given remedy is adequate is a legislative determination. As in Her-
nández, this Court has no warrant to doubt that the consideration of
Boule’s grievance secured adequate deterrence and afforded Boule an
alternative remedy. See 589 U. S., at ___. Pp. 12–13.
   (c) There is no Bivens cause of action for Boule’s First Amendment
retaliation claim. That claim presents a new Bivens context, and there
are many reasons to think that Congress is better suited to authorize
a damages remedy. Extending Bivens to alleged First Amendment vi-
olations would pose an acute “risk that fear of personal monetary lia-
bility and harassing litigation will unduly inhibit officials in the dis-
charge of their duties.” Anderson v. Creighton, 483 U. S. 635, 638. In
light of these costs, “Congress is in a better position to decide whether
or not the public interest would be served” by imposing a damages ac-
tion. Bush, 462 U. S., at 389. The Court of Appeals’ reasons for ex-
tending Bivens in this context—that retaliation claims are “well-estab-
lished” and that Boule alleges that Agent Egbert “was not carrying out
official duties” when the retaliation occurred—lack merit. Also lacking
4                           EGBERT v. BOULE

                                  Syllabus

    merit is Boule’s claim that this Court identified a Bivens cause of ac-
    tion under allegedly similar circumstances in Passman. Even assum-
    ing factual parallels, Passman carries little weight because it predates
    the Court’s current approach to implied causes of action. A plaintiff
    cannot justify a Bivens extension based on “parallel circumstances”
    with Bivens, Passman, or Carlson—the three cases in which the Court
    has implied a damages action—unless the plaintiff also satisfies the
    prevailing “analytic framework” prescribed by the last four decades of
    intervening case law. Ziglar, 582 U. S., at ___–___. Pp. 13–16.
998 F. 3d 370, reversed.

  THOMAS, J., delivered the opinion of the Court, in which ROBERTS, C. J.,
and ALITO, KAVANAUGH, and BARRETT, JJ., joined. GORSUCH, J., filed an
opinion concurring in the judgment. SOTOMAYOR, J., filed an opinion con-
curring in the judgment in part and dissenting in part, in which BREYER
and KAGAN, JJ., joined.
                        Cite as: 596 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 21–147
                                    _________________


   ERIK EGBERT, PETITIONER v. ROBERT BOULE
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                                   [June 8, 2022]

   JUSTICE THOMAS delivered the opinion of the Court.
   In Bivens v. Six Unknown Fed. Narcotics Agents, 403
U. S. 388 (1971), this Court authorized a damages action
against federal officials for alleged violations of the Fourth
Amendment. Over the past 42 years, however, we have de-
clined 11 times to imply a similar cause of action for other
alleged constitutional violations. See Chappell v. Wallace,
462 U. S. 296 (1983); Bush v. Lucas, 462 U. S. 367 (1983);
United States v. Stanley, 483 U. S. 669 (1987); Schweiker v.
Chilicky, 487 U. S. 412 (1988); FDIC v. Meyer, 510 U. S. 471
(1994); Correctional Services Corp. v. Malesko, 534 U. S. 61
(2001); Wilkie v. Robbins, 551 U. S. 537 (2007); Hui v. Cas-
taneda, 559 U. S. 799 (2010); Minneci v. Pollard, 565 U. S.
118 (2012); Ziglar v. Abbasi, 582 U. S. ___ (2017); Hernán-
dez v. Mesa, 589 U. S. ___ (2020). Nevertheless, the Court
of Appeals permitted not one, but two constitutional dam-
ages actions to proceed against a U. S. Border Patrol agent:
a Fourth Amendment excessive-force claim and a First
Amendment retaliation claim. Because our cases have
made clear that, in all but the most unusual circumstances,
prescribing a cause of action is a job for Congress, not the
courts, we reverse.
2                     EGBERT v. BOULE

                      Opinion of the Court

                              I
  Blaine, Washington, is the last town in the United States
along U. S. Interstate Highway 5 before reaching the Cana-
dian border. Respondent Robert Boule is a longtime Blaine
resident. The rear of his property abuts the Canadian bor-
der at “0 Avenue,” a Canadian street. Boule’s property line
actually extends five feet into Canada. Several years ago,
Boule placed a line of small stones on his property to mark
the international boundary. As shown below, any person
could easily enter the United States or Canada through or
near Boule’s property. See App. 100.




  Boule markets his home as a bed-and-breakfast aptly
named “Smuggler’s Inn.” The area surrounding the Inn “is
a hotspot for cross-border smuggling of people, drugs, illicit
money, and items of significance to criminal organizations.”
Id., at 91. “On numerous occasions,” U. S. Border Patrol
agents “have observed persons come south across the bor-
der and walk into Smuggler’s Inn through the back door.”
Id., at 101. Federal agents also have seized from the Inn
shipments of cocaine, methamphetamine, ecstasy, and
other narcotics. For a time, Boule served as a confidential
                     Cite as: 596 U. S. ____ (2022)                    3

                          Opinion of the Court

informant who would help federal agents identify and ap-
prehend persons engaged in unlawful cross-border activity
on or near his property. Boule claims that the Government
has paid him upwards of $60,000 for his services.
   Ever the entrepreneur, Boule saw his relationship with
Border Patrol as a business opportunity. Boule would host
persons who unlawfully entered the United States as
“guests” at the Inn and offer to drive them to Seattle or else-
where. He also would pick up Canada-bound guests
throughout the State and drive them north to his property
along the border. Either way, Boule would charge $100–
$150 per hour for his shuttle service and require guests to
pay for a night of lodging even if they never intended to stay
at the Inn. Meanwhile, Boule would inform federal law en-
forcement if he was scheduled to lodge or transport persons
of interest. In short order, Border Patrol agents would ar-
rive to arrest the guests, often within a few blocks of the
Inn. Boule would decline to offer his erstwhile customers a
refund. In his view, this practice was “nothing any different
than [the] normal policies of any hotel/motel.” Id., at 120.1
   In light of Boule’s business model, local Border Patrol
agents, including petitioner Erik Egbert, were well ac-
quainted with Smuggler’s Inn and the criminal activity that
attended it. On March 20, 2014, Boule informed Agent Eg-
bert that a Turkish national, arriving in Seattle by way of
New York, had scheduled transportation to Smuggler’s Inn
later that day. Agent Egbert grew suspicious, as he could
think of “no legitimate reason a person would travel from
Turkey to stay at a rundown bed-and-breakfast on the bor-
der in Blaine.” Id., at 104. The photograph below displays
the amenities for which Boule’s Turkish guest would have
——————
  1 Notwithstanding his defense of the Inn’s policies, Boule was recently

convicted in Canadian court for engaging in human trafficking. In De-
cember 2021, he pleaded guilty to trafficking 11 Afghanis and Syrians
into Canada. He billed each foreign national between $200 and $700 for
the trip. See Regina v. Boule, 2021 BCSC 2561, ¶¶7–11.
4                    EGBERT v. BOULE

                     Opinion of the Court

traveled more than 7,500 miles. See id., at 102.




   Later that afternoon, Agent Egbert observed one of
Boule’s vehicles—a black SUV with the license plate
“SMUGLER”—returning to the Inn. Agent Egbert sus-
pected that Boule’s Turkish guest was a passenger and fol-
lowed the SUV into the driveway so he could check the
guest’s immigration status. On Boule’s account, the situa-
tion escalated from there. Boule instructed Agent Egbert
to leave his property, but Agent Egbert declined. Instead,
Boule claims, Agent Egbert lifted him off the ground and
threw him against the SUV. After Boule collected himself,
Agent Egbert allegedly threw him to the ground. Agent Eg-
bert then checked the guest’s immigration paperwork, con-
cluded that everything was in order, and left. Later that
evening, Boule’s Turkish guest unlawfully entered Canada
from Smuggler’s Inn.
   Boule lodged a grievance with Agent Egbert’s supervi-
sors, alleging that Agent Egbert had used excessive force
and caused him physical injury. Boule also filed an admin-
istrative claim with Border Patrol pursuant to the Federal
Tort Claims Act (FTCA). See 28 U. S. C. §2675(a). Accord-
ing to Boule, Agent Egbert retaliated against him while
                   Cite as: 596 U. S. ____ (2022)              5

                       Opinion of the Court

those claims were pending by reporting Boule’s
“SMUGLER” license plate to the Washington Department
of Licensing for referencing illegal conduct, and by contact-
ing the Internal Revenue Service and prompting an audit
of Boule’s tax returns. Ultimately, Boule’s FTCA claim was
denied and, after a year-long investigation, Border Patrol
took no action against Agent Egbert for his alleged use of
force or acts of retaliation. Thereafter, Agent Egbert con-
tinued to serve as an active-duty Border Patrol agent.
   In January 2017, Boule sued Agent Egbert in his individ-
ual capacity in Federal District Court, alleging a Fourth
Amendment violation for excessive use of force and a First
Amendment violation for unlawful retaliation. Boule in-
voked Bivens and asked the District Court to recognize a
damages action for each alleged constitutional violation.
The District Court declined to extend a Bivens remedy to
Boule’s claims and entered judgment for Agent Egbert. The
Court of Appeals reversed. See 998 F. 3d 370, 385 (CA9
2021). Twelve judges dissented from the denial of rehear-
ing en banc. See id., at 373 (Bumatay, J., dissenting); id.,
at 384 (Owens, J., dissenting); ibid. (Bress, J., dissenting).
   We granted certiorari. 595 U. S. ___ (2021).
                               II
   In Bivens, the Court held that it had authority to create
“a cause of action under the Fourth Amendment” against
federal agents who allegedly manacled the plaintiff and
threatened his family while arresting him for narcotics vio-
lations. 403 U. S., at 397. Although “the Fourth Amend-
ment does not in so many words provide for its enforcement
by an award of money damages,” id., at 396, the Court “held
that it could authorize a remedy under general principles of
federal jurisdiction,” Ziglar, 582 U. S., at ___ (slip op., at 7)
(citing Bivens, 403 U. S., at 392). Over the following decade,
the Court twice again fashioned new causes of action under
the Constitution—first, for a former congressional staffer’s
6                     EGBERT v. BOULE

                      Opinion of the Court

Fifth Amendment sex-discrimination claim, see Davis v.
Passman, 442 U. S. 228 (1979); and second, for a federal
prisoner’s inadequate-care claim under the Eighth Amend-
ment, see Carlson v. Green, 446 U. S. 14 (1980).
   Since these cases, the Court has not implied additional
causes of action under the Constitution. Now long past “the
heady days in which this Court assumed common-law pow-
ers to create causes of action,” Malesko, 534 U. S., at 75
(Scalia, J., concurring), we have come “to appreciate more
fully the tension between” judicially created causes of ac-
tion and “the Constitution’s separation of legislative and ju-
dicial power,” Hernández, 589 U. S., at ___ (slip op., at 5).
At bottom, creating a cause of action is a legislative en-
deavor. Courts engaged in that unenviable task must eval-
uate a “range of policy considerations . . . at least as broad
as the range . . . a legislature would consider.” Bivens, 403
U. S., at 407 (Harlan, J., concurring in judgment); see also
post, at 2 (GORSUCH, J., concurring in judgment). Those
factors include “economic and governmental concerns,” “ad-
ministrative costs,” and the “impact on governmental oper-
ations systemwide.” Ziglar, 582 U. S., at ___, ___ (slip op.,
at 10, 13). Unsurprisingly, Congress is “far more competent
than the Judiciary” to weigh such policy considerations.
Schweiker, 487 U. S., at 423. And the Judiciary’s authority
to do so at all is, at best, uncertain. See, e.g., Hernández,
589 U. S., at ___ (slip op., at 6).
   Nonetheless, rather than dispense with Bivens alto-
gether, we have emphasized that recognizing a cause of ac-
tion under Bivens is “a disfavored judicial activity.” Ziglar,
582 U. S., at ___ (slip op., at 11) (internal quotation marks
omitted); Hernández, 589 U. S., at ___ (slip op., at 7) (inter-
nal quotation marks omitted). When asked to imply a
Bivens action, “our watchword is caution.” Id., at ___ (slip
op., at 6). “[I]f there are sound reasons to think Congress
might doubt the efficacy or necessity of a damages rem-
edy[,] the courts must refrain from creating [it].” Ziglar,
                  Cite as: 596 U. S. ____ (2022)              7

                      Opinion of the Court

582 U. S., at ___ (slip op., at 13). “[E]ven a single sound
reason to defer to Congress” is enough to require a court to
refrain from creating such a remedy. Nestlé USA, Inc. v.
Doe, 593 U. S. ___, ___ (2021) (plurality opinion) (slip op., at
6). Put another way, “the most important question is who
should decide whether to provide for a damages remedy,
Congress or the courts?” Hernández, 589 U. S., at ___–___
(slip op., at 19–20) (internal quotation marks omitted). If
there is a rational reason to think that the answer is “Con-
gress”—as it will be in most every case, see Ziglar, 582
U. S., at ___ (slip op., at 12)—no Bivens action may lie. Our
cases instruct that, absent utmost deference to Congress’
preeminent authority in this area, the courts “arrogat[e]
legislative power.” Hernández, 589 U. S., at ___ (slip op., at
5).
   To inform a court’s analysis of a proposed Bivens claim,
our cases have framed the inquiry as proceeding in two
steps. See Hernández, 589 U. S., at ___ (slip op., at 7).
First, we ask whether the case presents “a new Bivens con-
text”—i.e., is it “meaningful[ly]” different from the three
cases in which the Court has implied a damages action.
Ziglar, 582 U. S., at ___ (slip op., at 16). Second, if a claim
arises in a new context, a Bivens remedy is unavailable if
there are “special factors” indicating that the Judiciary is
at least arguably less equipped than Congress to “weigh the
costs and benefits of allowing a damages action to proceed.”
Ziglar, 582 U. S., at ___ (slip op., at 12) (internal quotation
marks omitted). If there is even a single “reason to pause
before applying Bivens in a new context,” a court may not
recognize a Bivens remedy. Hernández, 589 U. S., at ___
(slip op., at 7).
   While our cases describe two steps, those steps often re-
solve to a single question: whether there is any reason to
think that Congress might be better equipped to create a
damages remedy. For example, we have explained that a
new context arises when there are “potential special factors
8                         EGBERT v. BOULE

                          Opinion of the Court

that previous Bivens cases did not consider.” Ziglar, 582
U. S., at ___ (slip op., at 16). And we have identified several
examples of new contexts—e.g., a case that involves a “new
category of defendants,” Malesko, 534 U. S., at 68; see also
Ziglar, 582 U. S., at ___ (slip op., at 11)—largely because
they represent situations in which a court is not undoubt-
edly better positioned than Congress to create a damages
action. We have never offered an “exhaustive” accounting
of such scenarios, however, because no court could forecast
every factor that might “counse[l] hesitation.” Id., at ___
(slip op., at 16). Even in a particular case, a court likely
cannot predict the “systemwide” consequences of recogniz-
ing a cause of action under Bivens. Ziglar, 582 U. S., at ___
(slip op., at 13). That uncertainty alone is a special factor
that forecloses relief. See Hernández v. Mesa, 885 F. 3d
811, 818 (CA5 2018) (en banc) (“The newness of this ‘new
context’ should alone require dismissal”).
   Finally, our cases hold that a court may not fashion a
Bivens remedy if Congress already has provided, or has au-
thorized the Executive to provide, “an alternative remedial
structure.” Ziglar, 582 U. S., at ___ (slip op., at 14); see also
Schweicker, 487 U. S., at 425. If there are alternative re-
medial structures in place, “that alone,” like any special fac-
tor, is reason enough to “limit the power of the Judiciary to
infer a new Bivens cause of action.” Ziglar, 582 U. S., at ___
(slip op., at 14).2 Importantly, the relevant question is not
whether a Bivens action would “disrup[t]” a remedial
scheme, Schweicker, 487 U. S., at 426, or whether the court
“should provide for a wrong that would otherwise go unre-
dressed,” Bush, 462 U. S., at 388. Nor does it matter that
——————
  2 Congress also may preclude a claim under Bivens v. Six Unknown

Fed. Narcotics Agents, 403 U. S. 388 (1971), against federal officers if it
affirmatively forecloses one. “Even in circumstances in which a Bivens
remedy is generally available, an action under Bivens will be defeated if
the defendant is immune from suit,” Hui v. Castaneda, 559 U. S. 799,
807 (2010), and Congress may grant such immunity as it sees fit.
                  Cite as: 596 U. S. ____ (2022)             9

                      Opinion of the Court

“existing remedies do not provide complete relief.” Ibid.
Rather, the court must ask only whether it, rather than the
political branches, is better equipped to decide whether ex-
isting remedies “should be augmented by the creation of a
new judicial remedy.” Ibid; see also id., at 380 (“the ques-
tion [is] who should decide”).
                           III
  Applying the foregoing principles, the Court of Appeals
plainly erred when it created causes of action for Boule’s
Fourth Amendment excessive-force claim and First Amend-
ment retaliation claim.
                              A
  The Court of Appeals conceded that Boule’s Fourth
Amendment claim presented a new context for Bivens pur-
poses, yet it concluded there was no reason to hesitate be-
fore recognizing a cause of action against Agent Egbert. See
998 F. 3d, at 387. That conclusion was incorrect for two in-
dependent reasons: Congress is better positioned to create
remedies in the border-security context, and the Govern-
ment already has provided alternative remedies that pro-
tect plaintiffs like Boule. We address each in turn.
                                1
  In Hernández, we declined to create a damages remedy
for an excessive-force claim against a Border Patrol agent
who shot and killed a 15-year-old Mexican national across
the border in Mexico. See 589 U. S., at ___–___ (slip op., at
1–2). We did not recognize a Bivens action there because
“regulating the conduct of agents at the border unquestion-
ably has national security implications,” and the “risk of
undermining border security provides reason to hesitate be-
fore extending Bivens into this field.” Hernández, 589 U. S.,
at ___ (slip op., at 14). This reasoning applies here with full
force. During the alleged altercation with Boule, Agent Eg-
10                    EGBERT v. BOULE

                      Opinion of the Court

bert was carrying out Border Patrol’s mandate to “inter-
dic[t] persons attempting to illegally enter or exit the
United States or goods being illegally imported into or ex-
ported from the United States.” 6 U. S. C. §211(e)(3)(A).
Because “[m]atters intimately related to foreign policy and
national security are rarely proper subjects for judicial in-
tervention,” Haig v. Agee, 453 U. S. 280, 292 (1981), we re-
affirm that a Bivens cause of action may not lie where, as
here, national security is at issue.
    The Court of Appeals thought otherwise. In its view,
Boule’s Fourth Amendment claim is “conventional,” 998
F. 3d, at 387; see also post, at 8, 12 (SOTOMAYOR, J., concur-
ring in judgment in part and dissenting in part) (same),
and, though it arises in a new context, this Court has not
“ ‘cast doubt’ ” on extending Bivens within the “ ‘common and
recurrent sphere of law enforcement’ ” in which it arose, 998
F. 3d, at 389 (quoting Ziglar, 582 U. S., at ___ (slip op., at
11)). While Bivens and this case do involve similar allega-
tions of excessive force and thus arguably present “almost
parallel circumstances” or a similar “mechanism of injury,”
Ziglar, 582 U. S., at ___ (slip op., at 15), these superficial
similarities are not enough to support the judicial creation
of a cause of action. The special-factors inquiry—which
Bivens never meaningfully undertook, see Stanley, 483
U. S., at 678—shows here, no less than in Hernández, that
the Judiciary is not undoubtedly better positioned than
Congress to authorize a damages action in this national-se-
curity context. That this case does not involve a cross-bor-
der shooting, as in Hernández, but rather a more “conven-
tional” excessive-force claim, as in Bivens, does not bear on
the relevant point. Either way, the Judiciary is compara-
tively ill suited to decide whether a damages remedy
against any Border Patrol agent is appropriate.
    The Court of Appeals downplayed the national-security
risk from imposing Bivens liability because Agent Egbert
was not “literally ‘at the border,’ ” and Boule’s guest already
                  Cite as: 596 U. S. ____ (2022)            11

                      Opinion of the Court

had cleared customs in New York. 998 F. 3d, at 388; see
also post, at 11–12, 18 (opinion of SOTOMAYOR, J.) (same).
The court also found that Boule had a weightier interest in
Bivens relief than the parents of the deceased Mexican
teenager in Hernández, because Boule “is a United States
citizen, complaining of harm suffered on his own property
in the United States.” 998 F. 3d, at 388; see also post, at 12,
18 (opinion of SOTOMAYOR, J.) (same). Finding that “any
costs imposed by allowing a Bivens claim to proceed are out-
weighed by compelling interests in favor of protecting
United States citizens on their own property in the United
States,” the court extended Bivens to Boule’s case. 998
F. 3d, at 389.
   This analysis is deeply flawed. The Bivens inquiry does
not invite federal courts to independently assess the costs
and benefits of implying a cause of action. A court faces
only one question: whether there is any rational reason
(even one) to think that Congress is better suited to “weigh
the costs and benefits of allowing a damages action to pro-
ceed.” Ziglar, 582 U. S., at ___ (slip op., at 12). Thus, a
court should not inquire, as the Court of Appeals did here,
whether Bivens relief is appropriate in light of the balance
of circumstances in the “particular case.” Stanley, 483
U. S., at 683. A court inevitably will “impai[r]” governmen-
tal interests, and thereby frustrate Congress’ policymaking
role, if it applies the “ ‘special factors’ analysis” at such a
narrow “leve[l] of generality.” Id., at 681. Rather, under
the proper approach, a court must ask “[m]ore broadly” if
there is any reason to think that “judicial intrusion” into a
given field might be “harmful” or “inappropriate.” Ibid. If
so, or even if there is the “potential” for such consequences,
a court cannot afford a plaintiff a Bivens remedy. Ziglar,
582 U. S., at ___, ___ (slip op., at 16, 25) (emphasis added).
As in Hernández, then, we ask here whether a court is com-
petent to authorize a damages action not just against Agent
12                    EGBERT v. BOULE

                      Opinion of the Court

Egbert but against Border Patrol agents generally. The an-
swer, plainly, is no. See Hernández, 589 U. S., at ___ (slip
op., at 14) (refusing to extend Bivens into the “field” of “bor-
der security”).
   The Court of Appeals’ analysis betrays the pitfalls of ap-
plying the special-factors analysis at too granular a level.
The court rested on three irrelevant distinctions from Her-
nández. First, Agent Egbert was several feet from (rather
than straddling) the border, but cross-border security is ob-
viously implicated in either event. Second, Boule’s guest
arrived in Seattle from New York rather than abroad, but
an alien’s port of entry does not make him less likely to be
a national-security threat. And third, Agent Egbert inves-
tigated immigration violations on our side of the border, not
Canada’s, but immigration investigations in this country
are perhaps more likely to impact the national security of
the United States. In short, the Court of Appeals offered no
plausible basis to permit a Fourth Amendment Bivens
claim against Agent Egbert to proceed.
                               2
   Second, Congress has provided alternative remedies for
aggrieved parties in Boule’s position that independently
foreclose a Bivens action here. In Hernández, we declined
to authorize a Bivens remedy, in part, because the Execu-
tive Branch already had investigated alleged misconduct by
the defendant Border Patrol agent. See 589 U. S., at ___–
___, ___ (slip op., at 9–10, 14). In Malesko, we explained
that Bivens relief was unavailable because federal prison-
ers could, among other options, file grievances through an
“Administrative Remedy Program.” 534 U. S., at 74. Both
kinds of remedies are available here. The U. S. Border Pa-
trol is statutorily obligated to “control, direc[t], and super-
vis[e] . . . all employees.” 8 U. S. C. §1103(a)(2). And, by
regulation, Border Patrol must investigate “[a]lleged viola-
tions of the standards for enforcement activities” and accept
                      Cite as: 596 U. S. ____ (2022)                       13

                           Opinion of the Court

grievances from “[a]ny persons wishing to lodge a com-
plaint.” 8 CFR §§287.10(a)–(b). As noted, Boule took ad-
vantage of this grievance procedure, prompting a year-long
internal investigation into Agent Egbert’s conduct. See su-
pra, at 4–5.
   Boule nonetheless contends that Border Patrol’s griev-
ance process is inadequate because he is not entitled to par-
ticipate and has no right to judicial review of an adverse
determination.3 But we have never held that a Bivens al-
ternative must afford rights to participation or appeal.
That is so because Bivens “is concerned solely with deter-
ring the unconstitutional acts of individual officers”—i.e.,
the focus is whether the Government has put in place safe-
guards to “preven[t]” constitutional violations “from recur-
ring.” Malesko, 534 U. S., at 71, 74; see also Meyer, 510
U. S., at 485. And, again, the question whether a given
remedy is adequate is a legislative determination that must
be left to Congress, not the federal courts. So long as Con-
gress or the Executive has created a remedial process that
it finds sufficient to secure an adequate level of deterrence,
the courts cannot second-guess that calibration by superim-
posing a Bivens remedy. That is true even if a court inde-
pendently concludes that the Government’s procedures are
“not as effective as an individual damages remedy.” Bush,
——————
   3 Boule also argues that Agent Egbert forfeited any argument about

Border Patrol’s grievance process because he did not raise the issue in
the Court of Appeals. We disagree. Because recognizing a Bivens cause
of action “is an extraordinary act that places great stress on the separa-
tion of powers,” Nestlé USA, Inc. v. Doe, 593 U. S. ___, ___ (2021) (plural-
ity opinion) (slip op., at 7), we have “a concomitant responsibility” to eval-
uate any grounds that counsel against Bivens relief, Oliva v. Nivar, 973
F. 3d 438, 443, n. 2 (CA5 2020); see also Elhady v. Unidentified CBP
Agents, 18 F. 4th 880, 884 (CA6 2021). And, in any event, Agent Egbert
has consistently claimed that alternative remedies foreclose applying
Bivens in this case. Thus, under our precedents, he is “not limited to the
precise arguments [he] made below.” Yee v. Escondido, 503 U. S. 519,
534 (1992).
14                    EGBERT v. BOULE

                      Opinion of the Court

462 U. S., at 372. Thus here, as in Hernández, we have no
warrant to doubt that the consideration of Boule’s grievance
against Agent Egbert secured adequate deterrence and af-
forded Boule an alternative remedy. See 589 U. S., at ___
(slip op., at 10).
                               B
   We also conclude that there is no Bivens cause of action
for Boule’s First Amendment retaliation claim. While we
have assumed that such a damages action might be availa-
ble, see, e.g., Hartman v. Moore, 547 U. S. 250, 252 (2006),
“[w]e have never held that Bivens extends to First Amend-
ment claims,” Reichle v. Howards, 566 U. S. 658, 663, n. 4
(2012). Because a new context arises when there is a new
“constitutional right at issue,” Ziglar, 582 U. S., at ___ (slip
op., at 16), the Court of Appeals correctly held that Boule’s
First Amendment claim presents a new Bivens context. See
998 F. 3d, at 390. Now presented with the question
whether to extend Bivens to this context, we hold that there
is no Bivens action for First Amendment retaliation. There
are many reasons to think that Congress, not the courts, is
better suited to authorize such a damages remedy.
   Recognizing any new Bivens action “entail[s] substantial
social costs, including the risk that fear of personal mone-
tary liability and harassing litigation will unduly inhibit of-
ficials in the discharge of their duties.” Anderson v.
Creighton, 483 U. S. 635, 638 (1987). Extending Bivens to
alleged First Amendment violations would pose an acute
risk of increasing such costs. A plaintiff can turn practically
any adverse action into grounds for a retaliation claim.
And, “[b]ecause an official’s state of mind is easy to allege
and hard to disprove, insubstantial claims that turn on [re-
taliatory] intent may be less amenable to summary disposi-
tion.” Crawford-El v. Britton, 523 U. S. 574, 584–585
(1998) (internal quotation marks omitted). Even a frivolous
                  Cite as: 596 U. S. ____ (2022)            15

                      Opinion of the Court

retaliation claim “threaten[s] to set off broad-ranging dis-
covery in which there is often no clear end to the relevant
evidence.” Nieves v. Bartlett, 587 U. S. ___, ___ (2019) (slip
op., at 11) (internal quotation marks omitted).
   “[U]ndoubtedly,” then, the “prospect of personal liability”
under the First Amendment would lead “to new difficulties
and expense.” Schweiker, 487 U. S., at 425. Federal em-
ployees “face[d with] the added risk of personal liability for
decisions that they believe to be a correct response to im-
proper [activity] would be deterred from” carrying out their
duties. Bush, 462 U. S., at 389. We are therefore “con-
vinced” that, in light of these costs, “Congress is in a better
position to decide whether or not the public interest would
be served” by imposing a damages action. Id., at 390.
   The Court of Appeals nonetheless extended Bivens to the
First Amendment because, in its view, retaliation claims
are “well-established,” and Boule alleges that Agent Egbert
“was not carrying out official duties” when he retaliated
against him. 998 F. 3d, at 391. Neither rationale has merit.
First, just because plaintiffs often plead unlawful retalia-
tion to establish a First Amendment violation is not a rea-
son to afford them a cause of action to sue federal officers
for money damages. If anything, that retaliation claims are
common, and therefore more likely to impose “a significant
expansion of Government liability,” Meyer, 510 U. S., at
486, counsels against permitting Bivens relief.
   Second, the Court of Appeals’ scope-of-duty observation
does not meaningfully limit the number of potential Bivens
claims or otherwise undermine the reasons for hesitation
stated above. It is easy to allege that federal employees
acted beyond the scope of their authority when claiming a
constitutional violation. And, regardless, granting Bivens
relief because a federal agent supposedly did not act pursu-
ant to his law-enforcement mission “misses the point.” Her-
nández, 589 U. S., at ___ (slip op., at 14). “The question is
not whether national security,” or some other governmental
16                    EGBERT v. BOULE

                      Opinion of the Court

interest, actually “requires [the defendant’s] conduct.” Ibid.
Instead, we “ask whether the Judiciary should alter the
framework established by the political branches for ad-
dressing” any such conduct that allegedly violates the Con-
stitution. Ibid. With respect to that question, the foregoing
discussion shows that the Judiciary is ill equipped to alter
that framework generally, and especially so when it comes
to First Amendment claims.
  Boule responds that any hesitation is unwarranted be-
cause this Court in Passman already identified a Bivens
cause of action under allegedly similar circumstances.
There, the Court permitted a congressional staffer to sue a
congressman for sex discrimination under the Fifth Amend-
ment. See 442 U. S., at 231. In Boule’s view, Passman, like
this case, permitted a damages action to proceed even
though it required the factfinder to probe a federal official’s
motives for taking an adverse action against the plaintiff.
  Even assuming the factual parallels are as close as Boule
claims, Passman carries little weight because it predates
our current approach to implied causes of action and di-
verges from the prevailing framework in three important
ways. First, the Passman Court concluded that a Bivens
action must be available if there is “no effective means other
than the judiciary to vindicate” the purported Fifth Amend-
ment right. 442 U. S., at 243; see also Carlson, 446 U. S.,
at 18–19 (Congress can foreclose Bivens relief by
“provid[ing] an alternative remedy which it explicitly de-
clared to be a substitute for recovery directly under the Con-
stitution and viewed as equally effective”). Since then, how-
ever, we have explained that the absence of relief “does not
by any means necessarily imply that courts should award
money damages.” Schweiker, 487 U. S., at 421. Second,
Passman indicated that a damages remedy is appropriate
unless Congress “explicit[ly]” declares that a claimant “may
not recover money damages.” 442 U. S., at 246–247 (inter-
nal quotation marks omitted; emphasis deleted). Now,
                  Cite as: 596 U. S. ____ (2022)             17

                      Opinion of the Court

though, we defer to “congressional inaction” if “the design
of a Government program suggests that Congress has pro-
vided what it considers adequate remedial mechanisms.”
Schweiker, 487 U. S., at 423; see also Ziglar, 582 U. S., at
___ (slip op., at 14). Third, when assessing the “special fac-
tors,” Passman asked whether a court is competent to cal-
culate damages “without difficult questions of valuation or
causation.” 442 U. S., at 245. But today, we do not ask
whether a court can determine a damages amount. Rather,
we ask whether “there are sound reasons to think Congress
might doubt the efficacy or necessity of a damages remedy”
at all. Ziglar, 582 U. S., at ___ (slip op., at 13).
   In short, as we explained in Ziglar, a plaintiff cannot jus-
tify a Bivens extension based on “parallel circumstances”
with Bivens, Passman, or Carlson unless he also satisfies
the “analytic framework” prescribed by the last four dec-
ades of intervening case law. 582 U. S., at ___–___ (slip op.,
at 15–16). Boule has failed to do so.
                              IV
   Since it was decided, Bivens has had no shortage of de-
tractors. See, e.g., Bivens, 403 U. S., at 411 (Burger, C. J.,
dissenting); id., at 427 (Black, J., dissenting); id., at 430
(Blackmun, J., dissenting); Carlson, 446 U. S., at 31
(Rehnquist, J., dissenting); Malesko, 534 U. S., at 75
(Scalia, J., concurring); Hernández, 589 U. S., at ___
(THOMAS, J., concurring) (slip op., at 1); post, at 1–3 (opin-
ion of GORSUCH, J.). And, more recently, we have indicated
that if we were called to decide Bivens today, we would de-
cline to discover any implied causes of action in the Consti-
tution. See Ziglar, 582 U. S., at ___ (slip op., at 11). But, to
decide the case before us, we need not reconsider Bivens it-
self. Accordingly, we reverse the judgment of the Court of
Appeals.
                                               It is so ordered.
                 Cite as: 596 U. S. ____ (2022)            1

                   GORSUCH
              GORSUCH        , J., concurring
                     , J., concurring  in judgment

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 21–147
                          _________________


   ERIK EGBERT, PETITIONER v. ROBERT BOULE
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                         [June 8, 2022]

   JUSTICE GORSUCH, concurring in the judgment.
   Our Constitution’s separation of powers prohibits federal
courts from assuming legislative authority. As the Court
today acknowledges, Bivens v. Six Unknown Fed. Narcotics
Agents, 403 U. S. 388 (1971), crossed that line by
“impl[ying]” a new set of private rights and liabilities Con-
gress never ordained. Ante, at 5–6; see also Alexander v.
Sandoval, 532 U. S. 275, 286 (2001); Nestlé USA, Inc. v.
Doe, 593 U. S. ___, ___–___ (2021) (GORSUCH, J., concur-
ring) (slip op., at 4–7).
   Recognizing its misstep, this Court has struggled for dec-
ades to find its way back. Initially, the Court told lower
courts to follow a “two ste[p]” inquiry before applying
Bivens to any new situation. Ante, at 7. At the first step, a
court had to ask whether the case before it presented a “new
context” meaningfully different from Bivens. Ante, at 7. At
the second, a court had to consider whether “ ‘special fac-
tors’ ” counseled hesitation before recognizing a new cause
of action. Ibid. But these tests soon produced their own set
of questions: What distinguishes the first step from the sec-
ond? What makes a context “new” or a factor “special”?
And, most fundamentally, on what authority may courts
recognize new causes of action even under these standards?
   Today, the Court helpfully answers some of these linger-
ing questions. It recognizes that our two-step inquiry really
boils down to a “single question”: Is there “any reason to
2                     EGBERT v. BOULE

               GORSUCH, J., concurring in judgment

think Congress might be better equipped” than a court to
“ ‘weigh the costs and benefits of allowing a damages action
to proceed’ ”? Ante, at 7–8; see Ziglar v. Abbasi, 582 U. S.
120, ___–___ (2017) (slip op., at 13–14). But, respectfully,
resolving that much only serves to highlight the larger re-
maining question: When might a court ever be “better
equipped” than the people’s elected representatives to
weigh the “costs and benefits” of creating a cause of action?
    It seems to me that to ask the question is to answer it. To
create a new cause of action is to assign new private rights
and liabilities—a power that is in every meaningful sense
an act of legislation. See Sandoval, 532 U. S., at 286–287;
Nestlé, 593 U. S., at ___ (GORSUCH, J., concurring) (slip op.,
at 5); Jesner v. Arab Bank, PLC, 584 U. S. ___, ___ (2018)
(GORSUCH, J., concurring in part and concurring in judg-
ment) (slip op., at 3). If exercising that sort of authority
may once have been a “ ‘proper function for common-law
courts’ ” in England, it is no longer generally appropriate
“ ‘for federal tribunals’ ” in a republic where the people elect
representatives to make the rules that govern them. Sand-
oval, 532 U. S., at 287. Weighing the costs and benefits of
new laws is the bread and butter of legislative committees.
It has no place in federal courts charged with deciding cases
and controversies under existing law.
    Instead of saying as much explicitly, however, the Court
proceeds on to conduct a case-specific analysis. And there I
confess difficulties. The plaintiff is an American citizen
who argues that a federal law enforcement officer violated
the Fourth Amendment in searching the curtilage of his
home. Candidly, I struggle to see how this set of facts dif-
fers meaningfully from those in Bivens itself. To be sure, as
the Court emphasizes, the episode here took place near an
international border and the officer’s search focused on vio-
lations of the immigration laws. But why does that matter?
The Court suggests that Fourth Amendment violations
                  Cite as: 596 U. S. ____ (2022)             3

               GORSUCH, J., concurring in judgment

matter less in this context because of “likely” national-secu-
rity risks. Ante, at 11–12. So once more, we tote up for
ourselves the costs and benefits of a private right of action
in this or that setting and reach a legislative judgment. To
atone for Bivens, it seems we continue repeating its most
basic mistake.
   Of course, the Court’s real messages run deeper than its
case-specific analysis. If the costs and benefits do not jus-
tify a new Bivens action on facts so analogous to Bivens it-
self, it’s hard to see how they ever could. And if the only
question is whether a court is “better equipped” than Con-
gress to weigh the value of a new cause of action, surely the
right answer will always be no. Doubtless, these are the
lessons the Court seeks to convey. I would only take the
next step and acknowledge explicitly what the Court leaves
barely implicit. Sometimes, it seems, “this Court leaves a
door ajar and holds out the possibility that someone, some-
day might walk through it” even as it devises a rule that
ensures “no one . . . ever will.” Edwards v. Vannoy, 593
U. S. ___, ___ (2021) (GORSUCH, J., concurring) (slip op.,
at 1). In fairness to future litigants and our lower court col-
leagues, we should not hold out that kind of false hope, and
in the process invite still more “protracted litigation des-
tined to yield nothing.” Nestlé, 593 U. S., at ___ (GORSUCH,
J., concurring) (slip op., at 7). Instead, we should exercise
“the truer modesty of ceding an ill-gotten gain,” ibid., and
forthrightly return the power to create new causes of action
to the people’s representatives in Congress.
                 Cite as: 596 U. S. ____ (2022)            1

                   S
                   Opinion of S, OTOMAYOR
                    OTOMAYOR     J., dissenting
                                            , J.



SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 21–147
                          _________________


   ERIK EGBERT, PETITIONER v. ROBERT BOULE
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                         [June 8, 2022]

   JUSTICE SOTOMAYOR, with whom JUSTICE BREYER and
JUSTICE KAGAN join, concurring in the judgment in part
and dissenting in part.
   Respondent Robert Boule alleges that petitioner Erik Eg-
bert, a U. S. Customs and Border Patrol agent, violated the
Fourth Amendment by entering Boule’s property without a
warrant and assaulting him. Existing precedent permits
Boule to seek compensation for his injuries in federal court.
See Bivens v. Six Unknown Fed. Narcotics Agents, 403 U. S.
388 (1971); Ziglar v. Abbasi, 582 U. S. 120 (2017). The
Court goes to extraordinary lengths to avoid this result: It
rewrites a legal standard it established just five years ago,
stretches national-security concerns beyond recognition,
and discerns an alternative remedial structure where none
exists. The Court’s innovations, taken together, enable it
to close the door to Boule’s claim and, presumably, to others
that fall squarely within Bivens’ ambit.
   Today’s decision does not overrule Bivens. It neverthe-
less contravenes precedent and will strip many more indi-
viduals who suffer injuries at the hands of other federal of-
ficers, and whose circumstances are materially
indistinguishable from those in Bivens, of an important
remedy. I therefore dissent from the Court’s disposition of
Boule’s Fourth Amendment claim. I concur in the Court’s
judgment that Boule’s First Amendment retaliation claim
2                      EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

may not proceed under Bivens, but for reasons grounded in
precedent rather than this Court’s newly announced test.
                                I
   This case comes to the Court following the District
Court’s grant of summary judgment to Agent Egbert. The
Court is therefore bound to draw all reasonable factual in-
ferences in favor of Boule. See Tolan v. Cotton, 572 U. S.
650, 656–657 (2014) (per curiam). Because the Court fails
to do so, the factual record is described below in some detail,
in the light our precedent requires.
                              A
  Boule is a U. S. citizen who owns, operates, and lives in a
small bed-and-breakfast called the Smuggler’s Inn in
Blaine, Washington. The property line of the land on which
the inn is located touches the U. S.-Canada border. Shortly
after purchasing the property in 2000, Boule became aware
that people used his property to cross the border illegally in
both directions. Boule began serving as a paid, confidential
informant for Customs and Border Protection (CBP) in
2003 and for Immigration and Customs Enforcement (ICE)
in 2008. At the time of the events at issue in this case,
Boule was still serving as an informant for ICE. ICE would
coordinate with CBP and other agencies based on the infor-
mation Boule provided. Over the years, Boule provided in-
formation leading to numerous arrests.
  On the morning of March 20, 2014, petitioner Erik Eg-
bert, a CBP agent, twice stopped Boule while Boule was
running errands in town. Agent Egbert knew that Boule
was a long-time informant for ICE and that he had previ-
ously worked as an informant for CBP. Agent Egbert asked
Boule about guests at the inn, and Boule advised him of a
guest he expected to arrive that day from New York who
had flown in from Turkey the day before. Boule explained
that two of his employees were en route to pick the guest up
                 Cite as: 596 U. S. ____ (2022)           3

                   S
                   Opinion of S, OTOMAYOR
                    OTOMAYOR     J., dissenting
                                            , J.

at the Seattle-Tacoma International Airport. Agent Egbert
continued patrolling in his CBP vehicle for the rest of the
morning but stayed near the inn so he would see when the
car carrying the guest returned. When it arrived, he fol-
lowed the car into the driveway of the inn, passing a “no
trespassing” sign. Agent Egbert parked his vehicle behind
the arriving car in the driveway immediately adjacent to
the inn.
  Agent Egbert exited his patrol vehicle and approached
the car. Boule’s employee also exited the car; the guest re-
mained inside. From the front porch of his inn, Boule asked
Agent Egbert to leave. When Agent Egbert refused, Boule
stepped off the porch, positioned himself between Agent Eg-
bert and the vehicle, and explained that the person in the
car was a guest who had come from New York to Seattle
and who had been through security at the airport. Boule
again asked Agent Egbert to leave. Agent Egbert grabbed
Boule by his chest, lifted him up, and shoved him against
the vehicle and then threw him to the ground. Boule landed
on his hip and shoulder.
  Agent Egbert opened the car door and asked the guest
about his immigration status. Boule called 911 to request
a supervisor; Agent Egbert relayed the same request over
his radio. Several minutes later, a supervisor and another
agent arrived at the inn. After concluding that the guest
was lawfully in the country (just as Boule had previously
informed Agent Egbert), the three officers departed. Boule
later sought medical treatment for his injuries.
  Boule complained to Agent Egbert’s superiors about the
incident and filed an administrative claim with CBP, which
allegedly prompted Agent Egbert to retaliate against Boule.
Agent Egbert contacted the Internal Revenue Service (IRS),
the Social Security Administration, the Washington State
Department of Licensing, and the Whatcom County Asses-
sor’s Office, asking them to investigate Boule’s business.
These agencies did so, but none found that Boule had done
4                      EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

anything wrong. Boule paid over $5,000 to his accountant
to assist him in responding to the IRS’ tax audit. Boule also
filed claims pursuant to the Federal Tort Claims Act
(FTCA), which were denied. CBP’s investigation of Agent
Egbert concluded that he failed to be forthcoming with in-
vestigators and “demonstrated lack of integrity,” serious of-
fenses that warranted his removal. Rev. Redacted App.
184.
                              B
  Boule sued Agent Egbert in Federal District Court, seek-
ing damages under Bivens v. Six Unknown Fed. Narcotics
Agents, 403 U. S. 388, for violation of Boule’s First and
Fourth Amendment rights. The District Court granted
summary judgment to Agent Egbert on both claims. The
Court of Appeals reversed, concluding that both claims
were cognizable under Bivens. In the Court of Appeals’
view, Boule’s Fourth Amendment claim constituted a mod-
est extension of Bivens. Even so, the court explained, no
special factors counseled hesitation such that this extension
should be foreclosed; rather, “Boule’s Fourth Amendment
excessive force claim is part and parcel of the ‘common and
recurrent sphere of law enforcement’ ” that remained “a per-
missible area for Bivens claims.” 998 F. 3d 370, 389 (CA9
2021) (quoting Ziglar, 582 U. S., at ___ (slip op., at 11)). The
court separately held that Boule’s First Amendment claim
could proceed under Bivens.
  This Court granted certiorari. 595 U. S. ___ (2021).
                             II
                             A
  In Bivens, the plaintiff alleged that Federal Bureau of
Narcotics agents unlawfully entered his apartment in New
York City and used constitutionally unreasonable force to
arrest him. 403 U. S., at 389. This Court observed that an
“agent acting—albeit unconstitutionally—in the name of
                      Cite as: 596 U. S. ____ (2022)                      5

                        S
                        Opinion of S, OTOMAYOR
                         OTOMAYOR     J., dissenting
                                                 , J.

the United States possesses a far greater capacity for harm
than an individual trespasser exercising no authority other
than his own.” Id., at 392. The Fourth Amendment, the
Court explained, “guarantees to citizens of the United
States the absolute right to be free from unreasonable
searches and seizures carried out by virtue of federal au-
thority.” Ibid.
   The Court ultimately held that a “violation of [the Fourth
Amendment] by a federal agent acting under color of his
authority gives rise to a cause of action for damages.” Id.,
at 389. In doing so, the Court observed that existing state-
law causes of action were no substitute for a federal cause
of action because “[t]he interests protected by state laws
regulating trespass and the invasion of privacy” and those
protected by the Fourth Amendment “may be inconsistent
or even hostile.” Id., at 394; see also id., at 410 (Harlan, J.,
concurring in judgment) (“For people in Bivens’ shoes, it is
damages or nothing”).1 The Court also noted that the case
before it “involve[d] no special factors counselling hesita-
tion,” such as a question concerning federal fiscal policy.
Id., at 396.
   This Court has twice extended the cause of action first
articulated in Bivens: first to a Fifth Amendment due pro-
cess claim for sex discrimination, see Davis v. Passman, 442
U. S. 228 (1979), and then to an Eighth Amendment delib-
erate indifference claim for failure to provide proper medi-
cal attention, see Carlson v. Green, 446 U. S. 14 (1980). In
Davis, Carlson, and subsequent cases, the Court built on

——————
  1 For example, an individual “may bar the door against an unwelcome

private intruder, or call the police if he persists in seeking entrance” and
may seek damages under state law “for any consequent trespass.”
Bivens, 403 U. S., at 394. By contrast, “[t]he mere invocation of federal
power by a federal law enforcement official will normally render futile
any attempt to resist an unlawful entry or arrest by resort to the local
police; and a claim of authority to enter is likely to unlock the door as
well.” Ibid.
6                      EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

Bivens’ inquiry to develop a two-step test for determining
whether a Bivens cause of action may be “defeated.” Carl-
son, 446 U. S., at 18. First, the Court considered whether,
under the circumstances of a particular case, special factors
counseled hesitation in allowing a private right of action to
proceed. See, e.g., Bivens, 403 U. S., at 396; Davis, 442
U. S., at 246; Carlson, 446 U. S., at 18; Bush v. Lucas, 462
U. S. 367, 377–380 (1983). Second, the Court considered
whether “Congress has provided an alternative remedy
which it explicitly declared to be a substitute for recovery
directly under the Constitution and viewed as equally effec-
tive.” Carlson, 446 U. S., at 18–19; see also, e.g., Davis, 442
U. S., at 246–247; Bush, 462 U. S., at 377–378; Wilkie v.
Robbins, 551 U. S. 537, 550 (2007) (describing this two-step
test). Where, for example, Congress crafted an “elaborate
remedial system that has been constructed step by step,
with careful attention to conflicting policy considerations,”
Bush, 462 U. S., at 388, this Court concluded that “it would
be inappropriate . . . to supplement that regulatory scheme
with a new judicial remedy,” id., at 368; accord, Schweiker
v. Chilicky, 487 U. S. 412, 414 (1988). Applying this two-
step test, the Court has declined to extend Bivens beyond
situations like those addressed in Davis, Carlson, and
Bivens itself. See ante, at 1.
   In Ziglar v. Abbasi, 582 U. S. 120, the Court not only de-
clined to extend Bivens but also revised and narrowed its
two-step analytic framework. The Ziglar Court set forth a
new inquiry requiring courts considering a Bivens claim
first to ask whether a case “is different in a meaningful way
from previous Bivens cases decided by this Court” and
therefore arises in a “new . . . context.” 582 U. S., at ___
(slip op., at 16); see also Hernández v. Mesa, 589 U. S. ___,
___ (2020) (slip op., at 7). The Ziglar Court offered a laun-
dry list of differences that “might” be meaningful, including
“the rank of the officers involved; the constitutional right at
issue; the generality or specificity of the official action; the
                  Cite as: 596 U. S. ____ (2022)             7

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

extent of judicial guidance as to how an officer should re-
spond to the problem or emergency to be confronted; the
statutory or other legal mandate under which the officer
was operating; the risk of disruptive intrusion by the Judi-
ciary into the functioning of other branches; or the presence
of potential special factors that previous Bivens cases did
not consider.” 582 U. S., at ___ (slip op., at 16). The Court
recognized, however, that some differences “will be so triv-
ial that they will not suffice to create a new Bivens context.”
Id., at ___ (slip op., at 26).
  If the differences are in fact “meaningful ones,” ibid.,
“then the context is new,” id., at ___ (slip op., at 16), and a
court “proceed[s] to the second step” of the analysis, Her-
nández, 589 U. S., at ___ (slip op., at 7). The second step
requires courts to consider whether special factors counsel
hesitation in recognizing a Bivens remedy in a new context.
Ziglar, 582 U. S., at ___ (slip op., at 12); Hernández, 589
U. S., at ___ (slip op., at 7).
  Importantly, even as the Ziglar Court grafted a more de-
manding new-context inquiry onto the traditional Bivens
framework, the Court emphasized that its opinion was “not
intended to cast doubt on the continued force, or even the
necessity, of Bivens in the search-and-seizure context in
which it arose.” 582 U. S., at ___ (slip op., at 11). Quite the
opposite: The Court recognized that Bivens “vindicate[s] the
Constitution by allowing some redress for injuries” and
“provides instruction and guidance to federal law enforce-
ment officers going forward.” 582 U. S., at ___ (slip op., at
11). Accordingly, the Court explained, there are “powerful
reasons to retain [Bivens]” in the “common and recurrent
sphere of law enforcement.” Ibid. The Court further recog-
nized that “individual instances of discrimination or law en-
forcement overreach” are, by their nature, “difficult to ad-
dress except by way of damages actions after the fact.” Id.,
at ___ (slip op., at 21).
8                         EGBERT v. BOULE

                       S
                       Opinion of S, OTOMAYOR
                        OTOMAYOR     J., dissenting
                                                , J.

                             B
   Ziglar and Hernández control here. Applying the two-
step framework set forth in those cases, the Court of Ap-
peals’ determination that Boule’s Fourth Amendment claim
is cognizable under Bivens should be affirmed for two inde-
pendent reasons. First, Boule’s claim does not present a
new context. Second, even if it did, no special factors would
counsel hesitation.
                              1
   Boule’s Fourth Amendment claim does not arise in a new
context. Bivens itself involved a U. S. citizen bringing a
Fourth Amendment claim against individual, rank-and-file
federal law enforcement officers who allegedly violated his
constitutional rights within the United States by entering
his property without a warrant and using excessive force.
Those are precisely the facts of Boule’s complaint.
   The only arguably salient difference in “context” between
this case and Bivens is that the defendants in Bivens were
employed at the time by the (now-defunct) Federal Bureau
of Narcotics, while Agent Egbert was employed by CBP. As
discussed, however, this Court’s precedent instructs that
some differences are too “trivial . . . to create a new Bivens
context.” Ziglar, 582 U. S., at ___ (slip op., at 26).2 That it
was a CBP agent rather than a Federal Bureau of Narcotics
agent who unlawfully entered Boule’s property and used
constitutionally excessive force against him plainly is not
the sort of “meaningful” distinction that our new-context in-
quiry is designed to weed out. Ibid.
——————
    2 Egbert argues in passing that the fact that he was operating under a

“ ‘statutory . . . mandate’ not invoked in prior cases,” standing alone,
“dooms [Boule’s] no-new-context argument.” Reply Brief 19 (quoting
Ziglar, 582 U. S., at ___ (slip op., at 16)). Not so. Egbert fails to show
that any difference in statutory mandates as between CBP agents and
other law enforcement officers is “meaningful,” which our precedents re-
quire him to do. Id., at ___ (slip op., at 16).
                  Cite as: 596 U. S. ____ (2022)             9

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

   It is of course well established that a Bivens suit involv-
ing an entirely “ ‘new category of defendants’ ” arises in a
“ ‘new context.’ ” Ziglar, 582 U. S., at ___ (slip op., at 11);
see also Hernández, 589 U. S., at ___ (slip op., at 7). The
Court, however, has never relied on this principle to draw
artificial distinctions between line-level officers of the 83
different federal law enforcement agencies with authority
to make arrests and provide police protection. See Dept. of
Justice, C. Brooks, Federal Law Enforcement Officers,
2016—Statistical Tables (NCJ 251922, Oct. 2019),
https://bjs.ojp.gov/content/pub/pdf/fleo16st.pdf. Indeed, if
the “new context” inquiry were defined at such a fine level
of granularity, every case would raise a new context, be-
cause the Federal Bureau of Narcotics no longer exists. See
National Archives, Records of the Drug Enforcement Admin-
istration [DEA] (Aug. 15, 2016), https://www.archives.gov/
research/guide-fed-records/groups/170.html.
   Moreover, the “new category of defendants” language
traces back to a different concern raised in the Court’s de-
cision in Correctional Services Corp. v. Malesko, 534 U. S.
61, 68 (2001). That case involved an Eighth Amendment
claim brought by a federal prisoner against a private corpo-
ration under contract with the federal Bureau of Prisons.
The Court observed that “the threat of suit against an indi-
vidual’s employer,” rather than “the individual directly re-
sponsible for the alleged injury,” “was not the kind of deter-
rence contemplated by Bivens.” Id., at 70–71. Applying
Bivens to a corporate defendant would amount to a “marked
extension of Bivens . . . to contexts that would not advance
Bivens’ core purpose of deterring individual officers from
engaging in unconstitutional wrongdoing.” Malesko, 534
U. S., at 74; see also FDIC v. Meyer, 510 U. S. 471, 485
(1994) (declining to allow a Bivens claim to proceed against
a federal agency for similar reasons). Here, by contrast,
Boule’s suit against Agent Egbert directly advances that
core purpose.
10                      EGBERT v. BOULE

                     S
                     Opinion of S, OTOMAYOR
                      OTOMAYOR     J., dissenting
                                              , J.

  At bottom, Boule’s claim is materially indistinguishable
from the claim brought in Bivens. His case therefore does
not present a new context for the purposes of assessing
whether a Bivens remedy is available.
                                 2
   Even assuming that this case presents a new context, no
special factors warrant foreclosing a Bivens action.
   The Court “has not defined the phrase ‘special factors
counselling hesitation,’ ” but it has recognized that the “in-
quiry must concentrate on whether the Judiciary is well
suited, absent congressional action or instruction, to con-
sider and weigh the costs and benefits of allowing a dam-
ages action to proceed.” Ziglar, 582 U. S., at ___ (slip op.,
at 12); see also Hernández, 589 U. S., at ___–___ (slip op., at
7–8). For example, where a claim “would call into question
the formulation and implementation of a general policy” or
“require courts to interfere in an intrusive way with sensi-
tive functions of the Executive Branch,” recognizing a
Bivens action may be inappropriate. Ziglar, 582 U. S., at
___–___ (slip op., at 17–18); see also, e.g., Chappell v. Wal-
lace, 462 U. S. 296, 300 (1983) (declining to extend Bivens
where military personnel sought damages from superior of-
ficers, citing concerns about “tamper[ing] with the estab-
lished relationship between enlisted military personnel and
their superior officers,” which lies “at the heart of the nec-
essarily unique structure of the Military Establishment”).
Precedent thus establishes that “separation-of-powers prin-
ciples . . . should be central to the [special-factors] analysis.”
Ziglar, 582 U. S., at ___ (slip op., at 12).
   Here, the only possible special factor is that Boule’s prop-
erty abuts an international border. Boule’s case, however,
is a far cry from others in which the Court declined to ex-
tend Bivens for reasons of national security or foreign rela-
tions. In Hernández, for example, a CBP agent shot and
killed a Mexican child across the U. S.-Mexico border. 589
                  Cite as: 596 U. S. ____ (2022)            11

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

U. S., at ___ (slip op., at 2). The Mexican Government un-
successfully sought extradition of the agent to Mexico, and
after an investigation, the U. S. Department of Justice de-
clined to bring charges against the agent. Ibid. The par-
ents of the deceased child attempted to bring a Bivens ac-
tion against the CBP agent, but this Court held that several
“warning flags” counseled caution, including a “potential ef-
fect on foreign relations.” Hernández, 589 U. S., at ___ (slip
op., at 9). The Court observed that “[a] cross-border shoot-
ing is by definition an international incident,” and that both
the United States and Mexico had “legitimate and im-
portant interests that may be affected by the way in which
this matter is handled.” Id., at ___, ___ (slip op., at 9, 11).
The Court concluded that because “regulating the conduct
of agents at the border unquestionably has national secu-
rity implications, the risk of undermining border security
provides reason to hesitate before extending Bivens into
this field.” Id., at ___ (slip op., at 14).
   The conduct here took place near an international border
and involved a CBP agent. That, however, is where the
similarities with Hernández begin and end. The conduct
occurred exclusively on U. S. soil, and the injury was to a
U. S. citizen. This case therefore does not present an “in-
ternational incident” that might affect diplomatic relations,
unlike the cross-border killing of a foreign-national child.
As for national-security concerns, the Court in Hernández
emphasized that “some [CBP agents] are stationed right at
the border and have the responsibility of attempting to pre-
vent illegal entry”; it was “[f]or th[i]s reaso[n],” among oth-
ers, that their conduct had “a clear and strong connection
to national security.” Id., at ___ (slip op., at 13). Here, by
contrast, Agent Egbert was not “attempting to prevent ille-
gal entry” or otherwise engaged in activities with a “strong
connection to national security.” Ibid. Agent Egbert was
aware (because Boule had told him earlier in the day and
again at the scene) that the foreign national arriving at the
12                     EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

inn had already entered the United States by airplane and
had been processed by U. S. customs at the airport in New
York the previous day.
   Nor does this case present special factors similar to those
that deterred the Court from recognizing a Bivens action in
Ziglar. In that case, foreign nationals who had been unlaw-
fully present in the United States brought a Bivens action
against three “high executive officers in the Department of
Justice” and two wardens of the facility where they had
been held. Ziglar, 582 U. S., at ___ (slip op., at 2). The
Court reasoned that allowing the plaintiffs’ claims to pro-
ceed against the executive officers “would call into question
the formulation and implementation of a general policy,”
and that the discovery and litigation process would “border
upon or directly implicate the discussion and deliberations
that led to the formation of the policy in question,” thereby
implicating sensitive national-security functions entrusted
to Congress and the President. Id., at ___–___ (slip op., at
17–18). If Bivens liability were imposed, the Court ex-
plained, “high officers who face personal liability for dam-
ages might refrain from taking urgent and lawful action in
a time of crisis,” and “the costs and difficulties of later liti-
gation might intrude upon and interfere with the proper ex-
ercise of their office.” Ziglar, 582 U. S., at ___ (slip op., at
22).
   Here, Boule plainly does not seek to challenge or alter
“high-level executive policy.” Id., at ___ (slip op., at 16). Al-
lowing his claim to proceed would not require courts to in-
trude into “the discussion and deliberations that led to the
formation” of any policy or national-security decision or in-
terest. Id., at ___ (slip op., at 18). Agent Egbert, a line of-
ficer, was engaged in a run-of-the-mill inquiry into the sta-
tus of a foreign national on U. S. soil who had no actual or
suggested ties to terrorism, and who recently had been
through U. S. customs to boot. See id., at ___ (slip op., at
21) (distinguishing a challenge to “individual instances of
                   Cite as: 596 U. S. ____ (2022)             13

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

discrimination or law enforcement overreach,” which lends
itself to a Bivens action, from a challenge to “large-scale pol-
icy decisions,” which does not). No special factors counsel
against allowing Boule’s Bivens action to proceed.
                               C
   Boule also argues that his First Amendment retaliatory-
investigation claim is cognizable under Bivens. I concur in
the Court’s judgment that it is not, but I arrive at that con-
clusion by following precedent rather than by applying the
Court’s new, single-step inquiry. Ante, at 7; see infra, at
15–17.
   This Court has repeatedly assumed without deciding that
Bivens extends to First Amendment claims, see Wood v.
Moss, 572 U. S. 744, 757 (2014), but has never squarely held
as much, see Reichle v. Howards, 566 U. S. 658, 663, n. 4
(2012). Accordingly, Boule’s First Amendment retaliation
presents a new context for the purpose of the Bivens analy-
sis. See Ziglar, 582 U. S., at ___ (slip op., at 24) (noting that
a case can present a new context if it implicates a different
constitutional right than those already recognized as cog-
nizable under Bivens).
   Moving to the second step of the Bivens inquiry, unlike
Boule’s Fourth Amendment claim, there is “reason to
pause” before extending Bivens to Boule’s First Amendment
claim. Hernández, 589 U. S., at ___ (slip op., at 7). In par-
ticular, his First Amendment claim raises line-drawing con-
cerns similar to those this Court identified in Wilkie, 551
U. S. 537. In Wilkie, a landowner sought to bring a Bivens
action against federal officials whom the landowner ac-
cused of harassment and intimidation meant to extract an
easement across his property. 551 U. S., at 541. The Court
observed that “defining a workable cause of action” for such
a claim was “difficul[t].” Id., at 555; see also id., at 557.
Recognizing a Bivens action to redress retaliation under
such circumstances would, in the Court’s view, “invite
14                     EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

claims in every sphere of legitimate governmental action af-
fecting property interests” and “across this enormous swath
of potential litigation would hover the difficulty of devising
a . . . standard that could guide an employee’s conduct and
a judicial factfinder’s conclusion.” 551 U. S., at 561. Be-
cause of the “elusiveness of a limiting principle” for claims
like the landowner’s, id., at 561, n. 11, the Court decided
that courts were ill equipped to tailor an appropriate rem-
edy, id., at 562.
   Boule’s First Amendment retaliation claim raises similar
concerns. Unlike the constitutional rights this Court has
recognized as cognizable under Bivens, First Amendment
retaliation claims could potentially be brought against
many different federal officers, stretching substantially be-
yond the “common and recurrent sphere of law enforce-
ment” to reach virtually all federal employees. Ziglar, 582
U. S., at ___ (slip op., at 11). Under such circumstances,
this Court’s precedent holds that “ ‘evaluat[ing] the impact
of a new species of litigation’ ” on the efficiency of civil ser-
vice is a task for Congress, not the courts. Wilkie, 551 U. S.,
at 562; see also Ziglar, 582 U. S., at ___ (slip op., at 13). I
therefore concur in the judgment as to the Court’s reversal
of the Court of Appeals’ conclusion that Boule’s First
Amendment Bivens action may proceed, not for the reasons
the Court identifies, ante, at 13–16, but because precedent
requires it.
                            III
   If the legal standard the Court articulates to reject
Boule’s Fourth Amendment claim sounds unfamiliar, that
is because it is. Just five years after circumscribing the
standard for allowing Bivens claims to proceed, a restless
and newly constituted Court sees fit to refashion the stand-
ard anew to foreclose remedies in yet more cases. The
measures the Court takes to ensure Boule’s claim is dis-
missed are inconsistent with governing precedent.
                  Cite as: 596 U. S. ____ (2022)            15

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

                               A
   Two Terms ago, this Court reiterated and reaffirmed
Ziglar’s two-step test for assessing whether a claim may be
brought as a Bivens action. See Hernández, 589 U. S., at
___ (slip op., at 7) (“When asked to extend Bivens, we en-
gage in a two-step inquiry”). Today, however, the Court
pays lip service to the test set out in our precedents, but
effectively replaces it with a new single-step inquiry de-
signed to constrict Bivens. Ante, at 7 (acknowledging this
Court’s previous “two ste[p]” standard but insisting that
“those steps often resolve to a single question: whether
there is any reason to think that Congress might be better
equipped to create a damages remedy”); ante, at 8 (positing
that “[t]he newness of [some] ‘new context[s]’ should alone
require dismissal” (some internal quotation marks omit-
ted)). The Court goes so far as to announce that “[t]he
Bivens inquiry does not invite federal courts to inde-
pendently assess the costs and benefits of implying a cause
of action,” ante, at 11; instead, courts must “only” decide
“whether there is any rational reason (even one) to think
that Congress is better suited to ‘weigh the costs and bene-
fits of allowing a damages action to proceed,’ ” ibid. (quoting
Ziglar, 582 U. S., at ___ (slip op., at 12)).
   That approach contrasts starkly with the standard the
Court announced in Ziglar and applied in Hernández. This
Court regularly has considered whether courts are “well
suited . . . to consider and weigh the costs and benefits of
allowing a damages action to proceed,” Ziglar, 582 U. S., at
___ (slip op., at 12), and have never held that such weighing
is categorically impermissible, contrary to the Court’s anal-
ysis today. See also Wilkie, 551 U. S., at 554 (noting that
the Bivens inquiry asks courts to “weig[h] reasons for and
against the creation of a new cause of action”).
   The Court justifies its innovations by selectively quoting
our precedents and presenting its newly announced stand-
16                     EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

ard as if it were always the rule. The Court’s repeated cita-
tion to United States v. Stanley, 483 U. S. 669 (1987), is just
one example. The Court cites Stanley for, among other
things, the proposition that the special-factors analysis
must be conducted at a very broad level of generality. Ante,
at 11. Stanley, however, cautioned against a case-specific
special-factors analysis in the narrow context of “judicial in-
trusion upon military discipline.” 483 U. S., at 681. As it
had in previous cases seeking to raise Bivens actions in the
military context, the Stanley Court emphasized the need to
be “protective of military concerns,” 483 U. S., at 681, and
to avoid “call[ing] into question military discipline and de-
cisionmaking,” id., at 682. The Court therefore determined
that in the military sphere, the special-factors analysis
should be applied somewhat more broadly than the re-
spondent urged. Id., at 681. Stanley, in other words, re-
flected the Court’s longstanding approach to Bivens cases:
considering the facts and the substantive context of each
case and determining whether special factors counseled
hesitation. Stanley did not purport to articulate a special-
factors framework that should apply to all Bivens cases go-
ing forward.
   The Court further declares that “a plaintiff cannot justify
a Bivens extension based on ‘parallel circumstances’ ” with
previous cases that have recognized a Bivens remedy. Ante,
at 17. To the extent these statements suggest an exacting
new-context inquiry, they are in serious tension with the
Court’s longstanding rule that trivial differences alone do
not create a new Bivens context. See Ziglar, 582 U. S., at
___ (slip op., at 26); see also ante, at 2 (GORSUCH, J., concur-
ring in judgment) (“Candidly, I struggle to see how this set
of facts differs meaningfully from those in Bivens itself ”).
Indeed, until today, the Court has never so much as hinted
that courts should refuse to permit a Bivens action in a case
                     Cite as: 596 U. S. ____ (2022)                    17

                       S
                       Opinion of S, OTOMAYOR
                        OTOMAYOR     J., dissenting
                                                , J.

involving facts substantially identical to those in Bivens it-
self. Supra, at 8–9.3
                              B
   The Court’s application of its new standard to Boule’s
Fourth Amendment claim underscores just how novel that
standard is. Even assuming the claim presents a new con-
text, the Court’s insistence that national-security concerns
bar the claim directly contravenes Ziglar. Moreover, the
Court’s holding that a nonbinding administrative investi-
gation process, internal to the agency and offering no mean-
ingful protection of the constitutional interests at stake,
constitutes an alternative remedy that forecloses Bivens re-
lief blinks reality.
                               1
   The Court acknowledges the force of the Court of Appeals’
conclusion that Bivens and this case present “ ‘almost par-
allel circumstances,’ ” but it nonetheless concludes that a
most unlikely special factor counsels hesitation: the
“national-security context.” Ante, at 10. By the Court’s tell-
ing, Hernández declined to recognize a Bivens action “be-
cause ‘regulating the conduct of agents at the border un-
questionably has national security implications,’ and the
‘risk of undermining border security provides reason to hes-
itate before extending Bivens into this field.’ ” Ante, at 9
——————
   3 The Court supports its decision not to recognize an action under

Bivens v. Six Unknown Fed. Narcotics Agents, 403 U. S. 388 (1971), by
observing that we have declined to recognize a Bivens-style cause of ac-
tion for other constitutional violations. Ante, at 1. What the Court fails
to acknowledge, however, is that each of those cases presented a mean-
ingfully new context and/or raised special factors counseling hesitation
that are not present in this case. See supra, at 6, 9–10, 13–14, 15–16;
infra, at 21–22. The one exception is Hui v. Castaneda, 559 U. S. 799,
808 (2010), in which the Court did not have to conduct this analysis be-
cause it held the FTCA’s comprehensive remedial scheme, which pro-
vided both a cause of action and an exclusive damages remedy for the
claim at issue, clearly precluded a Bivens claim.
18                     EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

(quoting Hernández, 589 U. S., at ___ (slip op., at 14)). That
reasoning, the Court concludes, “applies here with full
force” because “national security is at issue.” Ante, at 9–10.
   This is sheer hyperbole. Most obviously, the Court’s con-
clusion that this case, which involves a physical assault by
a federal officer against a U. S. citizen on U. S. soil, raises
“national security” concerns does exactly what this Court
counseled against just four years ago. Back then, the Court
advised that “national-security concerns must not become a
talisman to use to ward off inconvenient claims—a ‘label’
used to ‘cover a multitude of sins.’ ” Ziglar, 582 U. S., at ___
(slip op., at 20) (quoting Mitchell v. Forsyth, 472 U. S. 511,
523 (1985)). It explained that this “danger of abuse is even
more heightened given the difficulty of defining the security
interest in domestic cases.” Ziglar, 582 U. S., at ___ (slip
op., at 20) (internal quotation marks omitted). This case
does not remotely implicate national security. The Court
may wish it were otherwise, but on the facts of this case, its
effort to raise the specter of national security is mere sleight
of hand.
   Nor is there any indication that Congress acted to deny a
Bivens remedy for a case like this, which otherwise might
counsel hesitation. See Bush, 462 U. S., at 368 (declining
to “supplement” Congress’ existing scheme “with a new ju-
dicial remedy”). Congress has not provided that federal law
enforcement officers may enter private property near a bor-
der at any time or for any purpose. Quite the contrary: Con-
gress has determined that immigration officers may enter
“private lands” within 25 miles of an international border
without a warrant only “for the purpose of patrolling the
border to prevent the illegal entry of aliens into the United
States.” 66 Stat. 233, 8 U. S. C. §1357(a)(3). This allowance
is itself subject to exceptions: Officers cannot enter a
“dwellin[g]” for immigration enforcement purposes without
a warrant. Ibid. Mere proximity to a border, in other
words, did not give Agent Egbert greater license to enter
                    Cite as: 596 U. S. ____ (2022)                  19

                      S
                      Opinion of S, OTOMAYOR
                       OTOMAYOR     J., dissenting
                                               , J.

Boule’s property. Nor does it diminish or call into question
the remedies for constitutional violations that a plaintiff
may pursue, particularly where, as here, an agent unques-
tionably was not acting “for the purpose of patrolling the
border to prevent the illegal entry of aliens into the United
States.” Ibid.
   Remarkably, the Court goes beyond invoking its national-
security talisman in this case alone. In keeping with the
unprecedented level of generality the Court imports into
the special-factors analysis, the Court holds that courts are
not “competent to authorize a damages action . . . against
Border Patrol agents generally.” Ante, at 11. This extraor-
dinary and gratuitous conclusion contradicts decades of
precedent requiring a context-specific determination of
whether a particular claim presents special factors counsel-
ing hesitation. See supra, at 6–8.4
   The consequences of the Court’s drive-by, categorical as-
sertion will be severe. Absent intervention by Congress,
CBP agents are now absolutely immunized from liability in
any Bivens action for damages, no matter how egregious the
misconduct or resultant injury. That will preclude redress
under Bivens for injuries resulting from constitutional vio-
lations by CBP’s nearly 20,000 Border Patrol agents, in-
cluding those engaged in ordinary law enforcement activi-
ties, like traffic stops, far removed from the border. U. S.
Customs and Border Protection, On a Typical Day in
Fiscal Year 2021, CBP . . . (2022), https://www.cbp.gov/
newsroom/stats/typical-day-fy2021. This is no hypothet-
ical: Certain CBP agents exercise broad authority to make
warrantless arrests and search vehicles up to 100 miles
away from the border. See 8 U. S. C. §1357(a); 8 CFR
——————
  4 Any concerns that a case-specific Bivens inquiry in cases involving

CBP or ICE agents would pose administrability problems is misplaced.
See Brief for American Civil Liberties Union et al. as Amici Curiae 14–
18 (citing lower court cases that have applied this approach to suits
against CBP and ICE agents).
20                         EGBERT v. BOULE

                        S
                        Opinion of S, OTOMAYOR
                         OTOMAYOR     J., dissenting
                                                 , J.

§287.1(a)(2) (2021). The Court’s choice to foreclose liability
for constitutional violations that occur in the course of such
activities, based on even the most tenuous and hypothetical
connection to the border (and thereby, to the “national-
security context”), betrays the context-specific nature of
Bivens and shrinks Bivens in the core Fourth Amendment
law enforcement sphere where it is needed most. See
Ziglar, 582 U. S., at ___ (slip op., at 11).5
                              2
  The Court further proclaims that Congress has provided
alternative remedies that “independently foreclose” a
Bivens action in this case. Ante, at 12. The administrative
remedy the Court perceives, however, is no remedy whatso-
ever.
  The sole “remedy” the Court cites is an administrative
grievance procedure that does not provide Boule with any
relief. The statute on which the Court relies provides: The
“Secretary of Homeland Security . . . shall have control, di-
rection, and supervision of all employees and of all the files
and records of [CBP].” 8 U. S. C. §1103(a)(2); see ante, at
12. Administrative regulations direct CBP to investigate
alleged violations of its own standards by its own employ-
ees. See 8 CFR §§287.10(a)–(b).6 The Court sees fit to defer
——————
   5 To the extent the Court’s decision may be motivated by fears that al-

lowing this Bivens action to proceed will open the floodgates to countless
claims in the future, cf. ante, at 15, that concern is overblown. The doc-
trine of qualified immunity will continue to protect government officials
from liability for damages unless a plaintiff “ ‘pleads facts showing (1)
that the official violated a statutory or constitutional right, and (2) that
the right was “clearly established” at the time of the challenged con-
duct.’ ” Wood v. Moss, 572 U. S. 744, 757 (2014) (quoting Ashcroft v. al-
Kidd, 563 U. S. 731, 735 (2011)).
   6 The regulations require any investigative report regarding excessive

force to “be referred promptly for appropriate action in accordance with
the policies and procedures of the Department [of Homeland Security].”
8 CFR §287.10(c). Those policies and procedures, in turn, explicitly es-
tablish no “right or benefit, substantive or procedural, enforceable at law
                    Cite as: 596 U. S. ____ (2022)                21

                      S
                      Opinion of S, OTOMAYOR
                       OTOMAYOR     J., dissenting
                                               , J.

to this procedure, even while acknowledging that complain-
ants in Boule’s position have no right to participate in the
proceedings or to seek judicial review of any determination.
Ante, at 12. The Court supports its conclusion that CBP’s
internal administrative grievance procedure offers an ade-
quate remedy by insisting that “we have never held that a
Bivens alternative must afford rights to participation or ap-
peal.” Ante, at 13. In the Court’s view, “[s]o long as Con-
gress or the Executive has created a remedial process that
it finds sufficient to secure an adequate level of deterrence,
the courts cannot second-guess that calibration by superim-
posing a Bivens remedy.” Ibid. (emphasis added).
   This analysis drains the concept of “remedy” of all mean-
ing. To be sure, the Court has previously deemed Bivens
claims foreclosed by “substantive” remedies to claimants
that are in significant part administrative. Bush, 462 U. S.,
at 385; see also, e.g., Schweiker, 487 U. S., at 424–425. The
Court also has recognized that existing remedies need not
“provide complete relief for the plaintiff,” Bush, 462 U. S.,
at 388, including loss due to emotional distress or mental
anguish, or attorney’s fees, Schweiker, 487 U. S., at 424–
425. Until today, however, this Court has never held that
a threadbare disciplinary review process, expressly confer-
ring no substantive rights, “secure[s] adequate deterrence
and afford[s] . . . an alternative remedy.” Ante, at 14. Nor
has it held that remedies providing no relief to the individ-
ual whose constitutional rights have been violated are “ad-
equate” for the purpose of foreclosing a Bivens action. To
the contrary, each of the alternative remedies the Court has
recognized has afforded participatory rights, an oppor-
tunity for judicial review, and the potential to secure at
least some meaningful relief. See, e.g., Minneci v. Pollard,
565 U. S. 118, 127 (2012) (state tort law); Ziglar, 582 U. S.,
——————
or in equity.” Dept. of Homeland Security, Dept. Policy on the Use of
Force, §X, Policy Statement 044–05 (Sept. 7, 2018).
22                        EGBERT v. BOULE

                       S
                       Opinion of S, OTOMAYOR
                        OTOMAYOR     J., dissenting
                                                , J.

at ___ (slip op., at 25) (petition for writ of habeas corpus or
injunctive relief ); Bush, 462 U. S., at 385.7
   The Court previously has emphasized that a Bivens ac-
tion may be inappropriate where “Congress has provided an
alternative remedy which it explicitly declared to be a sub-
stitute for recovery directly under the Constitution and
viewed as equally effective.” Carlson, 446 U. S., at 18–19
(emphasis deleted). Thus, our cases declining to extend
Bivens have done so where Congress, sometimes in conjunc-
tion with the Executive Branch, provided “comprehensive”
and meaningful remedies. Bush, 462 U. S., at 388; see also
Schweiker, 487 U. S., at 414, 423, 428 (emphasizing that
the “design” of the “elaborate remedial scheme” in the So-
cial Security disability program “suggests that Congress
has provided what it considers adequate remedial mecha-
nisms for constitutional violations that may occur in the
course of its administration”); Malesko, 534 U. S., at 72
(noting that remedies available to the plaintiff were “at
least as great, and in many respects greater, than anything

——————
   7 Aside from CBP’s internal grievance procedure, Agent Egbert con-

tends that the FTCA offers an alternative remedy for claims like Boule’s.
This Court does not endorse this argument, and for good reason. This
Court repeatedly has observed that the FTCA does not cover claims
against Government employees for “violation[s] of the Constitution of the
United States.” 28 U. S. C. §2679(b)(2)(A); see Wilkie v. Robbins, 551
U. S. 537, 553 (2007); Carlson v. Green, 446 U. S. 14, 20 (1980) (“Con-
gress views FTCA and Bivens as parallel, complementary causes of ac-
tion”); Correctional Services Corp. v. Malesko, 534 U. S. 61, 68 (2001)
(noting that it was “crystal clear” that “Congress intended the FTCA and
Bivens to serve as parallel and complementary sources of liability” (in-
ternal quotation marks omitted)). Just two Terms ago, the Court reaf-
firmed that by carving out claims “ ‘brought for . . . violation[s] of the
Constitution’ ” from the FTCA’s “ ‘exclusive remedy for most claims
against Government employees arising out of their official conduct,’ ”
“Congress made clear that it was not attempting to abrogate Bivens” and
instead “simply left Bivens where it found it,” Hernández v. Mesa, 589
U. S. ___, ___–___,
               ֪    and n. 9 (2020) (slip op., at 16–17, and n. 9) (quoting
Hui, 559 U. S., at 806; §2679(b)(2)(A)).
                     Cite as: 596 U. S. ____ (2022)                  23

                      S
                      Opinion of S, OTOMAYOR
                       OTOMAYOR     J., dissenting
                                               , J.

that could be had under Bivens”); Minneci, 565 U. S., at 120
(rejecting Bivens action for Eighth Amendment violations
against employees of a privately operated federal prison be-
cause “state tort law authorizes adequate alternative dam-
ages actions—actions that provide both significant deter-
rence and compensation”). By the Court’s logic, however,
the existence of any disciplinary framework, even if crafted
by the Executive Branch rather than Congress, and even if
wholly nonparticipatory and lacking any judicial review, is
sufficient to bar a court from recognizing a Bivens remedy.
That reasoning, as disturbing as it is wrong, marks yet an-
other erosion of Bivens’ deterrent function in the law en-
forcement sphere.8
                                C
   The Court thinly veils its disapproval of Bivens, ending
its opinion by citing a string of dissenting opinions and
single-Member concurrences by various Members of this
Court expressing criticisms of Bivens. Ante, at 16–17. But
the Court unmistakably stops short of overruling Bivens
and its progeny, and appropriately so. Even while declining
to extend Bivens to new contexts, this Court has reaffirmed
that it did “not inten[d] to cast doubt on the continued force,
or even the necessity, of Bivens in the search-and-seizure
context in which it arose.” Ziglar, 582 U. S., at ___ (slip op.,
at 11). Although today’s opinion will make it harder for
plaintiffs to bring a successful Bivens claim, even in the
Fourth Amendment context, the lower courts should not
read it to render Bivens a dead letter.
   That said, the Court plainly modifies the Bivens standard
in a manner that forecloses Boule’s claims and others like
them that should be permitted under this Court’s Bivens
——————
  8 Even beyond its doctrinal innovations on the merits, the Court also

fashions a brand new, Bivens-specific procedural rule under which it ex-
cuses Egbert’s forfeiture of his argument that CBP’s administrative pro-
cess suffices as an alternative remedy. Ante, at 12, n. 3.
24                     EGBERT v. BOULE

                    S
                    Opinion of S, OTOMAYOR
                     OTOMAYOR     J., dissenting
                                             , J.

precedents. That choice is in tension with the Court’s in-
sistence that “prescribing a cause of action is a job for Con-
gress, not the courts.” Ante, at 1; see ante, at 11 (cautioning
against “frustrat[ing] Congress’s policymaking role” when
considering whether special factors counsel hesitation).
Faithful adherence to this logic counsels maintaining
Bivens in its current scope, but does not support changing
the status quo to constrict Bivens, as the Court does today.
Congress, after all, has recognized and relied on the Bivens
cause of action in creating and amending other remedies,
including the FTCA. By nevertheless repeatedly amending
the legal standard that applies to Bivens claims and whit-
tling down the number of claims that remain viable, the
Court itself is making a policy choice for Congress. What-
ever the merits of that choice, the Court’s decision today is
no exercise in judicial modesty.
                          *     *    *
  This Court’s precedents recognize that suits for damages
play a critical role in deterring unconstitutional conduct by
federal law enforcement officers and in ensuring that those
whose constitutional rights have been violated receive
meaningful redress. The Court’s decision today ignores our
repeated recognition of the importance of Bivens actions,
particularly in the Fourth Amendment search-and-seizure
context, and closes the door to Bivens suits by many who
will suffer serious constitutional violations at the hands of
federal agents. I respectfully dissent from the Court’s treat-
ment of Boule’s Fourth Amendment claim.

```

---

## GROUP: content/cases/Elkins v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Elkins v. United States"
type: case
citation: "364 U.S. 206 (1960)"
parallel_cite: "80 S. Ct. 1437; 4 L. Ed. 2d 1669"
neutral_cite: 1960 U.S. LEXIS 1989
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1960
date_decided: 1960-06-27
docket: 126
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1960-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Elkins v. United States
  varies_by_point: false
  scope_note: "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106107/elkins-v-united-states/"
  cluster_id: 106107
  opinion_id: 9422064
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Anchor (silver-platter abolition; deterrence rationale)"
related: ["[[Weeks v. United States]]", "[[Mapp v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "silver-platter", "deterrence", "federalism"]
holding: "The 'silver-platter' doctrine is abolished: evidence obtained by state officers in a search that would violate the Fourth Amendment if conducted by federal officers is inadmissible in a federal criminal trial, because the exclusionary rule's purpose is to deter unconstitutional searches by removing the incentive to make them."
lake:
  record_id: Elkins v. United States
  status: verified
  projected_at: 2026-07-06
---

# Elkins v. United States

*364 U.S. 206 (1960)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
State officers searched Elkins and seized evidence that a federal court had found was obtained unlawfully; the state prosecution was dropped. Federal officers then obtained the items and Elkins was prosecuted federally. Under the then-prevailing "silver-platter" doctrine, evidence unconstitutionally seized by *state* officers (without federal participation) could still be handed to federal prosecutors and used in federal court. Elkins objected to its admission.

## Issue
Whether evidence obtained through an unreasonable search and seizure by state officers, without federal involvement, may be admitted against a defendant in a federal criminal trial.

## Rule
No. The silver-platter doctrine is abolished. "[W]e re-examine here the validity of what has come to be called the silver platter doctrine. … [W]e conclude that this doctrine can no longer be accepted." — 364 U.S. at 208. ^pin-208

The exclusionary rule rests on deterrence: "The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way — by removing the incentive to disregard it." — *Id.* at 217. ^pin-217

"[W]e hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial." — *Id.* at 223. ^pin-223

## Application
Because the items used against Elkins had been seized by state officers in a manner that would have violated the Fourth Amendment had federal officers done it, they could not be admitted in his federal prosecution. The Court added that a federal court must make an independent inquiry into the lawfulness of the state seizure under federal standards, regardless of any state-court ruling.

## Conclusion
The silver-platter doctrine was rejected; the unconstitutionally state-seized evidence was inadmissible in federal court, and the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Elkins* was decided the term before *[[Mapp v. Ohio]]* (1961), which made the exclusionary rule binding on the states and so largely mooted the silver-platter problem. *Elkins*'s articulation of the exclusionary rule's **deterrence purpose** remains foundational and is repeatedly invoked in later good-faith and cost-benefit cases.

## Appears on
- [[The Exclusionary Rule]] — *Anchor (silver-platter abolition; deterrence rationale)*

## Sources
- *Elkins v. United States*, 364 U.S. 206 (1960) — https://www.courtlistener.com/opinion/106107/elkins-v-united-states/ — pinpoints: 208, 217, 223.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6f7c14217643207a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "364 U.S. 206 (1960)", "court": "U.S. Supreme Court", "neutral_cite": "1960 U.S. LEXIS 1989", "official_citation_present": true, "parallel_cite": "80 S. Ct. 1437; 4 L. Ed. 2d 1669", "title": "Elkins v. United States", "year": "1960"}}
{"assertion_id": "086396ff6192d8c3", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The 'silver-platter' doctrine is abolished: evidence obtained by state officers in a search that would violate the Fourth Amendment if conducted by federal officers is inadmissible in a federal criminal trial, because the exclusionary rule's purpose is to deter unconstitutional searches by removing the incentive to make them.", "title": "Elkins v. United States"}}
{"assertion_id": "645d98eaf80aee97", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Anchor (silver-platter abolition; deterrence rationale)", "title": "Elkins v. United States"}}
{"assertion_id": "8c459e36c281f107", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Elkins v. United States"}}
{"assertion_id": "d607d4e85a4569ff", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1960-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Elkins v. United States", "field_i_validity": "good_law", "scope_note": "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited.", "title": "Elkins v. United States", "varies_by_point": "false"}}
```

### lake record — Elkins v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Elkins v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Elkins v. United States",
    "case_name_short": "Elkins",
    "case_name_full": "ELKINS Et Al. v. UNITED STATES",
    "input_case_name": "Elkins v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1960-06-27",
    "year": 1960,
    "docket": "126",
    "cluster_id": 106107,
    "lead_opinion_id": 9422064,
    "sibling_ids": [
      106107,
      9422064,
      9422065
    ],
    "absolute_url": "/opinion/106107/elkins-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "364 U.S. 206",
      "volume": "364",
      "reporter": "U.S.",
      "page": "206",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "80 S. Ct. 1437",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "1437",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 1669",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "1669",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1960 U.S. LEXIS 1989",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1989",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "364 U.S. 206",
        "volume": "364",
        "reporter": "U.S.",
        "page": "206",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 S. Ct. 1437",
        "volume": "80",
        "reporter": "S. Ct.",
        "page": "1437",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 L. Ed. 2d 1669",
        "volume": "4",
        "reporter": "L. Ed. 2d",
        "page": "1669",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1960 U.S. LEXIS 1989",
        "volume": "1960",
        "reporter": "U.S. LEXIS",
        "page": "1989",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "364 U.S. 206",
    "official_selection": {
      "court_class": "scotus",
      "selected": "364 U.S. 206",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-208",
      "page": null,
      "quote": "doctrine, evidence unconstitutionally seized by *state* officers (without federal participation) could still be handed to federal prosecutors and used in federal court. Elkins objected to its admission. ## Issue Whether evidence obtained through an unreasonable search and seizure by state officers, without federal involvement, may be admitted against a defendant in a federal criminal trial. ## Rule No. The silver-platter doctrine is abolished.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-217",
      "page": null,
      "quote": "The rule is calculated to prevent, not to repair. Its purpose is to deter \u2014 to compel respect for the constitutional guaranty in the only effectively available way \u2014 by removing the incentive to disregard it.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-223",
      "page": null,
      "quote": "[W]e hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant's immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant's timely objection in a federal criminal trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1960-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Elkins v. United States",
    "varies_by_point": false,
    "scope_note": "Good law. Decided the term before Mapp v. Ohio, which extended the exclusionary rule to the states and largely mooted the silver-platter problem; Elkins's deterrence rationale for the exclusionary rule remains foundational and is widely cited.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
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
        "journal_ref": "Elkins v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4371038,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane1_negative"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gideon v. Wainwright",
          "cluster_id": 106545,
          "cite": [
            "9 L. Ed. 2d 799",
            "83 S. Ct. 792",
            "372 U.S. 335",
            "1963 U.S. LEXIS 1942",
            "93 A.L.R. 2d 733",
            "23 Ohio Op. 2d 258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Monroe v. Pape",
          "cluster_id": 106170,
          "cite": [
            "5 L. Ed. 2d 492",
            "81 S. Ct. 473",
            "365 U.S. 167",
            "1961 U.S. LEXIS 1687"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nixon",
          "cluster_id": 109101,
          "cite": [
            "41 L. Ed. 2d 1039",
            "94 S. Ct. 3090",
            "418 U.S. 683",
            "1974 U.S. LEXIS 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
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
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preston v. United States",
          "cluster_id": 106771,
          "cite": [
            "11 L. Ed. 2d 777",
            "84 S. Ct. 881",
            "376 U.S. 364",
            "1964 U.S. LEXIS 1578"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Nobles",
          "cluster_id": 109292,
          "cite": [
            "45 L. Ed. 2d 141",
            "95 S. Ct. 2160",
            "422 U.S. 225",
            "1975 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Elkins v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106107 OR 9422064 OR 9422065) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjkwMDM4NDAwMDAwJnM9MzEzNTU2MyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106107+OR+9422064+OR+9422065%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106107 OR 9422064 OR 9422065)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OTEmcz0xMDU3NjE4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106107+OR+9422064+OR+9422065%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106107 OR 9422064 OR 9422065)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 1,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106107 OR 9422064 OR 9422065)",
    "indexed_citing_opinions": 1628,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106107,
        "count": 1501,
        "count_source": "search"
      },
      {
        "opinion_id": 9422064,
        "count": 178,
        "count_source": "search"
      },
      {
        "opinion_id": 9422065,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2501,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/elkins-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTk2MTkmcz05NDgxNjY5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106107+OR+9422064+OR+9422065%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106107,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104006,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105857,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 105880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 234366,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 234773,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 235212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 239614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 239813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 240496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 242217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 246433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 248020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 249351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1118348,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1122381,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1174129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1178849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1199500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1209203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1328981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1380217,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1401576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1472688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1475515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1476789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1480891,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1483661,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1489412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1490225,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1493506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1498347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1501575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1501987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1502497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1505389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1508855,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1508963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1509635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1545838,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1548044,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1549055,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1660499,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1670307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1680451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1837215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1921065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 1934063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2019054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2022531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2030212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2030951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2041058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2041065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2146371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2190973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2199709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2228330,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2352643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2466177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2615411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 2619395,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3233534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3246119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3302902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3307559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3311672,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3321660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3412636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3484807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3487094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3517292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3529427,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3534889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3553875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3571966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3580565,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3588018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3646527,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3672959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3682031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3780866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3812264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3827556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3842073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3848320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3924432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3948208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3980535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 3990360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4002892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4012045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106107,
        "cited_id": 4012941,
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
    "date_created": "2026-07-05T03:11:05Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:16:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:11:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Elkins v. United States

```
<opinion type="majority">
<author id="b280-14">Mr. Justice Stewart</author>
<p id="APZ">delivered the opinion of the Court.</p>
<p id="b280-15">The petitioners were indicted in the United States District Court in Oregon for the offense of intercepting and divulging telephone communications and of conspiracy to do so. <span class="citation no-link">47 U. S. C. §§ 501</span>, 605; <span class="citation no-link">18 U. S. C. § 371</span>. Before trial the petitioners made a motion to suppress as evidence several tape and wire recordings and <page-number citation-index="1" label="207">*207</page-number>a recording machine, which had originally been seized by state law enforcement officers in the home of petitioner Clark under circumstances which, two Oregon courts had found, had rendered the search and seizure unlawful.<footnotemark>1</footnotemark> At the hearing on the motion the district judge assumed without deciding that the articles had been obtained as the result of an unreasonable search and seizure, but denied the motion to suppress because there was no evidence that any “agent of the United States had any knowledge or information or suspicion of any kind that this search was being contemplated or was eventually made by the State officers until they read about it in the newspaper.” At the trial the articles in question were admitted in evidence against the petitioners, and they were convicted.</p>
<p id="b282-5"><page-number citation-index="1" label="208">*208</page-number>The convictions were affirmed by the Court of Appeals for the Ninth Circuit, <span class="citation" data-id="248020"><a href="/opinion/248020/james-butler-elkins-and-raymond-frederick-clark-v-united-states/" aria-description="Citation for case: James Butler Elkins and Raymond Frederick Clark v. United...">266 F. 2d 588</a></span>. That court agreed with the district judge that it was unnecessary to determine whether or not the original state search and seizure had been lawful, because there had been no participation by federal officers. “Hence the unlawfulness of the State search and seizure, if indeed they were unlawful, did not entitle defendants to an order of the .District Court suppressing the property seized.” <span class="citation" data-id="248020"><a href="/opinion/248020/james-butler-elkins-and-raymond-frederick-clark-v-united-states/#594" aria-description="Citation for case: James Butler Elkins and Raymond Frederick Clark v. United...">266 F. 2d, at 594</a></span>.</p>
<p id="b282-6">We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./361/810/">361 U. S. 810</a></span>, to consider a question of importance in the administration of federal justice. The question is this: May articles obtained as the result of an unreasonable search and seizure by state officers, without involvement of federal officers, be introduced in evidence against a defendant over his timely objection in a federal criminal trial? In a word, we re-examine here the validity of what has come to be called the silver platter doctrine.<footnotemark>2</footnotemark> For the reasons that follow we conclude that this doctrine can no longer be accepted.</p>
<p id="b282-7">To put the issue in historic perspective, the appropriate starting point must be <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. <page-number citation-index="1" label="209">*209</page-number>383</a></span>, decided in 1914. It was there that the Court established the rule which excludes in a federal criminal prosecution evidence obtained by federal agents in violation of the defendant's Fourth Amendment rights. The foundation for that decision was set out in forthright words:</p>
<blockquote id="b283-5">“The effect of the Fourth Amendment is to put the courts of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law. This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws. The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures and enforced confessions, the latter often obtained after subjecting accused persons to unwarranted practices destructive of rights secured by the Federal Constitution, should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.</blockquote>
<blockquote id="b283-6">“. . . If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts <page-number citation-index="1" label="210">*210</page-number>of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#391" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 391-393</a></span>.</blockquote>
<p id="b284-6">To the exclusionary rule of <em>Weeks </em>v. <em>United States </em>there has been unquestioning adherence for now almost half a century. See <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>; <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <em>Amos </em>v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>; <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <em>Grau </em>v. <em>United States, </em><span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U. S. 124</a></span>; <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <em>United States v. Jeffers, </em><span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>.</p>
<p id="b284-7">But the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>case also announced, unobtrusively but nonetheless definitely, another evidentiary rule. Some of the articles used as evidence against Weeks had been unlawfully seized by local police officers acting on their own account. The Court held that the admission of this evidence was not error for the reason that “the Fourth Amendment is not directed to individual misconduct of such officials. Its limitations reach the Federal Government and its agencies.” <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S., at 398</a></span>. Despité the limited discussion of this second ruling in the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>opinion, the right of the prosecutor in a federal criminal trial to avail himself of evidence unlawfully seized by state officers apparently went unquestioned for the next thirty-five years. See, <em>e. g., Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 33</a></span>; <em>Feldman </em>v. <em>United States, </em><span class="citation" data-id="9419517"><a href="/opinion/104006/feldman-v-united-states/#492" aria-description="Citation for case: Feldman v. United States">322 U. S. 487, 492</a></span>.<footnotemark>3</footnotemark></p>
<p id="b285-4"><page-number citation-index="1" label="211">*211</page-number>That such a rule would engender practical difficulties in an era of expanding federal criminal jurisdiction could not, perhaps, have been foreseen. In any event the difficulties soon appeared. They arose from the entirely commendable practice of state and federal agents to cooperate with each other in the investigation and detection of criminal activity. When in a federal criminal prosecution evidence which had been illegally seized by state officers was sought to be introduced, the question inevitably arose whether there had been such participation by federal agents in the search and seizure as to make applicable the exclusionary rule of <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>. </em>See <em>Flagg </em>v. <em>United States, </em><span class="citation" data-id="8799726"><a href="/opinion/8815246/flagg-v-united-states/#483" aria-description="Citation for case: Flagg v. United States">233 Fed. 481, 483</a></span>; <em>United States </em>v. <em>Slusser, </em><span class="citation" data-id="8819339"><a href="/opinion/8834327/united-states-v-slusser/#820" aria-description="Citation for case: United States v. Slusser">270 Fed. 818, 820</a></span>; <em>United States </em>v. <em>Falloco, </em><span class="citation" data-id="8823350"><a href="/opinion/8838257/united-states-v-falloco/#82" aria-description="Citation for case: United States v. Falloco">277 Fed. 75, 82</a></span>; <em>Legman </em>v. <em>United States, </em><span class="citation" data-id="8834058"><a href="/opinion/8848718/legman-v-united-states/#476" aria-description="Citation for case: Legman v. United States">295 Fed. 474, 476-478</a></span>; <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="1508855"><a href="/opinion/1508855/marron-v-united-states/#259" aria-description="Citation for case: Marron v. United States">8 F. 2d 251, 259</a></span>; <em>United States </em>v. <em>Brown, </em><span class="citation" data-id="1508963"><a href="/opinion/1508963/united-states-v-brown/#631" aria-description="Citation for case: United States v. Brown">8 F. 2d 630, 631</a></span>.</p>
<p id="b285-5">This Court first came to grips with the problem in <em>Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>. There it was held that when the participation of the federal agent in the search was “under color of his federal office” and the search “in substance and effect was a joint operation of the local and federal officers,” then the evidence .must be excluded, because “the effect is the same as though [the federal agent] had engaged in the undertaking as one exclusively his own.” <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S., at 33</a></span>. In <em>Gambino </em>v. <em>United States, </em><span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/" aria-description="Citation for case: Gambino v. United States">275 U. S. 310</a></span>, the Court went further. There state officers had seized liquor from the defendants’ automobile after an unlawful search in which no federal officers had participated. The liquor was admitted in evidence against the defendants in their subsequent federal trial for violation of the National Prohibition Act. This <page-number citation-index="1" label="212">*212</page-number>Court reversed the judgments of conviction, holding that the illegally seized evidence should have been excluded. Pointing out that there was “no suggestion that the defendants were committing, at the time of the arrest, search and seizure, any state offense; or that they had done so in the past; or that the [state] troopers believed that they had,” the Court found that “[t]he wrongful arrest, search and seizure were made solely on behalf of the United States.” <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#314" aria-description="Citation for case: Gambino v. United States">275 U. S., at 314, 316</a></span>.</p>
<p id="b286-5">Despite these decisions, or perhaps because of them, cases kept arising in which the federal courts were faced with determining whether there had been such participation by federal officers in a lawless state search as to make inadmissible in evidence that which had been seized. And it is fair to say that in their approach to this recurring question, no less than in their disposition of concrete cases, the federal courts did not find themselves in complete harmony, nor even internally self-consistent.<footnotemark>4</footnotemark> No less difficulty was experienced by the courts in determining whether, even in the absence of actual participation by federal agents, the state officers’ illegal search and seizure had nevertheless been made “solely on behalf of the United States.” <footnotemark>5</footnotemark></p>
<p id="b286-6">But difficult and unpredictable as may have been their application to concrete cases, the controlling principles seemed clear up to 1949. Evidence which had been seized by federal officers in violation of the Fourth Amendment <page-number citation-index="1" label="213">*213</page-number>could not be used in a federal criminal prosecution. Evidence which had been obtained by state agents in an unreasonable search and seizure was admissible, because, as <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>had pointed out, the Fourth Amendment was not “directed to” the “misconduct of such officials.” But if federal agents had participated in an unreasonable search and seizure by state officers, or if the state officers had acted solely on behalf of the United States, the evidence was not admissible in a federal prosecution.</p>
<p id="b287-5">Then came <em>Wolf </em>v. <em>Colorado, </em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>. With the ultimate determination in <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>— that the Due Process Clause of the Fourteenth Amendment does not itself require state courts to adopt the exclusionary rule with respect to evidence illegally seized by state agents — we are not here directly concerned. But nothing could be of greater relevance to the present inquiry than the underlying constitutional doctrine which <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>established. For there it was unequivocally determined by a unanimous Court that the Federal Constitution, by virtue of the Fourteenth Amendment, prohibits unreasonable searches and seizures by state officers. “The security of one’s privacy against arbitrary intrusion by the police ... is . . . implicit in ‘the concept of ordered liberty’ and as such enforceable against the States through the Due Process Clause.” <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27-28</a></span>. The Court has subsequently found frequent occasion to reiterate this statement from <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span>. </em>See <em>Stefanelli </em>v. <em>Minard, </em><span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/#119" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117, 119</a></span>; <em>Irvine </em>v. <em>California, 347 </em>U. S. 128, 132; <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#362" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 362-363</a></span>.</p>
<p id="b287-6">The foundation upon which the admissibility of state-seized evidence in a federal trial originally rested — that unreasonable state searches did not violate the Federal Constitution — thus disappeared in 1949. This removal of the doctrinal underpinning for the admissibility rule has apparently escaped the attention of most of the federal courts, which have continued to approve the admission of <page-number citation-index="1" label="214">*214</page-number>evidence illegally seized by state officers without so much as even discussing the impact of Wolf.<footnotemark>6</footnotemark> Only two of the courts of appeals which have adhered to the admissibility rule appear to have recognized that <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>casts doubt upon its continuing validity. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="235212"><a href="/opinion/235212/robert-laverne-jones-v-united-states/" aria-description="Citation for case: Robert Laverne Jones v. United States">217 F. 2d 381</a></span> (C. A. 8th Cir.); <em>United States </em>v. <em>Benanti, </em><span class="citation" data-id="242217"><a href="/opinion/242217/united-states-v-salvatore-benanti/" aria-description="Citation for case: United States v. Salvatore Benanti">244 F. 2d 389</a></span> (C. A. 2d Cir.), reversed on other grounds, <span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>. Cf. <em>Kendall </em>v. <em>United States, </em><span class="citation" data-id="249351"><a href="/opinion/249351/paul-a-kendall-and-ruth-elder-kendall-v-united-states/#165" aria-description="Citation for case: Paul A. Kendall and Ruth Elder Kendall v. United States">272 F. 2d 163, 165</a></span> (C. A. 5th Cir.). The Court of Appeals for the District of Columbia has been alone in squarely holding “that the Weeks and the Wolf decisions, considered together, make all evidence obtained by unconstitutional search and seizure unacceptable in federal courts.” <em>Hanna </em>v. <em>United States, </em>104 U. S. App. D. C. 205, 209, <span class="citation" data-id="246433"><a href="/opinion/246433/samuel-j-hanna-v-united-states/#727" aria-description="Citation for case: Samuel J. Hanna v. United States">260 F. 2d 723, 727</a></span>.</p>
<p id="b288-6">Yet this Court’s awareness that the constitutional doctrine of <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>operated to undermine the logical foundation of the <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>admissibility rule has been manifest from the very day that <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>was decided. In <em>Lustig </em>v. <em>United States, </em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">338 U. S. 74</a></span>, decided that day, the prevailing opinion carefully left open the question of the continuing validity of the admissibility rule. “Where there is participation on the part of federal officers,” the opinion said, “it is not necessary to consider what would be the result if the search had been conducted entirely by State officers.” 338 U. S., at 79. And in <em>Benanti </em>v. <em>United States, </em><span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>, the Court was at pains to point out that “[i]t has remained an open question in this Court whether evidence obtained solely by state agents in an illegal search may be admissible in federal court . . . .” <span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/#102" aria-description="Citation for case: Benanti v. United States">355 U. S., at 102, note 10</a></span>. There the question has stood for 11 years.</p>
<p id="b289-4"><page-number citation-index="1" label="215">*215</page-number>If resolution of the issue were to be dictated solely by principles of logic, it is clear what our decision would have to be. For surely no distinction can logically be drawn between evidence obtained in violation of the Fourth Amendment and that obtained in violation of the Fourteenth. The Constitution is flouted equally in either case. To the victim it matters not whether his constitutional right has been invaded by a federal agent or by a state officer.<footnotemark>7</footnotemark> It would be a curiously ambivalent rule that would require the courts of the United States to differentiate between unconstitutionally seized evidence upon so arbitrary a basis. Such a distinction indeed would appear to reflect an indefensibly selective evaluation of the provisions of the Constitution. Moreover, it would seem logically impossible to justify a policy that would bar from a federal trial what state officers had obtained in violation of a federal statute, yet would admit that which they had seized in violation of the Constitu-tionffitself. Cf. <em>Benanti </em>v. <em>United States, </em><span class="citation" data-id="105584"><a href="/opinion/105584/benanti-v-united-states/" aria-description="Citation for case: Benanti v. United States">355 U. S. 96</a></span>.</p>
<p id="b290-4"><page-number citation-index="1" label="216">*216</page-number>Mere logical symmetry and abstract reasoning are perhaps not enough, however, to support a doctrine that would exclude relevant evidence from the trial of a federal criminal case. It is true that there is not involved here an absolute or qualified testimonial privilege such as that accorded a spouse, a patient, or a penitent, which irrevocably bars otherwise admissible evidence because of the <em>status </em>of the witness or his relationship to the defendant. Cf. <em>Hawkins </em>v. <em>United States, </em><span class="citation" data-id="9421718"><a href="/opinion/105789/hawkins-v-united-states/" aria-description="Citation for case: Hawkins v. United States">358 U. S. 74</a></span>. A rule which would exclude evidence if, and only if, government officials in a particular case had chosen to engage in unlawful <em>conduct </em>is of a different order. Yet, any apparent limitation upon the process of discovering truth in a federal trial ought to be imposed only upon the basis of considerations which outweigh the general need for untrammeled disclosure . of competent and relevant evidence in a court of justice.</p>
<p id="b290-5">What is here invoked is the Court’s supervisory power over the administration of criminal justice in the federal courts, under which the Court has “from the very beginning -of its history, formulated rules of evidence to be applied in federal criminal prosecutions.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#341" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 341</a></span>. In devising such evi-dentiary rules, we are to be governed by “principles of the common law as they may be interpreted ... in the light of reason and experience.” Rule 26, Fed. Rules Crim. Proc. Determination of the issue before us must ultimately depend, therefore, upon evaluation of the exclusionary rule itself in the context here presented.</p>
<p id="b290-6">The exclusionary rule has for decades been the subject of ardent controversy. The arguments of its antagonists and of its proponents have been so many times marshalled as to require no lengthy elaboration here. Most of what has been said in opposition to the rule was distilled in a single Cardozo sentence — “The criminal is to go free because the constable has blundered.” <em>People </em>v. <em>Defore, </em><page-number citation-index="1" label="217">*217</page-number><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span>. The same point was made at somewhat greater length in the often quoted words of Professor Wigmore: “Titus, you have been found guilty of conducting a lottery; Flavius, you have confessedly violated the constitution. Titus ought to suffer imprisonment for crime, and Flavius for contempt. But no! We shall let you <em>both </em>go free. We shall not punish Flavius directly, but shall do so by reversing Titus’ conviction. This is our way of teaching people like Flavius to behave, and of teaching people like Titus to behave, and incidentally of securing respect for the Constitution. Our way of upholding the Constitution is not to strike at the man who breaks it, but to let off somebody else who broke something else.” 8 Wigmore, Evidence (3d ed. 1940), § 2184.</p>
<p id="b291-5">Yet, however felicitous their phrasing, these objections hardly answer the basic postulate of the exclusionary rule itself. The rule is calculated to prevent, not to repair. Its purpose is to deter — to compel respect for the constitutional guaranty in the only effectively available way— by removing the incentive to disregard it. See <em>Eleuteri </em>v. Rickman, 26 N. J. 506, 513, <span class="citation" data-id="1934063"><a href="/opinion/1934063/eleuteri-v-richman/#50" aria-description="Citation for case: Eleuteri v. Richman">141 A. 2d 46, 50</a></span>. Mr. Justice Jackson summed it up well:</p>
<blockquote id="b291-6">“Only occasional and more flagrant abuses come to the attention of the courts, and then only those where the search and seizure yields incriminating evidence and the defendant is at least sufficiently compromised to be indicted. If the officers raid a home, an office, or stop and search an automobile but find nothing incriminating, this invasion of the personal liberty of the innocent too often finds no practical redress. There may be, and I am convinced that there are, many unlawful searches of homes and automobiles of innocent people which turn up nothing incriminating, in which no arrest is made, about <page-number citation-index="1" label="218">*218</page-number>which courts do nothing, and about which we never hear.</blockquote>
<blockquote id="b292-5">“Courts can protect the innocent against such invasions only indirectly and through the medium of excluding evidence obtained against those who frequently are guilty.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#181" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 181</a></span> (dissenting opinion).</blockquote>
<p id="b292-6">Empirical statistics are not available to show that the inhabitants of states which follow the exclusionary rule suffer less from lawless searches and seizures than do those of states which admit evidence unlawfully obtained. Since as a practical matter it is never easy to prove a negative, it is hardly likely that conclusive factual data could ever be assembled. For much the same reason, it cannot positively be demonstrated that enforcement of the criminal law is either more or less effective under either rule.</p>
<p id="b292-7">But pragmatic evidence of a sort is not wanting. The federal courts themselves have operated under the exclusionary rule of <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>for almost half a century; yet it has not been suggested either that the Federal Bureau of Investigation has thereby been rendered ineffective, or that the administration of criminal justice in the federal courts has thereby been disrupted.<footnotemark>8</footnotemark> Moreover, the expe<page-number citation-index="1" label="219">*219</page-number>rience of the states is impressive. Not more than half the states continue totally to adhere to the rule that evidence is freely admissible no matter how it was obtained.<footnotemark>9</footnotemark> Most of the others have adopted the exclusionary rule in its entirety; the rest have adopted it in part.<footnotemark>10</footnotemark> The movement towards the rule of exclusion has been halting but seemingly inexorable.<footnotemark>11</footnotemark> Since the <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>decision one state has switched its position in that direction by legislation,<footnotemark>12</footnotemark> and two others by judicial decision.<footnotemark>13</footnotemark> Another state, uncommitted until 1955, in that year adopted the rule <page-number citation-index="1" label="220">*220</page-number>of exclusion.<footnotemark>14</footnotemark> Significantly, most of the exclusionary states which have had to consider the issue have held that evidence obtained by <em>federal </em>officers in a search and seizure unlawful under the Fourth Amendment must be suppressed in a prosecution in the <em>state </em>courts. <em>State </em>v. <em>Arregui, </em><span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span>; <em>Walters </em>v. <em>Commonwealth, </em><span class="citation" data-id="7148071"><a href="/opinion/7235652/walters-v-commonwealth/" aria-description="Citation for case: Walters v. Commonwealth">199 Ky. 182</a></span>, <span class="citation" data-id="7148071"><a href="/opinion/7235652/walters-v-commonwealth/" aria-description="Citation for case: Walters v. Commonwealth">250 S. W. 839</a></span>; <em>Little </em>v. <em>State, </em><span class="citation" data-id="3517292"><a href="/opinion/3544745/little-v-state/" aria-description="Citation for case: Little v. State">171 Miss. 818</a></span>, <span class="citation" data-id="3517292"><a href="/opinion/3544745/little-v-state/" aria-description="Citation for case: Little v. State">159 So. 103</a></span>; <em>State </em>v. <em>Rebasti, </em><span class="citation" data-id="3534889"><a href="/opinion/3557416/state-v-rebasti/" aria-description="Citation for case: State v. Rebasti">306 Mo. 336</a></span>, <span class="citation" data-id="3534889"><a href="/opinion/3557416/state-v-rebasti/" aria-description="Citation for case: State v. Rebasti">267 S. W. 858</a></span>; <em>State </em>v. <em>Hiteshew, </em><span class="citation" data-id="4012045"><a href="/opinion/4234880/state-v-hiteshew/" aria-description="Citation for case: State v. Hiteshew">42 Wyo. 147</a></span>, <span class="citation" data-id="4012045"><a href="/opinion/4234880/state-v-hiteshew/" aria-description="Citation for case: State v. Hiteshew">292 P. 2</a></span>; see <em>Ramirez </em>v. <em>State, </em><span class="citation" data-id="3924432"><a href="/opinion/4158808/ramirez-v-state/" aria-description="Citation for case: Ramirez v. State">123 Tex. Cr. R. 254</a></span>, <span class="citation" data-id="3924432"><a href="/opinion/4158808/ramirez-v-state/" aria-description="Citation for case: Ramirez v. State">58 S. W. 2d 829</a></span>. Compare <em>Rea </em>v. <em>United States, </em><span class="citation" data-id="9421227"><a href="/opinion/105343/rea-v-united-states/" aria-description="Citation for case: Rea v. United States">350 U. S. 214</a></span>.</p>
<p id="b294-6">The experience in California has been most illuminating. In 1955 the Supreme Court of that State resolutely turned its back on many years of precedent and adopted the exclusionary rule. <em>People </em>v. <em>Cahan, </em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span>. “We have been compelled to reach that conclusion because other remedies have completely failed to secure compliance with the constitutional provisions on the part of police officers with the attendant result that the courts under the ■ old rule have been constantly required to participate in, and in effect condone, the lawless activities of law enforcement officers. . . . Experience has demonstrated, however, that neither administrative, criminal nor civil remedies are effective in suppressing lawless searches and seizures. The innocent suffer with the guilty, and we cannot close our eyes to the effect the rule we adopt will have on the rights of those not before the court.” <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#445" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434, at 445, 447</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/#911" aria-description="Citation for case: People v. Cahan">282 P. 2d 905, at 911-912, 913</a></span>.</p>
<p id="b294-7">The ■ chief law enforcement officer of California was quoted as having made this practical evaluation of the <em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">Cahan</a></span> </em>decision less than two years later:</p>
<blockquote id="b294-8">“The over-all effects of the Cahan decision, particularly in view of the rules now worked out by the Supreme Court, have been excellent. A much <page-number citation-index="1" label="221">*221</page-number>greater education, is called for on the part of all peace officers of California. As a result, I am confident they will be much better police officers. I think there is more cooperation with the District Attorneys and this will make for better administration of criminal justice.” <footnotemark>15</footnotemark></blockquote>
<p id="b295-5">Impressive as is this experience of individual states, even more is to be said for adoption of the exclusionary rule in the particular context here presented — a context which brings into focus considerations of federalism. The very essence of a healthy federalism depends upon the avoidance of needless conflict between state and federal courts. Yet when a federal court sitting in an exclusionary state admits evidence lawlessly seized by state agents, it not only frustrates state policy, but frustrates that policy in a particularly inappropriate and ironic way. For by admitting the unlawfully seized evidence the federal court serves to defeat the state’s effort to assure obedience to the Federal Constitution. In states which have not adopted the exclusionary rule, on the other hand, it would work no conflict with local policy for a federal court to decline to receive evidence unlawfully seized by state officers. The question with which we deal today affects not at all the freedom of the states to develop and apply their own sanctions in their own way. Cf. <em>Wolf </em>v. Colorado, <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>.</p>
<p id="b295-6">Free and open cooperation between state and federal law enforcement officers is to be commended and encouraged. Yet that kind of cooperation is hardly promoted by a rule that implicitly invites federal officers to withdraw from such association and at least tacitly to ericour-<page-number citation-index="1" label="222">*222</page-number>age state officers in the disregard of constitutionally protected freedom. If, on the other hand, it is understood that the fruit of an unlawful search by state agents will be inadmissible in a federal trial, there can be no inducement to subterfuge and evasion with respect to federal-state cooperation in criminal investigation. Instead, forthright cooperation under constitutional standards will be promoted and fostered.</p>
<p id="b296-6">It must always be remembered that what the Constitution forbids is not all searches and seizures, but unreasonable searches and seizures. Without pausing to analyze individual decisions, it can fairly be said that in applying the Fourth Amendment this Court has seldom shown itself unaware of the practical demands of effective criminal investigation and law enforcement. Indeed, there are those who think that some of the Court’s decisions have tipped the balance too heavily against the protection of that individual privacy which it was the purpose of the Fourth Amendment to guarantee. See <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155, 183, 195</a></span> (dissenting opinions); <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66, 68</a></span> (dissenting opinions). In any event, while individual cases have sometimes evoked “fluctuating differences of view,” <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#235" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 235</a></span>, it can hardly be said that in the over-all pattern of Fourth Amendment decisions this Court has been either unrealistic or visionary.</p>
<p id="b296-7">These, then, are the considerations of reason and experience which point to the rejection of a doctrine that would freely admit in a federal criminal trial evidence seized by state agents in violation of the defendant’s constitutional rights. But there is another consideration— the imperative of judicial integrity. It was of this that Mr. Justice Holmes and Mr. Justice Brandéis so eloquently spoke in <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#469" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, at 469, 471</a></span>, more than 30 years ago. “For those who <page-number citation-index="1" label="223">*223</page-number>agree with me,” said Mr. Justice Holmes, “no distinction can be taken between the Government as prosecutor and the Government as judge.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 470</a></span>. (Dissenting opinion.) “In a government of laws,” said Mr. Justice Brandéis, “existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the means — to declare that the Government may commit crimes in order to secure the conviction of a private criminal — would bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face.” <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#485" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 485</a></span>. (Dissenting opinion.)</p>
<p id="b297-5">This basic principle was accepted by the Court in <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U. S. 332</a></span>. There it was held that “a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in willful disobedience of law.” <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#345" aria-description="Citation for case: McNabb v. United States">318 U. S., at 345</a></span>. Even less should the federal courts be accomplices in the willful disobedience of a Constitution they are sworn to uphold.</p>
<p id="b297-6">For these reasons we hold that evidence obtained by state officers during a search which, if conducted by federal officers, would have violated the defendant’s immunity from unreasonable searches and seizures under the Fourth Amendment is inadmissible over the defendant’s timely objection in a federal criminal trial.<footnotemark>16</footnotemark> In deter<page-number citation-index="1" label="224">*224</page-number>mining whether there has been an unreasonable search and seizure by state officers, a federal court must make an independent inquiry, whether or not there has been such an inquiry by a state court, and irrespective of how any such inquiry may have turned out. The test is one of federal law, neither enlarged by what one state court may have countenanced, nor diminished by what another may have colorably suppressed.</p>
<p id="b298-4">The judgment of the Court of Appeals is set aside, and the case is remanded to the District Court for further proceedings consistent with this opinion.</p>
<p id="b298-5">
<em>Vacated and remanded.</em>
</p>
<p id="b298-6">APPENDIX TO OPINION OF THE COURT.</p>
<p id="b298-7">Table <em>I. </em>— Admissibility, <em>in state courts, of evidence illegally seized by state officers.</em></p>
<p id="b298-9">
<em>State Pre-Weeks Pre-Wolf Post-Wolf</em>
</p>
<p id="b298-10">Alabama_ Admissible_ Admissible_ Partially</p>
<p id="b298-11">excludable</p>
<p id="b298-12">Arizona_ _ Admissible_ Admissible</p>
<p id="b298-13">Arkansas_ Admissible_ Admissible_ Admissible</p>
<p id="b298-14">California_ Admissible_ Admissible_ Excludable</p>
<p id="b298-15">Colorado_ _ Admissible_ Admissible</p>
<p id="b298-16">Connecticut_ Admissible_ Admissible_ Admissible</p>
<p id="b298-17">Delaware_ _ Admissible_ Excludable</p>
<p id="b298-18">Florida_ _ Excludable_ Excludable</p>
<p id="b298-19">Georgia_■_ Admissible_ Admissible_ Admissible</p>
<p id="b298-20">Idaho_ Admissible_ Excludable_ Excludable</p>
<p id="b298-21">Illinois_ Admissible.-. Excludable_ Excludable</p>
<p id="b298-22">Indiana_ _ Excludable_ Excludable</p>
<p id="b298-23">Iowa_ Excludable... Admissible_ Admissible</p>
<p id="b298-24">Kansas_ Admissible_ Admissible_ Admissible</p>
<p id="b298-25">Kentucky_ _ Excludable_ Excludable</p>
<p id="b298-26">Louisiana_ _ Admissible... Admissible</p>
<p id="b298-27">Maine_ Admissible_ Admissible_ Admissible</p>
<p id="AMr">Maryland_ Admissible_ Partially Partially excludable excludable</p>
<p id="b298-30">Massachusetts_ Admissible_ Admissible_ Admissible</p>
<p id="b299-4"><page-number citation-index="1" label="225">*225</page-number>Table <em>I. </em>— Admissibility, <em>in state courts, of evidence illegally seized by state officers </em>— Continued.</p>
<p id="b299-5">
<em>State Pre-Weeks Pre-Wolf Post-Wolf</em>
</p>
<p id="b299-6">Michigan_ Admissible_ Excludable_ Partially . excludable</p>
<p id="b299-8">Minnesota- Admissible. __ Admissible... Admissible</p>
<p id="b299-9">Mississippi_ _ Excludable_ Excludable</p>
<p id="b299-10">Missouri- Admissible_ Excludable... Excludable</p>
<p id="b299-11">Montana- Admissible_ Excludable_ Excludable</p>
<p id="b299-12">Nebraska- Admissible... Admissible_ Admissible</p>
<p id="b299-13">Nevada- - Admissible_ Admissible</p>
<p id="b299-14">New Hampshire_ Admissible_ Admissible_ Admissible</p>
<p id="b299-15">New Jersey_ _ Admissible_ Admissible</p>
<p id="b299-16">New Mexico_ _- Admissible_ Admissible</p>
<p id="b299-17">New York- Admissible... Admissible_ Admissible</p>
<p id="b299-18">North Carolina_ Admissible_ Admissible_ Excludable</p>
<p id="b299-19">North Dakota_ _ Admissible_ Admissible</p>
<p id="b299-20">Ohio- - Admissible_ Admissible</p>
<p id="b299-21">Oklahoma_ Admissible_ Excludable_ Excludable</p>
<p id="b299-22">Oregon- Admissible_ Excludable_ Excludable</p>
<p id="b299-23">Pennsylvania_ _ Admissible... Admissible</p>
<p id="b299-24">Rhode Island_ _ _ Excludable</p>
<p id="b299-25">South Carolina- Admissible_ Admissible_ Admissible</p>
<p id="b299-26">South Dakota_ Admissible. __ Excludable_ Partially excludable</p>
<p id="b299-28">Tennessee_... Admissible_ Excludable... Excludable</p>
<p id="b299-29">Texas- - Excludable_ Excludable</p>
<p id="b299-30">Utah- - Admissible_ Admissible</p>
<p id="b299-31">Vermont- Admissible_ Admissible_ Admissible</p>
<p id="b299-32">Virginia_ _ Admissible_ Admissible</p>
<p id="b299-33">Washington- Admissible... Excludable... Excludable</p>
<p id="b299-34">West Virginia_ Admissible_ Excludable_ Excludable</p>
<p id="b299-35">Wisconsin_ _ Excludable_ Excludable</p>
<p id="b299-36">Wyoming_ _ Excludable... Excludable</p>
<p id="b299-37">To admit — 27 To admit — 29 To admit — 24</p>
<p id="b299-38">To exclude — 1 To exclude— To exclude—</p>
<p id="b299-39">18. 26<footnotemark>*</footnotemark></p>
<p id="b299-40">Undecided— Undecided— Undecided—</p>
<p id="b299-41">20. 1. 0.</p>
<p id="b300-5"><page-number citation-index="1" label="226">*226</page-number>Table <em>II. </em>— Representative <em>cases by state, considering the admissibility of evidence illegally seized by state officers.</em></p>
<p id="b300-6">Alabama</p>
<p id="b300-7">Pre-Weeks: <em>Shields </em>v. <em>State, </em><span class="citation" data-id="6515773"><a href="/opinion/6639159/shields-v-state/" aria-description="Citation for case: Shields v. State">104 Ala. 35</a></span>, <span class="citation no-link">16 So. 85</span> (admissible).</p>
<p id="b300-8">Pre-Wolf: <em>Banks </em>v. <em>State, </em><span class="citation" data-id="3233534"><a href="/opinion/3232762/banks-v-state/" aria-description="Citation for case: Banks v. State">207 Ala. 179</a></span>, <span class="citation multiple-matches"><a href="/c/So./93/293/">93 So. 293</a></span> (admissible).</p>
<p id="b300-9">Post-Wolf: Cf. <em>Oldham </em>v. <em>State, </em><span class="citation" data-id="1118348"><a href="/opinion/1118348/oldham-v-state/" aria-description="Citation for case: Oldham v. State">259 Ala. 507</a></span>, <span class="citation" data-id="1118348"><a href="/opinion/1118348/oldham-v-state/" aria-description="Citation for case: Oldham v. State">67 So. 2d 55</a></span> (admissible) .</p>
<p id="b300-10">(Ala. Code, 1940 (Supp. 1955), Tit. 29, § 210, requires the exclusion of illegally obtained evidence in the trial of certain alcohol control cases.)</p>
<p id="b300-11">Arizona</p>
<p id="b300-12">Pre-Weeks: no holding.</p>
<p id="b300-13">Pre-Wolf: <em>Argetakis </em>v. <em>State, </em><span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">24 Ariz. 599</a></span>, <span class="citation" data-id="6474949"><a href="/opinion/6599573/argetakis-v-state/" aria-description="Citation for case: Argetakis v. State">212 P. 372</a></span> (admissible) .</p>
<p id="b300-14">Post-Wolf: <em>State </em>v. <em>Thomas, </em><span class="citation" data-id="1199500"><a href="/opinion/1199500/state-v-thomas/" aria-description="Citation for case: State v. Thomas">78 Ariz. 52</a></span>, <span class="citation" data-id="1199500"><a href="/opinion/1199500/state-v-thomas/" aria-description="Citation for case: State v. Thomas">275 P. 2d 408</a></span> (admissible).</p>
<p id="b300-15">Arkansas</p>
<p id="b300-16">Pre-Weeks: <em>Starchman </em>v. <em>State, </em><span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">62 Ark. 538</a></span>, <span class="citation" data-id="6543624"><a href="/opinion/6665982/starchman-v-state/" aria-description="Citation for case: Starchman v. State">36 S. W. 940</a></span> (admissible) .</p>
<p id="b300-17">Pre-Wolf: <em>Benson </em>v. <em>State, </em><span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">149 Ark. 633</a></span>, <span class="citation" data-id="7811152"><a href="/opinion/7866973/benson-v-state/" aria-description="Citation for case: Benson v. State">233 S. W. 758</a></span> (admissible) .</p>
<p id="b300-19">Post-Wolf: <em>Lane, Smith &amp; Barg </em>v. <em>State, </em><span class="citation" data-id="1780082"><a href="/opinion/1780082/lane-smith-barg-v-state/" aria-description="Citation for case: Lane, Smith &amp; Barg v. State">217 Ark. 114</a></span>, <span class="citation" data-id="1780082"><a href="/opinion/1780082/lane-smith-barg-v-state/" aria-description="Citation for case: Lane, Smith &amp; Barg v. State">229 S. W. 2d 43</a></span> (admissible).</p>
<p id="b300-20">California</p>
<p id="b300-21">Pre-Weeks: <em>People </em>v. <em>Le Doux, </em><span class="citation" data-id="3302902"><a href="/opinion/3303561/people-v-le-doux/" aria-description="Citation for case: People v. Le Doux">155 Cal. 535</a></span>, <span class="citation" data-id="3302902"><a href="/opinion/3303561/people-v-le-doux/" aria-description="Citation for case: People v. Le Doux">102 P. 517</a></span> (admissible).</p>
<p id="b300-22">Pre-Wolf: <em>People </em>v. <em>Mayen, </em><span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">188 Cal. 237</a></span>, <span class="citation" data-id="3307559"><a href="/opinion/3307673/people-v-mayen/" aria-description="Citation for case: People v. Mayen">205 P. 435</a></span> (admissible) .</p>
<p id="b300-23">Post-Wolf: <em>People </em>v. <em>Cahan, </em><span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">44 Cal. 2d 434</a></span>, <span class="citation" data-id="9576237"><a href="/opinion/1237532/people-v-cahan/" aria-description="Citation for case: People v. Cahan">282 P. 2d 905</a></span> (excludable) .</p>
<p id="b300-24">Colorado</p>
<p id="b300-25">Pre-Weeks: no holding.</p>
<p id="b300-26">Pre-Wolf: <em>Massantonio </em>v. <em>People, </em><span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">77 Colo. 392</a></span>, <span class="citation" data-id="3311672"><a href="/opinion/3316610/massantonio-v-people/" aria-description="Citation for case: Massantonio v. People">236 P. 1019</a></span> (admissible) .</p>
<p id="b300-27">Post-Wolf: <em>Williams </em>v. <em>People, </em><span class="citation" data-id="1174129"><a href="/opinion/1174129/williams-v-people/" aria-description="Citation for case: Williams v. People">136 Colo. 164</a></span>, <span class="citation" data-id="1174129"><a href="/opinion/1174129/williams-v-people/" aria-description="Citation for case: Williams v. People">315 P. 2d 189</a></span> (admissible).</p>
<p id="b300-28">Connecticut</p>
<p id="b300-29">Pre-Weeks: <em>State </em>v. <em>Griswold, </em><span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">67 Conn. 290</a></span>, <span class="citation" data-id="6583651"><a href="/opinion/6703553/state-v-griswold/" aria-description="Citation for case: State v. Griswold">34 A. 1046</a></span> (admissible) .</p>
<p id="b300-30">Pre-Wolf: <em>State </em>v. <em>Reynolds, </em><span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">101 Conn. 224</a></span>, <span class="citation" data-id="3321660"><a href="/opinion/3326264/state-v-reynolds/" aria-description="Citation for case: State v. Reynolds">125 A. 636</a></span> (admissible) .</p>
<p id="b300-31">Post-Wolf: no holding.</p>
<p id="b300-32">Delaware</p>
<p id="b300-33">Pre-Weeks: no holding.</p>
<p id="b300-34">Pre-Wolf: <em>State </em>v. <em>Chuchola, </em><span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">32 Del. 133</a></span>, <span class="citation" data-id="6556679"><a href="/opinion/6677615/state-v-chuchola/" aria-description="Citation for case: State v. Chuchola">120 A. 212</a></span> (admissible).</p>
<p id="b300-35">Post-Wolf: <em>Rickards </em>v. <em>State, </em><span class="citation" data-id="9757678"><a href="/opinion/2352643/rickards-v-state/" aria-description="Citation for case: Rickards v. State">45 Del. 573</a></span>, <span class="citation" data-id="9757678"><a href="/opinion/2352643/rickards-v-state/" aria-description="Citation for case: Rickards v. State">77 A. 2d 199</a></span> (excludable) .</p>
<p id="b301-5"><page-number citation-index="1" label="227">*227</page-number>Florida</p>
<p id="AxT">Pre-Weeks: no holding.</p>
<p id="AR">Pre-Wolf: <em>Atz </em>v. <em>Andrews, </em><span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">84 Fla. 43</a></span>, <span class="citation" data-id="4921024"><a href="/opinion/5103176/atz-v-andrews/" aria-description="Citation for case: Atz v. Andrews">94 So. 329</a></span> (excludable).</p>
<p id="A7C">Post-Wolf: <em>Byrd </em>v. <em>State, </em><span class="citation" data-id="1837215"><a href="/opinion/1837215/byrd-v-state/" aria-description="Citation for case: Byrd v. State">80 So. 2d 694</a></span> (Sup. Ct. Florida) (excludable).</p>
<p id="Atl">Georgia</p>
<p id="A6Y">Pre-Weeks: <em>Williams </em>v. <em>State, </em><span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">100 Ga. 511</a></span>, <span class="citation" data-id="5567449"><a href="/opinion/5717379/williams-v-state/" aria-description="Citation for case: Williams v. State">28 S. E. 624</a></span> (admissible) .</p>
<p id="ANs">Pre-Wolf: <em>Jackson </em>v. <em>State, </em><span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">156 Ga. 647</a></span>, <span class="citation" data-id="5584660"><a href="/opinion/5734032/jackson-v-state/" aria-description="Citation for case: Jackson v. State">119 S. E. 525</a></span> (admissible) .</p>
<p id="AaQ">Post-Wolf: <em>Atterberry </em>v. <em>State, </em><span class="citation" data-id="1209203"><a href="/opinion/1209203/atterberry-v-state/" aria-description="Citation for case: Atterberry v. State">212 Ga. 778</a></span>, <span class="citation no-link">95 S. E. 2d 787</span> (admissible).</p>
<p id="AhG">Idaho</p>
<p id="AR4">Pre-Weeks: <em>State </em>v. <em>Bond, </em><span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/" aria-description="Citation for case: State v. Bond">12 Idaho 424</a></span>, <span class="citation" data-id="5169254"><a href="/opinion/5337571/state-v-bond/" aria-description="Citation for case: State v. Bond">86 P. 43</a></span> (admissible).</p>
<p id="AGk">Pre-Wolf: <em>State </em>v. <em>Arregui, </em><span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">44 Idaho 43</a></span>, <span class="citation" data-id="3412636"><a href="/opinion/3416496/state-v-arregui/" aria-description="Citation for case: State v. Arregui">254 P. 788</a></span> (excludable.)</p>
<p id="Ac1">Post-Wolf: no holding.</p>
<p id="AeLy">Illinois</p>
<p id="AsJ">Pre-Weeks: <em>Siebert </em>v. <em>People, </em><span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/" aria-description="Citation for case: Siebert v. People">143 Ill. 571</a></span>, <span class="citation" data-id="6965240"><a href="/opinion/7061242/siebert-v-people/" aria-description="Citation for case: Siebert v. People">32 N. E. 431</a></span> (admissible).</p>
<p id="Aux">Pre-Wolf: <em>People </em>v. <em>Castree, </em><span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">311 Ill. 392</a></span>, <span class="citation" data-id="6981353"><a href="/opinion/7076578/people-v-castree/" aria-description="Citation for case: People v. Castree">143 N. E. 112</a></span> (excludable) .</p>
<p id="AD5H">Post-Wolf: <em>City of Chicago </em>v. Lord, <span class="citation" data-id="2030212"><a href="/opinion/2030212/city-of-chicago-v-lord/" aria-description="Citation for case: City of Chicago v. Lord">7 Ill. 2d 379</a></span>, <span class="citation" data-id="2030212"><a href="/opinion/2030212/city-of-chicago-v-lord/" aria-description="Citation for case: City of Chicago v. Lord">130 N. E. 2d 504</a></span> (excludable).</p>
<p id="Av2">Indiana</p>
<p id="ALv">Pre-Weeks: no holding.</p>
<p id="AKW">Pre-Wolf: <em>Flum </em>v. <em>State, </em><span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">193 Ind. 585</a></span>, <span class="citation" data-id="7057995"><a href="/opinion/7149435/flum-v-state/" aria-description="Citation for case: Flum v. State">141 N. E. 353</a></span> (excludable).</p>
<p id="ASJ">Post-Wolf: <em>Rohlfing </em>v. <em>State, </em><span class="citation" data-id="9523527"><a href="/opinion/2030951/rohlfing-v-state/" aria-description="Citation for case: Rohlfing v. State">230 Ind. 236</a></span>, <span class="citation" data-id="9523527"><a href="/opinion/2030951/rohlfing-v-state/" aria-description="Citation for case: Rohlfing v. State">102 N. E. 2d 199</a></span> (excludable) .</p>
<p id="Ash">Iowa</p>
<p id="AV8">Pre-Weeks: <em>State </em>v. <em>Sheridan, </em><span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">121 Iowa 164</a></span>, <span class="citation" data-id="7110547"><a href="/opinion/7199309/state-v-sheridan/" aria-description="Citation for case: State v. Sheridan">96 N. W. 730</a></span> (excludable) .</p>
<p id="ADP">Pre-Wolf: <em>State </em>v. <em>Rowley, </em><span class="citation" data-id="7120701"><a href="/opinion/7208995/state-v-rowley/" aria-description="Citation for case: State v. Rowley">197 Iowa 977</a></span>, <span class="citation no-link">195 N. W. 881</span> (admissible) .</p>
<p id="ASf">Post-Wolf: <em>State </em>v. <em>Smith, </em><span class="citation" data-id="2190973"><a href="/opinion/2190973/state-v-smith/" aria-description="Citation for case: State v. Smith">247 Iowa 500</a></span>, <span class="citation" data-id="2190973"><a href="/opinion/2190973/state-v-smith/" aria-description="Citation for case: State v. Smith">73 N. W. 2d 189</a></span> (admissible) .</p>
<p id="AE1Z">Kansas</p>
<p id="Aic">Pre-Weeks: <em>State </em>v. <em>Miller, </em><span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">63 Kan. 62</a></span>, <span class="citation" data-id="7891978"><a href="/opinion/7941374/state-v-miller/" aria-description="Citation for case: State v. Miller">64 P. 1033</a></span> (admissible).</p>
<p id="ApS">Pre-Wolf: <em>State </em>v. <em>Johnson, </em><span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">116 Kan. 58</a></span>, <span class="citation" data-id="7907024"><a href="/opinion/7955587/state-v-johnson/" aria-description="Citation for case: State v. Johnson">226 P. 245</a></span> (admissible).</p>
<p id="Aqo">Post-Wolf: <em>State </em>v. <em>Peasley, </em><span class="citation" data-id="1122381"><a href="/opinion/1122381/state-v-peasley/" aria-description="Citation for case: State v. Peasley">179 Kan. 314</a></span>, <span class="citation" data-id="1122381"><a href="/opinion/1122381/state-v-peasley/" aria-description="Citation for case: State v. Peasley">295 P. 2d 627</a></span> (admissible) :</p>
<p id="AOms">Kentucky</p>
<p id="AmZ">Pre-Weeks: no holding.</p>
<p id="AKM">Pre-Wolf: <em>Youman v. Commonwealth, </em><span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">189 Ky. 152</a></span>, <span class="citation" data-id="7146240"><a href="/opinion/7233831/youman-v-commonwealth/" aria-description="Citation for case: Youman v. Commonwealth">224 S. W. 860</a></span> (excludable).</p>
<p id="AqA"><page-number citation-index="1" label="228">*228</page-number>Post-Wolf: <em>Johnson </em>v. <em>Commonwealth, </em><span class="citation" data-id="5021031"><a href="/opinion/5198082/johnson-v-commonwealth/" aria-description="Citation for case: Johnson v. Commonwealth">296 S. W. 2d 210</a></span> (Ct. App. Kentucky) (excludable).</p>
<p id="AKP">Louisiana</p>
<p id="ARs">Pre-Weeks: no holding.</p>
<p id="A8q">Pre-Wolf: <em>State </em>v. <em>Fleckinger, </em><span class="citation no-link">162 La. 337</span>, <span class="citation" data-id="7172750"><a href="/opinion/7258573/state-v-fleckinger/" aria-description="Citation for case: State v. Fleckinger">93 So. 115</a></span> (admissible).</p>
<p id="A0Z">Post-Wolf: <em>State </em>v. <em>Mastricovo, </em><span class="citation" data-id="1660499"><a href="/opinion/1660499/state-v-mastricovo/" aria-description="Citation for case: State v. Mastricovo">221 La. 312</a></span>, <span class="citation" data-id="1660499"><a href="/opinion/1660499/state-v-mastricovo/" aria-description="Citation for case: State v. Mastricovo">59 So. 2d 403</a></span> (admissible) .</p>
<p id="ATk">Maine</p>
<p id="AHE">Pre-Weeks: <em>State </em>v. <em>Gorham, </em><span class="citation" data-id="4932917"><a href="/opinion/5114261/state-v-gorham/" aria-description="Citation for case: State v. Gorham">65 Me. 270</a></span> (admissible) (semble).</p>
<p id="AuxD">Pre-Wolf: <em>State </em>v. <em>Schoppe, </em><span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/" aria-description="Citation for case: State v. Schoppe">113 Me. 10</a></span>, <span class="citation" data-id="4938095"><a href="/opinion/5119383/state-v-schoppe/" aria-description="Citation for case: State v. Schoppe">92 A. 867</a></span> (admissible) <em>(semble),</em></p>
<p id="ApT">Post-Wolf: <em>no </em>holding.</p>
<p id="Ag9">MARYLAND</p>
<p id="AZq">Pre-Weeks: <em>Lawrence </em>v. <em>State, </em><span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/" aria-description="Citation for case: Lawrence v. State">103 Md. 17</a></span>, <span class="citation" data-id="3487094"><a href="/opinion/3489145/lawrence-v-state/" aria-description="Citation for case: Lawrence v. State">63 A. 96</a></span> (admissible).</p>
<p id="Az4">Pre-Wolf: <em>Meisinger </em>v. <em>State, </em><span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">155 Md. 195</a></span>, <span class="citation" data-id="3484807"><a href="/opinion/3486914/meisinger-v-state/" aria-description="Citation for case: Meisinger v. State">141 A. 536</a></span> (admissible) .</p>
<p id="AGnC">Post-Wolf: <em>Stevens </em>v. <em>State, </em><span class="citation" data-id="1921065"><a href="/opinion/1921065/stevens-v-state/" aria-description="Citation for case: Stevens v. State">202 Md. 117</a></span>, <span class="citation" data-id="1921065"><a href="/opinion/1921065/stevens-v-state/" aria-description="Citation for case: Stevens v. State">95 A. 2d 877</a></span> (admissible). (Flack’s Md. Ann. Code, 1951, Art. 35, § 5 requires the exclusion of illegally obtained evidence in the trial of most misdemeanors.)</p>
<p id="Aaa">Massachusetts</p>
<p id="AWR">Pre-Weeks: <em>Commonwealth </em>v. <em>Dana, </em><span class="citation" data-id="6407794"><a href="/opinion/6534076/commonwealth-v-dana/" aria-description="Citation for case: Commonwealth v. Dana">43 Mass. 329</a></span> (admissible).</p>
<p id="A6P">Pre-Wolf: <em>Commonwealths. Wilkins, </em><span class="citation" data-id="6436025"><a href="/opinion/6562275/commonwealth-v-wilkins/" aria-description="Citation for case: Commonwealth v. Wilkins">243 Mass. 356</a></span>, <span class="citation no-link">138 N. E. 11</span> (admissible).</p>
<p id="As2">Post-Wolf: no holding.</p>
<p id="Av5">Michigan</p>
<p id="AzD">Pre-Weeks: <em>People </em>v. <em>Aldorfer, </em><span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">164 Mich. 676</a></span>, <span class="citation" data-id="7946344"><a href="/opinion/7992842/people-v-aldorfer/" aria-description="Citation for case: People v. Aldorfer">130 N. W. 351</a></span> (admissible).</p>
<p id="A2T">Pre-Wolf: <em>People </em>v. <em>Marxhausen, </em><span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">204 Mich. 559</a></span>, <span class="citation" data-id="7950359"><a href="/opinion/7996598/people-v-marxhausen/" aria-description="Citation for case: People v. Marxhausen">171 N. W. 557</a></span> (excludable).</p>
<p id="AZL">Post-Wolf: <em>People </em>v. <em>Hildabridle, </em><span class="citation" data-id="9527923"><a href="/opinion/2041058/people-v-hildabridle/" aria-description="Citation for case: People v. Hildabridle">353 Mich. 562</a></span>, <span class="citation" data-id="9527923"><a href="/opinion/2041058/people-v-hildabridle/" aria-description="Citation for case: People v. Hildabridle">92 N. W. 2d 6</a></span> (excludable).</p>
<p id="AUa">(Art. II, § 10 of the Michigan Constitution of 1908, as amended, sets forth a limited class of items which are not excludable. See <em>People </em>v. <em>Gonzales, </em><span class="citation" data-id="9741641"><a href="/opinion/2228330/people-v-gonzales/" aria-description="Citation for case: People v. Gonzales">356 Mich. 247</a></span>, 97 N.- W. 2d 16.)</p>
<p id="A-b">Minnesota</p>
<p id="Ar0">Pre-Weeks: <em>State </em>v. <em>Strait, </em><span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">94 Minn. 384</a></span>, <span class="citation" data-id="7973247"><a href="/opinion/8017916/state-v-strait/" aria-description="Citation for case: State v. Strait">102 N. W. 913</a></span> (admissible).</p>
<p id="A_m">Pre-Wolf: <em>State </em>v. <em>Pluth, </em><span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">157 Minn. 145</a></span>, <span class="citation" data-id="7981382"><a href="/opinion/8025591/state-v-pluth/" aria-description="Citation for case: State v. Pluth">195 N. W. 789</a></span> (admissible).</p>
<p id="AAR">Post-Wolf: no holding.</p>
<p id="b303-5"><page-number citation-index="1" label="229">*229</page-number>Mississippi</p>
<p id="b303-6">Pre-Weeks: no holding.</p>
<p id="b303-7">Pre-Wolf: <em>Tucker </em>v. <em>State, </em><span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">128 Miss. 211</a></span>, <span class="citation" data-id="7994199"><a href="/opinion/8037845/tucker-v-state/" aria-description="Citation for case: Tucker v. State">90 So. 845</a></span> (excludable).</p>
<p id="b303-8">Post-Wolf: <em>Nobles </em>v. <em>State, </em><span class="citation" data-id="7996204"><a href="/opinion/8039738/nobles-v-state/" aria-description="Citation for case: Nobles v. State">222 Miss. 827</a></span>, <span class="citation" data-id="7996204"><a href="/opinion/8039738/nobles-v-state/" aria-description="Citation for case: Nobles v. State">77 So. 2d 288</a></span> (excludable) .</p>
<p id="b303-9">Missouri</p>
<p id="b303-10">Pre-Weeks: <em>State </em>v. <em>Pomeroy, </em><span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">130 Mo. 489</a></span>, <span class="citation" data-id="8011909"><a href="/opinion/8054876/state-v-pomeroy/" aria-description="Citation for case: State v. Pomeroy">32 S. W. 1002</a></span> (admissible) .</p>
<p id="b303-11">Pre-Wolf: <em>State </em>v. <em>Owens, </em><span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">302 Mo. 348</a></span>, <span class="citation" data-id="3529427"><a href="/opinion/3553710/state-v-owens/" aria-description="Citation for case: State v. Owens">259 S. W. 100</a></span> (excludable) .</p>
<p id="b303-12">Post-Wolf: <em>State </em>v. <em>Hunt, </em><span class="citation" data-id="2466177"><a href="/opinion/2466177/state-v-hunt/" aria-description="Citation for case: State v. Hunt">280 S. W. 2d 37</a></span> (Sup. Ct. Missouri) (excludable).</p>
<p id="b303-13">Montana</p>
<p id="b303-14">Pre-Weeks: <em>State </em>v. <em>Fuller, </em><span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/" aria-description="Citation for case: State v. Fuller">34 Mont. 12</a></span>, <span class="citation" data-id="8020864"><a href="/opinion/8063090/state-v-fuller/" aria-description="Citation for case: State v. Fuller">85 P. 369</a></span> (admissible).</p>
<p id="b303-15">Pre-Wolf: <em>State ex rel. King </em>v. <em>District Court, </em><span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">70 Mont. 191</a></span>, <span class="citation" data-id="8024014"><a href="/opinion/8066072/state-ex-rel-king-v-district-court/" aria-description="Citation for case: State ex rel. King v. District Court">224 P. 862</a></span> (excludable).</p>
<p id="b303-16">Post-Wolf: no holding.</p>
<p id="b303-17">Nebraska</p>
<p id="b303-18">Pre-Weeks: <em>Geiger </em>v. <em>State, </em><span class="citation" data-id="6642402"><a href="/opinion/6759719/geiger-v-state/" aria-description="Citation for case: Geiger v. State">6 Neb. 545</a></span> (admissible).</p>
<p id="b303-19">Pre-Wolf: <em>Billings </em>v. <em>State, </em><span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">109 Neb. 596</a></span>, <span class="citation" data-id="8032854"><a href="/opinion/8074092/billings-v-state/" aria-description="Citation for case: Billings v. State">191 N. W. 721</a></span> (admissible) .</p>
<p id="b303-20">Post-Wolf: <em>Haswell </em>v. <em>State, </em><span class="citation" data-id="2041065"><a href="/opinion/2041065/haswell-v-state/" aria-description="Citation for case: Haswell v. State">167 Neb. 169</a></span>, <span class="citation" data-id="2041065"><a href="/opinion/2041065/haswell-v-state/" aria-description="Citation for case: Haswell v. State">92 N. W. 2d 161</a></span> (admissible).</p>
<p id="b303-21">Nevada</p>
<p id="b303-22">Pre-Weeks:- no holding.</p>
<p id="b303-23">Pre-Wolf: <em>State </em>v. <em>Chin Gim, </em><span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">47 Nev. 431</a></span>, <span class="citation" data-id="8042834"><a href="/opinion/8083180/state-v-chin-gim/" aria-description="Citation for case: State v. Chin Gim">224 P. 798</a></span> (admissible) .</p>
<p id="b303-24">Post-Wolf: no holding.</p>
<p id="b303-25">New Hampshire</p>
<p id="b303-26">Pre-Weeks: <em>State </em>v. <em>Flynn, </em>36 N. H. 64 (admissible).</p>
<p id="b303-27">Pre-Wolf: <em>State </em>v. <em>Agalos, </em>79 N. H. 241, <span class="citation" data-id="3553875"><a href="/opinion/3573624/state-v-agalos/" aria-description="Citation for case: State v. Agalos">107 A. 314</a></span> (admissible) .</p>
<p id="b303-28">Post-Wolf: <em>State </em>v. <em>Mara, </em>96 N. H. 463, <span class="citation" data-id="2302903"><a href="/opinion/2302903/state-v-mara/" aria-description="Citation for case: State v. Mara">78 A. 2d 922</a></span> (admissible) .</p>
<p id="b303-29">New Jersey</p>
<p id="b303-30">Pre-Weeks: no holding</p>
<p id="b303-31">Pre-Wolf: <em>State </em>v. <em>Black, </em>5 N. J. Misc. 48, <span class="citation" data-id="8506298"><a href="/opinion/8533787/state-v-black/" aria-description="Citation for case: State v. Black">135 A. 685</a></span> (admissible) .</p>
<p id="b303-32">Post-Wolf: <em>Eleuteri </em>v. <em>Richman, </em>26 N. J. 506, <span class="citation" data-id="1934063"><a href="/opinion/1934063/eleuteri-v-richman/" aria-description="Citation for case: Eleuteri v. Richman">141 A. 2d 46</a></span> (admissible).</p>
<p id="b303-33">(N. J. Rev. Stat. 33:1-62 provides for the return of items illegally seized in the investigation of certain alcohol control offenses.)</p>
<p id="b304-4"><page-number citation-index="1" label="230">*230</page-number>New Mexico</p>
<p id="b304-5">Pre-Weeks: no holding.</p>
<p id="b304-6">Pre-Wolf: <em>State </em>v. <em>Dillon, </em>34 N. M. 366, <span class="citation" data-id="3571966"><a href="/opinion/3591159/state-v-dillon/" aria-description="Citation for case: State v. Dillon">281 P. 474</a></span> (admissible) .</p>
<p id="b304-7">Post-Wolf: <em>Breithaupt </em>v. <em>Abram, </em>58 N. M. 385, <span class="citation" data-id="6469115"><a href="/opinion/6594277/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">271 P. 2d 827</a></span> (admissible).</p>
<p id="b304-8">New Yoke</p>
<p id="b304-9">Pre-Weeks: <em>People </em>v. <em>Adams, </em><span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span> (admissible) .</p>
<p id="b304-10">Pre-Wolf: <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (admissible).</p>
<p id="b304-11">Post-Wolf: <em>People </em>v. <em>Variano, </em>5 N. Y. 2d 391, <span class="citation" data-id="5517425"><a href="/opinion/5670276/people-v-variano/" aria-description="Citation for case: People v. Variano">157 N. E. 2d 857</a></span> (admissible).</p>
<p id="b304-12">North Carolina</p>
<p id="b304-13">Pre-Weeks: <em>State </em>v. <em>Wallace, </em><span class="citation" data-id="6695783"><a href="/opinion/6809677/state-v-wallace/" aria-description="Citation for case: State v. Wallace">162 N. C. 622</a></span>, <span class="citation" data-id="3672959"><a href="/opinion/3926369/s-v-wallace/" aria-description="Citation for case: S. v. . Wallace">78 S. E. 1</a></span> (admissible).</p>
<p id="b304-14">Pre-Wolf: <em>State </em>v. <em>Simmons, </em><span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">183 N. C. 684</a></span>, <span class="citation" data-id="3646527"><a href="/opinion/3900534/state-v-simmons/" aria-description="Citation for case: State v. . Simmons">110 S. E. 591</a></span> (admissible).</p>
<p id="b304-15">Post-Wolf: <em>State </em>v. <em>Mills, </em><span class="citation" data-id="1328981"><a href="/opinion/1328981/state-v-mills/" aria-description="Citation for case: State v. Mills">246 N. C. 237</a></span>, <span class="citation" data-id="1328981"><a href="/opinion/1328981/state-v-mills/" aria-description="Citation for case: State v. Mills">98 S. E. 2d 329</a></span> (excludable) .</p>
<p id="b304-16">(N. C. Gen. Stat. § 15-27 requires the exclusion of illegally obtained evidence.)</p>
<p id="b304-17">North Dakota</p>
<p id="b304-18">Pre-Weeks: no holding.</p>
<p id="b304-19">Pre-Wolf: <em>State </em>v. <em>Fahn, </em><span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">53 N. D. 203</a></span>, <span class="citation" data-id="3682031"><a href="/opinion/3934924/state-v-fahn/" aria-description="Citation for case: State v. Fahn">205 N. W. 67</a></span> (admissible).</p>
<p id="b304-20">Post-Wolf: no holding.</p>
<p id="b304-21">Ohio</p>
<p id="b304-22">Pre-Weeks: no holding.</p>
<p id="b304-23">Pre-Wolf: <em>State </em>v. <em>Lindway, </em><span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">131 Ohio St. 166</a></span>, <span class="citation" data-id="3780866"><a href="/opinion/4024496/state-v-lindway/" aria-description="Citation for case: State v. Lindway">2 N. E. 2d 490</a></span> (admissible).</p>
<p id="b304-24">Post-Wolf: <em>State </em>v. <em>Mapp, </em><span class="citation no-link">170 Ohio St. 427</span>, <span class="citation no-link">166 N. E. 2d 387</span> (admissible).</p>
<p id="b304-25">Oklahoma</p>
<p id="b304-26">Pre-Weeks: <em>Silva </em>v. <em>State, </em><span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">6 Okla. Cr. 97</a></span>, <span class="citation" data-id="3827556"><a href="/opinion/4069690/silva-v-state/" aria-description="Citation for case: Silva v. State">116 P. 199</a></span> (admissible).</p>
<p id="b304-27">Pre-Wolf: <em>Gore </em>v. <em>State, </em><span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">24 Okla. Cr. 394</a></span>, <span class="citation" data-id="3812264"><a href="/opinion/4054922/gore-v-state/" aria-description="Citation for case: Gore v. State">218 P. 545</a></span> (excludable) .</p>
<p id="b304-28">Post-Wolf: <em>Hamel </em>v. <em>State, </em><span class="citation" data-id="2619395"><a href="/opinion/2619395/hamel-v-state/" aria-description="Citation for case: Hamel v. State">317 P. 2d 285</a></span> (Okla. Crim.) (ex-cludable) .</p>
<p id="b304-29">Oregon</p>
<p id="b304-30">Pre-Weeks: <em>State </em>v. <em>McDaniel, </em><span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/" aria-description="Citation for case: State v. McDaniel">39 Ore. 161</a></span>, <span class="citation" data-id="6898602"><a href="/opinion/6999518/state-v-mcdaniel/" aria-description="Citation for case: State v. McDaniel">65 P. 520</a></span> (admissible).</p>
<p id="b304-31">Pre-Wolf: See <em>State </em>v. <em>Laundy, </em><span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/" aria-description="Citation for case: State v. Laundy">103 Ore. 443</a></span>, <span class="citation" data-id="6907613"><a href="/opinion/7007488/state-v-laundy/" aria-description="Citation for case: State v. Laundy">204 P. 958</a></span> (excludable), although see <em>State </em>v. <em>Folkes, </em><span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/" aria-description="Citation for case: State v. Folkes">174 Ore. 568</a></span>, <span class="citation" data-id="3842073"><a href="/opinion/4083033/state-v-folkes/" aria-description="Citation for case: State v. Folkes">150 P. 2d 17</a></span> (not noticing <em>State v. Laundy).</em></p>
<p id="b304-32">Post-Wolf: <em>State </em>v. <em>Hoover, </em><span class="citation" data-id="2615411"><a href="/opinion/2615411/state-v-hoover/" aria-description="Citation for case: State v. Hoover">219 Ore. 288</a></span>, <span class="citation" data-id="2615411"><a href="/opinion/2615411/state-v-hoover/" aria-description="Citation for case: State v. Hoover">347 P. 2d 69</a></span> (questioning <em>Laundy).</em></p>
<p id="b305-5"><page-number citation-index="1" label="231">*231</page-number>Pennsylvania</p>
<p id="b305-6">Pre-Weeks: no holding.</p>
<p id="b305-7">Pre-Wolf: <em>Commonwealth </em>v. <em>Dabbierio, </em><span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">290 Pa. 174</a></span>, <span class="citation" data-id="3848320"><a href="/opinion/4089084/commonwealth-v-dabbierio/" aria-description="Citation for case: Commonwealth v. Dabbierio">138 A. 679</a></span> (admissible).</p>
<p id="b305-8">Post-Wolf: <em>Commonwealth </em>v. <em>Chaitt, </em><span class="citation" data-id="9735584"><a href="/opinion/2199709/commonwealth-v-chaitt/" aria-description="Citation for case: Commonwealth v. Chaitt">380 Pa. 532</a></span>, <span class="citation" data-id="9735584"><a href="/opinion/2199709/commonwealth-v-chaitt/" aria-description="Citation for case: Commonwealth v. Chaitt">112 A. 2d 379</a></span> (admissible).</p>
<p id="b305-9">Rhode Island</p>
<p id="b305-10">Pre-Weeks: no holding.</p>
<p id="b305-11">Pre-Wolf: no holding.</p>
<p id="b305-12">Post-Wolf: <em>State </em>v. <em>Hillman, </em>84 R. I. 396, <span class="citation" data-id="1493506"><a href="/opinion/1493506/state-v-hillman/" aria-description="Citation for case: State v. Hillman">125 A. 2d 94</a></span> (applying common law rule, but noticing the enactment of the statutory rule).</p>
<p id="b305-13">(R. I. Gen. Laws, 1956, § 9-19-25 requires the exclusion of illegally obtained evidence.)</p>
<p id="b305-14">South Carolina</p>
<p id="b305-15">Pre-Weeks: <em>State </em>v. <em>Atkinson, </em>40 S. C. 363, <span class="citation" data-id="6678093"><a href="/opinion/6793472/state-v-atkinson/" aria-description="Citation for case: State v. Atkinson">18 S. E. 1021</a></span> (admissible) .</p>
<p id="b305-16">Pre-Wolf: <em>State </em>v. <em>Green, </em>121 S. C. 230, <span class="citation no-link">114 S. E. 317</span> (admissible) .</p>
<p id="b305-17">Post-Wolf: <em>State </em>v. <em>Anderson, </em>230 S. C. 191, <span class="citation" data-id="1380217"><a href="/opinion/1380217/state-v-anderson/" aria-description="Citation for case: State v. Anderson">95 S. E. 2d 164</a></span> (admissible).</p>
<p id="b305-18">South Dakota</p>
<p id="b305-19">Pre-Weeks: <em>State </em>v. <em>Madison, </em>23 S. D. 584, <span class="citation" data-id="6687221"><a href="/opinion/6802175/state-v-madison/" aria-description="Citation for case: State v. Madison">122 N. W. 647</a></span> (admissible) .</p>
<p id="b305-20">Pre-Wolf: <em>State </em>v. <em>Gooder, </em>57 S. D. 619, <span class="citation" data-id="6692555"><a href="/opinion/6806990/state-v-gooder/" aria-description="Citation for case: State v. Gooder">234 N. W. 610</a></span> (excludable) .</p>
<p id="b305-21">Post-Wolf: <em>State </em>v. <em>Poppenga, </em>76 S. D. 592, <span class="citation" data-id="1680451"><a href="/opinion/1680451/state-v-poppenga/" aria-description="Citation for case: State v. Poppenga">83 N. W. 2d 518</a></span> (excludable).</p>
<p id="b305-22">S. D. Code, 1939, § 34.1102 provides for a limited return to the common-law rule of admissibility. See <em>State </em>v. <em>Lane, </em>76 S. D. 544, 82 N. W. 2d. 286.</p>
<p id="b305-23">Tennessee</p>
<p id="b305-24">Pre-Weeks: <em>Cohn </em>v. <em>State, </em><span class="citation" data-id="8300564"><a href="/opinion/8332572/cohn-v-state/" aria-description="Citation for case: Cohn v. State">120 Tenn. 61</a></span>, <span class="citation" data-id="3980535"><a href="/opinion/4208407/parriss-v-hughes/" aria-description="Citation for case: Parriss v. Hughes">109 S. W. 1149</a></span> (admissible).</p>
<p id="b305-25">Pre-Wolf: <em>Hughes </em>v. <em>State, </em><span class="citation" data-id="8302107"><a href="/opinion/8334068/hughes-v-state/" aria-description="Citation for case: Hughes v. State">145 Tenn. 544</a></span>, <span class="citation no-link">238 S. W. 588</span> (excludable).</p>
<p id="b305-26">Post-Wolf: <em>Lindsey </em>v. <em>State, </em><span class="citation" data-id="8302925"><a href="/opinion/8334836/lindsey-v-state/" aria-description="Citation for case: Lindsey v. State">191 Tenn. 51</a></span>, <span class="citation" data-id="8302925"><a href="/opinion/8334836/lindsey-v-state/" aria-description="Citation for case: Lindsey v. State">231 S. W. 2d 380</a></span> (excludable).</p>
<p id="b305-27">Texas</p>
<p id="b305-28">Pre-Weeks: no holding.</p>
<p id="b305-29">Pre-Wolf: <em>Chapin </em>v. <em>State, </em><span class="citation" data-id="3948208"><a href="/opinion/4179831/chapin-v-state/" aria-description="Citation for case: Chapin v. State">107 Tex. Cr. R. 477</a></span>, <span class="citation" data-id="3948208"><a href="/opinion/4179831/chapin-v-state/" aria-description="Citation for case: Chapin v. State">296 S. W. 1095</a></span> (excludable).</p>
<p id="b306-5"><page-number citation-index="1" label="232">*232</page-number>Post-Wolf: <em>Williamson </em>v. <em>State, </em><span class="citation" data-id="1670307"><a href="/opinion/1670307/williamson-v-state/" aria-description="Citation for case: Williamson v. State">156 Tex. Cr. R. 520</a></span>, <span class="citation" data-id="1670307"><a href="/opinion/1670307/williamson-v-state/" aria-description="Citation for case: Williamson v. State">244 S. W. 2d 202</a></span> (excludable).</p>
<p id="b306-6">(Vernon’s Tex. Stat., 1948 (Code Crim. Proc., Art. 72a) requires the exclusion of illegally obtained evidence.)</p>
<p id="b306-7">Utah</p>
<p id="b306-8">Pre-Weeks: no holding.</p>
<p id="b306-9">Pre-Wolf: <em>State </em>v. <em>Aime, </em><span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">62 Utah 476</a></span>, <span class="citation" data-id="8657438"><a href="/opinion/8674530/state-v-aime/" aria-description="Citation for case: State v. Aime">220 P. 704</a></span> (admissible). Post-Wolf: no holding.</p>
<p id="b306-10">Vermont</p>
<p id="b306-11">Pre-Weeks: <em>State </em>v. <em>Mathers, </em><span class="citation" data-id="6583727"><a href="/opinion/6703627/state-v-mathers/" aria-description="Citation for case: State v. Mathers">64 Vt. 101</a></span>, <span class="citation no-link">23 A. 590</span> (admissible).</p>
<p id="AR3">Pre-Wolf: <em>State </em>v. <em>Stacy, </em><span class="citation" data-id="3990360"><a href="/opinion/4216163/state-v-stacy/" aria-description="Citation for case: State v. Stacy">104 Vt. 379</a></span>, <span class="citation no-link">160 A. 257</span> (admissible).</p>
<p id="ANu">Post-Wolf: <em>In re Raymo, </em><span class="citation" data-id="1505389"><a href="/opinion/1505389/in-re-raymos-petition/" aria-description="Citation for case: In Re Raymo&#x27;s Petition">121 Vt. 246</a></span>, <span class="citation" data-id="1505389"><a href="/opinion/1505389/in-re-raymos-petition/" aria-description="Citation for case: In Re Raymo&#x27;s Petition">154 A. 2d 487</a></span> (admissible).</p>
<p id="b306-12">Virginia</p>
<p id="b306-13">Pre-Weeks: no holding.</p>
<p id="b306-14">Pre-Wolf: <em>Hall v. Commonwealth, </em><span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">138 Va. 727</a></span>, <span class="citation" data-id="6815460"><a href="/opinion/6919821/hall-v-commonwealth/" aria-description="Citation for case: Hall v. Commonwealth">121 S. E. 154</a></span> (admissible).</p>
<p id="b306-15">Post-Wolf: no holding.</p>
<p id="b306-16">Washington</p>
<p id="b306-17">Pre-Weeks: <em>State </em>v. <em>Royce, </em><span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">38 Wash. 111</a></span>, <span class="citation" data-id="4726508"><a href="/opinion/4919818/state-v-royce/" aria-description="Citation for case: State v. Royce">80 P. 268</a></span> (admissible).</p>
<p id="AmZF">Pre-Wolf: <em>State </em>v. <em>Gibbons, </em><span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">118 Wash. 171</a></span>, <span class="citation" data-id="4720844"><a href="/opinion/4914645/state-v-gibbons/" aria-description="Citation for case: State v. Gibbons">203 P. 390</a></span> (excludable) .</p>
<p id="b306-18">Post-Wolf: <em>State </em>v. <em>Cyr, </em><span class="citation" data-id="1178849"><a href="/opinion/1178849/state-v-cyr/" aria-description="Citation for case: State v. Cyr">40 Wash. 2d 840</a></span>, <span class="citation" data-id="1178849"><a href="/opinion/1178849/state-v-cyr/" aria-description="Citation for case: State v. Cyr">246 P. 2d 480</a></span> (excludable) .</p>
<p id="b306-19">West Virginia</p>
<p id="b306-20">Pre-Weeks: <em>State </em>v. <em>Edwards, </em><span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/" aria-description="Citation for case: State v. Edwards">51 W. Va. 220</a></span>, <span class="citation" data-id="8175125"><a href="/opinion/8212628/state-v-edwards/" aria-description="Citation for case: State v. Edwards">41 S. E. 429</a></span> (admissible).</p>
<p id="b306-21">Pre-Wolf: <em>State </em>v. <em>Wills, </em><span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/" aria-description="Citation for case: State v. Wills">91 W. Va. 659</a></span>, <span class="citation" data-id="8179537"><a href="/opinion/8216688/state-v-wills/" aria-description="Citation for case: State v. Wills">114 S. E. 261</a></span> (excludable) .</p>
<p id="b306-22">Post-Wolf: <em>State </em>v. <em>Calandros, </em><span class="citation" data-id="9621257"><a href="/opinion/1401576/state-v-calandros/" aria-description="Citation for case: State v. Calandros">140 W. Va. 720</a></span>, <span class="citation" data-id="9621257"><a href="/opinion/1401576/state-v-calandros/" aria-description="Citation for case: State v. Calandros">86 S. E. 2d 242</a></span> (excludable).</p>
<p id="b306-23">Wisconsin</p>
<p id="b306-24">Pre-Weeks: no holding.</p>
<p id="b306-25">Pre-Wolf: <em>Hoyer </em>v. <em>State, </em><span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">180 Wis. 407</a></span>, <span class="citation" data-id="8194030"><a href="/opinion/8229755/hoyer-v-state/" aria-description="Citation for case: Hoyer v. State">193 N. W. 89</a></span> (excludable).</p>
<p id="A8H">Post-Wolf: <em>State </em>v. <em>Kroening, </em><span class="citation" data-id="9520934"><a href="/opinion/2022531/state-v-kroening/" aria-description="Citation for case: State v. Kroening">274 Wis. 266</a></span>, <span class="citation no-link">79 N. W. 2d 810</span> (excludable).</p>
<p id="b306-26">Wyoming</p>
<p id="b306-27">Pre-Weeks: no holding.</p>
<p id="b306-28">Pre-Wolf: <em>State </em>v. <em>George, </em><span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">32 Wyo. 223</a></span>, <span class="citation" data-id="4012941"><a href="/opinion/4235695/state-v-george/" aria-description="Citation for case: State v. George">231 P. 683</a></span> (excludable).</p>
<p id="ANj">Post-Wolf: no holding.</p>
<footnote label="1">
<p id="b281-5"> The state officers, having received information that petitioners had in their possession obscene motion pictures, procured a search warrant to search petitioner Clark’s home. The affidavit upon which the warrant was based recited that “upon information and belief” it was thought that Clark possessed obscene pictures and accompanying sound recordings. The search revealed no obscene pictures, but various paraphernalia believed to have been used in making wiretaps were found and seized.</p>
<p id="b281-6">Following an appropriate motion, the Multnomah County District Court held the search warrant invalid and ordered suppression of the evidence. This action came, however, after the return of an indictment by a state grand jury, and the local district attorney challenged the power of the district court to suppress evidence once an indictment was in. Accordingly, the question was later argued anew on a motion to suppress in the Circuit Court for. Multnomah County, a court of general criminal jurisdiction. That court held the search unlawful and granted the motion to suppress. The state indictment was subsequently dismissed.</p>
<p id="b281-7">During the course of these state proceedings federal officers,- acting under a federal search warrant, obtained the articles from the safe-deposit box of a local bank where the state officials had placed them. Shortly after the state case was abandoned, a federal indictment was returned, and the instant prosecution followed.</p>
</footnote>
<footnote label="2">
<p id="b282-8"> The “silver platter” label stems from a phrase first turned in the prevailing opinion in <em>Lustig </em>v. <em>United States, </em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/#79" aria-description="Citation for case: Lustig v. United States">338 U. S. 74, 79</a></span>. The doctrine has been the subject of much comment in legal periodicals. See, <em>e.g., </em>Allen, The Wolf Casé: Search and Seizure, Federalism, and the Civil Liberties, 45 Ill. L. Rev. 1, 14-25; Galler, The Exclusion of Illegal State Evidence in Federal Courts, 49 J. Crim. L., Criminology <em>&amp; </em>Police Science 455; Kohn, Admissibility in Federal Court of Evidence Illegally Seized by State Officers, 1959 Wash. U. L. Q. 229; Kamisar, <em><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span> </em>and <em><span class="citation" data-id="9420385"><a href="/opinion/104713/lustig-v-united-states/" aria-description="Citation for case: Lustig v. United States">Lustig</a></span> </em>Ten Years Later: Illegal State Evidence in State and Federal Courts, <span class="citation no-link">43 Minn. L. Rev. 1083</span>; Parsons, State-Federal Crossfire in Search and Seizure and Self Incrimination, 42 Cornell L. Q. 346, 347-368; Comment, The <em>Benanti </em>Case: State Wiretap Evidence and the Federal Exclusionary Rule, 57 Col. L. Rev. 1159; Comment, Judicial Control of Illegal Search and Seizure, 58 Yale L. J. 144; Notes, 51 Col. L. Rev. 128, <span class="citation no-link">27 Geo. Wash. L. Rev. 392</span>. 5 N. Y. L. F. 301. 6 U. C. L. A. Rev. 703.</p>
</footnote>
<footnote label="3">
<p id="b284-8"> See, <em>e. g., Rettich </em>v. <em>United States, </em><span class="citation" data-id="1489412"><a href="/opinion/1489412/rettich-v-united-states/" aria-description="Citation for case: Rettich v. United States">84 F. 2d 118</a></span> (C. A. 1st Cir.); <em>Milburne </em>v. <em>United States, </em><span class="citation" data-id="6863032"><a href="/opinion/6965605/milburne-v-united-states/" aria-description="Citation for case: Milburne v. United States">77 F. 2d 310</a></span> (C. A. 2d Cir.); <em>Miller </em>v. <em>United States, </em><span class="citation" data-id="1549055"><a href="/opinion/1549055/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">50 F. 2d 505</a></span> (C. A. 3d Cir.); <em>Riggs </em>v. <em>United States, </em><span class="citation" data-id="9335930"><a href="/opinion/9340586/riggs-v-states/" aria-description="Citation for case: Riggs v. States">299 Fed. 273</a></span> (C. A. 4th Cir.); <em>Timonen </em>v. <em>United States, </em><span class="citation" data-id="8829031"><a href="/opinion/8843810/timonen-v-united-states/" aria-description="Citation for case: Timonen v. United States">286 Fed. 935</a></span> (C. A. 6th Cir.); <em>Fowler </em>v. <em>United States, </em><span class="citation" data-id="1472688"><a href="/opinion/1472688/fowler-v-united-states/" aria-description="Citation for case: Fowler v. United States">62 F. 2d 656</a></span> (C. A. 7th Cir.) (dictum); <em>Elam </em>v. <em>United States, </em><span class="citation" data-id="1509635"><a href="/opinion/1509635/elam-v-united-states/" aria-description="Citation for case: Elam v. United States">7 F. 2d 887</a></span> (C. A. 8th <page-number citation-index="1" label="211">*211</page-number>Cir.); <em>Brown </em>v. <em>United States, </em><span class="citation" data-id="1490225"><a href="/opinion/1490225/brown-v-united-states/" aria-description="Citation for case: Brown v. United States">12 F. 2d 926</a></span> (C. A. 9th Cir.); <em>Gilbert </em>v. <em>United States, </em><span class="citation" data-id="1498347"><a href="/opinion/1498347/gilbert-v-united-states/" aria-description="Citation for case: Gilbert v. United States">163 F. 2d 325</a></span> (C. A. 10th Cir.); <em>Shelton </em>v. <em>United States, </em>83 U. S. App. D. C. 257, <span class="citation" data-id="1476789"><a href="/opinion/1476789/shelton-v-united-states/" aria-description="Citation for case: Shelton v. United States">169 F. 2d 665</a></span>, overruled by <em>Hanna </em>v. <em>United States, </em>104 U. S. App. D. C. 205, <span class="citation" data-id="246433"><a href="/opinion/246433/samuel-j-hanna-v-united-states/" aria-description="Citation for case: Samuel J. Hanna v. United States">260 F. 2d 723</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b286-7"> Compare <em>Sutherland </em>v. <em>United States, </em><span class="citation" data-id="1501987"><a href="/opinion/1501987/sutherland-v-united-states/" aria-description="Citation for case: Sutherland v. United States">92 F. 2d 305</a></span> (C. A. 4th Cir.); <em>Ward </em>v. <em>United States, </em><span class="citation" data-id="9636747"><a href="/opinion/1475515/ward-v-united-states/" aria-description="Citation for case: Ward v. United States">96 F. 2d 189</a></span> (C. A.. 5th Cir.); <em>Fowler v. United States, </em><span class="citation" data-id="1472688"><a href="/opinion/1472688/fowler-v-united-states/" aria-description="Citation for case: Fowler v. United States">62 F. 2d 656</a></span> (C. A. 7th Cir.); <em>United States </em>v. <em>Butler, </em><span class="citation" data-id="1548044"><a href="/opinion/1548044/united-states-v-butler/" aria-description="Citation for case: United States v. Butler">156 F. 2d 897</a></span> (C. A. 10th Cir.); with <em>Kitt </em>v. <em>United States, </em><span class="citation" data-id="1480891"><a href="/opinion/1480891/kitt-v-united-states/" aria-description="Citation for case: Kitt v. United States">132 F. 2d 920</a></span> (C. A. 4th Cir.); <em>Sloane </em>v. <em>United States, </em><span class="citation" data-id="1501575"><a href="/opinion/1501575/sloane-v-united-states/" aria-description="Citation for case: Sloane v. United States">47 F. 2d 889</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="5">
<p id="b286-9"> Compare <em>United States v. Jankowski, </em><span class="citation" data-id="9642206"><a href="/opinion/1502497/united-states-v-jankowski/" aria-description="Citation for case: United States v. Jankowski">28 F. 2d 800</a></span> (C. A. 2d Cir.); <em>Marsh </em>v. <em>United States, </em><span class="citation" data-id="1483661"><a href="/opinion/1483661/marsh-v-united-states/" aria-description="Citation for case: Marsh v. United States">29 F. 2d 172</a></span> (C. A. 2d Cir.); with <em>United States </em>v. <em>Butler, </em><span class="citation" data-id="1548044"><a href="/opinion/1548044/united-states-v-butler/" aria-description="Citation for case: United States v. Butler">156 F. 2d 897</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="6">
<p id="b288-7"> See, e. <em>g., Burjord </em>v. <em>United States, </em><span class="citation" data-id="234366"><a href="/opinion/234366/burford-v-united-states/#125" aria-description="Citation for case: Burford v. United States">214 F. 2d 124, 125</a></span> (C. A. <em>5th </em>Cir.); <em>Ford </em>v. <em>United States, </em><span class="citation" data-id="239813"><a href="/opinion/239813/ralph-ford-v-united-states/#837" aria-description="Citation for case: Ralph Ford v. United States">234 F. 2d 835, 837</a></span> (C. A. 6th Cir.); <em>United States </em>v. <em>Moses, </em><span class="citation" data-id="239614"><a href="/opinion/239614/united-states-v-marvin-moses/" aria-description="Citation for case: United States v. Marvin Moses">234 F. 2d 124</a></span> (C. A. 7th Cir.); <em>Williams </em>v. <em>United States, 215 </em>F. 2d 695, 696 (C. A. 9th Cir.); <em>Gallegos </em>v. <em>United States, </em><span class="citation" data-id="240496"><a href="/opinion/240496/toby-anthony-gallegos-v-united-states-of-america-j-b-mingo-v-united/#696" aria-description="Citation for case: Toby Anthony Gallegos v. United States of America, J. B....">237 F. 2d 694, 696-697</a></span> (C. A. 10th Cir.).</p>
</footnote>
<footnote label="7">
<p id="b289-5"> Long before the Court established that the Fourteenth Amendment protects the security of one’s privacy against arbitrary intrusion by state officers, Mr. Justice (then Judge) Cardozo perceived a basic incongruity in a rule which excludes evidence unlawfully obtained by federal officers, but admits in the same court evidence unlawfully obtained by state agents. “The Federal rule as it stands is either too strict or too lax. A Federal prosecutor may take no benefit from evidence collected through the trespass of a Federal officer. . . . He does not have to be so scrupulous about evidence brought to him by others. How finely the line is drawn is seen when we recall that marshals in the service of the nation are on one side of it, and police in the service of.the States on the other. The nation may keep what the servants of the States supply. . . . We must go farther or not so far. The professed object of the trespass rather than the official character of the trespasser should test the rights of government. . . A government would be disingenuous, if, in determining the use that should be made of evidence drawn from such a source, it drew a line between them. This would be true whether they had acted in concert, or apart.” <em>People </em>v. <em>Defore, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#22" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 22-23</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#588" aria-description="Citation for case: People v. Defore">150 N. E. 585, 588</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b292-8"> The Director of the Federal Bureau of Investigation has written as follows:</p>
<p id="b292-9">“One of the quickest ways for any law enforcement officer to bring public disrepute upon himself, his organization and the entire profession is to be found guilty of a violation of civil rights. Our people may tolerate many mistakes of both intent and performance, but, with unerring instinct, they know that when any person is intentionally deprived of his constitutional rights those responsible have committed no ordinary offense. A crime of this nature, if subtly encouraged by failure to condemn and punish, certainly leads down the road to totalitarianism.</p>
<p id="b292-10">“Civil rights violations are all the more regrettable because they are so unnecessary. Professional standards in law enforcement pro<page-number citation-index="1" label="219">*219</page-number>vide for fighting crime with intelligence rather than force. ... In matters of scientific crime detection, the services of our FBI Laboratory are available to every duly constituted law enforcement officer in the nation. Full use of these and other facilities should make it entirely unnecessary for any officer to feel the need to use dishonorable methods.</p>
<p id="AqV-">“Complete protection of civil rights should be a primary concern of every officer. These rights are basic in the law and our obligation to uphold it leaves no room for any other course of action. Although the great majority in our profession have long since adopted that policy, we cannot yet be entirely proud of our record. Incidents which give justification to charges of civil rights violations by law enforcement officers still occur. . . . This state of affairs ought to be taken as a challenge to all of us. Every progressive police administrator and officer must do everything in his power to bring about such an improvement that our conduct and our record will conclusively prove each of these charges to be false.” FBI Law Enforcement Bulletin, September, 1952, pp. 1-2.</p>
</footnote>
<footnote label="9">
<p id="b293-7"> See Appendix, <em>post, </em>pp. 224^-225.</p>
</footnote>
<footnote label="10">
<p id="b293-8"> See Appendix, <em>post, </em>pp. 224-225.</p>
</footnote>
<footnote label="11">
<p id="b293-9"> For a discussion of recent developments in British Commonwealth jurisdictions, see Cowen, The Admissibility of Evidence Procured Through Illegal Searches and Seizures in British Commonwealth Jurisdictions, 5 Vanderbilt L. Rev. 523 (1952). The author concludes upon a survey of Commonwealth decisions “that there is no uniform rule on the admissibility of evidence procured through illegal searches and seizures.” <em>Id., </em>at 546.</p>
</footnote>
<footnote label="12">
<p id="b293-10"> North Carolina. See Appendix, <em>post, </em>p. 230.</p>
</footnote>
<footnote label="13">
<p id="b293-11"> Delaware and California. See Appendix, <em>post, </em>p. 226.</p>
</footnote>
<footnote label="14">
<p id="b294-9"> Rhode Island. See Appendix, <em>post, </em>p. 231.</p>
</footnote>
<footnote label="15">
<p id="b295-7"> Excerpt from letter of Governor Edmund G. Brown, then Attorney General of the State of California, to the Stanford Law Review, quoted in Note, <span class="citation no-link">9 Stan. L. Rev. 515</span>, 538 (1957). See also Barrett, Exclusion of Evidence Obtained by Illegal Searches — A Comment on People vs. Cahan, <span class="citation no-link">43 Cal. L. Rev. 565</span>, 586-588 (1955).</p>
</footnote>
<footnote label="16">
<p id="b297-7"> See Rule 41(e), Fed. Rules Crim. Proc. The defendant, of course, must have “standing” to object. See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>.</p>
</footnote>
<footnote label="*">
<p id="b299-42">Alaska and Hawaii both hold illegally obtained evidence to be ex-cludable, although it does not appear that either has passed anew on this question since attaining statehood.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Entick v. Carrington.md  (`case`, 5 assertions)

### content_page

```
---
title: "Entick v. Carrington"
type: case
citation: "19 How. St. Tr. 1029 (1765)"
parallel_cite: "95 Eng. Rep. 807; 2 Wils. K.B. 275"
neutral_cite: "[1765] EWHC KB J98"
court: "Court of Common Pleas (England)"
court_level: other
circuit: ""
year: 1765
date_decided: 1765-11-02
docket: ""
authority_weight: Historical
treatment:
  field_i_validity: good_law
  as_of_content: 1765-11-02
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Entick v. Carrington
  varies_by_point: false
  scope_note: "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Entick's foundational status is favorably restated by SCOTUS (Boyd, Jones, Riley). Authority weight remains Historical (English origin)."
  point_overrides: []
courtlistener:
  opinion_url: ""
  cluster_id: null
  opinion_id: null
  identity_checked: true
homes:
  - page: "[[Common Law Origins]]"
    role: "Key — Anchor (foundational origin)"
related: ["[[Wilkes v. Wood]]", "[[Boyd v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "historical", "common-law-origins", "general-warrant", "fourth-amendment", "trespass", "english-origins"]
holding: "A Secretary of State's general warrant to break into a home and seize the owner's books and papers in search of seditious libel is illegal: under the law of England every invasion of private property is a trespass requiring positive legal authority, and no such authority existed for this search and seizure."
lake:
  record_id: Entick v. Carrington
  status: verified_off_cl
  projected_at: 2026-07-07
off_cl_links:
  - source: BAILII
    url: "https://www.bailii.org/ew/cases/EWHC/KB/1765/J98.html"
    confirmed:
      caption: "Entick v Carrington & Ors"
      cite: "[1765] EWHC KB J98; 95 ER 807; 19 St Tr 1029; [1558-1774] All ER Rep 41"
      court: "King's Bench (BAILII retrospective filing label; historical court of decision: Court of Common Pleas, Camden CJ)"
      date: 1765-11-02
    checked_date: 2026-07-06
  - source: "Founders' Constitution"
    url: "https://press-pubs.uchicago.edu/founders/documents/amendIVs6.html"
    confirmed:
      caption: Entick v. Carrington
      cite: 95 Eng. Rep. 807
      court: "K.B. (Wilson's-Reports reprint label; historical court of decision: Court of Common Pleas)"
      date: 1765-11-02
    checked_date: 2026-07-06
---

# Entick v. Carrington

*19 How. St. Tr. 1029 (C.P. 1765)* · Court of Common Pleas (England) · **Historical** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
On a general warrant issued by the Earl of Halifax, a Secretary of State, the King's messenger Nathan Carrington and three others broke into the house of the writer John Entick, searched it for several hours, and carried away his books and papers, in search of evidence that Entick had written seditious libels (*The Monitor*). Entick sued the messengers in trespass. The defendants justified their conduct solely by the Secretary of State's warrant.

## Issue
Whether a Secretary of State's general warrant authorizing officers to break into a private home and seize the owner's papers, in search of seditious libel, was lawful authority for what would otherwise be a trespass.

## Rule
No. Lord Camden, C.J., grounded the decision in the protection of private property and the requirement of positive legal authority for any intrusion: "By the laws of England, every invasion of private property, be it ever so minute, is a trespass. No man can set his foot upon my ground without my licence, but he is liable to an action, though the damage be nothing …" — 19 How. St. Tr. at 1066; 95 Eng. Rep. at 817. ^pin-817

Because the executive could point to no law authorizing the warrant, it had none: "If it is law, it will be found in our books. If it is not to be found there, it is not law." — *Id.* ^pin-817b

## Application
The defendants could justify the entry and seizure only if some positive law authorized it. No statute and no precedent authorized a Secretary of State to issue a warrant to break into a private house and carry away the owner's papers in search of evidence of seditious libel. Silence in the law books was decisive: because no authority for the practice could be found, the warrant gave the messengers no legal protection, and their entry and seizure of Entick's papers were a trespass.

## Conclusion
Judgment for Entick. The general warrant was illegal and afforded the messengers no defense; intrusion upon a person's house and papers requires authority the law actually confers, which here did not exist.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Historical** (English origin; Court of Common Pleas).
- *Entick* is one of the two great English general-warrant cases (with [[Wilkes v. Wood]]) that the Fourth Amendment was written to enshrine. The U.S. Supreme Court has repeatedly treated it as authoritative on the original meaning of the Amendment — most famously in [[Boyd v. United States]], and it continues to be invoked in modern search-and-seizure decisions (e.g. the property-trespass theory revived in *[[United States v. Jones]]* and discussed alongside [[Katz v. United States]]). Its core principle remains good law.

## Appears on
- [[Common Law Origins]] — *Key — Anchor (foundational origin)*

## Sources
- *Entick v. Carrington*, 19 How. St. Tr. 1029 (C.P. 1765); 95 Eng. Rep. 807; 2 Wils. K.B. 275 — pinpoints: 19 How. St. Tr. at 1066 (95 Eng. Rep. at 817). No CourtListener record (English King's-era case); identity and quotations confirmed against Howell's State Trials and the English Reports. *(Decided in the Court of Common Pleas, Lord Camden, C.J.; the "Wils. K.B." citation is the Wilson's King's Bench Reports series, not the deciding court.)*

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b762055b0ea062eb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "19 How. St. Tr. 1029 (1765)", "court": "Court of Common Pleas (England)", "neutral_cite": "[1765] EWHC KB J98", "official_citation_present": true, "parallel_cite": "95 Eng. Rep. 807; 2 Wils. K.B. 275", "title": "Entick v. Carrington", "year": "1765"}}
{"assertion_id": "203b546356938224", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A Secretary of State's general warrant to break into a home and seize the owner's books and papers in search of seditious libel is illegal: under the law of England every invasion of private property is a trespass requiring positive legal authority, and no such authority existed for this search and seizure.", "title": "Entick v. Carrington"}}
{"assertion_id": "adb2408dd44e541f", "dimension": "support", "kind": "home_role", "locator": {"home": "Common Law Origins"}, "payload": {"home": "Common Law Origins", "role": "Key — Anchor (foundational origin)", "title": "Entick v. Carrington"}}
{"assertion_id": "435f2dbb197de6ae", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1765-11-02", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Entick v. Carrington", "field_i_validity": "good_law", "scope_note": "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Entick's foundational status is favorably restated by SCOTUS (Boyd, Jones, Riley). Authority weight remains Historical (English origin).", "title": "Entick v. Carrington", "varies_by_point": "false"}}
{"assertion_id": "78aa56ac0d320b91", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Historical", "title": "Entick v. Carrington"}}
```

### lake record — Entick v. Carrington

```json
{
  "schema_version": "s2.v1",
  "record_id": "Entick v. Carrington",
  "stub": false,
  "status": "verified_off_cl",
  "identity": {
    "case_name": "Entick v. Carrington",
    "case_name_short": "Entick",
    "case_name_full": "Entick v Carrington & Ors",
    "input_case_name": "Entick v. Carrington",
    "court": "Court of Common Pleas (England)",
    "court_id": null,
    "court_level": "other",
    "circuit": null,
    "state": null,
    "date_decided": "1765-11-02",
    "year": 1765,
    "docket": null,
    "cluster_id": null,
    "lead_opinion_id": null,
    "sibling_ids": [],
    "absolute_url": null,
    "identity_method": "off_cl",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "outside_cl_corpus_verified_by_off_cl_two_key"
  },
  "citations": {
    "official": {
      "cite": "19 How. St. Tr. 1029",
      "volume": 19,
      "reporter": "How. St. Tr.",
      "page": 1029,
      "type": "official",
      "selected_official": true,
      "source": "off_cl.adjudication"
    },
    "parallel": [
      {
        "cite": "95 Eng. Rep. 807",
        "volume": 95,
        "reporter": "Eng. Rep.",
        "page": 807,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "2 Wils. K.B. 275",
        "volume": 2,
        "reporter": "Wils. K.B.",
        "page": 275,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "[1765] EWHC KB J98",
        "volume": null,
        "reporter": null,
        "page": null,
        "type": "vendor_neutral",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "all": [
      {
        "cite": "19 How. St. Tr. 1029",
        "volume": 19,
        "reporter": "How. St. Tr.",
        "page": 1029,
        "type": "official",
        "selected_official": true,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "95 Eng. Rep. 807",
        "volume": 95,
        "reporter": "Eng. Rep.",
        "page": 807,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "2 Wils. K.B. 275",
        "volume": 2,
        "reporter": "Wils. K.B.",
        "page": 275,
        "type": "parallel",
        "selected_official": false,
        "source": "off_cl.adjudication"
      },
      {
        "cite": "[1765] EWHC KB J98",
        "volume": null,
        "reporter": null,
        "page": null,
        "type": "vendor_neutral",
        "selected_official": false,
        "source": "off_cl.adjudication"
      }
    ],
    "display": "19 How. St. Tr. 1029 (C.P. 1765)",
    "official_selection": {
      "court_class": "english_historical",
      "selected": "19 How. St. Tr. 1029 (C.P. 1765)",
      "reason": "off_cl_adjudication"
    }
  },
  "pinpoints": [],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1765-11-02",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Entick v. Carrington",
    "varies_by_point": false,
    "scope_note": "Off-CL record (A16/A17): CL citator lanes intentionally not run. Validity rests on the O1 web-verified page treatment (legacy 'good', as of 2026-06-30) re-seeded post-elevation per the S1 A4 mapping; Entick's foundational status is favorably restated by SCOTUS (Boyd, Jones, Riley). Authority weight remains Historical (English origin).",
    "point_overrides": [],
    "edges": [],
    "derivation": {}
  },
  "progeny": {
    "complete_query": null,
    "indexed_citing_opinions": null,
    "count_source": "off_cl_na",
    "per_sibling": [],
    "citation_count": null,
    "cache_path": null,
    "enumeration": null,
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [
    {
      "source": "BAILII",
      "url": "https://www.bailii.org/ew/cases/EWHC/KB/1765/J98.html",
      "confirmed": {
        "caption": "Entick v Carrington & Ors",
        "cite": "[1765] EWHC KB J98; 95 ER 807; 19 St Tr 1029; [1558-1774] All ER Rep 41",
        "court": "King's Bench (BAILII retrospective filing label; historical court of decision: Court of Common Pleas, Camden CJ)",
        "date": "1765-11-02"
      },
      "checked_date": "2026-07-06"
    },
    {
      "source": "Founders' Constitution",
      "url": "https://press-pubs.uchicago.edu/founders/documents/amendIVs6.html",
      "confirmed": {
        "caption": "Entick v. Carrington",
        "cite": "95 Eng. Rep. 807",
        "court": "K.B. (Wilson's-Reports reprint label; historical court of decision: Court of Common Pleas)",
        "date": "1765-11-02"
      },
      "checked_date": "2026-07-06"
    }
  ],
  "provenance": {
    "cl_source": null,
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-07T00:53:37Z",
    "date_modified": "2026-07-07T00:53:37Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "off-CL adjudication file: _run/o2-execute/offcl-entick-adjudication.json",
        "at": "2026-07-07T00:53:37Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json ('good' -> good_law) + O1 page frontmatter (as of 2026-06-30); re-seeded after verified_off_cl elevation (A17) — F-S2-31's revert applied only while the record was fail-closed",
        "at": "2026-07-06T00:00:00Z",
        "verifier": "orchestrator claude-fable-5 (user R14 Option 1 disposition 2026-07-06)"
      },
      "point_overrides": {
        "src": "verified_off_cl: no CL-derived point overrides",
        "at": "2026-07-07T00:53:37Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "verified_off_cl: no CL lead-opinion pinpoints",
        "at": "2026-07-07T00:53:37Z",
        "verifier": "orchestrator claude-fable-5"
      }
    }
  }
}

```

---

## GROUP: content/cases/Escobedo v. Illinois.md  (`case`, 7 assertions)

### content_page

```
---
title: "Escobedo v. Illinois"
type: case
citation: "378 U.S. 478 (1964)"
parallel_cite: "84 S. Ct. 1758; 12 L. Ed. 2d 977; 4 Ohio Misc. 197; 32 Ohio Op. 2d 31"
neutral_cite: 1964 U.S. LEXIS 827
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-22
docket: 615
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1964-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Escobedo v. Illinois
  varies_by_point: true
  scope_note: "The result stands, but Escobedo's Sixth-Amendment-during-interrogation theory was recast as a Fifth Amendment matter by Miranda (1966) and confined to its facts by Kirby v. Illinois (1972) and Moran v. Burbine (1986). Taught as the historical precursor to Miranda."
  point_overrides:
    - point: legacy-limited-escobedo-v-illinois
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Miranda v. Arizona
          cluster_id: 107252
          cite: 384 U.S. 436
          field_ii: limited
        - name: Kirby v. Illinois
          cluster_id: 108554
          cite: 406 U.S. 682
          field_ii: limited
        - name: Moran v. Burbine
          cluster_id: 111614
          cite: 475 U.S. 412
          field_ii: limited
      scope_note: "The result stands, but Escobedo's Sixth-Amendment-during-interrogation theory was recast as a Fifth Amendment matter by Miranda (1966) and confined to its facts by Kirby v. Illinois (1972) and Moran v. Burbine (1986). Taught as the historical precursor to Miranda."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106883/escobedo-v-illinois/"
  cluster_id: 106883
  opinion_id: 106883
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Historical"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[Miranda v. Arizona]]", "[[Massiah v. United States]]", "[[Kirby v. Illinois]]"]
aliases: []
tags: ["case", "sixth-amendment", "fifth-amendment", "right-to-counsel", "interrogation", "historical"]
holding: "Where an investigation has focused on a suspect in custody, the police are interrogating to elicit incriminating statements, the suspect has requested and been denied the chance to consult his retained lawyer, and he has not been warned of his right to remain silent, he has been denied the Sixth Amendment right to counsel and his statements are inadmissible."
lake:
  record_id: Escobedo v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Escobedo v. Illinois

*378 U.S. 478 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Escobedo was arrested for the murder of his brother-in-law. During interrogation he repeatedly asked to speak with his retained lawyer, who had come to the station and was himself trying to see Escobedo; police refused to let them meet and did not warn Escobedo of his right to remain silent. Escobedo made incriminating statements that were used to convict him.

## Issue
Whether the refusal, during a custodial interrogation that had focused on the suspect, to honor his request to consult his retained counsel — coupled with the failure to warn him of his right to remain silent — denied him the Sixth Amendment right to counsel and rendered his statements inadmissible.

## Rule
Yes. "We hold, therefore, that where, as here, the investigation is no longer a general inquiry into an unsolved crime but has begun to focus on a particular suspect, the suspect has been taken into police custody, the police carry out a process of interrogations that lends itself to eliciting incriminating statements, the suspect has requested and been denied an opportunity to consult with his lawyer, and the police have not effectively warned him of his absolute constitutional right to remain silent, the accused has been denied 'the Assistance of Counsel' in violation of the Sixth Amendment ... and ... no statement elicited by the police during the interrogation may be used against him at a criminal trial." — 378 U.S. at 490–491. ^pin-490

## Application
On Escobedo's facts every condition was met: the investigation had focused on him, he was in custody, the questioning was designed to elicit a confession, his repeated requests to consult his lawyer were denied while the lawyer was present and seeking him, and he was never warned of his right to silence. His incriminating statements were therefore obtained in violation of the Constitution and could not be used against him.

## Conclusion
The statements were inadmissible; the conviction was reversed. *Escobedo* was the bridge between the Sixth Amendment right to counsel and the protection of suspects during interrogation.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS** (result intact; rationale superseded).
- Two years later [[Miranda v. Arizona]] recast the concern as a **Fifth Amendment** matter, and [[Kirby v. Illinois]] (and *[[Moran v. Burbine]]*) confined *Escobedo* "to its own facts." The modern rule is that the **Sixth Amendment** right to counsel attaches only at the initiation of adversary judicial proceedings ([[United States v. Gouveia]]), while custodial interrogation is governed by *[[Miranda v. Arizona|Miranda]]*. *Escobedo* is taught as the historical precursor, not as a freestanding test.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Historical*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Escobedo v. Illinois*, 378 U.S. 478 (1964) — https://www.courtlistener.com/opinion/106883/escobedo-v-illinois/ — pinpoint: 490–491.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f25a9e1899b4dde4", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "378 U.S. 478 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 827", "official_citation_present": true, "parallel_cite": "84 S. Ct. 1758; 12 L. Ed. 2d 977; 4 Ohio Misc. 197; 32 Ohio Op. 2d 31", "title": "Escobedo v. Illinois", "year": "1964"}}
{"assertion_id": "0302371af20acfd8", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Historical", "title": "Escobedo v. Illinois"}}
{"assertion_id": "08bf8028885b413e", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (cross-doctrine)", "title": "Escobedo v. Illinois"}}
{"assertion_id": "9efe7dd81f746598", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where an investigation has focused on a suspect in custody, the police are interrogating to elicit incriminating statements, the suspect has requested and been denied the chance to consult his retained lawyer, and he has not been warned of his right to remain silent, he has been denied the Sixth Amendment right to counsel and his statements are inadmissible.", "title": "Escobedo v. Illinois"}}
{"assertion_id": "3ac82cdb28f41784", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Escobedo v. Illinois"}}
{"assertion_id": "e89b18a1cc0e3e91", "dimension": "treatment", "kind": "treatment_override", "locator": {"point": "legacy-limited-escobedo-v-illinois"}, "payload": {"by": [{"cite": "384 U.S. 436", "cluster_id": "107252", "field_ii": "limited", "name": "Miranda v. Arizona"}, {"cite": "406 U.S. 682", "cluster_id": "108554", "field_ii": "limited", "name": "Kirby v. Illinois"}, {"cite": "475 U.S. 412", "cluster_id": "111614", "field_ii": "limited", "name": "Moran v. Burbine"}], "field_i_validity": "caution", "point": "legacy-limited-escobedo-v-illinois", "point_label": "Legacy limited treatment point", "s3_binding_status": "provisional", "title": "Escobedo v. Illinois"}}
{"assertion_id": "fd25da6590612a0b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-06-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Escobedo v. Illinois", "field_i_validity": "caution", "scope_note": "The result stands, but Escobedo's Sixth-Amendment-during-interrogation theory was recast as a Fifth Amendment matter by Miranda (1966) and confined to its facts by Kirby v. Illinois (1972) and Moran v. Burbine (1986). Taught as the historical precursor to Miranda.", "title": "Escobedo v. Illinois", "varies_by_point": "true"}}
```

### lake record — Escobedo v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Escobedo v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Escobedo v. Illinois",
    "case_name_short": "Escobedo",
    "case_name_full": "Escobedo v. Illinois",
    "input_case_name": "Escobedo v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-22",
    "year": 1964,
    "docket": "615",
    "cluster_id": 106883,
    "lead_opinion_id": 106883,
    "sibling_ids": [
      106883,
      9422869,
      9422870
    ],
    "absolute_url": "/opinion/106883/escobedo-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 478",
      "volume": "378",
      "reporter": "U.S.",
      "page": "478",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1758",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1758",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 977",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "977",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 Ohio Misc. 197",
        "volume": "4",
        "reporter": "Ohio Misc.",
        "page": "197",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 Ohio Op. 2d 31",
        "volume": "32",
        "reporter": "Ohio Op. 2d",
        "page": "31",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 827",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 478",
        "volume": "378",
        "reporter": "U.S.",
        "page": "478",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1758",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1758",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 977",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "977",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 827",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "4 Ohio Misc. 197",
        "volume": "4",
        "reporter": "Ohio Misc.",
        "page": "197",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "32 Ohio Op. 2d 31",
        "volume": "32",
        "reporter": "Ohio Op. 2d",
        "page": "31",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 478",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 478",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-490",
      "page": null,
      "quote": "--- # Escobedo v. Illinois *378 U.S. 478 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **limited** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Escobedo was arrested for the murder of his brother-in-law. During interrogation he repeatedly asked to speak with his retained lawyer, who had come to the station and was himself trying to see Escobedo; police refused to let them meet and did not warn Escobedo of his right to remain silent. Escobedo made incriminating statements that were used to convict him. ## Issue Whether the refusal, during a custodial interrogation that had focused on the suspect, to honor his request to consult his retained counsel \u2014 coupled with the failure to warn him of his right to remain silent \u2014 denied him the Sixth Amendment right to counsel and rendered his statements inadmissible. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1964-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Escobedo v. Illinois",
    "varies_by_point": true,
    "scope_note": "The result stands, but Escobedo's Sixth-Amendment-during-interrogation theory was recast as a Fifth Amendment matter by Miranda (1966) and confined to its facts by Kirby v. Illinois (1972) and Moran v. Burbine (1986). Taught as the historical precursor to Miranda.",
    "point_overrides": [
      {
        "point": "legacy-limited-escobedo-v-illinois",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Miranda v. Arizona",
            "cluster_id": 107252,
            "cite": "384 U.S. 436",
            "field_ii": "limited"
          },
          {
            "name": "Kirby v. Illinois",
            "cluster_id": 108554,
            "cite": "406 U.S. 682",
            "field_ii": "limited"
          },
          {
            "name": "Moran v. Burbine",
            "cluster_id": 111614,
            "cite": "475 U.S. 412",
            "field_ii": "limited"
          }
        ],
        "scope_note": "The result stands, but Escobedo's Sixth-Amendment-during-interrogation theory was recast as a Fifth Amendment matter by Miranda (1966) and confined to its facts by Kirby v. Illinois (1972) and Moran v. Burbine (1986). Taught as the historical precursor to Miranda."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": "384 U.S. 436",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": "406 U.S. 682",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": "475 U.S. 412",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
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
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Corley v. United States",
          "cluster_id": 145888,
          "cite": [
            "173 L. Ed. 2d 443",
            "129 S. Ct. 1558",
            "556 U.S. 303",
            "2009 U.S. LEXIS 2512"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sawyer",
          "cluster_id": 2521466,
          "cite": [
            "2004 OK CR 22",
            "92 P.3d 707",
            "2004 WL 1244992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mendez v. State",
          "cluster_id": 1426447,
          "cite": [
            "56 S.W.3d 880",
            "2001 WL 1044612"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 1194882,
          "cite": [
            "17 Cal. 4th 279",
            "949 P.2d 890",
            "98 Cal. Daily Op. Serv. 789",
            "98 Daily Journal DAR 1025",
            "70 Cal. Rptr. 2d 793",
            "1998 Cal. LEXIS 23"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Larry Winsett v. Odie Washington, Warden of Dixon Correctional Center",
          "cluster_id": 748614,
          "cite": [
            "130 F.3d 269",
            "1997 U.S. App. LEXIS 32286",
            "1997 WL 716044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richard Louis Arnold Phillips v. Daniel B. Vasquez, Warden, San Quentin State Prison",
          "cluster_id": 697343,
          "cite": [
            "56 F.3d 1030",
            "95 Daily Journal DAR 6705",
            "95 Cal. Daily Op. Serv. 3912",
            "1995 U.S. App. LEXIS 12695",
            "1995 WL 319974"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
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
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
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
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moran v. Burbine",
          "cluster_id": 111614,
          "cite": [
            "89 L. Ed. 2d 410",
            "106 S. Ct. 1135",
            "475 U.S. 412",
            "1986 U.S. LEXIS 32",
            "54 U.S.L.W. 4265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
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
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
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
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hellard v. State",
          "cluster_id": 2459031,
          "cite": [
            "629 S.W.2d 4",
            "1982 Tenn. LEXIS 389"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frazier v. Cupp",
          "cluster_id": 107913,
          "cite": [
            "22 L. Ed. 2d 684",
            "89 S. Ct. 1420",
            "394 U.S. 731",
            "1969 U.S. LEXIS 1870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
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
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Escobedo v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106883 OR 9422869 OR 9422870) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03ODc4ODE2MDAwMDAmcz02ODM5JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106883+OR+9422869+OR+9422870%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(106883 OR 9422869 OR 9422870)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mzcmcz01NjgyMDE3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106883+OR+9422869+OR+9422870%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106883 OR 9422869 OR 9422870)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106883 OR 9422869 OR 9422870)",
    "indexed_citing_opinions": 3478,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106883,
        "count": 3261,
        "count_source": "search"
      },
      {
        "opinion_id": 9422869,
        "count": 360,
        "count_source": "search"
      },
      {
        "opinion_id": 9422870,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5250,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/escobedo-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwMzcyNDMmcz00ODM1MzUwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106883+OR+9422869+OR+9422870%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106883,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 237373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 261371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 1490510,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 1501119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 1653387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 1952574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 2193029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106883,
        "cited_id": 9422869,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 261371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 1653387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 2193029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422869,
        "cited_id": 5520716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 105382,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 237373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 1490510,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 1501119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9422870,
        "cited_id": 1952574,
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
    "date_created": "2026-07-05T03:16:35Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:16:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:16:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:16:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Escobedo v. Illinois

```
<div>
<center><b><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U.S. 478</a></span> (1964)</b></center>
<center><h1>ESCOBEDO<br>
v.<br>
ILLINOIS.</h1></center>
<center>No. 615.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 29, 1964.</center>
<center>Decided June 22, 1964.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS.
<p><i>Barry L. Kroll</i> argued the cause for petitioner. With him on the brief was <i>Donald M. Haskell.</i></p>
<p><i>James R. Thompson</i> argued the cause for respondent. With him on the brief were <i>Daniel P. Ward</i> and <i>Elmer C. Kissane.</i></p>
<p><i>Bernard Weisberg</i> argued the cause for the American Civil Liberties Union, as <i>amicus curiae,</i> urging reversal. With him on the brief was <i>Walter T. Fisher.</i></p>
<p><span class="star-pagination">*479</span> MR. JUSTICE GOLDBERG delivered the opinion of the Court.</p>
<p>The critical question in this case is whether, under the circumstances, the refusal by the police to honor petitioner's request to consult with his lawyer during the course of an interrogation constitutes a denial of "the Assistance of Counsel" in violation of the Sixth Amendment to the Constitution as "made obligatory upon the States by the Fourteenth Amendment," <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#342" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 342</a></span>, and thereby renders inadmissible in a state criminal trial any incriminating statement elicited by the police during the interrogation.</p>
<p>On the night of January 19, 1960, petitioner's brother-in-law was fatally shot. In the early hours of the next morning, at 2:30 a.m., petitioner was arrested without a warrant and interrogated. Petitioner made no statement to the police and was released at 5 that afternoon pursuant to a state court writ of habeas corpus obtained by Mr. Warren Wolfson, a lawyer who had been retained by petitioner.</p>
<p>On January 30, Benedict DiGerlando, who was then in police custody and who was later indicted for the murder along with petitioner, told the police that petitioner had fired the fatal shots. Between 8 and 9 that evening, petitioner and his sister, the widow of the deceased, were arrested and taken to police headquarters. En route to the police station, the police "had handcuffed the defendant behind his back," and "one of the arresting officers told defendant that DiGerlando had named him as the one who shot" the deceased. Petitioner testified, without contradiction, that the "detectives said they had us pretty well, up pretty tight, and we might as well admit to this crime," and that he replied, "I am sorry but I would like to have advice from my lawyer." A police officer testified that although petitioner was not formally charged "he was in custody" and "couldn't walk out the door."</p>
<p><span class="star-pagination">*480</span> Shortly after petitioner reached police headquarters, his retained lawyer arrived. The lawyer described the ensuing events in the following terms:</p>
<blockquote>"On that day I received a phone call [from "the mother of another defendant"] and pursuant to that phone call I went to the Detective Bureau at 11th and State. The first person I talked to was the Sergeant on duty at the Bureau Desk, Sergeant Pidgeon. I asked Sergeant Pidgeon for permission to speak to my client, Danny Escobedo. . . . Sergeant Pidgeon made a call to the Bureau lockup and informed me that the boy had been taken from the lockup to the Homicide Bureau. This was between 9:30 and 10:00 in the evening. Before I went anywhere, he called the Homicide Bureau and told them there was an attorney waiting to see Escobedo. He told me I could not see him. Then I went upstairs to the Homicide Bureau. There were several Homicide Detectives around and I talked to them. I identified myself as Escobedo's attorney and asked permission to see him. They said I could not. . . . The police officer told me to see Chief Flynn who was on duty. I identified myself to Chief Flynn and asked permission to see my client. He said I could not. . . . I think it was approximately 11:00 o'clock. He said I couldn't see him because they hadn't completed questioning. . . . [F]or a second or two I spotted him in an office in the Homicide Bureau. The door was open and I could see through the office. . . . I waved to him and he waved back and then the door was closed, by one of the officers at Homicide.<sup>[1]</sup> There were four or five officers milling <span class="star-pagination">*481</span> around the Homicide Detail that night. As to whether I talked to Captain Flynn any later that day, I waited around for another hour or two and went back again and renewed by [<i>sic</i>] request to see my client. He again told me I could not. . . . I filed an official complaint with Commissioner Phelan of the Chicago Police Department. I had a conversation with every police officer I could find. I was told at Homicide that I couldn't see him and I would have to get a writ of habeas corpus. I left the Homicide Bureau and from the Detective Bureau at 11th and State at approximately 1:00 A.M. [Sunday morning] I had no opportunity to talk to my client that night. I quoted to Captain Flynn the Section of the Criminal Code which allows an attorney the right to see his client."<sup>[2]</sup></blockquote>
<p>Petitioner testified that during the course of the interrogation he repeatedly asked to speak to his lawyer and that the police said that his lawyer "didn't want to see" him. The testimony of the police officers confirmed these accounts in substantial detail.</p>
<p>Notwithstanding repeated requests by each, petitioner and his retained lawyer were afforded no opportunity to consult during the course of the entire interrogation. At one point, as previously noted, petitioner and his attorney came into each other's view for a few moments but the attorney was quickly ushered away. Petitioner testified "that he heard a detective telling the attorney the latter would not be allowed to talk to [him] `until they <span class="star-pagination">*482</span> were done' " and that he heard the attorney being refused permission to remain in the adjoining room. A police officer testified that he had told the lawyer that he could not see petitioner until "we were through interrogating" him.</p>
<p>There is testimony by the police that during the interrogation, petitioner, a 22-year-old of Mexican extraction with no record of previous experience with the police, "was handcuffed"<sup>[3]</sup> in a standing position and that he "was nervous, he had circles under his eyes and he was upset" and was "agitated" because "he had not slept well in over a week."</p>
<p>It is undisputed that during the course of the interrogation Officer Montejano, who "grew up" in petitioner's neighborhood, who knew his family, and who uses "Spanish language in [his] police work," conferred alone with petitioner "for about a quarter of an hour. . . ." Petitioner testified that the officer said to him "in Spanish that my sister and I could go home if I pinned it on Benedict DiGerlando," that "he would see to it that we would go home and be held only as witnesses, if anything, if we had made a statement against DiGerlando . . . , that we would be able to go home that night." Petitioner testified that he made the statement in issue because of this assurance. Officer Montejano denied offering any such assurance.</p>
<p>A police officer testified that during the interrogation the following occurred:</p>
<blockquote>"I informed him of what DiGerlando told me and when I did, he told me that DiGerlando was [lying] and I said, `Would you care to tell DiGerlando that?' and he said, `Yes, I will.' So, I <span class="star-pagination">*483</span> brought . . . Escobedo in and he confronted DiGerlando and he told him that he was lying and said, `I didn't shoot Manuel, you did it.' "</blockquote>
<p>In this way, petitioner, for the first time, admitted to some knowledge of the crime. After that he made additional statements further implicating himself in the murder plot. At this point an Assistant State's Attorney, Theodore J. Cooper, was summoned "to take" a statement. Mr. Cooper, an experienced lawyer who was assigned to the Homicide Division to take "statements from some defendants and some prisoners that they had in custody," "took" petitioner's statement by asking carefully framed questions apparently designed to assure the admissibility into evidence of the resulting answers. Mr. Cooper testified that he did not advise petitioner of his constitutional rights, and it is undisputed that no one during the course of the interrogation so advised him.</p>
<p>Petitioner moved both before and during trial to suppress the incriminating statement, but the motions were denied. Petitioner was convicted of murder and he appealed the conviction.</p>
<p>The Supreme Court of Illinois, in its original opinion of February 1, 1963, held the statement inadmissible and reversed the conviction. The court said:</p>
<blockquote>"[I]t seems manifest to us, from the undisputed evidence and the circumstances surrounding defendant at the time of his statement and shortly prior thereto, that the defendant understood he would be permitted to go home if he gave the statement and would be granted an immunity from prosecution."</blockquote>
<p>Compare <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>.</p>
<p>The State petitioned for, and the court granted, rehearing. The court then affirmed the conviction. It said: "[T]he <span class="star-pagination">*484</span> officer denied making the promise and the trier of fact believed him. We find no reason for disturbing the trial court's finding that the confession was voluntary."<sup>[4]</sup> <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/#45" aria-description="Citation for case: The PEOPLE v. Escobedo">28 Ill. 2d 41, 45-46</a></span>, <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/#827" aria-description="Citation for case: The PEOPLE v. Escobedo">190 N. E. 2d 825, 827</a></span>. The court also held, on the authority of this Court's decisions in <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, that the confession was admissible even though "it was obtained after he had requested the assistance of counsel, which request was denied." <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/#46" aria-description="Citation for case: The PEOPLE v. Escobedo">28 Ill. 2d, at 46</a></span>, <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/#827" aria-description="Citation for case: The PEOPLE v. Escobedo">190 N. E. 2d, at 827</a></span>. We granted a writ of certiorari to consider whether the petitioner's statement was constitutionally admissible at his trial. <span class="citation multiple-matches"><a href="/c/U.%20S./375/902/">375 U. S. 902</a></span>. We conclude, for the reasons stated below, that it was not and, accordingly, we reverse the judgment of conviction.</p>
<p>In <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>, this Court observed that "a Constitution which guarantees a defendant the aid of counsel at . . . trial could surely vouchsafe no less to an indicted defendant under interrogation by the police in a completely extrajudicial proceeding. Anything less . . . might deny a defendant `effective representation by counsel at the only stage when <span class="star-pagination">*485</span> legal aid and advice would help him.' " <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#204" aria-description="Citation for case: Massiah v. United States"><i>Id.,</i> at 204</a></span>, quoting DOUGLAS, J., concurring in <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 326</a></span>.</p>
<p>The interrogation here was conducted before petitioner was formally indicted. But in the context of this case, that fact should make no difference. When petitioner requested, and was denied, an opportunity to consult with his lawyer, the investigation had ceased to be a general investigation of "an unsolved crime." <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#327" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 327</a></span> (STEWART, J., concurring). Petitioner had become the accused, and the purpose of the interrogation was to "get him" to confess his guilt despite his constitutional right not to do so. At the time of his arrest and throughout the course of the interrogation, the police told petitioner that they had convincing evidence that he had fired the fatal shots. Without informing him of his absolute right to remain silent in the face of this accusation, the police urged him to make a statement.<sup>[5]</sup> As this Court observed many years ago:</p>
<blockquote>"It cannot be doubted that, placed in the position in which the accused was when the statement was made to him that the other suspected person had charged him with crime, the result was to produce upon his mind the fear that if he remained silent it would be considered an admission of guilt, and therefore render certain his being committed for trial as the guilty person, and it cannot be conceived that the converse impression would not also have naturally <span class="star-pagination">*486</span> arisen, that by denying there was hope of removing the suspicion from himself." <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#562" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 562</a></span>.</blockquote>
<p>Petitioner, a layman, was undoubtedly unaware that under Illinois law an admission of "mere" complicity in the murder plot was legally as damaging as an admission of firing of the fatal shots. <i>Illinois</i> v. <i>Escobedo,</i> <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/" aria-description="Citation for case: The PEOPLE v. Escobedo">28 Ill. 2d 41</a></span>, <span class="citation" data-id="2193029"><a href="/opinion/2193029/the-people-v-escobedo/" aria-description="Citation for case: The PEOPLE v. Escobedo">190 N. E. 2d 825</a></span>. The "guiding hand of counsel" was essential to advise petitioner of his rights in this delicate situation. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#69" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45, 69</a></span>. This was the "stage when legal aid and advice" were most critical to petitioner. <i>Massiah</i> v. <i>United States, supra,</i> at 204. It was a stage surely as critical as was the arraignment in <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>, and the preliminary hearing in <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>. What happened at this interrogation could certainly "affect the whole trial," <i>Hamilton</i> v. <i>Alabama, supra,</i> at 54, since rights "may be as irretrievably lost, if not then and there asserted, as they are when an accused represented by counsel waives a right for strategic purposes." <i>Ibid.</i> It would exalt form over substance to make the right to counsel, under these circumstances, depend on whether at the time of the interrogation, the authorities had secured a formal indictment. Petitioner had, for all practical purposes, already been charged with murder.</p>
<p>The New York Court of Appeals, whose decisions this Court cited with approval in <i>Massiah,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#205" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, at 205</a></span>, has recently recognized that, under circumstances such as those here, no meaningful distinction can be drawn between interrogation of an accused before and after formal indictment. In <i>People</i> v. <i>Donovan,</i> 13 N. Y. 2d 148, <span class="citation" data-id="5520716"><a href="/opinion/5673265/people-v-donovan/" aria-description="Citation for case: People v. Donovan">193 N. E. 2d 628</a></span>, that court, in an opinion by Judge Fuld, held that a "confession taken from a defendant, during a period of detention [prior to indictment], after his attorney had requested and been denied access <span class="star-pagination">*487</span> to him" could not be used against him in a criminal trial.<sup>[6]</sup><i>Id.,</i> at 151, <span class="citation" data-id="5520716"><a href="/opinion/5673265/people-v-donovan/#629" aria-description="Citation for case: People v. Donovan">193 N. E. 2d, at 629</a></span>. The court observed that it "would be highly incongruous if our system of justice permitted the district attorney, the lawyer representing the State, to extract a confession from the accused while his own lawyer, seeking to speak with him, was kept from him by the police." <i>Id.,</i> at 152, <span class="citation" data-id="5520716"><a href="/opinion/5673265/people-v-donovan/#629" aria-description="Citation for case: People v. Donovan">193 N. E. 2d, at 629</a></span>.<sup>[7]</sup></p>
<p>In <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, we held that every person accused of a crime, whether state or federal, is entitled to a lawyer at trial.<sup>[8]</sup> The rule sought by the State here, however, would make the trial no more than an appeal from the interrogation; and the "right to use counsel at the formal trial [would be] a very hollow thing [if], for all practical purposes, the conviction is already assured by pretrial examination." <i>In re Groban,</i> 352 U. S. <span class="star-pagination">*488</span> 330, 344 (BLACK, J., dissenting).<sup>[9]</sup> "One can imagine a cynical prosecutor saying: `Let them have the most illustrious counsel, now. They can't escape the noose. There is nothing that counsel can do for them at the trial.' " <i>Ex parte Sullivan,</i> <span class="citation" data-id="1653387"><a href="/opinion/1653387/ex-parte-sullivan/#517" aria-description="Citation for case: Ex Parte Sullivan">107 F. Supp. 514, 517-518</a></span>.</p>
<p>It is argued that if the right to counsel is afforded prior to indictment, the number of confessions obtained by the police will diminish significantly, because most confessions are obtained during the period between arrest and indictment,<sup>[10]</sup> and "any lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to police under any circumstances." <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#59" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 59</a></span> (Jackson, J., concurring in part and dissenting in part). This argument, of course, cuts two ways. The fact that many confessions are obtained during this period points up its critical nature as a "stage when legal aid and advice" are surely needed. <i>Massiah</i> v. <i>United States, supra,</i> at 204; <i>Hamilton</i> v. <i>Alabama, supra</i><i>; </i><i>White</i> v. <i><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">Maryland, supra</a></span></i><i>.</i> The right to counsel would indeed be hollow if it began at a period when few confessions were obtained. There is necessarily a direct relationship between the importance of a stage to the police in their quest for a confession and the criticalness of that stage to the accused in his need for legal advice. Our Constitution, unlike some others, strikes the balance in favor of the right of the accused to be advised by his lawyer of his privilege against self-incrimination. See Note, 73 Yale L. J. 1000, 1048-1051 (1964).</p>
<p>We have learned the lesson of history, ancient and modern, that a system of criminal law enforcement <span class="star-pagination">*489</span> which comes to depend on the "confession" will, in the long run, be less reliable<sup>[11]</sup> and more subject to abuses<sup>[12]</sup> than a system which depends on extrinsic evidence independently secured through skillful investigation. As Dean Wigmore so wisely said:</p>
<blockquote>"[<i>A</i>]<i>ny system of administration which permits the prosecution to trust habitually to compulsory self-disclosure as a source of proof must itself suffer morally thereby.</i> The inclination develops to rely mainly upon such evidence, and to be satisfied with an incomplete investigation of the other sources. The exercise of the power to extract answers begets a forgetfulness of the just limitations of that power. The simple and peaceful process of questioning breeds a readiness to resort to bullying and to physical force and torture. If there is a right to an answer, there soon seems to be a right to the expected answer, that is, to a confession of guilt. Thus the legitimate use grows into the unjust abuse; ultimately, the innocent are jeopardized by the encroachments of a bad system. Such seems to have been the course of experience in those legal systems where the privilege was not recognized." 8 Wigmore, Evidence (3d ed. 1940), 309. (Emphasis in original.)</blockquote>
<p><span class="star-pagination">*490</span> This Court also has recognized that "history amply shows that confessions have often been extorted to save law enforcement officials the trouble and effort of obtaining valid and independent evidence . . . ." <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#519" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 519</a></span>.</p>
<p>We have also learned the companion lesson of history that no system of criminal justice can, or should, survive if it comes to depend for its continued effectiveness on the citizens' abdication through unawareness of their constitutional rights. No system worth preserving should have to <i>fear</i> that if an accused is permitted to consult with a lawyer, he will become aware of, and exercise, these rights.<sup>[13]</sup> If the exercise of constitutional rights will thwart the effectiveness of a system of law enforcement, then there is something very wrong with that system.<sup>[14]</sup></p>
<p>We hold, therefore, that where, as here, the investigation is no longer a general inquiry into an unsolved crime but has begun to focus on a particular suspect, the suspect <span class="star-pagination">*491</span> has been taken into police custody, the police carry out a process of interrogations that lends itself to eliciting incriminating statements, the suspect has requested and been denied an opportunity to consult with his lawyer, and the police have not effectively warned him of his absolute constitutional right to remain silent, the accused has been denied "the Assistance of Counsel" in violation of the Sixth Amendment to the Constitution as "made obligatory upon the States by the Fourteenth Amendment," <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#342" aria-description="Citation for case: Gideon v. Wainwright">372 U. S., at 342</a></span>, and that no statement elicited by the police during the interrogation may be used against him at a criminal trial.</p>
<p><i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, does not compel a contrary result. In that case the Court merely rejected the absolute rule sought by petitioner, that "every state denial of a request to contact counsel [is] an infringement of the constitutional right <i>without regard to the circumstances of the case.</i>" <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/#440" aria-description="Citation for case: Crooker v. California"><i>Id.,</i> at 440</a></span>. (Emphasis in original.) In its place, the following rule was announced:</p>
<blockquote>"[S]tate refusal of a request to engage counsel violates due process not only if the accused is deprived of counsel at trial on the merits, . . . <i>but also if he is deprived of counsel for any part of the pretrial proceedings,</i> provided that he is so prejudiced thereby as to infect his subsequent trial with an absence of `that fundamental fairness essential to the very concept of justice. . . .' The latter determination necessarily depends upon all the circumstances of the case." 357 U. S., at 439-440. (Emphasis added.)</blockquote>
<p>The Court, applying "these principles" to "the sum total of the circumstances [there] during the time petitioner was without counsel," <i>id.,</i> at 440, concluded that he had not been fundamentally prejudiced by the denial of his request for counsel. Among the critical circumstances which distinguish that case from this one are that the petitioner there, but not here, was explicitly advised by the police of his constitutional right to remain silent and <span class="star-pagination">*492</span> not to "say anything" in response to the questions, <i>id.,</i> at 437, and that petitioner there, but not here, was a well-educated man who had studied criminal law while attending law school for a year. The Court's opinion in <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, decided the same day, merely said that the "contention that petitioner had a constitutional right to confer with counsel is disposed of by <i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California</a></span></i> . . . ." That case adds nothing, therefore, to <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">Crooker</a></span>.</i> In any event, to the extent that <i><span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">Cicenia</a></span></i> or <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">Crooker</a></span></i> may be inconsistent with the principles announced today, they are not to be regarded as controlling.<sup>[15]</sup></p>
<p>Nothing we have said today affects the powers of the police to investigate "an unsolved crime," <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#327" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 327</a></span> (STEWART, J., concurring), by gathering information from witnesses and by other "proper investigative efforts." <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#519" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 519</a></span>. We hold only that when the process shifts from investigatory to accusatorywhen its focus is on the accused and its purpose is to elicit a confession our adversary system begins to operate, and, under the circumstances here, the accused must be permitted to consult with his lawyer.</p>
<p>The judgment of the Illinois Supreme Court is reversed and the case remanded for proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE HARLAN, dissenting.</p>
<p>I would affirm the judgment of the Supreme Court of Illinois on the basis of <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, <span class="star-pagination">*493</span> decided by this Court only six years ago. Like my Brother WHITE, <i>post,</i> p. 495, I think the rule announced today is most ill-conceived and that it seriously and unjustifiably fetters perfectly legitimate methods of criminal law enforcement.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>I think this case is directly controlled by <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, and I would therefore affirm the judgment.</p>
<p><i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>, is not in point here. In that case a federal grand jury had indicted Massiah. He had retained a lawyer and entered a formal plea of not guilty. Under our system of federal justice an indictment and arraignment are followed by a trial, at which the Sixth Amendment guarantees the defendant the assistance of counsel.<sup>[*]</sup> But Massiah was released on bail, and thereafter agents of the Federal Government deliberately elicited incriminating statements from him in the absence of his lawyer. We held that the use of these statements against him at his trial denied him the basic protections of the Sixth Amendment guarantee. Putting to one side the fact that the case now before us is not a federal case, the vital fact remains that this case does not involve the deliberate interrogation of a defendant after the initiation of judicial proceedings against him. The Court disregards this basic difference between the present case and Massiah's, with the bland assertion that "that fact should make no difference." <i>Ante,</i> p. 485.</p>
<p>It is "that fact," I submit, which makes all the difference. Under our system of criminal justice the institution of formal, meaningful judicial proceedings, by way of indictment, information, or arraignment, marks the <span class="star-pagination">*494</span> point at which a criminal investigation has ended and adversary proceedings have commenced. It is at this point that the constitutional guarantees attach which pertain to a criminal trial. Among those guarantees are the right to a speedy trial, the right of confrontation, and the right to trial by jury. Another is the guarantee of the assistance of counsel. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>.</p>
<p>The confession which the Court today holds inadmissible was a voluntary one. It was given during the course of a perfectly legitimate police investigation of an unsolved murder. The Court says that what happened during this investigation "affected" the trial. I had always supposed that the whole purpose of a police investigation of a murder was to "affect" the trial of the murderer, and that it would be only an incompetent, unsuccessful, or corrupt investigation which would not do so. The Court further says that the Illinois police officers did not advise the petitioner of his "constitutional rights" before he confessed to the murder. This Court has never held that the Constitution requires the police to give any "advice" under circumstances such as these.</p>
<p>Supported by no stronger authority than its own rhetoric, the Court today converts a routine police investigation of an unsolved murder into a distorted analogue of a judicial trial. It imports into this investigation constitutional concepts historically applicable only after the onset of formal prosecutorial proceedings. By doing so, I think the Court perverts those precious constitutional guarantees, and frustrates the vital interests of society in preserving the legitimate and proper function of honest and purposeful police investigation.</p>
<p>Like my Brother CLARK, I cannot escape the logic of my Brother WHITE's conclusions as to the extraordinary implications which emanate from the Court's opinion in <span class="star-pagination">*495</span> this case, and I share their views as to the untold and highly unfortunate impact today's decision may have upon the fair administration of criminal justice. I can only hope we have completely misunderstood what the Court has said.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE CLARK and MR. JUSTICE STEWART join, dissenting.</p>
<p>In <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>, the Court held that as of the date of the indictment the prosecution is disentitled to secure admissions from the accused. The Court now moves that date back to the time when the prosecution begins to "focus" on the accused. Although the opinion purports to be limited to the facts of this case, it would be naive to think that the new constitutional right announced will depend upon whether the accused has retained his own counsel, cf. <i>Gideon</i> v. <i>Wainright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <i>Griffin</i> v. <i>Illinois,</i> <span class="citation" data-id="9421263"><a href="/opinion/105382/griffin-v-illinois/" aria-description="Citation for case: Griffin v. Illinois">351 U. S. 12</a></span>; <i>Douglas</i> v. <i>California,</i> <span class="citation" data-id="9422548"><a href="/opinion/106546/douglas-v-california/" aria-description="Citation for case: Douglas v. California">372 U. S. 353</a></span>, or has asked to consult with counsel in the course of interrogation. Cf. <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span>. At the very least the Court holds that once the accused becomes a suspect and, presumably, is arrested, any admission made to the police thereafter is inadmissible in evidence unless the accused has waived his right to counsel. The decision is thus another major step in the direction of the goal which the Court seemingly has in mindto bar from evidence all admissions obtained from an individual suspected of crime, whether involuntarily made or not. It does of course put us one step "ahead" of the English judges who have had the good sense to leave the matter a discretionary one with the trial court.<sup>[*]</sup> I reject this step and <span class="star-pagination">*496</span> the invitation to go farther which the Court has now issued.</p>
<p>By abandoning the voluntary-involuntary test for admissibility of confessions, the Court seems driven by the notion that it is uncivilized law enforcement to use an accused's own admissions against him at his trial. It attempts to find a home for this new and nebulous rule of due process by attaching it to the right to counsel guaranteed in the federal system by the Sixth Amendment and binding upon the States by virtue of the due process guarantee of the Fourteenth Amendment. <i>Gideon</i> v. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra</a></span></i><i>.</i> The right to counsel now not only entitles the accused to counsel's advice and aid in preparing for trial but stands as an impenetrable barrier to any interrogation once the accused has become a suspect. From that very moment apparently his right to counsel attaches, a rule wholly unworkable and impossible to administer unless police cars are equipped with public defenders and undercover agents and police informants have defense counsel at their side. I would not abandon the Court's prior cases defining with some care and analysis the circumstances requiring the presence or aid of counsel and substitute the amorphous and wholly unworkable principle that counsel is constitutionally required whenever he would or could be helpful. <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>; <i>Gideon</i> v. <span class="star-pagination">*497</span> <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra</a></span></i><i>.</i> These cases dealt with the requirement of counsel at proceedings in which definable rights could be won or lost, not with stages where probative evidence might be obtained. Under this new approach one might just as well argue that a potential defendant is constitutionally entitled to a lawyer before, not after, he commits a crime, since it is then that crucial incriminating evidence is put within the reach of the Government by the would-be accused. Until now there simply has been no right guaranteed by the Federal Constitution to be free from the use at trial of a voluntary admission made prior to indictment.</p>
<p>It is incongruous to assume that the provision for counsel in the Sixth Amendment was meant to amend or supersede the self-incrimination provision of the Fifth Amendment, which is now applicable to the States. <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>. That amendment addresses itself to the very issue of incriminating admissions of an accused and resolves it by proscribing only compelled statements. Neither the Framers, the constitutional language, a century of decisions of this Court nor Professor Wigmore provides an iota of support for the idea that an accused has an absolute constitutional right not to answer even in the absence of compulsionthe constitutional right not to incriminate himself by making voluntary disclosures.</p>
<p>Today's decision cannot be squared with other provisions of the Constitution which, in my view, define the system of criminal justice this Court is empowered to administer. The Fourth Amendment permits upon probable cause even compulsory searches of the suspect and his possessions and the use of the fruits of the search at trial, all in the absence of counsel. The Fifth Amendment and state constitutional provisions authorize, indeed require, inquisitorial grand jury proceedings at which a potential defendant, in the absence of counsel, <span class="star-pagination">*498</span> is shielded against no more than compulsory incrimination. <i>Mulloney</i> v. <i>United States,</i> <span class="citation" data-id="9641903"><a href="/opinion/1501119/mulloney-v-united-states/#578" aria-description="Citation for case: Mulloney v. United States">79 F. 2d 566, 578</a></span> (C. A. 1st Cir.); <i>United States</i> v. <i>Benjamin,</i> <span class="citation" data-id="1490510"><a href="/opinion/1490510/united-states-v-benjamin/#522" aria-description="Citation for case: United States v. Benjamin">120 F. 2d 521, 522</a></span> (C. A. 2d Cir.); <i>United States</i> v. <i>Scully,</i> <span class="citation" data-id="9444722"><a href="/opinion/237373/united-states-v-patrick-j-scully/#115" aria-description="Citation for case: United States v. Patrick J. Scully">225 F. 2d 113, 115</a></span> (C. A. 2d Cir.); <i>United States</i> v. <i>Gilboy,</i> <span class="citation" data-id="1952574"><a href="/opinion/1952574/united-states-v-gilboy/" aria-description="Citation for case: United States v. Gilboy">160 F. Supp. 442</a></span> (D. C. M. D. Pa.). A grand jury witness, who may be a suspect, is interrogated and his answers, at least until today, are admissible in evidence at trial. And these provisions have been thought of as constitutional safeguards to persons suspected of an offense. Furthermore, until now, the Constitution has permitted the accused to be fingerprinted and to be identified in a line-up or in the courtroom itself.</p>
<p>The Court chooses to ignore these matters and to rely on the virtues and morality of a system of criminal law enforcement which does not depend on the "confession." No such judgment is to be found in the Constitution. It might be appropriate for a legislature to provide that a suspect should not be consulted during a criminal investigation; that an accused should never be called before a grand jury to answer, even if he wants to, what may well be incriminating questions; and that no person, whether he be a suspect, guilty criminal or innocent bystander, should be put to the ordeal of responding to orderly noncompulsory inquiry by the State. But this is not the system our Constitution requires. The only "inquisitions" the Constitution forbids are those which compel incrimination. Escobedo's statements were not compelled and the Court does not hold that they were.</p>
<p>This new American judges' rule, which is to be applied in both federal and state courts, is perhaps thought to be a necessary safeguard against the possibility of extorted confessions. To this extent it reflects a deep-seated distrust of law enforcement officers everywhere, unsupported by relevant data or current material based upon our own <span class="star-pagination">*499</span> experience. Obviously law enforcement officers can make mistakes and exceed their authority, as today's decision shows that even judges can do, but I have somewhat more faith than the Court evidently has in the ability and desire of prosecutors and of the power of the appellate courts to discern and correct such violations of the law.</p>
<p>The Court may be concerned with a narrower matter: the unknowing defendant who responds to police questioning because he mistakenly believes that he must and that his admissions will not be used against him. But this worry hardly calls for the broadside the Court has now fired. The failure to inform an accused that he need not answer and that his answers may be used against him is very relevant indeed to whether the disclosures are compelled. Cases in this Court, to say the least, have never placed a premium on ignorance of constitutional rights. If an accused is told he must answer and does not know better, it would be very doubtful that the resulting admissions could be used against him. When the accused has not been informed of his rights at all the Court characteristically and properly looks very closely at the surrounding circumstances. See <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span>; <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>. I would continue to do so. But in this case Danny Escobedo knew full well that he did not have to answer and knew full well that his lawyer had advised him not to answer.</p>
<p>I do not suggest for a moment that law enforcement will be destroyed by the rule announced today. The need for peace and order is too insistent for that. But it will be crippled and its task made a great deal more difficult, all in my opinion, for unsound, unstated reasons, which can find no home in any of the provisions of the Constitution.</p>
<h2>NOTES</h2>
<p>[1]  Petitioner testified that this ambiguous gesture "could have meant most anything," but that he "took it upon [his] own to think that [the lawyer was telling him] not to say anything," and that the lawyer "wanted to talk" to him.</p>
<p>[2]  The statute then in effect provided in pertinent part that: "All public officers . . . having the custody of any person . . . restrained of his liberty for any alleged cause whatever, shall, except in cases of imminent danger of escape, admit any practicing attorney . . . whom such person . . . may desire to see or consult . . ." Ill. Rev. Stat. (1959), c. 38, § 477. Repealed as of Jan. 1, 1964, by Act approved Aug. 14, 1963, H. B. No. 851.</p>
<p>[3]  The trial judge justified the handcuffing on the ground that it "is ordinary police procedure."</p>
<p>[4]  Compare <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span> (decided on the same day as the decision of the Illinois Supreme Court here), where we said:
</p>
<p>"Our conclusion is in no way foreclosed, as the State contends, by the fact that the state trial judge or the jury may have reached a different result on this issue.</p>
<p>"It is well settled that the duty of constitutional adjudication resting upon this Court requires that the question whether the Due Process Clause of the Fourteenth Amendment has been violated by admission into evidence of a coerced confession be the subject of an <i>independent</i> determination here, see, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#147" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 147-148</a></span>; `we cannot escape the responsibility of making our own examination of the record,' <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#316" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 316</a></span>." (Emphasis in original.)</p>
<p>[5]  Although there is testimony in the record that petitioner and his lawyer had previously discussed what petitioner should do in the event of interrogation, there is no evidence that they discussed what petitioner should, or could, do in the face of a false accusation that he had fired the fatal bullets.</p>
<p>[6]  The English Judges' Rules also recognize that a functional rather than a formal test must be applied and that, under circumstances such as those here, no special significance should be attached to formal indictment. The applicable Rule does not permit the police to question an accused, except in certain extremely limited situations not relevant here, at any time after the defendant "has been charged <i>or informed that he may be prosecuted.</i>" [1964] Crim. L. Rev. 166-170 (emphasis supplied). Although voluntary statements obtained in violation of these rules are not automatically excluded from evidence the judge may, in the exercise of his discretion, exclude them. "Recent cases suggest that perhaps the judges have been tightening up [and almost] inevitably, the effect of the new Rules will be to stimulate this tendency." <i>Id.,</i> at 182.</p>
<p>[7]  Canon 9 of the American Bar Association's Canon of Professional Ethics provides that:
</p>
<p>"A lawyer should not in any way communicate upon the subject of controversy with a party represented by counsel; much less should he undertake to negotiate or compromise the matter with him, but should deal only with his counsel. It is incumbent upon the lawyer most particularly to avoid everything that may tend to mislead a party not represented by counsel, and he should not undertake to advise him as to the law." See Broeder, Wong Sun v. United States: A Study in Faith and Hope, <span class="citation no-link">42 Neb. L. Rev. 483</span>, 599-604.</p>
<p>[8]  Twenty-two States including Illinois, urged us so to hold.</p>
<p>[9]  The Soviet criminal code does not permit a lawyer to be present during the investigation. The Soviet trial has thus been aptly described as "an appeal from the pretrial investigation." Feifer, Justice in Moscow (1964), 86.</p>
<p>[10]  See Barrett, Police Practices and the LawFrom Arrest to Release or Charge, <span class="citation no-link">50 Cal. L. Rev. 11</span>, 43 (1962).</p>
<p>[11]  See Committee Print, Subcommittee to Investigate Administration of the Internal Security Act, Senate Committee on the Judiciary, 85th Cong., 1st Sess., reporting and analyzing the proceedings at the XXth Congress of the Communist Party of the Soviet Union, February 25, 1956, exposing the false confessions obtained during the Stalin purges of the 1930's. See also <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9449514"><a href="/opinion/261371/lawrence-c-miller-jr-v-united-states/#772" aria-description="Citation for case: Lawrence C. Miller, Jr. v. United States">320 F. 2d 767, 772-773</a></span> (opinion of Chief Judge Bazelon); Lifton, Thought Reform and the Psychology of Totalism (1961); Rogge, Why Men Confess (1959); Schein, Coercive Persuasion (1961).</p>
<p>[12]  See Stephen, History of the Criminal Law, quoted in 8 Wigmore, Evidence (3d ed. 1940), 312; Report and Recommendations of the Commissioners' Committee on Police Arrests for Investigation, District of Columbia (1962).</p>
<p>[13]  Cf. Report of Attorney General's Committee on Poverty and the Administration of Federal Criminal Justice (1963), 10-11: "The survival of our system of criminal justice and the values which it advances depends upon a constant, searching, and creative questioning of official decisions and assertions of authority at all stages of the process. . . . Persons [denied access to counsel] are incapable of providing the challenges that are indispensable to satisfactory operation of the system. The loss to the interests of accused individuals, occasioned by these failures, are great and apparent. It is also clear that a situation in which persons are required to contest a serious accusation but are denied access to the tools of contest is offensive to fairness and equity. Beyond these considerations, however, is the fact that [this situation is] detrimental to the proper functioning of the system of justice and that the loss in vitality of the adversary system, thereby occasioned, significantly endangers the basic interests of a free community."</p>
<p>[14]  The accused may, of course, intelligently and knowingly waive his privilege against self-incrimination and his right to counsel either at a pretrial stage or at the trial. See <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>. But no knowing and intelligent waiver of any constitutional right can be said to have occurred under the circumstances of this case.</p>
<p>[15]  The authority of <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, and <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, was weakened by the subsequent decisions of this Court in <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>, <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>, and <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (as the dissenting opinion in the last-cited case recognized).</p>
<p>[*]  "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence."</p>
<p>[*]  "[I]t seems from reported cases that the judges have given up enforcing their own rules, for it is no longer the practice to exclude evidence obtained by questioning in custody. . . . A traditional principle of `fairness' to criminals, which has quite possibly lost some of the reason for its existence, is maintained in words while it is disregarded in fact. . . .
</p>
<p>"The reader may be expecting at this point a vigorous denunciation of the police and of the judges, and a plea for a return to the Judges' Rules as interpreted in 1930. What has to be considered, however, is whether these Rules are a workable part of the machinery of justice. Perhaps the truth is that the Rules have been abandoned, by tacit consent, just because they are an unreasonable restriction upon the activities of the police in bringing criminals to book." Williams, Questioning by the Police: Some Practical Considerations, [1960] Crim. L. Rev. 325, 331-332. See also [1964] Crim. L. Rev. 161-182.</p>

</div>
```

---
