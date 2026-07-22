# P5-L1FIX — LINT-1 verify-semantics rewrite (RULING P5-05)

Packet: **P5-L1FIX** · lane `P5-L1FIX` · model `claude-opus-4-8`
Authority: RULING P5-05 (LINT-1 verify-semantics defect, LAW-02 in the lint itself).
Write-scope: `scripts/lint/lint1_cl_identity.py` + fixtures, `_run/s9/p5/`.
Status: **COMPLETE** — code rewritten cluster-first, offline self-test green (9/9),
sanctioned 5-ref smoke green (4/4 verified refs PASS, 4 CL calls). Batch NOT launched
(orchestrator relaunches the full clean run after this report).

## Defect confirmed (as diagnosed)
A CourtListener human URL `.../opinion/<N>/<slug>/` embeds the **CLUSTER** id N, not an
opinion id. The prior collector never read `courtlistener.cluster_id`; it read
`opinion_id`/`opinion_url` and, on the URL fallback, treated N as an OPINION id, fetching
`/opinions/N/` → an unrelated record → **phantom identity mismatch** (Byrd cluster 4497658 =
Byrd, but opinion 4497658 = Guggenheim). Old records "passed" only by numeric coincidence
(Lawbox-era opinion id == cluster id). Verified live in the smoke: Terry cluster 107729 and
Hester cluster 100413 each still carry a sub-opinion whose id equals the cluster id (the
coincidence), alongside newer harvested opinion ids.

Sub-finding on the "fix the nested read" hint: `c.fm_get(fm, "courtlistener", <key>)` **does**
retrieve the nested block correctly on a real page (Byrd → cluster_id `'4497658'`,
opinion_id `'4274911'`). The bug was never the nested read; it was that the collector read
the wrong field (opinion_url→opinion_id) and had no cluster_id path. Rewrite reads cluster_id
first and derives it from the URL only as a fallback.

## What changed (`scripts/lint/lint1_cl_identity.py`)
1. **collect_references** — ref dict field renamed `opinion_id` → `cluster_id`; every
   URL-derived id is now a cluster id.
   - Frontmatter case refs read `courtlistener.cluster_id` (fallback: cluster id recovered
     from `opinion_url`) AND carry `courtlistener.opinion_id` when present.
   - Prose refs take the CLUSTER id from the embedded URL id; `opinion_id=None` (no binding
     asserted for prose).
   - Null-token guard routed through the shared `c.is_null_token` (folds `null`/`~`/`none`/`""`
     to absent → Entick/Wilkes emit no ref). New `_as_int` coerces subset-parser strings.
2. **verify_reference** — CLUSTER-FIRST, **ONE** call:
   `GET /clusters/<cluster_id>/?fields=case_name,case_name_full,case_name_short,sub_opinions`.
   - Kept: 13/min pacing, builder-token auth, and the P5 retry-once + distinguish-fetch-failure
     behavior (a failed fetch is now `"CL cluster N fetch failed (...) — identity UNVERIFIED,
     not a name mismatch"`, never a phantom mismatch).
   - Name-match against the cluster's canonical name (unchanged token logic).
   - **Binding leg (0 extra calls):** when the ref carries `opinion_id`, assert
     `/opinions/<opinion_id>/` appears in the cluster's `sub_opinions` (frontmatter refs only).
   - Three DISTINCT high messages: `no resolvable cluster id` · `identity mismatch` ·
     `binding mismatch` · plus the distinct `fetch failed … not a name mismatch`.
3. **Kept**: serial-lane gate flag (`--i-am-the-serial-cl-lane`, refuse→exit 2), ledger
   resume design, the memo, 13/min pacing, token auth.
   - Memo **re-keyed** to `(cluster_id, expected-tokens, opinion_id)`. opinion_id is in the
     key deliberately: the binding verdict depends on it, so a prose ref (opinion_id None) and
     a frontmatter ref (opinion_id set) to the same cluster/name must not share a memo slot
     (else the prose ref's name-only pass would suppress the frontmatter ref's binding check).
     Zero fidelity loss; still collapses the many duplicate prose refs.
   - Ledger key re-shaped to `file::line::cluster_id::opinion_id`. **The prior ledger MUST be
     wiped** before the clean re-run (both prior semantics invalid — P5-05); the orchestrator
     points `--ledger=` at a fresh path. Preserved evidence already on disk:
     `_run/s9/p5/lint1-ledger.INVALID-semantics.json`, `_run/s9/p5/lint1-ledger.INVALID-401s.json`.
4. **`--limit=N`** added (caps refs verified — the sanctioned smoke/scoped path).
5. **`--self-test`** added (offline, NO network) + committed fixtures.
6. Module docstring updated to the cluster-first semantics + the builder-credential note.

