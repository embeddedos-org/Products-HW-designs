#!/usr/bin/env python3
"""Power budget simulation for eSAT-8000 Satellite Platform Computer."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "GR712RC LEON3FT processor": 3.2,
    "RTG4 FPGA (SpaceWire router)": 4.5,
    "DDR4 with EDAC x2": 1.6,
    "SpaceWire LVDS x8": 0.96,
    "MIL-STD-1553B terminal x2": 0.7,
    "ADIS16505 IMU x2": 0.42,
    "MRAM x4": 0.12,
    "Telemetry and housekeeping": 0.4,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.82

total = sum(loads.values())
print("=" * 62)
print("eSAT-8000 Satellite Platform Computer — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
