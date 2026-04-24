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

## Security

### Debug Interface Security

Production hardware **must** disable all debug interfaces to prevent unauthorized access:

- **JTAG/SWD**: Disable JTAG via silicon fuse bits (e.g., SAM-BA efuses, STM32 RDP Level 2) before shipping. The ePower board already documents this — eRadar360 should follow the same practice for J6.
- **Depopulate debug headers**: Remove JTAG headers (J2, J6) from production builds. Use DNP (Do Not Populate) designators on BOM for production variants.
- **Series resistors**: Add 0-ohm DNP series resistors on TCK/TMS/TDI lines so debug traces can be physically disconnected in production.
- **UART debug console**: Disable or restrict UART2 debug output in production firmware. Do not expose boot ROM messages on shipping devices. Consider removing TP7/TP8 test points in production.

### Hardware Security Module (HSM) Considerations

- Use on-chip secure enclaves or external HSMs for key storage (firmware signing keys, device identity certificates).
- Enable secure boot chain: bootloader must verify firmware signatures before execution.
- Store cryptographic keys in hardware-protected key slots — never in firmware flash.
- Implement hardware-backed random number generation (TRNG) for cryptographic operations.

### Physical Tamper Protection

- Apply conformal coating over sensitive signal traces (JTAG, UART, SPI) on production boards.
- Consider tamper-detect mesh or enclosure switches that trigger key zeroization on physical intrusion.
- Use BGA packages where possible to reduce probe-ability of sensitive signal lines.
- Restrict access to reset lines (nRESET, nRST) — exposed reset pins allow glitching attacks.
- Remove or obfuscate silkscreen labels for debug connectors and test points in production.

### Repository Access

- This repository contains sensitive hardware design details (debug pinouts, component placements, test point locations). Restrict access to authorized personnel only.
- Do not share BOM part numbers, pick-and-place coordinates, or debug header pinouts publicly.

## License

Proprietary — see individual product directories for details.
