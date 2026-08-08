# Smart Waste Management — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Bin-mounted fill level sensor reporting container state so collection routes follow actual demand rather than a fixed calendar. Time-of-flight sensing handles irregular waste surfaces better than ultrasonic, which is easily confused by soft or angled loads.

## Electrical Specifications — eWM-300
| Parameter | Specification |
|---|---|
| **Controller** | STM32L071 Cortex-M0+ ultra-low-power |
| **Fill sensing** | VL53L1X time-of-flight, 4 m range, 2 cm resolution |
| **Fire detection** | Temperature threshold with immediate alert |
| **Tilt detection** | Accelerometer for overturn and theft reporting |
| **Reporting** | LoRaWAN, 4 scheduled reports per day plus events |
| **Battery life** | 8 years on a single lithium primary cell |
| **Environment** | IP67, -30degC to +70degC, impact resistant |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 4 |
| **Dimensions** | 60mm x 45mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG, potted |
| **Construction** | Shock-mounted for lid-slam impact |

## Compliance Targets
| Standard | Scope |
|---|---|
| ETSI EN 300 220 | Sub-GHz short-range devices |
| IEC 60529 IP67 | Ingress protection |
| EN 61000-6-3 | Residential emissions |
