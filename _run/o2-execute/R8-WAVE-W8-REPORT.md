# R8 WAVE W8 — batch report (frontier 2) — CLOSED

- **Lane/model:** r8-wave-author · `claude-opus-4-8` (Opus 4.8 [1m])
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** 1fde2d6 (git commit: none — orchestrator commits at the gate)
- **Batch:** W8 = 20 frontier rows (frontier-controlling + 2 frontier-split), the **final main wave**. **Outcome: 20 minted** (all born `under_review` ⚪) · **0 skips** · **0 escalations**. Every row re-verified CLEAN on read (identity + verbatim Rule quote + home); the pre-W5 audit's clean-frontier call held.
- **Case Index:** regenerated → **594 rows (+20), 0 blank Good-law cells.** **`npx quartz build` SUCCESS** (696 parsed, 2575 emitted; re-run green after body remediation). **0×429.**
- **CL usage:** **~65 serial MCP calls** (search_document pincite locates + read_document chunk/full reads + 3 cluster→sub-opinion resolutions for the modern-id rows), single serial lane throughout, **0×429**. A handful of transient "MCP server connection lost" errors occurred and were cleared by a single retry each (not rate-limit backoff; no true 429, no outage/yield).

## Minted (20) — all born `under_review` (⚪), one page each
Identity re-verified against the CL opinion text for **every** row before authoring. Each page carries exactly **one** pinned Rule quote, copied verbatim from the CL text, with a recognized same-line pincite ending in `^pin-N`.

| # | Page | Cite (projected) | Home · role | Author | pincite |
|---|---|---|---|---|---|
| 1 | Roaden v. Kentucky | 413 U.S. 496 (1973) | The Warrant Requirement · Anchor | Burger, C.J. | 413 U.S. **at 504** (star `*504`) |
| 2 | Timbs v. Indiana | 586 U.S. 146 (2019) | Civil Asset Forfeiture · Anchor | Ginsburg, J. | **139 S. Ct. at 687** (parallel; page-label `*687`) |
| 3 | United States v. Bajakajian | 524 U.S. 321 (1998) | Civil Asset Forfeiture · Anchor | Thomas, J. | 524 U.S. **at 334** (star `*335` follows) |
| 4 | United States v. $8,850 in Currency | 461 U.S. 555 (1983) | Civil Asset Forfeiture · Anchor | O'Connor, J. | 461 U.S. **at 556** (between `*556`/`*557`) |
| 5 | United States v. James Daniel Good Real Property | 510 U.S. 43 (1993) | Civil Asset Forfeiture · Anchor | Kennedy, J. | 510 U.S. **at 62** (between `*62`/`*63`) |
| 6 | United States v. Von Neumann | 474 U.S. 242 (1986) | Civil Asset Forfeiture · Anchor | Brennan, J. | 474 U.S. **at 250** (between `*250`/`*251`) |
| 7 | Scott v. United States | 436 U.S. 128 (1978) | Electronic Surveillance and Title III · Anchor | Rehnquist, J. | 436 U.S. **at 137** (star `*137`) |
| 8 | United States v. Donovan | 429 U.S. 413 (1977) | Electronic Surveillance and Title III · Anchor | Powell, J. | 429 U.S. **at 434** (between `*434`/`*435`) |
| 9 | United States v. Giordano | 416 U.S. 505 (1974) | Electronic Surveillance and Title III · Anchor | White, J. | 416 U.S. **at 527** (star `*527`) |
| 10 | United States v. United States District Court (Keith) | 407 U.S. 297 (1972) | Electronic Surveillance and Title III · Anchor | Powell, J. | 407 U.S. **at 324** (star `*324`) |
| 11 | Stone v. Powell | 428 U.S. 465 (1976) | The Exclusionary Rule · Anchor | Powell, J. | 428 U.S. **at 494** (between `*494`/`*495`; dissent "Ante, at 494") |
| 12 | United States v. Blue | 384 U.S. 251 (1966) | The Exclusionary Rule · Anchor | **Harlan, J.** | 384 U.S. **at 255** (between `*255`/`*256`) |
| 13 | United States v. Caceres | 440 U.S. 741 (1979) | The Exclusionary Rule · Anchor | Stevens, J. | 440 U.S. **at 755** (star `*755`) |
| 14 | United States v. Satterfield | 743 F.2d 827 (11th Cir. 1984) | The Exclusionary Rule · **Illustrates a circuit split** | Kravitch, J. (11th Cir.) | 743 F.2d **at 846** (between `*846`/`*847`) |
| 15 | South Dakota v. Neville | 459 U.S. 553 (1983) | Confessions… index · Anchor | O'Connor, J. | 459 U.S. **at 564** (star `*564`) |
| 16 | Weatherford v. Bursey | 429 U.S. 545 (1977) | Sixth Amendment Right to Counsel · Anchor | White, J. | 429 U.S. **at 558** (between `*558`/`*559`) |
| 17 | Will v. Michigan Dept. of State Police | 491 U.S. 58 (1989) | Section 1983 · Anchor | White, J. | 491 U.S. **at 71** (star `*71`) |
| 18 | United States v. Warshak | 631 F.3d 266 (6th Cir. 2010) | Third-Party Doctrine and Digital Surveillance · Anchor | Boggs, J. (6th Cir.) | 631 F.3d **at 288** (star `*288`) |
| 19 | United States v. Robinson (4th Cir. en banc) | 846 F.3d 694 (4th Cir. 2017) | Terry Stops and Reasonable Suspicion · **Illustrates a circuit split** | Niemeyer, J. (4th Cir. en banc) | 846 F.3d **at 696** (star `*696`) |
| 20 | Rochin v. California | 342 U.S. 165 (1952) | Common Law Origins · **Historical / origin** (history-render) | Frankfurter, J. | 342 U.S. **at 172** (star `*172`) |

