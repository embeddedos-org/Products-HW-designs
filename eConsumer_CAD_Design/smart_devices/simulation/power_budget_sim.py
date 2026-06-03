#!/usr/bin/env python3
"""Power budget simulation for eGlasses-AR Consumer AR Glasses."""
components = {
    "Snapdragon XR2+ Gen 1 SoC": 5.0,
    "LPDDR5 x4": 4 * 0.8,
    "UFS 3.1 storage": 0.5,
    "Dual micro-OLED displays": 2 * 0.8,
    "12MP camera": 0.5,
    "BLE SoC": 0.018,
    "Wi-Fi 6E module": 0.35,
    "4-mic array": 0.1,
    "Open-ear speakers": 0.5,
}
total = sum(components.values())
battery_mAh = 3000
battery_V = 3.7
runtime_h = battery_mAh * battery_V / 1000 / total
print("=" * 55)
print("eGlasses-AR Consumer AR Glasses — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"Battery runtime: {runtime_h:.1f} hours ({battery_mAh}mAh @ {battery_V}V)")
