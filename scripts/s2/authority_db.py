#!/usr/bin/env python3
"""Build and verify the S2 derived authority SQLite database."""

import argparse
import datetime as dt
import glob
import hashlib
import json
import os
import sqlite3
import sys
import tempfile


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
LAKE_DIR = os.path.join(REPO_ROOT, "_overhaul2", "lake")
CASES_DIR = os.path.join(LAKE_DIR, "cases")
MANIFEST_PATH = os.path.join(LAKE_DIR, "_manifest.json")
DETERMINISM_EXCLUDED_META_KEYS = {"built_at"}


def pool_root():
    from scripts.s2 import ingest as s2_ingest
    return os.environ.get("CSSI_LAKE_ROOT", s2_ingest.DEFAULT_CSSI_LAKE_ROOT)


def db_path(root=None):
    return os.path.join(root or pool_root(), "db", "authority.sqlite")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def hash_path_pairs(pairs):
    h = hashlib.sha256()
    for rel, digest in sorted(pairs):
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(digest.encode("ascii"))
        h.update(b"\n")
    return h.hexdigest()


def compute_lake_hash(lake_dir=LAKE_DIR):
    pairs = []
    for path in sorted(glob.glob(os.path.join(lake_dir, "cases", "*.json"))):
        pairs.append((os.path.relpath(path, lake_dir).replace(os.sep, "/"), sha256_file(path)))
    manifest = os.path.join(lake_dir, "_manifest.json")
    if os.path.exists(manifest):
        pairs.append(("_manifest.json", sha256_file(manifest)))
    return hash_path_pairs(pairs)


def slugify(value):
    import re
    value = str(value or "").strip().lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "case"


def canonical_record_json(record):
    return json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def load_case_records(cases_dir=CASES_DIR):
    out = []
    for path in sorted(glob.glob(os.path.join(cases_dir, "*.json"))):
        record = load_json(path)
        out.append((path, record))
    return out


def read_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def load_progeny_cache(root=None):
    root = root or pool_root()
    dirs = [
        os.path.join(root, "progeny"),
        os.path.join(root, "cache", "progeny"),
    ]
    by_record = {}
    read_paths = []
    for directory in dirs:
        if not os.path.isdir(directory):
            continue
        for path in sorted(glob.glob(os.path.join(directory, "*.jsonl"))):
            rows = read_jsonl(path)
            if not rows:
                continue
            read_paths.append(path)
            meta = rows[0] if isinstance(rows[0], dict) and rows[0].get("_meta") == "progeny-cache" else {}
            record_id = meta.get("record_id") or os.path.splitext(os.path.basename(path))[0]
            by_record[record_id] = {"path": path, "meta": meta, "rows": rows[1:] if meta else rows}
            by_record.setdefault(slugify(record_id), by_record[record_id])
    return by_record, read_paths


def compute_cache_hash(read_paths, root=None):
    root = root or pool_root()
    pairs = []
    for path in sorted(set(read_paths)):
        try:
            rel = os.path.relpath(path, root).replace(os.sep, "/")
        except ValueError:
            rel = path
        pairs.append((rel, sha256_file(path)))
    return hash_path_pairs(pairs)


