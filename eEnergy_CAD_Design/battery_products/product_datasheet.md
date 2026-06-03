# Battery Products — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Capacity | Voltage | Standard |
|---|---|---|---|---|
| eBMS-100A | Battery management system 100A | — | 12–96V | IEC 62619 |
| eLiPack-10kWh | 10kWh LiFePO4 pack | 10kWh | 48V | UL 1973 |
| eESS-100kWh | 100kWh energy storage system | 100kWh | 400V | IEC 62933 |
| ePPS-5kW | Portable power station 5kW | 5kWh | 48V | IEC 62368-1 |
| eSBM-Smart | Smart battery module | 1kWh | 24V | IEC 62619 |

## Electrical Specifications — eBMS-100A
| Parameter | Specification |
|---|---|
| **MCU** | STM32G474 (motor control grade, high-res ADC) |
| **Cell monitoring** | Analog Devices LTC6813 (18-cell, 16-bit) |
| **Current sensing** | INA3221 + shunt 1mΩ, ±100A |
| **Balancing** | Active balancing, 500mA per cell |
| **Protection** | OVP, UVP, OCP, OTP, SCP (<1µs) |
| **Communication** | CAN FD, SMBus, RS-485, BLE |
| **Accuracy** | ±1mV cell voltage, ±0.1°C temperature |
