# Border Security Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Solar-powered unattended ground sensor for border and perimeter monitoring, combining seismic, magnetic, passive infrared and mmWave sensing to classify crossings as personnel, vehicle or livestock. Designed to run for five years without a site visit, which puts every design decision behind the power budget.

## Electrical Specifications — eBRD-600
| Parameter | Specification |
|---|---|
| **Controller** | STM32U575 Cortex-M33 ultra-low-power secure MCU |
| **Sensing** | Seismic geophone, magnetometer, PIR, 60GHz mmWave |
| **Classification** | On-device TinyML, personnel / vehicle / animal |
| **False alarm rate** | <1 per sensor per week in field trials target |
| **Communications** | LoRa mesh 868/915MHz, 8km range, satellite backhaul |
| **Power** | 5W solar with 3.6Ah lithium buffer, 5-year design life |
| **Environment** | IP68, buried or staked, -40degC to +70degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 6 |
| **Dimensions** | 90mm x 60mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, potted for burial |
| **Construction** | No electrolytics; ceramic only for 5-year life |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 62676 | Video surveillance systems for security |
| MIL-STD-810H | Environmental engineering considerations |
| ETSI EN 300 220 | Sub-GHz short-range devices |
