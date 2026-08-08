# Satellite Ground Station — Placement and Area Check

> **Result:** FITS

| Metric | Value |
|---|---|
| Components placed | 380 |
| Components unplaced | 0 |
| Assembly-level items excluded | 1 |
| Courtyard area used | 4206.4 mm² |
| Usable board area | 38016.0 mm² |
| Courtyard utilisation | 11.1% |

## Method

Single-sided shelf packing inside the board outline less a 2 mm edge
keep-out. This establishes **area feasibility**, not a layout: it does not
consider routing channels, thermal spacing, connector positions, keep-outs,
or which side a part belongs on. A board that fits here can still be
unroutable.

Courtyard utilisation above roughly 60% on a single side generally means the
design needs both sides of the board, a larger outline, or finer geometry.

