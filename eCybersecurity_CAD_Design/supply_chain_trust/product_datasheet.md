# Supply Chain Trust Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Supply chain trust station verifying component provenance at goods-in, combining cryptographic authentication of parts that support it with X-ray and thermal signature comparison for those that do not. Counterfeit detection matters most for the legacy parts that carry no secure element at all.

## Electrical Specifications — eSCT-700
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Cryptographic check** | Challenge-response for parts with a secure element |
| **Thermal signature** | MLX90640 thermal profile comparison under load |
| **Optical inspection** | Die marking and package surface comparison |
| **Provenance record** | Signed SBOM/HBOM entry per verified lot |
| **Throughput** | 240 components per hour for full verification |
| **Database** | Reference signatures for 40000 part numbers |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 200mm x 160mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Isolated device-under-test power domain |

## Compliance Targets
| Standard | Scope |
|---|---|
| SAE AS6081 | Counterfeit electronic parts avoidance |
| NIST SP 800-161 | Cybersecurity supply chain risk management |
| IEC 62443-4-1 | Secure product development lifecycle |
