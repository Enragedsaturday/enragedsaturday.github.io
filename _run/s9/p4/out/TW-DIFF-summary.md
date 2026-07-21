# TW-DIFF summary (P4 / tripwire 13-cat re-run — reconciliation stage)

lane `TW-DIFF` · model `claude-opus-4-8` · 2026-07-21 · governed by RULING P4-07/P4-08
Write-scope: `_run/s9/p4/` only. Findings-only; the tripwire-CLOSURE verdict is the orchestrator's.
I5-DIFF units (digital/civil/foundations) are NOT re-diffed here — their classifications stand.

## Coverage (deterministic, per brief rule 4)
- **Items assigned:** 270 raw candidate rows — codex web_search lanes (10 TW-*.txt): confessions 15 · counsel 20 ·
  exclusionary 18 · fairtrial 20 · foundcraft 26 · searches 21 · seizures 39 · standards 24 · warrant 30 ·
  warrantexc 25 = **238**; Claude lanes TW-CLAUDE-1 20 + TW-CLAUDE-2 12 = **32**.
- **Items examined:** 270 / 270 (0 parse failures; codex `.txt` were clean JSONL, no prose-wrap recovery needed).
- **Union result:** 270 → **220 distinct cases** after dedup (normalized parties + circuit-bucket + year;
  docket-connected-component sub-split; reporter-cite + SCOTUS-caption-flip cross-key merges). Notable merges:
  Wilson 5th-2025 SPLIT into two real cases (23-30777 Terry / 25-30105 warrant); Gonzalez-Arocho MERGED across
  lanes (docket 25-1041, year-label 2025 vs 2026) → two-key; Chatrie SCOTUS caption-flip merged (25-112).
- **Items skipped:** 0.
- **Recency triage:** 152 citing-decision rows across 13 category queries examined (2 categories null-returned).

## Dual-model overlap (per unit + global)
| unit | union | both | codex-only | claude-only |
|---|---|---|---|---|
| standards | 26 | 1 | 23 | 2 |
| searches | 29 | 1 | 20 | 8 |
| seizures | 40 | 2 | 37 | 1 |
| warrant | 30 | 3 | 27 | 0 |
| warrantexc | 26 | 1 | 24 | 1 |
| exclusionary | 20 | 1 | 17 | 2 |
| confessions | 18 | 0 | 15 | 3 |
| counsel | 20 | 1 | 19 | 0 |
| fairtrial | 20 | 2 | 18 | 0 |
| foundcraft | 28 | 1 | 25 | 2 |
| **global (model-level)** | **220** | **13** | **190** | **17** |

Codex ran far broader (deep circuit tail); Claude ran narrower/SCOTUS-weighted. Per-unit "both" counts lane
agreement WITHIN a unit; global "both" (13) counts agreement anywhere (a case codex/Claude filed in different units,
e.g. Gonzalez-Arocho, is global-both but per-unit single-lane).

## Accounting result (220 distinct cases)
| classification | count |
|---|---|
| IN-CORPUS | 25 |
| ACCOUNTED-DISPOSITIONED | 22 |
| NOT-ACCOUNTED | 170 |
| RULED (P4-07) | 3 (Lowers, House, Brillhart; Pung not in TW union) |

**Method note / reliability:** DOCKET and REPORTER-CITE are the reliable accounting signals; caption-name match is
collision-prone for common surnames (Wilson/Williams/Johnson/Smith/…) and is used only as distinctive-rare-token
corroboration (geographic/generic tokens excluded). This surfaced **15 false IN-CORPUS page-name collisions** in the
first pass — e.g. corpus `United States v. Wilson` = 9th Cir. 2021 (13 F.4th 961), NOT the 5th Cir. 2025 Terry case;
corpus `United States v. Williams` = 9th Cir. 2006, NOT the 4th Cir. 2025 knock-announce case — both corrected to
NOT-ACCOUNTED. The 170 NOT-ACCOUNTED case-count is deliberately CONSERVATIVE (a common-surname case without a
docket/cite hit is counted absent rather than falsely accounted); residual single-key name-collision noise is
documented and does not touch the two-key set. A large NOT-ACCOUNTED count is expected — the codex lane cast a wide
frontier net and a teaching wiki does not page most 2024-26 circuit dispositions.

## Tripwire input — FOUR new TWO-KEY NOT-ACCOUNTED cases (fail-closed; verdict is orchestrator's)
Tripwire already FIRED (P4-07, Lowers predicate). The 10-category re-run adds **4** two-key NOT-ACCOUNTED cases the
ruled set did not list — all published federal circuit, all airtight-absent (docket+reporter grep=0 across
corpus/lake/S6):

