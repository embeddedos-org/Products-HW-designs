#!/usr/bin/env python3
"""Power budget simulation for eSiteSurvey Construction Survey Robot."""
components = {
    "RK3588S SoC": 8.0,
    "NVIDIA Jetson Orin NX": 20.0,
    "Livox Mid-360 LiDAR x2": 2 * 8.0,
    "RTK GPS x2": 2 * 0.135,
    "Sony IMX678 cameras x6": 6 * 0.35,
    "4G LTE module": 1.5,
    "UWB positioning IC": 0.1,
    "Drive motors (typical)": 4 * 50.0,
}
total = sum(components.values())
electronics = total - 4 * 50.0
print("=" * 55)
print("eSiteSurvey Construction Robot — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.2f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {electronics:>6.2f} W")
print(f"{'TOTAL (incl. drive motors)':<40} {total:>6.2f} W")
battery_Wh = 48 * 50
print(f"Battery (48V 50Ah): {battery_Wh:.0f} Wh")
print(f"Runtime: {battery_Wh/total:.1f} hours")
