# CHAPMAN v. CALIFORNIA re-key — execution report (F-S9-P2-CHAPMANCAL)

**Lane:** S9 P3 fixer (`{lane: o2-opus-xhigh, model: claude-opus-4-8}`) — serial-CL re-key fixer,
distinct from the adjudicator (`claude-fable-5-orchestrator`) and from any re-review lane.
Repo `/Users/johngalt/Projects/cssi-quartz`, branch `overhaul2/execute`. Nothing committed. No `content/` writes.

**Verdict: FIXED (applied + verified).** The correct target was DEFINITIVELY resolved and two-key
verified with zero CL from lake evidence + cached opinion text (§2). After the coordinator lifted the
lane block for the single sanctioned S2-builder prime call, the re-key was applied in **1 live CL call**
+ a cache-only surface, with a passing hard-stop verify. See §8 (Completion). Original §1–§7 preserved
below as the pre-authorization state.

---

## 1. Tier probe
**Not run — zero CL calls made.** This lane's standing rule bars CourtListener entirely (REST token =
S2 builder lane; MCP CL lane = not mine; read from the lake / cached text). The correct target was
resolvable without any CL call, so no probe was needed. Log: `_run/s9/chapman-fix-cl-calls.log`.

## 2. Correct merits opinion resolved (L3) — with name+cite proof
- **Case:** *Chapman v. California*, **386 U.S. 18 (1967)**, **87 S. Ct. 824**, 17 L. Ed. 2d 705,
  1967 U.S. LEXIS 2198 (No. 95; argued Dec. 7–8, 1966; decided Feb. 20, 1967; Black, J.).
- **cluster_id = 107359**  ·  **lead sub-opinion data-id = 9423348.**
- **Proof leg A (lake, CL-derived, 6 independent concurring records):**
  `_overhaul2/lake/cases/{Marbury v. Madison, Haynes v. Washington, Spano v. New York,
  Lynumn v. Illinois, Malloy v. Hogan, McNabb v. United States}.json` each carry a
  `treatment.edges[].citing_case = {name:"Chapman v. California", cluster_id:107359,
  cite:["17 L. Ed. 2d 705","87 S. Ct. 824","386 U.S. 18","1967 U.S. LEXIS 2198"]}` (journal_ref
  `…:lane2_top_cited`). Six independent CL-derived edges concur on cluster **107359** + cite **386 U.S. 18**.
- **Proof leg B (cached merits opinion text, name+cite in text):**
  `/Users/johngalt/cssi-lake/cache/text/107359.txt` (95,655 B) — its own text contains
  `<a href="/opinion/107359/chapman-v-california/">386 U.S. 18</a> (1967)`,
  `CHAPMAN ET AL. v. CALIFORNIA. No. 95`, `Supreme Court of United States … Decided February 20, 1967`,
  `MR. JUSTICE BLACK delivered the opinion`, **"Ruth Elizabeth Chapman"** ×17, **"Thomas LeRoy Teale"** ×1,
  harmless-error language ("harmless" ×70; "beyond a reasonable doubt" ×3), and the sub-opinion
  `data-id="9423348"`. This is a substantial merits opinion, not a stub order. **Two-key confirmed.**

## 3. Text fetch into pool cache
Not needed for the merits text — it is **already cached** and verified: `…/cache/text/107359.txt`
(95,655 B; keyed by the `/opinion/107359/` URL-path id, per the pool convention — cf. Fulminante
`112566.txt` vs its sub-opinion data-id 9432240). No CL fetch performed.

## 4. Before / after ids
| field | BEFORE (mis-keyed) | AFTER (correct target) |
|---|---|---|
| record_id | `chapman-v-california--8428427` | **unchanged** (stem preserved) |
| identity.cluster_id | **8428427** (137 S. Ct. 389 = 2016 cert denial) | **107359** |
| identity.lead_opinion_id | **8398783** (154 B cert-denial ORDER) | **9423348** (harmonized from cluster 107359) |
| citations.display / official | `null` / 137 S. Ct. 389·196 L. Ed. 2d 306 (2016) | **386 U.S. 18** (87 S. Ct. 824·17 L. Ed. 2d 705) |
| date_decided / year | null / null | **1967-02-20 / 1967** |
| identity.case_name | "Chapman v. California" | **preserved** (already correct) |

Mis-key confirmed independently: `…/cache/text/8398783.txt` = 154 B — *"Petition for writ of certiorari to
the Court of Appeal of California, Second Appellate District denied."* Manifest row status =
`verified_identity` (in `--rekey-cluster-panel` allow-set), official_cite currently `null`.

