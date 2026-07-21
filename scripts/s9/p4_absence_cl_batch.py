#!/usr/bin/env python3
"""S9 P4 I4 — absence-claim CL direction (R7.4).

Runs the batched CL full-text query list for every absence claim in
_run/s9/p4/absence-claims.jsonl (two-direction search, CL leg). Executed by the
CODEX BUILDER LANE (owns the token — S1 A1/L4'); token read from
~/.config/cssi/cl-token, never printed. Paced ~x4.5s/request (< 1,000/hr),
resumable (skips claim_ids already in the output), journaled.

Usage: python3 scripts/s9/p4_absence_cl_batch.py [--limit N]
Output: _run/s9/p4/out/I4-CL-results.jsonl   (one row per claim)
        _run/s9/p4/p4-cl-calls.log           (appended batch journal)
"""
import json, os, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLAIMS = os.path.join(ROOT, "_run/s9/p4/absence-claims.jsonl")
OUT = os.path.join(ROOT, "_run/s9/p4/out/I4-CL-results.jsonl")
LOG = os.path.join(ROOT, "_run/s9/p4/p4-cl-calls.log")
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
BASE = "https://www.courtlistener.com/api/rest/v4/search/"
PACE_SECONDS = 4.5
FIELDS = "caseName,court,dateFiled,citation,docketNumber,cluster_id,status"

def read_token():
    with open(TOKEN_PATH) as f:
        return f.read().strip()

def cl_search(q, token, filed_after=None, num=5):
    params = {"type": "o", "q": q, "order_by": "dateFiled desc",
              "fields": FIELDS}
    if filed_after:
        params["filed_after"] = filed_after
    url = BASE + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"Authorization": f"Token {token}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.load(r)
    hits = [{k: h.get(k) for k in ("caseName", "court", "dateFiled",
                                   "citation", "docketNumber", "cluster_id", "status")}
            for h in data.get("results", [])[:num]]
    return {"count": data.get("count"), "top": hits}

def build_queries(row):
    """Each suggested term runs UNQUOTED as its own query (CL tokenizes; quoted
    multi-word phrases over-restrict — smoke-tested 2026-07-21). Negative-claim
    classes add a recency leg on the first term (has the landscape moved?)."""
    terms = (row.get("search_terms_suggested") or [row["claim_text"][:120]])[:2]
    queries = [{"q": t, "filed_after": None, "leg": f"full-{i}"}
               for i, t in enumerate(terms)]
    if row.get("class") in ("split", "open-question", "not-decided", "no-court-has",
                            "first-impression"):
        queries.append({"q": terms[0], "filed_after": "2025-01-01", "leg": "recent"})
    return queries

def main():
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    token = read_token()
    done = set()
    if os.path.exists(OUT):
        with open(OUT) as f:
            for line in f:
                try:
                    done.add(json.loads(line)["claim_id"])
                except Exception:
                    pass
    rows = [json.loads(l) for l in open(CLAIMS) if l.strip()]
    todo = [r for r in rows if r["claim_id"] not in done]
    if limit:
        todo = todo[:limit]
    n_req = 0
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(OUT, "a") as out:
        for i, row in enumerate(todo):
            result = {"row": "p4.i4cl.v1", "claim_id": row["claim_id"],
                      "class": row.get("class"), "file": row.get("file"),
                      "queries": [], "lane": "s2-builder-codex-rest",
                      "model": "gpt-5.5", "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            for spec in build_queries(row):
                try:
                    res = cl_search(spec["q"], token, spec["filed_after"])
                    result["queries"].append({"q": spec["q"], "leg": spec["leg"],
                                              "filed_after": spec["filed_after"], **res})
                except Exception as e:
                    result["queries"].append({"q": spec["q"], "leg": spec["leg"],
                                              "error": str(e)[:200]})
                n_req += 1
                time.sleep(PACE_SECONDS)
            out.write(json.dumps(result) + "\n")
            out.flush()
            if (i + 1) % 20 == 0:
                print(f"[{i+1}/{len(todo)}] {n_req} requests", flush=True)
    with open(LOG, "a") as lg:
        lg.write(f"{t0} P4 I4 CL batch (builder lane, codex-invoked): {len(todo)} claims, "
                 f"{n_req} requests, paced {PACE_SECONDS}s, output I4-CL-results.jsonl\n")
    print(f"DONE: {len(todo)} claims, {n_req} requests")

if __name__ == "__main__":
    main()
