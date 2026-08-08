#!/usr/bin/env python3
"""Power budget simulation for eSLM-700 SLAM Compute Module."""
# Continuous load per subsystem, in watts, at the stated operating point.
loads = {
    "Jetson Orin Nano SLAM pipeline": 12.0,
    "Stereo camera pair": 1.6,
    "RPLIDAR S3 scanner": 3.5,
    "ADIS16470 IMU": 0.21,
    "iCE40 sync FPGA": 0.18,
    "LPDDR4 map memory": 1.1,
    "Ethernet and USB": 1.35,
}
BUS_V = 12
DCDC_EFFICIENCY = 0.89

total = sum(loads.values())
print("=" * 62)
print("eSLM-700 SLAM Compute Module — Power Budget")
print("=" * 62)
for name, watts in loads.items():
    print(f"{name:<44} {watts:>7.3f} W")
print("-" * 62)
print(f"{'TOTAL':<44} {total:>7.3f} W")
print(f"{BUS_V}V bus current: {total / BUS_V * 1000:.0f} mA")
print(f"Input power at {DCDC_EFFICIENCY:.0%} DC-DC efficiency: {total / DCDC_EFFICIENCY:.2f} W")
