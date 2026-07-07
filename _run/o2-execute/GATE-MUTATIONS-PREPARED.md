# GATE-MUTATIONS-PREPARED — W6-gate lake/manifest mutations (prepared, NOT executed)

**Lane:** O2 EXECUTE offline micro-repair (`claude-opus-4-8`). **Date:** 2026-07-07.
**Repo:** `/Users/johngalt/Projects/cssi-quartz` · branch `overhaul2/execute` · HEAD at prep `a3a4d36`.
**Status:** PREPARED ONLY. This lane executed **zero** lake/manifest/content writes and **zero** CL
calls. The manifest is a live write-point shared with W6 promotions — the orchestrator applies these
at the W6 gate, serialized against W6, after re-reading the manifest.

Two mutations: **(1)** the `davis--4881258` duplicate-cluster fold (A18 folded-alias) and **(2)** the
`reddick` circuit-label repair `ca5 → ca3`. A third prepared item (Larson official-cite) is an S2-lane
enrich instruction, not a gate lake-write — see `MICRO-REPAIR-REPORT.md §4` +
`_run/o2-execute/larson-web-cites.jsonl`.

Run all commands from the repo root. Each mutation lists: precondition → apply → verify.

---

## Mutation 1 — `united-states-v-davis--4881258` → folded-alias into `United States v. Howard Davis`

**Why.** The frontier stub `united-states-v-davis--4881258` (identity.cluster_id **4881258**, 997 F.3d
191, 4th Cir. 2021) is the SAME CourtListener opinion cluster as the already-authored page record
`United States v. Howard Davis` (cluster **4881258**, lead opinion 4685037, page
`content/cases/United States v. Howard Davis.md`). Minting the stub would double-page the same
decision under a different caption. This is the W5 Davis lesson; it is now caught pre-mint by the new
`cluster-collision` guard (F-R8-13) in `scripts/s6/mint_page.py`. Disposition per **A18 folded-alias**
precedent (S2 spec §A18; packet-A precedent morse/carman/chatrie).

**Mechanism.** The canonical `--apply-alias-folds` path (`scripts/s2/ingest.py::apply_alias_folds`).
Its guards all pass for this row: record is a stub-id (`--` present), status `verified_identity`
(allowed), survivor `United States v. Howard Davis` is in the manifest and is not itself folded.

Prepared input (already written): `_run/o2-execute/davis-fold.jsonl`.

**Precondition (expect both true):**
```bash
python3 - <<'PY'
import json
rec=json.load(open("_overhaul2/lake/cases/united-states-v-davis--4881258.json"))
m=json.load(open("_overhaul2/lake/_manifest.json"))
byid={r["record_id"]:r for r in m["records"]}
assert rec["status"]=="verified_identity" and rec["stub"] is True, rec["status"]
assert rec["identity"]["cluster_id"]==4881258
assert "United States v. Howard Davis" in byid, "survivor page record missing from manifest"
assert byid["United States v. Howard Davis"]["status"]!="folded-alias"
print("precondition OK: davis stub verified_identity, survivor present, cluster 4881258")
PY
```

**Apply:**
```bash
python3 scripts/s2/ingest.py --apply-alias-folds _run/o2-execute/davis-fold.jsonl
# expect stdout: "alias folds applied: 1"
```

**Edit shape (what apply_alias_folds writes — for review):**
- Lake record `_overhaul2/lake/cases/united-states-v-davis--4881258.json`:
  `status` → `folded-alias`; append `provenance.warnings[]`:
  `"folded-alias: subsumed into United States v. Howard Davis (packet-A Group-2); see _manifest.json folded_into + journal s6-dedupe-pointer"`.
  Record is **kept, never deleted** (A18: no silent merges).
- Manifest record (record_id `united-states-v-davis--4881258`): `status` → `folded-alias`,
  add `folded_into` = `"United States v. Howard Davis"`, add `fold_provenance` block, bump
  `last_record_write`.
- Journal (`manifest.active_journal`): a `s6-dedupe-pointer` event + a `packet-a.alias-fold` event.

**Verify (after apply):**
```bash
python3 - <<'PY'
import json
rec=json.load(open("_overhaul2/lake/cases/united-states-v-davis--4881258.json"))
m=json.load(open("_overhaul2/lake/_manifest.json"))
row=[r for r in m["records"] if r["record_id"]=="united-states-v-davis--4881258"][0]
assert rec["status"]=="folded-alias", rec["status"]
assert row["status"]=="folded-alias" and row.get("folded_into")=="United States v. Howard Davis", row
print("VERIFIED: davis folded-alias ->", row["folded_into"])
PY
# mint of the folded stub must now be refused (wrong-status; folded-alias is not mint-eligible):
python3 scripts/s6/mint_page.py --row united-states-v-davis--4881258 \
  --payload scripts/s6/fixtures/payload-history.md 2>&1 | grep -E "REFUSED \[(wrong-status|cluster-collision)\]"
```

---

## Mutation 2 — `united-states-v-reddick--4527853` circuit label `ca5 → ca3`

