#!/usr/bin/env python3
"""Shared S2 frontmatter serializer and canonical value helpers.

Projector and lints import this module so managed frontmatter is parsed,
serialized, and compared through one value-level path.
"""

import json
import os
import re
import sys
from collections import OrderedDict


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
LINT_DIR = os.path.join(REPO_ROOT, "scripts", "lint")
if LINT_DIR not in sys.path:
    sys.path.insert(0, LINT_DIR)

import _common as lint_common  # noqa: E402


MANAGED_TOP_LEVEL = (
    "citation",
    "parallel_cite",
    "neutral_cite",
    "court",
    "court_level",
    "circuit",
    "year",
    "date_decided",
    "docket",
    "authority_weight",
    "treatment",
    "courtlistener",
    "off_cl_links",
    "lake",
)

PRESERVED_TOP_LEVEL = (
    "title",
    "type",
    "homes",
    "related",
    "aliases",
    "tags",
    "holding",
    "body",
)

_INT_RE = re.compile(r"^-?(?:0|[1-9][0-9]*)$")
_SAFE_PLAIN_RE = re.compile(r"^[A-Za-z0-9_./@+-][A-Za-z0-9_ ./@+-]*$")
_TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_.-]*)\s*:")


def split_frontmatter(text):
    return lint_common.split_frontmatter(text)


