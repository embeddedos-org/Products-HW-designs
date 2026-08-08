#!/usr/bin/env python3
"""Power budget simulation for eVIS-600 Multi-Camera Vision Processor."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "i.MX 8M Plus with NPU active": 8.5,
    "Global-shutter sensor x4": 3.2,
    "iCE40 frame sync FPGA": 0.18,
    "LPDDR4 x2": 2.2,
    "IR strobe (850nm, 20% duty)": 3.6,
    "GigE and USB 3.0": 1.35,
    "Housekeeping": 0.4,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eVIS-600 Multi-Camera Vision Processor — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
