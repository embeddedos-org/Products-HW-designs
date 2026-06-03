#!/usr/bin/env python3
"""Power budget simulation for eFC-1000 Avionics Flight Computer."""
components = {
    "RK3588S SoC (full load)": 8.0,
    "STM32H7B3 x2": 2 * 0.25,
    "ARINC-429 Rx x4": 4 * 0.025,
    "ARINC-429 Tx x4": 4 * 0.030,
    "MIL-STD-1553B x2": 2 * 0.35,
    "RTK GPS x2": 2 * 0.135,
    "IMU x2": 2 * 0.065,
    "Xilinx Artix-7 FPGA": 1.5,
    "GbE PHY x4": 4 * 0.18,
    "LPDDR5 x2": 2 * 0.8,
    "eMMC": 0.3,
}
total = sum(components.values())
print("=" * 55)
print("eFC-1000 Avionics Flight Computer — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"28V bus current: {total/28*1000:.0f} mA (at 85% DCDC efficiency: {total/0.85:.2f} W)")
