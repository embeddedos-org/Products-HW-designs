# HEALTH-RING — Product Datasheet
> **Revision:** v2.1 | **Date:** 2026-06-02 | **Status:** Production Ready

---

## Product Overview

HEALTH-RING is a medical-grade smart ring providing continuous non-invasive monitoring of cardiovascular health, blood glucose trends (HbA1c proxy), blood pressure (cNIBP), sleep staging, and stress. It is the most sensor-dense smart ring on the market, targeting the De Novo regulatory pathway for novel non-invasive biomarker monitoring.

---

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Smart ring |
| **Available sizes** | US 6–13 (inner diameter 16.5mm–22.2mm) |
| **Width** | 8mm |
| **Thickness** | 2.5mm radial |
| **Outer material** | Grade 5 Titanium (Ti-6Al-4V) or Ceramic (ZrO₂) |
| **Inner band** | Medical-grade LSR silicone, Shore A 40 |
| **Weight** | 4g (titanium) / 3.8g (ceramic) |
| **Water resistance** | IP68 — 100m / 10 ATM |
| **Display** | None (haptic-only feedback) |
| **Operating temp** | 0°C to 45°C |

---

## 3D Model Specifications

### Outer Shell
- **Geometry**: Toroidal ring with chamfered edges (1mm chamfer)
- **Material**: Titanium Grade 5 (Ti-6Al-4V) — density 4.43 g/cm³
- **Surface finish**: PVD coating — Black, Silver, Gold, Rose Gold
- **Tolerance**: ±0.05mm CNC machined
- **Wall thickness**: 0.8mm (sides)

### Inner Sensor Band
- **Material**: Liquid silicone rubber (LSR), Shore A 40, biocompatible
- **Sensor windows**: 3× optical windows (sapphire glass, 2mm diameter)
- **Electrode pads**: 2× gold-plated EDA electrodes (5mm × 2mm)
- **Temperature sensor**: Embedded NTC thermistor, 0.5mm diameter

### PCB Assembly
- **PCB type**: 4-layer rigid-flex, 0.3mm total thickness
- **Shape**: Curved arc, 220° wrap around ring interior
- **Dimensions**: 22mm × 5mm × 0.3mm (size 10 reference)
- **Copper weight**: 0.5oz all layers
- **Surface finish**: ENIG

---

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **MCU** | Nordic nRF5340 (dual-core ARM Cortex-M33 @ 128MHz + M33 @ 64MHz) |
| **Flash** | 1MB internal + 4MB external QSPI NOR |
| **RAM** | 512KB internal |
| **Wireless** | BLE 5.3 (Long Range, 2 Mbps, Coded PHY) |
| **Antenna** | PCB trace antenna (integrated into flex PCB arc) |
| **Battery** | 3.7V LiPo, 22mAh (custom toroidal form factor) |
| **Charging** | Qi wireless, 5V/100mA (charging dock) |
| **Battery life** | 4–5 days (standard), 2 days (clinical mode) |
| **Standby current** | <3µA |
| **Peak current** | 12mA (BLE TX + all sensors) |

---

## Sensor Specifications

### Optical PPG — Heart Rate, SpO₂, HRV, Blood Pressure
| Parameter | Value |
|-----------|-------|
| **IC** | ams OSRAM AS7058 (3-channel PPG) |
| **LEDs** | Green (525nm) × 2, Red (660nm) × 1, IR (940nm) × 1 |
| **Photodiodes** | 3× silicon PD, 0.5mm² each |
| **Sample rate** | 25 Hz (standard), 100 Hz (sleep/workout) |
| **cNIBP algorithm** | PTT-based, calibrated against oscillometric reference |
| **HbA1c proxy** | Spectral analysis at 660nm/940nm ratio trend |

### Temperature
| Parameter | Value |
|-----------|-------|
| **Sensor** | NTC thermistor, 10kΩ @ 25°C, B=3950K |
| **Range** | 20°C – 42°C |
| **Accuracy** | ±0.2°C |
| **Resolution** | 0.01°C |

### Accelerometer — Sleep Staging, Activity
| Parameter | Value |
|-----------|-------|
| **IC** | Bosch BMA456 (ultra-low power) |
| **Range** | ±2g / ±4g / ±8g / ±16g |
| **Sample rate** | 0.78 Hz – 1600 Hz |
| **Current** | 2µA (low-power mode) |

### EDA — Stress Monitoring
| Parameter | Value |
|-----------|-------|
| **Method** | Electrodermal activity via gold electrodes |
| **Frequency** | DC + 1kHz AC |
| **Range** | 0.1µS – 100µS |
| **Accuracy** | ±5% |

---

## Regulatory Status

| Framework | Status |
|-----------|--------|
| FDA | De Novo petition — Class II novel device (HbA1c, cNIBP) |
| FCC | Part 15 §15.247 — e-label (no physical label space) |
| ISO 10993 | Biocompatibility — extended contact (>30 days) testing |
| IEC 60601-1 | Safety testing — SGS (Q3 2026) |
| ISO 13485 | QMS certified (BSI audit Q4 2026) |
| IEC 62304 | Class B software lifecycle — complete |

---

## Reference Documents

- [`hardware/pcb/health-ring.kicad_sch`](./hardware/pcb/health-ring.kicad_sch) — KiCad schematic
- [`bom.csv`](./bom.csv) — Full bill of materials
- [`simulation/ppg_biosensor_simulation.png`](./simulation/ppg_biosensor_simulation.png) — PPG simulation
- [eos-health regulatory/fda/FDA_DE_NOVO_HEALTH_RING_AND_LAB.md](https://github.com/embeddedos-org/eos-health/blob/main/regulatory/fda/FDA_DE_NOVO_HEALTH_RING_AND_LAB.md) — FDA De Novo package
