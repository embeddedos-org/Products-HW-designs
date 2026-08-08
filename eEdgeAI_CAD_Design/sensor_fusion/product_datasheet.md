# Sensor Fusion Platforms — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Multi-modal sensor fusion controller combining camera, radar, lidar and inertial inputs into a single tracked object list with per-object covariance. Time alignment across modalities is handled in hardware, since a fusion result is only as good as the worst-synchronised sensor feeding it.

## Electrical Specifications — eSFU-500
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 with R5F safety island |
| **Sensor inputs** | 4 camera, 2 radar, 1 lidar, 2 IMU |
| **Time alignment** | Hardware PTP, <50us cross-modality skew |
| **Fusion output** | Tracked object list with per-object covariance at 20Hz |
| **Functional safety** | ISO 26262 ASIL-B target, R5F lockstep monitor |
| **Interfaces** | Automotive Ethernet 1000BASE-T1, CAN FD x4 |
| **Environment** | -40degC to +105degC AEC-Q100 Grade 2 target |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 140mm x 100mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Constraint** | Automotive temperature-rated passives throughout |

## Compliance Targets
| Standard | Scope |
|---|---|
| ISO 26262 ASIL-B | Automotive functional safety |
| AEC-Q100 Grade 2 | Automotive component qualification |
| CISPR 25 Class 5 | Vehicle EMC emissions |
