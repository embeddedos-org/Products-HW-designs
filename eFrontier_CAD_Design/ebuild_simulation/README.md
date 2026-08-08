# eFrontier CAD Design — eBuild Simulation

## Overview
The eBuild simulation framework exercises these CAD designs against the eOS
embedded stack before any physical prototype is committed.

## Simulation Targets

| Product | Simulation Type | eOS Module |
|---|---|---|
| quantum_control | Power budget and thermal load | eOS real-time control |
| photonics | Power and thermal budget | eOS photonics control |
| nanotechnology | Power budget | eOS motion control |
| neuromorphic | Power budget | eOS spiking runtime |
| bioelectronics | Duty-cycled power | eOS biosignal stack |
| space_robotics | Power budget | eOS SpaceOS motion |
| swarm_systems | Duty-cycled power | eOS swarm runtime |

## Running Simulations

```bash
python3 eFrontier_CAD_Design/<product>/simulation/power_budget_sim.py
```

Every simulation in this division is executed by the repository gate:

```bash
python3 tools/validate_products.py --run eFrontier_CAD_Design
```
