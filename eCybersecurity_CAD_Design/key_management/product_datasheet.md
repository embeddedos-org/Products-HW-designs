# Key Management Appliances — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Key management appliance handling generation, distribution, rotation and destruction across an enterprise fleet, speaking KMIP to storage arrays and PKCS#11 to applications. Key state is replicated across a quorum so no single appliance loss destroys material, which is the failure mode that makes teams avoid rotation.

## Electrical Specifications — eKMS-3000
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Key capacity** | 1 million managed key objects |
| **Protocols** | KMIP 2.1, PKCS#11, REST, Vault-compatible API |
| **Replication** | Raft quorum across 3-7 appliances |
| **Key hierarchy** | Master key in secure element, DEK/KEK envelope |
| **Audit** | Append-only signed log, tamper-evident chain |
| **Rotation** | Policy-driven automatic rotation with grace windows |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 250mm x 180mm (1U) |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | Chassis intrusion switch wired to zeroise logic |

## Compliance Targets
| Standard | Scope |
|---|---|
| OASIS KMIP 2.1 | Key management interoperability protocol |
| NIST SP 800-57 | Key management recommendations |
| FIPS 140-3 Level 2 | Cryptographic module security |
