# CodeRabbit gate — RETRO-W0W1-quartz @ 8dc4fd3 (base: main)

- run: 2026-07-06T00:30:18Z
- cli: 0.6.4
- mode: --plain --type committed --base main --dir /var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T//cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz
- scope: .coderabbit.yaml path filters (code only) · restricted to quartz

```
Notice: Detected claude environment. Use `coderabbit review --agent` for structured agent-friendly output.
Connecting to CodeRabbit... 7s elapsed
Preparing review... 9s elapsed
────────────────────────────────────────
CodeRabbit Review

Diff      : committed changes only
Compare   : HEAD → main
Directory : cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz
────────────────────────────────────────

(\(\
(• .•)  Code Wars Episode VI: Return of the Unit Tests.

Preparing sandbox... 10s elapsed
Summarizing changes... 16s elapsed
Summarizing changes... 1m 07s elapsed - still working
Finishing analysis tools... 1m 25s elapsed - still working
Writing review comments... 1m 25s elapsed - still working
Writing review comments... 2m 07s elapsed - still working
Writing review comments... 3m 07s elapsed - still working

────────────────────────────────────────────────────────────────────────
  minor [Stability & Availability]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz/components/scripts/spa.inline.ts:136quartz/components/scripts/spa.inline.ts:136-143]8;;

  Guard decodeURIComponent in flashTargetBlock. Malformed
  percent-encoded hashes can throw URIError; the direct same-page click
  path calls this outside navigate()’s try/catch, so a bad hash can break
  the click after preventDefault(). A small try/catch that returns null
  protects both call sites.

Writing review comments... 4m 30s elapsed - still working - 1 finding so far
Writing review comments... 5m 30s elapsed - still working - 1 finding so far
Writing review comments... 6m 30s elapsed - still working - 1 finding so far
Writing review comments... 7m 30s elapsed - still working - 1 finding so far
Writing review comments... 8m 30s elapsed - still working - 1 finding so far

────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz/components/styles/casetable.scss:135quartz/components/styles/casetable.scss:135-141]8;;

  currentColor casing flagged by Stylelint.

  value-keyword-case expects currentcolor (lowercase) at Line 139.





  🧹 Proposed fix

         background: currentColor;
  +      background: currentcolor;


────────────────────────────────────────────────────────────────────────
  major [Functional Correctness]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz/components/styles/casetable.scss:124quartz/components/styles/casetable.scss:124-174]8;;

  Missing focus state on the new interactive a.casetable-pill.

  The treatment pill is now a real ` (per injectCaseMeta` in
  casetable.inline.ts), but this block only defines :hover. Without an
  explicit :focus-visible rule, keyboard users tabbing through the table
  get no assurance of a visible focus indicator on this pill beyond whatever
  (possibly reset) default browser/global styling applies. As per path
  instructions, quartz/ changes should prioritize accessibility.





  ♿ Proposed fix — add a focus-visible style

       &:hover {
         filter: brightness(1.08);
         cursor: pointer;
       }
  +
  +    &:focus-visible {
  +      outline: 2px solid var(--secondary);
  +      outline-offset: 2px;
  +    }

  As per path instructions, "prioritize type correctness, accessibility, and
  not breaking upstream-merge posture".


────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz/components/styles/treatmentBadge.scss:5quartz/components/styles/treatmentBadge.scss:5-9]8;;

  Empty comment line flagged by Stylelint.

  scss/comment-no-empty fires on the bare // at Line 5, same pattern as
  casetable.scss.





  🧹 Proposed fix

   // S3 · R4 #1 — treatment badge (colored, good-law axis) + authority-weight label
   // (neutral outline, separate axis). The two axes are kept visually distinct.
  -//
   // S5 — the pill renders the Field-I COMPOSITE (PRACTICES §2): good-law · history ·


────────────────────────────────────────────────────────────────────────
  minor [Maintainability & Code Quality]
  → ]8;;vscode://file//private/var/folders/vr/4ydf2jp510ldxk10ghhvqm2h0000gn/T/cr-gate-RETRO-W0W1-quartz-vCjaHD/quartz/components/styles/casetable.scss:6quartz/components/styles/casetable.scss:6-10]8;;

  Empty comment line flagged by Stylelint.

  scss/comment-no-empty fires on the bare // at Line 6.





  🧹 Proposed fix

   // untouched until JS runs, and the existing `.table-container { overflow-x: auto }`
   // keeps the fallback horizontally scrollable on mobile.
  -//
   // S5 — the ONE table schema (NUM-07): narrow columns are pinned, holding/relevance


────────────────────────────────────────
Review complete
5 findings ✔

Major    1
Minor    4
────────────────────────────────────────

Print all AI prompts: coderabbit review --show-prompts
```
