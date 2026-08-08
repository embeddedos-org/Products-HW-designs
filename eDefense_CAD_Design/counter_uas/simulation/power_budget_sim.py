#!/usr/bin/env python3
"""Power budget simulation for eCUAS-900 Counter-UAS Node."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ADRV9002 RF detection x2": 6.8,
    "IWR6843 mmWave radar x2": 4.0,
    "Jetson Orin Nano inference": 12.0,
    "ESP32-C6 Remote ID x2": 0.6,
    "LMX2594 synthesiser x2": 1.4,
    "HMC7044 clock tree": 1.1,
    "LPDDR4 x2": 2.2,
    "Ethernet and housekeeping": 1.4,
}
BUS_V = 24
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("eCUAS-900 Counter-UAS Node — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