## Fixtures (new) — `scripts/lint/fixtures/lint1_cl_identity/`
- `byrd_frontmatter.md` — URL embeds cluster id; cluster_id 4497658 + opinion_id 4274911 (binding leg).
- `url_only_frontmatter.md` — no cluster_id field → recovered from URL (107496); no opinion_id.
- `entick_null.md` — `cluster_id: null` / `opinion_id: null` → null-token guard emits no ref.
- `prose_ref.md` — prose CL URL id (111111) parsed as cluster id, opinion_id None.

## Self-test (offline, no network)
`python3 scripts/lint/lint1_cl_identity.py --self-test` → **PASS (9 checks, 0 failed)**.
Covers: URL→cluster-id extraction (frontmatter + URL-fallback + prose), opinion_id carry,
null-token guard, name-mismatch, **binding-mismatch**, fetch-failure-≠-mismatch, missing-cluster-id.

## SMOKE (sanctioned, live CL, 4 calls ≤ 12) — verbatim
```
=== REF 4 (Entick-null): sanctioned off-CL skip ===
  frontmatter/prose refs emitted for Entick: 0 (expect 0 -> nothing to verify)

=== Byrd (frontmatter) ===
  ref: cluster_id=4497658 opinion_id=4274911 expected='Byrd v. United States' source=frontmatter
  verdict: PASS (None)

=== Terry (old-era frontmatter) ===
  ref: cluster_id=107729 opinion_id=9423752 expected='Terry v. Ohio' source=frontmatter
  verdict: PASS (None)

=== Hester (prose URL ref) ===
  ref: cluster_id=100413 opinion_id=None expected='Hester v. United States' source=prose
  verdict: PASS (None)

=== Torres (known-good modern) ===
  ref: cluster_id=4867542 opinion_id=4671321 expected='Torres v. Madrid' source=frontmatter
  verdict: PASS (None)

=== RAW CLUSTER FETCHES (call budget: 4, <=12) ===
  GET https://www.courtlistener.com/api/rest/v4/clusters/4497658/?fields=case_name,case_name_full,case_name_short,sub_opinions
       code=200 case_name='Byrd v. United States'
       sub_opinions=['https://www.courtlistener.com/api/rest/v4/opinions/4274911/']
  GET https://www.courtlistener.com/api/rest/v4/clusters/107729/?fields=case_name,case_name_full,case_name_short,sub_opinions
       code=200 case_name='Terry v. Ohio'
       sub_opinions=['https://www.courtlistener.com/api/rest/v4/opinions/9423752/', 'https://www.courtlistener.com/api/rest/v4/opinions/9423753/', 'https://www.courtlistener.com/api/rest/v4/opinions/9423754/', 'https://www.courtlistener.com/api/rest/v4/opinions/9423755/', 'https://www.courtlistener.com/api/rest/v4/opinions/107729/']
  GET https://www.courtlistener.com/api/rest/v4/clusters/100413/?fields=case_name,case_name_full,case_name_short,sub_opinions
       code=200 case_name='Hester v. United States'
       sub_opinions=['https://www.courtlistener.com/api/rest/v4/opinions/100413/']
  GET https://www.courtlistener.com/api/rest/v4/clusters/4867542/?fields=case_name,case_name_full,case_name_short,sub_opinions
       code=200 case_name='Torres v. Madrid'
       sub_opinions=['https://www.courtlistener.com/api/rest/v4/opinions/4671321/']

=== SUMMARY ===
  Byrd (frontmatter)               PASS
  Terry (old-era frontmatter)      PASS
  Hester (prose URL ref)           PASS
  Torres (known-good modern)       PASS
  Entick-null                       SKIPPED (0 refs, correct)
ALL 4 VERIFIED REFS PASS: True
TOTAL CL CALLS: 4
```
Byrd verified as P5-05 specified: cluster 4497658 names Byrd ✓ and opinion 4274911 ∈
sub_opinions ✓ (binding). Terry ✓ (opinion 9423752 ∈ its sub_opinions). No phantom mismatches.

## Handoff to orchestrator (relaunch)
1. **Wipe** any prior lint1 ledger; run clean:
   `python3 scripts/lint/lint1_cl_identity.py --i-am-the-serial-cl-lane --ledger=_run/s9/p5/lint1-ledger.json`
   (~1,405 refs on the `content/cases` scope alone; full corpus larger; ~2h at 13/min with the
   halved per-ref call count — one cluster call, binding is free).
2. The INVALID-semantics + INVALID-401 ledgers remain as preserved evidence (untouched).
3. COH-17 gate slice (P5-04(a)) re-judges the batch's violations + a 20-row pass sample.
