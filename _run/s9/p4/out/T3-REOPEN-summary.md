# T3-REOPEN — R11 class-reopen sweep: unprovenanced bound-volume pincites on slip-only cases

**Packet:** T3-REOPEN  **WS:** SMP  **Lane/model:** T3-REOPEN / claude-opus-4-8  **Branch:** overhaul2/execute  **Findings-only (no content/lake/ledger edits).**

Triggered by the failed Lange T3 sample: `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md` asserts bound-volume pinpoints "594 U.S. at 313" and "594 U.S. 295, 303–04" for *Lange v. California*, but the lake treats Lange's pinpoints as slip-only and the lead-opinion cache (op 4698186) is a slip opinion with **no star pagination**, so the printed interior pages are unverifiable and no sanctioned pin source is recorded. This sweep generalizes that defect class across the corpus.

## Result headline

- **162 UNPROVENANCED bound-pin assertions filed** (class `t3-unprovenanced-pin`, severity medium, needs_cl=true) across **59 slip-only SCOTUS cases**.
- The Lange trigger is reproduced as **6 rows** (Exigent Circumstances lines 47/48/50/133×2 + a previously-unflagged **298** interior pin on `seizures/arrests/Arrest in the Home.md:120`).
- 124/162 rows carry a joined `assertion_id` from `_run/s9/assertion-inventory.json`.

## Method (mechanical, cache-only, no live CL)

1. **Oracle = cache star pagination.** For every lake case I read the lead-opinion text cache `~/cssi-lake/cache/text/<opinion_id>.txt` and detected page-break star markers (`class="star-pagination">*NNN`, `<page-num label="NNN">`). A case whose cache has **zero** such markers cannot substantiate any interior printed-page pincite. (Validated: King *462, Welsh *753, Santana *43, Agnello *30 all PRESENT ⇒ provenanced; Lange, Riley, Jardines, Brigham City, Herring, McNeely, Hudson, Brendlin all ABSENT on caches of 25k–101k chars ⇒ slip-only.) The lake `pinpoints[].star_marker` field is an incomplete record (e.g. King/Santana/Agnello read star_verified=False in the lake yet their caches are fully star-paginated), so the **cache**, not the lake field, is the provenance authority.
2. **Slip-only enumeration (set S).** Union of the two literal criteria + the operative cache oracle:
   - **A** `citations.slip_only==true`: **14** cases (all recent 2024–2026 slip / lower-court).
   - **B** `citations.official==null` with U.S.-reporter-era SCOTUS identity: **65** cases.
   - **C** U.S./SCOTUS identity + **cache has no star pagination** (the Lange class): **102** cases.
   - **Union |S| = 158** slip-only U.S.-reporter cases (1 cache-missing). Of 524 U.S./SCOTUS-identity cases, 422 have star-paginated caches (bound pins provenanceable) and 158 do not.
3. **Content scan.** All 724 `content/**/*.md` files scanned for bound-volume U.S.-reporter interior pincites in three forms: `AT` ("V U.S. at P"), `STR` ("V U.S. F, P"), `PINNOTE` (source-note `(pinpoint[s]: …)` attached to a `V U.S.` cite). Non-U.S. reporters (F.3d/F.4th/S.Ct./state) and slip-op pinnotes ("slip op., at N") are out of scope and excluded. Each pincite is attributed to a case by exact (vol,first-page) match, then volume-unique, name-agrees-with-volume, case-page filerid, and pin-in-page-range disambiguation. First-page cites (pin==official first page) are not interior and are dropped as FALSE-POSITIVE.
4. **Classify** each interior pincite: PROVENANCED (pin present as a cache star page), UNPROVENANCED (resolved case is slip-only per the oracle — filed), STAR-MISS (case IS star-paginated but the pin is outside the cached star range — out of scope, see caveats), UNRESOLVED, FALSE-POSITIVE.

## Coverage accounting (deterministic)

