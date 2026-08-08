#!/usr/bin/env python3
"""Duty-cycled power simulation for eSLD-300 Soldier Computer."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Standby (GNSS fix, mesh listen)": (0.062, 0.62),
    "Active display and messaging": (0.48, 0.22),
    "Map rendering and NPU detection": (1.15, 0.11),
    "Mesh transmit burst": (1.8, 0.05),
}
BATTERY_MAH = 8000

print("=" * 62)
print("eSLD-300 Soldier Computer — Power by Mode")
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
print(f"Battery life (4x 2000mAh LiPo): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
