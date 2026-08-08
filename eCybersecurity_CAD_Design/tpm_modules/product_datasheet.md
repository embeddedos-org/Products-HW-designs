# TPM Modules — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Discrete TPM 2.0 module in the standard pin-header form factors, providing measured boot, sealed storage and remote attestation for platforms whose SoC lacks a firmware TPM. Supplied in SPI and LPC variants so it drops into existing mainboard headers without redesign.

## Electrical Specifications — eTPM-20
| Parameter | Specification |
|---|---|
| **Specification** | TCG TPM 2.0 Family 2.0 Level 00 Revision 1.59 |
| **Interfaces** | SPI (14-pin) and LPC (20-pin) variants |
| **PCR banks** | SHA-1 and SHA-256, 24 PCRs each |
| **Key hierarchy** | Endorsement, storage and platform hierarchies |
| **NV storage** | 8KB user non-volatile, 100k write endurance |
| **Algorithms** | RSA-2048, ECC P-256, AES-128, SHA-256, HMAC |
| **Certification** | TCG certified, Common Criteria EAL4+ chip |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 4 |
| **Dimensions** | 32mm x 22mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Connector** | 2.54mm pin header, SPI 14-pin or LPC 20-pin |

## Compliance Targets
| Standard | Scope |
|---|---|
| TCG TPM 2.0 Library | Trusted platform module specification |
| TCG PC Client Platform | Platform TPM profile |
| Common Criteria EAL4+ | Chip-level security evaluation |
