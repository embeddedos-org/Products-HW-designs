#!/usr/bin/env python3
"""Power budget simulation for ePCU-700 Propulsion Control Unit."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "STM32H743 controller x2": 1.2,
    "ADS131M08 ADC x2": 0.62,
    "RTD conditioning x4": 0.24,
    "Valve driver quiescent x3": 0.9,
    "Valve solenoid drive (6 x 5A peak, 30% duty)": 25.2,
    "MIL-STD-1553B terminal": 0.35,
    "Isolated RS-485 and CAN": 0.55,
    "Analogue reference and housekeeping": 0.6,
}
BUS_V = 28
DCDC_EFFICIENCY = 0.87

total = sum(loads.values())
print("=" * 62)
print("ePCU-700 Propulsion Control Unit — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
