#!/usr/bin/env python3
"""S2 CourtListener authority ingest builder.

Authoring and self-tests are offline. Live runs use only Python stdlib and the
CourtListener REST API v4 through typed cluster/opinion fetchers.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import random
import re
import shutil
import socket
import sqlite3  # noqa: F401 - stdlib dependency reserved for the R13 loader path.
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter


API_BASE = "https://www.courtlistener.com/api/rest/v4"
DEFAULT_CSSI_LAKE_ROOT = "/Users/johngalt/cssi-lake"
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
CONSUMER_IDENTITY = "S2-BUILDER-AUTHORING"
SCHEMA_VERSION = "s2.v1"
URL_TIMEOUT_SECONDS = 60
FETCH_RETRY_DELAYS = (5.0, 15.0, 45.0)
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}
TRAILING_YEAR_PAREN_RE = r"\s*\([^()]*(?:17|18|19|20)\d{2}\)\s*$"
TRAILING_PAREN_RE = r"\s*\([^()]*\)\s*$"
READJUDICATION_FINDINGS = ["F-S2-16", "F-S2-17", "F-S2-18"]
READJUDICATION_ADJUDICATOR = "orchestrator claude-fable-5"
S6_CANDIDATE_INTAKE_ADJUDICATOR = "orchestrator claude-fable-5 (R2 gate 2026-07-06)"
S6_CANDIDATE_SOURCE_PREFIX = "s6-candidates/"
IDENTITY_PRIMARY_CLUSTER_LIMIT = 10
IDENTITY_FALLBACK_CLUSTER_LIMIT = 3
STRONG_IDENTITY_RUNGS = {"citation", "docket_number"}
READJUDICATION_RESET_FIELDS = ("identity", "citations", "pinpoints", "progeny", "treatment", "off_cl_links")
READJUDICATION_ROSTER_KEYS = (
    "record_id",
    "record_id_status",
    "source",
    "sources",
    "source_row_index",
    "roster_key",
    "roster_key_sha1",
    "stub",
    "page_path",
    "slug",
    "title",
    "caption",
    "expected_citation",
    "parallel_cite",
    "neutral_cite",
    "court",
    "court_era",
    "court_level",
    "circuit",
    "state",
    "year",
    "date_decided",
    "docket",
    "flags",
    "mentions",
    "variant_notes",
)

STRICT_COURT_CLASSES = {"scotus", "coa", "district", "state", "other"}
COURT_CLASS_ALIASES = {
    "circuit": "coa",
    "state-high": "state",
    "state-app": "state",
}
FAIL_CLOSED_STATUSES = {"fabrication_suspected", "not_found", "blocked"}
PRESEEDED_FIELD_I_VALIDITIES = {"good_law", "history", "caution", "questioned", "superseded"}
PRESEEDED_TREATMENT_PROVENANCE = "pre-seeded new-schema treatment (planning-time projection); R6 derivation to confirm"
PRESEEDED_TREATMENT_CARRY_KEYS = (
    "as_of_content",
    "as_of_treatment",
    "composite_basis",
    "composite_basis_ref",
    "varies_by_point",
    "scope_note",
    "point_overrides",
)
TREATMENT_LANES = [
    ("lane1_negative", 200),
    ("lane2_top_cited", 25),
    ("lane3_recency", 200),
]
TREATMENT_LANE_NAMES = tuple(lane for lane, _cap in TREATMENT_LANES)
LANE_RERUN_FINDINGS = ["F-S2-28"]
MIGRATION_REF_REPAIR_FINDINGS = ["F-S2-29"]
MIGRATION_REF_REPAIR_PROVENANCE = "F-S2-29 migration reference repair"
FAIL_CLOSED_TREATMENT_REPAIR_FINDINGS = ["F-S2-31"]
FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE = "F-S2-31 fail-closed treatment repair"
FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS = ("Entick v. Carrington", "Wilkes v. Wood")
R15_FLIP_EXPECTED_COUNT = 421
R15_FLIP_GATES = [
    "schema",
    "two-key",
    "a1-replacement",
    "dual-dates+provenance",
    "drift",
    "spot-check",
    "treatment-audit",
    "coderabbit",
]
R15_UNTOUCHED_EXPECTED_COUNTS = {
    "under_review:name+docket": 21,
    "under_review:pending": 14,
    "verified_identity": 65,
    "fabrication_suspected": 25,
    "not_found": 5,
}
CONTROLLING_CASE_NO_OFFICIAL_CITE_WARNING = "controlling case has no official cite in lake; cite omitted"
POINT_OVERRIDE_SCHEMA_KEYS = (
    "point",
    "point_label",
    "field_i_validity",
    "as_of_treatment",
    "s3_binding_status",
    "by",
    "scope_note",
)
CONTROLLING_CASE_SCHEMA_KEYS = ("name", "cluster_id", "cite", "field_ii")
MAX_RECORD_SLUG_CHARS = 100
OFF_CL_ALLOWED_SOURCES = {
    "Justia",
    "Google Scholar",
    "Cornell LII",
    "Official court",
    "Official reporter",
    # A17 (2026-07-06): English/foreign-corpus extension — lawful only within the A16
    # outside-CL-corpus scope guard, never as Key-2 for a case CL should hold.
    "BAILII",
    "Founders' Constitution",
    "English Reports facsimile",
}

ALLOWED_OPINION_SOURCES = {
    "cluster.sub_opinions[]",
    "search.sibling_ids[]",
    "search.opinions[].id",
}

LEAD_OPINION_TYPES = {
    "020lead",
    "lead-opinion",
    "015unamimous",
    "015unanimous",
    "010combined",
    "combined-opinion",
}

NEGATIVE_TERMS = [
    "overrul*",
    "abrogat*",
    "supersed*",
    "\"recede from\"",
    "\"no longer good law\"",
    "vacat*",
    "reversed",
]
NEGATIVE_TRIAGE_STEMS = ("overrul", "abrogat", "supersed", "vacat", "revers", "criticiz", "question")
NEGATIVE_TRIAGE_PHRASES = (("recede", "from"), ("no", "longer", "good", "law"))
SNIPPET_FIRST_TRIAGE_LANES = {"lane1_negative", "lane3_recency"}
SNIPPET_PROXIMITY_WORDS = 60
TREATMENT_SNIPPET_FIELD = "results[].opinions[].snippet"
TREATMENT_SNIPPET_SEARCH_FIELDS = ",".join([
    "absolute_url",
    "caseName",
    "caseNameFull",
    "citation",
    "citeCount",
    "cluster_id",
    "court",
    "court_citation_string",
    "court_id",
    "dateFiled",
    "opinions",
    "sibling_ids",
    "status",
    "syllabus",
])

STATE_FAMILIES = {
    "al": ["ala", "alacivapp", "alacrimapp"],
    "ak": ["alaska", "alaskactapp"],
    "az": ["ariz", "arizctapp"],
    "ar": ["ark", "arkctapp"],
    "ca": ["cal", "calctapp", "calappdeptsuper"],
    "co": ["colo", "coloctapp"],
    "ct": ["conn", "connappct"],
    "de": ["del", "delch", "delsuperct"],
    "dc": ["dc", "dccir"],
    "fl": ["fla", "fladistctapp"],
    "ga": ["ga", "gactapp"],
    "hi": ["haw", "hawapp"],
    "id": ["idaho", "idahoctapp"],
    "il": ["ill", "illappct"],
    "in": ["ind", "indctapp"],
    "ia": ["iowa", "iowactapp"],
    "ks": ["kan", "kanctapp"],
    "ky": ["ky", "kyctapp"],
    "la": ["la", "lactapp"],
    "me": ["me"],
    "md": ["md", "mdctspecapp"],
    "ma": ["mass", "massappct"],
    "mi": ["mich", "michctapp"],
    "mn": ["minn", "minnctapp"],
    "ms": ["miss", "missctapp"],
    "mo": ["mo", "moctapp"],
    "mt": ["mont"],
    "ne": ["neb", "nebctapp"],
    "nv": ["nev", "nevapp"],
    "nh": ["nh"],
    "nj": ["nj", "njsuperctappdiv"],
    "nm": ["nm", "nmctapp"],
    "ny": ["ny", "nyappdiv", "nyappterm"],
    "nc": ["nc", "ncctapp"],
    "nd": ["nd"],
    "oh": ["ohio", "ohioctapp"],
    "ok": ["okla", "oklacivapp", "oklacrimapp"],
    "or": ["or", "orctapp"],
    "pa": ["pa", "pasuperct", "pacommwct"],
    "ri": ["ri"],
    "sc": ["sc", "scctapp"],
    "sd": ["sd"],
    "tn": ["tenn", "tenncrimapp", "tennctapp"],
    "tx": ["tex", "texapp", "texcrimapp"],
    "ut": ["utah", "utahctapp"],
    "vt": ["vt"],
    "va": ["va", "vactapp"],
    "wa": ["wash", "washctapp"],
    "wv": ["wva"],
    "wi": ["wis", "wisctapp"],
    "wy": ["wyo"],
}

STATE_NAME_TO_ABBR = {
    "alabama": "al",
    "alaska": "ak",
    "arizona": "az",
    "arkansas": "ar",
    "california": "ca",
    "colorado": "co",
    "connecticut": "ct",
    "delaware": "de",
    "district of columbia": "dc",
    "florida": "fl",
    "georgia": "ga",
    "hawaii": "hi",
    "idaho": "id",
    "illinois": "il",
    "indiana": "in",
    "iowa": "ia",
    "kansas": "ks",
    "kentucky": "ky",
    "louisiana": "la",
    "maine": "me",
    "maryland": "md",
    "massachusetts": "ma",
    "michigan": "mi",
    "minnesota": "mn",
    "mississippi": "ms",
    "missouri": "mo",
    "montana": "mt",
    "nebraska": "ne",
    "nevada": "nv",
    "new hampshire": "nh",
    "new jersey": "nj",
    "new mexico": "nm",
    "new york": "ny",
    "north carolina": "nc",
    "north dakota": "nd",
    "ohio": "oh",
    "oklahoma": "ok",
    "oregon": "or",
    "pennsylvania": "pa",
    "rhode island": "ri",
    "south carolina": "sc",
    "south dakota": "sd",
    "tennessee": "tn",
    "texas": "tx",
    "utah": "ut",
    "vermont": "vt",
    "virginia": "va",
    "washington": "wa",
    "west virginia": "wv",
    "wisconsin": "wi",
    "wyoming": "wy",
}

CAPTION_TOKEN_CONTRACTIONS = {
    "commonwealth": "com",  # Bluebook T6 governmental party abbreviation.
    "board": "bd",  # Bluebook T6 governmental/organizational party abbreviation.
    "education": "ed",  # Normalize full form to CL caption abbreviation.
    "educ": "ed",  # Normalize alternate education abbreviation to CL form.
    "school": "sch",  # Bluebook T6 school abbreviation.
    "district": "dist",  # Bluebook T6 district abbreviation.
    "county": "cty",  # Keep distinct from company -> co.
    "cnty": "cty",  # Normalize alternate county abbreviation without colliding with company.
    "cty": "cty",  # Preserve already-contracted county form.
    "township": "twp",  # Bluebook T6 township abbreviation.
    "department": "dep",  # Normalize full form to CL caption abbreviation.
    "dept": "dep",  # Normalize alternate department abbreviation to CL form.
    "university": "univ",  # Normalize full form to CL caption abbreviation.
    "univ": "univ",  # Preserve already-contracted university form.
    "insurance": "ins",  # Normalize full form to CL caption abbreviation.
    "ins": "ins",  # Preserve already-contracted insurance form.
    "association": "assn",  # Bluebook T6 association abbreviation.
    "company": "co",  # Company may contract to co because county contracts to cty.
    "north": "n",  # Directional abbreviation; one-char outputs are retained.
    "south": "s",  # Directional abbreviation; one-char outputs are retained.
    "east": "e",  # Directional abbreviation; one-char outputs are retained.
    "west": "w",  # Directional abbreviation; one-char outputs are retained.
}

# Manifest/roster-backed agency initialisms only. Keep this phrase-level map
# separate from T6 token contractions so party-text checks do not substring-match
# broad abbreviations such as company -> co.
CAPTION_PHRASE_TOKEN_CONTRACTIONS = (
    (("federal", "bureau", "of", "investigation"), "fbi"),
    (("immigration", "and", "naturalization", "service"), "ins"),
)


def utc_now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0)


def iso_now():
    return utc_now().isoformat().replace("+00:00", "Z")


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=False)
        f.write("\n")
    os.replace(tmp, path)


def sha1_text(value):
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def slugify(value):
    value = value.strip().lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "case"


def bounded_record_slug(value, limit=MAX_RECORD_SLUG_CHARS):
    return slugify(value)[:limit].strip("-") or "case"


def normalize_court_class(value):
    if value is None:
        return None
    key = str(value).strip().lower()
    key = COURT_CLASS_ALIASES.get(key, key)
    if key in STRICT_COURT_CLASSES:
        return key
    return "other"


def normalize_source_record(record):
    out = dict(record)
    if "court_level" in out:
        out["court_level"] = normalize_court_class(out.get("court_level"))
    return out


def normalize_roster_value(value):
    if value is None:
        return ""
    if isinstance(value, (list, tuple)):
        return ",".join(normalize_roster_value(v) for v in value)
    value = str(value).strip().lower()
    value = value.replace("\u2019", "'").replace("\u2018", "'")
    value = re.sub(r"\s+", " ", value)
    return value


def normalized_roster_key(row):
    parts = [
        row.get("caption") or row.get("title") or row.get("record_id") or "",
        row.get("court_era") or row.get("court") or "",
        row.get("year") or row.get("date_decided") or "",
        row.get("docket") or row.get("expected_citation") or row.get("citation") or "",
        row.get("roster_key") or row.get("source_row_index") or "",
    ]
    return "|".join(normalize_roster_value(part) for part in parts)


def page_record_id(page_stem):
    if "--" in page_stem:
        raise ValueError("page-backed record_id cannot contain reserved '--': %s" % page_stem)
    return page_stem


def cluster_stub_record_id(case_name, cluster_id):
    if not cluster_id:
        raise ValueError("cluster stub requires cluster_id")
    return "%s--%s" % (bounded_record_slug(case_name), int(cluster_id))


def not_found_stub_record_id(row):
    key = normalized_roster_key(row)
    return "%s--u%s" % (bounded_record_slug(row.get("caption") or row.get("title") or "case"), sha1_text(key)[:8])


def citation_to_string(citation):
    if not citation:
        return ""
    if isinstance(citation, str):
        return citation
    if citation.get("cite"):
        return str(citation["cite"])
    parts = [citation.get("volume"), citation.get("reporter"), citation.get("page")]
    return " ".join(str(p).strip() for p in parts if p not in (None, ""))


def stripped_citation_text(citation):
    if isinstance(citation, (str, dict)) or not citation:
        return citation_to_string(citation).strip()
    return str(citation).strip()


def normalize_cite(cite):
    cite = citation_to_string(cite)
    cite = re.sub(TRAILING_YEAR_PAREN_RE, "", cite)
    cite = cite.replace("\u00a0", " ")
    cite = re.sub(r"\s+", " ", cite).strip()
    return cite


def citation_compare_key(cite):
    cite = normalize_cite(cite)
    cite = cite.casefold().replace(".", "")
    cite = re.sub(r"\s+", " ", cite).strip()
    cite = re.sub(r"(?<=[a-z])\s+(?=\d+[a-z])", "", cite)
    return cite


def citation_reporter(citation):
    if not citation:
        return ""
    if isinstance(citation, str):
        m = re.match(r"^\s*\d+\s+(.+?)\s+\d+\s*(?:\(|$)", citation)
        return m.group(1).strip() if m else ""
    return str(citation.get("reporter") or "").strip()


def citation_type(citation):
    if isinstance(citation, dict):
        try:
            return int(citation.get("type"))
        except (TypeError, ValueError):
            return citation.get("type")
    return None


def citation_rank(citation, court_class, precedence):
    court_class = court_class or "other"
    reporter = citation_reporter(citation)
    table = precedence.get("court_classes", {}).get(court_class, {})
    reporters = table.get("reporters", {})
    if reporter in reporters:
        return reporters[reporter]
    if court_class == "state":
        ctype = citation_type(citation)
        if ctype == 2:
            return table.get("reporter_classes", {}).get("official")
        if reporter in table.get("regional_reporters", {}):
            return table["regional_reporters"][reporter]
        if ctype == 3:
            return table.get("reporter_classes", {}).get("regional")
        return table.get("reporter_classes", {}).get("other")
    return None


def select_official_cite(citations, court_class, precedence):
    """Return (citation_or_none, reason). Same-rank ties fail closed."""
    candidates = []
    for citation in citations or []:
        ctype = citation_type(citation)
        if court_class in ("scotus", "coa", "district") and ctype != 1:
            continue
        rank = citation_rank(citation, court_class, precedence)
        if rank is None:
            return None, "unlisted_reporter:%s" % citation_reporter(citation)
        candidates.append((rank, normalize_cite(citation), citation))
    if not candidates:
        return None, "no_official_class_citation"
    candidates.sort(key=lambda item: (item[0], item[1]))
    best_rank = candidates[0][0]
    best = [item for item in candidates if item[0] == best_rank]
    if len({item[1] for item in best}) > 1:
        return None, "same_rank_tie"
    return best[0][2], "selected_rank_%s" % best_rank


def parse_circuit(value):
    if value is None:
        return None
    text = str(value).strip().lower()
    if text.startswith("ca") and text[2:].isdigit():
        return "ca%s" % int(text[2:])
    m = re.search(r"(\d+)(?:st|nd|rd|th)?", text)
    if m:
        return "ca%s" % int(m.group(1))
    if "d.c." in text or text in ("dc", "d c"):
        return "cadc"
    if "federal" in text:
        return "cafc"
    return None


def state_abbr(value):
    if not value:
        return None
    text = str(value).strip().lower().replace(".", "")
    if text in STATE_FAMILIES:
        return text
    return STATE_NAME_TO_ABBR.get(text)


def state_family_from_identity(identity):
    state = state_abbr(identity.get("state"))
    if not state:
        court_id = identity.get("court_id") or ""
        prefix = re.match(r"([a-z]+)", str(court_id).lower())
        if prefix:
            for abbr, ids in STATE_FAMILIES.items():
                if prefix.group(1) in ids:
                    state = abbr
                    break
    if not state and identity.get("court"):
        court = str(identity["court"]).lower()
        for name, abbr in STATE_NAME_TO_ABBR.items():
            if name in court:
                state = abbr
                break
    if state and state in STATE_FAMILIES:
        return STATE_FAMILIES[state]
    if identity.get("court_id"):
        return [str(identity["court_id"]).lower()]
    return []


def binding_jurisdiction_filter(identity):
    level = normalize_court_class(identity.get("court_level"))
    if level == "scotus":
        return ""
    if level == "coa":
        circuit = parse_circuit(identity.get("circuit") or identity.get("court_id") or identity.get("court"))
        if not circuit:
            return "AND court_id:(scotus)"
        return "AND court_id:(scotus OR %s)" % circuit
    if level == "district":
        circuit = parse_circuit(identity.get("circuit") or identity.get("court"))
        if not circuit:
            return "AND court_id:(scotus)"
        return "AND court_id:(scotus OR %s)" % circuit
    if level == "state":
        family = state_family_from_identity(identity)
        if not family:
            return "AND court_id:(scotus)"
        return "AND court_id:(scotus OR %s)" % " OR ".join(family)
    return "AND court_id:(scotus)"


def binding_court_ids(identity):
    level = normalize_court_class(identity.get("court_level"))
    if level == "scotus":
        return None
    if level == "coa":
        circuit = parse_circuit(identity.get("circuit") or identity.get("court_id") or identity.get("court"))
        return {"scotus", circuit} if circuit else {"scotus"}
    if level == "district":
        circuit = parse_circuit(identity.get("circuit") or identity.get("court"))
        return {"scotus", circuit} if circuit else {"scotus"}
    if level == "state":
        family = state_family_from_identity(identity)
        return set(["scotus"] + family) if family else {"scotus"}
    return {"scotus"}


def numeric_tail(value):
    text = str(value).rstrip("/")
    m = re.search(r"(\d+)$", text)
    return int(m.group(1)) if m else None


def extract_id(value):
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        for key in ("id", "opinion_id", "cluster_id"):
            if key in value:
                return extract_id(value[key])
    return numeric_tail(value)


def extract_opinion_id(value, source_label):
    """Extract only opinion ids from opinion-bearing arrays.

    Dicts are intentionally stricter than generic CL id parsing: `cluster_id`
    is a different namespace and must never be accepted as an opinion id.
    """
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        for key in ("id", "opinion_id"):
            if key in value and value[key] not in (None, ""):
                return extract_opinion_id(value[key], source_label)
        if "cluster_id" in value:
            raise ValueError("%s carried cluster_id but no opinion id" % source_label)
        return None
    return numeric_tail(value)


def strip_trailing_year_parenthetical(value):
    return re.sub(TRAILING_YEAR_PAREN_RE, "", value or "").strip()


def strip_trailing_parenthetical(value):
    text = str(value or "").strip()
    while re.search(TRAILING_PAREN_RE, text):
        text = re.sub(TRAILING_PAREN_RE, "", text).strip()
    return text


def first_party_terms(case_name):
    text = strip_trailing_year_parenthetical(case_name)
    parts = re.split(r"\s+v\.?\s+", text, maxsplit=1, flags=re.I)
    if len(parts) != 2:
        return [text.strip()] if text.strip() else []
    terms = []
    for part in parts:
        term = party_side_last_term(part)
        if term:
            terms.append(term)
    return terms


def strip_apostrophes(value):
    return str(value or "").replace("'", "").replace("\u2019", "").replace("\u2018", "")


def caption_word_tokens(value):
    return [token for token in slugify(strip_apostrophes(value)).split("-") if token]


def contract_caption_phrase_tokens(tokens):
    out = []
    changed = False
    i = 0
    while i < len(tokens):
        for phrase, contraction in CAPTION_PHRASE_TOKEN_CONTRACTIONS:
            phrase_len = len(phrase)
            if tuple(tokens[i:i + phrase_len]) == phrase:
                out.append(contraction)
                i += phrase_len
                changed = True
                break
        else:
            out.append(tokens[i])
            i += 1
    return out, changed


def party_side_last_term(value):
    phrase_tokens, phrase_changed = contract_caption_phrase_tokens(caption_word_tokens(value))
    if phrase_changed:
        words = [token for token in phrase_tokens if len(token) > 2]
    else:
        words = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]+", value) if len(w) > 2]
    return words[-1] if words else None


def caption_phrase_initialisms(value):
    phrase_tokens, phrase_changed = contract_caption_phrase_tokens(caption_word_tokens(value))
    if not phrase_changed:
        return set()
    contractions = {contraction for _phrase, contraction in CAPTION_PHRASE_TOKEN_CONTRACTIONS}
    return {token for token in phrase_tokens if token in contractions}


def caption_token_set(value):
    if not str(value or "").strip():
        return set()
    tokens, _changed = contract_caption_phrase_tokens(caption_word_tokens(value))
    return {
        CAPTION_TOKEN_CONTRACTIONS.get(token, token)
        for token in tokens
        if token
    }


def caption_sides(value):
    text = strip_trailing_year_parenthetical(value)
    parts = re.split(r"\s+v\.?\s+", text, maxsplit=1, flags=re.I)
    if len(parts) != 2:
        return None
    return [caption_token_set(parts[0]), caption_token_set(parts[1])]


def token_containment_match(left, right):
    return bool(left and right) and (left <= right or right <= left)


def canonical_caption_match(input_name, canonical_name):
    input_sides = caption_sides(input_name)
    canonical_sides = caption_sides(canonical_name)
    if input_sides and canonical_sides:
        return all(
            token_containment_match(input_side, canonical_side)
            for input_side, canonical_side in zip(input_sides, canonical_sides)
        )
    if input_sides or canonical_sides:
        return False
    return token_containment_match(caption_token_set(input_name), caption_token_set(canonical_name))


def canonical_caption_match_cluster(input_name, cluster, fallback_name=None):
    names = [
        cluster.get("case_name") if cluster else None,
        cluster.get("case_name_full") if cluster else None,
        cluster.get("case_name_short") if cluster else None,
        fallback_name,
    ]
    seen = set()
    for name in names:
        if not name:
            continue
        key = str(name)
        if key in seen:
            continue
        seen.add(key)
        if canonical_caption_match(input_name, key):
            return True
    return False


def party_term_candidate_sets(term):
    lowered = str(term or "").lower()
    stripped = strip_apostrophes(lowered)
    containment_candidates = {candidate for candidate in (lowered, stripped) if candidate}
    containment_candidates.update(
        full
        for full, contraction in CAPTION_TOKEN_CONTRACTIONS.items()
        if stripped and contraction == stripped
    )
    boundary_candidates = set()
    boundary_candidates.update(caption_phrase_initialisms(stripped))
    if stripped in CAPTION_TOKEN_CONTRACTIONS:
        boundary_candidates.add(CAPTION_TOKEN_CONTRACTIONS[stripped])
    return containment_candidates, boundary_candidates


def party_term_candidates(term):
    containment_candidates, boundary_candidates = party_term_candidate_sets(term)
    return containment_candidates | boundary_candidates


def text_contains_party_candidate(text, candidate, boundary=False):
    if not candidate:
        return False
    if boundary:
        return re.search(r"\b%s\b" % re.escape(candidate), text) is not None
    return candidate in text


def missing_party_terms(case_name, text):
    terms = first_party_terms(case_name)
    if not terms:
        return []
    lowered = strip_apostrophes((text or "").lower())
    missing = []
    for term in terms:
        containment_candidates, boundary_candidates = party_term_candidate_sets(term)
        if any(text_contains_party_candidate(lowered, candidate) for candidate in containment_candidates):
            continue
        if any(text_contains_party_candidate(lowered, candidate, boundary=True) for candidate in boundary_candidates):
            continue
        missing.append(term)
    return missing


def recency_window_start(build_date=None, years=3):
    if build_date is None:
        build_date = dt.date.today()
    if isinstance(build_date, str):
        build_date = dt.date.fromisoformat(build_date)
    try:
        return build_date.replace(year=build_date.year - years).isoformat()
    except ValueError:
        return build_date.replace(month=2, day=28, year=build_date.year - years).isoformat()


class TokenBucket:
    """Capacity-1 paced limiter kept under the old class name.

    A full token bucket can burst above a literal "N calls in any 60 seconds"
    rule. This limiter reserves one call every 60/N seconds; runtime `wait()`
    adds jitter before every network call, including the first call.
    """

    def __init__(self, rate_per_minute=14, capacity=None, start_time=None):
        self.rate_per_minute = float(rate_per_minute)
        if self.rate_per_minute <= 0:
            raise ValueError("rate_per_minute must be positive")
        self.capacity = 1.0
        self.interval = (60.0 / self.rate_per_minute) + 0.000001
        self.next_available_at = float(time.time() if start_time is None else start_time)

    @property
    def refill_per_second(self):
        return self.rate_per_minute / 60.0

    def consume_at(self, now, amount=1):
        amount = float(amount)
        if amount != 1.0:
            raise ValueError("paced limiter only supports single-call reservations")
        now = float(now)
        scheduled_at = max(now, self.next_available_at)
        wait = max(0.0, scheduled_at - now)
        self.next_available_at = scheduled_at + self.interval
        return wait

    def mark_completed_at(self, completed_at):
        completed_at = float(completed_at)
        self.next_available_at = max(self.next_available_at, completed_at + self.interval)

    def mark_completed(self):
        self.mark_completed_at(time.time())

    def wait(self):
        wait = self.consume_at(time.time())
        time.sleep(wait + random.uniform(0.05, 0.35))


class HourlyGuard:
    def __init__(self, max_per_hour=900):
        self.max_per_hour = max_per_hour
        self.calls = []

    def wait(self):
        now = time.time()
        self.calls = [ts for ts in self.calls if now - ts < 3600]
        if len(self.calls) >= self.max_per_hour:
            sleep_for = 3600 - (now - self.calls[0]) + 1
            time.sleep(max(1, sleep_for))
            now = time.time()
            self.calls = [ts for ts in self.calls if now - ts < 3600]
        self.calls.append(now)


class SessionTimer:
    def __init__(self, minutes=None):
        self.started = time.time()
        self.limit = None if minutes is None else float(minutes) * 60.0

    def expired(self):
        return self.limit is not None and (time.time() - self.started) >= self.limit


class CallBudget:
    def __init__(self, max_calls=None):
        self.max_calls = max_calls
        self.session_calls = 0
        self.cumulative_calls = 0

    def exhausted(self):
        return self.max_calls is not None and self.session_calls >= self.max_calls

    def record_call(self):
        self.session_calls += 1
        self.cumulative_calls += 1

    def snapshot(self, estimated_remaining=None):
        return {
            "calls_this_session": self.session_calls,
            "cumulative_calls_observed": self.cumulative_calls,
            "remaining_estimate": estimated_remaining,
            "max_calls_this_session": self.max_calls,
        }


class IngestInterrupted(Exception):
    def __init__(self, reason, record_id=None, step=None):
        super().__init__(reason)
        self.reason = reason
        self.record_id = record_id
        self.step = step


class FetchFailed(Exception):
    def __init__(self, method, url, step, reason, attempts, status=None, original=None):
        super().__init__("%s %s failed after %s attempt(s): %s" % (method, url, attempts, reason))
        self.method = method
        self.url = url
        self.step = step
        self.reason = reason
        self.attempts = attempts
        self.status = status
        self.original = original


class Journal:
    def __init__(self, path, run_id):
        self.path = path
        self.run_id = run_id
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)

    def append(self, **row):
        row.setdefault("ts", iso_now())
        row.setdefault("run", self.run_id)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, sort_keys=True) + "\n")

    def ensure_writable(self):
        directory = os.path.dirname(self.path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(self.path, "a", encoding="utf-8"):
            pass

    def rows(self):
        if not os.path.exists(self.path):
            return []
        out = []
        with open(self.path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return out


class ResumeState:
    def __init__(self, rows):
        self.steps = {}
        self.step_rows = {}
        self.lanes = {}
        self.selected_clusters = {}
        self.final_record_ids = {}
        for row in rows:
            record_id = row.get("record_id")
            step = row.get("step")
            lane = row.get("lane")
            status = row.get("status")
            if not record_id or not step:
                continue
            if lane:
                self.lanes[(record_id, step, lane)] = {
                    "status": status,
                    "skipped": row.get("skipped"),
                    "cursor": row.get("cursor"),
                    "reviewed": row.get("reviewed"),
                    "proposed": row.get("proposed"),
                    "cap_hit": row.get("cap_hit"),
                    "retry_pending": row.get("retry_pending"),
                    "fetch_failed": row.get("fetch_failed"),
                    "note": row.get("note"),
                    "failed_step": row.get("failed_step"),
                }
            else:
                self.steps[(record_id, step)] = status
                self.step_rows[(record_id, step)] = row
            if row.get("selected_cluster_id") is not None:
                self.selected_clusters[(record_id, step)] = row.get("selected_cluster_id")
            if row.get("final_record_id"):
                self.final_record_ids[(record_id, step)] = row.get("final_record_id")

    def step_complete(self, record_id, step):
        return self.steps.get((record_id, step)) == "complete"

    def step_status(self, record_id, step):
        return self.steps.get((record_id, step))

    def selected_cluster_id(self, record_id, step="identity"):
        return self.selected_clusters.get((record_id, step))

    def final_record_id(self, record_id, step="identity"):
        return self.final_record_ids.get((record_id, step))

    def lane_status(self, record_id, step, lane):
        return self.lanes.get((record_id, step, lane), {"status": "pending", "cursor": None})

    def lane_complete(self, record_id, step, lane):
        return self.lane_status(record_id, step, lane).get("status") == "complete"


def default_lane_status():
    return {
        "identity": "pending",
        "citations": "pending",
        "pinpoints": "pending",
        "progeny": "pending",
        "treatment": {
            lane: {"status": "pending", "cursor": None}
            for lane, _cap in TREATMENT_LANES
        },
        "provenance": "pending",
    }


def frontier_stub_lane_status(identity="pending"):
    return {
        "identity": identity,
        "fabrication_check": "pending",
        "citations": "pending",
        "off_cl_links": "pending",
        "provenance": "pending",
        "treatment": {},
    }


TREATMENT_LANE_STATE_FIELDS = (
    "cursor",
    "reviewed",
    "proposed",
    "cap_hit",
    "retry_pending",
    "fetch_failed",
    "note",
    "failed_step",
)


def treatment_lane_resume_row(record_id, lane, state, status=None, skipped=False):
    row = {
        "record_id": record_id,
        "step": "treatment",
        "lane": lane,
        "status": status if status is not None else state.get("status"),
    }
    if skipped:
        row["skipped"] = True
    for field in TREATMENT_LANE_STATE_FIELDS:
        value = state.get(field)
        if value is not None:
            row[field] = value
    return row


def resume_rows_from_manifest(records):
    rows = []
    for row in records:
        record_id = row.get("record_id")
        lane_status = row.get("lane_status") or {}
        if not record_id:
            continue
        for step in ("identity", "citations", "pinpoints", "progeny"):
            status = lane_status.get(step)
            if status in ("pending", "partial", "complete"):
                rows.append({"record_id": record_id, "step": step, "status": status})
        treatment = lane_status.get("treatment") or {}
        for lane, _cap in TREATMENT_LANES:
            state = treatment.get(lane) or {}
            if isinstance(state, str):
                state = {"status": state}
            status = state.get("status")
            if status in ("pending", "partial", "complete"):
                rows.append({
                    "record_id": record_id,
                    "step": "treatment",
                    "lane": lane,
                    "status": status,
                    "cursor": state.get("cursor"),
                    "reviewed": state.get("reviewed"),
                    "proposed": state.get("proposed"),
                    "cap_hit": state.get("cap_hit"),
                    "retry_pending": state.get("retry_pending"),
                    "fetch_failed": state.get("fetch_failed"),
                    "note": state.get("note"),
                    "failed_step": state.get("failed_step"),
                })
    return rows


class LakePaths:
    def __init__(self, repo_root, pool_root):
        self.repo_root = repo_root
        self.lake = os.path.join(repo_root, "_overhaul2", "lake")
        self.points = os.path.join(repo_root, "_overhaul2", "points")
        self.cases = os.path.join(self.lake, "cases")
        self.manifest = os.path.join(self.lake, "_manifest.json")
        self.schema = os.path.join(self.lake, "_schema.json")
        self.s2_binding = os.path.join(self.points, "s2-binding.yaml")
        self.precedence = os.path.join(self.lake, "_reporter-precedence.json")
        self.treatment_migration = os.path.join(self.lake, "_treatment-migration.json")
        self.pool = pool_root
        self.http_cache = os.path.join(pool_root, "cache", "http")
        self.progeny = os.path.join(pool_root, "cache", "progeny")
        self.text = os.path.join(pool_root, "cache", "text")
        self.journal = os.path.join(pool_root, "journal")
        self.logs = os.path.join(pool_root, "logs")
        self.db = os.path.join(pool_root, "db")

    def ensure(self):
        for path in [
            self.cases,
            self.http_cache,
            self.progeny,
            self.text,
            self.journal,
            self.logs,
            self.db,
        ]:
            os.makedirs(path, exist_ok=True)


def read_token(path=TOKEN_PATH):
    with open(os.path.expanduser(path), encoding="utf-8") as f:
        token = f.read().strip()
    if not token:
        raise RuntimeError("empty CourtListener token at %s" % path)
    return token


class CourtListenerClient:
    def __init__(self, paths, token, token_fingerprint, journal, budget, rate, hourly, run_id):
        self.paths = paths
        self.token = token
        self.token_fingerprint = token_fingerprint
        self.journal = journal
        self.budget = budget
        self.rate = rate
        self.analyze_rate = TokenBucket(rate_per_minute=60, capacity=1)
        self.hourly = hourly
        self.run_id = run_id
        self.call_log = os.path.join(paths.logs, "cl-calls.log")
        self.urlopen = urllib.request.urlopen
        self.sleep = time.sleep

    def build_url(self, endpoint, params=None):
        endpoint = endpoint.strip("/")
        query = urllib.parse.urlencode(params or {}, doseq=True)
        url = "%s/%s/" % (API_BASE, endpoint)
        return url + ("?" + query if query else "")

    def cache_path(self, url):
        return os.path.join(self.paths.http_cache, sha1_text(url) + ".json")

    def log_call(self, method, url, status=None):
        os.makedirs(os.path.dirname(self.call_log), exist_ok=True)
        row = {
            "ts": iso_now(),
            "consumer": CONSUMER_IDENTITY,
            "credential_fingerprint": self.token_fingerprint,
            "method": method,
            "url_sha1": sha1_text(url),
            "host": urllib.parse.urlparse(url).netloc,
            "status": status,
        }
        with open(self.call_log, "a", encoding="utf-8") as f:
            f.write(json.dumps(row, sort_keys=True) + "\n")

    def wait_for_network_call(self, record_id=None, step=None, extra_rate_bucket=None):
        if self.budget.exhausted():
            raise IngestInterrupted("call_budget_exhausted", record_id=record_id, step=step)
        self.rate.wait()
        if extra_rate_bucket is not None:
            extra_rate_bucket.wait()
        self.hourly.wait()
        self.budget.record_call()

    def mark_network_call_completed(self, extra_rate_bucket=None):
        self.rate.mark_completed()
        if extra_rate_bucket is not None:
            extra_rate_bucket.mark_completed()

    def retry_jitter(self):
        return random.uniform(0.25, 1.5)

    def sleep_before_retry(self, attempt):
        delay = FETCH_RETRY_DELAYS[attempt - 1] + self.retry_jitter()
        self.sleep(delay)

    def transport_failure_reason(self, exc):
        reason = getattr(exc, "reason", exc)
        if isinstance(reason, BaseException):
            return "%s: %s" % (reason.__class__.__name__, reason)
        return "%s: %s" % (exc.__class__.__name__, reason)

    def journal_fetch_failed(self, method, url, record_id, step, attempts, reason, status=None):
        self.journal.append(
            record_id=record_id,
            step=step or "http",
            status="fetch_failed",
            url_sha1=sha1_text(url),
            http_status=status,
            attempts=attempts,
            retry_pending=True,
            reason=reason,
            budget=self.budget.snapshot(),
        )

    def request_json_url(self, method, url, body=None, record_id=None, step=None, rate_bucket=None, timeout=URL_TIMEOUT_SECONDS):
        attempt = 0
        while True:
            attempt += 1
            self.wait_for_network_call(record_id=record_id, step=step or method.lower(), extra_rate_bucket=rate_bucket)
            req = urllib.request.Request(url, data=body, method=method)
            req.add_header("Authorization", "Token %s" % self.token)
            req.add_header("Accept", "application/json")
            req.add_header("User-Agent", "cssi-s2-builder/1.0")
            if body is not None:
                req.add_header("Content-Type", "application/json")
            try:
                with self.urlopen(req, timeout=timeout) as resp:
                    response_body = resp.read().decode("utf-8")
                    status = getattr(resp, "status", 200)
                self.log_call(method, url, status=status)
                self.mark_network_call_completed(extra_rate_bucket=rate_bucket)
                data = json.loads(response_body)
                self.journal.append(
                    record_id=record_id,
                    step=step or method.lower(),
                    status="network",
                    url_sha1=sha1_text(url),
                    http_status=status,
                    budget=self.budget.snapshot(),
                )
                return data
            except urllib.error.HTTPError as exc:
                self.log_call(method, url, status=exc.code)
                self.mark_network_call_completed(extra_rate_bucket=rate_bucket)
                if exc.code in RETRYABLE_HTTP_CODES:
                    if attempt <= len(FETCH_RETRY_DELAYS):
                        self.sleep_before_retry(attempt)
                        continue
                    reason = "http_%s" % exc.code
                    self.journal_fetch_failed(method, url, record_id, step, attempt, reason, status=exc.code)
                    raise FetchFailed(method, url, step, reason, attempt, status=exc.code, original=exc)
                raise
            except (urllib.error.URLError, TimeoutError, socket.timeout, ConnectionResetError) as exc:
                self.log_call(method, url, status="transport_error")
                self.mark_network_call_completed(extra_rate_bucket=rate_bucket)
                reason = self.transport_failure_reason(exc)
                if attempt <= len(FETCH_RETRY_DELAYS):
                    self.sleep_before_retry(attempt)
                    continue
                self.journal_fetch_failed(method, url, record_id, step, attempt, reason)
                raise FetchFailed(method, url, step, reason, attempt, original=exc)

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        cache_file = self.cache_path(url)
        if cache and os.path.exists(cache_file):
            with open(cache_file, encoding="utf-8") as f:
                data = json.load(f)
            self.journal.append(
                record_id=record_id,
                step=step or "http",
                status="cache-hit",
                url_sha1=sha1_text(url),
            )
            return data

        data = self.request_json_url("GET", url, record_id=record_id, step=step or "http")
        if cache:
            with open(cache_file, "w", encoding="utf-8") as f:
                json.dump(data, f)
        return data

    def post_json_url(self, url, payload, record_id=None, step=None, rate_bucket=None):
        body = json.dumps(payload).encode("utf-8")
        return self.request_json_url("POST", url, body=body, record_id=record_id, step=step or "post", rate_bucket=rate_bucket)

    def search(self, params, cache=True, record_id=None, step=None):
        return self.get_json_url(self.build_url("search", params), cache=cache, record_id=record_id, step=step or "search")

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        cluster_id = int(cluster_id)
        return self.get_json_url(self.build_url("clusters/%s" % cluster_id), cache=True, record_id=record_id, step=step)

    def opinion_ref(self, opinion_id, source_array, context=None):
        if source_array not in ALLOWED_OPINION_SOURCES:
            raise ValueError("opinion source must be one of %s" % sorted(ALLOWED_OPINION_SOURCES))
        opinion_id = int(opinion_id)
        return {
            "opinion_id": opinion_id,
            "source_array": source_array,
            "context": context or {},
        }

    def get_opinion(self, opinion_ref, record_id=None, step="opinion"):
        if not isinstance(opinion_ref, dict):
            raise TypeError("get_opinion requires an opinion_ref dict, not a raw id")
        source_array = opinion_ref.get("source_array")
        if source_array not in ALLOWED_OPINION_SOURCES:
            raise ValueError("untraceable opinion id source: %r" % source_array)
        opinion_id = int(opinion_ref["opinion_id"])
        self.journal.append(
            record_id=record_id,
            step=step + ".opinion-ref",
            status="trace",
            opinion_id=opinion_id,
            opinion_id_source=source_array,
            context=opinion_ref.get("context") or {},
        )
        return self.get_json_url(self.build_url("opinions/%s" % opinion_id), cache=True, record_id=record_id, step=step)

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        opinion_id = int(opinion_ref["opinion_id"])
        text_path = os.path.join(self.paths.text, "%s.txt" % opinion_id)
        if os.path.exists(text_path):
            with open(text_path, encoding="utf-8") as f:
                return f.read()
        opinion = self.get_opinion(opinion_ref, record_id=record_id, step=step)
        text = opinion_text(opinion)
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(text)
        return text

    def analyze_citations(self, text, record_id=None, job_id=None, resume=False):
        payload = {"text": text}
        if job_id:
            payload["job_id"] = job_id
        if resume:
            payload["resume_citation_analysis"] = True
        self.journal.append(
            record_id=record_id,
            step="analyze_citations",
            status="request",
            job_id=job_id,
            resume=bool(resume),
            throttle="60_per_minute",
        )
        return self.post_json_url(
            self.build_url("citation-lookup"),
            payload,
            record_id=record_id,
            step="analyze_citations",
            rate_bucket=self.analyze_rate,
        )


def opinion_text(opinion):
    for key in ("plain_text", "html_with_citations", "html", "xml_harvard", "html_lawbox"):
        value = opinion.get(key)
        if value:
            return str(value)
    return ""


def opinion_refs_from_cluster(client, cluster):
    refs = []
    for item in cluster.get("sub_opinions") or []:
        try:
            opinion_id = extract_opinion_id(item, "cluster.sub_opinions[]")
        except ValueError:
            continue
        if opinion_id:
            refs.append(client.opinion_ref(opinion_id, "cluster.sub_opinions[]", {"cluster_id": cluster.get("id")}))
    return refs


def opinion_refs_from_search_result(client, result):
    refs = []
    for item in result.get("sibling_ids") or []:
        try:
            opinion_id = extract_opinion_id(item, "search.sibling_ids[]")
        except ValueError:
            continue
        if opinion_id:
            refs.append(client.opinion_ref(opinion_id, "search.sibling_ids[]", {"cluster_id": result.get("cluster_id")}))
    for opinion in result.get("opinions") or []:
        try:
            opinion_id = extract_opinion_id(opinion, "search.opinions[]")
        except ValueError:
            continue
        if opinion_id:
            refs.append(client.opinion_ref(opinion_id, "search.opinions[].id", {"cluster_id": result.get("cluster_id")}))
    return refs


def outbound_edges_from_search_result(result):
    edges = []
    seen = set()
    for opinion in result.get("opinions") or []:
        try:
            source_opinion_id = extract_opinion_id(opinion, "search.opinions[]")
        except ValueError:
            continue
        if not source_opinion_id:
            continue
        for cited in opinion.get("cites") or []:
            cited_id = extract_id(cited)
            if not cited_id:
                continue
            key = (int(source_opinion_id), int(cited_id))
            if key in seen:
                continue
            seen.add(key)
            edges.append({
                "source_opinion_id": int(source_opinion_id),
                "cited_id": int(cited_id),
                "source": "search.opinions[].cites[]",
            })
    return edges


def pick_lead_ref(client, cluster, search_result=None):
    search_opinions = []
    if search_result:
        search_opinions = search_result.get("opinions") or []
        for opinion in search_opinions:
            otype = str(opinion.get("type") or "").lower()
            if otype in LEAD_OPINION_TYPES:
                try:
                    opinion_id = extract_opinion_id(opinion, "search.opinions[]")
                except ValueError:
                    continue
                if opinion_id:
                    return client.opinion_ref(opinion_id, "search.opinions[].id", {"lead_type": otype})
    for item in cluster.get("sub_opinions") or []:
        if isinstance(item, dict):
            otype = str(item.get("type") or "").lower()
            if otype in LEAD_OPINION_TYPES:
                try:
                    opinion_id = extract_opinion_id(item, "cluster.sub_opinions[]")
                except ValueError:
                    continue
                if opinion_id:
                    return client.opinion_ref(opinion_id, "cluster.sub_opinions[]", {"lead_type": otype})
    refs = opinion_refs_from_cluster(client, cluster)
    return refs[0] if refs else None


def search_count(data):
    for key in ("count", "count_exact", "total", "total_count"):
        if isinstance(data, dict) and key in data:
            try:
                return int(data[key])
            except (TypeError, ValueError):
                pass
    return None


def search_results(data):
    if not isinstance(data, dict):
        return []
    return data.get("results") or data.get("objects") or []


def next_url(data):
    if isinstance(data, dict):
        return data.get("next")
    return None


def initial_search_cursor(client, params):
    build_url = getattr(client, "build_url", None)
    if callable(build_url):
        return build_url("search", params)
    query = urllib.parse.urlencode(params or {}, doseq=True)
    return "%s?%s" % (API_BASE + "/search/", query) if query else API_BASE + "/search/"


def court_search_id(record):
    level = normalize_court_class(record.get("court_level"))
    if level == "scotus":
        return "scotus"
    if level == "coa":
        return parse_circuit(record.get("circuit") or record.get("court"))
    return None


def identity_search_case_name(record):
    raw = record.get("title") or record.get("caption") or record.get("record_id")
    if raw is None:
        return None
    text = str(raw)
    return strip_trailing_parenthetical(text) or text.strip()


def identity_search_params(record):
    params = {
        "type": "o",
        "case_name": identity_search_case_name(record),
        "order_by": "score desc",
        "page_size": 10,
    }
    court = court_search_id(record)
    if court:
        params["court"] = court
    if record.get("year"):
        params["filed_after"] = "%s-01-01" % record["year"]
        params["filed_before"] = "%s-12-31" % record["year"]
    return params


def identity_result_count(search):
    count = search_count(search)
    if count is not None:
        return count
    return len(search_results(search))


def identity_fallback_params(record, expected_cite):
    base = identity_search_params(record)
    caption = base.get("case_name")
    if caption:
        by_query = dict(base)
        by_query.pop("case_name", None)
        by_query["q"] = caption
        yield "q", by_query

    normalized_cite = normalize_cite(expected_cite)
    if normalized_cite:
        by_citation = {
            "type": "o",
            "citation": normalized_cite,
            "order_by": "score desc",
            "page_size": 10,
        }
        if base.get("court"):
            by_citation["court"] = base["court"]
        yield "citation", by_citation

    docket = record.get("docket")
    if docket:
        by_docket = {
            "type": "o",
            "docket_number": docket,
            "order_by": "score desc",
            "page_size": 10,
        }
        if base.get("court"):
            by_docket["court"] = base["court"]
        yield "docket_number", by_docket


def identity_search_attempts(record, expected_cite):
    attempts = [("case_name", identity_search_params(record))]
    seen = {json.dumps(attempts[0][1], sort_keys=True)}
    for rung, params in identity_fallback_params(record, expected_cite):
        key = json.dumps(params, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        attempts.append((rung, params))
    return attempts


def remaining_stronger_key_rungs(attempts, index):
    return [
        rung
        for rung, _params in attempts[index + 1:]
        if rung in STRONG_IDENTITY_RUNGS
    ]


def identity_candidate_caption_match(record, result, cluster):
    input_caption = record.get("title") or record.get("caption") or record.get("record_id")
    canonical = None
    if isinstance(cluster, dict):
        canonical = cluster.get("case_name")
    if not canonical and isinstance(result, dict):
        canonical = result.get("caseName") or result.get("case_name")
    return canonical_caption_match_cluster(input_caption, cluster, canonical)


def first_candidate_caption_match(record, candidates):
    if not candidates:
        return None
    _score, result, cluster = candidates[0]
    return identity_candidate_caption_match(record, result, cluster)


def frontier_identity_search_results(source_record, client, unresolved_id):
    expected_cite = source_record.get("expected_citation") or source_record.get("citation") or ""
    attempts = identity_search_attempts(source_record, expected_cite)
    for rung, params in attempts:
        step = "frontier.identity.search" if rung == "case_name" else "frontier.identity.search.%s" % rung
        search = client.search(params, cache=True, record_id=unresolved_id, step=step)
        results = search_results(search)
        if results:
            return results, rung
    return [], None


def frontier_identity_selection(source_record, client, journal, unresolved_id):
    expected_cite = source_record.get("expected_citation") or source_record.get("citation") or ""
    attempts = identity_search_attempts(source_record, expected_cite)
    best_candidates = []
    best_rung = None
    selected_candidates = []
    selected_rung = None
    for attempt_index, (rung, params) in enumerate(attempts):
        step = "frontier.identity.search" if rung == "case_name" else "frontier.identity.search.%s" % rung
        search = client.search(params, cache=True, record_id=unresolved_id, step=step)
        results = search_results(search)
        prefilter = {}
        candidates = identity_candidates(
            source_record,
            client,
            results,
            expected_cite,
            unresolved_id,
            max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
            prefilter_info=prefilter,
            rung=rung,
        )
        remaining = remaining_stronger_key_rungs(attempts, attempt_index)
        viable_for_rung = identity_viable_candidates(
            source_record,
            candidates,
            expected_cite,
            remaining,
            rung=rung,
        )
        journal.append(
            record_id=unresolved_id,
            step="frontier.identity.search.prefilter" if rung == "case_name" else "frontier.identity.search.fallback",
            status="complete",
            rung=rung,
            result_count=identity_result_count(search),
            clusters_fetched=len(candidates),
            viable=bool(viable_for_rung),
            caption_match=first_candidate_caption_match(source_record, candidates),
            remaining_stronger_rungs=remaining,
            **prefilter,
        )
        if candidates and (not best_candidates or candidates[0][0] > best_candidates[0][0]):
            best_candidates = candidates
            best_rung = rung
        if viable_for_rung:
            selected_candidates = viable_for_rung
            selected_rung = rung
            break
    candidates = selected_candidates or best_candidates
    rung = selected_rung if selected_candidates else best_rung
    if not candidates:
        return None, None, [], None
    return candidates[0][1], candidates[0][2], candidates[1:], rung


def identity_year_matches(record, result, cluster):
    if not record.get("year"):
        return False
    expected_year = str(record["year"])
    for value in (
        cluster.get("date_filed") if isinstance(cluster, dict) else None,
        cluster.get("dateFiled") if isinstance(cluster, dict) else None,
        result.get("dateFiled") if isinstance(result, dict) else None,
        result.get("date_filed") if isinstance(result, dict) else None,
    ):
        if str(value or "").startswith(expected_year):
            return True
    return False


def court_value_tokens(value):
    if value is None:
        return set()
    if isinstance(value, dict):
        tokens = set()
        for key in ("id", "slug", "short_name", "full_name", "citation_string"):
            tokens.update(court_value_tokens(value.get(key)))
        return tokens
    if isinstance(value, (list, tuple)):
        tokens = set()
        for item in value:
            tokens.update(court_value_tokens(item))
        return tokens
    text = str(value).strip().lower()
    return {text} if text else set()


def identity_court_matches(record, result, cluster):
    expected = court_search_id(record)
    if not expected:
        return False
    actual = set()
    if isinstance(cluster, dict):
        actual.update(court_value_tokens(cluster.get("court")))
        actual.update(court_value_tokens(cluster.get("court_id")))
    if isinstance(result, dict):
        actual.update(court_value_tokens(result.get("court")))
        actual.update(court_value_tokens(result.get("court_id")))
        actual.update(court_value_tokens(result.get("court_citation_string")))
    return expected.lower() in actual


def identity_candidate_evidence(record, result, cluster, expected_cite, rung=None):
    citation_match = citation_matches_expected(cluster, expected_cite)
    year_match = identity_year_matches(record, result, cluster)
    court_match = identity_court_matches(record, result, cluster)
    has_expected_cite = bool(normalize_cite(expected_cite))
    docket_key_match = rung == "docket_number" and bool(record.get("docket"))
    return {
        "expected_citation_match": citation_match,
        "docket_key_match": docket_key_match,
        "year_match": year_match,
        "court_match": court_match,
        "viable": citation_match or docket_key_match or (not has_expected_cite and year_match and court_match),
    }


def identity_candidate_score(record, result, cluster, expected_cite, rung=None):
    evidence = identity_candidate_evidence(record, result, cluster, expected_cite, rung=rung)
    score = 0
    if evidence["expected_citation_match"]:
        score += 100
    if evidence["docket_key_match"]:
        score += 90
    if evidence["year_match"]:
        score += 10
    if evidence["court_match"]:
        score += 10
    return score


def identity_viable_candidates(record, candidates, expected_cite, remaining_stronger_rungs=None, rung=None):
    remaining_stronger_rungs = remaining_stronger_rungs or []
    return [
        candidate
        for candidate in candidates
        if identity_candidate_evidence(record, candidate[1], candidate[2], expected_cite, rung=rung)["viable"]
        and (
            not remaining_stronger_rungs
            or identity_candidate_caption_match(record, candidate[1], candidate[2])
        )
    ]


def search_result_citations(result):
    citations = result.get("citation") if isinstance(result, dict) else None
    if citations in (None, ""):
        return []
    if isinstance(citations, (list, tuple)):
        return citations
    return [citations]


def search_result_citation_matches_expected(result, expected_key):
    if not expected_key:
        return False
    return any(citation_compare_key(citation) == expected_key for citation in search_result_citations(result))


def identity_candidate_result_plan(results, expected_cite, max_clusters, prefilter_max_clusters=None):
    expected_key = citation_compare_key(normalize_cite(expected_cite))
    prefilter_matches = []
    if expected_key:
        prefilter_matches = [
            result
            for result in results
            if search_result_citation_matches_expected(result, expected_key)
        ]
    if prefilter_matches:
        limit = prefilter_max_clusters if prefilter_max_clusters is not None else max_clusters
        candidate_results = prefilter_matches[:limit]
    else:
        candidate_results = results[:max_clusters]
    prefilter_fetched_cluster_ids = []
    if prefilter_matches:
        for result in candidate_results:
            cluster_id = extract_id(result.get("cluster_id") or result.get("cluster"))
            if cluster_id is not None:
                prefilter_fetched_cluster_ids.append(cluster_id)
    prefilter_info = {
        "citation_prefilter_matched_rows": len(prefilter_matches),
        "citation_prefilter_fetched_cluster_ids": prefilter_fetched_cluster_ids,
    }
    return candidate_results, prefilter_info


def identity_candidates(
    record,
    client,
    results,
    expected_cite,
    record_id,
    max_clusters=IDENTITY_PRIMARY_CLUSTER_LIMIT,
    prefilter_max_clusters=None,
    prefilter_info=None,
    rung=None,
):
    candidates = []
    candidate_results, local_prefilter_info = identity_candidate_result_plan(
        results,
        expected_cite,
        max_clusters,
        prefilter_max_clusters=prefilter_max_clusters,
    )
    if prefilter_info is not None:
        prefilter_info.update(local_prefilter_info)
    for result in candidate_results:
        cluster_id = result.get("cluster_id") or result.get("cluster")
        if not cluster_id:
            continue
        cluster = client.get_cluster(cluster_id, record_id=record_id, step="identity.cluster")
        score = identity_candidate_score(record, result, cluster, expected_cite, rung=rung)
        candidates.append((score, result, cluster))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates


def citation_matches_expected(cluster, expected):
    expected = citation_compare_key(expected)
    if not expected:
        return False
    for citation in cluster.get("citations") or []:
        if citation_compare_key(citation) == expected:
            return True
    return False


def text_names_parties(case_name, text):
    if not text:
        return False
    terms = first_party_terms(case_name)
    return bool(terms) and not missing_party_terms(case_name, text)


def base_field_provenance(src, verifier=CONSUMER_IDENTITY):
    return {"src": src, "at": iso_now(), "verifier": verifier}


def append_warning(record_json, warning):
    warnings = record_json["provenance"].setdefault("warnings", [])
    if warning not in warnings:
        warnings.append(warning)


def set_record_status(record_json, status, reason=None, explicit_adjudication=False):
    current = record_json.get("status")
    if current in FAIL_CLOSED_STATUSES and current != status and not explicit_adjudication:
        if reason:
            append_warning(record_json, "preserved %s over %s: %s" % (current, status, reason))
        return False
    record_json["status"] = status
    return True


def parse_frontmatter_scalar(value):
    value = value.strip()
    if value in ("", "null", "~"):
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value in ("[]", "{}"):
        return [] if value == "[]" else {}
    if value.startswith("[") and value.endswith("]"):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return [item.strip().strip("\"'") for item in value[1:-1].split(",") if item.strip()]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    if re.fullmatch(r"\d{4}", value):
        return int(value)
    return value


def parse_treatment_frontmatter_lines(lines):
    treatment = {}
    current_list_key = None
    current_item = None
    for line in lines:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()
        if indent <= 2 and not stripped.startswith("- ") and ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            if value.strip() == "":
                treatment[key] = [] if key == "point_overrides" else None
                current_list_key = key if key == "point_overrides" else None
            else:
                treatment[key] = parse_frontmatter_scalar(value)
                current_list_key = None
            current_item = None
            continue
        if current_list_key == "point_overrides" and indent >= 4:
            if stripped.startswith("- "):
                current_item = {}
                treatment.setdefault("point_overrides", []).append(current_item)
                stripped = stripped[2:].strip()
                if not stripped:
                    continue
            if current_item is not None and ":" in stripped:
                key, _, value = stripped.partition(":")
                current_item[key.strip()] = parse_frontmatter_scalar(value)
    return treatment


def legacy_treatment_from_page(page_path):
    if not page_path or not os.path.exists(page_path):
        return {}
    with open(page_path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    lines = text[4:end].splitlines()
    treatment_lines = []
    in_treatment = False
    for line in lines:
        if not in_treatment:
            if line.strip() == "treatment:":
                in_treatment = True
            continue
        if line and not line.startswith(" "):
            break
        treatment_lines.append(line)
    return parse_treatment_frontmatter_lines(treatment_lines)


def empty_record_shell(record_id, source_record, build_run):
    source_record = normalize_source_record(source_record)
    now = iso_now()
    return {
        "schema_version": SCHEMA_VERSION,
        "record_id": record_id,
        "stub": bool(source_record.get("stub")),
        "status": "draft",
        "identity": {
            "case_name": None,
            "case_name_short": None,
            "case_name_full": None,
            "input_case_name": source_record.get("title") or source_record.get("caption") or record_id,
            "court": source_record.get("court") or source_record.get("court_era") or None,
            "court_id": None,
            "court_level": source_record.get("court_level") or None,
            "circuit": source_record.get("circuit") or None,
            "state": source_record.get("state") or None,
            "date_decided": source_record.get("date_decided") or None,
            "year": source_record.get("year"),
            "docket": source_record.get("docket") or None,
            "cluster_id": None,
            "lead_opinion_id": None,
            "sibling_ids": [],
            "absolute_url": None,
            "identity_method": "pending",
            "expected_citation_found": False,
            "party_name_in_text": False,
            "canonical_name_match": None,
            "alternates": [],
            "reason_code": None,
        },
        "citations": {
            "official": None,
            "parallel": [],
            "vendor_neutral": [],
            "all": [],
            "display": None,
            "official_selection": {"court_class": source_record.get("court_level") or None, "selected": None, "reason": None},
        },
        "pinpoints": [],
        "treatment": {
            "field_i_validity": "unverified",
            "as_of_content": None,
            "as_of_treatment": None,
            "composite_basis": "unverified",
            "composite_basis_ref": None,
            "varies_by_point": False,
            "scope_note": None,
            "point_overrides": [],
            "edges": [],
            "derivation": {},
        },
        "progeny": {
            "complete_query": None,
            "indexed_citing_opinions": None,
            "count_source": None,
            "per_sibling": [],
            "citation_count": None,
            "cache_path": None,
            "enumeration": None,
            "cursor": None,
            "rows_cached": 0,
            "outbound_opinion_edges": [],
        },
        "off_cl_links": [],
        "provenance": {
            "cl_source": None,
            "cl_api": API_BASE,
            "built_by": CONSUMER_IDENTITY,
            "build_run": build_run,
            "date_created": now,
            "date_modified": now,
            "warnings": [],
            "field_provenance": {
                "identity": base_field_provenance("pending"),
                "treatment.field_i_validity": base_field_provenance("pending"),
                "point_overrides": base_field_provenance("pending"),
                "pinpoints": base_field_provenance("pending"),
            },
        },
    }


def classify_citations(cluster_citations, court_class, precedence):
    court_class = normalize_court_class(court_class) or "other"
    all_cites = []
    vendor = []
    for citation in cluster_citations or []:
        cite = {
            "cite": citation_to_string(citation),
            "volume": citation.get("volume") if isinstance(citation, dict) else None,
            "reporter": citation_reporter(citation) or None,
            "page": citation.get("page") if isinstance(citation, dict) else None,
            "type": citation_type(citation),
            "selected_official": False,
            "source": "cluster.citations[]",
        }
        all_cites.append(cite)
        if cite["type"] in (6, 7, 8):
            vendor.append(cite)
    official, reason = select_official_cite(all_cites, court_class, precedence)
    official_cite = None
    if official:
        official_cite = dict(official)
        official_cite["selected_official"] = True
    parallels = []
    for cite in all_cites:
        if official_cite and normalize_cite(cite) == normalize_cite(official_cite):
            continue
        if cite["type"] not in (6, 7, 8):
            parallels.append(cite)
    return {
        "official": official_cite,
        "parallel": parallels,
        "vendor_neutral": vendor,
        "all": all_cites,
        "display": normalize_cite(official_cite) if official_cite else None,
        "official_selection": {
            "court_class": court_class,
            "selected": normalize_cite(official_cite) if official_cite else None,
            "reason": reason,
        },
    }


def harvest_pinpoints(page_path, source_text):
    if not page_path or not os.path.exists(page_path):
        return []
    with open(page_path, encoding="utf-8") as f:
        page = f.read()
    pins = []
    pattern = re.compile(r"[\"“]([^\"”]{12,})[\"”][^\n]*?(?:at\s+(\d+))?[^\n]*?\^([A-Za-z0-9_-]+)")
    source_has_stars = bool(re.search(r"\*\d+", source_text or ""))
    for match in pattern.finditer(page):
        quote = re.sub(r"\s+", " ", match.group(1)).strip()
        page_num = match.group(2)
        pin_id = match.group(3)
        position = None
        fidelity = "not_checked"
        star_marker = None
        if source_text:
            normalized_source = re.sub(r"\s+", " ", source_text)
            position = normalized_source.find(quote)
            fidelity = "matched" if position >= 0 else "mismatch"
            if position >= 0 and source_has_stars:
                prefix = normalized_source[:position]
                stars = re.findall(r"\*(\d+)", prefix)
                if stars:
                    star_marker = stars[-1]
        status = "star-verified" if source_has_stars and star_marker else "slip-only"
        pins.append({
            "id": pin_id,
            "page": page_num,
            "quote": quote,
            "star_marker": star_marker,
            "quote_fidelity": fidelity,
            "pinpoint_status": status,
            "position": position if position is not None and position >= 0 else None,
        })
    return pins


def complete_cites_query(sibling_ids):
    ids = [str(int(i)) for i in sibling_ids if i is not None]
    if not ids:
        return None
    return "cites:(%s)" % " OR ".join(ids)


def official_domain_allowed(url):
    host = urllib.parse.urlparse(url).netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    if host in ("justia.com", "scholar.google.com", "law.cornell.edu", "supremecourt.gov"):
        return True
    if host.endswith(".justia.com") or host.endswith(".uscourts.gov") or host.endswith(".courts.gov"):
        return True
    if ".courts." in host or host.endswith(".state.us"):
        return True
    return False


def resolve_identity(record, client, journal, resume, build_run):
    record_id = record["record_id"]
    if resume.step_complete(record_id, "identity"):
        selected_cluster_id = resume.selected_cluster_id(record_id, "identity")
        if selected_cluster_id:
            cluster = client.get_cluster(selected_cluster_id, record_id=record_id, step="identity.cluster.replay")
            journal.append(record_id=record_id, step="identity", status="complete", skipped=True, replayed_selection=True)
            return {"cluster_id": selected_cluster_id, "opinions": []}, cluster, []
        journal.append(record_id=record_id, step="identity", status="complete", skipped=True, replayed_selection=False)
        return None, None, None

    expected_cite = record.get("expected_citation") or record.get("citation") or ""
    attempts = identity_search_attempts(record, expected_cite)
    primary_rung, params = attempts[0]
    search = client.search(params, cache=True, record_id=record_id, step="identity.search")
    results = search_results(search)
    primary_prefilter = {}
    candidates = identity_candidates(
        record,
        client,
        results,
        expected_cite,
        record_id,
        prefilter_max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
        prefilter_info=primary_prefilter,
        rung=primary_rung,
    )
    selected_rung = primary_rung
    primary_remaining = remaining_stronger_key_rungs(attempts, 0)
    viable_candidates = identity_viable_candidates(record, candidates, expected_cite, primary_remaining, rung=primary_rung)
    best_candidates = candidates
    best_rung = primary_rung if best_candidates else None
    selected_candidates = viable_candidates
    selected_rung = primary_rung if selected_candidates else None
    journal.append(
        record_id=record_id,
        step="identity.search.prefilter",
        status="complete",
        rung=primary_rung,
        result_count=identity_result_count(search),
        clusters_fetched=len(candidates),
        viable=bool(viable_candidates),
        caption_match=first_candidate_caption_match(record, candidates),
        remaining_stronger_rungs=primary_remaining,
        **primary_prefilter,
    )
    if not selected_candidates:
        for attempt_index, (rung, fallback) in enumerate(attempts[1:], start=1):
            fallback_search = client.search(fallback, cache=True, record_id=record_id, step="identity.search.fallback")
            fallback_results = search_results(fallback_search)
            fallback_prefilter = {}
            rung_candidates = identity_candidates(
                record,
                client,
                fallback_results,
                expected_cite,
                record_id,
                max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
                prefilter_info=fallback_prefilter,
                rung=rung,
            )
            remaining = remaining_stronger_key_rungs(attempts, attempt_index)
            viable_for_rung = identity_viable_candidates(record, rung_candidates, expected_cite, remaining, rung=rung)
            rung_viable = bool(viable_for_rung)
            journal.append(
                record_id=record_id,
                step="identity.search.fallback",
                status="complete",
                rung=rung,
                result_count=identity_result_count(fallback_search),
                clusters_fetched=len(rung_candidates),
                viable=rung_viable,
                caption_match=first_candidate_caption_match(record, rung_candidates),
                remaining_stronger_rungs=remaining,
                **fallback_prefilter,
            )
            if rung_candidates and (not best_candidates or rung_candidates[0][0] > best_candidates[0][0]):
                best_candidates = rung_candidates
                best_rung = rung
            if rung_viable:
                results = fallback_results
                selected_candidates = viable_for_rung
                selected_rung = rung
                break
        candidates = selected_candidates or best_candidates or []
        selected_rung = selected_rung if selected_candidates else best_rung
    else:
        candidates = selected_candidates
    selected = candidates[0] if candidates else None
    journal.append(
        record_id=record_id,
        step="identity",
        status="partial" if selected else "complete",
        candidate_count=len(candidates),
        selected_cluster_id=selected[2].get("id") if selected else None,
        search_rung=selected_rung if selected else None,
    )
    if not selected:
        return None, None, None
    return selected[1], selected[2], candidates[1:]


def apply_identity(record_json, source_record, search_result, cluster, alternates, client, journal):
    record_id = source_record["record_id"]
    expected_cite = source_record.get("expected_citation") or source_record.get("citation") or ""
    lead_ref = pick_lead_ref(client, cluster, search_result)
    lead_text = ""
    lead_id = None
    if lead_ref:
        lead_id = int(lead_ref["opinion_id"])
        lead_text = client.text_for_opinion(lead_ref, record_id=record_id, step="identity.lead_text")
    expected_found = citation_matches_expected(cluster, expected_cite) if expected_cite else False
    input_caption = source_record.get("title") or source_record.get("caption") or record_id
    missing_terms = missing_party_terms(input_caption, lead_text)
    party_found = bool(first_party_terms(input_caption)) and not missing_terms
    if missing_terms:
        journal.append(
            record_id=record_id,
            step="identity.party-text",
            status="miss",
            missing_terms=missing_terms,
        )
    canonical = cluster.get("case_name") or search_result.get("caseName") or search_result.get("case_name")
    canonical_match = canonical_caption_match_cluster(input_caption, cluster, canonical)
    sibling_ids = []
    for ref in opinion_refs_from_search_result(client, search_result):
        sibling_ids.append(int(ref["opinion_id"]))
    for ref in opinion_refs_from_cluster(client, cluster):
        sibling_ids.append(int(ref["opinion_id"]))
    sibling_ids = sorted(set(sibling_ids))
    record_json["progeny"]["outbound_opinion_edges"] = outbound_edges_from_search_result(search_result)
    identity = record_json["identity"]
    identity.update({
        "case_name": canonical,
        "case_name_short": cluster.get("case_name_short"),
        "case_name_full": cluster.get("case_name_full"),
        "court": source_record.get("court") or cluster.get("court") or search_result.get("court_citation_string"),
        "court_id": search_result.get("court_id") or cluster.get("court"),
        "court_level": normalize_court_class(source_record.get("court_level") or identity.get("court_level")),
        "circuit": source_record.get("circuit") or identity.get("circuit"),
        "date_decided": cluster.get("date_filed") or source_record.get("date_decided"),
        "year": source_record.get("year") or identity.get("year"),
        "docket": source_record.get("docket") or identity.get("docket"),
        "cluster_id": extract_id(cluster.get("id")),
        "lead_opinion_id": lead_id,
        "sibling_ids": sibling_ids,
        "absolute_url": cluster.get("absolute_url") or search_result.get("absolute_url"),
        "expected_citation_found": bool(expected_found),
        "party_name_in_text": bool(party_found),
        "canonical_name_match": canonical_match,
        "alternates": [
            {
                "cluster_id": alt_cluster.get("id"),
                "score": score,
                "case_name": alt_cluster.get("case_name"),
            }
            for score, _alt_result, alt_cluster in alternates[:5]
        ],
    })
    if canonical_match and expected_found and party_found:
        set_record_status(record_json, "under_review", "R15 structural gates have not cleared")
        identity["identity_method"] = "citation+party-text"
        identity["reason_code"] = "awaiting_r15_structural_gates"
    elif not canonical_match and expected_found and party_found:
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "citation+party-text"
        identity["reason_code"] = "caption_mismatch_canonical"
        append_warning(record_json, "input caption does not match CL canonical caption")
    elif not canonical_match:
        set_record_status(record_json, "fabrication_suspected")
        identity["identity_method"] = "fabrication-check"
        identity["reason_code"] = "canonical_name_mismatch"
        append_warning(record_json, "input caption does not match CL canonical caption")
    elif source_record.get("docket"):
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "name+docket"
        identity["reason_code"] = "recent_or_no_official_cite"
    else:
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "pending"
        identity["reason_code"] = "two_key_not_satisfied"
        append_warning(record_json, "two-key identity check did not fully satisfy citation plus party text")
    record_json["provenance"]["cl_source"] = cluster.get("source")
    record_json["provenance"]["field_provenance"]["identity"] = base_field_provenance("CourtListener search + clusters + lead opinion text")
    journal.append(record_id=record_id, step="identity", status="complete", final_status=record_json["status"])
    return lead_ref, lead_text


def apply_citations(record_json, cluster, precedence, journal):
    record_id = record_json["record_id"]
    court_class = normalize_court_class(record_json["identity"].get("court_level")) or "other"
    record_json["citations"] = classify_citations(cluster.get("citations") or [], court_class, precedence)
    if record_json["citations"]["official"] is None:
        set_record_status(record_json, "under_review", "official cite selection failed")
        append_warning(record_json, "official cite selection failed closed: %s" % record_json["citations"]["official_selection"]["reason"])
    journal.append(record_id=record_id, step="citations", status="complete", official=record_json["citations"]["display"])


def apply_pinpoints(record_json, source_record, lead_text, journal):
    record_id = record_json["record_id"]
    record_json["pinpoints"] = harvest_pinpoints(source_record.get("page_path"), lead_text)
    record_json["provenance"]["field_provenance"]["pinpoints"] = base_field_provenance("content page quote harvest + lead opinion text")
    journal.append(record_id=record_id, step="pinpoints", status="complete", count=len(record_json["pinpoints"]))


def fetch_progeny(record_json, source_record, client, journal, resume):
    record_id = source_record["record_id"]
    if resume.step_complete(record_id, "progeny") and record_json["progeny"].get("complete_query"):
        journal.append(record_id=record_id, step="progeny", status="complete", skipped=True)
        return False
    sibling_ids = record_json["identity"].get("sibling_ids") or []
    query = complete_cites_query(sibling_ids)
    if not query:
        journal.append(record_id=record_id, step="progeny", status="complete", skipped=True, reason="no_sibling_ids")
        return False
    first = client.search({"type": "o", "q": query, "order_by": "score desc", "page_size": 100}, cache=True, record_id=record_id, step="progeny.search")
    count = search_count(first)
    cache_path = os.path.join(client.paths.progeny, "%s.jsonl" % slugify(record_id))
    cursor = next_url(first)
    rows = search_results(first)
    with open(cache_path, "w", encoding="utf-8") as f:
        f.write(json.dumps({
            "_meta": "progeny-cache",
            "record_id": record_id,
            "complete_query": query,
            "enumeration": "bounded",
            "partial": bool(cursor),
            "cursor": cursor,
            "indexed_citing_opinions": count,
            "count_source": "search",
            "rows_cached": len(rows),
        }, sort_keys=True) + "\n")
        for result in rows:
            f.write(json.dumps(result, sort_keys=True) + "\n")
    per_sibling = []
    for sibling_id in sibling_ids:
        per = client.search({"type": "o", "q": "cites:(%s)" % sibling_id, "page_size": 1, "fields": "id"}, cache=True, record_id=record_id, step="progeny.per_sibling")
        per_sibling.append({
            "opinion_id": int(sibling_id),
            "count": search_count(per) or 0,
            "count_source": "search",
        })
    old_progeny = record_json.get("progeny") or {}
    record_json["progeny"] = {
        "complete_query": query,
        "indexed_citing_opinions": count,
        "count_source": "search",
        "per_sibling": per_sibling,
        "citation_count": old_progeny.get("citation_count"),
        "cache_path": cache_path,
        "enumeration": "bounded",
        "cursor": cursor,
        "rows_cached": len(rows),
        "outbound_opinion_edges": old_progeny.get("outbound_opinion_edges") or [],
    }
    journal.append(
        record_id=record_id,
        step="progeny",
        status="complete",
        indexed_citing_opinions=count,
        count_source="search",
        enumeration="bounded",
        cursor=cursor,
        rows_cached=len(rows),
    )
    return True


def lane_query(record_json, lane_name):
    query = record_json["progeny"].get("complete_query")
    if not query:
        return None, {}
    if lane_name == "lane1_negative":
        bounded = "%s AND (%s) %s" % (
            query,
            " OR ".join(NEGATIVE_TERMS),
            binding_jurisdiction_filter(record_json["identity"]),
        )
        return bounded, {
            "type": "o",
            "q": bounded,
            "stat_Published": "on",
            "order_by": "dateFiled desc",
            "page_size": 100,
            "fields": TREATMENT_SNIPPET_SEARCH_FIELDS,
        }
    if lane_name == "lane2_top_cited":
        return query, {"type": "o", "q": query, "order_by": "citeCount desc", "page_size": 25}
    if lane_name == "lane3_recency":
        filed_after = recency_window_start()
        return query, {
            "type": "o",
            "q": query,
            "order_by": "dateFiled desc",
            "filed_after": filed_after,
            "page_size": 100,
            "fields": TREATMENT_SNIPPET_SEARCH_FIELDS,
        }
    raise ValueError("unknown lane %s" % lane_name)


def snippet_text(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(snippet_text(item) for item in value if item is not None)
    return str(value)


def treatment_result_snippet(result):
    snippets = []
    top_level = snippet_text(result.get("snippet"))
    if top_level:
        snippets.append(top_level)
    for opinion in result.get("opinions") or []:
        if not isinstance(opinion, dict):
            continue
        value = snippet_text(opinion.get("snippet"))
        if value:
            snippets.append(value)
    return "\n".join(snippets).strip()


def word_tokens(value):
    return re.findall(r"[a-z0-9]+", str(value or "").lower())


def phrase_positions(tokens, phrase):
    phrase = tuple(phrase)
    if not phrase or len(phrase) > len(tokens):
        return []
    positions = []
    width = len(phrase)
    for index in range(0, len(tokens) - width + 1):
        if tuple(tokens[index:index + width]) == phrase:
            positions.append(index)
    return positions


def negative_keyword_positions(tokens):
    positions = []
    for index, token in enumerate(tokens):
        if any(token.startswith(stem) for stem in NEGATIVE_TRIAGE_STEMS):
            positions.append(index)
    for phrase in NEGATIVE_TRIAGE_PHRASES:
        positions.extend(phrase_positions(tokens, phrase))
    return sorted(set(positions))


def add_target_phrase(phrases, seen, value, min_tokens=2):
    tokens = tuple(word_tokens(value))
    if len(tokens) < min_tokens or tokens in seen:
        return
    seen.add(tokens)
    phrases.append(tokens)


def target_case_phrases(record_json):
    identity = record_json.get("identity") or {}
    phrases = []
    seen = set()
    for key in ("case_name", "case_name_full", "input_case_name"):
        add_target_phrase(phrases, seen, identity.get(key))
    short_name = identity.get("case_name_short")
    if short_name and len(str(short_name).strip()) >= 5:
        add_target_phrase(phrases, seen, short_name, min_tokens=1)

    citations = record_json.get("citations") or {}
    cite_values = [citations.get("display")]
    official = citations.get("official")
    if isinstance(official, dict):
        cite_values.append(official.get("cite") or citation_to_string(official))
    for cite in citations.get("all") or []:
        if isinstance(cite, dict):
            cite_values.append(cite.get("cite") or citation_to_string(cite))
            reporter = cite.get("reporter")
            page = cite.get("page")
            if reporter and page:
                cite_values.append("%s %s" % (reporter, page))
        else:
            cite_values.append(cite)
    for value in cite_values:
        add_target_phrase(phrases, seen, value)
    return phrases


def target_positions(tokens, record_json):
    positions = []
    for phrase in target_case_phrases(record_json):
        positions.extend(phrase_positions(tokens, phrase))
    return sorted(set(positions))


def citing_court_is_binding(result, identity):
    allowed = binding_court_ids(identity)
    if allowed is None:
        return True
    court_id = str(result.get("court_id") or "").lower()
    return court_id in allowed


def treatment_hit_id(result):
    cluster_id = extract_id(result.get("cluster_id") or result.get("cluster"))
    if cluster_id:
        return "cluster:%s" % cluster_id
    for opinion in result.get("opinions") or []:
        if isinstance(opinion, dict):
            opinion_id = extract_id(opinion.get("id"))
            if opinion_id:
                return "opinion:%s" % opinion_id
    if result.get("absolute_url"):
        return "url:%s" % result["absolute_url"]
    return "sha1:%s" % sha1_text(json.dumps(result, sort_keys=True, default=str))


def triage_treatment_hit(record_json, result):
    snippet = treatment_result_snippet(result)
    hit_id = treatment_hit_id(result)
    if not snippet:
        return {"hit_id": hit_id, "decision": "read", "reason": "missing_snippet"}

    tokens = word_tokens(snippet)
    negative_positions = negative_keyword_positions(tokens)
    if not negative_positions:
        return {"hit_id": hit_id, "decision": "snippet-classified", "reason": "no_negative_keyword_in_snippet"}

    nearby_targets = target_positions(tokens, record_json)
    if nearby_targets:
        distance = min(abs(negative - target) for negative in negative_positions for target in nearby_targets)
        if distance <= SNIPPET_PROXIMITY_WORDS:
            return {"hit_id": hit_id, "decision": "read", "reason": "negative_keyword_near_target"}
        return {"hit_id": hit_id, "decision": "snippet-classified", "reason": "negative_keyword_not_near_target"}

    if citing_court_is_binding(result, record_json.get("identity") or {}):
        return {"hit_id": hit_id, "decision": "read", "reason": "binding_ambiguous_negative_keyword"}
    return {"hit_id": hit_id, "decision": "snippet-classified", "reason": "nonbinding_ambiguous_negative_keyword"}


def treatment_derivation_row(lane_name, query, reviewed, cap, cap_hit, final_cursor, proposed, audit_needed=None, extra=None):
    if audit_needed is None:
        audit_needed = cap_hit
    row = {
        "query": query,
        "reviewed": reviewed,
        "cap": cap,
        "cap_hit": cap_hit,
        "final_cursor": final_cursor,
        "audit_needed": audit_needed,
        "proposed_negative_events": len(proposed),
    }
    row["audit_marker"] = "R15 treatment audit required" if cap_hit else None
    if lane_name in SNIPPET_FIRST_TRIAGE_LANES:
        row["triage_mode"] = "snippet-first"
        row["snippet_field"] = TREATMENT_SNIPPET_FIELD
    if extra:
        row.update(extra)
    return row


def treatment_hit_text(client, result, record_id, lane_name):
    refs = opinion_refs_from_search_result(client, result)
    if not refs:
        return ""
    return client.text_for_opinion(refs[0], record_id=record_id, step="treatment.%s.hit_text" % lane_name)


def review_treatment_hit(result, opinion_text_value=""):
    text = (json.dumps(result) + "\n" + (opinion_text_value or "")).lower()
    event = None
    if "overrul" in text:
        event = "overruled"
    elif "abrogat" in text:
        event = "abrogated"
    elif "supersed" in text:
        event = "superseded_by_statute"
    elif "criticiz" in text:
        event = "criticized"
    elif "question" in text:
        event = "questioned"
    return event


def treatment_edge_key(edge):
    citing = edge.get("citing_case") or {}
    return (
        citing.get("cluster_id"),
        citing.get("name"),
        edge.get("field_ii"),
        edge.get("field_iii"),
        edge.get("point"),
    )


def append_treatment_edges(record_json, proposed):
    edges = record_json["treatment"].setdefault("edges", [])
    existing = {treatment_edge_key(edge) for edge in edges}
    added = 0
    for edge in proposed:
        key = treatment_edge_key(edge)
        if key in existing:
            continue
        edges.append(edge)
        existing.add(key)
        added += 1
    return added


def mark_treatment_fetch_failed(record_json, journal, lane_name, query, cap, reviewed, proposed, cursor, failure, triage_extra=None):
    record_id = record_json["record_id"]
    append_treatment_edges(record_json, proposed)
    derivation = record_json["treatment"].setdefault("derivation", {})
    extra = {
        "fetch_failed": True,
        "retry_pending": True,
        "failed_step": failure.step,
        "failure_reason": failure.reason,
        "attempts": failure.attempts,
    }
    if triage_extra:
        extra.update(triage_extra)
    derivation[lane_name] = treatment_derivation_row(
        lane_name,
        query,
        reviewed,
        cap,
        False,
        cursor,
        proposed,
        audit_needed=False,
        extra=extra,
    )
    append_warning(record_json, "treatment %s fetch failed after bounded retries; retry pending" % lane_name)
    journal.append(
        record_id=record_id,
        step="treatment",
        lane=lane_name,
        status="partial",
        cursor=cursor,
        reviewed=reviewed,
        proposed=len(proposed),
        note="fetch_failed",
        fetch_failed=True,
        retry_pending=True,
        failed_step=failure.step,
        attempts=failure.attempts,
        reason=failure.reason,
    )


def run_treatment(record_json, source_record, client, journal, resume, session):
    record_id = source_record["record_id"]
    if record_json.get("stub"):
        return False
    changed = False
    completed_lanes = set()
    derivation = record_json["treatment"].setdefault("derivation", {})
    for lane_name, cap in TREATMENT_LANES:
        if session.expired():
            return changed
        lane_state = resume.lane_status(record_id, "treatment", lane_name)
        if lane_state.get("skipped") or lane_state.get("status") == "complete":
            journal.append(**treatment_lane_resume_row(record_id, lane_name, lane_state, skipped=True))
            if lane_state.get("status") == "complete":
                completed_lanes.add(lane_name)
            continue
        query, params = lane_query(record_json, lane_name)
        if not query:
            journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", reason="no_progeny_query")
            derivation[lane_name] = {
                "query": None,
                "reviewed": 0,
                "cap": cap,
                "cap_hit": False,
                "final_cursor": None,
                "audit_needed": False,
                "proposed_negative_events": 0,
            }
            changed = True
            completed_lanes.add(lane_name)
            continue
        retry_pending = bool(lane_state.get("retry_pending"))
        reviewed = 0 if retry_pending else int(lane_state.get("reviewed") or 0)
        proposed = []
        cursor = None if retry_pending else lane_state.get("cursor")
        cap_hit = False
        final_cursor = cursor
        triaged = 0
        triage_reads = 0
        snippet_classified = 0
        try:
            current_page_cursor = cursor or initial_search_cursor(client, params)
            data = client.get_json_url(cursor, cache=False, record_id=record_id, step="treatment.%s.resume" % lane_name) if cursor else client.search(params, cache=False, record_id=record_id, step="treatment.%s.search" % lane_name)
            while True:
                for result in search_results(data):
                    if reviewed >= cap:
                        break
                    reviewed += 1
                    if lane_name in SNIPPET_FIRST_TRIAGE_LANES:
                        triage = triage_treatment_hit(record_json, result)
                        triaged += 1
                        if triage["decision"] == "read":
                            triage_reads += 1
                        else:
                            snippet_classified += 1
                        journal.append(
                            record_id=record_id,
                            step="treatment.triage",
                            lane=lane_name,
                            status="journaled",
                            hit_id=triage["hit_id"],
                            decision=triage["decision"],
                            reason=triage["reason"],
                            snippet_field=TREATMENT_SNIPPET_FIELD,
                        )
                        if triage["decision"] == "read":
                            hit_text = treatment_hit_text(client, result, record_id, lane_name)
                            field_ii = review_treatment_hit(result, hit_text)
                        else:
                            field_ii = None
                    else:
                        hit_text = treatment_hit_text(client, result, record_id, lane_name)
                        field_ii = review_treatment_hit(result, hit_text)
                    if field_ii:
                        proposed.append({
                            "citing_case": {
                                "name": result.get("caseName") or result.get("case_name") or "",
                                "cluster_id": extract_id(result.get("cluster_id")),
                                "cite": result.get("citation") or None,
                                "field_ii": field_ii,
                            },
                            "field_ii": field_ii,
                            "field_iii": "mentioned",
                            "point": None,
                            "proposed": True,
                            "journal_ref": "%s:%s" % (record_id, lane_name),
                        })
                if reviewed >= cap:
                    cap_hit = True
                    final_cursor = next_url(data) or current_page_cursor
                    journal.append(
                        record_id=record_id,
                        step="treatment",
                        lane=lane_name,
                        status="complete",
                        cap_hit=True,
                        cursor=final_cursor,
                        audit_needed=True,
                        reviewed=reviewed,
                        proposed=len(proposed),
                        triaged=triaged if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                        full_text_reads=triage_reads if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                        snippet_classified=snippet_classified if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                    )
                    break
                url = next_url(data)
                if not url:
                    final_cursor = None
                    journal.append(
                        record_id=record_id,
                        step="treatment",
                        lane=lane_name,
                        status="complete",
                        cap_hit=False,
                        cursor=None,
                        audit_needed=False,
                        reviewed=reviewed,
                        proposed=len(proposed),
                        triaged=triaged if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                        full_text_reads=triage_reads if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                        snippet_classified=snippet_classified if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                    )
                    break
                final_cursor = url
                journal.append(
                    record_id=record_id,
                    step="treatment",
                    lane=lane_name,
                    status="partial",
                    cursor=url,
                    reviewed=reviewed,
                    proposed=len(proposed),
                    triaged=triaged if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                    full_text_reads=triage_reads if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                    snippet_classified=snippet_classified if lane_name in SNIPPET_FIRST_TRIAGE_LANES else None,
                )
                if session.expired():
                    extra = {}
                    if lane_name in SNIPPET_FIRST_TRIAGE_LANES:
                        extra = {
                            "triage_journaled": triaged,
                            "triage_read": triage_reads,
                            "triage_snippet_classified": snippet_classified,
                        }
                    derivation[lane_name] = treatment_derivation_row(
                        lane_name,
                        query,
                        reviewed,
                        cap,
                        False,
                        url,
                        proposed,
                        audit_needed=False,
                        extra=extra,
                    )
                    append_treatment_edges(record_json, proposed)
                    return True
                current_page_cursor = url
                data = client.get_json_url(url, cache=False, record_id=record_id, step="treatment.%s.page" % lane_name)
        except FetchFailed as exc:
            extra = {}
            if lane_name in SNIPPET_FIRST_TRIAGE_LANES:
                extra = {
                    "triage_journaled": triaged,
                    "triage_read": triage_reads,
                    "triage_snippet_classified": snippet_classified,
                }
            mark_treatment_fetch_failed(record_json, journal, lane_name, query, cap, reviewed, proposed, final_cursor, exc, triage_extra=extra)
            changed = True
            continue
        extra = {}
        if lane_name in SNIPPET_FIRST_TRIAGE_LANES:
            extra = {
                "triage_journaled": triaged,
                "triage_read": triage_reads,
                "triage_snippet_classified": snippet_classified,
            }
        derivation[lane_name] = treatment_derivation_row(
            lane_name,
            query,
            reviewed,
            cap,
            cap_hit,
            final_cursor,
            proposed,
            extra=extra,
        )
        append_treatment_edges(record_json, proposed)
        changed = True
        completed_lanes.add(lane_name)
    if all(resume.lane_complete(record_id, "treatment", lane) or lane in completed_lanes for lane, _cap in TREATMENT_LANES):
        journal.append(record_id=record_id, step="treatment", status="complete")
    return changed


def strip_wikilink(value):
    text = str(value or "").strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2]
    if "|" in text:
        text = text.split("|", 1)[0].strip()
    return text


def controlling_cases_from_legacy(by_values, field_ii):
    out = []
    for value in by_values or []:
        name = strip_wikilink(value)
        if not name:
            continue
        out.append({
            "name": name,
            "cluster_id": None,
            "cite": None,
            "field_ii": field_ii,
        })
    return out


def seed_preseeded_treatment(record_json, page_treatment):
    if record_json.get("status") in FAIL_CLOSED_STATUSES:
        return False
    field_i = normalize_roster_value(page_treatment.get("field_i_validity"))
    if field_i not in PRESEEDED_FIELD_I_VALIDITIES:
        return False

    was_treatment_migration_block = (
        record_json.get("status") == "blocked"
        and record_json["identity"].get("reason_code") == "treatment_migration_unmapped"
    )
    treatment = record_json["treatment"]
    treatment["field_i_validity"] = field_i
    for key in PRESEEDED_TREATMENT_CARRY_KEYS:
        if key in page_treatment and page_treatment[key] is not None:
            treatment[key] = page_treatment[key]
    if treatment.get("point_overrides") and "varies_by_point" not in page_treatment:
        treatment["varies_by_point"] = True
    if treatment.get("composite_basis") == "unverified" and treatment.get("composite_basis_ref"):
        treatment["composite_basis"] = "principal-holding"
    set_record_status(
        record_json,
        "under_review",
        PRESEEDED_TREATMENT_PROVENANCE,
        explicit_adjudication=was_treatment_migration_block,
    )
    if was_treatment_migration_block and record_json.get("status") == "under_review":
        record_json["identity"]["reason_code"] = None
    append_warning(record_json, PRESEEDED_TREATMENT_PROVENANCE)
    record_json["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance(PRESEEDED_TREATMENT_PROVENANCE)
    if treatment.get("point_overrides"):
        record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance(PRESEEDED_TREATMENT_PROVENANCE)
    return True


def seed_treatment_from_migration(record_json, source_record, migration):
    if record_json.get("stub"):
        return False
    if record_json.get("status") in FAIL_CLOSED_STATUSES:
        return False
    legacy = {
        "status": source_record.get("legacy_treatment_status") or source_record.get("treatment_status"),
        "as_of": source_record.get("legacy_treatment_as_of") or source_record.get("treatment_as_of"),
        "note": source_record.get("legacy_treatment_note") or source_record.get("treatment_note"),
        "by": source_record.get("legacy_treatment_by") or source_record.get("treatment_by") or [],
    }
    page_legacy = legacy_treatment_from_page(source_record.get("page_path"))
    for key, value in page_legacy.items():
        if legacy.get(key) in (None, "", []):
            legacy[key] = value
    legacy_status = normalize_roster_value(legacy.get("status"))
    if not legacy_status and seed_preseeded_treatment(record_json, page_legacy):
        return True
    mapping = (migration.get("mappings") or {}).get(legacy_status)
    if not mapping:
        set_record_status(record_json, "blocked", "legacy treatment value lacks migration mapping")
        record_json["identity"]["reason_code"] = record_json["identity"].get("reason_code") or "treatment_migration_unmapped"
        append_warning(record_json, "legacy treatment value lacks migration mapping: %s" % (legacy.get("status") or "<missing>"))
        return True

    field_i = mapping["field_i_validity"]
    old = json.dumps(record_json.get("treatment", {}), sort_keys=True)
    edge_field_ii = (mapping.get("edge_field_ii") or [None])[0]
    by_cases = controlling_cases_from_legacy(legacy.get("by"), edge_field_ii) if edge_field_ii else []
    treatment = record_json["treatment"]
    treatment.update({
        "field_i_validity": field_i,
        "as_of_content": source_record.get("date_decided") or None,
        "as_of_treatment": str(legacy.get("as_of")) if legacy.get("as_of") else None,
        "composite_basis": "migration-seed",
        "composite_basis_ref": source_record.get("title") or source_record.get("caption") or record_json["record_id"],
        "varies_by_point": bool(mapping.get("varies_by_point")),
        "scope_note": legacy.get("note") or mapping.get("notes") or "Treatment seeded from the sanctioned legacy migration table; three-lane derivation must confirm.",
    })
    if record_json.get("status") == "verified":
        set_record_status(record_json, "under_review", "migration seed requires R15 structural gates")
    if mapping.get("requires_point_overrides") and by_cases and not treatment.get("point_overrides"):
        treatment["point_overrides"] = [{
            "point": "legacy-limited-" + slugify(record_json["record_id"]),
            "point_label": "Legacy limited treatment point",
            "field_i_validity": field_i,
            "as_of_treatment": treatment["as_of_treatment"] or utc_now().date().isoformat(),
            "s3_binding_status": "provisional",
            "by": by_cases,
            "scope_note": legacy.get("note") or "Legacy limited treatment seed; S9 must adjudicate the point.",
        }]
    if mapping.get("requires_edge") and by_cases:
        existing = {
            (edge.get("citing_case", {}).get("name"), edge.get("field_ii"))
            for edge in treatment.get("edges") or []
        }
        for case in by_cases:
            key = (case["name"], edge_field_ii)
            if key not in existing:
                treatment.setdefault("edges", []).append({
                    "citing_case": case,
                    "field_ii": edge_field_ii,
                    "field_iii": "mentioned",
                    "point": None,
                    "proposed": True,
                    "journal_ref": "migration:%s" % legacy_status,
                })
    if (mapping.get("requires_edge") or mapping.get("requires_point_overrides")) and not by_cases:
        append_warning(record_json, "legacy treatment %s requires edge metadata; staged for S9 review" % legacy_status)
    append_warning(record_json, "legacy treatment migrated: %s -> %s" % (legacy_status, field_i))
    record_json["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance("_treatment-migration.json + page frontmatter")
    return json.dumps(record_json.get("treatment", {}), sort_keys=True) != old


def write_case_record(paths, record_json):
    record_json["provenance"]["date_modified"] = iso_now()
    os.makedirs(paths.cases, exist_ok=True)
    record_id = record_json["record_id"]
    write_json(os.path.join(paths.cases, record_id + ".json"), record_json)


def load_case_record(paths, record_id):
    path = os.path.join(paths.cases, record_id + ".json")
    if not os.path.exists(path):
        return None
    return read_json(path)


def remove_frontier_partial_record(paths, unresolved_id, final_id):
    if not unresolved_id or unresolved_id == final_id:
        return False
    path = os.path.join(paths.cases, unresolved_id + ".json")
    if not os.path.exists(path):
        return False
    try:
        partial = read_json(path)
    except (OSError, json.JSONDecodeError):
        return False
    identity = partial.get("identity") or {}
    if partial.get("record_id") == unresolved_id and partial.get("status") in ("draft", "blocked") and identity.get("identity_method") in ("pending", "blocked"):
        os.remove(path)
        return True
    return False


class ManifestStore:
    def __init__(self, path):
        self.path = path
        self.data = read_json(path)
        self.normalized = False
        for row in self.data.get("records", []):
            before = row.get("court_level")
            row.update(normalize_source_record(row))
            if row.get("court_level") != before:
                self.normalized = True
            row.setdefault("lane_status", frontier_stub_lane_status() if row.get("stub") else default_lane_status())
            row.setdefault("counts", {})
        self.by_record_id = {row["record_id"]: row for row in self.data.get("records", [])}

    def ensure_build_id(self, override=None):
        if override:
            self.data["build_id"] = override
            self.data["active_journal"] = "s2-ingest-%s.jsonl" % override
            return override
        build_id = self.data.get("build_id")
        if not build_id:
            seed = "%s|%s|%s" % (
                self.data.get("schema_version") or "s2",
                self.data.get("generated_at") or iso_now(),
                len(self.data.get("records", [])),
            )
            build_id = "s2-build-%s" % sha1_text(seed)[:12]
            self.data["build_id"] = build_id
            self.data["active_journal"] = "s2-ingest-%s.jsonl" % build_id
        return build_id

    def resume_rows(self):
        return resume_rows_from_manifest(self.data.get("records", []))

    def select(self, smoke_slug=None):
        records = self.data.get("records", [])
        if not smoke_slug:
            return records
        for row in records:
            keys = {
                row.get("record_id"),
                row.get("slug"),
                slugify(row.get("record_id") or ""),
                slugify(row.get("title") or row.get("caption") or ""),
            }
            if smoke_slug in keys:
                return [row]
        raise SystemExit("smoke slug not found in manifest: %s" % smoke_slug)

    def resolve_record_id(self, identifier):
        for row in self.data.get("records", []):
            keys = {
                row.get("record_id"),
                row.get("title"),
                row.get("caption"),
                row.get("slug"),
                slugify(row.get("record_id") or ""),
                slugify(row.get("title") or row.get("caption") or ""),
            }
            if identifier in keys:
                return row.get("record_id")
        return None

    def reset_for_readjudication(self, record_id):
        row = self.by_record_id.get(record_id)
        if not row:
            return None
        row["status"] = "pending"
        row["lane_status"] = default_lane_status()
        row["counts"] = {}
        row.pop("cluster_id", None)
        row.pop("lead_opinion_id", None)
        row.pop("official_cite", None)
        row["last_record_write"] = iso_now()
        return row

    def update_lane_status(self, row, record_id, resume_state):
        lane_status = row.setdefault("lane_status", default_lane_status())
        for step in ("identity", "citations", "pinpoints", "progeny"):
            status = resume_state.step_status(record_id, step)
            if status == "complete":
                lane_status[step] = "complete"
        treatment = lane_status.setdefault("treatment", {})
        for lane, _cap in TREATMENT_LANES:
            state = resume_state.lane_status(record_id, "treatment", lane)
            status = state.get("status")
            if status in ("partial", "complete"):
                existing = treatment.get(lane)
                existing_status = existing.get("status") if isinstance(existing, dict) else existing
                if state.get("skipped") and existing_status == status:
                    continue
                treatment[lane] = {
                    "status": status,
                    "cursor": state.get("cursor"),
                }
                if state.get("reviewed") is not None:
                    treatment[lane]["reviewed"] = state.get("reviewed")
                if state.get("proposed") is not None:
                    treatment[lane]["proposed"] = state.get("proposed")
                if state.get("cap_hit") is not None:
                    treatment[lane]["cap_hit"] = state.get("cap_hit")
                if state.get("retry_pending") is not None:
                    treatment[lane]["retry_pending"] = bool(state.get("retry_pending"))
                if state.get("fetch_failed") is not None:
                    treatment[lane]["fetch_failed"] = bool(state.get("fetch_failed"))
                if state.get("note") is not None:
                    treatment[lane]["note"] = state.get("note")
                if state.get("failed_step") is not None:
                    treatment[lane]["failed_step"] = state.get("failed_step")

    def update(self, old_record_id, record_json, counts=None, final_record_id=None, resume_state=None):
        row = self.by_record_id.get(old_record_id)
        if not row:
            return
        if final_record_id and final_record_id != old_record_id:
            row["record_id"] = final_record_id
            row["record_id_status"] = "resolved"
            self.by_record_id[final_record_id] = row
            self.by_record_id.pop(old_record_id, None)
        row["status"] = record_json.get("status")
        row["counts"].update(counts or {})
        row["last_record_write"] = iso_now()
        row["cluster_id"] = record_json["identity"].get("cluster_id")
        row["lead_opinion_id"] = record_json["identity"].get("lead_opinion_id")
        row["official_cite"] = record_json["citations"].get("display")
        if resume_state:
            self.update_lane_status(row, old_record_id, resume_state)
            if final_record_id and final_record_id != old_record_id:
                self.update_lane_status(row, final_record_id, resume_state)

    def regenerate_counts(self):
        records = self.data.get("records", [])
        status_counts = Counter(row.get("status") for row in records if isinstance(row, dict))
        counts = self.data.setdefault("counts", {})
        counts["total_manifest_records"] = len(records)
        counts["status_counts"] = {
            str(status): count
            for status, count in sorted(status_counts.items(), key=lambda item: str(item[0]))
        }

    def assert_unique_record_ids(self):
        seen = {}
        duplicates = {}
        for idx, row in enumerate(self.data.get("records", [])):
            if not isinstance(row, dict):
                raise ValueError("manifest record at index %s is not an object" % idx)
            record_id = row.get("record_id")
            if not record_id:
                raise ValueError("manifest record at index %s missing record_id" % idx)
            if record_id in seen:
                duplicates.setdefault(record_id, [seen[record_id]]).append(idx)
            else:
                seen[record_id] = idx
        if duplicates:
            summary = ", ".join(
                "%s at records[%s]" % (record_id, ",".join(str(idx) for idx in indexes))
                for record_id, indexes in sorted(duplicates.items())
            )
            raise ValueError("duplicate manifest record_id(s): %s" % summary)

    def save(self):
        self.assert_unique_record_ids()
        self.data["generated_at"] = self.data.get("generated_at")
        write_json(self.path, self.data)


def unique_preserve_order(values):
    out = []
    seen = set()
    for value in values:
        value = str(value or "").strip()
        if value and value not in seen:
            seen.add(value)
            out.append(value)
    return out


def clean_s6_candidate_value(value):
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def read_s6_candidate_queue(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError("%s:%s: invalid JSONL row: %s" % (path, line_no, exc)) from exc
            if not isinstance(row, dict):
                raise ValueError("%s:%s: candidate queue row must be a JSON object" % (path, line_no))
            if not clean_s6_candidate_value(row.get("caption")):
                if "queue" in row and ("rows" in row or "note" in row or "generated" in row):
                    continue
                raise ValueError("%s:%s: candidate queue row missing caption" % (path, line_no))
            rows.append((line_no, row))
    return rows


def s6_candidate_year(candidate):
    date = clean_s6_candidate_value(candidate.get("date") or candidate.get("date_decided"))
    if date:
        m = re.match(r"^((?:17|18|19|20)\d{2})", date)
        if m:
            return int(m.group(1))
    cite = clean_s6_candidate_value(candidate.get("citation") or candidate.get("expected_citation"))
    if cite:
        matches = re.findall(r"\b((?:17|18|19|20)\d{2})\b", cite)
        if matches:
            return int(matches[-1])
    return None


def s6_candidate_court_fields(candidate):
    court = clean_s6_candidate_value(candidate.get("court"))
    court_level = normalize_court_class(court)
    circuit = None
    if court_level == "other":
        circuit = parse_circuit(court)
        if circuit:
            court_level = "coa"
    return court, court_level, circuit


def s6_candidate_roster_key(row):
    return "|".join(
        normalize_roster_value(value)
        for value in (
            row.get("caption"),
            row.get("court") or row.get("court_level"),
            row.get("date") or row.get("date_decided") or row.get("year"),
            row.get("docket") or row.get("expected_citation") or row.get("citation"),
            row.get("source"),
            row.get("source_row_index"),
            row.get("prong"),
            row.get("posture"),
        )
    )


def unresolved_s6_candidate_record_id(caption, roster_key):
    slug = bounded_record_slug(caption, limit=72)
    return "UNRESOLVED:s6-candidate-%s-%s" % (slug, sha1_text(roster_key)[:8])


def s6_candidate_manifest_row(candidate, line_no):
    caption = clean_s6_candidate_value(candidate.get("caption"))
    leg = clean_s6_candidate_value(candidate.get("leg"))
    if not caption:
        raise ValueError("S6 candidate row missing caption")
    if not leg:
        raise ValueError("S6 candidate row for %s missing leg" % caption)
    if "/" in leg or "\\" in leg:
        raise ValueError("S6 candidate leg must be a simple path segment: %r" % leg)

    citation = clean_s6_candidate_value(candidate.get("citation") or candidate.get("expected_citation"))
    docket = clean_s6_candidate_value(candidate.get("docket"))
    date = clean_s6_candidate_value(candidate.get("date") or candidate.get("date_decided"))
    court, court_level, circuit = s6_candidate_court_fields(candidate)
    year = s6_candidate_year(candidate)
    source = S6_CANDIDATE_SOURCE_PREFIX + leg
    row = {
        "record_id_status": "UNRESOLVED",
        "source": source,
        "stub": True,
        "page_path": None,
        "slug": slugify(caption),
        "caption": caption,
        "status": "pending",
        "lane_status": frontier_stub_lane_status(),
        "counts": {},
        "last_record_write": iso_now(),
        "source_row_index": line_no,
        "leg": leg,
    }
    if citation:
        row["citation"] = citation
        row["expected_citation"] = citation
    if docket:
        row["docket"] = docket
    if date:
        row["date"] = date
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
            row["date_decided"] = date
    if year is not None:
        row["year"] = year
    if court:
        row["court"] = court
    if court_level:
        row["court_level"] = court_level
    if circuit:
        row["circuit"] = circuit
    for field in ("prong", "posture"):
        value = clean_s6_candidate_value(candidate.get(field))
        if value:
            row[field] = value
    if "page_candidate" in candidate:
        row["page_candidate"] = bool(candidate.get("page_candidate"))

    row["roster_key"] = s6_candidate_roster_key(row)
    row["roster_key_sha1"] = sha1_text(normalized_roster_key(row))
    row["record_id"] = unresolved_s6_candidate_record_id(caption, row["roster_key"])
    return row


def manifest_row_caption_slug(row):
    value = row.get("slug") or row.get("caption") or row.get("title")
    return slugify(value) if value else None


def docket_compare_key(value):
    value = normalize_roster_value(value)
    if not value:
        return None
    value = re.sub(r"^(?:no\.?|docket(?:\s+no\.?)?)\s+", "", value)
    return value or None


def citation_values(value):
    if value is None:
        return []
    if isinstance(value, dict):
        return [citation_to_string(value)]
    if isinstance(value, (list, tuple)):
        out = []
        for item in value:
            out.extend(citation_values(item))
        return out
    return [part.strip() for part in re.split(r"\s*;\s*", str(value)) if part.strip()]


def citation_has_dedupe_page_number(value):
    cite = normalize_cite(value)
    if not cite or "___" in cite:
        return False
    if isinstance(value, dict) and "page" in value:
        page = str(value.get("page") or "").strip()
        return bool(page and "___" not in page and re.search(r"\d", page))
    return re.search(r"^\s*\d+[A-Za-z]*\s+.+\s+\d+[A-Za-z]*(?:[-\u2013]\d+[A-Za-z]*)?\s*$", cite) is not None


def citation_compare_keys_from_value(value):
    keys = set()
    for cite in citation_values(value):
        if not citation_has_dedupe_page_number(cite):
            continue
        key = citation_compare_key(cite)
        if key:
            keys.add(key)
    return keys


def manifest_row_citation_keys(row):
    keys = set()
    for field in ("expected_citation", "citation", "official_cite", "parallel_cite", "neutral_cite"):
        keys.update(citation_compare_keys_from_value(row.get(field)))
    return keys


def index_manifest_candidate_row(indexes, row):
    record_id = row.get("record_id")
    if not record_id:
        return
    slug = manifest_row_caption_slug(row)
    if slug:
        indexes["caption_slug"].setdefault(slug, row)
    docket = docket_compare_key(row.get("docket"))
    if docket:
        indexes["docket"].setdefault(docket, row)
    for key in manifest_row_citation_keys(row):
        indexes["citation"].setdefault(key, row)


def build_manifest_candidate_dedupe(records):
    indexes = {"caption_slug": {}, "docket": {}, "citation": {}}
    for row in records:
        if isinstance(row, dict):
            index_manifest_candidate_row(indexes, row)
    return indexes


def find_s6_candidate_duplicate(row, indexes):
    checks = (
        ("caption-slug", row.get("slug"), indexes["caption_slug"]),
        ("docket", docket_compare_key(row.get("docket")), indexes["docket"]),
    )
    for field, key, index in checks:
        if key and key in index:
            return field, key, index[key]
    for key in sorted(manifest_row_citation_keys(row)):
        if key in indexes["citation"]:
            return "citation", key, indexes["citation"][key]
    return None


def journal_s6_candidate_skip(journal, row, duplicate, queue_path):
    duplicate_field, duplicate_key, existing = duplicate
    journal.append(
        step="s6-candidate-intake",
        action="skip-duplicate",
        status="skipped",
        leg=row.get("leg"),
        adjudicated_by=S6_CANDIDATE_INTAKE_ADJUDICATOR,
        queue_path=queue_path,
        source_row_index=row.get("source_row_index"),
        caption=row.get("caption"),
        docket=row.get("docket"),
        citation=row.get("citation"),
        duplicate_by=duplicate_field,
        duplicate_key=duplicate_key,
        existing_record_id=existing.get("record_id"),
        existing_status=existing.get("status"),
        existing_source=existing.get("source"),
    )


def journal_s6_candidate_append(journal, row, queue_path):
    journal.append(
        step="s6-candidate-intake",
        action="append",
        status="pending",
        record_id=row.get("record_id"),
        leg=row.get("leg"),
        adjudicated_by=S6_CANDIDATE_INTAKE_ADJUDICATOR,
        queue_path=queue_path,
        source=row.get("source"),
        source_row_index=row.get("source_row_index"),
        caption=row.get("caption"),
        docket=row.get("docket"),
        citation=row.get("citation"),
        page_candidate=row.get("page_candidate"),
    )


def add_s6_candidates(manifest, journal, queue_path):
    records = manifest.data.setdefault("records", [])
    indexes = build_manifest_candidate_dedupe(records)
    appended = []
    skipped = []
    for line_no, candidate in read_s6_candidate_queue(queue_path):
        row = s6_candidate_manifest_row(candidate, line_no)
        duplicate = find_s6_candidate_duplicate(row, indexes)
        if duplicate:
            skipped.append({"row": row, "duplicate": duplicate})
            journal_s6_candidate_skip(journal, row, duplicate, queue_path)
            continue
        records.append(row)
        manifest.by_record_id[row["record_id"]] = row
        index_manifest_candidate_row(indexes, row)
        appended.append(row)
        journal_s6_candidate_append(journal, row, queue_path)
    manifest.regenerate_counts()
    return {"appended": appended, "skipped": skipped}


def read_readjudicate_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    stripped = text.strip()
    if not stripped:
        return []
    if stripped.startswith("["):
        data = json.loads(stripped)
        if not isinstance(data, list):
            raise ValueError("readjudicate file JSON must be a list")
        return [str(item).strip() for item in data if str(item).strip()]
    values = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        values.append(line)
    return values


def readjudication_identifiers(args):
    values = list(args.readjudicate or [])
    for path in args.readjudicate_file or []:
        values.extend(read_readjudicate_file(path))
    return unique_preserve_order(values)


def append_resume_reset_rows(journal, record_id):
    for step in ("identity", "citations", "pinpoints", "progeny"):
        journal.append(record_id=record_id, step=step, status="pending", adjudication_reset=True)
    for lane, _cap in TREATMENT_LANES:
        journal.append(record_id=record_id, step="treatment", lane=lane, status="pending", adjudication_reset=True)


def readjudication_roster_source(row):
    return normalize_source_record({
        key: row.get(key)
        for key in READJUDICATION_ROSTER_KEYS
        if key in row
    })


def field_has_payload(value):
    if isinstance(value, dict):
        return any(field_has_payload(item) for item in value.values())
    if isinstance(value, list):
        return bool(value)
    return value not in (None, "", False)


def journal_readjudication_field_resets(journal, record_id, before_record, after_record):
    before_record = before_record or {}
    for field in READJUDICATION_RESET_FIELDS:
        before_value = before_record.get(field)
        after_value = after_record.get(field)
        row = {
            "step": "adjudication.field-reset",
            "record_id": record_id,
            "field": field,
            "status": "reset",
            "before_populated": field_has_payload(before_value),
            "reset_to_empty_shell": True,
        }
        if field == "identity":
            row["before_cluster_id"] = (before_value or {}).get("cluster_id") if isinstance(before_value, dict) else None
            row["after_cluster_id"] = (after_value or {}).get("cluster_id") if isinstance(after_value, dict) else None
        journal.append(**row)


def read_adjudication_file(path):
    if not path:
        raise ValueError("--elevate-off-cl requires --adjudication <file>")
    return read_json(path)


def citation_object_from_adjudication(value, selected_official=False):
    cite = stripped_citation_text(value)
    if not cite:
        raise ValueError("off-CL adjudication citation is empty")
    if isinstance(value, dict):
        return {
            "cite": cite,
            "volume": value.get("volume"),
            "reporter": citation_reporter(value) or value.get("reporter") or None,
            "page": value.get("page"),
            "type": value.get("type") or ("official" if selected_official else "parallel"),
            "selected_official": bool(selected_official),
            "source": value.get("source") or "off_cl.adjudication",
        }
    return {
        "cite": cite,
        "volume": None,
        "reporter": citation_reporter(cite) or None,
        "page": None,
        "type": "official" if selected_official else "parallel",
        "selected_official": bool(selected_official),
        "source": "off_cl.adjudication",
    }


def normalize_off_cl_citations(citations):
    if not isinstance(citations, dict):
        raise ValueError("off-CL adjudication citations must be an object")
    official = citation_object_from_adjudication(citations.get("official"), selected_official=True)
    parallel_values = citations.get("parallel") or []
    vendor_values = citations.get("vendor_neutral") or []
    if isinstance(parallel_values, (str, dict)):
        parallel_values = [parallel_values]
    if isinstance(vendor_values, (str, dict)):
        vendor_values = [vendor_values]
    parallel = [citation_object_from_adjudication(value) for value in parallel_values]
    vendor = [citation_object_from_adjudication(value) for value in vendor_values]
    display = stripped_citation_text(citations.get("display")) or normalize_cite(official)
    return {
        "official": official,
        "parallel": parallel,
        "vendor_neutral": vendor,
        "all": [official] + parallel + vendor,
        "display": display,
        "official_selection": {
            "court_class": citations.get("official_selection", {}).get("court_class") if isinstance(citations.get("official_selection"), dict) else None,
            "selected": display,
            "reason": "off_cl_adjudication",
        },
    }


def require_iso_date(value, field):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("%s must be YYYY-MM-DD" % field)
    return value


def normalize_off_cl_links(links):
    if not isinstance(links, list):
        raise ValueError("off_cl_links must be a list")
    out = []
    for index, link in enumerate(links):
        if not isinstance(link, dict):
            raise ValueError("off_cl_links[%s] must be an object" % index)
        source = link.get("source")
        if source not in OFF_CL_ALLOWED_SOURCES:
            raise ValueError("off_cl_links[%s].source is not R14-whitelisted: %r" % (index, source))
        url = str(link.get("url") or "").strip()
        parsed = urllib.parse.urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise ValueError("off_cl_links[%s].url must be an absolute http(s) URI" % index)
        confirmed = link.get("confirmed")
        if not isinstance(confirmed, dict):
            raise ValueError("off_cl_links[%s].confirmed must be an object" % index)
        normalized_confirmed = {}
        for field in ("caption", "cite", "court", "date"):
            value = confirmed.get(field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError("off_cl_links[%s].confirmed.%s must be a non-empty string" % (index, field))
            normalized_confirmed[field] = value.strip()
        require_iso_date(normalized_confirmed["date"], "off_cl_links[%s].confirmed.date" % index)
        checked_date = require_iso_date(link.get("checked_date"), "off_cl_links[%s].checked_date" % index)
        out.append({
            "source": source,
            "url": url,
            "confirmed": normalized_confirmed,
            "checked_date": checked_date,
        })
    distinct_sources = {link["source"] for link in out}
    if len(distinct_sources) < 2:
        raise ValueError("verified_off_cl requires at least two distinct R14-whitelisted sources")
    return out


def verify_off_cl_adjudication(adjudication, record_id=None):
    if not isinstance(adjudication, dict):
        raise ValueError("off-CL adjudication file must be a JSON object")
    if adjudication.get("record_id") not in (None, record_id):
        raise ValueError("off-CL adjudication record_id does not match %s" % record_id)
    if "trail" not in adjudication:
        raise ValueError("off-CL adjudication file must include trail")
    citations = normalize_off_cl_citations(adjudication.get("citations"))
    links = normalize_off_cl_links(adjudication.get("off_cl_links"))
    return citations, links, adjudication.get("trail")


def apply_off_cl_elevation(paths, manifest, journal, identifier, adjudication_path, build_run):
    if not adjudication_path:
        raise SystemExit("--elevate-off-cl requires --adjudication <file>; builder never self-elevates")
    record_id = manifest.resolve_record_id(identifier)
    if not record_id:
        raise SystemExit("off-CL elevation record not found in manifest: %s" % identifier)
    row = manifest.by_record_id.get(record_id)
    if not row:
        raise SystemExit("off-CL elevation record not found in manifest: %s" % identifier)
    previous_record = load_case_record(paths, record_id)
    previous_status = (previous_record or {}).get("status") or row.get("status")
    if previous_status != "not_found":
        raise SystemExit("off-CL elevation requires a terminal not_found record: %s is %s" % (record_id, previous_status))
    adjudication = read_adjudication_file(adjudication_path)
    citations, links, trail = verify_off_cl_adjudication(adjudication, record_id=record_id)

    manifest.reset_for_readjudication(record_id)
    source_record = readjudication_roster_source(row)
    record_json = empty_record_shell(record_id, source_record, build_run)
    caption = (
        adjudication.get("case_name")
        or links[0]["confirmed"]["caption"]
        or source_record.get("title")
        or source_record.get("caption")
        or record_id
    )
    record_json["identity"].update({
        "case_name": caption,
        "case_name_short": adjudication.get("case_name_short") or caption,
        "case_name_full": adjudication.get("case_name_full") or caption,
        "court": source_record.get("court") or links[0]["confirmed"]["court"],
        "court_id": None,
        "court_level": source_record.get("court_level") or "other",
        "date_decided": source_record.get("date_decided") or links[0]["confirmed"]["date"],
        "year": source_record.get("year"),
        "docket": source_record.get("docket") or None,
        "cluster_id": None,
        "lead_opinion_id": None,
        "sibling_ids": [],
        "absolute_url": None,
        "identity_method": "off_cl",
        "expected_citation_found": True,
        "party_name_in_text": True,
        "canonical_name_match": True,
        "reason_code": "outside_cl_corpus_verified_by_off_cl_two_key",
    })
    record_json["citations"] = citations
    record_json["off_cl_links"] = links
    record_json["progeny"].update({
        "complete_query": None,
        "indexed_citing_opinions": None,
        "count_source": "off_cl_na",
        "per_sibling": [],
        "citation_count": None,
        "cache_path": None,
        "enumeration": None,
        "cursor": None,
        "rows_cached": 0,
        "outbound_opinion_edges": [],
    })
    set_record_status(record_json, "verified_off_cl", explicit_adjudication=True)
    record_json["provenance"]["field_provenance"]["identity"] = base_field_provenance(
        "off-CL adjudication file: %s" % adjudication_path,
        verifier=READJUDICATION_ADJUDICATOR,
    )
    record_json["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance(
        "verified_off_cl: CL treatment lanes intentionally not run",
        verifier=READJUDICATION_ADJUDICATOR,
    )
    record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance(
        "verified_off_cl: no CL-derived point overrides",
        verifier=READJUDICATION_ADJUDICATOR,
    )
    record_json["provenance"]["field_provenance"]["pinpoints"] = base_field_provenance(
        "verified_off_cl: no CL lead-opinion pinpoints",
        verifier=READJUDICATION_ADJUDICATOR,
    )

    journal_readjudication_field_resets(journal, record_id, previous_record, record_json)
    write_case_record(paths, record_json)
    journal.append(
        step="adjudication",
        record_id=record_id,
        action="elevate-off-cl",
        status="verified_off_cl",
        adjudicated_by=READJUDICATION_ADJUDICATOR,
        adjudication_file=adjudication_path,
        off_cl_sources=sorted({link["source"] for link in links}),
        trail=trail,
    )
    journal.append(record_id=record_id, step="identity", status="complete", final_status="verified_off_cl", off_cl=True)
    journal.append(record_id=record_id, step="citations", status="complete", official=record_json["citations"]["display"], off_cl=True)
    journal.append(record_id=record_id, step="pinpoints", status="complete", skipped=True, off_cl_na=True)
    journal.append(record_id=record_id, step="progeny", status="complete", skipped=True, count_source="off_cl_na")
    manifest.update(
        record_id,
        record_json,
        counts={"cl_calls": 0},
        final_record_id=record_id,
        resume_state=ResumeState(journal.rows()),
    )
    return record_json


def apply_readjudications(paths, manifest, journal, identifiers, build_run):
    reset_ids = []
    for identifier in identifiers:
        record_id = manifest.resolve_record_id(identifier)
        if not record_id:
            raise SystemExit("readjudicate record not found in manifest: %s" % identifier)
        row = manifest.reset_for_readjudication(record_id)
        if not row:
            raise SystemExit("readjudicate record not found in manifest: %s" % identifier)
        source_record = readjudication_roster_source(row)
        previous_record = load_case_record(paths, record_id)
        record_json = empty_record_shell(record_id, source_record, build_run)
        set_record_status(
            record_json,
            "pending",
            "adjudicated reset for %s" % ",".join(READJUDICATION_FINDINGS),
            explicit_adjudication=True,
        )
        journal_readjudication_field_resets(journal, record_id, previous_record, record_json)
        write_case_record(paths, record_json)
        journal.append(
            step="adjudication",
            record_id=record_id,
            findings=READJUDICATION_FINDINGS,
            adjudicated_by=READJUDICATION_ADJUDICATOR,
            action="reset-identity-and-rerun",
        )
        append_resume_reset_rows(journal, record_id)
        reset_ids.append(record_id)
    return reset_ids


def validate_rerun_lanes(lanes):
    lanes = unique_preserve_order(lanes)
    unknown = [lane for lane in lanes if lane not in TREATMENT_LANE_NAMES]
    if unknown:
        raise SystemExit("--rerun-lane must be one of %s; got %s" % (", ".join(TREATMENT_LANE_NAMES), ", ".join(unknown)))
    return lanes


def selected_manifest_rows(manifest, identifiers):
    if not identifiers:
        return list(manifest.data.get("records", []))
    rows = []
    seen = set()
    for identifier in unique_preserve_order(identifiers):
        record_id = manifest.resolve_record_id(identifier)
        if not record_id:
            raise SystemExit("--records target not found in manifest: %s" % identifier)
        if record_id in seen:
            continue
        seen.add(record_id)
        rows.append(manifest.by_record_id[record_id])
    return rows


def reset_record_lanes_for_rerun(paths, manifest, journal, lanes, identifiers=None):
    selected = []
    explicit = bool(identifiers)
    for row in selected_manifest_rows(manifest, identifiers or []):
        record_id = row.get("record_id")
        if row.get("stub"):
            if explicit:
                raise SystemExit("--rerun-lane target is a stub/frontier record: %s" % record_id)
            continue
        record_json = load_case_record(paths, record_id)
        if not record_json:
            if explicit:
                raise SystemExit("--rerun-lane target has no case record: %s" % record_id)
            continue
        if record_json.get("status") != "under_review":
            if explicit:
                raise SystemExit("--rerun-lane target is not under_review: %s is %s" % (record_id, record_json.get("status")))
            continue
        treatment = record_json.setdefault("treatment", {})
        derivation = treatment.setdefault("derivation", {})
        lane_status = row.setdefault("lane_status", default_lane_status())
        treatment_status = lane_status.setdefault("treatment", {})
        for lane in lanes:
            derivation.pop(lane, None)
            treatment_status[lane] = {"status": "pending", "cursor": None}
            journal.append(
                record_id=record_id,
                step="treatment",
                lane=lane,
                status="pending",
                adjudication_reset=True,
                findings=LANE_RERUN_FINDINGS,
                action="reset-treatment-lane",
            )
        journal.append(
            step="adjudication",
            record_id=record_id,
            action="reset-treatment-lanes-for-rerun",
            lanes=lanes,
            findings=LANE_RERUN_FINDINGS,
            adjudicated_by=READJUDICATION_ADJUDICATOR,
            status="reset",
        )
        write_case_record(paths, record_json)
        selected.append(row)
    if explicit and not selected:
        raise SystemExit("--rerun-lane did not select any under_review records")
    return selected


def lane_scoped_resume(rows, record_id, lanes):
    scoped = list(rows)
    prior = ResumeState(scoped)
    targets = set(lanes)
    for lane in TREATMENT_LANE_NAMES:
        if lane in targets:
            scoped.append({
                "record_id": record_id,
                "step": "treatment",
                "lane": lane,
                "status": "pending",
                "cursor": None,
            })
        else:
            scoped.append(treatment_lane_resume_row(
                record_id,
                lane,
                prior.lane_status(record_id, "treatment", lane),
                skipped=True,
            ))
    return ResumeState(scoped)


def case_json_paths(paths):
    if not os.path.isdir(paths.cases):
        return []
    return [
        os.path.join(paths.cases, name)
        for name in sorted(os.listdir(paths.cases))
        if name.endswith(".json")
    ]


def case_lookup_key(value):
    text = strip_wikilink(value)
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = re.sub(r"\s+", " ", text).strip().casefold()
    return text


def official_cite_from_record(record):
    citations = record.get("citations") or {}
    official = stripped_citation_text(citations.get("official"))
    return official or stripped_citation_text(citations.get("display")) or None


def fallback_repo_path(paths, *parts):
    primary = os.path.join(paths.repo_root, *parts)
    if os.path.exists(primary):
        return primary
    return os.path.join(os.getcwd(), *parts)


def read_lake_schema(paths):
    return read_json(fallback_repo_path(paths, "_overhaul2", "lake", "_schema.json"))


def schema_field_ii_values(schema):
    values = (((schema.get("definitions") or {}).get("field_ii") or {}).get("enum") or [])
    return set(values)


def schema_s3_binding_status_values(schema):
    point_override = ((schema.get("definitions") or {}).get("point_override") or {})
    status = ((point_override.get("properties") or {}).get("s3_binding_status") or {})
    return set(status.get("enum") or [])


def parse_simple_yaml_value(value):
    value = value.strip()
    if not value:
        return ""
    if value in ("true", "false"):
        return value == "true"
    if value[0] in ("'", '"') and value[-1:] == value[0]:
        return value[1:-1]
    return value


def parse_s2_binding_rows(path):
    if not os.path.exists(path):
        return []
    rows = []
    section = None
    current = None
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.split("#", 1)[0].rstrip()
            if not line.strip():
                continue
            section_match = re.match(r"^(bound|pending):\s*$", line)
            if section_match:
                section = section_match.group(1)
                current = None
                continue
            if section not in ("bound", "pending"):
                continue
            item_match = re.match(r"^\s*-\s+([^:]+):\s*(.*)$", line)
            if item_match:
                current = {"_section": section}
                current[item_match.group(1).strip()] = parse_simple_yaml_value(item_match.group(2))
                rows.append(current)
                continue
            prop_match = re.match(r"^\s{4}([^:]+):\s*(.*)$", line)
            if prop_match and current is not None:
                current[prop_match.group(1).strip()] = parse_simple_yaml_value(prop_match.group(2))
    return rows


def load_s2_binding_statuses(paths, schema):
    status_values = schema_s3_binding_status_values(schema)
    bound_token = "bound" if "bound" in status_values else None
    provisional_token = "provisional" if "provisional" in status_values else None
    path = fallback_repo_path(paths, "_overhaul2", "points", "s2-binding.yaml")
    statuses = {}
    for row in parse_s2_binding_rows(path):
        if row.get("_section") == "bound" and row.get("row_type") == "point_override" and row.get("s2_point"):
            if bound_token:
                statuses[str(row["s2_point"])] = bound_token
        elif row.get("_section") == "pending" and provisional_token:
            for key in ("s2_point", "point", "pending_slug"):
                slug = row.get(key)
                if isinstance(slug, str) and slug and slug != "true":
                    statuses[slug] = provisional_token
    return statuses


def manifest_rows_by_record_id(paths):
    if not os.path.exists(paths.manifest):
        return {}
    manifest = read_json(paths.manifest)
    return {
        row.get("record_id"): row
        for row in manifest.get("records") or []
        if isinstance(row, dict) and row.get("record_id")
    }


def case_lookup_class(ref):
    source = ref.get("source")
    if source == "content/cases" or (ref.get("stub") is False and not str(ref.get("record_id") or "").count("--")):
        return "page"
    if ref.get("stub") or (source and source != "content/cases"):
        return "frontier"
    return "other"


def build_completed_case_lookup(paths):
    lookup = {}
    manifest_rows = manifest_rows_by_record_id(paths)
    for path in case_json_paths(paths):
        try:
            record = read_json(path)
        except (OSError, json.JSONDecodeError):
            continue
        identity = record.get("identity") or {}
        cluster_id = identity.get("cluster_id")
        manifest_row = manifest_rows.get(record.get("record_id")) or {}
        ref = {
            "record_id": record.get("record_id"),
            "cluster_id": int(cluster_id) if cluster_id is not None else None,
            "cite": official_cite_from_record(record),
            "source": manifest_row.get("source", record.get("source")),
            "stub": manifest_row.get("stub", record.get("stub")),
            "page_path": manifest_row.get("page_path") or record.get("page_path"),
            "path": path,
        }
        ref["lookup_class"] = case_lookup_class(ref)
        names = [
            record.get("record_id"),
            identity.get("input_case_name"),
            identity.get("case_name"),
            identity.get("case_name_full"),
            identity.get("case_name_short"),
        ]
        for name in names:
            key = case_lookup_key(name)
            if not key:
                continue
            bucket = lookup.setdefault(key, [])
            if not any(item["record_id"] == ref["record_id"] for item in bucket):
                bucket.append(ref)
    return lookup


def parse_controlling_case_entries(value):
    if value in (None, "", []):
        return []
    if isinstance(value, dict):
        return [dict(value)]
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(parse_controlling_case_entries(item))
        return out
    text = str(value).strip()
    if not text:
        return []
    if text.startswith("[") and text.endswith("]"):
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            parsed = None
        if parsed is not None:
            return parse_controlling_case_entries(parsed)
    wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)
    if wikilinks:
        return [{"name": strip_wikilink(name)} for name in wikilinks if strip_wikilink(name)]
    name = strip_wikilink(text)
    return [{"name": name}] if name else []


def migration_primary_field_ii(migration, mapping_name):
    edge_values = (migration.get("mappings", {}).get(mapping_name) or {}).get("edge_field_ii") or []
    return edge_values[0] if edge_values else None


def migration_case_list_matches(record_id, cases):
    record_key = case_lookup_key(record_id)
    record_tokens = caption_token_set(record_id)
    for case in cases or []:
        case_key = case_lookup_key(case)
        if case_key and case_key == record_key:
            return True
        case_tokens = caption_token_set(case)
        if case_tokens and record_tokens and case_tokens <= record_tokens:
            return True
    return False


def valid_field_ii(value, field_ii_values):
    text = str(value or "").strip()
    return bool(text) and (not field_ii_values or text in field_ii_values)


def migration_default_field_ii(record_id, override, migration, field_ii_values=None):
    if migration_case_list_matches(record_id, migration.get("limited_cases") or []):
        return migration_primary_field_ii(migration, "limited")
    existing = str(override.get("field_ii") or "").strip()
    if valid_field_ii(existing, field_ii_values):
        return existing
    field_i = normalize_roster_value(override.get("field_i_validity"))
    if field_i == "caution":
        return migration_primary_field_ii(migration, "limited")
    if field_i == "superseded":
        return migration_primary_field_ii(migration, "overruled")
    return None


def controlling_case_complete(entry):
    return (
        isinstance(entry, dict)
        and bool(str(entry.get("name") or "").strip())
        and entry.get("cluster_id") is not None
        and "cite" in entry
        and bool(str(entry.get("field_ii") or "").strip())
    )


def override_by_complete(override):
    by = override.get("by")
    return isinstance(by, list) and bool(by) and all(controlling_case_complete(entry) for entry in by)


def resolve_controlling_case(name, lookup, errors, record_id, context, warnings=None, dedupe_pointers=None):
    key = case_lookup_key(name)
    matches = lookup.get(key) or []
    if not matches:
        errors.append("%s %s unresolved controlling case %r: %s match(es)" % (record_id, context, name, len(matches)))
        return None
    page_matches = [ref for ref in matches if ref.get("lookup_class") == "page"]
    frontier_matches = [ref for ref in matches if ref.get("lookup_class") == "frontier"]
    if len(page_matches) == 1 and len(page_matches) + len(frontier_matches) == len(matches):
        ref = page_matches[0]
        for stub in frontier_matches:
            if dedupe_pointers is not None:
                dedupe_pointers.append({
                    "record_id": record_id,
                    "context": context,
                    "controlling_case": name,
                    "selected_record_id": ref.get("record_id"),
                    "passed_over_record_id": stub.get("record_id"),
                })
    elif len(matches) == 1:
        ref = matches[0]
    else:
        classes = {}
        for match in matches:
            classes.setdefault(match.get("lookup_class") or "other", []).append(match.get("record_id"))
        errors.append(
            "%s %s unresolved controlling case %r: %s match(es) by class %s"
            % (record_id, context, name, len(matches), json.dumps(classes, sort_keys=True))
        )
        return None
    if ref.get("cluster_id") is None:
        errors.append("%s %s controlling case %r has no cluster_id in lake record %s" % (record_id, context, name, ref.get("record_id")))
        return None
    cite = ref.get("cite") or None
    if cite is None:
        if warnings is not None:
            warnings.append(CONTROLLING_CASE_NO_OFFICIAL_CITE_WARNING)
    return {"name": name, "cluster_id": ref["cluster_id"], "cite": cite}


def point_override_binding_status(override, binding_statuses, status_values):
    point = str(override.get("point") or "")
    if point in binding_statuses:
        return binding_statuses[point]
    existing = str(override.get("s3_binding_status") or "").strip()
    if existing in status_values:
        return existing
    return "provisional" if "provisional" in status_values else None


def normalize_point_override_shape(record_id, override, repaired_by, binding_statuses, status_values, errors):
    normalized = {}
    for key in POINT_OVERRIDE_SCHEMA_KEYS:
        if key == "by":
            normalized[key] = repaired_by
            continue
        if key == "s3_binding_status":
            status = point_override_binding_status(override, binding_statuses, status_values)
            if not status:
                errors.append("%s point_override %r cannot derive s3_binding_status" % (record_id, override.get("point")))
                continue
            normalized[key] = status
            continue
        if key in override:
            normalized[key] = override[key]
        else:
            errors.append("%s point_override %r missing required key %r" % (record_id, override.get("point"), key))
    override.clear()
    override.update(normalized)


def repair_override_refs(record_id, override, lookup, migration, binding_statuses, status_values, field_ii_values, errors, warnings, dedupe_pointers):
    if "by" not in override:
        return False
    if (
        set(override) <= set(POINT_OVERRIDE_SCHEMA_KEYS)
        and override.get("s3_binding_status") in status_values
        and override_by_complete(override)
    ):
        return False
    before = json.dumps(override, sort_keys=True)
    default_field_ii = migration_default_field_ii(record_id, override, migration, field_ii_values)
    fallback_cite = stripped_citation_text(override.get("by_cite")) or None
    repaired = []
    entries = parse_controlling_case_entries(override.get("by"))
    if not entries:
        errors.append("%s point_override %r has no controlling case in by" % (record_id, override.get("point")))
        return False
    for entry in entries:
        name = strip_wikilink(entry.get("name"))
        if not name:
            errors.append("%s point_override %r has blank controlling case name" % (record_id, override.get("point")))
            continue
        resolved = resolve_controlling_case(
            name,
            lookup,
            errors,
            record_id,
            "point_override:%s" % override.get("point"),
            warnings=warnings,
            dedupe_pointers=dedupe_pointers,
        )
        if not resolved:
            continue
        entry_field_ii = str(entry.get("field_ii") or "").strip()
        field_ii = (entry_field_ii if valid_field_ii(entry_field_ii, field_ii_values) else None) or default_field_ii
        if not field_ii:
            errors.append("%s point_override %r controlling case %r cannot derive field_ii" % (record_id, override.get("point"), name))
            continue
        cite = resolved["cite"]
        if cite is None:
            cite = stripped_citation_text(entry.get("cite")) or fallback_cite
        new_entry = {
            "name": name,
            "cluster_id": entry.get("cluster_id") or resolved["cluster_id"],
            "cite": cite,
            "field_ii": field_ii,
        }
        repaired.append(new_entry)
    if repaired:
        normalize_point_override_shape(record_id, override, repaired, binding_statuses, status_values, errors)
    return json.dumps(override, sort_keys=True) != before


def repair_migration_edge(record_id, edge, lookup, errors, warnings, dedupe_pointers):
    if not str(edge.get("journal_ref") or "").startswith("migration:"):
        return False
    citing = edge.get("citing_case")
    if not isinstance(citing, dict):
        errors.append("%s migration edge has non-object citing_case" % record_id)
        return False
    before = json.dumps(edge, sort_keys=True)
    name = strip_wikilink(citing.get("name"))
    if not name:
        errors.append("%s migration edge has blank citing_case.name" % record_id)
        return False
    resolved = resolve_controlling_case(
        name,
        lookup,
        errors,
        record_id,
        "edge:%s" % edge.get("journal_ref"),
        warnings=warnings,
        dedupe_pointers=dedupe_pointers,
    )
    if not resolved:
        return False
    citing["name"] = name
    if not citing.get("cluster_id"):
        citing["cluster_id"] = resolved["cluster_id"]
    citing["cite"] = resolved["cite"]
    if not str(citing.get("field_ii") or "").strip() and edge.get("field_ii"):
        citing["field_ii"] = edge["field_ii"]
    return json.dumps(edge, sort_keys=True) != before


def repair_record_migration_refs(record, lookup, migration, binding_statuses, status_values, field_ii_values, errors, dedupe_pointers):
    treatment = record.get("treatment") or {}
    changed = False
    record_id = record.get("record_id")
    warnings = []
    for override in treatment.get("point_overrides") or []:
        if isinstance(override, dict):
            changed = repair_override_refs(
                record_id,
                override,
                lookup,
                migration,
                binding_statuses,
                status_values,
                field_ii_values,
                errors,
                warnings,
                dedupe_pointers,
            ) or changed
    for edge in treatment.get("edges") or []:
        if isinstance(edge, dict):
            changed = repair_migration_edge(record_id, edge, lookup, errors, warnings, dedupe_pointers) or changed
    existing_warnings = set(record.setdefault("provenance", {}).setdefault("warnings", []))
    for warning in warnings:
        append_warning(record, warning)
        if warning not in existing_warnings:
            changed = True
    if changed:
        append_warning(record, MIGRATION_REF_REPAIR_PROVENANCE)
        record["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance(
            MIGRATION_REF_REPAIR_PROVENANCE,
            verifier=READJUDICATION_ADJUDICATOR,
        )
    return changed


def repair_migration_refs(paths, journal, migration):
    schema = read_lake_schema(paths)
    binding_statuses = load_s2_binding_statuses(paths, schema)
    status_values = schema_s3_binding_status_values(schema)
    field_ii_values = schema_field_ii_values(schema)
    lookup = build_completed_case_lookup(paths)
    candidates = []
    errors = []
    dedupe_pointers = []
    for path in case_json_paths(paths):
        record = read_json(path)
        candidate = json.loads(json.dumps(record))
        if repair_record_migration_refs(
            candidate,
            lookup,
            migration,
            binding_statuses,
            status_values,
            field_ii_values,
            errors,
            dedupe_pointers,
        ):
            candidates.append((path, candidate))
    if errors:
        raise SystemExit("migration reference repair failed:\n" + "\n".join(sorted(errors)))
    for path, record in candidates:
        write_case_record(paths, record)
        journal.append(
            step="adjudication",
            record_id=record["record_id"],
            action="repair-migration-refs",
            findings=MIGRATION_REF_REPAIR_FINDINGS,
            adjudicated_by=READJUDICATION_ADJUDICATOR,
            status="repaired",
        )
    seen_pointers = set()
    for pointer in dedupe_pointers:
        key = json.dumps(pointer, sort_keys=True)
        if key in seen_pointers:
            continue
        seen_pointers.add(key)
        journal.append(
            step="dedupe",
            action="s6-dedupe-pointer",
            findings=MIGRATION_REF_REPAIR_FINDINGS,
            adjudicated_by=READJUDICATION_ADJUDICATOR,
            status="pointer",
            **pointer,
        )
    return [record["record_id"] for _path, record in candidates]


def repair_failclosed_treatment(paths, journal, record_ids=FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS):
    repaired = []
    journaled = {
        row.get("record_id")
        for row in journal.rows()
        if row.get("action") == "repair-failclosed-treatment"
    }
    for record_id in record_ids:
        path = os.path.join(paths.cases, record_id + ".json")
        if not os.path.exists(path):
            raise SystemExit("fail-closed treatment repair target missing: %s" % path)
        record = read_json(path)
        if record.get("status") not in FAIL_CLOSED_STATUSES:
            raise SystemExit(
                "fail-closed treatment repair target %r has status=%r"
                % (record_id, record.get("status"))
        )
        treatment = record.setdefault("treatment", {})
        if treatment.get("field_i_validity") == "unverified":
            provenance = record.get("provenance", {}).get("field_provenance", {}).get("treatment.field_i_validity", {})
            if provenance.get("src") == FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE and record_id not in journaled:
                journal.append(
                    step="adjudication",
                    record_id=record_id,
                    action="repair-failclosed-treatment",
                    findings=FAIL_CLOSED_TREATMENT_REPAIR_FINDINGS,
                    adjudicated_by=READJUDICATION_ADJUDICATOR,
                    status="repaired",
                    before_field_i_validity=None,
                    after_field_i_validity="unverified",
                )
                repaired.append(record_id)
            continue
        before = treatment.get("field_i_validity")
        treatment["field_i_validity"] = "unverified"
        append_warning(record, FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE)
        record.setdefault("provenance", {}).setdefault("field_provenance", {})[
            "treatment.field_i_validity"
        ] = base_field_provenance(
            FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE,
            verifier=READJUDICATION_ADJUDICATOR,
        )
        write_case_record(paths, record)
        journal.append(
            step="adjudication",
            record_id=record_id,
            action="repair-failclosed-treatment",
            findings=FAIL_CLOSED_TREATMENT_REPAIR_FINDINGS,
            adjudicated_by=READJUDICATION_ADJUDICATOR,
            status="repaired",
            before_field_i_validity=before,
            after_field_i_validity="unverified",
        )
        repaired.append(record_id)
    return repaired


def writable_repair_journal(paths, journal):
    try:
        journal.ensure_writable()
        return journal, False
    except OSError:
        fallback_path = os.path.join(paths.lake, "journal", os.path.basename(journal.path))
        fallback = Journal(fallback_path, journal.run_id)
        fallback.ensure_writable()
        return fallback, True


def load_lint13_validator():
    lint_dir = os.path.join(os.getcwd(), "scripts", "lint")
    if lint_dir not in sys.path:
        sys.path.insert(0, lint_dir)
    lint13_schema = __import__("lint13_schema")
    schema = lint13_schema.load_json(lint13_schema.SCHEMA_PATH)
    return lint13_schema, schema


def lint13_record_messages(lint13_schema, schema, path, record):
    return [violation.get("message") for violation in lint13_schema.validate_record(path, record, schema)]


def r15_two_key_eligible(record):
    identity = record.get("identity") or {}
    return (
        record.get("status") == "under_review"
        and identity.get("identity_method") == "citation+party-text"
        and identity.get("expected_citation_found") is True
        and identity.get("party_name_in_text") is True
    )


def r15_untouched_class(record):
    status = record.get("status")
    identity = record.get("identity") or {}
    if status == "under_review" and identity.get("identity_method") in ("name+docket", "pending"):
        return "under_review:%s" % identity.get("identity_method")
    if status in ("verified_identity", "fabrication_suspected", "not_found"):
        return status
    return None


def r15_status_counts(records):
    counts = Counter(record.get("status") for _path, record in records)
    return {
        str(status): count
        for status, count in sorted(counts.items(), key=lambda item: str(item[0]))
    }


def r15_format_id_list(record_ids):
    return "\n".join("  - %s" % record_id for record_id in sorted(record_ids))


def r15_assert_manifest_alignment(manifest, all_record_ids):
    manifest_ids = {row.get("record_id") for row in manifest.data.get("records") or [] if isinstance(row, dict)}
    missing = sorted(all_record_ids - manifest_ids)
    extra = sorted(manifest_ids - all_record_ids)
    if missing or extra:
        raise SystemExit(
            "r15 flip manifest/case record_id mismatch\n"
            "missing from manifest:\n%s\n"
            "extra in manifest:\n%s"
            % (r15_format_id_list(missing) if missing else "  - <none>",
               r15_format_id_list(extra) if extra else "  - <none>")
        )


def r15_assert_untouched_counts(protected_by_class, expected_counts):
    actual_counts = {name: len(record_ids) for name, record_ids in protected_by_class.items()}
    expected_keys = set(expected_counts)
    actual_keys = set(actual_counts)
    mismatched = []
    for key in sorted(expected_keys | actual_keys):
        if actual_counts.get(key, 0) != expected_counts.get(key, 0):
            mismatched.append("%s expected=%s actual=%s" % (key, expected_counts.get(key, 0), actual_counts.get(key, 0)))
    if mismatched:
        details = []
        for key in sorted(expected_keys | actual_keys):
            details.append("%s:\n%s" % (key, r15_format_id_list(protected_by_class.get(key, [])) or "  - <none>"))
        raise SystemExit(
            "r15 untouched-class count mismatch:\n%s\n\nrecord_id diff by class:\n%s"
            % ("\n".join(mismatched), "\n".join(details))
        )


def r15_raise_flip_mismatch(expected_ids, eligible_ids, expected_count, schema_rejected):
    missing = sorted(expected_ids - eligible_ids)
    extra = sorted(eligible_ids - expected_ids)
    lines = [
        "r15 flip count/set mismatch",
        "expected_count=%s actual_count=%s" % (expected_count, len(eligible_ids)),
        "missing expected record_id(s):",
        r15_format_id_list(missing) if missing else "  - <none>",
        "unexpected eligible record_id(s):",
        r15_format_id_list(extra) if extra else "  - <none>",
    ]
    if schema_rejected:
        lines.append("schema-rejected two-key record_id(s):")
        for record_id, messages in sorted(schema_rejected.items()):
            lines.append("  - %s: %s" % (record_id, "; ".join(messages[:3])))
    raise SystemExit("\n".join(lines))


def flip_verified_records(paths, manifest, journal, expected_count=R15_FLIP_EXPECTED_COUNT,
                          expected_untouched_counts=None):
    expected_untouched_counts = expected_untouched_counts or R15_UNTOUCHED_EXPECTED_COUNTS
    lint13_schema, schema = load_lint13_validator()
    case_records = []
    for path in case_json_paths(paths):
        case_records.append((path, read_json(path)))
    missing_id_paths = [path for path, record in case_records if not record.get("record_id")]
    if missing_id_paths:
        raise SystemExit(
            "r15 flip found record JSON missing record_id:\n%s"
            % r15_format_id_list(os.path.relpath(path, paths.repo_root) for path in missing_id_paths)
        )
    all_record_ids = {record.get("record_id") for _path, record in case_records if record.get("record_id")}
    r15_assert_manifest_alignment(manifest, all_record_ids)

    protected_by_class = {name: [] for name in expected_untouched_counts}
    protected_before = {}
    for path, record in case_records:
        record_id = record.get("record_id")
        protected_class = r15_untouched_class(record)
        if protected_class:
            protected_by_class.setdefault(protected_class, []).append(record_id)
            with open(path, encoding="utf-8") as f:
                protected_before[record_id] = f.read()
    r15_assert_untouched_counts(protected_by_class, expected_untouched_counts)
    protected_ids = set(protected_before)
    expected_ids = all_record_ids - protected_ids

    eligible = []
    schema_rejected = {}
    post_schema_rejected = {}
    for path, record in case_records:
        record_id = record.get("record_id")
        if not r15_two_key_eligible(record):
            continue
        pre_messages = lint13_record_messages(lint13_schema, schema, path, record)
        if pre_messages:
            schema_rejected[record_id] = pre_messages
            continue
        candidate = json.loads(json.dumps(record))
        candidate["status"] = "verified"
        if candidate.get("identity", {}).get("reason_code") == "awaiting_r15_structural_gates":
            candidate["identity"]["reason_code"] = None
        post_messages = lint13_record_messages(lint13_schema, schema, path, candidate)
        if post_messages:
            post_schema_rejected[record_id] = post_messages
            continue
        eligible.append((path, candidate))

    eligible_ids = {record["record_id"] for _path, record in eligible}
    if post_schema_rejected:
        schema_rejected.update(post_schema_rejected)
    if eligible_ids != expected_ids or len(eligible_ids) != expected_count or schema_rejected:
        r15_raise_flip_mismatch(expected_ids, eligible_ids, expected_count, schema_rejected)

    for path, record in eligible:
        record_id = record["record_id"]
        write_case_record(paths, record)
        journal.append(
            step="r15-flip",
            record_id=record_id,
            gates=list(R15_FLIP_GATES),
            adjudicated_by=READJUDICATION_ADJUDICATOR,
        )
        manifest.update(record_id, record, counts={}, final_record_id=record_id)

    untouched_changed = []
    for record_id, before in protected_before.items():
        path = os.path.join(paths.cases, record_id + ".json")
        with open(path, encoding="utf-8") as f:
            if f.read() != before:
                untouched_changed.append(record_id)
    if untouched_changed:
        raise SystemExit(
            "r15 untouched-class byte assertion failed:\n%s"
            % r15_format_id_list(untouched_changed)
        )

    manifest.regenerate_counts()
    manifest.save()
    case_records_after = [(path, read_json(path)) for path in case_json_paths(paths)]
    return {
        "flipped": sorted(eligible_ids),
        "protected_counts": {key: len(value) for key, value in sorted(protected_by_class.items())},
        "status_counts": r15_status_counts(case_records_after),
    }


def ensure_cluster_for_record(record_json, client, record_id, cluster=None, step="identity.cluster.reload"):
    if cluster:
        return cluster
    cluster_id = record_json["identity"].get("cluster_id")
    if cluster_id:
        return client.get_cluster(cluster_id, record_id=record_id, step=step)
    return None


def interruption_reason(client, session):
    if session is not None and session.expired():
        return "session_limit"
    budget = getattr(client, "budget", None)
    if budget is not None and budget.exhausted():
        return "call_budget_exhausted"
    return None


def interrupt_case_at_boundary(record_json, paths, journal, client, session, after_step):
    reason = interruption_reason(client, session)
    if not reason:
        return False
    budget = getattr(client, "budget", None)
    journal.append(
        record_id=record_json["record_id"],
        step="case-interruption",
        status="interrupted",
        reason=reason,
        after_step=after_step,
        budget=budget.snapshot() if budget is not None else None,
    )
    write_case_record(paths, record_json)
    record_json["_ingest_interrupted"] = reason
    return True


def persist_case_interruption(record_json, paths, journal, client, reason, during_step=None, error=None):
    budget = getattr(client, "budget", None)
    row = {
        "record_id": record_json["record_id"],
        "step": "case-interruption",
        "status": "interrupted",
        "reason": reason,
        "during_step": during_step,
        "budget": budget.snapshot() if budget is not None else None,
    }
    if isinstance(error, FetchFailed):
        row.update({
            "fetch_failed": True,
            "retry_pending": True,
            "failed_step": error.step,
            "attempts": error.attempts,
            "failure_reason": error.reason,
            "url_sha1": sha1_text(error.url),
            "http_status": error.status,
        })
    elif error is not None:
        row.update({
            "error_type": error.__class__.__name__,
            "error_message": str(error),
        })
    journal.append(**row)
    write_case_record(paths, record_json)
    record_json["_ingest_interrupted"] = reason
    return record_json


def completed_cl_silent_identity(record_json):
    if not record_json or record_json["identity"].get("cluster_id"):
        return False
    status = record_json.get("status")
    method = record_json["identity"].get("identity_method")
    return (status == "not_found" and method in ("not_found", "blocked")) or (status == "verified_off_cl" and method == "off_cl")


def process_page_record(source_record, client, paths, precedence, migration, journal, resume, build_run, session):
    source_record = normalize_source_record(source_record)
    record_id = page_record_id(source_record["record_id"])
    existing = load_case_record(paths, record_id)
    record_json = existing or empty_record_shell(record_id, source_record, build_run)
    changed = existing is None
    search_result = None
    cluster = None
    alternates = []
    lead_text = ""

    try:
        if existing and resume.step_complete(record_id, "identity") and completed_cl_silent_identity(record_json):
            extra = {"terminal_not_found": True} if record_json.get("status") == "not_found" else {"terminal_verified_off_cl": True}
            journal.append(record_id=record_id, step="identity", status="complete", skipped=True, loaded_existing=True, **extra)
            return record_json

        if resume.step_complete(record_id, "identity") and record_json["identity"].get("cluster_id"):
            journal.append(record_id=record_id, step="identity", status="complete", skipped=True, loaded_existing=True)
        else:
            search_result, cluster, alternates = resolve_identity(source_record, client, journal, resume, build_run)

        if cluster:
            lead_ref, lead_text = apply_identity(record_json, source_record, search_result, cluster, alternates, client, journal)
            changed = True

        if interrupt_case_at_boundary(record_json, paths, journal, client, session, "identity"):
            return record_json

        if not record_json["identity"].get("cluster_id") and not cluster:
            if resume.step_complete(record_id, "identity"):
                set_record_status(record_json, "blocked", "identity was complete but no existing record or journaled selection was available")
                record_json["identity"]["identity_method"] = "blocked"
                record_json["identity"]["reason_code"] = "identity_complete_without_record_or_selection"
                append_warning(record_json, "identity completion could not be replayed; blocked rather than marking not_found")
            else:
                set_record_status(record_json, "not_found")
                record_json["identity"]["identity_method"] = "not_found"
                record_json["identity"]["reason_code"] = "no_candidate_cluster"
                append_warning(record_json, "not found in CL identity search; not proof of fabrication")
                journal.append(record_id=record_id, step="identity", status="complete", final_status="not_found")
            if seed_treatment_from_migration(record_json, source_record, migration):
                changed = True
            changed = True
            record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("S2 treatment derivation proposed only")
            write_case_record(paths, record_json)
            return record_json

        citations_ready = resume.step_complete(record_id, "citations") and existing and record_json["citations"].get("all")
        need_cluster = (not citations_ready) or (record_json["progeny"].get("citation_count") is None)
        if need_cluster:
            cluster = ensure_cluster_for_record(record_json, client, record_id, cluster)
        if resume.step_complete(record_id, "citations") and existing and record_json["citations"].get("all"):
            journal.append(record_id=record_id, step="citations", status="complete", skipped=True, loaded_existing=True)
        elif cluster:
            apply_citations(record_json, cluster, precedence, journal)
            changed = True

        if interrupt_case_at_boundary(record_json, paths, journal, client, session, "citations"):
            return record_json

        if resume.step_complete(record_id, "pinpoints") and existing:
            journal.append(record_id=record_id, step="pinpoints", status="complete", skipped=True, loaded_existing=True)
        else:
            if not lead_text and record_json["identity"].get("lead_opinion_id"):
                lead_ref = client.opinion_ref(record_json["identity"]["lead_opinion_id"], "cluster.sub_opinions[]", {"replayed_from_record": True})
                lead_text = client.text_for_opinion(lead_ref, record_id=record_id, step="identity.lead_text.replay")
            apply_pinpoints(record_json, source_record, lead_text, journal)
            changed = True

        if interrupt_case_at_boundary(record_json, paths, journal, client, session, "pinpoints"):
            return record_json

        if cluster and record_json["progeny"].get("citation_count") != cluster.get("citation_count"):
            record_json["progeny"]["citation_count"] = cluster.get("citation_count")
            changed = True
        if not existing or record_json["treatment"].get("field_i_validity") == "unverified":
            if seed_treatment_from_migration(record_json, source_record, migration):
                changed = True
        if not interruption_reason(client, session):
            changed = fetch_progeny(record_json, source_record, client, journal, resume) or changed
        if interrupt_case_at_boundary(record_json, paths, journal, client, session, "progeny"):
            return record_json
        if not interruption_reason(client, session) and record_json["status"] in ("verified", "under_review"):
            changed = run_treatment(record_json, source_record, client, journal, resume, session) or changed
        if interrupt_case_at_boundary(record_json, paths, journal, client, session, "treatment"):
            return record_json
        if changed:
            record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("S2 treatment derivation proposed only")
            write_case_record(paths, record_json)
    except IngestInterrupted as exc:
        persist_case_interruption(record_json, paths, journal, client, exc.reason, during_step=exc.step, error=exc)
    except FetchFailed as exc:
        persist_case_interruption(record_json, paths, journal, client, "fetch_failed", during_step=exc.step, error=exc)
    except Exception as exc:
        persist_case_interruption(record_json, paths, journal, client, "unhandled_exception", error=exc)
    return record_json


def process_frontier_record(source_record, client, paths, precedence, journal, resume, build_run):
    source_record = normalize_source_record(source_record)
    unresolved_id = source_record["record_id"]
    shell = empty_record_shell(unresolved_id, source_record, build_run)
    if resume.step_complete(unresolved_id, "identity"):
        final_id = resume.final_record_id(unresolved_id, "identity") or unresolved_id
        existing = load_case_record(paths, final_id) or load_case_record(paths, unresolved_id)
        if existing:
            journal.append(record_id=unresolved_id, step="identity", status="complete", skipped=True, loaded_existing=True, final_record_id=existing["record_id"])
            return existing, existing["record_id"]
        shell["status"] = "blocked"
        shell["identity"]["identity_method"] = "blocked"
        shell["identity"]["reason_code"] = "frontier_identity_complete_without_record"
        append_warning(shell, "frontier identity completion could not be replayed; blocked rather than returning an empty shell")
        write_case_record(paths, shell)
        journal.append(record_id=unresolved_id, step="identity", status="complete", skipped=True, final_record_id=unresolved_id, final_status="blocked")
        return shell, unresolved_id
    result, cluster, alternates, search_rung = frontier_identity_selection(source_record, client, journal, unresolved_id)
    if not result or not cluster:
        final_id = not_found_stub_record_id(source_record)
        shell["record_id"] = final_id
        shell["stub"] = True
        shell["status"] = "not_found"
        shell["identity"]["identity_method"] = "not_found"
        shell["identity"]["reason_code"] = "frontier_no_candidate_cluster"
        append_warning(shell, "frontier not_found requires web/second-source cross-check before fabrication inference")
        write_case_record(paths, shell)
        journal.append(record_id=unresolved_id, step="identity", status="complete", final_record_id=final_id, final_status="not_found")
        return shell, final_id
    canonical = cluster.get("case_name") or result.get("caseName") or source_record.get("caption")
    input_caption = source_record.get("caption") or source_record.get("title") or unresolved_id
    final_id = cluster_stub_record_id(input_caption, cluster.get("id") or result.get("cluster_id"))
    canonical_match = canonical_caption_match_cluster(source_record.get("caption"), cluster, canonical)
    expected_cite = source_record.get("expected_citation") or source_record.get("citation") or ""
    expected_found = citation_matches_expected(cluster, expected_cite) if expected_cite else bool(cluster.get("citations"))
    strong_key_match = bool(expected_found or search_rung == "docket_number")
    shell["record_id"] = final_id
    shell["stub"] = True
    shell["status"] = "verified_identity" if (canonical_match or strong_key_match) else "fabrication_suspected"
    shell["identity"].update({
        "case_name": canonical,
        "case_name_short": cluster.get("case_name_short"),
        "case_name_full": cluster.get("case_name_full"),
        "cluster_id": extract_id(cluster.get("id") or result.get("cluster_id")),
        "absolute_url": cluster.get("absolute_url") or result.get("absolute_url"),
        "identity_method": "frontier-identity",
        "expected_citation_found": bool(expected_found),
        "party_name_in_text": False,
        "canonical_name_match": canonical_match,
        "alternates": [
            {
                "cluster_id": alt_cluster.get("id"),
                "score": score,
                "case_name": alt_cluster.get("case_name"),
            }
            for score, _alt_result, alt_cluster in alternates[:5]
        ],
        "reason_code": None if canonical_match else (
            "caption_mismatch_accepted_by_%s" % search_rung
            if strong_key_match else "canonical_name_mismatch"
        ),
    })
    if not canonical_match:
        append_warning(shell, "input caption does not match CL canonical caption")
        if strong_key_match:
            append_warning(shell, "frontier identity accepted by %s rung despite caption mismatch" % search_rung)
    shell["citations"] = classify_citations(cluster.get("citations") or [], source_record.get("court_level") or "state", precedence)
    shell["treatment"]["scope_note"] = "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
    shell["progeny"]["complete_query"] = None
    shell["provenance"]["field_provenance"]["identity"] = base_field_provenance("CourtListener frontier identity search")
    shell["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance("frontier stub, no treatment")
    shell["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("frontier stub, no treatment")
    shell["provenance"]["field_provenance"]["pinpoints"] = base_field_provenance("frontier stub, no pinpoints")
    write_case_record(paths, shell)
    remove_frontier_partial_record(paths, unresolved_id, final_id)
    journal.append(
        record_id=unresolved_id,
        step="identity",
        status="complete",
        final_record_id=final_id,
        final_status=shell["status"],
        selected_cluster_id=shell["identity"]["cluster_id"],
        search_rung=search_rung,
        canonical_match=canonical_match,
        expected_citation_found=bool(expected_found),
        strong_key_match=strong_key_match,
    )
    return shell, final_id


def run_ingest(args):
    repo_root = os.getcwd()
    pool_root = os.environ.get("CSSI_LAKE_ROOT", DEFAULT_CSSI_LAKE_ROOT)
    paths = LakePaths(repo_root, pool_root)
    if args.add_candidates:
        os.makedirs(os.path.join(paths.lake, "journal"), exist_ok=True)
    else:
        paths.ensure()
    manifest = ManifestStore(paths.manifest)
    had_build_id = bool(manifest.data.get("build_id"))
    run_id = manifest.ensure_build_id(args.run_id)
    if args.run_id or manifest.normalized or not had_build_id:
        manifest.save()
    journal_path = os.path.join(paths.journal, "s2-ingest-%s.jsonl" % run_id)
    journal = Journal(journal_path, run_id)
    if args.add_candidates:
        if (
            args.repair_migration_refs
            or args.repair_failclosed_treatment
            or args.flip_verified
            or args.elevate_off_cl
            or args.adjudication
            or args.readjudicate
            or args.readjudicate_file
            or args.rerun_lane
            or args.records
            or args.smoke
        ):
            raise SystemExit("--add-candidates cannot be combined with other action/filter options")
        journal, journal_fallback = writable_repair_journal(paths, journal)
        result = add_s6_candidates(manifest, journal, args.add_candidates)
        manifest.save()
        print("journal: %s%s" % (journal.path, " (repo-local fallback)" if journal_fallback else ""))
        print("s6 candidates appended: %s" % len(result["appended"]))
        print("s6 candidates skipped: %s" % len(result["skipped"]))
        print("total manifest records: %s" % manifest.data.get("counts", {}).get("total_manifest_records"))
        return
    if args.records and not args.rerun_lane:
        raise SystemExit("--records is only valid with --rerun-lane")
    if args.repair_migration_refs:
        if args.repair_failclosed_treatment or args.elevate_off_cl or args.readjudicate or args.readjudicate_file or args.rerun_lane or args.records or args.adjudication or args.smoke or args.flip_verified:
            raise SystemExit("--repair-migration-refs cannot be combined with other action/filter options")
        repaired = repair_migration_refs(paths, journal, read_json(paths.treatment_migration))
        manifest.save()
        print("journal: %s" % journal_path)
        print("migration refs repaired: %s" % len(repaired))
        return
    if args.repair_failclosed_treatment:
        if args.elevate_off_cl or args.readjudicate or args.readjudicate_file or args.rerun_lane or args.records or args.adjudication or args.smoke or args.flip_verified:
            raise SystemExit("--repair-failclosed-treatment cannot be combined with other action/filter options")
        journal, journal_fallback = writable_repair_journal(paths, journal)
        repaired = repair_failclosed_treatment(paths, journal)
        print("journal: %s%s" % (journal.path, " (repo-local fallback)" if journal_fallback else ""))
        print("fail-closed treatment repaired: %s" % len(repaired))
        return
    if args.flip_verified:
        if args.elevate_off_cl or args.readjudicate or args.readjudicate_file or args.rerun_lane or args.records or args.adjudication or args.smoke:
            raise SystemExit("--flip-verified cannot be combined with other action/filter options")
        journal, journal_fallback = writable_repair_journal(paths, journal)
        result = flip_verified_records(paths, manifest, journal)
        print("journal: %s%s" % (journal.path, " (repo-local fallback)" if journal_fallback else ""))
        print("verified flips: %s" % len(result["flipped"]))
        print("expected flips: %s" % R15_FLIP_EXPECTED_COUNT)
        print("untouched classes: %s" % json.dumps(result["protected_counts"], sort_keys=True))
        print("status counts: %s" % json.dumps(result["status_counts"], sort_keys=True))
        return
    if args.elevate_off_cl:
        if args.readjudicate or args.readjudicate_file or args.rerun_lane:
            raise SystemExit("--elevate-off-cl cannot be combined with --readjudicate or --rerun-lane")
        apply_off_cl_elevation(paths, manifest, journal, args.elevate_off_cl, args.adjudication, run_id)
        manifest.save()
        print("journal: %s" % journal_path)
        print("off-CL elevation complete: %s" % args.elevate_off_cl)
        return
    if args.adjudication:
        raise SystemExit("--adjudication is only valid with --elevate-off-cl")
    rerun_lanes = validate_rerun_lanes(args.rerun_lane)
    if rerun_lanes and (args.readjudicate or args.readjudicate_file):
        raise SystemExit("--rerun-lane cannot be combined with --readjudicate")
    readjudicate_ids = readjudication_identifiers(args)
    if readjudicate_ids:
        apply_readjudications(paths, manifest, journal, readjudicate_ids, run_id)
        manifest.save()
    token = read_token(args.token_path)
    fingerprint = sha256_text(token)[:12]
    if args.resume:
        resume_rows = journal.rows()
        if not args.run_id:
            resume_rows = manifest.resume_rows() + resume_rows
        resume = ResumeState(resume_rows)
    else:
        resume = ResumeState([])
    max_calls = 80 if args.smoke else args.max_calls
    budget = CallBudget(max_calls=max_calls)
    client = CourtListenerClient(
        paths=paths,
        token=token,
        token_fingerprint=fingerprint,
        journal=journal,
        budget=budget,
        rate=TokenBucket(rate_per_minute=args.rate_per_minute, capacity=1),
        hourly=HourlyGuard(max_per_hour=args.hourly_limit),
        run_id=run_id,
    )
    if rerun_lanes:
        rerun_record_filters = list(args.records or [])
        if args.smoke:
            rerun_record_filters.append(args.smoke)
        target_rows = reset_record_lanes_for_rerun(paths, manifest, journal, rerun_lanes, identifiers=rerun_record_filters)
        manifest.save()
        session = SessionTimer(args.session_minutes)
        journal.append(
            step="budget-checkpoint",
            status="start",
            mode="rerun-lane",
            lanes=rerun_lanes,
            budget=budget.snapshot(estimated_remaining="lane-scoped rerun only; identity/citations/progeny untouched"),
        )
        for source_record in target_rows:
            if session.expired():
                journal.append(step="case-interruption", status="interrupted", reason="session_limit", budget=budget.snapshot())
                break
            if budget.exhausted():
                journal.append(step="case-interruption", status="interrupted", reason="call_budget_exhausted", budget=budget.snapshot())
                break
            record_id = source_record["record_id"]
            record_call_start = budget.session_calls
            record_json = load_case_record(paths, record_id)
            try:
                base_rows = manifest.resume_rows() + journal.rows() if args.resume else journal.rows()
                resume = lane_scoped_resume(base_rows, record_id, rerun_lanes)
                if run_treatment(record_json, source_record, client, journal, resume, session):
                    write_case_record(paths, record_json)
            except IngestInterrupted as exc:
                persist_case_interruption(record_json, paths, journal, client, exc.reason, during_step=exc.step, error=exc)
            except FetchFailed as exc:
                persist_case_interruption(record_json, paths, journal, client, "fetch_failed", during_step=exc.step, error=exc)
            except Exception as exc:
                persist_case_interruption(record_json, paths, journal, client, "unhandled_exception", error=exc)
            interrupted = record_json.pop("_ingest_interrupted", None)
            current_resume = ResumeState(manifest.resume_rows() + journal.rows()) if args.resume else ResumeState(journal.rows())
            manifest.update(record_id, record_json, counts={"cl_calls": budget.session_calls - record_call_start}, final_record_id=record_id, resume_state=current_resume)
            manifest.save()
            journal.append(
                record_id=record_id,
                step="case-checkpoint",
                status="interrupted" if interrupted else "complete",
                reason=interrupted,
                mode="rerun-lane",
                lanes=rerun_lanes,
                budget=budget.snapshot(),
            )
            if interrupted:
                break
        journal.append(step="budget-checkpoint", status="end", mode="rerun-lane", lanes=rerun_lanes, budget=budget.snapshot())
        print("journal: %s" % journal_path)
        print("calls this session: %s" % budget.session_calls)
        return
    precedence = read_json(paths.precedence)
    migration = read_json(paths.treatment_migration)
    session = SessionTimer(args.session_minutes)
    records = manifest.select(args.smoke)
    journal.append(step="budget-checkpoint", status="start", budget=budget.snapshot(estimated_remaining="30-70 calls/case with snippet-first treatment triage"))
    for source_record in records:
        if session.expired():
            journal.append(step="case-interruption", status="interrupted", reason="session_limit", budget=budget.snapshot())
            break
        if budget.exhausted():
            journal.append(step="case-interruption", status="interrupted", reason="call_budget_exhausted", budget=budget.snapshot())
            break
        old_id = source_record["record_id"]
        record_call_start = budget.session_calls
        try:
            if source_record.get("stub"):
                record_json, final_id = process_frontier_record(source_record, client, paths, precedence, journal, resume, run_id)
            else:
                record_json = process_page_record(source_record, client, paths, precedence, migration, journal, resume, run_id, session)
                final_id = record_json["record_id"]
        except IngestInterrupted as exc:
            record_json = load_case_record(paths, old_id) or empty_record_shell(old_id, source_record, run_id)
            persist_case_interruption(record_json, paths, journal, client, exc.reason, during_step=exc.step, error=exc)
            final_id = record_json["record_id"]
        except FetchFailed as exc:
            record_json = load_case_record(paths, old_id) or empty_record_shell(old_id, source_record, run_id)
            persist_case_interruption(record_json, paths, journal, client, "fetch_failed", during_step=exc.step, error=exc)
            final_id = record_json["record_id"]
        except Exception as exc:
            record_json = load_case_record(paths, old_id) or empty_record_shell(old_id, source_record, run_id)
            persist_case_interruption(record_json, paths, journal, client, "unhandled_exception", error=exc)
            final_id = record_json["record_id"]
        interrupted = record_json.pop("_ingest_interrupted", None)
        current_resume = ResumeState(manifest.resume_rows() + journal.rows()) if args.resume and not args.run_id else ResumeState(journal.rows())
        manifest.update(old_id, record_json, counts={"cl_calls": budget.session_calls - record_call_start}, final_record_id=final_id, resume_state=current_resume)
        manifest.save()
        journal.append(
            record_id=final_id,
            step="case-checkpoint",
            status="interrupted" if interrupted else "complete",
            reason=interrupted,
            budget=budget.snapshot(),
        )
        if interrupted:
            break
    journal.append(step="budget-checkpoint", status="end", budget=budget.snapshot(estimated_remaining="review checkpoint required before relaunch; expect 30-70 calls/case"))
    print("journal: %s" % journal_path)
    print("calls this session: %s" % budget.session_calls)


def self_test_record_ids():
    assert page_record_id("Terry v. Ohio") == "Terry v. Ohio"
    try:
        page_record_id("bad--page")
    except ValueError:
        pass
    else:
        raise AssertionError("page record id accepted reserved namespace")
    assert cluster_stub_record_id("Nieves v. Bartlett", 4384503) == "nieves-v-bartlett--4384503"
    row = {
        "caption": "United States v. Smith",
        "court_era": "5th Cir. 2024",
        "year": 2024,
        "docket": "23-1000",
        "source_row_index": 77,
    }
    got = not_found_stub_record_id(row)
    assert re.match(r"^united-states-v-smith--u[0-9a-f]{8}$", got), got
    row2 = dict(row)
    row2["court_era"] = "9th Cir. 2024"
    assert not_found_stub_record_id(row) != not_found_stub_record_id(row2)
    long_caption = "Long " + ("Caption " * 60) + "v. Other"
    long_cluster_id = 10601315
    bounded = cluster_stub_record_id(long_caption, long_cluster_id)
    slug_part, suffix = bounded.rsplit("--", 1)
    assert len(slug_part) <= MAX_RECORD_SLUG_CHARS
    assert suffix == str(long_cluster_id)
    assert len((bounded + ".json").encode("utf-8")) <= 120
    long_row = dict(row, caption=long_caption)
    not_found = not_found_stub_record_id(long_row)
    slug_part, suffix = not_found.rsplit("--", 1)
    assert len(slug_part) <= MAX_RECORD_SLUG_CHARS
    assert re.match(r"^u[0-9a-f]{8}$", suffix), suffix


def self_test_precedence():
    precedence = {
        "court_classes": {
            "scotus": {"reporters": {"U.S.": 1, "S. Ct.": 2, "L. Ed. 2d": 3}},
            "coa": {"reporters": {"F.3d": 1, "F.4th": 1}},
            "district": {"reporters": {"F. Supp. 3d": 1}},
            "state": {
                "reporter_classes": {"official": 1, "regional": 2, "other": 3},
                "regional_reporters": {"P.3d": 2},
            },
        }
    }
    terry = [
        {"volume": 392, "reporter": "U.S.", "page": 1, "type": 1},
        {"volume": 88, "reporter": "S. Ct.", "page": 1868, "type": 1},
    ]
    selected, reason = select_official_cite(terry, "scotus", precedence)
    assert citation_reporter(selected) == "U.S.", reason
    tie = [
        {"volume": 1, "reporter": "F.3d", "page": 1, "type": 1},
        {"volume": 2, "reporter": "F.4th", "page": 2, "type": 1},
    ]
    selected, reason = select_official_cite(tie, "coa", precedence)
    assert selected is None and reason == "same_rank_tie"
    unlisted = [{"volume": 1, "reporter": "Unknown", "page": 1, "type": 1}]
    selected, reason = select_official_cite(unlisted, "scotus", precedence)
    assert selected is None and reason.startswith("unlisted_reporter")


def self_test_binding_filters():
    assert binding_jurisdiction_filter({"court_level": "scotus"}) == ""
    assert binding_jurisdiction_filter({"court_level": "circuit", "circuit": "4th Cir."}) == "AND court_id:(scotus OR ca4)"
    assert binding_jurisdiction_filter({"court_level": "coa", "circuit": "4th Cir."}) == "AND court_id:(scotus OR ca4)"
    assert binding_jurisdiction_filter({"court_level": "district", "circuit": "9"}) == "AND court_id:(scotus OR ca9)"
    state = binding_jurisdiction_filter({"court_level": "state-high", "state": "California"})
    assert state == "AND court_id:(scotus OR cal OR calctapp OR calappdeptsuper)", state
    assert normalize_court_class("state-app") == "state"
    assert normalize_court_class("state-high") == "state"
    assert normalize_court_class("circuit") == "coa"
    assert normalize_court_class("coa") == "coa"
    params = identity_search_params({"court_level": "circuit", "circuit": "4th Cir.", "title": "Case v. Name"})
    assert params["court"] == "ca4"


def self_test_token_bucket():
    bucket = TokenBucket(rate_per_minute=14, capacity=1, start_time=0)
    now = 0.0
    calls = []
    for _ in range(30):
        wait = bucket.consume_at(now)
        now += wait
        calls.append(now)
    for i, start in enumerate(calls):
        in_window = [call for call in calls[i:] if call - start < 60.0]
        assert len(in_window) <= 14, (start, in_window)
    analyze = TokenBucket(rate_per_minute=60, capacity=1, start_time=0)
    now = 0.0
    calls = []
    for _ in range(130):
        wait = analyze.consume_at(now)
        now += wait
        calls.append(now)
    for i, start in enumerate(calls):
        assert len([call for call in calls[i:] if call - start < 60.0]) <= 60


def self_test_collective_global_limiter():
    global_bucket = TokenBucket(rate_per_minute=14, capacity=1, start_time=0)
    analyze_bucket = TokenBucket(rate_per_minute=60, capacity=1, start_time=0)
    now = 0.0
    starts = []
    completions = []
    durations = [0.0, 5.5, 0.1, 1.7, 0.0, 6.2, 0.2]
    for i in range(35):
        extra = analyze_bucket if i % 4 == 0 else None
        wait = global_bucket.consume_at(now)
        now += wait
        if extra is not None:
            wait = extra.consume_at(now)
            now += wait
        start = now
        complete = start + durations[i % len(durations)]
        global_bucket.mark_completed_at(complete)
        if extra is not None:
            extra.mark_completed_at(complete)
        starts.append(start)
        completions.append(complete)
        now = complete
    for series in (starts, completions):
        for i, start in enumerate(series):
            in_window = [call for call in series[i:] if call - start < 60.0]
            assert len(in_window) <= 14, (start, in_window)
    min_completion_gap = min(b - a for a, b in zip(completions, completions[1:]))
    assert min_completion_gap + 0.000001 >= global_bucket.interval, min_completion_gap


def self_test_journal_resume():
    path = "/tmp/s2-journal-self-test.jsonl"
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
    journal = Journal(path, "selftest")
    journal.append(record_id="Terry v. Ohio", step="treatment", lane="lane1_negative", status="complete")
    journal.append(record_id="Terry v. Ohio", step="identity", status="complete")
    state = ResumeState(journal.rows())
    assert state.step_complete("Terry v. Ohio", "identity")
    assert state.lane_complete("Terry v. Ohio", "treatment", "lane1_negative")
    assert not state.lane_complete("Terry v. Ohio", "treatment", "lane2_top_cited")


class SelfTestClient:
    def __init__(self, paths, journal):
        self.paths = paths
        self.journal = journal
        self.search_calls = []
        self.url_calls = []

    def opinion_ref(self, opinion_id, source_array, context=None):
        return {"opinion_id": int(opinion_id), "source_array": source_array, "context": context or {}}

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if params.get("case_name"):
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 100,
                    "caseName": "Smith v. Jones",
                    "opinions": [{"id": 200, "type": "020lead"}],
                    "sibling_ids": [200],
                }],
            }
        return {"count": 0, "results": [], "next": None}

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        return {
            "id": int(cluster_id),
            "case_name": "Smith v. Jones",
            "case_name_short": "Smith",
            "case_name_full": "Smith v. Jones",
            "date_filed": "2024-01-01",
            "court": "scotus",
            "citation_count": 3,
            "absolute_url": "/opinion/100/smith-v-jones/",
            "citations": [{"volume": 1, "reporter": "U.S.", "page": 2, "type": 1}],
            "sub_opinions": [{"id": 200, "type": "020lead"}],
        }

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        return "Smith and Jones are both named in this opinion."

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        self.url_calls.append({"url": url, "step": step})
        return {"count": 0, "results": [], "next": None}


class IdentityApplyClient:
    def __init__(self, text):
        self.text = text

    def opinion_ref(self, opinion_id, source_array, context=None):
        return {"opinion_id": int(opinion_id), "source_array": source_array, "context": context or {}}

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        return self.text


class BirchfieldFallbackClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if params.get("case_name"):
            return {"count": 0, "results": [], "next": None}
        if params.get("q"):
            return {
                "count": 10,
                "results": [
                    {
                        "cluster_id": 9000 + i,
                        "caseName": "Unrelated v. Result %s" % i,
                        "opinions": [{"id": 8000 + i, "type": "020lead"}],
                    }
                    for i in range(10)
                ],
                "next": None,
            }
        if params.get("citation") == "579 U.S. 438":
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 3216497,
                    "caseName": "Birchfield v. N. Dakota. William Robert Bernard",
                    "opinions": [{"id": 4321, "type": "020lead"}],
                    "sibling_ids": [4321],
                }],
                "next": None,
            }
        raise AssertionError("unexpected fallback params %r" % params)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        self.cluster_calls.append({"cluster_id": int(cluster_id), "step": step})
        if 9000 <= int(cluster_id) < 9010:
            return {
                "id": int(cluster_id),
                "case_name": "Unrelated v. Result",
                "case_name_short": "Unrelated",
                "case_name_full": "Unrelated v. Result",
                "date_filed": "1999-01-01",
                "court": "ca9",
                "citations": [{"volume": 999, "reporter": "F.3d", "page": int(cluster_id), "type": 1}],
                "sub_opinions": [{"id": int(cluster_id) + 100, "type": "020lead"}],
            }
        return {
            "id": int(cluster_id),
            "case_name": "Birchfield v. N. Dakota. William Robert Bernard",
            "case_name_short": "Birchfield",
            "case_name_full": "Birchfield v. N. Dakota. William Robert Bernard",
            "date_filed": "2016-06-23",
            "court": "scotus",
            "citations": [{"volume": 579, "reporter": "U.S.", "page": 438, "type": 1}],
            "sub_opinions": [{"id": 4321, "type": "020lead"}],
        }


class LewisDisambiguatorFallbackClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if params.get("case_name"):
            return {"count": 0, "results": [], "next": None}
        if params.get("q"):
            return {
                "count": 3,
                "results": [
                    {
                        "cluster_id": cluster_id,
                        "caseName": case_name,
                        "dateFiled": "1966-12-05",
                        "court": "scotus",
                        "opinions": [{"id": 7000 + i, "type": "020lead"}],
                    }
                    for i, (cluster_id, case_name) in enumerate([
                        (107303, "United States v. Demko"),
                        (107304, "Wrong v. United States"),
                        (107305, "Lewis v. Wrong"),
                    ])
                ],
                "next": None,
            }
        if params.get("citation") == "385 U.S. 206":
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 385206,
                    "caseName": "Lewis v. United States",
                    "dateFiled": "1966-12-05",
                    "court": "scotus",
                    "opinions": [{"id": 7206, "type": "020lead"}],
                    "sibling_ids": [7206],
                }],
                "next": None,
            }
        raise AssertionError("unexpected Lewis fallback params %r" % params)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        cluster_id = int(cluster_id)
        self.cluster_calls.append({"cluster_id": cluster_id, "step": step})
        wrong_pages = {
            107303: ("United States v. Demko", 149),
            107304: ("Wrong v. United States", 150),
            107305: ("Lewis v. Wrong", 151),
        }
        if cluster_id in wrong_pages:
            case_name, page = wrong_pages[cluster_id]
            return {
                "id": cluster_id,
                "case_name": case_name,
                "case_name_short": case_name,
                "case_name_full": case_name,
                "date_filed": "1966-12-05",
                "court": "scotus",
                "citations": [{"volume": 385, "reporter": "U.S.", "page": page, "type": 1}],
                "sub_opinions": [{"id": cluster_id + 1000, "type": "020lead"}],
            }
        return {
            "id": cluster_id,
            "case_name": "Lewis v. United States",
            "case_name_short": "Lewis",
            "case_name_full": "Lewis v. United States",
            "date_filed": "1966-12-05",
            "court": "scotus",
            "citations": [{"volume": 385, "reporter": "U.S.", "page": 206, "type": 1}],
            "sub_opinions": [{"id": 7206, "type": "020lead"}],
        }


class PetersCitationPrefilterClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if params.get("case_name"):
            return {"count": 0, "results": [], "next": None}
        if params.get("q"):
            return {"count": 0, "results": [], "next": None}
        if params.get("citation") == "392 U.S. 40":
            rows = [
                ("107700", "Crossmatch v. One", ["40 S. Ct. 392"]),
                ("107701", "Crossmatch v. Two", ["392 F.2d 40"]),
                ("107702", "Crossmatch v. Three", ["55 Empl. Prac. Dec. (CCH) 40,392"]),
                ("107703", "Crossmatch v. Four", ["40 Misc. 392"]),
                ("107730", "Sibron v. New York", ["392 U.S. 40", "88 S. Ct. 1889"]),
                ("107705", "Crossmatch v. Six", ["392 U.S. 41"]),
                ("107706", "Crossmatch v. Seven", ["40 N.Y.2d 392"]),
                ("107707", "Crossmatch v. Eight", ["392 A.2d 40"]),
                ("107708", "Crossmatch v. Nine", ["40 Cal. App. 392"]),
                ("107709", "Crossmatch v. Ten", ["392 P.2d 40"]),
                ("107710", "Crossmatch v. Eleven", ["40 F. Supp. 392"]),
                ("107711", "Crossmatch v. Twelve", ["392 So. 2d 40"]),
                ("107712", "Crossmatch v. Thirteen", ["40 U.S. 392"]),
                ("107713", "Crossmatch v. Fourteen", ["392 N.E.2d 40"]),
            ]
            return {
                "count": 14,
                "results": [
                    {
                        "cluster_id": int(cluster_id),
                        "caseName": case_name,
                        "dateFiled": "1968-06-10",
                        "court": "scotus",
                        "court_id": "scotus",
                        "citation": citations,
                        "opinions": [{"id": int(cluster_id) + 1, "type": "020lead"}],
                        "sibling_ids": [int(cluster_id) + 1],
                    }
                    for cluster_id, case_name, citations in rows
                ],
                "next": None,
            }
        raise AssertionError("unexpected Peters fallback params %r" % params)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        cluster_id = int(cluster_id)
        self.cluster_calls.append({"cluster_id": cluster_id, "step": step})
        if cluster_id == 107730:
            return {
                "id": 107730,
                "case_name": "Sibron v. New York",
                "case_name_short": "Sibron",
                "case_name_full": "Sibron v. New York",
                "date_filed": "1968-06-10",
                "court": "scotus",
                "citations": [{"volume": 392, "reporter": "U.S.", "page": 40, "type": 1}],
                "sub_opinions": [{"id": 107731, "type": "020lead"}],
            }
        return {
            "id": cluster_id,
            "case_name": "Crossmatch v. Result",
            "case_name_short": "Crossmatch",
            "case_name_full": "Crossmatch v. Result",
            "date_filed": "1968-06-10",
            "court": "scotus",
            "citations": [{"volume": 999, "reporter": "U.S.", "page": cluster_id, "type": 1}],
            "sub_opinions": [{"id": cluster_id + 1, "type": "020lead"}],
        }


class NoCiteFallbackClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if params.get("case_name"):
            return {"count": 0, "results": [], "next": None}
        if params.get("q"):
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 202601,
                    "caseName": "Recent v. Case",
                    "dateFiled": "2026-01-15",
                    "court": "scotus",
                    "opinions": [{"id": 2601, "type": "020lead"}],
                    "sibling_ids": [2601],
                }],
                "next": None,
            }
        raise AssertionError("unexpected no-cite fallback params %r" % params)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        cluster_id = int(cluster_id)
        self.cluster_calls.append({"cluster_id": cluster_id, "step": step})
        return {
            "id": cluster_id,
            "case_name": "Recent v. Case",
            "case_name_short": "Recent",
            "case_name_full": "Recent v. Case",
            "date_filed": "2026-01-15",
            "court": "scotus",
            "citations": [],
            "sub_opinions": [{"id": 2601, "type": "020lead"}],
        }


class DocketContinuationFrontierClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step, "record_id": record_id})
        if params.get("case_name"):
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 88100,
                    "caseName": "United States v. $23,407.69 in U.S. Currency",
                    "dateFiled": "1983-05-23",
                    "court": "scotus",
                    "court_id": "scotus",
                    "opinions": [{"id": 88101, "type": "020lead"}],
                }],
                "next": None,
            }
        if params.get("q"):
            return {"count": 0, "results": [], "next": None}
        if params.get("docket_number") == "81-1062":
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 88500,
                    "caseName": "United States v. Eight Thousand Eight Hundred Fifty Dollars in U.S. Currency",
                    "dateFiled": "1983-05-23",
                    "court": "scotus",
                    "court_id": "scotus",
                    "opinions": [{"id": 88501, "type": "020lead"}],
                }],
                "next": None,
            }
        raise AssertionError("unexpected docket-continuation params %r" % params)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        cluster_id = int(cluster_id)
        self.cluster_calls.append({"cluster_id": cluster_id, "step": step, "record_id": record_id})
        if cluster_id == 88100:
            return {
                "id": cluster_id,
                "case_name": "United States v. $23,407.69 in U.S. Currency",
                "case_name_short": "United States v. $23,407.69",
                "case_name_full": "United States v. $23,407.69 in U.S. Currency",
                "date_filed": "1983-05-23",
                "court": "scotus",
                "absolute_url": "/opinion/88100/united-states-v-2340769-in-us-currency/",
                "citations": [{"volume": 715, "reporter": "F.2d", "page": 162, "type": 1}],
                "sub_opinions": [{"id": 88101, "type": "020lead"}],
            }
        return {
            "id": cluster_id,
            "case_name": "United States v. Eight Thousand Eight Hundred Fifty Dollars in U.S. Currency",
            "case_name_short": "United States v. Eight Thousand Eight Hundred Fifty Dollars",
            "case_name_full": "United States v. Eight Thousand Eight Hundred Fifty Dollars in U.S. Currency",
            "date_filed": "1983-05-23",
            "court": "scotus",
            "absolute_url": "/opinion/88500/united-states-v-eight-thousand-eight-hundred-fifty-dollars/",
            "citations": [{"volume": 461, "reporter": "U.S.", "page": 555, "type": 1}],
            "sub_opinions": [{"id": 88501, "type": "020lead"}],
        }


class ExhaustedFallbackClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        return {"count": 0, "results": [], "next": None}

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        self.cluster_calls.append({"cluster_id": int(cluster_id), "step": step})
        raise AssertionError("exhausted fallback fixture must not fetch clusters")


class NoSearchClient:
    def search(self, params, cache=True, record_id=None, step=None):
        raise AssertionError("terminal not_found resume skip must not search")

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        raise AssertionError("terminal not_found resume skip must not fetch cluster")


class FrontierLongCaptionClient:
    def __init__(self, canonical_caption):
        self.canonical_caption = canonical_caption
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step, "record_id": record_id})
        return {
            "count": 1,
            "results": [{
                "cluster_id": 10601315,
                "caseName": self.canonical_caption,
                "absolute_url": "/opinion/10601315/sarah-sanders-v-arkansas-board-of-corrections/",
            }],
            "next": None,
        }

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        self.cluster_calls.append({"cluster_id": int(cluster_id), "step": step, "record_id": record_id})
        return {
            "id": int(cluster_id),
            "case_name": self.canonical_caption,
            "case_name_short": "Sanders",
            "case_name_full": self.canonical_caption,
            "date_filed": "2024-01-01",
            "court": "ark",
            "absolute_url": "/opinion/10601315/sarah-sanders-v-arkansas-board-of-corrections/",
            "citations": [{"cite": "2024 Ark. 1", "type": 6}],
            "sub_opinions": [],
        }


class FrontierCitationFallbackClient:
    def __init__(self):
        self.search_calls = []
        self.cluster_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step, "record_id": record_id})
        if params.get("citation") == "123 U.S. 456":
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 123456,
                    "caseName": "Citation Fallback v. Case",
                    "absolute_url": "/opinion/123456/citation-fallback-v-case/",
                }],
                "next": None,
            }
        return {"count": 0, "results": [], "next": None}

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        self.cluster_calls.append({"cluster_id": int(cluster_id), "step": step, "record_id": record_id})
        return {
            "id": int(cluster_id),
            "case_name": "Citation Fallback v. Case",
            "case_name_short": "Citation Fallback",
            "case_name_full": "Citation Fallback v. Case",
            "date_filed": "2026-01-01",
            "court": "scotus",
            "absolute_url": "/opinion/123456/citation-fallback-v-case/",
            "citations": [{"volume": 123, "reporter": "U.S.", "page": 456, "type": 1}],
            "sub_opinions": [],
        }


def identity_fixture_search_result(cluster_id=100, opinion_id=200):
    return {
        "cluster_id": cluster_id,
        "caseName": "fixture",
        "opinions": [{"id": opinion_id, "type": "020lead"}],
        "sibling_ids": [opinion_id],
    }


def self_test_identity_primary_prefilter_plan():
    matched_results = [
        {"cluster_id": 7100 + i, "citation": ["500 U.S. 1"], "caseName": "Match %s" % i}
        for i in range(11)
    ]
    planned, info = identity_candidate_result_plan(
        matched_results,
        "500 U.S. 1 (1991)",
        IDENTITY_PRIMARY_CLUSTER_LIMIT,
        prefilter_max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
    )
    assert planned == matched_results[:IDENTITY_FALLBACK_CLUSTER_LIMIT]
    assert info == {
        "citation_prefilter_matched_rows": 11,
        "citation_prefilter_fetched_cluster_ids": [7100, 7101, 7102],
    }

    no_match_results = [
        {"cluster_id": 7200 + i, "citation": ["501 U.S. %s" % i], "caseName": "No Match %s" % i}
        for i in range(11)
    ]
    planned, info = identity_candidate_result_plan(
        no_match_results,
        "500 U.S. 1",
        IDENTITY_PRIMARY_CLUSTER_LIMIT,
        prefilter_max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
    )
    assert planned == no_match_results[:IDENTITY_PRIMARY_CLUSTER_LIMIT]
    assert info == {
        "citation_prefilter_matched_rows": 0,
        "citation_prefilter_fetched_cluster_ids": [],
    }

    planned, info = identity_candidate_result_plan(
        no_match_results,
        "",
        IDENTITY_PRIMARY_CLUSTER_LIMIT,
        prefilter_max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
    )
    assert planned == no_match_results[:IDENTITY_PRIMARY_CLUSTER_LIMIT]
    assert info == {
        "citation_prefilter_matched_rows": 0,
        "citation_prefilter_fetched_cluster_ids": [],
    }


def self_test_identity_caption_and_cite_fixtures():
    assert normalize_cite("283 F.3d 1040 (9th Cir. 2002)") == "283 F.3d 1040"
    assert normalize_cite("389 U.S. 35 (1967)") == "389 U.S. 35"
    assert normalize_cite("1 U.S. 2") == "1 U.S. 2"
    assert normalize_cite("foo (internal) 1 U.S. 2") == "foo (internal) 1 U.S. 2"
    assert citation_compare_key("2026 PA Super 114") == citation_compare_key("2026 Pa. Super. 114")
    assert citation_compare_key("283 F.3d 1040") == citation_compare_key("283 F. 3d 1040")
    assert citation_compare_key("403 U.S. 388") == citation_compare_key("403 US 388")
    assert citation_compare_key("403 U.S. 388") != citation_compare_key("403 U.S. 389")

    assert canonical_caption_match("Commonwealth v. Herlth", "Com. v. Herlth, J.")
    assert canonical_caption_match(
        "Birchfield v. North Dakota",
        "Birchfield v. N. Dakota. William Robert Bernard",
    )
    assert canonical_caption_match("Board of Education v. Earls", "Board of Ed. v. Earls")
    assert canonical_caption_match(
        "Bivens v. Six Unknown Named Agents",
        "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
    )
    assert canonical_caption_match(
        "Board of Education v. Earls",
        "Board of Education of Independent School District No. 92 of Pottawatomie County v. Earls",
    )
    assert canonical_caption_match(
        "Brower v. County of Inyo",
        "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
    )
    assert canonical_caption_match(
        "Skinner v. Railway Labor Executives' Ass'n",
        "Skinner v. Railway Labor Executives' Assn.",
    )
    assert caption_token_set("Federal Bureau of Investigation") == {"fbi"}
    assert "fbn" not in caption_token_set("Federal Bureau of Narcotics")
    assert canonical_caption_match(
        "FBI v. Fazaga",
        "Federal Bureau of Investigation v. Fazaga",
    )
    assert not canonical_caption_match("FBN v. Bivens", "Federal Bureau of Narcotics v. Bivens")
    assert first_party_terms("Federal Bureau of Investigation v. Fazaga") == ["fbi", "fazaga"]
    assert "fbi" in party_term_candidates("Federal Bureau of Investigation")
    assert text_names_parties(
        "Federal Bureau of Investigation v. Fazaga",
        "The FBI invoked the state secrets privilege against Fazaga.",
    )
    assert party_term_candidates("ass'n") == {"ass'n", "assn", "association"}
    assert party_term_candidates("association") == {"association", "assn"}
    assert party_term_candidates("skinner") == {"skinner"}
    association_text = "Skinner challenged the testing program adopted by the Association."
    assert "ass'n" not in association_text.lower()
    assert text_names_parties("Skinner v. Railway Labor Executives' Ass'n", association_text)
    assert text_names_parties("Skinner v. Railway Labor Executives Association", "Skinner challenged the Ass'n policy.")
    assert text_names_parties("Skinner v. Railway Labor Executives Association", "Skinner challenged the Ass\u2019n policy.")
    assert text_names_parties("Skinner v. Railway Labor Executives Ass'n", "Skinner challenged the Association policy.")
    assert not text_names_parties("Acme v. Company", "Acme asked the court to resolve a common issue.")
    assert not text_names_parties("Smith v. North", "Smith argued nothing about the other side.")
    assert not canonical_caption_match("Adams v. Williams", "Williams v. Adams")
    assert not canonical_caption_match("County of Inyo", "Company of Inyo")

    journal = Journal("/tmp/s2-identity-caption-self-test.jsonl", "selftest")
    try:
        os.unlink(journal.path)
    except FileNotFoundError:
        pass

    shortened_source = {
        "record_id": "bivens-short",
        "title": "Bivens v. Six Unknown Named Agents",
        "expected_citation": "403 U.S. 388 (1971)",
        "court_level": "scotus",
    }
    shortened_record = empty_record_shell("bivens-short", shortened_source, "selftest")
    shortened_cluster = {
        "id": 108375,
        "case_name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
        "case_name_short": "Bivens",
        "case_name_full": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
        "date_filed": "1971-06-21",
        "court": "scotus",
        "citations": [{"volume": 403, "reporter": "U.S.", "page": 388, "type": 1}],
        "sub_opinions": [{"id": 200, "type": "020lead"}],
    }
    apply_identity(
        shortened_record,
        shortened_source,
        identity_fixture_search_result(108375, 200),
        shortened_cluster,
        [],
        IdentityApplyClient("Bivens sued the Six Unknown Named Agents in this opinion."),
        journal,
    )
    assert shortened_record["status"] == "under_review"
    assert shortened_record["identity"]["canonical_name_match"] is True
    assert shortened_record["identity"]["identity_method"] == "citation+party-text"
    assert shortened_record["identity"]["reason_code"] == "awaiting_r15_structural_gates"

    herlth_source = {
        "record_id": "commonwealth-v-herlth",
        "title": "Commonwealth v. Herlth",
        "expected_citation": "2026 PA Super 114",
        "court_level": "state",
        "year": 2026,
    }
    herlth_record = empty_record_shell("commonwealth-v-herlth", herlth_source, "selftest")
    herlth_cluster = {
        "id": 10870804,
        "case_name": "Com. v. Herlth, J.",
        "case_name_short": "Com. v. Herlth",
        "case_name_full": "Com. v. Herlth, J.",
        "date_filed": "2026-05-23",
        "court": "pasuperct",
        "citations": [{"cite": "2026 Pa. Super. 114", "type": 6}],
        "sub_opinions": [{"id": 10870805, "type": "020lead"}],
    }
    apply_identity(
        herlth_record,
        herlth_source,
        identity_fixture_search_result(10870804, 10870805),
        herlth_cluster,
        [],
        IdentityApplyClient("The Commonwealth and Herlth are both named in the lead opinion."),
        journal,
    )
    assert herlth_record["status"] == "under_review"
    assert herlth_record["identity"]["expected_citation_found"] is True
    assert herlth_record["identity"]["party_name_in_text"] is True
    assert herlth_record["identity"]["canonical_name_match"] is True
    assert herlth_record["identity"]["identity_method"] == "citation+party-text"
    assert herlth_record["identity"]["reason_code"] == "awaiting_r15_structural_gates"

    birchfield_source = {
        "record_id": "birchfield-caption",
        "title": "Birchfield v. North Dakota",
        "expected_citation": "579 U.S. 438",
        "court_level": "scotus",
        "year": 2016,
    }
    birchfield_record = empty_record_shell("birchfield-caption", birchfield_source, "selftest")
    birchfield_cluster = {
        "id": 3216497,
        "case_name": "Birchfield v. N. Dakota. William Robert Bernard",
        "case_name_short": "Birchfield",
        "case_name_full": "Birchfield v. N. Dakota. William Robert Bernard",
        "date_filed": "2016-06-23",
        "court": "scotus",
        "citations": [{"volume": 579, "reporter": "U.S.", "page": 438, "type": 1}],
        "sub_opinions": [{"id": 4321, "type": "020lead"}],
    }
    apply_identity(
        birchfield_record,
        birchfield_source,
        identity_fixture_search_result(3216497, 4321),
        birchfield_cluster,
        [],
        IdentityApplyClient("Birchfield and North Dakota are both named in the lead opinion."),
        journal,
    )
    assert birchfield_record["status"] == "under_review"
    assert birchfield_record["identity"]["canonical_name_match"] is True
    assert birchfield_record["identity"]["identity_method"] == "citation+party-text"
    assert birchfield_record["identity"]["reason_code"] == "awaiting_r15_structural_gates"
    assert "input caption does not match CL canonical caption" not in birchfield_record["provenance"]["warnings"]

    skinner_source = {
        "record_id": "skinner-association",
        "title": "Skinner v. Railway Labor Executives' Ass'n",
        "expected_citation": "489 U.S. 602",
        "court_level": "scotus",
        "year": 1989,
    }
    skinner_record = empty_record_shell("skinner-association", skinner_source, "selftest")
    skinner_cluster = {
        "id": 112219,
        "case_name": "Skinner v. Railway Labor Executives' Assn.",
        "case_name_short": "Skinner",
        "case_name_full": "Skinner v. Railway Labor Executives' Assn.",
        "date_filed": "1989-03-21",
        "court": "scotus",
        "citations": [{"volume": 489, "reporter": "U.S.", "page": 602, "type": 1}],
        "sub_opinions": [{"id": 5321, "type": "020lead"}],
    }
    skinner_text = "Skinner challenged the testing program adopted by the Association."
    assert "ass'n" not in skinner_text.lower()
    apply_identity(
        skinner_record,
        skinner_source,
        identity_fixture_search_result(112219, 5321),
        skinner_cluster,
        [],
        IdentityApplyClient(skinner_text),
        journal,
    )
    assert skinner_record["status"] == "under_review"
    assert skinner_record["identity"]["expected_citation_found"] is True
    assert skinner_record["identity"]["party_name_in_text"] is True
    assert skinner_record["identity"]["canonical_name_match"] is True
    assert skinner_record["identity"]["identity_method"] == "citation+party-text"
    assert "input caption does not match CL canonical caption" not in skinner_record["provenance"]["warnings"]

    fazaga_source = {
        "record_id": "federal-bureau-of-investigation-v-fazaga--6448059",
        "caption": "Federal Bureau of Investigation v. Fazaga",
        "expected_citation": "595 U.S. 344",
        "court_level": "scotus",
        "year": 2022,
        "docket": "20-828",
    }
    fazaga_record = empty_record_shell(fazaga_source["record_id"], fazaga_source, "selftest")
    fazaga_cluster = {
        "id": 6448059,
        "case_name": "FBI v. Fazaga",
        "case_name_short": "Fazaga",
        "case_name_full": "",
        "date_filed": "2022-03-04",
        "court": "scotus",
        "citations": [{"volume": 595, "reporter": "U.S.", "page": 344, "type": 1}],
        "sub_opinions": [{"id": 6448060, "type": "020lead"}],
    }
    apply_identity(
        fazaga_record,
        fazaga_source,
        identity_fixture_search_result(6448059, 6448060),
        fazaga_cluster,
        [],
        IdentityApplyClient("The FBI and Fazaga disputed the privilege question."),
        journal,
    )
    assert fazaga_record["status"] == "under_review"
    assert fazaga_record["identity"]["expected_citation_found"] is True
    assert fazaga_record["identity"]["party_name_in_text"] is True
    assert fazaga_record["identity"]["canonical_name_match"] is True
    assert fazaga_record["identity"]["identity_method"] == "citation+party-text"
    assert "input caption does not match CL canonical caption" not in fazaga_record["provenance"]["warnings"]

    reversed_source = {
        "record_id": "adams-reversed",
        "title": "Adams v. Williams",
        "expected_citation": "407 U.S. 143",
        "court_level": "scotus",
    }
    reversed_record = empty_record_shell("adams-reversed", reversed_source, "selftest")
    reversed_cluster = {
        "id": 999,
        "case_name": "Williams v. Adams",
        "case_name_short": "Williams v. Adams",
        "case_name_full": "Williams v. Adams",
        "date_filed": "1972-06-12",
        "court": "scotus",
        "citations": [{"volume": 407, "reporter": "U.S.", "page": 143, "type": 1}],
        "sub_opinions": [{"id": 201, "type": "020lead"}],
    }
    apply_identity(
        reversed_record,
        reversed_source,
        identity_fixture_search_result(999, 201),
        reversed_cluster,
        [],
        IdentityApplyClient("Adams is named, but the other side is absent."),
        journal,
    )
    assert reversed_record["status"] == "fabrication_suspected"
    assert reversed_record["identity"]["reason_code"] == "canonical_name_mismatch"
    rows = journal.rows()
    assert any(row.get("step") == "identity.party-text" and row.get("missing_terms") == ["williams"] for row in rows)


def self_test_identity_fallback_ladder():
    keith_source = {
        "record_id": "united-states-v-united-states-district-court-keith--108581",
        "caption": "United States v. United States District Court (Keith)",
        "expected_citation": "407 U.S. 297 (1972)",
        "court_level": "scotus",
        "year": 1972,
    }
    keith_params = identity_search_params(keith_source)
    assert keith_params["case_name"] == "United States v. United States District Court"
    assert keith_params["court"] == "scotus"
    assert keith_params["filed_after"] == "1972-01-01"
    assert keith_params["filed_before"] == "1972-12-31"
    assert keith_source["caption"] == "United States v. United States District Court (Keith)"
    keith_fallbacks = dict(identity_fallback_params(keith_source, keith_source["expected_citation"]))
    assert keith_fallbacks["q"]["q"] == "United States v. United States District Court"

    robinson_source = {
        "record_id": "united-states-v-robinson-4th-cir-en-banc--4385870",
        "caption": "United States v. Robinson (4th Cir. en banc)",
        "expected_citation": "846 F.3d 694 (4th Cir. 2017)",
        "court_level": "coa",
        "court": "U.S. Court of Appeals, 4th Cir. (en banc)",
        "year": 2017,
        "docket": "No. 14-4902",
    }
    robinson_params = identity_search_params(robinson_source)
    assert robinson_params["case_name"] == "United States v. Robinson"
    assert robinson_params["court"] == "ca4"
    assert robinson_params["filed_after"] == "2017-01-01"
    assert robinson_params["filed_before"] == "2017-12-31"
    assert robinson_source["caption"] == "United States v. Robinson (4th Cir. en banc)"
    robinson_fallbacks = dict(identity_fallback_params(robinson_source, robinson_source["expected_citation"]))
    assert robinson_fallbacks["q"]["q"] == "United States v. Robinson"
    assert robinson_fallbacks["docket_number"]["docket_number"] == "No. 14-4902"

    lewis_source = {
        "record_id": "Lewis v. United States (1966)",
        "title": "Lewis v. United States (1966)",
        "expected_citation": "385 U.S. 206 (1966)",
        "court_level": "scotus",
        "year": 1966,
        "docket": "36",
    }
    lewis_params = identity_search_params(lewis_source)
    assert lewis_params["case_name"] == "Lewis v. United States"
    assert lewis_params["court"] == "scotus"
    assert lewis_params["filed_after"] == "1966-01-01"
    assert lewis_params["filed_before"] == "1966-12-31"
    lewis_fallbacks = dict(identity_fallback_params(lewis_source, lewis_source["expected_citation"]))
    assert lewis_fallbacks["q"]["q"] == "Lewis v. United States"
    assert lewis_fallbacks["q"]["court"] == "scotus"
    assert lewis_fallbacks["q"]["filed_after"] == "1966-01-01"
    assert lewis_fallbacks["q"]["filed_before"] == "1966-12-31"
    assert "case_name" not in lewis_fallbacks["q"]
    assert lewis_source["record_id"] == "Lewis v. United States (1966)"
    assert lewis_source["title"] == "Lewis v. United States (1966)"

    lewis_path = "/tmp/s2-identity-lewis-disambiguator-self-test.jsonl"
    try:
        os.unlink(lewis_path)
    except FileNotFoundError:
        pass
    lewis_journal = Journal(lewis_path, "selftest")
    lewis_client = LewisDisambiguatorFallbackClient()
    lewis_result, lewis_cluster, lewis_alternates = resolve_identity(
        lewis_source,
        lewis_client,
        lewis_journal,
        ResumeState([]),
        "selftest",
    )
    assert lewis_result["cluster_id"] == 385206
    assert lewis_cluster["id"] == 385206
    assert lewis_alternates == []
    assert [call["step"] for call in lewis_client.search_calls] == [
        "identity.search",
        "identity.search.fallback",
        "identity.search.fallback",
    ]
    assert lewis_client.search_calls[0]["params"]["case_name"] == "Lewis v. United States"
    assert lewis_client.search_calls[1]["params"]["q"] == "Lewis v. United States"
    assert lewis_client.search_calls[2]["params"]["citation"] == "385 U.S. 206"
    assert [call["cluster_id"] for call in lewis_client.cluster_calls] == [107303, 107304, 107305, 385206]
    lewis_rows = [row for row in lewis_journal.rows() if row.get("step") == "identity.search.fallback"]
    assert [
        (row.get("rung"), row.get("result_count"), row.get("clusters_fetched"), row.get("viable"))
        for row in lewis_rows
    ] == [("q", 3, 3, False), ("citation", 1, 1, True)]
    lewis_identity_rows = [row for row in lewis_journal.rows() if row.get("step") == "identity"]
    assert lewis_identity_rows[-1]["search_rung"] == "citation"

    peters_path = "/tmp/s2-identity-peters-prefilter-self-test.jsonl"
    try:
        os.unlink(peters_path)
    except FileNotFoundError:
        pass
    peters_journal = Journal(peters_path, "selftest")
    peters_source = {
        "record_id": "Peters v. New York",
        "title": "Peters v. New York",
        "expected_citation": "392 U.S. 40 (1968)",
        "court_level": "scotus",
        "year": 1968,
    }
    peters_client = PetersCitationPrefilterClient()
    peters_result, peters_cluster, peters_alternates = resolve_identity(
        peters_source,
        peters_client,
        peters_journal,
        ResumeState([]),
        "selftest",
    )
    assert peters_result["cluster_id"] == 107730
    assert peters_cluster["id"] == 107730
    assert peters_alternates == []
    assert [call["step"] for call in peters_client.search_calls] == [
        "identity.search",
        "identity.search.fallback",
        "identity.search.fallback",
    ]
    assert peters_client.search_calls[2]["params"]["citation"] == "392 U.S. 40"
    assert [call["cluster_id"] for call in peters_client.cluster_calls] == [107730]
    peters_rows = [row for row in peters_journal.rows() if row.get("step") == "identity.search.fallback"]
    assert [
        (
            row.get("rung"),
            row.get("result_count"),
            row.get("clusters_fetched"),
            row.get("viable"),
            row.get("citation_prefilter_matched_rows"),
            row.get("citation_prefilter_fetched_cluster_ids"),
        )
        for row in peters_rows
    ] == [("q", 0, 0, False, 0, []), ("citation", 14, 1, True, 1, [107730])]
    peters_record = empty_record_shell("Peters v. New York", peters_source, "selftest")
    apply_identity(
        peters_record,
        peters_source,
        peters_result,
        peters_cluster,
        peters_alternates,
        IdentityApplyClient("Peters and New York are both named in the lead opinion."),
        peters_journal,
    )
    assert peters_record["status"] == "under_review"
    assert peters_record["identity"]["cluster_id"] == 107730
    assert peters_record["identity"]["expected_citation_found"] is True
    assert peters_record["identity"]["party_name_in_text"] is True
    assert peters_record["identity"]["canonical_name_match"] is False
    assert peters_record["identity"]["identity_method"] == "citation+party-text"
    assert peters_record["identity"]["reason_code"] == "caption_mismatch_canonical"
    assert "input caption does not match CL canonical caption" in peters_record["provenance"]["warnings"]

    no_cite_path = "/tmp/s2-identity-no-cite-year-court-self-test.jsonl"
    try:
        os.unlink(no_cite_path)
    except FileNotFoundError:
        pass
    no_cite_journal = Journal(no_cite_path, "selftest")
    no_cite_source = {
        "record_id": "recent-no-cite",
        "title": "Recent v. Case (2026)",
        "court_level": "scotus",
        "year": 2026,
    }
    no_cite_client = NoCiteFallbackClient()
    no_cite_result, no_cite_cluster, no_cite_alternates = resolve_identity(
        no_cite_source,
        no_cite_client,
        no_cite_journal,
        ResumeState([]),
        "selftest",
    )
    assert no_cite_result["cluster_id"] == 202601
    assert no_cite_cluster["id"] == 202601
    assert no_cite_alternates == []
    assert [call["step"] for call in no_cite_client.search_calls] == ["identity.search", "identity.search.fallback"]
    assert no_cite_client.search_calls[0]["params"]["case_name"] == "Recent v. Case"
    assert no_cite_client.search_calls[1]["params"]["q"] == "Recent v. Case"
    no_cite_rows = [row for row in no_cite_journal.rows() if row.get("step") == "identity.search.fallback"]
    assert [
        (row.get("rung"), row.get("result_count"), row.get("clusters_fetched"), row.get("viable"))
        for row in no_cite_rows
    ] == [("q", 1, 1, True)]
    no_cite_identity_rows = [row for row in no_cite_journal.rows() if row.get("step") == "identity"]
    assert no_cite_identity_rows[-1]["search_rung"] == "q"

    path = "/tmp/s2-identity-fallback-self-test.jsonl"
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
    journal = Journal(path, "selftest")
    source = {
        "record_id": "Birchfield v. North Dakota",
        "title": "Birchfield v. North Dakota",
        "expected_citation": "579 U.S. 438 (2016)",
        "court_level": "scotus",
        "year": 2016,
    }
    client = BirchfieldFallbackClient()
    result, cluster, alternates = resolve_identity(source, client, journal, ResumeState([]), "selftest")
    assert result["cluster_id"] == 3216497
    assert cluster["id"] == 3216497
    assert alternates == []
    assert [call["step"] for call in client.search_calls] == [
        "identity.search",
        "identity.search.fallback",
        "identity.search.fallback",
    ]
    assert client.search_calls[1]["params"]["q"] == "Birchfield v. North Dakota"
    assert client.search_calls[2]["params"]["citation"] == "579 U.S. 438"
    assert "filed_after" not in client.search_calls[2]["params"]
    assert [call["cluster_id"] for call in client.cluster_calls] == [9000, 9001, 9002, 3216497]
    fallback_rows = [row for row in journal.rows() if row.get("step") == "identity.search.fallback"]
    assert [
        (row.get("rung"), row.get("result_count"), row.get("clusters_fetched"), row.get("viable"))
        for row in fallback_rows
    ] == [("q", 10, 3, False), ("citation", 1, 1, True)]
    assert [
        (row.get("rung"), row.get("citation_prefilter_matched_rows"), row.get("citation_prefilter_fetched_cluster_ids"))
        for row in fallback_rows
    ] == [("q", 0, []), ("citation", 0, [])]
    identity_rows = [row for row in journal.rows() if row.get("step") == "identity"]
    assert identity_rows[-1]["search_rung"] == "citation"

    exhausted_path = "/tmp/s2-identity-fallback-exhausted-self-test.jsonl"
    try:
        os.unlink(exhausted_path)
    except FileNotFoundError:
        pass
    exhausted_journal = Journal(exhausted_path, "selftest")
    exhausted_source = {
        "record_id": "Missing v. Case",
        "title": "Missing v. Case",
        "expected_citation": "1 U.S. 999",
        "court_level": "scotus",
        "year": 2020,
        "docket": "20-999",
        "legacy_treatment_status": "good",
        "legacy_treatment_as_of": "2026-06-30",
    }
    exhausted_client = ExhaustedFallbackClient()
    missing_result, missing_cluster, missing_alternates = resolve_identity(
        exhausted_source,
        exhausted_client,
        exhausted_journal,
        ResumeState([]),
        "selftest",
    )
    assert missing_result is None
    assert missing_cluster is None
    assert missing_alternates is None
    assert exhausted_client.cluster_calls == []
    exhausted_rows = [row for row in exhausted_journal.rows() if row.get("step") == "identity.search.fallback"]
    assert [row.get("rung") for row in exhausted_rows] == ["q", "citation", "docket_number"]
    assert all(row.get("clusters_fetched") == 0 and row.get("viable") is False for row in exhausted_rows)

    tmp = tempfile.mkdtemp(prefix="s2-fallback-exhaustion-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        not_found_journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        not_found_client = ExhaustedFallbackClient()
        good_migration = {
            "mappings": {
                "good": {
                    "field_i_validity": "good_law",
                    "requires_point_overrides": False,
                    "requires_edge": False,
                    "varies_by_point": False,
                }
            }
        }
        record = process_page_record(
            exhausted_source,
            not_found_client,
            paths,
            {"court_classes": {}},
            good_migration,
            not_found_journal,
            ResumeState([]),
            "selftest",
            SessionTimer(None),
        )
        assert record["status"] == "not_found"
        rows = not_found_journal.rows()
        primary_rows = [
            row
            for row in rows
            if row.get("step") == "identity.search.prefilter"
        ]
        fallback_indexes = [
            index
            for index, row in enumerate(rows)
            if row.get("step") == "identity.search.fallback"
        ]
        not_found_indexes = [
            index
            for index, row in enumerate(rows)
            if row.get("step") == "identity" and row.get("final_status") == "not_found"
        ]
        assert [
            (row.get("rung"), row.get("result_count"), row.get("clusters_fetched"), row.get("viable"))
            for row in primary_rows
        ] == [("case_name", 0, 0, False)]
        assert [rows[index].get("rung") for index in fallback_indexes] == ["q", "citation", "docket_number"]
        assert all(rows[index].get("clusters_fetched") == 0 and rows[index].get("viable") is False for index in fallback_indexes)
        assert not_found_indexes and max(fallback_indexes) < not_found_indexes[-1]
        persisted = load_case_record(paths, exhausted_source["record_id"])
        assert persisted["status"] == "not_found"
        assert persisted["treatment"]["field_i_validity"] == "unverified"
        before_seed = json.dumps(persisted, sort_keys=True)
        assert seed_treatment_from_migration(persisted, exhausted_source, good_migration) is False
        assert json.dumps(persisted, sort_keys=True) == before_seed
        assert not_found_client.cluster_calls == []
    finally:
        shutil.rmtree(tmp)


def self_test_terminal_not_found_skip_and_warning_dedupe():
    tmp = tempfile.mkdtemp(prefix="s2-terminal-not-found-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        source = {
            "record_id": "Entick v. Carrington",
            "title": "Entick v. Carrington",
            "expected_citation": "19 How. St. Tr. 1029",
            "court_level": "other",
            "year": 1765,
            "counts": {},
        }
        record = empty_record_shell("Entick v. Carrington", source, "selftest")
        record["status"] = "not_found"
        record["identity"]["identity_method"] = "not_found"
        record["identity"]["reason_code"] = "no_candidate_cluster"
        append_warning(record, "not found in CL identity search; not proof of fabrication")
        write_case_record(paths, record)
        before = read_json(os.path.join(paths.cases, "Entick v. Carrington.json"))
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        resume = ResumeState([{"record_id": "Entick v. Carrington", "step": "identity", "status": "complete"}])
        skipped = process_page_record(
            source,
            NoSearchClient(),
            paths,
            {"court_classes": {}},
            {"mappings": {}},
            journal,
            resume,
            "selftest",
            SessionTimer(None),
        )
        after = read_json(os.path.join(paths.cases, "Entick v. Carrington.json"))
        assert skipped["status"] == "not_found"
        assert before == after
        rows = journal.rows()
        assert rows == [{
            "record_id": "Entick v. Carrington",
            "step": "identity",
            "status": "complete",
            "skipped": True,
            "loaded_existing": True,
            "terminal_not_found": True,
            "ts": rows[0]["ts"],
            "run": "selftest",
        }], rows

        reset_shell = empty_record_shell("Entick v. Carrington", source, "selftest-reset")
        set_record_status(reset_shell, "pending", explicit_adjudication=True)
        write_case_record(paths, reset_shell)
        rerun_journal = Journal(os.path.join(tmp, "rerun-journal.jsonl"), "selftest")
        rerun_client = ExhaustedFallbackClient()
        rerun = process_page_record(
            source,
            rerun_client,
            paths,
            {"court_classes": {}},
            {"mappings": {}},
            rerun_journal,
            ResumeState([
                {"record_id": "Entick v. Carrington", "step": "identity", "status": "complete"},
                {"record_id": "Entick v. Carrington", "step": "identity", "status": "pending", "adjudication_reset": True},
            ]),
            "selftest",
            SessionTimer(None),
        )
        assert rerun["status"] == "not_found"
        assert rerun_client.search_calls

        duplicate_record = empty_record_shell("dupe-case", {"record_id": "dupe-case", "title": "Dupe v. Case"}, "selftest")
        duplicate_record["status"] = "not_found"
        for _ in range(3):
            set_record_status(duplicate_record, "blocked", "identity was complete but no existing record or journaled selection was available")
            append_warning(duplicate_record, "identity completion could not be replayed; blocked rather than marking not_found")
            append_warning(duplicate_record, "legacy treatment migrated: good -> good_law")
        warnings = duplicate_record["provenance"]["warnings"]
        assert warnings.count("preserved not_found over blocked: identity was complete but no existing record or journaled selection was available") == 1
        assert warnings.count("identity completion could not be replayed; blocked rather than marking not_found") == 1
        assert warnings.count("legacy treatment migrated: good -> good_law") == 1
    finally:
        shutil.rmtree(tmp)


def off_cl_link_fixture(source, cite="19 How. St. Tr. 1029"):
    return {
        "source": source,
        "url": "https://example.com/%s/entick" % slugify(source),
        "confirmed": {
            "caption": "Entick v. Carrington",
            "cite": cite,
            "court": "Court of Common Pleas",
            "date": "1765-11-02",
        },
        "checked_date": "2026-07-05",
    }


def off_cl_adjudication_fixture(record_id="Entick v. Carrington"):
    return {
        "record_id": record_id,
        "case_name": "Entick v. Carrington",
        "citations": {
            "official": "19 How. St. Tr. 1029",
            "parallel": ["95 Eng. Rep. 807"],
        },
        "off_cl_links": [
            off_cl_link_fixture("Google Scholar"),
            off_cl_link_fixture("Official reporter", cite="95 Eng. Rep. 807"),
        ],
        "trail": {
            "adjudicated_by": "orchestrator",
            "finding": "A16 outside-CL corpus fixture",
        },
    }


def verified_off_cl_schema_errors(record, schema):
    errors = []
    if record.get("status") not in schema["properties"]["status"]["enum"]:
        errors.append("status enum rejected %s" % record.get("status"))
    method = record.get("identity", {}).get("identity_method")
    if method not in schema["definitions"]["identity"]["properties"]["identity_method"]["enum"]:
        errors.append("identity_method enum rejected %s" % method)
    count_source = record.get("progeny", {}).get("count_source")
    if count_source not in schema["definitions"]["progeny"]["properties"]["count_source"]["enum"]:
        errors.append("progeny.count_source enum rejected %s" % count_source)
    link_required = set(schema["definitions"]["off_cl_link"]["required"])
    for link in record.get("off_cl_links") or []:
        missing = link_required - set(link)
        if missing:
            errors.append("off_cl_link missing %s" % sorted(missing))
    if record.get("status") == "verified_off_cl":
        identity = record.get("identity") or {}
        if identity.get("identity_method") != "off_cl":
            errors.append("verified_off_cl identity_method must be off_cl")
        if identity.get("cluster_id") is not None or identity.get("lead_opinion_id") is not None:
            errors.append("verified_off_cl CL identity ids must be null")
        official = record.get("citations", {}).get("official")
        if not stripped_citation_text(official):
            errors.append("verified_off_cl citations.official must be non-empty")
        sources = {link.get("source") for link in record.get("off_cl_links") or []}
        if len(sources) < 2:
            errors.append("verified_off_cl requires two distinct off_cl sources")
        if record.get("progeny", {}).get("count_source") != "off_cl_na":
            errors.append("verified_off_cl progeny.count_source must be off_cl_na")
    return errors


def verified_off_cl_record_fixture():
    source = {
        "record_id": "Entick v. Carrington",
        "title": "Entick v. Carrington",
        "court": "Court of Common Pleas",
        "court_level": "other",
        "date_decided": "1765-11-02",
        "year": 1765,
    }
    record = empty_record_shell("Entick v. Carrington", source, "selftest")
    citations, links, _trail = verify_off_cl_adjudication(off_cl_adjudication_fixture(), record_id="Entick v. Carrington")
    record["status"] = "verified_off_cl"
    record["identity"].update({
        "case_name": "Entick v. Carrington",
        "case_name_short": "Entick v. Carrington",
        "case_name_full": "Entick v. Carrington",
        "identity_method": "off_cl",
        "cluster_id": None,
        "lead_opinion_id": None,
        "expected_citation_found": True,
        "party_name_in_text": True,
        "canonical_name_match": True,
    })
    record["citations"] = citations
    record["off_cl_links"] = links
    record["progeny"]["count_source"] = "off_cl_na"
    return record


def self_test_verified_off_cl_schema():
    schema = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_schema.json"))
    valid = verified_off_cl_record_fixture()
    assert verified_off_cl_schema_errors(valid, schema) == []
    duplicate_source = json.loads(json.dumps(valid))
    duplicate_source["off_cl_links"][1]["source"] = duplicate_source["off_cl_links"][0]["source"]
    assert "verified_off_cl requires two distinct off_cl sources" in verified_off_cl_schema_errors(duplicate_source, schema)
    null_official = json.loads(json.dumps(valid))
    null_official["citations"]["official"] = None
    assert "verified_off_cl citations.official must be non-empty" in verified_off_cl_schema_errors(null_official, schema)
    blank_official_string = json.loads(json.dumps(valid))
    blank_official_string["citations"]["official"] = "  "
    assert "verified_off_cl citations.official must be non-empty" in verified_off_cl_schema_errors(blank_official_string, schema)
    blank_official_dict = json.loads(json.dumps(valid))
    blank_official_dict["citations"]["official"]["cite"] = "  "
    assert "verified_off_cl citations.official must be non-empty" in verified_off_cl_schema_errors(blank_official_dict, schema)


def self_test_off_cl_elevation_path():
    tmp = tempfile.mkdtemp(prefix="s2-off-cl-elevation-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        source = {
            "record_id": "Entick v. Carrington",
            "record_id_status": "resolved",
            "source": "content/cases",
            "stub": False,
            "title": "Entick v. Carrington",
            "expected_citation": "19 How. St. Tr. 1029",
            "parallel_cite": "95 Eng. Rep. 807",
            "court": "Court of Common Pleas",
            "court_level": "other",
            "date_decided": "1765-11-02",
            "year": 1765,
            "lane_status": default_lane_status(),
            "counts": {},
        }
        write_json(paths.manifest, {
            "schema_version": "s2.manifest.v1",
            "generated_at": iso_now(),
            "records": [dict(source)],
        })
        previous = empty_record_shell("Entick v. Carrington", source, "oldrun")
        previous["status"] = "not_found"
        previous["identity"]["identity_method"] = "blocked"
        previous["provenance"]["warnings"] = [
            "identity completion could not be replayed; blocked rather than marking not_found",
            "identity completion could not be replayed; blocked rather than marking not_found",
            "legacy treatment migrated: good -> good_law",
        ]
        write_case_record(paths, previous)
        adjudication_path = os.path.join(tmp, "entick-adjudication.json")
        write_json(adjudication_path, off_cl_adjudication_fixture())
        manifest = ManifestStore(paths.manifest)
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        elevated = apply_off_cl_elevation(paths, manifest, journal, "Entick v. Carrington", adjudication_path, "selftest")
        assert elevated["status"] == "verified_off_cl"
        assert elevated["identity"]["identity_method"] == "off_cl"
        assert elevated["identity"]["cluster_id"] is None
        assert elevated["citations"]["official"]["cite"] == "19 How. St. Tr. 1029"
        assert len({link["source"] for link in elevated["off_cl_links"]}) == 2
        assert elevated["progeny"]["count_source"] == "off_cl_na"
        assert elevated["provenance"]["warnings"] == []
        assert manifest.by_record_id["Entick v. Carrington"]["status"] == "verified_off_cl"
        rows = journal.rows()
        assert any(row.get("step") == "adjudication" and row.get("action") == "elevate-off-cl" for row in rows)
        assert any(row.get("step") == "progeny" and row.get("count_source") == "off_cl_na" for row in rows)

        padded_official = off_cl_adjudication_fixture()
        padded_official["citations"]["official"] = "  19 How. St. Tr. 1029  "
        padded_citations, _links, _trail = verify_off_cl_adjudication(padded_official, record_id="Entick v. Carrington")
        assert padded_citations["official"]["cite"] == "19 How. St. Tr. 1029"
        assert padded_citations["display"] == "19 How. St. Tr. 1029"

        padded_official_dict = off_cl_adjudication_fixture()
        padded_official_dict["citations"]["official"] = {"cite": "  19 How. St. Tr. 1029  "}
        padded_citations, _links, _trail = verify_off_cl_adjudication(padded_official_dict, record_id="Entick v. Carrington")
        assert padded_citations["official"]["cite"] == "19 How. St. Tr. 1029"
        assert padded_citations["display"] == "19 How. St. Tr. 1029"

        bad_duplicate_path = os.path.join(tmp, "bad-duplicate-source.json")
        bad_duplicate = off_cl_adjudication_fixture()
        bad_duplicate["off_cl_links"][1]["source"] = bad_duplicate["off_cl_links"][0]["source"]
        write_json(bad_duplicate_path, bad_duplicate)
        try:
            verify_off_cl_adjudication(read_json(bad_duplicate_path), record_id="Entick v. Carrington")
        except ValueError as exc:
            assert "two distinct" in str(exc)
        else:
            raise AssertionError("duplicate off-CL sources were accepted")

        for label, official in (
            ("null", None),
            ("blank-string", "  "),
            ("blank-dict", {"cite": "  "}),
        ):
            bad_official_path = os.path.join(tmp, "bad-official-%s.json" % label)
            bad_official = off_cl_adjudication_fixture()
            bad_official["citations"]["official"] = official
            write_json(bad_official_path, bad_official)
            try:
                verify_off_cl_adjudication(read_json(bad_official_path), record_id="Entick v. Carrington")
            except ValueError as exc:
                assert "citation is empty" in str(exc)
            else:
                raise AssertionError("%s official citation was accepted" % label)

        try:
            apply_off_cl_elevation(paths, manifest, journal, "Entick v. Carrington", None, "selftest")
        except SystemExit as exc:
            assert "builder never self-elevates" in str(exc)
        else:
            raise AssertionError("off-CL elevation ran without an adjudication file")
    finally:
        shutil.rmtree(tmp)


def self_test_frontier_stub_record_id_bounds_and_resume():
    tmp = tempfile.mkdtemp(prefix="s2-frontier-long-caption-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        source = {
            "record_id": "UNRESOLVED:arkansas-v-sanders",
            "record_id_status": "UNRESOLVED",
            "stub": True,
            "caption": "Arkansas v. Sanders",
            "slug": "arkansas-v-sanders",
            "court_level": "state",
            "year": 1979,
            "roster_key": "Arkansas v. Sanders|1979|fixture",
            "source_row_index": 4,
            "counts": {},
        }
        partial = empty_record_shell(source["record_id"], source, "selftest")
        write_case_record(paths, partial)
        canonical = (
            "Sarah Sanders, in her official capacity as Governor of Arkansas, Lindsay Wallace, "
            "in her official capacity as Secretary of the Arkansas Department of Corrections, "
            "and the Arkansas Department of Corrections v. Arkansas Board of Corrections and "
            "Benny Magness, in his official capacity as Chairman of the Arkansas Board of Corrections"
        )
        assert len(slugify(canonical)) > 255
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        client = FrontierLongCaptionClient(canonical)
        record, final_id = process_frontier_record(
            source,
            client,
            paths,
            {"court_classes": {"state": {"reporter_classes": {"official": 1}, "regional_reporters": {}}}},
            journal,
            ResumeState([{"record_id": source["record_id"], "step": "case-interruption", "status": "interrupted", "reason": "unhandled_exception"}]),
            "selftest",
        )
        assert final_id == "arkansas-v-sanders--10601315", final_id
        assert record["record_id"] == final_id
        assert re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*--[0-9]+$", final_id), final_id
        assert len((final_id + ".json").encode("utf-8")) <= 120
        assert os.path.exists(os.path.join(paths.cases, final_id + ".json"))
        assert not os.path.exists(os.path.join(paths.cases, source["record_id"] + ".json"))
        assert client.search_calls and client.cluster_calls
        rows = journal.rows()
        assert rows[-1]["record_id"] == source["record_id"]
        assert rows[-1]["final_record_id"] == final_id

        fallback_source = {
            "record_id": "UNRESOLVED:citation-fallback",
            "record_id_status": "UNRESOLVED",
            "stub": True,
            "caption": "Citation Fallback v. Case",
            "slug": "citation-fallback-v-case",
            "court_level": "scotus",
            "expected_citation": "123 U.S. 456 (2026)",
            "docket": "25-1",
            "year": 2026,
            "roster_key": "Citation Fallback v. Case|scotus|2026|123 U.S. 456|fixture",
            "source_row_index": 5,
            "counts": {},
        }
        fallback_client = FrontierCitationFallbackClient()
        fallback_record, fallback_id = process_frontier_record(
            fallback_source,
            fallback_client,
            paths,
            {"court_classes": {"scotus": {"reporters": {"U.S.": 1}}}},
            journal,
            ResumeState([]),
            "selftest",
        )
        assert fallback_id == "citation-fallback-v-case--123456", fallback_id
        assert fallback_record["status"] == "verified_identity"
        assert any(call["step"] == "frontier.identity.search.citation" for call in fallback_client.search_calls), fallback_client.search_calls
        assert journal.rows()[-1]["search_rung"] == "citation"

        docket_source = {
            "record_id": "UNRESOLVED:docket-continuation",
            "record_id_status": "UNRESOLVED",
            "stub": True,
            "caption": "United States v. $8,850 in Currency",
            "slug": "united-states-v-8-850-in-currency",
            "court_level": "scotus",
            "docket": "81-1062",
            "year": 1983,
            "roster_key": "United States v. $8,850 in Currency|scotus|1983|81-1062|fixture",
            "source_row_index": 6,
            "counts": {},
        }
        docket_client = DocketContinuationFrontierClient()
        docket_record, docket_id = process_frontier_record(
            docket_source,
            docket_client,
            paths,
            {"court_classes": {"scotus": {"reporters": {"U.S.": 1}, "reporter_classes": {"official": 1}}}},
            journal,
            ResumeState([]),
            "selftest",
        )
        assert docket_id == "united-states-v-8-850-in-currency--88500", docket_id
        assert docket_record["status"] == "verified_identity"
        assert docket_record["identity"]["canonical_name_match"] is False
        assert docket_record["identity"]["reason_code"] == "caption_mismatch_accepted_by_docket_number"
        assert any(call["params"].get("docket_number") == "81-1062" for call in docket_client.search_calls), docket_client.search_calls
        assert [call["cluster_id"] for call in docket_client.cluster_calls] == [88100, 88500]
        docket_rows = [
            row for row in journal.rows()
            if row.get("record_id") == docket_source["record_id"]
            and row.get("step") in ("frontier.identity.search.prefilter", "frontier.identity.search.fallback")
        ]
        assert [
            (row.get("rung"), row.get("clusters_fetched"), row.get("viable"), row.get("caption_match"), row.get("remaining_stronger_rungs"))
            for row in docket_rows
        ] == [
            ("case_name", 1, False, False, ["docket_number"]),
            ("q", 0, False, None, ["docket_number"]),
            ("docket_number", 1, True, False, []),
        ]
        assert journal.rows()[-1]["search_rung"] == "docket_number"

        no_result = dict(source)
        no_result["caption"] = "No Result v. Case"
        not_found_id = not_found_stub_record_id(no_result)
        assert re.match(r"^no-result-v-case--u[0-9a-f]{8}$", not_found_id), not_found_id
    finally:
        shutil.rmtree(tmp)


def self_test_s6_candidate_intake():
    tmp = tempfile.mkdtemp(prefix="s2-s6-candidate-intake-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        existing_caption = {
            "record_id": "Existing Caption v. Case",
            "record_id_status": "resolved",
            "source": "content/cases",
            "stub": False,
            "page_path": "content/cases/Existing Caption v. Case.md",
            "slug": "existing-caption-v-case",
            "title": "Existing Caption v. Case",
            "expected_citation": "1 U.S. 1 (1901)",
            "docket": "10-1",
            "court_level": "scotus",
            "status": "verified",
            "lane_status": default_lane_status(),
            "counts": {},
        }
        existing_docket = {
            "record_id": "Existing Docket v. Case",
            "record_id_status": "resolved",
            "source": "content/cases",
            "stub": False,
            "page_path": "content/cases/Existing Docket v. Case.md",
            "slug": "existing-docket-v-case",
            "title": "Existing Docket v. Case",
            "expected_citation": "2 U.S. 2 (1902)",
            "docket": "22-333",
            "court_level": "scotus",
            "status": "under_review",
            "lane_status": default_lane_status(),
            "counts": {},
        }
        write_json(paths.manifest, {
            "schema_version": "s2.manifest.v1",
            "generated_at": iso_now(),
            "counts": {},
            "records": [existing_caption, existing_docket],
        })
        queue_path = os.path.join(tmp, "queue.jsonl")
        queue_rows = [
            {
                "queue": "S6->S2 R7 candidate fixture",
                "rows": 6,
                "note": "metadata header must be ignored",
                "generated": "2026-07-06",
            },
            {
                "caption": "Novel Candidate v. Case",
                "docket": "99-100",
                "citation": "999 U.S. 100 (2026)",
                "date": "2026-05-01",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
            {
                "caption": "Slip Status One v. Case",
                "docket": "25-101",
                "citation": "607 U.S. ___",
                "date": "2026-05-01",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
            {
                "caption": "Slip Status Two v. Case",
                "docket": "25-102",
                "citation": "607 U.S. ___",
                "date": "2026-05-01",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
            {
                "caption": "Existing Caption v. Case",
                "docket": "88-777",
                "citation": "888 U.S. 8 (2026)",
                "date": "2026-05-02",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
            {
                "caption": "Citation Duplicate v. Case",
                "docket": "55-5",
                "citation": "1 U.S. 1",
                "date": "2026-05-02",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
            {
                "caption": "Different Caption v. Docket",
                "docket": "22-333",
                "citation": "777 U.S. 7 (2026)",
                "date": "2026-05-03",
                "court": "scotus",
                "leg": "sweep",
                "prong": "c",
                "posture": None,
                "page_candidate": True,
            },
        ]
        with open(queue_path, "w", encoding="utf-8") as f:
            for row in queue_rows:
                f.write(json.dumps(row, sort_keys=True) + "\n")

        manifest = ManifestStore(paths.manifest)
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        result = add_s6_candidates(manifest, journal, queue_path)
        manifest.save()

        assert len(result["appended"]) == 3, result
        assert len(result["skipped"]) == 3, result
        saved = read_json(paths.manifest)
        assert saved["counts"]["total_manifest_records"] == 5, saved["counts"]
        assert saved["counts"]["status_counts"]["pending"] == 3, saved["counts"]
        ids = [row["record_id"] for row in saved["records"]]
        assert len(ids) == len(set(ids)), ids

        appended = result["appended"][0]
        assert appended["source"] == "s6-candidates/sweep"
        assert appended["status"] == "pending"
        assert appended["stub"] is True
        assert appended["page_candidate"] is True
        assert appended["lane_status"] == frontier_stub_lane_status()
        assert appended["record_id"].startswith("UNRESOLVED:s6-candidate-novel-candidate-v-case-")
        assert appended["expected_citation"] == "999 U.S. 100 (2026)"
        assert appended["docket"] == "99-100"
        assert appended["year"] == 2026
        placeholder_appended = [row for row in result["appended"] if row.get("citation") == "607 U.S. ___"]
        assert [row.get("docket") for row in placeholder_appended] == ["25-101", "25-102"], placeholder_appended
        assert manifest_row_citation_keys(placeholder_appended[0]) == set()

        rows = journal.rows()
        assert len(rows) == 6, rows
        assert all(row.get("step") == "s6-candidate-intake" for row in rows)
        assert all(row.get("adjudicated_by") == S6_CANDIDATE_INTAKE_ADJUDICATOR for row in rows)
        append_rows = [row for row in rows if row.get("action") == "append"]
        skip_rows = [row for row in rows if row.get("action") == "skip-duplicate"]
        assert len(append_rows) == 3 and append_rows[0]["record_id"] == appended["record_id"], rows
        assert {row.get("duplicate_by") for row in skip_rows} == {"caption-slug", "docket", "citation"}, skip_rows
        assert {row.get("existing_record_id") for row in skip_rows} == {
            "Existing Caption v. Case",
            "Existing Docket v. Case",
        }, skip_rows
        assert any(row.get("duplicate_by") == "citation" and row.get("duplicate_key") == "1 us 1" for row in skip_rows), skip_rows

        bad_manifest = ManifestStore(paths.manifest)
        bad_manifest.data["records"].append(dict(bad_manifest.data["records"][0]))
        try:
            bad_manifest.save()
            assert False, "duplicate record_id save should fail"
        except ValueError as exc:
            assert "duplicate manifest record_id" in str(exc), exc
        assert read_json(paths.manifest)["counts"]["total_manifest_records"] == 5

        indexes = build_manifest_candidate_dedupe([existing_caption, existing_docket])
        citation_duplicate = s6_candidate_manifest_row({
            "caption": "Citation Duplicate v. Case",
            "docket": "55-5",
            "citation": "1 U.S. 1",
            "court": "scotus",
            "leg": "sweep",
            "page_candidate": True,
        }, 10)
        duplicate = find_s6_candidate_duplicate(citation_duplicate, indexes)
        assert duplicate[0] == "citation" and duplicate[2]["record_id"] == "Existing Caption v. Case", duplicate
    finally:
        shutil.rmtree(tmp)


class ProgenyBoundedClient:
    def __init__(self, paths):
        self.paths = paths
        self.search_calls = []
        self.url_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        query = params.get("q")
        if query == "cites:(200 OR 201)":
            return {
                "count": 5,
                "results": [{"id": "row-1"}, {"id": "row-2"}],
                "next": "page-2",
            }
        if query == "cites:(200)":
            return {"count": 3, "results": [{"id": "only-count"}], "next": None}
        if query == "cites:(201)":
            return {"count": 4, "results": [{"id": "only-count"}], "next": None}
        raise AssertionError("unexpected progeny query %r" % query)

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        self.url_calls.append({"url": url, "step": step})
        raise AssertionError("bounded progeny must not paginate: %s" % url)


class InterruptAfterIdentityClient(SelfTestClient):
    def __init__(self, paths, journal):
        super().__init__(paths, journal)
        self.budget = CallBudget(max_calls=1)

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        text = super().text_for_opinion(opinion_ref, record_id=record_id, step=step)
        self.budget.record_call()
        return text


class NoCallResumeClient:
    def __init__(self):
        self.calls = []
        self.search_calls = []
        self.url_calls = []

    def _unexpected(self, method):
        self.calls.append(method)
        raise AssertionError("resume-stability fixture made unexpected %s call" % method)

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        self._unexpected("search")

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        self.url_calls.append({"url": url, "step": step})
        self._unexpected("get_json_url")

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        self._unexpected("get_cluster")

    def opinion_ref(self, opinion_id, source_array, context=None):
        self._unexpected("opinion_ref")

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        self._unexpected("text_for_opinion")


def self_test_bounded_progeny():
    tmp = tempfile.mkdtemp(prefix="s2-progeny-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        source = {"record_id": "bounded-case", "title": "Bounded v. Case"}
        record = empty_record_shell("bounded-case", source, "selftest")
        record["identity"]["sibling_ids"] = [200, 201]
        record["progeny"]["citation_count"] = 9
        record["progeny"]["outbound_opinion_edges"] = [{"source_opinion_id": 200, "cited_id": 999, "source": "test"}]
        client = ProgenyBoundedClient(paths)
        assert fetch_progeny(record, source, client, journal, ResumeState([]))
        assert client.url_calls == []
        assert record["progeny"]["complete_query"] == "cites:(200 OR 201)"
        assert record["progeny"]["indexed_citing_opinions"] == 5
        assert record["progeny"]["count_source"] == "search"
        assert record["progeny"]["enumeration"] == "bounded"
        assert record["progeny"]["cursor"] == "page-2"
        assert record["progeny"]["rows_cached"] == 2
        assert record["progeny"]["citation_count"] == 9
        assert record["progeny"]["outbound_opinion_edges"][0]["cited_id"] == 999
        per_queries = [call["params"] for call in client.search_calls if call["step"] == "progeny.per_sibling"]
        assert per_queries == [
            {"type": "o", "q": "cites:(200)", "page_size": 1, "fields": "id"},
            {"type": "o", "q": "cites:(201)", "page_size": 1, "fields": "id"},
        ]
        with open(record["progeny"]["cache_path"], encoding="utf-8") as f:
            cached = [json.loads(line) for line in f if line.strip()]
        assert cached[0]["_meta"] == "progeny-cache"
        assert cached[0]["partial"] is True and cached[0]["cursor"] == "page-2"
        assert [row["id"] for row in cached[1:]] == ["row-1", "row-2"]
    finally:
        shutil.rmtree(tmp)


def self_test_outbound_edges_from_search_result():
    result = {
        "cluster_id": 100,
        "opinions": [
            {"id": 200, "cites": [1, 2, 2, {"id": 3}]},
            {"cluster_id": 999, "cites": [4]},
            {"id": 201, "cites": []},
        ],
    }
    assert outbound_edges_from_search_result(result) == [
        {"source_opinion_id": 200, "cited_id": 1, "source": "search.opinions[].cites[]"},
        {"source_opinion_id": 200, "cited_id": 2, "source": "search.opinions[].cites[]"},
        {"source_opinion_id": 200, "cited_id": 3, "source": "search.opinions[].cites[]"},
    ]


def self_test_identity_skip_preserves_record():
    tmp = tempfile.mkdtemp(prefix="s2-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        source = {
            "record_id": "smith-v-jones",
            "title": "Smith v. Jones",
            "expected_citation": "1 U.S. 2",
            "court_level": "scotus",
            "year": 2024,
            "legacy_treatment_status": "good",
            "legacy_treatment_as_of": "2026-06-30",
        }
        precedence = {"court_classes": {"scotus": {"reporters": {"U.S.": 1}}}}
        migration = {
            "mappings": {
                "good": {
                    "field_i_validity": "good_law",
                    "requires_point_overrides": False,
                    "requires_edge": False,
                    "varies_by_point": False,
                }
            }
        }
        client = SelfTestClient(paths, journal)
        session = SessionTimer(None)
        first = process_page_record(source, client, paths, precedence, migration, journal, ResumeState([]), "selftest", session)
        assert first["status"] == "under_review"
        before = json.dumps(load_case_record(paths, "smith-v-jones"), sort_keys=True)
        calls_before = (len(client.search_calls), len(client.url_calls))
        resumed = ResumeState(journal.rows())
        second = process_page_record(source, client, paths, precedence, migration, journal, resumed, "selftest", SessionTimer(None))
        after = json.dumps(load_case_record(paths, "smith-v-jones"), sort_keys=True)
        calls_after = (len(client.search_calls), len(client.url_calls))
        assert second["status"] != "not_found"
        assert before == after
        assert calls_after == calls_before

        lucky_sources = [
            ("Henry v. United States (1959)", "361 U.S. 98 (1959)", 1959),
            ("Chapman v. United States (1961)", "365 U.S. 610 (1961)", 1961),
            ("Davis v. United States (2011)", "564 U.S. 229 (2011)", 2011),
            ("Harris v. United States (1968)", "390 U.S. 234 (1968)", 1968),
        ]
        for index, (record_id, expected_citation, year) in enumerate(lucky_sources, start=1):
            disambiguated_source = {
                "record_id": record_id,
                "title": record_id,
                "expected_citation": expected_citation,
                "court_level": "scotus",
                "year": year,
            }
            record = empty_record_shell(record_id, disambiguated_source, "selftest")
            record["status"] = "under_review"
            record["identity"].update({
                "cluster_id": 5000 + index,
                "lead_opinion_id": 6000 + index,
                "sibling_ids": [6000 + index],
                "identity_method": "citation+party-text",
                "expected_citation_found": True,
                "party_name_in_text": True,
                "canonical_name_match": True,
            })
            record["citations"]["display"] = normalize_cite(expected_citation)
            record["citations"]["all"] = [{"cite": normalize_cite(expected_citation), "source": "selftest"}]
            record["progeny"]["complete_query"] = "cites:(%s)" % (6000 + index)
            record["progeny"]["citation_count"] = index
            record["treatment"]["field_i_validity"] = "good_law"
            write_case_record(paths, record)
            journal.append(record_id=record_id, step="identity", status="complete", selected_cluster_id=5000 + index)
            journal.append(record_id=record_id, step="citations", status="complete")
            journal.append(record_id=record_id, step="pinpoints", status="complete")
            journal.append(record_id=record_id, step="progeny", status="complete")
            for lane, _cap in TREATMENT_LANES:
                journal.append(record_id=record_id, step="treatment", lane=lane, status="complete")

        no_call_client = NoCallResumeClient()
        completed_resume = ResumeState(journal.rows())
        for record_id, expected_citation, year in lucky_sources:
            disambiguated_source = {
                "record_id": record_id,
                "title": record_id,
                "expected_citation": expected_citation,
                "court_level": "scotus",
                "year": year,
            }
            before = json.dumps(load_case_record(paths, record_id), sort_keys=True)
            resumed_record = process_page_record(
                disambiguated_source,
                no_call_client,
                paths,
                precedence,
                migration,
                journal,
                completed_resume,
                "selftest",
                SessionTimer(None),
            )
            after = json.dumps(load_case_record(paths, record_id), sort_keys=True)
            assert resumed_record["status"] == "under_review"
            assert "_ingest_interrupted" not in resumed_record
            assert before == after
        assert no_call_client.calls == []
    finally:
        shutil.rmtree(tmp)


def self_test_budget_interruption_resume():
    tmp = tempfile.mkdtemp(prefix="s2-budget-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        source = {
            "record_id": "smith-v-jones",
            "title": "Smith v. Jones",
            "expected_citation": "1 U.S. 2",
            "court_level": "scotus",
            "year": 2024,
            "legacy_treatment_status": "good",
            "legacy_treatment_as_of": "2026-06-30",
        }
        precedence = {"court_classes": {"scotus": {"reporters": {"U.S.": 1}}}}
        migration = {
            "mappings": {
                "good": {
                    "field_i_validity": "good_law",
                    "requires_point_overrides": False,
                    "requires_edge": False,
                    "varies_by_point": False,
                }
            }
        }
        first_client = InterruptAfterIdentityClient(paths, journal)
        first = process_page_record(source, first_client, paths, precedence, migration, journal, ResumeState([]), "selftest", SessionTimer(None))
        assert first.get("_ingest_interrupted") == "call_budget_exhausted"
        persisted = load_case_record(paths, "smith-v-jones")
        assert persisted and persisted["identity"]["cluster_id"] == 100
        rows = journal.rows()
        assert any(row.get("step") == "case-interruption" and row.get("after_step") == "identity" for row in rows)
        assert not any(row.get("step") == "citations" and row.get("status") == "complete" for row in rows)

        resume_client = SelfTestClient(paths, journal)
        resumed = process_page_record(source, resume_client, paths, precedence, migration, journal, ResumeState(rows), "selftest", SessionTimer(None))
        assert resumed["citations"]["display"] == "1 U.S. 2"
        assert resumed["progeny"]["complete_query"] == "cites:(200)"
        assert not any(call["params"].get("case_name") for call in resume_client.search_calls)
        resumed_rows = journal.rows()
        assert any(row.get("step") == "citations" and row.get("status") == "complete" for row in resumed_rows)
        assert any(row.get("step") == "progeny" and row.get("status") == "complete" for row in resumed_rows)
    finally:
        shutil.rmtree(tmp)


def self_test_readjudicate_reset_reruns_fail_closed_record():
    tmp = tempfile.mkdtemp(prefix="s2-readjudicate-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        manifest_data = {
            "schema_version": "s2.manifest.v1",
            "generated_at": iso_now(),
            "records": [{
                "record_id": "smith-v-jones",
                "record_id_status": "resolved",
                "source": "content/cases",
                "stub": False,
                "title": "Smith v. Jones",
                "expected_citation": "1 U.S. 2",
                "court_level": "scotus",
                "year": 2024,
                "legacy_treatment_status": "good",
                "legacy_treatment_as_of": "2026-06-30",
                "status": "fabrication_suspected",
                "lane_status": {
                    "identity": "complete",
                    "citations": "complete",
                    "pinpoints": "complete",
                    "progeny": "complete",
                    "treatment": {
                        "lane1_negative": {"status": "complete", "cursor": None},
                        "lane2_top_cited": {"status": "complete", "cursor": None},
                        "lane3_recency": {"status": "complete", "cursor": None},
                    },
                    "provenance": "pending",
                },
                "counts": {"cl_calls": 99},
            }],
        }
        write_json(paths.manifest, manifest_data)
        manifest = ManifestStore(paths.manifest)
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        journal.append(record_id="smith-v-jones", step="identity", status="complete", selected_cluster_id=100)
        journal.append(record_id="smith-v-jones", step="citations", status="complete")
        journal.append(record_id="smith-v-jones", step="pinpoints", status="complete")
        journal.append(record_id="smith-v-jones", step="progeny", status="complete")
        for lane, _cap in TREATMENT_LANES:
            journal.append(record_id="smith-v-jones", step="treatment", lane=lane, status="complete")

        source = manifest.by_record_id["smith-v-jones"]
        fail_closed = empty_record_shell("smith-v-jones", source, "selftest")
        fail_closed["status"] = "fabrication_suspected"
        fail_closed["identity"].update({
            "case_name": "Stale v. Payload",
            "cluster_id": 999999,
            "lead_opinion_id": 888888,
            "sibling_ids": [888888, 777777],
            "identity_method": "fabrication-check",
            "expected_citation_found": True,
            "party_name_in_text": True,
            "canonical_name_match": False,
        })
        fail_closed["identity"]["reason_code"] = "canonical_name_mismatch"
        fail_closed["citations"]["display"] = "999 U.S. 1"
        fail_closed["citations"]["all"] = [{"cite": "999 U.S. 1", "source": "stale"}]
        fail_closed["pinpoints"] = [{"id": "stale-pin", "quote": "stale"}]
        fail_closed["progeny"].update({
            "complete_query": "cites:(888888)",
            "citation_count": 12,
            "outbound_opinion_edges": [{"source_opinion_id": 888888, "cited_id": 1, "source": "stale"}],
        })
        fail_closed["treatment"].update({
            "field_i_validity": "good_law",
            "edges": [{"citing_case": {"name": "Stale v. Payload"}}],
        })
        write_case_record(paths, fail_closed)

        reset_ids = apply_readjudications(paths, manifest, journal, ["smith-v-jones"], "selftest")
        assert reset_ids == ["smith-v-jones"]
        reset_record = load_case_record(paths, "smith-v-jones")
        assert reset_record["status"] == "pending"
        assert reset_record["identity"]["cluster_id"] is None
        assert reset_record["identity"]["lead_opinion_id"] is None
        assert reset_record["identity"]["sibling_ids"] == []
        assert reset_record["identity"]["identity_method"] == "pending"
        assert reset_record["identity"]["expected_citation_found"] is False
        assert reset_record["citations"]["display"] is None
        assert reset_record["citations"]["all"] == []
        assert reset_record["pinpoints"] == []
        assert reset_record["progeny"]["complete_query"] is None
        assert reset_record["progeny"]["outbound_opinion_edges"] == []
        assert reset_record["treatment"]["field_i_validity"] == "unverified"
        assert reset_record["treatment"]["edges"] == []
        reset_resume = ResumeState(manifest.resume_rows() + journal.rows())
        assert not reset_resume.step_complete("smith-v-jones", "identity")
        assert not reset_resume.lane_complete("smith-v-jones", "treatment", "lane1_negative")
        field_rows = [row for row in journal.rows() if row.get("step") == "adjudication.field-reset"]
        assert {row.get("field") for row in field_rows} == set(READJUDICATION_RESET_FIELDS)
        identity_reset = [row for row in field_rows if row.get("field") == "identity"][0]
        assert identity_reset["before_cluster_id"] == 999999
        assert identity_reset["after_cluster_id"] is None
        assert any(
            row.get("step") == "adjudication"
            and row.get("findings") == READJUDICATION_FINDINGS
            and row.get("action") == "reset-identity-and-rerun"
            for row in journal.rows()
        )

        precedence = {"court_classes": {"scotus": {"reporters": {"U.S.": 1}}}}
        migration = {
            "mappings": {
                "good": {
                    "field_i_validity": "good_law",
                    "requires_point_overrides": False,
                    "requires_edge": False,
                    "varies_by_point": False,
                }
            }
        }
        client = SelfTestClient(paths, journal)
        rerun = process_page_record(source, client, paths, precedence, migration, journal, reset_resume, "selftest", SessionTimer(None))
        assert rerun["status"] == "under_review"
        assert rerun["identity"]["identity_method"] == "citation+party-text"
        assert any(call["step"] == "identity.search" for call in client.search_calls)
    finally:
        shutil.rmtree(tmp)


class TreatmentResumeClient:
    def __init__(self, pages):
        self.pages = dict(pages)
        self.search_calls = []
        self.url_calls = []

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append(step)
        return self.pages["first"]

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        self.url_calls.append(url)
        return self.pages[url]

    def opinion_ref(self, opinion_id, source_array, context=None):
        return {"opinion_id": int(opinion_id), "source_array": source_array, "context": context or {}}

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        return ""


class TreatmentCapCursorClient:
    def __init__(self):
        self.search_calls = []

    def build_url(self, endpoint, params=None):
        endpoint = endpoint.strip("/")
        query = urllib.parse.urlencode(params or {}, doseq=True)
        return "https://fixture.example/%s/%s" % (endpoint, "?" + query if query else "")

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        return {
            "count": 25,
            "results": [
                {"caseName": "Citing %02d" % index, "cluster_id": 9000 + index, "opinions": []}
                for index in range(25)
            ],
            "next": None,
        }

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        raise AssertionError("cap cursor fixture should not request a follow-up URL")


class LaneOnlyTreatmentClient:
    def __init__(self):
        self.search_calls = []

    def build_url(self, endpoint, params=None):
        endpoint = endpoint.strip("/")
        query = urllib.parse.urlencode(params or {}, doseq=True)
        return "https://fixture.example/%s/%s" % (endpoint, "?" + query if query else "")

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        if step != "treatment.lane2_top_cited.search":
            raise AssertionError("rerun fixture executed non-target lane: %s" % step)
        return {"count": 0, "results": [], "next": None}

    def get_json_url(self, url, cache=True, record_id=None, step=None):
        raise AssertionError("rerun fixture should not resume URL %s" % url)


class CountingLimiter:
    def __init__(self):
        self.waits = 0
        self.completed = 0

    def wait(self):
        self.waits += 1

    def mark_completed(self):
        self.completed += 1


class CountingHourly:
    def __init__(self):
        self.waits = 0

    def wait(self):
        self.waits += 1


class TimeoutDuringTreatmentClient(CourtListenerClient):
    def __init__(self, paths, journal):
        self.counting_rate = CountingLimiter()
        self.counting_hourly = CountingHourly()
        super().__init__(
            paths=paths,
            token="selftest-token",
            token_fingerprint="selftest",
            journal=journal,
            budget=CallBudget(max_calls=10),
            rate=self.counting_rate,
            hourly=self.counting_hourly,
            run_id="selftest",
        )
        self.search_steps = []
        self.urlopen_calls = []
        self.retry_sleeps = []
        self.sleep = self.retry_sleeps.append
        self.retry_jitter = lambda: 0.0
        self.urlopen = self.timeout_urlopen

    def timeout_urlopen(self, req, timeout=None):
        self.urlopen_calls.append({"url": req.full_url, "timeout": timeout})
        raise TimeoutError("socket read timeout")

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_steps.append(step)
        if step == "identity.search":
            return {
                "count": 1,
                "results": [{
                    "cluster_id": 100,
                    "caseName": "Smith v. Jones",
                    "opinions": [{"id": 200, "type": "020lead"}],
                    "sibling_ids": [200],
                }],
                "next": None,
            }
        if step == "progeny.search":
            return {"count": 1, "results": [{"id": "citing-row"}], "next": None}
        if step == "progeny.per_sibling":
            return {"count": 1, "results": [{"id": "count-row"}], "next": None}
        if step == "treatment.lane1_negative.search":
            return {
                "count": 1,
                "results": [{
                    "caseName": "Timeout Citer",
                    "cluster_id": 300,
                    "citation": "2 U.S. 3",
                    "opinions": [{"id": 301, "type": "020lead"}],
                }],
                "next": None,
            }
        if step and step.startswith("treatment."):
            return {"count": 0, "results": [], "next": None}
        raise AssertionError("unexpected search step %r" % step)

    def get_cluster(self, cluster_id, record_id=None, step="identity.cluster"):
        return {
            "id": int(cluster_id),
            "case_name": "Smith v. Jones",
            "case_name_short": "Smith",
            "case_name_full": "Smith v. Jones",
            "date_filed": "2024-01-01",
            "court": "scotus",
            "citation_count": 1,
            "absolute_url": "/opinion/100/smith-v-jones/",
            "citations": [{"volume": 1, "reporter": "U.S.", "page": 2, "type": 1}],
            "sub_opinions": [{"id": 200, "type": "020lead"}],
        }

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        if step and step.startswith("identity."):
            return "Smith and Jones are both named in this opinion."
        return super().text_for_opinion(opinion_ref, record_id=record_id, step=step)


class ExpireAfterFirstPage:
    def __init__(self):
        self.calls = 0

    def expired(self):
        self.calls += 1
        return self.calls > 1


def self_test_treatment_partial_resume():
    path = "/tmp/s2-treatment-resume-self-test.jsonl"
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
    journal = Journal(path, "selftest")
    source = {"record_id": "resume-case", "title": "Resume v. Case", "court_level": "scotus"}
    record = empty_record_shell("resume-case", source, "selftest")
    record["status"] = "under_review"
    record["identity"]["sibling_ids"] = [200]
    record["progeny"]["complete_query"] = "cites:(200)"
    first_page = {"results": [{"caseName": "A", "cluster_id": 1, "opinions": []}], "next": "page-2"}
    second_page = {"results": [{"caseName": "B", "cluster_id": 2, "opinions": []}], "next": None}
    client = TreatmentResumeClient({"first": first_page, "page-2": second_page})
    changed = run_treatment(record, source, client, journal, ResumeState([]), ExpireAfterFirstPage())
    assert changed
    assert client.search_calls == ["treatment.lane1_negative.search"]
    assert client.url_calls == []
    partial = ResumeState(journal.rows()).lane_status("resume-case", "treatment", "lane1_negative")
    assert partial["status"] == "partial" and partial["cursor"] == "page-2", partial

    resumed_record = empty_record_shell("resume-case", source, "selftest")
    resumed_record["status"] = "under_review"
    resumed_record["identity"]["sibling_ids"] = [200]
    resumed_record["progeny"]["complete_query"] = "cites:(200)"
    resume_client = TreatmentResumeClient({"first": first_page, "page-2": second_page})
    run_treatment(resumed_record, source, resume_client, journal, ResumeState(journal.rows()), ExpireAfterFirstPage())
    assert resume_client.url_calls and resume_client.url_calls[0] == "page-2"
    assert "treatment.lane1_negative.search" not in resume_client.search_calls


def self_test_treatment_lane_query_shapes_and_cap_cursor():
    path = "/tmp/s2-treatment-query-shape-self-test.jsonl"
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
    source = {"record_id": "query-case", "title": "Query v. Case", "court_level": "scotus"}
    record = empty_record_shell("query-case", source, "selftest")
    record["status"] = "under_review"
    record["identity"]["sibling_ids"] = [200]
    record["progeny"]["complete_query"] = "cites:(200)"

    lane_queries = {}
    for lane, _cap in TREATMENT_LANES:
        query, params = lane_query(record, lane)
        lane_queries[lane] = query
        assert "filed_after:" not in query
        assert "filed_after:" not in params["q"]
    lane3_query, lane3_params = lane_query(record, "lane3_recency")
    assert lane3_query == record["progeny"]["complete_query"]
    assert lane3_params["q"] == record["progeny"]["complete_query"]
    assert lane3_params["filed_after"] == recency_window_start()
    assert lane_queries["lane2_top_cited"] == lane_queries["lane3_recency"]

    journal = Journal(path, "selftest")
    client = TreatmentCapCursorClient()
    resume = ResumeState([
        {"record_id": "query-case", "step": "treatment", "lane": "lane1_negative", "status": "complete"},
        {"record_id": "query-case", "step": "treatment", "lane": "lane3_recency", "status": "complete"},
    ])
    assert run_treatment(record, source, client, journal, resume, SessionTimer(None))
    assert [call["step"] for call in client.search_calls] == ["treatment.lane2_top_cited.search"]
    expected_cursor = client.build_url("search", client.search_calls[0]["params"])
    derivation = record["treatment"]["derivation"]["lane2_top_cited"]
    assert derivation["cap_hit"] is True
    assert derivation["audit_needed"] is True
    assert derivation["final_cursor"] == expected_cursor
    lane = ResumeState(journal.rows()).lane_status("query-case", "treatment", "lane2_top_cited")
    assert lane["cap_hit"] is True and lane["cursor"] == expected_cursor


def self_test_rerun_lane_reset_scope():
    tmp = tempfile.mkdtemp(prefix="s2-rerun-lane-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        manifest_data = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": iso_now(),
            "records": [
                {
                    "record_id": "rerun-case",
                    "record_id_status": "resolved",
                    "source": "content/cases",
                    "stub": False,
                    "title": "Rerun v. Case",
                    "court_level": "scotus",
                    "status": "under_review",
                    "lane_status": {
                        "identity": "complete",
                        "citations": "complete",
                        "pinpoints": "complete",
                        "progeny": "complete",
                        "treatment": {
                            "lane1_negative": {
                                "status": "complete",
                                "cursor": "lane1-cursor",
                                "reviewed": 17,
                                "proposed": 1,
                                "cap_hit": False,
                            },
                            "lane2_top_cited": {"status": "complete", "cursor": None, "cap_hit": True, "reviewed": 25},
                            "lane3_recency": {
                                "status": "complete",
                                "cursor": "lane3-cursor",
                                "reviewed": 42,
                                "proposed": 2,
                                "cap_hit": True,
                            },
                        },
                        "provenance": "pending",
                    },
                    "counts": {},
                },
                {
                    "record_id": "untouched-case",
                    "record_id_status": "resolved",
                    "source": "content/cases",
                    "stub": False,
                    "title": "Untouched v. Case",
                    "court_level": "scotus",
                    "status": "under_review",
                    "lane_status": default_lane_status(),
                    "counts": {},
                },
            ],
        }
        write_json(paths.manifest, manifest_data)
        manifest = ManifestStore(paths.manifest)
        non_target_before = {
            lane: json.dumps(
                manifest.by_record_id["rerun-case"]["lane_status"]["treatment"][lane],
                sort_keys=False,
            )
            for lane in ("lane1_negative", "lane3_recency")
        }

        source = manifest.by_record_id["rerun-case"]
        record = empty_record_shell("rerun-case", source, "selftest")
        record["status"] = "under_review"
        record["identity"]["sibling_ids"] = [222]
        record["progeny"]["complete_query"] = "cites:(222)"
        record["treatment"]["derivation"] = {
            "lane1_negative": {"query": "lane1", "final_cursor": "lane1-cursor"},
            "lane2_top_cited": {"query": "lane2", "final_cursor": None, "cap_hit": True},
            "lane3_recency": {"query": "lane3", "final_cursor": "lane3-cursor"},
        }
        write_case_record(paths, record)

        untouched = empty_record_shell("untouched-case", manifest.by_record_id["untouched-case"], "selftest")
        untouched["status"] = "under_review"
        untouched["treatment"]["derivation"] = {"lane2_top_cited": {"query": "untouched"}}
        write_case_record(paths, untouched)
        untouched_path = os.path.join(paths.cases, "untouched-case.json")
        with open(untouched_path, encoding="utf-8") as f:
            untouched_before = f.read()

        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        selected = reset_record_lanes_for_rerun(paths, manifest, journal, ["lane2_top_cited"], identifiers=["rerun-case"])
        assert [row["record_id"] for row in selected] == ["rerun-case"]
        reset_record = load_case_record(paths, "rerun-case")
        assert "lane2_top_cited" not in reset_record["treatment"]["derivation"]
        assert reset_record["treatment"]["derivation"]["lane1_negative"]["final_cursor"] == "lane1-cursor"
        assert reset_record["treatment"]["derivation"]["lane3_recency"]["final_cursor"] == "lane3-cursor"
        assert manifest.by_record_id["rerun-case"]["lane_status"]["treatment"]["lane2_top_cited"] == {"status": "pending", "cursor": None}
        assert manifest.by_record_id["rerun-case"]["lane_status"]["treatment"]["lane1_negative"]["cursor"] == "lane1-cursor"
        with open(untouched_path, encoding="utf-8") as f:
            assert f.read() == untouched_before
        rows = journal.rows()
        assert any(row.get("step") == "adjudication" and row.get("findings") == LANE_RERUN_FINDINGS for row in rows)
        assert not ResumeState(manifest.resume_rows() + rows).lane_complete("rerun-case", "treatment", "lane2_top_cited")

        client = LaneOnlyTreatmentClient()
        resume = lane_scoped_resume(manifest.resume_rows() + rows, "rerun-case", ["lane2_top_cited"])
        assert run_treatment(reset_record, source, client, journal, resume, SessionTimer(None))
        assert [call["step"] for call in client.search_calls] == ["treatment.lane2_top_cited.search"]
        assert reset_record["treatment"]["derivation"]["lane1_negative"]["final_cursor"] == "lane1-cursor"
        assert reset_record["treatment"]["derivation"]["lane3_recency"]["final_cursor"] == "lane3-cursor"
        skip_rows = {
            row.get("lane"): row
            for row in journal.rows()
            if row.get("step") == "treatment" and row.get("skipped")
        }
        assert skip_rows["lane1_negative"]["cursor"] == "lane1-cursor"
        assert skip_rows["lane1_negative"]["reviewed"] == 17
        assert skip_rows["lane1_negative"]["cap_hit"] is False
        assert skip_rows["lane3_recency"]["cursor"] == "lane3-cursor"
        assert skip_rows["lane3_recency"]["reviewed"] == 42
        assert skip_rows["lane3_recency"]["cap_hit"] is True
        current_resume = ResumeState(manifest.resume_rows() + journal.rows())
        manifest.update("rerun-case", reset_record, counts={"cl_calls": 0}, final_record_id="rerun-case", resume_state=current_resume)
        for lane, before in non_target_before.items():
            after = manifest.by_record_id["rerun-case"]["lane_status"]["treatment"][lane]
            assert json.dumps(after, sort_keys=False) == before, (lane, before, after)
    finally:
        shutil.rmtree(tmp)


class SnippetTriageClient:
    def __init__(self, hits):
        self.hits = hits
        self.search_calls = []
        self.read_count = 0

    def search(self, params, cache=True, record_id=None, step=None):
        self.search_calls.append({"params": dict(params), "step": step})
        return {"count": len(self.hits), "results": self.hits, "next": None}

    def opinion_ref(self, opinion_id, source_array, context=None):
        return {"opinion_id": int(opinion_id), "source_array": source_array, "context": context or {}}

    def text_for_opinion(self, opinion_ref, record_id=None, step="opinion_text"):
        self.read_count += 1
        return "Target v. Case was overruled for this self-test."


def snippet_triage_hit(cluster_id, opinion_id, snippet=None, court_id="cal"):
    opinion = {"id": opinion_id, "type": "020lead"}
    if snippet is not None:
        opinion["snippet"] = snippet
    return {
        "caseName": "Citing %s" % cluster_id,
        "cluster_id": cluster_id,
        "citation": ["999 Test 1"],
        "court_id": court_id,
        "opinions": [opinion],
        "sibling_ids": [opinion_id],
    }


def self_test_treatment_snippet_triage():
    path = "/tmp/s2-snippet-triage-self-test.jsonl"
    try:
        os.unlink(path)
    except FileNotFoundError:
        pass
    journal = Journal(path, "selftest")
    source = {
        "record_id": "triage-case",
        "title": "Target v. Case",
        "court_level": "state",
        "state": "California",
    }
    record = empty_record_shell("triage-case", source, "selftest")
    record["status"] = "under_review"
    record["identity"].update({
        "case_name": "Target v. Case",
        "case_name_full": "Target v. Case",
        "case_name_short": "Target",
        "court_level": "state",
        "state": "California",
        "sibling_ids": [200],
    })
    record["citations"]["display"] = "1 Cal. 2d 3"
    record["citations"]["all"] = [{"cite": "1 Cal. 2d 3", "volume": 1, "reporter": "Cal. 2d", "page": 3}]
    record["progeny"]["complete_query"] = "cites:(200)"
    far_words = " ".join("filler%s" % i for i in range(SNIPPET_PROXIMITY_WORDS + 2))
    hits = [
        snippet_triage_hit(1, 101, "Target v. Case was overruled by the later decision."),
        snippet_triage_hit(2, 102, "The later court abrogated 1 Cal. 2d 3 in part."),
        snippet_triage_hit(3, 103, "We overrule the older line of cases without naming that authority.", court_id="cal"),
        snippet_triage_hit(4, 104, None),
        snippet_triage_hit(5, 105, "Target v. Case appears here as a string cite only."),
        snippet_triage_hit(6, 106, "overruled %s Target v. Case" % far_words),
    ]
    client = SnippetTriageClient(hits)
    resume = ResumeState([
        {"record_id": "triage-case", "step": "treatment", "lane": "lane2_top_cited", "status": "complete"},
        {"record_id": "triage-case", "step": "treatment", "lane": "lane3_recency", "status": "complete"},
    ])
    assert run_treatment(record, source, client, journal, resume, SessionTimer(None))
    assert client.read_count == 4, client.read_count
    assert client.search_calls[0]["step"] == "treatment.lane1_negative.search"
    assert client.search_calls[0]["params"]["fields"] == TREATMENT_SNIPPET_SEARCH_FIELDS
    assert "opinions" in client.search_calls[0]["params"]["fields"].split(",")
    rows = [row for row in journal.rows() if row.get("step") == "treatment.triage"]
    assert len(rows) == 6, rows
    assert len([row for row in rows if row.get("decision") == "read"]) == 4, rows
    assert len([row for row in rows if row.get("decision") == "snippet-classified"]) == 2, rows
    reasons = {row.get("reason") for row in rows}
    assert "negative_keyword_near_target" in reasons
    assert "binding_ambiguous_negative_keyword" in reasons
    assert "missing_snippet" in reasons
    assert "no_negative_keyword_in_snippet" in reasons
    assert "negative_keyword_not_near_target" in reasons
    derivation = record["treatment"]["derivation"]["lane1_negative"]
    assert derivation["triage_mode"] == "snippet-first"
    assert derivation["triage_journaled"] == 6
    assert derivation["triage_read"] == 4
    assert derivation["triage_snippet_classified"] == 2


def self_test_transport_timeout_retry_pending():
    tmp = tempfile.mkdtemp(prefix="s2-timeout-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        source = {
            "record_id": "timeout-case",
            "title": "Smith v. Jones",
            "expected_citation": "1 U.S. 2",
            "court_level": "scotus",
            "year": 2024,
            "legacy_treatment_status": "good",
            "legacy_treatment_as_of": "2026-06-30",
            "counts": {},
        }
        precedence = {"court_classes": {"scotus": {"reporters": {"U.S.": 1}}}}
        migration = {
            "mappings": {
                "good": {
                    "field_i_validity": "good_law",
                    "requires_point_overrides": False,
                    "requires_edge": False,
                    "varies_by_point": False,
                }
            }
        }
        client = TimeoutDuringTreatmentClient(paths, journal)
        record = process_page_record(source, client, paths, precedence, migration, journal, ResumeState([]), "selftest", SessionTimer(None))
        assert not record.get("_ingest_interrupted"), record.get("_ingest_interrupted")
        assert os.path.exists(os.path.join(paths.cases, "timeout-case.json"))
        assert len(client.urlopen_calls) == 4, client.urlopen_calls
        assert all(call["timeout"] == URL_TIMEOUT_SECONDS for call in client.urlopen_calls)
        assert client.retry_sleeps == list(FETCH_RETRY_DELAYS), client.retry_sleeps
        assert client.counting_rate.waits == 4 and client.counting_rate.completed == 4
        assert client.counting_hourly.waits == 4
        assert client.budget.session_calls == 4
        assert "treatment.lane2_top_cited.search" in client.search_steps

        rows = journal.rows()
        fetch_rows = [
            row for row in rows
            if row.get("step") == "treatment.lane1_negative.hit_text" and row.get("status") == "fetch_failed"
        ]
        assert fetch_rows and fetch_rows[-1]["attempts"] == 4, fetch_rows
        lane = ResumeState(rows).lane_status("timeout-case", "treatment", "lane1_negative")
        assert lane["status"] == "partial", lane
        assert lane["retry_pending"] is True and lane["fetch_failed"] is True, lane
        assert lane["note"] == "fetch_failed", lane

        write_json(paths.manifest, {
            "schema_version": SCHEMA_VERSION,
            "generated_at": iso_now(),
            "records": [dict(source, lane_status=default_lane_status())],
        })
        manifest = ManifestStore(paths.manifest)
        manifest.update("timeout-case", record, counts={"cl_calls": client.budget.session_calls}, resume_state=ResumeState(rows))
        lane_status = manifest.data["records"][0]["lane_status"]["treatment"]["lane1_negative"]
        assert lane_status["status"] == "partial", lane_status
        assert lane_status["retry_pending"] is True and lane_status["note"] == "fetch_failed", lane_status
    finally:
        shutil.rmtree(tmp)


def self_test_opinion_cluster_id_rejected():
    client = SelfTestClient(LakePaths("/tmp", "/tmp"), Journal("/tmp/s2-opinion-self-test.jsonl", "selftest"))
    result = {"cluster_id": 999, "opinions": [{"cluster_id": 999, "type": "020lead"}], "sibling_ids": []}
    assert opinion_refs_from_search_result(client, result) == []
    assert pick_lead_ref(client, {"sub_opinions": []}, result) is None
    try:
        extract_opinion_id({"cluster_id": 999}, "search.opinions[]")
    except ValueError:
        pass
    else:
        raise AssertionError("cluster_id-only opinion object was accepted")


def self_test_migration_round_trip():
    migration = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_treatment-migration.json"))
    source = {
        "record_id": "terry-v-ohio",
        "title": "Terry v. Ohio",
        "court_level": "scotus",
        "date_decided": "1968-06-10",
        "legacy_treatment_status": "good",
        "legacy_treatment_as_of": "2026-06-30",
    }
    record = empty_record_shell("terry-v-ohio", source, "selftest")
    record["status"] = "verified"
    changed = seed_treatment_from_migration(record, source, migration)
    assert changed
    assert record["status"] == "under_review"
    assert record["treatment"]["field_i_validity"] == "good_law"
    assert record["treatment"]["field_i_validity"] != "unverified"
    round_trip = json.loads(json.dumps(record))
    assert round_trip["treatment"]["field_i_validity"] == "good_law"
    verified_candidate = json.loads(json.dumps(record))
    verified_candidate["status"] = "verified"
    verified_candidate["identity"]["identity_method"] = "citation+party-text"
    verified_candidate["identity"]["cluster_id"] = 1
    verified_candidate["identity"]["lead_opinion_id"] = 2
    verified_candidate["identity"]["party_name_in_text"] = True
    verified_candidate["identity"]["expected_citation_found"] = True
    assert verified_candidate["treatment"]["field_i_validity"] != "unverified"


def self_test_failclosed_treatment_seed_guard():
    migration = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_treatment-migration.json"))
    source = {
        "record_id": "failclosed-seed-case",
        "title": "Failclosed Seed Case",
        "court_level": "other",
        "date_decided": "1765-11-02",
        "legacy_treatment_status": "good",
        "legacy_treatment_as_of": "2026-06-30",
    }
    for status in sorted(FAIL_CLOSED_STATUSES):
        record = empty_record_shell(source["record_id"], source, "selftest")
        record["status"] = status
        changed = seed_treatment_from_migration(record, source, migration)
        assert changed is False
        assert record["status"] == status
        assert record["treatment"]["field_i_validity"] == "unverified"

    preseeded = empty_record_shell("preseeded-failclosed", {"record_id": "preseeded-failclosed", "title": "Preseeded"}, "selftest")
    preseeded["status"] = "not_found"
    changed = seed_preseeded_treatment(preseeded, {"field_i_validity": "good_law"})
    assert changed is False
    assert preseeded["status"] == "not_found"
    assert preseeded["treatment"]["field_i_validity"] == "unverified"


def self_test_preseeded_new_schema_treatment():
    migration = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_treatment-migration.json"))
    expected = {
        "New York v. Belton": "caution",
        "United States v. Smith (2024)": "good_law",
    }
    outcomes = []
    for case_name, field_i in expected.items():
        page_path = os.path.join(os.getcwd(), "content", "cases", case_name + ".md")
        page_treatment = legacy_treatment_from_page(page_path)
        assert "status" not in page_treatment
        assert page_treatment["field_i_validity"] == field_i
        assert page_treatment["varies_by_point"] is True
        assert page_treatment["point_overrides"]
        source = {
            "record_id": case_name,
            "title": case_name,
            "page_path": page_path,
        }
        record = empty_record_shell(case_name, source, "selftest")
        changed = seed_treatment_from_migration(record, source, migration)
        assert changed
        assert record["status"] == "under_review"
        assert record["identity"].get("reason_code") is None
        assert record["treatment"]["field_i_validity"] == field_i
        assert record["treatment"]["as_of_content"] == page_treatment["as_of_content"]
        assert record["treatment"]["as_of_treatment"] == page_treatment["as_of_treatment"]
        assert record["treatment"]["point_overrides"] == page_treatment["point_overrides"]
        assert PRESEEDED_TREATMENT_PROVENANCE in record["provenance"]["warnings"]
        blocked_record = empty_record_shell(case_name, source, "selftest")
        blocked_record["status"] = "blocked"
        blocked_record["identity"]["reason_code"] = "treatment_migration_unmapped"
        assert seed_treatment_from_migration(blocked_record, source, migration) is False
        assert blocked_record["status"] == "blocked"
        assert blocked_record["identity"].get("reason_code") == "treatment_migration_unmapped"
        assert blocked_record["treatment"]["field_i_validity"] == "unverified"
        outcomes.append("%s=%s/%s/%s override(s)" % (
            case_name,
            record["treatment"]["field_i_validity"],
            record["status"],
            len(record["treatment"]["point_overrides"]),
        ))

    tmp = tempfile.mkdtemp(prefix="s2-preseed-selftest-")
    try:
        neither_path = os.path.join(tmp, "Neither v. Key.md")
        with open(neither_path, "w", encoding="utf-8") as f:
            f.write("---\ntitle: \"Neither v. Key\"\ntreatment:\n  note: \"missing legacy status and Field-I\"\n---\n")
        neither_source = {
            "record_id": "Neither v. Key",
            "title": "Neither v. Key",
            "page_path": neither_path,
        }
        neither_record = empty_record_shell("Neither v. Key", neither_source, "selftest")
        assert seed_treatment_from_migration(neither_record, neither_source, migration)
        assert neither_record["status"] == "blocked"
        assert neither_record["identity"]["reason_code"] == "treatment_migration_unmapped"

        unverified_path = os.path.join(tmp, "Unverified v. Key.md")
        with open(unverified_path, "w", encoding="utf-8") as f:
            f.write("---\ntitle: \"Unverified v. Key\"\ntreatment:\n  field_i_validity: unverified\n---\n")
        unverified_source = {
            "record_id": "Unverified v. Key",
            "title": "Unverified v. Key",
            "page_path": unverified_path,
        }
        unverified_record = empty_record_shell("Unverified v. Key", unverified_source, "selftest")
        assert seed_treatment_from_migration(unverified_record, unverified_source, migration)
        assert unverified_record["status"] == "blocked"
        assert unverified_record["identity"]["reason_code"] == "treatment_migration_unmapped"
    finally:
        shutil.rmtree(tmp)
    outcomes.append("neither-key=blocked")
    outcomes.append("unverified-field-i=blocked")
    print("preseeded treatment self-test: " + "; ".join(outcomes))


def self_test_repair_failclosed_treatment():
    tmp = tempfile.mkdtemp(prefix="s2-failclosed-treatment-repair-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        for record_id in FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS:
            record = empty_record_shell(record_id, {"record_id": record_id, "title": record_id, "court_level": "other"}, "selftest")
            record["status"] = "not_found"
            record["treatment"]["field_i_validity"] = "good_law"
            write_case_record(paths, record)
        repaired = repair_failclosed_treatment(paths, journal)
        assert repaired == list(FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS), repaired
        for record_id in FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS:
            record = load_case_record(paths, record_id)
            assert record["status"] == "not_found"
            assert record["treatment"]["field_i_validity"] == "unverified"
            assert FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE in record["provenance"]["warnings"]
            assert record["provenance"]["field_provenance"]["treatment.field_i_validity"]["src"] == FAIL_CLOSED_TREATMENT_REPAIR_PROVENANCE
        rows = journal.rows()
        assert len(rows) == len(FAIL_CLOSED_TREATMENT_REPAIR_RECORD_IDS), rows
        assert all(row.get("action") == "repair-failclosed-treatment" for row in rows)
        assert repair_failclosed_treatment(paths, journal) == []
    finally:
        shutil.rmtree(tmp)


def migration_ref_record(record_id, cluster_id=None, cite=None):
    record = empty_record_shell(record_id, {"record_id": record_id, "title": record_id, "court_level": "scotus"}, "selftest")
    record["status"] = "under_review"
    if cluster_id is not None:
        record["identity"]["cluster_id"] = cluster_id
    if cite:
        record["citations"]["official"] = {"cite": cite, "source": "selftest"}
        record["citations"]["display"] = cite
        record["citations"]["all"] = [{"cite": cite, "source": "selftest"}]
    return record


def migration_repair_fixture_mapping():
    return {
        "mappings": {
            "limited": {"edge_field_ii": ["limited"]},
            "overruled": {"edge_field_ii": ["overruled"]},
        }
    }


def lint13_validate_fixture_record(path, record):
    lint_dir = os.path.join(os.getcwd(), "scripts", "lint")
    if lint_dir not in sys.path:
        sys.path.insert(0, lint_dir)
    lint13_schema = __import__("lint13_schema")
    schema = lint13_schema.load_json(lint13_schema.SCHEMA_PATH)
    return lint13_schema.validate_record(path, record, schema)


def self_test_repair_real_belton_smith_fixture():
    tmp = tempfile.mkdtemp(prefix="s2-belton-smith-repair-selftest-")
    target_ids = ["New York v. Belton", "United States v. Smith (2024)"]
    support_ids = target_ids + ["Arizona v. Gant", "Chatrie v. United States", "united-states-v-chatrie--10881683"]
    legacy_override_by = {
        "New York v. Belton": ("[[Arizona v. Gant]]", "556 U.S. 332"),
        "United States v. Smith (2024)": ("[[Chatrie v. United States]]", "609 U.S. ___ (2026)"),
    }
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        os.makedirs(paths.points, exist_ok=True)
        shutil.copyfile(os.path.join(os.getcwd(), "_overhaul2", "lake", "_schema.json"), paths.schema)
        shutil.copyfile(os.path.join(os.getcwd(), "_overhaul2", "points", "s2-binding.yaml"), paths.s2_binding)

        real_manifest = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_manifest.json"))
        real_rows = {
            row.get("record_id"): row
            for row in real_manifest.get("records") or []
            if isinstance(row, dict) and row.get("record_id") in support_ids
        }
        for record_id in support_ids:
            source_path = os.path.join(os.getcwd(), "_overhaul2", "lake", "cases", record_id + ".json")
            record = read_json(source_path)
            if record_id in legacy_override_by:
                by, by_cite = legacy_override_by[record_id]
                override = record["treatment"]["point_overrides"][0]
                override["by"] = by
                override["by_cite"] = by_cite
                override["field_ii"] = "limited"
            write_json(os.path.join(paths.cases, record_id + ".json"), record)
        write_json(paths.manifest, {
            "schema_version": SCHEMA_VERSION,
            "generated_at": iso_now(),
            "records": [real_rows[record_id] for record_id in support_ids if record_id in real_rows],
        })

        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        migration = read_json(os.path.join(os.getcwd(), "_overhaul2", "lake", "_treatment-migration.json"))
        repaired = repair_migration_refs(paths, journal, migration)
        assert repaired == target_ids, repaired

        schema = read_lake_schema(paths)
        binding_statuses = load_s2_binding_statuses(paths, schema)
        limited_field_ii = migration_primary_field_ii(migration, "limited")
        lint_findings = []
        status_report = []
        for record_id in target_ids:
            record = load_case_record(paths, record_id)
            lint_findings.extend(lint13_validate_fixture_record(record_id + ".json", record))
            override = record["treatment"]["point_overrides"][0]
            assert set(override) == set(POINT_OVERRIDE_SCHEMA_KEYS), override
            assert set(override["by"][0]) == set(CONTROLLING_CASE_SCHEMA_KEYS), override["by"][0]
            assert "field_ii" not in override and "by_cite" not in override
            assert override["s3_binding_status"] == binding_statuses[override["point"]]
            status_report.append("%s:%s" % (record_id, override["s3_binding_status"]))
        belton = load_case_record(paths, "New York v. Belton")["treatment"]["point_overrides"][0]
        assert belton["by"][0]["field_ii"] == limited_field_ii
        smith = load_case_record(paths, "United States v. Smith (2024)")["treatment"]["point_overrides"][0]
        assert smith["by"][0]["name"] == "Chatrie v. United States"
        assert smith["by"][0]["cluster_id"] == 10881683
        assert smith["by"][0]["cite"] == "609 U.S. ___ (2026)"
        rows = journal.rows()
        dedupe_rows = [row for row in rows if row.get("action") == "s6-dedupe-pointer"]
        assert any(row.get("passed_over_record_id") == "united-states-v-chatrie--10881683" for row in dedupe_rows), dedupe_rows
        assert lint_findings == [], [finding.get("message") for finding in lint_findings]
        print(
            "migration repair acceptance fixture: repaired=%s; lint13_findings=%d; dedupe_pointers=%d; statuses=%s"
            % (", ".join(repaired), len(lint_findings), len(dedupe_rows), ", ".join(status_report))
        )
    finally:
        shutil.rmtree(tmp)


def self_test_repair_migration_refs():
    duplicate_page_errors = []
    duplicate_page = {
        "duplicate v. case": [
            {"record_id": "Duplicate v. Case", "lookup_class": "page", "cluster_id": 1, "cite": "1 U.S. 1"},
            {"record_id": "Duplicate v. Case Again", "lookup_class": "page", "cluster_id": 2, "cite": "2 U.S. 2"},
        ]
    }
    assert resolve_controlling_case("Duplicate v. Case", duplicate_page, duplicate_page_errors, "Target", "selftest") is None
    assert "page" in duplicate_page_errors[0]

    tmp = tempfile.mkdtemp(prefix="s2-migration-ref-repair-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        controller = migration_ref_record("Controller v. Case", cluster_id=12345, cite="1 U.S. 1")
        write_case_record(paths, controller)
        chatrie = migration_ref_record("United States v. Chatrie", cluster_id=777)
        chatrie["identity"]["docket"] = "19-1304"
        write_case_record(paths, chatrie)
        target = migration_ref_record("Target v. Case", cluster_id=999, cite="9 U.S. 9")
        target["treatment"]["point_overrides"] = [
            {
                "point": "point-a",
                "point_label": "Point A",
                "field_i_validity": "caution",
                "field_ii": "",
                "as_of_treatment": "2026-07-06",
                "s3_binding_status": "provisional",
                "by": "[[Controller v. Case]]",
                "by_cite": "fallback cite",
                "scope_note": "stringified by fixture",
            },
            {
                "point": "point-chatrie",
                "point_label": "Point Chatrie",
                "field_i_validity": "caution",
                "field_ii": "",
                "as_of_treatment": "2026-07-06",
                "s3_binding_status": "provisional",
                "by": "[[United States v. Chatrie]]",
                "by_cite": "unverified fallback cite",
                "scope_note": "name+docket fixture without official cite",
            },
        ]
        target["treatment"]["edges"] = [{
            "citing_case": {
                "name": "Controller v. Case",
                "cluster_id": None,
                "cite": None,
                "field_ii": "limited",
            },
            "field_ii": "limited",
            "field_iii": "mentioned",
            "point": None,
            "proposed": True,
            "journal_ref": "migration:limited",
        }]
        write_case_record(paths, target)
        repaired = repair_migration_refs(paths, journal, migration_repair_fixture_mapping())
        assert repaired == ["Target v. Case"], repaired
        repaired_target = load_case_record(paths, "Target v. Case")
        override = repaired_target["treatment"]["point_overrides"][0]
        assert set(override) == set(POINT_OVERRIDE_SCHEMA_KEYS)
        assert "field_ii" not in override and "by_cite" not in override
        assert override["by"] == [{
            "name": "Controller v. Case",
            "cluster_id": 12345,
            "cite": "1 U.S. 1",
            "field_ii": "limited",
        }]
        chatrie_override = repaired_target["treatment"]["point_overrides"][1]
        assert set(chatrie_override) == set(POINT_OVERRIDE_SCHEMA_KEYS)
        assert chatrie_override["by"] == [{
            "name": "United States v. Chatrie",
            "cluster_id": 777,
            "cite": "unverified fallback cite",
            "field_ii": "limited",
        }]
        assert repaired_target["treatment"]["edges"][0]["citing_case"]["cluster_id"] == 12345
        assert repaired_target["treatment"]["edges"][0]["citing_case"]["cite"] == "1 U.S. 1"
        assert MIGRATION_REF_REPAIR_PROVENANCE in repaired_target["provenance"]["warnings"]
        assert CONTROLLING_CASE_NO_OFFICIAL_CITE_WARNING in repaired_target["provenance"]["warnings"]
        assert any(row.get("action") == "repair-migration-refs" and row.get("findings") == MIGRATION_REF_REPAIR_FINDINGS for row in journal.rows())
    finally:
        shutil.rmtree(tmp)

    self_test_repair_real_belton_smith_fixture()

    tmp = tempfile.mkdtemp(prefix="s2-migration-ref-fail-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        bad = migration_ref_record("Bad Target v. Case", cluster_id=999, cite="9 U.S. 9")
        bad["treatment"]["point_overrides"] = [{
            "point": "point-b",
            "point_label": "Point B",
            "field_i_validity": "caution",
            "as_of_treatment": "2026-07-06",
            "s3_binding_status": "provisional",
            "by": "[[Missing v. Case]]",
            "scope_note": "unresolvable fixture",
        }]
        write_case_record(paths, bad)
        bad_path = os.path.join(paths.cases, "Bad Target v. Case.json")
        with open(bad_path, encoding="utf-8") as f:
            before = f.read()
        try:
            repair_migration_refs(paths, journal, migration_repair_fixture_mapping())
        except SystemExit as exc:
            assert "Missing v. Case" in str(exc)
        else:
            raise AssertionError("unresolvable migration ref did not fail closed")
        with open(bad_path, encoding="utf-8") as f:
            assert f.read() == before
        assert journal.rows() == []
    finally:
        shutil.rmtree(tmp)

    tmp = tempfile.mkdtemp(prefix="s2-migration-ref-byte-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        well = migration_ref_record("Well Formed v. Case", cluster_id=222, cite="2 U.S. 2")
        well["treatment"]["point_overrides"] = [{
            "point": "point-c",
            "point_label": "Point C",
            "field_i_validity": "caution",
            "as_of_treatment": "2026-07-06",
            "s3_binding_status": "provisional",
            "by": [{
                "name": "Already v. Resolved",
                "cluster_id": 333,
                "cite": "3 U.S. 3",
                "field_ii": "limited",
            }],
            "scope_note": "already well formed",
        }]
        write_case_record(paths, well)
        well_path = os.path.join(paths.cases, "Well Formed v. Case.json")
        with open(well_path, encoding="utf-8") as f:
            before = f.read()
        repaired = repair_migration_refs(paths, journal, migration_repair_fixture_mapping())
        assert repaired == []
        with open(well_path, encoding="utf-8") as f:
            assert f.read() == before
        assert journal.rows() == []
    finally:
        shutil.rmtree(tmp)


def self_test_status_preserve():
    record = empty_record_shell("status-case", {"record_id": "status-case", "title": "Status v. Case"}, "selftest")
    record["status"] = "fabrication_suspected"
    precedence = {"court_classes": {"other": {"reporters": {}}}}
    cluster = {"citations": [{"volume": 1, "reporter": "Unknown", "page": 1, "type": 1}]}
    journal = Journal("/tmp/s2-status-self-test.jsonl", "selftest")
    apply_citations(record, cluster, precedence, journal)
    assert record["status"] == "fabrication_suspected"


def r15_flip_fixture_record(record_id, status, method="citation+party-text", stub=False,
                            expected=True, party=True, cluster_id=100):
    source = {
        "record_id": record_id,
        "title": record_id,
        "caption": record_id,
        "court_level": "scotus",
        "stub": stub,
    }
    record = empty_record_shell(record_id, source, "selftest")
    record["stub"] = stub
    record["status"] = status
    record["identity"].update({
        "case_name": record_id.replace("--123", "").replace("--u12345678", ""),
        "case_name_short": record_id.split(" v. ")[0],
        "case_name_full": record_id.replace("--123", "").replace("--u12345678", ""),
        "court": "U.S. Supreme Court",
        "court_id": "scotus",
        "court_level": "scotus",
        "date_decided": "2020-01-02",
        "year": 2020,
        "docket": "19-1",
        "cluster_id": cluster_id,
        "lead_opinion_id": cluster_id + 1,
        "sibling_ids": [cluster_id + 1],
        "absolute_url": "/opinion/%s/%s/" % (cluster_id, slugify(record_id)),
        "identity_method": method,
        "expected_citation_found": expected,
        "party_name_in_text": party,
        "canonical_name_match": True,
        "reason_code": "awaiting_r15_structural_gates" if method == "citation+party-text" else None,
    })
    cite = {
        "cite": "590 U.S. %s" % (cluster_id % 100),
        "volume": "590",
        "reporter": "U.S.",
        "page": str(cluster_id % 100),
        "type": 1,
        "selected_official": True,
        "source": "selftest",
    }
    record["citations"].update({
        "official": cite,
        "parallel": [],
        "vendor_neutral": [],
        "all": [cite],
        "display": cite["cite"],
        "official_selection": {"court_class": "scotus", "selected": cite["cite"], "reason": "selftest"},
    })
    record["treatment"].update({
        "field_i_validity": "good_law" if status == "under_review" and method == "citation+party-text" else "unverified",
        "as_of_content": "2020-01-02",
        "as_of_treatment": "2026-07-06",
        "composite_basis": "principal-holding" if status == "under_review" and method == "citation+party-text" else "unverified",
        "composite_basis_ref": "selftest" if status == "under_review" and method == "citation+party-text" else None,
    })
    record["progeny"].update({
        "complete_query": "cites:(%s)" % (cluster_id + 1),
        "indexed_citing_opinions": 0,
        "count_source": "search",
        "per_sibling": [{"opinion_id": cluster_id + 1, "count": 0, "count_source": "search"}],
        "citation_count": 0,
    })
    if method in ("pending", "not_found", "blocked"):
        record["identity"]["cluster_id"] = None
        record["identity"]["lead_opinion_id"] = None
        record["identity"]["sibling_ids"] = []
        record["identity"]["absolute_url"] = None
    if method == "not_found":
        record["identity"]["expected_citation_found"] = False
        record["identity"]["party_name_in_text"] = False
    if method == "frontier-identity":
        record["identity"]["lead_opinion_id"] = None
        record["identity"]["sibling_ids"] = []
        record["identity"]["party_name_in_text"] = False
        record["treatment"]["scope_note"] = "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
        record["progeny"]["complete_query"] = None
        record["progeny"]["indexed_citing_opinions"] = None
        record["progeny"]["count_source"] = None
        record["progeny"]["per_sibling"] = []
        record["progeny"]["citation_count"] = None
    return record


def self_test_flip_verified():
    tmp = tempfile.mkdtemp(prefix="s2-r15-flip-selftest-")
    try:
        paths = LakePaths(tmp, os.path.join(tmp, "pool"))
        paths.ensure()
        fixtures = [
            r15_flip_fixture_record("Eligible v. One", "under_review", cluster_id=101),
            r15_flip_fixture_record("Eligible v. Two", "under_review", cluster_id=102),
            r15_flip_fixture_record("Name Docket v. Case", "under_review", method="name+docket", expected=True, party=False, cluster_id=201),
            r15_flip_fixture_record("Pending v. Case", "under_review", method="pending", expected=False, party=False, cluster_id=301),
            r15_flip_fixture_record("frontier-case--123", "verified_identity", method="frontier-identity", stub=True, expected=True, party=False, cluster_id=123),
            r15_flip_fixture_record("Fabricated v. Case", "fabrication_suspected", method="fabrication-check", expected=True, party=False, cluster_id=401),
            r15_flip_fixture_record("Not Found v. Case", "not_found", method="not_found", expected=False, party=False, cluster_id=501),
        ]
        for record in fixtures:
            write_case_record(paths, record)
        write_json(paths.manifest, {
            "schema_version": "s2.manifest.v1",
            "generated_at": iso_now(),
            "records": [
                {
                    "record_id": record["record_id"],
                    "record_id_status": "resolved",
                    "source": "content/cases" if not record.get("stub") else "s6-frontier",
                    "stub": record.get("stub", False),
                    "title": record["record_id"],
                    "status": record["status"],
                    "lane_status": default_lane_status(),
                    "counts": {},
                }
                for record in fixtures
            ],
            "counts": {},
        })
        manifest = ManifestStore(paths.manifest)
        journal = Journal(os.path.join(tmp, "journal.jsonl"), "selftest")
        protected_counts = {
            "under_review:name+docket": 1,
            "under_review:pending": 1,
            "verified_identity": 1,
            "fabrication_suspected": 1,
            "not_found": 1,
        }
        try:
            flip_verified_records(paths, manifest, journal, expected_count=3, expected_untouched_counts=protected_counts)
        except SystemExit as exc:
            assert "expected_count=3 actual_count=2" in str(exc)
        else:
            raise AssertionError("r15 flip count mismatch did not fail closed")
        assert journal.rows() == []

        protected_ids = ["Name Docket v. Case", "Pending v. Case", "frontier-case--123", "Fabricated v. Case", "Not Found v. Case"]
        before = {}
        for record_id in protected_ids:
            with open(os.path.join(paths.cases, record_id + ".json"), encoding="utf-8") as f:
                before[record_id] = f.read()

        result = flip_verified_records(paths, manifest, journal, expected_count=2, expected_untouched_counts=protected_counts)
        assert result["flipped"] == ["Eligible v. One", "Eligible v. Two"], result
        assert result["protected_counts"] == protected_counts
        assert result["status_counts"] == {
            "fabrication_suspected": 1,
            "not_found": 1,
            "under_review": 2,
            "verified": 2,
            "verified_identity": 1,
        }
        for record_id in result["flipped"]:
            record = load_case_record(paths, record_id)
            assert record["status"] == "verified"
            assert record["identity"]["reason_code"] is None
        for record_id in protected_ids:
            with open(os.path.join(paths.cases, record_id + ".json"), encoding="utf-8") as f:
                assert f.read() == before[record_id]
        rows = journal.rows()
        flip_rows = [row for row in rows if row.get("step") == "r15-flip"]
        assert len(flip_rows) == 2, rows
        for row in flip_rows:
            assert row["gates"] == R15_FLIP_GATES
            assert row["adjudicated_by"] == READJUDICATION_ADJUDICATOR
            assert set(["step", "record_id", "gates", "adjudicated_by", "ts", "run"]) <= set(row)
        saved_manifest = read_json(paths.manifest)
        assert saved_manifest["counts"]["status_counts"] == result["status_counts"]
    finally:
        shutil.rmtree(tmp)


def run_self_tests():
    self_test_record_ids()
    self_test_precedence()
    self_test_binding_filters()
    self_test_token_bucket()
    self_test_collective_global_limiter()
    self_test_journal_resume()
    self_test_identity_primary_prefilter_plan()
    self_test_identity_caption_and_cite_fixtures()
    self_test_identity_fallback_ladder()
    self_test_terminal_not_found_skip_and_warning_dedupe()
    self_test_verified_off_cl_schema()
    self_test_off_cl_elevation_path()
    self_test_frontier_stub_record_id_bounds_and_resume()
    self_test_s6_candidate_intake()
    self_test_bounded_progeny()
    self_test_outbound_edges_from_search_result()
    self_test_identity_skip_preserves_record()
    self_test_budget_interruption_resume()
    self_test_readjudicate_reset_reruns_fail_closed_record()
    self_test_treatment_partial_resume()
    self_test_treatment_lane_query_shapes_and_cap_cursor()
    self_test_rerun_lane_reset_scope()
    self_test_treatment_snippet_triage()
    self_test_transport_timeout_retry_pending()
    self_test_opinion_cluster_id_rejected()
    self_test_migration_round_trip()
    self_test_failclosed_treatment_seed_guard()
    self_test_preseeded_new_schema_treatment()
    self_test_repair_failclosed_treatment()
    self_test_repair_migration_refs()
    self_test_status_preserve()
    self_test_flip_verified()
    print("self-test passed")


def parse_args(argv):
    parser = argparse.ArgumentParser(description="S2 CourtListener authority ingest builder")
    parser.add_argument("--session-minutes", type=float, default=None, help="cleanly stop at a checkpoint after N minutes")
    parser.add_argument("--resume", dest="resume", action="store_true", default=True, help="consult journal and skip complete work (default)")
    parser.add_argument("--no-resume", dest="resume", action="store_false", help="ignore existing journal state")
    parser.add_argument("--smoke", help="run one manifest record by record_id/title slug; targets ~30-70 calls/case and enforces <=80 calls")
    parser.add_argument("--self-test", action="store_true", help="run offline unit checks and exit")
    parser.add_argument("--run-id", help="explicit fresh build id override; default is the stable id persisted in _manifest.json")
    parser.add_argument("--readjudicate", action="append", default=[], help="reset identity and downstream resume state for a record_id/title; repeatable")
    parser.add_argument("--readjudicate-file", action="append", default=[], help="file of record IDs/titles to readjudicate, one per line or JSON list")
    parser.add_argument("--rerun-lane", action="append", default=[], help="reset and rerun a treatment lane by name; repeatable")
    parser.add_argument("--records", action="append", default=[], help="record_id/title filter for --rerun-lane; repeatable")
    parser.add_argument("--repair-migration-refs", action="store_true", help="offline one-shot repair for migration/pre-seed controlling-case refs")
    parser.add_argument("--repair-failclosed-treatment", action="store_true", help="offline one-shot repair for fail-closed treatment validity seeded by F-S2-31")
    parser.add_argument("--flip-verified", action="store_true", help="offline R15 adjudicated flip from under_review to verified after structural gates")
    parser.add_argument("--add-candidates", help="offline append an S6 candidate queue JSONL as pending frontier stubs")
    parser.add_argument("--elevate-off-cl", help="elevate a terminal not_found record using an orchestrator-prepared off-CL adjudication file")
    parser.add_argument("--adjudication", help="JSON adjudication file required by --elevate-off-cl")
    parser.add_argument("--token-path", default=TOKEN_PATH, help="CourtListener token path")
    parser.add_argument("--rate-per-minute", type=int, default=14, help="token bucket refill and capacity")
    parser.add_argument("--hourly-limit", type=int, default=900, help="hourly guard ceiling")
    parser.add_argument("--max-calls", type=int, default=None, help="optional session call cap")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    if args.self_test:
        run_self_tests()
        return 0
    run_ingest(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
