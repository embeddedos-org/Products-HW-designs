#!/usr/bin/env python3
"""Power budget simulation for eFOR-900 Forensic Acquisition Appliance."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 acquisition processor": 4.2,
    "Artix-7 write-block fabric": 0.95,
    "DDR4 x4": 3.2,
    "eMMC x2": 0.6,
    "USB 3.0 transceiver x4": 1.6,
    "Gigabit Ethernet PHY x2": 0.9,
    "Operator display": 1.8,
    "Target media power": 6.0,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eFOR-900 Forensic Acquisition Appliance — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
