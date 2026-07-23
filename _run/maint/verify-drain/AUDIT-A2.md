# MAINT-1 verify-drain audit A2

Audit date: 2026-07-23  
Lane: CSSI builder, loop 2 of MAINT-1 verify-drain  
Command: `python3 scripts/maint/verify_drain.py --reexamine`

## Verdict

**PASS — no mismatch found.**

The reexamination completed cleanly:

```text
DONE: examined=54 fetches=4 promoted=36 slip_eligible=17
```

The append-only ledger had exactly 196 loop-1 rows before the command. Loop 2
is therefore lines 197–250, inclusive. It contains 54 rows and no `error`,
`slip_party_leg_failed`, or `cite_appeared` disposition.

All 36 newly promoted lake records were checked. Every one has:

- `status: verified`;
- a provenance warning naming its exact ledger `cite_rule`; and
- a provenance warning naming its exact ledger `party_rule`.

The rule-specific source checks also all passed:

- all 26 R1 rows have `identity.canonical_name_match: true`, and at least one
  non-null ledger `party_evidence.matched` value is genuinely present in the
  cached lead-opinion text;
- both R2 `cluster-subops-<cluster_id>.json` files genuinely list the lake
  record's `identity.lead_opinion_id`; and
- all five R3 lake records have
  `citations.official.source: "web-dual-leg"`.

## Loop-2 disposition counts

| Disposition | Count |
|---|---:|
| `promoted_verified` | 36 |
| `slip_eligible` | 17 |
| `not_promoted` | 1 |
| `error` | 0 |
| `slip_party_leg_failed` | 0 |
| `cite_appeared` | 0 |
| **Total** | **54** |

The two loop-1 transient failures resolved: **United States v. Payne** was
promoted using the ordinary cluster-citation and body-text legs, while
**State v. Volle** became `slip_eligible`.

## Promotion counts by rule

Party and citation rules are separate axes. In particular, the five R3
promotions also have the ordinary `body-text` party rule.

### Party rule

| Party rule | Promotions |
|---|---:|
| `caption-leg (MAINT-1-R1)` | 26 |
| `structural-leg (MAINT-1-R2)` | 2 |
| `body-text` | 8 |
| **Total** | **36** |

### Citation rule

| Citation rule | Promotions |
|---|---:|
| `cluster.citations` | 30 |
| `cluster.citations (recomputed)` | 1 |
| `web-dual-leg (MAINT-1-R3)` | 5 |
| **Total** | **36** |

Thus the explicit ruling counts are **R1: 26**, **R2: 2**, and **R3: 5**.
R3 overlaps with the party-rule axis rather than forming a mutually exclusive
third party-rule bucket.

## Rule inventory for every new promotion

| Ledger line | Record | Citation rule | Party rule |
|---:|---|---|---|
| 197 | Alasaad v. Wolf | `web-dual-leg (MAINT-1-R3)` | `body-text` |
| 198 | Arkansas v. Sanders | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 199 | Beecher v. Alabama | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 200 | Berkemer v. McCarty | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 201 | Brown v. Mississippi | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 202 | Brown v. Texas | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 203 | Camara v. Municipal Court | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 204 | Carroll v. Carman | `web-dual-leg (MAINT-1-R3)` | `body-text` |
| 208 | Davis v. United States | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 210 | Donovan v. Dewey | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 211 | Flippo v. West Virginia | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 212 | Frazier v. Cupp | `cluster.citations` | `structural-leg (MAINT-1-R2)` |
| 213 | Go-Bart Importing Co. v. United States | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 214 | Heller v. New York | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 215 | Horton v. California | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 216 | Jimerson v. Lewis | `web-dual-leg (MAINT-1-R3)` | `body-text` |
| 217 | Knight v. Jacobson | `cluster.citations` | `body-text` |
| 218 | Kolender v. Lawson | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 219 | Kuhlmann v. Wilson | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 220 | LaChance v. Erickson | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 221 | LaDuke v. Nelson | `cluster.citations` | `body-text` |
| 223 | Marbury v. Madison | `cluster.citations (recomputed)` | `caption-leg (MAINT-1-R1)` |
| 224 | Marcus v. Search Warrant | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 225 | Mathis v. United States (1968) | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 226 | Mooney v. Holohan | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 228 | People v. Frederick | `web-dual-leg (MAINT-1-R3)` | `body-text` |
| 231 | Robbins v. California | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 233 | Sorrells v. United States | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 234 | South Dakota v. Neville | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 235 | State v. Demesme | `cluster.citations` | `structural-leg (MAINT-1-R2)` |
| 236 | State v. Larson | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 239 | United States v. Anchondo | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 241 | United States v. Kolsuz | `web-dual-leg (MAINT-1-R3)` | `body-text` |
| 245 | United States v. Payne | `cluster.citations` | `body-text` |
| 246 | United States v. Perez-Rodriguez | `cluster.citations` | `caption-leg (MAINT-1-R1)` |
| 249 | Weeks v. United States | `cluster.citations` | `caption-leg (MAINT-1-R1)` |

## R1 caption-leg audit

All 26 R1 promotions were checked, not merely sampled. Each lake record has
`canonical_name_match: true`. For each one, the non-null matched phrase or
token shown below was checked case-insensitively against
`cache/op-<lead_opinion_id>.txt` and was genuinely present.

