# CSSI Overhaul 2 — RUNBOOK

*The master plan for the second CSSI overhaul, framed as a professional legal-reference **production
line** (Spine → Surfaces → Content → Assurance). This is the artifact a fresh context thread is
pointed at: "run S3" → the thread reads §0–§2 + `PRACTICES.md` + its spec entry in §4, researches
**continuously** (up front *and* live mid-interview), conducts the interview **show-don't-tell**
(open-ended + choices, browser mockups / written examples it **revises and pivots on** as answers
land), runs a **self-interview** over the self-owned design decisions, and only then writes the spec to
`_overhaul2/specs/SN-<slug>.spec.md`.*

Status: **see §7 — the single status authority** (this header no longer carries status; it went stale
once — audit COH-03). Content is untouched except user-approved hotfixes logged in the §0 human-pause
register. Last updated: 2026-07-02.

Companion docs (read alongside this): **`PRACTICES.md`** (the editorial/verification playbook every
spec inherits) · **`CL-DATA-INVENTORY.md`** (exactly what CourtListener gives us — the S2 schema seed).

---

## 0. How to use this runbook
- **One thread = one spec.** Point a new thread at a spec by number. It reads §0–§2 + `PRACTICES.md`
  (+ `CL-DATA-INVENTORY.md` for S2/S6/S9) + that spec's §4 entry, then runs the §1 lifecycle.
- **This phase decides three things only** (per the user): each spec's **direction**, the **execution
  order**, and **what each interview must extract**. Deep per-spec research + design happen in-thread.
- **Nothing is pre-decided.** Draft proposals (the taxonomy tree, the reconsidered-plan brief) are
  *inputs to refine*, never decisions to ratify. Specs are written only after interview + mockups sign-off.
- **The north star:** the definitive, 100%-verified edition — every case verified, every proposition
  traceable, framed properly, treatment-annotated, expansively searched. This is treatise/Restatement
  production, not wiki maintenance.
- **PRECEDENCE STACK (audit COH-08):** **approved specs > RUNBOOK > PRACTICES > wrappers.** On any
  conflict the higher-precedence text wins; the conflict MUST be resolved by adding a **forward
  supersession note** in the lower-precedence doc pointing at the winning text — never by silently
  rewriting or by letting both versions stand. Completed wrappers are superseded by their signed spec
  the day it lands (banner on each wrapper).
- **HUMAN-PAUSE REGISTER (audit COH-06 — scopes guardrail G8).** G8's "human sign-off for anything
  reader-facing" is scoped to these **enumerated pauses** inside the one autonomous run; nothing else
  stops the line:
  1. the **publish go-ahead** (final);
  2. **fabrication removals** (S6);
  3. **borderline-relevance sign-off** (S6);
  4. **content hotfixes during planning**;
  5. officer-summary approvals — **moot**: S1 banned the artifact project-wide (S1 §2.2/R6);
  6. the **release gate** (S9);
  7. the **volume/scope-guard pauses the specs define** (added at the coherence pass 2026-07-04 —
     they existed in signed spec text but were missing from this enumeration): S6 §9 (frontier
     yield >150 pages) · S7 §9 (>10 tier promotions) · S9 R7 (>10 new pages from completeness
     instruments) · S9 R7.5 (the sampled-frontier **tripwire** firing the full 13-category
     re-run — pause + surface evidence and revised wall-clock before proceeding);
  8. the **agent/lane-outage pause** (user decision 2026-07-04): if an agent lane breaks —
     realistically Codex — the run first attempts self-resolution (retry/backoff, fresh
     session, config/timeout fixes); if unresolved, **Codex-required workflows HALT and the
     issue elevates to the user** (interactive re-auth is always a user fix — headless cannot
     re-auth). **Never substitute a Claude lane to keep a Codex-required workflow moving** —
     the lake build, the 2 panel lanes, case-grain Thread-N reads, and dual-model discovery
     lose their writer≠checker / model-diversity guarantees without Codex. Independent
     non-Codex work may continue, checkpointed, only where it neither consumes nor
     substitutes for the halted lanes' outputs.
  *Entries:* **2026-07-02** content hotfix (Chatrie + Third-Party) — user-approved. **2026-07-03**
  deploy decision: hotfix commit `be02044` ships with the full-bundle deploy after EXECUTE — no
  interim push to main (user-decided; the pre-deploy live site knowingly retains the pre-fix pages).
- **Wrapper template notes (audit COH-25).** Future wrappers (S4+) copy `wrappers/S3.wrapper.md` and
  MUST carry two lifecycle steps: **(a)** the **REQUIRED visible self-interview** before writing (§1
  step 5); **(b)** an audit-intake step: "Read `_overhaul2/AUDIT-2026-07-02.md`, filter to your spec's
  rows, and address each — adopt / adapt / reject-with-rationale — in the spec's Decision Log."

## 1. Per-spec thread lifecycle
*Research and mockups are **continuous and interactive**, not one-shot phases. The loop is iterative:
keep researching and re-showing as the interview surfaces questions, and **be willing to pivot what
you're building** mid-stream. Nothing is locked until sign-off.*
1. **Research — up front AND throughout (web + CourtListener).** Internal (codebase/corpus + Overhaul-1
   findings) **and** external. **Use CourtListener AND web search together** — CL has coverage gaps, and
   web search surfaces terminology / legal theories / adjacent keywords that reframe and properly expand
   the search (`PRACTICES.md` §4). Assume nothing; web discovers, primary source confirms. **Don't stop
   at the up-front pass:** research **live mid-interview** the moment an answer opens a question, **verify
   feasibility/tooling for real** (prove it works — don't assume), and feed findings straight back in.
2. **Show, don't tell — and keep iterating it live.** Visual change → browser mockup on a branch (dev
   server `npx quartz build --serve` :8080), modifying only what's discussed; perfect it there, spec
   follows to the letter. Content change → a **written example** first (one overview, one rewritten
   brief). **When an interview answer changes the direction, change the mockup/example on the spot and
   re-show it** — pivot freely while defining what we're building. **The officer-bottom-line / BLUF /
   field-application summary is BANNED project-wide (S1 §2.2 + R6 Variant A — audit COH-01): do not
   design, mock, or generate it.** Its paraphrase-drift scar (the O1 trap) survives as S1 R7 — never
   auto-generate a controlling standard; the reader gets the verified rule + brief and applies it.
3. **Interview.** Options + context + open-ended opener; ask only user-owned decisions (recommendation-
   first, `AskUserQuestion`); self-resolve the rest and log it. **Always close open-ended** and
   interview on the answer. Research + mockup changes happen *inside* this loop, interactively. Don't
   over-produce; long material → briefs.
