# ePower Sequencing Family — ULP-SSN Board

> **Ultra-Low Power Space Sensor Node**
> IPC-6012 Class 3 (Space/Military) rated avionics board

## Overview

The ULP-SSN is a space-grade compute and sensor fusion board designed for the ePAM Space Shuttle and Combo Unit avionics systems. It combines an FPGA for real-time flight computation with an ultra-low-power MCU for power management and secure boot.

## Key Specifications

| Parameter | Specification |
|-----------|--------------|
| **PCB** | 12-layer, 150mm x 100mm, 1.6mm thick |
| **Classification** | IPC-6012 Class 3 (Space/Military) |
| **FPGA** | Xilinx Kintex UltraScale |
| **MCU** | Ambiq Apollo4 Blue (BLE 5.3, ultra-low-power) |
| **Security** | ATECC608B secure element |
| **Radio** | UHF/VHF transceiver |
| **Memory** | LPDDR4 |
| **Material** | Panasonic R-1566W (low-loss, high-speed) |
| **Finish** | ENIG (space-grade gold) |

## Files

| File | Description |
|------|-------------|
| `ulp_ssn.net` | Complete KiCad netlist |
| `ulp_ssn_schematic.html` | Interactive schematic viewer (open in browser) |
| `power_sequencing.html` | Power-on/sleep/wake/shutdown timing diagrams |
| `pcb_stackup.txt` | 12-layer stackup definition with impedance control |
| `decoupling_cap_map.csv` | Decoupling capacitor placement map |

## Power Sequencing Modes

| Mode | Description |
|------|-------------|
| **Power-on boot** | PMIC enables rails sequentially: VCCINT -> VCCO -> Radio, with PGOOD interlocks |
| **Sleep entry** | FPGA I/O banks depowered, MCU enters deep sleep (microamp draw) |
| **Wake-up** | Rails re-enabled in sequence, FPGA reconfigured from flash |
| **Emergency shutdown** | MCU writes shutdown flag, cuts own LDO last |

## Used In

| Product | Role |
|---------|------|
| [ePAM Space Shuttle](../) | Primary avionics: sensor fusion, trajectory, RCS, telemetry |
| [ePAM Combo Unit](../../combo_unit/) | Space-mode avionics: same role during trans-atmospheric flight |

## 12-Layer PCB Stackup

```
 L1  TOP        Signal    1 oz    (BGA fanout, high-speed traces)
 L2  GND        Plane     2 oz    (primary reference, thermal)
 L3  PWR        Plane     1 oz    (3.3V / 1.8V pours)
 L4  SIG1       Signal    0.5 oz  (SPI, UART, GPIO)
 L5  GND2       Plane     1 oz    (inner reference)
 L6  SIG2       Signal    0.5 oz  (memory bus horizontal)
 L7  SIG3       Signal    0.5 oz  (memory bus vertical)
 L8  GND3       Plane     1 oz    (inner reference)
 L9  SIG4       Signal    0.5 oz  (FPGA config, misc)
 L10 PWR2       Plane     2 oz    (0.9V FPGA core / AON rails)
 L11 GND4       Plane     2 oz    (bottom reference, RF guard)
 L12 BOT        Signal    1 oz    (bottom-side routing)
```
