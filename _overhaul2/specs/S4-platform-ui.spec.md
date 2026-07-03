# SPEC S4 — Platform, Nav & Reader-Signaling UI (the working standard)

status: APPROVED
depends-on: [S1]   gates: [S5, S8]   exec-wave: 1 (concurrent with the S2 lake build)
last-updated: 2026-07-03

> The platform layer that makes the reference *work*: the **TOC-tree explorer** (adopted from S3's
> signed-off prototype, R11, and corrected where the prototype was empirically wrong), the
> **typo-tolerant case-name search**, the **reader-signaling mechanisms** (treatment pill as a real
> link with provenance hover — the *mechanism*; S5 owns placement/format, audit COH-18), the **About
> page** that absorbs attribution + the currency explanation, and the **publish-pipeline reconcile to
> `content/`-canonical, Vercel-only** (user decision, 2026-07-03). Everything here was locked on a
> **live mockup** (commits `37d6f4f` + `bd50770` on `overhaul2/planning`, served over Tailscale) —
> the spec follows the mockup to the letter; where a requirement below says *"as mocked"*, the mockup
> commit is the normative reference. Read with `PRACTICES.md` §7 (reader-facing signaling) and the
> RUNBOOK §4-S4 entry. Conforms to S1; consumes S3's A8 ordering decision (frontmatter `weight:`).

## 1. Objective
Make the platform trustworthy and pleasant before the S3 restructure pours into it (exec wave 1):
a nav that can hold a 13-category, ≤3-level tree without scroll jank or unreachable overviews; search
that rescues case-name typos; treatment signaling a reader can *interrogate* (hover → provenance,
click → methodology); one canonical publish path (`content/` → build → Vercel) with the stale
vault-sync pipeline retired; and an honest, settled platform posture (freeze-and-own the Quartz 4.5.2
fork).

