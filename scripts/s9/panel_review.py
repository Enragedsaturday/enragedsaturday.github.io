#!/usr/bin/env python3
"""
S9 R1 panel-review machinery — the sighted 3-lane adversarial panel over every
legal-assertion surface (existence / support / quote-fidelity / pincite /
treatment / black-letter), built ON TOP of the frozen lane_runner harness (spec
S9 R1). We import lane_runner's isolation mechanics (manifest emission +
fail-closed blindness validation, the fresh-`codex exec` read-only sandbox
launcher, the prose-wrap JSON repair, the append-safe row emitter) and EXTEND
them — never fork them.

What is different from the blind Thread-N case-read (lane_runner §6):
  * lane_kind = "review" (NOT a BLIND_KIND). The manifest DISCLOSES the object's
    content page + its FULL lake record (judgment fields INCLUDED — a sighted
    reviewer sees treatment/homes, unlike the blind Thread-N reader) + the
    relevant cached opinion texts + the group's assertion-inventory rows. It
    STILL fail-closed-excludes sibling votes and in-progress adjudications
    (REQUIRED_REVIEW_EXCLUSIONS, R1) — validate_manifest refuses to launch a
    manifest that discloses a votes/adjudications surface.
  * refute-framed, default-refute-on-uncertainty (R1): each lens is an
    adversarial refuter. Lens A attacks support / quote-fidelity (+ existence,
    pincite, black-letter). Lens B attacks currency / treatment. Uncertainty
    defaults to REFUTED; a claim it cannot verify from the DISCLOSED evidence is
    flagged unverifiable (routed out / defaulted refuted) — never fabricated.
  * output contract: s9.finding.v1 rows are emitted ONLY for defects; a lens
    that finds no defect across the whole group emits ONE per-group clean
    attestation (s9.attestation.v1 -> panel-attestations.jsonl). s9.vote.v1 rows
    are emitted on any finding the lens reviews (its own refutations, and
    defense "stands" votes on findings a sibling already raised). Finding ids are
    DETERMINISTIC in (object, assertion_id, dimension) so the two Codex lenses
    and the Opus lane converge on the same finding_id and the orchestrator can
    tally >=2-of-3 refute. Every lens invocation also persists its FULL
    per-assertion verdict map to panel-results/<lane-id>.json so the orchestrator
    can backfill any vote a lens could not link at write time (blind, serial).

The Claude/Opus leg is NOT run here: `--panel-review-opus` writes a prompt-pack
(the exact review-form prompt + inlined disclosure set + audit manifest) that
o2-opus-xhigh Agent lanes run N-groups-per-invocation with identical framing;
the orchestrator dispatches those and emits their rows through the same contract.

Writer != checker: this lane FINDS and VOTES; it never adjudicates, never closes
its own row. Adjudication (the >=2-of-3 tally) and fixes are the orchestrator's.

`--self-test-panel` runs a MOCK lane (no live codex) proving: group resolution,
review-manifest validity + a fail-closed leak refusal, deterministic finding ids
+ cross-lens dedup, defect->finding+vote / clean->attestation, prose-wrap repair
+ unparseable-twice->no_review (no fabricated finding), and a complete mock panel
ledger reconciling green under LINT-30.

Stdlib only. COMMIT NOTHING. Content/lake read-only. Zero CL anywhere.
"""

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lane_runner as lr  # noqa: E402  (import + extend the frozen harness; don't fork)
import check_ledger  # noqa: E402  (LINT-30 on the result)

REPO_ROOT = lr.REPO_ROOT
RUN_DIR = lr.RUN_DIR
POOL_TEXT_DIR = lr.TEXT_DIR

INVENTORY_PATH = os.path.join(RUN_DIR, "assertion-inventory.json")
PANEL_WORKLIST = os.path.join(RUN_DIR, "worklists", "panel-review.jsonl")
PANEL_WORKLIST_V2 = os.path.join(RUN_DIR, "worklists", "panel-review.v2.jsonl")
LAKE_CASES_DIR = os.path.join(REPO_ROOT, "_overhaul2", "lake", "cases")

# coordinator scope rulings (ratified commit e010136):
#  (a) the ledger-row 964-pincite singleton EXITS the Codex panel (-> the
#      orchestrator's R9(b) Claude-lane >=1-in-10 sample). Excluded from v2.
#  (b) reference/craft groups whose existence rows carry substantive holding
#      text get PROMOTED to text-dependent disclosure (cited-case texts shown).
#  (c) the 80-black_letter registry singleton -> 3 shards of ~27.
LEDGER_ROW_OBJECT = os.path.join("_run", "s8-link-ledger.json")
REGISTRY_OBJECT = os.path.join("_overhaul2", "points", "registry.yaml")
REGISTRY_SHARD_COUNT = 3
TEXT_PROMOTE_CAP = 12   # max cited-case texts to disclose for a promoted group

CODEX_MODEL = lr.CODEX_MODEL          # gpt-5.5
OPUS_MODEL = "claude-opus-4-8"        # the model-diversity panel lane
PILOT_INVOCATION_CAP = 6              # 3 groups x 2 lenses, SERIAL (fleet at conc-6)

# the six paneled legal-assertion surfaces (R1) -> finding dimension + gate.
# All are LEGAL dimensions (never D-TOOL) so LINT-30 inv3 finder!=adjudicator
# binds: this lane FINDS (codex/opus), the orchestrator ADJUDICATES.
PANEL_DIM_D = {"existence": "D2", "support": "D4", "quote_fidelity": "D3",
               "pincite": "D5", "treatment": "D6", "black_letter": "D7"}
PANEL_DIM_GATE = {"existence": "G1", "support": "G2", "quote_fidelity": "G3",
                  "pincite": "G4", "treatment": "G7", "black_letter": "G2"}
PANEL_DIMS = ("existence", "support", "quote_fidelity", "pincite",
              "treatment", "black_letter")

# dimensions whose verification needs the OPINION TEXT (not just the lake record).
# existence (citation match) + treatment (good-law call vs the lake's own
# progeny/treatment fields) verify against the FULL lake record alone; disclosing
# the cached opinion text for those is pure token cost. This is the economy lever
# that keeps existence-only reference/index groups cheap.
TEXT_DEPENDENT_DIMS = frozenset(
    {"support", "quote_fidelity", "pincite", "black_letter"})

# which paneled dimensions each Codex lens is chartered to attack (R1 lens
# diversity). Each lens still REVIEWS the whole group, but its finding-raising
# authority is scoped to its charter; out-of-charter surfaces it defers on
# (records a verdict for the orchestrator, raises no finding).
LENS_CHARTER = {
    "A": frozenset({"existence", "support", "quote_fidelity", "pincite",
                    "black_letter"}),   # support / quote-fidelity attack
    "B": frozenset({"existence", "treatment"}),  # currency / treatment attack
}


# HARD auth markers = a genuine credential/model-auth stop (pause-#8). Soft
# markers ("credential"/"expired"/"authentication") appear in token-refresh
# noise and in codex's "reading additional input from stdin" hiccup, so they do
# NOT by themselves prove a systemic stop.
_HARD_AUTH_MARKERS = ("not logged in", "unauthorized", "401", "403",
                      "invalid api key", "please run `codex login`", "no api key")


def _hard_auth(blob):
    return any(m in (blob or "") for m in _HARD_AUTH_MARKERS)


# ==========================================================================
# 1. Inventory + worklist indexing
# ==========================================================================

_INV_CACHE = {"path": None, "by_id": None}


def load_inventory_index(path=INVENTORY_PATH):
    """{assertion_id -> item}. Cached (the inventory is ~12MB)."""
    if _INV_CACHE["path"] == path and _INV_CACHE["by_id"] is not None:
        return _INV_CACHE["by_id"]
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    items = d.get("items") if isinstance(d, dict) else d
    by_id = {it["assertion_id"]: it for it in items}
    _INV_CACHE.update(path=path, by_id=by_id)
    return by_id


def load_worklist_index(path=PANEL_WORKLIST):
    """{object -> worklist row}. The group id IS the object path (unique)."""
    idx = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            idx[r["object"]] = r
    return idx


def _has_holding_cells(row, inv_by_id):
    for aid in row.get("dimensions", {}).get("existence", []):
        pay = (inv_by_id.get(aid) or {}).get("payload") or {}
        if isinstance(pay.get("cells"), list) and len(pay["cells"]) >= 2:
            return True
    return False


def _should_text_promote(row, inv_by_id):
    """(b): reference/craft groups whose existence rows carry substantive holding
    text (a Case|Holding|Opinion table cell)."""
    if row.get("object_class") == "reference":
        return _has_holding_cells(row, inv_by_id)
    if "/instructor-craft-and-study/" in (row.get("object") or ""):
        return _has_holding_cells(row, inv_by_id)
    return False


