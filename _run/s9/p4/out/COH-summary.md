# COH packet summary — S9 R10 cross-layer coherence gates

Lane `COH` · model `claude-opus-4-8` · findings-only (no verdicts, no edits outside `_run/s9/p4/`).
Governing text: `_overhaul2/specs/S9-verification.spec.md` R10. Evidence from the lake, the
registry, the binding map, rendered `content/` pages, and prior `_run/s9/` artifacts. No CL.

**S3 binding-map artifact used:** `_overhaul2/points/s2-binding.yaml` (the point→node map; LINT-21
reads it). No separate S3 binding-map artifact exists under `_run/`; this is the one.

## Coverage (assigned / examined / skipped)

| Gate | Assigned | Examined | Skipped (reason) | Defect rows |
|---|---|---|---|---|
| (a) callout↔registry deep-equal | 80 registry nodes | 80 | 0 | 80 + 1 systemic |
| (a) override-slug resolution | 13 distinct slugs (14 instances) | 13 | 0 | 0 (all resolve) |
| (a) S2F-07b provisional-slug recheck | 10 provisional slugs | 10 | 0 | 0 (no 1:N split) |
| (b) prose↔lake treatment | 610 case pages | 609 | 1 (draft page) | 11 |
| (c) LINT-12 / LINT-14 | corpus | corpus | 0 | 151 (LINT-12) |
| (c) A13 REVIEW-row adjudication | migration rows | 0 exist | — | 0 |

Total candidate rows in `COH-findings.jsonl`: **243** (high 198, medium 43, low 2).
No silent truncation. Every node/page in scope carries a status.

## Gate (a) — callout↔registry + slugs + S2F-07b

**Method (deep-equal):** parsed `registry.yaml` via `_common.parse_yaml_subset`; grouped the 80
`registry_callout_pair` nodes by `home_page`; extracted each page's `> [!rule]` callout, split by
`^rule-<tail>` anchors; matched node→paragraph by anchor tail (shared-anchor pages match all their
nodes to the one paragraph). Normalized BOTH sides identically: markdown-link→text, wikilink→case
name (`… v. …`) or display, strip bold/italic, curly→straight quotes, dash-fold, whitespace-collapse
(Level A). A second pass additionally strips all quote glyphs + lowercases (Level B) to isolate
cosmetic-only divergence. Citation tokens (reporter cites + pincites + years) extracted and diffed.

**Result — R10(a) deep-equal FAILS corpus-wide.** The registry `statement` field is a hand-edited
paraphrase of the home-page callout, NOT a verbatim mirror. Taxonomy over 80 nodes:

| Bucket | Count | Meaning |
|---|---|---|
| **verbatim** (Level-A byte-equal after formatting-normalization) | **0** | none pass strict deep-equal |
| **cosmetic** (Level-B match; differ only in quote-glyph/punct/format) | **2** | `proof.reasonable-suspicion`, `proof.probable-cause` |
| **substantive** | **75** | real prose/citation divergence |
| — content-divergence (wording added/dropped/changed) | 14 | e.g. `proof.proof-ladder` drops "through the eyes of a reasonable, experienced officer" |
| — cite-divergence (citation tokens differ) | 61 | of which pincite-drop-only=16, different-authority=45 |
| **no-callout** (home_page has NO `[!rule]` block to compare) | **3** | see below |

The 3 **no-callout** nodes: `remedy.exclusionary` (home `…/the-exclusionary-rule/index.md`, **type
doctrine** → HIGH: a doctrine page with no rule callout violates S5 R2 and makes deep-equal
impossible), `foundations.fourth-amendment-framework` (type hub), `warrant.requirement` (type
index). The two overview/hub/index home_pages carry `also_on: []`, so the node's rule text lives on
no authored callout anywhere — the statement is unverifiable against a callout.

Representative substantive cite-divergences (both texts + cite sets in `COH-report.json`
`mismatch_list` and per-row `evidence`):
- `search.aerial-surveillance` — callout pincites `476 U.S. 207, 215` / `488 U.S. 445, 451-52`;
  statement drops to `476 U.S. 207` / `488 U.S. 445`.