| case | court / date / cite | doctrine | class_saturation | note |
|---|---|---|---|---|
| **United States v. Johnson** | 4th Cir. 2025 · 148 F.4th 287; 23-4255 (cert. den. 25-774) | canine sniff, apartment common hallway | **PARTIAL** | split flagged in corpus (Curtilage.md: May-Shaw + "lower courts split") but the FEDERAL canine-apartment-door split (Whitaker 7th vs Johnson 4th) in NO S6 log — **strongest additional-discovery-miss candidate** |
| **United States v. Wilson** | 5th Cir. 2025 · 23-30777 | post-Bruen gun-possession as RS for Terry stop | **PARTIAL** | armed-alone FRISK split catalogued; post-Bruen-STOP question not (0 "Bruen" in content/seizures/); holding rests on other facts |
| **United States v. Williams** | 4th Cir. 2025 · 130 F.4th 177; 23-4568 | knock-and-announce, no suppression (Hudson) | **SATURATED** | knock-and-announce fully in corpus; below-floor reaffirmance |
| **United States v. Gonzalez-Arocho** | 1st Cir. 2025/26 · 25-1041 | good-faith rejected / warrant-scope (wrong device) | **SATURATED** | good-faith UNIFORM per S6 exclusionary stop; below-floor fact-bound suppression win |

**Orchestrator call:** Only **Johnson** (and secondarily **Wilson**) present a gate-passing question S6's saturation
logs do NOT explicitly account for — the same "class-flagged-in-corpus vs case-absent-and-not-S6-catalogued" posture
as the Lowers predicate. Williams and Gonzalez-Arocho reaffirm settled, fully-covered doctrine (below floor). All four
carry `needs_cl:true` (existence/holding confirmation; none in lake).

**Single-key SCOTUS-level flags** (below the two-key threshold; analogous to I5-DIFF's Pung): **Klein v. Martin**
(SCOTUS 2026, No. 25-51, summary reversal of a 4th Cir Brady habeas grant on AEDPA deference — arguably out of the
officer-facing remit); **Gonzalez v. United States** (SCOTUS 2025, No. 24-5577, cert DENIED + Sotomayor/Gorsuch
statement on the in-the-presence misdemeanor-arrest rule — no holding; doctrine-ferment node the corpus lacks);
**Loper Bright** (Chevron overruling — out-of-remit admin law, correctly absent). All `needs_cl` except Loper Bright.

## TW-CLAUDE-1 flag verification — 22-4489 "hash-match cert grant"
**REFUTED — CONFLATION** (`needs_cl:false`, resolved offline). Docket **22-4489 = Chatrie's CA4 docket for the
GEOFENCE case** (10 codex rows cite it, all describe geofence: panel 107 F.4th 319 → en-banc grant → en-banc merits
136 F.4th 100). Its SCOTUS stage = **Chatrie v. United States, No. 25-112, 609 U.S. ___ (2026)** = **IN-CORPUS**. The
hash-match 4th Cir. case is **Lowers, 24-4546** = **RULED** (P4-07). The flag fused Lowers's hash-match holding +
Chatrie's docket 22-4489 + a spurious "2026-01-20 cert grant"; no such hash-match case/cert-grant exists in
corpus/lake/S6 or either lane's docket evidence. TW-CLAUDE-1's own summary flagged the docket mismatch. **Not a new
not-accounted case.**

## Recency triage (152 citing decisions)
Floor filter (published SCOTUS / federal circuit only) → 64 rows → **31 distinct clusters** (0 SCOTUS; all federal
circuit). **ALL 31 postdate the S6 run (2026-07-06; dateFiled 2026-07-06..07-21) and NONE is in corpus/lake.** Per
P4-07 currency logic (Brillhart/Pung non-charging), these are **R7.1 currency-watch, NOT pre-build discovery misses**;
none trips P4-03. Captions are routine circuit dispositions citing the corpus canon; doctrine-shaping status is
unverified offline (`needs_cl` on any the orchestrator promotes). One worth a note: **United States v. Richard
Brillhart** (11th Cir., docket **24-13232**) — DISTINCT from the tripwire Brillhart (24-13226, RULED) — likely a
companion/co-defendant appeal in the same CSAM/private-search matter.

## Ambiguities / calls flagged for the orchestrator
1. **Johnson (and Wilson) class-flagged-in-corpus vs case-absent-and-not-S6-catalogued** — the central further-miss
   judgment. Classified case-level NOT-ACCOUNTED (airtight) with class-saturation annotated; verdict left to the orchestrator.
2. **Two-key severity vs floor** — Williams/Gonzalez-Arocho are two-key but reaffirm doctrine the corpus fully covers
   (SATURATED). Reported high (two-key) for visibility; the orchestrator may floor them.
3. **Single-key NOT-ACCOUNTED bulk (141 low / 20 medium)** — conservative name-collision-noisy tail; below the two-key
   threshold. Reliable-signal (docket/cite) accounting used; residual imprecision documented.
4. **Loper Bright / ABA Formal Op. 512 / AI-citation-sanctions** — instructor-reference / out-of-remit items surfaced
   by codex/Claude foundcraft lanes; recommend R12 maintenance handoff, not S6 R8 born-draft.

## Outputs
- `_run/s9/p4/out/TW-DIFF.json` — per-unit union tables + case lists, overlap stats, accounting counts, the 170-row
  NOT-ACCOUNTED list (two-key status / class-saturation / severity / needs_cl / airtight evidence), the 4 two-key
  cases, the 22-4489 flag resolution, the recency-triage block (31 survivors), the S6 saturation catalogue, and the
  tripwire-input assessment.
- `_run/s9/p4/out/TW-DIFF-findings.jsonl` — 170 `p4.candidate.v1` rows, class `frontier-unaccounted`
  (severity high 9 / medium 20 / low 141; needs_cl true 170), each pointing to its source candidate row.
