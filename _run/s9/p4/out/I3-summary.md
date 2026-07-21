# I3 summary — S9 R7.3 dual-TOC doctrine audit (packet I3)

lane/model: I3 / claude-opus-4-8. Findings-only; no verdicts. WRITE-SCOPE `_run/s9/p4/` only.

## COH reuse statement
`_run/s9/p4/out/COH-report.json` did **not** exist at packet start (checked; only MER-*/S8H-*/B-* artifacts present). Therefore I did **not** reuse a COH callout inventory — I derived registry-point presence directly against each home_page.

## Half (1) — registry-point home-statement PRESENCE (R10 substrate)

**Scope: 80 points assigned / 80 examined / 0 skipped.** Registry parsed via `scripts/lint/_common.py::parse_yaml_subset` (`_overhaul2/points/registry.yaml`, `nodes:` → 80 nodes). Presence, not deep-equality (deep-equality R10 callout↔registry gate is COH's).

Method: for each node, extracted party-v-party case names (`CASE_RE`) + doctrinal key terms from `statement`, matched against the home_page file text. 75/80 fully covered by statement-case presence on the first pass. The 5 that the automated case-match could not auto-confirm were read/greped individually:

- `warrant.requirement` (`content/the-warrant/index.md`): core substance PRESENT — index states all four validity requirements verbatim (probable cause · neutral and detached magistrate · oath or affirmation · particularity as to place/things). The statement's secondary *Leon* good-faith clause is not on the index page; that doctrine is homed at `The Good-Faith Exception.md` and cross-referenced. **PRESENT** (the Leon-clause omission is a deep-equality nuance → flagged below for COH, not a presence gap).
- `search.tents` (`Tents.md`): PRESENT — 51 "tent", "temporary dwelling", "Katz", "expectation of privacy", "campground" all on page.
- `seizure.collective-knowledge` (`Collective Knowledge and the Fellow-Officer Rule.md`): PRESENT — "collective-knowledge", "fellow-officer", "imputed" (21), "bulletin", "dispatch", "pool" all present.
- `search.special-needs` (`Special Needs and Administrative Searches.md`): PRESENT — "special need" (14), "normal need for law enforcement" (2), "reasonableness balanc" (3), "suspicionless" (13).
- `confession.voluntariness` (`Due-Process Voluntariness of Confessions.md`): PRESENT — "totality of the circumstances", "coerc" (28), "overbore/overbear" (14), "due process", "voluntar" (41).

**Result: 80/80 points have their substance stated on the home_page. Zero presence findings.**

Observation for COH (not a finding, my remit is presence only): `warrant.requirement` statement asserts the *Leon* good-faith clause, which is not present on `content/the-warrant/index.md`. If the R10 deep-equality gate compares the full statement to the home callout, this may surface there.

## Half (2) — chapter/section-grain sweep of both reference TOCs

Grain decision: swept at **section grain** (each `§ X.Y`/`Section X.Y` bolded entry is one "chapter/section topic"), consulting subsections as evidence. Subsection (a)–(n) grain was used to characterize a section's coverage but not to mint one row per sub-subsection (that would be ~600 noise rows against the brief's "chapter/section topic" unit). Coverage tested against: doctrine page, section of a page, or case coverage — searched `content/` (90 doctrine/index pages + 610 case pages) before any zero-home call.

