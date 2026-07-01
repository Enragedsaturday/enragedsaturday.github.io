# SPEC S2 — Verified Authority Database (the spine)

status: APPROVED
depends-on: [S1]   gates: [S3, S4, S5, S6, S7, S8, S9]
last-updated: 2026-07-01

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
three-lane treatment derivation, per-field provenance); the fabrication + corrupted-object machinery;
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
monolith. `AUTO:LINT-S2-schema`.

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
`CHECKLIST:D1` · `PROCESS` · maps guardrail G1/G3.

**R3 — Citations & pinpoints.** `citations` carries the official cite (`type=1`), parallels, vendor-
neutral (Lexis/WL/neutral), each typed, plus a `display` string. CL `citation.type` map:
`1 Federal · 2 State · 3 State-regional · 4 Specialty · 5 Scotus-early · 6 Lexis · 7 Westlaw ·
8 Neutral` (confirmed at build against the live schema). `pinpoints[]` harvests every pincite already
present on our pages: `{id, page, quote, star_marker, quote_fidelity}`, the page = nearest preceding
`*N` star marker, the quote **string-matched** against source text via `search_document`/read
(guardrails G3 quote-fidelity + G4 pincite). New pinpoints authored downstream (S7) are written back to
the lake and re-projected. *Check:* every stored pinpoint's quote verbatim-matches the source and its
page equals the nearest preceding star marker. `AUTO` · `CHECKLIST:D1/D2`.

**R4 — Progeny / citing-references map.** The committed record stores the **complete OR'd query**
(`cites:(<all sibling_ids OR'd>)`), the **deduped total** (`total_citing_cases`), `per_sibling`
counts, and the raw `citation_count` (no polarity) — **not** the full list. Live-verified example:
*Terry* = **22,182** OR'd (vs 19,711 / 2,967 single-sibling — single counts under-count). The full
progeny list lives out-of-repo (`cache/progeny/<slug>.jsonl`) + in SQLite, regenerable from the query.
Material citing edges are recorded under `treatment.point_overrides[].by[]` and `treatment.edges[]`
(R5). *Check:* `total_citing_cases` = the OR'd deduped count (never a single sibling); the raw cache
regenerates from `complete_query`. `AUTO` · maps §4 forward-chaining.

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
case with a cluster_id + Field-II verb + as_of. `AUTO:LINT-6` · `CHECKLIST:D3`.

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
maps §3 KEY-2 / §4 phase 3–4.

**R7 — Fabrication + corrupted-object machinery.** "**Not found ≠ fabricated**": a `not_found` is
recent / outside-coverage / wrong-cite until a name+court+date **and** web cross-check say otherwise —
block + investigate, never auto-delete (guardrail G3). Name-mismatch → `fabrication_suspected`
(compare input vs canonical ourselves). A committed **`lake/_denylist.json`** hard-blocks known
corrupted CL objects — **Chatrie `10881683`** (index says SCOTUS/Chatrie, text is *Harmon v. ABC 2
News*) and **Zorn `10813527`** (text is *Strike 3 Holdings*) — each with its web-verified truth; the
builder refuses these ids and records the block. *Check:* no denylisted id is ever ingested; every
`not_found`/`fabrication_suspected` carries a cross-check trail. `AUTO` · `PROCESS`.

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
raw progeny/text. `PROCESS`.

**R10 — Build path: Codex, direct REST v4, paced + cached + resumable.** The builder is a **Python 3
stdlib** script (`scripts/s2/ingest.py`; `urllib`+`json`+`sqlite3`, zero third-party deps) run by Codex
headless (`codex exec … -c sandbox_workspace_write.network_access=true`, wrapped in a timeout; **no
MCP**). Token from `~/.config/cssi/cl-token` (mode 600, never committed). **Pacing:** token-bucket
≤~14 req/min + jitter (~840/hr, headroom under the ~1,000/hr ceiling); sha1(url) HTTP cache (identity/
cluster ~immutable for the run, treatment scans fresh); per-case-per-step resumable journal; exponential
backoff on 429/5xx; `analyze_citations` capped ~60/min with `job_id`/`resume_citation_analysis`.
*Check:* a killed run resumes from the journal with no duplicate CL calls; cache hits skip the network;
the run stays under the hourly ceiling. `PROCESS`.

**R11 — Lake scope / roster + the S2/S6/S8 boundary.** Build **verified records for the 457 existing
`content/cases/` pages now**, **and** run **identity + fabrication-check** on the **named-but-no-page
roster** (the S6 audit list) → **frontier stubs** (`status: verified_identity | not_found |
fabrication_suspected`) carrying identity + official cite + off-CL link **only** — **no treatment /
progeny derivation until S6 promotes a stub to a page.** **Authoring is S6's; case/term linking is
S8's.** S2 hands S6 verified cluster_ids + fabrication flags. *Check:* every existing case page has a
`verified`/`under_review` record; every roster entry has a stub with a status; no stub carries a page
or authored prose. `PROCESS`.

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
`AUTO:LINT-S2-drift` · `AUTO:LINT-S2-pagerecord`.

**R13 — Derived SQLite query layer (rebuildable).** `authority.sqlite`, loaded from `cases/` + the
progeny cache, holds: `cases` (record_id, cluster_id, lead_opinion_id, court_level, year,
field_i_validity, as_of_*, authority_weight, status), `citations`, `siblings`, `progeny`
(total_citing, per_sibling, complete_query), `edges` (material treatment edges: cited_case,
cluster_id, field_ii, field_iii, point), **`intra_edges`** (the intra-corpus citation graph — which of
*our* cases cite which, ≤~900 nodes), `coverage` (roster reconciliation for S6/S8), `overrides`
(point_overrides + controlling-case FKs for the staleness check), `provenance`. Not a source of truth —
droppable and rebuilt anytime. *Check:* the DB rebuilds deterministically from `cases/` + cache; every
`cases` row round-trips to its JSON record. `AUTO`.

