# Digital Forensic Appliances — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Forensic acquisition appliance imaging storage media through a hardware write blocker, computing hashes inline so integrity is established during capture rather than afterwards. The write block is enforced in hardware on the bus, not by driver configuration, which is what makes the resulting image defensible.

## Electrical Specifications — eFOR-900
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Write blocking** | Hardware-enforced on SATA, NVMe, USB and SAS |
| **Acquisition rate** | 480 MB/s sustained to E01 or raw image |
| **Hashing** | Concurrent MD5, SHA-1 and SHA-256 during capture |
| **Chain of custody** | Signed acquisition log with operator identity |
| **Formats** | Raw dd, EWF/E01, AFF4 |
| **Verification** | Post-acquisition re-read and hash comparison |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 240mm x 180mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Security** | Write-block logic in fabric, no firmware bypass path |

## Compliance Targets
| Standard | Scope |
|---|---|
| NIST SP 800-86 | Integrating forensic techniques into incident response |
| ISO/IEC 27037 | Identification, collection and preservation of evidence |
| NIST CFTT | Hardware write blocker tool requirements |
