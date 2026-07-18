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

## GROUP: content/cases/Roaden v. Kentucky.md  (`case`, 5 assertions)

### content_page

```
---
title: Roaden v. Kentucky
type: case
citation: "413 U.S. 496 (1973)"
parallel_cite: "93 S. Ct. 2796; 37 L. Ed. 2d 757"
neutral_cite: 1973 U.S. LEXIS 31
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-25
docket: No. 71-1134
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
  opinion_url: "https://www.courtlistener.com/opinion/108854/roaden-v-kentucky/"
  cluster_id: 108854
  opinion_id: null
  identity_checked: true
lake:
  record_id: Roaden v. Kentucky
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Anchor
related:
  - "[[The Warrant Requirement]]"
  - "[[Marcus v. Search Warrant]]"
  - "[[A Quantity of Copies of Books v. Kansas]]"
  - "[[Heller v. New York]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - prior-restraint
  - first-amendment
  - obscenity
  - seizure
holding: "The warrantless seizure of an allegedly obscene film from a commercial theater, incident to the exhibitor's arrest and based solely on the arresting officer's own conclusion that the film was obscene, is an unreasonable seizure: because the material is presumptively protected by the First Amendment, its seizure is a form of prior restraint that 'calls for a higher hurdle in the evaluation of reasonableness' and ordinarily requires a warrant issued on a prior judicial determination of obscenity."
aliases:
  - Roaden v. Kentucky
  - "Roaden v. Kentucky (1973)"
---

# Roaden v. Kentucky

*413 U.S. 496 (1973)* (No. 71-1134) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 108854 → combined opinion 108854 (Burger, C.J.; 413 U.S. 496, argued Nov. 14, 1972, decided June 25, 1973). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*504`). S9 promotes. -->

## Background
On September 29, 1970, the sheriff of Pulaski County, Kentucky, and the district prosecutor bought tickets to a local drive-in theater and watched a film called "Cindy and Donna." The sheriff concluded the film was obscene and, at its conclusion, went to the projection booth and arrested Roaden, the theater manager, for exhibiting an obscene film in violation of a Kentucky statute. Concurrent with the arrest, and with no warrant and no prior judicial determination of obscenity, the sheriff seized one copy of the film for use as evidence. Roaden's motion to suppress was denied, the film was admitted at trial, and he was convicted; the Court of Appeals of Kentucky affirmed, reasoning the film was properly seized incident to a lawful arrest.

## Issue
Whether allegedly obscene material — a film being exhibited to the public in a commercial theater — may be seized without a warrant, contemporaneously with and incident to an arrest for the public exhibition of that material.

## Rule
A seizure reasonable as to one kind of material may be unreasonable as to another: the seizure of presumptively expressive material implicates the First Amendment and cannot be assimilated to the warrantless seizure of weapons or contraband incident to arrest. Because taking a film in mid-exhibition halts a presumptively protected communication, it is a form of prior restraint and demands more, not less, than the ordinary warrant scrutiny: "Such precipitate action by a police officer, without the authority of a constitutionally sufficient warrant, is plainly a form of prior restraint and is, in those circumstances, unreasonable under Fourth Amendment standards. The seizure is unreasonable, not simply because it would have been easy to secure a warrant, but rather because prior restraint of the right of expression, whether by books or films, calls for a higher hurdle in the evaluation of reasonableness." — 413 U.S. at 504. ^pin-504

## Application
The film was seized on nothing more than the arresting officer's own conclusion that it was obscene; nothing before the seizure gave a magistrate the chance to focus searchingly on the question of obscenity, as *[[Marcus v. Search Warrant|Marcus]]* required. If a warrant to seize allegedly obscene material may not issue on an officer's bare conclusion, then *a fortiori* the officer may not seize it with no warrant at all. Nor was this a "now or never" situation: a film on a regular exhibition schedule in a public theater could be preserved by obtaining a warrant on a prior judicial determination of probable obscenity, without risking loss of the evidence. The incident-to-arrest rationale that justifies seizing a pistol or contraband therefore could not carry over to expressive material.

## Conclusion
The judgment of the Court of Appeals of Kentucky was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Burger, C.J., delivered the opinion of the Court. Brennan, J., joined by Stewart and Marshall, JJ., concurred in the judgment; Douglas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Roaden* is a warrant-requirement anchor for the special protection expressive materials receive at the seizure stage: where the "things to be seized" are presumptively First-Amendment-protected, the Fourth Amendment tolerates no shortcut around the warrant and the prior judicial determination it secures. Teach it alongside its companion *[[Heller v. New York]]* (decided the same day, sustaining a seizure made under a warrant after the magistrate viewed the film) and its antecedents *[[Marcus v. Search Warrant|Marcus]]* and *[[A Quantity of Copies of Books v. Kansas|A Quantity of Books]]*.

## Appears on
- [[Particularity]] — *Anchor*

