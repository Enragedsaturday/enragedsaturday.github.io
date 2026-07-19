# P2 ESCALATE PACKET 09/12

_findings: 25 | classes: quote-fidelity=25_

### F-S9-PR-0df5e15a60 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/State v. Mitcham.json
- **problem:** The stored pin-34 quote is not the opinion text at ¶34; it is a harvested chunk of the built content page beginning with front matter and page prose.
- **verbatim:** ¶34 The “independent source” exception permits the admission of evidence discovered during or because of an unlawful search if the evidence was also obtained independently from activities that were t…
- **tally:** codex-A=stands: The payload quote begins '--- # State v. Mitcham' and includes content-page sections, which cannot be a verbatim opinion quotation.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The payload quote for pin-34 is page-header boilerplate (same systematic first-block harvest bug seen across the pack), which does not appear in the opinion.
- **proposed_fix:** Replace pin-34 with the actual ¶34 quote from the cached opinion.

### F-S9-PR-0a295c44be · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/State v. Tarantino.json
- **problem:** The pin-591 quote is not an opinion quotation; it reproduces built-page markdown/header material and generated summaries instead of verbatim Tarantino text.
- **verbatim:** This expectation was not unreasonable even though there were small cracks between the boards in the building’s back wall. The presence of tiny cracks near the floor on the interior wall of a second-f…
- **tally:** codex-A=stands: The disclosed opinion text contains no markdown title, Background, Issue, or Rule block like the asserted quote.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload quote for pin-591 is page-header boilerplate (same systematic first-block harvest bug), not opinion text.
- **proposed_fix:** Replace pin-591 with the exact opinion passage beginning This expectation was not unreasonable even though there were small cracks between the boards in the building’s back wall.

### F-S9-PR-cd16c94050 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/State v. Volle.json
- **problem:** The stored pin-13 quote is not a verbatim opinion passage; it is a harvested chunk of the built page/header/prose, while the opinion text at the claimed slip-page passage contains the narrower Burgess sentence about digital-device search methods.
- **verbatim:** Because relevant information may be stored anywhere on such a device, it is ordinarily impractical—and sometimes impossible—for a warrant to prescribe in advance how officers must locate that data.
- **tally:** codex-A=stands: The lake quote for pin-13 begins with "--- # State v. Volle" and includes content-page sections, not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload quote for pin-13 is page-header boilerplate (same systematic first-block harvest bug), not opinion text.
- **proposed_fix:** Replace pin-13's stored quote with the actual quoted sentence from the opinion: "Because relevant information may be stored anywhere on such a device, it is ordinarily impractical—and sometimes impos…

### F-S9-PR-e534ddf08f · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Stoner v. California.json
- **problem:** The pinpoint quote is a malformed splice of page content, not a verbatim passage from the opinion text.
- **verbatim:** a guest in a hotel room is entitled to constitutional protection against unreasonable searches and seizures. That protection would disappear if it were left to depend upon the unfettered discretion o…
- **tally:** codex-A=stands: The payload includes markdown headings such as "## Issue" and "## Rule," which are not in the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The genuine content-page quote at ^pin-490 is verbatim-faithful to 376 U.S. at 490 and correctly pincited; the defect is confined to the inventory's captured quote string, not the wiki page.
- **proposed_fix:** Replace the payload quote with the actual page-490 passage beginning "No less than a tenant..." and ending with the hotel-employee discretion sentence.

### F-S9-PR-6f90161a47 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Stovall v. Denno.json
- **problem:** pin-302's lake quote is not a judicial-opinion excerpt; it is a harvested chunk of the built page/header and stops before the claimed opinion quotation. The page's displayed pin-302 quotation also is not character-faithful to the cached opinion because it uses 'conducive' where the disclosed opinio…
- **verbatim:** the confrontation conducted in this <span class="star-pagination">*302</span> case was so unnecessarily suggestive and conductive to irreparable mistaken identification that he was denied due process…
- **tally:** codex-A=stands: The payload quote begins with built-page material ('--- # Stovall v. Denno') rather than the Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Genuine page quote at ^pin-302 is faithful to 388 U.S. at 302 and correctly pincited; the defect is confined to the inventory payload string, not the page.
- **proposed_fix:** Replace pin-302 with the actual page-*302 opinion passage and align the content-page quotation to the disclosed text, preserving the cached wording or otherwise verifying any normalization from an of…

