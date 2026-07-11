# Thread-N escalation: United States v. Lyle — both lenses unread (loop cap 3)

**Status:** ESCALATE (flagged omission per S9 R5 no-regression floor — carried, not lost).

**Case:** United States v. Lyle (2d Cir.) · lead opinion 8415374 · cached text present (119KB, valid opinion XML, Chin, C.J.).

**Symptom:** Thread-N blind re-derivation lanes Lyle[A] and Lyle[B] failed on all 3 sweeps (2026-07-11 00:45–01:11), every attempt AUTH-CLASS ("Reading additional input from stdin…" / pause-#8 surface), while sibling lanes (incl. same-batch Small, Ruckman) succeeded in the same sweeps. Not a bad-text/schema fault — text and lead are valid. Largest payload in the residual set (119KB); likely straddling transient auth blips under conc-6.

**Disposition:** Left unread for the SR-5 reconciliation (2/1218 pairs = 0.16%); reconciler dispositions as candidate/unreadable. A dedicated single-lane retry during a quiet window should clear it; not worth blocking the pipeline. Re-attempt in the P4 residual sweep.
