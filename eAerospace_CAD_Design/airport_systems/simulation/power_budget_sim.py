#!/usr/bin/env python3
"""Power budget simulation for eAPT-900 Airfield Systems Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 application processor": 4.2,
    "STM32G474 PLC modem x2": 0.7,
    "IWR6843 mmWave sensor x2": 4.0,
    "DDR4 x2": 1.6,
    "Gigabit PHY x2 + switch": 1.6,
    "Isolated RS-485 x4": 1.4,
    "Isolated CAN x2": 0.8,
    "Digital isolation and I/O": 0.6,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eAPT-900 Airfield Systems Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
