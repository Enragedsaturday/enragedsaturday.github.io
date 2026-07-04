# CSSI — STANDARDS (the governing contract)

status: GOVERNING · authority: TOP
supersedes: `docs/FINAL-QA-SPEC.md` (authority absorbed; retained as history)
derived-from: `_overhaul2/specs/S1-standards.spec.md` §3 + Amendments A1–A9 (this document is the
prose realization of the signed O2 S1 spec; the O1 catalog is carried per S1 R1)
companion: `docs/STYLE.md` (house style · term register · Humanizer voice subset · mnemonic register)
last-updated: 2026-07-04 (O2 EXECUTE Wave 0)

---

## 0. Supremacy clause (SR-3)

**`docs/STANDARDS.md` is the single top-authority contract for the CSSI overhaul.**

It **absorbs** `docs/FINAL-QA-SPEC.md`'s §0 adversarial self-critique (the 15-point
failure-mode register) and the D1–D12 reviewer dimensions — now **carried, extended, and
expanded to D1–D14** in §4 below. `docs/FINAL-QA-SPEC.md` is retained only as historical
reference and carries a pointer header transferring its authority here.

On **any conflict** between this document and any other document — a spec, a runbook, a
prior manifest, the QA spec, a page convention — **STANDARDS.md governs**, subject to one
exception: the **signed Overhaul-2 specs** (`_overhaul2/specs/S1…S9`, including their
Amendments) are the law of the O2 EXECUTE run (RUNBOOK §0 precedence); this document is the
S1 spec's realization and must never diverge from it. Every later spec and the autonomous
**EXECUTE** run are bound by it: each must cite STANDARDS.md as governing and may extend it,
but may never contradict or weaken it.

This document is written to be read **top-to-bottom** as a reference and **grepped** by
rule ID (`L1`…`L8`, `N1`…`N13`, `SR-1`…`SR-14`), by verification gate (`G1`…`G10`), by
guardrail (`AI-G1`…`AI-G10`), by dimension (`D1`…`D14`), and by lint (`LINT-1`…`LINT-30`).
Nothing here edits content pages; it states the rules every page, deck, card, and
verification pass must satisfy.

**The catalog at a glance:** 8 scar-rules (L1–L8) + 13 mechanism-rules (N1–N13) + 14
standard rules (SR-1…SR-14; SR-6…SR-14 are the Overhaul-2 additions) = **35 enforceable
rules**, mapped onto **14** reviewer dimensions, **10** verification gates, **10** AI
guardrails, and the automated lint roster (LINT-1…14 defined here; the full 1–30 roster is
codified fail-closed at S9).

---

## 1. How to read a rule

Every rule is stated **testable**, with:

- **Rule statement** — what is required.
- **Trigger** — when the rule applies (the condition that puts a page/assertion in scope).
- **Check** — how a reviewer or script verifies compliance.
- **Enforcement** — one or more tags:
  - `AUTO:LINT-n` — a deterministic script in the lint roster (§7) decides it.
  - `CHECKLIST:Dn` — reviewer judgment against dimension *Dn* (§4) decides it.
  - `PROCESS` — orchestration discipline (the research protocol §5, the
    find→adjudicate→fix machine §6) decides it.

A rule may carry more than one tag (e.g. an `AUTO` guard plus a `CHECKLIST` backstop).

---

## 2. The rules catalog

### 2.A Scar-rules (already paid for — carried from the lessons register)

These eight are failure modes a prior build actually hit. They are non-negotiable.

#### L1 — Two-key rule / paraphrase drift
Every holding, rule statement, and quotation on any page or card traces to the primary
opinion via the **two-key rule**: **(key-1)** existence + proposition + verbatim pinpoint
where quoted; **(key-2)** good-law status. **Decks derive FROM verified pages, never the
reverse.** The professionalized form of the two keys is the 10-gate protocol (§5A).
- **Trigger:** any asserted holding / rule / quote / case anywhere.
- **Check:** the assertion appears in the assertion inventory with a CL-cited verdict;
  quotes are verbatim with a confirmed pinpoint; no card asserts a fact absent from its
  source page.
- **Enforcement:** `AUTO:LINT-2` (quote/pinpoint presence) + `AUTO:` deck↔page id check +
  `CHECKLIST:D1`.

#### L2 — Web is discovery-only
Nothing enters a page until confirmed against the primary opinion on CourtListener.
**Discovery ≠ assertion.**
- **Trigger:** any content sourced from web / secondary material.
- **Check:** every web-surfaced case/holding/quote has a corresponding CL confirmation in
  the manifest before it appears; unconfirmed items are flagged, never asserted.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D1/D3`.

#### L3 — cluster-id ≠ opinion-id
Every CL URL must resolve (HTTP 200) **AND** display the **named** case (identity, not just
status). Resolve cluster → lead opinion id; confirm the case name in returned text before
trusting any quote. Cluster ids and opinion ids are **separate namespaces that collide
numerically** — an opinion id comes only from `cluster.sub_opinions[]`, search
`sibling_ids[]`, or search `opinions[].id`, never from a page URL (which carries the
**cluster** id).
- **Trigger:** any CL URL on a page, or any quote read from CL.
- **Check:** the link-checker confirms the URL resolves and the returned text contains the
  case name; quote-reads are logged against the confirmed opinion id.
- **Enforcement:** `AUTO:LINT-1` (CL-URL identity) + `CHECKLIST:D7`.

#### L4′ — One serial CL lane per credential *(rescoped by S1 Amendment A1, 2026-07-02)*
Every CourtListener **credential** has exactly **one consumer**, serial within itself —
never two consumers on one credential.
- The **S2 Codex REST builder exclusively owns the project API token**
  (`~/.config/cssi/cl-token`); it is serial within itself and paced per S2 R10
  (token-bucket ≤~14 req/min, backoff, journal). No other process, agent, or lane may touch
  that token for any purpose — not review, not adjudication, not "one quick check"
  mid-build.
- The **Claude CL MCP** (claude.ai-managed connector) is a **separate credential**, used
  for **interactive spot-checks only** — never for bulk ingest, never scripted against the
  project token's quota.
- **Trigger:** any CL call anywhere in execution.
- **Check:** every builder journal / `cl-calls.log` line records the **consumer identity +
  credential fingerprint** (S9 audits on those fields); the log shows only builder calls on
  the project token with no concurrent timestamps; no MCP-originated call ever appears
  against the project token.
- **Enforcement:** `PROCESS` + `CHECKLIST` (log audit, S9).
- *Why rescoped:* the O1 global single lane made interactive review queue behind a 20–30 h
  build; CL enforces rate limits per credential, so per-credential serialization preserves
  the anti-breach intent (never self-inflict concurrency on one quota) while the
  two-consumer design stays legal.

#### L5 — find → adjudicate → fix (no reviewer edits)
Hard separation of the three roles. A reviewer never edits; a **legal** assertion never
changes without CL evidence at adjudication.
- **Trigger:** any review finding that would change a page.
- **Check:** every change traces to an adjudicated verdict (UPHELD/MODIFIED) with evidence;
  reviewers produced findings only; DISMISSED findings are logged with a reason.
- **Enforcement:** `PROCESS` (§6) + `CHECKLIST` (audit the findings→adjudications→fixes trail).

#### L6 — "Not found" ≠ "doesn't exist"
Before declaring a case fake/unverifiable, run the **misspelling-tolerant escalation
ladder** (reporter cite → name/phonetic variants → proposition full-text → web → re-locate
in CL). Only then mark `UNVERIFIABLE`, flagged, never asserted. Compare the **input name
against the CL canonical name ourselves** — the automated name-mismatch warning is masked
by cite dedup.
- **Trigger:** any CL lookup miss on a captured/cited case.
- **Check:** an `UNVERIFIABLE` verdict shows the full ladder was run (logged); no case
  marked fake from a single miss.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D1`.

