# CAMP-A1b — LINT-14 hybrid remedy (P4-18) packet summary

**Lane:** `{lane: CAMP-A1b, model: claude-opus-4-8}` · **Branch:** overhaul2/execute
**Authority:** RULING P4-18 (i/ii/iii); supersedes P4-16(a). S2 R2 (two-key party-name-in-text), `_schema.json` allOf[1], A16 precedent (verified_off_cl publish-gate addition), P4-14 (fieldI reader banner models {verified_identity, field_i unverified}), P4-10 (the 29-record promotion set), S1 A8 (weight lexicon), S4-R10.
**Write-scope used:** `_overhaul2/lake/cases/Riley v. California.json` (1 flip); `_overhaul2/lake/_schema.json` (identity_method enum += `p4-cache-text-check`, ruling-mandated — see scope note); `content/cases/Riley v. California.md` (re-projection, lake.status only); `content/cases/United States v. August.md` + `United States v. Sandoval.md` (holding: leak fixes); `scripts/lint/lint14_pagerecord.py` + `scripts/lint/_common.py` + 2 new fixtures; `_run/s9/p4/campaign/`.

## Deterministic coverage — 29/29

| Task | Assigned | Examined | Flipped | Residue | Skipped |
|---|---|---|---|---|---|
| P4-18(i) party-name-in-text earn | 29 records | 29 | 1 | 28 | 0 |

## Per-lint before -> after

| Lint | Before | After | Status |
|---|---|---|---|
| LINT-14 | 29 high | **0** | FIXED — 1 flipped to `verified` (P4-18(i)) + 28 accepted via `verified_identity` gate add (P4-18(ii)); self-test 5/5 PASS |
| LINT-13 | 0 | **0** | held — Riley re-validates `verified` after enum extension + earned two-key; self-test PASS |
| LINT-12 | 5 high | **5 high** | not regressed — identical baseline (Roberson/Sanders/Frank/Kalkines/Trent); Riley absent |
| LINT-16 | 1 high | **0** | FIXED — Standing `Historical foil.` FP cleared by `_common` guard; real leak fixture still fails; self-test 16/16 PASS |
| LINT-4 | 0 | **0** | unaffected — lint4 does not consume `weight_label_in_cell` |

---

## (i) P4-18(i) — earn the party-name-in-text leg: 1 flip

Mechanical check = the exact S2 identity assertion (`scripts/s2.ingest.missing_party_terms`), run against the cached **lead-opinion** text `~/cssi-lake/cache/text/<lead_opinion_id>.txt`. For US-captioned cases the US side's last term ('states') is trivially present in any federal opinion, so the operative check is the OTHER party's surname — matching S2's convention (validated: Agnello v. United States, a known-`verified` record, reproduces party_name_in_text=true). A record flips ONLY when BOTH terms appear **and** `field_i_validity != unverified` **and** `expected_citation_found == true` (schema allOf[1]).

| Record | lead_op | evidence (normalized offsets) | field_i | ecf | status |
|---|---|---|---|---|---|
| Riley v. California | 2680439 | `riley`@653, `california`@662 | good_law | True | verified_identity -> **verified** |

**Riley v. California** edits: `party_name_in_text` false->true; `identity_method` `panel-cluster-rekey`->`p4-cache-text-check`; `reason_code` `recent_or_no_official_cite`->null; a provenance.warnings row records the old method + evidence offsets; `status` verified_identity->verified. Re-projected (project.py `field_counts={'lake.status':1}`, idempotent 2nd pass). lint13=0.

## (ii) P4-18(ii) — residue stays verified_identity; publish gate amended: 28

