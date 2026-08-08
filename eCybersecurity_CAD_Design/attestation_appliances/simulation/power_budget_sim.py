#!/usr/bin/env python3
"""Power budget simulation for eATT-600 Attestation Verifier."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 appraisal processor": 4.2,
    "SE050 signing element x2": 0.09,
    "DDR4 x4": 3.2,
    "eMMC x2": 0.6,
    "Gigabit Ethernet PHY x2": 0.9,
    "TPM and housekeeping": 0.4,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eATT-600 Attestation Verifier — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
