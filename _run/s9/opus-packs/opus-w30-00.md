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

## GROUP: content/cases/City of Tahlequah v. Bond.md  (`case`, 5 assertions)

### content_page

```
---
title: "City of Tahlequah v. Bond"
type: case
citation: "595 U.S. 9 (2021)"
parallel_cite: ""
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2021
date_decided: 2021-10-18
docket: 20-1668
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2021-10-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: City of Tahlequah v. Bond
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/5292018/city-of-tahlequah-v-bond/"
  cluster_id: 5292018
  opinion_id: 5120580
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[District of Columbia v. Wesby]]", "[[Graham v. Connor]]", "[[Harlow v. Fitzgerald]]", "[[Hope v. Pelzer]]"]
aliases: ["Tahlequah v. Bond"]
tags: ["case", "qualified-immunity", "section-1983", "excessive-force", "clearly-established-law", "per-curiam"]
holding: "Courts must not define clearly established law at too high a level of generality; QI protects 'all but the plainly incompetent or those who knowingly violate the law.'"
lake:
  record_id: City of Tahlequah v. Bond
  status: verified
  projected_at: 2026-07-06
---

# City of Tahlequah v. Bond

*595 U.S. 9 (2021)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers responded to a call that Dominic Rollice, intoxicated, would not leave his ex-wife's garage. As they spoke with him, Rollice grabbed a hammer and raised it as if to strike or throw it; two officers shot and killed him. His estate sued under § 1983 for excessive force. The Tenth Circuit denied [[Qualified Immunity|qualified immunity]], holding the officers' earlier "cornering" of Rollice was reckless and that circuit precedent clearly established the violation.

## Issue
Whether the officers were entitled to [[Qualified Immunity|qualified immunity]] because no precedent clearly established that their conduct violated the Fourth Amendment.

## Rule
Yes. Clearly established law must be defined with specificity: "We have repeatedly told courts not to define clearly established law at too high a level of generality." — *City of Tahlequah v. Bond*, 595 U.S. 9 (2021) (slip op., at 3). ^pin-op3

[[Qualified Immunity|Qualified immunity]] "protects '"all but the plainly incompetent or those who knowingly violate the law."'" — *Id.* (slip op., at 3) (quoting *District of Columbia v. Wesby*). ^pin-op3a

## Application
None of the decisions the Tenth Circuit invoked involved facts close enough to give these officers fair notice that confronting an armed, intoxicated man who raised a hammer would violate the Fourth Amendment. Because no precedent squarely governed the situation the officers faced, they did not violate clearly established law and were entitled to [[Qualified Immunity|qualified immunity]] on this record.

## Conclusion
The officers were entitled to [[Qualified Immunity|qualified immunity]]; the Tenth Circuit's contrary judgment was reversed. The Court did not decide whether a constitutional violation occurred.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Tahlequah* reaffirms the particularized "clearly established law" standard of [[District of Columbia v. Wesby]] and the objective qualified-immunity framework of [[Harlow v. Fitzgerald]], cautioning against the high-generality approach the "obvious case" exception of [[Hope v. Pelzer]] permits only rarely.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *City of Tahlequah v. Bond*, 595 U.S. 9 (2021) (per curiam) — https://www.courtlistener.com/opinion/5290448/city-of-tahlequah-v-bond/ — pinpoint: slip op., at 3 (CL carries the slip opinion; cluster 5290448 → opinion 5118994).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "476736676c53b4db", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "595 U.S. 9 (2021)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "City of Tahlequah v. Bond", "year": "2021"}}
{"assertion_id": "0584d0d77a0b2e4b", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "City of Tahlequah v. Bond"}}
{"assertion_id": "edf5afc1266f6fec", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Courts must not define clearly established law at too high a level of generality; QI protects 'all but the plainly incompetent or those who knowingly violate the law.'", "title": "City of Tahlequah v. Bond"}}
{"assertion_id": "8ab43d8d03874eb9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2021-10-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "City of Tahlequah v. Bond", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "City of Tahlequah v. Bond", "varies_by_point": "false"}}
{"assertion_id": "cae9067d137a0f01", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "City of Tahlequah v. Bond"}}
```

### lake record — City of Tahlequah v. Bond

```json
{
  "schema_version": "s2.v1",
  "record_id": "City of Tahlequah v. Bond",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "City of Tahlequah v. Bond",
    "case_name_short": "Bond",
    "case_name_full": "",
    "input_case_name": "City of Tahlequah v. Bond",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2021-10-18",
    "year": 2021,
    "docket": "20-1668",
    "cluster_id": 5292018,
    "lead_opinion_id": 5120580,
    "sibling_ids": [
      5120580
    ],
    "absolute_url": "/opinion/5292018/city-of-tahlequah-v-bond/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 5290448,
        "score": 120,
        "case_name": "City of Tahlequah v. Bond"
      },
      {
        "cluster_id": 5292017,
        "score": 20,
        "case_name": "City of Tahlequah v. Bond"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "595 U.S. 9",
      "volume": "595",
      "reporter": "U.S.",
      "page": "9",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "595 U.S. 9",
        "volume": "595",
        "reporter": "U.S.",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "595 U.S. 9",
    "official_selection": {
      "court_class": "scotus",
      "selected": "595 U.S. 9",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op3",
      "page": null,
      "quote": "of Rollice was reckless and that circuit precedent clearly established the violation. ## Issue Whether the officers were entitled to qualified immunity because no precedent clearly established that their conduct violated the Fourth Amendment. ## Rule Yes. Clearly established law must be defined with specificity:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op3a",
      "page": null,
      "quote": "all but the plainly incompetent or those who knowingly violate the law.",
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
    "composite_basis_ref": "City of Tahlequah v. Bond",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(5120580) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
        "query": "cites:(5120580)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(5120580)",
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
    "complete_query": "cites:(5120580)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 5120580,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/city-of-tahlequah-v-bond.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 5120580,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 169897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 744141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 4638478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9430379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9434715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9820073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 5120580,
        "cited_id": 9888205,
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
    "date_created": "2026-07-05T00:29:11Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:30:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:29:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — City of Tahlequah v. Bond

```
                 Cite as: 595 U. S. ____ (2021)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
CITY OF TAHLEQUAH, OKLAHOMA, ET AL. v. AUSTIN
 P. BOND, AS SPECIAL ADMINISTRATOR OF THE ESTATE OF
          DOMINIC F. ROLLICE, DECEASED
   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED
    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT
             No. 20–1668. Decided October 18, 2021

   PER CURIAM.
   On August 12, 2016, Dominic Rollice’s ex-wife, Joy, called
911. Rollice was in her garage, she explained, and he was
intoxicated and would not leave. Joy requested police as-
sistance; otherwise, “it’s going to get ugly real quick.” 981
F. 3d 808, 812 (CA10 2020). The dispatcher asked whether
Rollice lived at the residence. Joy said he did not but ex-
plained that he kept tools in her garage.
   Officers Josh Girdner, Chase Reed, and Brandon Vick re-
sponded to the call. All three knew that Rollice was Joy’s
ex-husband, was intoxicated, and would not leave her
home.
   Joy met the officers out front and led them to the side
entrance of the garage. There the officers encountered Rol-
lice and began speaking with him in the doorway. Rollice
expressed concern that the officers intended to take him to
jail; Officer Girdner told him that they were simply trying
to get him a ride. Rollice began fidgeting with something
in his hands and the officers noticed that he appeared nerv-
ous. Officer Girdner asked if he could pat Rollice down for
weapons. Rollice refused.
   Police body-camera video captured what happened next.
As the conversation continued, Officer Girdner gestured
with his hands and took one step toward the doorway, caus-
ing Rollice to take one step back. Rollice, still conversing
with the officers, turned around and walked toward the
back of the garage where his tools were hanging over a
2               CITY OF TAHLEQUAH v. BOND

                          Per Curiam

workbench. Officer Girdner followed, the others close be-
hind. No officer was within six feet of Rollice. The video is
silent, but the officers stated that they ordered Rollice to
stop. Rollice kept walking. He then grabbed a hammer
from the back wall over the workbench and turned around
to face the officers. Rollice grasped the handle of the ham-
mer with both hands, as if preparing to swing a baseball
bat, and pulled it up to shoulder level. The officers backed
up, drawing their guns. At this point the video is no longer
silent, and the officers can be heard yelling at Rollice to
drop the hammer.
   He did not. Instead, Rollice took a few steps to his right,
coming out from behind a piece of furniture so that he had
an unobstructed path to Officer Girdner. He then raised
the hammer higher back behind his head and took a stance
as if he was about to throw the hammer or charge at the
officers. In response, Officers Girdner and Vick fired their
weapons, killing Rollice.
   Rollice’s estate filed suit against, among others, Officers
Girdner and Vick, alleging that the officers were liable un-
der 42 U. S. C. §1983, for violating Rollice’s Fourth Amend-
ment right to be free from excessive force. The officers
moved for summary judgment, both on the merits and on
qualified immunity grounds. The District Court granted
their motion. Burke v. Tahlequah, 2019 WL 4674316, *6
(ED Okla., Sept. 25, 2019). The officers’ use of force was
reasonable, it concluded, and even if not, qualified immun-
ity prevented the case from going further. Ibid.
   A panel of the Court of Appeals for the Tenth Circuit re-
versed. 981 F. 3d, at 826. The Court began by explaining
that Tenth Circuit precedent allows an officer to be held li-
able for a shooting that is itself objectively reasonable if the
officer’s reckless or deliberate conduct created a situation
requiring deadly force. Id., at 816. Applying that rule, the
Court concluded that a jury could find that Officer Girdner’s
                  Cite as: 595 U. S. ____ (2021)              3

                           Per Curiam

initial step toward Rollice and the officers’ subsequent “cor-
nering” of him in the back of the garage recklessly created
the situation that led to the fatal shooting, such that their
ultimate use of deadly force was unconstitutional. Id., at
823. As to qualified immunity, the Court concluded that
several cases, most notably Allen v. Muskogee, 119 F. 3d 837
(CA10 1997), clearly established that the officers’ conduct
was unlawful. 981 F. 3d, at 826. This petition followed.
   We need not, and do not, decide whether the officers vio-
lated the Fourth Amendment in the first place, or whether
recklessly creating a situation that requires deadly force
can itself violate the Fourth Amendment. On this record,
the officers plainly did not violate any clearly established
law.
   The doctrine of qualified immunity shields officers from
civil liability so long as their conduct “does not violate
clearly established statutory or constitutional rights of
which a reasonable person would have known.” Pearson v.
Callahan, 555 U. S. 223, 231 (2009). As we have explained,
qualified immunity protects “ ‘all but the plainly incompe-
tent or those who knowingly violate the law.’ ” District of
Columbia v. Wesby, 583 U. S. ___, ___ –___ (2018) (slip op.,
at 13–14) (quoting Malley v. Briggs, 475 U. S. 335, 341
(1986)).
   We have repeatedly told courts not to define clearly es-
tablished law at too high a level of generality. See, e.g.,
Ashcroft v. al-Kidd, 563 U. S. 731, 742 (2011). It is not
enough that a rule be suggested by then-existing precedent;
the “rule’s contours must be so well defined that it is ‘clear
to a reasonable officer that his conduct was unlawful in the
situation he confronted.’ ” Wesby, 583 U. S., at ___ (slip op.,
at 14) (quoting Saucier v. Katz, 533 U. S. 194, 202 (2001)).
Such specificity is “especially important in the Fourth
Amendment context,” where it is “sometimes difficult for an
officer to determine how the relevant legal doctrine, here
excessive force, will apply to the factual situation the officer
4               CITY OF TAHLEQUAH v. BOND

                         Per Curiam

confronts.” Mullenix v. Luna, 577 U. S. 7, 12 (2015) (per
curiam) (internal quotation marks omitted).
   The Tenth Circuit contravened those settled principles
here. Not one of the decisions relied upon by the Court of
Appeals—Estate of Ceballos v. Husk, 919 F. 3d 1204 (CA10
2019), Hastings v. Barnes, 252 Fed. Appx. 197 (CA10 2007),
Allen, 119 F. 3d 837, and Sevier v. Lawrence, 60 F. 3d 695
(CA10 1995)—comes close to establishing that the officers’
conduct was unlawful. The Court relied most heavily on
Allen. But the facts of Allen are dramatically different from
the facts here. The officers in Allen responded to a potential
suicide call by sprinting toward a parked car, screaming at
the suspect, and attempting to physically wrest a gun from
his hands. 119 F. 3d, at 841. Officers Girdner and Vick, by
contrast, engaged in a conversation with Rollice, followed
him into a garage at a distance of 6 to 10 feet, and did not
yell until after he picked up a hammer. We cannot conclude
that Allen “clearly established” that their conduct was reck-
less or that their ultimate use of force was unlawful.
   The other decisions relied upon by the Court of Appeals
are even less relevant. As for Sevier, that decision merely
noted in dicta that deliberate or reckless preseizure conduct
can render a later use of force excessive before dismissing
the appeal for lack of jurisdiction. See 60 F. 3d, at 700–701.
To state the obvious, a decision where the court did not even
have jurisdiction cannot clearly establish substantive con-
stitutional law. Regardless, that formulation of the rule is
much too general to bear on whether the officers’ particular
conduct here violated the Fourth Amendment. See al-Kidd,
563 U. S., at 742. Estate of Ceballos, decided after the
shooting at issue, is of no use in the clearly established in-
quiry. See Brosseau v. Haugen, 543 U. S. 194, 200, n. 4
(2004) (per curiam). And Hastings, an unpublished deci-
sion, involved officers initiating an encounter with a poten-
tially suicidal individual by chasing him into his bedroom,
screaming at him, and pepper-spraying him. 252 Fed.
                  Cite as: 595 U. S. ____ (2021)              5

                           Per Curiam

Appx., at 206. Suffice it to say, a reasonable officer could
miss the connection between that case and this one.
   Neither the panel majority nor the respondent has iden-
tified a single precedent finding a Fourth Amendment vio-
lation under similar circumstances. The officers were thus
entitled to qualified immunity.
   The petition for certiorari and the motions for leave to file
briefs amici curiae are granted, and the judgment of the
Court of Appeals is reversed.
                                              It is so ordered.

```

---

## GROUP: content/cases/Collins v. Virginia.md  (`case`, 5 assertions)

### content_page

```
---
title: "Collins v. Virginia"
type: case
citation: "584 U.S. 586 (2018)"
parallel_cite: "138 S. Ct. 1663; 201 L. Ed. 2d 9"
neutral_cite: 2018 U.S. LEXIS 3210
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2018
date_decided: 2018-05-29
docket: 16-1027
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2018-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Collins v. Virginia
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4501697/collins-v-virginia/"
  cluster_id: 4501697
  opinion_id: 4278950
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carroll v. United States]]", "[[California v. Carney]]", "[[Florida v. Jardines]]", "[[Coolidge v. New Hampshire]]"]
aliases: []
tags: ["case", "fourth-amendment", "automobile-exception", "curtilage", "home", "warrantless-search"]
holding: "The automobile exception does NOT authorize a warrantless entry of a home or its curtilage to search a vehicle parked there. The…"
lake:
  record_id: Collins v. Virginia
  status: verified
  projected_at: 2026-07-06
---

# Collins v. Virginia

*584 U.S. 586 (2018)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An officer investigating a distinctive orange-and-black motorcycle suspected of eluding police walked up the driveway of Collins's house to a parking patio partly enclosed by the home, pulled back a tarp covering the motorcycle, ran the plates, and confirmed it was stolen — all without a warrant. Collins moved to suppress, and the Virginia Supreme Court upheld the search under the automobile exception.

## Issue
Whether the automobile exception permits an officer, without a warrant, to enter the [[Curtilage|curtilage]] of a home to search a vehicle parked there.

## Rule
No. "For the foregoing reasons, we conclude that the automobile exception does not permit an officer without a warrant to enter a home or its curtilage in order to search a vehicle therein." — *Collins v. Virginia*, 584 U.S. 586 (2018) (slip op., at 14). ^pin-op14

