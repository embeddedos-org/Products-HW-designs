#!/usr/bin/env python3
"""Power budget simulation for eHub-Pro Smart Home Hub."""
components = {
    "NXP i.MX 8M Mini SoC": 2.5,
    "LPDDR4X x2": 2 * 0.2,
    "eMMC": 0.15,
    "BLE + Zigbee SoC": 0.018,
    "Z-Wave module": 0.025,
    "Wi-Fi 6 module": 0.25,
    "GbE PHY": 0.18,
    "USB-C PD controller": 0.05,
}
total = sum(components.values())
print("=" * 55)
print("eHub-Pro Smart Home Hub — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V input current: {total/12*1000:.0f} mA")