**R14 — Off-CL link whitelist + vetting.** Coverage-gap fallbacks are drawn from a whitelist —
**Justia, Google Scholar, Cornell LII, the official court/reporter site** — for reader links + parallel-
cite cross-check + independent citing-refs corroboration (G10). No open-web parametric links. *Check:*
every `off_cl_links[].source` is on the whitelist. `AUTO`.

**R15 — S2 build-QA gates + the S9 boundary.** S2 acceptance = **structural gates**: 100% schema-valid;
100% two-key on `verified` records; denylist enforced; dual dates + provenance present; drift lint +
page↔record lint green. **Build-review lanes** (lighter than S9): Codex builds; a **2nd Codex lane**
spot-checks ≥1-in-10 identities/cites (PRACTICES §3 governance, escalate on any error); the **Claude
lane** audits the treatment derivations. The **full 1-Claude+2-Codex per-proposition adversarial panel +
forced primary reads are S9's** deep pass reading *from* the lake. *Check:* the four structural gates
pass; the ≥1-in-10 sample logged; treatment audit recorded. `PROCESS`.

## 4. Lessons enforced
Directly answers the O2 findings: **CL is not a good-law oracle** (R5/R6 derive treatment from progeny
text + web over three lanes incl. recency; the Overhaul-1 biggest catch came from an out-of-band human
pass — now first-class). **Corrupted objects** (R7 denylist: Chatrie/Zorn). **Publish drift** (R12:
lake = SSOT, frontmatter generated + drift-linted, two-directional). **Name-rank fabrication risk**
(R2: citation-disambiguated two-key, live-proven necessary). **Under-verified quotes/pincites** (R3:
G3/G4 string-match). Carries S1 R2 (3-field treatment) and the guardrails G1/G3/G9/G10.

## 5. Method (execution — one autonomous run, Codex builds)
1. **Scaffold** `_overhaul2/lake/` (`_schema.json`, `_denylist.json`, `_manifest.json` seeded from the
   457 roster + the S6 audit list) + `/Volumes/AIStore2/cssi-lake/` cache dirs.
2. **Build `scripts/s2/ingest.py`** (Python stdlib): paced/cached/resumable CL v4 client; per-case →
   R2 identity, R3 cites+pinpoints, R4 progeny, R6 three-lane treatment, R8 provenance; frontier stubs
   per R11; denylist per R7.
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

## 7. Acceptance criteria
- [ ] `s2.v1` schema authored; every record schema-valid and canonical-serializer round-trips (R1).
- [ ] 100% of `verified` records pass the citation-disambiguated two-key; every non-verified carries a
      reason code; four identity edge cases handled (R2).
- [ ] Typed cites + star-paginated pinpoints; every stored quote verbatim-matches source (R3).
- [ ] Progeny stored as count+query+edges (OR'd deduped total); full list regenerates from cache (R4).
- [ ] 3-field treatment + dual dates + composite(principal-holding)+`varies_by_point` marker + point-
      overrides; no bare composite without `varies` when overrides exist (R5).
- [ ] Three-lane derivation (negative-keyword + top-25-cited + recency) run on every verified case;
      derivation trail recorded; negatives staged for S9 two-reviewer (R6).
- [ ] "Not found ≠ fabricated" enforced; Chatrie/Zorn denylist blocks ingest (R7).
- [ ] Per-record + per-judgment-field provenance present (R8).
- [ ] Three stores stood up; records survive without the volume; DB + cache rebuild from `cases/` (R9/R13).
- [ ] Builder paced + cached + resumable under the hourly ceiling; a killed run resumes cleanly (R10).
- [ ] 457 verified + frontier identity stubs; no stub authored; S6/S8 boundary respected (R11).
- [ ] Projection contract enforced; two-directional drift lint + page↔record lint green; `draft` exempt (R12).
- [ ] Off-CL links whitelisted only (R14).
- [ ] S2 structural gates pass; ≥1-in-10 spot-check + treatment audit logged; S9 boundary held (R15).

## 8. Verification plan
S2's own build-QA (R15) gates the lake. **S9** then reads *from* the lake and runs the full per-
proposition adversarial panel (1 Claude + 2 Codex, ≥2-of-3 refute), forced primary reads on recent/high-
profile cases, the 10-gate protocol, and the ledger — adjudicating every negative-treatment event S2
staged. The drift, page↔record, and schema lints run in CI fail-closed on every change.

## 9. Open items / escalations
- **S3 binding.** `point_overrides[].point` slugs are **provisional**; a binding map (`point → S3 node`)
  + a fail-closed lint activate **after S3 exists**. 1:N / N:1 taxonomy splits handled by the map.
- **Treatment-lane parameters** (recency window = last 3 terms / ≤3 yrs; top-N = 25) are **execution-
  tunable defaults** — revisit against real hit-rates during the run.
- **Override staleness propagation** (a controlling case's own `field_i` later changes) — the SQLite
  `overrides` consistency check flags it; automated re-derivation is a **maintenance-loop** task (GH#2).
- **Lake permanent home.** Built at `_overhaul2/lake/` for the run; graduation to a permanent
  `data/authority/` home is a post-publish (maintenance-loop) task, referenced via a single path constant.
- **CL `citation.type` enum** confirmed against the live schema at build (observed 1/2/6 on *Terry*).
- Frontier-stub edge cases (alias/variant collisions, cite-format placeholders) reconciled with the S6
  audit list at build.

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
- **SD5** three-lane defaults (regex set; top-25; last-3-terms/≤3-yrs recency) — tunable.
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
