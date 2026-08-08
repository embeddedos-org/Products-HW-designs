# Anti-Tamper Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Anti-tamper subsystem protecting critical program information in fielded equipment, combining an active enclosure mesh, environmental monitoring and immediate key zeroisation. Detection to zeroise completes in under 50ms on the tamper battery alone, so removing main power does not defeat it.

## Electrical Specifications — eATP-500
| Parameter | Specification |
|---|---|
| **Root of trust** | MAX32520 with SRAM PUF, no stored key material |
| **Tamper mesh** | 4-layer serpentine, <100um pitch, resistance and capacitance monitored |
| **Environmental** | Temperature, voltage, light and X-ray detection |
| **Response time** | <50ms detection to complete key zeroisation |
| **Backup power** | Coin cell sustains tamper monitoring for 10 years |
| **Evidence** | Tamper events logged to write-once FRAM with timestamp |
| **Certification target** | FIPS 140-3 Level 4 physical security |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 80mm x 60mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, potted in opaque tamper-evident epoxy |
| **Security** | Active mesh layers 2 and 9 enclosing all secret routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| FIPS 140-3 Level 4 | Cryptographic module physical security |
| DoDI 5200.39 | Critical program information protection |
| Common Criteria EAL5+ | Security evaluation target |
