#!/usr/bin/env python3
"""Duty-cycled power simulation for eBRD-600 Unattended Ground Sensor."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Deep sleep (PIR and seismic armed)": (4.2e-05, 0.958),
    "Wake and classify": (0.085, 0.03),
    "mmWave confirmation sweep": (0.31, 0.008),
    "LoRa mesh report": (0.12, 0.003),
    "Satellite backhaul burst": (0.95, 0.001),
}
BATTERY_MAH = 7200

print("=" * 62)
print("eBRD-600 Unattended Ground Sensor — Power by Mode")
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
print(f"Battery life (2x 3.6Ah LiSOCl2 with 5W solar): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
