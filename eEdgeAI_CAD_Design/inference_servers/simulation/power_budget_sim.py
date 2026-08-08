#!/usr/bin/env python3
"""Power budget simulation for eINF-4000 Edge Inference Server."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Jetson Orin NX x4 (sustained)": 100.0,
    "AM6254 management processor": 4.2,
    "Ethernet switch x2 + PHY x4": 3.4,
    "DDR4 and eMMC": 2.2,
    "SFP+ modules x2": 2.0,
    "Cooling fans x4": 9.6,
    "Telemetry and housekeeping": 1.2,
}
BUS_V = 48
DCDC_EFFICIENCY = 0.92

total = sum(loads.values())
print("=" * 62)
print("eINF-4000 Edge Inference Server — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
