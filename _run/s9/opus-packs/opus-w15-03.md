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

## GROUP: _overhaul2/lake/cases/United States v. Cooley.json  (`lake-record`, 2 assertions)

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
{"assertion_id": "6fb95b76b546ed2b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Cooley"}, "payload": {"all": [{"cite": "593 U.S. 345", "page": "345", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "593"}, {"cite": "141 S. Ct. 1638", "page": "1638", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "141"}, {"cite": "210 L. Ed. 2d 1", "page": "1", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "210"}], "display": "593 U.S. 345", "official": {"cite": "593 U.S. 345", "page": "345", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "593"}, "official_selection_present": true, "record_id": "United States v. Cooley"}}
{"assertion_id": "10176e5e34a5afa0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Cooley"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Cooley", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Cortez.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Cortez"
type: case
citation: "449 U.S. 411 (1981)"
parallel_cite: "101 S. Ct. 690; 66 L. Ed. 2d 621; 49 U.S.L.W. 4099"
neutral_cite: 1981 U.S. LEXIS 58
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-01-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Cortez
  varies_by_point: false
  scope_note: "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110377/united-states-v-cortez/"
  cluster_id: 110377
  opinion_id: 110377
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Anchor"
related: ["[[Terry v. Ohio]]", "[[United States v. Arvizu]]", "[[Navarette v. California]]", "[[Ornelas v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion", "terry-stop"]
holding: "Reasonable suspicion = a particularized and objective basis on the totality of the circumstances (the 'whole picture')."
lake:
  record_id: United States v. Cortez
  status: verified
  projected_at: 2026-07-06
---

# United States v. Cortez

*449 U.S. 411 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Border Patrol officers studied evidence of an alien-smuggling operation: footprints in a remote desert area showed a guide (nicknamed "Chevron" from a distinctive shoe print) leading groups on certain nights, and the tracks led toward a pickup point near a particular highway. From the pattern of clues — the likely night, time window, direction of travel, and that a vehicle would be needed to carry the group — the officers deduced when and where the smuggler's vehicle would pass, stopped a matching truck, and found illegal aliens inside.

## Issue
What quantum and kind of basis the Fourth Amendment requires for an investigatory vehicle stop — i.e., how reasonable suspicion is assessed.

## Rule
Reasonable suspicion is a particularized, objective judgment drawn from the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]: "the totality of the circumstances—the whole picture—must be taken into account. Based upon that whole picture the detaining officers must have a particularized and objective basis for suspecting the particular person stopped of criminal activity." — 449 U.S. at 417–18. ^pin-417

The assessment permits officers to draw on their experience and to make commonsense inferences and deductions about the cumulative information available to them.

## Application
The officers' chain of inferences — reconstructing the smuggler's method, route, likely night, and the time window from the physical clues, and reasoning that a vehicle would be needed at a predictable point — gave them a particularized and objective basis to suspect that the specific truck they stopped was carrying illegal aliens. Viewed as a whole rather than as isolated facts, that picture supported reasonable suspicion, so the investigatory stop was valid.

## Conclusion
The stop was supported by reasonable suspicion and was upheld. Reasonable suspicion is measured by the whole picture and requires a particularized and objective basis, informed by the officers' experience and reasonable inferences.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Cortez* refines the reasonable-suspicion standard of [[Terry v. Ohio]] and supplied the "whole picture" / "particularized and objective basis" language later applied in [[United States v. Arvizu]] (no divide-and-conquer), [[Ornelas v. United States]], and [[Navarette v. California]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Key — Progeny / Refinement*
- [[Reasonable Suspicion]] — *Key — Anchor*

## Sources
- *United States v. Cortez*, 449 U.S. 411 (1981) — https://www.courtlistener.com/opinion/110377/united-states-v-cortez/ — pinpoint: 417–18.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3229adf7972b73e7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Cortez"}, "payload": {"all": [{"cite": "449 U.S. 411", "page": "411", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "449"}, {"cite": "101 S. Ct. 690", "page": "690", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "66 L. Ed. 2d 621", "page": "621", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "66"}, {"cite": "1981 U.S. LEXIS 58", "page": "58", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1981"}, {"cite": "49 U.S.L.W. 4099", "page": "4099", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "49"}], "display": "449 U.S. 411", "official": {"cite": "449 U.S. 411", "page": "411", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "449"}, "official_selection_present": true, "record_id": "United States v. Cortez"}}
{"assertion_id": "10dbc353addb5dc9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-417", "record_id": "United States v. Cortez"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-417", "pinpoint_status": "slip-only", "quote": "from a distinctive shoe print) leading groups on certain nights, and the tracks led toward a pickup point near a particular highway. From the pattern of clues — the likely night, time window, direction of travel, and that a vehicle would be needed to carry the group — the officers deduced when and where the smuggler's vehicle would pass, stopped a matching truck, and found illegal aliens inside. ## Issue What quantum and kind of basis the Fourth Amendment requires for an investigatory vehicle stop — i.e., how reasonable suspicion is assessed. ## Rule Reasonable suspicion is a particularized, objective judgment drawn from the totality of the circumstances:", "quote_fidelity": "mismatch", "record_id": "United States v. Cortez", "star_marker": null}}
{"assertion_id": "5af87766b3d59d85", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Cortez"}, "payload": {"as_of_content": "1981-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Cortez", "scope_note": "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion.", "varies_by_point": false}}
```

### lake record — United States v. Cortez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cortez",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Cortez",
    "case_name_short": "Cortez",
    "case_name_full": "UNITED STATES v. CORTEZ Et Al.",
    "input_case_name": "United States v. Cortez",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-01-21",
    "year": 1981,
    "docket": null,
    "cluster_id": 110377,
    "lead_opinion_id": 110377,
    "sibling_ids": [
      110377,
      9428131,
      9428132
    ],
    "absolute_url": "/opinion/110377/united-states-v-cortez/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "449 U.S. 411",
      "volume": "449",
      "reporter": "U.S.",
      "page": "411",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 690",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 621",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4099",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4099",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 58",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "449 U.S. 411",
        "volume": "449",
        "reporter": "U.S.",
        "page": "411",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 690",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "690",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "66 L. Ed. 2d 621",
        "volume": "66",
        "reporter": "L. Ed. 2d",
        "page": "621",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 58",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "58",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 U.S.L.W. 4099",
        "volume": "49",
        "reporter": "U.S.L.W.",
        "page": "4099",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "449 U.S. 411",
    "official_selection": {
      "court_class": "scotus",
      "selected": "449 U.S. 411",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-417",
      "page": null,
      "quote": "from a distinctive shoe print) leading groups on certain nights, and the tracks led toward a pickup point near a particular highway. From the pattern of clues \u2014 the likely night, time window, direction of travel, and that a vehicle would be needed to carry the group \u2014 the officers deduced when and where the smuggler's vehicle would pass, stopped a matching truck, and found illegal aliens inside. ## Issue What quantum and kind of basis the Fourth Amendment requires for an investigatory vehicle stop \u2014 i.e., how reasonable suspicion is assessed. ## Rule Reasonable suspicion is a particularized, objective judgment drawn from the totality of the circumstances:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Cortez",
    "varies_by_point": false,
    "scope_note": "Good law; the 'particularized and objective basis' / 'whole picture' formulation of reasonable suspicion.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 9352593,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6620965,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tripp",
          "cluster_id": 6478743,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane1_negative"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sharpe",
          "cluster_id": 111378,
          "cite": [
            "84 L. Ed. 2d 605",
            "105 S. Ct. 1568",
            "470 U.S. 675",
            "1985 U.S. LEXIS 74",
            "53 U.S.L.W. 4346"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hensley",
          "cluster_id": 111294,
          "cite": [
            "83 L. Ed. 2d 604",
            "105 S. Ct. 675",
            "469 U.S. 221",
            "1985 U.S. LEXIS 34",
            "53 U.S.L.W. 4053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
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
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Hicks",
          "cluster_id": 111834,
          "cite": [
            "94 L. Ed. 2d 347",
            "107 S. Ct. 1149",
            "480 U.S. 321",
            "1987 U.S. LEXIS 1056",
            "55 U.S.L.W. 4258"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Chesternut",
          "cluster_id": 112095,
          "cite": [
            "100 L. Ed. 2d 565",
            "108 S. Ct. 1975",
            "486 U.S. 567",
            "1988 U.S. LEXIS 2582",
            "56 U.S.L.W. 4558"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knights",
          "cluster_id": 118468,
          "cite": [
            "151 L. Ed. 2d 497",
            "122 S. Ct. 587",
            "534 U.S. 112",
            "2001 U.S. LEXIS 10950"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Woods v. State",
          "cluster_id": 1628737,
          "cite": [
            "956 S.W.2d 33",
            "1997 Tex. Crim. App. LEXIS 90",
            "1997 WL 685978"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cortez:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110377 OR 9428131 OR 9428132) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQwMDQ0ODAwMDAwJnM9MTAzMTYwNzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110377+OR+9428131+OR+9428132%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 4,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(110377 OR 9428131 OR 9428132)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODcmcz0xNTE2NTcxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110377+OR+9428131+OR+9428132%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110377 OR 9428131 OR 9428132)",
        "reviewed": 171,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 171,
        "triage_read": 1,
        "triage_snippet_classified": 170
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110377 OR 9428131 OR 9428132)",
    "indexed_citing_opinions": 3643,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110377,
        "count": 3198,
        "count_source": "search"
      },
      {
        "opinion_id": 9428131,
        "count": 501,
        "count_source": "search"
      },
      {
        "opinion_id": 9428132,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5978,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-cortez.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0NzA5MyZzPTEwNjQ2MjMxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110377+OR+9428131+OR+9428132%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110377,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110377,
        "cited_id": 364821,
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
    "date_created": "2026-07-05T23:17:11Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:22:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:17:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Cortez

```
<div>
<center><b><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U.S. 411</a></span> (1981)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
CORTEZ ET AL.</h1></center>
<center>No. 79-404.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 1, 1980.</center>
<center>Decided January 21, 1981.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><span class="star-pagination">*412</span> <i>Barbara E. Etkind</i> argued the cause for the United States. With her on the briefs were <i>Solicitor General McCree, Assistant Attorney General Heymann, Deputy Solicitor General Frey, William G. Otis,</i> and <i>John C. Winkfield.</i></p>
<p><i>S. Jeffrey Minker</i> argued the cause and filed a brief for respondent Cortez.</p>
<p><i>Bernardo P. Velasco</i> argued the cause for respondent Hernandez-Loera. With him on the brief was <i>Thomas W. O'Toole.</i></p>
<p>CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./447/904/">447 U. S. 904</a></span>, to consider whether objective facts and circumstantial evidence suggesting that a particular vehicle is involved in criminal activity may provide <span class="star-pagination">*413</span> a sufficient basis to justify an investigative stop of that vehicle.</p>
<p></p>
<h2>I</h2>
<p>Late in 1976, Border Patrol officers patrolling a sparsely populated section of southern central Arizona found human footprints in the desert. In time, other sets of similar foot-prints were discovered in the same area. From these sets of footprints, it was deduced that, on a number of occasions, groups of from 8 to 20 persons had walked north from the Mexican border, across 30 miles of desert and mountains, over a fairly well-defined path, to an isolated point on Highway 86, an east-west road running roughly parallel to the Mexican border.</p>
<p>Officers observed that one recurring shoeprint bore a distinctive and repetitive V-shaped or chevron design. Because the officers knew from recorded experience that the area through which the groups passed was heavily trafficked by alines illegally entering the country from Mexico, they surmised that a person, to whom they gave the case-name "Chevron," was guiding aliens illegally into the United States over the path marked by the tracks to a point where they could be picked up by a vehicle.</p>
<p>The tracks led into or over obstacles that would have been avoided in daylight. From this, the officers deduced that "Chevron" probably led his groups across the border and to the pickup point at night. Moreover, based upon the times when they had discovered the distinctive sets of tracks, they concluded that "Chevron" generally traveled during or near weekends and on nights when the weather was clear.</p>
<p>Their tracking disclosed that when "Chevron's" groups came within 50 to 75 yards of Highway 86, they turned right and walked eastward, parallel to the road. Then, approximately at highway milepost 122, the tracks would turn north and disappear at the road. From this pattern, the officers concluded that the aliens very likely were picked up by a vehicle <span class="star-pagination">*414</span> probably one approaching from the east, for after a long overland march the group was most likely to walk parallel to the highway <i>toward</i> the approaching vehicle. The officers also concluded that, after the pickup, the vehicle probably returned to the east, because it was unlikely that the group would be walking away from its ultimate destination.</p>
<p>On the Sunday night of January 30-31, 1977, Officers Gray and Evans, two Border Patrolmen who had been pursuing the investigation of "Chevron," were on duty in the Casa Grande area. The latest set of observed "Chevron" tracks had been made on Saturday night, January 15-16. January 30-31 was the first clear night after three days of rain. For these reasons. Gray and Evans decided there was a strong possibility that "Chevron" would lead aliens from the border to the highway that night.</p>
<p>The officers assumed that, if "Chevron" did conduct a group that night, he would not leave Mexico until after dark, that is, about 6 p. m. They knew from their experience that groups of this sort, traveling on foot, cover about two and a half to three miles an hour. Thus, the 30-mile journey would take from 8 to 12 hours. From this, the officers calculated that "Chevron" and his group would arrive at Highway 86 somewhere between 2 a. m. and 6 a. m. on January 31.</p>
<p>About 1 a. m., Gray and Evans parked their patrol car on an elevated location about 100 feet off Highway 86 at milepost 149, a point some 27 miles east of milepost 122. From their vantage point, the officers could observe the Altar Valley, an adjoining territory they had been assigned to watch that night, and they also could see vehicles passing on Highway 86. They estimated that it would take approximately one hour and a half for a vehicle to make a round trip from their vantage point to milepost 122. Working on the hypothesis that that the pickup vehicle approached milepost 122 from the east and thereafter returned to its starting point, they focused upon vehicles that passed them from the east <span class="star-pagination">*415</span> and, after about one hour and a half, passed them returning to the east.</p>
<p>Because "Chevron" appeared to lead groups of the between 8 and 20 aliens at a time, the officers deduced that the pickup vehicle would be one that was capable of carrying that large a group without arousing suspicion. For this reason, and because they knew that certain types of vehicles were commonly used for smuggling sizable groups of aliens, they decided to limit their attention to vans, pickup trucks, other small trucks, campers, motor homes, and similar vehicles.</p>
<p>Traffic on Highway 86 at milepost 149 was normal on the night of the officers' surveillance. In the 5-hour period between 1 a. m. and 6 a. m., 15 to 20 vehicles passed the officers heading west, toward milepost 122. Only two of themboth pickup trucks with camper shellswere of the kind that the officers had concluded "Chevron" would likely use if he was to carry aliens that night. One, a distinctively colored pickup truck with a camper shell, passed for the first time at 4:30 a. m. Officer Gray was able to see and record only a partial license number, "GN 88."<sup>[1]</sup> At 6:12 a. m., almost exactly the estimated one hour and a half later, a vehicle looking like this same pickup passed them again, this time heading east.</p>
<p>The officers followed the pickup and were satisfied from its license plate, "GN 8804," that it was the same vehicle that had passed at 4:30 a. m. At that point, they flashed their police lights and intercepted the vehicle. Respondent Jesus Cortez was the driver and owner of the pickup; respondent Pedro Hernandez-Loera was sitting in the passenger's seat. Hernandez-Loera was wearing shoes with soles matching the distinctive "Chevron" shoeprint.</p>
<p>The officers identified themselves and told Cortez they were conducting an immigration check. They asked if he was <span class="star-pagination">*416</span> carrying any passengers in the camper. Cortez told them he had picked up some hitchhikers, and he proceeded to open the back of the camper. In the camper, there were six illegal aliens. The officers then arrested the respondents.</p>
<p>Cortez and Hernandez-Loera were charged with six counts of transporting illegal aliens in violation of <span class="citation no-link">8 U. S. C. § 1324</span> (a). By pretrial motion, they sought to suppress the evidence obtained by Officers Gray and Evans as a result of stopping their vehicle. They argued that the officers did not have adequate cause to make the investigative stop. The District Court denied the motion. A jury found the respondents guilty as charged. They were sentenced to concurrent prison terms of five years on each of six counts. In addition, Hernandez-Loera was fined $12,000.</p>
<p>A divided panel of the Court of Appeals for the Ninth Circuit reversed, holding that the officers lacked a sufficient basis to justify the stop of the pickup. <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d 505</a></span> (1979). That court recognized that <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975), provides a standard governing investigative stops of the kind involved in this case, stating:</p>
<blockquote>"The quantum of cause necessary in . . . cases [like this one] was established . . . in <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i>. . . . `[O]fficers on roving patrol may stop vehicles only if they are aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country.'" <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d, at 507</a></span> (quoting <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>) (citations omitted).</blockquote>
<p>The court also recognized that "the ultimate question on appeal is whether the trial judge's finding that founded suspicion was present here was clearly erroneous." <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/#507" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E....">595 F. 2d, at 507</a></span>. Here, because, in the view of the facts of the two judges constituting the majority, "[t]he officers did not have a valid basis for singling out the Cortez vehicle," <span class="citation" data-id="9465636"><a href="/opinion/364821/united-states-v-jesus-e-cortez-aka-jesus-e-cortez-espinoza-united/#508" aria-description="Citation for case: United States v. Jesus E. Cortez, A/K/A Jesus E...."><i>id.,</i> at 508</a></span>, and because <span class="star-pagination">*417</span> the circumstances admitted "far too many innocent inferences to make the officers' suspicions reasonably warranted," <i>ibid.,</i> the panel concluded that the stop of Cortez' vehicle was a violation of the respondents' rights under the Fourth Amendment. In dissent, Judge Chambers was persuaded that <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> recognized the validity of permitting an officer to assess the facts in light of his past experience.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment applies to seizures of the person, including brief investigatory stops such as the stop of the vehicle here. <i>Reid</i> v. <i>Georgia,</i> <span class="citation" data-id="9428067"><a href="/opinion/110336/reid-v-georgia/#440" aria-description="Citation for case: Reid v. Georgia">448 U. S. 438, 440</a></span> (1980); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878</a></span>; <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968). An investigatory stop must be justified by some objective manifestation that the person stopped is, or is about to be, engaged in criminal activity.<sup>[2]</sup><i>Brown</i> v. <i>Texas,</i> <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas">443 U. S. 47, 51</a></span> (1979); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 661</a></span> (1979); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>; <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146-149</a></span> (1972); <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 16-19</a></span>.</p>
<p>Courts have used a variety of terms to capture the elusive concept of what cause is sufficient to authorize police to stop a person. Terms like "articulable reasons" and "founded suspicion" are not self-defining; they fall short of providing clear guidance dispositive of the myriad factual situations that arise. But the essence of all that has been written is that the totality of the circumstancesthe whole picture must be taken into account. Based upon that whole picture the detaining officers must have a particularized and objective basis for suspecting the particular person stopped of criminal <span class="star-pagination">*418</span> activity. See, <i>e. g., </i><i>Brown</i> v. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Texas, supra,</i> at 51</a></span>; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>.</p>
<p>The idea that an assessment of the whole picture must yield a particularized suspicion contains two elements, each of which must be present before a stop is permissible. First, the assessment must be based upon all of the circumstances. The analysis proceeds with various objective observations, information from police reports, if such are available, and consideration of the modes or patterns of operation of certain kinds of lawbreakers. From these data, a trained officer draws inferences and makes deductionsinferences and deductions that might well elude an untrained person.</p>
<p>The process does not deal with hard certainties, but with probabilities. Long before the law of probabilities was articulated as such, practical people formulated certain commonsense conclusions about human behavior; jurors as factfinders are permitted to do the sameand so are law enforcement officers. Finally, the evidence thus collected must be seen and weighed not in terms of library analysis by scholars, but as understood by those versed in the field of law enforcement.</p>
<p>The second element contained in the idea that an assessment of the whole picture must yield a particularized suspicion is the concept that the process just described must raise a suspicion that the particular individual being stopped is engaged in wrongdoing. Chief Justice Warren, speaking for the Court in <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> said that "[t]his demand for specificity in the information upon which police action is predicated is <i>the central teaching of this Court's Fourth Amendment jurisprudence." Id.,</i> at 21, n. 18 (emphasis added). See also <i>Brown</i> v. <span class="citation" data-id="110128"><a href="/opinion/110128/brown-v-texas/#51" aria-description="Citation for case: Brown v. Texas"><i>Texas, supra,</i> at 51</a></span>; <i>Delaware</i> v. <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><i>Prouse, supra,</i> at 661-663</a></span>; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 884</a></span>.</p>
<p></p>
<h2>B</h2>
<p>This case portrays at once both the enormous difficulties of patrolling a 2,000-mile open border and the patient skills <span class="star-pagination">*419</span> needed by those charged with halting illegal entry into this country. It implicates all of the principles just discussed especially the imperative of recognizing that, when used by trained law enforcement officers, objective facts, meaningless to the untrained, can be combined with permissible deductions from such facts to form a legitimate basis for suspicion of a particular person and for action on that suspicion. We see here the kind of police work often suggested by judges and scholars as examples of appropriate and reasonable means of law enforcement. Here, fact on fact and clue on clue afforded a basis for the deductions and inferences that brought the officers to focus on "Chevron."</p>
<p>Of critical importance, the officers knew that the area was a crossing point for illegal aliens. They knew that it was common practice for persons to lead aliens through the desert from the border to Highway 86, where they couldby pre-arrangement be picked up by a vehicle. Moreover, based upon clues they had discovered in the 2-month period prior to the events at issue here, they believed that one such guide, whom they designated "Chevron," had a particular pattern of operations.</p>
<p>By piecing together the information at their disposal, the officers tentatively concluded that there was a reasonable likelihood that "Chevron" would attempt to lead a group of aliens on the night of Sunday, January 30-31. Someone with chevron-soled shoes had led several groups of aliens in the previous two months, yet it had been two weeks since the latest crossing. "Chevron," they deduced, was therefore due reasonably soon. "Chevron" tended to travel on clear weekend nights. Because it had rained on the Friday and Saturday nights of the weekend involved here, Sunday was the only clear night of that weekend; the officers surmised it was therefore a likely night for a trip.</p>
<p>Once they had focused on that night, the officers drew upon other objective facts known to them to deduce a time frame <span class="star-pagination">*420</span> within which "Chevron" and the aliens were likely to arrive. From what they knew of the practice of those who smuggle aliens, including what they knew of "Chevron's" previous activities, they deduced that the border crossing and journey through the desert would probably be at night. They knew the time when sunset would occur at the point of the border crossing; they knew about how long the trip would take. They were thus able to deduce that "Chevron" would likely arrive at the pickup point on Highway 86 in the time frame between 2 a. m. and 6 a. m.</p>
<p>From objective facts, the officers also deduced the probable point on the highwaymilepost 122at which "Chevron" would likely rendezvous with a pickup vehicle. They deduced from the direction taken by the sets of "Chevron" footprints they had earlier discovered that the pickup vehicle would approach the aliens from, and return with them to, a point east of milepost 122. They therefore staked out a position east of milepost 122 (at milepost 149) and watched for vehicles that passed them going west and then, approximately one and a half hours later, passed them again, this time going east.</p>
<p>From what they had observed about the previous groups guided by the person with "chevron" shoes, they deduced that "Chevron" would lead a group of 8 to 20 aliens. They therefore focused their attention on enclosed vehicles of that passenger capacity.</p>
<p>The analysis produced by Officers Gray and Evans can be summarized as follows: if, on the night upon which they believed "Chevron" was likely to travel, sometime between 2 a. m. and 6 a. m., a large enclosed vehicle was seen to make an east-west-east round trip to and from a deserted point (milepost 122) on a deserted road (Highway 86), the officers would stop the vehicle on the return trip. In a 4-hour period the officers observed only one vehicle meeting that description. And it is not surprising that when they stopped the <span class="star-pagination">*421</span> vehicle on its return trip it contained "Chevron" and several illegal aliens.<sup>[3]</sup></p>
<p></p>
<h2>C</h2>
<p>The limited purpose of the stop in this case was to question the occupants of the vehicle about their citizenship and immigration status and the reasons for the round trip in a short timespan in a virtually deserted area. No search of the camper or any of its occupants occurred until after respondent Cortez voluntarily opened the back door of the camper; thus, only the stop, not the search is at issue here. The intrusion upon privacy associated with this stop was limited and was "reasonably related in scope to the justification for [its] initiation," <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 29</a></span>.</p>
<p>We have recently held that stops by the Border Patrol may be justified under circumstances less than those constituting probable cause for arrest or search. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 880</a></span>.<sup>[4]</sup> Thus, the test is not whether Officers Gray and Evans had probable cause to conclude that the vehicle they stopped would contain "Chevron" and a group of illegal aliens. Rather the question is whether, based upon the whole picture, they, as experienced Border Patrol officers, could reasonably surmise that the particular vehicle <span class="star-pagination">*422</span> they stopped was engaged in criminal activity. On this record, they could so conclude.</p>
<p><i>Reversed.</i></p>
<p>JUSTICE MARSHALL concurs in the judgment.</p> <p>JUSTICE MARSHALL concurs in the judgment.</p>
<p>JUSTICE STEWART, concurring in the result.</p>
<p>The Border Patrol officers in this case knew, or had rationally deduced, that "Chevron" had repeatedly shepherded illegal aliens up from the border; that his treks had commonly ended early in the morning around milepost 122 on Highway 86; that he usually worked on weekends; that he probably had made no trips for two weeks; and that trips were most likely when the weather was good. Knowing of this pattern, the officers could reasonably anticipate, even if they could not guarantee, the arrival of another group of aliens, led by Chevron, at milepost 122 on the first clear weekend night in late January 1977. Route 86 leads through almost uninhabited country, so little travelled in the hours of darkness that only 15 to 20 westbound vehicles passed the police during the five hours they watched that Sunday night. Only two vehicles capacious enough to carry a sizable group of illegal aliens went by. One of those two vehicles not only drove past them, but returned in the opposite direction after just enough time had elapsed for a journey to milepost 122 and back. This nocturnal round trip into "desolate desert terrain" would in any event have been puzzling. Coming when and as it did, surely the most likely explanation for it was that Chevron was again shepherding aliens.</p>
<p>In sum, the Border Patrol officers had discovered an abundance of "specific articulable facts" which, "together with rational inferences from [them]," entirely warranted a "suspicion that the vehicl[e] contain[ed] aliens who [might] be illegally in the country." <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="star-pagination">*423</span> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884</a></span>. Because the information possessed by the officers thus met the requirements established by the <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> case for the kind of stop made here, I concur in the reversal of the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[1]  The second camper passed them 15 or 20 minutes later. As far as the record shows, it did not return.</p>
<p>[2]  Of course, an officer may stop and question a person if there are reasonable grounds to believe that person is wanted for past criminal conduct.</p>
<p>[3]  In <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884-885</a></span> (1975), the Court listed several factors to be considered as part of the totality of the circumstances in determining the existence <i>vel non</i> of a particularized suspicion in cases treating official attempts to stem the influx of illegal aliens into our country. Though the list did not purport to be exhaustive, it is noteworthy that several of the factors present here were recognized by <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> as significant in this context; for example, information about recent border crossings and the type of vehicle involved.</p>
<p>[4]  The wide public interest in effective measures to prevents the entry of illegal aliens at the Mexican border has been cataloged by this Court. See, <i>e. g., </i><i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#899" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 899-914</a></span> (1975) (BURGER, C. J., concurring in judgment); <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878-879</a></span>.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Cotterman.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "United States v. Cotterman"
type: case
citation: "709 F.3d 952 (2013)"
parallel_cite: ""
neutral_cite: "2013 WL 856292; 2013 U.S. App. LEXIS 4731"
court: "U.S. Court of Appeals, 9th Circuit (en banc)"
court_level: coa
circuit: 9th
year: 2013
date_decided: 2013-03-08
docket: ""
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2013-03-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Cotterman
  varies_by_point: false
  scope_note: "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/854692/united-states-v-howard-cotterman/"
  cluster_id: 854692
  opinion_id: 854692
  identity_checked: false
