#!/usr/bin/env python3
"""S9->S2 builder token-leg C: give Thread-N its missing substrate.

Class: lake records with a cluster_id but lead_opinion_id=None (S6 web-minted
under_review circuit cases + verified_identity residue). For each ELIGIBLE record:
  1. get_cluster(cluster_id)  -- served from cache if cached (0 net), else 1 live call.
     A cluster 404 is captured as a possible identity finding (skip, report).
  2. harmonized_lead_from_cluster -> lead opinion id (fail closed if None).
  3. text_for_opinion(lead)   -- fetches the lead opinion text into the pool if
     absent (1 live call), else served from disk/http cache (0 net).

EXCLUDE (honest skip): status in {not_found, fabrication_suspected, verified_off_cl},
or any whose cluster fetch 404s (reported). Records that ALREADY carry a
lead_opinion_id are skipped as resumable no-ops.

The lead_opinion_id WRITE is NOT here -- it goes through the sanctioned cache-fed
CLI `--rekey-lead-opinion-from-cache` (max_calls=0) after this leg fetches.

ONE serial REST lane, paced by ingest.py's own CourtListenerClient (TokenBucket
14/min, HourlyGuard 900/hr), journaled + call-logged. Checkpoint every 25 records
to a resumable done-list. Budget <= 420 live calls.

Usage:
  s9_s2_leg_c.py fetch-leads [max_calls]
"""
import sys, os, json, urllib.error
sys.path.insert(0, os.path.join(os.getcwd(), "scripts", "s2"))
import ingest

MODE = sys.argv[1] if len(sys.argv) > 1 else "fetch-leads"
MAX_CALLS = int(sys.argv[2]) if len(sys.argv) > 2 else 420

repo_root = os.getcwd()
pool_root = os.environ.get("CSSI_LAKE_ROOT", ingest.DEFAULT_CSSI_LAKE_ROOT)
paths = ingest.LakePaths(repo_root, pool_root)
paths.ensure()
manifest = ingest.ManifestStore(paths.manifest)
run_id = manifest.ensure_build_id(None)
journal = ingest.Journal(os.path.join(paths.journal, "s2-ingest-%s.jsonl" % run_id), run_id)
token = ingest.read_token()
budget = ingest.CallBudget(max_calls=MAX_CALLS)
client = ingest.CourtListenerClient(
    paths=paths, token=token, token_fingerprint=ingest.sha256_text(token)[:12],
    journal=journal, budget=budget,
    rate=ingest.TokenBucket(rate_per_minute=14, capacity=1),
    hourly=ingest.HourlyGuard(max_per_hour=900), run_id=run_id,
)

EXCLUDE = {"not_found", "fabrication_suspected", "verified_off_cl"}
ALLOW = set(ingest.REKEY_LEAD_ALLOW_STATUSES)
DONE_PATH = "_run/o2-execute/s9_legc_done.jsonl"
STATE_PATH = "_run/o2-execute/s9_legc_state.json"

journal.append(step="s9-s2-leg-c", status="driver-start", mode=MODE,
               lane="o2-opus-xhigh", model="claude-opus-4-8",
               consumer=ingest.CONSUMER_IDENTITY,
               budget=budget.snapshot(estimated_remaining="s9-s2 leg C; <=%d" % MAX_CALLS))


