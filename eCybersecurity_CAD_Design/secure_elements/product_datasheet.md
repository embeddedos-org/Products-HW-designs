# Secure Element Modules — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Pluggable secure element carrier providing device authentication, secure key storage and attestation for products that cannot justify a full HSM. Three device options are pin-compatible on one carrier so a design can move up or down the cost and assurance curve without a board respin.

## Electrical Specifications — eSE-100
| Parameter | Specification |
|---|---|
| **Device options** | SE050 (EAL6+), ATECC608B, STSAFE-A110, pin-compatible |
| **Key storage** | Up to 48 key slots depending on device fitted |
| **Algorithms** | ECDSA/ECDH P-256, AES-128/256, SHA-256, HMAC |
| **Authentication** | Mutual authentication with certificate chain validation |
| **Interface** | I2C with shielded connection, up to 1MHz |
| **Provisioning** | Factory-injected certificates or field provisioning |
| **Lifetime** | 25-year data retention, 400k write endurance |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 30mm x 22mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | I2C shielded by guard traces tied to ground |

## Compliance Targets
| Standard | Scope |
|---|---|
| Common Criteria EAL6+ | Secure element evaluation assurance |
| FIPS 140-3 Level 3 | Cryptographic module security |
| IEC 62443-4-2 | Component security requirements |
