# ISR Payload Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Gimbal-mounted intelligence, surveillance and reconnaissance payload combining electro-optical, thermal and laser rangefinder sensing with on-board target detection. Metadata is encoded to MISB ST 0601 in the payload, so exploitation downstream does not depend on a separate telemetry correlation step.

## Electrical Specifications — eISR-1200
| Parameter | Specification |
|---|---|
| **Processor** | Jetson Orin NX, 100 TOPS on-board inference |
| **Electro-optical** | 2.3MP global shutter, 30x continuous optical zoom |
| **Thermal** | 640x512 LWIR, 25mK NETD |
| **Laser rangefinder** | 1550nm eye-safe, 8km range, 1m accuracy |
| **Stabilisation** | 4-axis gimbal, 15 urad RMS jitter |
| **Video** | H.265 encode, STANAG 4609 with MISB ST 0601 metadata |
| **Detection** | On-board vehicle and personnel detection, 30fps |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 120mm x 100mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Constraint** | Mass-optimised for gimbal payload budget |

## Compliance Targets
| Standard | Scope |
|---|---|
| STANAG 4609 | NATO digital motion imagery format |
| MISB ST 0601 | UAS datalink local metadata set |
| DO-160G | Airborne environmental qualification |
