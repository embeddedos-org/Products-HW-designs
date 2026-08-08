# Zero Trust Gateways — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Zero trust network gateway enforcing per-session identity, device posture and policy before any traffic reaches a protected segment. Device posture is attested cryptographically rather than asserted, so a compromised endpoint cannot simply claim to be healthy.

## Electrical Specifications — eZTG-1000
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 with crypto offload |
| **Throughput** | 4 Gbps inspected, 8 Gbps mTLS terminated |
| **Policy** | Per-session identity, device posture and context evaluation |
| **Attestation** | Remote attestation of endpoint TPM quotes |
| **Micro-segmentation** | 4096 enforced segments with default-deny |
| **Protocols** | mTLS 1.3, WireGuard, IPsec, SPIFFE/SPIRE identity |
| **Logging** | Per-flow decision log to signed append-only store |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 220mm x 160mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Impedance-controlled 100 ohm differential Ethernet |

## Compliance Targets
| Standard | Scope |
|---|---|
| NIST SP 800-207 | Zero trust architecture |
| IEC 62443-3-3 | System security requirements |
| FIPS 140-3 Level 2 | Cryptographic module security |
