# I4-TRIAGE summary (WS=I4; findings/dispositions only, NO content edits)

Packet: I4-TRIAGE. Lane/model: `claude-opus-4-8`. WRITE-SCOPE: `_run/s9/p4/` only.
Task: JOIN absence-claims × web-direction × CL-direction per `claim_id`, read each claim's
page context, disposition all 181.

## Coverage (deterministic)
- Items assigned: **181** (`_run/s9/p4/absence-claims.jsonl`).
- Items examined: **181/181**. Every `claim_id` joined across all three inputs.
- Items skipped: **0**.
- JOIN integrity: absence=181, CL=181, web=181 (web files carry 60+60+61 objects; `wc -l`
  undercounts the no-trailing-newline last line). Union = 181; 0 missing, 0 duplicate, 0 extra.
- web verdict distribution as received: HOLDS 154, MOVED 27, UNCERTAIN 0.

## Disposition counts (181 total)
| Disposition | Count |
|---|---|
| CONFIRMED-HOLDS | 154 |
| CORPUS-ALREADY-CURRENT | 27 |
| MOVED-NEEDS-FIX | 0 |
| UNCERTAIN-WATCH | 0 |

Outputs:
- `_run/s9/p4/out/I4-TRIAGE-dispositions.jsonl` — 181 rows `{claim_id, disposition, basis, movers-cited}`.
- `_run/s9/p4/out/I4-TRIAGE-findings.jsonl` — 2 `p4.candidate.v1` rows (both enrichment, `needs_cl`, low severity).
- `_run/s9/p4/out/I4-TRIAGE-watch.jsonl` — 3 R12 watch additions.

