# PAIR-P1 summary — S9 P4 R6 contradiction sweep (pairs PAIR-0001..PAIR-0110)

**Packet:** PAIR-P1 · WS=PAIR · lane/model `claude-opus-4-8`
**Governing:** RULING P4-02 (per-pair review scoped to the pair's `shared_items`) + P4 worker brief (findings-only, no verdicts, no CL).
**Write-scope honored:** only `_run/s9/p4/` written.
**Outputs:** `out/PAIR-P1-dispositions.jsonl` (110 rows), `out/PAIR-P1-findings.jsonl` (empty — 0 HITs), this file.

## Coverage ledger (deterministic)
| metric | value |
|---|---|
| pairs assigned | 110 (PAIR-0001..PAIR-0110, contiguous) |
| pairs examined | 110 / 110 |
| pairs skipped | 0 |
| kind of every assigned pair | `shared-case` (each `shared_items` = 1 shared case) |
| distinct case pages (page_a) read | 51 |
| distinct topic pages (page_b) read | 51 |
| **HITs** | **0** |
| **CLEAN** | **110** |

Silent truncation: none. Every pair carries one `p4.pair.v1` disposition row.

## Method
1. Parsed `pair-list.json` for my 110 pairs; all are case-anchored (`page_a = content/cases/<case>.md`, `page_b = a doctrine home`) with a single shared case each.
2. **Case-page canonical record** (page_a): extracted per shared case `treatment.field_i_validity`, `varies_by_point`, `point_overrides`, `scope_note`, the rendered header treatment badge, the `## Treatment & subsequent history` section, and frontmatter `holding`. Four of my 51 shared cases are non-`good_law`: **Coolidge v. New Hampshire** and **Escobedo v. Illinois** = `caution` (rendered "limited", `varies_by_point: true`, with `point_overrides`); **Bell v. Wolfish** and **FBI v. Fazaga** = `unverified` (frontier stubs). The other 47 are `good_law`.
3. **Topic-page framing** (page_b): harvested every mention of the shared case (full name, italic short forms, wikilinks) with ±1-line context across all 51 topic pages, grouped so each page was read once and serves all its pairs.
4. Per RULING P4-02, checked only the shared item on the four legs: (i) Field-I treatment status + N4 "limited by [[case]]" tag identical across the pair; (ii) any overruled/superseded case rendered Historical (tier 6) on both; (iii) framing not semantically contradictory (incompatible rule statements, opposite outcomes, conflicting scope, mutually-exclusive boundary sentences) — page-specific emphasis permitted per N6; (iv) nothing else (full-page re-review was P1's job).
5. Since 0 HITs were produced, no `adjudications.jsonl` cross-check for hit-filing was required.

## Result: 110/110 CLEAN, 0 contradictions
Every shared case is framed **consistently** across its two (or three) home pages. Findings by leg:

- **Leg (i) — treatment status + N4 tag.** The 4 non-`good_law` shared cases carry consistent treatment across the pair:
  - **Coolidge v. New Hampshire** (PAIR-0058 Plain View / PAIR-0059 Neutral Magistrate): case page = `caution`, N4 tag "inadvertence prong abandoned by [[Horton v. California]]". Plain View page states "*Coolidge* limited by *Horton*" with the identical Horton controlling-case tag. Neutral-Magistrate page invokes the **surviving** prosecutor-as-magistrate holding (good law) — correct under `varies_by_point` + `point_overrides` (only the plain-view inadvertence point is limited). No contradiction.
  - **Escobedo v. Illinois** (PAIR-0075 Miranda / PAIR-0076 6A Counsel): case page = `caution` ("limited"; result intact, rationale recast as 5A by Miranda, confined by Kirby/Moran). 6A page carries explicit "(treatment: limited)"; Miranda page: "recast as a Fifth Amendment matter and confined to its facts." Identical status + successor authority (Miranda).
  - **Bell v. Wolfish** (PAIR-0018 / 0019) and **FBI v. Fazaga** (PAIR-0077 / 0078): case pages `unverified` (⚪ frontier stub — a *provenance* flag, not a substantive negative Field-II edge). Topic pages cite both as good, correctly-stated authority with no "limited/overruled" tag. No cross-page treatment conflict.
  - All 47 `good_law` shared cases carry no negative Field-II edge; no "limited by" tag appears on either page for the shared item (leg (i) identity holds trivially).
- **Leg (ii) — overruled-as-Historical.** No shared case in my scope is `superseded`/overruled, so this leg is vacuously satisfied for all 110. (Cases that are *overruled by* the shared case — e.g. Belton by Gant, Sanders by Acevedo, Aguilar/Spinelli by Gates — are correctly rendered as limited/superseded/abrogated where they appear, but they are not the pair's shared item.)
- **Leg (iii) — framing non-contradiction.** Page-specific emphasis differs as N6 allows (e.g. Herring read for "culpability threshold" on Good-Faith Exception vs "imputation limit" on Collective Knowledge; Bond as "bailment != abandonment" on Abandonment vs "tactile squeeze is a search" on REP; Coolidge's two distinct holdings on two pages), but no pair contains incompatible rule statements, opposite outcomes, conflicting scope claims, or mutually-exclusive boundary sentences. Rule quotes, holdings, and pincite anchors align across homes.

## Out-of-R6-scope observations (for orchestrator triage — not PAIR-P1 hits)
Filed as notes only, per the PAIR-P3 precedent; none is a shared-item contradiction and none is adjudicated here.

1. **Absent-home (coverage, not contradiction) — PAIR-0003 & PAIR-0037.** `content/the-exclusionary-rule-remedies-and-standing/the-exclusionary-rule/index.md` is a lean umbrella/landing page (51 lines) that links to child pages and does **not** mention **Almeida-Sanchez v. United States** or **Byars v. United States**, even though each case's home linkage produced the pair. No shared framing exists on page_b to contradict → CLEAN for R6, but the case↔index home linkage is a cross-reference/coverage question (P1/registry surface), routed for triage.
2. **Frontier-stub status on relied-upon SCOTUS authority — Bell v. Wolfish, FBI v. Fazaga.** Both case pages render header badge "Treatment: **Unverified**" (⚪) while their own Treatment sections describe them as good/foundational authority and multiple doctrine pages cite them as settled law. No cross-page contradiction (leg (i) clean), but the ⚪ frontier-stub state on SCOTUS cases used as settled authority may warrant S6/S9 promotion review. Not adjudicated here.
3. **Mislinked wikilink on a page_b (single-page authoring defect) — PAIR-0047 page_b** (`.../Reverse-Keyword and Geofence Warrants.md`). Prose discussing the Fifth Circuit's *United States v. Smith*, 110 F.4th 817 (5th Cir. 2024) uses the wikilink `[[Smith v. Maryland|Smith]]` at lines ~361, 363, 372 (e.g. "the search-threshold result the Fifth Circuit had reached in *[[Smith v. Maryland|Smith]]*"; line 363 uses both `[[Smith v. Maryland|Smith]]` and `[[United States v. Smith (2024)|Smith]]` for the same 5th-Cir. case). *Smith v. Maryland* (1979) is the pen-register third-party case — a different case; this is a mislinked target. It concerns a case that is **not** the pair's shared item (Chatrie), and is entirely within one page, so it is not an R6 pair contradiction; routed to P1/triage as a link-target fix.
