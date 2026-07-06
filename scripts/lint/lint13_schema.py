#!/usr/bin/env python3
"""
LINT-13 - S2 authority-record schema (alias LINT-S2-schema). Fail-closed.

Validates authority records by interpreting the committed draft-07 subset used
by `_overhaul2/lake/_schema.json`. Cross-file invariants that JSON Schema cannot
express, such as unique record IDs and filename/record ID agreement, remain in
this lint.
"""

import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.parse
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-13"
SCHEMA_PATH = os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "_schema.json")
SUPPORTED_SCHEMA_KEYWORDS = {
    "$id",
    "$ref",
    "$schema",
    "additionalProperties",
    "allOf",
    "anyOf",
    "const",
    "contains",
    "default",
    "definitions",
    "description",
    "else",
    "enum",
    "format",
    "if",
    "items",
    "minItems",
    "minLength",
    "minimum",
    "not",
    "pattern",
    "properties",
    "required",
    "then",
    "title",
    "type",
    "uniqueItems",
}


def v(path, msg):
    return c.make_violation(LINT, path, 1, c.HIGH, msg)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def schema_keywords(schema):
    found = set()

    def walk(node):
        if isinstance(node, list):
            for item in node:
                walk(item)
            return
        if not isinstance(node, dict):
            return
        for key, value in node.items():
            found.add(key)
            if key in ("properties", "definitions"):
                if isinstance(value, dict):
                    for child in value.values():
                        walk(child)
                continue
            if key in ("allOf", "anyOf"):
                walk(value)
                continue
            if key in ("items", "contains", "not", "if", "then", "else"):
                walk(value)
                continue
            if key == "additionalProperties" and isinstance(value, dict):
                walk(value)

    walk(schema)
    return found


def unsupported_schema_keywords(schema):
    return sorted(schema_keywords(schema) - SUPPORTED_SCHEMA_KEYWORDS)


