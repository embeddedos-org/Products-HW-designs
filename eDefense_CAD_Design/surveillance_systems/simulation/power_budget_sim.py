#!/usr/bin/env python3
"""Power budget simulation for eEO-4K Surveillance Camera."""
components = {
    "RK3588S SoC (video encoding)": 10.0,
    "Artix-7 FPGA (image proc)": 3.5,
    "Sony IMX585 sensor": 0.8,
    "4G LTE module (TX)": 1.5,
    "V2X transceiver": 0.8,
    "LPDDR5 x2": 2 * 0.8,
    "eMMC": 0.3,
    "Gimbal motors x3": 3 * 2.0,
}
total = sum(components.values())
print("=" * 55)
print("eEO-4K Surveillance Camera — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"28V MIL bus current: {total/28*1000:.0f} mA")
