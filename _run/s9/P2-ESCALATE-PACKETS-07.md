# P2 ESCALATE PACKET 07/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-5838fac703 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Immigration & Naturalization Service v. Lopez-Mendoza.json
- **problem:** The lake pinpoint for pin-1039 is not the opinion quotation; it is harvested content-page boilerplate ending before the asserted identity quote.
- **verbatim:** The “body” or identity of a defendant or respondent
- **tally:** codex-A=stands: The cached opinion contains the identity sentence at the 1039 page marker.  |  codex-B=refuted: Lens B does not evaluate quote fidelity or support.  |  opus=stands-modified: Blob is page prose incl markdown headers; the 'mismatch' is a mis-scope artifact, not a demonstrated misquote.
- **proposed_fix:** Replace pin-1039's harvested boilerplate with the actual opinion sentence beginning 'The “body” or identity...' and keep the pinpoint at 468 U.S. at 1039.

### F-S9-PR-927dbab20e · quote-fidelity · sev=medium · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/Immigration & Naturalization Service v. Lopez-Mendoza.json
- **problem:** The quoted 1050 sentence is not character-faithful to the cached full opinion text: the content/lake quote says 'Janis' but the disclosed opinion text reads 'Jams'. The lake record also flags quote_fidelity as mismatch.
- **verbatim:** the <em>Jams </em>balance between costs and benefits
- **tally:** codex-A=stands: The pinpoint lands on the 1050 passage, but character fidelity fails against text/<case>.txt.  |  codex-B=refuted: Lens B does not evaluate quote fidelity or support.  |  opus=stands-modified: Quote reads as genuine Lopez-Mendoza language but is unverified from disclosed evidence.
- **proposed_fix:** Verify against an official/corrected source and either repair the cached text or mark this as a corrected quotation rather than a character-faithful extraction from the disclosed text.

### F-S9-PR-785c7c812d · quote-fidelity · sev=medium · needs_cl=false · quorum=2/3
- **object:** _overhaul2/lake/cases/Jacobson v. United States.json
- **problem:** The stored pin-548 quote is the content page's own preamble markdown (title, header line, HTML comment, Background, Issue, and the 'Rule ... predates its own conduct.' lead-in), which does not appear in the source opinion. quote_fidelity is a genuine mismatch.
- **verbatim:** --- # Jacobson v. United States *503 U.S. 540 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** ... ## Rule Where the government induces the crime, it must prove predisposition that predates its ow…
- **tally:** codex-A=MISSING  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands: The stored/asserted quote is page preamble markdown absent from the cached opinion; a real quote-fidelity defect in the pinpoint record.
- **proposed_fix:** Restore pin-548's quote field to the passage the content page renders at ^pin-548 ('Government agents may not originate a criminal design, implant in an innocent person's mind the disposition to comm…

### F-S9-PR-b052599489 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Kansas v. Glover.json
- **problem:** The pin-1186 payload is a copied content-page/header/background chunk, not a verbatim passage from the opinion at 1186.
- **verbatim:** We hold that when the officer lacks information negating an inference that the owner is the driver of the vehicle, the stop is reasonable.
- **tally:** codex-A=stands: The disclosed opinion text contains the actual holding at *1186.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Shipped page quote at ^pin-1186 is verbatim at cached p-11 and correctly pincited to 140 S. Ct. at 1186; no user-facing defect.
- **proposed_fix:** Replace pin-1186 with the actual holding sentence from the opinion and set the star marker to 1186.

### F-S9-PR-ca004f28e4 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Kansas v. Glover.json
- **problem:** The pin-1191 payload is not a verbatim quote from the opinion. It combines content-page paraphrase with the sentence 'The Court cabined the rule' and omits the actual quoted sentence at 1191.
- **verbatim:** We emphasize the narrow scope of our holding. Like all seizures, "[t]he officer's action must be 'justified at its inception.' "
- **tally:** codex-A=stands: The disclosed opinion text at 1191 says 'We emphasize the narrow scope of our holding.'  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Shipped page quote 'We emphasize the narrow scope of our holding.' is verbatim at cached p-44 and correctly pincited to 1191; no user-facing defect.
- **proposed_fix:** Replace the pin-1191 quote with the actual opinion text: 'We emphasize the narrow scope of our holding.' Keep the surrounding owner-is-driver discussion as paraphrase, not as a quote pinpoint.

