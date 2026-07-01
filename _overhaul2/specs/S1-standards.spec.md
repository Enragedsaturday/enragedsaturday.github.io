# SPEC S1 — Standards & Style Manual

status: APPROVED
depends-on: []   gates: [S2, S3, S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-01

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

**R1 — Carry the O1 architecture forward.** `STANDARDS.md` retains: the Trigger/Check/Enforcement rule
format; scar-rules **L1–L8**, mechanism-rules **N1–N13**, standard-rules **SR-1…SR-5**; dimensions
**D1–D14**; the LINT-1…8 roster; the find→adjudicate→fix machine; DECISIONS D-0…D-8. *Check:* every O1
rule present and unchanged **unless** explicitly superseded by R2–R14. `PROCESS`.

**R2 — Treatment = the 3-field vocabulary (replaces single `treatment.status`).** Adopt PRACTICES §2:
Field I validity status (`good_law/history/caution/questioned/superseded/**unverified⚪**`), Field II
treatment tag (~12 values), Field III depth — each scoped to a point of law + an as-of date; "a red
flag is a clue, not a verdict." Rewrite STANDARDS §3.1 / N4 / N13. *Check:* the single-axis status is
gone; `⚪ unverified` can never render to a reader unbannered. `AUTO:LINT-6` (extended) · `CHECKLIST:D3`.

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

**R9 — Mnemonic register (verified; verbatim; uncited).** The permitted set + where each fits +
guardrails (Appendix B). **C.R.E.W.** = three justifications, **C / RE (Recognized Exception) / W** —
exigency is one example *inside* RE, not a fourth item. **"CRON" is removed** (a dictation error).
*Check:* mnemonics appear verbatim, never citation-attached; no four-way CREW; no CRON. `AUTO:LINT-8` ·
`CHECKLIST:D11`.

**R10 — Authority-weight lexicon (carry verbatim).** The 6 tiers (Binding—SCOTUS · Binding in-circuit
· Persuasive (outside circuit) · Persuasive—state, illustrative · Persuasive only—non-precedential ·
Historical); **"persuasive, not binding" banned**; circuit cases name the circuit; splits flagged.
*Check:* only these labels site-wide. `AUTO:LINT-4` · `CHECKLIST:D6`.

**R11 — Term register + single-source transclusion.** STYLE.md carries a controlled word list (canonical
spelling/definition per term of art); each rule/term is stated **once** as a canonical node and
transcluded, never re-paraphrased (PRACTICES §8). Term-of-art consistency: never drift *stop→detention→
seizure*. *Check:* a Vale-style prose lint enforces the register; no duplicate rule prose across pages.
`AUTO:LINT-7` (extended) · `CHECKLIST:D5`.

**R12 — Reviewer panel + machine ledger (standard-setting; mechanics in S9).** Legal assertions are
reviewed by **1 Claude + 2 Codex** with a **≥2-of-3 refute tally**; findings→adjudications→fixes→
inventory are **machine-emitted and reconcilable**. *Check:* STANDARDS §6/SR-4 states this; S9 implements.
`PROCESS`.

**R13 — Lint roster extended.** Add **LINT-9** (`^pin-N` carat-leak: block-ref anchors must not render
as visible text), **LINT-10** (prose em-dash with citation-range exemption); extend **LINT-4**
(lexicon incl. weight labels) and **LINT-6** (treatment → 3-field); add fail-closed **link/citation
resolve** + **term-register** checks. All run in CI, fail-closed. *Check:* roster documented in
STANDARDS §7. `AUTO`.

**R14 — Content-structure rules (carry + tighten).** Numbered "apply-it" lists (N3/N8); **no internal
meta-labels in prose** (kill "(woven in)"); **no SCOTUS case in "Recent developments"** (N5); tests/
prongs stated up front in the Rule (N3); brief-first (N8); **slip-op pinpoints only for the current
Supreme Court term** (else a reporter pinpoint). *Check:* the lints (LINT-3 extended) enforce each.
`AUTO:LINT-3` · `CHECKLIST:D10`.

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
- [ ] 3-field treatment + dual dates replace single status; `⭘ unverified` gate present (R2/R3).
- [ ] 10 gates + AI guardrails codified as testable rules (R4/R5).
- [ ] Graded-authority Variant A template present; no field-application summary (R6).
- [ ] Humanizer subset in STYLE.md; prose em-dash lint with citation-range exemption; carve-outs (R8).
- [ ] Mnemonic register verbatim; CREW = 3 justifications; no CRON (R9).
- [ ] 6-tier lexicon verbatim; "persuasive, not binding" banned (R10).
- [ ] Term register + single-source transclusion rule (R11).
- [ ] Lint roster extended (LINT-9/10 + updates), CI fail-closed (R13).
- [ ] Content-structure rules incl. slip-op-current-term-only (R14).

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
