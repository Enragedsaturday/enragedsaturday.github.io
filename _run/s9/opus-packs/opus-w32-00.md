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

## GROUP: content/cases/Ex parte Jackson.md  (`case`, 5 assertions)

### content_page

```
---
title: Ex parte Jackson
type: case
citation: "96 U.S. 727 (1878)"
parallel_cite: 24 L. Ed. 877
neutral_cite: 1877 U.S. LEXIS 1718
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1878
date_decided: 1878-05-13
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
  opinion_url: "https://www.courtlistener.com/opinion/89759/ex-parte-jackson/"
  cluster_id: 89759
  opinion_id: null
  identity_checked: true
lake:
  record_id: Ex parte Jackson
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Common Law Origins]]"
    role: Historical / origin
related:
  - "[[Common Law Origins]]"
  - "[[Carpenter v. United States]]"
  - "[[United States v. Jacobsen]]"
tags:
  - case
  - fourth-amendment
  - historical
  - sealed-mail
  - warrant-requirement
  - papers
  - origin
holding: "Sealed letters and packages committed to the mail are within the Fourth Amendment's protection to the same extent as papers kept in one's own home, and may be opened and examined only under a warrant issued on oath and particularly describing the thing to be seized — though Congress may constitutionally exclude certain matter, such as lottery circulars, from the mails."
aliases:
  - Ex parte Jackson
  - "Ex parte Jackson (1878)"
---

# Ex parte Jackson

*96 U.S. 727 (1878)* · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Historical origin — good law, rendered as history (⚪ unverified, pending S9)**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the historical framing below is authored orientation, not machine-certified. special: history-render — rendered as a foundational ORIGIN (role: Historical / origin), and it remains good law (NOT overruled). Identity cluster 89759 → opinion 89759 (Field, J.; 96 U.S. 727, decided 1878, October Term 1877). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*733`); the CL scan carries minor OCR artifacts (stray marks in "searches' and seizures" and "can only 'be opened"), normalized to the U.S. Reports text and flagged in Sources. S9 promotes. -->

## Background
Jackson was convicted under a federal statute that barred matter concerning lotteries from the mails, for depositing in the post a circular relating to a lottery. He sought a writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] in the Supreme Court, contending that Congress lacked power to exclude such material from the mails and that examining private mail to enforce the ban would violate constitutional guarantees. The case required the Court both to define Congress's power over the mails and to explain what Fourth Amendment protection attaches to items entrusted to the postal system.

## Issue
Whether Congress may exclude lottery circulars from the mails, and — for our purposes — whether sealed letters and packages in the mail are protected against being opened and inspected without a warrant.

## Rule
The Court drew a line between sealed matter (letters and sealed packages), which is fully protected, and open matter (newspapers and printed circulars left open to inspection), which is not. As to the former it announced the enduring rule: "The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures extends to their papers, thus closed against inspection, wherever they may be. Whilst in the mail, they can only be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one's own household." — 96 U.S. at 733. ^pin-733

## Application
Because a citizen's sealed correspondence in the mail is as guarded from inspection as papers kept at home, the government may not open it without a warrant satisfying the Fourth Amendment's oath and [[Particularity|particularity]] requirements. That protection did not, however, disable Congress from regulating what may travel through the mails: the power to exclude lottery circulars addressed *what could be carried*, not the warrantless opening of anyone's sealed mail, and could be enforced by refusing to transmit or by prosecuting deposits of forbidden matter. Jackson's conviction for depositing a lottery circular therefore stood.

## Conclusion
The writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] was **denied**; the conviction stood. Field, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Status: Unverified — rendered as history; still good law.** This page is authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Ex parte Jackson* is preserved here as a **historical origin**, not as superseded law — its sealed-mail principle has never been overruled and remains foundational. It is the Court's earliest holding that the Fourth Amendment follows a person's sealed papers into the hands of a third party (the Post Office), a principle carried forward across more than a century: *[[United States v. Van Leeuwen]]* (1970) (mailed packages), *[[United States v. Jacobsen]]* (1984), and echoed in the digital-privacy line, *[[Carpenter v. United States]]* (2018). Teach it as the origin point of the warrant requirement for sealed communications entrusted to others — an antecedent, not an artifact.

## Appears on
- [[Common Law Origins]] — *Historical / origin*

## Sources
- [*Ex parte Jackson*, 96 U.S. 727 (1878)](https://www.courtlistener.com/opinion/89759/ex-parte-jackson/) — pinpoint: 733 (Field, J., for the Court; the CL opinion text carries the reporter star `*733` at the start of the quoted passage). Rule quote string-matched to the CL opinion text 2026-07-07; the CL source is a period OCR scan with minor artifacts (e.g., a stray apostrophe in "searches' and seizures" and a stray quotation mark in "can only 'be opened") which were normalized to the U.S. Reports text — the substance is identical.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9640c60e8ed858d3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "96 U.S. 727 (1878)", "court": "U.S. Supreme Court", "neutral_cite": "1877 U.S. LEXIS 1718", "official_citation_present": true, "parallel_cite": "24 L. Ed. 877", "title": "Ex parte Jackson", "year": "1878"}}
{"assertion_id": "0c0c88161adae9e1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Sealed letters and packages committed to the mail are within the Fourth Amendment's protection to the same extent as papers kept in one's own home, and may be opened and examined only under a warrant issued on oath and particularly describing the thing to be seized — though Congress may constitutionally exclude certain matter, such as lottery circulars, from the mails.", "title": "Ex parte Jackson"}}
{"assertion_id": "40562f8264a1a5f3", "dimension": "support", "kind": "home_role", "locator": {"home": "Common Law Origins"}, "payload": {"home": "Common Law Origins", "role": "Historical / origin", "title": "Ex parte Jackson"}}
{"assertion_id": "4929930f0ad0b32c", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Ex parte Jackson", "varies_by_point": "false"}}
{"assertion_id": "ce3ba69ee7fd0ed0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ex parte Jackson"}}
```

### lake record — Ex parte Jackson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ex parte Jackson",
  "status": "under_review",
  "identity": {
    "case_name": "Ex Parte Jackson",
    "case_name_short": "",
    "case_name_full": "Ex Parte Jackson",
    "input_case_name": "Ex parte Jackson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1878-05-13",
    "year": 1878,
    "docket": null,
    "cluster_id": 89759,
    "lead_opinion_id": 89759,
    "sibling_ids": [],
    "absolute_url": "/opinion/89759/ex-parte-jackson/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "96 U.S. 727",
      "volume": "96",
      "reporter": "U.S.",
      "page": "727",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "24 L. Ed. 877",
        "volume": "24",
        "reporter": "L. Ed.",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1877 U.S. LEXIS 1718",
        "volume": "1877",
        "reporter": "U.S. LEXIS",
        "page": "1718",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "96 U.S. 727",
        "volume": "96",
        "reporter": "U.S.",
        "page": "727",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 L. Ed. 877",
        "volume": "24",
        "reporter": "L. Ed.",
        "page": "877",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1877 U.S. LEXIS 1718",
        "volume": "1877",
        "reporter": "U.S. LEXIS",
        "page": "1718",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "96 U.S. 727",
    "official_selection": {
      "court_class": "scotus",
      "selected": "96 U.S. 727",
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
    "date_created": "2026-07-06T13:48:00Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:48:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:48:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:48:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "ex-parte-jackson--89759",
      "to_record_id": "Ex parte Jackson",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Ex parte Jackson

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b742-5">
  Mr. Justice Field,
 </author>
<p id="A9Yc">
  after stating the case, delivered the opinion of the court.
 </p>
<p id="b742-6">
  The power vested in Congress “to establish post-oliices and post-roads ” has been practically construed, since the foundation of the government, to authorize not merely the designation of the routes over which the mail shall be carried, and the offices where letters and other documents shall be received to be distributed or forwarded, but the. carriage of. the mail, and all measures necessary to .secure-its safe and speedy transit, and the prompt delivery of its contents. The validity of legislation prescribing what should be carried, and its weight and form, and the charges to which it should be subjected,’has never been questioned. What .should be mailable has varied at different times, changing with the facility of transportation .over the post-roads. At one time, only letters, newspapers, magazines, pamphlets, and other printed matter, not exceeding eight ounces in weight, were carried; afterwards books were added to the list.; and now small packages of merchandise, not exceeding a prescribed weight, as well as books Rnd printed matter of all kinds, are transported in the mail. The power possessed by Congress embraces the regulation of the entire postal system of the country. The right to designate what shall be carried necessarily involves the right to determine what shall be excluded. The difficulty attending the subject arises, not from the want of power in Congress to ,prescribe regulations as to what shall constitute.mail matter, but from the necessity of enforcing them consistently with rights reserved to the people, of far, greater importance than the transportation of the mail. In their en
  <span citation-index="1" class="star-pagination" label="733"> 
   *733
   </span>
  forcement, a. distinction is to be made between different kinds ■of mail matter, — between wbat is intended to be kept free from inspection, such as letters, and sealed packages subject to letter postage; and what is open to inspection, such as newspapers, magazines, pamphlets, and other printed matter, purposely left in'a condition to be examined. Lettersand.sealed packages of this kind in the mail are as fully guarded from examination and inspection, except as to their outward form and weight, as. if they were retained by the parties forwarding them in their own domiciles. The constitutional guaranty of the right of the people to be secure in their papers against unreasonable searches’ and seizures extends to their papers, thus closed against inspection, wherever they may be. ■ Whilst in the mail, they can only "be opened and examined under like warrant, issued upon similar oath or affirmation, particularly describing the thing to be seized, as is required when papers are subjected to search in one’s, own household. No law of- Congress can place in the hands of officials connected with the postal service any authority to invade the secrecy of letters and such sealed’ packages in the mail; and all regulations adopted as to mail matter of this kind must .be in subordination to the great principle embodied in the fourth amendment of the Constitution.
 </p>
<p id="b743-5">
  Nor can any regulations be enforced against the transportation of printed matter in the mail, which is open to examination, so as to interfere in any manner with the freedom of the press. Liberty of circulating is as essential to that freedom as liberty of publishing; indeed, without the circulation, the publication would be of little value. If, therefore, printed matter be excluded from the mails, its .transportation in any other way cannot be forbidden by 'Congress.
 </p>
<p id="b743-6">
  In 1836’, the question as to the power of Congress.to exclude publications from the mail was discussed in the Senate; and the prevailing opinion of its members, as expressed in debate, was against the existence of the power. President Jackson, in his annual message of the previous year, had referred to the attempted circulation through the mail of inflammatory appeals, addressed to the passions of the slaves, in prints, and in various publications, tending to stimulate them to insurrection; and suggested to Congress the propriety of passing a law prohibiting,
  <span citation-index="1" class="star-pagination" label="734"> 
   *734
   </span>
  under severe penalties, such circulation of “ incendiary publica tions ” in the Southern States. In the Senate, that portion of the message was referred to a select committee, of which Mr. Calhoun was chairman; and he made -an elaborate report on the subject, in which he contended that-it belonged to the. States, and not to Congress, to determiné what is and what is not calculated to disturb their, security., and'that to'hold otherwise would be fatal to the States; for if Congress might determine what papers were incendiary, and as such prohibit their circulation through' the mail, it might also determine what were not incendiary, and enforce their circulation. Whilst, therefore, condemning in the strongest terms the circulation of the publications, he .insisted that Congress had not the power to pass a law prohibiting their transmission through the mail, on the ground that it would abridge the liberty of the'press. “ To understand,” he S,aid, “ more- fully • the extent of the control which the right of prohibiting circulation through the mail would give to'the government over the press, iff must be borne in mind that the power of Congress over the post-office and the mail is an exclusive power. It must also be remembered that Congress, in the exercise of this power, may declare any road or navigable water to be a post-road; and that, by the act of 1825, it is providéd ‘ that no stage, or other vehicle which regularly performs trips on a poSt-road, or on a road parallel to it, shall carry letters.’ The same provision extends to packets, boats, or other vessels on navigable waters. Like provision may be exténded to newspapers and pamphlets, which, if it ,be admitted that Congress has the right to discriminate in reference to their character, what papers shall or what shall not be transmitted by the mail, would subject the freedom of the press, on all subjects, political, moral, and religious, completely to its will and', pleasure. It would in fact, in some respects, more effectually control the freedom of the press than any sedition law, however severe its penalties.” Mr. Calhoun, at the same time, contended that when a State had pronounced certaijn publications 'to be dangerous to its peace, and prohibited théir circulation, it was the duty of Congress to respect its laws and co-operate- in their enforcement; and whilst, therefore, Congress could not prohibit the transmission of the ipcendiarv documejats through the mails,
  <span citation-index="1" class="star-pagination" label="735"> 
   *735
   </span>
  it could prevent their delivery by the postmasters in the States where their circulation was forbidden. In the discussion upon the bill reported by :,hitfi, similar views against the power of Congress Were expressed by other senators, who did not concur in the opinion that the delivery of - papers could be prevented when their transmission was permitted.
 </p>
<p id="b745-3">
  Great reliance is placed by the petitioner upon these views, coming, as they did in smany' instances^ from men alike distinguished a¡s jurists and statesmen. But it is evident that they were founded upon the assumption that it was competent for Congress to prohibit the transportation of newspapers and pamphlets over postal-routes in any other.way than by mail; and of course it would follow,] that if, with such a prohibition, the transportation in the mail could also be forbidden, the circulation of the documents would be destroyed, and a fatal blow given to the freedom' of ■ the press. But we do not think that Congress possesses the power to prevent the transportation in other ways, as merchandise, of matter which it ■ excludes from the mails. - To give efficiency to its regulations and prevent rival postal systems, it .may perhaps prohibit the carriage by others for hire, over postal routes, of articles which legitimately constitute mail matter, in the sense in which those terms were used when the Constitution was adopted, consisting of letters, and of newspapers and pamphlets, when not sent as merchandise ; but further than this its power of prohibition cannot extend.
 </p>
<p id="b745-4">
  Whilst regulations excluding matter from the mail cannot be enforced in a way which would require or permit an examinar tion into letters, or sealed packages-subject to letter postage, without warrant, issued upon oath or affirmation, in the search for prohibited matter, they may be enforced upon-competent evidence of their violation obtained in other ways; as from the parties receiving the letters or packages, or from agents-depositing them in the post-office, or others cognizant of the facts.' And as to objectionable printed matter, which is open to examination, the regulations may be enforced .in a similar way, by the imposition of penalties for their violation through the courts, and, in some cases, by the direct action of the officers' of the postal servicé. In many instances, those officers can act
  <span citation-index="1" class="star-pagination" label="736"> 
   *736
   </span>
  upon their- own inspection, and, from the nature of the case, must act without other proof; as. where the postage is not prepaid, or where there' is an excess of weight over the amount prescribed, or where the object is exposed, and shows unmistakably -that it is prohibited, as in the case of an obscene picture or print. In such cases, no difficulty arisés, and no principle is violated, in excluding the prohibited, articles or refusing to forward them. The. evidence'respecting'them is seen by- every one, and is in its nature conclusive.
 </p>
<p id="b746-3">
  " In excluding various' articles from, the mail, the object of Congress has.- not been to interfere with the freedom of the press, or with any other rights of the people; but -to refuse its facilities for the distribution of matter deemed injurious to the public morals. Thus, by the act of March 3, 1873, Congress declared. “ that no obscene, lewd, or lascivious book, pamphlet, picture, paper, print, or other publication of an indecent character, or any article or thing designed or intended for the prevention of conception or procuring of abortion, nor any, article or thing intended or adapted for any indecent or immoral use or- nature, nor any written or. printed card, circular, book, •pamphlet, advertisement, or notice of any kind, giving information, directly or indirectly, .where, or how; or of whom, or by what means, either- of the things before' mentioned may be-obtained or made, nor any. letter upon the envelope of- which, or. postal-card upon which indecent or scurrilous epithets may' be written or printed, shall be carried in the -mail; and any person who shall knowingly deposit, or cause to be deposited, for mailing or delivery, any of the hereinbefore mentioned arth cles or things, . . . shall' be deemed guilty of á misdemeanor, and, on conviction thereof, shall,' for every offence, be fined, not less than $100, nor more .than $5,000, or imprisonment at hard labor not less than one year nor more ’ than tefa years, or both, in the discretion of the judge.”
 </p>
<p id="b746-4">
  All that Congress meant by this act-was, that the mail should not be used to transport such corrupting publications and articles, and that any one who\attempted to use it for that purpose should be-punished. The same inhibition has been extended to circulars concerning lotteries, — institutions which are supposed to have a demoralizing, influence- upon the people. There is no
  <span citation-index="1" class="star-pagination" label="737"> 
   *737
   </span>
  question before us as to the evidence upon which thé conviction of the petitioner was had; nor does it appear whether the envelope in which the prohibited circular was deposited in the mail was sealed or left open for examination. The only question for our determination relates to the constitutionality of the act; and of that wé have no doubt.
 </p>
<p id="b747-3">
  The commitment of the petitioner to the county jail, until his fine was paid, was within the discretion of the court under the statute.
 </p>
<p id="b747-4">
  As there is an exemplified copy of the record of the petitioner’s indictment and conviction accompanying the petition, .the merits of his case havé been considered at his request upon this application; and, as we are of opinion that his imprisonment is legal, no object would be subserved by issuing the writs; they are therefore
 </p>
<p id="b747-5">
<em>
   Denied.
  </em>
</p>
</opinion>
```

---

## GROUP: content/cases/FBI v. Fazaga.md  (`case`, 6 assertions)

### content_page

