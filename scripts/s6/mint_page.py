#!/usr/bin/env python3
"""S6 R8 page-authoring pipeline — promote a verified stub into a born-conformant
BIRAC case page, atomically, offline.

Dry-run is the DEFAULT. `--write` is the guarded commit. The CLI performs ZERO
CourtListener / network calls (S6 R7 one-credential rule): it reads the signed
worklist (`_run/o2-execute/R8-WORKLIST.json`), the S2 lake stub record, and the
lake manifest, and reuses the S2 projection machinery (`scripts/s2/project.py` +
`serializer.py`) to build the data frontmatter — it never reimplements
projection.

One invocation authors one page (S6 R8 / SD3). Given a `--row <record_id>` and a
`--payload <path>` (the wave author's page BODY, written to a scratch file), it
stages, all-or-nothing:

  1. `content/cases/<stem>.md` — BIRAC skeleton (S5 R3), projected data
     frontmatter (S2), authored content frontmatter/body, born `lake.status`
     (default `under_review` — see BORN-STATUS note below), R15 banner renders.
  2. the S2 A6 stub->record promotion: rename
     `_overhaul2/lake/cases/<record_id>.json` -> `<stem>.json`, `record_id`->stem,
     drop `stub`, status->born-status, + a `_manifest.json` rename entry.
  3. an `authored` ledger row appended to `s6-authored-ledger.jsonl`, carrying the
     homes/roles + cite/year/holding/opinion + relevance-tag hints S7 needs to
     materialize the Key/Related rows and the generator needs for the index.

LOOP-2 amendment (R8-PIPELINE-ADJUDICATION E2/E3): the CLI **no longer writes the
Case Index or any homes page**. The Case Index is regenerated per wave batch by
`scripts/build_case_index.py` (single writer). S7 materializes each home's
Key/Related row from `s6-authored-ledger.jsonl` when it converts that home page.
The `homes[]` existence check is KEPT (a missing home target is refused).

The staged state is validated by LINT-15 (case skeleton), LINT-16 (case tables)
and a LINT-14 page<->record binding check; a failed lint => no partial write,
non-zero exit, machine-readable reason. Re-running an already-promoted row is a
clean `already-authored` no-op (S6 R8 resumability).

BORN-STATUS note (design decision, escalated): R8's prose says the page is born
`lake.status: draft`; S6 section 8 says the specimen "carries under_review until
the gates pass". `under_review` is a LINT-14 publish-eligible status, so the
mandated page<->record gate meaningfully validates the staged binding, and R15
renders the identical unverified banner for both. Default is `under_review`;
`--born-status draft` selects the literal R8 word (binding then checked via a
draft-inclusive sub-check). See the build report for the full rationale.

Usage:
  python3 scripts/s6/mint_page.py --row <record_id> --payload <body.md>     # dry-run
  python3 scripts/s6/mint_page.py --row <record_id> --payload <body.md> --as-of <ISO> --write
  python3 scripts/s6/mint_page.py --validate-only --row <record_id> --payload <body.md>
  python3 scripts/s6/mint_page.py --self-test
  python3 scripts/s6/mint_page.py --specimen-test
"""

import argparse
import copy
import glob
import json
import os
import re
import sys
from collections import OrderedDict


HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
LINT_DIR = os.path.join(REPO_ROOT, "scripts", "lint")
if LINT_DIR not in sys.path:
    sys.path.insert(0, LINT_DIR)

from scripts.s2 import project as s2project  # noqa: E402
from scripts.s2 import serializer  # noqa: E402
import _common as lint_common  # noqa: E402
import lint14_pagerecord as lint14  # noqa: E402
import lint15_skeleton as lint15  # noqa: E402
import lint16_casetables as lint16  # noqa: E402


# --------------------------------------------------------------------------
# constants / paths
# --------------------------------------------------------------------------

WORKLIST_REL = os.path.join("_run", "o2-execute", "R8-WORKLIST.json")
LEDGER_REL = os.path.join("_run", "o2-execute", "s6-authored-ledger.jsonl")
LAKE_REL = os.path.join("_overhaul2", "lake")
CONTENT_REL = "content"
MANIFEST_NAME = "_manifest.json"
FIXTURES_DIR = os.path.join(HERE, "fixtures")

# Lake statuses from which an S6 stub may be authored into a page. All 148 signed
# R8-WORKLIST rows are `verified_identity`; `verified` covers re-key-gated rows
# (packetb-dispositions: Wyman / GM-Leasing / Verdugo) and a re-promoted specimen;
# `verified_off_cl` covers the A17 English-corpus elevations (Entick / Wilkes).
ACCEPT_STATUSES = ("verified_identity", "verified", "verified_off_cl")
BORN_STATUSES = ("under_review", "draft")
DEFAULT_BORN_STATUS = "under_review"

# machine-readable refusal codes
REFUSE_WORKLIST_ABSENT = "worklist-absent"
REFUSE_NO_LAKE_RECORD = "no-lake-record"
REFUSE_WRONG_STATUS = "wrong-status"
REFUSE_NOT_A_STUB = "not-a-stub"
REFUSE_MISSING_CITATION = "record-missing-citation"
REFUSE_SLIP_INCOMPLETE = "record-slip-identity-incomplete"  # slip_only but no docket/court/year
REFUSE_STEM_RESERVED = "stem-contains-double-dash"
REFUSE_STEM_COLLISION = "stem-collision-distinct-case"
REFUSE_PAYLOAD_INVALID = "payload-invalid"
REFUSE_LINT_FAILED = "staged-lint-failed"
REFUSE_HOME_MISSING = "home-page-missing"
REFUSE_MANIFEST_MISSING_RECORD = "manifest-missing-record"
REFUSE_WEDGED_PARTIAL = "wedged-partial-state"       # F-R8-02: unrecoverable half-commit
REFUSE_HOMES_ROLES_DESYNC = "homes-roles-desync"     # F-R8-06: homes[]/roles[] not in bijection
REFUSE_RECORD_ID_COLLISION = "record-id-collision"   # F-R8-12: global lake record_id clash
# Retired loop-2 (R8-PIPELINE-ADJUDICATION E2/E3): the Case-Index insertion and
# the homes-page row insertion were REMOVED — the Case Index has a single writer
# (scripts/build_case_index.py, regenerated per wave batch) and S7 materializes
# the Key/Related rows from s6-authored-ledger.jsonl when it converts each home
# page. So `case-index-not-r6-converted` / `home-not-r6-converted` no longer exist.

ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}:\d{2}(Z|[+-]\d{2}:?\d{2})?)?$")


# --------------------------------------------------------------------------
# small deterministic helpers (kept local; projection reuses S2)
# --------------------------------------------------------------------------

def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json_atomic(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, path)


def write_text_atomic(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)


def norm_as_of(value):
    """Validate the deterministic --as-of stamp; return it unchanged. Raises on a
    non-ISO value so no wall-clock ever leaks into a journaled field."""
    if not value or not ISO_RE.match(str(value).strip()):
        raise ValueError("--as-of must be an ISO date/datetime (e.g. 2026-07-07 "
                         "or 2026-07-07T00:00:00Z); got %r" % (value,))
    return str(value).strip()


def home_link_from_path(home_path):
    """Map a homes[] content path to its wikilink target: a `.../Foo.md` -> `Foo`;
    a `.../<dir>/index.md` -> the dir's title-cased slug words. The link target is
    always the basename stem (Quartz resolves by title/stem), except index.md
    which resolves to its parent directory's display name."""
    rel = home_path[len("content/"):] if home_path.startswith("content/") else home_path
    stem = os.path.splitext(os.path.basename(rel))[0]
    if stem == "index":
        parent = os.path.basename(os.path.dirname(rel))
        return " ".join(w.capitalize() if w.islower() else w for w in parent.split("-"))
    return stem


def resolve_home_file(home_path, content_root):
    p = home_path if home_path.startswith("content" + os.sep) or home_path.startswith("content/") \
        else os.path.join(content_root, home_path)
    return os.path.normpath(os.path.join(REPO_ROOT, p)) if not os.path.isabs(p) else p


# --------------------------------------------------------------------------
# worklist / lake / manifest loaders
# --------------------------------------------------------------------------

def load_worklist(path=None):
    path = path or os.path.join(REPO_ROOT, WORKLIST_REL)
    return read_json(path)


def worklist_row(worklist, record_id):
    for row in worklist.get("rows", []):
        if row.get("record_id") == record_id:
            return row
    return None


def lake_cases_dir(lake_root):
    return os.path.join(lake_root, "cases")


def lake_record_path(lake_root, record_id):
    return os.path.join(lake_cases_dir(lake_root), record_id + ".json")


def manifest_path(lake_root):
    return os.path.join(lake_root, MANIFEST_NAME)


def load_manifest(lake_root):
    return read_json(manifest_path(lake_root))


def manifest_record(manifest, record_id):
    for rec in manifest.get("records", []):
        if rec.get("record_id") == record_id:
            return rec
    return None


# --------------------------------------------------------------------------
# stem + collision (S5 R9 / S2 A6)
# --------------------------------------------------------------------------

def existing_case_stems(content_root):
    out = {}
    for p in glob.glob(os.path.join(content_root, "cases", "*.md")):
        out[os.path.splitext(os.path.basename(p))[0]] = p
    return out


