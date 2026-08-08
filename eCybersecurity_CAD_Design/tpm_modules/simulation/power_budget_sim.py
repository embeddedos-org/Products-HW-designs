#!/usr/bin/env python3
"""Power budget simulation for eTPM-20 Discrete TPM Module."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "SLB9670 TPM 2.0 active": 0.055,
    "STSAFE authentication": 0.008,
    "Regulator quiescent": 0.002,
}
BUS_V = 3.3
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eTPM-20 Discrete TPM Module — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
