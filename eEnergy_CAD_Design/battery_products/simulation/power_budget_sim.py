#!/usr/bin/env python3
"""Power budget simulation for eBMS-100A Battery Management System."""
components = {
    "STM32G474 MCU": 0.08,
    "LTC6813 cell monitors x2": 2 * 0.025,
    "INA3221 power monitors x4": 4 * 0.002,
    "BQ40Z80 fuel gauge": 0.005,
    "CAN FD transceiver": 0.04,
    "RS-485 transceiver": 0.01,
    "BLE module": 0.018,
    "Active cell balancers x18": 18 * 0.002,
}
total = sum(components.values())
print("=" * 55)
print("eBMS-100A Battery Management System — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.1f} mW")
print("-" * 55)
print(f"{'TOTAL':<40} {total*1000:>6.1f} mW")
print(f"Quiescent current @ 48V: {total/48*1000:.1f} mA")