## Owed reciprocal re-link (pre-ratified) — LANDED
W7 de-linked Austin v. United States's two forward wikilinks to *Timbs* and *Bajakajian* (they didn't exist yet). After minting both in W8, I restored the links on `content/cases/Austin v. United States.md` **body-only**: (a) the two `[[…]]` wikilinks in the Treatment paragraph, (b) the two entries in the content-authored `related:` list, and (c) removed the now-obsolete "(Case-page cross-links … are deferred …)" parenthetical. The projected/managed frontmatter, lake, manifest, ledger, and pinned content were untouched. Austin now resolves both links (0 dead-wikilink highs at final build).

## Special-treatment rows
- **Rochin v. California (history-render, PRACTICES §7).** Rendered as a **historical origin**, not disguised: precise about the two threads — the "shocks the conscience" **substantive-due-process principle is still good law** (reaffirmed *County of Sacramento v. Lewis*, 1998), while Rochin's function as a **search-and-seizure exclusion vehicle was a pre-incorporation stopgap superseded** when *Mapp v. Ohio* (1961) incorporated the Fourth Amendment exclusionary rule against the States (with *Wolf v. Colorado* → *Rochin* → *Mapp* → *Schmerber* forward pointers). Header treatment label: "Historical origin (⚪ unverified, pending S9)".
- **United States v. Robinson (4th Cir. en banc) + United States v. Satterfield (frontier-split, LINT-21).** Both framed honestly as **in-circuit binding, persuasive elsewhere**, naming the live split rather than a settled national rule. *Robinson* (4th Cir.): a lawfully stopped person reasonably believed **armed** may be frisked without a separate showing of **dangerousness**, even in a right-to-carry jurisdiction — expressly placed on the **opposite side of the split** from *Northrup v. City of Toledo* (6th Cir., W7) and *United States v. Black*. *Satterfield* (11th Cir.): the inevitable discovery exception requires the lawful means to have been **actively pursued *prior*** to the illegality — one side of the post-*Nix v. Williams* split.

