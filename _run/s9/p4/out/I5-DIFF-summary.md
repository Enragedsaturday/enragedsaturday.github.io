# I5-DIFF summary (P4 / WS=I5 diff + tripwire-input stage)

lane `I5-DIFF` · model `claude-opus-4-8` · 2026-07-21 · governed by RULING P4-03
Write-scope: `_run/s9/p4/` only. Findings-only; the tripwire VERDICT is the orchestrator's.

## Coverage (deterministic, per brief rule 4)
- **Items assigned:** 131 raw candidate rows — codex web_search lane: `I5-digital.txt` 32 + `I5-civil.txt` 33 + `I5-foundations.txt` 44 = 109; Claude lane `I5-CLAUDE-candidates.jsonl` 22.
- **Items examined:** 131 / 131 (0 parse failures; the codex `.txt` files were clean JSONL — no prose-wrapping recovery needed).
- **Union result:** 131 → **100 distinct cases** after dedupe (normalized parties + court-circuit-bucket + year-month; spelled-out and numeric circuit ordinals reconciled; en-banc/panel kept distinct by court-bucket+date). 31 collapses were cross-lane (same case both models) or cross-unit (codex filed one case in >1 unit file).
- **Items skipped:** 0.

## Dual-model overlap (per unit)
| unit | union total | both models | codex-only | claude-only |
|---|---|---|---|---|
| digital | 34 | 4 | 28 | 2 |
| civil | 36 | 7 | 26 | 3 |
| foundations | 47 | 3 | 41 | 3 |
| **global (model-level, cross-unit)** | **100** | **14** | **78** | **8** |

Codex ran far broader (109 rows, deep circuit-court tail); Claude ran narrower/SCOTUS-weighted (22 rows). Model agreement is concentrated on the SCOTUS canon.

## Accounting result (100 distinct cases)
| classification | count |
|---|---|
| IN-CORPUS | 25 |
| ACCOUNTED-DISPOSITIONED | 14 |
| NOT-ACCOUNTED | 61 |