#### L7 — Scope-boundary claims are assertions (no narrow-scope synthesis)
A statement that **bounds a doctrine's reach — especially a *negative* bound** ("does not
reach X", "only Y", "vehicles, not persons") — is an **assertion, not discovery** (L2), and
carries the **two-key burden**. It must rest on **frontier-level** progressive research
(N12 Hop-2: circuit/state treatment, splits, first-impression) confirmed against
**primary** authority — never on secondary-source synthesis alone. Until that research is
run, the scope is recorded as **"unresolved — research,"** never as the narrow reading.
*(Scar: in the O1 S2 interview, community caretaking was first framed "vehicles, not persons
outside the home" from secondary synthesis; the mandated frontier pass then surfaced the
controlling person-caretaking line —* United States v. Garner *(10th Cir.) 3-part
caretaking-detention test;* United States v. Rideau *(5th Cir.) impaired-person-in-roadway;*
Graham v. Barnette *(8th Cir.) PC-of-dangerousness for emergency mental-health seizures —
reversing the boundary.)*
- **Trigger:** any who/what/where scope statement; any "only / never / does-not-reach"
  language.
- **Check:** every scope boundary cites primary authority at the frontier; negative bounds
  show the Hop-2 frontier pass was run (logged); no scope claim rests on secondary synthesis
  alone.
- **Enforcement:** `PROCESS` (§5 — frontier hop mandatory for scope claims) + `CHECKLIST:D2/D4`.
- *Relation:* strengthens **N10** (state scope) and **N12** (progressive research); sibling
  of **L2**.

#### L8 — Restatement, not editorialization — and NEVER auto-generate a controlling standard
*(sharpened by S1 R7; the officer-BLUF layer is banned project-wide by SR-9)*
Any explanatory, practical, or teaching paraphrase of a holding or rule — especially the
**un-anchored blocks that do not quote the opinion** — must **restate** it faithfully and
may **not add, drop, narrow, or broaden** a condition of the rule it conveys. **Never
auto-generate a controlling standard, holding, or test:** restate, do not editorialize;
ground it verbatim in the opinion. A paraphrase that moves the holding is **paraphrase
drift (L1)** and, where it bounds reach, a **negative-scope assertion (L7)** — carrying the
**two-key burden**, not a free-writing license. **Operating principle: case pages
*restate*; doctrine pages *teach*.** Doctrine pages teach through the verified Explanation
layer (§8.1) — the reader is given the verified rule + brief and applies it; **no
field-application / officer-bottom-line summary exists anywhere (SR-9)**. *(The canonical
scar: emergency aid requires an "**objectively reasonable basis to believe**" an occupant
is injured — a draft takeaway rewrote it as "**sees** someone in imminent danger," narrowing
a source-agnostic standard into a visual-observation rule the Court never imposed.)*
- **Trigger:** any statement of a controlling standard, holding, or test; any practical/
  explanatory paraphrase of one.
- **Check:** no standard asserted without a pinned primary-source quote/paraphrase that
  matches; the prose adds or drops no element of the pinpointed holding; case pages carry
  no generalized field-advice beyond a faithful restatement; spot-check the paraphrase
  against the opinion.
- **Enforcement:** `CHECKLIST:D1/D2/D4/D9` + `PROCESS`.
- *Relation:* strengthens **L1**, **L7**, and **N1**; realized at page level by **SR-9**
  (Variant A) and the ban in §8.1.

### 2.B Mechanism-rules (from the instructor's page-by-page notes)

#### N1 — Placement by holding, not keyword
A case's home page and key/related status is set by the legal proposition it stands for, not
surface-keyword overlap.
- **Trigger:** assigning a case to a page or to key/related.
- **Check:** each placement is justified by the case's holding (the proposition supports
  THIS page's doctrine); e.g. *Matlock* = consent/common-authority, not abandonment.
- **Enforcement:** `CHECKLIST:D2/D5`.

#### N2 — Authority-weight lexicon
Use the fixed **6-tier lexicon** (§3) everywhere, validated against the **exact allowlist**
(§3, per S1 A8); **never** "persuasive, not binding"; circuit cases name the circuit; splits
flagged; the tier word always comes **first** ("Binding — SCOTUS", never "SCOTUS — binding").
- **Trigger:** any authority/weight label on any case.
- **Check:** every weight label string-matches the §3 allowlist exactly (spacing, order,
  circuit suffix); no banned phrasing; no inverted label.
- **Enforcement:** `AUTO:LINT-4` (exact-allowlist validation) + `CHECKLIST:D6`.

#### N3 — Tests stated up front
Any named test / prongs / elements appear explicitly in the Rule/brief at the top — never
left for the reader to reconstruct (e.g. the *Dunn* 4 factors). "Apply it" sections are
**numbered ordered lists**, not prose.
- **Trigger:** a doctrine governed by a named multi-factor/element test; any "Apply it"
  section.
- **Check:** the test and all its prongs appear in the top brief; every "Apply it" section
  body parses as an ordered list (first non-blank line matches `^\s*[0-9]+\.`).
- **Enforcement:** `CHECKLIST:D14/D4` + `AUTO:LINT-3` (apply-it ordered-list sub-check).

#### N4 — Subsequent treatment inline *(rewritten for the 3-field vocabulary — SR-6)*
Where a case is materially narrowed / limited / abrogated / overruled, the treatment is
carried **structurally** (the Field-II edge in the lake + the Field-I pill rendered under
the case name) and **woven into the holding prose** where asserted ("limited by [linked
case]" folds into the holding text); add a 1–2 sentence *why* **only when it changes field
application**. Treatment must read consistently across every page the case appears on —
same Field-I composite, same controlling cases.
- **Trigger:** asserting a case that carries any material negative Field-II edge.
- **Check:** the treatment is present at the point of assertion wherever the case is
  asserted; the explanation is present iff field application changes; the treatment is
  stated consistently across every page (same composite + `point_overrides` everywhere).
- **Enforcement:** `CHECKLIST:D3/D5` + `AUTO:LINT-12` (lake↔frontmatter drift).

#### N5 — Frontier sections are role-based, not recency-based
The lower-court-developments section (heading standard: **"Lower-court developments"**, the
TEACH-08 rename of "Recent developments") is for circuit/state cases that
expand/narrow/split/first-impression vs SCOTUS. **Any SCOTUS holding belongs in Key cases
regardless of date.**
- **Trigger:** placing a case in the frontier section.
- **Check:** no SCOTUS case appears there (court identity read from the S2 lake, not from
  the label); every entry has an expand/narrow/split/first-impression role labeled.
- **Enforcement:** `AUTO:LINT-3` (lake-driven, section-scoped: no `Binding — SCOTUS` label
  and no wikilink to a SCOTUS-court case page inside the section) + `CHECKLIST:D10`.

#### N6 — Key-status is non-exclusive
A case is Key on a page if central to THAT doctrine, independent of being key elsewhere;
multi-homing is expected and framing is page-specific (promote *Herring* on Collective
Knowledge; move *Riley* to Related on Common Law).
- **Trigger:** assigning key/related to a multi-homed case.
- **Check:** key/related is decided per-page by centrality to that doctrine; framing differs
  appropriately across homes.
- **Enforcement:** `CHECKLIST:D2/D5`.

#### N7 — Link every named case
Every case named anywhere links to its own case page; passage-specific discussion →
deep-link to the pinpoint/highlighted span; whole-case reference → link the case page.
- **Trigger:** any case name in prose/tables.
- **Check:** no bare unlinked case name; passage discussions deep-link; link targets resolve
  (dead wikilinks and broken anchors block publish — fail-closed).
- **Enforcement:** `AUTO:LINT-5` (link-every-named-case + fail-closed wikilink resolve) +
  `CHECKLIST:D13`.

#### N8 — Brief-first
The full teaching brief (rule + limits + nuance + pitfalls, integrated) reads top-to-bottom
first; tables + the frontier section follow as supporting apparatus. The first H2 after
frontmatter is the Brief/Rule section per the §8.1 section order.
- **Trigger:** any doctrine page.
- **Check:** the brief is the first substantive content and is self-contained; apparatus
  follows it; the structural first-H2 check passes.
- **Enforcement:** `CHECKLIST:D14/D10` + `AUTO:LINT-3` (brief-first structural sub-check).

#### N9 — Frame around the field-decisive question (guidance, not a hard rule)
Frame each doctrine around the operational question an officer must answer, not "what is
the exception." For misunderstood topics (e.g. knock-and-talk) be exhaustive on
line-drawing. *Per the S1 decision log: this is a framing **strategy** applied by judgment
where it helps — not a lint-enforced requirement; not every page must carry an explicit
question line. It never licenses a field-application summary (SR-9 ban).*
- **Trigger:** authoring/reformatting any doctrine brief.
- **Check:** the brief orients the reader operationally; reviewer (instructor lens) confirms.
- **Enforcement:** `CHECKLIST:D9/D14`.

