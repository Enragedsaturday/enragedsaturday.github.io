# CAMP-L3 summary — LINT-3 case-wall -> labeled bullets

Lane `CAMP-L3` · model `claude-opus-4-8` · Authority: P4-WORKER-BRIEF.md; **RULING P4-16(e)**
last sentence ("LINT-3 case-walls -> labeled bullets per S1 A9 (editorial packets)"); S1 **A9 /
TEACH-07**. WRITE-SCOPE: `content/` (the flagged doctrine files) + `_run/s9/p4/campaign/`.

## Scope reconciliation (the "74 / 39" headline)
`python3 scripts/lint/lint3_structure.py content` reports **74 HIGH** rows. Those decompose as:
- **72 case-wall highs** (message "convert the case wall to labeled bullets [S1 A9/TEACH-07]")
  across **38 doctrine files** — **THIS IS THE CAMP-L3 TASK**.
- **2 N5 highs** ("Binding — SCOTUS label in 'Lower-court developments'") in
  `content/seizures/arrests/Arrest and Arrest Warrants.md` **lines 53–54** — a different LINT-3
  sub-check (SCOTUS-placement), explicitly **NOT CAMP-L3's** and left untouched.

So **74 highs = 72 case-wall (mine) + 2 N5 (not mine)**, and the **39 flagged files = my 38 +
that N5-only file**. The deliverable is deterministic **72/72** case-wall paragraphs converted;
the 2 N5 highs are a separate lane's / a later pass's item and remain (no regression introduced).

## Coverage (deterministic)
| | count |
|---|---|
| case-wall paragraphs assigned | 72 |
| examined | 72 |
| converted | 72 |
| skipped | 0 |

Rows: `_run/s9/p4/campaign/CAMP-L3-fixes.jsonl` (one `camp.fix.v1` row per paragraph:
`file, line` [ORIGINAL flagged line], `cases_count`, `technique`, plus `lane/model/task/lint`).
Technique split: **71 `bullets` + 1 `split`** (Plain View Doctrine L56, rule iii). Every worklist
line appears exactly once; no duplicates; `cases_count` matches the lint's reported count on all 72.

## Method (restructuring, NOT rewriting)
Per flagged Explanation-layer paragraph: keep the paragraph's **bold lead-in thesis** as the
prose lead-in (ending in a colon/period), then move each case-proposition onto a **`- ` labeled
bullet**. `lint3_structure.py` counts distinct cases only inside a *prose paragraph*; a `- ` list
item is a paragraph BREAK, so bulleting removes the wall from the density count while the lead-in
it leaves behind stays ≤3 cases. Only these edits were made: inserted `- ` markers + newlines;
splits at existing sentence/semicolon (occasionally serial-list) boundaries; boundary
capitalization; lead-in terminal period→colon; bold around EXISTING words. **No case, cite, pin,
`#anchor`, `[[wikilink]]`, quoted text, or authority-weight label was added, dropped, reworded,
or reordered.** Execution: 2 paragraphs authored by the lane directly; 70 fanned to 7 disjoint
`o2-opus-xhigh` fleet workers (batches A–G) against a fixed method spec, each self-verifying.

## Verification gates (all PASS)
1. **lint3 case-wall = 0** over full `content/` (was 72). Only the 2 non-mine N5 highs remain.
2. **Full 29-lint harness** over the 38 files: **0 highs** (was 72; every one a case-wall). No new
   HIGH on any of the other 28 lints — **zero regression** (LINT-10 em-dash, LINT-16 tables, etc.).
3. **Fidelity gate** (lowercased word-multiset of each file BODY vs `git show HEAD`): **OK on all
   38** — proves no word was dropped/added/altered (bullets/bold/case/punctuation wash out;
   tampering would show as a multiset delta). This catches the fidelity classes lint cannot.
4. **lint3 + lint10 `--self-test`**: PASS (fixtures untouched).
5. **Footprint**: `git diff --name-only HEAD` ∩ my worklist = **38/38**; nothing outside scope was
   authored by CAMP-L3. (The shared worktree carries ~316 other modified files from concurrent
   sibling lanes — content/cases/*, lake, scripts/s2, etc. — NOT CAMP-L3's and untouched by it.)

## Adjudication flags for the orchestrator (all lint-clean; recorded in fixes.jsonl `note`)
- **6 residual >3-case *bullets*** (`residual_bullet_max_cases` field): Miranda&Custodial L49 (4),
  Securing-the-Scene L45 (5, a slash-separated navigation pointer, not case propositions),
  Special-Needs L52 (4), Automobile-Exception L38 (4), Entry-to-Arrest L37 (4), Destruction L39 (4).
  Each is a **single sentence / coordinate citation string with no sentence- or semicolon-level
  split point**; bulleting satisfies the lint (bullets are exempt from the density count, gate = 0)
  but the *soft* ≤3-cases-per-bullet pedagogy target is unreachable without a prohibited rewrite.
  Held intact as the faithful rendering; **not improvised past HARD RULE (i)**. If sanctioned,
  comma-boundary splits reduce each to ≤3 with the word multiset preserved.
- **1 SPLIT** (Plain View L56): integrated analytical passage split into ≤3-case prose paragraphs
  (rule iii) instead of bulleted.
- **2 serial-list splits with colon lead-in** (Arrest-in-the-Home L39; Good-Faith L52): the wall was
  a single serial "gated by A, B, and C" / "does not apply to A, to B, to C, or to D" sentence;
  split at serial-list commas + a colon after the introducing verb/preposition. Mild deviation
  from sentence/semicolon-only splitting; all words preserved (fidelity OK).
- **1 mid-series bullet** (Reasonable Expectation L43, 8-case wall): a comma-preserving break inside
  a coordinate series yields one bullet beginning lowercase "aerial" — a faithful continuation.
- **Pre-existing, out-of-scope (NOT CAMP-L3):** `Community Caretaking.md` carries stray
  `</content>`/`</invoke>` trailer lines at EOF — **present in HEAD**, outside the flagged
  paragraph and outside my diff hunks, causes no lint HIGH; left untouched (noted for hygiene).

## Determinism
72 case-wall paragraphs in, 72 out; lint3 case-wall 72 → 0; harness 72 → 0; fidelity 38/38 OK.
