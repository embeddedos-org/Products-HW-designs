#!/usr/bin/env python3
"""Power budget simulation for eSurgBot-7 Surgical Robot Controller."""
components = {
    "RK3588S SoC": 8.0,
    "Artix-7 FPGA": 3.5,
    "Motor gate drivers x7": 7 * 0.08,
    "Current sense amps x7": 7 * 0.001,
    "Digital isolators x2": 2 * 0.02,
    "GbE PHY x4": 4 * 0.18,
    "Safety co-processors x2": 2 * 0.15,
}
total = sum(components.values())
print("=" * 55)
print("eSurgBot-7 Controller — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL (electronics)':<40} {total:>6.3f} W")
print(f"Motor peak power (7x Maxon EC-i 40): {7*40:.0f} W")
print(f"Total system peak: {total + 7*40:.0f} W @ 48V")
