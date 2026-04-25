# Combo Unit — Trans-Atmospheric Vehicle Product Datasheet

## Overview

The Combo Unit is the ultimate vehicle: a 4-seat craft that operates as an urban drone (low altitude), transitions through the atmosphere, and reaches suborbital space. The "Trans-Atmospheric" design handles both aerodynamic lift (drone mode) and reaction mass (space mode).

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Type** | Trans-atmospheric hybrid (eVTOL + suborbital) |
| **Seats** | 4 (1 pilot + 3 passengers) |
| **Length** | 11m |
| **Wingspan** | 10m (rotors) / 6m (wings only, rotors retracted) |
| **Height** | 3.5m |
| **Empty weight** | 2,800 kg |
| **MTOW** | 4,800 kg |
| **Body material** | Ti-6Al-4V frame + carbon-fiber/aerogel skin + ceramic TPS |

## Trans-Atmospheric Flight Profile

```
ALTITUDE
100km  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ KARMAN LINE ─ ─ ─ ─ ─ ─
                              ╱ ╲
                            ╱     ╲    SPACE MODE
                          ╱ Solar-  ╲   (Solar-thermal +
                        ╱  thermal   ╲   RCS thrusters)
30km   ─ ─ ─ ─ ─ ─ ─╱─ ─ ─ ─ ─ ─ ─ ╲─ ─ ─ ─ ─ ─ ─ ─ ─
                    ╱                   ╲
                  ╱  TRANSITION          ╲  TRANSITION
                ╱    (Rotors retract,      ╲ (Rotors deploy,
              ╱       rocket ignites)       ╲  glide descent)
500m   ─ ─ ╱─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╲─ ─ ─ ─ ─ ─
          ╱                                   ╲
        ╱   DRONE MODE                         ╲  DRONE MODE
      ╱     (8x tilt-rotors, DEP)                ╲ (VTOL landing)
0m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    TAKEOFF                                      LANDING
```

## Operating Modes

| Mode | Altitude | Propulsion | Speed |
|------|----------|-----------|-------|
| **Drone** | 0-500m | 8x electric tilt-rotors | 0-300 km/h |
| **Transition** | 500m-30km | Rotors retract + hybrid rocket ignites | 300-1,500 km/h |
| **Space** | 30km-100km+ | Solar-thermal rocket + RCS | Mach 3+ |
| **Re-entry** | 100km-500m | Glide + thermal protection | Controlled descent |
| **Landing** | 500m-0 | Rotors deploy + VTOL | 0-50 km/h |

## Propulsion

| System | Specification |
|--------|--------------|
| **Drone rotors** | 8x 75kW PMSM tilt-rotor (retractable into body) |
| **Hybrid rocket** | 200 kN thrust (HTPB + N2O) — atmospheric climb |
| **Solar-thermal** | 25 kN thrust (concentrated sunlight heats H2) |
| **RCS** | 16x cold gas N2 thrusters |
| **Total drone power** | 600 kW electric |
| **Total rocket thrust** | 225 kN |

## Power System

| Parameter | Specification |
|-----------|--------------|
| **Solar (atmospheric)** | 20m2 perovskite cells (wings + body) |
| **Solar (space)** | 30m2 deployable GaAs panels |
| **Battery** | 150 kWh solid-state (drone mode + avionics) |
| **H2 fuel cell** | 50 kW PEM (transition power + backup) |
| **H2 storage** | 15 kg compressed H2 (700 bar Type IV tanks) |

## Estimated Pricing

| Model | Price |
|-------|-------|
| **Full vehicle** | $5M - $9M |
| **1/16th fractional share** | $400,000 (25 flight hours/year) |
| **Managed fleet unit** | $7M (includes 5-year maintenance) |

## Design Challenges

| Challenge | Solution |
|-----------|---------|
| Weight vs. protection | Carbon-fiber/aerogel composite (light + insulating) |
| Dual atmosphere operation | Retractable rotors reduce drag in space transition |
| Thermal management | Ceramic TPS tiles + active cooling channels |
| Regulation | Dual FAA Part 135 + AST commercial space license |
| Power density | Solar-thermal rocket eliminates heavy chemical propellant |

## Avionics Board — ULP-SSN (ePower Sequencing Family)

The Combo Unit avionics are built on the **ULP-SSN** (Ultra-Low Power Space Sensor Node) board from the `ePower_sequencing_family_CAD/` product in this repo.

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

### Role in Combo Unit (Space Mode)

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
