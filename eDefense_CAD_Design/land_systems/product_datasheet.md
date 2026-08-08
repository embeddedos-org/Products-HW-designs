# Land Combat Vehicle Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Vehicle electronic architecture controller implementing a NATO Generic Vehicle Architecture backbone for armoured platforms, bridging legacy CAN subsystems onto a switched Ethernet core. Survives the 28V transients of MIL-STD-1275E without shedding load, including 100V spike and 250V surge events.

## Electrical Specifications — eLCS-1500
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Vehicle bus** | NATO GVA over 1GbE, plus CAN FD x8 legacy bridge |
| **Power transients** | MIL-STD-1275E compliant, 100V spike / 250V surge |
| **Inertial** | IIM-42652 high-shock IMU for hull motion |
| **Crew displays** | 4x DisplayPort outputs, sunlight readable |
| **Interfaces** | 1GbE x8, CAN FD x8, RS-422 x4, 48 discrete I/O |
| **Environment** | MIL-STD-810H, -46degC to +71degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 200mm x 160mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Connector** | MIL-DTL-38999 Series III |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-1275E | 28V vehicle electrical power characteristics |
| STANAG 4754 | NATO Generic Vehicle Architecture |
| MIL-STD-810H | Environmental engineering considerations |