def init_schema(conn):
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;
        DROP TABLE IF EXISTS meta;
        DROP TABLE IF EXISTS cases;
        DROP TABLE IF EXISTS citations;
        DROP TABLE IF EXISTS siblings;
        DROP TABLE IF EXISTS progeny;
        DROP TABLE IF EXISTS edges;
        DROP TABLE IF EXISTS intra_edges;
        DROP TABLE IF EXISTS coverage;
        DROP TABLE IF EXISTS overrides;
        DROP TABLE IF EXISTS provenance;

        CREATE TABLE meta (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );

        CREATE TABLE cases (
          record_id TEXT PRIMARY KEY,
          record_path TEXT NOT NULL,
          json_sha256 TEXT NOT NULL,
          record_json TEXT NOT NULL,
          cluster_id INTEGER,
          lead_opinion_id INTEGER,
          court TEXT,
          court_level TEXT,
          circuit TEXT,
          year INTEGER,
          date_decided TEXT,
          field_i_validity TEXT,
          as_of_content TEXT,
          as_of_treatment TEXT,
          authority_weight TEXT,
          status TEXT NOT NULL,
          stub INTEGER NOT NULL DEFAULT 0
        );

        CREATE TABLE citations (
          record_id TEXT NOT NULL,
          cite_kind TEXT NOT NULL,
          sort_order INTEGER NOT NULL,
          cite TEXT NOT NULL,
          type TEXT,
          source TEXT,
          reporter TEXT,
          volume TEXT,
          page TEXT,
          selected_official INTEGER NOT NULL DEFAULT 0,
          FOREIGN KEY(record_id) REFERENCES cases(record_id)
        );

        CREATE TABLE siblings (
          record_id TEXT NOT NULL,
          sort_order INTEGER NOT NULL,
          opinion_id INTEGER NOT NULL,
          PRIMARY KEY(record_id, opinion_id),
          FOREIGN KEY(record_id) REFERENCES cases(record_id)
        );

        CREATE TABLE progeny (
          record_id TEXT PRIMARY KEY,
          complete_query TEXT,
          indexed_citing_opinions INTEGER,
          count_source TEXT,
          per_sibling_json TEXT NOT NULL,
          citation_count INTEGER,
          cache_path TEXT,
          rows_cached INTEGER NOT NULL DEFAULT 0,
          enumeration TEXT,
          cursor TEXT,
          cache_rows_json TEXT NOT NULL,
          FOREIGN KEY(record_id) REFERENCES cases(record_id)
        );

        CREATE TABLE edges (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          cited_case TEXT NOT NULL,
          citing_case_name TEXT,
          cluster_id INTEGER,
          cite TEXT,
          field_ii TEXT,
          field_iii TEXT,
          point TEXT,
          proposed INTEGER,
          journal_ref TEXT,
          FOREIGN KEY(cited_case) REFERENCES cases(record_id)
        );

        CREATE TABLE intra_edges (
          source_record_id TEXT NOT NULL,
          target_record_id TEXT NOT NULL,
          source_opinion_id INTEGER,
          cited_id INTEGER,
          source TEXT NOT NULL,
          PRIMARY KEY(source_record_id, target_record_id, source_opinion_id, cited_id),
          FOREIGN KEY(source_record_id) REFERENCES cases(record_id),
          FOREIGN KEY(target_record_id) REFERENCES cases(record_id)
        );

        CREATE TABLE coverage (
          record_id TEXT PRIMARY KEY,
          manifest_source TEXT,
          page_path TEXT,
          page_exists INTEGER NOT NULL,
          record_exists INTEGER NOT NULL,
          status TEXT,
          stub INTEGER NOT NULL DEFAULT 0,
          slug TEXT,
          cluster_id INTEGER,
          expected_citation TEXT
        );

        CREATE TABLE overrides (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          record_id TEXT NOT NULL,
          point TEXT,
          point_label TEXT,
          field_i_validity TEXT,
          as_of_treatment TEXT,
          s3_binding_status TEXT,
          controlling_name TEXT,
          controlling_cluster_id INTEGER,
          controlling_cite TEXT,
          field_ii TEXT,
          scope_note TEXT,
          FOREIGN KEY(record_id) REFERENCES cases(record_id)
        );

        CREATE TABLE provenance (
          record_id TEXT NOT NULL,
          field TEXT NOT NULL,
          src TEXT,
          at TEXT,
          verifier TEXT,
          warnings_json TEXT,
          cl_source TEXT,
          cl_api TEXT,
          built_by TEXT,
          build_run TEXT,
          date_created TEXT,
          date_modified TEXT,
          PRIMARY KEY(record_id, field),
          FOREIGN KEY(record_id) REFERENCES cases(record_id)
        );
        """
    )


def citation_string(citation):
    if not citation:
        return ""
    if isinstance(citation, str):
        return citation
    if citation.get("cite"):
        return str(citation["cite"])
    parts = [citation.get("volume"), citation.get("reporter"), citation.get("page")]
    return " ".join(str(p).strip() for p in parts if p not in (None, ""))


def authority_weight(record):
    from scripts.s2.project import authority_weight as project_weight
    return project_weight(record)


def opinion_id_from_cache_row(row):
    opinions = row.get("opinions") if isinstance(row, dict) else None
    if isinstance(opinions, list) and opinions:
        first = opinions[0]
        if isinstance(first, dict):
            return first.get("id")
    return None


def cited_ids_from_cache_row(row):
    out = []
    opinions = row.get("opinions") if isinstance(row, dict) else None
    if isinstance(opinions, list):
        for opinion in opinions:
            if isinstance(opinion, dict):
                out.extend(x for x in opinion.get("cites") or [] if isinstance(x, int))
    return out


def build(db_out=None, root=None):
    root = root or pool_root()
    db_out = db_out or db_path(root)
    os.makedirs(os.path.dirname(db_out), exist_ok=True)
    records = load_case_records()
    progeny_cache, cache_paths = load_progeny_cache(root)
    lake_hash = compute_lake_hash()
    cache_hash = compute_cache_hash(cache_paths, root)
    built_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    fd, tmp_path = tempfile.mkstemp(prefix="authority.", suffix=".sqlite", dir=os.path.dirname(db_out))
    os.close(fd)
    try:
        conn = sqlite3.connect(tmp_path)
        init_schema(conn)
        conn.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("schema", "s2.authority.sqlite.v1"))
        conn.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("lake_hash", lake_hash))
        conn.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("cache_hash", cache_hash))
        conn.execute("INSERT INTO meta(key, value) VALUES (?, ?)", ("built_at", built_at))

        id_to_record = {}
        for path, record in records:
            rid = record["record_id"]
            ident = record.get("identity", {})
            treatment = record.get("treatment", {})
            record_json = canonical_record_json(record)
            rel = os.path.relpath(path, REPO_ROOT).replace(os.sep, "/")
            conn.execute(
                """
                INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    rid,
                    rel,
                    hashlib.sha256(record_json.encode("utf-8")).hexdigest(),
                    record_json,
                    ident.get("cluster_id"),
                    ident.get("lead_opinion_id"),
                    ident.get("court"),
                    ident.get("court_level"),
                    ident.get("circuit"),
                    ident.get("year"),
                    ident.get("date_decided"),
                    treatment.get("field_i_validity"),
                    treatment.get("as_of_content"),
                    treatment.get("as_of_treatment"),
                    authority_weight(record),
                    record.get("status"),
                    1 if record.get("stub") else 0,
                ),
            )
            for key in ("cluster_id", "lead_opinion_id"):
                value = ident.get(key)
                if isinstance(value, int):
                    id_to_record[value] = rid
            for opinion_id in ident.get("sibling_ids") or []:
                if isinstance(opinion_id, int):
                    id_to_record[opinion_id] = rid

        for _path, record in records:
            rid = record["record_id"]
            citations = record.get("citations", {})
            groups = [
                ("official", [citations.get("official")] if citations.get("official") else []),
                ("parallel", citations.get("parallel") or []),
                ("vendor_neutral", citations.get("vendor_neutral") or []),
                ("all", citations.get("all") or []),
            ]
            for kind, items in groups:
                for idx, cite in enumerate(items):
                    if not cite:
                        continue
                    conn.execute(
                        "INSERT INTO citations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            rid,
                            kind,
                            idx,
                            citation_string(cite),
                            str(cite.get("type")) if isinstance(cite, dict) and cite.get("type") is not None else None,
                            cite.get("source") if isinstance(cite, dict) else None,
                            cite.get("reporter") if isinstance(cite, dict) else None,
                            str(cite.get("volume")) if isinstance(cite, dict) and cite.get("volume") is not None else None,
                            str(cite.get("page")) if isinstance(cite, dict) and cite.get("page") is not None else None,
                            1 if isinstance(cite, dict) and cite.get("selected_official") else 0,
                        ),
                    )
            for idx, opinion_id in enumerate(record.get("identity", {}).get("sibling_ids") or []):
                conn.execute("INSERT OR IGNORE INTO siblings VALUES (?, ?, ?)", (rid, idx, opinion_id))

            prog = record.get("progeny", {})
            cache = progeny_cache.get(rid) or progeny_cache.get(slugify(rid)) or {"path": None, "rows": [], "meta": {}}
            cache_rows = cache.get("rows") or []
            conn.execute(
                "INSERT INTO progeny VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    rid,
                    prog.get("complete_query"),
                    prog.get("indexed_citing_opinions"),
                    prog.get("count_source"),
                    json.dumps(prog.get("per_sibling") or [], sort_keys=True),
                    prog.get("citation_count"),
                    cache.get("path") or prog.get("cache_path"),
                    len(cache_rows) or prog.get("rows_cached") or 0,
                    prog.get("enumeration"),
                    prog.get("cursor"),
                    json.dumps(cache_rows, sort_keys=True, ensure_ascii=False, separators=(",", ":")),
                ),
            )

            for edge in record.get("treatment", {}).get("edges") or []:
                citing = edge.get("citing_case") or {}
                cite = citing.get("cite")
                if isinstance(cite, list):
                    cite = "; ".join(str(x) for x in cite)
                conn.execute(
                    """
                    INSERT INTO edges(cited_case, citing_case_name, cluster_id, cite, field_ii, field_iii, point, proposed, journal_ref)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        rid,
                        citing.get("name"),
                        citing.get("cluster_id"),
                        cite,
                        edge.get("field_ii") or citing.get("field_ii"),
                        edge.get("field_iii"),
                        edge.get("point"),
                        1 if edge.get("proposed", True) else 0,
                        edge.get("journal_ref"),
                    ),
                )

            for override in record.get("treatment", {}).get("point_overrides") or []:
                by = override.get("by")
                controllers = by if isinstance(by, list) else [{"name": by, "cluster_id": None, "cite": override.get("by_cite"), "field_ii": override.get("field_ii")}]
                for controller in controllers:
                    conn.execute(
                        """
                        INSERT INTO overrides(record_id, point, point_label, field_i_validity, as_of_treatment, s3_binding_status,
                                              controlling_name, controlling_cluster_id, controlling_cite, field_ii, scope_note)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            rid,
                            override.get("point"),
                            override.get("point_label"),
                            override.get("field_i_validity"),
                            override.get("as_of_treatment"),
                            override.get("s3_binding_status"),
                            controller.get("name") if isinstance(controller, dict) else str(controller),
                            controller.get("cluster_id") if isinstance(controller, dict) else None,
                            controller.get("cite") if isinstance(controller, dict) else None,
                            controller.get("field_ii") if isinstance(controller, dict) else override.get("field_ii"),
                            override.get("scope_note"),
                        ),
                    )

            prov = record.get("provenance", {})
            conn.execute(
                "INSERT INTO provenance VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    rid,
                    "__record__",
                    None,
                    None,
                    None,
                    json.dumps(prov.get("warnings") or [], ensure_ascii=False),
                    prov.get("cl_source"),
                    prov.get("cl_api"),
                    prov.get("built_by"),
                    prov.get("build_run"),
                    prov.get("date_created"),
                    prov.get("date_modified"),
                ),
            )
            for field, stamp in (prov.get("field_provenance") or {}).items():
                conn.execute(
                    "INSERT INTO provenance VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        rid,
                        field,
                        stamp.get("src") if isinstance(stamp, dict) else None,
                        stamp.get("at") if isinstance(stamp, dict) else None,
                        stamp.get("verifier") if isinstance(stamp, dict) else None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                        None,
                    ),
                )

            for outbound in prog.get("outbound_opinion_edges") or []:
                target = id_to_record.get(outbound.get("cited_id"))
                if target:
                    conn.execute(
                        "INSERT OR IGNORE INTO intra_edges VALUES (?, ?, ?, ?, ?)",
                        (rid, target, outbound.get("source_opinion_id"), outbound.get("cited_id"), outbound.get("source") or "record.progeny.outbound_opinion_edges"),
                    )

        for cache in progeny_cache.values():
            for row in cache.get("rows") or []:
                source = id_to_record.get(row.get("cluster_id")) or id_to_record.get(opinion_id_from_cache_row(row))
                if not source:
                    continue
                for cited_id in cited_ids_from_cache_row(row):
                    target = id_to_record.get(cited_id)
                    if target:
                        conn.execute(
                            "INSERT OR IGNORE INTO intra_edges VALUES (?, ?, ?, ?, ?)",
                            (source, target, opinion_id_from_cache_row(row), cited_id, "cache.progeny.opinions[].cites[]"),
                        )

        manifest = load_json(MANIFEST_PATH)
        manifest_records = manifest.get("records") or []
        from scripts.s2 import serializer
        case_paths = {}
        for p in glob.glob(os.path.join(REPO_ROOT, "content", "cases", "*.md")):
            with open(p, encoding="utf-8") as f:
                fm, _body, _start = serializer.split_frontmatter(f.read())
            if fm.get("type") == "case":
                case_paths[os.path.splitext(os.path.basename(p))[0]] = p
        record_ids = {record["record_id"] for _path, record in records}
        for row in manifest_records:
            rid = row.get("record_id")
            if not rid:
                continue
            page_path = row.get("page_path")
            page_exists = bool(page_path and os.path.exists(os.path.join(REPO_ROOT, page_path)))
            conn.execute(
                "INSERT OR REPLACE INTO coverage VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    rid,
                    row.get("source"),
                    page_path,
                    1 if page_exists else 0,
                    1 if rid in record_ids else 0,
                    row.get("status"),
                    1 if row.get("stub") else 0,
                    row.get("slug"),
                    row.get("cluster_id"),
                    row.get("expected_citation"),
                ),
            )
        for stem, path in sorted(case_paths.items()):
            if stem not in record_ids:
                conn.execute(
                    "INSERT OR REPLACE INTO coverage VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (stem, "content/cases", os.path.relpath(path, REPO_ROOT).replace(os.sep, "/"), 1, 0, None, 0, slugify(stem), None, None),
                )

        conn.commit()
        conn.execute("VACUUM")
        conn.close()
        os.replace(tmp_path, db_out)
    except Exception:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    return db_out