| stage | count |
|---|---|
| lake case files enumerated for slip-only status | 668 / 668 |
| content `.md` files scanned | 724 / 724 |
| slip-only U.S.-reporter cases (set S) identified | 158 |
| &nbsp;&nbsp;— of S, cited with ≥1 bound interior U.S. pincite (defective) | 59 |
| &nbsp;&nbsp;— of S, no bound interior pincite in content (clean: first-page/slip-op only) | 99 |
| bound-volume interior U.S. pincite hits examined | 1671 |
| &nbsp;&nbsp;PROVENANCED (cache star page confirms pin) | 1452 |
| &nbsp;&nbsp;**UNPROVENANCED → filed** (deduped) | **162** |
| &nbsp;&nbsp;STAR-MISS (star-paginated case, pin outside cached range — NOT filed) | 41 |
| &nbsp;&nbsp;FALSE-POSITIVE (pin == official first page — NOT filed) | 8 |
| &nbsp;&nbsp;UNRESOLVED (volume-collision, un-attributable — NOT filed, see residue) | 7 |

**Nothing silently truncated.** Every hit is in one of the five buckets above; the three not-filed buckets are itemized (STAR-MISS reason below; FALSE-POSITIVE = first-page cites; UNRESOLVED listed individually).

## Enumeration / classification — the 58 defective slip-only cases

Each row: bound-pin count, the specific pins asserted, slip-only basis, opinion id (cache had 0 star markers).

