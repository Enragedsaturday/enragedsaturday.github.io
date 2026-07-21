#!/usr/bin/env python3
"""
S4 · R10 — regenerate `Case Index.md` from case-page frontmatter.

Single source of truth = `content/cases/*.md` frontmatter. This builds the
Case-Index table:

  | Case | Holding | Good law | Home page(s) | CourtListener |

  - Case          [[<title>]] wikilink to the case page
  - Holding       the `holding:` one-line ratio (frontmatter)
  - Good law      treatment.status -> glyph+label (NO blank cells, N13)
  - Home page(s)  the homes[].page links joined by " · "
  - CourtListener [opinion](<courtlistener.opinion_url>)

The 3 flagged caption exception rows (self-help; Cruz/West/Jackson trio;
stolen-vehicle White) are carried forward from the existing index verbatim
(no wikilink; flag note kept) so they never vanish; their previously-blank
Good-law cell is set to "⚠ unverifiable" to satisfy N13/LINT-6.

The human header prose + `type: index` frontmatter above the table are
preserved byte-for-byte (everything before the `| Case |` header). Rows are
sorted alphabetically by case name. Output is idempotent: re-running yields a
byte-identical file.

Stdlib only.  Usage: python3 scripts/build_case_index.py [--check]
  --check : regenerate to a temp string and diff against the on-disk file;
            exit 1 if they differ (does not write).
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "lint"))
import _common as c  # noqa: E402

INDEX = os.path.join(REPO, "content", "legal-system-research-and-reference", "Case Index.md")  # re-pointed at the S3 migration (2026-07-04)
CASES_GLOB = os.path.join(REPO, "content", "cases", "*.md")
BRIEF_QUEUE = os.path.join(REPO, "_overhaul", "coverage", "brief-mention-queue.md")
EXPORT_MARK = "CASE-INDEX-EXPORT"

TABLE_HEADER = "| Case | Holding | Good law | Home page(s) | CourtListener |"
TABLE_SEP = "|---|---|---|---|---|"
HEADER_RE = re.compile(r"^\|\s*Case\s*\|")

STATUS_LABEL = {
    "good": "good",
    "criticized": "⚠ criticized",
    "limited": "⚠ limited",
    "abrogated": "⚠ abrogated",
    "overruled": "⛔ overruled",
}
FLAG_LABEL = "⚠ unverifiable"


def sortkey(name):
    k = (name or "").strip().lower().replace("’", "'")
    k = re.sub(r"^[^a-z0-9]+", "", k)   # ignore leading quotes/italics/punct
    k = re.sub(r"\s+", " ", k)
    return k


def read_holding(text):
    """The holding is stored json-encoded; decode it losslessly."""
    for ln in text.split("\n")[1:]:
        if ln.strip() == "---":
            break
        m = re.match(r"^holding:\s*(.*\S)\s*$", ln)
        if m:
            try:
                return json.loads(m.group(1))
            except ValueError:
                return m.group(1)
    return ""


def page_rows():
    rows = []
    for p in sorted(glob.glob(CASES_GLOB)):
        text = c.read_text(p)
        fm, _body, _ = c.split_frontmatter(text)
        title = fm.get("title") or os.path.splitext(os.path.basename(p))[0]
        holding = read_holding(text)
        status = (c.fm_get(fm, "treatment", "status") or "").strip().lower()
        good = STATUS_LABEL.get(status, status or "good")
        homes = fm.get("homes") or []
        pages = [h.get("page", "").strip() for h in homes
                 if isinstance(h, dict) and h.get("page")]
        home = " · ".join(pages)
        opinion = c.fm_get(fm, "courtlistener", "opinion_url") or ""
        cl = "[opinion](%s)" % opinion if opinion else "—"
        case = "[[%s]]" % title
        rows.append((sortkey(title),
                     [case, holding, good, home, cl]))
    return rows


def _split_cells(ln):
    """Split a table row into cells on COLUMN-DELIMITER pipes only.

    R12-maintenance fix (FIN-INDEX, S9 P4): the old naive `ln.split("|")` broke
    on any carry-forward row whose Holding cell had picked up an S8 term-link with
    an escaped display pipe (`[[Reading and Citing Cases#reporter\\|reporter]]`) —
    the extra `|` inflated the cell count past 5 and the row was silently dropped,
    violating the "flagged rows never vanish" contract (e.g. the Cruz/West/Jackson
    UNVERIFIABLE row). Mirror the frozen zones splitter: blank wikilink-internal
    pipes, ignore escaped `\\|`, then slice on the surviving delimiter pipes."""
    buf = list(ln)
    for m in re.finditer(r"\[\[.*?\]\]", ln):
        for i in range(m.start(), m.end()):
            if buf[i] == "|":
                buf[i] = "\x00"
    masked = "".join(buf)
    pos = [m.start() for m in re.finditer(r"(?<!\\)\|", masked)]
    return [ln[a + 1:b].strip() for a, b in zip(pos, pos[1:])]


def flagged_rows(existing_lines):
    """Carry forward flagged caption rows from the current table verbatim,
    forcing a non-blank Good-law cell (N13)."""
    out = []
    for ln in existing_lines:
        if not ln.startswith("|") or ln.startswith("|---") or HEADER_RE.match(ln):
            continue
        cells = _split_cells(ln)
        if len(cells) != 5:
            continue
        case = cells[0]
        if "UNVERIFIABLE" not in case and "UNCONFIRMED" not in case:
            continue
        name = case.strip().strip("*").strip()
        out.append((sortkey(name),
                    [case, cells[1], FLAG_LABEL, cells[3], cells[4]]))
    return out


def brief_rows(page_titles=frozenset()):
    """Append the brief-mention exception rows (no `content/cases/` page)
    from the machine-readable CASE-INDEX-EXPORT table in
    `brief-mention-queue.md`. These are S5-demoted cases that earn a
    Case-Index row + an S6 home-page history note but NO BIRAC page.

    Each emitted row: an italic case LABEL (no [[wikilink]] — there is no
    page to link) tagged 'brief-mention — no page'; the one-line holding; the
    treatment glyph (N13 — never blank); the home-doctrine wikilink; and the
    CourtListener opinion link. Deterministic -> idempotent.

    De-dup guard: a queued case that has SINCE been authored a
    `content/cases/` page (S5 demotion is reversible; S7 promoted many) is
    skipped here — its authored page row is the single source of truth, so it
    must not also emit a stale "no page" brief-mention row (page-vs-brief-
    mention duplicate). `page_titles` is the set of authored case-page titles.
    """
    out = []
    if not os.path.exists(BRIEF_QUEUE):
        return out
    lines = c.read_text(BRIEF_QUEUE).split("\n")
    start = next((i for i, ln in enumerate(lines) if EXPORT_MARK in ln), None)
    if start is None:
        return out
    in_table = False
    for ln in lines[start + 1:]:
        s = ln.strip()
        if s.startswith("|"):
            in_table = True
            if s.startswith("|---") or s.lower().startswith("| case "):
                continue
            cells = [x.strip() for x in s.split("|")[1:-1]]
            if len(cells) != 5:
                continue
            case, holding, status, home, url = cells
            if case in page_titles:
                continue  # authored page row wins (single source of truth)
            glyph = STATUS_LABEL.get(status.lower(), status or "good")
            cl = "[opinion](%s)" % url if url.startswith("http") else "—"
            label = "*%s — brief-mention (no page)*" % case
            out.append((sortkey(case), [label, holding, glyph, home, cl]))
        elif in_table:
            break
    return out


def build():
    lines = c.read_text(INDEX).split("\n")
    # preamble = everything before the table header row
    hdr_idx = next((i for i, ln in enumerate(lines) if HEADER_RE.match(ln)),
                   None)
    if hdr_idx is None:
        raise RuntimeError("table header not found in Case Index.md")
    preamble = lines[:hdr_idx]

    pages = page_rows()
    page_titles = frozenset(
        cells[0][2:-2] for _k, cells in pages
        if cells[0].startswith("[[") and cells[0].endswith("]]")
    )
    briefs = brief_rows(page_titles)
    rows = pages + flagged_rows(lines) + briefs
    rows.sort(key=lambda r: r[0])

    body = [TABLE_HEADER, TABLE_SEP]
    for _key, cells in rows:
        body.append("| %s | %s | %s | %s | %s |" % tuple(cells))

    nbrief = sum(1 for _k, cells in rows
                 if "brief-mention (no page)" in cells[0])
    return "\n".join(preamble + body) + "\n", len(rows), \
        sum(1 for _k, cells in rows if cells[2] == FLAG_LABEL), nbrief


def main():
    out, nrows, nflag, nbrief = build()
    if "--check" in sys.argv[1:]:
        cur = c.read_text(INDEX) if os.path.exists(INDEX) else ""
        if cur == out:
            print("OK: regenerated output is byte-identical (idempotent).")
            sys.exit(0)
        print("DIFF: regenerated output differs from on-disk file.")
        sys.exit(1)
    with open(INDEX, "w", encoding="utf-8") as fh:
        fh.write(out)
    blanks = sum(1 for ln in out.split("\n")
                 if ln.startswith("|") and not ln.startswith("|---")
                 and not HEADER_RE.match(ln)
                 and len(ln.split("|")) == 7
                 and ln.split("|")[3].strip() == "")
    print("wrote %s" % os.path.relpath(INDEX, REPO))
    print("rows: %d  (linked: %d, brief-mention: %d, flagged: %d)"
          % (nrows, nrows - nflag - nbrief, nbrief, nflag))
    print("blank Good-law cells: %d" % blanks)


if __name__ == "__main__":
    main()