## 2. Scope
### 2.1 In scope (S4 designs + executes)
The explorer/nav model (TOC-tree: whole-header category toggle + `Overview` first-child row + always-
open sub-branches with link headers + connectors) and every explorer fix (scroll container, save/
restore, mobile drawer, wrap, spacing, quirks); the **weight-reading `sortFn`** + the `ContentDetails.
weight` content-index extension it requires (A8); FlexSearch **did-you-mean** (tolerant title index +
chip strip); the **pill/anchor/hover mechanism** (TreatmentBadge + casetable badges as `a.internal`,
popover delegation, provenance tooltip template); the **About page** + footer rework; the **publish
reconcile** (retire `redeploy.sh` vault sync + `com.cssi.quartz` launchd server + `serve-public.py`;
re-point `/cssi-ingest` to `content/`-canonical); the keep-Quartz-vs-fork posture; `quartz.layout.ts`
hygiene (CODE-05).
### 2.2 Out of scope (owned elsewhere)
Pill **placement/format inside entry models** + table schema/columns (**S5** — COH-18 boundary; S4
ships the mechanism and a default template only). The tree's *content* — categories, re-homing,
overviews (**S3**; S4 renders whatever tree `content/` holds). Treatment *data* — status, dual dates,
notes (**S2** projection; S4 renders the fields it finds in frontmatter). Term/case linking density
(**S8** — but S8's links inherit S4's popover delegation for free). The officer-BLUF layer —
**BANNED project-wide** (S1 §2.2 + R6; audit COH-01): no such artifact is designed, mocked, or
rendered here. Flashcard deck rebuild (**deferred run #2**; S4 preserves stems/aliases — COH-05c,
see R12). Maintenance-loop ingest cadence (**GH#2**).

## 3. Requirements (each testable)

**R1 — TOC-tree explorer, as decided on the mockup (audit CODE-03; user decision, interview round 1).**
Top-level categories are the only accordion: the **whole header row (title + chevron) toggles**; the
authored category overview is an *italic `Overview` first-child row* inside the opened branch, wired
into the connector geometry. Nested folders render as **always-open branches whose header IS the link
to their overview** (S3 model, unchanged). `├─/└─` connectors at every branch level; ticks aligned
with row centers (0.95rem — CODE-06). No smooth-scroll on nav (instant `scrollIntoView`, `block:
"nearest"`). *Check:* on a page ≥2 levels deep, the ancestor category shows open + emphasized; its
`Overview` row navigates to the category overview; no sub-branch has a toggle affordance. `MANUAL` on
the mockup · `AUTO:LINT-S3-overview` (overview reachability presupposes this rendering).

**R2 — One scroll container, working save/restore (supersedes the S3 R11 mechanism description).**
Empirical finding (live, this thread): stock Quartz gives the inner `ul.overflow` `max-height:100%;
overflow-y:auto`, and `div:has(> .overflow)` forces `.explorer-content` hidden — so the S3
prototype's save/restore against `.explorer-content` **read scrollTop 0 forever**. S4 makes
`.explorer-content` the single true scroll container at every breakpoint (`overflow-y:auto` at
specificity ≥0-2-0 + neutralized inner `ul.overflow`), keeps `overscroll-behavior: contain` on it
(and only it — the wheel-trap override on nested ULs is **desktop-scoped**, CODE-02b), gives the
mobile drawer `overflow-y:auto` (CODE-02a), and treats a saved `"0"` as no-saved-position so
scroll-to-active still fires (CODE-07a). **A forward supersession note goes into S3's Amendments**
pointing at this requirement (§0 precedence protocol). *Check:* scroll the expanded tree, navigate,
return — position restored; on a phone-width viewport the below-fold tree is reachable; `.explorer-ul`
never scrolls independently. `MANUAL` (mockup-verified 2026-07-03: content scrolled to 400, UL 0).

**R3 — Weight-reading `sortFn` (implements S3 A8 / TAX-09).** `ContentDetails` (contentIndex emitter)
gains `weight?: number` read from page frontmatter; folder nodes inherit their folder-index's weight
(trie assigns index-file data to the folder node — `fileTrie.ts` `insert`). The explorer `sortFn`
(closure-free, serialized): compare `node.data?.weight` ascending; **missing weight → +∞** (unweighted
sort after weighted, alphabetical among themselves); tie → `localeCompare(displayName, numeric)`;
the stock folders-before-files rule applies **only between two unweighted nodes** (Appendix A
interleaves pages and sub-umbrellas, so weight must be able to express that). *Check:* rendered order
equals authored order at every level on the S3 tree (`AUTO:LINT-S3-order`); a page without `weight:`
lands after its weighted siblings, not first.

**R4 — Did-you-mean case-name search ("moderate" — user decision, interview round 1).** The main
FlexSearch document index is **untouched** (tokenize `forward`; no `suggest` on the main query; no
fuzz in doctrinal ranking). A second, title-only index (`tokenize: "tolerant"`, FlexSearch ≥0.8, all
page titles) drives a **"Did you mean:" chip strip** above results, firing only when: basic search ·
query ≥3 chars · main results <3. Max 3 chips; each chip is a direct link to the page; the whole
layer is try/catch-isolated so suggestion failure can never break search. *Check:* `tery v ohio` →
zero main results + a Terry v. Ohio chip (mockup-verified); `katz` (clean query with ≥3 hits) shows
no strip; deleting the tolerant index at runtime leaves main search functional. `MANUAL` + a smoke
assertion in CI if S9 adds a browser lane.

**R5 — Pill-as-anchor mechanism (audit COH-18 — S4 owns MECHANISM, S5 owns placement).** The
TreatmentBadge status pill and the casetable-injected badges render as
`a.internal.treatment-badge` pointing at the *Verifying Good Law* page via **one exported constant**
(`caseHelpers.ts`); pill styling survives the anchor conversion (status classes outspecify
`a.internal` defaults, verified). **Popover attachment moves to event delegation**: one document-level
`mouseover` handler resolving `target.closest("a.internal")` (keeping the `activeAnchor` re-fire
guard), so server-rendered pills, table-injected badges, did-you-mean chips, and any future injected
anchor get popovers without registration-order coupling. *Check:* hovering a table badge on a
doctrine page fires the same popover as the page-header pill; a link-resolve lint fails the build if
the constant's target slug stops existing (S3 re-homes the page at execution — one-edit constant).
`AUTO:LINT-S4-goodlaw-target` (new, fail-closed).

**R6 — Provenance hover template ("standard" — user decision, interview round 1).** Tooltip (title
attr) = `Treatment: <label> · checked as of <date> · <one-line note> · Click: how we verify good
law`; popover previews the methodology page. When S2's projection lands dual dates, the template
reads `treatment.content_verified` + `treatment.checked` (names per S2 schema) and degrades
gracefully to today's single `as_of`. **Dates stay in the data model + behind the hover + on the
About page — never inline in prose** (PRACTICES §7 placement decision). No bespoke hover-card
component. *Check:* a case with only `as_of` and a case with dual dates both render sensible
tooltips; no page body text contains a generated as-of sentence.

**R7 — About page + footer (user decision: full "About this reference").** `content/about.md` — a
normal, lintable, S9-verifiable content page carrying: what the site is · how cases are verified
(short methodology, linking *Verifying Good Law*) · the how-current-is-this dual-dates explanation ·
attribution (**"Created with Quartz v4.5.2 (MIT)"** moved here from the footer; CourtListener/Free
Law Project) · not-legal-advice. Excluded from the explorer (`filterFn`), linked from the footer,
which becomes `© <year>` + `About this site` (stock Quartz GitHub/Discord links dropped).
`LICENSE.txt` retained (MIT obligation). The mockup draft is the working copy; final prose is
S7-voice-conformant and passes S9 like any page. *Check:* footer contains no "Created with Quartz";
`/about` renders; explorer does not list it; LICENSE.txt present.

**R8 — Publish reconcile: `content/`-canonical, Vercel-only (user decision, interview round 2;
audit COH-16b).** Production stays **push `main` → Vercel** (`vercel.json`: `npx quartz build` →
`public/`). At EXECUTE, **in the same step as the release-gate deploy and sequenced after it**:
(a) `launchctl bootout gui/$UID` + delete `~/Library/LaunchAgents/com.cssi.quartz.plist`; (b) delete
`serve-public.py`, `redeploy.sh`, and the `logs/` they wrote; (c) rewrite `~/.claude/commands/
cssi-ingest.md`: capture **stays** in the vault `_inbox/` (phone flow unchanged), verified pages
write **directly to `content/`**, publish step = commit + push `main`; the vault's wiki pages become
a **frozen archive** — no sync in either direction, ever; (d) document `npx quartz build --serve` as
the only local preview. The G8 publish pause still gates the final deploy itself (§0 register).
*Check:* after EXECUTE, port 8787 serves nothing; no script in the repo copies vault↔content; the
ingest command file contains no vault-page write path; a fresh `git grep -i "vault"` in active
scripts returns only historical docs.

**R9 — Freeze-and-own the fork (user decision, interview round 2).** `quartz/` is **owned code**: no
routine upstream merges (upstream is on Quartz 5; our explorer/search/badge/casetable patches make
merges expensive and risky); the `upstream` remote is kept for reference; fixes are cherry-picked
case-by-case with a Decision-Log note; re-evaluate only at the maintenance loop (GH#2). *Check:* this
requirement in the repo docs (`README`/`docs/`) so a future thread doesn't "helpfully" merge v5;
no `git merge upstream/*` commits after 2026-07-03.

**R10 — Explorer hygiene fixes (audit CODE-04/05/07b/07c).** (a) The stock `folder-button` toggle
wiring is rewritten for the R1 model — buttons exist only at depth 0, no dead subtree guard
(CODE-04 resolved by construction). (b) `quartz.layout.ts` header comment describes the current
model + A8 ordering (CODE-05 — done in mockup). (c) `folderIsPrefixOfCurrentSlug` compares
**prefix-with-separator** (`simpleFolderPath + "/"` or equality) so folder `searches` never
auto-opens for `searches-incident/...` — load-bearing under A8's unnumbered slugs (CODE-07b).
(d) The `!mobileExplorer` `return`-in-loop becomes `continue` (CODE-07c). *Check:* code review
against the mockup diff + a slug-collision fixture for (c).

**R11 — Sidebar & content spacing (audit CODE-08).** As mocked: two-line wrap with hanging indent +
`overflow-wrap: anywhere` on tree rows; left-sidebar right-padding 1.2rem; content-area list
breathing room (`article li + li` 0.3rem, nested lists 0.3rem top). Final values are the mockup's;
S5 may refine *inside entry models* only. *Check:* visual pass on the mockup; no horizontal
scrollbar in the sidebar at 380px.

**R12 — Flashcard-deck safety (audit COH-05c).** S4 changes **no page slug, stem, or alias** — its
only content addition is `about.md` (not deck-referenced). The retirement of `:8787` does not touch
`quartz/static/flashcards/` (served by Vercel identically). *Check:* diff of S4's execution touches
no file under `content/` except `about.md`; the deck's referenced stems resolve post-S4 (deferred
run #2's precondition intact).

## 4. Lessons enforced
**Publish drift** (live site rebuilt from a stale vault) → R8 kills the sync instead of patching it.
**Silent mechanism misdiagnosis** (S3's scroll retarget read 0 forever; nobody noticed because
scroll-to-active masked it) → R2 fixes it *and* records the supersession; R5 removes the same class
of implicit-order coupling from popovers. **URL churn** (TAX-09) → R3's weight sort. **Unreachable
overviews under collapse-mode** (CODE-03) → R1's user-decided model. **Pills-as-spans-lack-popovers**
(O1 finding) → R5. **"Everything must look perfect"** → R11's named values, not vibes. Officer-BLUF
stays banned (S1 R6) — this spec renders *verified* signals only.

## 5. Method (execution — wave 1, concurrent with the S2 lake build)
1. Explorer: apply the mockup commits (`8655398`, `37d6f4f`, `bd50770`) as the working standard;
   add R10c/R10d; implement R3 (ContentDetails.weight + sortFn swap, replacing the numeric-prefix
   interim). The S3 restructure (wave 2) then pours into a working nav.
2. Search: mockup's tolerant index + chip strip (R4) — already the decided form.
3. Signaling: casetable badge → anchor via the shared constant; popover delegation refactor (R5);
   tooltip template incl. dual-date fields (R6); `LINT-S4-goodlaw-target` in `scripts/lint/`.
4. About/footer: finalize `about.md` prose (S7 voice), footer per R7.
5. Publish: R8's retirement sequence at the release-gate step (last), with the §0 G8 pause.
6. Posture: R9 note into `docs/`; S3 Amendments get the R2 supersession pointer.

## 6. Deliverables
The productionized explorer (R1/R2/R3/R10/R11) · did-you-mean search (R4) · pill/popover mechanism +
lint (R5/R6) · `content/about.md` + footer (R7) · the retirement of `redeploy.sh`/`serve-public.py`/
`com.cssi.quartz` + the re-pointed `/cssi-ingest` (R8) · the fork-posture doc note (R9) · S3
Amendments supersession note (R2) · mockup commits `37d6f4f`/`bd50770` (normative reference).

## 7. Acceptance criteria
- [ ] R1 nav model live: whole-header toggle, Overview first-child row, link-header sub-branches, aligned connectors.
- [ ] R2 single scroll container; save/restore round-trips; mobile drawer scrolls; S3 supersession note filed.
- [ ] R3 rendered order == authored order on the S3 tree; unweighted-after-weighted fallback holds.
- [ ] R4 `tery v ohio` rescued; clean queries unaffected; suggestion layer failure-isolated.
- [ ] R5 every treatment badge (page + table) is an `a.internal` with a working popover; target lint green.
- [ ] R6 tooltip renders single- and dual-date frontmatter; no inline as-of prose anywhere.
- [ ] R7 About carries attribution + methodology + currency; footer minimal; LICENSE.txt intact.
- [ ] R8 post-EXECUTE: no vault sync path exists; :8787 dead; ingest writes to content/; Vercel is the only publish.
- [ ] R9 posture documented; no upstream merge.
- [ ] R10/R11 hygiene + spacing fixes in; slug-collision fixture passes.
- [ ] R12 no stem/alias changes; deck references resolve.

## 8. Verification plan
S4's own gates: the mockup IS the visual acceptance (user-signed, 2026-07-03); `LINT-S4-goodlaw-
target` + `LINT-S3-order` + the existing build gate run fail-closed in CI. **S9** re-verifies: the
R8 retirement checklist post-EXECUTE; R5 popover behavior on a sampled doctrine page + case page;
R6 template against S2's projected frontmatter; the R2 scroll round-trip. The About page passes the
standard content gates (G1–G10 where applicable) like any page.

## 9. Open items / escalations
- **Dual-date field names** (R6) bind to S2's projection schema at execution; if S2's names differ
  from `treatment.checked`/`content_verified`, the template adopts S2's names (S2 is the SSOT).
- **Search-index size**: the tolerant title index adds ~500 short entries client-side — negligible
  now; if S6's frontier stubs triple the corpus, revisit `limit` and chip count only.
- **`cases/` Overview row**: until S3 unlists `cases/`, its auto-generated folder node also gets an
  Overview row — harmless, disappears with S3's unlisting.
- **Did-you-mean threshold** (<3) is a constant; S8's linking pass may surface a better trigger —
  tune without re-interview (behavior class is locked, not the constant).

## 10. Decision log
**User decisions (interview, 2026-07-03).** D1 nav headers: whole-header toggle + Overview
first-child row (CODE-03; over the recommended title-link/chevron split — pivoted live on the
mockup, commit `bd50770`). D2 did-you-mean: moderate (chips on weak results). D3 About: full
"About this reference". D4 hover: standard (status + dates + note + methodology popover). D5
publish: content/-canonical, **Vercel-only — retire :8787/launchd/serve-public.py too**. D6 fork:
freeze-and-own 4.5.2.

**Self-interview (SD1–SD10, condensed; full text in the thread).** SD1 weight data via
`ContentDetails.weight` extension (vs. layout-table copy = drift, vs. new emitter = artifact);
folders-first only among unweighted. SD2 popover **event delegation** (vs. exported-attach coupling,
vs. implicit listener order = silent breakage). SD3 tolerant index over ALL titles; <3-hit trigger;
try/catch isolation; main index untouched. SD4 good-law target = one exported constant + fail-closed
lint. SD5 retirement sequenced after the release-gate deploy so the Tailscale bookmark never dies
early. SD7 About as a normal content page (lintable/verifiable), not an emitter. SD8 the R2 scroll
finding supersedes S3 R11's mechanism text via a forward note, never a silent rewrite. SD9 CODE-07
residuals: separator-safe prefix match + `continue`. SD10 tooltip template reads dual dates,
degrades to `as_of`; placement stays S5's.

**Audit-row dispositions (injected:S4 — AUDIT-CLOSURE gate).**
- **CODE-02a** ADOPTED — mobile drawer `overflow-y:auto` (mockup `37d6f4f`; R2).
- **CODE-02b** ADOPTED — wheel-trap override desktop-scoped (mockup `37d6f4f`; R2).
- **CODE-03** ADOPTED-ADAPTED — user chose the Overview-row variant over chevron-split (D1; R1).
- **CODE-04** ADOPTED — dead guard gone with the button-wiring rewrite (mockup + R10a).
- **CODE-05** ADOPTED — layout header comment refreshed (mockup `37d6f4f`; R10b).
- **CODE-06** ADOPTED — ticks at 0.95rem row centers (mockup `37d6f4f`; R1).
- **CODE-07** ADOPTED (3 parts) — saved-"0" fixed in mockup; prefix false-positive → R10c;
  return-vs-continue → R10d. Quirk notes carried here.
- **CODE-08** ADOPTED — wrap/padding/list-spacing named + mocked (R11).
- **COH-05c** ADOPTED — no stem/alias changes; deck safety is R12.
- **COH-16b** ADOPTED — pipeline ownership + D5 retirement lands as R8.
- **COH-18** ADOPTED — mechanism (R5/R6) vs. placement (S5) boundary held throughout.
- **TAX-09/A8** ADOPTED — weight-reading sortFn + content-index extension (R3); numeric-prefix
  interim superseded.