```
---
title: FBI v. Fazaga
type: case
citation: "595 U.S. 344 (2022)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2022
date_decided: ""
docket: 20-828
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
  opinion_url: "https://www.courtlistener.com/opinion/6448059/fbi-v-fazaga/"
  cluster_id: 6448059
  opinion_id: null
  identity_checked: true
lake:
  record_id: FBI v. Fazaga
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Suing Federal Officers]]"
    role: Recent development
  - page: "[[Electronic Surveillance and Title III]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Electronic Surveillance and Title III]]"
tags:
  - case
  - state-secrets-privilege
  - fisa
  - electronic-surveillance
  - national-security
holding: "The Foreign Intelligence Surveillance Act's § 1806(f) does not displace the state-secrets privilege; FISA's silence about that privilege and the two regimes' incompatible procedures mean § 1806(f) neither abrogates the privilege nor supplies a substitute for it."
---

# FBI v. Fazaga

*595 U.S. 344 (2022)* (No. 20-828) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 6448059 → opinion 6320170; quote string-matched to the CL opinion text 2026-07-07 (CL carries the slip opinion, 595 U.S. ___; the Held is on the syllabus page, 595 U.S. 344). S9 promotes. -->

## Background
Three Muslim residents of Southern California alleged that the FBI illegally surveilled them and their community because of their religion, using a confidential informant who infiltrated local mosques. They sued the Government and individual agents under the Foreign Intelligence Surveillance Act, the Fourth Amendment, and other provisions. The Government invoked the "state secrets" privilege and moved to dismiss most of the claims, arguing that litigating them would require disclosing counter-intelligence information vital to national security. The District Court dismissed those claims under the privilege, but the Ninth Circuit reversed in relevant part, holding that FISA's § 1806(f) — which lets a court review the legality of electronic surveillance in camera and [[Common Legal Terms#ex-parte|ex parte]] — displaced the state-secrets privilege for electronic-surveillance evidence.

## Issue
Whether 50 U.S.C. § 1806(f) of FISA displaces the state-secrets privilege and its dismissal remedy with respect to electronic-surveillance evidence.

## Rule
The state-secrets privilege protects against court-ordered disclosure of state and military secrets, and it is not lightly abrogated: "the privilege should not be held to have been abrogated or limited unless Congress has at least used clear statutory language." FISA contains no such language — it makes no reference to the state-secrets privilege at all — and § 1806(f)'s procedures are not incompatible with the privilege in any event, because the statute and the privilege ask different questions, authorize different relief, and follow different procedures. The Court therefore held: "Section 1806(f) does not displace the state secrets privilege." — 595 U.S. at 344 (Syllabus; holding developed at 350–356). ^pin-344

## Application
Even accepting the respondents' broad reading of § 1806(f), the Court found no clash with the privilege: § 1806(f) turns on whether the surveillance of the aggrieved person was lawfully authorized and conducted, while the privilege turns on whether disclosure would harm national security regardless of the evidence's lawfulness; the two also differ in the relief they permit and in their procedures (in camera and [[Common Legal Terms#ex-parte|ex parte]] review under the statute versus non-disclosure under the privilege). Because it resolved the case on this narrow, alternative ground, the Court expressly declined to decide which party's interpretation of § 1806(f) was correct, whether the Government's evidence was in fact privileged, or whether dismissal on the pleadings was proper.

## Conclusion
The judgment of the Ninth Circuit was **reversed** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Alito, J., delivered the opinion for a unanimous Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Fazaga* preserves the state-secrets privilege as a threshold obstacle to civil suits — including constitutional claims against federal agents — challenging foreign-intelligence electronic surveillance; it is a FISA/§ 1806(f) decision and does not itself resolve the merits of the plaintiffs' surveillance claims.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*
- [[Electronic Surveillance and Title III]] — *Related (cross-doctrine)*

## Sources
- [*FBI v. Fazaga*, 595 U.S. 344 (2022)](https://www.courtlistener.com/opinion/6448059/fbi-v-fazaga/) — pinpoint: 344 (holding; developed at 350–356); quote string-matched to the CL slip-opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d0e4cc17200f42d7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "595 U.S. 344 (2022)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "FBI v. Fazaga", "year": "2022"}}
{"assertion_id": "7228bddc27936a06", "dimension": "support", "kind": "home_role", "locator": {"home": "Suing Federal Officers"}, "payload": {"home": "Suing Federal Officers", "role": "Recent development", "title": "FBI v. Fazaga"}}
{"assertion_id": "adc95c14c8bfa0ce", "dimension": "support", "kind": "home_role", "locator": {"home": "Electronic Surveillance and Title III"}, "payload": {"home": "Electronic Surveillance and Title III", "role": "Related (cross-doctrine)", "title": "FBI v. Fazaga"}}
{"assertion_id": "b85227265cf0588f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Foreign Intelligence Surveillance Act's § 1806(f) does not displace the state-secrets privilege; FISA's silence about that privilege and the two regimes' incompatible procedures mean § 1806(f) neither abrogates the privilege nor supplies a substitute for it.", "title": "FBI v. Fazaga"}}
{"assertion_id": "7360814b8455edd5", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "FBI v. Fazaga", "varies_by_point": "false"}}
{"assertion_id": "841ac4fe419a17c0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "FBI v. Fazaga"}}
```

### lake record — FBI v. Fazaga

