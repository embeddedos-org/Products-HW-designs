# HEALTH-KEY ULTRA — Product Datasheet
> **Revision:** v2.1 | **Date:** 2026-06-02 | **Status:** Production Ready

---

## Product Overview

HEALTH-KEY ULTRA is a medical-grade health monitoring keychain/pendant device that provides continuous physiological monitoring in a form factor small enough to carry on a keychain or wear as a pendant. It is the world's first FDA-cleared (510(k) pending) health monitoring keychain, combining clinical-grade sensors with a cryptographic health identity key.

---

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Keychain / pendant |
| **Dimensions** | 45mm × 25mm × 8mm |
| **Weight** | 18g (titanium) / 14g (aluminum) |
| **Chassis material** | Grade 5 Titanium (Ti-6Al-4V) or Anodized Aluminum 6061-T6 |
| **Display** | 0.49" OLED, 64×32 px, SSD1306 |
| **Haptic** | ERM vibration motor, 150mN |
| **Keychain loop** | Stainless steel 316L, 8mm ID |
| **Water resistance** | IP67 — 1m / 30 min |
| **Operating temp** | -10°C to 50°C |
| **Storage temp** | -20°C to 60°C |

---

## 3D Model Specifications

### Outer Shell
- **Geometry**: Rounded rectangle with chamfered corners (r=3mm)
- **Material**: Titanium Grade 5 (Ti-6Al-4V) — density 4.43 g/cm³
- **Surface finish**: Bead-blasted + PVD coating (Black, Silver, Gunmetal)
- **Tolerance**: ±0.05mm CNC machined
- **Wall thickness**: 1.2mm (sides), 1.5mm (top/bottom)

### PCB Assembly
- **PCB type**: 4-layer rigid FR4, 1.0mm total thickness
- **Dimensions**: 38mm × 18mm × 1.0mm
- **Copper weight**: 1oz outer / 0.5oz inner
- **Surface finish**: ENIG (Electroless Nickel Immersion Gold)
- **Solder mask**: Green LPI, both sides

### Sensor Window
- **Material**: Sapphire glass, 3mm diameter, 0.5mm thick
- **Location**: Bottom face, centered
- **Seal**: Silicone O-ring, Shore A 70, 2.5mm ID

---

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **MCU** | Nordic nRF5340 (dual-core ARM Cortex-M33 @ 128MHz + M33 @ 64MHz) |
| **Flash** | 1MB internal + 8MB external QSPI NOR (Winbond W25Q64JV) |
| **RAM** | 512KB internal + 8MB PSRAM |
| **Wireless** | BLE 5.3 (Long Range, 2 Mbps, Coded PHY) |
| **Antenna** | Chip antenna (Molex 2450AT18D0100E) + PCB trace backup |
| **Battery** | 3.7V LiPo, 120mAh, custom 38×16×4mm |
| **Charging** | USB-C (5V/500mA), MCP73831 charger IC |
| **Battery life** | 3–5 days (continuous monitoring) |
| **Standby current** | <8µA (deep sleep, RTC active) |
| **Peak current** | 22mA (BLE TX + all sensors active) |
| **Supply voltage** | 3.0–4.2V (LiPo) → 1.8V / 3.3V regulated |

---

## Sensor Specifications

### Optical PPG — Heart Rate, SpO₂, HRV
| Parameter | Value |
|-----------|-------|
| **IC** | Maxim MAX86141 |
| **LEDs** | Green (537nm) × 2, Red (660nm) × 1, IR (940nm) × 1 |
| **Photodiodes** | 2× silicon PD, 0.5mm² each |
| **Sample rate** | 25 Hz (standard), 200 Hz (clinical mode) |
| **ADC resolution** | 19-bit |
| **Current consumption** | 1.1mA (standard), 4.5mA (clinical) |

### Bioimpedance — Hydration, Body Composition
| Parameter | Value |
|-----------|-------|
| **IC** | Analog Devices AD5940 |
| **Frequency range** | 1kHz – 200kHz |
| **Impedance range** | 100Ω – 1MΩ |
| **Accuracy** | ±0.1% |
| **Electrodes** | 2× stainless steel 316L, 5mm × 3mm |