def json_kind(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def json_equal(left, right):
    if json_kind(left) != json_kind(right):
        return False
    return left == right


def schema_path_join(base, child):
    return "%s/%s" % (base.rstrip("/"), child)


class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def resolve_ref(self, ref):
        if not ref.startswith("#/"):
            raise ValueError("unsupported $ref %r" % ref)
        node = self.schema
        for raw in ref[2:].split("/"):
            part = raw.replace("~1", "/").replace("~0", "~")
            if not isinstance(node, dict) or part not in node:
                raise ValueError("unresolved $ref %r" % ref)
            node = node[part]
        return node

    def validate(self, schema, instance, instance_path="$", schema_path="#"):
        if not isinstance(schema, dict):
            return ["%s: schema at %s must be an object" % (instance_path, schema_path)]

        errors = []
        if "$ref" in schema:
            try:
                errors.extend(self.validate(self.resolve_ref(schema["$ref"]), instance, instance_path, schema["$ref"]))
            except ValueError as exc:
                errors.append("%s: %s" % (instance_path, exc))
            schema = {k: val for k, val in schema.items() if k != "$ref"}
            if not schema:
                return errors

        for idx, sub in enumerate(schema.get("allOf") or []):
            errors.extend(self.validate(sub, instance, instance_path, schema_path_join(schema_path, "allOf/%d" % idx)))

        if "anyOf" in schema:
            if not any(self.is_valid(sub, instance, instance_path, schema_path_join(schema_path, "anyOf/%d" % idx))
                       for idx, sub in enumerate(schema["anyOf"])):
                errors.append("%s: does not match any schema in anyOf at %s" % (instance_path, schema_path))

        if "if" in schema:
            branch = "then" if self.is_valid(schema["if"], instance, instance_path, schema_path_join(schema_path, "if")) else "else"
            if branch in schema:
                errors.extend(self.validate(schema[branch], instance, instance_path, schema_path_join(schema_path, branch)))

        if "not" in schema and self.is_valid(schema["not"], instance, instance_path, schema_path_join(schema_path, "not")):
            errors.append("%s: matches forbidden schema at %s/not" % (instance_path, schema_path))

        if "type" in schema and not self.type_matches(instance, schema["type"]):
            errors.append("%s: expected type %r, got %s" % (instance_path, schema["type"], json_kind(instance)))

        if "const" in schema and not json_equal(instance, schema["const"]):
            errors.append("%s: expected const %r" % (instance_path, schema["const"]))

        if "enum" in schema and not any(json_equal(instance, item) for item in schema["enum"]):
            errors.append("%s: value %r is not in enum %r" % (instance_path, instance, schema["enum"]))

        if isinstance(instance, str):
            if "pattern" in schema and re.search(schema["pattern"], instance) is None:
                errors.append("%s: string does not match pattern %r" % (instance_path, schema["pattern"]))
            if "minLength" in schema and len(instance) < schema["minLength"]:
                errors.append("%s: length %d is less than minLength %d" % (instance_path, len(instance), schema["minLength"]))
            if "format" in schema and not self.format_matches(instance, schema["format"]):
                errors.append("%s: string %r does not match format %s" % (instance_path, instance, schema["format"]))

        if isinstance(instance, (int, float)) and not isinstance(instance, bool) and "minimum" in schema:
            if instance < schema["minimum"]:
                errors.append("%s: value %r is less than minimum %r" % (instance_path, instance, schema["minimum"]))

        if isinstance(instance, dict):
            required = schema.get("required") or []
            for key in required:
                if key not in instance:
                    errors.append("%s: missing required key %r" % (instance_path, key))
            properties = schema.get("properties") or {}
            for key, sub in properties.items():
                if key in instance:
                    errors.extend(self.validate(sub, instance[key], "%s.%s" % (instance_path, key), schema_path_join(schema_path, "properties/%s" % key)))
            additional = schema.get("additionalProperties", True)
            if additional is False:
                extra = sorted(set(instance) - set(properties))
                for key in extra:
                    errors.append("%s: additional property %r is not allowed" % (instance_path, key))
            elif isinstance(additional, dict):
                for key in sorted(set(instance) - set(properties)):
                    errors.extend(self.validate(additional, instance[key], "%s.%s" % (instance_path, key), schema_path_join(schema_path, "additionalProperties")))

        if isinstance(instance, list):
            if "minItems" in schema and len(instance) < schema["minItems"]:
                errors.append("%s: item count %d is less than minItems %d" % (instance_path, len(instance), schema["minItems"]))
            if schema.get("uniqueItems") is True:
                seen = set()
                for idx, item in enumerate(instance):
                    key = json.dumps(item, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                    if key in seen:
                        errors.append("%s[%d]: duplicate item violates uniqueItems" % (instance_path, idx))
                        break
                    seen.add(key)
            if "items" in schema:
                for idx, item in enumerate(instance):
                    errors.extend(self.validate(schema["items"], item, "%s[%d]" % (instance_path, idx), schema_path_join(schema_path, "items")))
            if "contains" in schema and not any(self.is_valid(schema["contains"], item, "%s[%d]" % (instance_path, idx), schema_path_join(schema_path, "contains"))
                                                for idx, item in enumerate(instance)):
                errors.append("%s: no array item matches contains at %s/contains" % (instance_path, schema_path))

        return errors

    def is_valid(self, schema, instance, instance_path="$", schema_path="#"):
        return not self.validate(schema, instance, instance_path, schema_path)

    @staticmethod
    def type_matches(instance, expected):
        choices = expected if isinstance(expected, list) else [expected]
        actual = json_kind(instance)
        for choice in choices:
            if choice == "number" and actual in ("integer", "number"):
                return True
            if choice == actual:
                return True
        return False

    @staticmethod
    def format_matches(value, fmt):
        if fmt == "date":
            if re.match(r"^\d{4}-\d{2}-\d{2}$", value) is None:
                return False
            try:
                dt.date.fromisoformat(value)
                return True
            except ValueError:
                return False
        if fmt == "date-time":
            try:
                dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
                return True
            except ValueError:
                return False
        if fmt == "uri":
            parsed = urllib.parse.urlparse(value)
            return bool(parsed.scheme and (parsed.netloc or parsed.scheme not in ("http", "https")))
        return True


def validate_record(path, record, schema=None):
    schema = schema or load_json(SCHEMA_PATH)
    validator = SchemaValidator(schema)
    return [v(path, err) for err in validator.validate(schema, record)]


def run(paths=None):  # noqa: ARG001
    out = []
    try:
        schema = load_json(SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        return [v(SCHEMA_PATH, "_schema.json must parse as JSON: %s" % exc)]
    unsupported = unsupported_schema_keywords(schema)
    if unsupported:
        return [v(SCHEMA_PATH, "_schema.json uses unsupported JSON-Schema keyword(s): %s" % ", ".join(unsupported))]

    case_paths = sorted(glob.glob(os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases", "*.json")))
    ids = []
    for path in case_paths:
        try:
            record = load_json(path)
        except Exception as exc:  # noqa: BLE001
            out.append(v(path, "record JSON parse failed: %s" % exc))
            continue
        ids.append(record.get("record_id") if isinstance(record, dict) else None)
        out.extend(validate_record(path, record, schema))
        if isinstance(record, dict) and os.path.basename(os.path.dirname(path)) == "cases" and record.get("record_id"):
            stem = os.path.splitext(os.path.basename(path))[0]
            if stem != record.get("record_id"):
                out.append(v(path, "filename stem %r must equal record_id %r" % (stem, record.get("record_id"))))

    for rid, count in Counter(ids).items():
        if rid and count > 1:
            out.append(v(os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "cases"), "duplicate record_id %r across lake/cases" % rid))

    manifest_path = os.path.join(c.REPO_ROOT, "_overhaul2", "lake", "_manifest.json")
    try:
        manifest = load_json(manifest_path)
        manifest_ids = [row.get("record_id") for row in manifest.get("records") or [] if isinstance(row, dict)]
        for rid, count in Counter(manifest_ids).items():
            if rid and count > 1:
                out.append(v(manifest_path, "duplicate record_id %r in _manifest.json" % rid))
    except Exception as exc:  # noqa: BLE001
        out.append(v(manifest_path, "_manifest.json must parse as JSON: %s" % exc))

    for page in glob.glob(os.path.join(c.REPO_ROOT, "content", "cases", "*.md")):
        stem = os.path.splitext(os.path.basename(page))[0]
        if "--" in stem:
            out.append(v(page, "content/cases page stem %r uses reserved A6 stub namespace '--'" % stem))
    return out


def self_test():
    try:
        schema = load_json(SCHEMA_PATH)
    except Exception as exc:  # noqa: BLE001
        sys.stderr.write("[self-test] FAIL: _schema.json parse failed: %s\n" % exc)
        return 1
    unsupported = unsupported_schema_keywords(schema)
    coverage_ok = not unsupported
    sys.stderr.write("[self-test] live schema keyword coverage -> %s (%d keywords)\n" % (
        "OK" if coverage_ok else "FAIL", len(schema_keywords(schema))))
    if unsupported:
        sys.stderr.write("[self-test] unsupported keyword(s): %s\n" % ", ".join(unsupported))

    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-13-record-*.json")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-13-record-*.json fixtures\n")
        return 1
    ok = coverage_ok
    for path in files:
        name = os.path.basename(path)
        expect = "pass" if name.endswith("-pass.json") else "fail" if name.endswith("-fail.json") else None
        if expect is None:
            continue
        record = load_json(path)
        violations = validate_record(path, record, schema)
        passed = (len(violations) == 0) if expect == "pass" else (len(violations) > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-40s expect=%-4s -> %s (%d viol)\n" % (
            name, expect, "OK" if passed else "MISMATCH", len(violations)))
        if not passed:
            for violation in violations[:5]:
                sys.stderr.write("             %s\n" % violation["message"])
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
