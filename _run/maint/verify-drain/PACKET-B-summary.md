# PACKET B — `slip_opinion` status

## Files changed

- `_overhaul2/lake/_schema.json` — added `slip_opinion` to the top-level lake
  status enum and changed no other schema rule.
- `quartz/components/DraftBanner.tsx` — renders a dedicated 📄 informational
  banner for `lake.status: slip_opinion`, with the required copy, class, and
  `data-lake-status`; the existing ⚪ unverified banner remains unchanged for
  draft and unverified states.
- `quartz/components/styles/draftBanner.scss` — added neutral light/dark theme
  styling for `.slip-banner` while sharing the existing banner layout.
- `quartz/components/caseHelpers.ts` — suppresses the draft/unverified banner
  predicate for slip opinions and data-drives the resolved treatment label to
  `Slip opinion` when a slip page would otherwise display `Unverified`.
- `quartz/components/caseHelpers.test.ts` — covers the slip-opinion pill label
  and suppression of the unverified draft-banner predicate.
- `scripts/s2/project.py` — added a self-test fixture proving
  `slip_opinion` passes through to projected `lake.status` verbatim; no projector
  allowlist was present or added.
- `scripts/lint/lint6_treatment_status.py` — distinguishes the informational
  slip banner from the unverified warning and tests that slip status wins even
  when Field-I is `unverified`.
- `scripts/lint/lint14_pagerecord.py` — admits `slip_opinion` through the
  page-to-record publish gate and covers it in the self-test record map.
- `scripts/lint/README.md` — documents the complete current LINT-14 accepted
  status set.
- `scripts/lint/fixtures/lint-6-slip-opinion-pass.md` — pass fixture for a
  slip-opinion page with unverified Field-I and complete dual dates.
- `scripts/lint/fixtures/lint-6-slip-opinion-null-date-fail.md` — fail fixture
  proving the informational slip banner does not waive dual treatment dates.
- `scripts/lint/fixtures/lint-14-page-slip-opinion-pass.md` — pass fixture for a
  page backed by a `slip_opinion` lake record.
- `_run/maint/verify-drain/PACKET-B-summary.md` — this implementation and
  verification record.

No file under `content/` or `_overhaul2/lake/cases/` was changed by this lane.

## Acceptance

- `python3 scripts/s2/project.py --self-test` — **PASS** (exit 0), including
  `slip_opinion status passthrough -> OK`.
- `python3 scripts/lint/run_all.py content` — all lint self-tests pass;
  LINT-6 and LINT-14 report zero findings. Before this lane, the corpus roster
  was 898 total (3 high / 884 medium / 11 low). The final snapshot is 1,054
  total (159 high / 884 medium / 11 low): the unchanged medium/low counts and
  zero LINT-6/LINT-14 findings show zero new findings from this lane. The +156
  LINT-13 highs come exclusively from concurrently modified
  `_overhaul2/lake/cases/*.json` files outside this lane.
- `npx quartz build` — **BLOCKED by a pre-existing pre-build bundler memory
  leak**. The exact command exits 134 at Node's 4 GB heap limit. Stable Node 24,
  single-thread, and 8 GB retries fail identically before the transpiled cache
  advances. A controlled 1 GB run with all three changed component/style files
  restored byte-for-byte to `HEAD` reproduces the same failure, proving it is
  independent of this lane. A final 128 GB-ceiling run was stopped after nine
  minutes and more than 40 GB of growth with no cache progress to protect the
  shared host. Focused `npx tsc --noEmit`, Sass compilation, and 15 helper tests
  pass.

## Additional verification

- `node --import tsx --test quartz/components/caseHelpers.test.ts` — **PASS**,
  15/15 tests.
- `npx tsc --noEmit` — **PASS**.
- `./node_modules/.bin/sass quartz/components/styles/draftBanner.scss
  /tmp/slip-draft-banner.css` — **PASS**.
- `python3 scripts/lint/lint6_treatment_status.py --self-test` — **PASS**.
- `python3 scripts/lint/lint14_pagerecord.py --self-test` — **PASS**.
- Two-axis code review — **PASS after correction**. The final recheck found no
  remaining standards/code-smell findings and no implementation-spec findings;
  the only remaining spec exception is the independently reproduced build
  blocker above.
- Scoped `git add`/commit — **BLOCKED by workspace permissions**:
  `.git/index.lock: Operation not permitted`. No files were staged.
