# S7 mini-lane L2 — SACO / constructive-entry (D7): dispositions + mint handoff

- **lane / model:** o2-execute mini-lane L2 (phase b) / `claude-opus-4-8`
- **generated:** 2026-07-08
- **spec authority:** S7 §3 D7 + §10 R10 + §11 annex; S6 A1 planning-time candidate sub-leg; frontier floor S6 R6 / user D5.
- **identity method:** CourtListener MCP, SEARCH-first, cluster/opinion ids resolved from search results (never guessed). **18 MCP calls total across phases a+b, 0 REST.**
- **machine artifacts:** `S7-L2-SACO-DISPOSITIONS.jsonl` (6c-2 loader; assemble=true → 2 brief-mention terminals); `_run/s6-candidates/arrests-saco.jsonl` (S6 R7 mint handoff); `_run/o2-execute/payloads/{United States v. Nora,United States v. Al-Azzawy,United States v. Vaneaton}.md` (staged BIRAC bodies).
- **provenance rule honored:** coverage ledger regenerated PROGRAMMATICALLY (`build_coverage_ledger.py --write`), never hand-edited; assembler gained a small 6c-2 loader (code delta, rides the standing code gate).

## Berkowitz correction (orchestrator step 2) — ACCEPTED
`content/cases/United States v. Berkowitz.md` exists (7th Cir. 927 F.2d 1376, cluster 557342, homed Arrest in the Home, related Payton/Watson/Knight). The narrow-side (announce-from-outside / physical-crossing) 7th-Cir. representative **IS nameable and wikilinkable** in the D7 section. Phase-(a) fail-closed non-naming of Berkowitz is withdrawn. **Still unnameable** (no page/no terminal → LINT-17 fail-closed): *United States v. Morgan*, 743 F.2d 1158 (6th Cir. 1984) (also an A1 "three distinct Morgans" alias trap — NOT the ledgered *Morgan v. Fairfield County*) and *Knight v. Jacobson*, 300 F.3d 1272 (11th Cir. 2002). Their circuits (6th recognizing, 11th narrow) are taught by honest circuit-naming.

## Terminals booked (assemble=true → coverage ledger)
### 1. Fisher v. City of San Jose — brief-mention (NEW terminal)
- **cite:** 558 F.3d 1069 (9th Cir. 2009) **(en banc)**; pincite 1074–79. **cluster/opinion:** 1355654 / 9597796 (Tallman, J.). **docket:** 04-16095.
- **evidence (MCP lead-opinion read 9597796):** "We address the Fourth Amendment's exigent circumstances doctrine in the context of armed standoffs." Fisher pointed a rifle at officers; en banc majority held exigency present; point-of-seizure / "constructive arrest" analysis in fnn. 4–5.
- **gate rationale:** brief-mention — armed-standoff exigency counterpoint to *Nora*'s exigency-absent holding; not a D7 spec-required page-grain element (Nora is the spine).
- **traps:** R9 alias — Fisher v. City of San Jose (9th Cir.) **≠** Michigan v. Fisher (existing SCOTUS page). Superseded panels **509 F.3d 952 (2007)** and **519 F.3d 908 (2008)** barred from any mint.
- **pointer:** `warrant-exceptions/home-entry-and-search/Entry to Arrest.md` (naming lands with the arrests/D7 batch; terminal booked now per orchestrator step 4).

### 2. United States v. Allen — brief-mention (NEW terminal)
- **cite:** 813 F.3d 76 (2d Cir. 2016); pincite 84–86. **cluster/opinion:** 8442555 / 8413824 (Lynch, J.; Lohier, J. concurring). **docket:** 13-3333-cr.
- **evidence (MCP lead-opinion read 8413824):** "where law enforcement officers have summoned a suspect to the door of his home, and he remains inside the home's confines, they may not effect a warrantless 'across the threshold' arrest in the absence of exigent circumstances" (~84); rests on *United States v. Reed*, 572 F.2d 412, 422–23 (2d Cir. 1978) (*83), approved by *Payton*; protection extends beyond actual trespass (*86).
- **gate rationale:** brief-mention — 2d-Cir. recognizing-side representative; page-eligible but the split is taught with *Nora* as spine, *Allen* as a pincited roster entry (L1 pattern).
- **disambiguation RESOLVED:** the signed 2d-Cir. *Allen* (813 F.3d 76), not *American Honda Motor Co. v. Allen* (7th Cir., 600 F.3d 813) or other namesakes.
- **pointer:** `warrant-exceptions/home-entry-and-search/Entry to Arrest.md`.

