#!/usr/bin/env python3
"""Power budget simulation for eNEU-400 Neuromorphic Platform."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Neuromorphic ASIC (always-on perception)": 0.42,
    "i.MX RT1064 host bridge": 0.35,
    "iCE40 AER arbitration": 0.18,
    "DDR4 weight storage": 0.8,
    "Gigabit Ethernet PHY": 0.45,
    "USB 3.0 transceiver": 0.4,
    "Energy measurement": 0.05,
}
BUS_V = 5
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eNEU-400 Neuromorphic Platform — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
