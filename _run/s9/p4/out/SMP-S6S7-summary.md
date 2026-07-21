# SMP-S6S7 — S9 R11 per-spec re-verification samples (S6 gate + S7 TEACH-03 by tier)

Packet: **SMP-S6S7** · lane `SMP-S6S7` · model `claude-opus-4-8` · Claude re-verifier (COH-17: cache/lake only, NO live CL).
Outputs (WRITE-SCOPE `_run/s9/p4/` only):
- `out/SMP-S6-sample.jsonl` (21 rows) · `out/SMP-S7-sample.jsonl` (35 rows) · `out/SMP-findings.jsonl` (2 candidates)

## Result headline
- **S6:** 17 gate/floor verdicts + 2 pause-packet disposition checks + 2 adjudication-file censuses — **all CONFIRM.** Both S6 pause packets (A/B) carry recorded USER dispositions.
- **S7:** 34 tier/gate/fix samples — **33 CONFIRM, 1 DISCREPANCY** (Lange T3 bound-volume pinpoint provenance, medium). One additional **low** provenance-hygiene candidate surfaced during an S6 CONFIRM (Vergara Key-2 source URLs).
- **2 candidates** filed to `SMP-findings.jsonl`. The one true sample failure (Lange) **REOPENS the T3 conversion class** per R11.

---

## (A) S6 sample — method + coverage
**Universe & deterministic draw ("every 10th row by file order"):**
| file | lines | sampled lines | N |
|---|---|---|---|
| `_run/s6-candidates/gated.jsonl` | 85 (line 1 = header) | 10,20,30,40,50,60,70,80 | 8 |
| `_run/s6-candidates/frontier-w1-reconciled.jsonl` | 56 | 10,20,30,40,50 | 5 |
| `_run/s6-candidates/frontier-w2-reconciled.jsonl` | 44 | 10,20,30,40 | 4 |
| `frontier-w1-adjudications.md` | 6 bullets + 3 info-flags | **full census** (1-in-10 < 1) | — |
| `frontier-w2-adjudications.md` | ~10 bullets + saturation cert | **full census** | — |

**N = 17 verdict rows** (8+5+4) across 182 verdict rows = 9.3% ≈ 1-in-10 (the "every 10th" rule is the deterministic instrument). Adjudication files examined in full (a census is stronger than a 1-in-10 sample at their size). **Items assigned:** gated 84 + w1 55 + w2 43 = 182 verdict rows + 2 adjudication files + 2 pause packets. **Examined:** 17 sampled + 2 census + 2 packets = 21. **Skipped:** the 165 non-sampled verdict rows (deterministic every-10th selection; not defects).

**Re-verification method (per row):** re-derive the R2 officer-field-relevance / two-key call from (i) the recorded rationale + prong, (ii) the lake record / `_manifest.json` identity, (iii) cached opinion text `~/cssi-lake/cache/text/<opinion_id>.txt` where a holding is asserted, and (iv) the final corpus state (page exists / fold / watch). Cross-checked each reconciled disposition against the frontier adjudication files.

**Notable confirmations:**
- **Case v. Montana** (gated:40) INGEST/a cache-confirmed at op **11240920** — Held "Brigham City objective-reasonableness standard … applies without further gloss; declines a probable-cause spin" matches the rationale verbatim. Lake record's null identity + `status: under_review` is the pre-adjudicated stale-inventory class; the gated row itself flags "page exists (under_review)".
- **Imbler v. Pachtman** (w2:40): adversarial check raised (absolute *prosecutorial* immunity sits near the R2 EXCLUDE "prosecutor craft" line) and **resolved by the recorded adjudication** — `frontier-w2-adjudications.md` rules Imbler+Buckley AUTHOR "squarely prong (c)"; `Absolute Immunity.md` exists. Not a writer freelance.
- **Pause packet A** (`s6-fabrications.md` → "DISPOSITIONS RETURNED (2026-07-06): User: all four groups approved"; `PACKET-A-REKEY-WORKORDER.md`; `DISPOSITIONS-2026-07-06.md`). **Pause packet B** (`packetb-dispositions.jsonl` header "user-delegated 3-agent panel … user directive received this session", 16 terminal items). Both carry recorded USER dispositions. ✔

---

## (B) S7 TEACH-03 sample BY TIER — method + coverage
The R5 conversion trail has **no consolidated file** (per S7-ACCEPTANCE-SWEEP AC-3/AC-8); tiers were extracted per-batch from `_run/o2-execute/JOURNAL.md` + `S7-ACCEPTANCE-SWEEP.md`.

**Tier universe found in the build:**
| tier | definition (S7 R5 / SD5) | conversions in build | sampled | method |
|---|---|---|---|---|
| **T1** CAP star pagination | mechanical star-page cite | 2 (King, Walter) | **2 (all)** | RECOMPUTE star from cache |
| **T2** citing-case co-occurrence (≥2) | corroborated page | **0** | 0 (empty) | — |
| **T3** paraphrase-downgrade | quote → tight paraphrase, no pin | ≥16 (Carpenter, Collins, Caniglia, Lange, Graham, Newman, August, Gaetjens, Cotterman, Cano, Morley, Lewis, Carlton-Williams, Byrd, Perry, Smith-v-Cain, Torres, Herlth …) | **12** | re-verify G2 (paraphrase breadth vs holding, no quote) |