Accounting checks per case: (a) corpus = `content/**/*.md` case-page frontmatter cite/docket/date-corroborated + doctrine-page reporter-cite/docket mention; (b) lake = `_overhaul2/lake/cases/*.json` **own-record only** (`identity.docket` + `citations.official/all`) — progeny citation-graph artifacts (`progeny.samples[].cite`) **excluded** (they produced false positives: e.g. Villarreal's `94 F.4th 374` and Cuevas's `107 F.4th 894` live inside *other* cases' progeny lists); (c) S6 logs = `_run/s6-candidates/*` + `s6-borderline.md` + `s6-coverage-ledger.json` + `s6-fabrications.md` by reporter-cite / docket / distinctive-surname.

### ACCOUNTED-DISPOSITIONED — the 14 include 9 subsumption/alias overrides (each cited in `I5-DIFF.json.not_accounted`→moved):
- **Chatrie panel (107 F.4th 319)** + **en-banc-grant order** → procedural stages of in-corpus Chatrie SCOTUS (panel rationale narrated `content/cases/Chatrie v. United States.md:62`; lake `united-states-v-chatrie--10881683.json`; `s6-fabrications.md`). The en-banc **merits (136 F.4th 100)** is IN-CORPUS (cited "Decision below" on the SCOTUS page:51/69/82).
- **Barnes v. Felix 5th Cir (91 F.4th 393)** → below of in-corpus Barnes SCOTUS (`Barnes v. Felix.md:47`).
- **Gonzalez v. Trevino 5th Cir remand (109 F.4th 853)** → successor of in-corpus Gonzalez SCOTUS (`Gonzalez v. Trevino.md:53,65`).
- **Fields v. Federal Bureau of Prisons 4th Cir** → reversed-below of in-corpus Goldey v. Fields (`Goldey v. Fields.md:54`).
- **Linton v. Zorn 2d Cir (135 F.4th 19)** → below of Zorn v. Linton SCOTUS (page-less but accounted: `gated.jsonl` INGEST 25-297 + lake `zorn-v-linton--10813527.json` + doctrine mention 607 U.S. 568).
- **Ingram v. Wayne County 6th en banc** → retention-hearing rule abrogated by in-corpus Culley (`Culley v. Marshall.md:42,57`).
- **Villarreal v. City of Laredo (2024 + 2025 en banc)** → **alias-fold** to tracked *Villarreal v. Alaniz* (No. 25-29): `gated.jsonl:72` (`aliases:["Villarreal v. City of Laredo"]`, full litigation_history) + Retaliatory Arrest node bullet `content/use-of-force-and-liability/Retaliatory Arrest.md:44`. (My cite-grep missed this initially because codex's cite `94 F.4th 374` differs from the built `91 F.4th 693`.)
- Plus lake/S6-named non-overrides: People v. Seymour, Leaders of a Beautiful Struggle, U.S. v. Ackerman, Williams v. Reed, U.S. v. Holcomb.

## Tripwire input (fail-closed; VERDICT is orchestrator's)
**3 TWO-KEY NOT-ACCOUNTED cases** (both models, absent by name from the entire build):

| case | court / date / cite | doctrine | class-saturation | note |
|---|---|---|---|---|
| **United States v. House** | 7th Cir. 2024-11 · 120 F.4th 1313, No. 23-1950 | pole-camera "not a search" (reaffirms Tuggle) | **SATURATED** | reaffirms in-corpus Tuggle; below R6 floor by S6's own logic |
| **United States v. Lowers** | 4th Cir. 2026-03-10 · No. 24-4546 | hash-match private-search / cloud files | **SATURATED** | new 4th-Cir entrant in a catalogued split; not first-impression |
| **United States v. Brillhart** | 11th Cir. 2026-07-09 · No. 24-13226 | private-search (models disagree: hash/CSAM vs FedEx package) | **SATURATED** | **postdates S6 run (2026-07-06)**; holding-divergent → soft two-key |

**Key finding for the tripwire:** S6 fired explicit per-category **SATURATION STOPs** (`frontier-w1-claude-log.md:23` searches; :29 seizures; :34 warrant-exceptions; :47 use-of-force; :52 exclusionary) declaring "every circuit accounted-for or split flagged." All three two-key cases fall **inside splits S6 catalogued**: pole-camera mosaic (Tuggle 7th / Moore-Bush 1st / Hay 10th / May-Shaw 6th) and hash-matching private-search (Wilson 9th vs 5th/6th). None presents an omitted/first-impression question. So the saturation logs **do** account for them at the class level, even though **no** log/page/lake row names the specific opinion. All 3 carry `needs_cl:true` for existence/holding confirmation (none is in the lake; Brillhart's holding is model-divergent and unverified). The orchestrator weighs *class-level accounted (cited)* vs *case-level absent (airtight)*.

## Ambiguities / calls flagged for the orchestrator
1. **Class-saturation vs case-absence** (above) — the central tripwire judgment. I classified case-level (NOT-ACCOUNTED, airtight) and annotated class-level saturation per row rather than pre-empting the verdict.
2. **Doctrine clusters NOT explicitly saturation-catalogued** (28 medium rows, `needs_cl:true`) — the genuine "look-harder" set if the orchestrator wants them: **FISA-702 querying** (Hasbajrami — `NOT-CATALOGUED`); the **post-Egbert Bivens circuit-SURVIVAL split** (Hicks/Xi/Snowden/Logsdon/Mohamed/Robinson v. Sauls/Sheikh/Arias/Enriquez-Perdomo/Hernandez v. Causey — `PARTIAL`; use-of-force stop named only officer-created-danger + wrong-house QI); the **Torres crowd-control less-lethal projectile-seizure line** (Dundon/Packard/Marks/Sanderlin/Puente/Cheairs/Keup/Hawatmeh/Epps/Cuevas — `NOT-EXPLICIT`); **special-needs 2024-26 applications** (Kanuszewski/McMurry/O.W. v. Carr/Robinson-2d). All 1-key (codex-only) → below the two-key tripwire.
3. **Pung v. Isabella County** (SCOTUS 2026-06-23, No. 25-95) — HIGH, `needs_cl:true`, but **1-key (claude-only)**: a SCOTUS-level takings/excessive-fines merits case absent from the build, decided before the S6 run. Not two-key, so it does not itself trip P4-03, but a real missing SCOTUS merits case warrants confirmation regardless.
4. **28 low rows** (`needs_cl:false`) — 1-key, class-saturated below-floor reaffirmances in already-catalogued splits (most pole-camera/border/CSLI/third-party/malicious-prosecution/dog-sniff singletons) + unpublished (Parkerson, 2025 WL). CL confirmation immaterial to the below-floor disposition; flagged low and left for the orchestrator to escalate if desired.

## Outputs
- `_run/s9/p4/out/I5-DIFF.json` — per-unit union tables, overlap stats, accounting counts, the 61-row NOT-ACCOUNTED list with per-row two-key status / published-on-face / class-saturation / gate-relevance / needs_cl / evidence, the S6 saturation-stop catalogue, and the tripwire-input block.
- `_run/s9/p4/out/I5-DIFF-findings.jsonl` — 61 `p4.candidate.v1` rows, class `frontier-unaccounted` (severity high 4 / medium 28 / low 29; needs_cl true 33 / false 28), each pointing to its source candidate row.
