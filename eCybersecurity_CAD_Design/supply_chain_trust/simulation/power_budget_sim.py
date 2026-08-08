#!/usr/bin/env python3
"""Power budget simulation for eSCT-700 Supply Chain Verification Station."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 station processor": 4.2,
    "MLX90640 thermal array x2": 0.36,
    "Optical inspection camera x2": 1.6,
    "ADS8688 characterisation x2": 0.66,
    "DDR4 x2": 1.6,
    "Operator display": 1.8,
    "DUT test power budget": 5.0,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eSCT-700 Supply Chain Verification Station — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
