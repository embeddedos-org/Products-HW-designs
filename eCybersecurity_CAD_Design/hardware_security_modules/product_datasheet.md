# Hardware Security Modules — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Network-attached hardware security module performing key generation, storage and cryptographic operations inside a tamper-responsive boundary. Sustains 12000 ECDSA P-256 signatures per second with keys that provably never leave the enclosure in plaintext form.

## Electrical Specifications — eHSM-9000
| Parameter | Specification |
|---|---|
| **Performance** | 12000 ECDSA P-256 sign/s, 45000 AES-256-GCM ops/s |
| **Key storage** | 8192 key slots, wrapped under a master key held in PUF |
| **Algorithms** | RSA-4096, ECDSA/ECDH P-521, AES-256, SHA-3, HMAC |
| **Tamper response** | Active mesh, zeroise in <50ms on breach |
| **Authentication** | M-of-N quorum with smartcard operators |
| **Interfaces** | Dual 10GbE, PKCS#11, KMIP 2.1, REST |
| **Certification target** | FIPS 140-3 Level 4, PCI HSM v4 |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 300mm x 200mm (1U) |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, potted in opaque tamper-evident epoxy |
| **Security** | 6-layer active tamper mesh enclosing the crypto boundary |

## Compliance Targets
| Standard | Scope |
|---|---|
| FIPS 140-3 Level 4 | Cryptographic module physical security |
| PCI HSM v4 | Payment card industry HSM requirements |
| Common Criteria EAL4+ | Security evaluation target |
