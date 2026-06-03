# Robot Components — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Key Spec | Interface |
|---|---|---|---|
| eServo-200 | EtherCAT servo drive 200W | 200W, 48V, 5A | EtherCAT |
| eActuator-50 | Linear actuator 50mm | 50mm stroke, 500N | CAN FD |
| eGripper-3F | 3-finger adaptive gripper | 80mm span, 50N | RS-485 |
| eVision-4K | Robot vision system | 4K stereo + depth | GbE |
| eLiDAR-360 | 360° solid-state LiDAR | 100m range, 0.1° res | Ethernet |

## Electrical Specifications — eServo-200
| Parameter | Specification |
|---|---|
| **MCU** | STM32G474 (FOC motor control) |
| **FPGA** | Lattice ECP5 (EtherCAT slave) |
| **Power stage** | 3-phase MOSFET bridge, 48V/5A |
| **Encoder** | 23-bit absolute (EnDat 2.2) |
| **Current loop** | 20kHz bandwidth |
| **Position accuracy** | ±0.01° |
| **Communication** | EtherCAT CoE (CiA 402) |
