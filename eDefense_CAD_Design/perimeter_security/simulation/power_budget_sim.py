#!/usr/bin/env python3
"""Power budget simulation for ePER-700 Perimeter Intrusion Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32H743 zone processor": 0.6,
    "ADS131M08 acquisition x4": 1.24,
    "IWR6843 zone radar x2": 4.0,
    "Fibre preamplifier x8": 0.88,
    "Ethernet switch and PHY x2": 2.0,
    "Isolated RS-485 and contacts": 1.15,
    "Recording and housekeeping": 0.6,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("ePER-700 Perimeter Intrusion Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