```json
{
  "schema_version": "s2.v1",
  "record_id": "FBI v. Fazaga",
  "status": "under_review",
  "identity": {
    "case_name": "FBI v. Fazaga",
    "case_name_short": "Fazaga",
    "case_name_full": "",
    "input_case_name": "Federal Bureau of Investigation v. Fazaga",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2022,
    "docket": "20-828",
    "cluster_id": 6448059,
    "lead_opinion_id": 6320170,
    "sibling_ids": [],
    "absolute_url": "/opinion/6448059/fbi-v-fazaga/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "595 U.S. 344",
      "volume": "595",
      "reporter": "U.S.",
      "page": "344",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "595 U.S. 344",
        "volume": "595",
        "reporter": "U.S.",
        "page": "344",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "595 U.S. 344",
    "official_selection": {
      "court_class": "scotus",
      "selected": "595 U.S. 344",
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
    "date_created": "2026-07-06T12:26:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "federal-bureau-of-investigation-v-fazaga--6448059",
      "to_record_id": "FBI v. Fazaga",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — FBI v. Fazaga

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

    FEDERAL BUREAU OF INVESTIGATION ET AL. v.
                FAZAGA ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

    No. 20–828.      Argued November 8, 2021—Decided March 4, 2022
Respondents Yassir Fazaga, Ali Malik, and Yasser Abdel Rahim, mem-
  bers of Muslim communities in California, filed a putative class action
  against the Federal Bureau of Investigation and certain Government
  officials, claiming that the Government subjected them and other Mus-
  lims to illegal surveillance under the Foreign Intelligence Surveillance
  Act of 1978 (FISA). FISA provides special procedures for use when the
  Government wishes to conduct foreign intelligence surveillance. Rele-
  vant here, FISA provides a procedure under which a trial-level court
  or other authority may consider the legality of electronic surveillance
  conducted under FISA and order specified forms of relief. See 50
  U. S. C. §1806(f). The Government moved to dismiss most of respond-
  ents’ claims under the “state secrets” privilege. See, e.g., General Dy-
  namics Corp. v. United States, 563 U. S. 478. After reviewing both
  public and classified filings, the District Court held that the state se-
  crets privilege required dismissal of all respondents’ claims against the
  Government, except for one claim under §1810, which it dismissed on
  other grounds. The District Court determined dismissal appropriate
  because litigation of the dismissed claims “would require or unjustifi-
  ably risk disclosure of secret and classified information.” 884 F. Supp.
  2d 1022, 1028–1029. The Ninth Circuit reversed in relevant part,
  holding that “Congress intended FISA to displace the state secrets
  privilege and its dismissal remedy with respect to electronic surveil-
  lance.” 965 F. 3d 1015, 1052.
Held: Section 1806(f) does not displace the state secrets privilege. Pp. 7–
 13.
    (a) The case requires the Court to determine whether FISA affects
 the availability or scope of the long-established “Government privilege
2                              FBI v. FAZAGA

                                   Syllabus

    against court-ordered disclosure of state and military secrets.” General
    Dynamics Corp., 563 U. S., at 484. Congress enacted FISA to provide
    special procedures for use when the Government wishes to conduct for-
    eign intelligence surveillance in light of the special national-security
    concerns such surveillance may present. See Clapper v. Amnesty Int’l
    USA, 568 U. S. 398, 402. When information is lawfully gathered pur-
    suant to FISA, §1806 permits its use in judicial and administrative
    proceedings but specifies procedures that must be followed before that
    is done. Subsection (f) of §1806 permits a court to determine whether
    information was lawfully gathered “in camera and ex parte” if the “At-
    torney General files an affidavit under oath that disclosure or an ad-
    versary hearing would harm the national security of the United
    States.” §1806(f).
       Central to the parties’ argumentation in this Court, and to the Ninth
    Circuit’s decision below, is the correct interpretation of §1806(f). The
    Ninth Circuit’s conclusion that Congress intended FISA to displace the
    state secrets privilege rested in part on its conclusion that §1806(f)’s
    procedures applied to this case. The Government contends that the
    Ninth Circuit erred because §1806(f) is a narrow provision that applies
    only when an aggrieved person challenges the admissibility of surveil-
    lance evidence. Respondents interpret §1806(f) more broadly, arguing
    that it also can be triggered when a civil litigant seeks to obtain secret
    surveillance information, as respondents did here, and when the Gov-
    ernment moves to dismiss a case pursuant to the state secrets privi-
    lege. The Court does not resolve the parties’ dispute about the mean-
    ing of §1806(f) because the Court reverses the Ninth Circuit on an
    alternative ground. Pp. 7–9.
       (b) Section 1806(f) does not displace the state secrets privilege, for
    two reasons. Pp. 9–13.
         (1) The text of FISA weighs heavily against the argument that
    Congress intended FISA to displace the state secrets privilege. The
    absence of any reference to the state secrets privilege in FISA is strong
    evidence that the availability of the privilege was not altered when
    Congress passed the Act. Regardless of whether the state secrets priv-
    ilege is rooted only in the common law (as respondents argue) or also
    in the Constitution (as the Government argues), the privilege should
    not be held to have been abrogated or limited unless Congress has at
    least used clear statutory language. See Norfolk Redevelopment and
    Housing Authority v. Chesapeake & Potomac Telephone Co. of Va., 464
    U. S. 30, 35; Jennings v. Rodriguez, 583 U. S. __, __. P. 9.
         (2) Even on respondents’ interpretation of §1806(f), nothing about
    the operation of §1806(f) is incompatible with the state secrets privi-
    lege. Although the Ninth Circuit and respondents view §1806(f) and
                      Cite as: 595 U. S. ____ (2022)                      3

                                 Syllabus

  the privilege as “animated by the same concerns” and operating in fun-
  damentally similar ways, that is simply wrong. As an initial matter,
  it seems clear that the state secrets privilege will not be invoked in the
  great majority of cases in which §1806(f) is triggered. And in the few
  cases in which an aggrieved party, rather than the Government, trig-
  gers the application of §1806(f), no clash exists between the statute
  and the privilege because they (1) require courts to conduct different
  inquiries, (2) authorize courts to award different forms of relief, and
  (3) direct the parties and the courts to follow different procedures.
     First, the central question for courts to determine under §1806(f) is
  “whether the surveillance of the aggrieved person was lawfully author-
  ized and conducted.” By contrast, the state secrets privilege asks
  whether the disclosure of evidence would harm national security in-
  terests, regardless of whether the evidence was lawfully obtained.
     Second, the relief available under the statute and under the privi-
  lege differs. Under §1806, a court has no authority to award any relief
  to an aggrieved person if it finds the evidence was lawfully obtained,
  whereas a court considering an assertion of the state secrets privilege
  may order the disclosure of lawfully obtained evidence if it finds that
  disclosure would not affect national security. And under respondents’
  interpretation of §1806(f), a court must award relief to an aggrieved
  person against whom evidence was unlawfully obtained, but under the
  state secrets privilege, lawfulness is not determinative. Moreover, the
  potential availability of dismissal on the pleadings pursuant to the
  state secrets privilege shows that the privilege and §1806(f) operate
  differently.
     Third, inquiries under §1806(f) and the state secrets privilege are
  procedurally different. Section 1806(f) allows “review in camera and
  ex parte” of materials “necessary to determine” whether the surveil-
  lance was lawful. Under the state secrets privilege, however, exami-
  nation of the evidence at issue, “even by the judge alone, in chambers,”
  should not be required if the Government shows “a reasonable danger
  that compulsion of the evidence” will expose information that “should
  not be divulged” in “the interest of national security.” United States v.
  Reynolds, 345 U. S. 1, 10. Pp. 9–13.
     (c) This decision answers the narrow question whether §1806(f) dis-
  places the state secrets privilege. The Court does not decide which
  party’s interpretation of §1806(f) is correct, whether the Government’s
  evidence is privileged, or whether the District Court was correct to dis-
  miss respondents’ claims on the pleadings. P. 13.
965 F. 3d 1015, reversed and remanded.

  ALITO, J., delivered the opinion for a unanimous Court.
                        Cite as: 595 U. S. ____ (2022)                                 1

                              Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order that
     corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                    _________________

                                     No. 20–828
                                    _________________

   FEDERAL BUREAU OF INVESTIGATION, ET AL.,
      PETITIONERS v. YASSIR FAZAGA, ET AL.
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                                  [March 4, 2022]

   JUSTICE ALITO delivered the opinion of the Court.
   In this case, we consider the relationship between the
longstanding “state secrets” privilege and a provision of the
Foreign Intelligence Surveillance Act of 1978 (FISA), 92
Stat. 1783, 50 U. S. C. §1801 et seq., that provides a proce-
dure under which a trial-level court or other authority may
consider the legality of electronic surveillance conducted
under FISA and may thereafter order specified forms of re-
lief. See §1806(f ). This case was brought in federal court
by three Muslim residents of Southern California who
allege that the Federal Bureau of Investigation illegally
surveilled them and others under FISA because of their re-
ligion. In response, the defendants (hereinafter Govern-
ment) invoked the state secrets privilege and asked the Dis-
trict Court to dismiss most of respondents’ claims because
the disclosure of counter-intelligence information that was
vital to an evaluation of those claims would threaten na-
tional-security interests.
   The District Court agreed with the Government’s argu-
ment and dismissed the claims in question, but the Ninth
Circuit reversed, reasoning that §1806(f ) “displaced” the
state secrets privilege. We now hold that §1806(f ) has no
2                       FBI v. FAZAGA

                      Opinion of the Court

such effect, and we therefore reverse.
                               I
                               A
   This Court has repeatedly recognized “a Government
privilege against court-ordered disclosure of state and mil-
itary secrets,” General Dynamics Corp. v. United States,
563 U. S. 478, 484 (2011); see also United States v.
Zubaydah, ___ U. S. ___, ___ (2022) (slip op., at 7); Tenet v.
Doe, 544 U. S. 1, 11 (2005); United States v. Reynolds, 345
U. S. 1, 6–7 (1953); Totten v. United States, 92 U. S. 105,
107 (1876). The present case requires us to determine
whether FISA affects the availability or scope of that long-
established privilege.
   Electronic surveillance for ordinary criminal law enforce-
ment purposes is governed by Title III of the Omnibus
Crime Control and Safe Streets Act of 1968, 18 U. S. C.
§§2510–2522, but foreign intelligence surveillance presents
special national-security concerns, and Congress therefore
enacted FISA to provide special procedures for use when
the Government wishes to conduct such surveillance. See
Clapper v. Amnesty Int’l USA, 568 U. S. 398, 402 (2013).
FISA established the Foreign Intelligence Surveillance
Court to entertain applications for and, where appropriate,
to issue orders authorizing such surveillance. See id., at
402–403; 50 U. S. C. §§1803–1805.
   When information is lawfully gathered pursuant to such
an order, §1806 permits its use in judicial and administra-
tive proceedings and specifies the procedure that must be
followed before that is done.
   Under §1806(c), “[w]henever the Government intends to
enter into evidence or otherwise use or disclose . . . against
                      Cite as: 595 U. S. ____ (2022)                     3

                          Opinion of the Court

an aggrieved person” 1 in any court proceeding2 any infor-
mation obtained under FISA, the United States must “no-
tify” both “the aggrieved person and the court.” Subsection
(e) then allows anyone against whom the Government in-
tends to use such information to move to suppress that evi-
dence on the ground that it was “unlawfully acquired” or
that “the surveillance was not made in conformity with an
order of authorization or approval.” §1806(e).
   The specific provision at issue here, subsection (f ) of
§1806, establishes procedures for determining the lawful-
ness and admissibility of such information. 3 That subsec-
tion permits a court to make that determination “in camera
——————
   1 An “aggrieved person” is “a person who is the target of an electronic

surveillance or any other person whose communications or activities
were subject to electronic surveillance.” 50 U. S. C. §1801(k).
   2 Section 1806 applies to proceedings in both federal and state court.

See §§1806(c), (d). It also applies to proceeding before any “department,
officer, agency, regulatory body, or other authority.” Ibid.
   3 The provision in its entirety reads: “Whenever a court or other au-

thority is notified pursuant to subsection (c) or (d), or whenever a motion
is made pursuant to subsection (e), or whenever any motion or request is
made by an aggrieved person pursuant to any other statute or rule of the
United States or any State before any court or other authority of the
United States or any State to discover or obtain applications or orders or
other materials relating to electronic surveillance or to discover, obtain,
or suppress evidence or information obtained or derived from electronic
surveillance under this chapter, the United States district court or,
where the motion is made before another authority, the United States
district court in the same district as the authority, shall, notwithstand-
ing any other law, if the Attorney General files an affidavit under oath
that disclosure or an adversary hearing would harm the national secu-
rity of the United States, review in camera and ex parte the application,
order, and such other materials relating to the surveillance as may be
necessary to determine whether the surveillance of the aggrieved person
was lawfully authorized and conducted. In making this determination,
the court may disclose to the aggrieved person, under appropriate secu-
rity procedures and protective orders, portions of the application, order,
or other materials relating to the surveillance only where such disclosure
is necessary to make an accurate determination of the legality of the sur-
veillance.”
4                       FBI v. FAZAGA

                      Opinion of the Court

and ex parte” if the “Attorney General files an affidavit un-
der oath that disclosure or an adversary hearing would
harm the national security of the United States.” §1806(f ).
   Three circumstances trigger these procedures: first,
where the United States or a state authority gives notice
under §1806(c) or (d) that it intends to “enter into evidence
or otherwise use or disclose” FISA information; second,
where an aggrieved person files a motion to suppress such
information under subsection (e); and third, where “any mo-
tion or request is made by an aggrieved person pursuant to
any other statute or rule of the United States or any State
before any court or other authority of the United States or
any State to discover or obtain applications or orders or
other materials relating to electronic surveillance or to dis-
cover, obtain, or suppress evidence or information obtained
or derived from electronic surveillance under this chapter.”
§1806(f ).
   Once §1806(f )’s in camera and ex parte procedures are
triggered, the court must review the “application, order,
and such other materials relating to the surveillance as
may be necessary to determine whether the surveillance of
the aggrieved person was lawfully authorized and con-
ducted.” Ibid. If the court finds that the evidence was un-
lawfully obtained, it must “suppress” the evidence or “oth-
erwise grant the motion of the aggrieved person.” §1806(g).
But if the court finds that the evidence was lawfully ob-
tained, it must “deny the motion of the aggrieved person
except to the extent that due process requires discovery or
disclosure.” Ibid.
                              B
   Respondents Yassir Fazaga, Ali Malik, and Yasser Abdel
Rahim are members of Muslim communities in southern
California who claim that the Federal Bureau of Investiga-
tion illegally surveilled them because of their religion. Re-
                     Cite as: 595 U. S. ____ (2022)                   5

                         Opinion of the Court

spondents allege that the FBI directed a confidential in-
formant to “gather information on Muslims in an indiscrim-
inate manner.” App. 97, First Amended Complaint ¶99.
This informant purportedly infiltrated a Muslim commu-
nity and gathered “hundreds of phone numbers and thou-
sands of email addresses of Muslims”; “hundreds of hours
of video recordings” made inside mosques, homes, and other
private locations; and “thousands of hours of audio record-
ing of conversations” and of “public discussion groups, clas-
ses, and lectures.” Id., at 194, Decl. of Craig Monteilh ¶71.
Respondents allege that the surveillance operation ended
when the informant, at the FBI’s instruction, began asking
members of the community about violent jihad, and some
of those individuals reported the informant to the FBI and
local police.
   In 2011, respondents filed this putative class action
against the United States, the FBI, and two FBI officials in
their official capacities. 4 Respondents claimed that the
Government’s unlawful information-gathering operation
violated their rights under the Establishment Clause; the
Free Exercise Clause; the Fourth Amendment; the equal
protection component of the Fifth Amendment’s Due Pro-
cess Clause; the Religious Freedom Restoration Act, 42
U. S. C. §2000bb et seq.; the Federal Tort Claims Act, 28
U. S. C. §1346; FISA, 50 U. S. C. §1810; the Privacy Act, 5
U. S. C. §552a; and California law.
   The Government moved to dismiss all those claims and
argued, among other things, that the state secrets privilege
required dismissal of most of them. To that end, Attorney
General Holder filed a declaration asserting a “formal claim
of the state secrets privilege in order to protect the national
——————
   4 Respondents also sued five named FBI agents and 20 unnamed

agents in their individual capacities, but we need not discuss those
claims or those parties (who are also respondents in this Court and who
filed briefs supporting the Government) in order to resolve the question
presented.
6                        FBI v. FAZAGA

                       Opinion of the Court

security interests of the United States.” App. 26, Decl. of
Eric H. Holder ¶1. This claim applied to the following cat-
egories of information: information that could “confirm or
deny whether a particular individual was or was not the
subject of an FBI counterterrorism investigation,” infor-
mation that could reveal the “initial reasons” for or the “sta-
tus and results” of an “FBI counterterrorism investigation,”
and information that could reveal the “sources and meth-
ods” used in such an investigation. Id., at 28, ¶4. An As-
sistant Director of the FBI filed a public declaration ex-
plaining why disclosure “reasonably could be expected to
cause significant harm to national security,” id., at 60, Decl.
of Mark F. Giuliano ¶32, along with a more detailed classi-
fied declaration.
   After reviewing both “the public and classified filings,”
the District Court held that the state secrets privilege re-
quired dismissal of all respondents’ claims against the Gov-
ernment, except for the claim under FISA, 50 U. S. C.
§1810, which it dismissed on sovereign-immunity grounds.
884 F. Supp. 2d 1022, 1049 (CD Cal. 2012); 885 F. Supp. 2d
978, 982–984 (CD Cal. 2012). The District Court concluded
that litigation of the claims it dismissed “would require or
unjustifiably risk disclosure of secret and classified infor-
mation.” 884 F. Supp. 2d, at 1028–1029.
   The Ninth Circuit reversed in relevant part and held that
“Congress intended FISA to displace the state secrets priv-
ilege and its dismissal remedy with respect to electronic
surveillance.” 965 F. 3d 1015, 1052 (2020). That holding
depended on two subsidiary conclusions. First, the Court
of Appeals held that “§1806(f ) procedures are to be used
when an aggrieved person affirmatively challenges, in any
civil case, the legality of electronic surveillance or its use in
litigation, whether the challenge is under FISA itself, the
Constitution, or any other law.” Ibid. Second, the Court of
Appeals held that, where §1806(f )’s procedures apply, it
“speak[s] quite directly to the question otherwise answered
                  Cite as: 595 U. S. ____ (2022)            7

                      Opinion of the Court

by the dismissal remedy sometimes required by the com-
mon law state secrets privilege.” Id., at 1045. That is so,
the Court of Appeals reasoned, because §1806(f )’s proce-
dures are “animated by the same concerns” as the state se-
crets privilege and “triggered” by a “nearly identical" pro-
cess. Id., at 1046. It thus reversed the District Court’s
dismissal of respondents’ claims on state secrets grounds.
  The Ninth Circuit denied rehearing en banc over the dis-
sent of Judge Bumatay and nine other judges. We granted
certiorari to decide whether §1806(f ) displaces the state se-
crets privilege. 594 U. S. ___ (2021).
                               II
                               A
   Much of the parties’ argumentation in this Court con-
cerns the correct interpretation of §1806(f ). The Govern-
ment contends that the Ninth Circuit erred because
§1806(f ) is “ ‘relevant only when a litigant challenges the
admissibility of the government’s surveillance evidence.’ ”
Reply Brief for Petitioners 2 (quoting Wikimedia Founda-
tion v. NSA, 14 F. 4th 276, 294 (CA4 2021)). But respond-
ents interpret that provision more broadly.
   Respondents do not dispute that §1806(f ) applies when
the Government seeks to introduce evidence and a private
party seeks to prevent such use, but they argue that
§1806(f ) is also sometimes triggered when “a civil litigant
seeks to obtain such secret information.” Brief for Respond-
ents 34. And they say that §1806(f ) applies in this case for
two reasons. First, they note that §1806(f ) is triggered not
only when the Government gives notice that it intends to
“enter into evidence” information obtained by means of cov-
ered surveillance but also when it notifies the court that it
“intends to . . . otherwise use” such information. §1806(c).
Respondents argue that the Government “use[d]” infor-
mation gathered under FISA when it invoked the state se-
crets privilege and asked the District Court to dismiss some
8                            FBI v. FAZAGA

                           Opinion of the Court

of respondents’ claims pursuant to that privilege. In re-
spondents’ view, the attempt to leverage a claim of privilege
into a dismissal constitutes a “use” of FISA information
against them. See Brief for Respondents 35–38; Tr. of Oral
Arg. 71–73. Second, respondents note that §1806(f ) applies
when an “aggrieved person” makes “any motion or request”
to “discover or obtain” electronic-surveillance evidence, and
they say that their complaint’s request for an injunction or-
dering the Government to “destroy or return any infor-
mation gathered through the unlawful surveillance pro-
gram” triggered that provision. App. 146; see also Brief for
Respondents 39–40. 5 That prayer for relief, they maintain,
constituted a “request” to “discover or obtain” the infor-
mation.
   The Government disagrees with both of these theories. It
argues that the assertion of the state secrets privilege did
not constitute a “use” of “information obtained or derived
from an electronic surveillance.” On the contrary, the Gov-
ernment contends, the assertion of the privilege repre-
sented an attempt to prevent the use of that information.
Reply Brief for Petitioners 2–3. In addition, the Govern-
ment maintains that respondents never filed a “ ‘motion or
request . . . to discover [or] obtain’ ” information derived
from or materials relating to FISA surveillance because
their complaint’s prayer for relief did not constitute a “ ‘mo-
tion or request.’ ” Id., at 5.
   We need not resolve this dispute about the meaning of


——————
   5 The Circuits disagree about the correct interpretation of §1806(f ).

Compare Wikimedia Foundation v. NSA, 14 F. 4th 276, 294 (CA4 2021)
(“[W]e conclude that §1806(f ) is relevant only when a litigant challenges
the admissibility of the government's surveillance evidence”), with 965
F. 3d 1015, 1052 (CA9 2020) (“§1806(f ) procedures are to be used when
any aggrieved person affirmatively challenges, in any civil case, the le-
gality of electronic surveillance or its use in litigation, whether the chal-
lenge is under FISA itself, the Constitution, or any other law”).
                     Cite as: 595 U. S. ____ (2022)                     9

                          Opinion of the Court

§1806(f ) because we reverse the Ninth Circuit on an alter-
native ground—namely, that even as interpreted by re-
spondents, §1806(f ) does not displace the state secrets priv-
ilege.
                            B
  We reach this conclusion for two reasons.
                                1
  First, the text of FISA weighs heavily against respond-
ents’ displacement argument. FISA makes no reference to
the state secrets privilege. It neither mentions the privilege
by name nor uses any identifiable synonym, and its only
reference to the subject of privilege reflects a desire to avoid
the alteration of privilege law. See §1806(a). 6
  The absence of any statutory reference to the state se-
crets privilege is strong evidence that the availability of the
privilege was not altered in any way. Regardless of whether
the state secrets privilege is rooted only in the common law
(as respondents argue) or also in the Constitution (as the
Government argues), the privilege should not be held to
have been abrogated or limited unless Congress has at least
used clear statutory language. See Norfolk Redevelopment
and Housing Authority v. Chesapeake & Potomac Telephone
Co. of Va., 464 U. S. 30, 35 (1983) (presumption against re-
peal of the common law); Jennings v. Rodriguez, 583 U. S.
___, ___ (2018) (slip op., at 12) (canon of constitutional
avoidance).
                              2
  Even if respondents’ interpretation of §1806(f ) is ac-
cepted, nothing about the operation of that provision is at
all incompatible with the state secrets privilege. The Ninth

——————
  6 That provision states: “No otherwise privileged communication ob-

tained in accordance with, or in violation of, the provisions of this sub-
chapter shall lose its privileged character.”
10                      FBI v. FAZAGA

                      Opinion of the Court

Circuit thought that §1806(f ) and the privilege are “ani-
mated by the same concerns,” 965 F. 3d, at 1046, and re-
spondents argue that they operate in “fundamentally simi-
lar” ways, Brief for Respondents 54, but that is simply
wrong.
   As an initial matter, it seems clear that the state secrets
privilege will not be invoked in the great majority of cases
in which §1806(f ) is triggered. Section 1806(f ) is most
likely to come into play when the Government seeks to use
FISA evidence in a judicial or administrative proceeding,
and the Government will obviously not invoke the state se-
crets privilege to block disclosure of information that it
wishes to use. Section 1806(f ) is much more likely to be
invoked in cases of this sort than in cases in which an ag-
grieved person takes the lead and seeks to obtain or disclose
FISA information for a simple reason: individuals affected
by FISA surveillance are very often unaware of the surveil-
lance unless it is revealed by the Government. See 2 D. Kris
& J. Wilson, National Security Investigations & Prosecu-
tions §30:4 (3d ed. 2019).
   With these cases out of the way, what is left are cases in
which an aggrieved party, rather than the Government,
triggers the application of §1806(f ), but even under re-
spondents’ interpretation of that provision, there is no clash
between §1806(f ) and the state secrets privilege. The stat-
ute and the privilege (1) require courts to conduct different
inquiries, (2) authorize courts to award different forms of
relief, and (3) direct the parties and the courts to follow dif-
ferent procedures. First and most importantly, the inquir-
ies required by §1806(f ) and our state secrets jurisprudence
are fundamentally different. Under §1806(f ), the central
question is the lawfulness of surveillance. Courts are in-
structed to determine “whether the surveillance of the ag-
grieved person was lawfully authorized and conducted.”
§1806(f ) (emphasis added).
   By contrast, when the state secrets privilege is asserted,
                 Cite as: 595 U. S. ____ (2022)           11

                     Opinion of the Court

the central question is not whether the evidence in question
was lawfully obtained but whether its disclosure would
harm national-security interests. As the Court explained
in Reynolds, the privilege applies where “there is a reason-
able danger that compulsion of the evidence will expose mil-
itary matters which, in the interest of national security,
should not be divulged.” 345 U. S., at 10; see also, e.g.,
Zubaydah, ___ U. S., at ___ (slip op., at 7) (“The state-se-
crets privilege permits the Government to prevent disclo-
sure of information when that disclosure would harm na-
tional security interests”); General Dynamics, 563 U. S., at
484 (noting that the privilege exists to serve the “some-
times-compelling necessity of governmental secrecy” over
“military, intelligence, and diplomatic” information). We
have never suggested that an assertion of the state secrets
privilege can be defeated by showing that the evidence was
unlawfully obtained.
   Second, in accordance with the fundamentally different
inquiries called for under §1806(f ) and the state secrets
privilege, the available relief also differs. Under §1806, a
court has no authority to award any relief to an aggrieved
person if it finds that the evidence was lawfully obtained,
whereas a court considering an assertion of the state secrets
privilege may order the disclosure of lawfully obtained evi-
dence if it finds that disclosure would not affect national
security (assuming that the information is otherwise sub-
ject to disclosure). And under §1806(f ), as interpreted by
respondents, a court must award relief to an aggrieved per-
son if it finds that the evidence was unlawfully obtained,
but under the state secrets privilege, lawfulness is not de-
terminative.
   In addition, the state secrets privilege, unlike §1806,
sometimes authorizes district courts to dismiss claims on
the pleadings. We need not delineate the circumstances in
which dismissal is appropriate (or determine whether dis-
12                      FBI v. FAZAGA

                      Opinion of the Court

missal was proper in this case), but even respondents con-
cede that dismissal is available in a “spy-contracting case”
when a case’s “very subject matter is secret.” Brief for Re-
spondents 25; see also Tenet, 544 U. S., at 11; Totten, 92
U. S., at 107; General Dynamics, 563 U. S., at 492. The
availability of dismissal pursuant to the state secrets priv-
ilege in at least some circumstances shows that the privi-
lege and §1806(f ) operate differently.
   Third, the inquiries under §1806(f ) and the state secrets
privilege are procedurally different. Section 1806(f ) allows
the Attorney General to obtain in camera and ex parte re-
view of the relevant surveillance evidence if he “files an af-
fidavit under oath that disclosure or an adversary hearing
would harm the national security of the United States.”
§1806(f ). By contrast, the state secrets privilege may be
invoked not just by the Attorney General but by “the head
of the department which has control over the matter, after
actual personal consideration by that officer.” Reynolds,
345 U. S., at 8. In Reynolds, for example, the Judge Advo-
cate General for the United States Air Force asserted the
privilege. See id., at 4; see also Zubaydah, ___ U. S., at ___
(slip op., at 5) (asserted by the Director of the Central Intel-
ligence Agency); General Dynamics, 563 U. S., at 482 (as-
serted by the Acting Secretary of the Air Force).
   The procedures used to evaluate assertions of the state
secrets privilege may also, in some circumstances, be more
protective of information than the procedures prescribed by
§1806(f ). Subsection (f ) allows “review in camera and
ex parte” of materials that are “necessary to determine”
whether the surveillance was lawful. Nothing in that sub-
section expressly provides that the Government may shield
highly classified information from review by the judge if the
information is “necessary” to the determination of the legal-
ity of surveillance. Reynolds, on the other hand, expressly
states that examination of the evidence at issue, “even by
the judge alone, in chambers,” should not be required if the
                  Cite as: 595 U. S. ____ (2022)                 13

                      Opinion of the Court

Government shows “a reasonable danger that compulsion
of the evidence” will expose information that “should not be
divulged” in “the interest of national security.” 345 U. S.,
at 10. Thus, the state secrets privilege, unlike §1806(f ),
may sometimes preclude even in camera, ex parte review of
the relevant evidence.
   For those reasons, we conclude that Congress did not
eliminate, curtail, or modify the state secrets privilege
when it enacted §1806(f ).
                              III
  We reiterate that today’s decision addresses only the nar-
row question whether §1806(f ) displaces the state secrets
privilege. Because we conclude that §1806(f ) does not have
that effect under either party’s interpretation of the statute,
we do not decide which interpretation is correct. Nor do we
decide whether the Government’s evidence is privileged or
whether the District Court was correct to dismiss respond-
ents’ claims on the pleadings. According to respondents,
the state secrets privilege authorizes dismissal only where
the case concerns a Government contract or where the very
subject of the action is secret. See Brief for Respondents
23–34. The Government, by contrast, relies on lower court
cases permitting dismissal in other circumstances. See Re-
ply Brief for Petitioners 19, n. 2 (citing cases). The Ninth
Circuit did not decide those questions, and we do not resolve
them here.
                        *    *     *
  The judgment of the United States Court of Appeals for
the Ninth Circuit is reversed, and the case is remanded for
further proceedings consistent with this opinion.

                                                   It is so ordered.

```

---

## GROUP: content/cases/FBI v. Fikre.md  (`case`, 5 assertions)

### content_page

