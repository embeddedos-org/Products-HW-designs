#!/usr/bin/env python3
"""Power budget simulation for eECG-12 Diagnostic ECG."""
components = {
    "STM32H7B3 MCU (active)": 0.12,
    "ADS1298 ECG AFE": 0.015,
    "nRF5340 BLE (TX)": 0.018,
    "ESP32-S3 Wi-Fi (TX)": 0.25,
    "Digital isolator": 0.005,
    "7-inch TFT display": 0.8,
    "Touch controller": 0.005,
    "Flash memory": 0.015,
    "Battery charger": 0.02,
}
total = sum(components.values())
battery_mAh = 5000
battery_V = 7.4
runtime_h = (battery_mAh * battery_V / 1000) / total
print("=" * 55)
print("eECG-12 — Power Budget Simulation")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.1f} mW")
print("-" * 55)
print(f"{'TOTAL':<40} {total*1000:>6.1f} mW")
print(f"Battery runtime: {runtime_h:.1f} hours ({battery_mAh}mAh @ {battery_V}V)")
