#!/usr/bin/env python3
"""Power budget simulation for ePQC-500 Post-Quantum Accelerator."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "PolarFire lattice fabric": 6.8,
    "MAX32520 key custodian": 0.22,
    "DDR4 x2": 1.6,
    "Gigabit Ethernet PHY x2": 0.9,
    "Clock generation": 1.1,
    "Side-channel monitoring": 0.3,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("ePQC-500 Post-Quantum Accelerator — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
