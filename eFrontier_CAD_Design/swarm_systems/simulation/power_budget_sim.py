#!/usr/bin/env python3
"""Duty-cycled power simulation for eSWM-200 Swarm Coordination Node."""
# Per-mode current draw in amps, paired with the fraction of time spent there.
# Duty cycles are expected to sum to 1.0 across a full operating period.
modes = {
    "Mesh listen and neighbour tracking": (0.042, 0.68),
    "UWB ranging exchange": (0.135, 0.22),
    "Consensus round with mesh transmit": (0.21, 0.09),
    "Map fragment sync": (0.18, 0.01),
}
BATTERY_MAH = 2000

print("=" * 62)
print("eSWM-200 Swarm Coordination Node — Power by Mode")
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
print(f"Battery life (2000mAh LiPo): {runtime_h:,.0f} h "
      f"({runtime_h / 24:.1f} days / {runtime_h / 8766:.2f} years)")
