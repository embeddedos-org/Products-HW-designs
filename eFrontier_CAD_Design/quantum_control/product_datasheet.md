# Quantum Control Electronics — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Research

## Product Overview
Room-temperature qubit control and readout electronics generating shaped microwave pulses and digitising dispersive readout for superconducting and trapped-ion platforms. Phase coherence across channels is the binding constraint, so every output shares one clock tree rather than being synchronised in software.

## Electrical Specifications — eQC-1000
| Parameter | Specification |
|---|---|
| **Control channels** | 16 arbitrary waveform outputs, 1 GSPS, 16-bit |
| **Readout channels** | 8 digitiser inputs, 500 MSPS, 16-bit |
| **Phase coherence** | <5 ps RMS skew across all channels |
| **Pulse shaping** | DRAG and derivative-corrected envelopes in fabric |
| **Latency** | <200 ns feedback from readout to conditional pulse |
| **Frequency range** | DC-8 GHz with external upconversion |
| **Cryostat interface** | Thermally anchored coax, 4K stage compatible |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 280mm x 200mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG with RF shielding cans |
| **Stackup** | Rogers RO4350B RF layers, phase-matched channel routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| EN 61010-1 | Laboratory measurement equipment safety |
| EN 55032 Class A | Emissions for commercial environments |
| EN 61326-1 | EMC for measurement and control equipment |
