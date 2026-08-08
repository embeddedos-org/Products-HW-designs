# Swarm Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Research

## Product Overview
Swarm coordination node for decentralised multi-agent systems, providing relative ranging, mesh consensus and collision avoidance without any central controller or infrastructure. Ultra-wideband ranging gives relative position where GNSS is unavailable, which is the case indoors and in most of the environments swarms are proposed for.

## Electrical Specifications — eSWM-200
| Parameter | Specification |
|---|---|
| **Processor** | STM32H743 Cortex-M7 at 480MHz |
| **Relative ranging** | UWB two-way ranging, +/-10 cm at 60 m |
| **Mesh** | Sub-GHz mesh, 200 nodes per network, self-healing |
| **Consensus** | Byzantine-tolerant to one third faulty nodes |
| **Update rate** | 50 Hz neighbour state exchange |
| **Collision avoidance** | Decentralised reciprocal velocity obstacles |
| **Mass** | 42 g including antenna and battery |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 8 |
| **Dimensions** | 58mm x 46mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Constraint** | Mass-optimised; keep-out under UWB antenna feed |

## Compliance Targets
| Standard | Scope |
|---|---|
| ETSI EN 300 328 | 2.4GHz wideband transmission systems |
| ETSI EN 302 065 | Ultra-wideband short-range devices |
| FCC Part 15 Subpart F | Ultra-wideband operation |
