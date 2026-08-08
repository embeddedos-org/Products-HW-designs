#!/usr/bin/env python3
"""Power budget simulation for eNPU-800 FPGA Neural Fabric."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Zynq UltraScale+ fabric at full utilisation": 18.5,
    "LPDDR4 x4": 4.4,
    "eMMC and boot flash": 0.42,
    "Gigabit Ethernet PHY": 0.45,
    "Clock generation": 1.1,
    "Telemetry and housekeeping": 0.5,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.9

total = sum(loads.values())
print("=" * 62)
print("eNPU-800 FPGA Neural Fabric — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
