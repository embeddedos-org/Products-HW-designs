#!/usr/bin/env python3
"""Power budget simulation for eEW-4400 Electronic Warfare Suite."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "ADRV9002 threat receiver x2": 6.8,
    "Zynq UltraScale+ processing": 16.0,
    "AD9265 IF digitiser x4": 4.8,
    "LMX2594 synthesiser x4": 2.8,
    "Ka-band beamformer x2": 7.0,
    "LPDDR4 x2": 2.2,
    "1553B and discrete I/O": 0.65,
    "Housekeeping": 0.9,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.86

total = sum(loads.values())
print("=" * 62)
print("eEW-4400 Electronic Warfare Suite — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
