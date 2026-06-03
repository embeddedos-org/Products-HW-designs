# eAerospace CAD Design

> EmbeddedOS aerospace hardware portfolio covering aircraft components, avionics, UAV/drone systems, and space systems — all designed to run the eOS embedded stack.

## Product Lines

| Product | Category | Key ICs | IPC Class | Status |
|---|---|---|---|---|
| aircraft_components | Structural / Mechanical | STM32H7, CAN FD, ARINC-429 | Class 3 | Design |
| avionics | Flight computers, displays | RK3588S, STM32H7, ZED-F9P | Class 3 / DO-254 | Design |
| uav_drone_systems | UAV / VTOL / Swarm | RK3588S, STM32G4, nRF5340 | Class 3 | Design |
| space_systems | Satellite / CubeSat | LEON3FT, RTAX2000, GR712RC | Class 3 / ECSS | Design |

## Directory Structure

```
eAerospace_CAD_Design/
├── README.md
├── aircraft_components/
├── avionics/
├── uav_drone_systems/
├── space_systems/
├── docs/
│   ├── business_plan.md
│   └── regulatory_path.md
└── ebuild_simulation/
    └── README.md
```

## Related Repositories
| Repo | Relationship |
|---|---|
| [eos-aero](https://github.com/embeddedos-org/eos-aero) | AeroSwift firmware and software |
| [eos](https://github.com/embeddedos-org/eos) | Embedded OS for flight controllers |
| [EoSim](https://github.com/embeddedos-org/EoSim) | Flight simulation and digital twin |
