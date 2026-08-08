# Launch Vehicle Avionics — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Launch vehicle flight computer handling guidance, navigation and control from lift-off through payload separation, with an independent autonomous flight termination system on a physically separate board and power domain. Sized for small-lift vehicles with ascent phases under twelve minutes.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eLV-500 | Guidance, navigation and control computer | Ring-mounted 6U |
| eLV-AFTS | Autonomous flight termination unit | Independent 3U |
| eLV-SEQ | Stage sequencing and pyro control | 3U |

## Electrical Specifications — eLV-500
| Parameter | Specification |
|---|---|
| **GNC processor** | GR712RC dual-core LEON3FT, radiation tolerant |
| **Sequencing logic** | AMD Xilinx Artix-7 XC7A100T |
| **Navigation** | ADIS16505 IMU triad + ZED-F9P GNSS, tightly coupled |
| **Update rate** | 200Hz navigation, 50Hz guidance |
| **Termination** | Independent AFTS with dissimilar processor and battery |
| **Pyro channels** | 16 initiator channels, dual-arm interlocked |
| **Telemetry** | S-band 2.2GHz, 2Mbps PCM downlink |
| **Vibration** | Qualified to 14.1 Grms random per NASA-STD-7001 |
| **Power** | 28VDC from vehicle battery, hot-redundant |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 233mm x 220mm (6U) |
| **Stackup** | Symmetric with isolated pyro return plane |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, staked and bonded for vibration |
| **Connector** | MIL-DTL-38999 Series III |

## Compliance Targets
| Standard | Scope |
|---|---|
| RCC 319-19 | Flight termination systems commonality standard |
| AFSPCMAN 91-710 | Range safety user requirements |
| NASA-STD-7001 | Payload vibroacoustic test criteria |
| MIL-STD-1576 | Electroexplosive subsystem safety |
