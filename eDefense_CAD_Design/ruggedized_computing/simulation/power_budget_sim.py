#!/usr/bin/env python3
"""Power budget simulation for eRGD-2000 Rugged Mission Computer."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "i.MX 8M Plus processor": 8.5,
    "LPDDR4 x2": 2.2,
    "eMMC x2": 0.6,
    "Gigabit Ethernet PHY x4": 1.8,
    "USB 3.0 transceiver x4": 1.6,
    "CAN FD and RS-422": 0.64,
    "TPM and housekeeping": 0.5,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eRGD-2000 Rugged Mission Computer — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
