# Infrastructure Equipment — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Function | Standard |
|---|---|---|
| eSM-3P | 3-phase smart electricity meter | IEC 62056, ANSI C12 |
| eWM-DN50 | DN50 ultrasonic water meter | ISO 4064 |
| eAQ-Pro | Air quality monitor (PM2.5, CO2, VOC) | EN 15267 |
| ePL-500 | Pipeline leak detection sensor | API 1130 |
| eGM-100 | Smart gas meter | EN 1359 |

## Electrical Specifications — eSM-3P Smart Electricity Meter
| Parameter | Specification |
|---|---|
| **MCU** | STM32L4R9 (metering) + STM32WL55 (LPWAN) |
| **Metering IC** | ADE9153A 3-phase energy metering |
| **Accuracy** | Class 0.2S (IEC 62052-11) |
| **Communication** | DLMS/COSEM, OFDM PLC, NB-IoT, LoRaWAN |
| **Display** | 6-digit LCD |
| **Tamper detection** | Magnetic, tilt, cover open |
| **Power** | 230VAC mains + 3.6V lithium backup |
