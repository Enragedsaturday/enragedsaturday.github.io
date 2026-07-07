#!/usr/bin/env python3
"""S6 slip-only marker stamper (S2 A3 slip precedent).

Stamps `citations.slip_only: true` (+ a `citations.slip_only_provenance` trail)
onto EXACTLY the journaled slip-only lake records — the real cases (mostly OT2025)
whose reporter cite does not exist yet. The marker is what unblocks the mint's
slip path (`scripts/s6/mint_page.py`); the mint NEVER infers slip-only from an
absent citation — only from this explicit marker.

Idiom mirrors ingest.py `--apply-web-keys`: **dry-run is the default**, `--write`
is guarded, every action is journaled, and the surface is BOUNDED to a named
allowlist — it refuses to stamp any record_id not in the slip-only allowlist and
refuses to stamp a record that already carries a real citation.

Allowlist: the recovery lane's `_run/o2-execute/R8-R3-web-cites.jsonl` rows with
`"slip_only": true` (15 at signing: Landor, Olivier, Konan, GEO Group, Mendoza,
Carter, Robinson, Larson, Davis, Holcomb, Hunt, Ruiz, Lee, Zorn, District of
Columbia v. R.W.). Enumerated — never a wildcard.

ZERO network. Writes lake records only through the guarded `--write` path.

Usage:
  python3 scripts/s6/stamp_slip_only.py                               # dry-run all allowlisted
  python3 scripts/s6/stamp_slip_only.py --record <id>                 # dry-run one (must be allowlisted)
  python3 scripts/s6/stamp_slip_only.py --as-of <ISO> --write         # guarded commit
  python3 scripts/s6/stamp_slip_only.py --self-test
"""

import argparse
import copy
import json
import os
import re
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))

ALLOWLIST_REL = os.path.join("_run", "o2-execute", "R8-R3-web-cites.jsonl")
LAKE_REL = os.path.join("_overhaul2", "lake")
JOURNAL_REL = os.path.join("_run", "o2-execute", "s6-slip-stamp-journal.jsonl")
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:?\d{2})?)?$")

REFUSE_NOT_IN_ALLOWLIST = "record-not-in-slip-allowlist"
REFUSE_NO_RECORD = "no-lake-record"
REFUSE_CITE_BEARING = "record-already-citation-bearing"
REFUSE_AS_OF = "as-of-required"


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def norm_as_of(value):
    if not value or not ISO_RE.match(str(value).strip()):
        raise ValueError("--as-of must be an ISO date/datetime; got %r" % (value,))
    return str(value).strip()


def load_allowlist(path):
    """Return {record_id: row} for exactly the `slip_only: true` rows."""
    out = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("slip_only") is True and row.get("record_id"):
                out[row["record_id"]] = row
    return out


def _has_real_citation(record):
    cit = record.get("citations") or {}
    if isinstance(cit.get("display"), str) and cit["display"].strip():
        return True
    official = cit.get("official")
    if isinstance(official, dict) and (official.get("cite") or official.get("reporter")):
        return True
    if isinstance(official, str) and official.strip():
        return True
    return False


def build_provenance(row, as_of, by, source_name):
    prov = {"source": source_name, "as_of": as_of, "by": by}
    if row.get("note"):
        prov["note"] = row["note"]
    legs = []
    for leg in row.get("legs") or []:
        if isinstance(leg, dict):
            legs.append({k: leg[k] for k in ("source", "url", "cite") if k in leg})
    if legs:
        prov["legs"] = legs
    return prov