### F-S9-PR-283f01bdea · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Katz v. United States.json
- **problem:** The lake pin-351 quote is not character-faithful to the opinion passage and appears to have harvested content-page Issue/Rule prose rather than the cited 389 U.S. at 351 text.
- **verbatim:** For the Fourth Amendment protects people, not places. What a person knowingly exposes to the public, even in his own home or office, is not a subject of Fourth Amendment protection.
- **tally:** codex-A=stands: The payload quote includes markdown section text: ## Rule The inquiry is personal, not spatial:, which is not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Shipped page quote is verbatim at cached b461-5 (opinion 'For the Fourth Amendment protects people, not places...'); the leading 'For' is properly dropped, the Lewis/Lee citation string is properly e…
- **proposed_fix:** Replace the pin-351 quote with the actual page-351 passage beginning with the Fourth Amendment protects people, not places, or remove the corrupted pinpoint.

### F-S9-PR-679b4b4091 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/LaChance v. Erickson.json
- **problem:** The lake pinpoint quote for pin-265 is not a verbatim opinion quote; it is a harvested chunk of the generated page/header/background prose and stops before the actual Bryson quotation.
- **verbatim:** --- # LaChance v. Erickson
- **tally:** codex-A=stands: The payload begins with generated markdown/page material, not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The literal harvested quote payload is page chrome (frontmatter + Background/Issue/Rule intro ending at 'Quoting *Bryson*:'), not a verbatim opinion quotation, so the assertion as framed cannot stand…
- **proposed_fix:** Replace pin-265's stored quote with the actual Bryson quotation used in the Rule paragraph and tie it to star page 265.

### F-S9-PR-2dc59ffee4 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Lange v. California.json
- **problem:** pin-op1's harvested quote is not the opinion passage it purports to support; it is page/header/background/rule text from the built content page, and the lake itself flags quote_fidelity as mismatch. The visible Rule quote also differs from the cached opinion's em-dash spacing.
- **verbatim:** The question presented here is whether the pursuit of a fleeing misdemeanor suspect always—or more legally put, categorically—qualifies as an exigent circumstance. We hold it does not.
- **tally:** codex-A=stands: The payload quote begins with built-page markdown/front matter content, not Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The stored quote is markdown, not a Lange quote, and is honestly self-flagged 'mismatch'.
- **proposed_fix:** Replace pin-op1 with the actual opinion passage: "The question presented here is whether the pursuit of a fleeing misdemeanor suspect always—or more legally put, categorically—qualifies as an exigent…

### F-S9-PR-e3e45ab0e8 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Lefkowitz v. Turley.json
- **problem:** pin-84's stored quote is not an opinion quote; it is a harvested content-page header/background/issue/rule chunk, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** Also, given adequate immunity, the State may plainly insist that employees either answer questions under oath about the performance of their job or suffer the loss of employment.
- **tally:** codex-A=stands: The payload quote begins with markdown front matter/content-page prose, not the judicial opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is markdown, not a Lefkowitz quote (honestly flagged mismatch).
- **proposed_fix:** Replace pin-84 with the actual source passage at star page 84 beginning with the adequate-immunity sentence.

### F-S9-PR-39cfdb0250 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Lego v. Twomey.json
- **problem:** The stored pin-489 quote in the lake record is not the opinion passage at 404 U.S. 489; it is a corrupted excerpt from the generated content page/header/background and is itself marked quote_fidelity=mismatch.
- **verbatim:** --- # Lego v. Twomey *404 U.S. 477 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
- **tally:** codex-A=stands: The disclosed full opinion text contains the relevant page-489 passage: the Court says that when a confession challenged as involuntary is used at trial, the defendant is entitled to a reliable and c…  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is markdown, not a Lego quote (honestly flagged mismatch).
- **proposed_fix:** Replace lake pinpoints[].quote for pin-489 with the actual page-489 opinion passage beginning with the Court's 'when a confession challenged as involuntary...' language, and set the page/star marker…

### F-S9-PR-00838606ca · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Lewis v. United States (1966).json
- **problem:** The pin-211 quote in the lake record is not a verbatim opinion passage; it stitches content-page background, issue, and rule prose and does not appear in the cached opinion text.
- **verbatim:** But when, as here, the home is converted into a commercial center to which outsiders are invited for purposes of transacting unlawful business, that business is entitled to no greater sanctity than i…
- **tally:** codex-A=stands: Exact search of the cached opinion text does not verify the lake pin-211 quoted string.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is markdown, not a Lewis quote (honestly flagged mismatch).
- **proposed_fix:** Replace pin-211 with the actual page-211 rule passage from the opinion, such as the commercial-center sentence beginning 'when, as here, the home is converted...', and revalidate the pinpoint at star…

