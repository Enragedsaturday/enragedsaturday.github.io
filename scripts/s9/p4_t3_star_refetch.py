#!/usr/bin/env python3
"""S9 P4 T3-REOPEN remedy — star-pagination re-fetch (builder lane, codex-invoked).

For each case named in _run/s9/p4/out/T3-REOPEN-findings.jsonl: fetch the lead
opinion's html_with_citations from CL REST v4 (token ~/.config/cssi/cl-token),
cache to _run/s9/p4/star-refetch/<opinion_id>.html, and report which asserted
bound-volume pins are covered by live star pagination. Paced 4.5s, resumable.

Output: _run/s9/p4/out/T3-STAR-REFETCH.jsonl (one row per finding)
"""
import json, os, re, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FINDINGS = os.path.join(ROOT, "_run/s9/p4/out/T3-REOPEN-findings.jsonl")
OUT = os.path.join(ROOT, "_run/s9/p4/out/T3-STAR-REFETCH.jsonl")
CACHE = os.path.join(ROOT, "_run/s9/p4/star-refetch")
LOG = os.path.join(ROOT, "_run/s9/p4/p4-cl-calls.log")
TOKEN = open(os.path.expanduser("~/.config/cssi/cl-token")).read().strip()
LAKE = os.path.join(ROOT, "_overhaul2/lake/cases")

os.makedirs(CACHE, exist_ok=True)

def lake_index():
    idx = {}
    for fn in os.listdir(LAKE):
        if not fn.endswith(".json"):
            continue
        try:
            r = json.load(open(os.path.join(LAKE, fn)))
        except Exception:
            continue
        ident = r.get("identity", {})
        name = (ident.get("case_name") or "").lower()
        idx[name] = {"lead": ident.get("lead_opinion_id"),
                     "cluster": ident.get("cluster_id"), "file": fn}
    return idx

def fetch_opinion(opid):
    path = os.path.join(CACHE, f"{opid}.html")
    if os.path.exists(path) and os.path.getsize(path) > 100:
        return open(path, encoding="utf-8", errors="replace").read(), False
    url = f"https://www.courtlistener.com/api/rest/v4/opinions/{opid}/?fields=html_with_citations"
    req = urllib.request.Request(url, headers={"Authorization": f"Token {TOKEN}"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.load(r)
    html = data.get("html_with_citations") or ""
    open(path, "w", encoding="utf-8").write(html)
    return html, True

STAR_RE = re.compile(r'star-pagination[^>]*>\s*\*?(\d+)|<page-number[^>]*>\s*\*?(\d+)|\*(\d{1,4})\b')

def star_pages(html):
    pages = set()
    for m in re.finditer(r'class="star-pagination"[^>]*>\s*\*?(\d+)', html):
        pages.add(int(m.group(1)))
    for m in re.finditer(r'<span class="citation[^"]*" [^>]*>\s*\*(\d+)', html):
        pages.add(int(m.group(1)))
    if not pages:  # fallback: bare *NNN tokens in text
        for m in re.finditer(r'\*(\d{1,4})\b', html):
            pages.add(int(m.group(1)))
    return pages

def main():
    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try:
                done.add(json.loads(line)["finding_line"])
            except Exception:
                pass
    idx = lake_index()
    rows = [json.loads(l) for l in open(FINDINGS) if l.strip()]
    n_fetch = 0
    t0 = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with open(OUT, "a") as out:
        for i, row in enumerate(rows):
            if i in done:
                continue
            claim = row.get("claim", "")
            evidence = row.get("evidence", "")
            m = re.search(r"slip-only '([^']+)'", claim)
            case_name = (m.group(1) if m else "").strip()
            opid_m = re.search(r'opinion_id=(\d+)', evidence)
            opid = int(opid_m.group(1)) if opid_m else None
            pins = sorted({int(p) for p in
                           re.findall(r'at (\d{1,4})[–\-]?(\d{0,4})', claim)
                           for p in ([p[0]] if not p[1] else [p[0], p[1]])
                           if p and int(p) < 3000})
            if not opid and case_name:
                rec = idx.get(case_name.lower())
                opid = rec.get("lead") if rec else None
            res = {"row": "p4.t3refetch.v1", "finding_line": i,
                   "case_name": case_name, "pins_asserted": pins,
                   "file": row.get("file"), "line": row.get("line"),
                   "lane": "s2-builder-codex-rest", "model": "gpt-5.5"}
            if not opid:
                res["status"] = "no-opinion-id"
                out.write(json.dumps(res) + "\n")
                continue
            try:
                html, fetched = fetch_opinion(opid)
                if fetched:
                    n_fetch += 1
                    time.sleep(4.5)
                pages = star_pages(html)
                res["opinion_id"] = opid
                res["star_page_count"] = len(pages)
                res["pins_covered"] = [p for p in pins if p in pages]
                res["pins_uncovered"] = [p for p in pins if p not in pages]
                res["status"] = ("live-star-covered" if pins and not res["pins_uncovered"]
                                 else "partial" if res["pins_covered"]
                                 else "no-live-star")
            except Exception as e:
                res["status"] = "error"
                res["error"] = str(e)[:200]
            out.write(json.dumps(res) + "\n")
            out.flush()
    with open(LOG, "a") as lg:
        lg.write(f"{t0} P4 T3 star-refetch (builder lane, codex-invoked): {n_fetch} opinion "
                 f"fetches over {len(rows)} findings -> T3-STAR-REFETCH.jsonl\n")
    print(f"DONE: {len(rows)} findings, {n_fetch} fetches")

if __name__ == "__main__":
    main()
