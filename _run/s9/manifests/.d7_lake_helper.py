#!/usr/bin/env python3
"""D-7 blindness-safe lake lookup: identity + citations ONLY (no treatment/progeny)."""
import json, sys, os, glob

LAKE = '/Users/johngalt/Projects/cssi-quartz/_overhaul2/lake/cases'
TEXT = '/Users/johngalt/cssi-lake/cache/text'
ALLOWED = ('case_name', 'case_name_full', 'court', 'court_id', 'court_level',
           'circuit', 'year', 'date_decided', 'cluster_id', 'lead_opinion_id',
           'sibling_ids')

def lookup(patterns):
    files = glob.glob(f'{LAKE}/*.json')
    out = []
    for pat in patterns:
        hits = [f for f in files if pat.lower() in os.path.basename(f).lower()]
        if not hits:
            out.append({'query': pat, 'lake_hit': False})
            continue
        for f in hits:
            rec = json.load(open(f))
            ident = rec.get('identity') or {}
            safe = {k: ident.get(k) for k in ALLOWED}
            cites = [c.get('cite') for c in (rec.get('citations') or []) if isinstance(c, dict)]
            lead = safe.get('lead_opinion_id')
            sibs = safe.get('sibling_ids') or []
            cached = [oid for oid in ([lead] if lead else []) + [s for s in sibs if s != lead]
                      if oid and os.path.exists(f'{TEXT}/{oid}.txt')]
            out.append({'query': pat, 'lake_hit': True,
                        'record': os.path.basename(f)[:-5], **safe,
                        'citations': cites, 'cached_text_ids': cached})
    print(json.dumps(out))

if __name__ == '__main__':
    lookup(sys.argv[1:])
