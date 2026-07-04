# Points-of-Law Registry + S2 Binding Map (S3 Phase 3)

This directory is the **join key** between the taxonomy (S3), case-treatment
(S2), doctrine assertions (S7), and linking/transclusion (S8). It is the S3 R4/R5
deliverable, built at `_overhaul2/points/` for the run; graduation to
`data/points/` is a post-publish task referenced through a single path constant
(S3 §9, mirrors S2's lake root).

## The two-artifact contract

| File | Owner spec | Purpose |
|---|---|---|
| `registry.yaml` | S3 R4 + R6 + Appendix C | The controlled list of **points of law** — atomic legal propositions finer than a page. Each node `{id, label, statement, home_page, also_on[], status}` (+ build-provenance `seed`, `why`). |
| `s2-binding.yaml` | S3 R5 + S2 A8/A13 | Maps **every** S2 `treatment.point_overrides[].point` provisional slug (and slug-valued `composite_basis_ref`) to one or more registry node ids. 1:N / N:1 allowed. |

A point of law is minted **only** under the R6 granularity rule — (a) S2 has, or
plausibly could have, **split treatment** on it; (b) it is a distinct
**black-letter rule** a page states; or (c) it is **transcluded** across pages —
never per sentence. **Page split = point split** (the calibration anchor: the SIA
family resolves to four distinct nodes — `search.person.sia` (Robinson),
`search.person.sia-cellphone` (Riley), `search.person.sia-alcohol` (Birchfield),
`search.vehicle.sia-recent-occupant` (Belton/Gant) — mirroring the SIA page split
the tree already carries). Every node carries a grep-able `why:` field: seeds say
`SEED (Appendix C)`; beyond-seed nodes cite the R6 clause. The orchestrator
adjudicates the minted set from those justifications.

**id grammar:** `area.object.point`, kebab-case; the `object` segment is omitted
where it does not apply (`proof.probable-cause`) and sub-point segments are allowed
(`search.home.exigency.emergency-aid`). `area` ~ the 13 categories
(`foundations`, `proof`, `search`, `seizure`, `warrant`, `remedy`, `confession`,
`counsel`, `fairtrial`, `liability`).

**statement grade:** all nodes ship `status: draft` (S7 refines to `verified`).
A node homed to an **authored** page carries a verbatim-grounded 1–3 sentence
proposition harvested from that page's black-letter rule (NO invented law). A node
homed to a **placed-empty stub** (R7) carries `statement: ''` — **except**
load-bearing nodes (the Belton/Gant `search.vehicle.sia-recent-occupant` binding
target, the two geofence binding targets, and Appendix C seed pairs whose rule
lives on a sibling authored page recorded in `also_on`), which carry a grounded
draft sourced from a case treatment record or a sibling authored page.

**Scope note — what is NOT minted:** reference pages (Category 12: Case Index,
Common Legal Terms, Legal Research Tools, Reading & Citing Cases, Federal Court
System, Verifying Good Law, State Citations) and instructor-craft pages
(Category 13: CREW, Three Golden Rules, Instructor Development) state no
black-letter search-and-seizure rule that treatment binds to — they get no nodes.
Within Foundations, Common Law Origins (history), the Analysis Checklist (method
scaffolding that transcludes other nodes), and Recalibration (framing) likewise
state no independent rule; only `foundations.fourth-amendment-framework` is minted.

## The R5 lint semantics

The fail-closed CI lint (`AUTO:LINT-S3-binding`, per S2 A8) **activates only once
both artifacts exist on the branch — which they now do.** It then enforces:

1. **(a)** every `point_overrides[].point` slug present in the lake resolves to
   ≥1 registry node;
2. **(b)** every bound node id exists in `registry.yaml`;
3. **(c)** the bound node's `home_page` renders the override's treatment
   (per-page routing) — e.g. Belton's `superseded` flag renders on the
   SIA — Vehicles node, while the Belton case page composite stays `caution / varies`.

The lint reads the lake (`_overhaul2/lake/cases/*.json`) at CI time. It **fails
closed** on any unbound override slug or any dangling node id. Companion registry
lint (`AUTO:LINT-S3-points`, R4): every node schema-validates, every `home_page`
and `also_on[]` resolves to a page on disk, ids are unique.

Until S3 binding lands, S2 emits `s3_binding_status: "provisional"` on every
override; the flip provisional → **bound** requires both artifacts present (S2 A8),
and the S9 prose-reference recheck (a 1:N slug split flags every page whose prose
cites the split slug) runs after binding.

## The `pending_slug` convention

`s2-binding.yaml` has two row shapes:

- **`bound[]`** — the slug is already present in the lake / projected into
  content-page frontmatter (currently: `search.vehicle.sia-recent-occupant` from
  Belton's A13 migration override, and `search.warrant.geofence-general-warrant`
  + the `search.digital.geofence-threshold` composite from *United States v. Smith*
  (2024)). These rows are **live now**.
- **`pending[]`** — a `{pending_slug: true, case, cluster_id, expected_field_ii,
  nodes, note}` row that **pre-registers the expected mapping keyed by case** for
  a `limited`-list override that S2 A13 + `lake/_treatment-migration.json`
  guarantee **will** exist but has not yet been minted by the running S2 build.
  The `cluster_id` lets the lint **activate incrementally**: the instant S2 writes
  that case's `point_overrides[].point`, the lint matches the pending row by
  cluster and treats the (now-live) slug as bound to `nodes[]`. No pending row
  ever fails the lint on its own — it is a promise, not a live edge.

The 11 mandatory `limited` cases are Belton (**already bound**, not repeated as
pending), plus the 10 pending rows: Boyd, Coolidge, Escobedo, Mathis (1968),
Monroe v. Pape, Elstad, Saucier, Thornton, Agurs, Chadwick. Each pending row names
the registry node the override is expected to bind (all 10 point at nodes that
already exist in `registry.yaml`, so the lint can bind them the moment the slug
lands).

**`cluster_id` = CourtListener cluster id** — the `/opinion/<cluster_id>/` value in
each case page's `courtlistener.opinion_url` (the frontmatter field is mislabeled
`opinion_id` but equals the lake record's `cluster_id`; verified on Terry v. Ohio
= 107729). This deliberately sidesteps the cluster-vs-opinion id confusion.

## GH#2 staleness note

Point-scoped treatment can go stale when a **controlling** case's own validity
later changes (e.g., if *Gant* were itself narrowed, the `superseded_by` edge on
`search.vehicle.sia-recent-occupant` would need re-derivation). The registry
records the point and its binding; **automatic re-derivation of overrides on
controlling-case drift is GH#2** (post-publish maintenance / citator), flagged by
the S2 R13 SQLite `overrides` check. Point slugs are **stable strings once minted**
(S2 A8) — taxonomy splits/renames are absorbed by this binding map, never by
re-spelling a slug.
