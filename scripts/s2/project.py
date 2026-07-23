#!/usr/bin/env python3
"""S2 lake-to-case-frontmatter projector.

Dry-run is the default. Use --write for the guarded content rewrite.
"""

import argparse
import glob
import json
import os
import shutil
import sys
import tempfile
from collections import Counter, OrderedDict


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.s2 import serializer  # noqa: E402


LAKE_REL = os.path.join("_overhaul2", "lake")
CASES_REL = os.path.join(LAKE_REL, "cases")
MIGRATION_REL = os.path.join(LAKE_REL, "_treatment-migration.json")
CONTENT_CASES_REL = os.path.join("content", "cases")
S2_FIXTURES_REL = os.path.join("scripts", "s2", "fixtures")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def load_records(lake_root=None, diagnostics=None):
    lake_root = lake_root or os.path.join(REPO_ROOT, LAKE_REL)
    records = {}
    record_paths = {}
    for path in sorted(glob.glob(os.path.join(lake_root, "cases", "*.json"))):
        record = load_json(path)
        rid = record.get("record_id")
        if not rid:
            if diagnostics is not None:
                diagnostics.append({"path": path, "warning": "missing record_id"})
            continue
        records[rid] = record
        record_paths[rid] = path
    return records, record_paths


def case_page_paths(paths=None):
    if paths:
        out = []
        for raw in paths:
            path = raw if os.path.isabs(raw) else os.path.join(REPO_ROOT, raw)
            if os.path.isdir(path):
                out.extend(sorted(glob.glob(os.path.join(path, "*.md"))))
            elif os.path.isfile(path) and path.endswith(".md"):
                out.append(path)
            else:
                out.extend(sorted(glob.glob(path, recursive=True)))
        return [p for p in out if p.endswith(".md")]
    return sorted(glob.glob(os.path.join(REPO_ROOT, CONTENT_CASES_REL, "*.md")))


def page_stem(path):
    return os.path.splitext(os.path.basename(path))[0]


def date_from_record(record):
    modified = record.get("provenance", {}).get("date_modified")
    if isinstance(modified, str) and len(modified) >= 10:
        return modified[:10]
    # CR-13: fail closed rather than guessing today()'s date. A today()
    # fallback silently writes a fresh lake.projected_at on every new-day run,
    # producing a phantom diff that defeats the idempotence contract this tool
    # tests via verify_idempotent()/self_test(). Consistent with the rest of
    # this file (authority_weight raises rather than guessing a bad circuit).
    rid = record.get("record_id") or "<unknown>"
    raise ValueError(
        "record %r lacks provenance.date_modified; fill it before projection" % rid
    )


def citation_string(citation):
    if not citation:
        return ""
    if isinstance(citation, str):
        return citation
    if citation.get("cite"):
        return str(citation["cite"])
    parts = [citation.get("volume"), citation.get("reporter"), citation.get("page")]
    return " ".join(str(part).strip() for part in parts if part not in (None, ""))


def citation_with_year(record):
    official = citation_string(record.get("citations", {}).get("official"))
    if not official:
        official = record.get("citations", {}).get("display") or ""
    # slip-only single source (S2 A3): a record marked `citations.slip_only` with no
    # reporter cite yet derives the honest slip form HERE, so the projector and the
    # S6 mint agree — no page-vs-projection drift (LINT-12). The slip cite already
    # carries its year, so it is returned as-is.
    if not official and record_is_slip_only(record):
        slip = derive_slip_cite(record)
        if slip:
            return slip
    year = record.get("identity", {}).get("year")
    if official and year and "(%s)" % year not in official:
        return "%s (%s)" % (official, year)
    return official


def joined_cites(citations):
    return "; ".join(citation_string(cite) for cite in citations or [] if citation_string(cite))


def circuit_label(value):
    if not value:
        return None
    text = str(value).strip()
    low = text.lower().replace(".", "")
    if low in ("dc", "d c", "cadc"):
        return "D.C. Cir."
    if low in ("fed", "federal", "cafc"):
        return "Fed. Cir."
    if low.startswith("ca") and low[2:].isdigit():
        num = int(low[2:])
    else:
        import re
        match = re.search(r"(\d+)", low)
        num = int(match.group(1)) if match else None
    if num is None or num < 1 or num > 11:
        return None
    suffix = {1: "1st", 2: "2d", 3: "3d"}.get(num, "%sth" % num if num else text)
    return "%s Cir." % suffix


