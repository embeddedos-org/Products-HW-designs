#!/usr/bin/env python3
"""Power budget simulation for eVent-Pro ICU Ventilator."""
components = {
    "STM32H7B3 MCU x2": 2 * 0.12,
    "Flow sensors x2": 2 * 0.025,
    "Pressure sensors x4": 4 * 0.005,
    "BLE module": 0.018,
    "Safety co-processors x2": 2 * 0.15,
    "10.1-inch TFT display": 1.2,
    "Blower motor (typical)": 25.0,
    "Solenoid valves x4": 4 * 2.5,
    "Battery charger": 0.05,
}
total = sum(components.values())
print("=" * 55)
print("eVent-Pro Ventilator — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"Battery backup (4h @ {total:.0f}W): {total*4/0.9:.0f} Wh required")
