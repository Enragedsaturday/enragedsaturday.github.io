# SPEC S5 — Entry Models (case + doctrine pages)

status: APPROVED
depends-on: [S1, S2, S3, S4]   gates: [S6, S7, S8, S9]   exec-wave: 2 (with the S3 restructure)
last-updated: 2026-07-03

> The two page templates everything renders through: the **BIRAC case page** (kept verbatim — liked,
> 457/457 uniform) and the **graded-authority doctrine page** (**S1 R6 Variant A** realized: black-letter
> rule callout → Brief → authorities). Plus the **controlled case-table schema set** (NUM-07: 51 header
> schemas → 3), the **pill/weight placement** inside entries (mechanism = S4 R5/R6, audit COH-18), the
> **3-field treatment rendering** incl. point-scoped overrides and the legacy migration window (COH-11),
> and the draft-state banners. Everything here was locked on a **live mockup** (commits `240be19` +
> `8ef8c3d` on `overhaul2/planning`, served over Tailscale; donor pages: *Probable Cause and Reasonable
> Suspicion* + *New York v. Belton*) — the spec follows the mockup to the letter; where a requirement
> says *"as mocked"*, those commits are the normative reference. **The officer-bottom-line / "In the
> field" box is BANNED project-wide (S1 §2.2 + R6 — audit COH-01): nothing here designs, mocks, or
> renders it.** Read with `PRACTICES.md` §5/§7 and the RUNBOOK §4-S5 entry. Conforms to S1; renders
> S2's projection; hangs on S3's tree/registry; consumes S4's mechanisms.

## 1. Objective
Fix the entry models so every case page and doctrine page is authored and rendered against one
standard: one BIRAC skeleton, one Variant-A doctrine skeleton, three sanctioned table schemas, one
treatment vocabulary (Field-I composite + point overrides) with dates behind the hover, and a
content-vs-data authoring boundary that makes table drift structurally impossible.