| Record | Lead opinion | Body-side evidence confirmed in cache | Verdict |
|---|---:|---|---|
| Arkansas v. Sanders | 9427641 | phrase `Arkansas` | PASS |
| Beecher v. Alabama | 9423505 | phrase `Alabama` | PASS |
| Berkemer v. McCarty | 9429728 | phrase `McCarty` | PASS |
| Brown v. Mississippi | 102604 | phrase `Brown` | PASS |
| Brown v. Texas | 110128 | phrase `Texas` | PASS |
| Camara v. Municipal Court | 107473 | token `municipal` | PASS |
| Davis v. United States | 9433017 | phrase `United States` | PASS |
| Donovan v. Dewey | 9428427 | phrase `Dewey` | PASS |
| Flippo v. West Virginia | 1854815 | phrase `West Virginia` | PASS |
| Go-Bart Importing Co. v. United States | 101643 | phrase `United States` | PASS |
| Heller v. New York | 9425413 | phrase `New York` | PASS |
| Horton v. California | 9432041 | phrase `California` | PASS |
| Kolender v. Lawson | 9429183 | phrase `Lawson` | PASS |
| Kuhlmann v. Wilson | 9430620 | phrase `Wilson` | PASS |
| LaChance v. Erickson | 118163 | phrase `Erickson` | PASS |
| Marbury v. Madison | 84759 | phrase `Marbury` | PASS |
| Marcus v. Search Warrant | 9422285 | token `search` | PASS |
| Mathis v. United States (1968) | 9423682 | phrase `United States` | PASS |
| Mooney v. Holohan | 102372 | phrase `Mooney` | PASS |
| Robbins v. California | 9428483 | phrase `California` | PASS |
| Sorrells v. United States | 101997 | phrase `United States` | PASS |
| South Dakota v. Neville | 9429007 | phrase `South Dakota` | PASS |
| State v. Larson | 1187724 | phrase `State` | PASS |
| United States v. Anchondo | 758111 | phrase `United States` | PASS |
| United States v. Perez-Rodriguez | 4882594 | phrase `United States` | PASS |
| Weeks v. United States | 98094 | phrase `United States` | PASS |

For every row in this table, the lake `status` and promotion-warning checks
also passed. **R1 verdict: 26/26 PASS.**

## R2 structural-leg spot checks

Every R2 row was checked.

| Record | Cluster cache | Lead opinion | Cached `sub_opinions[]` | Lake/warning | Verdict |
|---|---|---:|---|---|---|
| Frazier v. Cupp | `cluster-subops-107913.json` | 107913 | contains `/opinions/107913/` | `verified`; warning names `cluster.citations` and `structural-leg (MAINT-1-R2)` | PASS |
| State v. Demesme | `cluster-subops-5035127.json` | 4848796 | contains `/opinions/4848796/` (and 4848797) | `verified`; warning names `cluster.citations` and `structural-leg (MAINT-1-R2)` | PASS |

**R2 verdict: 2/2 PASS.**

## R3 web-dual-leg spot checks

Every R3 row was checked.

| Record | Official citation | Lake `citations.official.source` | Party rule | Lake/warning | Verdict |
|---|---|---|---|---|---|
| Alasaad v. Wolf | 988 F.3d 8 | `web-dual-leg` | `body-text` | `verified`; warning names R3 and body-text | PASS |
| Carroll v. Carman | 574 U.S. 13 | `web-dual-leg` | `body-text` | `verified`; warning names R3 and body-text | PASS |
| Jimerson v. Lewis | 94 F.4th 423 | `web-dual-leg` | `body-text` | `verified`; warning names R3 and body-text | PASS |
| People v. Frederick | 500 Mich. 228 | `web-dual-leg` | `body-text` | `verified`; warning names R3 and body-text | PASS |
| United States v. Kolsuz | 890 F.3d 133 | `web-dual-leg` | `body-text` | `verified`; warning names R3 and body-text | PASS |

**R3 verdict: 5/5 PASS.**

## Final remaining residue

### Verification-drain residue

Only one loop-2 drain row remains unpromoted:

- **illinois-v-fisher--5141053** — official citation leg passed via
  `cluster.citations`, but the party leg failed: `Fisher` is absent from the
  cached opinion text and the lake has `canonical_name_match: false`, so R1
  and R2 are correctly unavailable under the explicit ruling.

There were no genuine retry failures or other failed verification-drain rows.

### Cite-less slip queue

Seventeen loop-2 rows remain unpromoted as `slip_eligible`. These are not
verification failures: each has no official reporter citation, has a strict
body-text party-leg pass, and awaits the separate slip-status application
step or a future reporter citation.

- **Carter v. United States** — no official citation; strict body-text party leg passed.
- **Case v. Montana** — no official citation; strict body-text party leg passed.
- **Chatrie v. United States** — no official citation; strict body-text party leg passed.
- **District of Columbia v. R.W.** — no official citation; strict body-text party leg passed.
- **Landor v. Louisiana Dept. of Corrections** — no official citation; strict body-text party leg passed.
- **Olivier v. City of Brandon** — no official citation; strict body-text party leg passed.
- **People v. Hughes** — no official citation; strict body-text party leg passed.
- **Postal Service v. Konan** — no official citation; strict body-text party leg passed.
- **Robinson v. Commonwealth** — no official citation; strict body-text party leg passed.
- **State v. Volle** — prior transient fetch error resolved; no official citation and strict body-text party leg passed.
- **The GEO Group, Inc. v. Menocal** — no official citation; strict body-text party leg passed.
- **United States v. Hunt** — no official citation; strict body-text party leg passed.
- **United States v. Lewis** — no official citation; strict body-text party leg passed.
- **United States v. Mendoza** — no official citation; strict body-text party leg passed.
- **United States v. Morton** — no official citation; strict body-text party leg passed.
- **United States v. Porter** — no official citation; strict body-text party leg passed.
- **United States v. Trent** — no official citation; strict body-text party leg passed.

The 42 additional cite-less, non-paged `verified_identity` lake records were
outside both loop-2 pools and produced no loop-2 ledger rows; they are not
included in this verify-drain residue list.
