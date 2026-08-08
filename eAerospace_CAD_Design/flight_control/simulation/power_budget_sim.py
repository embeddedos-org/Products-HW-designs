#!/usr/bin/env python3
"""Power budget simulation for eFCS-2000 Flight Control Computer."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32H743 lane processors x6": 3.6,
    "Artix-7 XC7A100T I/O manager": 1.8,
    "ADIS16505 IMU x3": 0.63,
    "ARINC-429 Rx x2 / Tx x2": 0.22,
    "MIL-STD-1553B terminal x2": 0.7,
    "CAN FD transceiver x4": 0.14,
    "10BASE-T1L PHY x2": 0.18,
    "MRAM x3": 0.09,
    "Telemetry and housekeeping": 0.25,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.85

total = sum(loads.values())
print("=" * 62)
print("eFCS-2000 Flight Control Computer — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
