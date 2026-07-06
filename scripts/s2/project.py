#!/usr/bin/env python3
"""S2 lake-to-case-frontmatter projector.

Dry-run is the default. Use --write for the guarded content rewrite.
"""

import argparse
import datetime as dt
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


def load_records(lake_root=None):
    lake_root = lake_root or os.path.join(REPO_ROOT, LAKE_REL)
    records = {}
    record_paths = {}
    for path in sorted(glob.glob(os.path.join(lake_root, "cases", "*.json"))):
        record = load_json(path)
        rid = record.get("record_id")
        if rid:
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
    return dt.date.today().isoformat()


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


def authority_weight(record):
    identity = record.get("identity", {})
    level = identity.get("court_level")
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


def a13_gate(paths=None, migration_path=None):
    mappings = load_migration(migration_path)
    mapped = set(mappings.keys())
    counts = Counter()
    unmapped = []
    review = []
    new_form = 0
    missing = []
    for path in case_page_paths(paths):
        text = serializer.read_markdown(path)
        fm, _body, _start = serializer.split_frontmatter(text)
        if fm.get("type") != "case" or serializer.is_draft_page(fm):
            continue
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
        "mapping_keys": sorted(mapped),
        "ok_to_project": not unmapped,
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
    gate = a13_gate(paths)
    if not gate["ok_to_project"]:
        return {
            "gate": gate,
            "refused": True,
            "pages_changed": 0,
            "field_counts": {},
            "page_results": [],
        }

    records, record_paths = load_records(lake_root)
    results = []
    field_counts = Counter()
    pages_changed = 0
    skipped_review = set(gate["review"])
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
    }


def print_summary(result, stream=None):
    stream = stream or sys.stdout
    gate = result["gate"]
    stream.write("A13 gate: %s\n" % ("PASS" if gate["ok_to_project"] else "FAIL"))
    stream.write("legacy counts: %s\n" % json.dumps(gate["legacy_counts"], sort_keys=True))
    stream.write("new-form pages: %d\n" % gate["new_form_pages"])
    stream.write("review-staged pages: %d\n" % len(gate["review"]))
    stream.write("missing treatment status/new field: %d\n" % len(gate["missing_treatment_status"]))
    if gate["unmapped"]:
        stream.write("unmapped legacy values:\n")
        for path, value in gate["unmapped"]:
            stream.write("  %s: %s\n" % (os.path.relpath(path, REPO_ROOT), value))
    if result["refused"]:
        stream.write("projection refused by A13 gate\n")
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

    ok = ok and off_cl_ok and preserve_ok
    sys.stderr.write("[self-test] project idempotence -> %s\n" % ("OK" if once == twice else "FAIL"))
    sys.stderr.write("[self-test] verified_off_cl off_cl_links projection -> %s\n" % ("OK" if off_cl_ok else "FAIL"))
    sys.stderr.write("[self-test] preserved raw frontmatter bytes -> %s\n" % ("OK" if preserve_ok else "FAIL"))
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
    if args.self_test:
        return self_test()
    if args.verify_idempotent:
        return verify_idempotent()
    result = dry_run_or_write(args.paths or None, write=args.write)
    print_summary(result, sys.stderr)
    if args.summary_json:
        sys.stdout.write(json.dumps(result, sort_keys=True, default=str) + "\n")
    return 2 if result["refused"] else 0


if __name__ == "__main__":
    sys.exit(main())
