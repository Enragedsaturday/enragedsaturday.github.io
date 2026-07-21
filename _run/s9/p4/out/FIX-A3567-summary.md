# FIX-A3567 summary

Packet: FIX-A3567 (WRITE-SCOPE fix packet). Lane `FIX-A3567`, model `claude-opus-4-8`.
Triage rows applied: A3, A5, A6, A7. All evidence from lake + `~/cssi-lake/cache/text` (no CL calls).

## Coverage
- Items assigned: 4 (A3, A5, A6[=7 S8H-B fragment/pin rows], A7).
- Fix rows emitted: 10 (A3=1, A5=1, A6=7, A7=1) — all **FIXED**, none NOT-FIXED, no `needs_cl`.
- Every lake edit cache-verified with byte offsets (see fixes.jsonl `evidence`).

## Files written (WRITE-SCOPE only)
- `content/searches/the-third-party-doctrine-and-digital-surveillance/Reverse-Keyword and Geofence Warrants.md` (A3)
- `content/seizures/Seizure of the Person.md` (A7)
- `_overhaul2/lake/cases/united-states-v-holcomb--10670143.json` (A5)
- `_overhaul2/lake/cases/Florida v. Jardines.json` (A6: pin-9 fix + new pin-8, pin-9b)
- `_overhaul2/lake/cases/Kentucky v. King.json` (A6: new pin-op8b)
- `_overhaul2/lake/cases/United States v. Walker.json` (A6: pin-1364 fix)
- `_overhaul2/lake/cases/United States v. Cano.json` (A6: pin-op29 note)
- `_run/s9/p4/out/FIX-A3567-fixes.jsonl`, `_run/s9/p4/out/FIX-A3567-summary.md`

## Per-item

### A3 — geofence Smith mislink retarget  ⚠ COUNT DISCREPANCY (orchestrator attention)
- Convention decision tree: `content/cases/United States v. Smith (2024).md` **exists** → wikilink it (not the plain-italic/LINT-17 brief-mention fallback). Target `[[United States v. Smith (2024)|Smith]]` matches the page's own pre-existing correct link (line 38) and frontmatter `related`.
- **Adjudication A3 said "x3"; the current page has 9 instances** of the defect (piped `[[Smith v. Maryland|Smith]]` whose prose means the 5th Cir. geofence case). The stale `~line 361/363/372` refs predate the page's expansion (Brief / Common pitfalls / Lower-court developments / synthesis / tables). All 9 retargeted (8 literal-pipe via replace_all: lines 36,38×2,40,47,53,54,62; 1 escaped-pipe table cell: line 77).
- Genuine pen-register `Smith v. Maryland` (442 U.S. 735) **untouched**: line 76 table `[[Smith v. Maryland]]`, line 101 sources `*Smith v. Maryland*`. Post-edit grep: 0 residual piped mislinks. Surrounding prose unchanged; N7 respected.

### A5 — Holcomb superseding opinion
- Appended to `slip_only_provenance.note` (with `as_of 2026-07-20`): the 2026-07-17 superseding PUBLISHED opinion (docket 23-469, CL cluster 10932458, opinion 11400001, text not yet extracted on CL → still cite-less) supersedes the "no superseding published cite exists now" claim.
- `status` (`verified_identity`) and `treatment` (`field_i_validity: unverified`, `stub: true`) **unchanged** — still a frontier stub. Record-level `slip_only_provenance.as_of` (2026-07-07) left as the original slip-stamp date; the new date is embedded in the appended note per instruction.

### A6 — 7 fragment/pin rows (all lake-side; content not in write scope)
1–2. **Jardines pin-9** (`There is no customary invitation to do that`): cache 856347.txt @16395 is verbatim except a line-break hyphenation (`invita-`+`tion`). Documented in `notes`, flipped `quote_fidelity` mismatch→matched, `position`=16395. Page (9) was right; prior mismatch = de-hyphenation false-negative.
3. **Cano** (`pin-op29`): note added recording that the page/absolute_url use cluster id 4649091 but the quote lives only in lead 4426344 (present in 4426344.txt @~49681; absent from 4649091.txt). No page/quote edit.
4. **Walker pin-1364** (`did not exceed the geographic limit...`): cache 2844024.txt @7835 supports the quote (verbatim modulo curly→straight quotes + line-wrap + dropped leading "Second,"). Fixed: mismatch→matched, position=7835, `notes`. pin-1363/pin-1364a (also mismatch, **not named** in packet) left untouched.
5. **Jardines pin-8 (new)**: `approach the home by the front path` — byte-exact in 856347.txt @14872 (569 U.S. at 8). Added, matched, slip-only.
6. **Jardines pin-9b (new)**: `limited not only to a particular area but also to a specific purpose` — cache 856347.txt @16904 (569 U.S. at 9) modulo one `area`/`but` line break. Added, matched, slip-only. **Content-anchor desync reported**: Knock and Talk.md line 19 reuses wiki block `#^pin-9` for this distinct (but adjacent page-9) quote; content left unchanged (out of write scope).
7. **King pin-op8b (new)**: `the occupant has no obligation to open the door or to speak.` — cache 216733.txt @39895 (563 U.S. at 469) modulo one `no`/`obligation` line break; fragment is a substring. Added, matched, slip-only. Text is in 216733.txt (= content URL /opinion/216733/); record `lead_opinion_id` 9441559 cache lacks it (noted).

### A7 — Taylor v. Alabama pincite
- `Seizure of the Person.md` line 164: `217–218` → `690, 691, 692–693`. `217-218` is impossible for 457 U.S. 687 (out of range; not a parallel-reporter page). Cache 110760.txt confirms: pin-690b @9078 (star page 690), pin-691 @10556 (page 691); star markers *688–*699 present. Corrected value mirrors the canonical case page (`content/cases/Taylor v. Alabama.md` line 76: "690, 691, 692–693").
- **Mirrored lake pin**: none carried `217-218`; lake pins pin-690/pin-690b/pin-691 already cache-consistent at 690/691 → no Taylor lake edit needed.

## Notes for orchestrator / re-review (writer ≠ checker)
- **A3 count 9 vs adjudicated 3** — scope expansion of the fix vs the triage figure; called out above and in the A3 fix row (`count_discrepancy`). All 9 are the same adjudicated defect class; flagging in case the orchestrator wants to reconcile the finding count.
- **A6 pin-9 & pin-1364 fidelity flips** (mismatch→matched) and **new pins pin-8/pin-9b/pin-op8b/pin-op8b** are cache-verified but rely on whole-corpus de-hyphenation/quote-normalization, consistent with prior-phase pin conventions; a non-author re-reviewer should confirm against the cited offsets.
- **A6 content-side items not edited** (out of write scope, reported only): Knock and Talk.md line-19 `#^pin-9` anchor reuse (row 6); Cano.md cluster-id fragment URL (row 3). No content-page edits were made for A6.
- JSON re-validated: all five edited lake records parse; new pin ids — Jardines [pin-6,pin-9,pin-8,pin-9b], King [pin-op8,pin-op8b], Walker [pin-1363,pin-1364(matched),pin-1364a].