### F-S9-PR-ff5e091ced · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/Strickler v. Greene.json
- **problem:** The stored quote for pin-281 is not a quote from the opinion passage. It is copied from the generated content page header/background/rule prose, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** There are three components of a true <i><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span></…
- **tally:** codex-A=stands: The payload quote begins with content-page material, not opinion text: "--- # Strickler v. Greene ... ## Background ... ## Rule".  |  codex-B=refuted: Lens B does not adjudicate quote support or quote-fidelity defects.  |  opus=stands-modified: Genuine page quote at ^pin-281 is verbatim-faithful; the *282 star falls after 'favorable to the accused,' so the 281-282 span pincite is correct.
- **proposed_fix:** Replace pin-281's stored quote with the actual three-components passage from the opinion and keep the pin at 527 U.S. 281-282.

### F-S9-PR-ff655ddce8 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Agurs.json
- **problem:** The lake/inventory quote for pin-108 is not an opinion quote. It is a harvested chunk of the built content page beginning with the page title and background material, while the actual 427 U.S. at 108 quote is a separate sentence in the opinion text.
- **verbatim:** the prosecutor will not have violated his constitutional duty of disclosure unless his omission is of sufficient significance to result in the denial of the defendant's right to a fair trial.
- **tally:** codex-A=stands: Lake pinpoints[id=pin-108] has quote_fidelity='mismatch', pinpoint_status='slip-only', star_marker=null, and position=null.  |  codex-B=refuted: Lens B only: quote-fidelity mismatch/slip-only status is not a treatment/currency defect for this panel.  |  opus=stands-modified: Honest stub handling: the delivered payload is a broken extraction (markdown, not a quote), so the assertion is not verifiable as-framed — verifiable_from_disclosed=false.
- **proposed_fix:** Replace lake pinpoints[id=pin-108].quote with the actual quoted sentence from the opinion, set star_marker to 108, and mark quote_fidelity matched only after validating against the cached opinion tex…

### F-S9-PR-9edaf343c5 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Anchondo.json
- **problem:** The recorded pin-1045 quote is not character-faithful to the opinion. It reproduces built-page header/background material and stops before the actual quoted rule. The visible page quote also changes the opinion's curly double quotation marks around “search incident to arrest” into straight single q…
- **verbatim:** A warrantless search preceding an arrest is a legitimate “search incident to arrest” as long as (1) a legitimate basis for the arrest existed before the search, and (2) the arrest followed shortly af…
- **tally:** codex-A=stands: The lake pinpoints entry for pin-1045 begins with built-page markdown, not the opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B's charter.  |  opus=stands-modified: Stored payload.quote is page markdown, not opinion text -> genuine data-hygiene defect (same 'garbled lead-in capture' pattern as pin-273 and pin-321).
- **proposed_fix:** Replace the pin-1045 quote payload with the exact opinion sentence and preserve the opinion punctuation.

### F-S9-PR-dd252d893c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Arvizu.json
- **problem:** Pin-273's stored quote is not the quoted Arvizu opinion passage. It is an accidental scrape of the content page/header/background text ending before the actual quoted rule language, and the lake marks it as quote_fidelity mismatch.
- **verbatim:** "--- # United States v. Arvizu"
- **tally:** codex-A=stands: The lake pin-273 quote begins with content-page markup rather than opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Same garbled lead-in capture pattern as pin-1045 and pin-321; stored quote is page markdown, not opinion text -> data-hygiene defect.
- **proposed_fix:** Replace pin-273 with the actual opinion passage supporting the rule at page 273, preserving the opinion's quotation marks exactly or marking the quote as normalized. Then rerun fidelity and position/…

### F-S9-PR-243ada4636 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Ash.json
- **problem:** The pin-321 stored quote is not the opinion passage; it is a malformed excerpt from the built content page/front matter and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** We hold, then, that the Sixth Amendment does not grant the right to counsel at photographic displays conducted by the Government for the purpose of allowing a witness to attempt an identification of…
- **tally:** codex-A=stands: The payload quote begins with the content page header rather than opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Same garbled lead-in capture pattern as pin-1045 and pin-273; stored quote is page markdown, not opinion text -> data-hygiene defect.
- **proposed_fix:** Replace pin-321's quote with the actual opinion passage at 413 U.S. 321, or remove the malformed pin evidence. The page's displayed holding quote is supported by the cached opinion text.

