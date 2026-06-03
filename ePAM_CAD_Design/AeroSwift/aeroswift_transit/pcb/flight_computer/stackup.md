# AeroSwift-Transit Flight Computer PCB Stackup
**Board:** AS-T-FC-001 — AeroOS Triple-Redundant Flight Computer  
**Revision:** A  
**Layer Count:** 12 Layers  
**Board Dimensions:** 160mm × 120mm  
**Manufacturer Target:** TTM Technologies / Sanmina (IPC Class 3 Aerospace)

---

## Layer Stackup

| Layer | Name | Type | Material | Thickness (mm) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| L1 | TOP_SIGNAL | Signal | 2 oz Copper | 0.070 | FCC-A primary processor |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L2 | GND_PLANE_A | Ground | 1 oz Copper | 0.035 | FCC-A ground reference |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L3 | PWR_PLANE_A | Power | 1 oz Copper | 0.035 | FCC-A power rails |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L4 | INNER_SIG_A | Signal | 0.5 oz Copper | 0.018 | FCC-A DDR5 / PCIe |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L5 | INNER_SIG_B | Signal | 0.5 oz Copper | 0.018 | FCC-B DDR5 / PCIe |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L6 | PWR_PLANE_B | Power | 1 oz Copper | 0.035 | FCC-B power rails |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L7 | GND_PLANE_B | Ground | 1 oz Copper | 0.035 | FCC-B ground reference |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L8 | INNER_SIG_C | Signal | 0.5 oz Copper | 0.018 | FCC-C DDR5 / PCIe |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L9 | PWR_PLANE_C | Power | 1 oz Copper | 0.035 | FCC-C power rails |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L10 | GND_PLANE_C | Ground | 1 oz Copper | 0.035 | FCC-C ground reference |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L11 | HV_PWR_BUS | Power | 3 oz Copper | 0.105 | 800V battery bus (isolated) |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L12 | BOT_SIGNAL | Signal | 2 oz Copper | 0.070 | Bottom components, TMR voter |

**Total Board Thickness:** ~2.4mm (heavy copper variant)

---

## Triple Modular Redundancy (TMR) Architecture

The AS-T-FC-001 board hosts three independent flight control computers (FCC-A, FCC-B, FCC-C) on a single PCB, each with their own power domains, ground planes, and signal layers. The TMR Voter IC (Xilinx XC7S50 FPGA) arbitrates between the three FCCs at the hardware level.

```
FCC-A (L1/L2/L3/L4)  ──┐
FCC-B (L5/L6/L7/L8)  ──┤──> TMR Voter (L12) ──> Motor CAN Bus
FCC-C (L9/L10/L11)   ──┘
```

---

## Critical Design Rules

| Parameter | Value |
| :--- | :--- |
| Min Trace Width | 0.10mm (signal), 2.0mm (HV power) |
| Min Via Drill | 0.20mm (signal), 1.0mm (HV power) |
| HV Clearance | 6.0mm (800V creepage per IPC-2221B) |
| Controlled Impedance | 50Ω single-ended, 100Ω differential |
| Surface Finish | ENIG |
| IPC Class | Class 3 Aerospace (DO-254 Level A) |
| Conformal Coating | Acrylic, all assemblies |
