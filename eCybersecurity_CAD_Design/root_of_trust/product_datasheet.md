# Hardware Root of Trust — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Hardware root of trust providing device identity, key derivation and platform attestation from an SRAM physically unclonable function. No private key is ever stored: the identity is reconstructed from silicon variation at each boot and erased on power-down, so extracting flash yields nothing usable.

## Electrical Specifications — eROT-400
| Parameter | Specification |
|---|---|
| **Identity source** | SRAM PUF, 256-bit unique device secret |
| **Key storage** | None persistent; keys derived per boot and zeroised |
| **Attestation** | DICE layered attestation with per-layer CDI |
| **Cryptography** | ECDSA P-256/P-384, AES-256-GCM, SHA-2/SHA-3 |
| **Entropy** | NIST SP 800-90B compliant TRNG, 1.2 Mbit/s |
| **Side-channel** | DPA-resistant AES with masking and shuffling |
| **Certification target** | FIPS 140-3 Level 3 |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 85mm x 65mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, potted |
| **Security** | Secret routing confined to inner layers under ground pour |

## Compliance Targets
| Standard | Scope |
|---|---|
| FIPS 140-3 Level 3 | Cryptographic module security |
| TCG DICE | Device identifier composition engine |
| NIST SP 800-90B | Entropy source validation |
