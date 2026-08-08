# SLAM Compute Modules — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Visual-inertial SLAM compute module for robots and handheld scanners, running feature extraction, loop closure and dense mapping on board. A hardware-synchronised stereo pair and IMU keep visual-inertial initialisation robust, which is where most SLAM stacks fail first in low-texture spaces.

## Electrical Specifications — eSLM-700
| Parameter | Specification |
|---|---|
| **Processor** | NVIDIA Jetson Orin Nano 8GB, 40 TOPS |
| **Visual input** | Hardware-synchronised stereo, 2.3MP global shutter |
| **Lidar** | RPLIDAR S3 40m 360-degree scanner |
| **Inertial** | ADIS16470 industrial IMU, hardware time-stamped |
| **Map scale** | 500m x 500m dense, 2cm voxel resolution |
| **Loop closure** | Bag-of-words with 50k vocabulary, <200ms |
| **Relocalisation** | <1s from cold start in a known map |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 100mm x 80mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Impedance-controlled MIPI and PCIe routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| FCC Part 15 Subpart B | Unintentional radiator emissions |
| EN 55032 Class B | Emissions |
| IEC 62368-1 | Equipment safety |