### Temperature
| Parameter | Value |
|-----------|-------|
| **IC** | Maxim MAX30208 |
| **Range** | 0°C – 45°C |
| **Accuracy** | ±0.1°C |
| **Resolution** | 0.005°C |

### Accelerometer / Gyroscope — Activity, Fall Detection
| Parameter | Value |
|-----------|-------|
| **IC** | Bosch BMI270 |
| **Accelerometer range** | ±2g / ±4g / ±8g / ±16g |
| **Gyroscope range** | ±125 / ±250 / ±500 / ±1000 / ±2000 dps |
| **Sample rate** | 0.78 Hz – 1600 Hz |
| **Current** | 685µA (normal mode) |

### Cryptographic Security Element
| Parameter | Value |
|-----------|-------|
| **IC** | Microchip ATECC608B |
| **Algorithm** | ECDSA P-256, SHA-256, AES-128 |
| **Key storage** | 16 slots, 72-byte each |
| **Interface** | I²C, 1MHz |
| **Use case** | Health data signing, device identity, HIPAA audit trail |

---

## Communication Interfaces

| Interface | IC | Speed | Use |
|-----------|-----|-------|-----|
| BLE 5.3 | nRF5340 radio | 2 Mbps | App sync, cloud upload |
| USB-C | CH340C | USB 2.0 FS | Charging + debug UART |
| I²C | nRF5340 TWI | 400kHz | All sensors |
| SPI | nRF5340 SPIM | 32MHz | External flash |

---

## Software Stack

| Layer | Technology |
|-------|-----------|
| RTOS | Zephyr RTOS v3.6 |
| BLE stack | Zephyr BT (Nordic SoftDevice S140 compatible) |
| Sensor drivers | Custom Zephyr drivers (IEC 62304 Class B) |
| Health algorithms | EoS Health Algorithm Library v2.1 |
| Crypto | Mbed TLS 3.4 + ATECC608B hardware offload |
| OTA | MCUboot + SUIT manifest |
| Logging | RTT + UART (debug builds) |

---

## Regulatory Status

| Framework | Status |
|-----------|--------|
| FDA | 510(k) pre-submission filed (Q-Sub 2026-Q3) |
| FCC | Part 15 §15.247 — testing in progress |
| CE (EU MDR) | Technical file in preparation |
| ISO 13485 | QMS certified (BSI audit Q4 2026) |
| IEC 62304 | Class B software lifecycle — complete |
| ISO 10993 | Biocompatibility testing — Nelson Labs (Q3 2026) |
| IEC 60601-1 | Safety testing — SGS (Q3 2026) |
| HIPAA | BAA executed, PHI handling compliant |

---

## Manufacturing Notes

- **PCB assembly**: SMT + selective wave soldering; 0402 minimum component size
- **Enclosure**: CNC machined titanium; ultrasonic welding for final assembly
- **Test**: 100% electrical test (ICT) + functional test (BLE + sensor validation)
- **Calibration**: Factory calibration at 25°C for SpO₂ and temperature sensors
- **Marking**: CE, FCC ID, UDI (GS1 DataMatrix), RoHS compliant
- **Packaging**: Recycled cardboard, USB-C cable included, quick-start card

---

## Reference Documents

- [`hardware/pcb/health-key-ultra.kicad_sch`](./hardware/pcb/health-key-ultra.kicad_sch) — KiCad schematic
- [`bom.csv`](./bom.csv) — Full bill of materials
- [`hardware/cad/3d_models/`](./hardware/cad/3d_models/) — 3D model specifications
- [`simulation/`](./simulation/) — Power budget simulation
- [eos-health regulatory/fda/FDA_510K_HEALTH_KEY_ULTRA.md](https://github.com/embeddedos-org/eos-health/blob/main/regulatory/fda/FDA_510K_HEALTH_KEY_ULTRA.md) — FDA 510(k) package
