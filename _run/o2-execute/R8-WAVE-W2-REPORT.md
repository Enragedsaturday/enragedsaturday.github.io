# R8 WAVE W2 — batch report (sweep 2nd half + packet-B)

- **Lane/model:** r8-wave-author · `claude-opus-4-8`
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** e9b5cf5 (git commit: none — orchestrator commits at the gate)
- **Batch:** W2 = 16 rows. **Outcome:** 11 minted · 5 journaled skips · 0 escalations blocking.
- **CL discipline:** single serial MCP lane, ~35 CL calls total, **0×429**. No parallel CL consumer observed. No CL REST calls.

## Per-row outcomes

### Minted (11) — all born `under_review` (⚪), one page each
| # | Page (stem) | Cite | Home(s) · role · prong | Pincite (Rule quote) | pinpoint_status |
|---|---|---|---|---|---|
| 1 | Nance v. Ward | 597 U.S. 159 (2022) | §1983/QI · Recent development · c | slip op. at 1 ("We hold that it is") | slip-only (A3) |
| 2 | Perttu v. Richards | 605 U.S. 460 (2025) | §1983/QI · Recent development · c | 605 U.S. **468** ("we hold as a matter of statutory interpretation…") | star-verified (dissent "Ante, at 468") |
| 3 | Tanzin v. Tanvir | 592 U.S. 43 (2020) | §1983/QI · Recent development · c | slip op. at 1 ("We hold that it does") | slip-only (A3) |
| 4 | Uzuegbunam v. Preczewski | 592 U.S. 279 (2021) | §1983/QI · Recent development · c | slip op. at 11 (Part III, "we conclude that a request for nominal damages…") | slip-only (A3) |
| 5 | Bennis v. Michigan | 516 U.S. 442 (1996) | Civil Asset Forfeiture · Key · c | 516 U.S. **446** ("a long and unbroken line of cases…") | star-verified (before *447) |
| 6 | G. M. Leasing Corp. v. United States | 429 U.S. 338 (1977) | Curtilage (Key) + Warrant Requirement (Related) · a | 429 U.S. **351** + **352** (public-seizure / office-intrusion) | star-verified (before *352 / *353) |
| 7 | Heller v. New York | 413 U.S. 483 (1973) | The Warrant Requirement · Key · a | 413 U.S. **492** ("If such a seizure is pursuant to a warrant…") | star-verified (between *492/*493) |
| 8 | United States v. Carpenter (6th Cir. 2019 remand) | 926 F.3d 313 (2019) | The Exclusionary Rule · Key · b | 926 F.3d **313** ("Because these agents reasonably relied on the SCA, we AFFIRM…") | first-page (CL text uses ¶-markers, no internal F.3d star pagination) |
| 9 | United States v. Verdugo-Urquidez | 494 U.S. 259 (1990) | Fourth Amendment Framework · Key · a | 494 U.S. **265** ("'the people' … a class of persons who are part of a national community…") | star-verified (dissent "Ante, at 265") |
| 10 | Wyman v. James | 400 U.S. 309 (1971) | Special Needs & Administrative Searches · Key · a | 400 U.S. **317–318** ("the visitation in itself is not forced or compelled…") | star-verified (crosses *318) |
| 11 | Ziglar v. Abbasi | 582 U.S. 120 (2017) | §1983/QI · Key · c | 582 U.S. **135** ("separation-of-powers principles are or should be central…") | star-verified via S. Ct. parallel (*1858 = 137 S. Ct. 1857–58) |

Identity verified for each against the CL cluster (caption / cite / date / court) before authoring — no minting on an unverified identity (Egbert precedent). Notable identity confirmations: **Carpenter-remand** cluster 4628336 = "United States v. Timothy Carpenter", **926 F.3d 313 (6th Cir., 2019-06-11)** — the good-faith remand, distinct from SCOTUS Carpenter (585 U.S. 296); **Verdugo** cluster 112382 = **494 U.S. 259 (1990)** (the corrected merits cite, not the 1994 cert-denial 513 U.S. 1114); **Bennis** cluster 118005 = **516 U.S. 442** (re-keyed record). All 11 opinion texts read via MCP `read_document`/`search_document`; every Rule quote string-matched **verbatim** to CL text 2026-07-07.

### Skipped (5) — journaled, no mint attempted
| record_id | reason | why |
|---|---|---|
| landor-v-louisiana-department-of-corrections-and-public-safety--10878535 | deferred-recovery | `citations.display` empty (2026 term, slip-only; no U.S. Reports cite) — projected citation empty → CLI refuses `record-missing-citation`. Slip-cite render amendment in flight in a parallel lane. |
| olivier-v-city-of-brandon--10811625 | deferred-recovery | same slip-cite render gap |
| postal-service-v-konan--10799651 | deferred-recovery | same slip-cite render gap |
| the-geo-group-inc-v-menocal--10800194 | deferred-recovery | same slip-cite render gap |
| zorn-v-linton--10813527 | data-escalation | corrupt CL cluster (court_level/year/date_filed/docket null, `citations.display` empty) — long-standing escalation; not authored on a broken identity |

## packet-B disposition fidelity
Authored the framing the adjudications decided (`packetb-dispositions.jsonl` + panel ADJUDICATION):
- **8 Wyman** — special-needs/administrative home-visit; not a criminal search / reasonable; prong a.
- **9 G. M. Leasing** — public-place seizure needs no warrant vs. warrantless office entry violates 4A; administrative purpose does not relax the entry rule; homes Curtilage(Key)+Warrant Requirement(Related). Corpus spelling "G. M. Leasing" (spaced) is the stem; no dual-list.
- **10 Verdugo-Urquidez** — "the people" scope; framework anchor; authored on corrected 494 U.S. 259.
- **13 Carpenter-remand** — OWN PAGE, Leon/Krull good-faith on SCA reliance; **caption-trap note vs SCOTUS Carpenter** carried in-page.
- **14 Bennis** — PAGE (innocent-owner rule the core-four forfeiture anchors don't carry); **antecedent note referencing Calero-Toledo** added in Treatment (innocent-lessor language subsumed). Overruled orch bullets-for-both.
- **15 Ziglar** — PAGE via D1 flip (named in §1983 prose); Bivens-contraction trilogy leg with Hernandez/Egbert.
- **16 Heller v. New York** — PAGE (affirmative operational rule); **caption-trap note vs District of Columbia v. Heller** carried in-page + header comment. Overruled orch all-bullets.

**post-mint conversions NOT executed here** (E2/E3: S6 writes no homes pages; S7 materializes Key/Related rows from `s6-authored-ledger.jsonl`). The ledger `home_rows`/`worklist_note` carry the hints. Owed conversions on OTHER pages, deferred to S7: Wyman (Special Needs :175, Case Index :485); G. M. Leasing (Curtilage :123, Warrant Req. :181, Case Index :152, + Florida v. White Related); Verdugo (Case Index :458, keep Chavez :59 quote); Carpenter-remand (Exclusionary-Rule index :134/:202); Bennis (Calero antecedent — done in-page; node one-liner deferred); Ziglar (§1983 Sources :167–:168, Bivens scope note :21/:63).

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page carries exactly one pinned Rule quote (`^pin-N`, end-of-paragraph), string-matched verbatim to CL text. Slip-paginated SCOTUS opinions (Nance, Tanzin, Uzuegbunam) rendered **slip-only per S2 A3** (`^pin-op`, "slip op., at N", page equality not asserted) — matching the Chatrie/Taylor v. Riojas convention. Star-verified pins keyed to the nearest preceding reporter star marker. Ziglar's U.S. pin (135) corroborated by the S. Ct. star pagination the CL text carries (137 S. Ct. 1857–58), the Nieves pattern.

## Lint delta
- **Mint gate (LINT-6/13/14/15/16): all 11 pages clean, 0 findings** at both dry-run and post-mint (the W1 systemic LINT-6/13 fixes hold — no mint↔lint gap in that class).
- `scripts/lint/run_all.py` exits 1 on the pre-existing S7/S8/S9-owned known-red corpus (LINT-10 em-dash 4147, LINT-5 wikilink 2490, LINT-19/21, etc.). **Corpus HIGH count went DOWN 4742 → 4731 (−11).**
- **On my 11 pages, residual = accepted W1-baseline known-red classes only:** LINT-10 (em-dash budget, 23 high — S8 style remediation; the signed specimen register uses em-dashes) and LINT-5 (bare case name not wikilink, 29 med — S8 D13 wikilink materialization, incl. self-name references). W1-minted pages (Nieves/Martin/Goldey/…) carry the same two classes and only those.

### Mint↔lint gap found + remediated (disclosed for orchestrator ratification — writer≠checker)
The mint gate covers only LINT-14/15/16, so three defect classes the W1 payloads avoided slipped through on first write. Fixed by **body-only prose finalization** (frontmatter / lake / manifest / ledger / page↔record binding UNTOUCHED; LINT-14 still clean); returned for the machine to adjudicate at the gate:
1. **LINT-9 (visible mid-line `^pin` carat, 6× HIGH)** — Bennis/G. M. Leasing(×2)/Heller/Verdugo/Ziglar had prose continuing after the pin. Fixed by a paragraph break so each `^pin-N` ends its line (renders invisibly). R16 nominally routes LINT-9 to S9, but these were fresh authoring misses, cheap and correct to fix now.
2. **LINT-2 (inline quotation without a nearby pincite, MED)** — Nance (Application "…easy-to-employ…") and Carpenter-remand (two Application quotes) de-quoted to paraphrase; the single pinned Rule quote remains the verbatim carrier. Honors "no proposition without a verified pincite."
3. **dead-wikilink HIGH (4×, "blocks publish")** — Bennis→Calero-Toledo, Heller→Marcus/Roaden, Ziglar→Egbert de-linked in body prose to plain italic case names (they mint in W7/W8/tail; S8 D13 re-links once the pages exist — the accepted LINT-5-MED path). Frontmatter `related:` forward-refs left intact (not flagged; matches specimen).

Net effect of the finalization: −11 corpus HIGH; my pages now match the W1 conformance profile exactly.

## Batch close
- Case Index regenerated (`build_case_index.py`): 495 rows (+11, exactly the W2 pages), 0 blank Good-law cells.
- `npx quartz build` → **exit 0**, 597 files parsed, 2144 emitted (only benign git-untracked-date warnings — no git commit performed).
- Ledger: 11 `authored` rows appended (model `claude-opus-4-8`), lake stubs promoted to page-backed records, old stubs removed, manifest renames applied atomically by the CLI.
- Wave-plan: W2 → `authored` (minted 11, skipped 5).

## For the orchestrator
- Ratify (or revert) the body-only post-mint finalization above.
- 4 deferred-recovery slip-only rows (landor/olivier/konan/geo-group) + zorn data-escalation carry forward to the recovery/tail lane exactly as W1's slip/corrupt skips did.
- S7 owes the homes-page Key/Related materialization + the listed brief-mention→page conversions from `s6-authored-ledger.jsonl`.
