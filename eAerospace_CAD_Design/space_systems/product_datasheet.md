# Space Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Overview
Space-grade hardware portfolio: satellite buses, 1U/3U/6U CubeSats, reaction wheels, star trackers, deployable solar arrays, electric propulsion modules, and ground station hardware — all running radiation-hardened eOS.

## Product Family

| Model | Type | Mass | Power | Orbit |
|---|---|---|---|---|
| eSat-Bus-100 | 100kg satellite bus | 100kg | 200W | LEO/MEO |
| eCubeSat-3U | 3U CubeSat | 4kg | 10W | LEO |
| eRW-0.1 | Reaction wheel 0.1 Nms | 0.8kg | 5W peak | — |
| eST-200 | Star tracker | 0.35kg | 1.5W | — |
| eSA-50 | Deployable solar array 50W | 2kg | 50W | LEO |
| eEPS-5 | Electric propulsion module | 3kg | 50W | — |

## Electrical Specifications — eCubeSat-3U OBC
| Parameter | Specification |
|---|---|
| **CPU** | GR712RC LEON3FT dual-core SPARC V8 (rad-hard) |
| **Memory** | 256MB SDRAM (rad-hard) + 4GB NAND Flash |
| **Interfaces** | SpaceWire ×4, CAN ×2, UART ×8, SPI ×4, I2C ×4 |
| **Power** | 3.3V / 5V / 12V from EPS |
| **TID tolerance** | 100 krad (Si) |
| **SEL immunity** | LET > 60 MeV·cm²/mg |
| **ECSS** | ECSS-E-ST-50-12C compliant |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 96mm × 90mm (PC/104 CubeSat standard) |
| **IPC Class** | Class 3 Space |
| **Surface finish** | ENIG |
| **PCB material** | Isola 370HR (high-Tg) |
