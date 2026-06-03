# Power Electronics — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Power | Standard |
|---|---|---|---|
| eDCDC-5kW | Bidirectional DC-DC converter 5kW | 5kW | IEC 62477-1 |
| eUPS-10kVA | Online UPS 10kVA | 10kVA | IEC 62040-1 |
| eMotorDrive-22kW | Variable frequency drive 22kW | 22kW | IEC 61800-5-1 |
| ePDU-Smart | Smart power distribution unit | 32A | IEC 60309 |
| eBreaker-Smart | Smart circuit breaker | 63A | IEC 60898-1 |

## Electrical Specifications — eDCDC-5kW
| Parameter | Specification |
|---|---|
| **MCU** | STM32H7B3 + TMS320F28379D DSP |
| **Topology** | Dual active bridge (DAB), SiC MOSFETs |
| **Input** | 200–800VDC |
| **Output** | 48–400VDC (adjustable) |
| **Efficiency** | 98.2% peak |
| **Isolation** | 4kV galvanic isolation |
| **Communication** | CAN FD, Modbus RTU, CANopen |
