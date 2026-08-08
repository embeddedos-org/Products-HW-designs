# Ruggedised Computing Platforms — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Fanless ruggedised mission computer for vehicle, airborne and dismounted deployment. Conduction cooling through the chassis removes the fan as a failure point and lets the unit be sealed to IP67, at the cost of a lower sustained thermal envelope than an equivalent forced-air design.

## Electrical Specifications — eRGD-2000
| Parameter | Specification |
|---|---|
| **Processor** | NXP i.MX 8M Plus quad Cortex-A53 with 2.3-TOPS NPU |
| **Memory** | 8GB LPDDR4, 128GB eMMC with hardware encryption |
| **Cooling** | Fanless conduction to chassis, 45W sustained |
| **Interfaces** | 1GbE x4, USB 3.0 x4, CAN FD x2, RS-422 x4 |
| **Shock and vibration** | MIL-STD-810H Method 516.8 and 514.8 |
| **Power** | MIL-STD-1275E 28V with 50ms hold-up |
| **Ingress** | IP67 sealed, -40degC to +71degC operating |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 180mm x 140mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Thermal** | Copper coin under SoC for conduction path |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-810H | Environmental engineering considerations |
| MIL-STD-461G | Electromagnetic interference control |
| MIL-STD-1275E | 28V vehicle electrical power characteristics |
