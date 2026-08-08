# Speech and Audio Front Ends — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Far-field voice front end running beamforming, echo cancellation and on-device keyword spotting across an eight-microphone array. Wake-word detection stays local so no audio leaves the device until the wake word fires, which is a privacy property rather than only a bandwidth one.

## Electrical Specifications — eSPX-300
| Parameter | Specification |
|---|---|
| **Processor** | STM32U575 Cortex-M33 with DSP extensions |
| **Microphone array** | 8-element circular, 65mm radius |
| **Beamforming** | Adaptive MVDR, 360-degree steering |
| **Echo cancellation** | Full-duplex AEC, 40dB ERLE |
| **Wake word** | On-device, <2% false reject at 0.1 FA/hour |
| **Far-field range** | 5m at 65 dB SPL ambient |
| **Privacy** | Audio never leaves the device before wake-word detection |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 140mm diameter circular |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Constraint** | Acoustically isolated microphone mounting, no ground loops |

## Compliance Targets
| Standard | Scope |
|---|---|
| EN 301 489-1 | EMC for radio equipment |
| EN 55032 Class B | Emissions |
| IEC 62368-1 | Equipment safety |
