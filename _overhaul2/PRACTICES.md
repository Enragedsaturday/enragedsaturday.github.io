# CSSI O2 — Editorial & Verification Practices

*The professional playbook every O2 spec thread inherits. Distilled from five external research
threads (2026-07-01) on how authoritative legal references are actually produced and verified —
legal treatises, legal encyclopedias, the ALI Restatements, law-review cite-checking, magazine
fact-checking, and docs-as-code. Full citations live in the five research reports; the load-bearing
sources are named inline. This governs S1 (Standards) and is enforced by S9 + the CI lints.*

---

## 1. The convergent principles (all disciplines agree)
1. **The taxonomy IS the product.** One controlled classification is the spine; each rule/term is
   stated **once** and reused (transcluded), never re-paraphrased across pages, or copies drift.
   *(West Key Number System; docs SSOT/DITA; encyclopedia scope-notes.)*
2. **Separate the RULE from its SUPPORT and gate them differently.** *(ALI black-letter vs.
   Reporter's Notes; West opinion-text-is-authority, headnotes-are-not.)*
3. **Verify per-assertion, writer ≠ checker, fail-closed.** "Unmarked = unverified." The agent that
   wrote a claim cannot approve it. *(Magazine fact-checking; law-review subcite; docs PR review.)*
4. **Currency is a first-class, VISIBLE field.** Derived content lags primary law; show how current.
5. **Subsequent treatment is a controlled vocabulary — and a red flag is a CLUE, not a verdict**
   (read whether the negative treatment hits *your* point).
6. **Comprehensiveness has explicit stopping rules** (saturation / closed citation loop).
7. **One style manual + controlled vocabulary + automated enforcement** (Bluebook; style sheet; Vale).
8. **Staged draft states + multi-reviewer approval before "the law" ships.**
9. **An owned maintenance loop keeps it current after launch** (→ GH issue #2, deferred).
10. **Engineer against OUR failure mode.** AI legal drafting has a documented sanction record
    (1,300+ matters; *Mata v. Avianca* → precedential 9th-Cir. *LNU v. Blanche*); even RAG tools
    hallucinate 17–33% (Stanford RegLab). Grounding is necessary, **not sufficient**.

---

## 2. The three-field treatment vocabulary (replaces single `treatment.status`)
Modeled on Shepard's / KeyCite / BCite. Each case/proposition carries three orthogonal fields + an
**as-of date**. CL provides **none** of this natively (see `CL-DATA-INVENTORY.md` §Treatment) —
derive it from progeny opinion text + web search.

**Field I — Validity status** (one composite per case, scoped to a point of law):
`good_law` 🟢 · `history/neutral` 🔵 · `caution` 🟡 · `questioned/overruling_risk` 🟠 ·
`superseded/not_current` 🔴 · **`unverified` ⚪ (AI-native — never reaches a reader unbannered).**

**Field II — Treatment tag** (per citing case): `overruled` · `abrogated` · `superseded_by_statute`
· `limited` · `distinguished` · `criticized` · `questioned` · `modified` · `followed` · `explained`
· `reaffirmed` · `expanded`. *(Our "expansion/narrowing/interpretation" map.)*

**Field III — Depth** (per citing case): `examined` · `discussed` · `cited` · `mentioned` ·
`quoted`. On the free stack (no KeyCite stars) approximate by discussion length.

**Rules:** a red flag is a **clue** — mark `not_current` only when a negative Field-II tag hits the
**specific point relied on** in a **binding jurisdiction**, never on color alone. Every case gets one
Field-I + an as-of date; every material citing edge gets a Field-II + Field-III.

---

## 3. Per-proposition verification protocol (the professionalized "two-key," 10 gates)
A hybrid of the law-review cite-check (forward substantiation) + the citator check (backward
validity). Record PASS/FAIL/FLAG per gate; a proposition is VERIFIED only when all applicable gates pass.

**KEY 1 — Substantiation:** **G1** existence (locate exact authority) · **G2** support (the source
*actually stands for* the proposition; the signal/parenthetical matches) · **G3** quote fidelity
(verbatim string-match against source text) · **G4** pincite (the language is on the cited page) ·
**G5** form (Bluebook/house-style complete).

**KEY 2 — Validity:** **G6** direct history (not reversed/vacated/superseded in its own line) ·
**G7** citator/derived status recorded · **G8** on-point treatment (read the negative progeny; does
it strike *this* point?) · **G9** jurisdiction + a stated **validated-through date** · **G10**
independent corroboration (cross-check a 2nd source for load-bearing propositions).

**Governance:** one tracked row per proposition-source pair; an independent reviewer re-verifies **≥1
in 10** (escalate on any error found); two-person rule for anything tagged negative; preserve links.

---

## 4. Comprehensive-research protocol (the "expansive search," made defensible)
Use **CourtListener AND web search together** — CL has real coverage gaps, and web search surfaces
**terminology, legal theories, and adjacent keywords** that reframe the search and drive proper
expansion (per the user). Progressive & self-learning: narrow issue → doctrine/keyword → expand →
learn → expand (bounded).

**Six phases:** (0) frame with TARP + fix jurisdiction → (1) orient in secondary sources (Wex,
law-review via Scholar, FLETC, our own pages) → (2) anchor the controlling primary authority (CL,
dated, with pinpoint) → (3) **expand** (forward-chain `cites:(<ids>)`; backward-chain
`opinions_cited`; rule-phrase full-text sweep as the key-number proxy; circuit-split/first-impression
sweep — `"circuit split"`, `"decline to follow"`, `"first impression"`; **web-search sweep for
terminology/theory**; cross-check a 2nd tool) → (4) validate/update (derive treatment; assign the
6-tier weight; date the good-law status) → (5) **saturation stop**.

**STOP only when all true:** new searches surface only cases already seen · the core authorities cite
back to each other · both directions run on every key case · every circuit accounted for (or a split
flagged) · no unaddressed `"first impression"`/"we have not decided" in the newest cases · a 2nd tool
cross-checked · adverse/limiting authority captured (anti-cherry-pick) · further reading adds nothing.

Free-stack reality (state honestly): no key-number index, no depth-of-treatment stars → approximate
via rule-phrase search + reading discussion length.

---

## 5. The graded-authority entry model (ALI Restatement pattern)
Split each doctrine entry into layers gated differently:
- **Black-letter rule** — the doctrinal statement, the *only* thing published *as* "the law";
  requires **≥2 independent reviewers** to approve (our 1 Claude + 2 Codex panel).
- **Explanation / field application** — reviewed; the teaching brief. **Human-in-the-loop** for any
  "officer bottom line"/BLUF summarization — these drift on the controlling *standard* (emergency aid
  is an **objectively reasonable belief**, NOT "sees someone in imminent danger"). Never auto-generate
  the standard; ground it verbatim in the opinion.
- **Authorities & notes** — attributed, lighter-weight; the supporting cases + our evaluation.

Only primary-source opinion text is authority; our summaries orient but every load-bearing statement
pins to a primary source. Where courts split, state the split; if we pick a rule, say so and why.
**Draft states:** `draft → under_review → verified` — only `verified` is presented as settled.

> **S1/S5 interview deliverable:** mock up **two variants** — full ALI black-letter/explanation/notes
> vs. a lighter "verified rule + supporting notes" — and choose on the mockup.

---

## 6. AI-verification guardrails (G1–G10, pipeline gates, fail-closed)
We are the AI courts sanction people for trusting, so these are enforced, not advisory:
1. **Retrieval-grounded only** over vetted primary sources — never parametric recall/open web.
2. **No legal proposition without a verified primary-source pincite** + parenthetical → blocked from publish.
3. **Automated citation-existence check, fail-closed** (via `analyze_citations`): "not found" →
   **block + investigate** (cross-check a 2nd source), never auto-delete; name/citation mismatch →
   presumptively fabricated (**compare input name vs CL canonical ourselves** — the auto warning is
   masked by cite dedup).
4. **Quote-fidelity string-match** against retrieved source (`search_document`).
5. **Holding-support check** — the cited page supports the proposition (2nd pass).
6. **Treatment/currency check before publish** — overruled/abrogated cannot be presented as current.
7. **Separation of drafting from verification** — generator ≠ verifier; no self-certification.
8. **Human sign-off** for anything reader-facing/legally operative; recorded.
9. **Immutable provenance/audit trail** per assertion (prompt, model+version, retrieved sources,
   timestamp, verification results, verifier identity, approval/override).
10. **Dual as-of dating + re-verification cadence** — re-run G3/G4/G6 on a schedule (→ maintenance loop).

---

## 7. Reader-facing signaling scheme
- **Treatment flag** per authority (Field-I), **scoped to the point of law**, not the whole case.
- **Dual "as-of" dates** — `content_verified` + `treatment_checked` (decay independently). **Placement
  decision (user, 2026-07-01):** keep the dates in the **data model + behind a hover + on the About
  page** — do NOT litter them inline on every assertion.
- **Provenance** — every proposition traces (pincite → linked primary source → parenthetical →
  verification badge); "don't assert — link."
- **Overruled/superseded cases shown as HISTORY, never deleted, never disguised:** precise verb
  ("Overruled by …" / "Abrogated by …" / "Superseded by statute …"), visual demotion, scope the
  warning to the affected point, and a **forward-pointer to the successor** authority.

---

## 8. Consistency machinery (style manual + term register + CI)
- A committed **`STYLE.md`** (house style + controlled term vocabulary), precedence stack
  (project rules → legal citation manual → Chicago), with the "depart-when-it-improves-but-stay-
  consistent" escape valve.
- A **living term register** (canonical spelling/definition per term of art) — machine-enforceable.
- **Single source of truth** — each rule/term is a canonical node, transcluded (Quartz embeds), never
  restated.
- **Automated CI, fail-closed on every change:** prose linting for the term register (Vale-style) +
  markdown structure + **link/citation checks** (dead wikilink or unresolvable cite blocks publish) +
  the `^pin-N` carat-leak check (block-ref anchors must NOT render as visible text) + build. Extends
  the existing `scripts/lint/` roster.