4. **Follow-up research** to close every surfaced question with authority (the tail of the continuous
   research above — not the only research after step 1).
5. **Self-interview — REQUIRED, visible, before writing.** After the user's decisions, run an explicit
   self-interview over the **self-owned** design decisions you'd otherwise bake in silently (schema,
   paths, edge cases, spec boundaries, mechanics): pose each as a question, argue the alternatives, pick
   with rationale, and state the failure mode it guards against. Go **adversarially deep on the 1–2
   decisions that shape everything downstream** — work the problems, edge cases, and solutions out loud.
   This is the Overhaul-1 practice; **do not jump from decisions straight to prose.** It becomes the
   spec's Decision Log.
6. **Write the spec** (Overhaul-1 template: Objective · Scope · Requirements w/ `*Check:*` · Lessons ·
   Method · Deliverables · Acceptance · Verification · Open items · Decision log). Update §7 status.

**Disciplines (from `PRACTICES.md`):** taxonomy-as-spine + single-source-of-truth · rule-vs-support
graded authority · per-assertion verification, writer ≠ checker, fail-closed · visible currency ·
three-field treatment vocabulary · saturation stopping rules · AI guardrails G1–G10. Execution is one
autonomous run at the end (data-lake built first).

## 2. Findings & lessons (why O2 exists)
**Keep (Overhaul 1 worked):** lessons-register-as-constitution; thin-orchestrator + on-disk handoffs;
find→adjudicate→fix + loop-cap-3; coherence pass as a gate; deterministic FREE front-loading; LINT-1…8
+ build gate; D5 coherence + D8 mermaid; **BIRAC case format (liked — keep it).**

**Fix (each → a spec):**
- **Slip-op labels wrong** on ~43 of 47 files (only current-term legit) → S7/S2/S9.
- **CL is not a good-law oracle** — it has **no treatment signals at all** (`CL-DATA-INVENTORY.md`);
  Chatrie/Zorn had corrupted objects; the biggest Overhaul-1 catch came from an out-of-band human
  pass → S2 (derive treatment from progeny text + web) + S9 (cross-model + forced primary reads).
- **The mandated N-of-3 review collapsed to N-of-1**, blind re-derivation skipped, quotes/pinpoints
  under-verified, no machine ledger → S9.
- **Named-but-no-page cases** — ~70–80 (mostly circuit) named in prose with no page; some flagged
  fabrication-risk → S6 (verify → author or remove). **External links otherwise complete** (2 English
  cases excepted).
- **Table headers non-standardized**; treatment/weight rendered inconsistently → S5.
- **Explorer UI** jank (scroll target, padding, wrap), cramped lists, pills-as-spans-lack-popovers →
  S4/S5. **Publish drift** (live site rebuilt from the stale vault, not canonical `content/`) → S4.
- **Officer-summary paraphrase drift** on the controlling standard (emergency aid = *objectively
  reasonable belief*, not "imminent danger") → **resolved by S1's project-wide BAN on the officer-
  BLUF/field-application layer (S1 §2.2 + R6 — audit COH-01); no spec builds one.** The scar rule
  (never auto-generate a standard) survives as S1 R7.
- **`^pin-N` carat leak** — Obsidian block-ref anchors rendering as visible text; "everything must
  look perfect" → S9 + a CI lint.
- **Content structure**: apply-it prose not numbered lists; leaked "(woven in)" meta; "persuasive,
  not binding"; tests/prongs not up front; SCOTUS in "Recent developments" → S1 rules + S7.

**Feasibility (2026-07-01):** headless `codex exec` works (stdin `/dev/null` + timeout wrapper).
**S2 build path (decided 2026-07-01): Codex builds the data-lake** via a direct CL **REST API v4**
ingest script (token read from `~/.config/cssi/cl-token`, ~1,000 req/hr → paced + disk-cached +
resumable). This sidesteps the expired Codex CL-MCP OAuth (no MCP needed) and conserves Claude usage.
**Codex = builder + reviewer; Claude orchestrates/designs + takes 1 of the 3 review lanes.** The
Claude CL MCP stays only for interactive spot-checks. **L4 is rescoped by S1 amendment (audit
COH-07): one serial CL lane *per credential* — the Codex REST builder owns the token; the Claude MCP
lane is interactive spot-checks only. The two consumers may run concurrently.**
Live sites 200; popovers on; FlexSearch in place; MIT needs only `LICENSE.txt` retained.

## 3. The bundle & execution plan
**Nine specs**, production-line waves. Maintenance loop **deferred** →
<https://github.com/Enragedsaturday/cssi/issues/2> (the FORK's issue #2 — a bare `gh` default resolves
to upstream quartz; audit COH-23). Nesting max 3 levels (index-1 umbrella w/ overview → index-2
doctrine/sub-umbrella → index-3 doctrine).

| # | Spec | Build order | Depends on | Exec wave |
|---|------|-------------|-----------|-----------|
| **S1** | Standards & Style Manual | 1 | — | 0 (rulebook) |
| **S2** | Verified Authority Database (CourtListener source-of-truth) | 2 | S1 | 1 (built first) |
| **S3** | Taxonomy & Points-of-Law (categories, nesting, nav structure) | 3 | S1,S2 | 2 (restructure) |
| **S4** | Platform, Nav & Reader-Signaling UI | 4 | S1 | 1 (nav working-standard, before restructure) |
| **S5** | Entry Models (case + doctrine pages) | 5 | S1,S2,S3,S4 | 2 |
| **S6** | Coverage & Ingest (verify + author missing cases) | 6 | S2,S3,S5 | 3 |
| **S7** | Doctrine Production (brief-first rewrite) | 7 | S1,S2,S3,S5,S6 | 3 |
| **S8** | Legal-Term & Case Linking + Glossary | 8 | S2,S4,S6,S7 | 3 |
| **S9** | Verification Pipeline & Release Gate (1 Claude + 2 Codex) | 9 | all | 4 |

