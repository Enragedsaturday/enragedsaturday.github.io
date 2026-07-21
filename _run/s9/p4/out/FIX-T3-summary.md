# FIX-T3 — R11/P4-12 unprovenanced-pin ladder (execution)

**Packet:** FIX-T3 · **Lane/model:** FIX-T3 / claude-opus-4-8 · **Branch:** overhaul2/execute
**Authority:** RULING P4-12 (T3 unprovenanced-pin class disposition). **WRITE-SCOPE exercised:** `content/` (43 files), `_overhaul2/lake/cases/` (21 files / 28 pins), `_run/s9/p4/`.
**Oracle:** live `html_with_citations` star pagination re-fetched 2026-07-21 under `_run/s9/p4/star-refetch/<opid>.html` (P4-12(a)); second-source harvest **empty** (`T3-SECOND-SOURCE.jsonl`, 53 opinions, all `no-pagination-any-source`, P4-12(b) exhausted); cache oracle (`~/cssi-lake/cache/text/`) for the 7 unresolved.

## Headline

195 line-items dispositioned = **162 T3-REOPEN findings** + **33 residual (`no-live-star`) rows reconciled within them** + **7 UNRESOLVED cross-cites**, plus the Herring escalation.

| action (per finding) | count | keys |
|---|---|---|
| **upgraded** → lake pin `star-verified` + refetch provenance; content pin kept as printed | 66 | 29 |
| **kept-conversion-provenance** → documented S.Ct→U.S. conversion; U.S. pin kept; lake conversion-note | 5 | 5 |
| **converted** → content interior pin retired to first-page cite; lake stays slip-only; → R12 | 85 | 44 |
| **escalated** → prior star-verified lake pin vs refetch S.Ct-only, no documented conversion (Herring 144) | 6 | 1 |
| **provenanced-no-action** (7 UNRESOLVED) → star page present in cache; not a defect | 7 | 5 |
| **TOTAL fix rows** | **169** | |

Deterministic coverage: **assigned 162 + 7 = 169; examined 169; skipped 0.** Every finding_line 0–161 mapped 1:1 to a refetch row and dispositioned; every UNRESOLVED item classified.

## Method — canonical per-(opinion,pin) coverage (deterministic)

The input `refined_status` is assigned **per finding-row** and is internally inconsistent for the same `(opinion_id, pin)` across pages (e.g. Herring 144 tagged both `start-page-covered` and `no-live-star` on different pages). Star coverage is a fact about `(opinion, pin)`, so coverage was recomputed **directly from the refetch `html_with_citations`** — the artifact P4-12(a) names as the provenance:

- Extract visible `*NNN` / `<page-num label="NNN">` star markers per `<opid>.html`.
- Identify the **U.S.-reporter run** = the contiguous marker run anchored at the case's official first page (from lake `citations`). This excludes interleaved parallel-reporter markers (S.Ct/L.Ed), which for many post-2000 opinions are the *only* live pagination CL exposes.
- **live-star** ⟺ pin ∈ U.S. run; **start-page** ⟺ pin is the opinion's landing page (first U.S. marker = pin+1); else **convert**.

Result: **29 upgrade keys** (28 live-star + 1 start-page = Brendlin 251), **44 convert**, **5 documented-conversion keep**, **1 escalate**.

### Reconciliation vs the `refined_status` file — flagged for orchestrator sample-check

**(A) 13 upgrade keys the refined file under-counted** (it tagged them `no-live-star`/`no-star-pagination-live`, but the refetch html carries an explicit U.S.-reporter `*pin` marker — over-converting these would have retired *verifiable* pins):
Arizona v. Johnson 327 · Fernandez 303 · Florida v. Harris 244 · Florida v. Jardines 6/7/8/9/10 · Maryland v. King 465 · Plumhoff 777 · Prado Navarette 398 · Ryburn 477 · Grubbs 99. (Each interleaves S.Ct/L.Ed markers; the U.S. run brackets the first page — e.g. King U.S. run 439–482 vs S.Ct 1966–1990.)

**(B) 4 refined `start-page-covered` rows REFUTED by the html** (the live pagination is S.Ct-only; no U.S. star run, so the U.S. page is not a verifiable landing page):
- Herring 144 (fl 28, 94) → **escalated** (see below).
- Los Angeles County v. Rettele 614 (fl 100) → **kept-conversion-provenance** (page documents `127 S. Ct. at 1993–94`, star-verified).
- Scott v. Harris 386 (fl 115) → **converted** (bare U.S. pin, S.Ct-only markers 1772–1785).

The one genuine start-page upgrade — **Brendlin 251** — is U.S.-reporter (first live marker `*252`, landing page 251), retained.

## Documented cross-reporter conversions (KEEP) — for sample-check

5 locations show the parallel **S.Ct** pin adjacent to the U.S. pin, and that S.Ct pin **is** star-verified in the refetch. Per P4-12(c) cross-reporter clause the U.S. pin is KEPT and the lake pin carries a recorded-conversion note (not a bare assertion). Content unchanged at these locations.

