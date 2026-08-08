# Naval Combat Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Shipboard combat management processing node handling sensor fusion, track management, and weapon assignment across a distributed naval network. Built for the shock, vibration and power-quality environment of MIL-STD-1399 shipboard service, with conduction cooling and no rotating media.

## Electrical Specifications — eNAV-5000
| Parameter | Specification |
|---|---|
| **Processor** | Zynq UltraScale+ XCZU3EG, quad Cortex-A53 + FPGA |
| **Network** | Dual redundant 10GbE, IEEE 1588 PTP synchronised |
| **Track capacity** | 4000 simultaneous tracks, 50Hz update |
| **Shipboard power** | 440VAC 60Hz 3-phase and 28VDC per MIL-STD-1399-300 |
| **Shock** | MIL-S-901D Grade A, Class I heavyweight |
| **Cooling** | Conduction-cooled, no fans or rotating media |
| **Environment** | MIL-STD-810H, salt fog per Method 509 |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 233mm x 160mm (3U VPX) |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated per IPC-CC-830 |
| **Connector** | VPX VITA 46 with wedge locks |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-1399-300 | Shipboard electrical power interface |
| MIL-S-901D | Shock test for shipboard machinery |
| MIL-STD-461G | Electromagnetic interference control |