# --------------------------------------------------------------------------
# slip-only support (S2 A3 slip precedent) — the SINGLE source shared by the
# projector (citation_with_year) and the S6 mint (scripts/s6/mint_page.py imports
# these), so a slip row's page citation and its projection agree (no LINT-12 drift).
# --------------------------------------------------------------------------

def record_is_slip_only(record):
    """True iff the lake record carries the EXPLICIT slip-only marker — never
    inferred from an absent citation."""
    return (record.get("citations") or {}).get("slip_only") is True


def slip_court_abbr(record):
    """Bluebook-ish court abbreviation for a slip cite, from identity."""
    ident = record.get("identity") or {}
    level = ident.get("court_level")
    if level == "scotus":
        return "U.S."
    if level == "coa":
        circ = ident.get("circuit")
        return circuit_label(circ) if circ else None
    if level == "state":
        return ident.get("state") or None
    return None


def derive_slip_cite(record):
    """PROPOSED slip-opinion cite form for the header + Case cell, behind the
    citations.slip_only marker (FLAGGED FOR RATIFICATION — S2 A3 sanctions slip
    PINPOINTS, not a slip citation display; S5 R3 sanctions no slip header form).
    Bluebook slip form: `No. <docket>, slip op. (<court> <year>)`. Returns None if
    identity is too sparse for any honest cite (no docket AND no court/year). The
    slip form is NEVER written into citations.display — the marker is the truth and
    both the projector and the mint derive from it."""
    ident = record.get("identity") or {}
    docket = ident.get("docket")
    year = ident.get("year")
    court = slip_court_abbr(record)
    tail_parts = [p for p in (court, str(year) if year else None) if p]
    tail = "(%s)" % " ".join(tail_parts) if tail_parts else ""
    if docket:
        head = "No. %s, slip op." % docket
    elif tail:
        head = "slip op."
    else:
        return None
    return ("%s %s" % (head, tail)).strip()


def authority_weight(record):
    identity = record.get("identity", {})
    level = identity.get("court_level")
    # RULING P4-20(a): a non-precedential (Unpublished) COA/district disposition is
    # persuasive-only regardless of court level. precedential_status is an OPTIONAL
    # identity-grade CL fact on a different axis from treatment; SD9's court-level-
    # only derivation presumed published dispositions and is factually wrong for a
    # non-precedential COA decision. Absent signal => every path below is unchanged.
    if level in ("coa", "district") and identity.get("precedential_status") == "Unpublished":
        return "Persuasive only \u2014 non-precedential"
    if level == "scotus":
        return "Binding \u2014 SCOTUS"
    if level == "coa":
        circuit = identity.get("circuit")
        if not circuit:
            rid = record.get("record_id") or "<unknown>"
            raise ValueError(
                "COA record %r lacks identity.circuit; fill _overhaul2/lake/cases/%s.json "
                "before projection or authority DB build" % (rid, rid)
            )
        label = circuit_label(circuit)
        if not label:
            rid = record.get("record_id") or "<unknown>"
            raise ValueError(
                "COA record %r has unrecognized identity.circuit=%r; expected 1st-11th, "
                "D.C., or Fed." % (rid, circuit)
            )
        return "Binding in-circuit \u2014 %s" % label
    if level == "district":
        return "Persuasive only \u2014 non-precedential"
    if level == "state":
        return "Persuasive \u2014 state, illustrative"
    return "Historical"


def courtlistener_url(record):
    absolute = record.get("identity", {}).get("absolute_url")
    if not absolute:
        return ""
    if str(absolute).startswith("http"):
        return str(absolute)
    return "https://www.courtlistener.com%s" % absolute


def treatment_projection(record):
    treatment = record.get("treatment", {})
    out = OrderedDict()
    for key in (
        "field_i_validity",
        "as_of_content",
        "as_of_treatment",
        "composite_basis",
        "composite_basis_ref",
        "varies_by_point",
        "scope_note",
        "point_overrides",
    ):
        if key in treatment:
            out[key] = treatment[key]
    return out


