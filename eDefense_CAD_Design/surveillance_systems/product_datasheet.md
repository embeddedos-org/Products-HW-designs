# Surveillance Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Resolution | Range | Standard |
|---|---|---|---|---|
| eEO-4K | Electro-optical camera | 4K UHD | 10km | MIL-STD-810H |
| eTIR-640 | Thermal IR camera | 640×512 LWIR | 5km | MIL-STD-810H |
| eISR-Pro | ISR payload (EO+IR+LRF) | 4K + 640 LWIR | 15km | MIL-STD-810H |
| eRecon-UAV | Reconnaissance drone | — | 200km | MIL-STD-810H |

## Electrical Specifications — eEO-4K
| Parameter | Specification |
|---|---|
| **SoC** | Rockchip RK3588S + Xilinx XC7A100T FPGA |
| **Image sensor** | Sony IMX585 4K BSI CMOS |
| **Stabilization** | 3-axis gimbal, ±0.01° accuracy |
| **Video output** | H.265 4K@60fps, encrypted AES-256 |
| **Communication** | Encrypted 4G LTE + SATCOM backup |
| **Power** | 28VDC MIL-STD-704F |
| **Environmental** | MIL-STD-810H Method 501-510 |
| **EMC** | MIL-STD-461G |