### F-S9-PR-6dfa696c0d · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. August.json
- **problem:** pin-op5's stored quote is not an opinion quote; it is harvested content-page/frontmatter prose ending before the actual quoted rule. The lake record itself marks quote_fidelity as mismatch.
- **verbatim:** A protective sweep is lawful if:
- **tally:** codex-A=stands: The payload quote begins with page markup/content-page text: "--- # United States v. August *136 F.4th 595..." rather than text from the opinion.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The DISPLAYED quotation anchored at ^pin-op5 (the four-part test) is verbatim faithful to the opinion at slip op. 5, including the bracketed '[or curtilage]' insertion which the opinion itself contai…
- **proposed_fix:** Re-harvest pin-op5 so the stored quote is the actual rule passage from slip opinion page 5 beginning with “A protective sweep is lawful if:” or remove the pinpoint until corrected.

### F-S9-PR-fe42ad2c5a · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Bagley.json
- **problem:** The stored pin-682 quote is not the opinion passage at 473 U.S. 682; it is a harvested content-page fragment beginning with the page title and background text, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** The evidence is material only if there is a reasonable probability that, had the evidence been disclosed to the defense, the result of the proceeding would have been different. A “reasonable probabil…
- **tally:** codex-A=stands: The lake pinpoint quote begins with generated page material: "--- # United States v. Bagley...", not with opinion text.  |  codex-B=refuted: Lens B does not evaluate quote/support fidelity; currency embedded in the quoted page header matches the lake treatment good_law as of 2026-06-30.  |  opus=stands-modified: The DISPLAYED quotation anchored at ^pin-682 is verbatim faithful to Bagley at 473 U.S. 682 (cached opinion, paragraph b720-5).
- **proposed_fix:** Replace pin-682 with the actual opinion passage at page 682 and make the quoted text character-faithful to text/United States v. Bagley__6c76f5.txt.

### F-S9-PR-23153b2a18 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Banks.json
- **problem:** The reviewed pin-38 quote/pinpoint is not character-faithful to the opinion. It captures background/page prose and Markdown headings rather than the page-38 quoted sentence in the opinion; the lake record also flags quote_fidelity as mismatch.
- **verbatim:** we think that after 15 or 20 seconds without a response, police could fairly suspect that cocaine would be gone if they were reticent any longer.
- **tally:** codex-A=stands: The payload quote includes content-page material such as ## Issue and ## Rule, which is not opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The DISPLAYED quotation anchored at ^pin-38 is verbatim faithful to Banks at 540 U.S. 38 (cached opinion, the star-38 paragraph).
- **proposed_fix:** Replace pin-38's stored quote with the exact page-38 opinion sentence used in content_page, or regenerate the lake pinpoint from the opinion text.

### F-S9-PR-4cd37053e5 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Cano.json
- **problem:** The pin-op5 payload quote is not a verbatim excerpt from the Cano opinion; it is a corrupted scrape of the built page header/background/rule lead-in. The built page's displayed quote is substantively supported by slip page 5, but it is not character-faithful because it adds Markdown italics around…
- **verbatim:** We clarify Cotterman by holding that “reasonable suspicion” in this context means that officials must reasonably suspect that the cell phone contains digital contraband.
- **tally:** codex-A=stands: The lake pin-op5 quote reproduces content_page.md prose beginning with the page header, not the opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: The pin-op5 stored quote is a garbled page-dump, not a quotation from the opinion (a genuine quote_fidelity failure the build itself flagged 'mismatch').
- **proposed_fix:** Replace pin-op5 with the exact slip-page-5 opinion quote and remove quote-internal Markdown styling or altered quotation marks from the built page.

### F-S9-PR-93b0e95853 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Carloss.json
- **problem:** The asserted quote is not a character-faithful opinion quote and includes the Markdown heading '## Rule'; it appears to splice page Issue text with a heading. Lake pinpoints[] marks the quote as mismatch.
- **verbatim:** Carloss, however, claims that “No Trespassing” signs posted around the house
- **tally:** codex-A=stands: The payload contains '## Rule', which is page markup rather than opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: pin-op1 stored quote is a garbled page-dump (Issue prose + '## Rule' heading), a genuine quote_fidelity failure.
- **proposed_fix:** Remove the contaminated pin text, and if pin-op1 is retained, replace it with the actual quoted sentences from paragraph b1034-6.