def choose_stem(caption, record, content_root):
    """S2 A6: page stem = caption. S5 R9: collide with an existing DIFFERENT case
    -> disambiguate by (year) then (court). Returns (stem, note). Refuses a stem
    that already carries the reserved `--` (A6 invariant)."""
    caption = caption.strip()
    if "--" in caption:
        raise ValueError("caption %r contains the reserved '--' namespace [A6]" % caption)
    existing = existing_case_stems(content_root)
    if caption not in existing:
        return caption, None
    # a same-caption page exists — the specimen exhibit is the two-Smiths case.
    year = (record.get("identity") or {}).get("year")
    if year:
        cand = "%s (%s)" % (caption, year)
        if cand not in existing:
            return cand, "disambiguated by year (S5 R9 collision with %r)" % caption
    court = (record.get("identity") or {}).get("court_id") or (record.get("identity") or {}).get("circuit")
    if court:
        # build the suffix from the non-empty parts only, so a court-but-no-year
        # record yields `Caption (ca9)`, never `Caption (ca9 )` [F-R8-07].
        suffix = " ".join(p for p in (str(court), str(year) if year else "") if p)
        cand = "%s (%s)" % (caption, suffix)
        if cand not in existing:
            return cand, "disambiguated by court+year (S5 R9)"
    raise ValueError("stem collision: %r already names a distinct case page and no "
                     "(year)/(court) disambiguation is free" % caption)


# --------------------------------------------------------------------------
# payload parsing + validation
# --------------------------------------------------------------------------

BIRAC_HEADER_LINE_RE = re.compile(r"Treatment:\s*\*\*")
SOURCES_BULLET_OK_RE = re.compile(r"^\s*-\s*\[")            # bracketed link bullet (R12)


def parse_payload(path):
    text = serializer.read_markdown(path)
    fm, body, _start = serializer.split_frontmatter(text)
    # "everything below the frontmatter" is the body; if there is no frontmatter,
    # the whole file is the body and fm is {}.
    if not isinstance(fm, dict):
        fm = {}
    return fm, body


def validate_payload_body(body, stem):
    """Payload-body validation the work order enumerates (S5 R3/R6/R12). Returns a
    list of machine-readable {code, message}. LINT-15/16 are invoked over the
    fully-staged page separately (that catches the BIRAC sequence + table schemas
    authoritatively); these checks are the payload-only guards LINT-15/16 do not
    cover (H1 title, header line, Sources bracket form)."""
    errs = []
    lines = body.split("\n")

    # H1 must be `# <stem>`
    h1 = next((ln for ln in lines if ln.startswith("# ")), None)
    if h1 is None:
        errs.append({"code": "no-h1", "message": "payload body has no `# <title>` H1"})
    elif h1[2:].strip() not in (stem, '"%s"' % stem):
        errs.append({"code": "h1-mismatch",
                     "message": "H1 %r != page stem %r [S5 R3]" % (h1[2:].strip(), stem)})

    # locate section spans
    body_lines = lines
    secs = {s["title"].strip().lower(): s for s in lint_common.sections(body_lines)}

    # header line (R3): the degraded plain-text line between H1 and the first H2,
    # carrying `Treatment: **<label>**`.
    first_h2 = min((s["start"] for s in secs.values()), default=len(body_lines))
    header_zone = "\n".join(body_lines[:first_h2])
    if not BIRAC_HEADER_LINE_RE.search(header_zone):
        errs.append({"code": "no-header-line",
                     "message": "missing the R3 header line (a `… · Treatment: **<label>**` "
                                "line between the H1 and the first H2)"})

    # Sources (R12): bracketed-link bullets, never the retired `- *Case*, … — url` form.
    src = secs.get("sources")
    if src is None:
        errs.append({"code": "no-sources", "message": "missing `## Sources` section [S5 R3/R12]"})
    else:
        bullets = [body_lines[i] for i in range(src["start"] + 1, src["end"])
                   if body_lines[i].strip().startswith("-")]
        if not bullets:
            errs.append({"code": "empty-sources", "message": "`## Sources` has no bullets [R12]"})
        for b in bullets:
            # R12: EVERY Sources bullet must be the bracketed `- [...](...)` form
            # (a plain-text or em-dash bullet is rejected) [F-R8-08].
            if not SOURCES_BULLET_OK_RE.match(b):
                errs.append({"code": "sources-not-bracketed",
                             "message": "Sources bullet is not the bracketed "
                                        "`- [*Case*, cite (year)](url)` form [R12]: "
                                        + b.strip()[:80]})
    return errs


# --------------------------------------------------------------------------
# frontmatter assembly (reuses S2 projection)
# --------------------------------------------------------------------------

def promote_record(record, stem, born_status, as_of):
    """S2 A6 stub->record promotion, in memory. record_id -> stem, drop `stub`,
    status -> born_status; stamp provenance for a deterministic projected_at."""
    promoted = copy.deepcopy(record)
    promoted["record_id"] = serializer_page_stem_guard(stem)
    promoted.pop("stub", None)
    promoted["status"] = born_status
    ident = promoted.setdefault("identity", {})
    if isinstance(ident, dict):
        # keep identity as-is; page-backed record_id equals stem by construction
        pass
    prov = promoted.setdefault("provenance", {})
    if isinstance(prov, dict):
        prov["date_modified"] = as_of_to_iso(as_of)
        prov.setdefault("date_created", as_of_to_iso(as_of))
        prov.setdefault("s6_promotion", {})
        prov["s6_promotion"] = {"from_record_id": record.get("record_id"),
                                "to_record_id": stem, "as_of": as_of,
                                "born_status": born_status}
    return promoted


def serializer_page_stem_guard(stem):
    if "--" in stem:
        raise ValueError("page-backed record_id cannot contain reserved '--': %s" % stem)
    return stem


def as_of_to_iso(as_of):
    s = str(as_of).strip()
    if "T" in s or " " in s:
        return s.replace(" ", "T")
    return s  # bare date; project.date_from_record slices [:10]


# --------------------------------------------------------------------------
# slip-only support (S2 A3 slip precedent): a real case whose reporter cite does
# not exist yet, marked EXPLICITLY on the lake record (citations.slip_only: true).
# --------------------------------------------------------------------------

def record_is_slip_only(record):
    """True iff the lake record carries the EXPLICIT slip-only marker (never
    inferred from an absent citation)."""
    return (record.get("citations") or {}).get("slip_only") is True


def slip_court_abbr(record):
    """Bluebook-ish court abbreviation for a slip cite, from identity."""
    ident = record.get("identity") or {}
    level = ident.get("court_level")
    if level == "scotus":
        return "U.S."
    if level == "coa":
        circ = ident.get("circuit")
        return s2project.circuit_label(circ) if circ else None
    if level == "state":
        return ident.get("state") or None
    return None


def derive_slip_cite(record):
    """PROPOSED slip-opinion cite form for the header + Case cell, behind the
    citations.slip_only marker (FLAGGED FOR RATIFICATION — S2 A3 sanctions slip
    PINPOINTS, not a slip citation display; S5 R3 sanctions no slip header form).
    Bluebook slip form: `No. <docket>, slip op. (<court> <year>)`. Returns None if
    identity is too sparse for any honest cite (no docket AND no court/year)."""
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


def homes_roles_desync(row):
    """F-R8-06: fail-closed check that homes[] and roles[] are in bijection — every
    home has exactly one role and every role names a listed home. Returns a message
    string on desync (so the CLI refuses rather than silently defaulting to Key),
    else None."""
    homes = list(row.get("homes", []) or [])
    role_rows = list(row.get("roles", []) or [])
    role_homes = [r.get("home") for r in role_rows]
    missing_role = [h for h in homes if h not in role_homes]
    orphan_role = [rh for rh in role_homes if rh not in homes]
    blank_role = [r.get("home") for r in role_rows if not (r.get("role") or "").strip()]
    dup_role = [h for h in set(role_homes) if role_homes.count(h) > 1]
    if missing_role or orphan_role or blank_role or dup_role:
        return ("homes[]/roles[] desync: homes-without-role=%s · roles-without-home=%s · "
                "blank-role=%s · duplicate-role-home=%s"
                % (missing_role, orphan_role, blank_role, dup_role))
    return None


def build_homes_frontmatter(row):
    """homes[] frontmatter = worklist ground truth. Each entry: {page, role}. Callers
    must pass homes_roles_desync()-clean rows (no silent Key default) [F-R8-06]."""
    homes = []
    role_by_home = {r.get("home"): r.get("role") for r in (row.get("roles") or [])}
    for h in row.get("homes", []) or []:
        homes.append(OrderedDict([
            ("page", "[[%s]]" % home_link_from_path(h)),
            ("role", role_by_home.get(h)),
        ]))
    return homes


def assemble_frontmatter(promoted_record, row, payload_fm, stem):
    """Compose full case-page frontmatter: S2-projected managed data fields +
    authored/worklist-derived preserved fields. Data (weight/treatment/dates/cite)
    comes ONLY from the projection (R7 boundary); content comes from the payload."""
    projection = s2project.project_record(promoted_record)
    preserved = OrderedDict()
    preserved["title"] = stem
    preserved["type"] = "case"
    preserved["homes"] = build_homes_frontmatter(row)
    # content-owned fields from the author payload (never data)
    for key in ("related", "tags", "holding"):
        if key in payload_fm:
            preserved[key] = payload_fm[key]
    # aliases: worklist ground truth (fall back to payload if worklist omits)
    aliases = row.get("aliases") or payload_fm.get("aliases")
    if aliases:
        preserved["aliases"] = aliases
    fm = serializer.compose_projected_frontmatter(preserved, projection)
    return fm, projection


