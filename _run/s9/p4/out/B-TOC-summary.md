# B-TOC extraction summary (packet B-TOC, WS=I3, bootstrap)

Task: extraction-only. Extract chapter/section-grain TOCs from the two reference PDFs to
`_run/s9/p4/toc-lafave.md` and `_run/s9/p4/toc-njleh.md`. No audit performed.
WRITE-SCOPE honored: only `_run/s9/p4/` written. PDFs treated LOCAL-ONLY — read in place from
`.orca/drops/`, never committed or copied; only the derived markdown outlines were written.
Model: claude-opus-4-8. Lane: B-TOC.

## Method
Read tool PDF page support (≤20 pp/request). Each PDF is small (19 pp / 3 pp), so each was read
in a single request. TOCs are front matter; both PDFs' TOC regions were located and transcribed
in full. Titles, numbering, and italicized case names preserved verbatim; printed page numbers
carried through where the source shows them.

## PDF 1 — LaFave, *Search and Seizure* → `toc-lafave.md`
- Source: `.orca/drops/SSTOC.pdf` — 19 pp total (`pdfinfo`: Pages 19).
- Pages read: **all 19 (1–19), one request.** The PDF is TOC front matter only, in two parts:
  - PDF pp. 1–4 = printed pp. xxi–xxiv "**Summary of Contents by Section**" (section grain, no
    subsections, with page numbers). Cross-checked against the detailed TOC — all section start
    pages agree.
  - PDF pp. 5–19 = printed pp. xxv–xxxix "**Table of Contents**" (section + subsection grain,
    with page numbers). This is the fuller version and is what `toc-lafave.md` transcribes.
- Structure: **6 volumes, 11 chapters, 89 sections** (plus lettered subsections a–z, transcribed).
  - Vol 1 = Ch 1 (§§1.1–1.13, 13) + Ch 2 (§§2.1–2.7, 7)
  - Vol 2 = Ch 3 (§§3.1–3.7, 7) + Ch 4 (§§4.1–4.13, 13)
  - Vol 3 = Ch 5 (§§5.1–5.5, 5) + Ch 6 (§§6.1–6.7, 7) + Ch 7 (§§7.1–7.5, 5)
  - Vol 4 = Ch 8 (§§8.1–8.6, 6) + Ch 9 (§§9.1–9.8, 8)
  - Vol 5 = Ch 10 (§§10.1–10.11, 11)
  - Vol 6 = Ch 11 (§§11.1–11.7, 7)
  - Back matter: Table of Cases, Table of Laws and Rules, Table of Secondary Authorities, Index.
- Illegible / skipped: **none.** All pages fully legible. One transcription note flagged for the
  orchestrator, not an error: printed source shows both **§ 6.2(f) No-knock warrants — 453** and
  **§ 6.3 Search before and incident to arrest — 453** on the same page 453 (§6.3 begins on the
  same page §6.2 ends). Transcribed as printed.

## PDF 2 — NJLEH → `toc-njleh.md`
- Source: `.orca/drops/New Jersey Law Enforcement Handbook _ Blue360° Media.pdf` — 3 pp total
  (`pdfinfo`: Pages 3; Title "New Jersey Law Enforcement Handbook | Blue360° Media").
- Pages read: **all 3 (1–3), one request.** This is a Blue360° Media **product/marketing page**
  (Current Edition 2026, Digital Only, $200.00), not the book interior. Its TOC is an expandable
  web outline with **no printed page numbers.** TOC begins at the bottom of p.1 (after the
  price/description block) and runs through p.3.
- Structure captured: **13 chapters across the captured outline** (Volume 1: Chapters 1–10 under
  Part I; Volume 2: Chapters 11–13 under Parts II and III). ~50 sections captured (Vol 1 ≈ 39,
  Vol 2 captured ≈ 11), plus lettered/numbered subsections in Volume 2. Two numbering styles used
  by the source were preserved: Vol 1 "Section 1.1"; Vol 2 "§11.1.". One figure entry captured:
  "Figure 1.1 Staircase of Belief & Proof" (under Section 1.1).
- Illegible / skipped: **none illegible.** BUT the capture is **TRUNCATED**: the outline ends
  mid-tree on p.3 at **§13.2. Cases and Materials.** Everything after that point is absent from
  the PDF — i.e. the remainder of Chapter 13, any Volume 2 Table of Cases / Index, and any
  **Volume 3** (the p.1 marketing text calls this a "comprehensive three-volume guide," yet only
  Volumes 1 and 2 appear in the captured outline). Flagged for the orchestrator: if the I3 chapter
  sweep needs the full NJLEH TOC (Ch 13 remainder + Vol 3), a fuller source capture is required;
  this PDF does not contain it.

## Coverage ledger
- Items assigned: 2 PDFs (SSTOC.pdf; NJLEH product PDF).
- Items examined: 2/2. Pages examined: 19/19 (LaFave) + 3/3 (NJLEH) = 22/22.
- Items skipped: 0. (Note: a third file exists in `.orca/drops/` — `Book Jun 26, 2026.pdf` — but
  it is not named in this packet's scope and was not opened.)
- Outputs written: `_run/s9/p4/toc-lafave.md`, `_run/s9/p4/toc-njleh.md`, this summary.

## For the orchestrator
1. NJLEH TOC is incomplete (truncated at §13.2; no Volume 3 present). Chapter-sweep coverage
   against NJLEH is bounded by this — treat NJLEH chapters 1–12 as complete, Ch 13 as partial,
   Vol 3 as unavailable.
2. LaFave TOC is complete to subsection grain and internally cross-checked (two front TOCs agree).
