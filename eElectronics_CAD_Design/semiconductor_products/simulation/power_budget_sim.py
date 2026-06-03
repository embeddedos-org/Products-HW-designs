#!/usr/bin/env python3
"""Power budget simulation for eASIC-Vision evaluation board."""
components = {
    "eASIC-Vision ASIC (typical)": 5.0,
    "LPDDR5 x4": 4 * 0.8,
    "Artix-7 FPGA (PCIe bridge)": 1.5,
    "GbE PHY x4": 4 * 0.18,
    "USB-C PD controller": 0.05,
    "Board regulators": 0.5,
}
total = sum(components.values())
print("=" * 55)
print("eASIC-Vision Evaluation Board — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V input current: {total/12*1000:.0f} mA")
print(f"Performance/Watt: {100/5:.0f} TOPS/W (ASIC only)")
