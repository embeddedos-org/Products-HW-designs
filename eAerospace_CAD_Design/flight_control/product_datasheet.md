# Flight Control Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Triplex-redundant fly-by-wire flight control computer executing control laws for primary and secondary surfaces. Three dissimilar lanes vote on every actuator command, with a fourth monitor lane arbitrating disagreement. Each lane runs an independently compiled eOS RTOS image so a coding fault cannot propagate across the redundancy set.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eFCS-2000 | Primary flight control computer | 3U VPX |
| eFCS-2000M | Monitor and arbitration lane | 3U VPX |
| eACE-400 | Actuator control electronics | ARINC 600 |

## Electrical Specifications — eFCS-2000
| Parameter | Specification |
|---|---|
| **Architecture** | Triplex dissimilar lanes + independent monitor |
| **Lane processor** | STM32H743 Cortex-M7 at 480MHz, lockstep pair |
| **I/O management** | AMD Xilinx Artix-7 XC7A100T |
| **Inertial reference** | ADIS16505-2 tactical IMU, 0.4deg/hr bias stability |
| **Control loop rate** | 400Hz outer loop, 2kHz actuator inner loop |
| **Interfaces** | ARINC-429 x8, MIL-STD-1553B x2, CAN FD x4, 10BASE-T1L x2 |
| **Power** | 28VDC per MIL-STD-704F, dual-bus with hold-up |
| **Environment** | DO-160G Cat. D, -55degC to +85degC |
| **Design assurance** | DO-178C Level A software, DO-254 Level A hardware |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 233mm x 160mm (3U VPX) |
| **Stackup** | Sig/Gnd/Sig/Pwr symmetric, 50 ohm single-ended |
| **IPC Class** | Class 3 / DO-254 Level A |
| **Finish** | ENIG, conformal coated per IPC-CC-830 |
| **Connector** | VPX VITA 46 |

## Compliance Targets
| Standard | Scope |
|---|---|
| DO-254 Level A | Airborne electronic hardware design assurance |
| DO-178C Level A | Control law and RTOS software |
| DO-160G | Environmental qualification |
| MIL-STD-704F | Aircraft electrical power characteristics |
