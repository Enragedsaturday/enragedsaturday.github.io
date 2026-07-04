# CSSI — STYLE (the house style manual)

status: GOVERNING (style authority) · companion to `docs/STANDARDS.md` (the contract)
derived-from: `_overhaul2/specs/S1-standards.spec.md` R8–R11 + Appendices A/B + Amendments A6–A9
last-updated: 2026-07-04 (O2 EXECUTE Wave 0)

This manual governs **how prose is written**; `docs/STANDARDS.md` governs **what must be
true**. Voice rules here apply to **explanation prose only** — never to quoted opinions,
black-letter rules/holdings/standards, citations/case names, or controlled labels (the
NEVER-APPLY carve-outs, §3).

---

## 1. Precedence stack

On any style question, resolve in this order:

1. **Project rules** — this manual + `docs/STANDARDS.md` (the term register, the lexicon
   allowlist, the treatment vocabulary, the mnemonic register).
2. **Legal citation manual** — Bluebook conventions for citation form (gate G5).
3. **Chicago Manual of Style** — everything else.

**Escape valve:** depart when departing clearly improves the reader's understanding — but
stay consistent: a sanctioned departure is recorded here (or in the term register) so the
whole corpus departs the same way. Unrecorded one-off departures are style defects.

---

## 2. House style (the core rules)

- **Legal register, instructor voice.** Direct, precise, plain-English teaching prose.
  Write for a working officer-instructor: no academic throat-clearing, no chattiness.
- **Repeat the exact term** — never cycle synonyms for a term of art. The drift
  *stop → detention → seizure* changes the law mid-paragraph. (Register, §4.)
- **Legal modality is load-bearing.** Keep *may / must / shall / reasonable / objectively
  reasonable / articulable* exactly as the doctrine states them; reducing rhetorical hedging
  never licenses touching these.
- **Correct legal passives stay.** "The evidence was suppressed" is right when the actor is
  the court and the emphasis is the evidence; prefer active voice elsewhere.
- **Numbered tests stay numbered.** Real N-prong tests and "apply it" sequences are ordered
  lists (STANDARDS N3); never flatten them to prose to "improve flow."
- **Hyphenation of terms of art is doctrine, not decoration:** *good-faith exception*,
  *stop-and-frisk*, *bright-line rule*, *knock-and-talk*, *plain-view doctrine* (as
  modifiers). Never de-hyphenate. (Register, §4.)
- **Capitalization:** legal headings keep standard heading case; case-derived terms keep
  the case capital (*Terry* stop, *Miranda* warnings, *Franks* hearing).
- **Em-dash policy (the A7/A8 rule):**
  - Budget: **≤1 em-dash (—, U+2014) per block** (paragraph or list item); **never 2+ in
    one sentence**. Enforced fail-closed by LINT-10.
  - **Exempt from the count:** em-dashes inside **direct quotations** (quoted text keeps
    its original punctuation) and inside **controlled labels** ("Binding — SCOTUS",
    "Persuasive — state, illustrative").
  - **En-dashes (–, U+2013) in citation/page/date ranges are correct and required:**
    "392 U.S. 1, 21–22". This is a style rule, not a lint exemption — LINT-10 targets
    em-dashes only and never sees an en-dash. Never substitute an em-dash or hyphen where
    a range en-dash belongs inside a citation string.
- **Paragraph density (the Brief):** one doctrinal move per paragraph; ~5-sentence soft
  cap; a paragraph invoking **more than 3 cases** converts to labeled bullets (bolded case
  name + one-line role). No case-wall paragraphs.
- **Treatment glyphs:** 🟢 🔵 🟡 🟠 🔴 ⚪ — the six Field-I glyphs (STANDARDS §3.1). The
  unverified glyph is **⚪ U+26AA everywhere; U+2B58 is forbidden** (patchy font coverage
  renders it as tofu; LINT-6 flags it). These are controlled signals, not decoration; no
  other emoji in reader-facing prose.
