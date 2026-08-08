#!/usr/bin/env python3
"""Duty-cycled power simulation for eCS-200 Civic Sensing Node."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Sleep between measurement cycles": (0.00028, 0.76),
    "Air quality measurement": (0.145, 0.18),
    "Noise and pedestrian sensing": (0.092, 0.055),
    "LoRaWAN and NB-IoT reporting": (0.22, 0.005),
}
BATTERY_MAH = 14000

print("=" * 62)
print("eCS-200 Civic Sensing Node — Power by Mode")
print("=" * 62)
for name, (amps, duty) in modes.items():
    print(f"{name:<38} {amps * 1000:>10.3f} mA  @ {duty:>6.2%}")

duty_total = sum(duty for _, duty in modes.values())
if abs(duty_total - 1.0) > 0.001:
    print(f"\nWARNING: duty cycles sum to {duty_total:.3f}, not 1.000")

average_a = sum(amps * duty for amps, duty in modes.values())
runtime_h = BATTERY_MAH / (average_a * 1000)
print("-" * 62)
print(f"{'AVERAGE CURRENT':<38} {average_a * 1000:>10.3f} mA")
print(f"Battery life (4x 3500mAh Li-ion with 10W solar): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