## Identity / data notes (for S2 / S9)
- **Modern-id rows resolved via the cluster (opinion_id ≠ cluster_id):** Timbs (cluster 4591916 → majority opinion **9888039**, Ginsburg), Satterfield (8934150 → **8924377**, Kravitch), Robinson-4th (4340460 → en banc majority **9871494**, Niemeyer). Reading opinion_id = cluster_id for these returns a *different* opinion (e.g., 4591916 as an opinion id is a 1993 Tax Court memo, "Garcia-Wright v. Commissioner") — the on-read identity re-verification caught this; sub-opinions were fetched from the cluster and confirmed against caption/date. Legacy SCOTUS rows still resolve directly (opinion_id == cluster_id), all caption-verified on read.
- **United States v. Blue authorship:** the CL opinion text attributes the opinion to **Mr. Justice Harlan** (not the Chief Justice). Disclosed in the page header comment and Conclusion.
- **Parallel-reporter pincites (modern SCOTUS):** *Timbs*'s CL text is paginated to the **West S. Ct. reporter** (139 S. Ct. 682), not U.S. Reports; the pin is therefore `139 S. Ct. at 687` while the header/frontmatter cite stays the official 586 U.S. 146 (disclosed in Sources). (Same convention as W7 Mendez/Grady/Manuel/McDonough.)
- **Rochin verbatim em-dash:** the pinned "shocks the conscience" quote reproduces the source's em-dash in "stomach's contents—this course" (disclosed in Sources); verbatim fidelity preferred over the em-dash budget.

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page carries exactly **one** pinned Rule quote, string-matched (case-insensitive literal) against the CL opinion text this session, with a recognized same-line pincite + `^pin-N`. **LINT-9 (carat leak) = 0 on all 20.** Author attributions and dispositions taken from the CL opinion text seen directly (Burger/Ginsburg/Thomas/O'Connor/Kennedy/Brennan/Rehnquist/Powell/White/Harlan/Stevens/Frankfurter/Kravitch/Niemeyer/Boggs author lines all read on-page); separate-opinion line-ups (dissents/concurrences) taken from the CL text where read and otherwise stated conservatively. Treatment sections render each birth honestly as ⚪ `under_review`; Rochin rendered as good-law historical origin per PRACTICES §7 (precise verbs, forward pointer, demotion, not disguised).

## Body-only finalization (post-mint; frontmatter/lake/manifest/ledger/binding UNTOUCHED, except the pre-ratified Austin re-link)
First-write left **12 LINT-2 mediums** (secondary narrative quotes ≥6 words lacking a nearby pincite — e.g., Rochin "heedless of the means…", Keith AG-affidavit, Will "…suit against the official's office", Neville "I'm too drunk…") and **3 LINT-7 term-register highs** on Satterfield (`inevitable-discovery` → canonical `inevitable discovery`). Remediated **body-only** on the minted pages: the 12 secondary quotes de-quoted/paraphrased (each page's authoritative pinned Rule quote untouched), and the 3 Satterfield body occurrences corrected (the frontmatter `holding:` was reverted to match the ledger text after a `replace_all` briefly touched it — page↔ledger holding re-synced). Post-remediation on the 20 W8 pages: **LINT-2 = 0, LINT-7 = 0, LINT-9 = 0, LINT-5 dead-wikilink highs = 0.** Build re-run green.

## Lint delta (baseline = post-W7 corpus; frontier batch)
- **Mint gate (LINT-14/15/16): all 20 pages 0/0/0** at dry-run and at write.
- **LINT-2: 0 on all 20** (post body-only de-quote). **LINT-7: 0** (post term-register fix). **LINT-9: 0.**
- **LINT-5 (link-every-case): 53 mediums on the 20 pages, 0 highs.** The mediums are the **accepted pre-existing class** — (a) each case page's own name in its header/Sources cannot self-wikilink (the *Smith* specimen carries the same), and (b) passing mentions of cross-reference cases named in prose. **No dead-wikilink highs** (all intra-W8 and Austin cross-links resolve at the final batch build).
- **LINT-10 (em-dash budget): 57 highs across the 20 pages (~2.85/page).** The **documented corpus-wide known-red** (fires on the *Smith* specimen and every prior wave; owned by S1/style, not S6 authoring). In line with the specimen and W1–W7 house style — **no new class attributable to this batch** (reported delta-only per work order).
- **Corpus-wide lints unchanged in character** (LINT-19 overview-table highs are on S7/S8-owned home index pages, not W8 case pages; LINT-21 low overrides are S2-owned bound-PENDING lake rows).
- **Case Index regenerated → 594 rows (+20, exactly the W8 pages)**, 0 blank Good-law cells.
- **`npx quartz build` SUCCESS** (696 parsed, 2575 emitted; only expected "not yet tracked by git" date warnings on the new pages).

## Scope of writes (COMMIT NOTHING)
New: 20 `content/cases/*.md`, 20 promoted lake stem records (`_overhaul2/lake/cases/<stem>.json`), 20 payload scratch files under `_run/o2-execute/w8-payloads/`, this report. Modified by the CLI/regen/me: `_overhaul2/lake/_manifest.json` (20 rename entries), `_run/o2-execute/s6-authored-ledger.jsonl` (20 `authored` rows, `{lane: s6-r8-mint, model: claude-opus-4-8}`), `content/legal-system-research-and-reference/Case Index.md`, `content/cases/Austin v. United States.md` (pre-ratified reciprocal re-link, body-only), `_run/o2-execute/R8-WAVE-PLAN.json` (W8 status → authored). **Not committed** — the orchestrator commits at the batch gate.

## Fleet status after W8
W1 15 + W2 11 + W3 17 + W4 11 + W5 15 + W6 15 + W7 21 + **W8 20 = 125 minted** across the eight main waves. Remaining unminted rows are the journaled deferred-recovery / data-escalation / wrong-case skips tracked in the wave plan for the tail batch **W9** (citations.display-empty 2026-term rows, withdrawn-opinion holcomb, genuine CL cite gaps, folded duplicates). W8 (final main wave) is **CLOSED**.