- **T1 (2/2 CONFIRM):** King slip→T1 BOUND 462 — `*462` recomputed in cache op **9441559** (within police-created-exigency reasoning; also fixed the cluster-vs-opinion trap 216733→9441559). Walter ★657 — `*657` recomputed in cache op **9428007** (search-scope-limited-to-authorization passage).
- **T2 (0 available):** no co-occurrence conversions exist; the build's slip-ops were pre-2020 CAP→T1 or post-2020 no-CAP→T3. Reported as size 0 per "where available" — nothing to refute.
- **T3 (11 CONFIRM / 1 DISCREPANCY of 12):** clean paraphrases with first-page-only reporter cites and no fabricated pinpoints (Collins 584 U.S. 586; Cotterman 709 F.3d 952; Cano 934 F.3d 1002; Byrd 584 U.S. 395; Perry 565 U.S. 228; Smith v. Cain 565 U.S. 73; Torres 592 U.S. 306 with "all Torres quotes/pins removed"; Morley 99 F.4th 1328; Herlth state-illustrative; Carpenter 585 U.S.). Caniglia's majority quote is a **valid** case-page slip pin (verbatim recomputed in cache op **4687473**; #^pin-op3 = S2 A3-sanctioned "slip op., at 3"). **Lange = DISCREPANCY (see below).**

**Also sampled (per S9 R11 line 244):**
- **R3 carried-assertion gate rows — 10/10 CONFIRM.** 10 doctrine `[!rule]` propositions (Particularity, Destruction of Evidence, Lineups&RtC, Plain View, Entrapment, SIA Vehicles, 4A Malicious Prosecution, Cell-Site Simulators, Miranda Waiver/Invocation, Probable Cause), drawn every-8th from the 79 `object_class=doctrine` propositions in `assertion-inventory.json`. Each is a sound black-letter statement of controlling authority and is inventoried as its **own** proposition assertion (own `assertion_id`) — S7 R3 no-inheritance realized.
- **R9 fix-list dispositions — 10/10 CONFIRM.** All landed-with-diff-pointer or refuted-with-research-pointer: community-caretaking-reaches-persons (REFUTED→D5 reshape), Matlock→Consent, Herring→Collective-Knowledge + Whiteley exclusion-premise caveat, Riley→Common Law Origins, Dunn→Curtilage Rule, knock-and-talk→implied-license (pattern page), Bandiero/Santana-limited-by-Lange→Exigent, TEACH-04a PC/RS maxim, TEACH-04g persuasive-history→Historical, LAW-05 Zorn legend stripped.

---

## Discrepancies (→ `SMP-findings.jsonl`)
1. **[MEDIUM] `teach03-t3-boundvolume-pin-provenance` — Lange v. California @ Exigent Circumstances and Hot Pursuit.** The T3-tagged, slip-only case carries **bound-volume pinpoints** "594 U.S. 295, [313]" (:48, :50) and "594 U.S. at 303–04" (:47) with **no sanctioned R5 free-source**: cache op **4698186** is slip-only (zero page-number/star markers), the case page pins only "slip op., at 1", and no T2 co-occurrence is recorded anywhere in the journal. Per R5, a post-2020 slip-only SCOTUS case with no T2 hit must be T3 = paraphrase with **no** pinpoint. The paraphrase is holding-accurate (misdemeanor flight not categorical; case-by-case) — the defect is **pin provenance only**. **R11: this failed T3 sample REOPENS the T3 conversion class** — a sweep is owed for any other slip-only SCOTUS case carrying doctrine-page bound-volume pinpoints. `needs_cl:true` to confirm/refute the 313 / 303–04 page numbers against the official reporter (out of a cache-only lane's reach).
2. **[LOW] `frontier-mention-source-provenance` — United States v. Vergara @ frontier-w1-reconciled:20.** Key-2 web sources point to ca1 docket 20-1077 (a different case), not Vergara (11th Cir., 884 F.3d 1309). **Does NOT reopen the gate class:** relevance (below-floor border-search mention) and identity are independently correct in `_manifest.json` + the lake record; a traceability-hygiene note only, no page/assertion rides on it. The S6 sample verdict for this row stays CONFIRM.

## For the orchestrator to rule on
- Whether the Lange T3 finding's class-reopen is scoped to Lange alone or triggers a full slip-only-SCOTUS bound-volume-pinpoint sweep across doctrine pages (recommend the sweep; the pattern — a slip-only case linked to `/opinion/<cluster>/` while asserting a bound-volume page — is mechanically greppable).
- Note (not a defect): the same Exigent page hosts the correctly-landed R9 "Santana limited-by-Lange" fix; the two are independent (fix = point-status prose; discrepancy = pin provenance).
