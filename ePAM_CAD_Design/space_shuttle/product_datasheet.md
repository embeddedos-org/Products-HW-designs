# Space Shuttle — Suborbital Vehicle Product Datasheet

## Overview

The Space Shuttle is a 4-seat suborbital vehicle for space tourism and point-to-point global transport. Powered by solar-thermal propulsion with hydrogen fuel cells, it reaches 100km altitude (Karman line) for brief microgravity experiences.

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Type** | Suborbital reusable launch vehicle |
| **Seats** | 4 (1 pilot + 3 passengers) |
| **Length** | 14m |
| **Wingspan** | 9m (delta wing) |
| **Height** | 4.5m |
| **Empty weight** | 3,200 kg |
| **MTOW** | 5,500 kg |
| **Payload** | 450 kg |
| **Body material** | Titanium/carbon-fiber + ceramic TPS (thermal protection) |
| **Windows** | Fused silica triple-pane (rated 1650C) |

## Performance

| Parameter | Specification |
|-----------|--------------|
| **Max altitude** | 110 km (above Karman line) |
| **Apogee velocity** | Mach 3.5 |
| **Microgravity duration** | 4-6 minutes |
| **Flight duration** | 90 minutes (total mission) |
| **Ascent** | Rocket-powered vertical climb |
| **Descent** | Glide re-entry + powered landing |
| **Landing** | VTOL (retro-thrust) or runway (glide) |
| **Turnaround** | 72 hours between flights |
| **Design life** | 100 flights |

## Propulsion

| Parameter | Specification |
|-----------|--------------|
| **Primary** | Solar-thermal rocket (concentrated sunlight heats H2 propellant) |
| **Boost** | Hybrid rocket motor (HTPB + N2O) — initial ascent |
| **Thrust (boost)** | 120 kN |
| **Thrust (solar-thermal)** | 25 kN (sustained above 30km) |
| **Specific impulse** | 850s (solar-thermal), 280s (hybrid boost) |
| **Propellant** | Liquid hydrogen (solar-thermal) + N2O/HTPB (hybrid) |
| **RCS** | Cold gas nitrogen thrusters (16x) — attitude control |

## Power System

| Parameter | Specification |
|-----------|--------------|
| **Solar array** | 24m2 deployable GaAs panels (space-grade) |
| **Solar efficiency** | 32% (triple-junction GaAs) |
| **Solar concentrator** | Inflatable parabolic reflector (solar-thermal engine) |
| **Battery** | 40 kWh solid-state (avionics + life support) |
| **H2 fuel cell** | 15 kW PEM (backup power + water recovery) |
| **Water recovery** | Fuel cell exhaust H2O recycled for life support |

## Life Support

| System | Specification |
|--------|--------------|
| **Cabin pressure** | 101 kPa (sea-level equivalent) |
| **O2 supply** | Electrolysis from water + stored O2 tanks |
| **CO2 scrubbing** | LiOH canisters + regenerative molecular sieve |
| **Temperature** | Active thermal control (radiators + heaters) |
| **Radiation** | Polyethylene shielding + real-time dosimeter |
| **G-suit** | Integrated seat G-force protection (up to 4G) |

## Estimated Pricing

| Model | Price |
|-------|-------|
| **Per-seat ticket** (space tourism) | $250,000 |
| **Full vehicle purchase** | $2M - $4M |
| **1/8th fractional share** | $350,000 (50 flight hours/year) |

## Certification

| Authority | Standard | Status |
|-----------|---------|--------|
| FAA AST | Commercial space launch license | Required |
| FAA | Experimental airworthiness | Required |
| ITAR | Export control compliance | Required |

## Avionics Board — ULP-SSN (ePower Sequencing Family)

The Space Shuttle avionics are built on the **ULP-SSN** (Ultra-Low Power Space Sensor Node) board from the `ePower_sequencing_family_CAD/` product in this repo.

### ULP-SSN Board Specifications

| Parameter | Specification |
|-----------|--------------|
| **PCB** | 12-layer, 150mm x 100mm, IPC-6012 Class 3 (Space/Military) |
| **FPGA** | Xilinx Kintex UltraScale (sensor fusion + flight compute) |
| **MCU** | Ambiq Apollo4 Blue (ultra-low-power BLE, BGA-135) |
| **Security** | ATECC608B secure element (firmware hash verification) |
| **Radio** | UHF/VHF transceiver (ground telemetry downlink) |
| **Memory** | LPDDR4 (1.35V/1.5V) |
| **Power rails** | 3.3V core, 1.8V I/O, 0.9V FPGA core, AON (always-on) |
| **Power sequencing** | Hardware-managed with PMIC PGOOD interlocks |
| **PCB material** | Panasonic R-1566W (high-speed, low-loss) |
| **Surface finish** | ENIG (space-grade gold plating) |

### Role in Space Shuttle

```
ULP-SSN BOARD FUNCTIONS IN SPACE SHUTTLE

  FPGA (Kintex UltraScale)
  +-- Sensor fusion: IMU + star tracker + GPS
  +-- Real-time trajectory computation
  +-- RCS thruster firing patterns (16 channels)
  +-- Solar concentrator tracking servo
  +-- TPS thermal monitoring (temperature array)

  MCU (Apollo4 Blue)
  +-- Power sequencing & management
  +-- Life support monitoring (O2, CO2, pressure)
  +-- BLE: crew tablet/phone telemetry
  +-- Secure boot chain (ATECC608B verification)
  +-- Sleep/wake management for power conservation

  RADIO (UHF/VHF)
  +-- Ground telemetry downlink
  +-- Range safety commands (mission abort)
  +-- ADS-B transponder interface
```

### Power Sequencing for Space

The ULP-SSN board's power sequencing is critical for space operations:

- **Power-on boot**: PMIC enables rails in order: VCCINT -> VCCO -> Radio
- **Sleep entry** (orbit coast): FPGA I/O depowered, MCU enters deep sleep (uA draw)
- **Wake-up** (re-entry prep): Rails re-enabled, FPGA reconfigured, sensors calibrated
- **Emergency shutdown**: MCU writes shutdown flag, cuts all rails safely

### Cross-Reference

See full board design: [`ePower_sequencing_family_CAD/`](../ePower_sequencing_family_CAD/)
- `ulp_ssn.net` — Full netlist (FPGA + MCU + radio + power)
- `ulp_ssn_schematic.html` — Interactive schematic viewer
- `power_sequencing.html` — Timing diagrams (boot/sleep/wake/shutdown)
- `pcb_stackup.txt` — 12-layer space-grade stackup definition
- `decoupling_cap_map.csv` — Decoupling capacitor placement