homes:
  - page: "[[Border Searches]]"
    role: "Illustrates a circuit split"
related: ["[[United States v. Cano]]", "[[Riley v. California]]", "[[Carpenter v. United States]]"]
aliases: ["United States v. Howard Cotterman"]
tags: ["case", "fourth-amendment", "border-search", "digital-privacy"]
holding: "A forensic (comprehensive) examination of an electronic device seized at the border requires reasonable suspicion; it is the…"
lake:
  record_id: United States v. Cotterman
  status: under_review
  projected_at: 2026-07-06
---

# United States v. Cotterman

*709 F.3d 952 (9th Cir. 2013) (en banc)* · U.S. Court of Appeals, 9th Circuit (en banc) · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At the U.S.-Mexico border, agents flagged Cotterman based in part on a prior child-molestation conviction and conducted an initial manual review of his laptop, which turned up nothing. They then detained the laptop, shipped it roughly 170 miles to Tucson, and subjected it to a comprehensive forensic examination using software that recovered password-protected and deleted files — revealing child pornography. Cotterman moved to suppress.

## Issue
Whether a comprehensive forensic examination of an electronic device seized at the border requires reasonable suspicion, or whether it is a routine border search needing no suspicion.

## Rule
A forensic examination of a device requires reasonable suspicion, triggered by the search's intrusiveness rather than its location: "It is the comprehensive and intrusive nature of a forensic examination—not the location of the examination—that is the key factor triggering the requirement of reasonable suspicion here." — slip op., at 17. ^pin-op17