| case | U.S. pin | documented S.Ct (star-verified in refetch) | lake pin noted |
|---|---|---|---|
| Heien v. North Carolina | 574 U.S. 60 | 135 S. Ct. 536 (markers 535–542) | pin-60 (already star-verified) |
| Carroll v. Carman | 574 U.S. 18 | 135 S. Ct. 348, 352 (markers 348–352) | *no lake pin — noted* |
| Kingsley v. Hendrickson | 576 U.S. 396–397 | 135 S. Ct. 2473 (markers 2471–2479) | pin-397 |
| Virginia v. Moore | 553 U.S. 168 | 128 S. Ct. 1607 (markers 1601–1609) | pin-1607 |
| Los Angeles County v. Rettele | 550 U.S. 614 | 127 S. Ct. 1993–94 (markers 1990–1994) | pin-1993 |

## Escalation (do-not-guess) — Herring v. United States 555 U.S. 144 (6 findings)

Lake `pin-144` is **already `star-verified` (star_marker "144")** from a prior phase with an **unrecorded basis**, but the refetch `html_with_citations` paginates **S. Ct. only** (129 S. Ct. 697–711) — U.S. page 144 is absent from live star pagination, the second-source harvest is empty, and the content asserts a bare `555 U.S. at 144` with **no documented S.Ct conversion**. Converting would downgrade a prior star-verified pin (overturn a prior verified state); keeping asserts a page the refetch cannot substantiate. **Neither content nor lake was touched** — routed to the orchestrator as 6 `escalated` rows (case page L55 + Collective Knowledge L39/L103 + Good-Faith Exception L33/L41/L127). Contrast Heien 60, the same shape but with an on-page documented conversion → kept.

## The 33 residual (`no-live-star`) rows — reconciled

These are **sibling content locations** of pins whose case-page finding got a coverage verdict; the refetch pipeline left the sibling rows unrefined. Recomputed against the html oracle they resolve deterministically: **27 upgraded** (siblings of star-verified pins — e.g. Hudson 594, Grubbs 96/99, Randolph 120, Samson 857, Ryburn 476/477, Brigham 400/404), **4 escalated** (Herring 144), **1 kept-conversion** (Moore 168 mirror), **1 converted** (Scott 386). No residual left unclassified.

## The 7 UNRESOLVED cross-cites — all PROVENANCED (no defect)

Volume-collision cites the sweep could not attribute; each resolved to a target case whose **cache carries the star page** → not a `t3-unprovenanced-pin` defect. No content/lake change (targets are outside the named-case write-scope).

| file:line | resolved cite | star evidence |
|---|---|---|
| cases/Banks v. Dretke.md:53 | Strickler v. Greene, 527 U.S. 281–282 | `*281`/`*282` in cache 118307 |
| cases/United States v. Howard Davis.md:53 | Arizona v. Gant, 556 U.S. 343 | `label="343"` cache 9435359 |
| …the-exclusionary-rule/The Good-Faith Exception.md:28 | United States v. Leon, 468 U.S. 923 | `label="923"` cache 9429766 |
| …Special Needs and Administrative Searches.md:40, :74 | New Jersey v. T.L.O., 469 U.S. 351 (Blackmun concurrence) | `*351` in sibling-opinion cache 111301 |
| …Special Needs and Administrative Searches.md:46 | New Jersey v. T.L.O., 469 U.S. 341 (majority) | `label="341"` cache 9429812 |
| …searching-a-person/SIA Persons.md:33 | United States v. Robinson, 414 U.S. 235 | `label="235"` cache 9425474 |

## Ladder (d) — "S7 research annex §11" retirement

Sole occurrence: `…/Exigent Circumstances and Hot Pursuit.md:133` (Lange, a convert). The `(pinpoints: 303–04, 313 — bound-volume pins per S7 research annex §11 …)` clause is retired to `(first-page cite; interior bound-volume pincites retired per T3/P4-12 — lead opinion 4698186 is a slip opinion with no star pagination; body holding paraphrased, T3)`.

## Changes applied

- **content/** — 43 files, **81 lines** converted (interior U.S. pin → first-page/parallel cite; quotes and prose intact; each page's existing citation style followed). Line-index-verified applier, 0 old-string mismatches. Upgrade and kept-conversion locations were **not** edited (pins now provenanced, kept as printed).
- **_overhaul2/lake/cases/** — 28 pins across 21 files. **25 upgraded** to `star-verified` (star_marker set, refetch provenance note); **3 keep-cases** got the recorded-conversion note (Heien pin-60, Kingsley pin-397, Moore pin-1607, Rettele pin-1993 — Heien already star-verified). Round-trip `ensure_ascii=True, indent=2` → minimal diffs; concurrent sibling edits on shared worktree (e.g. Heien P4-10 promotion) preserved.
- **Lake gaps (6, no matching pin — content stays provenanced, noted not fixed):** Carroll v. Carman 18 (no pins), Kansas v. Ventris 594 (no pins), Rehberg v. Paulk 369 (only pin-slip-1), Florida v. Jardines 7 & 10, Florida v. Harris 244. These content pins are html-verified but have no discrete lake pin to flip (lake modeling gap, not a defect).

## Output files
- `_run/s9/p4/out/FIX-T3-fixes.jsonl` — 169 rows (66 upgraded / 5 kept-conversion / 85 converted / 6 escalated / 7 provenanced-no-action).
- `_run/s9/p4/out/R12-pin-upgrade-queue.jsonl` — 85 rows (every converted pin: case, cluster_id, retired printed pin, file:line — for re-verification when official U.S. Reports pagination lands).
- `_run/s9/p4/out/FIX-T3-summary.md` — this file.