The residue cannot reach `verified` without fabricating a two-key leg (banned). It stays at the legitimate S2 R1 status `verified_identity`; `lint14_pagerecord.py` ACCEPTED set gains `verified_identity` (mirrors A16's `verified_off_cl` addition; comment cites RULING P4-18 + the P4-14 banner model). Reader safety = the P4-14 fieldI reader banner (models exactly {status: verified_identity, field_i: unverified}) + each content assertion's own pin/quote discipline.

| Record | lead_op | field_i | ecf | residue class |
|---|---|---|---|---|
| Arizona v. Youngblood | 9431483 | unverified | True | field_i unverified |
| Austin v. United States | 9432892 | unverified | True | field_i unverified |
| Briscoe v. LaHue | 9429107 | unverified | True | field_i unverified |
| Buckley v. Fitzsimmons | 9432862 | unverified | True | field_i unverified |
| Burdeau v. McDowell | 99820 | unverified | True | field_i unverified |
| Chatrie v. United States | 11349205 | good_law | False | expected_citation_found=false |
| Chiaverini v. City of Napoleon | 11066663 | unverified | True | field_i unverified |
| Culley v. Marshall | 11066685 | unverified | True | field_i unverified |
| Egbert v. Boule | 6347905 | unverified | True | field_i unverified |
| G. M. Leasing Corp. v. United States | 9426638 | unverified | True | field_i unverified |
| Gonzalez v. Trevino | 11066659 | unverified | True | field_i unverified |
| Heien v. North Carolina | 9805193 | good_law | False | expected_citation_found=false |
| Horton v. California | 9432041 | good_law | True | party-name-miss |
| Imbler v. Pachtman | 9426281 | unverified | True | field_i unverified |
| Kolender v. Lawson | 9429183 | good_law | True | party-name-miss |
| Nieves v. Bartlett | 9226038 | unverified | True | field_i unverified |
| Rehberg v. Paulk | 626447 | unverified | True | field_i unverified |
| Sorrells v. United States | 101997 | good_law | True | party-name-miss |
| Thompson v. Clark | 6329458 | unverified | True | field_i unverified |
| Timbs v. Indiana | 9888039 | unverified | True | field_i unverified |
| United States v. Al-Azzawy | 465254 | unverified | True | field_i unverified |
| United States v. Bajakajian | 9433683 | unverified | True | field_i unverified |
| United States v. Nora | 2722177 | unverified | True | field_i unverified |
| United States v. Rideau | 587275 | good_law | False | expected_citation_found=false |
| United States v. United States District Court (Keith) | 9424952 | unverified | True | field_i unverified |
| United States v. Vaneaton | 9487908 | unverified | True | field_i unverified |
| United States v. Verdugo-Urquidez | 9431925 | unverified | True | field_i unverified |
| Weeks v. United States | 98094 | good_law | True | party-name-miss |

Residue classes: **21** field_i unverified (breadth-marked P4-10 currency/split promotions — the schema categorically forbids `verified` while field_i is unverified, which P4-16(a) itself directs them to keep); **4** party-name-miss (Horton/Kolender/Sorrells/Weeks — the distinguishing surname is absent from the lead-opinion body, which for these older cases carries no caption/syllabus; grep-confirmed 0 occurrences — "not found != fabricated"); **3** expected_citation_found=false (Chatrie/Heien/Rideau — schema allOf[1] blocks `verified`). 0 cache-miss (all 29 cache files present).

## (iii) P4-18(iii) escalation fixes

**August + Sandoval `holding:` weight-label leaks** (author-owned frontmatter; the leak surfaced only via the generated Case Index projection, LINT-16 rows 461/575). Reworded the label text OUT of the holding string, meaning preserved:
- `United States v. August`: dropped `(Binding in-circuit — 5th Cir.; Persuasive (outside circuit)) ` prefix.
- `United States v. Sandoval`: dropped `(Binding in-circuit — 9th Cir.) ` prefix.

FIN-INDEX regen (build_case_index.py, out of scope) re-runs at campaign end (P4-17(b)); the LINT-16 index carve-out keeps the stale generated rows quiet until then.

**Standing `Historical foil.` FP** — `_common.weight_label_in_cell`: the bare-word `Historical` rule fired on the Key-cases role prefix. Added a guard (`_historical_label_leak` + `_HISTORICAL_DESCRIPTIVE_TAIL_RE`): `Historical` counts as an A8 tier-6 label only standalone or dash/period/paren-annotated; a lowercase-word continuation (`Historical foil`, `Historical facts`, `Historical origin`) is descriptive prose. The real leak forms (bare `Historical`, the em-dash `Historical — ...` fixture) still fire. New pass fixture `lint-16-historical-role-pass.md`. lint16 self-test 16/16 PASS; lint4 full run 0.

## Scope note — `_schema.json` identity_method enum (out of the literal file list)

RULING P4-18(i) directs `identity_method="p4-cache-text-check"` AND the task requires lint13=0. The committed schema enum did not list that value, so the two are satisfiable only by extending the enum — the exact pattern by which `panel-cluster-rekey` was added for P4-10. Made the minimal one-line addition; `ingest.py:9019` enum self-check stays consistent; no projector reads identity_method; lint13 + its self-test stay green. Flagged because `_overhaul2/lake/_schema.json` was not in the enumerated write-scope; the edit is ruling-mandated, not discretionary.

## Concurrent-tree caveat

The shared working tree carries ~252 concurrent sibling-lane modifications (other campaign waves). CAMP-A1b's footprint is exactly: `_schema.json`, `Riley v. California.json`, `Riley v. California.md` (lake.status line only — a co-located pre-existing LINT-11 P4-16(d) Sources reword in that file's diff is NOT mine and was left intact), `United States v. August.md` + `United States v. Sandoval.md` (holding line only), `scripts/lint/lint14_pagerecord.py`, `scripts/lint/_common.py`, and 2 new fixtures.

## Handoffs (P4-18(iii) P5 items, unchanged)

- Luke-Wilson folded-alias deviation ACCEPTED (P4-18(iii)); no action here.
- 5th-Cir. Wilson caption-collision + coverage-ledger regen-durability -> P5 handoff (R12 data-hygiene); out of CAMP-A1b scope.
