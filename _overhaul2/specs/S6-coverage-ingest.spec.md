# SPEC S6 — Coverage & Ingest (verify + author missing cases)

**Status: APPROVED (signed at interview, 2026-07-03).**
gates: S2 (stub pre-seed, lake machinery), S3 (tree + placed-empty nodes), S5 (entry models — pages born conformant). Authoring order only; execution = wave 3 (RUNBOOK §3, COH-04).

Interview: 2026-07-03 (2 rounds, 8 user decisions D1–D8) + visible self-interview (SD1–SD8).
Exhibits: `~/briefs/2026-07-03-cssi-s6-roster-exhibit.html` (roster decomposition + why-missed
diagnostic) · specimen page `content/cases/United States v. Smith (2024).md` (live on the branch —
authored, two-key-verified, born S5-conformant; closed roster row 77 on re-scan: 89 → 88).

Precedence: this spec wins over RUNBOOK §4-S6 and the S6 wrapper (RUNBOOK §0 stack).

---

## 1. Objective

Close the coverage gap between "cases the corpus relies on" and "cases the corpus verifies": run
every named-but-no-page caption, every audit-injected gap case, and a bounded frontier through the
two-key existence protocol, then **author a born-conformant BIRAC page for everything real that
passes the officer-field-relevance gate** (user D1: the O1 "persuasive-only → no page" default is
FLIPPED), remove nothing without human sign-off, and hand S7/S8 a machine-readable coverage ledger
in which every candidate has exactly one terminal state. Coverage completion is measured against
the union (book ∪ named-in-prose ∪ prior-research ∪ GAP docket ∪ term sweep ∪ frontier), never the
book alone.

## 2. Scope

### 2.1 In scope (S6 owns)
- Existence-verification (two-key) + gate adjudication + authoring for the **S6-SEED roster**
  (89 committed rows; 88 live after the specimen — consumed as seed, not gospel; re-scanned fresh
  at EXECUTE).
- The **GAP docket** (GAP-01b/02b/04a–g) and the **OT2019→present SCOTUS term sweep** (GAP-05).
- The **full frontier pass** per S3 category (user D3) under the stricter frontier floor (user D5).
- The **reusable page-authoring pipeline** (R8) — defined here, invoked by S7 for its finds.
- Alias/variant adjudication (SEED §b) and fabrication-flag resolution (SEED §a).
- The **coverage ledger** (R11) — the COH-15 reconciliation artifact S8 consumes.
- Filling S3's placed-empty nodes with their anchor cases (S3 R7; prose remains S7's).
- Human pauses #2 (fabrication removals) and #3 (borderline sign-off) — packet design + timing.

### 2.2 Out of scope (owned elsewhere)
- CL credential + lake writes: **S2's builder owns the token** (S1 A1/L4′); S6 reaches CL only
  through the R7 candidate queue and reads stubs/lake. Claude CL MCP = interactive spot-checks only.
- Page FORMAT decisions: settled by S5 (R3/R6/R7/R12/R15) — S6 pages conform, never re-interview.
- Doctrine prose (S7), corpus-wide linking of all 388 bare mentions (S8), release verification (S9).
- The officer-BLUF / field-application layer: **banned project-wide** (S1 §2.2 + R6); no S6 page
  carries one.
- The recurring citator/coverage watch → GH#2 maintenance loop.

## 3. Requirements (each testable)

**R1 — Two-key existence verification, first and always.** Every candidate (roster, GAP, sweep,
frontier) is verified before any author/remove/exclude decision: **Key 1** CL identity via the S2
stub (cluster → lead opinion per the three-source rule; caption, court, date, cite); **Key 2** an
independent confirmation (web/official reporter) plus the **input-name vs CL-canonical comparison
done by us** (the auto warning is masked by cite dedup). **"Not found ≠ fabricated"**: a Key-1 miss
routes to the L6-style escalation (cite → name variants → proposition full-text → web → relocate);
only a full-ladder miss lands `unverifiable`. *Check:* every ledger row carries both key results (or
the ladder trace); zero pages authored from a `not_found`/`fabrication_suspected` stub; canonical-
name mismatches are adjudicated, never silently normalized. `PROCESS` + S9 ≥1-in-10 re-verify.

