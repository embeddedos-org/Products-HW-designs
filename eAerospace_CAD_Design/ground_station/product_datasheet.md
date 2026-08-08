# Satellite Ground Station — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Software-defined satellite ground station modem covering VHF through S-band, with CCSDS-compliant framing, Doppler-corrected tracking, and antenna rotator control. A Zynq UltraScale+ MPSoC runs the demodulation chain in fabric while the application processor handles pass scheduling and TLE propagation.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eGS-1200 | SDR baseband modem | 1U rackmount |
| eGS-RCU | Antenna rotator control unit | DIN rail |
| eGS-LNA | Low-noise front end | Mast-mounted IP67 |

## Electrical Specifications — eGS-1200
| Parameter | Specification |
|---|---|
| **RF transceiver** | ADRV9002 dual-channel, 30MHz-6GHz |
| **Baseband** | Zynq UltraScale+ XCZU3EG, quad Cortex-A53 + FPGA |
| **Frequency coverage** | VHF 144MHz, UHF 437MHz, S-band 2.2-2.4GHz |
| **Modulation** | BPSK, QPSK, OQPSK, GMSK, 8PSK |
| **Coding** | CCSDS convolutional, Reed-Solomon, turbo, LDPC |
| **Timing reference** | ZED-F9T GNSS-disciplined OCXO, 5ns to UTC |
| **Doppler tracking** | +/-60kHz closed-loop correction |
| **Data interface** | 10GbE SFP+, 1GbE management |
| **Rotator control** | Az/El via RS-485, 0.1 degree resolution |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 14 |
| **Dimensions** | 220mm x 180mm |
| **Stackup** | Rogers RO4350B RF layers over FR-4 core |
| **IPC Class** | Class 2 |
| **Finish** | ENIG with RF shielding cans |
| **Impedance** | 50 ohm single-ended, 100 ohm differential |

## Compliance Targets
| Standard | Scope |
|---|---|
| CCSDS 131.0-B-4 | TM synchronisation and channel coding |
| ITU-R SA.1810 | Earth station spurious emission limits |
| EN 301 489-1 | EMC for radio equipment |
| IEC 62368-1 | Audio/video and IT equipment safety |
