#!/usr/bin/env python3
"""Power budget simulation for eTLM-600 Telemetry Encoder."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Artix-7 PCM encoder FPGA": 2.1,
    "STM32H743 housekeeping": 0.6,
    "ADS8688 acquisition x16": 5.28,
    "S-band transmitter (10W RF)": 26.0,
    "LMX2594 synthesiser": 0.7,
    "1553B / ARINC-429 monitors": 0.85,
    "DDR4 frame buffer": 0.8,
    "Analogue reference and housekeeping": 0.9,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.85

total = sum(loads.values())
print("=" * 62)
print("eTLM-600 Telemetry Encoder — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