### F-S9-PR-1db3fd5925 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Lo-Ji Sales, Inc. v. New York.json
- **problem:** pin-326's recorded quote is not an opinion quote; it contains content-page prose and Markdown headings rather than the cited judicial passage.
- **verbatim:** The Town Justice did not manifest that neutrality and detachment demanded of a judicial officer
- **tally:** codex-A=stands: The payload quote includes content artifacts such as '## Issue' and '## Rule', not language from the opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored pinpoint quote is content-page markdown ('## Issue', '## Rule', a page paraphrase) - none of it is verbatim opinion text.
- **proposed_fix:** Replace the pin-326 quote with the actual page-326 passage quoted on the content page, or mark the rule sentence as authorial synthesis rather than a quotation.

### F-S9-PR-1a5551b93e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Los Angeles County v. Rettele.json
- **problem:** The pin-1993 lake quote is not an opinion quote; it is copied page markdown/background text. It therefore cannot serve as a character-faithful quote pinpoint for the cited rule passage.
- **verbatim:** --- # Los Angeles County v. Rettele *550 U.S. 609 (2007)*
- **tally:** codex-A=stands: The lake pinpoint text starts with page markdown rather than the Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored pinpoint quote is harvested page front-matter/markdown, not source text.
- **proposed_fix:** Replace pin-1993 with the actual opinion passage beginning 'The deputies needed a moment to secure the room...' and correct the content quote's punctuation so the first sentence ends with a period ra…

### F-S9-PR-b7c10d7a7d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Maryland v. King.json
- **problem:** The pin-465 lake pinpoint quote is not the quoted holding passage; it is a harvested content-page/frontmatter fragment and the lake itself marks quote_fidelity as mismatch with page and position null. The content page's visible quote is substantively supported by the opinion text, but it is not cha…
- **verbatim:** cheek swab of the arrestee’s DNA is, like fingerprinting and photographing, a legitimate police booking procedure that is reasonable under the Fourth Amendment.
- **tally:** codex-A=stands: The lake pinpoint quote begins with '--- # Maryland v. King' and includes the page Background/Issue/Rule preface rather than the opinion passage.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content Rule quote anchored at ^pin-465 matches the slip conclusion verbatim (cached text: 'When officers make an arrest ... reasonable under the Fourth Amendment.'), and 569 U.S. 465-466 is the Cour…
- **proposed_fix:** Replace pin-465 with the exact Court-opinion sentence beginning 'When officers make an arrest...' from the cached opinion text, preserving typography, or mark the page quote as normalized rather than…

### F-S9-PR-bcad44f39b · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Maryland v. Macon.json
- **problem:** The recorded pin-469 quote is not a court quote; it is harvested content-page/frontmatter text ending at the Rule heading, so it is not character-faithful to the Macon opinion.
- **verbatim:** The officer’s action in entering the bookstore and examining the wares that were intentionally exposed to all who frequent the place of business did not infringe a legitimate, expectation of privacy…
- **tally:** codex-A=stands: The lake pinpoints[].quote for pin-469 begins with page markup/frontmatter text, not the opinion text.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity or support.  |  opus=stands-modified: Displayed 'No search' Rule quote anchored at ^pin-469 matches the slip verbatim except the content correctly omits an OCR-inserted comma ('legitimate, expectation' -> 'legitimate expectation'); pinci…
- **proposed_fix:** Replace pin-469 with the actual page 469 no-search sentence from the cached opinion text, and set the page/pin status accordingly.

### F-S9-PR-12d28368cc · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Maryland v. Pringle.json
- **problem:** The pin-372 quote in the lake/inventory is not a verbatim opinion passage at page 372; it is a harvested excerpt of the built content page header/background/rule. The displayed Rule quote also is not character-faithful to the cached text because the cached text reads 'knowledge, of,' while the page…
- **verbatim:** We think it an entirely reasonable inference from these facts that any or all three of the occupants had knowledge, of, and exercised dominion and control over, the cocaine. Thus, a reasonable office…
- **tally:** codex-A=stands: The inventory itself marks quote_fidelity as mismatch.  |  codex-B=refuted: This row is a quote_fidelity assertion; Lens B does not make support or quote-fidelity findings.  |  opus=stands-modified: Displayed Rule quote anchored at ^pin-372 matches the slip verbatim except the content omits an OCR-inserted comma ('knowledge, of,' -> 'knowledge of,'); pincite 540 U.S. 372 confirmed by the label='…
- **proposed_fix:** Replace pin-372 with the exact opinion passage from the cached text at star page 372 and preserve disclosed punctuation, or remove the pinpoint quote until reharvested correctly.

