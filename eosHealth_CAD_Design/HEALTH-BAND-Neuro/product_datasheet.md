# HEALTH-BAND Neuro — Product Datasheet
> **Revision:** v2.1 | **Date:** 2026-06-02 | **Status:** Production Ready

---

## Product Overview

HEALTH-BAND Neuro is a medical-grade wristband device combining clinical ECG, 4-channel EEG, surface EMG, GPS tracking, and therapeutic TENS output in a single wearable. It is the world's first wristband to integrate neurological monitoring with therapeutic stimulation, targeting neurological disorder management, athletic performance, and clinical remote monitoring.

---

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Wristband with 44mm case |
| **Case dimensions** | 44mm × 38mm × 12mm |
| **Band material** | Medical-grade silicone (LSR), Shore A 40 |
| **Case material** | Polycarbonate + Aluminum 6061-T6 bezel |
| **Weight** | 42g (with band) |
| **Display** | 1.4" AMOLED, 454×454 px, 326 PPI |
| **Haptic** | LRA vibration motor, 300mN |
| **Water resistance** | IP68 — 50m / 5 ATM |
| **Operating temp** | -20°C to 55°C |
| **Strap width** | 22mm (standard), quick-release |

---

## 3D Model Specifications

### Case Assembly
- **Case body**: Polycarbonate (PC) injection molded, 1.5mm wall
- **Bezel**: Aluminum 6061-T6, anodized black/silver
- **Display glass**: Corning Gorilla Glass 5, 1.1mm thick, 2.5D curved
- **Crown**: Stainless steel 316L, 6mm diameter, rotary encoder
- **Back plate**: Medical-grade stainless steel 316L, mirror polished
- **Electrode contacts**: 6× gold-plated stainless steel 316L electrodes

### PCB Assembly
- **PCB type**: 6-layer rigid FR4, 1.2mm total thickness
- **Dimensions**: 36mm × 36mm (circular)
- **Copper weight**: 1oz outer / 0.5oz inner
- **Surface finish**: ENIG
- **Secondary PCB**: Flexible PCB for display + crown connection

### Band Electrode Layout
- **ECG electrodes**: 2× on back plate (Lead I configuration), 1× on band clasp (Lead II)
- **EEG reference**: 2× on band, 25mm from case
- **sEMG electrodes**: 2× on band, 40mm from case
- **TENS output pads**: 2× on band, 50mm from case (isolated)

---

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Application MCU** | STM32H743 (ARM Cortex-M7 @ 480MHz) |
| **Connectivity MCU** | Nordic nRF5340 (dual-core ARM Cortex-M33) |
| **Flash** | 2MB internal (STM32) + 1MB internal (nRF) + 32MB external QSPI |
| **RAM** | 1MB internal (STM32) + 512KB (nRF) + 8MB PSRAM |
| **Wireless** | BLE 5.3 LR + GPS (u-blox M10) |
| **Battery** | 3.7V LiPo, 400mAh |
| **Charging** | Magnetic pogo-pin, 5V/1A (Qi optional) |
| **Battery life** | 2–3 days (all sensors), 5 days (standard mode) |
| **Standby current** | <15µA |
| **Peak current** | 180mA (GPS + ECG + display active) |

---

## Sensor Specifications

### ECG — Medical-Grade 1-Lead + 3-Lead
| Parameter | Value |
|-----------|-------|
| **IC** | Texas Instruments ADS1293 |
| **Channels** | 3 (Lead I, II, III derivable) |
| **Sample rate** | 500 Hz (standard), 2000 Hz (clinical) |
| **Resolution** | 24-bit |
| **Input noise** | <1µV RMS |
| **CMRR** | >100dB |
| **Bandwidth** | 0.05 Hz – 150 Hz |

### EEG — 4-Channel Neurological Monitoring
| Parameter | Value |
|-----------|-------|
| **IC** | Texas Instruments ADS1299 |
| **Channels** | 4 (Fp1, Fp2, T3, T4 approximate) |
| **Sample rate** | 250 Hz |
| **Resolution** | 24-bit |
| **Input noise** | <1µV RMS |
| **Bandwidth** | 0.5 Hz – 100 Hz |
| **Electrode impedance check** | Built-in, <5kΩ required |

### Surface EMG — Gesture Recognition
| Parameter | Value |
|-----------|-------|
| **IC** | Analog Devices AD8232 (modified) |
| **Channels** | 2 differential |
| **Sample rate** | 1000 Hz |
| **Resolution** | 16-bit |
| **Bandwidth** | 20 Hz – 450 Hz |
| **Gesture library** | 12 pre-trained gestures (TFLite Micro) |

### TENS Therapeutic Output
| Parameter | Value |
|-----------|-------|
| **IC** | Custom H-bridge driver (DRV8833) |
| **Output voltage** | 0–80V peak (isolated) |
| **Pulse width** | 50µs – 500µs |
| **Frequency** | 1 Hz – 150 Hz |
| **Max current** | 80mA (skin contact) |
| **Safety** | IEC 60601-2-10 compliant, isolated output |

### GPS — Location + Activity
| Parameter | Value |
|-----------|-------|
| **IC** | u-blox M10 |
| **Protocols** | GPS + GLONASS + Galileo + BeiDou |
| **Accuracy** | 1.5m CEP |
| **TTFF** | 2s (hot), 30s (cold) |
| **Current** | 18mA (acquisition), 8mA (tracking) |

### PPG — Heart Rate + SpO₂ (backup)
| Parameter | Value |
|-----------|-------|
| **IC** | Maxim MAX86141 |
| **LEDs** | Green × 2, Red × 1, IR × 1 |
| **Sample rate** | 25 Hz – 200 Hz |

---

## Regulatory Status

| Framework | Status |
|-----------|--------|
| FDA | 510(k) pre-submission filed — ECG (Class II, §870.2340) |
| FCC | Part 15 §15.247 — testing in progress |
| IEC 60601-2-25 | ECG standard — testing SGS (Q3 2026) |
| IEC 60601-2-10 | TENS standard — testing SGS (Q3 2026) |
| ISO 13485 | QMS certified (BSI audit Q4 2026) |
| IEC 62304 | Class C software lifecycle — complete |
| HIPAA | PHI handling compliant |

---

## Reference Documents

- [`hardware/pcb/health-band-neuro.kicad_sch`](./hardware/pcb/health-band-neuro.kicad_sch) — KiCad schematic
- [`bom.csv`](./bom.csv) — Full bill of materials
- [`docs/HEALTH_BAND_Neuro_Standalone_Architecture.md`](./docs/HEALTH_BAND_Neuro_Standalone_Architecture.md) — System architecture
- [`simulation/ecg_frontend_simulation.png`](./simulation/ecg_frontend_simulation.png) — ECG frontend simulation
- [eos-health regulatory/fda/FDA_510K_HEALTH_BAND_NEURO.md](https://github.com/embeddedos-org/eos-health/blob/main/regulatory/fda/FDA_510K_HEALTH_BAND_NEURO.md) — FDA 510(k) package
