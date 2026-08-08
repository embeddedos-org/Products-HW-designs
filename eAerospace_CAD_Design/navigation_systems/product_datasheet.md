# Inertial Navigation Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Tactical-grade inertial navigation system providing a continuous position solution through GNSS outage, blending a triad of tactical IMUs with barometric, magnetic, and optional odometry aiding in an error-state Kalman filter. Drift is specified at under 1.5 nautical miles per hour of free inertial operation.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eINS-900 | Tactical inertial navigation system | 120x100x60mm |
| eINS-900L | Reduced-size variant for UAV | 80x70x40mm |
| eINS-AHRS | Attitude and heading reference only | 60x50x25mm |

## Electrical Specifications — eINS-900
| Parameter | Specification |
|---|---|
| **Inertial sensors** | 3x ADIS16505-2, 0.4deg/hr in-run bias stability |
| **Free inertial drift** | <1.5 nmi/hr CEP, 50% probability |
| **Attitude accuracy** | 0.05deg roll/pitch, 0.1deg heading (GNSS-aided) |
| **Filter** | 24-state error-state extended Kalman filter |
| **Aiding** | GNSS, barometric, magnetic, odometry, air data |
| **Update rate** | 200Hz navigation solution, 2kHz IMU sampling |
| **Alignment** | 60s coarse, 300s fine gyrocompass alignment |
| **Interfaces** | ARINC-429, MIL-STD-1553B, RS-422, CAN FD, Ethernet |
| **Environment** | DO-160G Cat. D, -40degC to +71degC |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 10 |
| **Dimensions** | 110mm x 90mm |
| **Stackup** | Isolated IMU mounting island, thermally symmetric |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Mechanical** | Machined aluminium housing, vibration isolated |

## Compliance Targets
| Standard | Scope |
|---|---|
| DO-334 | Airborne navigation sensors MOPS |
| STANAG 4572 | Standard interfaces for inertial navigation |
| DO-160G | Environmental qualification |
| MIL-STD-810H | Environmental engineering considerations |
