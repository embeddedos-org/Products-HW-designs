# Tactical Communications — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Frequency | Range | Standard |
|---|---|---|---|---|
| eTR-5000 | Tactical software-defined radio | 30MHz–2GHz | 50km | MIL-STD-188-181C |
| eSCT-200 | Secure communication terminal | — | SATCOM | NSA Type 1 |
| eMesh-100 | Tactical mesh network node | 900MHz/2.4GHz | 5km mesh | MIL-STD-188 |
| eEncrypt-HSM | Hardware encryption module | — | — | FIPS 140-3 Level 3 |

## Electrical Specifications — eTR-5000 SDR
| Parameter | Specification |
|---|---|
| **SoC** | Xilinx Zynq UltraScale+ ZU9EG (quad Cortex-A53 + FPGA) |
| **RF front-end** | AD9371 wideband transceiver 300MHz–6GHz |
| **Waveforms** | SINCGARS, HAVE QUICK II, Link-16, SRW |
| **Encryption** | AES-256, Type 1 NSA certified |
| **Power** | 28VDC, 45W typical |
| **Environmental** | MIL-STD-810H, IP67 |
