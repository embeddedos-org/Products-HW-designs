# C4ISR Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Deployable command and control node integrating Link-16, VMF and situational awareness feeds into a common operating picture. Cross-domain guard functions run on physically separate processors so classified and unclassified enclaves never share a memory controller.

## Electrical Specifications — eC4I-7000
| Parameter | Specification |
|---|---|
| **Processor** | Zynq UltraScale+ XCZU3EG + Jetson Orin NX for AI fusion |
| **Tactical data links** | Link-16 (MIL-STD-6016), VMF, JREAP-C |
| **Track capacity** | 8000 tracks, correlated across 6 sources |
| **Cross-domain** | Physically separate enclave processors, unidirectional guard |
| **Cryptography** | Suite B, hardware key store, zeroise on tamper |
| **Interfaces** | 10GbE x4, 1GbE x8, serial x8 |
| **Environment** | MIL-STD-810H transit case, -32degC to +60degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 260mm x 200mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Security** | Tamper mesh over key storage region |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-6016 | Tactical data link Link-16 message standard |
| STANAG 5516 | NATO tactical data exchange |
| FIPS 140-3 Level 3 | Cryptographic module security |
