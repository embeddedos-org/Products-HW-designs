# Civic Sensing Networks — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Multi-parameter urban sensing node measuring air quality, noise, temperature and pedestrian flow on street furniture. Sensor drift over a multi-year deployment is the main data quality risk, so each node carries a reference channel for periodic in-situ recalibration.

## Electrical Specifications — eCS-200
| Parameter | Specification |
|---|---|
| **Controller** | STM32U575 Cortex-M33 |
| **Air quality** | PM1/2.5/4/10, CO2, NO2, ozone and VOC |
| **Noise** | Class 2 sound level, LAeq and third-octave bands |
| **Pedestrian flow** | 60GHz radar counting, no imagery captured |
| **Drift management** | Reference channel for in-situ recalibration |
| **Communications** | LoRaWAN with NB-IoT fallback |
| **Power** | Solar with 14-day autonomy, or PoE where available |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 140mm x 100mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG, conformal coated |
| **Construction** | Sensor chamber isolated from board self-heating |

## Compliance Targets
| Standard | Scope |
|---|---|
| ISO 37122 | Sustainable cities indicators for smart cities |
| IEC 61672-1 Class 2 | Sound level meter performance |
| ETSI EN 300 220 | Sub-GHz short-range devices |
