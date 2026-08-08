#!/usr/bin/env python3
"""Power budget simulation for eKSK-900 Public Information Kiosk."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "i.MX 8M Plus processor": 8.5,
    "32-inch sunlight-readable display": 120.0,
    "Wi-Fi 6 hotspot x2": 4.4,
    "5G backhaul modem": 6.5,
    "LPDDR4 x2": 2.2,
    "Camera and sensing": 0.9,
    "Thermal management": 15.0,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eKSK-900 Public Information Kiosk — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