def plan_stamp(record_id, allowlist, lake_root, as_of, by, source_name):
    """Return a per-record plan dict (no write). `ok` True => a --write stamps it."""
    if record_id not in allowlist:
        return {"record_id": record_id, "ok": False, "refused": True,
                "code": REFUSE_NOT_IN_ALLOWLIST,
                "message": "record_id %r is not in the slip-only allowlist" % record_id}
    path = os.path.join(lake_root, "cases", record_id + ".json")
    if not os.path.exists(path):
        return {"record_id": record_id, "ok": False, "refused": True,
                "code": REFUSE_NO_RECORD, "message": "no lake record at %s" % path}
    record = read_json(path)
    if _has_real_citation(record):
        return {"record_id": record_id, "ok": False, "refused": True,
                "code": REFUSE_CITE_BEARING,
                "message": "record %r already carries a real citation — refusing to "
                           "mark it slip_only" % record_id}
    if (record.get("citations") or {}).get("slip_only") is True:
        return {"record_id": record_id, "ok": True, "refused": False,
                "already_stamped": True, "path": path}
    prov = build_provenance(allowlist[record_id], as_of, by, source_name)
    return {"record_id": record_id, "ok": True, "refused": False, "already_stamped": False,
            "path": path, "record": record, "provenance": prov}


def commit_stamp(plan, journal_path=None):
    """Apply one validated stamp plan (atomic per-record write). Journaled."""
    if not plan.get("ok") or plan.get("already_stamped"):
        return {"stamped": False, "record_id": plan["record_id"]}
    record = copy.deepcopy(plan["record"])
    cit = record.setdefault("citations", {})
    cit["slip_only"] = True
    cit["slip_only_provenance"] = plan["provenance"]
    write_json_atomic(plan["path"], record)
    if journal_path:
        jp = journal_path if os.path.isabs(journal_path) else os.path.join(REPO_ROOT, journal_path)
        os.makedirs(os.path.dirname(jp), exist_ok=True)
        with open(jp, "a", encoding="utf-8") as f:
            f.write(json.dumps({"event": "slip-only-stamp", "record_id": plan["record_id"],
                                "as_of": plan["provenance"]["as_of"],
                                "by": plan["provenance"]["by"]}, ensure_ascii=False) + "\n")
    return {"stamped": True, "record_id": plan["record_id"], "path": plan["path"]}


def run(allowlist_path, lake_root, records, as_of, by, write, journal_path):
    allowlist = load_allowlist(allowlist_path)
    source_name = os.path.basename(allowlist_path)
    targets = records if records else sorted(allowlist)
    results = []
    refused = 0
    stamped = 0
    skipped = 0
    for rid in targets:
        plan = plan_stamp(rid, allowlist, lake_root, as_of, by, source_name)
        if plan.get("refused"):
            refused += 1
            sys.stderr.write("REFUSED [%s] %s: %s\n" % (plan["code"], rid, plan["message"]))
        elif plan.get("already_stamped"):
            skipped += 1
            sys.stderr.write("already-stamped (no-op): %s\n" % rid)
        elif write:
            commit_stamp(plan, journal_path)
            stamped += 1
            sys.stderr.write("STAMPED %s\n" % rid)
        else:
            sys.stderr.write("DRY-RUN would stamp %s (slip_only + provenance)\n" % rid)
        results.append(plan)
    sys.stderr.write("[slip-stamp] targets=%d stamped=%d already=%d refused=%d %s\n" % (
        len(targets), stamped, skipped, refused, "(dry-run)" if not write else ""))
    return results, refused