def _tier_map():
    """{caption/record_id -> tier_rank} from the thread-n case worklist (R5
    tiering: recency=0, negatives=1, rule-bearing=2, high-profile=3, rest=4)."""
    m = {}
    p = os.path.join(RUN_DIR, "worklists", "thread-n-cases.jsonl")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                tr = r.get("tier_rank", 4)
                for k in (r.get("caption"), r.get("record_id")):
                    if k:
                        m[k] = tr
    return m


def _group_tier_rank(row, tmap):
    oc = row.get("object_class")
    base = os.path.splitext(os.path.basename((row.get("object") or "").split("#")[0]))[0]
    if oc in ("case", "lake-record"):
        return tmap.get(base, 4)
    if oc == "registry":
        return 1   # black-letter rules: high value + the >=2-approval gate
    if oc in ("doctrine", "reference"):
        return 2   # rule-bearing / craft pages
    return 4


def revise_panel_worklist(src=PANEL_WORKLIST, dst=PANEL_WORKLIST_V2,
                          inv_by_id=None, shard_count=REGISTRY_SHARD_COUNT):
    """Apply the ratified scope rulings and write panel-review.v2.jsonl:
      (a) DROP the ledger-row 964-pincite singleton (-> R9(b) Claude lane).
      (b) TAG reference/craft holding-table groups with text_promote=true.
      (c) SHARD the 80-black_letter registry singleton into `shard_count` shards
          (object = 'registry.yaml#shard-<n>', black_letter ids sliced evenly).
    Returns a summary dict."""
    inv_by_id = inv_by_id if inv_by_id is not None else load_inventory_index()
    rows_out, dropped, promoted, shards = [], 0, 0, 0
    with open(src, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            oc = r.get("object_class")
            if oc == "ledger-row" and r.get("object") == LEDGER_ROW_OBJECT:
                dropped += 1
                continue    # (a) exits the Codex panel
            if oc == "registry" and r.get("object") == REGISTRY_OBJECT:
                bl = list(r["dimensions"].get("black_letter", []))
                n = len(bl)
                size = (n + shard_count - 1) // shard_count
                for i in range(shard_count):
                    chunk = bl[i * size:(i + 1) * size]
                    if not chunk:
                        continue
                    shards += 1
                    sr = {
                        "schema": "s9.worklist.panel.v1",
                        "object": "%s#shard-%d" % (REGISTRY_OBJECT, i + 1),
                        "object_class": "registry",
                        "page_batch": r.get("page_batch", 0),
                        "page_ordinal": r.get("page_ordinal", 0),
                        "dimensions": {d: [] for d in PANEL_DIMS},
                        "counts": {d: 0 for d in PANEL_DIMS},
                        "total": len(chunk),
                        "black_letter_needs_2_approvals": True,
                        "shard_of": REGISTRY_OBJECT,
                        "shard_index": i + 1, "shard_count": shard_count,
                    }
                    sr["dimensions"]["black_letter"] = chunk
                    sr["counts"]["black_letter"] = len(chunk)
                    rows_out.append(sr)
                continue    # (c) replaced by shards
            if _should_text_promote(r, inv_by_id):
                r = dict(r, text_promote=True)
                promoted += 1
            rows_out.append(r)
    # (ordering) sort by R5 tier so recency/negatives lead, then renumber
    # page_ordinal/page_batch so the driver's file-order pass is tier-ordered.
    tmap = _tier_map()
    rows_out.sort(key=lambda r: (_group_tier_rank(r, tmap), r.get("object") or ""))
    for i, r in enumerate(rows_out):
        r["tier_rank"] = _group_tier_rank(r, tmap)
        r["page_ordinal"] = i
        r["page_batch"] = i // 12
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "w", encoding="utf-8") as f:
        for r in rows_out:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n")
    return {"dst": dst, "groups": len(rows_out), "dropped_ledger_row": dropped,
            "text_promoted": promoted, "registry_shards": shards}


# ==========================================================================
# 2. Group resolution — object -> disclosure set (content / lake / texts / rows)
# ==========================================================================

def _case_name_of(item):
    loc = item.get("locator") or {}
    pay = item.get("payload") or {}
    return (loc.get("case") or pay.get("case") or pay.get("title")
            or loc.get("record_id") or pay.get("record_id"))


def _lake_path_for(case_name):
    p = os.path.join(LAKE_CASES_DIR, "%s.json" % case_name)
    return p if os.path.exists(p) else None


def resolve_content_page(obj, object_class):
    """The object's content page. case/doctrine/reference -> the object itself;
    lake-record -> the sibling content/cases page; registry/ledger-row -> the
    object file (its own content). A '#shard-N' suffix is stripped to the real
    file. Returns (abs_path_or_None, note)."""
    obj = obj.split("#", 1)[0]   # strip a shard suffix (registry shards)
    if object_class in ("case", "doctrine", "reference", "registry",
                        "ledger-row"):
        p = os.path.join(REPO_ROOT, obj)
        return (p, None) if os.path.exists(p) else (None, "content page absent: %s" % obj)
    if object_class == "lake-record":
        base = os.path.splitext(os.path.basename(obj))[0]
        p = os.path.join(REPO_ROOT, "content", "cases", "%s.md" % base)
        return (p, None) if os.path.exists(p) else (None, "no content page for lake record %s" % base)
    p = os.path.join(REPO_ROOT, obj)
    return (p, None) if os.path.exists(p) else (None, "unresolved object %s" % obj)


def resolve_group(group_id, worklist_idx=None, inv_by_id=None, text_dir=None):
    """Resolve a panel-review group id (= object path) into its full disclosure
    set. Fail-closed: unresolved evidence is RECORDED (as a note + a lake_only /
    absent flag), never silently dropped and never fabricated."""
    text_dir = text_dir or POOL_TEXT_DIR   # late-bound: self-test patches the global
    worklist_idx = worklist_idx or load_worklist_index()
    inv_by_id = inv_by_id if inv_by_id is not None else load_inventory_index()
    if group_id not in worklist_idx:
        raise KeyError("group not in panel-review worklist: %s" % group_id)
    wl = worklist_idx[group_id]
    obj = wl["object"]
    oc = wl["object_class"]

    text_promote = bool(wl.get("text_promote"))   # (b) ruling
    # the group's inventory rows, by dimension
    rows = []
    dims_present = set()
    text_dep_cases = set()   # case names whose assertions need opinion text
    for dim, ids in wl["dimensions"].items():
        for aid in ids:
            it = inv_by_id.get(aid)
            if it is None:
                rows.append({"assertion_id": aid, "dimension": dim,
                             "MISSING_FROM_INVENTORY": True})
                continue
            row = {"assertion_id": aid, "dimension": dim, "kind": it.get("kind"),
                   "locator": it.get("locator"), "payload": it.get("payload")}
            rows.append(row)
            dims_present.add(dim)
            cn = _case_name_of(it)
            # text-dependent by dimension, OR promoted existence rows carrying
            # substantive holding text (ruling (b)) -> disclose the opinion text
            if cn and (dim in TEXT_DEPENDENT_DIMS or text_promote):
                text_dep_cases.add(cn)
    if text_promote and len(text_dep_cases) > TEXT_PROMOTE_CAP:
        # bound the disclosure (record which were held back to lake-only)
        keep = sorted(text_dep_cases)[:TEXT_PROMOTE_CAP]
        text_dep_cases = set(keep)

    # cases named across the group (+ the object's own case for case/lake-record)
    named = set()
    for it_id in [r["assertion_id"] for r in rows]:
        it = inv_by_id.get(it_id)
        if it:
            cn = _case_name_of(it)
            if cn:
                named.add(cn)
    if oc in ("case", "lake-record"):
        own = os.path.splitext(os.path.basename(obj))[0]
        named.add(own)
        if any(r["dimension"] in TEXT_DEPENDENT_DIMS for r in rows) or \
           "treatment" in dims_present:
            text_dep_cases.add(own)  # single-case group: its own text is cheap

    # lake records (FULL — judgment fields disclosed) + cached texts
    lake_records = {}   # case_name -> abs lake path
    cached_texts = {}   # case_name -> abs text path (only text-dependent cases)
    notes = []
    for cn in sorted(named):
        lp = _lake_path_for(cn)
        if lp is None:
            notes.append("no lake record for case '%s'" % cn)
            continue
        lake_records[cn] = lp
        if cn in text_dep_cases:
            try:
                with open(lp, encoding="utf-8") as f:
                    lead = (json.load(f).get("identity") or {}).get("lead_opinion_id")
            except (OSError, ValueError):
                lead = None
            if lead is None:
                notes.append("case '%s' has no lead_opinion_id (text undisclosed)" % cn)
                continue
            tp = os.path.join(text_dir, "%s.txt" % lead)
            if os.path.exists(tp):
                cached_texts[cn] = tp
            else:
                notes.append("cached text absent for case '%s' (lead %s); lake-only" % (cn, lead))

    content_page, cp_note = resolve_content_page(obj, oc)
    if cp_note:
        notes.append(cp_note)

    return {
        "group_id": group_id,
        "object": obj,
        "object_class": oc,
        "dimensions": {d: list(wl["dimensions"].get(d, [])) for d in PANEL_DIMS},
        "counts": wl.get("counts"),
        "total": wl.get("total"),
        "black_letter_needs_2_approvals": wl.get("black_letter_needs_2_approvals", False),
        "inventory_rows": rows,
        "content_page": content_page,
        "lake_records": lake_records,     # case -> lake path (FULL record)
        "cached_texts": cached_texts,     # case -> opinion text path (text-dep only)
        "cases_named": sorted(named),
        "text_disclosed_cases": sorted(cached_texts.keys()),
        "lake_only_cases": sorted(set(lake_records) - set(cached_texts)),
        "resolution_notes": notes,
    }


