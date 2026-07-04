#!/usr/bin/env python3
"""
LINT-24 — URL & slug stability.  S3 · R13 / A1 (alias LINT-S3-urls; S9 R8 roster
row 24).  FAIL-CLOSED.  Realizes A1's lint mechanics EXACTLY.

The restructure de-numbers every slug and moves pages, so every pre-O2 URL
changes. R13 requires that the complete pre-move URL inventory still resolves
(directly or via an alias-redirect) on the rebuilt site, and that zero old-path
references remain in source. Two checks:

(A) INVENTORY RESOLUTION.
    * `_overhaul2/url-inventory.json` must EXIST and be NON-EMPTY (A1: "the lint
      FAILS if the artifact is absent or empty") => HIGH.
    * Every inventory path must resolve against the CURRENT BUILD OUTPUT
      (`public/`). If `public/` is missing or has no `public/index.html`, the
      build output is absent/stale: emit ONE MEDIUM ("build output absent — run
      `npx quartz build` first") and SKIP resolution (exit 0 with the MEDIUM
      recorded — never a false pass, never a false HIGH). CI runs this row right
      after the build step, so the guard is CI-safe.
    * Normalization (A1, applied to BOTH sides): path-only (drop query/fragment);
      percent-decode; lowercase; strip ONE trailing slash; `/x/index` == `/x`.
      An unresolved real-page path => HIGH.

(B) OLD-PATH SWEEP (R13(c)).
    * Zero references to any of the 12 retired numbered top-level folders remain
      in source — checked in path-based WIKILINKS and in `homes:` / `related:`
      frontmatter values. `aliases:` values are DELIBERATELY EXEMPT: R13(a)
      stores the old full paths there ON PURPOSE, so the alias-redirect emitter
      serves every pre-O2 URL. Each surviving old-path reference => HIGH.

Not scoped by `paths` for check (A); check (B) honors `paths` (default: all
content).

SELF-TEST (S1 A3): `python3 lint24_urls.py --self-test` over the `fixtures/
lint-24-*` fixtures (inventories, a fixture build output, a no-index build dir,
and old-path pass/fail pages).

Usage:
  python3 lint24_urls.py
  python3 lint24_urls.py --self-test
"""

import glob
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-24"

INVENTORY_REL = os.path.join("_overhaul2", "url-inventory.json")
PUBLIC_REL = "public"

# The 12 retired numbered top-level category folders (pre-O2 tree). Any of these
# appearing as a path SEGMENT in a wikilink or in a homes:/related: value is a
# surviving old-path reference (R13(c)). Sourced from the pre-move content tree.
RETIRED_PREFIXES = (
    "1-foundations-history",
    "2-legal-system-research",
    "3-what-is-a-search",
    "4-what-is-a-seizure",
    "5-levels-of-suspicion",
    "6-warrant-requirement",
    "7-exceptions-warrant",
    "8-exclusionary-rule-remedies",
    "9-confessions-interrogation",
    "10-use-of-force-liability",
    "11-adjacent-doctrines",
    "12-instructor-craft-study",
)
# a retired prefix appearing as a whole path segment: (start|/)PREFIX(end|/)
_RETIRED_SEG_RE = re.compile(
    r"(?:^|/)(" + "|".join(re.escape(p) for p in RETIRED_PREFIXES) + r")(?:/|$)")


# ---------------------------------------------------------------------------
# (A) inventory resolution
# ---------------------------------------------------------------------------

def normalize_url(p):
    """A1 normalization: path-only; percent-decode; lowercase; strip one trailing
    slash; /x/index == /x. Root stays '/'."""
    p = p.split("#", 1)[0].split("?", 1)[0]
    p = urllib.parse.unquote(p).lower()
    if not p.startswith("/"):
        p = "/" + p
    if len(p) > 1 and p.endswith("/"):
        p = p[:-1]
    if p.endswith("/index"):
        p = p[: -len("/index")] or "/"
    if p == "/index":
        p = "/"
    return p or "/"


def emitted_routes(public_root):
    """Every route the build emits, normalized. A folder's index.html emits both
    the folder route and the /.../index route; alias-redirect stubs appear as
    ordinary .html files and are included naturally. 404.html -> /404."""
    routes = set()
    for h in glob.glob(os.path.join(public_root, "**", "*.html"), recursive=True):
        rel = os.path.relpath(h, public_root).replace(os.sep, "/")
        rel = rel[:-5]  # drop ".html"
        base = os.path.basename(rel)
        if base == "index":
            d = os.path.dirname(rel)
            routes.add(normalize_url("/" + d))
            routes.add(normalize_url("/" + rel))
        else:
            routes.add(normalize_url("/" + rel))
    return routes


