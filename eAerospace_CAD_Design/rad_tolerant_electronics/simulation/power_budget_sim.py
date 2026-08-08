#!/usr/bin/env python3
"""Power budget simulation for eRAD-100 Rad-Tolerant Processing Core."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "GR740 quad-core LEON4FT": 8.5,
    "RTAX2000S antifuse FPGA": 3.2,
    "RTG4 FPGA with scrubber": 4.5,
    "DDR4 with EDAC x4": 3.2,
    "MRAM x6": 0.18,
    "SpaceWire LVDS x6": 0.72,
    "Latch-up limiter overhead": 1.1,
    "Telemetry and housekeeping": 0.55,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.8

total = sum(loads.values())
print("=" * 62)
print("eRAD-100 Rad-Tolerant Processing Core — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