def project_record(record):
    identity = record.get("identity", {})
    citations = record.get("citations", {})
    projection = OrderedDict()
    projection["citation"] = citation_with_year(record)
    projection["parallel_cite"] = joined_cites(citations.get("parallel") or [])
    projection["neutral_cite"] = joined_cites(citations.get("vendor_neutral") or [])
    projection["court"] = identity.get("court") or ""
    projection["court_level"] = identity.get("court_level") or ""
    projection["circuit"] = identity.get("circuit") or ""
    projection["year"] = identity.get("year")
    projection["date_decided"] = identity.get("date_decided") or ""
    projection["docket"] = identity.get("docket") or ""
    projection["authority_weight"] = authority_weight(record)
    projection["treatment"] = treatment_projection(record)
    projection["courtlistener"] = OrderedDict([
        ("opinion_url", courtlistener_url(record)),
        ("cluster_id", identity.get("cluster_id")),
        ("opinion_id", identity.get("lead_opinion_id")),
        ("identity_checked", bool(identity.get("expected_citation_found") or record.get("status") == "verified_off_cl")),
    ])
    if record.get("status") == "verified_off_cl":
        projection["off_cl_links"] = record.get("off_cl_links") or []
    projection["lake"] = OrderedDict([
        ("record_id", record.get("record_id")),
        ("status", record.get("status")),
        ("projected_at", date_from_record(record)),
    ])
    return projection


def load_migration(migration_path=None):
    migration_path = migration_path or os.path.join(REPO_ROOT, MIGRATION_REL)
    data = load_json(migration_path)
    return data.get("mappings", {})


def a13_gate(paths=None, migration_path=None, records=None):
    mappings = load_migration(migration_path)
    mapped = set(mappings.keys())
    counts = Counter()
    unmapped = []
    review = []
    new_form = 0
    missing = []
    unmatched = []
    for path in case_page_paths(paths):
        text = serializer.read_markdown(path)
        fm, _body, _start = serializer.split_frontmatter(text)
        if fm.get("type") != "case" or serializer.is_draft_page(fm):
            continue
        lake = fm.get("lake") if isinstance(fm.get("lake"), dict) else {}
        rid = lake.get("record_id") or page_stem(path)
        if records is not None and rid not in records:
            unmatched.append((path, rid))
        treatment = fm.get("treatment") if isinstance(fm.get("treatment"), dict) else {}
        if "field_i_validity" in treatment:
            new_form += 1
            continue
        if "status" not in treatment:
            missing.append(path)
            continue
        value = str(treatment.get("status", "")).strip()
        if value.upper() == "REVIEW":
            review.append(path)
            continue
        counts[value] += 1
        if value not in mapped:
            unmapped.append((path, value))
    return {
        "legacy_counts": dict(sorted(counts.items())),
        "unmapped": unmapped,
        "review": review,
        "new_form_pages": new_form,
        "missing_treatment_status": missing,
        "unmatched_records": unmatched,
        "mapping_keys": sorted(mapped),
        "ok_to_project": not unmapped and not missing and not unmatched,
    }


def _field_counter(diff_paths):
    counts = Counter()
    for path in diff_paths:
        if not path:
            counts["$"] += 1
            continue
        parts = path.replace("[", ".[").split(".")
        if len(parts) >= 2 and parts[0] in ("treatment", "courtlistener", "lake"):
            counts[".".join(parts[:2])] += 1
        else:
            counts[parts[0]] += 1
    return counts


