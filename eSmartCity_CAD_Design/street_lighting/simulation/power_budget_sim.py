#!/usr/bin/env python3
"""Power budget simulation for eSL-400 Street Lighting Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32G474 controller": 0.28,
    "LoRaWAN transceiver (idle listen)": 0.02,
    "Energy metering x2": 0.03,
    "Motion and ambient sensing": 0.04,
    "Isolation and DALI drive": 0.16,
    "Regulator overhead": 0.12,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.85

total = sum(loads.values())
print("=" * 62)
print("eSL-400 Street Lighting Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
