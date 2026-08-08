#!/usr/bin/env python3
"""Power budget simulation for eSB-200 Secure Boot Subsystem."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32U575 boot processor": 0.14,
    "TPM 2.0 during measurement": 0.06,
    "ATECC608B signing": 0.014,
    "QSPI flash x2 read": 0.05,
    "FRAM state": 0.008,
    "Glitch and thermal monitoring": 0.012,
}
BUS_V = 5
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eSB-200 Secure Boot Subsystem — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
