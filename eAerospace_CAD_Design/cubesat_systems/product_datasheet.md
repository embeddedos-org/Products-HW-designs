# CubeSat Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
PC/104-compatible CubeSat avionics stack providing on-board computing, electrical power conditioning, and attitude determination for 1U through 12U missions. COTS-based rather than rad-hard, with watchdog-driven latch-up recovery and triple-redundant boot images sized for LEO missions of up to three years.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eCUBE-3U-OBC | On-board computer | PC/104 90x96mm |
| eCUBE-EPS | Electrical power system with MPPT | PC/104 90x96mm |
| eCUBE-ADCS | Attitude determination and control | PC/104 90x96mm |

## Electrical Specifications — eCUBE-3U
| Parameter | Specification |
|---|---|
| **Processor** | STM32H743 Cortex-M7 at 480MHz |
| **Supervisor** | iCE40UP5K FPGA watchdog and latch-up monitor |
| **Memory** | 16MB QSPI NOR triple-redundant boot, 1Mbit FRAM state |
| **Attitude sensing** | ICM-42688-P IMU + MMC5983MA magnetometer |
| **Power generation** | Deployable PV, MPPT charge, 2x 18650 Li-ion |
| **Bus** | PC/104 stack-through, I2C + CAN FD |
| **Downlink** | UHF 437MHz, 9.6-19.2kbps GMSK |
| **Mass** | 310g per board including harness |
| **Mission life** | 3 years LEO at 550km |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 90mm x 96mm (PC/104 form factor) |
| **Stackup** | Symmetric with dedicated analogue ground pour |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, staked components, conformal coated |
| **Connector** | PC/104 104-pin stack-through header |

## Compliance Targets
| Standard | Scope |
|---|---|
| CubeSat Design Specification Rev 14 | Mechanical and deployment interface |
| NASA-STD-6016 | Materials and outgassing |
| ECSS-E-ST-10-03C | Vibration and thermal vacuum testing |
| ITU-R Radio Regulations | UHF amateur/commercial downlink licensing |
