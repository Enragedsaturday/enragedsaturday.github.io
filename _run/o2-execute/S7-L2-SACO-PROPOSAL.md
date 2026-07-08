# S7-L2 SACO / Constructive-Entry — Pre-Mint Identity + Reliance Proposal (PHASE a)

- **Lane:** mini-lane L2 phase (a) · `{lane: o2-execute-S7-L2, model: claude-opus-4-8}`
- **Spec authority:** S7 §3 R10 (D7) + §10 D7 + §11 annex; S6 R6/A1 frontier floor + planning-time candidate sub-leg; S6 R11 terminal enum.
- **Status:** READ-ONLY (lake/content untouched). Identity + holdings verified. **Nothing minted / committed / mutated except this artifact.** Orchestrator adjudicates before phase (b).
- **CL usage:** 16 MCP calls (5 identity searches + 5 opinion-id pulls + 6 `search_document` text checks). **ZERO REST** (no `call_endpoint`/`get_endpoint_item`). SEARCH-first; every id resolved from result payloads, none guessed.
- **Budget guard note:** S6 close reported authored pages **148 ≤ §9 guard 150**. 3 SACO mints → **151 may breach 150** (see §5 fallback).

---

## 1. Identity table (verified facts + evidence pointers)

All six SACO-family captions + Harris. Cites match signed S6 A1 exactly (A1 corrected the task-prompt's Nora guess: **765** F.3d 1049, not 743).

| Case | Canonical cite | Court / year | cluster_id | lead opinion id | Tree/ledger status | Holding relied on by D7 — VERIFIED |
|---|---|---|---|---|---|---|
| **United States v. Nora** ("…v. Johnny Casel Nora") | 765 F.3d 1049 | 9th Cir. 2014 (Watford, J.) | **2722177** | 2722177 (combined) | **NO page / NO terminal** | Surround-and-call-out (20–30 officers, weapons drawn, PA "come out") = constructive entry → in-home arrest; **perimeter defeats flight/danger exigency at \*1055** (verbatim); distinguishes *Al-Azzawy* 784 F.2d at 894. Docket 12-50485. |
| **United States v. Al-Azzawy** ("…v. Riad Abed Al-Azzawy") | 784 F.2d 890 | 9th Cir. 1986 (Beezer, J.) | **465254** | 465254 (combined) | **NO page / NO terminal** | Trailer surrounded, bullhorn order to emerge; "only emerged under circumstances of extreme coercion, the arrest occurred while he was still inside his trailer" (894–95); arrest location = suspect's position. Court **affirmed** arrest-was-inside **but reversed suppression** on exigency (armed threats/grenades). Docket 85-5004. |
| **United States v. Vaneaton** ("…v. Jack Palmer Vaneaton") | 49 F.3d 1423 | 9th Cir. 1995 (Trott, J.) | **691388** | 9487908 (lead) / 691388 (combined) | **NO page / NO terminal** | Arrested "just inside the open door" of motel room after **voluntarily** opening to a knock → **no Payton violation** (voluntary-exposure pole). Tashima, J., dissenting (id 9487909). Docket 93-30387. |
| **Fisher v. City of San Jose** | 558 F.3d 1069 | 9th Cir. 2009 **en banc** (Tallman, J.) | **1355654** | 9597796 (lead) / 1355654 (combined) | **NO page / NO terminal** | Armed-standoff exigency; "we address the Fourth Amendment's exigent circumstances doctrine in the context of armed standoffs"; point-of-seizure / "constructive arrest" analysis. Docket 04-16095. Dissents: Paez (9597798), Reinhardt (9597799). |
| **United States v. Allen** | 813 F.3d 76 | 2d Cir. 2016 (Lynch, J.) | **8442555** | 8413824 (lead) / 8413825 (Lohier concur) | **NO page / NO terminal** | "where law enforcement officers have summoned a suspect to the door of his home, and he remains inside the home's confines, they may not effect a warrantless 'across the threshold' arrest in the absence of exigent circumstances" (~84); Reed line (\*83); protection extends beyond actual trespass (\*86). Docket 13-3333-cr. **RESOLVED — this is the signed 2d-Cir. Allen** (A1). |
| **United States v. Maez** | 872 F.2d 1444 | 10th Cir. 1989 | 521939 | (null — stub) | **PAGED** (`content/cases/United States v. Maez.md`, `homes:[[Arrest in the Home]] role Key`); lake `under_review`, treatment `unverified` (frontier stub) | 10th-Cir. split representative. No mint needed. **Owed:** enrich/verify treatment + internal pincite if D7 prose pincites it. |
| **New York v. Harris** | 495 U.S. 14 (1990) | SCOTUS 1990 | 112413 | 9431975 | **PAGED / verified** (`homes:[[Arrest in the Home]] role Limiting`) | The remedy tail: a Payton violation does **not** require suppressing a statement made **outside** the home; remedy reaches only what is gathered inside. **Available — no action.** |

---

## 2. Alias / supersession traps (booked for phase b — fail-closed)

- **Fisher v. City of San Jose ≠ Michigan v. Fisher** (existing SCOTUS page). Distinct court/cite (S6 A1 R9 flag confirmed). **Mint/cite only the en banc 558 F.3d 1069 (cluster 1355654).** Superseded panel opinions **509 F.3d 952 (2007, cluster 1201772)** and **519 F.3d 908 (2008, cluster 8440233)** must **not** be minted (Anderson-supersession precedent).
- **Al-Azzawy — two 9th-Cir. appeals:** SACO case = **784 F.2d 890 (1986, cluster 465254, docket 85-5004)**. The earlier **768 F.2d 1141 (1985, cluster 456032, docket 84-5367)** is a different appeal — do not fold/mint.
- **Allen — many namesakes:** signed case = **813 F.3d 76 (cluster 8442555, Lynch J.)**. NOT *American Honda Motor Co. v. Allen* (7th Cir., 600 F.3d 813, cluster 1364) or *Newsom v. Friedman* (76 F.3d 813 noise).
- **Nora:** citation 765 F.3d 1049 is unique (search count=1); full caption "United States v. Johnny Casel Nora."
- **UNSIGNED cases named INSIDE the paged/terminal cases — DO NOT NAME in D7 prose without a terminal (LINT-17 fail-closed, L1 precedent):** *United States v. Morgan* 743 F.2d 1158 (6th Cir. 1984) [cited in Al-Azzawy — also an A1 "three distinct Morgans" alias trap], *Knight v. Jacobson* 300 F.3d 1272 (11th Cir. 2002) and *United States v. Berkowitz* [both canvassed inside Allen as the narrow side]. None is in signed material → teach the narrow/6th positions by **circuit-naming only**, not by naming these cases.

---

## 3. Page-vs-terminal recommendation (S6 D5 frontier floor + reliance test)

**Floor (S6 R6, verbatim):** page only if *clearly controlling* (SCOTUS or binding-in-circuit on an omitted question) **or** a *split-marker* (both sides, circuits named); else Lower-court-developments bullet; **bullet→page conversion only when S7 prose relies on it.** LINT-17: every case **named in prose** needs a terminal.

| Case | Recommendation | One-line frontier-floor / reliance justification |
|---|---|---|
| **Nora** | **PAGE (mint)** | Spec-designated **spine**; prose quotes + pincites \*1055. Reliance at spine+pincite grain — non-negotiable per D7. |
| **Al-Azzawy** | **PAGE (mint)** | Doctrinal root of the 9th-Cir. constructive-entry rule; the spine literally pincites it (Nora → 784 F.2d at 894); supplies the coerced-emergence pole of the required **containment-vs-exit-command line** at holding grain. |
| **Vaneaton** | **PAGE (mint)** — *primary*; brief-mention terminal = economy fallback | Supplies the **voluntary-exposure** pole of the containment-vs-exit-command line (a spec-required element). Reliance = holding grain. Fallback to terminal if the §9 page guard binds (§5) or the line is taught by one-clause contrast without a Vaneaton pincite. |
| **Fisher v. City of San Jose** | **TERMINAL (brief-mention)** | Armed-standoff exigency counterpoint to Nora's exigency-absent holding; a split/refinement marker but **not** a D7 spec-required named element → prose does not rely at page grain. Pincite in the roster; identity note carries the alias/supersession traps (§2). |
| **Allen** | **TERMINAL (brief-mention)** | 2d-Cir. split representative. Page-**eligible** (binding-in-circuit + split-marker) but the split is taught with **Nora as spine**; Allen rides as a pincited roster entry — the L1 pattern ("split taught w/ page-backed circuits + brief-mention terminals"). Page = escalation only. |
| **Maez** | **no action** (already paged) | 10th-Cir. rep, Key on Arrest in the Home. *Owed:* treatment enrich if pincited. |
| **New York v. Harris** | **no action** (already paged, verified) | Remedy tail available. |

---

## 4. D7 section reliance map (proposition → case → grain)

| # | D7 proposition (spec §3/§10 R10) | Case(s) | Grain needed | Coverage |
|---|---|---|---|---|
| P1 | The circuit split: recognizing side **2d/6th/9th/10th** vs narrow physical-crossing side **5th/7th/11th**; **1st/3d/4th/8th unmapped (stated honestly)** | Nora/Al-Azzawy/Vaneaton (9th), Allen (2d), Maez (10th) | **circuit-naming** (no case pincite needed for LINT-17); anchor cases where signed | **2d/9th/10th backed.** 6th recognizing-circuit + entire 5th/7th/11th narrow side have **NO signed case** → honest "aligns / requires physical crossing (representative case not mapped in this build)" framing; **fail-closed** on Morgan/Knight/Berkowitz (§2). |
| P2 | **Nora as spine**: surround-and-call-out → constructive entry → in-home arrest; police force the exit | Nora | quoted holding + pincite (765 F.3d at 1053–\*55) | Nora **PAGE**. Verified verbatim. |
| P3 | **Perimeter defeats flight/danger exigency** (Nora at 1055) | Nora (+ contrast to Al-Azzawy at 894) | **pincite \*1055 (verified verbatim)** | Nora **PAGE** carries it; Al-Azzawy relied-on at 894. |
| P4 | **Containment-vs-exit-command line**: coerced emergence from a contained home = in-home arrest **vs** voluntary doorway exposure = no violation | Al-Azzawy (coerced pole, 894–95) · Vaneaton (voluntary pole, ~1425–27) | both poles at holding/pincite grain | Al-Azzawy **PAGE** + Vaneaton **PAGE** (primary). |
| P5 | Exigency **can** be present (standoff counterpoint) | Fisher (armed standoff, en banc) | illustrative pincite only | Fisher **TERMINAL** (not spec-required at page grain). |
| P6 | **Harris remedy tail**: Payton violation ≠ suppression of out-of-home statements | New York v. Harris | already paged | **No action.** |

---

## 5. Phase (b) work order DRAFT (orchestrator adjudicates before any mint)

### Scope-guard gate (resolve FIRST)
S6 close = **148/150** authored pages. **PRIMARY (3 mints) → 151 > 150 guard.** Orchestrator must confirm guard scope before the 3rd mint:
- **(A)** If SACO pages were pre-counted in the 150 planning envelope (S6 A1 pre-seed listed the SACO family) → PRIMARY 3-page plan proceeds.
- **(B)** If not → either invoke RUNBOOK §4 scope-guard pause (surface count) **or** adopt the **FALLBACK: 2 pages** (Nora + Al-Azzawy) with **Vaneaton → brief-mention terminal** (voluntary pole taught by pincited contrast), holding at **150**.

### Mint list (standard leg — identity Key-1 ALREADY DONE here, phase b skips to enrich→mint)
| Case | Homes[] (proposed) | Est. cost (identity pre-done) |
|---|---|---|
| **Nora** (cluster 2722177 / op 2722177) | `[[Arrest in the Home]]`/`[[Entry to Arrest]]` role **Key**; related Payton, Al-Azzawy, Vaneaton, New York v. Harris | ~4–6 MCP (enrich treatment/progeny) + authored BIRAC body |
| **Al-Azzawy** (cluster 465254 / op 465254) | `[[Arrest in the Home]]` role **Key**; related Payton, Nora, Johnson, Santana | ~4–6 MCP + body |
| **Vaneaton** (cluster 691388 / op 9487908) — *primary; terminal in fallback* | `[[Arrest in the Home]]` role **Key/Limiting**; related Payton, Nora, Al-Azzawy | ~4–6 MCP + body |

Per-page mint = enrich → S5 R3 BIRAC skeleton + projected frontmatter + R12 Sources + `opinion` anchor + R16 pins → stub→record promotion → Case-Index row → homes[] Key/Related rows on `[[Arrest in the Home]]`/`[[Entry to Arrest]]` → ledger `authored` row; LINT-15/17 green. **Total mint estimate ~14–18 MCP calls** (3 pages) or ~10–12 (2-page fallback).

### Terminal list (brief-mention — L1 lightweight path; identity+pincite captured)
| Case | Terminal | Pointer / pincite |
|---|---|---|
| **Fisher v. City of San Jose** (cluster 1355654 / lead 9597796) | `brief-mention` | Entry-to-Arrest D7 section, standoff-exigency roster; pincite 558 F.3d at ~1074–79 (pin in phase b); identity note = alias/supersession traps §2 |
| **Allen** (cluster 8442555 / lead 8413824) | `brief-mention` | Entry-to-Arrest D7 split roster, 2d-Cir. entry; pincite 813 F.3d at ~84–86 |

Terminals = `build_coverage_ledger` regen (partition +2) + in-write LINT-17 allowlist + page-naming pincite patch. **~2 MCP calls total** (pincites already captured; may need 1 read each to pin exact internal page).

### Honest gaps carried to phase (b)
1. **6th-Cir. recognizing circuit + 5th/7th/11th narrow side: NO signed case.** Teach by circuit-naming + honest "not mapped in this build." Do **not** name Morgan/Knight/Berkowitz (fail-closed, §2).
2. **Maez** treatment `unverified` (stub, op id null) — enrich if D7 pincites the 10th-Cir. rep.
3. **Vaneaton / Fisher internal pincites** not pinned to exact page in phase (a) — pin during phase (b) enrich (holdings verified; page numbers TBD).
4. **§9 page guard** gate above must clear before the 3rd mint.
