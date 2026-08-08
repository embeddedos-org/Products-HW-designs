#!/usr/bin/env python3
"""Power budget simulation for eSON-2400 Sonar Processing Unit."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ beamformer": 16.0,
    "ADS131M08 acquisition x8": 2.48,
    "AD9265 digitiser x2": 2.4,
    "Hydrophone preamplifier x16": 1.76,
    "Anti-alias filter stage": 0.96,
    "LPDDR4 x2": 2.2,
    "Clock distribution": 1.1,
    "Analogue reference and housekeeping": 1.2,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eSON-2400 Sonar Processing Unit — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
