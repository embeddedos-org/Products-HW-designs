#!/usr/bin/env python3
"""Power budget simulation for eEMR-800 Incident Command Unit."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 command processor": 4.2,
    "5G backhaul modem": 6.5,
    "Satellite modem (standby)": 0.9,
    "Wi-Fi 6 access point x2": 4.4,
    "Sub-GHz mesh x2": 0.9,
    "UWB positioning x2": 0.7,
    "Console display": 1.8,
    "Switch and housekeeping": 1.6,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eEMR-800 Incident Command Unit — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
