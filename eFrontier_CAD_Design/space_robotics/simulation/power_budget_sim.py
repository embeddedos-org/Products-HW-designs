#!/usr/bin/env python3
"""Power budget simulation for eSRB-900 Space Robotics Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "GR712RC control processor": 3.2,
    "RTG4 commutation fabric": 4.5,
    "Joint gate driver quiescent x7": 2.1,
    "Joint motor drive (7 axes, 40% duty)": 42.0,
    "Force/torque acquisition": 0.98,
    "SpaceWire and MRAM": 0.36,
    "Thermal heaters and housekeeping": 3.5,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.83

total = sum(loads.values())
print("=" * 62)
print("eSRB-900 Space Robotics Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