## Sources
- [*Roaden v. Kentucky*, 413 U.S. 496 (1973)](https://www.courtlistener.com/opinion/108854/roaden-v-kentucky/) — pinpoint: 504 (Burger, C.J., for the Court; the CL opinion text carries the reporter star `*504` at the start of the paragraph containing the quoted "higher hurdle" holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7e7d6ce72003bb06", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "413 U.S. 496 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 31", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2796; 37 L. Ed. 2d 757", "title": "Roaden v. Kentucky", "year": "1973"}}
{"assertion_id": "06a39cef17da542f", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Anchor", "title": "Roaden v. Kentucky"}}
{"assertion_id": "38f2bc9928f2749f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The warrantless seizure of an allegedly obscene film from a commercial theater, incident to the exhibitor's arrest and based solely on the arresting officer's own conclusion that the film was obscene, is an unreasonable seizure: because the material is presumptively protected by the First Amendment, its seizure is a form of prior restraint that 'calls for a higher hurdle in the evaluation of reasonableness' and ordinarily requires a warrant issued on a prior judicial determination of obscenity.", "title": "Roaden v. Kentucky"}}
{"assertion_id": "33e1c0220ce63792", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Roaden v. Kentucky", "varies_by_point": "false"}}
{"assertion_id": "f2b8bebfc1d6760d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Roaden v. Kentucky"}}
```

### lake record — Roaden v. Kentucky

```json
{
  "schema_version": "s2.v1",
  "record_id": "Roaden v. Kentucky",
  "status": "under_review",
  "identity": {
    "case_name": "Roaden v. Kentucky",
    "case_name_short": "Roaden",
    "case_name_full": "Roaden v. Kentucky",
    "input_case_name": "Roaden v. Kentucky",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-25",
    "year": 1973,
    "docket": "No. 71-1134",
    "cluster_id": 108854,
    "lead_opinion_id": 9425416,
    "sibling_ids": [],
    "absolute_url": "/opinion/108854/roaden-v-kentucky/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 496",
      "volume": "413",
      "reporter": "U.S.",
      "page": "496",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2796",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2796",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 757",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 31",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "31",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 496",
        "volume": "413",
        "reporter": "U.S.",
        "page": "496",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2796",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2796",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 757",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 31",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "31",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 496",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 496",
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
    "date_created": "2026-07-06T13:44:00Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "roaden-v-kentucky--108854",
      "to_record_id": "Roaden v. Kentucky",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Roaden v. Kentucky

```
<opinion type="majority">
<author id="b541-4"><page-number citation-index="1" label="497">*497</page-number>Mr. Chief Justice Burger</author>
<p id="AXD">delivered the opinion of of the Court.</p>
<p id="b541-5">The question presented in this case is whether the seizure of allegedly obscene material, contemporaneous with and as an incident to an arrest for the public exhibition of such material in a commercial theater may be accomplished without a warrant.</p>
<p id="b541-6">On September 29, 1970, the sheriff of Pulaski County, Kentucky, accompanied by the district prosecutor, purchased tickets to a local drive-in theater. There the sheriff observed, in its entirety, a film called “Cindy and Donna” and concluded that it was obscene and that its exhibition was in violation of a state statute. A substantial part of the film was also observed by a deputy sheriff from a vantage point on the road outside the theater. Since the petitioner conceded the obscenity of the film at trial, that issue is not before us for decision.<footnotemark>1</footnotemark></p>
<p id="b541-7">The sheriff, at the conclusion of the film, proceeded to the projection booth, where he arrested petitioner, the manager of the theater, on the charge of exhibiting an obscene film to the public contrary to Ky. Rev. Stat. § 436.101 (1973).<footnotemark>2</footnotemark> Concurrent with the arrest, the sheriff <page-number citation-index="1" label="498">*498</page-number>seized one copy of the film for use as evidence. It is uncontested: (a) that the sheriff had no warrant when he made the arrest and seizure, (b) that there had been no <page-number citation-index="1" label="499">*499</page-number>prior determination by a judicial officer on the question of obscenity, and (c) that the arrest was based solely on the sheriff’s observing the exhibition of the film.</p>
<p id="b543-5">On September 30, 1970, the day following the arrest of petitioner and the seizure of the film, the Grand Jury of Pulaski County heard testimony concerning the scenes and content of the film and returned an indictment charging petitioner with exhibiting an obscene film in violation of Ky. Rev. Stat. § 436.101. On October 3, 1970, petitioner entered a plea of not guilty in the Pulaski Circuit Court, and the case was set for trial. On October 12, 1970, petitioner filed a motion to suppress the film as evidence and to dismiss the indictment. The motion was predicated upon the ground that the film was “improperly, unlawfully and illegally seized, contrary to . . . the laws of the land.” Four days later, on October 16, 1970, the Pulaski Circuit Court heard argument at an adversary hearing on petitioner’s motion. The motion was denied.</p>
<p id="b543-6">Petitioner’s trial began on October 20, 1970. The arresting sheriff and one of his deputies were the only witnesses for the prosecution. The sheriff testified that the film displayed nudity and “intimate love scenes.” The sheriff further testified that, upon viewing the film, he determined that it was obscene and that its exhibition <page-number citation-index="1" label="500">*500</page-number>violated state law. He therefore arrested petitioner. Together with the testimony of the sheriff, the film itself was introduced in evidence. Petitioner's motion to suppress the film was renewed, and again overruled. The sheriff’s deputy took the stand and testified that he had viewed the final 30 minutes of the film from a vantage point on a public road outside the theater. Following this testimony, the jury was permitted to see the film.</p>
<p id="b544-5">Petitioner testified in his own behalf. He stated that, to his knowledge, no juveniles had been admitted to see the film, and that he had received no complaints about the film until it was seized by the sheriff. At the close of his testimony, the jury found petitioner guilty as charged. The jury rendered both a general verdict of guilty and a special verdict that the film was obscene, as provided by Ky. Rev. Stat. §436.101 (8).</p>
<p id="b544-6">On appeal, the Court of Appeals of Kentucky affirmed petitioner’s conviction. The Court of Appeals first emphasized that “[i]t was conceded by [petitioner’s] counsel in closing argument to the jury that the film is obscene. No issue is presented on appeal as to the obscenity of the material.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#815" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d 814, 815</a></span> (1971). The Court of Appeals then held that the film was properly seized incident to a lawful arrest, distinguishing the holdings of this Court in <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span> (1964), and <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span> (1961), on the ground that those decisions related to seizure of allegedly obscene materials “for destruction or suppression, not to seizures incident to an arrest for possessing, selling, or exhibiting a specific item.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#815" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d, at 815</a></span>. It also distinguished <em>Lee Art Theatre </em>v. <em>Virginia, </em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S. 636</a></span> (1968), on the grounds that there film “had been seized pursuant to a [defective] search warrant, not incident to an arrest.” <span class="citation" data-id="5038205"><a href="/opinion/5214390/roaden-v-commonwealth/#816" aria-description="Citation for case: Roaden v. Commonwealth">473 S. W. 2d, at 816</a></span>. The Court of Appeals relied on a decision of a federal three-judge <page-number citation-index="1" label="501">*501</page-number>court in <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi">309 F. Supp. 527</a></span> (SD Miss. 1970), which concluded that:</p>
<blockquote id="b545-5">“[Sjeizure of an allegedly obscene film as an incident to lawful arrests for a crime committed in the presence of the arresting officers, i. e., the public showing of such film, does not exceed constitutional bounds in the absence of a prior judicial hearing on the question of its obscenity.” <span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/#533" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi"><em>Id., </em>at 533</a></span>.</blockquote>
<p id="b545-6">The Court of Appeals specifically declined to follow a decision by another federal three-judge court in <em>Ledesma </em>v. <em>Perez, </em><span class="citation" data-id="9690341"><a href="/opinion/1867767/delta-book-distributors-inc-v-cronvich/" aria-description="Citation for case: Delta Book Distributors, Inc. v. Cronvich">304 F. Supp. 662</a></span> (ED La. 1969), which held unconstitutional the seizure of allegedly obscene material incident to an arrest, but without a warrant or a prior adversary hearing.<footnotemark>3</footnotemark></p>
<p id="b545-7">I</p>
<p id="b545-8">The Fourth Amendment proscription against “unreasonable . . . seizures,” applicable to the States through the Fourteenth Amendment, must not be read in a vacuum. A seizure reasonable as to one type of material in one setting may be unreasonable in a different setting or with respect to another kind of material. Cf. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#471" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 471-472</a></span> (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#509" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., at </em>509-510</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#512" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 512-513</a></span> (White, J., concurring and dissenting). The question to be resolved is whether the seizure of the film without a warrant was unreasonable under Fourth Amendment standards and, if so, <page-number citation-index="1" label="502">*502</page-number>whether the film was therefore inadmissible at-the trial. The seizure of instruments of a crime, such as a pistol or a knife, or “contraband or stolen goods or objects dangerous in themselves,” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#472" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 472</a></span>, are to be distinguished from quantities of books and movie films when a court appraises the reasonableness of the seizure under Fourth or Fourteenth Amendment standards.</p>
<p id="b546-5"><em>Marcus </em>v. <em>Search <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Warrant, supra,</a></span> </em>held that a warrant for the seizure of allegedly obscene books could not be issued on the conclusory opinion of a police officer that the books sought to be seized were obscene. Such a warrant lacked the safeguards demanded “to assure nonobscene material the constitutional protection to which it is entitled. . . . [T]he warrants issued on the strength of the conclusory assertions of a single police officer, without any scrutiny by the judge of any materials considered by the complainant to be obscene.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#731" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 731-732</a></span>. There had been “no step in the procedure before seizure designed to focus searchingly on the question of obscenity.” <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Id., </em>at 732</a></span>.</p>
<p id="b546-6">The sense of this holding was reaffirmed in <em>A Quantity of Books </em>v. <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">Kansas, supra,</a></span> </em>where the Court found unconstitutional a “massive seizure” of books from a commercial bookstore for the purpose of destroying the books as contraband. The result was premised on the lack of an adversary hearing prior to seizure, and the Court did not find it necessary to reach the claim that the seizure violated Fourth Amendment standards. <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S., at 210</a></span> n. 2. However, the Court emphasized:</p>
<blockquote id="b546-7">“It is no answer to say that obscene books are contraband, and that consequently the standards governing searches and seizures of allegedly obscene books should not differ from those applied with respect to narcotics, gambling paraphernalia and <page-number citation-index="1" label="503">*503</page-number>other contraband. We rejected that proposition in <span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/#211" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas"><em>Marcus.” Id., </em>at 211-212</a></span>.</blockquote>
<p id="b547-5"><em>Lee Art Theatre </em>v. <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Virginia, supra,</a></span> </em>was to the same effect with regard to seizure of a film from a commercial theater regularly open to the public. There a warrant for the seizure of the film was issued on the basis of a police officer’s affidavit giving the titles of the film and asserting in conclusory fashion that he had personally viewed the films and considered them obscene. The films were seized pursuant to the warrant and introduced into evidence in a criminal case against the exhibitor. Conviction ensued. On review, the Court held that “[t]he admission of the films in evidence requires reversal of petitioner’s conviction” because</p>
<blockquote id="b547-6">“[t]he procedure under which the warrant issued solely upon the conclusory assertions of the police officer without any inquiry by the justice of the peace into the factual basis for the officer’s conclusions was not a procedure 'designed to focus searchingly on the question of obscenity,’ <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">id.,</a></span> [Marcus </em>v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Search Warrant, </em>supra] at 732</a></span>, and therefore fell short of constitutional requirements demanding necessary sensitivity to freedom of expression.” <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>.</blockquote>
<p id="b547-7">No mention was made in the brief <em>per curiam Lee Art Theatre </em>opinion as to whether or not the seizure was incident to an arrest. The Court relied on <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>and <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span>.</em></p>
<p id="b547-8">The common thread of <em>Marcus, A Quantity of Books, </em>and <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span> </em>is to be found in the nature of the materials seized and the setting in which they were taken. See <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#486" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 486</a></span> (1965).<footnotemark>4</footnotemark> <page-number citation-index="1" label="504">*504</page-number>In each case the material seized fell arguably within First Amendment protection, and the taking brought to an abrupt halt an orderly and presumptively legitimate distribution or exhibition. Seizing a film then being exhibited to the general public presents essentially the same restraint on expression as the seizure of all the books in <em>a </em>bookstore. Such precipitate action by a police officer, without the authority of a constitutionally sufficient warrant, is plainly a form of prior restraint and is, in those circumstances, unreasonable under Fourth Amendment standards. The seizure is unreasonable, not simply because it would have been easy to secure a warrant, but rather because prior restraint of the right of expression, whether by books or films, calls for a higher hurdle in the evaluation of reasonableness. The setting of the bookstore or the commercial theater, each presumptively under the protection of the First Amendment, invokes such Fourth Amendment warrant requirements because we examine what is “unreasonable” in the light of the values of freedom of expression.<footnotemark>5</footnotemark> As we stated in <em>Stanford </em>v. <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas, supra:</a></span></em></p>
<blockquote id="b548-5">“In short, . . . the constitutional requirement that warrants must particularly describe the ‘things to be seized’ is to be accorded the most scrupulous exactitude when the ‘things’ are books, and the basis for their seizure is the ideas which they contain. See <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717</a></span>; <em>A Quantity of Books </em>v. <em>Kansas, </em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">378 U. S. 205</a></span>. No less a standard could be faithful to First Amendment freedoms. The constitutional impossibility of leav<page-number citation-index="1" label="505">*505</page-number>ing the protection of those freedoms to the whim of the officers charged with executing the warrant is dramatically underscored by what the officers saw fit to seize under the warrant in this case.” <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas">379 U. S., at 485</a></span> (footnotes omitted).</blockquote>
<p id="b549-5">Moreover, ordinary human experience should teach that the seizure of a movie film from a commercial theater with regularly scheduled performances, where a film is being played and replayed to paid audiences, presents a very different situation from that in which contraband is changing hands or where a robbery or assault is being perpetrated. In the latter settings, the probable cause for an arrest might justify the seizure of weapons, or other evidence or instruments of crime, without a warrant. Cf. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#764" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 764</a></span> (1969); <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#773" aria-description="Citation for case: Chimel v. California"><em>id., </em>at 773-774</a></span> (White, J., dissenting); <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Where there are exigent circumstances in which police action literally must be “now or never” to preserve the evidence of the crime, it is reasonable to permit action without prior judicial evaluation.<footnotemark>6</footnotemark> See <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#47" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 47-51</a></span> (1970). Cf. <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925). The facts surrounding the “massive seizures” of books in <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em><page-number citation-index="1" label="506">*506</page-number>and <em><span class="citation" data-id="9422858"><a href="/opinion/106878/a-quantity-of-copies-of-books-v-kansas/" aria-description="Citation for case: A Quantity of Copies of Books v. Kansas">A Quantity of Books</a></span>, </em>or the seizure of the film in <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span>, </em>presented no such “now or never” circumstances.</p>
<p id="b550-5">II</p>
<p id="b550-6">The film seized in this case was being exhibited at a commercial theater showing regularly scheduled performances to the general public. The seizure proceeded solely on a police officer’s conclusions that the film was obscene; there was no warrant. Nothing prior to seizure afforded a magistrate an opportunity to “focus searchingly on the question of obscenity.” See <em>Heller </em>v. <em>New York, ante, </em>at 488-489; <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#732" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S., at 732</a></span>. If, as <em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/" aria-description="Citation for case: Marcus v. Search Warrant of Property">Marcus</a></span> </em>and <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span> </em>held, a warrant for seizing allegedly obscene material may not issue on the mere conclusory allegations of an officer, <em>a fortiori, </em>the officer may not make such a seizure with no warrant at all. “The use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new. . . . The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression.” <em>Marcus </em>v. <span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property"><em>Search Warrant, supra, </em>at 724, 729</a></span>. In this case, as in <em><span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">Lee Art Theatre</a></span>, </em>the admission of the film in evidence requires reversal of petitioner’s conviction. <span class="citation" data-id="9423825"><a href="/opinion/107755/lee-art-theatre-inc-v-virginia/#637" aria-description="Citation for case: Lee Art Theatre, Inc. v. Virginia">392 U. S., at 637</a></span>.</p>
<p id="b550-7">The judgment of the Court of Appeals of Kentucky is reversed and this case remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b550-8">
<em>Reversed and remanded.</em>
</p>
<p id="b550-9">[For dissenting opinion of Mr. Justice Douglas, see <em>ante, </em>p. 494.]</p>
<footnote label="1">
<p id="b541-8"> Petitioner’s lawyer made the following statement to the trial jury during the closing arguments:</p>
<blockquote id="b541-9">“I would be good enough to tell you at the outset that, in behalf of Mr. Roaden, I am not going to get up here and defend the film observed yesterday nor the revolting scenes in it or try to argue or persuade you that those scenefs] were not obscene.” App. 37.</blockquote>
</footnote>
<footnote label="2">
<p id="b541-10"> Kentucky Revised Statutes §436.101 (1973), reads in relevant part as follows:</p>
<blockquote id="b541-11">“Obscene matter, distribution, penalties, destruction.</blockquote>
<blockquote id="b541-12">“(1) As used in this section:</blockquote>
<blockquote id="b541-13">“(a) 'Distribute' means to transfer possession of, whether with or without consideration.</blockquote>
<blockquote id="b541-14">“(b) ‘Matter’ means any book, magazine, newspaper, or other printed or written material or any picture, drawing, photograph, motion picture, or other pictorial representation or any statue or <page-number citation-index="1" label="498">*498</page-number>other figure, or any recording, transcription or mechanical, chemical or electrical reproduction or any other articles, equipment, machines or materials.</blockquote>
<blockquote id="AMp">“(c) 'Obscene’ means that to the average person, applying contemporary standards, the predominant appeal of the matter, taken as a whole, is to prurient interest, a shameful or morbid interest in nudity, sex, or excretion, which goes substantially beyond customary limits of candor in description or representation of such matters.</blockquote>
<blockquote id="ATl9">“(d) 'Person’ means any individual, partnership, firm, association, corporation, or other legal entity.</blockquote>
<blockquote id="AQz">“(2) Any person who, having knowledge of the obscenity thereof, sends or causes to be sent, or brings or causes to be brought, into this state for sale or distribution, or in this state prepares, publishes, prints, exhibits, distributes, or offers to distribute, or has in his possession with intent to distribute or to exhibit or offer to distribute, any obscene matter is punishable by fine of not more than $1,000 plus five dollars ($5.00) for each additional unit of material coming within the provisions of this chapter, which is involved in the offense, not to exceed ten thousand dollars ($10,000), or by imprisonment in the county jail for not more than six (6) months plus one (1) day for each additional unit of material coming -within the provisions of this chapter, and which is involved in the offense, such basic maximum and additional days not to exceed 360 days in the county jail, or by both such fine and imprisonment. If such person has previously been convicted of a violation of this subsection, he is punishable by fine of not more than $2,000 plus five dollars ($5.00) for each additional unit of material coming within the provisions of this chapter, which is involved in the offense, not to exceed $25,000, or by imprisonment in the county jail for not more than one (1) year, or by both such fine and such imprisonment. If a person has been twice convicted of a violation of this section, a violation of this subsection is punishable by imprisonment in the state penitentiary not exceeding five (5) years.</blockquote>
<blockquote id="A_DJ">“(8) The jury, or the court, if a jury trial is waived, shall render a general verdict, and shall also render a special verdict as to whether the matter named in the charge is obscene. The special <page-number citation-index="1" label="499">*499</page-number>verdict or findings on the issue of obscenity may be: ‘We find the . . . (title or description of matter) to be obscene,’ or, ‘We find the . . . (title or description of matter) not to be obscene/ as they may find each item is or is not obscene.</blockquote>
<blockquote id="Aob">“ (9) Upon the conviction of the accused, the court may, when the conviction becomes final, order any matter or advertisement, in respect whereof the accused stands convicted, and which remains in the possession or under the control of the attorney general, commonwealth’s attorney, county attorney, city attorney or their authorized assistants, or any law enforcement agency, to be destroyed, and the court may cause to be destroyed any such material in its possession or under its control.”</blockquote>
</footnote>
<footnote label="3">
<p id="b545-9"> We vacated the judgment in <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation" data-id="9716282"><a href="/opinion/2096144/hosey-v-city-of-jackson-mississippi/" aria-description="Citation for case: Hosey v. City of Jackson, Mississippi">309 F. Supp. 527</a></span> (SD Miss. 1970), on the grounds of the Court’s policy of noninterference in state prosecution; we did not reach the merits. <em>Hosey </em>v. <em>City of Jackson, </em><span class="citation multiple-matches"><a href="/c/U.%20S./401/987/">401 U. S. 987</a></span> (1971). We also vacated the judgment in <em>Ledesma </em>v. <em>Perez, </em><span class="citation" data-id="9690341"><a href="/opinion/1867767/delta-book-distributors-inc-v-cronvich/" aria-description="Citation for case: Delta Book Distributors, Inc. v. Cronvich">304 F. Supp. 662</a></span> (ED La. 1969), again on the grounds of noninterference with state criminal proceedings prior to adjudications by state courts. <em>Perez </em>v. <em>Ledesma, </em><span class="citation" data-id="9424442"><a href="/opinion/108266/perez-v-ledesma/" aria-description="Citation for case: Perez v. Ledesma">401 U. S. 82</a></span> (1971).</p>
</footnote>
<footnote label="4">
<p id="b547-9"> In <em>Stanford </em>v. <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">Texas, supra,</a></span> </em>we acknowledged the difference between books and weapons, narcotics, or cases of whiskey.</p>
</footnote>
<footnote label="5">
<p id="b548-6"> This does not mean an adversary proceeding is needed before seizure, since a warrant may be issued <em>ex parte. Heller </em>v. <em>New York, ante, </em>p. 483.</p>
</footnote>
<footnote label="6">
<p id="b549-6"> Counsel for Kentucky, together with counsel for New York in <em>Heller </em>v. <em>New York, ante, </em>at 493, and counsel for California as <em>amicus curiae </em>in <em>Heller, </em>have emphasized that allegedly obscene films are particularly difficult evidence to preserve unless kept in custody. We again take judicial notice that films may be compact, may be easy to destroy or to remove to another jurisdiction, and may be subject to pretrial alterations by cutting out scenes and resplicing reels. See <em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">ibid.</a></span> </em>But, as the <em>Heller </em>case demonstrates, where films are scheduled for exhibition in a commercial theater open to the public, procuring a warrant based on a prior judicial determination of probable cause of obscenity need not risk loss of the evidence.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Rodriguez v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Rodriguez v. United States"
type: case
citation: ""
parallel_cite: "575 U.S. 348; 135 S. Ct. 1609; 191 L. Ed. 2d 492; 83 U.S.L.W. 4241; 25 Fla. L. Weekly Fed. S 191"
neutral_cite: 2015 U.S. LEXIS 2807
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-04-21
docket: 13-9972
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Rodriguez v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2795278/rodriguez-v-united-states/"
  cluster_id: 2795278
  opinion_id: 9806947
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
related: ["[[Pennsylvania v. Mimms]]", "[[Delaware v. Prouse]]", "[[Berkemer v. McCarty]]"]
aliases: ["Rodriguez v. United States (2015)"]
tags: ["case", "fourth-amendment", "traffic-stops", "stop-duration", "dog-sniff", "mission"]
holding: "A traffic stop may last no longer than necessary to complete the stop's 'mission' (addressing the violation and ordinary inquiries).…"
lake:
  record_id: Rodriguez v. United States
  status: verified
  projected_at: 2026-07-06
---

# Rodriguez v. United States

*575 U.S. 348 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Struble, a K-9 officer, stopped Rodriguez for driving on the highway shoulder. After attending to everything relating to the stop — checking the licenses of Rodriguez and his passenger and issuing a written warning — Struble asked to walk his dog around the car. Rodriguez refused. Struble detained him until a second officer arrived, then ran the dog, which alerted; the ensuing search found methamphetamine. Seven or eight minutes elapsed from the written warning to the alert.

## Issue
Whether a traffic stop, otherwise completed, may be extended — even briefly — to conduct a dog sniff without independent reasonable suspicion.

## Rule
No. "We hold that a police stop exceeding the time needed to handle the matter for which the stop was made violates the Constitution's shield against unreasonable seizures." — *Rodriguez v. United States*, 575 U.S. 348 (slip op., at 1). ^pin-op1

The stop's "mission" — addressing the traffic violation and related safety concerns, plus ordinary inquiries like license, warrant, registration, and insurance checks — defines its permissible length: "Authority for the seizure thus ends when tasks tied to the traffic infraction are — or reasonably should have been — completed." — *Id.* (slip op., at 5). ^pin-op5

A dog sniff is not an ordinary incident of a traffic stop, and an officer may not prolong the stop to conduct one absent reasonable suspicion.

## Application
Struble had completed the traffic mission — he issued the written warning and returned the documents — before detaining Rodriguez for the dog sniff. Because a dog sniff is aimed at detecting ordinary criminal wrongdoing rather than the traffic violation, the added seven-to-eight minutes prolonged the seizure beyond its mission, and Struble lacked reasonable suspicion to justify the extension. Extending the completed stop for the sniff therefore violated the Fourth Amendment.

## Conclusion
A traffic stop may not be prolonged beyond the time needed to complete its mission to conduct a dog sniff without reasonable suspicion; the judgment was [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] (for the lower courts to address whether reasonable suspicion independently justified the detention).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Rodriguez* is the controlling rule on permissible traffic-stop duration.

## Appears on
- [[Traffic Stops]] — *Key — Anchor*

## Sources
- *Rodriguez v. United States*, 575 U.S. 348 (2015) — https://www.courtlistener.com/opinion/2795278/rodriguez-v-united-states/ — pinpoints: slip op., at 1, 5 (CL carries the slip opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5f39c7ec4facad1a", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 2807", "official_citation_present": false, "parallel_cite": "575 U.S. 348; 135 S. Ct. 1609; 191 L. Ed. 2d 492; 83 U.S.L.W. 4241; 25 Fla. L. Weekly Fed. S 191", "title": "Rodriguez v. United States", "year": "2015"}}
{"assertion_id": "57e9af0bf8c065b2", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A traffic stop may last no longer than necessary to complete the stop's 'mission' (addressing the violation and ordinary inquiries).…", "title": "Rodriguez v. United States"}}
{"assertion_id": "fbaf23af58a4a5ce", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Anchor", "title": "Rodriguez v. United States"}}
{"assertion_id": "c80161e6c9b73b8f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-04-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Rodriguez v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Rodriguez v. United States", "varies_by_point": "false"}}
{"assertion_id": "f96ccb764631673b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Rodriguez v. United States"}}
```

### lake record — Rodriguez v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Rodriguez v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Rodriguez v. United States",
    "case_name_short": "Rodriguez",
    "case_name_full": "Dennys RODRIGUEZ, Petitioner v. UNITED STATES.",
    "input_case_name": "Rodriguez v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-04-21",
    "year": 2015,
    "docket": "13-9972",
    "cluster_id": 2795278,
    "lead_opinion_id": 9806947,
    "sibling_ids": [
      2795278,
      9806947,
      9806948,
      9806949
    ],
    "absolute_url": "/opinion/2795278/rodriguez-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9271110,
        "score": 10,
        "case_name": "Bruff v. North Mississippi Health Services, Inc."
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "575 U.S. 348",
        "volume": "575",
        "reporter": "U.S.",
        "page": "348",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1609",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 492",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4241",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4241",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 191",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 2807",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "2807",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "575 U.S. 348",
        "volume": "575",
        "reporter": "U.S.",
        "page": "348",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 S. Ct. 1609",
        "volume": "135",
        "reporter": "S. Ct.",
        "page": "1609",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "191 L. Ed. 2d 492",
        "volume": "191",
        "reporter": "L. Ed. 2d",
        "page": "492",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 2807",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "2807",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 U.S.L.W. 4241",
        "volume": "83",
        "reporter": "U.S.L.W.",
        "page": "4241",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 191",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "191",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-op1",
      "page": null,
      "quote": "--- # Rodriguez v. United States *575 U.S. 348 (2015)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officer Struble, a K-9 officer, stopped Rodriguez for driving on the highway shoulder. After attending to everything relating to the stop \u2014 checking the licenses of Rodriguez and his passenger and issuing a written warning \u2014 Struble asked to walk his dog around the car. Rodriguez refused. Struble detained him until a second officer arrived, then ran the dog, which alerted; the ensuing search found methamphetamine. Seven or eight minutes elapsed from the written warning to the alert. ## Issue Whether a traffic stop, otherwise completed, may be extended \u2014 even briefly \u2014 to conduct a dog sniff without independent reasonable suspicion. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op5",
      "page": null,
      "quote": "\u2014 addressing the traffic violation and related safety concerns, plus ordinary inquiries like license, warrant, registration, and insurance checks \u2014 defines its permissible length:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Rodriguez v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4543099,
          "cite": [
            "301 Neb. 293",
            "917 N.W.2d 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lerma v. State",
          "cluster_id": 6241263,
          "cite": [
            "543 S.W.3d 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kruse",
          "cluster_id": 4643214,
          "cite": [
            "303 Neb. 799",
            "931 N.W.2d 148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "William Windham v. Harris County, Texas",
          "cluster_id": 4442638,
          "cite": [
            "875 F.3d 229"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Boyce",
          "cluster_id": 4765497,
          "cite": [
            "2020 Ohio 3573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Casillas",
          "cluster_id": 4240603,
          "cite": [
            "830 F.3d 403",
            "2016 FED App. 0171P",
            "2016 U.S. App. LEXIS 13303"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mark Dunbar (077839) (Monmouth and Statewide",
          "cluster_id": 4407425,
          "cite": [
            "229 N.J. 521",
            "163 A.3d 875",
            "2017 WL 2962256",
            "2017 N.J. LEXIS 747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Palmer",
          "cluster_id": 3196774,
          "cite": [
            "820 F.3d 640",
            "2016 WL 1594793"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez",
          "cluster_id": 8443636,
          "cite": [
            "877 F.3d 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andrea Miller v. Woodston Maddox",
          "cluster_id": 4415813,
          "cite": [
            "866 F.3d 386",
            "2017 FED App. 0170P",
            "2017 WL 3298570",
            "2017 U.S. App. LEXIS 14256"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chiaverini v. City of Napoleon",
          "cluster_id": 9598798,
          "cite": [
            "602 U.S. 556"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wayne Hill",
          "cluster_id": 3187279,
          "cite": [
            "818 F.3d 289",
            "2016 U.S. App. LEXIS 5073",
            "2016 WL 1085115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raul De La Rosa v. Mark White",
          "cluster_id": 4378490,
          "cite": [
            "852 F.3d 740",
            "2017 WL 1130225",
            "2017 U.S. App. LEXIS 5273"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Evans",
          "cluster_id": 2802206,
          "cite": [
            "786 F.3d 779",
            "15 Cal. Daily Op. Serv. 4997",
            "2015 U.S. App. LEXIS 8293",
            "2015 WL 2385010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jayel Antrone Coleman",
          "cluster_id": 4347860,
          "cite": [
            "890 N.W.2d 284",
            "2017 WL 541063",
            "2017 Iowa Sup. LEXIS 11"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bass",
          "cluster_id": 4873731,
          "cite": [
            "182 N.E.3d 714",
            "450 Ill. Dec. 902",
            "2021 IL 125434"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Hall v. City of Chicago",
          "cluster_id": 4738333,
          "cite": [
            "953 F.3d 945"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In the Matter of Property Seized From Robert Pardee, Robert Pardee",
          "cluster_id": 3161850,
          "cite": [
            "872 N.W.2d 384",
            "2015 Iowa Sup. LEXIS 101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest D. Shields",
          "cluster_id": 2808513,
          "cite": [
            "789 F.3d 733",
            "2015 U.S. App. LEXIS 10058",
            "2015 WL 3654318"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dwight M. Nelson a/k/a Nelson Dwight (080612)(Union County and Statewide)",
          "cluster_id": 4650558,
          "cite": [
            "206 A.3d 408",
            "237 N.J. 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zavian Jordan",
          "cluster_id": 4731958,
          "cite": [
            "952 F.3d 160"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Rodriguez v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2795278 OR 9806947 OR 9806948 OR 9806949) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjU0ODE5MjAwMDAwJnM9NjQ3NjYzNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282795278+OR+9806947+OR+9806948+OR+9806949%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(2795278 OR 9806947 OR 9806948 OR 9806949)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MiZzPTI4MDA0MzMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282795278+OR+9806947+OR+9806948+OR+9806949%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2795278 OR 9806947 OR 9806948 OR 9806949)",
        "reviewed": 186,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 186,
        "triage_read": 2,
        "triage_snippet_classified": 184
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2795278 OR 9806947 OR 9806948 OR 9806949)",
    "indexed_citing_opinions": 923,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2795278,
        "count": 434,
        "count_source": "search"
      },
      {
        "opinion_id": 9806947,
        "count": 492,
        "count_source": "search"
      },
      {
        "opinion_id": 9806948,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9806949,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2097,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/rodriguez-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNjk1Mzcmcz0xMDU5MzA2MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%282795278+OR+9806947+OR+9806948+OR+9806949%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2795278,
        "cited_id": 73644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 136990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 137742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 145912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 155035,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 168633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 215288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 606689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 688703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 765041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 774866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 775454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 776249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 787338,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 794433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 795668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 1196784,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 1274645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 2600016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2795278,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T17:38:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:41:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:41:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:44:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:41:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Rodriguez v. United States

```
<opinion type="majority">
<author id="p-10">Justice GINSBURGdelivered the opinion of the Court.</author>
<p id="p-11">In <em>Illinois v. Caballes,</em><extracted-citation case-ids="5902584" index="0" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S. 405</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="1" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="2" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">160 L.Ed.2d 842</a></span></extracted-citation> (2005), this Court held that a dog sniff conducted during a lawful traffic stop does not violate the Fourth Amendment's proscription of unreasonable seizures. This case presents the question whether the Fourth Amendment tolerates a dog sniff conducted after completion of a traffic stop. We hold that a police stop exceeding the time needed to handle the matter for which the stop was made violates the Constitution's shield against unreasonable seizures. A seizure justified only by a police-observed traffic violation, therefore, "become[s] unlawful if it is prolonged beyond the time reasonably required to complete th[e] mission" of issuing a ticket for the violation. <em><extracted-citation case-ids="5902584" index="3" url="https://cite.case.law/us/543/405/">Id</extracted-citation></em><extracted-citation case-ids="5902584" index="3" url="https://cite.case.law/us/543/405/">., at 407</extracted-citation>, <extracted-citation case-ids="5902584" index="4" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>. The Court so recognized in <em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">Caballes</a></span>,</em>and we adhere to the line drawn in that decision.</p>
<p id="p-12">I</p>
<p id="p-13">Just after midnight on March 27, 2012, police officer Morgan Struble observed a Mercury Mountaineer veer slowly onto the shoulder of Nebraska State Highway 275 for one or two seconds and then jerk back onto the road. Nebraska law prohibits driving on highway shoulders, see Neb.Rev.Stat. § 60-6,142 (2010), and on that basis, Struble pulled the Mountaineer over at 12:06 a.m. Struble is a K-9 officer with the Valley Police Department in Nebraska, and his dog Floyd was in his patrol car that night. Two men were in the Mountaineer: the driver, Dennys Rodriguez, and a front-seat passenger, Scott Pollman.</p>
<p id="p-14"><a class="page-label" data-citation-index="1" data-label="1613" href="#p1613" id="p1613">*1613</a>Struble approached the Mountaineer on the passenger's side. After Rodriguez identified himself, Struble asked him why he had driven onto the shoulder. Rodriguez replied that he had swerved to avoid a pothole. Struble then gathered Rodriguez's license, registration, and proof of insurance, and asked Rodriguez to accompany him to the patrol car. Rodriguez asked if he was required to do so, and Struble answered that he was not. Rodriguez decided to wait in his own vehicle.</p>
<p id="p-15">After running a records check on Rodriguez, Struble returned to the Mountaineer. Struble asked passenger Pollman for his driver's license and began to question him about where the two men were coming from and where they were going. Pollman replied that they had traveled to Omaha, Nebraska, to look at a Ford Mustang that was for sale and that they were returning to Norfolk, Nebraska. Struble returned again to his patrol car, where he completed a records check on Pollman, and called for a second officer. Struble then began writing a warning ticket for Rodriguez for driving on the shoulder of the road.</p>
<p id="p-16">Struble returned to Rodriguez's vehicle a third time to issue the written warning. By 12:27 or 12:28 a.m., Struble had finished explaining the warning to Rodriguez, and had given back to Rodriguez and Pollman the documents obtained from them. As Struble later testified, at that point, Rodriguez and Pollman "had all their documents back and a copy of the written warning. I got all the reason[s] for the stop out of the way[,] ... took care of all the business." App. 70.</p>
<p id="p-17">Nevertheless, Struble did not consider Rodriguez "free to leave." <em>Id.,</em>at 69-70. Although justification for the traffic stop was "out of the way," <em>id.,</em>at 70, Struble asked for permission to walk his dog around Rodriguez's vehicle. Rodriguez said no. Struble then instructed Rodriguez to turn off the ignition, exit the vehicle, and stand in front of the patrol car to wait for the second officer. Rodriguez complied. At 12:33 a.m., a deputy sheriff arrived. Struble retrieved his dog and led him twice around the Mountaineer. The dog alerted to the presence of drugs halfway through Struble's second pass. All told, seven or eight minutes had elapsed from the time Struble issued the written warning until the dog indicated the presence of drugs. A search of the vehicle revealed a large bag of methamphetamine.</p>
<p id="p-18">Rodriguez was indicted in the United States District Court for the District of Nebraska on one count of possession with intent to distribute 50 grams or more of methamphetamine, in violation of <extracted-citation index="5" url="https://cite.case.law/citations/?q=21%20U.S.C.%20%C2%A7%C2%A7%20841"><span class="citation no-link">21 U.S.C. §§ 841</span></extracted-citation>(a)(1)and (b)(1). He moved to suppress the evidence seized from his car on the ground, among others, that Struble had prolonged the traffic stop without reasonable suspicion in order to conduct the dog sniff.</p>
<p id="p-19">After receiving evidence, a Magistrate Judge recommended that the motion be denied. The Magistrate Judge found no probable cause to search the vehicle independent of the dog alert. App. 100 (apart from "information given by the dog," "Officer Struble had [no]thing other than a rather large hunch"). He further found that no reasonable suspicion supported the detention once Struble issued the written warning. He concluded, however, that under Eighth Circuit precedent, extension of the stop by "seven to eight minutes" for the dog sniff was only a <em>de minimis</em>intrusion on Rodriguez's Fourth Amendment rights and was therefore permissible.</p>
<p id="p-20">The District Court adopted the Magistrate Judge's factual findings and legal conclusions and denied Rodriguez's motion to suppress. The court noted that, in the Eighth Circuit, "dog sniffs that occur within a short time following the completion of <a class="page-label" data-citation-index="1" data-label="1614" href="#p1614" id="p1614">*1614</a>a traffic stop are not constitutionally prohibited if they constitute only de minimis intrusions." App. 114 (quoting <em>United States v. Alexander,</em><extracted-citation case-ids="6046952" index="6" url="https://cite.case.law/f3d/448/1014/#p1016"><span class="citation" data-id="794433"><a href="/opinion/794433/united-states-v-james-stephen-alexander-ii/" aria-description="Citation for case: United States v. James Stephen Alexander, II">448 F.3d 1014</a></span></extracted-citation>, 1016 (C.A.8 2006)). The court thus agreed with the Magistrate Judge that the "7 to 10 minutes" added to the stop by the dog sniff "was not of constitutional significance." App. 114. Impelled by that decision, Rodriguez entered a conditional guilty plea and was sentenced to five years in prison.</p>
<p id="p-21">The Eighth Circuit affirmed. The "seven- or eight-minute delay" in this case, the opinion noted, resembled delays that the court had previously ranked as permissible. <extracted-citation case-ids="3898384" index="7" url="https://cite.case.law/f3d/741/905/#p907"><span class="citation" data-id="2651839"><a href="/opinion/2651839/united-states-v-dennys-rodriguez/" aria-description="Citation for case: United States v. Dennys Rodriguez">741 F.3d 905</a></span></extracted-citation>, 907 (2014). The Court of Appeals thus ruled that the delay here constituted an acceptable "<em>de minimis</em>intrusion on Rodriguez's personal liberty." <span class="citation" data-id="2651839"><a href="/opinion/2651839/united-states-v-dennys-rodriguez/#908" aria-description="Citation for case: United States v. Dennys Rodriguez"><em>Id.,</em>at 908</a></span>. Given that ruling, the court declined to reach the question whether Struble had reasonable suspicion to continue Rodriguez's detention after issuing the written warning.</p>
<p id="p-22">We granted certiorari to resolve a division among lower courts on the question whether police routinely may extend an otherwise-completed traffic stop, absent reasonable suspicion, in order to conduct a dog sniff.573 U.S. ----, <extracted-citation case-ids="12592880,12592881,12592882,12592883,12592884" index="8" url="https://cite.case.law/s-ct/135/43/"><span class="citation multiple-matches"><a href="/c/S.Ct./135/43/">135 S.Ct. 43</a></span></extracted-citation>, <extracted-citation case-ids="12592881,12592882,12592883,12592920,12592921,12593054" index="9" url="https://cite.case.law/l-ed-2d/189/896/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/189/896/">189 L.Ed.2d 896</a></span></extracted-citation> (2014). Compare, <em>e.g.,</em> <em>United States v. Morgan,</em><extracted-citation case-ids="9465618" index="10" url="https://cite.case.law/f3d/270/625/#p632"><span class="citation" data-id="9494522"><a href="/opinion/775454/united-states-of-america-v-rosalind-sarah-morgan-fredine-walker-elijah-m/" aria-description="Citation for case: United States of America v. Rosalind Sarah Morgan Fredine...">270 F.3d 625</a></span></extracted-citation>, 632 (C.A.8 2001)(postcompletion delay of "well under ten minutes" permissible), with, <em>e.g.,</em> <em>State v. Baker,</em><extracted-citation case-ids="6993443" index="11" url="https://cite.case.law/p3d/229/650/"><span class="citation" data-id="2600016"><a href="/opinion/2600016/state-v-baker/" aria-description="Citation for case: State v. Baker">2010 UT 18</a></span></extracted-citation>, ¶ 13, <extracted-citation case-ids="6993443" index="12" url="https://cite.case.law/p3d/229/650/"><span class="citation" data-id="2600016"><a href="/opinion/2600016/state-v-baker/" aria-description="Citation for case: State v. Baker">229 P.3d 650</a></span></extracted-citation>, 658 (2010)("[W]ithout additional reasonable suspicion, the officer must allow the seized person to depart once the purpose of the stop has concluded.").</p>
<p id="p-23">II</p>
<p id="p-24">A seizure for a traffic violation justifies a police investigation of that violation. "[A] relatively brief encounter," a routine traffic stop is "more analogous to a so-called '<em>Terry</em>stop' ... than to a formal arrest." <em>Knowles v. Iowa,</em><extracted-citation case-ids="11076351" index="13" url="https://cite.case.law/us/525/113/#p117"><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">525 U.S. 113</a></span></extracted-citation>, 117, <extracted-citation case-ids="11076359,11076351" index="14" url="https://cite.case.law/s-ct/119/484/"><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">119 S.Ct. 484</a></span></extracted-citation>, <extracted-citation case-ids="11076351" index="15" url="https://cite.case.law/us/525/113/#p117"><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">142 L.Ed.2d 492</a></span></extracted-citation> (1998)(quoting <em>Berkemer v. McCarty,</em><extracted-citation case-ids="11338811" index="16" url="https://cite.case.law/us/468/420/#p439"><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U.S. 420</a></span></extracted-citation>, 439, <extracted-citation case-ids="11338811" index="17" url="https://cite.case.law/us/468/420/#p439"><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">104 S.Ct. 3138</a></span></extracted-citation>, <extracted-citation case-ids="11338811" index="18" url="https://cite.case.law/us/468/420/#p439"><span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">82 L.Ed.2d 317</a></span></extracted-citation> (1984), in turn citing <em>Terry v. Ohio,</em><extracted-citation case-ids="6167798" index="19" url="https://cite.case.law/us/392/1/"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="20" url="https://cite.case.law/us/392/1/"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S.Ct. 1868</a></span></extracted-citation>, <extracted-citation case-ids="6167798" index="21" url="https://cite.case.law/us/392/1/"><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L.Ed.2d 889</a></span></extracted-citation> (1968)). See also <em>Arizona v. Johnson,</em><extracted-citation case-ids="3679137" index="22" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">555 U.S. 323</a></span></extracted-citation>, 330, <extracted-citation case-ids="3679137" index="23" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span></extracted-citation>, <extracted-citation case-ids="3679137" index="24" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">172 L.Ed.2d 694</a></span></extracted-citation> (2009). Like a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></em>stop, the tolerable duration of police inquiries in the traffic-stop context is determined by the seizure's "mission"-to address the traffic violation that warranted the stop, <em>Caballes,</em><extracted-citation case-ids="5902584" index="25" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 407</a></span></extracted-citation>, 125 S.Ct. 834and attend to related safety concerns, <em>infra,</em>at 1619 - 1620. See also <em>United States v. Sharpe,</em><extracted-citation case-ids="11300009" index="26" url="https://cite.case.law/us/470/675/#p685"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">470 U.S. 675</a></span></extracted-citation>, 685, <extracted-citation case-ids="11300009" index="27" url="https://cite.case.law/us/470/675/#p685"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">105 S.Ct. 1568</a></span></extracted-citation>, <extracted-citation case-ids="11300009" index="28" url="https://cite.case.law/us/470/675/#p685"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">84 L.Ed.2d 605</a></span></extracted-citation> (1985); <em>Florida v. Royer,</em><extracted-citation case-ids="6195479" index="29" url="https://cite.case.law/us/460/491/#p500"><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">460 U.S. 491</a></span></extracted-citation>, 500, <extracted-citation case-ids="6195479" index="30" url="https://cite.case.law/us/460/491/#p500"><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">103 S.Ct. 1319</a></span></extracted-citation>, <extracted-citation case-ids="6195479" index="31" url="https://cite.case.law/us/460/491/#p500"><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">75 L.Ed.2d 229</a></span></extracted-citation> (1983)(plurality opinion) ("The scope of the detention must be carefully tailored to its underlying justification."). Because addressing the infraction is the purpose of the stop, it may "last no longer than is necessary to effectuate th[at] purpose." <em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/" aria-description="Citation for case: Florida v. Royer">Ibid.</a></span></em>See also <em>Caballes,</em><extracted-citation case-ids="5902584" index="32" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 407</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="33" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>. Authority for the seizure thus ends when tasks tied to the traffic infraction are-or reasonably should have been-completed. See <em>Sharpe,</em><extracted-citation case-ids="11300009" index="34" url="https://cite.case.law/us/470/675/#p685"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">470 U.S., at 686</a></span></extracted-citation>, <extracted-citation case-ids="11300009" index="35" url="https://cite.case.law/us/470/675/#p685"><span class="citation" data-id="9429956"><a href="/opinion/111378/united-states-v-sharpe/" aria-description="Citation for case: United States v. Sharpe">105 S.Ct. 1568</a></span></extracted-citation>(in determining the reasonable duration of a stop, "it [is] appropriate to examine whether the police diligently pursued [the] investigation").</p>
<p id="p-25">Our decisions in <em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">Caballes</a></span></em>and <em><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">Johnson</a></span></em>heed these constraints. In both cases, we concluded that the Fourth Amendment tolerated certain unrelated investigations that did not lengthen the roadside detention. <em>Johnson,</em><extracted-citation case-ids="3679137" index="36" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">555 U.S., at 327</a></span>-328</extracted-citation>, <extracted-citation case-ids="3679137" index="37" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span></extracted-citation>(questioning);<em>Caballes,</em><extracted-citation case-ids="5902584" index="38" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/#406" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 406</a></span>, 408</extracted-citation>, <extracted-citation case-ids="5902584" index="39" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>(dog sniff). In <em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">Caballes</a></span>,</em>however, we cautioned that a traffic stop "can become unlawful <a class="page-label" data-citation-index="1" data-label="1615" href="#p1615" id="p1615">*1615</a>if it is prolonged beyond the time reasonably required to complete th[e] mission" of issuing a warning ticket. <extracted-citation case-ids="5902584" index="40" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 407</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="41" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>. And we repeated that admonition in <em>Johnson</em>: The seizure remains lawful only "so long as [unrelated] inquiries do not measurably extend the duration of the stop." <extracted-citation case-ids="3679137" index="42" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">555 U.S., at 333</a></span></extracted-citation>, <extracted-citation case-ids="3679137" index="43" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span></extracted-citation>. See also <em>Muehler v. Mena,</em><extracted-citation case-ids="5902037" index="44" url="https://cite.case.law/us/544/93/#p101"><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">544 U.S. 93</a></span></extracted-citation>, 101, <extracted-citation case-ids="5902037" index="45" url="https://cite.case.law/us/544/93/#p101"><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">125 S.Ct. 1465</a></span></extracted-citation>, <extracted-citation case-ids="5902037" index="46" url="https://cite.case.law/us/544/93/#p101"><span class="citation" data-id="9434759"><a href="/opinion/142878/muehler-v-mena/" aria-description="Citation for case: Muehler v. Mena">161 L.Ed.2d 299</a></span></extracted-citation> (2005)(because unrelated inquiries did not "exten[d] the time [petitioner] was detained[,] ... no additional Fourth Amendment justification ... was required"). An officer, in other words, may conduct certain unrelated checks during an otherwise lawful traffic stop. But contrary to Justice ALITO's suggestion, <em>post,</em> at 1625, n. 2, he may not do so in a way that prolongs the stop, absent the reasonable suspicion ordinarily demanded to justify detaining an individual. But see <em>post,</em>at 1623 - 1624 (ALITO, J., dissenting) (premising opinion on the dissent's own finding of "reasonable suspicion," although the District Court reached the opposite conclusion, and the Court of Appeals declined to consider the issue).</p>
<p id="p-26">Beyond determining whether to issue a traffic ticket, an officer's mission includes "ordinary inquiries incident to [the traffic] stop." <em>Caballes,</em><extracted-citation case-ids="5902584" index="47" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 408</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="48" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>. Typically such inquiries involve checking the driver's license, determining whether there are outstanding warrants against the driver, and inspecting the automobile's registration and proof of insurance. See <em>Delaware v. Prouse,</em><extracted-citation case-ids="6187389" index="49" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span></extracted-citation>, 658-660, <extracted-citation case-ids="6187389" index="50" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation>, <extracted-citation case-ids="6187389" index="51" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L.Ed.2d 660</a></span></extracted-citation> (1979). See also 4 W. LaFave, Search and Seizure § 9.3(c), pp. 507-517 (5th ed. 2012). These checks serve the same objective as enforcement of the traffic code: ensuring that vehicles on the road are operated safely and responsibly. See <em>Prouse,</em><extracted-citation case-ids="6187389" index="52" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S., at 658</a></span>-659</extracted-citation>, <extracted-citation case-ids="6187389" index="53" url="https://cite.case.law/us/440/648/#p658"><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S.Ct. 1391</a></span></extracted-citation>; LaFave, Search and Seizure § 9.3(c), at 516(A "warrant check makes it possible to determine whether the apparent traffic violator is wanted for one or more previous traffic offenses.").</p>
<p id="p-27">A dog sniff, by contrast, is a measure aimed at "detect[ing] evidence of ordinary criminal wrongdoing." <em>Indianapolis v. Edmond,</em><extracted-citation case-ids="9505377" index="54" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32</a></span></extracted-citation>, 40-41, <extracted-citation case-ids="9505377" index="55" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S.Ct. 447</a></span></extracted-citation>, <extracted-citation case-ids="9505377" index="56" url="https://cite.case.law/us/531/32/#p40"><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L.Ed.2d 333</a></span></extracted-citation> (2000). See also <em>Florida v. Jardines,</em><extracted-citation case-ids="12696458" index="57" url="https://cite.case.law/us/569/1/"><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">569 U.S. 1</a></span></extracted-citation>, ---- - ----, <extracted-citation case-ids="12696458" index="58" url="https://cite.case.law/us/569/1/"><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">133 S.Ct. 1409</a></span></extracted-citation>, 1416-1417, <extracted-citation case-ids="12696458" index="59" url="https://cite.case.law/us/569/1/"><span class="citation" data-id="856347"><a href="/opinion/856347/florida-v-jardines/" aria-description="Citation for case: Florida v. Jardines">185 L.Ed.2d 495</a></span></extracted-citation> (2013). Candidly, the Government acknowledged at oral argument that a dog sniff, unlike the routine measures just mentioned, is not an ordinary incident of a traffic stop. See Tr. of Oral Arg. 33. Lacking the same close connection to roadway safety as the ordinary inquiries, a dog sniff is not fairly characterized as part of the officer's traffic mission.</p>
<p id="p-28">In advancing its <em>de minimis</em>rule, the Eighth Circuit relied heavily on our decision in <em>Pennsylvania v. Mimms,</em><extracted-citation case-ids="6180104" index="60" url="https://cite.case.law/us/434/106/"><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S. 106</a></span></extracted-citation>, <extracted-citation case-ids="6180104" index="61" url="https://cite.case.law/us/434/106/"><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span></extracted-citation>, <extracted-citation case-ids="6180104" index="62" url="https://cite.case.law/us/434/106/"><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">54 L.Ed.2d 331</a></span></extracted-citation> (1977)(<em>per curiam</em>). See <em>United States v. $404,905.00 in U.S. Currency,</em><extracted-citation case-ids="11546993" index="63" url="https://cite.case.law/f3d/182/643/#p649"><span class="citation" data-id="765041"><a href="/opinion/765041/united-states-of-america-v-40490500-in-us-currency-stephen/" aria-description="Citation for case: United States of America v. $ 404,905.00 in U.S....">182 F.3d 643</a></span></extracted-citation>, 649 (C.A.8 1999). In <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>,</em>we reasoned that the government's "legitimate and weighty" interest in officer safety outweighs the "<em>de minimis</em>" additional intrusion of requiring a driver, already lawfully stopped, to exit the vehicle. <extracted-citation case-ids="6180104" index="64" url="https://cite.case.law/us/434/106/"><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U.S., at 110</a></span>-111</extracted-citation>, <extracted-citation case-ids="6180104" index="65" url="https://cite.case.law/us/434/106/"><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">98 S.Ct. 330</a></span></extracted-citation>. See also <em>Maryland v. Wilson,</em><extracted-citation case-ids="11595747" index="66" url="https://cite.case.law/us/519/408/#p413"><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">519 U.S. 408</a></span></extracted-citation>, 413-415, <extracted-citation case-ids="11595747" index="67" url="https://cite.case.law/us/519/408/#p413"><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">117 S.Ct. 882</a></span></extracted-citation>, <extracted-citation case-ids="11595747" index="68" url="https://cite.case.law/us/519/408/#p413"><span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/" aria-description="Citation for case: Maryland v. Wilson">137 L.Ed.2d 41</a></span></extracted-citation> (1997)(passengers may be required to exit vehicle stopped for traffic violation). The Eighth Circuit, echoed in Justice THOMAS's dissent, believed that the imposition here similarly could be offset by the Government's "strong interest in interdicting the flow of illegal drugs along the nation's highways." <em>$404,905.00 in U.S. Currency,</em><extracted-citation case-ids="11546993" index="69" url="https://cite.case.law/f3d/182/643/#p649"><span class="citation" data-id="765041"><a href="/opinion/765041/united-states-of-america-v-40490500-in-us-currency-stephen/" aria-description="Citation for case: United States of America v. $ 404,905.00 in U.S....">182 F.3d, at 649</a></span></extracted-citation>; see <em>post,</em> at 1621.</p>
<p id="p-29"><a class="page-label" data-citation-index="1" data-label="1616" href="#p1616" id="p1616">*1616</a>Unlike a general interest in criminal enforcement, however, the government's officer safety interest stems from the mission of the stop itself. Traffic stops are "especially fraught with danger to police officers," <em>Johnson,</em><extracted-citation case-ids="3679137" index="70" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">555 U.S., at 330</a></span></extracted-citation>, <extracted-citation case-ids="3679137" index="71" url="https://cite.case.law/us/555/323/#p330"><span class="citation" data-id="145912"><a href="/opinion/145912/arizona-v-johnson/" aria-description="Citation for case: Arizona v. Johnson">129 S.Ct. 781</a></span></extracted-citation>(internal quotation marks omitted), so an officer may need to take certain negligibly burdensome precautions in order to complete his mission safely. Cf. <em>United States v. Holt,</em><extracted-citation case-ids="9486811" index="72" url="https://cite.case.law/f3d/264/1215/#p1221"><span class="citation" data-id="9494344"><a href="/opinion/774866/united-states-v-dennis-dayton-holt/" aria-description="Citation for case: United States v. Dennis Dayton Holt">264 F.3d 1215</a></span></extracted-citation>, 1221-1222 (C.A.10 2001)(en banc) (recognizing officer safety justification for criminal record and outstanding warrant checks), abrogated on other grounds as recognized in <em>United States v. Stewart,</em><extracted-citation case-ids="2540636,2536718" index="73" url="https://cite.case.law/f3d/473/1265/"><span class="citation" data-id="168633"><a href="/opinion/168633/united-states-v-stewart/" aria-description="Citation for case: United States v. Stewart">473 F.3d 1265</a></span></extracted-citation>, 1269 (C.A.10 2007). On-scene investigation into other crimes, however, detours from that mission. See <em>supra,</em>at 1615. So too do safety precautions taken in order to facilitate such detours. But cf. <em>post,</em> at 1624 - 1625 (ALITO, J., dissenting). Thus, even assuming that the imposition here was no more intrusive than the exit order in <em><span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">Mimms</a></span>,</em>the dog sniff could not be justified on the same basis. Highway and officer safety are interests different in kind from the Government's endeavor to detect crime in general or drug trafficking in particular.</p>
<p id="p-30">The Government argues that an officer may "incremental[ly]" prolong a stop to conduct a dog sniff so long as the officer is reasonably diligent in pursuing the traffic-related purpose of the stop, and the overall duration of the stop remains reasonable in relation to the duration of other traffic stops involving similar circumstances. Brief for United States 36-39. The Government's argument, in effect, is that by completing all traffic-related tasks expeditiously, an officer can earn bonus time to pursue an unrelated criminal investigation. See also <em>post,</em> at 1617 - 1619 (THOMAS, J., dissenting) (embracing the Government's argument). The reasonableness of a seizure, however, depends on what the police in fact do. See <em>Knowles,</em><extracted-citation case-ids="11076351" index="74" url="https://cite.case.law/us/525/113/#p117"><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">525 U.S., at 115</a></span>-117</extracted-citation>, <extracted-citation case-ids="11076359,11076351" index="75" url="https://cite.case.law/s-ct/119/484/"><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/" aria-description="Citation for case: Knowles v. Iowa">119 S.Ct. 484</a></span></extracted-citation>. In this regard, the Government acknowledges that "an officer always has to be reasonably diligent." Tr. of Oral Arg. 49. How could diligence be gauged other than by noting what the officer actually did and how he did it? If an officer can complete traffic-based inquiries expeditiously, then that is the amount of "time reasonably required to complete [the stop's] mission." <em>Caballes,</em><extracted-citation case-ids="5902584" index="76" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">543 U.S., at 407</a></span></extracted-citation>, <extracted-citation case-ids="5902584" index="77" url="https://cite.case.law/us/543/405/"><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">125 S.Ct. 834</a></span></extracted-citation>. As we said in <em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">Caballes</a></span></em>and reiterate today, a traffic stop "prolonged beyond" that point is "unlawful." <em><span class="citation" data-id="9434728"><a href="/opinion/137742/illinois-v-caballes/" aria-description="Citation for case: Illinois v. Caballes">Ibid.</a></span></em>The critical question, then, is not whether the dog sniff occurs before or after the officer issues a ticket, as Justice ALITO supposes, <em>post,</em> at 1624 - 1625, but whether conducting the sniff "prolongs"-<em>i.e.,</em> adds time to-"the stop," <em>supra,</em>at 1615.</p>
<p id="p-31">III</p>
<p id="p-32">The Magistrate Judge found that detention for the dog sniff in this case was not independently supported by individualized suspicion, see App. 100, and the District Court adopted the Magistrate Judge's findings, see <em>id</em>., at 112-113. The Court of Appeals, however, did not review that determination. But see <em>post,</em> at 1617, 1622 - 1623 (THOMAS, J., dissenting) (resolving the issue, nevermind that the Court of Appeals left it unaddressed); <em>post,</em> at 1623 - 1624 (ALITO, J., dissenting) (upbraiding the Court for addressing the sole issue decided by the Court of Appeals and characterizing the Court's answer as "unnecessary" because the Court, instead, should have decided an issue the Court of Appeals did not decide). The question whether reasonable suspicion of criminal activity justified detaining Rodriguez beyond completion of the traffic infraction <a class="page-label" data-citation-index="1" data-label="1617" href="#p1617" id="p1617">*1617</a>investigation, therefore, remains open for Eighth Circuit consideration on remand.</p>
<p id="p-33">* * *</p>
<p id="p-34">For the reasons stated, the judgment of the United States Court of Appeals for the Eighth Circuit is vacated, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="p-35"><em>It is so ordered.</em></p>
</opinion>
```

---

## GROUP: content/cases/Schmerber v. California.md  (`case`, 6 assertions)

### content_page

```
---
title: "Schmerber v. California"
type: case
citation: "384 U.S. 757 (1966)"
parallel_cite: "86 S. Ct. 1826; 16 L. Ed. 2d 908"
neutral_cite: 1966 U.S. LEXIS 1129
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1966
date_decided: 1966-06-20
docket: 658
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1966-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Schmerber v. California
  varies_by_point: false
  scope_note: "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107262/schmerber-v-california/"
  cluster_id: 107262
  opinion_id: 107262
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Anchor"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Missouri v. McNeely]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "fifth-amendment", "exigent-circumstances", "blood-draw", "dui", "bodily-intrusion"]
holding: "Compelled blood/BAC evidence is physical, not testimonial, so it does not violate the Fifth Amendment; and a warrantless blood draw on probable cause is reasonable where exigency — dissipating alcohol plus time already lost — leaves no time to obtain a warrant."
lake:
  record_id: Schmerber v. California
  status: verified
  projected_at: 2026-07-09
---

# Schmerber v. California

*384 U.S. 757 (1966)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Schmerber was arrested for driving under the influence at a hospital where he was being treated for injuries from a car accident he had apparently caused. At the direction of the arresting officer and over Schmerber's refusal, a physician drew a blood sample, and its analysis (showing intoxication) was admitted at his trial. He argued the compelled blood draw violated, among other things, his Fifth Amendment privilege against self-incrimination and his Fourth Amendment right against unreasonable searches.

## Issue
Whether the compelled, warrantless withdrawal and chemical analysis of a DUI arrestee's blood violates (1) the Fifth Amendment privilege against self-incrimination, and (2) the Fourth Amendment.

## Rule
**Fifth Amendment** — blood-alcohol evidence is physical, not testimonial: "the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature, and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends." — 384 U.S. at 761. ^pin-761

**Fourth Amendment** — a warrantless blood draw on probable cause is reasonable when [[Exigent Circumstances and Hot Pursuit|exigency]] leaves no time for a warrant. Because alcohol diminishes after drinking stops and time was lost transporting the accused and investigating the scene, "there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest." — [*Id.* at 770–771](https://www.courtlistener.com/opinion/107262/schmerber-v-california/#:~:text=there%20was%20no%20time%20to). ^pin-770

## Application
Schmerber's blood-alcohol level was naturally falling as his body metabolized the alcohol, and the officer — who had probable cause to believe he had been driving while intoxicated — had spent the available time bringing him to the hospital and investigating the accident, leaving no opportunity to obtain a warrant. On those special facts the warrantless extraction of blood was a reasonable response to the threatened loss of evidence, and a blood test performed by a physician in a hospital was a reasonable means of obtaining it.

## Conclusion
Neither the Fifth nor the Fourth Amendment was violated; the conviction was affirmed. *Schmerber* anchors the warrantless-blood-draw/bodily-intrusion line later refined by [[Missouri v. McNeely]] (no [[Common Legal Terms#per-se|per se]] DUI [[Exigent Circumstances and Hot Pursuit|exigency]]) and [[Birchfield v. North Dakota]] (breath, not blood, as a [[Search Incident to Arrest|search incident to arrest]]).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- [[Missouri v. McNeely]] (2013) **clarified** that the natural dissipation of alcohol does **not** create a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]] justifying a warrantless DUI blood draw; [[Exigent Circumstances and Hot Pursuit|exigency]] is judged case-by-case on the totality — consistent with *Schmerber*'s own fact-bound analysis.
- [[Birchfield v. North Dakota]] (2016) held a warrantless **blood** test is **not** justified as a search incident to a DUI arrest (a **breath** test is), so post-*[[Birchfield v. North Dakota|Birchfield]]* a warrantless blood draw rests on [[Exigent Circumstances and Hot Pursuit|exigency]] or another exception, not SITA.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Schmerber v. California*, 384 U.S. 757 (1966) — https://www.courtlistener.com/opinion/107262/schmerber-v-california/ — pinpoints: 761, 770–771.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "844d65099c3209ea", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "384 U.S. 757 (1966)", "court": "U.S. Supreme Court", "neutral_cite": "1966 U.S. LEXIS 1129", "official_citation_present": true, "parallel_cite": "86 S. Ct. 1826; 16 L. Ed. 2d 908", "title": "Schmerber v. California", "year": "1966"}}
{"assertion_id": "431185c0beacfd94", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Key — Anchor", "title": "Schmerber v. California"}}
{"assertion_id": "4d8dd40e179deb48", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Compelled blood/BAC evidence is physical, not testimonial, so it does not violate the Fifth Amendment; and a warrantless blood draw on probable cause is reasonable where exigency — dissipating alcohol plus time already lost — leaves no time to obtain a warrant.", "title": "Schmerber v. California"}}
{"assertion_id": "514490cf06d7ecae", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Alcohol Tests"}, "payload": {"home": "SIA Alcohol Tests", "role": "Related (cross-doctrine)", "title": "Schmerber v. California"}}
{"assertion_id": "1f15f31c5592e65d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Schmerber v. California"}}
{"assertion_id": "87cd7f2f8c7b93a5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1966-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Schmerber v. California", "field_i_validity": "good_law", "scope_note": "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands.", "title": "Schmerber v. California", "varies_by_point": "false"}}
```

### lake record — Schmerber v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Schmerber v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Schmerber v. California",
    "case_name_short": "Schmerber",
    "case_name_full": "Schmerber v. California",
    "input_case_name": "Schmerber v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1966-06-20",
    "year": 1966,
    "docket": "658",
    "cluster_id": 107262,
    "lead_opinion_id": 107262,
    "sibling_ids": [
      107262,
      9423255,
      9423256,
      9423257,
      9423258,
      9423259,
      9423260
    ],
    "absolute_url": "/opinion/107262/schmerber-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "384 U.S. 757",
      "volume": "384",
      "reporter": "U.S.",
      "page": "757",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "86 S. Ct. 1826",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1826",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 908",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "908",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1966 U.S. LEXIS 1129",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "1129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "384 U.S. 757",
        "volume": "384",
        "reporter": "U.S.",
        "page": "757",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 S. Ct. 1826",
        "volume": "86",
        "reporter": "S. Ct.",
        "page": "1826",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 L. Ed. 2d 908",
        "volume": "16",
        "reporter": "L. Ed. 2d",
        "page": "908",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1966 U.S. LEXIS 1129",
        "volume": "1966",
        "reporter": "U.S. LEXIS",
        "page": "1129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "384 U.S. 757",
    "official_selection": {
      "court_class": "scotus",
      "selected": "384 U.S. 757",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-761",
      "page": null,
      "quote": "--- # Schmerber v. California *384 U.S. 757 (1966)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Schmerber was arrested for driving under the influence at a hospital where he was being treated for injuries from a car accident he had apparently caused. At the direction of the arresting officer and over Schmerber's refusal, a physician drew a blood sample, and its analysis (showing intoxication) was admitted at his trial. He argued the compelled blood draw violated, among other things, his Fifth Amendment privilege against self-incrimination and his Fourth Amendment right against unreasonable searches. ## Issue Whether the compelled, warrantless withdrawal and chemical analysis of a DUI arrestee's blood violates (1) the Fifth Amendment privilege against self-incrimination, and (2) the Fourth Amendment. ## Rule **Fifth Amendment** \u2014 blood-alcohol evidence is physical, not testimonial:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-770",
      "page": null,
      "quote": "there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest.",
      "star_marker": "771",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 24817,
      "fragment": "#:~:text=there%20was%20no%20time%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1966-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Schmerber v. California",
    "varies_by_point": false,
    "scope_note": "Foundational warrantless-blood-draw / bodily-intrusion case; good law. Missouri v. McNeely (2013) clarified that the natural dissipation of alcohol is not a per se exigency (exigency is case-by-case), and Birchfield v. North Dakota (2016) held blood tests are not justified as a search incident to arrest (breath tests are). Schmerber's own fact-bound holding stands.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Bell",
          "cluster_id": 10747468,
          "cite": [
            "2025 ND 201"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
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
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gutierrez",
          "cluster_id": 6240355,
          "cite": [
            "245 Cal. Rptr. 3d 143",
            "33 Cal. App. Supp. 5th 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Camara v. Municipal Court of City and County of San Francisco",
          "cluster_id": 107473,
          "cite": [
            "18 L. Ed. 2d 930",
            "87 S. Ct. 1727",
            "387 U.S. 523",
            "1967 U.S. LEXIS 1254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ingraham v. Wright",
          "cluster_id": 109635,
          "cite": [
            "51 L. Ed. 2d 711",
            "97 S. Ct. 1401",
            "430 U.S. 651",
            "1977 U.S. LEXIS 74"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. United States",
          "cluster_id": 109432,
          "cite": [
            "48 L. Ed. 2d 39",
            "96 S. Ct. 1569",
            "425 U.S. 391",
            "1976 U.S. LEXIS 98",
            "37 A.F.T.R.2d (RIA) 1244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Florida",
          "cluster_id": 108186,
          "cite": [
            "26 L. Ed. 2d 446",
            "90 S. Ct. 1893",
            "399 U.S. 78",
            "1970 U.S. LEXIS 98",
            "53 Ohio Op. 2d 55"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Harper",
          "cluster_id": 112381,
          "cite": [
            "108 L. Ed. 2d 178",
            "110 S. Ct. 1028",
            "494 U.S. 210",
            "1990 U.S. LEXIS 1174"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
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
        "journal_ref": "Schmerber v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI4MjQzMjAwMDAwJnM9NDUwNTAzMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTcmcz0xMDg2NTAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
        "reviewed": 51,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 51,
        "triage_read": 3,
        "triage_snippet_classified": 48
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107262 OR 9423255 OR 9423256 OR 9423257 OR 9423258 OR 9423259 OR 9423260)",
    "indexed_citing_opinions": 4034,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107262,
        "count": 3693,
        "count_source": "search"
      },
      {
        "opinion_id": 9423255,
        "count": 457,
        "count_source": "search"
      },
      {
        "opinion_id": 9423256,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423257,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423258,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423259,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423260,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6073,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/schmerber-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjcyMSZzPTEwMzYwOTgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107262+OR+9423255+OR+9423256+OR+9423257+OR+9423258+OR+9423259+OR+9423260%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107262,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 103557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 105456,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 271964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1212162,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1347242,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1421285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1421344,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1440868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1447648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 1923442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107262,
        "cited_id": 3579530,
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
    "date_created": "2026-07-05T18:39:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:41:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:39:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Schmerber v. California

```
<div>
<center><b><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span> (1966)</b></center>
<center><h1>SCHMERBER<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 658.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 25, 1966.</center>
<center>Decided June 20, 1966.</center>
CERTIORARI TO THE APPELLATE DEPARTMENT OF THE SUPERIOR COURT OF CALIFORNIA, COUNTY OF LOS ANGELES.
<p><span class="star-pagination">*758</span> <i>Thomas M. McGurrin</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Edward L. Davenport</i> argued the cause for respondent. On the brief were <i>Roger Arnebergh</i> and <i>Philip E. Grey.</i></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioner was convicted in Los Angeles Municipal Court of the criminal offense of driving an automobile while under the influence of intoxicating liquor.<sup>[1]</sup> He had been arrested at a hospital while receiving treatment for injuries suffered in an accident involving the automobile that he had apparently been driving.<sup>[2]</sup> At the direction of a police officer, a blood sample was then withdrawn from petitioner's body by a physician at the hospital. <span class="star-pagination">*759</span> The chemical analysis of this sample revealed a percent by weight of alcohol in his blood at the time of the offense which indicated intoxication, and the report of this analysis was admitted in evidence at the trial. Petitioner objected to receipt of this evidence of the analysis on the ground that the blood had been withdrawn despite his refusal, on the advice of his counsel, to consent to the test. He contended that in that circumstance the withdrawal of the blood and the admission of the analysis in evidence denied him due process of law under the Fourteenth Amendment, as well as specific guarantees of the Bill of Rights secured against the States by that Amendment: his privilege against self-incrimination under the Fifth Amendment; his right to counsel under the Sixth Amendment; and his right not to be subjected to unreasonable searches and seizures in violation of the Fourth Amendment. The Appellate Department of the California Superior Court rejected these contentions and affirmed the conviction.<sup>[3]</sup> In view of constitutional decisions since we last considered these issues in <i>Breithaupt</i> v. <i>Abram,</i> 352 U. S. 432see <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>; <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span>, and <i>Mapp</i> v. <i>Ohio,</i> 367 U. S. 643we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./382/971/">382 U. S. 971</a></span>. We affirm.</p>
<p></p>
<h2>I.</h2>
<p></p>
<h2>THE DUE PROCESS CLAUSE CLAIM.</h2>
<p><i>Breithaupt</i> was also a case in which police officers caused blood to be withdrawn from the driver of an automobile involved in an accident, and in which there was ample justification for the officer's conclusion that the driver was under the influence of alcohol. There, as here, the extraction was made by a physician in a simple, medically acceptable manner in a hospital environment. <span class="star-pagination">*760</span> There, however, the driver was unconscious at the time the blood was withdrawn and hence had no opportunity to object to the procedure. We affirmed the conviction there resulting from the use of the test in evidence, holding that under such circumstances the withdrawal did not offend "that `sense of justice' of which we spoke in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/" aria-description="Citation for case: Rochin v. California">342 U. S. 165</a></span>." 352 U. S., at 435. <i>Breithaupt</i> thus requires the rejection of petitioner's due process argument, and nothing in the circumstances of this case<sup>[4]</sup> or in supervening events persuades us that this aspect of <i>Breithaupt</i> should be overruled.</p>
<p></p>
<h2>II.</h2>
<p></p>
<h2>THE PRIVILEGE AGAINST SELF-INCRIMINATION CLAIM.</h2>
<p><i>Breithaupt</i> summarily rejected an argument that the withdrawal of blood and the admission of the analysis report involved in that state case violated the Fifth Amendment privilege of any person not to "be compelled in any criminal case to be a witness against himself," citing <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>. But that case, holding that the protections of the Fourteenth Amendment do not embrace this Fifth Amendment privilege, has been succeeded by <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span>. We there held that "[t]he Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, <span class="star-pagination">*761</span> and to suffer no penalty . . . for such silence." We therefore must now decide whether the withdrawal of the blood and admission in evidence of the analysis involved in this case violated petitioner's privilege. We hold that the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature,<sup>[5]</sup> and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends.</p>
<p>It could not be denied that in requiring petitioner to submit to the withdrawal and chemical analysis of his blood the State compelled him to submit to an attempt to discover evidence that might be used to prosecute him for a criminal offense. He submitted only after the police officer rejected his objection and directed the physician to proceed. The officer's direction to the physician to administer the test over petitioner's objection constituted compulsion for the purposes of the privilege. The critical question, then is whether petitioner was thus compelled "to be a witness against himself."<sup>[6]</sup></p>
<p><span class="star-pagination">*762</span> If the scope of the privilege coincided with the complex of values it helps to protect, we might be obliged to conclude that the privilege was violated. In <i>Miranda</i> v. <i>Arizona, ante,</i> at 460, the Court said of the interests protected by the privilege: "All these policies point to one overriding thought: the constitutional foundation underlying the privilege is the respect a governmentstate or federal must accord to the dignity and integrity of its citizens. To maintain a `fair state-individual balance,' to require the government `to shoulder the entire load' . . . to respect the inviolability of the human personality, our accusatory system of criminal justice demands that the government seeking to punish an individual produce the evidence against him by its own independent labors, rather than by the cruel, simple expedient of compelling it from his own mouth." The withdrawal of blood necessarily involves puncturing the skin for extraction, and the percent by weight of alcohol in that blood, as established by chemical analysis, is evidence of criminal guilt. Compelled submission fails on one view to respect the "inviolability of the human personality." Moreover, since it enables the State to rely on evidence forced from the accused, the compulsion violates at least one meaning of the requirement that the State procure the evidence against an accused "by its own independent labors."</p>
<p>As the passage in <i>Miranda</i> implicitly recognizes, however, the privilege has never been given the full scope which the values it helps to protect suggest. History <span class="star-pagination">*763</span> and a long line of authorities in lower courts have consistently limited its protection to situations in which the State seeks to submerge those values by obtaining the evidence against an accused through "the cruel, simple expedient of compelling it from his own mouth. . . . In sum, the privilege is fulfilled only when the person is guaranteed the right `to remain silent unless he chooses to speak in the unfettered exercise of his own will.' " <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Ibid.</a></span></i> The leading case in this Court is <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>. There the question was whether evidence was admissible that the accused, prior to trial and over his protest, put on a blouse that fitted him. It was contended that compelling the accused to submit to the demand that he model the blouse violated the privilege. Mr. Justice Holmes, speaking for the Court, rejected the argument as "based upon an extravagant extension of the Fifth Amendment," and went on to say: "[T]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material. The objection in principle would forbid a jury to look at a prisoner and compare his features with a photograph in proof." <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S., at 252-253</a></span>.<sup>[7]</sup></p>
<p>It is clear that the protection of the privilege reaches an accused's communications, whatever form they might <span class="star-pagination">*764</span> take, and the compulsion of responses which are also communications, for example, compliance with a subpoena to produce one's papers. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>. On the other hand, both federal and state courts have usually held that it offers no protection against compulsion to submit to fingerprinting, photographing, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture.<sup>[8]</sup> The distinction which has emerged, often expressed in different ways, is that the privilege is a bar against compelling "communications" or "testimony," but that compulsion which makes a suspect or accused the source of "real or physical evidence" does not violate it.</p>
<p>Although we agree that this distinction is a helpful framework for analysis, we are not to be understood to agree with past applications in all instances. There will be many cases in which such a distinction is not readily drawn. Some tests seemingly directed to obtain "physical evidence," for example, lie detector tests measuring changes in body function during interrogation, may actually be directed to eliciting responses which are essentially testimonial. To compel a person to submit to testing in which an effort will be made to determine his guilt or innocence on the basis of physiological responses, whether willed or not, is to evoke the spirit and history of the Fifth Amendment. Such situations call to mind the principle that the protection of the privilege "is as broad as the mischief against which it seeks to guard," <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span>.</p>
<p><span class="star-pagination">*765</span> In the present case, however, no such problem of application is presented. Not even a shadow of testimonial compulsion upon or enforced communication by the accused was involved either in the extraction or in the chemical analysis. Petitioner's testimonial capacities were in no way implicated; indeed, his participation, except as a donor, was irrelevant to the results of the test, which depend on chemical analysis and on that alone.<sup>[9]</sup> Since the blood test evidence, although an incriminating product of compulsion, was neither petitioner's testimony nor evidence relating to some communicative act or writing by the petitioner, it was not inadmissible on privilege grounds.</p>
<p></p>
<h2>III.</h2>
<p></p>
<h2>THE RIGHT TO COUNSEL CLAIM.</h2>
<p>This conclusion also answers petitioner's claim that, in compelling him to submit to the test in face of the fact that his objection was made on the advice of counsel, <span class="star-pagination">*766</span> he was denied his Sixth Amendment right to the assistance of counsel. Since petitioner was not entitled to assert the privilege, he has no greater right because counsel erroneously advised him that he could assert it. His claim is strictly limited to the failure of the police to respect his wish, reinforced by counsel's advice, to be left inviolate. No issue of counsel's ability to assist petitioner in respect of any rights he did possess is presented. The limited claim thus made must be rejected.</p>
<p></p>
<h2>IV.</h2>
<p></p>
<h2>THE SEARCH AND SEIZURE CLAIM.</h2>
<p>In <i>Breithaupt,</i> as here, it was also contended that the chemical analysis should be excluded from evidence as the product of an unlawful search and seizure in violation of the Fourth and Fourteenth Amendments. The Court did not decide whether the extraction of blood in that case was unlawful, but rejected the claim on the basis of <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>. That case had held that the Constitution did not require, in state prosecutions for state crimes, the exclusion of evidence obtained in violation of the Fourth Amendment's provisions. We have since overruled <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> in that respect, holding in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, that the exclusionary rule adopted for federal prosecutions in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, must also be applied in criminal prosecutions in state courts. The question is squarely presented therefore, whether the chemical analysis <span class="star-pagination">*767</span> introduced in evidence in this case should have been excluded as the product of an unconstitutional search and seizure.</p>
<p>The overriding function of the Fourth Amendment is to protect personal privacy and dignity against unwarranted intrusion by the State. In <i><span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">Wolf</a></span></i> we recognized "[t]he security of one's privacy against arbitrary intrusion by the police" as being "at the core of the Fourth Amendment" and "basic to a free society." <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 27</a></span>. We reaffirmed that broad view of the Amendment's purpose in applying the federal exclusionary rule to the States in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i></p>
<p>The values protected by the Fourth Amendment thus substantially overlap those the Fifth Amendment helps to protect. History and precedent have required that we today reject the claim that the Self-Incrimination Clause of the Fifth Amendment requires the human body in all circumstances to be held inviolate against state expeditions seeking evidence of crime. But if compulsory administration of a blood test does not implicate the Fifth Amendment, it plainly involves the broadly conceived reach of a search and seizure under the Fourth Amendment. That Amendment expressly provides that "[t]he right of the people to be secure in their <i>persons,</i> houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . . ." (Emphasis added.) It could not reasonably be argued, and indeed respondent does not argue, that the administration of the blood test in this case was free of the constraints of the Fourth Amendment. Such testing procedures plainly constitute searches of "persons," and depend antecedently upon seizures of "persons," within the meaning of that Amendment.</p>
<p>Because we are dealing with intrusions into the human body rather than with state interferences with property relationships or private papers"houses, papers, and <span class="star-pagination">*768</span> effects"we write on a clean slate. Limitations on the kinds of property which may be seized under warrant,<sup>[10]</sup> as distinct from the procedures for search and the permissible scope of search,<sup>[11]</sup> are not instructive in this context. We begin with the assumption that once the privilege against self-incrimination has been found not to bar compelled intrusions into the body for blood to be analyzed for alcohol content, the Fourth Amendment's proper function is to constrain, not against all intrusions as such, but against intrusions which are not justified in the circumstances, or which are made in an improper manner. In other words, the questions we must decide in this case are whether the police were justified in requiring petitioner to submit to the blood test, and whether the means and procedures employed in taking his blood respected relevant Fourth Amendment standards of reasonableness.</p>
<p>In this case, as will often be true when charges of driving under the influence of alcohol are pressed, these questions arise in the context of an arrest made by an officer without a warrant. Here, there was plainly probable cause for the officer to arrest petitioner and charge him with driving an automobile while under the influence of intoxicating liquor.<sup>[12]</sup> The police officer who arrived <span class="star-pagination">*769</span> at the scene shortly after the accident smelled liquor on petitioner's breath, and testified that petitioner's eyes were "bloodshot, watery, sort of a glassy appearance." The officer saw petitioner again at the hospital, within two hours of the accident. There he noticed similar symptoms of drunkenness. He thereupon informed petitioner "that he was under arrest and that he was entitled to the services of an attorney, and that he could remain silent, and that anything that he told me would be used against him in evidence."</p>
<p>While early cases suggest that there is an unrestricted "right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime," <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <i>People</i> v. <i>Chiagles,</i> <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">237 N. Y. 193</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/" aria-description="Citation for case: People v. . Chiagles">142 N. E. 583</a></span> (1923) (Cardozo, J.), the mere fact of a lawful arrest does not end our inquiry. The suggestion of these cases apparently rests on two factorsfirst, there may be more immediate danger of concealed weapons or of destruction of evidence under the direct control of the accused, <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#72" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 72-73</a></span> (Frankfurter, J., dissenting); second, once a search of the arrested person for weapons is permitted, it would be both impractical and unnecessary to enforcement of the Fourth Amendment's purpose to attempt to confine the search to those objects alone. <i>People</i> v. <i>Chiagles,</i> <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#197" aria-description="Citation for case: People v. . Chiagles">237 N. Y., at 197-198</a></span>, <span class="citation" data-id="3579530"><a href="/opinion/3598271/people-v-chiagles/#584" aria-description="Citation for case: People v. . Chiagles">142 N. E., at 584</a></span>. Whatever the validity of these considerations in general, they have little applicability with respect to searches involving intrusions beyond the body's surface. The interests in <span class="star-pagination">*770</span> human dignity and privacy which the Fourth Amendment protects forbid any such intrusions on the mere chance that desired evidence might be obtained. In the absence of a clear indication that in fact such evidence will be found, these fundamental human interests require law officers to suffer the risk that such evidence may disappear unless there is an immediate search.</p>
<p>Although the facts which established probable cause to arrest in this case also suggested the required relevance and likely success of a test of petitioner's blood for alcohol, the question remains whether the arresting officer was permitted to draw these inferences himself, or was required instead to procure a warrant before proceeding with the test. Search warrants are ordinarily required for searches of dwellings, and, absent an emergency, no less could be required where intrusions into the human body are concerned. The requirement that a warrant be obtained is a requirement that the inferences to support the search "be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span>; see also <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 110-111</a></span>. The importance of informed, detached and deliberate determinations of the issue whether or not to invade another's body in search of evidence of guilt is indisputable and great.</p>
<p>The officer in the present case, however, might reasonably have believed that he was confronted with an emergency, in which the delay necessary to obtain a warrant, under the circumstances, threatened "the destruction of evidence," <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span>. We are told that the percentage of alcohol in the blood begins to diminish shortly after drinking stops, as the body functions to eliminate it from the system. Particularly in a case such as this, where time had <span class="star-pagination">*771</span> to be taken to bring the accused to a hospital and to investigate the scene of the accident, there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case was an appropriate incident to petitioner's arrest.</p>
<p>Similarly, we are satisfied that the test chosen to measure petitioner's blood-alcohol level was a reasonable one. Extraction of blood samples for testing is a highly effective means of determining the degree to which a person is under the influence of alcohol. See <i>Breithaupt</i> v. <i>Abram,</i> 352 U. S., at 436, n. 3. Such tests are a commonplace in these days of periodic physical examinations<sup>[13]</sup> and experience with them teaches that the quantity of blood extracted is minimal, and that for most people the procedure involves virtually no risk, trauma, or pain. Petitioner is not one of the few who on grounds of fear, concern for health, or religious scruple might prefer some other means of testing, such as the "breathalyzer" test petitioner refused, see n. 9, <i>supra.</i> We need not decide whether such wishes would have to be respected.<sup>[14]</sup></p>
<p>Finally, the record shows that the test was performed in a reasonable manner. Petitioner's blood was taken by a physician in a hospital environment according to accepted medical practices. We are thus not presented with the serious questions which would arise if a search involving use of a medical technique, even of the most <span class="star-pagination">*772</span> rudimentary sort, were made by other than medical personnel or in other than a medical environmentfor example, if it were administered by police in the privacy of the stationhouse. To tolerate searches under these conditions might be to invite an unjustified element of personal risk of infection and pain.</p>
<p>We thus conclude that the present record shows no violation of petitioner's right under the Fourth and Fourteenth Amendments to be free of unreasonable searches and seizures. It bears repeating, however, that we reach this judgment only on the facts of the present record. The integrity of an individual's person is a cherished value of our society. That we today hold that the Constitution does not forbid the States minor intrusions into an individual's body under stringently limited conditions in no way indicates that it permits more substantial intrusions, or intrusions under other conditions.</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE STEWART joins, concurring.</p>
<p>In joining the Court's opinion I desire to add the following comment. While agreeing with the Court that the taking of this blood test involved no testimonial compulsion, I would go further and hold that apart from this consideration the case in no way implicates the Fifth Amendment. Cf. my dissenting opinion and that of MR. JUSTICE WHITE in <i>Miranda</i> v. <i>Arizona, ante,</i> pp. 504, 526.</p>
<p>MR. CHIEF JUSTICE WARREN, dissenting.</p>
<p>While there are other important constitutional issues in this case, I believe it is sufficient for me to reiterate my dissenting opinion in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>, as the basis on which to reverse this conviction.</p>
<p><span class="star-pagination">*773</span> MR. JUSTICE BLACK with whom MR. JUSTICE DOUGLAS joins, dissenting.</p>
<p>I would reverse petitioner's conviction. I agree with the Court that the Fourteenth Amendment made applicable to the States the Fifth Amendment's provision that "No person . . . shall be compelled in any criminal case to be a witness against himself . . . ." But I disagree with the Court's holding that California did not violate petitioner's constitutional right against self-incrimination when it compelled him, against his will, to allow a doctor to puncture his blood vessels in order to extract a sample of blood and analyze it for alcoholic content, and then used that analysis as evidence to convict petitioner of a crime.</p>
<p>The Court admits that "the State compelled [petitioner] to submit to an attempt to discover evidence [in his blood] that might be [and was] used to prosecute him for a criminal offense." To reach the conclusion that compelling a person to give his blood to help the State convict him is not equivalent to compelling him to be a witness against himself strikes me as quite an extraordinary feat. The Court, however, overcomes what had seemed to me to be an insuperable obstacle to its conclusion by holding that</p>
<blockquote>". . . the privilege protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature, and that the withdrawal of blood and use of the analysis in question in this case did not involve compulsion to these ends." (Footnote omitted.)</blockquote>
<p>I cannot agree that this distinction and reasoning of the Court justify denying petitioner his Bill of Rights' guarantee that he must not be compelled to be a witness against himself.</p>
<p><span class="star-pagination">*774</span> In the first place it seems to me that the compulsory extraction of petitioner's blood for analysis so that the person who analyzed it could give evidence to convict him had both a "testimonial" and a "communicative nature." The sole purpose of this project which proved to be successful was to obtain "testimony" from some person to prove that petitioner had alcohol in his blood at the time he was arrested. And the purpose of the project was certainly "communicative" in that the analysis of the blood was to supply information to enable a witness to communicate to the court and jury that petitioner was more or less drunk.</p>
<p>I think it unfortunate that the Court rests so heavily for its very restrictive reading of the Fifth Amendment's privilege against self-incrimination on the words "testimonial" and "communicative." These words are not models of clarity and precision as the Court's rather labored explication shows. Nor can the Court, so far as I know, find precedent in the former opinions of this Court for using these particular words to limit the scope of the Fifth Amendment's protection. There is a scholarly precedent, however, in the late Professor Wigmore's learned treatise on evidence. He used "testimonial" which, according to the latest edition of his treatise revised by McNaughton, means "communicative" (8 Wigmore, Evidence § 2263 (McNaughton rev. 1961), p. 378), as a key word in his vigorous and extensive campaign designed to keep the privilege against self-incrimination "within limits the strictest possible." 8 Wigmore, Evidence § 2251 (3d ed. 1940), p. 318. Though my admiration for Professor Wigmore's scholarship is great, I regret to see the word he used to narrow the Fifth Amendment's protection play such a major part in any of this Court's opinions.</p>
<p>I am happy that the Court itself refuses to follow Professor Wigmore's implication that the Fifth Amendment <span class="star-pagination">*775</span> goes no further than to bar the use of forced self-incrimination statements coming from a "person's own lips." It concedes, as it must so long as <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, stands, that the Fifth Amendment bars a State from compelling a person to produce papers he has that might tend to incriminate him. It is a strange hierarchy of values that allows the State to extract a human being's blood to convict him of a crime because of the blood's content but proscribes compelled production of his lifeless papers. Certainly there could be few papers that would have any more "testimonial" value to convict a man of drunken driving than would an analysis of the alcoholic content of a human being's blood introduced in evidence at a trial for driving while under the influence of alcohol. In such a situation blood, of course, is not oral testimony given by an accused but it can certainly "communicate" to a court and jury the fact of guilt.</p>
<p>The Court itself, at page 764, expresses its own doubts, if not fears, of its own shadowy distinction between compelling "physical evidence" like blood which it holds does not amount to compelled self-incrimination, and "eliciting responses which are essentially testimonial." And in explanation of its fears the Court goes on to warn that</p>
<blockquote>"To compel a person to submit to testing [by lie detectors for example] in which an effort will be made to determine his guilt or innocence on the basis of physiological responses, whether willed or not, is to evoke the spirit and history of the Fifth Amendment. Such situations call to mind the principle that the protection of the privilege `is as broad as the mischief against which it seeks to guard.' <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#562" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 562</a></span>."</blockquote>
<p>A basic error in the Court's holding and opinion is its failure to give the Fifth Amendment's protection against <span class="star-pagination">*776</span> compulsory self-incrimination the broad and liberal construction that <i><span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">Counselman</a></span></i> and other opinions of this Court have declared it ought to have.</p>
<p>The liberal construction given the Bill of Rights' guarantee in <i>Boyd</i> v. <i>United States, supra</i><i>,</i> which Professor Wigmore criticized severely, see 8 Wigmore, Evidence, § 2264 (3d ed. 1940), pp. 366-373, makes that one among the greatest constitutional decisions of this Court. In that case, at 634-635, all the members of the Court decided that civil suits for penalties and forfeitures incurred for commission of offenses against the law,</p>
<blockquote>". . . are within the reason of criminal proceedings for all the purpose of . . . that portion of the Fifth Amendment which declares that no person shall be compelled in any criminal case to be a witness against himself; . . . within the meaning of the Fifth Amendment to the Constitution . . . ."<sup>[*]</sup></blockquote>
<p>Obviously the Court's interpretation was not completely supported by the literal language of the Fifth Amendment. Recognizing this, the Court announced a rule of constitutional interpretation that has been generally followed ever since, particularly in judicial construction of Bill of Rights guarantees:</p>
<blockquote>"A close and literal construction [of constitutional provisions for the security of persons and property] deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments <span class="star-pagination">*777</span> thereon." <i>Boyd</i> v. <i>United States, supra,</i> at 635.</blockquote>
<p>The Court went on to say, at 637, that to require "an owner to produce his private books and papers, in order to prove his breach of the laws, and thus to establish the forfeiture of his property, is surely compelling him to furnish evidence against himself." The Court today departs from the teachings of <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span>.</i> Petitioner Schmerber has undoubtedly been compelled to give his blood "to furnish evidence against himself," yet the Court holds that this is not forbidden by the Fifth Amendment. With all deference I must say that the Court here gives the Bill of Rights' safeguard against compulsory self-incrimination a construction that would generally be considered too narrow and technical even in the interpretation of an ordinary commercial contract.</p>
<p>The Court apparently, for a reason I cannot understand, finds some comfort for its narrow construction of the Fifth Amendment in this Court's decision in <i>Miranda</i> v. <i>Arizona, ante,</i> p. 436. I find nothing whatever in the majority opinion in that case which either directly or indirectly supports the holding in this case. In fact I think the interpretive constitutional philosophy used in <i>Miranda,</i> unlike that used in this case, gives the Fifth Amendment's prohibition against compelled self-incrimination a broad and liberal construction in line with the wholesome admonitions in the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> case. The closing sentence in the Fifth Amendment section of the Court's opinion in the present case is enough by itself, I think, to expose the unsoundness of what the Court here holds. That sentence reads:</p>
<blockquote>"Since the blood test evidence, although an incriminating product of compulsion, was neither petitioner's testimony nor evidence relating to some communicative act or writing by the petitioner, it was not inadmissible on privilege grounds."</blockquote>
<p><span class="star-pagination">*778</span> How can it reasonably be doubted that the blood test evidence was not in all respects the actual equivalent of "testimony" taken from petitioner when the result of the test was offered as testimony, was considered by the jury as testimony, and the jury's verdict of guilt rests in part on that testimony? The refined, subtle reasoning and balancing process used here to narrow the scope of the Bill of Rights' safeguard against self-incrimination provides a handy instrument for further narrowing of that constitutional protection, as well as others, in the future. Believing with the Framers that these constitutional safeguards broadly construed by independent tribunals of justice provide our best hope for keeping our people free from governmental oppression, I deeply regret the Court's holding. For the foregoing reasons as well as those set out in concurring opinions of BLACK and DOUGLAS, JJ., in <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#174" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 174, 177</a></span>, and my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span>, and the dissenting opinions in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440, 442</a></span>, I dissent from the Court's holding and opinion in this case.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I adhere to the views of THE CHIEF JUSTICE in his dissent in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>, and to the views I stated in my dissent in that case (<span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#442" aria-description="Citation for case: Breithaupt v. Abram"><i>id.,</i> 442</a></span>) and add only a word.</p>
<p>We are dealing with the right of privacy which, since the <i><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">Breithaupt</a></span></i> case, we have held to be within the penumbra of some specific guarantees of the Bill of Rights. <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span>. Thus, the Fifth Amendment marks "a zone of privacy" which the Government may not force a person to surrender. <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/#484" aria-description="Citation for case: Griswold v. Connecticut"><i>Id.,</i> 484</a></span>. Likewise the Fourth Amendment recognizes that right when it guarantees the right of the people to be <span class="star-pagination">*779</span> secure "in their persons." <i><span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">Ibid.</a></span></i> No clearer invasion of this right of privacy can be imagined than forcible bloodletting of the kind involved here.</p>
<p>MR. JUSTICE FORTAS, dissenting.</p>
<p>I would reverse. In my view, petitioner's privilege against self-incrimination applies. I would add that, under the Due Process Clause, the State, in its role as prosecutor, has no right to extract blood from an accused or anyone else, over his protest. As prosecutor, the State has no right to commit any kind of violence upon the person, or to utilize the results of such a tort, and the extraction of blood, over protest, is an act of violence. Cf. CHIEF JUSTICE WARREN'S dissenting opinion in <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#440" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 440</a></span>.</p>
<h2>NOTES</h2>
<p>[1]  California Vehicle Code § 23102 (a) provides, in pertinent part, "It is unlawful for any person who is under the influence of intoxicating liquor . . . to drive a vehicle upon any highway. . . ." The offense is a misdemeanor.</p>
<p>[2]  Petitioner and a companion had been drinking at a tavern and bowling alley. There was evidence showing that petitioner was driving from the bowling alley about midnight November 12, 1964, when the car skidded, crossed the road and struck a tree. Both petitioner and his companion were injured and taken to a hospital for treatment.</p>
<p>[3]  This was the judgment of the highest court of the State in this proceeding since certification to the California District Court of Appeal was denied. See <i>Edwards</i> v. <i>California,</i> <span class="citation" data-id="9419178"><a href="/opinion/103557/edwards-v-california/" aria-description="Citation for case: Edwards v. California">314 U. S. 160</a></span>.</p>
<p>[4]  We "cannot see that it should make any difference whether one states unequivocally that he objects or resorts to physical violence in protest or is in such condition that he is unable to protest." <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#441" aria-description="Citation for case: Breithaupt v. Abram">352 U. S., at 441</a></span> (WARREN, C. J., dissenting). It would be a different case if the police initiated the violence, refused to respect a reasonable request to undergo a different form of testing, or responded to resistance with inappropriate force. Compare the discussion at Part IV, <i>infra.</i></p>
<p>[5]  A dissent suggests that the report of the blood test was "testimonial" or "communicative," because the test was performed in order to obtain the testimony of others, communicating to the jury facts about petitioner's condition. Of course, all evidence received in court is "testimonial" or "communicative" if these words are thus used. But the Fifth Amendment relates only to acts on the part of the person to whom the privilege applies, and we use these words subject to the same limitations. A nod or head-shake is as much a "testimonial" or "communicative" act in this sense as are spoken words. But the terms as we use them do not apply to evidence of acts noncommunicative in nature as to the person asserting the privilege, even though, as here, such acts are compelled to obtain the testimony of others.</p>
<p>[6]  Many state constitutions, including those of most of the original Colonies, phrase the privilege in terms of compelling a person to give "evidence" against himself. But our decision cannot turn on the Fifth Amendment's use of the word "witness." "[A]s the manifest purpose of the constitutional provisions, both of the States and of the United States, is to prohibit the compelling of testimony of a self-incriminating kind from a party or a witness, the liberal construction which must be placed upon constitutional provisions for the protection of personal rights would seem to require that the constitutional guaranties, however differently worded, should have as far as possible the same interpretation . . . ." <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#584" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547, 584-585</a></span>. 8 Wigmore, Evidence § 2252 (McNaughton rev. 1961).</p>
<p>[7]  Compare Wigmore's view, "that the privilege is limited to testimonial disclosures. It was directed at the employment of legal process to <i>extract from the person's own lips</i> an admission of guilt, which would thus take the place of other evidence." 8 Wigmore, Evidence § 2263 (McNaughton rev. 1961). California adopted the Wigmore formulation in <i>People</i> v. <i>Trujillo,</i> <span class="citation" data-id="9630742"><a href="/opinion/1440868/people-v-trujillo/" aria-description="Citation for case: People v. Trujillo">32 Cal. 2d 105</a></span>, <span class="citation" data-id="9630742"><a href="/opinion/1440868/people-v-trujillo/" aria-description="Citation for case: People v. Trujillo">194 P. 2d 681</a></span> (1948); with specific regard to blood tests, see <i>People</i> v. <i>Haeussler,</i> <span class="citation" data-id="9632176"><a href="/opinion/1447648/people-v-haeussler/" aria-description="Citation for case: People v. Haeussler">41 Cal. 2d 252</a></span>, <span class="citation" data-id="9632176"><a href="/opinion/1447648/people-v-haeussler/" aria-description="Citation for case: People v. Haeussler">260 P. 2d 8</a></span> (1953); <i>People</i> v. <i>Duroncelay,</i> <span class="citation" data-id="9563990"><a href="/opinion/1212162/people-v-duroncelay/" aria-description="Citation for case: People v. Duroncelay">48 Cal. 2d 766</a></span>, <span class="citation" data-id="9563990"><a href="/opinion/1212162/people-v-duroncelay/" aria-description="Citation for case: People v. Duroncelay">312 P. 2d 690</a></span> (1957). Our holding today, however, is not to be understood as adopting the Wigmore formulation.</p>
<p>[8]  The cases are collected in 8 Wigmore, Evidence § 2265 (McNaughton rev. 1961). See also <i>United States</i> v. <i>Chibbaro,</i> <span class="citation" data-id="8875889"><a href="/opinion/8889735/united-states-v-chibbaro/" aria-description="Citation for case: United States v. Chibbaro">361 F. 2d 365</a></span> (C. A. 3d Cir. 1966); <i>People</i> v. <i>Graves,</i> <span class="citation" data-id="9592244"><a href="/opinion/1347242/people-v-graves/" aria-description="Citation for case: People v. Graves">64 Cal. 2d 208</a></span>, , <span class="citation" data-id="9592244"><a href="/opinion/1347242/people-v-graves/#116" aria-description="Citation for case: People v. Graves">411 P. 2d 114, 116</a></span> (1966); Weintraub, Voice Identification, Writing Exemplars and the Privilege Against Self-Incrimination, <span class="citation no-link">10 Vand. L. Rev. 485</span> (1957).</p>
<p>[9]  This conclusion would not necessarily govern had the State tried to show that the accused had incriminated himself when told that he would have to be tested. Such incriminating evidence may be an unavoidable by-product of the compulsion to take the test, especially for an individual who fears the extraction or opposes it on religious grounds. If it wishes to compel persons to submit to such attempts to discover evidence, the State may have to forgo the advantage of any <i>testimonial</i> products of administering the testproducts which would fall within the privilege. Indeed, there may be circumstances in which the pain, danger, or severity of an operation would almost inevitably cause a person to prefer confession to undergoing the "search," and nothing we say today should be taken as establishing the permissibility of compulsion in that case. But no such situation is presented in this case. See text at n. 13 <i>infra.</i>
</p>
<p>Petitioner has raised a similar issue in this case, in connection with a police request that he submit to a "breathalyzer" test of air expelled from his lungs for alcohol content. He refused the request, and evidence of his refusal was admitted in evidence without objection.</p>
<p>He argues that the introduction of this evidence and a comment by the prosecutor in closing argument upon his refusal is ground for reversal under <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span>. We think general Fifth Amendment principles, rather than the particular holding of <i><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span>,</i> would be applicable in these circumstances, see <i>Miranda</i> v. <i>Arizona, ante,</i> at 468, n. 37. Since trial here was conducted after our decision in <i>Malloy</i> v. <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Hogan, supra</a></span></i><i>,</i> making those principles applicable to the States, we think petitioner's contention is foreclosed by his failure to object on this ground to the prosecutor's question and statements.</p>
<p>[10]  See, <i>e. g., </i><i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>; contra, <i>People</i> v. <i>Thayer,</i> <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">63 Cal. 2d 635</a></span>, <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">408 P. 2d 108</a></span> (1965); <i>State</i> v. <i>Bisaccia,</i> 45 N. J. 504, <span class="citation" data-id="1923442"><a href="/opinion/1923442/state-v-bisaccia/" aria-description="Citation for case: State v. Bisaccia">213 A. 2d 185</a></span> (1965); Note, Evidentiary Searches: The Rule and the Reason, 54 Geo. L. J. 593 (1966).</p>
<p>[11]  See, <i>e. g., </i><i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span>; <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#235" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 235</a></span>; <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>.</p>
<p>[12]  California law authorizes a peace officer to arrest "without a warrant . . . [w]henever he has reasonable cause to believe that the person to be arrested has committed a felony, whether or not a felony has in fact been committed." <span class="citation no-link">Cal. Penal Code § 836.3</span>. Although petitioner was ultimately prosecuted for a misdemeanor, he was subject to prosecution for the felony since a companion in his car was injured in the accident, which apparently was the result of traffic law violations. <span class="citation no-link">Cal. Vehicle Code § 23101</span>. California's test of probable cause follows the federal standard. <i>People</i> v. <i>Cockrell,</i> <span class="citation" data-id="1421344"><a href="/opinion/1421344/people-v-cockrell/" aria-description="Citation for case: People v. Cockrell">63 Cal. 2d 659</a></span>, <span class="citation" data-id="1421344"><a href="/opinion/1421344/people-v-cockrell/" aria-description="Citation for case: People v. Cockrell">408 P. 2d 116</a></span> (1965).</p>
<p>[13]  "The blood test procedure has become routine in our everyday life. It is a ritual for those going into the military service as well as those applying for marriage licenses. Many colleges require such tests before permitting entrance and literally millions of us have voluntarily gone through the same, though a longer, routine in becoming blood donors." <i>Breithaupt</i> v. <i>Abram,</i> <span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#436" aria-description="Citation for case: Breithaupt v. Abram">352 U. S., at 436</a></span>.</p>
<p>[14]  See Karst, Legislative Facts in Constitutional Litigation, <span class="citation no-link">1960 Sup. Ct. Rev. 75</span>, 82-83.</p>
<p>[*]  A majority of the Court applied the same constitutional interpretation to the search and seizure provisions of the Fourth Amendment over the dissent of Mr. Justice Miller, concurred in by Chief Justice Waite.</p>

</div>
```

---

## GROUP: content/cases/Schneckloth v. Bustamonte.md  (`case`, 5 assertions)

### content_page

```
---
title: "Schneckloth v. Bustamonte"
type: case
citation: "412 U.S. 218 (1973)"
parallel_cite: "93 S. Ct. 2041; 36 L. Ed. 2d 854"
neutral_cite: 1973 U.S. LEXIS 6
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-05-29
docket: 71-732
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Schneckloth v. Bustamonte
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108800/schneckloth-v-bustamonte/"
  cluster_id: 108800
  opinion_id: 108800
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Florida v. Bostick]]", "[[United States v. Drayton]]", "[[Georgia v. Randolph]]", "[[Florida v. Jimeno]]", "[[Illinois v. Rodriguez]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent-searches", "voluntariness", "totality-of-circumstances"]
holding: "The voluntariness of consent to search is a question of fact determined from the TOTALITY OF ALL THE CIRCUMSTANCES; the government need…"
lake:
  record_id: Schneckloth v. Bustamonte
  status: verified
  projected_at: 2026-07-06
---

# Schneckloth v. Bustamonte

*412 U.S. 218 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A police officer stopped a car for burned-out lights. When the driver could not produce a license, the officer asked a passenger — Joe Alcala, brother of the car's owner — for permission to search the car. Alcala said "Sure, go ahead," and helped open the trunk, where stolen checks were found. Bustamonte, another occupant, was convicted; he argued the consent was invalid because no one had been told of a right to refuse.

## Issue
Whether, to establish that consent to a search was voluntary, the State must prove that the person consenting knew he had a right to refuse.

## Rule
Voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and knowledge of the right to refuse is not required. "[T]he question whether a consent to a search was in fact 'voluntary' or was the product of duress or coercion, express or implied, is a question of fact to be determined from the totality of all the circumstances." — 412 U.S. at 227. ^pin-227

"While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the *sine qua non* of an effective consent." — *Id.* ^pin-227a

## Application
The consent to search the car was given by Alcala after a routine traffic stop, with several officers present but no evidence of coercion. Because voluntariness turns on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]] and the State need not prove that Alcala knew he could refuse, his consent was voluntary on these facts, and the stolen checks discovered in the trunk were admissible.

## Conclusion
Consent voluntariness is determined from the totality of all the circumstances, without any requirement that the consenter be told of the right to refuse; the Court of Appeals' contrary rule was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Schneckloth* is the foundational consent-search voluntariness standard, applied in later consent cases such as [[Florida v. Bostick]] and [[United States v. Drayton]].

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *Schneckloth v. Bustamonte*, 412 U.S. 218 (1973) — https://www.courtlistener.com/opinion/108800/schneckloth-v-bustamonte/ — pinpoint: 227.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7fbf66f24b65de34", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "412 U.S. 218 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 6", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2041; 36 L. Ed. 2d 854", "title": "Schneckloth v. Bustamonte", "year": "1973"}}
{"assertion_id": "e4a593a64ba0d253", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The voluntariness of consent to search is a question of fact determined from the TOTALITY OF ALL THE CIRCUMSTANCES; the government need…", "title": "Schneckloth v. Bustamonte"}}
{"assertion_id": "ef3895b986a01cdc", "dimension": "support", "kind": "home_role", "locator": {"home": "Consent Searches"}, "payload": {"home": "Consent Searches", "role": "Key — Anchor", "title": "Schneckloth v. Bustamonte"}}
{"assertion_id": "2765cbc1c32b39bb", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Schneckloth v. Bustamonte", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Schneckloth v. Bustamonte", "varies_by_point": "false"}}
{"assertion_id": "8a06ae2c3c0aa953", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Schneckloth v. Bustamonte"}}
```

### lake record — Schneckloth v. Bustamonte

```json
{
  "schema_version": "s2.v1",
  "record_id": "Schneckloth v. Bustamonte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Schneckloth v. Bustamonte",
    "case_name_short": "Schneckloth",
    "case_name_full": "Schneckloth, Conservation Center Superintendent v. Bustamonte",
    "input_case_name": "Schneckloth v. Bustamonte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-05-29",
    "year": 1973,
    "docket": "71-732",
    "cluster_id": 108800,
    "lead_opinion_id": 108800,
    "sibling_ids": [
      108800,
      9425314,
      9425315,
      9425316,
      9425317,
      9425318,
      9425319
    ],
    "absolute_url": "/opinion/108800/schneckloth-v-bustamonte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "412 U.S. 218",
      "volume": "412",
      "reporter": "U.S.",
      "page": "218",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2041",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2041",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 854",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 6",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "412 U.S. 218",
        "volume": "412",
        "reporter": "U.S.",
        "page": "218",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2041",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2041",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "36 L. Ed. 2d 854",
        "volume": "36",
        "reporter": "L. Ed. 2d",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 6",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "6",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "412 U.S. 218",
    "official_selection": {
      "court_class": "scotus",
      "selected": "412 U.S. 218",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-227",
      "page": null,
      "quote": "and helped open the trunk, where stolen checks were found. Bustamonte, another occupant, was convicted; he argued the consent was invalid because no one had been told of a right to refuse. ## Issue Whether, to establish that consent to a search was voluntary, the State must prove that the person consenting knew he had a right to refuse. ## Rule Voluntariness is judged on the totality of the circumstances, and knowledge of the right to refuse is not required.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-227a",
      "page": null,
      "quote": "While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the *sine qua non* of an effective consent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Schneckloth v. Bustamonte",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poulson v. Commonwealth",
          "cluster_id": 10375911,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Baez",
          "cluster_id": 10283156,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane1_negative"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bounds v. Smith",
          "cluster_id": 109643,
          "cite": [
            "52 L. Ed. 2d 72",
            "97 S. Ct. 1491",
            "430 U.S. 817",
            "1977 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blackledge v. Allison",
          "cluster_id": 109648,
          "cite": [
            "52 L. Ed. 2d 136",
            "97 S. Ct. 1621",
            "431 U.S. 63",
            "1977 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Engle v. Isaac",
          "cluster_id": 110692,
          "cite": [
            "71 L. Ed. 2d 783",
            "102 S. Ct. 1558",
            "456 U.S. 107",
            "1982 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schriro v. Landrigan",
          "cluster_id": 145734,
          "cite": [
            "167 L. Ed. 2d 836",
            "127 S. Ct. 1933",
            "550 U.S. 465",
            "2007 U.S. LEXIS 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
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
        "journal_ref": "Schneckloth v. Bustamonte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjc1MjA5NjAwMDAwJnM9OTM3MjI2NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDgxJnM9MTE4NDY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjk4NjI0MDAwMDAwJnM9OTQzODk5NCZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108800 OR 9425314 OR 9425315 OR 9425316 OR 9425317 OR 9425318 OR 9425319)",
    "indexed_citing_opinions": 7588,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108800,
        "count": 6834,
        "count_source": "search"
      },
      {
        "opinion_id": 9425314,
        "count": 913,
        "count_source": "search"
      },
      {
        "opinion_id": 9425315,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425316,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425317,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425318,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 11786,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/schneckloth-v-bustamonte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NzQ0NjUmcz0xMDY5MjE3OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28108800+OR+9425314+OR+9425315+OR+9425316+OR+9425317+OR+9425318+OR+9425319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108800,
        "cited_id": 85668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 90687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 94093,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 96504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 102830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103012,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105306,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106660,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106721,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106821,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108297,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 108772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 227607,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 252628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 258899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 259180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 265436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 267291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 273438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 276566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 278364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 278813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 279301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 280244,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 281169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 286049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 287694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 289231,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 291168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 296899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 298163,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 299112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1100260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1140144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1149746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1165751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1207365,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1222379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1297467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1607433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1687619,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1750377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 1818084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 2112687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108800,
        "cited_id": 2614149,
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
    "date_created": "2026-07-05T18:41:45Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:44:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:41:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Schneckloth v. Bustamonte (truncated)

```
<div>
<center><b><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span> (1973)</b></center>
<center><h1>SCHNECKLOTH, CONSERVATION CENTER SUPERINTENDENT<br>
v.<br>
BUSTAMONTE.</h1></center>
<center>No. 71-732.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 10, 1972.</center>
<center>Decided May 29, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT.
<p><i>Robert R. Granucci,</i> Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>Evelle J. Younger,</i> Attorney General, <i>Herbert L. Ashby,</i> Chief Assistant Attorney General, <i>Doris H. Maier,</i> Assistant Attorney General, and <i>Edward P. O'Brien,</i> Deputy Attorney General</p>
<p><i>Stuart P. Tobisman,</i> by appointment of the Court, <span class="star-pagination">*219</span> <span class="citation multiple-matches"><a href="/c/U.%20S./405/1062/">405 U. S. 1062</a></span>, argued the cause and filed a brief for respondent <i>pro hac vice.</i><sup>[*]</sup></p>
<p><i>Melvin L. Wulf, Sanford J. Rosen, Joel M. Gora, A. L. Wirin, Fred Okrand,</i> and <i>Lawrence R. Sperber</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging affirmance.</p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>It is well settled under the Fourth and Fourteenth Amendments that a search conducted without a warrant issued upon probable cause is "<i>per se</i> unreasonable . . . subject only to a few specifically established and well-delineated exceptions." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#454" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 454-455</a></span>; <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 51</a></span>. It is equally well settled that one of the specifically established exceptions to the requirements of both a warrant and probable cause is a search that is conducted pursuant to consent. <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 593-594</a></span>; <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#630" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 630</a></span>. The constitutional question in the present case concerns the definition of "consent" in this Fourth and Fourteenth Amendment context.</p>
<p></p>
<h2>I</h2>
<p>The respondent was brought to trial in a California court upon a charge of possessing a check with intent to defraud.<sup>[1]</sup> He moved to suppress the introduction of certain material as evidence against him on the ground that the material had been acquired through an unconstitutional search and seizure. In response to the motion, the trial judge conducted an evidentiary hearing <span class="star-pagination">*220</span> where it was established that the material in question had been acquired by the State under the following circumstances:</p>
<p>While on routine patrol in Sunnyvale, California, at approximately 2:40 in the morning, Police Officer James Rand stopped an automobile when he observed that one headlight and its license plate light were burned out. Six men were in the vehicle. Joe Alcala and the respondent, Robert Bustamonte, were in the front seat with Joe Gonzales, the driver. Three older men were seated in the rear. When, in response to the policeman's question, Gonzales could not produce a driver's license, Officer Rand asked if any of the other five had any evidence of identification. Only Alcala produced a license, and he explained that the car was his brother's. After the six occupants had stepped out of the car at the officer's request and after two additional policemen had arrived, Officer Rand asked Alcala if he could search the car. Alcala replied, "Sure, go ahead." Prior to the search no one was threatened with arrest and, according to Officer Rand's uncontradicted testimony, it "was all very congenial at this time." Gonzales testified that Alcala actually helped in the search of the car, by opening the trunk and glove compartment. In Gonzales' words: "[T]he police officer asked Joe [Alcala], he goes, `Does the trunk open?' And Joe said, `Yes.' He went to the car and got the keys and opened up the trunk." Wadded up under the left rear seat, the police officers found three checks that had previously been stolen from a car wash.</p>
<p>The trial judge denied the motion to suppress, and the checks in question were admitted in evidence at Bustamonte's trial. On the basis of this and other evidence he was convicted, and the California Court of Appeal for the First Appellate District affirmed the conviction. <span class="star-pagination">*221</span> <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/" aria-description="Citation for case: People v. Bustamonte">270 Cal. App. 2d 648</a></span>, <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/" aria-description="Citation for case: People v. Bustamonte">76 Cal. Rptr. 17</a></span>. In agreeing that the search and seizure were constitutionally valid, the appellate court applied the standard earlier formulated by the Supreme Court of California in an opinion by then Justice Traynor: "Whether in a particular case an apparent consent was in fact voluntarily given or was in submission to an express or implied assertion of authority, is a question of fact to be determined in the light of all the circumstances." <i>People</i> v. <i>Michael,</i> <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#753" aria-description="Citation for case: People v. Michael">45 Cal. 2d 751, 753</a></span>, <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#854" aria-description="Citation for case: People v. Michael">290 P. 2d 852, 854</a></span>. The appellate court found that "[i]n the instant case the prosecution met the necessary burden of showing consent . . . since there were clearly circumstances from which the trial court could ascertain that consent had been freely given without coercion or submission to authority. Not only officer Rand, but Gonzales, the driver of the automobile, testified that Alcala's assent to the search of his brother's automobile was freely, even casually given. At the time of the request to search the automobile the atmosphere, according to Rand, was `congenial' and there had been no discussion of any crime. As noted, Gonzales said Alcala even attempted to aid in the search." <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/#652" aria-description="Citation for case: People v. Bustamonte">270 Cal. App. 2d, at 652</a></span>, <span class="citation" data-id="2198772"><a href="/opinion/2198772/people-v-bustamonte/#20" aria-description="Citation for case: People v. Bustamonte">76 Cal. Rptr., at 20</a></span>. The California Supreme Court denied review.<sup>[2]</sup></p>
<p>Thereafter, the respondent sought a writ of habeas corpus in a federal district court. It was denied.<sup>[3]</sup> On appeal, the Court of Appeals for the Ninth Circuit, relying on its prior decisions in <i>Cipres</i> v. <i>United States,</i> <span class="citation" data-id="267291"><a href="/opinion/267291/ramona-cipres-and-juan-montes-deoca-v-united-states/" aria-description="Citation for case: Ramona Cipres and Juan Montes Deoca v. United States">343 F. 2d 95</a></span>, and <i>Schoepflin</i> v. <i>United States,</i> <span class="citation" data-id="279301"><a href="/opinion/279301/emil-schoepflin-and-william-smith-v-united-states/" aria-description="Citation for case: Emil Schoepflin and William Smith v. United States">391 F. 2d 390</a></span>, set aside the District Court's order. <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,...">448 F. 2d 699</a></span>. The appellate court reasoned that a consent was a waiver of a person's Fourth and Fourteenth Amendment rights, and that the State was under an obligation to demonstrate, <span class="star-pagination">*222</span> not only that the consent had been uncoerced, but that it had been given with an understanding that it could be freely and effectively withheld. Consent could not be found, the court held, solely from the absence of coercion and a verbal expression of assent. Since the District Court had not determined that Alcala had <i>known</i> that his consent could have been withheld and that he could have refused to have his vehicle searched, the Court of Appeals vacated the order denying the writ and remanded the case for further proceedings. We granted certiorari to determine whether the Fourth and Fourteenth Amendments require the showing thought necessary by the Court of Appeals. <span class="citation multiple-matches"><a href="/c/U.%20S./405/953/">405 U. S. 953</a></span>.</p>
<p></p>
<h2>II</h2>
<p>It is important to make it clear at the outset what is not involved in this case. The respondent concedes that a search conducted pursuant to a valid consent is constitutionally permissible. In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#358" aria-description="Citation for case: Katz v. United States">389 U. S., at 358</a></span>, and more recently in <i>Vale</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#35" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 35</a></span>, we recognized that a search authorized by consent is wholly valid. See also <i>Davis</i> v. <i>United States,</i> 328 U. S., at 593-594; <i>Zap</i> v. <i>United States,</i> 328 U. S., at 630.<sup>[4]</sup> And similarly the State concedes that "[w]hen a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given." <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543, 548</a></span>. See also <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>.</p>
<p><span class="star-pagination">*223</span> The precise question in this case, then, is what must the prosecution prove to demonstrate that a consent was "voluntarily" given. And upon that question there is a square conflict of views between the state and federal courts that have reviewed the search involved in the case before us. The Court of Appeals for the Ninth Circuit concluded that it is an essential part of the State's initial burden to prove that a person knows he has a right to refuse consent. The California courts have followed the rule that voluntariness is a question of fact to be determined from the totality of all the circumstances, and that the state of a defendant's knowledge is only one factor to be taken into account in assessing the voluntariness of a consent. See, <i>e. g., </i><i>People</i> v. <i>Tremayne,</i> <span class="citation" data-id="2112687"><a href="/opinion/2112687/people-v-tremayne/" aria-description="Citation for case: People v. Tremayne">20 Cal. App. 3d 1006</a></span>, <span class="citation" data-id="2112687"><a href="/opinion/2112687/people-v-tremayne/" aria-description="Citation for case: People v. Tremayne">98 Cal. Rptr. 193</a></span>; <i>People</i> v. <i>Roberts,</i> <span class="citation" data-id="2186736"><a href="/opinion/2186736/people-v-roberts/" aria-description="Citation for case: People v. Roberts">246 Cal. App. 2d 715</a></span>, <span class="citation" data-id="2186736"><a href="/opinion/2186736/people-v-roberts/" aria-description="Citation for case: People v. Roberts">55 Cal. Rptr. 62</a></span>.</p>
<p></p>
<h2>A</h2>
<p>The most extensive judicial exposition of the meaning of "voluntariness" has been developed in those cases in which the Court has had to determine the "voluntariness" of a defendant's confession for purposes of the Fourteenth Amendment. Almost 40 years ago, in <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, the Court held that a criminal conviction based upon a confession obtained by brutality and violence was constitutionally invalid under the Due Process Clause of the Fourteenth Amendment. In some 30 different cases decided during the era that intervened between <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> and <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, the Court was faced with the necessity of determining whether in fact the confessions in issue had been "voluntarily" given.<sup>[5]</sup> It is to that body <span class="star-pagination">*224</span> of case law to which we turn for initial guidance on the meaning of "voluntariness" in the present context.<sup>[6]</sup></p>
<p>Those cases yield no talismanic definition of "voluntariness," mechanically applicable to the host of situations where the question has arisen. "The notion of `voluntariness,' " Mr. Justice Frankfurter once wrote, "is itself an amphibian." <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#604" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 604-605</a></span>. It cannot be taken literally to mean a "knowing" choice. "Except where a person is unconscious or drugged or otherwise lacks capacity for conscious choice, all incriminating statementseven those made under brutal treatmentare `voluntary' in the sense of representing a choice of alternatives. On the other hand, if `voluntariness' incorporates notions of `but-for' cause, the question should be whether the statement would have been made even absent inquiry or other official action. Under such a test, virtually no statement would be voluntary because very few people give incriminating statements in the absence of official action of some kind."<sup>[7]</sup> It is thus evident that neither linguistics nor epistemology will provide a ready definition of the meaning of "voluntariness."</p>
<p>Rather, "voluntariness" has reflected an accommodation of the complex of values implicated in police questioning <span class="star-pagination">*225</span> of a suspect. At one end of the spectrum is the acknowledged need for police questioning as a tool for the effective enforcement of criminal laws. See <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#578" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 578-580</a></span>. Without such investigation, those who were innocent might be falsely accused, those who were guilty might wholly escape prosecution, and many crimes would go unsolved. In short, the security of all would be diminished. <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span>. At the other end of the spectrum is the set of values reflecting society's deeply felt belief that the criminal law cannot be used as an instrument of unfairness, and that the possibility of unfair and even brutal police tactics poses a real and serious threat to civilized notions of justice. "[I]n cases involving involuntary confessions, this Court enforces the strongly felt attitude of our society that important human values are sacrificed where an agency of the government, in the course of securing a conviction, wrings a confession out of an accused against his will." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206-207</a></span>. See also <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#581" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 581-584</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 235-238</a></span>.</p>
<p>This Court's decisions reflect a frank recognition that the Constitution requires the sacrifice of neither security nor liberty. The Due Process Clause does not mandate that the police forgo all questioning, or that they be given carte blanche to extract what they can from a suspect. "The ultimate test remains that which has been the only clearly established test in Anglo-American courts for two hundred years: the test of voluntariness. Is the confession the product of an essentially free and unconstrained choice by its maker? If it is, if he has willed to confess, it may be used against him. If it is not, if his will has been overborne and his capacity for self-determination critically impaired, the use of his <span class="star-pagination">*226</span> confession offends due process." <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 602</a></span>.</p>
<p>In determining whether a defendant's will was overborne in a particular case, the Court has assessed the totality of all the surrounding circumstancesboth the characteristics of the accused and the details of the interrogation. Some of the factors taken into account have included the youth of the accused, <i>e. g., </i><i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span>; his lack of education, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>; or his low intelligence, <i>e. g., </i><i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191</a></span>; the lack of any advice to the accused of his constitutional rights, <i>e. g., </i><i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>; the length of detention, <i>e. g., </i><i>Chambers</i> v. <i><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">Florida, supra</a></span></i><i>;</i> the repeated and prolonged nature of the questioning, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; and the use of physical punishment such as the deprivation of food or sleep, <i>e. g., </i><i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span>.<sup>[8]</sup> In all of these cases, the Court determined the factual circumstances surrounding the confession, assessed the psychological impact on the accused, and evaluated the legal significance of how the accused reacted. <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#603" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 603</a></span>.</p>
<p>The significant fact about all of these decisions is that none of them turned on the presence or absence of a single controlling criterion; each reflected a careful scrutiny of all the surrounding circumstances. See <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#508" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 508</a></span> (Harlan, J., dissenting); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#534" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 534-535</a></span> (WHITE, J., dissenting). In none of them did the Court rule that the Due Process Clause required the prosecution to prove as part of its <span class="star-pagination">*227</span> initial burden that the defendant knew he had a right to refuse to answer the questions that were put. While the state of the accused's mind, and the failure of the police to advise the accused of his rights, were certainly factors to be evaluated in assessing the "voluntariness" of an accused's responses, they were not in and of themselves determinative. See, <i>e. g., </i><i>Davis</i> v. <i>North Carolina, supra</i><i>; </i><i>Haynes</i> v. <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#510" aria-description="Citation for case: Haynes v. Washington"><i>Washington, supra,</i> at 510-511</a></span>; <i>Culombe</i> v. <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#610" aria-description="Citation for case: Culombe v. Connecticut"><i>Connecticut, supra,</i> at 610</a></span>; <i>Turner</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9420381"><a href="/opinion/104711/turner-v-pennsylvania/#64" aria-description="Citation for case: Turner v. Pennsylvania">338 U. S. 62, 64</a></span>.</p>
<p></p>
<h2>B</h2>
<p>Similar considerations lead us to agree with the courts of California that the question whether a consent to a search was in fact "voluntary" or was the product of duress or coercion, express or implied, is a question of fact to be determined from the totality of all the circumstances. While knowledge of the right to refuse consent is one factor to be taken into account, the government need not establish such knowledge as the <i>sine qua non</i> of an effective consent. As with police questioning, two competing concerns must be accommodated in determining the meaning of a "voluntary" consentthe legitimate need for such searches and the equally important requirement of assuring the absence of coercion.</p>
<p>In situations where the police have some evidence of illicit activity, but lack probable cause to arrest or search, a search authorized by a valid consent may be the only means of obtaining important and reliable evidence.<sup>[9]</sup> In the present case for example, while the police had reason to stop the car for traffic violations, the State does not contend that there was probable cause to search the vehicle or that the search was incident to a valid arrest <span class="star-pagination">*228</span> of any of the occupants.<sup>[10]</sup> Yet, the search yielded tangible evidence that served as a basis for a prosecution, and provided some assurance that others, wholly innocent of the crime, were not mistakenly brought to trial. And in those cases where there is probable cause to arrest or search but where the police lack a warrant, a consent search may still be valuable. If the search is conducted and proves fruitless, that in itself may convince the police that an arrest with its possible stigma and embarrassment is unnecessary, or that a far more extensive search pursuant to a warrant is not justified. In short, a search pursuant to consent may result in considerably less inconvenience for the subject of the search, and properly conducted, is a constitutionally permissible and wholly legitimate aspect of effective police activity.</p>
<p>But the Fourth and Fourteenth Amendments require that a consent not be coerced, by explicit or implicit means, by implied threat or covert force. For, no matter how subtly the coercion was applied, the resulting "consent" would be no more than a pretext for the unjustified police intrusion against which the Fourth Amendment is directed. In the words of the classic admonition in <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, 635:</p>
<blockquote>"It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close <span class="star-pagination">*229</span> and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon."</blockquote>
<p>The problem of reconciling the recognized legitimacy of consent searches with the requirement that they be free from any aspect of official coercion cannot be resolved by any infallible touchstone. To approve such searches without the most careful scrutiny would sanction the possibility of official coercion; to place artificial restrictions upon such searches would jeopardize their basic validity. Just as was true with confessions, the requirement of a "voluntary" consent reflects a fair accommodation of the constitutional requirements involved. In examining all the surrounding circumstances to determine if in fact the consent to search was coerced, account must be taken of subtly coercive police questions, as well as the possibly vulnerable subjective state of the person who consents. Those searches that are the product of police coercion can thus be filtered out without undermining the continuing validity of consent searches. In sum, there is no reason for us to depart in the area of consent searches, from the traditional definition of "voluntariness."</p>
<p>The approach of the Court of Appeals for the Ninth Circuit finds no support in any of our decisions that have attempted to define the meaning of "voluntariness." Its ruling, that the State must affirmatively prove that the subject of the search knew that he had a right to refuse consent, would, in practice, create serious doubt whether consent searches could continue to be conducted. There might be rare cases where it could be proved from the record that a person in fact affirmatively knew of his <span class="star-pagination">*230</span> right to refusesuch as a case where he announced to the police that if he didn't sign the consent form, "you [police] are going to get a search warrant;"<sup>[11]</sup> or a case where by prior experience and training a person had clearly and convincingly demonstrated such knowledge.<sup>[12]</sup> But more commonly where there was no evidence of any coercion, explicit or implicit, the prosecution would nevertheless be unable to demonstrate that the subject of the search in fact had known of his right to refuse consent.</p>
<p>The very object of the inquirythe nature of a person's subjective understandingunderlines the difficulty of the prosecution's burden under the rule applied by the Court of Appeals in this case. Any defendant who was the subject of a search authorized solely by his consent could effectively frustrate the introduction into evidence of the fruits of that search by simply failing to testify that he in fact knew he could refuse to consent. And the near impossibility of meeting this prosecutorial burden suggests why this Court has never accepted any such litmus-paper test of voluntariness. It is instructive to recall the fears of then Justice Traynor of the California Supreme Court:</p>
<blockquote>"[I]t is not unreasonable for officers to seek interviews with suspects or witnesses or to call upon them at their homes for such purposes. Such inquiries, although courteously made and not accompanied with any assertion of a right to enter or search or secure answers, would permit the criminal to defeat his prosecution by voluntarily revealing all of the evidence against him and then contending that he acted only in response to an implied assertion of <span class="star-pagination">*231</span> unlawful authority." <i>People</i> v. <i>Michael,</i> <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#754" aria-description="Citation for case: People v. Michael">45 Cal. 2d, at 754</a></span>, <span class="citation" data-id="1140144"><a href="/opinion/1140144/people-v-michael/#854" aria-description="Citation for case: People v. Michael">290 P. 2d, at 854</a></span>.</blockquote>
<p>One alternative that would go far toward proving that the subject of a search did know he had a right to refuse consent would be to advise him of that right before eliciting his consent. That, however, is a suggestion that has been almost universally repudiated by both federal<sup>[13]</sup> and state courts,<sup>[14]</sup> and, we think, rightly so. For it would be thoroughly impractical to impose on the normal consent search the detailed requirements of an effective warning. Consent searches are part of the standard investigatory techniques of law enforcement <span class="star-pagination">*232</span> agencies. They normally occur on the highway, or in a person's home or office, and under informal and unstructured conditions. The circumstances that prompt the initial request to search may develop quickly or be a logical extension of investigative police questioning. The police may seek to investigate further suspicious circumstances or to follow up leads developed in questioning persons at the scene of a crime. These situations are a far cry from the structured atmosphere of a trial where, assisted by counsel if he chooses, a defendant is informed of his trial rights. Cf. <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/#243" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238, 243</a></span>. And, while surely a closer question, these situations are still immeasurably far removed from "custodial interrogation" where, in <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>,</i> we found that the Constitution required certain now familiar warnings as a prerequisite to police interrogation. Indeed, in language applicable to the typical consent search, we refused to extend the need for warnings:</p>
<blockquote>"Our decision is not intended to hamper the traditional function of police officers in investigating crime. . . . When an individual is in custody on probable cause, the police may, of course, seek out evidence in the field to be used at trial against him. Such investigation may include inquiry of persons not under restraint. General on-the-scene questioning as to facts surrounding a crime or other general questioning of citizens in the fact-finding process is not affected by our holding. It is an act of responsible citizenship for individuals to give whatever information they may have to aid in law enforcement." 384 U. S., at 477-478.</blockquote>
<p>Consequently, we cannot accept the position of the Court of Appeals in this case that proof of knowledge of the right to refuse consent is a necessary prerequisite <span class="star-pagination">*233</span> to demonstrating a "voluntary" consent. Rather, it is only by analyzing all the circumstances of an individual consent that it can be ascertained whether in fact it was voluntary or coerced. It is this careful sifting of the unique facts and circumstances of each case that is evidenced in our prior decisions involving consent searches.</p>
<p>For example, in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>, federal agents enforcing wartime gasoline-rationing regulations, arrested a filling station operator and asked to see his rationing coupons. He eventually unlocked a room where the agents discovered the coupons that formed the basis for his conviction. The District Court found that the petitioner had consented to the searchthat although he had at first refused to turn the coupons over, he had soon been persuaded to do so and that force or threat of force had not been employed to persuade him. Concluding that it could not be said that this finding was erroneous, this Court, in an opinion by MR. JUSTICE DOUGLAS that looked to all the circumstances surrounding the consent, affirmed the judgment of conviction: "The public character of the property, the fact that the demand was made during business hours at the place of business where the coupons were required to be kept, the existence of the right to inspect, the nature of the request, the fact that the initial refusal to turn the coupons over was soon followed by acquiescence in the demandthese circumstances all support the conclusion of the District Court." <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States"><i>Id.,</i> at 593-594</a></span>. See also <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">328 U. S. 624</a></span>.</p>
<p>Conversely, if under all the circumstances it has appeared that the consent was not given voluntarilythat it was coerced by threats or force, or granted only in submission to a claim of lawful authoritythen we have found the consent invalid and the search unreasonable. See, <i>e. g., </i><i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#548" aria-description="Citation for case: Bumper v. North Carolina">391 U. S., at 548-549</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>; <i>Amos</i> v. <span class="star-pagination">*234</span> <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>. In <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span>,</i> a 66-year-old Negro widow, who lived in a house located in a rural area at the end of an isolated mile-long dirt road, allowed four white law enforcement officials to search her home after they asserted they had a warrant to search the house. We held the alleged consent to be invalid, noting that "[w]hen a law enforcement officer claims authority to search a home under a warrant, he announces in effect that the occupant has no right to resist the search. The situation is instinct with coercionalbeit colorably lawful coercion. Where there is coercion there cannot be consent." <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/#550" aria-description="Citation for case: Bumper v. North Carolina">391 U. S., at 550</a></span>.</p>
<p>Implicit in all of these cases is the recognition that knowledge of a right to refuse is not a prerequisite of a voluntary consent. If the prosecution were required to demonstrate such knowledge, <i>Davis</i> and <i><span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/" aria-description="Citation for case: Zap v. United States">Zap</a></span></i> could not have found consent without evidence of that knowledge. And similarly if the failure to prove such knowledge were sufficient to show an ineffective consent, the <i>Amos, Johnson,</i> and <i><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">Bumper</a></span></i> opinions would surely have focused upon the subjective mental state of the person who consented. Yet they did not.</p>
<p>In short, neither this Court's prior cases, nor the traditional definition of "voluntariness" requires proof of knowledge of a right to refuse as the <i>sine qua non</i> of an effective consent to a search.<sup>[15]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*235</span> C</h2>
<p>It is said, however, that a "consent" is a "waiver" of a person's rights under the Fourth and Fourteenth Amendments. The argument is that by allowing the police to conduct a search, a person "waives" whatever right he had to prevent the police from searching. It is argued that under the doctrine of <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span>, to establish such a "waiver" the State must demonstrate "an intentional relinquishment or abandonment of a known right or privilege."</p>
<p>But these standards were enunciated in <i>Johnson</i> in the context of the safeguards of a fair criminal trial. Our cases do not reflect an uncritical demand for a knowing and intelligent waiver in every situation where a person has failed to invoke a constitutional protection. As Mr. Justice Black once observed for the Court: " `Waiver' is a vague term used for a great variety of purposes, good and bad, in the law." <i>Green</i> v. <i>United States,</i> <span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#191" aria-description="Citation for case: Green v. United States">355 U. S. 184, 191</a></span>. With respect to procedural due process, for example, the Court has acknowledged that waiver is possible, while explicitly leaving open the question whether a "knowing and intelligent" waiver need be shown.<sup>[16]</sup> See <i>D. H. Overmyer Co.</i> v. <i>Frick Co.,</i> <span class="star-pagination">*236</span> <span class="citation" data-id="9424754"><a href="/opinion/108474/d-h-overmyer-co-inc-of-ohio-v-frick-co/#185" aria-description="Citation for case: D. H. Overmyer Co., Inc. of Ohio v. Frick Co.">405 U. S. 174, 185-186</a></span>; <i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/#94" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67, 94-96</a></span>.<sup>[17]</sup></p>
<p>The requirement of a "knowing" and "intelligent" waiver was articulated in a case involving the validity of a defendant's decision to forgo a right constitutionally guaranteed to protect a fair trial and the reliability of the truth-determining process. <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst, supra</a></span></i><i>,</i> dealt with the denial of counsel in a federal criminal trial. There the Court held that under the Sixth Amendment a criminal defendant is entitled to the assistance of counsel, and that if he lacks sufficient funds to retain counsel, it is the Government's obligation to furnish him with a lawyer. As Mr. Justice Black wrote for the Court: "The Sixth Amendment stands as a constant admonition that if the constitutional safeguards it provides be lost, justice will not `still be done.' It embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel. That which is simple, orderly and necessary to the lawyer, to the untrained layman may appear intricate, complex and mysterious." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S., at 462-463</a></span> (footnote omitted). To preserve the fairness of the trial process the Court established an appropriately heavy burden on the Government before waiver could be found"an intentional <span class="star-pagination">*237</span> relinquishment or abandonment of a known right or privilege." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>Id.,</i> at 464</a></span>.</p>
<p>Almost without exception, the requirement of a knowing and intelligent waiver has been applied only to those rights which the Constitution guarantees to a criminal defendant in order to preserve a fair trial.<sup>[18]</sup> Hence, and hardly surprisingly in view of the facts of <i>Johnson</i> itself, the standard of a knowing and intelligent waiver has most often been applied to test the validity of a waiver of counsel, either at trial.<sup>[19]</sup> or upon a guilty plea.<sup>[20]</sup> And the Court has also applied the <i>Johnson</i> criteria to assess the effectiveness of a waiver of other trial rights such as the right to confrontation,<sup>[21]</sup> to a jury trial,<sup>[22]</sup> and to a speedy trial,<sup>[23]</sup> and the right to be free from <span class="star-pagination">*238</span> twice being placed in jeopardy.<sup>[24]</sup> Guilty pleas have been carefully scrutinized to determine whether the accused knew and understood all the rights to which he would be entitled at trial, and that he had intentionally chosen to forgo them.<sup>[25]</sup> And the Court has evaluated the knowing and intelligent nature of the waiver of trial rights in trial-type situations, such as the waiver of the privilege against compulsory self-incrimination before an administrative agency<sup>[26]</sup> or a congressional committee,<sup>[27]</sup> or the waiver of counsel in a juvenile proceeding.<sup>[28]</sup></p>
<p>The guarantees afforded a criminal defendant at trial also protect him at certain stages before the actual trial, and any alleged waiver must meet the strict standard of an intentional relinquishment of a "known" right. But the "trial" guarantees that have been applied to the "pretrial" <span class="star-pagination">*239</span> stage of the criminal process are similarly designed to protect the fairness of the trial itself.</p>
<p>Hence, in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>, and <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>, the Court held "that a post-indictment pretrial lineup at which the accused is exhibited to identifying witnesses is a critical stage of the criminal prosecution; that police conduct of such a lineup without notice to and in the absence of his counsel denies the accused his Sixth [and Fourteenth] Amendment right to counsel . . . ." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#272" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 272</a></span>. Accordingly, the Court indicated that the standard of a knowing and intelligent waiver must be applied to test the waiver of counsel at such a lineup. See <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#237" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 237</a></span>. The Court stressed the necessary interrelationship between the presence of counsel at a postindictment lineup before trial and the protection of the trial process itself:</p>
<blockquote>"Insofar as the accused's conviction may rest on a courtroom identification in fact the fruit of a suspect pretrial identification which the accused is helpless to subject to effective scrutiny at trial, the accused is deprived of that right of cross-examination which is an essential safeguard to his right to confront the witnesses against him. <i>Pointer</i> v. <i>Texas,</i> <span class="citation" data-id="9422988"><a href="/opinion/107014/pointer-v-texas/" aria-description="Citation for case: Pointer v. Texas">380 U. S. 400</a></span>. And even though cross-examination is a precious safeguard to a fair trial, it cannot be viewed as an absolute assurance of accuracy and reliability. Thus in the present context, where so many variables and pitfalls exist, the first line of defense must be the prevention of unfairness and the lessening of the hazards of eyewitness identification at the lineup itself. The trial which might determine the accused's fate may well not be that in the courtroom but that at the pretrial confrontation, with the State aligned against the accused the <span class="star-pagination">*240</span> witness the sole jury, and the accused unprotected against the overreaching, intentional or unintentional, and with little or no effective appeal from the judgment there rendered by the witness`that's the man.' " <i>Id.,</i> at 235-236.</blockquote>
<p>And in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, the Court found that <i>custodial</i> interrogation by the police was inherently coercive, and consequently held that detailed warnings were required to protect the privilege against compulsory self-incrimination. The Court made it clear that the basis for decision was the need to protect the fairness of the trial itself:</p>
<blockquote>"That counsel is present when statements are taken from an individual during interrogation obviously enhances the integrity of the fact-finding processes in court. The presence of an attorney, and the warnings delivered to the individual, enable the defendant under otherwise compelling circumstances to tell his story without fear, effectively, and in a way that eliminates the evils in the interrogation process. Without the protections flowing from adequate warnings and the rights of counsel, `all the careful safeguards erected around the giving of testimony, whether by an accused or any other witness, would become empty formalities in a procedure where the most compelling possible evidence of guilt, a confession, would have already been obtained at the unsupervised pleasure of the police.' " <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 466</a></span>.</blockquote>
<p>The standards of <i>Johnson</i> were, therefore, found to be a necessary prerequisite to a finding of a valid waiver. See 384 U. S., at 475-479. Cf. <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S., at 490</a></span> n. 14.<sup>[29]</sup></p>
<p><span class="star-pagination">*241</span> There is a vast difference between those rights that protect a fair criminal trial and the rights guaranteed under the Fourth Amendment. Nothing, either in the purposes behind requiring a "knowing" and "intelligent" waiver of trial rights, or in the practical application of such a requirement suggests that it ought to be extended to the constitutional guarantee against unreasonable searches and seizures.</p>
<p>A strict standard of waiver has been applied to those rights guaranteed to a criminal defendant to insure that he will be accorded the greatest possible opportunity to utilize every facet of the constitutional model of a fair criminal trial. Any trial conducted in derogation of that model leaves open the possibility that the trial reached an unfair result precisely because all the protections specified in the Constitution were not provided. A prime example is the right to counsel. For without that right, a wholly innocent accused faces the real and substantial danger that simply because of his lack of legal expertise he may be convicted. As Mr. Justice Harlan once wrote: "The sound reason why [the right to counsel] is so freely extended for a criminal trial is the severe injustice risked by confronting an untrained defendant with a range of technical points of law, evidence, and tactics familiar to the prosecutor but not to <span class="star-pagination">*242</span> himself." <i>Miranda</i> v. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#514" aria-description="Citation for case: Miranda v. Arizona"><i>Arizona, supra,</i> at 514</a></span> (dissenting opinion). The Constitution requires that every effort be made to see to it that a defendant in a criminal case has not unknowingly relinquished the basic protections that the Framers thought indispensable to a fair trial.<sup>[30]</sup></p>
<p>The protections of the Fourth Amendment are of a wholly different order, and have nothing whatever to do with promoting the fair ascertainment of truth at a criminal trial. Rather, as Mr. Justice Frankfurter's opinion for the Court put it in <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27</a></span>, the Fourth Amendment protects the "security of one's privacy against arbitrary intrusion by the police . . . ." In declining to apply the exclusionary rule of <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, to convictions that had become final before rendition of that decision, the Court emphasized that "there is no likelihood of unreliability or coercion present in a search-and-seizure case," <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#638" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 638</a></span>. In <i><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span>,</i> the Court indicated that those cases that had been given retroactive effect went to "the fairness of the trialthe very integrity of the fact-finding process. Here . . . the fairness of the trial is not under attack." <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#639" aria-description="Citation for case: Linkletter v. Walker"><i>Id.,</i> at 639</a></span>. The Fourth Amendment "is not an adjunct to the ascertainment of truth." The guarantees of the Fourth Amendment stand "as a protection of quite different constitutional valuesvalues reflecting the concern of our society for the right of each individual to be let alone. To recognize this is no more than to accord those values undiluted respect." <i>Tehan</i> v. <i>United States ex rel. Shott,</i> <span class="citation" data-id="9423130"><a href="/opinion/107148/tehan-v-united-states-ex-rel-shott/#416" aria-description="Citation for case: Tehan v. United States Ex Rel. Shott">382 U. S. 406, 416</a></span>.</p>
<p>Nor can it even be said that a search, as opposed to an eventual trial, is somehow "unfair" if a person consents to a search. While the Fourth and Fourteenth <span class="star-pagination">*243</span> Amendments limit the circumstances under which the police can conduct a search, there is nothing constitutionally suspect in a person's voluntarily allowing a search. The actual conduct of the search may be precisely the same as if the police had obtained a warrant. And unlike those constitutional guarantees that protect a defendant at trial, it cannot be said every reasonable presumption ought to be indulged against voluntary relinquishment. We have only recently stated: "[I]t is no part of the policy underlying the Fourth and Fourteenth Amendments to discourage citizens from aiding to the utmost of their ability in the apprehension of criminals." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#488" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 488</a></span>. Rather, the community has a real interest in encouraging consent, for the resulting search may yield necessary evidence for the solution and prosecution of crime, evidence that may insure that a wholly innocent person is not wrongly charged with a criminal offense.</p>
<p>Those cases that have dealt with the application of the <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> rule make clear that it would be next to impossible to apply to a consent search the standard of "an intentional relinquishment or abandonment of a known right or privilege."<sup>[31]</sup> To be true to <i>Johnson</i> <span class="star-pagination">*244</span> and its progeny, there must be examination into the knowing and understanding nature of the waiver, an examination that was designed for a trial judge in the structured atmosphere of a courtroom. As the Court expressed it in <i>Johnson:</i></p>
<blockquote>"The constitutional right of an accused to be represented by counsel invokes, of itself, the protection of a trial court, in which the accusedwhose life or liberty is at stakeis without counsel. This protecting duty imposes the serious and weighty responsibility upon the trial judge of determining whether there is an intelligent and competent waiver by the accused. While an accused may waive the right to counsel, whether there is a proper waiver should be clearly determined by the trial court, and it would be fitting and appropriate for that determination to appear upon the record." <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#465" aria-description="Citation for case: Johnson v. Zerbst">304 U. S., at 465</a></span>.<sup>[32]</sup></blockquote>
<p><span class="star-pagination">*245</span> It would be unrealistic to expect that in the informal, unstructured context of a consent search, a policeman, upon pain of tainting the evidence obtained, could make the detailed type of examination demanded by <i>Johnson.</i> And, if for this reason a diluted form of "waiver" were found acceptable, that would itself be ample recognition of the fact that there is no universal standard that must be applied in every situation where a person forgoes a constitutional right.<sup>[33]</sup></p>
<p>Similarly, a "waiver" approach to consent searches would be thoroughly inconsistent with our decisions that have approved "third party consents." In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#487" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 487-490</a></span>, where a wife surrendered to the police guns and clothing belonging to her husband, we found nothing constitutionally impermissible in the admission of that evidence at trial since the wife had not been coerced. <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#740" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 740</a></span>, held that evidence seized from the defendant's duffel bag in a search authorized by his cousin's consent was admissible at trial. We found that the defendant had assumed the risk that his cousin, with whom he shared the bag, would allow the police to search it. See also <i>Abel</i> v. <i>United States,</i> <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span>. And <span class="star-pagination">*246</span> in <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#802" aria-description="Citation for case: Hill v. California">401 U. S. 797, 802-805</a></span>, we held that the police had validly seized evidence from the petitioner's apartment incident to the arrest of a third party, since the police had probable cause to arrest the petitioner and reasonably, though mistakenly, believed the man they had arrested was he. Yet it is inconceivable that the Constitution could countenance the waiver of a defendant's right to counsel by a third party, or that a waiver could be found because a trial judge reasonably, though mistakenly, believed a defendant had waived his right to plead not guilty.<sup>[34]</sup></p>
<p>In short, there is nothing in the purposes or application of the waiver requirements of <i>Johnson</i> v. <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> that justifies, much less compels, the easy equation of a knowing waiver with a consent search. To make such an equation is to generalize from the broad rhetoric of some of our decisions, and to ignore the substance of the differing constitutional guarantees. We decline to follow what one judicial scholar has termed "the domino method of constitutional adjudication . . . wherein every explanatory statement in a previous opinion is made the basis for extension to a wholly different situation."<sup>[35]</sup></p>
<p></p>
<h2>D</h2>
<p>Much of what has already been said disposes of the argument that the Court's decision in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case requires the conclusion that knowledge of a right to refuse is an indispensable element of a valid consent. The considerations that informed the Court's holding in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are simply inapplicable in the present case. <span class="star-pagination">*247</span> In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> the Court found that the techniques of police questioning and the nature of custodial surroundings produce an inherently coercive situation. The Court concluded that "[u]nless adequate protective devices are employed to dispel the compulsion inherent in custodial surroundings, no statement obtained from the defendant can truly be the product of his free choice." 384 U. S., at 458. And at another point the Court noted that "without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <i>Id.,</i> at 467.</p>
<p>In this case, there is no evidence of any inherently coercive tacticseither from the nature of the police questioning or the environment in which it took place. Indeed, since consent searches will normally occur on a person's own familiar territory, the specter of incommunicado police interrogation in some remote station house is simply inapposite.<sup>[36]</sup> There is no reason to believe, under circumstances such as are present here, that the response to a policeman's question is presumptively coerced; and there is, therefore, no reason to reject the traditional test for determining the voluntariness of a person's response. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> of course, did not reach investigative questioning of a person not in custody, which is most directly analogous to the situation of a consent search, and it assuredly did not indicate that such questioning ought to be deemed inherently coercive. See <i>supra,</i> at 232.</p>
<p>It is also argued that the failure to require the Government to establish knowledge as a prerequisite to a valid <span class="star-pagination">*248</span> consent, will relegate the Fourth Amendment to the special province of "the sophisticated, the knowledgeable and the privileged." We cannot agree. The traditional definition of voluntariness we accept today has always taken into account evidence of minimal schooling, low intelligence, and the lack of any effective warnings to a person of his rights; and the voluntariness of any statement taken under those conditions has been carefully scrutinized to determine whether it was in fact voluntarily given.<sup>[37]</sup></p>
<p></p>
<h2>E</h2>
<p>Our decision today is a narrow one. We hold only that when the subject of a search is not in custody and the State attempts to justify a search on the basis of his consent, the Fourth and Fourteenth Amendments require that it demonstrate that the consent was in fact voluntarily given, and not the result of duress or coercion, express or implied. Voluntariness is a question of fact <span class="star-pagination">*249</span> to be determined from all the circumstances, and while the subject's knowledge of a right to refuse is a factor to be taken into account, the prosecution is not required to demonstrate such knowledge as a prerequisite to establishing a voluntary consent.<sup>[38]</sup> Because the California court followed these principles in affirming the respondent's conviction, and because the Court of Appeals for the Ninth Circuit in remanding for an evidentiary hearing required more, its judgment must be reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I join the Court's opinion and its judgment.</p>
<p>At the time <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), was decided, I, as a member of the Court of Appeals (but not of its panel) whose order was there reversed, found myself in agreement with the views expressed by Mr. Justice Harlan, writing for himself and my Brother STEWART in dissent. <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#242" aria-description="Citation for case: Kaufman v. United States"><i>Id.,</i> at 242</a></span>. My attitude has not changed in the four years that have passed since <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> was decided.</p>
<p>Although I agree with nearly all that MR. JUSTICE POWELL has to say in his detailed and persuasive concurring opinion, <i>post,</i> p. 250, I refrain from joining it at this time because, as MR. JUSTICE STEWART'S opinion reveals, it is not necessary to reconsider <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> in order to decide the present case.</p>
<p><span class="star-pagination">*250</span> MR. JUSTICE POWELL, with whom THE CHIEF JUSTICE and MR. JUSTICE REHNQUIST join, concurring.</p>
<p>While I join the opinion of the Court, it does not address what seems to me the overriding issue briefed and argued in this case: the extent to which federal habeas corpus should be available to a state prisoner seeking to exclude evidence from an allegedly unlawful search and seizure. I would hold that federal collateral review of a state prisoner's Fourth Amendment claimsclaims which rarely bear on innocenceshould be confined solely to the question of whether the petitioner was provided a fair opportunity to raise and have adjudicated the question in state courts. In view of the importance of this issue to our system of criminal justice, I think it appropriate to express my views.</p>
<p></p>
<h2>I</h2>
<p>Although petitions for federal habeas corpus assert a wide variety of constitutional questions, we are concerned in this case only with a Fourth Amendment claim that an unlawful search occurred and that the state court erred in failing to exclude the evidence obtained therefrom. A divided court in <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217</a></span> (1969), held that collateral review of search-and-seizure claims was appropriate on motions filed by federal prisoners under <span class="citation no-link">28 U. S. C. § 2255</span>. Until <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>,</i> a substantial majority of the federal courts of appeals had considered that claims of unlawful search and seizure " `are not proper matters to be presented by a motion to vacate sentence under § 2255 . . . .' " <i>Id.,</i> at 220. The rationale of this view was fairly summarized by the Court:</p>
<blockquote>"The denial of Fourth Amendment protection against unreasonable searches and seizures, the Government's <span class="star-pagination">*251</span> argument runs, is of a different nature from denials of other constitutional rights which we have held subject to collateral attack by federal prisoners. For unlike a claim of denial of effective counsel or of violation of the privilege against self incrimination, as examples, a claim of illegal search and seizure does not impugn the integrity of the fact-finding process or challenge evidence as inherently unreliable; rather, the exclusion of illegally seized evidence is simply a prophylactic device intended generally to deter Fourth Amendment violations by law enforcement officers." <i>Id.,</i> at 224.</blockquote>
<p>In rejecting this rationale, the Court noted that under prior decisions "the federal habeas remedy extends to state prisoners alleging that unconstitutionally obtained evidence was admitted against them at trial,"<sup>[1]</sup> and concluded that there was no basis for restricting "access by federal prisoners with illegal search-and-seizure claims to federal collateral remedies, while placing no similar restriction on access by state prisoners." <i>Id.,</i> at 225-226. In short, on petition for habeas corpus or collateral review filed in a federal district court, whether by state prisoners under <span class="citation no-link">28 U. S. C. § 2254</span> or federal prisoners under § 2255, the present rule is that Fourth Amendment claims may be asserted and the exclusionary rule must be applied in precisely the same manner as on direct review. Neither the history or purpose of habeas corpus, the desired prophylactic utility of the exclusionary rule as applied to Fourth Amendment claims, nor any sound reason relevant to the administration of criminal justice in our federal system justifies such a power.</p>
<p></p>
<h2>
<span class="star-pagination">*252</span> II</h2>
<p>The federal review involved in this Fourth Amendment case goes well beyond the traditional purpose of the writ of habeas corpus. Much of the present perception of habeas corpus stems from a revisionist view of the historic function that writ was meant to perform. The critical historical argument has focused on the nature of the writ at the time of its incorporation in our Constitution and at the time of the Habeas Corpus Act of 1867, the direct ancestor of contemporary habeas corpus statutes.<sup>[2]</sup> In <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#426" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 426</a></span> (1963), the Court interpreted the writ's historic position as follows:</p>
<blockquote>"At the time the privilege of the writ was written into the Federal Constitution it was settled that the writ lay to test any restraint contrary to fundamental law, which in England stemmed ultimately from Magna Charta but in this country was embodied in the written Constitution. Congress in 1867 sought to provide a federal forum for state prisoners having constitutional defenses by extending the habeas corpus powers of the federal courts to their constitutional maximum. Obedient to this purpose, we have consistently held that federal court <span class="star-pagination">*253</span> jurisdiction is conferred by the allegation of an unconstitutional restraint and is not defeated by anything that may occur in the state court proceedings."</blockquote>
<p>If this were a correct interpretation of the relevant history, the present wide scope accorded the writ would have arguable support, despite the impressive reasons to the contrary. But recent scholarship has cast grave doubt on <i>Fay's</i> version of the writ's historic function.</p>
<p>It has been established that both the Framers of the Constitution and the authors of the 1867 Act expected that the scope of habeas corpus would be determined with reference to the writ's historic, common-law development.<sup>[3]</sup> Mr. Chief Justice Marshall early referred to the common-law conception of the writ in determining its constitutional and statutory scope, <i>Ex parte Bollman,</i> <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#93" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 93-94</a></span> (1807); <i>Ex parte Watkins,</i> <span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/#201" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet. 193, 201-202</a></span> (1830), and Professor Oaks has noted that "when the 1867 Congress provided that persons restrained of their liberty in violation of the Constitution could obtain a writ of habeas corpus from a federal court, it undoubtedly intendedexcept to the extent the legislation provided otherwiseto incorporate the common-law uses and functions of this remedy."<sup>[4]</sup></p>
<p>It thus becomes important to understand exactly what was the common-law scope of the writ both when embraced by our Constitution and incorporated into the Habeas Corpus Act of 1867. Two respected scholars have recently explored precisely these questions.<sup>[5]</sup> Their efforts <span class="star-pagination">*254</span> have been both meticulous and revealing. Their conclusions differ significantly from those of the Court in <i>Fay</i> v. <i><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia</a></span></i><i>,</i> that habeas corpus traditionally has been available "to remedy any kind of governmental restraint contrary to fundamental law." <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#405" aria-description="Citation for case: Fay v. Noia">372 U. S., at 405</a></span>.</p>
<p>The considerable evidence marshaled by these scholars need not be restated here. Professor Oaks makes a convincing case that under the common law of habeas corpus at the time of the adoption of the Constitution, "once a person had been convicted by a superior court of general jurisdiction, a court disposing of a habeas corpus petition could not go behind the conviction for any purpose other than to verify the formal jurisdiction of the committing court."<sup>[6]</sup> Certainly that was what Mr. Chief Justice Marshall understood when he stated:</p>
<blockquote>"This writ [habeas corpus] is, as has been said, in the nature of a writ of error which brings up the body of the prisoner with the cause of commitment. The court can undoubtedly inquire into the sufficiency of that cause; but if it be the judgment of a court of competent jurisdiction, especially a judgment withdrawn by law from the revision of this court, is not that judgment in itself sufficient cause? Can the court, upon this writ, look beyond the judgment, and re-examine the charges on which it was rendered. A judgment, in its nature, concludes the subject on which it is rendered, and pronounces the law of the case. The judgment of a court of record whose jurisdiction is final, is as conclusive on all the world as the judgment of this court would be. It is as conclusive on this court as it is on other courts. It puts an end to inquiry concerning the fact, by deciding it." <i>Ex parte Watkins,</i> <span class="citation" data-id="85668"><a href="/opinion/85668/ex-parte-tobias-watkins/#202" aria-description="Citation for case: Ex Parte Tobias Watkins">3 Pet., at 202-203</a></span>.</blockquote>
<p><span class="star-pagination">*255</span> The respect shown under common law for the finality of the judgment of a committing court at the time of the Constitution and in the early 19th century did not, of course, explicitly contemplate the operation of habeas corpus in the context of federal-state relations. Federal habeas review for state prisoners was not available until passage of the Habeas Corpus Act of 1867. Yet there is no evidence that Congress intended that Act to jettison the respect theretofore shown by a reviewing court for prior judgments by a court of proper jurisdiction. The Act "received only the most perfunctory attention and consideration in the Congress; indeed, there were complaints that its effects could not be understood at all."<sup>[7]</sup> In fact, as Professor Bator notes, it would require overwhelming evidence, which simply is not present, to conclude that the 1867 Congress intended "to tear habeas corpus entirely out of the context of its historical meaning and scope and convert it into an ordinary writ of error with respect to all federal questions in all criminal cases."<sup>[8]</sup> Rather, the House Judiciary Committee when it reviewed the Act in 1884 understood that it was not "contemplated by its framers or . . . properly . . . construed to authorize the overthrow of the final judgments of the State courts of general jurisdiction, by the inferior Federal judges. . . ."<sup>[9]</sup></p>
<p>Much, of course, has transpired since that first Habeas Corpus Act. See <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#449" aria-description="Citation for case: Fay v. Noia">372 U. S., at 449-463</a></span> (Harlan, J., dissenting). The scope of federal habeas corpus for state prisoners has evolved from a quite limited inquiry into whether the committing state court had jurisdiction, <i>Andrews</i> v. <i>Swartz,</i> <span class="citation" data-id="94093"><a href="/opinion/94093/andrews-v-swartz/" aria-description="Citation for case: Andrews v. Swartz">156 U. S. 272</a></span> (1895); <i>In re</i> <span class="star-pagination">*256</span> <i>Moran,</i> <span class="citation" data-id="96504"><a href="/opinion/96504/matter-of-moran/" aria-description="Citation for case: Matter of Moran">203 U. S. 96</a></span> (1906), to whether the applicant had been given an adequate opportunity in state court to raise his constitutional claims, <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309</a></span> (1915); and finally to actual redetermination in federal court of state court rulings on a wide variety of constitutional contentions, <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span> (1953). No one would now suggest that this Court be imprisoned by every particular of habeas corpus as it existed in the late 18th and 19th centuries. But recognition of that reality does not liberate us from all historical restraint. The historical evidence demonstrates that the purposes of the writ, at the time of the adoption of the Constitution, were tempered by a due regard for the finality of the judgment of the committing court. This regard was maintained substantially intact when Congress, in the Habeas Corpus Act of 1867, first extended federal habeas review to the delicate interrelations of our dual court systems.</p>
<p></p>
<h2>III</h2>
<p>Recent decisions, however, have tended to depreciate the importance of the finality of prior judgments in criminal cases. <i>Kaufman,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#228" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 228</a></span>; <i>Sanders</i> v. <i>United States,</i> <span class="citation" data-id="9422578"><a href="/opinion/106591/sanders-v-united-states/#8" aria-description="Citation for case: Sanders v. United States">373 U. S. 1, 8</a></span> (1963); <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#424" aria-description="Citation for case: Fay v. Noia"><i>Fay, supra,</i> at 424</a></span>. This trend may be a justifiable evolution of the use of habeas corpus where the one in state custody raises a constitutional claim bearing on his innocence. But the justification for disregarding the historic scope and function of the writ is measurably less apparent in the typical Fourth Amendment claim asserted on collateral attack. In this latter case, a convicted defendant is most often asking society to redetermine a matter with no bearing at all on the basic justice of his incarceration.</p>
<p>Habeas corpus indeed <i>should</i> provide the added assurance for a free society that no innocent man suffers an unconstitutional loss of liberty. The Court in <i><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Fay</a></span></i> described <span class="star-pagination">*257</span> habeas corpus as a remedy for "whatever society deems to be intolerable restraints," and recognized that those to whom the writ should be granted "are persons whom society has grievously wronged and for whom belated liberation is little enough compensation." <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#401" aria-description="Citation for case: Fay v. Noia"><i>Id.,</i> at 401-402, 441</a></span>. The Court there acknowledged that the central reason for the writ lay in remedying injustice to the individual. Recent commentators have recognized the same core concept, one noting that "where <i>personal liberty</i> is involved, a democratic society . . . insists that it is less important to reach an unshakable decision than to <i>do justice</i> (emphasis added),"<sup>[10]</sup> and another extolling the use of the writ in <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span> (1954), with the assertion that "[b]ut for federal habeas corpus, these two men would have gone to their deaths for crimes of which they were found not guilty."<sup>[11]</sup></p>
<p>I am aware that history reveals no exact tie of the writ of habeas corpus to a constitutional claim relating to innocence or guilt. Traditionally, the writ was unavailable even for many constitutional pleas grounded on a claimant's innocence, while many contemporary proponents of expanded employment of the writ would permit its issuance for one whose deserved confinement was never in doubt. We are now faced, however, with the task of accommodating the historic respect for the finality of the judgment of a committing court with recent Court expansions of the role of the writ. This accommodation can best be achieved, with due regard to all of the values implicated, by recourse to the central reason for habeas corpus: the affording of means, <span class="star-pagination">*258</span> through an extraordinary writ, of redressing an <i>unjust</i> incarceration.</p>
<p>Federal habeas review of search and seizure claims is rarely relevant to this reason. Prisoners raising Fourth Amendment claims collaterally usually are quite <i>justly</i> detained. The evidence obtained from searches and seizures is often "the clearest proof of guilt" with a very high content of reliability.<sup>[12]</sup> Rarely is there any contention that the search rendered the evidence unreliable or that its means cast doubt upon the prisoner's guilt. The words of Mr. Justice Black drive home the point:</p>
<blockquote>"A claim of illegal search and seizure under the Fourth Amendment is crucially different from many other constitutional rights; ordinarily the evidence seized can in no way have been rendered untrustworthy by the means of its seizure and indeed often this evidence alone establishes beyond virtually any shadow of a doubt that the defendant is guilty." <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#237" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 237</a></span> (1969) (dissenting opinion).</blockquote>
<p>Habeas corpus review of search and seizure claims thus brings a deficiency of our system of criminal justice into sharp focus: a convicted defendant asserting no constitutional claim bearing on innocence and relying solely on an alleged unlawful search, is now entitled to federal habeas review of state conviction and the likelihood of release if the reviewing court concludes that the search was unlawful. That federal courts would actually redetermine constitutional claims bearing no relation to the prisoner's innocence with the possibility of releasing him from custody if the search is held unlawful not only defeats our societal interest in a rational legal system but serves no compensating ends of personal justice.</p>
<p></p>
<h2>
<span class="star-pagination">*259</span> IV</h2>
<p>This unprecedented extension of habeas corpus far beyond its historic bounds and in disregard of the writ's central purpose is an anomaly in our system sought to be justified only by extrinsic reasons which will be addressed in Part V of this opinion. But first let us look at the costs of this anomalycosts in terms of serious intrusions on other societal values. It is these other values that have been subordinatednot to further justice on behalf of arguably innocent persons but all too often to serve mechanistic rules quite unrelated to justice in a particular case. Nor are these neglected values unimportant to justice in the broadest sense or to our system of Government. They include (i) the most effective utilization of limited judicial resources, (ii) the necessity of finality in criminal trials, (iii) the minimization of friction between our federal and state systems of justice, and (iv) the maintenance of the constitutional balance upon which the doctrine of federalism is founded.</p>
<p>When raised on federal habeas, a claim generally has been considered by two or more tiers of state courts. It is the solemn duty of these courts, no less than federal ones, to safeguard personal liberties and consider federal claims in accord with federal law. The task which federal courts are asked to perform on habeas is thus most often one that has or should have been done before. The presumption that "if a job can be well done once, it should not be done twice" is sound and one calculated to utilize best "the intellectual, moral, and political resources involved in the legal system."<sup>[13]</sup></p>
<p><span class="star-pagination">*260</span> Those resources are limited but demand on them constantly increases. There is an insistent call on federal courts both in civil actions, many novel and complex, which affect intimately the lives of great numbers of people and in original criminal trials and appeals which deserve our most careful attention.<sup>[14]</sup> To the extent the federal courts are required to re-examine claims on collateral <span class="star-pagination">*261</span> attack,<sup>[15]</sup> they deprive primary litigants of their prompt availability and mature reflection. After all, the resources of our system are finite: their overextension jeopardizes the care and quality essential to fair adjudication.</p>
<p>The present scope of federal habeas corpus also has worked to defeat the interest of society in a rational point of termination for criminal litigation. Professor Amsterdam has identified some of the finality interests at stake in collateral proceedings:</p>
<blockquote>"They involve (a) duplication of judicial effort; (b) delay in setting the criminal proceeding at rest; (c) inconvenience and possibly danger in transporting a prisoner to the sentencing court for hearing; (d) postponed litigation of fact, hence litigation which will often be less reliable in reproducing the facts (i) respecting the postconviction claim itself, and (ii) respecting the issue of guilt if the collateral attack succeeds in a form which allows retrial. . . ."</blockquote>
<p>He concluded that:</p>
<blockquote>"[I]n combination, these finality considerations amount to a more or less persuasive argument against the cognizability of any particular collateral <span class="star-pagination">*262</span> claim, the strength of the argument depending upon the nature of the claim, the manner of its treatment (if any) in the conviction-proceedings, and the circumstances under which collateral litigation must be had."<sup>[16]</sup></blockquote>
<p>No effective judicial system can afford to concede the continuing theoretical possibility that there is error in every trial and that every incarceration is unfounded. At some point the law must convey to those in custody that a wrong has been committed, that consequent punishment has been imposed, that one should no longer look back with the view to resurrecting every imaginable basis for further litigation but rather should look forward to rehabilitation and to becoming a constructive citizen.<sup>[17]</sup></p>
<p>Nowhere should the merit of this view be more self-evident than in collateral attack on an allegedly unlawful search and seizure, where the petitioner often asks society to <i>redetermine</i> a claim with no relationship at all to the justness of his confinement. Professor Amsterdam has noted that "for reasons which are common to all search and seizure claims," he "would hold even a slight finality interest sufficient to deny the collateral remedy."<sup>[18]</sup> But, in fact, a strong finality interest militates against allowing <span class="star-pagination">*263</span> collateral review of search-and-seizure claims. Apart from the duplication of resources inherent in most habeas corpus proceedings, the validity of a search-and-seizure claim frequently hinges on a complex matrix of events which may be difficult indeed for the habeas court to disinter especially where, as often happens, the trial occurred years before the collateral attack and the state record is thinly sketched.<sup>[19]</sup></p>
<p>Finally, the present scope of habeas corpus tends to undermine the values inherent in our federal system of government. To the extent that every state criminal judgment is to be subject indefinitely to broad and repetitive federal oversight, we render the actions of state courts a serious disrespect in derogation of the constitutional balance between the two systems.<sup>[20]</sup> The present expansive scope of federal habeas review has prompted no small friction between state and federal judiciaries. Justice Paul C. Reardon of the Massachusetts Supreme <span class="star-pagination">*264</span> Judicial Court and then President of the National Center for State Courts, in identifying problems between the two systems, noted bluntly that "[t]he first, without question, is the effect of Federal habeas corpus proceedings on State courts." He spoke of the "humiliation of review from the full bench of the highest State appellate court to a single United States District Court judge." Such broad federal habeas powers encourage in his view the "growing denigration of the State courts and their functions in the public mind."<sup>[21]</sup> In so speaking Justice Reardon echoed the words of Professor Bator:</p>
<blockquote>"I could imagine nothing more subversive of a judge's sense of responsibility, of the inner subjective conscientiousness which is so essential a part of the difficult and subtle art of judging well, than an indiscriminate <span class="star-pagination">*265</span> acceptance of the notion that all the shots will always be called by someone else."<sup>[22]</sup></blockquote>
<p>In my view, this Court has few more pressing responsibilities than to restore the mutual respect and the balanced sharing of responsibility between the state and federal courts which our tradition and the Constitution itself so wisely contemplate. This can be accomplished without retreat from our inherited insistence that the writ of habeas corpus retain its full vitality as a means of redressing injustice.</p>
<p>This case involves only a relatively narrow aspect of the appropriate reach of habeas corpus. The specific issue before us, and the only one that need be decided at this time, is the extent to which a state prisoner may obtain federal habeas corpus review of a Fourth Amendment claim. Whatever may be formulated as a more comprehensive answer to the important broader issues (whether by clarifying legislation or in subsequent decisions), Mr. Justice Black has suggested what seems to me to be the appropriate threshold requirement in a case of this kind:</p>
<blockquote>"I would always require that the convicted defendant raise the kind of constitutional claim that casts some shadow of a doubt on his guilt." <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#242" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 242</a></span> (dissenting opinion).</blockquote>
<p>In a perceptive analysis, Judge Henry J. Friendly expressed a similar view. He would draw the line against habeas corpus review in the absence of a "colorable claim of innocence":</p>
<blockquote>"[W]ith a few important exceptions, convictions should be subject to collateral attack only when <span class="star-pagination">*266</span> the prisoner supplements his constitutional plea with a colorable claim of innocence."<sup>[23]</sup></blockquote>
<p>Where there is no constitutional claim bearing on innocence, the inquiry of the federal court on habeas review of a state prisoner's Fourth Amendment claim should be confined solely to the question whether the defendant was provided a fair opportunity in the state courts to raise and have adjudicated the Fourth Amendment claim. Limiting the scope of habeas review in this manner would reduce the role of the federal courts in determining the merits of constitutional claims with no relation to a petitioner's innocence and contribute to the restoration of recently neglected values to their proper place in our criminal justice system.</p>
<p></p>
<h2>V</h2>
<p>The importance of the values referred to above is not questioned. What, then, is the reason which has prompted this Court in recent decisions to extend habeas corpus to Fourth Amendment claims largely in disregard of its history as well as these values? In addressing Mr. Justice Black's dissenting view that constitutional claims raised collaterally should be relevant to the petitioner's innocence, the majority in <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> noted:</p>
<blockquote>"It [Mr. Justice Black's view] brings into question <i>the propriety of the exclusionary rule itself.</i> The application of that rule is not made to turn on the <span class="star-pagination">*267</span> existence of a possibility of innocence; rather, exclusion of illegally obtained evidence is deemed necessary to protect the right of all citizens, not merely the citizen on trial, to be secure against unreasonable searches and seizures." 394 U. S., at 229. (Emphasis added.)</blockquote>
<p>The exclusionary rule has occasioned much criticism, largely on grounds that its application permits guilty defendants to go free and law-breaking officers to go unpunished.<sup>[24]</sup> The oft-asserted reason for the rule is to deter illegal searches and seizures by the police, <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960); <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 656</a></span> (1961); <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 636</a></span> (1965); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 29</a></span> (1968).<sup>[25]</sup><span class="star-pagination">*268</span> The efficacy of this deterrent function, however, has been brought into serious question by recent empirical research. Whatever the rule's merits on an initial trial and appeal<sup>[26]</sup>a question not in issue herethe case for <span class="star-pagination">*269</span> collateral application of the rule is an anemic one. On collateral attack, the exclusionary rule retains its major liabilities while the asserted benefit of the rule dissolves. For whatever deterrent function the rule may serve when applied on trial and appeal becomes greatly attenuated when, months or years afterward, the claim surfaces for collateral review. The impermissible conduct has long since occurred, and the belated wrist slap of state police by federal courts harms no one but society on whom the convicted criminal is newly released.<sup>[27]</sup></p>
<p>Searches and seizures are an opaque area of the law: flagrant Fourth Amendment abuses will rarely escape detection but there is a vast twilight zone with respect to which one Justice has stated that our own "decisions . . . are hardly notable for their predictability,"<sup>[28]</sup> and another has observed that this Court was " `bifurcating elements too infinitesimal to be split.' "<sup>[29]</sup> Serious Fourth Amendment infractions can be dealt with by state judges or by this Court on direct review. But the nonfrivolous Fourth Amendment claims that survive for collateral attack are most likely to be in this grey, twilight area, where the law is difficult for courts to apply, let alone for the policeman on the beat to understand. This is <span class="star-pagination">*270</span> precisely the type of case where the deterrent function of the exclusionary rule is least efficacious, and where there is the least justification for freeing a duly convicted defendant.<sup>[30]</sup></p>
<p>Our decisions have not encouraged the thought that what may be an appropriate constitutional policy in one context automatically becomes such for all times and all seasons. In <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 629</a></span>, the Court recognized the compelling practical considerations against retroactive application of the exclusionary rule. Rather than viewing the rule as having eternal constitutional verity, the Court decided to</p>
<blockquote>"weigh the merits and demerits in each case by looking to the prior history of the rule in question, its purpose and effect, and whether retrospective operation will further or retard its operation. We believe that this approach is particularly correct with reference to the Fourth Amendment's prohibitions as to unreasonable searches and seizures." <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker"><i>Id.,</i> at 629</a></span>.</blockquote>
<p>Such a pragmatic approach compelled the Court to conclude that the rule's deterrent function would not be advanced by its retrospective application:</p>
<blockquote>"The misconduct of the police prior to <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> has already occurred and will not be corrected by releasing the prisoners involved. . . . Finally, the ruptured privacy of the victims' homes and effects cannot be restored. Reparation comes too late." <i>Id.,</i> at 637.</blockquote>
<p>See also <i>Desist</i> v. <i>United States,</i> <span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/" aria-description="Citation for case: Desist v. United States">394 U. S. 244</a></span> (1969).</p>
<p>The same practical, particularized analysis of the exclusionary rule's necessity also was evident in <i>Walder</i> v. <i>United States,</i> <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">347 U. S. 62</a></span> (1954), when the Court permitted <span class="star-pagination">*271</span> the Government to utilize unlawfully seized evidence to impeach the credibility of a defendant who had first testified broadly in his own defense. The Court held, in effect, that the policies protected by the exclusionary rule were outweighed in this case by the need to prevent perjury and assure the integrity of proceedings at trial. The Court concluded that to apply the exclusionary rule in such circumstances "would be a perversion of the Fourth Amendment." <span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/#65" aria-description="Citation for case: Walder v. United States"><i>Id.,</i> at 65</a></span>. The judgment in <i><span class="citation" data-id="105188"><a href="/opinion/105188/walder-v-united-states/" aria-description="Citation for case: Walder v. United States">Walder</a></span></i> revealed most pointedly that the policies behind the exclusionary rule are neither absolute nor allencompassing, but rather must be weighed and balanced against a competing and more compelling policy, namely the need for effective determination of truth at trial.</p>
<p>In sum: the case for the exclusionary rule varies with the setting in which it is imposed. It makes little sense to extend the <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> exclusionary rule to a federal habeas proceeding where its asserted deterrent effect must be least efficacious, and its obvious harmful consequences persist in full force.</p>
<p></p>
<h2>VI</h2>
<p>The final inquiry is whether the above position conforms to <span class="citation no-link">28 U. S. C. § 2254</span> (a) which provides:</p>
<blockquote>"The Supreme Court, a Justice thereof, a circuit judge, or a district court shall entertain an application for a writ of habeas corpus in behalf of a person in custody pursuant to the judgment of a State court only on the ground that he is in custody in violation of the Constitution or laws or treaties of the United States."</blockquote>
<p>The trend in recent years has witnessed a proliferation of constitutional rights, "a vast expansion of the claims of error in criminal cases for which a resourceful defense lawyer can find a constitutional basis."<sup>[31]</sup> Federal habeas <span class="star-pagination">*272</span> jurisdiction has been extended far beyond anyone's expectation or intendment when the concept of "custody in violation of the Constitution," now in § 2254 (a), first appeared in federal law over a century ago.<sup>[32]</sup></p>
<p>Mr. Justice Black was clearly correct in noting that "not every conviction based in part on a denial of a constitutional right is subject to attack by habeas corpus or § 2255 proceedings after a conviction has become final." <i>Kaufman,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#232" aria-description="Citation for case: Kaufman v. United States">394 U. S., at 232</a></span> (dissenting opinion). No evidence exists that Congress intended every allegation of a constitutional violation to afford an appropriate basis for collateral review: indeed, the latest revisions of the Federal Habeas Corpus statute in 1966<sup>[33]</sup> and the enactment of § 2254 (a) came at the time a majority of the courts of appeals held that claims of unlawful search and seizure " `are not proper matters to be presented by a motion to vacate sentence under § 2255 but can only be properly presented by appeal from the conviction.' " <i>Id.,</i> at 220, quoting <i>Warren</i> v. <i>United States,</i> <span class="citation" data-id="259180"><a href="/opinion/259180/alphonse-warren-v-united-states/#675" aria-description="Citation for case: Alphonse Warren v. United States">311 F. 2d 673, 675</a></span> (CA8 1963).<sup>[34]</sup> Though the precise discussion in <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span></i> concerned the claims of federal prisoners under § 2255, the then-existing principle of a distinction between review of search-and-seizure claims in direct and collateral proceedings clearly existed.</p>
<p>There is no indication that Congress intended to wipe out this distinction. Indeed, the broad purpose of the 1966 amendments pointed in the opposite direction. The report of the Senate Judiciary Committee notes that:</p>
<blockquote>"Although only a small number of these [habeas] applications have been found meritorious, the applications <span class="star-pagination">*273</span> in their totality have imposed a heavy burden on the Federal courts. . . . The bill seeks to alleviate the unnecessary burden by introducing a greater degree of finality of judgments in habeas corpus proceedings." S. Rep. No. 1797, 89th Cong., 2d Sess., 2 (1966).<sup>[35]</sup></blockquote>
<p>The House Report states similarly that:</p>
<blockquote>"While in only a small number of these applications have the petitioners been successful, they nevertheless have not only imposed an unnecessary burden on the work of the Federal courts but have also greatly interfered with the procedures and processes of the State courts by delaying, in many cases, the proper enforcement of their judgments." H. R. Rep. No. 1892, 89th Cong., 2d Sess., 5 (1966).</blockquote>
<p>This most recent congressional expression on the scope of federal habeas corpus reflected the sentiment, shared alike by judges and legislators, that the writ has overrun its historical banks to inundate the dockets of federal courts and denigrate the role of state courts. Though Congress did not address the precise question at hand, nothing in § 2254 (a), the state of the law at the time of its adoption, or the historical uses of the language "custody in violation of the Constitution" from which § 2254 (a) is derived,<sup>[36]</sup> compels a holding that rulings of state courts on claims of unlawful search and <span class="star-pagination">*274</span> seizure must be reviewed and redetermined in collateral proceedings.</p>
<p></p>
<h2>VII</h2>
<p>Perhaps no single development of the criminal law has had consequences so profound as the escalating use, over the past two decades, of federal habeas corpus to reopen and readjudicate state criminal judgments. I have commented in Part IV above on the far-reaching consequences: the burden on the system,<sup>[37]</sup> in terms of demands on the courts, prosecutors, defense attorneys, and other personnel and facilities; the absence of efficiency and finality in the criminal process, frustrating both the deterrent function of the law and the effectiveness of rehabilitation; the undue subordination of state courts, with the resulting exacerbation of state-federal relations; and the subtle erosion of the doctrine of federalism itself. Perhaps the single most disquieting consequence of openended habeas review is reflected in the prescience of Mr. Justice Jackson's warning that "[i]t must prejudice the occasional meritorious application to be buried in a flood of worthless ones."<sup>[38]</sup></p>
<p>If these consequences flowed from the safeguarding of constitutional claims of innocence they should, of course, be accepted as a tolerable price to pay for cherished standards of justice at the same time that efforts are pursued to find more rational procedures. Yet, as illustrated by the case before us today, the question on habeas corpus is <span class="star-pagination">*275</span> too rarely whether the prisoner was innocent of the crime for which he was convicted<sup>[39]</sup> and too frequently whether some evidence of undoubted probative value has been admitted in violation of an exclusionary rule ritualistically applied without due regard to whether it has the slightest likelihood of achieving its avowed prophylactic purpose.</p>
<p>It is this paradox of a system, which so often seems to subordinate substance to form, that increasingly provokes criticism and lack of confidence. Indeed, it is difficult to explain why a system of criminal justice deserves respect which allows repetitive reviews of convictions long since held to have been final at the end of the normal process of trial and appeal where the basis for re-examination is not even that the convicted defendant was innocent. There has been a halo about the "Great Writ" that no one would wish to dim. Yet one must wonder whether the stretching of its use far beyond any justifiable purpose will not in the end weaken rather than strengthen the writ's vitality.</p>
<p>MR. JUSTICE DOUGLAS, dissenting.</p>
<p>I agree with the Court of Appeals that "verbal assent" to a search is not enough, that the fact that consent was given to the search does not imply that the suspect knew that the alternative of a refusal existed. <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/#700" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,...">448 F. 2d 699, 700</a></span>. As that court stated:</p>
<blockquote>"[U]nder many circumstances a reasonable person might read an officer's `May I' as the courteous expression <span class="star-pagination">*276</span> of a demand backed by force of law." <span class="citation" data-id="299112"><a href="/opinion/299112/robert-bustamonte-v-merle-r-schneckloth-superintendent-california/#701" aria-description="Citation for case: Robert Bustamonte v. Merle R. Schneckloth,..."><i>Id.,</i> at 701</a></span>.</blockquote>
<p>A considerable constitutional guarantee rides on this narrow issue. At the time of the search there was no probable cause to believe that the car contained contraband or other unlawful articles. The car was stopped only because a headlight and the license plate light were burned out. The car belonged to Alcala's brother, from whom it was borrowed, and Alcala had a driver's license. Traffic citations were appropriately issued. The car was searched, the present record showing that Alcala consented. But whether Alcala knew he had the right to refuse, we do not know. All the Court of Appeals did was to remand the case to the District Court for a finding and if necessary, a hearing on that issue.</p>
<p>I would let the case go forward on that basis. The long, time-consuming contest in this Court might well wash out. At least we could be assured that, if it came back, we would not be rendering an advisory opinion. Had I voted to grant this petition, I would suggest we dismiss it as improvidently granted. But, being in the minority, I am bound by the Rule of Four.</p>
<p>MR. JUSTICE BRENNAN, dissenting.</p>
<p>The Fourth Amendment specifically guarantees "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures . . . ." We have consistently held that governmental searches conducted pursuant to a validly obtained warrant or reasonably incident to a valid arrest do not violate this guarantee. Here, however, as the Court itself recognizes, no search warrant was obtained and the State does not even suggest "that there was probable cause to search the vehicle or that the search was incident to a valid arrest of any of the occupants." <i>Ante,</i> <span class="star-pagination">*277</span> at 227-228. As a result, the search of the vehicle can be justified solely on the ground that the owner's brother gave his consentthat is, that he waived his Fourth Amendment right "to be secure" against an otherwise "unreasonable" search. The Court holds today that an individual can effectively waive this right even though he is totally ignorant of the fact that, in the absence of his consent, such invasions of his privacy would be constitutionally prohibited. It wholly escapes me how our citizens can meaningfully be said to have waived something as precious as a constitutional guarantee without ever being aware of its existence. In my view, the Court's conclusion is supported neither by "linguistics." nor by "epistemology," nor, indeed, by "common sense." I respectfully dissent.</p>
<p>MR. JUSTICE MARSHALL, dissenting.</p>
<p>Several years ago, MR. JUSTICE STEWART reminded us that "[t]he Constitution guarantees . . . a society of free choice. Such a society presupposes the capacity of its members to choose." <i>Ginsberg</i> v. <i>New York,</i> <span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/#649" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629, 649</a></span> (1968) (concurring in result). I would have thought that the capacity to choose necessarily depends upon knowledge that there is a choice to be made. But today the Court reaches the curious result that one can choose to relinquish a constitutional right the right to be free of unreasonable searcheswithout knowing that he has the alternative of refusing to accede to a police request to search.<sup>[1]</sup> I cannot agree, and therefore dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*278</span> I</h2>
<p>I believe that the Court misstates the true issue in this case. That issue is not, as the Court suggests, whether the police overbore Alcala's will in eliciting his consent, but rather, whether a simple statement of assent to search, without more,<sup>[2]</sup> should be sufficient to permit the police to search and thus act as a relinquishment of Alcala's constitutional right to exclude the police.<sup>[3]</sup> This Court has always scrutinized with great care claims that a person has forgone the opportunity to assert constitutional rights. See, <i>e. g., </i><i>Fuentes</i> v. <i>Shevin,</i> <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972); <i>D. H. Overmyer Co.</i> v. <i>Frick Co.,</i> <span class="citation" data-id="9424754"><a href="/opinion/108474/d-h-overmyer-co-inc-of-ohio-v-frick-co/" aria-description="Citation for case: D. H. Overmyer Co., Inc. of Ohio v. Frick Co.">405 U. S. 174</a></span> (1972); <i>Boykin</i> v. <i>Alabama,</i> <span class="citation" data-id="9424054"><a href="/opinion/107951/boykin-v-alabama/" aria-description="Citation for case: Boykin v. Alabama">395 U. S. 238</a></span> (1969); <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506</a></span> (1962). I see no reason to give the claim that a person consented to a search any less rigorous scrutiny. Every case in this Court involving this kind of search has heretofore spoken <span class="star-pagination">*279</span> of consent as a waiver.<sup>[4]</sup> See <i>e. g., </i><i>Amos</i> v. <i>United States,</i> <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/#317" aria-description="Citation for case: Amos v. United States">255 U. S. 313, 317</a></span> (1921); <i>Zap</i> v. <i>United States,</i> <span class="citation" data-id="104314"><a href="/opinion/104314/zap-v-united-states/#628" aria-description="Citation for case: Zap v. United States">328 U. S. 624, 628</a></span> (1946); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13</a></span> (1948).<sup>[5]</sup> Perhaps one skilled in linguistics <span class="star-pagination">*280</span> or epistemology can disregard those comments, but I find them hard to ignore.</p>
<p>To begin, it is important to understand that the opinion of the Court is misleading in its treatment of the issue here in three ways. First, it derives its criterion for determining when a verbal statement of assent to search operates as a relinquishment of a person's right to preclude entry from a justification of consent searches that is inconsistent with our treatment in earlier cases of exceptions to the requirements of the Fourth Amendment, and that is not responsive to the unique nature of the consent-search exception. Second, it applies a standard of voluntariness that was developed in a very different context, where the standard was based on policies different from those involved in this case. Third, it mischaracterizes our prior cases involving consent searches.</p>
<p></p>
<h2>A</h2>
<p>The Court assumes that the issue in this case is: what are the standards by which courts are to determine that consent is voluntarily given? It then imports into the law of search and seizure standards developed to decide entirely different questions about coerced confessions.<sup>[6]</sup></p>
<p>The Fifth Amendment, in terms, provides that no person "shall be compelled in any criminal case to be a witness against himself." Nor is the interest protected by the Due Process Clause of the Fourteenth Amendment any different. The inquiry in a case where a confession is challenged as having been elicited in an unconstitutional manner is, therefore, whether the behavior <span class="star-pagination">*281</span> of the police amounted to compulsion of the defendant.<sup>[7]</sup> Because of the nature of the right to be free of compulsion, it would be pointless to ask whether a defendant knew of it before he made a statement; no sane person would knowingly relinquish a right to be free of compulsion. Thus, the questions of compulsion and of violation of the right itself are inextricably intertwined. The cases involving coerced confessions, therefore, pass over the question of knowledge of that right as irrelevant, and turn directly to the question of compulsion.</p>
<p><i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), confirms this analysis. There the Court held that certain warnings must be given to suspects prior to their interrogation so that the inherently coercive nature of in-custody questioning would be diminished by the suspect's knowledge that he could remain silent. But, although those warnings, of course, convey information about various rights of the accused, the information is intended only to protect the suspect against acceding to the other coercive aspects of police interrogation. While we would not ordinarily think that a suspect could waive his right to be free of coercion, for example, we do permit suspects to waive the rights they are informed of by police warnings, on the belief that such information in itself sufficiently decreases the chance that a statement would be elicited by compulsion. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-

[...TRUNCATED 83133 of 203133 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
