#!/usr/bin/env python3
"""
LINT-1 — CourtListener CLUSTER identity + opinion-binding check.  Enforces S1 L3 + D7.

############################################################################
#  RUN ONLY THROUGH THE SINGLE SERIAL CL LANE AT THE GATE.                  #
#  NEVER run this in parallel, and never alongside any other CL caller (L4).#
#  ALL CourtListener traffic in the project is concurrency-1, always.       #
#  This file is WRITE-ONLY in the lint-authoring unit: it is built here but  #
#  executed later, exactly once, by the serial CL lane at the publish gate.  #
############################################################################

What it does
------------
For every CourtListener reference in the corpus it confirms BOTH halves of L3
CLUSTER-FIRST (see RULING P5-05):
  1. the CLUSTER id RESOLVES (HTTP 200), and
  2. the returned cluster displays the NAMED case (identity, not just status);
  and, for a case-page frontmatter ref that carries an opinion_id, that
  3. the opinion is actually BOUND to that cluster — i.e. /opinions/<opinion_id>/
     appears in the cluster's `sub_opinions` (the true cluster<->opinion binding).

Why cluster-first (RULING P5-05 / LAW-02 in the lint itself)
------------------------------------------------------------
A CourtListener human URL  https://www.courtlistener.com/opinion/<N>/<slug>/
embeds the CLUSTER id N, NOT an opinion id. The prior verify path treated N as
an opinion id and fetched /opinions/N/, which resolves to an unrelated record
(Byrd: cluster 4497658 = Byrd, but opinion 4497658 = Guggenheim), producing a
PHANTOM identity mismatch. Old records only "passed" by numeric coincidence
(Lawbox-era opinion id == cluster id). The corpus data is correct: case pages
carry BOTH `courtlistener.cluster_id` and `courtlistener.opinion_id`. So:
  - every URL-derived id is a CLUSTER id;
  - frontmatter refs read `courtlistener.cluster_id` (and carry opinion_id for
    the binding check);
  - the check is ONE cluster fetch (not the old two), name-match on the cluster,
    plus a zero-extra-call binding assertion when opinion_id is present.

References checked:
  - case-page frontmatter  courtlistener.cluster_id (+ opinion_id when present)
    (paired with the page `title` as the expected case name), and
  - any CourtListener opinion URL appearing in prose/tables — the URL id is the
    CLUSTER id (paired with the nearest party-v-party case name on the same
    line, when present; no opinion binding is asserted for prose refs).

Discipline (L4)
---------------
  - Uses the CourtListener v4 REST API under the builder credential
    (S9 Amendment A1(3) + RULING P5-04(b): v4 now 401s unauthenticated
    requests; the full-roster batch runs under the builder token). Falls back
    to no-auth only if the token file is absent.
  - Endpoint:  /api/rest/v4/clusters/<cluster_id>/?fields=case_name,
    case_name_full,case_name_short,sub_opinions  (ONE call per reference).
  - SERIAL pacing: sleeps MIN_INTERVAL_SECONDS between every call so the rate
    stays well under 20/min (default 13/min). Honors STOP-on-5/min-tier:
    if the tier regresses, RUNBOOK §3 STOP-and-notify governs — raise the
    interval or stop; never parallelize to "catch up".
  - Checkpointable: resumable via a JSON ledger so a long run can resume.
    NOTE (P5-05): the ledger key shape changed (cluster-id keyed). A stale
    ledger from the old (opinion-id) semantics MUST be wiped before a re-run.

It is importable (functions below) and has a CLI, but the CLI REFUSES to make
any network call unless the operator passes the explicit serial-lane
confirmation flag --i-am-the-serial-cl-lane. Importing this module performs no
I/O. `--self-test` runs offline fixtures only (no network). Do NOT execute the
verify path from the lint-authoring unit.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _common as c  # noqa: E402

LINT = "LINT-1"

API_BASE = "https://www.courtlistener.com/api/rest/v4"
USER_AGENT = "CSSI-LINT-1/1.0 (serial CL lane; +https://courtlistener.com)"

# --- serial pacing (L4) ---------------------------------------------------
MAX_CALLS_PER_MIN = 13            # target rate; keep well under 20/min AND under the ~1,000/hr token budget (P5 tune)
MIN_INTERVAL_SECONDS = 60.0 / MAX_CALLS_PER_MIN
REQUEST_TIMEOUT = 30


# --------------------------------------------------------------------------
# reference collection (no network)
# --------------------------------------------------------------------------

def _as_int(v):
    """Coerce a frontmatter scalar (the subset parser yields strings) to int,
    or None if absent/blank/non-numeric. Null-token spellings ('null','~',...)
    must be folded to absent by the caller BEFORE calling this."""
    if v is None:
        return None
    try:
        return int(str(v).strip())
    except (ValueError, TypeError):
        return None


def collect_references(paths=None):
    """Return a list of reference dicts to verify:
       {file, line, cluster_id, opinion_id, url, expected_name, source}

    Per RULING P5-05 every URL-derived id is a CLUSTER id. Frontmatter case
    refs read `courtlistener.cluster_id` directly (falling back to the id
    embedded in `opinion_url` only when cluster_id is absent) and carry
    `courtlistener.opinion_id` when present (for the binding check). Prose refs
    take their CLUSTER id from the embedded URL id and carry no opinion_id
    (no binding is asserted for prose). `source` is 'frontmatter' or 'prose'.
    No network I/O here."""
    refs = []
    for path in c.iter_markdown_files(paths):
        text = c.read_text(path)
        fm, body, start = c.split_frontmatter(text)

        if fm.get("type") == "case":
            cid = c.fm_get(fm, "courtlistener", "cluster_id")
            oid = c.fm_get(fm, "courtlistener", "opinion_id")
            url = c.fm_get(fm, "courtlistener", "opinion_url")
            title = fm.get("title") if isinstance(fm.get("title"), str) else ""
            # YAML-null guard (P5): the stdlib subset parser yields the STRING
            # 'null' (or '~'/'none'/'') for a YAML null scalar — the sanctioned
            # no-CL-record state (Entick/Wilkes). Treat those as ABSENT, not ids.
            if c.is_null_token(cid):
                cid = None
            if c.is_null_token(oid):
                oid = None
            if c.is_null_token(url):
                url = None
            # URL-derived ids are CLUSTER ids (P5-05): if the frontmatter omits
            # cluster_id but carries a URL, recover the CLUSTER id from the URL.
            if not cid and url:
                m = c.CL_OPINION_URL_RE.search(str(url))
                cid = m.group(1) if m else None
            cid = _as_int(cid)
            oid = _as_int(oid)
            if cid or url:
                refs.append({
                    "file": c.relpath(path), "line": 1,
                    "cluster_id": cid,
                    "opinion_id": oid,
                    "url": url or "",
                    "expected_name": title,
                    "source": "frontmatter",
                })

        body_lines = body.split("\n")
        fenced = c.fenced_line_numbers(body_lines)
        for i, line in enumerate(body_lines):
            if i in fenced:
                continue
            for m in c.CL_OPINION_URL_RE.finditer(line):
                cid = int(m.group(1))   # URL id == CLUSTER id (P5-05)
                nm = c.CASE_RE.search(c.mask_links_and_code(line))
                refs.append({
                    "file": c.relpath(path), "line": start + i,
                    "cluster_id": cid, "opinion_id": None,
                    "url": m.group(0),
                    "expected_name": nm.group(0) if nm else "",
                    "source": "prose",
                })
    return refs


# --------------------------------------------------------------------------
# CL fetch (network — serial lane only)
# --------------------------------------------------------------------------

def _cl_token():
    """Builder-credential token (S1 A1/L4' + S9 Amendment A1(3): the full-roster
    LINT-1 batch executes under the builder credential). Optional: falls back to
    no-auth if the token file is absent. Added at P5 when CL's v4 API began
    returning 401 to unauthenticated requests (2026-07-22)."""
    path = os.path.expanduser("~/.config/cssi/cl-token")
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read().strip() or None
    except OSError:
        return None


_TOKEN = _cl_token()


def _get_json(url):
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if _TOKEN:
        headers["Authorization"] = "Token " + _TOKEN
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        return resp.getcode(), json.loads(resp.read().decode("utf-8"))


def _name_tokens(name):
    """Significant party tokens for fuzzy identity matching (drops reporter
    cites, years, punctuation, and common stopwords)."""
    name = re.sub(r"\d.*$", "", name)            # drop trailing cite/year
    name = name.replace("’", "'")
    toks = re.findall(r"[A-Za-z]{3,}", name.lower())
    stop = {"the", "and", "for", "united", "states", "city", "county",
            "people", "commonwealth", "state", "ex", "rel"}
    return [t for t in toks if t not in stop]


def _cluster_url(cluster_id):
    return ("%s/clusters/%d/?fields=case_name,case_name_full,case_name_short,"
            "sub_opinions" % (API_BASE, cluster_id))


def verify_reference(ref):
    """Verify a single reference against CourtListener. ONE cluster call; the
    opinion-binding assertion costs 0 extra calls. Returns a violation dict on
    failure, or None on success. MUST be called only from the serial lane (it
    makes live HTTP calls).

    Cluster-first per RULING P5-05:
      (0) no cluster id            -> distinct 'no resolvable cluster id'
      (1) cluster fetch fails      -> distinct 'fetch failed ... not a mismatch'
                                      (retry once, distinguish from a real
                                      identity mismatch — P5 precision fix)
      (2) cluster names a different case (name tokens do not overlap)
                                   -> 'identity mismatch'
      (3) opinion_id present but NOT in the cluster's sub_opinions
                                   -> 'binding mismatch'
    """
    cid = ref.get("cluster_id")
    if not cid:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL reference has no resolvable cluster id: %s [L3]"
            % (ref.get("url") or "<none>"))

    # ONE call: the cluster record carries the canonical case name AND the
    # sub_opinions list. P5 retry-and-distinguish: a FAILED fetch must NOT
    # masquerade as an identity mismatch. Retry once (serial pacing between the
    # two attempts), then report a DISTINCT fetch-failure violation.
    url = _cluster_url(cid)
    case_name = ""
    sub_opinions = []
    fetch_failed = None
    got = False
    for attempt in (1, 2):
        try:
            code, cl = _get_json(url)
            if code == 200:
                case_name = (cl.get("case_name") or cl.get("case_name_full")
                             or cl.get("case_name_short") or "")
                sub_opinions = cl.get("sub_opinions") or []
                fetch_failed = None
                got = True
                break
            fetch_failed = "HTTP %s" % code
        except urllib.error.HTTPError as e:
            fetch_failed = "HTTP %d" % e.code
        except Exception as e:  # noqa: BLE001 - network/parse errors are failures
            fetch_failed = str(e)[:120]
        if attempt == 1:
            time.sleep(MIN_INTERVAL_SECONDS)   # serial pacing between retries (L4)
    if not got:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL cluster %d fetch failed (%s) — identity UNVERIFIED, not a name "
            "mismatch [L3]" % (cid, fetch_failed))

    # (2) identity by name against the CLUSTER's canonical case name.
    expected = ref.get("expected_name") or ""
    if expected:
        want = _name_tokens(expected)
        have = set(_name_tokens(case_name)) if case_name else set()
        matched = [t for t in want if t in have]
        if want and not matched:
            return c.make_violation(
                LINT, ref["file"], ref["line"], c.HIGH,
                "CL identity mismatch for cluster %d: expected '%s' but cluster "
                "names '%s' [L3]" % (cid, expected, case_name))

    # (3) cluster<->opinion binding (frontmatter refs that carry opinion_id;
    # 0 extra calls — sub_opinions came back with the cluster fetch).
    oid = ref.get("opinion_id")
    if oid:
        needle = "/opinions/%d/" % oid
        bound = any(needle in str(su) for su in sub_opinions)
        if not bound:
            listed = ", ".join(str(su) for su in sub_opinions) or "<none>"
            return c.make_violation(
                LINT, ref["file"], ref["line"], c.HIGH,
                "CL binding mismatch: opinion %d is not among cluster %d's "
                "sub_opinions [%s] [L3]" % (oid, cid, listed))
    return None


def run(paths=None, ledger_path=None, confirmed=False, limit=None):
    """Run the full identity sweep. SERIAL ONLY. Refuses to make network calls
    unless `confirmed=True` (set by the CLI serial-lane flag). `limit` caps the
    number of collected references verified (the sanctioned smoke path). Returns
    the list of violations."""
    refs = collect_references(paths)
    if limit is not None:
        refs = refs[:limit]
    if not confirmed:
        raise RuntimeError(
            "LINT-1 is serial-CL-gate-only. Refusing to make CL calls without "
            "explicit serial-lane confirmation (pass confirmed=True / "
            "--i-am-the-serial-cl-lane). Collected %d references." % len(refs))

    done = {}
    if ledger_path and os.path.exists(ledger_path):
        with open(ledger_path, "r", encoding="utf-8") as fh:
            done = json.load(fh)

    violations = []
    # P5 memo (orchestrator-mechanical): a cluster fetch is deterministic, so
    # identical (cluster_id, expected-tokens, opinion_id) triples yield identical
    # verdicts — verify once per triple, replay per ref (violations still reported
    # per file/line). Cuts the serial batch with zero fidelity loss.
    #   * cluster_id + expected-tokens fix the identity (name) verdict;
    #   * opinion_id is part of the key because the BINDING verdict depends on it
    #     — a frontmatter ref (opinion_id set) and a prose ref (opinion_id None)
    #     to the SAME cluster/name must NOT share a memo slot, or the prose ref
    #     (no binding check) could suppress the frontmatter ref's binding check.
    memo = {}
    for n, ref in enumerate(refs):
        key = "%s::%s::%s::%s" % (
            ref["file"], ref["line"], ref.get("cluster_id"),
            ref.get("opinion_id"))
        if key in done:
            if done[key]:
                violations.append(done[key])
            continue
        mkey = (ref.get("cluster_id"),
                tuple(sorted(_name_tokens(ref.get("expected_name") or ""))),
                ref.get("opinion_id"))
        if mkey in memo:
            base = memo[mkey]
            v = dict(base, file=ref["file"], line=ref["line"]) if base else None
        else:
            v = verify_reference(ref)
            memo[mkey] = v
        done[key] = v
        if v:
            violations.append(v)
        if ledger_path:
            with open(ledger_path, "w", encoding="utf-8") as fh:
                json.dump(done, fh)
        if n + 1 < len(refs):
            time.sleep(MIN_INTERVAL_SECONDS)   # serial pacing (L4)
    return violations


# --------------------------------------------------------------------------
# offline self-test (NO network) — exercises the P5-05 cluster-first semantics
# --------------------------------------------------------------------------

def _self_test():
    """Offline fixture self-test (NO network). Covers: URL->cluster-id
    extraction, frontmatter cluster_id read + opinion_id carry, null-token
    guard, name-mismatch, binding-mismatch, fetch-failure-is-not-a-mismatch,
    and the missing-cluster-id guard. Returns 0 on success, 1 on any failure."""
    global _get_json, MIN_INTERVAL_SECONDS
    failures = []
    ran = [0]

    def check(cond, label):
        ran[0] += 1
        print("  %s %s" % ("ok  " if cond else "FAIL", label))
        if not cond:
            failures.append(label)

    print("[LINT-1 self-test] collection (offline fixtures)")
    fixtures_dir = os.path.join(HERE, "fixtures", "lint1_cl_identity")
    refs = collect_references([fixtures_dir])
    by_name = {}
    for r in refs:
        by_name.setdefault(os.path.basename(r["file"]), []).append(r)

    # (a) frontmatter cluster_id read (the URL id is a CLUSTER id) + opinion carry
    byrd = next((r for r in by_name.get("byrd_frontmatter.md", [])
                 if r["source"] == "frontmatter"), None)
    check(byrd is not None
          and byrd["cluster_id"] == 4497658
          and byrd["opinion_id"] == 4274911,
          "frontmatter reads cluster_id=4497658 + opinion_id=4274911")

    # (b) cluster_id absent -> recovered from opinion_url (still a CLUSTER id)
    katz = next((r for r in by_name.get("url_only_frontmatter.md", [])
                 if r["source"] == "frontmatter"), None)
    check(katz is not None
          and katz["cluster_id"] == 107496
          and katz["opinion_id"] is None,
          "frontmatter cluster_id recovered from URL when field absent")

    # (c) prose URL id parsed as a CLUSTER id, no opinion binding carried
    prose = [r for r in refs if r["source"] == "prose"]
    check(any(r["cluster_id"] == 111111 and r["opinion_id"] is None
              for r in prose),
          "prose URL id parsed as cluster_id (opinion_id None)")

    # (d) null-token guard: null cluster_id/opinion_id -> NO ref emitted
    check(all(os.path.basename(r["file"]) != "entick_null.md" for r in refs),
          "null-token case emits no ref (Entick sanctioned no-CL state)")

    print("[LINT-1 self-test] verify (mocked cluster fetch — NO network)")
    canned = {
        # Byrd cluster: names Byrd, binds opinion 4274911
        ("%s/clusters/4497658/" % API_BASE): (200, {
            "case_name": "Byrd v. United States",
            "sub_opinions": [
                "https://www.courtlistener.com/api/rest/v4/opinions/4274911/"],
        }),
        # a cluster that names a DIFFERENT case (the real-CL numeric-coincidence
        # trap: e.g. opinion 4497658 = Guggenheim while cluster 4497658 = Byrd)
        ("%s/clusters/222222/" % API_BASE): (200, {
            "case_name": "Guggenheim v. City of Goleta",
            "sub_opinions": [
                "https://www.courtlistener.com/api/rest/v4/opinions/222222/"],
        }),
    }

    def fake_get_json(u):
        base = u.split("?", 1)[0]
        if base in canned:
            return canned[base]
        raise urllib.error.URLError("no fixture for %s" % base)

    orig_get_json = _get_json
    orig_interval = MIN_INTERVAL_SECONDS
    _get_json = fake_get_json
    MIN_INTERVAL_SECONDS = 0        # no real sleeping in the offline test
    try:
        v = verify_reference({"file": "f", "line": 1, "cluster_id": 4497658,
                              "opinion_id": 4274911,
                              "expected_name": "Byrd v. United States"})
        check(v is None, "byrd: cluster name + opinion binding -> PASS")

        v = verify_reference({"file": "f", "line": 1, "cluster_id": 4497658,
                              "opinion_id": 9999999,
                              "expected_name": "Byrd v. United States"})
        check(v is not None and "binding mismatch" in v["message"],
              "binding-mismatch detected (opinion not in sub_opinions)")

        v = verify_reference({"file": "f", "line": 1, "cluster_id": 222222,
                              "opinion_id": None,
                              "expected_name": "Byrd v. United States"})
        check(v is not None and "identity mismatch" in v["message"],
              "name-mismatch detected (wrong cluster names another case)")

        v = verify_reference({"file": "f", "line": 1, "cluster_id": 888888,
                              "opinion_id": None,
                              "expected_name": "Whatever v. Case"})
        check(v is not None and "fetch failed" in v["message"]
              and "not a name mismatch" in v["message"],
              "fetch-failure is DISTINCT from a name mismatch")

        v = verify_reference({"file": "f", "line": 1, "cluster_id": None,
                              "opinion_id": None, "expected_name": "X v. Y",
                              "url": ""})
        check(v is not None and "no resolvable cluster id" in v["message"],
              "missing cluster id -> distinct violation")
    finally:
        _get_json = orig_get_json
        MIN_INTERVAL_SECONDS = orig_interval

    print("[LINT-1 self-test] %s (%d checks, %d failed)"
          % ("PASS" if not failures else "FAIL", ran[0], len(failures)))
    return 0 if not failures else 1


def main():
    args = sys.argv[1:]
    if "--self-test" in args:
        sys.exit(_self_test())

    confirmed = "--i-am-the-serial-cl-lane" in args
    paths = [a for a in args if not a.startswith("-")] or None
    ledger = None
    limit = None
    for a in args:
        if a.startswith("--ledger="):
            ledger = a.split("=", 1)[1]
        elif a.startswith("--limit="):
            try:
                limit = int(a.split("=", 1)[1])
            except ValueError:
                limit = None

    if not confirmed:
        refs = collect_references(paths)
        if limit is not None:
            refs = refs[:limit]
        sys.stderr.write(
            "LINT-1 is WRITE-ONLY / serial-CL-gate-only. NOT running.\n"
            "RUN ONLY THROUGH THE SINGLE SERIAL CL LANE AT THE GATE (L4).\n"
            "Collected %d CL reference(s) that WOULD be verified.\n"
            "To actually run (serial lane only): "
            "python3 lint1_cl_identity.py --i-am-the-serial-cl-lane "
            "[--ledger=cl-ledger.json] [--limit=N] [glob ...]\n" % len(refs))
        sys.exit(2)

    violations = run(paths, ledger_path=ledger, confirmed=True, limit=limit)
    c.emit(violations)
    sys.exit(c.exit_code_for(violations))


if __name__ == "__main__":
    main()
