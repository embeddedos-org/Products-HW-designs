#!/usr/bin/env python3
"""Duty-cycled power simulation for eDIS-600 Disaster Early-Warning Node."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Continuous seismic monitoring": (0.0085, 0.978),
    "Meteorological sample and log": (0.032, 0.02),
    "LoRa and cellular alert": (0.24, 0.0015),
    "Satellite alert burst": (0.95, 0.0005),
}
BATTERY_MAH = 14400

print("=" * 62)
print("eDIS-600 Disaster Early-Warning Node — Power by Mode")
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
print(f"Battery life (4x 3.6Ah LiSOCl2 with 10W solar): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
