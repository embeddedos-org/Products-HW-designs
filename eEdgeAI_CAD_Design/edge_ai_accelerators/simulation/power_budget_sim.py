#!/usr/bin/env python3
"""Power budget simulation for eAI-2000 Edge Inference Module."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Jetson Orin NX (sustained inference)": 25.0,
    "Hailo-8 accelerator": 5.5,
    "LPDDR5 carrier memory": 1.1,
    "eMMC x2": 0.6,
    "2.5GbE PHY": 0.55,
    "Wi-Fi 6 / BLE module": 0.9,
    "Telemetry and housekeeping": 0.45,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eAI-2000 Edge Inference Module — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
