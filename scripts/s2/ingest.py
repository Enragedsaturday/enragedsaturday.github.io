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
import sqlite3  # noqa: F401 - stdlib dependency reserved for the R13 loader path.
import sys
import time
import urllib.error
import urllib.parse
import urllib.request


API_BASE = "https://www.courtlistener.com/api/rest/v4"
DEFAULT_CSSI_LAKE_ROOT = "/Users/johngalt/cssi-lake"
TOKEN_PATH = os.path.expanduser("~/.config/cssi/cl-token")
CONSUMER_IDENTITY = "S2-BUILDER-AUTHORING"
SCHEMA_VERSION = "s2.v1"

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
    cite = re.sub(r"\s*\((?:17|18|19|20)\d{2}\)\s*$", "", cite)
    cite = cite.replace("\u00a0", " ")
    cite = re.sub(r"\s+", " ", cite).strip()
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
    level = (identity.get("court_level") or "").lower()
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


def extract_id(value):
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        for key in ("id", "opinion_id", "cluster_id"):
            if key in value:
                return extract_id(value[key])
    text = str(value).rstrip("/")
    m = re.search(r"(\d+)$", text)
    return int(m.group(1)) if m else None


def first_party_terms(case_name):
    text = re.sub(r"\s+\((?:17|18|19|20)\d{2}\)\s*$", "", case_name or "")
    parts = re.split(r"\s+v\.?\s+", text, maxsplit=1, flags=re.I)
    if len(parts) != 2:
        return [text.strip()] if text.strip() else []
    terms = []
    for part in parts:
        words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]+", part) if len(w) > 2]
        if words:
            terms.append(words[-1].lower())
    return terms


def canonical_caption_match(input_name, canonical_name):
    return slugify(input_name) == slugify(canonical_name)


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
    def __init__(self, rate_per_minute=14, capacity=14, start_time=None):
        self.rate_per_minute = float(rate_per_minute)
        self.capacity = float(capacity)
        self.tokens = float(capacity)
        self.updated_at = float(time.time() if start_time is None else start_time)

    @property
    def refill_per_second(self):
        return self.rate_per_minute / 60.0

    def _refill(self, now):
        elapsed = max(0.0, float(now) - self.updated_at)
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_per_second)
        self.updated_at = float(now)

    def consume_at(self, now, amount=1):
        self._refill(now)
        amount = float(amount)
        if self.tokens >= amount:
            self.tokens -= amount
            return 0.0
        missing = amount - self.tokens
        wait = missing / self.refill_per_second
        self.tokens = 0.0
        self.updated_at = float(now) + wait
        return wait

    def wait(self):
        wait = self.consume_at(time.time())
        if wait > 0:
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

    def record_call(self):
        self.session_calls += 1
        self.cumulative_calls += 1
        if self.max_calls is not None and self.session_calls > self.max_calls:
            raise RuntimeError("call budget exceeded: %s > %s" % (self.session_calls, self.max_calls))

    def snapshot(self, estimated_remaining=None):
        return {
            "calls_this_session": self.session_calls,
            "cumulative_calls_observed": self.cumulative_calls,
            "remaining_estimate": estimated_remaining,
            "max_calls_this_session": self.max_calls,
        }


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
        self.lanes = {}
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
                }
            else:
                self.steps[(record_id, step)] = status

    def step_complete(self, record_id, step):
        return self.steps.get((record_id, step)) == "complete"

    def lane_status(self, record_id, step, lane):
        return self.lanes.get((record_id, step, lane), {"status": "pending", "cursor": None})

    def lane_complete(self, record_id, step, lane):
        return self.lane_status(record_id, step, lane).get("status") == "complete"