def dry_run_or_write(paths=None, write=False, lake_root=None):
    record_diagnostics = []
    records, record_paths = load_records(lake_root, diagnostics=record_diagnostics)
    gate = a13_gate(paths, records=records)
    if not gate["ok_to_project"]:
        return {
            "gate": gate,
            "refused": True,
            "pages_changed": 0,
            "field_counts": {},
            "page_results": [],
            "record_load_warnings": record_diagnostics,
            "projection_errors": [],
        }

    if write and record_diagnostics:
        return {
            "gate": gate,
            "refused": True,
            "pages_changed": 0,
            "field_counts": {},
            "page_results": [],
            "record_load_warnings": record_diagnostics,
            "projection_errors": [],
        }

    skipped_review = set(gate["review"])

    # CR-14: pre-validate project_record() for every matched record BEFORE any
    # write. authority_weight() (and now date_from_record()) raises for bad
    # data (e.g. a COA record missing/with an unrecognized circuit). The a13
    # gate never calls project_record(), so without this pass a bad record only
    # surfaces once the write loop reaches it — by which point earlier pages may
    # already have been os.replace()'d, leaving a partially-projected corpus and
    # a bare traceback instead of the structured refused/exit-2 path. Mirror the
    # gate's accumulate-then-refuse posture so a bad record blocks the whole
    # batch cleanly.
    projection_errors = []
    for path in case_page_paths(paths):
        text = serializer.read_markdown(path)
        fm, _body, _start = serializer.split_frontmatter(text)
        if fm.get("type") != "case" or serializer.is_draft_page(fm):
            continue
        if path in skipped_review:
            continue
        rid = fm.get("lake", {}).get("record_id") if isinstance(fm.get("lake"), dict) else None
        rid = rid or page_stem(path)
        record = records.get(rid)
        if not record:
            continue
        try:
            project_record(record)
        except Exception as exc:  # noqa: BLE001 - surface any bad record, never write a partial batch
            projection_errors.append({
                "page": os.path.relpath(path, REPO_ROOT),
                "record": os.path.relpath(record_paths[rid], REPO_ROOT),
                "error": "%s: %s" % (type(exc).__name__, exc),
            })
    if projection_errors:
        return {
            "gate": gate,
            "refused": True,
            "pages_changed": 0,
            "field_counts": {},
            "page_results": [],
            "record_load_warnings": record_diagnostics,
            "projection_errors": projection_errors,
        }

    results = []
    field_counts = Counter()
    pages_changed = 0
    for path in case_page_paths(paths):
        text = serializer.read_markdown(path)
        fm, _body, _start = serializer.split_frontmatter(text)
        if fm.get("type") != "case" or serializer.is_draft_page(fm):
            continue
        if path in skipped_review:
            continue
        rid = fm.get("lake", {}).get("record_id") if isinstance(fm.get("lake"), dict) else None
        rid = rid or page_stem(path)
        record = records.get(rid)
        if not record:
            continue
        projection = project_record(record)
        actual = serializer.managed_subset(fm)
        diffs = serializer.diff_paths(actual, projection)
        if diffs:
            pages_changed += 1
            field_counts.update(_field_counter(diffs))
            results.append({
                "page": os.path.relpath(path, REPO_ROOT),
                "record": os.path.relpath(record_paths[rid], REPO_ROOT),
                "fields": diffs,
            })
            if write:
                new_text = serializer.replace_frontmatter(text, projection)
                tmp = path + ".tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(new_text)
                os.replace(tmp, path)
    return {
        "gate": gate,
        "refused": False,
        "pages_changed": pages_changed,
        "field_counts": dict(sorted(field_counts.items())),
        "page_results": results,
        "record_load_warnings": record_diagnostics,
        "projection_errors": [],
    }


def print_summary(result, stream=None):
    stream = stream or sys.stdout
    gate = result["gate"]
    stream.write("A13 gate: %s\n" % ("PASS" if gate["ok_to_project"] else "FAIL"))
    stream.write("legacy counts: %s\n" % json.dumps(gate["legacy_counts"], sort_keys=True))
    stream.write("new-form pages: %d\n" % gate["new_form_pages"])
    stream.write("review-staged pages: %d\n" % len(gate["review"]))
    stream.write("missing treatment status/new field: %d\n" % len(gate["missing_treatment_status"]))
    stream.write("unmatched case pages: %d\n" % len(gate.get("unmatched_records", [])))
    stream.write("record JSON missing record_id: %d\n" % len(result.get("record_load_warnings", [])))
    if gate["unmapped"]:
        stream.write("unmapped legacy values:\n")
        for path, value in gate["unmapped"]:
            stream.write("  %s: %s\n" % (os.path.relpath(path, REPO_ROOT), value))
    if gate["missing_treatment_status"]:
        stream.write("missing treatment status/new field pages:\n")
        for path in gate["missing_treatment_status"]:
            stream.write("  %s\n" % os.path.relpath(path, REPO_ROOT))
    if gate.get("unmatched_records"):
        stream.write("unmatched case pages:\n")
        for path, rid in gate["unmatched_records"]:
            stream.write("  %s: %s\n" % (os.path.relpath(path, REPO_ROOT), rid))
    if result.get("record_load_warnings"):
        stream.write("record load warnings:\n")
        for row in result["record_load_warnings"]:
            stream.write("  WARNING %s: %s\n" % (os.path.relpath(row["path"], REPO_ROOT), row["warning"]))
    if result.get("projection_errors"):
        stream.write("projection validation errors (batch refused, no writes): %d\n" % len(result["projection_errors"]))
        for row in result["projection_errors"]:
            stream.write("  ERROR %s: %s\n" % (row["page"], row["error"]))
    if result["refused"]:
        stream.write("projection refused by A13 gate, record load warnings, or projection validation errors\n")
        return
    stream.write("pages that would change: %d\n" % result["pages_changed"])
    stream.write("field counts: %s\n" % json.dumps(result["field_counts"], sort_keys=True))


