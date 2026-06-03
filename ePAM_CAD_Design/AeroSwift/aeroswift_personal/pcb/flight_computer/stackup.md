# AeroSwift-Personal Flight Computer PCB Stackup
**Board:** AS-FC-001 — AeroOS Main Flight Computer  
**Revision:** A  
**Layer Count:** 8 Layers  
**Board Dimensions:** 120mm × 80mm  
**Manufacturer Target:** Advanced Circuits / PCBWay (IPC Class 3)

---

## Layer Stackup

| Layer | Name | Type | Material | Thickness (mm) | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| L1 | TOP_SIGNAL | Signal | 1 oz Copper | 0.035 | Component placement, high-speed signals |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | High-Tg FR4 equivalent |
| L2 | GND_PLANE | Ground | 1 oz Copper | 0.035 | Solid ground reference |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L3 | PWR_PLANE | Power | 1 oz Copper | 0.035 | 3.3V, 5V, 12V split planes |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L4 | INNER_SIGNAL_1 | Signal | 0.5 oz Copper | 0.018 | DDR5 memory bus |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L5 | INNER_SIGNAL_2 | Signal | 0.5 oz Copper | 0.018 | PCIe / MIPI CSI lanes |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L6 | GND_PLANE_2 | Ground | 1 oz Copper | 0.035 | Secondary ground reference |
| — | Core | Dielectric | Isola 370HR | 0.200 | |
| L7 | PWR_PLANE_2 | Power | 1 oz Copper | 0.035 | Battery bus, motor driver supply |
| — | Prepreg | Dielectric | Isola 370HR | 0.100 | |
| L8 | BOT_SIGNAL | Signal | 1 oz Copper | 0.035 | Bottom components, SPI/I2C buses |

**Total Board Thickness:** ~1.6mm (standard)

---

## Critical Design Rules

| Parameter | Value |
| :--- | :--- |
| Min Trace Width | 0.10mm (signal), 0.50mm (power) |
| Min Via Drill | 0.20mm (0.40mm pad) |
| Min Clearance | 0.10mm |
| Controlled Impedance | 50Ω single-ended (L1/L8), 100Ω differential (L4/L5) |
| Surface Finish | ENIG (Electroless Nickel Immersion Gold) |
| Solder Mask | LPI Green, both sides |
| Silkscreen | White, both sides |
| IPC Class | Class 3 (Aerospace/High-Reliability) |

---

## Key ICs & Placement Notes

| Component | Location | Placement Notes |
| :--- | :--- | :--- |
| RK3588S SoC | Center L1 | Thermal pad to copper pour, 4× thermal vias |
| STM32H7B3 | Near edge L1 | Close to motor driver connectors |
| LPDDR5 RAM | Adjacent to RK3588S | Match-length DDR5 routing on L4 |
| eMMC Flash | Adjacent to RK3588S | HS400 routing, length-matched |
| Epson G362P IMU | Isolated corner | Mechanical isolation from vibration |
| ZED-F9P GPS | Near antenna connector | Short RF trace to SMA connector |
| TEKTON3 V2X | Near antenna connector | 50Ω controlled impedance RF traces |
| INA3221 Power Monitor | Near battery connector | Kelvin sense connections |

---

## Connector Pinout Summary

| Connector | Type | Signals |
| :--- | :--- | :--- |
| J1 — Battery Bus | XT90-S | VBAT+, VBAT-, GND |
| J2 — Motor CAN Bus | 4-pin JST-GH | CAN_H, CAN_L, 12V, GND |
| J3 — GPS Antenna | SMA | RF (50Ω) |
| J4 — V2X Antenna | SMA | RF (50Ω) |
| J5 — LiDAR UART | 4-pin JST-GH | TX, RX, 5V, GND |
| J6 — IMU SPI | 6-pin JST-GH | MOSI, MISO, SCK, CS, 3.3V, GND |
| J7 — Camera MIPI | 30-pin FPC | MIPI CSI-2 4-lane |
| J8 — Debug JTAG | 10-pin ARM JTAG | SWDIO, SWDCLK, nRST, GND |
| J9 — Ground Station USB | USB-C | USB 3.2 Gen 1 |
