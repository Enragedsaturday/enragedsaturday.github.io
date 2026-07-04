# SPEC S9 — Verification Pipeline & Release Gate

**Status: APPROVED (signed at interview, 2026-07-04).**
gates: all of S1–S8 (S9 verifies everything). Authoring order only; execution = wave 4 (RUNBOOK §3),
after S8's linking lands. The LAST spec — the coherence pass over all nine + the AUDIT-CLOSURE gate
follow it.

Interview: 2026-07-04 (3 rounds + served brief + user notes; 7 user decisions D1–D7) + visible
self-interview (SD1–SD10, full text in the thread; SD1/SD2 worked adversarially deep).
Exhibits (all live on the branch): **the worked finding F-DEMO-001** (`_overhaul2/s9-demo/` —
finding → 3-lane panel → 2-of-3 refute kill → MODIFIED adjudication → fix → non-author re-review,
NOT-FIXED at round 1, FIXED at loop 2) · the signed ledger schema (`_overhaul2/s9-demo/
LEDGER-SCHEMA.md`) · the adjudicated LINT-3 acceptance fixture (`scripts/lint/fixtures/
lint-3-n5.md`) · the Codex feasibility probes (headless reviewer lane: `LANE-OK gpt-5.5`;
headless discovery: 74 live `web_search` events returning the 4th Cir. en banc *Chatrie*,
136 F.4th 100, verified on Justia — 2026-07-04) · interview brief
`~/briefs/2026-07-04-cssi-s9-interview.html`.

Precedence: this spec wins over RUNBOOK §4-S9 and the S9 wrapper (RUNBOOK §0 stack).

---

## 1. Objective

Run the continuous, fail-closed verification pipeline and the release gate that make the corpus the
definitive, 100%-verified edition: writer ≠ checker at every seam; a real 1-Claude + 2-Codex
adversarial panel with a genuine ≥2-of-3 refute tally; the 10-gate per-proposition protocol; an
**exhaustive blind re-derivation of every case and doctrine conclusion diffed against the built
corpus, with an evidence-cited adjudication of every discordance** (user D1 — the comparison layer);
a machine-emitted, script-reconciled ledger so the audit itself can be audited; bounded completeness
instruments with a fail-closed escalation tripwire; the full CI lint roster codified and green; and
a release gate whose every box passes or carries a logged escalation — zero silent gaps, zero
guessed legal assertions. S9 reads from the S2 lake (cached opinion text = the primary-read
substrate, zero CL quota); live CL only through the two per-credential serial lanes (S1 A1/L4′).

## 2. Scope

### 2.1 In scope (S9 owns)
- The review machine: panel composition, lane-isolation mechanics, the finding→vote→adjudication→
  fix→re-review loop (cap 3), the signed ledger schema + reconciliation script (R1–R4).
- The exhaustive blind re-derivation + concordance gate (R5) and the assertion inventory (R2).
- The question checklist per entry (framed? explained? cited? related? narrowed? expanded? good
  law? abrogated/overruled? current treatment?) — run inside R5/R6's review forms.
- The completeness package (user D7, option A): currency sweep · citing-graph gap check ·
  dual-TOC doctrine audit · absence-claim sweep · sampled frontier re-run with the full-re-run
  tripwire (R7). Dual-model discovery lanes throughout (user note, feasibility-verified).
- The CI lint-roster codification (COH-21) incl. the S2/S3/S4/S5/S6/S8 lint intake, final
  numbering, fixtures, fail-closed wiring (R8), and the S8-handoff verifications (R9).
- Per-spec re-verifications: S4 R8 retirement checklist + R5/R6 samples; S5 R2 callout↔registry
  coherence + point-status tables; S6 gate/two-key ≥1-in-10 via the Claude lane; S7 tier-sampled
  conversions + per-item G2 + the cross-page contradiction sweep; S8 ledger/adjudication/fragment/
  visual samples (R9–R11).
- The release gate (R13), the self-audit of the pass itself (R14), publish + verify-live + the
  legacy-pipeline retirement re-verification (R15), and the maintenance handoff (R12).

### 2.2 Out of scope (owned elsewhere)
- Authoring or re-designing content, templates, taxonomy, linking density — S9 verifies S1–S8's
  outputs and applies adjudicated fixes through the machine; it relitigates no settled decision.
- New-case authoring: discoveries route through S6 R8's pipeline (S9 never hand-mints a page).
- The `^pin-N` mid-line CONTENT remediation (S8 R6 — NUM-03 boundary); S9 keeps LINT-9 + the
  re-verification (R9).