# ==========================================================================
# 3. Sandbox — a temp dir OUTSIDE the repo holding ONLY the disclosure set
# ==========================================================================

def _safe_name(case_name):
    # keep readable but filesystem-safe; disambiguate collisions by a short hash
    stem = case_name.replace("/", "_").replace(":", "_")
    return "%s__%s" % (stem[:60], hashlib.sha1(case_name.encode()).hexdigest()[:6])


def materialize_panel_sandbox(resolved, task_md):
    """Create an isolated read-only sandbox holding ONLY the disclosed evidence.
    Returns (sandbox_dir, sandbox_files, evidence_index). Files:
      content_page.<ext>          — the object's content page
      lake/<case>.json            — FULL lake record(s) (judgment fields included)
      text/<case>.txt             — cached opinion text (text-dependent cases only)
      group_inventory.jsonl       — the group's assertion-inventory rows
      task.md                     — the lens review form
    NB: no file is named votes.jsonl / adjudications.jsonl / *.vote.json /
    *.adjudication.json, so the review-manifest blindness guard passes."""
    sb = tempfile.mkdtemp(prefix="s9-panel-")
    files = []
    evidence = {"content_page": None, "lake_records": {}, "cached_texts": {},
                "inventory": "group_inventory.jsonl"}

    cp = resolved["content_page"]
    if cp:
        ext = os.path.splitext(cp)[1] or ".md"
        dest = "content_page%s" % ext
        shutil.copyfile(cp, os.path.join(sb, dest))
        files.append(dest)
        evidence["content_page"] = dest

    os.makedirs(os.path.join(sb, "lake"), exist_ok=True)
    for cn, lp in sorted(resolved["lake_records"].items()):
        dest = os.path.join("lake", "%s.json" % _safe_name(cn))
        shutil.copyfile(lp, os.path.join(sb, dest))
        files.append(dest)
        evidence["lake_records"][cn] = dest

    if resolved["cached_texts"]:
        os.makedirs(os.path.join(sb, "text"), exist_ok=True)
        for cn, tp in sorted(resolved["cached_texts"].items()):
            dest = os.path.join("text", "%s.txt" % _safe_name(cn))
            shutil.copyfile(tp, os.path.join(sb, dest))
            files.append(dest)
            evidence["cached_texts"][cn] = dest

    with open(os.path.join(sb, "group_inventory.jsonl"), "w", encoding="utf-8") as f:
        for r in resolved["inventory_rows"]:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    files.append("group_inventory.jsonl")

    with open(os.path.join(sb, "task.md"), "w", encoding="utf-8") as f:
        f.write(task_md)
    files.append("task.md")

    return sb, files, evidence


# ==========================================================================
# 4. Review-form prompts (refute-framed, default-refute-on-uncertainty — R1)
# ==========================================================================

_PANEL_PREAMBLE = (
    "You are an ADVERSARIAL PANEL REVIEWER for a federal search-and-seizure "
    "legal-reference corpus. Your job is to REFUTE — to try, in good faith and "
    "hard, to break every assertion in this review group.\n\n"
    "GROUND RULES (non-negotiable):\n"
    "  * Your ENTIRE evidentiary universe is the files in your working directory. "
    "Do NOT search. Do NOT use any knowledge not confirmable from these files.\n"
    "  * content_page.*  = the built page whose assertions are under review.\n"
    "  * lake/<case>.json = the FULL authority record for a cited case "
    "(identity, citation, pinpoints[].quote, treatment/good-law fields, "
    "progeny edges). You MAY rely on its judgment fields — you are a SIGHTED "
    "reviewer.\n"
    "  * text/<case>.txt = the cached full opinion text (present only for cases "
    "whose assertions need verbatim/holding checks).\n"
    "  * group_inventory.jsonl = one row per assertion under review "
    "{assertion_id, dimension, kind, locator, payload}. Review EVERY row.\n"
    "  * DEFAULT TO REFUTED ON UNCERTAINTY. If you cannot verify an assertion "
    "from the disclosed evidence, do NOT guess: set verdict='refuted', "
    "verifiable_from_disclosed=false, and say what evidence you'd need. "
    "Never fabricate a cite, quote, or holding.\n\n"
)

_LENS_CHARTER_TEXT = {
    "A": (
        "YOUR ATTACK LENS = A (SUPPORT / QUOTE-FIDELITY). Attack, per assertion:\n"
        "  - existence: does the cited case exist and is the citation "
        "(reporter/court/year) exactly right vs the lake record?\n"
        "  - support: does the stated proposition/holding/home-role ACTUALLY "
        "follow from the opinion text and the lake holding — at the stated "
        "breadth, no overclaim (per-item, if enumerated)?\n"
        "  - quote_fidelity: is every verbatim quote character-faithful to "
        "text/<case>.txt or the lake pinpoints[].quote?\n"
        "  - pincite: does the pin land on the passage it claims?\n"
        "  - black_letter: is the black-letter rule text accurate and supported "
        "(it additionally needs >=2 affirmative approvals to stand).\n"
        "  Treatment/currency is NOT your charter — record a verdict but raise "
        "no treatment finding (lens B owns it).\n"
    ),
    "B": (
        "YOUR ATTACK LENS = B (CURRENCY / TREATMENT). Attack, per assertion:\n"
        "  - treatment: is the good-law / treatment call correct as of its date, "
        "consistent with the lake treatment fields and progeny edges? Is a weight "
        "label right? Has anything in the disclosed record superseded/overruled/"
        "abrogated/limited it?\n"
        "  - existence (currency angle): is the cited authority still live law?\n"
        "  Support/quote-fidelity is NOT your charter — record a verdict but "
        "raise no support/quote finding (lens A owns it).\n"
    ),
}

_PANEL_OUTPUT_CONTRACT = (
    "\nOUTPUT CONTRACT — return ONE JSON object, nothing else:\n"
    "{\n"
    '  "lens": "A" | "B",\n'
    '  "group_id": "<echo the group id>",\n'
    '  "reviewed": [\n'
    "    {\n"
    '      "assertion_id": "<from group_inventory.jsonl>",\n'
    '      "dimension": "existence|support|quote_fidelity|pincite|treatment|black_letter",\n'
    '      "verdict": "stands" | "refuted" | "stands-modified",\n'
    '      "verifiable_from_disclosed": true | false,\n'
    '      "defect": null,   // null when verdict=="stands"; else an object:\n'
    "      //  {\"problem\": \"...\", \"severity\": \"high|medium|low\", "
    "\"proposed_fix\": \"...\", \"evidence_quote\": \"verbatim from disclosed "
    "evidence or null\", \"needs_cl\": true|false, \"locator_note\": \"...\"}\n"
    '      "reasons": ["short evidence-grounded reason", "..."],\n'
    '      "breaks_true_positives": true | false,\n'
    '      "residual_risks": ["..."],\n'
    '      "suggested_tightening": "... or null"\n'
    "    }\n"
    "  ],\n"
    '  "notes": ""\n'
    "}\n"
    "Rules: verdict=='stands' <=> defect==null (assertion survives your attack). "
    "verdict=='refuted' <=> a real defect (the assertion as framed is wrong). "
    "verdict=='stands-modified' <=> survives but needs a stated modification "
    "(a minor defect). Review EVERY assertion_id in group_inventory.jsonl "
    "exactly once. Output ONLY the JSON object."
)


def panel_prompt(lens, group_id):
    return (_PANEL_PREAMBLE + _LENS_CHARTER_TEXT[lens]
            + "\nThe group under review is: %s\n" % group_id
            + _PANEL_OUTPUT_CONTRACT)


# ==========================================================================
# 5. Deterministic finding ids + row builders
# ==========================================================================

