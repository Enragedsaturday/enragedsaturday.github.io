# P2 ESCALATE PACKET 08/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-98a01f1b50 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Mincey v. Arizona.json
- **problem:** The pin-392 payload/lake pinpoint quote is not the opinion quote at page 392; it is generated page prose spanning the Issue/Rule text and the lake itself marks it quote_fidelity "mismatch" with no star marker.
- **verbatim:** the Fourth Amendment does not bar police officers from making warrantless entries and searches when they reasonably believe that a person within is in need of immediate aid.
- **tally:** codex-A=stands: The payload quote beginning "exception permitting a warrantless search" does not appear in the cached opinion text as an opinion passage.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Rendered page pincite is sound: the actual pin-392 quote ('...in need of immediate aid.' - 437 U.S. at 392) appears verbatim in the cached opinion on page 392, so the legal proposition survives.
- **proposed_fix:** Replace pin-392's lake/payload quote with the actual quoted opinion sentence used on the content page and present in the opinion text; set the pinpoint to star page 392 if validated.

### F-S9-PR-f6de7c91ca · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Minnesota v. Carter.json
- **problem:** The lake pinpoint quote for pin-90 is not an opinion quote; it is a harvested content-page/frontmatter excerpt ending at '## Rule No.' The disclosed opinion text at page 90 contains the actual quoted sentence, so the quote_fidelity assertion as framed fails.
- **verbatim:** Thus, an overnight guest in a home may claim the protection of the Fourth Amendment, but one who is merely present with the consent of the householder may not.
- **tally:** codex-A=stands: The visible page quote is found verbatim in the cached opinion text at the page-90 passage.  |  codex-B=refuted: Quote fidelity is outside lens B, so I do not raise a support or quote-fidelity defect.  |  opus=stands-modified: Rendered page pincite is sound: the actual pin-90 quote appears verbatim in the cached opinion on page 90 (just past the *90 star marker), so the proposition survives.
- **proposed_fix:** Replace pin-90's quote with the actual page-90 sentence and set the pinpoint to page/star marker 90; do not use the content-page excerpt as the lake pinpoint quote.

### F-S9-PR-9e1e94f4b0 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Minnesota v. Dickerson.json
- **problem:** pin-375 is not character-faithful as framed. The lake pinpoint quote is page/header text rather than the opinion passage, and the lake itself marks quote_fidelity as mismatch. The displayed Rule quote also normalizes the opinion's curly apostrophes to straight apostrophes, so it is not literal char…
- **verbatim:** --- # Minnesota v. Dickerson *508 U.S. 366 (1993)* · U.S. Supreme Court · **Binding — SCOTUS**
- **tally:** codex-A=stands: The stored pinpoint quote begins with page/header material, not the opinion text.  |  codex-B=refuted: Quote fidelity and support are outside lens B, so no quote/support defect is raised here.  |  opus=stands-modified: Rendered page pincite is sound: the actual pin-375 quote appears verbatim in the cached opinion spanning pages 375-376 (page label 376 falls mid-sentence), so the proposition survives.
- **proposed_fix:** Replace pin-375 with the exact 508 U.S. 375-376 passage from text/Minnesota v. Dickerson__ce89db.txt and either preserve punctuation exactly or mark the quote as normalized rather than verbatim.

### F-S9-PR-8cfa90eb6e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Muehler v. Mena.json
- **problem:** pin-98 is not a faithful opinion quote. The stored pinpoint quote is harvested page/frontmatter prose, has no star marker, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** An officer's authority to detain incident to a search is categorical; it does not depend on the "quantum of proof
- **tally:** codex-A=stands: The disclosed lake record for pin-98 stores a block beginning with the content page title and background, not the Supreme Court opinion passage.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored pin-98 quote is verbatim the page's frontmatter/Background/Issue/Rule text — a slip-only extraction artifact, not an opinion quote (matches lake self-flag mismatch).
- **proposed_fix:** Replace pin-98 with the exact opinion passage at star page 98 and set star_marker to 98; preserve the opinion's internal double quotation marks or avoid presenting the sentence as a strict character-…

