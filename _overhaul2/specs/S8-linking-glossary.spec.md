# SPEC S8 — Legal-Term & Case Linking + Glossary

**Status: APPROVED (signed at interview, 2026-07-04).**
gates: S2 (canonical names + frontier stubs + cached opinion text), S4 (popover/anchor mechanism),
S6 (R11 coverage ledger — the caption authority), S7 (final prose — the text linked over).
Authoring order only; execution = wave 3, **after S6 and S7** (RUNBOOK §3, COH-04).

Interview: 2026-07-04 (3 rounds + open floor; 8 user decisions D1–D8, two pivoted live on the
mockup) + visible self-interview (SD1–SD10, full text in the thread).
Exhibits (all live on the branch, served on :8080): **Knock and Talk** at signed density — mockup
commits `981b286` + `baa1e17` (split pincite) + `5b48d85`/`5d747f9` (landing behavior) —
**the normative density reference**; **Curtilage** — the rule-node embed + pinned-quote embed
(commits `981b286` + `51e1f4b`); **Florida v. Jardines** / **United States v. Walker** /
**United States v. Lundin** — external `#:~:text=` fragment pincites + the mid-line-pin
remediation exhibit.

Precedence: this spec wins over RUNBOOK §4-S8 and the S8 wrapper (RUNBOOK §0 stack).

---

## 1. Objective

Wire the finished corpus into one navigable web: every case mention anywhere — full caption or
short name — resolves to its case page (deep to the pin block when a pinned passage is being
discussed); every pincite on a verified quote jumps out to the opinion with the quoted text
highlighted; every term of art routes to its one home (doctrine page, glossary, or
citation-mechanics page) at every occurrence; every cross-page rule statement and block quote is a
transclusion of its single canonical source, never a restatement; and the glossary is audited and
expanded from S7-final text. Every action is ledgered so the 388-mention reconciliation (COH-15)
is a machine join, not a prose claim.

## 2. Scope

### 2.1 In scope (S8 owns)
- The corpus-wide **case-mention link pass** (R1–R3): full captions + short names, the
  ambiguity-resolution protocol, the no-page/plain rule against the S6 ledger.
- The **split pincite convention** (R4) + **external text-fragment generation** from verified
  pinpoint quotes (R5), including the lake write-back of validated fragments.
- **Pin-anchor remediation** (R6): the mid-line `^pin-N` class (NUM-03's content half, adapted
  here from S9 — see Decision Log) so every pin is a real block anchor before deep links wire.
- The **term link pass** (R7): four-way routing at every-occurrence density; the routing columns
  in the S1 term register; the vernacular skip-list.
- **Glossary audit + expansion** (R8) from S7-final text.
- **Transclusion** (R9): rule-node and pinned-quote embeds; the shingle-detector boundary; the
  full-slug embed grammar.
- The **landing-highlight mechanism** (R10) — flash + persistent tint, centered landing.
- **Table pipe-escaping** (R11, NUM-02) and the **exemption-zone catalog** (R2).
- The **S8 link ledger** (R12) + the LINT-5/LINT-7 rewrites and the new checks S9 wires (R13).

### 2.2 Out of scope (owned elsewhere)
- Authoring case pages or verifying existence (**S6**; S8 never mints a page and never links a
  caption the ledger calls `removed`/`unverifiable`). Doctrine prose itself (**S7** — S8 adds
  links/embeds/anchors, never rewrites sentences; a wording defect found mid-pass routes to the
  S9 coherence inbox).
- Pinpoint **content** — which passages get pins, quote fidelity, page numbers (**S2** R3 + **S7**
  R5; S8 remediates anchor *placement* and consumes the verified quotes).
