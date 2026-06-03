#!/usr/bin/env python3
"""Power budget simulation for ePCR-96 Real-time PCR."""
components = {
    "STM32H7B3 MCU": 0.12,
    "Raspberry Pi CM4": 3.5,
    "TEC Peltier modules x4 (heating)": 4 * 15.0,
    "RTD converters x4": 4 * 0.005,
    "H-bridge drivers x4": 4 * 0.05,
    "Photodiodes x4": 4 * 0.002,
    "Excitation LEDs x4": 4 * 0.5,
    "GbE PHY": 0.18,
    "Wi-Fi module": 0.25,
    "24-bit ADC": 0.035,
}
total = sum(components.values())
print("=" * 55)
print("ePCR-96 — Power Budget Simulation")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL (peak heating)':<40} {total:>6.3f} W")
idle = total - 4*15.0 + 4*5.0
print(f"{'TOTAL (idle/cooling)':<40} {idle:>6.3f} W")
