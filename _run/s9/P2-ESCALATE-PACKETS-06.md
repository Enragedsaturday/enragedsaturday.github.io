# P2 ESCALATE PACKET 06/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-6ec527744a · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Florida v. Meyers.json
- **problem:** pin-382's stored quote is not a character-faithful opinion quote; it is harvested page/editorial material beginning with the alias note and running through the page's Rule lead-in. The lake itself marks quote_fidelity as mismatch, and the cached opinion text at *382 contains different court languag…
- **verbatim:** In Michigan v. Thomas, 458 U. S. 259 (1982), we upheld a war-rantless search of an automobile
- **tally:** codex-A=stands: The asserted pin quote begins: "is carried as an `alias` so bare `[[Florida v. Myers]]` links resolve here", which is not judicial opinion text.  |  codex-B=refuted: This is a quote-fidelity row; Lens B does not assess verbatim support or quote accuracy.  |  opus=stands-modified: Content page's actual pin-382 quote matches the cached HTML opinion verbatim (war-rantless line-break hyphen removed).
- **proposed_fix:** Replace pin-382 with the actual quoted court passage supporting 466 U.S. at 382, or delete this faulty pinpoint and regenerate the quote harvest. Verify the page/star marker after replacement.

### F-S9-PR-4cc32b9043 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Florida v. Powell.json
- **problem:** The pin-62 lake pinpoint quote is not the application quotation attributed to 559 U.S. at 62; it captured the preceding citation sentence and the Application heading/page prose.
- **verbatim:** ## Application Reading the two statements together, the warning passed the test.
- **tally:** codex-A=stands: The lake record itself marks pin-62 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content page's actual pin-62 quote matches the Opinion-of-the-Court body verbatim (not the syllabus paraphrase).
- **proposed_fix:** Regenerate pin-62 so pinpoints[].quote is the actual opinion passage beginning with 'The first statement communicated that Powell could consult with a lawyer' and verify it against text/Florida v. Po…

### F-S9-PR-f8f91d8ce0 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Florida v. Powell.json
- **problem:** The pin-60 lake pinpoint quote is not the quoted Powell passage; it harvested content-page issue/rule prose around the marker, including a Markdown heading, rather than opinion text.
- **verbatim:** ## Rule Yes — warnings need not track any precise script.
- **tally:** codex-A=stands: The lake record itself marks pin-60 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content page's actual pin-60 quote matches the cached slip opinion verbatim.
- **proposed_fix:** Regenerate pin-60 so pinpoints[].quote is the actual opinion sentence beginning with 'The four warnings Miranda requires are invariable' and verify it against text/Florida v. Powell__c3ef95.txt.

### F-S9-PR-70755e88da · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Gooding v. United States.json
- **problem:** The pin quote is not an opinion quote; it is a concatenation of built-page summary prose and headings, while the actual page-439 opinion passage is statutory discussion. The lake pin also records quote_fidelity=mismatch.
- **verbatim:** That section provides that a warrant may be served
- **tally:** codex-A=stands: The payload quote includes content-page headings such as Issue and Rule, which are not part of the cached opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload quote is content-page prose ('## Issue ... ## Rule ...'), not text from the opinion — a harvester boundary artifact.
- **proposed_fix:** Replace pin-439 with an exact excerpt from the opinion's page-439 statutory passage, or remove quote treatment from the page-summary prose.

### F-S9-PR-58c61ed244 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Gouled v. United States.json
- **problem:** The pin-306 lake/inventory quote is not an opinion quote at all; it contains the built page frontmatter and narrative text, ending before the actual page-306 opinion passage. The lake also marks this pinpoint quote_fidelity as mismatch.
- **verbatim:** --- # Gouled v. United States
- **tally:** codex-A=stands: The recorded pin-306 quote starts with markdown page content rather than the opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no quote-fidelity finding is made.  |  opus=stands-modified: Payload quote is content-page frontmatter+prose ('--- # Gouled v. United States ... ## Rule ... The Court held that'), not opinion text — a harvester boundary artifact identical in shape to the Goodi…
- **proposed_fix:** Re-harvest pin-306 from the cached opinion at the *306 page marker so the pinpoint quote begins with the actual Gouled passage, not the content page markdown.