- The flashcard rebuild (deferred run #2 — S9 only confirms stems still resolve) and the
  maintenance loop itself (GH#2 — S9 seeds it, R12).
- The officer-BLUF layer stays banned (S1 §2.2 + R6); S9 verifies its absence, never builds it.

## 3. Requirements (each testable)

**R1 — The panel: 1 Claude + 2 Codex, mechanically isolated, lens-diverse (user D3; SD1).**
Every legal-assertion surface (existence, support, quote fidelity, pincite, treatment/good-law,
black-letter statements) is reviewed by the full adversarial panel — each lane prompted to REFUTE,
default-refute on uncertainty; **≥2-of-3 refute kills the assertion/finding as framed** (it returns
only through an evidence-cited adjudication). Black-letter rule text additionally requires
**≥2 affirmative reviewer approvals** (S1 R6/R12). Editorial/structural dimensions: one reviewer +
the lint roster. Isolation mechanics (all machine-checkable): each Codex lane = a fresh
`codex exec` (never `resume`), isolated working dir, **read-only sandbox**, `-o` capture, stdin
from `/dev/null`, caller-side timeout (COH-31 — macOS has no GNU timeout); model gpt-5.5; no CL
MCP (reviewers read the lake). Every lane invocation logs an **input manifest** (exact files/fields
disclosed); manifests MUST exclude sibling votes, in-progress adjudications, and (for blind work)
the lake's judgment fields. Votes are recorded before mutual disclosure. The two Codex lanes carry
**distinct attack lenses** (A: support/quote-fidelity; B: currency/treatment). The Claude lane
votes on every paneled finding (model diversity on every tally). *Check:* every paneled finding
has 3 lane votes with manifests; a manifest containing a sibling vote or a pre-vote judgment field
= a blindness-audit failure (R14); zero `resume` invocations in the lane journal. `AUTO` (manifest
audit) · `PROCESS`.

**R2 — The assertion inventory (the exhaustiveness gate).** P0 deterministically extracts every
tracked assertion from every object class (case pages, doctrine/overview/reference pages, glossary,
Case Index, nav, About, lake records, S6/S8 ledger rows): case-cite · proposition · quote+pinpoint
(+ `pinpoint_status`, + `fragment` where present — S2 A14) · treatment fields · weight label ·
homes/roles · registry point ↔ callout pair · mermaid block · link/embed targets. Each item gets an
`assertion_id`; **zero items may end the run without a verdict**. *Check:* the inventory enumerates
every R9-class object; the completeness audit (R14.5) fails on any verdict-less item. `AUTO`.

**R3 — The 10-gate protocol per proposition, per-item.** PRACTICES §3 runs per entry with
PASS/FAIL/FLAG recorded per gate: G1–G5 substantiation against the cached primary text (passage-
exhaustive by construction — every quote string-matched, every pincite star-verified or
`slip-only`-typed per S2 A3), G6–G10 validity (treatment on-point analysis, jurisdiction, dual
as-of dates, independent corroboration on load-bearing propositions). **G2 runs per enumeration
item** (S7 input (b)): in any conjoined/enumerated assertion, each item independently supports at
the stated breadth or is cut/qualified — the corrected knock-and-talk flashlight pitfall (commit
`4b48a4a`) is the committed fixture; categorical verbs trigger the S1 R7 breadth check. *Check:*
gate rows exist per proposition (carried assertions included — S7 R3's no-inheritance); a sampled
enumeration shows per-item gate rows. `AUTO` (ledger) · `CHECKLIST:D1/D2`.

**R4 — The machine + the signed ledger (user D5).** Find→adjudicate→fix→re-review, loop cap 3,
then ESCALATE → `_review-needed/<slug>.md`. The ledger = the four signed row types
(`s9.finding.v1` / `s9.vote.v1` / `s9.adjudication.v1` / `s9.fix.v1`, JSON-lines under `_run/s9/`,
joined to the inventory by `assertion_id`) with the **five reconciliation invariants checked by
script, not agent, fail-closed in CI**: (1) finding→adjudication 1:1; UPHELD/MODIFIED → a fix
whose final loop is FIXED, or an escalation; (2) paneled findings carry all 3 votes; ≥2-refute ⟹
never plain UPHELD-as-framed; (3) lane-identity: finder ≠ adjudicator on legal findings; fix
author ∉ its re-review lanes; no lane closes its own row; (4) every DISMISSED carries a reason
(the false-positive log); (5) counts reconcile end-to-end; zero verdict-less inventory items.
Legal verdicts MUST cite lake/CL/whitelist evidence; post-fix re-review is by a model that did not
author the fix. Normative reference: `_overhaul2/s9-demo/LEDGER-SCHEMA.md` + the F-DEMO-001 rows
(the worked instance — including the live NOT-FIXED→loop-2→FIXED trail). *Check:* the invariant
script runs green at the gate; the demo instance validates against the schema. `AUTO`.

**R5 — Exhaustive blind re-derivation + concordance (user D1/D2; SD2 — the comparison layer).**
**Thread P** (frozen at P0, hash-stamped `thread-P.json`): the built corpus's conclusions,
extracted deterministically — per case: holding/disposition, treatment on taught points, homes,
splits; per doctrine: case-set + split calls. **Thread N** (blind): for **every** case (~600), a
lane reads the cached opinion text and derives structured conclusions with NO access to the page,
the lake's judgment fields, or Thread P (manifest-enforced, R1); every read opens with an
independent parties-in-text ↔ caption identity assertion. Staffing (user D2): Codex lanes carry
case-grain reads; **Claude carries doctrine-grain re-derivations, ALL discordance adjudications,
and the ≥1-in-10 live-CL identity slice** (COH-17 — checking the builder's cache with a credential
+ model the builder never touched). Reconciliation (a separate step): diff at coverage + judgment
grain; concordant → `double-verified`; **fundamental discordance** (presence/absence · holding ·
home-by-holding · treatment/good-law · split direction) → the panel + a serial-evidence-cited
adjudication naming **what diverged and which conclusion stands**; cosmetic → reconcile freely.
**No-regression floor:** every Thread-P item absent from N is dispositioned, never silently lost.
**Stated limitation (SD2, honest):** Thread N shares the builder's source universe (cached texts +
builder-derived progeny lists); the compensating instruments are the identity assertions + Claude
live slice (mis-cache), the currency sweep's fresh queries (missed progeny), and R7's absence
sweep (unfalsifiable-from-cache claims). Tiering survives as ORDERING only: recency → negatives →
rule-bearing → high-profile → the rest. *Check:* `thread-P.json` frozen before any Thread-N
manifest is issued (hash + timestamps); N's conclusions recorded pre-reconciliation; every
discordance carries an adjudication with evidence; zero silent absences; the identity-assertion
field present on every N read. `AUTO` (manifests/hashes) · `PROCESS`.

**R6 — The question checklist + cross-page contradiction sweep.** Every entry's review form runs
the checklist: framed? explained? cited? related? narrowed? expanded? good law? abrogated/
overruled? current treatment? — answered from the R5 re-derivation + R3 gates, recorded per
object. **The contradiction sweep** (S7 input (c)): pairwise review over shared points (joined via
registry `also_on[]` + `homes[]`), hunting semantic contradiction between pages (the Knock-and-Talk
vs Plain View flashlight exhibit — contradiction, not duplication; the shingle detector
structurally cannot fire on it, so this is agent work, panel-refereed on hits). Overruled cases
render as history everywhere; treatment identical across every home (multi-home coherence).
*Check:* checklist columns complete per object; the sweep's pair list covers 100% of shared
points; every contradiction hit has an adjudication. `PROCESS` · `AUTO` (pair-list coverage).

**R7 — The completeness package (user D7 = option A + notes; SD5).** Five instruments, all finds
routed two-key → relevance gate → S6 R8's pipeline → born `draft` → the panel; >10 new pages ⇒
human pause (the S6 scope guard):
1. **Currency sweep** — re-poll every pending marker (COH-27: *Carter v. United States* cert
   No. 25-885 · *Noem v. Vasquez Perdomo* · the *Lange* felony-reservation note, S7 §9); re-run
   each doctrine's recency lane (`cites:(…) AND filed_after`) for decisions since the S2 build;
   bounded web sweep per category.
2. **Citing-graph gap check** — mechanical, from the lake + re-fetched lane-3 results: top-cited
   or recent progeny of each doctrine's key cases appearing nowhere in the corpus → coverage-gap
   findings → adjudicated (LCD bullet / page via S6 R8 / logged deliberate-exclusion).
3. **Dual-TOC doctrine audit** — every S3 registry point stated on its home page (the R10
   callout↔registry gate) + a chapter-grain sweep of BOTH reference TOCs (LaFave AND NJLEH): any
   topic with zero corpus home gets a logged disposition (covered / out-of-remit / gap→escalate).
4. **Absence-claim sweep** — enumerate every negative claim in final prose (grep: unmapped
   circuits, "no court has", first-impression, split markers + the change-list split sections);
   each gets a fresh two-direction search: CL full-text via a **batched query list executed by the
   S2 builder lane** (owns the token; serial, paced — the S6 R7 queue pattern) + web via a Codex
   `web_search` lane; results panel-reviewed.
5. **Sampled frontier re-run + tripwire** — an independent frontier pass on digital +
   civil-remedies (risk-chosen) **+ one random category** of the remaining 11, diffed against
   S6's saturation logs. **Tripwire (fail-closed): any two-key-real, gate-passing case or
   doctrine-grain point S6's logs do not account for ⇒ the full 13-category re-run fires.**
**Dual-model discovery everywhere** (user note): each instrument's search work runs BOTH a Claude
lane and a Codex `web_search` lane (recipe: `codex exec -c tools.web_search=true -s read-only …` —
the root `--search` flag does NOT pass through `exec`; feasibility verified live 2026-07-04, 74
search events, real find verified on Justia), finds unioned then two-keyed. A cross-spec note
(§ Cross-spec, below) adds the same dual-model lane to S6 R6's EXECUTE frontier. *Check:* per-
instrument artifacts exist (marker-poll log; gap-finding rows; TOC dispositions; absence-claim
ledger with per-claim search evidence; the sample-diff + tripwire evaluation); every find has a
ledger terminal state; the pause fires >10 pages. `PROCESS` · `AUTO` (artifacts + ledger).

**R8 — The CI lint roster, codified fail-closed (COH-21; SD4).** Numeric `LINT-<n>` is canonical
(S1 A5); the table below is THE roster; descriptive aliases permitted on first mention. All run in
CI fail-closed (HIGH blocks; the roster gates publish); every lint ships pass/fail fixtures in
`scripts/lint/fixtures/`.

| # | Name (alias) | Source / notes |
|---|---|---|
| 1 | CL identity | O1; serial-CL-gate-only, Claude-lane slice (COH-17) |
| 2 | quote/pinpoint | O1; consumes S2 A3 `pinpoint_status` |
| 3 | structure + N5 (extended) | **rebuilt lake-driven** per S1 A2 + the F-DEMO-001 adjudication: section-scoped — no `Binding — SCOTUS` label, no SCOTUS-court wikilink (court from the lake) inside a frontier section; heading re-pointed to `Lower-court developments` (TEACH-08/S5 R11); the token-window heuristic dies (COH-28 — its over- AND under-detection). Acceptance fixture: `lint-3-n5.md` (committed). Adds the S1 A9 >3-cases-per-paragraph sub-check |
| 4 | lexicon | validates against S1 A8's exact allowlist (spacing, order, circuit suffix) |
| 5 | link-every-case | **S8 rewrite**: ledger-aware bare-caption rule; markdown-link-text masked; **broken anchors = HIGH, fail-closed**; full-slug `![[` targets |
| 6 | treatment | 3-field + dual dates; U+2B58 invalid (S1 A6); ⚪ never unbannered |
| 7 | term register | **S8 rewrite**: first-occurrence rule DELETED (D1-inverted); register-coverage review flags; anchor resolution = fail |
| 8 | guardrails + mnemonics | + **TEACH-11: wikilink-target checks** — a mnemonic/maxim's link target must exist AND match the register entry (the CREW mislink and the inverted Golden-Rule maxim both pass naive text lints; target+wording check catches both) |
| 9 | carat-leak (`^pin-N`) | verification half of NUM-03 (content remediation = S8 R6): zero visible carats in rendered output, zero broken pin links; corpus-wide, re-measured at EXECUTE (audit's 299/233 had already drifted to ~404/267 by 2026-07-04 — seed-not-gospel) |
| 10 | em-dash budget | unit = **block** (paragraph or list item — S7 input (e)); quotes + controlled labels exempt (S1 A7/A8); Sources trailing info parenthesized per S5 R12 |
| 11 | pipeline-vocab | **TEACH-02b build**: the S1 A2 five-class pattern table, rendered-prose scope, About-page allowlist, committed exclusion list |
| 12 | lake↔frontmatter drift | ≡ `LINT-S2-drift` — **this table executes the re-pointing S1 A5 promised** (closure-verifier finding); S2 § notes the rename |
| 13 | lake schema | ≡ `LINT-S2-schema` |
| 14 | page↔record | ≡ `LINT-S2-pagerecord` |
| 15 | skeleton | S5 (doctrine H2 order + BIRAC) |
| 16 | case-tables | S5 (3 schemas, no authored data cells, host whitelist) |
| 17 | coverage-ledger caption | S6 R12 (prose caption ⇒ page or ledger terminal state) |
| 18–25 | S3 set | depth · overview · points · binding · derip · order/weight · urls · deck (≡ `LINT-S3-*`, renumbered; deck stems = deferred-run-#2's precondition) |
| 26 | good-law target | ≡ `LINT-S4-goodlaw-target` |
| 27 | pipe-escape | S8 R11 |
| 28 | fragment well-formedness | S8 R13(d) — syntax only; semantic validation is write-time vs cached text |
| 29 | shingle detector | S1 A3 R11: ≥25-token overlap between rule/pin blocks across files fails — **transclusion embeds excluded** (S8 R9's sanctioned path); MUST still fire on raw restatements (fixture-pinned) |
| 30 | ledger reconciliation | the R4 invariant script (S9's own audit-the-audit row) |

*Check:* `run_all.py` (extended) runs 2–30 green on the finished corpus (1 at the serial gate);
every row has fixtures; `LINT-S2-*`/`LINT-S3-*`/`LINT-S4-*` names survive only as aliases. `AUTO`.

**R9 — S8-handoff verification (the S9 wrapper block).** (a) **NUM-03**: post-S8-R6, mid-line
pins = 0, zero broken pin links, the 396+ pre-existing pin wikilinks resolve (LINT-9 + LINT-5).
(b) **S8 ledger review**: ≥1-in-10 of `_run/s8-link-ledger.json` rows re-checked via the Claude
lane; **100% of adjudicated ambiguity resolutions re-reviewed** (the judgment surface — the
three-Morgans class). (c) **Fragment spot-checks**: sampled external `#:~:text=` pincites followed
end-to-end in a real browser — the highlight lands on the quoted passage; every fragment traces to
a G3-passed lake quote (S2 A14); **zero fragments on S7 tier-3 paraphrases**. (d) **Shingle scope**
(R8 #29): embeds excluded, raw restatements fire. (e) **R10 visual sample**: deep-link landing =
centered + flash + persistent tint, SPA and hard loads both; plus S4's R5 popover sample and R6
tooltip against projected frontmatter. *Check:* per-item sample logs with pass/fail; any fragment
landing miss → the R4 machine. `PROCESS` · `MANUAL` (visual) · `AUTO` (greps).

**R10 — Cross-layer coherence gates.** (a) **Callout↔registry**: every S5 R2 rule-callout
paragraph deep-equals its registry `statement` (S3 R4); every S2 override slug resolves through
the binding map (S3 R5); **S2F-07b**: S7 prose citing provisional point slugs re-checked after
binding — a 1:N split flags every page citing the split slug. (b) **Prose↔lake**: every
"Treatment & subsequent history" section + point-status table consistent with the lake record
(S2 R12's coherence gate; S5 R5). (c) **Projection**: LINT-12/14 green; legacy values render only
through the S1 A4 mapping (S5 R14); every REVIEW-marked migration row adjudicated (S2 A13).
*Check:* deep-equal pass corpus-wide; zero unresolved slugs; zero un-adjudicated REVIEW rows.
`AUTO` · `PROCESS`.

**R11 — Per-spec re-verification samples (tier-aware).** S6: ≥1-in-10 gate verdicts + two-key
results via the Claude lane (COH-17); both pause packets carry recorded user dispositions.
S7: **TEACH-03 conversions sampled BY TIER** (input (d)) — T1 star-page recomputed; T2 the ≥2
co-occurrence evidence re-pulled; T3 re-verifies **G2 support** (no quote exists — the check is
paraphrase-vs-holding breadth); R3 carried-assertion gate rows sampled; R9 fix-list dispositions
audited (refuted items carry research pointers). S4: the R2 scroll round-trip, R4 did-you-mean
smoke, R12 stem safety. Mermaid/visuals: every diagram rendered + inspected against its page's
(re-verified) rule. *Check:* sample logs per spec with escalation on any failure (a failed sample
re-opens its class, not just the item). `PROCESS`.

**R12 — Maintenance handoff (user D6).** S9 emits, as machine artifacts: the CL citator-alert
seed list (every watch/pending row incl. Carter/Noem + the negative-treatment census), the
dual-date decay schedule (`as_of_*` re-verification cadence per PRACTICES §6.10), the fragment
re-validation queue (CL markup drift — S8 §9), the deck-rebuild precondition attestation (stems
resolve), and the open `_review-needed/` register — filed to GH#2 (the FORK's issue #2) on
publish. *Check:* the handoff artifact exists, is schema-valid, and GH#2 references it. `AUTO` ·
`PROCESS`.

**R13 — The release gate (user D4 — full composite; the literal definition of done).** Done ⇔
every box PASSES or carries a logged `_review-needed/` escalation; zero silent gaps; zero guessed
legal assertions; specifically: every inventory item verdicted (R2) · machine + ledger invariants
green (R4) · concordance complete with zero silent absences (R5) · checklist + contradiction
sweep complete (R6) · completeness instruments run, tripwire evaluated, finds terminal (R7) ·
lint roster 1–30 green (R8) · S8 handoffs verified (R9) · coherence gates pass (R10) · per-spec
samples clean or escalated-and-resolved (R11) · maintenance handoff emitted (R12) · the blocking
brief-quality composite on every doctrine page (an S1-conformant brief: rule callout verified,
test up front, pitfalls, no banned layer — a page with perfect cites but a muddled brief FAILS) ·
⚪ never reaches a reader unbannered · the **G8 publish pause** (§0 register #6) precedes any
production push. *Check:* the gate checklist evaluated object-by-object; every escalation is a
file with a stated open issue, none a guessed assertion. `PROCESS` · `AUTO`.

**R14 — Self-audit of the pass (SD6; O1 §8 upgraded).** (1) False-positive accounting: every
DISMISSED logged with reason; per-lane refute/dismiss rates surfaced (prompt-tuning signal, never
auto-suppression). (2) **Adjudication sampling re-check**: a random sample of UPHELD/MODIFIED
legal fixes gets an independent second confirmation (different lane, serial evidence); a failed
sample re-opens the dimension. (3) **Pass-sample re-read**: random "passed" pages re-read against
cached primary text by a lane that didn't review them. (4) **Blindness audit = manifest diffs**
(SD1/R1/R5): Thread-P-before-N proven by hashes + timestamps; a contaminated manifest voids the
affected concordance (agreement carries information only if blind) and re-runs it. (5) Inventory
completeness (zero verdict-less items). (6) Lint spot-verification (hand-check samples of green
lints — a green a hand-check contradicts is itself a finding). (7) Escalation audit (nothing
dropped at loop cap). (8) **Drift re-check at the gate**: pending markers + currency re-confirmed
immediately pre-publish (law moves during a long pass). *Check:* the self-audit section of the
final report carries all eight results; failures re-open phases, never ship. `PROCESS` · `AUTO`.

**R15 — Publish, verify live, retire (last).** On gate pass + the user's go-ahead (the G8 pause):
commit + push `main` → Vercel; **verify live** (pages 200, no internal 404s, popovers/search/
badges work, sampled fragments land, internal dirs unpublished, frozen flashcards load); then
execute + **re-verify the S4 R8 retirement checklist** (:8787 dead, launchd agent gone,
`serve-public.py`/`redeploy.sh` deleted, `/cssi-ingest` re-pointed, vault frozen) — sequenced
after the deploy per S4 D5. Deliver the final report as a served HTML brief (accuracy summary ·
negative-treatment census · splits/frontier table · concordance stats · escalations · the
maintenance handoff pointer). *Check:* live checks logged; retirement greps clean; the brief link
delivered. `PROCESS`.

## 4. Lessons enforced

**The O1 collapse** (N-of-3 → N-of-1; blind re-derivation skipped; no machine ledger) → R1's
manifest-enforced isolation, R4's script-checked invariants, R5 actually run corpus-wide — and the
F-DEMO-001 exhibit proves the loop live (a panel killing a plausible wrong fix from a prior
*verified* pass; a re-reviewer catching the fixer's own stale pointer). **CL is not a good-law
oracle** → R3/R5 derive from primary text; SD3's whitelist evidence lane codifies the web-L2
two-key that saved Chatrie/Zorn. **Cluster≠opinion ids** (LAW-02 class; reproduced twice since) →
every document read resolves `opinions[].id` from search first (S7 input (a)); typed fetchers +
identity assertions throughout. **Slip-op mislabels** → R11's tier-sampled TEACH-03 audit.
**Alarm fatigue** (a permanently-red lint teaches ignoring lints — S1 A8) → R8 rebuilds LINT-3
lake-driven instead of accepting documented false positives. **Concordance theater** → R5's
stated-limitation + compensating instruments; R14's manifest-diff blindness audit. **Numbers by
assertion** → every measured input re-derived at EXECUTE (the pin counts drifted 299→404 in two
days of mockups). **Writer ≠ checker** → COH-17's Claude-lane routing; read-only reviewer
sandboxes; lane-identity ledger invariants.

## 5. Method (execution — wave 4, one autonomous run)

- **P0 — Bootstrap.** Backup; load specs + STANDARDS + ledgers; build the assertion inventory
  (R2); **freeze + hash `thread-P.json`** (R5); wire the roster (R8) and run it for the baseline.
- **P1 — Parallel review + blind reads (free lanes, no CL).** Panel reviews per object (R1/R3/R6)
  + Thread-N blind re-derivation (R5), Codex case-grain / Claude doctrine-grain; manifests
  journaled. The Claude serial lane starts the ≥1-in-10 identity slice + pending-marker polls.
- **P2 — Adjudication + concordance.** Reconcile N vs P; adjudicate every discordance + every
  paneled finding (evidence-cited; serial lanes for live checks); stage fixes.
- **P3 — Fix loops.** Apply UPHELD/MODIFIED verbatim; non-author re-review; cap 3 → escalate.
- **P4 — Completeness + sweeps.** The five R7 instruments (dual-model); contradiction sweep (R6);
  S8-handoff + coherence + per-spec samples (R9–R11); discoveries → S6 R8 (pause >10 pages);
  tripwire evaluated.
- **P5 — Gate + self-audit.** R13 object-by-object; R14's eight checks; emit the maintenance
  handoff (R12); the final report brief.
- **P6 — Publish pause → deploy → verify live → retire** (R15).
Checkpointed/resumable throughout; the ledger is the run state; two serial CL lanes only, per
credential, journaled with consumer identity + credential fingerprint (S1 A1).

## 6. Deliverables

`_run/s9/` (findings/votes/adjudications/fixes JSONL + the invariant script) ·
`assertion-inventory.json` · `thread-P.json` + `s9-concordance.jsonl` · the R7 instrument
artifacts (marker log, gap findings, TOC dispositions, absence ledger, sample-diff + tripwire
verdict) · `scripts/lint/` roster 1–30 + fixtures (LINT-3 rebuilt; the demo fixture is its
acceptance test) · the R12 maintenance-handoff artifact (filed to GH#2) · `_review-needed/`
queue · `FINAL-S9-REPORT` + served brief · this spec · the F-DEMO-001 exhibit set
(`_overhaul2/s9-demo/`).

## 7. Acceptance criteria

- [ ] Every paneled finding: 3 manifest-clean votes; ≥2-refute never ships as-framed; black-letter
      carries ≥2 approvals (R1).
- [ ] Zero inventory items without a verdict; gate rows per proposition incl. per-item G2 (R2/R3).
- [ ] Ledger invariants 1–5 green by script; every fix's final loop FIXED or escalated (R4).
- [ ] Thread P frozen-before-N (hashes); every case + doctrine re-derived blind; every fundamental
      discordance carries a what-diverged/which-stands adjudication; zero silent absences (R5).
- [ ] Question checklist complete per entry; contradiction sweep covers 100% of shared points (R6).
- [ ] All five completeness instruments run dual-model; tripwire evaluated on evidence; every find
      ledger-terminal; >10-page pause honored (R7).
- [ ] Roster 1–30 green fail-closed; LINT-12/13/14 re-pointing executed; LINT-3 lake-driven with
      the committed fixture passing (R8).
- [ ] S8 handoffs verified: pins/anchors clean, ledger + 100%-adjudication review done, fragments
      land end-to-end, zero tier-3 fragments, shingle scope proven, landing visuals pass (R9).
- [ ] Coherence gates: callout↔registry deep-equal; all slugs bound (S2F-07b rechecked);
      prose↔lake consistent; zero un-adjudicated REVIEW rows (R10).
- [ ] Per-spec samples clean or escalated-and-resolved; TEACH-03 sampled by tier (R11).
- [ ] Maintenance handoff emitted + filed (R12). Release gate: every box PASS or logged
      escalation; G8 pause honored (R13). Self-audit 8/8 (R14). Live checks + retirement
      re-verification logged; final brief delivered (R15).

## 8. Verification plan (who watches the watchmen)

R14 is the meta-layer: the pass's own findings, adjudications, and blindness are themselves
sampled, re-checked, and manifest-audited; a failed meta-check re-opens the phase. The AUDIT-
CLOSURE gate (RUNBOOK §7) then runs as part of the coherence pass: an adversarial non-writer agent
walks `AUDIT-2026-07-02.md` and every spec's Decision Log and stamps closure. The user holds the
two human gates: the release-gate go-ahead and the publish pause.

## 9. Open items / escalations

- **Codex CL MCP** remains broken (re-confirmed 2026-07-04) — by design reviewers read the lake;
  if it is ever re-authed, it stays OFF for reviewer lanes (independence > convenience).
- **Codex output-schema drift**: reviewer lanes occasionally wrap JSON in prose; the lane harness
  strips/repairs, and an unparseable vote re-runs once then counts as `no-vote` (a 2-lane tally
  then requires unanimity to kill). To be exercised in the first EXECUTE batch.
- **Thread-N cost envelope**: ~600 case reads + ~90 doctrine derivations, parallel, cache-fed.
  If wall-clock threatens the run, the lever is batch width, never scope (D1 is a user decision).
- **Tripwire scope**: if the sampled re-run fires the full 13-category re-run, EXECUTE pauses and
  surfaces the evidence + revised wall-clock before proceeding (mirrors the >10-page pause).
- **`Reading and Citing Cases` successor slug** (S8 §9) — the citing-route target is register
  data; R9(e) verifies whatever the S3 tree emitted.
- **LINT numbering 18–30** is fixed by this spec's R8 table; if EXECUTE surfaces a collision, the
  table wins and the Decision Log records the correction.

## 10. Decision log

**User decisions (interview 2026-07-04, 3 rounds + served brief + notes):**
- **D1 — Exhaustive blind re-derivation** ("I'm leaning toward exhaustive… I want a comparison
  mechanism between what was written previously and what this round finds/writes, with a serious
  adjudication layer for any differences"): every case full-read blind, diffed, discordances
  seriously adjudicated (R5). Affordable because reads are cache-fed (zero CL quota).
- **D2 — Thread-N staffing split by grain**: Codex case-grain; Claude doctrine-grain +
  discordance adjudications + the live identity slice.
- **D3 — Panel scope = legal assertions + rule layer** (editorial = 1 reviewer + lints).
- **D4 — Release gate = full composite** (blocking brief-quality composite; escalations logged,
  never silent).
- **D5 — Ledger schema signed as demonstrated** (LEDGER-SCHEMA.md + F-DEMO-001).
- **D6 — Maintenance handoff adopted** (user addition): S9 seeds GH#2 with machine artifacts (R12).
- **D7 — Completeness = option A** (bounded instruments + absence sweep + sampled re-run with the
  full-re-run tripwire), **with two user notes folded in**: (i) discovery fan-out uses BOTH Claude
  and Codex ("the first iterations were claude only… codex could very well search differently") —
  Codex `web_search` feasibility verified live before writing, as required; (ii) **CL first-class
  with industry-accepted secondary fallback** (Justia et al.) for evidence and links when CL has
  gaps — codified as SD3's evidence hierarchy, aligned with S2 R14 / S5 R17.

**Self-interview (SD1–SD10, run visibly pre-spec; SD1/SD2 adversarially deep — full text in
thread):** SD1 lane independence = mechanical isolation + journaled input manifests + read-only
reviewer sandboxes + lens diversity + the Claude live slice (guards the O1 N-of-1 collapse and
COH-17's builder-checks-itself). SD2 concordance mechanics + the shared-source-universe limitation
stated openly with its three compensating instruments (guards concordance theater). SD3 evidence
hierarchy CL → 2-independent-whitelist-sources; absence queries batch through the builder lane
(one-credential rule). SD4 roster codification incl. executing the LINT-12/13/14 re-pointing and
rebuilding LINT-3 lake-driven per the F-DEMO-001 adjudication. SD5 sampled-re-run mechanics
(risk-chosen + one random category; evidence-triggered tripwire). SD6 self-audit upgrades
(manifest-diff blindness). SD7 contradiction sweep ≠ shingle detector. SD8 tier-sampled TEACH-03
(T3 re-verifies G2). SD9 pending markers re-polled twice (P4 + gate). SD10 negative scope (no
relitigation, no deck work, no content redesign).

**Audit intake (every injected:S9 row + named rows dispositioned — AUDIT-CLOSURE gate):**
- **COH-17** ADOPT — the ≥1-in-10 identity spot-check routes to the Claude lane (R5/R11); widened
  into the full independence architecture (R1/SD1: manifests, read-only sandboxes, lens diversity).
- **COH-21** ADOPT — the numeric roster codified (R8) **including the `LINT-S2-*` → LINT-12/13/14
  re-pointing S1 A5 promised but S2's text never executed** (closure-verifier finding; the S2
  cross-spec note below records the rename; aliases deprecated, table normative).
- **COH-27** ADOPT — pending-marker re-poll is R7.1 + R14.8 (polled at P4 AND re-confirmed at the
  gate): *Carter* No. 25-885, *Noem* (S6's watch row), the *Lange* reservation (S7 §9).
- **COH-28** ADOPT-ADAPTED — the LINT-3 fix folded into the roster, but **not** as the ticket's
  window patch: the live F-DEMO-001 panel killed that fix (breaks true positives two ways) and the
  adjudication lands the S1 A2 lake-driven rewrite instead, with the committed acceptance fixture.
  The ticket's "content verified correct" premise was refuted (TEACH-01 owns the content half; the
  two live HIGHs stay red until S7 relocates them). `_review-needed/lint3-…-false-positive.md`
  closes when both halves land at EXECUTE.
- **TEACH-02b** ADOPT — LINT-11 built per the S1 A2 class→check table (R8 #11).
- **TEACH-11** ADOPT — mnemonic lint gains wikilink-target + register-wording checks (R8 #8).
- **NUM-03** ADOPT-ADAPTED — boundary per the S8 Decision Log: content remediation = S8 R6; S9
  keeps LINT-9 + re-verification (R8 #9, R9(a)); sizing re-measured at EXECUTE (drift already
  observed: ~404 mid-line/267 files on 2026-07-04 vs the audit's 299/233).
- **S2F-07b** ADOPT — the provisional-slug prose recheck after S3 binding is R10(a).
- **S7-interview inputs (a)–(e)** ALL ADOPTED — (a) `opinions[].id` resolution before any document
  read (R1 lane rules + §4; re-confirmed live by the S8 thread); (b) per-item G2 (R3, flashlight
  fixture); (c) the cross-page contradiction sweep (R6); (d) tier-sampled TEACH-03 re-verification
  (R11); (e) LINT-10's block unit + parenthesized Sources info (R8 #10).

---

## Cross-spec notes filed with this spec

**S2 § (roster rename record).** `LINT-S2-schema` ≡ **LINT-13**, `LINT-S2-drift` ≡ **LINT-12**,
`LINT-S2-pagerecord` ≡ **LINT-14** (S1 A5 mapping, executed by S9 R8's normative table). S2's
spec text stands as written; its lint names are deprecated aliases from this date.

**S6 § Amendments A2 (proposed by S9, 2026-07-04) — dual-model frontier discovery.** Extends
S6 R6 (no text superseded): at EXECUTE, each category's frontier discovery runs BOTH a Claude
lane and a Codex `web_search` lane (recipe per S9 R7; feasibility verified 2026-07-04), finds
unioned before the R7 candidate queue. Per the user's note: the first iterations were
Claude-only; model diversity in discovery is now required. (Precedent: S8's A14 filing into S2;
S7's A1 filing into S6.)