*"Depends on" = **AUTHORING dependencies** — what must be signed before that spec is written; "Exec
wave" orders **execution** (audit COH-04). The two deliberately differ, and a spec header's `gates:`
list expresses authoring order only — it does NOT serialize execution: the S2 lake build and the S4
nav standard run concurrently in wave 1. Corrections baked in: S3 depends on S2 (the `point → node`
binding map consumes S2's point-override slugs); S5 depends on S4 (pill/hover mechanism — COH-18);
S8 depends on S2 (canonical names + frontier-stub linking), S6 (the pages it links), S7 (final text).*

**Execution order (one autonomous run):** S1 rulebook → **S2 database built (source of truth) + S4
nav working-standard + publish→content-canonical** → **S3 category restructure poured into the working
nav + S5 entry models** → **S6 ingest → S7 doctrine → S8 linking** → **S9 verify + release**. Build
order ≠ execution order deliberately (design the spine early; at execution the nav works before the
restructure lands).

## 4. Spec entries
Each: **Direction · Research first · Interview-extract (choices + what to show/mock) · Deliverable.**

### S1 — Standards & Style Manual
- **Direction.** The constitution + `STYLE.md`. Fold in Overhaul-1's self-critique and the new rules;
  adopt from `PRACTICES.md`: the graded-authority entry model, the 10-gate verification protocol, the
  three-field treatment vocabulary, the AI guardrails G1–G10, the reader-facing signaling scheme, the
  term register + SSOT transclusion rule, the 6-tier authority lexicon ("persuasive outside circuit"),
  slip-op-current-term-only, numbered apply-it lists, no meta-labels, SCOTUS-never-in-Recent-Dev,
  mnemonic policy (3 Golden Rules, C.R.E.W. "RE", strive-for-five, N.E.R.D.S., + other verified Bandiero sayings; "CRON" was a dictation error, dropped), and the **Humanizer** subset
  fit for a legal register. Each rule → Trigger/Check/Enforcement (testable by S9 + lints).
- **Research first.** Re-read `docs/STANDARDS.md`, `docs/FINAL-QA-SPEC.md`; fetch + evaluate the
  Humanizer skill; verify mnemonics verbatim (incl. CRON's Bandiero expansion).
- **Interview-extract.** Humanizer subset that applies vs. can't; voice heaviness; exact lexicon
  wording; **the graded-authority depth** — *mock up ALI-full vs. lighter "rule + notes" and choose.*
  *Show:* before/after voice paragraph; the two graded-authority variants.
- **Deliverable.** `S1-standards.spec.md` (+ `docs/STANDARDS.md` + `STYLE.md` at execution).
  ✅ **Written 2026-07-01** (audit COH-24). Decided highlights: graded authority = **Variant A**
  (rule/explanation/authorities); the **field-application / officer-BLUF summary is banned
  project-wide** (§2.2 + R6); 3-field treatment vocabulary; em-dash prose policy w/ citation-range
  carve-out; verified mnemonic register (CREW "RE", CRON dropped). The spec text wins over this entry
  (§0 precedence).

### S2 — Verified Authority Database (the spine)
- **Direction.** The West-Key-Number-style source of truth: one record per case built from
  `CL-DATA-INVENTORY.md` — verified identity (cluster→lead opinion), reporter cites + pinpoints,
  court/date/disposition, the **three-field treatment vocabulary + dual as-of dates** (derived from
  progeny text + web, since CL has no treatment signal), the **progeny/citing-references map**
  (`cites:(<all sibling ids>)`) for the expansion/narrowing picture, off-CL authoritative links
  (Justia/Scholar) for coverage gaps, and a **provenance/audit trail** per field. On connected storage,
  resumable. Absorbs the Chatrie/Zorn corrupted-object tickets. Every page + S9 read from it.
- **Research first.** `CL-DATA-INVENTORY.md`; confirm the build path (direct CL REST API token vs.
  Claude CL MCP — Codex MCP is optional and currently broken); the comprehensive-research protocol
  (`PRACTICES.md` §4); storage location/format on the pool.
- **Interview-extract.** The record schema; storage paths; build path (REST vs MCP); refresh cadence;
  off-CL vetting rule; the "not found ≠ fabricated" + name-vs-canonical fabrication check. *Show:* one
  fully populated example record (JSON) for a representative case incl. its progeny map.
- **Deliverable.** `S2-authority-database.spec.md`. ✅ **Written 2026-07-01.** Decided: **three coordinated
  stores** — flat per-case JSON = committed source of truth (`_overhaul2/lake/`), **derived SQLite**
  query layer (citation graph/coverage/verification) + raw cache out-of-repo (`/Volumes/AIStore2`),
  frontmatter = **generated projection** (lake is SSOT, two-directional drift lint). Scope = 457 now +
  frontier identity stubs (authoring→S6, linking→S8). Treatment = 3-field + dual dates + **composite
  (principal-holding) + `varies_by_point` + point-overrides**, derived over **three lanes** (negative-
  keyword + top-cited + **recency**). Builder = Codex, Python stdlib, direct REST v4, paced+cached+
  resumable. Live-confirmed the build path + the name-rank identity trap (Adams/Williams, Miranda).
  **Wall-clock (audit COH-19):** the lake build is **~15–25k CL calls at ≤~14 req/min ≈ 20–30+ h
  minimum — a multi-day paced run**, not an afternoon step; the R10 journal records lane completion
  so a resume never re-burns treatment-query quota. Schedule it as the wave-1 background lane.

### S3 — Taxonomy & Points-of-Law
- **Direction.** Our own category tree (3-level nesting; umbrella w/ authored **overview page** →
  doctrine/sub-umbrella → doctrine), self-explanatory, each node self-contained, more granular where
  it earns it. Exigency → flavors; relocate Plain View to a seizure cluster; promote
  Checkpoints/Inventory/Border out of the Special-Needs mega-page; rename "Levels of Suspicion" →
  "Standards of Proof" (full burden pyramid, **PC < preponderance**); re-homing rules (Brendlin, Katz,
  Graham); unlist `cases/`; the possible "Home Entry & Search" topic. Do NOT plagiarize the book.
  The taxonomy is also the **controlled classification** every proposition hangs off (spine) — S3
  therefore also owns the **point-of-law node scheme + the `point → S3 node` binding map** that
  resolves S2's provisional treatment-override slugs; a runbook-only thread must not under-scope this
  (audit COH-13b; delivered — see below).
- **Research first.** Current tree + Bandiero TOC + LaFave TOC (`.orca/drops/SSTOC.pdf`) + NJ Handbook
  (`.orca/drops/New Jersey Law Enforcement Handbook…pdf`) + Wex/casebook order + the draft tree
  (`~/briefs/2026-07-01-cssi-o2-taxonomy-proposal.html`, an input only).
- **Interview-extract.** Umbrella set + names; exceptions axis (suspicion-tier vs object vs flat);
  "Home Entry & Search" y/n; "Standards of Proof" rename; nav size; Knock-and-Talk placement; which
  nodes are index-2 umbrellas vs index-3 leaves; per-case re-homings. *Show:* a **live nav mockup** on
  a branch + a written overview page — lock the layout on the mockup before writing.
- **Deliverable.** `S3-taxonomy.spec.md`. ✅ **Written 2026-07-02.** Built our own tree from scratch on
  **NJLEH's object-led methodology**, breadth-checked vs LaFave + Bandiero, perfected on a live Tailscale
  mockup. **13 categories** (Appendix A): parallel **Searches/Seizures**, **Standards of Proof** moved to
  #2, **Warrant Exceptions** by object, **Home Entry & Search** premises bucket, new **Fair-Trial &
  Reliability** umbrella (Eyewitness ID + Brady/Giglio + Entrapment), **§1983 / Qualified Immunity** split,
  Plain View at the threshold, names de-ripped from Bandiero. Two layers: the tree + the **point-of-law
  registry** (`_overhaul2/points/registry.yaml`) with the fail-closed **`point → node` binding map** that
  closes S2 §9 (Belton→Gant = `search.vehicle.sia-recent-occupant`). The **"TOC-tree" nav model + sidebar
  scroll fix + connectors** were prototyped here but are **handed to S4**. Six new lints.

### S4 — Platform, Nav & Reader-Signaling UI
- **Direction.** Make the explorer *work* (retarget scroll save/restore to `.explorer-content`; drop
  smooth-scroll-on-nav; fix sidebar padding, two-line wrap; roomier rows; list/paragraph spacing in
  `custom.scss`). Move "Created with Quartz" → a single About page. Reconcile the **publish pipeline to
  `content/`-canonical** (retire the vault sync) so the live site is trustworthy. **Search:** FlexSearch
  fuzzy + case-name "did-you-mean." **Reader signaling** (from `PRACTICES.md` §7): verification badges,
  **dates in the data model + behind a hover + on the About page (NOT inline everywhere)**, treatment
  flags, overruled-as-history rendering, pills-as-anchors (so popovers work). Includes the honest
  keep-Quartz-vs-fork evaluation. This is a *working standard*, executed **before** the S3 restructure.
  **Pipeline ownership (audit COH-16): S4 owns reconciling the `/cssi-ingest` vault-inbox skill to
  `content/`-canonical** (the live skill still writes to the vault — retire or re-point it with the
  vault sync); its post-launch future belongs to the maintenance loop (deferred run #1, §4 footer).
  **S4/S5 boundary (audit COH-18): S4 owns the pill/anchor/hover MECHANISM** (components, popover
  wiring, `a.internal` anchors); **S5 owns pill PLACEMENT/format** inside the entry models.
- **Research first.** The technical audit (files located); FlexSearch `suggest`/tuning; OSS nested-nav
  options; the launchd/`redeploy.sh` publish path.
- **Interview-extract.** Fix stock explorer vs. OSS nested-nav (mock both); fuzzy aggressiveness;
  About-page content + attribution; how much provenance shows on hover. *Show:* side-by-side explorer
  mockups + a search-suggestions demo + a treatment-badge/hover mock on the dev server.
- **Deliverable.** `S4-platform-ui.spec.md`. ✅ **Written 2026-07-03** (mockup commits `37d6f4f` +
  `bd50770`; all injected:S4 audit rows dispositioned in the Decision Log). Decided highlights:
  nav = whole-header category toggle + **Overview first-child row** (CODE-03, user D1); did-you-mean
  = moderate (tolerant title index, chips on <3 hits); About = full "About this reference"; hover =
  status + dates + note; **publish = content/-canonical, Vercel-ONLY — :8787/launchd/serve-public.py
  + redeploy.sh retired at EXECUTE, `/cssi-ingest` re-pointed (vault = capture-only inbox)** (D5);
  fork posture = **freeze-and-own Quartz 4.5.2** (upstream is on v5; no routine merges) (D6).
  Live finding: the S3 prototype's scroll save/restore read a non-scrolling node (stock scroller is
  `ul.overflow`) — corrected as S4 R2 + S3 Amendments A9 forward note. The spec text wins over this
  entry (§0 precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **CODE-02a** mobile drawer needs `overflow-y:auto` (below-fold tree unreachable on phones) ·
  **CODE-02b** media-scope the wheel-trap `overscroll-behavior` override to desktop ·
  **CODE-03** top-level overviews unreachable in collapse-mode nav — chevron-toggle/title-link or a
  depth-0 overview row (S3 seam) · **CODE-04** delete/annotate the dead `button.closest("li.subtree")`
  guard · **CODE-05** update the stale `quartz.layout.ts` header comment (old 12-category scheme) ·
  **CODE-06** align the connector-tick `::after` with row centers · **CODE-07** stock quirks to note
  (saved `"0"` scrollTop suppresses scroll-to-active; `folderIsPrefixOfCurrentSlug` prefix
  false-positives; `!mobileExplorer` return-vs-continue) · **CODE-08** carry this entry's named items
  the diff omits (sidebar padding, two-line wrap, list/paragraph spacing) · **COH-05c** preserve
  flashcard-deck-referenced stems/aliases in nav/platform work (w/ S3) · **COH-16b** the
  publish/ingest pipeline ownership lands in this spec · **COH-18** pill/anchor/hover mechanism is
  S4's (placement = S5) · **TAX-09/A8 (2026-07-03)** the explorer `sortFn` reads frontmatter
  `weight:` (pages) + folder-index `weight:` (categories) — the mockup's numeric-prefix sort
  (commit 8655398) is superseded on this point (S3 § Amendments A8).

### S5 — Entry Models (case + doctrine pages)
- **Direction.** The **graded-authority doctrine page** — **Variant A: black-letter rule / explanation
  / authorities (adjudicated by S1 R6; `PRACTICES.md` §5 superseded on this point)** — and the **BIRAC
  case page** (keep the liked BIRAC). **The officer-bottom-line / "In the field" box is BANNED
  project-wide (S1 §2.2 + R6 — audit COH-01): do not design, mock, or spec it.** Standardized
  case-table schema (short shared headers, controlled widths, no
  side-scroll); treatment **pill under the case name**, **weight in the case column**, treatment column
  + "treated in full" removed, relevance tags under relevance; the pill is an **anchor** to the
  "Verifying Good Law / as-of" page with hover preview; "limited by/expanded by" folds into the holding.
  Draft-state machinery (`draft → under_review → verified`); provenance rendering. **Boundary (audit
  COH-18): S5 owns pill PLACEMENT/format in the entry models; the pill/anchor/hover MECHANISM is S4's.**
- **Research first.** `CaseTable.tsx`/`casetable.inline.ts`/`TreatmentBadge.tsx` (spans → `a.internal`);
  the book case-example PDF (~~missing — regenerate or drop~~ **RESOLVED 2026-07-03: reference
  dropped at the S5 interview, user D12 — audit COH-14**); S2 schema.
- **Interview-extract.** BIRAC section order + voice; ~~ALI-vs-lighter graded-authority~~ — **already
  adjudicated: S1 chose Variant A (S1 R6 + Appendix C — audit COH-12; do not re-mock or re-interview)**;
  final table columns; as-of page + hover; where deep-link/pinpoint highlights
  apply. *Show:* browser mockup of the new table + pill + hover; one written BIRAC page.
- **Deliverable.** `S5-entry-models.spec.md`. ✅ **Written 2026-07-03** (mockup commits `240be19` +
  `8ef8c3d`; all injected:S5 audit rows dispositioned in the Decision Log). Decided highlights:
  table schemas = **3 sanctioned** (Key cases `Case|Holding|Opinion` · Related
  `Case|Relevance here|Primary home|Opinion` · Case Index) with weight + Field-I pill **injected
  under the case name** (content-vs-data authoring boundary — cells never author
  weight/treatment/dates); dates **hover-only everywhere** (TEACH-15: cells count as inline);
  doctrine skeleton = field-decisive question → **`[!rule]` black-letter callout (canonical
  statement site, registry mirrors)** → Brief (closing `**Common pitfalls.**` bullets) →
  **"Lower-court developments" ABOVE the tables** (TEACH-08 rename + move) → Key cases → Related →
  Visual → Sources (**bracketed**); BIRAC kept verbatim; point-status table on split-treatment
  cases; legacy statuses render through the S1 A4 mapping (COH-11); **COH-14 book-PDF reference
  dropped (user D12)**. The spec text wins over this entry (§0 precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **TEACH-13** related-cases table integrity: self-reference ban + controlled header set + one CL
  anchor text · **TEACH-14** one Sources-section format (bracketed-link vs em-dash list) ·
  **TEACH-15** unify the treatment-cell format (527 bare / 342 / 51 / 25 variants; decide whether
  table cells count as "inline" under S1 R3) · **TEACH-08** heading standard for "Recent developments"
  (role-based rename or lookback window; S7 applies) · **TEACH-09** pitfalls format standard (bulleted
  bold-error+cite, per PC/RS) · **TEACH-10** decide grouped Key-cases sub-tables (adopt for >15-case
  pages or drop) · **NUM-07** table-header standardization: **51 distinct "Case" header schemas → 1** ·
  **COH-11** consume the S1/S2 old→new treatment-enum migration mapping before the projector
  overwrites · **COH-18** pill placement/format (mechanism = S4).

### S6 — Coverage & Ingest
- **Direction.** Verify + author the **named-but-no-page** cases (2026-07-01 audit: ~70–80 genuine,
  re-derived **~80–84** by NUM-05, mostly circuit). **Verify existence first (two-key; "not found ≠
  fabricated"; compare input name vs
  CL canonical)** — author a BIRAC page + external link for real ones, **remove** fabrications
  (*Mayville/Small/Lyle/Moore-Bush* were flagged). Diff the corpus against book roster ∪ named-in-prose
  ∪ prior-research ∪ bounded frontier; officer-field-relevance gate. Fix ~6 alias/variant mismatches;
  ignore ~5 citation-format placeholders. (Full seed: **`_overhaul2/S6-SEED.md`** + its generator
  script — regenerated 2026-07-02 per audit COH-02a; the old "§S6 seed / `audit_cases.py`" reference
  was dangling.) **388-bare-mention split (audit COH-15):** of the 388 distinct cases with ≥1 bare
  mention (NUM-04), **S6 owns existence-verification + authoring of only the ~80–84 no-page subset**
  (the S6-SEED roster); **S8 owns linking ALL 388** once pages exist — the two specs reconcile the
  numbers jointly (NUM-04/NUM-05 are the measured inputs).
- **Research first.** The audit list; Overhaul-1 coverage (`_overhaul/coverage/`); the comprehensive-
  research protocol; a why-missed taxonomy.
- **Interview-extract.** Relevance gate threshold; frontier reach; borderline sign-off. *Show:* the
  missed-case list + why-missed→generalized-search on a sample.
- **Deliverable.** `S6-coverage-ingest.spec.md`. ✅ **Written 2026-07-03** (specimen page
  `content/cases/United States v. Smith (2024).md` authored live — two-key verified, roster
  self-closed 89→88; all injected:S6 audit rows dispositioned in the Decision Log). Decided
  highlights: **the O1 "persuasive-only → no page" default is FLIPPED** (user D1 — every
  two-key-real, gate-passing named case earns a page); history cluster authored as history pages
  (D2); **full O1-style frontier inside S6** (D3) with a **stricter frontier floor**
  (controlling-or-split-marker; D5); two batched human-pause packets (D4); *Egbert/Martin/Culley*
  authored — R2 prong (c) widened to the SCOTUS civil-liability boundary (D6); OT2019→present term
  sweep signed (D7; *Noem* watch, *Villarreal* reject). Mechanics: candidate queue through S2's CL
  lane (no S6 credential), one reusable authoring pipeline (S7 invokes it), the COH-15
  reconciliation shipped as `_run/s6-coverage-ledger.json`, the seed scanner promoted to a CI lint
  (proposed LINT-17). The spec text wins over this entry (§0 precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **GAP-01b** author retaliatory-arrest coverage (*Nieves* 2019, *Gonzalez* 2024 — 0 hits today) ·
  **GAP-02b** author 4A malicious-prosecution coverage (*Thompson* 2022, *Chiaverini* 2024) ·
  **GAP-04a** *Cooley* (tribal officers/non-Indians) · **GAP-04b** *Lombardo* (prone restraint) ·
  **GAP-04c** *Culley* (forfeiture retention hearings) · **GAP-04d** reconsider page-less *Egbert* ·
  **GAP-04e** *Noem v. Vasquez Perdomo* (2025 shadow docket — watch item) · **GAP-04f** assess
  *Villarreal* (trial-side; likely reject-with-rationale) · **GAP-04g** reconsider *Martin* (FTCA
  wrong-house raid) alongside Egbert · **GAP-05** add an **OT2019→present term-by-term SCOTUS sweep**
  as a named seed source (never-named doctrine is invisible to the named-in-prose leg; recurring
  version → the maintenance loop) · **COH-15** the 388/~84 split (see Direction) · consume
  **`_overhaul2/S6-SEED.md`** (COH-02a + NUM-05) as the committed roster.

### S7 — Doctrine Production (brief-first)
- **Direction.** Produce/rewrite each doctrine/narrative page *through* the draft→review→verified
  pipeline: brief-first (rule + tests up front + limits + nuance + pitfalls integrated, no "(woven in)"
  label); numbered apply-it lists; nothing after the tables except the diagram; fix slip-op pinpoints,
  pipe-escaping, `^pin-N` leaks; per-page fixes originally captured from `Prompt.md` (**file missing —
  not in the repo anywhere; the parenthetical list here is the surviving record — regenerate or drop
  the reference at the S7 interview; audit COH-14**) (Matlock is a Consent table-entry;
  CREW "R"→"RE"; Herring→Key on Collective Knowledge; Riley→Related on Common Law; community caretaking
  reaches persons; Dunn factors in the Rule; Knock-and-Talk = lawful-presence/implied-license; Bandiero
  hot/fresh-pursuit line; Santana "limited by"; consent 3 prongs + scope pitfall; split Legal Research +
  add State Citations w/ opencase.com). Weave mnemonics where they earn it; Humanizer voice. Black-letter
  rules ≥2-reviewer approved; **officer summaries do not exist — the layer is banned project-wide by
  S1 (S1 §2.2 + R6 — audit COH-01); existing "field framing" prose migrates per TEACH-04e below.**
- **Research first.** Per page: current text; resolve flagged doctrinal questions with authority
  (horizontal-pooling vs *Pringle*; knock-and-talk split; caretaking-of-persons); live limits on
  over-cited cases (Santana). Web + CL.
- **Interview-extract.** The brief template + section order sign-off; which topics get exhaustive
  treatment; voice heaviness. *Show:* one fully rewritten doctrine brief as the pattern.
- **Deliverable.** `S7-doctrine-production.spec.md` + per-page change-list.
  ✅ **Written 2026-07-03** (pattern page = mockup commits `e0935ce` + `4b48a4a` — Knock and Talk,
  the normative template; change-list `_overhaul2/S7-CHANGELIST.md` signed with the spec, 93 rows
  tiered; all injected:S7 audit rows dispositioned in the Decision Log). Decided highlights:
  template signed as shown (D1); TEACH-04e = convert-or-delete content test (D2); **Prompt.md
  reference DROPPED** (D3, COH-14 closed — the §4-S7 list is the record, consumed verify-then-
  apply; the "community caretaking reaches persons" item was REFUTED by research and corrected);
  depth tiers A/B/C (D4/D6); **non-investigative person seizures covered caretaking-adjacent**
  (D5); **SACO/constructive entry head-on** in Arrest-in-the-Home (D7, *Nora* spine); TEACH-03 =
  four-tier pinpoint-conversion method; two new scar rules (no verification inheritance ·
  per-item citation support) from the flashlight correction (D8). Cross-spec: S6 § Amendments A1
  (planning-time candidates) + §4-S9 S7-interview inputs (a)–(e). The spec text wins over this
  entry (§0 precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **TEACH-01** relocate SCOTUS holdings out of every "Recent developments" section (5+ pages; FA
  Framework worst) · **TEACH-02c** strip reader-facing pipeline-vocabulary leaks per the broadened R14
  (rule IDs, "Re-homed from…", "CL-confirm pending", "No standalone case page" ×12, …) · **TEACH-03**
  corpus-wide slip-op→reporter pinpoint conversion (absorbs LAW-04) · **NUM-01** sizing for TEACH-03:
  43/47 case pages **plus ~22 doctrine pages** · **TEACH-04a** fix the inverted Golden-Rule maxim
  header (PC/RS :61) · **TEACH-04b** qualify "a shot that misses…is not a *force* seizure" ·
  **TEACH-04c** register or cut the "two C's" mnemonic (Miranda :23) · **TEACH-04d** fix the 21
  "SCOTUS — binding" label-order inversions · **TEACH-04e** define + apply the field-framing
  delete-vs-convert-to-N3-list migration rule (ties COH-01) · **TEACH-04f** fix the
  `[[CREW|Three Golden Rules]]` mislink · **TEACH-04g** "persuasive history" → tier "Historical" ·
  **TEACH-04h** fix the Warrant Requirement Sources :149 editing residue · **TEACH-05** em-dash
  rewrite pass (~1,100 hits in sample; policy = S1/TEACH-06) · **TEACH-08** apply the S5 heading
  standard for "Recent developments" · **TEACH-12a** add the missing `# Title` H1 (~14 doctrine
  pages) · **TEACH-12b** migrate the 6 legacy `## Rule`-skeleton pages to The Brief (FA Framework is
  a hub page) · **GAP-03b** scope the emerging-tech cluster into the Third-Party/Digital rewrite
  (reverse-keyword H · StingRay H · real-time CSLI M · IGG M · BWC M) · **GAP-03c** brief §702 /
  parallel-construction mention · **GAP-06** hotfixed (geofence pitfall) — verify no residue in the
  rewrite · **LAW-05** strip the stale "CL object 10813527 CORRUPTED" Zorn legend (§1983 page :188;
  same misdiagnosis class as LAW-02 — correct per S2 A1's root cause) · **NUM-08** negative scope:
  "persuasive, not binding" is already clean — budget no work.

### S8 — Legal-Term & Case Linking + Glossary
- **Direction.** Link **every named case** anywhere (even short names) → its page; deep-link/highlight
  to a pinpoint when discussing a passage. **Liberal** legal-term backlinks — every occurrence of a
  term-of-art links to `Common Legal Terms` with a hover preview. Single-source transclusion of
  canonical rule/term nodes. Audit/expand the glossary from finalized S7 text (non-vernacular only).
  Seed: **388 distinct cases have ≥1 bare (unlinked) mention** (2026-07-01 audit; confirmed by
  NUM-04). **Split (audit COH-15): S8 links ALL 388 once pages exist; S6 verifies + authors only the
  ~80–84 no-page subset** (`_overhaul2/S6-SEED.md`) — see §4-S6.
- **Research first.** `LINT-5`/`LINT-7`, the popover mechanism, `_overhaul/ledger/S7-term-map.md`.
- **Interview-extract.** Term-of-art inclusion test; every-occurrence vs first-occurrence (user leans
  every); highlight/pinpoint policy. *Show:* a page at the proposed link density + hover previews.
- **Deliverable.** `S8-linking-glossary.spec.md`.
  ✅ **Written 2026-07-04** (mockup commits `981b286` + `51e1f4b` + `baa1e17` + `5b48d85` +
  `5d747f9` — Knock and Talk at signed density + Curtilage embeds + Jardines/Walker/Lundin
  pincite exhibits; all S8 audit rows dispositioned in the Decision Log). Decided highlights:
  **every-occurrence** linking (D1) with a shared exemption-zone catalog; four-way term routing
  (page / glossary / citing / vernacular-skip) as register columns (D2); the **split pincite
  convention** (D5) — case name → internal **pin-deep** with a centered flash + persistent tint
  (D3), pincite pages → **external CL `#:~:text=` fragment** highlighting the verified quote
  (D4; fragments derive only from G3-passed lake quotes, validated against cached text —
  S2 § A14 adds `pinpoints[].fragment`); embeds = **rule nodes + pinned quotes only**, boundary
  = the S1 A3 shingle detector, **full-slug targets** (alias-stub transclusion trap found live)
  (D6); glossary-definition embeds rejected (hover suffices). Fail-closed short-name resolver
  (three-Morgans guard); `_run/s8-link-ledger.json` joins S6's ledger = the COH-15 machine
  reconciliation; LINT-5/LINT-7 rewritten (ledger-aware bare-caption rule; first-occurrence rule
  deleted; broken anchors → HIGH); **mid-line-pin remediation moves content-side to S8** (R6;
  LINT-9 + verification stay S9 — NUM-03 boundary). The spec text wins over this entry (§0
  precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **COH-15** link ALL 388 bare-mention cases once pages exist (S6 authors the no-page subset;
  reconcile the 388 / ~84 / LINT-5 numbers jointly with S6) · **NUM-04** the 388 seed is confirmed
  (40/40 sample hit-rate; conservative floor ≥365) · **NUM-02** pipe-escaping work list: **18 files /
  69 affected table lines** (per-file list in the audit report). *(All three dispositioned in the
  signed spec — COH-15/NUM-04 ADOPT, NUM-02 ADOPT-ADAPTED seed-not-gospel; plus an ADAPT pointer
  on S9's NUM-03: remediation rides S8 R6, lint+verify stay S9.)*

### S9 — Verification Pipeline & Release Gate
- **Direction.** The continuous, fail-closed pipeline (not just a final pass) + the release gate:
  **writer ≠ checker**; **1 Claude + 2 Codex** adversarial panel (ALI-style multi-reviewer for
  black-letter; real **≥2-of-3 refute tally**); the **10-gate protocol**; a **machine-emitted
  reconcilable ledger** (findings→adjudications→fixes→inventory, so we can audit the audit);
  **forced primary-source reads** on recent/high-profile cases; **web + CL** research fan-out (circuit
  splits, illustrative examples, cited-case chasing); blind re-derivation by a different model;
  post-fix re-review by a model that didn't write the fix. Runs the question checklist (framed?
  explained? cited? related? narrowed? expanded? good law? abrogated/overruled? current treatment?).
  Reads from S2 (barely touches live CL). **CI lints (fail-closed):** term register (Vale), structure,
  link/cite resolve, **`^pin-N` carat-leak**, build — extend `scripts/lint/`. Codex reviewers via
  headless `codex exec` (verified working; no CL MCP needed).
- **Research first.** `S9-verification.spec.md` (O1) + findings/adjudications; the Codex-reviewer
  harness; the ledger schema; `PRACTICES.md` §3/§6.
- **Interview-extract.** Exhaustive vs sampled primary re-reads; refuters per finding; Codex model
  (gpt-5.5) + how the two Codex lanes stay independent; definition-of-done. *Show:* the
  finding/adjudication JSON schema + one worked finding through find→adjudicate→fix→re-review.
- **Deliverable.** `S9-verification.spec.md`.
  ✅ **Written 2026-07-04** (worked exhibit `_overhaul2/s9-demo/` — one real finding (COH-28)
  driven live through find → 3-lane panel → ≥2-of-3 refute kill → MODIFIED adjudication → fix →
  non-author re-review (NOT-FIXED round 1, FIXED loop 2); ledger schema signed on it; all
  injected:S9 rows + S7 inputs (a)–(e) + S8 handoffs dispositioned in the Decision Log). Decided
  highlights: **exhaustive blind re-derivation** corpus-wide with a serious discordance
  adjudication layer (D1 — cache-fed, zero CL quota; Thread-N staffing split by grain, D2);
  panel = legal assertions + rule layer (D3); release gate = full composite (D4);
  completeness = bounded instruments + absence-claim sweep + **sampled frontier re-run with a
  fail-closed full-re-run tripwire** (D7), all discovery **dual-model Claude + Codex**
  (`codex exec -c tools.web_search=true` verified live; the root `--search` flag does NOT pass
  through `exec`); CL first-class with whitelisted-secondary evidence fallback; lint roster
  codified LINT-1…30 (LINT-12/13/14 re-pointing executed — S2 § A15; LINT-3 rebuilt lake-driven
  per the demo adjudication); maintenance handoff to GH#2 as machine artifacts (D6); S6 § A2
  filed (dual-model frontier). The spec text wins over this entry (§0 precedence).
- **Audit inputs (2026-07-02)** — from `AUDIT-2026-07-02.md`; address each (adopt / adapt /
  reject-with-rationale) in the spec's Decision Log:
  **COH-17** writer ≠ checker weakened (Codex builds the lake AND staffs 2 of 3 review lanes) — route
  the **≥1-in-10 identity spot-check to the Claude lane** · **COH-21** standardize lint naming
  (numeric LINT-9/10 vs `LINT-S2-*`) before codifying the roster (w/ the S1 amendment) · **COH-27**
  checklist line: re-poll "pending" markers (*Carter v. United States* cert-watch, No. 25-885) ·
  **COH-28** fold the open LINT-3 Chatrie recent-dev false-positive fix into the CI-lint roster ·
  **TEACH-02b** enforcement lint for the broadened R14 (ALL pipeline vocabulary, not just two
  phrases) · **TEACH-11** mnemonic-register lint needs **wikilink-target checks** (the CREW mislink
  and the inverted maxim both pass a naive text lint) · **NUM-03** size LINT-9 for **~230-file
  remediation** (299 visible mid-line `^pin-N` anchors across 233 files; 672 end-of-line masked by
  Quartz parsing) · **S2F-07b** (routed via amend:S2) — S9 rechecks S7 prose authored against
  provisional point slugs after the S3 binding map resolves them.
- **S7-interview inputs (2026-07-03)** — from the S7 thread (`S7-doctrine-production.spec.md`
  Lessons/Verification); address each in the S9 spec like audit rows:
  **(a)** Claude-lane CL spot-checks must resolve `opinions[].id` from search results before
  `read_document`/`search_document` — CL page URLs `/opinion/<id>/` carry **cluster** ids and the
  read tools silently fetch wrong/partial objects (the LAW-02 misdiagnosis class; reproduced live
  2026-07-03) · **(b)** G2 support checks run **per enumeration item** — one citation does not
  vouch for a conjoined list's other items (scar exhibit: the O1 "dog or flashlight" knock-and-talk
  pitfall, corrected commit `4b48a4a`) · **(c)** the coherence pass adds a **cross-page
  contradiction sweep** on shared points (exhibit: Knock-and-Talk vs Plain View on flashlight
  illumination — contradiction, not duplication, so the shingle detector never fires) ·
  **(d)** TEACH-03 re-verification samples **by conversion tier** (S7 R5's four-tier method;
  tier-3 paraphrase-downgrades re-verify G2 support — there is no quote for G4; every conversion
  records its source) · **(e)** LINT-10's counting unit = **block** (paragraph or list item);
  Sources trailing info is parenthesized per S5 R12, never em-dashed.

> **Deferred run #1 (audit COH-23 — full URL: <https://github.com/Enragedsaturday/cssi/issues/2>, the
> FORK's issue #2):** the **Maintenance Loop** — post-publish entry ownership + citator-
> watch re-verification (CL alerts) + a "New Topic" staging area + dual-date decay. A separate run.
>
> **Deferred run #2 (audit COH-05; user decision D3): the FLASHCARD REBUILD.** Post-S9, rebuild the
> frozen deck from finalized content — the deck deliberately carries stale content until then
> (COH-05d). Constraint assigned NOW: **S3 (renames/re-homings/unlisting — COH-05b) and S4
> (platform/nav — COH-05c) must preserve deck-referenced stems/aliases** or knowingly accept + log
> the breakage for the rebuild.

## 5. Adopted mechanisms
See **`PRACTICES.md`** for the full text of: the three-field treatment vocabulary (§2), the 10-gate
verification protocol (§3), the comprehensive-research saturation protocol (web + CL, §4), the
graded-authority entry model (§5), the AI guardrails G1–G10 (§6), the reader-facing signaling scheme
(§7), and the style-manual + term-register + CI approach (§8). See **`CL-DATA-INVENTORY.md`** for the
exact CourtListener fields/calls per data element (the S2 schema).

## 6. Reference inputs & key paths
- **O2 planning:** `_overhaul2/RUNBOOK.md` (this) · `PRACTICES.md` · `CL-DATA-INVENTORY.md` ·
  `specs/` (outputs). Briefs: `~/briefs/2026-07-01-cssi-overhaul-2-findings-and-bundle.html`,
  `…-taxonomy-proposal.html`, `…-reconsidered-plan.html` (all inputs, not decisions).
- **Overhaul-1 kit:** `_overhaul/` · `docs/STANDARDS.md`, `docs/FINAL-QA-SPEC.md`, `docs/RUNBOOK.md`
  · `_run/FINAL-S9-REPORT.md` · `scripts/lint/`.
- **Book + taxonomy refs:** `.orca/drops/Book Jun 26, 2026.pdf` (TOC), `…(1).pdf` (case-example →
  S5 — **RESOLVED 2026-07-03: reference dropped at the S5 interview (user D12) — audit COH-14**), `SSTOC.pdf`
  (LaFave), `New Jersey Law Enforcement Handbook…pdf`, `Prompt.md` (user intent — **missing: not in
  the repo anywhere; §4-S7 carries the surviving fix-list; regenerate or drop at the S7 interview —
  audit COH-14**). **`.orca/drops/` is LOCAL-ONLY** — untracked, and the copyrighted PDFs must never
  be committed (audit COH-14).
- **Content:** `content/` (canonical) — categories + `content/cases/` (~457) + Case Index.
- **Platform:** `quartz.config.ts`, `quartz.layout.ts`, `quartz/components/` (Explorer, Search, Footer,
  CaseTable, TreatmentBadge, popover). Dev: `npx quartz build --serve` → :8080.
- **Codex reviewers:** headless `codex exec -s workspace-write -c approval_policy=never
  --skip-git-repo-check --json -C <dir> -o <last.txt> "<prompt>" < /dev/null` (wrap in a timeout —
  macOS has no GNU `timeout` and `gtimeout` is absent on this host: use the caller's own timeout
  mechanism, e.g. the harness/tool-level timeout — audit COH-31);
  model gpt-5.5. Codex CL MCP optional/broken — reviewers read the data-lake. **CL credentials (audit
  COH-07): L4 rescoped by S1 amendment — one serial lane per credential; the Codex REST builder owns
  the token, the Claude MCP lane does interactive spot-checks only.**
- **Maintenance:** <https://github.com/Enragedsaturday/cssi/issues/2> (the fork's issue #2 — audit
  COH-23). **Publish:** push `origin main` → Vercel (reconcile in S4).

## 7. Status
| Spec | Interview | Spec written |
|---|---|---|
| S1 Standards & Style Manual | ✅ | ✅ |
| S2 Verified Authority Database | ✅ | ✅ |
| S3 Taxonomy & Points-of-Law | ✅ | ✅ |
| S4 Platform, Nav & Reader-Signaling | ✅ | ✅ |
| S5 Entry Models | ✅ | ✅ |
| S6 Coverage & Ingest | ✅ | ✅ |
| S7 Doctrine Production | ✅ | ✅ |
| S8 Legal-Term & Case Linking | ✅ | ✅ |
| S9 Verification Pipeline & Release Gate | ✅ | ✅ |

*Coherence pass over all nine: ✅ **PASSED 2026-07-04** — `_overhaul2/COHERENCE-REPORT.md`
(18 findings: 4 fixed-now · 3 amended:S9 · 2 covered · 9 no-defect; zero user-decision
conflicts) + the **AUDIT-CLOSURE gate STAMPED PASS** by the adversarial non-writer lane
(162/162 rows · 58/58 injected IDs, 61/61 legs). Next: the one autonomous EXECUTE run
(data-lake first) — launcher: `_overhaul2/wrappers/EXECUTE.wrapper.md`.*

**AUDIT-CLOSURE gate (blocking — part of the coherence pass).** The coherence pass **FAILS** if
either check fails:
1. any row in `_overhaul2/AUDIT-2026-07-02.md` lacks a **terminal disposition + a real pointer**
   (diff, spec-amendment section, RUNBOOK block, commit, or Decision-Log entry);
2. any `injected:S4..S9` ID lacks an explicit disposition (adopt / adapt / reject-with-rationale) in
   its spec's Decision Log.
Phase 5's adversarial agent (not a writer) walks the register and stamps closure.
