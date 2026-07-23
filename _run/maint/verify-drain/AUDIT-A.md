# MAINT-1 verify-drain audit A

Audit date: 2026-07-23  
Lane: CSSI builder, `s2-builder-codex-rest`  
Command: `python3 scripts/maint/verify_drain.py`

The drain completed cleanly on its first invocation:
`DONE: examined=196 fetches=223 promoted=142 slip_eligible=16`.
No retry was needed. This audit was read-only except for creation of this file.

## Disposition counts

| Disposition | Count |
|---|---:|
| `promoted_verified` | 142 |
| `not_promoted` | 36 |
| `slip_eligible` | 16 |
| `slip_party_leg_failed` | 0 |
| `cite_appeared` | 0 |
| `error` | 2 |
| **Total** | **196** |

The 36 `not_promoted` rows consist of 31 party-leg failures and 5
official-citation-leg failures. One of the 31 party-leg failures has only 94
characters of cached opinion text. The two errors are fetch/transport errors.

## Promoted-record spot checks

Ten `promoted_verified` rows were selected across the record-name alphabet
(A, C, E, G, K, M, P, S, W, and Z). For each row, the cache file named from
the lake record's `identity.lead_opinion_id` was opened and checked. Every
ledger `party_evidence.matched` phrase/token was genuinely present in that
cached text. Every lake record had `status: verified`,
`identity.party_name_in_text: true`,
`identity.expected_citation_found: true`, and a provenance warning naming the
2026-07-23 MAINT-1 promotion.

| Record | Lead opinion / claimed matches | Text check | Lake check | Verdict |
|---|---|---|---|---|
| A Quantity of Copies of Books v. Kansas | 9422858; token `books`, phrase `Kansas` | Both present | `verified`; true/true; warning present | PASS |
| California v. Prysock | 9428478; phrases `California`, `Prysock` | Both present | `verified`; true/true; warning present | PASS |
| Egbert v. Boule | 6347905; phrases `Egbert`, `Boule` | Both present | `verified`; true/true; warning present | PASS |
| Gonzalez v. Trevino | 11066659; phrases `Gonzalez`, `Trevino` | Both present | `verified`; true/true; warning present | PASS |
| Kansas v. Ventris | 145880; phrases `Kansas`, `Ventris` | Both present | `verified`; true/true; warning present | PASS |
| McDonough v. Smith | 9226046; phrases `McDonough`, `Smith` | Both present | `verified`; true/true; warning present | PASS |
| Perttu v. Richards | 11243419; phrases `Perttu`, `Richards` | Both present | `verified`; true/true; warning present | PASS |
| Stone v. Powell | 9426587; phrases `Stone`, `Powell` | Both present | `verified`; true/true; warning present | PASS |
| Weatherford v. Bursey | 9426656; phrases `Weatherford`, `Bursey` | Both present | `verified`; true/true; warning present | PASS |
| Ziglar v. Abbasi | 4181057; phrases `Ziglar`, `Abbasi` | Both present | `verified`; true/true; warning present | PASS |

**Promoted spot-check result: 10/10 passed; no mismatch found.**

## Slip-eligible spot checks

Three `slip_eligible` rows were checked against the lead-opinion cache in the
same manner. All claimed party matches were genuinely present. Each cached
cluster had zero citations and therefore zero official-class citations; the
lake `citations.official` value was null. As expected for the non-applying
verify-drain invocation, these lake records remain `under_review` with the two
identity-leg flags false and have no MAINT-1 promotion warning.

| Record | Lead opinion / claimed matches | Text check | Citation/lake check | Verdict |
|---|---|---|---|---|
| Carter v. United States | 11129122; phrases `Carter`, `United States` | Both present | 0 cluster citations; official null; `under_review` | PASS |
| Robinson v. Commonwealth | 11306090; phrases `Eddie Eugene Robinson`, `Commonwealth of Virginia` | Both present | 0 cluster citations; official null; `under_review` | PASS |
| United States v. Trent | 11323299; phrases `United States`, `Mark Anthony Trent` | Both present | 0 cluster citations; official null; `under_review` | PASS |

**Slip spot-check result: 3/3 passed; no mismatch found.**

## Cause classification for every `not_promoted` and `error` row