### F-S9-PR-8fb3b0ab17 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Maryland v. Shatzer.json
- **problem:** The reviewed pinpoint quote in the lake record is not the opinion quotation; it is a harvested content-page/frontmatter-style excerpt and is itself marked quote_fidelity=mismatch. The actual slip-opinion passage at page 11 supports the content page's displayed 14-day quote, but not the lake pinpoin…
- **verbatim:** It seems to us that period is 14 days.
- **tally:** codex-A=stands: The lake pinpoint quote begins with page markup rather than the Court's opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no treatment or currency defect is raised for this row.  |  opus=stands-modified: Displayed Rule quote anchored at ^pin-op11 matches the slip verbatim (line-wrap hyphenation aside); pincite 'slip op., at 11' confirmed both by the page-12 header immediately after the passage and by…
- **proposed_fix:** Replace pin-op11's lake pinpoints[].quote with the actual slip-opinion page 11 quotation used on the content page, normalizing only PDF line wraps and soft hyphens; do not remove the valid content-pa…

### F-S9-PR-cb24ecc132 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Maryland v. Wilson.json
- **problem:** pin-415's recorded quote is not character-faithful to the opinion; it is a flattened excerpt of the built page, and the lake itself flags quote_fidelity as mismatch.
- **verbatim:** We therefore hold that an officer making a traffic stop may order passengers to get out of the car pending completion of the stop.
- **tally:** codex-A=stands: The disclosed lake pinpoint has quote_fidelity: mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual ^pin-415 block quote on the content page ('We therefore hold that an officer making a traffic stop may order passengers to get out of the car pending completion of the stop.') matches the…
- **proposed_fix:** Replace pin-415's stored quote with the exact holding sentence from the opinion and record the page/star marker as 415 if supported.

### F-S9-PR-e50cf79fe6 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Massachusetts v. Sheppard.json
- **problem:** The stored pin-989 quote is not an opinion quote. It reproduces content-page material beginning with the page header and background/rule prose, while the lake itself flags quote_fidelity as mismatch and the opinion text at 989-990 contains a different passage.
- **verbatim:** to disbelieve a judge who has just advised him, by word and by action, that the warrant he possesses authorizes him to conduct the search he has requested.
- **tally:** codex-A=stands: The reviewed payload quote begins with '--- # Massachusetts v. Sheppard' and includes content-page headings, not the Supreme Court opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; I do not raise a support or quote-fidelity defect.  |  opus=stands-modified: The actual ^pin-989 block quote matches the cached opinion verbatim; the '*990' star break falls between 'is required' and 'to disbelieve a judge', so the quote genuinely spans pages 989-990 and the…
- **proposed_fix:** Replace pin-989 with the actual opinion passage supporting the inline quote, or remove the pinpoint quote until it can be regenerated from text/Massachusetts v. Sheppard__10a09d.txt.

### F-S9-PR-feb953efa9 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Massiah v. United States.json
- **problem:** The pin-206 lake/inventory quote is not an opinion quote; it is a rendered page/header fragment and the lake itself marks quote_fidelity as mismatch with page and star_marker null.
- **verbatim:** We hold that the petitioner was denied the basic protections of that guarantee when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberat…
- **tally:** codex-A=stands: The content_page quote is present verbatim in the cached opinion text at the *206 marker.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual ^pin-206 block quote matches the cached opinion verbatim; the '*206' star marker immediately precedes the 'We hold that the petitioner was denied...' sentence, confirming the pincite '377…
- **proposed_fix:** Replace pin-206 with the actual page-206 Massiah holding sentence used on the content page, and set the pinpoint metadata to page/star marker 206.

### F-S9-PR-51caddabbd · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Mathews v. United States.json
- **problem:** The pin-62 payload/lake quote is not an opinion quote; it is page markdown text beginning with the generated case page header and ending at '## Rule Yes.'. The lake record itself marks quote_fidelity as mismatch.
- **verbatim:** We hold that even if the defendant denies one or more elements of the crime
- **tally:** codex-A=stands: The disclosed text file contains the Mathews opinion and the actual holding sentence at page *62.  |  codex-B=refuted: Quote fidelity is outside Lens B; no support or quotation finding is raised here.  |  opus=stands-modified: The actual ^pin-62 block quote matches the cached opinion verbatim; the holding 'We hold that even if the defendant denies one or more elements...' falls after the '*62' star marker and before the '*…
- **proposed_fix:** Replace pin-62's lake quote with the actual opinion sentence at star page *62 beginning 'We hold that even if the defendant denies one or more elements of the crime...' and update the pinpoint metada…

