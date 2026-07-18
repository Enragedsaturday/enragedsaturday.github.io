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

## GROUP: content/cases/United States v. Cooley.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Cooley
type: case
citation: "593 U.S. 345 (2021)"
parallel_cite: "141 S. Ct. 1638; 210 L. Ed. 2d 1"
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2021
date_decided: ""
docket: 19-1414
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
  opinion_url: "https://www.courtlistener.com/opinion/4887958/united-states-v-cooley/"
  cluster_id: 4887958
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Cooley
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Recent development
related:
  - "[[Terry v. Ohio]]"
  - "[[Terry Stops and Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - terry-stop
  - reasonable-suspicion
  - tribal-authority
holding: A tribal police officer has authority to detain temporarily and to search a non-Indian traveling on a public right-of-way running through an Indian reservation for potential violations of state or federal law.
---

# United States v. Cooley

*593 U.S. 345 (2021)* (No. 19-1414) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4887958 → opinion 4691737; quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 593 U.S. ___; the Held is on the syllabus page, 593 U.S. 345). S9 promotes. -->

## Background
Crow Tribe police officer James Saylor found Joshua Cooley, a non-Indian, parked at night in a pickup truck on a stretch of U.S. Route 212 — a public right-of-way running through the Crow Reservation in Montana. During the encounter Saylor observed that Cooley appeared impaired, saw two semiautomatic rifles, and then noticed signs of methamphetamine; he detained Cooley and searched the truck, turning up guns and drugs. Cooley was charged with federal drug and firearm offenses. The Ninth Circuit affirmed suppression of the evidence, holding that a tribal officer lacks authority to detain or search a non-Indian on a public right-of-way unless a violation of law is "apparent," and that Saylor had not first tried to determine whether Cooley was an Indian.

## Issue
Whether a tribal police officer has authority to detain temporarily and to search a non-Indian traveling on a public right-of-way running through a reservation for a potential violation of state or federal law.

## Rule
Although tribes generally lack civil and criminal authority over non-members, *Montana v. United States* preserves an exception for conduct that threatens or has a direct effect on the tribe's political integrity, economic security, or health and welfare. That exception supplies the detention-and-search authority at issue: "A tribal police officer has authority to detain temporarily and to search non-Indian persons traveling on public rights-of-way running through a reservation for potential violations of state or federal law." — 593 U.S. at 345 (Syllabus). ^pin-345

The authority is bounded by the ordinary reasonableness limits of a temporary stop: the officer may detain the suspect only for the time reasonably necessary to summon the proper non-tribal authorities.

## Application
Saylor's stop and limited search fit the *Montana* second exception: a highway drug-and-gun threat on a reservation road directly implicates tribal health, welfare, and safety, and the authority to address it does not depend on first confirming the suspect's Indian status. The Court rejected the Ninth Circuit's "apparent violation" and Indian-status-first requirements as unworkable, and found that federal cross-deputization statutes neither displaced nor supplied a substitute for the tribe's retained authority. Justice Alito's [[Common Legal Terms#concurring-opinion|concurrence]] read the holding narrowly in *[[Terry v. Ohio|Terry]]* terms — a tribal officer may stop a non-Indian motorist on reasonable suspicion, search as needed for safety, and, with probable cause, detain the motorist until non-tribal officers arrive.

## Conclusion
The judgment of the Ninth Circuit was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Breyer, J., delivered the opinion of a unanimous Court; Alito, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Cooley* is primarily a tribal-sovereignty decision; its Fourth Amendment relevance here is its use of the temporary-detention framework — reasonable suspicion to stop, a safety search, and detention limited to what is reasonably necessary — to define a tribal officer's authority over non-Indians.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Recent development*

## Sources
- [*United States v. Cooley*, 593 U.S. 345 (2021)](https://www.courtlistener.com/opinion/4887958/united-states-v-cooley/) — pinpoint: 345 (Syllabus, holding); quote string-matched to the CL slip-opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6ce93d396f979f51", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "593 U.S. 345 (2021)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "141 S. Ct. 1638; 210 L. Ed. 2d 1", "title": "United States v. Cooley", "year": "2021"}}
{"assertion_id": "be531f5c0f59d150", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Recent development", "title": "United States v. Cooley"}}
{"assertion_id": "e5b512fd34aa3ee8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A tribal police officer has authority to detain temporarily and to search a non-Indian traveling on a public right-of-way running through an Indian reservation for potential violations of state or federal law.", "title": "United States v. Cooley"}}
{"assertion_id": "3c431254ab8257c9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Cooley"}}
{"assertion_id": "490a4a25b574d89b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Cooley", "varies_by_point": "false"}}
```

### lake record — United States v. Cooley

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cooley",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Cooley",
    "case_name_short": "Cooley",
    "case_name_full": "",
    "input_case_name": "United States v. Cooley",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2021,
    "docket": "19-1414",
    "cluster_id": 4887958,
    "lead_opinion_id": 4691737,
    "sibling_ids": [],
    "absolute_url": "/opinion/4887958/united-states-v-cooley/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "593 U.S. 345",
      "volume": "593",
      "reporter": "U.S.",
      "page": "345",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "141 S. Ct. 1638",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "210 L. Ed. 2d 1",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "593 U.S. 345",
        "volume": "593",
        "reporter": "U.S.",
        "page": "345",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "141 S. Ct. 1638",
        "volume": "141",
        "reporter": "S. Ct.",
        "page": "1638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "210 L. Ed. 2d 1",
        "volume": "210",
        "reporter": "L. Ed. 2d",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "593 U.S. 345",
    "official_selection": {
      "court_class": "scotus",
      "selected": "593 U.S. 345",
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
    "date_created": "2026-07-06T12:10:17Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:10:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:10:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:10:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-cooley--4887958",
      "to_record_id": "United States v. Cooley",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Cooley

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

                    UNITED STATES v. COOLEY

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

      No. 19–1414. Argued March 23, 2021—Decided June 1, 2021
Late one night Officer James Saylor of the Crow Police Department ap-
  proached a truck parked on United States Highway 212, a public right-
  of-way within the Crow Reservation in the State of Montana. Saylor
  spoke to the driver, Joshua James Cooley, and observed that Cooley
  appeared to be non-native and had watery, bloodshot eyes. Saylor also
  noticed two semiautomatic rifles lying on Cooley’s front seat. Fearing
  violence, Saylor ordered Cooley out of the truck and conducted a
  patdown search. Saylor also saw in the truck a glass pipe and a plastic
  bag that contained methamphetamine. Additional officers, including
  an officer with the federal Bureau of Indian Affairs, arrived on the
  scene in response to Saylor’s call for assistance. Saylor was directed
  to seize all contraband in plain view, leading Saylor to discover more
  methamphetamine. Saylor took Cooley to the Crow Police Department
  where federal and local officers further questioned Cooley. Subse-
  quently, a federal grand jury indicted Cooley on drug and gun offenses.
  The District Court granted Cooley’s motion to suppress the drug evi-
  dence. The Ninth Circuit affirmed. It reasoned that a tribal police
  officer could stop (and hold for a reasonable time) a non-Indian suspect
  if the officer first tries to determine whether the suspect is non-Indian
  and, in the course of doing so, finds an apparent violation of state or
  federal law. The Ninth Circuit concluded that Saylor had failed to
  make that initial determination here.
Held: A tribal police officer has authority to detain temporarily and to
 search non-Indian persons traveling on public rights-of-way running
 through a reservation for potential violations of state or federal law.
 Pp. 3–9.
    (a) As a “general proposition,” the “inherent sovereign powers of an
 Indian tribe do not extend to the activities of nonmembers of the tribe.”
2                      UNITED STATES v. COOLEY

                                   Syllabus

    Montana v. United States, 450 U. S. 544, 565. The Court identified in
    Montana two exceptions to that general rule, the second of which fits
    almost like a glove here: A tribe retains inherent authority over the
    conduct of non-Indians on the reservation “when that conduct threat-
    ens or has some direct effect on . . . the health or welfare of the tribe.”
    Id., at 566. The conclusion that Saylor’s actions here fall within Mon-
    tana’s second exception is consistent with the Court’s prior Montana
    cases. See Strate v. A–1 Contractors, 520 U. S. 438, 456 n. 11; see also
    Atkinson Trading Co. v. Shirley, 532 U. S. 645, 651. Similarly, the
    Court has held that when the “jurisdiction to try and punish an of-
    fender rests outside the tribe, tribal officers may exercise their power
    to detain the offender and transport him to the proper authorities.”
    Duro v. Reina, 495 U. S. 676, 697. Ancillary to the authority to
    transport a non-Indian suspect is the authority to search that individ-
    ual prior to transport, as several state courts and other federal courts
    have held. While that authority has sometimes been traced to a tribe’s
    right to exclude non-Indians, tribes “have inherent sovereignty inde-
    pendent of th[e] authority arising from their power to exclude,” Bren-
    dale v. Confederated Tribes and Bands of Yakima Nation, 492 U. S.
    408, 425 (plurality opinion), and here Montana’s second exception rec-
    ognizes that inherent authority. In addition, recognizing a tribal of-
    ficer’s authority to investigate potential violations of state or federal
    laws that apply to non-Indians whether outside a reservation or on a
    public right-of-way within the reservation protects public safety with-
    out implicating the concerns about applying tribal laws to non-Indians
    noted in the Court’s prior cases. Finally, the Court doubts the worka-
    bility of the Ninth Circuit’s standards, which would require tribal of-
    ficers first to determine whether a suspect is non-Indian and, if so, to
    temporarily detain a non-Indian only for “apparent” legal violations.
    919 F. 3d 1135, 1142. The first requirement produces an incentive to
    lie. The second requirement introduces a new standard into search
    and seizure law and creates a problem of interpretation that will arise
    frequently given the prevalence of non-Indians in Indian reservations.
    Pp. 3–7.
       (b) Cooley’s arguments against recognition of inherent tribal sover-
    eignty here are unpersuasive. While the Court agrees the Montana
    exceptions should not be interpreted so as to “ ‘swallow the rule,’ ”
    Plains Commerce Bank v. Long Family Land & Cattle Co., 554 U. S.
    316, 330, this case does not raise that concern due to the close fit be-
    tween Montana’s second exception and the facts here. In addition, the
    Court sees nothing in existing federal cross-deputization statutes that
    suggests Congress has sought to deny tribes the authority at issue. To
    the contrary, existing legislation and executive action appear to oper-
    ate on the assumption that tribes have retained this authority. Pp. 8–9.
                    Cite as: 593 U. S. ____ (2021)                  3

                              Syllabus

919 F. 3d 1135, vacated and remanded.

   BREYER, J., delivered the opinion for a unanimous Court. ALITO, J.,
filed a concurring opinion.
                        Cite as: 593 U. S. ____ (2021)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                    No. 19–1414
                                    _________________


  UNITED STATES, PETITIONER v. JOSHUA JAMES
                   COOLEY
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                                   [June 1, 2021]

   JUSTICE BREYER delivered the opinion of the Court.
   The question presented is whether an Indian tribe’s po-
lice officer has authority to detain temporarily and to
search a non-Indian on a public right-of-way that runs
through an Indian reservation. The search and detention,
we assume, took place based on a potential violation of state
or federal law prior to the suspect’s transport to the proper
nontribal authorities for prosecution.
   We have previously noted that a tribe retains inherent
sovereign authority to address “conduct [that] threatens or
has some direct effect on . . . the health or welfare of the
tribe.” Montana v. United States, 450 U. S. 544, 566 (1981);
see also Strate v. A–1 Contractors, 520 U. S. 438, 456, n. 11
(1997). We believe this statement of law governs here. And
we hold the tribal officer possesses the authority at issue.
                             I
  Late at night in February 2016, Officer James Saylor of
the Crow Police Department was driving east on United
States Highway 212, a public right-of-way within the Crow
Reservation, located within the State of Montana. Saylor
saw a truck parked on the westbound side of the highway.
2                UNITED STATES v. COOLEY

                      Opinion of the Court

Believing the occupants might need assistance, Saylor ap-
proached the truck and spoke to the driver, Joshua James
Cooley. Saylor noticed that Cooley had “watery, bloodshot
eyes” and “appeared to be non-native.” App. to Pet. for Cert.
95a. Saylor also noticed two semiautomatic rifles lying on
the front seat. Eventually fearing violence, Saylor ordered
Cooley out of the truck and conducted a patdown search.
He called tribal and county officers for assistance. While
waiting for the officers to arrive, Saylor returned to the
truck. He saw a glass pipe and plastic bag that contained
methamphetamine. The other officers, including an officer
with the federal Bureau of Indian Affairs, then arrived.
They directed Saylor to seize all contraband in plain view,
leading him to discover more methamphetamine. Saylor
took Cooley to the Crow Police Department where federal
and local officers further questioned Cooley.
   In April 2016, a federal grand jury indicted Cooley on
drug and gun offenses. See 21 U. S. C. §841(a)(1); 18
U. S. C. §924(c)(1)(A). The District Court granted Cooley’s
motion to suppress the drug evidence that Saylor had
seized. It reasoned that Saylor, as a Crow Tribe police of-
ficer, lacked the authority to investigate nonapparent vio-
lations of state or federal law by a non-Indian on a public
right-of-way crossing the reservation.
   The Government appealed. See 18 U. S. C. §3731. The
Ninth Circuit affirmed the District Court’s evidence-
suppression determination. The Ninth Circuit panel wrote
that tribes “cannot exclude non-Indians from a state or fed-
eral highway” and “lack the ancillary power to investigate
non-Indians who are using such public rights-of-way.” 919
F. 3d 1135, 1141 (2019). It added that a tribal police officer
nonetheless could stop (and hold for a reasonable time) a
non-Indian suspect, but only if (1) the officer first tried to
determine whether “the person is an Indian,” and, if the
person turns out to be a non-Indian, (2) it is “apparent” that
the person has violated state or federal law. Id., at 1142.
                  Cite as: 593 U. S. ____ (2021)              3

                      Opinion of the Court

Non-Indian status, the panel added, can usually be deter-
mined by “ask[ing] one question.” Ibid. (internal quotation
marks omitted). Because Saylor had not initially tried to
determine whether Cooley was an Indian, the panel held
that the lower court correctly suppressed the evidence.
   The Ninth Circuit denied the Government’s request for
rehearing en banc. We then granted the Government’s pe-
tition for certiorari in order to decide whether a tribal police
officer has authority to detain temporarily and to search
non-Indians traveling on public rights-of-way running
through a reservation for potential violations of state or fed-
eral law.
                              II
   Long ago we described Indian tribes as “distinct, inde-
pendent political communities” exercising sovereign au-
thority. Worcester v. Georgia, 6 Pet. 515, 559 (1832). Due
to their incorporation into the United States, however, the
“sovereignty that the Indian tribes retain is of a unique and
limited character.” United States v. Wheeler, 435 U. S. 313,
323 (1978). Indian tribes may, for example, determine
tribal membership, regulate domestic affairs among tribal
members, and exclude others from entering tribal land.
See, e.g., Plains Commerce Bank v. Long Family Land &
Cattle Co., 554 U. S. 316, 327–328 (2008). On the other
hand, owing to their “dependent status,” tribes lack any
“freedom independently to determine their external rela-
tions” and cannot, for instance, “enter into direct commer-
cial or governmental relations with foreign nations.”
Wheeler, 435 U. S., at 326. Tribes also lack inherent sover-
eign power to exercise criminal jurisdiction over non-
Indians. See Oliphant v. Suquamish Tribe, 435 U. S. 191,
212 (1978). In all cases, tribal authority remains subject to
the plenary authority of Congress. See, e.g., Michigan v.
Bay Mills Indian Community, 572 U. S. 782, 788 (2014).
   Here, no treaty or statute has explicitly divested Indian
4                 UNITED STATES v. COOLEY

                      Opinion of the Court

tribes of the policing authority at issue. We turn to prece-
dent to determine whether a tribe has retained inherent
sovereign authority to exercise that power. In answering
this question, our decision in Montana v. United States, 450
U. S. 544 (1981), is highly relevant. In that case we asked
whether a tribe could regulate hunting and fishing by non-
Indians on land that non-Indians owned in fee simple on a
reservation. We held that it could not. We supported our
conclusion by referring to our holding in Oliphant that a
tribe could not “exercise criminal jurisdiction over non-
Indians.” Montana, 450 U. S., at 565. We then wrote that
the “principles on which [Oliphant] relied support the gen-
eral proposition that the inherent sovereign powers of an
Indian tribe do not extend to the activities of nonmembers
of the tribe.” Ibid.
   At the same time, we made clear that Montana’s “general
proposition” was not an absolute rule. Ibid. We set forth
two important exceptions. First, we said that a “tribe may
regulate, through taxation, licensing, or other means, the
activities of nonmembers who enter consensual relation-
ships with the tribe or its members, through commercial
dealing, contracts, leases, or other arrangements.” Ibid.
Second, we said that a “tribe may also retain inherent
power to exercise civil authority over the conduct of non-
Indians on fee lands within its reservation when that con-
duct threatens or has some direct effect on the political in-
tegrity, the economic security, or the health or welfare of the
tribe.” Id., at 566 (emphasis added).
   The second exception we have just quoted fits the present
case, almost like a glove. The phrase speaks of the protec-
tion of the “health or welfare of the tribe.” To deny a tribal
police officer authority to search and detain for a reasonable
time any person he or she believes may commit or has com-
mitted a crime would make it difficult for tribes to protect
themselves against ongoing threats. Such threats may be
                 Cite as: 593 U. S. ____ (2021)            5

                     Opinion of the Court

posed by, for instance, non-Indian drunk drivers, transport-
ers of contraband, or other criminal offenders operating on
roads within the boundaries of a tribal reservation. As the
Washington Supreme Court has noted, “[a]llowing a known
drunk driver to get back in his or her car, careen off down
the road, and possibly kill or injure Indians or non-Indians
would certainly be detrimental to the health or welfare of
the Tribe.” State v. Schmuck, 121 Wash. 2d 373, 391, 850
P. 2d 1332, 1341, cert. denied, 510 U. S. 931 (1993).
   We have subsequently repeated Montana’s proposition
and exceptions in several cases involving a tribe’s jurisdic-
tion over the activities of non-Indians within the reserva-
tion. See, e.g., Plains Commerce Bank, 554 U. S., at 328–
330; Nevada v. Hicks, 533 U. S. 353, 358–360, and n. 3
(2001); South Dakota v. Bourland, 508 U. S. 679, 694–696
(1993); Duro v. Reina, 495 U. S. 676, 687–688 (1990); Bren-
dale v. Confederated Tribes and Bands of Yakima Nation,
492 U. S. 408, 426–430 (1989) (plurality opinion). In doing
so we have reserved a tribe’s inherent sovereign authority
to engage in policing of the kind before us. Most notably, in
Strate v. A–1 Contractors, 520 U. S. 438, 456–459 (1997),
we relied upon Montana’s general jurisdiction-limiting
principle to hold that tribal courts did not retain inherent
authority to adjudicate personal-injury actions against non-
members of the tribe based upon automobile accidents that
took place on public rights-of-way running through a reser-
vation. But we also said:
    “We do not here question the authority of tribal police
    to patrol roads within a reservation, including rights-
    of-way made part of a state highway, and to detain and
    turn over to state officers nonmembers stopped on the
    highway for conduct violating state law. Cf. State v.
    Schmuck, 121 Wash. 2d 373, 390, 850 P. 2d 1332, 1341
    (en banc) (recognizing that a limited tribal power ‘to
    stop and detain alleged offenders in no way confers an
6                UNITED STATES v. COOLEY

                     Opinion of the Court

    unlimited authority to regulate the right of the public
    to travel on the Reservation’s roads’), cert. denied, 510
    U. S. 931 (1993).” 520 U. S., at 456, n. 11.
We reiterated this point in Atkinson Trading Co. v. Shirley,
532 U. S. 645, 651 (2001), there confirming that Strate “did
not question the ability of tribal police to patrol the high-
way.”
   Similarly, we recognized in Duro that “[w]here jurisdic-
tion to try and punish an offender rests outside the tribe,
tribal officers may exercise their power to detain the of-
fender and transport him to the proper authorities.” 495
U. S., at 697. The authority to search a non-Indian prior to
transport is ancillary to this authority that we have already
recognized. Cf. Ortiz-Barraza v. United States, 512 F. 2d
1176, 1180–1181 (CA9 1975). Indeed, several state courts
and other federal courts have held that tribal officers pos-
sess the authority at issue here. See, e.g., Schmuck, 121
Wash. 2d, at 390, 850 P. 2d, at 1341; State v. Pamperien,
156 Ore. App. 153, 155–159, 967 P. 2d 503, 504–506 (1998);
State v. Ryder, 98 N. M. 453, 456, 649 P. 2d 756, 759 (1982);
see also United States v. Terry, 400 F. 3d 575, 579–580 (CA8
2005); Ortiz-Barraza, 512 F. 2d, at 1180–1181; see gener-
ally F. Cohen, Handbook of Federal Indian Law §9.07, p.
773 (2012). To be sure, in Duro we traced the relevant tribal
authority to a tribe’s right to exclude non-Indians from res-
ervation land. See 495 U. S., at 696–697. But tribes “have
inherent sovereignty independent of th[e] authority arising
from their power to exclude,” Brendale, 492 U. S., at 425
(plurality opinion), and here Montana’s second exception
recognizes that inherent authority.
   We also note that our prior cases denying tribal jurisdic-
tion over the activities of non-Indians on a reservation have
rested in part upon the fact that full tribal jurisdiction
would require the application of tribal laws to non-Indians
who do not belong to the tribe and consequently had no say
                  Cite as: 593 U. S. ____ (2021)            7

                      Opinion of the Court

in creating the laws that would be applied to them. See
Duro, 495 U. S., at 693 (noting the concern that tribal-court
criminal jurisdiction over nonmembers would subject such
defendants to “trial by political bodies that do not include
them”); Plains Commerce Bank, 554 U. S., at 337 (noting
that nonmembers “have no part in tribal government” and
have “no say in the laws and regulations that govern tribal
territory”). Saylor’s search and detention, however, do not
subsequently subject Cooley to tribal law, but rather only
to state and federal laws that apply whether an individual
is outside a reservation or on a state or federal highway
within it. As the Solicitor General points out, an initial in-
vestigation of non-Indians’ “violations of federal and state
laws to which those non-Indians are indisputably subject”
protects the public without raising “similar concerns” of the
sort raised in our cases limiting tribal authority. Brief for
United States 24–25.
   Finally, we have doubts about the workability of the
standards that the Ninth Circuit set out. Those standards
require tribal officers first to determine whether a suspect
is non-Indian and, if so, allow temporary detention only if
the violation of law is “apparent.” 919 F. 3d, at 1142. The
first requirement, even if limited to asking a single ques-
tion, would produce an incentive to lie. The second require-
ment—that the violation of law be “apparent”—introduces
a new standard into search and seizure law. Whether, or
how, that standard would be met is not obvious. At the
same time, because most of those who live on Indian reser-
vations are non-Indians, this problem of interpretation
could arise frequently. See, e.g., Brief for Former United
States Attorneys as Amici Curiae 24 (noting that 3.5 million
of the 4.6 million people living in American Indian areas in
the 2010 census were non-Indians); Brief for National In-
digenous Women’s Resource Center et al. as Amici Curiae
19–20 (noting that more than 70% of residents on several
reservations are non-Indian).
8                 UNITED STATES v. COOLEY

                      Opinion of the Court

                               III
   In response, Cooley cautions against “inappropriately ex-
pand[ing] the second Montana exception.” Brief for Re-
spondent 24–25 (citing Atkinson, 532 U. S., at 657, n. 12,
and Strate, 520 U. S., at 457–458). We have previously
warned that the Montana exceptions are “limited” and “can-
not be construed in a manner that would swallow the rule.”
Plains Commerce Bank, 554 U. S., at 330 (internal quota-
tion marks omitted). But we have also repeatedly acknowl-
edged the existence of the exceptions and preserved the pos-
sibility that “certain forms of nonmember behavior” may
“sufficiently affect the tribe as to justify tribal oversight.”
Id., at 335. Given the close fit between the second exception
and the circumstances here, we do not believe the warnings
can control the outcome.
   Cooley adds that federal cross-deputization statutes al-
ready grant many Indian tribes a degree of authority to en-
force federal law. See Brief for Respondent 28–30; see gen-
erally 25 U. S. C. §§2803(5), (7) (Secretary of the Interior
may authorize tribal officers to “make inquiries of any per-
son” related to the “carrying out in Indian country” of fed-
eral law and to “perform any other law enforcement related
duty”); §2805 (Secretary of the Interior may promulgate
rules “relating to the enforcement of ” federal criminal law
in Indian country); 25 CFR §12.21 (2019) (Bureau of Indian
Affairs may “issue law enforcement commissions” to tribal
police officers “to obtain active assistance” in enforcing fed-
eral criminal law). Because Congress has specified the
scope of tribal police activity through these statutes, Cooley
argues, the Court must not interpret tribal sovereignty to
fill any remaining gaps in policing authority. See Brief for
Respondent 12.
   We are not convinced by this argument. The statutory
and regulatory provisions to which Cooley refers do not eas-
ily fit the present circumstances. They are overinclusive,
for instance encompassing the authority to arrest. See
                  Cite as: 593 U. S. ____ (2021)                  9

                      Opinion of the Court

§2803(3). And they are also underinclusive. Because these
provisions do not govern violations of state law, tribes
would still need to strike agreements with a variety of other
authorities to ensure complete coverage. See Brief for Ca-
yuga Nation et al. as Amici Curiae 7–8, 25–27. More
broadly, cross-deputization agreements are difficult to
reach, and they often require negotiation between other au-
thorities and the tribes over such matters as training, re-
ciprocal authority to arrest, the “geographical reach of the
agreements, the jurisdiction of the parties, liability of offic-
ers performing under the agreements, and sovereign im-
munity.” Fletcher, Fort, & Singel, Indian Country Law En-
forcement and Cooperative Public Safety Agreements, 89
Mich. Bar J. 42, 44 (2010).
  In short, we see nothing in these provisions that shows
that Congress sought to deny tribes the authority at issue,
authority that rests upon a tribe’s retention of sovereignty
as interpreted by Montana, and in particular its second ex-
ception. To the contrary, in our view, existing legislation
and executive action appear to operate on the assumption
that tribes have retained this authority. See, e.g., Brief for
Current and Former Members of Congress as Amici Curiae
23–25; Brief for Former U. S. Attorneys as Amici Curiae
28–29.
                        *  *    *
  For these reasons, we vacate the Ninth Circuit’s judg-
ment and remand the case for further proceedings con-
sistent with this opinion.

                                                   It is so ordered.
                  Cite as: 593 U. S. ____ (2021)             1

                      ALITO, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 19–1414
                          _________________


  UNITED STATES, PETITIONER v. JOSHUA JAMES
                   COOLEY
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                         [June 1, 2021]

   JUSTICE ALITO, concurring.
   I join the opinion of the Court on the understanding that
it holds no more than the following: On a public right-of-
way that traverses an Indian reservation and is primarily
patrolled by tribal police, a tribal police officer has the au-
thority to (a) stop a non-Indian motorist if the officer has
reasonable suspicion that the motorist may violate or has
violated federal or state law, (b) conduct a search to the ex-
tent necessary to protect himself or others, and (c) if the
tribal officer has probable cause, detain the motorist for the
period of time reasonably necessary for a non-tribal officer
to arrive on the scene.

```

