# P2 ESCALATE PACKET 04/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-a36f060b59 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Adams v. Williams.json
- **problem:** The pin-147b quote is not character-faithful to the disclosed opinion text: it replaces an intervening sentence with an ellipsis and normalizes the dash punctuation, while the lake marks it mismatch/slip-only.
- **verbatim:** Some tips, completely lacking in indicia of reliability, would either warrant no police response
- **tally:** codex-A=stands: The opinion text contains an intervening sentence beginning with the evidence_quote, which the page quote omits with ellipsis.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Opening and closing spans match verbatim; the marked ellipsis correctly elides the omitted sentence.
- **proposed_fix:** Either quote the passage exactly from the text or mark it as an editorially ellipted quotation and verify the pinpoint at star page 147.

### F-S9-PR-a91bfaa150 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Adams v. Williams.json
- **problem:** The pin-147 payload/lake quote is not the opinion quote; it captures the content page header/background/rule lead-in and is marked quote_fidelity=mismatch with no verified star marker.
- **verbatim:** the information carried enough indicia of reliability to justify the officer's forcible stop of Williams.
- **tally:** codex-A=stands: The visible page quotation for pin-147 is present in the opinion text, but the assertion payload/lake pin quote is a harvested page-header block instead.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Page pin-147 quote 'the information carried enough indicia of reliability to justify the officer's forcible stop of Williams.' appears verbatim after the *147 marker; pincite 147 correct.
- **proposed_fix:** Replace pin-147 with the actual opinion sentence quoted on the page and verify it against star page 147.

### F-S9-PR-31a08a8516 · quote-fidelity · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Agnello v. United States.json
- **problem:** The quoted passage is the right Agnello passage, but it is not character-faithful to the cached opinion text because the payload uses straight apostrophes where the text has typographic apostrophes.
- **verbatim:** But the right does not extend to other places. Frank Agnello’s
- **tally:** codex-A=stands-modified: The substance of the passage appears in text/Agnello v. United States__20e485.txt at the transition from page *30 to *31.  |  codex-B=refuted: This is a quote-fidelity row; Lens B does not raise support or quote-fidelity findings.  |  opus=stands-modified: Every sentence of the page quote appears verbatim in the cached opinion; the *31 marker falls inside 'Frank Agnello's *31 house', so pincite 30-31 is correct.
- **proposed_fix:** Either mark this as a normalized quote, or update the displayed/lake quote to match the cached text characters for "Agnello’s" and "Alba’s".

### F-S9-PR-d794664111 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Agnello v. United States.json
- **problem:** The pin-30 payload is not a verbatim Agnello opinion quote. It is rendered page/front-matter content beginning with "--- # Agnello v. United States" and ending before the actual Supreme Court sentence at page 30.
- **verbatim:** The right without a search warrant contemporaneously to search persons lawfully arrested while committing crime and to search the place where the arrest is made in order to find and seize things conn…
- **tally:** codex-A=stands: The disclosed cached opinion contains the relevant page-30 sentence, but the payload quote contains content_page markdown, headings, and summary prose rather than opinion text.  |  codex-B=refuted: This is a quote-fidelity row; Lens B does not raise support or quote-fidelity findings.  |  opus=stands-modified: Page pin-30 quote matches the cached opinion verbatim (modulo the cached OCR stray period); pincite 30 correct.
- **proposed_fix:** Replace pin-30 with the actual opinion sentence beginning "The right without a search warrant contemporaneously..." and ending "...is not to be doubted."

### F-S9-PR-750c145f50 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Aguilar v. Texas.json
- **problem:** Pin pin-114 is not a character-faithful quotation from the opinion; it includes page-summary prose and markdown headings from the built page rather than verbatim opinion text.
- **verbatim:** "quote_fidelity": "mismatch"
- **tally:** codex-A=stands: The disclosed lake record itself flags pin-114 as quote_fidelity mismatch.  |  codex-B=refuted: This row makes a quote-fidelity assertion, and Lens B does not raise support or quote-fidelity findings.  |  opus=stands-modified: Page pin-114 quote matches the cached opinion verbatim with one properly-marked internal ellipsis; pincite 114 correct (sentence begins after *114, before *115).
- **proposed_fix:** Replace pin-114 with a verbatim excerpt from the actual 378 U.S. at 114 passage, or keep the surrounding Background/Issue/Rule language as uncited paraphrase rather than a quote pinpoint.