def finding_id_for(obj, assertion_id, dimension):
    """Deterministic in (object, assertion_id, dimension) so both Codex lenses
    and the Opus lane converge on ONE finding id per defect -> the orchestrator
    can tally >=2-of-3 refute and keep finding->adjudication 1:1 (LINT-30 inv1)."""
    h = hashlib.sha1(("%s\x1f%s\x1f%s" % (obj, assertion_id, dimension)).encode()).hexdigest()[:10]
    return "F-S9-PR-%s" % h


def build_finding_row(resolved, item_verdict, lens, run_id, manifest_ref):
    aid = item_verdict["assertion_id"]
    dim = item_verdict["dimension"]
    defect = item_verdict.get("defect") or {}
    inv_row = next((r for r in resolved["inventory_rows"]
                    if r["assertion_id"] == aid), {})
    locator = {
        "section": (inv_row.get("locator") or {}) if inv_row else None,
        "lines": None,
        "verbatim": defect.get("evidence_quote"),
    }
    return {
        "schema": "s9.finding.v1",
        "id": finding_id_for(resolved["object"], aid, dim),
        "run": run_id,
        "object": resolved["object"],
        "object_class": resolved["object_class"],
        "dimension": PANEL_DIM_D.get(dim, "D4"),
        "gate": PANEL_DIM_GATE.get(dim),
        "assertion_id": aid,
        "locator": locator,
        "problem": defect.get("problem") or "panel refutation (%s)" % dim,
        "severity": (defect.get("severity") or "medium").lower(),
        "proposed_fix": defect.get("proposed_fix"),
        "needs_cl": bool(defect.get("needs_cl")),
        "found_by": {"lane": "codex-%s" % lens, "model": CODEX_MODEL,
                     "note": "S9 R1 panel-review lens %s; refute-framed; "
                             "sighted (full lake disclosed)" % lens,
                     "register": "panel-review.jsonl"},
        "panel_dimension": dim,
        "confidence": defect.get("confidence") or 0.7,
    }


# ORCHESTRATOR RULING (2026-07-09, journaled): a vote row's `verdict` refers to
# THE FINDING (per check_ledger inv-2 and the signed F-DEMO-001 instance), while
# the lens's per-assertion verdict refers to THE CORPUS ASSERTION. The two are
# inverses on findings: assertion-refuted == the defect is real == the finding
# STANDS; assertion-stands == the sibling's finding is wrong == the finding is
# REFUTED. stands-modified carries through. Vote rows written before this
# mapping landed carry assertion-semantics and are normalized by the cutover
# script (_run/s9/vote-semantics-cutover.json records the boundary).
_ASSERTION_TO_FINDING_VERDICT = {
    "refuted": "stands",
    "stands": "refuted",
    "stands-modified": "stands-modified",
}


def build_vote_row(finding_id, item_verdict, lens, model, manifest_ref,
                   lane=None):
    lane = lane or "codex-%s" % lens
    verdict = _ASSERTION_TO_FINDING_VERDICT.get(
        item_verdict["verdict"], item_verdict["verdict"])
    row = lr.make_vote_row(
        finding_id, verdict, item_verdict.get("reasons") or [],
        lane=lane, model=model,
        breaks_tp=bool(item_verdict.get("breaks_true_positives")),
        residual=item_verdict.get("residual_risks") or [],
        tightening=item_verdict.get("suggested_tightening"),
        manifest_ref=manifest_ref)
    row["sandbox"] = "read-only (isolated temp; disclosure-set only)"
    row["independent"] = ("isolated %s exec; no sibling votes or in-progress "
                          "adjudications disclosed" % ("codex" if lane.startswith("codex") else "opus"))
    row["panel_dimension"] = item_verdict.get("dimension")
    return row


def build_attestation_row(resolved, lens, model, run_id, manifest_ref,
                          reviewed_ids, defense_votes, wall, tokens, lane=None):
    lane = lane or "codex-%s" % lens
    return {
        "schema": "s9.attestation.v1",
        "id": "A-S9-PR-%s-%s" % (lens, lr._short(resolved["object"])),
        "run": run_id,
        "object": resolved["object"],
        "object_class": resolved["object_class"],
        "group_id": resolved["group_id"],
        "lens": lens,
        "lane": lane,
        "model": model,
        "verdict": "clean",
        "sandbox": "read-only (isolated temp; disclosure-set only)",
        "independent": "isolated review; no sibling votes/adjudications disclosed",
        "reviewed_assertion_ids": reviewed_ids,
        "dimensions_reviewed": sorted({r["dimension"] for r in resolved["inventory_rows"]}),
        "defense_votes_cast": defense_votes,
        "manifest_ref": lr._rel(manifest_ref) if manifest_ref else None,
        "wall_clock_s": wall,
        "tokens": tokens,
        "recorded_before_reconciliation": True,
        "at": lr._now(),
    }


# ==========================================================================
# 6. Emission — findings (deduped by det. id) / votes / clean attestation
# ==========================================================================

def _existing_finding_ids(ledger_dir):
    p = os.path.join(ledger_dir, "findings.jsonl")
    ids = set()
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ids.add(json.loads(line).get("id"))
                except ValueError:
                    continue
    return ids


def _emit_attestation(row, ledger_dir):
    os.makedirs(ledger_dir, exist_ok=True)
    p = os.path.join(ledger_dir, "panel-attestations.jsonl")
    return lr.locked_append(p, json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _persist_result(ledger_dir, lane_id, payload):
    d = os.path.join(ledger_dir, "panel-results")
    os.makedirs(d, exist_ok=True)
    p = os.path.join(d, "%s.json" % lane_id)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2, sort_keys=True)
    return p


def emit_lens_result(resolved, lens, model, run_id, lane_id, obj_json,
                     result, manifest_ref, ledger_dir):
    """Turn a parsed lens reply into ledger rows per the R1 output contract.
    Returns a summary dict. Fail-closed: an unparseable reply -> no rows, a
    no_review result persisted (never a fabricated finding)."""
    lane = "codex-%s" % lens
    reviewed = (obj_json or {}).get("reviewed") or []
    existing = _existing_finding_ids(ledger_dir)
    verdict_map = {}     # assertion_id -> {dimension, verdict, has_defect}
    findings_emitted, votes_emitted, defense_votes = [], [], []
    charter = LENS_CHARTER.get(lens, frozenset(PANEL_DIMS))

    for iv in reviewed:
        aid = iv.get("assertion_id")
        dim = iv.get("dimension")
        verdict = iv.get("verdict")
        if not aid or dim not in PANEL_DIMS or verdict not in \
                ("stands", "refuted", "stands-modified"):
            continue
        has_defect = verdict in ("refuted", "stands-modified")
        verdict_map[aid] = {"dimension": dim, "verdict": verdict,
                            "has_defect": has_defect,
                            "in_charter": dim in charter,
                            "verifiable": iv.get("verifiable_from_disclosed", True)}
        fid = finding_id_for(resolved["object"], aid, dim)

        if has_defect and dim in charter:
            # emit the finding (deduped by deterministic id) + this lens's vote
            if fid not in existing:
                frow = build_finding_row(resolved, iv, lens, run_id, manifest_ref)
                lr.emit_row(frow, ledger_dir)
                existing.add(fid)
                findings_emitted.append(fid)
            vrow = build_vote_row(fid, iv, lens, model, manifest_ref, lane=lane)
            lr.emit_row(vrow, ledger_dir)
            votes_emitted.append({"finding_id": fid, "verdict": verdict})
        elif fid in existing:
            # defense/agreement vote on a finding a sibling already raised
            vrow = build_vote_row(fid, iv, lens, model, manifest_ref, lane=lane)
            lr.emit_row(vrow, ledger_dir)
            votes_emitted.append({"finding_id": fid, "verdict": verdict})
            if not has_defect:
                defense_votes.append({"finding_id": fid, "verdict": verdict})
        # else: no finding exists for this (still-standing) assertion -> the
        # verdict lives only in verdict_map for orchestrator backfill.

    reviewed_ids = [iv.get("assertion_id") for iv in reviewed if iv.get("assertion_id")]
    # A clean attestation may ONLY be emitted when the lane ACTUALLY PARSED and
    # raised no defect. A no_review/lane_error/manifest_refused reply parses to
    # zero findings too, but that is a lane FAILURE, not a clean bill of health —
    # emitting an attestation there would be fail-OPEN (falsely certifying the
    # group). Fail-closed: no attestation unless parse_status is parsed/repaired.
    parsed_ok = result.get("parse_status") in ("parsed", "repaired")
    clean = parsed_ok and (len(findings_emitted) == 0)
    attestation_ref = None
    if clean:
        att = build_attestation_row(resolved, lens, model, run_id, manifest_ref,
                                    reviewed_ids, defense_votes,
                                    result.get("wall_clock_s"), result.get("tokens"))
        attestation_ref = _emit_attestation(att, ledger_dir)

    summary = {
        "lane_id": lane_id, "group_id": resolved["group_id"], "lens": lens,
        "lane": lane, "model": model, "run": run_id,
        "parse_status": result.get("parse_status"),
        "attempts": result.get("attempts"),
        "reviewed_count": len(reviewed_ids),
        "group_total_assertions": resolved["total"],
        "findings_emitted": findings_emitted,
        "votes_emitted": votes_emitted,
        "defense_votes": defense_votes,
        "clean_attestation": clean,
        "verdict_map": verdict_map,
        "manifest_ref": lr._rel(manifest_ref) if manifest_ref else None,
        "wall_clock_s": result.get("wall_clock_s"),
        "tokens": result.get("tokens"),
        "text_disclosed_cases": resolved["text_disclosed_cases"],
        "lake_only_cases": resolved["lake_only_cases"],
        "resolution_notes": resolved["resolution_notes"],
        "at": lr._now(),
    }
    _persist_result(ledger_dir, lane_id, {"summary": summary,
                                          "raw_reply": result.get("last_message"),
                                          "parsed": obj_json,
                                          "attestation_ref": lr._rel(attestation_ref) if attestation_ref else None})
    return summary


