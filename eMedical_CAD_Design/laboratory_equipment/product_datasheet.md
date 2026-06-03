# Laboratory Equipment — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Function | Standard |
|---|---|---|
| ePCR-96 | Real-time PCR 96-well | ISO 15189 |
| eCentri-24K | Microcentrifuge 24,000 RPM | IEC 61010-2-020 |
| eSeq-Nano | Portable DNA sequencer | ISO 15189 |
| eSpec-UV | UV-Vis Spectrometer | ISO 15189 |
| eLab-Auto | Lab automation robot | ISO 13485 |

## Electrical Specifications — ePCR-96
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3 + Raspberry Pi CM4 (data processing) |
| **Thermal control** | Peltier TEC modules × 4, PID control |
| **Temperature accuracy** | ±0.1°C |
| **Ramp rate** | 6°C/s heating, 4°C/s cooling |
| **Fluorescence** | 4-channel optical detection (FAM, HEX, ROX, Cy5) |
| **Connectivity** | Ethernet, USB-C, Wi-Fi |
