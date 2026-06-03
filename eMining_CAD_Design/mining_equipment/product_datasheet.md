# Mining Equipment — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Standard |
|---|---|---|
| eHaul-Auto | Autonomous haul truck controller | ISO 17757 |
| eMineMonitor | Mine environment monitoring system | IECEx Zone 1 |
| eMine-UAV | Underground inspection drone | ATEX Zone 2 |
| eHeavy-Ctrl | Heavy equipment controller | ISO 15998 |
| eWorker-Safety | Worker proximity safety device | ISO 17757 |

## Electrical Specifications — eHaul-Auto
| Parameter | Specification |
|---|---|
| **CPU** | NXP LS1046A (quad Cortex-A72) + NVIDIA Jetson Orin NX |
| **Navigation** | LiDAR ×4, RTK GPS ×2, radar ×6 |
| **Safety** | ISO 17757, IEC 62061 SIL 3 |
| **Communication** | 900MHz mesh, 4G LTE, Wi-Fi 6 |
| **Power** | 24VDC vehicle bus |
| **Environmental** | IP67, MIL-STD-810H |
