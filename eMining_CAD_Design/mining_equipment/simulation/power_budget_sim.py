#!/usr/bin/env python3
"""Power budget simulation for eHaul-Auto Autonomous Haul Truck Controller."""
components = {
    "NXP LS1046A SoC": 8.0,
    "NVIDIA Jetson Orin NX": 20.0,
    "Livox Mid-360 LiDAR x4": 4 * 8.0,
    "RTK GPS x2": 2 * 0.135,
    "77GHz radar x6": 6 * 2.5,
    "4G LTE module": 1.5,
    "Power monitors x4": 4 * 0.002,
}
total = sum(components.values())
print("=" * 55)
print("eHaul-Auto Mining Truck Controller — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.2f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.2f} W")
print(f"24V vehicle bus current: {total/24*1000:.0f} mA")
