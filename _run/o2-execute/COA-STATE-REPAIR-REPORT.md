# COA/STATE identity-repair report (2026-07-07)

Lane/model: `{lane: s2-builder, model: claude-opus-4-8}`. Branch `overhaul2/execute`, from HEAD
`b8b9338`. **Committed nothing** — orchestrator commits at the gate. Granted the single serial CL
lane; MCP CourtListener is not this environment's (unauthorized), so all live CL was the REST token
via `scripts/s2/ingest.py` (the packet-A/R1/R8 mechanism), paced ≤14/min, journaled.

**CL calls this session: 59 network. 0×429. 0×5xx. 1×404** (a `courts/caaf` probe — CAAF's CL slug
is not `caaf`; harmless, no dependency). Cache-hit rate for the repair: **185/244 fetches (76%)** —
all 108 cluster reads cache-served; the 59 misses were first-fetch dockets + non-structural court
objects, now cached (re-runs are 0-CL). Ledger: `_overhaul/ledger/cl-calls.log` / pool
`logs/cl-calls.log` (delta 17726→17785). Journal: `s2-ingest-s2-build-96d841cbb12e.jsonl`, step
`r8.coa-state-repair`.

---

## Task 1 — repair tool extended for coa/state (`--repair-coa-state-from-cache`)

New sibling flag on `scripts/s2/ingest.py`, same bounded/journaled/fail-closed idiom as
`--repair-identity-from-cache`. **Key data fact:** in this cache the cluster endpoint carries **no
court** (`court=None`) — CourtListener puts the deciding court on the **docket**. So the derivation is:

- **Authoritative signal = the docket's `court_id`** (`ca1..ca11`/`cadc`/`cafc`/`scotus`, or a state
  slug). Federal circuits classify structurally (no extra fetch); for state/district slugs the
  **court object's `jurisdiction`** ("F"→coa, "FD/FB/FS"→district, "S/SA/ST/SS"→state) decides, and
  its `citation_string` ("11th Cir.", "La.", "D.C.") is the court label.
- **Cross-check = the cluster's citation reporters** (F.2d/F.3d/F.4th→coa; regional/state reporter→
  state; F. Supp.→district; U.S./S.Ct./L.Ed.→scotus). A reporter class that contradicts the docket
  court, or a state-specific reporter that names a different state, **fails closed**.
- **Roster `identity.court` string** ("9th Cir. 2020", "La. 2017", "D.C. Court of Appeals 2025",
  "unknown") is a known-unreliable secondary hint used only for reconciliation.
- Year/`date_decided` from `cluster.date_filed`; `docket_number` completes `identity.docket`.

**Default is fail-closed cache-only** (a cache miss is queued for the lane; no live CL). The opt-in
gate **`--repair-coa-state-allow-docket-fetch`** (mirrors `--web-keys-allow-verified-identity`)
permits the paced serial lane to fetch the docket (cache-first) + court object.

**Fail-closed refusals (never guessed, always escalated):** reporter/docket class mismatch; state
mismatch; roster **class-swap** or **state-swap** (jurisdiction change → suspected re-key);
unclassifiable/military court; coa with no circuit; and — added after a live catch (see wilson) — a
**circuit-swap that is not cite-corroborated** (`expected_citation_found≠True`): a roster circuit
disagreeing with the docket is a stale annotation only when the cluster cite proves the cluster is
the intended case; otherwise it may be a same-name namesake in another circuit.

**The D.C. trap is handled explicitly:** `court_id "dc"` → jurisdiction "S" → **state** (the D.C.
Court of Appeals, a state-class local high court), never the federal `cadc` D.C. Circuit.
`"D.C. Court of Appeals"` in a roster string maps to state dc; only `"D.C. Cir."` maps to coa cadc.

**Self-test + fixtures (`self_test_repair_coa_state_from_cache`, in the `--self-test` suite — all
green):** pure-derivation fixtures for a coa row, a state row, cadc, cafc, the D.C.-Court-of-Appeals
trap, a cite-corroborated circuit correction, an **uncorroborated** circuit swap (refuse), reporter
class conflict, reporter/docket state mismatch, roster class-swap, unclassifiable/military court, and
all cache-only paths (clean coa write, coa-no-circuit refusal, no-signal refusal, state write); plus
an end-to-end harness (docket-authoritative writes coa/state/dc, escalates a state-mismatch, queues
an uncached cluster, idempotent re-run "confirmed", cache-only mode never fetches a docket, and
out-of-scope status fails the batch closed).

