#!/usr/bin/env python3
"""Power budget simulation for eTR-5000 Tactical SDR."""
components = {
    "Zynq UltraScale+ ZU9EG": 15.0,
    "AD9371 RF transceiver": 4.5,
    "LPDDR4 x2": 2 * 0.8,
    "eMMC": 0.3,
    "RF switches x2": 2 * 0.05,
    "LNAs x2": 2 * 0.15,
    "GbE PHY x4": 4 * 0.18,
}
total = sum(components.values())
print("=" * 55)
print("eTR-5000 Tactical SDR — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w:>6.3f} W")
print("-" * 55)
print(f"{'TOTAL':<40} {total:>6.3f} W")
print(f"28V MIL bus current: {total/28*1000:.0f} mA")