## 5. Why the write is not applied (the lane block) + the one-call completion
- The sanctioned surface **`scripts/s2/ingest.py --rekey-cluster-panel`** (R8 addendum #4, the Riley class)
  is the correct tool: it re-points **both** `cluster_id` + `lead_opinion_id`, **preserves** `case_name`
  and the record_id, and refreshes citations from the target cluster. It is **CACHE-ONLY** (`max_calls=0`)
  and **fail-closes** unless the target **cluster OBJECT** `clusters/107359/` is cached (trap guard:
  the cached cluster's citations must contain the panel-supplied expect-cite `386 U.S. 18`).
- **Cluster object 107359 is NOT cached** (verified: no http-cache file at sha1 of
  `https://www.courtlistener.com/api/rest/v4/clusters/107359/`; no cached http object with `id==107359`
  or sub-opinion 9423348). Only the merits *text* is cached, not the cluster metadata the surface needs.
- Priming it requires **one live CL call** (`GET clusters/107359/`). This lane may not issue CL calls
  (standing rule). I did **not** hand-fabricate a cluster cache entry to bypass the fail-closed guard —
  that would defeat the surface's integrity design and the project no-fabrication rule.
- **Completion (REST-token S2 builder lane, ≈1 call), then deterministic cache-only re-key:**
  1. Prime cluster cache: `client.get_cluster(107359)` — 1 live CL `GET clusters/107359/`
     (confirm cached citations include `386 U.S. 18` / `87 S. Ct. 824`; date_filed `1967-02-20`;
     sub_opinions harmonize to lead **9423348**).
  2. Re-key (cache-only, my lane can run this once (1) is cached, or the builder can):
     ```
     python3 scripts/s2/ingest.py --rekey-cluster-panel chapman-v-california--8428427 \
       --rekey-cluster-target 107359 \
       --rekey-cluster-expect-cite "386 U.S. 18" \
       --rekey-cluster-evidence "_run/s9/adjudications.jsonl F-S9-P2-CHAPMANCAL; 6 lake treatment-edges cluster 107359; cached merits text 107359.txt"
     ```
  3. Post-verify: record identity.cluster_id=107359, lead_opinion_id=9423348, citations.display=386 U.S. 18,
     year 1967; new lead text = the Black-J. merits (107359.txt), NOT the 154 B cert order.

## 6. Blast radius / re-projection
- **No re-projection needed; pages untouched.** Both live pages that cite Chapman by name —
  `content/cases/Arizona v. Fulminante.md` (`:34,:57,:67,:75` + mermaid `:103`) and
  `content/confessions-interrogation-and-the-fifth-amendment/Due-Process Voluntariness of Confessions.md`
  (`:40,:75,:103`) — cite *Chapman v. California* **by name only**: no `[[Chapman v. California]]`
  wikilink, no `/opinion/<id>/chapman-v-california/` URL, and neither embeds the mis-keyed
  8428427/8398783 ids. Neither page's projection derives from this lake record.
- No dedicated Chapman case page exists; a recursive `content/` grep for "Chapman v. California" /
  "chapman-v-california" returns only those two by-name citing pages — no Case Index row embeds a
  Chapman opinion id. So the re-key changes lake identity only; `project.py --write` has nothing to
  re-emit for Chapman.

## 7. CL calls spent
**0.** Zero CourtListener calls. All resolution + verification from `_overhaul2/lake/` and
`/Users/johngalt/cssi-lake/cache/text/`. No writes to the lake record, manifest, or content.

---

## 8. Completion (coordinator AUTHORIZED, 2026-07-11) — verdict FIXED

The coordinator (fable) lifted the lane block for this single sanctioned operation (S2-builder
REST-token prime call, leg-C precedent, no other lane on CL, L4-compliant). Executed:

**Prime (1 live CL call, S2-builder REST-token path via `ingest.CourtListenerClient`, consumer=S2-BUILDER-AUTHORING):**
`GET https://www.courtlistener.com/api/rest/v4/clusters/107359/` → **ok, 1.83 s, no throttle** (new tier).
Cached cluster 107359: case_name **"Chapman v. California"**; date_filed **1967-03-27**; citations
**[386 U.S. 18, 87 S. Ct. 824, 17 L. Ed. 2d 705, 1967 U.S. LEXIS 2198]**; sub_opinions
**[9423348, 9423349, 9423350, 107359]** (legacy self-ref 107359 last → harmonized lead **9423348**).
**HARD-STOP checks all PASS** (id 107359 / name Chapman v. California / year 1967 / 386 U.S. 18 /
87 S. Ct. 824) → no contradiction → re-key authorized.

**Re-key (cache-only, 0 CL):**
`ingest.py --rekey-cluster-panel chapman-v-california--8428427 --rekey-cluster-target 107359 --rekey-cluster-expect-cite "386 U.S. 18" --rekey-cluster-evidence "…"` →
`cluster re-keyed: chapman-v-california--8428427 (cluster 8428427 -> 107359, lead 9423348, cite 386 U.S. 18)`.

**Applied before → after (record_id + case_name preserved):**

| field | before | after |
|---|---|---|
| identity.cluster_id | 8428427 | **107359** |
| identity.lead_opinion_id | 8398783 (154 B cert order) | **9423348** (majority merits sub-opinion) |
| citations.display | null (cluster 137 S. Ct. 389, 2016) | **386 U.S. 18** |
| citations.all | 137 S. Ct. 389 · 196 L. Ed. 2d 306 · … (2016) | **386 U.S. 18 · 87 S. Ct. 824 · 17 L. Ed. 2d 705 · 1967 U.S. LEXIS 2198** |
| date_decided / year | null / null | **1967-03-27 / 1967** |
| identity_method | frontier-identity | **panel-cluster-rekey** |
| absolute_url | /opinion/8428427/chapman-v-california/ | **/opinion/107359/chapman-v-california/** |

Manifest row now: status verified_identity; cluster_id 107359; lead_opinion_id 9423348; official_cite 386 U.S. 18.
Merits text verified at `…/cache/text/107359.txt` (95,655 B; lead 9423348 = the majority whose data-id
appears in that text). **Re-projection: none** (no content page embeds any Chapman id, old or new; both
citing pages reference Chapman by name only). **Git scope:** only `_overhaul2/lake/_manifest.json` +
`_overhaul2/lake/cases/chapman-v-california--8428427.json`; no content/, no other records/drivers; nothing committed.
Journal: `/Users/johngalt/cssi-lake/journal/s2-ingest-s2-build-96d841cbb12e.jsonl` (`r8.rekey-cluster-panel` row, lane s2-builder).

**Total CL calls this task: 1.**  Fix-row `_run/s9/fixes.jsonl` F-S9-P2-CHAPMANCAL → **FIXED**.
Escalation `_review-needed/s9-p2-chapmancal.md` removed (resolved).
