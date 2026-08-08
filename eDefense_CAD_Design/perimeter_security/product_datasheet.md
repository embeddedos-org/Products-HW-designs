# Perimeter Security Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Perimeter intrusion detection system fusing fibre-optic fence disturbance sensing, mmWave zone radar and video assessment across sites of up to 20km. Distinguishing wind and wildlife from genuine climb or cut events is what determines whether an operator keeps trusting the alarms.

## Electrical Specifications — ePER-700
| Parameter | Specification |
|---|---|
| **Controller** | STM32H743 Cortex-M7 zone processor |
| **Fibre sensing** | Distributed acoustic sensing, 20km per controller, 5m resolution |
| **Zone radar** | IWR6843AOP 60GHz, 120m coverage per unit |
| **Classification** | Climb, cut, lean and tunnel discrimination |
| **Nuisance rejection** | Wind, rain and wildlife filtering with local weather input |
| **Integration** | ONVIF Profile S video, Modbus TCP, dry contacts |
| **Environment** | IP66, -40degC to +70degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 160mm x 120mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG, conformal coated |
| **Isolation** | Isolated field interfaces for lightning survivability |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 62676 | Video surveillance systems for security |
| EN 50131 Grade 4 | Alarm systems intrusion detection |
| EN 61000-6-2 | Industrial immunity |
