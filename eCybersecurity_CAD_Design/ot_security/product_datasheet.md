# OT Security Appliances — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Operational technology security appliance performing passive protocol inspection and enforced segmentation for industrial networks. Deep packet inspection covers Modbus, DNP3, IEC 61850 and PROFINET, and the default deployment is passive tap so introducing it cannot itself halt a process line.

## Electrical Specifications — eOTS-800
| Parameter | Specification |
|---|---|
| **Processor** | TI AM6254 quad Cortex-A53 |
| **Protocols** | Modbus TCP/RTU, DNP3, IEC 61850 MMS/GOOSE, PROFINET, EtherNet/IP |
| **Deployment** | Passive tap, inline bridge, or enforced segmentation |
| **Asset discovery** | Passive fingerprinting of 6000 device profiles |
| **Anomaly detection** | Baseline process behaviour, deviation alerting |
| **Throughput** | 2 Gbps inspected at line rate |
| **Environment** | DIN rail, -40degC to +70degC, IEC 61850-3 target |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 160mm x 110mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Isolation** | Isolated serial field ports for surge survivability |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 62443-3-3 | System security requirements and security levels |
| IEC 61850-3 | Substation communication network robustness |
| EN 61000-6-2 | Industrial immunity |
