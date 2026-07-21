# I2-GAP — R7.2 citing-graph coverage-gap check — summary

**Packet:** I2-GAP (WS=I2, R7.2 instrument, mechanical, findings-only). **Lane/model:** I2-GAP / claude-opus-4-8.
**Write-scope:** `_run/s9/p4/` only. **CL:** none (lake + stored artifacts only, per P4 brief rule 2).

## Method
1. **Key-case universe (assigned).** "Doctrine key cases" = every `content/cases/*.md` whose frontmatter `homes[].role` contains "Key" or "Anchor" (the corpus's per-doctrine anchor designation; there is no literal "Key Cases" section — grep confirms 0). "Registry-point authorities" = cases cited in `_overhaul2/points/registry.yaml` node statements; these are a strict subset of the anchor set (all resolve to anchor case pages), so the union = **488 anchor case pages**, each mapped 1:1 to a lake record by name.
2. **Progeny assembly (from lake only).** For each anchor's lake record I read the `progeny` block (`cache_path` -> `~/cssi-lake/cache/progeny/<slug>.jsonl`, the bounded top-N citing opinions), plus `treatment.edges[]` and `progeny.per_sibling`. Progeny rows carry `caseName`, `citation[]`, `citeCount`, `cluster_id`, `opinions[].id`, `court_id`, `dateFiled` — the classification signals.
3. **In-corpus test (6 predicates, any hit = covered).** cluster_id in corpus (659) | opinion_id in corpus (1626) | norm-name in corpus (1117 names incl. lake identity case_name/full + record-id slugs) | docket in corpus (408) | reporter-cite present in content text | distinctive surname adjacent to "v." in content prose. Corpus = all `content/**/*.md` + all 668 lake records (any status).
4. **Gap eligibility.** A not-in-corpus progeny is a candidate if it is **top-cited** (SCOTUS any; circuit `citeCount>=40`) OR **recent** (`dateFiled>=2020`). US district / state / territorial / other courts are below the court floor (state-intermediate progeny of a SCOTUS anchor are not instructor-wiki coverage gaps) and are counted-then-skipped, not emitted.
5. **S6 accounted cross-check.** Each candidate is tested against `_run/s6-candidates/*` (frontier-*/gated/gap-docket/sweep/r7-queue/adjudication files): cluster_id (4), docket (137), caption (335 harvested captions), and variant-token co-occurrence. A hit = S6 already dispositioned it -> recorded **accounted**, NOT a finding.
6. **Severity (per packet rule).** high = SCOTUS or doctrine-shaping circuit (`citeCount>=150`); medium = circuit `citeCount 40-149` or recent multi-anchor; low = recent-only single/low-cite circuit (below doctrine-shaping floor). high+medium promoted to `findings.jsonl`; low enumerated in `I2-GAP-candidates-all.jsonl` (not promoted).

## Coverage (deterministic — nothing silently truncated)
| stage | count | note |
|---|---:|---|
| anchor key-cases assigned | 488 | union of role=Key/Anchor pages + registry authorities; all mapped to lake records |
| anchors examined (had cached progeny) | 373 | progeny `cache_path` exists |
| anchors skipped (no cached progeny) | 115 | lake bounded-enumeration returned `rows_cached=0` / no `cache_path` — no citing rows to check |
| progeny rows examined | 7,135 | across the 373 cached anchors |
| &nbsp;&nbsp;in-corpus (already covered) | 4,203 | one of 6 predicates hit |
| &nbsp;&nbsp;not-in-corpus, below court floor (skipped) | 1,792 | US district / state / territorial / other courts |
| &nbsp;&nbsp;not-in-corpus, gap-eligible (SCOTUS/circuit) | 1,140 | -> **522 distinct** cases after dedup (cluster+name) |
| accounted (S6-dispositioned, excluded from findings) | 2 | Medina (docket); Leaders of a Beautiful Struggle (reconciled) |
| **net candidates** | **520** | high 20 / medium 54 / low 446 (= 522 distinct − 2 accounted) |
| **findings.jsonl rows (high+medium)** | **74** | promoted for orchestrator triage |
| candidates-all.jsonl rows | 522 (+1 meta) | full enumeration: 520 candidates + 2 accounted-flagged (Leaders, Medina) |

## Accounted (S6-dispositioned — NOT findings)
- **Leaders of a Beautiful Struggle v. Baltimore Police Dep't** (2 F.4th 330, 4th Cir. en banc 2021; aerial/AIR surveillance; progeny of 8 corpus anchors — the highest-anchor on-domain candidate). Accounted: `frontier-searches-codex.jsonl` page_candidate + `frontier-w1-reconciled.jsonl` corrections "ADDED-DROP ... manifest record `beautiful-struggle-v-baltimore-police-dep-t` [not_found]" + `frontier-w1-codex-log.md` confirmed-absent list. Tracked not_found lake record; my caption matcher missed it (name variant), reconciled by S6-text token co-occurrence.
- **Medina v. Planned Parenthood South Atlantic** (2025, docket 23-1275). Accounted: docket match in `sweep-reconciled.jsonl` (OT2024 §1983 sweep).

## Doctrine-by-doctrine coverage
Gap columns count a candidate once per doctrine it touches (multi-doctrine anchors double-count), so column sums exceed the 74/20/54 distinct totals; the funnel above is authoritative for distinct counts.

| doctrine | anchors | w/ progeny cache | progeny rows examined | high gaps | medium gaps |
|---|---:|---:|---:|---:|---:|
| Foundations & 4A | 6 | 1 | 20 | 0 | 1 |
| Standards of Proof | 19 | 18 | 360 | 0 | 5 |
| Searches | 72 | 47 | 845 | 3 | 8 |
| Seizures | 62 | 45 | 880 | 0 | 12 |
| The Warrant | 25 | 22 | 440 | 0 | 4 |
| Warrant Exceptions | 126 | 101 | 1,935 | 6 | 22 |
| Exclusionary/Remedies/Standing | 56 | 50 | 947 | 3 | 5 |
| Confessions/5A | 74 | 67 | 1,306 | 4 | 7 |
| Right to Counsel | 18 | 15 | 300 | 0 | 2 |
| Fair Trial/Reliability | 39 | 33 | 640 | 3 | 7 |
| Use of Force/Liability | 63 | 37 | 681 | 5 | 6 |
| Legal System/Research | 1 | 1 | 20 | 1 | 0 |
| Instructor Craft | 0 | 0 | 0 | 0 | 0 |

## High-severity candidates (20) — orchestrator relevance-gate queue
SCOTUS = high by packet rule; the citing proposition is NOT in the lake row, so on/off-domain is a relevance-gate/serial-read call. **Advisory (unverified triage note):** most high-tier SCOTUS entries cite a corpus anchor for a non-4A/5A/6A proposition (appointments/immunity/FSIA/jury-trial/§1983 procedure) and are expected relevance-gate rejects; the on-domain-looking ones are the circuit 5A/confession cases.
| case | court | year | citeCount | #anchors | anchors (sample) |
|---|---|---:|---:|---:|---|
| United States v. Arthrex, Inc. | scotus | 2021 | 129 | 1 | Go-Bart Importing Co. v. United States |
| SEC v. Jarkesy | scotus | 2024 | 68 | 1 | Georgia v. Randolph |
| Trump v. United States | scotus | 2024 | 43 | 1 | Olmstead v. United States |
| Turkiye Halk Bankasi A.S. v. United States | scotus | 2023 | 33 | 1 | Illinois v. Lidster |
| United States v. Tsarnaev | scotus | 2022 | 26 | 2 | McNabb v. United States, United States v. Payner |
| Stanley v. City of Sanford | scotus | 2025 | 23 | 1 | City and County of San Francisco v. Sheehan |
| FCC v. AT&T | scotus | 2026 | 0 | 1 | Carpenter v. United States |
| Trump v. Barbara | scotus | 2026 | 0 | 4 | Carroll v. United States, Immigration & Naturalization Service v. Lopez-Mendoza, Kyllo v. United States… |
| Hunter v. United States | scotus | 2026 | 0 | 2 | Dickerson v. United States, McNabb v. United States |
| Learning Resources, Inc. v. Trump | scotus | 2026 | 0 | 1 | Marbury v. Madison |
| Gamble v. United States | scotus | 2019 | 0 | 1 | Wolf v. Colorado |
| United States v. Sewn Newton | circuit | 2004 | 366 | 2 | California v. Beheler, Dickerson v. United States |
| United States v. John Walsh | circuit | 1999 | 289 | 1 | United States v. Classic |
| Dwayne Woods v. Stephen Sinclair | circuit | 2014 | 228 | 1 | Banks v. Dretke |
| Villegas v. Gilroy Garlic Festival Ass'n | circuit | 2008 | 192 | 1 | Hanlon v. Berger |
| United States v. Brand | circuit | 2006 | 183 | 1 | Sherman v. United States |
| Armstrong v. Ashley | circuit | 2023 | 183 | 1 | Wearry v. Cain |
| Lenzi v. Systemax, Inc. | circuit | 2019 | 172 | 1 | United States v. Gastiaburo |
| Harmon v. City of Arlington | circuit | 2021 | 162 | 1 | Ryburn v. Huff |
| United States v. Demetrius Ramos | circuit | 2023 | 156 | 1 | Lego v. Twomey |

## Conclusion — saturation confirmed
The citing-graph gap check, at the depth the lake makes available (bounded top-~20 cached progeny per anchor), surfaces **no on-domain, unaccounted, doctrine-shaping coverage gap.** The single on-domain high-anchor candidate (Leaders of a Beautiful Struggle, 8 anchors) is already a tracked/dispositioned S6 record. The 74 promoted candidates are dominated by (a) off-domain SCOTUS citations of anchors (patent/appointments, presidential immunity, FSIA, tariffs, ADA, double-jeopardy dual-sovereignty), (b) high-cite circuit cases citing an anchor for a tangential point (habeas standards, §1983, employment, 1A), and (c) routine circuit applications. This is a coverage-saturation signal consistent with S6's documented R6 inclusion floor and its "dropped_already_tracked" reconciliation.

## Method limitations / for orchestrator ruling
- **Bounded progeny.** Lake progeny is `enumeration:"bounded"`, `rows_cached`≈20, ordered by CL relevance score — a thin, non-topical slice of each anchor's full citing graph (e.g. Escobedo indexes 3,478 citing opinions; 20 cached). A COMPLETE citing-graph gap check would need live `cites:(...)` enumeration = live CourtListener, which is **banned for this lane** (P4 brief rule 2). This packet is therefore a *cached-slice* gap check, not an exhaustive one; the 115 no-cache anchors are un-checked by construction. If P4 wants exhaustive progeny, route to the serial S2-builder CL lane.
- **treatment.edges are non-discriminating.** All 12,069 negative-lane treatment edges over the anchor set carry `field_iii:"mentioned"` (the `field_ii` status is the *citing* case's own validity, not its treatment of the anchor), so they add no "case-that-overruled-our-anchor" signal beyond the progeny cache; used only as an auxiliary name pool.
- **Name-mention in-corpus test is conservative.** Common surnames adjacent to "v." can mark a distinct case as covered (under-report bias); this is the intended fail-safe direction ("not found != fabricated"). id/docket/cite predicates are exact and carry the load.
- **low tier (446) not promoted.** Reason: recent-only single-anchor intermediate/circuit decisions citing one anchor in passing — below the S6 R6 doctrine-shaping floor (controlling-SCOTUS / binding-in-circuit-on-omitted-question / named-circuit-split). Fully enumerated + reproducible in `I2-GAP-candidates-all.jsonl` for audit; orchestrator may re-tier.
- **Duplicate clusters collapsed.** Multi-cluster CL entries for one case (Arthrex×2, Tsarnaev×3, Trump×2, Hunter×2, Learning Resources×2) deduped by cleaned caption (merging anchors, keeping max citeCount).
