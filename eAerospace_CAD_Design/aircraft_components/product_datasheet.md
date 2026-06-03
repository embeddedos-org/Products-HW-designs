# Aircraft Components — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Smart structural aircraft components with embedded health monitoring, CAN FD data buses, and ARINC-429 interfaces for integration into commercial and military airframes.

## Physical Specifications
| Parameter | Specification |
|---|---|
| **Primary structure** | Carbon-fiber reinforced polymer (CFRP), T800H/Epoxy |
| **Secondary structure** | Aluminum 7075-T6, Titanium Ti-6Al-4V |
| **Operating temp** | -55°C to +85°C (structural), -40°C to +70°C (electronics) |
| **Vibration** | DO-160G Cat. U (20g RMS, 20–2000Hz) |
| **Altitude** | 0–50,000 ft (certified) |

## Electrical Specifications
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3ZIT6 ARM Cortex-M7 @ 280MHz |
| **Data bus** | ARINC-429, CAN FD (ISO 11898-1) |
| **Sensors** | Strain gauges, accelerometers, temperature |
| **Power** | 28VDC MIL-STD-704F aircraft bus |
| **Connector** | MIL-DTL-38999 Series III |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 80mm × 60mm |
| **IPC Class** | Class 3 Aerospace |
| **Surface finish** | ENIG |
| **Conformal coating** | Acrylic (IPC-CC-830) |