## MOVED-NEEDS-FIX list
**None.** All 27 web-MOVED verdicts resolve to CORPUS-ALREADY-CURRENT on individual review
with page context. This matches the B6 triage prediction ("most MOVED = corpus-already-current
(resolved-reserved-question class); real movers adjudicated individually"). No absence claim as
rendered is stale/wrong given a verified mover the corpus does not reflect.

## Method
1. Programmatic JOIN of the three inputs by `claim_id`; coverage/dup asserted (181/181).
2. All 154 web-HOLDS → CONFIRMED-HOLDS after CL corroboration: scanned every claim's CL hit
   lists for an in-subject SCOTUS/published-circuit mover contradicting the negative claim. A
   dedicated SCOTUS-hit scan flagged 63 claims with SCOTUS hits; all were keyword noise
   (`Trump v. Barbara/Slaughter/CASA/Cook`, `Zubaydah`, old antitrust matching "collective
   knowledge", or a `Chatrie`/`Case v. Montana` the corpus already carries) — none an unreflected
   mover. See "CL-only signals" below for the one non-trivial case (Hunter, ruled false-positive).
3. All 27 web-MOVED individually reviewed against page context (read each `file:line` + section):
   - **Resolved-reserved-question class (SCOTUS-scoped negative claim, page narrates the
     reservation, mover is a corpus case page or a downstream lower-court remand):** ABS-0007,
     0008, 0009, 0010, 0015, 0023, 0024, 0026, 0029, 0034, 0035, 0036, 0045, 0056, 0057, 0092,
     0093, 0108, 0112. Confirmed each mover case page exists in corpus (Hiibel, Sitz, Opperman,
     Buckley, Davis, Samson, JDB, Nieves, Gonzalez v. Trevino) or the mover is an out-of-scope
     remand that does not falsify the SCOTUS-scoped claim.
   - **Page IS the mover:** ABS-0040, 0041 (Postal Service v. Konan — the page is the Konan case
     page and fully narrates the split's resolution; B6 predicted out-of-remit for page context).
   - **Out-of-remit mover:** ABS-0111 (Johnson v. VanderKooi = Michigan Supreme Court, outside
     the federal remit; per web's own basis it did not categorically foreclose the Hayes-style
     procedure — Hayes's reserved federal question still open).
   - **Mover homed on a sibling node the corpus already covers:** ABS-0178 (Case v. Montana 2026
     is an emergency-aid decision, fully covered on `[[Emergency Aid]]` + its own case page +
     Community Caretaking + Arrest in the Home + Case Index; this Exigent-Circumstances page's
     "no SCOTUS" is section-scoped to hot-pursuit lower-court developments — Case v. Montana is
     not a hot-pursuit mover). Verified via corpus grep: `Case v. Montana` present in 6 files.
   - **Composite reservation whose page already carries the mover:** ABS-0140, 0144 (Third-Party
     Doctrine and CSLI page carries Chatrie in the geofence section, pitfalls, and Key cases;
     B6 predicted "pages likely already carry Chatrie — verify"; verified).
   - **Ganias-scoped claim + unreflected downstream frontier:** ABS-0114 (claim accurate as to
     Ganias's own en-banc declination; Asinor/Richman/Kyer/Armendariz are unreflected but do not
     falsify the row → enrichment candidate + watch).

## CL-only signals (corroboration lane)
- **Hunter v. United States (SCOTUS 2026, cl 10876935/10877631, No. 24-351)** surfaced #3–4 on the
  Brady-pre-plea-split queries for ABS-0003/0004/0100/0101 (and on ABS-0156/0179). **Ruled a
  keyword false-positive, NOT a Brady mover:** the I2-GAP lane already characterized it as a
  progeny of *Dickerson* and *McNabb* under doctrine "confessions-interrogation-and-the-fifth-
  amendment" (`_run/s9/p4/out/I2-GAP-candidates-all.jsonl`). It is already owned by I2-GAP as a
  separate coverage-gap candidate; **not re-filed here** (per brief: do not re-litigate other
  lanes' items). The four Brady claims remain CONFIRMED-HOLDS; the web merits-read (which would
  have caught a June-2026 SCOTUS Brady decision, and instead cited *Garrett*/pending *Mills*)
  is authoritative.
- **ABS-0114 (Ganias retention):** CL surfaced Kyer (4th Cir. 2026) and Armendariz (10th Cir.
  2026) that the web lane did **not** — genuine CL-only published-circuit movement on the
  retention frontier. Folded into the ABS-0114 enrichment candidate + R12 watch (`needs_cl`).

## Findings (2 candidates — both enrichment, not stale-fact fixes)
1. **ABS-0114 unreflected-frontier-movement (low, needs_cl):** post-Ganias digital-over-retention
   line (Asinor D.C. Cir 2024; Richman D.D.C. 2025; Kyer 4th Cir 2026; Armendariz 10th Cir 2026)
   is unreflected in the corpus. The Ganias row itself is accurate — this is an optional LCD/anchor
   enrichment, not a correction.
2. **ABS-0177 unmapped-circuit-enrichment (low, needs_cl):** web surfaced candidate representative
   constructive-entry authority (Sharrar 3d Cir; Curzi 1st Cir; Duncan v. Storie 8th Cir) for
   circuits the page deliberately marks "unmapped." The hedge is literally accurate; verify each is
   on-point before mapping to narrow the list (no 4th Cir candidate surfaced).

## R12 watch additions (3)
- digital-data-retention frontier (ABS-0114; needs_cl).
- unmapped-circuit constructive-entry authority (ABS-0177; needs_cl).
- CSLI through-line "across every technology" phrasing post-Chatrie (ABS-0144; optional copy-tighten,
  no `needs_cl`).

## For orchestrator adjudication
- The two findings are **enrichment candidates on CORPUS-ALREADY-CURRENT rows** (the underlying
  absence claims are accurate); they are filed so the orchestrator can decide whether to seed a
  fix/enrichment packet, not because any rendered assertion is false. Both are `needs_cl` (holdings
  of Asinor/Richman/Kyer/Armendariz/Sharrar/Curzi/Duncan are not verifiable from the lake).
- Net: **0 stale absence claims.** The B-ABS negative-claim set is current as rendered.
