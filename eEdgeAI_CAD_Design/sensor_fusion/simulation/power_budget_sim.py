#!/usr/bin/env python3
"""Power budget simulation for eSFU-500 Sensor Fusion Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 fusion processor": 4.2,
    "IWR6843 radar x2": 4.0,
    "Camera input x4": 3.2,
    "IMU x2": 0.14,
    "DDR4 x2": 1.6,
    "Automotive Ethernet PHY x4": 1.8,
    "CAN FD x4 and PTP": 0.72,
    "GNSS and housekeeping": 0.55,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eSFU-500 Sensor Fusion Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