- `seizure.person.constructive-entry` — callout cites SCOTUS (`445 U.S. 573`, `451 U.S. 204`);
  statement cites circuit cases (`49 F.3d 1423`, `765 F.3d 1049`, `784 F.2d 890`) — different
  authorities entirely.
- `seizure.person.noninvestigative-caretaking` / `search.home.community-caretaking` — same pattern
  (SCOTUS in callout vs F.3d/F.4th in statement).

**Every mismatch is reported with both normalized texts** in `COH-findings.jsonl` (per-row
`evidence`) and both raw + normalized texts in `COH-report.json` `gate_a_callout_registry.mismatch_list`.

**ORCHESTRATOR RULING REQUIRED (do not auto-accept):** R10(a) and S5 R2 say "deep-equal", but the
corpus implements a semantic paraphrase. Either (i) the gate is literally byte-deep-equal and ~78
statements must be rewritten to verbatim-mirror their callouts (large fix), or (ii) the gate is
semantic and only the cite-divergences / no-callout cases are true defects. This is the single
`callout-registry-gate-systemic` HIGH row. I did not decide it — that is your call.

**Override-slug resolution (PASS):** 13 distinct override slugs (14 instances) across the lake
(`treatment.point_overrides[].point` + slug-shaped `composite_basis_ref`). LINT-21 → 0 high, 0 medium,
10 low. 3 resolve **bound-live** (`search.vehicle.sia-recent-occupant`,
`search.warrant.geofence-general-warrant`, `search.digital.geofence-threshold`); 10
`legacy-limited-*` resolve **bound-PENDING** (matched to `pending[]` by `cluster_id` — a promise, LOW,
not a defect). Zero unbound. No candidate rows filed (all resolve).

**S2F-07b (PASS):** the 10 provisional (`s3_binding_status:"provisional"`) slugs each appear on
exactly one page (their own case-page frontmatter). No slug binds to >1 distinct registry node, so
there is **no 1:N split** to flag; nothing to re-check post-binding. Zero pages flagged.

## Gate (b) — prose↔lake treatment (script + 20-row hand sample)

**Method:** scripted over all `content/cases/*.md` (type:case, non-draft). Per page: resolved the
lake record, extracted the `## Treatment & subsequent history` section, checked (1) R5-mandated
point-status table presence when lake has `point_overrides`/`varies_by_point`; (2) each override's
controlling authority named in the table; (3) status-word vs `field_i_validity` contradiction;
(4) any shown `(as of …)` date ∈ lake `as_of_*`; (5) orphan table; (6) `unverified` record asserting
a definite treatment without the ⚪ banner.

**Result:** 609 examined, **598 clean**, 1 skipped (draft). **11 defects, all one class:**
`prose-lake-missing-point-status-table` — of 12 `varies_by_point` lake records, only Belton and
Smith render the R5-mandated point-status table; the other 10 legacy-limited pages (Boyd, Coolidge,
Escobedo, Mathis, Monroe, Elstad, Saucier, Thornton, Agurs, Chadwick) plus Gouled render the simple
status form with no table. Severity **medium** — the underlying frontmatter/lake data is consistent;
the prose layer just doesn't surface the R5 table. NOTE for adjudication: these overrides are
provisional placeholders ("Legacy limited treatment point", `s3_binding_status:"provisional"`), and
prior P2 `treatment-noise` adjudications (e.g. F-S9-PR-3e2c7f0d62, -373fde4bd9) DISMISSED
`varies_by_point`-flag discrepancies as noise — you may rule these the same deferral.

**Zero** status-word contradictions, date drifts, orphan tables, or unverified-unbannered pages
across the other 598 pages. All 151 `unverified` pages carry the ⚪/unverified banner.

