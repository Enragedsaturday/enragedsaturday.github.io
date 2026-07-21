# I1-PREP summary — S9 R7.1 recency-lane query preparation

**Packet:** I1-PREP (WS=I1, S9 §5 P4, R7.1 currency sweep). **Lane/model:** `claude-opus-4-8`.
**Write-scope honored:** `_run/s9/p4/` only. **NO CourtListener calls** — this packet only
BUILDS the query list; the S2-builder serial CL lane executes them (P4-PLAN Wave S).
**Output:** `_run/s9/p4/recency-queries.json` (13 objects) + this file.

## Coverage (deterministic)

- **Categories assigned:** 13 (the 12 doctrine dirs under `content/` + note that 2 may be no-lane).
- **Categories examined:** 13 / 13.
- **Recency lanes built:** 11. **No-lane recorded (with reason):** 2.
- **Key cases selected:** 162 (11 lanes × ≤15). **Cases cut by the ~15 cap:** 506 (all recorded per category in `cut[]`).
- **Skipped:** 0.

| category | keys | cut | OR'd opinion IDs | slip cases |
|---|---|---|---|---|
| confessions-interrogation-and-the-fifth-amendment | 15 | 63 | 49 | 0 |
| fair-trial-and-reliability-doctrines | 15 | 24 | 52 | 0 |
| foundations-and-the-fourth-amendment | 12 | 0 | 42 | 0 |
| instructor-craft-and-study | no-lane | - | - | - |
| legal-system-research-and-reference | no-lane | - | - | - |
| searches | 15 | 58 | 53 | 1 |
| seizures | 15 | 73 | 54 | 0 |
| standards-of-proof | 15 | 18 | 58 | 0 |
| the-exclusionary-rule-remedies-and-standing | 15 | 39 | 56 | 0 |
| the-right-to-counsel | 15 | 10 | 67 | 0 |
| the-warrant | 15 | 28 | 44 | 0 |
| use-of-force-and-liability | 15 | 64 | 32 | 0 |
| warrant-exceptions | 15 | 129 | 55 | 0 |

## No-lane categories (recorded per task instruction)

- **instructor-craft-and-study** — pages are `type: craft` (CREW, Three Golden Rules, Instructor
  Development). Zero `[!rule]` callouts, zero registry points. The four cases they cite (Graham
  v. Connor, Maryland v. Buie, Illinois v. Gates, Brinegar v. United States) are worked *teaching
  examples*; their doctrine is owned and recency-monitored under the home categories
  (use-of-force-and-liability, warrant-exceptions/seizures, standards-of-proof). No independent
  case-law surface → no recency lane.
- **legal-system-research-and-reference** — pages are `type: reference/practical/index` (Reading
  and Citing Cases, Legal Research Tools, Verifying Good Law, The Federal Court System, State
  Citations and Conventions, Common Legal Terms glossary, Case Index navigation). Zero registry
  points, zero rule/key-case authorities, no doctrine whose progeny could be monitored → no lane.

## Method

**Key-case set per category = union of:**
1. **Rule-callout authorities** — every case wikilinked inside a `> [!rule]` black-letter callout
   on any page in `content/<category>/**` (79 rule callouts corpus-wide; this is the strongest
   doctrine-shaping signal).
2. **`## Key cases` / `## Related cases` table authorities** — the first wikilink of each table row.
3. **Registry-point authorities** — for every `registry.yaml` node homed in the category
   (parsed via `scripts/lint/_common.py::parse_yaml_subset`, 80 nodes across 11 categories),
   the cases named in the node `statement`/`label`.

**Case→lake resolution** (for opinion IDs + official cite): wikilink/citation string matched to a
lake record by exact `record_id`, then case-insensitive, then trailing-`(YYYY)`-stripped, then a
normalized key (punctuation/apostrophe/period-insensitive, trailing-parenthetical-stripped). The
normalized tier recovered `United States v. United States District Court (Keith)` and
`Michigan Dept. of State Police v. Sitz`. Only unmatched `X v. Y` strings (no lake record) are
excluded and listed per category in `notes`.

**Ranking / the ~15 cap.** Score = `rule`(+3) + `keycase`(+2) + `registry`(+2) + extra-page
breadth(+1 each) + SCOTUS(+2). Tie-break: SCOTUS first, then `progeny.indexed_citing_opinions`
(more citing progeny = more to monitor), then year desc, then name. Top 15 kept; the remainder
recorded in `cut[]` with score + progeny count. This deliberately prefers cases that are
**black-letter authorities on the category's own pages** over cases merely tabled once — e.g. in
`the-warrant`, Connally v. Georgia / Bailey v. United States (rule+registry, score 9) are kept
over Maryland v. Garrison / Coolidge v. New Hampshire (key-case-table only, score 7/6) even though
the latter have more raw progeny.

**Cite + ID recovery cascades** (per case, from its lake JSON):
- *official cite* → `citations.official.cite` → `citations.display` → `citations.official_selection.selected`
  → first `citations.all[]` U.S./type-1 reporter → else slip (no reporter cite).