### F-S9-PR-f3505c9ee4 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Arizona v. Fulminante.json
- **problem:** The pin-309 metadata validates only the fragment 'trial error,' at page *291, not the displayed p.309 quotation; the displayed quotation also changes the opinion's internal double quotation marks around trial error.
- **verbatim:** The admission of an involuntary confession\u0097a classic "trial error"\u0097is markedly different from the other two constitutional violations referred to in the Chapman footnote as not being subjec…
- **tally:** codex-A=stands: The inventory payload for pin-309 has star_marker 291, contradicting the page's cited p.309 passage.  |  codex-B=refuted: Quote fidelity is outside Lens B.  |  opus=stands-modified: Quote fidelity survives: the sub-phrase 'trial error,' is verbatim in the opinion, and the full page-309 quoted sentence is verbatim in Rehnquist's majority opinion (em-dashes dropped only in the HTM…
- **proposed_fix:** Retarget pin-309 to the page *309 passage and store the full exact sentence, preserving the opinion's double quotation marks around "trial error".

### F-S9-PR-57fdb73acc · quote-fidelity · sev=low · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Arizona v. Hicks.json
- **problem:** The quoted sentence is substantively present at page 326, but the page/payload use straight single quotes around 'plain view' where the opinion text uses curly double quotation marks.
- **verbatim:** We now hold that probable cause is required. To say otherwise would be to cut the “plain view” doctrine loose from its theoretical and practical moorings.
- **tally:** codex-A=stands-modified: The cited proposition and page location are supported by the cached opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands: Stored quote is a clean quotation matching the content page, but is flagged quote_fidelity=mismatch and the pincite is slip-only.
- **proposed_fix:** Change 'plain view' inside the quote to “plain view” or normalize the quote under an explicit typography-normalization rule.

### F-S9-PR-274a6bd342 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Ashcroft v. al-Kidd.json
- **problem:** pin-736's stored quote is not the opinion passage or the displayed p. 736 quotation; it is harvested content-page Markdown/background text, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** --- # Ashcroft v. al-Kidd *563 U.S. 731 (2011)*
- **tally:** codex-A=stands: Lake pin-736 has quote_fidelity=mismatch, pinpoint_status=slip-only, no page, and no star marker.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is the wiki page's own header/Background/Issue/Rule-intro prose and is not found as an opinion quotation (harvest artifact).
- **proposed_fix:** Replace pin-736 with the actual 563 U.S. at 736 objective-inquiry passage from the cached opinion, preserving quotation characters or not presenting it as verbatim.

### F-S9-PR-7031763b18 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Ashcroft v. al-Kidd.json
- **problem:** The quoted sentence is character-faithful, but the content page's displayed official pincite says Id. at 743 while the cached text places the holding paragraph after the 563 U.S. 744 marker; the lake verifies only the L. Ed. star page 1161.
- **verbatim:** [<span class="citation no-link">563 U.S. 744</span>]
- **tally:** codex-A=stands-modified: The asserted sentence appears verbatim in the cached opinion and matches lake pinpoints[pin-743].quote.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Quote matches the disclosed opinion verbatim; star_marker 1161 is correct because the *1161 L.Ed. break precedes the holding paragraph.
- **proposed_fix:** Change the displayed cite to 563 U.S. at 744 or cite the verified 179 L. Ed. 2d at 1161 unless another disclosed source verifies page 743.

### F-S9-PR-1cac0d5d43 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Atwater v. City of Lago Vista.json
- **problem:** pin-355 is not a character-faithful opinion quote. The stored quote is a content-page fragment with markdown heading text and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** Atwater's arrest satisfied constitutional requirements. There is no dispute that Officer Turek had probable cause to believe that Atwater had committed a crime in his presence.
- **tally:** codex-A=stands: The payload begins '(quoting *Whren v. United States*). ## Application ...', which is not text from the opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is page prose, not a source quotation (harvest artifact).
- **proposed_fix:** Replace pin-355 with the actual opinion passage on the application/ordinary-arrest point, and set the pin to the opinion location around 532 U.S. 354-355.

### F-S9-PR-24b588ae12 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Atwater v. City of Lago Vista.json
- **problem:** pin-354 is not a character-faithful opinion quote. It captured the built page header/background/rule text instead of the Supreme Court opinion passage; the lake marks quote_fidelity as mismatch.
- **verbatim:** Accordingly, we confirm today what our prior cases have intimated: the standard of probable cause "applie[s] to all arrests, without the need to `balance' the interests and circumstances involved in…
- **tally:** codex-A=stands: The payload starts with content-page markdown ('--- # Atwater v. City of Lago Vista') rather than the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is the page's own header/Background/Issue/Rule prose (harvest artifact).
- **proposed_fix:** Replace pin-354 with the opinion passage beginning 'Accordingly, we confirm today...' and anchor it to the *354 star pagination.

### F-S9-PR-4f43472a87 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Banks v. Dretke.json
- **problem:** The asserted pin-691 quote is not an opinion quote at all; it is a pasted fragment of the generated content page header/background/rule text. It does not match the disclosed opinion text for page *691.
- **verbatim:** The evidence at issue must be favorable to the accused, either because it is exculpatory, or because it is impeaching; that evidence must have been suppressed by the State, either willfully or inadve…
- **tally:** codex-A=stands: The payload begins with "--- # Banks v. Dretke" and includes page summary material, which is content_page text, not Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is the page's own header/Background/Issue prose (harvest artifact).
- **proposed_fix:** Replace pin-691's stored quote with the actual page-691 Brady/Strickler components sentence from the opinion text.

### F-S9-PR-8e4f05d35e · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Beckwith v. United States.json
- **problem:** The pin-346 payload quote is not an opinion quote; it contains built-page Markdown text spanning an issue/rule boundary.
- **verbatim:** In subsequent decisions, the Court specifically stressed that it was the <em>custodial </em>nature of the interrogation
- **tally:** codex-A=stands: The asserted quote begins 'of the investigation. ## Rule No — ...', which appears to be content_page Markdown, not language from the cached opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote is spliced page prose (harvest artifact), not a source quotation.
- **proposed_fix:** Replace pin-346 with the actual page-346 opinion language supporting the rule, or remove the verbatim-quote treatment for this pin.

### F-S9-PR-d12f7dc906 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Boyd v. United States.json
- **problem:** The pin-626 stored quote is not opinion text; it is corrupted page prose from the built content page and headings, not a character-faithful quote from Boyd.
- **verbatim:** As every American statesmen, during our revolutionary and formative period as a nation, was undoubtedly familiar with this monument of English freedom, and considered it as the true and ultimate expr…
- **tally:** codex-A=stands: The payload quote begins with built-page language: "to mean — and, in answering" and includes "## Rule"; that language is not in the opinion text.  |  codex-B=refuted: No treatment or currency defect is presented by this pinpoint assertion under lens B.  |  opus=stands-modified: The displayed content-page quote at ^pin-626 is verbatim-faithful to the opinion and correctly located on p.626, so no unsupported legal proposition is published.
- **proposed_fix:** Replace pin-626 with the actual quoted opinion language at 116 U.S. 626, such as: "considered it as the true and ultimate expression of constitutional law"; remove the copied Issue/Rule page prose fr…

### F-S9-PR-6d3ad9afe7 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brady v. Maryland.json
- **problem:** The pin-87 stored quote is not the opinion passage at 373 U.S. 87. It is a block of generated content-page header/background/issue text ending at '## Rule', while the opinion text at *87 contains the actual Brady rule sentence.
- **verbatim:** We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective…
- **tally:** codex-A=stands: The lake pinpoint itself flags quote_fidelity as 'mismatch'.  |  codex-B=refuted: Quote-fidelity is outside lens B; no treatment or currency claim in this assertion is refuted under this review lens.  |  opus=stands-modified: Displayed content-page quote at ^pin-87 matches the opinion verbatim and sits on p.87, so no unsupported proposition is published.
- **proposed_fix:** Replace pin-87's quote with the actual page-*87 opinion sentence beginning 'We now hold...' and set the pinpoint metadata to land on that passage, not on generated page prose.

### F-S9-PR-4299da42e4 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brendlin v. California.json
- **problem:** The stored pinpoint quote for pin-251 is not a faithful quotation from the opinion; it is harvested from the issue text and includes the markdown heading artifact '## Rule'.
- **verbatim:** by a traffic stop, so that he has standing to challenge the constitutionality of the stop. ## Rule
- **tally:** codex-A=stands: The lake record itself marks pin-251 quote_fidelity as mismatch.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Displayed content-page quote at ^pin-251 matches the opinion's opening sentence verbatim, so no unsupported proposition is published.
- **proposed_fix:** Replace pin-251's stored quote with: "When a police officer makes a traffic stop, the driver of the car is seized within the meaning of the Fourth Amendment."

### F-S9-PR-5e21802e7b · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brewer v. Williams.json
- **problem:** pin-398's lake/payload quote is not the quoted rule passage from the opinion. It is a harvested slice of the content page/background/headings, ending before the actual rule quote. The displayed rule quote is substantively supported, but the pinpoint quote record is not character-faithful to the opi…
- **verbatim:** Whatever else it may mean, the right to counsel granted by the Sixth and Fourteenth Amendments means at least that a person is entitled to the help of a lawyer at or after the time that judicial proc…
- **tally:** codex-A=stands: The payload quote begins with 'suggesting the child deserved a Christian burial...' and includes '## Issue'/'## Rule' text, which is not an opinion quote.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Displayed content-page quote at ^pin-398 matches the opinion verbatim (page legitimately starts the quotation at 'the right to counsel', dropping the introductory 'Whatever else it may mean,') and si…
- **proposed_fix:** Replace pin-398's quote with the actual page-398 passage beginning with the Sixth/Fourteenth Amendment right-to-counsel language, and anchor it to page 398. If exact fidelity is required, preserve th…

### F-S9-PR-d01cf7652c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brower v. County of Inyo.json
- **problem:** The reviewed pin-596 quote is not an opinion quote; it concatenates built-page Issue/Rule prose and a Markdown heading, and that exact text does not appear in the cached opinion.
- **verbatim:** but only when there is a governmental termination of freedom of movement <i>through means intentionally applied.</i>
- **tally:** codex-A=stands: The payload includes page-authored text, including '## Rule,' which is not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The real anchored quote is verbatim-faithful (bracketed '[A]' for 'a' at the start of the mid-sentence quotation is a proper capitalization substitution) and crosses the *597 marker, so the content p…
- **proposed_fix:** Replace the pin-596 quote with the actual 596-597 opinion passage supporting the rule, or treat the page's Issue/Rule wording as paraphrase rather than a pinpoint quote.

### F-S9-PR-ac6625eda1 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brown v. Illinois.json
- **problem:** pin-603's stored quote is not an opinion quote; it is a harvested content-page header/background/rule preface and does not appear as the Brown opinion text at page 603.
- **verbatim:** --- # Brown v. Illinois *422 U.S. 590 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading t…
- **tally:** codex-A=stands: The lake pinpoint itself marks quote_fidelity as mismatch and has page/star_marker null.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The real anchored quote is verbatim-faithful and sits on page 603 (between the *603 and *604 markers), so content pincite 603 is correct.
- **proposed_fix:** Replace pin-603 with the actual opinion passage supporting the page's rule quote: "The Miranda warnings are an important factor, to be sure, in determining whether the confession is obtained by explo…

### F-S9-PR-013cf8fcfa · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brown v. Mississippi.json
- **problem:** The pin-286 payload is not a faithful case quote; it is a harvested page/frontmatter-and-summary block ending at the Rule heading, not text from the Brown opinion. The actual content_page pin-286 rule quote is present in the opinion at page *286, but the lake/group assertion for this pin is defecti…
- **verbatim:** And the trial equally is a mere pretense where the state authorities have contrived a conviction resting solely upon confessions obtained by violence.
- **tally:** codex-A=stands: The lake pin-286 quote begins with page metadata and background text rather than an opinion passage.  |  codex-B=refuted: Quote-fidelity is outside Lens B; no support or quote-fidelity finding is made.  |  opus=stands-modified: The real anchored quote is verbatim-faithful and sits on page 286 (between *286 and *287), so content pincite 286 is correct.
- **proposed_fix:** Replace the stored pin-286 quote with the actual rule quote from content_page.md and text/Brown v. Mississippi__89e7f5.txt, and set star_marker to 286 after validation.

### F-S9-PR-0bfa9964b7 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brown v. Texas.json
- **problem:** The pinpoint quote is not an opinion quote; it captures the content page heading/prose instead of the cached opinion text.
- **verbatim:** The application of Tex. Penal Code Ann., Tit. 8, § 38.02 (1974), to detain appellant and require him to identify himself violated the Fourth Amendment because the officers lacked any reasonable suspi…
- **tally:** codex-A=stands: The asserted quote begins with markdown-style content-page text: ## Application The officers had no such basis.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The real anchored quote is verbatim-faithful and sits immediately after the *53 marker, so content pincite 53 is correct.
- **proposed_fix:** Replace pin-53 with the actual page-53 holding quote, or split the factual discussion on page 52 from the holding on page 53.

### F-S9-PR-20623a644c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Brown v. Texas.json
- **problem:** The pin-51 quote is not character-faithful to the opinion text and appears to be generated page prose spanning Background, Issue, and Rule rather than the cited page-51 balancing passage.
- **verbatim:** Consideration of the constitutionality of such seizures involves a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest,…
- **tally:** codex-A=stands: The inventory quote contains markdown headings and content-page prose, including ## Issue and ## Rule, which are not in the cached opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The real anchored quote is verbatim-faithful; the *51 marker falls mid-sentence (after 'involves a') so the operative balancing language is on page 51 and the content pincite 51 is correct.
- **proposed_fix:** Replace pin-51 with the actual page-51 balancing-test sentence from the opinion.

### F-S9-PR-0ddecd3c00 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Bumper v. North Carolina.json
- **problem:** pin-548's stored quote is not the opinion passage for the 548-549 rule quote. It is a generated fragment from the built page background/issue/rule text and does not match the cached opinion text at the cited pages.
- **verbatim:** When a prosecutor seeks to rely upon consent to justify the lawfulness of a search, he has the burden of proving that the consent was, in fact, freely and voluntarily given.<sup>[12]</sup> This burde…
- **tally:** codex-A=stands: The payload quote begins 'and let them in...' and includes markdown headings '## Issue' and '## Rule No.', which are not the opinion's quoted rule passage.  |  codex-B=refuted: This is a quote-fidelity assertion; Lens B reviews only currency, treatment, and authority weight.  |  opus=stands-modified: Stored quote text is corrupt (a harvest slip capturing page prose + '## Issue'/'## Rule' markers), so the pinpoint record itself is defective.
- **proposed_fix:** Replace lake pinpoints[pin-548].quote with the actual 548-549 rule passage beginning 'When a prosecutor seeks to rely upon consent...' and remove the generated content-page fragment.

### F-S9-PR-59af9e80ee · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Byars v. United States.json
- **problem:** The pin-29 payload is not an opinion quotation; it is harvested content-page prose spanning Background, Issue, and Rule, and it omits the actual warrant sentence cited on the page.
- **verbatim:** The warrant clearly is bad
- **tally:** codex-A=stands: The disclosed opinion text at the page-29 passage contains the warrant sentence, not the inventory payload's content-page narrative.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Stored quote text is a harvest slip capturing surrounding page prose + '## Issue'/'## Rule' markers, so the pinpoint record is defective.
- **proposed_fix:** Replace pin-29's stored quote with the opinion sentence at star page 29, and keep the page citation to 273 U.S. at 29.

### F-S9-PR-78571f5750 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/California v. Carney.json
- **problem:** The pin-392 pinpoint record is not quote-faithful: its stored quote is generated content-page/header material, not the cited opinion passage at 471 U.S. 392, and the lake itself marks quote_fidelity as mismatch with no star_marker, fragment, or position.
- **verbatim:** --- # California v. Carney *471 U.S. 386 (1985)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
- **tally:** codex-A=stands: The inventory/lake quote for pin-392 begins with page metadata rather than opinion text.  |  codex-B=refuted: Quote fidelity is outside lens B; this row presents no independent currency or treatment defect.  |  opus=stands-modified: The legal proposition survives: the content-page quote at pin-392 matches cached b462-6 verbatim and the *392 star-page is correct.
- **proposed_fix:** Rebuild pin-392 from the opinion text at *392, using the actual rule sentence beginning after 'In short,' and set a verified page/star marker or remove the pinpoint until verified.

