#!/usr/bin/env python3
"""Power budget simulation for eNav-ECDIS Navigation System."""
components = {
    "NXP i.MX 8M Plus SoC": 4.5,
    "LPDDR4X x2": 2 * 0.3,
    "eMMC": 0.2,
    "GbE PHY x4": 4 * 0.18,
    "27-inch IPS display": 35.0,
    "NMEA 2000 controller": 0.05,
    "Wi-Fi module": 0.25,
}
total = sum(components.values())
print("=" * 55)
print("eNav-ECDIS Navigation System — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"24VDC maritime bus current: {total/24*1000:.0f} mA")
