#!/usr/bin/env python3
"""Power budget simulation for eSIG-3600 SIGINT Receiver."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ADRV9002 receive channel x4": 13.6,
    "Zynq UltraScale+ processing": 16.0,
    "AD9265 IF digitiser x4": 4.8,
    "LMX2594 synthesiser x4": 2.8,
    "HMC7044 clock tree x2": 2.2,
    "10MHz OCXO": 1.8,
    "LPDDR4 x4": 4.4,
    "Storage and housekeeping": 1.6,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eSIG-3600 SIGINT Receiver — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
