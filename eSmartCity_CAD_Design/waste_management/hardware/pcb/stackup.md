# Smart Waste Management — PCB Stackup

> **Board:** eWM-300 | **Layers:** 4 | **Finished thickness:** 1.6 mm | **IPC class:** Class 2

## Construction

| # | Layer | Role | Copper | Dielectric |
|---|---|---|---|---|
| 1 | F.Cu | Signal / component side | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.4867 mm |
| 2 | In1.Cu | Ground plane | 1.0 oz | — |
| — | Core | FR-4 Tg170 dielectric | — | 0.4867 mm |
| 3 | In2.Cu | Signal (inner) | 1.0 oz | — |
| — | Prepreg | FR-4 Tg170 dielectric | — | 0.4867 mm |
| 4 | B.Cu | Signal / solder side | 1.0 oz | — |

## Board Parameters

| Parameter | Value |
|---|---|
| Outline | 60.0 mm x 45.0 mm |
| Finished thickness | 1.6 mm +/- 10% |
| Surface finish | ENIG, potted |
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
| Minimum clearance | 0.15 mm |
| Minimum track width | 0.15 mm |
| Minimum via diameter | 0.60 mm |
| Minimum drill | 0.30 mm |
| Minimum annular ring | 0.13 mm |