```
---
title: FBI v. Fikre
type: case
citation: "601 U.S. 234 (2024)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2024
date_decided: ""
docket: 22-1178
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
  opinion_url: "https://www.courtlistener.com/opinion/10600106/fbi-v-fikre/"
  cluster_id: 10600106
  opinion_id: null
  identity_checked: true
lake:
  record_id: FBI v. Fikre
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - mootness
  - voluntary-cessation
  - no-fly-list
  - civil-rights-remedies
holding: "A defendant's voluntary cessation of challenged conduct moots a case only if it carries the formidable burden of showing the conduct cannot reasonably be expected to recur; the government's removal of Yonas Fikre from the No Fly List, and its declaration that he would not be relisted 'based on currently available information,' did not carry that burden, so his suit was not moot."
---

# FBI v. Fikre

*601 U.S. 234 (2024)* (No. 22-1178) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10600106 → opinion 11066694; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Yonas Fikre, a U.S. citizen, was placed on the No Fly List while traveling abroad and sued the FBI and government officials, seeking a declaration that his placement violated his rights and an injunction removing him. In 2016 the government notified Fikre that it had taken him off the list — without explanation — and then argued the suit was moot. The district court agreed, but the Ninth Circuit twice reversed: neither the bare removal nor a later government declaration that Fikre would not be placed on the No Fly List in the future based on the information then available showed that he would not be relisted for the same or similar conduct. Because the Fourth Circuit had found a similar declaration sufficient to moot a parallel case, the Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether the government's voluntary removal of Fikre from the No Fly List, together with its declaration about his future status, rendered his challenge to that placement moot.

## Rule
A federal court has a "virtually unflagging obligation" to decide cases within its jurisdiction, and a defendant cannot "automatically moot a case" simply by suspending the challenged conduct after being sued. Under the voluntary-cessation doctrine, "a defendant's 'voluntary cessation of a challenged practice' will moot a case only if the defendant can show that the practice cannot 'reasonably be expected to recur.'" — 601 U.S. at 241. ^pin-241

That is a "formidable burden," because otherwise a defendant could suspend its conduct, win dismissal, and later resume where it left off.

## Application
The government's showing fell short of that formidable burden. Its declaration stated only that Fikre would not be relisted based on the information then available, and it never disclosed the conduct that had landed him on the list in the first place — so nothing prevented the government from returning him to the list for the same or similar conduct in the future. Because the government could not demonstrate that its challenged conduct could not reasonably be expected to recur, Fikre's suit was not moot and had to proceed.

## Conclusion
The judgment of the Ninth Circuit was **affirmed** and the case **[[Reading and Citing Cases#on-remand|remanded]]** for further proceedings. Gorsuch, J., delivered the opinion for a unanimous Court; Alito, J., joined by Kavanaugh, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Fikre* is a mootness decision that constrains the government's ability to defeat civil-rights and constitutional suits through strategic, unexplained voluntary cessation; it does not reach the merits of Fikre's challenge to his No Fly List placement.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*FBI v. Fikre*, 601 U.S. 234 (2024)](https://www.courtlistener.com/opinion/10600106/fbi-v-fikre/) — pinpoint: 241 (voluntary-cessation standard, Opinion of the Court); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8798192bbe3af798", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "601 U.S. 234 (2024)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "FBI v. Fikre", "year": "2024"}}
{"assertion_id": "600e2a88489f9004", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A defendant's voluntary cessation of challenged conduct moots a case only if it carries the formidable burden of showing the conduct cannot reasonably be expected to recur; the government's removal of Yonas Fikre from the No Fly List, and its declaration that he would not be relisted 'based on currently available information,' did not carry that burden, so his suit was not moot.", "title": "FBI v. Fikre"}}
{"assertion_id": "90bd808116e54384", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "FBI v. Fikre"}}
{"assertion_id": "0f6f82495b1b918a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "FBI v. Fikre"}}
{"assertion_id": "5e661cdf8175f423", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "FBI v. Fikre", "varies_by_point": "false"}}
```

### lake record — FBI v. Fikre

```json
{
  "schema_version": "s2.v1",
  "record_id": "FBI v. Fikre",
  "status": "under_review",
  "identity": {
    "case_name": "FBI v. Fikre",
    "case_name_short": "Fikre",
    "case_name_full": "",
    "input_case_name": "Federal Bureau of Investigation v. Fikre",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2024,
    "docket": "22-1178",
    "cluster_id": 10600106,
    "lead_opinion_id": 11066694,
    "sibling_ids": [],
    "absolute_url": "/opinion/10600106/fbi-v-fikre/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "601 U.S. 234",
      "volume": "601",
      "reporter": "U.S.",
      "page": "234",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "601 U.S. 234",
        "volume": "601",
        "reporter": "U.S.",
        "page": "234",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "601 U.S. 234",
    "official_selection": {
      "court_class": "scotus",
      "selected": "601 U.S. 234",
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
    "date_created": "2026-07-06T12:26:29Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:26:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:26:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:26:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:26:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "federal-bureau-of-investigation-v-fikre--10600106",
      "to_record_id": "FBI v. Fikre",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — FBI v. Fikre

```
                   PRELIMINARY PRINT

             Volume 601 U. S. Part 1
                             Pages 234–245




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                              March 19, 2024


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
234                     OCTOBER TERM, 2023

                                Syllabus


 FEDERAL BUREAU OF INVESTIGATION et al. v.
                 FIKRE

certiorari to the united states court of appeals for
                  the ninth circuit
      No. 22–1178. Argued January 8, 2024—Decided March 19, 2024
Respondent Yonas Fikre, a U. S. citizen and Sudanese emigree, brought
 suit alleging that the government placed him on the No Fly List unlaw-
 fully. In his complaint, Mr. Fikre alleged that he traveled from his
 home in Portland, Oregon, to Sudan in 2009 to pursue business opportu-
 nities there. At a visit to the U. S. embassy, two FBI agents informed
 Mr. Fikre that he could not return to the United States because the
 government had placed him on the No Fly List. The agents questioned
 him extensively about the Portland mosque he attended, and they of-
 fered to take steps to remove him from the No Fly List if he agreed to
 become an FBI informant and to report on other members of his reli-
 gious community. Mr. Fikre refused. He then traveled to the United
 Arab Emirates, where he alleges authorities interrogated and detained
Page Proof Pending Publication
 him for 106 days at the behest of the FBI. Unable to fy back to the
 United States, he ended up in Sweden, where he remained until Febru-
 ary 2015. While there, he fled this suit, alleging that the government
 had violated his rights to procedural due process by failing to provide
 either meaningful notice of his addition to the No Fly List or any appro-
 priate way to secure redress. He further alleged that the government
 had placed him on the list for constitutionally impermissible reasons
 related to his race, national origin, and religious beliefs. Mr. Fikre
 sought, among other things, an injunction prohibiting the government
 from keeping him on the No Fly List and a declaratory judgment con-
 frming the government had violated his rights. In May 2016, the gov-
 ernment notifed Mr. Fikre that he had been removed from the No Fly
 List and sought dismissal of his suit in district court, arguing that its
 administrative action had rendered the case moot. The district court
 agreed with the government, but the Ninth Circuit reversed, holding
 that a party seeking to moot a case based on its own voluntary cessation
 of challenged conduct must show that the conduct cannot “reasonably be
 expected to recur.” 904 F. 3d 1033, 1039. On remand, the government
 submitted a declaration asserting that, based on the currently available
 information, Mr. Fikre would not be placed on the No Fly List in the
 future, and the district court again dismissed Mr. Fikre's claim as moot.
 The Ninth Circuit once again reversed, holding that the government had
 failed to meet its burden because the declaration did not disclose the
                        Cite as: 601 U. S. 234 (2024)                     235

                                  Syllabus

  conduct that landed Mr. Fikre on the No Fly List and did not ensure
  that he would not be placed back on the list for engaging in the same
  or similar conduct in the future. 35 F. 4th 762, 770–772.
Held: The government has failed to demonstrate that this case is moot.
  A court with jurisdiction has a “virtually unfagging obligation” to hear
  and resolve questions properly before it. Colorado River Water Con-
  servation Dist. v. United States, 424 U. S. 800, 817. But the converse
  is also true as a federal court must dismiss a case that is moot. Al-
  ready, LLC v. Nike, Inc., 568 U. S. 85, 91. The limited authority vested
  in federal courts by Article III of the U. S. Constitution to decide cases
  and controversies means that federal courts may no more pronounce on
  past actions that have no “continuing effect” in the world than they may
  neglect their obligation to hear and resolve questions properly before
  them. Spencer v. Kemna, 523 U. S. 1, 18. This does not imply that a
  defendant may “automatically moot a case” by the simple expedient of
  suspending its challenged conduct after it is sued. Instead, a defend-
  ant's “voluntary cessation of a challenged practice” will moot a case
  only if the defendant can show that the practice cannot “reasonably be
  expected to recur.” Friends of the Earth, Inc. v. Laidlaw Environ-
  mental Services (TOC), Inc., 528 U. S. 167, 189. This standard holds
  for governmental defendants no less than for private ones. Applying
Page Proof Pending Publication
  these principles to the uncontested factual allegations here, this case is
  not moot. While the government's representation that it will not relist
  Mr. Fikre may mean that his past conduct is not enough to warrant
  relisting, that does not speak to whether the government might relist
  him if he engages in the same or similar conduct in the future. The
  government contends that because Mr. Fikre has been delisted since
  2016 and has presumably interacted freely with his co-religionists dur-
  ing that time, it is unlikely he will face relisting in the future. This too
  is insuffcient to warrant dismissal. A defendant's speculation about a
  plaintiff 's actions cannot make up for a lack of assurance about its own.
  The burden here is on the defendant to establish that it cannot reason-
  ably be expected to resume its challenged conduct, see West Virginia
  v. EPA, 597 U. S. 697, 719, and nothing the government offers here satis-
  fes that formidable standard. The government claims the Ninth Cir-
  cuit erred by requiring it to repudiate its past conduct to prove moot-
  ness, but what matters is not whether a defendant repudiates its past
  actions, but what the defendant can prove about its future conduct.
  Coming as this case does in a preliminary posture, the Court's judgment
  is a necessarily provisional one. As the complaint's allegations are tes-
  ted, different facts may emerge that may call for a different result. But
  adhering to traditional mootness principles, the government has so far
  failed to meet its burden. Pp. 240–245.
35 F. 4th 762, affrmed.
236                          FBI v. FIKRE

                          Opinion of the Court

  Gorsuch, J., delivered the opinion for a unanimous Court. Alito, J.,
fled a concurring opinion, in which Kavanaugh, J., joined, post, p. 245.

  Sopan Joshi argued the cause for petitioners. With him
on the briefs were Solicitor General Prelogar, Principal
Deputy Assistant Attorney General Boynton, Deputy Solic-
itor General Kneedler, and Sharon Swingle.
  Gadeir Abbas argued the cause for respondent. With him
on the brief were Lindsay C. Harrison, Lena Masri, Justin
Sadowsky, Hannah Mullen, Andrianna D. Kastanek, Benja-
min D. Alter, David A. Strauss, and Sarah M. Konsky.*

  Justice Gorsuch delivered the opinion of the Court.
  Yonas Fikre, a U. S. citizen, brought suit alleging that the
government placed him on the No Fly List unlawfully.
Later, the government removed him from the list. The only
question we are asked to decide is whether the government's
action suffces to render Mr. Fikre's claims moot.
Page Proof Pending Publication
                                    I
                                   A
  In the aftermath of the September 11, 2001, terrorist at-
tacks, the federal government rapidly expanded its No Fly

  *Briefs of amici curiae urging affrmance were fled for the American
Civil Liberties Union et al. by Hina Shamsi, Cecillia D. Wang, and An-
drew Kim; for Asian Americans Advancing Justice et al. by Koren Bell,
Michael J. Gottlieb, Mark T. Stancil, and Niyati Shah; for the Cato Insti-
tute by Russ Falconer, Daniel R. Adler, Matt Aidan Getz, and Clark M.
Neily III; for the Constitutional Law Center for Muslims in America by
Christina A. Jump and Chelsea G. Glover; for the Institute for Justice by
Samuel B. Gedge; for the Liberty Justice Center by Jacob Huebert; for
the Sikh Coalition et al. by John M. Reeves, Kelly Shackelford, Jeff Ma-
teer, David Hacker, and Hiram Sasser; and for Patrick G. Eddington by
Anastasia P. Boden and Thomas A. Berry.
  Briefs of amici curiae were fled for the Becket Fund for Religious
Liberty by Joseph C. Davis; and for Restore the Fourth, Inc., et al., by
Mahesha P. Subbaraman.
                       Cite as: 601 U. S. 234 (2024)                    237

                           Opinion of the Court

List. By 2016, the government forbade approximately
81,000 individuals from fying into, out of, within, or over the
United States. Brief for American Civil Liberties Union
et al. as Amici Curiae 5. Many of the details surrounding
the No Fly List are not publicly available. Some are classi-
fed, and it appears no statute or publicly promulgated regu-
lation describes the standards the government employs when
adding individuals to, or removing them from, the list. Id.,
at 6.
   In his complaint, Mr. Fikre challenged his placement on
the No Fly List. In support of his suit, he pleaded a number
of facts. Those as-yet uncontested factual allegations, the
truth of which we do not pass upon, aver as follows:*
   When he was a child and war broke out in his home coun-
try of Eritrea, Mr. Fikre and his family moved to Sudan be-
fore eventually immigrating to the United States. App. to
Pet. for Cert. 126a, Seventh Amended Complaint ¶4; id., at
137a, ¶51. In time, Mr. Fikre became a U. S. citizen, and as
Page Proof Pending Publication
an adult he lived in Portland, Oregon. Id., at 137a–138a,
¶¶51–52. After working for an American cell phone com-
pany, he decided to start his own business involving the dis-
tribution and retail sale of consumer electronic products in
his native East Africa. Id., at 138a, ¶52. In pursuit of this
new venture, he traveled to Sudan in late 2009 where some
of his extended family still lived. Ibid.
   On arrival, Mr. Fikre informed U. S. offcials of his interest
in pursuing business opportunities in the country. Ibid.
Eventually, he received an invitation to the U. S. embassy—
ostensibly for a luncheon. Id., at 138a–139a, ¶¶53–55. But,

   *Responding to Mr. Fikre's complaint with a motion to dismiss for lack
of jurisdiction, the government did not contest his factual allegations, and
the courts below thus assumed their truth. See Gibbs v. Buck, 307 U. S.
66, 72 (1939); 5C C. Wright & A. Miller, Federal Practice and Procedure
§ 1363, p. 107 (3d ed. 2004) (“The general rule” for Rule 12(b)(1) motions
challenging subject-matter jurisdiction is to take allegations “as true un-
less denied or controverted by the movant”). We do the same.
238                     FBI v. FIKRE

                     Opinion of the Court

once there, Fikre was whisked instead to a small meeting
room with two FBI agents. Id., at 139a, ¶¶55–56. The
agents told him that the government had placed him on the
No Fly List, so he “could not return to the United States.”
Ibid., ¶57. The agents then questioned him “extensively
about the events, activities, and leadership” of the Portland
mosque he attended. Ibid., ¶58. They asked him to serve
as an FBI informant and report on other members of his
religious community, offering to “take steps to remove [him]
from the No Fly List” if he agreed. Id., at 140a, ¶59.
Mr. Fikre refused and eventually departed. Ibid. The
next day, an agent told him over the phone that, “ `[w]hen-
ever you want to go home[,] you come to the embassy.' ” Id.,
at 140a–141a, ¶62. Mr. Fikre took this to mean that he
“would not be removed from the No Fly List and he could
not travel to the United States unless he became” an FBI
informant. Id., at 141a, ¶62.
  Several weeks later, Mr. Fikre traveled to the United Arab
Page Proof Pending Publication
Emirates to advance his business plans. Id., at 142a, ¶68.
Eventually, however, authorities there “arrested, impris-
oned, and tortured him.” 35 F. 4th 762, 766 (CA9 2022);
App. to Pet. for Cert. 142a–143a, Seventh Amended Com-
plaint ¶¶69–71. They interrogated him, too, about his Port-
land mosque, its events, leader, and fundraising activities.
Id., at 143a, ¶72. One interrogator told Mr. Fikre that the
FBI had solicited his interrogation and detention. Id., at
147a, ¶88. After holding him for 106 days, authorities ar-
ranged to have Mr. Fikre fown to Sweden where he had a
relative. Id., at 147a, ¶86, 148a, ¶90. He remained there
until February 2015, when the Swedish government re-
turned him to Portland by private jet. Id., at 152a, ¶105.

                              B
  While still in Sweden, Mr. Fikre fled this suit. In his
complaint, he alleged that the government had violated his
rights to procedural due process by failing to provide any
                   Cite as: 601 U. S. 234 (2024)            239

                      Opinion of the Court

meaningful notice of his addition to the No Fly List, any
information about the factual basis for his listing, and any
appropriate way to secure redress. Id., at 165a, ¶164. Fur-
ther, he claimed, the government had placed him on the list
for constitutionally impermissible reasons, including his race,
national origin, and religious beliefs. Id., at 168a, ¶176.
By way of relief, he sought a declaratory judgment confrm-
ing that the government had violated his rights, as well as
an injunction prohibiting it from keeping him on the No Fly
List. Id., at 169a–170a.
   Eventually, in May 2016, the government notified
Mr. Fikre that it had removed him from the No Fly List.
No explanation accompanied the decision. See Notice Re-
garding Plaintiff 's Status in No. 3:13–cv–899 (D Ore.), ECF
Doc. 98, p. 1. But, in court, the government argued that its
administrative action rendered his lawsuit moot; even ac-
cepting all his allegations as true, the government said, dis-
Page Proof Pending Publication
missal had to follow as a matter of law. Supp. Memorandum
Regarding Plaintiff 's Removal From the No Fly List, ECF
Doc. 104, pp. 2–4.
   The district court agreed with the government's assess-
ment, but the Ninth Circuit reversed. 904 F. 3d 1033 (2018).
When a party seeks to moot a case based on its own volun-
tary cessation of challenged conduct, the Ninth Circuit held,
it must show that its “ `allegedly wrongful behavior' ” cannot
“ `reasonably be expected to recur.' ” Id., at 1039. And, the
court continued, the government's “mere announcement that
Fikre was removed” from the No Fly List fell short of sat-
isfying this standard. Ibid.
   On remand, the government tried again. Once more, it
did not contest the truth of Mr. Fikre's allegations concern-
ing his experiences. See Memorandum in Support of De-
fendants' Motion To Dismiss in No. 3:13–cv–899 (D Ore.),
ECF Doc. 146, pp. 21–23. But, this time, the government
relied on a declaration from Christopher R. Courtright, the
Acting Deputy Director for Operations of the Terrorist
240                      FBI v. FIKRE

                      Opinion of the Court

Screening Center. The declaration represented that
Mr. Fikre “will not be placed on the No Fly List in the future
based on the currently available information.” App. to Pet.
for Cert. 118a, ¶5. Persuaded by the government's latest
motion, the district court again dismissed Mr. Fikre's claims
as moot. 35 F. 4th, at 769.
   Again, however, the Ninth Circuit reversed. The govern-
ment's declaration might mean that Mr. Fikre “will not be
placed on the No Fly List now based on what he did in the
past.” Id., at 772. But, the Ninth Circuit reasoned, the
declaration does not disclose what conduct landed Mr. Fikre
on the No Fly List, and it does not ensure that he will “not
be placed on the List if . . . he . . . engag[es] in the same or
similar conduct” in the future. Ibid. As a result, the court
concluded, the government had still failed to meet its burden
of establishing that its allegedly unlawful conduct cannot
“ `reasonably be expected to recur.' ” Id., at 770.
   Shortly after the Ninth Circuit issued its decision, the
