# Secure Boot Subsystems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Secure boot subsystem enforcing a verified boot chain from immutable ROM through bootloader to application, with measurements extended into a TPM at each stage. Rollback protection uses a monotonic counter in secure storage, so a signed-but-old image with a known vulnerability cannot be replayed onto the device.

## Electrical Specifications — eSB-200
| Parameter | Specification |
|---|---|
| **Root of trust** | Immutable boot ROM with OTP-fused public key hash |
| **Signature scheme** | ECDSA P-384 with SHA-384 image digest |
| **Measurement** | PCR extension into TPM 2.0 at each boot stage |
| **Rollback protection** | Monotonic counter in OTP, 64 update slots |
| **Boot time** | 180ms from reset to verified application entry |
| **Recovery** | A/B image slots with automatic fallback on failed attestation |
| **Key revocation** | Field-revocable signing keys, 4 generations |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 60mm x 45mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | TPM SPI bus routed on inner layers only |

## Compliance Targets
| Standard | Scope |
|---|---|
| NIST SP 800-193 | Platform firmware resiliency guidelines |
| TCG PC Client Platform | TPM 2.0 measured boot profile |
| IEC 62443-4-2 | Component security requirements |