### F-S9-PR-132099506f · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Graham v. Barnette.json
- **problem:** The pin-op10 quote is not an opinion quote; it appears to splice content-page Issue/Rule text rather than the cited case text.
- **verbatim:** Now that Caniglia has made clear that “there is no overarching ‘community caretaking’ doctrine,” 141 S. Ct. at 1600 (Alito, J., concurring), our use of that label seems to be a category error.
- **tally:** codex-A=stands: The lake pinpoint itself marks pin-op10 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Reader-facing quote at ^pin-op10 ('...category error') IS faithful to cached text (elides the parenthetical Alito cite with '. . .') and the pincite is defensible.
- **proposed_fix:** Replace the pin-op10 quote with the actual category-error sentence from the opinion, or regenerate the pinpoint against the cached opinion text.

### F-S9-PR-3647585329 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Graham v. Connor.json
- **problem:** The asserted pin-395 quote is not a Graham opinion passage; it splices page Markdown and section headings rather than the opinion text at 490 U.S. 395.
- **verbatim:** and hold that <i>all</i> claims that law enforcement officers have used excessive force
- **tally:** codex-A=stands: The payload quote includes content-page Markdown headings, not text from the Supreme Court opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Reader-facing quote at ^pin-395 is faithful to cached text and the pincite (395) is correct; defect is confined to the corrupted stored metadata quote (builder self-flagged 'mismatch').
- **proposed_fix:** Replace pin-395 with the actual page-395 holding passage from the cached opinion, beginning with the Court's statement that it holds all such excessive-force seizure claims are governed by the Fourth…

### F-S9-PR-d426433204 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Griffin v. Wisconsin.json
- **problem:** pin-873's stored quote is not a character-faithful judicial quote. It splices page-generated Issue/Rule text, including markdown heading text, rather than the opinion passage at 873-874.
- **verbatim:** A State’s operation of a probation system, like its operation of a school, government office or prison, or its supervision of a regulated industry, likewise presents “special <page-number citation-in…
- **tally:** codex-A=stands: The payload quote begins "satisfies the Fourth Amendment. ## Rule Yes...", which is not opinion text at the cited passage.  |  codex-B=refuted: Quote-fidelity/support is outside Lens B; no independent treatment or currency defect is raised for this pinpoint row.  |  opus=stands-modified: Reader-facing quote at ^pin-873 is faithful and its pincite (873-874) is correct; defect is confined to the corrupted stored metadata quote (self-flagged 'mismatch').
- **proposed_fix:** Replace the pin-873 quote with the actual opinion passage beginning "A State’s operation of a probation system..." and preserve source punctuation; use 483 U.S. 873-874 as the locator.

### F-S9-PR-c16d0250f5 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Groh v. Ramirez.json
- **problem:** Lake pin-557 is not an opinion quotation. It is page prose spanning Background, Issue, and Rule text, begins mid-sentence, and does not match the 557 passage in the opinion text.
- **verbatim:** The fact that the <i>application</i> adequately described the "things to be seized" does not save the <i>warrant</i> from its facial invalidity.
- **tally:** codex-A=stands: The pin quote begins with '), not the weapons' and includes '## Issue' and '## Rule', which are content-page headings, not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Reader-facing quote at ^pin-557 is faithful and its pincite (557) is correct; defect is confined to the corrupted stored metadata quote (self-flagged 'mismatch').
- **proposed_fix:** Replace pin-557 with the exact 557 opinion passage, preserving original quotation marks and formatting, or mark the page language as paraphrase instead of a quote.

### F-S9-PR-c02c9dbc3a · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Henry v. United States (1959).json
- **problem:** The pin-102 payload is not an opinion quote; it is a corrupted harvest of the content page text and frontmatter-like prose.
- **verbatim:** Probable cause exists if the facts and circumstances known to the officer warrant a prudent man in believing that the offense has been committed.
- **tally:** codex-A=stands: The payload begins with generated page content rather than text from Henry.  |  codex-B=refuted: Quote fidelity is outside Lens B; the embedded treatment language is covered by the separate treatment assertion.  |  opus=stands-modified: Underlying wiki proposition is sound: the real pin-102 quote matches cached text verbatim at page 102 (immediately after the '*102' marker).
- **proposed_fix:** Replace the pin-102 quote payload with the actual page-102 opinion sentence supporting the rule.

