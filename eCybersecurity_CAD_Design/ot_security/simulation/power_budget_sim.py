#!/usr/bin/env python3
"""Power budget simulation for eOTS-800 OT Security Appliance."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 inspection processor": 4.2,
    "DDR4 x2": 1.6,
    "eMMC storage": 0.3,
    "Gigabit Ethernet PHY x4": 1.8,
    "Switch fabric": 1.2,
    "Isolated serial interfaces": 1.05,
    "Housekeeping": 0.4,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eOTS-800 OT Security Appliance — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
