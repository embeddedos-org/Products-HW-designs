# Remote Attestation Appliances — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Attestation verifier appraising evidence from a device fleet against reference values and issuing signed attestation results. Implements the IETF RATS role split, so relying parties consume a short-lived result rather than parsing raw TPM quotes themselves.

## Electrical Specifications — eATT-600
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Architecture** | IETF RATS verifier role per RFC 9334 |
| **Evidence formats** | TPM 2.0 quotes, DICE certificates, ARM PSA tokens |
| **Throughput** | 6000 attestation appraisals per second |
| **Reference values** | 500k golden measurements, signed CoRIM import |
| **Result format** | EAT (RFC 9711) signed attestation results |
| **Freshness** | Nonce and epoch-based, configurable validity window |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 220mm x 160mm (1U) |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | Signing key confined to secure element, never in DRAM |

## Compliance Targets
| Standard | Scope |
|---|---|
| IETF RFC 9334 | Remote attestation procedures architecture |
| IETF RFC 9711 | Entity attestation token |
| FIPS 140-3 Level 2 | Cryptographic module security |
