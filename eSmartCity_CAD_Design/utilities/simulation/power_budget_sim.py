#!/usr/bin/env python3
"""Power budget simulation for eWM-DN50 Smart Water Meter."""
modes = {
    "Deep sleep (RTC only)": 2e-6,
    "MCU active (measurement)": 0.003,
    "Ultrasonic measurement": 0.010,
    "NB-IoT TX": 0.220,
    "LoRaWAN TX": 0.044,
    "LCD update": 0.001,
}
print("=" * 55)
print("eWM-DN50 Smart Water Meter — Power by Mode")
print("=" * 55)
for mode, current_A in modes.items():
    print(f"{mode:<35} {current_A*1e6:>8.1f} µA  ({current_A*3.6*1e6:.1f} µW)")
print()
# Duty cycle: measure every 15 min, NB-IoT uplink every 24h
meas_s = 0.1
nbiot_s = 5
period_s = 15 * 60
daily_periods = 96
avg_I = (modes["Ultrasonic measurement"] * meas_s + modes["Deep sleep (RTC only)"] * (period_s - meas_s)) / period_s
avg_I += modes["NB-IoT TX"] * nbiot_s / (24 * 3600)
battery_Ah = 8.5  # 3.6V D-cell lithium
runtime_years = battery_Ah / (avg_I * 1000 / 1000) / (365 * 24)
print(f"Average current: {avg_I*1e6:.1f} µA")
print(f"Battery runtime (8.5Ah lithium): {runtime_years:.1f} years")
