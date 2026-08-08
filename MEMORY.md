<!-- generated: eos-ai-scaffold -->
# Memory

Durable context for `eCAD-Hardware-Products` — decisions and constraints that outlive one
session and are not recoverable from the code or the git history.

Write here when a future reader would otherwise repeat an argument that was
already settled, or repeat a mistake that was already made.

## What belongs here

- Decisions and the reason behind them, especially the options rejected.
- Constraints that are not visible in the code — a deadline, a compatibility
  promise, a hardware limitation, an external dependency's behaviour.
- Traps: things that look wrong but are deliberate, and things that look safe
  but break.

## What does not

- Anything derivable by reading the code.
- Anything in the git log.
- Task status — that is [TASKS.md](./TASKS.md).
- Standards — those are [QUALITY.md](./QUALITY.md),
  [TESTING.md](./TESTING.md) and [SECURITY-STANDARDS.md](./SECURITY-STANDARDS.md).

## Decisions

Format: what was chosen, why, and what was rejected. The rejected option is the
valuable half — without it the decision gets re-argued every time someone new
notices the obvious-looking alternative.

| Date | Decision | Reason | Rejected alternative |
|------|----------|--------|----------------------|
| 2026-08-08 | Taxonomy names become product sub-directories inside the division for their category heading; categories with no division get a new one | Matches the structure the repository already uses (`eAerospace_CAD_Design/avionics`), and adding a sub-directory is far more reversible than adding a top-level division | One `*_CAD_Design` division per taxonomy name — rejected at ~350 top-level directories with heavy duplication, since `eAvionics` would restate `eAerospace_CAD_Design/avionics`. User decision, not inferred |
| 2026-08-08 | Product data is generated from `tools/catalog/` rather than hand-authored per directory | At 337 products, hand-authoring invites two defects that survive review: filler that resembles data, and BOM arithmetic that drifts. Costs are computed from a shared component library, so `Extended = Qty x Unit` and the total are right by construction | Hand-authoring each `bom.csv` — rejected on the arithmetic risk alone; the repository already carried three total mismatches and one CSV corruption found on 2026-08-08 |
| 2026-08-08 | `tools/validate_products.py` re-derives BOM arithmetic from the generated CSV instead of trusting the generator | Keeps the checker independent of the thing it checks. This caught a real generator defect (doubled comma in emitted Python) on first run | Having the generator self-verify — rejected because no role approves its own work, and a shared bug would then be invisible |
| 2026-08-08 | Pre-existing contract violations are enumerated in `tools/product_baseline.json` with a reason each, not fixed by loosening rules | Keeps new data held to the full contract while making every legacy deviation visible and attributable | Relaxing the validator until the repository passed — rejected because it would silently license the same defects in new data |
| 2026-08-08 | CAD artefacts are generated from the same catalog entry as the datasheet and BOM, and validated with real tools (`kiutils`, `ezdxf`, OpenSCAD) rather than by inspection | A board file that disagrees with its own datasheet is the defect this is designed to make impossible; the netlist's component list is cross-checked against the BOM for the same reason | Hand-drawing schematics per product — rejected at this scale, and it would reintroduce exactly the drift the generator removes |
| 2026-08-08 | Generated netlists carry component records and power nets only; signal nets are deliberately absent | Pin-level connectivity is not derivable from a bill of materials. An invented signal net would look authoritative and be wrong, which is worse than an acknowledged gap | Emitting plausible signal nets — rejected as fabrication; the omission is stated in each `.net` file header |
| 2026-08-08 | A BOM line carries an allocated designator *range* (`C1-C180`), not a single reference with a quantity | A line reading `C1` qty 180 cannot be built: a board needs 180 distinct designators, and the BOM, netlist and board can never be reconciled without them. 863 of 1637 lines were in this state before the change | Keeping aggregated references and expanding only at layout time — rejected because the BOM is the document people order from, and it was naming parts that did not exist |
| 2026-08-08 | The catalog's `ref` field is a *prefix hint*; numbering is allocated by the generator | Makes duplicate designators impossible by construction rather than merely detected. Two catalog lines may both say `U1`; they come out `U1` and `U2` | Validating for duplicates and failing — rejected as weaker: a check that can be forgotten loses to an invariant that cannot be violated |
| 2026-08-08 | Components carry an `assembly` flag; flagged items are costed in the BOM but excluded from board placement | Enclosures, battery packs, solar panels and the bare PCB are part of the product but are not mounted on the board. Including them made the area check meaningless — most obviously the PCB, placed on top of itself | Placing everything — rejected because it produced 15 false "does not fit" results and hid the 8 real ones |
| 2026-08-08 | Simulations are executed from a temporary copy, not in place | Several hand-authored simulations resolve their plot directory from `__file__` and write PNGs beside themselves. Validation that dirties the working tree is indistinguishable from an edit | Running them in place and tolerating the churn — rejected; a validator must be safe to run on a clean tree |

