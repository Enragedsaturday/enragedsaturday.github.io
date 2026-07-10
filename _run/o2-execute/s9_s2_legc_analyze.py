#!/usr/bin/env python3
"""Leg C dry-run analysis (NO network): worklist, statuses, cache state, thread-P coverage.
Usage: python3 s9_s2_legc_analyze.py
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "scripts", "s2"))
import ingest

repo_root = os.getcwd()
pool_root = os.environ.get("CSSI_LAKE_ROOT", ingest.DEFAULT_CSSI_LAKE_ROOT)
paths = ingest.LakePaths(repo_root, pool_root)
manifest = ingest.ManifestStore(paths.manifest)

EXCLUDE = {"not_found", "fabrication_suspected", "verified_off_cl"}
ALLOW = set(ingest.REKEY_LEAD_ALLOW_STATUSES)


def http_cached(cluster_id):
    url = ingest.API_BASE + "/clusters/%s/" % int(cluster_id)
    return os.path.exists(os.path.join(paths.http_cache, ingest.sha1_text(url) + ".json")), url


def text_present(oid):
    return os.path.exists(os.path.join(paths.text, "%s.txt" % int(oid)))


# --- worklist from miskey sweep ---
rows = []
with open("_run/s9/miskey-sweep.jsonl", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))

nolead = [r for r in rows if r.get("flag") == "no-lead-opinion"]

buckets = {"eligible": [], "excluded": [], "other_status": [], "unresolved": [], "already_lead": [], "no_cluster": []}
cluster_cached = 0
text_derivable_cached = 0
for r in nolead:
    raw = r["record"]
    rid_guess = raw[:-5] if raw.endswith(".json") else raw
    rid = manifest.resolve_record_id(rid_guess) or manifest.resolve_record_id(raw) or rid_guess
    row = manifest.by_record_id.get(rid)
    if not row:
        buckets["unresolved"].append({"record": raw, "rid_guess": rid_guess})
        continue
    status = row.get("status")
    rec = ingest.load_case_record(paths, rid)
    ident = (rec or {}).get("identity") or {}
    cid = ident.get("cluster_id")
    lead = ident.get("lead_opinion_id")
    entry = {"record": raw, "rid": rid, "status": status, "cluster_id": cid, "lead_opinion_id": lead,
             "sweep_cluster": r.get("cluster")}
    if lead is not None:
        buckets["already_lead"].append(entry)
        continue
    if status in EXCLUDE:
        buckets["excluded"].append(entry)
        continue
    if status not in ALLOW:
        buckets["other_status"].append(entry)
        continue
    if not cid:
        buckets["no_cluster"].append(entry)
        continue
    cached, _ = http_cached(cid)
    entry["cluster_cached"] = cached
    if cached:
        cluster_cached += 1
        try:
            cl = json.load(open(os.path.join(paths.http_cache, ingest.sha1_text(ingest.API_BASE + "/clusters/%s/" % int(cid)) + ".json")))
            hlead, subs = ingest.harmonized_lead_from_cluster(cl, int(cid))
            entry["harmonized_lead"] = hlead
            entry["text_present"] = bool(hlead) and text_present(hlead)
            if entry["text_present"]:
                text_derivable_cached += 1
        except Exception as e:
            entry["cache_err"] = str(e)
    buckets["eligible"].append(entry)

# --- thread-P coverage baseline: 609 case items ---
tp = json.load(open("_run/s9/thread-P.json"))
case_items = [it for it in tp["items"] if it.get("kind") == "case"]
covered = 0
missing = []
no_record = 0
for it in case_items:
    lk = it.get("lake") or {}
    lakeid = lk.get("record_id") if isinstance(lk, dict) else lk
    rid = lakeid if lakeid and manifest.by_record_id.get(lakeid) else (manifest.resolve_record_id(lakeid) if lakeid else None)
    if not rid:
        no_record += 1
        continue
    rec = ingest.load_case_record(paths, rid)
    ident = (rec or {}).get("identity") or {}
    lead = ident.get("lead_opinion_id")
    if lead is not None and text_present(lead):
        covered += 1
    else:
        missing.append({"p_id": it.get("p_id"), "lake": lakeid, "rid": rid,
                        "status": (manifest.by_record_id.get(rid) or {}).get("status"),
                        "lead": lead})

print(json.dumps({
    "nolead_rows": len(nolead),
    "buckets": {k: len(v) for k, v in buckets.items()},
    "cluster_already_cached": cluster_cached,
    "text_already_present_for_cached": text_derivable_cached,
    "threadP_cases": len(case_items),
    "threadP_covered_now": covered,
    "threadP_missing_now": len(missing),
    "threadP_no_record": no_record,
}, indent=2))

# dump full worklist + missing to files for the driver
with open("_run/o2-execute/s9_legc_worklist.json", "w") as f:
    json.dump(buckets, f, indent=1)
with open("_run/o2-execute/s9_legc_threadP_missing.json", "w") as f:
    json.dump({"missing": missing, "no_record": no_record}, f, indent=1)
print("wrote _run/o2-execute/s9_legc_worklist.json + s9_legc_threadP_missing.json")
