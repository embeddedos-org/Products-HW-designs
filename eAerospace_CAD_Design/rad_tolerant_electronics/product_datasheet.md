# Radiation-Tolerant Electronics — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Radiation-tolerant building-block board set for missions that cannot afford full rad-hard silicon everywhere. Combines a rad-hard processor and antifuse FPGA core with latch-up-protected COTS peripherals, triple modular redundancy in fabric, and scrubbing of configuration memory.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eRAD-100 | Rad-tolerant processing core | Eurocard 6U |
| eRAD-LCL | Latch-up current limiter array | Eurocard 3U |
| eRAD-SCRUB | Configuration memory scrubber | Mezzanine |

## Electrical Specifications — eRAD-100
| Parameter | Specification |
|---|---|
| **Processor** | GR740 quad-core LEON4FT, 250MHz |
| **Antifuse logic** | RTAX2000S, immune to configuration upset |
| **Redundancy** | Triple modular redundancy with majority voting |
| **Scrubbing** | Configuration memory scrub cycle every 500ms |
| **Latch-up protection** | Per-rail current limiters, 10us trip, autonomous retry |
| **Total ionising dose** | 300 krad(Si) qualified |
| **Single-event upset** | <1e-10 errors/bit-day at GEO worst case |
| **Single-event latch-up** | Immune to 80 MeV-cm2/mg |
| **Displacement damage** | 1e12 protons/cm2 at 60 MeV |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 16 |
| **Dimensions** | 233mm x 220mm (6U Eurocard) |
| **Stackup** | Polyimide, buried vias, symmetric construction |
| **IPC Class** | Class 3/A per IPC-6012DS space addendum |
| **Finish** | Electroplated nickel-gold, staked and bonded |
| **Shielding** | Selective tantalum spot shielding over sensitive die |

## Compliance Targets
| Standard | Scope |
|---|---|
| MIL-STD-883 TM1019 | Total ionising dose test method |
| ESCC 22900 | TID steady-state irradiation test method |
| JESD57 | Single-event effects test procedures |
| ECSS-Q-ST-60-15C | Radiation hardness assurance |
