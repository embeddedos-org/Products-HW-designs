# Autonomous Systems — Product Datasheet
> **Revision:** v1.0 | **Date:** 2026-06-03 | **Status:** Design Phase

## Product Family

| Model | Type | Payload | Speed | Navigation |
|---|---|---|---|---|
| eAMR-500 | Autonomous mobile robot | 500kg | 2 m/s | LiDAR SLAM |
| eWarehouse-1T | Warehouse robot | 1000kg | 1.5 m/s | QR + LiDAR |
| eDelivery-Bot | Last-mile delivery | 30kg | 1.2 m/s | GPS + LiDAR |
| eAgri-Tractor | Autonomous tractor | — | 3 m/s | RTK GPS + LiDAR |
| eSecurity-Patrol | Security patrol robot | — | 1.5 m/s | LiDAR SLAM |

## Electrical Specifications — eAMR-500
| Parameter | Specification |
|---|---|
| **SoC** | Rockchip RK3588S + NVIDIA Jetson Orin NX |
| **Navigation** | Livox Mid-360 LiDAR + u-blox ZED-F9P RTK GPS |
| **Vision** | 6× Sony IMX678 4K cameras (360° coverage) |
| **Drive** | 4× 500W BLDC hub motors |
| **Battery** | 48V 100Ah LiFePO4, 8h operation |
| **Safety** | ISO 3691-4, IEC 62061 SIL 2 |
| **Communication** | Wi-Fi 6, 4G LTE, ROS 2 |
