#!/usr/bin/env python3
"""Power budget simulation for eHSM-Pro Hardware Security Module."""
components = {
    "NXP LS1046A SoC": 8.0,
    "DDR4 ECC x4": 4 * 0.4,
    "eMMC": 0.2,
    "GbE PHY x4": 4 * 0.18,
    "Crypto co-processor": 0.001,
    "Tamper detection circuit": 0.005,
    "Battery-backed SRAM": 0.001,
    "USB-C PD controller": 0.05,
}
total = sum(components.values())
print("=" * 55)
print("eHSM-Pro Hardware Security Module — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"12V input current: {total/12*1000:.0f} mA")
print(f"Crypto throughput: AES-256 @ 10 Gbps hardware")
