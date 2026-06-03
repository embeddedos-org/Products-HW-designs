#!/usr/bin/env python3
"""Power budget simulation for eVCU-Pro Vehicle Control Unit."""
components = {
    "S32K344 MCU (active)": 0.25,
    "CAN FD transceivers x6": 6 * 0.04,
    "LIN transceivers x4": 4 * 0.01,
    "100BASE-T1 PHY x2": 2 * 0.18,
    "PMIC ASIL-D": 0.05,
    "System basis chip": 0.08,
    "Flash memory": 0.015,
}
total = sum(components.values())
print("=" * 55)
print("eVCU-Pro Vehicle Control Unit — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.1f} mW")
print("-" * 55)
print(f"{'TOTAL':<40} {total*1000:>6.1f} mW")
print(f"12V bus current: {total/12*1000:.1f} mA")
