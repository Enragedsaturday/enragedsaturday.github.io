# P2 ESCALATE PACKET 05/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-09b9c06ba2 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Ciraolo.json
- **problem:** The reviewed lake pinpoint quote for pin-215 is not the opinion passage at 476 U.S. 215; it is a harvested fragment from the content page header/background/issue section and is itself marked quote_fidelity='mismatch'.
- **verbatim:** In an age where private and commercial flight in the public airways is routine, it is unreasonable for respondent to expect that his marijuana plants were constitutionally protected from being observ…
- **tally:** codex-A=stands: The payload quote begins with the content page front matter/header and ends at '## Rule', not with the Ciraolo opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B's charter; no currency or treatment-specific defect is raised on this row.  |  opus=stands-modified: The legal proposition survives: the content-page quote at pin-215 matches cached b279-6 verbatim and the *215 star-page is correct.
- **proposed_fix:** Replace pin-215's stored quote with the actual opinion passage at *215, and set the page/pin metadata to the 215 passage rather than the page-header harvest.

### F-S9-PR-9459cf743b · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Greenwood.json
- **problem:** The pin-40 payload/lake quote is not the opinion passage; it is a corrupted harvest of the content page header, background, issue, and rule heading.
- **verbatim:** Here, we conclude that respondents exposed their garbage to the public sufficiently to defeat their claim to Fourth Amendment protection.
- **tally:** codex-A=stands: The payload quote begins with the page title/frontmatter-style text rather than language from the opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The legal proposition survives: the content-page quote at pin-40 matches cached b98-5 verbatim and the *40 star-page is correct.
- **proposed_fix:** Replace the pin-40 quote with the actual page-40 opinion sentence: "Here, we conclude that respondents exposed their garbage to the public sufficiently to defeat their claim to Fourth Amendment prote…

### F-S9-PR-a4dd07938e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Hodari D..json
- **problem:** The reviewed pin-626 quote is not a verbatim opinion quote; it appears to splice the content page Issue sentence ending with the markdown heading '## Rule'.
- **verbatim:** The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a seizure occurs even though the subject does not yield. We hold that i…
- **tally:** codex-A=stands: The payload quote 'under the Fourth Amendment before any physical force is applied. ## Rule' is not a contiguous opinion passage.  |  codex-B=refuted: Lens B does not assess quote support or quote fidelity.  |  opus=stands-modified: The legal proposition survives: the content-page quote at pin-626 matches the cached opinion verbatim and the *626 star-page is correct.
- **proposed_fix:** Replace pin-626's lake quote with the actual page-626 rule quote: 'The narrow question before us is whether, with respect to a show of authority as with respect to application of physical force, a se…

### F-S9-PR-3c1e221832 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Prysock.json
- **problem:** pin-359 is not character-faithful as stored/rendered. The lake pinpoint quote captures a generated page block rather than the quoted opinion sentence, and the rendered page cites 451 U.S. at 359 even though the lake official citation is 453 U.S. 355.
- **verbatim:** This Court has never indicated that the “rigidity” of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona…
- **tally:** codex-A=stands: The disclosed opinion text contains the quoted sentence at the page-359 marker, but the lake pin-359 quote is a markdown page excerpt beginning with the title and background, not the source passage.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Quote 'This Court has never indicated that the "rigidity" of Miranda extends to the precise formulation of the warnings given a criminal defendant.' matches the cached opinion (para b401-5) verbatim;…
- **proposed_fix:** Replace pin-359 with the actual opinion sentence and cite it as 453 U.S. at 359; do not store the generated page header/background/rule block as the pinpoint quote.

### F-S9-PR-828d952522 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Prysock.json
- **problem:** pin-359a is not character-faithful to the cached opinion text. The page/lake quote omits the introductory phrase and uses 'talismanic', while the disclosed text reads 'talis-manic'. It also relies on Id. following a wrong 451 U.S. citation in the rendered page.
- **verbatim:** Quite the contrary, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself i…
- **tally:** codex-A=stands: The disclosed cached opinion text does not match the quote character-for-character.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Quote 'Miranda itself indicated that no talismanic incantation was required to satisfy its strictures.' matches the cached opinion (para b401-6) verbatim; the source's 'talis-manic' is a line-break h…
- **proposed_fix:** Either quote the cached text exactly or convert the sentence to a paraphrase. If retained as a quote, fix the preceding citation chain to 453 U.S. at 359.

