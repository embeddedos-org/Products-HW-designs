#!/usr/bin/env python3
"""Power budget simulation for eSWX-200 Space Weather Instrument."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "GR712RC instrument controller": 3.2,
    "AD7124 ADC x4": 0.36,
    "ADS131M08 fluxgate ADC x2": 0.62,
    "Detector preamplifier chain": 0.88,
    "ZED-F9P GNSS occultation x2": 0.27,
    "SpaceWire LVDS interface": 0.24,
    "MRAM science buffer": 0.12,
    "Detector bias and housekeeping": 0.65,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.82

total = sum(loads.values())
print("=" * 62)
print("eSWX-200 Space Weather Instrument — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
