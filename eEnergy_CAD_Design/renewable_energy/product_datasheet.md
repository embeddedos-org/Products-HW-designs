# Renewable Energy Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Power | Standard |
|---|---|---|---|
| eSolarInv-10kW | String solar inverter 10kW | 10kW | IEC 61727, IEEE 1547 |
| eSolarTracker | Dual-axis solar tracker | — | IEC 61215 |
| eWindCtrl-50kW | Wind turbine controller 50kW | 50kW | IEC 61400-1 |
| eMicrogrid-100 | Microgrid controller 100kW | 100kW | IEEE 2030.7 |
| eSCC-60A | Solar charge controller 60A | 60A MPPT | IEC 62509 |

## Electrical Specifications — eSolarInv-10kW
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3 (dual) + TMS320F28379D DSP |
| **MPPT** | 4-channel, 99.5% efficiency |
| **Inverter topology** | 3-phase H-bridge, SiC MOSFETs |
| **Grid connection** | IEEE 1547-2018, anti-islanding |
| **Communication** | Modbus TCP, SunSpec, Wi-Fi, 4G |
| **Efficiency** | 98.6% peak (CEC weighted) |
| **THD** | <3% |
