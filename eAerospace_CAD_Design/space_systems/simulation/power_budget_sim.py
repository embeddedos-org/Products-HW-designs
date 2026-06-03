#!/usr/bin/env python3
"""Power budget simulation for eCubeSat-3U On-Board Computer."""
components = {
    "GR712RC LEON3FT SoC": 2.5,
    "SRAM x4": 4 * 0.15,
    "NAND Flash": 0.08,
    "SpaceWire transceivers x4": 4 * 0.12,
    "CAN transceivers x2": 2 * 0.04,
    "Power system manager": 0.05,
    "RF Transceiver AD9364": 1.2,
    "Power monitors x2": 2 * 0.002,
    "Artix-7 FPGA": 0.8,
}
total = sum(components.values())
print("=" * 55)
print("eCubeSat-3U OBC — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"3.3V bus current: {total/3.3*1000:.0f} mA")
print(f"Solar array requirement (30% margin): {total*1.3:.2f} W")
