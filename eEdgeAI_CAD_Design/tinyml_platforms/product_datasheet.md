# TinyML Platforms — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Battery-powered TinyML sensor node running quantised models entirely on a Cortex-M33, with no external accelerator. The design target is a year of always-on keyword and anomaly detection from a single coin cell, which constrains the model budget to roughly 256KB and 2 MFLOPs per inference.

## Electrical Specifications — eTML-100
| Parameter | Specification |
|---|---|
| **Processor** | STM32U575 Cortex-M33 at 160MHz with TrustZone |
| **Model budget** | 256KB quantised INT8, ~2 MFLOPs per inference |
| **Inference rate** | 10Hz always-on, 1.8ms per keyword inference |
| **Sensing** | IMU, microphone, temperature, humidity and pressure |
| **Wake power** | 3.2uA in always-on listening with hardware VAD |
| **Connectivity** | BLE 5.4 for model update and event reporting |
| **Battery life** | 12 months on a single CR2032 at 10Hz duty |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 48mm x 36mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Constraint** | No component above 1.2mm for wearable enclosure |

## Compliance Targets
| Standard | Scope |
|---|---|
| FCC Part 15 Subpart B | Unintentional radiator emissions |
| EN 300 328 | 2.4GHz wideband transmission systems |
| IEC 62368-1 | Equipment safety |