# ==========================================================================
# 7. The panel-review lane (one lens x one group)
# ==========================================================================

def _review_with_repair(prompt, sandbox, timeout_s, budget, mock):
    """Run the lens; on unparseable output re-run ONCE (budget permitting), then
    give up (no_review, fail-closed). Mirrors lane_runner._read_with_repair."""
    if mock is not None:
        raw = mock(prompt)
        base = {"last_message": raw, "wall_clock_s": 0.0, "auth_error": False,
                "tokens": {"total": None}, "stderr_tail": "", "timed_out": False,
                "returncode": 0}
        obj = lr.extract_json(raw)
        if obj is not None:
            base.update(parse_status="parsed", attempts=1)
            return base, obj
        raw2 = mock(prompt + "\n\nSTRICT: output ONLY valid JSON, no prose.")
        r2 = dict(base, last_message=raw2, attempts=2)
        obj2 = lr.extract_json(raw2)
        r2["parse_status"] = "repaired" if obj2 is not None else "no_review"
        return r2, obj2

    result = lr.run_codex(prompt, sandbox, timeout_s=timeout_s, budget=budget)
    if result.get("auth_error"):
        result.update(parse_status="auth_error", attempts=1)
        return result, None
    obj = lr.extract_json(result["last_message"])
    if obj is not None:
        result.update(parse_status="parsed", attempts=1)
        return result, obj
    if result.get("timed_out"):
        result.update(parse_status="no_review", attempts=1)
        return result, None
    # re-run ONCE with a strict-JSON nudge — budget permitting (pilot cap 6)
    if budget is not None and budget.used >= budget.cap:
        result.update(parse_status="no_review", attempts=1,
                      note="budget cap reached; repair re-run skipped (fail-closed)")
        return result, None
    strict = prompt + ("\n\nSTRICT: your ENTIRE reply must be ONE valid JSON "
                       "object. No prose, no code fences.")
    r2 = lr.run_codex(strict, sandbox, timeout_s=timeout_s, budget=budget)
    if r2.get("auth_error"):
        r2.update(parse_status="auth_error", attempts=2)
        return r2, None
    obj2 = lr.extract_json(r2["last_message"])
    r2.update(parse_status=("repaired" if obj2 is not None else "no_review"),
              attempts=2)
    return r2, obj2


def _default_worklist():
    """Prefer the ratified v2 worklist (ledger-row dropped, registry sharded,
    reference/craft promoted); fall back to v1 only if v2 was never built."""
    return PANEL_WORKLIST_V2 if os.path.exists(PANEL_WORKLIST_V2) else PANEL_WORKLIST


def run_panel_review(group_id, lens, run_id, budget, ledger_dir=RUN_DIR,
                     timeout_s=lr.DEFAULT_TIMEOUT_S, mock=None,
                     worklist_idx=None, inv_by_id=None, worklist_path=None):
    """One panel-review lens over one group. Emits s9.finding.v1 (defects only) +
    s9.vote.v1 (findings it reviews) + a per-group clean attestation, per R1.
    Returns a summary dict."""
    if worklist_idx is None:
        worklist_idx = load_worklist_index(worklist_path or _default_worklist())
    resolved = resolve_group(group_id, worklist_idx=worklist_idx,
                             inv_by_id=inv_by_id)
    lane_id = "codex-%s-panel-%s-%s" % (lens, run_id, lr._short(group_id))
    task_md = panel_prompt(lens, group_id)

    sandbox, sb_files, evidence = materialize_panel_sandbox(resolved, task_md)
    manifest = lr.build_manifest(
        lane_id, "review", files_disclosed=sb_files,
        fields_excluded=list(lr.REQUIRED_REVIEW_EXCLUSIONS),
        ids=[r["assertion_id"] for r in resolved["inventory_rows"]],
        identity_payload=None, discovery=False, sandbox_dir=sandbox)
    manifest["panel_group"] = group_id
    manifest["panel_lens"] = lens
    manifest["evidence_index"] = evidence
    manifest["text_disclosed_cases"] = resolved["text_disclosed_cases"]
    manifest["lake_only_cases"] = resolved["lake_only_cases"]
    manifest_ref = lr.write_manifest(manifest)

    violations = lr.validate_manifest(manifest, sandbox_files=sb_files)
    if violations:   # FAIL-CLOSED — never launch a leaky manifest
        shutil.rmtree(sandbox, ignore_errors=True)
        summary = {"lane_id": lane_id, "group_id": group_id, "lens": lens,
                   "parse_status": "manifest_refused", "findings_emitted": [],
                   "votes_emitted": [], "clean_attestation": False,
                   "manifest_ref": lr._rel(manifest_ref),
                   "violations": violations, "at": lr._now()}
        _persist_result(ledger_dir, lane_id, {"summary": summary})
        return summary

    result, obj = _review_with_repair(task_md, sandbox, timeout_s, budget, mock)

    if result.get("auth_error"):
        # Classify: a GENUINE credential stop (pause-#8) carries a HARD auth
        # marker AND no model output -> escalate. A transient/ambiguous flag
        # (e.g. codex's "reading additional input from stdin" hiccup, a soft
        # "credential"/"expired" token-refresh line, or any auth-ish noise while
        # OTHER calls on the same credential succeed) is NOT a systemic stop:
        # record a re-dispatchable lane_error (fail-closed, no rows) and PERSIST
        # the stderr for diagnosis instead of crashing the whole group.
        shutil.rmtree(sandbox, ignore_errors=True)
        blob = ((result.get("stderr_tail") or "") + " "
                + (result.get("last_message") or "")).lower()
        genuine = _hard_auth(blob) and not (result.get("last_message") or "").strip()
        summary = {"lane_id": lane_id, "group_id": group_id, "lens": lens,
                   "lane": "codex-%s" % lens, "model": CODEX_MODEL,
                   "parse_status": "lane_error", "auth_flagged": True,
                   "genuine_auth_stop": bool(genuine),
                   "findings_emitted": [], "votes_emitted": [],
                   "clean_attestation": False, "reviewed_count": 0,
                   "group_total_assertions": resolved["total"],
                   "manifest_ref": lr._rel(manifest_ref),
                   "stderr_tail": result.get("stderr_tail"),
                   "note": "auth-flagged codex failure; %s" %
                           ("GENUINE hard-marker stop (pause-#8)" if genuine
                            else "transient/ambiguous -> re-dispatchable lane_error"),
                   "at": lr._now()}
        _persist_result(ledger_dir, lane_id, {"summary": summary,
                                              "raw_reply": result.get("last_message")})
        if genuine:
            raise lr.AuthError(result.get("stderr_tail") or result.get("last_message"))
        return summary   # transient: fail-closed, orchestrator re-dispatches

    summary = emit_lens_result(resolved, lens, CODEX_MODEL, run_id, lane_id,
                               obj, result, manifest_ref, ledger_dir)
    shutil.rmtree(sandbox, ignore_errors=True)
    return summary


# ==========================================================================
# 8. Opus prompt-pack generator (the Claude panel leg — dispatched separately)
# ==========================================================================

def _read_text_capped(path, cap):
    with open(path, encoding="utf-8", errors="replace") as f:
        t = f.read()
    if cap and len(t) > cap:
        return t[:cap] + ("\n\n[...TRUNCATED %d of %d chars for pack size; the "
                          "Codex lane saw the full text — flag any check that "
                          "needs the tail...]" % (len(t) - cap, len(t))), True
    return t, False


