#!/usr/bin/env python3
"""Power budget simulation for eIoT-Board Industrial IoT Board."""
modes = {
    "Deep sleep (RTC only)": 0.0000012,
    "MCU active (no radio)": 0.005,
    "LoRa RX": 0.0055,
    "LoRa TX (22dBm)": 0.044,
    "BLE TX": 0.0055,
    "All sensors active": 0.003,
}
print("=" * 55)
print("eIoT-Board — Power Budget by Mode")
print("=" * 55)
for mode, current_A in modes.items():
    print(f"{mode:<35} {current_A*1000:>8.4f} mA  ({current_A*3.3*1000:.3f} mW)")
print()
# Duty cycle example: LoRa uplink every 10 min
tx_time_s = 0.5
period_s = 600
avg_current = (modes["LoRa TX (22dBm)"] * tx_time_s + modes["Deep sleep (RTC only)"] * (period_s - tx_time_s)) / period_s
battery_mAh = 2000
runtime_days = battery_mAh / (avg_current * 1000) / 24
print(f"Average current (LoRa 10-min interval): {avg_current*1e6:.1f} µA")
print(f"Battery runtime (2000mAh AA): {runtime_days:.0f} days ({runtime_days/365:.1f} years)")
