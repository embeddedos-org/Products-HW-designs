#!/usr/bin/env python3
"""Power budget simulation for eDCDC-5kW Bidirectional DC-DC Converter."""
rated = 5000
eff = 0.982
losses = rated * (1 - eff)
components = {
    "STM32H7B3 MCU": 0.12,
    "TMS320F28379D DSP": 0.5,
    "SiC MOSFET losses x8": losses * 0.6,
    "Transformer core losses": losses * 0.25,
    "Gate drivers x8": 8 * 0.05,
    "Current sensors x2": 2 * 0.01,
    "Digital isolators x4": 4 * 0.02,
    "Cooling fan": 10.0,
}
total = sum(components.values())
print("=" * 55)
print("eDCDC-5kW Bidirectional Converter — Loss Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<45} {w:>6.1f} W")
print("-" * 55)
print(f"{'TOTAL losses':<45} {total:>6.1f} W")
print(f"Efficiency: {(1 - total/rated)*100:.2f}%")
