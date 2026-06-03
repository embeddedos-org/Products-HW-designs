#!/usr/bin/env python3
"""Power budget simulation for eWatch-Pro Smart Watch."""
modes = {
    "Deep sleep (RTC + accel)": 0.000010,
    "Watch face update": 0.005,
    "BLE connected (no data)": 0.003,
    "BLE data transfer": 0.010,
    "ECG measurement (30s)": 0.008,
    "SpO2 measurement (15s)": 0.012,
    "GPS active": 0.135,
    "AMOLED display (50% brightness)": 0.030,
}
battery_mAh = 420
battery_V = 3.7
print("=" * 55)
print("eWatch-Pro Smart Watch — Power by Mode")
print("=" * 55)
for mode, current_A in modes.items():
    print(f"{mode:<40} {current_A*1000:>6.2f} mA")
print()
# Typical day: mostly sleep + BLE + display + hourly ECG
avg_I = (
    modes["Deep sleep (RTC + accel)"] * 0.90 +
    modes["AMOLED display (50% brightness)"] * 0.05 +
    modes["BLE connected (no data)"] * 0.04 +
    modes["ECG measurement (30s)"] * (30/3600) * 24 / 24
)
runtime_days = battery_mAh / (avg_I * 1000) / 24
print(f"Average current (typical use): {avg_I*1000:.3f} mA")
print(f"Battery runtime: {runtime_days:.1f} days ({battery_mAh}mAh @ {battery_V}V)")
