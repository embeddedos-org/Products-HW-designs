# UAV & Drone Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Full family of UAV platforms: fixed-wing long-endurance ISR drones, multirotor inspection drones, VTOL cargo drones, and swarm coordination modules — all running eOS AeroOS.

## Product Family

| Model | Type | Payload | Endurance | Range |
|---|---|---|---|---|
| eFW-1000 | Fixed-wing ISR | 2kg | 8h | 200km |
| eMR-400 | Multirotor inspection | 1kg | 45min | 10km |
| eVT-5000 | VTOL cargo | 5kg | 2h | 50km |
| eGCS-100 | Ground Control Station | — | — | 200km |
| eSwarm-10 | Swarm coordinator | — | — | 5km mesh |

## Electrical Specifications — eFW-1000 Flight Controller
| Parameter | Specification |
|---|---|
| **MCU** | Rockchip RK3588S + STM32H7B3 (dual) |
| **Navigation** | u-blox ZED-F9P RTK GPS (dual) + Epson G362P IMU |
| **Comms** | 900MHz LoRa + 5.8GHz video + 4G LTE backup |
| **Vision** | Sony IMX678 4K × 3 cameras |
| **LiDAR** | Livox Mid-360 solid-state |
| **Power** | 4S–6S LiPo (14.8V–22.2V) |
| **DO-178C** | Level C (commercial UAV) |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 100mm × 70mm |
| **IPC Class** | Class 3 |
| **Surface finish** | ENIG |
