#!/usr/bin/env python3
"""Power budget simulation for eTS-200 Industrial Temperature Sensor."""
components = {
    "STM32L4R9 MCU (active)": 0.010,
    "STM32L4R9 MCU (sleep)": 0.000002,
    "AD7124-8 ADC": 0.001,
    "HART modem": 0.008,
    "RTD converter": 0.005,
    "Voltage reference": 0.001,
    "LDO regulator": 0.002,
}
total_active = sum(components.values())
loop_voltage = 24  # V
loop_current_mA = 12  # mA typical operating point
loop_power = loop_voltage * loop_current_mA / 1000
print("=" * 55)
print("eTS-200 Temperature Sensor — Power Budget")
print("=" * 55)
for name, w in components.items():
    print(f"{name:<40} {w*1000:>6.2f} mW")
print("-" * 55)
print(f"{'TOTAL electronics':<40} {total_active*1000:>6.2f} mW")
print(f"Loop power available @ 12mA/24V: {loop_power*1000:.0f} mW")
print(f"Margin: {(loop_power - total_active)*1000:.0f} mW")
