#!/usr/bin/env python3
"""
S9 lane harness — the ONE invocation path for every P1/P2 lane (spec S9 R1/R4/R5).

Every Codex reviewer/reader lane and every panel-vote goes through here so the
mechanical-isolation guarantees (R1) are enforced in one place and cannot be
bypassed per-call:

  * Codex lane = a FRESH `codex exec` (never `resume`), `-s read-only`, an
    ISOLATED working dir per invocation (a temp sandbox OUTSIDE the repo holding
    ONLY the manifest-listed files — the page markdown, the lake judgment fields,
    and thread-P.json are physically not present), model gpt-5.5,
    `-c model_reasoning_effort=xhigh`, stdin `/dev/null`, `-o` capture, a
    caller-side perl-alarm timeout (COH-31 — macOS has no GNU `timeout`), and
    `-c tools.web_search=true` ONLY for discovery lanes (default OFF).
  * Every invocation writes `_run/s9/manifests/<lane-id>.json` BEFORE launch and
    VALIDATES it fail-closed: a blind Thread-N manifest may not disclose the
    content page, the lake record's judgment fields (treatment/homes — identity
    fields only: caption/cluster/opinion ids), or thread-P.json; a reviewer/vote
    manifest may not disclose sibling votes or in-progress adjudications. A
    manifest that would leak a forbidden surface aborts the launch (R14 blindness).
  * Output contract + repair: lanes return JSON per a per-lane_kind schema
    (case-read carries the MANDATORY identity assertion
    {parties_in_text, caption_claimed, match}). Prose-wrapped JSON is stripped/
    repaired; an unparseable result re-runs ONCE, then records `no-read`/`no-vote`
    (a 2-lane tally then needs unanimity to kill — spec §9).
  * Rows are appended JSONL under `_run/s9/` per LEDGER-SCHEMA (findings/votes/
    adjudications/fixes + reads: thread-N-reads.jsonl); every row carries
    {lane, model} exactly.

`--self-test` runs a MOCK lane (no live codex) proving: manifest-violation
detection, prose-wrap repair, no-read/no-vote fallback, and row validity vs
LINT-30 (a complete mock finding+3 votes+adjudication+fix reconciles green).

Stdlib only. COMMIT NOTHING. Content/lake read-only. The only live codex calls
are a pilot's (`--pilot`). Zero CL anywhere.
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import check_ledger  # noqa: E402  (LINT-30 — import, don't fork)

RUN_DIR = os.path.join(REPO_ROOT, "_run", "s9")
MANIFEST_DIR = os.path.join(RUN_DIR, "manifests")
THREAD_P = os.path.join(RUN_DIR, "thread-P.json")

POOL_ROOT = "/Users/johngalt/cssi-lake"
TEXT_DIR = os.path.join(POOL_ROOT, "cache", "text")

CODEX_MODEL = "gpt-5.5"
CODEX_REASONING = "xhigh"
DEFAULT_TIMEOUT_S = 600  # per-invocation wall-clock cap (perl-alarm; COH-31)
INVOCATION_CAP = 12      # pilot budget: the only live codex calls (work order)

# ledger row-type -> file
LEDGER_FILES = {
    "s9.read.v1": "thread-N-reads.jsonl",
    "s9.finding.v1": "findings.jsonl",
    "s9.vote.v1": "votes.jsonl",
    "s9.adjudication.v1": "adjudications.jsonl",
    "s9.fix.v1": "fixes.jsonl",
}

# identity fields a blind manifest MAY disclose (caption/cluster/opinion ids only)
IDENTITY_ALLOWED_KEYS = frozenset(
    {"caption_claimed", "cluster_id", "lead_opinion_id", "sibling_ids",
     "court", "court_level", "citation", "docket", "year", "record_id",
     "absolute_url"})
# keys that would leak a judgment (never in a blind manifest's identity payload)
JUDGMENT_KEYS = frozenset(
    {"treatment", "homes", "point_overrides", "holding", "disposition",
     "field_i_validity", "weight_label", "splits", "related", "progeny"})

BLIND_KINDS = ("case-read", "doctrine-rederive")


def _now():
    return datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(timespec="seconds")


def thread_p_hash():
    try:
        with open(THREAD_P, encoding="utf-8") as f:
            return json.load(f).get("content_hash")
    except OSError:
        return None


# ==========================================================================
# 1. Manifest — emission + fail-closed validation (R1 / R14 blindness)
# ==========================================================================

def build_manifest(lane_id, lane_kind, files_disclosed, fields_excluded,
                   ids, identity_payload=None, discovery=False, sandbox_dir=None):
    key = "case_ids" if lane_kind in BLIND_KINDS else "assertion_ids"
    return {
        "lane_id": lane_id,
        "lane_kind": lane_kind,
        "model": CODEX_MODEL,
        "files_disclosed": list(files_disclosed),
        "fields_excluded": list(fields_excluded),
        key: list(ids),
        "identity_payload": identity_payload or {},
        "discovery": bool(discovery),
        "sandbox_dir": sandbox_dir,
        "issued_at": _now(),
        "thread_p_hash_at_issue": thread_p_hash(),
    }


# a disclosed file is FORBIDDEN for a blind lane if its path looks like the
# content page, the frozen thread-P, or a full lake record (judgment fields)
_FORBIDDEN_BLIND_RE = re.compile(
    r"(?:^|/)content/|(?:^|/)thread-P\.json$|(?:^|/)_overhaul2/lake/cases/|"
    r"(?:^|/)assertion-inventory\.json$")
# a disclosed file is FORBIDDEN for a reviewer/vote lane if it is a sibling vote
# or an in-progress adjudication
_FORBIDDEN_REVIEW_RE = re.compile(
    r"(?:^|/)votes\.jsonl$|(?:^|/)adjudications\.jsonl$|"
    r"\.vote(?:\.[^/]*)?\.json$|\.adjudication\.json$")

REQUIRED_BLIND_EXCLUSIONS = ("content_page", "lake.treatment", "lake.homes",
                             "thread_p")
REQUIRED_REVIEW_EXCLUSIONS = ("sibling_votes", "in_progress_adjudications")


def validate_manifest(manifest, sandbox_files=None):
    """Return a list of blindness violations (empty == clean). Fail-closed:
    the launcher refuses to run any manifest with violations."""
    v = []
    kind = manifest.get("lane_kind")
    disclosed = list(manifest.get("files_disclosed") or [])
    if sandbox_files:
        disclosed = disclosed + list(sandbox_files)
    excl = set(manifest.get("fields_excluded") or [])

    if kind in BLIND_KINDS:
        for f in disclosed:
            if _FORBIDDEN_BLIND_RE.search(f):
                v.append("blind manifest discloses forbidden surface: %s" % f)
        ident = manifest.get("identity_payload") or {}
        for k in ident:
            if k in JUDGMENT_KEYS:
                v.append("blind identity payload leaks judgment field: %s" % k)
            elif k not in IDENTITY_ALLOWED_KEYS:
                v.append("blind identity payload carries non-identity key: %s" % k)
        for req in REQUIRED_BLIND_EXCLUSIONS:
            if req not in excl:
                v.append("blind manifest omits required exclusion: %s" % req)
    elif kind in ("vote", "review"):
        for f in disclosed:
            if _FORBIDDEN_REVIEW_RE.search(f):
                v.append("reviewer manifest discloses sibling vote/adjudication: %s" % f)
        for req in REQUIRED_REVIEW_EXCLUSIONS:
            if req not in excl:
                v.append("reviewer manifest omits required exclusion: %s" % req)
    else:
        v.append("unknown lane_kind: %r" % kind)

    if manifest.get("discovery") and kind in BLIND_KINDS:
        v.append("blind read/re-derivation must not enable web_search (independence)")
    return v


def write_manifest(manifest):
    os.makedirs(MANIFEST_DIR, exist_ok=True)
    p = os.path.join(MANIFEST_DIR, "%s.json" % manifest["lane_id"])
    with open(p, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2, sort_keys=True)
    return p


# ==========================================================================
# 2. Sandbox — a temp dir OUTSIDE the repo holding ONLY manifest files
# ==========================================================================

def materialize_case_sandbox(cached_text_path, identity_payload, prompt_kind):
    """Create an isolated read-only sandbox for a blind case read. Returns
    (sandbox_dir, sandbox_files). The opinion text is copied in as opinion.txt;
    the ONLY other files are identity.json (caption/ids only) and task.md."""
    sb = tempfile.mkdtemp(prefix="s9-lane-")
    shutil.copyfile(cached_text_path, os.path.join(sb, "opinion.txt"))
    with open(os.path.join(sb, "identity.json"), "w", encoding="utf-8") as f:
        json.dump(identity_payload, f, ensure_ascii=False, indent=2)
    with open(os.path.join(sb, "task.md"), "w", encoding="utf-8") as f:
        f.write(prompt_kind)
    return sb, ["opinion.txt", "identity.json", "task.md"]


# ==========================================================================
# 3. Codex invocation (fresh exec, read-only, perl-alarm timeout, capture)
# ==========================================================================

class InvocationBudget:
    def __init__(self, cap=INVOCATION_CAP):
        self.cap = cap
        self.used = 0

    def spend(self):
        if self.used >= self.cap:
            raise RuntimeError("codex invocation cap (%d) reached" % self.cap)
        self.used += 1
        return self.used


def run_codex(prompt, sandbox_dir, timeout_s=DEFAULT_TIMEOUT_S, discovery=False,
              budget=None):
    """One FRESH `codex exec` in the sandbox. Returns a dict with the last
    message, the raw --json event stream, exit info, wall clock, token estimate,
    and an auth_error flag. Never `resume`."""
    if budget is not None:
        budget.spend()
    out_msg = os.path.join(sandbox_dir, "_last_message.txt")
    events = os.path.join(sandbox_dir, "_events.jsonl")
    cmd = [
        "perl", "-e", "alarm shift; exec @ARGV", str(int(timeout_s)),
        "codex", "exec",
        "-C", sandbox_dir,
        "-s", "read-only",
        "-m", CODEX_MODEL,
        "-c", "model_reasoning_effort=%s" % CODEX_REASONING,
        # ZERO MCP for reviewer/reader lanes: no CourtListener (hard zero-CL
        # constraint + the CL MCP is broken), no context7/browser/etc. Reviewers
        # read only the sandbox (the lake text copied in). Clearing the whole
        # mcp_servers table also removes the broken-CL-OAuth startup failure.
        "-c", "mcp_servers={}",
        "--skip-git-repo-check",
        "--json",
        "-o", out_msg,
    ]
    if discovery:
        cmd += ["-c", "tools.web_search=true"]
    cmd += [prompt]

    t0 = time.time()
    with open(os.devnull, "rb") as devnull, open(events, "wb") as ev:
        proc = subprocess.run(cmd, stdin=devnull, stdout=ev,
                              stderr=subprocess.PIPE)
    wall = time.time() - t0

    last = ""
    if os.path.exists(out_msg):
        with open(out_msg, encoding="utf-8", errors="replace") as f:
            last = f.read()
    raw_events = ""
    if os.path.exists(events):
        with open(events, encoding="utf-8", errors="replace") as f:
            raw_events = f.read()
    stderr = (proc.stderr or b"").decode("utf-8", "replace")

    tokens = _parse_tokens(raw_events)
    if tokens.get("total") is None:  # fallback: char/4 estimate
        tokens = {"input": len(prompt) // 4, "output": len(last) // 4,
                  "total": (len(prompt) + len(last)) // 4, "source": "char-estimate"}

    timed_out = proc.returncode in (142, -14) or "alarm" in stderr.lower()
    auth_error = _looks_like_auth_error(stderr, last, proc.returncode)
    return {
        "last_message": last,
        "stderr_tail": stderr[-1200:],
        "returncode": proc.returncode,
        "wall_clock_s": round(wall, 1),
        "tokens": tokens,
        "timed_out": timed_out,
        "auth_error": auth_error,
        "events_path": events,
    }


_TOKEN_KEYS = ("total_tokens", "total_token_usage", "total", "tokens")


def _parse_tokens(raw_events):
    """Best-effort token extraction from the codex --json event stream. Codex
    emits usage in a token-count/usage event; shapes vary by version, so we scan
    every JSON line for input/output/total token fields and keep the max
    cumulative figure. Returns {input, output, total, source} (total may be
    None -> caller falls back to a char estimate)."""
    best = {"input": None, "output": None, "total": None, "source": "codex-events"}
    for line in raw_events.splitlines():
        line = line.strip()
        if not line or not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        for usage in _find_usage(obj):
            i = usage.get("input_tokens") or usage.get("prompt_tokens") \
                or usage.get("input")
            o = usage.get("output_tokens") or usage.get("completion_tokens") \
                or usage.get("output")
            t = usage.get("total_tokens") or usage.get("total") \
                or ((i or 0) + (o or 0) if (i or o) else None)
            if t and (best["total"] is None or t >= best["total"]):
                best.update(input=i, output=o, total=t)
    return best


def _find_usage(obj):
    """Yield dicts that look like a token-usage record anywhere in obj."""
    if isinstance(obj, dict):
        keys = set(obj.keys())
        if keys & {"input_tokens", "output_tokens", "total_tokens",
                   "prompt_tokens", "completion_tokens"}:
            yield obj
        for k, val in obj.items():
            if k in ("usage", "token_usage", "token_count", "info") and isinstance(val, dict):
                yield val
            if isinstance(val, (dict, list)):
                yield from _find_usage(val)
    elif isinstance(obj, list):
        for x in obj:
            yield from _find_usage(x)


_AUTH_MARKERS = ("not logged in", "unauthorized", "401", "403", "authentication",
                 "auth error", "invalid api key", "expired", "please run `codex login`",
                 "no api key", "credential")


_MCP_CONTEXT = ("mcp", "rmcp", "courtlistener", "oauth-protected-resource",
                "www-authenticate")


def _looks_like_auth_error(stderr, last, rc):
    """A GENUINE codex model-auth failure (the pause-#8 surface) vs. incidental
    MCP-server auth noise. With mcp_servers cleared this should not fire on MCP
    at all, but as a guard: an auth marker that appears ONLY in an MCP/rmcp/
    courtlistener context, while the model still returned a message, is NOT a
    codex-auth stop."""
    blob = ((stderr or "") + " " + (last or "")).lower()
    hit = any(m in blob for m in _AUTH_MARKERS)
    if not hit:
        return False
    mcp_scoped = any(m in blob for m in _MCP_CONTEXT)
    if mcp_scoped and last and last.strip():
        return False  # model produced output; the auth noise was MCP-only
    return True


# ==========================================================================
# 4. Output contract — strip/repair prose-wrapped JSON (spec §9 drift)
# ==========================================================================

_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.DOTALL)


def extract_json(text):
    """Return a dict parsed from a possibly prose-wrapped model reply, or None.
    Tries: (1) whole string; (2) fenced ```json block; (3) the outermost {...}
    via brace matching."""
    if not text:
        return None
    for cand in _json_candidates(text):
        try:
            obj = json.loads(cand)
            if isinstance(obj, dict):
                return obj
        except ValueError:
            continue
    return None


def _json_candidates(text):
    yield text.strip()
    for m in _FENCE_RE.finditer(text):
        yield m.group(1).strip()
    # outermost balanced {...}
    start = text.find("{")
    while start != -1:
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            else:
                if ch == '"':
                    in_str = True
                elif ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        yield text[start:i + 1]
                        break
        start = text.find("{", start + 1)


# ==========================================================================
# 5. Row emission (append-safe JSONL under _run/s9/)
# ==========================================================================

def emit_row(row, ledger_dir=RUN_DIR):
    schema = row.get("schema")
    fname = LEDGER_FILES.get(schema)
    if fname is None:
        raise ValueError("unknown row schema %r" % schema)
    os.makedirs(ledger_dir, exist_ok=True)
    p = os.path.join(ledger_dir, fname)
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    return p


# ==========================================================================
# 6. Case-read lane (blind Thread-N; the two Codex lenses)
# ==========================================================================

LENS_TASK = {
    "A": (
        "You are a BLIND case reviewer, attack lens A (SUPPORT / QUOTE-FIDELITY).\n"
        "Your entire evidentiary universe is the files in your working directory:\n"
        "  * opinion.txt  — the full text of ONE judicial opinion\n"
        "  * identity.json — the caption CLAIMED for it (parties, court, ids ONLY)\n"
        "You have NO other sources. Do not search. Do not assume facts not in "
        "opinion.txt.\n\n"
        "Derive, from opinion.txt ALONE:\n"
        "1. identity: read the party names ACTUALLY printed in the opinion text; "
        "compare to identity.json.caption_claimed; set match true/false.\n"
        "2. holding + disposition, in your own words, grounded in the text.\n"
        "3. support: the black-letter propositions the opinion ACTUALLY states, "
        "each with a SHORT verbatim quote you can find in opinion.txt and a rough "
        "location; if you cannot verify a quote verbatim, set verbatim_quote null.\n\n"
        "Return ONE JSON object, nothing else, exactly this shape:\n"
    ),
    "B": (
        "You are a BLIND case reviewer, attack lens B (CURRENCY / TREATMENT).\n"
        "Your entire evidentiary universe is the files in your working directory:\n"
        "  * opinion.txt  — the full text of ONE judicial opinion\n"
        "  * identity.json — the caption CLAIMED for it (parties, court, ids ONLY)\n"
        "You have NO other sources. Do not search. Judge ONLY from opinion.txt.\n\n"
        "Derive, from opinion.txt ALONE:\n"
        "1. identity: read the party names ACTUALLY printed in the opinion text; "
        "compare to identity.json.caption_claimed; set match true/false.\n"
        "2. holding + disposition, in your own words, grounded in the text.\n"
        "3. treatment: how THIS opinion treats prior law (does it overrule, limit, "
        "distinguish, or extend named prior cases?), any currency signals in the "
        "text itself, and the good-law posture as of the decision date.\n\n"
        "Return ONE JSON object, nothing else, exactly this shape:\n"
    ),
}

CASE_READ_SHAPE = {
    "identity": {"parties_in_text": "<parties you read>",
                 "caption_claimed": "<echo identity.json>",
                 "match": True},
    "holding": "<holding in your words>",
    "disposition": "<affirmed/reversed/remanded/...>",
    "lens": "A-or-B",
    "support": [{"proposition": "...", "verbatim_quote": "... or null",
                 "location": "... or null"}],
    "treatment": {"treats_prior": ["..."], "currency_signals": ["..."],
                  "good_law_as_of_decision": "..."},
    "splits": ["..."],
    "notes": "",
}


def _case_prompt(lens):
    return LENS_TASK[lens] + json.dumps(CASE_READ_SHAPE, indent=2) + \
        "\n\nOutput ONLY the JSON object."


def _identity_payload_for(worklist_row):
    return {
        "caption_claimed": worklist_row["caption"],
        "citation": worklist_row.get("citation"),
        "court_level": worklist_row.get("court_level"),
        "cluster_id": worklist_row.get("cluster_id"),
        "lead_opinion_id": worklist_row.get("lead_opinion_id"),
        "year": worklist_row.get("year"),
        "record_id": worklist_row.get("record_id"),
    }


def run_case_read(worklist_row, lens, run_id, budget, ledger_dir=RUN_DIR,
                  timeout_s=DEFAULT_TIMEOUT_S, mock=None):
    """Execute one blind case read (one lens). Emits an s9.read.v1 row. `mock`, if
    given, is a callable(prompt)->str returning a canned reply (self-test path,
    no live codex)."""
    case_id = worklist_row["case_id"]
    lane_id = "codex-%s-read-%s-%s" % (lens, run_id, _short(case_id))
    identity = _identity_payload_for(worklist_row)
    prompt = _case_prompt(lens)

    if not worklist_row.get("cached_text_present"):
        # fail-closed: no cached lead-opinion text -> route to live-CL identity
        # slice (out of this lane). Never fabricate a read.
        row = _read_row(worklist_row, lens, run_id, lane_id, identity,
                        parse_status="no_cached_text", conclusions=None,
                        wall=0.0, tokens=None, manifest_ref=None,
                        note="lead-opinion text absent from pool; routed to "
                             "live-CL identity slice (R5), NOT read here")
        return emit_and_return(row, ledger_dir)

    sandbox, sb_files = materialize_case_sandbox(
        worklist_row["cached_text_path"], identity, prompt)
    manifest = build_manifest(
        lane_id, "case-read", files_disclosed=sb_files,
        fields_excluded=["content_page", "lake.treatment", "lake.homes",
                         "lake.point_overrides", "thread_p"],
        ids=[case_id], identity_payload=identity, discovery=False,
        sandbox_dir=sandbox)
    manifest_ref = write_manifest(manifest)

    violations = validate_manifest(manifest, sandbox_files=sb_files)
    if violations:  # FAIL-CLOSED — never launch a leaky manifest
        shutil.rmtree(sandbox, ignore_errors=True)
        row = _read_row(worklist_row, lens, run_id, lane_id, identity,
                        parse_status="manifest_refused", conclusions=None,
                        wall=0.0, tokens=None, manifest_ref=manifest_ref,
                        note="manifest blindness violation (fail-closed): %s"
                             % "; ".join(violations))
        return emit_and_return(row, ledger_dir)

    # invocation 1
    result, obj, attempts, note = _read_with_repair(
        prompt, sandbox, timeout_s, budget, mock)

    if result.get("auth_error"):
        shutil.rmtree(sandbox, ignore_errors=True)
        raise AuthError(result.get("stderr_tail") or result.get("last_message"))

    parse_status = "parsed" if obj is not None else "no_read"
    if attempts > 1 and obj is not None:
        parse_status = "repaired"
    conclusions = _normalize_conclusions(obj, lens) if obj else None
    identity_assertion = (conclusions or {}).get("identity") if conclusions else None

    row = _read_row(worklist_row, lens, run_id, lane_id, identity,
                    parse_status=parse_status, conclusions=conclusions,
                    wall=result["wall_clock_s"], tokens=result["tokens"],
                    manifest_ref=manifest_ref, note=note,
                    identity_assertion=identity_assertion, attempts=attempts,
                    raw_message=result["last_message"])
    shutil.rmtree(sandbox, ignore_errors=True)
    return emit_and_return(row, ledger_dir)


class AuthError(Exception):
    pass


def _read_with_repair(prompt, sandbox, timeout_s, budget, mock):
    """Run the lane; on unparseable output re-run ONCE, then give up (no_read)."""
    if mock is not None:
        raw = mock(prompt)
        result = {"last_message": raw, "wall_clock_s": 0.0, "auth_error": False,
                  "tokens": {"total": None}, "stderr_tail": "", "timed_out": False,
                  "returncode": 0}
        obj = extract_json(raw)
        if obj is not None:
            return result, obj, 1, "mock parsed"
        raw2 = mock(prompt + "\n\nSTRICT: output ONLY valid JSON, no prose.")
        result2 = dict(result, last_message=raw2)
        obj2 = extract_json(raw2)
        if obj2 is not None:
            return result2, obj2, 2, "mock repaired on re-run"
        return result2, None, 2, "mock unparseable twice -> no_read"

    result = run_codex(prompt, sandbox, timeout_s=timeout_s, budget=budget)
    if result.get("auth_error"):
        return result, None, 1, "auth error"
    obj = extract_json(result["last_message"])
    if obj is not None:
        return result, obj, 1, "parsed first pass"
    if result.get("timed_out"):
        return result, None, 1, "timed out (no re-run)"
    # re-run ONCE with a strict-JSON nudge
    strict = prompt + "\n\nSTRICT: your ENTIRE reply must be ONE valid JSON " \
                      "object. No prose, no code fences."
    result2 = run_codex(strict, sandbox, timeout_s=timeout_s, budget=budget)
    if result2.get("auth_error"):
        return result2, None, 2, "auth error on re-run"
    obj2 = extract_json(result2["last_message"])
    if obj2 is not None:
        return result2, obj2, 2, "repaired on re-run"
    return result2, None, 2, "unparseable twice -> no_read"


def _normalize_conclusions(obj, lens):
    """Coerce the model object into the R5 structured-conclusion shape, tolerating
    missing keys (repair). The identity assertion is mandatory; if absent, it is
    recorded as present=False so the completeness gate can see the miss."""
    ident = obj.get("identity") or {}
    return {
        "identity": {
            "parties_in_text": ident.get("parties_in_text"),
            "caption_claimed": ident.get("caption_claimed"),
            "match": ident.get("match"),
            "present": bool(ident) and ("match" in ident),
        },
        "holding": obj.get("holding"),
        "disposition": obj.get("disposition"),
        "lens": obj.get("lens") or lens,
        "support": obj.get("support") if lens == "A" else None,
        "treatment": obj.get("treatment") if lens == "B" else None,
        "splits": obj.get("splits"),
        "notes": obj.get("notes"),
    }


def _read_row(wr, lens, run_id, lane_id, identity, parse_status, conclusions,
              wall, tokens, manifest_ref, note, identity_assertion=None,
              attempts=0, raw_message=None):
    return {
        "schema": "s9.read.v1",
        "id": lane_id,
        "run": run_id,
        "lane": "codex-%s" % lens,
        "model": CODEX_MODEL,
        "sandbox": "read-only (isolated temp; page/judgment/thread-P absent)",
        "lens": lens,
        "case_id": wr["case_id"],
        "record_id": wr["record_id"],
        "caption_claimed": wr["caption"],
        "cluster_id": wr.get("cluster_id"),
        "lead_opinion_id": wr.get("lead_opinion_id"),
        "cached_text_path": wr.get("cached_text_path"),
        "manifest_ref": _rel(manifest_ref) if manifest_ref else None,
        "identity_assertion": identity_assertion,
        "conclusions": conclusions,
        "parse": {"status": parse_status, "attempts": attempts, "note": note},
        "wall_clock_s": wall,
        "tokens": tokens,
        "recorded_before_reconciliation": True,
        "at": _now(),
    }


def emit_and_return(row, ledger_dir):
    emit_row(row, ledger_dir)
    return row


def _short(s):
    return hashlib.sha1((s or "").encode()).hexdigest()[:8]


def _rel(p):
    try:
        return os.path.relpath(p, REPO_ROOT)
    except ValueError:
        return p


# ==========================================================================
# 7. Panel-vote lane (the Opus lane for the pilot; s9.vote.v1)
# ==========================================================================

def make_vote_row(finding_id, verdict, reasons, lane="o2-opus-xhigh-pilot",
                  model="claude-opus-4-8", breaks_tp=False, residual=None,
                  tightening=None, manifest_ref=None):
    """Build an s9.vote.v1 row (recorded before any sibling vote / adjudication)."""
    return {
        "schema": "s9.vote.v1",
        "finding_id": finding_id,
        "lane": lane,
        "model": model,
        "sandbox": "n/a (Opus lane; manifest-isolated context)",
        "independent": "isolated manifest; no sibling votes or adjudications disclosed",
        "recorded_before_other_votes_read": True,
        "manifest_ref": _rel(manifest_ref) if manifest_ref else None,
        "verdict": verdict,           # refuted | stands | stands-modified
        "reasons": reasons,
        "breaks_true_positives": breaks_tp,
        "residual_risks": residual or [],
        "suggested_tightening": tightening,
        "at": _now(),
    }


def vote_manifest(lane_id, assertion_ids):
    """A reviewer/vote manifest that excludes sibling votes + in-progress
    adjudications (R1)."""
    return {
        "lane_id": lane_id,
        "lane_kind": "vote",
        "model": "claude-opus-4-8",
        "files_disclosed": [],   # assertion + cached-text evidence passed inline
        "fields_excluded": list(REQUIRED_REVIEW_EXCLUSIONS),
        "assertion_ids": list(assertion_ids),
        "discovery": False,
        "issued_at": _now(),
        "thread_p_hash_at_issue": thread_p_hash(),
    }


# ==========================================================================
# 8. Self-test (MOCK lane — no live codex)
# ==========================================================================

def self_test():
    errs = []

    # -- (a) manifest-violation detection --------------------------------
    good = build_manifest(
        "t-good", "case-read", files_disclosed=["opinion.txt", "identity.json"],
        fields_excluded=["content_page", "lake.treatment", "lake.homes", "thread_p"],
        ids=["P-c-x"], identity_payload={"caption_claimed": "A v. B",
                                         "cluster_id": 1, "lead_opinion_id": 2})
    if validate_manifest(good):
        errs.append("(a) clean blind manifest wrongly flagged: %s"
                    % validate_manifest(good))

    leak_page = build_manifest(
        "t-leak1", "case-read",
        files_disclosed=["opinion.txt", "content/cases/Terry v. Ohio.md"],
        fields_excluded=["content_page", "lake.treatment", "lake.homes", "thread_p"],
        ids=["P-c-x"])
    if not validate_manifest(leak_page):
        errs.append("(a) content-page leak NOT detected")

    leak_field = build_manifest(
        "t-leak2", "case-read", files_disclosed=["opinion.txt"],
        fields_excluded=["content_page", "lake.treatment", "lake.homes", "thread_p"],
        ids=["P-c-x"], identity_payload={"caption_claimed": "A v. B",
                                         "treatment": {"good_law": True}})
    if not any("judgment" in x for x in validate_manifest(leak_field)):
        errs.append("(a) judgment-field leak in identity NOT detected")

    leak_p = build_manifest(
        "t-leak3", "case-read",
        files_disclosed=["opinion.txt", "_run/s9/thread-P.json"],
        fields_excluded=["content_page", "lake.treatment", "lake.homes", "thread_p"],
        ids=["P-c-x"])
    if not validate_manifest(leak_p):
        errs.append("(a) thread-P leak NOT detected")

    missing_excl = build_manifest(
        "t-excl", "case-read", files_disclosed=["opinion.txt"],
        fields_excluded=["content_page"], ids=["P-c-x"],
        identity_payload={"caption_claimed": "A v. B"})
    if not any("omits required exclusion" in x for x in validate_manifest(missing_excl)):
        errs.append("(a) missing-required-exclusion NOT detected")

    vote_leak = {"lane_kind": "vote",
                 "files_disclosed": ["votes.jsonl"],
                 "fields_excluded": list(REQUIRED_REVIEW_EXCLUSIONS)}
    if not validate_manifest(vote_leak):
        errs.append("(a) reviewer sibling-vote leak NOT detected")

    # -- (b) prose-wrap repair -------------------------------------------
    prose = ('Sure — here is my analysis.\n```json\n'
             '{"identity": {"parties_in_text": "X v. Y", '
             '"caption_claimed": "X v. Y", "match": true}, "holding": "h"}\n'
             '```\nHope that helps!')
    obj = extract_json(prose)
    if not (obj and obj.get("holding") == "h"):
        errs.append("(b) fenced prose-wrapped JSON not repaired")
    braces = 'blah {"a": {"b": 1}, "holding": "z"} trailing'
    if extract_json(braces) is None:
        errs.append("(b) balanced-brace extraction failed")
    if extract_json("no json here at all") is not None:
        errs.append("(b) false-positive JSON extraction")

    # -- (c) no-read fallback via MOCK lane (unparseable twice) ----------
    calls = {"n": 0}

    def mock_garbage(_prompt):
        calls["n"] += 1
        return "I cannot produce JSON, sorry."  # never parseable

    wr = {"case_id": "P-c-mock", "record_id": "Mock v. Test",
          "caption": "Mock v. Test", "cluster_id": 1, "lead_opinion_id": 2,
          "citation": "1 U.S. 1", "court_level": "scotus", "year": 2000,
          "cached_text_present": True,
          "cached_text_path": os.path.join(TEXT_DIR, "does-not-matter.txt")}
    tmp_ledger = tempfile.mkdtemp(prefix="s9-selftest-ledger-")
    # patch materialize to a throwaway sandbox (mock never reads the file)
    sb = tempfile.mkdtemp(prefix="s9-selftest-sb-")
    open(os.path.join(sb, "opinion.txt"), "w").write("mock")
    try:
        row = run_case_read(_wr_with_sandbox(wr, sb), "A", "selftest",
                            InvocationBudget(cap=99), ledger_dir=tmp_ledger,
                            mock=mock_garbage)
    finally:
        shutil.rmtree(sb, ignore_errors=True)
    if row["parse"]["status"] != "no_read":
        errs.append("(c) unparseable-twice did not fall to no_read (got %s)"
                    % row["parse"]["status"])
    if calls["n"] != 2:
        errs.append("(c) no-read fallback did not re-run exactly once (n=%d)"
                    % calls["n"])

    # repaired-on-re-run path
    calls2 = {"n": 0}

    def mock_repair(_prompt):
        calls2["n"] += 1
        if calls2["n"] == 1:
            return "here you go: not json"
        return '{"identity": {"parties_in_text":"M v. T","caption_claimed":"Mock v. Test","match":false}, "holding":"h", "lens":"A"}'

    sb2 = tempfile.mkdtemp(prefix="s9-selftest-sb2-")
    open(os.path.join(sb2, "opinion.txt"), "w").write("mock")
    try:
        row2 = run_case_read(_wr_with_sandbox(wr, sb2), "A", "selftest",
                             InvocationBudget(cap=99), ledger_dir=tmp_ledger,
                             mock=mock_repair)
    finally:
        shutil.rmtree(sb2, ignore_errors=True)
    if row2["parse"]["status"] != "repaired":
        errs.append("(c) repair-on-re-run not recorded as 'repaired' (got %s)"
                    % row2["parse"]["status"])
    if not (row2.get("identity_assertion") and
            "match" in (row2["identity_assertion"] or {})):
        errs.append("(c) mandatory identity assertion missing from repaired read")

    # -- (d) row validity vs LINT-30 (complete mock ledger reconciles) ---
    demo_dir = tempfile.mkdtemp(prefix="s9-selftest-l30-")
    _write_mock_reconciling_ledger(demo_dir)
    viols, status = check_ledger.check_ledger(demo_dir)
    nh = sum(1 for x in viols if x["severity"] == check_ledger.c.HIGH)
    if status != "CHECKED" or nh != 0:
        errs.append("(d) mock complete ledger not LINT-30 green: status=%s HIGH=%d %s"
                    % (status, nh, [x["message"][:50] for x in viols][:3]))
    shutil.rmtree(demo_dir, ignore_errors=True)
    shutil.rmtree(tmp_ledger, ignore_errors=True)

    for e in errs:
        sys.stderr.write("[self-test] FAIL: %s\n" % e)
    sys.stderr.write("[self-test] lane_runner %s (%d check-group breaches)\n"
                     % ("PASS" if not errs else "FAIL", len(errs)))
    return 0 if not errs else 1


