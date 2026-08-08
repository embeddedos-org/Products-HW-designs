# Public Safety Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Public safety communications node bridging mission-critical push-to-talk over 5G with legacy TETRA and P25 radio estates. Bridging matters because migration takes a decade and responders cannot be left unable to reach each other partway through it.

## Electrical Specifications — ePS-1200
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Cellular** | 5G NR Sub-6GHz with 3GPP MCPTT, MCVideo and MCData |
| **Legacy bridging** | TETRA and P25 gateway with transcoding |
| **Priority** | 3GPP ARP and pre-emption for responder traffic |
| **Resilience** | Isolated operation when backhaul is lost, 72-hour battery |
| **Location** | GNSS with indoor dead-reckoning fallback |
| **Environment** | IP67, -30degC to +60degC, MIL-STD-810H shock |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 180mm x 140mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Stackup** | Isolated RF section with shielding cans |

## Compliance Targets
| Standard | Scope |
|---|---|
| 3GPP TS 23.379 | Mission critical push-to-talk |
| ETSI EN 303 413 | GNSS receiver requirements |
| EN 301 489-1 | EMC for radio equipment |
