# P5-R14B summary — self-audit sampling half (R14 checks 2, 3, 6)

Lane **P5-R14B** · model **claude-opus-4-8** · 2026-07-22 · WRITE-SCOPE `_run/s9/p5/` only · **no live CL** (cache/lake/page evidence only; zero `needs_cl` rows required — every check resolved from primary text already in the lake/cache).
Spec: **S9 R14** (2) adjudication sampling re-check · (3) pass-sample re-read · (6) lint spot-verification. Findings-only: verdicts are the orchestrator's. I am a fresh lane — I did not review, fix, adjudicate, or panel any sampled item.

Outputs:
- `_run/s9/p5/R14-2-sample.jsonl` — 20 rows
- `_run/s9/p5/R14-3-passreread.jsonl` — 10 rows
- `_run/s9/p5/R14-6-lintspot.jsonl` — 18 rows

## Headline verdicts
- **R14-2: 20/20 CONFIRM · 0 DISCREPANCY.** No adjudicated dimension re-opened.
- **R14-3: 10/10 CONFIRM.**
- **R14-6: 17/18 CONFIRM · 1 DISCREPANCY** (LINT-6 dual-date guarantee — a green my hand-check contradicts; details below).

---

## (2) Adjudication sampling re-check — 20 UPHELD/MODIFIED legal fixes

**Frame & sampling (deterministic, reproducible).** Filtered `adjudications.jsonl` to verdict ∈ {UPHELD, MODIFIED} AND finding_id ∈ {`F-S9-PR-*`, `F-S9-P2-*`} = the 489 legal fixes produced by the P2 machine (individual escalate + class-tally + SM tracks; the SM/individual/tally tracks all emit `F-S9-PR-<hex>` ids, so a sort-then-stride over the hex interleaves the three classes). Excluded the 1 `F-S9-TOOL-001` (editorial/structural, not-paneled) and the 8 `F-S9-DN/IDS/R9B` rows (date-decided / identity-slice / R9B-ledger tracks, not the P2 panel classes). Sorted finding_ids ascending; systematic stride = 489/20 = 24.45; picked index `int(i·stride)` for i=0..19 → 20 finding_ids.

**Method.** For each: assembled {finding, verdict, adjudicated_holding, fix rows, target's current lake/page state, cached primary text at the cited offsets} and confirmed independently from PRIMARY evidence (not the adjudication's reasoning): quote verbatim at pin? holding at adjudicated breadth? fix actually applied on the page/lake?

**Result: 20/20 CONFIRM.** Verified sub-claims:
- **Identity re-key (1):** Chapman v. California re-keyed to the merits cluster 107359 / lead 9423348 / cite 386 U.S. 18, status=verified_identity; cache 107359.txt = the 1967 harmless-error merits opinion, cache 8398783.txt = the 154-byte cert-denial (the wrong lead). Confirmed from cache.
- **Lake pin re-harvests (7: Benn, Hoffa, Jones, Ramsey, Abel, Murray, + Muniz pincite retarget):** every stored quote is now **verbatim in the cached opinion** and **sits on its cited star page** (`*310/*264/*616/*241/*542/*592` all present in cache, quote in-segment). Star-verified vs slip-only convention holds (Abel kept slip-only conservatively though `*241` exists; Jones curly-double-quotes preserved). Muniz 590-591→592 retarget is correct AND the content page has since been reconciled to 592 too.
- **Content-page holding/home/citation fixes (8: Carney, Conner, J.L., Aguilar, Carloss, Prysock, Scott, Lopez-Mendoza):** every fix is applied on the page; truncated holdings are completed at supported breadth, Prysock 451→453 U.S. corrected in all 3 body occurrences, the two home-role relabels landed on both frontmatter + Appears-on surfaces.
- **Registry substantiated-from-lake no-ops (3: fruits-attenuation, brady, proof-ladder):** each node's cited authorities exist in the lake as verified/good_law records with pinpoints matching the propositions (Wong Sun/Brown; Brady/Giglio; Terry/Gates/Brinegar). Node stays `draft` (S7 owns promotion) — no-edit is the correct fix.
- **Doctrine rule (Civil Asset Forfeiture):** loop-3 promoted Austin/Bajakajian/Timbs to verified_identity with holding pins; DP + innocent-owner fronts are supported by body-cited authorities (James Daniel Good, Bennis) on the same page.

Non-blocking observations recorded per-row (not discrepancies): Chapman `case_name_full` CL quirk; Brady node's "no-request" clause rests on still-pending Agurs; Civil-Forfeiture callout inline-cite names only the Excessive-Fines cases while the other fronts are body-cited (the P3 fix substantiated rather than edited the callout).

## (3) Pass-sample re-read — 10 zero-finding case pages

**Selection (deterministic).** "Passed" = zero findings across the whole run. Joined `findings.jsonl` objects vs `content/cases/`: 610 case pages; 101 have zero content-page findings, but 81 of those had a lake-record finding for the same case (robust slug+name normalization) → **20 STRICT-clean pages (zero findings on both content page AND lake record)**. Sorted; stride 20/10=2; picked indices 0,2,…,18 → 10 pages. I had not reviewed any of them.

**Method.** Re-read each against its cached lead-opinion text (`~/cssi-lake/cache/text/<lead>.txt`, all 10 present): holding accurate? quotes verbatim? pins consistent with pinpoint_status? treatment consistent with record?

