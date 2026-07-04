---
title: LINT-3 N5 fixture
type: doctrine
jurisdiction: Fourth Amendment
---

# LINT-3 N5 fixture

Acceptance fixture for the **rewritten, lake-driven LINT-3 (b) N5 check** (S1 A2 concretization;
COH-28 adjudicated F-DEMO-001, `_overhaul2/s9-demo/`): inside a frontier section
(`Recent developments` / its S5 R11 successor `Lower-court developments`), fire HIGH on any line
that (i) carries a `Binding — SCOTUS` label, (ii) wikilinks a case page whose lake `court` is
SCOTUS, or (iii) carries a U.S./S. Ct. reporter cite as the entry's own cite. A bare descriptive
`SCOTUS` token on a circuit-subject line (subsequent-history status label) does NOT fire.

**Expected under the rewritten check: TP-1..TP-4 fire HIGH; FP-1/FP-2 do not.**
**Baseline (current token-window lint):** on the pre-rename fixture (`## Recent developments`,
2026-07-04) it fired HIGH on all six shapes — the two descriptor-only shapes are its known
over-detection, and its 45-char window separately under-detects; both die with the rewrite.
After the coherence-pass heading rename below (TEACH-08), the current lint scopes NOTHING here
(its `recent-dev*` hints don't know the successor heading) — a third defect the rewrite fixes.
Do NOT patch the window heuristic — the panel killed that fix (breaks true positives two ways;
see f-001.adjudication.json).

## The Brief

Filler brief section so the section-order check stays quiet.

## Key cases

| Case | Holding | Opinion |
| --- | --- | --- |

## Lower-court developments

<!-- Heading per TEACH-08/S5 R11 (the frontier section's post-S7 name). The rewritten LINT-3
must scope this check to BOTH `Lower-court developments` (current) and the legacy
`Recent developments` (whose survival post-S7 is itself a LINT-15 rename violation). -->

- **TP-1 (FIRES — own U.S. reporter cite): *Riley v. California*, 573 U.S. 373 (2014)** — a SCOTUS holding narrated inside the frontier section.
- **TP-2 (FIRES — explicit court tag): *Torres v. Madrid* (SCOTUS 2021)** — explicit designation, no preceding circuit reference.
- **TP-3 (FIRES — cert-from-circuit shape): *Riley v. California*, on cert from the 9th Cir., 573 U.S. 373** — a circuit reference precedes, but the entry's own cite is a U.S. reporter cite. Pins the shape both Codex refuters used to kill the circuit-ref-suppression patch.
- **TP-4 (FIRES — the live-line shape: descriptor + taught holding): *United States v. Chatrie* (4th Cir.) → superseded by SCOTUS.** The Supreme Court held in *[[Chatrie v. United States]]*, 609 U.S. ___ (2026), that acquiring geofence Location History **is** a search (**Binding — SCOTUS**). — teaches the SCOTUS holding + SCOTUS-court wikilink + label inside the frontier section (the TEACH-01 class; the two live HIGHs at Standing:80 / ER:129 are this shape and stay red until S7 relocates them).
- **FP-1 (does NOT fire — descriptor-only, parenthesized circuit subject): *United States v. Chatrie* (4th Cir.) → superseded by SCOTUS; see Key cases.** — status label only; no holding taught, no SCOTUS-court wikilink, no U.S. cite. The legitimate post-S7 clean shape.
- **FP-2 (does NOT fire — descriptor-only, backtick circuit label): *United States v. Chatrie*** `4th Cir. → superseded by SCOTUS` — same class without parentheses (the ER:129 label shape, stripped of the taught holding).

## Sources

- [*Riley v. California*, 573 U.S. 373 (2014)](https://www.courtlistener.com/opinion/2687642/riley-v-california/)
