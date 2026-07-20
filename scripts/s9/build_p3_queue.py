#!/usr/bin/env python3
"""P3 queue + packet builder (orchestrator ledger plumbing).

Joins the 487 fix-owed adjudications (UPHELD/MODIFIED with no FIXED fix) to
their findings + panel-vote extracts, classifies each item (class label from
the adjudicated holding; QF sub-class from the P2-QF-RULING tag), and
partitions into disjoint-write packets:

  REG  — registry.yaml items, one packet per shard (SERIAL: same file)
  LAKE — lake-record items, packets of <=14, a lake file never split
  HM   — all home-mirror items + any queue item on a mirror doctrine page
         (single packet: overlapping write scopes)
  CONT — remaining content items, packets of <=12, a file never split

Outputs: _run/s9/p3/P3-QUEUE.jsonl, _run/s9/p3/packets/P3-PKT-*.jsonl,
_run/s9/p3/P3-PACKET-INDEX.json. Deterministic; safe to re-run (rebuilds).
"""
import json, re, os, collections, glob

RUN = "_run/s9"
P3 = f"{RUN}/p3"
PKT = f"{P3}/packets"


def load(path):
    with open(path) as fh:
        return [json.loads(l) for l in fh if l.strip()]


def final_loop_verdict(fx):
    loops = fx.get("loops") or []
    if loops:
        return (loops[-1].get("re_review") or {}).get("verdict")
    s = fx.get("status")
    return s if s in ("FIXED", "NOT-FIXED") else None


def classify(adj):
    h = " ".join(adj.get("adjudicated_holding") or [])
    m = re.search(r"class=([a-z0-9-]+)", h)
    if m:
        return m.group(1)
    if "P2-QF-RULING (i)" in h or "P2-QF-RULING(i)" in h:
        return "qf-harvest-artifact"
    if "P2-QF-RULING (iii)" in h:
        return "qf-pin-drift"
    if "P2-QF-RULING" in h:
        return "qf-other"
    return "individual"


def main():
    finds = {f["id"]: f for f in load(f"{RUN}/findings.jsonl")}
    adjs = load(f"{RUN}/adjudications.jsonl")
    fixes = load(f"{RUN}/fixes.jsonl")
    votes = collections.defaultdict(list)
    for v in load(f"{RUN}/votes.jsonl"):
        if v.get("finding_id"):
            votes[v["finding_id"]].append(v)

    fixed = {fx.get("finding_id") for fx in fixes if final_loop_verdict(fx) == "FIXED"}
    queue = []
    for a in adjs:
        fid = a.get("finding_id")
        if a.get("verdict") not in ("UPHELD", "MODIFIED") or fid in fixed:
            continue
        f = finds.get(fid)
        if not f:
            continue  # orphan refs are P5 tidy, not P3
        vex = []
        for v in votes[fid]:
            vex.append({k: v.get(k) for k in
                        ("lane", "verdict", "reasons", "suggested_tightening",
                         "residual_risks") if v.get(k)})
        queue.append({
            "finding_id": fid,
            "verdict": a["verdict"],
            "p3_class": classify(a),
            "object": f["object"],
            "object_class": f["object_class"],
            "severity": f.get("severity"),
            "dimension": f.get("dimension"),
            "locator": f.get("locator"),
            "problem": f.get("problem"),
            "proposed_fix": f.get("proposed_fix"),
            "adjudicated_holding": a.get("adjudicated_holding"),
            "adjudication_rule": (a.get("refute_tally") or {}).get("rule"),
            "needs_cl": bool(a.get("needs_cl") or f.get("needs_cl")),
            "votes": vex,
        })

    os.makedirs(PKT, exist_ok=True)
    for stale in glob.glob(f"{PKT}/P3-PKT-*.jsonl"):
        os.remove(stale)
    with open(f"{P3}/P3-QUEUE.jsonl", "w") as fh:
        for q in sorted(queue, key=lambda q: q["finding_id"]):
            fh.write(json.dumps(q, sort_keys=True) + "\n")

    # ---- partition ------------------------------------------------------
    mirror_re = re.compile(
        r"(Fruits|Exclusionary Rule|Qualified Immunity|Suing (State|Federal)"
        r"|Good.Faith)", re.I)
    reg, lake, hm, cont = [], [], [], []
    for q in queue:
        o = q["object"]
        if o.startswith("_overhaul2/points/registry"):
            reg.append(q)
        elif o.startswith("_overhaul2/lake/"):
            lake.append(q)
        elif q["p3_class"] == "home-mirror" or mirror_re.search(os.path.basename(o)):
            hm.append(q)
        else:
            cont.append(q)

    packets = {}
    # REG: one packet per shard anchor (serial lane)
    for q in reg:
        shard = q["object"].split("#")[-1] if "#" in q["object"] else "shard-0"
        packets.setdefault(f"R-{shard}", []).append(q)

    def pack_by_file(items, prefix, cap):
        byfile = collections.defaultdict(list)
        for q in items:
            byfile[q["object"]].append(q)
        cur, n = [], 1
        for fpath in sorted(byfile):
            if cur and len(cur) + len(byfile[fpath]) > cap:
                packets[f"{prefix}{n:02d}"] = cur
                cur, n = [], n + 1
            cur.extend(byfile[fpath])
        if cur:
            packets[f"{prefix}{n:02d}"] = cur

    pack_by_file(lake, "L", 14)
    if hm:
        packets["HM"] = hm
    pack_by_file(cont, "C", 12)

    index = {}
    for name in sorted(packets):
        rows = packets[name]
        with open(f"{PKT}/P3-PKT-{name}.jsonl", "w") as fh:
            for q in rows:
                fh.write(json.dumps(q, sort_keys=True) + "\n")
        index[name] = {
            "items": len(rows),
            "files": sorted({q["object"] for q in rows}),
            "classes": dict(collections.Counter(q["p3_class"] for q in rows)),
            "needs_cl": sum(q["needs_cl"] for q in rows),
        }
    with open(f"{P3}/P3-PACKET-INDEX.json", "w") as fh:
        json.dump({"queue": len(queue), "packets": index}, fh, indent=1, sort_keys=True)

    print(json.dumps({
        "queue": len(queue),
        "families": {"REG": len(reg), "LAKE": len(lake), "HM": len(hm), "CONT": len(cont)},
        "packets": {k: v["items"] for k, v in index.items()},
        "classes": dict(collections.Counter(q["p3_class"] for q in queue)),
    }, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
