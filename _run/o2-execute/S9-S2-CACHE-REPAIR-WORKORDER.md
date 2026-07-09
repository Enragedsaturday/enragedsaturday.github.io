# S9 → S2 builder work order — cache re-fetch + Davis re-keys (serial REST token lane)

Staged 2026-07-09 by the orchestrator from S9 findings F-S9-IDS-001/DN-002/DN-003/DN-004 +
the mechanical mis-key sweep (_run/s9/miskey-sweep.jsonl). Execute on the Codex builder lane
(owns the CL REST token; paced; journaled). ~15 calls total.

1. TEXT RE-FETCH for the 7 S7-re-keyed leads (identity live-confirmed by COH-17; pool lacks
   text under the new ids): 9441559 (King) · 9434613 (Thornton) · 11349205 (Chatrie) ·
   11312795 (R.W.) · 4703206 (Gaetjens) · 11346052 (Landor) · 11266325 (Konan).
2. DAVIS PAIR: both records cache stubs (1994: cluster 9148721 lead 9143409, 88B; 2011:
   cluster 7350241 lead 7268220, 154B). Resolve the true merits clusters (512 U.S. 452;
   564 U.S. 229) via citation search; sanctioned re-key + text fetch.
3. FISHER: re-key illinois-v-fisher--5141053 to the true Illinois v. Fisher (540 U.S. 544,
   docket 03-374); fetch text.
4. WYMAN: confirm cluster 108223 identity (claimed Nkansah mismatch); re-key to true Wyman
   (400 U.S. 309) if confirmed; fetch text.
5. RILEY NUANCE: lead 2680439 text exists (82KB) — verify its content is the 2014 merits
   opinion (doctrine lanes reported motions-order content; the case-grain read will also
   report); re-fetch only if confirmed wrong.
6. FLIPPO: verify 1854815 text is the legit per curiam (ancillary-pattern regex hit, likely
   false positive).
After: re-run fragments.py for affected records; re-run affected Thread-N reads; journal.
