# Propulsion Control Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Propulsion control unit for liquid bipropellant engines and electric thrusters, closing loops on chamber pressure, valve position, and mixture ratio. Handles throttle authority, ignition sequencing, and thermal margin protection, with hardware interlocks that inhibit ignition independently of software state.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| ePCU-700 | Liquid engine controller | Conduction-cooled 3U |
| ePCU-EP | Electric propulsion PPU controller | 3U |
| ePCU-RCS | Reaction control thruster driver | Compact 120x100mm |

## Electrical Specifications — ePCU-700
| Parameter | Specification |
|---|---|
| **Controller** | STM32H743 Cortex-M7, dual redundant |
| **Sensing** | ADS131M08 24-bit simultaneous ADC, 8 channels |
| **Pressure inputs** | 8x 4-20mA, 0.05% FS accuracy |
| **Thermocouples** | 12x Type-K via MAX31865 conditioning |
| **Valve drive** | 6x proportional solenoid, 0-5A PWM current control |
| **Ignition** | Dual-arm hardware interlock, software cannot bypass |
| **Loop rate** | 1kHz pressure control, 10kHz valve current |
| **Interfaces** | MIL-STD-1553B, CAN FD x2, RS-485 |
| **Environment** | -40degC to +85degC, 20 Grms random |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 160mm x 100mm (3U Eurocard) |
| **Stackup** | Isolated analogue island, 2oz power planes |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Cooling** | Conduction-cooled to wedge locks |

## Compliance Targets
| Standard | Scope |
|---|---|
| DO-254 Level B | Airborne electronic hardware design assurance |
| ECSS-E-ST-35C | Space engineering propulsion |
| IEC 61508 SIL 2 | Functional safety of the ignition interlock |
| MIL-STD-461G | Conducted and radiated emissions |
