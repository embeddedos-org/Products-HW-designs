# Disaster Management Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Disaster early-warning node monitoring seismic, hydrological and meteorological precursors and issuing Common Alerting Protocol messages over independent paths. Alert delivery uses satellite as well as terrestrial links because the terrestrial network is often the first casualty of the event being warned about.

## Electrical Specifications — eDIS-600
| Parameter | Specification |
|---|---|
| **Controller** | STM32U575 Cortex-M33 ultra-low-power |
| **Sensing** | 3-axis seismic accelerometer, water level, rainfall, wind |
| **Detection** | P-wave arrival within 1.2 s of onset |
| **Alerting** | CAP 1.2 messages over LoRa, cellular and satellite |
| **Independence** | Satellite path survives terrestrial network loss |
| **Power** | Solar with 5-day autonomy, 10-year design life |
| **Environment** | IP68, -40degC to +70degC, flood submersible |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 120mm x 90mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, potted |
| **Construction** | No electrolytics; ceramic only for 10-year life |

## Compliance Targets
| Standard | Scope |
|---|---|
| ITU-T X.1303 | Common alerting protocol |
| WMO No. 8 | Meteorological instrument measurement guidance |
| ETSI EN 300 220 | Sub-GHz short-range devices |