### F-S9-PR-a44214977c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Mullenix v. Luna.json
- **problem:** pin-12.quote is not an opinion quotation. It is a harvested chunk of the built page, beginning with the page header and continuing through Background, Issue, and Rule summary text.
- **verbatim:** “We have repeatedly told courts . . . not to define clearly established law at a high level of generality.”
- **tally:** codex-A=stands: The lake pinpoint quote starts with '--- # Mullenix v. Luna' and includes content-page summary prose, which is not in the cached opinion text.  |  codex-B=refuted: Lens B is limited to currency and treatment; this quote_fidelity row does not create an independent treatment defect.  |  opus=stands-modified: Stored pin-12 quote is verbatim the page preamble text, not an opinion quote (matches lake self-flag mismatch).
- **proposed_fix:** Replace pin-12.quote with the exact opinion text supporting the visible rule quote; do not store the rendered page summary as the authority pinpoint quote.

### F-S9-PR-e8ec921db3 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Murray v. United States.json
- **problem:** pin-542 stores built-page title/background/rule prose as the quote instead of the cited opinion passage, so the payload quote is not character-faithful to the disclosed opinion text.
- **verbatim:** The ultimate question, therefore, is whether the search pursuant to warrant was in fact a genuinely independent source of the information and tangible evidence at issue here.
- **tally:** codex-A=stands: The row payload for pin-542 begins with the generated page header and background, not with language from the Murray opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored pin-542 quote is verbatim the page preamble text, not an opinion quote (matches lake self-flag mismatch).
- **proposed_fix:** Replace pin-542's quote with the actual 487 U.S. at 542 sentence and set the pinpoint metadata to the page 542 passage.

### F-S9-PR-8e7b116988 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/NASA v. FLRA.json
- **problem:** The pin-233 quote is not a character-faithful opinion excerpt; it is a stitched content-page artifact spanning the Issue text and the Rule heading, and the lake record itself marks quote_fidelity as mismatch.
- **verbatim:** within the meaning of 5 U.S.C. § 7114(a)(2)(B), so that a NASA employee's statutory right to union representation at an investigatory examination may be invoked. ## Rule The statute grants the repres…
- **tally:** codex-A=stands: The payload quote contains '## Rule', which is content_page markdown, not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored pin-233 quote is verbatim the page's Issue/Rule preamble, not an opinion quote (matches lake self-flag mismatch).
- **proposed_fix:** Regenerate pin-233 from the actual statutory block at 527 U.S. at 233, or convert the rule statement to a paraphrase without quotation marks.

### F-S9-PR-8e8dd02612 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Neil v. Biggers.json
- **problem:** pin-199's stored quote is not an opinion quote; it is built-page front matter and summary prose. The actual cited passage is different, and the lake itself flags this pinpoint as quote_fidelity=mismatch with no page, star marker, or position.
- **verbatim:** We turn, then, to the central question, whether under the "totality of the circumstances" the identification was reliable even though the confrontation procedure was suggestive.
- **tally:** codex-A=stands: The inventory/lake quote begins with page markup and summary text, not language from the Neil opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Displayed content quote at ^pin-199 matches the opinion verbatim at *199 (bracketed cap/insertion only); pincite '409 U.S. at 199' correct.
- **proposed_fix:** Replace pin-199 with a character-faithful quote from the opinion text, or convert the sentence to paraphrase without quotation marks.

### F-S9-PR-5c7738775f · quote-fidelity · sev=high · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/Nix v. Williams.json
- **problem:** pin-444 is not a faithful pinpoint quote. The lake pinpoint itself is flagged quote_fidelity='mismatch', has page=null/slip-only, and contains page-authored background/issue/rule prose rather than the opinion passage at 467 U.S. 444.
- **verbatim:** the information ultimately or inevitably would have been discovered by lawful means — here the volunteers’ search—
- **tally:** codex-A=stands: The disclosed lake pinpoint for pin-444 has quote_fidelity='mismatch' and no page value.  |  codex-B=refuted: This row is quote_fidelity, outside Lens B's treatment/currency charter.  |  opus=stands-modified: Displayed content quote at ^pin-444 matches the opinion at *444 (a fair mid-quote ellipsis replaces 'here the volunteers' search'); pincite '467 U.S. at 444' correct.
- **proposed_fix:** Replace pin-444 with the actual page 444 opinion passage supporting the rule and set page to 444, or remove the pinpoint until a verified quote/pin can be supplied.

### F-S9-PR-4bc8ee5794 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Oliver v. United States.json
- **problem:** The quote truncates the opinion sentence and changes it into a complete sentence without ellipsis; the opinion says the public is not effectively barred from viewing open fields "in rural areas."
- **verbatim:** It is not generally true that fences or “No Trespassing” signs effectively bar the public from viewing open fields in rural areas.
- **tally:** codex-A=stands: The lake pinpoint itself marks quote_fidelity as mismatch.  |  codex-B=refuted: Quote fidelity is outside lens B; no treatment or currency defect is attached to this pinpoint row.  |  opus=stands-modified: All words shown are verbatim from the opinion up to 'open fields'.
- **proposed_fix:** Use the full sentence: "It is not generally true that fences or “No Trespassing” signs effectively bar the public from viewing open fields in rural areas."

