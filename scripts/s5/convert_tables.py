#!/usr/bin/env python3
"""
S5 · convert_tables.py — the mechanical per-page entry-model converter (S5 §5.2).

S7 runs this per-page during doctrine production; prose judgment stays human/S7.
This tool NEVER edits voice or prose — it only reshapes the mechanical scaffolding
so the S5 entry-model standards (R6/R7, R10, R11, R12, R13) hold. Stdlib only.

It applies, IN THIS ORDER, idempotently, to each page given:

  (a) TABLE SCHEMAS (R6/R7/R13) — rewrite every Case-column table header to the
      sanctioned exact set and STRIP the weight / treatment / date / year columns
      (cells never author data — the injection renders it):
        Key cases      | Case | Holding | Opinion |
        Related        | Case | Relevance here | Primary home | Opinion |
        Case Index     | Case | Primary home | Opinion |
      Case cells pass through (format *[[Case Name]]*, <cite> (<year>) is preserved
      where already present; cites are NEVER invented). Opinion-link anchor text is
      normalized to the one sanctioned token `opinion` (TEACH-13). Pipe splitting is
      bracket-aware ([[A|B]] display pipes are not cell boundaries).

  (b) FRONTIER SECTION (R11) — rename `## Recent developments` ->
      `## Lower-court developments` and MOVE it directly above the case tables
      (i.e. directly under The Brief) when the ordering differs.

  (c) SOURCES (R12) — convert em-dash-list Sources bullets to the bracketed form
        - [*Case Name*, <cite> (<year>)](<url>)
      with trailing info (pinpoints, treatment notes) as plain text after the link.
      Only mechanical rows (a clean italic case-name + cite + single URL) are
      rewritten; ambiguous rows are LEFT and reported for human judgment.

  (d) PITFALLS (R10) — normalize an alternate bulleted pitfalls lead-in to the
      `**Common pitfalls.**` bold-lead when mechanically safe (a bold-only lead
      line whose keyword names pitfalls, immediately followed by a bullet list).
      Inline-enumerated paragraphs and standalone `## Pitfalls` H2s are reported,
      never rewritten (non-mechanical — S7's judgment).

Flags:
  --dry-run           (DEFAULT) report the per-page diff summary; write NOTHING.
  --apply             write the transformed files back in place.
  --report-json PATH  write the structured per-page report (S7 consumes this).

Per-page report records BOTH what changed (`actions`) and what was left for human
judgment (`deferred`). Exit code is 0 on success (a report is not a failure).

Usage:
  python3 convert_tables.py [--dry-run|--apply] [--report-json out.json] PAGE [PAGE...]
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# scripts/s5/convert_tables.py -> repo root is two levels up
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
# reuse the lint corpus helpers (stdlib-only; shared frontmatter/heading parsing)
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "lint"))
import _common as c  # noqa: E402


# ---------------------------------------------------------------------------
# raw frontmatter split (preserve the frontmatter block byte-for-byte on write)
# ---------------------------------------------------------------------------

def split_raw(text):
    """Return (prefix_lines, body_lines). prefix_lines is the frontmatter block
    INCLUDING the closing '---' fence (verbatim); body_lines is everything after.
    Joining prefix + body with '\\n' reproduces the file exactly."""
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[: i + 1], lines[i + 1:]
    return [], lines


# ---------------------------------------------------------------------------
# table conversion (bracket-aware GFM parsing lives in _common, shared w/ LINT-16)
# ---------------------------------------------------------------------------

def normalize_opinion_cell(cell):
    """Rewrite every markdown link's anchor text in an opinion cell to `opinion`
    (TEACH-13). Non-link text is preserved."""
    def repl(m):
        return "[opinion](%s)" % m.group(2)
    if not cell.strip():
        return ""
    return c.MDLINK_URL_RE.sub(repl, cell).strip()


def convert_tables(body_lines, report):
    """Pass (a): rewrite every sanctioned Case-column table to its schema, dropping
    weight/treatment/date/year columns and normalizing opinion anchors. Returns the
    new body_lines. Tables without a Case column (incl. the R5 point-status table)
    are untouched."""
    # map header-line-index -> (new_rows, action|None, deferred|None)
    plans = {}
    for hidx, header_cells, rows in c.iter_tables(body_lines):
        kinds = [c.classify_case_header(h) for h in header_cells]
        schema = c.classify_case_table(kinds)
        end = (rows[-1] + 1) if rows else (hidx + 2)
        if schema is None:
            if "case" in kinds:
                plans[hidx] = (None, None, {
                    "pass": "tables",
                    "reason": "unrecognized-case-table",
                    "detail": "Case-column table headers %s do not map to a "
                              "sanctioned schema (need holding, or home[+relevance])"
                              % header_cells,
                    "line": hidx + 1,
                }, end)
            continue

        headers, order = c.CASE_TABLE_SCHEMAS[schema]
        col_of = {}
        for idx, k in enumerate(kinds):
            col_of.setdefault(k, idx)  # first column of each role
        dropped = sorted({k for k in kinds if k in ("weight", "treatment", "year")})
        missing = [r for r in order if r not in col_of]

        new_rows = ["| " + " | ".join(headers) + " |",
                    "|" + "|".join(["---"] * len(headers)) + "|"]
        for ridx in rows:
            src = c.split_table_row(body_lines[ridx])
            cells = []
            for role in order:
                val = src[col_of[role]] if (role in col_of and col_of[role] < len(src)) else ""
                if role == "opinion":
                    val = normalize_opinion_cell(val)
                cells.append(val)
            new_rows.append("| " + " | ".join(cells) + " |")

        original = body_lines[hidx:end]
        action = None
        if new_rows != original:
            action = {
                "pass": "tables", "type": "schema-rewrite", "schema": schema,
                "line": hidx + 1, "dropped_columns": dropped, "rows": len(rows),
                "note": ("no Opinion source column — emitted empty Opinion cells"
                         if "opinion" in missing else ""),
            }
        plans[hidx] = (new_rows, action, None, end)

    if not plans:
        return body_lines

    out = []
    i, n = 0, len(body_lines)
    while i < n:
        if i in plans:
            new_rows, action, deferred, end = plans[i]
            if deferred is not None:
                report["deferred"].append(deferred)
            if new_rows is None:
                out.extend(body_lines[i:end])
            else:
                if action is not None:
                    report["actions"].append(action)
                out.extend(new_rows)
            i = end
            continue
        out.append(body_lines[i])
        i += 1
    return out


# ---------------------------------------------------------------------------
# section helpers (H2 blocks)
# ---------------------------------------------------------------------------

def h2_sections(body_lines):
    """Return H2 sections as dicts {title, slug, start, end} (line indexes;
    end exclusive = next H2 or EOF), skipping fenced regions."""
    return c.sections(body_lines)


CASE_TABLE_TITLES = ("key cases", "related cases across doctrines", "case index")


# ---------------------------------------------------------------------------
# (b) frontier section — rename + move above the case tables
# ---------------------------------------------------------------------------

def convert_frontier(body_lines, report):
    secs = h2_sections(body_lines)
    frontier = None
    for s in secs:
        t = s["title"].strip().lower()
        if t == "recent developments" or t == "lower-court developments":
            frontier = s
            break
    if frontier is None:
        return body_lines

    # rename in place first
    renamed = False
    hi = frontier["start"]
    if body_lines[hi].strip().lower() != "## lower-court developments":
        body_lines = list(body_lines)
        body_lines[hi] = "## Lower-court developments"
        renamed = True
        report["actions"].append({
            "pass": "frontier", "type": "rename",
            "detail": "## Recent developments -> ## Lower-court developments",
            "line": hi + 1,
        })

    # locate the first case-table section
    secs = h2_sections(body_lines)
    frontier = next((s for s in secs
                     if s["title"].strip().lower() == "lower-court developments"), None)
    first_ct = next((s for s in secs
                     if s["title"].strip().lower() in CASE_TABLE_TITLES), None)
    if frontier is None or first_ct is None:
        if first_ct is None and (renamed or frontier is not None):
            report["deferred"].append({
                "pass": "frontier", "reason": "no-case-tables",
                "detail": "no Key cases / Related section to anchor the move; "
                          "renamed only",
                "line": (frontier["start"] + 1) if frontier else 0,
            })
        return body_lines

    if frontier["start"] < first_ct["start"]:
        return body_lines  # already above the case tables

    # move: extract frontier block, trim trailing blanks, reinsert above first_ct
    block = body_lines[frontier["start"]:frontier["end"]]
    while block and block[-1].strip() == "":
        block.pop()
    block = block + [""]
    remaining = body_lines[:frontier["start"]] + body_lines[frontier["end"]:]
    # recompute first_ct index in `remaining` (frontier was AFTER it, so its start
    # is unchanged, but recompute defensively)
    secs2 = h2_sections(remaining)
    first_ct2 = next((s for s in secs2
                      if s["title"].strip().lower() in CASE_TABLE_TITLES), None)
    if first_ct2 is None:
        return body_lines  # safety: abort the move, keep the rename
    ins = first_ct2["start"]
    new_body = remaining[:ins] + block + remaining[ins:]
    report["actions"].append({
        "pass": "frontier", "type": "move",
        "detail": "moved Lower-court developments above the case tables",
        "line": ins + 1,
    })
    return new_body


# ---------------------------------------------------------------------------
# (c) Sources — em-dash list -> bracketed links
# ---------------------------------------------------------------------------

# text — url [ — trailing...]   ; text starts with an italic case name (*...*)
SOURCE_RE = re.compile(
    r"^(?P<indent>\s*[-*]\s+)(?P<text>\*.+?)\s+—\s+(?P<url>https?://[^\s—]+)(?P<trail>.*)$"
)


def _clean_source_text(text):
    """A source link-text is mechanical iff it is a single italic case name +
    citation ending in a 4-digit year: exactly two '*' (the case-name italics),
    no embedded em-dash, no embedded URL, and a year is present."""
    t = text.strip()
    if not t.startswith("*"):
        return False
    if t.count("*") != 2:
        return False
    if "—" in t or "http" in t:
        return False
    if not re.search(r"\b(1[6-9]\d\d|20\d\d)\b", t):
        return False
    return True


def convert_sources(body_lines, report):
    secs = h2_sections(body_lines)
    src = next((s for s in secs
                if s["title"].strip().lower() == "sources"), None)
    if src is None:
        return body_lines
    fenced = c.fenced_line_numbers(body_lines)
    body_lines = list(body_lines)
    for i in range(src["start"] + 1, src["end"]):
        if i in fenced:
            continue
        line = body_lines[i]
        if "](http" in line or re.match(r"^\s*[-*]\s+\[", line):
            continue  # already bracketed / a markdown link — idempotent skip
        m = SOURCE_RE.match(line)
        if not m:
            continue
        text = m.group("text").strip()
        if not _clean_source_text(text):
            report["deferred"].append({
                "pass": "sources", "reason": "ambiguous-source",
                "detail": "non-mechanical Sources row (multiple URLs / embedded "
                          "parenthetical / no clean case-name+cite): %s" % line.strip()[:90],
                "line": i + 1,
            })
            continue
        trail = m.group("trail")
        trail = re.sub(r"^\s*—\s*", "", trail).strip()  # drop leading em-dash sep
        new = "%s[%s](%s)" % (m.group("indent"), text, m.group("url"))
        if trail:
            new += " " + trail
        if new != line:
            body_lines[i] = new
            report["actions"].append({
                "pass": "sources", "type": "bracket-link",
                "detail": text, "line": i + 1,
            })
    return body_lines


# ---------------------------------------------------------------------------
# (d) Pitfalls — normalize the bold lead-in when mechanically safe
# ---------------------------------------------------------------------------

PITFALL_KEYWORDS_RE = re.compile(
    r"pitfall|common error|recurring.*error|field and analytical error", re.IGNORECASE
)
BOLD_LEAD_RE = re.compile(r"^(?P<indent>\s*)(?:[-*]\s+)?\*\*(?P<bold>.+?)\.?\*\*\s*(?P<rest>.*)$")
CANON_PITFALL = "**Common pitfalls.**"


def _next_nonblank(body_lines, start, end):
    for k in range(start, end):
        if body_lines[k].strip() != "":
            return k
    return None


def convert_pitfalls(body_lines, report):
    fenced = c.fenced_line_numbers(body_lines)
    body_lines = list(body_lines)
    n = len(body_lines)
    for i in range(n):
        if i in fenced:
            continue
        line = body_lines[i]
        # standalone pitfalls H2 -> non-mechanical (needs merge into the Brief)
        mh = c.HEADING_RE.match(line)
        if mh and len(mh.group(1)) == 2 and PITFALL_KEYWORDS_RE.search(mh.group(2)):
            report["deferred"].append({
                "pass": "pitfalls", "reason": "standalone-h2",
                "detail": "standalone pitfalls H2 '%s' — merge into The Brief as a "
                          "'**Common pitfalls.**' bold-lead block (S7 judgment)"
                          % mh.group(2).strip(),
                "line": i + 1,
            })
            continue
        m = BOLD_LEAD_RE.match(line)
        if not m or not PITFALL_KEYWORDS_RE.search(m.group("bold")):
            continue
        if m.group("rest").strip() != "":
            # inline-enumerated items after the lead -> non-mechanical
            report["deferred"].append({
                "pass": "pitfalls", "reason": "inline-enumerated",
                "detail": "pitfalls lead-in has inline content (e.g. (1)…(2)…); "
                          "convert to a '**Common pitfalls.**' + bullet list (S7)",
                "line": i + 1,
            })
            continue
        nb = _next_nonblank(body_lines, i + 1, n)
        if nb is None or not re.match(r"^\s*[-*]\s+", body_lines[nb]):
            report["deferred"].append({
                "pass": "pitfalls", "reason": "no-bullets",
                "detail": "pitfalls bold-lead not followed by a bullet list",
                "line": i + 1,
            })
            continue
        # mechanical: rewrite the lead-in to the canonical bold lead
        if line.strip() != CANON_PITFALL:
            body_lines[i] = CANON_PITFALL
            report["actions"].append({
                "pass": "pitfalls", "type": "normalize-lead",
                "detail": "'%s' -> '%s'" % (line.strip()[:60], CANON_PITFALL),
                "line": i + 1,
            })
    return body_lines


# ---------------------------------------------------------------------------
# per-page driver
# ---------------------------------------------------------------------------

def convert_page(path):
    text = c.read_text(path)
    prefix, body_lines = split_raw(text)
    report = {"page": c.relpath(path), "changed": False,
              "actions": [], "deferred": []}

    body_lines = convert_tables(body_lines, report)
    body_lines = convert_frontier(body_lines, report)
    body_lines = convert_sources(body_lines, report)
    body_lines = convert_pitfalls(body_lines, report)

    new_text = "\n".join(prefix + body_lines)
    report["changed"] = new_text != text
    return report, new_text


def main():
    ap = argparse.ArgumentParser(description="S5 mechanical entry-model converter")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", default=True,
                      help="(default) report the diff summary; write nothing")
    mode.add_argument("--apply", action="store_true",
                      help="write the transformed files back in place")
    ap.add_argument("--report-json", metavar="PATH",
                    help="write the structured per-page report JSON")
    ap.add_argument("pages", nargs="+", help="page path(s) or dir/glob(s)")
    args = ap.parse_args()

    apply = args.apply
    paths = list(c.iter_markdown_files(args.pages))
    reports = []
    n_changed = 0
    for path in paths:
        try:
            report, new_text = convert_page(path)
        except Exception as e:  # never die on one bad page
            reports.append({"page": c.relpath(path), "error": str(e)})
            sys.stderr.write("[convert] ERROR %s: %s\n" % (c.relpath(path), e))
            continue
        reports.append(report)
        if report["changed"]:
            n_changed += 1
            if apply:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(new_text)
        # human-readable per-page summary
        if report["actions"] or report["deferred"]:
            sys.stderr.write("\n%s%s\n" % (
                report["page"], "" if apply else " (dry-run)"))
            for a in report["actions"]:
                sys.stderr.write("  changed  [%s] %s %s (L%s)\n" % (
                    a["pass"], a.get("type", ""),
                    a.get("detail") or a.get("schema") or a.get("note") or "", a["line"]))
            for d in report["deferred"]:
                sys.stderr.write("  DEFER    [%s] %s (L%s)\n" % (
                    d["pass"], d.get("detail", d.get("reason", "")), d["line"]))

    if args.report_json:
        with open(args.report_json, "w", encoding="utf-8") as fh:
            json.dump(reports, fh, ensure_ascii=False, indent=2)

    total_actions = sum(len(r.get("actions", [])) for r in reports)
    total_defer = sum(len(r.get("deferred", [])) for r in reports)
    sys.stderr.write(
        "\n[convert] %d page(s): %d would change%s · %d action(s) · %d deferred\n" % (
            len(paths), n_changed, "" if apply else " (dry-run)",
            total_actions, total_defer))
    sys.exit(0)


if __name__ == "__main__":
    main()