OPUS_PACK_FRAMING = (
    "# S9 R1 panel-review — Opus model-diversity lane (prompt pack)\n\n"
    "You are the **Claude/Opus** leg of the S9 three-lane adversarial panel "
    "(1 Claude + 2 Codex, R1). The two Codex lanes carry the A (support/quote-"
    "fidelity) and B (currency/treatment) attack lenses; **you carry model "
    "diversity and MUST vote on every paneled assertion across BOTH lenses' "
    "concerns.** You are refute-framed: try hard to break each assertion; "
    "**default to REFUTED on uncertainty**; never fabricate a cite, quote, or "
    "holding; use ONLY the evidence inlined below (no search, no outside "
    "knowledge). You are a SIGHTED reviewer — the FULL lake record (judgment "
    "fields included) is inlined.\n\n"
    "You are a WRITER lane, not an adjudicator: you FIND and VOTE. You do not "
    "tally, adjudicate, or close any row — the orchestrator does.\n\n"
    "For EACH group below, return one JSON object with the exact `reviewed[]` "
    "shape from the output contract (identical framing to the Codex lenses). "
    "Emit a finding object ONLY for a real defect (verdict refuted / "
    "stands-modified); a group you find wholly clean returns all-`stands` "
    "verdicts (the harness records a clean attestation). Concatenate the "
    "per-group JSON objects into a top-level `{\"packs\": [ ... ]}` array, one "
    "entry per group, each carrying its `group_id`.\n\n"
)


def generate_opus_pack(group_ids, batch_id, out_dir=None, text_cap=120000,
                       worklist_idx=None, inv_by_id=None):
    """Write the exact review-form prompt-pack for N groups so an o2-opus-xhigh
    Agent lane runs them with identical framing. Emits:
      <out_dir>/<batch_id>.md            — the exact prompt (framing + inlined
                                           disclosure set + output contract)
      <out_dir>/<batch_id>.manifest.json — audit manifests (one review-manifest
                                           per group; model claude-opus-4-8) +
                                           the emission metadata the orchestrator
                                           needs to route rows through the same
                                           contract.
    Returns {md_path, manifest_path, groups, total_assertions}."""
    out_dir = out_dir or os.path.join(RUN_DIR, "opus-packs")
    os.makedirs(out_dir, exist_ok=True)
    worklist_idx = worklist_idx or load_worklist_index(_default_worklist())
    inv_by_id = inv_by_id if inv_by_id is not None else load_inventory_index()

    md = [OPUS_PACK_FRAMING, _PANEL_OUTPUT_CONTRACT, "\n---\n"]
    manifests = []
    total_assertions = 0

    for gid in group_ids:
        resolved = resolve_group(gid, worklist_idx=worklist_idx,
                                 inv_by_id=inv_by_id)
        total_assertions += resolved["total"]
        lane_id = "opus-panel-%s-%s" % (batch_id, lr._short(gid))

        # audit manifest — same lane_kind/exclusions as a Codex review lane, but
        # model = opus and disclosure is INLINED (no sandbox; prompt-isolation).
        disclosed = (["content_page"]
                     + ["lake/%s" % c for c in sorted(resolved["lake_records"])]
                     + ["text/%s" % c for c in sorted(resolved["cached_texts"])]
                     + ["group_inventory"])
        man = lr.build_manifest(
            lane_id, "review", files_disclosed=disclosed,
            fields_excluded=list(lr.REQUIRED_REVIEW_EXCLUSIONS),
            ids=[r["assertion_id"] for r in resolved["inventory_rows"]],
            identity_payload=None, discovery=False, sandbox_dir="INLINED-IN-PACK")
        man["model"] = OPUS_MODEL
        man["panel_group"] = gid
        man["panel_lens"] = "opus-both"
        man["text_disclosed_cases"] = resolved["text_disclosed_cases"]
        man["lake_only_cases"] = resolved["lake_only_cases"]
        # fail-closed: the inlined disclosure must pass the same blindness guard
        viol = lr.validate_manifest(man, sandbox_files=disclosed)
        man["blindness_violations"] = viol
        manifests.append({"lane_id": lane_id, "group_id": gid,
                          "manifest": man, "total": resolved["total"],
                          "resolution_notes": resolved["resolution_notes"]})

        md.append("\n## GROUP: %s  (`%s`, %d assertions)\n"
                  % (gid, resolved["object_class"], resolved["total"]))
        if viol:
            md.append("\n> WARNING blindness-guard violations (do not review): %s\n"
                      % "; ".join(viol))
        md.append("\n### content_page\n\n```\n%s\n```\n"
                  % (_read_text_capped(resolved["content_page"], text_cap)[0]
                     if resolved["content_page"] else "[content page unresolved]"))
        md.append("\n### group_inventory (assertions under review)\n\n```jsonl\n"
                  + "\n".join(json.dumps(r, ensure_ascii=False)
                              for r in resolved["inventory_rows"]) + "\n```\n")
        for cn, lp in sorted(resolved["lake_records"].items()):
            body, trunc = _read_text_capped(lp, text_cap)
            md.append("\n### lake record — %s%s\n\n```json\n%s\n```\n"
                      % (cn, " (truncated)" if trunc else "", body))
        for cn, tp in sorted(resolved["cached_texts"].items()):
            body, trunc = _read_text_capped(tp, text_cap)
            md.append("\n### cached opinion text — %s%s\n\n```\n%s\n```\n"
                      % (cn, " (truncated)" if trunc else "", body))
        md.append("\n---\n")

    md_path = os.path.join(out_dir, "%s.md" % batch_id)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("".join(md))
    man_path = os.path.join(out_dir, "%s.manifest.json" % batch_id)
    with open(man_path, "w", encoding="utf-8") as f:
        json.dump({"schema": "s9.opus-pack.v1", "batch_id": batch_id,
                   "model": OPUS_MODEL, "lane_kind": "review",
                   "generated": lr._now(), "group_count": len(group_ids),
                   "total_assertions": total_assertions,
                   "finding_id_rule": "F-S9-PR-sha1(object|assertion_id|dimension)[:10]",
                   "emission_contract": "s9.finding.v1 (defects only) + "
                   "s9.vote.v1 (lane=opus-panel, model=claude-opus-4-8) + "
                   "s9.attestation.v1 for wholly-clean groups",
                   "groups": manifests}, f, ensure_ascii=False, indent=2)
    return {"md_path": md_path, "manifest_path": man_path,
            "groups": len(group_ids), "total_assertions": total_assertions}


# ==========================================================================
# 9. Self-test (MOCK lane — no live codex) + fixtures
# ==========================================================================

def _build_panel_fixtures():
    """Write a tiny self-contained panel fixture (worklist row + inventory +
    content page + lake record + cached text) under a temp root. Returns a dict
    of paths + the fixture group id."""
    root = tempfile.mkdtemp(prefix="s9-panel-fx-")
    text_dir = os.path.join(root, "text")
    lake_dir = os.path.join(root, "lake")
    content_dir = os.path.join(root, "content", "cases")
    for d in (text_dir, lake_dir, content_dir):
        os.makedirs(d, exist_ok=True)

    case = "Fixture v. Sample"
    lead = 9999001
    with open(os.path.join(text_dir, "%s.txt" % lead), "w", encoding="utf-8") as f:
        f.write("Justice Test delivered the opinion of the Court.\n"
                "We hold that a fixture search requires a warrant absent exigency.\n"
                "The judgment is affirmed.\n")
    lake_rec = {
        "record_id": case,
        "identity": {"case_name": case, "citation": "1 U.S. 1",
                     "court": "U.S. Supreme Court", "year": 2001,
                     "date_decided": "2001-01-01", "lead_opinion_id": lead,
                     "cluster_id": 5001},
        "citations": [{"cite": "1 U.S. 1"}],
        "pinpoints": [{"id": "pin-1", "quote": "a fixture search requires a warrant absent exigency"}],
        "treatment": {"field_i_validity": "good_law", "as_of_treatment": "2026-06-30",
                      "as_of_content": "2001-01-01", "scope_note": "Good law."},
    }
    with open(os.path.join(lake_dir, "%s.json" % case), "w", encoding="utf-8") as f:
        json.dump(lake_rec, f)
    content_obj = "content/cases/%s.md" % case
    with open(os.path.join(root, content_obj), "w", encoding="utf-8") as f:
        f.write("# %s\n\nHeld: a fixture search requires a warrant absent exigency.\n" % case)

    # inventory rows: one per dimension we exercise
    inv_items = [
        {"assertion_id": "fx_exist", "kind": "case_cite",
         "locator": {"field": "citation", "case": case},
         "object": content_obj, "object_class": "case",
         "payload": {"citation": "1 U.S. 1", "title": case, "year": "2001"}},
        {"assertion_id": "fx_support", "kind": "proposition",
         "locator": {"field": "holding", "case": case},
         "object": content_obj, "object_class": "case",
         "payload": {"holding": "a fixture search requires a warrant absent exigency",
                     "title": case}},
        {"assertion_id": "fx_quote", "kind": "quote_pinpoint",
         "locator": {"pin_id": "pin-1", "case": case},
         "object": content_obj, "object_class": "case",
         "payload": {"quote": "a fixture search requires a warrant absent exigency",
                     "title": case}},
        {"assertion_id": "fx_treat", "kind": "treatment",
         "locator": {"field": "treatment", "case": case},
         "object": content_obj, "object_class": "case",
         "payload": {"field_i_validity": "good_law", "title": case}},
    ]
    inv = {"schema": "s9.inventory.v1", "items": inv_items}
    inv_path = os.path.join(root, "assertion-inventory.json")
    with open(inv_path, "w", encoding="utf-8") as f:
        json.dump(inv, f)

    wl_row = {
        "schema": "s9.worklist.panel.v1", "object": content_obj,
        "object_class": "case", "page_batch": 0, "page_ordinal": 0,
        "dimensions": {"existence": ["fx_exist"], "support": ["fx_support"],
                       "quote_fidelity": ["fx_quote"], "pincite": [],
                       "treatment": ["fx_treat"], "black_letter": []},
        "counts": {"existence": 1, "support": 1, "quote_fidelity": 1,
                   "pincite": 0, "treatment": 1, "black_letter": 0},
        "total": 4, "black_letter_needs_2_approvals": False,
    }
    wl_path = os.path.join(root, "panel-review.jsonl")
    with open(wl_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(wl_row) + "\n")

    return {"root": root, "text_dir": text_dir, "content_obj": content_obj,
            "inv_path": inv_path, "wl_path": wl_path, "lake_dir": lake_dir}


