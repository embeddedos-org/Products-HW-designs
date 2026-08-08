#!/usr/bin/env python3
"""Power budget simulation for eMIL-100 Qualification Instrumentation."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32H743 controller": 0.6,
    "ADS8688 acquisition x8": 2.64,
    "AD7124 thermocouple x4": 0.36,
    "IEPE conditioning x8": 0.88,
    "Input buffer stage": 0.48,
    "Instrument bridge UARTs": 0.42,
    "Ethernet and isolated RS-485": 1.15,
    "Logging and housekeeping": 0.55,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.88

total = sum(loads.values())
print("=" * 62)
print("eMIL-100 Qualification Instrumentation — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