---

## Task 2 — run over the full residue (docket-authoritative)

Ground-truthed the residue at HEAD: **65 records** carry `court_level ∉ {scotus,coa,state,district}`
(59 None + 6 "other"), all projecting `authority_weight="Historical"` via `project.py`. Of these,
**54 are `verified_identity`** (the tool's scope). Ran **52** docket-authoritative
(`--repair-coa-state-allow-docket-fetch`), excluding **zorn** (instructed; corrupt cluster) and
**chapman** (known scotus mis-key, packet-B EXCLUDE-remit; outside the coa/state remit).

**Result: 44 repaired · 8 escalated · 0 queued.** (District: none appear in this residue.)

### 44 repaired/confirmed — authoritative court/circuit/state/year/docket

37 coa + 7 state. Every circuit/state is the docket's `court_id`; year is `cluster.date_filed`.
Docket numbers now populate `identity.docket`.

| court_level | records (circuit/state) |
|---|---|
| coa | alasaad(ca1) · gaetjens(ca7) · jimerson-v-lewis(ca5) · johnson-v-glick(ca2) · knight(ca11) · ackerman(ca10) · aigbekaen(ca4) · brinkley(ca4) · burgess(ca10) · camou(ca9) · capers(ca2) · carlton-williams(ca3) · castillo(ca1) · chavez(ca4) · crumble(ca8) · cruz(ca1) · davis(ca8) · hanapel(ca8) · hay(ca10) · holcomb(ca9) · hunt(ca9) · kolsuz(ca4) · lee(ca6) · loera(ca9) · loines(ca6) · massenburg(ca4) · may-shaw(ca6) · mayville(ca10) · moore-bush(ca1) · oliveras(ca2) · payne(ca9) · perez-rodriguez(ca1) · porter(ca8) · ruckman(ca5) · trent(ca8) · vasquez-algarin(ca3) · xiang(ca8) |
| state | carter(dc) · serge(pa) · seymour(co) · demesme(la) · karston(la) · larson(ia) · wint(nj) |

**8 circuit corrections** (roster annotation stale; docket authoritative; each cite-corroborated,
`expected_citation_found=True` — the cluster cite matched the roster's expected cite, so the roster's
*circuit label* was wrong): castillo ca5→**ca1** (126 F.4th 791) · chavez ca10→**ca4** (128 F.4th 226)
· loera ca10→**ca9** (135 F.4th 856) · porter ca5→**ca8** (142 F.4th 1140) · ruckman ca10→**ca5**
(690 F. App'x 189) · trent ca6→**ca8** (995 F.3d 1029) · davis ca4→**ca8** (R3-corroborated, below)
· wilson ca9→ca5 (**refused** — see escalations). Several stale roster *years* were also corrected
from the cluster (e.g. burgess "2009"→2024, capers "2010"→2021, castillo "2023"→2025).

### 8 escalations (fail-closed; NOT written — verified clean, no spurious court_level)

| record | reason | orchestrator action |
|---|---|---|
| people-v-frederick--10579458 | roster-state-swap **mi→ny** (docket court_id `ny`) | RE-KEY: cluster 10579458 is a New York *People v. Frederick* (2025); the record intends the Michigan cell-phone case (500 Mich. 228, 2017). Wrong-case mis-key, not a court repair. |
| state-v-andrews--4335207 | roster-state-swap **md→oh** (docket court_id `oh`) | RE-KEY: cluster 4335207 is an Ohio *State v. Andrews* (reporter "Ohio"); record intends the Maryland cell-site-simulator case (227 Md. App. 350). |
| united-states-v-cole--9623101 | unclassifiable-court `armfor` (military CAAF) | RE-KEY: cluster is a military *US v. Cole* (23-0162/AF); intended = 7th Cir., **21 F.4th 421** (R8-R3-web-cites). |
| united-states-v-lyle--8435375 | unclassifiable-court `nmcca` (Navy-Marine CCA) | RE-KEY: intended = 2d Cir., **919 F.3d 716** (R8-R3-web-cites). |
| united-states-v-small--10593041 | unclassifiable-court `nmcca` | RE-KEY: intended = 4th Cir., **944 F.3d 490** (R8-R3-web-cites). |
| united-states-v-mendoza--10131439 | unclassifiable-court `armfor` | RE-KEY: cluster is military *US v. Mendoza* (23-0210/AR); intended = 3d Cir. slip No. 25-1154 (R8-R3-web-cites). |
| united-states-v-ruiz--10650477 | unclassifiable-court `armfor` (CAAF, 24-0158/MC) | OFF-MODEL: cluster is correctly the CAAF case (matches R8-R3-web-cites) but CAAF is a military appellate court with no circuit — not on the coa/state/district ladder; R3 note flags it "evidentiary, not 4th Am" (possible corpus exclusion). Orchestrator decision. |
| united-states-v-wilson--10664712 | circuit-swap-uncorroborated ca9→ca5 | RE-KEY: cluster 10664712 is a 5th Cir. Wilson (docket 25-30105); intended = 9th Cir. **13 F.4th 961** (docket 18-50440, R8-R3-web-cites). Namesake mis-key — the reason the uncorroborated-swap gate was added. |

**Finding (cole/lyle/small/mendoza):** four "citations-empty" verified_identity clusters are mis-keyed
to **military namesakes** (armfor/nmcca) — which is exactly why CL held no reporter cite for them and
the R3 lane had to web-recover the federal-circuit cites. These are re-key candidates; the correct
federal cites are already in `R8-R3-web-cites.jsonl`.

### Residue remaining — how many still project a wrong/unknown authority weight

Residue dropped **65 → 21** (`court_level ∉ strict`). Manifest court_level: coa 66→**103**, state
9→**16**, None 59→**17**, other 6→4. The remaining 21:

- **8 escalated verified_identity** (the table above) — still project "Historical", surfaced with a
  specific re-key/off-model finding (not silently broken).
- **2 excluded** — zorn (corrupt cluster, held for off-CL/corrected-cluster) and chapman (scotus
  mis-key, packet-B EXCLUDE-remit).
- **11 off-scope** (not `verified_identity`, so outside the tool's allow-list): Entick + Wilkes
  (verified_off_cl English corpus — no CL cluster; "Historical" is defensible for them); Kalkines v.
  United States (verified, "other"; a Court-of-Claims case — an edge court, flagged below); 3
  not_found (no cluster to derive from); 3 folded-alias (not live pages); 2 fabrication_suspected.

**W3 priority subset — 7/8 clean, 1 escalated:**

| W3 row | outcome |
|---|---|
| alasaad-v-wolf--4855246 | **coa ca1, 2021**, docket 20-1077P ✓ |
| gaetjens-v-winnebago-county--4899427 | **coa ca7, 2021**, docket 20-1295 ✓ |
| jimerson-v-lewis--9475670 | **coa ca5, 2024**, docket 22-10441 ✓ |
| johnson-v-glick--8903545 | **coa ca2, 1973**, docket 72-2428 ✓ (roster was "unknown"; docket authoritative) |
| knight-v-jacobson--778847 | **coa ca11, 2002**, docket 01-15506 ✓ |
| state-v-demesme--5035127 | **state la, 2017**, docket 2017-KK-0954 ✓ |
| carter-v-united-states--10662535 | **state dc, 2025**, docket 23-CF-0388 ✓ (D.C.-Court-of-Appeals trap resolved to state, not cadc) |
| people-v-frederick--10579458 | **ESCALATED** — roster-state-swap mi→ny (wrong-case mis-key; needs re-key) |

---

## Task 3 — slip-identity completions

The 15 slip rows (`_run/o2-execute/s6-slip-stamp-journal.jsonl`). `derive_slip_cite` needs
docket + court + year; before this session 9 lacked them (per R8-PIPELINE §12). Those 9 overlap the
Task-2 residue, so the docket-authoritative run completed court + circuit/state + year + **docket** in
one pass.

**12/15 now mintable** (`derive_slip_cite` returns a non-None cite):

| status | slip rows |
|---|---|
| **newly completed this session (6)** | carter (state dc, 23-CF-0388) · larson (state ia, 24-0809) · davis (coa ca8, 23-2978) · holcomb (coa ca9, 23-469) · hunt (coa ca9, 23-2342) · lee (coa ca6, 24-1341) |
| already mintable (6) | robinson · D.C. v. R.W. · landor · olivier · konan · GEO Group |
| **blocked (3)** | **mendoza** (military mis-key cluster armfor — re-key first) · **ruiz** (CAAF off-model — orchestrator decision) · **zorn** (excluded — corrupt) |

**davis note (writer≠checker):** davis's cluster is citations-empty, so its circuit swap (roster ca4
→ docket ca8) is not cite-corroborated and the tool **escalated** it. I completed it as a Task-3
identity completion because the ratified dual-leg `R8-R3-web-cites.jsonl` states "COURT FIX: 8th Cir.,
No. 23-2978, 2025-09-11" and the cluster's docket number **23-2978** + date **2025-09-11** match that
recovery exactly (same evidentiary basis as the `--apply-web-cites` web-recovery landings). Journaled
with `basis="docket-authoritative + R3-docket-corroboration"`. wilson's analogous swap was **refuted**
by the same test (R3 docket 18-50440 ≠ cluster docket 25-30105) and stays escalated.

**Mint-display note for the S6 lane (not blocking):** for state slip rows `slip_court_abbr` emits the
raw `identity.state` abbr, so carter/larson render as `(dc 2025)`/`(ia 2025)` rather than
`(D.C. 2025)`/`(Iowa Ct. App. 2025)`. The clean court label is already in `identity.court`
("D.C. 2025", "Iowa Ct. App. 2025"); recommend `mint_page.slip_court_abbr` (S6 lane) prefer the
court `citation_string` for state. Mintability is unaffected.

---

## Integrity / escalations for the orchestrator

- Bijection **662 manifest ↔ 662 lake files**, 0 dup ids, 0 orphans. `status_counts` **unchanged**
  (court repair never touches status). Manifest fully re-synced to case records (0 desyncs) after a
  SIGTERM'd mid-run left some rows stale — re-run confirmed all 44 and saved.
- `project.py`: `--self-test` green; full-corpus dry-run **0 projection_errors, ok_to_project=true**;
  new-form pages 473→**484** (repaired rows now project real "Binding in-circuit"/"Persuasive-state"
  weights). All 44 repaired coa records carry a valid circuit (none raise).
- `ingest.py --self-test`: **green** (incl. the new `self_test_repair_coa_state_from_cache`).
- **Escalations:** (1) 8 verified_identity re-key/off-model rows (Task-2 table) — 6 are wrong-case
  mis-keys with the correct target already in `R8-R3-web-cites.jsonl`; ruiz is an off-model CAAF row;
  people-frederick/andrews are state-jurisdiction mis-keys. (2) mendoza + ruiz block slip mint until
  re-keyed/decided. (3) **Pre-existing (not this session):** `long-lake-township-v-maxon--ucb0bfc28`
  (not_found stub, cluster_id=None) has bogus `circuit="ca2021"` — a Michigan **state** case
  mis-tagged coa by the `parse_circuit`-year bug in `s6_candidate_court_fields`; it raises in a strict
  all-records projection (project.py's real content-page scope is unaffected). Out of the tool's
  verified_identity scope; flagged for the S6/frontier lane. (4) Kalkines v. United States (verified,
  court_level "other" — a Court-of-Claims edge court) is outside the verified_identity allow-list;
  orchestrator may extend scope or leave as-is.

## Files (UNCOMMITTED)

- Code: `scripts/s2/ingest.py` (+798 lines): `--repair-coa-state-from-cache` +
  `--repair-coa-state-allow-docket-fetch`; helpers `classify_cl_court_id`, `reporter_court_class`,
  `roster_court_hint`, `derive_coa_state_court`, `repair_coa_state_from_cache`; client `get_docket`/
  `get_court`; self-test `self_test_repair_coa_state_from_cache` (registered).
- Lake: 44 repaired case records + `_manifest.json` (counts regenerated, 662; coa 103/state 16).
  davis completed via R3 corroboration; wilson reverted to residue + escalated.
- Journal: `r8.coa-state-repair` (44 repaired/confirmed + 8 escalated + docket/court fetch trace).
- This report.