def _wr_with_sandbox(wr, sb):
    """For the mock path: point cached_text_path at a throwaway sandbox file so
    materialize_case_sandbox succeeds without the real pool."""
    w = dict(wr)
    w["cached_text_path"] = os.path.join(sb, "opinion.txt")
    return w


def _write_mock_reconciling_ledger(d):
    """A complete, internally-consistent 4-file ledger that satisfies all five
    LINT-30 invariants — proves the harness's row shapes reconcile green."""
    finding = {"schema": "s9.finding.v1", "id": "F-MOCK-1", "run": "selftest",
               "object": "content/cases/Mock.md", "object_class": "case",
               "dimension": "D1", "gate": "G1", "assertion_id": None,
               "locator": {"section": "x", "lines": "1", "verbatim": "y"},
               "problem": "mock", "severity": "high", "proposed_fix": "z",
               "needs_cl": False,
               "found_by": {"lane": "codex-A", "model": "gpt-5.5"},
               "confidence": 0.9}
    votes = [
        make_vote_row("F-MOCK-1", "refuted", ["r1"], lane="codex-A", model="gpt-5.5"),
        make_vote_row("F-MOCK-1", "refuted", ["r2"], lane="codex-B", model="gpt-5.5"),
        make_vote_row("F-MOCK-1", "stands-modified", ["r3"], lane="claude",
                      model="claude-opus-4-8"),
    ]
    adj = {"schema": "s9.adjudication.v1", "finding_id": "F-MOCK-1",
           "refute_tally": {"codex-A": "refuted", "codex-B": "refuted",
                            "claude": "stands-modified",
                            "rule": ">=2-of-3 refute kills", "result": "KILLED"},
           "verdict": "MODIFIED",
           "adjudicated_holding": ["mock modified holding"],
           "evidence": [{"kind": "lake", "ref": "mock"}],
           "adjudicator": {"lane": "claude", "model": "claude-opus-4-8"},
           "role_separation": "finder codex-A != adjudicator claude",
           "spawned_findings": [], "at": _now()}
    fix = {"schema": "s9.fix.v1", "finding_id": "F-MOCK-1",
           "adjudication_verdict": "MODIFIED",
           "applied_by": {"lane": "claude", "model": "claude-opus-4-8"},
           "artifacts": ["mock"], "content_edits": "none",
           "loops": [{"loop": 1, "re_review": {"lane": "codex-C", "model": "gpt-5.5",
                                               "round": 1, "verdict": "FIXED"}}],
           "loop_cap": 3, "writer_neq_checker": "author claude != reviewer codex-C",
           "at": _now()}
    with open(os.path.join(d, "findings.jsonl"), "w") as f:
        f.write(json.dumps(finding) + "\n")
    with open(os.path.join(d, "votes.jsonl"), "w") as f:
        for v in votes:
            f.write(json.dumps(v) + "\n")
    with open(os.path.join(d, "adjudications.jsonl"), "w") as f:
        f.write(json.dumps(adj) + "\n")
    with open(os.path.join(d, "fixes.jsonl"), "w") as f:
        f.write(json.dumps(fix) + "\n")