### F-S9-PR-fe6a4e3dc6 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/City of Los Angeles v. Patel.json
- **problem:** The pinpoint quote is not from the Patel opinion at all; it is a captured chunk of the built content page/header/background/rule text.
- **verbatim:** The Court has held that absent consent, exigent circum- stances, or the like, in order for an administrative search to be constitutional, the subject of the search must be afforded an opportunity to…
- **tally:** codex-A=stands: The asserted quote begins with markdown/front-matter content from the built page, not language from the cached Supreme Court opinion.  |  codex-B=refuted: Quote fidelity is outside lens B; no support or quote-fidelity finding is raised here.  |  opus=stands-modified: Content-page ^pin-op10 quote matches the cached opinion verbatim (dropping the 'The Court has held that' lead-in) and its pincite slip op. 10 is correct.
- **proposed_fix:** Replace pin-op10 with the actual slip-opinion page 10 passage about administrative searches and precompliance review.

### F-S9-PR-d2bcd90e7e · quote-fidelity · sev=medium · needs_cl=false · quorum=1/3
- **object:** _overhaul2/lake/cases/City of Ontario v. Quon.json
- **problem:** Content ^pin-761 pincites the quote 'Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the O'Connor plurality.' to '560 U.S. at 761', but the cached opinion places that sentence on page 7…
- **verbatim:** Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the O'Connor plurality.
- **tally:** codex-A=MISSING  |  codex-B=MISSING  |  opus=stands: The quote WORDS are verbatim-faithful, but the page pincite is wrong by three pages (quoted sentence is on 764, cited as 761).
- **proposed_fix:** Change the pincite from '560 U.S. at 761' to '560 U.S. at 764'.

### F-S9-PR-feddf80687 · quote-fidelity · sev=high · needs_cl=false · quorum=2/3
- **object:** _overhaul2/lake/cases/City of Ontario v. Quon.json
- **problem:** The pin-761 payload/lake quote is not a judicial quotation at all; it is a harvested chunk of the generated content page. The real quoted sentence appears in the opinion text at 560 U.S. 764, not 560 U.S. 761, and the content-page rendering also changes O’Connor to straight-apostrophe markdown insi…
- **verbatim:** Because the search was motivated by a legitimate work-related purpose, and because it was not excessive in scope, the search was reasonable under the approach of the
- **tally:** codex-A=stands: The disclosed lake pinpoint for pin-761 begins with generated page material, not opinion text.  |  codex-B=refuted: Quote-fidelity is outside Lens B; no independent treatment or currency defect is specific to this pin assertion.  |  opus=MISSING
- **proposed_fix:** Replace pin-761 with the actual opinion sentence beginning 'Because the search was motivated by a legitimate work-related purpose...' and update the content citation/pin from 560 U.S. at 761 to 560 U…

### F-S9-PR-e54352e499 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/City of Tahlequah v. Bond.json
- **problem:** The pin-op3 payload quote is not opinion text; it splices content-page summary text and markdown headings, and the lake record itself marks this pinpoint as quote_fidelity=mismatch.
- **verbatim:** We have repeatedly told courts not to define clearly es- tablished law at too high a level of generality.
- **tally:** codex-A=stands: The disclosed opinion text contains the quoted high-generality rule on slip page 3.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content ^pin-op3 quote matches the cached per curiam verbatim and is on slip op. page 3; pincite correct.
- **proposed_fix:** Replace the pin-op3 quote with the actual slip-opinion sentence: We have repeatedly told courts not to define clearly established law at too high a level of generality.

### F-S9-PR-775f3ed506 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Collins v. Virginia.json
- **problem:** The lake pinpoint quote for pin-op14 is not the opinion passage at slip op. 14; it is a harvested chunk of the built content page header/background/issue text ending at '## Rule No.'. That is not character-faithful to the cited opinion passage.
- **verbatim:** For the foregoing reasons, we conclude that the automo- bile exception does not permit an officer without a warrant to enter a home or its curtilage in order to search a vehicle therein.
- **tally:** codex-A=stands: The lake pinpoints[].quote begins with '--- # Collins v. Virginia' and includes page prose, not the opinion text.  |  codex-B=refuted: Quote-fidelity and support findings are outside Lens B under the task instructions.  |  opus=stands-modified: Content ^pin-op14 quote matches the cached Opinion of the Court verbatim (Part IV) and is on slip op. page 14; pincite correct.
- **proposed_fix:** Replace pin-op14's lake pinpoints[].quote with the actual slip-opinion passage supporting the page quote, and mark fidelity only after checking against the disclosed opinion text or an explicitly nor…