## Page mints (assemble=false → BLOCKED, staged + handed off)
**Nora / Al-Azzawy / Vaneaton are PAGE candidates (spine + the two poles of the containment-vs-exit-command line), not terminals.** `mint_page.py` requires a lake stub in `("verified_identity","verified","verified_off_cl")`. For a fresh in-CL frontier candidate that status is reachable **only** through the REST `frontier_identity_selection` leg (S2 builder token). This lane **has no CL token** (`~/.courtlistener*` absent; no env var) and is **barred from CL REST** by standing rule. Offline paths do not reach it: `--add-candidates` yields only a `status:"pending"` UNRESOLVED stub (and the ledger's 6b manifest-residual block would wrongly place such a stub as *brief-mention* — so `--add-candidates` was **deliberately not run**); `--apply-web-keys` / `--repair-identity-from-cache` operate only on already-resolved rows; `--elevate-off-cl` requires the case be absent from CL + 2 R14-whitelisted web sources (wrong semantics — these cases ARE in CL). Per the work-order clause **"if any leg fails … STOP that case and report — never force,"** the mint is stopped at the identity-resolution boundary and reported.

Identity is nonetheless **two-key-verified** via MCP (phase a): cluster resolved from the exact citation search + canonical caption match. Verbatim holdings captured (Nora ★1055; Al-Azzawy 894–95; Vaneaton 1426–27). All three cases + verified ids + homes/roles + holdings are in `arrests-saco.jsonl`; full BIRAC bodies are staged in `payloads/`.

| Case | cite | cluster / lead-op | homes[] | body |
|---|---|---|---|---|
| United States v. Nora (spine) | 765 F.3d 1049 (9th 2014) | 2722177 / 2722177 | [[Entry to Arrest]] Key · [[Arrest in the Home]] Key | payloads/United States v. Nora.md |
| United States v. Al-Azzawy (coerced-emergence pole) | 784 F.2d 890 (9th 1986) | 465254 / 465254 | [[Entry to Arrest]] Key · [[Arrest in the Home]] Key | payloads/United States v. Al-Azzawy.md |
| United States v. Vaneaton (voluntary-exposure pole) | 49 F.3d 1423 (9th 1995) | 691388 / 9487908 | [[Entry to Arrest]] Key · [[Arrest in the Home]] Limiting | payloads/United States v. Vaneaton.md |

**Home-page-missing check:** `content/warrant-exceptions/home-entry-and-search/Entry to Arrest.md` **exists** (so does `content/seizures/arrests/Arrest in the Home.md`) — the mints home to `[[Entry to Arrest]]` as directed; **no re-home to Arrest in the Home was required.**

**MINT-OWED work order for the S2 builder lane (token holder):** for each row —
`ingest.py --add-candidates _run/s6-candidates/arrests-saco.jsonl` → resolve identity (confirm the supplied cluster id → `verified_identity`) → `mint_page.py --row "<caption>" --payload "_run/o2-execute/payloads/<caption>.md" --as-of <ISO> --write` (born `under_review`; mint-gate LINT-15/16/14 must be 0). Then the D7 section (arrests batch) names all five and the coverage ledger regen flips Nora/Al-Azzawy/Vaneaton `assemble:false → authored` (+3 authored; +3 Case-Index rows).

## Maez treatment (orchestrator step 5)
`United States v. Maez` (paged, cluster 521939, `identity_method: frontier-identity`, `lead_opinion_id: null`, treatment `unverified`). No cached cluster text is present under the pool root for a scoped `--repair-coa-state-from-cache` / `--enrich-citations` (which require `verified_identity` + cached CL text), and treatment/progeny derivation needs the REST leg. **Journaled to S9** (do not improvise) — enrich Maez's treatment + internal pincite alongside the SACO mint resolution, when the token lane runs. The existing page + `homes:[[Arrest in the Home]] role Key` remain valid as the 10th-Cir. split representative.

## Ledger regeneration + gates
- **build_coverage_ledger.py --write:** RESULT **PASS**. Partition **246 → 248 distinct captions** (brief-mention 58 → 60: +Fisher, +Allen). authored held at **148/148/148**; conflicts 0; row-errors 0; folded-alias survivors ok 8/bad 0. `corpus_mention_baseline` unchanged at 56 (the 2 new captions are cu_allow rows).
- **LINT-17 corpus:** **0** (green).
- **LINT-13 / LINT-15 / LINT-16 / LINT-25:** **0 / 0 / 0 / 0.**
- **run_all:** **7912 → 7912** (no delta; HIGH unchanged at 4825). This lane touched **no content prose** — the 2 terminals live in the ledger and the D7 section that will name them is deferred to the arrests batch — so there is no LINT-5/17 corpus movement. (run_all exits nonzero on the pre-existing baseline HIGH count; not a regression.)
- **build:** `npx quartz build` exit 0 — **721 input / 2777 emitted**, byte-identical to baseline (no content pages minted).
- **Case Index:** **unchanged** — 0 case pages minted (mints blocked), so **not** +3; regeneration deferred to the mint completion.
- **git scope:** modified `_run/s6-coverage-ledger.json`, `_overhaul2/scripts/build_coverage_ledger.py`; new `_run/o2-execute/S7-L2-SACO-{PROPOSAL,DISPOSITIONS}.{md,jsonl}`, `_run/s6-candidates/arrests-saco.jsonl`, `_run/o2-execute/payloads/*.md`. **No `content/` or `_overhaul2/lake/` mutations.**

## Notes for the orchestrator
- **The 3 mints are blocked on the credential boundary, not on any doctrinal/identity problem.** Everything is staged for a ~0-few-REST resolution by the token lane. This is the same lane split the L1 close flagged (S2 REST leg owed) and the S6 R7 architecture ("S6 never calls the CL REST API … S2's builder lane ingests").
- **Updated D7 reliance map (Berkowitz now nameable):** recognizing side 2d/6th/9th/10th — 2d *Allen* (terminal ✓), 9th *Nora* (page-owed) / *Al-Azzawy* (page-owed) / *Vaneaton* (page-owed) / *Fisher* (terminal ✓), 10th *Maez* (paged ✓; treatment→S9), 6th circuit-named-only; narrow side 5th/7th/11th — 7th ***Berkowitz* (paged ✓ — nameable/wikilinkable)**, 5th + 11th circuit-named-only (Knight/Morgan unnameable, fail-closed); 1st/3d/4th/8th unmapped (stated honestly). *Harris* remedy tail: New York v. Harris (paged, verified ✓).