def self_test():
    import tempfile
    sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "lint"))
    import lint13_schema as L13  # noqa: E402
    results = []

    def check(label, cond):
        results.append((label, bool(cond)))
        sys.stderr.write("[self-test] %-46s -> %s\n" % (label, "OK" if cond else "FAIL"))

    with tempfile.TemporaryDirectory(prefix="slip-stamp-") as tmp:
        lake = os.path.join(tmp, "lake", "cases")
        os.makedirs(lake)
        # a real slip-only stub (no citation) — copy a live slip-only stub's shape
        live = os.path.join(REPO_ROOT, LAKE_REL, "cases",
                            "landor-v-louisiana-department-of-corrections-and-public-safety--10878535.json")
        base = read_json(live)
        base["record_id"] = "fixture-slip--900700"
        # start from an UNstamped base regardless of whether the live record has
        # already been stamped by the real gate run — the self-test owns its state.
        base.setdefault("citations", {})
        base["citations"].pop("slip_only", None)
        base["citations"].pop("slip_only_provenance", None)
        with open(os.path.join(lake, "fixture-slip--900700.json"), "w", encoding="utf-8") as f:
            json.dump(base, f, ensure_ascii=False)
        # a cite-bearing record (must be refused)
        cited = copy.deepcopy(base)
        cited["record_id"] = "fixture-cited--900701"
        cited.setdefault("citations", {})["display"] = "610 U.S. 1"
        cited["citations"]["official"] = {"cite": "610 U.S. 1"}
        with open(os.path.join(lake, "fixture-cited--900701.json"), "w", encoding="utf-8") as f:
            json.dump(cited, f, ensure_ascii=False)
        lake_root = os.path.join(tmp, "lake")

        allow = os.path.join(tmp, "allow.jsonl")
        with open(allow, "w", encoding="utf-8") as f:
            f.write(json.dumps({"record_id": "fixture-slip--900700", "slip_only": True,
                                "note": "SCOTUS No. 23-1197 slip",
                                "legs": [{"source": "Cornell LII", "url": "https://x", "cite": "No. 23-1197"}]}) + "\n")
            f.write(json.dumps({"record_id": "fixture-cited--900701", "slip_only": True,
                                "note": "cite-bearing"}) + "\n")
        al = load_allowlist(allow)
        source = os.path.basename(allow)

        # out-of-scope refusal
        p = plan_stamp("not-in-list--000", al, lake_root, "2026-07-07", "s6-slip-stamp", source)
        check("out-of-scope record refused", p.get("code") == REFUSE_NOT_IN_ALLOWLIST)
        # cite-bearing refusal
        p = plan_stamp("fixture-cited--900701", al, lake_root, "2026-07-07", "s6-slip-stamp", source)
        check("cite-bearing record refused", p.get("code") == REFUSE_CITE_BEARING)
        # happy stamp (dry-run plan ok)
        p = plan_stamp("fixture-slip--900700", al, lake_root, "2026-07-07", "s6-slip-stamp", source)
        check("slip-only plan ok", p.get("ok") and not p.get("already_stamped"))
        # commit + verify marker + provenance + schema conformance
        commit_stamp(p, None)
        rec = read_json(os.path.join(lake, "fixture-slip--900700.json"))
        check("marker written", rec["citations"].get("slip_only") is True)
        check("provenance trail written",
              rec["citations"]["slip_only_provenance"]["source"] == source
              and rec["citations"]["slip_only_provenance"]["legs"][0]["cite"] == "No. 23-1197")
        stamped_viols = L13.validate_record("x", rec, L13.load_json(L13.SCHEMA_PATH))
        check("stamped record passes LINT-13 schema", len(stamped_viols) == 0)
        # idempotent re-run
        p2 = plan_stamp("fixture-slip--900700", al, lake_root, "2026-07-07", "s6-slip-stamp", source)
        check("idempotent already-stamped", p2.get("already_stamped") is True)

    ok = all(v for _l, v in results)
    sys.stderr.write("[self-test] %s (%d/%d)\n"
                     % ("PASS" if ok else "FAIL", sum(v for _l, v in results), len(results)))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--allowlist", default=ALLOWLIST_REL)
    ap.add_argument("--lake-root", default=LAKE_REL)
    ap.add_argument("--record", action="append", help="restrict to record_id(s) (must be allowlisted)")
    ap.add_argument("--as-of", help="ISO date/datetime (required with --write)")
    ap.add_argument("--by", default="s6-slip-stamp")
    ap.add_argument("--write", action="store_true", help="guarded commit (default: dry-run)")
    ap.add_argument("--journal", default=JOURNAL_REL)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    as_of = args.as_of or "DRY-RUN"
    if args.write or args.as_of:
        try:
            as_of = norm_as_of(args.as_of or "")
        except ValueError as exc:
            sys.stderr.write("REFUSED [%s]: %s\n" % (REFUSE_AS_OF, exc))
            return 2

    allow_path = args.allowlist if os.path.isabs(args.allowlist) else os.path.join(REPO_ROOT, args.allowlist)
    lake_root = args.lake_root if os.path.isabs(args.lake_root) else os.path.join(REPO_ROOT, args.lake_root)
    _results, refused = run(allow_path, lake_root, args.record, as_of, args.by, args.write, args.journal)
    return 2 if refused else 0


if __name__ == "__main__":
    sys.exit(main())
