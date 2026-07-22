# FIX-L1URLS — summary

Packet: FIX-L1URLS (O2 EXECUTE, lane `claude`, model `claude-opus-4-8`)
Authority: `_run/s9/p5/COH17-GATE-SLICE.md` — the 5 REAL wrong-cluster URLs with
MCP-confirmed canonical cluster ids (Claude MCP lane, cross-credential vs. the
builder-token LINT-1 batch). Date: 2026-07-22.
Write-scope: the 5 named content files + `_run/s9/p5/`.

## 1. URL fixes applied (id + slug only; no surrounding text touched)

| # | Case | File:line | old cluster | new cluster | prior LINT-1 mismatch (wrong cluster named) |
|---|------|-----------|-------------|-------------|---------------------------------------------|
| 1 | *Missouri v. McNeely*, 569 U.S. 141 (2013) | SIA Alcohol Tests.md:78 | 882802 | **858288** | 'State v. Rentmeister' |
| 2 | *Mitchell v. Wisconsin*, 588 U.S. 840 (2019) | SIA Alcohol Tests.md:79 | 4218101 | **9231242** | 'Spokane Savings & Loan Society v. Park Vista Improvement Co.' |
| 3 | *Florida v. Jardines*, 569 U.S. 1 (2013) | Aerial and Enhanced Surveillance.md:97 | 2094497 | **856347** | 'In Re Hanford Nuclear Reservation Litigation' |
| 4 | *United States v. Gratkowski*, 964 F.3d 307 (5th Cir. 2020) | Third-Party Doctrine and CSLI.md:120 | 4772500 | **4765051** | 'Ostanek v. Ostanek' |
| 5 | *Minnesota v. Dickerson*, 508 U.S. 366 (1993) | Terry Stops and Reasonable Suspicion.md:156 | 112879 | **112873** | 'Wisconsin v. Mitchell' |

Slug form kept consistent in every case (only the numeric cluster id changed,
e.g. `/opinion/858288/missouri-v-mcneely/`). No other text on any line changed.

## 2. Collector-only re-check (LINT-1, unconfirmed mode — no serial-lane flag)

`python3 scripts/lint/lint1_cl_identity.py <file>` run once per file. The lint
correctly REFUSED all network I/O (exit 2, "WRITE-ONLY / serial-CL-gate-only")
and printed the collected reference count:

- SIA Alcohol Tests.md — 10 refs
- Aerial and Enhanced Surveillance.md — 21 refs
- Third-Party Doctrine and CSLI.md — 28 refs
- Terry Stops and Reasonable Suspicion.md — 58 refs

Grep confirms each fixed line now carries the corrected cluster id + slug
(858288 / 9231242 / 856347 / 4765051 / 112873); the old ids are absent from the
five fixed Sources/roster lines.

## 3. LINT-1 ledger update

`_run/s9/p5/lint1-ledger.json`: the 5 stale violation rows REMOVED
(45 -> 40 violations; 4425 -> 4420 total rows). Keys removed:

- `content/warrant-exceptions/searching-a-person/SIA Alcohol Tests.md::78::882802::None`
- `content/warrant-exceptions/searching-a-person/SIA Alcohol Tests.md::79::4218101::None`
- `content/searches/Aerial and Enhanced Surveillance.md::97::2094497::None`
- `content/searches/the-third-party-doctrine-and-digital-surveillance/Third-Party Doctrine and CSLI.md::120::4772500::None`
- `content/seizures/Terry Stops and Reasonable Suspicion.md::156::112879::None`

No corrected pass-rows were re-added to the ledger. Per instruction, **the
corrected refs are verified by the orchestrator's MCP slice (cross-credential)
rather than re-batched** through the builder-token serial CL lane. (Writer !=
checker: I do not certify the new cluster ids myself; the COH17 MCP slice is the
attestation of record.) Pre-edit ledger preserved at
`_run/s9/p5/lint1-ledger.pre-FIX-L1URLS.bak.json`.

## 4. FINDING — escalation to orchestrator (NOT in my edit scope; not self-fixed)

The identical wrong cluster ids ALSO appear at the **Case Index table rows** of
four of these files — same case, byte-identical wrong id:

- SIA Alcohol Tests.md:60 — McNeely `882802` (table row)
- SIA Alcohol Tests.md:61 — Mitchell `4218101` (table row)
- Aerial and Enhanced Surveillance.md:75 — Jardines `2094497` (table row)
- Terry Stops and Reasonable Suspicion.md:119 — Dickerson `112879` (table row)