- **Alasaad v. Wolf** — official citation tuple `988 F.3d 8` is absent from the cached cluster citations; the party leg passed.
- **Arkansas v. Sanders** — selected party token `sanders` (side `Sanders`) is absent from the cached opinion text (26,438 chars).
- **Beecher v. Alabama** — selected party token `beecher` (side `Beecher`) is absent from the cached opinion text (6,462 chars).
- **Berkemer v. McCarty** — selected party token `berkemer` (side `Berkemer`) is absent from the cached opinion text (49,809 chars).
- **Brown v. Mississippi** — selected party token `mississippi` (side `Mississippi`) is absent from the cached opinion text (17,267 chars).
- **Brown v. Texas** — selected party token `brown` (side `Brown`) is absent from the cached opinion text (12,411 chars).
- **Camara v. Municipal Court** — selected party token `camara` (side `Camara`) is absent from the cached opinion text (31,222 chars).
- **Carroll v. Carman** — official citation tuple `574 U.S. 13` is absent from the cached cluster citations; the party leg passed.
- **Davis v. United States** — selected party token `davis` (side `Davis`) is absent from the cached opinion text (17,779 chars).
- **Donovan v. Dewey** — selected party token `donovan` (side `Donovan`) is absent from the cached opinion text (23,336 chars).
- **Flippo v. West Virginia** — selected party token `flippo` (side `Flippo`) is absent from the cached opinion text (7,193 chars).
- **Frazier v. Cupp** — selected party tokens `frazier` and `cupp` are both absent from the cached opinion text (15,605 chars).
- **Go-Bart Importing Co. v. United States** — selected party token `importing` (side `Go-Bart Importing Co.`) is absent from the cached opinion text (20,719 chars).
- **Heller v. New York** — selected party token `heller` (side `Heller`) is absent from the cached opinion text (19,531 chars).
- **Horton v. California** — selected party token `horton` (side `Horton`) is absent from the cached opinion text (26,000 chars).
- **Jimerson v. Lewis** — official citation tuple `94 F.4th 423` is absent from the cached cluster citations; the party leg passed.
- **Knight v. Jacobson** — selected token `individual` from the side `Jacobson, Officer, Badge 3359, Individual` is absent from the cached opinion text (17,085 chars).
- **Kolender v. Lawson** — selected party token `kolender` (side `Kolender`) is absent from the cached opinion text (20,181 chars).
- **Kuhlmann v. Wilson** — selected party token `kuhlmann` (side `Kuhlmann`) is absent from the cached opinion text (49,784 chars).
- **LaChance v. Erickson** — selected party token `lachance` (side `LaChance`) is absent from the cached opinion text (8,296 chars).
- **LaDuke v. Nelson** — selected token `etc` from the side `Alan C. Nelson, Etc.` is absent from the cached opinion text (53,580 chars).
- **Marbury v. Madison** — selected party token `madison` (side `Madison`) is absent from the cached opinion text (54,308 chars).
- **Marcus v. Search Warrant** — selected party token `marcus` (side `Marcus`) is absent from the cached opinion text (41,854 chars).
- **Mathis v. United States (1968)** — selected party token `mathis` (side `Mathis`) is absent from the cached opinion text (6,599 chars).
- **Mooney v. Holohan** — selected party token `holohan` (side `Holohan`) is absent from the cached opinion text (11,933 chars).
- **People v. Frederick** — official citation tuple `500 Mich. 228` is absent from the cached cluster citations; the party leg passed.
- **Robbins v. California** — selected party token `robbins` (side `Robbins`) is absent from the cached opinion text (14,863 chars).
- **Sorrells v. United States** — selected party token `sorrells` (side `Sorrells`) is absent from the cached opinion text (42,321 chars).
- **South Dakota v. Neville** — selected party token `neville` (side `Neville`) is absent from the cached opinion text (27,832 chars).
- **State v. Demesme** — cached opinion text is tiny (94 chars); selected party tokens `state` and `demesme` are absent.
- **State v. Larson** — selected party token `larson` (side `Larson`) is absent from the cached opinion text (15,410 chars).
- **State v. Volle** — slip-phase fetch failed with `HTTP Error 502: Bad Gateway`.
- **United States v. Anchondo** — selected party token `anchondo` (side `Erick Anchondo`) is absent from the cached opinion text (6,415 chars).
- **United States v. Kolsuz** — official citation tuple `890 F.3d 133` is absent from the cached cluster citations; the party leg passed.
- **United States v. Payne** — drain-phase fetch failed with `<urlopen error [Errno 54] Connection reset by peer>`.
- **United States v. Perez-Rodriguez** — selected party token `perez-rodriguez` (side `Perez-Rodriguez`) is absent from the cached opinion text (100,452 chars).
- **Weeks v. United States** — selected party token `weeks` (side `Weeks`) is absent from the cached opinion text (25,208 chars).
- **illinois-v-fisher--5141053** — selected party token `fisher` (side `Fisher`) is absent from the cached opinion text (9,129 chars).

Independent re-checking of the cached opinion and cluster data found no
ledger-evidence mismatch in these 38 rows.

## Recommended follow-ups

1. Route the 31 party-leg failures for residue review, keeping the 94-character
   **State v. Demesme** cache result visibly separate from the 30 normal-length
   text results.
2. Route the five records whose expected official citation tuple was absent
   from the cached CourtListener cluster citations for citation-source review:
   **Alasaad v. Wolf**, **Carroll v. Carman**, **Jimerson v. Lewis**,
   **People v. Frederick**, and **United States v. Kolsuz**.
3. Retry or otherwise resolve the two transient fetch failures:
   **State v. Volle** (HTTP 502) and **United States v. Payne** (connection
   reset). They have ledger rows already, so any retry procedure should account
   for the ledger's resumable-key behavior.
4. During residue review, inspect caption-token selection in the rows where
   the selected terminal token is descriptive rather than a party surname:
   **Knight v. Jacobson** (`individual`), **LaDuke v. Nelson** (`etc`), and
   **Go-Bart Importing Co. v. United States** (`importing`).

No residue adjudication is made in this audit.
