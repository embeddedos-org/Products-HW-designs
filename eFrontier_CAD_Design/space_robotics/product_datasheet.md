# Space Robotics Controllers — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Research

## Product Overview
Radiation-tolerant robotics controller for orbital manipulators and planetary rovers, closing joint control loops on harmonic-drive actuators with force feedback. Round-trip light time makes teleoperation impractical beyond cislunar distance, so contact detection and safing are handled entirely on board.

## Electrical Specifications — eSRB-900
| Parameter | Specification |
|---|---|
| **Processor** | GR712RC rad-hard dual-core LEON3FT |
| **Joint control** | 7 axes, 1 kHz position and torque loops |
| **Actuators** | Harmonic drive, 100:1, zero backlash |
| **Force feedback** | 6-axis force/torque sensing at the end effector |
| **Autonomy** | On-board contact detection and autonomous safing |
| **Radiation** | 50 krad(Si) total ionising dose target |
| **Thermal** | -120degC to +120degC survival, heater-managed operation |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 180mm x 140mm |
| **IPC Class** | Class 3/A per IPC-6012DS |
| **Finish** | Electroplated nickel-gold, staked and conformal coated |
| **Outgassing** | ASTM E595, TML < 1.0%, CVCM < 0.1% |

## Compliance Targets
| Standard | Scope |
|---|---|
| ECSS-Q-ST-60C | Space product assurance, EEE components |
| ECSS-E-ST-50-12C | SpaceWire interface |
| ECSS-E-ST-33-01C | Space mechanisms |
