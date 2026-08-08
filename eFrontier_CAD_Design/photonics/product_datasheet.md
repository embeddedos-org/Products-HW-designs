# Integrated Photonics Platforms — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Research

## Product Overview
Control and readout platform for photonic integrated circuits, driving lasers and electro-optic modulators while stabilising die temperature to millikelvin precision. Thermal stability dominates: a photonic resonator drifts roughly 10 GHz per kelvin, so the TEC loop is the real instrument.

## Electrical Specifications — ePHO-800
| Parameter | Specification |
|---|---|
| **Laser sources** | 4x 1550nm DFB, 40mW, individually TEC-stabilised |
| **Temperature stability** | +/-0.002degC at the photonic die |
| **Modulation** | 10 GHz lithium niobate electro-optic modulator drive |
| **Detection** | 8-channel InGaAs APD with 5.5GHz transimpedance |
| **Wavelength control** | Closed-loop to +/-1 pm via cavity feedback |
| **Optical power** | Monitored per channel, interlocked to IEC 60825-1 Class 1 |
| **Interfaces** | 10GbE data, USB control, external clock input |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 220mm x 180mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG |
| **Thermal** | Isolated TEC island with guarded sense routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 60825-1 | Laser product safety classification and interlocks |
| EN 61010-1 | Laboratory equipment safety |
| EN 61326-1 | EMC for measurement and control equipment |
