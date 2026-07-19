# P2 ESCALATE PACKET 10/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-7cbcafb75b · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Harris (1971).json
- **problem:** The pin-583 quote stored in the lake/inventory is not an opinion quote; it is a long scrape of the built page header/background/rule text and is marked mismatch with no star marker.
- **verbatim:** These statements were against the informant's penal interest, for he thereby admitted major elements of an offense under the Internal Revenue Code.
- **tally:** codex-A=stands: The lake record itself marks pin-583 quote_fidelity as mismatch and pinpoint_status as slip-only.  |  codex-B=refuted: Quote fidelity is outside Lens B.  |  opus=stands-modified: Recorded quote is page markdown, not opinion text -> genuine extraction artifact, NOT a page misquote.
- **proposed_fix:** Replace pin-583 with the actual opinion passage on star page 583 supporting penal-interest reliability, and regenerate the pinpoint from the cached opinion text.

### F-S9-PR-a81dac608d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Havens.json
- **problem:** The stored pin-627 quote is not an opinion quotation. It splices content-page prose across Background, Issue, and Rule headings, and does not match the cached opinion text for the cited page.
- **verbatim:** ## Issue Whether illegally seized evidence may be used
- **tally:** codex-A=stands: The payload contains markdown headings '## Issue' and '## Rule', which are from the built page, not the opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; no currency or treatment assertion in this row is refuted.  |  opus=stands-modified: Recorded quote is page markdown, not opinion text -> extraction artifact, NOT a page misquote.
- **proposed_fix:** Replace pin-627 with the actual Court sentence at page 627 beginning 'In terms of impeaching...' / 'we see no difference...', set the page to 627, and rerun quote-fidelity after applying the corpus q…

### F-S9-PR-8912a54939 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Henry.json
- **problem:** The pin-270 quote field is not a character-faithful opinion quotation; it is a stitched excerpt from the content page with markdown artifacts and is already marked quote_fidelity=mismatch in the lake record.
- **verbatim:** Three factors are important. First, Nichols was acting under instructions as a paid informant for the Government; second, Nichols was ostensibly no more than a fellow inmate of Henry; and third, Henr…
- **tally:** codex-A=stands: The payload quote contains '*Massiah*', '## Rule', and wiki-link syntax, none of which are part of the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Recorded quote is page markdown, not opinion text -> extraction artifact, NOT a page misquote.
- **proposed_fix:** Replace the pin-270 quote with the actual opinion passage supporting the 270 pinpoint, beginning with 'Three factors are important...', and remove the stitched Issue/Rule prose from the quote field.

### F-S9-PR-4dcc841f1d · quote-fidelity · sev=medium · needs_cl=false · quorum=1/3
- **object:** _overhaul2/lake/cases/United States v. Johns.json
- **problem:** The pin-482 quotation 'whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks' is verbatim but is cited '469 U.S. at 482'. In the cached opinion the quoted sentence is the last sentence of paragraph b6…
- **verbatim:** whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks
- **tally:** codex-A=MISSING  |  codex-B=MISSING  |  opus=stands-modified: Quote text is verbatim, so it survives the quote-fidelity attack, but the page pincite is off by one: the quoted sentence sits on page 483 (between *483 and *484), while the content cites 482.
- **proposed_fix:** Change the pin-482 pincite from '469 U.S. at 482' to '469 U.S. at 483', and update the Sources line 'pinpoints: 482, 487' to 'pinpoints: 483, 487'.

### F-S9-PR-c9839ea0aa · quote-fidelity · sev=high · needs_cl=false · quorum=2/3
- **object:** _overhaul2/lake/cases/United States v. Johns.json
- **problem:** The pin-482 payload is not an opinion quote; it is a generated content-page/header/background excerpt harvested as a quote. The lake also marks this pinpoint quote_fidelity as mismatch with no star marker.
- **verbatim:** The issue presented by this case is whether the subsequent warrantless search was unreasonable merely because it occurred three days after the packages were unloaded from the pickup trucks.
- **tally:** codex-A=stands: The payload quote begins with generated page material, not the Johns opinion text.  |  codex-B=refuted: This is a quote-fidelity row; support and quote matching are outside lens B.  |  opus=MISSING
- **proposed_fix:** Replace pin-482 with the actual opinion sentence being quoted, or remove the verbatim quote/pin until it is re-harvested and verified against the opinion text.

