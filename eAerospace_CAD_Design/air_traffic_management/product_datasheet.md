# Air Traffic Management Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Ground surveillance receiver combining 1090MHz ADS-B extended squitter, Mode-S multilateration, and UAT reception into a single fused track feed. Time-of-arrival stamping is disciplined to UTC by a GNSS-locked OCXO, giving the sub-10ns timing that wide-area multilateration requires.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eATM-3000 | Surveillance receiver and fusion node | 1U rackmount |
| eATM-RSU | Remote sensor unit | Pole-mounted IP67 |
| eATM-TWR | Tower display interface | 19-inch console |

## Electrical Specifications — eATM-3000
| Parameter | Specification |
|---|---|
| **Receiver** | ADRV9002, 1090MHz ES and 978MHz UAT |
| **Processing** | Zynq UltraScale+ XCZU3EG, pulse decode in fabric |
| **Sensitivity** | -96 dBm MTL at 90% reply ratio |
| **Timing** | GNSS-disciplined OCXO, <10ns TOA stamping |
| **Capacity** | 2000 simultaneous tracks, 500 msg/s sustained |
| **Range** | 400km line of sight for ADS-B ES |
| **Output** | ASTERIX Cat-021/Cat-023 over TCP, 10GbE |
| **Redundancy** | Dual power feed, hot-standby pairing |
| **Availability** | 99.99% design target |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 260mm x 180mm |
| **Stackup** | Rogers RO4350B RF layer over FR-4 |
| **IPC Class** | Class 2 |
| **Finish** | ENIG with shielding cans over RF sections |
| **Impedance** | 50 ohm RF, 100 ohm differential |

## Compliance Targets
| Standard | Scope |
|---|---|
| ED-129B | Technical specification for ADS-B ground stations |
| DO-260C | 1090MHz extended squitter ADS-B MOPS |
| EUROCAE ED-142 | Wide-area multilateration performance |
| EN 301 489-1 | EMC for radio equipment |
