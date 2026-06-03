#!/usr/bin/env python3
"""Power budget simulation for eBio-Gate Biometric Access Control."""
components = {
    "RK3588S SoC (face recognition)": 8.0,
    "Sony IMX678 cameras x2": 2 * 0.35,
    "Fingerprint sensor": 0.08,
    "BLE module": 0.018,
    "LPDDR5 x2": 2 * 0.8,
    "eMMC": 0.3,
    "GbE PHY": 0.18,
    "Structured light projector": 1.5,
    "IR illuminators x4": 4 * 0.5,
}
total = sum(components.values())
print("=" * 55)
print("eBio-Gate Biometric System — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V PoE budget: {total/12*1000:.0f} mA (PoE+ = 30W max)")
