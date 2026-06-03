#!/usr/bin/env python3
"""Power budget simulation for ePLC-1000 Industrial PLC."""
components = {
    "NXP i.MX 8M Plus SoC": 4.5,
    "LPDDR4X x4": 4 * 0.3,
    "eMMC storage": 0.2,
    "GbE PHY": 0.18,
    "USB hub + GbE": 0.25,
    "Digital isolators x2": 2 * 0.02,
    "RS-485 transceiver": 0.01,
    "CAN FD transceiver": 0.04,
    "32 DI opto-isolators": 32 * 0.005,
    "32 DO relay drivers": 32 * 0.01,
}
total = sum(components.values())
print("=" * 55)
print("ePLC-1000 Industrial PLC — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"24VDC bus current: {total/24*1000:.0f} mA")
