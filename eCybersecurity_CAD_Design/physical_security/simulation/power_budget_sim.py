#!/usr/bin/env python3
"""Power budget simulation for eAccess-Pro Smart Access Control."""
components = {
    "STM32H7B3 MCU (active)": 0.12,
    "BLE + NFC SoC": 0.018,
    "NFC/RFID controller": 0.05,
    "GbE PHY": 0.18,
    "RS-485 transceiver": 0.01,
    "Door lock relay": 0.5,
    "Buzzer + LEDs": 0.1,
}
total = sum(components.values())
poe_budget = 30.0  # PoE+ 802.3at
print("=" * 55)
print("eAccess-Pro Smart Access Control — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.1f} mW")
print("-" * 55)
print(f"{'TOTAL':<40} {total*1000:>6.1f} mW")
print(f"PoE+ budget: {poe_budget*1000:.0f} mW available")
print(f"PoE+ margin: {(poe_budget - total)*1000:.0f} mW")