### F-S9-PR-66558cc11c · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Ceccolini.json
- **problem:** pin-280's stored quote is not an opinion quote; it is built-page markdown/frontmatter prose and the lake itself marks it quote_fidelity=mismatch and pinpoint_status=slip-only. The actual rule sentence at page *280 exists in the opinion text but is not the stored pin-280 quote.
- **verbatim:** the exclusionary rule should be invoked with much greater reluctance where the claim is based on a causal relationship between a constitutional violation and the discovery of a live witness than when…
- **tally:** codex-A=stands: The payload quote begins with built-page material ('--- # United States v. Ceccolini') rather than language from the opinion.  |  codex-B=refuted: No currency or treatment defect is raised under Lens B for this quote-fidelity row.  |  opus=stands-modified: The stored 'quote' is a page-harvest blob that appears nowhere in the opinion, confirming the record's own mismatch flag.
- **proposed_fix:** Replace pin-280 with the actual page-*280 sentence from the opinion text. For strict quote fidelity, start the quoted fragment with lowercase 'the' rather than '[T]he', or avoid beginning the sentenc…

### F-S9-PR-fef7347dbe · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Chadwick.json
- **problem:** The pin-11 payload is not an opinion quote. It is harvested page/frontmatter and content-page prose ending before the actual quoted Chadwick passage, while the cached opinion text contains the real page-11 passage separately.
- **verbatim:** By placing personal effects inside a double-locked footlocker, respondents manifested an expectation that the contents would remain free from public examination.
- **tally:** codex-A=stands: The lake pinpoints entry for pin-11 is marked quote_fidelity=mismatch and pinpoint_status=slip-only.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity or the malformed harvested quote.  |  opus=stands-modified: The stored 'quote' is a page-harvest blob absent from the opinion, confirming the record's own mismatch flag.
- **proposed_fix:** Replace the pin-11 lake quote with the actual opinion passage quoted on the content page and validate it against the cached opinion text at page *11.

### F-S9-PR-504211673c · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Classic.json
- **problem:** The reviewed pin-326 quote is not a verbatim passage from the opinion; it is a stitched excerpt from the page's Issue/Rule prose, and the lake itself marks quote_fidelity as mismatch.
- **verbatim:** Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is action taken 'under color of' state law.
- **tally:** codex-A=stands: The payload quote begins 'state law for purposes...' and contains '## Rule', which is generated page prose rather than opinion text.  |  codex-B=refuted: Quote fidelity is outside Lens B; I make no support or quote-fidelity finding.  |  opus=stands-modified: The page's Rule quote matches the cached opinion verbatim (cached passage: 'Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authorit…
- **proposed_fix:** Replace pin-326 quote with the actual opinion sentence: Misuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law, is a…

### F-S9-PR-228c5f6a78 · quote-fidelity · sev=medium · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Conner.json
- **problem:** The pin-666 lake quote is not an opinion quote; it is a corrupted harvest from the content page that includes Markdown section headings and surrounding page prose. The lake itself marks quote_fidelity as mismatch.
- **verbatim:** and that the occupant opened the door not voluntarily but in response to their show of authority. ## Issue Whether police obtain lawful, consensual access to a motel room when an occupant opens the d…
- **tally:** codex-A=stands: The disclosed lake pinpoint for pin-666 has quote_fidelity: mismatch.  |  codex-B=refuted: Quote fidelity is outside Lens B, so no support or quote-fidelity defect is raised here.  |  opus=stands-modified: The page's Rule quote matches the cached opinion verbatim (cached text: 'an unconstitutional search occurs when officers gain visual or physical access to a motel room after an occupant opens the doo…
- **proposed_fix:** Replace pin-666's stored quote with the actual opinion passage at page 666, or at least with the exact quoted sentence used in the Rule section, and remove the harvested Markdown headings.

### F-S9-PR-50df7fadd0 · quote-fidelity · sev=high · needs_cl=true · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Dunn.json
- **problem:** The pin-301 payload/lake quote is not the opinion passage at 480 U.S. 301; it is generated page text beginning with the page header and background. The lake record itself flags quote_fidelity as mismatch.
- **verbatim:** curtilage questions should be resolved with particular reference to four factors
- **tally:** codex-A=stands: The disclosed opinion text at page 301 contains the four-factor curtilage passage, not the header/background text in the payload.  |  codex-B=refuted: Lens B does not adjudicate quote-fidelity defects; no independent currency or treatment defect is created by this row.  |  opus=stands-modified: Rendered quote at ^pin-301 ('curtilage questions should be resolved with particular reference to four factors...') is verbatim in the opinion at *301; pincite 301 correct.
- **proposed_fix:** Replace pin-301 with the actual 480 U.S. at 301 curtilage-factors passage or re-extract the pinpoint from the cached opinion text.

