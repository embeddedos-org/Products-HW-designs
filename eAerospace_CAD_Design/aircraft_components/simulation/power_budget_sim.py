#!/usr/bin/env python3
"""Power budget simulation for Aircraft Components embedded controller."""
import json

components = {
    "STM32H7B3 MCU (active)": 120e-3,
    "CAN FD transceivers x2": 2 * 12e-3,
    "ARINC-429 Rx": 25e-3,
    "ARINC-429 Tx": 30e-3,
    "Strain gauge amps x4": 4 * 1.2e-3,
    "Accelerometers x2": 2 * 2.0e-3,
    "RTD converters x4": 4 * 5.5e-3,
    "Flash memory": 15e-3,
    "Crypto co-processor": 1.5e-3,
    "LDO regulator quiescent": 2.0e-3,
}

vcc = 3.3
total_mA = sum(v * 1000 for v in components.values())
total_W = sum(components.values()) * vcc

print("=" * 55)
print("Aircraft Components — Power Budget Simulation")
print("=" * 55)
print(f"{'Component':<35} {'Current (mA)':>12}")
print("-" * 55)
for name, current in components.items():
    print(f"{name:<35} {current*1000:>12.2f}")
print("-" * 55)
print(f"{'TOTAL':<35} {total_mA:>12.2f}")
print(f"Power @ {vcc}V: {total_W*1000:.1f} mW")
print(f"Power @ 28V bus (with 85% DCDC): {total_W/0.85*1000:.1f} mW")

result = {"total_current_mA": round(total_mA, 2), "power_mW_at_3v3": round(total_W*1000, 1)}
print("\nJSON:", json.dumps(result, indent=2))
