# Satellite Platform Avionics — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Radiation-hardened satellite platform computer for LEO and GEO buses, handling attitude determination and control, telemetry and telecommand, power management, and payload data routing. Built on a dual-core LEON3FT processor with an EDAC-protected memory subsystem and SpaceWire fabric to the payload.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eSAT-8000 | Platform on-board computer | Eurocard 6U |
| eSAT-PCU | Power conditioning and distribution unit | Eurocard 6U |
| eSAT-RIU | Remote interface unit | Eurocard 3U |

## Electrical Specifications — eSAT-8000
| Parameter | Specification |
|---|---|
| **Processor** | GR712RC dual-core LEON3FT SPARC V8, 100MHz |
| **Reconfigurable logic** | Microchip RTG4 RT4G150 rad-tolerant flash FPGA |
| **Memory** | 2GB DDR4 with Reed-Solomon EDAC, 256kbit MRAM for critical state |
| **Payload fabric** | SpaceWire x8 at 200Mbps per ECSS-E-ST-50-12C |
| **Platform bus** | MIL-STD-1553B dual redundant, CAN FD x2 |
| **Total ionising dose** | 100 krad(Si) target |
| **Single-event latch-up** | Immune to 60 MeV-cm2/mg |
| **Power** | 28V unregulated bus, 100W platform allocation |
| **Design life** | 15 years GEO / 7 years LEO |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 233mm x 220mm (6U Eurocard) |
| **Stackup** | Buried-via symmetric, polyimide substrate |
| **IPC Class** | Class 3/A per IPC-6012DS space addendum |
| **Finish** | Electroplated nickel-gold, staked and conformal coated |
| **Outgassing** | ASTM E595, TML < 1.0%, CVCM < 0.1% |

## Compliance Targets
| Standard | Scope |
|---|---|
| ECSS-Q-ST-60C | Space product assurance, EEE components |
| ECSS-E-ST-50-12C | SpaceWire links, nodes, routers and networks |
| ECSS-E-ST-10-03C | Space engineering testing |
| MIL-STD-883 | Microcircuit test methods and screening |
