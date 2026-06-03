# Surgical Devices — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Advanced surgical device portfolio: robotic surgical system, electrosurgical generator, endoscopic imaging system, and surgical navigation system — all running eOS Medical.

## Product Family

| Model | Function | DOF | Standard |
|---|---|---|---|
| eSurgBot-7 | 7-DOF surgical robot arm | 7 | IEC 60601-2-77 |
| eESG-400 | Electrosurgical generator 400W | — | IEC 60601-2-2 |
| eEndo-4K | 4K endoscopic camera | — | IEC 60601-1 |
| eSurgNav-3D | 3D surgical navigation | — | IEC 60601-2-10 |

## Electrical Specifications — eSurgBot-7
| Parameter | Specification |
|---|---|
| **Controller** | Rockchip RK3588S + FPGA Xilinx XC7A100T |
| **Actuators** | 7× Maxon EC-i 40 brushless DC motors |
| **Encoders** | 7× Renishaw RESA absolute encoders |
| **Force sensing** | ATI Mini45 6-DOF F/T sensor |
| **Latency** | <1ms control loop (real-time eOS) |
| **Safety** | IEC 62061 SIL 2, dual-channel safety relay |
| **Power** | 48VDC, 800W peak |
