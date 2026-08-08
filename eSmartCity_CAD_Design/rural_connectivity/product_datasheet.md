# Rural Connectivity Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Rural connectivity node combining a small-cell base station with long-range point-to-point backhaul for communities beyond fibre reach. Runs from solar with battery buffer, since grid supply in target deployments is frequently absent or unreliable.

## Electrical Specifications — eRUR-700
| Parameter | Specification |
|---|---|
| **Baseband** | Zynq UltraScale+ XCZU3EG, 5G NR small cell |
| **Coverage** | 8 km radius rural macro, 64 concurrent users |
| **Backhaul** | Point-to-point 5-6 GHz, 40 km at 400 Mbps |
| **Spectrum** | Sub-6GHz NR bands plus licensed-exempt backhaul |
| **Power** | 200W solar array with 48-hour battery autonomy |
| **Mounting** | Tower or pole, 30 kg including radome |
| **Environment** | IP66, -30degC to +55degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 260mm x 200mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG with RF shielding cans |
| **Stackup** | Rogers RO4350B RF layers over FR-4 core |

## Compliance Targets
| Standard | Scope |
|---|---|
| 3GPP TS 38.104 | NR base station radio transmission and reception |
| ETSI EN 302 217 | Fixed radio systems point-to-point |
| EN 301 489-1 | EMC for radio equipment |
