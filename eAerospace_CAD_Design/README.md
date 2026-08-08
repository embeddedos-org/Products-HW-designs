# eAerospace CAD Design

> EmbeddedOS aerospace hardware portfolio covering aircraft components, avionics, UAV/drone systems, and space systems — all designed to run the eOS embedded stack.

## Product Lines

| Product | Category | Key ICs | IPC Class | Status |
|---|---|---|---|---|
| aircraft_components | Structural / Mechanical | STM32H7, CAN FD, ARINC-429 | Class 3 | Design |
| avionics | Flight computers, displays | RK3588S, STM32H7, ZED-F9P | Class 3 / DO-254 | Design |
| uav_drone_systems | UAV / VTOL / Swarm | RK3588S, STM32G4, nRF5340 | Class 3 | Design |
| space_systems | Satellite / CubeSat | LEON3FT, RTAX2000, GR712RC | Class 3 / ECSS | Design |
| flight_control | Fly-by-wire actuation and control law execution | STM32H743, XC7A100T, ADIS16505 | Class 3 | Design |
| satellite_platforms | GEO/LEO satellite bus avionics | GR712RC, RTG4, ISL71001 | Class 3 | Design |
| cubesat_systems | 1U-12U CubeSat OBC, EPS and ADCS | STM32H743, iCE40UP5K, ICM-42688-P | Class 3 | Design |
| ground_station | SDR ground segment, tracking and baseband | ADRV9002, XCZU3EG, ZED-F9T | Class 3 | Design |
| launch_systems | Launch vehicle flight computer and FTS | GR712RC, XC7A100T, ADIS16505 | Class 3 | Design |
| propulsion_control | Engine and thruster control electronics | STM32H743, ADS131M08, DRV8353 | Class 3 | Design |
| air_traffic_management | ADS-B, multilateration and surveillance fusion | ADRV9002, XCZU3EG, ZED-F9T | Class 3 | Design |
| airport_systems | AGL control, stand guidance, apron sensing | AM6254, DP83867, IWR6843 | Class 3 | Design |
| telemetry_systems | PCM/IRIG telemetry encoding and downlink | XC7A100T, ADRV9002, ADS8688 | Class 3 | Design |
| gnss_receivers | Multi-band GNSS, RTK, anti-spoof | ZED-F9P, ECP5, ADIS16470 | Class 3 | Design |
| navigation_systems | GNSS-denied inertial navigation | ADIS16505, XC7A35T, STM32H743 | Class 3 | Design |
| space_weather | Radiation, magnetometry and TEC monitoring | GR712RC, AD7124, MMC5983MA | Class 3 | Design |
| rad_tolerant_electronics | Rad-tolerant building blocks and SEE mitigation | RTAX2000S, GR740, ISL71001 | Class 3 | Design |

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
