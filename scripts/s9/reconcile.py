#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S9 P2 reconciliation engine  --  spec S9 R5 (exhaustive blind re-derivation + concordance;
no-regression floor: "every Thread-P item absent from N is dispositioned, never silently lost").

Reads (read-only; zero CourtListener):
  _run/s9/thread-P.json            frozen P0 corpus conclusions (724 items: 609 case + 115 doctrine)
  _run/s9/thread-N-reads.jsonl     blind case reads, 2 lenses/case (A=support-cited, B=treatment-cited)
  _run/s9/thread-N-doctrine.jsonl  79 doctrine derivations + 36 skip-dispositions
  _run/s6-coverage-ledger.json     coverage-inbox + brief-mention ledger (pre-classify known gaps)

Writes:
  _run/s9/reconciliation.jsonl     one row per P item {p_id, class, evidence_refs, discordance_detail?, ...}
  _run/s9/P2-DISCORDANCE-QUEUE.md   orchestrator adjudication queue grouped by discordance kind
  _run/s9/reconciliation-summary.json  machine summary counts

The SCRIPT classifies MECHANICALLY (semantic comparison is agent work). It never buries a conflict:
it fails toward DISCORDANT-candidate on uncertainty and surfaces every candidate for the orchestrator.

Lane: s9-p2-reconcile   Model: claude-opus-4-8   (COMMIT NOTHING; deterministic; self-test w/ fixtures)
"""
import argparse
import json
import re
import sys
from collections import defaultdict, Counter, OrderedDict

# --------------------------------------------------------------------------- #
# Thresholds (calibrated on the frozen corpus: both-lens overlap-coef p10=0.294,
# median=0.545 -> a 0.30 strong floor keeps ~90% of clean-read cases STRONG-eligible).
# --------------------------------------------------------------------------- #
STRONG_OVERLAP_COEF = 0.30
READABLE_PARSE = ("parsed", "repaired")

# Roles under a doctrine where P homing a case that N does NOT derive is an EXPECTED
# N-blindness artifact (foil/history/cross-ref/related/limiting), not an over-inclusion defect.
EXPECTED_OI_ROLE = re.compile(
    r"foil|histor|related|cross[- ]?doctrine|cross[- ]?ref|illustrat|limiting|origin|umbrella|overlap",
    re.I,
)
# Coverage-ledger terminals that mean "deliberately not a standalone page" -> a KNOWN gap.
LEDGER_KNOWN_TERMINALS = frozenset(
    {"brief-mention", "excluded-remit", "folded-alias", "removed", "unverifiable", "watch"}
)
# Conservative self-referential negative-treatment probe (advisory only; see TREATMENT note below).
TREATMENT_SELFNEG = re.compile(
    r"\bthis (?:decision|opinion|case|holding|ruling|precedent)\b[^.]{0,80}"
    r"(?:overrul|abrogat|no longer good|superseded|not good law)"
    r"|\bhas (?:since )?been (?:overrul|abrogat|supersed)"
    r"|\bno longer good law\b|\blater overrul",
    re.I,
)

STOPWORDS = frozenset("""
a an the of to in on for and or by with without under is are was were be been being that this these
those it its as at from into upon which who whom whose not no nor but if then than so such shall may
can will would could should must does did done has have had their his her our your my we they them he
she you i also where when while within between per each any all more most other some only over after
before about against upon than not held holds holding court case rule where whether because did does
""".split())

# --------------------------------------------------------------------------- #
# Text utilities
# --------------------------------------------------------------------------- #
def norm_tokens(s):
    if not s:
        return frozenset()
    return frozenset(t for t in re.findall(r"[a-z0-9]+", s.lower()) if len(t) >= 3 and t not in STOPWORDS)


def overlap_coef(a, b):
    """Overlap coefficient |A n B| / min(|A|,|B|)  (robust to length asymmetry between P & N prose)."""
    if not a or not b:
        return 0.0
    return len(a & b) / min(len(a), len(b))


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


# Curated legal-caption abbreviation expansions (consistent both sides -> equality is meaningful).
ORG_ABBREV = {
    "dist": "district", "distr": "district", "sch": "school", "co": "company",
    "corp": "corporation", "dept": "department", "depart": "department", "assn": "association",
    "ass": "association", "univ": "university", "natl": "national", "intl": "international",
    "comm": "commission", "commn": "commission", "bd": "board", "mfg": "manufacturing",
    "svcs": "services", "svc": "service", "servs": "services", "auth": "authority",
    "twp": "township", "cnty": "county",
}
# Org/procedural tokens dropped when forming a party-token signature (distinctive names remain).
ORG_STOP = frozenset("""
district school county city board department company corporation association commission university
national international unified town village state states united commonwealth people municipal court
authority township services service authority the of v et al inc ltd llc lp lp co corp no
""".split())


def norm_caption(s):
    """Normalize a case caption for identity matching (cluster_id is preferred; this is a fallback)."""
    if not s:
        return ""
    s = s.lower()
    s = re.sub(r"\.md$", "", s)
    s = re.sub(r"^cases/", "", s)
    s = re.sub(r"#\s*\d+", " ", s)          # drop "#1" style panel/division markers
    s = re.sub(r"[^a-z0-9]+", " ", s)
    toks = [ORG_ABBREV.get(t, t) for t in s.split() if t]
    toks = ["v" if t == "v" else t for t in toks]
    return re.sub(r"\s+", " ", " ".join(toks)).strip()


def caption_signature(s):
    """Frozenset of distinctive party tokens (drops org/procedural words + pure digits + 1-char)."""
    nc = norm_caption(s)
    return frozenset(t for t in nc.split()
                     if t not in ORG_STOP and not t.isdigit() and len(t) >= 2)


def disp_direction(s):
    """Coarse outcome direction from a disposition string (for cross-lens holding-direction check)."""
    if not s:
        return None
    s = s.lower()
    aff = "affirm" in s
    rev = ("revers" in s) or ("vacat" in s)
    if aff and rev:
        return "MIXED"
    if aff:
        return "AFFIRM"
    if rev:
        return "REVERSE"
    if "dismiss" in s:
        return "DISMISS"
    if "grant" in s or "certiorari" in s:
        return "CERT"
    if "remand" in s:
        return "REMAND"
    return "OTHER"


def is_readable(read):
    if not read:
        return False
    if (read.get("parse") or {}).get("status") not in READABLE_PARSE:
        return False
    return bool((read.get("conclusions") or {}).get("holding"))


# --------------------------------------------------------------------------- #
# Loaders
# --------------------------------------------------------------------------- #
def load_thread_p(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_coverage(path):
    """Return caption/cluster indexes of the coverage-inbox + brief-mention ledger."""
    idx = {"by_cluster": {}, "by_caption": {}}
    try:
        with open(path, encoding="utf-8") as fh:
            led = json.load(fh)
    except FileNotFoundError:
        return idx
    for row in (led.get("rows") or []) + (led.get("corpus_mention_baseline") or []):
        term = row.get("terminal")
        cid = row.get("cluster_id")
        if cid is not None:
            idx["by_cluster"].setdefault(cid, term)
        for cap in (row.get("caption"), row.get("canonical")):
            nc = norm_caption(cap)
            if nc:
                idx["by_caption"].setdefault(nc, term)
    return idx


# --------------------------------------------------------------------------- #
# Case reconciliation (judgment grain)
# --------------------------------------------------------------------------- #
def classify_case(p_item, lensrows):
    """
    lensrows: {'A': read|None, 'B': read|None}.  Returns dict with class / discordance kinds / detail /
    evidence.  Mechanical rules only.  Fails toward DISCORDANT-candidate.
    """
    p_hold_tokens = norm_tokens(p_item.get("holding"))
    p_hold_present = bool(p_item.get("holding_present"))

    # A row is PARSED if the lane returned structured content (identity assertion is made even when
    # no holding was extractable); READABLE (for holding concordance) additionally requires a holding.
    parsed = {l: r for l, r in lensrows.items()
              if r and (r.get("parse") or {}).get("status") in READABLE_PARSE}
    readable = {l: r for l, r in parsed.items()
                if (r.get("conclusions") or {}).get("holding")}
    evidence = [f"P:{p_item.get('path')}"]
    for l in ("A", "B"):
        r = lensrows.get(l)
        if r:
            evidence.append(
                f"N-{l}:{r.get('id')}::{(r.get('parse') or {}).get('status')}"
                + (f"::{r.get('cached_text_path')}" if r.get("cached_text_path") else "")
            )

    kinds = []
    detail = {"p_holding": p_item.get("holding"), "lenses": {}}

    # --- (a) identity assertion: either lens flagging mismatch = flag (over ALL parsed rows, so a
    #     present=False "case not found in cached text" signal is never masked by an empty holding
    #     or by a readable sibling lens -- it is the strongest mis-cache signal) ------------------
    id_absent = False
    id_caption = False
    for l, r in sorted(parsed.items()):
        idn = (r.get("conclusions") or {}).get("identity") or {}
        detail["lenses"][l] = {
            "match": idn.get("match"),
            "present": idn.get("present"),
            "has_holding": bool((r.get("conclusions") or {}).get("holding")),
            "parties_in_text": (idn.get("parties_in_text") or "")[:160],
            "disposition": (r.get("conclusions") or {}).get("disposition"),
            "holding": (r.get("conclusions") or {}).get("holding"),
        }
        if idn.get("present") is False:
            id_absent = True
        elif idn.get("match") is False:
            id_caption = True
    if id_absent:
        kinds.append("identity-absent")      # parties/case not found in cached text -> possible mis-cache
    if id_caption:
        kinds.append("identity-caption")     # parties present but caption-match uncertain (often benign)

    # --- (b) holding concordance ------------------------------------------------------
    overlaps = {}
    for l, r in readable.items():
        nt = norm_tokens((r.get("conclusions") or {}).get("holding"))
        overlaps[l] = {
            "overlap_coef": round(overlap_coef(p_hold_tokens, nt), 3),
            "jaccard": round(jaccard(p_hold_tokens, nt), 3),
        }
        detail["lenses"][l]["overlap"] = overlaps[l]
    max_oc = max((o["overlap_coef"] for o in overlaps.values()), default=0.0)
    detail["max_overlap_coef"] = max_oc

    # presence/absence: P asserts a holding but N cannot find the case/parties in the cached text
    if p_hold_present and id_absent:
        kinds.append("presence-absence")
    # holding-direction: readable but zero shared content token with P holding
    if readable and p_hold_tokens and max_oc == 0.0:
        kinds.append("holding-overlap-zero")
    # cross-lens outcome-direction conflict (one lens AFFIRM, the other REVERSE)
    dirs = {
        disp_direction((r.get("conclusions") or {}).get("disposition"))
        for r in readable.values()
    }
    dirs.discard(None)
    if {"AFFIRM", "REVERSE"} <= dirs:
        kinds.append("holding-direction-conflict")

    # --- treatment: ADVISORY ONLY.  N reads are as-of-decision (manifest-blind to later
    #     treatment); self-negative string matches are dominated by false positives
    #     ("X remains good law", "no prior case is overruled").  Surfacing them as
    #     DISCORDANT would bury real conflicts under noise, so they route to a separate,
    #     labeled advisory bucket -- treatment currency is R7's job, not the N re-derivation.
    treatment_advisory = None
    b = readable.get("B")
    if b:
        tr = (b.get("conclusions") or {}).get("treatment") or {}
        gl = str(tr.get("good_law_as_of_decision") or "")
        p_valid = (p_item.get("treatment") or {}).get("field_i_validity")
        if TREATMENT_SELFNEG.search(gl) and p_valid == "good_law":
            m = TREATMENT_SELFNEG.search(gl)
            treatment_advisory = {
                "p_field_i_validity": p_valid,
                "n_good_law_excerpt": gl[max(0, m.start() - 20): m.start() + 140],
            }

    # --- classify ---------------------------------------------------------------------
    if kinds:
        cls = "DISCORDANT-candidate"                    # any discordance signal (incl. bare identity flag)
    elif not readable:
        cls = "UNREADABLE"                              # nothing parsed w/ a holding, and no identity flag
    elif len(readable) == 2 and max_oc >= STRONG_OVERLAP_COEF:
        cls = "CONCORDANT-STRONG"
    else:
        cls = "CONCORDANT-WEAK"   # single-lens only, or low holding overlap

    return {
        "class": cls,
        "kinds": kinds,
        "lenses_read": sorted(readable.keys()),
        "evidence_refs": evidence,
        "detail": detail if (kinds or treatment_advisory) else None,
        "treatment_advisory": treatment_advisory,
    }


# --------------------------------------------------------------------------- #
# Doctrine reconciliation (coverage grain + split calls)
# --------------------------------------------------------------------------- #
def build_case_indexes(p):
    by_cluster, by_caption, by_path = {}, {}, {}
    sig_map = defaultdict(set)  # party-signature -> {p_id,...} (ambiguous sigs are not resolved)
    by_id = {}
    home_doctrines = defaultdict(set)  # case_path -> {doctrine_title,...}
    for it in p["items"]:
        if it["kind"] == "case":
            by_id[it["p_id"]] = it
            cid = (it.get("lake") or {}).get("cluster_id")
            if cid is not None:
                by_cluster.setdefault(cid, it)
            for cap in (it.get("title"), (it.get("lake") or {}).get("record_id")):
                nc = norm_caption(cap)
                if nc:
                    by_caption.setdefault(nc, it)
                sig = caption_signature(cap)
                if len(sig) >= 2:
                    sig_map[sig].add(it["p_id"])
            by_path.setdefault(it.get("path"), it)
    for it in p["items"]:
        if it["kind"] == "doctrine":
            for hc in ((it.get("case_set") or {}).get("homed_cases") or []):
                home_doctrines[hc.get("case_path")].add(it.get("title") or it.get("p_id"))
    by_sig = {sig: next(iter(pids)) for sig, pids in sig_map.items() if len(pids) == 1}
    return {
        "by_cluster": by_cluster,
        "by_caption": by_caption,
        "by_path": by_path,
        "by_sig": by_sig,
        "by_id": by_id,
        "home_doctrines": home_doctrines,
    }


def resolve_case(entry, cidx):
    """Resolve an N-derived case_set entry (caption+cluster_id) to a P case item, or None.
    Order: cluster_id (P lake) -> exact normalized caption -> unambiguous party-token signature."""
    cid = entry.get("cluster_id")
    if cid is not None and cid in cidx["by_cluster"]:
        return cidx["by_cluster"][cid]
    nc = norm_caption(entry.get("caption"))
    if nc in cidx["by_caption"]:
        return cidx["by_caption"][nc]
    sig = caption_signature(entry.get("caption"))
    if len(sig) >= 2 and sig in cidx["by_sig"]:
        return cidx["by_id"][cidx["by_sig"][sig]]
    return None


def classify_doctrine(p_item, n_row, cidx, coverage, unreadable_paths):
    doc_path = p_item.get("path")
    evidence = [f"P:{doc_path}"]

    # skip-disposition rows: dispositioned, not a conflict surface
    if n_row is not None and "disposition" in n_row:
        evidence.append(f"N-skip:{n_row.get('disposition')}::covered_by={n_row.get('covered_by')}")
        return {
            "class": "N-SKIP-DISPOSITION",
            "join": "N-skip-disposition",
            "evidence_refs": evidence,
            "coverage_gaps": [],
            "over_inclusions": [],
            "split_diff": None,
            "detail": None,
        }

    if n_row is None:
        return {
            "class": "JOIN-MISS",
            "join": "JOIN-MISS",
            "evidence_refs": evidence,
            "coverage_gaps": [],
            "over_inclusions": [],
            "split_diff": None,
            "detail": None,
        }

    evidence.append(f"N-derive:{n_row.get('lane')}::{n_row.get('model')}")
    derived = n_row.get("derived") or {}
    n_cases = derived.get("case_set") or []

    # P-homed identity set for this doctrine (keyed by case path)
    p_homed = OrderedDict()
    for hc in ((p_item.get("case_set") or {}).get("homed_cases") or []):
        p_homed[hc.get("case_path")] = hc.get("role")

    # ---- coverage-gap: cases N derives that P does NOT home here ----
    coverage_gaps = []
    matched_p_paths = set()
    for entry in n_cases:
        pc = resolve_case(entry, cidx)
        entry_path = pc.get("path") if pc else None
        if entry_path and entry_path in p_homed:
            matched_p_paths.add(entry_path)
            continue  # N-derived case IS homed here -> concordant on this case
        # pre-classify the gap
        role = entry.get("role_claim")
        cu = entry.get("candidate_unverified") is True
        if pc:
            homes = cidx["home_doctrines"].get(pc.get("path")) or set()
            gap_class = "homed-elsewhere" if homes else "P-case-unhomed"
        else:
            cid = entry.get("cluster_id")
            term = coverage["by_cluster"].get(cid) if cid is not None else None
            if term is None:
                term = coverage["by_caption"].get(norm_caption(entry.get("caption")))
            if term in LEDGER_KNOWN_TERMINALS:
                gap_class = f"known-ledger:{term}"
            elif term == "authored":
                gap_class = "ledger-authored"
            elif cu:
                gap_class = "N-unverified"
            else:
                gap_class = "UNKNOWN-gap"
        coverage_gaps.append(
            {
                "caption": entry.get("caption"),
                "cluster_id": entry.get("cluster_id"),
                "n_role": role,
                "candidate_unverified": cu,
                "gap_class": gap_class,
                "resolved_p_path": pc.get("path") if pc else None,
            }
        )

    # ---- over-inclusion: cases P homes that N did NOT derive ----
    # Over-inclusion (P superset of N) is NOT a corpus defect -- N's blind re-derivation is a
    # focused key-case subset, so P homing more is expected.  It is surfaced (never buried) but
    # does NOT trigger DISCORDANT-candidate.  Buckets: n-blind-unread (case had no readable N read)
    # / expected-role (foil/history/related/etc.) / over-inclusion-candidate (core-role case a
    # blind read missed -- worth a glance).
    over_inclusions = []
    for cpath, role in p_homed.items():
        if cpath in matched_p_paths:
            continue
        if cpath in unreadable_paths:
            oi_class = "n-blind-unread"
        elif role and EXPECTED_OI_ROLE.search(role):
            oi_class = "expected-role"
        else:
            oi_class = "over-inclusion-candidate"
        over_inclusions.append({"case_path": cpath, "p_role": role, "oi_class": oi_class})

    # ---- split-call diff (presence grain; direction is agent work) ----
    p_split = (p_item.get("split") or {})
    p_has = bool(p_split.get("has_split_signal"))
    n_splits = derived.get("splits") or []
    n_has = bool(n_splits)
    split_diff = None
    if p_has != n_has:
        split_diff = {
            "p_has_split_signal": p_has,
            "n_has_split": n_has,
            "kind": "N-only-split" if n_has else "P-only-split",
            "n_split_questions": [s.get("question") for s in n_splits if isinstance(s, dict)][:4],
            "p_circuit_positions": [
                {"case": cp.get("case"), "label": cp.get("label")}
                for cp in (p_split.get("circuit_positions") or [])
            ][:6],
        }

    unknown_gaps = [g for g in coverage_gaps if g["gap_class"] == "UNKNOWN-gap"]
    oi_candidates = [o for o in over_inclusions if o["oi_class"] == "over-inclusion-candidate"]

    # DISCORDANT-candidate triggers only on signals of a possible CORPUS defect: a coverage-gap
    # (N found a case P should home but lacks) or a split-presence diff.  Over-inclusion is
    # expected N-blindness (surfaced as WEAK, not a candidate).
    if unknown_gaps or split_diff:
        cls = "DISCORDANT-candidate"
    elif oi_candidates or coverage_gaps or over_inclusions:
        cls = "CONCORDANT-WEAK"   # diffs exist but all pre-explained (ledger/role/elsewhere/blind)
    else:
        cls = "CONCORDANT-STRONG"

    detail = None
    if cls == "DISCORDANT-candidate" or oi_candidates:
        detail = {
            "doctrine_title": p_item.get("title") or p_item.get("topic"),
            "unknown_gaps": unknown_gaps,
            "oi_candidates": oi_candidates,
            "split_diff": split_diff,
            "p_homed_count": len(p_homed),
            "n_derived_count": len(n_cases),
        }

    return {
        "class": cls,
        "join": "matched",
        "evidence_refs": evidence,
        "coverage_gaps": coverage_gaps,
        "over_inclusions": over_inclusions,
        "split_diff": split_diff,
        "detail": detail,
    }


# --------------------------------------------------------------------------- #
# Top-level reconcile
# --------------------------------------------------------------------------- #
def reconcile(p, reads, doc_rows, coverage):
    pcase = [it for it in p["items"] if it["kind"] == "case"]
    pdoc = [it for it in p["items"] if it["kind"] == "doctrine"]

    # index N case reads by case_id (== P p_id) and lens; also by record_id for join-audit
    reads_by_case = defaultdict(dict)
    n_case_ids = set()
    n_record_ids = set()
    for r in reads:
        reads_by_case[r.get("case_id")][r.get("lens")] = r
        n_case_ids.add(r.get("case_id"))
        n_record_ids.add(r.get("record_id"))

    doc_by_id = {r["doctrine_id"]: r for r in doc_rows}

    cidx = build_case_indexes(p)

    rows = []
    counts = Counter()
    kind_counts = Counter()
    join_miss = []
    treatment_advisories = []
    doctrine_gap_summary = Counter()
    doctrine_oi_summary = Counter()

    # ---- cases ----
    for it in pcase:
        pid = it["p_id"]
        lensrows = reads_by_case.get(pid, {})
        if not lensrows:
            join = "JOIN-MISS"
            row = {
                "p_id": pid,
                "kind": "case",
                "title": it.get("title"),
                "class": "JOIN-MISS",
                "join": join,
                "evidence_refs": [f"P:{it.get('path')}"],
            }
            join_miss.append(
                {"p_id": pid, "kind": "case", "title": it.get("title"), "path": it.get("path"),
                 "record_id": (it.get("lake") or {}).get("record_id")}
            )
            counts["JOIN-MISS"] += 1
        else:
            res = classify_case(it, lensrows)
            join = "matched"
            row = {
                "p_id": pid,
                "kind": "case",
                "title": it.get("title"),
                "citation": it.get("citation"),
                "class": res["class"],
                "join": join,
                "lenses_read": res["lenses_read"],
                "discordance_kinds": res["kinds"],
                "evidence_refs": res["evidence_refs"],
            }
            if res["detail"]:
                row["discordance_detail"] = res["detail"]
            if res["treatment_advisory"]:
                row["treatment_advisory"] = res["treatment_advisory"]
                treatment_advisories.append({"p_id": pid, "title": it.get("title"),
                                             **res["treatment_advisory"]})
            counts[res["class"]] += 1
            for k in res["kinds"]:
                kind_counts[k] += 1
        rows.append(row)

    # case paths with no readable N read (UNREADABLE or JOIN-MISS) -> N-blind for doctrine OI
    unreadable_paths = {
        it.get("path") for it, row in zip(pcase, rows)
        if row["class"] in ("UNREADABLE", "JOIN-MISS")
    }

    # ---- doctrines ----
    for it in pdoc:
        pid = it["p_id"]
        n_row = doc_by_id.get(pid)
        res = classify_doctrine(it, n_row, cidx, coverage, unreadable_paths)
        row = {
            "p_id": pid,
            "kind": "doctrine",
            "title": it.get("title") or it.get("topic") or pid,
            "class": res["class"],
            "join": res["join"],
            "evidence_refs": res["evidence_refs"],
        }
        if res["coverage_gaps"]:
            row["coverage_gaps"] = res["coverage_gaps"]
            for g in res["coverage_gaps"]:
                doctrine_gap_summary[g["gap_class"]] += 1
        if res["over_inclusions"]:
            row["over_inclusions"] = res["over_inclusions"]
            for o in res["over_inclusions"]:
                doctrine_oi_summary[o["oi_class"]] += 1
        if res["split_diff"]:
            row["split_diff"] = res["split_diff"]
        if res["detail"]:
            row["discordance_detail"] = res["detail"]
        counts["doc:" + res["class"]] += 1
        rows.append(row)

    # ---- join audit (both directions) ----
    p_case_ids = {it["p_id"] for it in pcase}
    p_doc_ids = {it["p_id"] for it in pdoc}
    n_orphan_cases = sorted(n_case_ids - p_case_ids)
    n_orphan_docs = sorted(set(doc_by_id) - p_doc_ids)

    summary = {
        "lane": "s9-p2-reconcile",
        "model": "claude-opus-4-8",
        "spec": "S9 R5",
        "totals": {
            "p_items": len(p["items"]),
            "p_cases": len(pcase),
            "p_doctrines": len(pdoc),
            "n_read_rows": len(reads),
            "n_cases_covered": len(n_case_ids & p_case_ids),
            "n_doctrine_rows": len(doc_rows),
        },
        "case_class_counts": {k: counts[k] for k in
                              ["CONCORDANT-STRONG", "CONCORDANT-WEAK", "DISCORDANT-candidate",
                               "UNREADABLE", "JOIN-MISS"] if counts[k]},
        "case_discordance_kind_counts": dict(kind_counts),
        "doctrine_class_counts": {k.replace("doc:", ""): v for k, v in counts.items()
                                  if k.startswith("doc:")},
        "doctrine_coverage_gap_counts": dict(doctrine_gap_summary),
        "doctrine_over_inclusion_counts": dict(doctrine_oi_summary),
        "treatment_advisory_count": len(treatment_advisories),
        "no_regression_floor": {
            "declared": p.get("no_regression_floor"),
            "dispositioned": len(rows),
            "join_miss_count": len(join_miss),
            "n_orphan_case_ids": n_orphan_cases,
            "n_orphan_doctrine_ids": n_orphan_docs,
            "floor_satisfied": len(rows) == len(p["items"]),
        },
        "residual": {
            "reads_parse_status": dict(Counter((r.get("parse") or {}).get("status") for r in reads)),
            "cases_no_readable_lens": counts["UNREADABLE"],
            "note": "Reads may still be sweeping; UNREADABLE = no parsed lens yet (no_cached_text/"
                    "no_read). Re-run after the sweep completes; classes for swept cases will settle.",
        },
    }
    return rows, summary, {
        "join_miss": join_miss,
        "treatment_advisories": treatment_advisories,
        "n_orphan_cases": n_orphan_cases,
        "n_orphan_docs": n_orphan_docs,
    }


# --------------------------------------------------------------------------- #
# Output writers
# --------------------------------------------------------------------------- #
def write_reconciliation_jsonl(rows, path):
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def _md_case_candidate_line(row):
    det = row.get("discordance_detail") or {}
    lenses = det.get("lenses") or {}
    parts = []
    for l in sorted(lenses):
        lv = lenses[l]
        parts.append(
            f"lens {l}: match={lv.get('match')} present={lv.get('present')} "
            f"disp={lv.get('disposition')!r} oc={(lv.get('overlap') or {}).get('overlap_coef')}"
        )
    kinds = ",".join(row.get("discordance_kinds") or [])
    return (f"- **{row['title']}** ({row.get('citation','')}) `{row['p_id']}` — kinds: **{kinds}**\n"
            f"    - P holding: {(det.get('p_holding') or '')[:220]}\n"
            f"    - N: {' | '.join(parts)}\n"
            f"    - refs: {', '.join(row.get('evidence_refs') or [])}\n")


def write_queue_md(rows, summary, extra, path):
    cases = [r for r in rows if r["kind"] == "case"]
    docs = [r for r in rows if r["kind"] == "doctrine"]
    case_cands = [r for r in cases if r["class"] == "DISCORDANT-candidate"]
    doc_cands = [r for r in docs if r["class"] == "DISCORDANT-candidate"]

    # group case candidates by primary kind priority
    priority = ["presence-absence", "identity-absent", "holding-overlap-zero",
                "holding-direction-conflict", "identity-caption"]

    def primary_kind(r):
        ks = r.get("discordance_kinds") or []
        for p in priority:
            if p in ks:
                return p
        return ks[0] if ks else "other"

    groups = defaultdict(list)
    for r in case_cands:
        groups[primary_kind(r)].append(r)

    lines = []
    A = lines.append
    A("# S9 P2 — Discordance Adjudication Queue\n")
    A(f"> Lane `{summary['lane']}` · model `{summary['model']}` · spec {summary['spec']}. "
      "Mechanical reconciliation of Thread-P (built corpus) vs Thread-N (blind re-derivation). "
      "Every candidate below is for the **orchestrator** to adjudicate (what diverged / which stands). "
      "The script fails toward candidate and never buries a conflict.\n")
    A("## Summary\n")
    A(f"- Case classes: {json.dumps(summary['case_class_counts'])}")
    A(f"- Case discordance kinds: {json.dumps(summary['case_discordance_kind_counts'])}")
    A(f"- Doctrine classes: {json.dumps(summary['doctrine_class_counts'])}")
    A(f"- Doctrine coverage-gap classes: {json.dumps(summary['doctrine_coverage_gap_counts'])}")
    A(f"- Doctrine over-inclusion classes: {json.dumps(summary['doctrine_over_inclusion_counts'])}")
    A(f"- No-regression floor satisfied: **{summary['no_regression_floor']['floor_satisfied']}** "
      f"({summary['no_regression_floor']['dispositioned']}/{summary['totals']['p_items']} P items "
      f"dispositioned; JOIN-MISS={summary['no_regression_floor']['join_miss_count']})")
    A(f"- Residual (reads sweeping): UNREADABLE={summary['residual']['cases_no_readable_lens']} "
      f"cases; parse status {json.dumps(summary['residual']['reads_parse_status'])}\n")

    # JOIN-MISS
    A("## JOIN-MISS (P items with no N disposition — no-regression floor)\n")
    if extra["join_miss"]:
        for jm in extra["join_miss"]:
            A(f"- `{jm['p_id']}` **{jm['title']}** ({jm['kind']}) — {jm['path']}")
    else:
        A("- none")
    if extra["n_orphan_cases"] or extra["n_orphan_docs"]:
        A(f"\n> N-side orphans (N ids absent from P): cases={extra['n_orphan_cases']} "
          f"docs={extra['n_orphan_docs']}")
    A("")

    # Case candidates by kind
    A("## Case discordance candidates (judgment grain)\n")
    order = priority + sorted(k for k in groups if k not in priority)
    for kind in order:
        grp = groups.get(kind)
        if not grp:
            continue
        A(f"### {kind}  ({len(grp)})\n")
        for r in sorted(grp, key=lambda x: x["p_id"]):
            A(_md_case_candidate_line(r))
        A("")

    # Doctrine candidates
    A("## Doctrine discordance candidates (coverage + split grain)\n")
    if not doc_cands:
        A("- none\n")
    for r in sorted(doc_cands, key=lambda x: x["p_id"]):
        det = r.get("discordance_detail") or {}
        A(f"### {r['title']} `{r['p_id']}`  (P-homed {det.get('p_homed_count')} / "
          f"N-derived {det.get('n_derived_count')})")
        for g in det.get("unknown_gaps") or []:
            A(f"  - UNKNOWN coverage-gap: **{g['caption']}** (cluster {g['cluster_id']}, "
              f"N-role {g['n_role']}, cand_unverified={g['candidate_unverified']})")
        for o in det.get("oi_candidates") or []:
            A(f"  - over-inclusion candidate: {o['case_path']} (P-role: {o['p_role']})")
        sd = det.get("split_diff")
        if sd:
            A(f"  - split diff [{sd['kind']}]: P_signal={sd['p_has_split_signal']} "
              f"N_split={sd['n_has_split']}; N-questions={sd.get('n_split_questions')}")
        A("")

    # Over-inclusion advisory (WEAK -- P superset of N is expected N-blindness, NOT a defect;
    # listed so a core-role case a blind read entirely missed still gets a glance).
    oi_docs = [r for r in docs
               if any((o.get("oi_class") == "over-inclusion-candidate")
                      for o in (r.get("over_inclusions") or []))]
    A("## Over-inclusion advisory (WEAK; P homes, N lacks — expected N-blindness)\n")
    A("> Not counted as DISCORDANT-candidate. Only core-role misses (non foil/history/progeny-"
      "role, N could read the case) are listed; n-blind-unread and expected-role are omitted here.\n")
    if not oi_docs:
        A("- none\n")
    for r in sorted(oi_docs, key=lambda x: x["p_id"]):
        cands = [o for o in r["over_inclusions"] if o["oi_class"] == "over-inclusion-candidate"]
        A(f"- **{r['title']}** `{r['p_id']}` ({len(cands)}): "
          + "; ".join(f"{o['case_path'].split('/')[-1][:-3]} [{o['p_role']}]" for o in cands[:8]))
    A("")

    # Treatment advisory (NOT candidates -- as-of-decision blindness; agent/currency read)
    A("## Treatment-currency advisory (low-confidence; NOT auto-adjudicated)\n")
    A("> N reads are as-of-decision (manifest-blind to later treatment); self-negative string "
      "matches are dominated by false positives. Surfaced (never buried) for the R7 currency "
      "sweep / agent read, but not counted as DISCORDANT-candidate.\n")
    if extra["treatment_advisories"]:
        for t in sorted(extra["treatment_advisories"], key=lambda x: x["p_id"]):
            A(f"- **{t['title']}** `{t['p_id']}` — P.validity={t['p_field_i_validity']}; "
              f"N excerpt: …{t['n_good_law_excerpt'].strip()}…")
    else:
        A("- none")
    A("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# --------------------------------------------------------------------------- #
# Self-test (synthetic fixtures, no I/O on the real lake)
# --------------------------------------------------------------------------- #
def _read(case_id, lens, *, holding, match=True, present=True, disp="affirmed",
          parse="parsed", treatment=None, rid="rec"):
    concl = {"holding": holding, "disposition": disp,
             "identity": {"match": match, "present": present, "parties_in_text": "x"}}
    if treatment is not None:
        concl["treatment"] = treatment
    return {"case_id": case_id, "record_id": rid, "lens": lens, "id": f"{case_id}-{lens}",
            "parse": {"status": parse}, "conclusions": concl, "cached_text_path": "/x.txt"}


def selftest():
    # --- synthetic P ---
    def pcase(pid, title, holding, hp=True, cluster=None, validity="good_law", homes=None):
        return {"kind": "case", "p_id": pid, "title": title, "citation": "1 U.S. 1",
                "path": f"cases/{title}.md", "holding": holding, "holding_present": hp,
                "homes": homes or [], "related": [],
                "treatment": {"field_i_validity": validity},
                "lake": {"cluster_id": cluster, "record_id": title}}

    def pdoc(pid, title, homed, split_signal=False, circuit_positions=None):
        return {"kind": "doctrine", "p_id": pid, "title": title, "path": f"{title}.md",
                "type": "doctrine",
                "case_set": {"homed_cases": homed, "homed_count": len(homed)},
                "split": {"has_split_signal": split_signal,
                          "circuit_positions": circuit_positions or []}}

    p = {
        "no_regression_floor": 9,
        "items": [
            pcase("P-c-strong", "Strong Case",
                  "The warrantless search of the home violated the Fourth Amendment absent exigency."),
            pcase("P-c-weak", "Weak Case",
                  "Probable cause supported the automobile search under the vehicle exception."),
            pcase("P-c-ident", "Ident Case", "Some holding about consent searches and voluntariness."),
            pcase("P-c-absent", "Absent Case", "A holding about stop-and-frisk reasonable suspicion."),
            pcase("P-c-zero", "Zero Case", "alpha bravo charlie delta echo foxtrot golf hotel india"),
            pcase("P-c-unread", "Unread Case", "A holding never read by N yet pending the sweep."),
            pcase("P-c-absent2", "Absent2 Case", "A real holding P asserts about curtilage."),
            pcase("P-c-joinmiss", "Joinmiss Case", "A holding with no N read at all."),
            pdoc("P-d-doc1", "Doctrine One",
                 [{"case_path": "cases/Strong Case.md", "case_title": "Strong Case", "role": "Key — Anchor"},
                  {"case_path": "cases/Foil Case.md", "case_title": "Foil Case", "role": "Historical (foil)"}],
                 split_signal=False),
            pdoc("P-d-doc2", "Doctrine Two",
                 [{"case_path": "cases/Weak Case.md", "case_title": "Weak Case", "role": "Key"}],
                 split_signal=True,
                 circuit_positions=[{"case": "Weak Case", "label": "Binding — 9th"}]),
        ],
    }

    reads = [
        # strong: both lenses, high overlap, clean identity
        _read("P-c-strong", "A", holding="The warrantless search of the home violated the Fourth "
              "Amendment absent exigency circumstances."),
        _read("P-c-strong", "B", holding="Warrantless home search violated the Fourth Amendment "
              "with no exigency present.", treatment={"good_law_as_of_decision": "controlling good law"}),
        # weak: single lens only
        _read("P-c-weak", "A", holding="Probable cause supported the automobile search vehicle exception."),
        # identity-caption: match False, present True, holding fine
        _read("P-c-ident", "A", holding="Some holding about consent searches and voluntariness.",
              match=False, present=True),
        _read("P-c-ident", "B", holding="Consent search voluntariness holding.", match=False, present=True),
        # presence-absence: present False
        _read("P-c-absent", "A", holding="A holding about stop and frisk reasonable suspicion.",
              match=False, present=False),
        _read("P-c-absent", "B", holding="Stop and frisk reasonable suspicion.", match=False, present=False),
        # zero overlap
        _read("P-c-zero", "A", holding="zulu yankee xray whiskey victor uniform tango sierra romeo"),
        _read("P-c-zero", "B", holding="quebec papa oscar november mike lima kilo juliet"),
        # unread: parse no_cached_text
        _read("P-c-unread", "A", holding="", parse="no_cached_text"),
        _read("P-c-unread", "B", holding="", parse="no_read"),
        # absent2: parsed but present=False AND empty holding -> must NOT be masked as UNREADABLE;
        # the present=False (case-not-in-cached-text) signal surfaces as identity-absent + presence
        _read("P-c-absent2", "A", holding="", parse="parsed", match=None, present=False),
        _read("P-c-absent2", "B", holding="", parse="parsed", match=None, present=False),
        # (P-c-joinmiss: NO reads at all)
    ]

    doc_rows = [
        # doctrine one: N derives Strong (homed) + New Gap (unknown) + Foil (P has as foil-role oi ok);
        # but Foil Case is P-homed and NOT N-derived -> expected-role over-inclusion
        {"doctrine_id": "P-d-doc1", "lane": "D-1", "model": "claude-fable-5",
         "derived": {"case_set": [
             {"caption": "Strong Case", "cluster_id": None, "role_claim": "anchor"},
             {"caption": "New Gap Case", "cluster_id": 999999, "role_claim": "rule-bearing",
              "candidate_unverified": False},
         ], "splits": [], "negative_notes": []}},
        # doctrine two: P signals split, N finds none -> P-only split diff -> candidate
        {"doctrine_id": "P-d-doc2", "lane": "D-1", "model": "claude-fable-5",
         "derived": {"case_set": [
             {"caption": "Weak Case", "cluster_id": None, "role_claim": "anchor"},
         ], "splits": [], "negative_notes": []}},
    ]

    coverage = {"by_cluster": {}, "by_caption": {}}
    rows, summary, extra = reconcile(p, reads, doc_rows, coverage)
    by_id = {r["p_id"]: r for r in rows}

    def expect(pid, cls, kinds=None):
        r = by_id[pid]
        assert r["class"] == cls, f"{pid}: got {r['class']} expected {cls}"
        if kinds is not None:
            assert set(r.get("discordance_kinds") or []) == set(kinds), \
                f"{pid}: kinds {r.get('discordance_kinds')} != {kinds}"

    expect("P-c-strong", "CONCORDANT-STRONG", [])
    expect("P-c-weak", "CONCORDANT-WEAK", [])
    expect("P-c-ident", "DISCORDANT-candidate", ["identity-caption"])
    expect("P-c-absent", "DISCORDANT-candidate", ["identity-absent", "presence-absence"])
    expect("P-c-zero", "DISCORDANT-candidate", ["holding-overlap-zero"])
    expect("P-c-unread", "UNREADABLE")
    expect("P-c-absent2", "DISCORDANT-candidate", ["identity-absent", "presence-absence"])
    expect("P-c-joinmiss", "JOIN-MISS")
    assert by_id["P-c-joinmiss"]["join"] == "JOIN-MISS"

    # doctrine one: has an UNKNOWN gap (New Gap Case) -> candidate; foil over-inclusion expected
    d1 = by_id["P-d-doc1"]
    assert d1["class"] == "DISCORDANT-candidate", d1["class"]
    assert any(g["gap_class"] == "UNKNOWN-gap" and g["caption"] == "New Gap Case"
               for g in d1["coverage_gaps"]), d1["coverage_gaps"]
    assert any(o["oi_class"] == "expected-role" for o in d1["over_inclusions"]), d1["over_inclusions"]

    # doctrine two: P-only split diff -> candidate
    d2 = by_id["P-d-doc2"]
    assert d2["class"] == "DISCORDANT-candidate", d2["class"]
    assert d2["split_diff"]["kind"] == "P-only-split"

    # floor: all 10 P items dispositioned
    assert summary["no_regression_floor"]["dispositioned"] == 10
    assert summary["no_regression_floor"]["floor_satisfied"] is True
    assert summary["no_regression_floor"]["join_miss_count"] == 1

    # determinism: identical rerun -> identical serialized rows
    rows2, _, _ = reconcile(p, reads, doc_rows, coverage)
    s1 = "\n".join(json.dumps(r, sort_keys=True, ensure_ascii=False) for r in rows)
    s2 = "\n".join(json.dumps(r, sort_keys=True, ensure_ascii=False) for r in rows2)
    assert s1 == s2, "non-deterministic output"

    print("SELFTEST PASS  (10/10 fixtures; case+doctrine classes, identity-absent unmasking, "
          "floor, determinism)")
    return True


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="S9 P2 reconciliation engine (spec R5)")
    ap.add_argument("--thread-p", default="_run/s9/thread-P.json")
    ap.add_argument("--reads", default="_run/s9/thread-N-reads.jsonl")
    ap.add_argument("--doctrine", default="_run/s9/thread-N-doctrine.jsonl")
    ap.add_argument("--coverage", default="_run/s6-coverage-ledger.json")
    ap.add_argument("--out-jsonl", default="_run/s9/reconciliation.jsonl")
    ap.add_argument("--out-queue", default="_run/s9/P2-DISCORDANCE-QUEUE.md")
    ap.add_argument("--out-summary", default="_run/s9/reconciliation-summary.json")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        ok = selftest()
        sys.exit(0 if ok else 1)

    p = load_thread_p(args.thread_p)
    reads = load_jsonl(args.reads)
    doc_rows = load_jsonl(args.doctrine)
    coverage = load_coverage(args.coverage)

    rows, summary, extra = reconcile(p, reads, doc_rows, coverage)

    write_reconciliation_jsonl(rows, args.out_jsonl)
    write_queue_md(rows, summary, extra, args.out_queue)
    with open(args.out_summary, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2, sort_keys=True)

    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
