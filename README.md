# eHardware-Designs-Products

[![CI](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/ci.yml/badge.svg)](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/ci.yml)
[![CodeQL](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/codeql.yml/badge.svg)](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/codeql.yml)
[![Scorecard](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/scorecard.yml/badge.svg)](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/scorecard.yml)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Book](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/book-build.yml/badge.svg)](https://github.com/embeddedos-org/eHardware-Designs-Products/actions/workflows/book-build.yml)

Hardware designs, schematics, PCB layouts, 3D models, BOMs, and product datasheets for the EmbeddedOS hardware product line.

## Products

| Product | Description | Devices | Status |
|---------|-------------|---------|--------|
| [`eRadar360_CAD/`](eRadar360_CAD/) | Next-gen driver awareness radar — 120mm x 85mm, 10-layer hybrid PCB | 1 board | Active |
| [`eHealth365_CAD_Design/`](eHealth365_CAD_Design/) | Two-device health monitoring — Smart Ring Pro + Smart Patch Pro with 3D models, mobile app | 2 wearables + app | Active |
| [`ePAM_CAD_Design/`](ePAM_CAD_Design/) | Personal Air Mobility — 4 solar-hybrid vehicles (Urban Drone, Space Shuttle, Eco Car, Combo Unit) + mobile app | 4 vehicles + app | Active |

## Product Summary

### eRadar360 — Driver Awareness Radar
- 120mm x 85mm, 10-layer hybrid PCB
- Radar sensor array for automotive ADAS
- Full KiCad schematics, BOM, pick-and-place, antenna design

### eHealth365 — Health Monitoring System
- **Smart Ring Pro**: Titanium ring, 2.5mm wide, 4g — HR/HRV, SpO2, temperature, accelerometer, ketone breath port, skin conductance
- **Smart Patch Pro**: 40x30mm arm patch, 3.5mm thin — CGM glucose, sweat electrolytes, bioimpedance hydration, monthly blood cartridge
- Mobile app: dark-theme dashboard, daily health score, AI food camera
- Coverage: ~90% of all health metrics with 2 devices

### ePAM — Personal Air Mobility
- **Eco Car**: 4-5 seat solar-hybrid ground vehicle, $28-45K, 500-900km range
- **Urban Drone**: 4-seat eVTOL, $85-120K, 300-500km range, 8x tilt-rotors
- **Space Shuttle**: 4-seat suborbital, $2-4M, 100km altitude, solar-thermal rocket
- **Combo Unit**: 4-seat trans-atmospheric, $5-9M, drone-to-space in one vehicle
- **ULP-SSN Avionics**: 12-layer IPC-6012 Class 3 Space/Military board (Kintex FPGA + Apollo4 MCU)
- Tesla-like mobile app: single app controls all 4 vehicles
- Shared power architecture: solar + H2 fuel cell + solid-state battery + kinetic regen

## What's Included Per Product

Each product directory contains:

| File Type | Description | Extension |
|-----------|-------------|-----------|
| **Schematics** | Full KiCad electrical schematics | `.kicad_sch` |
| **Netlists** | Component connectivity data | `.net` |
| **PCB stackup** | Layer definitions, materials, impedance | `.txt` |
| **BOM** | Bill of materials with costs | `.csv` |
| **Product datasheet** | Complete specifications | `.md` |
| **Manufacturing notes** | Assembly, QC, production instructions | `.md` |
| **3D models** | Mechanical design specs & exploded views | `.md` |
| **Interactive schematics** | Browser-viewable schematic diagrams | `.html` |
| **Business plans** | Cost analysis, go-to-market, regulatory | `.md` |
| **App architecture** | Mobile app UI specs & tech stack | `.md` |

## Repository Structure

```
eHardware-Designs-Products/
├── eRadar360_CAD/
│   ├── eradar360.kicad_sch              KiCad schematic
│   ├── eradar360.net                    Netlist
│   ├── eradar360_schematic.html         Interactive schematic
│   ├── pcb_stackup.txt                  10-layer stackup
│   ├── bom.csv                          Bill of materials
│   ├── pick_and_place.csv               Pick-and-place coordinates
│   ├── decoupling_cap_map.csv           Decoupling capacitor map
│   ├── antenna_design.md                RF antenna design
│   ├── product_datasheet.md             Full specifications
│   ├── bring_up_guide.md                Board power-on testing
│   ├── manufacturing_notes.md           Assembly instructions
│   └── power_sequencing.html            Power timing diagrams
│
├── eHealth365_CAD_Design/
│   ├── smart_ring_pro/                  Smart Ring Pro (finger, 24/7)
│   │   ├── ring_schematic.kicad_sch
│   │   ├── bom.csv
│   │   ├── product_datasheet.md
│   │   └── manufacturing_notes.md
│   ├── smart_patch_pro/                 Smart Patch Pro (upper arm, weekly)
│   │   ├── patch_schematic.kicad_sch
│   │   ├── bom.csv
│   │   ├── product_datasheet.md
│   │   └── cartridge_interface.md
│   ├── 3d_models/                       3D CAD specs
│   ├── app_architecture/                Mobile app (dark-theme dashboard)
│   └── docs/                            Sensing strategy, battery, data flow
│
├── ePAM_CAD_Design/
│   ├── eco_car/                         Solar-hybrid ground vehicle
│   │   ├── car_schematic.kicad_sch
│   │   ├── bom.csv
│   │   └── product_datasheet.md
│   ├── urban_drone/                     eVTOL aircraft
│   │   ├── drone_schematic.kicad_sch
│   │   ├── bom.csv
│   │   └── product_datasheet.md
│   ├── space_shuttle/                   Suborbital vehicle
│   │   ├── shuttle_schematic.kicad_sch
│   │   ├── bom.csv
│   │   ├── product_datasheet.md
│   │   └── avionics_ulp_ssn/           ULP-SSN space-grade avionics board
│   │       ├── ulp_ssn.net
│   │       ├── ulp_ssn_schematic.html
│   │       ├── power_sequencing.html
│   │       ├── pcb_stackup.txt
│   │       └── decoupling_cap_map.csv
│   ├── combo_unit/                      Trans-atmospheric hybrid
│   │   ├── combo_schematic.kicad_sch
│   │   └── product_datasheet.md
│   ├── power_architecture/              Shared power systems
│   ├── 3d_models/                       Vehicle 3D specs
│   ├── app_architecture/                Tesla-like control app
│   └── docs/                            Business plan, regulatory, infrastructure
│
├── .github/workflows/
│   ├── ci.yml                           CAD validation CI
│   ├── codeql.yml                       Security analysis
│   ├── scorecard.yml                    OSSF Scorecard
│   └── auto-assign.yml                  PR auto-assignment
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── CODEOWNERS
```

## Requirements

- [KiCad](https://www.kicad.org/) 7.0+ for schematic and PCB viewing/editing
- Python 3.10+ for automated design scripts
- Web browser for interactive schematic viewers (`.html` files)

## Getting Started

```bash
# Clone the repository
git clone https://github.com/embeddedos-org/eHardware-Designs-Products.git
cd eHardware-Designs-Products

# Open a schematic in KiCad
kicad eRadar360_CAD/eradar360.kicad_sch

# View interactive schematics in browser
open eRadar360_CAD/eradar360_schematic.html
open ePAM_CAD_Design/space_shuttle/avionics_ulp_ssn/ulp_ssn_schematic.html

# View power sequencing timing diagrams
open ePAM_CAD_Design/space_shuttle/avionics_ulp_ssn/power_sequencing.html
```

## CI/CD — CAD Validation

The CI pipeline automatically validates all design files on every push and PR:

| Check | What It Validates |
|-------|------------------|
| **KiCad schematic syntax** | Parses all `.kicad_sch` files for valid S-expression syntax |
| **Netlist consistency** | Validates `.net` files for proper component references |
| **BOM completeness** | Checks all `.csv` BOMs have required columns (Reference, Description, Qty) |
| **PCB stackup** | Validates layer count and thickness definitions in `.txt` stackup files |
| **Documentation** | Checks all product directories have a `product_datasheet.md` |
| **Markdown links** | Validates internal cross-references between docs |
| **HTML schematics** | Checks `.html` files are valid and loadable |
| **CSV format** | Validates BOM and pick-and-place CSV formatting |
| **File size** | Ensures no accidentally committed large binary files |

## Related Repositories

| Repo | Relationship |
|------|-------------|
| [eos](https://github.com/embeddedos-org/eos) | Embedded firmware for all hardware products |
| [eAI](https://github.com/embeddedos-org/eAI) | AI inference for wearable health scoring & autonomous flight |
| [eNI](https://github.com/embeddedos-org/eNI) | Neural interface for biosignal processing (eHealth365) |
| [eBoot](https://github.com/embeddedos-org/eBoot) | Secure bootloader with board-specific ports |
| [ebuild](https://github.com/embeddedos-org/ebuild) | Build system with KiCad hardware analyzer |
| [EoSim](https://github.com/embeddedos-org/EoSim) | Simulate hardware without physical boards |
| [eApps](https://github.com/embeddedos-org/eApps) | Mobile app platform for eHealth365 & ePAM apps |

## Security

This repository contains sensitive hardware design details. See [SECURITY.md](SECURITY.md).

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

Proprietary — see individual product directories for details.

---
Part of the [EmbeddedOS Organization](https://embeddedos-org.github.io).
