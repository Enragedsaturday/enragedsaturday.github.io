#!/usr/bin/env python3
"""T3 pass (b): second-source pagination harvest (builder lane).
For each distinct opinion in T3-STAR-REFETCH.jsonl with refined status not live-covered,
fetch xml_harvard + html_lawbox + html_columbia; save; report star coverage per pin."""
import json, os, re, time, urllib.request
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOKEN = open(os.path.expanduser("~/.config/cssi/cl-token")).read().strip()
IN = os.path.join(ROOT, "_run/s9/p4/out/T3-STAR-REFETCH-refined.jsonl")
OUT = os.path.join(ROOT, "_run/s9/p4/out/T3-SECOND-SOURCE.jsonl")
CACHE = os.path.join(ROOT, "_run/s9/p4/star-refetch")
rows = [json.loads(l) for l in open(IN)]
need = {}
for r in rows:
    if r.get("refined_status") in ("live-star-covered", "start-page-covered", "covered-mixed"):
        continue
    opid = r.get("opinion_id")
    if opid:
        need.setdefault(opid, []).extend(r.get("pins_asserted") or [])
done = set()
if os.path.exists(OUT):
    for l in open(OUT):
        try: done.add(json.loads(l)["opinion_id"])
        except Exception: pass
out = open(OUT, "a")
n = 0
for opid, pins in need.items():
    if opid in done: continue
    url = f"https://www.courtlistener.com/api/rest/v4/opinions/{opid}/?fields=xml_harvard,html_lawbox,html_columbia"
    req = urllib.request.Request(url, headers={"Authorization": f"Token {TOKEN}"})
    res = {"row": "p4.t3src2.v1", "opinion_id": opid, "pins": sorted(set(p for p in pins if p >= 10))}
    try:
        with urllib.request.urlopen(req, timeout=120) as r2:
            data = json.load(r2)
        pages = set()
        srcs = {}
        for fld in ("xml_harvard", "html_lawbox", "html_columbia"):
            t = data.get(fld) or ""
            if not t: continue
            found = {int(m) for pat in (r'<page-number[^>]*>\s*\*?(\d+)', r'class="star-pagination"[^>]*>\s*\*?(\d+)', r'\*Page (\d+)')
                     for m in re.findall(pat, t)}
            if found:
                srcs[fld] = len(found)
                pages |= found
                open(os.path.join(CACHE, f"{opid}.{fld}.txt"), "w").write(t)
        res["sources"] = srcs
        res["star_pages"] = len(pages)
        real = res["pins"]
        first = min(pages) if pages else None
        res["covered"] = [p for p in real if p in pages] + ([p for p in real if first and p < first] if pages else [])
        res["uncovered"] = [p for p in real if p not in res["covered"]]
        res["status"] = "second-source-covered" if real and not res["uncovered"] else ("partial" if res["covered"] else "no-pagination-any-source")
    except Exception as e:
        res["status"] = "error"; res["error"] = str(e)[:150]
    out.write(json.dumps(res) + "\n"); out.flush()
    n += 1; time.sleep(4.5)
print(f"DONE: {n} opinions fetched")