def row_counts(path=None):
    path = path or db_path()
    conn = sqlite3.connect(path)
    tables = ["cases", "citations", "siblings", "progeny", "edges", "intra_edges", "coverage", "overrides", "provenance", "meta"]
    out = {}
    for table in tables:
        out[table] = conn.execute("SELECT count(*) FROM %s" % table).fetchone()[0]
    conn.close()
    return out


def read_meta(conn):
    return dict(conn.execute("SELECT key, value FROM meta"))


def comparable_table_content(path):
    conn = sqlite3.connect(path)
    tables = ["cases", "citations", "siblings", "progeny", "edges", "intra_edges", "coverage", "overrides", "provenance", "meta"]
    out = {}
    for table in tables:
        if table == "meta":
            rows = conn.execute(
                "SELECT key, value FROM meta WHERE key NOT IN (%s)" %
                ",".join("?" for _ in DETERMINISM_EXCLUDED_META_KEYS),
                tuple(sorted(DETERMINISM_EXCLUDED_META_KEYS)),
            ).fetchall()
        else:
            rows = conn.execute("SELECT * FROM %s" % table).fetchall()
        out[table] = sorted([tuple(row) for row in rows], key=repr)
    conn.close()
    return out


def assert_fresh(path=None, root=None):
    root = root or pool_root()
    path = path or db_path(root)
    conn = sqlite3.connect(path)
    meta = read_meta(conn)
    conn.close()
    progeny_cache, cache_paths = load_progeny_cache(root)
    del progeny_cache
    expected_lake = compute_lake_hash()
    expected_cache = compute_cache_hash(cache_paths, root)
    errors = []
    if meta.get("lake_hash") != expected_lake:
        errors.append("lake_hash mismatch: db=%s current=%s" % (meta.get("lake_hash"), expected_lake))
    if meta.get("cache_hash") != expected_cache:
        errors.append("cache_hash mismatch: db=%s current=%s" % (meta.get("cache_hash"), expected_cache))
    if errors:
        raise RuntimeError("; ".join(errors))
    return True