The automobile exception is a warrant exception for the vehicle; it does not independently justify the separate trespass of entering constitutionally protected [[Curtilage|curtilage]] to reach the vehicle.

## Application
The motorcycle was parked on the [[Curtilage|curtilage]] — a partly enclosed section of the driveway adjacent to and intimately tied to the home. The officer physically entered that [[Curtilage|curtilage]] and pulled off the tarp to search the motorcycle without a warrant. Because the automobile exception did not authorize entering the [[Curtilage|curtilage]], the warrantless intrusion was unlawful on these facts; whether it might be justified on another ground, such as [[Exigent Circumstances and Hot Pursuit|exigency]], was left for remand.

## Conclusion
The automobile exception did not authorize the warrantless [[Curtilage|curtilage]] entry; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Collins* bounds the [[Carroll v. United States]] / [[California v. Carney]] automobile exception at the home's [[Curtilage|curtilage]], applying the [[Curtilage|curtilage]] protection recognized in [[Florida v. Jardines]].

## Appears on
- [[Automobile Exception]] — *Key — Progeny / Refinement*

## Sources
- *Collins v. Virginia*, 584 U.S. 586 (2018) — https://www.courtlistener.com/opinion/4501697/collins-v-virginia/ — pinpoint: slip op., at 14 (CL carries the slip opinion; cluster 4501697 → opinion 4278950).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cd947a15834095d7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "584 U.S. 586 (2018)", "court": "U.S. Supreme Court", "neutral_cite": "2018 U.S. LEXIS 3210", "official_citation_present": true, "parallel_cite": "138 S. Ct. 1663; 201 L. Ed. 2d 9", "title": "Collins v. Virginia", "year": "2018"}}
{"assertion_id": "0c4f97e1622cb66f", "dimension": "support", "kind": "home_role", "locator": {"home": "Automobile Exception"}, "payload": {"home": "Automobile Exception", "role": "Key — Progeny / Refinement", "title": "Collins v. Virginia"}}
{"assertion_id": "332f716f119c0068", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The automobile exception does NOT authorize a warrantless entry of a home or its curtilage to search a vehicle parked there. The…", "title": "Collins v. Virginia"}}
{"assertion_id": "0c0b22d77d518ac6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2018-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Collins v. Virginia", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Collins v. Virginia", "varies_by_point": "false"}}
{"assertion_id": "16b907761da6aaec", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Collins v. Virginia"}}
```

### lake record — Collins v. Virginia

```json
{
  "schema_version": "s2.v1",
  "record_id": "Collins v. Virginia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Collins v. Virginia",
    "case_name_short": "Collins",
    "case_name_full": "",
    "input_case_name": "Collins v. Virginia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2018-05-29",
    "year": 2018,
    "docket": "16-1027",
    "cluster_id": 4501697,
    "lead_opinion_id": 4278950,
    "sibling_ids": [
      4278950
    ],
    "absolute_url": "/opinion/4501697/collins-v-virginia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "584 U.S. 586",
      "volume": "584",
      "reporter": "U.S.",
      "page": "586",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "138 S. Ct. 1663",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 9",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2018 U.S. LEXIS 3210",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3210",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "584 U.S. 586",
        "volume": "584",
        "reporter": "U.S.",
        "page": "586",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "138 S. Ct. 1663",
        "volume": "138",
        "reporter": "S. Ct.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "201 L. Ed. 2d 9",
        "volume": "201",
        "reporter": "L. Ed. 2d",
        "page": "9",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2018 U.S. LEXIS 3210",
        "volume": "2018",
        "reporter": "U.S. LEXIS",
        "page": "3210",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "584 U.S. 586",
    "official_selection": {
      "court_class": "scotus",
      "selected": "584 U.S. 586",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op14",
      "page": null,
      "quote": "--- # Collins v. Virginia *584 U.S. 586 (2018)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An officer investigating a distinctive orange-and-black motorcycle suspected of eluding police walked up the driveway of Collins's house to a parking patio partly enclosed by the home, pulled back a tarp covering the motorcycle, ran the plates, and confirmed it was stolen \u2014 all without a warrant. Collins moved to suppress, and the Virginia Supreme Court upheld the search under the automobile exception. ## Issue Whether the automobile exception permits an officer, without a warrant, to enter the curtilage of a home to search a vehicle parked there. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2018-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Collins v. Virginia",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "LaCour v. Marshalls of California",
          "cluster_id": 10765564,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wittey",
          "cluster_id": 9404034,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Chesney",
          "cluster_id": 4536724,
          "cite": [
            "196 A.3d 253"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Garza v. Idaho",
          "cluster_id": 4594419,
          "cite": [
            "586 U.S. 232",
            "139 S. Ct. 738",
            "203 L. Ed. 2d 77",
            "2019 U.S. LEXIS 1596"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Caldwell",
          "cluster_id": 4904976,
          "cite": [
            "7 F.4th 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pacheco v. State",
          "cluster_id": 10048657,
          "cite": [
            "465 Md. 311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Alexis",
          "cluster_id": 4573870,
          "cite": [
            "112 N.E.3d 796",
            "481 Mass. 91"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soukaneh v. Andrzejewski",
          "cluster_id": 10038252,
          "cite": [
            "112 F.4th 107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 9385343,
          "cite": [
            "62 F.4th 733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raheim Trice",
          "cluster_id": 4769607,
          "cite": [
            "966 F.3d 506"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander v. City of Syracuse",
          "cluster_id": 10356512,
          "cite": [
            "132 F.4th 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Suggs",
          "cluster_id": 4888422,
          "cite": [
            "998 F.3d 1125"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. State",
          "cluster_id": 10020965,
          "cite": [
            "233 A.3d 86",
            "470 Md. 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Long",
          "cluster_id": 4775413,
          "cite": [
            "157 N.E.3d 362",
            "2020 Ohio 4090"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Maxim",
          "cluster_id": 4683972,
          "cite": [
            "454 P.3d 543",
            "165 Idaho 901"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Noli",
          "cluster_id": 9399584,
          "cite": [
            "412 Mont. 170",
            "529 P.3d 813",
            "2023 MT 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 7852694,
          "cite": [
            "43 F.4th 94"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 4869243,
          "cite": [
            "2021 IL App (1st) 180509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lamar Clancy",
          "cluster_id": 4805551,
          "cite": [
            "979 F.3d 1135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Toddrey Willie Bruce",
          "cluster_id": 4794438,
          "cite": [
            "977 F.3d 1112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hernandez-Mieses",
          "cluster_id": 4644586,
          "cite": [
            "931 F.3d 134"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dylan Ostrum",
          "cluster_id": 9496998,
          "cite": [
            "99 F.4th 999"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 8439952,
          "cite": [
            "893 F.3d 66"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Prentiss Jackson",
          "cluster_id": 9510705,
          "cite": [
            "103 F.4th 483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 9500300,
          "cite": [
            "243 N.E.3d 782",
            "2024 Ohio 1763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Simpkins",
          "cluster_id": 4796830,
          "cite": [
            "978 F.3d 1"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Collins v. Virginia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4278950) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 3,
        "triage_snippet_classified": 108
      },
      "lane2_top_cited": {
        "query": "cites:(4278950)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9Nzg2MjEzMiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284278950%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4278950)",
        "reviewed": 48,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 48,
        "triage_read": 1,
        "triage_snippet_classified": 47
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4278950)",
    "indexed_citing_opinions": 142,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4278950,
        "count": 142,
        "count_source": "search"
      }
    ],
    "citation_count": 349,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/collins-v-virginia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MzU0MyZzPTEwMDM4MjUyJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%284278950%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4278950,
        "cited_id": 85412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 87010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 103794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 105511,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 106775,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 111833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145902,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 145922,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 218926,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 354014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 622304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 1501475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 2089408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 2621047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4278950,
        "cited_id": 3580565,
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
    "date_created": "2026-07-05T00:30:26Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:34:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:30:36Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Collins v. Virginia

```
(Slip Opinion)              OCTOBER TERM, 2017                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                          COLLINS v. VIRGINIA

        CERTIORARI TO THE SUPREME COURT OF VIRGINIA

     No. 16–1027. Argued January 9, 2018—Decided May 29, 2018
During the investigation of two traffic incidents involving an orange
 and black motorcycle with an extended frame, Officer David Rhodes
 learned that the motorcycle likely was stolen and in the possession of
 petitioner Ryan Collins. Officer Rhodes discovered photographs on
 Collins’ Facebook profile of an orange and black motorcycle parked in
 the driveway of a house, drove to the house, and parked on the street.
 From there, he could see what appeared to be the motorcycle under a
 white tarp parked in the same location as the motorcycle in the pho-
 tograph. Without a search warrant, Office Rhodes walked to the top
 of the driveway, removed the tarp, confirmed that the motorcycle was
 stolen by running the license plate and vehicle identification num-
 bers, took a photograph of the uncovered motorcycle, replaced the
 tarp, and returned to his car to wait for Collins. When Collins re-
 turned, Officer Rhodes arrested him. The trial court denied Collins’
 motion to suppress the evidence on the ground that Officer Rhodes
 violated the Fourth Amendment when he trespassed on the house’s
 curtilage to conduct a search, and Collins was convicted of receiving
 stolen property. The Virginia Court of Appeals affirmed. The State
 Supreme Court also affirmed, holding that the warrantless search
 was justified under the Fourth Amendment’s automobile exception.
Held: The automobile exception does not permit the warrantless entry
 of a home or its curtilage in order to search a vehicle therein. Pp. 3–
 14.
    (a) This case arises at the intersection of two components of the
 Court’s Fourth Amendment jurisprudence: the automobile exception
 to the warrant requirement and the protection extended to the curti-
 lage of a home. In announcing each of the automobile exception’s jus-
 tifications—i.e., the “ready mobility of the automobile” and “the per-
 vasive regulation of vehicles capable of traveling on the public
2                          COLLINS v. VIRGINIA

                                   Syllabus

    highways,” California v. Carney, 471 U. S. 386, 390, 392—the Court
    emphasized that the rationales applied only to automobiles and not
    to houses, and therefore supported their different treatment as a con-
    stitutional matter. When these justifications are present, officers
    may search an automobile without a warrant so long as they have
    probable cause. Curtilage—“the area ‘immediately surrounding and
    associated with the home’ ”—is considered “ ‘part of the home itself for
    Fourth Amendment purposes.’ ” Florida v. Jardines, 569 U. S. 1, 6.
    Thus, when an officer physically intrudes on the curtilage to gather
    evidence, a Fourth Amendment search has occurred and is presump-
    tively unreasonable absent a warrant. Pp. 3–6.
        (b) As an initial matter, the part of the driveway where Collins’ mo-
    torcycle was parked and subsequently searched is curtilage. When
    Officer Rhodes searched the motorcycle, it was parked inside a par-
    tially enclosed top portion of the driveway that abuts the house. Just
    like the front porch, side garden, or area “outside the front window,”
    that enclosure constitutes “an area adjacent to the home and ‘to
    which the activity of home life extends.’ ” Jardines, 569 U. S., at 6, 7.
        Because the scope of the automobile exception extends no further
    than the automobile itself, it did not justify Officer Rhodes’ invasion
    of the curtilage. Nothing in this Court’s case law suggests that the
    automobile exception gives an officer the right to enter a home or its
    curtilage to access a vehicle without a warrant. Such an expansion
    would both undervalue the core Fourth Amendment protection af-
    forded to the home and its curtilage and “ ‘untether’ ” the exception
    “ ‘from the justifications underlying’ ” it. Riley v. California, 573 U. S.
    ___, ___. This Court has similarly declined to expand the scope of
    other exceptions to the warrant requirement. Thus, just as an officer
    must have a lawful right of access to any contraband he discovers in
    plain view in order to seize it without a warrant—see Horton v. Cali-
    fornia, 496 U. S. 128, 136–137—and just as an officer must have a
    lawful right of access in order to arrest a person in his home—see
    Payton v. New York, 445 U. S. 573, 587–590—so, too, an officer must
    have a lawful right of access to a vehicle in order to search it pursu-
    ant to the automobile exception. To allow otherwise would unmoor
    the exception from its justifications, render hollow the core Fourth
    Amendment protection the Constitution extends to the house and its
    curtilage, and transform what was meant to be an exception into a
    tool with far broader application. Pp. 6–11.
        (c) Contrary to Virginia’s claim, the automobile exception is not a
    categorical one that permits the warrantless search of a vehicle any-
    time, anywhere, including in a home or curtilage. Scher v. United
    States, 305 U. S. 251; Pennsylvania v. Labron, 518 U. S. 938, distin-
    guished. Also unpersuasive is Virginia’s proposed bright line rule for
                      Cite as: 584 U. S. ____ (2018)                       3

                                 Syllabus

  an automobile exception that would not permit warrantless entry
  only of the house itself or another fixed structure, e.g., a garage, inside
  the curtilage. This Court has long been clear that curtilage is afford-
  ed constitutional protection, and creating a carveout for certain types
  of curtilage seems more likely to create confusion than does uniform
  application of the Court’s doctrine. Virginia’s rule also rests on a
  mistaken premise, for the ability to observe inside curtilage from a
  lawful vantage point is not the same as the right to enter curtilage
  without a warrant to search for information not otherwise accessible.
  Finally, Virginia’s rule automatically would grant constitutional
  rights to those persons with the financial means to afford residences
  with garages but deprive those persons without such resources of any
  individualized consideration as to whether the areas in which they
  store their vehicles qualify as curtilage. Pp. 11–14.
292 Va. 486, 790 S. E. 2d 611, reversed and remanded.

  SOTOMAYOR, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, GINSBURG, BREYER, KAGAN, and GORSUCH,
JJ., joined. THOMAS, J., filed a concurring opinion. ALITO, J., filed a
dissenting opinion.
                        Cite as: 584 U. S. ____ (2018)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 16–1027
                                   _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                                 [May 29, 2018] 


  JUSTICE SOTOMAYOR delivered the opinion of the Court.
  This case presents the question whether the automobile
exception to the Fourth Amendment permits a police
officer, uninvited and without a warrant, to enter the
curtilage of a home in order to search a vehicle parked
therein. It does not.
                             I
   Officer Matthew McCall of the Albemarle County Police
Department in Virginia saw the driver of an orange and
black motorcycle with an extended frame commit a traffic
infraction. The driver eluded Officer McCall’s attempt to
stop the motorcycle. A few weeks later, Officer David
Rhodes of the same department saw an orange and black
motorcycle traveling well over the speed limit, but the
driver got away from him, too. The officers compared
notes and concluded that the two incidents involved the
same motorcyclist.
   Upon further investigation, the officers learned that the
motorcycle likely was stolen and in the possession of peti-
tioner Ryan Collins. After discovering photographs on
Collins’ Facebook profile that featured an orange and
black motorcycle parked at the top of the driveway of a
2                    COLLINS v. VIRGINIA

                      Opinion of the Court

house, Officer Rhodes tracked down the address of the
house, drove there, and parked on the street. It was later
established that Collins’ girlfriend lived in the house and
that Collins stayed there a few nights per week.1
  From his parked position on the street, Officer Rhodes
saw what appeared to be a motorcycle with an extended
frame covered with a white tarp, parked at the same angle
and in the same location on the driveway as in the Face-
book photograph. Officer Rhodes, who did not have a
warrant, exited his car and walked toward the house. He
stopped to take a photograph of the covered motorcycle
from the sidewalk, and then walked onto the residential
property and up to the top of the driveway to where the
motorcycle was parked. In order “to investigate further,”
App. 80, Officer Rhodes pulled off the tarp, revealing a
motorcycle that looked like the one from the speeding
incident. He then ran a search of the license plate and
vehicle identification numbers, which confirmed that the
motorcycle was stolen. After gathering this information,
Officer Rhodes took a photograph of the uncovered motor-
cycle, put the tarp back on, left the property, and returned
to his car to wait for Collins.
  Shortly thereafter, Collins returned home.          Officer
Rhodes walked up to the front door of the house and
knocked. Collins answered, agreed to speak with Officer
Rhodes, and admitted that the motorcycle was his and
that he had bought it without title. Officer Rhodes then
arrested Collins.
  Collins was indicted by a Virginia grand jury for receiv-
ing stolen property. He filed a pretrial motion to suppress
the evidence that Officer Rhodes had obtained as a result
of the warrantless search of the motorcycle. Collins ar-
gued that Officer Rhodes had trespassed on the curtilage
——————
  1 Virginia does not dispute that Collins has Fourth Amendment

standing. See Minnesota v. Olson, 495 U. S. 91, 96–100 (1990).
                  Cite as: 584 U. S. ____ (2018)             3

                      Opinion of the Court

of the house to conduct an investigation in violation of the
Fourth Amendment. The trial court denied the motion
and Collins was convicted.
   The Court of Appeals of Virginia affirmed. It assumed
that the motorcycle was parked in the curtilage of the
home and held that Officer Rhodes had probable cause to
believe that the motorcycle under the tarp was the same
motorcycle that had evaded him in the past. It further
concluded that Officer Rhodes’ actions were lawful under
the Fourth Amendment even absent a warrant because
“numerous exigencies justified both his entry onto the
property and his moving the tarp to view the motorcycle
and record its identification number.” 65 Va. App. 37, 46,
773 S. E. 2d 618, 623 (2015).
   The Supreme Court of Virginia affirmed on different
reasoning. It explained that the case was most properly
resolved with reference to the Fourth Amendment’s auto-
mobile exception. 292 Va. 486, 496–501, 790 S. E. 2d 611,
616–618 (2016). Under that framework, it held that
Officer Rhodes had probable cause to believe that the
motorcycle was contraband, and that the warrantless
search therefore was justified. Id., at 498–499, 790 S. E. 2d,
at 617.
   We granted certiorari, 582 U. S. ___ (2017), and now
reverse.
                               II
  The Fourth Amendment provides in relevant part that
the “right of the people to be secure in their persons, houses,
papers, and effects, against unreasonable searches and
seizures, shall not be violated.” This case arises at the
intersection of two components of the Court’s Fourth
Amendment jurisprudence: the automobile exception to
the warrant requirement and the protection extended to
the curtilage of a home.
4                   COLLINS v. VIRGINIA

                      Opinion of the Court

                              A
                              1
   The Court has held that the search of an automobile can
be reasonable without a warrant. The Court first articu-
lated the so-called automobile exception in Carroll v.
United States, 267 U. S. 132 (1925). In that case, law
enforcement officers had probable cause to believe that a
car they observed traveling on the road contained illegal
liquor. They stopped and searched the car, discovered and
seized the illegal liquor, and arrested the occupants. Id.,
at 134–136. The Court upheld the warrantless search and
seizure, explaining that a “necessary difference” exists
between searching “a store, dwelling house or other struc-
ture” and searching “a ship, motor boat, wagon or automo-
bile” because a “vehicle can be quickly moved out of the
locality or jurisdiction in which the warrant must be
sought.” Id., at 153.
   The “ready mobility” of vehicles served as the core justi-
fication for the automobile exception for many years.
California v. Carney, 471 U. S. 386, 390 (1985) (citing, e.g.,
Cooper v. California, 386 U. S. 58, 59 (1967); Chambers v.
Maroney, 399 U. S. 42, 51–52 (1970)). Later cases then
introduced an additional rationale based on “the pervasive
regulation of vehicles capable of traveling on the public
highways.” Carney, 471 U. S., at 392. As the Court ex-
plained in South Dakota v. Opperman, 428 U. S. 364
(1976):
    “Automobiles, unlike homes, are subjected to perva-
    sive and continuing governmental regulation and con-
    trols, including periodic inspection and licensing re-
    quirements. As an everyday occurrence, police stop
    and examine vehicles when license plates or inspec-
    tion stickers have expired, or if other violations, such
    as exhaust fumes or excessive noise, are noted, or if
    headlights or other safety equipment are not in proper
                  Cite as: 584 U. S. ____ (2018)            5

                      Opinion of the Court

    working order.” Id., at 368.
  In announcing each of these two justifications, the Court
took care to emphasize that the rationales applied only to
automobiles and not to houses, and therefore supported
“treating automobiles differently from houses” as a consti-
tutional matter. Cady v. Dombrowski, 413 U. S. 433, 441
(1973).
  When these justifications for the automobile exception
“come into play,” officers may search an automobile with-
out having obtained a warrant so long as they have proba-
ble cause to do so. Carney, 471 U. S., at 392–393.
                               2
   Like the automobile exception, the Fourth Amendment’s
protection of curtilage has long been black letter law.
“[W]hen it comes to the Fourth Amendment, the home is
first among equals.” Florida v. Jardines, 569 U. S. 1, 6
(2013). “At the Amendment’s ‘very core’ stands ‘the right
of a man to retreat into his own home and there be free
from unreasonable governmental intrusion.’ ” Ibid. (quot-
ing Silverman v. United States, 365 U. S. 505, 511 (1961)).
To give full practical effect to that right, the Court consid-
ers curtilage—“the area ‘immediately surrounding and
associated with the home’ ”—to be “ ‘part of the home itself
for Fourth Amendment purposes.’ ” Jardines, 569 U. S., at
6 (quoting Oliver v. United States, 466 U. S. 170, 180
(1984)). “The protection afforded the curtilage is essentially
a protection of families and personal privacy in an area
intimately linked to the home, both physically and psycho-
logically, where privacy expectations are most height-
ened.” California v. Ciraolo, 476 U. S. 207, 212–213
(1986).
   When a law enforcement officer physically intrudes on
the curtilage to gather evidence, a search within the mean-
ing of the Fourth Amendment has occurred. Jardines, 569
U. S., at 11. Such conduct thus is presumptively unrea-
6                    COLLINS v. VIRGINIA

                      Opinion of the Court

sonable absent a warrant.
                              B
                              1
   With this background in mind, we turn to the applica-
tion of these doctrines in the instant case. As an initial
matter, we decide whether the part of the driveway where
Collins’ motorcycle was parked and subsequently searched
is curtilage.
   According to photographs in the record, the driveway
runs alongside the front lawn and up a few yards past the
front perimeter of the house. The top portion of the
driveway that sits behind the front perimeter of the house
is enclosed on two sides by a brick wall about the height of
a car and on a third side by the house. A side door pro-
vides direct access between this partially enclosed section
of the driveway and the house. A visitor endeavoring to
reach the front door of the house would have to walk
partway up the driveway, but would turn off before enter-
ing the enclosure and instead proceed up a set of steps
leading to the front porch. When Officer Rhodes searched
the motorcycle, it was parked inside this partially enclosed
top portion of the driveway that abuts the house.
   The “ ‘conception defining the curtilage’ is . . . familiar
enough that it is ‘easily understood from our daily experi-
ence.’ ” Jardines, 569 U. S., at 7 (quoting Oliver, 466 U. S.,
at 182, n. 12). Just like the front porch, side garden, or
area “outside the front window,” Jardines, 569 U. S., at 6,
the driveway enclosure where Officer Rhodes searched the
motorcycle constitutes “an area adjacent to the home and
‘to which the activity of home life extends,’ ” and so is
properly considered curtilage, id., at 7 (quoting Oliver, 466
U. S., at 182, n. 12).
                              2
    In physically intruding on the curtilage of Collins’ home
                    Cite as: 584 U. S. ____ (2018)                  7

                        Opinion of the Court

to search the motorcycle, Officer Rhodes not only invaded
Collins’ Fourth Amendment interest in the item searched,
i.e., the motorcycle, but also invaded Collins’ Fourth
Amendment interest in the curtilage of his home. The
question before the Court is whether the automobile ex-
ception justifies the invasion of the curtilage.2 The answer
is no.
   Applying the relevant legal principles to a slightly dif-
ferent factual scenario confirms that this is an easy case.
Imagine a motorcycle parked inside the living room of a
house, visible through a window to a passerby on the
street. Imagine further that an officer has probable cause
to believe that the motorcycle was involved in a traffic
infraction. Can the officer, acting without a warrant,
enter the house to search the motorcycle and confirm
whether it is the right one? Surely not.
   The reason is that the scope of the automobile exception
extends no further than the automobile itself. See, e.g.,
Pennsylvania v. Labron, 518 U. S. 938, 940 (1996) (per
curiam) (explaining that the automobile exception “per-
mits police to search the vehicle”); Wyoming v. Houghton,
526 U. S. 295, 300 (1999) (“[T]he Framers would have
regarded as reasonable (if there was probable cause) the
warrantless search of containers within an automobile”).
Virginia asks the Court to expand the scope of the auto-
mobile exception to permit police to invade any space
outside an automobile even if the Fourth Amendment
protects that space. Nothing in our case law, however,
suggests that the automobile exception gives an officer the
right to enter a home or its curtilage to access a vehicle
——————
  2 Helpfully, the parties have simplified matters somewhat by each

making a concession. Petitioner concedes “for purposes of this appeal”
that Officer Rhodes had probable cause to believe that the motorcycle
was the one that had eluded him, Brief for Petitioner 5, n. 3, and
Virginia concedes that “Officer Rhodes searched the motorcycle,” Brief
for Respondent 12.
8                    COLLINS v. VIRGINIA

                      Opinion of the Court

without a warrant. Expanding the scope of the automobile
exception in this way would both undervalue the core
Fourth Amendment protection afforded to the home and
its curtilage and “ ‘untether’ ” the automobile exception
“ ‘from the justifications underlying’ ” it. Riley v. Califor-
nia, 573 U. S. ___, ___ (2014) (slip op., at 10) (quoting
Arizona v. Gant, 556 U. S. 332, 343 (2009)).
    The Court already has declined to expand the scope of
other exceptions to the warrant requirement to permit
warrantless entry into the home. The reasoning behind
those decisions applies equally well in this context. For
instance, under the plain-view doctrine, “any valid war-
rantless seizure of incriminating evidence” requires that
the officer “have a lawful right of access to the object
itself.” Horton v. California, 496 U. S. 128, 136–137
(1990); see also id., at 137, n. 7 (“ ‘[E]ven where the object
is contraband, this Court has repeatedly stated and en-
forced the basic rule that the police may not enter and
make a warrantless seizure’ ”); G. M. Leasing Corp. v.
United States, 429 U. S. 338, 354 (1977) (“It is one thing to
seize without a warrant property resting in an open area
. . . , and it is quite another thing to effect a warrantless
seizure of property . . . situated on private premises to
which access is not otherwise available for the seizing
officer”). A plain-view seizure thus cannot be justified if it
is effectuated “by unlawful trespass.” Soldal v. Cook
County, 506 U. S. 56, 66 (1992). Had Officer Rhodes seen
illegal drugs through the window of Collins’ house, for
example, assuming no other warrant exception applied, he
could not have entered the house to seize them without
first obtaining a warrant.
    Similarly, it is a “settled rule that warrantless arrests in
public places are valid,” but, absent another exception
such as exigent circumstances, officers may not enter a
home to make an arrest without a warrant, even when
they have probable cause. Payton v. New York, 445 U. S.
                 Cite as: 584 U. S. ____ (2018)            9

                     Opinion of the Court

573, 587–590 (1980). That is because being “ ‘arrested in
the home involves not only the invasion attendant to all
arrests but also an invasion of the sanctity of the home.’ ”
Id., at 588–589 (quoting United States v. Reed, 572 F. 2d
412, 423 (CA2 1978)). Likewise, searching a vehicle
parked in the curtilage involves not only the invasion of
the Fourth Amendment interest in the vehicle but also an
invasion of the sanctity of the curtilage.
   Just as an officer must have a lawful right of access to
any contraband he discovers in plain view in order to seize
it without a warrant, and just as an officer must have a
lawful right of access in order to arrest a person in his
home, so, too, an officer must have a lawful right of access
to a vehicle in order to search it pursuant to the automo-
bile exception. The automobile exception does not afford
the necessary lawful right of access to search a vehicle
parked within a home or its curtilage because it does not
justify an intrusion on a person’s separate and substantial
Fourth Amendment interest in his home and curtilage.
   As noted, the rationales underlying the automobile
exception are specific to the nature of a vehicle and the
ways in which it is distinct from a house. See Part II–A–1,
supra. The rationales thus take account only of the bal-
ance between the intrusion on an individual’s Fourth
Amendment interest in his vehicle and the governmental
interests in an expedient search of that vehicle; they do
not account for the distinct privacy interest in one’s home
or curtilage. To allow an officer to rely on the automobile
exception to gain entry into a house or its curtilage for the
purpose of conducting a vehicle search would unmoor the
exception from its justifications, render hollow the core
Fourth Amendment protection the Constitution extends to
the house and its curtilage, and transform what was
meant to be an exception into a tool with far broader
application. Indeed, its name alone should make all this
10                       COLLINS v. VIRGINIA

                          Opinion of the Court

clear enough: It is, after all, an exception for automobiles.3
——————
  3 The dissent concedes that “the degree of the intrusion on privacy” is

relevant in determining whether a warrant is required to search a
motor vehicle “located on private property.” Post, at 5–6 (opinion of
ALITO, J.). Yet it puzzlingly asserts that the “privacy interests at stake”
here are no greater than when a motor vehicle is searched “on public
streets.” Post, at 3–4. “An ordinary person of common sense,” post,
at 2, however, clearly would understand that the privacy interests at
stake in one’s private residential property are far greater than on a
public street. Contrary to the dissent’s suggestion, it is of no signifi-
cance that the motorcycle was parked just a “short walk up the drive-
way.” Ibid. The driveway was private, not public, property, and the
motorcycle was parked in the portion of the driveway beyond where a
neighbor would venture, in an area “intimately linked to the home, . . .
where privacy expectations are most heightened.” California v. Ciraolo,
476 U. S. 207, 213 (1986). Nor does it matter that Officer Rhodes
“did not damage any property,” post, at 2, for an officer’s care in con-
ducting a search does not change the character of the place being
searched. And, as we explain, see infra, at 13–14, it is not dispositive
that Officer Rhodes did not “observe anything along the way” to the
motorcycle “that he could not have seen from the street,” post, at 2.
Law enforcement officers need not “shield their eyes when passing by a
home on public thoroughfares,” Ciraolo, 476 U. S., at 213, but the
ability visually to observe an area protected by the Fourth Amendment
does not give officers the green light physically to intrude on it. See
Florida v. Jardines, 569 U. S. 1, 7–8 (2013). It certainly does not
permit an officer physically to intrude on curtilage, remove a tarp to
reveal license plate and vehicle identification numbers, and use those
numbers to confirm that the defendant committed a crime.
  The dissent also mistakenly relies on a law enacted by the First
Congress and mentioned in Carroll v. United States, 267 U. S. 132,
150–151 (1925), that authorized the warrantless search of vessels.
Post, at 4–5, n. 3. The dissent thinks it implicit in that statute that
“officers could cross private property such as wharves in order to reach
and board those vessels.” Ibid. Even if it were so that a police officer
could have entered a private wharf to search a vessel, that would not
prove he could enter the curtilage of a home to do so. To the contrary,
whereas the statute relied upon in Carroll authorized warrantless
searches of vessels, it expressly required warrants to search houses.
See 267 U. S., at 150–157; Act of July 31, 1789, §24, 1 Stat. 43. Here,
Officer Rhodes did not invade a private wharf to undertake a search; he
invaded the curtilage of a home.
                 Cite as: 584 U. S. ____ (2018)           11

                     Opinion of the Court

  Given the centrality of the Fourth Amendment interest
in the home and its curtilage and the disconnect between
that interest and the justifications behind the automobile
exception, we decline Virginia’s invitation to extend the
automobile exception to permit a warrantless intrusion on
a home or its curtilage.
                             III

                              A

  Virginia argues that this Court’s precedent indicates
that the automobile exception is a categorical one that
permits the warrantless search of a vehicle anytime,
anywhere, including in a home or curtilage. Specifically,
Virginia points to two decisions that it contends resolve
this case in its favor. Neither is dispositive or persuasive.
  First, Virginia invokes Scher v. United States, 305 U. S.
251 (1938). In that case, federal officers received a confi-
dential tip that a particular car would be transporting
bootleg liquor at a specified time and place. The officers
identified and followed the car until the driver “turned
into a garage a few feet back of his residence and within
the curtilage.” Id., at 253. As the driver exited his car, an
officer approached and stated that he had been informed
that the car was carrying contraband.              The driver
acknowledged that there was liquor in the trunk, and the
officer proceeded to open the trunk, find the liquor, arrest
the driver, and seize both the car and the liquor. Id., at
253–254. Although the officer did not have a search war-
rant, the Court upheld the officer’s actions as reasonable.
Id., at 255.
  Scher is inapposite. Whereas Collins’ motorcycle was
parked and unattended when Officer Rhodes intruded on
the curtilage to search it, the officers in Scher first en-
countered the vehicle when it was being driven on public
streets, approached the curtilage of the home only when
the driver turned into the garage, and searched the vehicle
12                  COLLINS v. VIRGINIA

                     Opinion of the Court

only after the driver admitted that it contained contra-
band. Scher by no means established a general rule that
the automobile exception permits officers to enter a home
or its curtilage absent a warrant. The Court’s brief analy-
sis referenced Carroll, but only in the context of observing
that, consistent with that case, the “officers properly could
have stopped” and searched the car “just before [petitioner]
entered the garage,” a proposition the petitioner did
“not seriously controvert.” Scher, 305 U. S., at 254–255.
The Court then explained that the officers did not lose
their ability to stop and search the car when it entered
“the open garage closely followed by the observing officer”
because “[n]o search was made of the garage.” Id., at 255.
It emphasized that “[e]xamination of the automobile ac-
companied an arrest, without objection and upon admis-
sion of probable guilt,” and cited two search-incident-to-
arrest cases. Ibid. (citing Agnello v. United States, 269
U. S. 20, 30 (1925); Wisniewski v. United States, 47 F. 2d
825, 826 (CA6 1931)). Scher’s reasoning thus was both
case specific and imprecise, sounding in multiple doc-
trines, particularly, and perhaps most appropriately, hot
pursuit. The decision is best regarded as a factbound one,
and it certainly does not control this case.
   Second, Virginia points to Labron, 518 U. S. 938, where
the Court upheld under the automobile exception the
warrantless search of an individual’s pickup truck that
was parked in the driveway of his father-in-law’s farm-
house. Id., at 939–940; Commonwealth v. Kilgore, 544 Pa.
439, 444, 677 A. 2d 311, 313 (1995). But Labron provides
scant support for Virginia’s position. Unlike in this case,
there was no indication that the individual who owned the
truck in Labron had any Fourth Amendment interest in
the farmhouse or its driveway, nor was there a determina-
tion that the driveway was curtilage.
                 Cite as: 584 U. S. ____ (2018)          13

                     Opinion of the Court

                              B
   Alternatively, Virginia urges the Court to adopt a more
limited rule regarding the intersection of the automobile
exception and the protection afforded to curtilage. Virginia
would prefer that the Court draw a bright line and hold
that the automobile exception does not permit warrantless
entry into “the physical threshold of a house or a similar
fixed, enclosed structure inside the curtilage like a gar-
age.” Brief for Respondent 46. Requiring officers to make
“case-by-case curtilage determinations,” Virginia reasons,
unnecessarily complicates matters and “raises the poten-
tial for confusion and . . . error.” Id., at 46–47 (internal
quotation marks omitted).
   The Court, though, has long been clear that curtilage is
afforded constitutional protection. See Oliver, 466 U. S.,
at 180. As a result, officers regularly assess whether an
area is curtilage before executing a search. Virginia pro-
vides no reason to conclude that this practice has proved
to be unadministrable, either generally or in this context.
Moreover, creating a carveout to the general rule that
curtilage receives Fourth Amendment protection, such
that certain types of curtilage would receive Fourth
Amendment protection only for some purposes but not for
others, seems far more likely to create confusion than does
uniform application of the Court’s doctrine.
   In addition, Virginia’s proposed rule rests on a mistaken
premise about the constitutional significance of visibility.
The ability to observe inside curtilage from a lawful van-
tage point is not the same as the right to enter curtilage
without a warrant for the purpose of conducting a search
to obtain information not otherwise accessible. Cf. Cir-
aolo, 476 U. S., at 213–214 (holding that “physically non-
intrusive” warrantless aerial observation of the curtilage
of a home did not violate the Fourth Amendment, and
could form the basis for probable cause to support a war-
rant to search the curtilage). So long as it is curtilage, a
14                   COLLINS v. VIRGINIA

                      Opinion of the Court

parking patio or carport into which an officer can see from
the street is no less entitled to protection from trespass
and a warrantless search than a fully enclosed garage.
  Finally, Virginia’s proposed bright-line rule automati-
cally would grant constitutional rights to those persons
with the financial means to afford residences with garages
in which to store their vehicles but deprive those persons
without such resources of any individualized consideration
as to whether the areas in which they store their vehicles
qualify as curtilage. See United States v. Ross, 456 U. S.
798, 822 (1982) (“[T]he most frail cottage in the kingdom is
absolutely entitled to the same guarantees of privacy as
the most majestic mansion”).
                             IV
   For the foregoing reasons, we conclude that the automo-
bile exception does not permit an officer without a warrant
to enter a home or its curtilage in order to search a vehicle
therein. We leave for resolution on remand whether Of-
ficer Rhodes’ warrantless intrusion on the curtilage of
Collins’ house may have been reasonable on a different
basis, such as the exigent circumstances exception to the
warrant requirement. The judgment of the Supreme
Court of Virginia is therefore reversed, and the case is
remanded for further proceedings not inconsistent with
this opinion.
                                              It is so ordered.
                 Cite as: 584 U. S. ____ (2018)           1

                    THOMAS, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 16–1027
                         _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                        [May 29, 2018] 


   JUSTICE THOMAS, concurring.
   I join the Court’s opinion because it correctly resolves
the Fourth Amendment question in this case. Notably,
the only reason that Collins asked us to review this ques-
tion is because, if he can prove a violation of the Fourth
Amendment, our precedents require the Virginia courts to
apply the exclusionary rule and potentially suppress the
incriminating evidence against him. I write separately
because I have serious doubts about this Court’s authority
to impose that rule on the States. The assumption that
state courts must apply the federal exclusionary rule is
legally dubious, and many jurists have complained that it
encourages “distort[ions]” in substantive Fourth Amend-
ment law, Rakas v. Illinois, 439 U. S. 128, 157 (1978)
(White, J., dissenting); see also Coolidge v. New Hamp-
shire, 403 U. S. 443, 490 (1971) (Harlan, J., concurring);
Calabresi, The Exclusionary Rule, 26 Harv. J. L. & Pub.
Pol’y 111, 112 (2003).
   The Fourth Amendment, as relevant here, protects the
people from “unreasonable searches” of “their . . . houses.”
As a general rule, warrantless searches of the curtilage
violate this command. At the founding, curtilage was
considered part of the “hous[e]” itself. See 4 W. Black-
stone, Commentaries on the Laws of England 225
(1769) (“[T]he capital house protects and privileges all its
branches and appurtenants, if within the curtilage”). And
2                       COLLINS v. VIRGINIA

                        THOMAS, J., concurring

except in circumstances not present here, house searches
required a specific warrant. See W. Cuddihy, The Fourth
Amendment: Origins and Original Meaning 602–1791,
p. 743 (2009) (Cuddihy); Donahue, The Original Fourth
Amendment, 83 U. Chi. L. Rev. 1181, 1237–1240 (2016);
Davies, Recovering the Original Fourth Amendment, 98
Mich. L. Rev. 547, 643–646 (1999). A warrant was re-
quired even if the house was being searched for stolen
goods or contraband—objects that, unlike cars, are not
protected by the Fourth Amendment at all. Id., at 647–
650; see also Carroll v. United States, 267 U. S. 132, 150–
152 (1925) (Taft, C. J.) (discussing founding-era evidence
that a search warrant was required when stolen goods and
contraband were “concealed in a dwelling house” but not
when they were “in course of transportation and concealed
in a movable vessel”). Accordingly, the police acted “un-
reasonabl[y]” when they searched the curtilage of Collins’
house without a warrant.1
   While those who ratified the Fourth and Fourteenth
Amendments would agree that a constitutional violation
occurred here, they would be deeply confused about the
posture of this case and the remedy that Collins is seek-
ing. Historically, the only remedies for unconstitutional
searches and seizures were “tort suits” and “self-help.”
Utah v. Strieff, 579 U. S. ___, ___ (2016) (slip op., at 4).
The exclusionary rule—the practice of deterring illegal
searches and seizures by suppressing evidence at criminal
trials—did not exist. No such rule existed in “Roman Law,
Napoleonic Law or even the Common Law of England.”
Burger, Who Will Watch the Watchman? 14 Am. U.
L. Rev. 1 (1964). And this Court did not adopt the federal
——————
  1 Collins did not live at the house; he merely stayed there with his

girlfriend several times a week. But Virginia does not contest Collins’
assertion that the house is his, so I agree with the Court that Virginia
has forfeited any argument to the contrary. See ante, at 2, n. 1; United
States v. Jones, 565 U. S. 400, 404, n. 2 (2012).
                  Cite as: 584 U. S. ____ (2018)            3

                     THOMAS, J., concurring

exclusionary rule until the 20th century. See Weeks v.
United States, 232 U. S. 383 (1914). As late as 1949,
nearly two-thirds of the States did not have an exclusion-
ary rule. See Wolf v. Colorado, 338 U. S. 25, 29 (1949).
Those States, as then-Judge Cardozo famously explained,
did not understand the logic of a rule that allowed “[t]he
criminal . . . to go free because the constable has blun-
dered.” People v. Defore, 242 N. Y. 13, 21, 150 N. E. 585,
587 (1926).
   The Founders would not have understood the logic of
the exclusionary rule either. Historically, if evidence was
relevant and reliable, its admissibility did not “depend
upon the lawfulness or unlawfulness of the mode, by
which it [was] obtained.” United States v. The La Jeune
Eugenie, 26 F. Cas. 832, 843 (No. 15, 551) (CC Mass. 1822)
(Story, J.); accord, 1 S. Greenleaf, Evidence §254a,
pp. 825–826 (14th ed. 1883) (“[T]hat . . . subjects of evi-
dence may have been . . . unlawfully obtained . . . is no
valid objection to their admissibility if they are pertinent
to the issue”); 4 J. Wigmore, Evidence §2183, p. 626 (2d ed.
1923) (“[I]t has long been established that the admissibil-
ity of evidence is not affected by the illegality of the means
through which the party has been enabled to obtain the
evidence” (emphasis deleted)). And the common law some-
times reflected the inverse of the exclusionary rule: The
fact that someone turned out to be guilty could justify an
illegal seizure. See Gelston v. Hoyt, 3 Wheat. 246, 310
(1818) (Story, J.) (“At common law, any person may at his
peril, seize for a forfeiture to the government; and if the
government adopt his seizure, and the property is con-
demned, he will be completely justified”); 2 W. Hawkins,
Pleas of the Crown 77 (1721) (“And where a Man arrests
another, who is actually guilty of the Crime for which he is
arrested, . . . he needs not in justifying it, set forth any
special Cause of his Suspicion”).
   Despite this history, the Court concluded in Mapp v.
4                        COLLINS v. VIRGINIA

                         THOMAS, J., concurring

Ohio, 367 U. S. 643 (1961), that the States must apply the
federal exclusionary rule in their own courts. Id., at 655.2
Mapp suggested that the exclusionary rule was required
by the Constitution itself. See, e.g., id., at 657 (“[T]he
exclusionary rule is an essential part of both the Fourth
and Fourteenth Amendments”); id., at 655 (“[E]vidence
obtained by searches and seizures in violation of the Con-
stitution is, by that same authority, inadmissible in a
state court”); id., at 655–656 (“[I]t was . . . constitutionally
necessary that the exclusion doctrine—an essential part of
the right to privacy—be also insisted upon”).3 But that
suggestion could not withstand even the slightest scrutiny.
The exclusionary rule appears nowhere in the Constitu-
tion, postdates the founding by more than a century, and
contradicts several longstanding principles of the common
law. See supra, at 2–3; Cuddihy 759–760; Amar, Fourth
Amendment First Principles, 107 Harv. L. Rev. 757, 786
(1994); Kaplan, The Limits of the Exclusionary Rule, 26

——————
   2 Twelve years before Mapp, the Court declined to apply the federal

exclusionary rule to the States. See Wolf v. Colorado, 338 U. S. 25
(1949). Wolf denied that the Constitution requires the exclusionary
rule, since “most of the English-speaking world” does not apply that
rule and alternatives such as civil suits and internal police discipline do
not “fal[l] below the minimal standards assured by the Due Process
Clause.” Id., at 29, 31. In Mapp, the Court overruled Wolf and applied
the exclusionary rule to the States, even though no party had briefed or
argued that question. See 367 U. S., at 672–674, and nn. 4–6 (Harlan,
J., dissenting); Stewart, The Road to Mapp v. Ohio and Beyond: The
Origins, Development and Future of the Exclusionary Rule, 83 Colum.
L. Rev. 1365, 1368 (1983).
   3 Justice Black, the essential fifth vote in Mapp, did not agree that

the Fourth Amendment contains an exclusionary rule. See 367 U. S.,
at 661–662 (concurring opinion) (“[T]he Fourth Amendment does not
itself contain any provision expressly precluding the use of such evi-
dence, and I am extremely doubtful that such a provision could prop-
erly be inferred”). But he concluded that, when the police seize private
papers, suppression is required by a combination of the Fourth and
Fifth Amendments. See id., at 662–666.
                      Cite as: 584 U. S. ____ (2018)                       5

                          THOMAS, J., concurring

Stan. L. Rev. 1027, 1030–1031 (1974).
    Recognizing this, the Court has since rejected Mapp’s
“ ‘[e]xpansive dicta’ ” and clarified that the exclusionary
rule is not required by the Constitution. Davis v. United
States, 564 U. S. 229, 237 (2011) (quoting Hudson v. Mich-
igan, 547 U. S. 586, 591 (2006)). Suppression, this Court
has explained, is not “a personal constitutional right.”
United States v. Calandra, 414 U. S. 338, 348 (1974);
accord, Stone v. Powell, 428 U. S. 465, 486 (1976). The
Fourth Amendment “says nothing about suppressing
evidence,” Davis, supra, at 236, and a prosecutor’s “use of
fruits of a past unlawful search or seizure ‘work[s] no new
Fourth Amendment wrong,’ ” United States v. Leon, 468
U. S. 897, 906 (1984) (quoting Calandra, supra, at 354).4
Instead, the exclusionary rule is a “judicially created”
doctrine that is “prudential rather than constitutionally
mandated.” Pennsylvania Bd. of Probation and Parole v.
Scott, 524 U. S. 357, 363 (1998); accord, Herring v. United
States, 555 U. S. 135, 139 (2009); Arizona v. Evans, 514
U. S. 1, 10 (1995); United States v. Janis, 428 U. S. 433,
459–460 (1976).5
——————
   4 The exclusionary rule is not required by the Due Process Clause

either. Given its nonexistent historical foundation, the exclusionary
rule cannot be a “settled usag[e] and mod[e] of proceeding existing in
the common and statute law of England, before the emigration of our
ancestors.” Murray’s Lessee v. Hoboken Land & Improvement Co., 18
How. 272, 277 (1856). And the rule “has ‘no bearing on . . . the fairness
of the trial.’ ” Desist v. United States, 394 U. S. 244, 254, n. 24 (1969).
If anything, the exclusionary rule itself “ ‘offends basic concepts of the
criminal justice system’ ” and exacts a “ ‘costly toll upon truth-seeking.’ ”
Herring v. United States, 555 U. S. 135, 141 (2009). “The [excluded]
evidence is likely to be the most reliable that could possibly be obtained
[and thus] exclusion rather than admission creates the danger of a
verdict erroneous on the true facts.” H. Friendly, Benchmarks 260
(1967).
   5 These statements cannot be dismissed as mere dicta. Cf. Dickerson

v. United States, 530 U. S. 428, 438–441, and n. 2 (2000) (constitution-
alizing the rule announced in Miranda v. Arizona, 384 U. S. 436 (1966),
6                       COLLINS v. VIRGINIA

                        THOMAS, J., concurring

   Although the exclusionary rule is not part of the Consti-
tution, this Court has continued to describe it as “federal
law” and assume that it applies to the States. Evans,
supra; Massachusetts v. Sheppard, 468 U. S. 981, 991
(1984). Yet the Court has never attempted to justify this
assumption. If the exclusionary rule is federal law, but is
not grounded in the Constitution or a federal statute, then
it must be federal common law. See Monaghan, Foreword:
Constitutional Common Law, 89 Harv. L. Rev. 1, 10
(1975). As federal common law, however, the exclusionary
rule cannot bind the States.
   Federal law trumps state law only by virtue of the Su-
premacy Clause, which makes the “Constitution, and the
Laws of the United States which shall be made in Pursu-
ance thereof; and all Treaties . . . the supreme Law of the
Land,” Art. VI, cl. 2. When the Supremacy Clause refers
to “[t]he Laws of the United States made in Pursuance [of
the Constitution],” it means federal statutes, not federal
common law. Ramsey, The Supremacy Clause, Original
Meaning, and Modern Law, 74 Ohio St. L. J. 559, 572–599
(2013) (Ramsey); Clark, Separation of Powers as a Safe-
guard of Federalism, 79 Texas L. Rev. 1321, 1334–1336,
1338–1367 (2001) (Clark); see also Gibbons v. Ogden, 9
Wheat. 1, 211 (1824) (Marshall, C. J.) (“The appropriate
application of that part of the clause which confers . . .
supremacy on laws . . . is to . . . the laws of Congress, made
in pursuance of the constitution”); Hart, The Relations

——————
despite earlier precedents to the contrary). The nonconstitutional
status of the exclusionary rule is why this Court held in Stone v.
Powell, 428 U. S. 465, 482–495 (1976), that violations are not cogniza-
ble on federal habeas review. Cf. Dickerson, supra, at 439 n. 3. And
the nonconstitutional status of the rule is why this Court has created
more than a dozen exceptions to it, which apply even when the Fourth
Amendment is concededly violated. See United States v. Weaver, 808
F. 3d 26, 49 (CADC 2015) (Henderson, J., dissenting) (collecting cases);
cf. Dickerson, supra, at 441.
                 Cite as: 584 U. S. ____ (2018)            7

                    THOMAS, J., concurring

Between State and Federal Law, 54 Colum. L. Rev. 489,
500 (1954) (“[T]he supremacy clause is limited to those
‘Laws’ of the United States which are passed by Congress
pursuant to the Constitution”). By referencing laws “made
in Pursuance” of the Constitution, the Supremacy Clause
incorporates the requirements of Article I, which force
Congress to stay within its enumerated powers, §8, and
follow the cumbersome procedures for enacting federal
legislation, §7. See Wyeth v. Levine, 555 U. S. 555, 585–
587 (2009) (THOMAS, J., concurring in judgment); 3 J.
Story, Commentaries on the Constitution of the United
States §1831, pp. 693–694 (1833); Clark 1334. Those
procedures—especially the requirement that bills pass the
Senate, where the States are represented equally and
Senators were originally elected by state legislatures—
safeguard federalism by making federal legislation more
difficult to pass and more responsive to state interests.
See Ramsey 565; Clark 1342–1343. Federal common law
bypasses these procedures and would not have been con-
sidered the kind of “la[w]” that can bind the States under
the Supremacy Clause. See Ramsey 564–565, 568, 574,
581; Jay, Origins of Federal Common Law: Part Two, 133
U. Pa. L. Rev. 1231, 1275 (1985).
   True, this Court, without citing the Supremacy Clause,
has recognized several “enclaves of federal judge-made law
which bind the States.” Banco Nacional de Cuba v. Sab-
batino, 376 U. S. 398, 426 (1964); see, e.g., id., at 427–428
(foreign affairs); Hinderlider v. La Plata River & Cherry
Creek Ditch Co., 304 U. S. 92, 110 (1938) (disputes be-
tween States); Garrett v. Moore-McCormack Co., 317 U. S.
239, 245 (1942) (admiralty); Clearfield Trust Co. v. United
States, 318 U. S. 363, 366 (1943) (certain rights and obli-
gations of the United States); Textile Workers v. Lincoln
Mills of Ala., 353 U. S. 448, 456–457 (1957) (aspects of
federal labor law). To the extent these enclaves are dele-
gations of lawmaking authority from the Constitution or a
8                   COLLINS v. VIRGINIA

                    THOMAS, J., concurring

federal statute, they do not conflict with the original
meaning of the Supremacy Clause (though they might be
illegitimate for other reasons). See Ramsey 568–569;
Grano, Prophylactic Rules in Criminal Procedure: A Ques-
tion of Article III Legitimacy, 80 Nw. U. L. Rev. 100, 131–
132 (1985). To the extent these enclaves are not rooted in
the Constitution or a statute, their pre-emptive force is
questionable. But that is why this Court has “limited”
them to a “ ‘few’ ” “narrow areas” where “the authority and
duties of the United States as sovereign are intimately
involved” or where “the interstate or international nature
of the controversy makes it inappropriate for state law to
control.” Texas Industries, Inc. v. Radcliff Materials, Inc.,
451 U. S. 630, 640–641 (1981) (quoting Wheeldin v.
Wheeler, 373 U. S. 647, 651 (1963)). Outside these narrow
enclaves, the general rule is that “[t]here is no federal
general common law” and “[e]xcept in matters governed by
the Federal Constitution or by Acts of Congress, the law to
be applied in any case is the law of the State.” Erie R. Co.
v. Tompkins, 304 U. S. 64, 78 (1938).
   These precedents do not support requiring the States to
apply the exclusionary rule. As explained, the exclusion-
ary rule is not rooted in the Constitution or a federal
statute. This Court has repeatedly rejected the idea that
the rule is in the Fourth and Fourteenth Amendments,
expressly or implicitly. See Davis, 564 U. S., at 236; Leon,
468 U. S., at 905–906; cf. Ziglar v. Abbasi, 582 U. S. ___,
___ (2017) (slip op., at 11) (explaining that reading implied
remedies into the Constitution is “a ‘disfavored’ judicial
activity”). And the exclusionary rule does not implicate
any of the special enclaves of federal common law. It does
not govern the sovereign duties of the United States or
disputes of an interstate or international character. In-
stead, the rule governs the methods that state police
officers use to solve crime and the procedures that state
courts use at criminal trials—subjects that the Federal
                      Cite as: 584 U. S. ____ (2018)                       9

                          THOMAS, J., concurring

Government generally has no power to regulate. See
United States v. Morrison, 529 U. S. 598, 618 (2000) (ex-
plaining that “[t]he regulation” and “vindication” of intra-
state crime “has always been the province of the States”);
Smith v. Phillips, 455 U. S. 209, 221 (1982) (“Federal
courts hold no supervisory authority over state judicial
proceedings”). These are not areas where federal common
law can bind the States.6
                         *    *    *
  In sum, I am skeptical of this Court’s authority to im-
pose the exclusionary rule on the States. We have not yet
revisited that question in light of our modern precedents,
which reject Mapp’s essential premise that the exclusion-
ary rule is required by the Constitution. We should do so.




——————
  6 Of course, the States are free to adopt their own exclusionary rules

as a matter of state law. But nothing in the Federal Constitution
requires them to do so. Even assuming the Constitution requires
particular state-law remedies for federal constitutional violations, it
does not require the exclusionary rule. The “sole purpose” of the
exclusionary rule is “to deter future Fourth Amendment violations”; it
does not “ ‘redress’ ” or “ ‘repair’ ” past ones. Davis v. United States, 564
U. S. 229, 236–237 (2011). This Court has noted the lack of evidence
supporting its deterrent effect, see United States v. Janis, 428 U. S.
433, 450, n. 22 (1976), and this Court has recognized the effectiveness
of alternative deterrents such as state tort law, state criminal law,
internal police discipline, and suits under 42 U. S. C. §1983, see Hud-
son v. Michigan, 547 U. S. 586, 597–599 (2006).
                    Cite as: 584 U. S. ____ (2018)                   1

                         ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                             _________________

                             No. 16–1027
                             _________________


 RYAN AUSTIN COLLINS, PETITIONER v. VIRGINIA
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                       VIRGINIA

                            [May 29, 2018] 


   JUSTICE ALITO, dissenting.
   The Fourth Amendment prohibits “unreasonable”
searches. What the police did in this case was entirely
reasonable. The Court’s decision is not.
   On the day in question, Officer David Rhodes was stand-
ing at the curb of a house where petitioner, Ryan Austin
Collins, stayed a couple of nights a week with his girl-
friend. From his vantage point on the street, Rhodes saw
an object covered with a tarp in the driveway, just a car’s
length or two from the curb. It is undisputed that Rhodes
had probable cause to believe that the object under the
tarp was a motorcycle that had been involved a few
months earlier in a dangerous highway chase, eluding the
police at speeds in excess of 140 mph. See Tr. of Oral Arg.
22; App. to Pet. for Cert. 67. Rhodes also had probable
cause to believe that petitioner had been operating the
motorcycle1 and that a search of the motorcycle would
provide evidence that the motorcycle had been stolen.2
   If the motorcycle had been parked at the curb, instead of
in the driveway, it is undisputed that Rhodes could have
——————
  1 Petitioner had a photo on his Facebook profile of a motorcycle that

resembled the unusual motorcycle involved in the prior highway chase.
See ante, at 1–2 (majority opinion).
  2 Rhodes suspected the motorcycle was stolen based on a conversation

he had with the man who had sold the motorcycle to petitioner. See
App. 57–58.
2                  COLLINS v. VIRGINIA

                     ALITO, J., dissenting

searched it without obtaining a warrant. See Tr. of Oral
Arg. 9; Reply Brief 1. Nearly a century ago, this Court
held that officers with probable cause may search a motor
vehicle without obtaining a warrant. Carroll v. United
States, 267 U. S. 132, 153, 155–156 (1925). The principal
rationale for this so-called automobile or motor-vehicle
exception to the warrant requirement is the risk that the
vehicle will be moved during the time it takes to obtain a
warrant. Id., at 153; California v. Carney, 471 U. S. 386,
390–391 (1985). We have also observed that the owner of
an automobile has a diminished expectation of privacy in
its contents. Id., at 391–393.
   So why does the Court come to the conclusion that
Officer Rhodes needed a warrant in this case? Because, in
order to reach the motorcycle, he had to walk 30 feet or so
up the driveway of the house rented by petitioner’s girl-
friend, and by doing that, Rhodes invaded the home’s
“curtilage.” Ante, at 6–7. The Court does not dispute that
the motorcycle, when parked in the driveway, was just as
mobile as it would have been had it been parked at the
curb. Nor does the Court claim that Officer Rhodes’s short
walk up the driveway did petitioner or his girlfriend any
harm. Rhodes did not damage any property or observe
anything along the way that he could not have seen from
the street. But, the Court insists, Rhodes could not enter
the driveway without a warrant, and therefore his search
of the motorcycle was unreasonable and the evidence
obtained in that search must be suppressed.
   An ordinary person of common sense would react to the
Court’s decision the way Mr. Bumble famously responded
when told about a legal rule that did not comport with the
reality of everyday life. If that is the law, he exclaimed,
“the law is a ass—a idiot.” C. Dickens, Oliver Twist 277
(1867).
   The Fourth Amendment is neither an “ass” nor an “idiot.”
Its hallmark is reasonableness, and the Court’s strikingly
                  Cite as: 584 U. S. ____ (2018)            3

                      ALITO, J., dissenting

unreasonable decision is based on a misunderstanding of
Fourth Amendment basics.
   The Fourth Amendment protects “[t]he right of the
people to be secure in their persons, houses, papers, and
effects.” A “house,” for Fourth Amendment purposes, is
not limited to the structure in which a person lives, but by
the same token, it also does not include all the real property
surrounding a dwelling. See, e.g., Florida v. Jardines, 569
U. S. 1, 6 (2013); United States v. Dunn, 480 U. S. 294,
300–301 (1987). Instead, a person’s “house” encompasses
the dwelling and a circumscribed area of surrounding land
that is given the name “curtilage.” Oliver v. United States,
466 U. S. 170, 180 (1984). Land outside the curtilage is
called an “open field,” and a search conducted in that area
is not considered a search of a “house” and is therefore not
governed by the Fourth Amendment. Ibid. Ascertaining
the boundaries of the curtilage thus determines only
whether a search is governed by the Fourth Amendment.
The concept plays no other role in Fourth Amendment
analysis.
   In this case, there is no dispute that the search of the
motorcycle was governed by the Fourth Amendment, and
therefore whether or not it occurred within the curtilage is
not of any direct importance. The question before us is not
whether there was a Fourth Amendment search but
whether the search was reasonable. And the only possible
argument as to why it might not be reasonable concerns
the need for a warrant. For nearly a century, however, it
has been well established that officers do not need a war-
rant to search a motor vehicle on public streets so long as
they have probable cause. Carroll, supra, at 153, 156; see
also, e.g., Pennsylvania v. Labron, 518 U. S. 938, 940
(1996) (per curiam); Carney, supra, at 394; South Dakota
v. Opperman, 428 U. S. 364, 367–368 (1976); Chambers v.
Maroney, 399 U. S. 42, 50–51 (1970). Thus, the issue here
is whether there is any good reason why this same rule
4                      COLLINS v. VIRGINIA

                         ALITO, J., dissenting

should not apply when the vehicle is parked in plain view
in a driveway just a few feet from the street.
   In considering that question, we should ask whether the
reasons for the “automobile exception” are any less valid
in this new situation. Is the vehicle parked in the drive-
way any less mobile? Are any greater privacy interests at
stake? If the answer to those questions is “no,” then the
automobile exception should apply. And here, the answer
to each question is emphatically “no.” The tarp-covered
motorcycle parked in the driveway could have been uncov-
ered and ridden away in a matter of seconds. And Officer
Rhodes’s brief walk up the driveway impaired no real
privacy interests.
   In this case, the Court uses the curtilage concept in a way
that is contrary to our decisions regarding other, exigency-
based exceptions to the warrant requirement. Take, for
example, the “emergency aid” exception. See Brigham
City v. Stuart, 547 U. S. 398 (2006). When officers reason-
ably believe that a person inside a dwelling has urgent
need of assistance, they may cross the curtilage and enter
the building without first obtaining a warrant. Id., at
403–404. The same is true when officers reasonably be-
lieve that a person in a dwelling is destroying evidence.
See Kentucky v. King, 563 U. S. 452, 460 (2011). In both of
those situations, we ask whether “ ‘the exigencies of the
situation’ make the needs of law enforcement so compel-
ling that the warrantless search is objectively reasonable.”
Brigham City, supra, at 403 (quoting Mincey v. Arizona,
437 U. S. 385, 394 (1978)). We have not held that the need
to cross the curtilage independently necessitates a war-
rant, and there is no good reason to apply a different rule
here.3
——————
  3 Indeed, I believe that the First Congress implicitly made the same

judgment in enacting the statute on which Carroll v. United States, 267
U. S. 132 (1925), relied when the motor-vehicle exception was first
                     Cite as: 584 U. S. ____ (2018)                    5

                          ALITO, J., dissenting

   It is no answer to this argument that the emergency-aid
and destruction-of-evidence exceptions require an inquiry
into the practicality of obtaining a warrant in the particu-
lar circumstances of the case. Our precedents firmly
establish that the motor-vehicle exception, unlike these
other exceptions, “has no separate exigency requirement.”
Maryland v. Dyson, 527 U. S. 465, 466–467 (1999) (per
curiam). It is settled that the mobility of a motor vehicle
categorically obviates any need to engage in such a case-
specific inquiry. Requiring such an inquiry here would
mark a substantial alteration of settled Fourth Amend-
ment law.
   This does not mean, however, that a warrant is never
needed when officers have probable cause to search a
motor vehicle, no matter where the vehicle is located.
While a case-specific inquiry regarding exigency would be
inconsistent with the rationale of the motor-vehicle excep-
tion, a case-specific inquiry regarding the degree of intru-
sion on privacy is entirely appropriate when the motor
vehicle to be searched is located on private property. After
all, the ultimate inquiry under the Fourth Amendment is
——————
recognized. Since the First Congress sent the Bill of Rights to the
States for ratification, we have often looked to laws enacted by that
Congress as evidence of the original understanding of the meaning of
those Amendments. See, e.g., id., at 150–151; Town of Greece v. Gallo-
way, 572 U. S. ___, ___–___ (2014) (slip op., at 7–8); United States v.
Villamonte-Marquez, 462 U. S. 579, 585–586 (1983); United States v.
Ramsey, 431 U. S. 606, 616–617 (1977). Carroll itself noted that the
First Congress enacted a law authorizing officers to search vessels
without a warrant. 267 U. S., at 150–151. Although this statute did
not expressly state that these officers could cross private property such
as wharves in order to reach and board those vessels, I think that was
implicit. Otherwise, the statute would very often have been ineffective.
And when Congress later enacted similar laws, it made this authoriza-
tion express. See, e.g., An Act Further to Prevent Smuggling and for
Other Purposes, §5, 14 Stat. 179. For this reason, Officer Rhodes’s
conduct in this case is consistent with the original understanding of the
Fourth Amendment, as explicated in Carroll.
6                   COLLINS v. VIRGINIA

                     ALITO, J., dissenting

whether a search is reasonable, and that inquiry often
turns on the degree of the intrusion on privacy. Thus,
contrary to the opinion of the Court, an affirmance in this
case would not mean that officers could perform a war-
rantless search if a motorcycle were located inside a house.
See ante, at 7. In that situation, the intrusion on privacy
would be far greater than in the present case, where the
real effect, if any, is negligible.
  I would affirm the decision below and therefore respect-
fully dissent.

```

---

## GROUP: content/cases/Colonnade Catering Corp. v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Colonnade Catering Corp. v. United States
type: case
citation: "397 U.S. 72 (1970)"
parallel_cite: "90 S. Ct. 774; 25 L. Ed. 2d 60"
neutral_cite: 1970 U.S. LEXIS 66
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1970
date_decided: 1970-02-25
docket: 108
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
  opinion_url: "https://www.courtlistener.com/opinion/108077/colonnade-catering-corp-v-united-states/"
  cluster_id: 108077
  opinion_id: null
  identity_checked: true
lake:
  record_id: Colonnade Catering Corp. v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Foundational (closely-regulated-industry administrative search)"
related:
  - "[[United States v. Biswell]]"
  - "[[See v. City of Seattle]]"
  - "[[Camara v. Municipal Court]]"
  - "[[Donovan v. Dewey]]"
  - "[[New York v. Burger]]"
tags:
  - case
  - fourth-amendment
  - administrative-search
  - closely-regulated-industry
  - warrantless-inspection
  - special-needs
holding: "Because the liquor industry has long been subject to close federal supervision and inspection, Congress has broad authority to fashion warrantless inspection schemes for it; but where the governing statute punished a licensee's refusal to admit an inspector only with a fine and did not authorize forcible, warrantless entry, federal agents who broke the lock on a storeroom exceeded the statutory scheme, and the seized liquor had to be suppressed."
---

# Colonnade Catering Corp. v. United States

*397 U.S. 72 (1970)* (No. 108) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 108077 → 397 U.S. 72, No. 108, decided 1970-02-25 (Douglas, J.); Rule quotes string-matched to the CL opinion text 2026-07-07. -->

## Background
Colonnade, a New York catering business holding a federal retail liquor dealer's occupational tax stamp, was visited by federal agents who suspected that bottles were being refilled in violation of the excise laws. When the company president refused to unlock the liquor storeroom and asked for a warrant, an agent broke the lock, entered, and seized the liquor. Colonnade sued to recover and suppress it. The District Court ordered the liquor returned; the Second Circuit reversed.

## Issue
Whether federal agents, acting under liquor-inspection statutes that punish a dealer's refusal of entry with a fine, may forcibly enter a locked storeroom without a warrant to inspect a closely regulated liquor business.

## Rule
Writing for the Court, Justice Douglas held that the liquor industry's long regulatory pedigree gives Congress wide latitude to authorize inspections: "We agree that Congress has broad power to design such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand." — 397 U.S. at 76. ^pin-76

But that power must be exercised by statute: "Where Congress has authorized inspection but made no rules governing the procedure that inspectors must follow, the Fourth Amendment and its various restrictive rules apply." Dealing "here with the liquor industry long subject to close supervision and inspection," the Court found that "Congress selected a standard that does not include forcible entries without a warrant." — 397 U.S. at 77. ^pin-77

## Application
Because of the industry's history of close supervision, the general rule of *[[See v. City of Seattle|See]]* — that a warrant is required to compel an administrative entry on non-public commercial premises — did not automatically control. But the specific scheme Congress enacted resolved a refusal of entry by imposing a fine, not by authorizing a forcible, warrantless break-in. The agents who broke the storeroom lock therefore exceeded what Congress had authorized, and the seizure was unlawful.

## Conclusion
**Reversed.** Douglas, J., wrote for the Court; Burger, C.J. (joined by Black and Stewart, JJ.), dissented. The forcible warrantless entry was not authorized by the statutory inspection scheme.

## Treatment & subsequent history
**Good law — foundational.** *Colonnade*, together with *[[United States v. Biswell]]* (firearms dealers, 1972), is one of the two foundational closely-regulated-industry cases: it establishes that a long history of pervasive regulation can support a statutory warrantless-inspection regime. The doctrine matured through *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]* and *[[Donovan v. Dewey]]* and was organized into the three-part test of *[[New York v. Burger]]* (1987).

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 108077 + 397 U.S. 72); renders under the ⚪ banner until S9 promotion. *[[Marshall v. Barlow's Inc|Marshall v. Barlow's, Inc.]]* is not yet in the corpus and is named in plain text to avoid a dangling link.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Foundational (closely-regulated-industry administrative search)*

## Sources
- [*Colonnade Catering Corp. v. United States*, 397 U.S. 72 (1970)](https://www.courtlistener.com/opinion/108077/colonnade-catering-corp-v-united-states/) — pinpoints: 76 (congressional power to inspect the closely regulated liquor industry), 77 (statute authorized a fine, not forcible warrantless entry; Douglas, J.); quotes string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f228668097c061a3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "397 U.S. 72 (1970)", "court": "U.S. Supreme Court", "neutral_cite": "1970 U.S. LEXIS 66", "official_citation_present": true, "parallel_cite": "90 S. Ct. 774; 25 L. Ed. 2d 60", "title": "Colonnade Catering Corp. v. United States", "year": "1970"}}
{"assertion_id": "95b10f60f00fe01b", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Foundational (closely-regulated-industry administrative search)", "title": "Colonnade Catering Corp. v. United States"}}
{"assertion_id": "cfd99e0125a1962f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Because the liquor industry has long been subject to close federal supervision and inspection, Congress has broad authority to fashion warrantless inspection schemes for it; but where the governing statute punished a licensee's refusal to admit an inspector only with a fine and did not authorize forcible, warrantless entry, federal agents who broke the lock on a storeroom exceeded the statutory scheme, and the seized liquor had to be suppressed.", "title": "Colonnade Catering Corp. v. United States"}}
{"assertion_id": "806652781f4c64f7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Colonnade Catering Corp. v. United States"}}
{"assertion_id": "fdf38f93d1825bef", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Colonnade Catering Corp. v. United States", "varies_by_point": "false"}}
```

### lake record — Colonnade Catering Corp. v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colonnade Catering Corp. v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Colonnade Catering Corp. v. United States",
    "case_name_short": "",
    "case_name_full": "Colonnade Catering Corp. v. United States",
    "input_case_name": "Colonnade Catering Corp. v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1970-02-25",
    "year": 1970,
    "docket": "108",
    "cluster_id": 108077,
    "lead_opinion_id": 9424185,
    "sibling_ids": [],
    "absolute_url": "/opinion/108077/colonnade-catering-corp-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "397 U.S. 72",
      "volume": "397",
      "reporter": "U.S.",
      "page": "72",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "90 S. Ct. 774",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "774",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 60",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1970 U.S. LEXIS 66",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "397 U.S. 72",
        "volume": "397",
        "reporter": "U.S.",
        "page": "72",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "90 S. Ct. 774",
        "volume": "90",
        "reporter": "S. Ct.",
        "page": "774",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 L. Ed. 2d 60",
        "volume": "25",
        "reporter": "L. Ed. 2d",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1970 U.S. LEXIS 66",
        "volume": "1970",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "397 U.S. 72",
    "official_selection": {
      "court_class": "scotus",
      "selected": "397 U.S. 72",
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
    "date_created": "2026-07-08T00:41:06Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "W10 on-read identity re-verification 2026-07-07: docket 108 confirmed verbatim from CL lead-opinion caption (html_with_citations)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T00:41:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "colonnade-catering-corp-v-united-states--108077",
      "to_record_id": "Colonnade Catering Corp. v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Colonnade Catering Corp. v. United States

```
<opinion type="majority">
<author id="b170-11">Mr. Justice Douglas</author>
<p id="Ag">delivered the opinion of the Court.</p>
<p id="b170-12">Petitioner, a licensee in New York authorized to serve alcoholic beverages and also the holder.of a federal retail liquor dealer’s occupational tax stamp, <span class="citation no-link">26 U. S. C. § 5121</span> (a), brought this suit to obtain the return of seized liquor and to suppress it as evidence. The District Court granted the relief. The Court of Appeals reversed. <span class="citation" data-id="284599"><a href="/opinion/284599/petition-of-the-colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Petition of the Colonnade Catering Corp. v. United States">410 F. 2d 197</a></span>. The case is here on a petition for writ of certiorari which we granted, <span class="citation multiple-matches"><a href="/c/U.%20S./396/814/">396 U. S. 814</a></span>, to review the decision in light of <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, and <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>.</p>
<p id="b170-13">Petitioner runs a catering agent, a member of the Alcohol and Tobacco Tax Divi<page-number citation-index="1" label="73">*73</page-number>sion of the Internal Revenue Service, was a guest at a party on petitioner’s premises and noted a possible violation of the federal excise tax law. When federal agents later visited the place, another party was in progress. They noticed that liquor was being served. Without the manager’s consent, they inspected the cellar. Then they asked the manager to open the locked liquor storeroom. He said that the only person authorized to open that room was one Rozzo, petitioner’s president, who was not on the premises. Later Rozzo arrived and refused to open the storeroom. He asked if the agents had a search warrant and they answered that they did not need one. When Rozzo continued to refuse to unlock the room, an agent broke the lock and entered. Then they removed the bottles of liquor now in controversy which they apparently suspected of being refilled contrary to the command of <span class="citation no-link">26 U. S. C. § 5301</span> (c).</p>
<p id="b171-4">It is provided in <span class="citation no-link">26 U. S. C. § 5146</span> (b)<footnotemark>1</footnotemark> and in <span class="citation no-link">26 U. S. C. § 7606</span> <footnotemark>2</footnotemark> that the Secretary of the Treasury or <page-number citation-index="1" label="74">*74</page-number>delegate has broad authority to enter and inspect the premises of retail dealers in liquors.<footnotemark>3</footnotemark> And in case of the refusal of a dealer to permit the inspection, it is provided <span class="citation no-link">26 U. S. C. § 7342</span>:</p>
<blockquote id="b172-5">“Any owner of any building or place, or person having the agency or superintendence of the same, who refuses to admit any officer or employee of the Treasury Department acting under the authority of section 7606 (relating to entry of premises for examination of taxable articles) or refuses to permit him examine such article or articles, shall, for every such refusal, forfeit $500.”</blockquote>
<p id="b172-6">The question is whether the imposition of a fine for refusal to permit entry — with the attendant consequences that violation of inspection laws may have in this closely regulated industry — is under this statutory scheme the exclusive sanction, absent a warrant to break and enter.</p>
<p id="b172-7">In <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#366" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 366-367</a></span>, a case involving an inspection under a municipal code, we said:</p>
<blockquote id="b172-8">“[The] inspector has no power to force entry and did not attempt it. A fine is imposed for resistance, but officials are not authorized to break past the unwilling occupant.”</blockquote>
<p id="b172-9"><em>Frank </em>v. <em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/" aria-description="Citation for case: Frank v. Maryland">Maryland</a></span> </em>was overruled in Camara v. <em>Municipal <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Court, supra,</a></span> </em>insofar as it permitted warrantless searches or inspections under municipal fire, health, and housing codes. The dictum that the provision for a fine on refusal to allow inspection made the use of force improper when there was no warrant was not disturbed ; and the question is whether that dictum contains the controlling principle<footnotemark>4</footnotemark> for this cáse.</p>
<p id="b173-3"><page-number citation-index="1" label="75">*75</page-number>The Government, emphasizing that the Fourth Amendment bans only “unreasonable searches and seizures,” <footnotemark>5</footnotemark> relies heavily on the long history of the regulation of the liquor industry during pre-Fourth Amendment days, first in England and later in the American Colonies. It is pointed out, for example, that in 1660 the precursor of modern-day liquor legislation was enacted in England<footnotemark>6</footnotemark> which allowed commissioners to enter, on demand, brewing houses at all times for inspection. Massachusetts had a similar law in 1692.<footnotemark>7</footnotemark> And in 1791, the year in which the Fourth Amendment was ratified, Congress imposed an excise tax on imported distilled spirits and on liquor distilled here,<footnotemark>8</footnotemark> under which law federal officers had broad powers to inspect distilling premises and the premises of the importer<footnotemark>9</footnotemark> without a warrant. From these and later laws and regulations governing the liquor industry, it is argued that Congress has been most solicitous in protecting the revenue against various types of fraud and to that end has repeatedly granted federal agents power to make warrantless searches and seizures of articles under the liquor laws.</p>
<p id="b174-4"><page-number citation-index="1" label="76">*76</page-number>The Court recognized the special treatment spection laws of this kind in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 624:</p>
<blockquote id="b174-5">“[I]n the case of excisable or dutiable articles, the government has an interest in them for the payment of the duties thereon, and until such duties paid has a right to keep them under observation, to pursue and drag them from concealment.”</blockquote>
<p id="b174-6">it added:</p>
<blockquote id="b174-7">“The seizure of stolen goods common law; and the seizure of goods forfeited for breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past; and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as 'unreasonable,’ and they are not embraced within the prohibition of the amendment.” <span class="citation no-link"><em>Id., </em>at 623</span>.</blockquote>
<p id="b174-8">We agree that Congress has broad power to such powers of inspection under the liquor laws as it deems necessary to meet the evils at hand. The general rule laid down in <em>See </em>v. <em>City of <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">Seattle, supra,</a></span> </em>at 545— “that administrative entry, without consent, upon the portions of commercial premises which are not open to the public may only be compelled through prosecution or physical force within the framework of a warrant procedure” — is therefore not applicable here. In <em>See, </em><page-number citation-index="1" label="77">*77</page-number>we reserved decision on the problems of “licensing programs” requiring inspection, saying they can be resolved “on a case-by-case basis under the general Fourth Amendment standard of reasonableness.” <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#546" aria-description="Citation for case: See v. City of Seattle"><em>Id., </em>at 546</a></span>.</p>
<p id="b175-4">Where Congress has authorized inspection but made no rules governing the procedure that inspectors must follow, the Fourth Amendment and its various restrictive rules apply. We said in the <em>See </em>case:</p>
<blockquote id="b175-5">“The businessman, like the occupant of a residence, has a constitutional right to go about his business free from unreasonable official entries upon his private commercial property. The businessman, too, has that right placed in jeopardy if the decision to enter and inspect for violation of regulatory laws can be made and enforced by the inspector in the field without official authority evidenced by a warrant.” <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#543" aria-description="Citation for case: See v. City of Seattle"><em>Id., </em>at 543</a></span>.</blockquote>
<p id="b175-6">What was said in <em>See </em>reflects this Nation’s traditions that are strongly opposed to using force without definite authority to break down doors. We deal here with the liquor industry long subject to close supervision and inspection. As respects that industry, and its various branches including retailers, Congress has broad authority to fashion standards of reasonableness for searches and seizures. Under the existing statutes, Congress selected a standard that does not include forcible entries without a warrant. It resolved the issue, not by authorizing forcible, warrantless entries, but by making it an offense for a licensee to refuse admission to the inspector.</p>
<p id="b175-7">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b171-5"> <span class="citation no-link">26 U. S. C. § 5146</span> (b) provides:</p>
<p id="b171-6">or his delegate may enter during business hours premises (including places of storage) of any dealer for the purpose of inspecting or examining any records or other documents required to be kept by such dealer under this chapter or regulations issued pursuant thereto and any distilled spirits, wines, or beer or stored by such dealer on such premises.”</p>
</footnote>
<footnote label="2">
<p id="b171-7"> <span class="citation no-link">26 U. S. C. § 7606</span> provides:</p>
<p id="b171-8">“(a) Entry during day.</p>
<p id="b171-9">“The Secretary or his delegate may enter, in the daytime, any building or place where any articles or objects subject to tax are made, produced, or kept, so far as it may be necessary for the purpose of examining said articles or objects.</p>
<p id="b171-10">“(b) Entry at night.</p>
<p id="b171-11">are open Secretary or his delegate may enter them while so open, in the performance of his duties.”</p>
</footnote>
<footnote label="3">
<p id="b172-10"> As defined in <span class="citation no-link">26 U. S. C. § 5122</span> (a).</p>
</footnote>
<footnote label="4">
<p id="b172-11"> And see <em>United States </em>v. <em>Frisch, </em><span class="citation" data-id="6888050"><a href="/opinion/6989657/united-states-v-frisch/#662" aria-description="Citation for case: United States v. Frisch">140 F. 2d 660, 662</a></span>.</p>
</footnote>
<footnote label="5">
<p id="b173-4"> The Fourth Amendment reads as follows:</p>
<blockquote id="b173-5">“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall be violated, and no Warrants shall issue, but upon probable supported by Oath or affirmation, and particularly describing place to be searched, and the persons or things to be seized.”</blockquote>
</footnote>
<footnote label="6">
<p id="b173-6">. 23, § 19.</p>
</footnote>
<footnote label="7">
<p id="b173-7"> Act of June 24, 1692, Mass. Acts and Resolves, Vol. 1, 1692-p. 33, c. 5, § 8.</p>
</footnote>
<footnote label="8">
<p id="b173-8"> Act of March 3, 1791, <span class="citation no-link">1 Stat. 199</span>.</p>
</footnote>
<footnote label="9">
<p id="b173-9"> Section 29 of the Act of March 3, 1791, <span class="citation no-link">1 Stat. 206</span>, provided:</p>
<blockquote id="b173-10">officers of inspection of each survey at all times in the daytime, upon request, to enter into all every the houses, store-houses, ware-houses, buildings and which shall have been [registered] in manner aforesaid, and tasting, gauging or otherwise, to take an account of the quantity, and proofs of the said spirits therein contained; and also to samples thereof, paying for the same the usual price.”</blockquote>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Colorado v. Bertine.md  (`case`, 5 assertions)

### content_page

```
---
title: "Colorado v. Bertine"
type: case
citation: "479 U.S. 367 (1987)"
parallel_cite: "107 S. Ct. 738; 93 L. Ed. 2d 739; 55 U.S.L.W. 4105"
neutral_cite: 1987 U.S. LEXIS 286
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-01-14
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-01-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Colorado v. Bertine
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111788/colorado-v-bertine/"
  cluster_id: 111788
  opinion_id: 9430773
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Lafayette]]", "[[Florida v. Wells]]", "[[South Dakota v. Opperman]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory-search", "impoundment", "standardized-criteria", "closed-container"]
holding: "Inventory searches (including opening closed containers) are permissible where police discretion is exercised according to standardized…"
lake:
  record_id: Colorado v. Bertine
  status: verified
  projected_at: 2026-07-06
---

# Colorado v. Bertine

*479 U.S. 367 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After arresting Bertine for driving under the influence, and before a tow truck arrived, a Boulder officer inventoried his van pursuant to police procedures, opening a closed backpack and the containers inside it and finding drugs, cash, and paraphernalia. Bertine moved to suppress, arguing the warrantless inventory of closed containers was unconstitutional.

## Issue
Whether police may, as part of a routine inventory of an impounded vehicle conducted under standardized procedures, open closed containers without a warrant or probable cause.

## Rule
Yes, where standardized procedures govern and the inventory is not a pretext for investigation. "[R]easonable police regulations relating to inventory procedures administered in good faith satisfy the Fourth Amendment, even though courts might as a matter of hindsight be able to devise equally reasonable rules requiring a different procedure." — 479 U.S. 367, 374. ^pin-374

Police discretion is permissible if cabined: "Nothing in *Opperman* or *Lafayette* prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity." — *Id.* at 375. ^pin-375

## Application
The Boulder officer inventoried Bertine's van and its closed containers pursuant to departmental procedures, exercising the choice to impound according to standardized criteria, and there was no showing the inventory was a ruse to investigate crime. Because the inventory and the opening of the containers followed good-faith standardized procedures on these facts, the search was reasonable.

## Conclusion
The inventory search, including the closed containers, was constitutional; the Colorado Supreme Court's suppression was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Bertine* applies the inventory doctrine of [[South Dakota v. Opperman]] and [[Illinois v. Lafayette]]; [[Florida v. Wells]] later confirmed that standardized criteria must in fact govern the opening of containers, lest the inventory become a pretext for general rummaging.

## Appears on
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Colorado v. Bertine*, 479 U.S. 367 (1987) — https://www.courtlistener.com/opinion/111788/colorado-v-bertine/ — pinpoints: 374, 375.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0f03ed439f66e8f2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "479 U.S. 367 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 286", "official_citation_present": true, "parallel_cite": "107 S. Ct. 738; 93 L. Ed. 2d 739; 55 U.S.L.W. 4105", "title": "Colorado v. Bertine", "year": "1987"}}
{"assertion_id": "14b678398bda71b6", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Inventory searches (including opening closed containers) are permissible where police discretion is exercised according to standardized…", "title": "Colorado v. Bertine"}}
{"assertion_id": "49e9874e1f6ab520", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Key — Progeny / Refinement", "title": "Colorado v. Bertine"}}
{"assertion_id": "1a854419871b7c28", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-01-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Colorado v. Bertine", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Colorado v. Bertine", "varies_by_point": "false"}}
{"assertion_id": "ba19687b99475893", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Colorado v. Bertine"}}
```

### lake record — Colorado v. Bertine

```json
{
  "schema_version": "s2.v1",
  "record_id": "Colorado v. Bertine",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Colorado v. Bertine",
    "case_name_short": "Bertine",
    "case_name_full": "Colorado v. Bertine",
    "input_case_name": "Colorado v. Bertine",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-01-14",
    "year": 1987,
    "docket": null,
    "cluster_id": 111788,
    "lead_opinion_id": 9430773,
    "sibling_ids": [
      111788,
      9430773,
      9430774,
      9430775
    ],
    "absolute_url": "/opinion/111788/colorado-v-bertine/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "479 U.S. 367",
      "volume": "479",
      "reporter": "U.S.",
      "page": "367",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 738",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "738",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 739",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "739",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4105",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4105",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 286",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "286",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "479 U.S. 367",
        "volume": "479",
        "reporter": "U.S.",
        "page": "367",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 738",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "738",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 L. Ed. 2d 739",
        "volume": "93",
        "reporter": "L. Ed. 2d",
        "page": "739",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 286",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "286",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4105",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4105",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "479 U.S. 367",
    "official_selection": {
      "court_class": "scotus",
      "selected": "479 U.S. 367",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-374",
      "page": null,
      "quote": "--- # Colorado v. Bertine *479 U.S. 367 (1987)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After arresting Bertine for driving under the influence, and before a tow truck arrived, a Boulder officer inventoried his van pursuant to police procedures, opening a closed backpack and the containers inside it and finding drugs, cash, and paraphernalia. Bertine moved to suppress, arguing the warrantless inventory of closed containers was unconstitutional. ## Issue Whether police may, as part of a routine inventory of an impounded vehicle conducted under standardized procedures, open closed containers without a warrant or probable cause. ## Rule Yes, where standardized procedures govern and the inventory is not a pretext for investigation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-375",
      "page": null,
      "quote": "Nothing in *Opperman* or *Lafayette* prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-01-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Colorado v. Bertine",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Charles E. Blake v. State of Mississippi",
          "cluster_id": 4541114,
          "cite": [
            "256 So. 3d 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4486934,
          "cite": [
            "2018 CO 27",
            "415 P.3d 815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Otis Sams, Jr. v. State of Indiana",
          "cluster_id": 4369368,
          "cite": [
            "71 N.E.3d 372",
            "2017 WL 677723",
            "2017 Ind. App. LEXIS 70"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Anderson v. State of Indiana",
          "cluster_id": 4327181,
          "cite": [
            "64 N.E.3d 903",
            "2016 Ind. App. LEXIS 432",
            "2016 WL 7078344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4316369,
          "cite": [
            "2016 COA 150",
            "417 P.3d 868"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Weathers v. State of Indiana",
          "cluster_id": 4248521,
          "cite": [
            "61 N.E.3d 279",
            "2016 Ind. App. LEXIS 297",
            "2016 WL 4379346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Parks",
          "cluster_id": 4247757,
          "cite": [
            "2015 COA 158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeffrey Ray Cox v. State",
          "cluster_id": 4288224,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Skinner v. Railway Labor Executives' Assn.",
          "cluster_id": 112219,
          "cite": [
            "103 L. Ed. 2d 639",
            "109 S. Ct. 1402",
            "489 U.S. 602",
            "1989 U.S. LEXIS 1568",
            "4 I.E.R. Cas. (BNA) 224",
            "1989 CCH OSHD 28,476",
            "57 U.S.L.W. 4324",
            "13 OSHC (BNA) 2065",
            "130 L.R.R.M. (BNA) 2857",
            "49 Empl. Prac. Dec. (CCH) 38,791"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Birchfield v. N. Dakota. William Robert Bernard",
          "cluster_id": 3216497,
          "cite": [
            "579 U.S. 438",
            "195 L. Ed. 2d 560",
            "2016 U.S. LEXIS 4058",
            "136 S. Ct. 2160"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Indianapolis v. Edmond",
          "cluster_id": 118391,
          "cite": [
            "148 L. Ed. 2d 333",
            "121 S. Ct. 447",
            "531 U.S. 32",
            "2000 U.S. LEXIS 8084",
            "69 U.S.L.W. 4009",
            "14 Fla. L. Weekly Fed. S 9",
            "2000 Colo. J. C.A.R. 6401",
            "2000 Cal. Daily Op. Serv. 9549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Von Raab",
          "cluster_id": 112220,
          "cite": [
            "103 L. Ed. 2d 685",
            "109 S. Ct. 1384",
            "489 U.S. 656",
            "1989 U.S. LEXIS 6033",
            "1989 CCH OSHD 28,589",
            "4 I.E.R. Cas. (BNA) 246",
            "57 U.S.L.W. 4338",
            "49 Empl. Prac. Dec. (CCH) 38,792"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Wells",
          "cluster_id": 112412,
          "cite": [
            "109 L. Ed. 2d 1",
            "110 S. Ct. 1632",
            "495 U.S. 1",
            "1990 U.S. LEXIS 2035",
            "58 U.S.L.W. 4454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hendrickson",
          "cluster_id": 1135960,
          "cite": [
            "917 P.2d 563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
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
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Redd",
          "cluster_id": 2387024,
          "cite": [
            "48 Cal. 4th 691",
            "229 P.3d 101",
            "108 Cal. Rptr. 3d 192",
            "2010 Cal. LEXIS 3749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scottie Ray Hurst",
          "cluster_id": 770650,
          "cite": [
            "228 F.3d 751",
            "2000 U.S. App. LEXIS 23606",
            "2000 WL 1363206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Lynn Cummins, United States of America v. Timothy Akins, A/K/A Michael Mayfield",
          "cluster_id": 552404,
          "cite": [
            "920 F.2d 498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1302221,
          "cite": [
            "973 P.2d 52",
            "83 Cal. Rptr. 2d 275",
            "20 Cal. 4th 119"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rahman",
          "cluster_id": 7078717,
          "cite": [
            "189 F.3d 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald James Causey",
          "cluster_id": 498394,
          "cite": [
            "834 F.2d 1179",
            "1987 U.S. App. LEXIS 17041",
            "1987 WL 23392"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brenton-Farley",
          "cluster_id": 147727,
          "cite": [
            "607 F.3d 1294",
            "2010 U.S. App. LEXIS 11125",
            "2010 WL 2179617"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. George M. Khoury, Howard Kluver, David W. West, Louis H. Chippas",
          "cluster_id": 540141,
          "cite": [
            "901 F.2d 948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zapata",
          "cluster_id": 195255,
          "cite": [
            "18 F.3d 971",
            "1994 WL 86216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Colorado v. Bertine:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzg3MzI0ODAwMDAwJnM9MjY0NjU3NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTUmcz02MDA3NDEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
        "reviewed": 49,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 49,
        "triage_read": 0,
        "triage_snippet_classified": 49
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111788 OR 9430773 OR 9430774 OR 9430775)",
    "indexed_citing_opinions": 993,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111788,
        "count": 827,
        "count_source": "search"
      },
      {
        "opinion_id": 9430773,
        "count": 186,
        "count_source": "search"
      },
      {
        "opinion_id": 9430774,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430775,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1722,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/colorado-v-bertine.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NTM0ODYmcz05NTc2MDY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111788+OR+9430773+OR+9430774+OR+9430775%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111788,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 110976,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 364699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 432054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1211186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1284293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 1792609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111788,
        "cited_id": 2051832,
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
    "date_created": "2026-07-05T00:34:24Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T00:39:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T00:34:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Colorado v. Bertine

```
<opinion type="majority">
<author id="b522-13">Chief Justice Rehnquist</author>
<p id="AGe">delivered the opinion of the Court.</p>
<p id="b522-14">On February 10, 1984, a police officer in Boulder, Colorado, arrested respondent Steven Lee Bertine for driving while under the influence of alcohol. After Bertine was taken into custody and before the arrival of a tow truck to take Bertine’s van to an impoundment lot,<footnotemark>1</footnotemark> a backup officer <page-number citation-index="1" label="369">*369</page-number>inventoried the contents of the van. The officer opened a closed backpack in which he found controlled substances, cocaine paraphernalia, and a large amount of cash. Bertine was subsequently charged with driving while under the influence of alcohol, unlawful possession of cocaine with intent to dispense, sell, and distribute, and unlawful possession of methaqualone. We are asked to decide whether the Fourth Amendment prohibits the State from proving these charges with the evidence discovered during the inventory of Ber-tine’s van. We hold that it does not.</p>
<p id="b523-5">The backup officer inventoried the van in accordance with local police procedures, which require a detailed inspection and inventory of impounded vehicles. He found the backpack directly behind the frontseat of the van. Inside the pack, the officer observed a nylon bag containing metal canisters. Opening the canisters, the officer discovered that they contained cocaine, methaqualone tablets, cocaine paraphernalia, and $700 in cash. In an outside zippered pouch of the backpack, he also found $210 in cash in a sealed envelope. After completing the inventory of the van, the officer had the van towed to an impound lot and brought the backpack, money, and contraband to the police station.</p>
<p id="b523-6">After Bertine was charged with the offenses described above, he moved to suppress the evidence found during the inventory search on the ground, <em>inter alia, </em>that the search of the closed backpack and containers exceeded the permissible scope of such a search under the Fourth Amendment. The Colorado trial court ruled that probable causé supported Bertine’s arrest and that the police officers had made the decisions to impound the vehicle and to conduct a thorough inventory search in good faith. Although noting that the inventory of the vehicle was performed in a “somewhat slipshod” manner, the District Court concluded that “the search of the backpack was done for the purpose of protecting the <page-number citation-index="1" label="370">*370</page-number>owner’s property, protection of the police from subsequent claims of loss or stolen property, and the protection of the police from dangerous instrumentalities.” App. 81-83. The court observed that the standard procedures for impounding vehicles mandated a “detailed inventory involving the opening of containers and the listing of [their] contents.” <em>Id., </em>at 81. Based on these findings, the court determined that the inventory search did not violate Bertine’s rights under the Fourth Amendment of the United States Constitution. <em>Id., </em>at 83. The court, nevertheless, granted Bertine’s motion to suppress, holding that the inventory search violated the Colorado Constitution.</p>
<p id="b524-5">On the State’s interlocutory appeal, the Supreme Court of Colorado affirmed. <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/" aria-description="Citation for case: People v. Bertine">706 P. 2d 411</a></span> (1985). In contrast to the District Court, however, the Colorado Supreme Court premised its ruling on the United States Constitution. The court recognized that in <em>South Dakota </em>v. <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976), we had held inventory searches of automobiles to be consistent with the Fourth Amendment, and that in <em>Illinois </em>v. <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">462 U. S. 640</a></span> (1983), we had held that the inventory search of personal effects of an arrestee at a police station was also permissible under that Amendment. The Supreme Court of Colorado felt, however, that our decisions in <em>Arkansas </em>v. <em>Sanders, </em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">442 U. S. 753</a></span> (1979), and <em>United States </em>v. <em>Chadwick, </em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1</a></span> (1977), holding searches of closed trunks and suitcases to violate the Fourth Amendment, meant that <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>did not govern this case.<footnotemark>2</footnotemark></p>
<p id="b524-6">We granted certiorari to consider the important and recurring question of federal law decided by the Colorado Supreme <page-number citation-index="1" label="371">*371</page-number>Court.<footnotemark>3</footnotemark> <span class="citation" data-id="9053299"><a href="/opinion/9059729/colorado-v-bertine/" aria-description="Citation for case: Colorado v. Bertine">475 U. S. 1081</a></span> (1986). As that court recognized, inventory searches are now a well-defined exception to the warrant requirement of the Fourth Amendment. See <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#643" aria-description="Citation for case: Illinois v. Lafayette"><em>Lafayette, supra, </em>at 643</a></span>; <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#367" aria-description="Citation for case: South Dakota v. Opperman"><em>Opperman, supra, </em>at 367-376</a></span>. The policies behind the warrant requirement are not implicated in an inventory search, <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#370" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 370, n. 5</a></span>, nor is the related concept of probable cause:</p>
<blockquote id="b525-5">“The standard of probable cause is peculiarly related to criminal investigations, not routine, noncriminal procedures. . . . The probable-cause approach is unhelpful when analysis centers upon the reasonableness of routine administrative caretaking functions, particularly when no claim is made that the protective procedures are a subterfuge for criminal investigations.” <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Ibid.</a></span></em></blockquote>
<p id="b525-6">See also <em>United States </em>v. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#10" aria-description="Citation for case: United States v. Chadwick"><em>Chadwick, supra, </em>at 10, n. 5</a></span>. For these reasons, the Colorado Supreme Court’s reliance on <em>Arkansas </em>v. <em><span class="citation" data-id="9427641"><a href="/opinion/110119/arkansas-v-sanders/" aria-description="Citation for case: Arkansas v. Sanders">Sanders, supra,</a></span> </em>and <em>United States </em>v. <em><span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">Chadwick, supra,</a></span> </em>was incorrect. Both of these cases concerned searches solely for the purpose of investigating criminal conduct, with the validity of the searches therefore dependent on the application of the probable-cause and warrant requirements of the Fourth Amendment.</p>
<p id="b525-7">By contrast, an inventory search may be “reasonable” under the Fourth Amendment even though it is not conducted pursuant to a warrant based upon probable cause. In <page-number citation-index="1" label="372">*372</page-number><em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>, </em>this Court assessed the reasonableness of an inventory search of the glove compartment in an abandoned automobile impounded by the police. We found that inventory procedures serve to protect an owner’s property while it is in the custody of the police, to insure against claims of lost, stolen, or vandalized property, and to guard the police from danger. In light of these strong governmental interests and the diminished expectation of privacy in an automobile, we upheld the search. In reaching this decision, we observed that our cases accorded deference to police caretaking procedures designed to secure and protect vehicles and their contents within police custody. See <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967); <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968); <em>Cady </em>v. <em>Dombrowski, </em><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447-448</a></span> (1973).<footnotemark>4</footnotemark></p>
<p id="b526-5">In our more recent decision, <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>a police officer conducted an inventory search of the contents of a shoulder bag in the possession of an individual being taken into custody. In deciding whether this search was reasonable, we recognized that the search served legitimate governmental interests similar to those identified in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>. </em>We determined that those interests outweighed the individual’s Fourth Amendment interests and upheld the search.</p>
<p id="b526-6">In the present case, as in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>there was no showing that the police, who were following standardized procedures, acted in bad faith or for the sole purpose of investigation. In addition, the governmental interests justifying the inventory searches in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>are <page-number citation-index="1" label="373">*373</page-number>nearly the same as those which obtain here. In each case, the police were potentially responsible for the property taken into their custody. By securing the property, the police protected the property from unauthorized interference. Knowledge of the precise nature of the property helped guard against claims of theft, vandalism, or negligence. Such knowledge also helped to avert any danger to police or others that may have been posed by the property.<footnotemark>5</footnotemark></p>
<p id="b527-5">The Supreme Court of Colorado opined that <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>was not controlling here because there was no danger of introducing contraband or weapons into a jail facility. Our opinion in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>however, did not suggest that the station-house setting of the inventory search was critical to our holding in that case. Both in the present case and in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>the common governmental interests described above were served by the inventory searches.</p>
<p id="b527-6">The Supreme Court of Colorado also expressed the view that the search in this case was unreasonable because Bertine’s van was towed to a secure, lighted facility and because Bertine himself could have been offered the opportunity to make other arrangements for the safekeeping of his property. But the security of the storage facility does not completely eliminate the need for inventorying; the police may still wish to protect themselves or the owners of the lot against false claims of theft or dangerous instrumentalities. And while giving Bertine an opportunity to make alterna<page-number citation-index="1" label="374">*374</page-number>tive arrangements would undoubtedly have been possible, we said in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>:</em></p>
<blockquote id="b528-5">“[T]he real question is not what ‘could have been achieved,’ but whether the Fourth Amendment <em>requires </em>such steps ....</blockquote>
<blockquote id="b528-6">“The reasonableness of any particular governmental activity does not necessarily or invariably turn on the existence of alternative ‘less intrusive’ means.” <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#647" aria-description="Citation for case: Illinois v. Lafayette">462 U. S., at 647</a></span> (emphasis in original).</blockquote>
<p id="b528-7">See <em>Cady </em>v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski"><em>Dombrowski, supra, </em>at 447</a></span>; <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557, n. 12</a></span> (1976). We conclude that here, as in <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>reasonable police regulations relating to inventory procedures administered in good faith satisfy the Fourth Amendment, even though courts might as a matter of hindsight be able to devise equally reasonable rules requiring a different procedure.<footnotemark>6</footnotemark></p>
<p id="b528-8">The Supreme Court of Colorado also thought it necessary to require that police, before inventorying a container, weigh the strength of the individual’s privacy interest in the container against the possibility that the container might serve as a repository for dangerous or valuable items. We think that such a requirement is contrary to our decisions in <page-number citation-index="1" label="375">*375</page-number><em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span>, </em>and by analogy to our decision in <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982):</p>
<blockquote id="b529-5">“Even if less intrusive means existed of protecting some particular types of property, it would be unreasonable to expect police officers in the everyday course of business to make fine and subtle distinctions in deciding which containers or items may be searched and which must be sealed as a unit.” <span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette"><em>Lafayette, supra, </em>at 648</a></span>.</blockquote>
<blockquote id="b529-6">“When a legitimate search is under way, and when its purpose and its limits have been precisely defined, nice distinctions between closets, drawers, and containers, in the case of a home, or between glove compartments, upholstered seats, trunks, and wrapped packages, in the case of a vehicle, must give way to the interest in the prompt and efficient completion of the task at hand.” <em>United States </em>v. <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#821" aria-description="Citation for case: United States v. Ross"><em>Ross, supra, </em>at 821</a></span>.</blockquote>
<p id="b529-7">We reaffirm these principles here: “‘[a] single familiar standard is essential to guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.’ ” <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette, supra,</a></span> </em>at 648 (quoting <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981)).</p>
<p id="b529-8">Bertine finally argues that the inventory search of his van was unconstitutional because departmental regulations gave the police officers discretion to choose between impounding his van and parking and locking it in a public parking place. The Supreme Court of Colorado did not rely on this argument in reaching its conclusion, and we reject it. Nothing in <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>or <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>prohibits the exercise of police discretion so long as that discretion is exercised according to standard criteria and on the basis of something other than suspicion of evidence of criminal activity. Here, the discretion afforded the Boulder police was exercised in light of <page-number citation-index="1" label="376">*376</page-number>standardized criteria, related to the feasibility and appropriateness of parking and locking a vehicle rather than impounding it.<footnotemark>7</footnotemark> There was no showing that the police chose to impound Bertine’s van in order to investigate suspected criminal activity.</p>
<p id="b530-5">While both <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>are distinguishable from the present case on their facts, we think that the principles enunciated in those cases govern the present one. The judgment of the Supreme Court of Colorado is therefore</p>
<p id="b530-6">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b522-16"><em> </em>Section 7-7-2(a)(4) of the Boulder Revised Code authorizes police officers to impound vehicles when drivers are taken into custody. Section 7-7-2(a)(4) provides:</p>
<blockquote id="b522-17">“A peace officer is authorized to remove or cause to be removed a vehicle from any street, parking lot, or driveway when:</blockquote>
<blockquote id="pAz0">[[Image here]]</blockquote>
<blockquote id="b523-7"><page-number citation-index="1" label="369">*369</page-number>(4) The driver of a vehicle is taken into custody by the police department.” Boulder Rev. Code § 7-7-2(a)(4)(1981).</blockquote>
</footnote>
<footnote label="2">
<p id="b524-7"> Two justices dissented from the majority opinion, arguing that <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>and <em>Illinois </em>v. <em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/" aria-description="Citation for case: Illinois v. Lafayette">Lafayette</a></span> </em>compel the conclusion that the inventory search of the backpack found in Bertine’s van was permissible under the Fourth Amendment.</p>
</footnote>
<footnote label="3">
<p id="b525-8"> Since our decision in <em>South Dakota </em>v. <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span>, </em>several courts have confronted the issue whether police may inventory the contents of containers found in vehicles taken into police custody. See, <em>e. g., United States </em>v. <em>Griffin, </em><span class="citation" data-id="9471903"><a href="/opinion/432054/united-states-v-charles-e-griffin-and-jerome-griffin/" aria-description="Citation for case: United States v. Charles E. Griffin and Jerome Griffin">729 F. 2d 475</a></span> (CA7) (upholding inventory search of package found in paper bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/830/">469 U. S. 830</a></span> (1984); <em>United States </em>v. <em>Bloomfield, </em><span class="citation" data-id="364699"><a href="/opinion/364699/united-states-v-rick-thomas-bloomfield/" aria-description="Citation for case: United States v. Rick Thomas Bloomfield">594 F. 2d 1200</a></span> (CA8 1979) (affirming suppression of evidence found in closed knapsack); <em>People </em>v. <em>Braasch, </em><span class="citation" data-id="2051832"><a href="/opinion/2051832/people-v-braasch/" aria-description="Citation for case: People v. Braasch">122 Ill. App. 3d 747</a></span>, <span class="citation" data-id="2051832"><a href="/opinion/2051832/people-v-braasch/" aria-description="Citation for case: People v. Braasch">461 N. E. 2d 651</a></span> (1984) (upholding inventory of paper bag); <em>People </em>v. <em>Gonzalez, </em>62 N. Y. 2d 386, <span class="citation" data-id="5536314"><a href="/opinion/5687200/people-v-gonzalez/" aria-description="Citation for case: People v. Gonzalez">465 N. E. 2d 823</a></span> (1984) (upholding inventory of paper bag); <em>Boggs </em>v. <em>Commonwealth, </em><span class="citation" data-id="1211186"><a href="/opinion/1211186/boggs-v-commonwealth/" aria-description="Citation for case: Boggs v. Commonwealth">229 Va. 501</a></span>, <span class="citation" data-id="1211186"><a href="/opinion/1211186/boggs-v-commonwealth/" aria-description="Citation for case: Boggs v. Commonwealth">331 S. E. 2d 407</a></span> (1985) (upholding inventory of boxes and pouch found in bag), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./475/1031/">475 U. S. 1031</a></span> (1986).</p>
</footnote>
<footnote label="4">
<p id="b526-7"> The Colorado Supreme Court correctly stated that <em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">Opperman</a></span> </em>did not address the question whether the scope of an inventory search may extend to closed containers located in the interior of an impounded vehicle. We did note, however, that “ ‘when the police take custody of any sort of container [such as] an automobile ... it is reasonable to search the container to itemize the property to be held by the police.’ ” 428 U. S., at 371 (quoting <em>United States </em>v. <em>Gravitt, </em><span class="citation" data-id="313366"><a href="/opinion/313366/united-states-v-jerry-eugene-gravitt/#378" aria-description="Citation for case: United States v. Jerry Eugene Gravitt">484 F. 2d 375, 378</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1135/">414 U. S. 1135</a></span> (1974)).</p>
</footnote>
<footnote label="5">
<p id="b527-7"> In arguing that the latter two interests are not implicated here, the dissent overlooks the testimony of the backup officer who conducted the inventory of Bertine’s van. According to the officer, the vehicle inventory procedures of the Boulder Police Department are designed for the “[p]ro-teetion of the police department” in the event that an individual later claims that “there was something of value taken from within the vehicle.” 2 Tr. 19. The officer added that inventories are also conducted in order to cheek “[f]or any dangerous items such as explosives [or] weapons.” Id., at 20. The officer testified that he had found such items in vehicles.</p>
</footnote>
<footnote label="6">
<p id="b528-9"> We emphasize that, in this case, the trial court found that the Police Department’s procedures mandated the opening of closed containers and the listing of their contents. Our decisions have always adhered to the requirement that inventories be conducted according to standardized criteria. See <em>Lafayette, </em><span class="citation" data-id="9429258"><a href="/opinion/110976/illinois-v-lafayette/#648" aria-description="Citation for case: Illinois v. Lafayette">462 U. S., at 648</a></span>; <em>Opperman, </em><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#374" aria-description="Citation for case: South Dakota v. Opperman">428 U. S., at 374-376</a></span>.</p>
<p id="b528-10">By quoting a portion <em>of </em>the Colorado Supreme Court’s decision out of context, the dissent suggests that the inventory here was not authorized by the standard procedures of the Boulder Police Department. See <em>post, </em>at 380-381. Yet that court specifically stated that the procedure followed here was “officially authorized.” <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/#413" aria-description="Citation for case: People v. Bertine">706 P. 2d 411, 413, n. 2</a></span> (1985). In addition, the court did not disturb the trial court’s finding that the police procedures for impounding vehicles required a detailed inventory of Bertine’s van. See <span class="citation" data-id="9851817"><a href="/opinion/1284293/people-v-bertine/#418" aria-description="Citation for case: People v. Bertine"><em>id., </em>at 418-419</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b530-9"> In arguing that the Boulder Police Department procedures set forth no standardized criteria guiding an officer’s decision to impound a vehicle, the dissent selectively quotes from the police directive concerning the care and security of vehicles taken into police custody. The dissent fails to mention that the directive establishes several conditions that must be met before an officer may pursue the park-and-loek alternative. For example, police may not park and lock the vehicle where there is reasonable risk of damage or vandalism to the vehicle or where the approval of the arrestee cannot be obtained. App. 91-92, 94-95. Not only do such conditions circumscribe the discretion of individual officers, but they also protect the vehicle and its contents and minimize claims of property loss.</p>
</footnote>
</opinion>
```

---
