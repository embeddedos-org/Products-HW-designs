#!/usr/bin/env python3
"""Power budget simulation for eZTG-1000 Zero Trust Gateway."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 enforcement processor": 4.2,
    "DDR4 x4": 3.2,
    "eMMC storage": 0.3,
    "Gigabit Ethernet PHY x4": 1.8,
    "Managed switch": 1.2,
    "SFP+ modules x2": 2.0,
    "Security elements and housekeeping": 0.5,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eZTG-1000 Zero Trust Gateway — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
