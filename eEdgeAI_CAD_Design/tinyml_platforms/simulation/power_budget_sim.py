#!/usr/bin/env python3
"""Duty-cycled power simulation for eTML-100 TinyML Sensor Node."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Always-on listening (hardware VAD)": (3.2e-06, 0.968),
    "Inference burst": (0.0089, 0.03),
    "BLE event report": (0.0062, 0.0018),
    "Model update over BLE": (0.015, 0.0002),
}
BATTERY_MAH = 225

print("=" * 62)
print("eTML-100 TinyML Sensor Node — Power by Mode")
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
print(f"Battery life (CR2032 coin cell): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