---

## GROUP: content/cases/United States v. Daniels.md  (`case`, 6 assertions)

### content_page

```
---
title: United States v. Daniels
type: case
citation: "101 F.4th 770 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir.
court_level: coa
circuit: ca10
year: 2024
date_decided: 2024-05-08
docket: 22-1378
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9500360/united-states-v-daniels/"
  cluster_id: 9500360
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Daniels
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: Key
  - page: "[[Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Terry v. Ohio]]"
  - "[[United States v. Black]]"
  - "[[Reasonable Suspicion]]"
tags:
  - case
  - fourth-amendment
  - seizure
  - terry-stop
  - reasonable-suspicion
  - anonymous-tip
holding: "The totality of the circumstances did not establish reasonable suspicion to detain Daniels: a near-anonymous, non-emergency tip that alleged no illegality and described men in dark clothing — which Daniels, in a bright orange jumpsuit, did not match — plus his mere proximity to the described SUV in a high-crime area late at night amounted only to an arbitrary hunch, so suppressing his name as the fruit of the unlawful detention was proper."
---

# United States v. Daniels

*101 F.4th 770 (10th Cir. 2024)* (No. 22-1378) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9500360 → opinion 9966973 (101 F.4th 770, decided 2024-05-08); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Just before midnight, the Aurora Police Department received a near-anonymous, non-emergency call reporting that three Black men in dark hoodies and jeans were taking guns in and out of their pockets and getting in and out of a dark SUV in an apartment parking lot; the caller thought they were "getting ready to do something" but conceded it was not an emergency and reported no illegality. Officer Idler arrived at the high-crime complex, spotted a dark SUV, and saw Lyndell Daniels standing five to ten feet away — wearing a bright orange jumpsuit with a reflective strip. Daniels appeared to say something to the SUV, which then drove off at a normal speed. Idler ordered Daniels to raise his hands, detained him, obtained his name, and learned he was a felon. The SUV was later stopped and found to contain a stolen Glock, and Daniels's name led to a DNA warrant tying him to that gun. Charged as a felon in possession, Daniels moved to suppress his name as the fruit of an unlawful detention; the district court granted the motion, and the government appealed.

## Issue
Whether Officer Idler had reasonable suspicion to detain Daniels, where a near-anonymous, non-emergency tip described men in dark clothing handling guns, Daniels wore bright orange and merely stood near the described SUV in a high-crime area late at night, and the tip alleged no illegality.

## Rule
An investigatory detention is justified at its inception only if specific and articulable facts, and the rational inferences from them, give rise to a reasonable suspicion that a person has committed, is committing, or is about to commit a crime, assessed under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. Applying that standard [[Common Legal Terms#de-novo|de novo]], the Tenth Circuit affirmed suppression: "the totality of the circumstances known by Officer Idler when he detained Daniels did not amount to reasonable suspicion. As such, Daniels' detention was unreasonable under the Fourth Amendment, and the district court's grant of Daniels' motion to suppress was proper." — slip op. at 6.

## Application
Each factor fell short. The non-emergency "area watch" tip alleged no illegality and described men in dark hoodies — a description Daniels, in a bright orange jumpsuit, plainly did not match, so the tip could supply suspicion only as to the individuals and things it described. The dark SUV's presence and its unhurried departure were not inherently suspicious, and Daniels's mere proximity and apparently saying something to it did not make him suspicious by association. The late hour and high-crime location added little, and the reported handling of firearms carried limited weight where public carry may be lawful. Taken together, the circumstances left Officer Idler acting on "an arbitrary hunch," not reasonable suspicion particularized to Daniels.

## Conclusion
**Affirmed**: the district court properly suppressed Daniels's name as the fruit of an unlawful detention. Seymour, J., wrote for the court (Eid, Seymour, Kelly, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Daniels* reinforces that reasonable suspicion must be particularized to the person seized: a suspect who does not match a tip's description, and whose only connection is proximity to a described vehicle in a high-crime area at night, cannot be detained on the tip or by association — echoing *[[United States v. Black]]* on lawful firearm activity and suspicion by association.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key*
- [[Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- [*United States v. Daniels*, 101 F.4th 770 (10th Cir. 2024)](https://www.courtlistener.com/opinion/9500360/united-states-v-daniels/) — pinpoint: slip op. at 6 (totality / no-reasonable-suspicion holding); the CL opinion text carries the slip-opinion page numbers rather than 101 F.4th star pagination, so the pin is slip-style per S2 A3. Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7b8d154d2c7234a2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "101 F.4th 770 (2024)", "court": "10th Cir.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Daniels", "year": "2024"}}
{"assertion_id": "30d48ff520796879", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "United States v. Daniels"}}
{"assertion_id": "c5ace58d7e48de11", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Key", "title": "United States v. Daniels"}}
{"assertion_id": "dba4b8c66feac98d", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The totality of the circumstances did not establish reasonable suspicion to detain Daniels: a near-anonymous, non-emergency tip that alleged no illegality and described men in dark clothing — which Daniels, in a bright orange jumpsuit, did not match — plus his mere proximity to the described SUV in a high-crime area late at night amounted only to an arbitrary hunch, so suppressing his name as the fruit of the unlawful detention was proper.", "title": "United States v. Daniels"}}
{"assertion_id": "0bf04e7a619430cc", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Daniels", "varies_by_point": "false"}}
{"assertion_id": "e4acfccabf57fac0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Daniels"}}
```