### F-S9-PR-0fe3b74880 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Herring v. United States.json
- **problem:** The harvested pin-144 quote is page Markdown and narrative text, not the verbatim opinion sentence cited by the page.
- **verbatim:** 3. To trigger the exclusionary rule, police conduct must be sufficiently deliberate that exclusion can meaningfully deter it, and sufficiently culpable that such deterrence is worth the price paid by…
- **tally:** codex-A=stands: The payload quote starts with the built page header and background text, which is not in the opinion passage at the cited rule sentence.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Underlying wiki proposition is sound: the real pin-144 quote matches the cached slip text verbatim (line-break hyphenation aside).
- **proposed_fix:** Replace pin-144 with the actual opinion sentence beginning: "To trigger the exclusionary rule, police conduct must be sufficiently deliberate..."

### F-S9-PR-19b3f2218f · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hester v. United States.json
- **problem:** The pin-58 quote payload is not a character-faithful quote from the opinion; it overcaptures content-page/front-matter text and stops before the actual quoted passage.
- **verbatim:** there was no seizure in the sense of the law when the officers examined the contents of each after it had been abandoned.
- **tally:** codex-A=stands: The disclosed opinion text contains the actual no-seizure sentence on page *58.  |  codex-B=refuted: Lens B does not evaluate support or quote fidelity.  |  opus=stands-modified: Underlying wiki proposition is sound: the real pin-58 quote matches cached text verbatim and sits on page 58 (between the *58 and *59 star markers), confirming the pincite.
- **proposed_fix:** Replace the pin-58 quote payload with the actual opinion sentence: "there was no seizure in the sense of the law when the officers examined the contents of each after it had been abandoned."

