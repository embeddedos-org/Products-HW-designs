#!/usr/bin/env python3
"""Power budget simulation for eGOV-500 E-Government Terminal."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 processor": 4.2,
    "Imaging cameras x3": 3.0,
    "DDR4 x2": 1.6,
    "Interaction display": 1.8,
    "Secure elements and TPM": 0.15,
    "Ethernet and USB": 1.7,
    "Printer interface": 2.5,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eGOV-500 E-Government Terminal — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