### lake record — United States v. Daniels

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Daniels",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Daniels",
    "case_name_short": "Daniels",
    "case_name_full": "",
    "input_case_name": "United States v. Daniels",
    "court": "10th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2024-05-08",
    "year": 2024,
    "docket": "22-1378",
    "cluster_id": 9500360,
    "lead_opinion_id": 9966973,
    "sibling_ids": [],
    "absolute_url": "/opinion/9500360/united-states-v-daniels/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "101 F.4th 770",
      "volume": "101",
      "reporter": "F.4th",
      "page": "770",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "101 F.4th 770",
        "volume": "101",
        "reporter": "F.4th",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "101 F.4th 770",
    "official_selection": {
      "court_class": "coa",
      "selected": "101 F.4th 770",
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
    "date_created": "2026-07-07T01:39:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:39:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-daniels--9500360",
      "to_record_id": "United States v. Daniels",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Daniels

```
Appellate Case: 22-1378    Document: 010111045898         Date Filed: 05/08/2024 Page: 1
                                                                                 FILED
                                                                     United States Court of Appeals
                                         PUBLISH                             Tenth Circuit

                        UNITED STATES COURT OF APPEALS                       May 8, 2024

                                                                        Christopher M. Wolpert
                              FOR THE TENTH CIRCUIT                         Clerk of Court


   UNITED STATES OF AMERICA,

         Plaintiff - Appellant,

   v.                                                              No. 22-1378

   LYNDELL DANIELS,

         Defendant - Appellee.



                      Appeal from the United States District Court
                              for the District of Colorado
                          (D.C. No. 21-CR-00332-RMR)
                        _________________________________

 Elizabeth S. Ford Milani, Assistant United States Attorney (Cole Finegan, United States
 Attorney, with her on the brief), Office of the United States Attorney, Denver, Colorado,
 for Plaintiff-Appellant.

 John C. Arceci, Assistant Federal Public Defender (Virginia L. Grady, Federal Public
 Defender, with him on the briefs), Office of the Federal Public Defender, Denver,
 Colorado, for Defendant-Appellee.
                          _________________________________

 Before EID, SEYMOUR, and KELLY, Circuit Judges.
                   _________________________________

 SEYMOUR, Circuit Judge.
                     _________________________________

        Mr. Lyndell Daniels was detained by law enforcement who, by using his name,

 connected Daniels to a stolen Glock and charged him with being a felon in possession of a
Appellate Case: 22-1378     Document: 010111045898         Date Filed: 05/08/2024       Page: 2


 firearm in violation of 18 U.S.C. § 922(g)(1). Daniels moved to suppress his name as the

 fruit of an unlawful investigative detention, arguing the officers had no reasonable

 suspicion to detain him. The district court agreed and granted his motion. On appeal, the

 government argues the district court erred because there was reasonable suspicion to detain

 Daniels. We affirm.

                                         Background

        Just before midnight on February 7, 2021, the Aurora Police Department received a

 near-anonymous call. The caller expressed concern over something happening in her

 apartment complex’s parking lot: Three Black men, wearing dark hoodies and jeans, were

 intermittently taking guns in and out of their pockets and getting in and out of a dark SUV.

 The caller believed they were “getting ready to do something,” but conceded that it was not

 an emergency and reported no illegality. Rec., vol. I at 55. The call was logged as a non-

 emergency “area watch.” Id.

        Aurora Police Officers William Idler and Glenn Snow were dispatched to the

 caller’s apartment, located in a high-crime neighborhood of Aurora, Colorado. The

 complex was densely populated, and the parking lot was well-lit. Officer Idler arrived first

 and identified what he assumed to be the reported dark SUV. Standing five to ten feet away

 from the SUV was Daniels. Daniels was wearing a bright orange jumpsuit with a reflective

 strip and an orange hood under a black jacket. Officer Idler testified that as he approached,

 Daniels appeared to say something (which he could not hear) to the SUV. At that point, the

 SUV left the parking lot at a normal rate of speed. Officer Idler identified himself and




                                               2
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024      Page: 3


 ordered Daniels to put his hands up. Daniels immediately complied and was detained.

 Officer Idler acquired Daniels’ name, ran a criminal background check, and discovered he

 was a convicted felon.

        Police separately followed the dark SUV. The car drove lawfully, but eventually ran

 a red light and was stopped. Within the vehicle, officers found four firearms, one of which

 was a stolen 9mm Glock 17. Using Daniels’ name, law enforcement obtained a warrant for

 his DNA. Subsequent forensic testing of the DNA tied Daniels to the stolen Glock. A grand

 jury indicted Daniels on the sole count of being a felon in possession of a firearm in

 violation of 18 U.S.C. § 922(g)(1). In response, Daniels moved to suppress his name as the

 fruit of Officer Idler’s unlawful detention. The district court held an evidentiary hearing

 and then granted his motion. This appeal followed.

                                              Discussion

        The government argues that the district court erred in granting Daniels’ motion to

 suppress because Officer Idler had reasonable suspicion to detain Daniels. When reviewing

 a district court’s grant of a motion to suppress, we review factual findings for clear error

 and legal determinations de novo. United States v. Morales, 961 F.3d 1086, 1090 (10th Cir.

 2020). “[We] view[] the evidence in the light most favorable to the district court’s

 decision.” Id. The ultimate question of reasonableness under the Fourth Amendment we

 review de novo. Id.

        The Fourth Amendment establishes a right to be free from “unreasonable searches

 and seizures.” U.S. Const. amend. IV. Even so, in Terry v. Ohio, 392 U.S. 1 (1968), the




                                                3
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 4


 Supreme Court clarified that “a police officer may in appropriate circumstances and in an

 appropriate manner approach a person for purposes of investigating possibly criminal

 behavior even though there is no probable cause to make an arrest.” 392 U.S. at 22. In

 other words, the Fourth Amendment permits temporary detentions of individuals—so long

 as “the facts available to the officer at the moment of the seizure or the search ‘warrant a

 man of reasonable caution in the belief’ that the action taken was appropriate.” Id. at 21–

 22. See also United States v. McHugh, 639 F.3d 1250, 1255 (10th Cir. 2011) (observing

 that the Fourth Amendment protects individuals from unreasonable “investigatory stops”

 and detentions). To be “reasonable” a police officer’s investigatory stop must be “justified

 at its inception,” and the “officer’s actions must be reasonably related in scope to the

 circumstances which justified the interference in the first place.” United States v. Madrid,

 713 F.3d 1251, 1256 (10th Cir. 2013) (quoting Terry, 392 U.S. at 20) (internal quotations

 omitted). This appeal concerns only the first prong, i.e., whether Daniels’ detention by

 Officer Idler was justified at its inception.

        “An investigatory detention is justified at its inception if the specific and articulable

 facts and rational inferences drawn from those facts give rise to a reasonable suspicion a

 person has or is committing a crime,” id. (quoting McHugh, 639 F.3d at 1255), or “that

 criminal activity ‘may be afoot.’” United States v. Sokolow, 490 U.S. 1, 7 (1989). Police

 officers must have “reasonable suspicion that criminal activity ‘is, has, or is about to

 occur.’” United States v. Copening, 506 F.3d 1241, 1246 (10th Cir. 2007); see also United

 States v. Cortez, 449 U.S. 411, 417 (1981) (“An investigatory stop must be justified by




                                                 4
Appellate Case: 22-1378        Document: 010111045898         Date Filed: 05/08/2024       Page: 5


 some objective manifestation that the person stopped is, or is about to be, engaged in

 criminal activity.”). It is true that “the likelihood of criminal activity need not rise to the

 level required for probable cause,” United States v. Arvizu, 534 U.S. 266, 274 (2002), but it

 is equally true that officers cannot rely on “inchoate and unparticularized suspicion[s] or

 ‘hunch[es].’” Sokolow, 490 U.S. at 7. The Fourth Amendment requires “some minimal

 level of objective justification.” Id. The objective nature of this standard is key. See Terry,

 392 U.S. at 21–22 (“[I]t is imperative that the facts be judged against an objective standard

 . . . .”) (emphasis added).

        To determine whether a detaining officer had the required “particularized and

 objective basis for suspecting [a] particular person stopped of criminal activity,” we

 consider the “totality of the circumstances—the whole picture.” Cortez, 449 U.S. at 417–

 18. When making that determination, “a court may not evaluate and reject each factor in

 isolation.” Madrid, 713 F.3d at 1256 (quoting United States v. Gandara-Salinas, 327 F.3d

 1127, 1130 (10th Cir. 2003)). Indeed, “[c]onduct that may be wholly innocent may

 nonetheless support a finding of reasonable suspicion in certain circumstances.” United

 States v. Johnson, 364 F.3d 1185, 1192 (10th Cir. 2004). All factors, “mitigating and

 aggravating,” must be considered in the totality of the circumstances. Id. at 1193.

        The parties agree Officer Idler detained Daniels for the purposes of the Fourth

 Amendment and so was subject to its strictures. The parties and the district court further

 agree that there were four relevant factors and circumstances known to Officer Idler when

 he detained Daniels: (1) the 911 phone call and Computer Aided Dispatch (“CAD”) notes,




                                                 5
Appellate Case: 22-1378       Document: 010111045898          Date Filed: 05/08/2024       Page: 6


 (2) the presence and actions of the dark SUV, (3) the time of Officer Idler’s encounter with

 Daniels, and (4) the location of their encounter. The question before us is whether the

 district court properly analyzed and weighed these factors when determining Officer Idler

 did not have reasonable suspicion to detain Daniels. Our de novo review convinces us that

 the totality of the circumstances known by Officer Idler when he detained Daniels did not

 amount to reasonable suspicion. As such, Daniels’ detention was unreasonable under the

 Fourth Amendment, and the district court’s grant of Daniels’ motion to suppress was

 proper. We address each factor before analyzing all together to determine whether the

 totality of the circumstances established reasonable suspicion. United States v. Leon, 80

 F.4th 1160, 1166 (10th Cir. 2023).

        1. The 911 Call

        The district court began by analyzing the import of the near-anonymous 911 call. A

 tip to the police, like a 911 call, can “justify an investigatory stop if under the totality of the

 circumstances the tip furnishes both sufficient indicia of reliability and sufficient

 information to provide reasonable suspicion that criminal conduct is, has, or is about to

 occur.” Madrid, 713 F.3d at 1258. Our analysis to determine a tip’s reliability is “case-

 specific” and factor-based. United States v. Chavez, 660 F.3d 1215, 1222 (10th Cir. 2011).

 We consider:

        (1) [W]hether the informant lacked “true anonymity” (i.e., whether the police knew
        some details about the informant or had means to discover them); (2) whether the
        informant reported contemporaneous, firsthand knowledge; (3) whether the
        informant provided detailed information about the events observed; (4) the
        informant’s stated motivation for reporting the information; and (5) whether the
        police were able to corroborate information provided by the informant.


                                                 6
Appellate Case: 22-1378      Document: 010111045898           Date Filed: 05/08/2024        Page: 7



 Id. “[N]o single factor is dispositive.” Id.

        The district court eschewed this factor-based inquiry for a comparison between the

 instant case and Florida v. J.L., 529 U.S. 266 (2000), in which the Supreme Court found

 that “the bare report of an unknown, unaccountable informant,” unaccompanied by

 “specific indicia of reliability” was insufficient to establish reasonable suspicion. 529 U.S.

 at 269, 271. While the district court’s comparative analysis was not per se improper, see

 Chavez, 660 F.3d at 1222 (comparing the factual circumstances between J.L. and the case

 before it), it was insufficient. Since J.L., our circuit has articulated the nature of those

 “specific indicia of reliability,” and the district court should have evaluated the presence

 (or lack thereof) of those indicia in its analysis. See, e.g., Chavez, 660 F.3d at 1222;

 Copening, 506 F.3d at 1247; United States v. Brown, 496 F.3d 1070 (10th Cir. 2007);

 Madrid, 713 F.3d at 1258. United States v. Johnson is illustrative: There, when considering

 the reliability of an anonymous tip, we were “mindful of the concerns expressed in J.L.,”

 but ultimately evaluated those concerns alongside the specific facts of Johnson’s case. See

 364 F.3d at 1191.

        As we review the facts of this case under the proper analysis, the call is close. All

 the indicia we traditionally consider appear to be present, but to varying degrees of

 potency. The 911 call alone was certainly insufficient to establish reasonable suspicion—

 indeed, the government itself does not contend that it was sufficient—and the call’s

 reliability, even when placed alongside the other facts of this case, is not determinative.




                                                 7
Appellate Case: 22-1378       Document: 010111045898          Date Filed: 05/08/2024       Page: 8


          Nonetheless, even assuming its reliability, we afford the 911 call little weight. In

 Navarette v. California, 572 U.S. 393 (2014), the Supreme Court observed that even a

 reliable tip must create “reasonable suspicion that ‘criminal activity may be afoot.’” 572

 U.S. at 401 (citing Terry, 392 U.S. at 30). As an example, it noted that “a reliable tip

 alleging the dangerous behaviors [consistent with drunk driving] would justify a traffic

 stop on suspicion of drunk driving.” Id. at 402. Here, we have assumed arguendo the 911

 call’s reliability, but that inquiry is separate from its utility in establishing reasonable

 suspicion. Id. The tip alleged no criminal activity or dangerous behaviors; the caller only

 reported that guns were being intermittently taken in and out of pockets, and that the three

 Black men “look like they are getting ready to do something.” Rec., vol. I at 57. This may

 be odd, but it is not obviously illegal. Moreover, if we are to take seriously the normative

 thrust of the Supreme Court’s recent decision in New York State Rifle & Pistol Association,

 Inc., v. Bruen, 597 U.S. 1 (2022), then we cannot look with suspicion on citizens

 presumably exercising their Second Amendment rights in a lawful way. 597 U.S. at 70

 (“The constitutional right to bear arms in public for self-defense is not a ‘second-class right

 . . . .”).

          Granted, “reasonable suspicion may exist even where a 911 call fails to allege

 criminal activity,” see United States v. Conner, 699 F.3d 1225, 1231 (10th Cir. 2012), but

 the described activity here, i.e., three Black men looking like they were about to “do

 something,” getting in and out of an SUV, is simply too generic. The men were not yelling

 or hollering or running or disturbing anyone or, frankly, doing much of anything. Another




                                                 8
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 9


 caller reporting that she was nervous because three armed Black men were relaxing

 alongside an SUV would have been just as descriptive and (un)helpful in establishing

 reasonable suspicion.

        The tip is even less useful in establishing reasonable suspicion for Daniels. Recall,

 the 911 call could have only helped establish reasonable suspicion for the individuals or

 things described. United States v. Fisher, 597 F.3d 1156, 1158–59 (10th Cir. 2010) (“The

 particular person that is stopped must be suspected of criminal activity.”). The district court

 found that it would have been “objectively unreasonable” for Officer Idler to believe that

 Daniels was one of the men described, because he “so obviously did not match the

 description of the individuals identified by the caller.” Rec., vol. I at 115. When asked

 during testimony, Officer Snow, who accompanied Officer Idler to the scene, agreed that

 Daniels “did not match the description . . . that the caller had given.” Rec., vol. IV at 76.

 “Other than the fact that he was black, there was nothing about the Defendant to suggest

 that he was one of the individuals described by the 911 caller.” Rec., vol. I at 115. We

 agree. That criminal activity might be afoot does not give police carte blanche to arrest

 everyone who happens to be nearby. See Fisher, 597 F.3d at 1158–59.

        We consider the 911 call in our totality analysis, but we appropriately “discount” the

 weight we afford it because of the call’s supergeneric, innocuous nature and because

 Daniels himself was not described in it. Johnson, 364 F.3d at 1192.




                                                9
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 10


         2. The Presence and Actions of the SUV

         The district court next considered the weight that should be given to the presence

  and actions of the dark SUV that was idling in the parking lot and that then drove away

  (ostensibly at the direction of Daniels) as Officer Idler approached. We hold that the SUV

  and its actions were insufficient alone to establish reasonable suspicion.

         The government argued below and to us that Officer Idler had reasonable suspicion

  to stop Daniels because of Daniels’ association with the SUV. We interpret this argument

  as raising two important inquiries: (1) whether the SUV itself was reasonably suspicious

  because of its presence and actions, and (2) the nature of Daniels’ association with the

  SUV.

         We address first whether the dark SUV itself was reasonably suspicious. The SUV

  at issue was idling in front of Daniels’ apartment complex as Officer Idler approached. But

  it was far from the only vehicle present. Officer Idler’s bodycam shows at least three other

  cars idling in front of the complex; at least three cars leaving or driving through the lot; one

  car parked in the no-parking loading zone; and no open parking spots to be seen. In other

  words, the parking lot was packed and busy, especially given the late hour. In that context,

  we do not find the dark SUV’s mere presence in the lot to be odd, much less suspicious.

  We do not ignore that the 911 call reported that there was a “dark color SUV” in the

  parking lot. And, indeed, so there was. But the tip’s support is ultimately superficial, and

  its practical utility limited. The bodycam footage shows two “dark color” SUVs, one black,

  the other burgundy, idling in the complex’s lot, one right behind the other. The SUV at




                                                10
Appellate Case: 22-1378       Document: 010111045898           Date Filed: 05/08/2024       Page: 11


  issue in this case turned out to be the black SUV, but the caller gave no hint which one she

  was referring to. The CAD notes are absent of any make, model, color, or license plate

  number.1 It was a coin flip then, as equally likely to be wrong as right, by Officer Idler

  when deciding which SUV’s presence in the lot was “suspicious.” In that sense, even

  assuming the tip’s “reliabil[ity] in its assertion of illegality,”2 it was certainly not reliable

  “in its tendency to identify a determinate person [or thing].” J.L., 529 U.S. at 272. We are

  generally skeptical of anonymous or near-anonymous tips, and even more skeptical when

  they are supergeneric, as here. See Johnson, 364 F.3d at 1191 (“Overly generic tips, even if

  made in good faith, could give police excessive discretion to stop and search large numbers

  of citizens.”). The situation faced by Officer Idler as he approached the complex and was

  forced to proceed on an arbitrary hunch is a good illustration why.

           Moreover, although reasonable suspicion does not demand witnessing illegal

  conduct, Conner, 699 F.3d at 1231 (“Reasonable suspicion may exist even where . . . the

  responding officers do not observe any illegal conduct.”), Officer Idler did not observe any

  criminal activity or even the guns reported by the 911 tipster, weakening the claim that the

  SUV was inherently suspicious.3 Indeed, our review of the record indicates that Officer


  1
   The CAD notes did provide slightly more description for a nearby sedan, which the caller
  described as either “sil[ver] or white.” Rec., vol. I at 58.
  2
      Which, we again emphasize, the tip did not allege.
  3
    The district court made a factual finding that “Further, there is no evidence here that the
  officers observed anything to suggest that the SUV or its occupants were carrying guns or
  otherwise engaged in illegal activity.” Rec., vol. I at 117. Our independent review of the
  record confirms this assessment. Morales, 961 F.3d at 1090.


                                                  11
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024     Page: 12


  Idler did not witness any activity whatsoever by anyone in or near the SUV before the SUV

  drove away. We are ever “mindful of the concerns expressed in J.L.,” Johnson, 364 F.3d at

  1191, and we find the facts of this case uncomfortably reminiscent of the facts there. In

  J.L., aside from an anonymous tip, the “officers had no reason to suspect” J.L. and his

  friends of any illegal conduct, the officers “did not see a firearm,” J.L. and his friends made

  no threatening or otherwise unusual movements, and when the officers approached, J.L.

  was “just hanging out.” J.L., 529 U.S. at 268. Here, there was a near-anonymous tip that

  did not allege illegal conduct, no illegal conduct or firearms were seen, neither the SUV

  nor Daniels made any threatening or unusual movements, and the SUV appeared to be

  innocuously idling as Officer Idler approached.

         Of course, the SUV did drive away as Officer Idler approached (ostensibly at

  Daniels’ direction in Officer Idler’s recount). This action by the SUV offers more, but

  ultimately insufficient, support to establish reasonable suspicion. Certainly, we can and do

  consider a suspect’s evasive movements in determining reasonable suspicion, see, e.g.,

  United States v. Briggs, 720 F.3d 1281, 1286 (10th Cir. 2013), and “headlong flight” is far

  from the only behavior that is fair game, see id. at 1287.4 The facts here make it difficult to


  4
   Our caselaw requires something more than just walking away when the police arrive.
  After all, “not all attempts to avoid police contact raise suspicion[].” Briggs, 720 F.3d at
  1287. The government cites several cases, but none are persuasively analogous. In United
  States v. Briggs, the defendants “changed direction” and “picked up their pace”; Briggs
  “repeatedly looked over his shoulder” and “grabbed at the waistline of his pants”; and one
  defendant was “nearly running.” 720 F.3d at 1283,1287. In United States v. Ballance, we
  admitted that Ballance’s “walking away from [a] gas station on foot” supported reasonable
  suspicion, but there was a tip alleging illegality and identifying Ballance’s specific car. No.



                                                12
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024     Page: 13


  determine whether the SUV was attempting to evade the police as it drove away. The

  district court did not think it was, finding that the “SUV here simply left the parking lot.”

  Rec., vol. I at 117. The government does not allege that finding was clearly erroneous, and

  upon our review of the record, we agree. See Morales, 961 F.3d at 1090. The bodycam

  shows the SUV driving away at a normal rate of speed, a speed similar to that of a white

  car that can be seen leaving as Officer Idler arrived. According to Officer Snow, who had a

  better vantage point, the black SUV did not appear to drive away “at a high rate of speed”

  or “jump a curb or anything like that,” and otherwise simply, and safely, departed. Rec.,

  vol. IV at 74. Further, the burgundy SUV left during the encounter, and another vehicle

  drove several yards away when Officer Idler approached. This confirms that the parking lot

  was busy with activity. We cannot say that simply leaving the lot, as the bodycam footage

  shows several other cars similarly doing, indicated that criminal activity was afoot. In

  United States v. Davis, 94 F.3d 1465 (10th Cir. 1996), we found that a defendant’s “actions

  in exiting [a] car, making and then breaking eye contact with the officers, and then walking

  away from the officers” was not sufficient alone to establish reasonable suspicion. The

  facts in this case offer even less support. 94 F.3d at 1468. The SUV driving away at a

  normal rate of speed as Officer Idler approached is not enough to establish the


  20-3141, 2022 WL 108330, at *6 (10th Cir. Jan. 12, 2022) (unpublished). United States v.
  Madrid stands for the proposition that the defendant’s “attempted exit from [a] parking lot
  just after a police car drove by” could be considered in the reasonable suspicion analysis,
  713 F.3d at 1257, which the district court here did not dispute. United States v. Robinson is
  the only case cited that has held that a simple “about-face” could contribute, but it is
  unpublished and its analysis is conclusory. 304 F.App’x 746, 751 (10th Cir. 2008)
  (unpublished).


                                                13
Appellate Case: 22-1378        Document: 010111045898        Date Filed: 05/08/2024     Page: 14


  “particularized and objective basis for suspecting” it of criminal activity. Cortez, 449 U.S.

  at 417.

            That leads to our second inquiry, Daniels’ association with the SUV. We interpret

  the government as arguing that Daniels’ interaction with the SUV (ostensibly warning the

  SUV to leave as Officer Idler approached) both contributed to the reasonable suspicion of

  the SUV and linked Daniels to it. We are unpersuaded, because Daniels’ connection to the

  SUV appears tenuous. The government alleges that the SUV left at the direction of

  Daniels. But Officer Idler did not hear what Daniels may have said to the SUV’s

  occupants. True, we do “accord deference to an officer’s ability to distinguish between

  innocent and suspicious actions,” see Madrid, 713 F.3d at 1256, but we are not required to

  take on blind faith an officer’s speculation on the contents of a conversation he admits he

  could not hear.5 A fair inference for Officer Idler to have made was that there was some

  relationship between the occupants of the SUV and Daniels. But the nature of that

  relationship was unknown. This inference may have been sufficient if the SUV had done

  something else to be reasonably suspicious, but the other facts do not substantially indicate

  that Officer Idler had a “particular and objective basis” to suspect either Daniels (or the



  5
    Indeed, we are especially reticent to accord much deference to Officer Idler’s instincts
  given his contradictory narratives. In his summary of the stop, related the following day,
  Officer Idler reported a mundane, if ambiguous, scene: “I heard [Daniels] saying
  something when the Dark SUV pulled out of the parking lot and fled the scene.” Rec., vol.
  I at 28. However, at his testimony, Officer Idler’s story recast Daniels into the role of
  scout, warning the SUV to flee as he approached: “[T]he person in the orange jumpsuit
  with the black jacket on [Daniels] I heard say something to the people inside the black
  SUV, and then the black SUV took off.” Rec., vol. IV at 29.


                                                 14
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024        Page: 15


  SUV) had been or was committing a crime. See id. That is, after all, our reasonable

  suspicion lodestar: whether the facts tended to show that Daniels committed or was about

  to commit a crime. See Johnson, 364 F.3d at 1189. His proximity to an innocuous SUV and

  an unknown conversation with its occupants who then simply left when Officer Idler

  approached do not tend to show that.

         All of this can and must be considered in our final totality of the circumstances

  analysis, but we agree with the district court that neither the SUV’s nor Daniels’ presence

  or actions are sufficient alone to establish reasonable suspicion.

         3. The Time and Location

         The district court finally considered the location and time of Officer Idler’s

  encounter with Daniels. It observed that the stop occurred in a “high crime area” of Aurora,

  Colorado “in the middle of the night,” and concluded that those facts, although insufficient

  alone, could be considered in the totality of the circumstances analysis. We agree.6

         Of course, these factors do not operate as a “check-the-box” exercise or foreclose

  analysis of “relevant contextual considerations.” Wardlow, 528 U.S. at 124. Here, Officer

  Idler detained Daniels near midnight. But the evening in question was February 7, 2021,



  6
    Caselaw has extensively established that such facts can be considered. See, e.g., Illinois v.
  Wardlow, 528 U.S. 119, 124 (2000); McHugh, 639 F.3d at 1257; United States v. DeJear,
  552 F.3d 1196, 1201 (10th Cir. 2009) (noting that “the fact that conduct occurs in an area
  known for criminal activity” should be considered when determining reasonable
  suspicion); United States v. Clarkson, 551 F.3d 1196, 1202 (10th Cir. 2009) (“This court
  has also considered the time of night as a factor in determining the existence of reasonable
  suspicion.”); Gallegos v. City of Colo. Springs, 114 F.3d 1024, 1029 (10th Cir. 1997)
  (considering the time of night, 1:15 AM, in the reasonable suspicion analysis).


                                                15
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024      Page: 16


  the night of the Super Bowl LV. An officer should have expected football fans celebrating

  (or commiserating about) the game’s outcome late into the night. The time of day Officer

  Idler encountered Daniels is militated by the events of that day. Moreover, the district court

  found the parking lot was “well-lit,” “densely populated,” and “heavily trafficked,” and we

  agree. Rec., vol. I at 119. This further militates against finding reasonable suspicion,

  because any actions taken by the SUV’s occupants (or Daniels) would be easily seen and

  quickly reported, which Officer Idler would have known.

         That the neighborhood was a “high-crime area” with police often getting calls for

  “domestic violence or people with weapons or other such various felonies or intense

  crimes,” Rec., vol. IV at 20–21, did offer some objective and particularized reason for

  suspicion. But caselaw has been skeptical that such a factor can carry the day. See, e.g.,

  United States v. Dennison, 410 F.3d 1203, 1208 (10th Cir. 2005) (“[Defendant]’s presence

  in a high-crime area is not, ‘standing alone,’ enough to provide reasonable suspicion, but it

  may be a ‘relevant contextual consideration’ in a Terry analysis.”).

         Both the time and location factors are relevant, and so we consider them in our

  totality of the circumstances analysis below. But neither one was sufficient by itself to

  establish reasonable suspicion.

         4. Totality of the Circumstances

         Having concluded that none of those factors alone establish reasonable suspicion,

  our task is now to consider the “totality of the circumstances—the whole picture,” faced by

  Officer Idler as he approached and detained Daniels. Cortez, 449 U.S. at 417–18.




                                                16
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024     Page: 17


         Our review of the records shows the following circumstances were known to Officer

  Idler as he approached and detained Daniels on that fateful February 7th night: (1) the

  police received an arguably reliable tip describing three Black men in dark clothing,

  holding guns, and getting in and out of a dark SUV; (2) the tipster believed the men were

  about to “do something” but reported no illegality; (3) based on the call, Officers Snow and

  Idler were dispatched on a “non-emergency area watch request”; (4) the officers did not see

  any of the men identified by the caller, but possibly identified the “dark color SUV”

  reported as a black SUV idling in front of the complex; (5) the officers did not see any

  guns or illegal activity when they arrived; (6) Officer Idler saw Daniels who was wearing a

  bright orange jumpsuit, orange jeans, and a black jacket; (7) Daniels was standing five to

  ten feet away from the black SUV; (8) Officer Idler thought he heard Daniels say

  something to the SUV, after which the SUV left the lot at a “normal rate of speed”; (9)

  Daniels did not have any guns, did not attempt to leave the scene, and initially complied

  with all of Officer Idler’s orders; (10) the encounter took place near midnight; (11) the stop

  was in a high-crime area; and (12) the parking lot was busy, packed, and well-lit. Like the

  district court, we are not persuaded that these circumstances provided Officer Idler with

  reasonable suspicion to detain Daniels.

         We again emphasize the principle that anchors our analysis: Officer Idler had to

  have a “particularized and objective basis” to believe Daniels had been or was committing,

  or was about to commit a crime or engage in criminal activity. Cortez, 449 U.S. at 417–18.

  That minimal objective basis was not met here. The supergeneric and vague 911 tip did not




                                               17
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 18


  allege illegal, or even particularly unusual, activity by the men the caller identified, and

  nowhere at all did it describe anyone akin to Daniels. As Officer Idler arrived, he was

  confronted by an unremarkable, frankly banal, scene: a packed and busy apartment parking

  lot with several cars leaving, idling in, and driving through it. It was perhaps a bit more

  puzzling given the late time of night, but that could have been plausibly explained by the

  trouncing the Buccaneers had shown the Chiefs only a few hours prior.7 As the caller had

  described, there was a “dark colored SUV” outside, two in fact, but no hint as to which one

  the caller had been referring. Despite the area’s reputation as a “high-crime area,” the

  bodycam footage shows nothing was amiss, much less dangerous, as Officer Idler

  approached the scene. Officer Idler admitted that he did not see any weapons when he

  arrived. As he approached, he heard Daniels say something (ostensibly to the SUV) and

  saw the black SUV, which had been idling, leave at a normal, lawful speed. Neither before

  nor after being stopped did Daniels make any threatening or evasive movements, and he

  complied with all Officer Idler’s orders. Daniels had no firearms on him, and he was

  dressed in a bright, eye-catching orange jumpsuit—which seems to be a somewhat

  counterintuitive fashion choice for someone committing, or about to commit, a crime and

  hoping to get away with it.

         The most glaring thing about these circumstances viewed together is what there is

  not: any hint of any kind of illegality whatsoever. True, “[c]onduct that may be wholly



  7
    For those keeping score, the Buccaneers ended the night with a final victory of 31–9 over
  the Chiefs.


                                                18
Appellate Case: 22-1378      Document: 010111045898           Date Filed: 05/08/2024      Page: 19


  innocent may nonetheless support a finding of reasonable suspicion in certain

  circumstances,” but here we have trouble identifying anything but innocent conduct.

  Johnson, 364 F.3d at 1192. Even analyzing everything together, we are not persuaded the

  circumstances known to Officer Idler “tend to show that [Daniels had] committed or [was]

  about to commit a crime,” as reasonable suspicion demands. Id. at 1189. There are precious

  few facts to suggest that criminal activity was “afoot”—and fewer still that Daniels had any

  role in it, if it was. Whatever is needed to establish reasonable suspicion, this case falls

  short of that minimal particularized and objective basis we have always required. Because

  there was no reasonable suspicion to stop Daniels, Officer Idler’s investigatory detention of

  him was unreasonable under the Fourth Amendment, and the district court’s order to

  suppress was proper.

         Before concluding, we address two of the government’s arguments that the district

  court’s process when conducting its totality of the circumstances analysis was improper.

  First, the government appears to suggest that the district court should not have been

  allowed to consider and weigh the innocent and unsuspicious facts in the record when

  determining whether Officer Idler had reasonable suspicion. See Aplt. Br. at 27; Aplt.

  Reply at 11. To the extent that is their argument, it is certainly wrong. The district court

  was not only empowered, but required, to evaluate all the factors in the record when

  analyzing reasonable suspicion, including facts militating against reasonable suspicion. See

  Johnson, 364 F.3d at 1193 (“All of the[] factors, mitigating and aggravating, should have




                                                 19
Appellate Case: 22-1378       Document: 010111045898           Date Filed: 05/08/2024          Page: 20


  been analyzed as part of the totality of the circumstances faced by Officer Middleton at the

  inception of the detention.”).

         Second, the government contends that the district court analyzed each factor (the

  911 call, the SUV, the time and location) in isolation, rather than weighing them together.

  To illustrate the kind of analysis we have found impermissible, it points us to Johnson.

  There, too, the district court granted a motion to suppress based on four factors. See id. at

  1189–90. The court conducted its totality analysis by “proceed[ing] through the factors . . .

  evaluat[ing] and reject]ing] each before moving on to the next.” Id. at 1190. The court

  mentioned the “appropriate ‘totality of the circumstances’ standard only once, in passing,

  and only after having analyzed each factor . . . in isolation.” Id. This, we found, was

  improper. Id. at 1189.

         Here, the district court avoided the improper process in Johnson. It analyzed each

  factor individually, but it was clear that it would consider all the facts in its totality

  analysis: “This Court will analyze each fact, and it will then consider all the facts together

  to determine whether the totality of the circumstances supports a finding of reasonable

  suspicion sufficient to support the Defendant’s detention.” Rec., vol. I at 111 (emphasis

  added). The court did not say that it would consider “all the facts that support reasonable

  suspicion”; it said “all the facts”—even those it found would not support reasonable

  suspicion alone. It lived up to its promise. It dedicated an entire section to its totality

  analysis, separate from the factors, as we have here. In that analysis, the court included




                                                  20
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024     Page: 21


  discussion of the 911 call and the SUV along with all the other facts, despite finding the

  former two insufficient to support reasonable suspicion alone.

         The court engaged in the exact process we have approved. It analyzed the relevant

  factors to determine whether, standing alone, they supported reasonable suspicion;

  discounted those factors that were weak based on the record; and finally considered all the

  factors together to analyze as required. That the government was unhappy with the result is

  not enough to transform its substantive distaste into procedural error.

                                              Conclusion

         Because the circumstances confronting Officer Idler did not amount to reasonable

  suspicion, his detention of Daniels was unreasonable under the Fourth Amendment. As

  such, the district court properly granted Daniels’ motion to suppress. We affirm.




                                               21
Appellate Case: 22-1378      Document: 010111045898          Date Filed: 05/08/2024      Page: 22



  22-1378, United States v. Daniels
  EID, J., concurring in the judgment.

         I generally agree with the majority’s opinion, but write separately to express my

  view regarding the degree of suspicion to be assigned to the 911 call. The majority

  thinks that the 911 caller described nothing but innocuous conduct. Maj. Op. at 10

  (reasoning that the caller described three men armed with guns who only acted

  “innocuous[ly]”). I disagree. At the same time, however, I agree with the majority that

  any reasonable suspicion from the call did not attach to Daniels for a simple reason: He

  did not match the caller’s description of the men engaged in suspicious activity.

         To begin, unlike the majority, I would find that the 911 caller described three men

  acting suspiciously. Late at night, at about 11:35 PM, someone called the police

  reporting that three Black men in dark clothing visibly held “guns in their hands” and

  “intermittently t[ook] out [the] guns and then put[] them back into their pockets.” App’x

  Vol. I at 107, 112. The caller stated that the men appeared as if “they [we]re getting

  ready to do something.” Id. at 112. And the caller went on to say that these three men

  repeatedly got “in and out” of a “dark color SUV.” Id. at 107.

         If a police officer were to observe that situation, I would think that the three men’s

  “unusual conduct” would lead the officer “reasonably to conclude in light of his

  experience that criminal activity may be afoot and that the persons with whom he is

  dealing [are] armed and presently dangerous.” Terry v. Ohio, 392 U.S. 1, 30 (1968).

         The majority thinks differently. First, as part of its reasoning, the majority states

  that the 911 call did not establish reasonable suspicion because the officers took the call
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024       Page: 23



  as a “non-emergency area watch request.” Maj. Op. at 17. It is true that the 911 caller

  also stated that the situation described was “currently not an emerg[ency].” App’x Vol. I

  at 112. But surely reasonable suspicion may arise outside of an emergency. What makes

  that clear is that an officer may confirm or dispel suspicion of a crime before it occurs.

  See, e.g., Terry, 392 U.S. at 30 (involving officers who suspected that two men appeared

  to be “casing a job” by walking in front of and peering into a store several times).

  Indeed, crime can still be afoot without an emergency, such as while suspects prepare for

  a crime, whether it be casing a store for a future robbery or putting guns and equipment in

  a car like the 911 caller described. Compare id., with App’x Vol. I at 107, 112

  (describing men in dark clothing getting in and out of an SUV while armed with guns in-

  hand and appearing as if “they [we]re getting ready to do something” close to midnight).

         As the primary reason for finding no suspicious activity from the call, the majority

  places great weight on an assumption that the call “alleged no criminal activity or

  dangerous behaviors.” Maj. Op. at 8 (“[T]he caller only reported that guns were being

  intermittently taken in and out of pockets, and that the three men ‘look like they are

  getting ready to do something.’” (citation omitted)). In reaching its holding, the majority

  relies on the “normative thrust of the Supreme Court’s recent decision in” New York State

  Rifle & Pistol Association, Inc. v. Bruen, 597 U.S. 1 (2022), to reason that the three men

  here were “presumably exercising their Second Amendment rights in a lawful way.”

  Maj. Op. at 8 (emphasis added).

         The problem with the majority’s reasoning is that we do not know for certain,

  under the relevant law or the record, whether the open carry of firearms here was

                                                   2
Appellate Case: 22-1378     Document: 010111045898         Date Filed: 05/08/2024        Page: 24



  “lawful” or not. Id. Colorado leaves the regulation over the open carry of firearms to its

  local and municipal authorities. See Colo. Rev. Stat. Ann. § 29-11.7-104. Looking to the

  relevant locality here, the City of Aurora leaves the lawfulness of open carried firearms

  up to public and private property owners.1 With that in mind, the law here does not

  necessarily clarify whether the three men described in the 911 call could carry openly

  because we do not know if the apartment parking lot had any restrictions on open carry of

  a firearm. And the record does not help us out either in that regard.

         This is not a case where we know that individuals merely “exercise[ed] their

  Second Amendment rights in a lawful way.” Contra Maj. Op. at 8. Or at least, nothing

  from the law or record indicates that is the case. Even so, based on nothing more than

  speculation, the majority holds that the men “presumably” open carried guns lawfully.

  Id. (emphasis added).

         I would not presume so. I acknowledge that the Supreme Court has said that

  “bare-boned tips about guns” do not create “an automatic firearm exception” to the

  Fourth Amendment. Florida v. J.L., 529 U.S. 266, 273 (2000). But the caller here did

  not just report that the men had guns. There was more: Again, three men dressed in dark

  clothing, actively moved in and out of cars in a parking lot close to midnight, were



         1
           See Aurora Stat. art. IV, div. 2, § 94-152(a) (providing that “[i]t shall be
  unlawful for any person, carrying a firearm, to enter or remain upon any private
  property of another or any building or property of a commercial establishment when
  such property, building, or establishment is posted with notification that the carrying
  of firearms is prohibited”); id. § 94-154(a) (providing that “[t]he carrying of firearms
  in or upon public facilities is unlawful when said facilities are posted with
  notification that the carrying of firearms is prohibited”).
                                                  3
Appellate Case: 22-1378     Document: 010111045898          Date Filed: 05/08/2024       Page: 25



  visibly armed with weapons, and appeared as if “they [we]re getting ready to do

  something.” App’x Vol. I at 107, 112. That I would find amounts to a tip “that criminal

  activity may be afoot.” Terry, 392 U.S. at 30.

         In any case, however, the suspicious activity described on the call does not end

  this matter. The officers here did not view the situation described on the 911 call with

  their own eyes. Instead, the officers received a tip that needed to be corroborated.

  Importantly, “[a] police officer cannot legally detain a person simply because criminal

  activity is afoot.” United States v. Fisher, 597 F.3d 1156, 1158 (10th Cir. 2010). Instead,

  an officer must “suspect[]” that “the particular person stopped” has committed or was

  committing “criminal activity.” Id. at 1158–59.

         With that in mind, something needed to connect Daniels as one of the men

  described in the 911 call. Nothing did. Critically, the government concedes that “Officer

  Idler didn’t notice anyone in the area matching the clothing descriptions provided by the

  911 caller.” Aplt. Br. at 3. And indeed, the record reflects that no officer could

  reasonably expect Daniels to be one of the men in dark clothing described on the call.

  Daniels was not wearing a black hoodie. He instead wore a bright orange jumpsuit with a

  reflective strip across the front. The 911 call also mentioned that the three men went in

  and out of a dark colored SUV. Daniels did no such thing. Instead, he stood

  “approximately five to ten feet away” from an SUV, “outside his own home.” App’x

  Vol. I at 107, 121. And lastly, the 911 caller described that the men visibly held “guns in

  their hands and pockets.” Id. at 112. Yet again, Daniels did no such thing. At no time



                                                   4
Appellate Case: 22-1378      Document: 010111045898         Date Filed: 05/08/2024        Page: 26



  did Officer Idler see Daniels with a firearm in hand or on his person, even after the

  seizure.

  As such, I agree with the majority that Daniels did not match the caller’s description. See

  Maj. Op. at 9–10.

         In sum, unlike the majority, I believe that the 911 call reported suspicious activity.

  That disagreement aside, I agree with the majority that Daniels did not match the caller’s

  description of the three men acting suspiciously. Any suspicion stemming from the call

  was dispelled when Officer Idler found no one on the scene that matched the caller’s

  description. For these reasons, I concur in the judgment.




                                                   5

```

---

## GROUP: content/cases/United States v. Hanapel.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Hanapel
type: case
citation: "112 F.4th 539 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir. 2024
court_level: coa
circuit: ca8
year: 2024
date_decided: 2024-08-12
docket: 23-2653
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10038262/united-states-v-james-hanapel/"
  cluster_id: 10038262
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Hanapel
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entrapment]]"
    role: Key
