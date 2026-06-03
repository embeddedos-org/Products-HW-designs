#!/usr/bin/env python3
"""Power budget simulation for eGasDetect-4 4-Gas Detector."""
modes = {
    "Deep sleep (sensors warm)": 0.0008,
    "MCU active (measurement)": 0.005,
    "BLE advertising": 0.003,
    "BLE connected + data TX": 0.010,
    "Alarm (buzzer + vibration)": 0.150,
    "2.4-inch TFT display": 0.080,
}
print("=" * 55)
print("eGasDetect-4 — Power by Mode")
print("=" * 55)
for mode, current_A in modes.items():
    print(f"{mode:<40} {current_A*1000:>6.1f} mA")
print()
# Typical: sensors always warm, measure every 5s, BLE advertising
sensor_warmup = 0.0008
meas_duty = modes["MCU active (measurement)"] * (0.1 / 5)
ble_duty = modes["BLE advertising"] * 0.1
display_duty = modes["2.4-inch TFT display"] * 0.3
avg_I = sensor_warmup + meas_duty + ble_duty + display_duty
battery_mAh = 3600
runtime_h = battery_mAh / (avg_I * 1000)
print(f"Average current (typical use): {avg_I*1000:.2f} mA")
print(f"Battery runtime (3600mAh LiSOCl2): {runtime_h:.0f} hours ({runtime_h/24/365:.1f} years)")
