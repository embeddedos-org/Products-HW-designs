#!/usr/bin/env python3
"""Power budget simulation for eMDS-800 Maritime Surveillance Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 fusion processor": 4.2,
    "IWR6843 mmWave radar x2": 4.0,
    "ADRV9002 AIS receiver": 3.4,
    "Visible camera x2": 1.6,
    "LWIR thermal module": 0.65,
    "DDR4 x2": 1.6,
    "Ethernet PHY and SFP+": 2.9,
    "LTE backhaul modem": 2.2,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eMDS-800 Maritime Surveillance Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
