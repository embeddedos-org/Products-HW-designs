# Dismounted Soldier Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Body-worn soldier computer providing blue-force tracking, tactical messaging and heads-up situational awareness on a single battery cycle covering a 72-hour mission. Power draw was the primary design constraint, so the display and radio duty-cycle aggressively against soldier activity state.

## Electrical Specifications — eSLD-300
| Parameter | Specification |
|---|---|
| **Processor** | NXP i.MX 8M Plus quad Cortex-A53 with NPU |
| **Positioning** | MAX-M10S GNSS with dead-reckoning fallback |
| **Tactical radio** | Sub-GHz mesh, 2W, 4km urban range |
| **Personal area network** | BLE 5.4 for weapon sight and helmet display |
| **Battery life** | 72 hours with adaptive duty cycling |
| **Mass** | 480g including battery and harness |
| **Environment** | MIL-STD-810H, IP68, -32degC to +60degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 110mm x 70mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Construction** | Rigid-flex to reduce interconnect failure under load |

## Compliance Targets
| Standard | Scope |
|---|---|
| STANAG 4677 | Dismounted soldier system architecture |
| MIL-STD-810H | Environmental engineering considerations |
| MIL-STD-461G | Electromagnetic interference control |
