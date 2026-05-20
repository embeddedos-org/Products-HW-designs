# eCAD-Hardware-Products

<!-- begin: org-uniform badges (audit-2026-05) -->
[![CI](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/ci.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/ci.yml)
[![CodeQL](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/codeql.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/embeddedos-org/eCAD-Hardware-Products/badge)](https://securityscorecards.dev/viewer/?uri=github.com/embeddedos-org/eCAD-Hardware-Products)
[![Release](https://img.shields.io/github/v/tag/embeddedos-org/eCAD-Hardware-Products?label=release&sort=semver)](https://github.com/embeddedos-org/eCAD-Hardware-Products/releases)
[![License](https://img.shields.io/github/license/embeddedos-org/eCAD-Hardware-Products)](LICENSE)
<!-- end: org-uniform badges (audit-2026-05) -->


[![CI](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/ci.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/ci.yml)
[![CodeQL](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/codeql.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/codeql.yml)
[![Scorecard](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/scorecard.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/scorecard.yml)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Book](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/book-build.yml/badge.svg)](https://github.com/embeddedos-org/eCAD-Hardware-Products/actions/workflows/book-build.yml)

Hardware designs, schematics, PCB layouts, 3D models, BOMs, and product datasheets for the EmbeddedOS hardware product line.

## Products

| Product | Description | Devices | Status |
|---------|-------------|---------|--------|
| [\Health365_CAD_Design/\](eHealth365_CAD_Design/) | Two-device health monitoring — Smart Ring Pro + Smart Patch Pro with 3D models, mobile app | 2 wearables + app | Active |
| [\PAM_CAD_Design/\](ePAM_CAD_Design/) | Personal Air Mobility — 4 solar-hybrid vehicles (Urban Drone, Space Shuttle, Eco Car, Combo Unit) + mobile app | 4 vehicles + app | Active |

> **Note:** eRadar360 has moved to its own repository: [embeddedos-org/eRadar360_CAD](https://github.com/embeddedos-org/eRadar360_CAD)

## 🌟 Future Designs (Donor Showcase)

Ten concept-stage hardware products spanning health & accessibility, climate &
food, education & research, and infrastructure & frontier. Each lives as a
browseable directory under [`future_designs/`](future_designs/) with a
concept datasheet, BOM placeholder, and a one-page donor business plan —
enough for sponsors to evaluate before any silicon is committed.

### ❤️ Health, Accessibility, Dignity

| | Design | Pitch | Donor tier |
|---|---|---|---|
| 👓 | [`eVision`](future_designs/eVision/) | Wearable obstacle-detection band for blind / low-vision users (~$200 BOM vs $4 K commercial). | $5 K — 25 production units for a school for the blind. |
| 🤖 | [`eHand`](future_designs/eHand/) | Open-source 6-DOF myoelectric prosthetic hand (~$1.5 K BOM vs $30–60 K commercial). | $2 K — one full eHand build per recipient. |
| 🧠 | [`eBCI-Lite`](future_designs/eBCI-Lite/) | 8-channel dry-EEG headband + AAC keyboard for ALS / locked-in patients (~$300 BOM vs $15 K commercial). | $10 K — 30 evaluation units for one neurology clinic. |

### 🌍 Climate, Food, Water

| | Design | Pitch | Donor tier |
|---|---|---|---|
| 🌾 | [`eFarm`](future_designs/eFarm/) | Solar-powered LoRaWAN soil/crop sensor mesh for smallholder farmers (~$40 per node + $120 gateway). | $1 K — 25-acre cooperative farm. |
| 💧 | [`eHydro`](future_designs/eHydro/) | Community water-quality buoy + public dashboard (~$250 BOM, advisory data only). | $3 K — 10-buoy mesh on a contested river basin for a year. |
| 🐝 | [`eHive`](future_designs/eHive/) | Acoustic + climate beehive monitor classifying healthy / queenless / swarming / collapsing colonies (~$90 BOM). | $500 — 5-hive community apiary for two years. |

### 🤖 Robotics, Education, Research

| | Design | Pitch | Donor tier |
|---|---|---|---|
| 🚙 | [`eRover-Mini`](future_designs/eRover-Mini/) | $400 open-source autonomous research rover (TurtleBot alternative). | $2 K — 5 rovers for a university lab. |
| 🎓 | [`eEdu-Kit`](future_designs/eEdu-Kit/) | Classroom-ready all-in-one STEM dev board + 12-week curriculum (~$25 BOM). | $1 K — one classroom of 30 + curriculum. |

### ⚡ Infrastructure & Frontier

| | Design | Pitch | Donor tier |
|---|---|---|---|
| ⚡ | [`eMeshGrid`](future_designs/eMeshGrid/) | Off-grid micro-grid controller for community solar + battery + inverter (~$1.2 K controller). | $25 K — 1 controller + 30 kWh battery + solar for a 200-person village. |
| 🛰️ | [`eCubeSat-1U`](future_designs/eCubeSat-1U/) | 1U CubeSat reference design with EmbeddedOS as flight software (~$8 K hw + ~$30 K ride-share launch). | $30 K — sponsor one student-built satellite from build to launch. |

> **Canon impact: zero.** All ten designs live under `future_designs/` and
> are explicitly excluded from the canonical 13-product / 14-book roster
> until they graduate to a top-level CAD directory with a working KiCad
> schematic, real BOM, and integration smoke test. See
> [`future_designs/README.md`](future_designs/README.md) for the graduation
> checklist.

## Product Summary

### eHealth365 — Health Monitoring System
- **Smart Ring Pro**: Titanium ring, 2.5mm wide, 4g — HR/HRV, SpO2, temperature, accelerometer, ketone breath port, skin conductance
- **Smart Patch Pro**: 40x30mm arm patch, 3.5mm thin — CGM glucose, sweat electrolytes, bioimpedance hydration, monthly blood cartridge
- Mobile app: dark-theme dashboard, daily health score, AI food camera
- Coverage: ~90% of all health metrics with 2 devices

### ePAM — Personal Air Mobility
- **Eco Car**: 4-5 seat solar-hybrid ground vehicle, \-45K, 500-900km range
- **Urban Drone**: 4-seat eVTOL, \-120K, 300-500km range, 8x tilt-rotors
- **Space Shuttle**: 4-seat suborbital, \-4M, 100km altitude, solar-thermal rocket
- **Combo Unit**: 4-seat trans-atmospheric, \-9M, drone-to-space in one vehicle
- **ULP-SSN Avionics**: 12-layer IPC-6012 Class 3 Space/Military board (Kintex FPGA + Apollo4 MCU)
- Tesla-like mobile app: single app controls all 4 vehicles
- Shared power architecture: solar + H2 fuel cell + solid-state battery + kinetic regen

## What's Included Per Product

Each product directory contains:

| File Type | Description | Extension |
|-----------|-------------|-----------|
| **Schematics** | Full KiCad electrical schematics | \.kicad_sch\ |
| **Netlists** | Component connectivity data | \.net\ |
| **PCB stackup** | Layer definitions, materials, impedance | \.txt\ |
| **BOM** | Bill of materials with costs | \.csv\ |
| **Product datasheet** | Complete specifications | \.md\ |
| **Manufacturing notes** | Assembly, QC, production instructions | \.md\ |
| **3D models** | Mechanical design specs & exploded views | \.md\ |
| **Interactive schematics** | Browser-viewable schematic diagrams | \.html\ |
| **Business plans** | Cost analysis, go-to-market, regulatory | \.md\ |
| **App architecture** | Mobile app UI specs & tech stack | \.md\ |

## Repository Structure

```
eCAD-Hardware-Products/
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
\
## Requirements

- [KiCad](https://www.kicad.org/) 7.0+ for schematic and PCB viewing/editing
- Python 3.10+ for automated design scripts
- Web browser for interactive schematic viewers (\.html\ files)

## Getting Started

\\ash
# Clone the repository
git clone https://github.com/embeddedos-org/eCAD-Hardware-Products.git
cd eCAD-Hardware-Products

# Open a schematic in KiCad
kicad eHealth365_CAD_Design/smart_ring_pro/ring_schematic.kicad_sch

# View interactive schematics in browser
open ePAM_CAD_Design/space_shuttle/avionics_ulp_ssn/ulp_ssn_schematic.html

# View power sequencing timing diagrams
open ePAM_CAD_Design/space_shuttle/avionics_ulp_ssn/power_sequencing.html
\
## CI/CD — CAD Validation

The CI pipeline automatically validates all design files on every push and PR:

| Check | What It Validates |
|-------|------------------|
| **KiCad schematic syntax** | Parses all \.kicad_sch\ files for valid S-expression syntax |
| **Netlist consistency** | Validates \.net\ files for proper component references |
| **BOM completeness** | Checks all \.csv\ BOMs have required columns (Reference, Description, Qty) |
| **PCB stackup** | Validates layer count and thickness definitions in \.txt\ stackup files |
| **Documentation** | Checks all product directories have a \product_datasheet.md\ |
| **Markdown links** | Validates internal cross-references between docs |
| **HTML schematics** | Checks \.html\ files are valid and loadable |
| **CSV format** | Validates BOM and pick-and-place CSV formatting |
| **File size** | Ensures no accidentally committed large binary files |

## Related Repositories

| Repo | Relationship |
|------|-------------|
| [eRadar360_CAD](https://github.com/embeddedos-org/eRadar360_CAD) | Driver awareness radar hardware design (standalone repo) |
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

<!-- begin: release-model (audit-2026-05) -->
## Release model

`master` is the line of development; every PR lands here. `release` is a
rolling pointer to the latest released `vX.Y.Z` tag, updated automatically
by [`.github/workflows/sync-release-branch.yml`](.github/workflows/sync-release-branch.yml).
Tags are immutable.

See [embeddedos-org/.github/STANDARDS.md](https://github.com/embeddedos-org/.github/blob/master/STANDARDS.md)
for the org-wide tag scheme, release model, and the compliance frameworks
every product targets.
<!-- end: release-model (audit-2026-05) -->

## License

Proprietary — see individual product directories for details.

---
Part of the [EmbeddedOS Organization](https://embeddedos-org.github.io).