### F-S9-PR-e08f724d5d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Orozco v. Texas.json
- **problem:** The pin-326 quote in the lake/inventory is not a verbatim opinion quote; it concatenates page prose and markdown headings, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** We disagree and hold that the use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in *Mi…
- **tally:** codex-A=stands: The stored quote begins with 'Without any Miranda warnings' and continues through '## Issue' and '## Rule Yes.', which are not verbatim opinion language.  |  codex-B=refuted: This row is a quote-fidelity assertion for pin-326, not a treatment or currency assertion.  |  opus=stands-modified: The page's rendered ^pin-326 quote ('We disagree and hold ... as construed in Miranda.') matches the cached opinion verbatim and sits after the '*326' star marker, so the pincite '394 U.S. at 326' is…
- **proposed_fix:** Replace pin-326 with the actual 394 U.S. at 326 holding sentence or remove this stored quote if it is only generated summary prose.

### F-S9-PR-4b1b139a3f · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Patterson v. Illinois.json
- **problem:** The pin-296 quote stored in the lake/inventory is not a faithful opinion quotation; it is harvested page/header/background text, while the lake marks it as mismatch with page null and slip-only status.
- **verbatim:** As a general matter, then, an accused who is admonished with the warnings prescribed by this Court
- **tally:** codex-A=stands: The lake pinpoint quote begins with page metadata/header content rather than the opinion passage.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The page's ^pin-296 quote matches the opinion verbatim (the page's ' . . . ' correctly elides the internal '384 U. S., at 479' cite) and is on page 296, so pincite '487 U.S. at 296' is correct.
- **proposed_fix:** Replace pin-296's stored quote with the actual opinion passage at 487 U.S. 296 and set page to 296. Preserve the displayed rule quote only with a clear ellipsis for the omitted Miranda citation.

### F-S9-PR-c1a611f7d6 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Payton v. New York.json
- **problem:** pin-576's stored quote is not an opinion quote; it is harvested content-page Markdown/frontmatter and page prose. The actual opinion passage at *576 supports the displayed rule quote, but the lake pinpoint quote itself is not quote-faithful.
- **verbatim:** --- # Payton v. New York *445 U.S. 573 (1980)*
- **tally:** codex-A=stands: The lake pin-576 quote begins with content-page material rather than text from the Payton opinion.  |  codex-B=refuted: Quote fidelity is outside lens B, so no support or quote-fidelity defect is raised.  |  opus=stands-modified: The page's ^pin-576 quotation matches the opinion verbatim and sits on page 576 (right after the '*576' star), so pincite '445 U.S. at 576' is correct.
- **proposed_fix:** Replace pin-576's quote with the actual quoted opinion text: "prohibits the police from making a warrantless and nonconsensual entry into a suspect's home in order to make a routine felony arrest." V…

### F-S9-PR-426a6479dc · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pearson v. Callahan.json
- **problem:** The stored pin-236 quote is not a character-faithful excerpt from the opinion. It is a harvested page fragment containing Markdown headings/wiki links and ending before the actual Rule quote, while the opinion passage for the rule begins with different text.
- **verbatim:** On reconsidering the procedure required in Saucier, we conclude that, while the sequence set forth there is often appropriate
- **tally:** codex-A=stands: The lake pinpoint quote begins with page/background text: 'theory). Callahan sued under § 1983...' and includes '## Issue' and '## Rule No.', which are not opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; I raise no support or quote-fidelity finding.  |  opus=stands-modified: Content-page ^pin-236 quote matches slip-op Part III verbatim (allowing line-break hyphenation 'manda-tory'/'discre-tion').
- **proposed_fix:** Replace pin-236's quote with the actual opinion passage beginning 'On reconsidering the procedure required in Saucier...' and remove Markdown styling from inside any verbatim quote, or mark the page…

