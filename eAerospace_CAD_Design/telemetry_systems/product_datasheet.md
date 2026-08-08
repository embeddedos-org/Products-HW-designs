# Telemetry Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Airborne and range telemetry encoder that samples analogue and digital instrumentation into an IRIG 106 PCM stream, applies CCSDS framing and forward error correction, then transmits on S-band. Handles 256 analogue channels with per-channel programmable sample rates and IRIG-B time correlation.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eTLM-600 | PCM encoder and S-band transmitter | Conduction-cooled 3U |
| eTLM-DAU | Remote data acquisition unit | Compact 100x80mm |
| eTLM-GRX | Ground telemetry receiver | 1U rackmount |

## Electrical Specifications — eTLM-600
| Parameter | Specification |
|---|---|
| **Encoder** | AMD Xilinx Artix-7 XC7A100T, IRIG 106 Chapter 4 PCM |
| **Analogue inputs** | 256 channels, 16-bit, up to 10kSPS per channel |
| **Digital inputs** | 128 discrete, 32 differential serial |
| **Bus monitoring** | MIL-STD-1553B, ARINC-429, CAN FD |
| **Aggregate rate** | 20Mbps PCM output |
| **Coding** | CCSDS Reed-Solomon (255,223), rate-1/2 convolutional |
| **Transmitter** | S-band 2.2-2.4GHz, 10W, SOQPSK-TG |
| **Time correlation** | IRIG-B AM and DCLS, 1us to UTC |
| **Environment** | DO-160G Cat. D, 20 Grms random |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 160mm x 100mm (3U Eurocard) |
| **Stackup** | Segregated analogue acquisition island |
| **IPC Class** | Class 3 |
| **Finish** | ENIG, conformal coated |
| **Connector** | MIL-DTL-38999 Series III |

## Compliance Targets
| Standard | Scope |
|---|---|
| IRIG 106-22 | Telemetry standards, Range Commanders Council |
| CCSDS 131.0-B-4 | TM synchronisation and channel coding |
| DO-160G | Environmental qualification |
| MIL-STD-461G | Conducted and radiated emissions |
