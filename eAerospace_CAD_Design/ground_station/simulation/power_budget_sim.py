#!/usr/bin/env python3
"""Power budget simulation for eGS-1200 SDR Ground Station Modem."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ADRV9002 RF transceiver": 3.4,
    "Zynq UltraScale+ XCZU3EG": 11.5,
    "LMX2594 synthesiser x2": 1.4,
    "HMC7044 clock distribution": 1.1,
    "10MHz OCXO": 1.8,
    "ZED-F9T timing GNSS": 0.28,
    "LPDDR4 x2": 2.2,
    "Gigabit Ethernet PHY x2": 0.9,
    "SFP+ modules x2": 2.0,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eGS-1200 SDR Ground Station Modem — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
