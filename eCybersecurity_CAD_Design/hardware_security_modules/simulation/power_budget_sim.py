#!/usr/bin/env python3
"""Power budget simulation for eHSM-9000 Network HSM."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ crypto engine": 16.0,
    "MAX32520 key custodian x2": 0.44,
    "SE050 key storage x4": 0.18,
    "LPDDR4 x2": 2.2,
    "eMMC x2": 0.6,
    "Tamper monitoring and detection": 0.55,
    "10GbE SFP+ and management PHY": 2.9,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eHSM-9000 Network HSM — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
