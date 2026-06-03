# Industrial Sensors — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Sensor Type | Range | Interface | IP Rating |
|---|---|---|---|---|
| eTS-200 | Temperature (PT100 RTD) | -200°C to +850°C | 4-20mA / HART | IP67 |
| ePS-500 | Pressure (piezo) | 0–500 bar | 4-20mA / HART | IP68 |
| eVS-100 | Vibration (MEMS) | 0–100g | IO-Link / CAN | IP67 |
| eGS-400 | Gas (electrochemical) | 0–1000 ppm | Modbus RTU | IP65 |
| eFS-50 | Flow (ultrasonic) | 0–50 m/s | PROFIBUS DP | IP68 |

## Electrical Specifications — eTS-200
| Parameter | Specification |
|---|---|
| **MCU** | STM32L4R9 ARM Cortex-M4 @ 120MHz (ultra-low-power) |
| **ADC** | 24-bit sigma-delta (AD7124-8) |
| **Interface** | 4-20mA loop + HART 7 + IO-Link |
| **Power** | Loop-powered (4-20mA, 8–30VDC) |
| **Accuracy** | ±0.1°C |
| **EMC** | IEC 61000-4 series, ATEX Zone 2 |