**20-row hand-verified PASS sample (20/20 correct):** treatment section read against the lake record.
superseded: Aguilar v. Texas, Jones v. United States, Michigan v. Jackson, Olmstead v. United States
(all render overruled/abrogated + Historical, consistent). good_law: Abel, Byrd, Davis (2011),
Gooding, Kentucky v. King, Michigan v. DeFillippo, Orozco, Smith v. Illinois, Cortez, Ramsey (all
"good"). unverified: A Quantity of Copies of Books v. Kansas, Imbler v. Pachtman, Stone v. Powell,
United States v. Liddell (all ⚪-bannered). caution/varies: New York v. Belton (composite + table,
Superseded/Gant). good_law/varies: United States v. Smith (2024) (composite + table, confirmed by
Chatrie). *One sample (A Quantity of Copies of Books) initially looked unbannered on a truncated
preview; the full section carries the "*Status note (⚪):*" banner — true PASS. Confirmed the ⚪
codepoint check corpus-wide.*

## Gate (c) — projection (LINT-12/14 + A13 REVIEW rows)

- **LINT-14 (page↔record):** `0` violations — **GREEN / PASS**.
- **LINT-12 (lake↔frontmatter drift):** **151 HIGH — RED / FAIL** (R10c requires green). Field
  frequency: `courtlistener.opinion_id` ×140, `lake.projected_at` ×140, `treatment.scope_note` ×9,
  `authority_weight` ×4, `treatment.varies_by_point` ×1 (Gouled), `citation` ×1, `parallel_cite` ×1.
  **136 pages are a pure re-projection-stale class** (`opinion_id: null` → expected lead_opinion_id;
  stale `projected_at`) — mechanical, cured by re-running `scripts/s2/project.py`. **15 rows are
  substantive** (scope_note / authority_weight / varies_by_point / citation / parallel_cite drift).
  Emitted as 151 per-page `lint12-drift` rows, each tagged `reprojection-stale` or
  `substantive-drift` in `evidence`. NOT previously adjudicated (grep of adjudications = 0 for
  opinion_id/projected_at/drift).
- **A13 REVIEW rows (PASS, vacuous):** `a13_gate()` → 0 REVIEW pages, 0 unmapped, 0
  missing-status; all 609 pages are new-form (`field_i_validity`). `lake/_treatment-migration.json`
  carries mapping tables + a `review_policy`, but **no per-row REVIEW markers**, and no page carries
  legacy `treatment.status: REVIEW`. So there are zero REVIEW-marked migration rows requiring an
  adjudication — the requirement is satisfied with nothing to check.

## Items for orchestrator adjudication (ambiguities I did NOT decide)

1. **callout↔registry deep-equal interpretation** (the systemic HIGH row) — verbatim-mirror rewrite
   vs semantic gate. Blocks R10(a) either way.
2. **3 no-callout home_pages** — `remedy.exclusionary` (doctrine page missing its rule callout =
   likely real HIGH); the hub/index home_page assignments for `foundations.fourth-amendment-framework`
   and `warrant.requirement` (statement has no callout anywhere; possibly a home_page/also_on fix).
3. **10 legacy-limited + Gouled missing point-status tables** — real R5 gap or accepted provisional
   deferral (cf. dismissed P2 treatment-noise rows).
4. **LINT-12 red** — the 136-page re-projection is mechanical (route to a re-project fix packet); the
   15 substantive drifts (incl. Gouled `varies_by_point`, Kalkines `authority_weight`) need review.

## Dedup

Checked `_run/s9/adjudications.jsonl` (2331 rows). No prior adjudication of: callout↔registry
deep-equal (the 14 callout-mentioning rows are holding-substance SUPPORT adjudications, not
deep-equal text; F-S9-PR-abd71b69e2 dismissed geofence-threshold callout *correctness*, a different
axis), LINT-12 opinion_id/projected_at drift (0 hits), or missing point-status tables (0 hits). All
COH findings are fresh. `_review-needed/` contains no callout/registry/drift/table register.

## Artifacts
- `_run/s9/p4/out/COH-report.json` — per-gate pass/fail counts + full mismatch lists (both texts).
- `_run/s9/p4/out/COH-findings.jsonl` — 243 `p4.candidate.v1` rows.
- `_run/s9/p4/out/COH-summary.md` — this file.
