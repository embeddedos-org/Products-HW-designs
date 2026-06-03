# Avionics Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Full-stack avionics suite including flight computers, navigation systems, air data computers, flight displays, communication radios, transponders, weather radar, and terrain awareness systems — all running eOS.

## Avionics Suite Components

| Unit | Function | Form Factor |
|---|---|---|
| eFC-1000 | Primary Flight Computer | 3U VPX |
| eNAV-500 | Navigation / FMS | 3U VPX |
| eADC-200 | Air Data Computer | ARINC 600 |
| eFD-1080 | Flight Display (1080p) | 10.4" Panel |
| eCOM-400 | VHF/UHF Comm Radio | ARINC 600 |
| eXPDR-1090 | Mode-S ADS-B Transponder | ARINC 600 |

## Electrical Specifications — eFC-1000
| Parameter | Specification |
|---|---|
| **SoC** | Rockchip RK3588S (6-core ARM + 32-TOPS NPU) |
| **RTOS Co-processor** | STM32H7B3 (dual redundant) |
| **Memory** | 8GB LPDDR5 + 64GB eMMC |
| **Interfaces** | ARINC-429 ×16, CAN FD ×4, MIL-STD-1553B ×2, Ethernet ×4 |
| **Power** | 28VDC MIL-STD-704F |
| **DO-178C** | Level A certified software |
| **DO-254** | Level A certified hardware |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 233mm × 160mm (3U VPX) |
| **IPC Class** | Class 3 / DO-254 Level A |
| **Connector** | VPX VITA 46 |