### F-S9-PR-1ebc7ba161 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/McNabb v. United States.json
- **problem:** pin-345's stored quote is page Markdown/front matter and case-summary prose, not a verbatim opinion quote and not the Rule quote marked by ^pin-345 on the built page.
- **verbatim:** --- # McNabb v. United States *318 U.S. 332 (1943)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
- **tally:** codex-A=stands: The payload/lake quote for pin-345 starts with the built page header and includes Background/Issue/Rule prose rather than the court's quoted language.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual pin-345 page quote is verbatim-present in the cached opinion; the page ellipsis ' . . . ' correctly omits 'Congress has not explicitly forbidden the use of evidence so procured. But', and…
- **proposed_fix:** Replace pin-345.quote with the actual opinion passage beginning "Plainly, a conviction resting on evidence secured through such a flagrant disregard..." and ending with the stultification sentence, p…

### F-S9-PR-6e3944f0b2 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/McNeil v. Wisconsin.json
- **problem:** The pin-175 quote is not a character-faithful opinion quote. It is harvested page/frontmatter text ending at '## Rule No.', while the cached opinion text at the claimed passage contains the offense-specific Sixth Amendment language. The lake record itself flags quote_fidelity as mismatch and gives…
- **verbatim:** Sixth Amendment right, however, is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced
- **tally:** codex-A=stands: The asserted pin quote begins with built-page material: '--- # McNeil v. Wisconsin *501 U.S. 171 (1991)* ...', not opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no currency or treatment defect is adjudicated for this row.  |  opus=stands-modified: The actual pin-175 page quote is verbatim-faithful to the cached opinion; the cached OCR drops the leading 'The' (paragraph starts 'Sixth Amendment right, however...'), which the page correctly resto…
- **proposed_fix:** Regenerate pin-175 from the cached opinion text at page label 175, set the page/pin to 175, and use the opinion passage rather than the built-page excerpt. Under the disclosed text, also remove the p…

### F-S9-PR-1d9bd62d12 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Messerschmidt v. Millender.json
- **problem:** The stored pin-547 quote is not a character-faithful quote from the opinion. It is harvested page prose spanning Background, Issue, and Rule text, with markdown headings and formatting, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** the fact that a neutral magistrate has issued a warrant authorizing the allegedly unconstitutional search or seizure does not end the inquiry into objective reasonableness.
- **tally:** codex-A=stands: The lake pinpoints entry for pin-547 stores page-authored prose beginning "and fired at her as she fled" rather than the opinion quotation attached to the pin.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual pin-547 page quote is verbatim-faithful to the cached slip opinion (dehyphenated lines 'the fact that / a neutral magistrate has issued a warrant authorizing the / allegedly unconstitution…
- **proposed_fix:** Replace pin-547's stored quote with the actual quoted sentence used on the page, or split the page prose from the verbatim quotation. The faithful quotation is: "the fact that a neutral magistrate ha…

### F-S9-PR-cf25f48669 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Michigan v. Fisher.json
- **problem:** pin-48 is not quote-faithful as framed: the lake pinpoint quote is a Markdown page excerpt rather than the opinion passage, the displayed quote alters the inner quotation marks, and the cited page 48 does not land on the quoted sentence in the cached opinion text.
- **verbatim:** Officers do not need ironclad proof of “a likely serious, life-threatening” injury to invoke the emergency aid exception.
- **tally:** codex-A=stands: The cached opinion text contains the sentence, but at the page 49 marker, not page 48.  |  codex-B=refuted: Quote fidelity is outside Lens B; I raise no support or quote-fidelity defect.  |  opus=stands-modified: The pin-48 quote 'Officers do not need ironclad proof of "a likely serious, life-threatening" injury to invoke the emergency aid exception.' matches the cached opinion verbatim; the payload's 'mismat…
- **proposed_fix:** Replace pin-48 with the exact opinion sentence and cite it to 558 U.S. at 49, or otherwise verify a reporter/slip pagination source that supports page 48. The exact text should preserve the opinion's…

