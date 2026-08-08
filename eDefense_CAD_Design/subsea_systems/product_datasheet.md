# Subsea Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Subsea electronics module for ROV, AUV and seabed installation control at depths to 3000m. Uses a pressure-balanced oil-filled housing rather than a one-atmosphere vessel, which removes the dominant implosion failure mode and cuts housing mass substantially.

## Electrical Specifications — eSUB-400
| Parameter | Specification |
|---|---|
| **Controller** | STM32H743 Cortex-M7, dual redundant |
| **Depth rating** | 3000m, pressure-balanced oil-filled |
| **Sensing** | 24-bit AD7124 for strain, pressure and temperature |
| **Subsea comms** | 10BASE-T1L single-pair Ethernet over umbilical, 1km reach |
| **Acoustic link** | Backup acoustic modem interface, 9kbps |
| **Power** | 375VDC subsea bus, isolated step-down |
| **Design life** | 25 years without intervention |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 140mm x 90mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, parylene coated for oil immersion |
| **Construction** | No electrolytics; oil-compatible components only |

## Compliance Targets
| Standard | Scope |
|---|---|
| API 17F | Subsea production control systems |
| IEC 61508 SIL 2 | Functional safety of shutdown paths |
| ISO 13628-6 | Subsea production control system design |
