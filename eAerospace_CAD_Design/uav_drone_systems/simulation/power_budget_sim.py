#!/usr/bin/env python3
"""Power budget simulation for eFW-1000 UAV Flight Controller."""
components = {
    "RK3588S SoC": 8.0,
    "STM32H7B3 x2": 2 * 0.25,
    "ZED-F9P GPS x2": 2 * 0.135,
    "G362P IMU x2": 2 * 0.065,
    "Livox Mid-360 LiDAR": 8.0,
    "Sony IMX678 cameras x3": 3 * 0.35,
    "LoRa SX1276": 0.12,
    "4G LTE module": 1.5,
    "V2X TEKTON3": 0.8,
    "Motor drivers x8": 8 * 0.05,
    "Power monitors x4": 4 * 0.002,
}
total = sum(components.values())
print("=" * 55)
print("eFW-1000 UAV Flight Controller — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"4S LiPo (14.8V) current: {total/14.8*1000:.0f} mA")
