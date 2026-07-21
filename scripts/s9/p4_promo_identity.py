#!/usr/bin/env python3
"""P4 promotion workorder — cluster identity fetch loop (builder lane)."""
import json, os, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOKEN = open(os.path.expanduser("~/.config/cssi/cl-token")).read().strip()
IDS = [112448,587275,9231236,10600071,110926,4591916,118234,10600097,101997,108581,109387,626447,112894,110885,99820,112382,6475794,98094,2722177,465254,691388,2680439,6457347,10600074,2760668,112904,112156,109579,10881683]
out = {}
for cid in IDS:
    url = (f"https://www.courtlistener.com/api/rest/v4/clusters/{cid}/"
           "?fields=id,case_name,citations,date_filed,precedential_status")
    req = urllib.request.Request(url, headers={"Authorization": f"Token {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            out[cid] = json.load(r)
    except Exception as e:
        out[cid] = {"error": str(e)[:150]}
    time.sleep(1.2)
json.dump(out, open(os.path.join(ROOT, "_run/s9/p4/out/PROMO-identity-fetch.json"), "w"), indent=1)
ok = sum(1 for v in out.values() if "error" not in v)
print(f"fetched {ok}/{len(IDS)}")