def load_done():
    done = {}
    if os.path.exists(DONE_PATH):
        with open(DONE_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    r = json.loads(line)
                    done[r["rid"]] = r
    return done


def append_done(row):
    with open(DONE_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def text_present(oid):
    return os.path.exists(os.path.join(paths.text, "%s.txt" % int(oid)))


def build_worklist():
    rows = []
    with open("_run/s9/miskey-sweep.jsonl", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    nolead = [r for r in rows if r.get("flag") == "no-lead-opinion"]
    work = []
    skipped = []
    for r in nolead:
        raw = r["record"]
        rid_guess = raw[:-5] if raw.endswith(".json") else raw
        rid = manifest.resolve_record_id(rid_guess) or manifest.resolve_record_id(raw) or rid_guess
        row = manifest.by_record_id.get(rid)
        if not row:
            skipped.append({"record": raw, "rid": rid, "reason": "unresolved-in-manifest"})
            continue
        status = row.get("status")
        rec = ingest.load_case_record(paths, rid)
        ident = (rec or {}).get("identity") or {}
        cid = ident.get("cluster_id")
        lead = ident.get("lead_opinion_id")
        if lead is not None:
            skipped.append({"record": raw, "rid": rid, "status": status,
                            "reason": "already-has-lead", "lead": lead})
            continue
        if status in EXCLUDE:
            skipped.append({"record": raw, "rid": rid, "status": status,
                            "reason": "excluded-status"})
            continue
        if status not in ALLOW:
            skipped.append({"record": raw, "rid": rid, "status": status,
                            "reason": "status-not-rekey-eligible"})
            continue
        if not cid:
            skipped.append({"record": raw, "rid": rid, "status": status,
                            "reason": "no-cluster-id"})
            continue
        work.append({"record": raw, "rid": rid, "status": status, "cluster_id": int(cid)})
    return work, skipped


if MODE == "fetch-leads":
    work, skipped = build_worklist()
    done = load_done()
    processed = list(done.values())
    fetched_now = 0
    cache_hits = 0
    text_fetched = 0
    leads_resolved = 0
    not_found_404 = []
    no_lead_derivable = []
    fetch_failures = []
    i_since_ckpt = 0
    n = 0
    for w in work:
        rid = w["rid"]
        if rid in done and done[rid].get("outcome") == "lead-text-ready":
            continue  # resumable skip
        n += 1
        cid = w["cluster_id"]
        # step 1: cluster (cache-hit expected; live fetch if uncached; 404 -> identity finding)
        before = budget.session_calls
        try:
            cluster = client.get_cluster(cid, record_id=rid, step="s9.legc.cluster")
        except urllib.error.HTTPError as exc:
            if getattr(exc, "code", None) == 404:
                rec = {"rid": rid, "cluster_id": cid, "outcome": "cluster-404",
                       "note": "possible identity finding: cluster not on CL"}
                not_found_404.append(rec); append_done(rec)
                journal.append(step="s9-s2-leg-c", status="cluster-404", record_id=rid,
                               cluster_id=cid, lane="o2-opus-xhigh", model="claude-opus-4-8")
                continue
            raise
        except (ingest.IngestInterrupted, ingest.FetchFailed) as exc:
            rec = {"rid": rid, "cluster_id": cid, "outcome": "cluster-fetch-failed",
                   "reason": getattr(exc, "reason", str(exc))}
            fetch_failures.append(rec); append_done(rec)
            journal.append(step="s9-s2-leg-c", status="cluster-fetch-failed", record_id=rid,
                           cluster_id=cid, reason=rec["reason"], lane="o2-opus-xhigh", model="claude-opus-4-8")
            # sustained-failure guard
            if len(fetch_failures) >= 8 and len(fetch_failures) > (fetched_now + text_fetched):
                journal.append(step="s9-s2-leg-c", status="stop-sustained-failures",
                               failures=len(fetch_failures), lane="o2-opus-xhigh", model="claude-opus-4-8")
                break
            continue
        after = budget.session_calls
        if after == before:
            cache_hits += 1
        # step 2: harmonized lead
        try:
            lead, subs = ingest.harmonized_lead_from_cluster(cluster, cid)
        except ValueError as exc:
            rec = {"rid": rid, "cluster_id": cid, "outcome": "no-lead-derivable",
                   "reason": "unparsable sub_opinion: %s" % exc}
            no_lead_derivable.append(rec); append_done(rec)
            continue
        if lead is None:
            rec = {"rid": rid, "cluster_id": cid, "outcome": "no-lead-derivable",
                   "reason": "cluster carries no sub_opinion"}
            no_lead_derivable.append(rec); append_done(rec)
            continue
        leads_resolved += 1
        # step 3: lead opinion text into the pool
        had_text = text_present(lead)
        tbefore = budget.session_calls
        try:
            ref = client.opinion_ref(lead, "cluster.sub_opinions[]", context={"leg": "s9-s2-leg-c", "cluster_id": cid})
            text = client.text_for_opinion(ref, record_id=rid, step="s9.legc.text")
        except urllib.error.HTTPError as exc:
            rec = {"rid": rid, "cluster_id": cid, "lead": lead, "outcome": "opinion-http-%s" % getattr(exc, "code", "err")}
            fetch_failures.append(rec); append_done(rec)
            journal.append(step="s9-s2-leg-c", status="opinion-fetch-failed", record_id=rid,
                           cluster_id=cid, opinion_id=lead, http=getattr(exc, "code", None),
                           lane="o2-opus-xhigh", model="claude-opus-4-8")
            continue
        except (ingest.IngestInterrupted, ingest.FetchFailed) as exc:
            rec = {"rid": rid, "cluster_id": cid, "lead": lead, "outcome": "opinion-fetch-failed",
                   "reason": getattr(exc, "reason", str(exc))}
            fetch_failures.append(rec); append_done(rec)
            journal.append(step="s9-s2-leg-c", status="opinion-fetch-failed", record_id=rid,
                           cluster_id=cid, opinion_id=lead, reason=rec["reason"],
                           lane="o2-opus-xhigh", model="claude-opus-4-8")
            if budget.exhausted():
                journal.append(step="s9-s2-leg-c", status="stop-budget-exhausted",
                               lane="o2-opus-xhigh", model="claude-opus-4-8")
                break
            if len(fetch_failures) >= 8 and len(fetch_failures) > (fetched_now + text_fetched):
                journal.append(step="s9-s2-leg-c", status="stop-sustained-failures",
                               failures=len(fetch_failures), lane="o2-opus-xhigh", model="claude-opus-4-8")
                break
            continue
        tafter = budget.session_calls
        live = tafter - tbefore
        if live > 0:
            text_fetched += 1
        rec = {"rid": rid, "cluster_id": cid, "lead": lead, "outcome": "lead-text-ready",
               "text_bytes": os.path.getsize(os.path.join(paths.text, "%s.txt" % lead)),
               "text_was_present": had_text, "live_calls": live}
        processed.append(rec); append_done(rec)
        done[rid] = rec
        i_since_ckpt += 1
        if i_since_ckpt >= 25:
            with open(STATE_PATH, "w") as f:
                json.dump({"processed_this_run": n, "budget": budget.snapshot(),
                           "text_fetched": text_fetched, "cache_hits": cache_hits,
                           "leads_resolved": leads_resolved}, f, indent=1)
            journal.append(step="s9-s2-leg-c", status="checkpoint", processed_this_run=n,
                           text_fetched=text_fetched, budget=budget.snapshot(),
                           lane="o2-opus-xhigh", model="claude-opus-4-8")
            i_since_ckpt = 0

    summary = {
        "worklist_eligible": len(work),
        "processed_this_run": n,
        "leads_resolved": leads_resolved,
        "text_fetched_live": text_fetched,
        "cluster_cache_hits": cache_hits,
        "cluster_404": not_found_404,
        "no_lead_derivable": no_lead_derivable,
        "fetch_failures": fetch_failures,
        "skipped_pre": skipped,
        "session_network_calls": budget.session_calls,
        "budget_max": MAX_CALLS,
    }
    with open(STATE_PATH, "w") as f:
        json.dump(summary, f, indent=1)
    journal.append(step="s9-s2-leg-c", status="driver-end", mode=MODE,
                   session_network_calls=budget.session_calls, budget=budget.snapshot(),
                   lane="o2-opus-xhigh", model="claude-opus-4-8")
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    print("SESSION_NETWORK_CALLS=%d" % budget.session_calls)
else:
    raise SystemExit("unknown mode %s" % MODE)