def verify_roundtrip(path=None):
    path = path or db_path()
    conn = sqlite3.connect(path)
    rows = conn.execute("SELECT record_id, record_path, record_json FROM cases ORDER BY record_id").fetchall()
    conn.close()
    if not rows:
        raise RuntimeError("cases.record_json roundtrip failed: cases table has zero rows")
    errors = []
    for rid, rel, record_json in rows:
        source = load_json(os.path.join(REPO_ROOT, rel))
        if json.loads(record_json) != source:
            errors.append(rid)
    if errors:
        raise RuntimeError("cases.record_json roundtrip failed for %d records: %s" % (len(errors), ", ".join(errors[:10])))
    return True


def self_test():
    lake_hash = compute_lake_hash()
    cache, paths = load_progeny_cache(pool_root())
    cache_hash = compute_cache_hash(paths, pool_root())
    hash_ok = bool(lake_hash) and bool(cache_hash) and isinstance(cache, dict)
    with tempfile.TemporaryDirectory(prefix="s2-authority-db-self-test-") as tmp:
        root = os.path.join(tmp, "pool")
        first = build(os.path.join(root, "db", "authority-one.sqlite"), root=root)
        second = build(os.path.join(root, "db", "authority-two.sqlite"), root=root)
        deterministic = comparable_table_content(first) == comparable_table_content(second)
        empty_db = os.path.join(root, "db", "empty.sqlite")
        conn = sqlite3.connect(empty_db)
        init_schema(conn)
        conn.commit()
        conn.close()
        try:
            verify_roundtrip(empty_db)
        except RuntimeError as exc:
            zero_row_ok = "zero rows" in str(exc)
        else:
            zero_row_ok = False
    ok = hash_ok and deterministic and zero_row_ok
    sys.stderr.write("[self-test] hash inputs -> %s (cache files=%d)\n" % ("OK" if hash_ok else "FAIL", len(paths)))
    sys.stderr.write("[self-test] two rebuilds deterministic except meta.built_at -> %s\n" % ("OK" if deterministic else "FAIL"))
    sys.stderr.write("[self-test] empty cases roundtrip fails closed -> %s\n" % ("OK" if zero_row_ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="Run offline authority DB self-test")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("rebuild")
    sub.add_parser("counts")
    sub.add_parser("assert-fresh")
    sub.add_parser("verify-roundtrip")
    sub.add_parser("self-test")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.cmd == "rebuild":
        path = build()
        sys.stderr.write("rebuilt %s\n" % path)
        sys.stdout.write(json.dumps(row_counts(path), sort_keys=True) + "\n")
        return 0
    if args.cmd == "counts":
        sys.stdout.write(json.dumps(row_counts(), sort_keys=True) + "\n")
        return 0
    if args.cmd == "assert-fresh":
        assert_fresh()
        sys.stderr.write("authority.sqlite freshness OK\n")
        return 0
    if args.cmd == "verify-roundtrip":
        verify_roundtrip()
        sys.stderr.write("cases.record_json roundtrip OK\n")
        return 0
    if args.cmd == "self-test":
        return self_test()
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
