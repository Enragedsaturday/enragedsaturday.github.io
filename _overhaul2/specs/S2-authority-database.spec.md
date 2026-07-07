# SPEC S2 — Verified Authority Database (the spine)

status: APPROVED (amended 2026-07-02, audit integration — see § Amendments)
depends-on: [S1]   gates: [S3, S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-02

> The West-Key-Number-style source of truth: **one verified record per case**, built by Codex from the
> live CourtListener **REST API v4**, that every downstream spec reads from instead of touching live CL.
> Three coordinated stores: **flat per-case JSON = the committed record of truth** · a **derived SQLite**
> query layer (citation graph, coverage, verification) · case-page **frontmatter = a generated projection**
> of the lake. Read with `_overhaul2/PRACTICES.md` (§2 treatment, §3 the 10 gates, §4 research protocol,
> §6 guardrails) and `_overhaul2/CL-DATA-INVENTORY.md` (the field→call map). Conforms to S1.

## 1. Objective
Stand up the verified authority database — the single, versioned, resumable source of truth for every
case the site cites — so that identity, citations, pinpoints, treatment (good-law status), the progeny
map, and provenance are derived once, verified, and read by all downstream specs and by S9. Output: the
lake (`_overhaul2/lake/`), its out-of-repo build cache + derived SQLite, the ingest builder, the
frontmatter projector, and the drift/existence lints.

## 2. Scope
### 2.1 In scope (S2 designs + builds)
The `s2.v1` record schema; the storage architecture (JSON truth / out-of-repo cache / derived SQLite);
the Codex ingest builder (citation-disambiguated identity, cite + pinpoint harvest, progeny map,
three-lane treatment derivation, per-field provenance); the fabrication + corrupted-object machinery
*(reworked — see Amendments A1; rev. per Codex review 2026-07-02)*;
the SSOT projection contract + projector + fail-closed drift lint; the roster (457 existing + frontier
identity stubs); S2's own build-QA gates.
### 2.2 Out of scope (owned elsewhere)
Taxonomy / point-of-law node IDs (**S3** — S2 uses provisional `point` slugs, bound to S3 later);
page rendering, badges, hovers (**S4/S5** — S2 supplies the data contract, S5 renders); authoring
pages for frontier cases (**S6**) and case/term linking (**S8**); per-page prose incl. the
"Treatment & subsequent history" section (**S7**); the deep per-proposition adversarial panel + forced
primary reads (**S9** — S2 *seeds*, S9 *verifies*); the maintenance loop / citator-watch / override
staleness-propagation (**GH#2**, deferred).

## 3. Requirements (each testable)

**R1 — The record schema `s2.v1`, one JSON file per case.** Each case = `lake/cases/<slug>.json`
(`slug` = the `content/cases/` filename stem = `record_id`). Blocks: `identity` · `citations` ·
`pinpoints` · `treatment` · `progeny` · `off_cl_links` · `provenance`, plus top-level `schema_version`
and `status ∈ {draft, under_review, verified, verified_identity, not_found, fabrication_suspected,
blocked}`. A committed JSON Schema (`lake/_schema.json`) validates every record. *Check:* every record
parses, schema-validates, and round-trips through the canonical serializer; one file per case, no
monolith. `AUTO:LINT-S2-schema`. *Amended — see Amendments A6.*

**R2 — Identity: citation-disambiguated two-key, fail-closed.** Resolve per CL-DATA-INVENTORY §Identity:
`search` → `cluster_id` + `sibling_ids[]`; pick the lead via `sub_opinions[].type ∈
{lead-opinion/020lead, 015unamimous, 010combined}`; **confirm by citation AND party-name-in-text** —
a record is `verified` only when its `citations[]` carries the expected reporter/volume/page **and**
the lead/combined text names the parties. **Never trust name-rank** (live proof: `case_name="Adams v.
Williams"` ranked *Williams v. Adams*; `"Arizona v. Johnson"` ranked *Johnson v. Arizona*; `"Miranda"`
ranked a cert-denial cluster). Four named edge cases: (a) **multiple clusters** → pick by
citation+date+court, record the alternates in `provenance.warnings`; (b) **recent / no official cite**
→ fall back to `case_name`+`docket`+`court`, `identity_method="name+docket"`, `status` stays
`under_review` (never `verified`); (c) **name ≠ canonical** → `fabrication_suspected`, block +
investigate (we compare the input name to `cluster.case_name` ourselves — the auto warning is masked by
cite dedup); (d) **not found** → `not_found`, web + 2nd-source cross-check, **never delete**. *Check:*
100% of `verified` records pass the two-key; every non-verified record carries a reason code.
`CHECKLIST:D1` · `PROCESS` · maps guardrail G1/G3. *Amended — see Amendments A16 (edge case (e):
outside-corpus → `verified_off_cl` via the off-CL two-key analogue).*

**R3 — Citations & pinpoints.** `citations` carries the official cite (`type=1`), parallels, vendor-
neutral (Lexis/WL/neutral), each typed, plus a `display` string. CL `citation.type` map:
`1 Federal · 2 State · 3 State-regional · 4 Specialty · 5 Scotus-early · 6 Lexis · 7 Westlaw ·
8 Neutral` (confirmed at build against the live schema). `pinpoints[]` harvests every pincite already
present on our pages: `{id, page, quote, star_marker, quote_fidelity}`, the page = nearest preceding
`*N` star marker, the quote **string-matched** against source text via `search_document`/read
(guardrails G3 quote-fidelity + G4 pincite). New pinpoints authored downstream (S7) are written back to
the lake and re-projected. *Check:* every stored pinpoint's quote verbatim-matches the source and its
page equals the nearest preceding star marker. `AUTO` · `CHECKLIST:D1/D2`. *Amended — see
Amendments A2 (official-cite precedence), A3 (pinpoint fallback status).*

**R4 — Progeny / citing-references map.** The committed record stores the **complete OR'd query**
(`cites:(<all sibling_ids OR'd>)`), the **deduped total** (`total_citing_cases`), `per_sibling`
counts, and the raw `citation_count` (no polarity) — **not** the full list. Live-verified example:
*Terry* = **22,182** OR'd (vs 19,711 / 2,967 single-sibling — single counts under-count). The full
progeny list lives out-of-repo (`cache/progeny/<slug>.jsonl`) + in SQLite, regenerable from the query.
Material citing edges are recorded under `treatment.point_overrides[].by[]` and `treatment.edges[]`
(R5). *Check:* `total_citing_cases` = the OR'd deduped count (never a single sibling); the raw cache
regenerates from `complete_query`. `AUTO` · maps §4 forward-chaining. *Amended — see Amendments A5.*

**R5 — Treatment = 3-field vocabulary + dual dates + composite-with-overrides.** Adopt PRACTICES §2 /
S1 R2. Each record carries a **composite** `field_i_validity` (`good_law🟢 · history🔵 · caution🟡 ·
questioned🟠 · superseded🔴 · unverified⚪`) = **the headline validity of the case's principal
holding** (`composite_basis: "principal-holding"`); `as_of_content` + `as_of_treatment` (decay
independently); a machine `scope_note`; and **`point_overrides[]`** for split-treatment cases. Each
override = `{point (provisional slug), point_label, field_i_validity, as_of_treatment, by[]
(controlling case: name+cluster_id+cite+field_ii), scope_note}`; overrides key to a **citation
relationship** (verifiable now, S3-independent) with `s3_binding_status:"provisional"` — bound to S3
nodes when S3 lands. **Whenever `point_overrides` is non-empty, `varies_by_point:true` rides with the
composite everywhere** (badge, degraded header, table) so a reader on an unmatched page is always warned
"treatment varies — see Treatment." `field_ii` (≤12 tags) + `field_iii` (depth) per material edge.
Overrides exist **only on `verified` records**; `⚪ unverified` blocks all treatment, bannered.
Worked specimen: *New York v. Belton* (110559) composite `caution` + `varies`, override on the
vehicle-search point = `superseded` **by** *Arizona v. Gant* (145887, 556 U.S. 332). *Check:* no bare
composite renders without `varies_by_point` when overrides exist; every override names a controlling
case with a cluster_id + Field-II verb + as_of. `AUTO:LINT-6` · `CHECKLIST:D3`. *Amended — see
Amendments A8.*

**R6 — Three-lane treatment derivation (CL has NO treatment signal).** Derive Field-I / overrides per
case by reading progeny text + web, over three lanes, then stop at saturation: **(1) negative-keyword
scan** `cites:(<siblings>) AND (overrul* OR abrogat* OR supersed* OR "recede from" OR "no longer good
law" OR vacat* OR reversed)`; **(2) top-N by citation** (default N=25 most-cited progeny read); **(3)
recency lane** — every citing case from the **last 3 completed terms** + anything **≤3 years old**
regardless of cite count, binding jurisdictions first (fresh overrulings carry near-zero citations, so
lanes 1–2 are structurally blind to them). For each hit apply the §2 on-point test — does the negative
treatment strike **this** case's specific point in a **binding** jurisdiction? A red flag is a **clue,
not a verdict**: a sub-point strike → `point_override`; a core-holding strike → composite flip. Web-
corroborate load-bearing calls (G10). **Saturation stop** when new reads surface only already-classified
relationships. **Every negative-treatment event (override or flip) is *proposed* by the builder and only
*lands* under S9's two-reviewer rule.** *Check:* all three lanes run on every `verified` case; a
derivation trail (queries + hits reviewed) is recorded in `provenance`. `PROCESS` · `CHECKLIST:D3` ·
maps §3 KEY-2 / §4 phase 3–4. *Amended — see Amendments A4 (lane-1 bounding), A9 (lane-3 server-side),
A11 (recency window).*

**R7 — Fabrication + corrupted-object machinery.** "**Not found ≠ fabricated**": a `not_found` is
recent / outside-coverage / wrong-cite until a name+court+date **and** web cross-check say otherwise —
block + investigate, never auto-delete (guardrail G3). Name-mismatch → `fabrication_suspected`
(compare input vs canonical ourselves). A committed **`lake/_denylist.json`** hard-blocks known
corrupted CL objects — **Chatrie `10881683`** (index says SCOTUS/Chatrie, text is *Harmon v. ABC 2
News*) and **Zorn `10813527`** (text is *Strike 3 Holdings*) — each with its web-verified truth; the
builder refuses these ids and records the block. *Check:* no denylisted id is ever ingested; every
`not_found`/`fabrication_suspected` carries a cross-check trail. `AUTO` · `PROCESS`. *Amended — see
Amendments A1 (the id denylist is DELETED as an ingest blocker; Chatrie and Zorn MUST be ingested).*

**R8 — Provenance / immutable audit trail.** Per-record base (`cl_source, cl_api, built_by, build_run,
date_created, date_modified, warnings[]`) + per-field `{src, at, verifier}` on the **judgment** fields
only (`identity`, `treatment.field_i_validity`, `point_overrides`, `pinpoints`) — mechanically-copied CL
fields need no per-field stamp (guardrail G9). *Check:* every judgment field traces to source + verifier
+ timestamp. `AUTO` · maps G9.

**R9 — Storage architecture (three stores).** **(a) Committed truth** — `_overhaul2/lake/`:
`cases/<slug>.json` (~457 + stubs), `_manifest.json` (roster + per-case status + counts),
`_denylist.json`, `_schema.json`, `README.md`. **(b) Out-of-repo build cache** —
`/Volumes/AIStore2/cssi-lake/`: `cache/http/<sha1(url)>.json` (request cache), `progeny/<slug>.jsonl`,
`text/<opinion_id>.txt`, `journal/s2-ingest-<run>.jsonl` (resumable), `logs/cl-calls.log`
(gitignored, regenerable). **(c) Derived SQLite** — `<pool>/db/authority.sqlite` (R13). The distilled
records are the versioned source of truth; the DB and cache are rebuildable from them + CL. *Check:*
records survive without the volume mounted; DB + cache regenerate from `cases/` + CL; repo carries no
raw progeny/text. `PROCESS`. *Amended — see Amendments A1 (`_denylist.json` → `_advisory.json`),
A7 (lake-hash freshness stamp), A10 (`<pool>` defined).*

**R10 — Build path: Codex, direct REST v4, paced + cached + resumable.** The builder is a **Python 3
stdlib** script (`scripts/s2/ingest.py`; `urllib`+`json`+`sqlite3`, zero third-party deps) run by Codex
headless (`codex exec … -c sandbox_workspace_write.network_access=true`, wrapped in a timeout; **no
MCP**). Token from `~/.config/cssi/cl-token` (mode 600, never committed). **Pacing:** token-bucket
≤~14 req/min + jitter (~840/hr, headroom under the ~1,000/hr ceiling); sha1(url) HTTP cache (identity/
cluster ~immutable for the run, treatment scans fresh); per-case-per-step resumable journal; exponential
backoff on 429/5xx; `analyze_citations` capped ~60/min with `job_id`/`resume_citation_analysis`.
*Check:* a killed run resumes from the journal with no duplicate CL calls; cache hits skip the network;
the run stays under the hourly ceiling. `PROCESS`. *Amended — see Amendments A9 (wall-clock + budget
checkpoints + per-lane resume).*

**R11 — Lake scope / roster + the S2/S6/S8 boundary.** Build **verified records for the 457 existing
`content/cases/` pages now**, **and** run **identity + fabrication-check** on the **named-but-no-page
roster** (the S6 audit list) → **frontier stubs** (`status: verified_identity | not_found |
fabrication_suspected`) carrying identity + official cite + off-CL link **only** — **no treatment /
progeny derivation until S6 promotes a stub to a page.** **Authoring is S6's; case/term linking is
S8's.** S2 hands S6 verified cluster_ids + fabrication flags. *Check:* every existing case page has a
`verified`/`under_review` record; every roster entry has a stub with a status; no stub carries a page
or authored prose. `PROCESS`. *Amended — see Amendments A6 (stub record_id rule), A12 (roster =
`_overhaul2/S6-SEED.md`).*

**R12 — SSOT projection contract + projector + fail-closed drift lint.** The lake is upstream truth;
verified frontmatter fields are a **generated projection**. **Managed** (projector-owned):
`citation, parallel_cite, neutral_cite, court, court_level, circuit, year, date_decided, docket,
authority_weight, treatment{…3-field + point_overrides…}, courtlistener{…}, lake{record_id, status,
projected_at}`. **Preserved** (never touched): `title, type, homes, related, aliases, tags, holding,
body`. No field is in both. `authority_weight` is **derived** from `court_level` via the S1 R10 six-tier
lexicon (reader-relative "persuasive-outside-circuit" framing is S5 rendering, not a stored field).
Projector + lint share one **canonical serializer** and compare **parsed values (deep-equal)**, not raw
text. The **drift lint (CI, fail-closed) is two-directional**: `frontmatter ≠ lake` fails whether
frontmatter was hand-edited **or** the lake changed without re-projection; the error is **actionable**
(names the record path + re-project command: "edit the lake, not frontmatter"). **`draft` pages are
exempt** until promoted; every `type: case` **page** must resolve to a `verified`/`under_review` record
**before publish** (a page↔record lint) — but a record need not have a page (stubs). Structured
treatment (lake) vs the authored **prose** "Treatment & subsequent history" section (S7) is reconciled
by a **coherence gate (S9)**, not the drift lint. *Check:* managed frontmatter deep-equals the
projection site-wide; no managed field hand-editable without lint failure; every case page ↔ a record.
`AUTO:LINT-S2-drift` · `AUTO:LINT-S2-pagerecord`. *Amended — see Amendments A13 (treatment-enum
migration mapping gates the first projection), A16 (page↔record lint also accepts
`verified_off_cl`).*

**R13 — Derived SQLite query layer (rebuildable).** `authority.sqlite`, loaded from `cases/` + the
progeny cache, holds: `cases` (record_id, cluster_id, lead_opinion_id, court_level, year,
field_i_validity, as_of_*, authority_weight, status), `citations`, `siblings`, `progeny`
(total_citing, per_sibling, complete_query), `edges` (material treatment edges: cited_case,
cluster_id, field_ii, field_iii, point), **`intra_edges`** (the intra-corpus citation graph — which of
*our* cases cite which, ≤~900 nodes), `coverage` (roster reconciliation for S6/S8), `overrides`
(point_overrides + controlling-case FKs for the staleness check), `provenance`. Not a source of truth —
droppable and rebuilt anytime. *Check:* the DB rebuilds deterministically from `cases/` + cache; every
`cases` row round-trips to its JSON record. `AUTO`. *Amended — see Amendments A5 (`progeny` columns:
`total_citing` → `indexed_citing_opinions` + `count_source`; rev. per Codex review 2026-07-02),
A7 (lake-hash + cache-hash stamps + consumer freshness assert), A10 (`<pool>` defined).*

**R14 — Off-CL link whitelist + vetting.** Coverage-gap fallbacks are drawn from a whitelist —
**Justia, Google Scholar, Cornell LII, the official court/reporter site** — for reader links + parallel-
cite cross-check + independent citing-refs corroboration (G10). No open-web parametric links. *Check:*
every `off_cl_links[].source` is on the whitelist. `AUTO`. *Amended — see Amendments A16 (for
`verified_off_cl` records the whitelist links are load-bearing Key-2 identity evidence).*

**R15 — S2 build-QA gates + the S9 boundary.** S2 acceptance = **structural gates**: 100% schema-valid;
100% two-key on `verified` records; denylist enforced; dual dates + provenance present; drift lint +
page↔record lint green. **Build-review lanes** (lighter than S9): Codex builds; a **2nd Codex lane**
spot-checks ≥1-in-10 identities/cites (PRACTICES §3 governance, escalate on any error); the **Claude
lane** audits the treatment derivations. The **full 1-Claude+2-Codex per-proposition adversarial panel +
forced primary reads are S9's** deep pass reading *from* the lake. *Check:* the four structural gates
pass; the ≥1-in-10 sample logged; treatment audit recorded. `PROCESS`. *Amended — see Amendments A1:
the "denylist enforced" structural gate is REPLACED (rev. per Codex review 2026-07-02).*

## 4. Lessons enforced
Directly answers the O2 findings: **CL is not a good-law oracle** (R5/R6 derive treatment from progeny
text + web over three lanes incl. recency; the Overhaul-1 biggest catch came from an out-of-band human
pass — now first-class). **Corrupted objects** (R7 denylist: Chatrie/Zorn — *amended, see Amendments A1: the diagnosis was
refuted; the enforced lesson is now the id-namespace rule + the two-key guard*). **Publish drift** (R12:
lake = SSOT, frontmatter generated + drift-linted, two-directional). **Name-rank fabrication risk**
(R2: citation-disambiguated two-key, live-proven necessary). **Under-verified quotes/pincites** (R3:
G3/G4 string-match). Carries S1 R2 (3-field treatment) and the guardrails G1/G3/G9/G10.

## 5. Method (execution — one autonomous run, Codex builds)
1. **Scaffold** `_overhaul2/lake/` (`_schema.json`, `_denylist.json`, `_manifest.json` seeded from the
   457 roster + the S6 audit list) + `/Volumes/AIStore2/cssi-lake/` cache dirs. *Amended — see
   Amendments A1 (`_denylist.json` → `_advisory.json`), A12 (seed roster = `_overhaul2/S6-SEED.md`).*
2. **Build `scripts/s2/ingest.py`** (Python stdlib): paced/cached/resumable CL v4 client; per-case →
   R2 identity, R3 cites+pinpoints, R4 progeny, R6 three-lane treatment, R8 provenance; frontier stubs
   per R11; denylist per R7. *Amended — A1: no denylist; typed fetchers + advisory notes instead.*
3. **Run headless via Codex** over the roster; write `cases/<slug>.json` + cache + journal; log calls.
4. **Load the SQLite** (R13) from `cases/` + cache; derive `intra_edges` + `coverage`.
5. **Build the projector** (`scripts/s2/project.py`) + the shared canonical serializer; project managed
   frontmatter into `content/cases/` (idempotent); stamp `lake{}`.
6. **Add lints** to `scripts/lint/`: `LINT-S2-schema`, `LINT-S2-drift` (two-directional, value-level),
   `LINT-S2-pagerecord` — all CI fail-closed.
7. **Build-QA** (R15): structural gates + the ≥1-in-10 Codex spot-check + Claude treatment audit; flip
   passing records to `verified`; hand the frontier stubs + fabrication flags to S6.

## 6. Deliverables
`_overhaul2/lake/` (records + `_schema.json` + `_denylist.json` + `_manifest.json` + `README.md`) ·
`/Volumes/AIStore2/cssi-lake/` (cache + `db/authority.sqlite` + journal + logs) ·
`scripts/s2/ingest.py` + `scripts/s2/project.py` + the shared serializer ·
`scripts/lint/` extensions (`LINT-S2-schema` / `-drift` / `-pagerecord`) ·
projected managed frontmatter across `content/cases/`.
*Amended — see Amendments A1 (`_denylist.json` → `_advisory.json`), A2 (adds
`_reporter-precedence.json`; rev. per Codex review 2026-07-02), and A13 (adds
`_treatment-migration.json`).*

## 7. Acceptance criteria
- [ ] `s2.v1` schema authored; every record schema-valid and canonical-serializer round-trips (R1).
- [ ] 100% of `verified` records pass the citation-disambiguated two-key; every non-verified carries a
      reason code; four identity edge cases handled (R2).
- [ ] Typed cites + star-paginated pinpoints; every stored quote verbatim-matches source (R3).
      *(amended — A2, A3)*
- [ ] Progeny stored as count+query+edges (OR'd deduped total); full list regenerates from cache (R4).
      *(amended — A5)*
- [ ] 3-field treatment + dual dates + composite(principal-holding)+`varies_by_point` marker + point-
      overrides; no bare composite without `varies` when overrides exist (R5). *(amended — A8)*
- [ ] Three-lane derivation (negative-keyword + top-25-cited + recency) run on every verified case;
      derivation trail recorded; negatives staged for S9 two-reviewer (R6). *(amended — A4, A9, A11)*
- [ ] "Not found ≠ fabricated" enforced; Chatrie/Zorn denylist blocks ingest (R7). *(amended — A1:
      REVERSED — the denylist is deleted; the build FAILS unless Chatrie + Zorn are ingested)*
- [ ] Per-record + per-judgment-field provenance present (R8).
- [ ] Three stores stood up; records survive without the volume; DB + cache rebuild from `cases/`
      (R9/R13). *(amended — A7, A10)*
- [ ] Builder paced + cached + resumable under the hourly ceiling; a killed run resumes cleanly (R10).
      *(amended — A9)*
- [ ] 457 verified + frontier identity stubs; no stub authored; S6/S8 boundary respected (R11).
      *(amended — A6, A12)*
- [ ] Projection contract enforced; two-directional drift lint + page↔record lint green; `draft` exempt
      (R12). *(amended — A13)*
- [ ] Off-CL links whitelisted only (R14).
- [ ] S2 structural gates pass; ≥1-in-10 spot-check + treatment audit logged; S9 boundary held (R15).
      *(amended — A1: the "denylist enforced" gate is replaced in the roster; rev. per Codex review
      2026-07-02)*

## 8. Verification plan
S2's own build-QA (R15) gates the lake. **S9** then reads *from* the lake and runs the full per-
proposition adversarial panel (1 Claude + 2 Codex, ≥2-of-3 refute), forced primary reads on recent/high-
profile cases, the 10-gate protocol, and the ledger — adjudicating every negative-treatment event S2
staged. The drift, page↔record, and schema lints run in CI fail-closed on every change.

## 9. Open items / escalations
- **S3 binding.** `point_overrides[].point` slugs are **provisional**; a binding map (`point → S3 node`)
  + a fail-closed lint activate **after S3 exists**. 1:N / N:1 taxonomy splits handled by the map.
- **Treatment-lane parameters** (recency window = last 3 terms / ≤3 yrs; top-N = 25) are **execution-
  tunable defaults** — revisit against real hit-rates during the run. *(amended — A4 adds the lane-1
  scan cap; A11 replaces the window with one uniform rolling 3-year `filed_after`)*
- **Override staleness propagation** (a controlling case's own `field_i` later changes) — the SQLite
  `overrides` consistency check flags it; automated re-derivation is a **maintenance-loop** task (GH#2).
- **Lake permanent home.** Built at `_overhaul2/lake/` for the run; graduation to a permanent
  `data/authority/` home is a post-publish (maintenance-loop) task, referenced via a single path constant.
- **CL `citation.type` enum** confirmed against the live schema at build (observed 1/2/6 on *Terry*).
  *(amended — A2: `type=1` is a class, not a unique selector — Terry carries three type-1 cites)*
- Frontier-stub edge cases (alias/variant collisions, cite-format placeholders) reconciled with the S6
  audit list at build. *(amended — A6 defines the stub record_id; A12: the roster artifact is
  `_overhaul2/S6-SEED.md`)*

## Appendix — Decision log
**User-facing interview (2026-07-01):**
- **A · Store** = JSON records are the committed source of truth; a **derived SQLite** query layer holds
  the citation graph / coverage / verification; raw cache out-of-repo. (Rejected: Postgres-first — loses
  git-diffable truth + adds ops/network for the builder; everything-out-of-repo — truth unversioned.)
- **B · Scope** = 457 now + identity/fabrication **pre-seed** of the no-page roster; **authoring → S6,
  linking → S8**.
- **C · Treatment** = exhaustive **three lanes** (negative-keyword + top-by-citation + **recency**) —
  recency added by the user: fresh overrulings carry ~zero citations, so cite-ranked lanes miss them.
- **D · SSOT** = lake is the source of truth; frontmatter is a **generated projection**.

**Self-interview (SD1–SD14; SD4/SD8 worked to edge cases):**
- **SD1** one JSON file per case (not monolith/JSONL) — per-case diffs + resumable writes.
- **SD2** lake at `_overhaul2/lake/` for the run; permanent-home graduation deferred (see Open items).
- **SD3** committed record stores progeny count+query+edges; full list → cache+SQLite.
- **SD4** treatment = **composite (principal-holding) + `varies_by_point` marker + `point_overrides`**;
  overrides keyed to the citation relationship (S3-independent), bound to S3 later. **Composite rule =
  principal-holding + forced varies marker** (chosen over most-severe / mixed-sentinel — a safe headline
  that is never the last word; the marker rides everywhere so an unmatched page always warns). Negative
  events proposed by the builder, adjudicated by S9's two-reviewer rule. Overrides only on `verified`.
  *(see Amendments A8 — `composite_basis_ref` makes the principal-holding referent auditable)*
- **SD5** three-lane defaults (regex set; top-25; last-3-terms/≤3-yrs recency) — tunable. *(see
  Amendments A4, A9, A11 — lane-1 bounding, lane-3 server-side, uniform rolling recency window)*
- **SD6** identity fail-closed, four edge cases (multiple clusters / no-cite / name-mismatch / not-found).
- **SD7** S2 harvests+verifies existing pinpoints; S7 authors new (written back); S9 re-verifies.
- **SD8** projection = fixed managed/preserved split (mutually exclusive) + shared canonical serializer +
  **value-level, two-directional, actionable drift lint**; structured treatment (lake) vs prose (authored)
  reconciled by an S9 **coherence gate**, not the drift lint; page↔record publish gate, `draft` exempt.
- **SD9** `authority_weight` derived from `court_level` via S1 R10; reader-relative framing is S5.
- **SD10** frontier stubs = identity + fabrication + off-CL link only; no treatment/progeny pre-promotion.
- **SD11** provenance per-record + per-field on judgment fields only.
- **SD12** builder = Python 3 stdlib (`urllib`/`json`/`sqlite3`), zero deps, sandbox-friendly.
- **SD13** pacing = token-bucket ≤~14/min + jitter, sha1(url) cache, per-step journal, backoff.
- **SD14** S2 QA = structural gates + light build-review; deep per-proposition verification is S9's.

---

## Amendments — 2026-07-02 (audit integration)

*Source: the 2026-07-02 eight-agent audit. Register: `_overhaul2/AUDIT-2026-07-02.md` (rows routed
`amend:S2`). Evidence: the S2-feasibility report, live-verified against CourtListener v4 —
`_overhaul2/AUDIT-2026-07-02-full-brief.html`, appendix B. Each amendment states its register ref,
quotes the superseded text, gives the new normative text, and records the reasoning. Where a task
brief and the register disagreed on an ID, the **register ID** governs. Body pointers
(`*Amended — see Amendments A<n>.*`) mark every touched requirement.*

### A1 — R7 reworked: the id denylist is DELETED as an ingest blocker; *Chatrie* and *Zorn* MUST be ingested
**Register:** S2F-01a (CRITICAL) + S2F-01b (CRITICAL). Root-cause shared with LAW-02a (content side is
Phase 4's). **This is a decision reversal** — full adversarial treatment below.

**Supersedes (R7):**
> "A committed **`lake/_denylist.json`** hard-blocks known corrupted CL objects — **Chatrie
> `10881683`** (index says SCOTUS/Chatrie, text is *Harmon v. ABC 2 News*) and **Zorn `10813527`**
> (text is *Strike 3 Holdings*) — each with its web-verified truth; the builder refuses these ids and
> records the block. *Check:* no denylisted id is ever ingested"

and its echoes: §4 ("Corrupted objects (R7 denylist: Chatrie/Zorn)"), R9(a) + Method 1–2 + §6
(`_denylist.json`), the §7 criterion "Chatrie/Zorn denylist blocks ingest (R7)", and **R15's
structural gate "denylist enforced"** (rev. per Codex review 2026-07-02).

**New normative text:**
1. **The id denylist is deleted as an ingest blocker.** No committed list of CL ids may block
   ingestion. `lake/_denylist.json` is removed from the committed store and replaced by
   **`lake/_advisory.json`** — non-blocking advisory notes, every entry **namespaced by object type**
   (`{"object_type": "cluster"|"opinion", "id": …, "note": …}`).
2. **Structural rule (load-bearing): NEVER fetch `/opinions/<cluster_id>`.** Opinion ids enter the
   pipeline **only** from `cluster.sub_opinions[]` (or the search response's `sibling_ids[]` /
   `opinions[]` arrays). The CL client exposes **typed fetchers** (`get_cluster(cluster_id)` /
   `get_opinion(opinion_id)`); there is no code path by which a cluster id reaches the opinions
   endpoint, and every `get_opinion` argument is traceable in the journal to an extraction from
   `cluster.sub_opinions[]`, search `sibling_ids[]`, **or search `opinions[].id`** — each trace
   labeled with its source array (rev. per Codex review 2026-07-02).
3. **The systemic guard for this failure class is R2's two-key identity check** (citation AND
   party-name-in-text): an object fetched under a mistaken id fails both keys and lands
   `under_review`/`fabrication_suspected` with a cross-check trail — never silently ingested, never
   silently excluded.
4. **Advisory note (REWORKED, non-blocking)** committed in `lake/_advisory.json` so the legend cannot
   resurface:
   - `cluster 10881683` = ***Chatrie v. United States***, SCOTUS, decided **2026-06-29**, lead opinion
     `11349205` — **MUST be ingested** (core CSSI subject matter; live case page exists).
   - `cluster 10813527` = ***Zorn v. Linton***, SCOTUS, decided **2026-03-23**, sub-opinion `11280281`
     — **MUST be ingested** (live case page exists).
   - `opinion 10881683` (→ cluster 10415095, *Harmon v. ABC 2 News*) and `opinion 10813527`
     (→ cluster 10346939, *Strike 3 Holdings*) are **valid, unrelated opinion objects — not
     corruption**. O1 fetched **cluster ids against `/opinions/`** and read the id-collision as
     corrupted data; documented here as the root cause.
5. **Acceptance + gate replacement (§7 and R15):** the §7 R7 criterion **and R15's structural gate
   "denylist enforced"** both become — *no blocking id-list exists; the typed-fetcher rule holds
   (journal audit: zero `/opinions/` fetches with a non-extraction-derived id);
   `verified`/`under_review` records for Chatrie (10881683) and Zorn (10813527) exist in the lake —
   the build FAILS if either is missing; `_advisory.json` present with the namespaced root-cause
   notes.* R15's gate roster reads accordingly (schema-valid · two-key · this replacement gate ·
   dual dates + provenance · drift + page↔record lints). The "not found ≠ fabricated" half of R7 and
   its fabrication machinery are **unchanged**. (rev. per Codex review 2026-07-02)

**Rationale (Decision-Log grade).**
- *Why the original decision was made:* during O1, fetching ids 10881683/10813527 returned
  *Harmon*/*Strike 3* texts under what the index called Chatrie/Zorn. From inside that session,
  "index says X, text says Y" reads exactly like upstream data corruption, and a hard denylist is the
  standard defense against poisoned objects. The spec codified it in good faith, with "web-verified
  truths" attached.
- *What the audit proved (live, 2026-07-02):* both ids are valid **CLUSTER** ids of the genuine 2026
  SCOTUS decisions (Chatrie sub-opinion 11349205 text verified: "Held: Police officers conducted a
  Fourth Amendment search…"). The Harmon/Strike 3 texts belong to valid **OPINION** objects that
  merely share the same numerals in a different id namespace. Nothing was ever corrupt; O1 crossed
  namespaces by fetching cluster ids against the opinions endpoint.
- *Cost had the rule stood:* the builder would have refused both clusters — silently excluding the
  newest landmark geofence SCOTUS decision from the authority database of a search-and-seizure wiki.
  Both cases have live pages, so R12's page↔record lint would then have blocked publish or forced
  status hacks. A silent hole in the worst possible place.
- *Alternatives weighed:* **(i)** keep the denylist, re-point it at the opinion ids — rejected:
  opinions 10881683/10813527 are valid objects; blocking them mislabels good data and keeps a
  symptom-patch alive over an unfixed namespace bug, inviting the next misdiagnosed id. **(ii)** keep
  an empty denylist mechanism "just in case" — rejected: a standing blocklist with zero verified
  members is an attractive nuisance (this exact failure re-arming itself); genuinely bad objects are
  already quarantined per-record by R2's fail-closed statuses, which carry evidence instead of a bare
  block. **(iii)** fix only the two entries' prose — rejected: without the structural never-fetch
  rule the O1 failure class stays reachable.
- *Why the replacement is strictly safer:* the typed-fetcher rule prevents the entire class rather
  than two instances; the two-key check catches any residue; the advisory note preserves the
  institutional memory without blocking power.

### A2 — R3: official-cite selection needs reporter precedence (`type=1` is a class, not a selector)
**Register:** S2F-02 (HIGH).

**Supersedes (R3):**
> "`citations` carries the official cite (`type=1`), parallels, vendor-neutral (Lexis/WL/neutral),
> each typed, plus a `display` string."

**New normative text:** `type=1` identifies the **class** of federal official cites, not a unique
member — live-verified: *Terry* carries **three** type-1 citations (392 U.S. 1 · 88 S. Ct. 1868 ·
20 L. Ed. 2d 889). The official cite is selected from the official-class set by **reporter
precedence**: **SCOTUS:** `U.S.` > `S. Ct.` > `L. Ed.`/`L. Ed. 2d`. **Courts of appeals:** the
Federal Reporter chain (`F.`/`F.2d`/`F.3d`/`F.4th`) over any parallel. **District courts:** the
`F. Supp.` chain (`F. Supp.`/`F. Supp. 2d`/`F. Supp. 3d`). **State courts:** the official state
reporter (official > regional > other). The precedence is **committed machine-readable**:
**`lake/_reporter-precedence.json`** (reporter string → rank, per court class), editorially seeded
from Bluebook T1 — the stdlib builder consults **only this table**; "Bluebook rank" is the table's
editorial source, never a runtime judgment (rev. per Codex review 2026-07-02). Non-selected
official-class cites are stored as parallels (unchanged). **Unresolvable cases** (same-rank
duplicates, or a reporter **unlisted in the table**): the builder selects nothing, logs the case to
the R10 journal + `provenance.warnings`, and the record stays `under_review` until the R15
spot-check lane resolves it. *Replacement check (cite half):*
every `verified` record's official cite is the highest-precedence member of its official-class set;
every tie is journaled. **Rationale:** without precedence the builder can stamp "88 S. Ct. 1868" as
*Terry*'s official cite nondeterministically; a fail-closed tie rule beats a silent arbitrary pick.

### A3 — R3: pinpoint fallback status for opinions without star pagination
**Register:** COH-10 (MED).

**Supersedes (R3, check):**
> "*Check:* every stored pinpoint's quote verbatim-matches the source and its page equals the nearest
> preceding star marker."

**New normative text:** every pinpoint carries **`pinpoint_status ∈ {"star-verified", "slip-only"}`**.
`star-verified`: source text has star pagination; `page` = nearest preceding `*N`; quote
string-matched (the original rule). `slip-only`: the source (slip opinion / recent case) has **no
star pagination**; store the **slip page as cited** + a **paragraph/quote anchor** (the verbatim
`quote` + its `position` from `search_document`); the quote is still string-matched — page equality
is **not** asserted. `slip-only` pins are upgrade candidates when reporter pagination lands (S7
write-back or the GH#2 maintenance loop); the projector carries the status through so S5/S7 can
render or convert accordingly. *Replacement check:* every pinpoint's quote verbatim-matches;
`star-verified` ⇒ page = nearest preceding star marker; `slip-only` ⇒ slip page + anchor recorded;
no pinpoint lacks a status. **Rationale:** the original check was structurally unsatisfiable for
exactly the cases the recency lane exists to catch (e.g. current-term *Chatrie*); a typed fallback
keeps the gate honest instead of forcing fake pages or blanket exemptions.

### A4 — R6 lane 1 bounded: filters + caps so saturation can actually trigger
**Register:** S2F-03 (HIGH).

**Supersedes (R6, lane 1):**
> "**(1) negative-keyword scan** `cites:(<siblings>) AND (overrul* OR abrogat* OR supersed* OR
> "recede from" OR "no longer good law" OR vacat* OR reversed)`"

**New normative text:** lane 1 is **bounded**: the query adds **(a)** a court filter =
**`binding_jurisdiction_filter(record)`**, computed from the record's own `identity` court fields
(`court_level` + circuit/state), emitted as a `court_id:(…)` clause ANDed into the lane query —
**SCOTUS record:** no court filter (every court is bound); **court-of-appeals record:**
`AND court_id:(scotus OR ca<N>)` (own circuit + SCOTUS); **district record:**
`AND court_id:(scotus OR ca<N>)` for the encompassing circuit (a district holding is displaced by
its own circuit or SCOTUS); **state record:** `AND court_id:(scotus OR <own-state CL court-id
family>)` (own state's courts + SCOTUS). Non-binding negative treatment is corroboration only, not
default scan scope. *(rev. per Codex review 2026-07-02 — replaces the erroneous "S1 R10 court map"
reference: R10 is the label lexicon, and "rendering court" was not an S2 field; the filter is now
defined on S2's own record fields with concrete CL query syntax.)* **(b)**
`stat_Published` only; **(c)** `order_by=dateFiled desc`; **(d)** a **per-case scan cap, default 200
results scanned per lane** (execution-tunable like the other lane parameters). Lane 1 counts toward
the **same saturation rule** as lane 2 (stop when new reads only re-surface already-classified
relationships). **Hitting the cap is logged** in the R10 journal and the record's derivation trail —
never silent truncation — and every capped lane is reported to the R15 treatment audit. *Check:*
no lane-1 query runs unfiltered; every cap hit appears in journal + provenance. **Rationale:**
live-verified, the unbounded OR'd query on *Terry* returns **6,917** hits — it dwarfs lane 2's N=25
and saturation never triggers; on mega-cases "scan" was unbounded work with no stop condition.

### A5 — R4: citing-count provenance is three-valued; relabel `total_citing_cases`
**Register:** S2F-06 (MED). *(The tasking brief listed this content under "S2F-04"; the register ID
S2F-06 governs.)*

**Supersedes (R4):**
> "the **deduped total** (`total_citing_cases`)" … "*Check:* `total_citing_cases` = the OR'd deduped
> count (never a single sibling)"

**New normative text:** the field is renamed **`indexed_citing_opinions`**, labeled **"indexed citing
opinions (search)"**, and every stored citing count carries a **`count_source ∈ {"search",
"cluster.citation_count", "opinions-cited"}`**. The record stores each count it fetched with its
source — live-verified on *Terry*, the three are **not interchangeable**: `cluster.citation_count`
**37,950** ≠ lead-opinion `opinions-cited` edge rows **37,624** ≠ OR'd search **22,182**. The OR'd
search count remains the operative progeny-scan denominator (it is the set the lanes can actually
enumerate) but is never presented as a total-citing-cases figure. Note — **contra the inventory's
old caveat** (corrected there this date): the `opinions-cited` edge table is the **more complete**
citing-edge source for the lead (37,624 ≈ 37,950; search is ~15k lower because it counts only
indexed opinions and splits by sibling). **SQLite propagation (R13):** the rename carries into the
DB schema — the `progeny` table's `total_citing` column becomes **`indexed_citing_opinions`** and the
table gains a **`count_source`** column; every citing count stored in the DB carries its source, same
enum as the record field (rev. per Codex review 2026-07-02). *Replacement check:* no record — and no
DB row — carries an unlabeled citing count; `indexed_citing_opinions` = the OR'd deduped search
count. **Rationale:** an honest label
prevents downstream prose ("cited by N cases") from inheriting a number that is an artifact of which
endpoint was asked.

### A6 — R1/R11: frontier-stub `record_id` generation (stubs have no page)
**Register:** S2F-05 (MED).

**Supersedes (R1):**
> "(`slug` = the `content/cases/` filename stem = `record_id`)"

**New normative text:** that identity holds **only for page-backed records**. **Frontier stubs**
(R11 roster entries with no page): `record_id = slugify(cluster.case_name) + "--" + <cluster_id>`
(e.g. `nieves-v-bartlett--4384503`), file `lake/cases/<record_id>.json`, top-level **`stub: true`**.
`not_found` stubs (no cluster id): `slugify(input caption) + "--u" + sha1(normalized roster key)[:8]`,
where the **normalized roster key** concatenates, canonically, every identifying field the roster row
carries: caption + court + year/date + docket/citation + the S6-SEED source-row id — a caption-only
hash would collide on same-caption/different-court entries (rev. per Codex review 2026-07-02).
**Collision safety:** the `--` suffix namespace is reserved — `LINT-S2-schema` fails if any
`content/cases/` filename stem contains `--` (verified 2026-07-02: 0 of 457 do), so no stub can
collide with a current or future S6 page slug; additionally `LINT-S2-schema` asserts **global
record_id uniqueness** across `lake/cases/` + `_manifest.json` and fails on any two roster keys
resolving to one record_id (rev. per Codex review 2026-07-02). **Promotion:** when S6 authors the
page, S6 renames the record to the page filename stem, drops `stub: true`, and records
`old record_id → new` in `_manifest.json` in the same commit; the page↔record lint treats the rename
atomically. *Check:* every stub record_id parses to caption+id (or caption+`--u`hash) form; no page
stem contains `--`; record_ids globally unique; every promoted stub has a manifest rename entry. **Rationale:** without a rule, stub filenames would be invented ad hoc at
build time — the one moment nobody is looking at naming — and S6 would inherit collisions.

### A7 — R9/R13: the third consistency direction — lake content-hash stamp in SQLite
**Register:** S2F-04 (MED). *(The tasking brief listed this content under "S2F-06"; the register ID
S2F-04 governs.)*

**Adds to R13 (no text deleted):** at DB build, the loader computes **`lake_hash`** = sha256 over the
sorted `(path, sha256(file))` pairs of `lake/cases/*.json` + `_manifest.json`, **and `cache_hash`** =
the same construction over **every out-of-repo cache input the DB loader actually reads** (the
`<pool>/progeny/<slug>.jsonl` files; extendable to any future loader input) — R13's SQLite loads from
the progeny cache too, so a lake-only hash would let a stale cache pass freshness (rev. per Codex
review 2026-07-02). Both are written with `built_at` to a **`meta`** table in `authority.sqlite`.
**Every consumer** (S6 coverage reads, S8 linking reads, S9 verification reads, and the projector if
it reads the DB) MUST recompute **both hashes** and **assert equality before reading**; either
mismatch = **fail-closed** (stop and rebuild the DB — never read stale). *Check:* `meta.lake_hash` +
`meta.cache_hash` present; a deliberately staled DB — via lake edit **or** cache edit — makes a
consumer read fail in test. **Rationale:** lake↔frontmatter drift is linted two-directionally, but
the DB is droppable/rebuildable while S6/S8 read `coverage`/`intra_edges` from it — a stale DB (or a
DB built from a stale cache) silently serves an old roster. Two cheap columns close the triangle.

### A8 — R5: auditable composite basis + stable point slugs + the S9 prose recheck
**Register:** S2F-07a (MED) + S2F-07b (MED).

**Supersedes (R5, in part):**
> "**the headline validity of the case's principal holding** (`composite_basis:
> "principal-holding"`)"

**New normative text:** the record additionally stores **`composite_basis_ref`** — the **point slug**
of the principal holding where one exists in `point_overrides[]`/the point vocabulary, else a
**one-sentence principal-holding statement** — so the composite judgment is auditable (*which*
holding was rated). **Point slugs are stable strings once minted** — never re-spelled; taxonomy
splits/renames are absorbed by the binding map, not by rewriting slugs. **Binding source (updates
§9/SD4) — a PRECONDITION, not an assumption** (rev. per Codex review 2026-07-02, mirroring A12's
S6-SEED framing): S3 is SIGNED, and its R4 names the point-of-law registry
**`_overhaul2/points/registry.yaml`** + the `point → node` binding map as committed S3 deliverables —
**neither exists on the branch yet**. S2 therefore emits **provisional slugs only**; the flip of
`s3_binding_status:"provisional"` → bound REQUIRES both artifacts to exist on the branch, and the S9
prose-reference lint (next sentence) **activates only after that binding**. **S7 prose authored
against provisional slugs gets an explicit S9 recheck after binding:** the S9 coherence gate (R12)
extends to prose point references — a 1:N slug split flags every page whose prose cites the split
slug.
*Check:* every composite carries `composite_basis_ref`; every override slug resolves through the S3
binding map by S9 time. **Rationale:** "principal holding" was a judgment with no recorded referent —
unauditable and unfalsifiable; and without declared slug stability, the binding map guards the data
while the prose silently rots.

### A9 — R10/R6: wall-clock stated; lane 3 server-side; per-lane resumability
**Register:** S2F-08a (MED) + S2F-08b (MED) + S2F-08c (MED). Runbook twin: COH-19 (fixed-now).

**Adds to R10 / amends R6 lane 3 (no text deleted):**
**(a) Schedule (normative):** the full-roster build ≈ **15–25k CL calls**; at ≤~14 req/min that is
**≈20–30+ hours of API time minimum — a multi-day run** once treatment reads are included. The run
is planned as **resumable sessions**; each session start/end writes a **budget checkpoint** to the
journal (calls this session / cumulative / remaining estimate vs. the hourly ceiling). The RUNBOOK
§4-S2 entry carries the same wall-clock statement (COH-19).
**(b) Lane 3 is server-side, mandatory:** `cites:(<all sibling_ids OR'd>) AND filed_after:<window
start>` — live-verified working (on *Terry*: 89 hits including two 2026 SCOTUS decisions). No
client-side date-filtering of full progeny pulls.
**(c) Per-lane completion in the journal:** the R10 journal records, per case, per lane,
`pending | partial(cursor) | complete`. Treatment scans are **deliberately uncached**, so on resume
the builder consults lane status and continues from the recorded cursor — completed lanes are never
re-run, and treatment-query quota is never re-burned. *Check:* a killed-run resume replays zero
completed lanes; the journal shows per-lane status + budget checkpoints. **Rationale:** "one
autonomous run" hid a multi-day wall-clock; without lane-level resume, every restart re-pays the
most expensive, uncacheable queries.

### A10 — R9/R13: the `<pool>` path token defined
**Register:** COH-29 (LOW).

**Supersedes (R9(c)):**
> "**(c) Derived SQLite** — `<pool>/db/authority.sqlite` (R13)."

**New normative text:** **`<pool>`** = the out-of-repo connected-storage root for the S2 build,
**`/Volumes/AIStore2/cssi-lake`** — the same root R9(b) names for the cache. Defined **once, here**;
every other occurrence (`<pool>/db/authority.sqlite` ≡ `/Volumes/AIStore2/cssi-lake/db/
authority.sqlite`, §6 Deliverables) references this definition. The builder holds it as a **single
path constant** (`CSSI_LAKE_ROOT`, env-overridable) — which is also the one knob for the §9
permanent-home graduation. **Rationale:** the token was inferable only by cross-reading §6; an
undefined path token in a storage requirement is exactly how a build lands on the wrong volume.

### A11 — R6 lane 3: one uniform rolling recency window (courts don't all have "terms")
**Register:** COH-30 (LOW).

**Supersedes (R6, lane 3):**
> "**(3) recency lane** — every citing case from the **last 3 completed terms** + anything **≤3 years
> old** regardless of cite count, binding jurisdictions first"

**New normative text:** the recency lane = every citing case with
**`filed_after = build_date − 3 years`** (a rolling date window), regardless of citation count,
binding jurisdictions first — **uniform across all courts**. "Last 3 completed terms" is retired as
a SCOTUS-specific gloss: a 3-year rolling window covers ≥3 SCOTUS terms by construction and is
directly expressible as the server-side `filed_after` filter (A9(b)). Remains an execution-tunable
default per §9. *Check:* every lane-3 query carries the computed `filed_after`, same formula for
every court. **Rationale:** circuit and state courts have no "terms" — the old wording made the lane
ambiguous for exactly the progeny (fresh circuit overrulings) it exists to catch.

### A12 — Method 1/R11: the manifest/roster seed is `_overhaul2/S6-SEED.md`
**Register:** COH-02b (CRITICAL — the S2 pointer half; the artifact half is COH-02a, fixed-now
Phase 3a).

**Supersedes (Method step 1, R11, §9):**
> "`_manifest.json` seeded from the 457 roster + the S6 audit list" · "the **named-but-no-page
> roster** (the S6 audit list)" · "reconciled with the S6 audit list at build"

**New normative text:** the committed no-page roster is **`_overhaul2/S6-SEED.md`** (regenerated and
committed in audit-integration Phase 3a; input sizing per NUM-05, ~80–84 entries). Every "S6 audit
list" reference in this spec now means that file; the previously referenced "§S6 seed /
`audit_cases.py`" artifacts **do not exist** and are no longer cited. Method step 1 seeds
`_manifest.json` from the 457 `content/cases/` stems + `_overhaul2/S6-SEED.md`; R11's identity/
fabrication pre-seed runs over its entries; frontier-stub edge cases reconcile against it at build.
*(At amendment time S6-SEED.md is being generated in a parallel Phase-3a lane; it is the committed
handoff artifact regardless — S2 MUST NOT start Method step 1 until it exists on the branch.)*
**Rationale:** S2's manifest seeded from a dangling reference meant the build's roster depended on a
past session's memory — the exact failure class the kit's "small on-disk handoffs" rule exists for.

### A13 — R12: legacy treatment-enum migration mapping gates the first projection
**Register:** COH-11 (MED) — the **S2 half** (the vocabulary half is `amend:S1`, owned by the S1
amendment writer; consumed by S5).

**Adds to R12 (no text deleted):** before the projector **first** overwrites managed `treatment{}`
frontmatter, a committed **legacy→Field-I migration mapping** must exist:
**`lake/_treatment-migration.json`** — the **mechanical encoding of S1 Amendment A4's mapping
table**, which is *the only sanctioned old→new translation* (rev. per Codex review 2026-07-02).
Encoded rows (S1 A4, counted 2026-07-02): 439 `good` → `good_law` 🟢 · 11 `limited` → `caution` 🟡 +
**mandatory ≥1 `point_overrides[]`** on the limited point (Field-II `limited`, or `superseded` where
replaced outright) + `varies_by_point: true` · 5 `overruled` → `superseded/not_current` 🔴 +
Field-II `overruled` edge to the overruling case · 2 `abrogated` → `superseded/not_current` 🔴 +
Field-II `abrogated` edge · `criticized` (0) → `caution` 🟡. No migrated case maps to `unverified` ⚪.
**`REVIEW` is reserved ONLY for** (a) a legacy value that does not appear in the S1 A4 table
(unexpected input), or (b) an entry whose **required edge metadata cannot be determined** (e.g. a
`limited` case with no identifiable override target) — it is **not a general escape hatch**; a
`REVIEW`-marked page is staged for the S9 two-reviewer rule and the projector will not overwrite it
until adjudicated. The pre-projection legacy value is preserved in the record's
`provenance.warnings` (migration log) — nothing is silently destroyed. The mapping's **semantics**
are S1 A4's; S2 owns the **fail-closed mechanical application**: the projector refuses to run while
any observed legacy value lacks a mapping entry. Per S1 A4's consumption rule, the mapping **seeds**
Field-I; R6's three-lane derivation then confirms or adjusts, and the mapping alone never yields
`verified`. S5 consumes the same table for rendering migration. *Check:* projector run preceded by a
complete mapping that byte-for-byte encodes S1 A4's rows; migration log covers every overwritten
page; every `REVIEW` entry cites reason (a) or (b). **Rationale:** the projector is the one tool in
the kit that mass-overwrites existing human-reviewed treatment calls; doing that without the
recorded, sanctioned old→new map is an irreversible information discard.

---

*Inventory-side amendments (S2F-09a–e + the S2F-06 caveat correction) are applied directly in
`_overhaul2/CL-DATA-INVENTORY.md`, marked "(audit 2026-07-02, live-verified)".*

---

## Amendments — 2026-07-04 (S8-interview intake)

### A14 — R3: optional pinpoint `fragment` field (external text-fragment links)
**Source:** the S8 interview/spec (`S8-linking-glossary.spec.md` R5; precedent: S6 § A1 authored
at the S7 interview). **Adds to R3 (no text superseded):** each pinpoint MAY carry
**`fragment`** — the validated `#:~:text=` string S8 generates from the pin's G3-verified
`quote` — plus **`fragment_validated_at`**. Written back through R3's existing "new pinpoints
authored downstream are written back" path; generation + validation semantics are wholly S8 R5's
(fragments derive only from G3-passed quotes, validated to exactly one whitespace-insensitive
match against the R9(b) cached opinion text — no live CL calls). `lake/_schema.json` marks both
fields optional; records without them remain schema-valid. *Rationale:* the fragment is derived
pinpoint data with exactly one natural home — the pinpoint record; storing it anywhere else
would fork the lake's SSOT.

---

## Amendments — 2026-07-04 (S9 roster codification)

### A15 — Lint names re-pointed: `LINT-S2-*` → LINT-12/13/14 (COH-21 executed)
**Source:** S9 R8's normative roster table (per S1 A5's mapping; the 2026-07-02 closure
verification flagged that A5's "executed there" clause had never landed in this spec's text).
From this date: **`LINT-S2-drift` ≡ LINT-12 · `LINT-S2-schema` ≡ LINT-13 · `LINT-S2-pagerecord`
≡ LINT-14.** This spec's body text (R1, R12, Method 5–6, §6, A6) stands as written; the
`LINT-S2-*` names survive only as deprecated aliases, and the CI implementation registers under
the numeric ids. No check semantics change.

---

## Amendments — 2026-07-05 (EXECUTE run; user decision)

### A16 — R2/R12/R14: `verified_off_cl` — the off-CL resting state for outside-CL-corpus cases
**Source:** live EXECUTE finding (session-5 adjudication: *Entick v. Carrington* (1765, Court of
Common Pleas, 19 How. St. Tr. 1029; 95 Eng. Rep. 807) is honestly `not_found` — an English case
outside CL's corpus — yet holds a roster page). As written, R12's page↔record lint (`verified`/
`under_review` only) makes such a page **unpublishable forever**: its record can never reach
`verified` (the R2 two-key requires CL `citations[]` + party text) and `not_found` fails the
lint. The status vocabulary and lint gain one state; nothing else changes.

**Adds to R2 (no text superseded):** a fifth named edge case — (e) **outside-corpus** → a
`not_found` record MAY be elevated to **`verified_off_cl`** when it satisfies the **off-CL
two-key analogue**: **Key 1** — official citation(s) recorded from an authoritative reporter
(`citations.official` + parallels; for Entick: 19 How. St. Tr. 1029 / 95 Eng. Rep. 807);
**Key 2** — **≥2 independent R14-whitelisted sources** (Justia, Google Scholar, Cornell LII,
official court/reporter site) each confirming caption + cite + court + date, recorded as
`off_cl_links[]` with a G10 cross-check trail in `provenance` (per-source: url, what was
confirmed, checked-date). Identity fields stay CL-null (`cluster_id: null` is the honest
value); `identity_method: "off_cl"`. The elevation is an **orchestrator adjudication** (not
builder-automatic): each candidate is a named user-visible decision journaled at a session gate.

**Adds to R12:** the page↔record lint accepts `verified_off_cl` alongside `verified`/
`under_review` for the page↔record check. The drift lint/projector treat it as a normal managed
status; the projected frontmatter carries the off-CL reader links (R14's reader-link purpose).
The **treatment lanes stay CL-silent** for such records: Field-I derives from the R6 web lane +
S7 prose only, `varies_by_point` per normal rules; progeny stays empty with
`count_source: "off_cl_na"` — no lane may fabricate CL-shaped data for a record CL does not hold.

**Adds to R14 (no text superseded):** for `verified_off_cl` records the whitelist links are
**load-bearing identity evidence** (Key 2), not just reader fallbacks; the existing R14 check
(`every off_cl_links[].source on the whitelist`) plus a new check — every `verified_off_cl`
record carries ≥2 distinct-source `off_cl_links[]` and non-null `citations.official` — both
enforced by LINT-13 (schema) at build and re-verified at the S9 panel like any identity.

**Scope guard:** `verified_off_cl` is lawful ONLY where the R2 ladder exhausted honestly AND the
case is plausibly outside CL's corpus (pre-1789 English, some state-archaic, foreign); a US case
that *should* be in CL stays `not_found` pending investigation (R7's "not found ≠ fabricated"
discipline is unchanged). Expected initial population: exactly one (Entick).

---

## Amendments — 2026-07-06 (EXECUTE run; user decision)

### A17 — R14: whitelist extension for English/foreign-corpus cases (user Option 1)
**Source:** the R14 decision packet (`~/briefs/2026-07-06-r14-whitelist-english-cases.html`),
user disposition 2026-07-06: **"Extend for English-corpus cases: BAILII + scholarly/facsimile
second source"** (Option 1 as recommended).

**Adds to R14 (no text superseded), scoped to cases adjudicated outside CL's corpus (the A16
scope guard):** the whitelist gains **(a) BAILII** (bailii.org — Free Access to Law; treated as
official-reporter-equivalent for English case law) and **(b)** the scholarly/facsimile class:
**Founders' Constitution** (Univ. of Chicago Press scholarly edition) and **English Reports
facsimile** (CommonLII or an academic-hosted scan of the actual reporter page). The US-centric
whitelist members are unchanged; the new sources are NOT valid Key-2 evidence for a case CL
should hold.

**Precision + labeling honesty (recorded so trails stay literal):** (i) a scholarly/facsimile
source may confirm the decision **date to year precision**; day precision then rides the
reporter/BAILII record, and the per-source trail states the precision each source actually
supports — the `confirmed.date` field carries the adjudicated ISO date, never a fabricated one.
(ii) Where a source's **catalogue label** differs from the historical court of decision (BAILII
and the Wilson's-Reports reprint file *Entick* under K.B.; the State Trials report and modern
scholarship agree on C.P., Camden CJ), the record keeps the adjudicated historical court and the
trail notes the source's filing label — a cataloguing artifact is not an identity doubt.

**Population at signing:** Entick v. Carrington + Wilkes v. Wood, each elevated with BAILII +
Founders' Constitution (both sources live-confirmed 2026-07-06; BAILII content machine-verified
via archive.org snapshots because bailii.org bot-challenges non-interactive fetches — snapshot
URLs recorded in the adjudication trails).

### A18 — R11/A6: `folded-alias` — the lake terminal for alias-folded stub records
**Source:** packet-A Group-2 execution (2026-07-06, builder lane; orchestrator-ratified same
session). S6 R9 alias-folds need a machine-terminal for the passed-over record: `folded-alias`
joins the stub status vocabulary (schema enum + LINT-13). Semantics: the record is subsumed by
a controlling row — the manifest carries `folded_into`, the journal carries the
`s6-dedupe-pointer` + `packet-a.alias-fold` events, and provenance warns human readers. A
folded row is never authored, never counted as pending work, and never deleted (no silent
merges — R9). Population at signing: morse-v-french--6536632 (→ French v. Merrill) ·
carman-v-carroll--8693292 (→ carroll-v-carman--2750102) · united-states-v-chatrie--10881683
(→ Chatrie v. United States page row). The name matches S6 R11's ledger terminal
`folded-alias` by design.