| # | case | us cite | basis | pins asserted (files:lines) | #rows |
|---|---|---|---|---|---|
| 1 | Riley v. California | 573 U.S. 373 | C: cache-no-star | 386, 387, 393–403, 403 | 13 |
| 2 | Florida v. Jardines | 569 U.S. 1 | B: official==null | 10, 6, 7, 8, 9 | 11 |
| 3 | Brigham City v. Stuart | 547 U.S. 398 | C: cache-no-star | 400, 404 | 8 |
| 4 | Herring v. United States | 555 U.S. 135 | C: cache-no-star | 144 | 6 |
| 5 | Lange v. California | 594 U.S. 295 | C: cache-no-star | 298, 303, 303–04, 313 | 6 |
| 6 | Brendlin v. California | 551 U.S. 249 | C: cache-no-star | 251 | 5 |
| 7 | Carroll v. United States | 267 U.S. 132 | C: cache-no-star | 149, 153, 153–56 | 5 |
| 8 | Hudson v. Michigan | 547 U.S. 586 | C: cache-no-star | 594 | 5 |
| 9 | Missouri v. McNeely | 569 U.S. 141 | B: official==null | 156 | 5 |
| 10 | Cone v. Bell | 556 U.S. 449 | C: cache-no-star | 469, 470 | 4 |
| 11 | Messerschmidt v. Millender | 565 U.S. 535 | C: cache-no-star | 547 | 4 |
| 12 | Ryburn v. Huff | 565 U.S. 469 | C: cache-no-star | 476, 477 | 4 |
| 13 | Samson v. California | 547 U.S. 843 | C: cache-no-star | 852, 857 | 4 |
| 14 | United States v. Grubbs | 547 U.S. 90 | C: cache-no-star | 96, 99 | 4 |
| 15 | Arizona v. Johnson | 555 U.S. 323 | C: cache-no-star | 326, 327 | 3 |
| 16 | Birchfield v. N. Dakota. William Robert Bernard | 579 U.S. 438 | C: cache-no-star | 474 | 3 |
| 17 | Fernandez v. California | 571 U.S. 292 | B: official==null | 303 | 3 |
| 18 | Florida v. Harris | 568 U.S. 237 | C: cache-no-star | 244, 244–48, 248 | 3 |
| 19 | Georgia v. Randolph | 547 U.S. 103 | C: cache-no-star | 120 | 3 |
| 20 | Heien v. North Carolina | 574 U.S. 54 | B: official==null | 60, 61 | 3 |
| 21 | Kingsley v. Hendrickson | 576 U.S. 389 | B: official==null | 396, 396–397 | 3 |
| 22 | Montejo v. Louisiana | 556 U.S. 778 | C: cache-no-star | 797 | 3 |
| 23 | Plumhoff v. Rickard | 572 U.S. 765 | B: official==null | 777 | 3 |
| 24 | Prado Navarette v. California | 572 U.S. 393 | B: official==null | 398, 398–99 | 3 |
| 25 | Rothgery v. Gillespie County | 554 U.S. 191 | B: official==null | 213 | 3 |
| 26 | Chavez v. Martinez | 538 U.S. 760 | C: cache-no-star | 766, 767 | 2 |
| 27 | District of Columbia v. Wesby | 583 U.S. 48 | C: cache-no-star | 60, 60–61 | 2 |
| 28 | Florida v. Powell | 559 U.S. 50 | C: cache-no-star | 60, 62 | 2 |
| 29 | Gonzalez v. Trevino | 602 U.S. 653 | C: cache-no-star | 658 | 2 |
| 30 | Gutierrez v. Saenz | 606 U.S. 305 | C: cache-no-star | 314 | 2 |
| 31 | Mullenix v. Luna | 577 U.S. 7 | B: official==null | 12 | 2 |
| 32 | Pearson v. Callahan | 555 U.S. 223 | C: cache-no-star | 236 | 2 |
| 33 | Rodriguez v. United States | 575 U.S. 348 | B: official==null | 350, 350–51 | 2 |
| 34 | Scott v. Harris | 550 U.S. 372 | C: cache-no-star | 386 | 2 |
| 35 | United States v. Classic | 313 U.S. 299 | C: cache-no-star | 326 | 2 |
| 36 | Utah v. Strieff | 579 U.S. 232 | B: official==null | 241 | 2 |
| 37 | Barnes v. Felix | 605 U.S. 73 | C: cache-no-star | 80 | 1 |
| 38 | Bobby v. Dixon | 565 U.S. 23 | C: cache-no-star | 31 | 1 |
| 39 | Carroll v. Carman | 574 U.S. 13 | C: cache-no-star | 18 | 1 |
| 40 | Chiaverini v. City of Napoleon | 602 U.S. 556 | C: cache-no-star | 562 | 1 |
| 41 | Corley v. United States | 556 U.S. 303 | C: cache-no-star | 309 | 1 |
| 42 | Culley v. Marshall | 601 U.S. 377 | C: cache-no-star | 381 | 1 |
| 43 | Dupree v. Younger | 598 U.S. 729 | C: cache-no-star | 733 | 1 |
| 44 | Egbert v. Boule | 596 U.S. 482 | C: cache-no-star | 491 | 1 |
| 45 | FBI v. Fikre | 601 U.S. 234 | C: cache-no-star | 241 | 1 |
| 46 | Florence v. Board of Chosen Freeholders of County of Burlington | 566 U.S. 318 | C: cache-no-star | 326 | 1 |
| 47 | Hernandez v. Mesa | 589 U.S. 93 | C: cache-no-star | 99 | 1 |
| 48 | Kansas v. Ventris | 556 U.S. 586 | C: cache-no-star | 594 | 1 |
| 49 | Lackey v. Stinnie | 604 U.S. 192 | C: cache-no-star | 204 | 1 |
| 50 | Los Angeles County, California v. Rettele | 550 U.S. 609 | B: official==null | 614 | 1 |
| 51 | Martin v. United States | 605 U.S. 395 | C: cache-no-star | 409 | 1 |
| 52 | Maryland v. King | 569 U.S. 435 | B: official==null | 465 | 1 |
| 53 | McNabb v. United States | 318 U.S. 332 | C: cache-no-star | 345 | 1 |
| 54 | Nieves v. Bartlett | 587 U.S. 391 | C: cache-no-star | 406 | 1 |
| 55 | Perttu v. Richards | 605 U.S. 460 | C: cache-no-star | 468 | 1 |
| 56 | Rehberg v. Paulk | 566 U.S. 356 | C: cache-no-star | 369 | 1 |
| 57 | SAUCIER v. KATZ Et Al. | 533 U.S. 194 | C: cache-no-star | 201 | 1 |
| 58 | Virginia v. Moore | 553 U.S. 164 | C: cache-no-star | 168 | 1 |
| 59 | Ziglar v. Abbasi | 582 U.S. 120 | C: cache-no-star | 135 | 1 |

## The Lange trigger (6 filed rows)

- `content/seizures/arrests/Arrest in the Home.md:120` [PINNOTE] — pin **298** — "- [*Lange v. California*, 594 U.S. 295 (2021)](https://www.courtlistener.com/opinion/4894407/lange-v-californi…"
- `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:47` [AT] — pin **303** — "| Hot pursuit of a fleeing **felony** suspect follows across the threshold | **Good law**, with *[[Lange v. Ca…"
- `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:48` [STR] — pin **313** — "| Broad reading: **any** fleeing-suspect pursuit is a categorical exigency that crosses the threshold | **Limi…"
- `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:50` [STR] — pin **313** — "*[[Lange v. California|Lange]]* holds that "pursuit of a fleeing misdemeanor suspect" does not "categorically …"
- `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:133` [PINNOTE] — pin **303–04** — "- [*Lange v. California*, 594 U.S. 295 (2021)](https://www.courtlistener.com/opinion/4894407/lange-v-californi…"
- `content/warrant-exceptions/home-entry-and-search/Exigent Circumstances and Hot Pursuit.md:133` [PINNOTE] — pin **313** — "- [*Lange v. California*, 594 U.S. 295 (2021)](https://www.courtlistener.com/opinion/4894407/lange-v-californi…"