def verify_idempotent():
    with tempfile.TemporaryDirectory(prefix="s2-project-idempotent-") as tmp:
        tmp_content = os.path.join(tmp, "content")
        os.makedirs(tmp_content, exist_ok=True)
        tmp_cases = os.path.join(tmp_content, "cases")
        shutil.copytree(os.path.join(REPO_ROOT, CONTENT_CASES_REL), tmp_cases)
        first = dry_run_or_write([tmp_cases], write=True)
        second = dry_run_or_write([tmp_cases], write=True)
        sys.stdout.write("verify-idempotent temp cases: %s\n" % tmp_cases)
        sys.stdout.write("first run refused: %s\n" % ("yes" if first["refused"] else "no"))
        sys.stdout.write("first run pages changed: %d\n" % first["pages_changed"])
        sys.stdout.write("first run field counts: %s\n" % json.dumps(first["field_counts"], sort_keys=True))
        sys.stdout.write("second run refused: %s\n" % ("yes" if second["refused"] else "no"))
        sys.stdout.write("second run pages changed: %d\n" % second["pages_changed"])
        sys.stdout.write("second run field counts: %s\n" % json.dumps(second["field_counts"], sort_keys=True))
        if first["refused"]:
            sys.stdout.write("verify-idempotent result: FAIL (first projection refused)\n")
            return 1
        if second["refused"]:
            sys.stdout.write("verify-idempotent result: FAIL (second projection refused)\n")
            return 1
        if second["pages_changed"] != 0:
            for row in second["page_results"][:10]:
                sys.stdout.write("second-run diff: %s fields=%s\n" % (row["page"], ", ".join(row["fields"][:12])))
            sys.stdout.write("verify-idempotent result: FAIL\n")
            return 1
        sys.stdout.write("verify-idempotent result: PASS\n")
        return 0


