#!/usr/bin/env python3
"""Power budget simulation for ePHO-800 Photonics Control Platform."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq-7020 control processor": 4.5,
    "DFB laser drive x4": 6.4,
    "TEC controller x4 (steady state)": 12.0,
    "Electro-optic modulator drive x2": 3.2,
    "APD bias and TIA x8": 2.4,
    "Precision measurement chain": 0.72,
    "Ethernet and housekeeping": 1.35,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("ePHO-800 Photonics Control Platform — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
