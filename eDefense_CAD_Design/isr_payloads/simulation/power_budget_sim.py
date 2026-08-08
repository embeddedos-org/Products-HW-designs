#!/usr/bin/env python3
"""Power budget simulation for eISR-1200 ISR Payload."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Jetson Orin NX inference": 25.0,
    "Electro-optical sensor x2": 1.6,
    "LWIR thermal core": 0.65,
    "Artix-7 sync and gimbal control": 0.95,
    "Gimbal IMU": 0.21,
    "Gimbal BLDC drive (4 axes)": 18.0,
    "LPDDR4 x2": 2.2,
    "Ethernet PHY x2": 0.9,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eISR-1200 ISR Payload — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
