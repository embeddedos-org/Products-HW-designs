# Edge AI Accelerator Modules — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
General-purpose edge inference module pairing a Jetson Orin NX with a discrete Hailo-8 accelerator, so vision pipelines and transformer workloads can run concurrently without contending for the same compute. Conduction-cooled to a 40W sustained envelope in a 150x115mm footprint.

## Electrical Specifications — eAI-2000
| Parameter | Specification |
|---|---|
| **Primary compute** | NVIDIA Jetson Orin NX 16GB, 100 TOPS INT8 |
| **Secondary accelerator** | Hailo-8 M.2, 26 TOPS for parallel vision pipeline |
| **Memory** | 16GB LPDDR5 on module plus 8GB carrier-side |
| **Storage** | 128GB eMMC with hardware encryption |
| **Camera input** | 8 lanes MIPI CSI-2, 4 simultaneous sensors |
| **Networking** | 2.5GbE, Wi-Fi 6 and BLE 5.3 |
| **Thermal envelope** | 40W sustained conduction-cooled, 60W peak |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 150mm x 115mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Thermal** | Copper coin under module, 6W/mK gap pad to chassis |

## Compliance Targets
| Standard | Scope |
|---|---|
| FCC Part 15 Subpart B | Unintentional radiator emissions |
| EN 55032 Class B | Multimedia equipment emissions |
| IEC 62368-1 | Equipment safety |
