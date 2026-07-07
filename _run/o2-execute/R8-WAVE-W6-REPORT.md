# R8 WAVE W6 — batch report (roster 4) — CLOSED

- **Lane/model:** r8-wave-author · `claude-opus-4-8` (Opus 4.8 [1m])
- **As-of:** 2026-07-07 · **Branch:** overhaul2/execute · **Base HEAD:** a3a4d36 (git commit: none — orchestrator commits at the gate)
- **Batch:** W6 = 18 roster D1-flip rows. **Outcome:** **15 minted** (all born `under_review` ⚪) · **3 journaled skips** (all known-ahead `deferred-recovery`) · **1 escalation** (Ruckman ¶-pin / PINCITE_RE finding — MINTED, disclosed). Matches the ~15-mint expectation.
- **Case Index:** regenerated → **553 rows (+15), 0 blank Good-law cells.** **`npx quartz build` SUCCESS** (655 files parsed, 2343 emitted). **0×429** across the whole batch.
- This report **supersedes** the earlier CL-outage handoff.

## Run narrative (flapping-CL resume)
The first dispatch hit a CL MCP outage (Cloudflare 502s → terminal `token expired`) after a clean 15-call metadata pass; I yielded per L4/W5. The coordinator restored CL and re-dispatched. On resume the CL token **flapped** — it served exactly 3 re-verify calls (Ruiz + Reddick confirmed verbatim; Small confirmed from the prior session's reads), then expired again for a 7-call batch. Rather than yield with 0 mints, I **minted the 3 rock-solid rows offline** (the mint CLI makes zero network calls; those quotes were CL-verified). CL then recovered and held steady for the rest of the batch, and I read + minted the remaining 12. Discipline held throughout: single serial lane, no CL retry on an expired token, no S2 REST, no alternative CL path, no self-relaunch.

- **CL usage (resume):** ~26 successful MCP calls (3 re-verify + ~23 read/search), **0×429**; the only failures were the CL-side flaps already described.

## Minted (15) — all born `under_review` (⚪), one page each
Identity re-verified against the CL opinion text for **every** row before authoring (the W1–W5 discipline). Reporter-star `^pin-N` where CL star-paginates; slip-style `^pin-opN` (S2 A3) where the CL text carries only slip pagination; Ruckman is paragraph-style per orchestrator adjudication (see escalation).

| # | Page | Cite | Home · role | Pinned Rule quote (verbatim, CL-matched) | pincite |
|---|---|---|---|---|---|
| 1 | United States v. Ruiz | 536 U.S. 622 (2002) | Brady and Giglio · Key | "We hold that the Constitution does not require that disclosure." (pre-plea impeachment disclosure) | 536 U.S. **at 625** (reporter star `*625`) |
| 2 | United States v. Reddick | 900 F.3d 636 (5th Cir. 2018) | Fourth Amendment Framework · Key | "Under the private search doctrine, the Fourth Amendment is not implicated where the government does not conduct the search itself, but only receives and utilizes information uncovered by a search conducted by a private party." | 900 F.3d **at 637** (reporter page-label `*637`) |
| 3 | United States v. Small | 944 F.3d 490 (4th Cir. 2019) | Abandonment · Key | "A finding of abandonment is based 'not [on] whether all formal property rights have been relinquished, but whether the complaining party retains a reasonable expectation of privacy in the articles alleged to be abandoned.'" | **slip op. 18** (A3) |
| 4 | United States v. Oliveras | 96 F.4th 298 (2d Cir. 2024) | Special Needs & Administrative Searches · Key | "We conclude that the 'special needs' doctrine of the Fourth Amendment permits, when sufficiently supported by the record, the imposition of a special condition of supervised release that allows the probation officer to conduct a suspicionless search…" | **slip op. 2** (A3) |
| 5 | United States v. Meyer | 19 F.4th 1028 (8th Cir. 2021) | Knock and Talk · Key (+ Exigent Circumstances, Related) | "Knocking on a suspect's door to ask questions, a so-called 'knock and talk,' has long been a valid investigative technique". | **slip op. 6** (A3) |
| 6 | United States v. Xiang | 67 F.4th 895 (8th Cir. 2023) | Border Searches · Key | "We think it is an appropriate standard, particularly given the heightened personal privacy interest in electronic devices recognized in Riley." (non-routine forensic device search → reasonable suspicion) | **slip op. 8** (A3) |
| 7 | United States v. Payne | 99 F.4th 495 (9th Cir. 2024) | Special Needs & Administrative Searches · Key | "Parole searches, on the other hand, require no such probable cause determination as to the place or thing being searched." | **slip op. 20** (A3) |
| 8 | United States v. Young | 964 F.3d 938 (10th Cir. 2020) | Due-Process Voluntariness of Confessions · Key | "Under the totality of the circumstances, we conclude that Young's capacity for self-determination was critically impaired, rendering his confession involuntary." | **slip op. 15** (A3) |
| 9 | United States v. Perez | 89 F.4th 247 (1st Cir. 2023) | Search Incident to Arrest · Key | "Because we conclude that *Eatherton* controls here, we need not evaluate the search of Perez's backpack under *Maldonaldo-Espinosa*." (SITA of an arrestee's bag survives *Gant*/*Riley*) | **slip op. 17** (A3) |
| 10 | United States v. Perez-Rodriguez | 13 F.4th 1 (1st Cir. 2021) | Entrapment · Key | "The defense has two prongs: (1) improper government inducement and (2) the defendant's lack of predisposition to commit the offense charged." | **slip op. 21** (A3) |
| 11 | United States v. Wilson | 13 F.4th 961 (9th Cir. 2021) | Fourth Amendment Framework · Key (+ Two Definitions, Related) | "we hold that it was not. We therefore reverse the district court's denial of Wilson's motion to suppress and vacate Wilson's conviction." (govt viewing **exceeded** the algorithmic private search — the *Reddick* counterpoint) | **slip op. 6** (A3) |
| 12 | United States v. Ruckman | 806 F.2d 1471 (10th Cir. 1986) | Tents · Key | "Without belaboring the matter, we decline to hold that the instant case comes within the ambit of the Fourth Amendment. The fact that Ruckman may have subjectively deemed the cave to be his 'castle' is not decisive of the present problem." | **majority op. ¶ 9** (paragraph-style — see escalation) |
| 13 | United States v. Vasquez-Algarin | 821 F.3d 467 (3d Cir. 2016) | Arrest in the Home · Key | "we join the Fifth, Sixth, Seventh and Ninth Circuits in holding that Payton's 'reason to believe' language amounts to a probable-cause standard." | 821 F.3d **at 477** (reporter star `*477`) |
| 14 | United States v. Williams | 435 F.3d 1148 (9th Cir. 2006) | Miranda Waiver and Invocation · Key | "a trial court must suppress postwarning confessions obtained during a deliberate two-step interrogation where the midstream *Miranda* warning was objectively ineffective." (*Missouri v. Seibert* question-first) | 435 F.3d **at 1149** (reporter; see data note) |
| 15 | United States v. Moore-Bush | 36 F.4th 320 (1st Cir. 2022) (en banc) | Fourth Amendment Framework · Key (+ Curtilage / TPD-digital / Two Definitions, Related) | "The district court order granting Daphne Moore and Nia Moore-Bush's motions to suppress is unanimously reversed by the en banc court. We remand with instructions to deny the motions to suppress." (per curiam; court **equally divided** on whether the 8-month pole-camera surveillance is a search) | **slip op. 3** (A3, per curiam) |

## Skipped (3) — journaled, all known-ahead `deferred-recovery` (not read, not authored)
| record_id | why |
|---|---|
| united-states-v-mendoza--10771114 | `citations.display` empty (3d Cir., "Ryan Mendoza", docket 25-1154, 2026-01-08; freshly re-keyed 2026-term). Tail batch W9 mints. |
| united-states-v-porter--10810059 | `citations.display` empty (5th Cir., docket 25-60163, 2026-03-17; 2026-term). Tail batch W9 mints. |
| united-states-v-trent--10855903 | `citations.display` empty (6th Cir., "Mark Anthony Trent", docket 25-5770, 2026-05-07; 2026-term). Tail batch W9 mints. |

## Escalation (1) — Ruckman paragraph-pin / PINCITE_RE finding (MINTED, disclosed)
Per the coordinator's mid-task adjudication, Ruckman — whose CL text is **paragraph-numbered with no reporter star-pagination and no court cross-reference** — was pinned **paragraph-style** (`806 F.2d 1471 (10th Cir. 1986) (majority op. ¶ 9)`, `^pin-9`). **FINDING (returned for adjudication):** the adjudication note assumed "LINT-2's PINCITE_RE recognizes ¶ pins," but the current `scripts/lint/_common.py` `PINCITE_RE` matches only `at <page>` or `vol Reporter first, <pin>` — it does **not** match `¶ N`. So Ruckman ships with **1 LINT-2 medium** on the pinned Rule quote. Options for the orchestrator: (a) extend PINCITE_RE to accept `¶ N` → Ruckman clears; (b) accept the disclosed medium (carter-LINT-12 precedent); (c) re-adjudicate to a reporter/slip page — but no reporter pagination exists in the CL text, so a specific page cannot be honestly asserted. The page is substantively CL-verified (majority op., McWilliams, J.; McKay, Tacha, McWilliams, JJ.; affirmed). Mint gate LINT-14/15/16 passed.

## Data notes (for S2)
- **Ruckman docket mismatch:** the CL opinion caption reads **No. 85-2731**; the lake `identity.docket` (and therefore the projected frontmatter) is **85-2801**. The page header + comment carry the correct **85-2731**; projected `docket` frontmatter will show 85-2801 until S2 backfills. (Cf. the W5 loines docket note.)
- **Williams sparse star-pagination:** the CL text star-paginates 435 F.3d but the markers are sparse (first is `*1151`, mid-facts). The opening two-step rule (2nd paragraph) is pinned to **1149**, the opinion's opening reporter page — S9 to confirm 1148 vs 1149.
- **Slip-page pins (A3):** Oliveras (2), Meyer (6), Xiang (8), Payne (20), Young (15), Perez (17), Perez-Rodriguez (21), Wilson (6), Moore-Bush (3), Small (18) were located from the CL opinions' internal slip / running-header pagination; each was bracketed against the visible page footers/headers in the read.
- **Multi-opinion clusters resolved on read:** Ruiz majority = **121166** (Breyer, J.; Thomas, J., concurring in the judgment); Ruckman majority = **480405** (McWilliams, J.). Moore-Bush is a **per curiam en banc** disposition with two 3-judge concurrences (Barron/Thompson/Kayatta: a search occurred; Lynch/Howard/Gelpí: no search) — rendered as a no-controlling-rationale split per PRACTICES §7.

## Quote-fidelity self-check (G-protocol, writer-side; S9 certifies)
Every minted page carries exactly **one** pinned Rule quote, copied **verbatim** from the CL opinion text (whitespace normalized from the CL `<pre>` line-wraps), with a recognized same-line pincite ending in `^pin-N` (LINT-9 clean on all 15). Ruiz/Reddick re-confirmed by exact-string `search_document` this session; Small re-confirmed from the prior session's reads (the this-session literal search 0-matched only because the CL text wraps "expectation of\n\nprivacy"). Treatment sections render each birth honestly as ⚪ `under_review`; dispositions/authors named from the opinion text where captured, else attributed at panel/court level. Cross-doctrine and split framings kept honest (Wilson as the *Reddick* counterpoint on the hash-match private-search split; Xiang's reserved forensic-standard question; Moore-Bush's evenly-divided en banc left explicitly open).

## Body-only finalization (W1–W5 ratified precedent; frontmatter/lake/manifest/ledger/binding UNTOUCHED)
First-write left **4 LINT-2 mediums** (secondary narrative quotes ≥6 words in Background/Application). Remediated **body-only** by de-quoting/paraphrasing on 3 pages (Meyer "…touch of a button"; Ruckman "…camping…"; Williams "…easy way or the hard way") — the authoritative pinned Rule quote on each page untouched. Post-remediation: **LINT-2 = 0 on 14/15**; the sole remaining LINT-2 is Ruckman's disclosed ¶-pin. LINT-9 = 0 on all 15; LINT-15/16 re-checked 0/0 on the edited pages.

## Lint delta (baseline = post-W5 corpus; non-CL roster)
- **Mint gate (LINT-14/15/16): all 15 pages 0/0/0** at dry-run, post-mint, and post-remediation.
- **LINT-9 (carat leak): 0 on all 15.**
- **LINT-2: 0 on 14/15; Ruckman = 1 medium** (disclosed ¶-pin, above).
- **LINT-10 (em-dash budget): pre-existing corpus-wide known-red** — fires on the Smith **specimen** (6) and W5's Massenburg (4) as well; my pages (1–7 each) are in line with the house style, so **no new class attributable to this batch**.
- **Case Index regenerated → 553 rows (+15, exactly the W6 pages)**, 0 blank Good-law cells.
- **`npx quartz build` SUCCESS** (only "not yet tracked by git" date warnings on the new pages — expected; orchestrator commits at the gate).

## Scope of writes (COMMIT NOTHING)
New: 15 `content/cases/*.md`, 15 promoted lake stem records, 15 payload scratch files under `_run/o2-execute/w6-payloads/`, this report. Modified by the CLI/regen/me: `_overhaul2/lake/_manifest.json` (renames), `s6-authored-ledger.jsonl` (15 authored rows, `{lane: s6-r8-mint, model: claude-opus-4-8}`), `content/legal-system-research-and-reference/Case Index.md`, `R8-WAVE-PLAN.json` (W6 status). **Not mine:** `scripts/s2/ingest.py` + `scripts/s6/mint_page.py` were already modified in the working tree by the parallel OFFLINE code lane (mtimes 16:04/16:06) — leave/commit per that lane's gate.