related:
  - "[[Entrapment]]"
  - "[[Jacobson v. United States]]"
  - "[[Mathews v. United States]]"
  - "[[Sherman v. United States]]"
tags:
  - case
  - entrapment
  - predisposition
  - inducement
  - undercover-sting
  - eighth-circuit
holding: "The Eighth Circuit affirmed the denial of judgment of acquittal, holding that Hanapel failed to establish entrapment as a matter of law: there was no government inducement as a matter of law, and his initial hesitation on learning the decoy's age did not negate the predisposition a reasonable jury could find from his ready pursuit of the opportunity — arriving at the meeting place with condoms within hours."
---

# United States v. Hanapel

*112 F.4th 539 (8th Cir. 2024)* (No. 23-2653) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 10038262 → opinion 10504863 (112 F.4th 539, decided 2024-08-12); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
During the 2021 Sturgis Motorcycle Rally, a Homeland Security agent posed on the SKOUT social app as "Journey," a fictitious fourteen-year-old. James Hanapel, messaging as a twenty-one-year-old "Max Taylor," asked to "hang out." When Journey said she was fourteen, Hanapel first replied "I can't talk to you" and that they could "be friends but nothing more." After Journey said guys her age were "lame" and that she "met people" on the app "all the time," Hanapel steered the exchange to sex, proposed that they "hook up," agreed to meet at a local middle school that night, and said he would bring condoms. He was arrested at the school with a newly purchased package of condoms and admitted he had traveled to have sex with the girl. A jury convicted him of attempted enticement of a minor, 18 U.S.C. § 2422(b); the district court denied his motion for judgment of acquittal based on entrapment and imposed the 120-month statutory minimum.