**Why.** `United States v. Reddick`, **900 F.3d 636**, is a **Third Circuit** (3d Cir. 2018) decision
(the abandoned-cell-phone / private-search case). The frontier stub mislabels it `identity.circuit =
"ca5"` / `identity.court = "5th Cir."` (and the manifest mirrors those). Identity is otherwise clean
(cluster 4527853, cite 900 F.3d 636, docket 17-41116, party `Henry Franklin Reddick`). Audit
authority: `_run/o2-execute/PRE-W5-AUDIT-REPORT.md:81` — *"reddick circuit mislabel — identity clean
(900 F.3d 636 = 3d Cir. Reddick private-search) but manifest circuit=ca5; should be **ca3**.
Court-repair, not a re-key."* (also line 17). `scripts/s2/project.py::circuit_label("ca3") = "3d
Cir."`, so fixing `circuit` corrects the projected parenthetical.

**Mechanism.** Targeted deterministic edit (idempotent, fail-closed on the current value). The
cache-served `--repair-coa-state-from-cache` tool is **not usable offline** here: cluster 4527853 is
not in the local HTTP cache, so that path would queue-for-lane (needs a CL call the S2 lane owns). The
label is unambiguous (audit-adjudicated), so a targeted edit is the correct offline repair.

**Apply (fail-closed; only rewrites `ca5`/`5th Cir.`):**
```bash
python3 - <<'PY'
import json
def load(p): return json.load(open(p, encoding="utf-8"))
def dump(p,d):
    import os
    t=p+".tmp"; open(t,"w",encoding="utf-8").write(json.dumps(d,indent=2,ensure_ascii=False)+"\n"); os.replace(t,p)

recp="_overhaul2/lake/cases/united-states-v-reddick--4527853.json"
rec=load(recp); ident=rec["identity"]
assert ident.get("circuit") in ("ca5","ca3"), ident.get("circuit")     # fail-closed guard
assert ident.get("court") in ("5th Cir.","3d Cir."), ident.get("court")
ident["circuit"]="ca3"; ident["court"]="3d Cir."
dump(recp, rec)

mp="_overhaul2/lake/_manifest.json"; m=load(mp)
row=[r for r in m["records"] if r["record_id"]=="united-states-v-reddick--4527853"][0]
assert row.get("circuit") in ("ca5","ca3"), row.get("circuit")
row["circuit"]="ca3"; row["court"]="3d Cir."
row["last_record_write"]=__import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
dump(mp, m)
print("APPLIED: reddick circuit ca5->ca3, court 5th Cir.->3d Cir. (record + manifest)")
PY
```
> Note: `court_era` = `"5th Cir. 2018 / 6th Cir. 2020"` in the manifest is the ORIGINAL roster-capture
> provenance (the wiki shorthand was ambiguous); leave it as-is — it documents the capture, and the
> authoritative identity is now the corrected `circuit`/`court`.

**Verify (after apply):**
```bash
python3 - <<'PY'
import sys, json
sys.path.insert(0,"scripts")
from s2.project import circuit_label
rec=json.load(open("_overhaul2/lake/cases/united-states-v-reddick--4527853.json"))
m=json.load(open("_overhaul2/lake/_manifest.json"))
row=[r for r in m["records"] if r["record_id"]=="united-states-v-reddick--4527853"][0]
assert rec["identity"]["circuit"]=="ca3" and rec["identity"]["court"]=="3d Cir.", rec["identity"]
assert row["circuit"]=="ca3" and row["court"]=="3d Cir.", row
assert circuit_label("ca3")=="3d Cir."
assert rec["identity"]["cluster_id"]==4527853 and rec["citations"]["display"]=="900 F.3d 636"
print("VERIFIED: reddick 900 F.3d 636 projects as", circuit_label(rec["identity"]["circuit"]), "(3d Cir. 2018)")
PY
```

---

## Not a gate lake-write (cross-references)

- **Larson official cite** (item 4): S2-lane enrich instruction, not a gate lake-write. Determination +
  two-source evidence in `MICRO-REPAIR-REPORT.md §4`; ready input at `_run/o2-execute/larson-web-cites.jsonl`.
  Preferred path is a `OFFICIAL_SELECTION_NOISE_REPORTERS` code fix + `--enrich-citations` re-run
  (preserves the P.2d parallel); the `--apply-web-cites` line is the no-code alternative.
- **Holcomb** (item 3): **no mutation.** Recommendation = **WATCH / non-page terminal** (opinion 132
  F.4th 1118 withdrawn 2025-09-11, no successor published as of 2026-07; keep the wiki's page-less
  brief-mention). Evidence in `MICRO-REPAIR-REPORT.md §3`.

---
## ORCHESTRATOR DISPOSITIONS (2026-07-07, W6 gate)
- **Mutation 1 (davis fold): APPLIED** — `alias folds applied: 1`, record kept w/ folded-alias status per A18.
- **Mutation 2 (reddick ca5→ca3): REFUTED — NOT APPLIED.** Ground truth fetched at the gate:
  cluster 4527853 → docket 7688717 → **court_id "ca5"**, docket_number 17-41116 (5th Cir. pattern).
  The PRE-W5-AUDIT-REPORT.md:81 flag was itself wrong; W6's on-read identity verification minted
  the page correctly as 5th Cir. (900 F.3d 636, private-search/PhotoDNA, S.D. Tex. appeal). No edit
  made; audit report stands corrected by this note.
