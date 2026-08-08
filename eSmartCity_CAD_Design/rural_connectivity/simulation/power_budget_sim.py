#!/usr/bin/env python3
"""Power budget simulation for eRUR-700 Rural Connectivity Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ baseband": 16.0,
    "ADRV9002 transceiver x2": 6.8,
    "RF power amplifier stage": 42.0,
    "LMX2594 synthesiser x2": 1.4,
    "OCXO and GNSS timing": 2.1,
    "LPDDR4 x4": 4.4,
    "Backhaul radio": 8.5,
    "Ethernet and housekeeping": 2.4,
}
BUS_V = 48
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eRUR-700 Rural Connectivity Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