def render_page(frontmatter, body):
    fmtext = serializer.dumps_frontmatter(frontmatter)
    body = body if body.startswith("\n") else "\n" + body
    return fmtext + body


# --------------------------------------------------------------------------
# S7-materialization ledger hints (loop-2: the CLI no longer WRITES index/homes
# rows — it records everything S7 + the index generator need to write them later)
# --------------------------------------------------------------------------

# S5 R6 relevance-tag advisory vocabulary (Related schema-2 first-word tag).
RELEVANCE_TAGS = ("Extends", "Limits", "Boundary", "Foil")


def opinion_url(projection):
    """The opinion link URL for the eventual Opinion cell: CL when present, else
    the S2 R14 whitelisted off-CL fallback (Justia/Scholar/Cornell/official)."""
    url = (projection.get("courtlistener") or {}).get("opinion_url") or ""
    if not url:
        for link in projection.get("off_cl_links") or []:
            if isinstance(link, dict) and link.get("url"):
                return link["url"]
            if isinstance(link, str) and link:
                return link
    return url


def primary_home_link(row):
    """Primary home = the first Key home, else the first home (Related rows point
    a case's Primary-home cell at its owning doctrine page)."""
    role_by_home = {r.get("home"): r.get("role") for r in (row.get("roles") or [])}
    homes = row.get("homes", []) or []
    for h in homes:
        if (role_by_home.get(h) or "").strip().lower().startswith("key"):
            return home_link_from_path(h)
    return home_link_from_path(homes[0]) if homes else ""


def placements_from_payload(payload_fm):
    """OPTIONAL author-supplied per-home cell hints for the S7 row materialization:
    a list of {home, cell, tag?, primary_home?}, keyed to the worklist homes. No
    longer required (S7 authors the relevance/holding text when it converts the
    home page) — folded into the ledger `home_rows` if present."""
    pl = payload_fm.get("placements")
    out = {}
    if isinstance(pl, list):
        for item in pl:
            if isinstance(item, dict) and item.get("home"):
                out[item["home"]] = item
    return out


def first_sentence(text):
    text = str(text or "").strip()
    m = re.search(r"(.+?[.!?])(\s|$)", text)
    return (m.group(1) if m else text).strip()


def role_class_of(role):
    r = (role or "").strip().lower()
    if r.startswith("related"):
        return "related"
    return "key"


def extract_relevance_tag_hint(note):
    """R6 relevance-tag hint (Extends/Limits/Boundary/Foil) if the worklist note or
    a placement mentions one — advisory only; S7 finalizes. None if none present."""
    if not note:
        return None
    low = str(note).lower()
    for tag in RELEVANCE_TAGS:
        if re.search(r"\b%s\b" % tag.lower(), low):
            return tag
    return None


def build_home_rows_ledger(row, payload_fm, holding, primary, stem, cite):
    """Per-home S7-materialization hints for the authored-ledger row. Each entry is
    self-contained (F-R8-09: `stem` + `cite` denormalized in, so S7 needs no join
    to the row level to build the `*[[<stem>]]*, <cite>` Case cell): role_class
    (key->schema-1, related->schema-2), the primary-home link, an optional
    relevance-tag hint (worklist note or placement), and author-supplied cell text."""
    placements = placements_from_payload(payload_fm)
    role_by_home = {r.get("home"): r.get("role") for r in (row.get("roles") or [])}
    note_tag = extract_relevance_tag_hint(row.get("note"))
    out = []
    for h in row.get("homes", []) or []:
        rclass = role_class_of(role_by_home.get(h))
        pl = placements.get(h) or {}
        entry = OrderedDict([
            ("home", h),
            ("role", role_by_home.get(h)),
            ("role_class", rclass),
            ("schema", "key" if rclass == "key" else "related"),
            ("stem", stem),          # F-R8-09: Case-cell wikilink target (NOT caption)
            ("cite", cite),          # F-R8-09: Case-cell cite (with year)
        ])
        if rclass == "key":
            entry["holding_cell_hint"] = pl.get("cell") or first_sentence(holding)
        else:
            entry["relevance_tag_hint"] = pl.get("tag") or note_tag
            entry["relevance_cell_hint"] = pl.get("cell")
            entry["primary_home"] = pl.get("primary_home") or primary
        out.append(entry)
    return out


# --------------------------------------------------------------------------
# staged lint validation (delta on touched files; absolute-clean on the new page)
# --------------------------------------------------------------------------

def _viol_signatures(violations):
    """A location-independent signature multiset so a *new* violation introduced
    by an inserted row is detectable even though the ambient corpus is red."""
    from collections import Counter
    return Counter((v.get("lint"), v.get("severity"), re.sub(r"\d+", "#", v.get("message", ""))[:120])
                   for v in violations)


def staged_lints_ok(staged_dir, new_page_path, staged_records, baselines, born_status):
    """Run LINT-15/16/14 over the staged tree. The new page must be absolutely
    clean; each touched existing file must not gain a NEW violation signature vs
    its pre-insert baseline. Returns (ok, findings)."""
    findings = []

    # (1) the new page — absolute clean on LINT-15 (case) + LINT-16
    for mod, name in ((lint15, "LINT-15"), (lint16, "LINT-16")):
        v = mod.check_file(new_page_path)
        for row in v:
            findings.append({"file": lint_common.relpath(new_page_path), "lint": name,
                             "severity": row["severity"], "message": row["message"]})

    # (1b) LINT-14 page<->record binding on the new page
    v14 = lint14.check_page(new_page_path, staged_records)
    if born_status == "draft" and not v14:
        # LINT-14 skips draft pages; run the binding sub-check explicitly
        v14 = _draft_binding_check(new_page_path, staged_records)
    for row in v14:
        findings.append({"file": lint_common.relpath(new_page_path), "lint": "LINT-14",
                         "severity": row["severity"], "message": row["message"]})

    # (2) touched existing files — delta (no NEW signature)
    for path, before in baselines.items():
        after = lint16.check_file(path) + lint15.check_file(path)
        before_sig = _viol_signatures(before)
        after_sig = _viol_signatures(after)
        gained = after_sig - before_sig
        for (lint, sev, msg), n in gained.items():
            findings.append({"file": lint_common.relpath(path), "lint": lint,
                             "severity": sev, "message": "NEW (%dx): %s" % (n, msg)})

    # Born-conformant contract: the new page must carry ZERO LINT-15/16/14
    # findings at ANY severity (LINT-15's case-skeleton drift is MEDIUM, so a HIGH
    # gate would let a mis-sequenced BIRAC page through), and no touched file may
    # gain a NEW signature. Any finding fails the gate.
    ok = len(findings) == 0
    return ok, findings


def _draft_binding_check(page_path, records):
    """R8 draft mode: LINT-14 skips drafts, so validate the page<->record binding
    (rid==stem, record present, not a stub) directly."""
    text = serializer.read_markdown(page_path)
    fm, _b, _s = serializer.split_frontmatter(text)
    out = []
    stem = os.path.splitext(os.path.basename(page_path))[0]
    rid = lint14.page_record_id(page_path, fm)
    if rid != stem:
        out.append(lint_common.make_violation("LINT-14", page_path, 1, lint_common.HIGH,
                   "draft binding: lake.record_id=%r != stem %r [A6]" % (rid, stem)))
    if rid not in records:
        out.append(lint_common.make_violation("LINT-14", page_path, 1, lint_common.HIGH,
                   "draft binding: no staged lake record %r" % rid))
    else:
        _p, rec = records[rid]
        if rec.get("stub"):
            out.append(lint_common.make_violation("LINT-14", page_path, 1, lint_common.HIGH,
                       "draft binding: staged record still carries stub:true [A6]"))
    return out


# --------------------------------------------------------------------------
# lake-derived promotion-state classification (F-R8-02: completion is detected
# from lake+page state, NOT from the mutable manifest `renames` array)
# --------------------------------------------------------------------------

def promotion_marker(record):
    return ((record.get("provenance") or {}).get("s6_promotion") or {}).get("from_record_id")


def promoted_at_candidates(lake_root, record_id, candidate_stems):
    """Fast path — look only at the named candidate stems (no full scan)."""
    for stem in candidate_stems:
        if not stem:
            continue
        p = lake_record_path(lake_root, stem)
        if os.path.exists(p):
            try:
                rec = read_json(p)
            except Exception:
                continue
            if promotion_marker(rec) == record_id:
                return p, rec
    return None, None


def promoted_record_scan(lake_root, record_id):
    """Fallback — full scan over page-backed records (stem has no `--`) for the
    s6_promotion marker. Used only when old json is gone and the candidate check
    missed (a disambiguated stem after a crash) — rare."""
    for p in sorted(glob.glob(os.path.join(lake_cases_dir(lake_root), "*.json"))):
        stem = os.path.basename(p)[:-5]
        if "--" in stem:
            continue
        try:
            rec = read_json(p)
        except Exception:
            continue
        if promotion_marker(rec) == record_id:
            return p, rec
    return None, None


def manifest_has_rename(manifest, record_id, stem):
    for r in manifest.get("renames", []) or []:
        old = r.get("old") or r.get("from")
        new = r.get("new") or r.get("to")
        if old == record_id and new == stem:
            return True
    return False