# ==========================================================================
# 9. CLI
# ==========================================================================

def _load_worklist_rows(record_ids):
    wl = os.path.join(RUN_DIR, "worklists", "thread-n-cases.jsonl")
    rows = {}
    with open(wl, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r["record_id"] in record_ids:
                rows[r["record_id"]] = r
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--case-read", metavar="RECORD_ID",
                    help="run one live blind case read")
    ap.add_argument("--lens", choices=["A", "B"], default="A")
    ap.add_argument("--run-id", default="p1-h")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)
    ap.add_argument("--ledger-dir", default=RUN_DIR)
    # --- R1 sighted panel-review modes (lazy-dispatched to panel_review.py so the
    #     ONE invocation path stays here without a bloated/circular import) ---
    ap.add_argument("--panel-review", metavar="GROUP_ID",
                    help="run ONE Codex lens over one panel-review group")
    ap.add_argument("--panel-review-opus", metavar="GROUP_IDS",
                    help="generate the Opus prompt-pack for comma-separated groups")
    ap.add_argument("--batch-id", default="opus-batch-1")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--cap", type=int, default=INVOCATION_CAP)
    ap.add_argument("--self-test-panel", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        sys.exit(self_test())

    if args.self_test_panel or args.panel_review or args.panel_review_opus:
        import panel_review  # lazy: panel_review imports us -> avoid import cycle
        if args.self_test_panel:
            sys.exit(panel_review.self_test_panel())
        if args.panel_review_opus:
            gids = [g.strip() for g in args.panel_review_opus.split(",") if g.strip()]
            out = panel_review.generate_opus_pack(gids, args.batch_id,
                                                  out_dir=args.out_dir)
            sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
            sys.exit(0)
        try:
            summary = panel_review.run_panel_review(
                args.panel_review, args.lens, args.run_id,
                InvocationBudget(cap=args.cap), ledger_dir=args.ledger_dir,
                timeout_s=args.timeout)
        except AuthError as e:
            sys.stderr.write("AUTH-CLASS CODEX FAILURE (pause-#8 surface):\n%s\n" % e)
            sys.exit(3)
        sys.stdout.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        sys.exit(0)

    if args.case_read:
        rows = _load_worklist_rows({args.case_read})
        if args.case_read not in rows:
            sys.exit("record not in worklist: %s" % args.case_read)
        try:
            row = run_case_read(rows[args.case_read], args.lens, args.run_id,
                                InvocationBudget(), ledger_dir=args.ledger_dir,
                                timeout_s=args.timeout)
        except AuthError as e:
            sys.stderr.write("AUTH-CLASS CODEX FAILURE (pause-#8 surface):\n%s\n" % e)
            sys.exit(3)
        sys.stdout.write(json.dumps(row, ensure_ascii=False, indent=2) + "\n")
        sys.exit(0)

    ap.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
