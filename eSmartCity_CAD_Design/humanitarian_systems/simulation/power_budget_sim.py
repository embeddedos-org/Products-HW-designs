#!/usr/bin/env python3
"""Power budget simulation for eHUM-400 Humanitarian Field Kit."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 processor": 4.2,
    "Satellite modems": 3.1,
    "Wi-Fi 6 access point x2": 4.4,
    "LoRa mesh gateway": 0.45,
    "Cold chain monitoring": 0.62,
    "DDR4 and storage": 2.2,
    "Operator display": 1.8,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eHUM-400 Humanitarian Field Kit — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