### F-S9-PR-5ec0792ee2 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Leary.json
- **problem:** Pin-600's stored quote is garbled page prose from the Issue/Rule sections, not a character-faithful opinion quotation. The visible rule quote also omits the opinion's bracketed word [also].
- **verbatim:** The particularity requirement [also] ensures that a search is confined in scope to particularly described evidence relating to a specific crime for which there is demonstrated probable cause.
- **tally:** codex-A=stands: The payload quote begins with issue text and includes markdown heading text, so it cannot be verified as an opinion quotation.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Reader-facing page quotation is verbatim-faithful to the opinion at star page 600 and correctly attributed to Voss v. Bergsgaard, so the quote proposition survives.
- **proposed_fix:** Regenerate pin-600 from the opinion text and quote the exact sentence including [also], or paraphrase without quotation marks.

### F-S9-PR-329e3fc994 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Leon.json
- **problem:** pin-922's stored quote is not the opinion quote at 468 U.S. 922; it is a chunk of the generated content page/front matter ending before the actual quoted sentence. The lake record itself marks quote_fidelity as mismatch and pinpoint_status as slip-only.
- **verbatim:** We conclude that the marginal or nonexistent benefits produced by suppressing evidence obtained in objectively reasonable reliance on a subsequently invalidated search warrant cannot justify the subs…
- **tally:** codex-A=stands: The payload quote begins with '--- # United States v. Leon' and reproduces content-page material, not opinion text.  |  codex-B=refuted: Lens B does not assess quote fidelity or support.  |  opus=stands-modified: Reader-facing page quotation is verbatim-faithful to the opinion on page 922 (the quote precedes the *923 marker), so the quote proposition survives.
- **proposed_fix:** Replace pin-922 quote with the page-922 opinion sentence beginning 'We conclude that the marginal or nonexistent benefits...' and set an appropriate 922 star/pin status after validation.

### F-S9-PR-d25d57422e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Mathis.json
- **problem:** The pin-1276 harvested quote is not an opinion quote at all; it is a large chunk of the built content page/frontmatter rather than the passage from the Mathis opinion.
- **verbatim:** Alternatively, even if the search warrant was not supported by probable cause, evidence obtained from the search of Mathis’s phone was not subject to suppression under the good faith exception to the…
- **tally:** codex-A=stands: The payload quote begins with markdown page material ('--- # United States v. Mathis') that does not appear as opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The RENDERED content-page pin-1276 quote is verbatim-faithful to the cached opinion (slip op. p.22 = 767 F.3d at 1276), so the fidelity claim itself survives.
- **proposed_fix:** Replace pin-1276.quote with the actual opinion sentence beginning 'Alternatively, even if the search warrant was not supported by probable cause...'.

### F-S9-PR-2dc9ca569d · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Matlock.json
- **problem:** pin-170's lake pinpoint quote is not an opinion quote; it is a concatenation of the built page header/background/issue/rule. The lake itself marks the pinpoint as mismatch, slip-only, with no star_marker. The actual page-170 passage is the common-authority sentence, and the rendered page also silen…
- **verbatim:** the consent of one who possesses common authority over premises or effects is valid as against the absent, nonconsenting person with whom that authority is shared.
- **tally:** codex-A=stands: The disclosed lake record for pin-170 has quote_fidelity=mismatch, pinpoint_status=slip-only, and star_marker=null.  |  codex-B=refuted: Quote fidelity/support is outside lens B, so no quote-fidelity defect is raised here.  |  opus=stands-modified: The rendered content-page pin-170 quote is verbatim-faithful to the cached opinion (text at the *170->*171 boundary), so the fidelity claim survives.
- **proposed_fix:** Replace pin-170 with the exact opinion text at page 170, set the page/star metadata to 170, and render the quote either lower-case as in the source or with bracketed capitalization.

