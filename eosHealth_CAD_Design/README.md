# EoS Health — Four-Device Wearable Health Platform
> **CAD Design Archive | Hardware Prototyping with eBuild Simulation**
> Complete hardware designs, KiCad schematics, BOMs, 3D models, and simulation scripts for the EoS Health product ecosystem

---

## System Overview

EoS Health is a four-device wearable health monitoring platform covering **100% of clinically relevant health metrics** — from cardiovascular vitals and neurological signals to blood chemistry and molecular biomarkers. All four devices communicate via BLE 5.3 and integrate with the EoS Health mobile app and cloud platform.

```
┌──────────────────────────┐   ┌──────────────────────────┐
│  🔑 HEALTH-KEY ULTRA     │   │  🩺 HEALTH-BAND Neuro    │
│  Keychain / Pendant      │   │  Wristband               │
│                          │   │                          │
│  • SpO₂ + Heart Rate     │   │  • ECG (medical-grade)   │
│  • Temperature           │   │  • EEG (4-channel)       │
│  • Blood Pressure (est.) │   │  • sEMG (gesture)        │
│  • Hydration (bioZ)      │   │  • GPS + Activity        │
│  • Emergency SOS         │   │  • TENS therapy output   │
│  • Crypto health key     │   │  • Neurological scoring  │
└────────────┬─────────────┘   └────────────┬─────────────┘
             │                              │
             │         BLE 5.3             │
             └──────────────┬──────────────┘
                            │
┌──────────────────────────┐│  ┌──────────────────────────┐
│  💍 HEALTH-RING          ││  │  🧪 HEALTH-LAB           │
│  Smart Ring              ││  │  Wearable Lab Patch      │
│                          ││  │                          │
│  • PPG (HR + SpO₂)       ││  │  • Sweat glucose (CGM)   │
│  • HbA1c (non-invasive)  ││  │  • Cortisol (stress)     │
│  • Blood pressure (cNIBP)││  │  • Electrolytes (sweat)  │
│  • Sleep staging         ││  │  • Lactate (workout)     │
│  • Stress (HRV)          ││  │  • Hydration (bioZ)      │
│  • Activity + Steps      ││  │  • Skin pH               │
└────────────┬─────────────┘│  └────────────┬─────────────┘
             │              │               │
             └──────────────┴───────────────┘
                            │
                  ┌─────────────────────┐
                  │   📱 EoS HEALTH APP │
                  │   + Cloud Platform  │
                  │   + eBuild Stack    │
                  └─────────────────────┘
```

---

## Device Directory

| Device | Form Factor | MCU | BLE | Battery | FDA Path |
|--------|-------------|-----|-----|---------|----------|
| [HEALTH-KEY ULTRA](./HEALTH-KEY-ULTRA/) | Keychain/pendant, 45×25×8mm | nRF5340 | BLE 5.3 LR | 120mAh LiPo | 510(k) Class II |
| [HEALTH-BAND Neuro](./HEALTH-BAND-Neuro/) | Wristband, 44mm case | nRF5340 + STM32H7 | BLE 5.3 LR | 400mAh LiPo | 510(k) Class II |
| [HEALTH-RING](./HEALTH-RING/) | Smart ring, sizes 6–13 US | nRF5340 | BLE 5.3 LR | 22mAh LiPo | De Novo Class II |
| [HEALTH-LAB](./HEALTH-LAB/) | Adhesive patch, 50×30×4mm | nRF5340 | BLE 5.3 LR | 50mAh LiPo | De Novo Class II |

---

## Repository Structure

```
eosHealth_CAD_Design/
├── README.md                          ← This file
├── docs/
│   ├── SYSTEM_ARCHITECTURE.md         ← Full system block diagram
│   ├── SENSOR_COVERAGE_MATRIX.md      ← All metrics across all devices
│   └── EBUILD_INTEGRATION.md          ← eBuild stack integration guide
├── ebuild_simulation/
│   ├── README.md                      ← eBuild simulation guide
│   ├── eos_stack_sim.py               ← Full EoS stack simulator
│   └── device_models/                 ← Per-device simulation models
├── HEALTH-KEY-ULTRA/
│   ├── product_datasheet.md
│   ├── bom.csv
│   ├── hardware/
│   │   ├── pcb/health-key-ultra.kicad_sch
│   │   └── cad/3d_models/
│   ├── docs/
│   └── simulation/
├── HEALTH-BAND-Neuro/
│   ├── product_datasheet.md
│   ├── bom.csv
│   ├── hardware/
│   │   ├── pcb/health-band-neuro.kicad_sch
│   │   └── cad/3d_models/
│   ├── docs/
│   └── simulation/
├── HEALTH-RING/
│   ├── product_datasheet.md
│   ├── bom.csv
│   ├── hardware/
│   │   ├── pcb/health-ring.kicad_sch
│   │   └── cad/3d_models/
│   ├── docs/
│   └── simulation/
└── HEALTH-LAB/
    ├── product_datasheet.md
    ├── bom.csv
    ├── hardware/
    │   ├── pcb/health-lab.kicad_sch
    │   └── cad/3d_models/
    ├── docs/
    └── simulation/
```

---

## Relationship to eHealth365

The EoS Health platform is the **production successor** to the eHealth365 prototype concept. Key differences:

| Aspect | eHealth365 | EoS Health |
|--------|-----------|------------|
| Devices | 2 (Ring + Patch) | 4 (Key + Band + Ring + Lab) |
| MCU | nRF5340 | nRF5340 + STM32H7 (Band) |
| FDA path | Concept only | Active 510(k) + De Novo submissions |
| Firmware | Prototype | Production (IEC 62304 Class C) |
| Clinical validation | None | 10 IRB-approved studies |
| eBuild integration | Planned | Active — see `ebuild_simulation/` |

---

## eBuild Simulation

The `ebuild_simulation/` directory contains everything needed to simulate the EoS Health hardware stack using the eBuild framework. This enables:

- **Pre-silicon validation** of sensor algorithms before physical prototypes
- **EoS stack integration testing** — firmware, BLE, cloud, and app layers
- **Regression testing** against clinical reference datasets
- **Hardware-in-the-loop (HIL)** testing with QEMU + Renode

See [`ebuild_simulation/README.md`](./ebuild_simulation/README.md) for full setup instructions.

---

## License

Hardware designs are released under **CERN Open Hardware Licence v2 - Strongly Reciprocal (CERN-OHL-S)**.
Software and firmware are released under **Apache 2.0**.
Documentation is released under **CC BY 4.0**.

© 2026 EmbeddedOS Organization. All rights reserved.
