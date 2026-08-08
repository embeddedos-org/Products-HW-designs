#!/usr/bin/env python3
"""Power budget simulation for eC4I-7000 C4ISR Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ data link processor": 14.5,
    "Jetson Orin NX AI fusion": 25.0,
    "Cross-domain guard processors": 0.8,
    "LPDDR4 x4": 4.4,
    "eMMC x2": 0.6,
    "Gigabit Ethernet PHY x8": 3.6,
    "SFP+ modules x4": 4.0,
    "Security and housekeeping": 1.1,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eC4I-7000 C4ISR Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
