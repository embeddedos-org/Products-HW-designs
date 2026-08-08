#!/usr/bin/env python3
"""Power budget simulation for ePS-1200 Public Safety Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 bridging processor": 4.2,
    "5G NR modem": 6.5,
    "ADRV9002 legacy transceiver": 3.4,
    "GNSS and IMU": 0.21,
    "DDR4 x2": 1.6,
    "Gigabit Ethernet PHY x2": 0.9,
    "Charger and housekeeping": 0.8,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("ePS-1200 Public Safety Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
