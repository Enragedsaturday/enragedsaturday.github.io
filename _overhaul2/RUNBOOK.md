# CSSI Overhaul 2 — RUNBOOK

*The master plan for the second CSSI overhaul, framed as a professional legal-reference **production
line** (Spine → Surfaces → Content → Assurance). This is the artifact a fresh context thread is
pointed at: "run S3" → the thread reads §0–§2 + `PRACTICES.md` + its spec entry in §4, does the
spec's own research, conducts the interview (open-ended + choices, **show-don't-tell** with browser
mockups / written examples), does follow-up research, and writes the spec to
`_overhaul2/specs/SN-<slug>.spec.md`.*

Status: **planning/research phase** — no specs written, nothing in `content/` changed.
Last updated: 2026-07-01.

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

## 1. Per-spec thread lifecycle
1. **Research first (web + CourtListener).** Internal (codebase/corpus + Overhaul-1 findings) **and**
   external. **Use CourtListener AND web search together** — CL has coverage gaps, and web search
   surfaces terminology / legal theories / adjacent keywords that reframe and properly expand the
   search (`PRACTICES.md` §4). Assume nothing; web discovers, primary source confirms.
2. **Show, don't tell.** Visual change → browser mockup on a branch (dev server `npx quartz build
   --serve` :8080), modifying only what's discussed; perfect it there, spec follows to the letter.
   Content change → a **written example** first (one overview, one rewritten brief). **Any officer-
   bottom-line / BLUF summarization is human-in-the-loop and grounded verbatim in the case's standard
   — never auto-generated** (paraphrase drift on the controlling standard is the trap that pulled us
   back from this in Overhaul 1).
3. **Interview.** Options + context + open-ended opener; ask only user-owned decisions (recommendation-
   first, `AskUserQuestion`); self-resolve the rest and log it. **Always close open-ended** and
   interview on the answer. Don't over-produce; long material → briefs.
4. **Follow-up research** to resolve surfaced questions (with authority).
5. **Write the spec** (Overhaul-1 template: Objective · Scope · Requirements w/ `*Check:*` · Lessons ·
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
  reasonable belief*, not "imminent danger") → S5/S7, human-in-the-loop.
- **`^pin-N` carat leak** — Obsidian block-ref anchors rendering as visible text; "everything must
  look perfect" → S9 + a CI lint.
- **Content structure**: apply-it prose not numbered lists; leaked "(woven in)" meta; "persuasive,
  not binding"; tests/prongs not up front; SCOTUS in "Recent developments" → S1 rules + S7.

**Feasibility (2026-07-01):** headless `codex exec` works (stdin `/dev/null` + timeout wrapper).
**Codex's CL MCP OAuth is still expired** (3 tries; fix = `codex mcp logout courtlistener && codex
mcp login courtlistener` from the CLI) — but **not blocking**: reviewers read the data-lake, not live
CL, and the lake is best built via the direct CL REST API (token) or the authenticated Claude CL MCP.
Live sites 200; popovers on; FlexSearch in place; MIT needs only `LICENSE.txt` retained.

## 3. The bundle & execution plan
**Nine specs**, production-line waves. Maintenance loop **deferred** → GitHub issue #2. Nesting max 3
levels (index-1 umbrella w/ overview → index-2 doctrine/sub-umbrella → index-3 doctrine).

| # | Spec | Build order | Depends on | Exec wave |
|---|------|-------------|-----------|-----------|
| **S1** | Standards & Style Manual | 1 | — | 0 (rulebook) |
| **S2** | Verified Authority Database (CourtListener source-of-truth) | 2 | S1 | 1 (built first) |
| **S3** | Taxonomy & Points-of-Law (categories, nesting, nav structure) | 3 | S1 | 2 (restructure) |
| **S4** | Platform, Nav & Reader-Signaling UI | 4 | S1 | 1 (nav working-standard, before restructure) |
| **S5** | Entry Models (case + doctrine pages) | 5 | S1,S2,S3 | 2 |
| **S6** | Coverage & Ingest (verify + author missing cases) | 6 | S2,S3,S5 | 3 |
| **S7** | Doctrine Production (brief-first rewrite) | 7 | S1,S2,S3,S5,S6 | 3 |
| **S8** | Legal-Term & Case Linking + Glossary | 8 | S4,S7 | 3 |
| **S9** | Verification Pipeline & Release Gate (1 Claude + 2 Codex) | 9 | all | 4 |

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
  mnemonic policy (3 Golden Rules, C.R.E.W. "RE", strive-for-five, CRON), and the **Humanizer** subset
  fit for a legal register. Each rule → Trigger/Check/Enforcement (testable by S9 + lints).
- **Research first.** Re-read `docs/STANDARDS.md`, `docs/FINAL-QA-SPEC.md`; fetch + evaluate the
  Humanizer skill; verify mnemonics verbatim (incl. CRON's Bandiero expansion).
- **Interview-extract.** Humanizer subset that applies vs. can't; voice heaviness; exact lexicon
  wording; **the graded-authority depth** — *mock up ALI-full vs. lighter "rule + notes" and choose.*
  *Show:* before/after voice paragraph; the two graded-authority variants.
- **Deliverable.** `S1-standards.spec.md` (+ `docs/STANDARDS.md` + `STYLE.md` at execution).

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
- **Deliverable.** `S2-authority-database.spec.md`.

### S3 — Taxonomy & Points-of-Law
- **Direction.** Our own category tree (3-level nesting; umbrella w/ authored **overview page** →
  doctrine/sub-umbrella → doctrine), self-explanatory, each node self-contained, more granular where
  it earns it. Exigency → flavors; relocate Plain View to a seizure cluster; promote
  Checkpoints/Inventory/Border out of the Special-Needs mega-page; rename "Levels of Suspicion" →
  "Standards of Proof" (full burden pyramid, **PC < preponderance**); re-homing rules (Brendlin, Katz,
  Graham); unlist `cases/`; the possible "Home Entry & Search" topic. Do NOT plagiarize the book.
  The taxonomy is also the **controlled classification** every proposition hangs off (spine).
- **Research first.** Current tree + Bandiero TOC + LaFave TOC (`.orca/drops/SSTOC.pdf`) + NJ Handbook
  (`.orca/drops/New Jersey Law Enforcement Handbook…pdf`) + Wex/casebook order + the draft tree
  (`~/briefs/2026-07-01-cssi-o2-taxonomy-proposal.html`, an input only).
- **Interview-extract.** Umbrella set + names; exceptions axis (suspicion-tier vs object vs flat);
  "Home Entry & Search" y/n; "Standards of Proof" rename; nav size; Knock-and-Talk placement; which
  nodes are index-2 umbrellas vs index-3 leaves; per-case re-homings. *Show:* a **live nav mockup** on
  a branch + a written overview page — lock the layout on the mockup before writing.
- **Deliverable.** `S3-taxonomy.spec.md` — target tree + overview list + re-homing table.

### S4 — Platform, Nav & Reader-Signaling UI
- **Direction.** Make the explorer *work* (retarget scroll save/restore to `.explorer-content`; drop
  smooth-scroll-on-nav; fix sidebar padding, two-line wrap; roomier rows; list/paragraph spacing in
  `custom.scss`). Move "Created with Quartz" → a single About page. Reconcile the **publish pipeline to
  `content/`-canonical** (retire the vault sync) so the live site is trustworthy. **Search:** FlexSearch
  fuzzy + case-name "did-you-mean." **Reader signaling** (from `PRACTICES.md` §7): verification badges,
  **dates in the data model + behind a hover + on the About page (NOT inline everywhere)**, treatment
  flags, overruled-as-history rendering, pills-as-anchors (so popovers work). Includes the honest
  keep-Quartz-vs-fork evaluation. This is a *working standard*, executed **before** the S3 restructure.
- **Research first.** The technical audit (files located); FlexSearch `suggest`/tuning; OSS nested-nav
  options; the launchd/`redeploy.sh` publish path.
- **Interview-extract.** Fix stock explorer vs. OSS nested-nav (mock both); fuzzy aggressiveness;
  About-page content + attribution; how much provenance shows on hover. *Show:* side-by-side explorer
  mockups + a search-suggestions demo + a treatment-badge/hover mock on the dev server.
- **Deliverable.** `S4-platform-ui.spec.md`.

### S5 — Entry Models (case + doctrine pages)
- **Direction.** The **graded-authority doctrine page** (black-letter rule / explanation / authorities
  — `PRACTICES.md` §5) and the **BIRAC case page** (keep the liked BIRAC; the officer-bottom-line /
  "In the field" box is a **human-in-the-loop, standard-grounded** option to design carefully, not
  auto-generate). Standardized case-table schema (short shared headers, controlled widths, no
  side-scroll); treatment **pill under the case name**, **weight in the case column**, treatment column
  + "treated in full" removed, relevance tags under relevance; the pill is an **anchor** to the
  "Verifying Good Law / as-of" page with hover preview; "limited by/expanded by" folds into the holding.
  Draft-state machinery (`draft → under_review → verified`); provenance rendering.
- **Research first.** `CaseTable.tsx`/`casetable.inline.ts`/`TreatmentBadge.tsx` (spans → `a.internal`);
  the book case-example PDF (`.orca/drops/Book Jun 26, 2026 (1).pdf`); S2 schema.
- **Interview-extract.** BIRAC section order + officer voice; **ALI-vs-lighter graded-authority** (mock
  both — shared with S1); final table columns; as-of page + hover; where deep-link/pinpoint highlights
  apply. *Show:* browser mockup of the new table + pill + hover; one written BIRAC page; the two
  doctrine-page authority variants.
- **Deliverable.** `S5-entry-models.spec.md`.

### S6 — Coverage & Ingest
- **Direction.** Verify + author the **named-but-no-page** cases (2026-07-01 audit: ~70–80 genuine,
  mostly circuit). **Verify existence first (two-key; "not found ≠ fabricated"; compare input name vs
  CL canonical)** — author a BIRAC page + external link for real ones, **remove** fabrications
  (*Mayville/Small/Lyle/Moore-Bush* were flagged). Diff the corpus against book roster ∪ named-in-prose
  ∪ prior-research ∪ bounded frontier; officer-field-relevance gate. Fix ~6 alias/variant mismatches;
  ignore ~5 citation-format placeholders. (Full seed: this file's earlier §S6 seed / `audit_cases.py`.)
- **Research first.** The audit list; Overhaul-1 coverage (`_overhaul/coverage/`); the comprehensive-
  research protocol; a why-missed taxonomy.
- **Interview-extract.** Relevance gate threshold; frontier reach; borderline sign-off. *Show:* the
  missed-case list + why-missed→generalized-search on a sample.
- **Deliverable.** `S6-coverage-ingest.spec.md`.

### S7 — Doctrine Production (brief-first)
- **Direction.** Produce/rewrite each doctrine/narrative page *through* the draft→review→verified
  pipeline: brief-first (rule + tests up front + limits + nuance + pitfalls integrated, no "(woven in)"
  label); numbered apply-it lists; nothing after the tables except the diagram; fix slip-op pinpoints,
  pipe-escaping, `^pin-N` leaks; per-page fixes from `Prompt.md` (Matlock is a Consent table-entry;
  CREW "R"→"RE"; Herring→Key on Collective Knowledge; Riley→Related on Common Law; community caretaking
  reaches persons; Dunn factors in the Rule; Knock-and-Talk = lawful-presence/implied-license; Bandiero
  hot/fresh-pursuit line; Santana "limited by"; consent 3 prongs + scope pitfall; split Legal Research +
  add State Citations w/ opencase.com). Weave mnemonics where they earn it; Humanizer voice. Black-letter
  rules ≥2-reviewer approved; officer summaries human-in-the-loop.
- **Research first.** Per page: current text; resolve flagged doctrinal questions with authority
  (horizontal-pooling vs *Pringle*; knock-and-talk split; caretaking-of-persons); live limits on
  over-cited cases (Santana). Web + CL.
- **Interview-extract.** The brief template + section order sign-off; which topics get exhaustive
  treatment; voice heaviness. *Show:* one fully rewritten doctrine brief as the pattern.
- **Deliverable.** `S7-doctrine-production.spec.md` + per-page change-list.

### S8 — Legal-Term & Case Linking + Glossary
- **Direction.** Link **every named case** anywhere (even short names) → its page; deep-link/highlight
  to a pinpoint when discussing a passage. **Liberal** legal-term backlinks — every occurrence of a
  term-of-art links to `Common Legal Terms` with a hover preview. Single-source transclusion of
  canonical rule/term nodes. Audit/expand the glossary from finalized S7 text (non-vernacular only).
  Seed: **388 distinct cases have ≥1 bare (unlinked) mention** (2026-07-01 audit).
- **Research first.** `LINT-5`/`LINT-7`, the popover mechanism, `_overhaul/ledger/S7-term-map.md`.
- **Interview-extract.** Term-of-art inclusion test; every-occurrence vs first-occurrence (user leans
  every); highlight/pinpoint policy. *Show:* a page at the proposed link density + hover previews.
- **Deliverable.** `S8-linking-glossary.spec.md`.

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

> **Deferred (GitHub issue #2):** the **Maintenance Loop** — post-publish entry ownership + citator-
> watch re-verification (CL alerts) + a "New Topic" staging area + dual-date decay. A separate run.

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
  S5), `SSTOC.pdf` (LaFave), `New Jersey Law Enforcement Handbook…pdf`, `Prompt.md` (user intent).
- **Content:** `content/` (canonical) — categories + `content/cases/` (~457) + Case Index.
- **Platform:** `quartz.config.ts`, `quartz.layout.ts`, `quartz/components/` (Explorer, Search, Footer,
  CaseTable, TreatmentBadge, popover). Dev: `npx quartz build --serve` → :8080.
- **Codex reviewers:** headless `codex exec -s workspace-write -c approval_policy=never
  --skip-git-repo-check --json -C <dir> -o <last.txt> "<prompt>" < /dev/null` (wrap in a timeout);
  model gpt-5.5. Codex CL MCP optional/broken — reviewers read the data-lake.
- **Maintenance:** GitHub issue #2. **Publish:** push `origin main` → Vercel (reconcile in S4).

## 7. Status
| Spec | Interview | Spec written |
|---|---|---|
| S1 Standards & Style Manual | ☐ | ☐ |
| S2 Verified Authority Database | ☐ | ☐ |
| S3 Taxonomy & Points-of-Law | ☐ | ☐ |
| S4 Platform, Nav & Reader-Signaling | ☐ | ☐ |
| S5 Entry Models | ☐ | ☐ |
| S6 Coverage & Ingest | ☐ | ☐ |
| S7 Doctrine Production | ☐ | ☐ |
| S8 Legal-Term & Case Linking | ☐ | ☐ |
| S9 Verification Pipeline & Release Gate | ☐ | ☐ |

*Coherence pass over all nine → one autonomous EXECUTE run (data-lake first).*
