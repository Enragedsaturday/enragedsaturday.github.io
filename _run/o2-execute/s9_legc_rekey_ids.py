import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "scripts", "s2"))
import ingest
repo_root=os.getcwd()
pool_root=os.environ.get("CSSI_LAKE_ROOT", ingest.DEFAULT_CSSI_LAKE_ROOT)
paths=ingest.LakePaths(repo_root, pool_root)
manifest=ingest.ManifestStore(paths.manifest)
EXCLUDE={"not_found","fabrication_suspected","verified_off_cl"}
ALLOW=set(ingest.REKEY_LEAD_ALLOW_STATUSES)
rows=[json.loads(l) for l in open("_run/s9/miskey-sweep.jsonl") if l.strip()]
nolead=[r for r in rows if r.get("flag")=="no-lead-opinion"]
ids=[]
for r in nolead:
    raw=r["record"]; g=raw[:-5] if raw.endswith(".json") else raw
    rid=manifest.resolve_record_id(g) or manifest.resolve_record_id(raw) or g
    row=manifest.by_record_id.get(rid)
    if not row: continue
    st=row.get("status")
    rec=ingest.load_case_record(paths,rid); ident=(rec or {}).get("identity") or {}
    if ident.get("lead_opinion_id") is not None: continue  # already landed
    if st in EXCLUDE or st not in ALLOW: continue
    if not ident.get("cluster_id"): continue
    ids.append(rid)
# emit newline-delimited
sys.stdout.write("\n".join(ids))
