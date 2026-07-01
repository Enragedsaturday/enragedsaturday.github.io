# CourtListener → Data-Lake Field Inventory (S2 seed)

*Live-verified against the CourtListener v4 API (via MCP), 2026-07-01. Sample: Terry v. Ohio,
392 U.S. 1 (1968) → cluster `107729`. This is the concrete schema seed for S2 (Verified Authority
Database). Object model: **Docket → Cluster (the "case") → Opinions (N sub-opinions)**; the cluster
is the primary case record, opinions hold text + the citation graph.*

## Critical gotchas (read first)
1. **`cluster_id` ≠ `opinion_id`** (but can coincide as a legacy artifact — Terry cluster `107729`
   equals its `combined-opinion` id `107729`, yet the real **lead opinion is `9423752`**). Always
   resolve the lead via `cluster.sub_opinions[]` + `opinion.type`; never assume equality.
2. **The `citation` search filter is FUZZY**, not exact (`citation="392 U.S. 1"` returned other
   cases). Hit an exact case by `case_name` + `court`, or verify via `analyze_citations`.
3. **Citation edges attach per-opinion and split across sub-opinions.** Terry cluster
   `citation_count = 37,943`, but `cites:(107729)` = 19,711 and `cites:(9423752)` = 2,967. A complete
   progeny pull ORs **all** `sibling_ids`.
4. **One logical case can have multiple clusters** (e.g., the cert/motions order). Disambiguate by
   citation + date + court.

## Identity verification (exact sequence)
1. `search(type="o", case_name="…", court="scotus")` → `cluster_id` + `sibling_ids[]`.
2. `get_endpoint_item(endpoint_id="clusters", item_id=<cluster_id>)` → `sub_opinions[]`.
3. Pick the lead: `opinion.type ∈ {020lead, 015unamimous, 010combined}` (the `search` `opinions[]`
   array already carries `type`).
4. Confirm identity: `search_document(opinion_id=<lead>, query="<party surname>")` — the text must
   name the parties. **Cluster confirmed only when** its `citations[]` has the expected
   reporter/volume/page **and** the lead/combined text names the parties.

## Per-data-element → exact CL source map (the schema)
| Data element | CL call → field | Notes |
|---|---|---|
| **IDENTITY** | | |
| Case name (short/canonical/full) | `clusters.case_name` / `case_name_short` / `case_name_full` | |
| Cluster id (case key) | search `cluster_id`; `clusters.id` | primary key |
| Lead opinion id | `clusters.sub_opinions[]` → `type ∈ {020lead,015unamimous,010combined}` | **≠ cluster_id** |
| All opinion ids | search `sibling_ids[]` | lead + concurrences + dissents |
| absolute_url | `clusters.absolute_url` (prefix `courtlistener.com`) | |
| **CITATIONS / PINPOINTS** | | |
| Official reporter cite | `clusters.citations[]` where `type=1` (`reporter="U.S."`/`F.3d`/`F.4th`) | volume+reporter+page |
| Parallel / Lexis / WL / neutral | `citations[].type` 1 / 6 / 7 / 8; search `lexisCite`, `neutralCite` | |
| Pinpoint page | star-pagination `*N` markers in `read_document` text; start = `citations[].page` | nearest preceding `*N` |
| Verbatim quote verify | `search_document(opinion_id, query)` → `position` + snippet | the fabrication test |
| **COURT / DATE / DISPOSITION** | | |
| Court | search `court_id` / `court_citation_string`; join `courts.citation_string` (Blue Book) | |
| Date decided/argued | `clusters.date_filed`; `other_dates`; `dockets.date_argued` | |
| Docket number | `dockets.docket_number` | |
| Disposition / posture / history | `clusters.disposition` / `posture` / `history` | **often empty** |
| Judges / author / per curiam | `clusters.judges`; `opinions.author_str`; `per_curiam` | author is per-opinion |
| Precedential status | `clusters.precedential_status`; search `status` | |
| SCOTUS vote data | `clusters.scdb_decision_direction`, `scdb_votes_majority/_minority` | |
| **PROGENY / CITING-REFS** | | |
| Later cases citing this | `search(type="o", q="cites:(<all sibling_ids OR'd>)")` → full metadata list | **recommended**; paginate |
| Raw edges + depth | `opinions-cited` → `citing_opinion`, `cited_opinion`, `depth` | depth = intensity, NOT polarity; counts unreliable |
| Outbound authorities | `opinions.opinions_cited[]` | what it relied on |
| Influence magnitude | `clusters.citation_count` | no polarity |
| **TREATMENT / GOOD-LAW** | | |
| Overruled/abrogated/negative | **NOT IN CL** → read progeny text for "overrul/abrogat" (`read_document`/`search_document`) **+ web search** | no Shepard's/KeyCite equivalent |
| **FULL TEXT / QUOTES** | | |
| Opinion text | `read_document(opinion_id)` → `html_with_citations` (opinions) / `plain_text` (RECAP) | 24h cache; chunkable |
| Fabrication cite check | `analyze_citations(text=…)` → FOUND/NOT FOUND + canonical name + cluster_id + parallels | **compare input name vs canonical yourself** — the auto name-mismatch warning is masked by cite dedup |
| **PROVENANCE** | | |
| Source lineage | `clusters.source`; `opinions.sha1` (empty = shell object), `extracted_by_ocr`, `download_url` | |
| Timestamps | `date_created`, `date_modified` | staleness |

## What CL does NOT give us (must come from opinion text + web)
- **Any good-law / treatment / negative-history signal** — derive it (progeny grep + web).
- **Depth-of-treatment polarity** — `opinions-cited.depth` is citation frequency, not "examined/discussed."
- **Reliable name-mismatch fabrication warning** — do the name comparison ourselves.

## Coverage gaps → how to read "not found"
Recent cases are indexed but often have **no official cite yet** (fall back to `case_name`+`docket`+`court`);
district/`F. Supp.` coverage is patchy; some cases carry only a vendor-neutral cite; duplicate/legacy/
corrupted objects exist. **"Not found" = recent / outside-coverage / wrong-cite — NEVER proof of
fabrication.** Cross-check by name+court+date and by web search before flagging.

## Rate envelope
Authenticated REST is **~1,000 req/hr with our token** (verified 2026-07-01; token stored out-of-repo at `~/.config/cssi/cl-token`, mode 600 — never committed). `analyze_citations` throttled tighter
(~**60/min**, 250 unique cites/job → `job_id` + `resume_citation_analysis`). Be economical: `search`
with `fields=` + `sibling_ids` gets a whole cluster in one call; `read_document` caches 24h.