Outputs:
- `_run/s9/p4/out/I3-toc-dispositions.jsonl` — **all 142** topic rows (compact, `p4.toc-disposition.v1`).
- `_run/s9/p4/out/I3-findings.jsonl` — **11** zero-home candidate rows (`p4.candidate.v1`, `class:toc-gap`) — every topic dispositioned out-of-remit or gap-escalate, so the orchestrator can adjudicate the out-of-remit calls. `covered`/`covered-elsewhere` have a corpus home so they are NOT emitted as findings (the row's "no corpus home" claim would be false); `unknowable-from-capture` is a capture-limit marker, not a no-home determination, so it is recorded in dispositions only.

### Coverage stats

| TOC | topics | covered (dedicated) | covered-elsewhere | out-of-remit | unknowable | gap-escalate |
|-----|-------:|--------------------:|------------------:|-------------:|-----------:|-------------:|
| LaFave (Ch 1–11 + back matter) | 90 | 49 | 32 | 9 | 0 | 0 |
| NJLEH (Ch 1–13 + region markers) | 52 | 35 | 11 | 2 | 4 | 0 |
| **Total** | **142** | **84** | **43** | **11** | **4** | **0** |

Covered-or-covered-elsewhere = 127/142 (89%). **Zero true doctrinal gaps** — expected, since the corpus was purpose-built for exactly this domain (federal search-and-seizure + confessions + counsel + eyewitness/fair-trial).

### out-of-remit dispositions (11) — with reason (all flagged to findings for adjudication)
LaFave: §1.11 Expungement of arrest records (civil records remedy) · §1.12 Injunction/Lyons standing (equitable-remedy/standing; damages remedy §1983 is homed) · §1.13 Self-help/resistance to illegal arrest (substantive state criminal law) · §4.12 Miscellaneous warrant requirements — return/receipt (Rule 41 ministerial mechanics) · §4.13 Subpoenas duces tecum (grand-jury/5A compelled-production, distinct from warrants) · §11.1 Waiver/forfeiture of objection (trial-preservation procedure) · §11.2 Motion to suppress mechanics (suppression-motion procedure; substantive standards + standing homed) · §11.5 Prospective/retroactive application of new rules (retroactivity/habeas doctrine; Davis good-faith piece is homed) · LaFave back matter (reference apparatus).
NJLEH: §1.8 Extra-Territorial Arrests (state territorial-jurisdiction/fresh-pursuit law; federal extraterritorial-*search* Verdugo is separately covered) · §2.7 Telephonic Search Warrants (procedural warrant-issuance mechanism; constitutional core homed).

Borderline calls the orchestrator may want to re-rule (I chose covered/covered-elsewhere but flag them): §1.9 Challenge of jurisdiction → covered-elsewhere via Lopez-Mendoza (body/identity-not-suppressible), but the Ker-Frisbie forcible-abduction-doesn't-void-jurisdiction sub-point is not separately homed. §11.6 impeachment and §11.7 Stone-v-Powell/harmless-error are covered-elsewhere only for their doctrinally-significant holdings; pure appellate-review mechanics within them are out-of-remit.

## NJLEH capture limitation (stated, per brief)

The NJLEH TOC (`_run/s9/p4/toc-njleh.md`) is a **bounded capture**: it is a Blue360° product-page web outline with **no printed page numbers**, transcribed from a 3-page PDF that **terminates mid-tree at Vol 2, Ch 13, §13.2**. Consequences for this sweep:
- **Ch 1–12: complete** and swept at section grain (48 sections, all covered/covered-elsewhere except the 2 out-of-remit above).
- **Ch 13: partial.** Only §13.1 (Introduction) and §13.2 (Cases and Materials) titles are captured; capture ends AT §13.2 (line 126 marker). Both are marked **`unknowable-from-capture`** — the titles nominally align to the well-populated `content/use-of-force-and-liability/` section (Section 1983, Qualified Immunity, Malicious Prosecution, Bivens/FTCA, Absolute Immunity, Civil Forfeiture, Use of Force, Retaliatory Arrest), but a truncated chapter cannot be certified as covered.
- **Ch 13 remainder (beyond §13.2)** and **Volume 3 (entire)** — the publisher's marketing text calls it a "comprehensive three-volume guide," yet only Vol 1–2 appear in the capture. Both are recorded as **`unknowable-from-capture`** region markers (not covered, not gap) — their topics cannot be enumerated or assessed from the captured pages.

Per the brief, no Ch-13+/Vol-3 region is marked "covered."

## Deterministic coverage
- Half (1): 80 registry points assigned / 80 examined / 0 skipped. 0 presence findings.
- Half (2): 142 TOC topics dispositioned / 142 examined / 0 silently skipped. 4 rows are explicit `unknowable-from-capture` markers (Ch13×2 + Ch13-remainder + Vol3), not skips. 11 out-of-remit findings; 0 gap-escalate.

## Ambiguities for the orchestrator
1. Half-1 `warrant.requirement` Leon-clause presence-vs-deep-equality boundary (COH R10 gate territory).
2. The 11 out-of-remit calls are surfaced as findings so out-of-remit vs gap can be adjudicated; §1.9 (Ker-Frisbie sub-point), §11.6, §11.7 are the closest borderline covered-elsewhere calls.
3. TOC sweep grain = section-level by design; if the machine wants sub-subsection (a)–(n) granularity for any specific section, that is a re-scope.
