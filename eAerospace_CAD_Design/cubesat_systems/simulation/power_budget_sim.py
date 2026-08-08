#!/usr/bin/env python3
"""Duty-cycled power simulation for eCUBE-3U CubeSat Avionics."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Eclipse idle (OBC + FRAM only)": (0.045, 0.35),
    "Sunlit nominal (ADCS active)": (0.18, 0.52),
    "Payload acquisition": (0.42, 0.08),
    "UHF downlink burst": (1.25, 0.05),
}
BATTERY_MAH = 7000

print("=" * 62)
print("eCUBE-3U CubeSat Avionics — Power by Mode")
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
print(f"Battery life (2x 18650 at 3500mAh): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