### F-S9-PR-ed63cc25f7 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Edwards.json
- **problem:** The stored pin-803 quote is corrupted: it contains built-page markdown/header/background text and stops before the actual opinion passage used for the 803 rule quote.
- **verbatim:** searches and seizures that could be made
- **tally:** codex-A=stands: The payload quote begins with page content rather than the Supreme Court opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Rendered quote at ^pin-803 ('that could be made on the spot at the time of arrest may legally be conducted later when the accused arrives at the place of detention') is verbatim at *802-803; pincite…
- **proposed_fix:** Replace pin-803's stored quote with the actual opinion passage at page 803, or with the visible page quote that is supported by the opinion text.

### F-S9-PR-0c472c9630 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Evans.json
- **problem:** The asserted pin quote is not a verbatim passage from the opinion. It is a harvested block of content-page prose and Markdown headings, ending before the actual quoted holding.
- **verbatim:** Accordingly, we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search, and the evidence discovered subsequently (pursuant to valid search warrants) was not th…
- **tally:** codex-A=stands: The asserted quote contains phrases such as '## Issue' and '## Rule', which are not opinion text.  |  codex-B=refuted: Lens B does not adjudicate quote fidelity or support, and this row embeds no separate currency/treatment claim.  |  opus=stands-modified: Rendered quote at ^pin-1539 ('we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search... was lawfully obtained') is verbatim at *1539 (page drops leading 'Ac…
- **proposed_fix:** Replace pin-1539's stored quote with the actual holding passage from the opinion, e.g. 'Accordingly, we hold the search conducted at the bus station of the carry-on bag was a lawful inventory search,…

### F-S9-PR-b6f7ba318b · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Flores-Montano.json
- **problem:** The lake pinpoint quote for pin-150 is not the opinion passage; it is a capture of the generated page header/background/rule text and omits the actual quoted holding sentence.
- **verbatim:** did not require reasonable suspicion.
- **tally:** codex-A=stands: The disclosed opinion text contains the holding sentence at star page 150.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Rendered quote at ^pin-150 ('We hold that the search in question did not require reasonable suspicion.') is verbatim in the opinion's opening paragraph; pincite 150 defensible.
- **proposed_fix:** Replace pin-150's pinpoint quote with the actual holding sentence from star page 150 and re-run quote validation.

### F-S9-PR-5aa46d8604 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Garner.json
- **problem:** The pin-1213 quote in the lake/payload is not an opinion quote; it is a harvested chunk of the built content page beginning with page markup and background text.
- **verbatim:** community caretaking detention must be based upon “‘specific and articulable facts which . . . reasonably warrant [an] intrusion’ into the individual’s liberty.”
- **tally:** codex-A=stands: The payload quote begins with built-page markup, not the Garner opinion text.  |  codex-B=refuted[backfill]: quorum backfill: lane verdict projected from persisted panel-result verdict map  |  opus=stands-modified: Payload 'quote' is page-structural text (front-matter through Rule intro), not a quotation, so it cannot be verified as a faithful quote as-framed.
- **proposed_fix:** Replace pin-1213 with the actual opinion passage supporting the articulable-facts rule.

### F-S9-PR-24292273c6 · quote-fidelity · sev=high · needs_cl=false · quorum=3/3
- **object:** _overhaul2/lake/cases/United States v. Gastiaburo.json
- **problem:** The pin-585 payload quote is not an opinion quote; it is a large excerpt from the built content page and stops before the cited 'is clearly correct' language. It is not character-faithful to the cached opinion text.
- **verbatim:** The third argument, based on the “automobile exception” to the warrant requirement, is clearly correct.
- **tally:** codex-A=stands: The lake pinpoint for pin-585 is marked quote_fidelity mismatch and slip-only.  |  codex-B=refuted: Quote fidelity is outside lens B, so no support or text-match finding is made.  |  opus=stands-modified: Payload 'quote' is page-structural text (front-matter through Rule intro), not a quotation, so it cannot be verified as a faithful quote as-framed.
- **proposed_fix:** Replace pin-585 with the actual p.585 opinion sentence or the narrower quoted phrase used on the page.

