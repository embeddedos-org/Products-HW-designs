#!/usr/bin/env python3
"""Power budget simulation for eLCS-1500 Vehicle Architecture Controller."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "AM6254 processor": 4.2,
    "Artix-7 I/O FPGA": 0.95,
    "DDR4 x2": 1.6,
    "Ethernet switch x2 + PHY x4": 3.4,
    "CAN FD controller x8": 0.72,
    "RS-422 interface x4": 0.28,
    "Digital isolation x12": 0.9,
    "Housekeeping": 0.6,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eLCS-1500 Vehicle Architecture Controller — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