(Gratkowski has no table-row twin — its only occurrence was the fixed Sources
line 120, now clean.)

These table-row refs passed LINT-1 as NULL (non-violation) rows because the
row's case name is a `[[wikilink]]` caption, which `mask_links_and_code` masks
out -> the pairing heuristic saw no "X v. Y" caption -> the name check was
skipped -> trivial pass. This is exactly the lint-heuristic blind spot COH17
flagged ("pairing should prefer the row's [[wikilink]] subject"). They are
therefore genuine wrong-cluster URLs that the gate batch did not surface as
violations.

My instructed edit list is explicit to the 5 Sources/roster lines only
("Apply exactly ... URL id + slug only; no other text"), so per writer!=checker
discipline I did NOT self-expand scope to the table rows. Returning this to the
machine to adjudicate whether a follow-up packet should correct these four
table-row URLs to the same MCP-confirmed canonical ids
(882802->858288, 4218101->9231242, 2094497->856347, 112879->112873).

## 5. ADDENDUM — table-row twins corrected (coordinator adjudication)

The §4 escalation was adjudicated: SAME ruling, SAME canonical ids — the COH17
slice's MCP confirmations cover the CASE IDENTITY, not the surface. The four
Case Index table-row twins were corrected to the identical canonical clusters
(id + slug only, no other text on the line):

| Case | File:line (table row) | old cluster | new cluster |
|------|-----------------------|-------------|-------------|
| *Missouri v. McNeely* | SIA Alcohol Tests.md:60 | 882802 | **858288** |
| *Mitchell v. Wisconsin* | SIA Alcohol Tests.md:61 | 4218101 | **9231242** |
| *Florida v. Jardines* | Aerial and Enhanced Surveillance.md:75 | 2094497 | **856347** |
| *Minnesota v. Dickerson* | Terry Stops and Reasonable Suspicion.md:119 | 112879 | **112873** |

No LINT-1 ledger action for these four: they were null pass-rows (not
violations), so there was no violation key to remove. Each case now carries the
canonical cluster on BOTH its table-row and Sources-line URL.

**Corpus-wide sweep (post-fix):** `grep -rn` over all of `content/` for every
old id — both URL-form (`opinion/<id>/`) and bare-number — returns ZERO hits.
No further twins exist anywhere in the corpus; nothing else to fix or report.

### Handoff note — LINT-1 lint-heuristic backlog (3 items)
The wikilink-masked-caption blind spot in LINT-1's pairing (this packet's
diagnosis) JOINS the two COH17 lint-heuristic items. Full backlog for a future
lint-hardening pass:
1. **(COH17)** nearest-name pairing grabs a DIFFERENT case named on the same
   line — pairing should prefer the row's `[[wikilink]]` subject / skip
   *Id.*-links.
2. **(COH17)** tokenizer digit-truncation ("District 47J v. Acton" -> want-tokens
   lose 'acton') — tokenizer should not truncate at digits mid-caption.
3. **(FIX-L1URLS, new)** `mask_links_and_code` masks a `[[wikilink]]` case
   caption entirely, so Case Index table rows yield an EMPTY expected-name and
   pass the identity check trivially (false-negative: a wrong-cluster URL on a
   wikilink-captioned row is never surfaced). The pairing should read the
   `[[wikilink]]` target as the expected case name for such rows (dovetails with
   item 1's "prefer the row's [[wikilink]] subject"). Empirically this hid four
   real wrong-cluster URLs (SIA:60/61, Aerial:75, Terry:119) that only the
   Sources-line twins exposed.

## Outputs
- `_run/s9/p5/FIX-L1URLS-fixes.jsonl` (9 rows: 5 Sources/roster + 4 table-row followup)
- `_run/s9/p5/FIX-L1URLS-summary.md` (this file)
- `_run/s9/p5/lint1-ledger.json` (5 violation rows removed)
- `_run/s9/p5/lint1-ledger.pre-FIX-L1URLS.bak.json` (pre-edit backup)
- Edited content: SIA Alcohol Tests.md (lines 60, 61, 78, 79), Aerial and
  Enhanced Surveillance.md (lines 75, 97), Third-Party Doctrine and CSLI.md
  (line 120), Terry Stops and Reasonable Suspicion.md (lines 119, 156)
