# B-PAIR summary — R6 contradiction-sweep pair list

**Packet:** B-PAIR (bootstrap, WS=PAIR) · **lane/model:** `claude-opus-4-8`
**Governing:** S9 §5 P4 R6 (contradiction sweep, 100% coverage of shared points).
**Write-scope honored:** only `_run/s9/p4/` written (`pair-list.json`, this summary).
**Outputs:** `_run/s9/p4/pair-list.json` (437 pairs), this file.

## Headline counts
| metric | value |
|---|---|
| registry points total | 80 |
| registry points multi-hosted (>1 hosting page) | 7 |
| cases total (`content/cases/*.md`) | 610 |
| cases multi-home (>1 resolved home) | 136 |
| **resulting unique page pairs** | **437** |

Pair breakdown: 1 registry-only · 432 shared-case-only · 4 mixed (registry + case on the same page pair).

## Method
1. **Registry** (`_overhaul2/points/registry.yaml`) parsed with
   `scripts/lint/_common.py::parse_yaml_subset` over the whole file (no frontmatter fences);
   80 `nodes[]` read for `id` / `home_page` / `also_on[]`. Hosting pages of a node =
   `[home_page] + also_on` (repo-relative content paths, already disk-resolving). Any node with
   >1 hosting page emits **all C(n,2)** host-page pairs (`why: also_on`). All 7 multi-hosted
   nodes have exactly 2 hosts → 1 pair each = 7 registry contributions.
2. **Cases** (`content/cases/*.md`) parsed with the same frontmatter parser; `homes[]` block
   read for `page` (wikilink) + `role`. Wikilinks resolved to repo-rel paths via a full
   `content/**/*.md` index (Quartz basename first, then frontmatter `title`/`topic`/`aliases`,
   stripping `#anchor` and `|display`). Distinct-home count drives multi-home selection.
3. **Dedupe:** pairs keyed on the unordered `frozenset({page_a, page_b})`; the **union of
   shared items** is preserved per pair in `shared_items[]` (each `{kind, id|case}`). `kind` is
   `mixed` when a pair carries both a registry point and a shared case; `why` concatenates
   (`also_on+multi-home`). `point_slug_or_case` is a representative (case preferred); full
   membership is in `shared_items`.

## Coverage ledger (deterministic)
- **Assigned:** 80 registry points + 610 case files = 690 source records.
- **Examined:** 690/690. Registry: 80 nodes read (7 multi-hosted). Cases: 610 read
  (609 have a `homes:` block; 1 has none — `content/cases/index.md`, the case-index landing).
- **Skipped (with reason):** 73 registry nodes (single hosting page → no pair, per R6);
  474 case files (473 single-home + 1 no-home → not multi-homed, out of R6 scope). Zero silent
  drops.
- **Resolution health:** unresolved case-home wikilinks = **0/305** home entries. Every
  `[[…]]` resolved to an on-disk content page.

## Contribution → dedup reconciliation (audit)
- Registry: 7 host-pair contributions → 5 distinct page pairs carry a registry point
  (1 registry-only + 4 mixed); 2 registry contributions coincided with an existing pair
  (PAIR-0387 and PAIR-0397 each carry **two** registry points on one host pair).
- Cases: 208 home×home + 305 case-anchor = 513 contributions. Per multi-home distribution
  (108×2-home, 24×3-home, 3×4-home, 1×5-home): ΣC(n,2)=208 and Σn=305 — exact, confirming
  every case's home entries resolved 1:1 to distinct pages (no intra-case home collision).
- 513 case + 7 registry = 520 raw contributions → **437 unique pairs** after dedupe.

## Generation-rule note for the orchestrator (adjudicable)
The R6 rule text — "every case with >1 home contributes its **home-page pairs** (case page
itself is the canonical record, include it as **page_a** for treatment-identity checks)" — is
read here as the **superset** to guarantee 100% coverage:
- **Case-anchored pairs** — `page_a = content/cases/<case>.md`, `page_b = each home` (the
  treatment-identity checks; canonical record vs each doctrine-page treatment). 305 contributions.
- **Home×home pairs** — `C(n,2)` among the resolved homes (direct doctrine-vs-doctrine
  contradiction, in case the canonical case page is a stub/silent on a sub-point). 208 contributions.
Both carry `why: multi-home`. If the orchestrator prefers the narrower reading (case-anchor
only), drop the 208 home×home-derived pairs — they are identifiable as `shared-case`/`mixed`
pairs whose `page_a` is **not** under `content/cases/` (or, for mixed, whose case items came
only via a home×home contribution). Chosen the superset because under-coverage is a packet
failure and the parenthetical reads as an addition on top of the home-page pairs.

## Notes / flags
- **Basename collision:** only `index` is ambiguous (25 `index.md` files). Zero case homes
  link to bare `[[index]]`; every index.md home (e.g. `[[The Exclusionary Rule]]`) resolved
  uniquely via frontmatter `title`/`topic`, not the bare basename. No mis-resolution.
- **Mixed pairs (4):** PAIR-0387 (Traffic Stops ↔ Checkpoints and Roadblocks; 2 checkpoint
  points + Delaware v. Prouse), PAIR-0397 (Arrest in the Home ↔ Entry to Arrest; 2 points +
  8 cases incl. Payton/Steagald/Harris), PAIR-0425 (Searching Effects and Containers ↔
  Automobile Exception; `search.effects.containers` + Acevedo/Chadwick/Ross), PAIR-0427
  (Destruction of Evidence ↔ Exigent Circumstances and Hot Pursuit; `search.home.exigency.destruction`
  + Kentucky v. King). These are high-value contradiction targets (a point and its cases share
  the exact page pair) and should sweep first.
- This is a bootstrap artifact (pair enumeration only) — **no verdicts, no candidate findings**.
  The per-pair contradiction sweep (`out/PAIR-*-findings.jsonl`) is a downstream lane.
