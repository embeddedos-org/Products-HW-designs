#!/usr/bin/env python3
"""Power budget simulation for eTrafficCtrl AI Traffic Controller."""
components = {
    "NXP i.MX 8M Plus SoC": 4.5,
    "LPDDR4X x2": 2 * 0.3,
    "eMMC": 0.2,
    "4G LTE module (active)": 1.5,
    "V2X transceiver": 0.8,
    "Wi-Fi module": 0.25,
    "GbE PHY x4": 4 * 0.18,
    "Radar sensor": 2.0,
    "Camera (4K AI)": 3.5,
    "LED signal heads x12": 12 * 8.0,
}
total = sum(components.values())
electronics = total - 12 * 8.0
print("=" * 55)
print("eTrafficCtrl — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.2f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {electronics:>6.2f} W")
print(f"{'TOTAL (incl. LED signals)':<40} {total:>6.2f} W")
print(f"Annual energy: {total * 8760 / 1000:.0f} kWh")
