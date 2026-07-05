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


API_BASE = "https://www.courtlistener.com/api/rest/v4"
DEFAULT_CSSI_LAKE_ROOT = "/Users/johngalt/cssi-lake"
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
CONSUMER_IDENTITY = "S2-BUILDER-AUTHORING"
SCHEMA_VERSION = "s2.v1"
URL_TIMEOUT_SECONDS = 60
FETCH_RETRY_DELAYS = (5.0, 15.0, 45.0)
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}
TRAILING_YEAR_PAREN_RE = r"\s*\([^()]*(?:17|18|19|20)\d{2}\)\s*$"
READJUDICATION_FINDINGS = ["F-S2-16", "F-S2-17", "F-S2-18"]
READJUDICATION_ADJUDICATOR = "orchestrator claude-fable-5"
IDENTITY_PRIMARY_CLUSTER_LIMIT = 10
IDENTITY_FALLBACK_CLUSTER_LIMIT = 3
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
    "company": "co",  # Company may contract to co because county contracts to cty.
    "north": "n",  # Directional abbreviation; one-char outputs are retained.
    "south": "s",  # Directional abbreviation; one-char outputs are retained.
    "east": "e",  # Directional abbreviation; one-char outputs are retained.
    "west": "w",  # Directional abbreviation; one-char outputs are retained.
}


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
    return "%s--%s" % (slugify(case_name), int(cluster_id))


def not_found_stub_record_id(row):
    key = normalized_roster_key(row)
    return "%s--u%s" % (slugify(row.get("caption") or row.get("title") or "case"), sha1_text(key)[:8])


def citation_to_string(citation):
    if not citation:
        return ""
    if isinstance(citation, str):
        return citation
    if citation.get("cite"):
        return str(citation["cite"])
    parts = [citation.get("volume"), citation.get("reporter"), citation.get("page")]
    return " ".join(str(p).strip() for p in parts if p not in (None, ""))


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


def first_party_terms(case_name):
    text = strip_trailing_year_parenthetical(case_name)
    parts = re.split(r"\s+v\.?\s+", text, maxsplit=1, flags=re.I)
    if len(parts) != 2:
        return [text.strip()] if text.strip() else []
    terms = []
    for part in parts:
        words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]+", part) if len(w) > 2]
        if words:
            terms.append(words[-1].lower())
    return terms