#### N10 — State scope explicitly
State what/who/where a doctrine covers; split bundled doctrines; research, never assume
(e.g. community caretaking: persons vs vehicles).
- **Trigger:** a doctrine with ambiguous or bundled scope.
- **Check:** scope is stated explicitly; bundled doctrines split or boundary-noted; scope
  claims are authority-backed.
- **Enforcement:** `CHECKLIST:D4/D2`.

#### N11 — Wire the glossary
Non-vernacular terms link to the glossary (hover-preview + click-through); the glossary is
audited continuously from live page text.
- **Trigger:** any non-vernacular legal term in prose.
- **Check:** terms link to the glossary; the glossary covers all terms used; no orphan terms.
- **Enforcement:** `AUTO:LINT-7` (glossary wiring + term-register enforcement) +
  `CHECKLIST:D13/D11`.

#### N12 — Progressive research
narrow issue → doctrine/keyword → expand → learn → expand, **bounded**. Assume nothing; web
discovers, CL confirms (protocol + bound in §5). **Use CourtListener AND web search
together** — CL has real coverage gaps, and web search surfaces terminology, legal theories,
and adjacent keywords that reframe and properly expand the search.
- **Trigger:** rounding out any page beyond captured seed cases.
- **Check:** research followed the bounded protocol; a stop condition was met; all additions
  are CL-verified.
- **Enforcement:** `PROCESS` (§5) + `CHECKLIST:D4`.

#### N13 — No blank treatment status *(rewritten for the 3-field vocabulary — SR-6)*
Every case carries an explicit, verified **Field-I validity composite** plus **dual as-of
dates** (`as_of_content` + `as_of_treatment`); a composite is stamped only after a logged
derivation/check. `unverified ⚪` is the AI-native honest default for never-verified
records — it may exist in the data model but **never reaches a reader unbannered**.
- **Trigger:** any case asserted on any page or in the Case Index.
- **Check:** every case row/assertion carries a non-blank Field-I composite with both as-of
  dates; no `good_law` without a logged check; no unbannered `unverified` renders.
- **Enforcement:** `AUTO:LINT-6` (3-field + dual dates + glyph + unbannered-⚪) +
  `CHECKLIST:D3`.

### 2.C Standard rules — O1 set (SR-1…SR-5, carried)

#### SR-1 — Exhaustive live re-verification (USER DECISION)
Every asserted case is re-verified **live against the primary opinion** — **including
manifest-grade cases** — for proposition, every verbatim quote + pinpoint, and good-law
currency. No case is exempt by prior verification grade; prior manifests are a starting
reference, not a substitute for the live re-check. *(O2 realization: the S2 lake ingest IS
the live re-verification pass — every record is built from live CL reads through the
builder credential (L4′); S9 then verifies from the lake, barely touching live CL.)*
- **Trigger:** the S2 ingest + S9 exhaustive pass; any page authored/reformatted.
- **Check:** the assertion inventory shows a fresh live-CL-derived verdict for **every**
  case; the builder journal evidences the re-check; zero cases pass on manifest alone.
- **Enforcement:** `PROCESS` (S2 build + S9, per-credential serial lanes) + `CHECKLIST:D1`
  + audit (inventory completeness).

#### SR-2 — Instructor-grade framing gate (USER DECISION; blocking)
Citation accuracy is necessary but **not sufficient**. Every doctrine page must also pass an
instructor-grade gate: the rule/test is stated correctly and up front (N3); the doctrine is
**complete** (black-letter rule · elements/prongs · burden + who bears it · standard of
review · remedy · controlling authority + progeny by role · limits · nuances · pitfalls · the
operational "apply it" angle — the D4 checklist); and it **actually teaches** (D9). A page
with perfect cites but a muddled or incomplete brief **FAILS** and is escalated, not shipped.
- **Trigger:** every doctrine page at review/sign-off.
- **Check:** the page passes the composite gate **D2 ∧ D4 ∧ D9 ∧ D14**; the completeness
  checklist has no unlogged gap; a reviewer signs off teachability.
- **Enforcement:** `CHECKLIST` (composite, blocking).

#### SR-3 — STANDARDS.md supremacy (USER DECISION)
`docs/STANDARDS.md` is the single top-authority contract. It **absorbs**
`FINAL-QA-SPEC.md`'s §0 self-critique and the D1–D12 dimensions (now extended). On any
conflict, STANDARDS.md governs; `FINAL-QA-SPEC.md` is retained as historical reference with a
pointer header. Every later spec and the EXECUTE run obey it.
- **Trigger:** any cross-doc conflict or later-spec authoring.
- **Check:** STANDARDS.md exists and is cited as governing; `FINAL-QA-SPEC.md` carries the
  pointer header; no later spec contradicts STANDARDS.md.
- **Enforcement:** `PROCESS` + `CHECKLIST`.
- *(This rule is declared operatively in §0 above.)*

#### SR-4 — Enforcement model (USER DECISION)
Enforce **automated where cheap + reviewer checklist** for judgment. The automated lint
roster (§7) runs in CI, fail-closed, and gates publish; the reviewer checklist (the
D-dimensions) covers framing, completeness, pedagogy, placement, and Mermaid doctrinal
accuracy. A page ships only when **both** pass (or escalations are logged in
`_review-needed/`).
- **Trigger:** pre-publish and per-page review.
- **Check:** the lint roster is green; the reviewer checklist is signed; escalations are
  logged.
- **Enforcement:** `AUTO` (roster) + `CHECKLIST`.