- The popover/anchor/hover **mechanism** (**S4** R5/R6 — S8 rides event delegation as-is; the one
  addition, the landing highlight, is R10's and supersedes nothing in S4).
- Pill placement, table schemas (**S5**). CI wiring + lint-roster numbering + release
  verification (**S9**; S8 delivers lint specs + fixtures).
- The Claude CL MCP lane is interactive spot-checks only; S8's fragment validation reads S2's
  cached text, **never live CL** (S1 A1/L4′).

## 3. Requirements (each testable)

**R1 — Link every case mention (user D1; the 388 seed).** Every mention of a case anywhere in
reader-facing content — full caption ("Florida v. Jardines") or short name (*Jardines*) — links
to its case page, at **every occurrence** (not first-occurrence), except in the R2 exemption
zones. Un-paged captions follow **the ledger rule**: a mention whose caption has a non-page
terminal state in `_run/s6-coverage-ledger.json` (`excluded-remit`, `unverifiable`, `removed`,
`folded-alias`, `watch`, `brief-mention`) stays **plain text** — never a dangling wikilink, never
a resurrected caption (COH-15). *Trigger:* the S8 EXECUTE pass; any later commit touching
`content/`. *Check:* the R12 ledger joins S6's — zero in-scope plain mentions of `authored`
captions; every plain mention cites a non-page terminal state or an exemption zone; LINT-5
(rewritten, R13) guards the steady state. `AUTO` · `PROCESS`.

**R2 — Exemption zones (one catalog, shared by linker and lints).** No link/term pass edits
inside: **(a)** headings; **(b)** code fences + mermaid blocks; **(c)** direct quotations
(quoted opinion text is never marked up — S1 Appendix A NEVER-APPLY); **(d)** citation strings
(reporter volumes/pages, parenthetical history: "(per curiam)", "rev'd on qualified-immunity
grounds", "reh'g en banc denied" — the pincite-link half of R4 is the one sanctioned edit inside
a citation string); **(e)** Sources sections (S5 R12 bullets are markdown links; case names
inside link text cannot nest wikilinks); **(f)** frontmatter + HTML comments; **(g)** a term's
own page (no self-links); **(h)** the sanctioned Case cells of R6 tables (already linked by S5
construction). The catalog is encoded **once** (`scripts/s8/zones.py`, imported by the linker and
by LINT-5/7). *Check:* the zone module has fixture tests; linker diffs show zero edits inside
zones. `AUTO`.

**R3 — Short-name resolution, fail-closed (SD1).** The resolver auto-links a short name only on a
**unique** resolution, tried in order: (1) **page-scope binding** — an earlier same-page
full-caption mention binds its short form for the rest of that page; (2) **page-roster match** —
unique match against the page's `homes[]`/Key-cases/Related set; (3) **corpus caption index** —
unique match against the S2 lake caption/alias index. Anything ambiguous (three *Morgans*, two
*Smiths*) is **never auto-linked**: it lands in the adjudication queue, a writer lane resolves it
with a one-line rationale, and the resolution is a ledger row S9 reviews. **Eponym phrases in the
term register ("Terry stop", "Miranda warnings", "Katz test", "Brady material", "Franks
hearing") route as terms (R7), not case mentions**; the bare italic name routes as a case.
*Check:* zero auto-links from ambiguous resolutions (resolver journal); every queue row carries
rationale + reviewer; register-listed eponyms never link case pages. `AUTO` (journal) ·
`PROCESS`.

**R4 — The split pincite convention (user D5, pivoted live; supplements S5 R16 — no text
superseded).** Where prose cites a **quoted, pinned** proposition: the **case-name half**
(*Jardines*, *id.*) links **internal, deep to the pin block** (`[[Case#^pin-N|…]]` — S5 R16's
rule, kept); the **pincite page numbers** ("8", "9–10", "469–70") link **external** to the
opinion with the R5 text fragment, so one click lands on the highlighted passage in the source.
Where no pin exists (paraphrase support, S7 R5 tier-3 downgrades): the name links **page-level
internal** and the pincite links **plain external** (opinion page, no fragment — a fragment is
never invented; there is no quote to highlight). On **case pages**, each pinned block's own
citation line ("— 569 U.S. at 6") carries the external fragment link (as exhibited on Jardines/
Walker). Table `opinion` cells and LCD `[opinion]` links stay page-level (S5 R6/R17 unchanged).
*Check:* sampled quoted propositions show both halves wired per the convention; zero fragment
links on tier-3 paraphrases; every external pincite host ∈ CL ∪ the S2 R14 whitelist. `PROCESS` ·
S9 sample.

**R5 — Fragment generation from verified quotes only (SD6).** External `#:~:text=` fragments
derive **exclusively from S2 pinpoint quotes that passed G3** (string-matched against source).
Generator contract, each rule live-verified on the mockup: **(a)** normalize to the *rendered*
CL text (whitespace collapses — slip texts hard-wrap mid-sentence; typographic dashes/quotes
follow the source, not our curly forms); **(b)** the snippet must not cross a **star-page
label** (CL interposes `*6` as visible text mid-sentence — a crossing fragment silently fails);
**(c)** validate = exactly **one** whitespace-insensitive match against S2's cached opinion text
(`<pool>/text/<opinion_id>.txt` — zero live CL calls, zero quota); **(d)** prefer a distinctive
start-only snippet (≥5 words); long quotes use `start,end`; multiple matches disambiguate with
`prefix-`; **(e)** URL-encode per the WICG syntax. The validated fragment is **written back to
the lake pinpoint record** (`pinpoints[].fragment`, via S2 R3's downstream write-back path — the
one-field schema addition rides as S2 § Amendments A14, filed with this spec). Unvalidatable →
plain external pincite + journal row. *Check:* every emitted fragment re-validates against cached
text at exactly one match; zero fragments without a G3-passed quote; the lake field present on
every fragment-linked pin. `AUTO` (validator) · `PROCESS`.

**R6 — Pin-anchor remediation precedes deep-linking (SD7; NUM-03 content half, ADAPTED from
S9's row — see Decision Log).** Quartz mints a block id only for an end-of-block `^pin-N`; the
corpus carries **299 mid-line pins across 233 files** (audit; re-measured at EXECUTE) that are
simultaneously visible-text leaks and **dead anchors** (live count today: 128 broken
`[[Case#^pin-N]]` deep links, including two on the S7 pattern page). Before wiring deep links, S8
mechanically remediates: each mid-line pin's block is **split** (or the anchor moved) so every
pin ends its own paragraph/list item — content order and wording untouched (exhibit: Walker
:46 / Lundin :46, commit `981b286`). S9 keeps LINT-9 (carat-leak guard) + re-verification.
*Check:* post-pass, mid-line `^pin-N` greps to 0; every `#^pin-N` wikilink resolves (LINT-5
broken-anchor = 0 at HIGH); the 396 pre-existing pin wikilinks still resolve. `AUTO`.

**R7 — Term links: four-way routing at every occurrence (user D2/D1).** Every occurrence of a
routed term outside R2 zones links per the **routing columns of the S1 A3 machine-readable term
register** (one artifact — the O1 term map `_overhaul/ledger/S7-term-map.md` is consumed as seed
and retired): **route: page** — terms of art with a doctrine-page home (curtilage, qualified
immunity, exigency, suppression→Exclusionary Rule, standing-4A…) link the page, piped display
preserving inflection; **route: glossary** — non-vernacular terms of art with no page home
(de novo, clear error, per curiam, respondeat superior, totality of the circumstances…) link
`[[Common Legal Terms#anchor]]`; **route: citing** — citation-mechanics terms (en banc,
certiorari, vacated, remand, slip opinion…) link `[[Reading and Citing Cases#anchor]]` (or its
S3-tree successor page); **route: skip** — the officer-vernacular list (search, seizure, arrest,
stop, frisk, warrant, consent, probable cause, reasonable suspicion, contraband, Miranda-as-
vernacular…) stays unlinked in prose; the list is instructor-editable register data, seeded from
the O1 map §E. Adjectival/compound uses ("qualified-immunity grounds" inside citation history)
follow their zone; noun uses link. *Check:* register rows carry route+target; a sampled page
shows every in-scope occurrence of routed terms linked; LINT-7 (rewritten) flags unlinked
register-term occurrences as review items and dead anchors as failures. `AUTO:LINT-7` (extended)
· `CHECKLIST:D5`.

**R8 — Glossary audit + expansion (non-vernacular only; O1 R9 rule).** After S7 finalizes, sweep
the corpus for non-vernacular terms of art with no page home and no glossary entry; author
entries as **pure definitions — zero citations, zero case-tied propositions** (keeps the glossary
outside the CL verification surface; case-tied limits stay on doctrine pages); anchorize
`### Term`; add register rows (route: glossary). Existing 37 anchors audited for the same rule.
*Check:* every glossary entry cites nothing; every register glossary-route resolves to an anchor;
no term both glossary-routed and page-routed. `AUTO:LINT-7` · `CHECKLIST:D5`.

**R9 — Transclusion: rule nodes + pinned quotes, on reliance (user D6; SD2).** Two embed flavors
only (glossary-definition embeds rejected — hover previews deliver definitions on demand):
**(a) rule embeds** — where a page teaches another page's black-letter rule, it embeds the
canonical rule-callout point paragraph (`![[<full-slug>#^rule-<tail>]]`) inside a `[!rule]`
shell titled `Black-letter rule — stated on [[Home Page]]`; **(b) pinned-quote embeds** — where
prose block-quotes a passage a case page pins, it embeds the pin block (`![[cases/<Case>#^pin-N]]`)
instead of re-typing the quote (short inline quote snippets woven into a sentence stay ordinary
quoted text + R4 links). **The boundary is the S1 A3 shingle detector**: prose that would overlap
a foreign rule/pin block ≥25 tokens must embed (embeds are the sanctioned way past the detector);
below the threshold, link in the page's own words. **Embed grammar: full-slug targets only** —
name/alias targets resolve through alias redirect stubs and the transclusion resolver silently
falls back to a bare link (live-verified failure + fix, commits `981b286`/`51e1f4b`). *Check:*
shingle detector green corpus-wide with embeds excluded from matching; every `![[` target is
full-slug and resolves (R13 check); the two Curtilage exhibits render (rule shell + quote block).
`AUTO` · `CHECKLIST:D5`.

**R10 — Landing highlight (user D7/D8, tuned live).** Internal anchor/pin landings: the target
block **flashes amber and settles to a visibly persistent tint** (rgba 255,208,84: 0.55 → 0.35)
that survives until the next navigation; the landing is **centered in the viewport** (SPA
`scrollIntoView({block:"center"})`; `scroll-margin-top: 30vh` for browser-native hard-load hash
scrolls). Because the SPA router navigates via `pushState` — which **never fires the CSS
`:target` selector** — the router applies the highlight class on every hash landing (both
navigation paths); `:target` remains for hard loads. Implementation = the mockup commits
(`51e1f4b`/`5b48d85`/`5d747f9`, normative); mechanism files are platform-layer (S4's domain) but
nothing in S4's signed text is superseded — this is additive behavior S8 owns. External
landings use the browser's own text-fragment highlight (persistent by construction). *Check:*
clicking a pin deep-link on the live site flashes + tints + centers; hard-loading the same URL
does too; the tint clears on next navigation. `MANUAL` on mockup · S9 visual sample.

**R11 — Table pipe-escaping (NUM-02).** Every wikilink inside a table row uses `\|` for its
display pipe. Quartz self-heals unescaped pipes at build (live-verified — the live site renders
today's 19 files/58 lines correctly), so this is **source hygiene**: S8's own pass injects piped
links into table cells at scale, and unescaped forms break in every other markdown surface. The
work list is **re-derived at EXECUTE** (the audit's 18/69 had already drifted to 19/58/68 by
2026-07-04 — seed-not-gospel). *Check:* unescaped-pipe-in-table-wikilink greps to 0 corpus-wide;
the check runs in the R13 lint kit. `AUTO`.

**R12 — The S8 link ledger (COH-15's join — SD3).** The pass emits `_run/s8-link-ledger.json`:
one row per case-mention occurrence — `{file, line, matched_text, caption_key, resolution:
{target, method: caption|page-scope|roster|corpus|adjudicated, rationale?}, action: linked |
linked-deep | plain:no-page | plain:adjudicated | exempt:<zone>}` — plus a terms section
(register coverage counts per page) and an embeds section (every `![[` with its source anchor).
**Reconciliation is the machine join:** NUM-04's 388 distinct bare-mention captions re-derive
from the ledger; join × S6's coverage ledger proves R1's check. *Check:* schema-valid; the join
runs clean in CI (a script, not an agent); S9 samples ≥1-in-10 rows + 100% of adjudicated rows.
`AUTO` · `PROCESS`.

**R13 — Lint kit rewrite (S8 designs + fixtures; S9 wires CI + final numbering per S1 A5).**
**(a) LINT-5 rewritten:** bare-caption check is **ledger-aware** (bare `authored` caption = fail;
bare non-page-terminal caption = pass — the rule, not an exception); markdown-link text masked
(kills the Sources false-positive class — 57/59 of the mockup pages' hits); R2 zones shared;
**broken anchor escalates MEDIUM → HIGH** (fail-closed — deep links and embeds are load-bearing);
`![[` embed targets must be full-slug. **(b) LINT-7 rewritten:** the first-occurrence-only rule
(old check (c)) is **deleted — inverted by D1**; replaced by register-coverage review flags +
anchor resolution (fail). **(c) pipe-escape check** (R11). **(d) fragment well-formedness**
(syntax only; semantic validation is R5's, at write time against cached text — CI never calls
CL). Fixtures for every check (`scripts/lint/fixtures/`). *Check:* each lint has pass/fail
fixtures; the old LINT-7(c) cannot fire; the kit runs green on the finished corpus. `AUTO`.

## 4. Lessons enforced

**Copies drift** (the O1 scar; PRACTICES §1) → R9 makes the shingle detector the mechanical
embed/link boundary. **Wrong-authority links** are worse than no link → R3's fail-closed
ambiguity queue (the three-Morgans trap). **Never invent evidence** → R5 fragments only from
G3-verified quotes; paraphrases never get fragments (mirrors "never resurrect an unverifiable
caption", R1). **Numbers-by-assertion** (COH-15) → R12's join. **Silent mechanism misdiagnosis**
(S4's scroll lesson) → R10 documents *why* `:target` can't work under `pushState`; R9 documents
the alias-stub transclusion trap — both found and fixed live, not assumed. **Cluster-vs-opinion
ids** bit again during fragment verification (a `search_document` against a page-URL id returned
0 hits on famous text) → resolve `opinions[].id` from search first (RUNBOOK §4-S9 input (a),
reconfirmed). **Seed-not-gospel** (S6 discipline) → every measured input (388 / 18-69 / 299-233)
is re-derived at EXECUTE; the drift is already visible today.

## 5. Method (execution — wave 3, after S7's batches land)

1. **Inventory** — fresh mention scan + pipe scan + pin scan over the S7-final corpus; build the
   caption index from the S2 lake (captions + aliases + short forms); load the S6 ledger.
2. **Pin remediation** (R6) across case pages; commit as one mechanical pass; LINT-5 anchor
   check green before any deep link is written.
3. **Case-mention pass** (R1–R3) per S3-category batch: script auto-links unambiguous mentions
   (zones enforced); ambiguity queue adjudicated by the writer lane; one commit per batch.
4. **Split-pincite + fragments** (R4–R5): wire name-half deep links; generate + validate
   fragments from lake pinpoints against cached text; write back `pinpoints[].fragment`; wire
   external pincite links (case pages first, then doctrine-side pincites).
5. **Term pass** (R7): extend the S1 register with routing columns (seed from the O1 term map +
   the S7-final sweep); script links register terms at density; unregistered candidate terms
   accumulate for R8.
6. **Glossary expansion** (R8): author + anchorize new entries; register rows; wire.
7. **Embeds** (R9): shingle-detector sweep finds restatements; convert to embeds (rule shell /
   pin block); re-run detector to green.
8. **Ledger + lints** (R12–R13): emit the ledger; run the join against S6's ledger; hand S9 the
   lint kit + fixtures + the adjudication queue for review.

## 6. Deliverables

- The linked corpus (case mentions, split pincites, term links, embeds) — one commit per
  batch/pass, all born on the working branch for S9.
- `_run/s8-link-ledger.json` (R12) + the adjudication queue with rationales.
- `scripts/s8/` (zone catalog, resolver, fragment generator+validator, pipe-escape fixer) +
  rewritten `lint5`/`lint7` + new checks + fixtures (R13).
- Term-register routing columns + vernacular skip-list (S1 A3 artifact, extended) + new glossary
  entries (R8).
- Lake write-back: `pinpoints[].fragment` on fragment-linked pins (+ the S2 § A14 note).
- The landing-highlight mechanism (R10) — mockup commits normative.
- This spec; mockup commits `981b286` · `51e1f4b` · `baa1e17` · `5b48d85` · `5d747f9`
  (normative exhibits); S9 wrapper handed back.

## 7. Acceptance criteria

- [ ] R1/R12 join clean: zero in-scope plain mentions of `authored` captions; every plain
      mention cites a non-page terminal state or exemption zone; 388 re-derived from the ledger.
- [ ] R3: zero ambiguous auto-links; every adjudication row carries rationale; register eponyms
      never link case pages.
- [ ] R4/R5: sampled quoted propositions wired both halves; every fragment re-validates at
      exactly one match against cached text; zero fragments on tier-3 paraphrases; fragments
      written back to the lake.
- [ ] R6: mid-line pins = 0; broken pin anchors = 0 (HIGH); pre-existing pin links intact.
- [ ] R7/R8: register routing complete; sampled pages fully linked at density; glossary entries
      citation-free; no dual-routed term.
- [ ] R9: shingle detector green with embeds sanctioned; all `![[` targets full-slug + resolving;
      the two embed flavors render as exhibited.
- [ ] R10: flash + persistent tint + centered landing on SPA and hard loads.
- [ ] R11: unescaped table pipes = 0.
- [ ] R13: lint kit + fixtures delivered; old LINT-7(c) deleted; broken-anchor = HIGH.

## 8. Verification plan

S8 self-verifies **mechanics only** (resolver journal, fragment validator, greps, the ledger
join — all scripts). **S9** reviews: ≥1-in-10 ledger rows re-checked through the Claude lane;
**100% of adjudicated ambiguity resolutions** re-reviewed (they are the judgment surface);
fragment spot-checks by actually following sampled links; embed coherence (the shingle sweep +
rendered-output sample); the R10 visual sample; LINT kit wired fail-closed into CI with final
numbering (S1 A5 / COH-21). The writer≠checker rule holds: the linking lane never closes its own
queue rows.

## 9. Open items / escalations

- **S2 § A14** (pinpoint `fragment` field) is filed with this spec as a cross-spec amendment
  note (S7→S6-A1 precedent); if the S2 builder's schema freeze predates it at EXECUTE, the
  fragments live in the S8 ledger until the next lake build — links still ship.
- **Fragment browser support**: text fragments are supported in Chromium, Safari ≥16.1, Firefox
  ≥131; older browsers land at the opinion page top — accepted degradation, no fallback UI.
- **CourtListener markup drift**: fragments validate against S2's cached text; if CL re-renders
  opinions (markup changes), fragments may stop matching — re-validation rides the GH#2
  maintenance loop (dual-date decay class).
- **`Reading and Citing Cases` successor**: the citing-route target follows the S3 tree's
  reference category at execution (register `target` is data, not code).
- **Backlink density** on landmark cases (Terry, Jardines) grows large under every-occurrence —
  accepted (reference-work posture); revisit only if S9 review finds pages unreadable.
- **LINT numbering** for the new checks is provisional pending S9's roster codification (S1 A5).

## 10. Decision log

**User decisions (interview 2026-07-04, 3 rounds + open floor, pivots live on the mockup):**
- **D1 — Every-occurrence density** for case mentions and routed terms (confirmed lean), with
  the R2 exemption zones as mocked.
- **D2 — Four-way term routing** (page / glossary / citing / vernacular-skip) as mocked; skip-
  list stays unlinked.
- **D3 — Landing highlight**: flash + tint (round 2: "works, but tune"), landing **centered**
  (round 3: top-flush rejected), tint **persists visibly** (open floor: no fade-to-nothing).
- **D4 — Internal + external highlight split** (round 2 pivot): internal deep links flash on our
  case page; pinned quotes ALSO jump out to the opinion with the URL highlight convention.
- **D5 — The split pincite convention** (round 2→3): case name → internal **pin-deep** (round 3:
  chose pin-block over page-top); pincite pages → external `#:~:text=` fragment.
- **D6 — Embed scope**: rule embeds + pinned-quote embeds adopted; **glossary-definition embeds
  rejected** (hover previews suffice; the flavor-3 demo was removed from the mockup).
- **D7 — Interactive-example protocol**: embed/flavor decisions made only after exact mock
  locations were provided (user instruction: always say exactly where in the mock to look).
- **D8 — Open floor closed** with the persistence tuning (→D3) and nothing else.

**Self-interview (SD1–SD10, run visibly pre-spec; full text in thread):** SD1 short-name
resolver — fail-closed unique-resolution ladder + eponym-as-term rule (guards wrong-authority
links). SD2 embed boundary = the shingle detector; full-slug embed grammar (guards drift AND
over-embedding; alias-stub trap live-verified). SD3 ledger join as the COH-15 artifact. SD4 lint
rewrites incl. broken-anchor escalation + Sources masking. SD5 routing lives in the S1 register
(one artifact; O1 map retired to seed). SD6 fragment contract (G3-quotes only; star-label
boundary; cached-text validation; whitespace-insensitive). SD7 pin remediation moves content-side
to S8, guard stays S9 (wave-order deadlock). SD8 idempotent staged pass, writer≠checker. SD9
popover contract verified — no new work. SD10 scale accepted; density tuning = register edits,
never per-page exceptions.

**Audit intake (every S8 row dispositioned — AUDIT-CLOSURE gate):**
- **COH-15** ADOPT — delivered as the R12 ledger join against S6 R11's ledger: S6 authors the
  no-page subset, S8 links ALL 388+ reading the ledger; the 388 / 88 / LINT-5 figures reconcile
  row-by-row by script. The joint-reconciliation obligation is closed by machine artifact.
- **NUM-04** ADOPT — the 388 seed acknowledged as the measured input (40/40 sample); consumed
  **seed-not-gospel**: the mention inventory is re-derived at EXECUTE (R1/Method 1) and the
  number re-emerges from the R12 ledger, not from the audit figure.
- **NUM-02** ADOPT-ADAPTED — the pipe-escape work is R11, but the audit's list (18 files/69
  lines) is consumed as a stale measurement: live re-derivation on 2026-07-04 already shows
  19/58/68 (S7 pattern-page rewrite + S6 specimen drift), and Quartz demonstrably self-heals at
  render — so the requirement is source-hygiene with a fresh EXECUTE-time list, not a fixed
  work list.
- **NUM-03** *(S9's row, ADAPTED here with pointer)* — the mid-line-pin **content remediation**
  rides S8 (R6: S8 touches those blocks anyway and needs the anchors); **LINT-9 + verification
  stay S9's**. The S9 wrapper carries this boundary explicitly.

---

## Cross-spec note filed with this spec

**S2 § Amendments A14 (proposed by S8, 2026-07-04) — pinpoint `fragment` field.** Adds to R3's
pinpoint block: `fragment` (the validated `#:~:text=` string) + `fragment_validated_at`, written
back through R3's existing downstream write-back path when S8 generates external pincite links.
Semantics + validation contract live in S8 R5; S2's schema gains the optional field only. Filed
as an appended amendment in `S2-authority-database.spec.md` (precedent: S6 § A1, authored at the
S7 interview).
