# Signals Intelligence Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Wideband signals intelligence receiver performing continuous spectrum survey, emitter classification and time-difference-of-arrival geolocation. Four coherent receive channels share a common clock tree, which is what makes cross-channel phase interferometry usable for direction finding.

## Electrical Specifications — eSIG-3600
| Parameter | Specification |
|---|---|
| **Receiver** | 4x ADRV9002 coherent channels, 30MHz-6GHz |
| **Instantaneous bandwidth** | 160MHz per channel |
| **Survey rate** | 40 GHz/s spectrum sweep |
| **Direction finding** | Phase interferometry, 1 degree RMS accuracy |
| **Geolocation** | TDOA across networked nodes, <100m CEP at 20km |
| **Classification** | Automatic modulation recognition, 40 signal classes |
| **Recording** | Continuous IQ capture to NVMe, 2GB/s sustained |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 280mm x 200mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG with RF shielding cans |
| **Stackup** | Rogers RO4350B RF layers, phase-matched channel routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-461G | Electromagnetic interference control |
| STANAG 4658 | Electronic warfare data exchange |
| DO-160G | Airborne environmental qualification |
