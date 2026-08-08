# Airport Ground Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Airport ground infrastructure controller for airfield ground lighting, docking guidance, and apron surveillance. Individual lamp control and monitoring runs over a power-line carrier on the existing series circuit, avoiding the trenching that a parallel data network would require on a live airfield.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eAPT-900 | Airfield lighting control and monitoring | DIN rail |
| eAPT-VDGS | Visual docking guidance system | Gate-mounted IP66 |
| eAPT-APR | Apron surveillance sensor | Mast IP67 |

## Electrical Specifications — eAPT-900
| Parameter | Specification |
|---|---|
| **Controller** | TI AM6254 quad Cortex-A53 industrial SoC |
| **Lamp control** | Power-line carrier over 6.6A series circuit, 2048 fixtures |
| **Lamp monitoring** | Individual lamp fault detection within 2 seconds |
| **Docking sensor** | IWR6843AOP 60GHz mmWave, +/-5cm azimuth accuracy |
| **Aircraft typing** | Automatic recognition of 42 airframe profiles |
| **Interfaces** | Dual GbE ring, RS-485 x4, CAN FD x2, 32 dry contacts |
| **Redundancy** | Dual controller with 50ms failover |
| **Environment** | -40degC to +70degC, IP66 field units |
| **Availability** | 99.99% with hot standby |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 180mm x 130mm |
| **Stackup** | Isolated mains section with 8mm creepage |
| **IPC Class** | Class 2 |
| **Finish** | ENIG, conformal coated |
| **Isolation** | 4kV reinforced between mains and logic |

## Compliance Targets
| Standard | Scope |
|---|---|
| ICAO Annex 14 Vol I | Aerodrome design and operations |
| FAA AC 150/5345-53 | Airport lighting equipment certification |
| IEC 61822 | Constant current regulators for aeronautical lighting |
| EN 61000-6-2 | Industrial immunity |
