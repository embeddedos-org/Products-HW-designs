#!/usr/bin/env python3
"""Power budget simulation for eROT-400 Hardware Root of Trust."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "MAX32520 PUF processor": 0.22,
    "SE050 secure element": 0.045,
    "PolarFire crypto fabric": 1.35,
    "TPM 2.0": 0.06,
    "FRAM helper data": 0.016,
    "Attack detection monitoring": 0.05,
}
BUS_V = 5
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eROT-400 Hardware Root of Trust — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
