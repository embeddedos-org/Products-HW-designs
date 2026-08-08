# eEdgeAI CAD Design — eBuild Simulation

## Overview
The eBuild simulation framework exercises these CAD designs against the eOS
embedded stack before any physical prototype is committed.

## Simulation Targets

| Product | Simulation Type | eOS Module |
|---|---|---|
| edge_ai_accelerators | Thermal and power budget | eOS eAI runtime |
| tinyml_platforms | Duty-cycled power and battery life | eOS eAI micro runtime |
| npu_subsystems | Power budget | eOS NPU HAL |
| vision_processing | Power budget | eOS eVision pipeline |
| speech_processing | Duty-cycled power | eOS eSpeech runtime |
| sensor_fusion | Power budget | eOS eFusion |
| slam_compute | Power budget | eOS eSLAM |
| inference_servers | Power budget | eOS eAI serving runtime |

## Running Simulations

```bash
python3 eEdgeAI_CAD_Design/<product>/simulation/power_budget_sim.py
```

Every simulation in this division is executed by the repository gate:

```bash
python3 tools/validate_products.py --run eEdgeAI_CAD_Design
```