def self_test():
    record = {
        "record_id": "Fixture v. Case",
        "status": "under_review",
        "identity": {
            "court": "U.S. Supreme Court",
            "court_level": "scotus",
            "circuit": None,
            "year": 2020,
            "date_decided": "2020-01-02",
            "docket": "19-1",
            "cluster_id": 123,
            "lead_opinion_id": 456,
            "absolute_url": "/opinion/456/fixture-v-case/",
            "expected_citation_found": True,
        },
        "citations": {
            "official": {"cite": "590 U.S. 1"},
            "parallel": [{"cite": "140 S. Ct. 1"}],
            "vendor_neutral": [],
        },
        "treatment": {
            "field_i_validity": "good_law",
            "as_of_content": "2020-01-02",
            "as_of_treatment": "2026-07-06",
            "composite_basis": "principal-holding",
            "composite_basis_ref": "fixture",
            "varies_by_point": False,
            "scope_note": "Fixture note.",
            "point_overrides": [],
        },
        "provenance": {"date_modified": "2026-07-06T00:00:00Z"},
    }
    projected = project_record(record)
    slip_opinion_record = json.loads(json.dumps(record))
    slip_opinion_record["status"] = "slip_opinion"
    slip_opinion_projected = project_record(slip_opinion_record)
    slip_opinion_ok = (
        slip_opinion_projected.get("lake", {}).get("status") == "slip_opinion"
    )
    md = "---\ntitle: Fixture v. Case\ntype: case\ncitation: old\nhomes: []\n---\n# Body\n"
    once = serializer.replace_frontmatter(md, projected)
    twice = serializer.replace_frontmatter(once, projected)
    ok = once == twice and serializer.canonicalize(serializer.managed_subset(serializer.split_frontmatter(once)[0])) == serializer.canonicalize(projected)

    off_cl = load_json(os.path.join(REPO_ROOT, S2_FIXTURES_REL, "project-verified-off-cl.json"))
    off_cl_ok = project_record(off_cl).get("off_cl_links") == off_cl["off_cl_links"]

    def preserved_bytes(text):
        raw = serializer._split_frontmatter_raw(text)
        if raw is None:
            return text
        opener, fm_lines, closer, body = raw
        kept = []
        for key, lines in serializer._frontmatter_segments(fm_lines):
            if key not in serializer.MANAGED_TOP_LEVEL:
                kept.extend(lines)
        return opener + "".join(kept) + closer + body

    fixture_path = os.path.join(REPO_ROOT, S2_FIXTURES_REL, "project-preserve-formatting.md")
    preserve_source = serializer.read_markdown(fixture_path)
    preserve_after = serializer.replace_frontmatter(preserve_source, projected)
    preserve_ok = preserved_bytes(preserve_source) == preserved_bytes(preserve_after)

    # CR-13: date_from_record fails closed (no today() guess) on a record with
    # no/short provenance.date_modified; a valid date passes straight through.
    try:
        date_from_record({"record_id": "no-date", "provenance": {}})
    except ValueError:
        cr13_missing_ok = True
    else:
        cr13_missing_ok = False
    try:
        date_from_record({"record_id": "short-date", "provenance": {"date_modified": "2026"}})
    except ValueError:
        cr13_short_ok = True
    else:
        cr13_short_ok = False
    cr13_ok = cr13_missing_ok and cr13_short_ok and date_from_record(
        {"record_id": "ok", "provenance": {"date_modified": "2026-07-07T12:00:00Z"}}
    ) == "2026-07-07"

    with tempfile.TemporaryDirectory(prefix="s2-project-gate-self-test-") as tmp:
        lake_root = os.path.join(tmp, "lake")
        lake_cases = os.path.join(lake_root, "cases")
        page_root = os.path.join(tmp, "pages")
        os.makedirs(lake_cases, exist_ok=True)
        os.makedirs(page_root, exist_ok=True)

        matched_record = json.loads(json.dumps(record))
        matched_record["record_id"] = "matched-case"
        with open(os.path.join(lake_cases, "matched-case.json"), "w", encoding="utf-8") as f:
            json.dump(matched_record, f)
        with open(os.path.join(lake_cases, "missing-id.json"), "w", encoding="utf-8") as f:
            json.dump({"status": "under_review"}, f)

        good_page_dir = os.path.join(page_root, "good")
        missing_status_dir = os.path.join(page_root, "missing-status")
        unmatched_dir = os.path.join(page_root, "unmatched")
        for directory in (good_page_dir, missing_status_dir, unmatched_dir):
            os.makedirs(directory, exist_ok=True)
        with open(os.path.join(good_page_dir, "matched-case.md"), "w", encoding="utf-8") as f:
            f.write("---\ntype: case\nlake:\n  record_id: matched-case\ntreatment:\n  field_i_validity: unverified\n---\n")
        with open(os.path.join(missing_status_dir, "matched-case.md"), "w", encoding="utf-8") as f:
            f.write("---\ntype: case\nlake:\n  record_id: matched-case\ntreatment:\n  scope_note: missing status fixture\n---\n")
        with open(os.path.join(unmatched_dir, "absent-case.md"), "w", encoding="utf-8") as f:
            f.write("---\ntype: case\nlake:\n  record_id: absent-case\ntreatment:\n  field_i_validity: unverified\n---\n")

        good_result = dry_run_or_write([good_page_dir], lake_root=lake_root)
        missing_status_result = dry_run_or_write([missing_status_dir], lake_root=lake_root)
        unmatched_result = dry_run_or_write([unmatched_dir], lake_root=lake_root)
        write_warning_result = dry_run_or_write([good_page_dir], write=True, lake_root=lake_root)
        load_warning_ok = len(good_result["record_load_warnings"]) == 1 and not good_result["refused"]
        missing_status_ok = (
            missing_status_result["refused"]
            and len(missing_status_result["gate"]["missing_treatment_status"]) == 1
        )
        unmatched_ok = (
            unmatched_result["refused"]
            and unmatched_result["gate"]["unmatched_records"] == [
                (os.path.join(unmatched_dir, "absent-case.md"), "absent-case")
            ]
        )
        write_warning_ok = write_warning_result["refused"] and len(write_warning_result["record_load_warnings"]) == 1

        # CR-14: a batch containing a record that raises on project_record()
        # (here a COA record with no circuit) must be refused up front with
        # projection_errors, and NO page in the batch may be partially written.
        cr14_lake = os.path.join(tmp, "cr14-lake")
        cr14_cases = os.path.join(cr14_lake, "cases")
        cr14_pages = os.path.join(tmp, "cr14-pages")
        os.makedirs(cr14_cases, exist_ok=True)
        os.makedirs(cr14_pages, exist_ok=True)
        good_coa = json.loads(json.dumps(record))
        good_coa["record_id"] = "good-coa"
        good_coa["identity"]["court_level"] = "coa"
        good_coa["identity"]["circuit"] = "ca9"
        bad_coa = json.loads(json.dumps(record))
        bad_coa["record_id"] = "bad-coa"
        bad_coa["identity"]["court_level"] = "coa"
        bad_coa["identity"]["circuit"] = None  # authority_weight raises ValueError
        for rec in (good_coa, bad_coa):
            with open(os.path.join(cr14_cases, rec["record_id"] + ".json"), "w", encoding="utf-8") as f:
                json.dump(rec, f)
        good_coa_page = os.path.join(cr14_pages, "good-coa.md")
        for rid in ("good-coa", "bad-coa"):
            with open(os.path.join(cr14_pages, rid + ".md"), "w", encoding="utf-8") as f:
                f.write("---\ntype: case\nlake:\n  record_id: %s\ntreatment:\n  field_i_validity: unverified\n---\n" % rid)
        good_coa_before = serializer.read_markdown(good_coa_page)
        cr14_dry = dry_run_or_write([cr14_pages], lake_root=cr14_lake)
        cr14_write = dry_run_or_write([cr14_pages], write=True, lake_root=cr14_lake)
        good_coa_after = serializer.read_markdown(good_coa_page)
        cr14_ok = (
            cr14_dry["refused"]
            and len(cr14_dry["projection_errors"]) == 1
            and cr14_dry["projection_errors"][0]["record"].endswith("bad-coa.json")
            and cr14_write["refused"]
            and len(cr14_write["projection_errors"]) == 1
            and good_coa_before == good_coa_after  # good page NOT partially written
        )

    # slip-only single-source projection (S2 A3): a slip-marked record with no
    # reporter cite derives the slip form from citation_with_year, so the mint and
    # the projector agree; an UNMARKED citeless record stays "" (unchanged).
    slip_rec = {
        "record_id": "Slip Fixture",
        "status": "under_review",
        "identity": {"court": "U.S. Supreme Court", "court_level": "scotus", "circuit": None,
                     "year": 2026, "docket": "23-1197"},
        "citations": {"official": None, "parallel": [], "vendor_neutral": [], "all": [],
                      "display": "", "slip_only": True},
        "provenance": {"date_modified": "2026-07-07T00:00:00Z"},
    }
    slip_proj = project_record(slip_rec).get("citation")
    unmarked = json.loads(json.dumps(slip_rec))
    unmarked["citations"]["slip_only"] = False
    unmarked_proj = project_record(unmarked).get("citation")
    slip_ok = (slip_proj == "No. 23-1197, slip op. (U.S. 2026)" and unmarked_proj == "")

    # RULING P4-20(a): authority_weight honors an OPTIONAL non-precedential signal.
    # A coa/district record with identity.precedential_status == "Unpublished" derives
    # the tier-5 A8 label 'Persuasive only — non-precedential'; an ABSENT signal leaves
    # every court-level path byte-identical (regression guard); the guard is scoped to
    # coa/district so a stray scotus flag never demotes 'Binding — SCOTUS'.
    def _weight(level, **ident):
        return authority_weight({"record_id": "prec", "identity": dict(court_level=level, **ident)})
    prec_unpub_coa = _weight("coa", circuit="ca6", precedential_status="Unpublished")
    prec_pub_coa = _weight("coa", circuit="ca6")
    prec_unpub_dist = _weight("district", precedential_status="Unpublished")
    prec_scotus_flag = _weight("scotus", precedential_status="Unpublished")
    prec_ok = (
        prec_unpub_coa == "Persuasive only — non-precedential"
        and prec_pub_coa == "Binding in-circuit — 6th Cir."
        and prec_unpub_dist == "Persuasive only — non-precedential"
        and prec_scotus_flag == "Binding — SCOTUS"
    )

    ok = ok and slip_opinion_ok and off_cl_ok and preserve_ok and load_warning_ok and missing_status_ok and unmatched_ok and write_warning_ok and cr13_ok and cr14_ok and slip_ok and prec_ok
    sys.stderr.write("[self-test] slip_opinion status passthrough -> %s\n"
                     % ("OK" if slip_opinion_ok else "FAIL"))
    sys.stderr.write("[self-test] slip-only projection single-source (S2 A3) -> %s (slip=%r unmarked=%r)\n"
                     % ("OK" if slip_ok else "FAIL", slip_proj, unmarked_proj))
    sys.stderr.write("[self-test] P4-20(a) precedential_status weight derivation -> %s (coa/unpub=%r coa/pub=%r)\n"
                     % ("OK" if prec_ok else "FAIL", prec_unpub_coa, prec_pub_coa))
    sys.stderr.write("[self-test] project idempotence -> %s\n" % ("OK" if once == twice else "FAIL"))
    sys.stderr.write("[self-test] verified_off_cl off_cl_links projection -> %s\n" % ("OK" if off_cl_ok else "FAIL"))
    sys.stderr.write("[self-test] preserved raw frontmatter bytes -> %s\n" % ("OK" if preserve_ok else "FAIL"))
    sys.stderr.write("[self-test] missing record_id load warning -> %s\n" % ("OK" if load_warning_ok else "FAIL"))
    sys.stderr.write("[self-test] missing treatment status gate -> %s\n" % ("OK" if missing_status_ok else "FAIL"))
    sys.stderr.write("[self-test] unmatched case page gate -> %s\n" % ("OK" if unmatched_ok else "FAIL"))
    sys.stderr.write("[self-test] write refused on load warning -> %s\n" % ("OK" if write_warning_ok else "FAIL"))
    sys.stderr.write("[self-test] CR-13 date_from_record fails closed on missing/short date -> %s\n" % ("OK" if cr13_ok else "FAIL"))
    sys.stderr.write("[self-test] CR-14 bad record refuses batch, no partial write -> %s\n" % ("OK" if cr14_ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Optional case markdown paths/globs/directories")
    parser.add_argument("--write", action="store_true", help="Rewrite content frontmatter")
    parser.add_argument("--dry-run", action="store_true", help="Dry-run only (default)")
    parser.add_argument("--summary-json", action="store_true", help="Emit machine-readable summary")
    parser.add_argument("--self-test", action="store_true", help="Run offline projector self-test")
    parser.add_argument("--verify-idempotent", action="store_true", help="Project-write twice in a temp copy of content/cases and require the second run to be clean")
    args = parser.parse_args(argv)
    if args.write and args.dry_run:
        parser.error("--write and --dry-run cannot be combined")
    if args.self_test:
        return self_test()
    if args.verify_idempotent:
        return verify_idempotent()
    result = dry_run_or_write(args.paths or None, write=args.write)
    print_summary(result, sys.stderr)
    if args.summary_json:
        sys.stdout.write(json.dumps(result, sort_keys=True, default=str) + "\n")
    return 2 if result["refused"] or (args.write and result.get("record_load_warnings")) else 0


if __name__ == "__main__":
    sys.exit(main())
