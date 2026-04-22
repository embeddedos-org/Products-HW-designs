# Products-HW-designs

[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)

Hardware designs, EE documentation, and board datasheets for EmbeddedOS products.

## Contents

| Product | Description | Status |
|---------|-------------|--------|
| `eRadar360_CAD/` | Next-gen driver awareness radar system — 120mm × 85mm, 10-layer hybrid PCB | Active |

## What's Included

Each product directory contains:

- **Schematics & PCB** — Full design files (KiCad format)
- **Product Datasheet** — Complete specifications for the board
- **Bring-Up Guide** — Power-on and board testing procedures
- **Manufacturing Notes** — BOM, assembly, and production files
- **Test Procedures** — Validation and quality assurance steps

## Requirements

- [KiCad](https://www.kicad.org/) 7.0+ for schematic and PCB viewing/editing
- Python 3.10+ for automated design scripts (if applicable)

## Getting Started

```bash
# Clone the repository
git clone https://github.com/embeddedos-org/Products-HW-designs.git
cd Products-HW-designs

# Open a schematic in KiCad
kicad eRadar360_CAD/eradar360.kicad_sch
```

## Related Repositories

| Repo | Relationship |
|------|-------------|
| [eos](https://github.com/embeddedos-org/eos) | Firmware that runs on these boards |
| [eboot](https://github.com/embeddedos-org/eboot) | Bootloader with board-specific ports |
| [ebuild](https://github.com/embeddedos-org/ebuild) | Build system with hardware analyzer (KiCad/YAML) |
| [eosim](https://github.com/embeddedos-org/eosim) | Simulate hardware without physical boards |

## License

Proprietary — see individual product directories for details.
