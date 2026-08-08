#!/usr/bin/env python3
"""Power budget simulation for eSE-100 Secure Element Carrier."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "SE050 active crypto operation": 0.045,
    "ATECC608B active": 0.014,
    "STSAFE-A110 active": 0.008,
    "Regulator quiescent": 0.001,
}
BUS_V = 3.3
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eSE-100 Secure Element Carrier — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
