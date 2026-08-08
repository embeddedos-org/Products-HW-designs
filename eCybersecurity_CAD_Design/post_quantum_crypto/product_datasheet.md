# Post-Quantum Cryptography Accelerators — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Post-quantum cryptography accelerator implementing ML-KEM and ML-DSA in FPGA fabric, sized for the large key and signature objects those schemes require. Supports hybrid classical-plus-PQC handshakes so deployment does not depend on the peer having migrated first.

## Electrical Specifications — ePQC-500
| Parameter | Specification |
|---|---|
| **Algorithms** | ML-KEM-768/1024 (FIPS 203), ML-DSA-65/87 (FIPS 204) |
| **Hash-based signatures** | SLH-DSA (FIPS 205) for firmware signing |
| **Performance** | 18000 ML-KEM-768 encapsulations/s |
| **Hybrid mode** | X25519 + ML-KEM concurrent key agreement |
| **Key sizes** | Handles 1568-byte ML-KEM and 4627-byte ML-DSA objects |
| **Side-channel** | Constant-time lattice arithmetic, masked NTT |
| **Host interface** | PCIe Gen2 x4 or 10GbE |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 140mm x 100mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Length-matched DDR4 and back-drilled PCIe |

## Compliance Targets
| Standard | Scope |
|---|---|
| FIPS 203 | Module-lattice key encapsulation mechanism |
| FIPS 204 | Module-lattice digital signature algorithm |
| NIST SP 800-227 | Key encapsulation mechanism recommendations |
