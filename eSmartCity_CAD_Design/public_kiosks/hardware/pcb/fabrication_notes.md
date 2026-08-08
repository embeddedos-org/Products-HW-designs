# Public Information Kiosks — Fabrication Notes

## Fabrication

- Build to IPC-6012 Class 2.
- Surface finish: ENIG, conformal coated.
- Base material FR-4 Tg170 or better, UL 94V-0 marked.
- Finished thickness 1.6 mm +/- 10%.
- Solder mask both sides; silkscreen both sides, white on green.
- Electrical test: 100% netlist verification against the supplied netlist.
- No design changes without written approval; report any DFM issue instead.

## Assembly

- Assemble to IPC-A-610 Class 2.
- Lead-free process, SAC305, per J-STD-001.
- Moisture-sensitive devices handled per J-STD-033.
- ESD control per ANSI/ESD S20.20 throughout.

## Status of this design — read before quoting

Generated from `tools/catalog`. **This is not a fabrication release.**

What exists: board outline, layer stack, design rules, and every
board-mounted part placed without courtyard overlap inside the outline.
The BOM, the netlist and the placed footprints reconcile against each other.

What does not exist yet, and is required before fabrication:

- **No pads.** Placed footprints carry body and courtyard outlines only.
  Real IPC-7351 land patterns must be assigned before layout.
- **No routing.** No traces, no vias, no copper pours.
- **No signal nets.** The netlist carries power distribution only; pin-level
  connectivity is not derivable from a bill of materials and has been left
  out rather than invented.
- **No DRC, no Gerbers, no signal integrity or thermal simulation.**
- **Component part numbers and prices are unverified** against any
  distributor. Confirm availability, lifecycle status and pricing before use.