**R2 — The officer-field-relevance gate (O1 R1 inherited, prong (c) widened; user D1/D6 — SD1).**
INGEST iff (a) **field conduct** ∨ (b) **admissibility/suppression** ∨ (c) **officer civil-liability
exposure, including its SCOTUS boundary markers (Bivens, FTCA, forfeiture)**; EXCLUDE iff purely
prosecutor/defense/trial craft (an EXCLUDE names the craft it belongs to). The gate is applied to
everything every seed leg surfaces. **Under the flip (D1), every gate-passing, two-key-real
named-in-prose case earns a page** — persuasive-only is a weight label, no longer an exclusion
ground. Writer lane proposes verdict + prong + one-line rationale; a non-writer lane re-checks
≥1-in-10; disagreement auto-promotes to the borderline packet. *Check:* every ledger row has
verdict + prong; a sample of EXCLUDEs is genuinely trial-only; a sample of INGESTs is genuinely
field-relevant; spot-check disagreements appear in packet B. `PROCESS` · `CHECKLIST`.

**R3 — Borderline sign-off, batched (human pause #3; user D4).** Gate-ambiguous candidates are not
auto-decided. They accumulate into **one packet** (`_run/s6-borderline.md`, O1 format: case ·
proposition · the specific ambiguity · recommended disposition), surfaced **once, after the
candidate universe closes** (R10 ordering); dispositions fold back into the ledger. Known members
at signing: *Wyman v. James*, *G.M. Leasing*, *Verdugo-Urquidez* (thin field nexus — rec. INGEST),
*Chapman v. California* (harmless error, trial-side — rec. EXCLUDE), 6th-Cir. *Carpenter* remand
(rec. own page, SD6). *Check:* no borderline is authored or dropped without a recorded user
disposition; the packet exists even if empty. `PROCESS` (enumerated pause).

**R4 — Fabrication resolution, batched early (human pause #2; user D4 — SD5).** SEED §a rows
(*Mayville, Small, Lyle, Moore-Bush*) + any `fabrication_suspected` stub re-run the two-key under
O2's protocol. Packet A (`_run/s6-fabrications.md`) carries verify results + a recommended
author/remove per case and pauses for the user **early** (stub flags exist from wave 1). Approved
removal = prose surgery at every mention site (re-anchor or rewrite; coordinated with S7) + an
omissions-register tombstone + a ledger `removed` row — never silent deletion, never auto-delete.
The second bare "*United States v. Jackson*" (O1 S5 R9) is adjudicated in its Exclusionary-Rule
context, not by caption. *Check:* every §a row reaches a terminal verdict with user sign-off;
zero removals without a packet-A entry; post-removal grep finds no dangling mention. `PROCESS`.

**R5 — The seed legs (the candidate universe).** The diff runs over the union of: **(i)** the
S6-SEED roster (re-generated at EXECUTE — `_overhaul2/scripts/audit_cases.py`); **(ii)** the book-
roster residual + O1 omissions register + O1 185-list (prior-research floor — may not regress);
**(iii)** the **GAP docket**: GAP-01b (*Nieves*, *Gonzalez*), GAP-02b (*Thompson*, *Chiaverini*),
GAP-04a *Cooley*, 04b *Lombardo*, 04c *Culley*, 04d *Egbert* (reopened; user D6 = AUTHOR), 04g
*Martin* (D6 = AUTHOR), 04e *Noem* (watch-item, not authored), 04f *Villarreal* (rejected,
trial-side); **(iv)** the **OT2019→present term sweep** (user D7): per Term, every SCOTUS merits
decision + noted shadow-docket order in 4A / 5A-interrogation / 6A-field / §1983-QI-FTCA space,
each run through R1+R2; **(v)** the **frontier** (R6). *Check:* the ledger accounts for every
member of every leg; the sweep list per Term is enumerated in the run artifacts; the prior-research
floor holds (no O1-confirmed case regresses to page-less without a ledger reason). `PROCESS`.

**R6 — The frontier: full O1-style discovery, stricter inclusion floor (user D3 + D5).** Per S3
category: **web-first discovery** (terminology/theories/candidate names; web never asserts) → CL
confirmation **via the R7 queue** → ≤2 expansion hops beyond seed → the PRACTICES §4 **saturation
stops** (new searches only resurface known cases · both directions run on key cases · every circuit
accounted for or the split flagged · no unaddressed first-impression markers · 2nd tool
cross-checked · adverse authority captured). **Inclusion floor for frontier finds:** a page only if
**clearly controlling** (Binding — SCOTUS, or binding-in-circuit on a question the corpus omits) or
a **split-marker** (both sides, circuits named); other real+relevant finds enter as Lower-court-
developments bullets (S5 R11) — bullet-cases convert to page candidates only when S7's prose comes
to rely on them (via R8's pipeline). *Check:* per-category log shows hop bound + a satisfied stop
condition; every frontier page cites its controlling/split justification; no doctrine page balloons
past the S1 digestibility budget from frontier adds. `PROCESS` · `CHECKLIST`.

**R7 — The candidate queue (the one-credential rule holds — SD2).** S6 never calls the CL REST API.
Frontier/sweep candidates not already in the lake are emitted as per-category
`_run/s6-candidates/<category>.jsonl` batches (caption, proposition, doctrine node, discovery
evidence); **S2's builder lane** ingests each batch through its existing identity+fabrication
machinery → frontier stubs (S2 R11 states; A6 record_ids); S6 gates and authors **only from
stubs**. Discovery (web, no CL) is scheduled early and batched large; the closed lists (GAP docket,
term sweep) run while stub batches turn around. The Claude MCP lane stays interactive-spot-check
only. *Check:* zero CL REST calls from S6 code paths; every authored page's record pre-exists its
page (the S2 R12 page↔record lint holds by construction); the queue + stub journal make the
frontier resumable with no re-burned quota. `AUTO` (lane audit) · `PROCESS`.

**R8 — One reusable authoring pipeline (SD3; pages born conformant).** Input: a `verified_identity`
stub + home node(s) + role(s). Output, atomically: a BIRAC page in the **S5 R3 skeleton** with the
projected frontmatter shape, tables per **R6 schemas** (no authored data in cells, R7 boundary),
**R12 bracketed Sources**, `opinion` anchor text, pins per R16, born `lake.status: draft` (banner
per R15 until promoted); the stub→record promotion (S2 A6 rename + manifest entry); a Case-Index
row; a Key-cases/Related row on each `homes[]` page; a ledger `authored` row. History-cluster pages
(user D2: *Sanders*, *Trupiano*, *Frank v. Maryland*, *Robbins*, + *Quantity of Books* pending its
normalization fix) render as **history** per PRACTICES §7 — precise verb, forward-pointer to the
successor, visual demotion, never disguised. **S7 invokes this same pipeline** for rewrite-time
discoveries — no second page-mint exists. *Check:* every S6 page passes LINT-15/16 on creation;
every promoted stub has a manifest rename entry; a sampled history page carries verb + successor
pointer; S7's spec references R8 (coherence pass). `AUTO:LINT-15/16` · `PROCESS`.

**R9 — Alias/variant adjudication (SEED §b — SD6).** Same-case caption variants → **one page +
`aliases:`** (*Alasaad v. Mayorkas/Wolf* = one 1st-Cir. case). Same-litigation distinct decisions →
**fold-by-default** into the terminal page's Treatment & subsequent history (4th-Cir. en banc
*Chatrie* folds into the SCOTUS *Chatrie* page) **unless** the earlier decision's own point is
load-bearing in prose (6th-Cir. *Carpenter* good-faith remand → packet B, rec. own page).
Distinct-case surname coincidences (*U.S. v. Davis* 4th Cir. 2021, *U.S. v. Lewis* 6th Cir. 2023,
*U.S. v. Wilson* 9th Cir. 2021) → normal roster rows; year/court disambiguated filenames (the
specimen's two-Smiths collision is the standing exhibit). Scanner normalization hardened: leading-
article fold ("A Quantity…"), successor-official fold (Mayorkas/Wolf). *Check:* zero blind merges
(each §b row carries an adjudication note); no case split across two pages (S1 A3 shingle detector
+ Case-Index uniqueness); the scanner re-run post-fix reclassifies *Quantity* correctly. `PROCESS`
· `AUTO` (scanner assertions).

**R10 — Execution ordering (SD4).** (1) SEED verification off wave-1 stubs → **packet A** early;
(2) GAP docket + term sweep (closed lists); (3) frontier per category through the R7 queue;
(4) **packet B** once the universe closes; (5) authoring waves (R8) as sign-offs land — GAP/sweep
pages need not wait on frontier saturation. UNVERIFIABLE carry-forwards (*Cruz, West, White*) stay
page-less flagged exceptions unless R1 ever passes. *Check:* run journal shows the two pauses
landed in order with evidence attached; no authoring precedes its stub + gate verdict. `PROCESS`.

**R11 — The coverage ledger (COH-15 joint reconciliation — SD7).** S6 emits
`_run/s6-coverage-ledger.json`: one row per distinct caption in the candidate universe —
`{caption, canonical, cluster_id|null, leg(s), gate: {verdict, prong, rationale}, keys: {cl, independent},
terminal: authored|brief-mention|excluded-remit|unverifiable|removed|folded-alias|watch, pointer}`.
The **388-mention reconciliation is a ledger property, not a prose claim**: NUM-04's 388 distinct
bare-mention captions ⊇ (existing-page set ∪ S6 terminal states); **S8 links every mention whose
caption has a page and applies its own rule (opinion-link/plain) to the rest, reading this ledger**
— the numbers (388 / 89→88 / authored-N) reconcile row-by-row. *Check:* ledger partitions the
universe completely (no caption without exactly one terminal state); S8's spec names this file as
its input; NUM-04/NUM-05 figures re-derive from it. `AUTO` (schema + partition check).

**R12 — The why-missed diagnostic → standing defenses (SD8).** Every terminal `authored` row from
the roster carries ≥1 why-missed class; each class ships its generalized defense: **class 2**
(prose-grew-past-roster) → the seed scanner becomes a **CI lint** (a prose caption resolving to no
page fails the build unless the ledger records a terminal non-page state; proposed LINT-17, named
finally under S9's COH-21 pass); **class 4** (caption drift) → the R9 normalizer folds, committed
in `audit_cases.py`; **class 7** (structural blindness to never-named law) → the term sweep (R5.iv)
now, the GH#2 citator watch recurring. *Check:* LINT-17 (or successor name) is in `scripts/lint/`
with the ledger-allowlist wired; a synthetic new bare caption fails CI; the sweep artifact exists
per Term. `AUTO:LINT-17` · `PROCESS`.

## 4. Lessons enforced

**The O1 scar set:** web-discovery scouts inventing frameworks (*Mayville/Lyle/Small*) and reversing
holdings (*Moore-Bush*) → R1's two-key + R4's human-pause removal lane + R7's web-discovers/stub-
confirms split. **Named-but-no-page drift** (~70–80 grew silently) → R12's CI lint so the class can
never regrow unwatched. **Caption traps** (cluster≠opinion ids; two same-caption 5th-Cir. Smiths a
week apart; Alasaad's successor-secretary captions) → R1's canonical comparison + R9's adjudication
rules. **"Not found ≠ fabricated"** cuts both ways: the escalation ladder before any `unverifiable`,
and no resurrection without verification. **Persuasive-only invisibility** (51 deliberate O1
exclusions rediscovered as "misses") → R11's ledger: deliberate exclusion is now a recorded terminal
state, auditable against "missed again."

## 5. Method (execution — wave 3)

1. Regenerate the roster (`audit_cases.py`, post-R9 normalizer fixes); reconcile against S2's stub
   manifest; verify SEED rows off existing stubs (R1) → emit **packet A** (R4).
2. Enumerate the GAP docket + the OT2019→present term sweep (R5.iii/iv); gate (R2); queue any
   lake-missing candidates (R7).
3. Frontier per S3 category (R6): web discovery → `candidates.jsonl` → S2 stub batches → gate.
4. Close the universe; emit **packet B** (R3); fold dispositions.
5. Authoring waves via R8 (GAP/sweep first, then roster conversions, then frontier passers);
   history cluster per D2; aliases per R9.
6. Emit the coverage ledger (R11); wire LINT-17 (R12); hand S7 the pipeline entry point + ledger,
   S8 the ledger.

## 6. Deliverables

- `_run/s6-coverage-ledger.json` (R11) · `_run/s6-borderline.md` + `_run/s6-fabrications.md`
  (R3/R4 packets, with dispositions folded back) · `_run/s6-candidates/*.jsonl` (R7).
- ~95–130 new `content/cases/` pages (est.): ≈60–70 roster conversions (88 minus remit-fails,
  unverifiables, alias-folds) + 9 GAP pages + sweep passers + frontier passers — every one born
  S5-conformant via R8, `draft` until S9 promotion.
- Scanner/normalizer hardening in `_overhaul2/scripts/audit_cases.py` + LINT-17 in `scripts/lint/`.
- Per-Term sweep artifacts; per-category frontier logs (hop bound + stop condition).

## 7. Acceptance criteria

- [ ] Every candidate-universe caption has exactly one ledger terminal state with two-key evidence
      (R1/R11); the partition is complete and machine-checked.
- [ ] Zero pages authored from unverified/fabrication-flagged stubs; zero CL REST calls from S6
      lanes (R7); every page's lake record predates the page.
- [ ] Both human-pause packets surfaced with recommendations and returned with recorded user
      dispositions before any removal/borderline authoring (R3/R4).
- [ ] All gate-passing named-in-prose cases have pages (D1 flip realized); frontier pages each
      carry a controlling/split justification (D5); history cluster renders as history (D2).
- [ ] GAP docket dispositions match D6/D7 (author: Nieves, Gonzalez, Thompson, Chiaverini, Cooley,
      Lombardo, Culley, Egbert, Martin; watch: Noem; reject: Villarreal) and are ledger-recorded.
- [ ] Every S6 page passes LINT-15/16 at creation; LINT-17 live with the ledger allowlist; the
      S3 placed-empty nodes hold their anchor cases.
- [ ] S7's spec references R8's pipeline; S8's spec references R11's ledger (coherence pass checks
      both).

## 8. Verification plan

S9 re-verifies ≥1-in-10 gate verdicts and two-key results through the **Claude lane** (COH-17
routing); the writer≠checker rule holds per page (the R8 author lane never self-certifies; S9's
panel reviews). Quote fidelity + pincites on authored pages ride the 10-gate protocol (G1–G10).
The ledger partition check, LINT-15/16/17, and the lane audit (R7) run in CI. The specimen page
(*U.S. v. Smith (2024)*) re-enters the pipeline at EXECUTE like any authored page — it carries
`under_review` until the gates pass, and its roster row stays closed only if promotion succeeds.

## 9. Open items / escalations

- **Sweep enumeration source** (per-Term SCOTUS docket lists): compiled at EXECUTE from official
  Term summaries + cross-checked against CL; if enumeration proves noisy, escalate the source
  choice to a run-time note, not a new interview.
- **Estimated authoring volume** (~95–130 pages) is a planning figure; if the frontier floor
  (D5) still yields >150 pages, pause and surface the count before authoring (scope guard).
- **`Quantity of Copies of Books`** rides the R9 normalizer fix; if the O1 borderline disposition
  (brief-mention) conflicts with the D1 flip at EXECUTE, it goes to packet B (rec. INGEST as
  history).
- ***Carter v. United States* (D.C. 2025)** overlaps S9's COH-27 cert-watch (No. 25-885): author
  per the flip; the watch marker stays until the cert petition resolves.
- **Zorn v. Linton / LLC v. John Doe residue**: the corrupted-object legend cleanup is S7's
  (LAW-05); S6 only ensures *Zorn*'s roster row terminates correctly (author — 2026 SCOTUS §1983).

## 10. Decision log

**User decisions (interview 2026-07-03):**
- **D1 — The flip.** Every two-key-real, gate-passing named-in-prose case earns a BIRAC page;
  "persuasive-only" becomes a weight label, not an exclusion ground. (Round 1, Q1 — chose
  maximal over the recommended structural middle.)
- **D2 — History pages.** *Sanders/Trupiano/Frank/Robbins* (+ *Quantity*, pending R9 fix) authored
  as full history-rendered pages, not index rows.
- **D3 — Full frontier.** O1-style bounded progressive frontier (≤2 hops, web-first → CL) runs
  inside S6 per S3 category. (Chose thorough over the recommended light split-probe.)
- **D4 — Two batched pause packets.** Fabrications early (packet A), borderlines after
  universe-close (packet B).
- **D5 — Stricter frontier floor.** Frontier finds: page iff controlling or split-marker; bullets
  otherwise; bullet→page conversion only when S7 prose relies on it.
- **D6 — Remit line widened at the SCOTUS boundary.** *Egbert*, *Martin*, *Culley* authored (with
  *Nieves/Gonzalez/Thompson/Chiaverini/Cooley*); R2's prong (c) codifies it.
- **D7 — Term sweep signed as proposed.** OT2019→present, four buckets, merits + noted shadow
  docket; *Noem* = watch; *Villarreal* = reject-with-rationale.
- **D8 — Open floor closed** with nothing to add.

**Self-interview (SD1–SD8, run visibly pre-spec):** SD1 gate mechanics (O1 R1 inherited, prong (c)
widened; writer-proposes/non-writer-re-checks; EXCLUDE names its craft) — guards scope creep and
silent under-inclusion. SD2 candidate queue through S2's lane (rejected: MCP-lane batch use; own
token) — guards the one-credential rule, makes pages born with records. SD3 single reusable
pipeline (S7 invokes) — guards format drift. SD4 ordering — guards evidence-less pauses. SD5
removal = prose surgery + tombstone + ledger — guards silent deletion. SD6 alias rules
(fold-by-default; load-bearing exception) — guards blind merges and split pages. SD7 ledger as the
COH-15 artifact — guards numbers-by-assertion. SD8 lint conversions — guards class regrowth.

**Audit intake (every injected:S6 row dispositioned):**
- **GAP-01b** ADOPT — *Nieves* + *Gonzalez* authored into S3 A5's Retaliatory Arrest node (R5.iii).
- **GAP-02b** ADOPT — *Thompson* + *Chiaverini* authored into the Malicious Prosecution node.
- **GAP-04a** ADOPT — *Cooley* authored (unanimous SCOTUS, field authority).
- **GAP-04b** ADOPT — *Lombardo* authored; per-curiam QI pages have corpus precedent
  (*Kisela/Tahlequah/Rivas-Villegas/White v. Pauly*) — self-resolved, logged.
- **GAP-04c** ADOPT — *Culley* authored into the placed forfeiture node (user D6).
- **GAP-04d** ADOPT (reopened) — *Egbert* authored (user D6 overrides O1 OPTIONAL-tier).
- **GAP-04e** ADAPT — *Noem* = watch-item ledger state, not authored (stayed posture, no merits).
- **GAP-04f** REJECT-WITH-RATIONALE — *Villarreal*: 6A recess consultation is trial-side; outside
  the R2 remit (user D7 confirmation).
- **GAP-04g** ADOPT — *Martin* authored alongside Egbert (user D6).
- **GAP-05** ADOPT — the term sweep is R5.iv, a named seed leg; recurring version routed to GH#2.
- **COH-15** ADOPT — the 388/88 split reconciles in R11's ledger; S6 authors the no-page subset,
  S8 links all 388 reading the ledger (joint reconciliation delivered as a machine artifact).
- **COH-02a / NUM-05** ADOPT — `_overhaul2/S6-SEED.md` consumed as the committed roster
  (seed-not-gospel; re-generated at EXECUTE; live count 88 after the specimen closed row 77;
  the committed file stays the 2026-07-02 snapshot — regenerate, don't hand-edit).
- **NUM-04** (routed via S8) — acknowledged as the 388 measured input to R11; no S6-side change.

---

## Amendments — 2026-07-03 (S7-interview intake)

### A1 — Planning-time candidate sub-leg (extends R5; no text superseded)
The S7 interview's verified research (2026-07-03; research annex in `S7-doctrine-production.spec.md`)
surfaced gate-relevant captions before EXECUTE. They join the R5 union as named sub-leg
**(ii-b) planning-time discoveries**, consumed like any leg (R1 two-key → R2 gate → R10 ordering →
R8 authoring); nothing below pre-adjudicates a verdict, and the D5 frontier floor still decides
page vs Lower-court-developments bullet:
- **Knock-and-talk** (already named in prose on the branch — mockup commits `e0935ce`/`4b48a4a`,
  so the R12/LINT-17 class is live for these four): *Morgan v. Fairfield County*, 903 F.3d 553
  (6th Cir. 2018) · *People v. Frederick*, 895 N.W.2d 541 (Mich. 2017) · *State v. Christensen*,
  517 S.W.3d 60 (Tenn. 2017) · *Carroll v. Carman*, 574 U.S. 13 (2014) (per curiam).
- **SACO / constructive entry** (S7 user D7): *United States v. Nora*, 765 F.3d 1049 (9th Cir.
  2014) · *Fisher v. City of San Jose*, 558 F.3d 1069 (9th Cir. 2009) (en banc) · *United States
  v. Al-Azzawy*, 784 F.2d 890 (9th Cir. 1986) · *United States v. Maez*, 872 F.2d 1444 (10th Cir.
  1989) · *United States v. Allen*, 813 F.3d 76 (2d Cir. 2016) · *United States v. Vaneaton*,
  49 F.3d 1423 (9th Cir. 1995).
- **Caretaking-of-persons** (S7 user D5): *Graham v. Barnette*, 5 F.4th 872 (8th Cir. 2021) ·
  *United States v. Morgan*, 71 F.4th 540 (6th Cir. 2023) · *United States v. Treisman*, 71 F.4th
  225 (4th Cir. 2023) · *Bakutis v. Dean*, 129 F.4th 299 (5th Cir. 2025).
- **Collective knowledge (horizontal split)**: *United States v. Massenburg*, 654 F.3d 480 (4th
  Cir. 2011) · *United States v. Chavez*, 534 F.3d 1338 (10th Cir. 2008) · *United States v.
  Cook*, 277 F.3d 82 (1st Cir. 2002) · *United States v. Balser*, 70 F.4th 613 (1st Cir. 2023).

**R9 adjudication flags booked now** (blind-merge prevention): *Fisher v. City of San Jose* ≠ the
existing *Michigan v. Fisher* page; **three distinct Morgans** (*Morgan v. Fairfield County* (6th
Cir. 2018) · *United States v. Morgan*, 743 F.2d 1158 (6th Cir. 1984) · *United States v. Morgan*,
71 F.4th 540 (6th Cir. 2023)) — distinct-case rows, never folded. **Supersession note:** 9th-Cir.
*United States v. Anderson* is cited as the **en banc** 101 F.4th 586 (2024); the 2022 panel
(56 F.4th 748) is superseded and must not be page-minted.

*Rationale (decision-log-grade):* R8 would catch each of these as a rewrite-time discovery, but
only as a mid-wave trickle; pre-seeding books them into the batched verification lanes and books
the alias traps before any page-mint. No requirement text changes; the R5 union was built to be
extended by named legs.
