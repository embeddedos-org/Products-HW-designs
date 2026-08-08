# Inertial Navigation Systems — PCB Stackup

> **Board:** eINS-900 | **Layers:** 10 | **Finished thickness:** 1.6 mm | **IPC class:** Class 3

## Construction

| # | Layer | Role | Copper | Dielectric |
|---|---|---|---|---|
| 1 | F.Cu | Signal / component side | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 2 | In1.Cu | Ground plane | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 3 | In2.Cu | Signal (inner) | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 4 | In3.Cu | Power plane | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 5 | In4.Cu | Signal (inner) | 1.0 oz | — |
| — | Core | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 6 | In5.Cu | Power plane | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 7 | In6.Cu | Signal (inner) | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 8 | In7.Cu | Power plane | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 9 | In8.Cu | Signal (inner) | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.1389 mm |
| 10 | B.Cu | Signal / solder side | 1.0 oz | — |

## Board Parameters

| Parameter | Value |
|---|---|
| Outline | 110.0 mm x 90.0 mm |
| Finished thickness | 1.6 mm +/- 10% |
| Surface finish | ENIG, conformal coated |
| Base material | FR-4 Tg170, UL 94V-0 |
| Copper weight | 1.0 oz outer and inner |
| Mounting holes | 4 x 3.2 mm, 5.0 mm inset |

## Impedance Targets

| Structure | Target | Tolerance |
|---|---|---|
| Single-ended microstrip | 50 ohm | +/- 10% |
| Differential pair | 100 ohm | +/- 10% |
| USB / Ethernet differential | 90 ohm | +/- 10% |

## Design Rules

| Rule | Value |
|---|---|
| Minimum clearance | 0.20 mm |
| Minimum track width | 0.20 mm |
| Minimum via diameter | 0.70 mm |
| Minimum drill | 0.35 mm |
| Minimum annular ring | 0.15 mm |

## Notes

Isolated IMU mounting island, thermally symmetric
