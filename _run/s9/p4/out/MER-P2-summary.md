# MER-P2 summary (S9 R11 Mermaid pass)

- **Lane:** MER-P2 · model `claude-opus-4-8`
- **Scope:** blocks MER-016 through MER-030 in `_run/s9/p4/mermaid-blocks.json`
- **Coverage:** 15 assigned / 15 examined / 0 skipped
- **Render:** 15/15 rendered ok (mmdc @ 1000px, white bg, pptr.json headless-shell)
- **Legible:** 15/15
- **Faithful:** 15/15 PASS · 0 FINDING
- **Findings file:** `_run/s9/p4/out/MER-P2-findings.jsonl` (empty — no candidates)
- **Verdicts:** `_run/s9/p4/out/MER-P2-verdicts.jsonl` (15 rows)

## Method
For each block: wrote body to `render/<id>.mmd`; rendered to `<id>.png`; visually Read the PNG; Read the host `.md` page (front-matter `[!rule]` callout + The Brief + Key/Related-case tables + the in-page ```mermaid``` fence). Compared every node, branch label, and case-at-node against the page's stated rule for (a) correct branch logic, (b) correct cases labeled at the right nodes, (c) no contradiction with the black-letter rule, (d) compact + legible. The rendered `.mmd` is byte-identical to the fence embedded in each page (generated from the same JSON body), so the check is diagram-logic-vs-doctrine, not fence-vs-render drift.

## Per-block result
| id | page | render | legible | faithful |
|---|---|---|---|---|
| MER-016 | searches/Aerial and Enhanced Surveillance | ok | yes | PASS |
| MER-017 | searches/Curtilage | ok | yes | PASS |
| MER-018 | searches/Electronic Surveillance and Title III | ok | yes | PASS |
| MER-019 | searches/Open Fields | ok | yes | PASS |
| MER-020 | searches/Plain View Doctrine | ok | yes | PASS |
| MER-021 | searches/Private and Foreign Searches | ok | yes | PASS |
| MER-022 | searches/Tents | ok | yes | PASS |
| MER-023 | .../Cell-Site Simulators | ok | yes | PASS |
| MER-024 | .../Investigative Genetic Genealogy | ok | yes | PASS |
| MER-025 | .../Real-Time Tracking | ok | yes | PASS |
| MER-026 | .../Reverse-Keyword and Geofence Warrants | ok | yes | PASS |
| MER-027 | .../Third-Party Doctrine and CSLI | ok | yes | PASS |
| MER-028 | two-definitions-of-search/Reasonable Expectation of Privacy | ok | yes | PASS |
| MER-029 | two-definitions-of-search/Trespass | ok | yes | PASS |
| MER-030 | seizures/Collective Knowledge and the Fellow-Officer Rule | ok | yes | PASS |

## Notes for the orchestrator (non-blocking, cosmetic — recorded, not filed as findings)
- **MER-020 (Plain View):** the diagram is the largest in the set (Horton 3-element chain + plain-feel branch); it renders tall and spread but each node text is legible at 1000px. No overlap or truncation. PASS.
- **MER-026 (Geofence):** decision node `B{Acquisition a search?}` has only a `Yes` exit. This is doctrinally correct, not a defect: the page states the search threshold is settled (Chatrie: acquisition IS a search), so a `No` branch would contradict the stated rule. PASS.
- **MER-030 (Collective Knowledge):** terminal-side node reads "Acting officer relies in objective good faith." The page's rule/brief phrase the acting officer's reliance as "objective reliance" (Hensley), reserving "good faith" for the Herring remedy strand. The wording is a loose synthesis but does NOT alter branch logic — the `Basis exists at the source? No -> Invalid seizure (Whiteley limit)` gate correctly makes source-basis the necessary condition, so good-faith reliance never cures a missing basis. Recorded as cosmetic; no candidate filed.

## Ambiguities requiring a ruling
None. All 15 diagrams are faithful to their host pages' stated rules.
