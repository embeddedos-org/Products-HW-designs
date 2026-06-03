# AeroSwift CAD Design

> AeroSwift is EmbeddedOS's autonomous aerial mobility platform, comprising two product lines — **AeroSwift Personal** (AS-1/2, single-to-dual-seat personal eVTOL) and **AeroSwift Transit** (AS-10, 10-passenger urban air transit vehicle) — built on a shared AeroOS flight-computer platform.

## Product Overview

| Product | Model | Seats | Power System | Altitude | Target Price | Market |
|---|---|---|---|---|---|---|
| **AeroSwift Personal** | AS-1 / AS-2 | 1–2 | Solar + Semi-Solid-State Battery | 0–3,000m | $85K–$120K | Personal commuters |
| **AeroSwift Transit** | AS-10 | 10 | Solar + 60kWh Solid-State Pack | 0–5,000m | $1.2M–$1.8M | Urban transit fleets |

## Hardware Architecture

Both products share a common **AeroOS Flight Computer** platform based on:

- **SoC:** Rockchip RK3588S (6-core ARM Cortex-A76/A55 + 32-TOPS NPU)
- **RTOS Co-Processor:** STM32H7B3 ARM Cortex-M7 @ 280MHz (dual)
- **V2X:** Autotalks TEKTON3 DSRC + C-V2X sidelink
- **Navigation:** u-blox ZED-F9P dual-frequency RTK GPS (dual)
- **IMU:** Epson G362P 6-DOF (dual redundant)
- **LiDAR:** Livox Mid-360 solid-state 360° obstacle detection
- **Power Monitor:** TI INA3221 triple-channel

The **AeroSwift Transit** flight computer (AS-T-FC-001) adds **Triple Modular Redundancy (TMR)** via a Xilinx XC7S50 FPGA voter arbitrating three independent flight control computers on a 12-layer PCB.

## Directory Structure

```
AeroSwift/
├── README.md
├── aeroswift_personal/          AeroSwift Personal (AS-1/2) — 1-2 seat eVTOL
│   ├── bom/
│   │   └── bom_master.csv       Full vehicle bill of materials
│   ├── pcb/
│   │   └── flight_computer/
│   │       └── stackup.md       AS-FC-001 8-layer PCB stackup (IPC Class 3)
│   ├── cad/                     CAD model files (placeholder)
│   └── antenna/                 Antenna design files (placeholder)
├── aeroswift_transit/           AeroSwift Transit (AS-10) — 10-seat urban air transit
│   ├── bom/
│   │   ├── bom_master.csv       Full vehicle bill of materials
│   │   └── bom_pcb.csv          Flight computer PCB bill of materials
│   ├── pcb/
│   │   └── flight_computer/
│   │       └── stackup.md       AS-T-FC-001 12-layer TMR PCB stackup (DO-254 Level A)
│   ├── cad/                     CAD model files (placeholder)
│   └── antenna/                 Antenna design files (placeholder)
└── shared_platform/             Shared AeroOS platform hardware (from monorepo)
    ├── bom/
    │   ├── bom_personal.csv     Personal variant consolidated BOM
    │   └── bom_transit.csv      Transit variant consolidated BOM
    └── pcb/
        └── flight_computer/
            ├── stackup_personal.md  Personal flight computer PCB stackup
            └── stackup_transit.md   Transit flight computer PCB stackup
```

## PCB Summary

| Board ID | Product | Layers | Dimensions | IPC Class | Key Feature |
|---|---|---|---|---|---|
| AS-FC-001 | AeroSwift Personal | 8 | 120×80mm | Class 3 | Single flight computer |
| AS-T-FC-001 | AeroSwift Transit | 12 | 160×120mm | Class 3 / DO-254 Level A | Triple Modular Redundancy (TMR) |

## Power Architecture

Both products use a shared multi-source power strategy:

```
+-------------------+  +-------------------+  +-------------------+
|  Perovskite Solar |  | Solid-State / Li- |  |  Kinetic Regen    |
|  Wing/roof film   |  |  Metal Battery    |  |  Descent capture  |
|  Primary harvest  |  |  Primary storage  |  |  Braking energy   |
+-------------------+  +-------------------+  +-------------------+
```

- **Personal:** 12m² perovskite-on-silicon solar film + 22.5kWh semi-solid-state Li-metal pack (×4)
- **Transit:** 48m² perovskite-on-silicon solar film + 60kWh pure solid-state silicon-anode pack (×8)

## Related Repositories

| Repo | Relationship |
|---|---|
| [eos-aero](https://github.com/embeddedos-org/eos-aero) | AeroSwift monorepo — firmware, software, docs |
| [eos](https://github.com/embeddedos-org/eos) | Embedded OS firmware for AeroOS flight controllers |
| [eAI](https://github.com/embeddedos-org/eAI) | AI for autonomous flight, obstacle avoidance, route planning |
| [EoSim](https://github.com/embeddedos-org/EoSim) | Flight simulation & digital twin of AeroSwift vehicles |
| [eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products) | Parent CAD design repository |
