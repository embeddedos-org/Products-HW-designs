# Protection Equipment — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Detection | Standard |
|---|---|---|---|
| eBio-Gate | Biometric access control | Face + Iris + Fingerprint | FIPS 201-3 |
| ePerim-Sensor | Perimeter intrusion detection | Seismic + PIR + Radar | MIL-STD-810 |
| eDetect-CBRN | CBRN detection sensor | Chemical + Bio + Rad + Nuclear | STANAG 4632 |
| eScan-Pro | Security scanner (X-ray) | Dual-energy X-ray | IEC 62463 |

## Electrical Specifications — eBio-Gate
| Parameter | Specification |
|---|---|
| **SoC** | Rockchip RK3588S (face recognition NPU) |
| **Cameras** | 2× Sony IMX678 4K (visible + NIR) |
| **Iris scanner** | IriShield MK2120U |
| **Fingerprint** | Synaptics FS9500 optical |
| **Liveness detection** | 3D structured light |
| **Recognition speed** | <0.3s |
| **FAR** | <0.0001% |
| **FRR** | <0.1% |