def _mock_reconciling_panel_ledger(d):
    """A complete, internally-consistent panel-shaped ledger (finding from a
    panel lens + 3 votes with >=2 refute + a MODIFIED adjudication + a fix whose
    final loop is FIXED) — proves the panel row shapes reconcile green under
    LINT-30."""
    fid = finding_id_for("content/cases/Fixture v. Sample.md", "fx_quote", "quote_fidelity")
    finding = {"schema": "s9.finding.v1", "id": fid, "run": "selftest-panel",
               "object": "content/cases/Fixture v. Sample.md", "object_class": "case",
               "dimension": "D3", "gate": "G3", "assertion_id": "fx_quote",
               "locator": {"section": "quote", "lines": None, "verbatim": "mismatch"},
               "problem": "quote drift vs cached text", "severity": "high",
               "proposed_fix": "restore verbatim", "needs_cl": False,
               "found_by": {"lane": "codex-A", "model": "gpt-5.5"},
               "confidence": 0.8}
    votes = [
        build_vote_row(fid, {"assertion_id": "fx_quote", "dimension": "quote_fidelity",
                             "verdict": "refuted", "reasons": ["drift"],
                             "breaks_true_positives": False}, "A", "gpt-5.5", None),
        build_vote_row(fid, {"assertion_id": "fx_quote", "dimension": "quote_fidelity",
                             "verdict": "refuted", "reasons": ["drift confirmed"],
                             "breaks_true_positives": False}, "B", "gpt-5.5", None),
        build_vote_row(fid, {"assertion_id": "fx_quote", "dimension": "quote_fidelity",
                             "verdict": "stands-modified", "reasons": ["minor"],
                             "breaks_true_positives": False}, None, OPUS_MODEL, None,
                       lane="opus-panel"),
    ]
    adj = {"schema": "s9.adjudication.v1", "finding_id": fid,
           "refute_tally": {"codex-A": "refuted", "codex-B": "refuted",
                            "opus-panel": "stands-modified",
                            "rule": ">=2-of-3 refute kills", "result": "KILLED"},
           "verdict": "MODIFIED", "adjudicated_holding": ["restore the verbatim quote"],
           "evidence": [{"kind": "lake", "ref": "pin-1"}],
           "adjudicator": {"lane": "o2-fable-orchestrator", "model": "claude-fable-5"},
           "role_separation": "finder codex-A != adjudicator o2-fable-orchestrator",
           "spawned_findings": [], "at": lr._now()}
    fix = {"schema": "s9.fix.v1", "finding_id": fid, "adjudication_verdict": "MODIFIED",
           "applied_by": {"lane": "o2-opus-xhigh", "model": OPUS_MODEL},
           "artifacts": ["fixture"], "content_edits": "restored quote",
           "loops": [{"loop": 1, "re_review": {"lane": "codex-C", "model": "gpt-5.5",
                                               "round": 1, "verdict": "FIXED"}}],
           "loop_cap": 3, "writer_neq_checker": "author o2-opus-xhigh != reviewer codex-C",
           "at": lr._now()}
    with open(os.path.join(d, "findings.jsonl"), "w") as f:
        f.write(json.dumps(finding) + "\n")
    with open(os.path.join(d, "votes.jsonl"), "w") as f:
        for v in votes:
            f.write(json.dumps(v) + "\n")
    with open(os.path.join(d, "adjudications.jsonl"), "w") as f:
        f.write(json.dumps(adj) + "\n")
    with open(os.path.join(d, "fixes.jsonl"), "w") as f:
        f.write(json.dumps(fix) + "\n")


