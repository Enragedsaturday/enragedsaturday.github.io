# SPEC S1 — Standards & Style Manual

status: APPROVED
depends-on: []   gates: [S2, S3, S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-02

> The constitution. S1 **designs** the rules; it authors `docs/STANDARDS.md` (updated) + `docs/STYLE.md`
> (new) at execution. Read with `_overhaul2/PRACTICES.md` — this spec **references** the mechanism text
> there (3-field treatment, 10 gates, AI guardrails, signaling) rather than duplicating it. Every rule
> carries **Trigger · Check · Enforcement** (`AUTO:LINT-n` / `CHECKLIST:Dn` / `PROCESS`), the O1 format.

## 1. Objective
Refresh the CSSI constitution for Overhaul 2: carry the Overhaul-1 rule architecture forward and extend
it with the production-line mechanisms, so every page is authored and verified against one testable
standard. Output: an updated `docs/STANDARDS.md` + a new `docs/STYLE.md`.

## 2. Scope
### 2.1 In scope (S1 designs)
The rules catalog (carry-forward + O2 extensions); the graded-authority entry template; the treatment
vocabulary; the per-proposition verification protocol; the AI guardrails; the reader-signaling scheme;
the 6-tier authority-weight lexicon; the Humanizer voice subset; the mnemonic register; the term
register; the lint roster.
### 2.2 Out of scope (owned elsewhere)
Taxonomy (S3); data-lake schema (S2 — though S1 fixes the treatment fields the lake must carry);
page rendering / reader-signaling UI (S4); per-page content (S7); review harness mechanics (S9).
**The field-application / "officer bottom line" summary is OUT for the whole project** — it is a
human-in-the-loop artifact and a paraphrase-drift risk; the reader is given the verified rule + brief
and applies it themselves.

## 3. Requirements (each testable)

*Amended — Trigger lines added for R1–R14; see Amendments A3.*

**R1 — Carry the O1 architecture forward.** `STANDARDS.md` retains: the Trigger/Check/Enforcement rule
format; scar-rules **L1–L8**, mechanism-rules **N1–N13**, standard-rules **SR-1…SR-5**; dimensions
**D1–D14**; the LINT-1…8 roster; the find→adjudicate→fix machine; DECISIONS D-0…D-8. *Check:* every O1
rule present and unchanged **unless** explicitly superseded by R2–R14. `PROCESS`.
*Amended — L4 rescoped to one-serial-lane-per-credential; see Amendments A1.*

**R2 — Treatment = the 3-field vocabulary (replaces single `treatment.status`).** Adopt PRACTICES §2:
Field I validity status (`good_law/history/caution/questioned/superseded/**unverified⚪**`), Field II
treatment tag (~12 values), Field III depth — each scoped to a point of law + an as-of date; "a red
flag is a clue, not a verdict." Rewrite STANDARDS §3.1 / N4 / N13. *Check:* the single-axis status is
gone; `⚪ unverified` can never render to a reader unbannered. `AUTO:LINT-6` (extended) · `CHECKLIST:D3`.
*Amended — old→new migration mapping added (A4); ⚪ fixed as the canonical glyph (A6). See Amendments.*

**R3 — Dual as-of dating + placement.** Every case/entry carries `content_verified` and
`treatment_checked` (decay independently). **Reader-facing placement = data model + hover + the About
page, NOT inline** on every assertion (PRACTICES §7). *Check:* both dates in the schema; no inline
date litter. `AUTO:LINT-6` · `CHECKLIST:D7`.

**R4 — The 10-gate per-proposition verification protocol.** Codify PRACTICES §3 as named rules: KEY-1
substantiation G1–G5 (existence, support, quote fidelity, pincite, form) + KEY-2 validity G6–G10
(direct history, citator/derived status, on-point treatment, jurisdiction+validated-through date,
independent corroboration); PASS/FAIL/FLAG per gate; **≥1-in-10 independent re-verify**. *Check:* a
proposition is VERIFIED only when all applicable gates pass. `CHECKLIST:D1` · `PROCESS`.

**R5 — AI guardrails G1–G10 (new first-class block).** Adopt PRACTICES §6, fail-closed: retrieval-
grounded only; no proposition without a verified pincite; citation-existence check ("not found ≠
fabricated" → block+investigate; compare input name vs CL canonical ourselves); quote string-match;
holding-support; treatment/currency check; generator ≠ verifier; human sign-off; immutable provenance;
dual-date re-verification. *Check:* each maps to a pipeline gate or a review dimension. `PROCESS` · `AUTO`.
*Amended — Check concretized (named G1–G10 enforcement-map table); see Amendments A3.*

**R6 — Graded-authority entry model = Variant A.** Every doctrine page = **Black-letter rule** (the
only thing published *as* the law; ≥2 independent reviewers) → **Explanation** (the verified teaching
brief: nuances, limits, pitfalls) → **Authorities & notes** (attributed, lighter). **No field-
application summary.** Update STANDARDS §8.1 to this 3-layer template. *Check:* template present; the
rule layer is a distinct, separately-gated object; no auto-generated officer-bottom-line. `CHECKLIST:D10/D14`.

**R7 — L8 sharpened: never auto-generate a controlling standard.** Restate, do not editorialize; never
add/drop/narrow/broaden a holding or standard; ground it verbatim in the opinion. The canonical scar:
emergency aid is an **"objectively reasonable basis to believe,"** not "sees someone in imminent
danger." *Check:* no standard asserted without a pinned primary-source quote/paraphrase that matches.
`CHECKLIST:D1/D2` · `PROCESS`.

**R8 — Humanizer voice subset (STYLE.md).** Codify the ADOPT/ADAPT/REJECT table (Appendix A). The voice
pass applies to **explanation prose ONLY**. **Cut the em-dash habit in prose; KEEP en-dashes in
citation/page/date ranges** ("392 U.S. 1, 21–22"). Hard carve-outs: never inside a quotation, on a
black-letter rule/holding/standard, on citations/case names, or on controlled labels. *Check:* a lint
flags prose em-dashes with a citation-range exemption; carve-outs enforced. `AUTO:LINT-10` (new) ·
`CHECKLIST:D9`.
*Amended — Check concretized (A3); LINT-10 exemptions restated correctly (A7); em-dash density budget +
S7 rewrite-pass decision (A8). See Amendments.*

**R9 — Mnemonic register (verified; verbatim; uncited).** The permitted set + where each fits +
guardrails (Appendix B). **C.R.E.W.** = three justifications, **C / RE (Recognized Exception) / W** —
exigency is one example *inside* RE, not a fourth item. **"CRON" is removed** (a dictation error).
*Check:* mnemonics appear verbatim, never citation-attached; no four-way CREW; no CRON. `AUTO:LINT-8` ·
`CHECKLIST:D11`.

**R10 — Authority-weight lexicon (carry verbatim).** The 6 tiers (Binding—SCOTUS · Binding in-circuit
· Persuasive (outside circuit) · Persuasive—state, illustrative · Persuasive only—non-precedential ·
Historical); **"persuasive, not binding" banned**; circuit cases name the circuit; splits flagged.
*Check:* only these labels site-wide. `AUTO:LINT-4` · `CHECKLIST:D6`.
*Amended — canonical label order ("Binding — SCOTUS", never "SCOTUS — binding") and the exact
spaced-form label allowlist added to the Check; R10's listed forms are superseded on spacing by A8's
allowlist, and LINT-4 validates against it exactly. See Amendments A8 (rev. per Codex review
2026-07-02).*

**R11 — Term register + single-source transclusion.** STYLE.md carries a controlled word list (canonical
spelling/definition per term of art); each rule/term is stated **once** as a canonical node and
transcluded, never re-paraphrased (PRACTICES §8). Term-of-art consistency: never drift *stop→detention→
seizure*. *Check:* a Vale-style prose lint enforces the register; no duplicate rule prose across pages.
`AUTO:LINT-7` (extended) · `CHECKLIST:D5`.
*Amended — Check concretized (machine-readable register + mechanical duplicate-prose detector); see
Amendments A3.*

**R12 — Reviewer panel + machine ledger (standard-setting; mechanics in S9).** Legal assertions are
reviewed by **1 Claude + 2 Codex** with a **≥2-of-3 refute tally**; findings→adjudications→fixes→
inventory are **machine-emitted and reconcilable**. *Check:* STANDARDS §6/SR-4 states this; S9 implements.
`PROCESS`.

**R13 — Lint roster extended.** Add **LINT-9** (`^pin-N` carat-leak: block-ref anchors must not render
as visible text), **LINT-10** (prose em-dash with citation-range exemption); extend **LINT-4**
(lexicon incl. weight labels) and **LINT-6** (treatment → 3-field); add fail-closed **link/citation
resolve** + **term-register** checks. All run in CI, fail-closed. *Check:* roster documented in
STANDARDS §7. `AUTO`.
*Amended — lint numbering standardized (LINT-9…LINT-14; `LINT-S2-*` mapped into the series); see
Amendments A5.*

**R14 — Content-structure rules (carry + tighten).** Numbered "apply-it" lists (N3/N8); **no internal
meta-labels in prose** (kill "(woven in)"); **no SCOTUS case in "Recent developments"** (N5); tests/
prongs stated up front in the Rule (N3); brief-first (N8); **slip-op pinpoints only for the current
Supreme Court term** (else a reporter pinpoint). *Check:* the lints (LINT-3 extended) enforce each.
`AUTO:LINT-3` · `CHECKLIST:D10`.
*Amended — meta-label ban broadened to ALL editorial-pipeline vocabulary with Trigger/Check/Enforcement
(A2); paragraph-density budget for the Brief added (A9). See Amendments.*

## 4. Lessons enforced
Carries L1–L8, N1–N13, SR-1…SR-5. Sharpens **L8** (R7). Adds the AI-guardrail block (R5 — engineer
against our own failure mode: Mata v. Avianca → 9th-Cir. LNU v. Blanche; Stanford RegLab 17–33%).
Upgrades N4/N13 (treatment) and N11/LINT-7 (term register).

## 5. Method (execution)
1. Branch. 2. Rewrite `docs/STANDARDS.md`: carry-forward verbatim where unchanged; rewrite §3.1/N4/N13
for 3-field treatment + dual dates; add the graded-authority template (§8.1), the 10-gate protocol, the
AI-guardrail block, the reviewer-panel/ledger standard; extend D-dimensions + lint roster. 3. Author
`docs/STYLE.md`: house style + precedence stack (project → legal citation manual → Chicago); the term
register (word list); the Humanizer subset table; the mnemonic register. 4. Extend `scripts/lint/`
(LINT-9, LINT-10; LINT-4/6/7 updates; link/cite fail-closed). Every rule = Trigger/Check/Enforcement.

## 6. Deliverables
`docs/STANDARDS.md` (updated) · `docs/STYLE.md` (new) · `scripts/lint/` extensions (LINT-9/10 + updates).

## 7. Acceptance criteria
- [ ] All O1 rules carried or explicitly superseded (R1).
- [ ] 3-field treatment + dual dates replace single status; `⚪ unverified` gate present (R2/R3).
      *(rev. per Codex review 2026-07-02 — glyph corrected in place per A6)*
- [ ] 10 gates + AI guardrails codified as testable rules (R4/R5).
- [ ] Graded-authority Variant A template present; no field-application summary (R6).
- [ ] Humanizer subset in STYLE.md; prose em-dash lint with citation-range exemption; carve-outs (R8).
- [ ] Mnemonic register verbatim; CREW = 3 justifications; no CRON (R9).
- [ ] 6-tier lexicon verbatim; "persuasive, not binding" banned (R10).
- [ ] Term register + single-source transclusion rule (R11).
- [ ] Lint roster extended (LINT-9/10 + updates), CI fail-closed (R13).
- [ ] Content-structure rules incl. slip-op-current-term-only (R14).

*Amended — criteria read subject to Amendments A1–A9: the R2/R3 line's glyph was corrected in place to
`⚪` (A6; rev. per Codex review 2026-07-02); "citation-range exemption" in the R8 line reads per A7;
the R14 line includes the broadened pipeline-vocabulary ban (A2) and the paragraph-density budget (A9);
the lint roster reads per A5.*

## 8. Verification plan
→ S9 confirms every rule is testable and enforced; the lints run in CI fail-closed; the graded-authority
template and treatment vocabulary are exercised on a sample page during S5/S7 review.

## 9. Open items / escalations
- Motor-vehicle 4-element checklist wording **UNVERIFIED** (bluetogold.com Cloudflare-blocked) — verify
  before any use in S7.
- Final STYLE.md precedence order + word-list seeding settled at execution.

## Appendix A — Humanizer ADOPT / ADAPT / REJECT (voice pass, explanation prose only)
**ADOPT:** ban AI-vocab (delve/tapestry/testament/landscape/underscore/leverage…); cut filler
(in-order-to→to); kill significance-inflation, promo adjectives, "-ing" padding, chatbot tics/
sycophancy/cutoff-disclaimers, signposting/fake-candor/staccato-drama, false ranges; **don't cycle
synonyms — repeat the exact term** (= term-of-art discipline); vague attribution → dated/specific source.
**ADAPT (with legal carve-out):** reduce rhetorical hedging but keep legal modality (may/must/reasonable/
objectively-reasonable/articulable); prefer active but keep correct legal passives; avoid rule-of-three
padding but keep real N-prong tests; kill "not just X, it's Y" but keep genuine doctrinal contrasts;
strip decorative emoji but keep treatment-status glyphs; **em/en-dashes: cut the em-dash habit in prose,
KEEP en-dashes in citation/page/date ranges.**
**REJECT (conflicts with legal writing):** de-hyphenating terms of art (good-faith, stop-and-frisk,
bright-line); converting numbered tests/apply-it lists to prose; lowercasing legal headings.
**NEVER APPLY:** inside a quoted opinion; on a black-letter rule/holding/standard; on citations/case
names; on controlled labels (weight/treatment).

## Appendix B — Mnemonic register (verified)
| Device | Wording | Fits |
|---|---|---|
| **C.R.E.W.** (3 justifications) | **C**onsent · **R**ecognized **E**xception · **W**arrant (exigency is one example inside RE) | CREW / "what is a search" intro; exceptions overview |
| **N.E.R.D.S.** | Bandiero's report-writing acronym | Instructor craft / report-writing |
| **Three Golden Rules** | (1) articulate the *why* → more likely upheld (*Terry*); (2) more serious crime/circumstance → more reasonable (*Graham*); (3) 4A deals in **probabilities, not possibilities** (*Brinegar*/*Gates*) | Instructor craft; woven where apt |
| **Strive for Five** | Articulation drill — name ≥5 facts, "opinion first, then because →"; not a 5-factor test | Reasonable suspicion / articulation |
| **Hot / fresh pursuit** | "Hot pursuit = hot on the suspect's tail; fresh pursuit = fresh on the trail" | Exigency / hot pursuit |
| **Dominoes (Decision Sequencing)** | Unlawful step taints what's derived after it; what's found *before* the first fallen domino survives. **Credit Bruce-Alan Barnard.** **Guardrail:** oversimplifies — attenuation / independent source / inevitable discovery mean not every later domino falls. | Fruit of the poisonous tree (§8) |
| **Rubber band** | The 4A "stretches" for violent/urgent/fast-moving situations. **Guardrail:** a reasonableness *multiplier, not a warrant bypass.* | Three Golden Rules R2; reasonableness |
| **"Worthless alone → totality"** | Individual factors mean little in isolation; build the totality. | Reasonable suspicion (pairs with Strive for Five) |
| define/attribute only | "right to be left alone" = **Brandeis, *Olmstead* dissent** (not Bandiero) | Katz / REP |
| ~~CRON~~ | **REMOVED — dictation error, no such Bandiero mnemonic** | — |

## Appendix C — Decision log
- **Graded authority = Variant A** (rule/explanation/authorities), + drop the field-application summary
  entirely (human-in-the-loop; reader applies the rule). *Adjudicated on the 2026-07-01 mockup.*
- **Field-decisive question (N9) = framing strategy, not an explicit requirement.** The one-line
  orienting question is retained as *guidance* (carried via N9), applied by judgment where it helps;
  it is **not** a hard/lint-enforced rule and every page need not carry one. Exact placement in the
  Variant A template, if any, is an S5 (Entry Models) call.
- **Humanizer** adopted as a fenced voice pass (Appendix A); the driving concern was em-dash overuse —
  resolved as prose-cut + citation-range keep.
- **Treatment** upgraded to the 3-field vocabulary; **dates** kept in data-model/hover/About, not inline.
- **CRON dropped** (dictation error); Bandiero's real inventory verified (Appendix B); no hidden acronym.
- **Codex builds the data-lake** via REST+token (S2); Codex + 2 lanes review; Claude orchestrates + 1 lane.

## Amendments — 2026-07-02 (audit integration)

Register: `_overhaul2/AUDIT-2026-07-02.md`. Each amendment supersedes the quoted body text; body
pointers mark every amended site. A1 and A3 change prior decisions and carry Decision-Log-grade
reasoning. R1's carry-forward exception ("unless explicitly superseded by R2–R14") is read as
"…by R2–R14 **or a logged Amendment below**" — an amendment IS the explicit-supersession mechanism.

### A1 — L4 rescoped: one serial CL lane **per credential** (COH-07)

**Supersedes (R1 carry-forward of O1 L4, `docs/STANDARDS.md` §L4):** "**ALL** CourtListener calls go
through a single serial lane (concurrency-1), **always** — writing, review, adjudication, and research
alike."

**New normative text (L4′):** Every CourtListener **credential** has exactly **one consumer**, serial
within itself — never two consumers on one credential.
- The **S2 Codex REST builder exclusively owns the project API token** (`~/.config/cssi/cl-token`);
  it is serial within itself and paced per S2 R10 (token-bucket ≤~14 req/min, backoff, journal). No
  other process, agent, or lane may touch that token for any purpose — not review, not adjudication,
  not "one quick check" mid-build.
- The **Claude CL MCP** (claude.ai-managed connector) is a **separate credential**, used for
  **interactive spot-checks only** — never for bulk ingest, never scripted against the project token's
  quota.
- *Trigger:* any CL call anywhere in execution. *Check:* every builder journal / `cl-calls.log` line
  records the **consumer identity + credential fingerprint** (rev. per Codex review 2026-07-02 — S9
  audits on those fields); the log shows only builder calls on the project token with no concurrent
  timestamps; no MCP-originated call ever appears against the project token. *Enforcement:* `PROCESS`
  + `CHECKLIST` (log audit, S9).

**Decision log.** *Question:* O1's L4 mandates ONE serial lane project-wide, but O2 designs two CL
consumers (S2 REST builder + Claude MCP spot-checks). Keep, drop, or rescope? *Why L4 existed:* the O1
rate-limit breach escalation — uncoordinated concurrent calls on one shared token blew through the
throttle tier (hence the tier probe and the STOP-on-old-5/min-tier rule). Its intent is
**never self-inflict concurrency on a single quota**. *Alternatives:* (a) keep the global single lane —
every interactive spot-check queues behind a 20–30 h build; review becomes unworkable, inviting covert
violations; (b) allow free concurrency — recreates the O1 scar; (c) one serial lane per credential —
CL enforces rate limits per credential, so per-credential serialization preserves the anti-breach
intent exactly while the two-consumer design stays legal. *Pick:* (c). *Failure mode guarded:* quota
exhaustion / 429 escalation on a shared token — including the subtle case of "borrowing" the project
token for a quick manual check during a build, which is now explicitly forbidden.

### A2 — R14 broadened: ban ALL editorial-pipeline vocabulary from reader-facing prose (TEACH-02a)

**Supersedes (R14, partial):** "**no internal meta-labels in prose** (kill '(woven in)')".

**New normative text:** No **editorial-pipeline vocabulary** may appear in reader-facing prose,
site-wide. The banned classes (each grep-able):
1. **Rule/spec/lint identifiers** — `LINT-\d+` / `LINT-S2-*`, rule refs `L\d`/`N\d{1,2}`/`SR-\d`/
   `R\d{1,2}`/`D-?\d{1,2}`/`G\d{1,2}`, spec refs `S[1-9]` (word-bounded, context-aware: "S. Ct."
   and statute section numbers never match).
2. **Provenance / re-homing notes** — "Re-homed from", "Moved from", "Merged from", "Split from",
   "migrated from".
3. **Pipeline status markers** — "CL-confirm pending", "pending CL", "annotate-only", "deferred to
   EXECUTE", "pending verification", "TODO", "TBD", "FIXME".
4. **Editorial meta-labels** — "(woven in)", "No standalone case page" (×12 files live today),
   "placeholder", "this page intentionally".
5. **Internal artifact names** — `cl-calls.log`, S6-SEED, STANDARDS/STYLE/spec/wrapper/RUNBOOK/
   PRACTICES references, "data lake", "frontmatter", "lint" (as our pipeline's artifacts).

Where such state must **persist**, it moves to an **HTML comment** (`<!-- s8: CL-confirm pending -->`)
or a **frontmatter key** — never rendered prose. The About page is the one sanctioned place the
methodology may be described; it is allowlisted.
- *Trigger:* any commit touching `content/`. *Check:* the five pattern classes above grep to **0
  hits** over reader-facing text (source minus frontmatter, HTML comments, and code fences), modulo
  the allowlist. *Enforcement:* `AUTO:LINT-11` (pipeline-vocab, per A5; S9 implements in the CI
  roster, fail-closed) · `CHECKLIST:D10`.

Boundary: stripping today's live leaks is S7 work (register TEACH-02c); the lint build is S9
(TEACH-02b). N5 ("no SCOTUS case in Recent developments") is unchanged.

**Concretized Check for the broadened R14 (rev. per Codex review 2026-07-02).** R14's "the lints
enforce each" is delivered, for the vocabulary ban, by the class→check mapping below (closing
COH-09's R14 leg). All rows run over rendered prose only — frontmatter, HTML comments, code fences,
and the About-page allowlist are excluded before matching:

| Class | Pattern family (`grep -E`) | Enforcing check | Fail mode |
|---|---|---|---|
| 1 — identifiers | `\bLINT(-S2)?-[0-9]+\b` · `\b[LNRG][0-9]{1,2}\b` · `\bSR-[0-9]\b` · `\bD-?[0-9]{1,2}\b` · `\bS[1-9]\b`, run with a committed exclusion list (`S\. Ct\.`, §-numbered statutes, docket formats) | `AUTO:LINT-11` fail-closed; a flagged hit clears only via the committed allowlist file, each entry adjudicated under `CHECKLIST:D10` | CI red on any un-allowlisted hit |
| 2 — provenance notes | case-insensitive `\b(re-homed\|moved\|merged\|split\|migrated) from\b` | `AUTO:LINT-11` fail-closed | CI red |
| 3 — status markers | `CL-confirm pending` · `pending CL` · `annotate-only` · `deferred to EXECUTE` · `pending verification` · `\bTODO\b` · `\bTBD\b` · `\bFIXME\b` | `AUTO:LINT-11` fail-closed | CI red |
| 4 — meta-labels | `\(woven in\)` · `No standalone case page` · `placeholder` · `this page intentionally` | `AUTO:LINT-11` fail-closed | CI red |
| 5a — concrete artifact names | `cl-calls\.log` · `S6-SEED` · `RUNBOOK` · `PRACTICES` · `STANDARDS\.md` · `STYLE\.md` · `\.spec\.md` · `\bwrapper\b` | `AUTO:LINT-11` fail-closed | CI red |
| 5b — generic pipeline terms ("data lake", "frontmatter", "lint" used as **our** artifacts) | the words grep, but the disqualifying **intent** ("used as ours") is judgment-only — not honestly lintable | **demoted to `CHECKLIST:D10`**: a grep-assisted review sweep, adjudicated by a reviewer | review finding, not CI |

R14's remaining (non-vocabulary) items map to concrete `AUTO:LINT-3 (extended)` sub-checks, one
each (rev. per Codex re-verify 2026-07-02): **N3/N8 apply-it lists** — every "Apply it" section body
must parse as an ordered list (`^\s*[0-9]+\.` first non-blank line; anything else fails); **N5** —
no `Binding — SCOTUS` label and no wikilink to a SCOTUS-court case page inside a "Recent
developments" section (section-scoped grep against the S2 lake's court field); **brief-first** —
first H2 after frontmatter must be the Brief/Rule section per the R2 section-order table (structural
check); **slip-op pinpoints** — `slip op\.` on any page whose case `date_decided` predates the
current term fails (court/date read from the S2 lake). Each is fail-closed CI red.

### A3 — Trigger lines for R1–R14; R5/R8/R11/R14 Checks concretized (COH-09)

**Decision log.** *Question:* the spec header promises every rule carries **Trigger · Check ·
Enforcement**, but no R-rule has a Trigger, and the R5/R8/R11 Checks are untestable as written.
Narrow the promise, or deliver it? *Alternatives:* (i) narrow the §-promise to the delivered
STANDARDS.md with a note — cheap but leaves the spec internally false for a full planning cycle and
makes execution invent 14 triggers ad hoc; (ii) add Trigger lines now + concretize the three weak
Checks — 14 one-liners, keeps the spec self-consistent, and STANDARDS.md inherits ready-made
triggers. *Pick:* (ii). *Failure mode guarded:* a rule with no firing condition is enforced only by
memory — exactly how the "(woven in)" leak class survived O1 review.

**New normative text — Triggers (each R-rule reads with its line):**

| Rule | Trigger (when the rule fires) |
|---|---|
| R1 | Any edit to `docs/STANDARDS.md`, or any spec/amendment superseding an O1 rule |
| R2 | Any treatment value written or rendered (frontmatter, lake record, badge, hover) |
| R3 | Any case/entry created or re-verified; any reader-facing date rendered |
| R4 | Any legal proposition authored or materially edited |
| R5 | Any AI-generated legal content entering the pipeline |
| R6 | Any doctrine page created or restructured |
| R7 | Any statement of a controlling standard, holding, or test |
| R8 | Any voice pass over explanation prose; any commit touching explanation prose |
| R9 | Any mnemonic used or introduced |
| R10 | Any authority-weight label written |
| R11 | Any term of art used; any rule prose authored |
| R12 | Any legal-assertion review cycle (S9) |
| R13 | Every CI run |
| R14 | Any commit touching `content/` (structure, pinpoints, prose) |

**Concretized Checks (supersede the quoted Check clauses):**
- **R5** — was: "each maps to a pipeline gate or a review dimension." Now: STANDARDS.md carries a
  named **G1–G10 enforcement-map table**; all 10 rows name ≥1 concrete enforcement point (a `LINT-n`,
  a named PRACTICES §6 pipeline gate, or a D-dimension + checklist step); no row reads bare
  "PROCESS". Mechanical check: the table exists, has 10 complete rows.
- **R8** — was: "a lint flags prose em-dashes with a citation-range exemption; carve-outs enforced."
  Now: `LINT-10` exists in `scripts/lint/` and runs in CI; it enforces the A8 density budget over
  explanation prose, excluding direct quotations and controlled labels (per A7); a committed fixture
  file (`scripts/lint/fixtures/lint-10.md`) with known pass/fail paragraphs is exercised by the
  lint's self-test.
- **R11** — was: "a Vale-style prose lint enforces the register; no duplicate rule prose across
  pages." Now: (a) the term register is **machine-readable** (table in `docs/STYLE.md` or
  `scripts/lint/term-register.yml`) and LINT-7-extended consumes it directly; (b) canonical rule
  nodes carry block-ref anchors, and a **duplicate-prose detector** (shingle match ≥25 overlapping
  tokens between rule-layer blocks in different files) fails CI.
- **R14** — was: "the lints (LINT-3 extended) enforce each." Now concretized by the pattern-class
  table in A2 for the broadened vocabulary ban (each class → grep family → LINT-11 or a demoted
  `CHECKLIST:D10` item); the non-vocabulary R14 items keep LINT-3 (extended). *(rev. per Codex
  review 2026-07-02)*

### A4 — Old→new treatment-enum migration mapping (COH-11)

**Extends R2** (no text superseded; the mapping the spec lacked). Old lexicon = `docs/STANDARDS.md`
§3.1: `good | criticized | limited | abrogated | overruled`. Live frontmatter (457 case pages,
counted 2026-07-02): 439 `good` · 11 `limited` · 5 `overruled` · 2 `abrogated` · 0 `criticized`.

| Old `treatment.status` | Count | New Field-I composite (PRACTICES §2) | Edge / override handling |
|---|---|---|---|
| `good` | 439 | `good_law` 🟢 | No edge required; old `as_of` seeds `as_of_treatment`; S2 R6 re-derives and may downgrade |
| `limited` | 11 | `caution` 🟡 | **Mandatory ≥1 `point_overrides[]`** on the limited point; override Field-II = `limited` (or `superseded` where replaced outright — e.g. *Belton*→*Gant*, the S2 R5 worked specimen); `varies_by_point: true` |
| `overruled` | 5 | `superseded/not_current` 🔴 | Field-II `overruled` edge to the overruling case; authority-weight moves to tier 6 (Historical) per §3.1's carried rule |
| `abrogated` | 2 | `superseded/not_current` 🔴 | Field-II `abrogated` edge (*Aguilar*/*Spinelli* → *Illinois v. Gates*) |
| `criticized` | 0 | `caution` 🟡 (default) | Escalate to `questioned/overruling_risk` 🟠 only when the negative treatment hits the **relied-on point** in a **binding jurisdiction** (PRACTICES §2 red-flag rule) |

The 11 `limited`: *Boyd, Coolidge, Escobedo, Mathis (1968), Monroe v. Pape, Belton, Elstad, Saucier,
Thornton, Agurs, Chadwick*. The 5 `overruled`: *Gouled, Jones (1960), Michigan v. Jackson, Olmstead,
Wolf*. The 2 `abrogated`: *Aguilar, Spinelli*.

**Point-level override rule:** any case bad on **fewer than all** taught points gets a composite that
reflects its **principal holding** plus `point_overrides[]` for the divergent points (S2 R5); if the
principal holding itself is the dead point, the composite is `superseded/not_current`. **No migrated
case maps to `unverified` ⚪** — ⚪ is reserved for records never O1-verified (frontier stubs); the 457
keep their seeded value + O1 `as_of` until S2's derivation re-stamps them.

**Consumption:** this table is the **only** sanctioned old→new translation. **S2's projector consumes
this table** to seed Field-I; S2 R6's three-lane derivation then confirms or adjusts; the mapping
alone never yields `verified`. S5 renders from the projected values downstream.

### A5 — Lint naming standardized: numeric LINT-9…N series (COH-21)

**Extends R13** (no text superseded; resolves the numeric-vs-`LINT-S2-*` fork). The **numeric
`LINT-<n>` ID is canonical**, continuing O1's LINT-1…8; a descriptive alias in parentheses is
permitted on first mention. Reserved numbers:

| ID | Name | Origin |
|---|---|---|
| LINT-9 | carat-leak (`^pin-N`) | R13 (already assigned) |
| LINT-10 | prose em-dash budget | R13/A8 (already assigned) |
| LINT-11 | pipeline-vocab | **new** — the broadened-R14 lint (A2); S9 implements |
| LINT-12 | lake↔frontmatter drift | = S2's `LINT-S2-drift` |
| LINT-13 | lake schema | = S2's `LINT-S2-schema` |
| LINT-14 | page↔record publish gate | = S2's `LINT-S2-pagerecord` |

`LINT-S2-*` names are **deprecated aliases**; the S2 spec's text still uses them on disk — the
re-pointing to LINT-12/13/14 is codified at S9 with the lint-roster build (register COH-21,
injected:S9; rev. per closure verification 2026-07-02). Term-register enforcement **stays on LINT-7 (extended)** per R11/R13 —
the audit's provisional "LINT-12 register/term drift" label is realized as LINT-7-extended plus
LINT-12 (drift), because R11 already numbers the register lint and a second number would recreate
the fork this amendment removes. S9 codifies the full roster; LINT-3 precision work (COH-28) remains
S9's.

### A6 — Glyph fork resolved: `⚪` canonical, U+2B58 forbidden (COH-20)

**Supersedes (§7 acceptance criterion):** "`⭘ unverified` gate present (R2/R3)."

**New normative text:** the unverified glyph is **`⚪` (U+26AA MEDIUM WHITE CIRCLE)** everywhere —
specs, STANDARDS.md, frontmatter, badges, hovers. **U+2B58 HEAVY CIRCLE is forbidden.**
*Rationale:* `⚪` is the majority usage (PRACTICES §2, S2 R5, S1 R2 itself — the U+2B58 at the
acceptance line was the lone outlier) and belongs to the same emoji set as its siblings
🟢🔵🟡🟠🔴, so the six render uniformly across platforms and fonts; U+2B58 has patchy font coverage
and can render as tofu in tables and badges. LINT-6 (extended) treats U+2B58 as an invalid glyph.
**Carve-out (rev. per Codex review 2026-07-02):** the old glyph may appear only in quoted superseded
text within Amendments (the quote above is the sole permitted site); the spec body — including the
§7 criterion — has been swept to `⚪`, and all other references to the forbidden character use its
codepoint name, never the literal glyph.

### A7 — LINT-10's exemption restated correctly (COH-22)

**Supersedes (R8 Check + §7 acceptance wording):** "a lint flags prose em-dashes with a
**citation-range exemption**."

**New normative text:** citation ranges ("392 U.S. 1, 21–22") use **en-dashes (U+2013)**; LINT-10
targets **em-dashes (U+2014)**, so a "citation-range exemption" is vacuous — the lint never sees an
en-dash. What LINT-10 **actually exempts**: **(a) em-dashes inside direct quotations** from opinions
or other sources (quoted text keeps its original punctuation, per the Appendix A NEVER-APPLY
carve-out); **(b) controlled labels that contain em-dashes** ("Binding — SCOTUS",
"Persuasive — state, illustrative"). R8's "KEEP en-dashes in citation/page/date ranges" survives
unchanged as a **style rule** — it is not a lint exemption. Optional extension for the S9 roster:
flag an em-dash or hyphen used where a range en-dash belongs inside a citation string.

### A8 — Em-dash policy: S7 rewrite pass + density budget; weight-label order canonical (TEACH-05/TEACH-06 policy · TEACH-04d rule)

**Extends R8 and R10** (records the adjudicated policy; supersedes nothing beyond the Check additions).

**Em-dash decision.** *Question:* R8 bans the em-dash habit, but the audit measured 26–43 em-dashes/1k
words (~1,100 hits in an 11-page sample) — enforce by lint alone, or rewrite? *Alternatives:* (a)
zero-tolerance lint — ~1,100 findings swamp review and the ban degrades to noise; (b) budget lint
with no rewrite — the corpus stays over budget and CI is permanently red; (c) **S7 performs a
REWRITE pass** to bring prose under budget, then LINT-10 guards the steady state. *Pick:* (c).
*Failure mode guarded:* alarm fatigue — a permanently-red lint teaches everyone to ignore lints.
**The budget:** **≤1 em-dash per paragraph; never 2+ in one sentence; direct quotations and
controlled labels exempt** (excluded from counts, per A7). LINT-10 enforces the budget fail-closed
(per-paragraph/per-sentence, not per-instance). The corpus-wide rewrite itself is S7 work
(register TEACH-05).

**Weight-label order (adds to R10's Check):** the canonical format is **tier word first, qualifier
after the em-dash** — "Binding — SCOTUS", "Binding in-circuit — 9th Cir." The inverted form
("SCOTUS — binding"; 21 live instances vs 1,761 canonical) is **forbidden**; LINT-4 flags any weight
label whose tier word follows the em-dash. Fixing the 21 is S7 work (register TEACH-04d).

**Exact allowed label strings (rev. per Codex review 2026-07-02).** The complete allowlist — all six
tiers, **spaced em-dash form** (` — `). R10's body listing (which shows unspaced dashes) is
**superseded on spacing** by this allowlist:

1. `Binding — SCOTUS`
2. `Binding in-circuit — <circuit>` (circuit suffix mandatory per R10's name-the-circuit rule,
   e.g. `Binding in-circuit — 9th Cir.`)
3. `Persuasive (outside circuit) — <circuit>` (suffix mandatory — the label is definitionally a
   circuit case)
4. `Persuasive — state, illustrative`
5. `Persuasive only — non-precedential`
6. `Historical`

`<circuit>` matches `(1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|D.C.|Fed.) Cir.` **LINT-4 is
extended to validate every weight label against this allowlist exactly** — inversions, unspaced
dashes, en-dash or hyphen in place of the em-dash, and case variants all fail; the lint is no longer
inversion-only.

### A9 — Paragraph-density budget for the Brief (TEACH-07)

**Extends R14** (new style rule; supersedes nothing). The Explanation layer ("the Brief") must not
stack case walls (audit specimens: 200–250-word paragraphs at Two Definitions :29/:31, Warrant
Requirement :46). **Budget:** **one doctrinal move per paragraph; ~5-sentence soft cap; any paragraph
invoking more than 3 cases converts to labeled bullets** (bolded case name + one-line role).
- *Trigger:* any Explanation-layer prose authored or edited. *Check:* mechanical density counts
  (sentences per paragraph; case-name mentions per paragraph) via script — soft-cap breach = review
  flag, >3-case stacking = hard flag. *Enforcement (rev. per Codex review 2026-07-02 — split, so the
  "hard rule" label matches its mechanism):* the **>3-cases-per-paragraph check is fail-closed**
  (`AUTO`, S9 roster) — case mentions per rendered paragraph are mechanically countable via wikilink
  density, so fail-closed costs no judgment; the one-move-per-paragraph and ~5-sentence soft cap
  remain **advisory** (`CHECKLIST:D9` + advisory lint — paragraphing is prose judgment).
