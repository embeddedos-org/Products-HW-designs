# Smart Street Lighting — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
NEMA socket luminaire controller providing adaptive dimming, energy metering and fault reporting across a city lighting estate. Revenue-grade metering per luminaire is what allows unmetered-supply tariffs to be replaced with measured billing, which usually funds the retrofit.

## Electrical Specifications — eSL-400
| Parameter | Specification |
|---|---|
| **Controller** | STM32G474 Cortex-M4 at 170MHz |
| **Socket** | ANSI C136.41 7-pin NEMA twist-lock |
| **Dimming** | 0-10V and DALI-2 output, 1% to 100% |
| **Metering** | Class 1 energy accuracy per IEC 62053-21 |
| **Adaptive control** | Ambient light, motion and schedule-driven profiles |
| **Communications** | LoRaWAN with TALQ 2.x smart city interface |
| **Lifetime** | 20 years, 25000 dim cycles |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 70mm diameter circular |
| **IPC Class** | Class 2 |
| **Finish** | ENIG, conformal coated |
| **Isolation** | 4kV reinforced between mains and control |

## Compliance Targets
| Standard | Scope |
|---|---|
| ANSI C136.41 | Dimming receptacles for roadway lighting |
| IEC 62053-21 | Static meters for active energy, Class 1 |
| EN 61000-6-3 | Residential and light industrial emissions |
