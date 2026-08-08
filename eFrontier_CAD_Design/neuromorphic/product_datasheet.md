# Neuromorphic Computing Platforms — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Research

## Product Overview
Spiking neural network platform pairing a neuromorphic ASIC with an event-based vision sensor interface, targeting always-on perception at milliwatt power. The efficiency argument only holds for genuinely sparse, event-driven workloads; dense frame-based inference remains better served by a conventional NPU.

## Electrical Specifications — eNEU-400
| Parameter | Specification |
|---|---|
| **Neuromorphic core** | 256k spiking neurons, 64M synapses |
| **Event throughput** | 180M synaptic operations per second |
| **Energy per synaptic op** | ~24 pJ at nominal supply |
| **Learning** | On-chip STDP and three-factor local learning rules |
| **Sensor interface** | Event-based vision sensor input, AER protocol |
| **Host interface** | 1GbE and USB 3.0 |
| **Power envelope** | 1.8W typical for always-on perception |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 120mm x 100mm |
| **IPC Class** | Class 2 |
| **Finish** | ENIG |
| **Stackup** | Length-matched AER event bus routing |

## Compliance Targets
| Standard | Scope |
|---|---|
| FCC Part 15 Subpart B | Unintentional radiator emissions |
| EN 55032 Class B | Emissions |
| IEC 62368-1 | Equipment safety |
