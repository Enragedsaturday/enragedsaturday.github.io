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

## GROUP: content/cases/Marcus v. Search Warrant.md  (`case`, 5 assertions)

### content_page

```
---
title: Marcus v. Search Warrant
type: case
citation: "367 U.S. 717 (1961)"
parallel_cite: "81 S. Ct. 1708; 6 L. Ed. 2d 1127"
neutral_cite: 1961 U.S. LEXIS 813
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-06-19
docket: No. 225
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
  opinion_url: "https://www.courtlistener.com/opinion/106287/marcus-v-search-warrant-of-property/"
  cluster_id: 106287
  opinion_id: null
  identity_checked: true
lake:
  record_id: Marcus v. Search Warrant
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Particularity]]"
    role: Anchor
related:
  - "[[The Warrant Requirement]]"
  - "[[A Quantity of Copies of Books v. Kansas]]"
tags:
  - case
  - fourth-amendment
  - warrant-requirement
  - particularity
  - general-warrant
  - obscenity
  - first-amendment
holding: "Warrants to seize allegedly obscene publications that issue on a police officer's conclusory complaint, without any judicial scrutiny of the materials or a prior adversary hearing, and that leave the selection of what to seize to the executing officers' discretion, operate as general warrants and lack the safeguards the Constitution demands."
aliases:
  - Marcus v. Search Warrant
  - "Marcus v. Search Warrant of Property (1961)"
  - Marcus v. Search Warrant of Property at 104 East Tenth Street
---

# Marcus v. Search Warrant

*367 U.S. 717 (1961)* (No. 225) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 106287 → combined opinion 106287 (Brennan, J.; 367 U.S. 717, decided June 19, 1961). Full case name: Marcus v. Search Warrant of Property at 104 East Tenth Street, Kansas City, Missouri. Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*732`). S9 promotes. -->

## Background
On the strength of a single police officer's conclusory complaints that certain magazines were obscene, Missouri judges issued warrants authorizing their seizure. Officers then searched newsstands and a distributor and seized roughly 11,000 copies of some 280 publications, deciding item by item, on their own judgment, what to take. No judge examined the materials before issuing the warrants, and no adversary hearing on obscenity preceded the seizure. The publisher and distributors challenged the seizures.

## Issue
Whether Missouri's procedures for seizing allegedly obscene publications — warrants issued on a conclusory complaint, without judicial review of the materials or a prior adversary determination of obscenity, and leaving the choice of what to seize to the officers — satisfied the constitutional requirements governing searches and seizures.

## Rule
The Court held the warrants were, in effect, general warrants that delegated the seizure decision to the executing officers: "The warrants gave the broadest discretion to the executing officers; they merely repeated the language of the statute and the complaints, specified no publications, and left to the individual judgment of each of the many police officers involved the selection of such magazines as in his view constituted 'obscene . . . publications.'" — 367 U.S. at 732. ^pin-732

## Application
Because the warrants named no particular items and no judge had scrutinized the materials, each officer made ad hoc, on-the-spot decisions about what was obscene — the standardless discretion the [[Particularity|particularity]] requirement exists to prevent. That defect was especially grave where the seizures swept in presumptively protected expression, without any prior adversary hearing to separate protected from unprotected material. The procedures therefore lacked the safeguards due process demands to keep nonobscene material from being suppressed.

## Conclusion
The judgment was **reversed**. Brennan, J., delivered the opinion of the Court; Black, J. (joined by Douglas, J.), concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Marcus* is a **warrant-requirement anchor**: it enforces the [[Particularity|particularity]] command by condemning warrants that leave the choice of what to seize to the officer's discretion — the modern echo of the general-warrant abuses that produced the Fourth Amendment. Its First Amendment overlay — heightened procedural safeguards when the thing seized is expression — was developed in *[[A Quantity of Copies of Books v. Kansas]]* (1964) and *[[Roaden v. Kentucky]]* (1973). Teach it for the core lesson that a warrant must particularly describe what may be seized.

## Appears on
- [[Particularity]] — *Anchor*

