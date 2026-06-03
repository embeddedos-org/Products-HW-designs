#!/usr/bin/env python3
"""Power budget simulation for eSM-3P Smart Electricity Meter."""
components = {
    "STM32L4R9 MCU (active)": 0.010,
    "STM32WL55 (LoRaWAN TX)": 0.040,
    "ADE9153A metering IC": 0.008,
    "OFDM PLC modem": 0.150,
    "LCD display": 0.002,
    "Crypto co-processor": 0.001,
    "AC-DC power module loss": 0.300,
}
total = sum(components.values())
print("=" * 55)
print("eSM-3P Smart Electricity Meter — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.1f} mW")
print("-" * 55)
print(f"{'TOTAL':<40} {total*1000:>6.1f} mW")
print(f"Annual energy: {total * 8760 / 1000:.2f} kWh")