def check_inventory(inventory_path, public_root):
    """A1 check (A). Returns violations. Fail-closed on missing/empty inventory;
    build-output-absent yields ONE MEDIUM and a skip (exit 0)."""
    if not os.path.isfile(inventory_path):
        return [c.make_violation(
            LINT, inventory_path, 1, c.HIGH,
            "url-inventory missing: %s not found — the pre-move URL inventory is a "
            "required R13/A1 artifact (fail-closed) [R13/A1]"
            % c.relpath(inventory_path))]
    try:
        doc = json.load(open(inventory_path, encoding="utf-8"))
    except (OSError, ValueError) as e:
        return [c.make_violation(
            LINT, inventory_path, 1, c.HIGH,
            "url-inventory not parseable (%s) — fail-closed [R13/A1]" % e)]
    paths = doc.get("paths") if isinstance(doc, dict) else None
    if not isinstance(paths, list) or not paths:
        return [c.make_violation(
            LINT, inventory_path, 1, c.HIGH,
            "url-inventory is empty (no `paths`) — the lint FAILS on an empty "
            "artifact (fail-closed) [R13/A1]")]

    index_html = os.path.join(public_root, "index.html")
    if not os.path.isdir(public_root) or not os.path.isfile(index_html):
        return [c.make_violation(
            LINT, public_root, 1, c.MEDIUM,
            "build output absent — run `npx quartz build` first; skipping URL "
            "resolution (no false pass). %d inventory paths unchecked [R13/A1]"
            % len(paths))]

    routes = emitted_routes(public_root)
    out = []
    for p in paths:
        if not isinstance(p, str):
            continue
        if normalize_url(p) not in routes:
            out.append(c.make_violation(
                LINT, inventory_path, 1, c.HIGH,
                "inventory path %r (normalized %r) resolves to no emitted page or "
                "alias redirect in the build output — a pre-O2 URL that now 404s "
                "(fail-closed) [R13/A1]" % (p, normalize_url(p))))
    return out


# ---------------------------------------------------------------------------
# (B) old-path sweep (R13(c))
# ---------------------------------------------------------------------------

def _retired_in(value):
    """Return the retired prefix found as a path segment in `value`, or None."""
    if not isinstance(value, str):
        return None
    m = _RETIRED_SEG_RE.search(value)
    return m.group(1) if m else None


def check_oldpaths(path):
    """R13(c): flag retired-prefix references in path-based wikilinks and in
    homes:/related: frontmatter. aliases: values are exempt (R13(a) old-path
    aliases are the redirect mechanism)."""
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)

    # frontmatter homes: / related:
    for key in ("homes", "related"):
        val = fm.get(key)
        vals = val if isinstance(val, list) else ([val] if isinstance(val, str) else [])
        for v in vals:
            hit = _retired_in(v)
            if hit:
                out.append(c.make_violation(
                    LINT, path, start, c.HIGH,
                    "old-path reference in frontmatter `%s:` value %r (retired "
                    "folder %r) — the R13(c) link sweep rewrites these to new "
                    "paths (aliases: are exempt) [R13(c)]" % (key, v, hit)))

    # body wikilinks (path-based targets)
    body_lines = body.split("\n")
    for i, line in enumerate(body_lines):
        for m in c.WIKILINK_RE.finditer(line):
            target = m.group(1).split("|")[0].split("#")[0].strip()
            hit = _retired_in(target)
            if hit:
                out.append(c.make_violation(
                    LINT, path, start + i, c.HIGH,
                    "old-path wikilink [[%s]] (retired folder %r) — rewrite to the "
                    "new path; zero old-path references remain in source [R13(c)]"
                    % (m.group(1), hit)))
    return out


def run(paths=None):
    out = []
    # (A) inventory resolution against the current build output
    out.extend(check_inventory(os.path.join(c.REPO_ROOT, INVENTORY_REL),
                               os.path.join(c.REPO_ROOT, PUBLIC_REL)))
    # (B) old-path sweep over source
    for path in c.iter_markdown_files(paths):
        out.extend(check_oldpaths(path))
    return out


# --------------------------------------------------------------------------
# self-test — inventories + fixture build output + old-path pages
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    inv_pass = os.path.join(fixdir, "lint-24-inventory-pass.json")
    inv_fail = os.path.join(fixdir, "lint-24-inventory-fail.json")
    pub = os.path.join(fixdir, "lint-24-public")
    pub_noindex = os.path.join(fixdir, "lint-24-public-noindex")
    op_pass = os.path.join(fixdir, "lint-24-oldpath-pass.md")
    op_fail = os.path.join(fixdir, "lint-24-oldpath-fail.md")
    for req in (inv_pass, inv_fail, op_pass, op_fail):
        if not os.path.isfile(req):
            sys.stderr.write("[self-test] FAIL: missing fixture %s\n" % req)
            return 1
    ok = True

    def check(desc, fn, expect):
        nonlocal ok
        viols = fn()
        n_high = sum(1 for v in viols if v["severity"] == c.HIGH)
        n_med = sum(1 for v in viols if v["severity"] == c.MEDIUM)
        if expect == "pass":
            passed = n_high == 0 and n_med == 0
        elif expect == "medium":
            passed = n_high == 0 and n_med >= 1
        else:  # high
            passed = n_high >= 1
        ok = ok and passed
        sys.stderr.write("[self-test] %-34s expect=%-6s -> %s (%d high, %d med)\n" % (
            desc, expect, "OK" if passed else "MISMATCH", n_high, n_med))
        if not passed:
            for v in viols:
                sys.stderr.write("             [%s] %s\n" % (v["severity"], v["message"]))

    # (A) inventory resolution
    check("inventory resolves (build present)",
          lambda: check_inventory(inv_pass, pub), "pass")
    check("inventory has unresolved path",
          lambda: check_inventory(inv_fail, pub), "high")
    check("build output absent -> MEDIUM+skip",
          lambda: check_inventory(inv_pass, pub_noindex), "medium")
    check("missing inventory -> HIGH",
          lambda: check_inventory(os.path.join(fixdir, "lint-24-nope.json"), pub), "high")
    # empty inventory -> HIGH
    empty_inv = os.path.join(fixdir, "lint-24-inventory-empty.json")
    if os.path.isfile(empty_inv):
        check("empty inventory -> HIGH",
              lambda: check_inventory(empty_inv, pub), "high")

    # (B) old-path sweep
    check("old-path in aliases only (pass)",
          lambda: check_oldpaths(op_pass), "pass")
    check("old-path in wikilink/homes (fail)",
          lambda: check_oldpaths(op_fail), "high")

    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