Page Proof Pending Publication
Fourth Circuit held that a similar declaration was suffcient
to moot another American citizen's lawsuit challenging his
placement on the No Fly List. See Long v. Pekoske, 38
F. 4th 417, 427 (CA4 2022). To resolve this confict in lower
court authority, the government asked us to hear Mr. Fikre's
case, and we agreed to do so. 600 U. S. ––– (2023).

                              II
   The Constitution grants federal courts jurisdiction to de-
cide “Cases” or “Controversies.” Art. III, §§ 1, 2. A court
with jurisdiction has a “virtually unfagging obligation” to
hear and resolve questions properly before it. Colorado
River Water Conservation Dist. v. United States, 424 U. S.
800, 817 (1976). But the converse also holds true. Some-
times, events in the world overtake those in the courtroom,
and a complaining party manages to secure outside of litiga-
tion all the relief he might have won in it. When that hap-
pens, a federal court must dismiss the case as moot. Al-
                   Cite as: 601 U. S. 234 (2024)             241

                      Opinion of the Court

ready, LLC v. Nike, Inc., 568 U. S. 85, 91 (2013). It must
because federal judges are not counselors or academics; they
are not free to take up hypothetical questions that pique a
party's curiosity or their own. The limited authority vested
in federal courts to decide cases and controversies means
that they may no more pronounce on past actions that do not
have any “continuing effect” in the world than they may
shirk decision on those that do. Spencer v. Kemna, 523 U. S.
1, 18 (1998).
   None of this implies that a defendant may “automatically
moot a case” by the simple expedient of suspending its chal-
lenged conduct after it is sued. Already, 568 U. S., at 91.
Instead, our precedents hold, a defendant's “ `voluntary ces-
sation of a challenged practice' ” will moot a case only if the
defendant can show that the practice cannot “ `reasonably be
expected to recur.' ” Friends of the Earth, Inc. v. Laidlaw
Environmental Services (TOC), Inc., 528 U. S. 167, 189
Page Proof Pending Publication
(2000); see United States v. W. T. Grant Co., 345 U. S. 629,
632–633 (1953).
   We have described this as a “formidable burden. ”
Friends of the Earth, 528 U. S., at 190. And the reason for
it is simple: “The Constitution deals with substance,” not
strategies. Cummings v. Missouri, 4 Wall. 277, 325 (1867).
Were the rule more forgiving, a defendant might suspend its
challenged conduct after being sued, win dismissal, and later
pick up where it left off; it might even repeat “this cycle” as
necessary until it achieves all of its allegedly “unlawful
ends.” Already, 568 U. S., at 91. A live case or controversy
cannot be so easily disguised, and a federal court's constitu-
tional authority cannot be so readily manipulated. To show
that a case is truly moot, a defendant must prove “ `no rea-
sonable expectation' ” remains that it will “return to [its] old
ways.” W. T. Grant Co., 345 U. S., at 632–633. That much
holds for governmental defendants no less than for private
ones. See, e. g., West Virginia v. EPA, 597 U. S. 697, 719
(2022); Trinity Lutheran Church of Columbia, Inc. v. Comer,
242                      FBI v. FIKRE

                      Opinion of the Court

582 U. S. 449, 457, n. 1 (2017); Parents Involved in Commu-
nity Schools v. Seattle School Dist. No. 1, 551 U. S. 701, 719–
720 (2007).
   The parties dispute none of these principles; the only ques-
tion we face concerns their application. Proceeding as the
courts below did, we accept Mr. Fikre's uncontested factual
allegations as true for purposes of this motion to dismiss.
See supra, at 237, n.*. As the lower courts did, too, we ac-
cept as true the supplemental evidence the government of-
fered: its declaration representing that Mr. Fikre “will not
be placed on the No Fly List in the future based on the
currently available information.” App. to Pet. for Cert.
118a, ¶5.
   Viewed in that light, this case is not moot. To appreciate
why, it is enough to consider one aspect of Mr. Fikre's com-
plaint. He contends that the government placed him on
the No Fly List for constitutionally impermissible reasons,
Page Proof Pending Publication
including his religious beliefs. In support of his claim,
Mr. Fikre alleges (among other things) that FBI agents in-
terrogated him about a mosque in Portland he once attended
and threatened to keep him on the No Fly List unless he
agreed to serve as an informant against his co-religionists.
Accepting these as-yet uncontested allegations, the govern-
ment's representation that it will not relist Mr. Fikre based
on “currently available information” may mean that his past
actions are not enough to warrant his relisting. But, as the
court of appeals observed, none of that speaks to whether
the government might relist him if he does the same or simi-
lar things in the future—say, attend a particular mosque or
refuse renewed overtures to serve as an informant. Put
simply, the government's sparse declaration falls short of
demonstrating that it cannot reasonably be expected to do
again in the future what it is alleged to have done in the
past. Friends of the Earth, 528 U. S., at 190.
   If its declaration alone will not do, the government asks
us to consider two further things. First, it points to the fact
                   Cite as: 601 U. S. 234 (2024)            243

                      Opinion of the Court

that it removed Mr. Fikre from the No Fly List in 2016.
The government acknowledges that it took this action only
after he fled suit. But, it stresses, the parties have now
sparred in court for some years since his delisting. Second,
the government surmises that, during this period, Mr. Fikre
“presumably has joined religious organizations” and inter-
acted freely with his co-religionists. Reply Brief 9. To-
gether, the government submits, these points make it un-
likely he will face relisting in the future.
   That, too, is insuffcient to warrant dismissal. A case does
not automatically become moot when a defendant suspends
its challenged conduct and then carries on litigating for some
specifed period. Nor can a defendant's speculation about a
plaintiff 's actions make up for a lack of assurance about its
own. (For that matter, given what little we know at this
stage in the proceedings, Mr. Fikre may have done none of
the things the government presumes he has, perhaps wish-
Page Proof Pending Publication
ing to but refraining for fear of fnding himself relisted.) In
all cases, it is the defendant's “burden to establish” that it
cannot reasonably be expected to resume its challenged
conduct—whether the suit happens to be new or long linger-
ing, and whether the challenged conduct might recur imme-
diately or later at some more propitious moment. West Vir-
ginia, 597 U. S., at 719. Nothing the government offers here
satisfes that formidable standard. See Parents Involved,
551 U. S., at 719 (declining to dismiss a case as moot fve
years after the defendant voluntarily ceased its challenged
conduct); City of Mesquite v. Aladdin's Castle, Inc., 455 U. S.
283, 288–289 (1982) (similar).
   Aiming now in a different direction, the government con-
tends that the Ninth Circuit erred by confating mootness
with the merits. The government reads portions of that
court's decisions as suggesting that, to win dismissal, it had
to admit it lacked any lawful basis for including Mr. Fikre on
the No Fly List in the frst place. For his part, Mr. Fikre
disputes this characterization of the Ninth Circuit's work;
244                      FBI v. FIKRE

                       Opinion of the Court

never, he says, did that court require the government to re-
pudiate its past conduct to prove mootness.
   Rather than resolve who has the better reading of another
court's decisions, it is enough to underline the reason for our
own. Yes, a party's repudiation of its past conduct may
sometimes help demonstrate that conduct is unlikely to
recur. See, e. g., County of Los Angeles v. Davis, 440 U. S.
625, 632–633 (1979). But often a case will become moot even
when a defendant “vehemently” insists on the propriety of
“the conduct that precipitated the lawsuit.” Already, 568
U. S., at 91. What matters is not whether a defendant repu-
diates its past actions, but what repudiation can prove about
its future conduct. It is on that consideration alone—the
potential for a defendant's future conduct—that we rest our
judgment.
   Necessarily, our judgment is a provisional one. Just be-
cause the government has not yet demonstrated that
Page Proof Pending Publication
Mr. Fikre's case is moot does not mean it will never be able
to do so. This case comes to us in a preliminary posture,
framed only by uncontested factual allegations and a terse
declaration. As the case unfolds, the complaint's allegations
will be tested rather than taken as true, and different facts
may emerge that may call for a different conclusion. That
is a possibility courts must be alive to in this (and any) case,
for a federal court's duty to ensure itself of Article III juris-
diction may begin at the inception of a lawsuit, but it persists
throughout the life of the proceedings. Spencer, 523 U. S.,
at 7.
   To be sure, litigating disputes that potentially touch on
matters of national security beyond the motion-to-dismiss
stage can present evidentiary challenges for parties and
courts alike. Careful attention must be paid to the handling
of classifed or privileged information. For our present pur-
poses, however, it is enough to know both sides agree that
“[a]dhering to traditional mootness principles is especially
important in this national-security context.” Reply Brief
                   Cite as: 601 U. S. 234 (2024)            245

                      Alito, J., concurring

18; see Brief for Petitioners 34; Brief for Respondent 45.
And adhering to those principles here, “it is impossible to
conclude” the government has so far “borne [its] burden” of
proving that this dispute is moot. Adarand Constructors,
Inc. v. Slater, 528 U. S. 216, 224 (2000) (per curiam).
                                *
  The judgment of the Court of Appeals for the Ninth
Circuit is
                                            Affrmed.

   Justice Alito, with whom Justice Kavanaugh joins,
concurring.
   I join the Court's opinion, but write to clarify my under-
standing that our decision does not suggest that the Govern-
ment must disclose classifed information to Mr. Fikre, his
attorney, or a court to show that this case is moot. In at
least some instances, requiring the Government to disclose
Page Proof Pending Publication
sensitive information regarding its grounds for placing or re-
moving a person from the No-Fly List could undermine the
Government's signifcant interests in airline safety and the
prevention of terrorist attacks. Indeed, some of the Na-
tion's 600-plus district courts are poorly positioned to handle
classifed documents, and most court personnel lack security
clearance. Recognizing such limitations, I do not under-
stand the Court's opinion to require the Government to dis-
close classifed information as a matter of course. On the
contrary, non-classifed information or information obtained
in discovery from the plaintiff in this and other cases may be
suffcient to show that the allegedly unlawful listing is un-
likely to recur, thereby proving mootness.
                           Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
Page Proof Pending Publication
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
punctuation. The following additional edits were made:

None

```

---

## GROUP: content/cases/Fare v. Michael C.md  (`case`, 5 assertions)

### content_page

```
---
title: "Fare v. Michael C."
type: case
citation: "442 U.S. 707 (1979)"
parallel_cite: "99 S. Ct. 2560; 61 L. Ed. 2d 197"
neutral_cite: 1979 U.S. LEXIS 133
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-10-01
docket: 78-334
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Fare v. Michael C.
  varies_by_point: false
  scope_note: "Good law; the juvenile totality-of-the-circumstances waiver test remains the rule (cf. J.D.B. v. North Carolina on age in the custody inquiry)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110117/fare-v-michael-c/"
  cluster_id: 110117
  opinion_id: 110117
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Miranda v. Arizona]]", "[[Yarborough v. Alvarado]]", "[[J.D.B. v. North Carolina]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "juvenile", "invocation", "waiver"]
holding: "A juvenile's request to speak with his probation officer is not a per se invocation of the Fifth Amendment (unlike a request for a lawyer); whether a juvenile validly waived his Miranda rights is judged by the totality of the circumstances."
lake:
  record_id: Fare v. Michael C
  status: verified
  projected_at: 2026-07-09
---

# Fare v. Michael C.

