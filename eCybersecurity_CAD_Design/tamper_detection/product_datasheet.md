# Tamper Detection Subsystems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Board-level tamper detection subsystem monitoring enclosure switches, light ingress, temperature excursion and supply glitching, with an event log that survives power loss. Distinct from the anti-tamper response subsystem: this detects and records, leaving the response policy to the protected system.

## Electrical Specifications — eTD-300
| Parameter | Specification |
|---|---|
| **Sensors** | Enclosure switch, ambient light, temperature, supply glitch, mesh |
| **Mesh monitoring** | Resistance and capacitance, 0.1% deviation threshold |
| **Temperature window** | Configurable, default -20degC to +85degC |
| **Response time** | <5ms from event to logged and signalled |
| **Event log** | FRAM, 4096 timestamped events, survives power loss |
| **Backup power** | Coin cell, 10-year monitoring life |
| **Output** | Open-drain alarm, I2C status, zeroise strobe |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 75mm x 55mm |
| **IPC Class** | Class 3 |
| **Finish** | ENIG |
| **Security** | Mesh sense traces on layers 2 and 7 |

## Compliance Targets
| Standard | Scope |
|---|---|
| FIPS 140-3 Level 3 | Cryptographic module physical security |
| IEC 62443-4-2 | Component security requirements |
| EN 50131 Grade 3 | Alarm system tamper requirements |
