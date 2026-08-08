# Embedded Vision Processing — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Multi-camera embedded vision processor handling ISP, rectification, and detection across four synchronised global-shutter sensors. Hardware frame synchronisation keeps inter-camera skew under 1us, which is what makes the stereo and structured-light modes usable on moving subjects.

## Electrical Specifications — eVIS-600
| Parameter | Specification |
|---|---|
| **Processor** | NXP i.MX 8M Plus with 2.3-TOPS NPU |
| **Camera inputs** | 4x MIPI CSI-2, 2.3MP global shutter, hardware synchronised |
| **Frame sync skew** | <1us inter-camera |
| **ISP** | Hardware debayer, lens correction, HDR fusion, tone mapping |
| **Detection** | 30fps object detection at 1920x1080 |
| **Illumination** | Synchronised 850nm IR strobe, IEC 62471 Risk Group 1 |
| **Output** | 1GbE with GigE Vision, USB 3.0, H.265 encode |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 100mm x 80mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Impedance-controlled 100 ohm differential MIPI lanes |

## Compliance Targets
| Standard | Scope |
|---|---|
| IEC 62471 | Photobiological safety of the IR illuminator |
| EN 55032 Class B | Emissions |
| IEC 62368-1 | Equipment safety |
