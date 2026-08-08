# eFrontier CAD Design

> EmbeddedOS frontier research hardware — quantum control, photonics, nanotechnology, neuromorphic compute, bioelectronics, space robotics and swarm systems.

## Product Lines

| Product | Category | Key Standard | Status |
|---|---|---|---|
| quantum_control | Qubit control and readout electronics | EN 61010-1 | Design |
| photonics | Photonic integrated circuit control and readout | IEC 60825-1 | Design |
| nanotechnology | Scanning probe and nanopositioning control | EN 61010-1 | Design |
| neuromorphic | Spiking neural network compute | CE / FCC Part 15B | Design |
| bioelectronics | Neural interface and electrophysiology | ISO 10993 / IEC 60601-1 | Design |
| space_robotics | Orbital manipulator and rover control | ECSS-Q-ST-60C / ECSS-E-ST-50-12C | Design |
| swarm_systems | Decentralised multi-agent coordination | ETSI EN 300 328 / CE | Design |

## Directory Structure

```
eFrontier_CAD_Design/
├── README.md
├── quantum_control/
├── photonics/
├── nanotechnology/
├── neuromorphic/
├── bioelectronics/
├── space_robotics/
├── swarm_systems/
├── docs/
│   ├── business_plan.md
│   └── regulatory_path.md
└── ebuild_simulation/
    └── README.md
```

Each product directory carries a datasheet, a costed bill of materials, a
runnable power simulation, and trees for CAD and PCB artefacts. The data is
generated from `tools/catalog/` and checked by `tools/validate_products.py`.