def read_markdown(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def canonicalize(value):
    """Return a normalized parsed value suitable for deep equality.

    The repo's stdlib YAML subset parser preserves most scalars as strings.
    This canonicalizer narrows obvious JSON-like scalars so `year: 1986`,
    `identity_checked: true`, and `opinion_id: null` compare by value rather
    than by the raw spelling in frontmatter.
    """
    if isinstance(value, OrderedDict):
        value = dict(value)
    if isinstance(value, dict):
        return {str(k): canonicalize(v) for k, v in sorted(value.items(), key=lambda item: str(item[0]))}
    if isinstance(value, list):
        return [canonicalize(v) for v in value]
    if isinstance(value, str):
        s = value.strip()
        low = s.lower()
        if low in ("true", "false"):
            return low == "true"
        if low in ("null", "none", "~"):
            return None
        if _INT_RE.match(s):
            try:
                return int(s)
            except ValueError:
                return value
        return value
    return value


def canonical_json(value):
    return json.dumps(canonicalize(value), sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def managed_subset(frontmatter):
    return OrderedDict((key, frontmatter[key]) for key in MANAGED_TOP_LEVEL if key in frontmatter)


def is_draft_page(frontmatter):
    if str(frontmatter.get("status", "")).strip().lower() == "draft":
        return True
    lake = frontmatter.get("lake")
    if isinstance(lake, dict) and str(lake.get("status", "")).strip().lower() == "draft":
        return True
    return False


def _needs_quotes(value):
    if value == "":
        return True
    if value.strip() != value:
        return True
    if value.lower() in {"true", "false", "null", "none", "~"}:
        return True
    if value[0] in "-?:,[]{}#&*!|>'\"%@`":
        return True
    if ":" in value or "#" in value or "[" in value or "]" in value or "{" in value or "}" in value:
        return True
    if "\n" in value:
        return True
    if not _SAFE_PLAIN_RE.match(value):
        return True
    return False


def yaml_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int) and not isinstance(value, bool):
        return str(value)
    if isinstance(value, float):
        return json.dumps(value, ensure_ascii=False)
    text = str(value)
    if _needs_quotes(text):
        return json.dumps(text, ensure_ascii=False)
    return text


def _dump_yaml_lines(value, indent=0):
    pad = " " * indent
    if isinstance(value, dict):
        lines = []
        for key, item in value.items():
            if isinstance(item, (dict, list)):
                if isinstance(item, list) and not item:
                    lines.append("%s%s: []" % (pad, key))
                elif isinstance(item, dict) and not item:
                    lines.append("%s%s: {}" % (pad, key))
                else:
                    lines.append("%s%s:" % (pad, key))
                    lines.extend(_dump_yaml_lines(item, indent + 2))
            else:
                lines.append("%s%s: %s" % (pad, key, yaml_scalar(item)))
        return lines
    if isinstance(value, list):
        if not value:
            return [pad + "[]"]
        lines = []
        for item in value:
            if isinstance(item, dict):
                if not item:
                    lines.append(pad + "- {}")
                    continue
                first = True
                for key, val in item.items():
                    if first:
                        if isinstance(val, (dict, list)):
                            lines.append("%s- %s:" % (pad, key))
                            lines.extend(_dump_yaml_lines(val, indent + 4))
                        else:
                            lines.append("%s- %s: %s" % (pad, key, yaml_scalar(val)))
                        first = False
                    else:
                        if isinstance(val, (dict, list)):
                            lines.append("%s  %s:" % (pad, key))
                            lines.extend(_dump_yaml_lines(val, indent + 4))
                        else:
                            lines.append("%s  %s: %s" % (pad, key, yaml_scalar(val)))
            elif isinstance(item, list):
                lines.append(pad + "-")
                lines.extend(_dump_yaml_lines(item, indent + 2))
            else:
                lines.append("%s- %s" % (pad, yaml_scalar(item)))
        return lines
    return [pad + yaml_scalar(value)]


def dumps_frontmatter(frontmatter):
    lines = ["---"]
    lines.extend(dumps_frontmatter_body(frontmatter))
    lines.append("---")
    return "\n".join(lines) + "\n"


def dumps_frontmatter_body(frontmatter):
    lines = []
    for key, value in frontmatter.items():
        if isinstance(value, (dict, list)):
            if isinstance(value, list) and not value:
                lines.append("%s: []" % key)
            elif isinstance(value, dict) and not value:
                # CR-15: a bare "key:" reparses as null, not {}; emit "key: {}"
                # to mirror the empty-list case and _dump_yaml_lines' empty-dict
                # handling, so canonicalize({}) does not report phantom drift.
                lines.append("%s: {}" % key)
            else:
                lines.append("%s:" % key)
                lines.extend(_dump_yaml_lines(value, 2))
        else:
            lines.append("%s: %s" % (key, yaml_scalar(value)))
    return lines


def compose_projected_frontmatter(existing_fm, projection):
    """Merge projection into frontmatter without touching preserved fields."""
    out = OrderedDict()
    for key in ("title", "type"):
        if key in existing_fm:
            out[key] = existing_fm[key]
    for key in MANAGED_TOP_LEVEL:
        if key in projection:
            out[key] = projection[key]
    for key, value in existing_fm.items():
        if key in out or key in MANAGED_TOP_LEVEL:
            continue
        out[key] = value
    return out


def replace_frontmatter(markdown_text, projection):
    """Replace projector-managed frontmatter blocks without reserializing preserved keys."""
    raw = _split_frontmatter_raw(markdown_text)
    if raw is None:
        return dumps_frontmatter(projection) + markdown_text
    opener, fm_lines, closer, body = raw
    newline = "\r\n" if opener.endswith("\r\n") else "\n"
    rendered = {
        key: [line + newline for line in dumps_frontmatter_body(OrderedDict([(key, value)]))]
        for key, value in projection.items()
    }
    seen_managed = set()
    out_lines = []
    for key, lines in _frontmatter_segments(fm_lines):
        if key in MANAGED_TOP_LEVEL:
            if key not in seen_managed and key in rendered:
                out_lines.extend(rendered[key])
            seen_managed.add(key)
            continue
        out_lines.extend(lines)
    for key in MANAGED_TOP_LEVEL:
        if key in rendered and key not in seen_managed:
            out_lines.extend(rendered[key])
    return opener + "".join(out_lines) + closer + body


def _split_frontmatter_raw(text):
    lines = text.splitlines(True)
    if not lines or lines[0].strip() != "---":
        return None
    end = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end = idx
            break
    if end is None:
        return None
    return lines[0], lines[1:end], lines[end], "".join(lines[end + 1:])


def _top_level_key(line):
    if line.startswith((" ", "\t")):
        return None
    match = _TOP_LEVEL_KEY_RE.match(line.rstrip("\r\n"))
    return match.group(1) if match else None


def _frontmatter_segments(lines):
    segments = []
    idx = 0
    while idx < len(lines):
        key = _top_level_key(lines[idx])
        if key is None:
            segments.append((None, [lines[idx]]))
            idx += 1
            continue
        block = [lines[idx]]
        idx += 1
        while idx < len(lines) and lines[idx].startswith((" ", "\t")):
            block.append(lines[idx])
            idx += 1
        segments.append((key, block))
    return segments


def diff_paths(left, right, prefix=""):
    left = canonicalize(left)
    right = canonicalize(right)
    if left == right:
        return []
    if isinstance(left, dict) and isinstance(right, dict):
        paths = []
        for key in sorted(set(left) | set(right)):
            child = "%s.%s" % (prefix, key) if prefix else str(key)
            if key not in left or key not in right:
                paths.append(child)
            else:
                paths.extend(diff_paths(left[key], right[key], child))
        return paths
    if isinstance(left, list) and isinstance(right, list):
        paths = []
        for idx in range(max(len(left), len(right))):
            child = "%s[%d]" % (prefix, idx)
            if idx >= len(left) or idx >= len(right):
                paths.append(child)
            else:
                paths.extend(diff_paths(left[idx], right[idx], child))
        return paths
    return [prefix or "$"]


def self_test():
    """CR-15: an empty managed dict must serialize as `key: {}` and round-trip
    back to an empty mapping (not null/string) so it does not phantom-drift
    against a projected empty dict. Mirrors the existing empty-list handling."""
    fm = OrderedDict([("title", "T"), ("treatment", {}), ("lake", {}), ("off_cl_links", [])])
    text = dumps_frontmatter(fm)
    assert "treatment: {}" in text, text
    assert "lake: {}" in text, text
    assert "off_cl_links: []" in text, text
    parsed, _body, _start = split_frontmatter(text)
    assert parsed["treatment"] == {}, repr(parsed["treatment"])
    assert parsed["lake"] == {}, repr(parsed["lake"])
    assert parsed["off_cl_links"] == [], repr(parsed["off_cl_links"])
    # no phantom drift vs a projection carrying real empty containers
    actual = managed_subset(parsed)
    assert diff_paths(actual, OrderedDict([("treatment", {}), ("lake", {}), ("off_cl_links", [])])) == []
    # replace_frontmatter path renders empty dicts the same way
    doc = "---\ntitle: T\ntreatment: {}\n---\nbody\n"
    out = replace_frontmatter(doc, OrderedDict([("treatment", {})]))
    assert "treatment: {}" in out, out
    # the parser (not canonicalize) narrows the empty flow map to a real dict,
    # matching how the empty flow list is already narrowed to a real list
    assert split_frontmatter("---\nk: {}\n---\n")[0]["k"] == {}
    assert split_frontmatter("---\nk: []\n---\n")[0]["k"] == []

    # Serializer<->reader round-trip for managed strings carrying a literal
    # double-quote. yaml_scalar emits the json.dumps escaped form (\" for a quote,
    # \\ for a backslash); _common._unquote / _strip_inline_comment reverse it
    # exactly. Without that, an embedded-quote scope_note (the Arizona v. Roberson
    # class) can never converge -> a LINT-12 false positive and a project.py
    # idempotence failure. The probes cover: a plain embedded quote, an embedded
    # quote followed by a '#' (which must NOT read as an inline comment), and an
    # embedded backslash.
    for probe in (
        'flagged audit_needed ("R15 treatment audit required"); none accepted.',
        'a literal " quote, then a # hash, then a back\\slash tail',
        'plain value with no special characters',
    ):
        rt = OrderedDict([("treatment", OrderedDict([("scope_note", probe)]))])
        rt_parsed, _rb, _rs = split_frontmatter(dumps_frontmatter(rt))
        assert rt_parsed["treatment"]["scope_note"] == probe, (
            probe, rt_parsed["treatment"]["scope_note"])
    # And the value-level idempotence the projector relies on (managed_subset of a
    # round-tripped doc must diff-clean against the source mapping).
    rt_doc = OrderedDict([("treatment", OrderedDict([
        ("scope_note", 'edge flagged audit_needed ("R15 treatment audit required")')]))])
    assert diff_paths(managed_subset(split_frontmatter(dumps_frontmatter(rt_doc))[0]), rt_doc) == []

    print("serializer self-test passed")


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        self_test()
