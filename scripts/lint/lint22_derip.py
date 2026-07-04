#!/usr/bin/env python3
"""
LINT-22 — de-rip naming.  S3 · R9 (alias LINT-S3-derip; S9 R8 roster row 22).

Anti-plagiarism: category and sub-umbrella labels are OUR OWN and must not
reproduce Bandiero's verbatim part titles (he is an S9 reviewer). This lint
fails (HIGH) if any category / sub-umbrella LABEL — its `index.md` frontmatter
`title:`, or, absent a title, the folder-derived display name — string-matches
(case-insensitive, whitespace-normalized) a committed banned-title.

The enforced R9 renames were: "Levels of Suspicion" -> Standards of Proof;
"Search Warrant Exceptions" -> Warrant Exceptions; "The Sixth Amendment Right to
Counsel" -> The Right to Counsel; "What is a Search/Seizure?" -> Searches /
Seizures; and the copied Bandiero 7a/7b "PC needed / PC not needed" exception
split is retired.

SCOPE — same overview set as LINT-19: every `index.md` under `content/` except
the site root `content/index.md` and `content/cases/index.md`.

SELF-TEST (S1 A3): `python3 lint22_derip.py --self-test` over the labeled
`fixtures/lint-22-*.md` pages (filename suffix `-pass` / `-fail`).

Usage:
  python3 lint22_derip.py [glob ...]
  python3 lint22_derip.py --self-test
"""

import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-22"

# ---------------------------------------------------------------------------
# The committed banned-title list (S3 R9). Built from R9's five NAMED Bandiero
# part titles plus the retired 7a/7b "PC needed / not needed" exception-split
# labels (the historical `7a-pc-needed` / `7b-pc-not-needed` folders and their
# display names, sourced from the pre-O2 layout). Matching is case-insensitive
# and whitespace-normalized (see _norm). EXTEND THIS LIST as further Bandiero /
# other-source verbatim titles are identified — one entry per banned surface form.
# ---------------------------------------------------------------------------
BANNED_TITLES = (
    # R9's five named Bandiero TOC part titles:
    "Levels of Suspicion",
    "Search Warrant Exceptions",
    "The Sixth Amendment Right to Counsel",
    "What is a Search?",
    "What is a Seizure?",
    # the retired 7a/7b PC-needed / not-needed exception split (R9: "the copied
    # 7a/7b PC-needed split is gone") — conceptual labels + the historical
    # pre-O2 display names:
    "PC needed",
    "PC not needed",
    "Probable Cause Needed",
    "Probable Cause Not Needed",
    "Probable-Cause Exceptions",
    "Suspicion-Based / Per-Se Exceptions",
)


def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


_BANNED_NORM = {_norm(b): b for b in BANNED_TITLES}


def _is_overview_index(path):
    rel = os.path.relpath(path, c.CONTENT_ROOT).replace(os.sep, "/")
    if os.path.basename(rel).lower() != "index.md":
        return False
    if rel == "index.md":
        return False
    if rel.split("/")[0] == "cases":
        return False
    return True


def _folder_display_name(path):
    """Quartz-style fallback display when index.md has no title: the containing
    folder slug with hyphens/underscores turned to spaces."""
    folder = os.path.basename(os.path.dirname(os.path.abspath(path)))
    return folder.replace("-", " ").replace("_", " ").strip()


def check_label(path):
    """Return HIGH violation(s) if this overview's label (title, else folder
    display name) matches a banned title."""
    out = []
    fm, _body, _start = c.split_frontmatter(c.read_text(path))
    title = fm.get("title")
    label = title if (isinstance(title, str) and title.strip()) \
        else _folder_display_name(path)
    hit = _BANNED_NORM.get(_norm(label))
    if hit is not None:
        out.append(c.make_violation(
            LINT, path, 1, c.HIGH,
            "category/sub-umbrella label %r reproduces a banned (Bandiero / "
            "retired-split) title %r — labels must be our own, de-ripped [R9]"
            % (label, hit)))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        if _is_overview_index(path):
            out.extend(check_label(path))
    return out


# --------------------------------------------------------------------------
# self-test — labeled fixtures (filename suffix -pass / -fail)
# --------------------------------------------------------------------------

def self_test():
    fixdir = os.path.join(c.HERE, "fixtures")
    files = sorted(glob.glob(os.path.join(fixdir, "lint-22-*.md")))
    if not files:
        sys.stderr.write("[self-test] FAIL: no lint-22-*.md fixtures\n")
        return 1
    ok = True
    for f in files:
        name = os.path.basename(f)
        expect = "pass" if name.endswith("-pass.md") else \
                 "fail" if name.endswith("-fail.md") else None
        if expect is None:
            continue
        viols = check_label(f)
        passed = (len(viols) == 0) if expect == "pass" else (len(viols) > 0)
        ok = ok and passed
        sys.stderr.write("[self-test] %-32s expect=%-4s -> %s (%d viol)\n" % (
            name, expect, "OK" if passed else "MISMATCH", len(viols)))
        if not passed:
            for v in viols:
                sys.stderr.write("             %s\n" % v["message"])
    sys.stderr.write("[self-test] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    c.cli_main(run, LINT)
