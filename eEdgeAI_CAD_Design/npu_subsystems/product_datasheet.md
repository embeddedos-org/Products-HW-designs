# NPU Subsystems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
FPGA-implemented neural processing fabric for workloads whose dataflow does not map well onto a fixed-function NPU — sparse models, unusual quantisation, or operators a vendor toolchain will not lower. Trades peak TOPS for the ability to change the datapath after tape-out is no longer an option.

## Electrical Specifications — eNPU-800
| Parameter | Specification |
|---|---|
| **Fabric** | Zynq UltraScale+ XCZU3EG, systolic array in PL |
| **Throughput** | 4.2 TOPS INT8 at 300MHz fabric clock |
| **Precision** | INT4, INT8, INT16 and bfloat16 datapaths |
| **Memory bandwidth** | 19.2 GB/s to LPDDR4 |
| **Toolchain** | eAI compiler lowering ONNX to fabric microcode |
| **Reconfiguration** | Partial reconfiguration, 40ms datapath swap |
| **Host interface** | PCIe Gen2 x4 or 1GbE |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 120mm x 90mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Length-matched LPDDR4 fly-by, back-drilled PCIe |

## Compliance Targets
| Standard | Scope |
|---|---|
| FCC Part 15 Subpart B | Unintentional radiator emissions |
| EN 55032 Class A | Multimedia equipment emissions |
| IEC 62368-1 | Equipment safety |
