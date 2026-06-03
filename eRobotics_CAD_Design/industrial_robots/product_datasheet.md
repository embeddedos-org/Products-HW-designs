# Industrial Robots — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Payload | Reach | Repeatability |
|---|---|---|---|---|
| eArm-7 | 7-DOF collaborative robot | 10kg | 1.3m | ±0.02mm |
| eWeld-6 | 6-DOF welding robot | 8kg | 1.8m | ±0.05mm |
| eAssemble-4 | 4-DOF SCARA assembly | 5kg | 0.8m | ±0.01mm |
| ePick-Delta | Delta pick-and-place | 2kg | 0.6m | ±0.05mm |
| eCobot-5 | 5-DOF collaborative | 5kg | 0.9m | ±0.03mm |

## Electrical Specifications — eArm-7 Controller
| Parameter | Specification |
|---|---|
| **CPU** | NXP i.MX 8M Plus (quad Cortex-A53 + Cortex-M7) |
| **FPGA** | Xilinx XC7A100T (real-time servo control) |
| **Servo drives** | 7× integrated EtherCAT servo drives |
| **Encoders** | 7× 23-bit absolute encoders |
| **Safety** | ISO 10218-1, IEC 62061 SIL 2, PLe |
| **Communication** | EtherCAT, PROFINET, ROS 2 |
| **Power** | 48VDC, 2kW peak |