## Sources
- [*Marcus v. Search Warrant of Property at 104 East Tenth Street, Kansas City, Missouri*, 367 U.S. 717 (1961)](https://www.courtlistener.com/opinion/106287/marcus-v-search-warrant/) — pinpoint: 732 (Brennan, J., for the Court; the CL opinion text carries the reporter star `*732` immediately before the quoted sentence). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6500d6554dd93317", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "367 U.S. 717 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 813", "official_citation_present": true, "parallel_cite": "81 S. Ct. 1708; 6 L. Ed. 2d 1127", "title": "Marcus v. Search Warrant", "year": "1961"}}
{"assertion_id": "180ecb827d26549e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Warrants to seize allegedly obscene publications that issue on a police officer's conclusory complaint, without any judicial scrutiny of the materials or a prior adversary hearing, and that leave the selection of what to seize to the executing officers' discretion, operate as general warrants and lack the safeguards the Constitution demands.", "title": "Marcus v. Search Warrant"}}
{"assertion_id": "a61f937fa6f30370", "dimension": "support", "kind": "home_role", "locator": {"home": "Particularity"}, "payload": {"home": "Particularity", "role": "Anchor", "title": "Marcus v. Search Warrant"}}
{"assertion_id": "8fff9a53c3d4b57b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Marcus v. Search Warrant", "varies_by_point": "false"}}
{"assertion_id": "f7e91dce31a08d1a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Marcus v. Search Warrant"}}
```

### lake record — Marcus v. Search Warrant

```json
{
  "schema_version": "s2.v1",
  "record_id": "Marcus v. Search Warrant",
  "status": "under_review",
  "identity": {
    "case_name": "Marcus v. Search Warrant of Property",
    "case_name_short": "Marcus",
    "case_name_full": "MARCUS Et Al. v. SEARCH WARRANT OF PROPERTY AT 104 EAST TENTH STREET, KANSAS CITY, MISSOURI, Et Al.",
    "input_case_name": "Marcus v. Search Warrant",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-06-19",
    "year": 1961,
    "docket": "No. 225",
    "cluster_id": 106287,
    "lead_opinion_id": 9422285,
    "sibling_ids": [],
    "absolute_url": "/opinion/106287/marcus-v-search-warrant-of-property/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "367 U.S. 717",
      "volume": "367",
      "reporter": "U.S.",
      "page": "717",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 1708",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1127",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 813",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "813",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "367 U.S. 717",
        "volume": "367",
        "reporter": "U.S.",
        "page": "717",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 1708",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "1708",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 L. Ed. 2d 1127",
        "volume": "6",
        "reporter": "L. Ed. 2d",
        "page": "1127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 813",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "813",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "367 U.S. 717",
    "official_selection": {
      "court_class": "scotus",
      "selected": "367 U.S. 717",
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
    "date_created": "2026-07-06T13:43:51Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:44:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "marcus-v-search-warrant--106287",
      "to_record_id": "Marcus v. Search Warrant",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Marcus v. Search Warrant

```
<opinion type="majority">
<author id="b754-10">Mr. Justice Brennan</author>
<p id="AU7">delivered the opinion of the Court.</p>
<p id="b754-11">This appeal presents the question whether due process under the Fourteenth Amendment was denied the appellants by the application in this case of Missouri’s procedures authorizing the search for and seizure of allegedly obscene publications preliminarily to their destruction by burning or otherwise if found by a court to be obscene. The procedures are statutory, but are supplemented by a rule of the Missouri Supreme Court.<footnotemark>1</footnotemark> The warrant for search for and seizure of obscene material issues on a sworn complaint filed with a judge or magis<page-number citation-index="1" label="719">*719</page-number>trate.<footnotemark>2</footnotemark> If the complainant states “positively and not upon information or belief,” or states “evidential facts from which such judge or magistrate determines the existence of probable cause” to believe that obscene material “is being held or kept in any place or in any building,” “such judge or magistrate shall issue a search warrant directed to any peace officer commanding him to search the place therein described and to seize and bring before such judge or magistrate the personal property therein described.” <footnotemark>3</footnotemark> The owner of the property is not afforded a <page-number citation-index="1" label="720">*720</page-number>hearing before the warrant issues; the proceeding is <em>ex parte. </em>However, the judge or magistrate issuing the warrant must fix a date, not less than five nor more than 20 days after the seizure, for a hearing to determine whether the seized material is obscene.<footnotemark>4</footnotemark> The owner of the material may appear at such hearing and defend <page-number citation-index="1" label="721">*721</page-number>against the charge.<footnotemark>5</footnotemark> No time limit' is provided within which the judge must announce his decision. If the judge finds that the material is obscene, he is required to order it to be publicly destroyed, by burning or otherwise; if he finds that it is not obscene, he shall order its return to its owner.<footnotemark>6</footnotemark></p>
<p id="b757-5">The Missouri Supreme Court sustained the validity of the procedures as applied in this case. <span class="citation" data-id="5024262"><a href="/opinion/5201171/search-warrant-of-property-at-5-west-12th-street-kansas-city-v-marcus/" aria-description="Citation for case: Search Warrant of Property at 5 West 12th Street, Kansas...">334 S. W. 2d 119</a></span>. The appellants brought this appeal here under <span class="citation no-link">28 U. S. C. § 1257</span> (2). We postponed consideration of the question of our jurisdiction to the hearing of the case on the merits. <span class="citation multiple-matches"><a href="/c/U.%20S./364/811/">364 U. S. 811</a></span>. We hold that the appeal is properly here, see <em>Dahnke-Walker Milling Co. </em>v. <em>Bondurant, </em><span class="citation" data-id="9418469"><a href="/opinion/99884/dahnke-walker-milling-co-v-bondurant/" aria-description="Citation for case: Dahnke-Walker Milling Co. v. Bondurant">257 U. S. 282</a></span>, and turn to the merits.</p>
<p id="b757-6">Appellant, Kansas City News Distributors, managed by appellant, Homer Smay, is a wholesale distributor of magazines, newspapers and books in the Kansas City area. The other appellants operate five retail newsstands <page-number citation-index="1" label="722">*722</page-number>in Kansas City. In October 1957, Police Lieutenant Coughlin of the Kansas City Police Department Vice Squad was conducting an investigation into the distribution of allegedly obscene magazines. On October 8, 1957, he visited Distributors’ place of business and showed Smay a list of magazines. Smay admitted that his company distributed all but one of the magazines on the list. The following day, October 9, Lieutenant Coughlin visited the five newsstands and purchased one magazine at each.<footnotemark>7</footnotemark> On October 10 the officer signed and filed six sworn complaints in the Circuit Court of Jackson County, stating in each complaint that “of his own knowledge” the appellant named therein, at its stated place of business, “kept for the purpose of [sale] . . . obscene . . . publications . . . .” No copy of any magazine on Lieutenant Coughlin’s list, or purchased by him at the newsstands, was filed with the complaint or shown to the circuit judge. The circuit judge issued six search warrants authorizing, as to the premises of the appellant named in each, “any peace officer in the State of Missouri . . . [to] search the said premises . . . within 10 days after the issuance of this warrant by day or night, and . . . seize . . . [obscene materials] and take same into your possession . . . .”</p>
<p id="b758-6">All of the warrants were executed on October 10, but by different law enforcement officers. Lieutenant Coughlin with two other Kansas City police officers, and an officer of the Jackson County Sheriff’s Patrol, executed the warrant against Distributors. Distributors’ stock of magazines runs “into hundreds of thousands . . . [p]robably closer to a million copies.” The officers examined the publications in the stock on the main floor of the establishment, <page-number citation-index="1" label="723">*723</page-number>not confining themselves to Lieutenant Coughlin’s original list. They seized all magazines which “[i]n our judgment” were obscene; when an officer thought “a magazine . . . ought to be picked up” he seized all copies of it. After three hours the examination was completed and the magazines seized were “hauled away in a truck and put on the 15th floor of the courthouse.” A substantially similar procedure was followed at each of the five newsstands. Approximately 11,000 copies of 280 publications, principally magazines but also some books and photographs, were seized at the six places.<footnotemark>8</footnotemark></p>
<p id="b759-5">The circuit judge fixed October 17 for the hearing, which was later continued to October 23. Timely motions were made by the appellants to quash the search warrants and to suppress as evidence the property seized, and for the immediate return of the property. The motions were rested on a number of grounds but we are concerned only with the challenge to the application of the procedures in the context of the protections for free speech and press assured against state abridgment by the Fourteenth Amendment.<footnotemark>9</footnotemark> Unconstitutionality in violation of the Fourteenth Amendment was asserted because the procedures as applied (1) allowed a seizure by police officers “without notice or any hearing afforded to the movants prior to seizure for the purpose of determining whether or not these . . . publications are ob<page-number citation-index="1" label="724">*724</page-number>scene . . .,” and (2) because they “allowed police officers and deputy sheriffs to decide and make a judicial determination after the warrant was issued as to which . . . magazines were . . . obscene . . . and were subject to seizure, impairing movants’ freedom of speech and publication.” The circuit judge reserved rulings on the motions and heard testimony of the police officers concerning the events surrounding the issuance and execution of the several warrants. On December 12, 1957, the circuit judge filed an unreported opinion in which he overruled the several motions and found that 100 of the 280 seized items were obscene. A judgment thereupon issued directing that the 100 items, and all copies thereof, “shall be retained by the Sheriff of Jackson County ... as necessary evidence for the purpose of possible criminal prosecution or prosecutions, and, when such necessity no longer exists, said Sheriff . . . shall publicly destroy the same by burning within thirty days thereafter”; it ordered further that the 180 items not found to be obscene, and all copies thereof, “shall be returned forthwith by the Sheriff ... to the rightful owner or owners . . . .”</p>
<p id="b760-4">I.</p>
<p id="b760-5">The use by government of the power of search and seizure as an adjunct to a system for the suppression of objectionable publications is not new. Historically the struggle for freedom of speech and press in England was bound up with the issue of the scope of the search and seizure power. See generally Siebert, Freedom of the Press in England, 1476-1776; Hanson, Government and the Press, 1695-1763. It was a principal instrument for the enforcement of the Tudor licensing system. The Stationers’ Company was incorporated in 1557 to help implement that system and was empowered “to make search whenever it shall please them in any place, shop, <page-number citation-index="1" label="725">*725</page-number>house, chamber, or building or any printer, binder or bookseller whatever within our kingdom of England or the dominions of the same of or for any books or things printed, or to be printed, and to seize, take hold, burn, or turn to the proper use of the foresaid community, all and several those books and things which are or shall be printed contrary to the form of any statute, act, or proclamation, made or to be made <em>. . . </em><footnotemark>10</footnotemark></p>
<p id="b761-5">An order of council confirmed and expanded the Company’s power in 1566,<footnotemark>11</footnotemark> and the Star Chamber reaffirmed it in 1586 by a decree “That it shall be lawful for the wardens of the said Company for the time being or any two of the said Company thereto deputed by the said wardens, to make search in all workhouses, shops, warehouses of printers, booksellers, bookbinders, or where they shall have reasonable cause of suspicion, and all books [etc.] . . . contrary to . . . these present ordinances to stay and take to her Majesty’s use . . . .”<footnotemark>12</footnotemark> Books thus seized were taken to Stationers’ Hall where they were inspected by ecclesiastical officers, who decided whether they should be burnt. These powers were exercised under the Tudor censorship to suppress both Catholic and Puritan dissenting literature.<footnotemark>13</footnotemark></p>
<p id="b761-6">Each succeeding regime during turbulent Seventeenth Century England used the search and seizure power to suppress publications. James I commissioned the ecclesiastical judges comprising the Court of High Commission “to enquire and search for ... all heretical, schismatical and seditious books, libels, and writings, <em>and all other books, pamphlets and portraitures offensive to the state or set forth without sufficient and lawful authority in that </em><page-number citation-index="1" label="726">*726</page-number><em>behalf, </em>. . . and the same books [etc.] and their printing-presses themselves likewise to seize <em>and so to order and dispose of them ... as they may not after serve or be employed for any such unlawful use .. ..” </em><footnotemark>14</footnotemark> The Star Chamber decree of 1637, re-enacting the requirement that all books be licensed, continued the broad powers of the Stationers' Company to enforce the licensing laws.<footnotemark>15</footnotemark> During the political overturn of the 1640’s Parliament on several occasions asserted the necessity of a broad search and seizure power to control printing. Thus an order of 1648 gave power to the searchers “to search in any house or place where there is just cause of suspicion, that Presses are kept and employed in the printing of Scandalous and lying Pamphlets, . . . [and] to seize such scandalous and lying pamphlets as they find upon search <em>. . . .” </em><footnotemark>16</footnotemark> The Restoration brought a new licensing act in 1662. Under its authority “messengers of the press” operated under the secretaries of state, who issued executive warrants for the seizure of persons and papers. These warrants, while sometimes specific in content, often gave the most general discretionary authority. For example, a warrant to Roger L’Estrange, the Surveyor of the Press, empowered him to “seize all seditious books and libels and to apprehend the authors, contrivers, printers, publishers, and dispersers of them,” and to “search any house, shop, printing room, chamber, warehouse, etc. for seditious, scandalous or unlicensed pictures, books, or papers, to bring away or deface the same, and the letter press, taking away all the copies . . . .” <footnotemark>17</footnotemark> Another warrant gave L’Estrange power to “search for <page-number citation-index="1" label="727">*727</page-number>&amp; seize authors, contrivers, printers, . . . publishers, dispensers, &amp; concealers of treasonable, schismaticall, seditious or unlicensed books, libells, pamphlets, or papers . . . together with all copys exemplaryes of such Books, libells, pamphlets or paper as aforesaid.” <footnotemark>18</footnotemark></p>
<p id="AV-M">Although increasingly attacked, the licensing system was continued in effect for a time even after the Revolution of 1688 and executive warrants continued to issue for the search for and seizure of offending books. The Stationers’ Company was also ordered “to make often and diligent searches in all such places you or any of you shall know or have any probable reason to suspect, and to seize all unlicensed, scandalous books and pamphlets . . . .” <footnotemark>19</footnotemark> And even when the device of prosecution for seditious libel replaced licensing as the principal governmental control of the press,<footnotemark>20</footnotemark> it too was enforced with the aid of general warrants — authorizing either the arrest of all persons connected with the publication of a particular libel and the search of their premises, or the seizure of all the papers of a named person alleged to be connected with the publication of a libel.<footnotemark>21</footnotemark></p>
<p id="b764-4"><page-number citation-index="1" label="728">*728</page-number>Enforcement through general warrants was finally judicially condemned in England. This was the consequence of the struggle of the 1760’s between the Crown and the opposition press led by John Wilkes, author and editor of the North Briton. From this struggle came the great case of <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, which this Court has called “one of the landmarks of English liberty.” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626</a></span>. A warrant based on a charge of seditious libel issued for the arrest of Entick, writer for an opposition paper, and for the seizure of all his papers. The officers executing the warrant ransacked Entick’s home for four hours and carted away great quantities of books and papers. Lord Camden declared the general warrant for the seizure of papers contrary to the common law, despite its long history. Camden said: “This power so assumed by the secretary of state is an execution upon all the party’s papers, in the first instance. His house is rifled; his most valuable secrets are taken out of his possession, before the paper for which he is charged is found to be criminal by any competent jurisdiction, and before he is convicted either of writing, publishing, or being concerned in the paper.” At 1064. Camden expressly dismissed the contention that such a warrant could be justified on the grounds that it was “necessary for the ends of government to lodge such a power with a state <em>officer; </em>and . . . better to prevent the publication before than to punish the offender afterwards.” At 1073. In <em>Wilkes </em>v. <em>Wood, </em>19 How. St. Tr. 1153, Camden also condemned the general warrants employed against John Wilkes for his publication of issue No. 45 of the North Briton. He declared that these warrants, calling for the arrest of unnamed persons connected with the alleged libel and seizure of their papers, amounted to a “discretionary power given to messengers to search wherever their suspicions may chance to fall. If such a power is <page-number citation-index="1" label="729">*729</page-number>truly invested in a secretary of state, and he can delegate this power, it certainly may affect the person and property of every man in this kingdom, and is totally subversive of the liberty of the subject.” <em>Id., </em>1167.<footnotemark>22</footnotemark></p>
<p id="b765-5">This history was, of course, part of the intellectual matrix within which our own constitutional fabric was shaped. The Bill of Rights was fashioned against the background of knowledge that unrestricted power of search and seizure could also be an instrument for stifling liberty of expression. For the serious hazard of suppression of innocent expression inhered in the discretion confided in the officers authorized to exercise the power.</p>
<p id="b765-6">II.</p>
<p id="b765-7">The question here is whether the use by Missouri in this case of the search and seizure power to suppress <page-number citation-index="1" label="730">*730</page-number>obscene publications involved abuses inimical to protected expression. We held in <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/#485" aria-description="Citation for case: Roth v. United States">354 U. S. 476, 485</a></span>,<footnotemark>23</footnotemark> that “obscenity is not within the area of constitutionally protected speech or press.” But in <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>itself we expressly recognized the complexity of the test of obscenity fashioned in that case, and the vital necessity in its application of safeguards to prevent denial of “the protection of freedom of speech and press for material which does not treat sex in a manner appealing to prurient interest.” <em>Id., </em>p. 488. We have since held that a State’s power to suppress obscenity is limited by the constitutional protections for free expression. In <em>Smith </em>v. <em>California, </em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/#155" aria-description="Citation for case: Smith v. California">361 U. S. 147, 155</a></span>, we said, “The existence of the State’s power to prevent the distribution of obscene matter does not mean that there can be no constitutional barrier to any form of practical exercise of that power,” inasmuch as “our holding in <em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">Roth</a></span> </em>does not recognize any state power to restrict the dissemination of books which are not obscene.” <em>Id., </em>p. 152. We therefore held that a State may not impose absolute criminal liability on a bookseller for the possession of obscene material, even if it may dispense with the element of <em>scienter </em>in dealing with such evils as impure food and drugs. We remarked the distinction between the cases: “There is no specific constitutional inhibition against making the distributors of food the strictest censors of their merchandise, but the constitutional guarantees of the freedom of speech and of the press stand in the way of imposing a similar requirement on the bookseller.” <em>Id., </em>pp. 152-153. The Missouri Supreme Court’s assimilation of obscene literature to gambling paraphernalia or other contraband for purposes of search and seizure does not therefore answer the appellants’ constitutional claim, but merely restates the issue <page-number citation-index="1" label="731">*731</page-number>whether obscenity may be treated in the same way. The authority to the police officers under the warrants issued in this case, broadly to seize “obscene . . . publications,” poses problems not raised by the warrants to seize “gambling implements” and “all intoxicating liquors” involved in the cases cited by the Missouri Supreme Court. <span class="citation" data-id="5024262"><a href="/opinion/5201171/search-warrant-of-property-at-5-west-12th-street-kansas-city-v-marcus/#125" aria-description="Citation for case: Search Warrant of Property at 5 West 12th Street, Kansas...">334 S. W. 2d, at 125</a></span>. For the use of these warrants implicates questions whether the procedures leading to their issuance and surrounding their execution were adequate to avoid suppression of constitutionally protected publications. “. . . [T]he line between speech unconditionally guaranteed and speech which may legitimately be regulated, suppressed, or punished is finely drawn. . . . The separation of legitimate from illegitimate speech calls for . . . sensitive tools . . . .” <em>Speiser </em>v. <em>Randall, </em><span class="citation" data-id="9421696"><a href="/opinion/105751/speiser-v-randall/#525" aria-description="Citation for case: Speiser v. Randall">357 U. S. 513, 525</a></span>.<footnotemark>24</footnotemark> It follows that, under the Fourteenth Amendment, a State is not free to adopt whatever procedures it pleases for dealing with obscenity as here involved without regard to the possible consequences for constitutionally protected speech.</p>
<p id="b767-5">We believe that Missouri’s procedures as applied in this case lacked the safeguards which due process demands to assure nonobscene material the constitutional protection to which it is entitled. Putting to one side the fact that no opportunity was afforded the appellants to elicit and contest the reasons for the officer’s belief, or otherwise to argue against the propriety of the seizure to the issuing judge, still the warrants issued on the strength <page-number citation-index="1" label="732">*732</page-number>of the conclusory assertions of a single police officer, without any scrutiny by the judge of any materials considered by the complainant to be obscene. The warrants gave the broadest discretion to the executing officers; they merely repeated the language of the statute and the complaints, specified no publications, and left to the individual judgment of each of the many police officers involved the selection of such magazines as in his view constituted “obscene . . . publications.” So far as appears from the record, none of the officers except Lieutenant Coughlin had previously examined any of the publications which were subsequently seized. It is plain that in many instances, if not in all, each officer actually made <em>ad hoc </em>decisions on the spot and, gauged by the number of publications seized and the time spent in executing the warrants, each decision was made with little opportunity for reflection and deliberation. As to publications seized because they appeared on the Lieutenant’s list, we know nothing of the basis for the original judgment that they were obscene. It is no reflection on the good faith or judgment of the officers to conclude that the task they were assigned was simply an impossible one to perform with any realistic expectation that the obscene might be accurately separated from the constitutionally protected. They were provided with no guide to the exercise of informed discretion, because there was no step in the procedure before seizure designed to focus searchingly on the question of obscenity. See generally 1 Chafee, Government and Mass Communications, pp. 200-218. In consequence there were suppressed and withheld from the market for over two months 180 publications not found obscene.<footnotemark>25</footnotemark> The fact that only one-third of the <page-number citation-index="1" label="733">*733</page-number>publications seized were finally condemned strengthens the conclusion that discretion to seize allegedly obscene materials cannot be confided to law enforcement officials without greater safeguards than were here operative. Procedures which sweep so broadly and with so little discrimination are obviously deficient in techniques required by the Due Process Clause of the Fourteenth Amendment to prevent erosion of the constitutional guarantees.<footnotemark>26</footnotemark></p>
<p id="b770-5"><page-number citation-index="1" label="734">*734</page-number>III.</p>
<p id="b770-6">The reliance of the Missouri Supreme Court upon <em>Kingsley Books, Inc., </em>v. <em>Brown, </em><span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/" aria-description="Citation for case: Kingsley Books, Inc. v. Brown">354 U. S. 436</a></span>, is misplaced. The differences in the procedures under the New York statute upheld in that case and the Missouri procedures as applied here are marked. They amount to the distinction between “a 'limited injunctive remedy,’ under closely defined procedural safeguards, against the sale and distribution of written and printed matter found after due trial to be obscene,” <span class="citation" data-id="9421490"><a href="/opinion/105544/kingsley-books-inc-v-brown/#437" aria-description="Citation for case: Kingsley Books, Inc. v. Brown"><em>Kingsley Books, supra, </em>at 437</a></span>, and a scheme which in operation inhibited the circulation of publications indiscriminately because of the <page-number citation-index="1" label="735">*735</page-number>absence of any such safeguards. <em>First, </em>the New York injunctive proceeding was initiated by a complaint filed with the court which charged that a particular named obscene publication had been displayed, and to which were annexed copies of the publication alleged to be obscene.<footnotemark>27</footnotemark> The court, in restraining distribution pending final judicial determination of the claim, thus had the allegedly obscene material before it and could exercise an independent check on the judgment of the prosecuting authority at a point before any restraint took place. <em>Second, </em>the restraints in <em>Kingsley Books, </em>both temporary and permanent, ran only against the named publication ; no catchall restraint against the distribution of all “obscene” material was imposed on the defendants there, comparable to the warrants here which authorized a mass seizure and the removal of a broad range of items from circulation.<footnotemark>28</footnotemark> <em>Third, Kingsley Books </em>does not support the proposition that the State may impose the extensive <page-number citation-index="1" label="736">*736</page-number>restraints imposed here on the distribution of these publications prior to an adversary proceeding on the issue of obscenity, irrespective of whether or not the material is legally obscene. This Court expressly noted there that the State was not attempting to punish the distributors for disobedience of any interim order entered before hearing. The Court pointed out that New York might well construe its own law as not imposing any punishment for violation of an interim order were the book found not obscene after due trial. 354 U. S., at 443, n. 2. But there is no doubt that an effective restraint — indeed the most effective restraint possible — was imposed prior to hearing on the circulation of the publications in this case, because all copies on which the police could lay their hands were physically removed from the newsstands and from the premises of the wholesale distributor. An opportunity comparable to that which the distributor in <em>Kingsley Books </em>might have had to circulate the publication despite the interim restraint and then raise the claim of nonobscenity by way of defense to a prosecution for doing so was never afforded these appellants because the copies they possessed were taken away. Their ability to circulate their publications was left to the chance of securing other copies, themselves subject to mass seizure under other such warrants. The public’s opportunity to obtain the publications was thus determined by the distributor’s readiness and ability to outwit the police by obtaining and selling other copies before they in turn could be seized. In addition to its unseemliness, we do not believe that this kind of enforced competition affords a reasonable likelihood that nonobscene publications, entitled to constitutional protection, will reach the public. A distributor may have every reason to believe that a publication is constitutionally protected and will be so held after judicial hearing, but his belief is unavailing as against the contrary judgment of <page-number citation-index="1" label="737">*737</page-number>the police officer who seizes it from him.<footnotemark>29</footnotemark> Finally, a subdivision of the New York statute in <em>Kingsley Books </em>required that a judicial decision on the merits of obscenity be made within two days of trial, which in turn was required to be within one day of the joinder of issue on the request for an injunction.<footnotemark>30</footnotemark> In contrast, the Missouri statutory scheme drawn in question here has no limitation on the time within which decision must be made, only a provision for rapid trial of the issue of obscenity. And in fact over two months elapsed between seizure and decision.<footnotemark>31</footnotemark> In these circumstances the restraint on the circu<page-number citation-index="1" label="738">*738</page-number>lation of publications was far more thoroughgoing and drastic than any restraint upheld by this Court in <em>Kingsley Books.</em></p>
<p id="b774-6">Mass seizure in the fashion of this case was thus effected without any safeguards to protect legitimate expression. The judgment of the Missouri Supreme Court sustaining the condemnation of the 100 publications therefore cannot be sustained. We have no occasion to reach the question of the correctness of the finding that the publications are obscene. Nor is it necessary for us to decide in this case whether Missouri lacks all power under its statutory scheme to seize and condemn obscene material. Since a violation of the Fourteenth Amendment infected the proceedings, in order to vindicate appellants’ constitutional rights the judgment is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b774-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b754-12"> These procedures are separate from and in addition to the State’s criminal statutes. See <em>State </em>v. <em>Mac Sales Co., </em><span class="citation" data-id="1484628"><a href="/opinion/1484628/state-v-mac-sales-co/" aria-description="Citation for case: State v. Mac Sales Co.">263 S. W. 2d 860</a></span>. The criminal statutes are Mo. Rev. Stat., §§563.270, 563.280, 563.290; see also § 563.310.</p>
</footnote>
<footnote label="2">
<p id="b755-5"> Mo. Rev. Stat., §542.380, in pertinent part provides:</p>
<p id="b755-6">“Upon complaint being made, on oath, in writing, to any officer authorized to issue process for the apprehension of offenders, that any of the property or articles herein named are kept within the county of such officer, if he shall be satisfied that there is reasonable ground for such complaint, shall issue a warrant to the sheriff or any constable of the county, directing him to search for and seize any of the following property or articles:</p>
<p id="b755-7">“(2) Any of the following articles, kept for the purpose of being sold, published, exhibited, given away or otherwise distributed or circulated, viz.: obscene, lewd, licentious, indecent or lascivious books, pamphlets, ballads, papers, drawings, lithographs, engravings, pictures, models, casts, prints or other articles or publications of an indecent, immoral or scandalous character, or any letters, handbills, cards, circulars, books, pamphlet's or advertisements or notices of any kind giving information, directly or indirectly, when, where, how or of whom any of such things can be obtained.” These procedures also govern seizure and condemnation of gambling paraphernalia, contraceptive devices, and tools and other articles used to manufacture or produce such items. Fraudulent, forged, and counterfeited writings and other articles, and the instruments used to make them, are also declared contraband and subject to seizure. § 542.440.</p>
</footnote>
<footnote label="3">
<p id="b755-8"> Missouri Supreme Court Rule 33.01 of the Rules of Criminal Procedure provides:</p>
<p id="b755-9">“(a) If a complaint in writing be filed with the judge or magistrate of any court having original jurisdiction to try criminal offenses stating that personal property . . . the seizure of which under search warrant is now or may hereafter be authorized by any statute of this <page-number citation-index="1" label="720">*720</page-number>State, is being held or kept at any place or in any building . . . within the territorial jurisdiction of such judge or magistrate, and if such complaint be verified by the oath or affirmation of the complainant and states such facts positively and not upon information or belief; or if the same be supported by written affidavits verified by oath or affirmation stating evidential facts from which such judge or magistrate determines the existence of probable cause, then such judge or magistrate shall issue a search warrant directed to any peace officer commanding him to search the place therein described and to seize and bring before such judge or magistrate the personal property therein described.</p>
<p id="b756-8">“ (b) The complainant and the warrant issued thereon must contain a description of the personal property to be searched for and seized and a description of the place to be searched, in sufficient detail and particularity to enable the officer serving the warrant to readily ascertain and identify the same.”</p>
</footnote>
<footnote label="4">
<p id="b756-9"> Mo. Rev. Stat., §542.400 provides:</p>
<p id="b756-10">“The judge or magistrate issuing the warrant shall set a day, not less than five days nor more than twenty days after the date of such service and seizure, for determining whether such property is the kind of property mentioned in section 542.380, and shall order the officer having such property in charge to retain possession of the same until after such hearing. Written notice of the date and place of such hearing shall be given, at least five days before such date, by posting a copy of such notice in a conspicuous place upon the premises in which such property is seized, and by delivering a copy of such notice to any person claiming an interest in such property, whose name may be known to the person making the complaint or to the officer'issuing or serving such warrant, or leaving the same at the usual place of abode of such person with any member of his family or household above the age of fifteen years. Such notice shall be signed by the magistrate or judge or by the clerk of the court of such judge.”</p>
</footnote>
<footnote label="5">
<p id="b757-7"> Mo. Rev. Stat., § 542.410 provides:</p>
<p id="b757-8">“Rights of property owner. — The owner or owners of such property may appear at such hearing and defend against the charges as to the nature and use of the property so seized, and such judge or magistrate shall determine, from the evidence produced at such hearing, whether the property is the kind of property m'entioned in section 542.380.”</p>
</footnote>
<footnote label="6">
<p id="b757-9"> Mo. Rev. Stat., § 542.420 provides:</p>
<p id="b757-10">“Disposition of property. — If the judge or magistrate hearing such cause shall determine that the property or articles are of the kind mentioned in section 542.380, he shall cause the same to be publicly destroyed, by burning or otherwise, and if he find that such property is not of the kind mentioned, he shall order the same returned to its owner. If it appears that it may be necessary to use such articles or property as evidence in any criminal prosecution, the judge or magistrate shall order the officer having possession of them to retain such possession until such necessity no longer exists, and they shall neither be destroyed nor returned to the owner until they are no longer needed as such evidence.”</p>
</footnote>
<footnote label="7">
<p id="b758-7"> He bought a copy of the same magazine at three of the stands, a copy of another edition of this magazine at a fourth stand, and a copy of one other magazine at the fifth stand;</p>
</footnote>
<footnote label="8">
<p id="b759-6"> The publications seized included so-called “girlie” magazines, nudist magazines, treatises and manuals on sex, photography magazines, cartoon and joke books and still photographs.</p>
</footnote>
<footnote label="9">
<p id="b759-7"> Because of the result which we reach, it is unnecessary to decide other constitutional questions raised by the appellants, (1) whether the Missouri statutes are invalid on their face as authorizing an unconstitutional censorship and previous restraint of publications; (2) whether the Missouri courts applied an unconstitutional test of obscenity; and (3) whether the publications condemned are obscene under the test of <em>Roth </em>v. <em>United States, </em><span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/" aria-description="Citation for case: Roth v. United States">354 U. S. 476</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b761-7"> 1 Arber, Transcript of the Registers of the Company of Stationers of London, 1554 — 1640 A. D., p. xxxi.</p>
</footnote>
<footnote label="11">
<p id="b761-8"> Elton, The Tudor Constitution, p. 106.</p>
</footnote>
<footnote label="12">
<p id="b761-9"> Elton, <em>supra, </em>pp. 182-183.</p>
</footnote>
<footnote label="13">
<p id="b761-10"> Siebert, <em>supra, </em>pp. 83, 85-86, 97.</p>
</footnote>
<footnote label="14">
<p id="b762-6"> Siebert, <em>supra, </em>p. 139, citing Pat. Roll, 9 Jac. I, Pt. 18; <em>id., </em>II, Pt. 15.</p>
</footnote>
<footnote label="15">
<p id="b762-7"> 4 Arber, <em>supra, </em>pp. 529-536.</p>
</footnote>
<footnote label="16">
<p id="b762-8"> Siebert, <em>supra, </em>214-215, note 72.</p>
</footnote>
<footnote label="17">
<p id="b762-9"> Siebert, <em>supra, </em>p. 254, citing Minute Entry Book 5, p. 177.</p>
</footnote>
<footnote label="18">
<p id="b763-5"> Siebert, <em>supra, </em>p. 256, citing Entry Book, Chas. II, 1664, Vol. 21, p. 21; also Vol. 16, p. 130.</p>
</footnote>
<footnote label="19">
<p id="b763-6"> Cal. St. P., Dom. Ser., 1690-1691, p. 74.</p>
</footnote>
<footnote label="20">
<p id="b763-7"> One of the primary objections to licensing was its enforcement through search and seizure. The House of Commons’ list of reasons why the licensing act should not be renewed included: “Because that Act subjects all Mens Houses, as well Peers as Commoners, to be searched at any Time, either by Day or Night, by a Warrant under the Sign Manual, or under the Hand of One of the Secretaries of State, directed to any Messenger, if such Messenger shall upon probable Reason suspect that there are any unlicensed Books there; and the Houses of all Persons free of the Company of Stationers are subject to the like Search, on a Warrant from the Master and Wardens of the said Company, or any One of them.” 15 Journals of the House of Lords, April 18, 1695, p. 546.</p>
</footnote>
<footnote label="21">
<p id="b763-8"> Siebert, <em>supra, </em>pp. 374 — 376.</p>
</footnote>
<footnote label="22">
<p id="b765-8"> A contemporary London pamphlet summed up the widespread indignation against the use of the general warrant for the seizure of papers: “In such a party-crime, as a public libel, who can endure this assumed authority of taking all papers indiscriminately? . . . where there is even a charge against one particular paper, to seize <em>all, </em>of every kind, is extravagant, unreasonable and inquisitorial. It is infamous in theory, and downright tyranny and despotism in practice.” Father of Candor, A Letter Concerning Libels, Warrants, and the Seizure of Papers, p. 48 (2d ed. 1764, J. Almon printer).</p>
<p id="b765-9">See generally Lasson, The History and Development of the Fourth Amendment, pp'. 42-50; Hanson, Government and the Press, 1695-1763, pp. 29-32, 49-50. An even broader form of general warrant was the writ of assistance, which met such vigorous opposition in the American Colonies prior to the Revolution. Unlike the warrants of the North Briton affair and <em>Entick </em>v. <em>Carrington, </em>which were at least concerned with a particular designated libel, these writs empowered the executing officer to seize any illegally imported goods or merchandise. Moreover, in addition to authorizing search without limit of place, they had no fixed duration. In effect, complete discretion was given to the executing officials; in the words of James Otis, their use placed “the liberty of every man in the hands of every petty officer.” Tudor, Life of James Otis (1823), p. 66. See Lasson, <em>supra, </em>pp. 51-78.</p>
</footnote>
<footnote label="23">
<p id="b766-6"> This holding applied also to the obscenity question raised under the Fourteenth Amendment in <em>Alberts </em>v. <em><span class="citation" data-id="9421895"><a href="/opinion/105972/smith-v-california/" aria-description="Citation for case: Smith v. California">California</a></span>, </em>decided in the same opinion.</p>
</footnote>
<footnote label="24">
<p id="b767-6"> Lord Camden in <em>Entick </em>v. <em>Carrington </em>recognized that there was no justification for the abuse of the search and seizure power in suppressing seditious libel, even if the view were accepted that “men ought not to be allowed to have such evil instruments in their keeping.” 19 How. St. Tr., at 1072. He said, “If [libels may be seized], I am afraid, that all the inconveniences of a general seizure will follow upon a right allowed to seize a part. The search in such cases will be general, and every house will fall under the power of a secretary of state to be rummaged before proper conviction.” <em>Id.., </em>at 1071.</p>
</footnote>
<footnote label="25">
<p id="b768-6"> Among the publications ordered returned were such titles as “The Dawn of Rational Sex Ethics,” “Sex Symbolism,” “Notes on Cases of Sexual Suppression,” “Your Affections, Emotions and Feel<page-number citation-index="1" label="733">*733</page-number>ings,” “Sexual Impotence, Its Causes and Treatments,” “The Psychology of Sex Life,” “Freud on Sleep and Sexual Dreams,” “The Determination of Sex,” “Sex and Psychoanalysis,” “Artificial Insemination,” “Syphilis, A Treatise for the American Public,” “What You Should Know About Sexual Impotency,” “Variations in Sexual Behavior,” “Sex Life in Marriage,” “Psychopathia Sexualis,” “The Sex Technique in Marriage,” “Sexual Deviations,” “Sex Practice in Later Years,” and “Marriage, Sex, and Family Problems.”</p>
</footnote>
<footnote label="26">
<p id="b769-5"> English practice in such cases has placed greater restraint on the seizure power. Seizure of obscene material, as a prelude to condemnation, was authorized there by Lord Campbell’s Obscene Publications Act of 1857, 20 &amp; 21 Vict., c. 83. As originally proposed, that statute would have allowed search for and seizure of obscene matter either under authority granted by magistrates or on warrants granted by the Chief Commissioner of Police. Moreover, the affidavit for obtaining a warrant would have been required to contain merely the statement that the person making it had reasonable ground for suspicion that obscene publications were kept on the premises to be searched. See 146 Hansard’s Parliamentary Debates, 3d Series, p. 866. These provisions met vigorous opposition in Parliament. A number of members emphasized that the difficulty of defining obscenity made broad search powers in police hands extremely dangerous. See <em>id., </em>pp. 330-332, 1360-1362, 147 Hansard, <em>supra, </em>pp. 1863-1864. As a result, amendments were adopted removing the grant of authority to the police commissioner to authorize a search and seizure, requiring greater specificity in the allegations before a warrant could be issued, and providing that warrants could issue only for the seizure of books the publication of which would constitute a common-law misdemeanor. Lord Lyndhurst, draftsman of these amendments, explained: “I have now provided that the person shall swear that he has reason to believe, and that he does believe, that there are such publications in <page-number citation-index="1" label="734">*734</page-number>such a place, and shall further state to the magistrate the reasons which lead to that belief. Nor does it stop there. The most material Amendment is, that he must state what the publications are, and that they are of such a nature that, if published, the party publishing them will be guilty of a misdemeanour. The magistrate must also be satisfied that the case is a proper one for a prosecution 146 Hansard, <em>supra, </em>at p. 1360. The Lord Chancellor summarized the effect of the changes: “As the Bill now stood, these search-warrants would only be granted after great precautions . . . .” <em>Id., </em>p. 1362.</p>
<p id="b770-8">According to a recent summary of procedures to obtain a warrant under that Act, a police officer would ordinarily buy copies of a work he suspected of obscenity. They would be examined by the police and sent to the Director of Public Prosecutions. The latter would return them with advice as to whether a warrant should be applied for. If a decision were made to seek a warrant, the publications would be laid before a magistrate with the sworn affidavit of the officer, in order that he might be satisfied that they were of the character necessary to justify seizure. See Memorandum of the Association of Chief Police Officers of England and Wales, Minutes of Evidence Taken Before the Select Committee of the House of Commons on the Obscene Publications Bill, 1956-1957, pp. 132-136. See also, <em>id., </em>p. 23.</p>
<p id="b770-9">The Act was replaced by the Obscene Publications Act of 1959, 7 &amp; 8 Eliz. II, c. 66. See 23 Mod. L. Bev. 285.</p>
</footnote>
<footnote label="27">
<p id="b771-5"> The feasibility of particularization in complaint and warrant in a ease such as the present is apparent, since the publications were sold on newsstands distributing to the public. Compare Lord Camden’s remark in <em>Entick </em>v. <em>Carrington, </em>directed to the contention that a general warrant might be justifiable as a means of uncovering evidence of crime: “If ... a right of search for the sake of discovering evidence ought in any case to be allowed, this crime [seditious libel] above all others ought to be excepted, as wanting such a discovery less than any other. It is committed in open daylight, and in the face of the world; . . .” 19 How. St. Tr., at 1074.</p>
</footnote>
<footnote label="28">
<p id="b771-6"> The trial judge in <em>Kingsley Books </em>refused to enjoin the distribution of future issues of the publication in question, stating: “[u]nless the work be before the court at the time of the hearing at which the injunction is sought, it is inappropriate to make a judicial determination with respect to it. In respect of this feature of the case, the plaintiff seeks a likely trespass upon a constitutionally protected area, and the court must reject that prayer.” <span class="citation" data-id="5432110"><a href="/opinion/5589878/burke-v-kingsley-books-inc/#168" aria-description="Citation for case: Burke v. Kingsley Books, Inc.">208 Misc. 150, 168-169</a></span>, 142 N. Y. S. 2d 735, 751. Cf. <em>Near </em>v. <em>Minnesota ex rel. Olson, </em><span class="citation" data-id="9418724"><a href="/opinion/101773/near-v-minnesota-ex-rel-olson/" aria-description="Citation for case: Near v. Minnesota Ex Rel. Olson">283 U. S. 697</a></span>.</p>
</footnote>
<footnote label="29">
<p id="b773-4"> Cf. Freund, The Supreme Court and Civil Liberties, <span class="citation no-link">4 Vand. L. Rev. 533</span>, 539.</p>
<p id="b773-5">Blackstone’s often-quoted formulation of the principle of freedom of the press, though restricted to the prohibition of <em>“previous </em>restraints upon publications,” nevertheless acknowledged the importance of an adjudicatory procedure as a protection against the suppression of inoffensive publications. He wrote: “to punish (as the law does at present) any dangerous or offensive writings, which, when published, shall <em>on a fair and impartial trial be adjudged of a pernicious tendency, </em>is necessary for the preservation of peace and good order . . . .” 4 Commentaries, pp. 151-152. (Emphasis added.) Compare Butler, J., dissenting in <em>Near </em>v. <em>Minnesota ex rel. <span class="citation" data-id="9418724"><a href="/opinion/101773/near-v-minnesota-ex-rel-olson/" aria-description="Citation for case: Near v. Minnesota Ex Rel. Olson">Olson, supra,</a></span> </em>p. 723: “The decision of the Court in this case declares Minnesota and every other State powerless to restrain by injunction the business of publishing and circulating among the people malicious, scandalous and defamatory periodicals that <em>in due course of judicial procedure has been adjudged to be a public nuisance.’’ </em>(Emphasis added.)</p>
</footnote>
<footnote label="30">
<p id="b773-6"> This provision was not directly implicated in <em>Kingsley Books </em>because the parties had waived the provision for immediate trial.</p>
</footnote>
<footnote label="31">
<p id="b773-7"> Compare the objection of the House of Commons to renewal of licensing: “Because that Act appoints no Time wherein the Archbishop, or Bishop of London, shall appoint a learned Man, or that One or more of the Company of Stationers shall go to the Customhouse, to view imported Books; so that they or either of them may delay it till the Importer may be undone, by having so great a Part of his Stock lie dead . . . .” 15 Journals of the House of Lords, April 18, 1695, p. 546.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Maryland v. Buie.md  (`case`, 5 assertions)

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
{"assertion_id": "6f1486a5cba42cb0", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "494 U.S. 325 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 1176", "official_citation_present": true, "parallel_cite": "110 S. Ct. 1093; 108 L. Ed. 2d 276", "title": "Maryland v. Buie", "year": "1990"}}
{"assertion_id": "cb600265914abf80", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Protective sweep incident to an in-home arrest: (1) without probable cause or reasonable suspicion, officers may as a precaution look in…", "title": "Maryland v. Buie"}}
{"assertion_id": "f27fc0f2b7d1ed12", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Key — Anchor", "title": "Maryland v. Buie"}}
{"assertion_id": "1c9e644963b88321", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Maryland v. Buie"}}
{"assertion_id": "a65fa48328f6b04f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-03-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Maryland v. Buie", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Maryland v. Buie", "varies_by_point": "false"}}
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

## GROUP: content/cases/Massiah v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Massiah v. United States"
type: case
citation: "377 U.S. 201 (1964)"
parallel_cite: "84 S. Ct. 1199; 12 L. Ed. 2d 246"
neutral_cite: 1964 U.S. LEXIS 1277
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-05-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-05-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Massiah v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106822/massiah-v-united-states/"
  cluster_id: 106822
  opinion_id: 106822
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Anchor"
related: ["[[Maine v. Moulton]]", "[[Kuhlmann v. Wilson]]", "[[Brewer v. Williams]]", "[[United States v. Henry]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "deliberate-elicitation", "post-indictment"]
holding: "Once adversary proceedings have begun (here, post-indictment), the government violates the Sixth Amendment when it deliberately elicits…"
lake:
  record_id: Massiah v. United States
  status: verified
  projected_at: 2026-07-06
---

# Massiah v. United States

*377 U.S. 201 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Massiah was indicted on federal narcotics charges, retained counsel, and was released on bail. A codefendant, Colson, agreed to cooperate with federal agents and let them install a radio transmitter in his car. Colson then drew Massiah into an incriminating conversation, which an agent overheard by radio. The statements were used against Massiah at trial.

## Issue
Whether the government may use against a defendant at trial his own incriminating statements, deliberately elicited by government agents after indictment and outside the presence of his counsel.

## Rule
No — such deliberate post-indictment elicitation violates the Sixth Amendment. "We hold that the petitioner was denied the basic protections of that guarantee when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel." — 377 U.S. at 206. ^pin-206

The rule reaches indirect and surreptitious interrogations, not just questioning in a police station.

## Application
By the time of the recorded conversation, Massiah had been indicted and had retained counsel, so his Sixth Amendment right had attached. The federal agents, acting through the cooperating codefendant and the hidden transmitter, deliberately elicited incriminating statements from him without counsel present — indeed, without his even knowing he was being interrogated. Using those statements against him at trial denied him the assistance of counsel the Sixth Amendment guarantees.

## Conclusion
Reversed: incriminating statements deliberately elicited from an indicted, represented defendant outside the presence of counsel cannot be used against him at trial.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Massiah* is the foundation of the Sixth Amendment "deliberate elicitation" doctrine, later refined by [[Maine v. Moulton]] (knowing exploitation) and [[Kuhlmann v. Wilson]] (action beyond mere listening), and applied in [[Brewer v. Williams]] and [[United States v. Henry]]. It remains good law.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Anchor*

## Sources
- *Massiah v. United States*, 377 U.S. 201 (1964) — https://www.courtlistener.com/opinion/106822/massiah-v-united-states/ — pinpoint: 206.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "5563fa3028ca7800", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "377 U.S. 201 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 1277", "official_citation_present": true, "parallel_cite": "84 S. Ct. 1199; 12 L. Ed. 2d 246", "title": "Massiah v. United States", "year": "1964"}}
{"assertion_id": "48a28de4eacff3dc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Once adversary proceedings have begun (here, post-indictment), the government violates the Sixth Amendment when it deliberately elicits…", "title": "Massiah v. United States"}}
{"assertion_id": "57c6df118a1d66a6", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Anchor", "title": "Massiah v. United States"}}
{"assertion_id": "d230960c5ebb4962", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-05-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Massiah v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Massiah v. United States", "varies_by_point": "false"}}
{"assertion_id": "df8e0fda60168341", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Massiah v. United States"}}
```

### lake record — Massiah v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Massiah v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Massiah v. United States",
    "case_name_short": "Massiah",
    "case_name_full": "Massiah v. United States",
    "input_case_name": "Massiah v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-05-18",
    "year": 1964,
    "docket": null,
    "cluster_id": 106822,
    "lead_opinion_id": 106822,
    "sibling_ids": [
      106822,
      9422796,
      9422797
    ],
    "absolute_url": "/opinion/106822/massiah-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "377 U.S. 201",
      "volume": "377",
      "reporter": "U.S.",
      "page": "201",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1199",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 246",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 1277",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1277",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "377 U.S. 201",
        "volume": "377",
        "reporter": "U.S.",
        "page": "201",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1199",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1199",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 246",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 1277",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "1277",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "377 U.S. 201",
    "official_selection": {
      "court_class": "scotus",
      "selected": "377 U.S. 201",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-206",
      "page": null,
      "quote": "--- # Massiah v. United States *377 U.S. 201 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Massiah was indicted on federal narcotics charges, retained counsel, and was released on bail. A codefendant, Colson, agreed to cooperate with federal agents and let them install a radio transmitter in his car. Colson then drew Massiah into an incriminating conversation, which an agent overheard by radio. The statements were used against Massiah at trial. ## Issue Whether the government may use against a defendant at trial his own incriminating statements, deliberately elicited by government agents after indictment and outside the presence of his counsel. ## Rule No \u2014 such deliberate post-indictment elicitation violates the Sixth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-05-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Massiah v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Bateman",
          "cluster_id": 9413757,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Benton",
          "cluster_id": 10134904,
          "cite": [
            "317 Or. App. 384",
            "505 P.3d 975"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
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
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Justin Barrett Blakeney v. State of Mississippi",
          "cluster_id": 4442047,
          "cite": [
            "236 So. 3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zackary Stewart v. Karl Wagner",
          "cluster_id": 4255669,
          "cite": [
            "836 F.3d 978",
            "2016 U.S. App. LEXIS 16642",
            "2016 WL 4728039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended September 20, 2016 State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 4472001,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 3218790,
          "cite": [
            "882 N.W.2d 68",
            "2016 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Alexander Marshall",
          "cluster_id": 2806802,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fischer v. Smith",
          "cluster_id": 8442138,
          "cite": [
            "780 F.3d 556",
            "2015 U.S. App. LEXIS 4195",
            "2015 WL 1186845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Taylor",
          "cluster_id": 7306221,
          "cite": [
            "17 F. Supp. 3d 162",
            "2014 WL 1653194",
            "2014 U.S. Dist. LEXIS 57397"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane1_negative"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Padilla v. Kentucky",
          "cluster_id": 1723,
          "cite": [
            "176 L. Ed. 2d 284",
            "130 S. Ct. 1473",
            "559 U.S. 356",
            "2010 U.S. LEXIS 2928"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sawyer v. Whitley",
          "cluster_id": 112773,
          "cite": [
            "120 L. Ed. 2d 269",
            "112 S. Ct. 2514",
            "505 U.S. 333",
            "1992 U.S. LEXIS 3864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
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
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuhlmann v. Wilson",
          "cluster_id": 111726,
          "cite": [
            "91 L. Ed. 2d 364",
            "106 S. Ct. 2616",
            "477 U.S. 436",
            "1986 U.S. LEXIS 65",
            "54 U.S.L.W. 4809"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rushen v. Spain",
          "cluster_id": 111051,
          "cite": [
            "78 L. Ed. 2d 267",
            "104 S. Ct. 453",
            "464 U.S. 114",
            "1983 U.S. LEXIS 11",
            "52 U.S.L.W. 3452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Massiah v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106822 OR 9422796 OR 9422797) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzA2MjgxNjAwMDAwJnM9MjcwNjU3NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106822+OR+9422796+OR+9422797%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(106822 OR 9422796 OR 9422797)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03OTAmcz00ODAzNjAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106822+OR+9422796+OR+9422797%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106822 OR 9422796 OR 9422797)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 1,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106822 OR 9422796 OR 9422797)",
    "indexed_citing_opinions": 2146,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106822,
        "count": 1988,
        "count_source": "search"
      },
      {
        "opinion_id": 9422796,
        "count": 206,
        "count_source": "search"
      },
      {
        "opinion_id": 9422797,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3189,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/massiah-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzMDk1NiZzPTk0MDYyOTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28106822+OR+9422796+OR+9422797%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106822,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 100989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 104079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 258052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 262616,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106822,
        "cited_id": 1236300,
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
    "date_created": "2026-07-05T12:23:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T12:26:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:23:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Massiah v. United States

```
<div>
<center><b><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U.S. 201</a></span> (1964)</b></center>
<center><h1>MASSIAH<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 199.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 3, 1964.</center>
<center>Decided May 18, 1964.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Robert J. Carluccio</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Solicitor General Cox</i> argued the cause for the United States. With him on the brief were <i>Assistant Attorney General Miller</i> and <i>Jerome Nelson.</i></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner was indicted for violating the federal narcotics laws. He retained a lawyer, pleaded not guilty, and was released on bail. While he was free on bail a federal agent succeeded by surreptitious means in listening to incriminating statements made by him. Evidence of these statements was introduced against the petitioner at his trial over his objection. He was convicted, and the Court of Appeals affirmed.<sup>[1]</sup> We granted certiorari to <span class="star-pagination">*202</span> consider whether, under the circumstances here presented, the prosecution's use at the trial of evidence of the petitioner's own incriminating statements deprived him of any right secured to him under the Federal Constitution. <span class="citation multiple-matches"><a href="/c/U.%20S./374/805/">374 U. S. 805</a></span>.</p>
<p>The petitioner, a merchant seaman, was in 1958 a member of the crew of the S. S. <i>Santa Maria.</i> In April of that year federal customs officials in New York received information that he was going to transport a quantity of narcotics aboard that ship from South America to the United States. As a result of this and other information, the agents searched the <i>Santa Maria</i> upon its arrival in New York and found in the afterpeak of the vessel five packages containing about three and a half pounds of cocaine. They also learned of circumstances, not here relevant, tending to connect the petitioner with the cocaine. He was arrested, promptly arraigned, and subsequently indicted for possession of narcotics aboard a United States vessel.<sup>[2]</sup> In July a superseding indictment was returned, charging the petitioner and a man named Colson with the same substantive offense, and in separate counts charging the petitioner, Colson, and others with having conspired to possess narcotics aboard a United States vessel, and to import, conceal, and facilitate the sale of narcotics.<sup>[3]</sup> The petitioner, who had retained a lawyer, pleaded not guilty and was released on bail, along with Colson.</p>
<p>A few days later, and quite without the petitioner's knowledge, Colson decided to cooperate with the government agents in their continuing investigation of the narcotics activities in which the petitioner, Colson, and others had allegedly been engaged. Colson permitted an agent named Murphy to install a Schmidt radio transmitter <span class="star-pagination">*203</span> under the front seat of Colson's automobile, by means of which Murphy, equipped with an appropriate receiving device, could overhear from some distance away conversations carried on in Colson's car.</p>
<p>On the evening of November 19, 1959, Colson and the petitioner held a lengthy conversation while sitting in Colson's automobile, parked on a New York street. By prearrangement with Colson, and totally unbeknown to the petitioner, the agent Murphy sat in a car parked out of sight down the street and listened over the radio to the entire conversation. The petitioner made several incriminating statements during the course of this conversation. At the petitioner's trial these incriminating statements were brought before the jury through Murphy's testimony, despite the insistent objection of defense counsel. The jury convicted the petitioner of several related narcotics offenses, and the convictions were affirmed by the Court of Appeals.<sup>[4]</sup></p>
<p>The petitioner argues that it was an error of constitutional dimensions to permit the agent Murphy at the trial to testify to the petitioner's incriminating statements which Murphy had overheard under the circumstances disclosed by this record. This argument is based upon two distinct and independent grounds. First, we are told that Murphy's use of the radio equipment violated the petitioner's rights under the Fourth Amendment, and, consequently, that all evidence which Murphy thereby obtained was, under the rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, inadmissible against the petitioner at the trial. Secondly, it is said that the petitioner's <span class="star-pagination">*204</span> Fifth and Sixth Amendment rights were violated by the use in evidence against him of incriminating statements which government agents had deliberately elicited from him after he had been indicted and in the absence of his retained counsel. Because of the way we dispose of the case, we do not reach the Fourth Amendment issue.</p>
<p>In <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>, this Court reversed a state criminal conviction because a confession had been wrongly admitted into evidence against the defendant at his trial. In that case the defendant had already been indicted for first-degree murder at the time he confessed. The Court held that the defendant's conviction could not stand under the Fourteenth Amendment. While the Court's opinion relied upon the totality of the circumstances under which the confession had been obtained, four concurring Justices pointed out that the Constitution required reversal of the conviction upon the sole and specific ground that the confession had been deliberately elicited by the police after the defendant had been indicted, and therefore at a time when he was clearly entitled to a lawyer's help. It was pointed out that under our system of justice the most elemental concepts of due process of law contemplate that an indictment be followed by a trial, "in an orderly courtroom, presided over by a judge, open to the public, and protected by all the procedural safeguards of the law." <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#327" aria-description="Citation for case: Spano v. New York">360 U. S., at 327</a></span> (STEWART, J., concurring). It was said that a Constitution which guarantees a defendant the aid of counsel at such a trial could surely vouchsafe no less to an indicted defendant under interrogation by the police in a completely extrajudicial proceeding. Anything less, it was said, might deny a defendant "effective representation by counsel at the only stage when legal aid and advice would help him." <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#326" aria-description="Citation for case: Spano v. New York">360 U. S., at 326</a></span> (DOUGLAS, J., concurring).</p>
<p>Ever since this Court's decision in the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> case, the New York courts have unequivocally followed this constitutional <span class="star-pagination">*205</span> rule. "Any secret interrogation of the defendant, from and after the finding of the indictment, without the protection afforded by the presence of counsel, contravenes the basic dictates of fairness in the conduct of criminal causes and the fundamental rights of persons charged with crime." <i>People</i> v. <i>Waterman,</i> 9 N. Y. 2d 561, 565, <span class="citation" data-id="5519137"><a href="/opinion/5671829/people-v-waterman/#448" aria-description="Citation for case: People v. Waterman">175 N. E. 2d 445, 448</a></span>.<sup>[5]</sup></p>
<p>This view no more than reflects a constitutional principle established as long ago as <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, where the Court noted that ". . . during perhaps the most critical period of the proceedings . . . that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation [are] vitally important, the defendants . . . [are] as much entitled to such aid [of counsel] during that period as at the trial itself." <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#57" aria-description="Citation for case: Powell v. Alabama"><i>Id.,</i> at 57</a></span>. And since the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> decision the same basic constitutional principle has been broadly reaffirmed by this Court. <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>. See <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>.</p>
<p>Here we deal not with a state court conviction, but with a federal case, where the specific guarantee of the Sixth Amendment directly applies.<sup>[6]</sup><i>Johnson</i> v. <i>Zerbst,</i> 304 <span class="star-pagination">*206</span> U. S. 458. We hold that the petitioner was denied the basic protections of that guarantee when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel. It is true that in the <i><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">Spano</a></span></i> case the defendant was interrogated in a police station, while here the damaging testimony was elicited from the defendant without his knowledge while he was free on bail. But, as Judge Hays pointed out in his dissent in the Court of Appeals, "if such a rule is to have any efficacy it must apply to indirect and surreptitious interrogations as well as those conducted in the jailhouse. In this case, Massiah was more seriously imposed upon . . . because he did not even know that he was under interrogation by a government agent." 307 F. 2d, at 72-73.</p>
<p>The Solicitor General, in his brief and oral argument, has strenuously contended that the federal law enforcement agents had the right, if not indeed the duty, to continue their investigation of the petitioner and his alleged criminal associates even though the petitioner had been indicted. He points out that the Government was continuing its investigation in order to uncover not only the source of narcotics found on the S. S. <i>Santa Maria,</i> but also their intended buyer. He says that the quantity of narcotics involved was such as to suggest that the petitioner was part of a large and well-organized ring, and indeed that the continuing investigation confirmed this suspicion, since it resulted in criminal charges against many defendants. Under these circumstances the Solicitor General concludes that the government agents were completely "justified in making use of Colson's cooperation by having Colson continue his normal associations and by surveilling them."</p>
<p>We may accept and, at least for present purposes, completely approve all that this argument implies, Fourth <span class="star-pagination">*207</span> Amendment problems to one side. We do not question that in this case, as in many cases, it was entirely proper to continue an investigation of the suspected criminal activities of the defendant and his alleged confederates, even though the defendant had already been indicted. All that we hold is that the defendant's own incriminating statements, obtained by federal agents under the circumstances here disclosed, could not constitutionally be used by the prosecution as evidence against <i>him</i> at his trial.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE CLARK and MR. JUSTICE HARLAN join, dissenting.</p>
<p>The current incidence of serious violations of the law represents not only an appalling waste of the potentially happy and useful lives of those who engage in such conduct but also an overhanging, dangerous threat to those unidentified and innocent people who will be the victims of crime today and tomorrow. This is a festering problem for which no adequate cures have yet been devised. At the very least there is much room for discontent with remedial measures so far undertaken. And admittedly there remains much to be settled concerning the disposition to be made of those who violate the law.</p>
<p>But dissatisfaction with preventive programs aimed at eliminating crime and profound dispute about whether we should punish, deter, rehabilitate or cure cannot excuse concealing one of our most menacing problems until the millennium has arrived. In my view, a civilized society must maintain its capacity to discover transgressions of the law and to identify those who flout it. This much is necessary even to know the scope of the problem, much less to formulate intelligent countermeasures. It will just not do to sweep these disagreeable matters under the rug or to pretend they are not there at all.</p>
<p><span class="star-pagination">*208</span> It is therefore a rather portentous occasion when a constitutional rule is established barring the use of evidence which is relevant, reliable and highly probative of the issue which the trial court has before itwhether the accused committed the act with which he is charged. Without the evidence, the quest for truth may be seriously impeded and in many cases the trial court, although aware of proof showing defendant's guilt, must nevertheless release him because the crucial evidence is deemed inadmissible. This result is entirely justified in some circumstances because exclusion serves other policies of overriding importance, as where evidence seized in an illegal search is excluded, not because of the quality of the proof, but to secure meaningful enforcement of the Fourth Amendment. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>; <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>. But this only emphasizes that the soundest of reasons is necessary to warrant the exclusion of evidence otherwise admissible and the creation of another area of privileged testimony. With all due deference, I am not at all convinced that the additional barriers to the pursuit of truth which the Court today erects rest on anything like the solid foundations which decisions of this gravity should require.</p>
<p>The importance of the matter should not be underestimated, for today's rule promises to have wide application well beyond the facts of this case. The reason given for the result herethe admissions were obtained in the absence of counselwould seem equally pertinent to statements obtained at any time after the right to counsel attaches, whether there has been an indictment or not; to admissions made prior to arraignment, at least where the defendant has counsel or asks for it; to the fruits of admissions improperly obtained under the new rule; to criminal proceedings in state courts; and to defendants long since convicted upon evidence <span class="star-pagination">*209</span> including such admissions. The new rule will immediately do service in a great many cases.</p>
<p>Whatever the content or scope of the rule may prove to be, I am unable to see how this case presents an unconstitutional interference with Massiah's right to counsel. Massiah was not prevented from consulting with counsel as often as he wished. No meetings with counsel were disturbed or spied upon. Preparation for trial was in no way obstructed. It is only a sterile syllogisman unsound one, besidesto say that because Massiah had a right to counsel's aid before and during the trial, his out-of-court conversations and admissions must be excluded if obtained without counsel's consent or presence. The right to counsel has never meant as much before, <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>; <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and its extension in this case requires some further explanation, so far unarticulated by the Court.</p>
<p>Since the new rule would exclude all admissions made to the police, no matter how voluntary and reliable, the requirement of counsel's presence or approval would seem to rest upon the probability that counsel would foreclose any admissions at all. This is nothing more than a thinly disguised constitutional policy of minimizing or entirely prohibiting the use in evidence of voluntary out-of-court admissions and confessions made by the accused. Carried as far as blind logic may compel some to go, the notion that statements from the mouth of the defendant should not be used in evidence would have a severe and unfortunate impact upon the great bulk of criminal cases.</p>
<p>Viewed in this light, the Court's newly fashioned exclusionary principle goes far beyond the constitutional privilege against self-incrimination, which neither requires nor suggests the barring of voluntary pretrial admissions. The Fifth Amendment states that no person "shall be compelled in any criminal case to be a witness against <span class="star-pagination">*210</span> himself . . . ." The defendant may thus not be compelled to testify at his trial, but he may if he wishes. Likewise he may not be compelled or coerced into saying anything before trial; but until today he could if he wished to, and if he did, it could be used against him. Whether as a matter of self-incrimination or of due process, the proscription is against compulsioncoerced incrimination. Under the prior law, announced in countless cases in this Court, the defendant's pretrial statements were admissible evidence if voluntarily made; inadmissible if not the product of his free will. Hardly any constitutional area has been more carefully patrolled by this Court, and until now the Court has expressly rejected the argument that admissions are to be deemed involuntary if made outside the presence of counsel. <i>Cicenia</i> v. <i><span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">Lagay, supra</a></span></i><i>; </i><i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>.</i><sup>[*]</sup></p>
<p>The Court presents no facts, no objective evidence, no reasons to warrant scrapping the voluntary-involuntary test for admissibility in this area. Without such evidence I would retain it in its present form.</p>
<p>This case cannot be analogized to the American Bar Association's rule forbidding an attorney to talk to the opposing party litigant outside the presence of his counsel. Aside from the fact that the Association's canons are not of constitutional dimensions, the specific canon argued is inapposite because it deals with the conduct <span class="star-pagination">*211</span> of lawyers and not with the conduct of investigators. Lawyers are forbidden to interview the opposing party because of the supposed imbalance of legal skill and acumen between the lawyer and the party litigant; the reason for the rule does not apply to nonlawyers and certainly not to Colson, Massiah's codefendant.</p>
<p>Applying the new exclusionary rule is peculiarly inappropriate in this case. At the time of the conversation in question, petitioner was not in custody but free on bail. He was not questioned in what anyone could call an atmosphere of official coercion. What he said was said to his partner in crime who had also been indicted. There was no suggestion or any possibility of coercion. What petitioner did not know was that Colson had decided to report the conversation to the police. Had there been no prior arrangements between Colson and the police, had Colson simply gone to the police after the conversation had occurred, his testimony relating Massiah's statements would be readily admissible at the trial, as would a recording which he might have made of the conversation. In such event, it would simply be said that Massiah risked talking to a friend who decided to disclose what he knew of Massiah's criminal activities. But if, as occurred here, Colson had been cooperating with the police prior to his meeting with Massiah, both his evidence and the recorded conversation are somehow transformed into inadmissible evidence despite the fact that the hazard to Massiah remains precisely the same the defection of a confederate in crime.</p>
<p>Reporting criminal behavior is expected or even demanded of the ordinary citizen. Friends may be subpoenaed to testify about friends, relatives about relatives and partners about partners. I therefore question the soundness of insulating Massiah from the apostasy of his partner in crime and of furnishing constitutional sanctions for the strict secrecy and discipline of criminal organizations. <span class="star-pagination">*212</span> Neither the ordinary citizen nor the confessed criminal should be discouraged from reporting what he knows to the authorities and from lending his aid to secure evidence of crime. Certainly after this case the Colsons will be few and far between; and the Massiahs can breathe much more easily, secure in the knowledge that the Constitution furnishes an important measure of protection against faithless compatriots and guarantees sporting treatment for sporting peddlers of narcotics.</p>
<p>Meanwhile, of course, the public will again be the loser and law enforcement will be presented with another serious dilemma. The general issue lurking in the background of the Court's opinion is the legitimacy of penetrating or obtaining confederates in criminal organizations. For the law enforcement agency, the answer for the time being can only be in the form of a prediction about the future application of today's new constitutional doctrine. More narrowly, and posed by the precise situation involved here, the question is this: when the police have arrested and released on bail one member of a criminal ring and another member, a confederate, is cooperating with the police, can the confederate be allowed to continue his association with the ring or must he somehow be withdrawn to avoid challenge to trial evidence on the ground that it was acquired after rather than before the arrest, after rather than before the indictment?</p>
<p>Defendants who are out on bail have been known to continue their illicit operations. See <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="262616"><a href="/opinion/262616/robert-lowell-rogers-v-united-states/" aria-description="Citation for case: Robert Lowell Rogers v. United States">325 F. 2d 485</a></span> (C. A. 10th Cir.). That an attorney is advising them should not constitutionally immunize their statements made in furtherance of these operations and relevant to the question of their guilt at the pending prosecution. In this very case there is evidence that after indictment defendant Aiken tried to <span class="star-pagination">*213</span> persuade Agent Murphy to go into the narcotics business with him. Under today's decision, Murphy may neither testify as to the content of this conversation nor seize for introduction in evidence any narcotics whose location Aiken may have made known.</p>
<p>Undoubtedly, the evidence excluded in this case would not have been available but for the conduct of Colson in cooperation with Agent Murphy, but is it this kind of conduct which should be forbidden to those charged with law enforcement? It is one thing to establish safeguards against procedures fraught with the potentiality of coercion and to outlaw "easy but self-defeating ways in which brutality is substituted for brains as an instrument of crime detection." <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#344" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 344</a></span>. But here there was no substitution of brutality for brains, no inherent danger of police coercion justifying the prophylactic effect of another exclusionary rule. Massiah was not being interrogated in a police station, was not surrounded by numerous officers or questioned in relays, and was not forbidden access to others. Law enforcement may have the elements of a contest about it, but it is not a game. <i>McGuire</i> v. <i>United States,</i> <span class="citation" data-id="100989"><a href="/opinion/100989/mcguire-v-united-states/#99" aria-description="Citation for case: McGuire v. United States">273 U. S. 95, 99</a></span>. Massiah and those like him receive ample protection from the long line of precedents in this Court holding that confessions may not be introduced unless they are voluntary. In making these determinations the courts must consider the absence of counsel as one of several factors by which voluntariness is to be judged. See <i>House</i> v. <i>Mayo,</i> <span class="citation" data-id="104079"><a href="/opinion/104079/house-v-mayo/#45" aria-description="Citation for case: House v. Mayo">324 U. S. 42, 45-46</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 567</a></span>; <i>Cicenia</i> v. <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/#509" aria-description="Citation for case: Cicenia v. Lagay"><i>Lagay, supra,</i> at 509</a></span>. This is a wiser rule than the automatic rule announced by the Court, which requires courts and juries to disregard voluntary admissions which they might well find to be the best possible evidence in discharging their responsibility for ascertaining truth.</p>
<h2>NOTES</h2>
<p>[1]  <span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62</a></span>.</p>
<p>[2]  21 U. S. C. § 184a.</p>
<p>[3]  <span class="citation no-link">21 U. S. C. §§ 173</span>, 174.</p>
<p>[4]  The petitioner's trial was upon a second superseding indictment which had been returned on March 3, 1961, and which included additional counts against him and other defendants. The Court of Appeals reversed his conviction upon a conspiracy count, one judge dissenting, but affirmed his convictions upon three substantive counts, one judge dissenting. <span class="citation" data-id="9448761"><a href="/opinion/258052/united-states-v-winston-massiah-mitchell-anfield-leonard-royal-aiken-and/" aria-description="Citation for case: United States v. Winston Massiah, Mitchell Anfield,...">307 F. 2d 62</a></span>.</p>
<p>[5]  See also <i>People</i> v. <i>Davis,</i> 13 N. Y. 2d 690, <span class="citation" data-id="5520812"><a href="/opinion/5673349/people-v-davis/" aria-description="Citation for case: People v. Davis">191 N. E. 2d 674</a></span>, 241 N. Y. S. 2d 172 (1963); <i>People</i> v. <i>Rodriguez,</i> 11 N. Y. 2d 279, <span class="citation" data-id="5519859"><a href="/opinion/5672480/people-v-rodriguez/" aria-description="Citation for case: People v. Rodriguez">183 N. E. 2d 651</a></span>, 229 N. Y. S. 2d 353 (1962); <i>People</i> v. <i>Meyer,</i> 11 N. Y. 2d 162, <span class="citation" data-id="5519835"><a href="/opinion/5672465/people-v-meyer/" aria-description="Citation for case: People v. Meyer">182 N. E. 2d 103</a></span>, 227 N. Y. S. 2d 427 (1962); <i>People</i> v. <i>Di Biasi,</i> 7 N. Y. 2d 544, <span class="citation" data-id="5518161"><a href="/opinion/5670925/people-v-di-biasi/" aria-description="Citation for case: People v. Di Biasi">166 N. E. 2d 825</a></span>, 200 N. Y. S. 2d 21 (1960); <i>People</i> v. <i>Swanson,</i> 18 App. Div. 2d 832, 237 N. Y. S. 2d 400 (2d Dept. 1963); <i>People</i> v. <i>Price,</i> 18 App. Div. 2d 739, 235 N. Y. S. 2d 390 (3d Dept. 1962); <i>People</i> v. <i>Wallace,</i> 17 App. Div. 2d 981, 234 N. Y. S. 2d 579 (2d Dept. 1962); <i>People</i> v. <i>Karmel,</i> 17 App. Div. 2d 659, 230 N. Y. S. 2d 413 (2d Dept. 1962); <i>People</i> v. <i>Robinson,</i> 16 App. Div. 2d 184, 224 N. Y. S. 2d 705 (4th Dept. 1962).</p>
<p>[6]  "In all criminal prosecutions, the accused shall enjoy the right . . . to have the Assistance of Counsel for his defence."</p>
<p>[*]  Today's rule picks up where the Fifth Amendment ends and bars wholly voluntary admissions. I would assume, although one cannot be sure, that the new rule would not have a similar supplemental role in connection with the Fourth Amendment. While the Fifth Amendment bars only compelled incrimination, the Fourth Amendment bars only unreasonable searches. It could be argued, fruitlessly I would hope, that if the police must stay away from the defendant they must also stay away from his house once the right to counsel has attached and that a court must exclude the products of a reasonable search made pursuant to a properly issued warrant but without the consent or presence of the accused's counsel.</p>

</div>
```

---

## GROUP: content/cases/McNabb v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "McNabb v. United States"
type: case
citation: "318 U.S. 332 (1943)"
parallel_cite: "63 S. Ct. 608; 87 L. Ed. 819"
neutral_cite: 1943 U.S. LEXIS 1280
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1943
date_decided: 1943-06-07
docket: 25
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1943-06-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: McNabb v. United States
  varies_by_point: false
  scope_note: "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501, per Corley v. United States."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103791/mcnabb-v-united-states/"
  cluster_id: 103791
  opinion_id: 103791
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Mallory v. United States]]", "[[Corley v. United States]]", "[[Gerstein v. Pugh]]", "[[County of Riverside v. McLaughlin]]"]
aliases: []
tags: ["case", "fifth-amendment", "confessions", "mcnabb-mallory", "prompt-presentment", "supervisory-power", "federal"]
holding: "Under the Court's supervisory power over the federal courts, confessions obtained from federal arrestees during a prolonged detention conducted in flagrant disregard of the statutory duty to bring them promptly before a committing magistrate are inadmissible — independent of the Constitution."
lake:
  record_id: McNabb v. United States
  status: verified
  projected_at: 2026-07-06
---

# McNabb v. United States

*318 U.S. 332 (1943)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The McNabbs, a Tennessee family suspected of running an illegal still, were arrested by federal officers after a revenue agent was shot and killed during a raid. Several family members were detained by the officers — held in a barren cell, subjected to days of unremitting questioning by numerous officers, without friends or counsel and before any order of commitment — until they made incriminating statements. The statements were admitted and the McNabbs were convicted of second-degree murder of the federal officer.

## Issue
Whether confessions obtained from federal arrestees during a prolonged detention conducted in disregard of the statutory duty to take them promptly before a committing magistrate are admissible in the federal courts.

## Rule
No — they are excluded under the Court's supervisory power over federal criminal justice, apart from the Constitution. "Plainly, a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in wilful disobedience of law. . . . [T]o permit such evidence to be made the basis of a conviction in the federal courts would stultify the policy which Congress has enacted into law." — 318 U.S. at 345. ^pin-345

The exclusion rests on the integrity of the federal courts, not on a constitutional command: "We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. . . . The history of liberty has largely been the history of observance of procedural safeguards." — *Id.* at 347. ^pin-347

## Application
The McNabbs were questioned while in the custody of the arresting officers and before any commitment order, held in a barren cell and interrogated continuously for days without friends or counsel. Their confessions were thus secured during a detention that flagrantly disregarded the statutes requiring prompt presentment to a committing magistrate. Allowing convictions to rest on evidence so obtained would make the courts accomplices in disobedience of those statutes, so the confessions had to be excluded — the Court resting on its supervisory authority rather than reaching the constitutional question.

## Conclusion
The confessions were inadmissible and the convictions could not stand; the judgments were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *McNabb* is the first half of the **McNabb-Mallory** federal prompt-presentment rule, completed by [[Mallory v. United States]] under Federal Rule of Criminal Procedure 5(a). It is a **federal-court** supervisory-power rule, not a constitutional rule binding the States. Congress later **modified** — but did not supplant — the rule by 18 U.S.C. §3501's six-hour safe harbor, as the Court held in [[Corley v. United States]]. The prompt-presentment duty is the confession-suppression counterpart to the prompt judicial probable-cause determination of [[Gerstein v. Pugh]] and [[County of Riverside v. McLaughlin]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *McNabb v. United States*, 318 U.S. 332 (1943) — https://www.courtlistener.com/opinion/103791/mcnabb-v-united-states/ — pinpoints: 345, 347.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "718fc52386300624", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "318 U.S. 332 (1943)", "court": "U.S. Supreme Court", "neutral_cite": "1943 U.S. LEXIS 1280", "official_citation_present": true, "parallel_cite": "63 S. Ct. 608; 87 L. Ed. 819", "title": "McNabb v. United States", "year": "1943"}}
{"assertion_id": "b7abd27902b182c5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Under the Court's supervisory power over the federal courts, confessions obtained from federal arrestees during a prolonged detention conducted in flagrant disregard of the statutory duty to bring them promptly before a committing magistrate are inadmissible — independent of the Constitution.", "title": "McNabb v. United States"}}
{"assertion_id": "ca6c38a2c9d8b4d0", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Anchor", "title": "McNabb v. United States"}}
{"assertion_id": "d4928b0ae68035d4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "McNabb v. United States"}}
{"assertion_id": "d70c62c7dab340e9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1943-06-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "McNabb v. United States", "field_i_validity": "good_law", "scope_note": "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified — not supplanted — by 18 U.S.C. §3501, per Corley v. United States.", "title": "McNabb v. United States", "varies_by_point": "false"}}
```

### lake record — McNabb v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "McNabb v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "McNabb v. United States",
    "case_name_short": "McNabb",
    "case_name_full": "McNABB Et Al. v. UNITED STATES",
    "input_case_name": "McNabb v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1943-06-07",
    "year": 1943,
    "docket": "25",
    "cluster_id": 103791,
    "lead_opinion_id": 103791,
    "sibling_ids": [
      103791,
      9419320,
      9419321
    ],
    "absolute_url": "/opinion/103791/mcnabb-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8196926,
        "score": 20,
        "case_name": "McNabb v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "318 U.S. 332",
      "volume": "318",
      "reporter": "U.S.",
      "page": "332",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "63 S. Ct. 608",
        "volume": "63",
        "reporter": "S. Ct.",
        "page": "608",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 819",
        "volume": "87",
        "reporter": "L. Ed.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1943 U.S. LEXIS 1280",
        "volume": "1943",
        "reporter": "U.S. LEXIS",
        "page": "1280",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "318 U.S. 332",
        "volume": "318",
        "reporter": "U.S.",
        "page": "332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 S. Ct. 608",
        "volume": "63",
        "reporter": "S. Ct.",
        "page": "608",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 L. Ed. 819",
        "volume": "87",
        "reporter": "L. Ed.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1943 U.S. LEXIS 1280",
        "volume": "1943",
        "reporter": "U.S. LEXIS",
        "page": "1280",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "318 U.S. 332",
    "official_selection": {
      "court_class": "scotus",
      "selected": "318 U.S. 332",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-345",
      "page": null,
      "quote": "--- # McNabb v. United States *318 U.S. 332 (1943)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background The McNabbs, a Tennessee family suspected of running an illegal still, were arrested by federal officers after a revenue agent was shot and killed during a raid. Several family members were detained by the officers \u2014 held in a barren cell, subjected to days of unremitting questioning by numerous officers, without friends or counsel and before any order of commitment \u2014 until they made incriminating statements. The statements were admitted and the McNabbs were convicted of second-degree murder of the federal officer. ## Issue Whether confessions obtained from federal arrestees during a prolonged detention conducted in disregard of the statutory duty to take them promptly before a committing magistrate are admissible in the federal courts. ## Rule No \u2014 they are excluded under the Court's supervisory power over federal criminal justice, apart from the Constitution.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-347",
      "page": null,
      "quote": "We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. . . . The history of liberty has largely been the history of observance of procedural safeguards.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1943-06-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "McNabb v. United States",
    "varies_by_point": false,
    "scope_note": "Good law as the 'McNabb' half of the McNabb-Mallory federal prompt-presentment rule. A federal supervisory-power / Rule 5(a) rule, not a constitutional rule binding the States; later modified \u2014 not supplanted \u2014 by 18 U.S.C. \u00a73501, per Corley v. United States.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Fortunato",
          "cluster_id": 6580749,
          "cite": [
            "466 Mass. 500",
            "996 N.E.2d 457",
            "2013 WL 5451772",
            "2013 Mass. LEXIS 719"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mitchell",
          "cluster_id": 2662992,
          "cite": [
            "841 F. Supp. 2d 322",
            "2012 WL 256088",
            "2012 U.S. Dist. LEXIS 10769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
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
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re United States",
          "cluster_id": 202116,
          "cite": [
            "441 F.3d 44",
            "2006 U.S. App. LEXIS 7779",
            "2006 WL 744801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Garcia-Echaverria",
          "cluster_id": 786819,
          "cite": [
            "374 F.3d 440",
            "2004 U.S. App. LEXIS 13590",
            "2004 WL 1470466"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Dennis Johnson",
          "cluster_id": 784434,
          "cite": [
            "351 F.3d 988",
            "63 Fed. R. Serv. 69",
            "2003 U.S. App. LEXIS 25298",
            "2003 WL 22952102"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pouncey",
          "cluster_id": 7897125,
          "cite": [
            "241 Conn. 802",
            "699 A.2d 901",
            "1997 Conn. LEXIS 226"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard A. Pelullo",
          "cluster_id": 733401,
          "cite": [
            "105 F.3d 117",
            "1997 U.S. App. LEXIS 311",
            "1997 WL 6366"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario",
          "cluster_id": 6576998,
          "cite": [
            "422 Mass. 48",
            "661 N.E.2d 71",
            "1996 Mass. LEXIS 29"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Juan Ramon MATTA-BALLESTEROS, Defendant-Appellant",
          "cluster_id": 709239,
          "cite": [
            "71 F.3d 754",
            "95 Daily Journal DAR 15853",
            "95 Cal. Daily Op. Serv. 9042",
            "43 Fed. R. Serv. 338",
            "1995 U.S. App. LEXIS 33475",
            "1995 WL 704693"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 7896184,
          "cite": [
            "234 Conn. 324",
            "662 A.2d 1199",
            "1995 Conn. LEXIS 254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Turner",
          "cluster_id": 1188941,
          "cite": [
            "878 P.2d 521",
            "8 Cal. 4th 137",
            "32 Cal. Rptr. 2d 762",
            "94 Daily Journal DAR 11425",
            "94 Cal. Daily Op. Serv. 6238",
            "1994 Cal. LEXIS 4151"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Horn",
          "cluster_id": 674595,
          "cite": [
            "29 F.3d 754",
            "29 Fed. R. Serv. 3d 1525",
            "1994 U.S. App. LEXIS 18687",
            "1994 WL 378486"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane1_negative"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Young",
          "cluster_id": 111353,
          "cite": [
            "84 L. Ed. 2d 1",
            "105 S. Ct. 1038",
            "470 U.S. 1",
            "1985 U.S. LEXIS 49",
            "53 U.S.L.W. 4159"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. United States",
          "cluster_id": 105254,
          "cite": [
            "99 L. Ed. 2d 150",
            "75 S. Ct. 127",
            "348 U.S. 121",
            "1954 U.S. LEXIS 2740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pinkerton v. United States",
          "cluster_id": 104316,
          "cite": [
            "328 U.S. 640",
            "66 S. Ct. 1180",
            "90 L. Ed. 1489",
            "1946 U.S. LEXIS 3154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massiah v. United States",
          "cluster_id": 106822,
          "cite": [
            "12 L. Ed. 2d 246",
            "84 S. Ct. 1199",
            "377 U.S. 201",
            "1964 U.S. LEXIS 1277"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cupp v. Naughten",
          "cluster_id": 108888,
          "cite": [
            "38 L. Ed. 2d 368",
            "94 S. Ct. 396",
            "414 U.S. 141",
            "1973 U.S. LEXIS 180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elkins v. United States",
          "cluster_id": 106107,
          "cite": [
            "4 L. Ed. 2d 1669",
            "80 S. Ct. 1437",
            "364 U.S. 206",
            "1960 U.S. LEXIS 1989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rabinowitz",
          "cluster_id": 104769,
          "cite": [
            "94 L. Ed. 2d 653",
            "70 S. Ct. 430",
            "339 U.S. 56",
            "1950 U.S. LEXIS 2298",
            "94 L. Ed. 653"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
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
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Costello v. United States",
          "cluster_id": 105355,
          "cite": [
            "100 L. Ed. 2d 397",
            "76 S. Ct. 406",
            "350 U.S. 359",
            "1956 U.S. LEXIS 1845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Townsend v. Burke",
          "cluster_id": 104579,
          "cite": [
            "92 L. Ed. 2d 1690",
            "68 S. Ct. 1252",
            "334 U.S. 736",
            "1948 U.S. LEXIS 1988",
            "92 L. Ed. 1690"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherman v. United States",
          "cluster_id": 105681,
          "cite": [
            "2 L. Ed. 2d 848",
            "78 S. Ct. 819",
            "356 U.S. 369",
            "1958 U.S. LEXIS 1024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolf v. Colorado",
          "cluster_id": 104709,
          "cite": [
            "93 L. Ed. 2d 1782",
            "69 S. Ct. 1359",
            "338 U.S. 25",
            "1949 U.S. LEXIS 2079",
            "93 L. Ed. 1782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNabb v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103791 OR 9419320 OR 9419321) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NzUwNDMyMDAwMDAmcz0yMzUwNjAwJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103791+OR+9419320+OR+9419321%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 17,
        "triage_snippet_classified": 183
      },
      "lane2_top_cited": {
        "query": "cites:(103791 OR 9419320 OR 9419321)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03ODYmcz0xMDUxNDkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103791+OR+9419320+OR+9419321%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103791 OR 9419320 OR 9419321)",
        "reviewed": 5,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 5,
        "triage_read": 0,
        "triage_snippet_classified": 5
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(103791 OR 9419320 OR 9419321)",
    "indexed_citing_opinions": 1337,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103791,
        "count": 1254,
        "count_source": "search"
      },
      {
        "opinion_id": 9419320,
        "count": 120,
        "count_source": "search"
      },
      {
        "opinion_id": 9419321,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2030,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mcnabb-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MTYyNDEmcz00NzA3NTk1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103791+OR+9419320+OR+9419321%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103791,
        "cited_id": 84842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 85535,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 91057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94327,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 94454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 99746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 101963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103791,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T12:57:29Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:00:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T12:57:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — McNabb v. United States

```
<p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">318 U.S. 332</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">63 S.Ct. 608</a></span></p>
    <p class="case_cite"><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">87 L.Ed. 819</a></span></p>
    <p class="parties">McNABB et al.<br>v.<br>UNITED STATES.</p>
    <p class="docket">No. 25.</p>
    <p class="date">Argued Oct. 22, 1942.</p>
    <p class="date">Decided March 1, 1943.</p>
    <p class="date">Rehearing Denied June 7, 1943.</p>
    <div class="prelims">
      <p class="indent">See <span class="citation multiple-matches"><a href="/c/U.S./319/784/">319 U.S. 784</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./63/1322/">63 S.Ct. 1322</a></span>, 87 L.Ed. &#8212;-.</p>
      <p class="indent">Mr. E. B. Baker, of Chattanooga, Tenn., for petitioners.</p>
      <p class="indent">Mr. Asst. Atty. Gen. Wendell Berge, of Washington, D.C., for respondent.</p>
      <p class="indent">Mr. Justice FRANKFURTER, delivered the opinion of the Court.</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The petitioners are under sentence of imprisonment for forty-five years for the murder of an officer of the Alcohol Tax Unit of the Bureau of Internal Revenue engaged in the performance of his official duties. <span class="citation no-link">18 U.S.C. &#167; 253</span>, <span class="citation no-link">18 U.S.C.A. &#167; 253</span>. They were convicted of second-degree murder in the District Court for the Eastern District of Tennessee, and on appeal to the Circuit Court of Appeals for the Sixth Circuit the convictions were sustained. <span class="citation" data-id="1486063"><a href="/opinion/1486063/mcnabb-v-united-states/" aria-description="Citation for case: McNabb v. United States">123 F.2d 848</a></span>. We brought the case here because the petition for certiorari presented serious questions in the administration of federal criminal justice. <span class="citation multiple-matches"><a href="/c/U.S./316/658/">316 U.S. 658</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./62/1305/">62 S.Ct. 1305</a></span>, <span class="citation no-link">86 L.Ed. 1736</span>. Determination of these questions turns upon the circumstances relating to the admission in evidence of incriminating statements made by the petitioners.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">On the afternoon of Wednesday, July 31, 1940, information was received at the Chattanooga office of the Alcoholic Tax Unit that several members of the McNabb family were planning to sell that night whiskey on which federal taxes had not been paid. The McNabbs were a clan of Tennessee mountaineers living about twelve miles from Chattanooga in a section known as the McNabb Settlement. Plans were made to apprehend the McNabbs while actually engaged in their illicit enterprise. That evening four revenue agents, accompanied by the Government's informers, drove to the McNabb Settlement. When they approached the rendezvous arranged between the McNabbs and the informers, the officers got out of the car. The informers drove on and met five of the McNabbs, of whom three&#8212;the twin brothers Freeman and Raymond, and their cousin Benjamin&#8212;are the petitioners here. (The two others, Emuil and Barney McNabb, were acquitted at the direction of the trial court.) The group proceeded to a spot near the family cemetery where the liquor was hidden. While cans containing whiskey were being loaded into the car, one of the informers flashed a prearranged signal to the officers who thereupon came running. One of these called out, 'All right, boys, federal officers!', and the McNabbs took flight.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">Instead of pursuing the McNabbs, the officers began to empty the cans. They heard noises coming from the direction of the cemetery, and after a short while a large rock landed at their feet. An officer named Leeper ran into the cemetery. He looked about with his flashlight but discovered no one. Noticing a couple of whiskey cans there he began to pour out their contents. Shortly afterwards the other officers heard a shot; running into the cemetery they found Leeper on the ground, fatally wounded. A few minutes later&#8212;at about ten o'clock&#8212;he died without having identified his assailant. A second shot slightly wounded another officer. A search of the cemetery proved futile, and the officers left.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">About three or four hours later&#8212;between one and two o'clock Thursday morning&#8212;federal officers went to the home of Freeman, Raymond, and Emuil McNabb and there placed them under arrest. Freeman and Raymond were twenty-five years old. Both had lived in the Settlement all their lives; neither had gone beyond the fourth grade in school; neither had ever been farther from his home than Jasper, twenty-one miles away. Emuil was twenty-two years old. He, too, had lived in the Settlement all his life, and had not gone beyond the second grade.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Immediately upon arrest, Freeman, Raymond, and Emuil were taken directly to the Federal Building at Chattanooga. They were not brought before a United States Commissioner or a judge. Instead, they were placed in a detention room (where there was nothing they could sit or lie down on, except the floor), and kept there for about fourteen hours, from three o'clock Thursday morning until five o'clock that afternoon. They were given some sandwiches. They were not permitted to see relatives and friends who attempted to visit them. They had no lawyer. There is no evidence that they requested the assistance of counsel, or that they were told that they were entitled to such assistance.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">Barney McNabb, who had been arrested early Thursday morning by the local police, was handed over to the federal authorities about nine or ten o'clock that morning. He was twenty-eight years old; like the other McNabbs he had spent his entire life in the Settlement, had never gone beyond Jasper, and his schooling stopped at the third grade. Barney was placed in a separate room in the Federal Building where he was questioned for a short period. The officers then took him to the scene of the killing, brought him back to the Federal Building, questioned him further for about an hour, and finally removed him to the county jail three blocks away.</p>
    </div>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">In the meantime, direction of the investigation had been assumed by H. B. Taylor, district supervisor of the Alcohol Tax Unit, with headquarters at Louisville, Kentucky. Taylor was the Government's chief witness on the central issue of the admissbility of the statements made by the McNabbs. Arriving in Chattanooga early Thursday morning, he spent the day in study of the case before beginning his interrogation of the prisoners. Freeman, Raymond, and Emuil, who had been taken to the county jail about five o'clock Thursday afternoon, were brought back to the Federal Building early that evening. According to Taylor, his questioning of them began at nine o'clock. Other officers set the hour earlier.<a class="footnote" href="#fn1" id="fn1_ref">1</a></p>
    </div>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Throughout the questioning, most of which was done by Taylor, at least six officers were present. At no time during its course was a lawyer or any relative or friend of the defendants present. Taylor began by telling 'each of them before they were questioned that we were Government officers, what we were investigating, and advised them that they did not have to make a statement, that they need not fear force, and that any statement made by them would be used against them, and that they need not answer any questions asked unless they desired to do so'.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">The men were questioned singly and together. As described by one of the officers, 'they would be brought in, be questioned possibly at various times, some of them half an hour, or maybe an hour, or maybe two hours'. Taylor testified that the questioning continued until one o'clock in the morning, when the defendants were taken back to the county jail.<a class="footnote" href="#fn2" id="fn2_ref">2</a></p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">The questioning was resumed Friday morning, probably sometime between nine and ten o'clock.<a class="footnote" href="#fn3" id="fn3_ref">3</a> 'They were brought down from the jail several times, how many I don't know. They were questioned one at a time, as we would finish one he would be sent back and we would try to reconcile the facts they told, connect up the statements they made, and they we would get two of them together. I think at one time we probably had all five together trying to reconcile their statements. * * * When I knew the truth I told the defendants what I knew. I never called them damn liars, but I did say they were lying to me. * * * It would be impossible to tell all the motions I made with my hands during the two days of questioning, however, I didn't threaten anyone. None of the officers were prejudiced towards these defendants nor bitter toward them. We were only trying to find out who killed our fellow officer.'</p>
    </div>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">Benjamin McNabb, the third of the petitioners, came to the office of the Alcohol Tax Unit about eight or nine o'clock Friday morning and voluntarily surrendered. Benjamin was twenty years old, had never been arrested before, had lived in the McNabb Settlement all his life, and had not got beyond the fourth grade in school. He told the officers that he had heard that they were looking for him but that he was entirely innocent of any connection with the crime. The officers made him take his clothes off for a few minutes because, so he testified, 'they wanted to look at me. This scared me pretty much.'<a class="footnote" href="#fn4" id="fn4_ref">4</a> He was not taken before a United States Commissioner or a judge. Instead, the officers questioned him for about five or six hours. When finally in the afternoon he was confronted with the statement that the others accused him of having fired both shots, Benjamin said, 'If they are going to accuse me of that, I will tell the whole truth; you may get your pencil and paper and write it down.' He then confessed that he had fired the first shot, but denied that he had also fired the second.</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">Because there were 'certain discrepancies in their stories, and we were anxious to straighten them out', the defendants were brought to the Federal Building from the jail between nine and ten o'clock Friday night. They were again questioned, sometimes separately, sometimes together. Taylor testified that 'We had Freeman McNabb on the night of the second (Friday) for about three and one-half hours. I don't remember the time but I remember him particularly because he certainly was hard to get anything out of. He would admit he lied before, and then tell it all over again. I knew some of the things about the whole truth and it took about three and one-half hours before he would say it was the truth, and I finally got him to tell a story which he said was true and which certainly fit better with the physical facts and circumstances than any other story he had told. It took me three and one-half hours to get a story that was satisfactory or that I believed was nearer the truth than when we started.'</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">The questioning of the defendants continued until about two o'clock Saturday morning, when the officers finally 'got all the discrepancies straightened out.' Benjamin did not change his story that he had fired only the first shot. Freeman and Raymond admitted that they were present when the shooting occurred, but denied Benjamin's charge that they had urged him to shoot. Barney and Emuil, who were acquitted at the direction of the trial court, made no incriminating admissions.</p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">Concededly, the admissions made by Freeman, Raymond and Benjamin constituted the crux of the Government's case against them, and the convictions cannot stand if such evidence be excluded. Accordingly, the question for our decision is whether these incriminating statements, made under the circumstances we have summarized,<a class="footnote" href="#fn5" id="fn5_ref">5</a> were properly admitted. Relying upon the guarantees of the Fifth Amendment that no person 'shall be compelled in any Criminal Case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law', the petitioners contend that the Constitution itself forbade the use of this evidence against them. The Government counters by urging that the Constitution proscribes only 'involuntary' confessions, and that judged by appropriate criteria of 'voluntariness' the petitioners' admissions were voluntary and hence admissible.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">It is true, as the petitioners assert, that a conviction in the federal courts, the foundation of which is evidence obtained in disregard of liberties deemed fundamental by the Constitution, cannot stand. Boyd v. United States, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">6 S.Ct. 524</a></span>, <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">29 L.Ed. 746</a></span>; Weeks v. United States, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U.S. 383</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">34 S.Ct. 341</a></span>, <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">58 L.Ed. 652</a></span>, L.R.A.1915B, 834, Ann.Cas.1915C, 1177; Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U.S. 298</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">41 S.Ct. 261</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L.Ed. 647</a></span>; Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S.Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L.Ed. 654</a></span>; Agnello v. United States, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U.S. 20</a></span>, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">46 S.Ct. 4</a></span>, <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">70 L.Ed. 145</a></span>; Byars v. United States, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U.S. 28</a></span>, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">47 S.Ct. 248</a></span>, <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">71 L.Ed. 520</a></span>; Grau v. United States, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">287 U.S. 124</a></span>, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">53 S.Ct. 38</a></span>, <span class="citation" data-id="101963"><a href="/opinion/101963/grau-v-united-states/" aria-description="Citation for case: Grau v. United States">77 L.Ed. 212</a></span>. And this Court has, on Constitutional grounds, set aside convictions, both in the federal and state courts, which were based upon confessions 'secured by protracted and repeated questioning of ignorant and untutored persons in whose minds the power of officers was greatly magnified', Lisenba v. California, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#239" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 239, 240</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#291" aria-description="Citation for case: Lisenba v. California">62 S.Ct. 280, 291</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">86 L.Ed. 166</a></span>, or 'who have been unlawfully held incommunicado without advice of friends or counsel', Ward v. Texas, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#555" aria-description="Citation for case: Ward v. Texas">316 U.S. 547, 555</a></span>, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#1143" aria-description="Citation for case: Ward v. Texas">62 S.Ct. 1139, 1143</a></span>, <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">86 L.Ed. 1663</a></span>, and see Brown v. Mississippi, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U.S. 278</a></span>, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">56 S.Ct. 461</a></span>, <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">80 L.Ed. 682</a></span>; Chambers v. Florida, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">60 S.Ct. 472</a></span>, <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">84 L.Ed. 716</a></span>; Canty v. Alabama, <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U.S. 629</a></span>, <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">60 S.Ct. 612</a></span>, <span class="citation no-link">84 L.Ed. 988</span>; White v. Texas, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U.S. 530</a></span>, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">60 S.Ct. 1032</a></span>, <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">84 L.Ed. 1342</a></span>; Lomax v. Texas, <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U.S. 544</a></span>, <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">61 S.Ct. 956</a></span>, <span class="citation no-link">85 L.Ed. 1511</span>; Vernon v. Alabama, <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U.S. 547</a></span>, <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">61 S.Ct. 1092</a></span>, <span class="citation" data-id="8156478"><a href="/opinion/8194543/bakery-pastry-drivers-helpers-local-802-v-wohl/" aria-description="Citation for case: Bakery &amp; Pastry Drivers &amp; Helpers Local 802 v. Wohl">85 L.Ed. 1513</a></span>.</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">In the view we take of the case, however, it becomes unnecessary to reach the Constitutional issue pressed upon us. For, while the power of this Court to undo convictions in state courts is limited to the enforcement of those 'fundamental principles of liberty and justice', Hebert v. Louisiana, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U.S. 312, 316</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#104" aria-description="Citation for case: Hebert v. Louisiana">47 S.Ct. 103, 104</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/" aria-description="Citation for case: Hebert v. Louisiana">71 L.Ed. 270</a></span>, <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/" aria-description="Citation for case: Hebert v. Louisiana">48 A.L.R. 1102</a></span>, which are secured by the Fourteenth Amendment, the scope of our reviewing power over convictions brought here from the federal courts is not confined to ascertainment of Constitutional validity. Judicial supervision of the administration of criminal justice in the federal courts implies the duty of establishing and maintaining civilized standards of procedure and evidence. Such standards are not satisfied merely by observance of those minimal historic safeguards for securing trial by reason which are summarized as 'due process of law' and below which we reach what is really trial by force. Moreover, review by this Court of state action expressing its notion of what will best further its own security in the administration of criminal justice demands appropriate respect for the deliberative judgment of a state in so basic an exercise of its jurisdiction. Considerations of large policy in making the necessary accommodations in our federal system are wholly irrelevant to the formulation and application of proper standards for the enforcement of the federal criminal law in the federal courts.</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">The principles governing the admissibility of evidence in federal criminal trials have not been restricted, therefore, to those derived solely from the Constitution. In the exercise of its supervisory authority over the administration of criminal justice in the federal courts, see Nardone v. United States, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U.S. 338, 341, 342</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#267" aria-description="Citation for case: Nardone v. United States">60 S.Ct. 266, 267, 268</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>, this Court has, from the very beginning of its history, formulated rules of evidence to be applied in federal criminal prosecutions. E.g., Ex parte Bollman &amp; Swartwout, <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#130" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75, 130, 131</a></span>, <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout">2 L.Ed. 554</a></span>; United States v. Palmer, <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/#643" aria-description="Citation for case: United States v. Palmer">3 Wheat. 610, 643, 644</a></span>, <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/" aria-description="Citation for case: United States v. Palmer">4 L.Ed. 471</a></span>; United States v. Furlong, <span class="citation" data-id="85290"><a href="/opinion/85290/united-states-v-furlong/#199" aria-description="Citation for case: United States v. Furlong">5 Wheat. 184, 199</a></span>, <span class="citation" data-id="85290"><a href="/opinion/85290/united-states-v-furlong/" aria-description="Citation for case: United States v. Furlong">5 L.Ed. 64</a></span>; United States v. Gooding, <span class="citation" data-id="85535"><a href="/opinion/85535/united-states-v-gooding/#468" aria-description="Citation for case: United States v. Gooding">12 Wheat. 460, 468, 470</a></span>, <span class="citation" data-id="85535"><a href="/opinion/85535/united-states-v-gooding/" aria-description="Citation for case: United States v. Gooding">6 L.Ed. 693</a></span>; United States v. Wood, <span class="citation" data-id="9416399"><a href="/opinion/86149/united-states-v-wood/" aria-description="Citation for case: United States v. Wood">14 Pet. 430</a></span>, <span class="citation" data-id="9416399"><a href="/opinion/86149/united-states-v-wood/" aria-description="Citation for case: United States v. Wood">10 L.Ed. 527</a></span>; United States v. Murphy, <span class="citation" data-id="86206"><a href="/opinion/86206/united-states-v-murphy/" aria-description="Citation for case: United States v. Murphy">16 Pet. 203</a></span>, <span class="citation" data-id="86206"><a href="/opinion/86206/united-states-v-murphy/" aria-description="Citation for case: United States v. Murphy">10 L.Ed. 937</a></span>; Funk v. United States, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">290 U.S. 371</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">54 S.Ct. 212</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">78 L.Ed. 369</a></span>, <span class="citation" data-id="102164"><a href="/opinion/102164/funk-v-united-states/" aria-description="Citation for case: Funk v. United States">93 A.L.R. 1136</a></span>; Wolfle v. United States, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">291 U.S. 7</a></span>, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">54 S.Ct. 279</a></span>, <span class="citation" data-id="102181"><a href="/opinion/102181/wolfle-v-united-states/" aria-description="Citation for case: Wolfle v. United States">78 L.Ed. 617</a></span>; see 1 Wigmore on Evidence (3d ed. 1940) pp. 170-97; Note, 47 Harv.L.Rev. 853.<a class="footnote" href="#fn6" id="fn6_ref">6</a> And in formulating such rules of evidence for federal criminal trials the Court has been guided by considerations of justice not limited to the strict canons of evidentiary relevance.</p>
    </div>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">Quite apart from the Constitution, therefore, we are constrained to hold that the evidence elicited from the petitioners in the circumstances disclosed here must be excluded. For in their treatment of the petitioners the arresting officers assumed functions which Congress has explicitly denied them. They subjected the accused to the pressures of a procedure which is wholly incompatible with the vital but very restricted duties of the investigating and arresting officers of the Government and which tends to undermine the integrity of the criminal proceeding. Congress has explicitly commanded that 'It shall be the duty of the marshal, his deputy, or other officer, who may arrest a person charged with any crime or offense, to take the defendant before the nearest United States commissioner or the nearest judicial officer having jurisdiction under existing laws for a hearing, commitment, or taking bail for trial * * *'. <span class="citation no-link">18 U.S.C. &#167; 595</span>, <span class="citation no-link">18 U.S.C.A. &#167; 595</span>. Similarly, the Act of June 18, 1934, c. 595, <span class="citation no-link">48 Stat. 1008</span>, 5 U.S.C. &#167; 300a, 5 U.S.C.A. &#167; 300a, authorizing officers of the Federal Bureau of Investigation to make arrests, requires that 'the person arrested shall be immediately taken before a committing officer.' Compare also the Act of March 1, 1879, c. 125, <span class="citation no-link">20 Stat. 327</span>, 341, <span class="citation no-link">18 U.S.C. &#167; 593</span>, <span class="citation no-link">18 U.S.C.A. &#167; 593</span>, which provides that when arrests are made of persons in the act of operating an illicit destillery, the arrested persons shall be taken forthwith before some judicial officer residing in the county where the arrests were made, or if none, in the county nearest to the place of arrest. Similar legislation, requiring that arrested persons be promptly taken before a committing authority, appears on the statute books of nearly all the states.<a class="footnote" href="#fn7" id="fn7_ref">7</a></p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">The purpose of this impressively pervasive requirement of criminal procedure is plain. A democratic society, in which respect for the dignity of all men is central, naturally guards against the misuse of the law enforcement process. Zeal in tracking down crime is not in itself an assurance of soberness of judgment. Disinterestendness in law enforcement does not alone prevent disregard of cherished liberties. Experience has therefore counseled that safeguards must be provided against the dangers of the overzealous as well as the despotic. The awful instruments of the criminal law cannot be entrusted to a single functionary. The complicated process of criminal justice is therefore divided into different parts, responsibility for which is separately vested in the various participants upon whom the criminal law relies for its vindication. Legislation such as this, requiring that the police must with reasonable promptness show legal cause for detaining arrested persons, constitutes an important safeguard&#8212;not only in assuring protection for the innocent but also in securing conviction of the guilty by methods that commend themselves to a progressive and self-confident society. For this procedural requirement checks resort to those reprehensible practices known as the 'third degree' which, though universally rejected as indefensible, still find their way into use. It aims to avoid all the evil implications of secret interrogation of persons accused of crime. It reflects not a sentimental but a sturdy view of law enforcement. It outlaws easy but self-defeating ways in which brutality is substituted for brains as an instrument of crime detection.<a class="footnote" href="#fn8" id="fn8_ref">8</a> A statute carrying such purposes is expressive of a general legislative policy to which courts should not be heedless when appropriate situations call for its application.</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">The circumstances in which the statements admitted in evidence against the petitioners were secured reveal a plain disregard of the duty enjoined by Congress upon federal law officers. Freeman and Raymond McNabb were arrested in the middle of the night at their home. Instead of being brought before a United States Commissioner or a judicial officer, as the law requires, in order to determine the sufficiency of the justification for their detention, they were put in a barren cell and kept there for fourteen hours. For two days they were subjected to unremitting questioning by numerous officers. Benjamin's confession was secured by detaining him unlawfully and questioning him continuously for five or six hours. The McNabbs had to submit to all this without the aid of friends or the benefit of counsel. The record leaves no room for doubt that the questioning of the petitioners took place while they were in the custody of the arresting officers and before any order of commitment was made. Plainly, a conviction resting on evidence secured through such a flagrant disregard of the procedure which Congress has commanded cannot be allowed to stand without making the courts themselves accomplices in wilful disobedience of law. Congress has not explicitly forbidden the use of evidence so procured. But to permit such evidence to be made the basis of a conviction in the federal courts would stultify the policy which Congress has enacted into law.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">Unlike England, where the Judges of the King's Bench have prescribed rules for the interrogation of prisoners while in the custody of police officers,<a class="footnote" href="#fn9" id="fn9_ref">9</a> we have no specific provisions of law governing federal law enforcement officers in procuring evidence from persons held in custody. But the absence of specific restraints going beyond the legislation to which we have referred does not imply that the circumstances under which evidence was secured are irrelevant in ascertaining its admissibility. The mere fact that a confession was made while in the custody of the police does not render it inadmissible. Compare Hopt v. Utah, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#583" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U.S. 574, 583</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#206" aria-description="Citation for case: Hopt v. People of Territory of Utah">4 S.Ct. 202, 206</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">28 L.Ed. 262</a></span>; Sparf v. United States, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#55" aria-description="Citation for case: Sparf v. United States">156 U.S. 51, 55, 715</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#275" aria-description="Citation for case: Sparf v. United States">15 S.Ct. 273, 275</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/" aria-description="Citation for case: Sparf v. United States">39 L.Ed. 343</a></span>; United States ex rel. Bilokumsky v. Tod, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U.S. 149, 157</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#57" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">44 S.Ct. 54, 57</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">68 L.Ed. 221</a></span>; Ziang Sun Wan v. United States, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1, 14</a></span>, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#3" aria-description="Citation for case: Ziang Sung Wan v. United States">45 S.Ct. 1, 3</a></span>, <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">69 L.Ed. 131</a></span>. But where in the course of a criminal trial in the federal courts it appears that evidence has been obtained in such violation of legal rights as this case discloses, it is the duty of the trial court to entertain a motion for the exclusion of such evidence and to hold a hearing, as was done here, to determine whether such motion should be granted or denied. Cf. Gouled v. United States, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#312" aria-description="Citation for case: Gouled v. United States">255 U.S. 298, 312, 313</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#266" aria-description="Citation for case: Gouled v. United States">41 S.Ct. 261, 266</a></span>, <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">65 L.Ed. 647</a></span>; Amos v. United States, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U.S. 313</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">41 S.Ct. 266</a></span>, <span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">65 L.Ed. 654</a></span>; Nardone v. United States, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U.S. 338, 341, 342</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#267" aria-description="Citation for case: Nardone v. United States">60 S.Ct. 266, 267, 268</a></span>, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>. The interruption of the trial for this purpose should be no longer than is required for a competent determination of the substantiality of the motion. As was observed in the Nardone case, supra, 'The civilized conduct of criminal trials cannot be confined within mechanical rules. It necessarily demands the authority of limited direction entrusted to the judge presiding in federal trials, including a well-established range of judicial discretion, subject to appropriate review on appeal in ruling upon preliminary questions of fact. Such a system as ours must, within the limits here indicated, rely on the learning, good sense, fairness and courage of federal trial judges.' <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U.S. at page 342</a></span>, 60 S.Ct. at page 268, <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">84 L.Ed. 307</a></span>.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">In holding that the petitioners' admissions were improperly received in evidence against them, and that having been based on this evidence their convictions cannot stand, we confine ourselves to our limited function as the court of ultimate review of the standards, formulated and applied by federal courts in the trial of criminal cases. We are not concerned with law enforcement practices except in so far as courts themselves become instruments of law enforcement. We hold only that a decent regard for the duty of courts as agencies of justice and custodians of liberty forbids that men should be convicted upon evidence secured under the circumstances revealed here. In so doing, we respect the policy which underlies Congressional legislation. The history of liberty has largely been the history of observance of procedural safeguards. And the effective administration of criminal justice hardly requires disregard of fair procedures imposed by law.</p>
    </div>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">Reversed.</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">Mr. Justice RUTLEDGE took no part in the consideration or decision of this case.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">Mr. Justice REED, dissenting.</p>
    </div>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">I find myself unable to agree with the opinion of the Court in this case. An officer of the United States was killed while in the performance of his duties. From the circumstances detailed in the Court's opinion, there was obvious reason to suspect that the petitioners here were implicated in firing the fatal shot from the dark. The arrests followed. As the guilty parties were known only to the McNabbs who took part in the assault at the burying ground, it was natural and proper that the officers would question them as to their actions.<a class="footnote" href="#fn1-1" id="fn1-1_ref">1</a></p>
    </div>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">The cases just cited show that statements made while under interrogation may be used at a trial if it may fairly be said that the information was given voluntarily. A frank and free confession of crime by the culprit affords testimony of the highest credibility and of a character which may be verified easily. Equally frank responses to officers by innocent people arrested under misapprehension give the best basis for prompt discharge from custody. The realization of the convincing quality of a confession tempts officials to press suspects unduly for such statements. To guard accused persons against the danger of being forced to confess, the law admits confessions of guilt only when they are voluntarily made. While the connotation of voluntary is indefinite, it affords an understandable label under which can be readily classified the various acts of terrorism, promises, trickery and threats which have led this and other courts to refuse admission as evidence to confessions.<a class="footnote" href="#fn2-1" id="fn2-1_ref">2</a> The cases cited in the Court's opinion show the broad coverage of this rule of law. Through it those coerced into confession have found a ready defense from injustice.</p>
    </div>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">Were the Court today saying merely that in its judgment the confessions of the McNabbs were not voluntary, there would be no occasion for this single protest. A notation of dissent would suffice. The opinion, however, does more. Involuntary confessions are not constitutionally admissible because violative of the provision of self-incrimination in the Bill of Rights. Now the Court leaves undecided whether the present confessions are voluntary or involuntary and declares that the confessions must be excluded because in addition to questioning the petitioners, the arresting officers failed promptly to take them before a committing magistrate. The Court finds a basis for the declaration of this new rule of evidence in its supervisory authority over the administration of criminal justice. I question whether this offers to the trial courts and the peace officers a rule of admissibility as clear as the test of the voluntary character of the confession. I am opposed to broadening the possibilities of defendants escaping punishment by these more rigorous technical requirements in the administration of justice. If these confessions are otherwise voluntary, civilized standards, in my opinion, are not advanced by setting aside these judgments because of acts of omission which are not shown to have tended toward coercing the admissions.</p>
    </div>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">Our police officers occasionally overstep legal bounds. This record does not show when the petitioners were taken before a committing magistrate. No point was made of the failure to commit by defendant or counsel. No opportunity was given to the officers to explain. Objection to the introduction of the confessions was made only on the ground that they were obtained through coercion. This was determined against the accused both by the Court, when it appraised the fact as to the voluntary character of the confessions, preliminarily to determining the legal question of their admissibility, and by the jury. The Court saw and heard witnesses for the prosecution and the defense. The defendants did not take the stand before the jury. The uncontradicted evidence does not require a different conclusion. The officers of the Alcohol Tax Unit should not be disciplined by overturning this conviction.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Officer Burke testified that the questioning Thursday night began at 6 P.M., Officer Kitts, at 7 P.M., and Officer Jakes, at 'possibly 6 or 7 o'clock'.</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> Here again Taylor's testimony is at variance with that of other officers. Officer Kitts estimated that the questioning Thursday night ended at 10 P.M., Officer Burke, at 11 P.M., and Officer Jakes, at midnight. No officer testified that the questioning that night lasted less than three hours.</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> Taylor testified that the McNabbs were brought back Friday morning 'probably about nine or nine-thirty'. None of the other officers could recall the exact time. Officer Burke thought 'it must have been after nine o'clock', while Officer Jakes guessed that it was 'somewhere around ten or eleven o'clock in the morning'.</p>
      </div>
      <div class="footnote" id="fn4">
        <a class="footnote" href="#fn4_ref">4</a>
        <p> Taylor testified that the reason for having Benjamin remove his clothes was that 'I was informed that he had gotten an injury running through the woods or that he had been hit by a stray shot. We didn't know whether or not this was true, and asked him to take his clothes off in order to examine him and find out.'</p>
      </div>
      <div class="footnote" id="fn5">
        <a class="footnote" href="#fn5_ref">5</a>
        <p> To determine the admissibility of the statements secured from the defendants while they were in the custody of the federal officers, the trial court conducted a preliminary examination in the absence of the jury. After hearing the evidence (consisting principally of the testimony of the defendants and the officers), the court concluded that the statements were admissible. An exception to this ruling was taken. When the jury was recalled, the witnesses for the Government repeated their testimony. The defendants rested upon their claim that the trial court erred in admitting these statements, and stood on their constitutional right not to take the witness stand before the jury. At the conclusion of the Government's case the defendants moved to exclude from the consideration of the jury the evidence relating to the admissions made by them. This motion was denied. The motion was renewed at the conclusion of the defendants' case, and again was denied. The court charged the jury that the defendants' admissions should be disregard if found to have been involuntarily made. The issue of law which was decided by the trial court in admitting the statements made by the petitioners did not become, therefore, a question of fact foreclosed by the jury's general verdict of guilty. Under these circumstances we have treated as facts only the testimony offered on behalf of the Government and so much of the petitioners' evidence as is neither contradicted by nor inconsistent with that of the Government.</p>
      </div>
      <div class="footnote" id="fn6">
        <a class="footnote" href="#fn6_ref">6</a>
        <p> The function of formulating rules of evidence in areas not governed by statute has always been one of the chief concerns of courts: 'The rules of evidence on which we practise today have mostly grown up at the hands of the judges; and, except as they may be really something more than rules of evidence, they may, in the main, properly enough be left to them to be modified and reshaped.' J. B. Thayer, A Preliminary Treatise on Evidence at the Common Law (1898) pp. 530, 531.</p>
      </div>
      <div class="footnote" id="fn7">
        <a class="footnote" href="#fn7_ref">7</a>
        <p> Alabama&#8212;Code, 1940, Tit. 15, &#167; 160; Arizona&#8212;Code, 1939, &#167;&#167; 44-107, 44-140, 44-141; Arkansas&#8212;Pope's Digest of Statutes, 1937, &#167;&#167; 3729, 3731; California&#8212;Penal Code, 1941, &#167;&#167; 821&#8212;29, 847&#8212;49; Colorado&#8212;Statutes, 1935, c. 48, &#167; 428; Connecticut&#8212;Gen.Stats.1930, &#167; 239; Delaware&#8212;Rev.Code, 1935, &#167;&#167; 4456, 5173; District of Columbia&#8212;Code, 1940, &#167;&#167; 4-140, 23-301; Florida&#8212;Statutes, 1941, &#167;&#167; 901.06, 901.23; Georgia&#8212;Code, 1933, &#167;&#167; 27-210, 27-212; Idaho&#8212;Code, 1932, &#167;&#167; 19-515, 19-518, 19-614, 19-615; Illinois&#8212;Rev.Stats., 1941, c. 38, &#167;&#167; 655, 660; Indiana&#8212;Baldwin's Stats.Ann.1934, &#167; 11484; Iowa&#8212;Code, 1939, &#167;&#167; 13478, 13481, 13486, 13488; Kansas Gen.Stats., 1935, &#167; 62-610; Kentucky&#8212;Code, 1938, &#167;&#167; 45, 46; Louisiana&#8212;Code of Criminal Procedure, 1932, arts. 66, 79, 80; Maine&#8212;Rev.Stats., 1930, c. 145, &#167; 9; Massachusetts-Gen.Laws, 1932, c. 276, &#167;&#167; 22, 29, 34; Michigan&#8212;Stats.Ann.1938, &#167;&#167; 28.863, 28.872, 28.873, 28.885; Minnesota&#8212;Mason's Stats., 1927, c. 104, &#167;&#167; 10575, 10581; Mississippi&#8212;Code, 1930, c. 21, &#167; 1230; Missouri Rev.Stats.1939, &#167;&#167; 3862, 3883, Mo.R.S.A. &#167;&#167; 3862, 3883; Montana Rev.Code, 1935, &#167;&#167; 11731, 11739, 11740; Nebraska&#8212;Comp.Stats., 1929, &#167; 29-412; Nevada&#8212;Comp.Laws, 1929, &#167;&#167; 10744&#8212;48, 10762&#8212;64; New Hampshire&#8212;Pub.Laws, 1926, c. 364, &#167; 13; New Jersey&#8212;Rev.Stats., 1937, &#167; 2:216&#8212;9, N.J.S.A. 2:216&#8212;9; New York&#8212;Code of Criminal Procedure, 1939, &#167;&#167; 158, 159, 165, 185; North Carolina&#8212;Code, 1939, &#167;&#167; 4528, 4548; North Dakota&#8212;Comp.Laws, 1913, &#167;&#167; 10543, 10548, 10576, 10578; Ohio&#8212;Throckmorton's Code, 1940, &#167;&#167; 13432-3, 13432-4; Oklahoma&#8212;Statutes, 1941, Tit. 22, &#167;&#167; 176, 177, 181, 205; Oregon Code, 1930, &#167;&#167; 13-2117, 13-2201; Pennsylvania&#8212;Purdon's Stats.Ann., Perm.ed., Tit. 19, &#167;&#167; 3, 4; Rhode Island&#8212;Gen.Laws, 1938, c. 625, &#167; 68; South Carolina&#8212;Code, 1942, &#167;&#167; 907, 920; South Dakota&#8212;Code, 1939, &#167;&#167; 34-1608, 34-1619 to 34-1624; Tennessee&#8212;Michie's Code, 1938, &#167;&#167; 11515, 11544; Texas&#8212;Vernon's Code of Criminal Procedure, 1936, Arts. 233&#8212;235; Utah&#8212;Rev.Stats., 1933, &#167;&#167; 105-4-4, 105-4-5, 103-26-51; Virginia&#8212;Code, 1942, &#167;&#167; 4826, 4827a; Washington Rev.Stats., 1932, &#167; 1949; West Virginia&#8212;Code, 1937, &#167; 6150; Wisconsin&#8212;Statutes, 1941, &#167; 361.08; Wyoming&#8212;Rev.Stats., 1931, &#167;&#167; 33-108, 33-110, 33-115.</p>
      </div>
      <div class="footnote" id="fn8">
        <a class="footnote" href="#fn8_ref">8</a>
        <p> 'During the discussions which took place on the Indian Code of Criminal Procedure in 1872 some observations were made on the reasons which occasionally lead native police officers to apply torture to prisoners. An experienced civil officer observed, 'There is a great deal of laziness in it. It is far pleasanter to sit comfortably in the shade rubbing red pepper into a poor devil's eyes than to go about in the sun hunting up evidence.' This was a new view to me, but I have no doubt of its truth.' Sir James Fitzjames Stephen, A History of the Criminal Law of England (1883) vol. 1, p. 442 note. Compare &#167;&#167; 25 and 26 of the Indian Evidence Act 1872).</p>
      </div>
      <div class="footnote" id="fn9">
        <a class="footnote" href="#fn9_ref">9</a>
        <p> In 1912 the Judges of the King's Bench, at the request of the Home Secretary, issued rules for the guidance of police officers. See Rex v. Voisin, L.R. (1918) 1 K.B 531, 539. These rules were amended in 1918, and in 1930 a circular was issued by the Home Office, with the approval of the Judges, in order to clear up difficulties in their construction. 6 Police Journal (1933) 352-56, containing the texts of the Judge's Rules and the Circular. See Report of the Royal Commission on Police Powers and Procedure (1929) Cmd. 3297. Although the Rules do not have the force of law, Rex v. Voisin, supra, the English courts insist that they be strictly observed before admitting statements made by accused persons while in the custody of the police. See 1 Taylor on Evidence (12th ed. 1931) pp. 556&#8212;562; 'Questioning an Accused Person', 92 Justice of the Peace and Local Government Review 743, 758 (1928); Keedy, Preliminary Examination of Accused Persons in England, 73 Proceedings of American Philosophical Society 103 (1934). For a dramatic illustration of the English attitude towards interrogation of arrested persons by the police, see Inquiry in regard to the Interrogation by the Police of Miss Savidge (1928) Cmd. 3147.</p>
      </div>
      <div class="footnote" id="fn1-1">
        <a class="footnote" href="#fn1-1_ref">1</a>
        <p> Hopt v. Utah, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#584" aria-description="Citation for case: Hopt v. People of Territory of Utah">110 U.S. 574, 584</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/#207" aria-description="Citation for case: Hopt v. People of Territory of Utah">4 S.Ct. 202, 207</a></span>, <span class="citation" data-id="91057"><a href="/opinion/91057/hopt-v-people-of-territory-of-utah/" aria-description="Citation for case: Hopt v. People of Territory of Utah">28 L.Ed. 262</a></span>; Sparf &amp; Hansen v. United States, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#55" aria-description="Citation for case: Sparf v. United States">156 U.S. 51, 55, 715</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#275" aria-description="Citation for case: Sparf v. United States">15 S.Ct. 273, 275</a></span>, <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/" aria-description="Citation for case: Sparf v. United States">39 L.Ed. 343</a></span>; Pierce v. United States, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">160 U.S. 355</a></span>, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">16 S.Ct. 321</a></span>, <span class="citation" data-id="94327"><a href="/opinion/94327/pierce-v-united-states/" aria-description="Citation for case: Pierce v. United States">40 L.Ed. 454</a></span>; Wilson v. United States, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#623" aria-description="Citation for case: Wilson v. United States">162 U.S. 613, 623</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#899" aria-description="Citation for case: Wilson v. United States">16 S.Ct. 895, 899</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">40 L.Ed. 1090</a></span>; cf. State ex rel. Bilokumsky v. Tod, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#157" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">263 U.S. 149, 157</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/#57" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">44 S.Ct. 54, 57</a></span>, <span class="citation" data-id="100280"><a href="/opinion/100280/united-states-ex-rel-bilokumsky-v-tod/" aria-description="Citation for case: United States Ex Rel. Bilokumsky v. Tod">68 L.Ed. 221</a></span>.</p>
      </div>
      <div class="footnote" id="fn2-1">
        <a class="footnote" href="#fn2-1_ref">2</a>
        <p> 'In short, the true test of admissibility is that the confession is made freely, voluntarily and without compulsion or inducement of any sort.' Wilson v. United States, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#623" aria-description="Citation for case: Wilson v. United States">162 U.S. 613, 623</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/#899" aria-description="Citation for case: Wilson v. United States">16 S.Ct. 895, 899</a></span>, <span class="citation" data-id="94454"><a href="/opinion/94454/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">40 L.Ed. 1090</a></span>; Lisenba v. California, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#239" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 239</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#291" aria-description="Citation for case: Lisenba v. California">62 S.Ct. 280, 291</a></span>, <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">86 L.Ed. 166</a></span>.</p>
      </div>
    </div>
    
```

---