## Issue
Whether Hanapel established entrapment as a matter of law — both government inducement and his own lack of predisposition — so that the district court erred in denying his motion for judgment of acquittal, or whether a reasonable jury could reject the entrapment defense.

## Rule
The [[Common Legal Terms#affirmative-defense|affirmative defense]] of entrapment has two elements — "government inducement of the crime, and a lack of predisposition on the part of the defendant to engage in the criminal conduct." The government may use "artifice, stratagem, and undercover agents" and may furnish a willing person the opportunity to offend; it may not implant criminal design in an unwilling person. To overturn a conviction as a matter of law the defendant must establish **both** inducement and non-predisposition, and a ready response to minimal inducement itself indicates predisposition. Applying that standard, the court held that a defendant's early reluctance does not, by itself, negate predisposition: "Initial hesitance to engage in criminal conduct does not establish lack of predisposition as a matter of law." — 112 F.4th 539, slip op. at 8. ^pin-op8

## Application
Neither element was established as a matter of law. On inducement, the government did not initiate contact — Hanapel proposed the meeting and was first to raise "hook[ing] up" and sex — and neither Journey's unsolicited sports-bra photo (far more revealing images have been held insufficient) nor her mildly "precocious" persona compelled a finding of inducement; the court concluded there was no inducement as a matter of law. On predisposition, Hanapel's initial "friends but nothing more" response to Journey's age did not negate predisposition: once she signaled interest, he promptly discussed sexual acts and, within four hours of learning she was a minor, arrived at the meeting place with condoms — evidence from which a reasonable jury could find him predisposed.

## Conclusion
**Affirmed.** Chief Judge Colloton wrote for the panel (Colloton, C.J.; Erickson and Kobes, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hanapel* is a clean recent application of the federal **subjective** entrapment test: the controlling fact is **predisposition**, not the fact of inducement, so a sting that merely furnishes the opportunity — and a defendant's momentary hesitation before seizing it — leaves the jury's rejection of the defense intact.

## Appears on
- [[Entrapment]] — *Key*

## Sources
- [*United States v. Hanapel*, 112 F.4th 539 (8th Cir. 2024)](https://www.courtlistener.com/opinion/10038262/united-states-v-james-hanapel/) — pinpoint: slip op. at 8 (predisposition / no-inducement-as-a-matter-of-law holding; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e4100f5a5e397b87", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "112 F.4th 539 (2024)", "court": "8th Cir. 2024", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Hanapel", "year": "2024"}}
{"assertion_id": "760e34c51a4a241a", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key", "title": "United States v. Hanapel"}}
{"assertion_id": "8426f3c38021fb30", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Eighth Circuit affirmed the denial of judgment of acquittal, holding that Hanapel failed to establish entrapment as a matter of law: there was no government inducement as a matter of law, and his initial hesitation on learning the decoy's age did not negate the predisposition a reasonable jury could find from his ready pursuit of the opportunity — arriving at the meeting place with condoms within hours.", "title": "United States v. Hanapel"}}
{"assertion_id": "96f7af043b27a706", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Hanapel", "varies_by_point": "false"}}
{"assertion_id": "ef4ecb1e9d12f528", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 8th Cir.", "title": "United States v. Hanapel"}}
```

### lake record — United States v. Hanapel

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hanapel",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. James Hanapel",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Hanapel",
    "court": "8th Cir. 2024",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2024-08-12",
    "year": 2024,
    "docket": "23-2653",
    "cluster_id": 10038262,
    "lead_opinion_id": 10504863,
    "sibling_ids": [],
    "absolute_url": "/opinion/10038262/united-states-v-james-hanapel/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "112 F.4th 539",
      "volume": "112",
      "reporter": "F.4th",
      "page": "539",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "112 F.4th 539",
        "volume": "112",
        "reporter": "F.4th",
        "page": "539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "112 F.4th 539",
    "official_selection": {
      "court_class": "state",
      "selected": "112 F.4th 539",
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
    "date_created": "2026-07-06T05:53:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hanapel--10038262",
      "to_record_id": "United States v. Hanapel",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hanapel

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 23-2653
                        ___________________________

                             United States of America,

                        lllllllllllllllllllllPlaintiff - Appellee,

                                           v.

                               James Dean Hanapel,

                      lllllllllllllllllllllDefendant - Appellant.
                                       ____________

                    Appeal from United States District Court
                    for the District of South Dakota - Western
                                   ____________

                            Submitted: March 15, 2024
                              Filed: August 12, 2024
                                  ____________

Before COLLOTON, Chief Judge, ERICKSON and KOBES, Circuit Judges.
                            ____________

COLLOTON, Chief Judge.

      A jury found James Hanapel guilty of attempting to entice a minor to engage
in sexual activity. See 18 U.S.C. § 2422(b). The charge arose from Hanapel’s
dialogue with an undercover officer who posed as a fourteen-year-old girl. At trial,
Hanapel raised the affirmative defense of entrapment. At the close of the
government’s case, he moved for judgment of acquittal on the ground that he was
entrapped as a matter of law. The district court* denied the motion, and we affirm.

                                          I.

      In August 2021, several law enforcement agencies participated in an operation
to combat child exploitation on the internet during the Sturgis Motorcycle Rally in
South Dakota. As part of the operation, a special agent from the Department of
Homeland Security posed as “Journey,” a fictitious fourteen-year-old girl whose
parents were attending the rally.

       The agent created an account for Journey on SKOUT, an internet application
that is used for dating and social networking. On Journey’s public profile, he
represented that she was eighteen years old because SKOUT required users to be no
younger. He also included two photographs of “Journey” that were actually pictures
of an adult woman associated with law enforcement.

      On August 10, 2021, Hanapel sent a message to Journey from an account
purporting to belong to “Max Taylor.” According to the profile, Max Taylor was a
twenty-one-year-old man located in Box Elder, South Dakota. Hanapel asked
whether Journey wanted to “hang out.” The next day, Journey said “[m]aybe” and
provided a telephone number.

       On August 12, Hanapel and Journey began to communicate via text message.
Hanapel asked whether Journey “[w]ant[ed] some company.” Journey said that she
did, but she “want[ed] to tell” Hanapel that she was “not 18” and was “just here trying



      *
       The Honorable Jeffrey L. Viken, United States District Judge for the District
of South Dakota, now retired.

                                         -2-
to have fun while my parents are at the rally.” Hanapel asked, “How old are you ??”
At 3:40 p.m., Journey replied, “14 but turn 15 in a couple months.”

        Less than one minute later, Hanapel responded, “Yoo I can’t talk to you.” He
added that they could “be friends but nothing more.” Journey wrote back: “ok.
sorry. i understand. guys my age are pretty lame and you seemed pretty cool. i
didn’t mean to upset you sorry. you were just so cute.” Hanapel reassured her that
“[i]t’s okay you seem cool I just don’t want trouble if you wanna hangout and grab
ice cream or catch a movie that’s cool but I’d have to meet your parents[.] Because
if they got the wrong impression I’m going to jail.”

      Journey said that she was “not here to get anyone in trouble,” and had “met
people” on SKOUT “all the time.” Hanapel replied, “Oh okay well do you wanna go
do something.” Journey asked what he had in mind. Hanapel suggested that they
could “grab food or watch a movie,” and asked what Journey had “done with people
before.” Journey answered, “a lot....lol [laugh out loud].” Hanapel asked what she
meant, and Journey told him to “just use your imagination hehehehe.”

       Hanapel again asked if Journey “want[ed] some company.” She said that it
“depends on what you have in mind,” because “this is my last night home by myself
so i have to be careful on who i choose to hang with so i can make the most of it.”
Hanapel told her it was “really up to” her whether they met and what they would do.
Journey said she “like[s] someone who knows what they want.”

      Hanapel asked, “Honestly you tryna hook up ?” Journey replied, “up to you
maxie.” He asked why he was “making all the decisions”; Journey said that he was
“older and more experienced.” Hanapel asked for Journey’s address. She said, “what
are you thinking maxxie? look at you trying to be my pick.”




                                        -3-
       Journey then sent a photograph of herself and asked whether Hanapel liked her
outfit. In the photo, Journey appears to be holding the camera above her head. She
is looking up at the camera, and wearing a sports bra and leggings. Special Agent
Berger testified that he sent this photo because he considered it “nonsexual in nature.”
He testified that the clothing was “consistent with what the temperature was like
outside” in mid-August. Hanapel replied that the photo was “[s]exy,” and said, “I’m
thinking I come over we watch a movie make out and see what happens from there.”
Journey asked what he “had in mind” because she “may surprise” him. He suggested
they “could hook up.”

       The conversation pivoted to Journey’s experiences with other people whom she
met on SKOUT. Hanapel asked her how many people she had met, how old they
were, and what they did together. Journey answered that she met “a few” people who
were older than “Max,” and that they did “fun stuff hehehehe.” Hanapel asked
“[w]hat kind of fun stuff,” and Journey replied, “didnt i tell you to use your
imagination. im willing to try whatever. you just name it.” Hanapel suggested
“[s]ex,” and asked if she “want[ed] to fuck.” Journey asked, “do you?” Hanapel
answered, “Yes I’m down.” Journey asked whether there was anything that Hanapel
“want[ed] to try.” He said, “Yeah anal if you[’re] down.”

       The two agreed to meet at a local middle school that night. Hanapel agreed to
bring condoms. He drove to the school and was arrested at approximately 7:30 p.m.
on August 12. Police found a newly purchased package of condoms in his car. In a
post-arrest interview, Hanapel admitted that he traveled to the school to have sex with
the girl.

       A grand jury charged Hanapel with attempted enticement of a minor to engage
in unlawful sexual activity. See 18 U.S.C. § 2422(b). At trial, the district court gave
the jury the following instruction:



                                          -4-
      One of the issues in this case is whether Mr. Hanapel was entrapped.
      The government has the burden of proving beyond a reasonable doubt
      that Mr. Hanapel was not entrapped by showing either: (1) Mr. Hanapel
      was willing to solicit a minor before he was approached or contacted by
      law enforcement agents; or (2) the government, or someone acting for
      the government, did not persuade or talk Mr. Hanapel into soliciting a
      minor. In deciding whether Mr. Hanapel was willing to solicit a minor
      before he was approached or contacted by law enforcement agents, you
      may consider whether the defendant enthusiastically responded and
      promptly availed himself of his first opportunity to commit a crime
      without government prodding. If the government proves either of these
      beyond a reasonable doubt, you must reject Mr. Hanapel’s claim of
      entrapment. If the government fails to prove at least one of these
      beyond a reasonable doubt, then you must find Mr. Hanapel not guilty.

      The law allows the government to use undercover agents, deception, and
      other methods to present a person already willing to commit a crime
      with the opportunity to commit a crime, but the law does not allow the
      government to persuade an unwilling person to commit a crime. Simply
      giving someone a favorable opportunity to commit a crime is not the
      same as persuading him.

       While the jury deliberated, Hanapel moved for judgment of acquittal. He
argued that the evidence showed that he was entrapped as a matter of law. The
district court denied the motion. The jury returned a guilty verdict, and the district
court sentenced Hanapel to the statutory minimum term of 120 months’
imprisonment. Hanapel appeals and renews his contention that he was entrapped as
a matter of law. Viewing the evidence in the light most favorable to the verdict, we
consider whether any reasonable jury could have rejected the entrapment defense.
See United States v. Neri, 89 F.4th 668, 670 (8th Cir. 2023).




                                         -5-
                                         II.

      It is “well settled that the government may use artifice, stratagem, and
undercover agents in its pursuit of criminals.” United States v. Myers, 575 F.3d 801,
806 (8th Cir. 2009). The government may not “originate a criminal design, implant
in an innocent person’s mind the disposition to commit a criminal act, and then
induce commission of the crime.” Jacobson v. United States, 503 U.S. 540, 548
(1992). The affirmative defense of entrapment “guards against such overzealous
prosecutions.” United States v. Lasley, 79 F.4th 979, 983 (8th Cir. 2023).

       An entrapment defense has two elements: “government inducement of the
crime, and a lack of predisposition on the part of the defendant to engage in the
criminal conduct.” Mathews v. United States, 485 U.S. 58, 63 (1988). The
inducement and predisposition “inquiries are often closely linked, because the need
for greater inducement may suggest that the defendant was not predisposed to commit
the crime; and conversely, a ready response to minimal inducement indicates criminal
predisposition.” Myers, 575 F.3d at 805. A defendant is entitled to a jury instruction
on entrapment if prior to trial he produces sufficient evidence of inducement. United
States v. Young, 613 F.3d 735, 746 (8th Cir. 2010). If he makes a showing of
inducement, the burden at trial shifts to the government to prove predisposition
beyond a reasonable doubt. Id. at 747.

      The district court concluded that Hanapel produced sufficient evidence to
warrant a jury instruction on entrapment. But the jury found beyond a reasonable
doubt that he was not entrapped. To prevail on appeal, Hanapel must establish as a
matter of law both that he was induced and that he was not predisposed to commit the
offense. See Myers, 575 F.3d at 805-06 & n.4; United States v. Hinton, 908 F.2d 355,
357 (8th Cir. 1990).




                                         -6-
       We begin with inducement. Four factors are relevant: (1) whether the
government initiated the contact with the defendant; (2) whether the government
introduced the topics of meeting and sex; (3) the effect of the photos sent by the
government; and (4) the degree to which the government influenced the behavior of
the defendant by portraying the minor as sexually precocious. United States v. Tobar,
985 F.3d 591, 593 (8th Cir. 2021); Myers, 575 F.3d at 806.

      The government did not initiate contact with Hanapel. Hanapel first proposed
a meeting with the minor, and he was the first to mention that they could “hook up”
and engage in “[s]ex.” Hanapel argues that the government introduced the topic of
sex when Journey told Hanapel that she wanted to “make the most” of her time at
home alone. While Journey’s response may have been suggestive, she did not
pressure Hanapel to engage in sexual activity or propose sexual activity directly.
Hanapel interpreted her message to refer to sexual activity, and he then explicitly
suggested engaging in such conduct.

       Hanapel’s primary argument is that he was induced as a matter of law when
Journey sent him an unsolicited photo of herself in a sports bra. He argues that the
government sent the “suggestive” photo because he was hesitant to meet Journey. We
are not convinced that the photo establishes inducement as a matter of law. Hanapel
argues summarily that the photo “speak[s] for itself,” but it does not say much about
entrapment. Hanapel described Journey as “fully clothed” when he described the
photo to police. Far more revealing images have been held insufficient to constitute
inducement as a matter of law. See United States v. Shinn, 681 F.3d 924, 928-30 (8th
Cir. 2012); Myers, 575 F.3d at 803, 806. The evidence also does not compel a
conclusion that the government sent the photo in response to Hanapel’s reluctance.
Journey sent the photo in direct response to his message asking for her address. By
that time, Hanapel already had asked whether she was “tryna hook up.” A reasonable
jury could reject Hanapel’s contention that the government’s use of the photo
demonstrated impermissible inducement.

                                         -7-
       Nor are we convinced that adding Journey’s supposedly “precocious” conduct
to the photograph amounts to inducement as a matter of law. While Journey implied
that she previously had engaged in sexual activity, she also downplayed her sexual
history in a message to Hanapel: “trust me im not that experienced.” To the extent
that Journey’s “photos and behavior portray her as sexually precocious, it is only to
a minor degree.” Tobar, 985 F.3d at 593. There was no inducement as a matter of
law.

      As for predisposition, we conclude that the evidence was sufficient for a
reasonable jury to reject Hanapel’s defense. A defendant is predisposed if he readily
responds to a government agent’s offer of opportunity to commit a crime. Jacobson,
503 U.S. at 549-50; Myers, 575 F.3d at 807-08. Hanapel argues that he was not
predisposed because when Journey first shared her age, he told her that they could “be
friends but nothing more.”

       Initial hesitance to engage in criminal conduct does not establish lack of
predisposition as a matter of law. In United States v. Zupnik, 989 F.3d 649 (8th Cir.
2021), the defendant also balked at first and told the minor, “I am kinda waaayyy too
old for you !” Id. at 652. But when the minor said that she was “just tired of boys,”
the defendant “proceeded to exchange sexually explicit messages with her and plan
to meet her in person to engage in sexual acts.” Id. at 652, 655-56. This court
concluded that the exchange included “more than sufficient evidence” of the
defendant’s predisposition. Id. at 656.

       Other than his initial reaction to Journey’s age, Hanapel showed no hesitation
or resistance to meet and engage in sexual conduct. Once Journey told him that “guys
my age are pretty lame,” and that she “met people on” SKOUT “all the time,”
Hanapel began to discuss sexual activity. Within four hours after Journey revealed
that she was a minor, Hanapel was at their agreed-upon meeting place with newly



                                         -8-
purchased condoms. Based on this conduct, a reasonable jury could conclude that
Hanapel was predisposed to commit the offense.

      The judgment of the district court is affirmed.
                     ______________________________




                                      -9-

```

---

## GROUP: content/cases/United States v. Hay.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Hay
type: case
citation: "95 F.4th 1304 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 10th Cir. 2024
court_level: coa
circuit: ca10
year: 2024
date_decided: 2024-03-19
docket: 22-3276
authority_weight: "Binding in-circuit — 10th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/9485331/united-states-v-hay/"
  cluster_id: 9485331
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Hay
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (pole cameras)"
related:
  - "[[Third-Party Doctrine & CSLI]]"
  - "[[Carpenter v. United States]]"
  - "[[Kyllo v. United States]]"
  - "[[United States v. Knotts]]"
tags:
  - case
  - fourth-amendment
  - search
  - digital-privacy
  - pole-camera
  - video-surveillance
  - carpenter
  - tenth-circuit
holding: "The Tenth Circuit affirmed, holding that a fixed pole camera trained on the exterior of Hay's home — recording roughly fifteen hours a day for sixty-eight days but capturing only what was visible to passersby in public view — was not a Fourth Amendment search under the circuit's Jackson rule, and that Carpenter's mosaic theory of the 'whole of physical movements' does not disturb that rule for conventional, single-location camera surveillance of a home's exterior."
---

# United States v. Hay

*95 F.4th 1304 (10th Cir. 2024)* (No. 22-3276) · U.S. Court of Appeals for the Tenth Circuit · **Binding in-circuit — 10th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 9485331 → opinion 9951944 (95 F.4th 1304, decided 2024-03-19); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Bruce Hay, an Army veteran, was found permanently disabled by the Department of Veterans Affairs in 2006 and drew lifetime benefits. After an anonymous tip that he was faking, VA investigators surveilled him — tailing him, feigning a deer-poaching operation to watch him up close, and installing a motion-activated **pole camera** on a school rooftop across the street from his home. The camera recorded near-constant footage of his house as visible from the street — about fifteen hours a day for sixty-eight days. A Kansas jury convicted Hay of ten counts of stealing government property (18 U.S.C. § 641) and six counts of wire fraud (§ 1343). Hay moved for acquittal or a new trial, arguing among other things that the warrantless, months-long pole-camera surveillance violated the Fourth Amendment.

## Issue
Whether the government's warrantless installation of a fixed pole camera that recorded the exterior of Hay's home — continuously for sixty-eight days — was a Fourth Amendment search, in particular whether *[[Carpenter v. United States]]* extends its "whole of physical movements" mosaic theory to prolonged video surveillance of a residence visible to the public.

## Rule
Under the circuit's rule, camera surveillance capturing only what is exposed to public view is not a search: viewing settings in public view, or visible via generally available technology, does not constitute a search, while viewing private settings perceptible only through technology not in general public use does. Because the pole camera "could not capture footage of any activity that was not in public view, it did not violate the Fourth Amendment," and the extended duration did not change that logic. *[[Carpenter v. United States|Carpenter]]*'s narrow mosaic holding about historical cell-site data does not reach fixed camera surveillance of a home's exterior: "Our holding in *Jackson* that pole cameras trained on a house do not violate the Fourth Amendment remains binding law, and *Carpenter*, without more, does not disturb it." — 95 F.4th 1304, slip op. at 18. ^pin-op18

## Application
Hay's argument that sixty-eight days of continuous recording "painted an intimate portrait" of his life, cataloguing his habits and visitors, was "precluded by *Jackson*" — the length of the surveillance did not change the basic logic that camera surveillance of a home visible to passersby is not a search. *[[Carpenter v. United States|Carpenter]]* did not alter the equation: the Supreme Court called that decision "a narrow one" that did not call into question conventional surveillance techniques and tools such as security cameras. A pole camera fixed across the street came nowhere close to capturing the whole of Hay's physical movements — it saw only one location's exterior, and the moment Hay left home the camera could not track him. The court noted that no circuit had held extended exterior video surveillance of a house to be a search under *[[Carpenter v. United States|Carpenter]]*.

## Conclusion
**Affirmed.** Judge Tymkovich wrote for the panel (Tymkovich, Murphy, and Carson, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hay* is a leading data point on the **unsettled pole-camera question**: the Tenth Circuit (like the Fifth, Sixth, and Seventh) declines to extend *[[Carpenter v. United States|Carpenter]]*'s mosaic theory to fixed exterior camera surveillance of a home, while a First Circuit [[Reading and Citing Cases#en-banc|en banc]] court deadlocked and the Fourth Circuit found aerial city-wide tracking a search. Teach it as circuit-split / unsettled authority — never as a settled nationwide rule that pole cameras are categorically permissible.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (pole cameras)*

## Sources
- [*United States v. Hay*, 95 F.4th 1304 (10th Cir. 2024)](https://www.courtlistener.com/opinion/9485331/united-states-v-hay/) — pinpoint: slip op. at 18 (the *Jackson*-binding / *Carpenter*-does-not-disturb holding; the CL opinion text carries the court's internal slip pagination, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "20579f606b95c527", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "95 F.4th 1304 (2024)", "court": "10th Cir. 2024", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Hay", "year": "2024"}}
{"assertion_id": "37ce19fd16492560", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Tenth Circuit affirmed, holding that a fixed pole camera trained on the exterior of Hay's home — recording roughly fifteen hours a day for sixty-eight days but capturing only what was visible to passersby in public view — was not a Fourth Amendment search under the circuit's Jackson rule, and that Carpenter's mosaic theory of the 'whole of physical movements' does not disturb that rule for conventional, single-location camera surveillance of a home's exterior.", "title": "United States v. Hay"}}
{"assertion_id": "de3718238561a1a1", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Lower-court development (pole cameras)", "title": "United States v. Hay"}}
{"assertion_id": "04393e85bf51e6bb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Hay", "varies_by_point": "false"}}
{"assertion_id": "77d47b1075b23c2e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 10th Cir.", "title": "United States v. Hay"}}
```

### lake record — United States v. Hay

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hay",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Hay",
    "case_name_short": "Hay",
    "case_name_full": "",
    "input_case_name": "United States v. Hay",
    "court": "10th Cir. 2024",
    "court_id": "ca10",
    "court_level": "coa",
    "circuit": "ca10",
    "state": null,
    "date_decided": "2024-03-19",
    "year": 2024,
    "docket": "22-3276",
    "cluster_id": 9485331,
    "lead_opinion_id": 9951944,
    "sibling_ids": [],
    "absolute_url": "/opinion/9485331/united-states-v-hay/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "95 F.4th 1304",
      "volume": "95",
      "reporter": "F.4th",
      "page": "1304",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "95 F.4th 1304",
        "volume": "95",
        "reporter": "F.4th",
        "page": "1304",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "95 F.4th 1304",
    "official_selection": {
      "court_class": "state",
      "selected": "95 F.4th 1304",
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
    "date_created": "2026-07-06T05:53:33Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:53:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hay--9485331",
      "to_record_id": "United States v. Hay",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hay

```
Appellate Case: 22-3276         Document: 010111018128    Date Filed: 03/19/2024    Page: 1
                                                                                    FILED
                                                                        United States Court of Appeals
                                                PUBLISH                         Tenth Circuit

                           UNITED STATES COURT OF APPEALS                     March 19, 2024

                                                                           Christopher M. Wolpert
                                 FOR THE TENTH CIRCUIT                         Clerk of Court
                             _________________________________

  UNITED STATES OF AMERICA,

         Plaintiff - Appellee,

  v.                                                           No. 22-3276

  BRUCE L. HAY,

         Defendant - Appellant.

  ----------------------------------------------------

  REPORTERS COMMITTEE FOR
  FREEDOM OF THE PRESS; FIRST
  AMENDMENT COALITION; FREEDOM
  OF THE PRESS FOUNDATION; THE
  MEDIA INSTITUTE; NATIONAL PRESS
  PHOTOGRAPHERS ASSOCIATION;
  THE NEWS LEADERS ASSOCIATON;
  NEWS/MEDIA ALLIANCE; RADIO
  TELEVISION DIGITAL NEWS
  ASSOCIATION; SOCIETY OF
  ENVIRONMENTAL JOURNALISTS,

          Amici Curiae.
                             _________________________________

                         Appeal from the United States District Court
                                  for the District of Kansas
                              (D.C. No. 2:19-CR-20044-JAR-1)
                           _________________________________

 Rachel Tennell, Debevoise & Plimpton LLP, New York, New York (Benjamin Leb and
 Anagha Sundararajan, Debevoise & Plimpton LLP, New York, New York; David A.
 O’Neil, Debevoise & Plimpton LLP, Washington, D.C.; and Melody Brandon, Federal
 Public Defender, and Paige A. Nichols, Assistant Federal Public Defender, Kansas
Appellate Case: 22-3276    Document: 010111018128         Date Filed: 03/19/2024    Page: 2



 Federal Public Defender’s Office, Topeka, Kansas, with her on the briefs) for Defendant-
 Appellant.

 Kevin J. Barber, United States Department of Justice, Criminal Division, Appellate
 Section, Washington, D.C. (Nicole M. Argentieri, Acting Assistant Attorney General,
 and Lisa H. Miller, Deputy Assistant Attorney General, United States Department of
 Justice, Criminal Division, Appellate Section, Washington, D.C.; and Kate E. Brubacher,
 United States Attorney, District of Kansas, and James A. Brown, Assistant United States
 Attorney, Appellate Chief, District of Kansas, Topeka, Kansas, with him on the brief) for
 Plaintiff-Appellee.

 Brett Max Kaufman, American Civil Liberties Union Foundation, New York, New York;
 Sharon Brett, American Civil Liberties Union of Kansas, Overland Park, Kansas; Tim
 Macdonald, American Civil Liberties Union of Colorado, Denver, Colorado; and Tom
 McBrien, Electronic Privacy Information Center, Washington, D.C., filed an Amicus
 Curiae Brief of American Civil Liberties Union, American Civil Liberties Union of
 Kansas, American Civil Liberties Union of Colorado, Brennan Center for Justice, Center
 for Democracy & Technology, and Electronic Privacy Information Center in Support of
 Defendant-Appellant.

 Katie Townsend, Counsel of Record for Amici Curiae, and Gabe Rottman, Grayson
 Clary, and Emily Hockett, Reporters Committee for Freedom of the Press, Washington,
 D.C., filed an Amicus Curiae Brief of The Reporters Committee for Freedom of the Press
 and 8 Media Organizations in Support of Defendant-Appellant.
                        _________________________________

 Before TYMKOVICH, MURPHY, and CARSON, Circuit Judges.
                  _________________________________

 TYMKOVICH, Circuit Judge.
                 _________________________________

       Does the Fourth Amendment permit the government to surveil a home for

 months on end without a warrant? This case requires us to decide.

       The Department of Veterans Affairs (VA) offers lifetime benefits to

 permanently disabled veterans. A Kansas jury convicted Bruce Hay of ten counts of

 stealing government property and six counts of wire fraud as part of a scheme to



                                             2
Appellate Case: 22-3276     Document: 010111018128         Date Filed: 03/19/2024        Page: 3



 defraud the VA by exaggerating his disability. As part of its investigation, VA

 agents installed a pole camera across the street from his house to film his activities.

        Mr. Hay appeals his conviction. He contends that (1) the evidence presented

 at trial is insufficient to support a conviction, (2) the VA’s installation of a pole

 camera violated his Fourth Amendment rights, and (3) the district judge wrongfully

 admitted evidence to the extent that it deprived him of a fair trial.

        We affirm the district court.

                                     I. Background

        Bruce Hay is a U.S. Army veteran. In 2005, while at home in Kansas, he was

 involved in a serious car accident. Doctors diagnosed him with “functional

 neurological disorder,” or FND, a psychological disorder that impaired his mobility.

 Following this diagnosis, Mr. Hay applied for disability benefits from the VA. In

 2006, the VA determined that Mr. Hay was permanently disabled and therefore

 entitled to benefits.

        Six years later, the VA Inspector General’s office received an anonymous tip

 alleging that Mr. Hay was not, in fact, permanently disabled. It initiated an

 investigation into Mr. Hay’s disability status. Mr. Hay lived in Osawatomie, a small

 town in eastern Kansas. To investigate Mr. Hay’s mobility, officers feigned an

 operation involving deer poaching on a nearby farm so that they could monitor Mr.

 Hay from a closer distance. They also tailed him to medical appointments and other

 events. For a more robust record of his daily activities, they installed a pole camera

 on a school rooftop across the street from Mr. Hay’s house. The camera was remote-
                                              3
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 4



 controlled and activated by motion, and it recorded near constant footage of Mr.

 Hay’s house as visible from across the street. All told, the camera captured 15 hours

 of footage per day for 68 days.

       Over the course of a six-year investigation, the VA finally developed enough

 evidence to suggest that Mr. Hay was faking his disability and that he was not

 entitled to disability benefits. Subsequently, a grand jury indicted Mr. Hay on ten

 counts of stealing government property in violation of 18 U.S.C. § 641 and six counts

 of wire fraud in violation of 18 U.S.C. § 1343. A jury found Mr. Hay guilty of all

 counts.

                                     II. Analysis

       Mr. Hay argues that he was entitled to a judgment of acquittal or a new trial

 for three reasons: (1) the evidence presented at trial was insufficient to support a

 conviction for stealing government property or for wire fraud; (2) the district court

 admitted pole camera footage that was obtained in violation of the Fourth

 Amendment; and (3) the district court admitted other incriminating evidence and

 testimony in violation of the Federal Rules of Evidence.

       A. Sufficiency of the evidence

              1. Stealing government property

       Mr. Hay first contends his conviction should be vacated because the

 government did not supply sufficient evidence to prove that he stole government

 property. In reviewing motions for a judgment of acquittal, we must consider

 whether “viewing the evidence in the light most favorable to the Government, any
                                            4
Appellate Case: 22-3276      Document: 010111018128         Date Filed: 03/19/2024    Page: 5



 rational trier of fact could have found the defendant guilty of the crime beyond a

 reasonable doubt.” United States v. Delgado-Uribe, 363 F.3d 1077, 1081 (10th Cir.

 2004).

          Mr. Hay was charged with fraudulently taking government property under

 18 U.S.C. § 641. That statute makes it a crime to take government property in four

 different ways. It applies to:

                Whoever [1] embezzles, [2] steals, [3] purloins, or
                [4] knowingly converts to his use or the use of another, or
                without authority, sells, conveys or disposes of any record,
                voucher, money, or thing of value of the United States or of
                any department or agency thereof, or any property made or
                being made under contract for the United States or any
                department or agency thereof.

 18 U.S.C. § 641 (brackets added).

          Mr. Hay argues that because his scheme involved fraud and deception, but not

 theft, the statute does not cover his misconduct. The question, then, is whether

 “steal[ing],” as used in the statute, encompasses acts of fraud and deception. It does.

          The term “‘steal’ may denote the criminal taking of personal property either by

 larceny, embezzlement, or false pretenses.” United States v. Turley, 352 U.S. 407, 412

 (1957) (citing Black’s Law Dictionary (4th ed. 1951)) (emphasis added). See also Steal,

 Black’s Law Dictionary (3d ed. 1933) (defining “steal” as “the criminal taking of

 personal property by larceny, embezzlement, or false pretenses.”). Accordingly, circuit

 courts have consistently affirmed convictions under 18 U.S.C. § 641 for submitting

 fraudulent paperwork to the government in order to obtain money. See United States v.

 Ransom, 642 F.3d 1285, 1289-1290 (10th Cir. 2011) (affirming conviction under

                                               5
Appellate Case: 22-3276      Document: 010111018128          Date Filed: 03/19/2024      Page: 6



 18 U.S.C. § 641 for falsification of government timesheets); United States v. Rivera-

 Ortiz, 14 F.4th 91, 101 (1st Cir. 2021) (affirming conviction under 18 U.S.C. § 641 for

 misrepresenting the defendant’s occupation on a social security disability insurance

 application); United States v. Oliver, 238 F.3d 471, 472-473 (3d Cir. 2001) (similar); and

 United States v. Dowl, 619 F.3d 494, 501-502 (5th Cir. 2010) (affirming conviction under

 18 U.S.C. § 641 for falsifying loan applications). Mr. Hay feigned a permanent disability

 to access government benefits. That qualifies as “stealing” under 18 U.S.C. § 641.

        Mr. Hay resists this conclusion, arguing that “none of the offenses enumerated in

 the statute—embezzlement, theft, conversion—extend to offenses that require, as

 necessary elements, proof of both a material misrepresentation and an intent to deceive.”

 Aplt. Br. at 23. According to Mr. Hay, the term “steal” refers to a “range of common-law

 theft offenses that all require the ‘wrongful taking’ of property without the consent of the

 owner.” Id. at 24-25 (citing United States v. Hill, 835 F.2d 759, 763 (10th Cir. 1987);

 C.R.S. Recovery, Inc. v. Laxton, 550 Fed. App’x 512, 513 (9th Cir. 2013); and Steal,

 Merriam-Webster Dictionary). Mr. Hay also distinguishes “stealing” from “fraud,”

 which “requires proof that the defendant obtained property by means of ‘false pretenses,

 representations, or promises’ that is ‘reasonably calculated to deceive persons of ordinary

 prudence.’” Id. at 25 (citing United States v. Cochran, 109 F.3d 660, 664 (10th Cir.

 1997); and Fraud, Black’s Law Dictionary (3d ed. 1933)).

        Mr. Hay’s definition of “stealing” is overly narrow and unsupported by the text of

 the statute or by precedent. As the Supreme Court explained in Turley, “steal[ing]”

 includes the “criminal taking of personal property . . . by . . . false pretenses.” Turley,

                                               6
Appellate Case: 22-3276     Document: 010111018128         Date Filed: 03/19/2024     Page: 7



 352 U.S. at 412. “[T]he courts interpreting [stolen and steal] have declared that they do

 not have a necessary common-law meaning coterminous with larceny and exclusive of

 other theft crimes.” Id. This reasoning forecloses Mr. Hay’s argument.

        Mr. Hay points to our decision in United States v. Hill, where we held that “while

 § 641 defines a broad crime against property, it nonetheless circumscribes the means by

 which that crime can be committed.” 835 F.2d 759, 763 (10th Cir. 1987) (internal

 citation omitted). But Hill does not help Mr. Hay because its analysis turns on an

 intrinsic distinction between conversion and stealing regarding how possession is

 obtained: “[o]ne who gains possession of property by wrongfully taking it from another

 steals. One who comes into possession of property by lawful means, but afterwards

 wrongfully exercises dominion over that property against the rights of the true owner,

 commits conversion.” Id. at 764 (internal citations omitted). Thus, we concluded, “proof

 that the defendant converted property of the government is not proof that he stole it. The

 concepts of stealing and conversion are mutually exclusive.” Id. (emphasis in original).

        Unlike in Hill, the government does not argue here that Mr. Hay both came into

 possession of property in a lawful manner (i.e. conversion) and also wrongfully took the

 property (i.e. stealing). Id. Rather, the government argues that Mr. Hay’s initial

 acquisition of government property was wrongful because it was obtained through false

 pretenses, thereby placing it within Hill’s definition of stealing. And as Turley made

 clear, “fraud” and “stealing” are not mutually exclusive—stealing encompasses

 wrongfully obtaining property through “false pretenses.” 352 U.S. at 412.



                                              7
Appellate Case: 22-3276     Document: 010111018128          Date Filed: 03/19/2024        Page: 8



        Separately, Mr. Hay argues that the absence of “fraud” in the statutory text implies

 that Congress did not intend for the statute to forbid stealing by means of fraud. He

 points to other statutes that forbid both “stealing” and “obtaining by fraud” as evidence

 that Congress treats these as two separate offenses. See 18 U.S.C. §§ 659, 665(a),

 666(a)(1)(A), 668(b)(1), and 670(a). He notes that Congress did not place 18 U.S.C.

 § 641 in the section of the criminal code that criminalizes fraud offenses more generally.

        Even if Congress considered “stealing” and “fraud” to be two separate offenses,

 the statute forbidding “stealing” would still forbid “fraud” wherever a defendant

 committed “fraud” as a strategy to steal. “Stealing,” as explained by the Supreme Court,

 means the taking of property “by larceny, embezzlement, or false pretenses”—an

 expansive definition. Turley, 352 U.S. at 412 (discussing the definition of “stolen” in the

 National Motor Vehicle Theft Act, 18 U.S.C. § 2312). And obviously, the actus reus of

 stealing can violate more than one federal criminal statute. For example, one might both

 steal explosives by wrongfully transporting them away and separately violate 18 U.S.C.

 § 842(a)(3)(A) (prohibiting possession of explosive materials without a license), or steal

 an armed vessel and also violate 18 U.S.C. § 964 by delivering it to a belligerent nation,

 or steal a drone while flying it off in a way that would recklessly interfere with the

 operation of a manned aircraft in violation of 18 U.S.C. § 39B(a)(2).

        Since 18 U.S.C. § 641 prohibits stealing government property by means of fraud or

 deception, the government presented sufficient evidence to support Mr. Hay’s conviction.




                                               8
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024   Page: 9



              2. Wire fraud

       The jury also found Mr. Hay guilty of six counts of wire fraud under 18 U.S.C.

 § 1343. He contends that the government presented insufficient evidence to show he

 intended to commit fraud.

       The federal wire fraud statute applies to

              [w]hoever, having devised or intending to devise any
              scheme or artifice to defraud, or for obtaining money or
              property by means of false or fraudulent pretenses,
              representations, or promises, transmits or causes to be
              transmitted by means of wire, radio, or television
              communication in interstate or foreign commerce, any
              writings, signs, signals, pictures, or sounds for the purpose
              of executing such scheme or artifice.

 18 U.S.C. § 1343. Any falsehood must be material to the scheme, Neder v. United

 States, 527 U.S. 1, 24 (1999), and the defendant must have intended to defraud.

 United States v. Hanson, 41 F.3d 580, 583 (10th Cir. 1994).

       At trial, the government presented evidence that Mr. Hay committed wire

 fraud by lying to the VA about the extent of his injuries to obtain benefits. While

 Mr. Hay does not dispute the statements alleged by the government, he argues that

 they were insufficient to establish materiality or intent.

       We disagree. A reasonable factfinder could conclude that Mr. Hay’s

 statements were material to the VA’s decision to assign him disability benefits. “A

 false statement is material when it has a natural tendency to influence, or is capable

 of influencing, the decision of the decisionmaking body to which it was addressed.”

 United States v. Williams, 934 F.3d 1122, 1128 (10th Cir. 2019) (internal quotation


                                             9
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 10



  marks omitted). VA officials testified multiple times that the agency considered Mr.

  Hay’s description of his disability when determining his disability status. See, e.g.,

  R. Vol. III at 325, 360, 398, and 412. Viewing this evidence in the light most

  favorable to the government, see Delgado-Uribe, 363 F.3d at 1077, a reasonable trier

  of fact could conclude that Mr. Hay’s statements to the government were material.

        Mr. Hay argues that the government has not met its burden of showing

  materiality since his “doctors also had access to his full medical records, including

  reports and test results” and it was “Mr. Hay’s doctors, not Mr. Hay himself, [who]

  diagnosed him with FND based on the evidence before them, and there is no evidence

  that this diagnosis was based solely on Mr. Hay’s self-reporting his symptoms.”

  Aplt. Br. at 36-37. This argument misapprehends the standard for materiality. The

  government did not bear the burden of proving that Mr. Hay’s false statements were

  decisive to the VA’s disability determination, only that they were “capable of

  influencing” that decision. Williams, 934 F.3d at 1128. Any negligence on the part

  of Mr. Hay’s doctors in this determination is entirely consistent with the materiality

  of Mr. Hay’s misstatements.

        A reasonable factfinder could also conclude that the discrepancy between

  Mr. Hay’s statements to the VA and his actual physical condition demonstrated an

  intent to defraud. The jury heard considerable evidence from agents and medical

  professionals that Mr. Hay systematically exaggerated his symptoms to obtain

  benefits. As one VA agent testified, Mr. Hay exhibited extreme mobility difficulties

  when at his benefits exams. He could only move with assistance from his wife and

                                             10
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 11



  climbed stairs one step at a time, with both feet on each stair. After his exam, when

  he believed that he was out of the VA’s sight, Mr. Hay drove over to a pawn shop,

  walked in without assistance of his cane or his wife, and walked out carrying a

  toolbox. As neurologist Dr. Danielle Baker put it, “there is a marked discrepancy in

  what both Mr. Hay and his wife have documented on forms and also demonstrated in

  evaluations, compensation benefit evaluations versus what was seen with actual

  every day daily functioning when surveillance was taken.” R. Vol. III at 850.

  Viewing this evidence in the light most favorable to the government, a reasonable

  trier of fact could conclude that Mr. Hay intended to defraud the government. See

  Delgado-Uribe, 363 F.3d at 1077.

        Mr. Hay also contends that the government has not carried its burden of

  showing intent, since he “was upfront with his doctors about his disabilities” and told

  his doctors that his “episodes only happened once or twice a week.” Aplt. Br. at 37.

  These points, accepted as true, do not warrant reversal. The government proved

  fraud at trial by showing that the chasm between the symptoms that Mr. Hay reported

  to the VA and the mobility he exhibited out of sight was so great as to be misleading.

  Even if Mr. Hay acknowledged some aptitude for physical activity to his doctors, it

  does not follow that the government’s exaggeration theory was unsupported by the

  evidence overall. That Mr. Hay admitted some ability to perform physical tasks is

  fully consistent with the jury’s conclusion that he exaggerated his physical condition.

                                        *    *   *



                                            11
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 12



        In sum, the evidence at trial was sufficient to support the convictions for theft

  of government property and wire fraud.

        B. Fourth Amendment

        Mr. Hay next argues that the district court should have suppressed evidence

  obtained from camera surveillance of his home under the Fourth Amendment. He

  contends that constant video surveillance of his home over several months constitutes

  an unreasonable search under emerging Supreme Court case law.

        As part of its investigation, the VA installed a pole-mounted camera across the

  street from Mr. Hay’s house. The camera was motion-activated and remote-

  controlled, and it produced footage of the front of Mr. Hay’s property. The camera

  could only view Mr. Hay’s property as visible from the street.

        The Fourth Amendment guarantees “[t]he right of the people to be secure in

  their persons, houses, papers, and effects, against unreasonable searches and

  seizures.” U.S. Const. amend. IV. “When an individual seeks to preserve something

  as private, and his expectation of privacy is one that society is prepared to recognize

  as reasonable, we have held that official intrusion into that private sphere generally

  qualifies as a search and requires a warrant supported by probable cause.” Carpenter

  v. United States, 585 U.S. 296, 304 (2018). Warrantless searches “are per se

  unreasonable under the Fourth Amendment—subject only to a few specifically

  established and well-delineated exceptions.” Arizona v. Grant, 556 U.S. 332, 338

  (2009).



                                             12
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 13



        “For much of our history, Fourth Amendment search doctrine was tied to

  common-law trespass and focused on whether the Government obtains information

  by physically intruding on a constitutionally protected area.” Carpenter, 585 U.S.

  at 304. In the 1960s and 1970s, however, the Supreme Court expanded the Fourth

  Amendment’s sphere of protection to situations where an individual “seeks to

  preserve something as private, and his expectation of privacy is one that society is

  prepared to recognize as reasonable.” Id. (citing Smith v. Maryland, 442 U.S. 735,

  740 (1979)). This “reasonableness” inquiry is the touchstone of modern Fourth

  Amendment analysis.

        For decades, the Supreme Court has held that individuals do not have a

  reasonable expectation of privacy in activity that occurs in public view. “The Fourth

  Amendment protection of the home has never been extended to require law

  enforcement officers to shield their eyes when passing by a home on public

  thoroughfares.” California v. Ciraolo, 476 U.S. 207, 213 (1986). For instance, the

  Fourth Amendment does not require a warrant to view property from the air, if “[a]ny

  member of the public flying in this airspace who glanced down could have seen

  everything that the[] officers observed.” Id. at 213-214; see also Dow Chemical Co.

  v. United States, 476 U.S. 227, 238-239 (1986) (holding that aerial view of an

  industrial plant did not violate the Fourth Amendment, even if “human vision is

  enhanced somewhat”).

        But the Supreme Court has required police obtain a warrant to view activities

  that are beyond public view and perceptible only through equipment outside of

                                            13
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024      Page: 14



  general commercial circulation. In Kyllo v. United States, the government surveilled

  a house using a thermal imaging camera. 533 U.S. 27, 34 (2001). In deeming this to

  be a search, the Court explained that when “the Government uses a device that is not

  in general public use, to explore details of the home that would previously have been

  unknowable without physical intrusion, the surveillance is a ‘search’ and is

  presumptively unreasonable without a warrant.” Id. at 40; see also id. at 39 (thermal

  vision “might disclose, for example, at what hour each night the lady of the house

  takes her daily sauna and bath—a detail that many would consider ‘intimate’”). The

  Supreme Court’s guideposts are clear: viewing of private settings, visible only with

  technology that is not in general public use, is considered a search; viewing settings

  that are in public view, or visible via generally available technology, does not

  constitute a search.

        We have already concluded that the use of a pole camera does not constitute a

  search if the camera can only capture activity in public view. In United States v.

  Jackson, we held that “[t]he use of video equipment and cameras to record activity

  visible to the naked eye does not ordinarily violate the Fourth Amendment.”

  213 F.3d 1269, 1280 (10th Cir. 2000) (citing Dow Chem. Co., 476 U.S. at 239 and

  Ciraolo, 476 U.S. at 213). We reasoned that “activity a person knowingly exposes to

  the public is not a subject of Fourth Amendment protection” and that the pole

  cameras at issue in that case “were incapable of viewing inside the houses, and were

  capable of observing only what any passerby would easily have been able to

  observe.” Id. at 1281. Although Jackson predates Kyllo, it is entirely consistent with

                                            14
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024       Page: 15



  the holding in Kyllo since videographic equipment is in general commercial

  circulation and available to the public at large.

        The facts of this case are not meaningfully different from those in Jackson.

  Both cases involve the extensive use of cameras surreptitiously filming the front of

  the house. While Mr. Hay noted at oral argument that the pole camera incidentally

  captured activity in his house, that activity occurred at night in front of the window

  and was therefore visible to any passerby. Since the pole camera could not capture

  footage of any activity that was not in public view, it did not violate the Fourth

  Amendment.

        To counter this, Mr. Hay argues that Jackson has been abrogated by the

  Supreme Court’s Carpenter decision. He contends that while limited video

  surveillance might not violate the Constitution, the government’s months-long,

  potentially limitless surveillance crosses the line. In Carpenter, the Supreme Court

  considered whether the government conducts a search when it accesses historical

  cell-site location information. There, the government subpoenaed cell phone data

  from the suspect’s wireless provider to track the suspect’s movement before, during,

  and after a crime. The Court found this to be a search covered by the Fourth

  Amendment. It explained that whenever a cell phone connects to a cell site, “it

  generates a time-stamped record known as cell-site location information,” the

  precision of which “depends on the size of the geographic area covered by the cell

  site.” Carpenter, 585 U.S. at 301. Since many people carry their cell phones with

  them wherever they go, cell-site location information “chronicle[s] a person’s past

                                             15
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024      Page: 16



  movements through the record of his cell phone signals.” Id. at 309. The Court

  found this unreasonable since “[w]hoever the suspect turns out to be, he has

  effectively been tailed every moment of every day for five years, and the police

  may—in the Government’s view—call upon the results of that surveillance without

  regard to the constraints of the Fourth Amendment.” Id. at 312.

        The Carpenter court distinguished the case from United States v. Knotts,

  where it found that planting a transmitter in a suspect’s car to aid in tracking the

  vehicle did not constitute a search. 460 U.S. 276, 282 (1983). There, the Court

  explained that “[a] person travelling in an automobile on public thoroughfares has no

  reasonable expectation of privacy in his movements from one place to another.” Id.

  at 281. Although the officers “relied not only on visual surveillance, but on the use

  of the beeper to signal the presence of [the] automobile to the police receiver,”

  “nothing in the Fourth Amendment prohibited the police from augmenting the

  sensory faculties bestowed upon them at birth” with the beeper. Id. at 282. The

  Carpenter court found that Knotts was not controlling on the question of cell site

  location information, since that opinion had acknowledged that “different

  constitutional principles may be applicable if twenty-four hour surveillance of any

  citizen of this country were possible.” Carpenter, 585 U.S. at 306-307 (citing

  Knotts, 460 U.S. at 283-284) (internal quotation marks and brackets omitted). It

  further noted that in a more recent case on vehicle tracking, “[a] majority of this

  Court has already recognized that individuals have a reasonable expectation of

  privacy in the whole of their physical movements.” Id. at 310 (citing United States v.

                                             16
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024      Page: 17



  Jones, 565 U.S. 400, 430 (2018) (Alito, J. concurring); and Jones, 565 U.S. at 415

  (Sotomayor, J., concurring)).

        The Carpenter court distinguished “pursu[ing] a suspect for a brief stretch,”

  which fell within a societal expectation of privacy, from “secretly monitor[ing] and

  catalogu[ing] every single movement of an individual’s car for a very long period,”

  which fell outside of it. Id. (citing Jones, 565 U.S. at 429-430 (Alito, J.,

  concurring)). It reasoned that “[a]llowing government access to cell-site records

  contravenes that expectation” because “[m]apping a cell phone’s location over the

  course of 127 days provides an all-encompassing record of the holder’s

  whereabouts.” Id. at 311. This in turn “provides an intimate window into a person’s

  life, revealing not only his particular movements, but through them his ‘familial,

  political, professional, religious, and sexual associations.’” Id. citing (Jones,

  565 U.S. at 415 (Sotomayor, J. concurring)). Further, unlike tracking devices in cars,

  “police need not even know in advance whether they want to follow a particular

  individual, or when,” since cell site location data allows the Government to “travel

  back in time to retrace a person’s whereabouts, subject only to the retention policies

  of the wireless carriers.” Id. at 312. The Carpenter court concluded that accessing

  cell site location information “invaded Carpenter’s reasonable expectation of privacy

  in the whole of his physical movements” and therefore constituted a search. Id.

  at 313.

        Mr. Hay contends that he has a similar reasonable expectation of privacy in the

  whole of his physical movements coming and going from his home, plus a heightened

                                             17
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 18



  expectation of privacy in the exterior to his home. According to Mr. Hay, the

  recording of his house for an extended period of time (68 days in this case) catalogs

  his habits, patterns, and visitors in a way that ordinary physical surveillance could

  not duplicate. As he puts it, “the footage obtained painted an intimate portrait of

  Mr. Hay’s personal life,” including “when he entered and exited his home; who

  visited him and his family,” and “what Mr. Hay did on his own front porch.” Aplt.

  Br. at 44. He acknowledges that this activity took place in public but argues that

  “[w]hile people subjectively lack an expectation of privacy in some discrete actions

  they undertake in unshielded areas around their homes, they do not expect that every

  such action will be observed and perfectly preserved for the future.” Id. at 45 (citing

  Commonwealth v. Mora, 150 N.E.3d 297, 306 (Mass. 2020)).

        This argument is precluded by Jackson. That the surveillance took place over

  an extended period of time does not change the basic logic of the opinion—camera

  surveillance of a home visible to passersby does not constitute a search. Nor does

  Carpenter change the equation. The Supreme Court expressly noted that its decision

  was “a narrow one:” “[w]e do not express a view on matters not before us: real-time

  CSLI or ‘tower dumps’ . . . or call into question conventional surveillance techniques

  and tools, such as security cameras.” Carpenter, 585 U.S. at 316 (emphasis added).

  Our holding in Jackson that pole cameras trained on a house do not violate the Fourth

  Amendment remains binding law, and Carpenter, without more, does not disturb it.

  In so holding, we are not alone. No circuit court has concluded that extended video

  surveillance of a house is a search under Carpenter. See United States v. Dennis,

                                             18
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 19



  41 F.4th 732, 740-741 (5th Cir. 2022) (finding no Fourth Amendment violation in the

  installation of cameras directed at front and back of defendant’s house); United States

  v. Tuggle, 4 F.4th 505, 523-524 (7th Cir. 2021) (finding no Fourth Amendment

  violation in government’s prolonged, round-the clock use of cameras capturing the

  exterior of defendant’s home); and United States v. Trice, 966 F.3d 506, 518-520

  (6th Cir. 2020) (finding no Fourth Amendment violation in installation of camera

  across the hallway from entrance of defendant’s apartment); cf. Leaders of a

  Beautiful Struggle v. Baltimore Police Dep’t, 2 F.4th 330, 341-342 (4th Cir. 2021)

  (en banc) (finding a Fourth Amendment violation in use of planes to record

  movements across an entire city). An en banc First Circuit deadlocked on the

  question, with an even number of judges reaching opposite conclusions. See United

  States v. Moore-Bush, 36 F.4th 320 (1st Cir. 2022) (en banc).

        Regardless, Mr. Hay’s privacy interests fall outside Carpenter’s rationale.

  Carpenter acknowledged that individuals have a privacy interest in “the whole of

  their physical movements.” Carpenter, 585 U.S. at 310. The pole camera across the

  street from Mr. Hay came nowhere close to capturing “the whole of his physical

  movements.” It could only capture his movements at a single location, outside his

  house. As soon as he left his house, the government could no longer track him by

  this means. And the Carpenter majority was particularly concerned by retrospective

  police searches of previously unidentified individuals—i.e. where the government

  would “travel back in time to retrace a person’s whereabouts, subject only to the

  retention policies of the wireless carriers.” Id. at 312. In this case, the government

                                             19
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024     Page: 20



  did not delve into a preexisting data set on Mr. Hay’s whereabouts. It set up the

  camera while Mr. Hay was already under investigation as a prospective, not

  retrospective, investigative measure. The surveillance here merely enhances what

  law enforcement could always do—monitor a suspect’s movement in public view.

         Mr. Hay attempts to divine a new privacy interest by merging the one

  articulated in Carpenter (a retrospective “all encompassing record of the holder’s

  whereabouts,” 585 U.S. at 311), with the one identified in Kyllo and Ciraolo (privacy

  connected to one’s home). 533 U.S. at 31, 476 U.S. at 213; see also Lange v.

  California, 141 S. Ct. 2011, 2018 (2021) (“[W]hen it comes to the Fourth

  Amendment, the home is first among equals.” (citing Florida v. Jardines, 569 U.S. 1,

  6 (2013)).

         But the Supreme Court’s recognition of privacy interests in the home does not

  “require law enforcement officers to shield their eyes when passing by a home on

  public thoroughfares.” Ciraolo, 476 U.S. at 213. The government executes a search

  when it “uses a device that is not in general public use, to explore details of the home

  that would previously have been unknowable without physical intrusion,” Kyllo,

  533 U.S. at 40, but “[n]ow more than ever, cameras are ubiquitous, found in the

  hands and pockets of virtually all Americans, on the doorbells and entrances of

  homes, and on the walls and ceilings of businesses.” Tuggle, 4 F.4th at 516.

  Mr. Hay retains some privacy interests in the whole of his physical movements and in

  the interior of his home, but the pole camera at issue did not infringe upon either of

  those interests.

                                             20
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024      Page: 21



        The Supreme Court has defined a “search” under the Fourth Amendment not

  by a fixed point, but by “[w]hen an individual seeks to preserve something as private

  and his expectation of privacy is one that society is prepared to recognize as

  reasonable.” Carpenter, 585 U.S. at 304 (citing Smith, 442 U.S. at 740) (internal

  quotation marks omitted). “Current Fourth Amendment jurisprudence admits of a

  precarious circularity: Cutting-edge technologies will eventually and inevitably

  permeate society. In turn, society’s expectations of privacy will change as citizens

  increasingly rely on and expect these new technologies.” Tuggle, 4 F.4th at 527

  (upholding use of pole camera).

        Few technologies have expanded more rapidly than the ubiquitous camera,

  which is worn by police officers, built into cellphones that the Carpenter court called

  “almost a feature of human anatomy,” and strapped to front doors. United States v.

  Moore-Bush, 36 F.4th at 372 (Lynch, J., concurring) (citing Carpenter, 585 U.S.

  at 311). Cutting edge drone technology enables police to conduct discreet aerial

  investigations, see State v. Stevens, 210 N.E.3d 1154, 1157 (Ohio App. 2023), while

  satellite images of homes are free and readily available to citizens and law

  enforcement alike. See In re Murphy, No. 771 Sept. Term 2022, 2023 WL 2999975,

  at *6 (Md. App. 2023). Artificial intelligence software accelerates facial

  identification and pattern recognition to a previously unimaginable degree. As video

  cameras proliferate throughout society, regrettably, the reasonable expectation of

  privacy from filming is diminished.



                                            21
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024       Page: 22



        In conclusion, Mr. Hay had no reasonable expectation of privacy in a view of

  the front of his house. The district court did not err in denying suppression of that

  footage.

        C. Evidentiary rulings

        Finally, Mr. Hay argues that he is entitled to a new trial because of three

  erroneous evidentiary rulings by the district court. “We review a trial court’s

  evidentiary decisions for abuse of discretion. However, we subject to de novo review

  a trial court’s legal conclusions about the Federal Rules of Evidence.” United States

  v. Cherry, 217 F.3d 811, 814 (10th Cir. 2000).

        First, Mr. Hay argues that the district court erred in permitting the VA agents

  to narrate the contents of video footage. He argues that this testimony bolstered the

  impact of the footage by allowing non-expert opinion testimony outside the agent’s

  expertise. Federal Rule of Evidence 701(b), only permits lay testimony when it is:

               (a) rationally based on the witness’s perception;
               (b) helpful to clearly understanding the witness’s testimony
                   or to determining a fact in issue; and
               (c) not based on scientific, technical, or other specialized
                   knowledge within the scope of Rule 702.

  Fed. R. Evid. 701. Mr. Hay argues that the agents’ testimony did not satisfy the

  second condition, because “their impressions of the footage itself were

  inappropriate.” Aplt. Br. at 60.

        But Rule 701 does not prohibit lay testimony of impressions if those

  impressions are helpful to determining a fact in issue. Fed. R. Evid. 701(b). The

  district court did not abuse its discretion in concluding that the VA agents’

                                             22
Appellate Case: 22-3276     Document: 010111018128        Date Filed: 03/19/2024    Page: 23



  impressions of what was occurring in the video, informed by their deep familiarity

  with the footage, would help the jury determine a fact in issue.

        Second, Mr. Hay argues that the district court erred by permitting the

  government to introduce his VA exam records, which included the doctors’

  assessment of his entitlement to disability benefits. According to Mr. Hay, these

  were out-of-court statements offered for their truth and therefore excludable under

  Fed. R. Evid. 801. The district court admitted these records under Fed. R. Evid.

  803(4)’s exception for “medical diagnosis or treatment.”1 Mr. Hay contends that the

  exception does not apply, because a medical assessment for the purpose of

  determining disability is not a “diagnosis.”

        We disagree. The dictionary definition of “diagnosis” means “the discovery of

  a patient’s illness or the determination of the nature of his disease from a study of his

  symptoms,” or “[t]he art or act of recognizing the presence of disease from its

  symptoms, and deciding as to its character, also the decision reached, for

  determination of type or condition through case or specimen study or conclusion

  arrived at through critical perception or scrutiny.” Diagnosis, Black’s Law

  Dictionary (4th rev. ed. 1968). Nothing in that definition suggests that making a

  disability determination for a given ailment precludes being “diagnosed” with that



  1
   Rule 803(4) provides that “[a] statement that: (A) is made for — and is reasonably
  pertinent to — medical diagnosis or treatment; and (B) describes medical history;
  past or present symptoms or sensations; their inception; or their general cause” is an
  exception to the rule against hearsay evidence.

                                             23
Appellate Case: 22-3276    Document: 010111018128        Date Filed: 03/19/2024    Page: 24



  ailment. Indeed, it seems to require as much. Rule 803(4) authorizes admission of

  the VA records.

        Third, Mr. Hay argues that the district court erred in admitting evidence from

  after the charging period. The indictment charged Mr. Hay with committing theft

  and fraud between 2011 and 2018. The district court, however, also admitted

  evidence of Mr. Hay’s behavior from after that period—a mechanic’s lien stating that

  he had worked as a farm manager from 1985 to 2020, and a video from 2021.

  Mr. Hay contends that this evidence was unduly prejudicial in violation of Fed. R.

  Evid. 403.

        Rule 403 permits a district court to “exclude relevant evidence if its probative

  value is substantially outweighed by a danger of one or more of the following: unfair

  prejudice, confusing the issues, misleading the jury, undue delay, wasting time, or

  needlessly presenting cumulative evidence.” “Assessing the probative value of the

  proffered evidence, and weighing any factors counseling against admissibility is a

  matter first for the district court’s sound judgment under Rules 401 and 403.”

  Sprint/United Management Co. v. Mendelsohn, 552 U.S. 379, 384 (2008) (quoting

  United States v. Abel, 469 U.S. 45, 54 (1984)) (brackets omitted). “This is

  particularly true with respect to Rule 403 since it requires an on-the-spot balancing of

  probative value and prejudice, potentially to exclude as unduly prejudicial some

  evidence that already has been found to be factually relevant.” Id. (internal quotation

  marks omitted). Accordingly, a “trial court has broad discretion to determine



                                            24
Appellate Case: 22-3276   Document: 010111018128        Date Filed: 03/19/2024    Page: 25



  whether prejudice inherent in otherwise relevant evidence outweighs its probative

  value.” United States v. Poole, 929 F.2d 1476, 1482 (10th Cir. 1991).

        The district court acted within its discretion in admitting evidence post-dating

  the charging period. The VA allotted benefits to Mr. Hay because it determined that

  he was “permanently disabled,” so any evidence that Mr. Hay was able to perform

  physical labor after that determination—whether or not it was within the charged

  period—was probative as to whether he had defrauded the VA.

                                   III. Conclusion

        We affirm the district court’s denial of a judgment of acquittal and

  admission of the contested evidence.




                                            25

```

---