class LakePaths:
    def __init__(self, repo_root, pool_root):
        self.repo_root = repo_root
        self.lake = os.path.join(repo_root, "_overhaul2", "lake")
        self.cases = os.path.join(self.lake, "cases")
        self.manifest = os.path.join(self.lake, "_manifest.json")
        self.precedence = os.path.join(self.lake, "_reporter-precedence.json")
        self.pool = pool_root
        self.http_cache = os.path.join(pool_root, "cache", "http")
        self.progeny = os.path.join(pool_root, "progeny")
        self.text = os.path.join(pool_root, "text")
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
        self.analyze_rate = TokenBucket(rate_per_minute=60, capacity=60)
        self.hourly = hourly
        self.run_id = run_id
        self.call_log = os.path.join(paths.logs, "cl-calls.log")

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

        attempt = 0
        while True:
            attempt += 1
            self.rate.wait()
            self.hourly.wait()
            self.budget.record_call()
            req = urllib.request.Request(url)
            req.add_header("Authorization", "Token %s" % self.token)
            req.add_header("Accept", "application/json")
            req.add_header("User-Agent", "cssi-s2-builder/1.0")
            try:
                with urllib.request.urlopen(req, timeout=45) as resp:
                    body = resp.read().decode("utf-8")
                    status = getattr(resp, "status", 200)
                self.log_call("GET", url, status=status)
                data = json.loads(body)
                if cache:
                    with open(cache_file, "w", encoding="utf-8") as f:
                        json.dump(data, f)
                self.journal.append(
                    record_id=record_id,
                    step=step or "http",
                    status="network",
                    url_sha1=sha1_text(url),
                    http_status=status,
                    budget=self.budget.snapshot(),
                )
                return data
            except urllib.error.HTTPError as exc:
                self.log_call("GET", url, status=exc.code)
                if exc.code in (429, 500, 502, 503, 504) and attempt < 6:
                    time.sleep(min(120, (2 ** attempt) + random.uniform(0.25, 1.5)))
                    continue
                raise

    def post_json_url(self, url, payload, record_id=None, step=None, rate_bucket=None):
        body = json.dumps(payload).encode("utf-8")
        attempt = 0
        while True:
            attempt += 1
            (rate_bucket or self.rate).wait()
            self.hourly.wait()
            self.budget.record_call()
            req = urllib.request.Request(url, data=body, method="POST")
            req.add_header("Authorization", "Token %s" % self.token)
            req.add_header("Accept", "application/json")
            req.add_header("Content-Type", "application/json")
            req.add_header("User-Agent", "cssi-s2-builder/1.0")
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    response_body = resp.read().decode("utf-8")
                    status = getattr(resp, "status", 200)
                self.log_call("POST", url, status=status)
                data = json.loads(response_body)
                self.journal.append(
                    record_id=record_id,
                    step=step or "post",
                    status="network",
                    url_sha1=sha1_text(url),
                    http_status=status,
                    budget=self.budget.snapshot(),
                )
                return data
            except urllib.error.HTTPError as exc:
                self.log_call("POST", url, status=exc.code)
                if exc.code in (429, 500, 502, 503, 504) and attempt < 6:
                    time.sleep(min(120, (2 ** attempt) + random.uniform(0.25, 1.5)))
                    continue
                raise

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
        opinion_id = extract_id(item)
        if opinion_id:
            refs.append(client.opinion_ref(opinion_id, "cluster.sub_opinions[]", {"cluster_id": cluster.get("id")}))
    return refs


def opinion_refs_from_search_result(client, result):
    refs = []
    for opinion_id in result.get("sibling_ids") or []:
        if extract_id(opinion_id):
            refs.append(client.opinion_ref(extract_id(opinion_id), "search.sibling_ids[]", {"cluster_id": result.get("cluster_id")}))
    for opinion in result.get("opinions") or []:
        opinion_id = extract_id(opinion)
        if opinion_id:
            refs.append(client.opinion_ref(opinion_id, "search.opinions[].id", {"cluster_id": result.get("cluster_id")}))
    return refs


def pick_lead_ref(client, cluster, search_result=None):
    search_opinions = []
    if search_result:
        search_opinions = search_result.get("opinions") or []
        for opinion in search_opinions:
            otype = str(opinion.get("type") or "").lower()
            if otype in LEAD_OPINION_TYPES:
                return client.opinion_ref(extract_id(opinion), "search.opinions[].id", {"lead_type": otype})
    for item in cluster.get("sub_opinions") or []:
        if isinstance(item, dict):
            otype = str(item.get("type") or "").lower()
            if otype in LEAD_OPINION_TYPES:
                return client.opinion_ref(extract_id(item), "cluster.sub_opinions[]", {"lead_type": otype})
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
    level = (record.get("court_level") or "").lower()
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