## 2. Scope
### 2.1 In scope (S5 designs)
The doctrine-page skeleton (rule callout, Brief, pitfalls, Lower-court developments, tables, Sources);
the BIRAC case-page standard (locked) + its treatment-section internals (point-status table); the
controlled table-schema set + case-cell format + injection placement (weight box, Field-I pill, varies
chip); table widths/no-side-scroll; the dates-behind-hover rule within entries (TEACH-15 terminal);
Sources format (TEACH-14); the frontier-section standard (TEACH-08); pitfalls format (TEACH-09);
grouped sub-tables policy (TEACH-10); related-table integrity (TEACH-13); the migration-window
rendering (COH-11); draft-state banners; pinpoint deep-link standard within entries; the Case Index
schema; the S5 lints (skeleton + tables).
### 2.2 Out of scope (owned elsewhere)
The pill/anchor/popover MECHANISM — components, event delegation, tooltip template, `GOOD_LAW_SLUG`
constant (**S4** R5/R6; audit COH-18 — this spec only *places and formats*; the delegation S4 specced
is implemented in the mockup commits and noted there). Treatment *data* — derivation, composites,
overrides, dual dates (**S2**; S5 renders the projection). The tree, re-homings, overviews, the point
registry itself (**S3**). Applying these standards corpus-wide — prose rewrites, table conversions,
heading renames across ~48 doctrine pages (**S7**, running S5's converter). Link density + term
linking + transclusion mechanics (**S8**). Lint implementation in CI + the `^pin-N` carat-leak
remediation (**S9**; NUM-03). Authoring missing case pages (**S6**).

## 3. Requirements (each testable)

**R1 — Doctrine-page skeleton (Variant A realized; user decisions D4/D5, interview 2026-07-03).**
Every `type: doctrine` page renders, in order:
`# Title` → *field-decisive question* (one italic line — S1 N9 guidance, applied by judgment, not
mandatory) → **`> [!rule]` black-letter callout** (R2) → `## The Brief` (the Explanation layer,
closing with the pitfalls block, R10) → `## Lower-court developments` (R11) → `## Key cases` →
`## Related cases across doctrines` (optional — only when cross-doctrine cases earn framing) →
`## Visual` (optional diagram) → `## Sources` (R12). Category/sub-umbrella **overviews and
craft/reference pages are exempt** from the rule callout and tables (S3 R2 already bans key-case
tables on overviews). *Trigger:* any doctrine page authored or restructured. *Check:* H2 sequence on
every `type: doctrine` page matches the skeleton (optional sections may be absent, never reordered);
the callout is present and first after the H1/question. `AUTO:LINT-15 (skeleton)` · `CHECKLIST:D10`.

**R2 — The black-letter rule layer IS the canonical statement site (self-interview SD2).** The
`[!rule] Black-letter rule` callout is composed of the point-of-law statements the page **owns**
(S3 registry `home_page`), one paragraph per point: bolded lead term, verbatim-grounded rule with
pincite(s) (S1 R7 — never auto-generate a standard), and a stable block anchor **`^rule-<point-tail>`**
(e.g. `^rule-probable-cause`). The registry's `statement` field **mirrors** this text; S8 transcludes
*from the callout*; a page owning no minted point still opens with a rule callout (S1 R6 binds every
doctrine page) and S3 R6 decides whether it earns a node. Rule text is the layer gated by
**≥2 independent reviewers** (S1 R6/R12 — S9 mechanics). *Check:* every doctrine page's callout
paragraphs carry anchors + pincites; callout text ↔ registry `statement` deep-equal (S9 coherence
gate); no rule prose duplicated outside transclusion (S1 A3 shingle detector). `CHECKLIST:D1/D10` ·
`AUTO` (S9).

**R3 — BIRAC case page locked verbatim (user decision D9).** Section order:
`# Title` → header line (*cite* · court · **weight** · Treatment: **<label>**) → `## Background` →
`## Issue` → `## Rule` → `## Application` → `## Conclusion` → `## Treatment & subsequent history` →
`## Appears on` → `## Sources`. The degraded plain-text header line stays in source (components
enhance it, never replace it). Voice unchanged. *Check:* 100% of `type: case` pages carry exactly
this H2 sequence (today: 457/457). `AUTO:LINT-15` (case half).

**R4 — Case-page header signaling (as mocked on Belton).** TreatmentBadge renders: the **Field-I
composite pill** (label only — no date text) as an `a.internal` anchor to *Verifying Good Law* via
S4's exported constant; the **`varies by point` chip** (dashed, italic) whenever
`varies_by_point`/overrides exist — an anchor to `#treatment--subsequent-history`; the **neutral
authority-weight label**. Hover = S4 R6 provenance template (dual dates, degrading to single
`as_of`). The six status classes are `treatment-good-law/-history/-caution/-questioned/-superseded/
-unverified`, colors tracking 🟢🔵🟡🟠🔴⚪. *Check:* Belton renders Caution + varies + weight; hover
carries both dates + scope note; no date text in the pill. `MANUAL` on mockup · S9 sample.

**R5 — Treatment & subsequent history internals (user decision D10).** The section opens with a bold
composite lead (`**Composite: <label> — treatment varies by point.**` for split cases; a simple
status lead otherwise), then — **mandatory whenever `point_overrides` is non-empty** — the
**point-status table**: `| Point of law | Status | Controlling authority |`, one row per override
(+ optionally the surviving points, rendered `Good law`), then the explanatory prose (S7 authors;
S9's coherence gate reconciles prose ↔ lake per S2 R12). This table is the sanctioned **authored**
rendering of lake data (the one carve-out from R7's boundary) and carries **no dates** (hover/About
own currency). *Check:* every `varies_by_point` case page renders the table; each row names the
controlling case + Field-II verb consistent with the lake record. `AUTO` (S9 coherence) ·
`CHECKLIST:D3`.

**R6 — The controlled table-schema set (NUM-07: 51 → 3; user decision D1).** The only sanctioned
Case-column table schemas, exact header strings:
1. **Key cases:** `| Case | Holding | Opinion |`
2. **Related cases across doctrines:** `| Case | Relevance here | Primary home | Opinion |`
3. **Case Index (reference/router):** `| Case | Primary home | Opinion |` (S3 regenerates the Index;
   this spec owns its schema).
Case-cell format: `*[[Case Name]]*, <cite> (<year>)`. Relevance cells open with a **bolded 1–2-word
tag** (*Extends. Limits. Boundary. Foil.* — advisory vocabulary, shape standard). **One anchor text:
`opinion`** for every opinion link (TEACH-13). **Self-reference ban:** a Related row whose Primary
home is the current page is an error (it belongs in Key cases). **Grouped sub-tables (TEACH-10) are
author's discretion** (user decision D7): a large Key-cases section MAY split into bolded,
doctrinally-labeled sub-tables — each individually schema-conformant. *Check:* every table with a
Case/Name column matches a sanctioned header row exactly; anchor text uniform; zero self-referential
Related rows. `AUTO:LINT-16 (case-tables)`.

**R7 — The content-vs-data authoring boundary (self-interview SD1 — the drift killer).** Table cells
author **content** (name, cite, year, holding, relevance, primary home, opinion link); table cells
never author **data** (authority weight, treatment status, dates) — data renders via injection from
the frontmatter projection (lake-derived, S2 SSOT). The one carve-out: the R5 point-status table.
JS-off degradation is accepted: the static table stays legible; the authoritative signal lives on
the case page. *Check:* weight-label strings (S1 A8 allowlist) and Field-I/legacy status tokens grep
to **0** inside Key-cases/Related/Index table rows corpus-wide. `AUTO:LINT-16` · `CHECKLIST:D10`.

**R8 — Pill/weight placement in tables (audit COH-18 — S5's half; user decision D2; as mocked).**
The case cell gains a **meta line under the case name**: `[weight box] [● Field-I pill] [varies
chip]`, flex-wrapped, injected when the row resolves to a case record (weight/pill only when the
schema carries no such column — always, under R6). The pill is an `a.internal` to the S4 constant's
target; hover = S4 R6 template via `title`; popover fires through S4 R5's event delegation (any
injected anchor gets hovers for free). Sorting by case name ignores the injected meta. *Check:*
hovering a table pill fires the same popover + tooltip family as the page-header pill;
`tery`-style unresolved rows degrade to plain text with no meta line. `MANUAL` on mockup · S9 sample.

**R9 — Controlled widths, no side-scroll (as mocked, incl. the mobile fix).** Desktop/tablet:
`table-layout: fixed`, width 100% — Case 30%, Opinion 4.6rem, Primary home 17%, Year 4.2rem, prose
column flexes; `overflow-wrap: break-word`. **Mobile (≤ Quartz `$mobile`): stock auto layout + the
`.table-container` overflow scroll** — the live 400px check showed fixed layout crushes the prose
column to one word per line. *Check:* no horizontal scrollbar on a Key-cases page at ≥1200px; at
400px the table remains readable (container scrolls, prose wraps naturally). `MANUAL` · S9 visual.

**R10 — Pitfalls standard (TEACH-09; user decision D6).** The Brief closes with a
**`**Common pitfalls.**`** bold lead-in followed by bullets, each opening with the **bolded error**
then the correcting cite (donor: PC/RS). No standalone pitfalls H2; no numbered-in-paragraph
variants; no "Recurring field and analytical errors" fork. *Check:* pitfalls blocks corpus-wide
match the shape (bold lead + bulleted bold-error+cite); zero alternate pitfall headings.
`AUTO:LINT-15` (pattern) · S7 applies (register TEACH-09).

**R11 — "Lower-court developments" — the frontier section (TEACH-08; user decision D5).** The
section is renamed **`## Lower-court developments`** (role-based — can't go stale) and sits
**directly under The Brief, above the case tables**. Content: role-tagged bullets — bold case name
+ court + year, italic role tag (*narrows / extends / splits*), the holding line, the weight label,
`[opinion](…)` link; **no SCOTUS** (S1 N5 — a SCOTUS holding is never a "development"; it goes in
the brief and Key cases); **no inline dates; no meta-labels** (S1 A2). An emerging **circuit split**
may also earn a one-line mention in the Brief itself, by judgment. S7 applies corpus-wide (the 2008
*Liddell* class gets re-homed or cut during the rewrite). **Lint re-pointing:** S1 A2's
N5 section-scoped check and any "Recent developments" grep re-point to the new heading (routed to
S9's roster — see §9). *Check:* zero `## Recent developments` headings post-S7; the section precedes
`## Key cases` on every page that has both; no SCOTUS-court wikilink inside it (S2 lake court
field). `AUTO:LINT-15` + LINT-3-extended (S9).

**R12 — Sources standard (TEACH-14; user decision D8).** One format, both page types: bracketed
links — `- [*Case Name*, <cite> (<year>)](<url>)`, trailing parentheticals (pinpoints, treatment
notes) as plain text after the link. Donor: Miranda; the em-dash list form is retired (no Sources
carve-out needed under S1 A7/A8). *Check:* every Sources bullet matches the bracketed pattern.
`AUTO:LINT-16` (pattern).

**R13 — Dates hover-only within entries (TEACH-15 terminal; user decision D3).** Table cells DO
count as "inline" under S1 R3: **no as-of/date text renders in any table cell, pill, or entry
header line** — dual dates live in the hover tooltip and on the About page. The 527/342/51/25
treatment-cell variants die with the treatment column (R6/R7). *Check:* date-pattern grep inside
sanctioned tables + pill markup = 0; the tooltip renders dual dates (or degraded single `as_of`).
`AUTO:LINT-16` · `MANUAL` hover check.

**R14 — Migration-window rendering (COH-11 — consumes S1 A4 / S2 A13).** All entry-model rendering
resolves treatment through one shared helper: the S2-projected 3-field shape when present, else the
legacy single status **through the S1 A4 mapping** (`good→good_law · limited→caution+varies ·
criticized→caution · overruled/abrogated→superseded`) — so the reader sees ONE vocabulary before and
after the projector lands, and a legacy `limited` case always carries the varies warning. An
**unmapped legacy value renders Unverified ⚪ + banner** — fail-visible, never silent. The legacy
path is belt-and-suspenders after S2 A13's projector runs (which is the authoritative migration).
*Check:* a projected page (Belton) and a legacy page render the same label set; an injected bogus
status renders the ⚪ banner in test. `AUTO` (helper unit check) · S9 sample.

**R15 — Draft-state banners (self-interview SD4).** Any case page whose `lake.status` ∈
{`draft`, `under_review`} or whose Field-I is `unverified` renders a **top-of-content ⚪ banner**
("This entry has not completed verification — treat as unverified."). The real wall is S2 R12's
page↔record publish gate; the banner is defense-in-depth so S1 R2's "⚪ never reaches a reader
unbannered" holds even on previews. *Check:* an `under_review` fixture renders the banner;
`verified` renders none. `AUTO` (fixture) · maps S1 R2.

**R16 — Pinpoint deep-links within entries (user decision D11).** Case pages keep one `^pin-N`
block anchor per pinpointed passage in Rule/Application (slip-only pins render as authored, per S2
A3's `pinpoint_status`). **Every quoted proposition in doctrine prose whose case page pins the
passage links the pin anchor** (`[[Case#^pin-N|…]]`) so a click lands on the exact passage;
paraphrases link the page normally. S8 mechanizes density; S9 owns the visible-carat remediation
(LINT-9, NUM-03). *Check:* sampled quoted propositions land on pinned text (S9 dimension D1/D2).
`CHECKLIST:D1` · S9.

**R17 — Opinion-link fallback (user decision D1 note; consumes S2 R14).** The Opinion column's
target is the CourtListener opinion when coverage exists; on a CL gap it is the record's whitelisted
`off_cl_links` fallback in order **Justia → Google Scholar → Cornell LII → official court/reporter
site**. Anchor text stays `opinion` either way (TEACH-13's one-anchor-text). *Check:* every opinion
link's host ∈ CL ∪ the S2 R14 whitelist. `AUTO:LINT-16` (host check).

## 4. Lessons enforced
**Table drift** (900+ authored data cells, 4 date formats — NUM-09/TEACH-15) → R7's content-vs-data
boundary + R13. **Copies drift** (the same rule restated across pages) → R2's canonical-callout +
registry mirror. **Header anarchy** (51 schemas, 43 singletons — NUM-07) → R6's three schemas +
LINT-16. **Pills-as-spans-lack-popovers** (O1) → R8 on S4 R5's delegation. **Misscoped good-law
verdicts** (Belton read as simply "limited") → R4/R5 render the composite + point-scoped table so
the reader sees *which point* died. **Stale "Recent"** (2008 under "Recent developments") → R11's
role-based name. **Officer-BLUF stays banned** (S1 §2.2/R6) — no field-application layer exists in
either skeleton; the scar rule (S1 R7: never auto-generate a standard) is why R2's rule text is
verbatim-grounded + pincited.

## 5. Method (execution — wave 2, with the S3 restructure)
1. Adopt the mockup commits (`240be19`, `8ef8c3d`) as the working standard — components
   (caseHelpers resolver + labels, TreatmentBadge, CaseTable island, casetable.inline injection,
   popover delegation, casetable/treatmentBadge/custom SCSS) are already the decided form.
2. Ship `scripts/s5/convert_tables.py`: mechanical corpus conversion — strip weight/treatment
   columns, rewrite headers to the R6 set, Sources → bracketed, `## Recent developments` →
   `## Lower-court developments` + section move, pitfalls lead normalization. **S7 runs it per-page
   during doctrine production** (prose judgment stays human/S7).
3. Case pages: the S2 projector (A13) rewrites treatment frontmatter; S5's components render it; S7
   authors the R5 point tables for the 11 `limited` + 7 `overruled/abrogated` migrations.
4. Add `LINT-15 (skeleton)` + `LINT-16 (case-tables)` to `scripts/lint/` (S9 wires CI, numbering
   confirmed at the roster codification per S1 A5).
5. Banner component for R15; fixture pages for the lint self-tests.

## 6. Deliverables
This spec · mockup commits `240be19` + `8ef8c3d` (normative reference) · the entry-model components
as mocked (shared treatment resolver in `caseHelpers.ts`, TreatmentBadge, casetable island +
injection, SCSS) · `scripts/s5/convert_tables.py` (at execution) · `LINT-15`/`LINT-16` specs (S9
implements CI) · the R15 banner (at execution) · Decision Log below (audit dispositions).

## 7. Acceptance criteria
- [ ] R1/R3 skeletons hold: doctrine H2 order (incl. Lower-court developments above tables) + BIRAC
      order 457/457; exempt page classes untouched.
- [ ] R2 every doctrine rule callout: anchored, pincited paragraphs; registry mirror deep-equal (S9).
- [ ] R4 header pill: label-only, varies chip anchored to the treatment section, dual-date hover.
- [ ] R5 every varies case renders the point-status table consistent with the lake.
- [ ] R6/R7 zero non-sanctioned Case-table headers; zero authored data tokens in table cells.
- [ ] R8 table pills fire popovers via delegation; unresolved rows degrade cleanly.
- [ ] R9 no side-scroll ≥1200px; mobile auto layout readable.
- [ ] R10–R12 pitfalls/frontier/Sources standards hold corpus-wide post-S7.
- [ ] R13 zero rendered dates inside entries; hover carries them.
- [ ] R14 legacy and projected pages render one vocabulary; unknown → ⚪ banner.
- [ ] R15 non-verified pages banner; verified don't.
- [ ] R16 sampled quoted propositions deep-link to pins.
- [ ] R17 every opinion link host ∈ CL ∪ whitelist.

## 8. Verification plan
S5's own gates: the mockup IS the visual acceptance (user-signed, 2026-07-03); LINT-15/16 run
fail-closed once S9 wires them. **S9** re-verifies: R2 callout↔registry coherence + the ≥2-reviewer
rule-layer gate; R5 point tables against lake records; R8 popover behavior sampled; R16 pin-link
landing checks; R11's re-pointed N5 lint. S7's production runs the converter and is itself gated by
the standard content gates.

## 9. Open items / escalations
- **S2 projection field names** — mocked as `treatment.field_i_validity / varies_by_point /
  as_of_content / as_of_treatment / point_overrides[] / scope_note` + `lake{record_id,status,
  projected_at}` (S2 R5/R12 record names). If the projector emits different frontmatter names, the
  shared resolver adopts S2's (S2 is SSOT) — one-file change (mirrors S4 §9).
- **Heading-dependent lints** — S1 A2's N5 check and any "Recent developments" grep re-point to
  `## Lower-court developments` (S9 roster codification; register TEACH-08).
- **LINT numbering** — LINT-15/16 provisional per S1 A5's numeric series; S9 confirms at the roster.
- **Relevance-tag vocabulary** stays advisory; if S7 production forks it badly, close the list then.
- **`^rule-<point-tail>` anchor grammar** binds to S3's registry ids at execution (tail = last id
  segment; collisions within a page get the full dotted id, dashes for dots).
- **JS-off/print story** — accepted degradation (R7); if print matters later, a build-time injection
  emitter is the upgrade path (worked SD1 alternative b), not authored cells.

## 10. Decision log

**User decisions (interview, 2026-07-03 — on the live mockup).**
- **D1** Both table schemas approved (Key cases 3-col; Related 4-col); note adopted: on a CL
  coverage gap the opinion link falls back to a whitelisted source (→ R17; header renamed `Opinion`).
- **D2** Pill + weight under the case name (meta line), not inline or column.
- **D3** Dates hover-only **everywhere** incl. the case-page header pill; table cells count as
  "inline" under S1 R3 (TEACH-15 terminal).
- **D4** Rule callout approved; **field-decisive question moves above the callout** (pivoted live).
- **D5** Frontier heading = **"Lower-court developments"** (over the recommended "Circuit & state
  frontier"); section sits **above the tables, under the Brief** (pivoted live); circuit-split
  brief-mentions by judgment.
- **D6** Pitfalls = bold `**Common pitfalls.**` lead + bulleted bold-error+cite, closing the Brief.
- **D7** Grouped Key-cases sub-tables = **author's discretion** (schema-conformant; no threshold).
- **D8** Sources = bracketed links.
- **D9** BIRAC kept exactly as-is (order + voice).
- **D10** Treatment section = composite lead + point-status table + prose.
- **D11** Pinpoint deep-links on **every quoted proposition**.
- **D12** COH-14 book case-example PDF: **drop the reference** (BIRAC already settled from the live
  corpus).

**Self-interview (SD1–SD10, condensed; full text in the thread).** SD1 content-vs-data boundary —
client injection from the projection over authored cells (drift) and build-time rewrite (new
cross-file plumbing for JS-off only); Treatment-section carve-out. SD2 the rule callout IS the
canonical statement site; registry mirrors; S8 transcludes from it; per-point block anchors; exempt
page classes. SD3 legacy renders through S1 A4 at the component layer; unknown → ⚪ fail-visible.
SD4 draft banners as defense-in-depth behind S2's publish gate. SD5 three sanctioned schemas (one
per table role) incl. the Case Index. SD6 `opinion` anchor text constant; fallback data-driven.
SD7 self-reference ban lintable. SD8 relevance-tag shape enforced, vocabulary advisory. SD9 fixed
widths desktop-only (mobile crush found live at 400px). SD10 the TEACH-08 rename must re-point S1
A2's N5 lint (routed S9).

**Audit-row dispositions (injected:S5 — AUDIT-CLOSURE gate).**
- **TEACH-08** ADOPTED-ADAPTED — role-based rename per the audit, but the user chose
  **"Lower-court developments"** and moved the section above the tables (D5; R11); lookback-window
  alternative rejected (staleness returns). S7 applies (its register row stands).
- **TEACH-09** ADOPTED — bulleted bold-error+cite per the PC/RS donor, as the Brief's bold-lead
  closing block (D6; R10).
- **TEACH-10** ADAPTED — grouping kept but as author's discretion (user D7) instead of the audit's
  >15-case threshold; re-fork risk contained by R6 (sub-tables stay schema-conformant + LINT-16).
- **TEACH-13** ADOPTED — self-reference ban + controlled header set + one `opinion` anchor text
  (R6; lint conditions in LINT-16).
- **TEACH-14** ADOPTED — one Sources format: bracketed links (D8; R12).
- **TEACH-15** ADOPTED — table cells count as inline; the treatment column dies, all four cell-date
  variants retired; dates hover-only (D3; R7/R13). Resolved jointly with COH-11's vocabulary.
- **NUM-07** ADOPTED — 51 schemas → **3 sanctioned** (one per table role) + exact-header lint
  (R6/LINT-16). The "→1" target is realized as one schema *per role* — a single literal schema
  cannot carry both holdings and cross-doctrine framing (option offered; user chose the pair, D1).
- **COH-11** ADOPTED — S1 A4/S2 A13 mapping consumed at the rendering layer (shared resolver);
  legacy `limited` auto-warns varies; unmapped → ⚪ banner (R14).
- **COH-18** ADOPTED — boundary held: S4's mechanism (R5 delegation, R6 template, the exported
  constant) consumed as-is — the delegation S4 specced was implemented in mockup `240be19` as S4 R5
  prescribes; S5 placed/formatted (R4/R8).
- **COH-14** RESOLVED — user decision D12: the missing book case-example PDF reference is
  **dropped**; RUNBOOK §4-S5/§6 pointers updated this date.
