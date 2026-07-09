#!/usr/bin/env python3
"""S9->S2 builder token-leg driver: stage clusters + fetch opinion texts into the
pool cache through ingest.py's OWN CourtListenerClient (its pacing/budget/journal/
call-log). Read-only w.r.t. the lake (writes only pool cache/http + cache/text).
The re-key MUTATION is NOT here -- it goes through the sanctioned
`--rekey-cluster-panel` CLI. Constructed exactly as main() builds a live surface.
Usage:
  driver.py stage-clusters 117863 218926
  driver.py fetch-texts 9441559,9434613,...
  driver.py verify-cluster-cites 117863=512_U.S._452 218926=564_U.S._229 131160=540_U.S._544
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "scripts", "s2"))
import ingest

MODE = sys.argv[1]
repo_root = os.getcwd()
pool_root = os.environ.get("CSSI_LAKE_ROOT", ingest.DEFAULT_CSSI_LAKE_ROOT)
paths = ingest.LakePaths(repo_root, pool_root)
paths.ensure()
manifest = ingest.ManifestStore(paths.manifest)
run_id = manifest.ensure_build_id(None)
journal = ingest.Journal(os.path.join(paths.journal, "s2-ingest-%s.jsonl" % run_id), run_id)
token = ingest.read_token()
budget = ingest.CallBudget(max_calls=40)
client = ingest.CourtListenerClient(
    paths=paths, token=token, token_fingerprint=ingest.sha256_text(token)[:12],
    journal=journal, budget=budget,
    rate=ingest.TokenBucket(rate_per_minute=14, capacity=1),
    hourly=ingest.HourlyGuard(max_per_hour=900), run_id=run_id,
)
journal.append(step="s9-s2-cache-repair", status="driver-start", mode=MODE,
               lane="o2-opus-xhigh", model="claude-opus-4-8",
               consumer=ingest.CONSUMER_IDENTITY,
               budget=budget.snapshot(estimated_remaining="s9-s2 workorder; <=40"))

def net(): return budget.session_calls

if MODE == "stage-clusters":
    for cid in sys.argv[2:]:
        before = net()
        cl = client.get_cluster(int(cid), record_id="S9-S2-stage", step="s9.stage.cluster")
        after = net()
        p = client.cache_path(client.build_url("clusters/%s" % int(cid)))
        print(json.dumps({"cluster": int(cid), "network_calls": after-before,
                          "cached": os.path.exists(p),
                          "case_name": cl.get("case_name"),
                          "date_filed": cl.get("date_filed"),
                          "cites": [c.get("cite") for c in (cl.get("citations") or [])],
                          "sub_opinions": len(cl.get("sub_opinions") or [])}))
elif MODE == "verify-cluster-cites":
    for spec in sys.argv[2:]:
        cid, want = spec.split("=", 1)
        want = want.replace("_", " ")
        p = client.cache_path(client.build_url("clusters/%s" % int(cid)))
        if not os.path.exists(p):
            print(json.dumps({"cluster": int(cid), "cached": False})); continue
        cl = json.load(open(p))
        cites = [c.get("cite") for c in (cl.get("citations") or [])]
        keys = {ingest.citation_compare_key(c) for c in cites}
        lead, subs = ingest.harmonized_lead_from_cluster(cl, int(cid))
        print(json.dumps({"cluster": int(cid), "expect_cite": want,
                          "present": ingest.citation_compare_key(want) in keys,
                          "cites": cites, "harmonized_lead": lead,
                          "date_filed": cl.get("date_filed"),
                          "case_name": cl.get("case_name")}))
elif MODE == "fetch-texts":
    ids = [int(x) for x in sys.argv[2].split(",") if x.strip()]
    src = sys.argv[3] if len(sys.argv) > 3 else "cluster.sub_opinions[]"
    for oid in ids:
        before = net()
        ref = client.opinion_ref(oid, src, context={"leg": "s9-s2-cache-repair"})
        text = client.text_for_opinion(ref, record_id="S9-S2-textfetch", step="s9.text")
        after = net()
        tp = os.path.join(paths.text, "%s.txt" % oid)
        head = ""
        if os.path.exists(tp):
            with open(tp, encoding="utf-8") as f:
                head = f.read(160)
        print(json.dumps({"opinion": oid, "network_calls": after-before,
                          "text_bytes": os.path.getsize(tp) if os.path.exists(tp) else None,
                          "head": head[:120]}, ensure_ascii=False))
else:
    raise SystemExit("unknown mode %s" % MODE)

journal.append(step="s9-s2-cache-repair", status="driver-end", mode=MODE,
               lane="o2-opus-xhigh", model="claude-opus-4-8",
               budget=budget.snapshot())
print("SESSION_NETWORK_CALLS=%d" % budget.session_calls)