def citation_matches_expected(cluster, expected):
    expected = normalize_cite(expected)
    if not expected:
        return False
    for citation in cluster.get("citations") or []:
        if normalize_cite(citation) == expected:
            return True
    return False


def text_names_parties(case_name, text):
    if not text:
        return False
    lowered = text.lower()
    terms = first_party_terms(case_name)
    return bool(terms) and all(term in lowered for term in terms)


def base_field_provenance(src, verifier=CONSUMER_IDENTITY):
    return {"src": src, "at": iso_now(), "verifier": verifier}


def empty_record_shell(record_id, source_record, build_run):
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
        journal.append(record_id=record_id, step="identity", status="complete", skipped=True)
        return None, None, None

    params = identity_search_params(record)
    search = client.search(params, cache=True, record_id=record_id, step="identity.search")
    results = search_results(search)
    expected_cite = record.get("expected_citation") or record.get("citation") or ""
    candidates = []
    for result in results[:10]:
        cluster_id = result.get("cluster_id") or result.get("cluster")
        if not cluster_id:
            continue
        cluster = client.get_cluster(cluster_id, record_id=record_id, step="identity.cluster")
        score = 0
        if citation_matches_expected(cluster, expected_cite):
            score += 100
        if record.get("year") and str(cluster.get("date_filed") or "").startswith(str(record["year"])):
            score += 10
        candidates.append((score, result, cluster))
    candidates.sort(key=lambda item: item[0], reverse=True)
    selected = candidates[0] if candidates else None
    journal.append(
        record_id=record_id,
        step="identity",
        status="partial" if selected else "complete",
        candidate_count=len(candidates),
        selected_cluster_id=selected[2].get("id") if selected else None,
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
    party_found = text_names_parties(source_record.get("title") or source_record.get("caption") or record_id, lead_text)
    canonical = cluster.get("case_name") or search_result.get("caseName") or search_result.get("case_name")
    canonical_match = canonical_caption_match(source_record.get("title") or source_record.get("caption") or record_id, canonical or "")
    sibling_ids = []
    for ref in opinion_refs_from_search_result(client, search_result):
        sibling_ids.append(int(ref["opinion_id"]))
    for ref in opinion_refs_from_cluster(client, cluster):
        sibling_ids.append(int(ref["opinion_id"]))
    sibling_ids = sorted(set(sibling_ids))
    identity = record_json["identity"]
    identity.update({
        "case_name": canonical,
        "case_name_short": cluster.get("case_name_short"),
        "case_name_full": cluster.get("case_name_full"),
        "court": source_record.get("court") or cluster.get("court") or search_result.get("court_citation_string"),
        "court_id": search_result.get("court_id") or cluster.get("court"),
        "court_level": source_record.get("court_level") or identity.get("court_level"),
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
    if not canonical_match:
        record_json["status"] = "fabrication_suspected"
        identity["identity_method"] = "fabrication-check"
        identity["reason_code"] = "canonical_name_mismatch"
        warnings.append("input caption does not match CL canonical caption")
    elif expected_found and party_found:
        record_json["status"] = "verified"
        identity["identity_method"] = "citation+party-text"
    elif source_record.get("docket"):
        record_json["status"] = "under_review"
        identity["identity_method"] = "name+docket"
        identity["reason_code"] = "recent_or_no_official_cite"
    else:
        record_json["status"] = "under_review"
        identity["identity_method"] = "pending"
        identity["reason_code"] = "two_key_not_satisfied"
        warnings.append("two-key identity check did not fully satisfy citation plus party text")
    record_json["provenance"]["cl_source"] = cluster.get("source")
    record_json["provenance"]["field_provenance"]["identity"] = base_field_provenance("CourtListener search + clusters + lead opinion text")
    journal.append(record_id=record_id, step="identity", status="complete", final_status=record_json["status"])
    return lead_ref, lead_text


def apply_citations(record_json, cluster, precedence, journal):
    record_id = record_json["record_id"]
    court_class = record_json["identity"].get("court_level") or "other"
    record_json["citations"] = classify_citations(cluster.get("citations") or [], court_class, precedence)
    if record_json["citations"]["official"] is None:
        record_json["status"] = "under_review"
        record_json["provenance"]["warnings"].append("official cite selection failed closed: %s" % record_json["citations"]["official_selection"]["reason"])
    journal.append(record_id=record_id, step="citations", status="complete", official=record_json["citations"]["display"])


def apply_pinpoints(record_json, source_record, lead_text, journal):
    record_id = record_json["record_id"]
    record_json["pinpoints"] = harvest_pinpoints(source_record.get("page_path"), lead_text)
    record_json["provenance"]["field_provenance"]["pinpoints"] = base_field_provenance("content page quote harvest + lead opinion text")
    journal.append(record_id=record_id, step="pinpoints", status="complete", count=len(record_json["pinpoints"]))


def fetch_progeny(record_json, source_record, client, journal, resume):
    record_id = source_record["record_id"]
    if resume.step_complete(record_id, "progeny"):
        journal.append(record_id=record_id, step="progeny", status="complete", skipped=True)
        return
    sibling_ids = record_json["identity"].get("sibling_ids") or []
    query = complete_cites_query(sibling_ids)
    if not query:
        journal.append(record_id=record_id, step="progeny", status="complete", skipped=True, reason="no_sibling_ids")
        return
    first = client.search({"type": "o", "q": query, "order_by": "score desc", "page_size": 100}, cache=True, record_id=record_id, step="progeny.search")
    count = search_count(first)
    cache_path = os.path.join(client.paths.progeny, "%s.jsonl" % slugify(record_id))
    written = 0
    data = first
    url = next_url(data)
    with open(cache_path, "w", encoding="utf-8") as f:
        while True:
            for result in search_results(data):
                f.write(json.dumps(result, sort_keys=True) + "\n")
                written += 1
            if not url:
                break
            data = client.get_json_url(url, cache=True, record_id=record_id, step="progeny.page")
            url = next_url(data)
    per_sibling = []
    for sibling_id in sibling_ids:
        per = client.search({"type": "o", "q": "cites:(%s)" % sibling_id, "page_size": 1}, cache=True, record_id=record_id, step="progeny.per_sibling")
        per_sibling.append({
            "opinion_id": int(sibling_id),
            "count": search_count(per) or 0,
            "count_source": "search",
        })
    record_json["progeny"] = {
        "complete_query": query,
        "indexed_citing_opinions": count,
        "count_source": "search",
        "per_sibling": per_sibling,
        "citation_count": None,
        "cache_path": cache_path,
    }
    journal.append(record_id=record_id, step="progeny", status="complete", indexed_citing_opinions=count, rows_cached=written)


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
        return bounded, {"type": "o", "q": bounded, "stat_Published": "on", "order_by": "dateFiled desc", "page_size": 100}
    if lane_name == "lane2_top_cited":
        return query, {"type": "o", "q": query, "order_by": "citeCount desc", "page_size": 25}
    if lane_name == "lane3_recency":
        filed_after = recency_window_start()
        recent = "%s AND filed_after:%s" % (query, filed_after)
        return recent, {"type": "o", "q": recent, "order_by": "dateFiled desc", "filed_after": filed_after, "page_size": 100}
    raise ValueError("unknown lane %s" % lane_name)


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


def run_treatment(record_json, source_record, client, journal, resume, session):
    record_id = source_record["record_id"]
    if record_json.get("stub"):
        return
    lanes = [
        ("lane1_negative", 200),
        ("lane2_top_cited", 25),
        ("lane3_recency", 200),
    ]
    derivation = record_json["treatment"].setdefault("derivation", {})
    for lane_name, cap in lanes:
        if session.expired():
            return
        lane_state = resume.lane_status(record_id, "treatment", lane_name)
        if lane_state.get("status") == "complete":
            journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", skipped=True)
            continue
        query, params = lane_query(record_json, lane_name)
        if not query:
            journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", reason="no_progeny_query")
            continue
        reviewed = 0
        proposed = []
        cursor = lane_state.get("cursor")
        data = client.get_json_url(cursor, cache=False, record_id=record_id, step="treatment.%s.resume" % lane_name) if cursor else client.search(params, cache=False, record_id=record_id, step="treatment.%s.search" % lane_name)
        while True:
            for result in search_results(data):
                if reviewed >= cap:
                    break
                reviewed += 1
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
                journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", cap_hit=True, reviewed=reviewed, proposed=len(proposed))
                break
            url = next_url(data)
            if not url:
                journal.append(record_id=record_id, step="treatment", lane=lane_name, status="complete", reviewed=reviewed, proposed=len(proposed))
                break
            data = client.get_json_url(url, cache=False, record_id=record_id, step="treatment.%s.page" % lane_name)
        derivation[lane_name] = {
            "query": query,
            "reviewed": reviewed,
            "cap": cap,
            "proposed_negative_events": len(proposed),
        }
        record_json["treatment"]["edges"].extend(proposed)
    if all(resume.lane_complete(record_id, "treatment", lane) for lane, _cap in lanes):
        journal.append(record_id=record_id, step="treatment", status="complete")


def seed_treatment_from_migration(record_json, source_record):
    record_json["treatment"].update({
        "field_i_validity": "unverified",
        "as_of_content": None,
        "as_of_treatment": None,
        "composite_basis": "unverified",
        "composite_basis_ref": source_record.get("title") or source_record.get("caption") or record_json["record_id"],
        "varies_by_point": False,
        "scope_note": "Treatment seeded as unverified until migration and three-lane derivation complete.",
    })
    record_json["provenance"]["field_provenance"]["treatment.field_i_validity"] = base_field_provenance("S2 migration gate pending")


def write_case_record(paths, record_json):
    record_json["provenance"]["date_modified"] = iso_now()
    os.makedirs(paths.cases, exist_ok=True)
    record_id = record_json["record_id"]
    write_json(os.path.join(paths.cases, record_id + ".json"), record_json)


class ManifestStore:
    def __init__(self, path):
        self.path = path
        self.data = read_json(path)
        self.by_record_id = {row["record_id"]: row for row in self.data.get("records", [])}

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

    def update(self, old_record_id, record_json, counts=None, final_record_id=None):
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

    def save(self):
        self.data["generated_at"] = self.data.get("generated_at")
        write_json(self.path, self.data)


def process_page_record(source_record, client, paths, precedence, journal, resume, build_run, session):
    record_id = page_record_id(source_record["record_id"])
    record_json = empty_record_shell(record_id, source_record, build_run)
    search_result, cluster, alternates = resolve_identity(source_record, client, journal, resume, build_run)
    lead_text = ""
    if cluster:
        lead_ref, lead_text = apply_identity(record_json, source_record, search_result, cluster, alternates, client, journal)
        apply_citations(record_json, cluster, precedence, journal)
        apply_pinpoints(record_json, source_record, lead_text, journal)
        record_json["progeny"]["citation_count"] = cluster.get("citation_count")
        seed_treatment_from_migration(record_json, source_record)
        if not session.expired():
            fetch_progeny(record_json, source_record, client, journal, resume)
        if not session.expired() and record_json["status"] in ("verified", "under_review"):
            run_treatment(record_json, source_record, client, journal, resume, session)
    else:
        record_json["status"] = "not_found"
        record_json["identity"]["identity_method"] = "not_found"
        record_json["identity"]["reason_code"] = "no_candidate_cluster"
        record_json["provenance"]["warnings"].append("not found in CL identity search; not proof of fabrication")
        journal.append(record_id=record_id, step="identity", status="complete", final_status="not_found")
    record_json["provenance"]["field_provenance"]["point_overrides"] = base_field_provenance("S2 treatment derivation proposed only")
    write_case_record(paths, record_json)
    return record_json


def process_frontier_record(source_record, client, paths, precedence, journal, resume, build_run):
    unresolved_id = source_record["record_id"]
    shell = empty_record_shell(unresolved_id, source_record, build_run)
    if resume.step_complete(unresolved_id, "identity"):
        journal.append(record_id=unresolved_id, step="identity", status="complete", skipped=True)
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
    shell["record_id"] = final_id
    shell["stub"] = True
    shell["status"] = "verified_identity" if canonical_caption_match(source_record.get("caption"), canonical) else "fabrication_suspected"
    shell["identity"].update({
        "case_name": canonical,
        "case_name_short": cluster.get("case_name_short"),
        "case_name_full": cluster.get("case_name_full"),
        "cluster_id": extract_id(cluster.get("id") or result.get("cluster_id")),
        "absolute_url": cluster.get("absolute_url") or result.get("absolute_url"),
        "identity_method": "frontier-identity",
        "expected_citation_found": bool(cluster.get("citations")),
        "party_name_in_text": False,
        "canonical_name_match": canonical_caption_match(source_record.get("caption"), canonical),
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
    token = read_token(args.token_path)
    fingerprint = sha256_text(token)[:12]
    run_id = args.run_id or utc_now().strftime("%Y%m%dT%H%M%SZ")
    journal_path = os.path.join(paths.journal, "s2-ingest-%s.jsonl" % run_id)
    journal = Journal(journal_path, run_id)
    resume = ResumeState(journal.rows()) if args.resume else ResumeState([])
    max_calls = 40 if args.smoke else args.max_calls
    budget = CallBudget(max_calls=max_calls)
    client = CourtListenerClient(
        paths=paths,
        token=token,
        token_fingerprint=fingerprint,
        journal=journal,
        budget=budget,
        rate=TokenBucket(rate_per_minute=args.rate_per_minute, capacity=args.rate_per_minute),
        hourly=HourlyGuard(max_per_hour=args.hourly_limit),
        run_id=run_id,
    )
    manifest = ManifestStore(paths.manifest)
    precedence = read_json(paths.precedence)
    session = SessionTimer(args.session_minutes)
    records = manifest.select(args.smoke)
    journal.append(step="budget-checkpoint", status="start", budget=budget.snapshot(estimated_remaining="15-25k total-run envelope"))
    for source_record in records:
        if session.expired():
            break
        old_id = source_record["record_id"]
        if source_record.get("stub"):
            record_json, final_id = process_frontier_record(source_record, client, paths, precedence, journal, resume, run_id)
        else:
            record_json = process_page_record(source_record, client, paths, precedence, journal, resume, run_id, session)
            final_id = record_json["record_id"]
        manifest.update(old_id, record_json, counts={"cl_calls": budget.session_calls}, final_record_id=final_id)
        manifest.save()
        journal.append(record_id=final_id, step="case-checkpoint", status="complete", budget=budget.snapshot())
    journal.append(step="budget-checkpoint", status="end", budget=budget.snapshot(estimated_remaining="review checkpoint required before relaunch"))
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
    assert binding_jurisdiction_filter({"court_level": "coa", "circuit": "4th Cir."}) == "AND court_id:(scotus OR ca4)"
    assert binding_jurisdiction_filter({"court_level": "district", "circuit": "9"}) == "AND court_id:(scotus OR ca9)"
    state = binding_jurisdiction_filter({"court_level": "state", "state": "California"})
    assert state == "AND court_id:(scotus OR cal OR calctapp OR calappdeptsuper)", state


def self_test_token_bucket():
    bucket = TokenBucket(rate_per_minute=14, capacity=14, start_time=0)
    waits = [bucket.consume_at(0) for _ in range(14)]
    assert waits == [0.0] * 14
    wait = bucket.consume_at(0)
    assert 4.28 < wait < 4.29, wait
    assert 4.28 < bucket.consume_at(wait) < 4.29


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


def run_self_tests():
    self_test_record_ids()
    self_test_precedence()
    self_test_binding_filters()
    self_test_token_bucket()
    self_test_journal_resume()
    print("self-test passed")


def parse_args(argv):
    parser = argparse.ArgumentParser(description="S2 CourtListener authority ingest builder")
    parser.add_argument("--session-minutes", type=float, default=None, help="cleanly stop at a checkpoint after N minutes")
    parser.add_argument("--resume", dest="resume", action="store_true", default=True, help="consult journal and skip complete work (default)")
    parser.add_argument("--no-resume", dest="resume", action="store_false", help="ignore existing journal state")
    parser.add_argument("--smoke", help="run one manifest record by record_id/title slug; enforces <=40 calls")
    parser.add_argument("--self-test", action="store_true", help="run offline unit checks and exit")
    parser.add_argument("--run-id", help="journal run id; defaults to UTC timestamp")
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
