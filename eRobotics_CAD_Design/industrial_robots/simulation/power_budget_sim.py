#!/usr/bin/env python3
"""Power budget simulation for eArm-7 Collaborative Robot Controller."""
components = {
    "NXP i.MX 8M Plus SoC": 4.5,
    "Artix-7 FPGA": 3.5,
    "Motor gate drivers x7": 7 * 0.08,
    "Current sense amps x7": 7 * 0.001,
    "Safety co-processors x2": 2 * 0.15,
    "GbE PHY x4 (EtherCAT)": 4 * 0.18,
    "LPDDR4X x2": 2 * 0.3,
}
total_electronics = sum(components.values())
motor_peak_W = 7 * 150  # 7 joints × 150W peak each
print("=" * 55)
print("eArm-7 Robot Controller — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {total_electronics:>6.3f} W")
print(f"Motor peak power (7 joints): {motor_peak_W} W")
print(f"Total system peak: {total_electronics + motor_peak_W:.0f} W @ 48V")
print(f"48V bus current peak: {(total_electronics + motor_peak_W)/48*1000:.0f} mA")