def self_test_panel():
    errs = []
    fx = _build_panel_fixtures()
    wl_idx = load_worklist_index(fx["wl_path"])
    inv_idx = load_inventory_index(fx["inv_path"])
    gid = fx["content_obj"]
    # keep the self-test's manifests OUT of the production manifest dir
    _orig_manifest_dir = lr.MANIFEST_DIR
    _tmp_manifest_dir = tempfile.mkdtemp(prefix="s9-panel-manifests-")
    lr.MANIFEST_DIR = _tmp_manifest_dir

    # -- (a) group resolution -------------------------------------------
    # point lake + text resolution at the fixture dirs
    _orig_lake, _orig_text = LAKE_CASES_DIR, POOL_TEXT_DIR
    globals()["LAKE_CASES_DIR"] = fx["lake_dir"]
    globals()["POOL_TEXT_DIR"] = fx["text_dir"]
    try:
        resolved = resolve_group(gid, worklist_idx=wl_idx, inv_by_id=inv_idx)
    finally:
        globals()["LAKE_CASES_DIR"] = _orig_lake
        globals()["POOL_TEXT_DIR"] = _orig_text
    if resolved["total"] != 4:
        errs.append("(a) group total %s != 4" % resolved["total"])
    if "Fixture v. Sample" not in resolved["lake_records"]:
        errs.append("(a) lake record not resolved: %s" % list(resolved["lake_records"]))
    if "Fixture v. Sample" not in resolved["cached_texts"]:
        errs.append("(a) text-dependent case text not disclosed (support/quote present)")

    # -- (b) review-manifest validity + fail-closed leak refusal ---------
    good = lr.build_manifest("t-review", "review",
                             files_disclosed=["content_page.md", "lake/x.json",
                                              "group_inventory.jsonl", "task.md"],
                             fields_excluded=list(lr.REQUIRED_REVIEW_EXCLUSIONS),
                             ids=["fx_exist"])
    if lr.validate_manifest(good):
        errs.append("(b) clean review manifest wrongly flagged: %s" % lr.validate_manifest(good))
    leak = lr.build_manifest("t-review-leak", "review",
                             files_disclosed=["content_page.md", "votes.jsonl"],
                             fields_excluded=list(lr.REQUIRED_REVIEW_EXCLUSIONS),
                             ids=["fx_exist"])
    if not any("sibling vote" in x for x in lr.validate_manifest(leak)):
        errs.append("(b) sibling-vote leak NOT detected in review manifest")
    miss = lr.build_manifest("t-review-excl", "review",
                             files_disclosed=["content_page.md"],
                             fields_excluded=["sibling_votes"], ids=["fx_exist"])
    if not any("omits required exclusion" in x for x in lr.validate_manifest(miss)):
        errs.append("(b) missing required review exclusion NOT detected")

    # -- (c) mock lens: defect -> finding+vote; dedup; clean -> attestation
    globals()["LAKE_CASES_DIR"] = fx["lake_dir"]
    ledger = tempfile.mkdtemp(prefix="s9-panel-ledger-")

    def mock_lensA(_p):
        return json.dumps({"lens": "A", "group_id": gid, "reviewed": [
            {"assertion_id": "fx_exist", "dimension": "existence", "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["cite matches lake"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None},
            {"assertion_id": "fx_support", "dimension": "support", "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["holding matches"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None},
            {"assertion_id": "fx_quote", "dimension": "quote_fidelity", "verdict": "refuted",
             "verifiable_from_disclosed": True,
             "defect": {"problem": "quote drift", "severity": "high",
                        "proposed_fix": "restore", "evidence_quote": "requires a warrant",
                        "needs_cl": False, "locator_note": "pin-1"},
             "reasons": ["drift vs text"], "breaks_true_positives": False,
             "residual_risks": [], "suggested_tightening": None},
            {"assertion_id": "fx_treat", "dimension": "treatment", "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["lens A defers"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None},
        ], "notes": ""})

    def mock_lensB(_p):
        # agrees on the quote defect (defense/agreement vote) + all-else stands
        return json.dumps({"lens": "B", "group_id": gid, "reviewed": [
            {"assertion_id": "fx_exist", "dimension": "existence", "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["still good law"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None},
            {"assertion_id": "fx_quote", "dimension": "quote_fidelity", "verdict": "refuted",
             "verifiable_from_disclosed": True, "defect": None,
             "reasons": ["agree drift"], "breaks_true_positives": False,
             "residual_risks": [], "suggested_tightening": None},
            {"assertion_id": "fx_treat", "dimension": "treatment", "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["good law confirmed"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None},
        ], "notes": ""})

    try:
        sumA = run_panel_review(gid, "A", "selftest", lr.InvocationBudget(cap=99),
                                ledger_dir=ledger, mock=mock_lensA,
                                worklist_idx=wl_idx, inv_by_id=inv_idx)
        sumB = run_panel_review(gid, "B", "selftest", lr.InvocationBudget(cap=99),
                                ledger_dir=ledger, mock=mock_lensB,
                                worklist_idx=wl_idx, inv_by_id=inv_idx)
    finally:
        globals()["LAKE_CASES_DIR"] = _orig_lake
        globals()["POOL_TEXT_DIR"] = _orig_text

    if len(sumA["findings_emitted"]) != 1:
        errs.append("(c) lens A did not emit exactly 1 finding: %s" % sumA["findings_emitted"])
    if sumA["clean_attestation"]:
        errs.append("(c) lens A wrongly emitted a clean attestation despite a defect")
    # lens B agrees on the same quote defect: NO new finding (dedup), but a vote
    if len(sumB["findings_emitted"]) != 0:
        errs.append("(c) lens B raised a duplicate finding (dedup failed): %s" % sumB["findings_emitted"])
    if not any(v["verdict"] == "refuted" for v in sumB["votes_emitted"]):
        errs.append("(c) lens B did not cast an agreement vote on the shared finding")
    # exactly one finding row, two votes on it
    fcount = sum(1 for _ in open(os.path.join(ledger, "findings.jsonl")))
    vcount = sum(1 for _ in open(os.path.join(ledger, "votes.jsonl")))
    if fcount != 1:
        errs.append("(c) ledger has %d finding rows (want 1 after dedup)" % fcount)
    if vcount != 2:
        errs.append("(c) ledger has %d vote rows (want 2: A refute + B refute)" % vcount)

    # clean-group attestation: a lens that finds NO defect
    def mock_clean(_p):
        return json.dumps({"lens": "A", "group_id": gid, "reviewed": [
            {"assertion_id": a, "dimension": d, "verdict": "stands",
             "verifiable_from_disclosed": True, "defect": None, "reasons": ["ok"],
             "breaks_true_positives": False, "residual_risks": [], "suggested_tightening": None}
            for a, d in [("fx_exist", "existence"), ("fx_support", "support"),
                         ("fx_quote", "quote_fidelity"), ("fx_treat", "treatment")]
        ], "notes": ""})

    ledger2 = tempfile.mkdtemp(prefix="s9-panel-clean-")
    globals()["LAKE_CASES_DIR"] = fx["lake_dir"]
    globals()["POOL_TEXT_DIR"] = fx["text_dir"]
    try:
        sumc = run_panel_review(gid, "A", "clean", lr.InvocationBudget(cap=99),
                                ledger_dir=ledger2, mock=mock_clean,
                                worklist_idx=wl_idx, inv_by_id=inv_idx)
    finally:
        globals()["LAKE_CASES_DIR"] = _orig_lake
        globals()["POOL_TEXT_DIR"] = _orig_text
    if not sumc["clean_attestation"]:
        errs.append("(c) clean review did not emit a clean attestation")
    if not os.path.exists(os.path.join(ledger2, "panel-attestations.jsonl")):
        errs.append("(c) panel-attestations.jsonl not written for clean review")
    if os.path.exists(os.path.join(ledger2, "findings.jsonl")):
        errs.append("(c) clean review wrongly wrote a finding row")

    # -- (d) prose-wrap repair + unparseable-twice -> no_review ----------
    calls = {"n": 0}

    def mock_prose(_p):
        calls["n"] += 1
        return ("Sure, here is my review:\n```json\n" + mock_clean(_p) + "\n```\nThanks!")
    ledger3 = tempfile.mkdtemp(prefix="s9-panel-prose-")
    globals()["LAKE_CASES_DIR"] = fx["lake_dir"]
    globals()["POOL_TEXT_DIR"] = fx["text_dir"]
    try:
        sumd = run_panel_review(gid, "A", "prose", lr.InvocationBudget(cap=99),
                                ledger_dir=ledger3, mock=mock_prose,
                                worklist_idx=wl_idx, inv_by_id=inv_idx)
    finally:
        globals()["LAKE_CASES_DIR"] = _orig_lake
        globals()["POOL_TEXT_DIR"] = _orig_text
    if sumd["parse_status"] != "parsed":
        errs.append("(d) fenced prose-wrapped reply not parsed (got %s)" % sumd["parse_status"])

    def mock_garbage(_p):
        return "I cannot output JSON."
    ledger4 = tempfile.mkdtemp(prefix="s9-panel-garbage-")
    globals()["LAKE_CASES_DIR"] = fx["lake_dir"]
    globals()["POOL_TEXT_DIR"] = fx["text_dir"]
    try:
        sume = run_panel_review(gid, "A", "garbage", lr.InvocationBudget(cap=99),
                                ledger_dir=ledger4, mock=mock_garbage,
                                worklist_idx=wl_idx, inv_by_id=inv_idx)
    finally:
        globals()["LAKE_CASES_DIR"] = _orig_lake
        globals()["POOL_TEXT_DIR"] = _orig_text
    if sume["parse_status"] != "no_review":
        errs.append("(d) unparseable-twice did not fall to no_review (got %s)" % sume["parse_status"])
    if sume["findings_emitted"]:
        errs.append("(d) no_review wrongly fabricated a finding")

    # -- (e) complete mock panel ledger reconciles green under LINT-30 ---
    demo = tempfile.mkdtemp(prefix="s9-panel-l30-")
    _mock_reconciling_panel_ledger(demo)
    viols, status = check_ledger.check_ledger(demo)
    nh = sum(1 for x in viols if x["severity"] == check_ledger.c.HIGH)
    if status != "CHECKED" or nh != 0:
        errs.append("(e) mock panel ledger not LINT-30 green: status=%s HIGH=%d %s"
                    % (status, nh, [x["message"][:60] for x in viols][:4]))

    lr.MANIFEST_DIR = _orig_manifest_dir   # restore production manifest dir
    for x in (ledger, ledger2, ledger3, ledger4, demo, fx["root"],
              _tmp_manifest_dir):
        shutil.rmtree(x, ignore_errors=True)

    for e in errs:
        sys.stderr.write("[self-test-panel] FAIL: %s\n" % e)
    sys.stderr.write("[self-test-panel] panel_review %s (%d breaches)\n"
                     % ("PASS" if not errs else "FAIL", len(errs)))
    return 0 if not errs else 1


# ==========================================================================
# 10. CLI
# ==========================================================================

def main(argv=None):
    ap = argparse.ArgumentParser(description="S9 R1 panel-review machinery")
    ap.add_argument("--panel-review", metavar="GROUP_ID",
                    help="run ONE Codex lens over one review group (object path)")
    ap.add_argument("--lens", choices=["A", "B"], default="A")
    ap.add_argument("--panel-review-opus", metavar="GROUP_IDS",
                    help="generate an Opus prompt-pack for comma-separated group ids")
    ap.add_argument("--batch-id", default="opus-batch-1")
    ap.add_argument("--out-dir", default=None)
    ap.add_argument("--run-id", default="p1-panel")
    ap.add_argument("--ledger-dir", default=RUN_DIR)
    ap.add_argument("--timeout", type=int, default=lr.DEFAULT_TIMEOUT_S)
    ap.add_argument("--cap", type=int, default=lr.INVOCATION_CAP)
    ap.add_argument("--self-test-panel", action="store_true")
    args = ap.parse_args(argv)

    if args.self_test_panel:
        return self_test_panel()

    if args.panel_review_opus:
        gids = [g.strip() for g in args.panel_review_opus.split(",") if g.strip()]
        out = generate_opus_pack(gids, args.batch_id, out_dir=args.out_dir)
        sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
        return 0

    if args.panel_review:
        try:
            summary = run_panel_review(
                args.panel_review, args.lens, args.run_id,
                lr.InvocationBudget(cap=args.cap), ledger_dir=args.ledger_dir,
                timeout_s=args.timeout)
        except lr.AuthError as e:
            sys.stderr.write("AUTH-CLASS CODEX FAILURE (pause-#8 surface):\n%s\n" % e)
            return 3
        sys.stdout.write(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