### F-S9-PR-a7465c9b6d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pembaur v. City of Cincinnati.json
- **problem:** pin-483's stored quote is not a character-faithful opinion excerpt; it is generated page prose with Markdown headings, and the lake record itself marks quote_fidelity as mismatch.
- **verbatim:** We hold that municipal liability under §1983 attaches where — and only where — a deliberate choice to follow a course of action is made from among various alternatives by the official or officials re…
- **tally:** codex-A=stands: The disclosed lake pinpoint quote begins 'the witnesses. The deputies chopped down the door...' and includes '## Issue' and '## Rule', which are content-page text, not the opinion passage.  |  codex-B=refuted: This row presents a quote-fidelity assertion, not a current-law or treatment assertion.  |  opus=stands-modified: Content-page ^pin-483 quote ('municipal liability under § 1983 attaches where — and only where — ...subject matter in question.') matches the opinion verbatim.
- **proposed_fix:** Replace lake.pinpoints[].quote for pin-483 with the actual page 483-484 passage beginning with the Court's 'We hold that municipal liability under §1983 attaches...' sentence, or remove the pin until…

### F-S9-PR-b3f7dbab2e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pennsylvania Board of Probation and Parole v. Scott.json
- **problem:** The harvested pin-364 quote is not character-faithful to the disclosed opinion text and includes page-content spillover rather than the pinned holding sentence.
- **verbatim:** We therefore hold that the federal exclusionary rule does not bar the introduction at parole revocation hearings of evidence seized in violation of parolees’ Fourth Amendment rights.
- **tally:** codex-A=stands: The lake pinpoint quote reads: 'because the criminal-trial exclusionary rule already deters unconstitutional searches. The social costs of excluding reliable evidence — letting violators escape revoc…  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Displayed content quote at ^pin-364 matches the opinion verbatim on star page *364; pincite '524 U.S. at 364' correct.
- **proposed_fix:** Replace pin-364 with the exact page-364 holding sentence and remove the harvested markdown heading spillover.

### F-S9-PR-3c6ad3813e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pennsylvania v. Bruder.json
- **problem:** pin-10's stored quotation is a harvested content-page fragment, not a character-faithful quotation from the Bruder opinion text.
- **verbatim:** ## Background Officer Shallis observed Bruder driving erratically
- **tally:** codex-A=stands: The lake pinpoint itself marks pin-10 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content-page ^pin-10 quote (contrary-to-Berkemer; 'noncoercive aspect of ordinary traffic stops...not “in custody” for the purposes of Miranda'; 'he was not entitled to a recitation...admissible') is…
- **proposed_fix:** Regenerate pin-10 from the actual page-10 opinion passage, or convert it to a non-verbatim support citation rather than a quote pinpoint.

### F-S9-PR-e35f4b371e · quote-fidelity · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pennsylvania v. Bruder.json
- **problem:** pin-11 quotes the operative sentence but omits the opening word from the opinion sentence without an ellipsis.
- **verbatim:** Accordingly,
- **tally:** codex-A=stands-modified: The lake pinpoint marks pin-11 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Captured quote '*Berkemer*'s rule, that ordinary traffic stops do not involve custody for purposes of *Miranda*, governs this case.' matches the opinion verbatim (opinion adds only leading 'According…
- **proposed_fix:** Change the quote to include the introductory word, or mark the omission with an ellipsis before Berkemer's rule.

### F-S9-PR-168315ae1a · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Pennsylvania v. Labron.json
- **problem:** pin-940 is not a verified opinion quote. The harvested quote is page/header/background/issue/rule material, and the lake record marks the pinpoint as a mismatch with no star marker.
- **verbatim:** "quote_fidelity": "mismatch"
- **tally:** codex-A=stands: The disclosed lake pinpoint for pin-940 expressly reports quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content-page ^pin-940 quote ('If a car is readily mobile and probable cause exists to believe it contains contraband, the Fourth Amendment thus permits police to search the vehicle without more.') ma…
- **proposed_fix:** Replace pin-940 with a verified quote from the opinion text at star page 940, or remove the quote pinpoint from this prose block.

