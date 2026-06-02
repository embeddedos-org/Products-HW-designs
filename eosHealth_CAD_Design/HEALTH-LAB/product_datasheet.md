# HEALTH-LAB — Product Datasheet
> **Revision:** v2.1 | **Date:** 2026-06-02 | **Status:** Production Ready

---

## Product Overview

HEALTH-LAB is a wearable electrochemical biosensor patch that provides continuous molecular biomarker monitoring from sweat and interstitial fluid. It measures glucose, cortisol, electrolytes, lactate, skin pH, and hydration — metrics previously only available through blood draws or clinical laboratory tests. HEALTH-LAB is the world's first wearable to combine six simultaneous electrochemical biosensors in a single adhesive patch.

---

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Flexible adhesive patch |
| **Dimensions** | 50mm × 30mm × 4mm |
| **Substrate** | Polyimide (PI) flexible PCB |
| **Adhesive** | Medical-grade acrylic adhesive (3M 1524) |
| **Weight** | 6g |
| **Wear location** | Upper arm, abdomen, or lower back |
| **Wear duration** | 7 days continuous |
| **Water resistance** | IPX7 — sweat and shower proof |
| **Operating temp** | 15°C to 40°C |
| **Skin contact** | ISO 10993-5 cytotoxicity tested |

---

## 3D Model Specifications

### Patch Assembly
- **Flexible substrate**: Polyimide 25µm, 2-layer flex PCB
- **Encapsulation**: Medical-grade epoxy, 1mm thick over electronics
- **Biosensor array**: 6× electrochemical sensors, screen-printed on PI
- **Reference electrode**: Ag/AgCl printed reference, 5mm × 3mm
- **Microfluidic channel**: Laser-cut PDMS, 200µm channel width
- **Adhesive area**: 45mm × 25mm active adhesive zone

### Electronics Module (detachable)
- **Dimensions**: 25mm × 15mm × 3mm
- **PCB type**: 4-layer rigid FR4, 0.8mm
- **Connection**: 8-pin ZIF connector to flex substrate
- **Enclosure**: Medical-grade ABS, IP67 sealed

---

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **MCU** | Nordic nRF5340 (dual-core ARM Cortex-M33) |
| **Electrochemical AFE** | Analog Devices LMP91000 × 3 (2 sensors each) |
| **Flash** | 1MB internal + 4MB external QSPI NOR |
| **RAM** | 512KB |
| **Wireless** | BLE 5.3 LR |
| **Battery** | 3.7V LiPo, 50mAh (in electronics module) |
| **Battery life** | 7 days (matches patch wear duration) |
| **Standby current** | <5µA |
| **Peak current** | 18mA (BLE TX + all 6 sensors active) |

---

## Biosensor Specifications

### Glucose — Continuous Glucose Monitoring (CGM)
| Parameter | Value |
|-----------|-------|
| **Method** | Enzymatic amperometry (GOx on carbon electrode) |
| **Range** | 40–400 mg/dL |
| **Accuracy** | MARD <15% (ISO 15197:2013) |
| **Sample rate** | Every 5 minutes |
| **Calibration** | Factory-calibrated, optional fingerstick at day 3 |
| **Lag time** | 10–15 minutes vs. blood glucose |

### Cortisol — Stress Hormone
| Parameter | Value |
|-----------|-------|
| **Method** | Molecularly imprinted polymer (MIP) electrochemical |
| **Range** | 1–200 ng/mL (sweat) |
| **Accuracy** | ±20% vs. serum ELISA |
| **Sample rate** | Every 15 minutes |
| **Diurnal tracking** | Morning peak, afternoon trough detection |

### Electrolytes — Sodium, Potassium
| Parameter | Value |
|-----------|-------|
| **Method** | Ion-selective electrode (ISE) |
| **Sodium range** | 10–160 mM |
| **Potassium range** | 1–32 mM |
| **Accuracy** | ±5 mM (Na⁺), ±2 mM (K⁺) |
| **Sample rate** | Continuous (sweat-triggered) |

### Lactate — Exercise Metabolism
| Parameter | Value |
|-----------|-------|
| **Method** | Enzymatic amperometry (LOx on carbon electrode) |
| **Range** | 0.5–20 mmol/L |
| **Accuracy** | ±10% vs. blood lactate |
| **Sample rate** | Every 2 minutes (exercise mode) |

### Skin pH
| Parameter | Value |
|-----------|-------|
| **Method** | Polyaniline (PANI) potentiometric electrode |
| **Range** | pH 4.0–8.0 |
| **Accuracy** | ±0.1 pH units |
| **Sample rate** | Continuous |

### Hydration — Bioimpedance
| Parameter | Value |
|-----------|-------|
| **IC** | Analog Devices AD5940 |
| **Frequency** | 1kHz – 100kHz |
| **Impedance range** | 100Ω – 100kΩ |
| **Accuracy** | ±5% |

---

## Regulatory Status

| Framework | Status |
|-----------|--------|
| FDA | De Novo petition — Class II novel device (sweat glucose, cortisol) |
| FCC | Part 15 §15.247 — e-label |
| ISO 10993 | Biocompatibility — 7-day skin contact testing (Nelson Labs) |
| IEC 60601-1 | Safety testing — SGS (Q3 2026) |
| ISO 13485 | QMS certified (BSI audit Q4 2026) |
| IEC 62304 | Class B software lifecycle — complete |
| ISO 15197 | CGM accuracy standard — clinical validation study EOS-CL-003 |

---

## Reference Documents

- [`hardware/pcb/health-lab.kicad_sch`](./hardware/pcb/health-lab.kicad_sch) — KiCad schematic
- [`bom.csv`](./bom.csv) — Full bill of materials
- [`simulation/signal_integrity_simulation.png`](./simulation/signal_integrity_simulation.png) — Signal integrity simulation
- [eos-health regulatory/fda/FDA_DE_NOVO_HEALTH_RING_AND_LAB.md](https://github.com/embeddedos-org/eos-health/blob/main/regulatory/fda/FDA_DE_NOVO_HEALTH_RING_AND_LAB.md) — FDA De Novo package
