# Edge Inference Servers — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Edge inference server aggregating four accelerator modules behind a single 10GbE ingress, for sites that need on-premise model serving without a data-centre power or cooling envelope. Sized for a 250W cabinet budget so it can be deployed in existing telecom and retail enclosures.

## Electrical Specifications — eINF-4000
| Parameter | Specification |
|---|---|
| **Accelerators** | 4x Jetson Orin NX, 400 TOPS aggregate |
| **Ingress** | 10GbE SFP+ with load balancing across modules |
| **Model serving** | Concurrent multi-model, 40 streams at 30fps |
| **Memory** | 64GB aggregate LPDDR5 |
| **Storage** | 1TB NVMe model repository |
| **Power envelope** | 250W sustained, fits existing cabinet budgets |
| **Management** | Redfish-compatible out-of-band management |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 420mm x 300mm (1U backplane) |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Thermal** | Front-to-back forced air, 4x 40mm fans |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 62368-1 | Equipment safety |
| EN 55032 Class A | Emissions for commercial environments |
| EN 55035 | Immunity for multimedia equipment |
