#!/usr/bin/env python3
"""Power budget simulation for eNAV-5000 Naval Combat Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ XCZU3EG": 14.5,
    "LPDDR4 x4": 4.4,
    "eMMC x2": 0.6,
    "Gigabit Ethernet PHY x4": 1.8,
    "PTP timing PHY x2": 1.0,
    "SFP+ modules x4": 4.0,
    "Telemetry and housekeeping": 0.7,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.85

total = sum(loads.values())
print("=" * 62)
print("eNAV-5000 Naval Combat Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
