#!/usr/bin/env python3
"""Power budget simulation for eTCU-Pro Train Control Unit."""
components = {
    "NXP LS1043A SoC": 5.0,
    "STM32H7B3 safety MCU x2": 2 * 0.12,
    "DDR4 ECC x2": 2 * 0.4,
    "eMMC": 0.2,
    "GbE PHY x4": 4 * 0.18,
    "CAN FD transceivers x2": 2 * 0.04,
    "RS-485 transceivers x2": 2 * 0.01,
    "Digital isolators x2": 2 * 0.02,
}
total = sum(components.values())
print("=" * 55)
print("eTCU-Pro Train Control Unit — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"24VDC railway bus current: {total/24*1000:.0f} mA")