### F-S9-PR-d78205a3e2 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Mendenhall.json
- **problem:** The pin-554 quote text is not character-faithful to the opinion text; it appears to be a malformed harvest of page prose rather than the cited Mendenhall sentence.
- **verbatim:** We conclude that a person has been “seized” within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed t…
- **tally:** codex-A=stands: The disclosed opinion text contains the Mendenhall free-to-leave sentence at the page 554 marker, not the payload string beginning '? ## Rule'.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Recorded pin-554 quote '? ## Rule A person is seized only when a reasonable person would not feel free to leave.' is a markdown/gloss harvest artifact, not opinion language; the opinion (p. b612-6, *…
- **proposed_fix:** Replace pin-554 with the exact opinion sentence from page 554, preserving the opinion text punctuation or expressly defining a normalization rule.

### F-S9-PR-dde329d155 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Morley.json
- **problem:** The pin-op15 stored quote is not a character-faithful excerpt from the opinion; it is built-page Markdown/header/background text ending before the actual quoted rule.
- **verbatim:** quote_fidelity": "mismatch"
- **tally:** codex-A=stands: The lake record itself marks pin-op15 quote_fidelity as mismatch and has null position and null fragment.  |  codex-B=refuted: Quote fidelity is outside lens B, so I do not raise the disclosed mismatch as a support/quote defect.  |  opus=stands-modified: The rendered rule quote at ^pin-op15 is verbatim at slip op. 15 and correctly pincited, so the legal proposition stands.
- **proposed_fix:** Re-harvest pin-op15 from the cached opinion on slip-opinion page 15 and store the actual automobile-exception rule sentence, with a validated position or fragment.

### F-S9-PR-9eeddb4060 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Morton.json
- **problem:** The pin-op13 quote payload/lake pinpoint is not the opinion quote at slip page 13; it is a harvested copy of the rendered page header/background/issue text. The lake record itself marks this pinpoint quote_fidelity as mismatch and has no position.
- **verbatim:** We do not decide if the state judge should have authorized full searches of the phones based on these affidavits.
- **tally:** codex-A=stands: The disclosed cached opinion contains the page-13 passage after the court's separator, not the markdown/header/background text carried in the inventory payload.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Rendered rule quote at ^pin-op13 is verbatim at slip op. 13 and correctly pincited, so the legal proposition stands.
- **proposed_fix:** Replace pin-op13 with the actual slip-page-13 opinion excerpt beginning with the court's two-sentence good-faith/non-decision statement, and store a valid position/page/fragment. Preserve character f…

### F-S9-PR-0a71103366 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Neugin.json
- **problem:** The quote is not character-faithful. It splices two conclusion passages with an ellipsis and omits the intervening sentence fragment, while presenting the result as one quoted proposition. The lake record also marks pin-op17 quote_fidelity as mismatch.
- **verbatim:** the police would not have inevitably discovered the evidence absent the Fourth Amendment violation. Because the violation caused the discovery of the ammunition and firearm, that evidence is fruit of…
- **tally:** codex-A=stands: The disclosed text has a full stop after Fourth Amendment violation and then a separate sentence beginning Because the violation caused the discovery of the ammunition and firearm.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity.  |  opus=stands-modified: The quote is faithful (both ellipsis fragments verbatim), so the legal proposition holds and the 'mismatch' flag is over-conservative.
- **proposed_fix:** Use the full conclusion language or split it into two accurate quotes instead of the current ellipsis splice.

### F-S9-PR-85b22daa59 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Neugin.json
- **problem:** The pin-op15 payload quote is not an opinion passage. It is a harvested excerpt from content_page.md beginning with page chrome and background prose, and the lake record marks quote_fidelity as mismatch.
- **verbatim:** (1984)); accord United States v. Owens, 782 F.2d 146, 153 (10th Cir. 1986) (“[T]he inevitable discovery exception to the exclusionary rule cannot be invoked because of [a] highly speculative assumpti…
- **tally:** codex-A=stands: The disclosed lake pinpoint for pin-op15 contains page header/content-page prose, not text from the Neugin opinion.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity.  |  opus=stands-modified: Rendered rule quote at ^pin-op15 is verbatim at slip op. 15 with correct Owens attribution and pincite; only the pinpoint's stored quote string is the header-block harvest artifact.
- **proposed_fix:** Replace pin-op15 with the actual opinion passage quoting Owens, and mark it matched only if the displayed quote preserves the bracketed initial and quotation marks accurately.

### F-S9-PR-e0f85d3c21 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Payner.json
- **problem:** pin-735 is not a character-faithful opinion quote or verified pinpoint; it is a scraped blend of page summary prose and markdown headings, and the lake marks it as mismatched with no star marker.
- **verbatim:** "quote_fidelity": "mismatch"
- **tally:** codex-A=stands: The disclosed lake record itself marks pin-735 quote_fidelity as mismatch and pinpoint_status as slip-only.  |  codex-B=refuted: This row is a quote-fidelity assertion; Lens B checks only currency and treatment.  |  opus=stands-modified: The corrupted/slip-only pin-735 record is a real but minor data defect; HOWEVER the quotation actually rendered on the page at ^pin-735 is verbatim-faithful to the cached opinion (id b777-7) and corr…
- **proposed_fix:** Regenerate pin-735 from the actual rule passage at 447 U.S. 735, beginning with the opinion's rule sentence, and attach a verified star marker/fragment instead of the current summary-prose artifact.

### F-S9-PR-0046c2b746 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Sharpe.json
- **problem:** The pin-685 quote stored in the lake/inventory is not an opinion quote; it is built-page/frontmatter content and the lake itself marks it as quote_fidelity mismatch with no star marker.
- **verbatim:** --- # United States v. Sharpe *470 U.S. 675 (1985)*
- **tally:** codex-A=stands: The asserted pin-685 payload begins with the generated page header rather than the opinion text.  |  codex-B=refuted: Lens B does not attack quote fidelity or support.  |  opus=stands-modified: Pinpoint RECORD is malformed (quote = content-page prose, not an opinion passage), but the underlying anchored proposition IS verbatim-supported at 470 U.S. 685, so the deliverable's legal content is…
- **proposed_fix:** Replace pin-685 with the actual 470 U.S. at 685 passage, e.g. "But our cases impose no rigid time limitation on Terry stops.", and mark it only after verifying the pinpoint against the opinion text.

### F-S9-PR-5a332ca2ee · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Smith (2024).json
- **problem:** The pin-838 quote record is not character-faithful to the opinion passage it claims to support: the lake pinpoint quote contains harvested page prose ending before the actual quoted holding, and the built page's displayed quotation changes source typography by using straight apostrophes where the o…
- **verbatim:** law enforcement’s reasonable conduct in this case in light of the novelty of
- **tally:** codex-A=stands: The lake record itself marks pin-838 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Malformed pinpoint record (quote = page prose), but the anchored content-page holding is verbatim in the cached Conclusion, so the deliverable's legal content is accurate.
- **proposed_fix:** Replace pin-838 with the actual page-38 holding quote from the opinion text and preserve source characters, including law enforcement’s and district court’s; then re-run quote matching.

### F-S9-PR-3a2a2c3648 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Sokolow.json
- **problem:** pin-8 is not a faithful quote pinpoint. The lake pin-8 quote is a harvested content-page/header excerpt, not the Sokolow opinion passage used by the page, and the lake itself marks quote_fidelity as mismatch with no star marker.
- **verbatim:** In evaluating the validity of a stop such as this, we must consider "the totality of the circumstances  the whole picture."
- **tally:** codex-A=stands: The cached opinion contains the relevant passage at star page 8, but the lake pin-8 quote begins with page/frontmatter material rather than that passage.  |  codex-B=refuted: Lens B does not attack quote fidelity; no currency or treatment defect specific to pin-8 is disclosed.  |  opus=stands-modified: Malformed pinpoint record (quote = page prose), but the anchored content-page proposition is verbatim-supported at 490 U.S. 8 (the em-dash the CL extraction dropped is faithfully restored on the cont…
- **proposed_fix:** Replace pin-8 with the actual opinion passage at star page 8 and set a verified star_marker/position only after matching the cached text.

### F-S9-PR-6caf6311d8 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Van Leeuwen.json
- **problem:** pin-252's lake quote is page/frontmatter/background text, not the Supreme Court passage supporting the quoted rule.
- **verbatim:** The nature and weight of the packages, the fictitious return address, and the British Columbia license plates of respondent who made the mailings in this border town certainly justified detention, wi…
- **tally:** codex-A=stands: The lake pinpoint itself marks pin-252 quote_fidelity as mismatch and has no star marker.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The record's own 'mismatch/slip-only' flag is correct: the stored blob does not occur in the opinion, so the pin is not asserting a false verified quote.
- **proposed_fix:** Replace pin-252 with the actual opinion text at star page 252, or with the exact quoted substring used on the content page, and set the star marker to 252.

### F-S9-PR-88e97a5f90 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Ventresca.json
- **problem:** Pin-108's stored quote is not an opinion quote; it is a harvested block from the built content page/frontmatter through the Rule heading. It does not appear as quoted opinion text.
- **verbatim:** affidavits for search warrants, such as the one involved here, must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion.
- **tally:** codex-A=stands: Lake marks pin-108 quote_fidelity as mismatch and pinpoint_status as slip-only.  |  codex-B=refuted: Quote fidelity is outside lens B; no support or quote-fidelity defect is raised.  |  opus=stands-modified: Recorded quote string is content-page markdown ('--- # United States v. Ventresca ... ## Rule Yes.'), which is genuinely absent from the opinion — quote_fidelity='mismatch' is accurate as to the corr…
- **proposed_fix:** Replace pin-108 with the actual page 108 opinion passage beginning "affidavits for search warrants, such as the one involved here, must be tested and interpreted..."

### F-S9-PR-621d0612b3 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Vinton.json
- **problem:** The quoted passage changes the officer's name from 'Officer Alton' in the opinion to 'Officer Aton' in the inventory/content quote, so it is not character-faithful.
- **verbatim:** Examining the totality of the circumstances objectively, Officer Alton had a reasonable belief, based on specific and articulable facts, that Vinton was armed and dangerous. See Long, 463 U.S. at 104…
- **tally:** codex-A=stands: The disclosed opinion says 'Officer Alton'; the reviewed quote says 'Officer Aton'.  |  codex-B=refuted: Quote fidelity is outside lens B.  |  opus=stands-modified: Opinion text at slip op. 8-9 reads 'Officer Alton had a reasonable belief...'; the recorded/page quote substitutes 'Aton' (dropped 'l'), an infidelity within quotation marks.
- **proposed_fix:** Correct the quote to 'Officer Alton' and preserve an accurate ellipsis only for the omitted citation text.

### F-S9-PR-a9362bd6cd · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Vinton.json
- **problem:** pin-20's stored pinpoint quote is not a verbatim opinion passage; it is copied from content-page narrative and headings, including '## Issue' and '## Rule', rather than the opinion text supporting the pin.
- **verbatim:** hidden elsewhere in the vicinity. This concern was not abated by ordering Vinton out of the car and handcuffing him, because had Vinton ultimately not been arrested, he would have been “permitted to…
- **tally:** codex-A=stands: The disclosed opinion contains the 'This concern was not abated' passage, not the inventory quote beginning 'sticker that could suggest...'.  |  codex-B=refuted: Quote fidelity is outside lens B.  |  opus=stands-modified: Recorded quote string is page markdown (contains '## Issue', '## Rule', '*Michigan v. Long*'), genuinely absent from the opinion — quote_fidelity='mismatch' is accurate as to the corrupted field.
- **proposed_fix:** Replace pin-20's quote with the actual opinion passage beginning 'This concern was not abated...' and remove generated page headings from the pinpoint quote.

### F-S9-PR-28a1f2148e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Winston v. Lee.json
- **problem:** The stored/payload quote for pin-759 is not an opinion quote at all; it is a harvested block of the built page header/background/rule text.
- **verbatim:** A compelled surgical intrusion into an individual’s body for evidence, however,
- **tally:** codex-A=stands: The payload begins with page markup and summary text, not the Supreme Court opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload quote is a harvest artifact (page front-matter), not verifiable as an opinion quotation.
- **proposed_fix:** Replace the pin-759 quote with the actual opinion sentence from page 759, preserving exact punctuation, or remove the faulty pinpoint quote.

### F-S9-PR-3305e629bc · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Wolf v. Colorado.json
- **problem:** pin-27 is not a verified authority quote. The lake quote is generated page/header/background prose, not the quoted Wolf passage, and the lake itself marks the pinpoint as a mismatch with no star marker or position.
- **verbatim:** The security of one's privacy against arbitrary intrusion by the policewhich is at the core of the Fourth Amendmentis basic to a free society. It is therefore implicit in "the concept of ordered li…
- **tally:** codex-A=stands: The payload quote for pin-27 begins with '--- # Wolf v. Colorado' and includes page prose, not opinion text.  |  codex-B=refuted: Lens B does not raise support or quote-fidelity findings.  |  opus=stands-modified: Payload quote is a harvest artifact (front-matter), not an opinion quotation.
- **proposed_fix:** Replace pin-27 with the actual opinion sentence from text/Wolf v. Colorado__a8b65b.txt at star pages 27-28, preserving the opinion text's quotation marks and pagination, then reverify the fragment/st…

### F-S9-PR-f7e4ae2e6c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Wong Sun v. United States.json
- **problem:** The asserted quote is not opinion text. It appears to be harvested from the content page across the Issue/Rule boundary, including the markdown heading '## Rule', and is not character-faithful to the case text.
- **verbatim:** the more apt question in such a case is
- **tally:** codex-A=stands: The asserted fragment includes content-page prose and the markdown heading '## Rule', which cannot be a verbatim Supreme Court quote.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload quote is a harvest artifact (page Issue/Rule prose), not an opinion quotation.
- **proposed_fix:** Replace this harvested fragment with the actual 371 U.S. 487-488 passage supporting the rule, or remove the quote assertion for pin-488.

