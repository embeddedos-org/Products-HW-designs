# eAerospace — eBuild Simulation

## Overview
The eBuild simulation framework will test and validate all eAerospace CAD designs against the eOS embedded stack before physical prototyping.

## Simulation Targets

| Product | Simulation Type | eOS Module |
|---|---|---|
| aircraft_components | Power budget, CAN FD bus timing | eOS HAL, eOS CAN |
| avionics | ARINC-429 data flow, MIL-STD-1553B | eOS ARINC, eOS 1553 |
| uav_drone_systems | Flight dynamics, sensor fusion | eOS AeroOS, eAI |
| space_systems | Orbital power budget, SpaceWire | eOS SpaceOS |

## Running Simulations
```bash
cd eAerospace_CAD_Design/{product}/simulation/
python3 power_budget_sim.py
```

## Integration with EoSim
All simulation results feed into the [EoSim](https://github.com/embeddedos-org/EoSim) digital twin platform for hardware-in-the-loop testing.