- **Weight labels:** exact-allowlist strings only (STANDARDS §3.0); tier word first,
  qualifier after the spaced em-dash; circuit suffix mandatory on tiers 2–3.
- **Dates:** reader-facing as-of dates live in the data model, hovers, and the About page —
  never inline on assertions (STANDARDS SR-6). Table cells count as inline.
- **No editorial-pipeline vocabulary in reader-facing prose** (STANDARDS SR-11/§7.3): no
  rule/lint identifiers, re-homing notes, status markers, meta-labels, or internal artifact
  names. Persistent state goes in HTML comments or frontmatter keys.

---

## 3. The Humanizer voice subset (ADOPT / ADAPT / REJECT)

The voice pass applies to **explanation prose ONLY**.

**ADOPT (apply fully):**
- Ban AI-vocabulary: *delve, tapestry, testament, landscape, underscore, leverage,
  crucial, pivotal, foster, robust, navigate (figurative), realm, harness, unlock…*
- Cut filler: *in order to* → *to*; *it is important to note that* → (delete); *serves to* →
  (the verb).
- Kill significance-inflation and promo adjectives (*groundbreaking, critical insight,
  powerful framework*).
- Cut "-ing" padding openers (*Building on this…, Recognizing that…*).
- No chatbot tics: no sycophancy, no cutoff disclaimers, no "as an AI."
- No signposting or fake candor (*Let's be clear, To be honest, Importantly,*).
- No staccato drama (one-word sentences for effect) and no false ranges (*from X to Y*
  where X and Y aren't ends of a real spectrum).
- **Don't cycle synonyms — repeat the exact term** (= term-of-art discipline, §4).
- Vague attribution → dated/specific source ("courts have held" → name the case).

**ADAPT (apply with the legal carve-out):**
- Reduce rhetorical hedging, but **keep legal modality** (*may/must/reasonable/objectively
  reasonable/articulable*).
- Prefer active voice, but **keep correct legal passives**.
- Avoid rule-of-three padding, but **keep real N-prong tests**.
- Kill "not just X, it's Y" constructions, but **keep genuine doctrinal contrasts**
  (holding vs. dictum; rule vs. exception).
- Strip decorative emoji, but **keep the treatment-status glyphs** (§2).
- **Em/en-dashes:** cut the em-dash habit in prose (budget, §2); **keep en-dashes in
  citation/page/date ranges.**

**REJECT (conflicts with legal writing):**
- De-hyphenating terms of art (*good-faith → good faith* as a modifier). Never.
- Converting numbered tests / apply-it lists to prose. Never.
- Lowercasing legal headings or case-derived capitals. Never.

**NEVER APPLY (hard carve-outs — the voice pass does not touch):**
- Inside a quoted opinion or any direct quotation.
- On a black-letter rule, holding, or standard (Layer 1 text).
- On citations or case names.
- On controlled labels (weight labels, treatment tags, glyphs).

---

## 4. The term register

**The machine-readable register is `scripts/lint/term-register.yml` — the single source of
truth.** This section states the rules; it never duplicates the list (SSOT — two copies
drift).

- Each register entry fixes the **canonical spelling** of a term of art; listed
  **banned variants fail CI** (LINT-7, fail-closed; hits inside direct quotations are
  exempt — quoted sources keep their spelling).
- **Drift sets** name the siblings a term must never silently slide into
  (*probable cause ↛ reasonable suspicion*; *seizure ↛ stop ↛ detention*). Not machine-
  enforced — reviewer judgment (CHECKLIST:D5).
- Every non-vernacular term links to `Common Legal Terms` (STANDARDS N11); the register's
  `glossary:` field names the target anchor. **Definitions live once, in the glossary** —
  the `glossary:` binding is how a register entry meets R11's "canonical
  spelling/definition" pair without duplicating definition text (definition coverage +
  anchor resolution are enforced from the S8 glossary audit onward).
- **Single-source transclusion (STANDARDS SR-14):** each rule/term is stated once as a
  canonical block-ref-anchored node and transcluded (`![[…]]`) everywhere else — never
  re-paraphrased. The shingle detector (≥25 overlapping tokens) fails CI on raw
  restatements.
- **Growing the register:** additions land in the YAML with `canonical`, optional
  `banned_variants`, `glossary`, `note`; the S7/S8 glossary audit feeds it. Removals
  require a logged reason.

---

## 5. The mnemonic register (verified; verbatim; uncited)

Only these devices are permitted, **verbatim**, never citation-attached (a mnemonic is a
teaching device, not an authority — attaching a cite launders it into one). LINT-8 enforces
the register, including **wikilink-target checks** (a mnemonic's link target must exist and
match the register entry).

| Device | Wording | Fits |
|---|---|---|
| **C.R.E.W.** (3 justifications) | **C**onsent · **R**ecognized **E**xception · **W**arrant (exigency is one example *inside* RE, not a fourth item) | CREW / "what is a search" intro; exceptions overview |
| **N.E.R.D.S.** | Bandiero's report-writing acronym | Instructor craft / report-writing |
| **Three Golden Rules** | (1) articulate the *why* → more likely upheld (*Terry*); (2) more serious crime/circumstance → more reasonable (*Graham*); (3) 4A deals in **probabilities, not possibilities** (*Brinegar*/*Gates*) | Instructor craft; woven where apt |
| **Strive for Five** | Articulation drill — name ≥5 facts, "opinion first, then because →"; not a 5-factor test | Reasonable suspicion / articulation |
| **Hot / fresh pursuit** | "Hot pursuit = hot on the suspect's tail; fresh pursuit = fresh on the trail" | Exigency / hot pursuit |
| **Dominoes (Decision Sequencing)** | Unlawful step taints what's derived after it; what's found *before* the first fallen domino survives. **Credit Bruce-Alan Barnard.** **Guardrail:** oversimplifies — attenuation / independent source / inevitable discovery mean not every later domino falls. | Fruit of the poisonous tree |
| **Rubber band** | The 4A "stretches" for violent/urgent/fast-moving situations. **Guardrail:** a reasonableness *multiplier, not a warrant bypass.* | Three Golden Rules R2; reasonableness |
| **"Worthless alone → totality"** | Individual factors mean little in isolation; build the totality. | Reasonable suspicion (pairs with Strive for Five) |
| define/attribute only | "right to be left alone" = **Brandeis, *Olmstead* dissent** (not Bandiero) | Katz / REP |

**Removed:** ~~CRON~~ — a dictation error; no such Bandiero mnemonic exists. Never
reintroduce it. **CREW is three justifications, never four** (no four-way CREW).

**Guardrails:** mnemonics appear verbatim (no paraphrase, no expansion); never
citation-attached; each is used only where its "Fits" column places it; a device carrying
its own guardrail note teaches the guardrail with it.

---

## 6. Citation style notes

- Bluebook form (gate G5); reporter cites with en-dash page ranges ("392 U.S. 1, 21–22").
- **Slip-opinion pinpoints only for the current SCOTUS term** (STANDARDS SR-12); everything
  older cites the reporter.
- Circuit abbreviations in weight labels: `1st|2d|3d|4th|5th|6th|7th|8th|9th|10th|11th|
  D.C.|Fed.` + `Cir.` (the allowlist regex).
- Sources sections use the **bracketed-link format**; trailing info is **parenthesized**,
  never em-dashed (S5 R12).
- Quotations are verbatim (gate G3) — including their original punctuation; never "fix" a
  quote's style.

---

*End of STYLE.md. The machine-readable term register lives at
`scripts/lint/term-register.yml`; the treatment vocabulary and lexicon allowlist live in
`docs/STANDARDS.md` §3.*
