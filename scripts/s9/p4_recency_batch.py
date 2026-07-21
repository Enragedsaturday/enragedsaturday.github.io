#!/usr/bin/env python3
"""S9 P4 I1 — per-category recency lanes (R7.1): run the consolidated
cites:(opinion-ids) AND filed_after:2026-07-04 queries from
_run/s9/p4/recency-queries.json via CL REST v4. Builder-lane (codex-invoked),
token from ~/.config/cssi/cl-token, paced, journaled.

Output: _run/s9/p4/out/I1-recency-results.jsonl (one row per category)
"""
import json, os, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QUERIES = os.path.join(ROOT, "_run/s9/p4/recency-queries.json")
OUT = os.path.join(ROOT, "_run/s9/p4/out/I1-recency-results.jsonl")
LOG = os.path.join(ROOT, "_run/s9/p4/p4-cl-calls.log")
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
BASE = "https://www.courtlistener.com/api/rest/v4/search/"
FIELDS = "caseName,court,dateFiled,citation,docketNumber,cluster_id,status"

def main():
    token = open(TOKEN_PATH).read().strip()
    lanes = json.load(open(QUERIES))
    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try:
                done.add(json.loads(line)["category"])
            except Exception:
                pass
    n_req = 0
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(OUT, "a") as out:
        for lane in lanes:
            cat = lane["category"]
            if cat in done:
                continue
            row = {"row": "p4.i1recency.v1", "category": cat,
                   "lane": "s2-builder-codex-rest", "model": "gpt-5.5",
                   "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            q = lane.get("query")
            if not q or lane.get("no_lane"):
                row["status"] = "no-lane"
                row["reason"] = lane.get("notes") or lane.get("reason")
                out.write(json.dumps(row) + "\n")
                continue
            # filed_after must be an API PARAM — embedded `filed_after:` in q is
            # not a q operator and silently zeroes the query (probed 2026-07-21).
            q_cites = q.split(" AND filed_after")[0].strip()
            params = {"type": "o", "q": q_cites, "filed_after": "2026-07-04",
                      "order_by": "dateFiled desc", "fields": FIELDS}
            url = BASE + "?" + urllib.parse.urlencode(params)
            req = urllib.request.Request(url, headers={"Authorization": f"Token {token}"})
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = json.load(r)
                row["count"] = data.get("count")
                row["results"] = [{k: h.get(k) for k in
                                   ("caseName", "court", "dateFiled", "citation",
                                    "docketNumber", "cluster_id", "status")}
                                  for h in data.get("results", [])[:20]]
            except Exception as e:
                row["error"] = str(e)[:300]
            n_req += 1
            out.write(json.dumps(row) + "\n")
            out.flush()
            time.sleep(4.5)
    with open(LOG, "a") as lg:
        lg.write(f"{t0} P4 I1 recency batch (builder lane, codex-invoked): "
                 f"{n_req} requests over {len(lanes)} categories -> I1-recency-results.jsonl\n")
    print(f"DONE: {n_req} requests")

if __name__ == "__main__":
    main()