### F-S9-PR-20eff56c8c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Colorado v. Bertine.json
- **problem:** The pin-374 payload is not an opinion quote; it is a generated page/header/background/rule excerpt. The actual page-374 opinion passage is the inventory-procedure rule quoted in content_page.md, not the payload text.
- **verbatim:** reasonable police regulations relating to inventory procedures administered in good faith satisfy the Fourth Amendment, even though courts might as a matter of hindsight be able to devise equally rea…
- **tally:** codex-A=stands: The lake pin-374 quote begins with the content page front matter/header, not with text from the opinion.  |  codex-B=refuted: Quote fidelity is outside lens B, so I make no support or quote-fidelity finding.  |  opus=stands-modified: The stored pinpoint quote is page markdown (frontmatter delimiter + header + Background/Issue/Rule prose), not opinion text, so as a quotation it is not faithful.
- **proposed_fix:** Replace the pin-374 lake quote with the actual opinion passage at 479 U.S. 367, 374 beginning with reasonable police regulations, and set the pinpoint page/status accordingly.

### F-S9-PR-c3c880ea25 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Colorado v. Connelly.json
- **problem:** pin-167's stored quote is not character-faithful to the opinion text; it captures issue/rule page text instead of the page-167 holding sentence, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** coercive police activity is a necessary predicate to the finding that a confession is not “voluntary”
- **tally:** codex-A=stands: The disclosed text contains the holding sentence on page 167, while the inventory/lake quote is a splice of the Issue and Rule prose from the built page.  |  codex-B=refuted: Quote fidelity is outside Lens B; no currency or treatment defect is created by this pinpoint row.  |  opus=stands-modified: The stored pinpoint quote is page markdown (tail of the Issue plus the Rule header), not opinion text, so as a quotation it is not faithful.
- **proposed_fix:** Regenerate pin-167 from the actual page-167 holding sentence beginning with 'We hold that coercive police activity...' and preserve the source quotation marks or apply a documented normalization poli…

### F-S9-PR-61da105410 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Colorado v. Spring.json
- **problem:** The disclosed pin-577 quote is not the opinion passage supporting the rendered quotation; it is a markdown excerpt from the built page, and the lake record itself marks quote_fidelity as mismatch. The actual opinion passage at page 577 begins with the Court's holding language.
- **verbatim:** Accordingly, we hold that a suspect’s awareness of all the possible subjects of questioning in advance of interrogation is not relevant
- **tally:** codex-A=stands: The lake pin quote starts with page markdown rather than opinion text: "--- # Colorado v. Spring *479 U.S. 564 (1987)*".  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The stored pinpoint quote is page markdown (frontmatter + header + Background/Issue/Rule prose), not opinion text, so as a quotation it is not faithful.
- **proposed_fix:** Replace pin-577's stored quote with the actual page 577 opinion text beginning "Accordingly, we hold that a suspect’s awareness..." and set the pin/page metadata to the 577 passage. Also make the ren…

### F-S9-PR-56723723bb · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/County of Riverside v. McLaughlin.json
- **problem:** pin-56's stored quote is not the page-56 rule passage; it appears to splice the content-page Issue/Rule text and heading rather than quote the opinion.
- **verbatim:** we believe that a jurisdiction that provides judicial determinations of probable cause within 48 hours of arrest will, as a general matter, comply with the promptness requirement
- **tally:** codex-A=stands: The lake pin itself flags quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual ^pin-56 content-page quotation is verbatim in the cached opinion ('within 48 hours of arrest will, as a general matter, comply with the promptness requirement of Gerstein').
- **proposed_fix:** Replace pin-56 with the actual page-56 passage supporting the 48-hour rule, or regenerate the pin from the opinion text.