<!-- Example of the level of detail worth recording:
| 2026-03-14 | Queue writes in-process rather than via Redis | Deploy target has no
network sidecar; measured throughput was sufficient at 4x expected peak |
Redis Streams — rejected on operational cost, not on capability. Revisit if
peak exceeds 8x. |
-->

## Constraints

| Constraint | Source | Consequence if broken |
|------------|--------|-----------------------|
| Manufacturer part numbers and unit costs in `tools/catalog/components.json` are **Assumed**, not verified against any distributor | Authored from domain knowledge on 2026-08-08; no distributor API was called | Quoting or procuring from this data without checking each MPN and price against Mouser/Digi-Key/Octopart. `validate_products.py` proves internal consistency only and makes no claim about the outside world |
| `pytest` is not installed in the current environment, though `run_all_tests.py` invokes it | Observed 2026-08-08: `python3 -m pytest` reports "No module named pytest" | Reporting the suite as passing via `run_all_tests.py` when it was actually run with `python3 -m unittest discover -s tests` |
| CAD validation needs `kiutils`, `ezdxf` and OpenSCAD; simulations need `numpy`, `matplotlib`, `scipy`. See `tools/requirements.txt` | Installed 2026-08-08 to `~/.local`; `apt` was unavailable because sudo needs a password, so OpenSCAD came from an extracted AppImage at `~/.local/share/openscad-appimage` | Missing tools are reported as skips, never as passes — so a green run on a bare machine can silently mean "not checked". Confirm the skip count is zero before trusting a CAD result |
| `eosHealth_CAD_Design/HEALTH-RING/simulation/ppg_biosensor_sim.py` is an **unseeded** Monte Carlo sitting on its own spec limit | Measured 2026-08-08 over 8 runs: HbA1c mean error 0.409%–0.643% against a 0.5% spec; exited non-zero 4 times out of 8 | Treating any single run of it as evidence. It is baselined by prefix so the gate is stable, but the underlying design margin is genuinely absent |
| Six BOMs have a stated total that disagrees with the sum of their line items and remain **unfixed** | Found by the validator on 2026-08-08; baselined as `UNRESOLVED DEFECT` | Treating a green gate as "all BOM costs are correct". Run `--show-known` to list them; each needs an owner decision on which figure is authoritative |

## Traps

Things that look wrong but are deliberate, and things that look safe but break.
Add an entry the first time something here costs someone an hour — that is the
threshold, and it is deliberately low.

- **Placed footprints have no pads.** This looks like an unfinished export. It is
  deliberate: a land pattern invented from a package name looks fabricable and is
  not. Assign real IPC-7351 footprints before layout.
- **The netlist has no signal nets.** Also deliberate — pin-level connectivity is
  not derivable from a bill of materials. The omission is stated in each `.net`
  header rather than filled with plausible guesses.
- **A green gate does not mean the CAD was checked.** Missing tools are reported
  as skips, never failures. On a machine without `kiutils`, `ezdxf` or OpenSCAD,
  the CAD checks silently do not run. Confirm the skip count is zero.
- **`generate_products.py` rewrites catalog JSON formatting** if a script edits it
  with `json.dump`. Nested arrays expand and diffs get noisy. Harmless, but do not
  mistake it for a content change.

---

Rules for this file:

- Absolute dates. Never "last week" or "recently".
- One entry per fact. A paragraph covering three decisions gets skimmed.
- Delete an entry when it becomes false. A stale note is worse than a missing
  one, because it is trusted.
- If an entry is derivable from the code or the git log, it does not belong
  here.