The [[Reading and Citing Cases#en-banc|en banc]] court accordingly held that the forensic examination of Cotterman's computer required a showing of reasonable suspicion — a modest requirement — distinguishing such a search from the routine, suspicionless manual inspection permitted at the border. (The follow-on examination was not an "extended border search," because the laptop never cleared customs.)

## Application
The forensic imaging and analysis of Cotterman's laptop — recovering hidden, encrypted, and deleted files and exposing the most intimate details of his digital life — was so comprehensive and intrusive that it required reasonable suspicion, regardless of being performed 170 miles inland. On the facts, the agents had reasonable suspicion (the prior conviction, a border-alert hit, and password-protected files), so the forensic search was reasonable and the child-pornography evidence was admissible; the suppression order was reversed.

## Conclusion
Forensic examination of a device seized at the border requires reasonable suspicion, which the agents had here; the suppression was reversed. The intrusiveness of a comprehensive forensic search — not where it occurs — is what triggers the reasonable-suspicion requirement.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.** Clarified by [[United States v. Cano]], which held that the "reasonable suspicion" *Cotterman* requires means suspicion that the device contains digital contraband and confined such searches to that purpose.
- *Cotterman* reflects the digital-privacy concerns later voiced by SCOTUS in [[Riley v. California]] and [[Carpenter v. United States]]; it anchors a circuit split — the Eleventh Circuit (*[[United States v. Touset]]*) requires no suspicion even for forensic border device searches.

## Appears on
- [[Border Searches]] — *Illustrates a circuit split*

## Sources
- *United States v. Cotterman*, 709 F.3d 952 (9th Cir. 2013) (en banc) — https://www.courtlistener.com/opinion/854692/united-states-v-howard-cotterman/ — pinpoint: slip op., at 17 (CL carries the slip opinion; cluster 854692).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d1decc040b637858", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Cotterman"}, "payload": {"all": [{"cite": "709 F.3d 952", "page": "952", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "709"}, {"cite": "2013 WL 856292", "page": "856292", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2013"}, {"cite": "2013 U.S. App. LEXIS 4731", "page": "4731", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}], "display": "709 F.3d 952", "official": {"cite": "709 F.3d 952", "page": "952", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "709"}, "official_selection_present": true, "record_id": "United States v. Cotterman"}}
{"assertion_id": "fe9ec475082aa33d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-op17", "record_id": "United States v. Cotterman"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-op17", "pinpoint_status": "slip-only", "quote": "--- # United States v. Cotterman *709 F.3d 952 (9th Cir. 2013) (en banc)* · U.S. Court of Appeals, 9th Circuit (en banc) · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the U.S.-Mexico border, agents flagged Cotterman based in part on a prior child-molestation conviction and conducted an initial manual review of his laptop, which turned up nothing. They then detained the laptop, shipped it roughly 170 miles to Tucson, and subjected it to a comprehensive forensic examination using software that recovered password-protected and deleted files — revealing child pornography. Cotterman moved to suppress. ## Issue Whether a comprehensive forensic examination of an electronic device seized at the border requires reasonable suspicion, or whether it is a routine border search needing no suspicion. ## Rule A forensic examination of a device requires reasonable suspicion, triggered by the search's intrusiveness rather than its location:", "quote_fidelity": "mismatch", "record_id": "United States v. Cotterman", "star_marker": null}}
{"assertion_id": "b22fa5b35117b7eb", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Cotterman"}, "payload": {"as_of_content": "2013-03-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Cotterman", "scope_note": "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset).", "varies_by_point": false}}
```

### lake record — United States v. Cotterman

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Cotterman",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Howard Cotterman",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Howard Wesley COTTERMAN, Defendant-Appellee",
    "input_case_name": "United States v. Cotterman",
    "court": "U.S. Court of Appeals, 9th Circuit (en banc)",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2013-03-08",
    "year": 2013,
    "docket": null,
    "cluster_id": 854692,
    "lead_opinion_id": 854692,
    "sibling_ids": [
      854692,
      9505756,
      9505757,
      9505758
    ],
    "absolute_url": "/opinion/854692/united-states-v-howard-cotterman/",
    "identity_method": "pending",
    "expected_citation_found": false,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "709 F.3d 952",
      "volume": "709",
      "reporter": "F.3d",
      "page": "952",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2013 WL 856292",
        "volume": "2013",
        "reporter": "WL",
        "page": "856292",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4731",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4731",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "709 F.3d 952",
        "volume": "709",
        "reporter": "F.3d",
        "page": "952",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 856292",
        "volume": "2013",
        "reporter": "WL",
        "page": "856292",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. App. LEXIS 4731",
        "volume": "2013",
        "reporter": "U.S. App. LEXIS",
        "page": "4731",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "709 F.3d 952",
    "official_selection": {
      "court_class": "coa",
      "selected": "709 F.3d 952",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op17",
      "page": null,
      "quote": "--- # United States v. Cotterman *709 F.3d 952 (9th Cir. 2013) (en banc)* \u00b7 U.S. Court of Appeals, 9th Circuit (en banc) \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At the U.S.-Mexico border, agents flagged Cotterman based in part on a prior child-molestation conviction and conducted an initial manual review of his laptop, which turned up nothing. They then detained the laptop, shipped it roughly 170 miles to Tucson, and subjected it to a comprehensive forensic examination using software that recovered password-protected and deleted files \u2014 revealing child pornography. Cotterman moved to suppress. ## Issue Whether a comprehensive forensic examination of an electronic device seized at the border requires reasonable suspicion, or whether it is a routine border search needing no suspicion. ## Rule A forensic examination of a device requires reasonable suspicion, triggered by the search's intrusiveness rather than its location:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-03-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Cotterman",
    "varies_by_point": false,
    "scope_note": "Good law in-circuit; later clarified by United States v. Cano (reasonable suspicion = suspicion of digital contraband) and part of a circuit split with the 11th Cir. (Touset).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Wurie",
          "cluster_id": 870435,
          "cite": [
            "728 F.3d 1",
            "2013 U.S. App. LEXIS 9937",
            "2013 WL 2129119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles Skaggs, Jr.",
          "cluster_id": 6247820,
          "cite": [
            "25 F.4th 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Haitao Xiang",
          "cluster_id": 9397097,
          "cite": [
            "67 F.4th 895"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fischer v SSA",
          "cluster_id": 10699387,
          "cite": [
            "2014 DNH 227"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abidor v. Napolitano",
          "cluster_id": 8730636,
          "cite": [
            "990 F. Supp. 2d 260",
            "2013 WL 6912654"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kitzhaber",
          "cluster_id": 8442802,
          "cite": [
            "828 F.3d 1083",
            "2016 WL 3745541"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524074,
          "cite": [
            "103 F.4th 1303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramos",
          "cluster_id": 7320653,
          "cite": [
            "190 F. Supp. 3d 992",
            "2016 U.S. Dist. LEXIS 73571",
            "2016 WL 3552140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Caballero",
          "cluster_id": 7319742,
          "cite": [
            "178 F. Supp. 3d 1008",
            "2016 U.S. Dist. LEXIS 51132",
            "2016 WL 1546731"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Phillips",
          "cluster_id": 7305585,
          "cite": [
            "9 F. Supp. 3d 1130",
            "2014 U.S. Dist. LEXIS 42294",
            "2014 WL 1275916"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lustig",
          "cluster_id": 7305087,
          "cite": [
            "3 F. Supp. 3d 808",
            "2014 WL 902502",
            "2014 U.S. Dist. LEXIS 31554"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4781994,
          "cite": [
            "973 F.3d 966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Javier Hernandez",
          "cluster_id": 10796167,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bejar-Guizar",
          "cluster_id": 10625883,
          "cite": [
            "142 F.4th 1188"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marcos Mendez",
          "cluster_id": 9524075,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Molina-Isidoro",
          "cluster_id": 7326797,
          "cite": [
            "267 F. Supp. 3d 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cano",
          "cluster_id": 7323106,
          "cite": [
            "222 F. Supp. 3d 876",
            "2016 WL 6920449",
            "2016 U.S. Dist. LEXIS 163675"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Saffarinia",
          "cluster_id": 4695910,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Cotterman:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      },
      "lane2_top_cited": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
        "reviewed": 19,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 18,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
        "reviewed": 4,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 4,
        "triage_read": 0,
        "triage_snippet_classified": 4
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(854692 OR 9505756 OR 9505757 OR 9505758)",
    "indexed_citing_opinions": 19,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 854692,
        "count": 8,
        "count_source": "search"
      },
      {
        "opinion_id": 9505756,
        "count": 11,
        "count_source": "search"
      },
      {
        "opinion_id": 9505757,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9505758,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 93,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-cotterman.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 19,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 854692,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 111635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 112877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 145768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 204312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 213651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 279144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 363605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 365925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 409244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 411245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 463360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 479793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 500701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 591454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 625692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 626454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 679542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 768288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 770213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 773999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 776810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 777177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 777268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 787918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 794720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 795398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 795859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1235958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1390224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1448376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1458074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 1589964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2246387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2538573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 854692,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 111635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 145640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 145768,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 204312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 213651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 363605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 409244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 411245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 479793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 500701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 591454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 625692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 678602,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 679542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 770213,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 773999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 777177,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 777268,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 787918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 795859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1235958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1390224,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 9426823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505756,
        "cited_id": 9430181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 112037,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 148280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 463360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 788904,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 791557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 792062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 795398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1448376,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 1448445,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 2538573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 2620876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 3052128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 9248165,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505757,
        "cited_id": 9434573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 110336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 111509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 112877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 134729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 183026,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 279144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 365925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 450644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 456285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 626454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 768288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 776460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 776810,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 777176,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 788746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 794720,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1225723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1234252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 1589964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 2246387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 3024820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9505758,
        "cited_id": 3037708,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "CU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T23:22:08Z",
    "date_modified": "2026-07-06T09:03:53Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:25:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:22:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Cotterman (truncated)

```
                     FOR PUBLICATION

     UNITED STATES COURT OF APPEALS
          FOR THE NINTH CIRCUIT

 UNITED STATES OF AMERICA ,                        No. 09-10139
                Plaintiff-Appellant,
                                                      D.C. No.
                      v.                           4:07-cr-01207-
                                                    RCC-CRP-1
 HOWARD WESLEY COTTERMAN ,
             Defendant-Appellee.                      OPINION

         Appeal from the United States District Court
                  for the District of Arizona
          Raner C. Collins, District Judge, Presiding

               Argued and Submitted En Banc
             June 19, 2012—Pasadena, California

                       Filed March 8, 2013

Before: Alex Kozinski, Chief Judge, Sidney R. Thomas, M.
Margaret McKeown, Kim McLane Wardlaw, Raymond C.
Fisher, Ronald M. Gould, Richard R. Clifton, Consuelo M.
   Callahan, Milan D. Smith, Jr., Mary H. Murguia, and
            Morgan Christen, Circuit Judges.1

              Opinion by Judge McKeown;
Partial Concurrence and Partial Dissent by Judge Callahan;
           Dissent by Judge Milan D. Smith, Jr.


 1
   Judge Betty B. Fletcher was a member of the en banc panel but passed
away after argument of the case. Judge W ardlaw was drawn as her
replacement.
2               UNITED STATES V . COTTERMAN

                           SUMMARY*


                           Criminal Law

    The en banc court reversed the district court’s order
suppressing evidence of child pornography obtained from a
forensic examination of the defendant’s laptop, which was
seized by agents at the U.S.-Mexico border in response to an
alert based in part on a prior conviction for child molestation.

     The en banc court explained that a border search of a
computer is not transformed into an “extended border search”
requiring particularized suspicion simply because the device
is transported and examined beyond the border. The en banc
court wrote that the fact that the forensic examination
occurred 170 miles away from the border did not heighten the
interference with the defendant’s privacy, and the extended
border search doctrine does not apply, in this case in which
the defendant’s computer never cleared customs and the
defendant never regained possession.

    The en banc court held that the forensic examination of
the defendant’s computer required a showing of reasonable
suspicion, a modest requirement in light of the Fourth
Amendment. The en banc court wrote that it is the
comprehensive and intrusive nature of forensic examination
– not the location of the examination – that is the key factor
triggering the requirement of reasonable suspicion here. The
en banc court wrote that the uniquely sensitive nature of data
on electronic devices, which often retain information far

  *
    This summary constitutes no part of the opinion of the court. It has
been prepared by court staff for the convenience of the reader.
              UNITED STATES V . COTTERMAN                    3

beyond the perceived point of erasure, carries with it a
significant expectation of privacy and thus renders an
exhaustive exploratory search more intrusive than with other
forms of property.

    The en banc court held that the border agents had
reasonable suspicion to conduct an initial search at the border
(which turned up no incriminating material) and the forensic
examination. The en banc court wrote that the defendant’s
Treasury Enforcement Communication System alert, prior
child-related conviction, frequent travels, crossing from a
country known for sex tourism, and collection of electronic
equipment, plus the parameters of the Operation Angel Watch
program aimed at combating child sex tourism, taken
collectively, gave rise to reasonable suspicion of criminal
activity.

    The en banc court wrote that password protection of files,
which is ubiquitous among many law-abiding citizens, will
not in isolation give rise to reasonable suspicion, but that
password protection may be considered in the totality of the
circumstances where, as here, there are other indicia of
criminal activity. The en banc court wrote that the existence
of password-protected files is also relevant to assessing the
reasonableness of the scope and duration of the search of the
defendant’s computer.

    The en banc court concluded that the examination of the
defendant’s electronic devices was supported by reasonable
suspicion and that the scope and manner of the search were
reasonable under the Fourth Amendment.

    Concurring in part, dissenting in part, and concurring in
the judgment, Judge Callahan (with whom Judge Clifton
4              UNITED STATES V . COTTERMAN

joined and with whom Judge M. Smith joined as to all but
Part II.A) wrote that the majority’s new rule requiring
reasonable suspicion for any thorough search of electronic
devices entering the United States flouts more than a century
of Supreme Court precedent, is unworkable and unnecessary,
and will severely hamstring the government’s ability to
protect our borders.

     Judge M. Smith (with whom Judges Clifton and Callahan
joined with respect to Part I) dissented. Judge Smith wrote
that the majority’s decision to create a reasonable suspicion
requirement for some property searches at the border so
muddies current border search doctrine that border agents will
be left to divine on an ad hoc basis whether a property search
is sufficiently “comprehensive and intrusive” to require
suspicion, or sufficiently “unintrusive” to come within the
traditional border search exception. Judge Smith also wrote
that the majority’s determination that reasonable suspicion
exists under the exceedingly weak facts of this case
undermines the liberties of U.S. citizens generally – not just
at the border, and not just with regard to our digital data – but
on every street corner, in every vehicle, and wherever else we
rely on the doctrine of reasonable suspicion to safeguard our
legitimate privacy interests.
              UNITED STATES V . COTTERMAN                 5

                       COUNSEL

Dennis K. Burke, Christina M. Cabanillas, Carmen F. Corbin,
John S. Leonardo, John J. Tuchi, United States Attorney’s
Office for the District of Arizona, Tucson, Arizona, for
Appellant.

William J. Kirchner, Law Office of Nash & Kirchner, P.C.,
Tucson, Arizona, for Appellee.

David M. Porter, Malia N. Brink, National Association of
Criminal Defense Lawyers, Washington, D.C.; Michael Price,
Brennan Center for Justice, New York, New York; Hanni M.
Fakhoury, Electronic Frontier Foundation, San Francisco,
California, for Amicus Curiae National Association of
Criminal Defense Lawyers and Electronic Frontier
Foundation.

Christopher T. Handman, Mary Helen Wimberly, Hogan
Lovells US LLP, Washington, D.C.; Sharon Bradford
Franklin, The Constitution Project, Washington, D.C., for
Amicus Curiae The Constitution Project.


                        OPINION

McKEOWN, Circuit Judge:

    Every day more than a million people cross American
borders, from the physical borders with Mexico and Canada
to functional borders at airports such as Los Angeles (LAX),
Honolulu (HNL), New York (JFK, LGA), and Chicago
(ORD, MDW). As denizens of a digital world, they carry
with them laptop computers, iPhones, iPads, iPods, Kindles,
6             UNITED STATES V . COTTERMAN

Nooks, Surfaces, tablets, Blackberries, cell phones, digital
cameras, and more. These devices often contain private and
sensitive information ranging from personal, financial, and
medical data to corporate trade secrets. And, in the case of
Howard Cotterman, child pornography.

    Agents seized Cotterman’s laptop at the U.S.-Mexico
border in response to an alert based in part on a fifteen-year-
old conviction for child molestation. The initial search at the
border turned up no incriminating material. Only after
Cotterman’s laptop was shipped almost 170 miles away and
subjected to a comprehensive forensic examination were
images of child pornography discovered.

    This watershed case implicates both the scope of the
narrow border search exception to the Fourth Amendment’s
warrant requirement and privacy rights in commonly used
electronic devices. The question we confront “is what limits
there are upon this power of technology to shrink the realm
of guaranteed privacy.” Kyllo v. United States, 533 U.S. 27,
34 (2001). More specifically, we consider the reasonableness
of a computer search that began as a cursory review at the
border but transformed into a forensic examination of
Cotterman’s hard drive.

    Computer forensic examination is a powerful tool capable
of unlocking password-protected files, restoring deleted
material, and retrieving images viewed on web sites. But
while technology may have changed the expectation of
privacy to some degree, it has not eviscerated it, and certainly
not with respect to the gigabytes of data regularly maintained
as private and confidential on digital devices. Our Founders
were indeed prescient in specifically incorporating “papers”
within the Fourth Amendment’s guarantee of “[t]he right of
                UNITED STATES V . COTTERMAN                          7

the people to be secure in their persons, houses, papers, and
effects.” U.S. Const. amend. IV. The papers we create and
maintain not only in physical but also in digital form reflect
our most private thoughts and activities.

    Although courts have long recognized that border
searches constitute a “historically recognized exception to the
Fourth Amendment’s general principle that a warrant be
obtained,” United States v. Ramsey, 431 U.S. 606, 621
(1977), reasonableness remains the touchstone for a
warrantless search. Even at the border, we have rejected an
“anything goes” approach. See United States v. Seljan,
547 F.3d 993, 1000 (9th Cir. 2008) (en banc).

    Mindful of the heavy burden on law enforcement to
protect our borders juxtaposed with individual privacy
interests in data on portable digital devices, we conclude that,
under the circumstances here, reasonable suspicion was
required for the forensic examination of Cotterman’s laptop.
Because border agents had such a reasonable suspicion, we
reverse the district court’s order granting Cotterman’s motion
to suppress the evidence of child pornography obtained from
his laptop.

I. FACTUAL BACKGROUND AND PROCEDURAL HISTORY 2

    Howard Cotterman and his wife were driving home to the
United States from a vacation in Mexico on Friday morning,
April 6, 2007, when they reached the Lukeville, Arizona, Port
of Entry. During primary inspection by a border agent, the



  2
    The facts related here are drawn from the record of the evidentiary
hearing held before the magistrate judge.
8                UNITED STATES V . COTTERMAN

Treasury Enforcement Communication System (“TECS”)3
returned a hit for Cotterman. The TECS hit indicated that
Cotterman was a sex offender—he had a 1992 conviction for
two counts of use of a minor in sexual conduct, two counts of
lewd and lascivious conduct upon a child, and three counts of
child molestation—and that he was potentially involved in
child sex tourism. Because of the hit, Cotterman and his wife
were referred to secondary inspection, where they were
instructed to exit their vehicle and leave all their belongings
in the car. The border agents called the contact person listed
in the TECS entry and, following that conversation, believed
the hit to reflect Cotterman’s involvement “in some type of
child pornography.” The agents searched the vehicle and
retrieved two laptop computers and three digital cameras.
Officer Antonio Alvarado inspected the electronic devices
and found what appeared to be family and other personal
photos, along with several password-protected files.

     Border agents contacted Group Supervisor Craig Brisbine
at the Immigration and Customs Enforcement (“ICE”) office
in Sells, Arizona, and informed him about Cotterman’s entry
and the fact that he was a sex offender potentially involved in
child sex tourism. The Sells Duty Agent, Mina Riley, also
spoke with Officer Alvarado and then contacted the ICE
Pacific Field Intelligence Unit, the office listed on the TECS
hit, to get more information. That unit informed Riley that
the alert was part of Operation Angel Watch, which was
aimed at combating child sex tourism by identifying
registered sex offenders in California, particularly those who
travel frequently outside the United States. She was advised


    3
    The TECS is an investigative tool of the Department of Homeland
Security that keeps track of individuals entering and exiting the country
and of individuals involved in or suspected to be involved in crimes.
                  UNITED STATES V . COTTERMAN                 9

to review any media equipment, such as computers, cameras,
or other electronic devices, for potential evidence of child
pornography. Riley then spoke again to Alvarado, who told
her that he had been able to review some of the photographs
on the Cottermans’ computers but had encountered password-
protected files that he was unable to access.

    Agents Brisbine and Riley departed Sells for Lukeville at
about 1:30 p.m. and decided en route to detain the
Cottermans’ laptops for forensic examination. Upon their
arrival, they gave Cotterman and his wife Miranda warnings
and interviewed them separately. The interviews revealed
nothing incriminating. During the interview, Cotterman
offered to help the agents access his computer. The agents
declined the offer out of concern that Cotterman might be
able to delete files surreptitiously or that the laptop might be
“booby trapped.”

    The agents allowed the Cottermans to leave the border
crossing around 6 p.m., but retained the Cottermans’ laptops
and a digital camera.4 Agent Brisbine drove almost 170 miles
from Lukeville to the ICE office in Tucson, Arizona, where
he delivered both laptops and one of the three digital cameras
to ICE Senior Special Agent & Computer Forensic Examiner
John Owen. Agent Owen began his examination on Saturday,
the following day. He used a forensic program to copy the
hard drives of the electronic devices. He determined that the
digital camera did not contain any contraband and released
the camera that day to the Cottermans, who had traveled to
Tucson from Lukeville and planned to stay there a few days.
Agent Owen then used forensic software that often must run
for several hours to examine copies of the laptop hard drives.

 4
     The other two cameras were returned to the Cottermans.
10               UNITED STATES V . COTTERMAN

He began his personal examination of the laptops on Sunday.
That evening, Agent Owen found seventy-five images of
child pornography within the unallocated space of
Cotterman’s laptop.5

    Agent Owen contacted the Cottermans on Sunday evening
and told them he would need Howard Cotterman’s assistance
to access password-protected files he found on Cotterman’s
laptop. Cotterman agreed to provide the assistance the
following day, but never showed up. When Agent Brisbine
called again to request Cotterman’s help in accessing the
password-protected files, Cotterman responded that the
computer had multiple users and that he would need to check
with individuals at the company from which he had retired in
order to get the passwords. The agents had no further contact
with Cotterman, who boarded a flight to Mexico from Tucson
the next day, April 9, and then flew onward to Sydney,
Australia. On April 11, Agent Owen finally managed to open
twenty-three password-protected files on Cotterman’s laptop.
The files revealed approximately 378 images of child
pornography. The vast majority of the images were of the
same girl, approximately 7–10 years of age, taken over a two-
to three-year period. In many of the images, Cotterman was
sexually molesting the child. Over the next few months,
Agent Owen discovered hundreds more pornographic images,
stories, and videos depicting children.




 5
   “Unallocated space is space on a hard drive that contains deleted data,
usually emptied from the operating system’s trash or recycle bin folder,
that cannot be seen or accessed by the user without the use of forensic
software. Such space is available to be written over to store new
information.” United States v. Flyer, 633 F.3d 911, 918 (9th Cir. 2011).
              UNITED STATES V . COTTERMAN                    11

    A grand jury indicted Cotterman for a host of offenses
related to child pornography. Cotterman moved to suppress
the evidence gathered from his laptop and the fruits of that
evidence. The magistrate judge filed a Report and
Recommendation finding that the forensic examination was
an “extended border search” that required reasonable
suspicion. He found that the TECS hit and the existence of
password-protected files on Cotterman’s laptop were
suspicious, but concluded that those facts did not suffice to
give rise to reasonable suspicion of criminal activity. The
district judge adopted the Report and Recommendation and
granted Cotterman’s motion to suppress.

    In its interlocutory appeal of that order, the government
characterized the issue as follows: “Whether the authority to
search a laptop computer without reasonable suspicion at a
border point of entry permits law enforcement to take it to
another location to be forensically examined, when it has
remained in the continuous custody of the government.” A
divided panel of this court answered that question in the
affirmative and reversed. United States v. Cotterman,
637 F.3d 1068 (9th Cir. 2011). The panel concluded that
reasonable suspicion was not required for the search and that
“[t]he district court erred in suppressing the evidence lawfully
obtained under border search authority.” Id. at 1084. In
dissent, Judge Betty B. Fletcher wrote that “officers must
have some level of particularized suspicion in order to
conduct a seizure and search like the one at issue here.” Id.
(B. Fletcher, J., dissenting). By a vote of a majority of
nonrecused active judges, rehearing en banc was ordered.
673 F.3d 1206 (9th Cir. 2012). Following en banc oral
argument, we requested supplemental briefing on the issue of
whether reasonable suspicion existed at the time of the
search.
12            UNITED STATES V . COTTERMAN

II. WAIVER

    The government argued below that the forensic
examination was part of a routine border search not requiring
heightened suspicion and, alternatively, that reasonable
suspicion justified the search. Before the district court, the
government maintained “the facts of this case clearly
establish that there was reasonable suspicion.” However,
having failed to obtain a favorable ruling on that ground, the
government did not challenge on appeal the conclusion that
there was no reasonable suspicion. Rather, it sought a broad
ruling that no suspicion of any kind was required. Cotterman
thus argued in his answering brief that the government had
waived the issue—an assertion that the government did not
address in its reply brief. Cotterman contends that the
government has abandoned and conceded the issue of
reasonable suspicion and that this court may not address that
issue. We disagree.

    We review de novo the ultimate question of whether a
warrantless search was reasonable under the Fourth
Amendment. United States v. Johnson, 256 F.3d 895, 905
(9th Cir. 2001) (en banc).         Our review necessarily
encompasses a determination as to the applicable standard: no
suspicion, reasonable suspicion or probable cause. That the
government may hope for the lowest standard does not alter
our de novo review, particularly when the issue was fully
briefed and argued below. Further, we may consider an issue
that has not been adequately raised on appeal if such a failure
will not prejudice the opposing party. United States v. Ullah,
976 F.2d 509, 514 (9th Cir. 1992). Where, as here, we
“called for and received supplemental briefs by both parties,”
Alcarez v. INS, 384 F.3d 1150, 1161 (9th Cir. 2004), the
government’s failure to address the issue does not prejudice
               UNITED STATES V . COTTERMAN                     13

Cotterman. See also United States v. Resendiz-Ponce,
549 U.S. 102, 103–04 (2007).

III.    THE BORDER SEARCH

    The broad contours of the scope of searches at our
international borders are rooted in “the long-standing right of
the sovereign to protect itself by stopping and examining
persons and property crossing into this country.” Ramsey,
431 U.S. at 616. Thus, border searches form “a narrow
exception to the Fourth Amendment prohibition against
warrantless searches without probable cause.” Seljan,
547 F.3d at 999 (internal quotation marks and citation
omitted). Because “[t]he Government’s interest in preventing
the entry of unwanted persons and effects is at its zenith at the
international border,” United States v. Flores-Montano,
541 U.S. 149, 152 (2004), border searches are generally
deemed “reasonable simply by virtue of the fact that they
occur at the border.” Ramsey, 431 U.S. at 616.

    This does not mean, however, that at the border “anything
goes.” Seljan, 547 F.3d at 1000. Even at the border,
individual privacy rights are not abandoned but “[b]alanced
against the sovereign’s interests.” United States v. Montoya
de Hernandez, 473 U.S. 531, 539 (1985). That balance “is
qualitatively different . . . than in the interior” and is “struck
much more favorably to the Government.” Id. at 538, 540.
Nonetheless, the touchstone of the Fourth Amendment
analysis remains reasonableness.            Id. at 538.        The
reasonableness of a search or seizure depends on the totality
of the circumstances, including the scope and duration of the
deprivation. See United States v. Jacobsen, 466 U.S. 109,
124 (1984); see also United States v. Duncan, 693 F.2d 971,
977 (9th Cir. 1982).
14               UNITED STATES V . COTTERMAN

    In view of these principles, the legitimacy of the initial
search of Cotterman’s electronic devices at the border is not
in doubt. Officer Alvarado turned on the devices and opened
and viewed image files while the Cottermans waited to enter
the country. It was, in principle, akin to the search in Seljan,
where we concluded that a suspicionless cursory scan of a
package in international transit was not unreasonable.
547 F.3d at 1004. Similarly, we have approved a quick look
and unintrusive search of laptops. United States v. Arnold,
533 F.3d 1003, 1009 (9th Cir. 2008) (holding border search
reasonable where “CBP officers simply ‘had [traveler] boot
[the laptop] up, and looked at what [he] had inside.’”) (second
alteration in original).6 Had the search of Cotterman’s laptop
ended with Officer Alvarado, we would be inclined to
conclude it was reasonable even without particularized
suspicion. See id. But the search here transformed into
something far different. The difficult question we confront is
the reasonableness, without a warrant, of the forensic
examination that comprehensively analyzed the hard drive of
the computer.

     A. The Forensic Examination Was Not An Extended
        Border Search

    Cotterman urges us to treat the examination as an
extended border search that requires particularized suspicion.

 6
   Although the Arnold decision expressed its conclusion in broad terms,
stating that, “reasonable suspicion is not needed for customs officials to
search a laptop or other personal electronic storage devices at the border,”
Arnold, 533 F.3d at 1008, the facts do not support such an unbounded
holding. As an en banc court, we narrow Arnold to approve only the
relatively simple search at issue in that case, not to countenance
suspicionless forensic examinations. The dissent’s extensive reliance on
Arnold is misplaced in the en banc environment.
              UNITED STATES V . COTTERMAN                    15

Although the semantic moniker “extended border search”
may at first blush seem applicable here, our jurisprudence
does not support such a claim. We have “define[d] an
extended border search as any search away from the border
where entry is not apparent, but where the dual requirements
of reasonable certainty of a recent border crossing and
reasonable suspicion of criminal activity are satisfied.”
United States v. Guzman-Padilla, 573 F.3d 865, 878–79 (9th
Cir. 2009) (internal quotation marks and citations omitted).
The key feature of an extended border search is that an
individual can be assumed to have cleared the border and thus
regained an expectation of privacy in accompanying
belongings. See United States v. Abbouchi, 502 F.3d 850,
855 (9th Cir. 2007) (“Because the delayed nature of an
extended border search . . . necessarily entails a greater level
of intrusion on legitimate expectations of privacy than an
ordinary border search, the government must justify an
extended border search with reasonable suspicion that the
search may uncover contraband or evidence of criminal
activity.”) (internal quotation marks omitted) (emphasis
added).

    Cotterman’s case is different. Cotterman was stopped and
searched at the border. Although he was allowed to depart
the border inspection station after the initial search, some of
his belongings, including his laptop, were not. The follow-on
forensic examination was not an “extended border search.”
A border search of a computer is not transformed into an
extended border search simply because the device is
transported and examined beyond the border.

    To be sure, our case law has not always articulated the
“extended border search” doctrine with optimal clarity. But
the confusion has come in distinguishing between facts
16               UNITED STATES V . COTTERMAN

describing a functional border search and those describing an
extended border search, not in defining the standard for a
search at the border. See, e.g., United States v. Cardona,
769 F.2d 625, 628 (9th Cir. 1985) (“We have recently
recognized the difficulty of making sharp distinctions
between searches at the functional equivalent of the border
and extended border searches.”). The “functional equivalent”
doctrine effectively extends the border search doctrine to all
ports of entry, including airports. See Almeida-Sanchez v.
United States, 413 U.S. 266, 273 (1973). A routine customs
search at the “functional equivalent” of the border is
“analyzed as a border search” and requires neither probable
cause nor reasonable suspicion. Seljan, 547 F.3d at 999.
This case involves a search initiated at the actual border and
does not encounter any of the difficulties surrounding
identification of a “functional” border. As to the extended
border search doctrine, we believe it is best confined to cases
in which, after an apparent border crossing or functional
entry, an attenuation in the time or the location of conducting
a search reflects that the subject has regained an expectation
of privacy.7

    In his dissent, Judge Smith advocates applying the
extended border search doctrine because the forensic
examination occurred 170 miles from the border and days
after Cotterman’s entry. Moving the laptop to a specialized

 7
   This characterization is consistent with how our circuit and others have
articulated the doctrine. See, e.g., United States v. Villasenor, 608 F.3d
467, 471–72 (9th Cir. 2010); United States v. Yang, 286 F.3d 940, 945–46
(7th Cir. 2002); United States v. Hyde, 37 F.3d 116, 120 n.2 (3d Cir.
1994); United States v. Santiago, 837 F.2d 1545, 1548 (11th Cir. 1988);
United States v. Gaviria, 805 F.2d 1108, 1112 (2d Cir. 1986); United
States v. Niver, 689 F.2d 520, 526 (5th Cir. 1982); United States v. Bilir,
592 F.2d 735, 739–40 (4th Cir. 1979).
                 UNITED STATES V . COTTERMAN                         17

lab at a distant location might highlight that the search
undertaken there was an extensive one, but it is not the
dispositive factor here. Because Cotterman never regained
possession of his laptop, the fact that the forensic
examination occurred away from the border, in Tucson, did
not heighten the interference with his privacy. Time and
distance become relevant to determining whether there is an
adequate nexus to a recent border crossing only after the
subject or items searched have entered. See Villasenor,
608 F.3d at 471 (explaining that reasonableness of extended
border search depends on “whether the totality of the
surrounding circumstances, including the time and distance
elapsed” establish that items to be searched have recently
entered the country) (internal quotation marks omitted).
Cotterman’s computer never cleared customs so entry was
never effected. In short, the extended border search doctrine
does not fit the search here.

     B. Forensic Examination At The Border Requires
        Reasonable Suspicion

    It is the comprehensive and intrusive nature of a forensic
examination—not the location of the examination—that is the
key factor triggering the requirement of reasonable suspicion
here.8 See Cotterman, 637 F.3d at 1086–87 n.6 (B. Fletcher,
J., dissenting) (recognizing that “[a] computer search in a
forensic lab will always be equivalent to an identical search
at the border. The duration of a computer search is not


 8
   The concurrence goes to great lengths to “refute any such notion” that
location and duration contributed to our holding reasonable suspicion
required here. Concurrence at 40–43. W e see no reason for such an
exegesis; our opinion is clear on the point that these factors are not at
issue.
18               UNITED STATES V . COTTERMAN

controlled by where the search is conducted. The duration of
a computer search is controlled by what one is looking for
and how one goes about searching for it.”) (emphasis in
original). The search would have been every bit as intrusive
had Agent Owen traveled to the border with his forensic
equipment. Indeed, Agent Owen had a laptop with forensic
software that he could have used to conduct an examination
at the port of entry itself, although he testified it would have
been a more time-consuming effort. To carry out the
examination of Cotterman’s laptop, Agent Owen used
computer forensic software to copy the hard drive and then
analyze it in its entirety, including data that ostensibly had
been deleted. This painstaking analysis is akin to reading a
diary line by line looking for mention of criminal
activity—plus looking at everything the writer may have
erased.9

    Notwithstanding a traveler’s diminished expectation of
privacy at the border, the search is still measured against the
Fourth Amendment’s reasonableness requirement, which
considers the nature and scope of the search. Significantly,
the Supreme Court has recognized that the “dignity and
privacy interests of the person being searched” at the border
will on occasion demand “some level of suspicion in the case
of highly intrusive searches of the person.” Flores-Montano,
541 U.S. at 152. Likewise, the Court has explained that
“some searches of property are so destructive,” “particularly
offensive,” or overly intrusive in the manner in which they


 9
   Agent Owen used a software program called EnCase that exhibited the
distinctive features of computer forensic examination. The program
copied, analyzed, and preserved the data stored on the hard drive and gave
the examiner access to far more data, including password-protected,
hidden or encrypted, and deleted files, than a manual user could access.
              UNITED STATES V . COTTERMAN                   19

are carried out as to require particularized suspicion. Id. at
152, 154 n.2, 155–56; Montoya de Hernandez, 473 U.S. at
541. The Court has never defined the precise dimensions of
a reasonable border search, instead pointing to the necessity
of a case-by-case analysis. As we have emphasized,
“[r]easonableness, when used in the context of a border
search, is incapable of comprehensive definition or of
mechanical application.” Duncan, 693 F.2d at 977 (internal
quotation marks and citation omitted).

    Over the past 30-plus years, the Supreme Court has dealt
with a handful of border cases in which it reaffirmed the
border search exception while, at the same time, leaving open
the question of when a “particularly offensive” search might
fail the reasonableness test. The trail begins with United
States v. Ramsey, where the Court reserved judgment on this
question: “We do not decide whether, and under what
circumstances, a border search might be deemed
‘unreasonable’ because of the particularly offensive manner
in which it is carried out.” 431 U.S. at 618 n.13. Of note, the
Court cited two cases, albeit non-border cases, as examples:
Kremen v. United States, 353 U.S. 346, 347–48 (1957)
(holding unconstitutional an exhaustive warrantless search of
a cabin and seizure of its entire contents that were moved 200
miles away for examination) and Go-Bart Importing Co. v.
United States, 282 U.S. 344, 358 (1931) (condemning as
“lawless invasion of the premises and a general exploratory
search” a warrantless “unlimited search, ransacking the desk,
safe, filing cases and other parts of [an] office”).

    Less than ten years later, in 1985, the Court observed that
it had “not previously decided what level of suspicion would
justify a seizure of an incoming traveler for purposes other
than a routine border search” and then went on to hold in the
20            UNITED STATES V . COTTERMAN

context of an alimentary canal search that reasonable
suspicion was required for “the detention of a traveler at the
border, beyond the scope of a routine customs search and
inspection.” Montoya de Hernandez, 473 U.S. at 540–41.
The Court’s reference to “routine border search” was parsed
in a later case, Flores-Montano, where the Court explained
that “the reasons that might support a requirement of some
level of suspicion in the case of highly intrusive searches of
the person—dignity and privacy interests of the person being
searched—simply do not carry over to vehicles,” and, more
specifically, to the gas tank of a car. 541 U.S. at 152.
Accordingly, the Court rejected a privacy claim vis-a-vis an
automobile gas tank.

    We are now presented with a case directly implicating
substantial personal privacy interests.           The private
information individuals store on digital devices—their
personal “papers” in the words of the Constitution—stands in
stark contrast to the generic and impersonal contents of a gas
tank. See, e.g., United States v. Jones, 132 S. Ct. 945, 957
(2012) (Sotomayor, J., concurring) (expressing “doubt that
people would accept without complaint the warrantless
disclosure to the Government of a list of every Web site they
had visited in the last week, or month, or year”). We rest our
analysis on the reasonableness of this search, paying
particular heed to the nature of the electronic devices and the
attendant expectation of privacy.

    The amount of private information carried by
international travelers was traditionally circumscribed by the
size of the traveler’s luggage or automobile. That is no
longer the case. Electronic devices are capable of storing
warehouses full of information. The average 400-gigabyte
laptop hard drive can store over 200 million pages—the
                 UNITED STATES V . COTTERMAN                          21

equivalent of five floors of a typical academic library. See
Orin S. Kerr, Searches and Seizures in a Digital World,
119 Harv. L. Rev. 531, 542 (2005) (explaining that an 80 GB
hard drive is equivalent to 40 million pages or one floor of an
academic library); see also LexisNexis, How Many Pages in
a Gigabyte?, http://www.lexisnexis.com/applieddiscovery/
lawlibrary/whitePapers/ADI_FS_PagesInAGigabyte.pdf.
Even a car full of packed suitcases with sensitive documents
cannot hold a candle to the sheer, and ever-increasing,
capacity of digital storage.10

    The nature of the contents of electronic devices differs
from that of luggage as well. Laptop computers, iPads and
the like are simultaneously offices and personal diaries. They
contain the most intimate details of our lives: financial
records, confidential business documents, medical records
and private emails. This type of material implicates the
Fourth Amendment’s specific guarantee of the people’s right
to be secure in their “papers.” U.S. Const. amend. IV. The
express listing of papers “reflects the Founders’ deep concern
with safeguarding the privacy of thoughts and ideas—what
we might call freedom of conscience—from invasion by the
government.” Seljan, 547 F.3d at 1014 (Kozinski, C.J.,
dissenting); see also New York v. P.J. Video, Inc., 475 U.S.
868, 873 (1986). These records are expected to be kept


   10
      W e are puzzled by the dissent’s speculation about “how many
gigabytes of storage [one must] buy to secure the guarantee that
reasonable suspicion will be required before one’s devices are searched.”
Dissent at 68. We discuss the typical storage capacity of electronic
devices simply to highlight the features that generally distinguish them
from traditional baggage. Indeed, we do not and need not determine
whether Cotterman’s laptop possessed unusually large or simply
“average” capacity in order to resolve that the forensic examination of it
required reasonable suspicion.
22               UNITED STATES V . COTTERMAN

private and this expectation is “one that society is prepared to
recognize as ‘reasonable.’” Katz v. United States, 389 U.S.
347, 361 (1967) (Harlan, J., concurring).11

     Electronic devices often retain sensitive and confidential
information far beyond the perceived point of erasure,
notably in the form of browsing histories and records of
deleted files. This quality makes it impractical, if not
impossible, for individuals to make meaningful decisions
regarding what digital content to expose to the scrutiny that
accompanies international travel. A person’s digital life
ought not be hijacked simply by crossing a border. When
packing traditional luggage, one is accustomed to deciding
what papers to take and what to leave behind. When carrying
a laptop, tablet or other device, however, removing files
unnecessary to an impending trip is an impractical solution
given the volume and often intermingled nature of the files.
It is also a time-consuming task that may not even effectively
erase the files.

    The present case illustrates this unique aspect of
electronic data. Agents found incriminating files in the
unallocated space of Cotterman’s laptop, the space where the
computer stores files that the user ostensibly deleted and
maintains other “deleted” files retrieved from web sites the
user has visited. Notwithstanding the attempted erasure of
material or the transient nature of a visit to a web site,

  11
    The dissent’s discussion about Facebook and other platforms where
the user voluntarily transmits personal data over the Internet, often
oblivious to privacy issues, Dissent at 65–66, is a red herring. Of course,
willful disclosure of electronic data, like disclosure of other material,
undercuts an individual’s expectation of privacy. But there was no such
disclosure here. Nor does the border search implicate such an affirmative
disclosure.
                  UNITED STATES V . COTTERMAN                            23

computer forensic examination was able to restore the files.
It is as if a search of a person’s suitcase could reveal not only
what the bag contained on the current trip, but everything it
had ever carried.

    With the ubiquity of cloud computing, the government’s
reach into private data becomes even more problematic.12 In
the “cloud,” a user’s data, including the same kind of highly
sensitive data one would have in “papers” at home, is held on
remote servers rather than on the device itself. The digital
device is a conduit to retrieving information from the cloud,
akin to the key to a safe deposit box. Notably, although the
virtual “safe deposit box” does not itself cross the border, it
may appear as a seamless part of the digital device when
presented at the border. With access to the cloud through
forensic examination, a traveler’s cache is just a click away
from the government.

    As Justice Scalia wrote, “It would be foolish to contend
that the degree of privacy secured to citizens by the Fourth
Amendment has been entirely unaffected by the advance of
technology.” Kyllo, 533 U.S. at 33–34. Technology has the
dual and conflicting capability to decrease privacy and
augment the expectation of privacy. While the thermal
imaging device in Kyllo threatened to expose the hour at


  12
     “The term ‘cloud computing’ is based on the industry usage of a cloud
as a metaphor for the ethereal internet. . . . An external cloud platform is
storage or software access that is essentially rented from (or outsourced to)
a remote public cloud service provider, such as Amazon or Google. . . .
By contrast, an internal or private cloud is a cluster of servers that is
networked behind an individual or company’s own firewall.” David A.
Couillard, Defogging the Cloud: Applying Fourth Amendment Principles
to Evolving Privacy Expectations in Cloud Computing, 93 Minn. L. Rev.
2205, 2216 (2009) (internal citations omitted).
24              UNITED STATES V . COTTERMAN

which “the lady of the house” took her daily “sauna and
bath,” id. at 38, digital devices allow us to carry the very
papers we once stored at home.

    The point is technology matters. The Department of
Homeland Security has acknowledged as much in the context
of international travelers:

        Where someone may not feel that the
        inspection of a briefcase would raise
        significant privacy concerns because the
        volume of information to be searched is not
        great, that same person may feel that a search
        of their laptop increases the possibility of
        privacy risks due to the vast amount of
        information potentially available on electronic
        devices.

DHS, Privacy Impact Assessment for the Border Searches of
Electronic Devices 2 (Aug. 25, 2009), available at
h t t p : / / w w w . d hs.gov/ x li brary/ ass e t s / p r i v a c y
/privacy_pia_cbp_laptop.pdf.

     This is not to say that simply because electronic devices
house sensitive, private information they are off limits at the
border. The relevant inquiry, as always, is one of
reasonableness. But that reasonableness determination must
account for differences in property. See Samson v.
California, 547 U.S. 843, 848 (2006) (“Under our general
Fourth Amendment approach, we examine the totality of the
circumstances to determine whether a search is reasonable
. . . .”) (internal quotation marks, citation, and alterations
omitted) (emphasis added). Unlike searches involving a
reassembled gas tank, Flores-Montano, 541 U.S. at 150, or
              UNITED STATES V . COTTERMAN                    25

small hole in the bed of a pickup truck, United States v.
Chaudhry, 424 F.3d 1051, 1054 (9th Cir. 2005), which have
minimal or no impact beyond the search itself—and little
implication for an individual’s dignity and privacy
interests—the exposure of confidential and personal
information has permanence.           It cannot be undone.
Accordingly, the uniquely sensitive nature of data on
electronic devices carries with it a significant expectation of
privacy and thus renders an exhaustive exploratory search
more intrusive than with other forms of property.

    After their initial search at the border, customs agents
made copies of the hard drives and performed forensic
evaluations of the computers that took days to turn up
contraband. It was essentially a computer strip search. An
exhaustive forensic search of a copied laptop hard drive
intrudes upon privacy and dignity interests to a far greater
degree than a cursory search at the border. It is little comfort
to assume that the government—for now—does not have the
time or resources to seize and search the millions of devices
that accompany the millions of travelers who cross our
borders. It is the potential unfettered dragnet effect that is
troublesome.

     We recognize the important security concerns that prevail
at the border. The government’s authority to protect the
nation from contraband is well established and may be
“heightened” by “national cris[e]s,” such as the smuggling of
illicit narcotics, Montoya de Hernandez, 473 U.S. at 538, the
current threat of international terrorism and future threats yet
to take shape. But even in the face of heightened concerns,
we must account for the Fourth Amendments rights of
travelers. Id. at 539.
26                UNITED STATES V . COTTERMAN

    The effort to interdict child pornography is also a
legitimate one. But legitimate concerns about child
pornography do not justify unfettered crime-fighting searches
or an unregulated assault on citizens’ private information.
Reasonable suspicion is a modest, workable standard that is
already applied in the extended border search, Terry stop,13
and other contexts.       Its application to the forensic
examination here will not impede law enforcement’s ability
to monitor and secure our borders or to conduct appropriate
searches of electronic devices.

    Nor does applying this standard impede the deterrent
effect of suspicionless searches, which the dissent contends
is critical to thwarting savvy terrorists and other criminals.
Dissent at 63. The Supreme Court has never endorsed the
proposition that the goal of deterring illegal contraband at the
border suffices to justify any manner of intrusive search.
Rather, reasonableness remains the touchstone and the Court
has expressed support for the deterrence value of
suspicionless searches of a routine nature, such as vehicle
checkpoints near the border.           See United States v.
Martinez-Fuerte, 428 U.S. 543, 556 (1976) (“We note here
only the substantiality of the public interest in the practice of
routine stops for inquiry at permanent checkpoints, a practice
which the Government identifies as the most important of the
traffic-checking operations.”) (emphasis added). In practical
terms, suspicionless searches of the type approved in Arnold
will continue; border officials will conduct further, forensic
examinations where their suspicions are aroused by what they
find or by other factors. Reasonable suspicion leaves ample
room for agents to draw on their expertise and experience to
pick up on subtle cues that criminal activity may be afoot.

 13
      Terry v. Ohio, 392 U.S. 1, 30 (1983).
                 UNITED STATES V . COTTERMAN                           27

See United States v. Tiong, 224 F.3d 1136, 1140 (9th Cir.
2000).14

     We have confidence in the ability of law enforcement to
distinguish a review of computer files from a forensic
examination. We do not share the alarm expressed by the
concurrence and the dissent that the standard we announce
will prove unmanageable or give border agents a “Sophie’s
choice” between thorough searches and Bivens actions.
Concurrence at 48–49; Dissent at 65. Determining whether
reasonable suspicion is required does not necessitate a
“complex legal determination[]” to be made on a “moment-
by-moment basis.” Dissent at 61. Rather, it requires that
officers make a commonsense differentiation between a
manual review of files on an electronic device and application
of computer software to analyze a hard drive, and utilize the
latter only when they possess a “particularized and objective



  14
     The greatest obstacle to ferreting out contraband at the border has
always been the sheer number of international travelers. Any contention
that national security will be critically hampered by stripping border
agents of a critical law enforcement tool— suspicionless forensic
examinations of electronics— is undermined by the fact that, as a matter
of commonsense and resources, it is only when reasonable suspicion is
aroused that such searches typically take place. See, e.g., Chaudhry,
424 F.3d at 1054 (B. Fletcher, J., concurring) (“As a practical matter,
border agents are too busy to do extensive searches (removing gas tanks
and door panels, boring holes in truck beds) unless they have suspicion.”).
As Judge Callahan acknowledges in her separate opinion, the record
suggests that “remote and/or intensive searches of electronic devices
crossing the border do not occur all that often.” Concurrence at 50 n.11.
The reference that only a small fraction of travelers at the border have
their devices searched simply reinforces our point— our ruling will not
place an undue burden on border agents who already rely on a degree of
suspicion in referring travelers to secondary inspection.
28            UNITED STATES V . COTTERMAN

basis for suspecting the person stopped of criminal activity.”
Tiong, 224 F.3d at 1140 (internal quotation marks omitted).

    International travelers certainly expect that their property
will be searched at the border. What they do not expect is
that, absent some particularized suspicion, agents will mine
every last piece of data on their devices or deprive them of
their most personal property for days (or perhaps weeks or
even months, depending on how long the search takes).
United States v. Ramos-Saenz, 36 F.3d 59, 61 n.3 (9th Cir.
1994) (“Intrusiveness includes both the extent of a search as
well as the degree of indignity that may accompany a
search.”). Such a thorough and detailed search of the most
intimate details of one’s life is a substantial intrusion upon
personal privacy and dignity. We therefore hold that the
forensic examination of Cotterman’s computer required a
showing of reasonable suspicion, a modest requirement in
light of the Fourth Amendment.

IV.    REASONABLE SUSPICION

    Reasonable suspicion is defined as “a particularized and
objective basis for suspecting the particular person stopped of
criminal activity.” United States v. Cortez, 449 U.S. 411,
417–18 (1981). This assessment is to be made in light of “the
totality of the circumstances.” Id. at 417. “[E]ven when
factors considered in isolation from each other are susceptible
to an innocent explanation, they may collectively amount to
a reasonable suspicion.” United States v. Berber-Tinoco,
510 F.3d 1083, 1087 (9th Cir. 2007). We review reasonable
suspicion determinations de novo, reviewing findings of
historical fact for clear error and giving “due weight to
inferences drawn from those facts by resident judges and
               UNITED STATES V . COTTERMAN                    29

local law enforcement officers.” Ornelas v. United States,
517 U.S. 690, 699 (1996).

   In the district court and in supplemental briefing, the
government argued that the border agents had reasonable
suspicion to conduct the initial search and the forensic
examination of Cotterman’s computer. We agree.

    The objective facts reflect that both the agents at the
border and the agents who arrived later from Sells based their
decision to search Cotterman’s belongings on the TECS hit.
Officer Alvarado was told by those in charge of administering
the TECS database that he should search Cotterman’s
property because the TECS hit indicated “that [Cotterman]
appeared to [have] been involved in some type of child
pornography.” Agent Riley also looked up Cotterman’s
criminal record and understood that he had a prior conviction
for child pornography. As it turned out, Cotterman’s
previous conviction was not for pornography, but for child
molestation. Nonetheless, the agents’ understanding of the
objective facts, albeit mistaken, is the baseline for
determining reasonable suspicion. See Liberal v. Estrada,
632 F.3d 1064, 1077 (9th Cir. 2011) (“Even if an officer
makes a mistake of fact, that mistake ‘will not render a stop
illegal, if the objective facts known to the officer gave rise to
a reasonable suspicion that criminal activity was afoot.’”
(quoting United States v. Mariscal, 285 F.3d 1127, 1131 (9th
Cir. 2002))).

    By itself, Cotterman’s 1992 conviction for child
molestation does not support reasonable suspicion to conduct
an extensive forensic search of his electronic devices.
“Although a prior criminal history cannot alone establish
reasonable suspicion . . . it is permissible to consider such a
30                UNITED STATES V . COTTERMAN

fact as part of the total calculus of information in th[at]
determination[].” Burrell v. McIlroy, 464 F.3d 853, 858 n.3
(9th Cir. 2006). The TECS alert was not based merely on
Cotterman’s conviction—the agents were aware that the alert
targeted Cotterman because he was a sex offender “who
travel[ed] frequently out of the country” and who was
“possibly involved in child sex tourism.” Further, Agent
Riley testified that an examination of Cotterman’s passport
confirmed that he had traveled in and out of the country
frequently since his conviction in 1992.

    In further support of reasonable suspicion, the
government asserts that Mexico, from which the Cottermans
were returning, is “a country associated with sex tourism.”15
The ICE field office specifically informed Agent Riley that
the alert was part of Operation Angel Watch, which targeted
individuals potentially involved in sex tourism and alerted
officials to be on the lookout for laptops, cameras and other
paraphernalia of child pornography. See 156 Cong. Rec.
S9581-03 (daily ed. Dec. 14, 2010) (describing Operation
Angel Watch as a program “help[ing] ICE [to] identify travel
patterns of convicted sex offenders who may attempt to
exploit children in foreign countries”). Cotterman’s TECS
alert, prior child-related conviction, frequent travels, crossing
from a country known for sex tourism, and collection of
electronic equipment, plus the parameters of the Operation


 15
    It is ironic that the dissent expresses concern that, by factoring in the
incidence of crime in particular countries, “thousands of individuals . . .
will now be forced to reconsider traveling to entire countries . . . or will
need to leave all their electronic equipment behind, to avoid arousing a
‘reasonable’ suspicion,” Dissent at 78, when, if forensic examination of
those travelers’ electronics occurs at the border, the dissent would require
no suspicion at all.
                 UNITED STATES V . COTTERMAN                           31

Angel Watch program, taken collectively, gave rise to
reasonable suspicion of criminal activity.

    To these factors, the government adds another—the
existence of password-protected files on Cotterman’s
computer.16 We are reluctant to place much weight on this
factor because it is commonplace for business travelers,
casual computer users, students and others to password
protect their files. Law enforcement “cannot rely solely on
factors that would apply to many law-abiding citizens,”
Berber-Tinoco, 510 F.3d at 1087, and password protection is
ubiquitous. National standards require that users of mobile
electronic devices password protect their files. See generally
United States Department of Commerce, Computer Security
Division, National Institute of Standards and Technology,
Computer Security (2007) (NIST Special Publication
800-111). Computer users are routinely advised—and in
some cases, required by employers—to protect their files
when traveling overseas. See, e.g., Michael Price, National
Security Watch, 34-MAR Champion 51, 52 (March 2010)
(“[T]here is one relatively simple thing attorneys can do
[when crossing the border] to protect their privacy and the
rights of their clients: password-protect the computer login
and any sensitive files or folders.”).

    Although password protection of files, in isolation, will
not give rise to reasonable suspicion, where, as here, there are
other indicia of criminal activity, password protection of files




 16
    Agent Riley testified that Alvarado told her that he had “encounter[ed]
some files that were password protected,” while Agent Alvarado testified
that he found one file.
32               UNITED STATES V . COTTERMAN

may be considered in the totality of the circumstances.17 To
contribute to reasonable suspicion, encryption or password
protection of files must have some relationship to the
suspected criminal activity. Here, making illegal files
difficult to access makes perfect sense for a suspected holder
of child pornography. When combined with the other
circumstances, the fact that Officer Alvarado encountered at
least one password protected file on Cotterman’s computer
contributed to the basis for reasonable suspicion to conduct
a forensic examination.

    The existence of the password-protected files is also
relevant to assessing the reasonableness of the scope and
duration of the search of Cotterman’s computer. The search
was necessarily protracted because of the password protection
that Cotterman employed. After Cotterman failed to provide
agents with the passwords to the protected files and fled the
country, it took Agent Owen days to override the computer
security and open the image files of child pornography.

     Although we must take into account factors weighing
both in favor and against reasonable suspicion, Cotterman’s
innocent explanation does not tip the balance. See Tiong,
224 F.3d at 1140 (recognizing that “innocent possibilities
. . . do not undermine reasonable suspicion”). The dissent
suggests that Cotterman’s offer at the border “to help the
agents access his computer” counsels against a finding of
reasonable suspicion. Dissent at 80. The agents were


  17
      W e do not suggest that password protecting an entire device—as
opposed to files within a device— can be a factor supporting a reasonable
suspicion determination. Using a password on a device is a basic means
of ensuring that the device cannot be accessed by another in the event it
is lost or stolen.
               UNITED STATES V . COTTERMAN                    33

appropriately wary of such an offer due to concerns that
Cotterman could tamper with the devices. Nor did the
agents’ discovery of vacation photos eliminate the suspicion
that Cotterman had engaged in criminal activity while abroad
or might be importing child pornography into the country.
Because the first examination of Cotterman’s laptop, by
Officer Alvarado, turned up nothing incriminating, Cotterman
urges that any suspicion prompted by the TECS alert was
dispelled by this initial failure. But the nature of the alert on
Cotterman, directing agents to review media and electronic
equipment for child pornography, justified conducting the
forensic examination despite the failure of the first search to
yield any contraband.

     Collectors of child pornography can hardly be expected
to clearly label such files and leave them in readily visible
and accessible sections of a computer’s hard drive,
particularly when they are traveling through border crossings,
where individuals ordinarily anticipate confronting at least a
cursory inspection. Officer Alvarado, who was responsible
for conducting the initial search, was specifically looking for
photographs as described in the TECS hit but testified that he
had only a slightly above-average familiarity with laptops.
He could do no more than open a file, look at it and see if he
could access it. He testified that “[i]f [he] encountered
something that [he] could not access, then [he] would
reference it to somebody that may have that ability to look at
[it].” That is precisely what occurred here. Officer Alvarado
came across password-protected files but, unable to open
them, moved on to other files. Alvarado told Agent Riley
about the password protection, and she and Agent Brisbine
decided to seize the computers for further examination. The
border agents “certainly had more than an inchoate and
unparticularized suspicion or hunch” of criminal activity to
34             UNITED STATES V . COTTERMAN

support their decision to more carefully search for evidence
of child pornography. Montoya de Hernandez, 473 U.S. at
542 (internal quotation marks and citation omitted). An alert
regarding possession of this type of criminal contraband
justified obtaining additional resources, here available in
Tucson, to properly determine whether illegal files were
present.

    Unlike the dissent, we credit the agents’ observations and
experience in acting upon significant myriad factors that
support reasonable suspicion. It is not our province to nitpick
the factors in isolation but instead to view them in the totality
of the circumstances. For the above reasons, we conclude
that the examination of Cotterman’s electronic devices was
supported by reasonable suspicion and that the scope and
manner of the search were reasonable under the Fourth
Amendment. Cotterman’s motion to suppress therefore was
erroneously granted.

     REVERSED.



CALLAHAN, Circuit Judge, concurring in part, dissenting in
part, and concurring in the judgment, with whom CLIFTON,
Circuit Judge, joins, and with whom M. SMITH, Circuit
Judge, joins as to all but Part II.A:

     Whether it is drugs, bombs, or child pornography, we
charge our government with finding and excluding any and
all illegal and unwanted articles and people before they cross
our international borders. Accomplishing that Herculean task
requires that the government be mostly free from the Fourth
Amendment’s usual restraints on searches of people and their
               UNITED STATES V . COTTERMAN                    35

property. Today the majority ignores that reality by erecting
a new rule requiring reasonable suspicion for any thorough
search of electronic devices entering the United States. This
rule flouts more than a century of Supreme Court precedent,
is unworkable and unnecessary, and will severely hamstring
the government’s ability to protect our borders.

    I therefore dissent from Part III of the majority’s opinion.
I concur in Parts I, II, and IV, and in particular the majority’s
conclusion in Part IV that the government had reasonable
suspicion to conduct the forensic examination of Howard
Cotterman’s electronic devices. I therefore also concur in the
judgment.

                               I.

    Over the last 125 years, the Supreme Court has explained
that the United States and its people have a “paramount
interest” in national self-protection and an “inherent” right to
exclude illegal and “unwanted persons and effects.” United
States v. Flores-Montano, 541 U.S. 149, 152–53 (2004); see
also United States v. Montoya de Hernandez, 473 U.S. 531,
537–40 (1985); United States v. Ramsey, 431 U.S. 606,
616–18 (1977); United States v. Thirty-Seven (37)
Photographs, 402 U.S. 363, 376 (1971); Carroll v. United
States, 267 U.S. 132, 154 (1925); Boyd v. United States,
116 U.S. 616, 623 (1886). Accordingly, “[t]he Government’s
interest in preventing the entry of unwanted persons and
effects is at its zenith at the international border.” Flores-
Montano, 541 U.S. at 152.

    To effectuate this interest, the Supreme Court has
recognized a broad exception to the Fourth Amendment’s
requirement of probable cause or a warrant for searches
36               UNITED STATES V . COTTERMAN

conducted at the border. Under that exception, searches of
people and their property at the United States borders and
their functional equivalents are per se reasonable, meaning
that they typically do not require a warrant, probable cause,
or even reasonable suspicion. Montoya de Hernandez,
473 U.S. at 538; see also Flores-Montano, 541 U.S. at
152–53; Ramsey, 431 U.S. at 616–18; United States v. Seljan,
547 F.3d 993, 999–1000 (9th Cir. 2008) (en banc), cert.
denied, 129 S. Ct. 1368 (2009).

    In the long time that the Court has recognized the border
search doctrine, the Court has found just one search at the
border that required reasonable suspicion. See Montoya de
Hernandez, 473 U.S. at 541 (upholding the 24-hour detention
of a woman suspected of smuggling illegal drugs in her
digestive system, followed by a pregnancy test and rectal
examination, based on reasonable suspicion). In the
remaining cases, the Court consistently has described the
government’s border search authority in very broad terms1


   1
     See, e.g., Flores-Montano, 541 U.S. at 152 (“The Government’s
interest in preventing the entry of unwanted persons and effects is at its
zenith at the international border.”); id. at 153 (“It is axiomatic that the
United States, as sovereign, has the inherent authority to protect, and a
paramount interest in protecting, its territorial integrity.”); Ramsey,
431 U.S. at 617 (“This interpretation, that border searches were not
subject to the warrant provisions of the Fourth Amendment and were
‘reasonable’ within the meaning of that Amendment, has been faithfully
adhered to by this Court.”); id. at 620 (“The border-search exception is
grounded in the recognized right of the sovereign to control, subject to
substantive limitations imposed by the Constitution, who and what may
enter the country.”); Thirty-Seven (37) Photographs, 402 U.S. at 376 (“[A
traveler’s] right to be let alone neither prevents the search of his luggage
nor the seizure of unprotected, but illegal, materials when his possession
of them is discovered during such a search.               Customs officers
characteristically inspect luggage and their power to do so is not
                 UNITED STATES V . COTTERMAN                            37

and overturned the lower courts’ attempts to cabin that
authority.2 The Court also repeatedly has gone out of its way
to explain that border searches generally are exempt from the
limits it imposes on domestic searches. See, e.g., Flores-
Montano, 541 U.S. at 154 (“[O]n many occasions, we have
noted that the expectation of privacy is less at the border than
it is in the interior.”); Montoya de Hernandez, 473 U.S. at
539–40 (“But not only is the expectation of privacy less at the
border than in the interior, the Fourth Amendment balance
between the interests of the Government and the privacy right
of the individual is also struck much more favorably to the
Government at the border.” (internal and external citations
omitted)); United States v. 12 200-Foot Reels of Super 8mm.
Film, 413 U.S. 123, 125 (1973) (“Import restrictions and
searches of persons or packages at the national borders rest on




questioned in this case; it is an old practice and is intimately associated
with excluding illegal articles from the country.”); Carroll, 267 U.S. at
154 (“Travelers may be so stopped in crossing an international boundary
because of national self-protection reasonably requiring one entering the
country to identify himself as entitled to come in, and his belongings as
effects which may be lawfully brought in.”). Even in Montoya de
Hernandez the Court described the government’s border search authority
expansively. See 473 U.S. at 539–40, 542–44.

 2
   See, e.g., Flores-Montano, 541 U.S. at 152–55 (overturning the Ninth
Circuit’s conclusion that the border search of a gas tank required
reasonable suspicion); Ramsey, 431 U.S. at 616–22 (overturning the D.C.
Circuit’s conclusion that the search of international mail required probable
cause); Thirty-Seven (37) Photographs, 402 U.S. at 376 (relying in part on
border search doctrine to overturn lower court’s decision that statute
barring the importation of obscene material was unconstitutional).
38               UNITED STATES V . COTTERMAN

different considerations and different rules of constitutional
law from domestic regulations.”).3

                                    II.

    It is against this legal backdrop that we must assess the
constitutionality of the government’s search in this case. As
with all searches subject to Fourth Amendment review, the
constitutionality of a border search turns on whether it is
reasonable. See Brigham City, Utah v. Stuart, 547 U.S. 398,
403 (2006) (“[T]he ultimate touchstone of the Fourth
Amendment is ‘reasonableness.’”). Under the border search
doctrine, suspicionless border searches are per se reasonable.
However, the Supreme Court has identified three situations
in which they might not be per se reasonable, i.e., at least
reasonable suspicion is required: (1) “highly intrusive
searches of the person;” (2) destructive searches of property;



   3
     See also City of Indianapolis v. Edmond, 531 U.S. 32, 47–48 (2000)
(explaining that decision barring domestic drug interdiction checkpoints
“does not affect the validity of border searches or searches at places like
airports”); United States v. Ross, 456 U.S. 798, 823 (1982) (explaining
that while the Fourth Amendment gives protection to containers in
domestic vehicles, “[t]he luggage carried by a traveler entering the country
may be searched at random by a customs officer”); Torres v. Puerto Rico,
442 U.S. 465, 472–74 (1979) (distinguishing between United
States–Puerto Rico border and international borders in holding
unconstitutional the search of a traveler’s luggage without “articulable
suspicion”); United States v. Brignoni-Ponce, 422 U.S. 873, 884 (1975)
(“Except at the border and its functional equivalents, officers on roving
patrol may stop vehicles” only with reasonable suspicion they contain
illegal aliens); Almeida-Sanchez v. United States, 413 U.S. 266, 272–76
(1973) (distinguishing searches of vehicles at the border from a search that
occurred 25 miles away); Carroll, 267 U.S. at 151–54 (distinguishing
between interior and border searches of vehicles and persons).
                 UNITED STATES V . COTTERMAN                            39

and (3) searches conducted in a “particularly offensive”
manner. Flores-Montano, 541 U.S. at 152–56 & n.2.

     Although its opinion is not entirely clear, the majority
appears to rely on the first and third exceptions to hold that
the search at issue in this case required reasonable suspicion.
(There is no claim that the government damaged or destroyed
Cotterman’s property.) But the exception for “highly
intrusive searches of the person,” Flores-Montano, 541 U.S.
at 152, cannot apply here; “papers,” even private ones in
electronic format, are not a “person.” See id. (“The reasons
that might support a requirement of some level of suspicion
in the case of highly intrusive searches of the person—dignity
and privacy interests of the person being searched—simply
do not carry over to vehicles.”). That leaves the exception for
searches conducted in a “particularly offensive” manner. Id.
at 154 n.2. The majority relies primarily on the notion that
electronic devices are special to conclude that reasonable
suspicion was required. Majority at 20–28. The majority is
mistaken.

                                    A.

    The majority correctly concludes that the government’s
forensic search in Tucson was not an extended border search,
as the border agents retained custody of Cotterman’s laptop.4

  4
    I agree with the majority that this case does not involve an extended
border search. Unlike a border search, an extended border search takes
place at a location “away from the border where entry is not apparent, but
where the dual requirements of reasonable certainty of a recent border
crossing and reasonable suspicion of criminal activity are satisfied.”
United States v. Guzman-Padilla, 573 F.3d 865, 878–79 (9th Cir. 2009)
(internal quotation marks and citation omitted), cert. denied, 131 S. Ct. 67
(2010). Reasonable suspicion is required precisely because the individual
40               UNITED STATES V . COTTERMAN

Id. at 9, 14–15. The majority also states that “[i]t is the
comprehensive and intrusive nature of a forensic
examination—not the location of the examination—that is the
key factor triggering the requirement of reasonable suspicion
here.” Majority at 17. The inclusion of the word “key” might
be read to imply that some other factor, such as the location
and duration of the search, contributed to its purported
unreasonableness. I write to refute any such notion.

    First consider the facts. The border agents took
Cotterman’s electronic devices to the nearest computing
center (to Tucson, where Cotterman and his wife were
already traveling), before clearing them for entry into the
United States. The computer specialist moved the search
ahead of his other work and conducted it over the weekend.
Although the forensic search lasted five days, it took only 48
hours to discover the initial 75 images of child pornography.
The agents were reasonably reluctant to rely on Cotterman’s
offer to help, since he might have deleted or otherwise made
unrecoverable any contraband that his devices contained.
The agents returned the devices as soon as they cleared them.




has regained an expectation of privacy by moving away from the border.
See United States v. Villasenor, 608 F.3d 467, 471–72 (9th Cir.), cert.
denied, 131 S. Ct. 547 (2010); United States v. Whiting, 781 F.2d 692, 695
(9th Cir. 1986). Here, there was no attenuation between Cotterman’s
border crossing and the forensic search of his electronic property; the
government conducted that search before clearing the property for entry
and before Cotterman could regain an expectation of privacy in that
property. See 19 U.S.C. § 1499 (providing that imported goods are
permitted entry only after Customs clears them); United States v. Alfonso,
759 F.2d 728, 734 (9th Cir. 1985) (“Extended border searches occur after
the actual entry has been effected and intrude more on an individual’s
normal expectation of privacy.”).
               UNITED STATES V . COTTERMAN                    41

    Now consider the law. The Supreme Court has upheld the
constitutionality of a police search of packages retrieved from
an automobile, even though the police conducted their search
three days after the police stopped the vehicle and at the
police station. United States v. Johns, 469 U.S. 478, 485–88
(1985). The Court rejected the argument that “searches of
containers discovered in the course of a vehicle search are
subject to temporal restrictions not applicable to the vehicle
search itself.” Id. at 485. Although Johns involved a
domestic automobile search based on probable cause, it still
stands for the proposition, equally applicable to this case, that
“the legality of the search was determined by reference to the
[applicable] exception to the warrant requirement.” Id.

     In the border search context, the Supreme Court, in
upholding the lengthy detention of a person reasonably
suspected of smuggling drugs in her digestive system at an
airport, addressed whether that detention was “reasonably
related in scope to the circumstances which justified it
initially.” Montoya de Hernandez, 473 U.S. at 542. The
Court explained that: (1) “courts should not indulge in
unrealistic second-guessing” when answering this question,
as “[a]uthorities must be allowed to graduate their response
to the demands of any particular situation;” (2) the Court
consistently has “refused to charge police with delays in
investigatory detention attributable to the suspect’s evasive
actions;” and (3) “we have also consistently rejected hard-
and-fast time limits.” Id. at 542–43 (quotation marks and
citations omitted). The Court emphasized that, at the
international border, “the Fourth Amendment balance of
interests leans heavily to the Government” because the
government is charged not just with investigating crime but
with “protecting this Nation from entrants who may bring
anything harmful into this country.” Id. at 544. Finally, any
42                UNITED STATES V . COTTERMAN

“length” or “discomfort” associated with a border search does
not offend the Fourth Amendment when it “result[s] solely
from the method by which [a traveler] cho[oses] to smuggle
[contraband] into this country.” Id.

    Any suggestion that the government’s search here was
“particularly offensive” due to the location and duration of
the search runs counter to the Supreme Court’s admonitions
in Johns and Montoya de Hernandez. It also effectively
requires the government to supply every port of entry with the
equipment and staff needed to conduct forensic electronic
searches, or at least to have such equipment and staff waiting
at a nearby location. Such a requirement is unreasonable,
particularly since the record in this case suggests that a
forensic search of Cotterman’s electronic devices at the
border station would have taken longer than the search at the
Tucson computing center.5 See United States v. Hill,
459 F.3d 966, 974–75 (9th Cir. 2006), cert. denied, 127 S. Ct.
1863 (2007) (discussing problems inherent in requiring police
to bring with them equipment to search electronic media); cf.
Johns, 469 U.S. at 486–87 (explaining that requiring police


 5
   The district court found that the government could have conducted the
forensic search at the Lukeville border station. United States v.
Cotterman, No. CR 07-1207-TUC-RCC, 2009 WL 465028, at *1 (D. Ariz.
Feb. 24, 2009). The court presumably based this finding on testimony that
the computer specialist who conducted the forensic examination had a
specially-equipped laptop. However, the specialist testified that using his
laptop at the border station, rather than transporting Cotterman’s electronic
devices to the Tucson computer center, would have taken “a lot longer”
because the laptop was “not nearly as extensive as what I have in my lab,”
the “processor in my laptop is much slower” than the lab equipment, and
“I could only do one computer at a time with the laptop.” Technical
difficulties also could have slowed down an examination conducted at the
border station.
              UNITED STATES V . COTTERMAN                   43

officers to immediately inspect all packages “would be of
little benefit to the person whose property is searched”).

                              B.

    The majority’s opinion turns primarily on the notion that
electronic devices deserve special consideration because they
are ubiquitous and can store vast quantities of personal
information. That idea is fallacious and has no place in the
border search context.

    The Supreme Court has been willing to distinguish only
between border searches of people and property, not between
different types of property. In 2004, in Flores-Montano, the
Court explained that

       the reasons that might support a requirement
       of some level of suspicion in the case of
       highly intrusive searches of the
       person—dignity and privacy interests of the
       person being searched—simply do not carry
       over to vehicles. Complex balancing tests to
       determine what is a “routine” search of a
       vehicle, as opposed to a more “intrusive”
       search of a person, have no place in border
       searches of vehicles.

541 U.S. at 152. We have since applied Flores-Montano to
hold that any distinction between “routine” and “nonroutine”
searches does not apply to searches of property, and that there
can be no “least restrictive means” test for border searches.
United States v. Chaudhry, 424 F.3d 1051, 1054 (9th Cir.
2005), cert. denied, 547 U.S. 1083 (2006); United States v.
Cortez-Rocha, 394 F.3d 1115, 1122–23 (9th Cir. 2004), cert.
44               UNITED STATES V . COTTERMAN

denied, 546 U.S. 849 (2005).6 Put another way, the Supreme
Court—and, reluctantly, this court—have refused to adopt a
sliding “intrusiveness” scale for border searches of property.
Thus, the Court has all but held that property that crosses the
border, whatever it is, does not merit Fourth Amendment
protection.

    Of course, Flores-Montano, Chaudhry, and Cortez-Rocha
involved vehicles or parts of vehicles, not electronic devices,
and the other border search cases that have reached the
Supreme Court all involved containers of some sort. See,
e.g., Ramsey, 431 U.S. at 616–22 (mail); Thirty-Seven (37)
Photographs, 402 U.S. at 376 (luggage). And yes, the Court
has left open the possibility that a border search might be
“‘‘unreasonable’ because of the particularly offensive manner
in which it is carried out.’” Flores-Montano, 541 U.S. at 154
n.2 (quoting Ramsey, 431 U.S. at 618 n.13). But is the mere
fact that Cotterman chose to save his child pornography
electronically, rather than print it out on paper, enough to
invoke that exception?

   The two courts of appeals—including this court—that
have had occasion to address whether electronic devices


  6
    In 1985, the Supreme Court wrote about the government’s “plenary
authority to conduct routine searches and seizures at the border.”
Montoya de Hernandez, 473 U.S. at 537 (emphasis added); see also id. at
541 n.4 (“Because the issues are not presented today we suggest no view
on what level of suspicion, if any, is required for nonroutine border
searches such as strip, body-cavity, or involuntary x-ray searches.”)
(emphasis added). W e unfortunately seized on the word “routine” to
establish a sliding scale of intrusiveness, with more intrusive (i.e., less
“routine”) searches requiring reasonable suspicion. See, e.g., United
States v. Molina-Tarazon, 279 F.3d 709, 711–13 (9th Cir. 2002). Flores-
Montano plainly repudiated that approach.
              UNITED STATES V . COTTERMAN                  45

deserve special consideration have correctly concluded that
they do not. In United States v. Arnold, 533 F.3d 1003,
1008–10 (9th Cir. 2008), cert. denied, 555 U.S. 1176 (2009),
we held that laptops are like other property, relying on the
reasoning and language in Flores-Montano, Chaudhry, and
Cortez-Rocha discussed above (among other cases).
Similarly, in United States v. Ickes, 393 F.3d 501, 503–07
(4th Cir. 2005), the Fourth Circuit upheld an extensive border
search of the defendant’s laptop that revealed child
pornography. Notably, the court held that the border agents
had reasonable suspicion to search the defendant’s laptop, but
explained why that did not matter:

       The agents did not inspect the contents of
       Ickes’s computer until they had already
       discovered marijuana paraphernalia, photo
       albums of child pornography, a disturbing
       video focused on a young ball boy, and an
       outstanding warrant for Ickes’s arrest. As a
       practical matter, computer searches are most
       likely to occur where—as here—the traveler’s
       conduct or the presence of other items in his
       possession suggest the need to search further.
       However, to state the probability that
       reasonable suspicions will give rise to more
       intrusive searches is a far cry from enthroning
       this notion as a matter of constitutional law.
       The essence of border search doctrine is a
       reliance upon the trained observations and
       judgments of customs officials, rather than
       upon constitutional requirements applied to
       the inapposite context of this sort of search.
46               UNITED STATES V . COTTERMAN

Id. at 507. Thus, the Fourth Circuit has recognized what the
majority does not: electronic devices are like any other
container that the Supreme Court has held may be searched
at the border without reasonable suspicion.7 Though we are
not bound by Arnold nor Ickes in this en banc proceeding, we
are bound by what the Supreme Court has said: in the unique
context of border searches, property is property and we may
not chip away at the government’s authority to search it by
adopting a sliding scale of intrusiveness. It’s the border, not
the technology, that “matters.” Majority at 24; cf. Ramsey,
431 U.S. at 620 (“It is clear that there is nothing in the
rationale behind the border-search exception which suggests
that the mode of entry will be critical.”).

    Logic and commonsense, not just Supreme Court
precedent, reveal the flaws in the majority’s opinion. The
fact that electronic devices are capable of storing a lot of
personal information does not make an extensive search of
them “particularly offensive.” We have squarely rejected the
idea that the “intrusiveness” of a search depends in whole or
in part on the nature of the property being searched. In
United States v. Giberson, 527 F.3d 882 (9th Cir. 2008), we
specifically rebuffed the argument that computers are special
for Fourth Amendment purposes by virtue of how much
information they store; “neither the quantity of information,
nor the form in which it is stored, is legally relevant in the
Fourth Amendment context.” Id. at 888; see also California
v. Carney, 471 U.S. 386, 393–94 (1985) (rejecting applying




  7
    I agree with Judge Smith that the majority’s opinion appears to create
an imprudent split with the Fourth Circuit. See Dissent at 58.
                 UNITED STATES V . COTTERMAN                            47

Fourth Amendment protection to property (a mobile home)
that is “capable of functioning as a home” simply on account
of the property’s size or “worth[iness]” as a container);
United States v. Payton, 573 F.3d 859, 864 (9th Cir. 2009)
(“Giberson held that computers were not entitled to a special
categorical protection of the Fourth Amendment.”); Kyllo v.
United States, 533 U.S. 27, 41 (2001) (Stevens, J., dissenting)
(explaining that Fourth Amendment exceptions and
distinctions based solely on a type of technology are
“unwise[ ] and inconsistent with the Fourth Amendment”).

     While Giberson and Carney involved domestic searches,
their reasoning applies equally in the border search context.
If the government may search the contents of a briefcase, car,
or mobile home that transits the border, there is no reason it
should not also be able to search the contents of a camera,
tablet, or laptop that enters the country. All of those things
are capable of storing, and often do store, private information.
See Ross, 456 U.S. at 823 (“The luggage carried by a traveler
entering the country may be searched at random by a customs
officer; the luggage may be searched no matter how great the
traveler’s desire to conceal the contents may be.” (emphasis
added)). The majority points out that electronic devices can
and usually do store much more private information than their
non-electronic counterparts. Majority at 17–24. But “a port
of entry is not a traveler’s home,” Thirty-Seven (37)
Photographs, 402 U.S. at 376, even if a traveler chooses to
carry a home’s worth of personal information across it.8


 8
    The element of choice is crucial. The fact that border searches occur
at fixed times and checkpoints makes them inherently less intrusive; a
person “with advance notice of the location of a permanent checkpoint has
an opportunity to avoid the search entirely, or at least to prepare for, and
limit, the intrusion on her privacy.” Mich. Dep’t of State Police v. Sitz,
48               UNITED STATES V . COTTERMAN

Moreover, a bright-line rule distinguishing electronic from
non-electronic devices—of the sort the Supreme Court has
made clear has no place in Fourth Amendment jurisprudence,
Ohio v. Robinette, 519 U.S. 33, 39 (1996)—is arbitrary; there
is no reason someone carrying a laptop should receive greater
privacy protection than someone who chooses (or can only
afford) to convey his or her personal information on paper.

    In short, today the court erects a new bright-line rule:
“forensic examination” of electronic devices “at the border
requires reasonable suspicion.” Majority at 17; see also id. at
21 n.10. The majority never defines “forensic,” leaving
border agents to wonder exactly what types of searches are




496 U.S. 444, 463 (1990) (Stevens, J., dissenting); see also Montoya de
Hernandez, 473 U.S. at 544 (“Respondent’s detention was long,
uncomfortable, indeed, humiliating; but both its length and its discomfort
resulted solely from the method by which she chose to smuggle illicit
drugs into this country.”).

     The element of choice goes to the more fundamental issue of whether
someone can have any reasonable expectation of privacy when he or she
voluntarily carries electronic equipment across the border. Border officers
are permitted to examine a written diary, and someone who wants to keep
the contents of a diary secret should know not to take it across the border.
The same should be true for personal data stored on a laptop or other
electronic device rather than a written diary.

      Moreover, the fact that the Fourth Amendment does not apply in
foreign countries further weakens any claim to a reasonable expectation
of privacy in property that crosses the United States border. Carrying an
electronic device outside the United States almost always entails carrying
it into another country, making it subject to search under that country’s
laws. Travelers expect these intrusions, or at least their possibility.
                 UNITED STATES V . COTTERMAN                            49

off-limits.9 Even if the majority means to require reasonable
suspicion for any type of digital forensic border search, no
court has ever erected so categorical a rule, based on so
general a type of search or category of property, and the
Supreme Court has rightly slapped down anything remotely
similar. The majority invites—indeed, requires—the Court
to do so again.10

                                   III.

    The majority’s holding contravenes Supreme Court
precedent, defies logic and commonsense, and is unworkable.
It is also unnecessary and will impair the federal
government’s ability to protect our borders.

    As Judge Smith points out in his dissent, “[b]order patrol
agents process hundreds of thousands of travelers each day
and conduct thousands of searches on electronic devices each
year.” Dissent at 61–62 (citation omitted). All the evidence
in this case suggests that the government does not have the
resources—time, personnel, facilities, or technology—to
exhaustively search every (or even a majority) of the
electronic devices that cross our borders. Cf. Ickes, 393 F.3d
at 507. Unless we somehow manage to solve our fiscal
problems, and unless the government somehow manages to


 9
   See Darrin J. Behr, Anti-Forensics: What it Does and Why You Need
to Know, 255 N.J. Law. 9, 10 (Dec. 2008) (“Due to the fact that there are
hundreds of digital forensic investigation procedures developed all over
the world, digital forensics has yet to be defined.”).

  10
     I note that a case currently pending in the Sixth Circuit appears to
raise similar issues as this case. See United States v. Stewart, No. 12-1427
(6th Cir. filed Apr. 5, 2012); see also United States v. Stewart, 715 F.
Supp. 2d 750 (E.D. Mich. 2010).
50                UNITED STATES V . COTTERMAN

acquire better technology at a faster pace than the rest of us,
these restraints will continue. That means border agents must
prioritize who, what, and how they search. By and large,
border agents will conduct forensic electronic searches of
people who, like Howard Cotterman, the agents reasonably
suspect may be trying to carry illegal articles into, or
themselves illegally enter, the country.11 That agents
typically will have reasonable suspicion is, of course, “a far
cry from enthroning this notion as a matter of constitutional
law.” Ickes, 393 F.3d at 507.

    The majority finds this reality check to be of “little
comfort[;] [i]t is the potential unfettered dragnet effect that is
troublesome.” Majority at 25. But that abstract risk, which
exists with any exception to the Fourth Amendment, does not
justify a bright-line rule requiring reasonable suspicion for
any thorough search of electronic devices entering the United


  11
      Testimony from the suppression hearing in this case suggests that
remote and/or intensive searches of electronic devices crossing the border
do not occur all that often. For example, the computer specialist who
conducted the forensic search of Cotterman’s laptop testified that the
search was the first one he was asked to conduct in his 18 months on the
job at the Tucson computer center. (He added that at his previous post at
San Francisco International Airport, forensic searches were done right at
the airport.) Similarly, one of the border agents testified that this was the
first case he was aware of in which electronic devices were turned over to
Immigrations and Customs Enforcement for forensic examination, and
that even cursory reviews of laptops for information about illegal drug
trading occurred “no more than five” times during agent’s three-plus years
at the Lukeville border station. See Michael Chertoff, Secretary of
Homeland Security, Searches Are Legal, Essential, USA Today, July 16,
2008 (“Of the approximately 400 million travelers who entered the
country last year, only a tiny percentage were referred to secondary
baggage inspection for a more thorough examination. Of those, only a
fraction had electronic devices that may have been checked.”).
                UNITED STATES V . COTTERMAN                          51

States. See Robinette, 519 U.S. at 39 (“[W]e have
consistently eschewed bright-line rules, instead emphasizing
the fact-specific nature of the reasonableness inquiry.”); see
also Lyng v. Nw. Indian Cemetery Protective Ass’n, 485 U.S.
439, 445 (1988) (“A fundamental and longstanding principle
of judicial restraint requires that courts avoid reaching
constitutional questions in advance of the necessity of
deciding them.”).

    Moreover, border agents are not free to undertake
“unfettered crime-fighting searches or an unregulated assault
on citizens’ private information.” Majority at 26. As I
explained in my concurrence in Seljan, Congress and the
Executive Branch have (and have exercised) the authority to
restrict when and how border agents conduct searches. See
Seljan, 547 F.3d at 1012 (Callahan, J., concurring) (citing,
e.g., 19 U.S.C. § 1583; 19 C.F.R. § 145.3(b)-(c)); see also
Yule Kim, Cong. Research Serv. RL34404, Border Searches
of Laptop Computers and Other Electronic Storage Devices,
13–14 (2009) (describing recent legislative proposals to limit
border searches of electronic devices). In a similar vein,
Justice Breyer has noted that “Customs keeps track of the
border searches its agents conduct, including the reasons for
the searches. This administrative process should help
minimize concerns that [border] searches might be
undertaken in an abusive manner.” Flores-Montano,
541 U.S. at 156 (Breyer, J., concurring) (internal citation
omitted).12



 12
   See also U.S. Customs & Border Protection, Directive No. 3340-049,
Border Search of Electronic Devices Containing Information, 3–9 (2009)
(describing procedures for, and limits on, border searches of electronic
devices).
52             UNITED STATES V . COTTERMAN

    Apart from being unnecessary, the majority’s new limits
on the government’s border search authority will make it
much harder for border agents to do their jobs, for at least two
reasons. First, it is common knowledge that border agents at
security checkpoints conduct more thorough searches not
simply of those persons who arouse suspicion but also of a
percentage of travelers on a random basis. Otherwise, a
person who appears entirely innocent will have nothing to
fear and will not be deterred from carrying something that
should not be brought into the country. A checkpoint limited
to searches that can be justified by articulable grounds for
“reasonable suspicion” is bound to be less effective.

    Second, courtesy of the majority’s decision, criminals
now know they can hide their child pornography or terrorist
connections in the recesses of their electronic devices, while
border agents, fearing Fourth Amendment or Bivens actions,
will avoid conducting the searches that could find those
illegal articles. The result will be that people and things we
wish to keep out of our country will get in—a result hardly in
keeping with our “inherent authority to protect, and a
paramount interest in protecting,” the “territorial integrity” of
the United States. Flores-Montano, 541 U.S. at 153. The
border search doctrine must account for the fact that border
agents may need time and forensics to bypass “evasive
actions” a criminal has taken to hide contraband or other
illegal articles from plain view. Montoya de Hernandez,
473 U.S. at 542–43. I would rather leave those difficult
decisions “to the discretion of the officers in the field who
confront myriad circumstances we can only begin to imagine
from the relative safety of our chambers.” United States v.
                 UNITED STATES V . COTTERMAN                           53

Williams, 419 F.3d 1029, 1034 (9th Cir.), cert. denied,
546 U.S. 1081 (2005).13

                                   IV.

    The border search exception to the Fourth Amendment
may be just that—an exception—but it is, and must be, a
mighty one. The government’s right and duty to protect our
nation’s territorial integrity demand that the government have
clear authority to exclude—and thus to find—those people
and things we have decided are offensive, threatening, or
otherwise unwanted. Recognizing this, the Supreme Court
has only once required reasonable suspicion for border
searches in the 125 years it has been reviewing them. In the
remaining cases, the Court has eschewed bright-line rules,
balancing tests, and sliding intrusiveness scales, alluding to
the possibility of, but never finding, a “particularly offensive”


 13
    The majority insists that reasonable suspicion is a “modest, workable
standard” that is applied in domestic stops of automobiles “and other
contexts,” and that still allows “agents to draw on their expertise and
experience.” Majority at 26, 27 n.14. The majority is wrong for at least
three reasons. First, in making this argument, the majority reveals that it
does not appreciate the crucial differences between domestic and border
searches, despite those differences being spelled out in a century of case
law. Those differences range from the legitimate expectation of privacy
that people have in their property to the constraints government officials
face in searching it. Second, a reasonable suspicion standard injects
unnecessary judicial review where previously it was absent. Third, just
because border agents could apply the reasonable suspicion standard does
not mean they are, or should be, constitutionally compelled to do so. See
Ickes, 393 F.3d at 507; cf. Seljan, 547 F.3d at 1011 (Callahan, J.
concurring) (explaining that requiring border agents to apply a First
Amendment exception to border searches “would require them to engage
in the sort of decision-making process that the Supreme Court wished to
avoid in sanctioning expansive border searches”).
54            UNITED STATES V . COTTERMAN

search. The fact that electronic devices can store large
amounts of private information, or that the government can
search them forensically, does not make a thorough search of
such devices “particularly offensive.” Rather, the Supreme
Court and this court have wisely avoided making the
reasonableness of a search turn on the nature of the property
being searched, for the many reasons discussed above. The
result has been a clear, well-understood, efficient, and
effective rule that border searches are per se reasonable.

    Regrettably the majority, dispensing with these well-
settled, sensible, and binding principles, lifts our anchor and
charts a course for muddy waters. Now border agents,
instead of knowing that they may search any and all property
that crosses the border for illegal articles, must ponder
whether their searches are sufficiently “comprehensive and
intrusive,” Majority at 17, to require reasonable suspicion,
and whether they have such suspicion. In most cases the
answer is going to be as clear as, well, mud. We’re due for
another course correction.



M. SMITH, Circuit Judge, dissenting, with whom CLIFTON
and CALLAHAN, Circuit Judges, join with respect to Part I:

    I respectfully dissent. Until today, federal courts have
consistently upheld suspicionless searches of electronic
storage devices at the border. See United States v. Arnold,
533 F.3d 1003, 1008 (9th Cir. 2008), cert. denied, 555 U.S.
1176 (2009) (“[R]easonable suspicion is not needed for
customs officials to search a laptop or other personal
electronic storage devices at the border.”); see also United
States v. Ickes, 393 F.3d 501, 507 (4th Cir. 2005) (no finding
              UNITED STATES V . COTTERMAN                   55

of reasonable suspicion required to search personal computers
and disks at border); United States v. Linarez-Delgado,
259 Fed. Appx. 506, 508 (3d Cir. 2007); United States v.
McAuley, 563 F. Supp. 2d 672, 677–78 (W.D. Tex. 2008);
United States v. Bunty, 617 F. Supp. 2d 359, 365 (E.D. Pa.
2008). Yet the majority ignores these cases, rewrites long
standing Fourth Amendment jurisprudence, and, in narrowing
Arnold, creates a circuit split.

    While I share some of the majority’s concerns about the
steady erosion of our personal privacy in this digital age, the
majority’s decision to create a reasonable suspicion
requirement for some property searches at the border so
muddies current border search doctrine that border agents will
be left to divine on an ad hoc basis whether a property search
is sufficiently “comprehensive and intrusive” to require
reasonable suspicion, or sufficiently “unintrusive” to come
within the traditional border search exception. Requiring
border patrol agents to determine that reasonable suspicion
exists prior to performing a basic forensic examination of a
laptop or other electronic devices discourages such searches,
leaving our borders open to electronically savvy terrorists and
criminals who may hereafter carry their equipment and data
across our borders with little fear of detection. In fact, the
majority opinion makes such a legal bouillabaisse out of the
previously unambiguous border search doctrine, that I
sincerely hope the Supreme Court will grant certiorari, and
reverse the holding in this case regarding the level of
suspicion necessary to search electronic devices at the border,
for the sake of our national security, and the consistency of
our national border search law.

   The Supreme Court rejected our last attempt to narrow the
border search exception, cautioning us not to create “complex
56            UNITED STATES V . COTTERMAN

balancing tests” for border searches of property except in the
rarest of cases, where the search is “so destructive as to
require” reasonable suspicion. United States v. Flores-
Montano, 541 U.S. 149, 152, 156 (2004) (rejecting our
proposed reasonable suspicion requirement in United States
v. Molina-Tarazon, 279 F.3d 709, 713–17 (9th Cir. 2002)).
“Time and again” the Court has concluded that border
searches are “‘reasonable simply by virtue of the fact that
they occur at the border.’” Id. at 152–53 (quoting United
States v. Ramsey, 431 U.S. 606, 616 (1977)).

    Despite the Court’s clear ruling on the issue, the majority
again seeks to whittle away at the border search exception,
this time by conjuring a reasonable suspicion requirement for
border searches that employ computer software to search an
electronic storage device. Why the use of computer software
to analyze a hard drive triggers a reasonable suspicion
requirement while a “manual review” of the same hard drive
requires no suspicion, is left unexplained. Although
technology may serve as a useful proxy for the intrusiveness
of a search today, in the future even cursory searches might
be more efficiently conducted by the use of such technology.
Under the majority’s reasonable suspicion standard,
individuals’ privacy rights are only as secure as the
sophistication of the government’s current search mechanism.

    Moreover, the task of distinguishing these
“comprehensive and intrusive” laptop searches from the
“unintrusive search” of a laptop affirmed in Arnold, 533 F.3d
at 1008, or the search of a private letter affirmed in United
States v. Seljan, 547 F.3d 993, 1003 (9th Cir. 2008) (en banc),
leaves border patrol officers with a difficult choice: either
protect our nation from those who mean us harm, or risk their
own jobs and livelihood in a Bivens action, or disciplinary
              UNITED STATES V . COTTERMAN                   57

proceedings. Apart from being administratively impractical,
the majority’s reasonable suspicion requirement disregards
well established border search jurisprudence, and undermines
vital national security interests. Ironically, the majority did
not even need to consider the border search doctrine in this
case because the search at issue in this case did not occur at
the border.

    Separately, but importantly, the majority’s application of
the reasonable suspicion requirement to Cotterman is also
troubling. The majority purports to be concerned with
travelers’ “personal privacy and dignity,” but its
determination that reasonable suspicion exists under the
exceedingly weak facts of this case undermines the liberties
of U.S. citizens generally—not just at the border, and not just
with regard to our digital data—but on every street corner, in
every vehicle, and wherever else we rely on the doctrine of
reasonable suspicion to safeguard our legitimate privacy
interests.

I. The Border Search Doctrine

    The majority heralds this as a “watershed” case that
requires a narrowing of the border search exception to
accommodate the privacy interests allegedly created by new
technologies. Yet despite the majority’s attempts to avoid the
fact, the border search exception is clear and inflexible. The
Supreme Court has repeatedly affirmed the breadth of the
border search doctrine, extending a reasonable suspicion
requirement only to: (1) “highly intrusive searches of the
person”; (2) “searches of property [that] are so destructive as
to require” reasonable suspicion; and (3) searches carried out
in a “particularly offensive manner”—of which the Court has
yet to find an example. Flores-Montano, 541 U.S. at 152,
58            UNITED STATES V . COTTERMAN

154 n.2, 156 (quotations and citations omitted) (emphasis
added).

    The majority misconstrues these narrowly-defined
exceptions, reading Flores-Montano to require reasonable
suspicion whenever a search of property is deemed “overly
intrusive.” Majority at 18–19. Yet, the exceptions articulated
in Flores-Montano are far more circumscribed—applying not
to “overly intrusive” searches of property, like the search of
Cotterman’s computer, but only to “highly intrusive searches
of the person.” Flores-Montano, 541 U.S. at 152 (emphasis
added). The majority’s adoption of a reasonable suspicion
requirement to “comprehensive forensic examination[s]” of
property is irreconcilable with Flores-Montano. Majority at
6.

    We have consistently rejected a reasonable suspicion
requirement for border searches of expressive materials, such
as papers and their modern-day equivalent—the data
contained on electronic storage devices. See, e.g., Seljan,
547 F.3d at 1003 (“An envelope containing personal
correspondence is not uniquely protected from search at the
border.”); Arnold, 533 F.3d at 1008 (“[R]easonable suspicion
is not needed for customs officials to search a laptop or other
personal electronic storage devices at the border.”). The
majority states that its en banc decision narrows Arnold to
permit only “relatively simple” border searches of laptops,
and “not to countenance suspicionless forensic
examinations.” Majority at 14 n.6. In narrowing Arnold,
however, the court creates a circuit split regarding the
application of reasonable suspicion to border searches of
electronic devices. See United States v. Ickes, 393 F.3d 501
(4th Cir. 2005); see also United States v. Linarez-Delgado,
259 Fed. Appx. 506, 508 (3d Cir. 2007).
              UNITED STATES V . COTTERMAN                  59

    For instance, in Ickes (as in Arnold) the defendant-
appellant argued that a reasonable suspicion requirement was
necessary for laptop searches at the border because otherwise
“any person carrying a laptop computer [] on an international
flight would be subject to a search of the files on the
computer hard drive.” Ickes, 393 F.3d at 506–07. The Fourth
Circuit rejected this argument, noting that

       “[a]s a practical matter, computer searches are
       most likely to occur where—as here—the
       traveler’s conduct or the presence of other
       items in his possession suggest the need to
       search further.      However, to state the
       probability that reasonable suspicions will
       give rise to more intrusive searches is a far
       cry from enthroning this notion as a matter of
       constitutional law. The essence of border
       search doctrine is a reliance upon the trained
       observations and judgments of customs
       officials, rather than upon constitutional
       requirements applied to the inapposite context
       of this sort of search.”

Id. at 507 (emphasis added). The Third Circuit similarly
rejected a reasonable suspicion requirement for border
searches of electronic data, albeit in an unpublished opinion.
See United States v. Linarez-Delgado, 259 Fed. Appx. 506,
508 (3d Cir. 2007) (“Data storage media and electronic
equipment, such as films, computer devices, and videotapes,
may be inspected and viewed during a reasonable border
search.”) (citing Ickes, 393 F.3d 501). Because the majority
has narrowed our holding in Arnold that “reasonable
suspicion is not needed for customs officials to search a
laptop or other personal electronic storage devices at the
60             UNITED STATES V . COTTERMAN

border,” Arnold, 533 F.3d at 1008, the Ninth Circuit stands
alone, as it so often does.

    The majority likens the search of Cotterman’s laptop to a
“computer strip search,” Majority at 25, and proceeds to
conflate the law regarding property searches with that
regarding “highly intrusive searches of the person.” Flores-
Montano, 541 U.S. at 152. However, the “reasons that might
support a requirement of some level of suspicion in the case
of highly intrusive searches of the person—dignity and
privacy interests of the person being searched—simply do not
carry over” to laptops, which know no dignity or shame, and
thus have neither of those interests. Flores-Montano,
541 U.S. at 152 (emphasis added). Moreover, even genuine
strip searches do not necessarily require reasonable suspicion
at the border. See United States v. Montoya de Hernandez,
473 U.S. 531, 541 n.4 (1985) (expressly declining to decide
“what level of suspicion, if any, is required for . . . strip, body
cavity, or involuntary x-ray searches”) (emphasis added).

    The majority’s decision to insulate electronic storage
devices from the border search exception unsettles the border
search doctrine, places inappropriate burdens on law
enforcement, reduces deterrence, and raises serious national
security concerns. It also ignores the realities of electronic
data transmission and the reduced privacy expectations that
accompany much of this data, particularly at the border where
“[t]he government’s interest in preventing the entry of
unwanted persons and effects is at its zenith.” Flores-
Montano, 541 U.S. at 152.
               UNITED STATES V . COTTERMAN                    61

    A. Burdens on Law Enforcement

    The majority’s holding cripples law enforcement at the
border by depriving border patrol agents of the clear
administrative guidance they need to carry out core law
enforcement activities. “Officers who interact with those
suspected of violating the law have an essential interest in
readily administrable rules.” Florence v. Bd. of Chosen
Freeholders of Cnty. of Burlington, 132 S. Ct. 1510, 1522
(2012). Yet the majority’s holding requires border patrol
agents to determine on a case-by-case and moment-by-
moment basis whether a search of digital data remains
“unintrusive,” a la Arnold, or has become “comprehensive
and intrusive,” a la Cotterman. Majority at 14, 17.
Requiring law enforcement to make such complex legal
determinations on the spot, and in the face of potentially
grave national security threats, strips agents of their necessary
discretion and deprives them of an efficient and administrable
rule.

    The majority dismisses the burden its reasonable
suspicion requirement places on law enforcement, asserting
that agents can simply “draw on their expertise and
experience” to make the necessary judgment calls. Majority
at 26. Yet rather than actually deferring to this expertise and
experience, the majority forces border patrol agents to justify
their decisions under a heightened standard that has never
before been applied to border searches of property.

    Border patrol agents process hundreds of thousands of
travelers each day and conduct thousands of searches on
62             UNITED STATES V . COTTERMAN

electronic devices each year.1 Identifying national security
and criminal threats at the border requires a high level of
experience and discretion in order to recognize and respond
to the ever-changing tactics of those who seek to enter our
country with nefarious intent. In recognition of these crucial
interests, the border search exception provides law
enforcement with broad discretion to conduct border searches
of property without resorting to case-by-case determinations
of reasonable suspicion—determinations border patrol agents
are ill-equipped to handle. See generally Florence, 132 S. Ct.
at 1522 (rejecting reasonable suspicion requirement for prison
strip-searches under this rationale). Moreover, as a practical
matter, suspicionless border searches of property make sense,
in light of the sheer number of individuals crossing the border
with electronic devices each day. See United States v.
Martinez-Fuerte, 428 U.S. 543, 557 (1976) (requiring
reasonable suspicion for vehicle checkpoints near the
Mexican border “would be impractical because the flow of
traffic tends to be too heavy to allow the particularized study
of a given car”). Given these realities of law enforcement at
the border, a reasonable suspicion requirement for all “overly
intrusive” electronic searches is simply not practicable.

     B. National Security Concerns

    The majority’s decision to insulate electronic devices
from search at the border creates serious national security
concerns. An “ever present threat exists from the potential
for terrorists to employ the same smuggling and
transportation networks, infrastructure, drop houses, and
other support” as other illegal aliens. U.S. Customs and

 1
   Department of Homeland Security Privacy Office, Annual Report to
Congress 54 (2009).
                 UNITED STATES V . COTTERMAN                          63

Border Protection, National Border Patrol Strategy 5 (2005).
The Department of Homeland Security has found that border
searches of electronic storage devices are “essential” for
“detect[ing] evidence relating to terrorism and other national
security matters.”2 Terrorists rely on electronic storage
devices, for example, to copy and alter passports and other
travel documents.3 By providing special privacy protections
for electronic devices at the border, the majority eliminates
the powerful deterrent of suspicionless searches and
significantly aids technologically savvy terrorists and
criminals who rely on encryption and other surreptitious
forms of data storage in their efforts to do harm. See
Martinez-Fuerte, 428 U.S. at 557 (rejecting reasonable
suspicion requirement for vehicle checkpoints near the
Mexican border because to hold otherwise “would largely
eliminate any deterrent to the conduct of well-disguised
smuggling operations”).

    The majority contends that the goal of deterrence does not
justify “any manner of intrusive search” at the border.
Majority at 26. Although I certainly agree with the majority
that a policy objective like deterrence cannot justify an
otherwise unconstitutional “highly intrusive search[] of the
person” at the border, Flores-Montano, 541 U.S. at 152, the
crucial role of deterrence cannot, and should not, be
understated. In fact, the Supreme Court recently affirmed the
importance of deterrence in upholding suspicionless strip


     2
   U.S. Customs and Border Protection, Border Search of Electronic
Devices Containing Information, CBP Directive No. 3340-049 § 1 (2009).

 3
   Thomas R. Eldridge, et al., 9/11 and Terrorist Travel: Staff Report of
the National Commission on Terrorist Attacks Upon the United States 60
(2004).
64            UNITED STATES V . COTTERMAN

searches—the apotheosis of an intrusive search. Florence,
132 S. Ct. at 1516 (rejecting reasonable suspicion
requirement for prison strip searches and reasoning that
“deterring the possession of contraband depends in part on
the ability to conduct searches without predictable
exceptions”). The suspicionless strip search upheld in
Florence, which included a close visual inspection of “the
buttocks or genital areas,” was unquestionably more intrusive
than the so-called “computer strip search” at issue here. Id.
at 1515.

    The majority contends that the deterrence function of
suspicionless searches will not be hampered by the
requirement of reasonable suspicion because, “as a matter of
commonsense and resources, it is only when reasonable
suspicion is aroused that such searches typically take place.”
Majority at 27 n.14. This is, of course, the very argument
rejected by the Fourth Circuit in Ickes. See Ickes, 393 F.3d at
507 (“As a practical matter, computer searches are most
likely to occur where—as here—the traveler’s conduct or the
presence of other items in his possession suggest the need to
search further. However, to state the probability that
reasonable suspicions will give rise to more intrusive
searches is a far cry from enthroning this notion as a matter
of constitutional law.”).

    In addition to undermining deterrence, a reasonable
suspicion requirement will likely disincentivize agents to
conduct laptop searches in close cases. See Florence, 132
S. Ct. at 1522 (“To avoid liability” if required to find
reasonable suspicion, “officers might be inclined not to
conduct a thorough search in any close case, thus creating
unnecessary risk for the entire jail population.”). Border
patrol agents accused of conducting an “unreasonable” search
                 UNITED STATES V . COTTERMAN                       65

face very real consequences—as federal officials, for
example, they may be sued in their individual capacities for
civil damages, as part of a Bivens4 action. See Ronald J.
Sievert, Meeting the Twenty-First Century Terrorist Threat
Within the Scope of Twentieth Century Constitutional Law,
37 Hous. L. Rev. 1421, 1424 (2000). The majority’s
reasonable suspicion requirement saddles border patrol agents
with a “Sophie’s choice” between securing our nation, and
protecting their own livelihoods. These misaligned incentives
create unnecessary risk, not just for a prison population, as in
Florence, 132 S. Ct. at 1522, but for our entire nation.

      C. Expectation of Privacy in Electronic Data at the
         Border

    The majority suggests that travelers at the border have a
heightened expectation of privacy in their electronic storage
devices, due to the “uniquely sensitive nature of [this] data.”
Majority at 25. There is no question that searches of
electronic data are protected by the Fourth Amendment, but
we have never found this data to be immune from the border
search exception. In fact, these electronic storage devices are
hardly a bastion of privacy. When connected to the Internet,
they transmit a massive amount of intimate data to the public
on an almost constant basis, rendering it unremarkable that
they can be searched at the border, where “[t]he government’s
interest in preventing the entry of unwanted persons and
effects is at its zenith.” Flores-Montano, 541 U.S. at 152.

    Indeed, Facebook, for example, now has more than 500
million users, who share

[...TRUNCATED 30934 of 150934 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/United States v. Crews.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "United States v. Crews"
type: case
citation: "445 U.S. 463 (1980)"
parallel_cite: "100 S. Ct. 1244; 63 L. Ed. 2d 537"
neutral_cite: 1980 U.S. LEXIS 1293
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-03-25
docket: 78-777
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Crews
  varies_by_point: false
  scope_note: "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110230/united-states-v-crews/"
  cluster_id: 110230
  opinion_id: 9427838
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Key — Progeny (independent source)"
  - page: "[[Eyewitness Identification]]"
    role: "Related (cross-doctrine)"
related: ["[[Wong Sun v. United States]]", "[[Silverthorne Lumber Co. v. United States]]", "[[United States v. Wade]]", "[[Stovall v. Denno]]", "[[United States v. Ceccolini]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "fruit-of-the-poisonous-tree", "independent-source", "eyewitness-identification"]
holding: "A victim's in-court identification of the accused is not a suppressible fruit of his illegal arrest where the victim's presence and her ability to identify him have an independent source predating the police misconduct."
lake:
  record_id: United States v. Crews
  status: verified
  projected_at: 2026-07-09
---

# United States v. Crews

*445 U.S. 463 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A woman was robbed at gunpoint; she immediately notified police, gave a full description, and the next day voluntarily viewed photographs. Crews was later detained without probable cause, photographed while in custody, and the victim identified his photo and then him at a lineup. The pretrial photographic and lineup identifications were conceded to be suppressible fruits of the illegal arrest; the disputed question was whether the victim's identification of Crews at trial must also be suppressed.

## Issue
Whether a crime victim's in-court identification of the accused must be suppressed as a fruit of the defendant's unlawful arrest.

## Rule
No, where the identification's components have an [[Inevitable Discovery and Independent Source|independent source]] that antedates the illegality. "A victim's in-court identification of the accused has three distinct elements" — the victim's presence to testify, her ability to reconstruct the crime and identify the defendant, and the defendant's own physical presence in the courtroom — and on these facts "none of these three elements 'has been come at by exploitation' of the violation of the defendant's Fourth Amendment rights." — 445 U.S. at 471 (quoting *Wong Sun v. United States*, 371 U.S. 471, 488). ^pin-471

## Application
Each element traced to a source independent of the illegal arrest. The victim's presence was "not traceable to any Fourth Amendment violation," because "the victim's identity was known long before there was any official misconduct." — *Id.* at 472. ^pin-472

Her capacity to identify rested on an independent recollection of the crime itself, uninfluenced by the suppressible pretrial procedures: "the victim's capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity." — *Id.* at 473. ^pin-473

As to the third element, the defendant could not "claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest." — [*Id.* at 474](https://www.courtlistener.com/opinion/110230/united-states-v-crews/#:~:text=claim%20immunity%20from%20prosecution%20simply). ^pin-474

## Conclusion
Because the in-court identification was not the product of the Fourth Amendment violation, it was not a suppressible fruit; the District of Columbia Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Crews* applies the [[Wong Sun v. United States]] / [[Silverthorne Lumber Co. v. United States]] independent-source principle to identification evidence, and dovetails with the [[United States v. Wade]] / [[Stovall v. Denno]] independent-source test for an in-court identification following a tainted pretrial procedure.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny ([[Inevitable Discovery and Independent Source|independent source]])*
- [[Eyewitness Identification]] — *Related (cross-doctrine)*

## Sources
- *United States v. Crews*, 445 U.S. 463 (1980) — https://www.courtlistener.com/opinion/110230/united-states-v-crews/ — pinpoints: 471, 472, 473, 474.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "64416a9ae950d1ae", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Crews"}, "payload": {"all": [{"cite": "445 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "445"}, {"cite": "100 S. Ct. 1244", "page": "1244", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "63 L. Ed. 2d 537", "page": "537", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "63"}, {"cite": "1980 U.S. LEXIS 1293", "page": "1293", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "445 U.S. 463", "official": {"cite": "445 U.S. 463", "page": "463", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "445"}, "official_selection_present": true, "record_id": "United States v. Crews"}}
{"assertion_id": "38a91ef9bc1d140d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-472", "record_id": "United States v. Crews"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-472", "pinpoint_status": "slip-only", "quote": "not traceable to any Fourth Amendment violation,", "quote_fidelity": "mismatch", "record_id": "United States v. Crews", "star_marker": null}}
{"assertion_id": "9acfa5ae99233539", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-474", "record_id": "United States v. Crews"}, "payload": {"fragment": "#:~:text=claim%20immunity%20from%20prosecution%20simply", "page": null, "pin_id": "pin-474", "pinpoint_status": "star-verified", "quote": "claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest.", "quote_fidelity": "matched", "record_id": "United States v. Crews", "star_marker": "474"}}
{"assertion_id": "a4a99a60e63d2561", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-473", "record_id": "United States v. Crews"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-473", "pinpoint_status": "slip-only", "quote": "the victim's capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity.", "quote_fidelity": "mismatch", "record_id": "United States v. Crews", "star_marker": null}}
{"assertion_id": "b84d776364e617f7", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-471", "record_id": "United States v. Crews"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-471", "pinpoint_status": "slip-only", "quote": "--- # United States v. Crews *445 U.S. 463 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A woman was robbed at gunpoint; she immediately notified police, gave a full description, and the next day voluntarily viewed photographs. Crews was later detained without probable cause, photographed while in custody, and the victim identified his photo and then him at a lineup. The pretrial photographic and lineup identifications were conceded to be suppressible fruits of the illegal arrest; the disputed question was whether the victim's identification of Crews at trial must also be suppressed. ## Issue Whether a crime victim's in-court identification of the accused must be suppressed as a fruit of the defendant's unlawful arrest. ## Rule No, where the identification's components have an independent source that antedates the illegality.", "quote_fidelity": "mismatch", "record_id": "United States v. Crews", "star_marker": null}}
{"assertion_id": "60ef1600af844c2e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Crews"}, "payload": {"as_of_content": "1980-03-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Crews", "scope_note": "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law.", "varies_by_point": false}}
```

### lake record — United States v. Crews

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Crews",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Crews",
    "case_name_short": "Crews",
    "case_name_full": "United States v. Crews",
    "input_case_name": "United States v. Crews",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-03-25",
    "year": 1980,
    "docket": "78-777",
    "cluster_id": 110230,
    "lead_opinion_id": 9427838,
    "sibling_ids": [
      110230,
      9427838,
      9427839,
      9427840
    ],
    "absolute_url": "/opinion/110230/united-states-v-crews/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 463",
      "volume": "445",
      "reporter": "U.S.",
      "page": "463",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1244",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1244",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 537",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 1293",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "1293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 463",
        "volume": "445",
        "reporter": "U.S.",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1244",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1244",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 537",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "537",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 1293",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "1293",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 463",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 463",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-471",
      "page": null,
      "quote": "--- # United States v. Crews *445 U.S. 463 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A woman was robbed at gunpoint; she immediately notified police, gave a full description, and the next day voluntarily viewed photographs. Crews was later detained without probable cause, photographed while in custody, and the victim identified his photo and then him at a lineup. The pretrial photographic and lineup identifications were conceded to be suppressible fruits of the illegal arrest; the disputed question was whether the victim's identification of Crews at trial must also be suppressed. ## Issue Whether a crime victim's in-court identification of the accused must be suppressed as a fruit of the defendant's unlawful arrest. ## Rule No, where the identification's components have an independent source that antedates the illegality.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-472",
      "page": null,
      "quote": "not traceable to any Fourth Amendment violation,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-473",
      "page": null,
      "quote": "the victim's capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-474",
      "page": null,
      "quote": "claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest.",
      "star_marker": "474",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15824,
      "fragment": "#:~:text=claim%20immunity%20from%20prosecution%20simply",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Crews",
    "varies_by_point": false,
    "scope_note": "The independent-source analysis of an in-court identification, and the rule that a defendant's presence is not a suppressible fruit, remain good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Parker Chad Ross v. Commonwealth of Virginia",
          "cluster_id": 1061425,
          "cite": [
            "61 Va. App. 752",
            "739 S.E.2d 910",
            "2013 WL 1564533",
            "2013 Va. App. LEXIS 115"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Young v. Conway",
          "cluster_id": 810124,
          "cite": [
            "698 F.3d 69",
            "2012 U.S. App. LEXIS 21502",
            "2012 WL 4876235"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 5901088,
          "cite": [
            "53 A.D.3d 1151",
            "860 N.Y.S.2d 780"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 6356597,
          "cite": [
            "19 Misc. 3d 675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olivarez v. State",
          "cluster_id": 1560637,
          "cite": [
            "171 S.W.3d 283",
            "2005 WL 1385355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 6588047,
          "cite": [
            "63 Mass. App. Ct. 587",
            "827 N.E.2d 1263",
            "2005 Mass. App. LEXIS 489"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Henderson v. State",
          "cluster_id": 1745593,
          "cite": [
            "82 S.W.3d 750",
            "2002 WL 1590495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leonard Henderson v. State",
          "cluster_id": 2920338,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Astuto",
          "cluster_id": 6173483,
          "cite": [
            "263 A.D.2d 459",
            "694 N.Y.S.2d 407",
            "1999 N.Y. App. Div. LEXIS 7765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane1_negative"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
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
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. MacOn",
          "cluster_id": 111477,
          "cite": [
            "86 L. Ed. 2d 370",
            "105 S. Ct. 2778",
            "472 U.S. 463",
            "1985 U.S. LEXIS 110",
            "53 U.S.L.W. 4783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pablo Escoboza Vega",
          "cluster_id": 403767,
          "cite": [
            "678 F.2d 376",
            "1982 U.S. App. LEXIS 18982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Geisler",
          "cluster_id": 7894925,
          "cite": [
            "222 Conn. 672",
            "610 A.2d 1225",
            "61 U.S.L.W. 2093",
            "1992 Conn. LEXIS 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ortiz v. Barkley",
          "cluster_id": 1810562,
          "cite": [
            "558 F. Supp. 2d 444",
            "2008 U.S. Dist. LEXIS 43653",
            "2008 WL 2266313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1377787,
          "cite": [
            "751 P.2d 395",
            "44 Cal. 3d 883",
            "245 Cal. Rptr. 336",
            "1988 Cal. LEXIS 74"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dodt",
          "cluster_id": 5686979,
          "cite": [
            "61 N.Y.2d 408",
            "462 N.E.2d 1159",
            "474 N.Y.S.2d 441",
            "1984 N.Y. LEXIS 4120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vanderbilt v. State",
          "cluster_id": 2459138,
          "cite": [
            "629 S.W.2d 709",
            "1981 Tex. Crim. App. LEXIS 1156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. $191,910.00 in U.S. Currency, Bruce R. Morgan, Claimant-Appellee",
          "cluster_id": 663161,
          "cite": [
            "16 F.3d 1051",
            "94 Daily Journal DAR 2139",
            "94 Cal. Daily Op. Serv. 1214",
            "1994 U.S. App. LEXIS 2681",
            "1994 WL 46744"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thurman",
          "cluster_id": 1367765,
          "cite": [
            "846 P.2d 1256",
            "203 Utah Adv. Rep. 18",
            "1993 Utah LEXIS 40",
            "1993 WL 4794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brnja",
          "cluster_id": 5684289,
          "cite": [
            "50 N.Y.2d 366",
            "406 N.E.2d 1066",
            "429 N.Y.S.2d 173",
            "1980 N.Y. LEXIS 2356"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fleming v. State",
          "cluster_id": 1702179,
          "cite": [
            "604 So. 2d 280",
            "1992 WL 132439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, State of California, Intervenor v. Raphyal Crawford, AKA Aarmyl Crawford",
          "cluster_id": 786677,
          "cite": [
            "372 F.3d 1048",
            "2004 U.S. App. LEXIS 12116",
            "2004 WL 1375521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnny L. Marshall v. Secretary, Florida Department of Corrections",
          "cluster_id": 4237860,
          "cite": [
            "828 F.3d 1277",
            "2016 U.S. App. LEXIS 12812",
            "2016 WL 3742164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Colon",
          "cluster_id": 198134,
          "cite": [
            "157 F.3d 9",
            "1998 U.S. App. LEXIS 24862",
            "1998 WL 671324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Manbeck, United States of America v. Kenneth Herring, United States of America v. Mark Huiet Sale, United States of America v. Lorenz Josephus Proden, United States of America v. Kermit Theodore Brogden, United States of America v. John Wesley Flannel, United States of America v. Gary Gallopo, United States of America v. John Benjamin Barton, Jr., Jessie Lee Mallory, and Arthur Duncan, United States of America v. John O'hare, Eddie Brantley, Thomas Earnest Folske, Thomas Sams Hightower, Timothy Allen Laxton, Harrell Lewis, Jr., and John Isidore Stevens, United States of America v. Aaron Douglas Staetter, John Michael Iyoob, James Anthony Hastings, and Gregory Michael Scott, United States of America v. David Martin Summerville",
          "cluster_id": 441989,
          "cite": [
            "744 F.2d 360",
            "1984 U.S. App. LEXIS 18698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Oliver L. North",
          "cluster_id": 552750,
          "cite": [
            "920 F.2d 940",
            "287 U.S. App. D.C. 146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George Terzado-Madruga",
          "cluster_id": 537704,
          "cite": [
            "897 F.2d 1099",
            "1990 WL 27249"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. Nevada",
          "cluster_id": 117833,
          "cite": [
            "128 L. Ed. 2d 1",
            "114 S. Ct. 1280",
            "511 U.S. 79",
            "1994 U.S. LEXIS 2655"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "110OAG40",
          "cluster_id": 10638768,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane3_recency"
      },
      {
        "citing_case": {
          "name": "Maryland Attorney General Opinion 110OAG40",
          "cluster_id": 10848272,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Crews:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MjIwNjA4MDAwMDAmcz0xMTk5NjAxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAmcz01Njg2MTk2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
        "reviewed": 18,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 18,
        "triage_read": 2,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110230 OR 9427838 OR 9427839 OR 9427840)",
    "indexed_citing_opinions": 738,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110230,
        "count": 643,
        "count_source": "search"
      },
      {
        "opinion_id": 9427838,
        "count": 111,
        "count_source": "search"
      },
      {
        "opinion_id": 9427839,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1155,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-crews.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5NDQwNyZzPTgyNDQ5NzEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110230+OR+9427838+OR+9427839+OR+9427840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110230,
        "cited_id": 91772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107238,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 109693,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 237954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 250068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 332396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 1920133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110230,
        "cited_id": 2073438,
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
    "date_created": "2026-07-05T23:25:11Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T23:36:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T23:25:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Crews

```
<opinion type="majority">
<author id="b525-5">Mr. Justice Brennan</author>
<p id="AKJ">delivered the opinion of the Court, except as to Part II-D.</p>
<p id="b525-6">We are called upon to decide whether in the circumstances of this case an in-court identification of the accused by the victim of a crime should be suppressed as the fruit of the defendant’s unlawful arrest.</p>
<p id="b525-7">I</p>
<p id="b525-8">On the morning of January 3, 1974, a woman was accosted and robbed at gunpoint by a young man in the women’s restroom on the grounds of the Washington Monument. Her assailant, peering at her through a 4-inch crack between the wall and the door of the stall she occupied, asked for $10 and demanded that he be let into the stall. When the woman refused, the robber pointed a pistol over the top of the door and repeated his ultimatum. The victim then surrendered the money, but the youth demanded an additional $10. When the woman opened her purse and showed her assailant that she had no more cash, he gained entry to her stall and made sexual advances upon her. She tried to resist and pleaded with him to leave. He eventually did, warning his victim that he would shoot her if she did not wait at least 20 minutes before following him out of the restroom. The woman complied, and upon leaving the restroom 20 minutes later, immediately reported the incident to the police.</p>
<p id="b525-9">On January 6, two other women were assaulted and robbed in a similar episode in the same restroom. A young man threatened the women with a broken bottle, forced them to hand over $20, and then departed, again cautioning his victims not to leave for 20 minutes. The description of the <page-number citation-index="1" label="466">*466</page-number>robber given to the police by these women matched that given by the first victim: All three described their assailant as a young black male, 15-18 years old, approximately 5'5" to 5'8" tall, slender in build, with a very dark complexion and smooth skin.</p>
<p id="b526-5">Three days later, on January 9, Officer David Rayfield of the United States Park Police observed respondent in the area of the Washington Monument concession stand and restrooms. Aware of the robberies of the previous week and noting respondent’s resemblance to the police “lookout” that described the perpetrator, the officer and his partner approached respondent.<footnotemark>1</footnotemark> Respondent gave the officers his name and said that he was 16 years old. When asked why he was not in school, respondent replied that he had just “walked away from school.” <footnotemark>2</footnotemark> The officers informed respondent of his likeness to the suspect’s description, but there was no further questioning about those events. Respondent was allowed to leave, and the officers watched as he entered the nearby restrooms.</p>
<p id="b526-6">While respondent was still inside, Officer Rayfield saw and spoke to James Dickens, a tour guide who had previously reported having seen a young man hanging around the area of the Monument on the day of the January 3d robbery. In response to the officer’s request to observe respondent as he left the restroom, Dickens tentatively identified him as the individual he had seen on the day of the robbery.</p>
<p id="b526-7">On the basis of this additional information, the officers again approached respondent and detained him. Detective Earl Ore, the investigator assigned to the robberies, was immediately summoned. Upon his arrival some 10 or 15 minutes later, Detective Ore attempted to take a Polaroid photo<page-number citation-index="1" label="467">*467</page-number>graph of respondent, but the inclement weather conditions frustrated his several efforts to produce a picture suitable for display to the robbery victims. Respondent was therefore taken into custody, ostensibly because he was a suspected truant. He was then transported to Park Police headquarters, where the police briefly questioned him, obtained the desired photograph, telephoned his school, and released him. Respondent was never formally arrested or charged with any offense, and his detention at the station lasted no more than an hour.</p>
<p id="b527-5">On the following day, January 10, the police showed the victim of the first robbery an array of eight photographs, including one of respondent. Although she had previously viewed over 100 pictures of possible suspects without identifying any of them as her assailant, she immediately selected respondent’s photograph as that of the man who had robbed her. On January 13, one of the other victims made a similar identification.<footnotemark>3</footnotemark> Respondent was again taken into custody, and at a court-ordered lineup held on January 21, he was positively identified by the two women who had made the photographic identifications.</p>
<p id="b527-6">The grand jury returned an indictment against respondent on February 22, 1974, charging him with two counts of armed robbery, two counts of robbery, one count of attempted armed robbery, and three counts of assault with a dangerous weapon.<footnotemark>4</footnotemark> Respondent filed a pretrial motion to suppress all identification testimony, contending that his detention on the truancy charges had been merely a pretext to allow the police to obtain evidence for the robbery investigation. After hearing extensive testimony from the three victims, the police officers, and respondent, the trial court found that the respondent’s detention at Park Police headquarters on January 9 consti<page-number citation-index="1" label="468">*468</page-number>tuted an arrest without probable cause.<footnotemark>5</footnotemark> Accordingly, the court ruled that the products of that arrest — the photographic and lineup identifications — could not be introduced at trial. But the judge concluded that the victims’ ability to identify respondent in court was based upon independent recollection untainted by the intervening identifications, and therefore held such testimony admissible. At trial, all three victims identified respondent as their assailant. On April 23, the jury convicted him of armed robbery of the first victim, but returned verdicts of not guilty on all other charges.<footnotemark>6</footnotemark> Respondent was sentenced to four years’ probation under the Federal Youth Corrections Act, <span class="citation no-link">18 U. S. C. § 5010</span> (a).</p>
<p id="b528-5">On appeal, the District of Columbia Court of Appeals, sitting en banc, reversed respondent’s conviction and ordered the suppression of the first robbery victim’s in-court identi<page-number citation-index="1" label="469">*469</page-number>fication.<footnotemark>7</footnotemark> <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/" aria-description="Citation for case: Crews v. United States">389 A. 2d 277</a></span> (1978). The court viewed its decision to be a wholly conventional application of the familiar “fruit of the poisonous tree” doctrine. See <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920). After upholding the trial court’s finding that respondent was detained without probable cause — a determination that is not challenged in this Court<footnotemark>8</footnotemark> — the Court of Appeals turned to consideration of what evidentiary consequences ought to flow from that Fourth Amendment violation. In deciding whether the in-court identification should have been suppressed, the court observed that the analysis must focus on whether the evidence was obtained by official “exploitation” of the “primary illegality” within the meaning of <em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span></em><footnotemark><em>9</em></footnotemark><em> </em>and that the principal issue was whether the unlawful police behavior bore a causal relationship to the acquisition of the challenged testimony. The court answered that question in the affirmative, reasoning that but for respondent’s unlawful arrest, the police would not have obtained the photograph that led to his subsequent identification by the complaining witnesses and, ultimately, prosecution of the case.<footnotemark>10</footnotemark> Satisfied that the <page-number citation-index="1" label="470">*470</page-number>in-court identification was thus at least indirectly the product of official misconduct, the court then considered whether any of three commonly advanced exceptions to the exclusionary rule — the “independent source,” “inevitable discovery,” or “attentuation” doctrines<footnotemark>11</footnotemark> — nonetheless justified its admission. Finding these exceptions inapplicable, the Court of Appeals concluded that, the in-court identification testimony should have been excluded as a product of the violation of respondent’s Fourth Amendment rights. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./440/907/">440 U. S. 907</a></span> (1979). We reverse.</p>
<p id="b530-5">II</p>
<p id="b530-6"><em>Wong <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Sun, supra,</a></span> </em>articulated the guiding principle for determining whether evidence derivatively obtained from a violation of the Fourth Amendment is admissible against the accused at trial: “The exclusionary prohibition extends as well to the indirect as the direct products of such invasions.” <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 484</a></span>. See <em>Silverthome Lumber Co. </em>v. <em>United States, supra; Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914). As subsequent cases have confirmed, the exclusionary sanction applies to any “fruits” of a constitutional violation — whether such evidence be tangible, physical material actually seized in an illegal search,<footnotemark>12</footnotemark> items observed or words overheard in the course of the unlawful activity,<footnotemark>13</footnotemark> or confessions or statements of the accused obtained during an illegal arrest and detention.<footnotemark>14</footnotemark></p>
<p id="b531-4"><page-number citation-index="1" label="471">*471</page-number>In the typical “fruit of the poisonous tree” case, however, the challenged evidence was acquired by the police <em>after </em>some initial Fourth Amendment violation, and the question before the court is whether the chain of causation proceeding from the unlawful conduct has become so attenuated or has been interrupted by some intervening circumstance so as to remove the “taint” imposed upon that evidence by the original illegality. Thus most cases begin with the premise that the challenged evidence is in some sense the product of illegal governmental activity. It is the Court of Appeals’ application of that premise to the facts of this case that we find erroneous.</p>
<p id="b531-5">A ,victim’s in-court identification of the accused has three distinct elements. First, the victim is present at trial to testify as to what transpired between her and the offender, and to identify the defendant as the culprit. Second, the victim possesses knowledge of and the ability to reconstruct the prior criminal occurrence and to identify the defendant from her observations of him at the time of the crime. And third, the defendant is also physically present in the courtroom, so that the victim can observe him and compare his appearance to that of the offender. In the present case, it is our conclusion that none of these three elements “has been come at by exploitation” of the violation of the defendant’s Fourth Amendment rights. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States"><em>Wong Sun, supra, </em>at 488</a></span>.</p>
<p id="b531-6">A</p>
<p id="b531-7">In this case, the robbery victim’s presence in the courtroom at respondent’s trial was surely not the product of any police misconduct. She had notified the authorities immediately after the attack and had given them a full description of her assailant. The very next day, she went to the police station to view photographs of possible suspects, and she voluntarily assisted the police in their investigation at all times. Thus this is not a case in which the witness’ identity was discovered or her cooperation secured only as a result of an unlawful <page-number citation-index="1" label="472">*472</page-number>search or arrest of the accused.<footnotemark>15</footnotemark> Here the victim’s identity was known long before there was any official misconduct, and her presence in court is thus not traceable to any Fourth Amendment violation.</p>
<p id="b532-5">B</p>
<p id="b532-6">Nor did the illegal arrest infect the victim’s ability to give accurate identification testimony. Based upon her observations at the time of the robbery, the victim constructed a mental image of her assailant. At trial, she retrieved this mnemonic representation, compared it to the figure of the defendant, and positively identified him as the robber.<footnotemark>16</footnotemark> No part of this process was affected by respondent’s illegal arrest. In the language of the “time-worn metaphor” of the poisonous tree, <em>Harrison </em>v. <em>United </em>States, <span class="citation" data-id="9423779"><a href="/opinion/107736/harrison-v-united-states/#222" aria-description="Citation for case: Harrison v. United States">392 U. S. 219, 222</a></span> (1968), the toxin in this case was injected only after the evidentiary bud had blossomed; the fruit served at trial was not poisoned.</p>
<p id="b532-7">This is not to say that the intervening photographic and lineup identifications — both of which are conceded to be suppressible fruits of the Fourth Amendment violation — could not under some circumstances affect the reliability of the in-court identification and render it inadmissible as well. Indeed, given the vagaries of human memory and the inherent suggestibility of many identification procedures,<footnotemark>17</footnotemark> just <page-number citation-index="1" label="473">*473</page-number>the opposite may be true. But in the present case the trial court expressly found that the witness’ courtroom identification rested on an independent recollection of her initial encounter with the assailant, uninfluenced by the pretrial identifications, and this determination finds ample support in the record.<footnotemark>18</footnotemark> In short, the victim’s capacity to identify her assailant in court neither resulted from nor was biased by the unlawful police conduct committed long after she had developed that capacity.<footnotemark>19</footnotemark></p>
<p id="b534-3"><page-number citation-index="1" label="474">*474</page-number>c</p>
<p id="b534-4">Insofar as respondent challenges his own presence at trial, he cannot claim immunity from prosecution simply because his appearance in court was precipitated by an unlawful arrest. An illegal arrest, without more, has never been viewed as a bar to subsequent prosecution, nor as a defense to a valid conviction. <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#119" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 119</a></span> (1975); <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952); <em>Ker </em>v. <em>Illinois, </em><span class="citation" data-id="91772"><a href="/opinion/91772/ker-v-illinois/" aria-description="Citation for case: Ker v. Illinois">119 U. S. 436</a></span> (1886).<footnotemark>20</footnotemark> The exclusionary principle of <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span> </em>and <em>Silverthorne Lumber Co. </em>delimits what proof the Government may offer against the accused at trial, closing the courtroom door to evidence secured by official lawlessness. Respondent is not himself a suppressible “fruit,” and the illegality of his detention cannot deprive the Government of the opportunity to prove his guilt through the introduction of evidence wholly untainted by the police misconduct.</p>
<p id="b534-5">D<footnotemark>*</footnotemark></p>
<p id="b534-6">Respondent argues, however, that in one respect his corpus is itself a species of “evidence.” When the victim singles out respondent and declares, “That’s the man who robbed me,” his physiognomy becomes something of evidentary value, much like a photograph showing respondent at the scene of the <page-number citation-index="1" label="475">*475</page-number>crime.<footnotemark>21</footnotemark> And, as with, the introduction of such a photograph, he contends that the crucial inquiry for Fourth Amendment purposes is whether that evidence has become available only as a result of official misconduct. We read the Court of Appeals’ opinion as essentially adopting this analysis to support its suppression order. See <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#285" aria-description="Citation for case: Crews v. United States">389 A. 2d, at 285-287</a></span>.</p>
<p id="b535-5">We need not decide whether respondent’s person should be considered evidence, and therefore a possible “fruit” of police misconduct. For in this case the record plainly discloses that prior to his illegal arrest, the police both knew respondent’s identity and had some basis to suspect his involvement in the very crimes with which he was charged. Moreover, before they approached respondent, the police had already obtained access to the “evidence” that implicated him in the robberies, <em>i. e., </em>the mnemonic representations of the criminal retained by the victims and related to the police in the form of their agreement upon his description. In short, the Fourth Amendment violation in this case yielded nothing of evidentiary value that the police did not already have in their grasp.<footnotemark>22</footnotemark> Rather, respondent’s unlawful arrest served merely to link together two extant ingredients in his identification. The exclusionary rule enjoins the Government from benefiting from evidence it has unlawfully obtained; it does not reach backward to taint information that was in official hands prior to any illegality.</p>
<p id="b535-6">Accordingly, this case is very different from one like <em>Davis </em>v. <em>Mississippi, </em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), in which the defendant’s identity and connection to the illicit activity were only first discovered through an illegal arrest or search. In that case, the defendant’s fingerprints were ordered suppressed as the <page-number citation-index="1" label="476">*476</page-number>fruits of an unlawful detention. A woman had been raped in her home, and during the next 10 days, the local police rounded up scores of black youths, randomly stopping, interrogating, and fingerprinting them. Davis’ prints were discovered to match a set found at the scene of the crime, and on that basis he was arrested and convicted. Had it not been for Davis’ illegal detention, however, his prints would not have been obtained and he would never have become a suspect.' Here, in contrast, the robbery investigation had already focused on respondent, and the police had independent reasonable grounds to suspect his culpability.</p>
<p id="b536-5">We find <em>Bynum </em>v. <em>United States, </em>104 U. S. App. D. C. 368, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span> (1958), cited with approval in <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#724" aria-description="Citation for case: Davis v. Mississippi"><em>Davis, supra, </em>at 724</a></span>, helpful in our analysis as well. In <em><span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">Bynum</a></span>, </em>the defendant voluntarily came down to the police station to look for his brother, who had been arrested earlier that day while driving an auto sought in connection with a robbery. After telling one of the officers that he owned the car, Bynum was arrested and fingerprinted. Those prints were later found to match a set at the scene of the robbery, and Bynum was convicted based in part on that evidence. The Court of Appeals held that the police lacked probable cause at the time of Bynum’s arrest, and it ordered the prints suppressed as “something of evidentiary value which the public authorities have caused an arrested person to yield to them during illegal detention.” 104 U. S. App. D. C., at 370, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#467" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 467</a></span>. As this Court noted in <em><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>, </em>however, <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#725" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 725-726, n. 4</a></span>, Bynum was subsequently reindicted for the same offense, and the Government on retrial introduced an older set of his fingerprints, taken from an FBI file, that were in no' way connected with his unlawful arrest. The Court of Appeals affirmed that conviction, holding that the fingerprint identification made on the basis of information already in the FBI’s possession was not tainted by the subsequent illegality and was therefore admissible. <em>Bynum </em>v. <em>United States, </em>107 U. S. App. D. C. 109, <span class="citation" data-id="250068"><a href="/opinion/250068/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">274 F. 2d 767</a></span> (1960).</p>
<p id="b537-4"><page-number citation-index="1" label="477">*477</page-number>The parallels between <em>Bynum </em>and this case are apparent: The pretrial identification obtained through use of the photograph taken during respondent’s illegal detention cannot be <em>introduced; </em>but the in-court identification is admissible, even if respondent’s argument be accepted, because the police’s knowledge of respondent’s identity and the victim’s independent recollections of him both antedated the unlawful arrest and were thus untainted by the constitutional violation. The judgment of the Court of Appeals is accordingly</p>
<p id="b537-5">
<em>Reversed.</em>
</p>
<judges id="b537-6">Mr. Justice Marshall took no part in the consideration or decision of this case.</judges>
<footnote label="1">
<p id="b526-8"> Officer Rayfield testified that his suspicions were further aroused both by respondent’s presence on the almost deserted park grounds and by his apparently aimless meanderings around the restroom and concessions area.</p>
</footnote>
<footnote label="2">
<p id="b526-9"><em> </em>Tr. 52. References are to the transcript of the suppression hearing and trial held on April 22 and 23, 1974, in the Superior Court of the District of Columbia.</p>
</footnote>
<footnote label="3">
<p id="b527-7"> The third victim did not review the photographic array, nor did she attend the subsequent lineup.</p>
</footnote>
<footnote label="4">
<p id="b527-8"> See D. C. Code §§ 22-502, 22-2901, and 22-3202 (1973).</p>
</footnote>
<footnote label="5">
<p id="b528-6"> The suppression hearing produced conflicting testimony as to the reasons for the attempt to photograph respondent. Officer Rayfield asserted that respondent was processed as a routine juvenile truant, a procedure that involves photographing the suspect and then calling his school and home to determine whether he is in fact truant. Tr. 53-54. Rayfield did acknowledge, however, that he had some suspicion that respondent was the robber described in the police description. <em>Id., </em>at 55, 57. Similarly, Detective Ore, while maintaining that respondent was apprehended and taken down to Park Police headquarters as a suspected truant, <em>id., </em>at 61, 63, admitted that his intent in trying to photograph him was to obtain a picture that could be shown to the complaining witnesses. <em>Id., </em>at 59.</p>
<p id="b528-7">The Government does not now attempt to justify respondent’s detention on the truancy charge, nor did it raise that argument in the court below. The Court of Appeals found that the procedures followed in respondent’s case did not conform to the typical truancy practices described by the police and that the officers never even superficially pursued the truancy matter. By the same token, the court expressly disavowed the existence of a “sham” or “pretext” arrest, and it analyzed respondent’s apprehension as a traditional arrest for armed robbery and assault without probable cause. <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#299" aria-description="Citation for case: Crews v. United States">389 A. 2d 277, 299-300, n. 32</a></span> (DC 1978).</p>
</footnote>
<footnote label="6">
<p id="b528-8"> Because respondent was acquitted of all charges in connection with the robberies of January 6, the only issue raised on his appeal was the admissibility of the first robbery victim’s in-court identification.</p>
</footnote>
<footnote label="7">
<p id="b529-5"> On February 16, 1977, a division of the Court of Appeals originally affirmed respondent’s conviction, <span class="citation" data-id="9695751"><a href="/opinion/1920133/crews-v-united-states/" aria-description="Citation for case: Crews v. United States">369 A. 2d 1063</a></span>. Three months later, however, the full court granted respondent’s motion for rehearing and vacated its earlier judgment. Record 356.</p>
</footnote>
<footnote label="8">
<p id="b529-6"> See Brief for United States 5, n. 4.</p>
</footnote>
<footnote label="9">
<p id="b529-7"> “We need not hold that all evidence is ‘fruit of the poisonous tree’ simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a ease is 'whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.’ Maguire, Evidence of Guilt, 221 (1959).” <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 487-488</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b529-8"> “[T]he unlawful arrest produced photographs which were shown to the complaining witnesses who, as a result, identified [respondent); this resulted in his reapprehension, which yielded a court-ordered lineup iden<page-number citation-index="1" label="470">*470</page-number>tification and, eventually, in-court identification testimony during prosecution of the case.” <span class="citation" data-id="9711085"><a href="/opinion/2073438/crews-v-united-states/#289" aria-description="Citation for case: Crews v. United States">389 A. 2d, at 289</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b530-8"> See <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939) (attenuation); <em>Silverthome Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920) (independent source); <em>United States ex rel. Owens </em>v. <em>Twomey, </em><span class="citation" data-id="324383"><a href="/opinion/324383/united-states-of-america-ex-rel-jesse-owens-v-john-j-twomey-warden/#865" aria-description="Citation for case: United States of America Ex Rel. Jesse Owens v. John J....">508 F. 2d 858, 865</a></span> (CA7 1974) (inevitable discovery).</p>
</footnote>
<footnote label="12">
<p id="b530-9"> <em>E. g., Whiteley </em>v. <em>Warden, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560</a></span> (1971); <em>Sibron </em>v. <em>New York, </em><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968); <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span> (1964).</p>
</footnote>
<footnote label="13">
<p id="b530-10"> <em>E. g., United States </em>v. <em>Giordano, </em><span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span> (1974).; see <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961); <em>McGinnis </em>v. <em>United States, </em><span class="citation" data-id="6912304"><a href="/opinion/7011844/mcginnis-v-united-states/" aria-description="Citation for case: McGinnis v. United States">227 F. 2d 598</a></span> (CA1 1955).</p>
</footnote>
<footnote label="14">
<p id="b530-11"> <em>E. g., Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span> (1979); <em>Brown </em>v. <em>Illinois, </em><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975).</p>
</footnote>
<footnote label="15">
<p id="b532-8"> See generally Ruffin, Out on a Limb of the Poisonous Tree: The Tainted Witness, <span class="citation no-link">15 UCLA L. Rev. 32</span> (1967).</p>
</footnote>
<footnote label="16">
<p id="b532-9"> At oral argument, the Government compared the witness’ mental image to an undeveloped photograph of the robber that is given to the police immediately after the crime, but which becomes visible only at the trial. Tr. of Oral Arg. 11-12. Although this analogy may not comport precisely with current psychological theories of perception, see, <em>e. g., </em>Buckout, Eyewitness Testimony, Scientific American 23 (Dec. 1974), it is apt for purposes of analysis.</p>
</footnote>
<footnote label="17">
<p id="b532-10"> See, e. <em>g., </em>P. Wall, Eye-Witness Identification in Criminal Cases 40-64 (1965); Note,. Did Your Eyes Deceive You? Expert Psychological Testimony on the Unreliability of Eyewitness Identification, <span class="citation no-link">29 Stan. L. Rev. 969</span>, 974-989 (1977).</p>
</footnote>
<footnote label="18">
<p id="b533-5"> <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), enumerated several factors for consideration in applying the “independent origins” test. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#241" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 241</a></span>. Cf. <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U. S. 98</a></span> (1977); <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972). We attach particular significance to the following circumstances which support the trial court’s determination in this case: the victim viewed her assailant at close range for a period of 5-10 minutes under excellent lighting conditions and with no distractions, Tr. 4, 7, 111; respondent closely matched the description given by the victim immediately after the robbery, <em>id., </em>at 52, 59; the victim failed to identify anyone other than respondent, <em>id., </em>at 8, but twice selected respondent without hesitation in nonsuggestive pretrial identification procedures, <em>id., </em>at 9-11; and only a week had passed between the victim’s initial observation of respondent and her first identification of him, <em>id., </em>at 8-9.</p>
<p id="b533-6">Our reliance on the fact that the witness twice identified respondent in out-of-court confrontations is not intended to assign any independent evidentiary value to those identifications for to do so would undermine the exclusionary rule’s objectives in denying the Government the benefit of any evidence wrongfully obtained. Rather, the accurate pretrial identifications assume significance only to the extent that they indicate that the witness’ ability to identify respondent antedated any police misconduct, and hence that her in-court identification had an “independent source.”</p>
</footnote>
<footnote label="19">
<p id="b533-7"> Respondent contends that the “independent source” test of <em>United States </em>v. <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade, supra,</a></span> </em>and <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), although derived from an identical formulation in <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>see 388 U. S., at 241, seeks only to determine whether the in-court identification is sufficiently reliable to satisfy due process, and is thus inapplicable in the context of this Fourth Amendment violation. We agree that a satisfactory resolution of the reliability issue does not provide a complete answer to the considerations underlying <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>but note only that in the present case both concerns are met.</p>
</footnote>
<footnote label="20">
<p id="b534-7"> Cf. <em>United States </em>v. <em>Blue, </em><span class="citation" data-id="107238"><a href="/opinion/107238/united-states-v-blue/#255" aria-description="Citation for case: United States v. Blue">384 U. S. 251, 255</a></span> (1966):</p>
<blockquote id="b534-8">“Our numerous precedents ordering the exclusion of such illegally obtained evidence assume implicitly that the remedy does not extend to barring the prosecution altogether. So drastic a step might advance marginally some of the ends served by exclusionary rules, but it would also increase to an intolerable degree interference with the public interest in having the guilty brought to book.”</blockquote>
<p id="b534-9">In some cases, of course, prosecution may effectively be foreclosed by the absence of the challenged evidence. But this contemplated consequence is the product of the exclusion of specific evidence tainted by the Fourth Amendment violation and is not the result of a complete bar to prosecution.</p>
</footnote>
<footnote label="*">
<p id="b534-10">This part is joined only by Mb. Justice Stewart and Mr. Justice Stevens.</p>
</footnote>
<footnote label="21">
<p id="b535-7"> Cf. <em>Stevenson </em>v. <em>Mathews, </em><span class="citation" data-id="332396"><a href="/opinion/332396/kurt-stevenson-v-james-w-mathews-warden-wisconsin-correctional-camp/#63" aria-description="Citation for case: Kurt Stevenson v. James W. Mathews, Warden, Wisconsin...">529 F. 2d 61, 63</a></span> (CA7 1976).</p>
</footnote>
<footnote label="22">
<p id="b535-8"> Thus we are not called upon in this ease to hypothesize about whether routine investigatory procedures would eventually have led the police to discover respondent’s culpability. His involvement in the robberies was already suspected, and no new evidence was acquired through the violation of his Fourth Amendment rights.</p>
</footnote>
</opinion>
```

---
