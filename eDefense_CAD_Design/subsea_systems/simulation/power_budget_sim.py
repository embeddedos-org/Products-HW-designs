#!/usr/bin/env python3
"""Power budget simulation for eSUB-400 Subsea Control Module."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32H743 controller x2": 1.2,
    "AD7124 ADC x4": 0.36,
    "RTD conditioning x4": 0.24,
    "10BASE-T1L PHY x2": 0.18,
    "Isolated RS-485 x2": 0.7,
    "Sensor amplification chain": 0.42,
    "Isolation and housekeeping": 0.55,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.84

total = sum(loads.values())
print("=" * 62)
print("eSUB-400 Subsea Control Module — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