Lange's own case page (`content/cases/Lange v. California.md`) correctly cites *slip op., at 1* and records "pinpoint given as slip-opinion page" — so the defect is the **doctrine/table pages** promoting slip pins to bound-volume pins. The Exigent-Circumstances sources note claims provenance "bound-volume pins per S7 research annex §11", but (a) no such annex records bound pages for Lange, and (b) an annex is not a sanctioned page-number source under the T3 rubric (star marker in cache / recorded T1–T2 conversion / a different case with official cites) — the cache is a slip opinion and the slip-stamp journal has no Lange bound conversion.

## Caveats / items for the orchestrator to rule

1. **STAR-MISS bucket (41 hits, NOT filed).** These resolve to cases whose cache IS star-paginated but the asserted pin falls outside the cached star range. All have `cache_markup==True`, so they are **not** the slip-only class. They are dominated by (i) partial cache excerpts (dissent/appendix pages beyond the cached majority) and (ii) residual cross-case attribution. Left unfiled as out-of-scope for `t3-unprovenanced-pin`; flag if a dedicated star-range audit is wanted.
2. **Cross-reporter conversion cases.** A few filed cases (e.g. *Carroll v. Carman*, *Riley v. California*, *Heien v. North Carolina*) carry U.S.-reporter pins whose only recorded basis is a conversion from **S. Ct.** star pagination present in the cache (the content notes this, e.g. "= 574 U.S. at 18–19"). Under the strict cache-U.S.-star oracle these are unprovenanced *for the U.S. page*; the underlying holding is pinned in S.Ct. The fix may be a sanctioned S.Ct.→U.S. conversion rather than a live re-pull. Filed as needs_cl for the serial lane to confirm the printed U.S. page.
3. **UNRESOLVED residue (7 hits, NOT filed).** Volume-collision pincites on doctrine pages where the cited case could not be uniquely attributed (multiple same-volume cases contain the pin, or the only nearby name is a see-also). Some may be slip-only defects (e.g. a `469 U.S. at 341/351` special-needs cite). Listed for manual disambiguation:
   - `content/cases/Banks v. Dretke.md:53` — 527 U.S. at 281 (nearest name: Brady v. Maryland)
   - `content/cases/United States v. Howard Davis.md:53` — 556 U.S. at 343 (nearest name: Chimel v. California)
   - `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/The Good-Faith Exception.md:28` — 468 U.S. at 923 (nearest name: Franks v. Delaware)
   - `content/warrant-exceptions/programmatic-and-special-needs-searches/Special Needs and Administrative Searches.md:40` — 469 U.S. at 351 (nearest name: Common Legal Terms)
   - `content/warrant-exceptions/programmatic-and-special-needs-searches/Special Needs and Administrative Searches.md:46` — 469 U.S. at 341 (nearest name: [[Vernonia School District 47J v. Acton|Vernonia]])
   - `content/warrant-exceptions/programmatic-and-special-needs-searches/Special Needs and Administrative Searches.md:74` — 469 U.S. at 351 (nearest name: Common Legal Terms)
   - `content/warrant-exceptions/searching-a-person/SIA Persons.md:33` — 414 U.S. at 235 (nearest name: [[Terry v. Ohio|Terry]])
4. **Scope of set S.** The 14 `slip_only==true` cases (criterion A) produced **zero** bound-pin hits — they are cited slip-only in content, exactly as intended; no defect. The whole defect class lives in criterion C (established SCOTUS opinions whose CL cache is plain text without CAP/Harvard star pagination) plus the official==null SCOTUS set (criterion B).

## Output files
- `_run/s9/p4/out/T3-REOPEN-findings.jsonl` — 162 `p4.candidate.v1` rows.
- `_run/s9/p4/out/T3-REOPEN-summary.md` — this file.