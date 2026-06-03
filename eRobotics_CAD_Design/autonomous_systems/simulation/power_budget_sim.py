#!/usr/bin/env python3
"""Power budget simulation for eAMR-500 Autonomous Mobile Robot."""
components = {
    "RK3588S SoC": 8.0,
    "NVIDIA Jetson Orin NX": 20.0,
    "Livox Mid-360 LiDAR": 8.0,
    "RTK GPS x2": 2 * 0.135,
    "Sony IMX678 cameras x6": 6 * 0.35,
    "Motor gate drivers x4": 4 * 0.08,
    "4G LTE module": 1.5,
    "Battery management IC": 0.05,
    "Hub motors x4 (typical load)": 4 * 100.0,
}
total = sum(components.values())
electronics = total - 4 * 100.0
print("=" * 55)
print("eAMR-500 Autonomous Robot — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>7.2f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {electronics:>7.2f} W")
print(f"{'TOTAL (incl. motors @ 50% load)':<40} {total:>7.2f} W")
print(f"48V LiFePO4 100Ah capacity: {48*100:.0f} Wh")
print(f"Runtime at typical load: {48*100/total:.1f} h")