### F-S9-PR-a7ea230637 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hiibel v. Sixth Judicial Dist. Court.json
- **problem:** Pin-186's payload quote is not an opinion passage; it is a harvested page fragment spanning background/issue/rule text, while the actual page-186 opinion quote is different.
- **verbatim:** Obtaining a suspect's name in the course of a <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span><…
- **tally:** codex-A=stands: The asserted quote contains markdown headings ('## Issue', '## Rule') and does not appear as a character-faithful quote in the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Pin survives: a genuine faithful quote exists at p.186 ('Obtaining a suspect's name in the course of a Terry stop serves important government interests.'), verified verbatim in cached text.
- **proposed_fix:** Replace pin-186 with the opinion sentence: "Obtaining a suspect's name in the course of a Terry stop serves important government interests."

### F-S9-PR-eac5c00fda · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hill v. California.json
- **problem:** The reviewed pin-802 payload is not a verbatim Hill opinion passage; it is a harvested content-page fragment and the lake record itself marks the pinpoint quote_fidelity as mismatch with no star marker.
- **verbatim:** [w]hen the police have probable cause to arrest one party, and when they reasonably mistake a second party for the first party, then the arrest of the second party is a valid arrest.
- **tally:** codex-A=stands: The lake quote begins with page markdown text, not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Pin survives: the faithful quote exists at p.802, verified in cached text before the '*803' star marker.
- **proposed_fix:** Replace pin-802's stored quote with the actual opinion passage at star page 802 and set the star marker to 802.

### F-S9-PR-54a935b1cd · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hoffa v. United States.json
- **problem:** The pin-310 stored quote is not a character-faithful opinion quote; it is harvested page prose spanning the built page Background, Issue, and Rule lead-in. The lake record itself marks quote_fidelity as mismatch and has no star marker.
- **verbatim:** There is no constitutional right to be arrested.
- **tally:** codex-A=stands: The payload quote includes content-page headings and prose such as '## Issue' and '## Rule', which are not a contiguous passage from the opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no currency or treatment defect specific to pin-310 appears in the disclosed record.  |  opus=stands-modified: Pin survives: 'There is no constitutional right to be arrested.' is verbatim in the cached opinion at p.310.
- **proposed_fix:** Replace pin-310's quote with the actual quoted sentence from the opinion, 'There is no constitutional right to be arrested.', and set the pinpoint to page/star 310 in paragraph b414-6.

### F-S9-PR-25242d5204 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hope v. Pelzer.json
- **problem:** The pin-741 payload quote is not a character-faithful opinion quote; it is harvested page prose spanning the Issue/Rule text and a markdown heading, and the lake itself marks quote_fidelity as mismatch with no star marker.
- **verbatim:** Our opinion in Lanier thus makes clear that officials can still be on notice that their conduct violates established law even in novel factual circumstances.
- **tally:** codex-A=stands: The asserted payload quote does not appear as a continuous passage in the disclosed opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no treatment or currency defect attaches to this pinpoint.  |  opus=stands-modified: Pin survives: the faithful quote exists at p.741 ('officials can still be on notice that their conduct violates established law even in novel factual circumstances'); the content page's '[O]fficials.…
- **proposed_fix:** Replace pin-741's stored quote with the actual page-*741 opinion passage supporting the rendered quote, or remove the quote pinpoint if the sentence is only page synthesis. The likely corrected opini…

### F-S9-PR-1586e0f5c5 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Horton v. California.json
- **problem:** The pin-130 payload is not an opinion quote at all; it is harvested content-page/frontmatter prose. The actual opinion sentence is different and the lake record marks this pin as a mismatch.
- **verbatim:** We conclude that even though inadvertence is a characteristic of most legitimate “plain-view” seizures, it is not a necessary condition.
- **tally:** codex-A=stands: The disclosed opinion supports the inadvertence proposition, but not the harvested payload quote.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity or textual support.  |  opus=stands-modified: Content-page quote at ^pin-130 ('even though inadvertence is a characteristic of most legitimate "plain-view" seizures, it is not a necessary condition.') matches the opinion verbatim (curly vs strai…
- **proposed_fix:** Replace pin-130 with the actual opinion sentence and re-check the page pin: We conclude that even though inadvertence is a characteristic of most legitimate “plain-view” seizures, it is not a necessa…

### F-S9-PR-f88b011fe9 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Howes v. Fields.json
- **problem:** The pin-op9 payload quote is not character-faithful to the opinion text; it appears to splice page prose/Markdown from the built page rather than an opinion passage.
- **verbatim:** Not all restraints on freedom of movement amount to custody for purposes of Miranda.
- **tally:** codex-A=stands: The lake itself marks pin-op9 quote_fidelity as mismatch.  |  codex-B=refuted: Lens B found no independent currency or treatment defect tied to pin-op9; the pin cites the same verified SCOTUS authority with field_i_validity good_law.  |  opus=stands-modified: Content-page quote at ^pin-op9 ('Not all restraints on freedom of movement amount to custody for purposes of Miranda.') matches the opinion verbatim.
- **proposed_fix:** Replace the pin-op9 stored quote with the actual slip-opinion passage used on the page: "Not all restraints on freedom of movement amount to custody for purposes of Miranda."

### F-S9-PR-8f1ac131c5 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hudson v. Michigan.json
- **problem:** pin-594's harvested quote is not the opinion passage. It is page/frontmatter/summary text ending before the actual quoted sentence, and the displayed page quote also changes the opinion's curly apostrophe in "one’s" to straight "one's".
- **verbatim:** What the knock-and-announce rule has never protected, however, is one’s interest in preventing the government from seeing or taking evidence described in a warrant.
- **tally:** codex-A=stands: The disclosed opinion text contains the quoted proposition at lines 379-381, not the page/frontmatter block stored in the pin payload.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Content-page quote at ^pin-594 ('What the knock-and-announce rule has never protected, however, is one's interest in preventing the government from seeing or taking evidence described in a warrant.')…
- **proposed_fix:** Replace pin-594 with the actual opinion sentence and preserve the opinion's characters: "What the knock-and-announce rule has never protected, however, is one’s interest in preventing the government…

### F-S9-PR-c9f6c99912 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Hudson v. Palmer.json
- **problem:** The reviewed pin-526 quote payload is not a verbatim opinion passage for the cited holding; it is harvested content-page prose plus section headers, and the lake itself marks quote_fidelity as mismatch. The visible page quote at 468 U.S. 526 appears faithful, but this reviewed quote_pinpoint payloa…
- **verbatim:** hold that society is not prepared to recognize as legitimate any subjective expectation of privacy that a prisoner might have in his prison cell and that, accordingly, the Fourth Amendment proscripti…
- **tally:** codex-A=stands: The lake pinpoint quote contains content headings such as ## Issue and ## Rule No., which are not opinion text.  |  codex-B=refuted: This row is a quote-fidelity/pinpoint assertion; support and quote-fidelity defects are outside lens B.  |  opus=stands-modified: Content-page quote at ^pin-526 matches the opinion verbatim; the leading '[W]e' correctly brackets the opinion's original lowercase 'we' (mid-sentence after 'Notwithstanding our caution...').
- **proposed_fix:** Replace pin-526's stored quote with the actual 468 U.S. at 526 holding passage, or retarget the inventory row to the visible holding quote on content_page.md line 53.

### F-S9-PR-e1ec5bd80e · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Illinois v. Gates.json
- **problem:** The quote is substantively close but not character-faithful to the disclosed opinion text: the opinion says 'commonsense' and uses curly double quotation marks, while the payload says 'common-sense' and uses straight single quotation marks.
- **verbatim:** practical, commonsense decision whether, given all the circumstances set forth in the affidavit before him, including the “veracity” and “basis of knowledge”
- **tally:** codex-A=stands: The disclosed opinion text reads 'practical, commonsense decision'; the payload/content quote reads 'practical, common-sense decision'.  |  codex-B=refuted: Lens B found no treatment or currency defect tied to pin-238a.  |  opus=stands-modified: Quotation is otherwise verbatim and correctly pincited to 238; only an orthographic hyphen was inserted into 'commonsense'.
- **proposed_fix:** Correct the quote to match the opinion text exactly, including 'commonsense' and the opinion's quotation marks around veracity and basis of knowledge.

### F-S9-PR-5e43e012da · quote-fidelity · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Illinois v. Rodriguez.json
- **problem:** The quoted words are substantively faithful, but the pin metadata flags quote_fidelity as mismatch and does not record the page-split marker where the cached text inserts *189 between 'warrantless' and 'entry'.
- **verbatim:** If not, then warrantless <span class="star-pagination">*189</span> entry without further inquiry is unlawful unless authority actually exists. But if so, the search is valid.
- **tally:** codex-A=stands-modified: The content quote matches lake pinpoints[].quote exactly.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Quote text reads as a clean, plausible opinion quotation, but with no source text disclosed I cannot affirm fidelity.
- **proposed_fix:** Keep the quote text, but mark the quote as verified under pagination-normalized comparison and record the *189 split or page range 188-189.

### F-S9-PR-e3345f6fbe · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Illinois v. Rodriguez.json
- **problem:** The pin-188 quote is a malformed harvest of content-page prose and headings, not a verbatim quote from the opinion. The visible page quote also differs from the cached opinion punctuation around 'moment. . .'.
- **verbatim:** determination of consent to enter must "be judged against an objective standard: would the facts available to the officer at the moment. . . `warrant a man of reasonable caution in the belief'"
- **tally:** codex-A=stands: The payload quote contains Markdown headings such as '## Issue' and '## Rule', which are not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload 'quote' is page prose incl markdown headers, confirming a mis-scoped span; the 'mismatch' is not evidence the page's actual quotation is unfaithful.
- **proposed_fix:** Replace pin-188 with the actual *188 quotation and align punctuation with the cached opinion text.

### F-S9-PR-1c188b3e42 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Illinois v. Wardlow.json
- **problem:** The pin-124b quote is not character-faithful as framed: it changes the opinion's curly apostrophe to a straight apostrophe and joins two sentences while omitting the intervening Brown v. Texas citation without any ellipsis or citation-omitted signal.
- **verbatim:** An individual’s presence in an area of expected criminal activity, standing alone, is not enough to support a reasonable, particularized suspicion that the person is committing a crime. <em>Brown </e…
- **tally:** codex-A=stands: The lake record marks pin-124b quote_fidelity as mismatch and pinpoint_status as slip-only.  |  codex-B=refuted: This row presents a quote-fidelity issue, not a treatment or currency assertion.  |  opus=stands-modified: Quote reads as genuine Wardlow language but is unverified from disclosed evidence.
- **proposed_fix:** Use the opinion's punctuation and either include the intervening citation or mark the omission, e.g. split the quote or insert an ellipsis/citation-omitted notation between the two sentences.

### F-S9-PR-4808993ffa · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Illinois v. Wardlow.json
- **problem:** The pin-124 quote payload is not a verbatim opinion passage; it is a harvested Markdown/content-page excerpt beginning with the page title and background, while the visible pinned rule quote on the page is a different sentence from the opinion.
- **verbatim:** Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable suspicion.
- **tally:** codex-A=stands: The lake record itself marks pin-124 quote_fidelity as mismatch and pinpoint_status as slip-only.  |  codex-B=refuted: This is a quote-fidelity row; lens B does not raise support or quote findings.  |  opus=stands-modified: Blob composition (markdown headers; ends at 'Rule Yes.') shows a mis-scoped span, not a genuine quote comparison.
- **proposed_fix:** Replace pin-124's quote payload with the actual opinion sentence pinned on the page: "Our cases have also recognized that nervous, evasive behavior is a pertinent factor in determining reasonable sus…

