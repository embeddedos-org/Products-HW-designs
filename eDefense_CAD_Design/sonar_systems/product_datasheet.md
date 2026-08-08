# Sonar Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Multi-channel sonar processing unit performing beamforming, matched filtering and classification for hull-mounted, towed-array and dipping sonar. A 64-element array is digitised at the wet end and beamformed in FPGA fabric, so array gain is not lost to analogue cable runs.

## Electrical Specifications — eSON-2400
| Parameter | Specification |
|---|---|
| **Processor** | Zynq UltraScale+ XCZU3EG, beamforming in fabric |
| **Channels** | 64 hydrophone elements, simultaneous sampling |
| **Bandwidth** | 1kHz-100kHz, active and passive modes |
| **Dynamic range** | 120 dB with 24-bit acquisition |
| **Beamforming** | Time-domain delay-and-sum, 256 simultaneous beams |
| **Classification** | Spectrogram-based, DEMON and LOFAR analysis |
| **Transmit** | 4-channel projector drive, 2kW peak |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 233mm x 160mm (3U VPX) |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Stackup** | Segregated analogue acquisition island |

## Compliance Targets
| Standard | Scope |
|---|---|
| STANAG 1170 | NATO underwater acoustic equipment |
| IEC 60565 | Hydrophone calibration |
| MIL-STD-461G | Electromagnetic interference control |
