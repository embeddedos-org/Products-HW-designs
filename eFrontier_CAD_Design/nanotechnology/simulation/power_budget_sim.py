#!/usr/bin/env python3
"""Power budget simulation for eNANO-600 Scanning Probe Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq-7020 scan processor": 4.5,
    "Piezo drive amplifier x6": 7.2,
    "24-bit acquisition chain": 0.98,
    "Preamplifier and instrumentation stage": 1.16,
    "Low-noise analogue supplies": 2.4,
    "Ethernet and housekeeping": 0.85,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eNANO-600 Scanning Probe Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