- *cites() opinion IDs* → `progeny.complete_query` (the exact S6-built id list) → `identity.sibling_ids`
  → `[lead_opinion_id]` → `[cluster_id]` → none.

## S6 phrasing divergences (task requirement — mirror S6, record divergence)

The naive pattern in the packet text is `cites:(<key case cite strings>) AND filed_after:2026-07-04`.
S6's actual recency phrasing differs on three counts; I mirrored S6 and preserved the naive form
alongside for reference.

1. **`cites:` takes OPINION IDs, not citation strings (primary divergence).** S2 R4/R6 and every
   lake record's `progeny.complete_query` show the operator as `cites:(<all sibling opinion IDs
   OR'd>)` — e.g. Terry = `cites:(107729 OR 9423752 OR 9423753 OR 9423754 OR 9423755)`.
   CourtListener's `cites:` operator indexes citations *by opinion id*; it does **not** accept
   reporter citation strings ("392 U.S. 1"), so the naive cite-string form returns nothing.
   → The executable `query` field uses OR'd opinion IDs (S6-faithful). A `query_naive_cites`
   field preserves the literal cite-string / quoted-slip-name form the packet described, marked
   non-executable. Per-case `sibling_ids`, `id_source`, and `cluster_id` are carried in each
   `key_cases[]` entry so the builder lane can audit the id set.

2. **filed_after floor differs from S6 lane-3's rolling window.** S6 treatment-derivation lane-3
   (S2 R6, A9(b), A11) used a rolling `filed_after = build_date − 3 years`. R7.1's recency
   *re-run* instead uses a fixed `filed_after:2026-07-04` — "any decision **since** the S2 build /
   spec signing," not a 3-year lookback. This is the correct R7.1 semantic (currency since build)
   and is intentionally not the S6 lane-3 window. Matches the pattern already used in the P1/P4
   marker-poll log (`filed_after=2026-06-01`/`2025-10-01` per-marker floors).

3. **Per-category consolidation vs S6 per-case queries.** S6 ran one `cites()` query per case
   (ORing that case's own siblings). R7.1 here issues one query per *category*, ORing all ≤15 key
   cases' siblings — a union of citing-graphs, more efficient for a completeness sweep, semantically
   equivalent to running the per-case queries and unioning results. (S6's separate *lane-1*
   negative-keyword form, `cites:(<siblings>) AND (overrul* OR abrogat* …)`, is a different
   instrument — treatment, not recency — and is deliberately not reproduced here.)

## Notes / flags for the S2-builder serial CL lane

- **Slip-only cases** (no reporter cite; still contribute their opinion IDs to `cites()`, and
  appear name-in-quotes in the naive form): `Chatrie v. United States` (searches). Other very
  recent slips (Case v. Montana, District of Columbia v. R.W., State v. Volle, Postal Service v.
  Konan, Landor, Olivier, Robinson, Goldey, Gutierrez) fell below the cap and sit in `cut[]`.
- **Zero-ID key case:** `Entick v. Carrington` (foundations) — 1765 English case, no CL opinion
  record (no cluster_id/opinion id). It is a legitimate foundations authority but contributes
  **no** IDs to the query and cannot be recency-monitored; flagged in that category's `notes`.
- **ID fallbacks** (sibling_ids empty → lead_opinion_id/cluster_id used): recorded per category in
  `notes`; e.g. foundations `United States v. Lee` via `lead_opinion_id=101118` (274 U.S. 559,
  1927 — verified correct case, not a namesake).
- **Query length:** category queries OR up to ~67 opinion IDs (the-right-to-counsel). Long but
  valid; the builder should page results and pace ≤14 calls/min per P4-PLAN Wave S.
- **cite recovery for null-official records:** several non-slip SCOTUS cases have
  `citations.official=null` in the lake (Jardines, Atwater, Maryland v. King, McNeely, Navarette,
  etc., reason `unlisted_reporter:Fla. L. Weekly Fed. S`); their real U.S. cite was recovered from
  `citations.all[]` for the `cite` metadata. This is a lake data-quality observation for the
  builder, not a query blocker (IDs come from `sibling_ids`/`complete_query`, which are present).

## Ambiguities for the orchestrator to rule on

1. **Scope of "key cases" = rule-callout + Key-cases-table + registry** (my operating definition).
   If R7.1 intends *only* the tighter black-letter rule-callout set, the cut lists already isolate
   the delta (drop key-case-table-only authorities). Flagging in case a narrower reading is wanted.
2. **Per-category vs per-case query granularity** (divergence #3). I consolidated to one query per
   category. If the builder prefers S6's per-case granularity for cleaner attribution of which
   anchor a new decision cites, each `key_cases[].sibling_ids` supports regenerating per-case
   `cites()` queries without re-deriving the set.
3. **filed_after date** fixed at `2026-07-04` (spec-signing / S2-build floor). If the intended
   floor is the actual S2 lake build date (if later), the single constant is trivially swapped.
