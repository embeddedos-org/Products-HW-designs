# Space Weather Monitoring — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-08-08 | **Status:** Design Phase

## Product Overview
Space weather instrument package measuring energetic particle flux, total ionising dose, magnetic field, and ionospheric total electron content. Flown as a hosted payload or on a dedicated smallsat, feeding both spacecraft anomaly attribution and ground forecasting models.

## Product Family

| Unit | Function | Form Factor |
|---|---|---|
| eSWX-200 | Space weather instrument controller | Eurocard 3U |
| eSWX-PD | Particle detector head | Aperture 25mm |
| eSWX-MAG | Boom-mounted fluxgate magnetometer | Boom head |

## Electrical Specifications — eSWX-200
| Parameter | Specification |
|---|---|
| **Controller** | GR712RC rad-hard dual-core LEON3FT |
| **Particle detection** | Silicon telescope, 0.1-100 MeV protons, 0.05-10 MeV electrons |
| **Dosimetry** | RADFET total ionising dose, 0.1 rad resolution |
| **Magnetometer** | Fluxgate triad, +/-65000 nT, 0.1 nT resolution |
| **TEC measurement** | Dual-frequency GNSS occultation, 0.1 TECU |
| **Sample rate** | 1Hz nominal, 20Hz burst during events |
| **Data volume** | 180 MB/day nominal, 900 MB/day in burst |
| **Interfaces** | SpaceWire x2, CAN FD, MIL-STD-1553B |
| **Total ionising dose** | 100 krad(Si) instrument survival |

## PCB Specifications
| Parameter | Value |
|---|---|
| **Layers** | 12 |
| **Dimensions** | 160mm x 100mm (3U Eurocard) |
| **Stackup** | Guarded analogue island for detector bias |
| **IPC Class** | Class 3/A per IPC-6012DS |
| **Finish** | Electroplated nickel-gold, staked, conformal coated |
| **Outgassing** | ASTM E595, TML < 1.0%, CVCM < 0.1% |

## Compliance Targets
| Standard | Scope |
|---|---|
| ECSS-E-ST-10-04C | Space environment specification |
| ISO 15390 | Galactic cosmic ray model reference |
| ECSS-Q-ST-60C | EEE component selection and screening |
| ECSS-E-ST-50-12C | SpaceWire interface |
