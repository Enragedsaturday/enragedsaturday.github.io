#!/usr/bin/env python3
"""
S8H-A independent verification script (read-only). NOT the lint suite —
a from-scratch cross-check of NUM-03's two halves:

  (1) mid-line ^pin-N visible-carat risk: for every content/**/*.md line
      (frontmatter skipped, fenced code blocks skipped, HTML comments
      blanked), mask [[wikilinks]] and `inline code` to non-word filler,
      then find any ^token whose match does NOT end at end-of-line. This
      independently re-derives what LINT-9 measures, using a separately
      written mask/scan so it is not just re-running the same code.

  (2) pin wikilink resolution: every [[Target#^pin-N]] (or embed
      ![[Target#^pin-N]]) is resolved to a content/**/*.md file (by page
      stem / alias-free basename match, case-insensitive) and then checked
      that the target file contains a block-anchor DEFINITION for that
      exact ^pin-N token (a line that, after stripping, ENDS with
      ^pin-N — the Obsidian block-ref rule).

Prints JSON to stdout: {"midline": [...], "resolved": N, "broken": [...]}
"""
import glob
import json
import os
import re
import sys

REPO_ROOT = "/Users/johngalt/Projects/cssi-quartz"
CONTENT = os.path.join(REPO_ROOT, "content")

WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\[\]]+?)\]\]")
EMBED_RE = re.compile(r"!\[\[([^\[\]]+?)\]\]")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FENCE_RE = re.compile(r"^\s*```")
ANCHOR_TOKEN_RE = re.compile(r"(?<!\[)\^[A-Za-z0-9][A-Za-z0-9-]*")
PIN_ANCHOR_RE = re.compile(r"\^pin-[A-Za-z0-9]+$")
PIPE_SPLIT_RE = re.compile(r"\\?\|")


def split_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            nl = text.find("\n", end + 1)
            body_start = nl + 1 if nl != -1 else len(text)
            fm = text[:body_start]
            return fm, text[body_start:], fm.count("\n")
    return "", text, 0


def fenced_lines(lines):
    fenced = set()
    infence = False
    for i, ln in enumerate(lines):
        if FENCE_RE.match(ln):
            fenced.add(i)
            infence = not infence
            continue
        if infence:
            fenced.add(i)
    return fenced


def mask_line(line):
    def fillcode(m):
        return "#" * (m.end() - m.start())
    line = INLINE_CODE_RE.sub(fillcode, line)
    line = WIKILINK_RE.sub(fillcode, line)
    line = EMBED_RE.sub(fillcode, line)
    return line


def find_midline_carats():
    hits = []
    for path in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        _, body, start = split_frontmatter(text)
        body = HTML_COMMENT_RE.sub(lambda m: "".join("\n" if c == "\n" else " " for c in m.group(0)), body)
        lines = body.split("\n")
        fenced = fenced_lines(lines)
        for i, line in enumerate(lines):
            if i in fenced:
                continue
            masked = mask_line(line).rstrip()
            if not masked:
                continue
            for m in ANCHOR_TOKEN_RE.finditer(masked):
                if m.end() != len(masked):
                    hits.append({
                        "file": os.path.relpath(path, REPO_ROOT),
                        "line": start + i + 1,
                        "token": m.group(0),
                        "context": masked.strip()[:140],
                    })
    return hits


# --------------------------------------------------------------------------
# pin wikilink resolution
# --------------------------------------------------------------------------

def build_page_index():
    """basename (no ext, lowercased) -> list of relpaths; also full relpath
    (no ext, lowercased) -> relpath, for path-qualified targets."""
    by_base = {}
    by_relstem = {}
    for path in glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True):
        rel = os.path.relpath(path, CONTENT)
        stem = rel[:-3] if rel.endswith(".md") else rel
        base = os.path.basename(stem).lower()
        by_base.setdefault(base, []).append(path)
        by_relstem[stem.lower()] = path
    return by_base, by_relstem


def resolve_page(target, by_base, by_relstem):
    t = target.strip()
    if t.lower() in by_relstem:
        return by_relstem[t.lower()]
    base = os.path.basename(t).lower()
    cands = by_base.get(base)
    if cands and len(cands) >= 1:
        # prefer exact relstem suffix match if multiple
        for c in cands:
            rel = os.path.relpath(c, CONTENT)
            stem = rel[:-3] if rel.endswith(".md") else rel
            if stem.lower().endswith(t.lower()):
                return c
        return cands[0]
    return None


def target_has_pin_anchor(path, anchor):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    _, body, _ = split_frontmatter(text)
    for line in body.split("\n"):
        s = line.rstrip()
        if s.endswith(anchor):
            # confirm it's a real anchor token match at end (word boundary before ^)
            m = ANCHOR_TOKEN_RE.search(s)
            if m and m.end() == len(s) and m.group(0) == anchor:
                return True
    return False


def check_pin_wikilinks():
    by_base, by_relstem = build_page_index()
    resolved = 0
    broken = []
    total_pin_refs = 0
    for path in sorted(glob.glob(os.path.join(CONTENT, "**", "*.md"), recursive=True)):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        _, body, start = split_frontmatter(text)
        lines_starts = [0]
        idx = body.find("\n")
        while idx != -1:
            lines_starts.append(idx + 1)
            idx = body.find("\n", idx + 1)

        def lineno(off):
            import bisect
            return start + bisect.bisect_right(lines_starts, off)

        for regex in (WIKILINK_RE, EMBED_RE):
            for m in regex.finditer(body):
                raw_inner = m.group(1).strip()
                # strip a `|display text` pipe (or table-escaped `\|`) before
                # looking for the anchor, same convention as LINT-5.
                inner = PIPE_SPLIT_RE.split(raw_inner, 1)[0].strip()
                if "#^pin-" not in inner:
                    continue
                total_pin_refs += 1
                page, _, anchor = inner.partition("#")
                page = page.strip()
                anchor = anchor.strip()
                if page == "":
                    target_path = path
                else:
                    target_path = resolve_page(page, by_base, by_relstem)
                ln = lineno(m.start())
                if target_path is None:
                    broken.append({
                        "file": os.path.relpath(path, REPO_ROOT),
                        "line": ln,
                        "ref": inner,
                        "reason": "target page does not resolve",
                    })
                    continue
                if not target_has_pin_anchor(target_path, anchor):
                    broken.append({
                        "file": os.path.relpath(path, REPO_ROOT),
                        "line": ln,
                        "ref": inner,
                        "target": os.path.relpath(target_path, REPO_ROOT),
                        "reason": "anchor '%s' not defined on target page" % anchor,
                    })
                    continue
                resolved += 1
    return total_pin_refs, resolved, broken


if __name__ == "__main__":
    midline = find_midline_carats()
    total, resolved, broken = check_pin_wikilinks()
    print(json.dumps({
        "midline_carat_count": len(midline),
        "midline_hits": midline,
        "pin_wikilink_total": total,
        "pin_wikilink_resolved": resolved,
        "pin_wikilink_broken_count": len(broken),
        "pin_wikilink_broken": broken,
    }, indent=2, ensure_ascii=False))