#### SR-5 — Independent-replication concordance (build-time cross-verification)
Where conclusions already produced and verified by a **prior thread** (a prior research
manifest, a prior build, an independent reviewer) are re-derived by a **new pass**, the new
pass runs **conclusion-blind** to the prior result — forming and **recording its own
conclusions first** — and is then **reconciled** against the prior thread. **Concordance**
(same case set · holding/ratio · home-by-holding (N1) · role · treatment/good-law · split
call) raises the assertion to **double-verified** (a stronger grade than a single pass).
**Fundamental discordance** — any of those axes differ; cosmetic wording/ordering does
**not** count — **escalates** to the find→adjudicate→fix machine (§6), is **adjudicated
against primary authority** (per-credential serial lane, L4′), and the verdict must state
**what diverged** (prior wrong / new wrong / scope-or-framing shift) and **which conclusion
stands**. Independence is **conclusion-blind** (both threads may use the same primary
sources; the new thread must **not** be seeded with the prior thread's conclusions) and is
**enforced by orchestration** (freeze prior → run new with prior withheld → reconcile).
**No prior verified conclusion may be silently absent** from the reconciliation.
- **Trigger:** any pass that re-derives conclusions a prior verified thread already produced
  (the S2 lake vs O1 manifests; the S9 blind re-derivation vs the build).
- **Check:** the prior conclusion set was **frozen before** the new pass began; the new pass
  **recorded its conclusions before** reconciliation; every item carries a
  concordant/discordant disposition; fundamental discordances were adjudicated with
  primary-authority evidence + a logged verdict; no prior verified conclusion is silently
  dropped.
- **Enforcement:** `PROCESS` (orchestration: blind-then-reconcile) + `CHECKLIST:D1/D5` +
  `AUTO` (concordance diff where the conclusion sets are structured).

### 2.D Standard rules — O2 set (SR-6…SR-14, from the signed S1 spec R2–R14)

#### SR-6 — Three-field treatment vocabulary + dual as-of dating (replaces the single axis)
Treatment is the **3-field vocabulary** of §3.1 (Field I validity composite · Field II
per-edge treatment tag · Field III per-edge depth), each scoped to a point of law with an
as-of date; every record carries **dual dates** — `as_of_content` (content verified) and
`as_of_treatment` (treatment checked) — which **decay independently**. **A red flag is a
clue, not a verdict:** mark `superseded/not_current` only when a negative Field-II tag hits
the **specific point relied on** in a **binding jurisdiction**, never on color alone.
Reader-facing date placement = **data model + hover + the About page, NOT inline** on every
assertion. The old single-axis enum migrates **only** through the §3.2 mapping table.
- **Trigger:** any treatment value written or rendered (frontmatter, lake record, badge,
  hover); any case/entry created or re-verified; any reader-facing date rendered.
- **Check:** the single-axis status is gone post-projection; `⚪ unverified` never renders
  unbannered; both dates present in the schema; no inline date litter.
- **Enforcement:** `AUTO:LINT-6` (extended) + `AUTO:LINT-12/13` (lake drift/schema) +
  `CHECKLIST:D3/D7`.

#### SR-7 — The 10-gate per-proposition verification protocol
The professionalized two-key (§5A): KEY-1 substantiation **G1–G5** + KEY-2 validity
**G6–G10**, PASS/FAIL/FLAG per gate; a proposition is VERIFIED only when all applicable
gates pass; an independent reviewer re-verifies **≥1 in 10** (escalate on any error found);
two-person rule for anything tagged negative.
- **Trigger:** any legal proposition authored or materially edited.
- **Check:** one tracked row per proposition-source pair with per-gate results; the
  ≥1-in-10 re-verify is logged; no VERIFIED with an open FAIL/FLAG.
- **Enforcement:** `CHECKLIST:D1` + `PROCESS` (S9 pipeline; ledger rows).

#### SR-8 — AI-verification guardrails (fail-closed, first-class)
The ten guardrails of §5B (retrieval-grounded only; no proposition without a verified
pincite; citation-existence fail-closed; quote string-match; holding-support; treatment/
currency before publish; generator ≠ verifier; human sign-off at the enumerated pauses;
immutable provenance; dual-date re-verification). Each maps to a concrete enforcement point
— the §5B enforcement-map table is normative.
- **Trigger:** any AI-generated legal content entering the pipeline.
- **Check:** the §5B table's 10 rows each name ≥1 concrete enforcement point; every gate
  fires where its trigger condition occurs; no bare-"PROCESS" row.
- **Enforcement:** per the §5B table (`AUTO` + `CHECKLIST` + named pipeline gates).

#### SR-9 — Graded-authority entry model = Variant A; officer-BLUF banned project-wide
Every doctrine page = **Black-letter rule** (the only thing published *as* the law;
≥2 independent reviewers) → **Explanation** (the verified teaching brief) → **Authorities &
notes** (attributed, lighter) — the §8.1 template. **The field-application /
"officer bottom line" / BLUF summary is BANNED project-wide:** it is a human-in-the-loop
artifact and a paraphrase-drift risk; do not design, mock, or generate it. The reader gets
the verified rule + brief and applies it. Existing field-framing prose migrates by the
convert-or-delete content test (S7).
- **Trigger:** any doctrine page created or restructured.
- **Check:** the §8.1 template is followed; the rule layer is a distinct, separately-gated
  object; no auto-generated officer-bottom-line anywhere.
- **Enforcement:** `CHECKLIST:D10/D14` + `AUTO:LINT-15` (skeleton, S5) + review sweep.

#### SR-10 — Reviewer panel + machine ledger
Legal assertions are reviewed by an adversarial panel — **1 Claude lane + 2 independent
Codex lanes** — with a real **≥2-of-3 refute tally** (votes recorded blind, before mutual
disclosure); findings → votes → adjudications → fixes → inventory are **machine-emitted and
reconcilable** (JSON-lines ledger per `_overhaul2/s9-demo/LEDGER-SCHEMA.md`), so the audit
itself can be audited. Writer ≠ checker invariants (lane identity, no self-closing) are
machine-checked by a script, not an agent.
- **Trigger:** any legal-assertion review cycle (S9).
- **Check:** every paneled finding has all three lane votes; ≥2-refuted findings are never
  UPHELD-as-framed; lane-identity invariants hold across the ledger; counts reconcile.
- **Enforcement:** `PROCESS` (S9 implements) + `AUTO:LINT-30` (ledger reconciliation).

#### SR-11 — Pipeline-vocabulary ban (reader-facing prose is civilian)
No **editorial-pipeline vocabulary** in reader-facing prose, site-wide. The five banned
classes (each grep-able; full pattern table in §7.3): (1) rule/spec/lint identifiers;
(2) provenance / re-homing notes ("Re-homed from…"); (3) pipeline status markers
("CL-confirm pending", "TODO"); (4) editorial meta-labels ("(woven in)", "No standalone
case page"); (5) internal artifact names ("data lake", "frontmatter", "lint" as our
artifacts). Where such state must persist, it moves to an **HTML comment or frontmatter
key** — never rendered prose. The About page is the one sanctioned place the methodology may
be described (allowlisted).
- **Trigger:** any commit touching `content/`.
- **Check:** the five pattern classes grep to **0 hits** over rendered prose (source minus
  frontmatter, HTML comments, code fences), modulo the committed allowlist; class 5's
  generic terms are a grep-assisted review sweep (judgment).
- **Enforcement:** `AUTO:LINT-11` (classes 1–5a, fail-closed; S9 builds) +
  `CHECKLIST:D10` (class 5b + allowlist adjudication).

#### SR-12 — Slip-op pinpoints only for the current Supreme Court term
A slip-opinion pinpoint (`slip op. at N`) is legal **only** for cases from the current
SCOTUS term (no reporter pagination exists yet). Any older case cites a **reporter
pinpoint**. Conversion of legacy slip-op cites is S7 work (four-tier method); this rule
guards the steady state.
- **Trigger:** any pinpoint cite authored or edited.
- **Check:** `slip op.` appears only on pages whose case `date_decided` (from the S2 lake)
  is within the current term.
- **Enforcement:** `AUTO:LINT-3` (extended, lake-driven) + `CHECKLIST:D7`.

#### SR-13 — Voice, em-dash policy, and paragraph density (the Humanizer subset)
The voice pass applies to **explanation prose ONLY**, per the ADOPT/ADAPT/REJECT table in
`docs/STYLE.md` §3. **Em-dashes:** cut the habit in prose — budget **≤1 em-dash per block
(paragraph or list item), never 2+ in one sentence**; direct quotations and controlled
labels are exempt (excluded from counts); **en-dashes in citation/page/date ranges are
correct and kept** ("392 U.S. 1, 21–22" — a style rule, not a lint exemption: LINT-10
targets U+2014 only and never sees an en-dash). Hard carve-outs — the voice pass NEVER
applies: inside a quoted opinion; on a black-letter rule/holding/standard; on
citations/case names; on controlled labels. **Paragraph density (the Brief):** one
doctrinal move per paragraph; ~5-sentence soft cap; any paragraph invoking **more than 3
cases** converts to labeled bullets (bolded case name + one-line role).
- **Trigger:** any voice pass over explanation prose; any commit touching explanation
  prose; any Explanation-layer prose authored or edited.
- **Check:** LINT-10 enforces the em-dash budget fail-closed over explanation prose (unit =
  block; quotations + controlled labels masked; self-tested against
  `scripts/lint/fixtures/lint-10.md`); the >3-cases-per-paragraph check is fail-closed
  (wikilink density is mechanically countable); one-move-per-paragraph + the 5-sentence cap
  are advisory.
- **Enforcement:** `AUTO:LINT-10` + `AUTO:LINT-3` (>3-case stacking) + `CHECKLIST:D9`.

#### SR-14 — Term register + single-source transclusion
`scripts/lint/term-register.yml` is the **machine-readable** controlled word list (canonical
spelling/definition per term of art; `docs/STYLE.md` §4 references it — never duplicates
it). Each rule/term is stated **once** as a canonical node (block-ref-anchored) and
**transcluded**, never re-paraphrased — copies drift. Term-of-art consistency: never drift
*stop → detention → seizure*; repeat the exact term (synonym-cycling is banned by the voice
table).
- **Trigger:** any term of art used; any rule prose authored.
- **Check:** (a) LINT-7 (extended) consumes the register directly and fails banned variant
  spellings; (b) canonical rule nodes carry block-ref anchors, and the **duplicate-prose
  shingle detector** (≥25 overlapping tokens between rule-layer blocks in different files,
  transclusion embeds excluded) fails CI.
- **Enforcement:** `AUTO:LINT-7` (extended) + `AUTO:LINT-29` (shingle detector, S9 builds) +
  `CHECKLIST:D5`.

---

## 3. The authority-weight lexicon (mandatory vocabulary)

These six tiers are the **only** permitted authority labels site-wide. The blunt phrase
**"persuasive, not binding" is BANNED.**

### 3.0 The exact allowlist *(S1 A8 — normative; spaced em-dash ` — ` forms only)*

| # | Exact label string | Meaning |
|---|---|---|
| 1 | `Binding — SCOTUS` | Nationwide binding authority. |
| 2 | `Binding in-circuit — <circuit>` | A circuit holding, within its own circuit (circuit suffix **mandatory**). |
| 3 | `Persuasive (outside circuit) — <circuit>` | Replaces the banned "persuasive, not binding" (suffix **mandatory**). |
| 4 | `Persuasive — state, illustrative` | Paired with the federal rule. |
| 5 | `Persuasive only — non-precedential` | Unpublished; the only "not binding even at home" tier. |
| 6 | `Historical` | English/colonial origins; or overruled cases shown as history. |

`<circuit>` matches `(1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|D.C.|Fed.) Cir.`

**Label order is canonical: tier word first, qualifier after the em-dash.** The inverted
form ("SCOTUS — binding") is **forbidden**. LINT-4 validates every weight label against
this allowlist **exactly** — inversions, unspaced dashes, en-dash or hyphen in place of the
em-dash, case variants, and a missing mandatory circuit suffix all fail. Genuine splits are
flagged. Enforced by `AUTO:LINT-4` + `CHECKLIST:D6` (N2).

### 3.1 The three-field treatment vocabulary *(SR-6 — replaces the single `treatment.status` axis)*

Authority-weight is **separate from** good-law currency. Treatment is modeled on
Shepard's / KeyCite / BCite as **three orthogonal fields + as-of dates**. CourtListener
provides **none** of this natively — it is **derived** from progeny opinion text + web
search, through the S2 three-lane derivation.

**Field I — Validity status** (one composite per case, scoped to a point of law; the
composite reflects the **principal holding**, with `point_overrides[]` for divergent
points and `varies_by_point` flagging split-treatment cases):

```
field_i_validity ∈ { good_law 🟢 | history 🔵 | caution 🟡 | questioned 🟠 |
                     superseded 🔴 | unverified ⚪ }
```

*Naming (two layers, one vocabulary):* the tokens above are the **machine enum** — exactly what
the lake records and projected frontmatter store, per the S2 record schema (S2 R5), and what
LINT-6 validates. The **full composite names** from PRACTICES §2 — `history/neutral`,
`questioned/overruling_risk`, `superseded/not_current` — are the same values' display/
documentation composites (the slash reads "aka"); they may appear in prose and reader-facing
explanations but never as stored values.

- `good_law` 🟢 — no material negative treatment on the taught points.
- `history` 🔵 — neutral/historical significance (e.g. superseded framework kept as history).
- `caution` 🟡 — materially limited/criticized on some point; read the overrides.
- `questioned` 🟠 — overruling risk: negative treatment hits a relied-on point in a binding
  jurisdiction.
- `superseded` 🔴 — not current law on its principal holding (overruled / abrogated /
  superseded by statute); rendered as **history** (tier 6), never disguised, never deleted,
  with a forward-pointer to the successor authority.
- `unverified` ⚪ — **AI-native honest default** for records never verified; **never reaches
  a reader unbannered**. The glyph is **⚪ U+26AA everywhere; U+2B58 is forbidden**
  (LINT-6 treats it as an invalid glyph).

**Field II — Treatment tag** (per material citing edge): `overruled` · `abrogated` ·
`superseded_by_statute` · `limited` · `distinguished` · `criticized` · `questioned` ·
`modified` · `followed` · `explained` · `reaffirmed` · `expanded`.

**Field III — Depth** (per material citing edge): `examined` · `discussed` · `cited` ·
`mentioned` · `quoted`. (No KeyCite stars on the free stack — approximate by discussion
length.)

**Dual as-of dates:** every record carries `as_of_content` (content verified against the
primary opinion) and `as_of_treatment` (treatment last checked). They **decay
independently**. Reader-facing placement: **data model + hover + About page — never inline
litter.**

**Rules:** a red flag is a **clue** — mark `superseded` only when a negative Field-II tag
hits the **specific point relied on** in a **binding jurisdiction**, never on color alone.
Every case gets one Field-I + dates; every material citing edge gets a Field-II +
Field-III. An overruled case is shown under **tier 6 (Historical)** and carries its
Field-I everywhere it appears (D5).

### 3.2 Old→new migration mapping *(S1 A4 — the ONLY sanctioned translation)*

Old single-axis lexicon: `docs/STANDARDS.md` (O1) §3.1: `good | criticized | limited |
abrogated | overruled`. Live frontmatter (457 case pages, counted 2026-07-02): 439 `good` ·
11 `limited` · 5 `overruled` · 2 `abrogated` · 0 `criticized`.

| Old `treatment.status` | Count | New Field-I composite (machine token) | Edge / override handling |
|---|---|---|---|
| `good` | 439 | `good_law` 🟢 | No edge required; old `as_of` seeds `as_of_treatment`; the S2 derivation re-derives and may downgrade |
| `limited` | 11 | `caution` 🟡 | **Mandatory ≥1 `point_overrides[]`** on the limited point; override Field-II = `limited` (or `superseded` where replaced outright — *Belton*→*Gant*); `varies_by_point: true` |
| `overruled` | 5 | `superseded` 🔴 (composite name: `superseded/not_current`) | Field-II `overruled` edge to the overruling case; authority-weight moves to tier 6 (Historical) |
| `abrogated` | 2 | `superseded` 🔴 (composite name: `superseded/not_current`) | Field-II `abrogated` edge (*Aguilar*/*Spinelli* → *Illinois v. Gates*) |
| `criticized` | 0 | `caution` 🟡 (default) | Escalate to `questioned` 🟠 (`questioned/overruling_risk`) only when the negative treatment hits the **relied-on point** in a **binding jurisdiction** |

The 11 `limited`: *Boyd, Coolidge, Escobedo, Mathis (1968), Monroe v. Pape, Belton, Elstad,
Saucier, Thornton, Agurs, Chadwick*. The 5 `overruled`: *Gouled, Jones (1960), Michigan v.
Jackson, Olmstead, Wolf*. The 2 `abrogated`: *Aguilar, Spinelli*.

**Point-level override rule:** a case bad on **fewer than all** taught points gets a
composite reflecting its **principal holding** plus `point_overrides[]` for the divergent
points; if the principal holding itself is the dead point, the composite is `superseded`.
**No migrated case maps to `unverified` ⚪** — ⚪ is reserved for records never verified
(frontier stubs); the 457 keep their seeded value + O1 `as_of` until the S2 derivation
re-stamps them. The S2 projector consumes this table to seed Field-I; the three-lane
derivation then confirms or adjusts; **the mapping alone never yields `verified`.**

---

## 4. The check dimensions (D1–D14)

The D1–D12 reviewer framework is **carried**; three dimensions are **extended**; two
dimensions (**D13, D14**) were **added** in O1 and are carried. Each dimension maps to the
rules it enforces; every rule maps to ≥1 dimension or PROCESS lane (the **no-orphan
invariant**).

### 4.1 The rule → dimension mapping

| Dim | Name | Status | Rules it enforces |
|---|---|---|---|
| D1 | Accuracy / two-key (exhaustive) | extended → exhaustive-live (SR-1) + 10-gate (SR-7) | L1, L2, L6, L8, SR-1, SR-5, SR-7, SR-8 |
| D2 | Framing | carried | N1, N6, N10, L7, L8 |
| D3 | Shepardize + new frontier | extended (SR-6 3-field) | N4, N13, L2, SR-6 |
| D4 | Completeness | carried | N3, N9, N10, N12, SR-2, L7, L8 |
| D5 | Internal consistency & cross-page coherence | extended (SR-14 transclusion) | N1, N4, N6, SR-5, SR-14 |
| D6 | Guardrails | extended (N2 exact allowlist) | N2 + fed/state, apocryphal trio, mnemonics, no inline flashcards |
| D7 | Citation hygiene | extended (SR-12 slip-op) | L3, L1 (quote/pinpoint), SR-12 |
| D8 | Visual accuracy (Mermaid) | carried | (render + doctrinal faithfulness) |
| D9 | Pedagogy / teachability | extended (SR-13 voice/density) | N9, SR-2, L8, SR-13 |
| D10 | Structure / spec compliance | extended (SR-11 vocab ban) | N5, N8, SR-9, SR-11 |
| D11 | Practical/reference/history pages | carried | N11 (glossary accuracy) + guardrails |
| D12 | Deck ↔ page ↔ index integrity | carried | L1 (decks derive from pages) |
| D13 | Linking & glossary wiring | carried | N7, N11 |
| D14 | Brief-first architecture & teachability-up-front | carried | N3, N8, N9, SR-9 |

Process-lane rules (no dedicated dimension, enforced by orchestration discipline and audit):
**L4′** (per-credential serial lanes — journal/log audit), **L5** (find→adjudicate→fix trail
audit), **SR-3** (supremacy — cross-doc audit), **SR-4** (enforcement model — roster +
checklist audit), **SR-10** (panel + ledger — reconciliation script). Every rule therefore
maps to at least one dimension **or** a PROCESS lane; no rule is orphaned, and every
dimension carries at least one rule.

### 4.2 The extended dimensions (acceptance lines)

- **D1 — Accuracy / two-key (exhaustive-live + 10-gate).** Every asserted case, holding,
  fact, quote, and pinpoint traces to the opinion through the G1–G10 protocol (§5A); under
  SR-1 every case is verified **live** (the S2 ingest), not on a prior manifest.
  *Acceptance:* every assertion in the inventory has a per-gate verdict; zero unverified
  legal claims asserted as settled.
- **D3 — Shepardize + new frontier (extended: SR-6).** Validity through the 3-field
  vocabulary: Field-I composite + overrides recorded; material citing edges tagged
  (Field-II/III); genuine splits/restrictions/frontiers surfaced and labeled; dual as-of
  dates present. *Acceptance:* current Field-I recorded for every case; treatment
  consistent everywhere the case appears; nothing stale asserted as current.
- **D5 — Internal consistency (extended: SR-14).** Shared cases framed and treated
  consistently; canonical rule/term nodes transcluded, never re-paraphrased; no duplicate
  rule prose. *Acceptance:* no contradictions; shingle detector clean; overruled cases shown
  as history everywhere.
- **D6 — Guardrails (extended: exact allowlist).** Every authority label string-matches the
  §3.0 allowlist; no banned phrasing; no inverted labels; no apocryphal trio; mnemonics
  verbatim + uncited; no inline flashcards. *Acceptance:* fed/state never blurred;
  allowlist-clean; guardrail-clean.
- **D7 — Citation hygiene (extended: SR-12).** Bluebook consistency; pinpoint present
  wherever a quote appears; every CL URL resolves and shows the named case; slip-op
  pinpoints only for the current term. *Acceptance:* no stale slip-op cites; zero broken CL
  links.
- **D9 — Pedagogy (extended: SR-13).** Rule-first clarity, the "why," operational
  application, instructor voice, digestible — under the voice table and density budgets.
  *Acceptance:* teaches; no case-wall paragraphs; voice-table-clean.
- **D10 — Structure (extended: SR-11).** Template sections present + ordered; frontmatter
  correct; in the MOC; zero pipeline vocabulary in rendered prose. *Acceptance:*
  structure-clean; vocab-ban-clean modulo the allowlist.

### 4.3 The carried dimensions (reference)

- **D2 — Framing.** Each case framed correctly *for the doctrine of THIS page*; nuances and
  pitfalls explained, not just named.
- **D4 — Completeness.** Full per-doctrine checklist: black-letter rule · elements/prongs ·
  burden + who bears it · standard of review · remedy · controlling authority + progeny by
  role · limits · nuances · pitfalls · lower-court developments · cross-links · the
  operational "apply it" angle.
- **D8 — Visual accuracy (Mermaid).** Render every diagram and visually inspect; every
  node/branch matches the page's stated rule.
- **D11 — Practical/reference/history pages.** The non-case pages: mnemonics verbatim,
  glossary accurate, court-system/research facts correct, history framed as history, no rot.
- **D12 — Deck ↔ page ↔ index integrity.** No orphaned deck cards; card `page`/`source`
  valid; Case Index regenerated and correct; decks derive from verified pages.
- **D13 — Linking & glossary wiring.** Every named case links to its case page; passage
  discussions deep-link to the pinpoint span; non-vernacular terms link to the glossary;
  all link targets resolve. *Acceptance:* no bare case name; no orphan glossary term;
  deep-links point to the correct span; zero broken wikilinks.
- **D14 — Brief-first architecture & teachability-up-front.** The integrated teaching brief
  reads top-to-bottom and self-contained as the first content; named tests/prongs appear up
  front; tables and the frontier section follow as apparatus. *Acceptance:* brief-first
  order holds on every doctrine page; tests are stated, not reconstructed.

---

## 5. The research discipline (N12 — progressive, bounded)

For each page, **seed = the captured cases plus the controlling foundational SCOTUS authority
the doctrine rests on**, added even if uncaptured (*Chimel* for SITA, *Schneckloth* for
consent). Then expand progressively through at most three hops:

- **Hop 0 (seed):** the proposition the capture/page states.
- **Hop 1 (doctrine/keyword):** the named test, its elements, the controlling authority +
  significant progeny by role.
- **Hop 2 (frontier):** circuit splits, recent developments, weak-but-overused field cases
  officers rely on, issues of first impression.

**Recursion bound:** at most **2 expansion hops beyond the seed** per page.

**Division of labor — web discovers, CL confirms:** web search (free, parallel)
**discovers** candidates — terminology, legal theories, adjacent keywords that reframe the
search; the **per-credential serial CL lane** (L4′) **confirms** existence + proposition +
verbatim quote before anything is asserted (L2).

**Stop conditions (any one ends the research for a page):**
1. the D4 completeness checklist for the doctrine is fully covered;
2. a full hop surfaces no new load-bearing authority;
3. the page would exceed the ½–1-page digestible budget — then cut to load-bearing authority
   only.

**Saturation (corpus-level, from the comprehensive-research protocol):** STOP only when all
true — new searches surface only cases already seen · the core authorities cite back to
each other · both directions run on every key case · every circuit accounted for (or a
split flagged) · no unaddressed "first impression" language in the newest cases · a 2nd
tool cross-checked · adverse/limiting authority captured (anti-cherry-pick) · further
reading adds nothing.

**Case identification (L6):** misspelling-tolerant — never declare a case fake from one
miss; run the escalation ladder (reporter cite → name/phonetic variants → proposition
full-text → web → re-locate in CL). The **cluster-id ≠ opinion-id (L3)** guard applies on
every read.

**Scope claims (L7) — frontier mandate:** any boundary on a doctrine's reach — and especially
a *negative* one ("only X" / "does not reach Y") — is treated as an assertion: the **Hop-2
frontier pass is mandatory** (circuit/state treatment, splits, first-impression) **plus**
primary confirmation before the boundary may appear. Until then the page records the scope as
**"unresolved — research,"** never the narrow reading.

---

## 5A. The 10-gate per-proposition verification protocol (SR-7)

A hybrid of the law-review cite-check (forward substantiation) + the citator check
(backward validity). Record **PASS / FAIL / FLAG per gate**; a proposition is VERIFIED only
when all applicable gates pass.

**KEY 1 — Substantiation:**
- **G1 — existence.** Locate the exact authority (identity confirmed per L3/L6).
- **G2 — support.** The source *actually stands for* the proposition; the
  signal/parenthetical matches. **Support is checked per enumeration item** — one citation
  does not vouch for a conjoined list's other items.
- **G3 — quote fidelity.** Verbatim string-match against source text.
- **G4 — pincite.** The language is on the cited page.
- **G5 — form.** Bluebook/house-style complete.

**KEY 2 — Validity:**
- **G6 — direct history.** Not reversed/vacated/superseded in its own line.
- **G7 — citator/derived status recorded.** The derived Field-I/II/III record exists.
- **G8 — on-point treatment.** Read the negative progeny; does it strike *this* point?
- **G9 — jurisdiction + validated-through date** stated.
- **G10 — independent corroboration.** Cross-check a 2nd source for load-bearing
  propositions.

**Governance:** one tracked row per proposition-source pair; an independent reviewer
re-verifies **≥1 in 10** (escalate on any error found); **two-person rule** for anything
tagged negative; preserve links. Enforced through the S9 ledger (SR-10) + `CHECKLIST:D1`.

---

## 5B. The AI-verification guardrails (SR-8 — fail-closed, first-class)

We are the AI courts sanction people for trusting (1,300+ documented sanction matters;
*Mata v. Avianca* → precedential 9th-Cir. *LNU v. Blanche*; even RAG tools hallucinate
17–33% — Stanford RegLab). Grounding is necessary, **not sufficient**. These are enforced,
not advisory. **The enforcement map is normative — no guardrail rests on bare "PROCESS":**

| # | Guardrail | Concrete enforcement point(s) |
|---|---|---|
| AI-G1 | **Retrieval-grounded only** over vetted primary sources — never parametric recall / open web | S2 lake per-field `provenance` (schema-enforced — `AUTO:LINT-13`); `CHECKLIST:D1` |
| AI-G2 | **No legal proposition without a verified primary-source pincite** + parenthetical | Gate G4 (§5A) per proposition; `AUTO:LINT-2`; publish blocked on FAIL |
| AI-G3 | **Citation-existence check, fail-closed**: "not found" → **block + investigate** (L6 ladder), never auto-delete; name/cite mismatch → presumptively fabricated (compare input name vs CL canonical ourselves) | Gate G1 (§5A); `AUTO:LINT-1` (identity); S2 two-key identity (`verified` requires citation match + party-name-in-text); `CHECKLIST:D1` |
| AI-G4 | **Quote-fidelity string-match** against retrieved source text | Gate G3 (§5A); `AUTO:LINT-2`; S2 pinpoint verification vs cached text |
| AI-G5 | **Holding-support check** — the cited page supports the proposition (2nd pass, per enumeration item) | Gate G2 (§5A); panel dimension `CHECKLIST:D1/D2` |
| AI-G6 | **Treatment/currency check before publish** — overruled/abrogated never presented as current | Gates G6–G8 (§5A); `AUTO:LINT-6` (3-field) + `AUTO:LINT-26` (good-law target); `CHECKLIST:D3` |
| AI-G7 | **Generator ≠ verifier** — no self-certification, ever | Ledger lane-identity invariants, machine-checked (`AUTO:LINT-30`); L5 role separation; SR-10 panel |
| AI-G8 | **Human sign-off** for anything reader-facing/legally operative — scoped to the RUNBOOK §0 enumerated-pause register (publish go-ahead · fabrication removals · borderline relevance · release gate · scope-guard pauses) | The §0 register (named pipeline gate); release-gate `CHECKLIST` (composite) |
| AI-G9 | **Immutable provenance/audit trail** per assertion (model+version, retrieved sources, timestamp, verification results, verifier identity) | S2 `provenance` blocks (`AUTO:LINT-13`) + ledger rows with `{lane, model}` (`AUTO:LINT-30`) |
| AI-G10 | **Dual as-of dating + re-verification cadence** — re-run G3/G4/G6 on a schedule | `AUTO:LINT-6` (dual dates present); maintenance-loop handoff artifacts (S9 → GH#2); `CHECKLIST:D3` |

---

## 6. The find → adjudicate → fix machine (L5/L4′) + the reviewer panel (SR-10)

The standing verification machine, governed by STANDARDS.md. Three separated roles; a legal
assertion never changes on a reviewer's opinion alone.

1. **REVIEW** (parallel, free, **NO CL**). Per page, dimensional reviewers emit structured
   findings:
   `{id, page, dimension(D1–D14), locator(section + verbatim text), problem, severity(high|med|low), proposed_fix, needs_cl, confidence}`.
   **Reviewers may not edit pages.** They surface, they don't decide. Reviewer lanes run
   read-only; input manifests are journaled (writer ≠ checker, machine-auditable).

2. **PANEL (legal assertions + the rule layer).** An adversarial panel — **1 Claude lane +
   2 independent Codex lanes** — votes on each paneled finding: verdict ∈ {refuted, stands,
   stands-modified}, votes recorded **blind** (before mutual disclosure). **≥2-of-3 refute
   kills the finding as framed** (it may only be DISMISSED, MODIFIED, or ESCALATED — never
   plain UPHELD).

3. **ADJUDICATE.** Every finding → a verdict in the set
   **{UPHELD, MODIFIED, DISMISSED, ESCALATE}** with `adjudicated_fix` + `evidence`.
   - `needs_cl=true` findings (good-law, proposition, quote/pinpoint, case existence,
     CL-URL, new-frontier) → adjudicated with **lake/CL/web evidence** through the
     appropriate credential lane (L4′); **no CL-grade evidence → cannot UPHOLD a change to
     a legal assertion** (→ DISMISS or ESCALATE).
   - Non-legal findings (formatting, structure, missing cross-link, internal contradiction,
     pedagogy, corpus-supported completeness gap) → a free editor-adjudicator.
   - **DISMISSED findings are logged with the reason** (a dismissed false-positive is a
     successful outcome — it guards against over-correction).

4. **FIX** (parallel, free). Per page, a fixer applies **only** UPHELD/MODIFIED adjudicated
   fixes, verbatim from the adjudication; **ESCALATE → `_review-needed/`**. The fixer
   introduces no new content of its own. **Post-fix re-review is performed by a lane that
   did not write the fix.**

**The machine ledger (SR-10):** findings → votes → adjudications → fixes → inventory are
machine-emitted JSON-lines rows (schema: `_overhaul2/s9-demo/LEDGER-SCHEMA.md`), joined by
`assertion_id`, every row carrying lane identity + exact model id. A **script — not an
agent — checks the reconciliation invariants in CI** (every finding adjudicated; tallies
complete; lane-identity separations hold; counts reconcile; every DISMISSED carries a
reason). `AUTO:LINT-30`.

**Loop cap 3**, then escalate to `_review-needed/<slug>.md` with the open issue. **Checkpoint
the ledger after every sub-phase** (resumable). Surface consequential calls in the final
report.

---

## 7. The enforcement model (SR-4 — automated where cheap + reviewer checklist)

A page ships only when **both** gates pass (or escalations are logged in `_review-needed/`):
(1) the automated lint roster is green, **and** (2) the D1–D14 reviewer checklist is signed.

### 7.1 Automated lint roster (deterministic)

Runs in CI, fail-closed, and gates publish. **Numeric `LINT-<n>` ids are canonical (S1 A5);
descriptive aliases are permitted on first mention; `LINT-S2-*` / `LINT-S3-*` / `LINT-S4-*`
names survive only as deprecated aliases.** The CL-touching lint (LINT-1) runs only through
its assigned credential lane (L4′). Rows 1–14 are defined here; **the full 1–30 roster —
including the S3/S5/S6/S8 sets — is codified fail-closed at S9 (S9 R8 is THE roster), every
row with committed pass/fail fixtures.**

| Lint | What it checks | Enforces |
|---|---|---|
| **LINT-1** | Every CL URL resolves (200) **and** returned text contains the named case; runs at the serial gate on the builder credential, with the ≥1-in-10 judgment slice on the Claude lane | L3, D7 |
| **LINT-2** | Every block/inline quote has an accompanying pinpoint cite (else de-quote/pin) | L1, D7 |
| **LINT-3** | Structure (extended, lake-driven — *rebuild lands at S9 per the F-DEMO-001 adjudication*): section order; brief-first first-H2; apply-it ordered lists; **no SCOTUS case in the frontier section** (court from the lake); slip-op current-term-only; >3-cases-per-paragraph hard flag; single controlling amendment in frontmatter | N3, N5, N8, SR-12, SR-13, D10 |
| **LINT-4** | Every authority label validated **exactly** against the §3.0 allowlist (spacing, order, circuit suffix); banned "persuasive, not binding"; inverted labels | N2, D6 |
| **LINT-5** | Every named case resolves to a case-page wikilink (no bare case names); **fail-closed wikilink/anchor resolve** (dead link or broken anchor blocks publish) | N7, D13 |
| **LINT-6** | 3-field treatment + dual as-of dates; legacy single-axis gone post-projection; U+2B58 forbidden; ⚪ `unverified` never unbannered | N13, SR-6, D3 |
| **LINT-7** | Term-register enforcement (consumes `scripts/lint/term-register.yml`: banned variants fail) + glossary wiring (best-effort half) | N11, SR-14, D13 |
| **LINT-8** | Guardrails: no apocryphal Holiday/McCall/Smith trio; mnemonics verbatim + uncited (wikilink-target checks: the linked register entry must exist and match); no inline `## Flashcards` | D6, D11 |
| **LINT-9** | **Carat-leak (`^pin-N`)**: block-ref anchors must never render as visible text — zero mid-line block anchors; zero broken pin links | L1, D7, D13 |
| **LINT-10** | **Prose em-dash budget** (unit = block: paragraph or list item; >1/block or 2+/sentence fails; direct quotations + controlled labels exempt; self-tested against `fixtures/lint-10.md`) | SR-13, D9 |
| **LINT-11** | **Pipeline-vocab ban** (the §7.3 five-class pattern table; rendered-prose scope; About-page allowlist; committed exclusion list) — *S9 builds* | SR-11, D10 |
| **LINT-12** | **Lake↔frontmatter drift** (two-directional, value-level deep-equal; managed fields only) — *lands with S2* (alias: `LINT-S2-drift`) | SR-6, D3 |
| **LINT-13** | **Lake schema** (every record validates against `lake/_schema.json`) — *lands with S2* (alias: `LINT-S2-schema`) | SR-8/AI-G1, D1 |
| **LINT-14** | **Page↔record publish gate** (every `type: case` page resolves to a `verified`/`under_review` lake record before publish) — *lands with S2* (alias: `LINT-S2-pagerecord`) | SR-6, D1 |

### 7.2 Reviewer checklist (judgment — the D-dimensions)

The reviewer checklist covers what scripts cannot decide: framing correctness (D2),
placement-by-holding (N1/D2), completeness vs the D4 checklist (D4), cross-page coherence
(D5), Mermaid doctrinal accuracy (D8), pedagogy/teachability (D9), brief-first architecture
(D14), and the **SR-2 instructor-grade composite gate (D2 ∧ D4 ∧ D9 ∧ D14, blocking)**.

**Both required pre-ship.** A page ships only when the roster is green **and** the checklist
is signed (or escalations are logged in `_review-needed/`).

### 7.3 The pipeline-vocabulary pattern table (SR-11 / LINT-11 — normative)

All rows run over **rendered prose only** — frontmatter, HTML comments, code fences, and the
About-page allowlist are excluded before matching:

| Class | Pattern family (`grep -E`) | Enforcing check | Fail mode |
|---|---|---|---|
| 1 — identifiers | `\bLINT(-S2)?-[0-9]+\b` · `\b[LNRG][0-9]{1,2}\b` · `\bSR-[0-9]\b` · `\bD-?[0-9]{1,2}\b` · `\bS[1-9]\b`, run with a committed exclusion list (`S\. Ct\.`, §-numbered statutes, docket formats) | `AUTO:LINT-11` fail-closed; a flagged hit clears only via the committed allowlist file, each entry adjudicated under `CHECKLIST:D10` | CI red on any un-allowlisted hit |
| 2 — provenance notes | case-insensitive `\b(re-homed\|moved\|merged\|split\|migrated) from\b` | `AUTO:LINT-11` fail-closed | CI red |
| 3 — status markers | `CL-confirm pending` · `pending CL` · `annotate-only` · `deferred to EXECUTE` · `pending verification` · `\bTODO\b` · `\bTBD\b` · `\bFIXME\b` | `AUTO:LINT-11` fail-closed | CI red |
| 4 — meta-labels | `\(woven in\)` · `No standalone case page` · `placeholder` · `this page intentionally` | `AUTO:LINT-11` fail-closed | CI red |
| 5a — concrete artifact names | `cl-calls\.log` · `S6-SEED` · `RUNBOOK` · `PRACTICES` · `STANDARDS\.md` · `STYLE\.md` · `\.spec\.md` · `\bwrapper\b` | `AUTO:LINT-11` fail-closed | CI red |
| 5b — generic pipeline terms ("data lake", "frontmatter", "lint" used as **our** artifacts) | the words grep, but the disqualifying **intent** is judgment-only | **`CHECKLIST:D10`**: a grep-assisted review sweep, adjudicated by a reviewer | review finding, not CI |

---

## 8. Canonical template tables of contents

### 8.1 Graded-authority doctrine page — Variant A (SR-9 + N8) — section order

Every doctrine page is the **three-layer graded-authority model**, gated per layer:

- **Layer 1 — Black-letter rule.** The doctrinal statement — the *only* thing published
  *as* "the law." Requires **≥2 independent reviewer approvals** (the SR-10 panel). Stated
  once as the canonical node (block-ref-anchored; registry mirrors transclude it — SR-14);
  named tests/prongs up front (N3).
- **Layer 2 — Explanation (the Brief).** The verified teaching brief: nuances, limits,
  pitfalls integrated; brief-first (N8); voice + density per SR-13.
- **Layer 3 — Authorities & notes.** Attributed, lighter-weight; the supporting cases +
  our evaluation.

**There is NO fourth layer.** The field-application / officer-bottom-line / BLUF summary is
banned project-wide (SR-9).

Concrete section order (the S5 entry model realizes this template):

1. **Frontmatter** — projector-managed fields (lake projection) + preserved fields; single
   controlling amendment; aliases (renamed pages); `related:`.
2. **Field-decisive question** (framing guidance, N9 — where it helps) → **`[!rule]`
   black-letter callout** (Layer 1 — the canonical statement site) → **The Brief**
   (Layer 2 — integrated, self-contained, closing `**Common pitfalls.**` bullets).
3. **Lower-court developments** — role-based frontier section, ABOVE the tables
   (circuit/state expand/narrow/split/first-impression; **no SCOTUS** — N5).
4. **Key cases** — sanctioned table schema (S5): `Case | Holding | Opinion`; weight +
   Field-I pill injected **under the case name** from the data model (cells never author
   weight/treatment/dates); non-exclusive key-status (N6); placement-by-holding (N1).
5. **Related cases across doctrines** — `Case | Relevance here | Primary home | Opinion`;
   framed for THIS page's doctrine.
6. **Visual (Mermaid)** — where a multi-factor/branching test exists.
7. **Sources** — bracketed-link format (Layer 3).

*Cross-cutting on every doctrine page:* link every named case (N7); treatment carried
structurally + woven into holdings (N4); glossary-wired terms (N11); exact-allowlist
authority labels (N2); two-key / 10-gate (L1/SR-7).

### 8.2 BIRAC case page (N7 home target) — skeleton owned by S5, referenced here

The BIRAC case-page format is **kept verbatim from the liked O1 model** (S5 owns the
skeleton: anchors for deep-linking per N7, frontmatter, aliases). Reference order:
**Background → Issue → Rule → Analysis → Conclusion**, with pinpointed holding, authority
weight (exact allowlist) + Field-I treatment pill, CL link, and backlinks to doctrine
pages. Split-treatment cases carry a **point-status table** (per-point Field-I). Per L8,
**case pages *restate*; doctrine pages *teach*** — no generalized field-advice on the
canonical case record.

---

## 9. Consistency with prior rulings (DECISIONS.md D-0…D-8)

This document **extends, never reverses** the prior self-interview decision log:

- **D-3 (slug stability / naming):** preserved — renamed pages carry aliases (template
  frontmatter §8.1/§8.2); no slug is silently changed.
- **D-5 (two-key + circuit-split policy):** preserved and strengthened — the two-key rule
  (L1) governs every assertion through the 10-gate protocol (SR-7), circuit cases name the
  circuit and flag splits (N2 / §3), and SR-1 adds exhaustive live re-verification on top.
- **D-6 (lossless deck):** preserved — decks derive FROM verified pages and never the reverse
  (L1); deck↔page↔index integrity is D12; flashcard ids are preserved. *(The deck itself is
  deliberately frozen until the post-S9 flashcard rebuild — deferred run #2; S3/S4 preserve
  deck-referenced stems/aliases or log the breakage.)*

No rule in this catalog contradicts D-0…D-8.

---

*End of STANDARDS.md — the governing contract. On any conflict, this document governs
(subject to the signed O2 specs per §0). Style, voice, the term register, and the mnemonic
register live in `docs/STYLE.md`.*