*442 U.S. 707 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Michael C., a 16-year-old on probation, was taken into custody on suspicion of murder and given [[Miranda and Custodial Interrogation|Miranda warnings]]. He asked to see his probation officer. Police did not produce the officer and continued questioning; Michael then waived his rights and made incriminating statements and sketches. The California Supreme Court held that his request for his probation officer was a [[Common Legal Terms#per-se|per se]] invocation of his Fifth Amendment rights, equivalent to a request for counsel, requiring that questioning stop.

## Issue
Whether a juvenile's request to speak with his probation officer is a [[Common Legal Terms#per-se|per se]] invocation of the Fifth Amendment right to counsel (or to silence), and by what standard a juvenile's waiver of [[Miranda and Custodial Interrogation|Miranda rights]] is measured.

## Rule
A request for a probation officer is not a [[Common Legal Terms#per-se|per se]] invocation. The [[Common Legal Terms#per-se|per se]] rule for a request for *counsel* rests on the lawyer's unique role: "A probation officer simply is not necessary, in the way an attorney is, for the protection of the legal rights of the accused, juvenile or adult." Accordingly, "[n]or do we believe that a request by a juvenile to speak with his probation officer constitutes a *per se* request to remain silent. ... we decline to find that the request for the probation officer is tantamount to the request for an attorney." — 442 U.S. at 724. ^pin-724

Juvenile waiver is governed by totality: "This totality-of-the-circumstances approach is adequate to determine whether there has been a waiver even where interrogation of juveniles is involved." — [*Id.* at 725](https://www.courtlistener.com/opinion/110117/fare-v-michael-c/#:~:text=This%20totality%2Dof%2Dthe%2Dcircumstances%20approach%20is%20adequate). ^pin-725

The inquiry weighs the juvenile's age, experience, education, background, and intelligence, and whether he understood the warnings and the consequences of waiving.

## Application
Michael's request for his probation officer was not, by itself, an invocation of counsel or silence that required questioning to cease; courts could instead consider that request as one factor in the totality. Looking to all the circumstances — his age, his prior experience with the justice system, the warnings he received and acknowledged, and his decision to talk after asking for the officer — the record supported a finding that he knowingly and voluntarily waived his Fifth Amendment rights, so his statements were admissible.

## Conclusion
A probation-officer request is not a [[Common Legal Terms#per-se|per se]] invocation; juvenile waivers are assessed under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]. The California Supreme Court's [[Common Legal Terms#per-se|per se]] rule was rejected and its judgment reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The totality test for juvenile waiver remains the rule. Later cases address the juvenile's status in the related **custody** inquiry: [[J.D.B. v. North Carolina]] (a child's age is part of the objective custody analysis), distinguishing [[Yarborough v. Alvarado]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Fare v. Michael C.*, 442 U.S. 707 (1979) — https://www.courtlistener.com/opinion/110117/fare-v-michael-c/ — pinpoints: 724, 725.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e4f7eb5b52005e1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "442 U.S. 707 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 133", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2560; 61 L. Ed. 2d 197", "title": "Fare v. Michael C.", "year": "1979"}}
{"assertion_id": "15cd349c50bc532d", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny", "title": "Fare v. Michael C."}}
{"assertion_id": "3908370853c1ebe7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A juvenile's request to speak with his probation officer is not a per se invocation of the Fifth Amendment (unlike a request for a lawyer); whether a juvenile validly waived his Miranda rights is judged by the totality of the circumstances.", "title": "Fare v. Michael C."}}
{"assertion_id": "ceca5ec3f9dbeda9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Fare v. Michael C."}}
{"assertion_id": "eb8d2dc10322059a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Fare v. Michael C.", "field_i_validity": "good_law", "scope_note": "Good law; the juvenile totality-of-the-circumstances waiver test remains the rule (cf. J.D.B. v. North Carolina on age in the custody inquiry).", "title": "Fare v. Michael C.", "varies_by_point": "false"}}
```

### lake record — Fare v. Michael C

```json
{
  "schema_version": "s2.v1",
  "record_id": "Fare v. Michael C",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Fare v. Michael C.",
    "case_name_short": "Fare",
    "case_name_full": "Fare, Acting Chief Probation Officer v. Michael C.",
    "input_case_name": "Fare v. Michael C.",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-10-01",
    "year": 1979,
    "docket": "78-334",
    "cluster_id": 110117,
    "lead_opinion_id": 110117,
    "sibling_ids": [
      110117,
      9427635,
      9427636,
      9427637
    ],
    "absolute_url": "/opinion/110117/fare-v-michael-c/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 707",
      "volume": "442",
      "reporter": "U.S.",
      "page": "707",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2560",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 197",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 133",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 707",
        "volume": "442",
        "reporter": "U.S.",
        "page": "707",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2560",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 197",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "197",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 133",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "133",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 707",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 707",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-724",
      "page": null,
      "quote": "--- # Fare v. Michael C. *442 U.S. 707 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Michael C., a 16-year-old on probation, was taken into custody on suspicion of murder and given Miranda warnings. He asked to see his probation officer. Police did not produce the officer and continued questioning; Michael then waived his rights and made incriminating statements and sketches. The California Supreme Court held that his request for his probation officer was a per se invocation of his Fifth Amendment rights, equivalent to a request for counsel, requiring that questioning stop. ## Issue Whether a juvenile's request to speak with his probation officer is a per se invocation of the Fifth Amendment right to counsel (or to silence), and by what standard a juvenile's waiver of Miranda rights is measured. ## Rule A request for a probation officer is not a per se invocation. The per se rule for a request for *counsel* rests on the lawyer's unique role:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-725",
      "page": null,
      "quote": "This totality-of-the-circumstances approach is adequate to determine whether there has been a waiver even where interrogation of juveniles is involved.",
      "star_marker": "725",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 41514,
      "fragment": "#:~:text=This%20totality%2Dof%2Dthe%2Dcircumstances%20approach%20is%20adequate",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Fare v. Michael C.",
    "varies_by_point": false,
    "scope_note": "Good law; the juvenile totality-of-the-circumstances waiver test remains the rule (cf. J.D.B. v. North Carolina on age in the custody inquiry).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "the State of Texas v. Kevin Castanedanieto",
          "cluster_id": 7857287,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Saldierna",
          "cluster_id": 4527726,
          "cite": [
            "817 S.E.2d 174",
            "371 N.C. 407"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Benitez",
          "cluster_id": 4465236,
          "cite": [
            "810 S.E.2d 781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kasey A. Smith",
          "cluster_id": 4442984,
          "cite": [
            "162 Idaho 878",
            "406 P.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2820149,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "CHARLES S. TURNER,CHRISTOPHER D. TURNER,RUSSELL L. OVERTON, LEVY ROUSE, CLIFTON E. YARBOROUGH, KELVIN D. SMITH, & TIMOTHY CATLETT",
          "cluster_id": 2807493,
          "cite": [
            "116 A.3d 894",
            "2015 D.C. App. LEXIS 262"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zaitar",
          "cluster_id": 2662455,
          "cite": [
            "858 F. Supp. 2d 103",
            "2012 WL 1570865",
            "2012 U.S. Dist. LEXIS 63313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane1_negative"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Berkemer v. McCarty",
          "cluster_id": 111249,
          "cite": [
            "82 L. Ed. 2d 317",
            "104 S. Ct. 3138",
            "468 U.S. 420",
            "1984 U.S. LEXIS 140",
            "52 U.S.L.W. 5023"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reno v. Flores",
          "cluster_id": 112833,
          "cite": [
            "123 L. Ed. 2d 1",
            "113 S. Ct. 1439",
            "507 U.S. 292",
            "1993 U.S. LEXIS 2399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burger v. Kemp",
          "cluster_id": 111957,
          "cite": [
            "97 L. Ed. 2d 638",
            "107 S. Ct. 3114",
            "483 U.S. 776",
            "1987 U.S. LEXIS 3047"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
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
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Bradshaw",
          "cluster_id": 110987,
          "cite": [
            "77 L. Ed. 2d 405",
            "103 S. Ct. 2830",
            "462 U.S. 1039",
            "1983 U.S. LEXIS 82",
            "51 U.S.L.W. 4940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Male Juvenile (95-Cr-1074)",
          "cluster_id": 744606,
          "cite": [
            "121 F.3d 34",
            "1997 U.S. App. LEXIS 19219",
            "1997 WL 416548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Muniz",
          "cluster_id": 112464,
          "cite": [
            "110 L. Ed. 2d 528",
            "110 S. Ct. 2638",
            "496 U.S. 582",
            "1990 U.S. LEXIS 3211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leif Taylor v. Thomas M. Maddox, Interim Director George Galaza Cal Terhune",
          "cluster_id": 786028,
          "cite": [
            "366 F.3d 992",
            "2004 U.S. App. LEXIS 9068",
            "2004 WL 1043343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neal v. State",
          "cluster_id": 1869722,
          "cite": [
            "451 So. 2d 743"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Shatzer",
          "cluster_id": 1734,
          "cite": [
            "175 L. Ed. 2d 1045",
            "130 S. Ct. 1213",
            "559 U.S. 98",
            "2010 U.S. LEXIS 1899"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Oklahoma",
          "cluster_id": 112142,
          "cite": [
            "101 L. Ed. 2d 702",
            "108 S. Ct. 2687",
            "487 U.S. 815",
            "1988 U.S. LEXIS 3028",
            "56 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Stephenson",
          "cluster_id": 2410270,
          "cite": [
            "878 S.W.2d 530",
            "1994 Tenn. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solem v. Stumes",
          "cluster_id": 111112,
          "cite": [
            "79 L. Ed. 2d 579",
            "104 S. Ct. 1338",
            "465 U.S. 638",
            "1984 U.S. LEXIS 36",
            "52 U.S.L.W. 4307"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Fare v. Michael C:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110117 OR 9427635 OR 9427636 OR 9427637) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzI3Mjc2ODAwMDAwJnM9MjUwNzgyNyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110117+OR+9427635+OR+9427636+OR+9427637%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110117 OR 9427635 OR 9427636 OR 9427637)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjkmcz0yMjM0NTEyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110117+OR+9427635+OR+9427636+OR+9427637%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110117 OR 9427635 OR 9427636 OR 9427637)",
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
    "complete_query": "cites:(110117 OR 9427635 OR 9427636 OR 9427637)",
    "indexed_citing_opinions": 1106,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110117,
        "count": 995,
        "count_source": "search"
      },
      {
        "opinion_id": 9427635,
        "count": 136,
        "count_source": "search"
      },
      {
        "opinion_id": 9427636,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427637,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1729,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/fare-v-michael-c.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwNDYzMTEmcz0xMDI3NjE4OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110117+OR+9427635+OR+9427636+OR+9427637%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110117,
        "cited_id": 88971,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 103992,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 106018,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 106421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 107439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 108378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 109430,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 109997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 348757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 1185789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 1247133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 1396562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 1412703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110117,
        "cited_id": 2176459,
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
    "date_created": "2026-07-05T03:20:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:20:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:20:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:24:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:20:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Fare v. Michael C

```
<div>
<center><b><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">442 U.S. 707</a></span> (1979)</b></center>
<center><h1>FARE, ACTING CHIEF PROBATION OFFICER<br>
v.<br>
MICHAEL C.</h1></center>
<center>No. 78-334.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1979.</center>
<center>Decided June 20, 1979.</center>
CERTIORARI TO THE SUPREME COURT OF CALIFORNIA.
<p><span class="star-pagination">*708</span> <i>Mark Alan Hart,</i> Deputy Attorney General of California, argued the cause for petitioner. With him on the briefs were <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>S. Clark Moore,</i> Assistant Attorney General, and <i>James H. Kline</i> and <i>Shunji Asari,</i> Deputy Attorneys General.</p>
<p><span class="star-pagination">*709</span> <i>Albert J. Menaster</i> argued the cause for respondent. With him on the brief were <i>Wilbur F. Littlefield, Dennis A. Fischer,</i> and <i>Kenneth I. Clayman.</i><sup>[*]</sup></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court. established certain procedural safeguards designed to protect the rights of an accused, under the Fifth and Fourteenth Amendments, to be free from compelled self-incrimination during custodial interrogation. The Court specified, among other things, that if the accused indicates in any manner that he wishes to remain silent or to consult an attorney, interrogation must cease, and any statement obtained from him during interrogation thereafter may not be admitted against him at his trial. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 444-445, 473-474</a></span>.</p>
<p>In this case, the State of California, in the person of its acting chief probation officer, attacks the conclusion of the Supreme Court of California that a juvenile's request, made while undergoing custodial interrogation, to see his <i>probation officer</i> is <i>per se</i> an invocation of the juvenile's Fifth Amendment rights as pronounced in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p></p>
<h2>I</h2>
<p>Respondent Michael C. was implicated in the murder of Robert Yeager. The murder occurred during a robbery of the victim's home on January 19, 1976. A small truck registered in the name of respondent's mother was identified as having been near the Yeager home at the time of the killing, and a young man answering respondent's description was seen by witnesses near the truck and near the home shortly before Yeager was murdered.</p>
<p><span class="star-pagination">*710</span> On the basis of this information, Van Nuys, Cal., police took respondent into custody at approximately 6:30 p. m. on February 4. Respondent then was 16 1/2 years old and on probation to the Juvenile Court. He had been on probation since the age of 12. Approximately one year earlier he had served a term in a youth corrections camp under the supervision of the Juvenile Court. He had a record of several previous offenses, including burglary of guns and purse snatching, stretching back over several years.</p>
<p>Upon respondent's arrival at the Van Nuys station house two police officers began to interrogate him. The officers and respondent were the only persons in the room during the interrogation. The conversation was tape-recorded. One of the officers initiated the interview by informing respondent that he had been brought in for questioning in relation to a murder. The officer fully advised respondent of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. The following exchange then occurred, as set out in the opinion of the California Supreme Court, <i>In re Michael C.,</i> <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#473" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d 471, 473-474</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#8" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d 7, 8</a></span> (1978) (emphasis added by that court):</p>
<blockquote>"Q. . . . Do you understand all of these rights as I have explained them to you?</blockquote>
<blockquote>"A. Yeah.</blockquote>
<blockquote>"Q. Okay, do you wish to give up your right to remain silent and talk to us about this murder?</blockquote>
<blockquote>"A. What murder? I don't know about no murder.</blockquote>
<blockquote>"Q. I'll explain to you which one it is if you want to talk to us about it.</blockquote>
<blockquote>"A. Yeah, I might talk to you.</blockquote>
<blockquote>"Q. Do you want to give up your right to have an attorney present here while we talk about it?</blockquote>
<blockquote>"A. <i>Can I have my probation officer here?</i>
</blockquote>
<blockquote>"Q. Well I can't get a hold of your probation officer right now. You have the right to an attorney.</blockquote>
<blockquote>"A. How I know you guys won't pull no police officer in and tell me he's an attorney?</blockquote>
<blockquote>
<span class="star-pagination">*711</span> "Q. Huh?</blockquote>
<blockquote>"A. [How I know you guys won't pull no police officer in and tell me he's an attorney?]</blockquote>
<blockquote>"Q. Your probation officer is Mr. Christiansen.</blockquote>
<blockquote>"A. Yeah.</blockquote>
<blockquote>"Q. Well I'm not going to call Mr. Christiansen tonight. There's a good chance we can talk to him later, but I'm not going to call him right now. If you want to talk to us without an attorney present, you can. If you don't want to, you don't have to. But if you want to say something, you can, and if you don't want to say something you don't have to. That's your right. You understand that right?</blockquote>
<blockquote>"A. Yeah.</blockquote>
<blockquote>"Q. Okay, will you talk to us without an attorney present?</blockquote>
<blockquote>"A. Yeah I want to talk to you."</blockquote>
<p>Respondent thereupon proceeded to answer questions put to him by the officers. He made statements and drew sketches that incriminated him in the Yeager murder.</p>
<p>Largely on the basis of respondent's incriminating statements, probation authorities filed a petition in Juvenile Court alleging that respondent had murdered Robert Yeager, in violation of Cal. Penal Code Ann. § 187 (West Supp. 1979), and that respondent therefore should be adjudged a ward of the Juvenile Court, pursuant to Cal. Welf. &amp; Inst. Code Ann. § 602 (West Supp. 1979).<sup>[1]</sup> App. 4-5. Respondent thereupon moved to suppress the statements and sketches he gave the police during the interrogation. He alleged that the statements had been obtained in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in that <span class="star-pagination">*712</span> his request to see his probation officer at the outset of the questioning constituted an invocation of his Fifth Amendment right to remain silent, just as if he had requested the assistance of an attorney. Accordingly, respondent argued that since the interrogation did not cease until he had a chance to confer with his probation officer, the statements and sketches could not be admitted against him in the Juvenile Court proceedings. In so arguing, respondent relied by analogy on the decision in <i>People</i> v. <i>Burton,</i> <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">6 Cal. 3d 375</a></span>, <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">491 P. 2d 793</a></span> (1971), where the Supreme Court of California had held that a minor's request, made during custodial interrogation, to see his parents constituted an invocation of the minor's Fifth Amendment rights.</p>
<p>In support of his suppression motion, respondent called his probation officer, Charles P. Christiansen, as a witness. Christiansen testified that he had instructed respondent that if at any time he had "a concern with his family," or ever had "a police contact," App. 27, he should get in touch with his probation officer immediately. The witness stated that, on a previous occasion, when respondent had had a police contact and had failed to communicate with Christiansen, the probation officer had reprimanded him. <i>Id.,</i> at 28. This testimony, respondent argued, indicated that when he asked for his probation officer, he was in fact asserting his right to remain silent in the face of further questioning.</p>
<p>In a ruling from the bench, the court denied the motion to suppress. <i>Id.,</i> at 41-42. It held that the question whether respondent had waived his right to remain silent was one of fact to be determined on a case-by-case basis, and that the facts of this case showed a "clear waiver" by respondent of that right. <i>Id.,</i> at 42. The court observed that the transcript of the interrogation revealed that respondent specifically had told the officers that he would talk with them, and that this waiver had come at the outset of the interrogation and not after prolonged questioning. The court noted that <span class="star-pagination">*713</span> respondent was a "16 and a half year old minor who has been through the court system before, has been to [probation] camp, has a probation officer, [and is not] a young, naive minor with no experience with the courts." <i>Ibid.</i> Accordingly, it found that on the facts of the case respondent had waived his Fifth Amendment rights, notwithstanding the request to see his probation officer.<sup>[2]</sup></p>
<p>On appeal, the Supreme Court of California took the case by transfer from the California Court of Appeal and, by a divided vote, reversed. <i>In re Michael C.,</i> <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d 471</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d 7</a></span> (1978). The court held that respondent's "request to see his probation officer at the commencement of interrogation negated any possible willingness on his part to discuss his case with the police [and] thereby invoked his Fifth Amendment privilege." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#474" aria-description="Citation for case: Fare v. Michael C."><i>Id.,</i> at 474</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#8" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 8</a></span>. The court based this conclusion on its view that, because of the juvenile court system's emphasis on the relationship between a probation officer and the probationer, the officer was "a trusted guardian figure who exercises the authority of the state as <i>parens patriae</i> and whose duty it is to implement <span class="star-pagination">*714</span> the protective and rehabilitative powers of the juvenile court." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#476" aria-description="Citation for case: Fare v. Michael C."><i>Id.,</i> at 476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. As a consequence, the court found that a minor's request for his probation officer was the same as a request to see his parents during interrogation, and thus under the rule of <i><span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">Burton</a></span></i> constituted an invocation of the minor's Fifth Amendment rights.</p>
<p>The fact that the probation officer also served as a peace officer, and, whenever a proceeding against a juvenile was contemplated, was charged with a duty to file a petition alleging that the minor had committed an offense, did not alter, in the court's view, the fact that the officer in the eyes of the juvenile was a trusted guardian figure to whom the minor normally would turn for help when in trouble with the police. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#476" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. Relying on <i><span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">Burton</a></span>,</i> the court ruled that it would unduly restrict <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to limit its reach in a case involving a minor to a request by the minor for an attorney, since it would be "`fatuous to assume that a minor in custody will be in a position to call an attorney for assistance and it is unrealistic to attribute no significance to his call for help from the only person to whom he normally looksa parent or guardian.'" <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#475" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 475-476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#9" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 9</a></span>, quoting <i>People</i> v. <i>Burton,</i> <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#382" aria-description="Citation for case: People v. Burton">6 Cal. 3d, at 382</a></span>, <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#797" aria-description="Citation for case: People v. Burton">491 P. 2d, at 797-798</a></span>. The court dismissed the concern expressed by the State that a request for a probation officer could not be distinguished from a request for one's football coach, music teacher, or clergyman on the ground that the probation officer, unlike those other figures in the juvenile's life, was charged by statute to represent the interests of the juvenile. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>.</p>
<p>The court accordingly held that the probation officer would act to protect the minor's Fifth Amendment rights in precisely the way an attorney would act if called for by the accused. In so holding, the court found the request for a probation officer to be a <i>per se</i> invocation of Fifth Amendment rights in the same way the request for an attorney was found <span class="star-pagination">*715</span> in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to be, regardless of what the interrogation otherwise might reveal. In rejecting a totality-of-the-circumstances inquiry, the court stated:</p>
<blockquote>"Here, however, we face conduct which, regardless of considerations of capacity, coercion or voluntariness, per se invokes the privilege against self-incrimination. Thus our question turns not on whether the [respondent] had the ability, capacity or willingness to give a knowledgeable waiver, and hence whether he acted voluntarily, but whether, when he called for his probation officer, he exercised his Fifth Amendment privilege. We hold that in doing so he no less invoked the protection against self-incrimination than if he asked for the presence of an attorney." <i>Ibid.,</i> <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10-11</a></span>.</blockquote>
<p>See also <i><span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">id.,</a></span></i> at 478 n. 4, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 11</a></span> n. 4. The court went on to conclude that since the State had not met its "burden of proving that a minor who requests to see his probation officer does not intend to assert his Fifth Amendment privilege," <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#478" aria-description="Citation for case: Fare v. Michael C."><i>id.,</i> at 478</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#11" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 11</a></span>, the trial court should not have admitted the confessions obtained after respondent had requested his probation officer.<sup>[3]</sup></p>
<p><span class="star-pagination">*716</span> The State of California petitioned this Court for a writ of certiorari. MR. JUSTICE REHNQUIST, as Circuit Justice, stayed the execution of the mandate of the Supreme Court of California. <span class="citation" data-id="109997"><a href="/opinion/109997/fare-acting-chief-probation-officer-v-michael-c/" aria-description="Citation for case: Fare, Acting Chief Probation Officer v. Michael C.">439 U. S. 1310</a></span> (1978). Because the California judgment extending the <i>per se</i> aspects of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> presents an important question about the reach of that case, we thereafter issued the writ. <span class="citation multiple-matches"><a href="/c/U.%20S./439/925/">439 U. S. 925</a></span> (1978).</p>
<p></p>
<h2>II</h2>
<p>We note at the outset that it is clear that the judgment of <span class="star-pagination">*717</span> the California Supreme Court rests firmly on that court's interpretation of federal law. This Court, however, has not heretofore extended the <i>per se</i> aspects of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> safeguards beyond the scope of the holding in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case itself.<sup>[4]</sup> We therefore must examine the California court's decision to determine whether that court's conclusion so to extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is in harmony with <i>Miranda'</i>s underlying principles. For it is clear that "a State may not impose . . . greater restrictions as a matter of <i>federal constitutional law</i> when this Court specifically refrains from imposing them." <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 719</a></span> (1975) (emphasis in original). See <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369</a></span> (1979).</p>
<p>The rule the Court established in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is clear. In order to be able to use statements obtained during custodial interrogation of the accused, the State must warn the accused prior to such questioning of his right to remain silent and of his right to have counsel, retained or appointed, present during interrogation. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 473</a></span>. "Once [such] warnings have been given, the subsequent procedure is clear." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i></p>
<blockquote>"If the individual indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease. At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. . . . If the individual states that he wants an attorney, the interrogation must cease until an attorney is present. At that time, the <span class="star-pagination">*718</span> individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning. If the individual cannot obtain an attorney and he indicates that he wants one before speaking to police, they must respect his decision to remain silent." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 473-474</a></span> (footnote omitted).</blockquote>
<p>Any statements obtained during custodial interrogation conducted in violation of these rules may not be admitted against the accused, at least during the State's case in chief. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 479</a></span>. Cf. <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/#224" aria-description="Citation for case: Harris v. New York">401 U. S. 222, 224</a></span> (1971).</p>
<p>Whatever the defects, if any, of this relatively rigid requirement that interrogation must cease upon the accused's request for an attorney, <i>Miranda'</i>s holding has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis. See <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443-446</a></span> (1974).</p>
<p>The California court in this case, however, significantly has extended this rule by providing that a request by a juvenile for his probation officer has the same effect as a request for an attorney. Based on the court's belief that the probation officer occupies a position as a trusted guardian figure in the minor's life that would make it normal for the minor to turn to the officer when apprehended by the police, and based as well on the state-law requirement that the officer represent the interest of the juvenile, the California decision found that consultation with a probation officer fulfilled the role for the juvenile that consultation with an attorney does in general, <span class="star-pagination">*719</span> acting as a "`protective [device] . . . to dispel the compulsion inherent in custodial surroundings.'" <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>, quoting <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 458</a></span>.</p>
<p>The rule in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> however, was based on this Court's perception that the lawyer occupies a critical position in our legal system because of his unique ability to protect the Fifth Amendment rights of a client undergoing custodial interrogation. Because of this special ability of the lawyer to help the client preserve his Fifth Amendment rights once the client becomes enmeshed in the adversary process, the Court found that "the right to have counsel present at the interrogation is indispensable to the protection of the Fifth Amendment privilege under the system" established by the Court. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 469</a></span>. Moreover, the lawyer's presence helps guard against overreaching by the police and ensures that any statements actually obtained are accurately transcribed for presentation into evidence. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 470</a></span>.</p>
<p>The <i>per se</i> aspect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was thus based on the unique role the lawyer plays in the adversary system of criminal justice in this country. Whether it is a minor or an adult who stands accused, the lawyer is the one person to whom society as a whole looks as the protector of the legal rights of that person in his dealings with the police and the courts. For this reason, the Court fashioned in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> the rigid rule that an accused's request for an attorney is <i>per se</i> an invocation of his Fifth Amendment rights, requiring that all interrogation cease.</p>
<p>A probation officer is not in the same posture with regard to either the accused or the system of justice as a whole. Often he is not trained in the law, and so is not in a position to advise the accused as to his legal rights. Neither is he a trained advocate, skilled in the representation of the interests of his client before both police and courts. He does not assume the power to act on behalf of his client by virtue of his status as adviser, nor are the communications of the accused to the probation officer shielded by the lawyer-client privilege.</p>
<p><span class="star-pagination">*720</span> Moreover, the probation officer is the employee of the State which seeks to prosecute the alleged offender. He is a peace officer, and as such is allied, to a greater or lesser extent, with his fellow peace officers. He owes an obligation to the State, notwithstanding the obligation he may also owe the juvenile under his supervision. In most cases, the probation officer is duty bound to report wrongdoing by the juvenile when it comes to his attention, even if by communication from the juvenile himself. Indeed, when this case arose, the probation officer had the responsibility for filing the petition alleging wrongdoing by the juvenile and seeking to have him taken into the custody of the Juvenile Court. It was respondent's probation officer who filed the petition against him, and it is the acting chief of probation for the State of California, a probation officer, who is petitioner in this Court today.<sup>[5]</sup></p>
<p><span class="star-pagination">*721</span> In these circumstances, it cannot be said that the probation officer is able to offer the type of independent advice that an accused would expect from a lawyer retained or assigned to assist him during questioning. Indeed, the probation officer's duty to his employer in many, if not most, cases would conflict sharply with the interests of the juvenile. For where an attorney might well advise his client to remain silent in the face of interrogation by the police, and in doing so would be "exercising [his] good professional judgment . . . to protect to the extent of his ability the rights of his client," <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#480" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 480-481</a></span>, a probation officer would be bound to advise his charge to cooperate with the police. The justices who concurred in the opinion of the California Supreme Court in this case aptly noted: "Where a conflict between the minor and the law arises, the probation officer can be neither neutral nor in the minor's corner." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#479" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 479</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#12" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 12</a></span>. It thus is doubtful that a general rule can be established that a juvenile, in every case, looks to his probation officer as a "trusted guardian figure" rather than as an officer of the court system that imposes punishment.</p>
<p>By the same token, a lawyer is able to protect his client's rights by learning the extent, if any, of the client's involvement in the crime under investigation, and advising his client accordingly. <span class="star-pagination">*722</span> To facilitate this, the law rightly protects the communications between client and attorney from discovery. We doubt, however, that similar protection will be afforded the communications between the probation officer and the minor. Indeed, we doubt that a probation officer, consistent with his responsibilities to the public and his profession, could withhold from the police or the courts facts made known to him by the juvenile implicating the juvenile in the crime under investigation.</p>
<p>We thus believe it clear that the probation officer is not in a position to offer the type of legal assistance necessary to protect the Fifth Amendment rights of an accused undergoing custodial interrogation that a lawyer can offer. The Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> recognized that "the attorney plays a vital role in the administration of criminal justice under our Constitution." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#481" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 481</a></span>. It is this pivotal role of legal counsel that justifies the <i>per se</i> rule established in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> and that distinguishes the request for counsel from the request for a probation officer, a clergyman, or a close friend. A probation officer simply is not necessary, in the way an attorney is, for the protection of the legal rights of the accused, juvenile or adult. He is significantly handicapped by the position he occupies in the juvenile system from serving as an effective protector of the rights of a juvenile suspected of a crime.</p>
<p>The California Supreme Court, however, found that the close relationship between juveniles and their probation officers compelled the conclusion that a probation officer, for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> was sufficiently like a lawyer to justify extension of the <i>per se</i> rule. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#476" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. The fact that a relationship of trust and cooperation between a probation officer and a juvenile might exist, however, does not indicate that the probation officer is capable of rendering effective legal advice sufficient to protect the juvenile's rights during interrogation by the police, or of providing the other services rendered by a lawyer. To find otherwise <span class="star-pagination">*723</span> would be "an extension of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requirements [that] would cut this Court's holding in that case completely loose from its own explicitly stated rationale." <i>Beckwith</i> v. <i>United States,</i> <span class="citation" data-id="9426365"><a href="/opinion/109430/beckwith-v-united-states/#345" aria-description="Citation for case: Beckwith v. United States">425 U. S. 341, 345</a></span> (1976). Such an extension would impose the burdens associated with the rule of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> on the juvenile justice system and the police without serving the interests that rule was designed simultaneously to protect. If it were otherwise, a juvenile's request for almost anyone he considered trustworthy enough to give him reliable advice would trigger the rigid rule of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>Similarly, the fact that the State has created a statutory duty on the part of the probation officer to protect the interests of the juvenile does not render the probation officer any more capable of rendering legal assistance to the juvenile or of protecting his legal rights, especially in light of the fact that the State has also legislated a duty on the part of the officer to report wrongdoing by the juvenile and serve the ends of the juvenile court system. The State cannot transmute the relationship between probation officer and juvenile offender into the type of relationship between attorney and client that was essential to the holding of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> simply by legislating an amorphous "duty to advise and care for the juvenile defendant." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. Though such a statutory duty might serve to distinguish to some degree the probation officer from the coach and the clergyman, it does not justify the extension of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to requests to see probation officers. If it did, the State could expand the class of persons covered by the <i>Miranda per se</i> rule simply by creating a duty to care for the juvenile on the part of other persons, regardless of whether the logic of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> would justify that extension.</p>
<p>Nor do we believe that a request by a juvenile to speak with his probation officer constitutes a <i>per se</i> request to remain silent. As indicated, since a probation officer does not fulfill the important role in protecting the rights of the accused <span class="star-pagination">*724</span> juvenile that an attorney plays, we decline to find that the request for the probation officer is tantamount to the request for an attorney. And there is nothing inherent in the request for a probation officer that requires us to find that a juvenile's request to see one necessarily constitutes an expression of the juvenile's right to remain silent. As discussed below, courts may take into account such a request in evaluating whether a juvenile in fact had waived his Fifth Amendment rights before confessing. But in other circumstances such a request might well be consistent with a desire to speak with the police. In the absence of further evidence that the minor intended in the circumstances to invoke his Fifth Amendment rights by such a request, we decline to attach such overwhelming significance to this request.</p>
<p>We hold, therefore, that it was error to find that the request by respondent to speak with his probation officer <i>per se</i> constituted an invocation of respondent's Fifth Amendment right to be free from compelled self-incrimination. It therefore was also error to hold that because the police did not then cease interrogating respondent the statements he made during interrogation should have been suppressed.</p>
<p></p>
<h2>III</h2>
<p><i>Miranda</i> further recognized that after the required warnings are given the accused, "[i]f the interrogation continues without the presence of an attorney and a statement is taken, a heavy burden rests on the government to demonstrate that the defendant knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>. We noted in <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#373" aria-description="Citation for case: North Carolina v. Butler">441 U. S., at 373</a></span>, that the question whether the accused waived his rights "is not one of form, but rather whether the defendant in fact knowingly and voluntarily waived the rights delineated in the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case." Thus, the determination whether statements obtained during custodial <span class="star-pagination">*725</span> interrogation are admissible against the accused is to be made upon an inquiry into the totality of the circumstances surrounding the interrogation, to ascertain whether the accused in fact knowingly and voluntarily decided to forgo his rights to remain silent and to have the assistance of counsel. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475-477</a></span>.</p>
<p>This totality-of-the-circumstances approach is adequate to determine whether there has been a waiver even where interrogation of juveniles is involved. We discern no persuasive reasons why any other approach is required where the question is whether a juvenile has waived his rights, as opposed to whether an adult has done so. The totality approach permits indeed, it mandatesinquiry into all the circumstances surrounding the interrogation. This includes evaluation of the juvenile's age, experience, education, background, and intelligence, and into whether he has the capacity to understand the warnings given him, the nature of his Fifth Amendment rights, and the consequences of waiving those rights. See <i>North Carolina</i> v. <i><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">Butler, supra</a></span></i><i>.</i></p>
<p>Courts repeatedly must deal with these issues of waiver with regard to a broad variety of constitutional rights. There is no reason to assume that such courtsespecially juvenile courts, with their special expertise in this areawill be unable to apply the totality-of-the-circumstances analysis so as to take into account those special concerns that are present when young persons, often with limited experience and education and with immature judgment, are involved. Where the age and experience of a juvenile indicate that his request for his probation officer or his parents is, in fact, an invocation of his right to remain silent, the totality approach will allow the court the necessary flexibility to take this into account in making a waiver determination. At the same time, that approach refrains from imposing rigid restraints on police and courts in dealing with an experienced older juvenile with an extensive prior record who knowingly and intelligently waives <span class="star-pagination">*726</span> his Fifth Amendment rights and voluntarily consents to interrogation.</p>
<p>In this case, we conclude that the California Supreme Court should have determined the issue of waiver on the basis of all the circumstances surrounding the interrogation of respondent. The Juvenile Court found that under this approach, respondent in fact had waived his Fifth Amendment rights and consented to interrogation by the police after his request to see his probation officer was denied. Given its view of the case, of course, the California Supreme Court did not consider this issue, though it did hold that the State had failed to prove that, notwithstanding respondent's request to see his probation officer, respondent had not intended to invoke his Fifth Amendment rights.</p>
<p>We feel that the conclusion of the Juvenile Court was correct. The transcript of the interrogation reveals that the police officers conducting the interrogation took care to ensure that respondent understood his rights. They fully explained to respondent that he was being questioned in connection with a murder. They then informed him of all the rights delineated in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> and ascertained that respondent understood those rights. There is no indication in the record that respondent failed to understand what the officers told him. Moreover, after his request to see his probation officer had been denied, and after the police officer once more had explained his rights to him, respondent clearly expressed his willingness to waive his rights and continue the interrogation.</p>
<p>Further, no special factors indicate that respondent was unable to understand the nature of his actions. He was a 16 1/2-year-old juvenile with considerable experience with the police. He had a record of several arrests. He had served time in a youth camp, and he had been on probation for several years. He was under the full-time supervision of probation authorities. There is no indication that he was of insufficient intelligence to understand the rights he was waiving, or what the consequences of that waiver would be. He was not <span class="star-pagination">*727</span> worn down by improper interrogation tactics or lengthy questioning or by trickery or deceit.</p>
<p>On these facts, we think it clear that respondent voluntarily and knowingly waived his Fifth Amendment rights. Respondent argues, however, that any statements he made during interrogation were coerced. Specifically, respondent alleges that the police made threats and promises during the interrogation to pressure him into cooperating in the hope of obtaining leniency for his cooperative attitude. He notes also that he repeatedly told the officers during his interrogation that he wished to stop answering their questions, but that the officers ignored his pleas. He argues further that the record reveals that he was afraid that the police would coerce him, and that this fear caused him to cooperate. He points out that at one point the transcript revealed that he wept during the interrogation.</p>
<p>Review of the entire transcript reveals that respondent's claims of coercion are without merit. As noted, the police took care to inform respondent of his rights and to ensure that he understood them. The officers did not intimidate or threaten respondent in any way. Their questioning was restrained and free from the abuses that so concerned the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445-455</a></span>. The police did indeed indicate that a cooperative attitude would be to respondent's benefit, but their remarks in this regard were far from threatening or coercive. And respondent's allegation that he repeatedly asked that the interrogation cease goes too far: at some points he did state that he did not know the answer to a question put to him or that he could not, or would not, answer the question, but these statements were not assertions of his right to remain silent.</p>
<p></p>
<h2>IV</h2>
<p>We hold, in short, that the California Supreme Court erred in finding that a juvenile's request for his probation officer was a <i>per se</i> invocation of that juvenile's Fifth Amendment <span class="star-pagination">*728</span> rights under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> We conclude, rather, that whether the statements obtained during subsequent interrogation of a juvenile who has asked to see his probation officer, but who has not asked to consult an attorney or expressly asserted his right to remain silent, are admissible on the basis of waiver remain a question to be resolved on the totality of the circumstances surrounding the interrogation. On the basis of the record in this case, we hold that the Juvenile Court's findings that respondent voluntarily and knowingly waived his rights and consented to continued interrogation, and that the statements obtained from him were voluntary, were proper, and that the admission of those statements in the proceeding against respondent in Juvenile Court was correct.</p>
<p>The judgment of the Supreme Court of California is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN and MR. JUSTICE STEVENS join, dissenting.</p>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court sought to ensure that the inherently coercive pressures of custodial interrogation would not vitiate a suspect's privilege against self-incrimination. Nothing that these pressures "can operate very quickly to overbear the will of one merely made aware of his privilege," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 469</a></span>, the Court held:</p>
<blockquote>"If [a suspect in custody] indicates in any manner, at any time prior to or during questioning, that he wishes to remain silent, the interrogation must cease. At this point he has shown that he intends to exercise his Fifth Amendment privilege; any statement taken after the person invokes his privilege cannot be other than the product of compulsion, subtle or otherwise. . . . If the individual states that he wants an attorney, the interrogation <span class="star-pagination">*729</span> must cease until an attorney is present." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#473" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 473-474</a></span> (footnote omitted).</blockquote>
<p>See also <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 444-445</a></span>.</p>
<p>As this Court has consistently recognized, the coerciveness of the custodial setting is of heightened concern where, as here, a juvenile is under investigation. In <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span> (1948), the plurality reasoned that because a 15 1/2-year-old minor was particularly susceptible to overbearing interrogation tactics, the voluntariness of his confession could not "be judged by the more exacting standards of maturity." <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio"><i>Id.,</i> at 599</a></span>. The Court reiterated this point in <i>Gallegos</i> v. <i>Colorado,</i> <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#54" aria-description="Citation for case: Gallegos v. Colorado">370 U. S. 49, 54</a></span> (1962), observing that a 14-year-old suspect could not "be compared with an adult in full possession of his senses and knowledgeable of the consequences of his admissions." The juvenile defendant, in the Court's view, required</p>
<blockquote>"the aid of more mature judgment as to the steps he should take in the predicament in which he found himself. A lawyer or an adult relative or friend could have given the petitioner the protection which his own immaturity could not." <i><span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/" aria-description="Citation for case: Gallegos v. Colorado">Ibid.</a></span></i>
</blockquote>
<p>And, in <i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#55" aria-description="Citation for case: In Re GAULT">387 U. S. 1, 55</a></span> (1967), the Court admonished that "the greatest care must be taken to assure that [a minor's] admission was voluntary."</p>
<p>It is therefore critical in the present context that we construe <i>Miranda'</i>s prophylactic requirements broadly to accomplish their intended purpose"dispel[ling] the compulsion inherent in custodial surroundings." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 458</a></span>. To effectuate this purpose, the Court must ensure that the "protective device" of legal counsel, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#465" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 465-466, 469</a></span>, be readily available, and that any intimation of a desire to preclude questioning be scrupulously honored. Thus, I believe <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires that interrogation cease whenever a juvenile requests an adult who is obligated to represent his interests. Such a <span class="star-pagination">*730</span> request, in my judgment, constitutes both an attempt to obtain advice and a general invocation of the right to silence. For, as the California Supreme Court recognized, "`[i]t is fatuous to assume that a minor in custody will be in a position to call an attorney for assistance,'" <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#475" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d 471, 475-476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#9" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d 7, 9</a></span> (1978), quoting <i>People</i> v. <i>Burton,</i> <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#382" aria-description="Citation for case: People v. Burton">6 Cal. 3d 375, 382</a></span>, <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#797" aria-description="Citation for case: People v. Burton">491 P. 2d 793, 797</a></span> (1971), or that he will trust the police to obtain a lawyer for him.<sup>[1]</sup> A juvenile in these circumstances will likely turn to his parents, or another adult responsible for his welfare, as the only means of securing legal counsel. Moreover, a request for such adult assistance is surely inconsistent with a present desire to speak freely. Requiring a strict verbal formula to invoke the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> would "protect the knowledgeable accused from stationhouse coercion while abandoning the young person who knows no more than to ask for the . . . person he trusts." <i>Chaney</i> v. <i>Wainwright,</i> <span class="citation" data-id="9464113"><a href="/opinion/348757/ben-chaney-v-louie-l-wainwright-secretary-of-the-florida-department-of/#1134" aria-description="Citation for case: Ben Chaney v. Louie L. Wainwright, Secretary of the...">561 F. 2d 1129, 1134</a></span> (CA5 1977) (Goldberg, J., dissenting).</p>
<p>On my reading of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> a California juvenile's request for his probation officer should be treated as a <i>per se</i> assertion of Fifth Amendment rights. The California Supreme Court determined that probation officers have a statutory duty to represent minors' interests and, indeed, are "trusted guardian figure[s]" to whom a juvenile would likely turn for assistance. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#476" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 476</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. In addition, the court found, probation officers are particularly well suited to assist a juvenile "on such matters as to whether or not he should obtain an attorney" and "how to conduct himself with police." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#476" aria-description="Citation for case: Fare v. Michael C."><i>Id.,</i> at 476, 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>. Hence, a juvenile's request <span class="star-pagination">*731</span> for a probation officer may frequently be an attempt to secure protection from the coercive aspects of custodial questioning.<sup>[2]</sup></p>
<p>This Court concludes, however, that because a probation officer has law enforcement duties, juveniles generally would not call upon him to represent their interests, and if they did, would not be well served. <i>Ante,</i> at 721-722. But that conclusion ignores the California Supreme Court's express determination that the officer's responsibility to initiate juvenile proceedings did not negate his function as personal adviser to his wards.<sup>[3]</sup> I decline to second-guess that court's assessment of state law. See <i>Murdock</i> v. <i>Memphis,</i> <span class="citation" data-id="9416986"><a href="/opinion/88971/murdock-v-city-of-memphis/#626" aria-description="Citation for case: Murdock v. City of Memphis">20 Wall. 590, 626</a></span> (1875); <i>General Trading Co.</i> v. <i>State Tax Comm'n,</i> <span class="citation" data-id="9419509"><a href="/opinion/103992/general-trading-co-v-state-tax-commission-of-iowa/#337" aria-description="Citation for case: General Trading Co. v. State Tax Commission of Iowa">322 U. S. 335, 337</a></span> (1944); <i>Scripto, Inc.</i> v. <i>Carson,</i> <span class="citation" data-id="106018"><a href="/opinion/106018/scripto-inc-v-carson/#210" aria-description="Citation for case: Scripto, Inc. v. Carson">362 U. S. 207, 210</a></span> (1960).<sup>[4]</sup> Further, although the majority here speculates <span class="star-pagination">*732</span> that probation officers have a duty to advise cooperation with the police, <i>ante,</i> at 721a proposition suggested only in the concurring opinion of two justices below, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#479" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 479</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#11" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 11-12</a></span> (Mosk, J., joined by Bird, C. J., concurring)respondent's probation officer instructed all his charges "not to go and admit openly to an offense, [but rather] to get some type of advice from . . . parents or a lawyer." App. 30. Absent an explicit statutory provision or judicial holding, the officer's assessment of the obligations imposed by state law is entitled to deference by this Court.</p>
<p>Thus, given the role of probation officers under California law, a juvenile's request to see his officer may reflect a desire for precisely the kind of assistance <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> guarantees an accused before he waives his Fifth Amendment rights. At the very least, such a request signals a desire to remain silent until contact with the officer is made. Because the Court's contrary determination withdraws the safeguards of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> from those most in need of protection, I respectfully dissent.</p>
<p>MR. JUSTICE POWELL, dissenting.</p>
<p>Although I agree with the Court that the Supreme Court of California misconstrued <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966),<sup>[1]</sup> I would not reverse the California court's judgment. This Court repeatedly has recognized that "the greatest care" must be taken to assure that an alleged confession of a juvenile was voluntary. See, <i>e. g., </i><i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">387 U. S. 1</a></span>, 55 <span class="star-pagination">*733</span> (1967); <i>Gallegos</i> v. <i>Colorado,</i> <span class="citation" data-id="9422423"><a href="/opinion/106421/gallegos-v-colorado/#54" aria-description="Citation for case: Gallegos v. Colorado">370 U. S. 49, 54</a></span> (1962); <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599-600</a></span> (1948) (plurality opinion). Respondent was a young person, 16 years old at the time of his arrest and the subsequent prolonged interrogation at the station house. Although respondent had had prior brushes with the law, and was under supervision by a probation officer, the taped transcript of his interrogationas well as his testimony at the suppression hearingdemonstrates that he was immature, emotional,<sup>[2]</sup> and uneducated, and therefore was likely to be vulnerable to the skillful, two-on-one, repetitive style of interrogation to which he was subjected. App. 54-82.</p>
<p>When given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and asked whether he desired an attorney, respondent requested permission to "have my probation officer here," a request that was refused. <i>Id.,</i> at 55. That officer testified later that he had communicated frequently with respondent, that respondent had serious and "extensive" family problems, and that the officer had instructed respondent to call him immediately "at any time he has a police contact, even if they stop him and talk to him on the street." <i>Id.,</i> at 26-31.<sup>[3]</sup> The reasons given by the probation officer for having so instructed his charge were substantially the same reasons that prompt this Court to examine with special care the circumstances under which a minor's alleged confession was obtained. After stating that respondent had been "going through problems," the officer observed that "many times the kids don't understand what is going on, and what they are supposed to do relative to police . . . ." <i>Id.,</i> at 29. This view of the limited understanding of the average 16-year-old was borne out by respondent's question when, <span class="star-pagination">*734</span> during interrogation, he was advised of his right to an attorney: "How I know you guys won't pull no police officer in and tell me he's an attorney?" <i>Id.,</i> at 55. It was during this part of the interrogation that the police had denied respondent's request to "have my probation officer here." <i>Ibid.</i></p>
<p>The police then proceeded, despite respondent's repeated denial of any connection to the murder under investigation, see <i>id.,</i> at 56-60, persistently to press interrogation until they extracted a confession. In <i>In re Gault,</i> in addressing police interrogation of detained juveniles, the Court stated:</p>
<blockquote>"If counsel was not present for some permissible reason when an admission was obtained [from a child], the greatest care must be taken to assure that the admission was voluntary, in the sense not only that it was not coerced or suggested, but also that it was not the product of ignorance of rights or of adolescent fantasy, fright or despair." <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/#55" aria-description="Citation for case: In Re GAULT">387 U. S., at 55</a></span>.</blockquote>
<p>It is clear that the interrogating police did not exercise "the greatest care" to assure that respondent's "admission was voluntary."<sup>[4]</sup> In the absence of counsel, and having refused to call the probation officer, they nevertheless engaged in protracted interrogation.</p>
<p>Although I view the case as close, I am not satisfied that this particular 16-year-old boy, in this particular situation, was subjected to a fair interrogation free from inherently coercive circumstances. For these reasons, I would affirm the judgment of the Supreme Court of California.</p>
<h2>NOTES</h2>
<p>[*]  <i>Fred E. Inbau, Frank G. Carrington, Wayne W. Schmidt, George Nicholson, Edwin L. Miller, Jr.,</i> and <i>Peter C. Lehman</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  The petition also alleged that respondent had participated in an attempted armed robbery earlier on the same evening Yeager was murdered. The Juvenile Court, however, held that the evidence was insufficient to support this charge and it was dismissed. App. 6. No issue relating to this second charge is before the Court.</p>
<p>[2]  The California Court of Appeal, in an opinion reported and then vacated, affirmed. <i>In re Michael C.,</i> <span class="citation no-link">135 Cal. Rptr. 762</span> (1977). That court noted that since the Juvenile Court's findings of fact resolved against respondent his contention that the confession had been coerced from him by threats and promises, it would have to "conclude that there was a knowing and intelligent waiver of the minor's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights unless it can be said that the request to speak to a probation officer was in and of itself sufficient to invoke" respondent's Fifth Amendment privilege. <i>Id.,</i> at 765-766 (footnote omitted). It refused to extend the rule of <i>People</i> v. <i>Burton,</i> <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">6 Cal. 3d 375</a></span>, <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">491 P. 2d 793</a></span> (1971), to include a request for a probation officer, finding it difficult to distinguish such a request from a request to see "one's football coach, music teacher or clergyman." 135 Cal. Rptr., at 766. Even if the <i><span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">Burton</a></span></i> rule were applicable, the court held, there was sufficient evidence of an affirmative waiver of his rights by respondent to distinguish <i><span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">Burton</a></span>,</i> where the California Supreme Court had noted that there was "nothing in the way of affirmative proof that defendant did not intend to assert his privilege." <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#383" aria-description="Citation for case: People v. Burton">6 Cal. 3d, at 383</a></span>, <span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/#798" aria-description="Citation for case: People v. Burton">491 P. 2d, at 798</a></span>.</p>
<p>[3]  Two justices concurred in the court's opinion and judgment. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#478" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 478</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#11" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 11</a></span>. They expressed concern that a probation officer's public responsibilities would make it difficult for him to offer legal advice to a minor implicated in a crime, and that a minor advised to cooperate with the police, perhaps even to confess, justifiably could complain later "that he had been subjected to a variation of the Mutt-and-Jeff technique criticized in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i> initial interrogating by overbearing officers, then comforting by a presumably friendly and gentle peace officer in the guise of a probation officer." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 479</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#12" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 12</a></span>.
</p>
<p>Two justices dissented. <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#480" aria-description="Citation for case: Fare v. Michael C."><i>Id.,</i> at 480</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#12" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 12</a></span>. They would have affirmed respondent's conviction on the basis of the finding of the Juvenile Court that, in light of all the circumstances surrounding the interrogation of respondent, there was sufficient affirmative proof that respondent had waived his privilege.</p>
<p>The dissenters pointed out that the opinion of the court was confusing in holding, on the one hand, that the request for a probation officer was <i>per se</i> an invocation of the minor's Fifth Amendment rights, and, on the other, that reversal was required because the State had not carried its burden of proving that respondent, by requesting his probation officer, did not intend thereby to assert his Fifth Amendment privilege. <i>Ibid.,</i> <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#12" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 12-13</a></span>.</p>
<p>There may well be ambiguity in this regard. See <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C."><i>id.,</i> at 477-478</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#11" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 11</a></span>. On the basis of that ambiguity, respondent argues that the California court did not establish a <i>per se</i> rule, but held only that on the facts here respondent's request to see his probation officer constituted an invocation of his Fifth Amendment rights. The decision in <i>People</i> v. <i>Randall,</i> <span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/" aria-description="Citation for case: People v. Randall">1 Cal. 3d 948</a></span>, <span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/" aria-description="Citation for case: People v. Randall">464 P. 2d 114</a></span> (1970), upon which the California court relied in both <i><span class="citation" data-id="9619138"><a href="/opinion/1396562/people-v-burton/" aria-description="Citation for case: People v. Burton">Burton</a></span></i> and the present case, however, indicates that the court did indeed establish a <i>per se</i> rule in this case. In <i><span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/" aria-description="Citation for case: People v. Randall">Randall</a></span>,</i> the court stated that even though a suspect might have invoked his Fifth Amendment rights by asking for counsel or by stating he wished to remain silent, it might be possible that subsequent voluntary statements of the accused, not prompted by custodial interrogation, would be admissible if the State could show that they were the product of the voluntary decision of the accused to waive the rights he had asserted. <i>People</i> v. <i>Randall,</i> <span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/#956" aria-description="Citation for case: People v. Randall">1 Cal. 3d, at 956</a></span>, and n. 7, <span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/#119" aria-description="Citation for case: People v. Randall">464 P. 2d, at 119</a></span>, and n. 7.</p>
<p><i>Randall</i> thus indicates that the <i>per se</i> language employed by the California Supreme Court in this case is compatible with the finding that the State could have negated the <i>per se</i> effect of the request for a probation officer by showing that, notwithstanding his <i>per se</i> invocation of his rights, respondent later voluntarily decided to waive those rights and volunteer statements. In light of <i><span class="citation" data-id="9581593"><a href="/opinion/1247133/people-v-randall/" aria-description="Citation for case: People v. Randall">Randall</a></span>,</i> and in light of the strong <i>per se</i> language used by the California Supreme Court in its opinion in this case, see, <i>e. g.,</i> <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10-11</a></span>, we think that any ambiguity in that opinion must be resolved in favor of a conclusion that the court did in fact establish a <i>per se</i> rule.</p>
<p>[4]  Indeed, this Court has not yet held that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> applies with full force to exclude evidence obtained in violation of its proscriptions from consideration in juvenile proceedings, which for certain purposes have been distinguished from formal criminal prosecutions. See <i>McKeiver</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9424648"><a href="/opinion/108378/mckeiver-v-pennsylvania/#540" aria-description="Citation for case: McKeiver v. Pennsylvania">403 U. S. 528, 540-541</a></span> (1971) (plurality opinion). We do not decide that issue today. In view of our disposition of this case, we assume without deciding that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> principles were fully applicable to the present proceedings.</p>
<p>[5]  When this case arose, a California statute provided that a proceeding in juvenile court to declare a minor a ward of the court was to be commenced by the filing of a petition by a probation officer. Cal. Welf. &amp; Inst. Code Ann. § 650 (West 1972). This provision since has been amended to provide that most such petitions are to be filed by the prosecuting attorney. 1976 Cal. Stats., ch. 1071, § 20. Respondent argues that, whatever the status of the probation officer as a peace officer at the time this case arose, the amendment of § 650 indicates that in the future a probation officer is not to be viewed as a legal adversary of the accused juvenile. Consequently, respondent believes that any holding of this Court with regard to respondent's 1976 request for a probation officer will be mere dictum with regard to a juvenile's similar request today. Brief for Respondent 9-10, and n. 4.
</p>
<p>We disagree. The fact that a California probation officer in 1976 was responsible for initiating a complaint is only one factor in our analysis. The fact remains that a probation officer does not fulfill the role in our system of criminal justice that an attorney does, regardless of whether he acts merely as a counselor or has significant law enforcement duties. And in California, as in many States, the other duties of a probation officer are incompatible with the view that he may act as a counselor to a juvenile accused of crime. The very California statute that imposes upon the probation officer the duty to represent the interests of the juvenile also provides: "It shall be the duty of the probation officer to prepare for every hearing [of criminal charges against a juvenile] a social study of the minor, containing such matters as may be relevant to a proper disposition of the case." Cal. Welf. &amp; Inst. Code Ann. § 280 (West Supp. 1979).</p>
<p>Similarly, a probation officer is required, upon the order of the juvenile court or the Youth Authority, to investigate the circumstances surrounding the charge against the minor and to file written reports and recommendations. §§ 281, 284. And a probation officer in California continues to have the powers and authority of a peace officer in connection with any violation of a criminal statute that is discovered by the probation officer in the course of his probation activities. § 283; Cal. Penal Code Ann. § 830.5 (West 1970). The duties of a peace officer, like the investigative and reporting duties of probation officers, are incompatible with the role of legal adviser to a juvenile accused of crime.</p>
<p>[1]  The facts of the instant case are illustrative. When the police offered to obtain an attorney for respondent, he replied: "How I know you guys won't pull no police officer in and tell me he's an attorney?" <i>Ante,</i> at 710. Significantly, the police made no attempt to allay that concern. See <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 476</a></span> n. 3, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span> n. 3.</p>
<p>[2]  The Court intimates that construing a request for a probation officer as an invocation of the Fifth Amendment privilege would undermine the specificity of <i>Miranda'</i>s prophylactic rules. <i>Ante,</i> at 718. Yet the Court concedes that the statutory duty to "advise and care for the juvenile defendant," <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>, distinguishes probation officers from other adults, such as coaches and clergymen. <i>Ante,</i> at 723. Since law enforcement officials should be on notice of such legal relationships, they would presumably have no difficulty determining whether a suspect has asserted his Fifth Amendment rights.
</p>
<p>Although I agree with my Brother POWELL that, on the facts here, respondent was not "subjected to a fair interrogation free from inherently coercive circumstances," <i>post,</i> at 734, I do not believe a case-by-case approach provides police sufficient guidance, or affords juveniles adequate protection.</p>
<p>[3]  In filing the petition and performing the other functions enumerated <i>ante,</i> at 720-721, n. 5, the probation officer must act in the best interests of the minor. See <i>In re Steven C.,</i> <span class="citation" data-id="2176459"><a href="/opinion/2176459/pebbles-v-steven-c/#264" aria-description="Citation for case: Pebbles v. Steven C.">9 Cal. App. 3d 255, 264-265</a></span>, <span class="citation" data-id="2176459"><a href="/opinion/2176459/pebbles-v-steven-c/#101" aria-description="Citation for case: Pebbles v. Steven C.">88 Cal. Rptr. 97, 101-102</a></span> (1970).</p>
<p>[4]  One thing is certain. The California Supreme Court is more familiar with the duties and performance of its probation officers than we are.
</p>
<p>Of course, "[i]t is peculiarly within the competence of the highest court of a State to determine that in its jurisdiction the police should be subject to more stringent rules than are required as a federal constitutional minimum." <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#728" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 728</a></span> (1975) (MARSHALL, J., dissenting). See also <i>People</i> v. <i>Disbrow,</i> <span class="citation" data-id="9551944"><a href="/opinion/1185789/people-v-disbrow/" aria-description="Citation for case: People v. Disbrow">16 Cal. 3d 101</a></span>, <span class="citation" data-id="9551944"><a href="/opinion/1185789/people-v-disbrow/" aria-description="Citation for case: People v. Disbrow">545 P. 2d 272</a></span> (1976) (refusing to follow <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971)); Brennan, State Constitutions and the Protection of Individual Rights, <span class="citation no-link">90 Harv. L. Rev. 489</span> (1977).</p>
<p>[1]  The California Supreme Court, purporting to apply <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> stated:
</p>
<p>"Here . . . we face conduct which, regardless of considerations of capacity, coercion or voluntariness, per se invokes the privilege against self-incrimination." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d 471, 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d 7, 10</a></span> (1978). I agree with the Court's opinion today that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot be read as support for any such <i>per se</i> rule.</p>
<p>[2]  The Juvenile Court Judge observed that he had "heard the tapes" of the interrogation, and was "aware of the fact that Michael [respondent] was crying at the time he talked to the police officers." App. 53.</p>
<p>[3]  The Supreme Court of California stated that a "probation officer is an official appointed pursuant to legislative enactment `to represent the interests' of the juvenile [and] . . . has borne the duty to advise and care for the juvenile defendant." <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#477" aria-description="Citation for case: Fare v. Michael C.">21 Cal. 3d, at 477</a></span>, <span class="citation" data-id="9624545"><a href="/opinion/1412703/fare-v-michael-c/#10" aria-description="Citation for case: Fare v. Michael C.">579 P. 2d, at 10</a></span>.</p>
<p>[4]  Minors who become embroiled with the law range from the very young up to those on the brink of majority. Some of the older minors become fully "street-wise," hardened criminals, deserving no greater consideration than that properly accorded all persons suspected of crime. Other minors are more of a child than an adult. As the Court indicated in <i>In re Gault,</i> <span class="citation" data-id="9423418"><a href="/opinion/107439/in-re-gault/" aria-description="Citation for case: In Re GAULT">387 U. S. 1</a></span> (1967), the facts relevant to the care to be exercised in a particular case vary widely. They include the minor's age, actual maturity, family environment, education, emotional and mental stability, and, of course, any prior record he might have.</p>

</div>
```

---