**Result: 10/10 CONFIRM.** All holdings are accurate against the cached opinions; all distinctive quoted phrases verify verbatim; all 10 carry the ⚪ unverified banner consistent with their `under_review`/`unverified` records.

**Cross-cutting observation for the orchestrator (important):** the STRICT-clean pool is **frontier-stub-dominated** — 16/20 `under_review`, 17/20 field_i `unverified`, and all 10 sampled pages are `under_review` with **0 lake pins**. "Passed" here means *generated no findings*, not *deeply verified*: these are circuit/state cases authored from CL-verified identity stubs, honestly rendered under the ⚪ banner with treatment/pins deferred to S6 promotion. The re-read confirms their holdings and quotes are accurate and honestly labeled, but their pincites remain machine-unverified exactly as the banner discloses (e.g., Massenburg's `654 F.3d at 493` has no reporter star-pagination in cache; Loines/Mendez use `slip op. at 13`). One minor quote-scoping nuance (Ziglar: page quotes "a disfavored judicial activity" as a unit; the opinion quotes only "disfavored") — words verbatim, scope broadened; not a misquote.

## (6) Lint spot-verification — 6 GREEN lints × 3 samples = 18

All six ran green (exit 0, 0 violations) at audit time. For each I confirmed the green is REAL via corpus samples + a negative control (crafted bad input via glob, committed fail fixture, or `--self-test`) proving the lint actually fires.

| Lint | samples | negative control | verdict |
|---|---|---|---|
| LINT-4 lexicon | Curtilage/index/Trent labels exact-allowlist (1796 sites scanned) | fires 2 HIGH on inverted + missing-Cir. labels | 3 CONFIRM |
| LINT-6 treatment | Terry (real dual dates) · Loines (frontier, ⚪ bannered) | fires HIGH on truly-blank date | **2 CONFIRM + 1 DISCREPANCY** |
| LINT-9 carat-leak | Muniz/Jones/Hoffa end-of-line anchors, 0 leaks (643 pages) | fires HIGH on mid-line `^pin-3` | 3 CONFIRM |
| LINT-12 drift | Terry/Katz/Prysock FM == lake projection | fail fixture fires HIGH | 3 CONFIRM |
| LINT-13 schema | Terry/Katz/Loines conformant, id==filename (672 recs, 0 dup) | self-test: 4 fail-fixtures fire | 3 CONFIRM |
| LINT-17 coverage | Albright/Baxter/Calero-Toledo page-less prose captions covered by ledger terminals | self-test PASS | 3 CONFIRM |

### The one DISCREPANCY — LINT-6 dual-date guarantee (a green a hand-check contradicts = a finding)
LINT-6's own docstring requires projected pages to carry **both** `as_of_content` AND `as_of_treatment` non-blank (R3) and fires HIGH on blank. But `scripts/lint/_common.py::split_frontmatter` (the stdlib subset parser) parses `as_of_content: null` as the **string `"null"`**, which is non-blank, so the sub-check passes on the placeholder token. **159 content pages carry a literal `null` date token** — 131 `under_review` + 21 `verified_identity` (design-consistent: bannered, dates deferred to S6), **plus 7 `verified`/`good_law` pages that are NOT bannered**: `United States v. Karo`, `County of Riverside v. McLaughlin`, `United States v. Conner`, `United States v. Mathis`, `United States v. Basher`, `Florida v. Riley`, `United States v. Leary` — each with `as_of_content: null`. The negative control confirms LINT-6 *does* catch a genuinely blank date, so this is a **null-token precision gap** (the green overstates R3 dual-date completeness), not a broken lint. Reader impact is bounded: those 7 pages still carry a real `as_of_treatment` currency date; only `as_of_content` is the `null` placeholder. Filed for orchestrator adjudication (writer ≠ checker — I do not decide whether the underlying state is acceptable or the lint should be tightened).

### LINT-17 note (not a discrepancy)
The coverage ledger is a **frozen superset**: 58/105 non-page terminal rows correspond to real page-less prose captions (green working correctly), but 47/105 are not in current prose — forward-looking `watch` (e.g. *Noem v. Vasquez Perdomo*), `excluded-remit` (e.g. *Castro v. Guevara*), and unrealized `brief-mention` (e.g. *Addington v. Texas*, whose Proof-Ladder pointer cites the concept via a glossary link without naming the caption). Harmless to the lint (unused allowlist entries), but "every ledger row matches a current prose caption" is not literally true.

### Peripheral (out of my assigned 6): LINT-5 is not fully green — it reports MEDIUM bare-caption rows (`United States v. Wilson`, `Carman v. Carroll` not wikilinked). Reported for awareness only; LINT-5 was not in this packet's scope.

## Coverage accounting
- R14-2: assigned 20 / examined 20 / skipped 0. Frame 489 legal P2 UM adjudications; 8 non-P2 legal tracks (DN/IDS/R9B) and 1 TOOL row deliberately out of frame (documented above).
- R14-3: assigned 10 / examined 10 / skipped 0. STRICT-clean pool = 20; sampled every 2nd.
- R14-6: assigned 18 / examined 18 / skipped 0. 6 lints × 3 samples; each lint additionally exercised with a firing negative control.
- Total 48 audit rows emitted. Builder (out-of-tree, reproducible): `scratchpad/build_r14b.py`; picks: `scratchpad/r14-2-picks.json`, `scratchpad/r14-3-picks.json`.