def ledger_has_authored(ledger_path, record_id, stem):
    lp = ledger_path if os.path.isabs(ledger_path) else os.path.join(REPO_ROOT, ledger_path)
    if not os.path.exists(lp):
        return False
    with open(lp, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if (row.get("record_id_before") == record_id
                    and row.get("record_id_after") == stem
                    and row.get("terminal") in ("authored", "reconciled")):
                return True
    return False


def global_record_id_conflict(lake_root, stem, from_record_id):
    """F-R8-12: a promotion to `stem` is unsafe if some OTHER lake record already
    holds record_id == stem (not our own prior promotion of this row). Returns the
    conflicting path or None."""
    p = lake_record_path(lake_root, stem)
    if not os.path.exists(p):
        return None
    try:
        rec = read_json(p)
    except Exception:
        return p
    # our own prior promotion of this exact row is not a conflict (roll-forward)
    if promotion_marker(rec) == from_record_id:
        return None
    return p


# --------------------------------------------------------------------------
# plan (dry-run) + commit (--write)
# --------------------------------------------------------------------------

def refuse(code, message, **extra):
    r = {"ok": False, "refused": True, "code": code, "message": message}
    r.update(extra)
    return r


def _ledger_row(record_id, stem, caption, projection, holding, row, payload_fm,
                primary, page_rel, born_status, as_of, reconciled=False):
    """The authored (or reconciled) ledger row — the owed-row record S7 materializes
    from + the per-page fields the Case-Index generator reads."""
    cite = projection.get("citation")
    entry = OrderedDict([
        ("terminal", "reconciled" if reconciled else "authored"),
        ("record_id_before", record_id),
        ("record_id_after", stem),
        ("caption", caption),
        ("cite", cite),
        ("year", projection.get("year")),
        ("court", projection.get("court")),
        ("authority_weight", projection.get("authority_weight")),
        ("opinion_url", opinion_url(projection)),
        ("holding", holding),
        ("leg", row.get("leg")),
        ("prong", row.get("prong")),
        ("basis", row.get("basis")),
        ("homes", row.get("homes")),
        ("roles", row.get("roles")),
        ("primary_home", primary),
        ("home_rows", build_home_rows_ledger(row, payload_fm, holding, primary, stem, cite)),
        ("worklist_note", row.get("note")),
        ("page", page_rel),
        ("born_status", born_status),
        ("lints_run", ["LINT-15", "LINT-16", "LINT-14"]),
        ("as_of", as_of),
        ("ts", as_of_to_iso(as_of)),
        ("lane", "s6-r8-mint"),
        ("model", "claude-opus-4-8"),
    ])
    if reconciled:
        entry["reconciled_from"] = "crash-tail (page+lake-rename landed; manifest/ledger completed)"
    return entry


def plan_mint(record_id, payload_path, worklist_path, lake_root, content_root,
              ledger_path, born_status, as_of):
    """Build the full mint plan and validate the staged state, WITHOUT writing.
    Returns a result dict; `ok` True means a --write would commit. Completion is
    LAKE-DERIVED (F-R8-02): the on-disk state is classified into fresh /
    already-authored / crash-tail-reconcile / wedged-partial."""
    worklist = load_worklist(worklist_path)
    row = worklist_row(worklist, record_id)
    if row is None:
        return refuse(REFUSE_WORKLIST_ABSENT,
                      "record_id %r is not in the signed R8 worklist" % record_id)

    manifest = load_manifest(lake_root)

    caption = row.get("caption") or record_id
    old_path = lake_record_path(lake_root, record_id)
    old_exists = os.path.exists(old_path)
    # NOTE (CR-02): the homes[]/roles[] bijection gate (F-R8-06) is deferred to the
    # FRESH path below — it must NOT run before the already-authored/crash-tail
    # classification, or a post-authoring worklist edit would break the documented
    # idempotent no-op of an already-promoted row.

    # ---- POST-COMMIT / CRASH-TAIL classification (old stub json gone) ----------
    if not old_exists:
        prom_path, promoted_rec = promoted_at_candidates(lake_root, record_id, [caption])
        if promoted_rec is None:
            prom_path, promoted_rec = promoted_record_scan(lake_root, record_id)
        if promoted_rec is None:
            return refuse(REFUSE_NO_LAKE_RECORD,
                          "no lake record at %s and no promoted record carries its "
                          "s6_promotion marker — nothing to author" % lint_common.relpath(old_path))
        stem = promoted_rec.get("record_id")
        page_abs = os.path.join(content_root, "cases", stem + ".md")
        page_rel = os.path.relpath(page_abs, os.path.dirname(content_root))
        page_exists = os.path.exists(page_abs)
        manifest_entry = manifest_has_rename(manifest, record_id, stem)
        ledger_done = ledger_has_authored(ledger_path, record_id, stem)
        if not page_exists:
            return refuse(REFUSE_WEDGED_PARTIAL,
                          "lake rename landed (%s.json present, old gone) but page %s is missing "
                          "— half-committed; refusing (manual reconcile)" % (stem, page_rel))
        if manifest_entry and ledger_done:
            return {"ok": True, "refused": False, "already_authored": True,
                    "record_id": record_id, "stem": stem, "page": page_rel}
        # crash-tail: page + lake-rename landed, but manifest and/or ledger did not.
        # Roll forward the missing steps (F-R8-02(b)). Rebuild the ledger row from
        # the re-supplied payload + the on-disk promoted record.
        if not payload_path or not os.path.exists(payload_path):
            return refuse(REFUSE_PAYLOAD_INVALID,
                          "crash-tail reconcile of %r needs --payload to rebuild the ledger row"
                          % record_id)
        payload_fm, _body = parse_payload(payload_path)
        try:
            projection = s2project.project_record(promoted_rec)
        except ValueError as exc:
            return refuse("projection-failed", str(exc))
        if not projection.get("citation") and record_is_slip_only(promoted_rec):
            sc = derive_slip_cite(promoted_rec)
            if sc:
                projection["citation"] = sc
        holding = payload_fm.get("holding") or ""
        primary = primary_home_link(row)
        rc_born = promoted_rec.get("status") or born_status
        ledger = _ledger_row(record_id, stem, caption, projection, holding, row, payload_fm,
                             primary, page_rel, rc_born, as_of, reconciled=True)
        return {
            "ok": True, "refused": False, "already_authored": False, "mode": "reconcile",
            "record_id": record_id, "stem": stem, "stem_note": None, "born_status": rc_born,
            "page": {"path": page_rel, "abs": page_abs, "text": None},
            "reconcile": {"manifest_pending": not manifest_entry, "ledger_pending": not ledger_done},
            "manifest": {"path": manifest_path(lake_root),
                         "rename_entry": {"old": record_id, "new": stem, "as_of": as_of,
                                          "by": "s6-r8-mint-reconcile"},
                         "record": promoted_rec},
            "ledger": {"path": ledger_path, "row": ledger},
            "file_plans": [], "lint_findings": [], "projection": projection,
        }

    # ---- FRESH path (old stub json present) ------------------------------------
    record = read_json(old_path)

    status = record.get("status")
    if status not in ACCEPT_STATUSES:
        return refuse(REFUSE_WRONG_STATUS,
                      "lake status %r not in accepted %s" % (status, ACCEPT_STATUSES),
                      status=status)
    # F-R8-01: mint iff the record is a stub. A page-backed (non-stub) record is
    # refused — never promoted-over/deleted.
    if not record.get("stub"):
        return refuse(REFUSE_NOT_A_STUB,
                      "lake record %r is not a stub (stub!=true) — R8 mints only from "
                      "verified stubs; a page-backed record must not be re-promoted [A6/F-R8-01]"
                      % record_id)

    # F-R8-06 (CR-02: fresh-path only — after the already-authored/crash-tail
    # classification, so a post-authoring worklist edit never disturbs the no-op):
    # homes[]/roles[] must be in bijection — no silent Key default.
    desync = homes_roles_desync(row)
    if desync:
        return refuse(REFUSE_HOMES_ROLES_DESYNC, desync)

    special = row.get("special") or []
    if isinstance(special, str):
        special = [special]
    if "history-render" in special:
        fiv = (record.get("treatment") or {}).get("field_i_validity")
        if fiv in (None, "", "good_law"):
            return refuse("history-class-mismatch",
                          "special=history-render but Field-I is %r (not a history/superseded "
                          "class) — a history page must not fight the R15 banner [PRACTICES §7]"
                          % (fiv,), field_i_validity=fiv)

    caption = row.get("caption") or record.get("identity", {}).get("case_name") or record_id
    try:
        stem, stem_note = choose_stem(caption, record, content_root)
    except ValueError as exc:
        code = REFUSE_STEM_RESERVED if "reserved" in str(exc) else REFUSE_STEM_COLLISION
        return refuse(code, str(exc))

    # F-R8-12: a foreign lake record already holding record_id==stem would duplicate.
    conflict = global_record_id_conflict(lake_root, stem, record_id)
    if conflict:
        return refuse(REFUSE_RECORD_ID_COLLISION,
                      "lake record %s already holds record_id==%r (not this row's promotion) — "
                      "promotion would duplicate the record_id [A6/F-R8-12]"
                      % (lint_common.relpath(conflict), stem))
    # dual-record wedge: our OWN prior promotion at stem AND the old stub still present
    _wp, wedged = promoted_at_candidates(lake_root, record_id, [stem])
    if wedged is not None:
        return refuse(REFUSE_WEDGED_PARTIAL,
                      "both the stub %r and our promoted record %r exist (os.remove orphan / "
                      "dual-record) — refusing; reconcile manually" % (record_id, stem))

    # F-R8-03: the manifest must carry a record for this row (ground-truth, fail-closed).
    if manifest_record(manifest, record_id) is None:
        return refuse(REFUSE_MANIFEST_MISSING_RECORD,
                      "lake record %r is absent from the manifest — manifest ground-truth "
                      "broken; refusing to promote [F-R8-03]" % record_id)

    # projection + citation completeness gate
    promoted = promote_record(record, stem, born_status, as_of)
    try:
        projection = s2project.project_record(promoted)
    except ValueError as exc:
        return refuse("projection-failed", str(exc))
    # slip-only support: an EXPLICIT citations.slip_only marker (S2 A3 precedent)
    # lets a real case whose reporter cite does not exist yet mint with an honest
    # slip form; `record-missing-citation` stays exactly as-is for UNMARKED rows.
    slip_only = record_is_slip_only(record)
    slip_cite = None
    if not projection.get("citation"):
        if slip_only:
            slip_cite = derive_slip_cite(promoted)
            if not slip_cite:
                return refuse(REFUSE_SLIP_INCOMPLETE,
                              "record %r is slip_only but its identity lacks a docket AND a "
                              "court/year — cannot derive an honest slip cite; complete "
                              "identity before mint" % record_id)
        else:
            return refuse(REFUSE_MISSING_CITATION,
                          "projected citation is empty for %r — the stub's citations lane "
                          "must be populated (S2 builder) before R8 mint" % record_id)

    # payload
    if not payload_path or not os.path.exists(payload_path):
        return refuse(REFUSE_PAYLOAD_INVALID, "payload file not found: %r" % payload_path)
    payload_fm, body = parse_payload(payload_path)
    body_errs = validate_payload_body(body, stem)
    if body_errs:
        return refuse(REFUSE_PAYLOAD_INVALID, "payload body failed validation",
                      errors=body_errs)

    frontmatter, projection = assemble_frontmatter(promoted, row, payload_fm, stem)
    if slip_cite:
        # inject the honest slip cite into the frontmatter + projection (the
        # projector emits no cite for a slip-only record) so the page's citation,
        # the Case-cell, and the ledger all carry the slip form.
        frontmatter["citation"] = slip_cite
        projection["citation"] = slip_cite
    page_text = render_page(frontmatter, body)
    page_abs = os.path.join(content_root, "cases", stem + ".md")
    page_rel = os.path.relpath(page_abs, os.path.dirname(content_root))

    # loop-2 (E2/E3): the CLI writes NO index/homes rows — only the born page.
    holding = payload_fm.get("holding") or ""
    primary = primary_home_link(row)
    file_plans = []

    # homes existence validation — a missing home target is refused (fail-closed)
    for h in row.get("homes", []) or []:
        home_abs = resolve_home_file(h, content_root)
        if not os.path.exists(home_abs):
            return refuse(REFUSE_HOME_MISSING, "homes[] page not found: %s" % h)

    ledger = _ledger_row(record_id, stem, caption, projection, holding, row, payload_fm,
                         primary, page_rel, born_status, as_of)

    plan = {
        "ok": None, "refused": False, "already_authored": False, "mode": "fresh",
        "record_id": record_id, "stem": stem, "stem_note": stem_note,
        "born_status": born_status,
        "page": {"path": page_rel, "abs": page_abs, "text": page_text},
        "lake_rename": {"old": old_path, "new": lake_record_path(lake_root, stem),
                        "record": promoted},
        "manifest": {"path": manifest_path(lake_root),
                     "rename_entry": {"old": record_id, "new": stem, "as_of": as_of,
                                      "by": "s6-r8-mint"}},
        "file_plans": file_plans,
        "ledger": {"path": ledger_path, "row": ledger},
        "projection": projection,
    }

    # stage into a temp mirror and lint (only the born page under loop-2)
    ok, findings = _stage_and_lint(plan, lake_root, content_root, born_status)
    plan["lint_findings"] = findings
    plan["baselines_checked"] = [lint_common.relpath(fp["path"]) for fp in file_plans]
    if not ok:
        plan["ok"] = False
        plan["refused"] = True
        plan["code"] = REFUSE_LINT_FAILED
        plan["message"] = "staged LINT-15/16/14 introduced HIGH findings"
        return plan
    plan["ok"] = True
    return plan


def _stage_and_lint(plan, lake_root, content_root, born_status):
    """Stage the new page + touched files + renamed lake record into a temp mirror
    and run the lints there (never mutating the real tree). Returns (ok, findings)."""
    import tempfile
    with tempfile.TemporaryDirectory(prefix="s6-mint-stage-") as tmp:
        # mirror lake/cases into tmp, apply the rename, so LINT-14 sees staged state
        staged_records = _staged_records(lake_root, plan)
        # write the new page to a temp path
        page_abs = os.path.join(tmp, os.path.basename(plan["page"]["path"]))
        write_text_atomic(page_abs, plan["page"]["text"])
        # write touched files to temp copies and lint them there
        baselines = {}
        for fp in plan["file_plans"]:
            orig = fp["path"]
            tmp_copy = os.path.join(tmp, "touched_" + os.path.basename(orig))
            baselines[tmp_copy] = lint16.check_file(orig) + lint15.check_file(orig)
            write_text_atomic(tmp_copy, fp["new_text"])
        ok, findings = staged_lints_ok(tmp, page_abs, staged_records, baselines, born_status)
        # relabel temp file paths in findings back to the real target for clarity
        for f in findings:
            f["file"] = f["file"].replace("touched_", "")
        return ok, findings


def _staged_records(lake_root, plan):
    """LINT-14 record map with the promotion applied: drop old rid, add stem."""
    records = {}
    for p in sorted(glob.glob(os.path.join(lake_cases_dir(lake_root), "*.json"))):
        try:
            rec = read_json(p)
        except Exception:
            continue
        rid = rec.get("record_id")
        if rid:
            records[rid] = (p, rec)
    old = os.path.basename(plan["lake_rename"]["old"])[:-5]
    records.pop(old, None)
    records[plan["stem"]] = (plan["lake_rename"]["new"], plan["lake_rename"]["record"])
    return records


def _append_ledger(lpath_abs, row):
    with open(lpath_abs, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def _roll_forward(plan, lake_root):
    """F-R8-02(b): complete a crash-tail row (page + lake-rename already on disk;
    manifest and/or ledger missing) by finishing steps 4-5 only, journaled as
    `reconciled`. Manifest write is atomic; ledger append is idempotent (guarded by
    the ledger-has-authored check at plan time)."""
    rc = plan.get("reconcile", {})
    if rc.get("manifest_pending"):
        mpath = plan["manifest"]["path"]
        backup = None
        if os.path.exists(mpath):
            with open(mpath, "rb") as f:
                backup = f.read()
        try:
            manifest = read_json(mpath)
            _apply_manifest_promotion(manifest, plan)
            write_json_atomic(mpath, manifest)
        except Exception as exc:
            if backup is not None:
                with open(mpath, "wb") as f:
                    f.write(backup)
            raise RuntimeError("reconcile manifest write failed and was rolled back: %s" % exc)
    if rc.get("ledger_pending"):
        lpath = plan["ledger"]["path"]
        lpath_abs = lpath if os.path.isabs(lpath) else os.path.join(REPO_ROOT, lpath)
        os.makedirs(os.path.dirname(lpath_abs), exist_ok=True)
        _append_ledger(lpath_abs, plan["ledger"]["row"])
    return {"committed": True, "reconciled": True, "stem": plan["stem"],
            "page": plan["page"]["abs"]}


def commit_plan(plan, lake_root):
    """Apply a validated plan atomically with reverse-order rollback. Fresh order:
    page, lake rename (marker set BEFORE remove — F-R8-02(c)), manifest, ledger
    (last). A `reconcile` plan rolls the missing steps forward instead. On any
    failure the page, both lake records, the manifest, and the ledger are all
    byte-restored."""
    if not plan.get("ok"):
        raise RuntimeError("refusing to commit an un-ok plan")
    if plan.get("mode") == "reconcile":
        return _roll_forward(plan, lake_root)

    backups = []       # (path, original_bytes_or_None)
    renamed = None     # {old,new,old_bytes,new_existed,removed_old}
    ledger_pre = None  # (path, pre_size)

    def backup(path):
        if os.path.exists(path):
            with open(path, "rb") as f:
                backups.append((path, f.read()))
        else:
            backups.append((path, None))

    try:
        # 1. new page
        page_abs = plan["page"]["abs"]
        os.makedirs(os.path.dirname(page_abs), exist_ok=True)
        backup(page_abs)
        write_text_atomic(page_abs, plan["page"]["text"])
        # 2. index + homes (empty under loop-2)
        for fp in plan["file_plans"]:
            backup(fp["path"])
            write_text_atomic(fp["path"], fp["new_text"])
        # 3. lake rename: write new record, then remove old — but record the
        # rollback marker BEFORE the remove so an os.remove failure cannot orphan
        # the new record (F-R8-02(c)); skip the remove when old==new (F-R8-01).
        old = plan["lake_rename"]["old"]
        new = plan["lake_rename"]["new"]
        with open(old, "rb") as f:
            old_bytes = f.read()
        new_existed = os.path.exists(new)
        renamed = {"old": old, "new": new, "old_bytes": old_bytes,
                   "new_existed": new_existed, "removed_old": False}
        write_json_atomic(new, plan["lake_rename"]["record"])
        if os.path.abspath(old) != os.path.abspath(new):
            os.remove(old)
            renamed["removed_old"] = True
        # 4. manifest
        mpath = plan["manifest"]["path"]
        backup(mpath)
        manifest = read_json(mpath)
        _apply_manifest_promotion(manifest, plan)
        write_json_atomic(mpath, manifest)
        # 5. ledger append LAST (never first — a crash before this must not
        # fabricate an authored claim; the completion marker is the lake rename)
        lpath = plan["ledger"]["path"]
        lpath_abs = lpath if os.path.isabs(lpath) else os.path.join(REPO_ROOT, lpath)
        os.makedirs(os.path.dirname(lpath_abs), exist_ok=True)
        ledger_pre = (lpath_abs, os.path.getsize(lpath_abs) if os.path.exists(lpath_abs) else 0)
        _append_ledger(lpath_abs, plan["ledger"]["row"])
        return {"committed": True, "page": page_abs, "stem": plan["stem"]}
    except Exception as exc:  # reverse-order rollback
        if ledger_pre is not None:
            lp, sz = ledger_pre
            with open(lp, "r+", encoding="utf-8") as f:
                f.truncate(sz)
        if renamed is not None:
            if not renamed["new_existed"] and os.path.exists(renamed["new"]):
                os.remove(renamed["new"])
            if renamed["removed_old"]:
                with open(renamed["old"], "wb") as f:
                    f.write(renamed["old_bytes"])
        for path, original in reversed(backups):
            if original is None:
                if os.path.exists(path):
                    os.remove(path)
            else:
                with open(path, "wb") as f:
                    f.write(original)
        raise RuntimeError("commit failed and was rolled back: %s" % exc)


def _apply_manifest_promotion(manifest, plan):
    """F-R8-04: the manifest is AUTHORITATIVE live state. On promotion, append the
    rename entry AND update the record's stale fields (mirror what a fresh scaffold
    would emit for a page-backed record) AND stamp file-level provenance without
    clobbering the `generated_*` fields."""
    old = plan["manifest"]["rename_entry"]["old"]
    new = plan["manifest"]["rename_entry"]["new"]
    as_of = plan["manifest"]["rename_entry"].get("as_of")
    if not manifest_has_rename(manifest, old, new):
        manifest.setdefault("renames", []).append(plan["manifest"]["rename_entry"])
    rec = manifest_record(manifest, old) or manifest_record(manifest, new)
    if rec is not None:
        rec["record_id"] = new
        rec["stub"] = False
        rec["status"] = plan["born_status"]
        rec["page_path"] = plan["page"]["path"]
        # mirror the stale scaffold fields a page-backed record would carry
        rec["slug"] = ingest_slug(new)
        rec["title"] = new
        rec["caption"] = new
        rec["record_id_status"] = "resolved"
        rec["source"] = "content/cases"
        if isinstance(rec.get("lane_status"), dict):
            rec["lane_status"]["identity"] = "complete"
    # file-level provenance stamp (never touches generated_by/generated_at/build_id)
    mutations = manifest.setdefault("s6_mutations", [])
    mutations.append({"old": old, "new": new, "as_of": as_of, "by": "s6-r8-mint"})


def ingest_slug(value):
    """Mirror scripts/s2/ingest.py::slugify for the promoted record's `slug` field."""
    value = value.strip().lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "case"


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _abs(path):
    return path if os.path.isabs(path) else os.path.join(REPO_ROOT, path)


def run_cli(args):
    worklist_path = _abs(args.worklist)
    lake_root = _abs(args.lake_root)
    content_root = _abs(args.content_root)
    ledger_path = _abs(args.ledger)
    payload = _abs(args.payload) if args.payload else None

    as_of = None
    if args.write or args.as_of:
        try:
            as_of = norm_as_of(args.as_of or "")
        except ValueError as exc:
            sys.stderr.write("REFUSED [as-of-required]: %s\n" % exc)
            return 2
    else:
        as_of = args.as_of or "DRY-RUN"

    plan = plan_mint(args.row, payload, worklist_path, lake_root, content_root,
                     ledger_path, args.born_status, as_of)

    if args.summary_json:
        printable = {k: v for k, v in plan.items() if k not in ("projection",)}
        if "page" in printable and isinstance(printable["page"], dict):
            printable["page"] = {kk: vv for kk, vv in printable["page"].items() if kk != "text"}
        if "lake_rename" in printable:
            printable["lake_rename"] = {"old": lint_common.relpath(plan["lake_rename"]["old"]),
                                        "new": lint_common.relpath(plan["lake_rename"]["new"])}
        printable["file_plans"] = [{"path": lint_common.relpath(fp["path"]), "kind": fp["kind"]}
                                   for fp in plan.get("file_plans", [])]
        sys.stdout.write(json.dumps(printable, ensure_ascii=False, default=str) + "\n")

    _print_plan(plan, sys.stderr)

    if plan.get("refused"):
        return 2
    if plan.get("already_authored"):
        sys.stderr.write("already-authored (no-op): %s\n" % plan["stem"])
        return 0
    if args.write:
        result = commit_plan(plan, lake_root)
        verb = "RECONCILED" if result.get("reconciled") else "COMMITTED"
        sys.stderr.write("%s %s -> %s\n" % (verb, plan["record_id"], result["page"]))
        return 0
    if plan.get("mode") == "reconcile":
        sys.stderr.write("DRY-RUN reconcile pending %s (use --write --as-of <ISO> to roll forward)\n"
                         % (plan.get("reconcile"),))
        return 0
    sys.stderr.write("DRY-RUN ok (use --write --as-of <ISO> to commit)\n")
    return 0


def _print_plan(plan, stream):
    if plan.get("refused"):
        stream.write("REFUSED [%s]: %s\n" % (plan.get("code"), plan.get("message")))
        for e in plan.get("errors", []) or []:
            stream.write("  - %s: %s\n" % (e.get("code"), e.get("message")))
        for f in plan.get("lint_findings", []) or []:
            stream.write("  LINT %s [%s] %s: %s\n"
                         % (f["lint"], f["severity"], f["file"], f["message"]))
        return
    if plan.get("already_authored"):
        return
    mode = plan.get("mode", "fresh")
    stream.write("PLAN [%s] %s -> stem %r (born %s)\n"
                 % (mode, plan["record_id"], plan["stem"], plan["born_status"]))
    if plan.get("stem_note"):
        stream.write("  stem: %s\n" % plan["stem_note"])
    stream.write("  page: %s\n" % plan["page"]["path"])
    if mode == "reconcile":
        stream.write("  reconcile pending: %s\n" % plan.get("reconcile"))
    else:
        stream.write("  lake rename: %s -> %s\n" % (lint_common.relpath(plan["lake_rename"]["old"]),
                                                    lint_common.relpath(plan["lake_rename"]["new"])))
        stream.write("  staged lint findings (any = fail): %d\n" % len(plan.get("lint_findings", [])))
    stream.write("  ledger: %s (%s)\n"
                 % (lint_common.relpath(_abs(plan["ledger"]["path"])), plan["ledger"]["row"]["terminal"]))


# --------------------------------------------------------------------------
# specimen + self-tests
# --------------------------------------------------------------------------

def specimen_test():
    """The born-conformant exhibit: US v. Smith (2024). (a) the payload-validator
    passes over the live page body; (b) the S2 projector over its lake record
    deep-equals the live page's managed frontmatter, modulo lake.status."""
    page = os.path.join(REPO_ROOT, "content", "cases", "United States v. Smith (2024).md")
    rec_path = os.path.join(REPO_ROOT, LAKE_REL, "cases", "United States v. Smith (2024).json")
    text = serializer.read_markdown(page)
    fm, body, _ = serializer.split_frontmatter(text)
    stem = "United States v. Smith (2024)"

    body_errs = validate_payload_body(body, stem)
    a_ok = not body_errs

    l15 = lint15.check_file(page)
    l16 = lint16.check_file(page)
    skel_ok = not l15 and not l16

    record = read_json(rec_path)
    projection = s2project.project_record(record)
    managed = serializer.managed_subset(fm)
    diffs = serializer.diff_paths(managed, projection)
    # the only permitted delta is lake.status (verified page vs draft/under_review born)
    proj_ok = all(d.startswith("lake.status") for d in diffs) if diffs else True

    sys.stderr.write("[specimen] payload-body validator      -> %s (%d errs)\n"
                     % ("OK" if a_ok else "FAIL", len(body_errs)))
    for e in body_errs:
        sys.stderr.write("           %s: %s\n" % (e["code"], e["message"]))
    sys.stderr.write("[specimen] LINT-15/16 on live page     -> %s (%d/%d)\n"
                     % ("OK" if skel_ok else "FAIL", len(l15), len(l16)))
    sys.stderr.write("[specimen] projector == managed fm     -> %s (diffs=%s)\n"
                     % ("OK" if proj_ok else "FAIL", diffs))
    ok = a_ok and skel_ok and proj_ok
    sys.stderr.write("[specimen] %s\n" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def _write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def self_test():
    """End-to-end fixtures in private temp sandboxes (no real-lake mutation): the
    happy path + promotion side-effects, idempotent no-op, collision, history
    class, and every refusal + rollback path — including the loop-3 additions:
    non-stub gate (F-R8-01), lake-derived crash-tail reconcile + wedged-partial
    (F-R8-02), manifest cross-check + record-flip (F-R8-03), commit-time
    failure-injection rollback (F-R8-05), homes/roles desync (F-R8-06), and
    global record_id collision (F-R8-12)."""
    import shutil
    import tempfile
    results = []

    def check(label, cond):
        results.append((label, bool(cond)))
        sys.stderr.write("[self-test] %-46s -> %s\n" % (label, "OK" if cond else "FAIL"))

    fx = FIXTURES_DIR
    as_of = "2026-07-07T00:00:00Z"
    payload = os.path.join(fx, "payload-alpha.md")
    payload_collision = os.path.join(fx, "payload-collision.md")
    payload_hist = os.path.join(fx, "payload-history.md")
    payload_bad = os.path.join(fx, "payload-bad-skeleton.md")

    def setup(base):
        """Build a fresh sandbox lake+content+manifest+homes; return its paths."""
        lr = os.path.join(base, "lake")
        cr = os.path.join(base, "content")
        os.makedirs(os.path.join(lr, "cases"))
        os.makedirs(os.path.join(cr, "cases"))
        os.makedirs(os.path.join(cr, "doctrine"))
        for name, rid in (("alpha", "fixture-alpha--900001"),
                          ("collision", "fixture-collision--900002"),
                          ("wrongstatus", "fixture-wrongstatus--900003"),
                          ("history", "fixture-history--900004")):
            shutil.copy(os.path.join(fx, "stub-fixture-%s.json" % name),
                        os.path.join(lr, "cases", rid + ".json"))
        shutil.copy(os.path.join(fx, "manifest-fixture.json"), os.path.join(lr, MANIFEST_NAME))
        shutil.copy(os.path.join(fx, "home-key-r6.md"), os.path.join(cr, "doctrine", "Fixture Doctrine.md"))
        shutil.copy(os.path.join(fx, "home-related-r6.md"), os.path.join(cr, "doctrine", "Fixture Related Home.md"))
        shutil.copy(os.path.join(fx, "existing-collision-page.md"),
                    os.path.join(cr, "cases", "Fixture Collision Case.md"))
        return {"lr": lr, "cr": cr, "ledger": os.path.join(base, "led.jsonl"),
                "wl": os.path.join(fx, "worklist-fixture.json")}

    def mint(s, rid, pl, born="under_review", wl=None):
        return plan_mint(rid, pl, wl or s["wl"], s["lr"], s["cr"], s["ledger"], born, as_of)

    with tempfile.TemporaryDirectory(prefix="s6-selftest-") as root:
        # ---- group A: refusal gates (one shared sandbox; these do not write) ----
        a = setup(os.path.join(root, "A"))
        check("worklist-absent refusal",
              mint(a, "not-a-row--000000", payload).get("code") == REFUSE_WORKLIST_ABSENT)
        check("wrong-status refusal",
              mint(a, "fixture-wrongstatus--900003", payload).get("code") == REFUSE_WRONG_STATUS)

        # F-R8-01: non-stub (page-backed) record is refused, never promoted-over.
        nonstub = read_json(os.path.join(fx, "stub-fixture-alpha.json"))
        nonstub.update({"record_id": "fixture-nonstub--900005", "stub": False, "status": "verified"})
        nonstub["identity"]["case_name"] = "Fixture Nonstub Case"
        _write_json(os.path.join(a["lr"], "cases", "fixture-nonstub--900005.json"), nonstub)
        wl_ns = os.path.join(root, "wl-nonstub.json")
        _write_json(wl_ns, {"rows": [{"record_id": "fixture-nonstub--900005",
                    "caption": "Fixture Nonstub Case", "leg": "roster", "prong": "a",
                    "homes": ["doctrine/Fixture Doctrine.md"],
                    "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]}]})
        check("non-stub refusal (F-R8-01)",
              mint(a, "fixture-nonstub--900005", payload, wl=wl_ns).get("code") == REFUSE_NOT_A_STUB)

        # F-R8-06: homes[]/roles[] desync (home with no role) is refused, no Key default.
        wl_desync = os.path.join(root, "wl-desync.json")
        _write_json(wl_desync, {"rows": [{"record_id": "fixture-alpha--900001",
                    "caption": "Fixture Alpha Case", "leg": "roster", "prong": "a",
                    "homes": ["doctrine/Fixture Doctrine.md", "doctrine/Fixture Related Home.md"],
                    "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]}]})
        check("homes/roles desync refusal (F-R8-06)",
              mint(a, "fixture-alpha--900001", payload, wl=wl_desync).get("code") == REFUSE_HOMES_ROLES_DESYNC)

        # F-R8-03 plan-time: a lake stub absent from the manifest is refused.
        nom = read_json(os.path.join(fx, "stub-fixture-alpha.json"))
        nom.update({"record_id": "fixture-nomanifest--900006"})
        nom["identity"]["case_name"] = "Fixture Nomanifest Case"
        _write_json(os.path.join(a["lr"], "cases", "fixture-nomanifest--900006.json"), nom)
        wl_nom = os.path.join(root, "wl-nomanifest.json")
        _write_json(wl_nom, {"rows": [{"record_id": "fixture-nomanifest--900006",
                    "caption": "Fixture Nomanifest Case", "leg": "roster", "prong": "a",
                    "homes": ["doctrine/Fixture Doctrine.md"],
                    "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]}]})
        check("manifest-missing-record refusal (F-R8-03)",
              mint(a, "fixture-nomanifest--900006", payload, wl=wl_nom).get("code")
              == REFUSE_MANIFEST_MISSING_RECORD)

        # ---- group B: happy path + commit side-effects + idempotency ----
        b = setup(os.path.join(root, "B"))
        p = mint(b, "fixture-alpha--900001", payload)
        check("happy-path plan ok (mode fresh)", p.get("ok") and p.get("mode") == "fresh")
        check("happy-path stem", p.get("stem") == "Fixture Alpha Case")
        check("happy-path writes NO index/home files (loop-2)", p.get("file_plans") == [])
        check("alias row in frontmatter", "Fixture Alias" in p["page"]["text"])
        check("born under_review in page", "status: under_review" in p["page"]["text"])
        committed = commit_plan(p, b["lr"])
        check("commit created page", os.path.exists(committed["page"]))
        check("lake renamed to stem",
              os.path.exists(os.path.join(b["lr"], "cases", "Fixture Alpha Case.json"))
              and not os.path.exists(os.path.join(b["lr"], "cases", "fixture-alpha--900001.json")))
        home_key = os.path.join(b["cr"], "doctrine", "Fixture Doctrine.md")
        check("home page unmodified (no row written)",
              "Fixture Alpha Case" not in serializer.read_markdown(home_key))
        # F-R8-03: post-commit manifest carries the rename entry AND the flipped record
        mani = read_json(os.path.join(b["lr"], MANIFEST_NAME))
        check("manifest rename entry recorded (F-R8-03)",
              manifest_has_rename(mani, "fixture-alpha--900001", "Fixture Alpha Case"))
        flipped = manifest_record(mani, "Fixture Alpha Case")
        check("manifest record flipped (F-R8-03/04)",
              flipped is not None and flipped.get("stub") is False
              and flipped.get("status") == "under_review"
              and flipped.get("slug") == "fixture-alpha-case"
              and flipped.get("record_id_status") == "resolved")
        check("manifest provenance stamped, generated_* intact (F-R8-04)",
              mani.get("s6_mutations") and mani.get("generated_by") == "S6-MINT-SELFTEST-FIXTURE")
        with open(b["ledger"], encoding="utf-8") as f:
            last = [json.loads(l) for l in f if l.strip()][-1]
        check("ledger authored row appended",
              last.get("terminal") == "authored" and last.get("record_id_after") == "Fixture Alpha Case")
        check("ledger carries cite + year (generator/S7)",
              last.get("cite") == "588 U.S. 100 (2019)" and last.get("year") == 2019)
        check("ledger home_rows carry role_class + tag + denorm stem/cite (F-R8-09)",
              [hr["role_class"] for hr in last.get("home_rows", [])] == ["key", "related"]
              and last["home_rows"][1].get("relevance_tag_hint") == "Extends"
              and all(hr.get("stem") == "Fixture Alpha Case" and hr.get("cite") for hr in last["home_rows"]))
        check("idempotent already-authored (lake-derived, F-R8-02)",
              mint(b, "fixture-alpha--900001", payload).get("already_authored") is True)
        # CR-02: a post-authoring worklist edit that DESYNCS homes/roles must NOT
        # break the already-authored no-op (the desync gate is fresh-path only).
        wl_desync_b = os.path.join(root, "wl-desync-b.json")
        _write_json(wl_desync_b, {"rows": [{"record_id": "fixture-alpha--900001",
                    "caption": "Fixture Alpha Case", "leg": "roster", "prong": "a",
                    "homes": ["doctrine/Fixture Doctrine.md", "doctrine/Fixture Related Home.md"],
                    "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]}]})
        check("idempotent survives post-authoring worklist desync (CR-02)",
              mint(b, "fixture-alpha--900001", payload, wl=wl_desync_b).get("already_authored") is True)

        # ---- group C: collision + history + bad-skeleton + missing-home ----
        c = setup(os.path.join(root, "C"))
        check("collision disambiguated by year",
              mint(c, "fixture-collision--900002", payload_collision).get("stem")
              == "Fixture Collision Case (2021)")
        check("history-class plan ok",
              mint(c, "fixture-history--900004", payload_hist).get("ok") is True)
        pre = set(glob.glob(os.path.join(c["cr"], "cases", "*.md")))
        bad = mint(c, "fixture-history--900004", payload_bad)
        check("bad-skeleton refused",
              bad.get("refused") and bad.get("code") in (REFUSE_PAYLOAD_INVALID, REFUSE_LINT_FAILED))
        check("no partial write on refusal",
              set(glob.glob(os.path.join(c["cr"], "cases", "*.md"))) == pre)
        check("missing-home target refused",
              mint(c, "fixture-history--900004", payload_hist,
                   wl=os.path.join(fx, "worklist-missing-home.json")).get("code") == REFUSE_HOME_MISSING)

        # F-R8-12: a foreign lake record already holding record_id==stem is refused.
        foreign = read_json(os.path.join(fx, "stub-fixture-history.json"))
        foreign.update({"record_id": "Fixture History Case", "stub": False, "status": "verified"})
        foreign.get("provenance", {}).pop("s6_promotion", None)
        _write_json(os.path.join(c["lr"], "cases", "Fixture History Case.json"), foreign)
        check("global record_id collision refused (F-R8-12)",
              mint(c, "fixture-history--900004", payload_hist).get("code") == REFUSE_RECORD_ID_COLLISION)

        # ---- group D: commit-time failure-injection rollback (F-R8-05) ----
        d = setup(os.path.join(root, "D"))
        p = mint(d, "fixture-alpha--900001", payload)
        old_json = os.path.join(d["lr"], "cases", "fixture-alpha--900001.json")
        new_json = os.path.join(d["lr"], "cases", "Fixture Alpha Case.json")
        page_abs = p["page"]["abs"]
        snap = {
            "old": open(old_json, "rb").read(),
            "manifest": open(os.path.join(d["lr"], MANIFEST_NAME), "rb").read(),
            "ledger": (open(d["ledger"], "rb").read() if os.path.exists(d["ledger"]) else b""),
        }

        def _boom(lpath, rowdata):   # write a partial line, then fail (exercise truncate)
            with open(lpath, "a", encoding="utf-8") as f:
                f.write("PARTIAL-SHOULD-BE-ROLLED-BACK\n")
            raise RuntimeError("injected mid-commit failure")

        orig = globals()["_append_ledger"]
        globals()["_append_ledger"] = _boom
        raised = False
        try:
            commit_plan(p, d["lr"])
        except RuntimeError:
            raised = True
        finally:
            globals()["_append_ledger"] = orig
        check("failure-injection raised", raised)
        check("rollback: page absent", not os.path.exists(page_abs))
        check("rollback: old lake record byte-restored",
              os.path.exists(old_json) and open(old_json, "rb").read() == snap["old"])
        check("rollback: new lake record removed", not os.path.exists(new_json))
        check("rollback: manifest byte-restored",
              open(os.path.join(d["lr"], MANIFEST_NAME), "rb").read() == snap["manifest"])
        check("rollback: ledger byte-restored (truncated)",
              (open(d["ledger"], "rb").read() if os.path.exists(d["ledger"]) else b"") == snap["ledger"])

        # ---- group E: crash-tail reconcile + wedged-partial (F-R8-02) ----
        e = setup(os.path.join(root, "E"))
        p = mint(e, "fixture-alpha--900001", payload)
        # hand-apply ONLY steps 1-3 (page + lake rename), leaving manifest+ledger undone
        os.makedirs(os.path.dirname(p["page"]["abs"]), exist_ok=True)
        write_text_atomic(p["page"]["abs"], p["page"]["text"])
        write_json_atomic(p["lake_rename"]["new"], p["lake_rename"]["record"])
        os.remove(p["lake_rename"]["old"])
        rc = mint(e, "fixture-alpha--900001", payload)
        check("crash-tail classified as reconcile (F-R8-02)",
              rc.get("mode") == "reconcile" and rc.get("ok")
              and rc["reconcile"]["manifest_pending"] and rc["reconcile"]["ledger_pending"])
        res = commit_plan(rc, e["lr"])
        mani_e = read_json(os.path.join(e["lr"], MANIFEST_NAME))
        with open(e["ledger"], encoding="utf-8") as f:
            e_rows = [json.loads(l) for l in f if l.strip()]
        check("reconcile rolled forward manifest + ledger",
              res.get("reconciled") and manifest_has_rename(mani_e, "fixture-alpha--900001", "Fixture Alpha Case")
              and e_rows and e_rows[-1]["terminal"] == "reconciled")
        check("post-reconcile == already-authored",
              mint(e, "fixture-alpha--900001", payload).get("already_authored") is True)

        # wedged-partial: old stub AND our promoted record both present -> refuse
        w = setup(os.path.join(root, "W"))
        pw = mint(w, "fixture-alpha--900001", payload)
        write_json_atomic(os.path.join(w["lr"], "cases", "Fixture Alpha Case.json"),
                          pw["lake_rename"]["record"])   # new present WHILE old still present
        check("wedged-partial (dual-record) refused (F-R8-02)",
              mint(w, "fixture-alpha--900001", payload).get("code") == REFUSE_WEDGED_PARTIAL)

        # ---- group F: slip-only support (S2 A3) ----
        fs = setup(os.path.join(root, "F"))
        slipstub = read_json(os.path.join(fx, "stub-fixture-slip.json"))
        _write_json(os.path.join(fs["lr"], "cases", "fixture-slip--900700.json"), slipstub)
        mani = read_json(os.path.join(fs["lr"], MANIFEST_NAME))
        mani["records"].append({"record_id": "fixture-slip--900700", "stub": True,
                                "status": "verified_identity", "slug": "fixture-slip",
                                "caption": "Fixture Slip Case", "page_path": None})
        # an unmarked no-cite stub (marker removed) to prove the refusal is unchanged
        nocite = read_json(os.path.join(fx, "stub-fixture-slip.json"))
        nocite["record_id"] = "fixture-nocite--900701"
        nocite["citations"].pop("slip_only", None)
        nocite["citations"].pop("slip_only_provenance", None)
        _write_json(os.path.join(fs["lr"], "cases", "fixture-nocite--900701.json"), nocite)
        mani["records"].append({"record_id": "fixture-nocite--900701", "stub": True,
                                "status": "verified_identity", "slug": "fixture-nocite",
                                "caption": "Fixture Nocite Case", "page_path": None})
        _write_json(os.path.join(fs["lr"], MANIFEST_NAME), mani)
        wl_slip = os.path.join(root, "wl-slip.json")
        _write_json(wl_slip, {"rows": [
            {"record_id": "fixture-slip--900700", "caption": "Fixture Slip Case", "leg": "sweep",
             "prong": "a", "homes": ["doctrine/Fixture Doctrine.md"],
             "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]},
            {"record_id": "fixture-nocite--900701", "caption": "Fixture Nocite Case", "leg": "roster",
             "prong": "a", "homes": ["doctrine/Fixture Doctrine.md"],
             "roles": [{"home": "doctrine/Fixture Doctrine.md", "role": "Key"}]}]})
        p = mint(fs, "fixture-slip--900700", os.path.join(fx, "payload-slip.md"), wl=wl_slip)
        check("slip-only marked row mints (S2 A3)", p.get("ok") and not p.get("refused"))
        check("slip cite injected into frontmatter",
              "No. 23-1197, slip op. (U.S. 2026)" in (p.get("page", {}) or {}).get("text", ""))
        check("slip cite in ledger + home_rows",
              p["ledger"]["row"]["cite"] == "No. 23-1197, slip op. (U.S. 2026)"
              and p["ledger"]["row"]["home_rows"][0]["cite"] == "No. 23-1197, slip op. (U.S. 2026)")
        # UNMARKED no-cite row still refuses record-missing-citation (unchanged)
        p = mint(fs, "fixture-nocite--900701", os.path.join(fx, "payload-alpha.md"), wl=wl_slip)
        check("unmarked no-cite row still refuses (record-missing-citation)",
              p.get("code") == REFUSE_MISSING_CITATION)

    ok = all(v for _l, v in results)
    sys.stderr.write("[self-test] %s (%d/%d)\n"
                     % ("PASS" if ok else "FAIL", sum(v for _l, v in results), len(results)))
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--row", help="record_id to author (looked up in R8-WORKLIST.json)")
    parser.add_argument("--payload", help="path to the authored page BODY (scratch file)")
    parser.add_argument("--as-of", help="ISO date/datetime for journaled/ledger values (required with --write)")
    parser.add_argument("--write", action="store_true", help="guarded commit (default: dry-run)")
    parser.add_argument("--born-status", choices=BORN_STATUSES, default=DEFAULT_BORN_STATUS,
                        help="born lake.status (default under_review; see BORN-STATUS note)")
    parser.add_argument("--worklist", default=WORKLIST_REL)
    parser.add_argument("--lake-root", default=LAKE_REL)
    parser.add_argument("--content-root", default=CONTENT_REL)
    parser.add_argument("--ledger", default=LEDGER_REL)
    parser.add_argument("--summary-json", action="store_true")
    parser.add_argument("--validate-only", action="store_true",
                        help="run payload + status gates and staged lints, write nothing")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--specimen-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()
    if args.specimen_test:
        return specimen_test()
    if not args.row or not args.payload:
        parser.error("--row and --payload are required (or use --self-test / --specimen-test)")
    if args.validate_only:
        args.write = False
    return run_cli(args)


if __name__ == "__main__":
    sys.exit(main())
