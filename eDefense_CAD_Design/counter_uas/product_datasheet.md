# Counter-UAS Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Counter-UAS node combining RF protocol detection, mmWave radar tracking and acoustic cueing to detect and classify small unmanned aircraft. Remote ID decoding per ASTM F3411 separates cooperative traffic from genuine intrusions, which keeps the false alarm rate workable in urban airspace.

## Electrical Specifications — eCUAS-900
| Parameter | Specification |
|---|---|
| **RF detection** | ADRV9002, 400MHz-6GHz protocol fingerprinting |
| **Radar** | IWR6843AOP 60GHz, 1.2km Group-1 UAS detection |
| **Remote ID** | ASTM F3411 Bluetooth and Wi-Fi NAN decoding |
| **Classification** | On-board inference, 60 airframe and protocol classes |
| **Detection range** | 3km RF, 1.2km radar for 250g quadrotor |
| **Direction finding** | 4-element array, 3 degree RMS bearing accuracy |
| **Environment** | IP67, -30degC to +60degC, pole or vehicle mount |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 200mm x 160mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG with RF shielding cans |
| **Stackup** | Rogers RO4350B RF layer over FR-4 |

## Compliance Targets
| Standard | Scope |
|---|---|
| ETSI EN 303 883 | Radio measurement equipment |
| ASTM F3411 | Remote identification of unmanned aircraft |
| EN 301 489-1 | EMC for radio equipment |