def caption_token_set(value):
    if not str(value or "").strip():
        return set()
    return {
        CAPTION_TOKEN_CONTRACTIONS.get(token, token)
        for token in slugify(value).split("-")
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


def missing_party_terms(case_name, text):
    terms = first_party_terms(case_name)
    if not terms:
        return []
    lowered = (text or "").lower()
    return [term for term in terms if term not in lowered]


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
        self.cases = os.path.join(self.lake, "cases")
        self.manifest = os.path.join(self.lake, "_manifest.json")
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


def court_search_id(record):
    level = normalize_court_class(record.get("court_level"))
    if level == "scotus":
        return "scotus"
    if level == "coa":
        return parse_circuit(record.get("circuit") or record.get("court"))
    return None


def identity_search_params(record):
    params = {
        "type": "o",
        "case_name": record.get("title") or record.get("caption") or record.get("record_id"),
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


def identity_candidate_evidence(record, result, cluster, expected_cite):
    citation_match = citation_matches_expected(cluster, expected_cite)
    year_match = identity_year_matches(record, result, cluster)
    court_match = identity_court_matches(record, result, cluster)
    return {
        "expected_citation_match": citation_match,
        "year_match": year_match,
        "court_match": court_match,
        "viable": citation_match or (year_match and court_match),
    }


def identity_candidate_score(record, result, cluster, expected_cite):
    evidence = identity_candidate_evidence(record, result, cluster, expected_cite)
    score = 0
    if evidence["expected_citation_match"]:
        score += 100
    if evidence["year_match"]:
        score += 10
    if evidence["court_match"]:
        score += 10
    return score


def identity_viable_candidates(record, candidates, expected_cite):
    return [
        candidate
        for candidate in candidates
        if identity_candidate_evidence(record, candidate[1], candidate[2], expected_cite)["viable"]
    ]


def identity_candidates(record, client, results, expected_cite, record_id, max_clusters=IDENTITY_PRIMARY_CLUSTER_LIMIT):
    candidates = []
    for result in results[:max_clusters]:
        cluster_id = result.get("cluster_id") or result.get("cluster")
        if not cluster_id:
            continue
        cluster = client.get_cluster(cluster_id, record_id=record_id, step="identity.cluster")
        score = identity_candidate_score(record, result, cluster, expected_cite)
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


def set_record_status(record_json, status, reason=None, explicit_adjudication=False):
    current = record_json.get("status")
    if current in FAIL_CLOSED_STATUSES and current != status and not explicit_adjudication:
        if reason:
            record_json["provenance"]["warnings"].append("preserved %s over %s: %s" % (current, status, reason))
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

    params = identity_search_params(record)
    search = client.search(params, cache=True, record_id=record_id, step="identity.search")
    results = search_results(search)
    expected_cite = record.get("expected_citation") or record.get("citation") or ""
    candidates = identity_candidates(record, client, results, expected_cite, record_id)
    selected_rung = "case_name"
    viable_candidates = identity_viable_candidates(record, candidates, expected_cite)
    if not viable_candidates:
        best_candidates = candidates
        best_rung = "case_name" if best_candidates else None
        selected_candidates = []
        for rung, fallback in identity_fallback_params(record, expected_cite):
            fallback_search = client.search(fallback, cache=True, record_id=record_id, step="identity.search.fallback")
            fallback_results = search_results(fallback_search)
            rung_candidates = identity_candidates(
                record,
                client,
                fallback_results,
                expected_cite,
                record_id,
                max_clusters=IDENTITY_FALLBACK_CLUSTER_LIMIT,
            )
            rung_viable = bool(identity_viable_candidates(record, rung_candidates, expected_cite))
            journal.append(
                record_id=record_id,
                step="identity.search.fallback",
                status="complete",
                rung=rung,
                result_count=identity_result_count(fallback_search),
                clusters_fetched=len(rung_candidates),
                viable=rung_viable,
            )
            if rung_candidates and (not best_candidates or rung_candidates[0][0] > best_candidates[0][0]):
                best_candidates = rung_candidates
                best_rung = rung
            if rung_viable:
                results = fallback_results
                selected_candidates = rung_candidates
                selected_rung = rung
                break
        candidates = selected_candidates or best_candidates or []
        selected_rung = selected_rung if selected_candidates else best_rung
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
    warnings = record_json["provenance"]["warnings"]
    if canonical_match and expected_found and party_found:
        set_record_status(record_json, "under_review", "R15 structural gates have not cleared")
        identity["identity_method"] = "citation+party-text"
        identity["reason_code"] = "awaiting_r15_structural_gates"
    elif not canonical_match and expected_found and party_found:
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "citation+party-text"
        identity["reason_code"] = "caption_mismatch_canonical"
        warnings.append("input caption does not match CL canonical caption")
    elif not canonical_match:
        set_record_status(record_json, "fabrication_suspected")
        identity["identity_method"] = "fabrication-check"
        identity["reason_code"] = "canonical_name_mismatch"
        warnings.append("input caption does not match CL canonical caption")
    elif source_record.get("docket"):
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "name+docket"
        identity["reason_code"] = "recent_or_no_official_cite"
    else:
        set_record_status(record_json, "under_review")
        identity["identity_method"] = "pending"
        identity["reason_code"] = "two_key_not_satisfied"
        warnings.append("two-key identity check did not fully satisfy citation plus party text")
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
        record_json["provenance"]["warnings"].append("official cite selection failed closed: %s" % record_json["citations"]["official_selection"]["reason"])
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
        recent = "%s AND filed_after:%s" % (query, filed_after)
        return recent, {
            "type": "o",
            "q": recent,
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
    warning = "treatment %s fetch failed after bounded retries; retry pending" % lane_name
    warnings = record_json["provenance"].setdefault("warnings", [])
    if warning not in warnings:
        warnings.append(warning)
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
        if lane_state.get("status") == "complete":
            journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", skipped=True)
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
                    final_cursor = next_url(data)
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
    warnings = record_json["provenance"]["warnings"]
    if PRESEEDED_TREATMENT_PROVENANCE not in warnings:
        warnings.append(PRESEEDED_TREATMENT_PROVENANCE)
    record_json["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance(PRESEEDED_TREATMENT_PROVENANCE)
    if treatment.get("point_overrides"):
        record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance(PRESEEDED_TREATMENT_PROVENANCE)
    return True


def seed_treatment_from_migration(record_json, source_record, migration):
    if record_json.get("stub"):
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
        record_json["provenance"]["warnings"].append("legacy treatment value lacks migration mapping: %s" % (legacy.get("status") or "<missing>"))
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
        record_json["provenance"]["warnings"].append("legacy treatment %s requires edge metadata; staged for S9 review" % legacy_status)
    record_json["provenance"]["warnings"].append("legacy treatment migrated: %s -> %s" % (legacy_status, field_i))
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
            row.setdefault("lane_status", default_lane_status())
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

    def save(self):
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
                record_json["provenance"]["warnings"].append("identity completion could not be replayed; blocked rather than marking not_found")
            else:
                set_record_status(record_json, "not_found")
                record_json["identity"]["identity_method"] = "not_found"
                record_json["identity"]["reason_code"] = "no_candidate_cluster"
                record_json["provenance"]["warnings"].append("not found in CL identity search; not proof of fabrication")
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
        shell["provenance"]["warnings"].append("frontier identity completion could not be replayed; blocked rather than returning an empty shell")
        write_case_record(paths, shell)
        journal.append(record_id=unresolved_id, step="identity", status="complete", skipped=True, final_record_id=unresolved_id, final_status="blocked")
        return shell, unresolved_id
    search = client.search(identity_search_params(source_record), cache=True, record_id=unresolved_id, step="frontier.identity.search")
    results = search_results(search)
    if not results:
        final_id = not_found_stub_record_id(source_record)
        shell["record_id"] = final_id
        shell["stub"] = True
        shell["status"] = "not_found"
        shell["identity"]["identity_method"] = "not_found"
        shell["identity"]["reason_code"] = "frontier_no_candidate_cluster"
        shell["provenance"]["warnings"].append("frontier not_found requires web/second-source cross-check before fabrication inference")
        write_case_record(paths, shell)
        journal.append(record_id=unresolved_id, step="identity", status="complete", final_record_id=final_id, final_status="not_found")
        return shell, final_id
    result = results[0]
    cluster = client.get_cluster(result.get("cluster_id"), record_id=unresolved_id, step="frontier.identity.cluster")
    canonical = cluster.get("case_name") or result.get("caseName") or source_record.get("caption")
    final_id = cluster_stub_record_id(canonical, cluster.get("id") or result.get("cluster_id"))
    canonical_match = canonical_caption_match_cluster(source_record.get("caption"), cluster, canonical)
    shell["record_id"] = final_id
    shell["stub"] = True
    shell["status"] = "verified_identity" if canonical_match else "fabrication_suspected"
    shell["identity"].update({
        "case_name": canonical,
        "case_name_short": cluster.get("case_name_short"),
        "case_name_full": cluster.get("case_name_full"),
        "cluster_id": extract_id(cluster.get("id") or result.get("cluster_id")),
        "absolute_url": cluster.get("absolute_url") or result.get("absolute_url"),
        "identity_method": "frontier-identity",
        "expected_citation_found": bool(cluster.get("citations")),
        "party_name_in_text": False,
        "canonical_name_match": canonical_match,
    })
    shell["citations"] = classify_citations(cluster.get("citations") or [], source_record.get("court_level") or "state", precedence)
    shell["treatment"]["scope_note"] = "Frontier stub: treatment/progeny intentionally not derived until S6 promotion."
    shell["progeny"]["complete_query"] = None
    shell["provenance"]["field_provenance"]["identity"] = base_field_provenance("CourtListener frontier identity search")
    shell["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance("frontier stub, no treatment")
    shell["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("frontier stub, no treatment")
    shell["provenance"]["field_provenance"]["pinpoints"] = base_field_provenance("frontier stub, no pinpoints")
    write_case_record(paths, shell)
    journal.append(record_id=unresolved_id, step="identity", status="complete", final_record_id=final_id, final_status=shell["status"])
    return shell, final_id


def run_ingest(args):
    repo_root = os.getcwd()
    pool_root = os.environ.get("CSSI_LAKE_ROOT", DEFAULT_CSSI_LAKE_ROOT)
    paths = LakePaths(repo_root, pool_root)
    paths.ensure()
    manifest = ManifestStore(paths.manifest)
    had_build_id = bool(manifest.data.get("build_id"))
    run_id = manifest.ensure_build_id(args.run_id)
    if args.run_id or manifest.normalized or not had_build_id:
        manifest.save()
    journal_path = os.path.join(paths.journal, "s2-ingest-%s.jsonl" % run_id)
    journal = Journal(journal_path, run_id)
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


def identity_fixture_search_result(cluster_id=100, opinion_id=200):
    return {
        "cluster_id": cluster_id,
        "caseName": "fixture",
        "opinions": [{"id": opinion_id, "type": "020lead"}],
        "sibling_ids": [opinion_id],
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
        record = process_page_record(
            exhausted_source,
            not_found_client,
            paths,
            {"court_classes": {}},
            {"mappings": {}},
            not_found_journal,
            ResumeState([]),
            "selftest",
            SessionTimer(None),
        )
        assert record["status"] == "not_found"
        rows = not_found_journal.rows()
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
        assert [rows[index].get("rung") for index in fallback_indexes] == ["q", "citation", "docket_number"]
        assert not_found_indexes and max(fallback_indexes) < not_found_indexes[-1]
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
        assert seed_treatment_from_migration(blocked_record, source, migration)
        assert blocked_record["status"] == "under_review"
        assert blocked_record["identity"].get("reason_code") is None
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


def self_test_status_preserve():
    record = empty_record_shell("status-case", {"record_id": "status-case", "title": "Status v. Case"}, "selftest")
    record["status"] = "fabrication_suspected"
    precedence = {"court_classes": {"other": {"reporters": {}}}}
    cluster = {"citations": [{"volume": 1, "reporter": "Unknown", "page": 1, "type": 1}]}
    journal = Journal("/tmp/s2-status-self-test.jsonl", "selftest")
    apply_citations(record, cluster, precedence, journal)
    assert record["status"] == "fabrication_suspected"


def run_self_tests():
    self_test_record_ids()
    self_test_precedence()
    self_test_binding_filters()
    self_test_token_bucket()
    self_test_collective_global_limiter()
    self_test_journal_resume()
    self_test_identity_caption_and_cite_fixtures()
    self_test_identity_fallback_ladder()
    self_test_bounded_progeny()
    self_test_outbound_edges_from_search_result()
    self_test_identity_skip_preserves_record()
    self_test_budget_interruption_resume()
    self_test_readjudicate_reset_reruns_fail_closed_record()
    self_test_treatment_partial_resume()
    self_test_treatment_snippet_triage()
    self_test_transport_timeout_retry_pending()
    self_test_opinion_cluster_id_rejected()
    self_test_migration_round_trip()
    self_test_preseeded_new_schema_treatment()
    self_test_status_preserve()
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