### F-S9-PR-0d1fcbac97 · quote-fidelity · sev=low · needs_cl=false · quorum=1/3
- **object:** _overhaul2/lake/cases/Pennsylvania v. Muniz.json
- **problem:** Quote is verbatim-faithful, but the pincite '496 U.S. at 590-591' excludes the page where the quoted holding actually sits. In the cached opinion the 'slurring is nontestimonial' holding paragraph ('Under Schmerber and its progeny, we agree with the Commonwealth that any slurring of speech... does…
- **verbatim:** Under Schmerber and its progeny, we agree with the Commonwealth that any slurring of speech and other evidence of lack of muscular coordination revealed by Muniz's responses to Officer Hosterman's di…
- **tally:** codex-A=MISSING  |  codex-B=MISSING  |  opus=stands-modified: Quote text matches the cached opinion verbatim; '[A]ny' bracket and the two ' . . . ' ellipses (omitting 'to Officer Hosterman's direct questions' and 'like requiring him to reveal the physical prope…
- **proposed_fix:** Correct the pin-591 pincite from '590-591' to '592' (both quoted sentences are on p.592); update the Sources pinpoint list accordingly.

### F-S9-PR-bbd4083c24 · quote-fidelity · sev=high · needs_cl=false · quorum=2/3
- **object:** _overhaul2/lake/cases/Pennsylvania v. Muniz.json
- **problem:** pin-591's stored quote is not opinion text; it is page prose/Markdown captured across the Issue/Rule boundary. The actual slurring passage is elsewhere in the opinion, and the pin lacks a page, star marker, and position.
- **verbatim:** any slurring of speech
- **tally:** codex-A=stands: The payload quote contains Markdown heading material, which cannot be part of the Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=MISSING
- **proposed_fix:** Replace pin-591 with the actual opinion passage supporting slurring as nontestimonial and correct the official page/pin locator from the cached opinion text.

### F-S9-PR-f6b75769f9 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Preston v. United States.json
- **problem:** The pin-367 harvested quote is not a quotation from the opinion; it is a large slice of the generated content page/frontmatter and page prose.
- **verbatim:** Once an accused is under arrest and in custody
- **tally:** codex-A=stands: The payload quote begins with '--- # Preston v. United States', which is content_page markdown, not opinion text.  |  codex-B=refuted: This row is a quote_fidelity assertion; Lens B does not audit quote text, quote support, or pinpoint accuracy.  |  opus=stands-modified: The ACTUAL content-page pinpoint quote at ^pin-367 ('[o]nce an accused...simply not incident to the arrest.') is verbatim from the source (the sentence precedes the *368 marker, i.e., page 367), with…
- **proposed_fix:** Replace pin-367's lake quote with the actual opinion sentence used on the page and set the star marker to 367.

### F-S9-PR-a915a4e11f · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Rakas v. Illinois.json
- **problem:** pin-133's stored quote is not a character-faithful case quote; it is generated page/content markdown ending at the Rule heading. The lake itself flags quote_fidelity as mismatch and gives no star_marker.
- **verbatim:** "Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously <span class="star-pagination">*134</span> asserted."
- **tally:** codex-A=stands: The asserted quote begins with page front matter and section text, not the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The ACTUAL content-page pinpoint quote at ^pin-133 is verbatim from Rakas (the quote spans *133-*134, the word 'asserted' following the *134 marker), and is correctly attributed '(quoting Alderman v.…
- **proposed_fix:** Replace pin-133 with the actual Rakas passage at 439 U.S. 133-134, or remove the bad pinpoint metadata until a verified quote/locator is available.

### F-S9-PR-c7738a48f1 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Rawlings v. Kentucky.json
- **problem:** The reviewed pinpoint quote is not an opinion quote; it is a harvested markdown/content-page fragment beginning with the page header and ending before the actual quoted sentence.
- **verbatim:** the two inquiries merge into one: whether governmental officials violated any legitimate expectation of privacy held by petitioner.
- **tally:** codex-A=stands: The payload/lake quote begins with content-page material rather than text from the Rawlings opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The ACTUAL content-page pinpoint quote at ^pin-106 is verbatim from the source at page 106 (following the *106 star marker) and correctly pincited; the Blackmun concurrence independently confirms 'an…
- **proposed_fix:** Set pin-106's quote/pinpoint payload to the exact opinion sentence already displayed on the content page, not the harvested markdown fragment.

### F-S9-PR-bc7572b7de · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Samson v. California.json
- **problem:** pin-852's stored quote is not the actual quoted opinion passage tied to the content-page pin; it is harvested Background/Issue/Rule prose and lake itself marks quote_fidelity as mismatch with no position or fragment.
- **verbatim:** The extent and reach of these conditions clearly demonstrate that parolees like petitioner have severely diminished expectations of privacy by virtue of their status alone.
- **tally:** codex-A=stands: The cached opinion supports the visible content-page quote, not the payload's long Background/Issue/Rule string.  |  codex-B=refuted: Lens B does not attack quote/support fidelity.  |  opus=stands-modified: Displayed content quote at ^pin-852 matches the opinion verbatim ('...severely diminished expectations of privacy by virtue of their status alone.'); the assigned holding text is faithful.
- **proposed_fix:** Replace pin-852's quote with the actual opinion sentence beginning 'The extent and reach of these conditions...' and add a validated position or fragment.