### F-S9-PR-b720590dbd · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/County of Sacramento v. Lewis.json
- **problem:** The pin-836 quote payload is not a character-faithful opinion quote; it is a harvested block of built-page metadata/background/rule text. The lake itself marks this pinpoint as quote_fidelity=mismatch, slip-only, and without a star marker.
- **verbatim:** We answer no, and hold that in such circumstances only a purpose to cause harm unrelated to the legitimate object of arrest will satisfy
- **tally:** codex-A=stands: The payload begins with built-page text, including '--- # County of Sacramento v. Lewis', rather than with opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B, so no quote/support defect is raised.  |  opus=stands-modified: The actual ^pin-836 content-page quotation is verbatim in the cached opinion ('We answer no, and hold that in such circumstances only a purpose to cause harm unrelated to the legitimate object of arr…
- **proposed_fix:** Replace pin-836's quote payload with the actual page-836 sentence quoted in content_page.md and verify it against the opinion text with star_marker 836.

### F-S9-PR-fca1a0d449 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Cupp v. Murphy.json
- **problem:** pin-296 is not a faithful opinion quote. The harvested lake quote is a collapsed excerpt from the built page, not the opinion, and the content pin also conflates a page *295 quote with a page *296 quote under a single 412 U.S. at 296 pincite. The first quoted phrase also drops source punctuation.
- **verbatim:** the search of the respondent's fingernails went beyond mere "physical characteristics. . . constantly exposed to the public,"
- **tally:** codex-A=stands: The lake record itself marks pin-296 quote_fidelity as mismatch and gives no star_marker, position, or fragment.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual ^pin-296 content-page quotations are verbatim in the cached opinion: 'in these circumstances, justified the police in subjecting him to the very limited search necessary to preserve the hi…
- **proposed_fix:** Split or repair the pin. Cite the physical-characteristics quote to 412 U.S. at 295 using the exact punctuation, and cite the Chimel-rationale sentence separately to 412 U.S. at 296.

### F-S9-PR-130f219fc7 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/District of Columbia v. Wesby.json
- **problem:** The harvested pinpoint quote is not an opinion quote; it is a corrupt run-on fragment from the built page, including Background, Issue, and Rule text.
- **verbatim:** In concluding otherwise, the panel majority engaged in an “excessively technical dissection” of the factors support- ing probable cause.
- **tally:** codex-A=stands: The payload quote includes Markdown section text from content_page.md, not a contiguous passage from the opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The disclosed quote is verbatim content-page Markdown (contains '## Issue'/'## Rule'), i.e., an S8 harvest artifact, not a fabricated opinion quotation.
- **proposed_fix:** Replace the pin-op11 quote with the actual slip-opinion passage supporting the citation.

### F-S9-PR-6df0103333 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Donovan v. Dewey.json
- **problem:** pin-598's lake quote is not an opinion quote; it is corrupted page/content boilerplate and does not appear in the cached opinion text.
- **verbatim:** The greater latitude to conduct warrantless inspections of commercial property reflects the fact that the expectation of privacy that the owner of commercial property enjoys in such property differs…
- **tally:** codex-A=stands: The lake pinpoints entry itself marks pin-598 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The disclosed quote is verbatim content-page Markdown (title/header + '## Rule'), an S8 harvest artifact, not an opinion quotation.
- **proposed_fix:** Replace pin-598 with the actual 598-599 opinion passage beginning 'The greater latitude to conduct warrantless inspections...' and set the pinpoint metadata to the real page range.

### F-S9-PR-aeeebcc253 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Dow Chemical Co. v. United States.json
- **problem:** The pin-239 quote is not character-faithful opinion text; it stitches content-page prose and a heading into the purported quote. The lake record itself marks this pin quote_fidelity=mismatch, pinpoint_status=slip-only, and star_marker=null.
- **verbatim:** We conclude that the open areas of an industrial plant complex with numerous plant structures spread over an area of 2,000 acres are not analogous to the “curtilage” of a dwelling for purposes of aer…
- **tally:** codex-A=stands: The payload quote contains '## Rule No.' and content-page wording, not the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The disclosed quote contains '## Rule' Markdown, so it is an S8 harvest artifact of authored page prose, not an opinion quotation.
- **proposed_fix:** Regenerate pin-239 from the actual page-239 opinion passage, anchoring either the full 'We conclude...' sentence or the quoted 'such an industrial complex...' clause.

### F-S9-PR-2767214c3e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Doyle v. Ohio.json
- **problem:** pin-617's stored quote is an over-harvest from the built page, not a character-faithful opinion quote; it begins with page markdown/frontmatter-like text and includes page prose rather than the U.S. Reports passage.
- **verbatim:** Silence in the wake of these warnings may be nothing more than the arrestee's exercise of these <i>Miranda</i> rights. Thus, every post-arrest silence is insolubly ambiguous because of what the State…
- **tally:** codex-A=stands: The lake record itself marks pin-617 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The disclosed quote contains '## Rule' Markdown and the case header, so it is an S8 harvest artifact, not an opinion quotation.
- **proposed_fix:** Replace pin-617 with the actual opinion passage supporting the insolubly ambiguous point.

### F-S9-PR-6ac7a21e01 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Edwards v. Arizona.json
- **problem:** pin-484's payload quote is not an opinion quotation; it is page/header/background/rule prose and does not match the cited opinion passage at 451 U.S. 484.
- **verbatim:** when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-in…
- **tally:** codex-A=stands: The lake record itself marks pin-484 quote_fidelity as 'mismatch'.  |  codex-B=refuted: Quote-fidelity is outside lens B, so no support or quote-fidelity finding is made.  |  opus=stands-modified: The actual ^pin-484 quote on the content page ('[W]hen an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by s…
- **proposed_fix:** Replace pin-484 with the actual 484 passage beginning with the Court's holding on waiver after police-initiated custodial interrogation, and set the pinpoint to page 484.

### F-S9-PR-0ca0ae240d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Escobedo v. Illinois.json
- **problem:** pin-490's stored pinpoint quote is not a quote from the Escobedo opinion passage. It is harvested page markdown/header/background text, while the actual 490-491 passage begins with the Court's holding paragraph.
- **verbatim:** <p>We hold, therefore, that where, as here, the investigation is no longer a general inquiry into an unsolved crime but has begun to focus on a particular suspect, the suspect <span class="star-pagin…
- **tally:** codex-A=stands: The disclosed lake pinpoint quote starts with page content, not opinion text: it includes the markdown title/header/background/issue material.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The actual ^pin-490 quote on the content page is verbatim-faithful to the inlined opinion: all retained words match the source exactly, and the two ' ... ' spans are legitimate ellipsis elisions of '…
- **proposed_fix:** Replace lake pinpoints[pin-490].quote with the actual holding paragraph from text/Escobedo v. Illinois__a3ccd8.txt at the 490-491 passage, and rebuild the page so the pin points to that source passag…

### F-S9-PR-395bcb5628 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Fare v. Michael C.json
- **problem:** pin-724's stored quote is not an opinion passage; it is a scraped excerpt of the built page/header, and the lake marks it as a mismatch with no star marker. It cannot verify the page's quoted Rule text at that pin.
- **verbatim:** --- # Fare v. Michael C. *442 U.S. 707 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
- **tally:** codex-A=stands: The pin-724 payload says quote_fidelity is mismatch, pinpoint_status is slip-only, and star_marker is null.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Both quoted passages verify verbatim in the disclosed opinion, so the substance/holding is faithful; the defect is pincite precision, not fabrication.
- **proposed_fix:** Replace pin-724 with the actual opinion passage(s), or split the pin: the attorney-role quote appears in the opinion before the *723 marker, while the 'Nor do we believe...' passage spans the *723/*7…

### F-S9-PR-c71e4a2aac · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Florida v. Jardines.json
- **problem:** The stored pin-6 quote is not a faithful opinion quote; it stitches the page's Issue/Rule prose, including markdown heading text, rather than the Supreme Court passage supporting the pin.
- **verbatim:** ## Rule Yes. Bringing a drug dog onto the curtilage
- **tally:** codex-A=stands: The challenged pin-6 quote includes markdown text from content_page.md rather than opinion language.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content page's actual pin-6 quote matches the cached slip opinion verbatim.
- **proposed_fix:** Replace lake pinpoints[].quote for pin-6 with the actual opinion passage beginning with the officers gathering information in Jardines's curtilage, or treat the current rule sentence as paraphrase ra…

### F-S9-PR-3f19ee3ded · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Florida v. Jimeno.json
- **problem:** The asserted pinpoint quote is generated page/front-matter prose beginning with '--- # Florida v. Jimeno', not the Jimeno opinion passage tied to 500 U.S. at 251. It is not character-faithful to the cached opinion text and the lake marks it as mismatch.
- **verbatim:** The standard for measuring the scope of a suspect’s consent under the Fourth Amendment is that of “objective” reasonableness—
- **tally:** codex-A=stands: The lake/payload quote is a content-page excerpt, not a verbatim extract from the cached opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content page's actual pin-251 quote matches the cached HTML opinion verbatim.
- **proposed_fix:** Replace pin-251's stored quote with the exact objective-reasonableness sentence from the opinion and remove the generated page prose from pinpoints[].quote.

