# eRadar360 — "Aegis One" Driver Awareness System

> Next-generation threat intelligence platform with V2X, AI, and 360° phased-array radar.

## Product Overview

eRadar360 is built from the ground up as a **threat intelligence system** — not a radar detector with features bolted on. Every subsystem is best-in-class, and they all share data through an on-device neural network.

**Target Price:** $699
**Dimensions:** 120mm × 85mm × 18mm
**Weight:** 185g
**Mount:** Magnetic windshield mount + suction cup

---

## Key Features

| Feature | Specification |
|---------|---------------|
| **Display** | 4" Samsung AMOLED, 480×800, 600 nits, color-coded threat map |
| **Front Radar** | SIW phased array, 8×8 elements, 24 dBi, ±45° beam steering |
| **Rear Radar** | SIW phased array, 4×4 elements, 18 dBi, ±30° beam steering |
| **Radar Bands** | Ka (33.4–36.0 GHz), K (24.05–24.25 GHz), Ku (13.45–13.50 GHz), X (10.5–10.55 GHz) |
| **Laser** | 5× Hamamatsu InGaAs APD array, 360° coverage, 904nm + 1550nm |
| **V2X** | DSRC (5.9 GHz) + C-V2X (PC5), receives law enforcement BSM |
| **AI Engine** | 6 TOPS NPU (RK3588S), signature fingerprinting, 97% false-alert suppression |
| **GPS** | u-blox NEO-M9N, 1.5m CEP, cloud-shared threat database |
| **OBD-II** | CAN bus integration — speed, cruise state, lane context |
| **Connectivity** | Bluetooth 5.3, Wi-Fi 6, USB-C (data + power) |
| **Audio** | 3.5mm jack + built-in 2W speaker |
| **Power** | 12V vehicle (OBD-II) or USB-C 5V/3A |

---

## Block Diagram

```
                            ┌──────────────────────────────────────────────┐
                            │              eRadar360 / Aegis One          │
                            │                                              │
  ┌─────────────┐     SPI   │  ┌──────────┐    MIPI-DSI   ┌────────────┐ │
  │ FRONT ARRAY │◄─────────►│  │  AWR2944 │──────────────►│  4" OLED   │ │
  │ 8×8 SIW     │           │  │  (Front) │               │  Display   │ │
  │ Ka/K/X band │           │  │   U1     │               │   U6       │ │
  └─────────────┘           │  └────┬─────┘               └────────────┘ │
                            │       │ SPI                                  │
  ┌─────────────┐     SPI   │  ┌────▼──────────────────┐                  │
  │ REAR ARRAY  │◄─────────►│  │     RK3588S           │   ┌──────────┐ │
  │ 4×4 SIW     │           │  │  Main CPU + 6T NPU    │◄─►│  DDR4    │ │
  │ Ka/K/X band │           │  │     U3                 │   │  8Gb U11 │ │
  └─────────────┘           │  │                        │   └──────────┘ │
                            │  │  ┌─ AI Threat Engine   │                  │
  ┌─────────────┐     SPI   │  │  ├─ Signature DB       │   ┌──────────┐ │
  │  AWR2944    │◄─────────►│  │  ├─ V2X Correlator    │◄─►│  Flash   │ │
  │  (Rear) U2  │           │  │  └─ OBD Context Fuser │   │  256Mb   │ │
  └─────────────┘           │  └────┬───┬───┬───┬──────┘   │  U12     │ │
                            │       │   │   │   │          └──────────┘ │
  ┌─────────────┐    UART   │  ┌────▼─┐ │   │   │                       │
  │  TEKTON3    │◄─────────►│  │STM32 │ │   │   │    ┌──────────────┐  │
  │  V2X  U4    │           │  │H7B3  │ │   │   └───►│ USB-C + 3.5mm│  │
  │  DSRC/C-V2X │           │  │ U8   │ │   │        │ Connectors   │  │
  └─────────────┘           │  └──────┘ │   │        └──────────────┘  │
                            │           │   │                           │
  ┌─────────────┐   Analog  │  ┌────────▼┐ │   ┌──────────────┐       │
  │ 5× InGaAs   │◄─────────►│  │NEO-M9N  │ └──►│ TPS65219     │       │
  │ APD Laser   │           │  │GPS U7   │     │ PMIC  U10    │       │
  │ Array  U5   │           │  └─────────┘     └──────┬───────┘       │
  └─────────────┘           │                         │                │
                            │  ┌─────────┐     ┌──────▼───────┐       │
  ┌─────────────┐    CAN    │  │ELM327 + │     │ Power Rails  │       │
  │  OBD-II     │◄─────────►│  │MCP2551  │     │ 5V,3.3V,1.8V │       │
  │  Port       │           │  │  U9     │     │ 0.85V,1.1V   │       │
  └─────────────┘           │  └─────────┘     └──────────────┘       │
                            └──────────────────────────────────────────┘
```

---

## Design Files

| File | Description |
|------|-------------|
| `pcb_stackup.txt` | 10-layer hybrid Rogers 4003C / FR4 stackup |
| `bom.csv` | Full bill of materials with real MPN and pricing |
| `decoupling_cap_map.csv` | Decoupling capacitor placement for all ICs |
| `power_sequencing.html` | Interactive power-on/sleep/wake/shutdown timing |
| `eradar360_schematic.html` | Interactive block schematic viewer |
| `eradar360.net` | KiCad netlist export |
| `antenna_design.md` | SIW phased array design rationale and calculations |
| `bring_up_guide.md` | Board bring-up and test procedure |

---

## Architecture Highlights

### Why SIW Phased Array?
Standard microstrip patch arrays (used in R8, Redline 360c) are fixed-beam. The SIW array electronically steers ±45° — when AI detects a signal at 20° left, firmware focuses the beam for 3–4 dB extra gain. That's detecting a gun at 2 miles vs 1 mile.

### Why V2X?
Modern smart city infrastructure broadcasts law enforcement activity on DSRC/C-V2X channels. No consumer detector listens to this. eRadar360 knows about a speed trap a mile before any radar signal is detectable.

### Why On-Device AI?
The false-alert problem plagues every detector. The RK3588S NPU fingerprints radar signatures by pulse pattern and modulation — not just frequency band. 97% false-alert suppression without cloud dependency.

### Why OBD-II?
Your car knows your speed, cruise state, and lane. Feeding this into alert logic eliminates an entire category of irrelevant warnings (e.g., no alert when adaptive cruise is managing speed).

---

## License

Proprietary — EmbeddedOS
