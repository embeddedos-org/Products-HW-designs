# GNSS Receiver Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Multi-constellation multi-band GNSS receiver with RTK and PPP correction support, tightly coupled inertial aiding, and interference detection. An ECP5 FPGA monitors the raw IF spectrum for jamming and spoofing signatures, so an attack is reported rather than silently degrading the position solution.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eGNSS-400 | RTK receiver with inertial aiding | 70x50mm module |
| eGNSS-400T | Timing receiver variant | 70x50mm module |
| eGNSS-ANT | Multi-band active antenna | Puck IP67 |

## Electrical Specifications — eGNSS-400
| Parameter | Specification |
|---|---|
| **Constellations** | GPS L1/L2/L5, Galileo E1/E5, GLONASS, BeiDou, QZSS |
| **Position accuracy** | 1cm + 1ppm horizontal with RTK fix |
| **Convergence** | <10s RTK, <30min PPP |
| **Update rate** | 20Hz position, 200Hz inertial-aided |
| **Inertial aiding** | ADIS16470 industrial IMU, tightly coupled |
| **Interference monitor** | ECP5 FPGA spectral analysis, jamming and spoofing flags |
| **Interfaces** | UART x2, USB 2.0, CAN FD, 1PPS, event capture |
| **Anti-spoofing** | Signal authentication via Galileo OSNMA |
| **Power** | 5V input, 1.1W typical with RTK active |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 100mm x 80mm |
| **Stackup** | Continuous RF ground under antenna feed |
| **IPC Class** | Class 3 |
| **Finish** | ENIG with RF shield can |
| **Impedance** | 50 ohm RF trace to antenna port |

## Compliance Targets
| Standard | Scope |
|---|---|
| DO-229F | GPS/SBAS airborne equipment MOPS |
| ETSI EN 303 413 | GNSS receiver radio equipment |
| DO-160G | Environmental qualification |
| EN 301 489-19 | EMC for GNSS receivers |
